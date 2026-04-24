from __future__ import annotations

import pandas as pd

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.evaluation.metrics import (
    bias,
    diebold_mariano,
    diebold_mariano_small_sample,
    mae,
    rmse,
    sign_accuracy,
)
from realtime_gdp_nowcast.io import write_table

GROUP_KEYS = ["snapshot_mode", "checkpoint_id", "target_id", "revision_target_flag"]


def _filter_main_text_point_table(metrics_summary: pd.DataFrame, checkpoint_order: list[str]) -> pd.DataFrame:
    cutoff_rank = {
        "A": checkpoint_order.index("pre_advance"),
        "S": checkpoint_order.index("pre_second"),
        "T": checkpoint_order.index("pre_third"),
    }
    frame = metrics_summary[~metrics_summary["revision_target_flag"]].copy()
    frame["checkpoint_rank"] = frame["checkpoint_id"].map({checkpoint_id: idx for idx, checkpoint_id in enumerate(checkpoint_order)})
    filtered = frame[frame.apply(lambda row: row["checkpoint_rank"] <= cutoff_rank.get(row["target_id"], -1), axis=1)].copy()
    return filtered.drop(columns=["checkpoint_rank"])


def _filter_main_text_revision_table(metrics_summary: pd.DataFrame, checkpoint_order: list[str]) -> pd.DataFrame:
    cutoff_rank = {
        "DELTA_SA": checkpoint_order.index("pre_second"),
        "DELTA_TS": checkpoint_order.index("pre_third"),
    }
    frame = metrics_summary[metrics_summary["revision_target_flag"]].copy()
    frame = frame[frame["target_id"].isin(cutoff_rank)].copy()
    frame["checkpoint_rank"] = frame["checkpoint_id"].map({checkpoint_id: idx for idx, checkpoint_id in enumerate(checkpoint_order)})
    filtered = frame[frame.apply(lambda row: row["checkpoint_rank"] <= cutoff_rank[row["target_id"]], axis=1)].copy()
    return filtered.drop(columns=["checkpoint_rank"])


def _align_with_reference(frame: pd.DataFrame, ref_frame: pd.DataFrame) -> pd.DataFrame:
    aligned = frame[
        [
            "target_quarter_label",
            "realized_value",
            "forecast_value",
        ]
    ].merge(
        ref_frame[["target_quarter_label", "forecast_value"]].rename(columns={"forecast_value": "reference_forecast"}),
        on="target_quarter_label",
        how="inner",
    )
    return aligned.dropna().reset_index(drop=True)


def load_forecasts(settings: ProjectSettings) -> pd.DataFrame:
    forecast_path = settings.paths.outputs / "forecasts" / "forecast_results.parquet"
    if not forecast_path.exists():
        raise FileNotFoundError("No forecasts found. Run model commands first.")
    forecasts = pd.read_parquet(forecast_path).copy()
    forecasts["error"] = forecasts["realized_value"] - forecasts["forecast_value"]
    return forecasts


