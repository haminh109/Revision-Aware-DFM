from __future__ import annotations

import json
import logging

import numpy as np
import pandas as pd

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.io import write_table, write_text
from realtime_gdp_nowcast.models.common import (
    append_forecasts,
    get_factor_store,
    get_known_target_value,
    load_model_inputs,
    ols_fit_predict,
)
from realtime_gdp_nowcast.models.state_space_release import (
    POINT_TARGETS,
    fit_and_forecast_structural_release_model,
)


LOGGER = logging.getLogger(__name__)

FEATURES_BY_TARGET = {
    "A": ["factor"],
    "S": ["factor", "known_A"],
    "T": ["factor", "known_A", "known_S"],
    "M": ["factor", "known_A", "known_S", "known_T"],
}


def _fallback_release_forecast(train: pd.DataFrame, current_row: pd.Series) -> dict[str, float]:
    forecasts: dict[str, float] = {}
    for target_id in POINT_TARGETS:
        known_value = get_known_target_value(current_row, target_id)
        if known_value is not None:
            forecasts[target_id] = known_value
        else:
            forecasts[target_id] = ols_fit_predict(train, FEATURES_BY_TARGET[target_id], target_id, current_row)
    return forecasts


def run(settings: ProjectSettings) -> pd.DataFrame:
    inputs = load_model_inputs(settings)
    schedule = inputs["schedule"]
    schedule_features = inputs["schedule_features"]
    targets_wide = inputs["targets_wide"]
    factor_store = get_factor_store(settings, inputs["snapshot_panel"])
    backtest_start = pd.Period(settings.sample["backtest_start_quarter"], freq="Q-DEC")
    schedule = schedule[schedule["target_quarter"] >= backtest_start].copy()
    schedule = schedule.sort_values(["snapshot_mode", "checkpoint_id", "target_quarter"]).reset_index(drop=True)

    params_cache: dict[tuple[str, str], np.ndarray | None] = {}
    records: list[dict[str, object]] = []
    diagnostics_records: list[dict[str, object]] = []
    structural_successes = 0
    fallback_runs = 0

    for row in schedule.itertuples(index=False):
        quarterly_factor = factor_store[
            (factor_store["snapshot_mode"] == row.snapshot_mode)
            & (factor_store["checkpoint_id"] == row.checkpoint_id)
            & (factor_store["forecast_target_quarter_label"] == row.target_quarter_label)
        ]
        if quarterly_factor.empty:
            continue
        current_factor = quarterly_factor[quarterly_factor["target_quarter"] == row.target_quarter]
        if current_factor.empty:
            continue

        train = quarterly_factor[quarterly_factor["target_quarter"] < row.target_quarter].merge(
            targets_wide[["target_quarter", "A", "S", "T", "M"]],
            on="target_quarter",
            how="left",
        )
        if train.empty:
            continue

        history_release_rows = schedule_features[
            (schedule_features["snapshot_mode"] == row.snapshot_mode)
            & (schedule_features["checkpoint_id"] == row.checkpoint_id)
            & (schedule_features["target_quarter_label"] != row.target_quarter_label)
        ]
        current_release_row = schedule_features[
            (schedule_features["snapshot_mode"] == row.snapshot_mode)
            & (schedule_features["checkpoint_id"] == row.checkpoint_id)
            & (schedule_features["target_quarter_label"] == row.target_quarter_label)
        ]
        train = train.merge(history_release_rows, on="target_quarter_label", how="left")
        current_row = pd.concat([current_factor.reset_index(drop=True), current_release_row.reset_index(drop=True)], axis=1).iloc[0]

        known_releases = {target_id: get_known_target_value(current_row, target_id) for target_id in ["A", "S", "T"]}
        group_key = (row.snapshot_mode, row.checkpoint_id)
        fit = fit_and_forecast_structural_release_model(
            train_endog=train[POINT_TARGETS],
            train_factor=train["factor"],
            current_factor=float(current_factor["factor"].iloc[0]),
            known_releases=known_releases,
            start_params=params_cache.get(group_key),
            maxiter=int(settings.get("models", "release_dfm", "maxiter", default=80)),
        )

        if fit is None:
            forecasts = _fallback_release_forecast(train, current_row)
            diagnostics = {
                "estimation_mode": "fallback_regression",
                "structural_converged": False,
                "optimization_method": "fallback",
                "loglikelihood": np.nan,
            }
            fallback_runs += 1
        else:
            forecasts = fit.forecasts
            params_cache[group_key] = fit.params
            diagnostics = {
                "estimation_mode": "structural",
                "structural_converged": fit.converged,
                "optimization_method": fit.optimization_method,
                "loglikelihood": fit.loglikelihood,
            }
            structural_successes += 1

        diagnostics_records.append(
            {
                "snapshot_mode": row.snapshot_mode,
                "checkpoint_id": row.checkpoint_id,
                "forecast_origin": row.forecast_origin,
                "target_quarter": row.target_quarter,
                "target_quarter_label": row.target_quarter_label,
                "training_quarters": int(len(train)),
                **diagnostics,
            }
        )

        for target_id in POINT_TARGETS:
            realized_value = float(
                targets_wide.loc[targets_wide["target_quarter"] == row.target_quarter, target_id].iloc[0]
            )
            records.append(
                {
                    "snapshot_mode": row.snapshot_mode,
                    "checkpoint_id": row.checkpoint_id,
                    "forecast_origin": row.forecast_origin,
                    "target_quarter": row.target_quarter,
                    "target_quarter_label": row.target_quarter_label,
                    "target_id": target_id,
                    "forecast_value": forecasts[target_id],
                    "realized_value": realized_value,
                    "revision_target_flag": False,
                    **diagnostics,
                }
            )

    LOGGER.info(
        "Release-structured model completed | structural_runs=%s fallback_runs=%s",
        structural_successes,
        fallback_runs,
    )
    output = pd.DataFrame(records)
    diagnostics_frame = pd.DataFrame(diagnostics_records)
    diagnostics_path = settings.paths.outputs / "diagnostics" / "release_dfm_diagnostics.parquet"
    write_table(diagnostics_frame, diagnostics_path)
    write_table(diagnostics_frame, diagnostics_path.with_suffix(".csv"))
    summary = {
        "structural_runs": structural_successes,
        "fallback_runs": fallback_runs,
        "structural_share": structural_successes / max(structural_successes + fallback_runs, 1),
        "converged_share_within_structural": (
            float(diagnostics_frame.loc[diagnostics_frame["estimation_mode"] == "structural", "structural_converged"].mean())
            if not diagnostics_frame.empty and (diagnostics_frame["estimation_mode"] == "structural").any()
            else 0.0
        ),
    }
    summary_path = settings.paths.outputs / "diagnostics" / "release_dfm_summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    write_text(
        "\n".join(
            [
                "# Release DFM Run Summary",
                "",
                f"- Structural runs: {summary['structural_runs']}",
                f"- Fallback runs: {summary['fallback_runs']}",
                f"- Structural share: {summary['structural_share']:.3f}",
                f"- Converged share within structural fits: {summary['converged_share_within_structural']:.3f}",
                "",
                f"- Diagnostics table: `{diagnostics_path}`",
            ]
        ),
        settings.paths.outputs / "reports" / "release_dfm_run_summary.md",
    )
    append_forecasts(settings, output, "release_dfm")
    return output
