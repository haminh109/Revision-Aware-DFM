# Research Log

## 2026-04-24

- Validated `Stage 0`, `Stage 1`, and `Stage 2` in the imported repo; all three returned `PASS`.
- Chose the imported repo as the canonical workspace because it already contains raw, bronze, and silver artifacts plus semantic validation reports.
- Locked the downstream pipeline to build on top of bronze/silver, not to rebuild the existing data foundation from scratch.
- Kept `ROUTPUT` from `RTDSM` as the GDP target backbone and `GDPC1` as the historical GDP release-date proxy.
- Chose a conservative timing policy for currently unmapped financial/survey series: use `realtime_start` as a proxy only in the new processed layer, never overwrite Stage 2 semantics.
- Replaced the old Census proxy design based on the union of availability dates with a stronger `first-release proxy` built from the earliest non-missing ALFRED vintage per observation for `retail_sales`, `housing`, `durable_goods`, `inventories`, and `trade`.
- Updated checkpoint construction so exact schedules prefer mapped first-release proxy events over generic fallback vintage-day revisions whenever Census official calendar pages are unavailable.

## Open research issues

- Verify whether `RSXFS` should remain the preferred real retail-sales proxy in the v1 exact-timing panel or whether `RSAFS` should also be included in robustness.
- Decide in the paper draft whether `UMCSENT` should remain a proxy-timed indicator or move to appendix-only robustness if its timing support is judged too weak.
- Review whether benchmark and annual-revision GDP vintages should be excluded from the historical GDP release calendar inferred from `GDPC1`.
