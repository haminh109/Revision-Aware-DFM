from __future__ import annotations

import json
import logging

import numpy as np
import pandas as pd

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.models.common import append_forecasts, get_known_target_value, load_model_inputs, ols_fit_predict
from realtime_gdp_nowcast.models.dfm import estimate_quarterly_factor
from realtime_gdp_nowcast.io import write_table, write_text
from realtime_gdp_nowcast.models.state_space_revision import (
    POINT_TARGETS,
    REVISION_TARGETS,
    fit_and_forecast_structural_revision_model,
)


LOGGER = logging.getLogger(__name__)


def _revision_state(train: pd.DataFrame) -> pd.Series:
    revision_frame = train[REVISION_TARGETS].dropna()
    if revision_frame.empty:
        return pd.Series(dtype=float)
    standardized = (revision_frame - revision_frame.mean()) / revision_frame.std(ddof=0).replace(0.0, np.nan)
    standardized = standardized.fillna(0.0)
    _, _, vh = np.linalg.svd(standardized.to_numpy(), full_matrices=False)
    state = standardized.to_numpy() @ vh[0]
    return pd.Series(state, index=revision_frame.index)


def _forecast_revision_state(train: pd.DataFrame, current_factor: float) -> float:
    state = _revision_state(train)
    if len(state) < 8:
        return 0.0
    aligned = train.loc[state.index].copy()
    aligned["state"] = state
    aligned["state_lag"] = aligned["state"].shift(1)
    aligned = aligned.dropna(subset=["state", "state_lag", "factor"])
    if aligned.empty:
        return 0.0
    x = np.column_stack([np.ones(len(aligned)), aligned["state_lag"], aligned["factor"]])
    y = aligned["state"].to_numpy()
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    last_state = float(aligned["state"].iloc[-1])
    return float(np.array([1.0, last_state, current_factor]) @ beta)


def _approximation_fallback(
    train: pd.DataFrame,
    current_row: pd.Series,
    current_factor_value: float,
) -> tuple[dict[str, float], dict[str, float]]:
    base_forecasts = {
        target_id: (
            get_known_target_value(current_row, target_id)
            if get_known_target_value(current_row, target_id) is not None
            else ols_fit_predict(train, ["factor", "known_A", "known_S", "known_T"], target_id, current_row)
        )
        for target_id in POINT_TARGETS
    }

    predicted_state = _forecast_revision_state(train, current_factor_value)
    train_revision = train.dropna(subset=REVISION_TARGETS).copy()
    train_revision["state_proxy"] = _revision_state(train)
    train_revision = train_revision.dropna(subset=["state_proxy"])
    revision_forecasts = {target_id: 0.0 for target_id in REVISION_TARGETS}
    if not train_revision.empty:
        for revision_target in revision_forecasts:
            known_value = get_known_target_value(current_row, revision_target)
            if known_value is not None:
                revision_forecasts[revision_target] = known_value
                continue
            revision_forecasts[revision_target] = ols_fit_predict(
                train_revision.rename(columns={"state_proxy": "state"}),
                ["state", "factor", "known_A", "known_S", "known_T"],
                revision_target,
                pd.Series({"state": predicted_state, **current_row.to_dict()}),
            )

    adjusted = {
        "A": base_forecasts["A"],
        "S": base_forecasts["A"] + revision_forecasts["DELTA_SA"],
        "T": base_forecasts["A"] + revision_forecasts["DELTA_SA"] + revision_forecasts["DELTA_TS"],
        "M": base_forecasts["A"] + revision_forecasts["DELTA_SA"] + revision_forecasts["DELTA_TS"] + revision_forecasts["DELTA_MT"],
    }
    return adjusted, revision_forecasts


def _structural_revision_forecast(
    train: pd.DataFrame,
    current_row: pd.Series,
    current_factor_value: float,
    previous_params: np.ndarray | None,
    settings: ProjectSettings,
) -> tuple[dict[str, float], dict[str, float], np.ndarray | None, bool, dict[str, object]]:
    known_releases = {target_id: get_known_target_value(current_row, target_id) for target_id in ["A", "S", "T"]}
    fit = fit_and_forecast_structural_revision_model(
        train_endog=train[POINT_TARGETS],
        train_factor=train["factor"],
        current_factor=current_factor_value,
        known_releases=known_releases,
        start_params=previous_params,
        maxiter=int(settings.get("models", "revision_dfm", "maxiter", default=100)),
    )
    if fit is None:
        adjusted, revision_forecasts = _approximation_fallback(train, current_row, current_factor_value)
        diagnostics = {
            "estimation_mode": "fallback_approximation",
            "structural_converged": False,
            "optimization_method": "fallback",
            "loglikelihood": np.nan,
        }
        return adjusted, revision_forecasts, previous_params, False, diagnostics

    adjusted = fit.forecasts
    revision_forecasts = {
        "DELTA_SA": adjusted["S"] - adjusted["A"],
        "DELTA_TS": adjusted["T"] - adjusted["S"],
        "DELTA_MT": adjusted["M"] - adjusted["T"],
    }
    diagnostics = {
        "estimation_mode": "structural",
        "structural_converged": fit.converged,
        "optimization_method": fit.optimization_method,
        "loglikelihood": fit.loglikelihood,
    }
    return adjusted, revision_forecasts, fit.params, True, diagnostics


