from __future__ import annotations

import pandas as pd

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.models.common import (
    append_forecasts,
    get_known_target_value,
    get_bridge_features,
    load_model_inputs,
    ols_fit_predict,
)


def run(settings: ProjectSettings) -> pd.DataFrame:
    inputs = load_model_inputs(settings)
    snapshot_panel = inputs["snapshot_panel"]
    schedule = inputs["schedule"]
    schedule_features = inputs["schedule_features"]
    targets_wide = inputs["targets_wide"]
    series_catalog = inputs["series_catalog"]
    feature_store = get_bridge_features(settings, snapshot_panel, series_catalog)

    backtest_start = pd.Period(settings.sample["backtest_start_quarter"], freq="Q-DEC")
    feature_columns = [column for column in feature_store.columns if column.startswith("block_")]
    min_history = settings.models["bridge"]["min_history_quarters"]
    records: list[dict[str, object]] = []

    for row in schedule.itertuples(index=False):
        if row.target_quarter < backtest_start:
            continue
        current = feature_store[
            (feature_store["snapshot_mode"] == row.snapshot_mode)
            & (feature_store["checkpoint_id"] == row.checkpoint_id)
            & (feature_store["target_quarter"] == row.target_quarter)
        ]
        if current.empty:
            continue
        current_row = current.iloc[0]
        current_release_row = schedule_features[
            (schedule_features["snapshot_mode"] == row.snapshot_mode)
            & (schedule_features["checkpoint_id"] == row.checkpoint_id)
            & (schedule_features["target_quarter_label"] == row.target_quarter_label)
        ].iloc[0]
        train_features = feature_store[
            (feature_store["snapshot_mode"] == row.snapshot_mode)
            & (feature_store["checkpoint_id"] == row.checkpoint_id)
            & (feature_store["target_quarter"] < row.target_quarter)
        ]
        if len(train_features) < min_history:
            continue
        train = train_features.merge(targets_wide, on="target_quarter", how="left")
        for target_id in ["A", "S", "T", "M"]:
            known_value = get_known_target_value(current_release_row, target_id)
            if known_value is not None:
                forecast_value = known_value
            else:
                forecast_value = ols_fit_predict(train, feature_columns, target_id, current_row)
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
    append_forecasts(settings, output, "bridge")
    return output
