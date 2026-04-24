from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.data.catalogs import all_series
from realtime_gdp_nowcast.data.time import combine_date_time, parse_alfred_vintage_column, period_to_quarter_label
from realtime_gdp_nowcast.io import write_table

LOGGER = logging.getLogger(__name__)

DEFAULT_TIME_BY_SOURCE = {
    "BEA": "08:30",
    "BLS": "08:30",
    "CENSUS": "08:30",
    "CENSUS_PROXY": "08:30",
    "FED_G17": "09:15",
    "ISM": "10:00",
    "MICHIGAN": "10:00",
}


def _normalize_quarter_label(value: str) -> str:
    return str(value).strip().replace(":", "")


def _default_release_time(source_family: str, series_id: str) -> tuple[str, str]:
    source_family = str(source_family or "").strip().upper()
    if series_id == "UMCSENT":
        return "10:00", "assumed_from_michigan_default"
    if source_family in DEFAULT_TIME_BY_SOURCE:
        return DEFAULT_TIME_BY_SOURCE[source_family], "assumed_from_source_default"
    return "23:59", "assumed_from_vintage_day_end"


def _build_series_release_calendar(settings: ProjectSettings, silver_calendar: pd.DataFrame) -> pd.DataFrame:
    series_df = all_series(settings)
    mapped_series = series_df[series_df["release_calendar_id"] != "currently_unmapped"].copy()
    release_rows = silver_calendar.copy()
    release_rows["public_release_date"] = pd.to_datetime(release_rows["release_date"])

    expanded_rows: list[dict[str, object]] = []
    for _, series_row in mapped_series.iterrows():
        block_rows = release_rows[release_rows["release_block"] == series_row["release_calendar_id"]]
        for calendar_row in block_rows.itertuples(index=False):
            time_text = calendar_row.release_time_et
            timing_assumption = "from_stage2_calendar"
            if pd.isna(time_text) or str(time_text).strip() == "":
                time_text, timing_assumption = _default_release_time(calendar_row.source_family, series_row["series_id"])
            expanded_rows.append(
                {
                    "series_id": series_row["series_id"],
                    "release_block": calendar_row.release_block,
                    "public_release_date": pd.Timestamp(calendar_row.public_release_date).normalize(),
                    "public_release_time_et": time_text,
                    "agency": calendar_row.source_family,
                    "reference_period": calendar_row.reference_period_label,
                    "release_round": "standard",
                    "source_type": calendar_row.source_type,
                    "release_time_status": calendar_row.release_time_status,
                    "proxy_method": calendar_row.proxy_method,
                    "timing_assumption": timing_assumption,
                    "provenance_file": calendar_row.provenance_file,
                }
            )

    calendar = pd.DataFrame(expanded_rows)
    if calendar.empty:
        return calendar
    calendar["public_release_timestamp_et"] = calendar.apply(
        lambda row: combine_date_time(
            row["public_release_date"],
            row["public_release_time_et"],
            settings.project["timezone"],
        ),
        axis=1,
    )
    return calendar.drop_duplicates(
        subset=["series_id", "public_release_date", "public_release_time_et", "release_block"]
    )


def _infer_gdp_release_rows(settings: ProjectSettings, gdpc1_path: Path) -> pd.DataFrame:
    wide = pd.read_csv(gdpc1_path, na_values=["."])
    burn_in_start = pd.Period(settings.sample["burn_in_start_quarter"], freq="Q-DEC")
    backtest_end = pd.Period(settings.sample["backtest_end_quarter"], freq="Q-DEC")
    vintage_columns: list[tuple[pd.Timestamp, str]] = []
    for column in wide.columns[1:]:
        vintage_date = parse_alfred_vintage_column(column)
        if vintage_date is not None:
            vintage_columns.append((vintage_date.normalize(), column))
    vintage_columns = sorted(set(vintage_columns))

    rows: list[dict[str, object]] = []
    for record in wide.itertuples(index=False):
        target_quarter = pd.Period(pd.Timestamp(record.date), freq="Q-DEC")
        if target_quarter < burn_in_start or target_quarter > backtest_end:
            continue
        target_quarter_label = period_to_quarter_label(target_quarter)
        target_quarter_end = target_quarter.asfreq("M", how="end").to_timestamp(how="end").normalize()
        observed_dates = [
            vintage_date
            for vintage_date, column in vintage_columns
            if target_quarter_end < vintage_date <= target_quarter_end + pd.Timedelta(days=120) and pd.notna(getattr(record, column))
        ]
        first_three = observed_dates[:3]
        if len(first_three) < 3:
            continue
        for release_round, release_date in zip(["advance", "second", "third"], first_three):
            rows.append(
                {
                    "series_id": settings.project["gdp_release_proxy_series_id"],
                    "release_block": "gdp",
                    "public_release_date": release_date,
                    "public_release_time_et": "08:30",
                    "agency": "BEA",
                    "reference_period": target_quarter_label,
                    "release_round": release_round,
                    "source_type": "inferred_from_gdpc1_vintages",
                    "release_time_status": "assumed_from_source_default",
                    "proxy_method": "alfred_vintage_first_three_after_quarter_end",
                    "timing_assumption": "inferred_release_date_assumed_bea_time",
                    "provenance_file": str(gdpc1_path.relative_to(settings.paths.root)),
                }
            )

    calendar = pd.DataFrame(rows).drop_duplicates(
        subset=["series_id", "reference_period", "release_round", "public_release_date"]
    )
    if calendar.empty:
        return calendar
    calendar["public_release_timestamp_et"] = calendar.apply(
        lambda row: combine_date_time(
            row["public_release_date"],
            row["public_release_time_et"],
            settings.project["timezone"],
        ),
        axis=1,
    )
    return calendar


def build_release_calendar(settings: ProjectSettings) -> pd.DataFrame:
    silver_calendar_path = settings.paths.silver_data / "calendars" / "release_calendar_silver.csv"
    gdpc1_path = settings.paths.raw_data / "alfred" / "series_observations" / "GDPC1.csv"
    if not silver_calendar_path.exists() or not gdpc1_path.exists():
        raise FileNotFoundError("Missing Stage 2 calendar inputs or GDPC1 raw vintages.")

    silver_calendar = pd.read_csv(silver_calendar_path)
    series_calendar = _build_series_release_calendar(settings, silver_calendar)
    gdp_calendar = _infer_gdp_release_rows(settings, gdpc1_path)
    calendar = pd.concat([series_calendar, gdp_calendar], ignore_index=True)
    if calendar.empty:
        raise RuntimeError("Processed release calendar is empty. Stage 3 cannot continue.")

    if "reference_period" in calendar.columns:
        mask = calendar["reference_period"].notna() & calendar["reference_period"].astype(str).str.contains(":Q")
        calendar.loc[mask, "reference_period"] = calendar.loc[mask, "reference_period"].map(_normalize_quarter_label)

    calendar = calendar.sort_values(
        ["series_id", "public_release_timestamp_et", "reference_period", "release_round"]
    ).reset_index(drop=True)
    write_table(calendar, settings.paths.processed_data / "release_calendar.parquet")
    write_table(calendar, settings.paths.processed_data / "release_calendar.csv")

    inferred_only = calendar[calendar["series_id"] == settings.project["gdp_release_proxy_series_id"]].copy()
    write_table(inferred_only, settings.paths.interim_data / "gdp_release_calendar_inferred.csv")
    LOGGER.info("Built processed release calendar with %s rows", len(calendar))
    return calendar
