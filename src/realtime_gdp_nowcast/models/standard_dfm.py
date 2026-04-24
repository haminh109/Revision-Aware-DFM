from __future__ import annotations

import pandas as pd

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.models.common import (
    append_forecasts,
    get_factor_store,
    get_known_target_value,
    load_model_inputs,
    ols_fit_predict,
)


def run(settings: ProjectSettings) -> pd.DataFrame:
    inputs = load_model_inputs(settings)
    snapshot_panel = inputs["snapshot_panel"]
    schedule = inputs["schedule"]
    schedule_features = inputs["schedule_features"]
    targets_wide = inputs["targets_wide"]
    factor_store = get_factor_store(settings, snapshot_panel)
    backtest_start = pd.Period(settings.sample["backtest_start_quarter"], freq="Q-DEC")
    records: list[dict[str, object]] = []

    for row in schedule.itertuples(index=False):
        if row.target_quarter < backtest_start:
            continue
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
            targets_wide,
            on="target_quarter",
            how="left",
        )
        current_row = current_factor.iloc[0]
        current_release_row = schedule_features[
            (schedule_features["snapshot_mode"] == row.snapshot_mode)
            & (schedule_features["checkpoint_id"] == row.checkpoint_id)
            & (schedule_features["target_quarter_label"] == row.target_quarter_label)
        ].iloc[0]
        for target_id in ["A", "S", "T", "M"]:
            known_value = get_known_target_value(current_release_row, target_id)
            if known_value is not None:
                forecast_value = known_value
            else:
                forecast_value = ols_fit_predict(train, ["factor"], target_id, current_row)
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
                    "forecast_value": forecast_value,
                    "realized_value": realized_value,
                    "revision_target_flag": False,
                }
            )

    output = pd.DataFrame(records)
    append_forecasts(settings, output, "standard_dfm")
    return output
