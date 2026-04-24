from __future__ import annotations

import logging
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.data.catalogs import required_series
from realtime_gdp_nowcast.data.time import quarter_label_to_period
from realtime_gdp_nowcast.features.panel import build_bridge_feature_store
from realtime_gdp_nowcast.io import write_table
from realtime_gdp_nowcast.models.dfm import estimate_quarterly_factor

LOGGER = logging.getLogger(__name__)

GDP_TARGET_TO_RELEASE_ROUND = {
    "A": "advance",
    "S": "second",
    "T": "third",
}

KNOWN_VALUE_COLUMN = {
    "A": "known_A",
    "S": "known_S",
    "T": "known_T",
    "DELTA_SA": "known_DELTA_SA",
    "DELTA_TS": "known_DELTA_TS",
}


def load_model_inputs(settings: ProjectSettings) -> dict[str, pd.DataFrame]:
    snapshot_panel = pd.read_parquet(settings.paths.processed_data / "snapshot_panel.parquet")
    schedule = pd.read_parquet(settings.paths.processed_data / "checkpoint_schedule.parquet")
    targets_long = pd.read_parquet(settings.paths.processed_data / "targets.parquet")
    targets_wide = pd.read_parquet(settings.paths.processed_data / "targets_wide.parquet")
    release_calendar = pd.read_parquet(settings.paths.processed_data / "release_calendar.parquet")

    for frame in [schedule, targets_long, targets_wide]:
        frame["target_quarter"] = frame["target_quarter_label"].map(quarter_label_to_period)

    schedule["forecast_origin"] = pd.to_datetime(schedule["forecast_origin"])
    release_calendar["public_release_timestamp_et"] = pd.to_datetime(release_calendar["public_release_timestamp_et"])
    schedule_features = build_release_feature_store(settings, schedule, targets_wide, release_calendar)
    return {
        "snapshot_panel": snapshot_panel,
        "schedule": schedule,
        "targets_long": targets_long,
        "targets_wide": targets_wide,
        "release_calendar": release_calendar,
        "schedule_features": schedule_features,
        "series_catalog": required_series(settings),
    }


def append_forecasts(settings: ProjectSettings, forecasts: pd.DataFrame, model_id: str) -> Path:
    output_path = settings.paths.outputs / "forecasts" / "forecast_results.parquet"
    forecasts = forecasts.copy()
    forecasts["model_id"] = model_id
    if output_path.exists():
        current = pd.read_parquet(output_path)
        current = current[current["model_id"] != model_id]
        combined = pd.concat([current, forecasts], ignore_index=True)
    else:
        combined = forecasts
    write_table(combined, output_path)
    write_table(combined, settings.paths.outputs / "forecasts" / "forecast_results.csv")
    return output_path


def get_bridge_features(settings: ProjectSettings, snapshot_panel: pd.DataFrame, series_catalog: pd.DataFrame) -> pd.DataFrame:
    feature_path = settings.paths.interim_data / "bridge_features.parquet"
    snapshot_path = settings.paths.processed_data / "snapshot_panel.parquet"
    catalog_path = settings.paths.series_catalog
    inputs_are_older_than_cache = (
        feature_path.exists()
        and snapshot_path.exists()
        and feature_path.stat().st_mtime >= snapshot_path.stat().st_mtime
        and feature_path.stat().st_mtime >= catalog_path.stat().st_mtime
    )
    if inputs_are_older_than_cache:
        return pd.read_parquet(feature_path)
    features = build_bridge_feature_store(snapshot_panel, series_catalog, settings)
    write_table(features, feature_path)
    write_table(features, settings.paths.interim_data / "bridge_features.csv")
    return features


