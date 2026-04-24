from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.evaluation.run import build_evaluation_artifacts, load_forecasts, write_evaluation_outputs
from realtime_gdp_nowcast.io import write_table, write_text


def _headline_rows(frame: pd.DataFrame, checkpoint_map: dict[str, str]) -> pd.DataFrame:
    subset = frame.copy()
    subset = subset[subset["target_id"].isin(checkpoint_map)].copy()
    subset = subset[subset.apply(lambda row: row["checkpoint_id"] == checkpoint_map[row["target_id"]], axis=1)].copy()
    return subset.reset_index(drop=True)


def _best_rows(frame: pd.DataFrame, group_keys: list[str]) -> pd.DataFrame:
    if frame.empty:
        return frame
    return frame.sort_values(group_keys + ["RMSE", "MAE"]).groupby(group_keys, as_index=False).first()


def _headline_exact_vs_pseudo(headline_point_table: pd.DataFrame) -> pd.DataFrame:
    ablation = headline_point_table.pivot_table(
        index=["model_id", "target_id", "checkpoint_id"],
        columns="snapshot_mode",
        values="RMSE",
        aggfunc="first",
    ).reset_index()
    if {"exact", "pseudo"}.issubset(ablation.columns):
        ablation["rmse_gap_exact_minus_pseudo"] = ablation["exact"] - ablation["pseudo"]
    return ablation.sort_values(["target_id", "model_id"])


def _pandemic_excluded_artifacts(settings: ProjectSettings, forecasts: pd.DataFrame) -> dict[str, pd.DataFrame]:
    excluded = set(settings.sample["pandemic_quarters"])
    filtered = forecasts[~forecasts["target_quarter_label"].isin(excluded)].copy()
    return build_evaluation_artifacts(settings, filtered)


def _best_headline_report_table(headline_point_table: pd.DataFrame) -> pd.DataFrame:
    return _best_rows(headline_point_table, ["target_id", "snapshot_mode"])


def _best_headline_revision_report_table(headline_revision_table: pd.DataFrame) -> pd.DataFrame:
    return _best_rows(headline_revision_table, ["target_id", "snapshot_mode"])


