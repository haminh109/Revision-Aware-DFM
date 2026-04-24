The repository no longer depends on the live Census economic indicators calendar for Stage 0
usability.

Why:

1. `https://www.census.gov/economic-indicators/calendar-listview.html` is unreliable for automated
   acquisition because Cloudflare may block access.
2. The repository already uses ALFRED / FRED as the canonical source for the Census-related
   indicator values.
3. The missing component was release-day timing metadata, not the indicator values themselves.

Replacement design:

1. Census indicator values remain unchanged and continue to come from ALFRED / FRED.
2. Census release timing is represented by a `first-release proxy calendar` derived from the
   earliest non-missing ALFRED vintage for each observation of the Census-related series already
   used in the repo.
3. This is materially stronger than taking the union of all ALFRED availability dates because it
   separates first releases from later revisions.
4. Intraday timing is set to a transparent `08:30 ET` source-default assumption for the proxy
   events.

Proxy artifacts:

- `data/raw/calendars/census/census_proxy_release_events.csv`
- `data/raw/calendars/census/census_proxy_release_calendar.csv`
- `data/raw/calendars/census/census_proxy_calendar_metadata.json`
- `data/interim/census_first_release_proxy_calendar.csv`

Build command:

```bash
python scripts/build_census_proxy_calendar.py
```

Optional official HTML:

- `data/raw/calendars/census/economic_indicators_calendar.html` can still be stored when available.
- `CENSUS_CALENDAR_MANUAL_HTML` can point to a browser-saved HTML export if you want to keep that
  raw file for reference.
- If the live Census page is blocked, Stage 0 should continue with the proxy calendar artifacts.
