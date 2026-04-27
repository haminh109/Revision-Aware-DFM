# Journal Evidence Package

Generated UTC: `2026-04-26T18:58:19+00:00`

Source backtest directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/exact_pseudo_backtest_mature_3y_max_iter100`

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
| exact | pre_advance | A | ar | spf | 80 | 45.9846 | 1.1084 | 0.1338 |
| exact | pre_advance | A | ar | release_dfm | 80 | 41.5355 | 1.0812 | 0.1398 |
| exact | pre_advance | A | ar | standard_dfm | 80 | 41.5355 | 1.0812 | 0.1398 |
| exact | pre_advance | A | ar | bridge | 80 | 27.1821 | 1.0763 | 0.1409 |
| exact | pre_advance | A | ar | revision_dfm_kalman_em | 80 | 38.5079 | 1.0617 | 0.1442 |
| exact | pre_advance | A | ar | joint_indicator_revision_dfm_full_kalman_em | 80 | 36.6848 | 1.0238 | 0.1530 |
| exact | pre_advance | A | ar | indicator_revision_only_dfm_kalman_em | 80 | 36.1709 | 1.0036 | 0.1578 |
| exact | pre_advance | A | ar | monthly_mixed_frequency_kalman_em | 80 | 29.2419 | 0.9970 | 0.1594 |
| exact | pre_advance | A | ar | no_revision | 80 | -1.9098 | -1.2209 | 0.8889 |
| exact | pre_advance | A | ar | midas_umidas | 80 | -127.7273 | -2.6386 | 0.9958 |
| exact | pre_advance | A | bridge | spf | 80 | 18.8025 | 1.1557 | 0.1239 |
| exact | pre_advance | A | bridge | release_dfm | 80 | 14.3534 | 1.0892 | 0.1380 |
| exact | pre_advance | A | bridge | standard_dfm | 80 | 14.3534 | 1.0892 | 0.1380 |
| exact | pre_advance | A | bridge | revision_dfm_kalman_em | 80 | 11.3258 | 1.0214 | 0.1535 |
| exact | pre_advance | A | bridge | joint_indicator_revision_dfm_full_kalman_em | 80 | 9.5027 | 0.8838 | 0.1884 |

## Point MCS-Style Bootstrap Rows

| timing_mode | checkpoint_id | outcome_id | model_id | mean_squared_error | included_in_mcs_alpha_10pct | final_model_count | last_set_p_value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | A | spf | 4.9504 | True | 10 | 0.6027 |
| exact | pre_advance | A | release_dfm | 9.3995 | True | 10 | 0.6027 |
| exact | pre_advance | A | standard_dfm | 9.3995 | True | 10 | 0.6027 |
| exact | pre_advance | A | revision_dfm_kalman_em | 12.4271 | True | 10 | 0.6027 |
| exact | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 14.2502 | True | 10 | 0.6027 |
| exact | pre_advance | A | indicator_revision_only_dfm_kalman_em | 14.7641 | True | 10 | 0.6027 |
| exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 21.6931 | True | 10 | 0.6027 |
| exact | pre_advance | A | bridge | 23.7529 | True | 10 | 0.6027 |
| exact | pre_advance | A | ar | 50.9350 | True | 10 | 0.6027 |
| exact | pre_advance | A | no_revision | 52.8448 | True | 10 | 0.6027 |
| exact | pre_advance | A | midas_umidas | 178.6623 | False | 10 | 0.6027 |
| exact | pre_second | S | no_revision | 0.3245 | True | 11 | 0.1438 |
| exact | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.3582 | True | 11 | 0.1438 |
| exact | pre_second | S | monthly_mixed_frequency_kalman_em | 0.3723 | True | 11 | 0.1438 |
| exact | pre_second | S | joint_indicator_revision_dfm_full_kalman_em | 0.4208 | True | 11 | 0.1438 |
| exact | pre_second | S | revision_dfm_kalman_em | 0.4435 | True | 11 | 0.1438 |
| exact | pre_second | S | release_dfm | 0.4771 | True | 11 | 0.1438 |
| exact | pre_second | S | spf | 5.4636 | True | 11 | 0.1438 |
| exact | pre_second | S | standard_dfm | 8.5462 | True | 11 | 0.1438 |
| exact | pre_second | S | bridge | 20.6357 | True | 11 | 0.1438 |

## Point Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| spf | exact | pre_advance | A | 68 | -2.7151 | 1.0659 | 0.6618 | 0.8971 |
| release_dfm | exact | pre_advance | A | 68 | -3.4728 | 1.3710 | 0.6765 | 0.8529 |
| standard_dfm | exact | pre_advance | A | 68 | -3.4728 | 1.3710 | 0.6765 | 0.8529 |
| revision_dfm_kalman_em | exact | pre_advance | A | 80 | -3.7083 | 1.5052 | 0.6875 | 0.8625 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 80 | -4.3705 | 1.6650 | 0.6000 | 0.7750 |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | A | 80 | -3.8362 | 1.7409 | 0.6250 | 0.8125 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | A | 80 | -4.7401 | 1.7961 | 0.7250 | 0.8750 |
| bridge | exact | pre_advance | A | 68 | -4.2343 | 1.8351 | 0.7794 | 0.8971 |
| ar | exact | pre_advance | A | 68 | -5.6181 | 2.4184 | 0.8235 | 0.9265 |
| no_revision | exact | pre_advance | A | 68 | -5.6216 | 2.4988 | 0.8235 | 0.9265 |
| midas_umidas | exact | pre_advance | A | 68 | -4.1142 | 6.2809 | 0.8382 | 0.9559 |
| no_revision | exact | pre_second | S | 67 | -0.8834 | 0.3002 | 0.8657 | 0.9403 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | S | 79 | -0.9311 | 0.3156 | 0.7975 | 0.9114 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | S | 79 | -0.9061 | 0.3277 | 0.7975 | 0.9114 |
| revision_dfm_kalman_em | exact | pre_second | S | 79 | -1.0219 | 0.3454 | 0.7848 | 0.9114 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 79 | -0.9950 | 0.3548 | 0.7342 | 0.8861 |
| release_dfm | exact | pre_second | S | 67 | -1.1439 | 0.3591 | 0.8358 | 0.9254 |
| spf | exact | pre_second | S | 67 | -2.6206 | 1.1638 | 0.7164 | 0.8806 |

## Revision Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| no_revision | exact | pre_advance | DELTA_SA | 67 | -0.8834 | 0.3002 | 0.8657 | 0.9403 |
| spf | exact | pre_advance | DELTA_SA | 67 | -0.8834 | 0.3002 | 0.8657 | 0.9403 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | DELTA_SA | 79 | -0.8557 | 0.3062 | 0.7975 | 0.9114 |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | DELTA_SA | 79 | -0.8771 | 0.3084 | 0.8354 | 0.9367 |
| revision_dfm_kalman_em | exact | pre_advance | DELTA_SA | 79 | -0.9693 | 0.3405 | 0.7975 | 0.8987 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | DELTA_SA | 79 | -0.9556 | 0.3415 | 0.7468 | 0.9114 |
| release_dfm | exact | pre_advance | DELTA_SA | 67 | -1.0405 | 0.3417 | 0.8507 | 0.9254 |
| standard_dfm | exact | pre_advance | DELTA_SA | 67 | -1.0405 | 0.3417 | 0.8507 | 0.9254 |
| ar | exact | pre_advance | DELTA_SA | 67 | -1.0821 | 0.3640 | 0.8507 | 0.9403 |
| bridge | exact | pre_advance | DELTA_SA | 67 | -1.1528 | 0.3913 | 0.8507 | 0.8955 |
| midas_umidas | exact | pre_advance | DELTA_SA | 67 | -4.0642 | 6.6520 | 0.8955 | 0.9552 |
| revision_dfm_kalman_em | exact | pre_second | DELTA_TS | 79 | -0.4163 | 0.1838 | 0.8354 | 0.9494 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | DELTA_TS | 79 | -0.4160 | 0.1841 | 0.8481 | 0.9494 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | DELTA_TS | 79 | -0.4176 | 0.1841 | 0.8481 | 0.9494 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | DELTA_TS | 79 | -0.4714 | 0.1965 | 0.8354 | 0.9367 |
| no_revision | exact | pre_second | DELTA_TS | 67 | -0.6440 | 0.1969 | 0.7612 | 0.8657 |
| spf | exact | pre_second | DELTA_TS | 67 | -0.6440 | 0.1969 | 0.7612 | 0.8657 |
| release_dfm | exact | pre_second | DELTA_TS | 67 | -0.6377 | 0.1979 | 0.7463 | 0.8657 |

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
