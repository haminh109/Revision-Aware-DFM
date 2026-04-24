from __future__ import annotations

import logging
import warnings
from dataclasses import dataclass

import numpy as np
import pandas as pd

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.data.time import period_to_quarter_label, quarter_label_to_period
from realtime_gdp_nowcast.features.panel import snapshot_to_monthly_matrix

LOGGER = logging.getLogger(__name__)
FACTOR_VALUE_CLIP = 12.0
STATE_VALUE_CLIP = 25.0
LOADING_VALUE_CLIP = 10.0
COVARIANCE_VALUE_CLIP = 1_000.0


@dataclass(slots=True)
class StateSpaceFactorResult:
    monthly_factor: pd.DataFrame
    quarterly_factor: pd.DataFrame
    factor_method: str
    em_iterations: int
    final_loglikelihood: float


def _symmetrize(matrix: np.ndarray) -> np.ndarray:
    return 0.5 * (matrix + matrix.T)


def _safe_matmul(left: np.ndarray, right: np.ndarray, clip: float) -> np.ndarray:
    with np.errstate(over="ignore", divide="ignore", invalid="ignore", under="ignore"):
        product = np.matmul(left, right)
    product = np.nan_to_num(product, nan=0.0, posinf=clip, neginf=-clip)
    return np.clip(product, -clip, clip)


def _psd_eigendecomposition(matrix: np.ndarray, ridge: float = 1e-6) -> tuple[np.ndarray, np.ndarray]:
    symmetric = np.asarray(matrix, dtype=float)
    symmetric = np.nan_to_num(symmetric, nan=0.0, posinf=COVARIANCE_VALUE_CLIP, neginf=-COVARIANCE_VALUE_CLIP)
    symmetric = np.clip(symmetric, -COVARIANCE_VALUE_CLIP, COVARIANCE_VALUE_CLIP)
    symmetric = _symmetrize(symmetric)
    eigenvalues, eigenvectors = np.linalg.eigh(symmetric)
    eigenvalues = np.clip(np.nan_to_num(eigenvalues, nan=ridge, posinf=ridge, neginf=ridge), ridge, None)
    return eigenvalues, eigenvectors


def _project_psd(matrix: np.ndarray, ridge: float = 1e-6) -> np.ndarray:
    eigenvalues, eigenvectors = _psd_eigendecomposition(matrix, ridge=ridge)
    return _symmetrize(_safe_matmul(eigenvectors * eigenvalues, eigenvectors.T, clip=COVARIANCE_VALUE_CLIP))


def _inverse_psd(matrix: np.ndarray, ridge: float = 1e-6) -> tuple[np.ndarray, float]:
    eigenvalues, eigenvectors = _psd_eigendecomposition(matrix, ridge=ridge)
    inverse = _safe_matmul(eigenvectors * (1.0 / eigenvalues), eigenvectors.T, clip=COVARIANCE_VALUE_CLIP)
    logdet = float(np.sum(np.log(eigenvalues)))
    return _symmetrize(inverse), logdet


def _sanitize_array(values: np.ndarray | pd.DataFrame | pd.Series, clip: float = FACTOR_VALUE_CLIP) -> np.ndarray:
    array = np.asarray(values, dtype=float)
    array = np.where(np.isfinite(array), array, np.nan)
    finite = np.isfinite(array)
    if finite.any():
        array[finite] = np.clip(array[finite], -clip, clip)
    return array


def _standardize_factor(values: np.ndarray) -> np.ndarray:
    vector = _sanitize_array(values)
    finite = np.isfinite(vector)
    if not finite.any():
        return np.zeros_like(vector)
    centered = vector.copy()
    centered[finite] = centered[finite] - centered[finite].mean()
    scale = centered[finite].std(ddof=0)
    if not np.isfinite(scale) or scale < 1e-6:
        return centered
    centered[finite] = centered[finite] / scale
    centered[~finite] = 0.0
    return centered


def _companion_matrix(ar_params: np.ndarray) -> np.ndarray:
    order = len(ar_params)
    transition = np.zeros((order, order), dtype=float)
    transition[0, :order] = ar_params
    if order > 1:
        transition[1:, :-1] = np.eye(order - 1)
    return transition


