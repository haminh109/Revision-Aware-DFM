from __future__ import annotations

import logging

import pandas as pd

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.data.catalogs import all_series
from realtime_gdp_nowcast.data.time import combine_date_time
from realtime_gdp_nowcast.io import write_table

LOGGER = logging.getLogger(__name__)

UNMAPPED_TIME_BY_SERIES = {
    "UMCSENT": "10:00",
    "FEDFUNDS": "23:59",
    "GS10": "23:59",
    "T10Y3MM": "23:59",
}

BRONZE_EVENT_DTYPES = {
    "series_id": "string",
    "observation_date": "string",
    "realtime_start": "string",
    "value_raw": "string",
    "value_numeric": "string",
    "is_missing_value": "string",
}


def _load_bronze_indicator_long(settings: ProjectSettings, series_ids: list[str]) -> pd.DataFrame:
    bronze_path = settings.paths.bronze_data / "indicators" / "alfred_monthly_long.csv"
    if not bronze_path.exists():
        raise FileNotFoundError("Missing Stage 1 bronze indicator file.")

    chunks: list[pd.DataFrame] = []
    usecols = [
        "series_id",
        "observation_date",
        "realtime_start",
        "value_raw",
        "value_numeric",
        "is_missing_value",
    ]
    for chunk in pd.read_csv(
        bronze_path,
        usecols=usecols,
        dtype=BRONZE_EVENT_DTYPES,
        chunksize=500_000,
        low_memory=False,
    ):
        filtered = chunk[chunk["series_id"].isin(series_ids)].copy()
        if filtered.empty:
            continue
        filtered = filtered[filtered["is_missing_value"].astype(str).str.lower() != "true"]
        filtered["observation_date"] = pd.to_datetime(filtered["observation_date"])
        filtered["realtime_start"] = pd.to_datetime(filtered["realtime_start"])
        filtered["value_numeric"] = pd.to_numeric(filtered["value_numeric"], errors="coerce")
        filtered = filtered.dropna(subset=["observation_date", "realtime_start", "value_numeric"])
        chunks.append(filtered)

    if not chunks:
        return pd.DataFrame(columns=usecols)
    return pd.concat(chunks, ignore_index=True)


