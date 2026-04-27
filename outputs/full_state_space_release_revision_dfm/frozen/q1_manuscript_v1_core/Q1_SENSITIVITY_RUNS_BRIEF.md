# Q1 Sensitivity Runs Brief

Audit date: 2026-04-27

No active Python process was found for the journal pipeline, exact/pseudo backtest,
initialization audit, or journal evidence package after the sensitivity runs.

## Accepted Core Freeze

- Freeze: `q1_manuscript_v1_core`
- Failure audit: all main and mature robustness runs have `failure_rows = 0`.
- Headline run: `exact_pseudo_backtest_max_iter100`.
- Headline status: accepted for manuscript tables and narrative.

## Accepted Sensitivity Freezes

| Freeze | Coverage | Failure audit |
| --- | --- | --- |
| `q1_manuscript_v1_sensitivity_k` | Factor-count checks for `K=2` and `K=3`; baseline factor setting is in the core freeze. | All rows have `failure_rows = 0`. |
| `q1_manuscript_v1_sensitivity_midas` | MIDAS lag checks for lags `4` and `9`; lag `6` is in the core freeze. | All rows have `failure_rows = 0`. |
| `q1_manuscript_v1_sensitivity_rolling` | Rolling 10-year window check. | All rows have `failure_rows = 0`. |
| `q1_manuscript_v1_sensitivity_exclude_covid` | Excludes 2020Q2 and 2020Q3. | All rows have `failure_rows = 0`. |

## Manuscript Use

Use `q1_manuscript_v1_core` as the only source for headline Q1 manuscript
numbers. Use the four sensitivity freezes only for robustness and appendix
tables. The core narrative should keep the no-revision benchmark as a central
empirical finding and use the state-space evidence for uncertainty, release
mechanism, revision-risk, mature-target robustness, and estimator stability.
