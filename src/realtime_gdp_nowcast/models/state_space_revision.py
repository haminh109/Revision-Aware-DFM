from __future__ import annotations

import logging
import warnings
from dataclasses import dataclass

import numpy as np
import pandas as pd
from statsmodels.tsa.statespace.mlemodel import MLEModel
from statsmodels.tools.sm_exceptions import ConvergenceWarning


LOGGER = logging.getLogger(__name__)

POINT_TARGETS = ["A", "S", "T", "M"]
REVISION_TARGETS = ["DELTA_SA", "DELTA_TS", "DELTA_MT"]


def _logistic(value: float) -> float:
    clipped = float(np.clip(value, -30.0, 30.0))
    return 1.0 / (1.0 + np.exp(-clipped))


def _bounded_ar(value: float) -> float:
    return 0.98 * np.tanh(value)


def _positive_variance(value: float) -> float:
    clipped = float(np.clip(value, -20.0, 20.0))
    return np.exp(clipped) + 1e-6


def _to_raw_ar(phi: float) -> float:
    bounded = np.clip(phi / 0.98, -0.999, 0.999)
    return float(np.arctanh(bounded))


def _to_raw_probability(value: float) -> float:
    clipped = np.clip(value, 1e-3, 1.0 - 1e-3)
    return float(np.log(clipped / (1.0 - clipped)))


def _safe_variance(values: pd.Series | np.ndarray) -> float:
    array = np.asarray(values, dtype=float)
    array = array[np.isfinite(array)]
    if array.size == 0:
        return 1.0
    return float(max(np.var(array, ddof=0), 1e-2))


def _fit_arx_start(target: pd.Series, factor: pd.Series) -> tuple[float, float, float, float]:
    design = pd.DataFrame(
        {
            "target": pd.Series(target, dtype=float).reset_index(drop=True),
            "lag": pd.Series(target, dtype=float).reset_index(drop=True).shift(1),
            "factor": pd.Series(factor, dtype=float).reset_index(drop=True),
        }
    ).dropna()
    if len(design) < 8:
        variance = _safe_variance(target)
        return 0.0, 0.35, 0.0, variance
    x = np.column_stack([np.ones(len(design)), design["lag"], design["factor"]])
    y = design["target"].to_numpy()
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    fitted = x @ beta
    residual = y - fitted
    return (
        float(beta[0]),
        float(np.clip(beta[1], -0.95, 0.95)),
        float(beta[2]),
        _safe_variance(residual),
    )


def _estimate_start_params(
    endog: pd.DataFrame,
    factor: pd.Series,
    previous_params: np.ndarray | None = None,
) -> np.ndarray:
    if previous_params is not None:
        previous = np.asarray(previous_params, dtype=float)
        if previous.shape == (14,) and np.isfinite(previous).all():
            return previous

    target_frame = endog[POINT_TARGETS].astype(float).reset_index(drop=True)
    factor_series = pd.Series(factor, dtype=float).reset_index(drop=True).fillna(0.0)
    level_proxy = (
        target_frame["M"]
        .where(target_frame["M"].notna(), target_frame[["A", "S", "T", "M"]].mean(axis=1))
        .fillna(target_frame[["A", "S", "T", "M"]].mean(axis=1))
        .fillna(0.0)
    )
    revision_proxy = (target_frame["A"] - level_proxy).fillna(0.0)

    alpha_g, phi_g, beta_g, var_state_g = _fit_arx_start(level_proxy, factor_series)
    alpha_r, phi_r, beta_r, var_state_r = _fit_arx_start(revision_proxy, factor_series)

    ratio_base = revision_proxy.replace(0.0, np.nan)
    lambda_s_est = pd.Series((target_frame["S"] - level_proxy) / ratio_base).replace([np.inf, -np.inf], np.nan).median()
    lambda_t_est = pd.Series((target_frame["T"] - level_proxy) / ratio_base).replace([np.inf, -np.inf], np.nan).median()
    if pd.isna(lambda_s_est):
        lambda_s_est = 0.55
    lambda_s_est = float(np.clip(lambda_s_est, 0.10, 0.95))
    if pd.isna(lambda_t_est):
        lambda_t_est = 0.25
    lambda_t_est = float(np.clip(lambda_t_est, 0.05, lambda_s_est - 1e-3))
    lambda_t_ratio_est = float(np.clip(lambda_t_est / lambda_s_est, 0.05, 0.95))

    obs_var_a = _safe_variance(target_frame["A"] - (level_proxy + revision_proxy))
    obs_var_s = _safe_variance(target_frame["S"] - (level_proxy + lambda_s_est * revision_proxy))
    obs_var_t = _safe_variance(target_frame["T"] - (level_proxy + lambda_t_est * revision_proxy))
    obs_var_m = _safe_variance(target_frame["M"] - level_proxy)

    return np.array(
        [
            alpha_g,
            alpha_r,
            _to_raw_ar(phi_g),
            _to_raw_ar(phi_r),
            beta_g,
            beta_r,
            _to_raw_probability(lambda_s_est),
            _to_raw_probability(lambda_t_ratio_est),
            np.log(obs_var_a),
            np.log(obs_var_s),
            np.log(obs_var_t),
            np.log(obs_var_m),
            np.log(var_state_g),
            np.log(var_state_r),
        ],
        dtype=float,
    )


