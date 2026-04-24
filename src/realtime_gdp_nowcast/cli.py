from __future__ import annotations

import argparse
import logging

from realtime_gdp_nowcast.config import load_settings
from realtime_gdp_nowcast.data.calendars import build_release_calendar
from realtime_gdp_nowcast.data.download import run_download_data
from realtime_gdp_nowcast.data.event_panel import build_event_panel
from realtime_gdp_nowcast.data.snapshots import build_snapshots
from realtime_gdp_nowcast.data.targets import build_targets
from realtime_gdp_nowcast.evaluation.run import run as run_evaluation
from realtime_gdp_nowcast.logging_utils import configure_logging
from realtime_gdp_nowcast.models import ar, bridge, release_dfm, revision_dfm, standard_dfm
from realtime_gdp_nowcast.reporting.report import build_report

LOGGER = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Real-time GDP nowcasting research pipeline")
    parser.add_argument("--root", default=".", help="Project root directory")
    parser.add_argument("--config", default=None, help="Optional path to config YAML")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command in [
        "download-data",
        "build-calendars",
        "build-targets",
        "build-event-panel",
        "build-snapshots",
        "run-benchmarks",
        "run-release-dfm",
        "run-revision-dfm",
        "evaluate",
        "build-report",
    ]:
        subparsers.add_parser(command)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    configure_logging(verbose=args.verbose)
    settings = load_settings(root=args.root, config_path=args.config)

    if args.command == "download-data":
        run_download_data(settings)
    elif args.command == "build-calendars":
        build_release_calendar(settings)
    elif args.command == "build-targets":
        build_targets(settings)
    elif args.command == "build-event-panel":
        build_event_panel(settings)
    elif args.command == "build-snapshots":
        build_snapshots(settings)
    elif args.command == "run-benchmarks":
        LOGGER.info("Running AR benchmark")
        ar.run(settings)
        LOGGER.info("Running Bridge benchmark")
        bridge.run(settings)
        LOGGER.info("Running Standard DFM benchmark")
        standard_dfm.run(settings)
    elif args.command == "run-release-dfm":
        release_dfm.run(settings)
    elif args.command == "run-revision-dfm":
        revision_dfm.run(settings)
    elif args.command == "evaluate":
        run_evaluation(settings)
    elif args.command == "build-report":
        build_report(settings)


if __name__ == "__main__":
    main()
