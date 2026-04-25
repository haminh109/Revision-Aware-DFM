from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import erfc, sqrt
from pathlib import Path

import numpy as np
import pandas as pd

from full_state_space_release_revision_dfm.data_adapter import load_gdp_release_panel
from full_state_space_release_revision_dfm.joint_indicator_revision_dfm import (
    JointIndicatorRevisionDFMConfig,
    fit_joint_indicator_revision_dfm,
    forecast_gdp_releases,
)
from full_state_space_release_revision_dfm.release_revision_dfm import (
    ReleaseRevisionDFMConfig,
    fit_release_revision_dfm,
    forecast_release_row,
)


RELEASE_ORDER = ("A", "S", "T", "M")
CHECKPOINT_TARGETS = {
    "pre_advance": "A",
    "pre_second": "S",
    "pre_third": "T",
}
REVISION_TARGETS = {
    "DELTA_SA": ("pre_advance", "S", "A"),
    "DELTA_TS": ("pre_second", "T", "S"),
    "DELTA_MT": ("pre_third", "M", "T"),
}
CHECKPOINT_MONTH_OFFSET = {
    "pre_advance": 1,
    "pre_second": 2,
    "pre_third": 3,
}
MODEL_IDS = (
    "ar",
    "bridge",
    "standard_dfm",
    "release_dfm",
    "revision_dfm_kalman_em",
    "joint_indicator_revision_dfm_full_kalman_em",
)
DEFAULT_SERIES = (
    "PAYEMS",
    "UNRATE",
    "AWHMAN",
    "INDPRO",
    "TCU",
    "W875RX1",
    "RSAFS",
    "HOUST",
    "PERMIT",
    "DGORDER",
    "BUSINV",
    "BOPGSTB",
    "GS10",
    "TB3MS",
)
DEFAULT_GDP_RELEASE_CALENDAR = "data/silver/calendars/gdp_release_calendar_alfred.csv"
RATE_OR_LEVEL_SERIES = {"UNRATE", "TCU", "FEDFUNDS", "GS10", "TB3MS", "T10Y3MM", "UMCSENT"}
BLOCKS = {
    "labor_activity": ("PAYEMS", "UNRATE", "AWHMAN", "INDPRO", "TCU"),
    "consumption_income": ("W875RX1", "DSPIC96", "PCECC96", "RSAFS", "RSXFS", "UMCSENT"),
    "housing_orders": ("HOUST", "PERMIT", "DGORDER", "NEWORDER"),
    "trade_inventories": ("BUSINV", "ISRATIO", "BOPGSTB", "BOPTEXP", "BOPTIMP"),
    "financial": ("FEDFUNDS", "GS10", "TB3MS", "T10Y3MM"),
}


@dataclass(slots=True)
class ExactPseudoBacktestConfig:
    repo_root: Path
    output_dir: Path
    series_ids: tuple[str, ...] = DEFAULT_SERIES
    eval_start: str = "2005:Q1"
    eval_end: str = "2024:Q4"
    data_start: str = "1992-01-01"
    min_train: int = 48
    max_origins: int = 8
    n_factors: int = 1
    max_iter: int = 5
    tolerance: float = 1e-4
    maturity_lag_quarters: int = 12
    gdp_release_calendar_path: Path | None = None


def _quarter_to_period(label: str) -> pd.Period:
    year, quarter = label.split(":Q")
    return pd.Period(year=int(year), quarter=int(quarter), freq="Q")


def _period_to_label(period: pd.Period) -> str:
    return f"{period.year}:Q{period.quarter}"


def _quarter_end(label: str) -> pd.Timestamp:
    return _quarter_to_period(label).to_timestamp(how="end").normalize()


def _load_gdp_release_calendar(config: ExactPseudoBacktestConfig) -> pd.DataFrame:
    path = config.gdp_release_calendar_path or config.repo_root / DEFAULT_GDP_RELEASE_CALENDAR
    if not path.exists():
        return pd.DataFrame()
    calendar = pd.read_csv(path, parse_dates=["public_release_date"])
    required = {"target_quarter", "release_round", "public_release_date", "derivation_status"}
    missing = required.difference(calendar.columns)
    if missing:
        raise ValueError(f"GDP release calendar is missing columns: {sorted(missing)}")
    return calendar


