from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


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
    mcs_bootstrap_reps: int,
    gdp_release_targets: Path | None,
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
        "--output-dir",
        str(run_dir),
    ]
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
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run and freeze a journal-candidate full-state evidence package.")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--max-iters", nargs="+", type=int, default=[50, 100])
    parser.add_argument("--max-origins", type=int, default=0, help="Use 0 for the full 2005Q1-2024Q4 sample.")
    parser.add_argument("--mcs-bootstrap-reps", type=int, default=1000)
    parser.add_argument("--mature-max-iter", type=int, default=50)
    parser.add_argument("--mature-variants", nargs="+", choices=sorted(MATURE_TARGETS), default=["mature_1y", "mature_3y", "mature_latest"])
    parser.add_argument("--freeze-name", default=f"full_state_space_journal_candidate_{datetime.now().strftime('%Y%m%d')}")
    parser.add_argument("--skip-mature-robustness", action="store_true")
    parser.add_argument("--run-initialization-audit", action="store_true")
    parser.add_argument("--initialization-seeds", nargs="+", type=int, default=[1, 2, 3, 4, 5])
    parser.add_argument("--initialization-max-iter", type=int, default=50)
    parser.add_argument("--initialization-max-origins", type=int, default=12)
    parser.add_argument("--manifest-only", action="store_true", help="Do not copy generated output directories into the frozen folder.")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    manifest: dict[str, object] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "repo_root": str(repo_root),
        "max_iters": args.max_iters,
        "max_origins": args.max_origins,
        "mcs_bootstrap_reps": args.mcs_bootstrap_reps,
        "runs": {},
    }
    _run([sys.executable, "scripts/10_build_gdp_release_calendar_from_alfred.py"], repo_root, args.dry_run)
    _run([sys.executable, "scripts/11_build_mature_target_robustness_panels.py"], repo_root, args.dry_run)
    for max_iter in args.max_iters:
        run_name = f"exact_pseudo_backtest_max_iter{max_iter}"
        manifest["runs"][run_name] = _build_run(
            repo_root,
            run_name=run_name,
            max_iter=max_iter,
            max_origins=args.max_origins,
            mcs_bootstrap_reps=args.mcs_bootstrap_reps,
            gdp_release_targets=None,
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
                mcs_bootstrap_reps=args.mcs_bootstrap_reps,
                gdp_release_targets=MATURE_TARGETS[variant],
                dry_run=args.dry_run,
            )
        manifest["mature_robustness_runs"] = mature_runs
    _run(
        [
            sys.executable,
            "-m",
            "full_state_space_release_revision_dfm.build_convergence_stability_table",
            "--output-root",
            str(OUTPUT_ROOT),
            "--output-dir",
            str(OUTPUT_ROOT / "convergence_stability_journal_candidate"),
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
            for run_group in ["runs", "mature_robustness_runs"]:
                entries = manifest.get(run_group, {})
                if isinstance(entries, dict):
                    for run_name, paths in entries.items():
                        if isinstance(paths, dict):
                            for path_name, path_value in paths.items():
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
    print(f"Journal candidate manifest: {(freeze_dir / 'MANIFEST.json').resolve()}")


if __name__ == "__main__":
    main()
