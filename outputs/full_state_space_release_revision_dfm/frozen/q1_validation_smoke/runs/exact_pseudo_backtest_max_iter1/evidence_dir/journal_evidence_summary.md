# Journal Evidence Package

Generated UTC: `2026-04-26T11:09:48+00:00`

Source backtest directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/exact_pseudo_backtest_max_iter1`

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
| exact | pre_advance | A | ar | bridge | 1 | -0.0004 |  |  |
| exact | pre_advance | A | ar | indicator_revision_only_dfm_kalman_em | 1 | -0.0564 |  |  |
| exact | pre_advance | A | ar | joint_indicator_revision_dfm_full_kalman_em | 1 | -0.0011 |  |  |
| exact | pre_advance | A | ar | midas_umidas | 1 | 0.0531 |  |  |
| exact | pre_advance | A | ar | monthly_mixed_frequency_kalman_em | 1 | -0.1845 |  |  |
| exact | pre_advance | A | ar | no_revision | 1 | 0.0261 |  |  |
| exact | pre_advance | A | ar | release_dfm | 1 | 0.0331 |  |  |
| exact | pre_advance | A | ar | revision_dfm_kalman_em | 1 | -0.0599 |  |  |
| exact | pre_advance | A | ar | spf | 1 | -0.0569 |  |  |
| exact | pre_advance | A | ar | standard_dfm | 1 | 0.0331 |  |  |
| exact | pre_advance | A | bridge | ar | 1 | 0.0004 |  |  |
| exact | pre_advance | A | bridge | indicator_revision_only_dfm_kalman_em | 1 | -0.0559 |  |  |
| exact | pre_advance | A | bridge | joint_indicator_revision_dfm_full_kalman_em | 1 | -0.0006 |  |  |
| exact | pre_advance | A | bridge | midas_umidas | 1 | 0.0535 |  |  |
| exact | pre_advance | A | bridge | monthly_mixed_frequency_kalman_em | 1 | -0.1841 |  |  |

## Point MCS-Style Bootstrap Rows

| timing_mode | checkpoint_id | outcome_id | model_id | mean_squared_error | included_in_mcs_alpha_10pct | final_model_count | last_set_p_value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | A | midas_umidas | 0.0103 | True | 11 |  |
| exact | pre_advance | A | release_dfm | 0.0303 | True | 11 |  |
| exact | pre_advance | A | standard_dfm | 0.0303 | True | 11 |  |
| exact | pre_advance | A | no_revision | 0.0373 | True | 11 |  |
| exact | pre_advance | A | ar | 0.0634 | True | 11 |  |
| exact | pre_advance | A | bridge | 0.0639 | True | 11 |  |
| exact | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.0645 | True | 11 |  |
| exact | pre_advance | A | indicator_revision_only_dfm_kalman_em | 0.1198 | True | 11 |  |
| exact | pre_advance | A | spf | 0.1203 | True | 11 |  |
| exact | pre_advance | A | revision_dfm_kalman_em | 0.1233 | True | 11 |  |
| exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.2480 | True | 11 |  |
| exact | pre_second | S | monthly_mixed_frequency_kalman_em | 0.0001 | True | 11 |  |
| exact | pre_second | S | release_dfm | 0.0002 | True | 11 |  |
| exact | pre_second | S | standard_dfm | 0.0011 | True | 11 |  |
| exact | pre_second | S | bridge | 0.0052 | True | 11 |  |
| exact | pre_second | S | no_revision | 0.0088 | True | 11 |  |
| exact | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.0141 | True | 11 |  |
| exact | pre_second | S | joint_indicator_revision_dfm_full_kalman_em | 0.0282 | True | 11 |  |
| exact | pre_second | S | revision_dfm_kalman_em | 0.0285 | True | 11 |  |
| exact | pre_second | S | ar | 0.0608 | True | 11 |  |

## Point Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | A | 1 | -2.2054 | 0.8553 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_advance | A | 1 | -2.3381 | 0.9744 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 1 | -2.3427 | 0.9749 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | A | 1 | -2.3474 | 0.9919 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | S | 1 | -2.0804 | 0.7466 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 1 | -2.1190 | 0.7784 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_second | S | 1 | -2.1222 | 0.7808 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | S | 1 | -2.1258 | 0.7824 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_third | T | 1 | -2.0432 | 0.7198 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 1 | -2.0819 | 0.7477 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | T | 1 | -2.0925 | 0.7556 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | T | 1 | -2.1381 | 0.7920 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | A | 1 | -2.2055 | 0.8557 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_advance | A | 1 | -2.3382 | 0.9750 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 1 | -2.3428 | 0.9752 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | A | 1 | -2.3472 | 0.9913 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | S | 1 | -2.0804 | 0.7466 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | S | 1 | -2.1190 | 0.7784 | 1.0000 | 1.0000 |

## Revision Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | DELTA_SA | 1 | -2.3047 | 0.9349 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_advance | DELTA_SA | 1 | -2.3324 | 0.9605 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | DELTA_SA | 1 | -2.3513 | 0.9793 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | DELTA_SA | 1 | -2.3720 | 0.9994 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_second | DELTA_TS | 1 | -2.2972 | 0.9280 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | DELTA_TS | 1 | -2.2996 | 0.9303 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | DELTA_TS | 1 | -2.3149 | 0.9446 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | DELTA_TS | 1 | -2.3183 | 0.9474 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_third | DELTA_MT | 1 | -2.3554 | 1.0131 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | DELTA_MT | 1 | -2.3671 | 1.0183 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | DELTA_MT | 1 | -2.3937 | 1.0496 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | DELTA_MT | 1 | -2.4644 | 1.1215 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 1 | -2.3047 | 0.9349 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 1 | -2.3324 | 0.9605 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | DELTA_SA | 1 | -2.3513 | 0.9793 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | DELTA_SA | 1 | -2.3720 | 0.9994 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_second | DELTA_TS | 1 | -2.2971 | 0.9280 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | DELTA_TS | 1 | -2.2996 | 0.9303 | 1.0000 | 1.0000 |

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
