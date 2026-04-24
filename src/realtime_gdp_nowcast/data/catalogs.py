from __future__ import annotations

import pandas as pd

from realtime_gdp_nowcast.config import ProjectSettings


def load_series_catalog(settings: ProjectSettings) -> pd.DataFrame:
    df = pd.read_csv(settings.paths.series_catalog)
    df["required_in_v1"] = df["required_in_v1"].astype(str).str.lower().eq("true")
    return df.sort_values(["required_in_v1", "series_id"], ascending=[False, True]).reset_index(drop=True)


def load_target_catalog(settings: ProjectSettings) -> pd.DataFrame:
    df = pd.read_csv(settings.paths.target_catalog)
    df["is_main_text_target"] = df["is_main_text_target"].astype(str).str.lower().eq("true")
    return df


def all_series(settings: ProjectSettings) -> pd.DataFrame:
    return load_series_catalog(settings).reset_index(drop=True)


def required_series(settings: ProjectSettings) -> pd.DataFrame:
    return all_series(settings).query("required_in_v1").reset_index(drop=True)
