import pandas as pd

from realtime_gdp_nowcast.data.calendars import _infer_first_release_candidates


def test_infer_first_release_candidates_keeps_earliest_vintage_per_observation() -> None:
    frame = pd.DataFrame(
        {
            "series_id": ["RSXFS", "RSXFS", "RSXFS", "BUSINV"],
            "observation_date": pd.to_datetime(["2024-01-01", "2024-01-01", "2024-02-01", "2024-01-01"]),
            "realtime_start": pd.to_datetime(["2024-02-14", "2024-03-14", "2024-03-14", "2024-03-15"]),
        }
    )

    inferred = _infer_first_release_candidates(frame)

    assert len(inferred) == 3
    jan_rsxfs = inferred[
        (inferred["series_id"] == "RSXFS") & (inferred["observation_date"] == pd.Timestamp("2024-01-01"))
    ]
    assert pd.Timestamp(jan_rsxfs["realtime_start"].iloc[0]) == pd.Timestamp("2024-02-14")
