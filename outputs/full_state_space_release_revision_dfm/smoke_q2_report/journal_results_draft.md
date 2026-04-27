# Journal Results Draft

Generated UTC: `2026-04-25T15:11:06+00:00`

Source output directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/smoke_q2_check`

Report package directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/smoke_q2_report`

## Data Coverage

- Point forecast rows: `60`.
- Revision forecast rows: `60`.
- Failure rows: `0`.
- GDP release calendar rows: `960`.
- Bias convention: `forecast_error = forecast_value - realized_value`; all bias values are mean forecast errors under this convention.
- The headline 2005Q1--2024Q4 A/S/T GDP calendar is derived from ALFRED `GDPC1` vintage dates when available; fallback rows are documented in the calendar file.

## Estimation Diagnostics

Kalman/EM rows report both `convergence_rate` and `mean_iterations`. A zero convergence rate means the strict log-likelihood tolerance was not reached before the iteration cap; it does not mean the forecast failed. For a journal version, either report these as fixed-iteration EM estimates or rerun with a higher iteration cap and verify convergence.

| table | model_id | timing_mode | checkpoint_id | outcome_id | convergence_rate | mean_iterations | median_llf_relative_last_improvement | RMSE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 0.000 | 2.000 | 0.080 | 0.113 |
| point | revision_dfm_kalman_em | exact | pre_advance | A | 0.000 | 2.000 | 0.123 | 0.135 |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 0.000 | 2.000 | 0.080 | 0.109 |
| point | revision_dfm_kalman_em | exact | pre_second | S | 0.000 | 2.000 | 0.128 | 0.080 |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 0.000 | 2.000 | 0.081 | 0.028 |
| point | revision_dfm_kalman_em | exact | pre_third | T | 0.000 | 2.000 | 0.123 | 0.007 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 0.000 | 2.000 | 0.080 | 0.121 |
| point | revision_dfm_kalman_em | pseudo | pre_advance | A | 0.000 | 2.000 | 0.123 | 0.144 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | S | 0.000 | 2.000 | 0.080 | 0.111 |
| point | revision_dfm_kalman_em | pseudo | pre_second | S | 0.000 | 2.000 | 0.128 | 0.082 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | T | 0.000 | 2.000 | 0.081 | 0.029 |
| point | revision_dfm_kalman_em | pseudo | pre_third | T | 0.000 | 2.000 | 0.123 | 0.008 |

## Headline Point Forecast Winners

| timing_mode | checkpoint_id | target_id | best_models | best_RMSE | best_MAE | best_bias | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.113 | 0.113 | 0.113 | 1 |
| exact | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.004 | 0.004 | 0.004 | 1 |
| exact | pre_third | T | revision_dfm_kalman_em | 0.007 | 0.007 | -0.007 | 1 |
| pseudo | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.121 | 0.121 | 0.121 | 1 |
| pseudo | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.005 | 0.005 | 0.005 | 1 |
| pseudo | pre_third | T | revision_dfm_kalman_em | 0.008 | 0.008 | -0.008 | 1 |

Main reading:

- Under exact timing, the point-forecast winner by RMSE is release/factor-structured for all three headline checkpoints in this build.
- Standard DFM and release DFM tie at the advance checkpoint in the current factor-regression approximation because they use the same information before any current-quarter GDP release is observed.
- The later-release result remains the cleanest release-structure evidence: known same-quarter GDP releases materially reduce the S/T forecasting problem.

## Headline Revision Forecast Winners

| timing_mode | checkpoint_id | revision_target_id | best_models | best_RMSE | best_MAE | best_bias | best_sign_accuracy | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | DELTA_SA | standard_dfm; release_dfm | 0.002 | 0.002 | -0.002 | 1.000 | 1 |
| exact | pre_second | DELTA_TS | ar | 0.025 | 0.025 | -0.025 | 1.000 | 1 |
| exact | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.599 | 0.599 | 0.599 | 0.000 | 1 |
| pseudo | pre_advance | DELTA_SA | standard_dfm; release_dfm | 0.002 | 0.002 | -0.002 | 1.000 | 1 |
| pseudo | pre_second | DELTA_TS | bridge | 0.022 | 0.022 | 0.022 | 1.000 | 1 |
| pseudo | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.599 | 0.599 | 0.599 | 0.000 | 1 |

