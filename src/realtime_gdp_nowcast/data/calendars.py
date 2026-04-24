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

BRONZE_FIRST_RELEASE_USECOLS = [
    "series_id",
    "observation_date",
    "realtime_start",
    "value_numeric",
    "is_missing_value",
]

BRONZE_FIRST_RELEASE_DTYPES = {
    "series_id": "string",
    "observation_date": "string",
    "realtime_start": "string",
    "value_numeric": "string",
    "is_missing_value": "string",
}


def _display_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def _normalize_quarter_label(value: str) -> str:
    return str(value).strip().replace(":", "")


def _default_release_time(source_family: str, series_id: str) -> tuple[str, str]:
    source_family = str(source_family or "").strip().upper()
    if series_id == "UMCSENT":
        return "10:00", "assumed_from_michigan_default"
    if source_family in DEFAULT_TIME_BY_SOURCE:
        return DEFAULT_TIME_BY_SOURCE[source_family], "assumed_from_source_default"
    return "23:59", "assumed_from_vintage_day_end"


def _proxy_release_blocks(settings: ProjectSettings) -> set[str]:
    configured = settings.get("project", "census_proxy_release_blocks", default=[])
    return {str(value).strip() for value in configured if str(value).strip()}


def _build_series_release_calendar(
    settings: ProjectSettings,
    silver_calendar: pd.DataFrame,
    excluded_release_blocks: set[str] | None = None,
) -> pd.DataFrame:
    series_df = all_series(settings)
    mapped_series = series_df[series_df["release_calendar_id"] != "currently_unmapped"].copy()
    release_rows = silver_calendar.copy()
    if excluded_release_blocks:
        release_rows = release_rows[~release_rows["release_block"].isin(excluded_release_blocks)].copy()
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


def _load_bronze_first_release_candidates(settings: ProjectSettings, series_ids: list[str]) -> pd.DataFrame:
    bronze_path = settings.paths.bronze_data / "indicators" / "alfred_monthly_long.csv"
    if not bronze_path.exists():
        LOGGER.warning("Bronze ALFRED long file missing; cannot build Census first-release proxy calendar.")
        return pd.DataFrame(columns=["series_id", "observation_date", "realtime_start"])

    grouped_chunks: list[pd.DataFrame] = []
    for chunk in pd.read_csv(
        bronze_path,
        usecols=BRONZE_FIRST_RELEASE_USECOLS,
        dtype=BRONZE_FIRST_RELEASE_DTYPES,
        chunksize=500_000,
        low_memory=False,
    ):
        filtered = chunk[chunk["series_id"].isin(series_ids)].copy()
        if filtered.empty:
            continue
        filtered = filtered[filtered["is_missing_value"].astype(str).str.lower() != "true"]
        filtered["observation_date"] = pd.to_datetime(filtered["observation_date"], errors="coerce")
        filtered["realtime_start"] = pd.to_datetime(filtered["realtime_start"], errors="coerce")
        filtered["value_numeric"] = pd.to_numeric(filtered["value_numeric"], errors="coerce")
        filtered = filtered.dropna(subset=["series_id", "observation_date", "realtime_start", "value_numeric"])
        first_release = _infer_first_release_candidates(filtered)
        grouped_chunks.append(first_release)

    if not grouped_chunks:
        return pd.DataFrame(columns=["series_id", "observation_date", "realtime_start"])
    combined = pd.concat(grouped_chunks, ignore_index=True)
    return (
        _infer_first_release_candidates(combined)
        .sort_values(["series_id", "observation_date"])
        .reset_index(drop=True)
    )


def _infer_first_release_candidates(frame: pd.DataFrame) -> pd.DataFrame:
    return frame.groupby(["series_id", "observation_date"], as_index=False)["realtime_start"].min()


def _infer_census_first_release_proxy_calendar(settings: ProjectSettings) -> pd.DataFrame:
    series_df = all_series(settings)
    proxy_blocks = _proxy_release_blocks(settings)
    proxy_series = series_df[series_df["release_calendar_id"].isin(proxy_blocks)].copy()
    if proxy_series.empty:
        return pd.DataFrame()

    first_release = _load_bronze_first_release_candidates(settings, proxy_series["series_id"].tolist())
    if first_release.empty:
        return pd.DataFrame()

    first_release = first_release.merge(
        proxy_series[["series_id", "release_calendar_id"]],
        on="series_id",
        how="left",
    )
    release_time = str(settings.get("project", "census_proxy_first_release_time_et", default="08:30"))
    bronze_path = settings.paths.bronze_data / "indicators" / "alfred_monthly_long.csv"
    provenance_file = _display_path(bronze_path, settings.paths.root)

    calendar = first_release.rename(columns={"release_calendar_id": "release_block"}).copy()
    calendar["observation_date"] = calendar["observation_date"].dt.normalize()
    calendar["public_release_date"] = calendar["realtime_start"].dt.normalize()
    calendar["public_release_time_et"] = release_time
    calendar["agency"] = "CENSUS_PROXY"
    calendar["reference_period"] = pd.PeriodIndex(calendar["observation_date"], freq="M").astype(str)
    calendar["release_round"] = "standard"
    calendar["source_type"] = "proxy_first_release_from_alfred"
    calendar["release_time_status"] = "assumed_from_source_default"
    calendar["proxy_method"] = "alfred_first_observed_vintage"
    calendar["timing_assumption"] = "alfred_first_release_proxy_assumed_census_time"
    calendar["provenance_file"] = provenance_file
    calendar["public_release_timestamp_et"] = calendar.apply(
        lambda row: combine_date_time(
            row["public_release_date"],
            row["public_release_time_et"],
            settings.project["timezone"],
        ),
        axis=1,
    )
    calendar = calendar[
        [
            "series_id",
            "observation_date",
            "release_block",
            "public_release_date",
            "public_release_time_et",
            "agency",
            "reference_period",
            "release_round",
            "source_type",
            "release_time_status",
            "proxy_method",
            "timing_assumption",
            "provenance_file",
            "public_release_timestamp_et",
        ]
    ].drop_duplicates(subset=["series_id", "reference_period", "public_release_date"])

    write_table(calendar, settings.paths.interim_data / "census_first_release_proxy_calendar.parquet")
    write_table(calendar, settings.paths.interim_data / "census_first_release_proxy_calendar.csv")
    LOGGER.info(
        "Built Census first-release proxy calendar with %s rows across %s series",
        len(calendar),
        calendar["series_id"].nunique(),
    )
    return calendar


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
                    "provenance_file": _display_path(gdpc1_path, settings.paths.root),
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
    census_proxy_calendar = _infer_census_first_release_proxy_calendar(settings)
    excluded_proxy_blocks = _proxy_release_blocks(settings) if not census_proxy_calendar.empty else set()
    series_calendar = _build_series_release_calendar(settings, silver_calendar, excluded_release_blocks=excluded_proxy_blocks)
    gdp_calendar = _infer_gdp_release_rows(settings, gdpc1_path)
    calendar = pd.concat([series_calendar, census_proxy_calendar, gdp_calendar], ignore_index=True)
    if calendar.empty:
        raise RuntimeError("Processed release calendar is empty. Stage 3 cannot continue.")

    if "observation_date" not in calendar.columns:
        calendar["observation_date"] = pd.NaT

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