def _build_headline_gap_figure(headline_ablation: pd.DataFrame, settings: ProjectSettings) -> Path:
    subset = headline_ablation.copy()
    if subset.empty or "rmse_gap_exact_minus_pseudo" not in subset.columns:
        path = settings.paths.outputs / "figures" / "submission_exact_vs_pseudo_gap.png"
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.axis("off")
        ax.text(0.5, 0.5, "No exact-vs-pseudo gap available.", ha="center", va="center")
        fig.tight_layout()
        fig.savefig(path, dpi=150)
        plt.close(fig)
        return path

    heatmap_data = subset.pivot_table(
        index="model_id",
        columns="target_id",
        values="rmse_gap_exact_minus_pseudo",
        aggfunc="first",
    )
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.heatmap(heatmap_data, annot=True, fmt=".3f", cmap="RdBu_r", center=0.0, ax=ax)
    ax.set_title("Headline RMSE gap: exact minus pseudo")
    ax.set_xlabel("Target")
    ax.set_ylabel("Model")
    fig.tight_layout()
    path = settings.paths.outputs / "figures" / "submission_exact_vs_pseudo_gap.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def build_submission_pack(settings: ProjectSettings) -> str:
    forecasts = load_forecasts(settings)
    full_artifacts = build_evaluation_artifacts(settings, forecasts)
    write_evaluation_outputs(settings, full_artifacts)

    point_checkpoint_map = dict(settings.reporting["headline_point_checkpoints"])
    revision_checkpoint_map = dict(settings.reporting["headline_revision_checkpoints"])

    headline_point_table = _headline_rows(full_artifacts["main_text_point_table"], point_checkpoint_map)
    headline_revision_table = _headline_rows(full_artifacts["main_text_revision_table"], revision_checkpoint_map)
    headline_ablation = _headline_exact_vs_pseudo(headline_point_table)
    headline_best = _best_headline_report_table(headline_point_table)
    headline_revision_best = _best_headline_revision_report_table(headline_revision_table)

    robustness_artifacts = _pandemic_excluded_artifacts(settings, forecasts)
    pandemic_excluded_headline_point = _headline_rows(robustness_artifacts["main_text_point_table"], point_checkpoint_map)
    pandemic_excluded_headline_revision = _headline_rows(
        robustness_artifacts["main_text_revision_table"],
        revision_checkpoint_map,
    )

    comparison_columns = ["model_id", "snapshot_mode", "target_id", "checkpoint_id"]
    pandemic_gap = headline_point_table[comparison_columns + ["RMSE"]].merge(
        pandemic_excluded_headline_point[comparison_columns + ["RMSE"]].rename(columns={"RMSE": "RMSE_no_pandemic"}),
        on=comparison_columns,
        how="left",
    )
    pandemic_gap = pandemic_gap.rename(columns={"RMSE": "RMSE_full_sample"})
    pandemic_gap["rmse_change_no_pandemic_minus_full"] = pandemic_gap["RMSE_no_pandemic"] - pandemic_gap["RMSE_full_sample"]

    figure_path = _build_headline_gap_figure(headline_ablation, settings)

    write_table(headline_point_table, settings.paths.outputs / "tables" / "headline_point_results.csv")
    write_table(headline_revision_table, settings.paths.outputs / "tables" / "headline_revision_results.csv")
    write_table(headline_ablation, settings.paths.outputs / "tables" / "headline_exact_vs_pseudo.csv")
    write_table(headline_best, settings.paths.outputs / "tables" / "headline_point_winners.csv")
    write_table(headline_revision_best, settings.paths.outputs / "tables" / "headline_revision_winners.csv")
    write_table(
        pandemic_excluded_headline_point,
        settings.paths.outputs / "tables" / "headline_point_results_no_pandemic.csv",
    )
    write_table(
        pandemic_excluded_headline_revision,
        settings.paths.outputs / "tables" / "headline_revision_results_no_pandemic.csv",
    )
    write_table(pandemic_gap, settings.paths.outputs / "tables" / "headline_point_pandemic_robustness.csv")

    report = f"""# Submission Mode Report

## Headline Design

- Point targets use release-relevant checkpoints only: A at `{point_checkpoint_map['A']}`, S at `{point_checkpoint_map['S']}`, T at `{point_checkpoint_map['T']}`.
- Revision targets use release-relevant checkpoints only: DELTA_SA at `{revision_checkpoint_map['DELTA_SA']}`, DELTA_TS at `{revision_checkpoint_map['DELTA_TS']}`.
- Pandemic robustness excludes: {", ".join(settings.sample["pandemic_quarters"])}.

## Headline Point-Forecast Winners

{headline_best.to_markdown(index=False)}

## Headline Revision-Forecast Winners

{headline_revision_best.to_markdown(index=False) if not headline_revision_best.empty else "No headline revision rows available."}

## Headline Exact vs Pseudo

{headline_ablation.to_markdown(index=False)}

## Pandemic Robustness For Headline Point Results

{pandemic_gap.to_markdown(index=False)}

## Suggested Main Narrative

- At the earliest release-relevant checkpoint for `A`, the current winner is `standard_dfm`, which means the factor-extraction upgrade materially strengthened the non-release baseline.
- `release_dfm` and `revision_dfm` dominate the later release-relevant checkpoints for `S` and `T`, which is the main evidence in favor of structured release modeling.
- Exact timing helps more clearly for the later structured checkpoints than for the earliest `A` checkpoint, so the timing contribution should be framed as heterogeneous rather than universal.
- Revision forecasting is currently economically interpretable but should be framed as an extension rather than the make-or-break contribution.

## Artifacts

- Headline point table: `{settings.paths.outputs / "tables" / "headline_point_results.csv"}`
- Headline revision table: `{settings.paths.outputs / "tables" / "headline_revision_results.csv"}`
- Headline ablation: `{settings.paths.outputs / "tables" / "headline_exact_vs_pseudo.csv"}`
- Pandemic robustness: `{settings.paths.outputs / "tables" / "headline_point_pandemic_robustness.csv"}`
- Gap figure: `{figure_path}`
"""
    write_text(report, settings.paths.outputs / "reports" / "submission_mode_report.md")
    return report