Revision interpretation:

- The Kalman/EM GDP revision model and the full joint indicator-revision model improve some adjacent revision RMSE cells.
- Sign accuracy should be interpreted cautiously; it is a direction statistic for often-small revision increments, not the main evidence.

## Exact Versus Pseudo Timing

| model_id | checkpoint_id | target_id | exact | pseudo | exact_minus_pseudo_RMSE |
| --- | --- | --- | --- | --- | --- |
| ar | pre_advance | A | 0.252 | 0.252 | 0.000 |
| ar | pre_second | S | 0.246 | 0.246 | 0.000 |
| ar | pre_third | T | 0.222 | 0.222 | 0.000 |
| bridge | pre_advance | A | 0.253 | 0.330 | -0.077 |
| bridge | pre_second | S | 0.072 | 0.124 | -0.053 |
| bridge | pre_third | T | 0.045 | 0.013 | 0.033 |
| indicator_revision_only_dfm_kalman_em | pre_advance | A | 0.263 | 0.270 | -0.006 |
| indicator_revision_only_dfm_kalman_em | pre_second | S | 0.004 | 0.005 | -0.002 |
| indicator_revision_only_dfm_kalman_em | pre_third | T | 0.091 | 0.091 | -0.001 |
| joint_indicator_revision_dfm_full_kalman_em | pre_advance | A | 0.113 | 0.121 | -0.008 |
| joint_indicator_revision_dfm_full_kalman_em | pre_second | S | 0.109 | 0.111 | -0.001 |
| joint_indicator_revision_dfm_full_kalman_em | pre_third | T | 0.028 | 0.029 | -0.001 |
| midas_umidas | pre_advance | A | 0.789 | 0.809 | -0.020 |
| midas_umidas | pre_second | S | 1.370 | 1.395 | -0.025 |
| midas_umidas | pre_third | T | 0.358 | 0.352 | 0.006 |
| monthly_mixed_frequency_kalman_em | pre_advance | A | 0.248 | 0.237 | 0.011 |
| monthly_mixed_frequency_kalman_em | pre_second | S | 0.112 | 0.114 | -0.002 |
| monthly_mixed_frequency_kalman_em | pre_third | T | 0.026 | 0.020 | 0.006 |
| no_revision | pre_advance | A | 0.193 | 0.193 | 0.000 |
| no_revision | pre_second | S | 0.094 | 0.094 | 0.000 |
| no_revision | pre_third | T | 0.104 | 0.104 | 0.000 |
| release_dfm | pre_advance | A | 0.174 | 0.143 | 0.031 |
| release_dfm | pre_second | S | 0.015 | 0.016 | -0.000 |
| release_dfm | pre_third | T | 0.036 | 0.035 | 0.000 |
| revision_dfm_kalman_em | pre_advance | A | 0.135 | 0.144 | -0.009 |
| revision_dfm_kalman_em | pre_second | S | 0.080 | 0.082 | -0.002 |
| revision_dfm_kalman_em | pre_third | T | 0.007 | 0.008 | -0.001 |
| standard_dfm | pre_advance | A | 0.174 | 0.143 | 0.031 |
| standard_dfm | pre_second | S | 0.033 | 0.024 | 0.009 |
| standard_dfm | pre_third | T | 0.037 | 0.015 | 0.022 |

Negative exact-minus-pseudo values mean exact event timing lowers RMSE. Positive values mean pseudo timing has lower RMSE in that cell.

Revision timing gaps:

