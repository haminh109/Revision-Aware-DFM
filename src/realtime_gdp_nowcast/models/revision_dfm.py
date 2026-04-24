from __future__ import annotations

import numpy as np
import pandas as pd

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.models.common import append_forecasts, get_known_target_value, load_model_inputs, ols_fit_predict
from realtime_gdp_nowcast.models.dfm import estimate_quarterly_factor


def _revision_state(train: pd.DataFrame) -> pd.Series:
    revision_cols = ["DELTA_SA", "DELTA_TS", "DELTA_MT"]
    revision_frame = train[revision_cols].dropna()
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


def run(settings: ProjectSettings) -> pd.DataFrame:
    inputs = load_model_inputs(settings)
    snapshot_panel = inputs["snapshot_panel"]
    schedule = inputs["schedule"]
    schedule_features = inputs["schedule_features"]
    targets_wide = inputs["targets_wide"]
    backtest_start = pd.Period(settings.sample["backtest_start_quarter"], freq="Q-DEC")
    records: list[dict[str, object]] = []

    for row in schedule.itertuples(index=False):
        if row.target_quarter < backtest_start:
            continue
        snapshot_group = snapshot_panel[
            (snapshot_panel["snapshot_mode"] == row.snapshot_mode)
            & (snapshot_panel["checkpoint_id"] == row.checkpoint_id)
            & (snapshot_panel["target_quarter_label"] == row.target_quarter_label)
        ]
        quarterly_factor = estimate_quarterly_factor(snapshot_group, row.target_quarter_label, settings)
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

        base_forecasts = {
            target_id: (
                get_known_target_value(current_row, target_id)
                if get_known_target_value(current_row, target_id) is not None
                else ols_fit_predict(train, ["factor", "known_A", "known_S", "known_T"], target_id, current_row)
            )
            for target_id in ["A", "S", "T", "M"]
        }
        predicted_state = _forecast_revision_state(train, current_factor_value)

        train_revision = train.dropna(subset=["DELTA_SA", "DELTA_TS", "DELTA_MT"]).copy()
        train_revision["state_proxy"] = _revision_state(train)
        train_revision = train_revision.dropna(subset=["state_proxy"])
        revision_forecasts = {"DELTA_SA": 0.0, "DELTA_TS": 0.0, "DELTA_MT": 0.0}
        if not train_revision.empty:
            for revision_target in revision_forecasts:
                known_value = get_known_target_value(current_row, revision_target)
                if known_value is not None:
                    revision_forecasts[revision_target] = known_value
                    continue
                features = ["state", "factor", "known_A", "known_S", "known_T"]
                revision_forecasts[revision_target] = ols_fit_predict(
                    train_revision.rename(columns={"state_proxy": "state"}),
                    features,
                    revision_target,
                    pd.Series({"state": predicted_state, **current_row.to_dict()}),
                )

        adjusted = {
            "A": base_forecasts["A"],
            "S": base_forecasts["A"] + revision_forecasts["DELTA_SA"],
            "T": base_forecasts["A"] + revision_forecasts["DELTA_SA"] + revision_forecasts["DELTA_TS"],
            "M": base_forecasts["A"] + revision_forecasts["DELTA_SA"] + revision_forecasts["DELTA_TS"] + revision_forecasts["DELTA_MT"],
        }

        for target_id in ["A", "S", "T", "M"]:
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
                }
            )

        for target_id, value in revision_forecasts.items():
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
                    "forecast_value": value,
                    "realized_value": realized_value,
                    "revision_target_flag": True,
                }
            )

    output = pd.DataFrame(records)
    append_forecasts(settings, output, "revision_dfm")
    return output
