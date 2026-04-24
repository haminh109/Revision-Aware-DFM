import warnings

import numpy as np
import pandas as pd
from numpy.exceptions import ComplexWarning

from realtime_gdp_nowcast.models.state_space_revision import (
    POINT_TARGETS,
    StructuralRevisionStateSpaceModel,
    fit_and_forecast_structural_revision_model,
)


def _synthetic_training_data(nobs: int = 48) -> tuple[pd.DataFrame, pd.Series]:
    rng = np.random.default_rng(7)
    factor = pd.Series(rng.normal(size=nobs))
    level = np.zeros(nobs)
    revision = np.zeros(nobs)
    for idx in range(1, nobs):
        level[idx] = 0.25 + 0.65 * level[idx - 1] + 0.55 * factor.iloc[idx] + rng.normal(scale=0.18)
        revision[idx] = 0.05 + 0.35 * revision[idx - 1] + 0.20 * factor.iloc[idx] + rng.normal(scale=0.10)
    endog = pd.DataFrame(
        {
            "A": level + revision + rng.normal(scale=0.15, size=nobs),
            "S": level + 0.55 * revision + rng.normal(scale=0.12, size=nobs),
            "T": level + 0.20 * revision + rng.normal(scale=0.10, size=nobs),
            "M": level + rng.normal(scale=0.05, size=nobs),
        }
    )
    return endog, factor


def test_structural_revision_loadings_are_ordered() -> None:
    endog, factor = _synthetic_training_data()
    model = StructuralRevisionStateSpaceModel(endog, factor)
    lambda_s, lambda_t = model.transformed_loadings(model.start_params)
    assert 0.0 < lambda_t <= lambda_s < 1.0


def test_structural_revision_model_runs_and_forecasts() -> None:
    endog, factor = _synthetic_training_data()
    with warnings.catch_warnings(record=True) as caught:
        fit = fit_and_forecast_structural_revision_model(
            train_endog=endog,
            train_factor=factor,
            current_factor=0.35,
            known_releases={"A": 1.2, "S": None, "T": None},
            maxiter=50,
        )
    assert fit is not None
    assert set(fit.forecasts) == set(POINT_TARGETS)
    assert np.isfinite([fit.forecasts[target_id] for target_id in POINT_TARGETS]).all()
    assert fit.forecasts["A"] == 1.2
    assert fit.optimization_method in {"lbfgs", "powell", "powell+lbfgs"}
    assert not any(issubclass(item.category, ComplexWarning) for item in caught)