| model_id | checkpoint_id | revision_target_id | exact | pseudo | exact_minus_pseudo_RMSE |
| --- | --- | --- | --- | --- | --- |
| ar | pre_advance | DELTA_SA | 0.005 | 0.005 | 0.000 |
| ar | pre_second | DELTA_TS | 0.025 | 0.025 | 0.000 |
| ar | pre_third | DELTA_MT | 0.935 | 0.935 | 0.000 |
| bridge | pre_advance | DELTA_SA | 0.013 | 0.016 | -0.003 |
| bridge | pre_second | DELTA_TS | 0.028 | 0.022 | 0.005 |
| bridge | pre_third | DELTA_MT | 0.727 | 0.733 | -0.006 |
| indicator_revision_only_dfm_kalman_em | pre_advance | DELTA_SA | 0.094 | 0.094 | 0.000 |
| indicator_revision_only_dfm_kalman_em | pre_second | DELTA_TS | 0.104 | 0.104 | 0.000 |
| indicator_revision_only_dfm_kalman_em | pre_third | DELTA_MT | 0.599 | 0.599 | 0.000 |
| joint_indicator_revision_dfm_full_kalman_em | pre_advance | DELTA_SA | 0.059 | 0.058 | 0.001 |
| joint_indicator_revision_dfm_full_kalman_em | pre_second | DELTA_TS | 0.103 | 0.103 | -0.000 |
| joint_indicator_revision_dfm_full_kalman_em | pre_third | DELTA_MT | 0.678 | 0.678 | 0.000 |
| midas_umidas | pre_advance | DELTA_SA | 0.340 | 0.346 | -0.006 |
| midas_umidas | pre_second | DELTA_TS | 0.116 | 0.114 | 0.002 |
| midas_umidas | pre_third | DELTA_MT | 1.634 | 1.654 | -0.019 |
| monthly_mixed_frequency_kalman_em | pre_advance | DELTA_SA | 0.005 | 0.006 | -0.000 |
| monthly_mixed_frequency_kalman_em | pre_second | DELTA_TS | 0.051 | 0.050 | 0.001 |
| monthly_mixed_frequency_kalman_em | pre_third | DELTA_MT | 0.670 | 0.668 | 0.002 |
| no_revision | pre_advance | DELTA_SA | 0.094 | 0.094 | 0.000 |
| no_revision | pre_second | DELTA_TS | 0.104 | 0.104 | 0.000 |
| no_revision | pre_third | DELTA_MT | 0.599 | 0.599 | 0.000 |
| release_dfm | pre_advance | DELTA_SA | 0.002 | 0.002 | 0.000 |
| release_dfm | pre_second | DELTA_TS | 0.054 | 0.054 | 0.000 |
| release_dfm | pre_third | DELTA_MT | 0.906 | 0.902 | 0.004 |
| revision_dfm_kalman_em | pre_advance | DELTA_SA | 0.086 | 0.085 | 0.001 |
| revision_dfm_kalman_em | pre_second | DELTA_TS | 0.103 | 0.103 | -0.000 |
| revision_dfm_kalman_em | pre_third | DELTA_MT | 0.685 | 0.685 | 0.000 |
| standard_dfm | pre_advance | DELTA_SA | 0.002 | 0.002 | 0.000 |
| standard_dfm | pre_second | DELTA_TS | 0.037 | 0.037 | -0.000 |
| standard_dfm | pre_third | DELTA_MT | 0.913 | 0.913 | -0.000 |

## Robustness Winners

| subsample | timing_mode | checkpoint_id | target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- |
| full_sample | exact | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.113 | 1 |
| full_sample | exact | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.004 | 1 |
| full_sample | exact | pre_third | T | revision_dfm_kalman_em | 0.007 | 1 |
| full_sample | pseudo | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.121 | 1 |
| full_sample | pseudo | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.005 | 1 |
| full_sample | pseudo | pre_third | T | revision_dfm_kalman_em | 0.008 | 1 |
| exclude_pandemic | exact | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.113 | 1 |
| exclude_pandemic | exact | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.004 | 1 |
| exclude_pandemic | exact | pre_third | T | revision_dfm_kalman_em | 0.007 | 1 |
| exclude_pandemic | pseudo | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.121 | 1 |
| exclude_pandemic | pseudo | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.005 | 1 |
| exclude_pandemic | pseudo | pre_third | T | revision_dfm_kalman_em | 0.008 | 1 |
| post_pandemic | exact | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.113 | 1 |
| post_pandemic | exact | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.004 | 1 |
| post_pandemic | exact | pre_third | T | revision_dfm_kalman_em | 0.007 | 1 |
| post_pandemic | pseudo | pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.121 | 1 |
| post_pandemic | pseudo | pre_second | S | indicator_revision_only_dfm_kalman_em | 0.005 | 1 |
| post_pandemic | pseudo | pre_third | T | revision_dfm_kalman_em | 0.008 | 1 |

