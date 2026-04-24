from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.evaluation.run import run as run_evaluation
from realtime_gdp_nowcast.io import write_text


def _build_nowcast_path_figure(forecasts: pd.DataFrame, settings: ProjectSettings) -> Path:
    quarter = settings.project["report_recent_quarter"]
    subset = forecasts[
        (forecasts["target_quarter_label"] == quarter)
        & (forecasts["target_id"] == "A")
        & forecasts["model_id"].isin(["bridge", "standard_dfm", "release_dfm", "revision_dfm"])
        & (forecasts["snapshot_mode"] == "exact")
    ].copy()
    order = [checkpoint["checkpoint_id"] for checkpoint in settings.checkpoints]
    subset["checkpoint_id"] = pd.Categorical(subset["checkpoint_id"], categories=order, ordered=True)
    subset = subset.sort_values(["model_id", "checkpoint_id"])

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=subset, x="checkpoint_id", y="forecast_value", hue="model_id", marker="o", ax=ax)
    if not subset.empty:
        ax.axhline(subset["realized_value"].iloc[0], color="black", linestyle="--", label="realized")
    ax.set_title(f"Advance GDP nowcast path for {quarter}")
    ax.set_xlabel("Checkpoint")
    ax.set_ylabel("Forecast")
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()
    path = settings.paths.outputs / "figures" / "nowcast_path.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def _build_update_decomposition_figure(forecasts: pd.DataFrame, settings: ProjectSettings) -> Path:
    subset = forecasts[
        (forecasts["target_id"] == "A")
        & (forecasts["model_id"] == "release_dfm")
        & (forecasts["snapshot_mode"] == "exact")
        & ~forecasts["revision_target_flag"]
    ].copy()
    order = [checkpoint["checkpoint_id"] for checkpoint in settings.checkpoints]
    subset["checkpoint_id"] = pd.Categorical(subset["checkpoint_id"], categories=order, ordered=True)
    subset = subset.sort_values(["target_quarter", "checkpoint_id"])
    subset["forecast_change"] = subset.groupby("target_quarter")["forecast_value"].diff().abs()
    summary = subset.groupby("checkpoint_id", dropna=False, observed=False)["forecast_change"].mean().reset_index()

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=summary, x="checkpoint_id", y="forecast_change", color="#35608f", ax=ax)
    ax.set_title("Average absolute nowcast update by checkpoint")
    ax.set_xlabel("Checkpoint")
    ax.set_ylabel("Average absolute update")
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()
    path = settings.paths.outputs / "figures" / "forecast_update_decomposition.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def build_report(settings: ProjectSettings) -> str:
    artifacts = run_evaluation(settings)
    point_table = artifacts["main_text_point_table"]
    revision_table = artifacts["main_text_revision_table"]
    ablation = artifacts["ablation"]
    forecasts = artifacts["forecasts"]

    nowcast_path = _build_nowcast_path_figure(forecasts, settings)
    update_path = _build_update_decomposition_figure(forecasts, settings)

    best_point = (
        point_table.sort_values(["target_id", "RMSE"])
        .groupby(["target_id", "snapshot_mode", "checkpoint_id"], as_index=False)
        .first()
    )
    best_revision = (
        revision_table.sort_values(["target_id", "RMSE"])
        .groupby(["target_id", "snapshot_mode", "checkpoint_id"], as_index=False)
        .first()
    )

    report = f"""# Paper Draft Report

## Scope

- Main targets: {", ".join(settings.reporting["main_text_targets"])}
- Forecast modes: exact and pseudo real-time
- Models currently implemented: `ar`, `bridge`, `standard_dfm`, `release_dfm`, `revision_dfm`

## Best Point-Forecast Results (Main Text Sample)

{best_point.to_markdown(index=False)}

## Best Revision-Forecast Results (Main Text Sample)

{best_revision.to_markdown(index=False) if not best_revision.empty else "Revision results not available yet."}

## Exact vs Pseudo Ablation

{ablation.to_markdown(index=False)}

## Figures

- Nowcast path: `{nowcast_path}`
- Update decomposition: `{update_path}`

## Notes

- `standard_dfm`, `release_dfm`, and `revision_dfm` now share a common state-space factor extraction layer rather than the earlier PCA-only approximation.
- `revision_dfm` now runs as a structural latent-state state-space model for the GDP release ladder, with run diagnostics available in `outputs/diagnostics/revision_dfm_diagnostics.parquet`.
- `release_dfm` now runs as a structural release-ladder state-space model, with run diagnostics available in `outputs/diagnostics/release_dfm_diagnostics.parquet`.
- Full diagnostic tables remain available in `outputs/tables/point_forecast_table.csv` and `outputs/tables/revision_forecast_table.csv`.
"""
    write_text(report, settings.paths.outputs / "reports" / "paper_draft_report.md")
    return report