def _fit_structural_model(
    endog: pd.DataFrame,
    factor: pd.Series,
    start_params: np.ndarray,
    *,
    method: str,
    maxiter: int,
) -> tuple[object | None, bool]:
    model = StructuralRevisionStateSpaceModel(endog, factor)
    fit_kwargs: dict[str, object] = {
        "start_params": np.asarray(start_params, dtype=float),
        "maxiter": maxiter,
        "disp": False,
        "method": method,
        "cov_type": "none",
    }
    if method in {"lbfgs", "bfgs", "cg", "ncg"}:
        fit_kwargs["optim_score"] = "approx"
        fit_kwargs["optim_complex_step"] = False
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ConvergenceWarning)
            fitted = model.fit(**fit_kwargs)
        mle_retvals = getattr(fitted, "mle_retvals", {}) or {}
        converged = bool(mle_retvals.get("converged", False))
        if not converged and mle_retvals.get("warnflag", 0) == 0:
            converged = True
        if not np.isfinite(float(getattr(fitted, "llf", np.nan))):
            return None, False
        return fitted, converged
    except Exception as exc:  # pragma: no cover - numerical fallback
        LOGGER.debug("Structural %s fit failed: %s", method, exc)
        return None, False


class StructuralRevisionStateSpaceModel(MLEModel):
    """
    Quarterly state-space model with:
    - latent activity state g_t
    - latent revision state r_t

    Observation equations:
        A_t = g_t + 1.0 * r_t + e_A,t
        S_t = g_t + lambda_S * r_t + e_S,t
        T_t = g_t + lambda_T * r_t + e_T,t
        M_t = g_t + e_M,t

    Transition equations:
        g_t = alpha_g + phi_g * g_{t-1} + beta_g * factor_t + eta_g,t
        r_t = alpha_r + phi_r * r_{t-1} + beta_r * factor_t + eta_r,t
    """

    def __init__(self, endog: pd.DataFrame, factor: pd.Series) -> None:
        endog_frame = endog[POINT_TARGETS].astype(float).copy()
        factor_array = pd.Series(factor, dtype=float).fillna(0.0).to_numpy()
        super().__init__(endog_frame.to_numpy(), k_states=2, k_posdef=2, initialization="approximate_diffuse")
        self.factor = factor_array
        self.k_endog = len(POINT_TARGETS)
        self.ssm["selection"] = np.eye(2)
        self.ssm["transition"] = np.eye(2)
        self.ssm["design"] = np.array(
            [
                [1.0, 1.0],
                [1.0, 0.5],
                [1.0, 0.2],
                [1.0, 0.0],
            ]
        )
        self.ssm["obs_cov"] = np.eye(self.k_endog)
        self.ssm["state_cov"] = np.eye(2)
        self.ssm["state_intercept"] = np.zeros((2, self.nobs))

    @property
    def start_params(self) -> np.ndarray:
        base_level = np.nanmean(self.endog[:, 0]) if self.endog.size else 0.0
        level_scale = np.nanstd(self.endog[:, 0]) if self.endog.size else 1.0
        return np.array(
            [
                0.10 * base_level,
                0.0,
                np.arctanh(0.65 / 0.98),
                np.arctanh(0.35 / 0.98),
                0.5,
                0.1,
                0.0,
                -0.8,
                np.log(max(level_scale**2, 1e-2)),
                np.log(max(level_scale**2 * 0.7, 1e-2)),
                np.log(max(level_scale**2 * 0.4, 1e-2)),
                np.log(max(level_scale**2 * 0.2, 1e-2)),
                np.log(max(level_scale**2 * 0.2, 1e-2)),
                np.log(max(level_scale**2 * 0.1, 1e-2)),
            ],
            dtype=float,
        )

    @property
    def param_names(self) -> list[str]:
        return [
            "alpha_g",
            "alpha_r",
            "phi_g_raw",
            "phi_r_raw",
            "beta_g",
            "beta_r",
            "lambda_s_raw",
            "lambda_t_ratio_raw",
            "log_var_obs_a",
            "log_var_obs_s",
            "log_var_obs_t",
            "log_var_obs_m",
            "log_var_state_g",
            "log_var_state_r",
        ]

    def update(self, params: np.ndarray, **kwargs: object) -> None:
        params = np.asarray(np.real(params), dtype=float)
        alpha_g, alpha_r, phi_g_raw, phi_r_raw, beta_g, beta_r, lambda_s_raw, lambda_t_ratio_raw = params[:8]
        obs_var_raw = params[8:12]
        state_var_raw = params[12:14]

        phi_g = _bounded_ar(phi_g_raw)
        phi_r = _bounded_ar(phi_r_raw)
        lambda_s = _logistic(lambda_s_raw)
        lambda_t = lambda_s * _logistic(lambda_t_ratio_raw)

        self.ssm["design"] = np.array(
            [
                [1.0, 1.0],
                [1.0, lambda_s],
                [1.0, lambda_t],
                [1.0, 0.0],
            ],
            dtype=float,
        )
        self.ssm["transition"] = np.array(
            [
                [phi_g, 0.0],
                [0.0, phi_r],
            ],
            dtype=float,
        )
        self.ssm["obs_cov"] = np.diag([_positive_variance(value) for value in obs_var_raw])
        self.ssm["state_cov"] = np.diag([_positive_variance(value) for value in state_var_raw])
        self.ssm["state_intercept"] = np.vstack(
            [
                alpha_g + beta_g * self.factor,
                alpha_r + beta_r * self.factor,
            ]
        )

    def transformed_loadings(self, params: np.ndarray) -> tuple[float, float]:
        params = np.asarray(params, dtype=float)
        lambda_s = _logistic(params[6])
        lambda_t = lambda_s * _logistic(params[7])
        return float(lambda_s), float(lambda_t)


