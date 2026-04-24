from __future__ import annotations

import logging

import numpy as np
import pandas as pd

from realtime_gdp_nowcast.config import ProjectSettings
from realtime_gdp_nowcast.data.catalogs import required_series
from realtime_gdp_nowcast.data.time import (
    end_of_day,
    last_business_day,
    previous_business_day,
    quarter_label_to_period,
    quarter_range,
    quarter_window,
)
from realtime_gdp_nowcast.features.transforms import apply_transform, expanding_standardize
from realtime_gdp_nowcast.io import write_table

LOGGER = logging.getLogger(__name__)


def _coerce_checkpoint_timestamp(
    timestamp: pd.Timestamp | None,
    fallback_day: pd.Timestamp,
    timezone: str,
) -> pd.Timestamp:
    if timestamp is not None and pd.notna(timestamp):
        return pd.Timestamp(timestamp)
    return end_of_day(fallback_day, timezone)


def _release_date_in_month(
    event_panel: pd.DataFrame,
    series_ids: list[str],
    observation_month: pd.Period,
    month_period: pd.Period,
) -> pd.Timestamp | None:
    candidates = event_panel[
        event_panel["series_id"].isin(series_ids)
        & (event_panel["observation_month"] == observation_month)
        & (event_panel["release_month"] == month_period)
    ]
    if candidates.empty:
        return None
    return pd.Timestamp(candidates["public_release_timestamp_et"].max())


