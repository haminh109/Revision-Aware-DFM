from __future__ import annotations

import numpy as np
import pandas as pd


def apply_transform(values: pd.Series, transform_code: str) -> pd.Series:
    numeric = pd.to_numeric(values, errors="coerce")
    if transform_code == "level":
        return numeric
    if transform_code == "diff":
        return numeric.diff()
    if transform_code == "logdiff_annualized":
        return np.log(numeric).diff() * 1200.0
    raise ValueError(f"Unsupported transform_code: {transform_code}")


def expanding_standardize(values: pd.Series) -> pd.Series:
    mean = values.expanding(min_periods=12).mean()
    std = values.expanding(min_periods=12).std(ddof=0).replace(0.0, np.nan)
    standardized = (values - mean) / std
    return standardized.replace([np.inf, -np.inf], np.nan)
