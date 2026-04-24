from __future__ import annotations

import logging
import warnings

import numpy as np
import pandas as pd
from statsmodels.tsa.ar_model import AutoReg

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.models.common import append_forecasts, get_known_target_value, load_model_inputs

LOGGER = logging.getLogger(__name__)

warnings.filterwarnings(
    "ignore",
    category=RuntimeWarning,
    message=".*encountered in matmul.*",
    module=r"statsmodels\.tsa\.ar_model",
)


def _forecast_single_series(series: pd.Series, min_lag: int, max_lag: int, ic: str) -> float:
    clean = pd.Series(series.dropna().astype(float).to_numpy())
    if len(clean) < 12:
        return float(clean.iloc[-1]) if not clean.empty else 0.0

    best_score = np.inf
    best_result = None
    for lag in range(min_lag, max_lag + 1):
        if len(clean) <= lag + 5:
            continue
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", RuntimeWarning)
                result = AutoReg(clean, lags=lag, old_names=False).fit()
        except Exception:
            continue
        score = getattr(result, ic)
        if not np.isfinite(score):
            continue
        if score < best_score:
            best_score = score
            best_result = result
    if best_result is None:
        return float(clean.iloc[-1])
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            forecast = float(best_result.forecast(steps=1).iloc[0])
        return forecast if np.isfinite(forecast) else float(clean.iloc[-1])
    except Exception:
        return float(clean.iloc[-1])


def run(settings: ProjectSettings) -> pd.DataFrame:
    inputs = load_model_inputs(settings)
    schedule = inputs["schedule"]
    schedule_features = inputs["schedule_features"]
    targets_wide = inputs["targets_wide"]
    model_cfg = settings.models["ar"]

    backtest_start = pd.Period(settings.sample["backtest_start_quarter"], freq="Q-DEC")
    results: list[dict[str, object]] = []
    target_ids = ["A", "S", "T", "M"]

    for row in schedule.itertuples(index=False):
        target_quarter = row.target_quarter
        if target_quarter < backtest_start:
            continue
        row_features = schedule_features[
            (schedule_features["snapshot_mode"] == row.snapshot_mode)
            & (schedule_features["checkpoint_id"] == row.checkpoint_id)
            & (schedule_features["target_quarter_label"] == row.target_quarter_label)
        ].iloc[0]
        for target_id in target_ids:
            known_value = get_known_target_value(row_features, target_id)
            if known_value is not None:
                forecast_value = known_value
            else:
                history = targets_wide[targets_wide["target_quarter"] < target_quarter][["target_quarter", target_id]]
                forecast_value = _forecast_single_series(
                    history[target_id],
                    min_lag=model_cfg["min_lag"],
                    max_lag=model_cfg["max_lag"],
                    ic=model_cfg["ic"],
                )
            realized_value = float(
                targets_wide.loc[targets_wide["target_quarter"] == target_quarter, target_id].iloc[0]
            )
            results.append(
                {
                    "snapshot_mode": row.snapshot_mode,
                    "checkpoint_id": row.checkpoint_id,
                    "forecast_origin": row.forecast_origin,
                    "target_quarter": target_quarter,
                    "target_quarter_label": row.target_quarter_label,
                    "target_id": target_id,
                    "forecast_value": forecast_value,
                    "realized_value": realized_value,
                    "revision_target_flag": False,
                }
            )

    output = pd.DataFrame(results)
    append_forecasts(settings, output, "ar")
    return output
