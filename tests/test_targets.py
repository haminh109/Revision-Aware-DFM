import pandas as pd

from realtime_gdp_nowcast.data.time import parse_quarter_from_string


def test_parse_quarter_from_string_accepts_colon() -> None:
    quarter = parse_quarter_from_string("2024:Q3")
    assert str(quarter) == "2024Q3"


def test_target_revision_arithmetic() -> None:
    frame = pd.DataFrame({"A": [1.0], "S": [2.5], "T": [3.0], "M": [4.0]})
    assert float((frame["S"] - frame["A"]).iloc[0]) == 1.5
    assert float((frame["T"] - frame["S"]).iloc[0]) == 0.5
