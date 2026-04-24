from __future__ import annotations

import math

import numpy as np
import pandas as pd
from scipy import stats


def rmse(errors: pd.Series) -> float:
    errors = errors.dropna()
    return float(math.sqrt(np.mean(np.square(errors)))) if not errors.empty else math.nan


def mae(errors: pd.Series) -> float:
    errors = errors.dropna()
    return float(np.mean(np.abs(errors))) if not errors.empty else math.nan


def bias(errors: pd.Series) -> float:
    errors = errors.dropna()
    return float(errors.mean()) if not errors.empty else math.nan


def sign_accuracy(actual: pd.Series, predicted: pd.Series) -> float:
    mask = actual.notna() & predicted.notna()
    if not mask.any():
        return math.nan
    return float((np.sign(actual[mask]) == np.sign(predicted[mask])).mean())


def _dm_loss_diff(actual: pd.Series, pred_a: pd.Series, pred_b: pd.Series, power: int = 2) -> pd.Series:
    frame = pd.DataFrame(
        {
            "actual": pd.Series(actual).reset_index(drop=True),
            "pred_a": pd.Series(pred_a).reset_index(drop=True),
            "pred_b": pd.Series(pred_b).reset_index(drop=True),
        }
    ).dropna()
    if len(frame) < 10:
        return pd.Series(dtype=float)
    return np.abs(frame["actual"] - frame["pred_a"]) ** power - np.abs(frame["actual"] - frame["pred_b"]) ** power


def diebold_mariano(actual: pd.Series, pred_a: pd.Series, pred_b: pd.Series, power: int = 2) -> float:
    loss_diff = _dm_loss_diff(actual, pred_a, pred_b, power=power)
    if len(loss_diff) < 10:
        return math.nan
    if np.isclose(loss_diff.var(ddof=1), 0.0):
        return math.nan
    statistic = loss_diff.mean() / math.sqrt(loss_diff.var(ddof=1) / len(loss_diff))
    p_value = 2 * (1 - stats.t.cdf(abs(statistic), df=len(loss_diff) - 1))
    return float(p_value)


def diebold_mariano_small_sample(
    actual: pd.Series,
    pred_a: pd.Series,
    pred_b: pd.Series,
    power: int = 2,
    horizon: int = 1,
) -> float:
    loss_diff = _dm_loss_diff(actual, pred_a, pred_b, power=power)
    sample_size = len(loss_diff)
    if sample_size < 10 or horizon < 1:
        return math.nan
    variance = loss_diff.var(ddof=1)
    if np.isclose(variance, 0.0):
        return math.nan
    statistic = loss_diff.mean() / math.sqrt(variance / sample_size)
    h = min(int(horizon), sample_size)
    small_sample_factor = math.sqrt((sample_size + 1 - 2 * h + (h * (h - 1) / sample_size)) / sample_size)
    adjusted_statistic = statistic * small_sample_factor
    p_value = 2 * (1 - stats.t.cdf(abs(adjusted_statistic), df=sample_size - 1))
    return float(p_value)