def _build_exact_schedule(settings: ProjectSettings, release_calendar: pd.DataFrame, event_panel: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    gdp_proxy_id = settings.project["gdp_release_proxy_series_id"]
    backtest_quarters = quarter_range(settings.sample["burn_in_start_quarter"], settings.sample["backtest_end_quarter"])
    gdp_calendar = release_calendar[release_calendar["series_id"] == gdp_proxy_id].copy()

    for quarter in backtest_quarters:
        label = f"{quarter.year}Q{quarter.quarter}"
        window = quarter_window(quarter)
        gdp_rows = gdp_calendar[gdp_calendar["reference_period"] == label]
        gdp_release_map = {
            round_name: end_of_day(previous_business_day(release_date), settings.project["timezone"])
            for round_name, release_date in gdp_rows.set_index("release_round")["public_release_date"].to_dict().items()
        }
        m1_end = end_of_day(last_business_day(window.first_month), settings.project["timezone"])
        m2_date = _release_date_in_month(
            event_panel,
            ["PAYEMS", "UNRATE", "AWHMAN"],
            window.first_month,
            window.second_month,
        )
        m3_date = _release_date_in_month(
            event_panel,
            ["W875RX1", "RSXFS", "BOPGSTB", "BUSINV"],
            window.second_month,
            window.third_month,
        )
        checkpoint_map = {
            "m1_end": m1_end,
            "m2_labor": _coerce_checkpoint_timestamp(
                m2_date,
                last_business_day(window.second_month),
                settings.project["timezone"],
            ),
            "m3_spending_trade_inventories": _coerce_checkpoint_timestamp(
                m3_date,
                last_business_day(window.third_month),
                settings.project["timezone"],
            ),
            "pre_advance": gdp_release_map.get(
                "advance",
                end_of_day(previous_business_day((window.third_month + 1).to_timestamp(how="end")), settings.project["timezone"]),
            ),
            "pre_second": gdp_release_map.get(
                "second",
                end_of_day(previous_business_day((window.third_month + 2).to_timestamp(how="end")), settings.project["timezone"]),
            ),
            "pre_third": gdp_release_map.get(
                "third",
                end_of_day(previous_business_day((window.third_month + 3).to_timestamp(how="end")), settings.project["timezone"]),
            ),
        }
        for checkpoint in settings.checkpoints:
            rows.append(
                {
                    "snapshot_mode": "exact",
                    "target_quarter_label": label,
                    "checkpoint_id": checkpoint["checkpoint_id"],
                    "checkpoint_label": checkpoint["label"],
                    "forecast_origin": checkpoint_map[checkpoint["checkpoint_id"]],
                }
            )
    return pd.DataFrame(rows)


def _latest_month_end_at_or_before(forecast_origin: pd.Timestamp, timezone: str) -> pd.Timestamp:
    local_origin = pd.Timestamp(forecast_origin).tz_convert(timezone)
    month_period = local_origin.tz_localize(None).to_period("M")
    month_end_origin = end_of_day(last_business_day(month_period), timezone)
    if month_end_origin > local_origin:
        month_period -= 1
        month_end_origin = end_of_day(last_business_day(month_period), timezone)
    return month_end_origin


def _build_pseudo_schedule(settings: ProjectSettings, exact_schedule: pd.DataFrame) -> pd.DataFrame:
    pseudo_schedule = exact_schedule.copy()
    pseudo_schedule["snapshot_mode"] = "pseudo"
    pseudo_schedule["forecast_origin"] = pseudo_schedule["forecast_origin"].map(
        lambda ts: _latest_month_end_at_or_before(ts, settings.project["timezone"])
    )
    return pseudo_schedule


def _prepare_snapshot_frame(latest: pd.DataFrame) -> pd.DataFrame:
    prepared_frames: list[pd.DataFrame] = []
    for _, group in latest.groupby("series_id"):
        group = group.sort_values("observation_date").copy()
        group["value_transformed"] = apply_transform(group["value_raw"], group["transform_code"].iloc[0])
        group["value_standardized"] = expanding_standardize(group["value_transformed"])
        prepared_frames.append(group)
    return pd.concat(prepared_frames, ignore_index=True) if prepared_frames else latest


def _extract_single_snapshot(
    event_panel: pd.DataFrame,
    release_ns: np.ndarray,
    target_quarter_label: str,
    checkpoint_id: str,
    checkpoint_label: str,
    forecast_origin: pd.Timestamp,
    snapshot_mode: str,
) -> pd.DataFrame:
    target_quarter = quarter_label_to_period(target_quarter_label)
    target_quarter_end = target_quarter.asfreq("M", how="end").to_timestamp(how="end").normalize()
    cutoff = int(np.searchsorted(release_ns, pd.Timestamp(forecast_origin).value, side="right"))
    available = event_panel.iloc[:cutoff]
    available = available[available["observation_date"] <= target_quarter_end]
    if available.empty:
        return available

    latest = available.groupby(["series_id", "observation_date"], as_index=False).tail(1).copy()
    latest = latest.sort_values(["series_id", "observation_date"]).reset_index(drop=True)
    latest = _prepare_snapshot_frame(latest)
    latest["forecast_origin"] = forecast_origin
    latest["checkpoint_id"] = checkpoint_id
    latest["checkpoint_label"] = checkpoint_label
    latest["target_quarter_label"] = target_quarter_label
    latest["snapshot_mode"] = snapshot_mode
    return latest


def build_snapshots(settings: ProjectSettings) -> tuple[pd.DataFrame, pd.DataFrame]:
    event_panel_path = settings.paths.processed_data / "event_panel.parquet"
    release_calendar_path = settings.paths.processed_data / "release_calendar.parquet"
    if not event_panel_path.exists() or not release_calendar_path.exists():
        raise FileNotFoundError("Missing processed inputs. Run `build-event-panel` and `build-calendars` first.")

    event_panel = pd.read_parquet(event_panel_path)
    release_calendar = pd.read_parquet(release_calendar_path)
    series_catalog = required_series(settings)
    event_panel = event_panel[event_panel["series_id"].isin(series_catalog["series_id"])].copy()
    event_panel["observation_month"] = pd.PeriodIndex(event_panel["observation_date"], freq="M")
    event_panel["release_month"] = (
        pd.to_datetime(event_panel["public_release_timestamp_et"])
        .dt.tz_convert(settings.project["timezone"])
        .dt.tz_localize(None)
        .dt.to_period("M")
    )
    event_panel = event_panel.sort_values(
        ["public_release_timestamp_et", "series_id", "observation_date", "vintage_date"]
    ).reset_index(drop=True)
    release_ns = event_panel["public_release_timestamp_et"].astype("int64").to_numpy()

    exact_schedule = _build_exact_schedule(settings, release_calendar, event_panel)
    pseudo_schedule = _build_pseudo_schedule(settings, exact_schedule)
    schedule = pd.concat([exact_schedule, pseudo_schedule], ignore_index=True)
    schedule["forecast_origin_date"] = pd.to_datetime(schedule["forecast_origin"]).dt.tz_convert(
        settings.project["timezone"]
    ).dt.date.astype(str)
    schedule = schedule.sort_values(["snapshot_mode", "target_quarter_label", "forecast_origin"]).reset_index(drop=True)

    snapshots: list[pd.DataFrame] = []
    total_rows = len(schedule)
    for idx, row in enumerate(schedule.itertuples(index=False), start=1):
        if idx == 1 or idx == total_rows or idx % 50 == 0:
            LOGGER.info(
                "Building snapshots | completed=%s/%s mode=%s checkpoint=%s quarter=%s",
                idx,
                total_rows,
                row.snapshot_mode,
                row.checkpoint_id,
                row.target_quarter_label,
            )
        snapshot = _extract_single_snapshot(
            event_panel,
            release_ns,
            row.target_quarter_label,
            row.checkpoint_id,
            row.checkpoint_label,
            row.forecast_origin,
            row.snapshot_mode,
        )
        if not snapshot.empty:
            snapshots.append(snapshot)

    snapshot_panel = pd.concat(snapshots, ignore_index=True) if snapshots else pd.DataFrame()
    write_table(schedule, settings.paths.processed_data / "checkpoint_schedule.parquet")
    write_table(schedule, settings.paths.processed_data / "checkpoint_schedule.csv")
    write_table(snapshot_panel, settings.paths.processed_data / "snapshot_panel.parquet")
    write_table(snapshot_panel, settings.paths.processed_data / "snapshot_panel.csv")
    LOGGER.info("Built snapshot panel with %s rows", len(snapshot_panel))
    return schedule, snapshot_panel
