# Journal Evidence Package

Generated UTC: `2026-04-25T15:11:14+00:00`

Source backtest directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/smoke_q2_check`

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
| exact | pre_advance | A | ar | indicator_revision_only_dfm_kalman_em | 1 | -0.0060 |  |  |
| exact | pre_advance | A | ar | joint_indicator_revision_dfm_full_kalman_em | 1 | 0.0506 |  |  |
| exact | pre_advance | A | ar | midas_umidas | 1 | -0.5593 |  |  |
| exact | pre_advance | A | ar | monthly_mixed_frequency_kalman_em | 1 | 0.0021 |  |  |
| exact | pre_advance | A | ar | no_revision | 1 | 0.0261 |  |  |
| exact | pre_advance | A | ar | release_dfm | 1 | 0.0331 |  |  |
| exact | pre_advance | A | ar | revision_dfm_kalman_em | 1 | 0.0452 |  |  |
| exact | pre_advance | A | ar | standard_dfm | 1 | 0.0331 |  |  |
| exact | pre_advance | A | bridge | ar | 1 | 0.0004 |  |  |
| exact | pre_advance | A | bridge | indicator_revision_only_dfm_kalman_em | 1 | -0.0055 |  |  |
| exact | pre_advance | A | bridge | joint_indicator_revision_dfm_full_kalman_em | 1 | 0.0511 |  |  |
| exact | pre_advance | A | bridge | midas_umidas | 1 | -0.5588 |  |  |
| exact | pre_advance | A | bridge | monthly_mixed_frequency_kalman_em | 1 | 0.0025 |  |  |
| exact | pre_advance | A | bridge | no_revision | 1 | 0.0266 |  |  |

## Point MCS-Style Bootstrap Rows

| timing_mode | checkpoint_id | outcome_id | model_id | mean_squared_error | included_in_mcs_alpha_10pct | final_model_count | last_set_p_value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.0128 | True | 10 |  |
| exact | pre_advance | A | revision_dfm_kalman_em | 0.0182 | True | 10 |  |
| exact | pre_advance | A | release_dfm | 0.0303 | True | 10 |  |
| exact | pre_advance | A | standard_dfm | 0.0303 | True | 10 |  |
| exact | pre_advance | A | no_revision | 0.0373 | True | 10 |  |
| exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.0613 | True | 10 |  |
| exact | pre_advance | A | ar | 0.0634 | True | 10 |  |
| exact | pre_advance | A | bridge | 0.0639 | True | 10 |  |
| exact | pre_advance | A | indicator_revision_only_dfm_kalman_em | 0.0694 | True | 10 |  |
| exact | pre_advance | A | midas_umidas | 0.6227 | True | 10 |  |
| exact | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.0000 | True | 10 |  |
| exact | pre_second | S | release_dfm | 0.0002 | True | 10 |  |
| exact | pre_second | S | standard_dfm | 0.0011 | True | 10 |  |
| exact | pre_second | S | bridge | 0.0052 | True | 10 |  |
| exact | pre_second | S | revision_dfm_kalman_em | 0.0065 | True | 10 |  |
| exact | pre_second | S | no_revision | 0.0088 | True | 10 |  |
| exact | pre_second | S | joint_indicator_revision_dfm_full_kalman_em | 0.0120 | True | 10 |  |
| exact | pre_second | S | monthly_mixed_frequency_kalman_em | 0.0126 | True | 10 |  |
| exact | pre_second | S | ar | 0.0608 | True | 10 |  |
| exact | pre_second | S | midas_umidas | 1.8769 | True | 10 |  |

## Point Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | A | 1 | -1.9810 | 0.6827 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 1 | -2.1401 | 0.7936 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_advance | A | 1 | -2.1479 | 0.8002 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | A | 1 | -2.2580 | 0.8962 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | S | 1 | -1.7303 | 0.5276 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | S | 1 | -1.7485 | 0.5357 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 1 | -1.7755 | 0.5518 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_second | S | 1 | -1.7814 | 0.5544 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_third | T | 1 | -1.6404 | 0.4808 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | T | 1 | -1.6864 | 0.5045 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 1 | -1.6950 | 0.5079 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | T | 1 | -1.8716 | 0.6059 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | A | 1 | -1.9812 | 0.6832 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 1 | -2.1402 | 0.7938 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_advance | A | 1 | -2.1480 | 0.8005 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | A | 1 | -2.2578 | 0.8956 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | S | 1 | -1.7303 | 0.5277 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | S | 1 | -1.7485 | 0.5357 | 1.0000 | 1.0000 |

## Revision Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | DELTA_SA | 1 | -1.8574 | 0.5983 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_advance | DELTA_SA | 1 | -1.9471 | 0.6542 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | DELTA_SA | 1 | -1.9880 | 0.6810 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | DELTA_SA | 1 | -2.0104 | 0.6961 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_second | DELTA_TS | 1 | -1.8641 | 0.6025 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | DELTA_TS | 1 | -1.8662 | 0.6038 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | DELTA_TS | 1 | -1.8699 | 0.6060 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | DELTA_TS | 1 | -1.9356 | 0.6462 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | DELTA_MT | 1 | -2.0081 | 0.7289 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_third | DELTA_MT | 1 | -2.0133 | 0.7432 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | DELTA_MT | 1 | -2.0635 | 0.7760 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | DELTA_MT | 1 | -2.2279 | 0.8997 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 1 | -1.8574 | 0.5983 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 1 | -1.9471 | 0.6541 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | DELTA_SA | 1 | -1.9880 | 0.6810 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | DELTA_SA | 1 | -2.0104 | 0.6961 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_second | DELTA_TS | 1 | -1.8641 | 0.6025 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | DELTA_TS | 1 | -1.8662 | 0.6038 | 1.0000 | 1.0000 |

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