def build_event_panel(settings: ProjectSettings) -> pd.DataFrame:
    calendar_path = settings.paths.processed_data / "release_calendar.parquet"
    if not calendar_path.exists():
        raise FileNotFoundError("Missing processed release calendar. Run `build-calendars` first.")

    release_calendar = pd.read_parquet(calendar_path)
    release_calendar["public_release_date"] = pd.to_datetime(release_calendar["public_release_date"]).dt.normalize()
    if "observation_date" in release_calendar.columns:
        release_calendar["observation_date"] = pd.to_datetime(release_calendar["observation_date"], errors="coerce")
    series_df = all_series(settings)
    raw_events = _load_bronze_indicator_long(settings, series_df["series_id"].tolist())
    if raw_events.empty:
        raise RuntimeError("No bronze indicator events were loaded for the configured series catalog.")

    raw_events = raw_events[raw_events["observation_date"] >= pd.Timestamp(settings.sample["ingest_start"])].copy()
    raw_events["vintage_date"] = raw_events["realtime_start"].dt.normalize()
    raw_events = raw_events.merge(series_df, on="series_id", how="left")
    calendar_columns = [
        "series_id",
        "release_block",
        "public_release_date",
        "public_release_time_et",
        "source_type",
        "timing_assumption",
        "release_time_status",
    ]
    if "observation_date" in release_calendar.columns:
        calendar_columns.insert(1, "observation_date")

    if "observation_date" in release_calendar.columns:
        specific_calendar = release_calendar[release_calendar["observation_date"].notna()].copy()
        generic_calendar = release_calendar[release_calendar["observation_date"].isna()].copy()
    else:
        specific_calendar = pd.DataFrame(columns=calendar_columns)
        generic_calendar = release_calendar.copy()

    enriched = raw_events.copy()
    if not specific_calendar.empty:
        enriched = enriched.merge(
            specific_calendar[calendar_columns].rename(columns={"observation_date": "calendar_observation_date"}),
            left_on=["series_id", "vintage_date", "observation_date"],
            right_on=["series_id", "public_release_date", "calendar_observation_date"],
            how="left",
            suffixes=("", "_specific"),
        )
    else:
        enriched["calendar_observation_date"] = pd.NaT
        for column in ["release_block", "public_release_time_et", "source_type", "timing_assumption", "release_time_status"]:
            enriched[column] = pd.NA

    enriched = enriched.merge(
        generic_calendar[[column for column in calendar_columns if column != "observation_date"]].rename(
            columns={column: f"{column}_generic" for column in calendar_columns if column not in {"series_id", "observation_date"}}
        ),
        left_on=["series_id", "vintage_date"],
        right_on=["series_id", "public_release_date_generic"],
        how="left",
    )

    for column in ["release_block", "public_release_time_et", "source_type", "timing_assumption", "release_time_status"]:
        generic_column = f"{column}_generic"
        if generic_column in enriched.columns:
            enriched[column] = enriched[column].combine_first(enriched[generic_column])
    if "public_release_date_generic" in enriched.columns:
        enriched = enriched.drop(columns=["public_release_date_generic"])
    drop_columns = [
        column
        for column in [
            "calendar_observation_date",
            "release_block_generic",
            "public_release_time_et_generic",
            "source_type_generic",
            "timing_assumption_generic",
            "release_time_status_generic",
        ]
        if column in enriched.columns
    ]
    if drop_columns:
        enriched = enriched.drop(columns=drop_columns)

    unmapped_mask = enriched["public_release_time_et"].isna()
    if unmapped_mask.any():
        enriched.loc[unmapped_mask, "public_release_time_et"] = enriched.loc[unmapped_mask, "series_id"].map(
            UNMAPPED_TIME_BY_SERIES
        ).fillna("23:59")
        enriched.loc[unmapped_mask, "source_type"] = enriched.loc[unmapped_mask, "source_type"].fillna(
            "alfred_vintage_proxy"
        )
        enriched.loc[unmapped_mask, "timing_assumption"] = enriched.loc[unmapped_mask, "timing_assumption"].fillna(
            "fallback_to_alfred_vintage_date"
        )
        enriched.loc[unmapped_mask, "release_time_status"] = enriched.loc[unmapped_mask, "release_time_status"].fillna(
            "assumed_from_vintage_day"
        )
        enriched.loc[unmapped_mask, "release_block"] = enriched.loc[unmapped_mask, "release_block"].fillna(
            enriched.loc[unmapped_mask, "release_calendar_id"]
        )

    enriched["public_release_timestamp_et"] = enriched.apply(
        lambda row: combine_date_time(
            row["vintage_date"],
            row["public_release_time_et"],
            settings.project["timezone"],
        ),
        axis=1,
    )
    enriched["available_flag"] = 1
    event_panel = enriched.copy()
    event_panel["value"] = pd.to_numeric(event_panel["value_numeric"], errors="coerce")
    event_panel["value_raw"] = event_panel["value"]
    event_panel = event_panel[
        [
            "series_id",
            "observation_date",
            "vintage_date",
            "public_release_timestamp_et",
            "value",
            "value_raw",
            "available_flag",
            "block",
            "transform_code",
            "release_calendar_id",
            "release_block",
            "required_in_v1",
            "source_type",
            "timing_assumption",
            "release_time_status",
        ]
    ].drop_duplicates(subset=["series_id", "observation_date", "vintage_date"])
    event_panel = event_panel.sort_values(
        ["public_release_timestamp_et", "series_id", "observation_date", "vintage_date"]
    ).reset_index(drop=True)

    write_table(event_panel, settings.paths.processed_data / "event_panel.parquet")
    write_table(event_panel, settings.paths.processed_data / "event_panel.csv")
    LOGGER.info("Built event panel with %s rows across %s series", len(event_panel), event_panel["series_id"].nunique())
    return event_panel
