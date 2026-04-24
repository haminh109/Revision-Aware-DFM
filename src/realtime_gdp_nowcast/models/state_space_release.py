from __future__ import annotations

import logging
import warnings
from dataclasses import dataclass

import numpy as np
import pandas as pd
from statsmodels.tools.sm_exceptions import ConvergenceWarning
from statsmodels.tsa.statespace.mlemodel import MLEModel


LOGGER = logging.getLogger(__name__)

POINT_TARGETS = ["A", "S", "T", "M"]


def _bounded_ar(value: float) -> float:
    return 0.98 * np.tanh(value)


def _to_raw_ar(phi: float) -> float:
    bounded = np.clip(phi / 0.98, -0.999, 0.999)
    return float(np.arctanh(bounded))


def _positive_variance(value: float) -> float:
    clipped = float(np.clip(value, -20.0, 20.0))
    return np.exp(clipped) + 1e-6


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
        return 0.0, 0.45, 0.0, variance
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


class StructuralReleaseStateSpaceModel(MLEModel):
    """
    One-state release-ladder model:

        y_r,t = g_t + e_r,t,   r in {A, S, T, M}
        g_t   = alpha + phi * g_{t-1} + beta * factor_t + eta_t
    """

    def __init__(self, endog: pd.DataFrame, factor: pd.Series) -> None:
        endog_frame = endog[POINT_TARGETS].astype(float).copy()
        factor_array = pd.Series(factor, dtype=float).fillna(0.0).to_numpy()
        super().__init__(endog_frame.to_numpy(), k_states=1, k_posdef=1, initialization="approximate_diffuse")
        self.factor = factor_array
        self.k_endog = len(POINT_TARGETS)
        self.ssm["selection"] = np.array([[1.0]])
        self.ssm["transition"] = np.array([[1.0]])
        self.ssm["design"] = np.ones((self.k_endog, 1), dtype=float)
        self.ssm["obs_cov"] = np.eye(self.k_endog, dtype=float)
        self.ssm["state_cov"] = np.array([[1.0]])
        self.ssm["state_intercept"] = np.zeros((1, self.nobs))

    @property
    def start_params(self) -> np.ndarray:
        level = pd.Series(self.endog[:, 0], dtype=float)
        factor = pd.Series(self.factor, dtype=float)
        alpha, phi, beta, state_var = _fit_arx_start(level, factor)
        scale = np.sqrt(_safe_variance(level))
        return np.array(
            [
                alpha,
                _to_raw_ar(phi),
                beta,
                np.log(max(scale**2, 1e-2)),
                np.log(max(scale**2 * 0.7, 1e-2)),
                np.log(max(scale**2 * 0.4, 1e-2)),
                np.log(max(scale**2 * 0.2, 1e-2)),
                np.log(max(state_var, 1e-2)),
            ],
            dtype=float,
        )

    @property
    def param_names(self) -> list[str]:
        return [
            "alpha_g",
            "phi_g_raw",
            "beta_g",
            "log_var_obs_a",
            "log_var_obs_s",
            "log_var_obs_t",
            "log_var_obs_m",
            "log_var_state_g",
        ]

    def update(self, params: np.ndarray, **kwargs: object) -> None:
        params = np.asarray(np.real(params), dtype=float)
        alpha_g, phi_g_raw, beta_g = params[:3]
        obs_var_raw = params[3:7]
        state_var_raw = params[7]
        phi_g = _bounded_ar(phi_g_raw)

        self.ssm["transition"] = np.array([[phi_g]], dtype=float)
        self.ssm["design"] = np.ones((self.k_endog, 1), dtype=float)
        self.ssm["obs_cov"] = np.diag([_positive_variance(value) for value in obs_var_raw])
        self.ssm["state_cov"] = np.array([[_positive_variance(state_var_raw)]], dtype=float)
        self.ssm["state_intercept"] = np.array([alpha_g + beta_g * self.factor], dtype=float)


@dataclass(slots=True)
class StructuralReleaseFit:
    forecasts: dict[str, float]
    params: np.ndarray
    converged: bool
    optimization_method: str
    loglikelihood: float


def _fit_model(
    endog: pd.DataFrame,
    factor: pd.Series,
    start_params: np.ndarray,
    *,
    method: str,
    maxiter: int,
) -> tuple[object | None, bool]:
    model = StructuralReleaseStateSpaceModel(endog, factor)
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
        LOGGER.debug("Structural release %s fit failed: %s", method, exc)
        return None, False


def fit_and_forecast_structural_release_model(
    train_endog: pd.DataFrame,
    train_factor: pd.Series,
    current_factor: float,
    known_releases: dict[str, float | None],
    *,
    start_params: np.ndarray | None = None,
    maxiter: int = 80,
) -> StructuralReleaseFit | None:
    if len(train_endog) < 24 or train_endog[POINT_TARGETS].dropna(how="all").shape[0] < 24:
        return None

    try:
        model = StructuralReleaseStateSpaceModel(train_endog, train_factor)
        candidate_start = (
            np.asarray(start_params, dtype=float)
            if start_params is not None and np.asarray(start_params).shape == (8,) and np.isfinite(start_params).all()
            else model.start_params
        )
        fitted, converged = _fit_model(train_endog, train_factor, candidate_start, method="lbfgs", maxiter=maxiter)
        optimization_method = "lbfgs"
        if fitted is None or not converged:
            powell_fit, powell_converged = _fit_model(
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
                refined_fit, refined_converged = _fit_model(
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
        extended_model = StructuralReleaseStateSpaceModel(extended_endog, extended_factor)
        filtered = extended_model.filter(np.asarray(fitted.params, dtype=float))
        current_state = float(filtered.filtered_state[0, -1])
        forecasts = {target_id: current_state for target_id in POINT_TARGETS}
        for target_id, value in known_releases.items():
            if value is not None:
                forecasts[target_id] = float(value)

        return StructuralReleaseFit(
            forecasts=forecasts,
            params=np.asarray(fitted.params, dtype=float),
            converged=converged,
            optimization_method=optimization_method,
            loglikelihood=float(getattr(fitted, "llf", np.nan)),
        )
    except Exception as exc:  # pragma: no cover - numerical fallback
        LOGGER.warning("Structural release model fit failed; falling back to regression benchmark: %s", exc)
        return None