def _origin_date(
    target_quarter: str,
    checkpoint_id: str,
    timing_mode: str,
    gdp_release_calendar: pd.DataFrame | None = None,
) -> pd.Timestamp:
    quarter_end = _quarter_end(target_quarter)
    month_end = quarter_end + pd.offsets.MonthEnd(CHECKPOINT_MONTH_OFFSET[checkpoint_id])
    if timing_mode == "pseudo":
        return month_end.normalize()
    if timing_mode == "exact":
        release_round = CHECKPOINT_TARGETS[checkpoint_id]
        if gdp_release_calendar is not None and not gdp_release_calendar.empty:
            match = gdp_release_calendar.loc[
                gdp_release_calendar["target_quarter"].astype(str).eq(str(target_quarter))
                & gdp_release_calendar["release_round"].astype(str).eq(release_round)
            ]
            if not match.empty:
                release_date = pd.Timestamp(match.iloc[0]["public_release_date"]).normalize()
                return (release_date - pd.offsets.BDay(1)).normalize()
        return (month_end - pd.offsets.BDay(1)).normalize()
    raise ValueError(f"Unknown timing_mode: {timing_mode}")


def _load_release_panel(repo_root: Path) -> pd.DataFrame:
    panel = load_gdp_release_panel(repo_root / "data/bronze/targets/gdp_release_targets.csv")
    periods = [_quarter_to_period(label) for label in panel.index]
    ordered = panel.assign(_period=periods).sort_values("_period").drop(columns="_period")
    return ordered.loc[:, RELEASE_ORDER]


def _load_alfred_monthly_long(config: ExactPseudoBacktestConfig) -> pd.DataFrame:
    path = config.repo_root / "data/bronze/indicators/alfred_monthly_long.csv"
    raw = pd.read_csv(
        path,
        usecols=["series_id", "series_frequency", "observation_date", "realtime_start", "value_numeric"],
        parse_dates=["observation_date", "realtime_start"],
        low_memory=False,
    )
    frame = raw.loc[raw["series_frequency"].eq("monthly")].copy()
    frame = frame[frame["series_id"].isin(config.series_ids)]
    frame = frame[frame["observation_date"] >= pd.Timestamp(config.data_start)]
    frame["value_numeric"] = pd.to_numeric(frame["value_numeric"], errors="coerce")
    frame = frame[np.isfinite(frame["value_numeric"])]
    return frame.sort_values(["series_id", "observation_date", "realtime_start"])


def _quarterly_average(panel: pd.DataFrame) -> pd.DataFrame:
    if panel.empty:
        return pd.DataFrame()
    q = panel.resample("QE").mean()
    q.index = [_period_to_label(period) for period in q.index.to_period("Q")]
    return q


