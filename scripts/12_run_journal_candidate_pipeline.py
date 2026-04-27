from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT_FOR_IMPORT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT_FOR_IMPORT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT_FOR_IMPORT))

import pandas as pd

from full_state_space_release_revision_dfm.q2_benchmarks import build_public_spf_rgdp_growth_csv


OUTPUT_ROOT = Path("outputs/full_state_space_release_revision_dfm")
MATURE_TARGETS = {
    "baseline": None,
    "mature_1y": Path("data/bronze/targets/robustness/gdp_release_targets_mature_1y.csv"),
    "mature_3y": Path("data/bronze/targets/robustness/gdp_release_targets_mature_3y.csv"),
    "mature_latest": Path("data/bronze/targets/robustness/gdp_release_targets_mature_latest.csv"),
}


def _run(command: list[str], cwd: Path, dry_run: bool = False) -> None:
    print("$ " + " ".join(command), flush=True)
    if not dry_run:
        subprocess.run(command, cwd=cwd, check=True)


def _git_metadata(repo_root: Path) -> dict[str, object]:
    def run_git(args: list[str]) -> str:
        try:
            return subprocess.check_output(["git", *args], cwd=repo_root, text=True, stderr=subprocess.DEVNULL).strip()
        except Exception:
            return ""

    commit = run_git(["rev-parse", "HEAD"])
    status = run_git(["status", "--short"])
    return {
        "is_git_repo": bool(commit),
        "commit_hash": commit or "",
        "status_short": status,
        "dirty": bool(status),
    }


def _copytree(src: Path, dst: Path, dry_run: bool = False) -> None:
    print(f"copy {src} -> {dst}", flush=True)
    if dry_run:
        return
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def _build_run(
    repo_root: Path,
    run_name: str,
    max_iter: int,
    max_origins: int,
    n_factors: int,
    midas_lags: int,
    spf_forecasts: Path | None,
    mcs_bootstrap_reps: int,
    gdp_release_targets: Path | None,
    estimation_window: str,
    rolling_window_quarters: int,
    exclude_quarters: tuple[str, ...],
    parallel_jobs: int,
    dry_run: bool,
) -> dict[str, str]:
    run_dir = OUTPUT_ROOT / run_name
    report_dir = OUTPUT_ROOT / f"{run_name}_report_package"
    evidence_dir = OUTPUT_ROOT / f"{run_name}_journal_evidence"
    variance_dir = OUTPUT_ROOT / f"{run_name}_variance_audit"
    backtest_cmd = [
        sys.executable,
        "-m",
        "full_state_space_release_revision_dfm.exact_pseudo_backtest",
        "--max-origins",
        str(max_origins),
        "--max-iter",
        str(max_iter),
        "--n-factors",
        str(n_factors),
        "--midas-lags",
        str(midas_lags),
        "--estimation-window",
        estimation_window,
        "--rolling-window-quarters",
        str(rolling_window_quarters),
        "--parallel-jobs",
        str(parallel_jobs),
        "--output-dir",
        str(run_dir),
    ]
    if exclude_quarters:
        backtest_cmd.extend(["--exclude-quarters", *exclude_quarters])
    if spf_forecasts is not None:
        backtest_cmd.extend(["--spf-forecasts", str(spf_forecasts)])
    if gdp_release_targets is not None:
        backtest_cmd.extend(["--gdp-release-targets", str(gdp_release_targets)])
    _run(backtest_cmd, repo_root, dry_run)
    _run(
        [
            sys.executable,
            "-m",
            "full_state_space_release_revision_dfm.build_report_package",
            "--source-dir",
            str(run_dir),
            "--output-dir",
            str(report_dir),
        ],
        repo_root,
        dry_run,
    )
    _run(
        [
            sys.executable,
            "-m",
            "full_state_space_release_revision_dfm.build_journal_evidence_package",
            "--source-dir",
            str(run_dir),
            "--output-dir",
            str(evidence_dir),
            "--mcs-bootstrap-reps",
            str(mcs_bootstrap_reps),
        ],
        repo_root,
        dry_run,
    )
    _run(
        [
            sys.executable,
            "-m",
            "full_state_space_release_revision_dfm.build_variance_audit",
            "--source-dir",
            str(run_dir),
            "--output-dir",
            str(variance_dir),
        ],
        repo_root,
        dry_run,
    )
    return {
        "run_dir": str(run_dir),
        "report_dir": str(report_dir),
        "evidence_dir": str(evidence_dir),
        "variance_dir": str(variance_dir),
        "max_iter": str(max_iter),
        "n_factors": str(n_factors),
        "midas_lags": str(midas_lags),
        "estimation_window": estimation_window,
        "rolling_window_quarters": str(rolling_window_quarters),
        "exclude_quarters": ";".join(exclude_quarters),
        "parallel_jobs": str(parallel_jobs),
    }


