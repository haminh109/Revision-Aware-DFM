from __future__ import annotations

import json
import logging
import shutil
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from realtime_gdp_nowcast.config import ProjectSettings, load_settings
from realtime_gdp_nowcast.data.calendars import build_release_calendar
from realtime_gdp_nowcast.data.snapshots import build_snapshots
from realtime_gdp_nowcast.data.targets import build_targets
from realtime_gdp_nowcast.data.event_panel import build_event_panel
from realtime_gdp_nowcast.data.time import quarter_label_to_period
from realtime_gdp_nowcast.evaluation.run import build_evaluation_artifacts, load_forecasts, write_evaluation_outputs
from realtime_gdp_nowcast.io import write_table, write_text
from realtime_gdp_nowcast.models import ar, bridge, release_dfm, revision_dfm, standard_dfm

LOGGER = logging.getLogger(__name__)

POINT_COMPARISON_KEYS = ["model_id", "snapshot_mode", "target_id", "checkpoint_id"]
REVISION_COMPARISON_KEYS = ["model_id", "snapshot_mode", "target_id", "checkpoint_id"]


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


def _best_headline_report_table(headline_point_table: pd.DataFrame) -> pd.DataFrame:
    return _best_rows(headline_point_table, ["target_id", "snapshot_mode"])


def _best_headline_revision_report_table(headline_revision_table: pd.DataFrame) -> pd.DataFrame:
    return _best_rows(headline_revision_table, ["target_id", "snapshot_mode"])


def _build_headline_gap_figure(headline_ablation: pd.DataFrame, settings: ProjectSettings) -> Path:
    subset = headline_ablation.copy()
    path = settings.paths.outputs / "figures" / "submission_exact_vs_pseudo_gap.png"
    if subset.empty or "rmse_gap_exact_minus_pseudo" not in subset.columns:
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
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def _coerce_quarter_period(frame: pd.DataFrame) -> pd.DataFrame:
    coerced = frame.copy()
    coerced["target_quarter_period"] = coerced["target_quarter_label"].map(quarter_label_to_period)
    return coerced


def _filter_forecasts(
    forecasts: pd.DataFrame,
    *,
    start_quarter: str | None = None,
    end_quarter: str | None = None,
    excluded_quarters: list[str] | None = None,
) -> pd.DataFrame:
    filtered = _coerce_quarter_period(forecasts)
    if start_quarter is not None:
        filtered = filtered[filtered["target_quarter_period"] >= pd.Period(start_quarter, freq="Q-DEC")]
    if end_quarter is not None:
        filtered = filtered[filtered["target_quarter_period"] <= pd.Period(end_quarter, freq="Q-DEC")]
    if excluded_quarters:
        excluded = {pd.Period(label, freq="Q-DEC") for label in excluded_quarters}
        filtered = filtered[~filtered["target_quarter_period"].isin(excluded)]
    return filtered.drop(columns=["target_quarter_period"]).copy()


def _subsample_artifacts(
    settings: ProjectSettings,
    forecasts: pd.DataFrame,
    *,
    start_quarter: str | None = None,
    end_quarter: str | None = None,
    excluded_quarters: list[str] | None = None,
) -> dict[str, pd.DataFrame]:
    filtered = _filter_forecasts(
        forecasts,
        start_quarter=start_quarter,
        end_quarter=end_quarter,
        excluded_quarters=excluded_quarters,
    )
    return build_evaluation_artifacts(settings, filtered)


def _headline_tables_from_artifacts(
    settings: ProjectSettings,
    artifacts: dict[str, pd.DataFrame],
) -> dict[str, pd.DataFrame]:
    point_checkpoint_map = dict(settings.reporting["headline_point_checkpoints"])
    revision_checkpoint_map = dict(settings.reporting["headline_revision_checkpoints"])
    headline_point_table = _headline_rows(artifacts["main_text_point_table"], point_checkpoint_map)
    headline_revision_table = _headline_rows(artifacts["main_text_revision_table"], revision_checkpoint_map)
    return {
        "headline_point": headline_point_table,
        "headline_revision": headline_revision_table,
        "headline_ablation": _headline_exact_vs_pseudo(headline_point_table),
        "headline_point_best": _best_headline_report_table(headline_point_table),
        "headline_revision_best": _best_headline_revision_report_table(headline_revision_table),
    }