Revision robustness winners:

| subsample | timing_mode | checkpoint_id | revision_target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- |
| full_sample | exact | pre_advance | DELTA_SA | standard_dfm; release_dfm | 0.002 | 1 |
| full_sample | exact | pre_second | DELTA_TS | ar | 0.025 | 1 |
| full_sample | exact | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.599 | 1 |
| full_sample | pseudo | pre_advance | DELTA_SA | standard_dfm; release_dfm | 0.002 | 1 |
| full_sample | pseudo | pre_second | DELTA_TS | bridge | 0.022 | 1 |
| full_sample | pseudo | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.599 | 1 |
| exclude_pandemic | exact | pre_advance | DELTA_SA | standard_dfm; release_dfm | 0.002 | 1 |
| exclude_pandemic | exact | pre_second | DELTA_TS | ar | 0.025 | 1 |
| exclude_pandemic | exact | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.599 | 1 |
| exclude_pandemic | pseudo | pre_advance | DELTA_SA | standard_dfm; release_dfm | 0.002 | 1 |
| exclude_pandemic | pseudo | pre_second | DELTA_TS | bridge | 0.022 | 1 |
| exclude_pandemic | pseudo | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.599 | 1 |
| post_pandemic | exact | pre_advance | DELTA_SA | standard_dfm; release_dfm | 0.002 | 1 |
| post_pandemic | exact | pre_second | DELTA_TS | ar | 0.025 | 1 |
| post_pandemic | exact | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.599 | 1 |
| post_pandemic | pseudo | pre_advance | DELTA_SA | standard_dfm; release_dfm | 0.002 | 1 |
| post_pandemic | pseudo | pre_second | DELTA_TS | bridge | 0.022 | 1 |
| post_pandemic | pseudo | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.599 | 1 |

## Suggested Report Claim

A defensible report claim from this build is: release-structured conditioning and revision-aware state-space modeling are operationally useful in a real-time GDP release-ladder design, especially once at least one same-quarter GDP release is known. The code now supports full Kalman/EM and joint indicator-revision specifications on the same exact/pseudo origins as the benchmark family. If convergence remains below tolerance at the chosen iteration cap, describe the estimates as fixed-iteration EM/Kalman estimates and include the diagnostics table.

## Reporting Cautions

- Do not mix these full state-space outputs with older frozen outputs unless the table explicitly labels the build.
- If the paper claims full Kalman/EM estimation, cite the files in this package and the exact/pseudo backtest outputs, not the older factor-regression-only report.
- The current generated package is traceable to forecast CSVs, but model selection should still be described as out-of-sample RMSE ranking rather than proof of universal dominance.
- One S-release quarter has incomplete RTDSM target coverage in the current data, so S and DELTA_SA/DELTA_TS headline cells have 79 forecasts rather than 80.

## Quick Narrative Anchors

Exact headline winners:

| checkpoint_id | target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- |
| pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.113 | 1 |
| pre_second | S | indicator_revision_only_dfm_kalman_em | 0.004 | 1 |
| pre_third | T | revision_dfm_kalman_em | 0.007 | 1 |

Pseudo headline winners:

| checkpoint_id | target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- |
| pre_advance | A | joint_indicator_revision_dfm_full_kalman_em | 0.121 | 1 |
| pre_second | S | indicator_revision_only_dfm_kalman_em | 0.005 | 1 |
| pre_third | T | revision_dfm_kalman_em | 0.008 | 1 |

## Figures

- `figures/point_rmse_by_model_exact.png`
- `figures/point_rmse_by_model_pseudo.png`
- `figures/revision_rmse_by_model_exact.png`
- `figures/exact_minus_pseudo_point_gaps.png`
