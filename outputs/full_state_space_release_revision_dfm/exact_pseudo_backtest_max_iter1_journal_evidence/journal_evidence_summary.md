# Journal Evidence Package

Generated UTC: `2026-04-26T16:29:06+00:00`

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
| exact | pre_advance | A | ar | bridge | 2 | -0.0355 |  |  |
| exact | pre_advance | A | ar | indicator_revision_only_dfm_kalman_em | 2 | -0.0417 |  |  |
| exact | pre_advance | A | ar | joint_indicator_revision_dfm_full_kalman_em | 2 | -0.0624 |  |  |
| exact | pre_advance | A | ar | midas_umidas | 2 | -1.6705 |  |  |
| exact | pre_advance | A | ar | monthly_mixed_frequency_kalman_em | 2 | -0.0765 |  |  |
| exact | pre_advance | A | ar | no_revision | 2 | -0.0184 |  |  |
| exact | pre_advance | A | ar | release_dfm | 2 | -0.3864 |  |  |
| exact | pre_advance | A | ar | revision_dfm_kalman_em | 2 | -0.0497 |  |  |
| exact | pre_advance | A | ar | spf | 2 | -0.4321 |  |  |
| exact | pre_advance | A | ar | standard_dfm | 2 | -0.3864 |  |  |
| exact | pre_advance | A | bridge | ar | 2 | 0.0355 |  |  |
| exact | pre_advance | A | bridge | indicator_revision_only_dfm_kalman_em | 2 | -0.0062 |  |  |
| exact | pre_advance | A | bridge | joint_indicator_revision_dfm_full_kalman_em | 2 | -0.0269 |  |  |
| exact | pre_advance | A | bridge | midas_umidas | 2 | -1.6350 |  |  |
| exact | pre_advance | A | bridge | monthly_mixed_frequency_kalman_em | 2 | -0.0410 |  |  |

## Point MCS-Style Bootstrap Rows

| timing_mode | checkpoint_id | outcome_id | model_id | mean_squared_error | included_in_mcs_alpha_10pct | final_model_count | last_set_p_value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | A | ar | 0.0837 | True | 11 |  |
| exact | pre_advance | A | no_revision | 0.1021 | True | 11 |  |
| exact | pre_advance | A | bridge | 0.1192 | True | 11 |  |
| exact | pre_advance | A | indicator_revision_only_dfm_kalman_em | 0.1254 | True | 11 |  |
| exact | pre_advance | A | revision_dfm_kalman_em | 0.1334 | True | 11 |  |
| exact | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.1461 | True | 11 |  |
| exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.1603 | True | 11 |  |
| exact | pre_advance | A | release_dfm | 0.4702 | True | 11 |  |
| exact | pre_advance | A | standard_dfm | 0.4702 | True | 11 |  |
| exact | pre_advance | A | spf | 0.5158 | True | 11 |  |
| exact | pre_advance | A | midas_umidas | 1.7543 | True | 11 |  |
| exact | pre_second | S | no_revision | 0.0044 | True | 11 |  |
| exact | pre_second | S | release_dfm | 0.0065 | True | 11 |  |
| exact | pre_second | S | monthly_mixed_frequency_kalman_em | 0.0166 | True | 11 |  |
| exact | pre_second | S | revision_dfm_kalman_em | 0.0201 | True | 11 |  |
| exact | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.0283 | True | 11 |  |
| exact | pre_second | S | joint_indicator_revision_dfm_full_kalman_em | 0.0305 | True | 11 |  |
| exact | pre_second | S | bridge | 0.0480 | True | 11 |  |
| exact | pre_second | S | ar | 0.0584 | True | 11 |  |
| exact | pre_second | S | standard_dfm | 0.2087 | True | 11 |  |

## Point Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | A | 2 | -2.2067 | 0.8568 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_advance | A | 2 | -2.3394 | 0.9764 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 2 | -2.3461 | 0.9837 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | A | 2 | -2.3458 | 0.9844 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | S | 2 | -2.1029 | 0.7652 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_second | S | 2 | -2.1052 | 0.7672 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 2 | -2.1202 | 0.7795 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | S | 2 | -2.1276 | 0.7850 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_third | T | 2 | -2.0667 | 0.7419 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 2 | -2.0863 | 0.7571 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | T | 2 | -2.0973 | 0.7660 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | T | 2 | -2.1424 | 0.8015 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | A | 2 | -2.2066 | 0.8566 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_advance | A | 2 | -2.3394 | 0.9765 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 2 | -2.3459 | 0.9832 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | A | 2 | -2.3458 | 0.9842 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | S | 2 | -2.1029 | 0.7651 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_second | S | 2 | -2.1052 | 0.7671 | 1.0000 | 1.0000 |

## Revision Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | DELTA_SA | 2 | -2.3057 | 0.9355 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_advance | DELTA_SA | 2 | -2.3337 | 0.9621 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | DELTA_SA | 2 | -2.3524 | 0.9801 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | DELTA_SA | 2 | -2.3733 | 1.0010 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_second | DELTA_TS | 2 | -2.2773 | 0.9117 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | DELTA_TS | 2 | -2.3014 | 0.9336 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | DELTA_TS | 2 | -2.3167 | 0.9480 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | DELTA_TS | 2 | -2.3446 | 0.9749 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | DELTA_MT | 2 | -2.3636 | 1.0053 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_third | DELTA_MT | 2 | -2.3691 | 1.0137 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | DELTA_MT | 2 | -2.3893 | 1.0330 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | DELTA_MT | 2 | -2.4610 | 1.1075 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 2 | -2.3057 | 0.9355 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 2 | -2.3337 | 0.9621 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | DELTA_SA | 2 | -2.3524 | 0.9801 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | DELTA_SA | 2 | -2.3733 | 1.0010 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_second | DELTA_TS | 2 | -2.2773 | 0.9117 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | DELTA_TS | 2 | -2.3014 | 0.9336 | 1.0000 | 1.0000 |

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
