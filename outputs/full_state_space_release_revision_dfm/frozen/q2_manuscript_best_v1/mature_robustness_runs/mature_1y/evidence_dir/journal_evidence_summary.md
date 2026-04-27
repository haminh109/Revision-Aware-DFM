# Journal Evidence Package

Generated UTC: `2026-04-26T00:14:24+00:00`

Source backtest directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/exact_pseudo_backtest_mature_1y_max_iter100`

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
| exact | pre_advance | A | ar | release_dfm | 80 | 41.5355 | 1.0812 | 0.1398 |
| exact | pre_advance | A | ar | standard_dfm | 80 | 41.5355 | 1.0812 | 0.1398 |
| exact | pre_advance | A | ar | bridge | 80 | 27.1821 | 1.0763 | 0.1409 |
| exact | pre_advance | A | ar | revision_dfm_kalman_em | 80 | 38.9573 | 1.0559 | 0.1455 |
| exact | pre_advance | A | ar | joint_indicator_revision_dfm_full_kalman_em | 80 | 37.0364 | 1.0166 | 0.1547 |
| exact | pre_advance | A | ar | indicator_revision_only_dfm_kalman_em | 80 | 36.6089 | 0.9957 | 0.1597 |
| exact | pre_advance | A | ar | monthly_mixed_frequency_kalman_em | 80 | 30.0494 | 0.9927 | 0.1604 |
| exact | pre_advance | A | ar | no_revision | 80 | -1.9098 | -1.2209 | 0.8889 |
| exact | pre_advance | A | ar | midas_umidas | 80 | -127.7273 | -2.6386 | 0.9958 |
| exact | pre_advance | A | bridge | release_dfm | 80 | 14.3534 | 1.0892 | 0.1380 |
| exact | pre_advance | A | bridge | standard_dfm | 80 | 14.3534 | 1.0892 | 0.1380 |
| exact | pre_advance | A | bridge | revision_dfm_kalman_em | 80 | 11.7752 | 1.0051 | 0.1574 |
| exact | pre_advance | A | bridge | joint_indicator_revision_dfm_full_kalman_em | 80 | 9.8543 | 0.8683 | 0.1926 |
| exact | pre_advance | A | bridge | indicator_revision_only_dfm_kalman_em | 80 | 9.4268 | 0.8063 | 0.2100 |
| exact | pre_advance | A | bridge | monthly_mixed_frequency_kalman_em | 80 | 2.8673 | 0.4859 | 0.3135 |

## Point MCS-Style Bootstrap Rows

| timing_mode | checkpoint_id | outcome_id | model_id | mean_squared_error | included_in_mcs_alpha_10pct | final_model_count | last_set_p_value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | A | release_dfm | 9.3995 | True | 9 | 0.5685 |
| exact | pre_advance | A | standard_dfm | 9.3995 | True | 9 | 0.5685 |
| exact | pre_advance | A | revision_dfm_kalman_em | 11.9778 | True | 9 | 0.5685 |
| exact | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 13.8986 | True | 9 | 0.5685 |
| exact | pre_advance | A | indicator_revision_only_dfm_kalman_em | 14.3261 | True | 9 | 0.5685 |
| exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 20.8856 | True | 9 | 0.5685 |
| exact | pre_advance | A | bridge | 23.7529 | True | 9 | 0.5685 |
| exact | pre_advance | A | ar | 50.9350 | True | 9 | 0.5685 |
| exact | pre_advance | A | no_revision | 52.8448 | True | 9 | 0.5685 |
| exact | pre_advance | A | midas_umidas | 178.6623 | False | 9 | 0.5685 |
| exact | pre_second | S | no_revision | 0.3245 | True | 10 | 0.1340 |
| exact | pre_second | S | monthly_mixed_frequency_kalman_em | 0.3585 | True | 10 | 0.1340 |
| exact | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.3639 | True | 10 | 0.1340 |
| exact | pre_second | S | revision_dfm_kalman_em | 0.4479 | True | 10 | 0.1340 |
| exact | pre_second | S | joint_indicator_revision_dfm_full_kalman_em | 0.4497 | True | 10 | 0.1340 |
| exact | pre_second | S | release_dfm | 0.4771 | True | 10 | 0.1340 |
| exact | pre_second | S | standard_dfm | 8.5462 | True | 10 | 0.1340 |
| exact | pre_second | S | bridge | 20.6357 | True | 10 | 0.1340 |
| exact | pre_second | S | midas_umidas | 22.7560 | True | 10 | 0.1340 |
| exact | pre_second | S | ar | 48.1930 | True | 10 | 0.1340 |

## Point Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| release_dfm | exact | pre_advance | A | 68 | -3.4728 | 1.3710 | 0.6765 | 0.8529 |
| standard_dfm | exact | pre_advance | A | 68 | -3.4728 | 1.3710 | 0.6765 | 0.8529 |
| revision_dfm_kalman_em | exact | pre_advance | A | 80 | -3.6168 | 1.5144 | 0.7000 | 0.8750 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 80 | -4.2687 | 1.6804 | 0.6000 | 0.7625 |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | A | 80 | -3.7466 | 1.7462 | 0.6250 | 0.8000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | A | 80 | -4.5214 | 1.8040 | 0.7250 | 0.8625 |
| bridge | exact | pre_advance | A | 68 | -4.2343 | 1.8351 | 0.7794 | 0.8971 |
| ar | exact | pre_advance | A | 68 | -5.6181 | 2.4184 | 0.8235 | 0.9265 |
| no_revision | exact | pre_advance | A | 68 | -5.6216 | 2.4988 | 0.8235 | 0.9265 |
| midas_umidas | exact | pre_advance | A | 68 | -4.1142 | 6.2809 | 0.8382 | 0.9559 |
| no_revision | exact | pre_second | S | 67 | -0.8834 | 0.3002 | 0.8657 | 0.9403 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | S | 79 | -0.9118 | 0.3120 | 0.8101 | 0.9114 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | S | 79 | -0.9124 | 0.3288 | 0.8101 | 0.9114 |
| revision_dfm_kalman_em | exact | pre_second | S | 79 | -1.0258 | 0.3478 | 0.7975 | 0.9114 |
| release_dfm | exact | pre_second | S | 67 | -1.1439 | 0.3591 | 0.8358 | 0.9254 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 79 | -1.0319 | 0.3637 | 0.7468 | 0.8861 |
| standard_dfm | exact | pre_second | S | 67 | -3.0271 | 1.4070 | 0.6866 | 0.8657 |
| bridge | exact | pre_second | S | 67 | -3.8618 | 1.8159 | 0.7313 | 0.9104 |

## Revision Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| no_revision | exact | pre_advance | DELTA_SA | 67 | -0.8834 | 0.3002 | 0.8657 | 0.9403 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | DELTA_SA | 79 | -0.8615 | 0.3067 | 0.7975 | 0.9114 |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | DELTA_SA | 79 | -0.8796 | 0.3088 | 0.8354 | 0.9367 |
| release_dfm | exact | pre_advance | DELTA_SA | 67 | -1.0405 | 0.3417 | 0.8507 | 0.9254 |
| standard_dfm | exact | pre_advance | DELTA_SA | 67 | -1.0405 | 0.3417 | 0.8507 | 0.9254 |
| revision_dfm_kalman_em | exact | pre_advance | DELTA_SA | 79 | -0.9887 | 0.3467 | 0.7975 | 0.8861 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | DELTA_SA | 79 | -0.9866 | 0.3504 | 0.7595 | 0.9114 |
| ar | exact | pre_advance | DELTA_SA | 67 | -1.0821 | 0.3640 | 0.8507 | 0.9403 |
| bridge | exact | pre_advance | DELTA_SA | 67 | -1.1528 | 0.3913 | 0.8507 | 0.8955 |
| midas_umidas | exact | pre_advance | DELTA_SA | 67 | -4.0642 | 6.6520 | 0.8955 | 0.9552 |
| revision_dfm_kalman_em | exact | pre_second | DELTA_TS | 79 | -0.4151 | 0.1836 | 0.8354 | 0.9494 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | DELTA_TS | 79 | -0.4156 | 0.1840 | 0.8481 | 0.9494 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | DELTA_TS | 79 | -0.4167 | 0.1840 | 0.8481 | 0.9494 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | DELTA_TS | 79 | -0.4612 | 0.1952 | 0.8354 | 0.9367 |
| no_revision | exact | pre_second | DELTA_TS | 67 | -0.6440 | 0.1969 | 0.7612 | 0.8657 |
| release_dfm | exact | pre_second | DELTA_TS | 67 | -0.6377 | 0.1979 | 0.7463 | 0.8657 |
| standard_dfm | exact | pre_second | DELTA_TS | 67 | -0.6433 | 0.1994 | 0.7612 | 0.8806 |
| ar | exact | pre_second | DELTA_TS | 67 | -0.7816 | 0.2212 | 0.7612 | 0.8657 |

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