def _stabilize_ar_params(ar_params: np.ndarray, max_root: float = 0.98) -> np.ndarray:
    params = np.asarray(ar_params, dtype=float).copy()
    if params.size == 0:
        return np.array([0.0], dtype=float)
    if params.size == 1:
        params[0] = float(np.clip(params[0], -max_root, max_root))
        return params

    transition = _companion_matrix(params)
    spectral_radius = np.max(np.abs(np.linalg.eigvals(transition)))
    if np.isfinite(spectral_radius) and spectral_radius >= max_root:
        shrink = 0.95 * max_root / max(spectral_radius, 1e-6)
        params *= shrink
    return params


def _initial_factor(monthly_matrix: pd.DataFrame) -> np.ndarray:
    filled = monthly_matrix.sort_index().ffill().fillna(0.0)
    if filled.empty:
        return np.array([], dtype=float)
    if filled.shape[1] < 2 or filled.shape[0] < 6:
        return _standardize_factor(filled.mean(axis=1).to_numpy(dtype=float))
    centered = filled - filled.mean()
    centered_values = _sanitize_array(centered.to_numpy(dtype=float))
    if not np.isfinite(centered_values).any():
        return np.zeros(centered_values.shape[0], dtype=float)
    try:
        with warnings.catch_warnings():
            warnings.filterwarnings("error", category=RuntimeWarning)
            covariance = _safe_matmul(
                centered_values.T,
                centered_values,
                clip=COVARIANCE_VALUE_CLIP,
            ) / max(centered_values.shape[0] - 1, 1)
            eigenvalues, eigenvectors = _psd_eigendecomposition(covariance)
            lead_index = int(np.argmax(eigenvalues))
            lead_vector = eigenvectors[:, lead_index]
            first_component = _safe_matmul(centered_values, lead_vector, clip=STATE_VALUE_CLIP)
            first_component = first_component / max(float(np.sqrt(eigenvalues[lead_index])), 1e-6)
        return _standardize_factor(first_component)
    except Exception:
        return _standardize_factor(filled.mean(axis=1).to_numpy(dtype=float))


