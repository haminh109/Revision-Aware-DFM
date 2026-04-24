from __future__ import annotations

import logging
from functools import lru_cache

import numpy as np
import pandas as pd
from statsmodels.tsa.ar_model import AutoReg

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.data.time import period_to_quarter_label, quarter_label_to_period
from realtime_gdp_nowcast.features.transforms import apply_transform, expanding_standardize

LOGGER = logging.getLogger(__name__)


def latest_snapshot_values(snapshot_df: pd.DataFrame) -> pd.DataFrame:
    if {"value_transformed", "value_standardized"}.issubset(snapshot_df.columns):
        prepared = snapshot_df.sort_values(["series_id", "observation_date"]).reset_index(drop=True).copy()
        prepared["observation_month"] = pd.PeriodIndex(prepared["observation_date"], freq="M")
        return prepared

    current = snapshot_df.sort_values(["series_id", "observation_date"]).copy()
    current["observation_month"] = pd.PeriodIndex(current["observation_date"], freq="M")
    transformed_frames: list[pd.DataFrame] = []
    for series_id, group in current.groupby("series_id"):
        group = group.sort_values("observation_date").copy()
        group["value_transformed"] = apply_transform(group["value_raw"], group["transform_code"].iloc[0])
        group["value_standardized"] = expanding_standardize(group["value_transformed"])
        transformed_frames.append(group)
    if not transformed_frames:
        return current.iloc[0:0]
    return pd.concat(transformed_frames, ignore_index=True)


def snapshot_to_monthly_matrix(snapshot_df: pd.DataFrame) -> pd.DataFrame:
    prepared = latest_snapshot_values(snapshot_df)
    pivot = prepared.pivot_table(
        index="observation_month",
        columns="series_id",
        values="value_standardized" if "value_standardized" in prepared.columns else "value_transformed",
        aggfunc="last",
    ).sort_index()
    pivot.index = pd.PeriodIndex(pivot.index, freq="M")
    return pivot


def _ar_impute(series: pd.Series, steps: int, max_lag: int) -> list[float]:
    clean = series.dropna()
    if clean.empty:
        return [0.0] * steps
    if len(clean) < 8:
        return [float(clean.iloc[-1])] * steps
    lag = max(1, min(max_lag, len(clean) // 3))
    try:
        result = AutoReg(clean, lags=lag, old_names=False).fit()
        forecast = result.forecast(steps=steps)
        return [float(value) for value in forecast]
    except Exception as exc:  # pragma: no cover - fallback path
        LOGGER.debug("AR imputation fallback due to %s", exc)
        return [float(clean.iloc[-1])] * steps


def impute_target_quarter_months(matrix: pd.DataFrame, target_quarter_label: str, max_lag: int = 6) -> pd.DataFrame:
    target_quarter = quarter_label_to_period(target_quarter_label)
    months = pd.period_range(target_quarter.asfreq("M", how="start"), target_quarter.asfreq("M", how="end"), freq="M")
    full_index = pd.period_range(matrix.index.min(), months[-1], freq="M") if not matrix.empty else months
    expanded = matrix.reindex(full_index)
    for column in expanded.columns:
        missing_months = [month for month in months if pd.isna(expanded.loc[month, column])]
        if not missing_months:
            continue
        history = expanded.loc[expanded.index < months[0], column]
        predictions = _ar_impute(history, steps=len(missing_months), max_lag=max_lag)
        for month, prediction in zip(missing_months, predictions):
            expanded.loc[month, column] = prediction
    return expanded


def quarter_average_features(
    snapshot_df: pd.DataFrame,
    series_catalog: pd.DataFrame,
    target_quarter_label: str,
    max_lag: int,
) -> pd.DataFrame:
    matrix = snapshot_to_monthly_matrix(snapshot_df)
    if matrix.empty:
        return pd.DataFrame()
    imputed = impute_target_quarter_months(matrix, target_quarter_label, max_lag=max_lag)
    target_quarter = quarter_label_to_period(target_quarter_label)
    target_months = pd.period_range(
        target_quarter.asfreq("M", how="start"),
        target_quarter.asfreq("M", how="end"),
        freq="M",
    )
    quarter_means = imputed.loc[target_months].mean(axis=0, skipna=True).rename("feature_value").reset_index()
    quarter_means = quarter_means.rename(columns={"index": "series_id"})
    merged = quarter_means.merge(series_catalog[["series_id", "block"]], on="series_id", how="left")
    block_features = merged.groupby("block", dropna=False)["feature_value"].mean().to_dict()
    row = {f"block_{key}": value for key, value in block_features.items()}
    row["target_quarter"] = target_quarter
    row["target_quarter_label"] = target_quarter_label
    return pd.DataFrame([row])


def build_bridge_feature_store(
    snapshot_panel: pd.DataFrame,
    series_catalog: pd.DataFrame,
    settings: ProjectSettings,
) -> pd.DataFrame:
    rows: list[pd.DataFrame] = []
    max_lag = settings.models["standard_dfm"]["monthly_imputation_max_lag"]
    keys = ["snapshot_mode", "checkpoint_id", "target_quarter_label"]
    for key_values, group in snapshot_panel.groupby(keys):
        snapshot_mode, checkpoint_id, target_quarter_label = key_values
        features = quarter_average_features(group, series_catalog, target_quarter_label, max_lag=max_lag)
        if features.empty:
            continue
        features["snapshot_mode"] = snapshot_mode
        features["checkpoint_id"] = checkpoint_id
        rows.append(features)
    if not rows:
        return pd.DataFrame()
    store = pd.concat(rows, ignore_index=True)
    store["target_quarter"] = store["target_quarter_label"].map(quarter_label_to_period)
    return store.sort_values(["snapshot_mode", "checkpoint_id", "target_quarter"])
