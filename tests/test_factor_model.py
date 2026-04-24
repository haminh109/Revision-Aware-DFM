from pathlib import Path

import numpy as np
import pandas as pd

from realtime_gdp_nowcast.config import load_settings
from realtime_gdp_nowcast.models.dfm import _inverse_psd, estimate_monthly_factor, estimate_quarterly_factor


def _synthetic_snapshot() -> pd.DataFrame:
    rng = np.random.default_rng(12)
    months = pd.period_range("2018-01", "2021-12", freq="M")
    latent = rng.normal(size=len(months)).cumsum() * 0.15
    rows: list[dict[str, object]] = []
    for series_id, loading in [("PAYEMS", 1.0), ("INDPRO", 0.8), ("RSXFS", 0.6)]:
        for index, month in enumerate(months):
            value = loading * latent[index] + rng.normal(scale=0.2)
            if series_id == "RSXFS" and month >= pd.Period("2021-11", freq="M"):
                value = np.nan
            rows.append(
                {
                    "series_id": series_id,
                    "observation_date": month.to_timestamp(how="end"),
                    "value_raw": value,
                    "value_standardized": value,
                    "transform_code": "level",
                }
            )
    frame = pd.DataFrame(rows).dropna(subset=["value_standardized"]).copy()
    frame["snapshot_mode"] = "exact"
    frame["checkpoint_id"] = "pre_advance"
    frame["target_quarter_label"] = "2021Q4"
    return frame


def test_state_space_factor_handles_missing_target_months() -> None:
    settings = load_settings(root=Path(__file__).resolve().parents[1])
    snapshot = _synthetic_snapshot()
    result = estimate_monthly_factor(snapshot, "2021Q4", settings)
    assert result.factor_method in {"state_space_em_kalman", "cross_sectional_mean_fallback"}
    assert len(result.monthly_factor) >= 36
    target_months = result.monthly_factor[result.monthly_factor["target_quarter_label"] == "2021Q4"]
    assert len(target_months) == 3
    assert np.isfinite(target_months["factor"]).all()


def test_quarterly_factor_contains_requested_quarter() -> None:
    settings = load_settings(root=Path(__file__).resolve().parents[1])
    snapshot = _synthetic_snapshot()
    quarterly = estimate_quarterly_factor(snapshot, "2021Q4", settings)
    assert "2021Q4" in set(quarterly["target_quarter_label"])
    assert np.isfinite(quarterly["factor"]).all()


def test_inverse_psd_handles_rank_deficient_matrix() -> None:
    matrix = np.array([[1.0, 1.0], [1.0, 1.0]])
    inverse, logdet = _inverse_psd(matrix)
    assert np.isfinite(inverse).all()
    assert np.isfinite(logdet)