def _estimate_measurement_params(y: np.ndarray, factor: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    y = _sanitize_array(y)
    factor = _standardize_factor(factor)
    n_series = y.shape[1]
    loadings = np.zeros(n_series, dtype=float)
    obs_var = np.ones(n_series, dtype=float)
    for column in range(n_series):
        mask = np.isfinite(y[:, column]) & np.isfinite(factor)
        if mask.sum() < 6:
            continue
        x = factor[mask]
        denominator = float(np.dot(x, x))
        if denominator < 1e-6:
            continue
        beta = float(np.dot(x, y[mask, column]) / denominator)
        residual = y[mask, column] - beta * x
        loadings[column] = beta
        obs_var[column] = float(max(np.var(residual, ddof=0), 1e-3))
    if not np.any(np.abs(loadings) > 1e-6):
        loadings[:] = 1.0 / max(n_series, 1)
    return loadings, obs_var


def _estimate_state_params(factor: np.ndarray, factor_order: int) -> tuple[np.ndarray, float]:
    factor = _standardize_factor(factor)
    order = max(1, factor_order)
    if len(factor) <= order + 4:
        params = np.zeros(order, dtype=float)
        params[0] = 0.55
        return _stabilize_ar_params(params), 0.5

    target = factor[order:]
    lags = np.column_stack([factor[order - lag - 1 : -lag - 1] for lag in range(order)])
    beta, *_ = np.linalg.lstsq(lags, target, rcond=None)
    beta = _stabilize_ar_params(np.asarray(beta, dtype=float))
    residual = target - lags @ beta
    state_var = float(max(np.var(residual, ddof=0), 1e-3))
    return beta, state_var


def _kalman_smoother(
    y: np.ndarray,
    loadings: np.ndarray,
    obs_var: np.ndarray,
    ar_params: np.ndarray,
    state_var: float,
) -> tuple[np.ndarray, float]:
    y = _sanitize_array(y)
    loadings = np.clip(
        np.nan_to_num(np.asarray(loadings, dtype=float), nan=0.0, posinf=0.0, neginf=0.0),
        -LOADING_VALUE_CLIP,
        LOADING_VALUE_CLIP,
    )
    obs_var = np.clip(np.nan_to_num(np.asarray(obs_var, dtype=float), nan=1.0, posinf=1.0, neginf=1.0), 1e-4, None)
    ar_params = _stabilize_ar_params(np.nan_to_num(np.asarray(ar_params, dtype=float), nan=0.0, posinf=0.0, neginf=0.0))
    state_var = float(max(np.nan_to_num(state_var, nan=0.5, posinf=0.5, neginf=0.5), 1e-4))
    nobs, _ = y.shape
    order = len(ar_params)
    transition = _companion_matrix(ar_params)
    state_cov = np.zeros((order, order), dtype=float)
    state_cov[0, 0] = state_var

    filtered_state = np.zeros((nobs, order), dtype=float)
    filtered_cov = np.zeros((nobs, order, order), dtype=float)
    predicted_state = np.zeros((nobs, order), dtype=float)
    predicted_cov = np.zeros((nobs, order, order), dtype=float)

    current_state = np.zeros(order, dtype=float)
    current_cov = np.eye(order, dtype=float) * 5.0
    loglikelihood = 0.0

    for index in range(nobs):
        if index == 0:
            state_pred = current_state
            cov_pred = current_cov
        else:
            state_pred = _safe_matmul(transition, filtered_state[index - 1], clip=STATE_VALUE_CLIP)
            cov_pred = _safe_matmul(
                _safe_matmul(transition, filtered_cov[index - 1], clip=COVARIANCE_VALUE_CLIP),
                transition.T,
                clip=COVARIANCE_VALUE_CLIP,
            ) + state_cov
        state_pred = np.clip(state_pred, -STATE_VALUE_CLIP, STATE_VALUE_CLIP)
        cov_pred = _project_psd(cov_pred)
        predicted_state[index] = state_pred
        predicted_cov[index] = cov_pred

        mask = np.isfinite(y[index])
        if not mask.any():
            filtered_state[index] = state_pred
            filtered_cov[index] = cov_pred
            continue

        design = np.zeros((int(mask.sum()), order), dtype=float)
        design[:, 0] = loadings[mask]
        obs_cov = np.diag(obs_var[mask])
        innovation = y[index, mask] - _safe_matmul(design, state_pred, clip=STATE_VALUE_CLIP)
        forecast_cov = _project_psd(
            _safe_matmul(
                _safe_matmul(design, cov_pred, clip=COVARIANCE_VALUE_CLIP),
                design.T,
                clip=COVARIANCE_VALUE_CLIP,
            )
            + obs_cov
        )
        inv_forecast_cov, logdet = _inverse_psd(forecast_cov)
        kalman_gain = _safe_matmul(
            _safe_matmul(cov_pred, design.T, clip=COVARIANCE_VALUE_CLIP),
            inv_forecast_cov,
            clip=COVARIANCE_VALUE_CLIP,
        )
        state_filt = state_pred + _safe_matmul(kalman_gain, innovation, clip=STATE_VALUE_CLIP)
        state_filt = np.clip(state_filt, -STATE_VALUE_CLIP, STATE_VALUE_CLIP)
        cov_filt = cov_pred - _safe_matmul(
            _safe_matmul(kalman_gain, design, clip=COVARIANCE_VALUE_CLIP),
            cov_pred,
            clip=COVARIANCE_VALUE_CLIP,
        )
        cov_filt = _project_psd(cov_filt)
        filtered_state[index] = state_filt
        filtered_cov[index] = cov_filt

        innovation_quadratic = float(
            np.asarray(
                _safe_matmul(
                    _safe_matmul(innovation.T, inv_forecast_cov, clip=COVARIANCE_VALUE_CLIP),
                    innovation,
                    clip=COVARIANCE_VALUE_CLIP,
                )
            ).squeeze()
        )
        loglikelihood += -0.5 * (
            innovation_quadratic
            + logdet
            + len(innovation) * np.log(2.0 * np.pi)
        )

    smoothed_state = filtered_state.copy()
    smoothed_cov = filtered_cov.copy()
    for index in range(nobs - 2, -1, -1):
        next_cov = predicted_cov[index + 1]
        inv_next_cov, _ = _inverse_psd(next_cov)
        smoother_gain = _safe_matmul(
            _safe_matmul(filtered_cov[index], transition.T, clip=COVARIANCE_VALUE_CLIP),
            inv_next_cov,
            clip=COVARIANCE_VALUE_CLIP,
        )
        smoothed_state[index] = filtered_state[index] + _safe_matmul(
            smoother_gain,
            (smoothed_state[index + 1] - predicted_state[index + 1]),
            clip=STATE_VALUE_CLIP,
        )
        smoothed_state[index] = np.clip(smoothed_state[index], -STATE_VALUE_CLIP, STATE_VALUE_CLIP)
        smoothed_cov[index] = filtered_cov[index] + _safe_matmul(
            _safe_matmul(
                smoother_gain,
                (smoothed_cov[index + 1] - predicted_cov[index + 1]),
                clip=COVARIANCE_VALUE_CLIP,
            ),
            smoother_gain.T,
            clip=COVARIANCE_VALUE_CLIP,
        )
        smoothed_cov[index] = _project_psd(smoothed_cov[index])

    return smoothed_state[:, 0], float(loglikelihood)


def _expand_monthly_matrix(monthly_matrix: pd.DataFrame, target_quarter_label: str) -> pd.DataFrame:
    target_quarter = quarter_label_to_period(target_quarter_label)
    target_end = target_quarter.asfreq("M", how="end")
    start = monthly_matrix.index.min() if not monthly_matrix.empty else target_quarter.asfreq("M", how="start")
    full_index = pd.period_range(start, target_end, freq="M")
    return monthly_matrix.reindex(full_index)


def estimate_monthly_factor(
    snapshot_df: pd.DataFrame,
    target_quarter_label: str,
    settings: ProjectSettings,
) -> StateSpaceFactorResult:
    monthly_matrix = snapshot_to_monthly_matrix(snapshot_df)
    if monthly_matrix.empty:
        empty = pd.DataFrame(columns=["observation_month", "factor"])
        return StateSpaceFactorResult(
            monthly_factor=empty,
            quarterly_factor=pd.DataFrame(columns=["target_quarter", "factor", "target_quarter_label"]),
            factor_method="empty",
            em_iterations=0,
            final_loglikelihood=float("nan"),
        )

    monthly_matrix = _expand_monthly_matrix(monthly_matrix, target_quarter_label)
    y = _sanitize_array(monthly_matrix.to_numpy(dtype=float))
    factor_order = int(settings.models["standard_dfm"].get("factor_order", 2))
    min_history = int(settings.get("models", "standard_dfm", "factor_min_history_months", default=24))
    em_iterations = int(settings.get("models", "standard_dfm", "factor_em_iterations", default=4))

    if monthly_matrix.shape[0] < max(min_history, factor_order + 4):
        factor = _standardize_factor(monthly_matrix.ffill().fillna(0.0).mean(axis=1).to_numpy())
        method = "cross_sectional_mean_fallback"
        final_loglikelihood = float("nan")
        actual_iterations = 0
    else:
        factor = _initial_factor(monthly_matrix)
        loadings, obs_var = _estimate_measurement_params(y, factor)
        ar_params, state_var = _estimate_state_params(factor, factor_order)
        final_loglikelihood = float("nan")
        actual_iterations = 0
        for _ in range(em_iterations):
            smoothed_factor, loglikelihood = _kalman_smoother(y, loadings, obs_var, ar_params, state_var)
            factor = _standardize_factor(smoothed_factor)
            loadings, obs_var = _estimate_measurement_params(y, factor)
            ar_params, state_var = _estimate_state_params(factor, factor_order)
            final_loglikelihood = loglikelihood
            actual_iterations += 1
        method = "state_space_em_kalman"

    monthly_factor = pd.DataFrame(
        {
            "observation_month": monthly_matrix.index,
            "factor": factor,
        }
    )
    monthly_factor["target_quarter"] = pd.PeriodIndex(monthly_factor["observation_month"], freq="M").asfreq("Q-DEC")
    monthly_factor["target_quarter_label"] = [
        period_to_quarter_label(period) for period in monthly_factor["target_quarter"]
    ]

    quarterly_factor = (
        monthly_factor.groupby("target_quarter", as_index=False)["factor"].mean()
        .sort_values("target_quarter")
        .reset_index(drop=True)
    )
    quarterly_factor["target_quarter_label"] = [
        period_to_quarter_label(period) for period in quarterly_factor["target_quarter"]
    ]
    quarterly_factor["factor_method"] = method
    quarterly_factor["em_iterations"] = actual_iterations
    quarterly_factor["final_loglikelihood"] = final_loglikelihood
    return StateSpaceFactorResult(
        monthly_factor=monthly_factor,
        quarterly_factor=quarterly_factor,
        factor_method=method,
        em_iterations=actual_iterations,
        final_loglikelihood=final_loglikelihood,
    )


def estimate_quarterly_factor(
    snapshot_df: pd.DataFrame,
    target_quarter_label: str,
    settings: ProjectSettings,
) -> pd.DataFrame:
    result = estimate_monthly_factor(snapshot_df, target_quarter_label, settings)
    return result.quarterly_factor