@dataclass(slots=True)
class StructuralRevisionFit:
    forecasts: dict[str, float]
    params: np.ndarray
    converged: bool
    optimization_method: str
    loglikelihood: float


def _forecast_from_filtered_state(
    model: StructuralRevisionStateSpaceModel,
    params: np.ndarray,
    filtered_state: np.ndarray,
) -> dict[str, float]:
    lambda_s, lambda_t = model.transformed_loadings(params)
    g_state = float(filtered_state[0])
    r_state = float(filtered_state[1])
    return {
        "A": g_state + r_state,
        "S": g_state + lambda_s * r_state,
        "T": g_state + lambda_t * r_state,
        "M": g_state,
    }


def fit_and_forecast_structural_revision_model(
    train_endog: pd.DataFrame,
    train_factor: pd.Series,
    current_factor: float,
    known_releases: dict[str, float | None],
    *,
    start_params: np.ndarray | None = None,
    maxiter: int = 100,
) -> StructuralRevisionFit | None:
    if len(train_endog) < 24:
        return None
    if train_endog[POINT_TARGETS].dropna(how="all").shape[0] < 24:
        return None

    try:
        candidate_start = _estimate_start_params(train_endog, train_factor, previous_params=start_params)
        fitted, converged = _fit_structural_model(
            train_endog,
            train_factor,
            candidate_start,
            method="lbfgs",
            maxiter=maxiter,
        )
        optimization_method = "lbfgs"
        if fitted is None or not converged:
            powell_fit, powell_converged = _fit_structural_model(
                train_endog,
                train_factor,
                candidate_start if fitted is None else np.asarray(fitted.params, dtype=float),
                method="powell",
                maxiter=max(20, min(maxiter, 40)),
            )
            if powell_fit is not None:
                optimization_method = "powell"
                fitted = powell_fit
                converged = powell_converged
                refined_fit, refined_converged = _fit_structural_model(
                    train_endog,
                    train_factor,
                    np.asarray(powell_fit.params, dtype=float),
                    method="lbfgs",
                    maxiter=max(20, maxiter // 2),
                )
                if refined_fit is not None:
                    optimization_method = "powell+lbfgs"
                    fitted = refined_fit
                    converged = refined_converged
        if fitted is None:
            return None
        current_row = {target_id: np.nan for target_id in POINT_TARGETS}
        for target_id, value in known_releases.items():
            if target_id in current_row and value is not None:
                current_row[target_id] = float(value)
        extended_endog = pd.concat([train_endog, pd.DataFrame([current_row])], ignore_index=True)
        extended_factor = pd.concat([pd.Series(train_factor, dtype=float), pd.Series([current_factor], dtype=float)], ignore_index=True)
        extended_model = StructuralRevisionStateSpaceModel(extended_endog, extended_factor)
        filtered = extended_model.filter(np.asarray(fitted.params, dtype=float))
        current_state = filtered.filtered_state[:, -1]
        forecasts = _forecast_from_filtered_state(extended_model, fitted.params, current_state)
        for target_id, value in known_releases.items():
            if value is not None and target_id in forecasts:
                forecasts[target_id] = float(value)
        return StructuralRevisionFit(
            forecasts=forecasts,
            params=np.asarray(fitted.params, dtype=float),
            converged=converged,
            optimization_method=optimization_method,
            loglikelihood=float(getattr(fitted, "llf", np.nan)),
        )
    except Exception as exc:  # pragma: no cover - numerical fallback
        LOGGER.warning("Structural revision model fit failed; falling back to approximation: %s", exc)
        return None
