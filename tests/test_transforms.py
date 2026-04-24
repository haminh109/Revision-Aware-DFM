import pandas as pd

from realtime_gdp_nowcast.features.transforms import apply_transform, expanding_standardize


def test_apply_transform_diff() -> None:
    series = pd.Series([1.0, 2.0, 4.0])
    transformed = apply_transform(series, "diff")
    assert transformed.iloc[-1] == 2.0


def test_expanding_standardize_returns_nan_then_values() -> None:
    values = pd.Series(range(20))
    standardized = expanding_standardize(values)
    assert standardized.iloc[:11].isna().all()
    assert standardized.iloc[-1] == standardized.iloc[-1]