def _comparison_table(
    base_table: pd.DataFrame,
    scenario_table: pd.DataFrame,
    *,
    comparison_keys: list[str],
    scenario_name: str,
    scenario_label: str,
) -> pd.DataFrame:
    renamed = scenario_table[comparison_keys + ["RMSE", "MAE", "DM_test", "DM_test_small_sample", "sign_accuracy", "n_forecasts", "n_comparable"]].rename(
        columns={
            "RMSE": "RMSE_scenario",
            "MAE": "MAE_scenario",
            "DM_test": "DM_test_scenario",
            "DM_test_small_sample": "DM_test_small_sample_scenario",
            "sign_accuracy": "sign_accuracy_scenario",
            "n_forecasts": "n_forecasts_scenario",
            "n_comparable": "n_comparable_scenario",
        }
    )
    merged = base_table.merge(renamed, on=comparison_keys, how="left")
    merged["scenario_name"] = scenario_name
    merged["scenario_label"] = scenario_label
    merged["rmse_delta_scenario_minus_main"] = merged["RMSE_scenario"] - merged["RMSE"]
    merged["mae_delta_scenario_minus_main"] = merged["MAE_scenario"] - merged["MAE"]
    return merged.sort_values(["scenario_name", "target_id", "snapshot_mode", "model_id"]).reset_index(drop=True)


def _small_sample_dm_table(headline_table: pd.DataFrame) -> pd.DataFrame:
    columns = [
        "model_id",
        "snapshot_mode",
        "target_id",
        "checkpoint_id",
        "RMSE",
        "MAE",
        "DM_test",
        "DM_test_small_sample",
        "n_forecasts",
        "n_comparable",
    ]
    available_columns = [column for column in columns if column in headline_table.columns]
    return headline_table[available_columns].copy().sort_values(["target_id", "snapshot_mode", "model_id"])


def _run_scenario_pipeline(base_settings: ProjectSettings, config_path: str) -> tuple[ProjectSettings, dict[str, pd.DataFrame]]:
    scenario_settings = load_settings(
        root=base_settings.paths.root,
        config_path=base_settings.paths.root / config_path,
    )
    LOGGER.info("Running robustness scenario pipeline | config=%s", scenario_settings.config_path)
    build_targets(scenario_settings)
    build_release_calendar(scenario_settings)
    build_event_panel(scenario_settings)
    build_snapshots(scenario_settings)
    ar.run(scenario_settings)
    bridge.run(scenario_settings)
    standard_dfm.run(scenario_settings)
    release_dfm.run(scenario_settings)
    revision_dfm.run(scenario_settings)
    forecasts = load_forecasts(scenario_settings)
    artifacts = build_evaluation_artifacts(scenario_settings, forecasts)
    write_evaluation_outputs(scenario_settings, artifacts)
    return scenario_settings, artifacts


def _freeze_submission_artifacts(
    settings: ProjectSettings,
    files_to_copy: dict[str, Path],
    headline_best: pd.DataFrame,
    headline_revision_best: pd.DataFrame,
) -> Path:
    freeze_name = str(settings.get("robustness", "freeze_name", default="submission_final"))
    freeze_root = settings.paths.outputs / "frozen" / freeze_name
    freeze_root.mkdir(parents=True, exist_ok=True)

    copied_files: dict[str, str] = {}
    for artifact_name, source_path in files_to_copy.items():
        destination = freeze_root / source_path.name
        shutil.copy2(source_path, destination)
        copied_files[artifact_name] = str(destination)

    manifest = {
        "generated_at_utc": pd.Timestamp.utcnow().isoformat(),
        "config_path": str(settings.config_path),
        "freeze_name": freeze_name,
        "artifacts": copied_files,
        "headline_point_winners": headline_best.to_dict(orient="records"),
        "headline_revision_winners": headline_revision_best.to_dict(orient="records"),
    }
    manifest_path = freeze_root / "freeze_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    manifest_md = "\n".join(
        [
            "# Frozen Submission Build",
            "",
            f"- Generated at (UTC): {manifest['generated_at_utc']}",
            f"- Config: `{settings.config_path}`",
            "",
            "## Copied Artifacts",
            "",
            *[f"- {name}: `{path}`" for name, path in copied_files.items()],
            "",
            "## Headline Point Winners",
            "",
            headline_best.to_markdown(index=False),
            "",
            "## Headline Revision Winners",
            "",
            headline_revision_best.to_markdown(index=False) if not headline_revision_best.empty else "No headline revision winners available.",
            "",
        ]
    )
    write_text(manifest_md, freeze_root / "freeze_manifest.md")
    return freeze_root


