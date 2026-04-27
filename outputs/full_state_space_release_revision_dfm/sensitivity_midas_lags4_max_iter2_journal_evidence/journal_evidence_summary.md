# Journal Evidence Package

Generated UTC: `2026-04-26T11:06:41+00:00`

Source backtest directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/sensitivity_midas_lags4_max_iter2`

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
| exact | pre_advance | A | ar | indicator_revision_only_dfm_kalman_em | 4 | 0.0150 |  |  |
| exact | pre_advance | A | ar | joint_indicator_revision_dfm_full_kalman_em | 4 | 0.0282 |  |  |
| exact | pre_advance | A | ar | midas_umidas | 4 | -3.7717 |  |  |
| exact | pre_advance | A | ar | monthly_mixed_frequency_kalman_em | 4 | 0.1913 |  |  |
| exact | pre_advance | A | ar | no_revision | 4 | -0.0628 |  |  |
| exact | pre_advance | A | ar | release_dfm | 4 | -0.0452 |  |  |
| exact | pre_advance | A | ar | revision_dfm_kalman_em | 4 | 0.0359 |  |  |
| exact | pre_advance | A | ar | spf | 4 | -0.1973 |  |  |
| exact | pre_advance | A | ar | standard_dfm | 4 | -0.0452 |  |  |
| exact | pre_advance | A | bridge | ar | 4 | -0.0146 |  |  |
| exact | pre_advance | A | bridge | indicator_revision_only_dfm_kalman_em | 4 | 0.0004 |  |  |
| exact | pre_advance | A | bridge | joint_indicator_revision_dfm_full_kalman_em | 4 | 0.0136 |  |  |
| exact | pre_advance | A | bridge | midas_umidas | 4 | -3.7863 |  |  |
| exact | pre_advance | A | bridge | monthly_mixed_frequency_kalman_em | 4 | 0.1766 |  |  |

## Point MCS-Style Bootstrap Rows

| timing_mode | checkpoint_id | outcome_id | model_id | mean_squared_error | included_in_mcs_alpha_10pct | final_model_count | last_set_p_value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.1057 | True | 11 |  |
| exact | pre_advance | A | revision_dfm_kalman_em | 0.2611 | True | 11 |  |
| exact | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.2688 | True | 11 |  |
| exact | pre_advance | A | indicator_revision_only_dfm_kalman_em | 0.2820 | True | 11 |  |
| exact | pre_advance | A | bridge | 0.2823 | True | 11 |  |
| exact | pre_advance | A | ar | 0.2970 | True | 11 |  |
| exact | pre_advance | A | release_dfm | 0.3421 | True | 11 |  |
| exact | pre_advance | A | standard_dfm | 0.3421 | True | 11 |  |
| exact | pre_advance | A | no_revision | 0.3597 | True | 11 |  |
| exact | pre_advance | A | spf | 0.4943 | True | 11 |  |
| exact | pre_advance | A | midas_umidas | 4.0686 | True | 11 |  |
| exact | pre_second | S | bridge | 0.0252 | True | 11 |  |
| exact | pre_second | S | no_revision | 0.0343 | True | 11 |  |
| exact | pre_second | S | release_dfm | 0.0564 | True | 11 |  |
| exact | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.1076 | True | 11 |  |
| exact | pre_second | S | monthly_mixed_frequency_kalman_em | 0.1162 | True | 11 |  |
| exact | pre_second | S | revision_dfm_kalman_em | 0.1467 | True | 11 |  |
| exact | pre_second | S | standard_dfm | 0.1601 | True | 11 |  |
| exact | pre_second | S | joint_indicator_revision_dfm_full_kalman_em | 0.1663 | True | 11 |  |
| exact | pre_second | S | ar | 0.5451 | True | 11 |  |

## Point Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | A | 4 | -1.9902 | 0.7098 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 4 | -2.1489 | 0.8218 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_advance | A | 4 | -2.1689 | 0.8370 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | A | 4 | -2.2523 | 0.8945 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | S | 4 | -1.7625 | 0.5563 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_second | S | 4 | -1.7752 | 0.5676 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | S | 4 | -1.7892 | 0.5724 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 4 | -1.7928 | 0.5795 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | T | 4 | -1.6621 | 0.4989 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_third | T | 4 | -1.6636 | 0.4990 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 4 | -1.6771 | 0.5069 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | T | 4 | -1.8592 | 0.6107 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | A | 4 | -1.9898 | 0.7087 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 4 | -2.1483 | 0.8202 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_advance | A | 4 | -2.1676 | 0.8336 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | A | 4 | -2.2526 | 0.8955 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | S | 4 | -1.7625 | 0.5563 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_second | S | 4 | -1.7751 | 0.5675 | 1.0000 | 1.0000 |

## Revision Density Metrics

| model_id | timing_mode | checkpoint_id | outcome_id | n_density_forecasts | mean_log_score | mean_crps | coverage_68 | coverage_90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | DELTA_SA | 4 | -1.8461 | 0.5948 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_advance | DELTA_SA | 4 | -1.9666 | 0.6764 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | DELTA_SA | 4 | -1.9865 | 0.6892 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | DELTA_SA | 4 | -1.9971 | 0.6930 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_second | DELTA_TS | 4 | -1.8372 | 0.5884 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | DELTA_TS | 4 | -1.8708 | 0.6079 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | DELTA_TS | 4 | -1.8747 | 0.6103 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | DELTA_TS | 4 | -1.9932 | 0.6873 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | DELTA_MT | 4 | -1.9795 | 0.7026 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | exact | pre_third | DELTA_MT | 4 | -2.0207 | 0.7349 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | DELTA_MT | 4 | -2.0344 | 0.7439 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | DELTA_MT | 4 | -2.2056 | 0.8743 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 4 | -1.8461 | 0.5948 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 4 | -1.9665 | 0.6762 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | DELTA_SA | 4 | -1.9864 | 0.6890 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | DELTA_SA | 4 | -1.9971 | 0.6929 | 1.0000 | 1.0000 |
| revision_dfm_kalman_em | pseudo | pre_second | DELTA_TS | 4 | -1.8372 | 0.5884 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | DELTA_TS | 4 | -1.8708 | 0.6079 | 1.0000 | 1.0000 |

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
