from pathlib import Path

from realtime_gdp_nowcast.config import load_settings


def test_load_settings_works() -> None:
    settings = load_settings(root=Path(__file__).resolve().parents[1])
    assert settings.project["gdp_release_proxy_series_id"] == "GDPC1"
    assert settings.paths.series_catalog.exists()
