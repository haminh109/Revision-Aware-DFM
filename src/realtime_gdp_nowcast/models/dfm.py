from __future__ import annotations

import logging

import numpy as np
import pandas as pd

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.data.time import period_to_quarter_label
from realtime_gdp_nowcast.features.panel import impute_target_quarter_months, snapshot_to_monthly_matrix

LOGGER = logging.getLogger(__name__)


def estimate_quarterly_factor(snapshot_df: pd.DataFrame, target_quarter_label: str, settings: ProjectSettings) -> pd.DataFrame:
    monthly_matrix = snapshot_to_monthly_matrix(snapshot_df)
    if monthly_matrix.empty:
        return pd.DataFrame(columns=["target_quarter", "factor"])
    imputed = impute_target_quarter_months(
        monthly_matrix,
        target_quarter_label,
        max_lag=settings.models["standard_dfm"]["monthly_imputation_max_lag"],
    )
    imputed = imputed.replace([np.inf, -np.inf], np.nan).ffill().fillna(0.0)
    if imputed.shape[1] < 2 or imputed.shape[0] < 24:
        factor = imputed.mean(axis=1)
    else:
        centered = imputed - imputed.mean()
        _, _, vh = np.linalg.svd(centered.to_numpy(), full_matrices=False)
        first_component = vh[0]
        factor = pd.Series(centered.to_numpy() @ first_component, index=imputed.index)

    quarterly = factor.groupby(factor.index.asfreq("Q-DEC")).mean().rename("factor").reset_index()
    quarterly = quarterly.rename(columns={"index": "target_quarter"})
    quarterly["target_quarter_label"] = quarterly["target_quarter"].map(period_to_quarter_label)
    return quarterly
