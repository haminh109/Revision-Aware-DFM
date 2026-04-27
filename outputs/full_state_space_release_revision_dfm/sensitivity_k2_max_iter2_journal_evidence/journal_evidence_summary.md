# Journal Evidence Package

Generated UTC: `2026-04-26T11:05:30+00:00`

Source backtest directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/sensitivity_k2_max_iter2`

## What This Adds

- HAC Diebold-Mariano-style forecast comparison tests.
- Clark-West-style adjusted tests for nested or near-nested structured comparisons.
- A model-confidence-set proxy based on squared-error loss differences.
- Block-bootstrap MCS-style confidence sets by timing/checkpoint/target.
- Model-implied state-space density evaluation where forecast variances are available, with leakage-safe residual calibration as fallback.
- Cumulative squared-error difference tables and selected figures.
- Data coverage and calendar audit tables.

## Main Caveat

State-space rows can use model-implied predictive variance from the Kalman measurement block. Non-state-space benchmarks still use leakage-safe expanding residual calibration when enough prior forecast errors exist. The MCS-style table is a transparent block-bootstrap implementation; if a target journal requires an exact Hansen-Lunde-Nason implementation, treat it as an auditable diagnostic layer rather than the final word.

## Selected DM/HAC Rows

| timing_mode | checkpoint_id | outcome_id | baseline_model | model_id | n_obs | mean_loss_diff | test_stat | p_value_model_better_one_sided |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | A | ar | bridge | 4 | 0.0146 |  |  |
| exact | pre_advance | A | ar | indicator_revision_only_dfm_kalman_em | 4 | 0.0640 |  |  |
| exact | pre_advance | A | ar | joint_indicator_revision_dfm_full_kalman_em | 4 | 0.0995 |  |  |
| exact | pre_advance | A | ar | midas_umidas | 4 | -2.5521 |  |  |
| exact | pre_advance | A | ar | monthly_mixed_frequency_kalman_em | 4 | 0.0880 |  |  |
| exact | pre_advance | A | ar | no_revision | 4 | -0.0628 |  |  |
| exact | pre_advance | A | ar | release_dfm | 4 | 0.0282 |  |  |
| exact | pre_advance | A | ar | revision_dfm_kalman_em | 4 | 0.0753 |  |  |
| exact | pre_advance | A | ar | spf | 4 | -0.1973 |  |  |
| exact | pre_advance | A | ar | standard_dfm | 4 | 0.0282 |  |  |
| exact | pre_advance | A | bridge | ar | 4 | -0.0146 |  |  |
| exact | pre_advance | A | bridge | indicator_revision_only_dfm_kalman_em | 4 | 0.0494 |  |  |
| exact | pre_advance | A | bridge | joint_indicator_revision_dfm_full_kalman_em | 4 | 0.0849 |  |  |
| exact | pre_advance | A | bridge | midas_umidas | 4 | -2.5667 |  |  |
| exact | pre_advance | A | bridge | monthly_mixed_frequency_kalman_em | 4 | 0.0734 |  |  |

## Point MCS-Style Bootstrap Rows

| timing_mode | checkpoint_id | outcome_id | model_id | mean_squared_error | included_in_mcs_alpha_10pct | final_model_count | last_set_p_value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.1974 | True | 11 |  |
| exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.2090 | True | 11 |  |
| exact | pre_advance | A | revision_dfm_kalman_em | 0.2217 | True | 11 |  |
| exact | pre_advance | A | indicator_revision_only_dfm_kalman_em | 0.2329 | True | 11 |  |
| exact | pre_advance | A | release_dfm | 0.2687 | True | 11 |  |
| exact | pre_advance | A | standard_dfm | 0.2687 | True | 11 |  |
| exact | pre_advance | A | bridge | 0.2823 | True | 11 |  |
| exact | pre_advance | A | ar | 0.2970 | True | 11 |  |
| exact | pre_advance | A | no_revision | 0.3597 | True | 11 |  |
| exact | pre_advance | A | spf | 0.4943 | True | 11 |  |
| exact | pre_advance | A | midas_umidas | 2.8490 | True | 11 |  |
| exact | pre_second | S | bridge | 0.0252 | True | 11 |  |
| exact | pre_second | S | no_revision | 0.0343 | True | 11 |  |
| exact | pre_second | S | release_dfm | 0.0631 | True | 11 |  |
| exact | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.1079 | True | 11 |  |
| exact | pre_second | S | monthly_mixed_frequency_kalman_em | 0.1352 | True | 11 |  |
| exact | pre_second | S | standard_dfm | 0.1421 | True | 11 |  |
| exact | pre_second | S | revision_dfm_kalman_em | 0.1511 | True | 11 |  |
| exact | pre_second | S | joint_indicator_revision_dfm_full_kalman_em | 0.1762 | True | 11 |  |
| exact | pre_second | S | ar | 0.5451 | True | 11 |  |

## Point Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | A | 4 | -1.9820 | 0.6995 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 4 | -2.1419 | 0.8104 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_advance | A | 4 | -2.1690 | 0.8338 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | A | 4 | -2.2527 | 0.9025 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | S | 4 | -1.7465 | 0.5479 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_second | S | 4 | -1.7752 | 0.5682 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 4 | -1.7814 | 0.5746 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | S | 4 | -1.7901 | 0.5747 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | T | 4 | -1.6609 | 0.4974 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_third | T | 4 | -1.6696 | 0.5016 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 4 | -1.6755 | 0.5053 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | T | 4 | -1.8482 | 0.6057 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | A | 4 | -1.9820 | 0.6995 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 4 | -2.1418 | 0.8100 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_advance | A | 4 | -2.1681 | 0.8311 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | A | 4 | -2.2531 | 0.9036 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | S | 4 | -1.7465 | 0.5479 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_second | S | 4 | -1.7751 | 0.5682 | 1.0000 | 1.0000 |

## Revision Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | DELTA_SA | 4 | -1.8366 | 0.5890 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_advance | DELTA_SA | 4 | -1.9712 | 0.6792 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | DELTA_SA | 4 | -1.9863 | 0.6854 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | DELTA_SA | 4 | -1.9804 | 0.6855 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_second | DELTA_TS | 4 | -1.8370 | 0.5880 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | DELTA_TS | 4 | -1.8536 | 0.5977 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | DELTA_TS | 4 | -1.8558 | 0.5990 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | DELTA_TS | 4 | -1.9925 | 0.6862 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | DELTA_MT | 4 | -1.9788 | 0.7020 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_third | DELTA_MT | 4 | -2.0263 | 0.7384 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | DELTA_MT | 4 | -2.0343 | 0.7444 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | DELTA_MT | 4 | -2.1942 | 0.8651 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 4 | -1.8366 | 0.5890 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 4 | -1.9711 | 0.6789 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | DELTA_SA | 4 | -1.9803 | 0.6853 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | DELTA_SA | 4 | -1.9863 | 0.6854 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_second | DELTA_TS | 4 | -1.8370 | 0.5880 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | DELTA_TS | 4 | -1.8536 | 0.5977 | 1.0000 | 1.0000 |

## Calendar Audit

| audit_item | value | detail |
| --- | --- | --- |
| calendar_rows | 960 | gdp_release_calendar_used.csv |
| calendar_status::derived_from_alfred_gdpc1_vintage_date | 641 | all release rounds |
| calendar_status::fallback_deterministic_month_end | 319 | all release rounds |
| headline_A_S_T_calendar_status::derived_from_alfred_gdpc1_vintage_date | 240 | 2005Q1-2024Q4 |

## Figures

- `figures/point_cumulative_loss_exact_pre_third_T_joint_vs_release.png`
- `figures/point_cumulative_loss_exact_pre_second_S_release_vs_standard.png`
- `figures/revision_cumulative_loss_exact_delta_sa_joint_vs_release.png`