def get_factor_store(settings: ProjectSettings, snapshot_panel: pd.DataFrame) -> pd.DataFrame:
    feature_path = settings.paths.interim_data / "quarterly_factor_store.parquet"
    snapshot_path = settings.paths.processed_data / "snapshot_panel.parquet"
    expected_version = str(settings.get("models", "standard_dfm", "factor_store_version", default="state_space_v1"))
    inputs_are_older_than_cache = (
        feature_path.exists()
        and snapshot_path.exists()
        and feature_path.stat().st_mtime >= snapshot_path.stat().st_mtime
        and feature_path.stat().st_mtime >= settings.config_path.stat().st_mtime
    )
    if inputs_are_older_than_cache:
        cached = pd.read_parquet(feature_path)
        cached_version = str(cached["factor_store_version"].iloc[0]) if not cached.empty and "factor_store_version" in cached.columns else ""
        if cached_version == expected_version:
            return cached

    rows: list[pd.DataFrame] = []
    keys = ["snapshot_mode", "checkpoint_id", "target_quarter_label"]
    total_groups = snapshot_panel[keys].drop_duplicates().shape[0]
    for index, (key, group) in enumerate(snapshot_panel.groupby(keys), start=1):
        if index == 1 or index == total_groups or index % 100 == 0:
            LOGGER.info("Building factor store | completed=%s/%s", index, total_groups)
        snapshot_mode, checkpoint_id, target_quarter_label = key
        quarterly_factor = estimate_quarterly_factor(group, target_quarter_label, settings)
        if quarterly_factor.empty:
            continue
        quarterly_factor = quarterly_factor.copy()
        quarterly_factor["snapshot_mode"] = snapshot_mode
        quarterly_factor["checkpoint_id"] = checkpoint_id
        quarterly_factor["forecast_target_quarter_label"] = target_quarter_label
        quarterly_factor["factor_store_version"] = expected_version
        rows.append(quarterly_factor)

    if not rows:
        return pd.DataFrame()
    store = pd.concat(rows, ignore_index=True)
    store = store.sort_values(
        ["snapshot_mode", "checkpoint_id", "forecast_target_quarter_label", "target_quarter"]
    ).reset_index(drop=True)
    write_table(store, feature_path)
    write_table(store, settings.paths.interim_data / "quarterly_factor_store.csv")
    return store


def build_release_feature_store(
    settings: ProjectSettings,
    schedule: pd.DataFrame,
    targets_wide: pd.DataFrame,
    release_calendar: pd.DataFrame,
) -> pd.DataFrame:
    target_lookup = targets_wide.set_index("target_quarter_label")
    gdp_calendar = release_calendar[
        (release_calendar["series_id"] == settings.project["gdp_release_proxy_series_id"])
        & release_calendar["release_round"].isin(["advance", "second", "third"])
    ].copy()
    release_lookup = gdp_calendar.pivot_table(
        index="reference_period",
        columns="release_round",
        values="public_release_timestamp_et",
        aggfunc="first",
    )

    rows: list[dict[str, object]] = []
    for row in schedule.itertuples(index=False):
        realized = target_lookup.loc[row.target_quarter_label]
        gdp_release_times = release_lookup.loc[row.target_quarter_label] if row.target_quarter_label in release_lookup.index else pd.Series(dtype=object)
        known_values = {}
        for target_id, release_round in GDP_TARGET_TO_RELEASE_ROUND.items():
            release_time = gdp_release_times.get(release_round, pd.NaT)
            is_observed = pd.notna(release_time) and row.forecast_origin >= release_time
            known_values[f"known_{target_id}"] = realized[target_id] if is_observed else np.nan
        known_values["known_DELTA_SA"] = (
            known_values["known_S"] - known_values["known_A"]
            if pd.notna(known_values["known_A"]) and pd.notna(known_values["known_S"])
            else np.nan
        )
        known_values["known_DELTA_TS"] = (
            known_values["known_T"] - known_values["known_S"]
            if pd.notna(known_values["known_S"]) and pd.notna(known_values["known_T"])
            else np.nan
        )
        rows.append(
            {
                "snapshot_mode": row.snapshot_mode,
                "checkpoint_id": row.checkpoint_id,
                "target_quarter_label": row.target_quarter_label,
                "target_quarter": row.target_quarter,
                **known_values,
            }
        )

    return pd.DataFrame(rows)


def get_known_target_value(current_row: pd.Series, target_id: str) -> float | None:
    column = KNOWN_VALUE_COLUMN.get(target_id)
    if column is None or column not in current_row.index or pd.isna(current_row[column]):
        return None
    return float(current_row[column])


def ols_fit_predict(train: pd.DataFrame, feature_columns: Iterable[str], target_column: str, current_row: pd.Series) -> float:
    feature_columns = [
        column
        for column in feature_columns
        if column in train.columns and column in current_row.index and pd.notna(current_row[column]) and train[column].notna().any()
    ]
    if not feature_columns:
        clean_target = train[target_column].dropna()
        return float(clean_target.iloc[-1]) if not clean_target.empty else 0.0
    train_clean = train.dropna(subset=[target_column, *feature_columns]).copy()
    if train_clean.empty:
        clean_target = train[target_column].dropna()
        return float(clean_target.iloc[-1]) if not clean_target.empty else 0.0
    x_train = np.column_stack([np.ones(len(train_clean)), train_clean[feature_columns].to_numpy()])
    y_train = train_clean[target_column].to_numpy()
    beta, *_ = np.linalg.lstsq(x_train, y_train, rcond=None)
    current_values = np.array([1.0, *[float(current_row[column]) for column in feature_columns]])
    return float(current_values @ beta)
