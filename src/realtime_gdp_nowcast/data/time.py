from __future__ import annotations

import re
from dataclasses import dataclass

import pandas as pd
from pandas.tseries.offsets import BDay


QUARTER_PATTERN = re.compile(r"^(?P<year>\d{4})(?::)?Q(?P<quarter>[1-4])$")
RTDSM_VINTAGE_PATTERN = re.compile(r"^[A-Z]+(?P<year>\d{2})Q(?P<quarter>[1-4])$")
ALFRED_VINTAGE_PATTERN = re.compile(r"^[A-Z0-9]+_(?P<vintage>\d{8})$")


@dataclass(frozen=True, slots=True)
class QuarterWindow:
    quarter: pd.Period
    first_month: pd.Period
    second_month: pd.Period
    third_month: pd.Period


def quarter_label_to_period(label: str) -> pd.Period:
    match = QUARTER_PATTERN.match(label)
    if not match:
        raise ValueError(f"Invalid quarter label: {label}")
    return pd.Period(f"{match.group('year')}Q{match.group('quarter')}", freq="Q-DEC")


def period_to_quarter_label(period: pd.Period) -> str:
    period = period.asfreq("Q-DEC")
    return f"{period.year}Q{period.quarter}"


def shift_quarter(label_or_period: str | pd.Period, steps: int) -> pd.Period:
    period = quarter_label_to_period(label_or_period) if isinstance(label_or_period, str) else label_or_period
    return period + steps


def quarter_range(start: str, end: str) -> list[pd.Period]:
    start_period = quarter_label_to_period(start)
    end_period = quarter_label_to_period(end)
    return list(pd.period_range(start_period, end_period, freq="Q-DEC"))


def quarter_window(period: pd.Period) -> QuarterWindow:
    quarter = period.asfreq("Q-DEC")
    third_month = quarter.asfreq("M", how="end")
    first_month = third_month - 2
    second_month = third_month - 1
    return QuarterWindow(
        quarter=quarter,
        first_month=first_month,
        second_month=second_month,
        third_month=third_month,
    )


def month_end(period: pd.Period) -> pd.Timestamp:
    return period.to_timestamp(how="end").normalize()


def last_business_day(period: pd.Period) -> pd.Timestamp:
    return pd.date_range(end=month_end(period), periods=1, freq="B")[0].normalize()


def previous_business_day(timestamp: pd.Timestamp) -> pd.Timestamp:
    return (pd.Timestamp(timestamp).normalize() - BDay(1)).normalize()


def combine_date_time(date_value: pd.Timestamp | str, time_text: str, timezone: str) -> pd.Timestamp:
    ts = pd.Timestamp(f"{pd.Timestamp(date_value).date()} {time_text}")
    if ts.tzinfo is not None:
        return ts.tz_convert(timezone)
    return ts.tz_localize(timezone)


def end_of_day(date_value: pd.Timestamp | str, timezone: str) -> pd.Timestamp:
    return combine_date_time(date_value, "23:59", timezone)


def month_to_quarter(month_period: pd.Period) -> pd.Period:
    return month_period.asfreq("Q-DEC")


def parse_rtdsm_vintage_column(column_name: str) -> pd.Period | None:
    match = RTDSM_VINTAGE_PATTERN.match(column_name)
    if not match:
        return None
    year = int(match.group("year"))
    year += 1900 if year >= 65 else 2000
    quarter = int(match.group("quarter"))
    return pd.Period(f"{year}Q{quarter}", freq="Q-DEC")


def parse_alfred_vintage_column(column_name: str) -> pd.Timestamp | None:
    match = ALFRED_VINTAGE_PATTERN.match(column_name)
    if not match:
        return None
    return pd.Timestamp(match.group("vintage"))


def parse_quarter_from_string(value: str) -> pd.Period:
    cleaned = str(value).strip()
    return quarter_label_to_period(cleaned)


def infer_gdp_reference_quarter(release_date: pd.Timestamp) -> pd.Period:
    month = release_date.month
    year = release_date.year
    mapping = {
        1: (year - 1, 4, "advance"),
        2: (year - 1, 4, "second"),
        3: (year - 1, 4, "third"),
        4: (year, 1, "advance"),
        5: (year, 1, "second"),
        6: (year, 1, "third"),
        7: (year, 2, "advance"),
        8: (year, 2, "second"),
        9: (year, 2, "third"),
        10: (year, 3, "advance"),
        11: (year, 3, "second"),
        12: (year, 3, "third"),
    }
    ref_year, ref_quarter, _ = mapping[month]
    return pd.Period(f"{ref_year}Q{ref_quarter}", freq="Q-DEC")


def infer_gdp_release_round(release_date: pd.Timestamp) -> str:
    month = release_date.month
    mapping = {
        1: "advance",
        2: "second",
        3: "third",
        4: "advance",
        5: "second",
        6: "third",
        7: "advance",
        8: "second",
        9: "third",
        10: "advance",
        11: "second",
        12: "third",
    }
    return mapping[month]
