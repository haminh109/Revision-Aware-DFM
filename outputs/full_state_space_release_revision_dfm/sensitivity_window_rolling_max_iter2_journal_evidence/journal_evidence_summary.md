# Journal Evidence Package

Generated UTC: `2026-04-26T11:07:16+00:00`

Source backtest directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/sensitivity_window_rolling_max_iter2`

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
| exact | pre_advance | A | ar | bridge | 4 | -0.4021 |  |  |
| exact | pre_advance | A | ar | indicator_revision_only_dfm_kalman_em | 4 | 0.4331 |  |  |
| exact | pre_advance | A | ar | joint_indicator_revision_dfm_full_kalman_em | 4 | 0.1997 |  |  |
| exact | pre_advance | A | ar | midas_umidas | 4 | -1.4224 |  |  |
| exact | pre_advance | A | ar | monthly_mixed_frequency_kalman_em | 4 | 0.5408 |  |  |
| exact | pre_advance | A | ar | no_revision | 4 | 0.0000 |  |  |
| exact | pre_advance | A | ar | release_dfm | 4 | -1.1256 |  |  |
| exact | pre_advance | A | ar | revision_dfm_kalman_em | 4 | 0.2947 |  |  |
| exact | pre_advance | A | ar | spf | 4 | 0.3350 |  |  |
| exact | pre_advance | A | ar | standard_dfm | 4 | -1.1256 |  |  |
| exact | pre_advance | A | bridge | ar | 4 | 0.4021 |  |  |
| exact | pre_advance | A | bridge | indicator_revision_only_dfm_kalman_em | 4 | 0.8353 |  |  |
| exact | pre_advance | A | bridge | joint_indicator_revision_dfm_full_kalman_em | 4 | 0.6018 |  |  |
| exact | pre_advance | A | bridge | midas_umidas | 4 | -1.0203 |  |  |
| exact | pre_advance | A | bridge | monthly_mixed_frequency_kalman_em | 4 | 0.9429 |  |  |

## Point MCS-Style Bootstrap Rows

| timing_mode | checkpoint_id | outcome_id | model_id | mean_squared_error | included_in_mcs_alpha_10pct | final_model_count | last_set_p_value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.2885 | True | 11 |  |
| exact | pre_advance | A | indicator_revision_only_dfm_kalman_em | 0.3962 | True | 11 |  |
| exact | pre_advance | A | spf | 0.4943 | True | 11 |  |
| exact | pre_advance | A | revision_dfm_kalman_em | 0.5346 | True | 11 |  |
| exact | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.6296 | True | 11 |  |
| exact | pre_advance | A | no_revision | 0.8293 | True | 11 |  |
| exact | pre_advance | A | ar | 0.8293 | True | 11 |  |
| exact | pre_advance | A | bridge | 1.2314 | True | 11 |  |
| exact | pre_advance | A | release_dfm | 1.9549 | True | 11 |  |
| exact | pre_advance | A | standard_dfm | 1.9549 | True | 11 |  |
| exact | pre_advance | A | midas_umidas | 2.2517 | True | 11 |  |
| exact | pre_second | S | no_revision | 0.0343 | True | 11 |  |
| exact | pre_second | S | release_dfm | 0.0662 | True | 11 |  |
| exact | pre_second | S | midas_umidas | 0.1132 | True | 11 |  |
| exact | pre_second | S | revision_dfm_kalman_em | 0.1325 | True | 11 |  |
| exact | pre_second | S | monthly_mixed_frequency_kalman_em | 0.1413 | True | 11 |  |
| exact | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.2041 | True | 11 |  |
| exact | pre_second | S | joint_indicator_revision_dfm_full_kalman_em | 0.2247 | True | 11 |  |
| exact | pre_second | S | ar | 0.5606 | True | 11 |  |
| exact | pre_second | S | spf | 0.6809 | True | 11 |  |

## Point Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | A | 4 | -2.2955 | 0.9541 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 4 | -2.4346 | 1.1027 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_advance | A | 4 | -2.4503 | 1.1136 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | A | 4 | -2.6758 | 1.3688 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | S | 4 | -2.1534 | 0.8199 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 4 | -2.1657 | 0.8313 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_second | S | 4 | -2.2010 | 0.8536 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | S | 4 | -2.3645 | 1.0012 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_third | T | 4 | -2.1514 | 0.8122 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 4 | -2.1892 | 0.8467 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | T | 4 | -2.1972 | 0.8544 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | T | 4 | -2.3350 | 0.9773 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | A | 4 | -2.2950 | 0.9525 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 4 | -2.4340 | 1.1006 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_advance | A | 4 | -2.4492 | 1.1099 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | A | 4 | -2.6759 | 1.3691 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | S | 4 | -2.1534 | 0.8198 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | S | 4 | -2.1656 | 0.8312 | 1.0000 | 1.0000 |

## Revision Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | DELTA_SA | 4 | -2.3981 | 1.0299 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_advance | DELTA_SA | 4 | -2.4875 | 1.1297 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | DELTA_SA | 4 | -2.4957 | 1.1389 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | DELTA_SA | 4 | -2.5136 | 1.1578 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | DELTA_TS | 4 | -2.3185 | 0.9489 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | DELTA_TS | 4 | -2.3271 | 0.9571 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_second | DELTA_TS | 4 | -2.3570 | 0.9880 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | DELTA_TS | 4 | -2.6147 | 1.2754 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | DELTA_MT | 4 | -2.4484 | 1.0976 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_third | DELTA_MT | 4 | -2.4879 | 1.1440 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | DELTA_MT | 4 | -2.5352 | 1.1967 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | DELTA_MT | 4 | -2.6843 | 1.3862 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 4 | -2.3981 | 1.0299 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 4 | -2.4874 | 1.1295 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | DELTA_SA | 4 | -2.4956 | 1.1388 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | DELTA_SA | 4 | -2.5136 | 1.1578 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | DELTA_TS | 4 | -2.3185 | 0.9489 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | DELTA_TS | 4 | -2.3271 | 0.9571 | 1.0000 | 1.0000 |

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