def build_submission_pack(settings: ProjectSettings) -> str:
    forecasts = load_forecasts(settings)
    full_artifacts = build_evaluation_artifacts(settings, forecasts)
    write_evaluation_outputs(settings, full_artifacts)

    headline = _headline_tables_from_artifacts(settings, full_artifacts)
    headline_point_table = headline["headline_point"]
    headline_revision_table = headline["headline_revision"]
    headline_ablation = headline["headline_ablation"]
    headline_best = headline["headline_point_best"]
    headline_revision_best = headline["headline_revision_best"]

    pandemic_excluded_artifacts = _subsample_artifacts(
        settings,
        forecasts,
        excluded_quarters=list(settings.sample["pandemic_quarters"]),
    )
    pandemic_headline = _headline_tables_from_artifacts(settings, pandemic_excluded_artifacts)
    pandemic_excluded_headline_point = pandemic_headline["headline_point"]
    pandemic_excluded_headline_revision = pandemic_headline["headline_revision"]

    comparison_columns = ["model_id", "snapshot_mode", "target_id", "checkpoint_id"]
    pandemic_gap = headline_point_table[comparison_columns + ["RMSE"]].merge(
        pandemic_excluded_headline_point[comparison_columns + ["RMSE"]].rename(columns={"RMSE": "RMSE_no_pandemic"}),
        on=comparison_columns,
        how="left",
    )
    pandemic_gap = pandemic_gap.rename(columns={"RMSE": "RMSE_full_sample"})
    pandemic_gap["sample_name"] = "no_pandemic"
    pandemic_gap["sample_label"] = "Exclude pandemic quarters"
    pandemic_gap["rmse_change_sample_minus_full"] = pandemic_gap["RMSE_no_pandemic"] - pandemic_gap["RMSE_full_sample"]

    subsample_comparisons_point: list[pd.DataFrame] = [pandemic_gap]
    subsample_comparisons_revision: list[pd.DataFrame] = []
    point_subsample_tables: dict[str, pd.DataFrame] = {
        "headline_point_results_no_pandemic.csv": pandemic_excluded_headline_point,
    }
    revision_subsample_tables: dict[str, pd.DataFrame] = {
        "headline_revision_results_no_pandemic.csv": pandemic_excluded_headline_revision,
    }

    for sample_name, sample_config in dict(settings.get("robustness", "subsamples", default={})).items():
        subsample_artifacts = _subsample_artifacts(
            settings,
            forecasts,
            start_quarter=sample_config.get("start_quarter"),
            end_quarter=sample_config.get("end_quarter"),
        )
        subsample_headline = _headline_tables_from_artifacts(settings, subsample_artifacts)
        point_table = subsample_headline["headline_point"]
        revision_table = subsample_headline["headline_revision"]
        point_subsample_tables[f"headline_point_results_{sample_name}.csv"] = point_table
        revision_subsample_tables[f"headline_revision_results_{sample_name}.csv"] = revision_table

        point_comparison = headline_point_table[comparison_columns + ["RMSE", "MAE"]].merge(
            point_table[comparison_columns + ["RMSE", "MAE"]].rename(
                columns={"RMSE": "RMSE_sample", "MAE": "MAE_sample"}
            ),
            on=comparison_columns,
            how="left",
        )
        point_comparison = point_comparison.rename(columns={"RMSE": "RMSE_full_sample", "MAE": "MAE_full_sample"})
        point_comparison["sample_name"] = sample_name
        point_comparison["sample_label"] = sample_config.get("label", sample_name.replace("_", " ").title())
        point_comparison["rmse_change_sample_minus_full"] = (
            point_comparison["RMSE_sample"] - point_comparison["RMSE_full_sample"]
        )
        point_comparison["mae_change_sample_minus_full"] = (
            point_comparison["MAE_sample"] - point_comparison["MAE_full_sample"]
        )
        subsample_comparisons_point.append(point_comparison)

        if not revision_table.empty:
            revision_comparison = headline_revision_table[REVISION_COMPARISON_KEYS + ["RMSE", "MAE", "sign_accuracy"]].merge(
                revision_table[REVISION_COMPARISON_KEYS + ["RMSE", "MAE", "sign_accuracy"]].rename(
                    columns={
                        "RMSE": "RMSE_sample",
                        "MAE": "MAE_sample",
                        "sign_accuracy": "sign_accuracy_sample",
                    }
                ),
                on=REVISION_COMPARISON_KEYS,
                how="left",
            )
            revision_comparison = revision_comparison.rename(
                columns={
                    "RMSE": "RMSE_full_sample",
                    "MAE": "MAE_full_sample",
                    "sign_accuracy": "sign_accuracy_full_sample",
                }
            )
            revision_comparison["sample_name"] = sample_name
            revision_comparison["sample_label"] = sample_config.get("label", sample_name.replace("_", " ").title())
            revision_comparison["rmse_change_sample_minus_full"] = (
                revision_comparison["RMSE_sample"] - revision_comparison["RMSE_full_sample"]
            )
            subsample_comparisons_revision.append(revision_comparison)

    point_scenario_comparisons: list[pd.DataFrame] = []
    revision_scenario_comparisons: list[pd.DataFrame] = []
    scenario_winners: list[pd.DataFrame] = []
    for scenario_name, config_path in dict(settings.get("robustness", "scenario_configs", default={})).items():
        scenario_label = scenario_name.replace("_", " ").title()
        scenario_settings, scenario_artifacts = _run_scenario_pipeline(settings, config_path)
        scenario_headline = _headline_tables_from_artifacts(scenario_settings, scenario_artifacts)
        point_scenario_comparisons.append(
            _comparison_table(
                headline_point_table,
                scenario_headline["headline_point"],
                comparison_keys=POINT_COMPARISON_KEYS,
                scenario_name=scenario_name,
                scenario_label=scenario_label,
            )
        )
        if not scenario_headline["headline_revision"].empty:
            revision_scenario_comparisons.append(
                _comparison_table(
                    headline_revision_table,
                    scenario_headline["headline_revision"],
                    comparison_keys=REVISION_COMPARISON_KEYS,
                    scenario_name=scenario_name,
                    scenario_label=scenario_label,
                )
            )
        scenario_best = scenario_headline["headline_point_best"].copy()
        scenario_best["scenario_name"] = scenario_name
        scenario_best["scenario_label"] = scenario_label
        scenario_best["scenario_outputs"] = str(scenario_settings.paths.outputs)
        scenario_winners.append(scenario_best)

    point_scenario_robustness = pd.concat(point_scenario_comparisons, ignore_index=True) if point_scenario_comparisons else pd.DataFrame()
    revision_scenario_robustness = (
        pd.concat(revision_scenario_comparisons, ignore_index=True) if revision_scenario_comparisons else pd.DataFrame()
    )
    scenario_winner_table = pd.concat(scenario_winners, ignore_index=True) if scenario_winners else pd.DataFrame()

    point_subsample_robustness = pd.concat(subsample_comparisons_point, ignore_index=True)
    revision_subsample_robustness = (
        pd.concat(subsample_comparisons_revision, ignore_index=True) if subsample_comparisons_revision else pd.DataFrame()
    )

    point_small_sample_dm = _small_sample_dm_table(headline_point_table)
    revision_small_sample_dm = _small_sample_dm_table(headline_revision_table)
    figure_path = _build_headline_gap_figure(headline_ablation, settings)

    key_outputs = {
        "headline_point_results": settings.paths.outputs / "tables" / "headline_point_results.csv",
        "headline_revision_results": settings.paths.outputs / "tables" / "headline_revision_results.csv",
        "headline_exact_vs_pseudo": settings.paths.outputs / "tables" / "headline_exact_vs_pseudo.csv",
        "submission_mode_report": settings.paths.outputs / "reports" / "submission_mode_report.md",
    }

    write_table(headline_point_table, key_outputs["headline_point_results"])
    write_table(headline_revision_table, key_outputs["headline_revision_results"])
    write_table(headline_ablation, key_outputs["headline_exact_vs_pseudo"])
    write_table(headline_best, settings.paths.outputs / "tables" / "headline_point_winners.csv")
    write_table(headline_revision_best, settings.paths.outputs / "tables" / "headline_revision_winners.csv")
    write_table(point_small_sample_dm, settings.paths.outputs / "tables" / "headline_point_small_sample_dm.csv")
    write_table(revision_small_sample_dm, settings.paths.outputs / "tables" / "headline_revision_small_sample_dm.csv")

    for filename, table in point_subsample_tables.items():
        write_table(table, settings.paths.outputs / "tables" / filename)
    for filename, table in revision_subsample_tables.items():
        write_table(table, settings.paths.outputs / "tables" / filename)

    write_table(pandemic_gap, settings.paths.outputs / "tables" / "headline_point_pandemic_robustness.csv")
    write_table(point_subsample_robustness, settings.paths.outputs / "tables" / "headline_point_subsample_robustness.csv")
    if not revision_subsample_robustness.empty:
        write_table(
            revision_subsample_robustness,
            settings.paths.outputs / "tables" / "headline_revision_subsample_robustness.csv",
        )
    if not point_scenario_robustness.empty:
        write_table(point_scenario_robustness, settings.paths.outputs / "tables" / "headline_point_scenario_robustness.csv")
    if not revision_scenario_robustness.empty:
        write_table(
            revision_scenario_robustness,
            settings.paths.outputs / "tables" / "headline_revision_scenario_robustness.csv",
        )
    if not scenario_winner_table.empty:
        write_table(scenario_winner_table, settings.paths.outputs / "tables" / "headline_scenario_winners.csv")

    report = f"""# Submission Mode Report

## Headline Design

- Point targets use release-relevant checkpoints only: A at `{settings.reporting["headline_point_checkpoints"]["A"]}`, S at `{settings.reporting["headline_point_checkpoints"]["S"]}`, T at `{settings.reporting["headline_point_checkpoints"]["T"]}`.
- Revision targets use release-relevant checkpoints only: DELTA_SA at `{settings.reporting["headline_revision_checkpoints"]["DELTA_SA"]}`, DELTA_TS at `{settings.reporting["headline_revision_checkpoints"]["DELTA_TS"]}`.
- Pandemic robustness excludes: {", ".join(settings.sample["pandemic_quarters"])}.

## Headline Point-Forecast Winners

{headline_best.to_markdown(index=False)}

## Headline Revision-Forecast Winners

{headline_revision_best.to_markdown(index=False) if not headline_revision_best.empty else "No headline revision rows available."}

## Headline Exact vs Pseudo

{headline_ablation.to_markdown(index=False)}

## Subsample Robustness

{point_subsample_robustness.to_markdown(index=False)}

## Scenario Robustness

{point_scenario_robustness.to_markdown(index=False) if not point_scenario_robustness.empty else "No scenario robustness rows available."}

## Small-Sample DM Headline Table

{point_small_sample_dm.to_markdown(index=False)}

## Suggested Main Narrative

- The frozen headline pack should continue to emphasize later-release gains from structured models rather than claiming universal dominance at the earliest `A` checkpoint.
- Excluding the pandemic and splitting the sample around the GFC are now part of the default submission pack, so any strong claim should be retained only if it survives both filters.
- `expanded_panel` tests whether the results are driven by a narrow indicator set, while `alternative_data_choice` tests whether retail/trade measurement choices are driving the headline findings.
- The small-sample DM table should be cited whenever the comparable sample is short enough that asymptotic p-values may look optimistic.

## Artifacts

- Headline point table: `{key_outputs["headline_point_results"]}`
- Headline revision table: `{key_outputs["headline_revision_results"]}`
- Headline ablation: `{key_outputs["headline_exact_vs_pseudo"]}`
- Point subsample robustness: `{settings.paths.outputs / "tables" / "headline_point_subsample_robustness.csv"}`
- Point scenario robustness: `{settings.paths.outputs / "tables" / "headline_point_scenario_robustness.csv"}`
- Small-sample DM table: `{settings.paths.outputs / "tables" / "headline_point_small_sample_dm.csv"}`
- Gap figure: `{figure_path}`
"""
    write_text(report, key_outputs["submission_mode_report"])

    freeze_files = {
        **key_outputs,
        "headline_point_subsample_robustness": settings.paths.outputs / "tables" / "headline_point_subsample_robustness.csv",
        "headline_point_small_sample_dm": settings.paths.outputs / "tables" / "headline_point_small_sample_dm.csv",
    }
    point_scenario_path = settings.paths.outputs / "tables" / "headline_point_scenario_robustness.csv"
    if point_scenario_path.exists():
        freeze_files["headline_point_scenario_robustness"] = point_scenario_path

    freeze_root = _freeze_submission_artifacts(
        settings,
        freeze_files,
        headline_best=headline_best,
        headline_revision_best=headline_revision_best,
    )
    LOGGER.info("Frozen submission artifacts at %s", freeze_root)
    return report
