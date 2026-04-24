from __future__ import annotations

import logging
import subprocess
import sys
from pathlib import Path

from realtime_gdp_nowcast.config import ProjectSettings

LOGGER = logging.getLogger(__name__)

REQUIRED_INPUTS = [
    "data/raw/alfred/series_observations/GDPC1.csv",
    "data/bronze/indicators/alfred_monthly_long.csv",
    "data/silver/calendars/release_calendar_silver.csv",
    "data/silver/targets/gdp_release_stage_silver.csv",
    "data/silver/targets/gdp_complete_vintages_silver.csv",
]

VALIDATION_SCRIPTS = [
    "scripts/validate_stage0.py",
    "scripts/validate_stage1.py",
    "scripts/validate_stage2.py",
]


def _check_required_inputs(root: Path) -> None:
    missing = [relative for relative in REQUIRED_INPUTS if not (root / relative).exists()]
    if missing:
        missing_text = "\n".join(f"- {path}" for path in missing)
        raise FileNotFoundError(f"Missing required repo inputs:\n{missing_text}")


def _run_validation_script(root: Path, script_relative_path: str) -> None:
    script_path = root / script_relative_path
    LOGGER.info("Running %s", script_relative_path)
    completed = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"{script_relative_path} failed with code {completed.returncode}\n"
            f"STDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}"
        )
    if completed.stdout.strip():
        LOGGER.info("%s", completed.stdout.strip())


def run_download_data(settings: ProjectSettings) -> None:
    root = settings.paths.root
    _check_required_inputs(root)

    if not settings.download.get("validate_existing_raw_only", False):
        LOGGER.warning(
            "This repo is configured to work from existing raw/bronze/silver inputs. "
            "Fresh download logic is intentionally disabled in the research pipeline."
        )

    for script in VALIDATION_SCRIPTS:
        _run_validation_script(root, script)
