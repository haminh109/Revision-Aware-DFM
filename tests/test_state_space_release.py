import numpy as np
import pandas as pd

from realtime_gdp_nowcast.models.state_space_release import (
    POINT_TARGETS,
    fit_and_forecast_structural_release_model,
)


def _synthetic_training_data(nobs: int = 48) -> tuple[pd.DataFrame, pd.Series]:
    rng = np.random.default_rng(24)
    factor = pd.Series(rng.normal(size=nobs))
    level = np.zeros(nobs)
    for idx in range(1, nobs):
        level[idx] = 0.20 + 0.70 * level[idx - 1] + 0.45 * factor.iloc[idx] + rng.normal(scale=0.16)
    endog = pd.DataFrame(
        {
            "A": level + rng.normal(scale=0.18, size=nobs),
            "S": level + rng.normal(scale=0.12, size=nobs),
            "T": level + rng.normal(scale=0.10, size=nobs),
            "M": level + rng.normal(scale=0.06, size=nobs),
        }
    )
    return endog, factor


def test_structural_release_model_runs_and_forecasts() -> None:
    endog, factor = _synthetic_training_data()
    fit = fit_and_forecast_structural_release_model(
        train_endog=endog,
        train_factor=factor,
        current_factor=0.25,
        known_releases={"A": 1.1, "S": None, "T": None},
        maxiter=40,
    )
    assert fit is not None
    assert set(fit.forecasts) == set(POINT_TARGETS)
    assert np.isfinite([fit.forecasts[target_id] for target_id in POINT_TARGETS]).all()
    assert fit.forecasts["A"] == 1.1
    assert fit.optimization_method in {"lbfgs", "powell", "powell+lbfgs"}