def _build_factor_cache(snapshot_panel: pd.DataFrame, settings: ProjectSettings) -> dict[tuple[str, str, str], pd.DataFrame]:
    factor_cache: dict[tuple[str, str, str], pd.DataFrame] = {}
    keys = ["snapshot_mode", "checkpoint_id", "target_quarter_label"]
    total_groups = snapshot_panel[keys].drop_duplicates().shape[0]
    for index, (key, group) in enumerate(snapshot_panel.groupby(keys), start=1):
        if index == 1 or index == total_groups or index % 100 == 0:
            LOGGER.info("Building quarterly factor cache | completed=%s/%s", index, total_groups)
        factor_cache[key] = estimate_quarterly_factor(group, key[2], settings)
    return factor_cache


def run(settings: ProjectSettings) -> pd.DataFrame:
    inputs = load_model_inputs(settings)
    snapshot_panel = inputs["snapshot_panel"]
    schedule = inputs["schedule"]
    schedule_features = inputs["schedule_features"]
    targets_wide = inputs["targets_wide"]
    backtest_start = pd.Period(settings.sample["backtest_start_quarter"], freq="Q-DEC")
    factor_cache = _build_factor_cache(snapshot_panel, settings)
    schedule = schedule[schedule["target_quarter"] >= backtest_start].copy()
    schedule = schedule.sort_values(["snapshot_mode", "checkpoint_id", "target_quarter"]).reset_index(drop=True)

    params_cache: dict[tuple[str, str], np.ndarray | None] = {}
    records: list[dict[str, object]] = []
    diagnostics_records: list[dict[str, object]] = []
    structural_successes = 0
    approximation_fallbacks = 0

    for row in schedule.itertuples(index=False):
        factor_key = (row.snapshot_mode, row.checkpoint_id, row.target_quarter_label)
        quarterly_factor = factor_cache.get(factor_key)
        if quarterly_factor is None or quarterly_factor.empty:
            continue
        current_factor = quarterly_factor[quarterly_factor["target_quarter"] == row.target_quarter]
        if current_factor.empty:
            continue
        current_factor_value = float(current_factor["factor"].iloc[0])
        train = quarterly_factor[quarterly_factor["target_quarter"] < row.target_quarter].merge(
            targets_wide[["target_quarter", "A", "S", "T", "M", "DELTA_SA", "DELTA_TS", "DELTA_MT"]],
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

        group_key = (row.snapshot_mode, row.checkpoint_id)
        adjusted, revision_forecasts, updated_params, used_structural, diagnostics = _structural_revision_forecast(
            train,
            current_row,
            current_factor_value,
            params_cache.get(group_key),
            settings,
        )
        params_cache[group_key] = updated_params
        structural_successes += int(used_structural)
        approximation_fallbacks += int(not used_structural)
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
                    "forecast_value": adjusted[target_id],
                    "realized_value": realized_value,
                    "revision_target_flag": False,
                    **diagnostics,
                }
            )

        for target_id in REVISION_TARGETS:
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
                    "forecast_value": revision_forecasts[target_id],
                    "realized_value": realized_value,
                    "revision_target_flag": True,
                    **diagnostics,
                }
            )

    LOGGER.info(
        "Revision-aware model completed | structural_runs=%s fallback_runs=%s",
        structural_successes,
        approximation_fallbacks,
    )
    output = pd.DataFrame(records)
    diagnostics_frame = pd.DataFrame(diagnostics_records)
    diagnostics_path = settings.paths.outputs / "diagnostics" / "revision_dfm_diagnostics.parquet"
    write_table(diagnostics_frame, diagnostics_path)
    write_table(diagnostics_frame, diagnostics_path.with_suffix(".csv"))
    summary = {
        "structural_runs": structural_successes,
        "fallback_runs": approximation_fallbacks,
        "structural_share": structural_successes / max(structural_successes + approximation_fallbacks, 1),
        "converged_share_within_structural": (
            float(diagnostics_frame.loc[diagnostics_frame["estimation_mode"] == "structural", "structural_converged"].mean())
            if not diagnostics_frame.empty and (diagnostics_frame["estimation_mode"] == "structural").any()
            else 0.0
        ),
    }
    summary_path = settings.paths.outputs / "diagnostics" / "revision_dfm_summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    write_text(
        "\n".join(
            [
                "# Revision DFM Run Summary",
                "",
                f"- Structural runs: {summary['structural_runs']}",
                f"- Fallback runs: {summary['fallback_runs']}",
                f"- Structural share: {summary['structural_share']:.3f}",
                f"- Converged share within structural fits: {summary['converged_share_within_structural']:.3f}",
                "",
                f"- Diagnostics table: `{diagnostics_path}`",
            ]
        ),
        settings.paths.outputs / "reports" / "revision_dfm_run_summary.md",
    )
    append_forecasts(settings, output, "revision_dfm")
    return output
