import pandas as pd

from realtime_gdp_nowcast.data.snapshots import _latest_month_end_at_or_before, _release_date_in_month
from realtime_gdp_nowcast.data.time import period_to_quarter_label, quarter_label_to_period


def test_quarter_label_round_trip() -> None:
    label = "2024Q2"
    period = quarter_label_to_period(label)
    assert period_to_quarter_label(period) == label


def test_pseudo_month_end_never_exceeds_exact_checkpoint() -> None:
    timezone = "America/New_York"
    exact_origin = pd.Timestamp("2024-04-24 23:59:00", tz=timezone)
    pseudo_origin = _latest_month_end_at_or_before(exact_origin, timezone)
    assert pseudo_origin == pd.Timestamp("2024-03-29 23:59:00", tz=timezone)
    assert pseudo_origin <= exact_origin


def test_month_end_is_stable_when_checkpoint_is_already_month_end() -> None:
    timezone = "America/New_York"
    exact_origin = pd.Timestamp("2024-03-29 23:59:00", tz=timezone)
    pseudo_origin = _latest_month_end_at_or_before(exact_origin, timezone)
    assert pseudo_origin == exact_origin


def test_release_date_in_month_prefers_mapped_first_release_over_fallback_revision() -> None:
    frame = pd.DataFrame(
        {
            "series_id": ["RSXFS", "RSXFS"],
            "observation_month": [pd.Period("2024-02", freq="M"), pd.Period("2024-02", freq="M")],
            "release_month": [pd.Period("2024-03", freq="M"), pd.Period("2024-03", freq="M")],
            "public_release_timestamp_et": [
                pd.Timestamp("2024-03-14 08:30:00", tz="America/New_York"),
                pd.Timestamp("2024-03-28 23:59:00", tz="America/New_York"),
            ],
            "source_type": ["proxy_first_release_from_alfred", "alfred_vintage_proxy"],
        }
    )

    release_date = _release_date_in_month(
        frame,
        ["RSXFS"],
        pd.Period("2024-02", freq="M"),
        pd.Period("2024-03", freq="M"),
    )

    assert release_date == pd.Timestamp("2024-03-14 08:30:00", tz="America/New_York")
