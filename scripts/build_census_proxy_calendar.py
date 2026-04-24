import json
import re
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ALFRED_SERIES_DIR = PROJECT_ROOT / "data" / "raw" / "alfred" / "series_observations"
CENSUS_CALENDAR_DIR = PROJECT_ROOT / "data" / "raw" / "calendars" / "census"

SOURCE = "ALFRED"
PROXY_METHOD = "alfred_first_observed_vintage"
SERIES_NOTES = (
    "Series-level first-release proxy inferred from the earliest non-missing ALFRED vintage for each observation."
)
BLOCK_NOTES = (
    "Block-level first-release proxy calendar derived from series-level ALFRED first vintages; not an official Census release calendar."
)

RELEASE_BLOCKS = {
    "retail_sales": ["RSAFS", "RSXFS"],
    "housing": ["HOUST", "PERMIT"],
    "durable_goods": ["DGORDER", "NEWORDER"],
    "inventories": ["BUSINV", "ISRATIO"],
    "trade": ["BOPGSTB", "BOPTEXP", "BOPTIMP"],
}

SERIES_TO_BLOCK = {
    series_id: release_block
    for release_block, series_ids in RELEASE_BLOCKS.items()
    for series_id in series_ids
}

SERIES_OUTPUT_PATH = CENSUS_CALENDAR_DIR / "census_proxy_release_events.csv"
BLOCK_OUTPUT_PATH = CENSUS_CALENDAR_DIR / "census_proxy_release_calendar.csv"
METADATA_OUTPUT_PATH = CENSUS_CALENDAR_DIR / "census_proxy_calendar_metadata.json"


def _parse_vintage_columns(series_id: str, columns: list[str]) -> list[tuple[pd.Timestamp, str]]:
    pattern = re.compile(rf"^{re.escape(series_id)}_(\d{{8}})$")
    vintage_columns: list[tuple[pd.Timestamp, str]] = []
    for column in columns[1:]:
        match = pattern.match(column)
        if not match:
            continue
        vintage_columns.append((pd.Timestamp(match.group(1)), column))
    return sorted(vintage_columns)


def infer_first_release_rows(series_id: str, csv_path: Path) -> pd.DataFrame:
    wide = pd.read_csv(csv_path, na_values=["."])
    vintage_columns = _parse_vintage_columns(series_id, wide.columns.tolist())
    if not vintage_columns:
        raise ValueError(f"Could not infer ALFRED vintage columns for {series_id}.")

    rows: list[dict[str, object]] = []
    for record in wide.itertuples(index=False):
        observation_date = pd.Timestamp(record.date)
        for vintage_date, column in vintage_columns:
            value = getattr(record, column)
            if pd.notna(value):
                rows.append(
                    {
                        "series_id": series_id,
                        "release_block": SERIES_TO_BLOCK[series_id],
                        "observation_date": observation_date.normalize(),
                        "reference_period": observation_date.to_period("M").strftime("%Y-%m"),
                        "release_date": vintage_date.normalize(),
                        "release_time_et": "08:30",
                        "proxy_method": PROXY_METHOD,
                        "provenance_file": csv_path.relative_to(PROJECT_ROOT).as_posix(),
                        "notes": SERIES_NOTES,
                    }
                )
                break

    events = pd.DataFrame(rows)
    if events.empty:
        raise ValueError(f"No first-release proxy rows were inferred for {series_id}.")
    return events.drop_duplicates(subset=["series_id", "observation_date", "release_date"]).sort_values(
        ["release_date", "series_id", "observation_date"]
    )


def build_series_events() -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for series_id in sorted(SERIES_TO_BLOCK):
        csv_path = ALFRED_SERIES_DIR / f"{series_id}.csv"
        if not csv_path.exists():
            raise FileNotFoundError(f"Missing ALFRED observations file: {csv_path}")
        frames.append(infer_first_release_rows(series_id, csv_path))
    events = pd.concat(frames, ignore_index=True)
    events.insert(0, "source", SOURCE)
    return events.sort_values(["release_date", "release_block", "series_id", "observation_date"]).reset_index(drop=True)


def build_block_calendar(events: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        events.groupby(["release_block", "release_date"], as_index=False)
        .agg(
            included_series=("series_id", lambda values: ";".join(sorted(set(values)))),
            reference_periods=("reference_period", lambda values: ";".join(sorted(set(values)))),
        )
        .sort_values(["release_date", "release_block"], kind="stable")
        .reset_index(drop=True)
    )
    grouped["source"] = SOURCE
    grouped["release_time_et"] = "08:30"
    grouped["proxy_method"] = PROXY_METHOD
    grouped["notes"] = BLOCK_NOTES
    return grouped[
        [
            "source",
            "release_block",
            "release_date",
            "release_time_et",
            "included_series",
            "reference_periods",
            "proxy_method",
            "notes",
        ]
    ]


def build_metadata() -> dict[str, object]:
    return {
        "title": "Census proxy first-release calendar",
        "status": "proxy_not_official",
        "source": SOURCE,
        "proxy_method": PROXY_METHOD,
        "summary": (
            "Series-level first-release proxy calendar for Census-related indicators derived from the earliest "
            "non-missing ALFRED vintage for each observation."
        ),
        "important_notes": [
            "This is NOT an official Census release calendar.",
            "It targets first-release timing rather than the union of all availability dates.",
            "It is designed to separate first releases from later revisions when the live Census calendar is unavailable.",
            "Intraday timing is set to 08:30 ET as a transparent source-default assumption.",
        ],
        "release_blocks": RELEASE_BLOCKS,
        "input_pattern": "data/raw/alfred/series_observations/{SERIES_ID}.csv",
        "artifacts": {
            "series_level_events": SERIES_OUTPUT_PATH.relative_to(PROJECT_ROOT).as_posix(),
            "block_level_calendar": BLOCK_OUTPUT_PATH.relative_to(PROJECT_ROOT).as_posix(),
        },
    }


def write_outputs(events: pd.DataFrame, calendar: pd.DataFrame) -> None:
    CENSUS_CALENDAR_DIR.mkdir(parents=True, exist_ok=True)
    events.to_csv(SERIES_OUTPUT_PATH, index=False)
    calendar.to_csv(BLOCK_OUTPUT_PATH, index=False)
    with METADATA_OUTPUT_PATH.open("w", encoding="utf-8") as file_obj:
        json.dump(build_metadata(), file_obj, ensure_ascii=False, indent=2)


def main() -> None:
    events = build_series_events()
    calendar = build_block_calendar(events)
    write_outputs(events, calendar)
    print(f"[OK] Wrote {len(events)} series-level proxy events -> {SERIES_OUTPUT_PATH}")
    print(f"[OK] Wrote {len(calendar)} block-level proxy rows -> {BLOCK_OUTPUT_PATH}")
    print(f"[OK] Wrote metadata -> {METADATA_OUTPUT_PATH}")


if __name__ == "__main__":
    main()