def build_evaluation_artifacts(settings: ProjectSettings, forecasts: pd.DataFrame) -> dict[str, pd.DataFrame]:
    forecasts = forecasts.copy()
    reference_model = settings.reporting["benchmark_reference_model"]
    metrics_rows: list[dict[str, object]] = []
    reference_lookup = {
        key: frame for key, frame in forecasts[forecasts["model_id"] == reference_model].groupby(GROUP_KEYS)
    }

    for keys, frame in forecasts.groupby(["model_id", *GROUP_KEYS]):
        model_id, snapshot_mode, checkpoint_id, target_id, revision_target_flag = keys
        ref_frame = reference_lookup.get((snapshot_mode, checkpoint_id, target_id, revision_target_flag))
        relative_rmsfe = None
        dm_pvalue = None
        dm_pvalue_small_sample = None
        n_comparable = 0
        if ref_frame is not None and not ref_frame.empty:
            aligned = _align_with_reference(frame, ref_frame)
            n_comparable = len(aligned)
            ref_rmse = rmse(aligned["realized_value"] - aligned["reference_forecast"])
            model_rmse = rmse(aligned["realized_value"] - aligned["forecast_value"])
            relative_rmsfe = model_rmse / ref_rmse if ref_rmse and not pd.isna(ref_rmse) else None
            dm_pvalue = diebold_mariano(
                aligned["realized_value"],
                aligned["forecast_value"],
                aligned["reference_forecast"],
            )
            dm_pvalue_small_sample = diebold_mariano_small_sample(
                aligned["realized_value"],
                aligned["forecast_value"],
                aligned["reference_forecast"],
            )
        metrics_rows.append(
            {
                "model_id": model_id,
                "snapshot_mode": snapshot_mode,
                "checkpoint_id": checkpoint_id,
                "target_id": target_id,
                "revision_target_flag": revision_target_flag,
                "RMSE": rmse(frame["error"]),
                "MAE": mae(frame["error"]),
                "bias": bias(frame["error"]),
                "relative_RMSFE": relative_rmsfe,
                "DM_test": dm_pvalue,
                "DM_test_small_sample": dm_pvalue_small_sample,
                "sign_accuracy": sign_accuracy(frame["realized_value"], frame["forecast_value"]) if revision_target_flag else None,
                "n_forecasts": len(frame),
                "n_comparable": n_comparable,
            }
        )

    metrics_summary = pd.DataFrame(metrics_rows).sort_values(["target_id", "snapshot_mode", "checkpoint_id", "model_id"])
    main_targets = settings.reporting["main_text_targets"]
    point_table = metrics_summary[
        metrics_summary["target_id"].isin(main_targets) & ~metrics_summary["revision_target_flag"]
    ].copy()
    revision_table = metrics_summary[metrics_summary["revision_target_flag"]].copy()
    checkpoint_order = [checkpoint["checkpoint_id"] for checkpoint in settings.checkpoints]
    main_text_point_table = _filter_main_text_point_table(point_table, checkpoint_order)
    main_text_revision_table = _filter_main_text_revision_table(metrics_summary, checkpoint_order)

    ablation = main_text_point_table.pivot_table(
        index=["model_id", "checkpoint_id", "target_id"],
        columns="snapshot_mode",
        values="RMSE",
        aggfunc="first",
    ).reset_index()
    if {"exact", "pseudo"}.issubset(ablation.columns):
        ablation["rmse_gap_exact_minus_pseudo"] = ablation["exact"] - ablation["pseudo"]

    return {
        "metrics_summary": metrics_summary,
        "point_table": point_table,
        "revision_table": revision_table,
        "main_text_point_table": main_text_point_table,
        "main_text_revision_table": main_text_revision_table,
        "ablation": ablation,
        "forecasts": forecasts,
    }


def write_evaluation_outputs(settings: ProjectSettings, artifacts: dict[str, pd.DataFrame]) -> None:
    metrics_summary = artifacts["metrics_summary"]
    point_table = artifacts["point_table"]
    revision_table = artifacts["revision_table"]
    main_text_point_table = artifacts["main_text_point_table"]
    main_text_revision_table = artifacts["main_text_revision_table"]
    ablation = artifacts["ablation"]
    write_table(metrics_summary, settings.paths.outputs / "tables" / "metrics_summary.csv")
    write_table(point_table, settings.paths.outputs / "tables" / "point_forecast_table.csv")
    write_table(revision_table, settings.paths.outputs / "tables" / "revision_forecast_table.csv")
    write_table(main_text_point_table, settings.paths.outputs / "tables" / "main_text_point_forecast_table.csv")
    write_table(main_text_revision_table, settings.paths.outputs / "tables" / "main_text_revision_forecast_table.csv")
    write_table(ablation, settings.paths.outputs / "tables" / "ablation_exact_vs_pseudo.csv")


def run(settings: ProjectSettings) -> dict[str, pd.DataFrame]:
    forecasts = load_forecasts(settings)
    artifacts = build_evaluation_artifacts(settings, forecasts)
    write_evaluation_outputs(settings, artifacts)
    return artifacts