def _snapshot_indicator_panels(
    raw: pd.DataFrame,
    origin_date: pd.Timestamp,
    series_ids: tuple[str, ...],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    available = raw.loc[raw["realtime_start"] <= origin_date]
    if available.empty:
        empty = pd.DataFrame(columns=list(series_ids))
        return empty, empty

    first = available.groupby(["series_id", "observation_date"], as_index=False).first()
    current = available.groupby(["series_id", "observation_date"], as_index=False).last()
    first_panel = first.pivot(index="observation_date", columns="series_id", values="value_numeric").sort_index()
    current_panel = current.pivot(index="observation_date", columns="series_id", values="value_numeric").sort_index()
    common = [series for series in series_ids if series in first_panel.columns and series in current_panel.columns]
    first_q = _quarterly_average(first_panel.loc[:, common])
    current_q = _quarterly_average(current_panel.loc[:, common])
    return first_q, current_q


def _transform_quarterly_panel(panel: pd.DataFrame) -> pd.DataFrame:
    transformed = pd.DataFrame(index=panel.index)
    for col in panel.columns:
        series = pd.to_numeric(panel[col], errors="coerce").astype(float)
        if col in RATE_OR_LEVEL_SERIES:
            transformed[col] = series.diff()
        elif (series.dropna() > 0).all():
            with np.errstate(invalid="ignore", divide="ignore"):
                transformed[col] = 400.0 * np.log(series).diff()
        else:
            transformed[col] = series.diff()
    return transformed.replace([np.inf, -np.inf], np.nan)


def _standardize_by_train(features: pd.DataFrame, train_index: pd.Index) -> pd.DataFrame:
    train = features.loc[features.index.intersection(train_index)]
    means = train.mean(skipna=True)
    scales = train.std(skipna=True).replace(0.0, np.nan)
    scales = scales.fillna(1.0)
    standardized = (features - means) / scales
    return standardized.replace([np.inf, -np.inf], np.nan)


def _impute_with_train_means(features: pd.DataFrame, train_index: pd.Index) -> pd.DataFrame:
    train = features.loc[features.index.intersection(train_index)]
    means = train.mean(skipna=True).fillna(0.0)
    return features.fillna(means).fillna(0.0)


def _mask_release_panel_for_checkpoint(
    releases: pd.DataFrame,
    origin_pos: int,
    checkpoint_id: str,
    maturity_lag_quarters: int,
) -> pd.DataFrame:
    panel = releases.iloc[: origin_pos + 1].copy()
    positions = np.arange(len(panel))
    panel.loc[positions > origin_pos - maturity_lag_quarters, "M"] = np.nan
    current_idx = panel.index[-1]
    if checkpoint_id == "pre_advance":
        panel.loc[current_idx, ["A", "S", "T", "M"]] = np.nan
    elif checkpoint_id == "pre_second":
        panel.loc[current_idx, ["S", "T", "M"]] = np.nan
    elif checkpoint_id == "pre_third":
        panel.loc[current_idx, ["T", "M"]] = np.nan
    else:
        raise ValueError(f"Unknown checkpoint_id: {checkpoint_id}")
    return panel


def _evaluation_positions(releases: pd.DataFrame, config: ExactPseudoBacktestConfig) -> list[int]:
    start = _quarter_to_period(config.eval_start)
    end = _quarter_to_period(config.eval_end)
    positions: list[int] = []
    for pos, label in enumerate(releases.index):
        period = _quarter_to_period(str(label))
        if start <= period <= end and pos >= config.min_train and releases.loc[label, ["A", "S", "T"]].notna().any():
            positions.append(pos)
    if config.max_origins and config.max_origins > 0:
        positions = positions[-config.max_origins :]
    return positions


def _ols_predict(X_train: np.ndarray, y_train: np.ndarray, x_current: np.ndarray, ridge: float = 1e-6) -> float:
    X = np.asarray(X_train, dtype=float)
    y = np.asarray(y_train, dtype=float)
    x = np.asarray(x_current, dtype=float)
    mask = np.isfinite(y) & np.isfinite(X).all(axis=1)
    if mask.sum() < max(5, X.shape[1] + 2):
        return float(np.nanmean(y)) if np.isfinite(y).any() else np.nan
    X = X[mask]
    y = y[mask]
    X = np.column_stack([np.ones(len(X)), X])
    x = np.r_[1.0, np.nan_to_num(x, nan=0.0, posinf=0.0, neginf=0.0)]
    xtx = X.T @ X + ridge * np.eye(X.shape[1])
    xty = X.T @ y
    beta = np.linalg.solve(xtx, xty)
    return float(x @ beta)


def _select_ar_lag(y: pd.Series, max_lag: int = 4) -> int:
    values = pd.to_numeric(y, errors="coerce").dropna().to_numpy(dtype=float)
    best_lag = 1
    best_bic = np.inf
    for lag in range(1, max_lag + 1):
        if len(values) <= lag + 6:
            continue
        target = values[lag:]
        rows = np.column_stack([values[lag - j - 1 : len(values) - j - 1] for j in range(lag)])
        pred = np.array([_ols_predict(rows[:i], target[:i], rows[i]) for i in range(max(lag + 3, 5), len(target))])
        actual = target[max(lag + 3, 5) :]
        if len(actual) < 5:
            continue
        resid = actual - pred
        sse = float(np.nansum(resid**2))
        bic = len(actual) * np.log(max(sse / len(actual), 1e-12)) + (lag + 1) * np.log(len(actual))
        if bic < best_bic:
            best_bic = bic
            best_lag = lag
    return best_lag


def _forecast_ar(release_train: pd.DataFrame) -> dict[str, float]:
    forecasts: dict[str, float] = {}
    for target in RELEASE_ORDER:
        values = pd.to_numeric(release_train[target].iloc[:-1], errors="coerce").dropna()
        if len(values) < 8:
            forecasts[target] = float(values.mean()) if len(values) else np.nan
            continue
        lag = _select_ar_lag(values)
        y = values.to_numpy(dtype=float)
        target_y = y[lag:]
        X = np.column_stack([y[lag - j - 1 : len(y) - j - 1] for j in range(lag)])
        current_x = np.array([y[-j - 1] for j in range(lag)])
        forecasts[target] = _ols_predict(X, target_y, current_x)
    return forecasts


def _block_features(features: pd.DataFrame) -> pd.DataFrame:
    blocks = pd.DataFrame(index=features.index)
    for block_name, members in BLOCKS.items():
        cols = [col for col in members if col in features.columns]
        if cols:
            blocks[block_name] = features.loc[:, cols].mean(axis=1, skipna=True)
    return blocks


def _forecast_bridge(features: pd.DataFrame, release_train: pd.DataFrame) -> dict[str, float]:
    features = features.reindex(release_train.index)
    train_index = release_train.index[:-1]
    current_index = release_train.index[-1]
    standardized = _standardize_by_train(_transform_quarterly_panel(features), train_index)
    blocks = _block_features(standardized)
    blocks = _impute_with_train_means(blocks, train_index)
    forecasts: dict[str, float] = {}
    for target in RELEASE_ORDER:
        y = release_train[target]
        lag = y.shift(1)
        X = blocks.copy()
        X[f"{target}_lag1"] = lag
        train_mask = X.index.isin(train_index)
        forecasts[target] = _ols_predict(
            X.loc[train_mask].to_numpy(dtype=float),
            y.loc[train_mask].to_numpy(dtype=float),
            X.loc[current_index].to_numpy(dtype=float),
        )
    return forecasts


def _fit_factor_panel(features: pd.DataFrame, train_index: pd.Index, n_factors: int) -> pd.DataFrame:
    transformed = _standardize_by_train(_transform_quarterly_panel(features), train_index)
    filled = _impute_with_train_means(transformed, train_index)
    train = filled.loc[filled.index.intersection(train_index)]
    if train.shape[0] < 6 or train.shape[1] < 2:
        factor = filled.mean(axis=1).to_frame("factor_1")
        return factor
    centered_train = train - train.mean(axis=0)
    train_array = np.clip(
        np.nan_to_num(centered_train.to_numpy(dtype=float), nan=0.0, posinf=0.0, neginf=0.0),
        -25.0,
        25.0,
    )
    _, _, vh = np.linalg.svd(train_array, full_matrices=False)
    k = min(n_factors, vh.shape[0])
    centered_all = filled - train.mean(axis=0)
    all_array = np.clip(
        np.nan_to_num(centered_all.to_numpy(dtype=float), nan=0.0, posinf=0.0, neginf=0.0),
        -25.0,
        25.0,
    )
    with np.errstate(invalid="ignore", divide="ignore", over="ignore"):
        scores = all_array @ vh[:k].T
    scores = np.nan_to_num(scores, nan=0.0, posinf=0.0, neginf=0.0)
    return pd.DataFrame(scores, index=filled.index, columns=[f"factor_{i + 1}" for i in range(k)])


def _known_release_features(release_train: pd.DataFrame, checkpoint_id: str) -> list[str]:
    if checkpoint_id == "pre_advance":
        return []
    if checkpoint_id == "pre_second":
        return ["A"]
    if checkpoint_id == "pre_third":
        return ["A", "S"]
    return []


def _forecast_standard_dfm(features: pd.DataFrame, release_train: pd.DataFrame, n_factors: int) -> dict[str, float]:
    features = features.reindex(release_train.index)
    train_index = release_train.index[:-1]
    current_index = release_train.index[-1]
    factors = _fit_factor_panel(features, train_index, n_factors)
    forecasts: dict[str, float] = {}
    for target in RELEASE_ORDER:
        y = release_train[target]
        train_mask = factors.index.isin(train_index)
        forecasts[target] = _ols_predict(
            factors.loc[train_mask].to_numpy(dtype=float),
            y.loc[train_mask].to_numpy(dtype=float),
            factors.loc[current_index].to_numpy(dtype=float),
        )
    return forecasts


def _forecast_release_dfm(
    features: pd.DataFrame,
    release_train: pd.DataFrame,
    checkpoint_id: str,
    n_factors: int,
) -> dict[str, float]:
    features = features.reindex(release_train.index)
    train_index = release_train.index[:-1]
    current_index = release_train.index[-1]
    factors = _fit_factor_panel(features, train_index, n_factors)
    known_cols = _known_release_features(release_train, checkpoint_id)
    design = factors.copy()
    for col in known_cols:
        design[f"known_{col}"] = release_train[col]
    design = _impute_with_train_means(design, train_index)
    forecasts: dict[str, float] = {}
    for target in RELEASE_ORDER:
        y = release_train[target]
        train_mask = design.index.isin(train_index)
        forecasts[target] = _ols_predict(
            design.loc[train_mask].to_numpy(dtype=float),
            y.loc[train_mask].to_numpy(dtype=float),
            design.loc[current_index].to_numpy(dtype=float),
        )
    return forecasts


def _forecast_revision_dfm_kalman(
    features: pd.DataFrame,
    release_train: pd.DataFrame,
    config: ExactPseudoBacktestConfig,
) -> tuple[dict[str, float], dict[str, object]]:
    transformed = _transform_quarterly_panel(features).reindex(release_train.index)
    model_config = ReleaseRevisionDFMConfig(
        n_factors=config.n_factors,
        max_iter=config.max_iter,
        tolerance=config.tolerance,
        verbose=False,
    )
    result = fit_release_revision_dfm(transformed, release_train.loc[:, RELEASE_ORDER], config=model_config)
    forecasts = forecast_release_row(result)
    return forecasts, _em_diagnostics(result.loglikelihood_history, result.converged, result.n_iter)


def _forecast_joint_indicator_revision_dfm(
    first_features: pd.DataFrame,
    current_features: pd.DataFrame,
    release_train: pd.DataFrame,
    config: ExactPseudoBacktestConfig,
) -> tuple[dict[str, float], dict[str, object]]:
    first = _transform_quarterly_panel(first_features).reindex(release_train.index)
    current = _transform_quarterly_panel(current_features).reindex(release_train.index)
    model_config = JointIndicatorRevisionDFMConfig(
        n_factors=config.n_factors,
        max_iter=config.max_iter,
        tolerance=config.tolerance,
        verbose=False,
    )
    result = fit_joint_indicator_revision_dfm(
        first,
        release_train.loc[:, RELEASE_ORDER],
        monthly_mature_panel=current,
        config=model_config,
    )
    forecasts = forecast_gdp_releases(result)
    return forecasts, _em_diagnostics(result.loglikelihood_history, result.converged, result.n_iter)


def _em_diagnostics(history: list[float], converged: bool, n_iter: int) -> dict[str, object]:
    clean = [float(value) for value in history if np.isfinite(value)]
    llf_initial = clean[0] if clean else np.nan
    llf_final = clean[-1] if clean else np.nan
    if len(clean) >= 2:
        last_improvement = clean[-1] - clean[-2]
        relative_last_improvement = abs(last_improvement) / (1.0 + abs(clean[-2]))
    else:
        last_improvement = np.nan
        relative_last_improvement = np.nan
    return {
        "converged": bool(converged),
        "n_iter": int(n_iter),
        "loglikelihood": llf_final,
        "llf_initial": llf_initial,
        "llf_final": llf_final,
        "llf_last_improvement": last_improvement,
        "llf_relative_last_improvement": relative_last_improvement,
        "llf_history_length": int(len(history)),
    }


def _forecast_all_models(
    first_features: pd.DataFrame,
    current_features: pd.DataFrame,
    release_train: pd.DataFrame,
    checkpoint_id: str,
    config: ExactPseudoBacktestConfig,
) -> dict[str, dict[str, object]]:
    outputs: dict[str, dict[str, object]] = {}
    outputs["ar"] = {"forecasts": _forecast_ar(release_train), "converged": True, "n_iter": 0, "loglikelihood": np.nan}
    outputs["bridge"] = {
        "forecasts": _forecast_bridge(current_features, release_train),
        "converged": True,
        "n_iter": 0,
        "loglikelihood": np.nan,
    }
    outputs["standard_dfm"] = {
        "forecasts": _forecast_standard_dfm(current_features, release_train, config.n_factors),
        "converged": True,
        "n_iter": 0,
        "loglikelihood": np.nan,
    }
    outputs["release_dfm"] = {
        "forecasts": _forecast_release_dfm(current_features, release_train, checkpoint_id, config.n_factors),
        "converged": True,
        "n_iter": 0,
        "loglikelihood": np.nan,
    }
    try:
        forecasts, diagnostics = _forecast_revision_dfm_kalman(current_features, release_train, config)
        outputs["revision_dfm_kalman_em"] = {
            "forecasts": forecasts,
            **diagnostics,
        }
    except Exception as exc:  # pragma: no cover - operational path
        outputs["revision_dfm_kalman_em"] = {"forecasts": {}, "converged": False, "n_iter": 0, "loglikelihood": np.nan, "error": str(exc)}
    try:
        forecasts, diagnostics = _forecast_joint_indicator_revision_dfm(
            first_features,
            current_features,
            release_train,
            config,
        )
        outputs["joint_indicator_revision_dfm_full_kalman_em"] = {
            "forecasts": forecasts,
            **diagnostics,
        }
    except Exception as exc:  # pragma: no cover - operational path
        outputs["joint_indicator_revision_dfm_full_kalman_em"] = {
            "forecasts": {},
            "converged": False,
            "n_iter": 0,
            "loglikelihood": np.nan,
            "error": str(exc),
        }
    return outputs


def _dm_pvalue(model_errors: pd.Series, baseline_errors: pd.Series) -> float:
    aligned = pd.concat([model_errors, baseline_errors], axis=1, join="inner").dropna()
    if aligned.shape[0] < 5:
        return np.nan
    differential = aligned.iloc[:, 0] ** 2 - aligned.iloc[:, 1] ** 2
    sd = differential.std(ddof=1)
    if not np.isfinite(sd) or sd <= 1e-12:
        return 1.0
    t_stat = float(differential.mean() / (sd / np.sqrt(len(differential))))
    return float(erfc(abs(t_stat) / sqrt(2.0)))


def _summarize_forecasts(forecasts: pd.DataFrame, group_col: str) -> pd.DataFrame:
    if forecasts.empty:
        return pd.DataFrame()
    rows: list[dict[str, object]] = []
    group_keys = ["timing_mode", "checkpoint_id", group_col]
    for keys, group in forecasts.groupby(group_keys, dropna=False):
        timing_mode, checkpoint_id, target_id = keys
        baseline = group.loc[group["model_id"].eq("ar")].set_index("target_quarter")["forecast_error"]
        baseline_rmse = np.sqrt(np.mean(baseline**2)) if len(baseline) else np.nan
        for model_id, model_group in group.groupby("model_id", dropna=False):
            error = model_group["forecast_error"]
            rmse = float(np.sqrt(np.mean(error**2)))
            model_errors = model_group.set_index("target_quarter")["forecast_error"]
            sign_hit = np.sign(model_group["forecast_value"]) == np.sign(model_group["realized_value"])
            rows.append(
                {
                    "model_id": model_id,
                    "timing_mode": timing_mode,
                    "checkpoint_id": checkpoint_id,
                    group_col: target_id,
                    "n_forecasts": int(error.notna().sum()),
                    "RMSE": rmse,
                    "MAE": float(np.mean(np.abs(error))),
                    "bias": float(np.mean(error)),
                    "relative_RMSFE": float(rmse / baseline_rmse) if baseline_rmse and np.isfinite(baseline_rmse) else np.nan,
                    "DM_test": 1.0 if model_id == "ar" else _dm_pvalue(model_errors, baseline),
                    "sign_accuracy": float(sign_hit.mean()),
                    "convergence_rate": float(model_group["converged"].mean()),
                    "mean_iterations": float(model_group["n_iter"].mean()),
                    "mean_llf_relative_last_improvement": float(
                        pd.to_numeric(model_group.get("llf_relative_last_improvement", np.nan), errors="coerce").mean()
                    ),
                    "median_llf_relative_last_improvement": float(
                        pd.to_numeric(model_group.get("llf_relative_last_improvement", np.nan), errors="coerce").median()
                    ),
                    "max_llf_relative_last_improvement": float(
                        pd.to_numeric(model_group.get("llf_relative_last_improvement", np.nan), errors="coerce").max()
                    ),
                }
            )
    return pd.DataFrame(rows)


def _build_exact_pseudo_gaps(metrics: pd.DataFrame, id_col: str) -> pd.DataFrame:
    if metrics.empty:
        return pd.DataFrame()
    pivot = metrics.pivot_table(
        index=["model_id", "checkpoint_id", id_col],
        columns="timing_mode",
        values="RMSE",
        aggfunc="first",
    ).reset_index()
    if "exact" not in pivot or "pseudo" not in pivot:
        pivot["exact_minus_pseudo_RMSE"] = np.nan
    else:
        pivot["exact_minus_pseudo_RMSE"] = pivot["exact"] - pivot["pseudo"]
    return pivot


def run_exact_pseudo_backtest(config: ExactPseudoBacktestConfig) -> dict[str, pd.DataFrame]:
    releases = _load_release_panel(config.repo_root)
    raw = _load_alfred_monthly_long(config)
    gdp_release_calendar = _load_gdp_release_calendar(config)
    positions = _evaluation_positions(releases, config)
    point_rows: list[dict[str, object]] = []
    revision_rows: list[dict[str, object]] = []
    failure_rows: list[dict[str, object]] = []
    snapshot_cache: dict[pd.Timestamp, tuple[pd.DataFrame, pd.DataFrame]] = {}

    for origin_pos in positions:
        target_quarter = str(releases.index[origin_pos])
        for timing_mode in ("exact", "pseudo"):
            for checkpoint_id, point_target in CHECKPOINT_TARGETS.items():
                origin_date = _origin_date(target_quarter, checkpoint_id, timing_mode, gdp_release_calendar)
                if origin_date not in snapshot_cache:
                    snapshot_cache[origin_date] = _snapshot_indicator_panels(raw, origin_date, config.series_ids)
                first_q, current_q = snapshot_cache[origin_date]
                release_train = _mask_release_panel_for_checkpoint(
                    releases,
                    origin_pos,
                    checkpoint_id,
                    config.maturity_lag_quarters,
                )
                model_outputs = _forecast_all_models(first_q, current_q, release_train, checkpoint_id, config)
                for model_id, payload in model_outputs.items():
                    if payload.get("error"):
                        failure_rows.append(
                            {
                                "model_id": model_id,
                                "timing_mode": timing_mode,
                                "forecast_origin": f"{target_quarter}:{checkpoint_id}:{timing_mode}",
                                "forecast_origin_date": origin_date.date().isoformat(),
                                "checkpoint_id": checkpoint_id,
                                "target_quarter": target_quarter,
                                "error_message": payload["error"],
                            }
                        )
                    forecasts = payload.get("forecasts", {})
                    forecast_value = forecasts.get(point_target, np.nan)
                    realized_value = releases.iloc[origin_pos][point_target]
                    if np.isfinite(forecast_value) and np.isfinite(realized_value):
                        point_rows.append(
                            {
                                "model_id": model_id,
                                "timing_mode": timing_mode,
                                "forecast_origin": f"{target_quarter}:{checkpoint_id}:{timing_mode}",
                                "forecast_origin_date": origin_date.date().isoformat(),
                                "checkpoint_id": checkpoint_id,
                                "target_id": point_target,
                                "target_quarter": target_quarter,
                                "forecast_value": float(forecast_value),
                                "realized_value": float(realized_value),
                                "forecast_error": float(forecast_value - realized_value),
                                "revision_target_flag": False,
                                "converged": bool(payload.get("converged", False)),
                                "n_iter": int(payload.get("n_iter", 0) or 0),
                                "loglikelihood": payload.get("loglikelihood", np.nan),
                                "llf_initial": payload.get("llf_initial", np.nan),
                                "llf_final": payload.get("llf_final", np.nan),
                                "llf_last_improvement": payload.get("llf_last_improvement", np.nan),
                                "llf_relative_last_improvement": payload.get("llf_relative_last_improvement", np.nan),
                                "llf_history_length": payload.get("llf_history_length", np.nan),
                                "n_indicators": int(current_q.shape[1]),
                            }
                        )
                    for revision_id, (revision_checkpoint, high_release, low_release) in REVISION_TARGETS.items():
                        if revision_checkpoint != checkpoint_id:
                            continue
                        high_forecast = forecasts.get(high_release, np.nan)
                        low_forecast = forecasts.get(low_release, np.nan)
                        high_realized = releases.iloc[origin_pos][high_release]
                        low_realized = releases.iloc[origin_pos][low_release]
                        if all(np.isfinite(x) for x in [high_forecast, low_forecast, high_realized, low_realized]):
                            forecast_revision = float(high_forecast - low_forecast)
                            realized_revision = float(high_realized - low_realized)
                            revision_rows.append(
                                {
                                    "model_id": model_id,
                                    "timing_mode": timing_mode,
                                    "forecast_origin": f"{target_quarter}:{checkpoint_id}:{timing_mode}",
                                    "forecast_origin_date": origin_date.date().isoformat(),
                                    "checkpoint_id": checkpoint_id,
                                    "target_id": revision_id,
                                    "revision_target_id": revision_id,
                                    "target_quarter": target_quarter,
                                    "forecast_value": forecast_revision,
                                    "realized_value": realized_revision,
                                    "forecast_error": forecast_revision - realized_revision,
                                    "revision_target_flag": True,
                                    "converged": bool(payload.get("converged", False)),
                                    "n_iter": int(payload.get("n_iter", 0) or 0),
                                    "loglikelihood": payload.get("loglikelihood", np.nan),
                                    "llf_initial": payload.get("llf_initial", np.nan),
                                    "llf_final": payload.get("llf_final", np.nan),
                                    "llf_last_improvement": payload.get("llf_last_improvement", np.nan),
                                    "llf_relative_last_improvement": payload.get("llf_relative_last_improvement", np.nan),
                                    "llf_history_length": payload.get("llf_history_length", np.nan),
                                    "n_indicators": int(current_q.shape[1]),
                                }
                            )

    point_forecasts = pd.DataFrame(point_rows)
    revision_forecasts = pd.DataFrame(revision_rows)
    point_metrics = _summarize_forecasts(point_forecasts, "target_id")
    revision_metrics = _summarize_forecasts(revision_forecasts, "revision_target_id")
    return {
        "forecast_results": point_forecasts,
        "revision_forecast_results": revision_forecasts,
        "metrics_summary": point_metrics,
        "revision_metrics_summary": revision_metrics,
        "exact_pseudo_point_gaps": _build_exact_pseudo_gaps(point_metrics, "target_id"),
        "exact_pseudo_revision_gaps": _build_exact_pseudo_gaps(revision_metrics, "revision_target_id"),
        "failures": pd.DataFrame(failure_rows),
        "gdp_release_calendar_used": gdp_release_calendar,
    }


def write_outputs(outputs: dict[str, pd.DataFrame], config: ExactPseudoBacktestConfig) -> None:
    config.output_dir.mkdir(parents=True, exist_ok=True)
    file_map = {
        "forecast_results": "forecast_results.csv",
        "revision_forecast_results": "revision_forecast_results.csv",
        "metrics_summary": "metrics_summary.csv",
        "revision_metrics_summary": "revision_metrics_summary.csv",
        "exact_pseudo_point_gaps": "exact_pseudo_point_gaps.csv",
        "exact_pseudo_revision_gaps": "exact_pseudo_revision_gaps.csv",
        "failures": "failures.csv",
        "gdp_release_calendar_used": "gdp_release_calendar_used.csv",
    }
    for key, filename in file_map.items():
        outputs[key].to_csv(config.output_dir / filename, index=False)
    _write_summary(outputs, config)


def _write_summary(outputs: dict[str, pd.DataFrame], config: ExactPseudoBacktestConfig) -> None:
    lines = [
        "# Exact/Pseudo Real-Time Backtest",
        "",
        "This run compares AR, bridge, standard DFM, release DFM, GDP revision DFM, and the full joint indicator-revision Kalman/EM model on the same forecast origins.",
        "",
        "## Configuration",
        "",
        f"- eval_start: `{config.eval_start}`",
        f"- eval_end: `{config.eval_end}`",
        f"- max_origins: `{config.max_origins}` (`0` means all eligible origins)",
        f"- min_train: `{config.min_train}` quarters",
        f"- n_factors: `{config.n_factors}`",
        f"- max_iter: `{config.max_iter}`",
        f"- maturity_lag_quarters: `{config.maturity_lag_quarters}`",
        f"- indicators: `{', '.join(config.series_ids)}`",
        "",
        "## GDP Release Calendar",
        "",
    ]
    calendar = outputs["gdp_release_calendar_used"]
    if calendar.empty:
        lines.extend(
            [
                "No GDP release calendar file was found. Exact checkpoint dates fell back to deterministic month-end approximations.",
                "",
            ]
        )
    else:
        status_counts = calendar["derivation_status"].value_counts().to_dict()
        eval_calendar = calendar.loc[
            calendar["target_quarter"].astype(str).between(config.eval_start, config.eval_end)
            & calendar["release_round"].astype(str).isin(["A", "S", "T"])
        ]
        eval_status_counts = eval_calendar["derivation_status"].value_counts().to_dict()
        lines.extend(
            [
                f"- rows loaded: `{len(calendar)}`",
                f"- derivation_status counts: `{status_counts}`",
                f"- eval-sample A/S/T derivation_status counts: `{eval_status_counts}`",
                "- exact checkpoint dates use one business day before the mapped GDP release date.",
                "",
            ]
        )
    lines.extend(
        [
        "## Timing Interpretation",
        "",
        "- `exact` snapshots use ALFRED vintages with `realtime_start <= forecast_origin_date`.",
        "- `pseudo` snapshots use a coarse month-end cutoff for the same release checkpoint month.",
        "- GDP release dates are loaded from the ALFRED GDPC1 vintage-derived calendar when available; otherwise the runner falls back to deterministic month-end approximations.",
        "",
        "## Point Metrics",
        "",
        ]
    )
    point_metrics = outputs["metrics_summary"]
    lines.append("No point metrics were produced." if point_metrics.empty else point_metrics.round(4).to_string(index=False))
    lines.extend(["", "## Revision Metrics", ""])
    revision_metrics = outputs["revision_metrics_summary"]
    lines.append("No revision metrics were produced." if revision_metrics.empty else revision_metrics.round(4).to_string(index=False))
    lines.extend(["", "## Failures", ""])
    failures = outputs["failures"]
    lines.append("No failures." if failures.empty else failures.to_string(index=False))
    lines.append("")
    (config.output_dir / "run_summary.md").write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run exact/pseudo release-aware backtest on existing repo artifacts.")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Defaults to <repo-root>/outputs/full_state_space_release_revision_dfm/exact_pseudo_backtest.",
    )
    parser.add_argument("--series", nargs="*", default=list(DEFAULT_SERIES))
    parser.add_argument("--eval-start", default="2005:Q1")
    parser.add_argument("--eval-end", default="2024:Q4")
    parser.add_argument("--data-start", default="1992-01-01")
    parser.add_argument("--min-train", type=int, default=48)
    parser.add_argument("--max-origins", type=int, default=8, help="Use most recent N eligible origins; pass 0 for all.")
    parser.add_argument("--n-factors", type=int, default=1)
    parser.add_argument("--max-iter", type=int, default=5)
    parser.add_argument("--tolerance", type=float, default=1e-4)
    parser.add_argument("--maturity-lag-quarters", type=int, default=12)
    parser.add_argument(
        "--gdp-release-calendar",
        type=Path,
        default=None,
        help=f"Defaults to <repo-root>/{DEFAULT_GDP_RELEASE_CALENDAR}.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = args.output_dir or args.repo_root / "outputs/full_state_space_release_revision_dfm/exact_pseudo_backtest"
    config = ExactPseudoBacktestConfig(
        repo_root=args.repo_root,
        output_dir=output_dir,
        series_ids=tuple(args.series),
        eval_start=args.eval_start,
        eval_end=args.eval_end,
        data_start=args.data_start,
        min_train=args.min_train,
        max_origins=args.max_origins,
        n_factors=args.n_factors,
        max_iter=args.max_iter,
        tolerance=args.tolerance,
        maturity_lag_quarters=args.maturity_lag_quarters,
        gdp_release_calendar_path=args.gdp_release_calendar,
    )
    outputs = run_exact_pseudo_backtest(config)
    write_outputs(outputs, config)
    print(f"Wrote exact/pseudo outputs to {config.output_dir}")
    print(f"Point forecasts: {len(outputs['forecast_results'])}")
    print(f"Revision forecasts: {len(outputs['revision_forecast_results'])}")
    print(f"Failures: {len(outputs['failures'])}")


if __name__ == "__main__":
    main()
