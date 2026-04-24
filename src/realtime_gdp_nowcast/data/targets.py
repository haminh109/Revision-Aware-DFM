from __future__ import annotations

import logging

import numpy as np
import pandas as pd

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.data.time import quarter_label_to_period
from realtime_gdp_nowcast.io import write_table

LOGGER = logging.getLogger(__name__)

RELEASE_STAGE_TO_TARGET_ID = {
    "first": "A",
    "second": "S",
    "third": "T",
}


def _normalize_quarter_label(value: str) -> str:
    return str(value).strip().replace(":", "")


def _annualized_growth(level: pd.Series, lag_level: pd.Series) -> pd.Series:
    ratio = pd.to_numeric(level, errors="coerce") / pd.to_numeric(lag_level, errors="coerce")
    return (np.power(ratio, 4.0) - 1.0) * 100.0


def _load_release_stage_targets(path: str | pd.io.common.FilePath) -> pd.DataFrame:
    raw = pd.read_csv(path)
    frame = raw[raw["release_stage"].isin(RELEASE_STAGE_TO_TARGET_ID)].copy()
    frame["target_quarter_label"] = frame["target_quarter"].map(_normalize_quarter_label)
    frame["target_id"] = frame["release_stage"].map(RELEASE_STAGE_TO_TARGET_ID)
    frame["value"] = pd.to_numeric(frame["value"], errors="coerce")
    wide = (
        frame.pivot_table(
            index="target_quarter_label",
            columns="target_id",
            values="value",
            aggfunc="last",
        )
        .reset_index()
        .rename_axis(None, axis=1)
    )
    return wide


def _load_mature_targets(path: str | pd.io.common.FilePath) -> pd.DataFrame:
    raw = pd.read_csv(path)
    raw["target_quarter_label"] = raw["target_quarter"].map(_normalize_quarter_label)
    raw["vintage_period_label"] = raw["vintage_period"].map(_normalize_quarter_label)
    raw["target_quarter_period"] = raw["target_quarter_label"].map(quarter_label_to_period)
    raw["vintage_period"] = raw["vintage_period_label"].map(quarter_label_to_period)
    raw["target_ord"] = pd.PeriodIndex(raw["target_quarter_period"], freq="Q-DEC").asi8
    raw["vintage_ord"] = pd.PeriodIndex(raw["vintage_period"], freq="Q-DEC").asi8
    raw["level"] = pd.to_numeric(raw["value"], errors="coerce")
    raw = raw.sort_values(["vintage_ord", "target_ord"]).reset_index(drop=True)

    raw["lag_target_ord"] = raw.groupby("vintage_ord")["target_ord"].shift(1)
    raw["lag_level"] = raw.groupby("vintage_ord")["level"].shift(1)
    contiguous = raw["target_ord"] - raw["lag_target_ord"] == 1
    raw.loc[~contiguous, "lag_level"] = np.nan
    raw["mature_growth"] = _annualized_growth(raw["level"], raw["lag_level"])
    mature = raw[raw["vintage_ord"] - raw["target_ord"] == 12].copy()
    mature = mature[["target_quarter_label", "mature_growth"]].rename(columns={"mature_growth": "M"})
    return mature.drop_duplicates(subset=["target_quarter_label"]).reset_index(drop=True)


def build_targets(settings: ProjectSettings) -> pd.DataFrame:
    release_stage_path = settings.paths.silver_data / "targets" / "gdp_release_stage_silver.csv"
    complete_vintages_path = settings.paths.silver_data / "targets" / "gdp_complete_vintages_silver.csv"
    if not release_stage_path.exists() or not complete_vintages_path.exists():
        raise FileNotFoundError("Missing silver target files. Stage 2 inputs must exist before Stage 3 starts.")

    fst = _load_release_stage_targets(release_stage_path)
    mature = _load_mature_targets(complete_vintages_path)
    merged = fst.merge(mature, on="target_quarter_label", how="left")
    merged["DELTA_SA"] = merged["S"] - merged["A"]
    merged["DELTA_TS"] = merged["T"] - merged["S"]
    merged["DELTA_MT"] = merged["M"] - merged["T"]
    merged["is_pandemic_quarter"] = merged["target_quarter_label"].isin(settings.sample["pandemic_quarters"])
    merged = merged.sort_values("target_quarter_label").reset_index(drop=True)

    target_long = merged.melt(
        id_vars=["target_quarter_label", "is_pandemic_quarter"],
        value_vars=["A", "S", "T", "M", "DELTA_SA", "DELTA_TS", "DELTA_MT"],
        var_name="target_id",
        value_name="realized_value",
    )
    target_long["revision_target_flag"] = target_long["target_id"].str.startswith("DELTA_")

    LOGGER.info("Built processed target layer with %s quarters", len(merged))
    write_table(merged, settings.paths.processed_data / "targets_wide.parquet")
    write_table(merged, settings.paths.processed_data / "targets_wide.csv")
    write_table(target_long, settings.paths.processed_data / "targets.parquet")
    write_table(target_long, settings.paths.processed_data / "targets.csv")
    return target_long
