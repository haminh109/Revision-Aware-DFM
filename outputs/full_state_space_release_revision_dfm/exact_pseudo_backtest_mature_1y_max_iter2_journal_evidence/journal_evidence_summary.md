# Journal Evidence Package

Generated UTC: `2026-04-26T11:04:17+00:00`

Source backtest directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/exact_pseudo_backtest_mature_1y_max_iter2`

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
| exact | pre_advance | A | ar | indicator_revision_only_dfm_kalman_em | 4 | -0.0634 |  |  |
| exact | pre_advance | A | ar | joint_indicator_revision_dfm_full_kalman_em | 4 | -0.0458 |  |  |
| exact | pre_advance | A | ar | midas_umidas | 4 | -2.5521 |  |  |
| exact | pre_advance | A | ar | monthly_mixed_frequency_kalman_em | 4 | 0.1301 |  |  |
| exact | pre_advance | A | ar | no_revision | 4 | -0.0628 |  |  |
| exact | pre_advance | A | ar | release_dfm | 4 | -0.0452 |  |  |
| exact | pre_advance | A | ar | revision_dfm_kalman_em | 4 | -0.0357 |  |  |
| exact | pre_advance | A | ar | spf | 4 | -0.1973 |  |  |
| exact | pre_advance | A | ar | standard_dfm | 4 | -0.0452 |  |  |
| exact | pre_advance | A | bridge | ar | 4 | -0.0146 |  |  |
| exact | pre_advance | A | bridge | indicator_revision_only_dfm_kalman_em | 4 | -0.0780 |  |  |
| exact | pre_advance | A | bridge | joint_indicator_revision_dfm_full_kalman_em | 4 | -0.0604 |  |  |
| exact | pre_advance | A | bridge | midas_umidas | 4 | -2.5667 |  |  |
| exact | pre_advance | A | bridge | monthly_mixed_frequency_kalman_em | 4 | 0.1154 |  |  |

## Point MCS-Style Bootstrap Rows

| timing_mode | checkpoint_id | outcome_id | model_id | mean_squared_error | included_in_mcs_alpha_10pct | final_model_count | last_set_p_value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.1669 | True | 11 |  |
| exact | pre_advance | A | bridge | 0.2823 | True | 11 |  |
| exact | pre_advance | A | ar | 0.2970 | True | 11 |  |
| exact | pre_advance | A | revision_dfm_kalman_em | 0.3327 | True | 11 |  |
| exact | pre_advance | A | release_dfm | 0.3421 | True | 11 |  |
| exact | pre_advance | A | standard_dfm | 0.3421 | True | 11 |  |
| exact | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.3428 | True | 11 |  |
| exact | pre_advance | A | no_revision | 0.3597 | True | 11 |  |
| exact | pre_advance | A | indicator_revision_only_dfm_kalman_em | 0.3604 | True | 11 |  |
| exact | pre_advance | A | spf | 0.4943 | True | 11 |  |
| exact | pre_advance | A | midas_umidas | 2.8490 | True | 11 |  |
| exact | pre_second | S | bridge | 0.0252 | True | 11 |  |
| exact | pre_second | S | no_revision | 0.0343 | True | 11 |  |
| exact | pre_second | S | release_dfm | 0.0564 | True | 11 |  |
| exact | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.1031 | True | 11 |  |
| exact | pre_second | S | standard_dfm | 0.1601 | True | 11 |  |
| exact | pre_second | S | revision_dfm_kalman_em | 0.1639 | True | 11 |  |
| exact | pre_second | S | joint_indicator_revision_dfm_full_kalman_em | 0.1823 | True | 11 |  |
| exact | pre_second | S | monthly_mixed_frequency_kalman_em | 0.1861 | True | 11 |  |
| exact | pre_second | S | ar | 0.5451 | True | 11 |  |

## Point Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | A | 4 | -2.0275 | 0.7421 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 4 | -2.2074 | 0.8746 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_advance | A | 4 | -2.2390 | 0.9002 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | A | 4 | -2.2614 | 0.9071 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | S | 4 | -1.6952 | 0.5211 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 4 | -1.7892 | 0.5792 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | S | 4 | -1.7943 | 0.5828 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_second | S | 4 | -1.8173 | 0.5926 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | T | 4 | -1.6163 | 0.4759 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 4 | -1.6684 | 0.5021 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_third | T | 4 | -1.6720 | 0.5030 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | T | 4 | -1.8350 | 0.5938 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | A | 4 | -2.0272 | 0.7415 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 4 | -2.2068 | 0.8731 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_advance | A | 4 | -2.2385 | 0.8987 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | A | 4 | -2.2617 | 0.9081 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | S | 4 | -1.6951 | 0.5211 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | S | 4 | -1.7892 | 0.5792 | 1.0000 | 1.0000 |

## Revision Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | DELTA_SA | 4 | -1.7937 | 0.5650 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | DELTA_SA | 4 | -1.9734 | 0.6761 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | DELTA_SA | 4 | -2.0086 | 0.7018 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_advance | DELTA_SA | 4 | -2.0123 | 0.7045 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | DELTA_TS | 4 | -1.7855 | 0.5591 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | DELTA_TS | 4 | -1.8146 | 0.5753 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_second | DELTA_TS | 4 | -1.8507 | 0.5962 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | DELTA_TS | 4 | -1.9880 | 0.6841 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | DELTA_MT | 4 | -1.9946 | 0.6953 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | DELTA_MT | 4 | -2.0681 | 0.7475 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_third | DELTA_MT | 4 | -2.0699 | 0.7492 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | DELTA_MT | 4 | -2.2482 | 0.8923 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 4 | -1.7937 | 0.5650 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | DELTA_SA | 4 | -1.9734 | 0.6761 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | DELTA_SA | 4 | -2.0084 | 0.7015 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 4 | -2.0122 | 0.7041 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | DELTA_TS | 4 | -1.7855 | 0.5591 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | DELTA_TS | 4 | -1.8146 | 0.5753 | 1.0000 | 1.0000 |

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
