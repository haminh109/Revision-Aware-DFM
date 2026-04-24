import math

import pandas as pd

from realtime_gdp_nowcast.evaluation.metrics import bias, diebold_mariano, mae, rmse, sign_accuracy


def test_error_metrics() -> None:
    errors = pd.Series([1.0, -1.0, 2.0, -2.0])
    assert round(rmse(errors), 6) == round((2.5) ** 0.5, 6)
    assert mae(errors) == 1.5
    assert bias(errors) == 0.0


def test_sign_accuracy() -> None:
    actual = pd.Series([1.0, -1.0, 2.0])
    predicted = pd.Series([0.5, -0.1, -0.4])
    assert sign_accuracy(actual, predicted) == 2 / 3


def test_diebold_mariano_ignores_misaligned_indices() -> None:
    actual = pd.Series([1.0, 2.0, 3.0, 4.0] * 3, index=range(12))
    pred_a = pd.Series([1.1, 1.8, 3.2, 3.7] * 3, index=range(12))
    pred_b = pd.Series(
        [0.9, 2.4, 2.8, 4.5] * 3,
        index=[f"200{i}Q{j}" for i, j in zip([1, 1, 1, 1] * 3, [1, 2, 3, 4] * 3)],
    )
    result = diebold_mariano(actual, pred_a, pred_b)
    assert not math.isnan(result)