def _safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size <= 1:
        return pd.DataFrame()
    return pd.read_csv(path)


def _copy_if_exists(src: Path, dst: Path) -> None:
    if src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def _write_freeze_audits(repo_root: Path, freeze_dir: Path, manifest: dict[str, object]) -> None:
    runs = manifest.get("runs", {})
    mature_runs = manifest.get("mature_robustness_runs", {})
    sensitivity_runs = manifest.get("sensitivity_runs", {})
    run_groups = {
        "main": runs if isinstance(runs, dict) else {},
        "mature": mature_runs if isinstance(mature_runs, dict) else {},
        "sensitivity": sensitivity_runs if isinstance(sensitivity_runs, dict) else {},
    }
    failure_rows: list[dict[str, object]] = []
    for group_name, entries in run_groups.items():
        for run_name, paths in entries.items():
            if not isinstance(paths, dict):
                continue
            run_dir = repo_root / str(paths.get("run_dir", ""))
            failures = _safe_read_csv(run_dir / "failures.csv")
            failure_rows.append(
                {
                    "run_group": group_name,
                    "run_name": run_name,
                    "failure_rows": int(len(failures)),
                    "run_dir": str(run_dir),
                }
            )
    pd.DataFrame(failure_rows).to_csv(freeze_dir / "FREEZE_FAILURE_AUDIT.csv", index=False)

    max_iters = manifest.get("max_iters", [])
    main_iter = max(max_iters) if isinstance(max_iters, list) and max_iters else None
    if main_iter is not None:
        main_run = f"exact_pseudo_backtest_max_iter{main_iter}"
        main_paths = runs.get(main_run, {}) if isinstance(runs, dict) else {}
        if isinstance(main_paths, dict):
            report_dir = repo_root / str(main_paths.get("report_dir", ""))
            variance_dir = repo_root / str(main_paths.get("variance_dir", ""))
            _copy_if_exists(report_dir / "headline_point_results.csv", freeze_dir / "HEADLINE_POINT_WINNERS_FROM_FREEZE.csv")
            _copy_if_exists(report_dir / "headline_revision_results.csv", freeze_dir / "HEADLINE_REVISION_WINNERS_FROM_FREEZE.csv")
            _copy_if_exists(report_dir / "convergence_diagnostics.csv", freeze_dir / f"STATE_SPACE_CONVERGENCE_MAIN_MAX_ITER{main_iter}.csv")
            _copy_if_exists(variance_dir / "variance_point_audit.csv", freeze_dir / f"STATE_SPACE_VARIANCE_POINT_MAIN_MAX_ITER{main_iter}.csv")
            _copy_if_exists(variance_dir / "variance_revision_audit.csv", freeze_dir / f"STATE_SPACE_VARIANCE_REVISION_MAIN_MAX_ITER{main_iter}.csv")
            _copy_if_exists(variance_dir / "covariance_matrix_audit.csv", freeze_dir / f"STATE_SPACE_COVARIANCE_SUMMARY_MAIN_MAX_ITER{main_iter}.csv")

    mature_rows: list[pd.DataFrame] = []
    if isinstance(mature_runs, dict):
        for variant, paths in mature_runs.items():
            if not isinstance(paths, dict):
                continue
            report_dir = repo_root / str(paths.get("report_dir", ""))
            for filename, table in [
                ("headline_point_results.csv", "point"),
                ("headline_revision_results.csv", "revision"),
            ]:
                frame = _safe_read_csv(report_dir / filename)
                if frame.empty:
                    continue
                frame.insert(0, "table", table)
                frame.insert(0, "mature_variant", str(variant))
                mature_rows.append(frame)
    if mature_rows:
        pd.concat(mature_rows, ignore_index=True).to_csv(freeze_dir / "MATURE_ROBUSTNESS_WINNERS_FROM_FREEZE.csv", index=False)

    file_rows = []
    for path in sorted(freeze_dir.rglob("*")):
        if path.is_file():
            file_rows.append(
                {
                    "relative_path": str(path.relative_to(freeze_dir)),
                    "size_bytes": int(path.stat().st_size),
                }
            )
    pd.DataFrame(file_rows).to_csv(freeze_dir / "EVIDENCE_PACKAGE_FILE_AUDIT.csv", index=False)

    lines = [
        "# Q1 Manuscript Freeze Brief",
        "",
        f"Generated UTC: `{datetime.now(timezone.utc).isoformat(timespec='seconds')}`",
        "",
        "## Interpretation",
        "",
        "- Treat this freeze as the source of manuscript tables only after checking `FREEZE_FAILURE_AUDIT.csv`.",
        "- The Q1 narrative should compare S/T results against no-revision first, then use density, revision diagnostics, mature robustness, and mechanism evidence for state-space value.",
        "- SPF is included only if `MANIFEST.json` points to a built or supplied public SPF benchmark file.",
        "",
        "## Key Files",
        "",
        "- `MANIFEST.json`: run configuration, git metadata, copied artifact map.",
        "- `HEADLINE_POINT_WINNERS_FROM_FREEZE.csv` and `HEADLINE_REVISION_WINNERS_FROM_FREEZE.csv`: summary only, not the sole evidence.",
        "- `runs/*/evidence_dir/`: DM/CW/MCS/bootstrap/density/revision/mechanism tables.",
        "- `FREEZE_FAILURE_AUDIT.csv`: run-level failure counts.",
        "",
    ]
    (freeze_dir / "MANUSCRIPT_RESULTS_BRIEF.md").write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run and freeze a journal-candidate full-state evidence package.")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--max-iters", nargs="+", type=int, default=[50, 100])
    parser.add_argument("--max-origins", type=int, default=0, help="Use 0 for the full 2005Q1-2024Q4 sample.")
    parser.add_argument("--n-factors", type=int, default=1)
    parser.add_argument("--midas-lags", type=int, default=6)
    parser.add_argument("--estimation-window", choices=["expanding", "rolling"], default="expanding")
    parser.add_argument("--rolling-window-quarters", type=int, default=40)
    parser.add_argument("--exclude-quarters", nargs="*", default=[])
    parser.add_argument("--parallel-jobs", type=int, default=1, help="Parallel forecast-origin chunks for each backtest run.")
    parser.add_argument(
        "--spf-forecasts",
        type=Path,
        default=None,
        help="Optional CSV with forecast_origin_date,target_quarter,target_id,forecast_value columns.",
    )
    parser.add_argument("--build-public-spf", action="store_true", help="Download and normalize public Philadelphia Fed SPF RGDP growth benchmark.")
    parser.add_argument("--public-spf-output", type=Path, default=Path("data/external/spf/spf_rgdp_growth_benchmark.csv"))
    parser.add_argument("--mcs-bootstrap-reps", type=int, default=1000)
    parser.add_argument("--mature-max-iter", type=int, default=50)
    parser.add_argument("--mature-variants", nargs="+", choices=sorted(MATURE_TARGETS), default=["mature_1y", "mature_3y", "mature_latest"])
    parser.add_argument("--freeze-name", default=f"full_state_space_journal_candidate_{datetime.now().strftime('%Y%m%d')}")
    parser.add_argument("--skip-main-runs", action="store_true", help="Run only mature/sensitivity/diagnostic blocks requested by flags.")
    parser.add_argument("--skip-mature-robustness", action="store_true")
    parser.add_argument("--run-initialization-audit", action="store_true")
    parser.add_argument("--initialization-seeds", nargs="+", type=int, default=[1, 2, 3, 4, 5])
    parser.add_argument("--initialization-max-iter", type=int, default=50)
    parser.add_argument("--initialization-max-origins", type=int, default=12)
    parser.add_argument("--run-q1-sensitivity", action="store_true")
    parser.add_argument("--sensitivity-max-iter", type=int, default=None)
    parser.add_argument("--sensitivity-mcs-bootstrap-reps", type=int, default=None)
    parser.add_argument("--factor-grid", nargs="*", type=int, default=[1, 2, 3])
    parser.add_argument("--midas-lag-grid", nargs="*", type=int, default=[4, 6, 9])
    parser.add_argument("--window-modes", nargs="*", choices=["expanding", "rolling"], default=["expanding", "rolling"])
    parser.add_argument("--exclude-covid-sensitivity", action="store_true")
    parser.add_argument("--manifest-only", action="store_true", help="Do not copy generated output directories into the frozen folder.")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    spf_forecasts = args.spf_forecasts
    if args.build_public_spf:
        if not args.dry_run:
            build_public_spf_rgdp_growth_csv(args.public_spf_output)
        spf_forecasts = args.public_spf_output
    manifest: dict[str, object] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "repo_root": str(repo_root),
        "git": _git_metadata(repo_root),
        "max_iters": args.max_iters,
        "max_origins": args.max_origins,
        "n_factors": args.n_factors,
        "midas_lags": args.midas_lags,
        "estimation_window": args.estimation_window,
        "rolling_window_quarters": args.rolling_window_quarters,
        "exclude_quarters": args.exclude_quarters,
        "parallel_jobs": args.parallel_jobs,
        "spf_forecasts": str(spf_forecasts) if spf_forecasts is not None else None,
        "build_public_spf": bool(args.build_public_spf),
        "mcs_bootstrap_reps": args.mcs_bootstrap_reps,
        "runs": {},
    }
    _run([sys.executable, "scripts/10_build_gdp_release_calendar_from_alfred.py"], repo_root, args.dry_run)
    _run([sys.executable, "scripts/11_build_mature_target_robustness_panels.py"], repo_root, args.dry_run)
    if not args.skip_main_runs:
        for max_iter in args.max_iters:
            run_name = f"exact_pseudo_backtest_max_iter{max_iter}"
            manifest["runs"][run_name] = _build_run(
                repo_root,
                run_name=run_name,
                max_iter=max_iter,
                max_origins=args.max_origins,
                n_factors=args.n_factors,
                midas_lags=args.midas_lags,
                spf_forecasts=spf_forecasts,
                mcs_bootstrap_reps=args.mcs_bootstrap_reps,
                gdp_release_targets=None,
                estimation_window=args.estimation_window,
                rolling_window_quarters=args.rolling_window_quarters,
                exclude_quarters=tuple(args.exclude_quarters),
                parallel_jobs=max(int(args.parallel_jobs), 1),
                dry_run=args.dry_run,
            )
    if not args.skip_mature_robustness:
        mature_runs: dict[str, object] = {}
        for variant in args.mature_variants:
            run_name = f"exact_pseudo_backtest_{variant}_max_iter{args.mature_max_iter}"
            mature_runs[variant] = _build_run(
                repo_root,
                run_name=run_name,
                max_iter=args.mature_max_iter,
                max_origins=args.max_origins,
                n_factors=args.n_factors,
                midas_lags=args.midas_lags,
                spf_forecasts=spf_forecasts,
                mcs_bootstrap_reps=args.mcs_bootstrap_reps,
                gdp_release_targets=MATURE_TARGETS[variant],
                estimation_window=args.estimation_window,
                rolling_window_quarters=args.rolling_window_quarters,
                exclude_quarters=tuple(args.exclude_quarters),
                parallel_jobs=max(int(args.parallel_jobs), 1),
                dry_run=args.dry_run,
            )
        manifest["mature_robustness_runs"] = mature_runs
    if args.run_q1_sensitivity:
        sensitivity_iter = args.sensitivity_max_iter or max(args.max_iters)
        specs: dict[str, dict[str, object]] = {}

        def add_spec(
            name: str,
            *,
            n_factors: int = args.n_factors,
            midas_lags: int = args.midas_lags,
            estimation_window: str = args.estimation_window,
            exclude_quarters: tuple[str, ...] = tuple(args.exclude_quarters),
        ) -> None:
            specs[name] = {
                "n_factors": n_factors,
                "midas_lags": midas_lags,
                "estimation_window": estimation_window,
                "exclude_quarters": exclude_quarters,
            }

        for k in args.factor_grid:
            add_spec(f"sensitivity_k{k}_max_iter{sensitivity_iter}", n_factors=k)
        for lag in args.midas_lag_grid:
            add_spec(f"sensitivity_midas_lags{lag}_max_iter{sensitivity_iter}", midas_lags=lag)
        for window_mode in args.window_modes:
            add_spec(f"sensitivity_window_{window_mode}_max_iter{sensitivity_iter}", estimation_window=window_mode)
        if args.exclude_covid_sensitivity:
            add_spec(
                f"sensitivity_exclude_covid_max_iter{sensitivity_iter}",
                exclude_quarters=tuple([*args.exclude_quarters, "2020:Q2", "2020:Q3"]),
            )

        baseline_spec = {
            "n_factors": args.n_factors,
            "midas_lags": args.midas_lags,
            "estimation_window": args.estimation_window,
            "exclude_quarters": tuple(args.exclude_quarters),
        }
        sensitivity_runs: dict[str, object] = {}
        for run_name, spec in specs.items():
            if spec == baseline_spec:
                continue
            sensitivity_runs[run_name] = _build_run(
                repo_root,
                run_name=run_name,
                max_iter=sensitivity_iter,
                max_origins=args.max_origins,
                n_factors=int(spec["n_factors"]),
                midas_lags=int(spec["midas_lags"]),
                spf_forecasts=spf_forecasts,
                mcs_bootstrap_reps=args.sensitivity_mcs_bootstrap_reps or args.mcs_bootstrap_reps,
                gdp_release_targets=None,
                estimation_window=str(spec["estimation_window"]),
                rolling_window_quarters=args.rolling_window_quarters,
                exclude_quarters=tuple(spec["exclude_quarters"]),
                parallel_jobs=max(int(args.parallel_jobs), 1),
                dry_run=args.dry_run,
            )
        manifest["sensitivity_runs"] = sensitivity_runs
    convergence_run_names = [str(name) for name in manifest["runs"].keys()]
    sensitivity_entries = manifest.get("sensitivity_runs", {})
    if not convergence_run_names and isinstance(sensitivity_entries, dict):
        convergence_run_names = [str(name) for name in sensitivity_entries.keys()]
    if convergence_run_names:
        _run(
            [
                sys.executable,
                "-m",
                "full_state_space_release_revision_dfm.build_convergence_stability_table",
                "--output-root",
                str(OUTPUT_ROOT),
                "--output-dir",
                str(OUTPUT_ROOT / "convergence_stability_journal_candidate"),
                "--run-names",
                *convergence_run_names,
            ],
            repo_root,
            args.dry_run,
        )
        manifest["convergence_stability"] = str(OUTPUT_ROOT / "convergence_stability_journal_candidate")
    if args.run_initialization_audit:
        _run(
            [
                sys.executable,
                "-m",
                "full_state_space_release_revision_dfm.run_initialization_audit",
                "--output-root",
                str(OUTPUT_ROOT / "initialization_audit_journal_candidate"),
                "--seeds",
                *map(str, args.initialization_seeds),
                "--max-iter",
                str(args.initialization_max_iter),
                "--max-origins",
                str(args.initialization_max_origins),
                "--parallel-jobs",
                str(max(int(args.parallel_jobs), 1)),
            ],
            repo_root,
            args.dry_run,
        )
        manifest["initialization_audit"] = str(OUTPUT_ROOT / "initialization_audit_journal_candidate")
    freeze_dir = OUTPUT_ROOT / "frozen" / args.freeze_name
    if not args.dry_run:
        freeze_dir.mkdir(parents=True, exist_ok=True)
        if not args.manifest_only:
            copied: dict[str, str] = {}
            for run_group in ["runs", "mature_robustness_runs", "sensitivity_runs"]:
                entries = manifest.get(run_group, {})
                if isinstance(entries, dict):
                    for run_name, paths in entries.items():
                        if isinstance(paths, dict):
                            for path_name in ["run_dir", "report_dir", "evidence_dir", "variance_dir"]:
                                path_value = paths.get(path_name)
                                if not path_value:
                                    continue
                                src = repo_root / str(path_value)
                                if src.exists():
                                    dst = freeze_dir / run_group / str(run_name) / path_name
                                    _copytree(src, dst, args.dry_run)
                                    copied[f"{run_group}/{run_name}/{path_name}"] = str(dst)
            for key in ["convergence_stability", "initialization_audit"]:
                path_value = manifest.get(key)
                if path_value:
                    src = repo_root / str(path_value)
                    if src.exists():
                        dst = freeze_dir / key
                        _copytree(src, dst, args.dry_run)
                        copied[key] = str(dst)
            manifest["copied_freeze_artifacts"] = copied
        (freeze_dir / "MANIFEST.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        readme = [
            "# Full-State Journal Candidate Freeze",
            "",
            f"Generated UTC: `{manifest['generated_utc']}`",
            "",
            "This folder records the run manifest for the journal-candidate evidence package.",
            "The generated output directories are listed in `MANIFEST.json`.",
            "",
            "Use this freeze only after verifying that every referenced output directory exists and passes the variance/convergence audits.",
            "",
        ]
        (freeze_dir / "README.md").write_text("\n".join(readme), encoding="utf-8")
        _write_freeze_audits(repo_root, freeze_dir, manifest)
        (freeze_dir / "MANIFEST.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Journal candidate manifest: {(freeze_dir / 'MANIFEST.json').resolve()}")


if __name__ == "__main__":
    main()
