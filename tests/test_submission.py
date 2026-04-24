import pandas as pd

from realtime_gdp_nowcast.reporting.submission import _filter_forecasts, _headline_exact_vs_pseudo, _headline_rows


def test_headline_rows_respect_checkpoint_map() -> None:
    frame = pd.DataFrame(
        [
            {"target_id": "A", "checkpoint_id": "pre_advance", "RMSE": 1.0},
            {"target_id": "A", "checkpoint_id": "m3_spending_trade_inventories", "RMSE": 2.0},
            {"target_id": "S", "checkpoint_id": "pre_second", "RMSE": 3.0},
            {"target_id": "T", "checkpoint_id": "pre_third", "RMSE": 4.0},
        ]
    )
    headline = _headline_rows(frame, {"A": "pre_advance", "S": "pre_second", "T": "pre_third"})
    assert headline["checkpoint_id"].tolist() == ["pre_advance", "pre_second", "pre_third"]
    assert headline["target_id"].tolist() == ["A", "S", "T"]


def test_headline_exact_vs_pseudo_builds_gap() -> None:
    frame = pd.DataFrame(
        [
            {"model_id": "release_dfm", "target_id": "A", "checkpoint_id": "pre_advance", "snapshot_mode": "exact", "RMSE": 4.8},
            {"model_id": "release_dfm", "target_id": "A", "checkpoint_id": "pre_advance", "snapshot_mode": "pseudo", "RMSE": 5.0},
        ]
    )
    ablation = _headline_exact_vs_pseudo(frame)
    assert list(ablation.columns) == ["model_id", "target_id", "checkpoint_id", "exact", "pseudo", "rmse_gap_exact_minus_pseudo"]
    assert round(ablation.loc[0, "rmse_gap_exact_minus_pseudo"], 6) == -0.2


def test_filter_forecasts_applies_quarter_bounds_and_exclusions() -> None:
    frame = pd.DataFrame(
        [
            {"target_quarter_label": "2005Q1", "forecast_value": 1.0},
            {"target_quarter_label": "2008Q4", "forecast_value": 2.0},
            {"target_quarter_label": "2010Q1", "forecast_value": 3.0},
            {"target_quarter_label": "2020Q2", "forecast_value": 4.0},
        ]
    )
    filtered = _filter_forecasts(
        frame,
        start_quarter="2005Q1",
        end_quarter="2020Q4",
        excluded_quarters=["2020Q2"],
    )
    assert filtered["target_quarter_label"].tolist() == ["2005Q1", "2008Q4", "2010Q1"]
