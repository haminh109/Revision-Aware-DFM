# Data Registry

## Core sources

- `RTDSM`: GDP release targets and mature-vintage construction
- `ALFRED`: monthly vintage histories and release dates
- `BEA/BLS/Census/Federal Reserve`: release-time defaults and agency interpretation
- `silver` layer in this repo: machine-readable mapping from indicators to release blocks and timing support status

## v1 indicator panel

| Block | Series IDs |
| --- | --- |
| Labor and aggregate activity | `PAYEMS`, `UNRATE`, `AWHMAN`, `INDPRO`, `TCU` |
| Consumption and income | `W875RX1`, `RSXFS`, `UMCSENT` |
| Investment and housing | `HOUST`, `PERMIT`, `DGORDER`, `NEWORDER` |
| Inventories and trade | `BUSINV`, `BOPGSTB` |
| Financial and survey variables | `T10Y3MM`, `FEDFUNDS`, `GS10` |

## Exact-timing policy

- Official/proxy timing support comes first from `data/silver/indicators/indicator_release_map.csv` and `data/silver/calendars/release_calendar_silver.csv`.
- Historical GDP release dates are inferred from `GDPC1` ALFRED vintage starts to recover first, second, and third release dates quarter by quarter.
- For `currently_unmapped` series such as `UMCSENT`, `T10Y3MM`, `FEDFUNDS`, and `GS10`, the downstream pipeline uses `realtime_start` as a conservative availability-date proxy and logs the assumption in `research_log.md`.

## File conventions

- Raw ALFRED downloads: `data/raw/alfred/<series_id>/`
- Raw RTDSM downloads: `data/raw/rtdsm/<series_slug>/`
- Processed panels: `data/processed/*.parquet`
- Tables: `outputs/tables/*.csv`
- Figures: `outputs/figures/*.png`

## Logging rules

- Any series substitution must be logged here with date, reason, and replacement.
- Any manual release-time override must be logged here with source and rationale.
- Any use of `realtime_start` as a timing proxy for currently unmapped series must be logged here and in `research_log.md`.
