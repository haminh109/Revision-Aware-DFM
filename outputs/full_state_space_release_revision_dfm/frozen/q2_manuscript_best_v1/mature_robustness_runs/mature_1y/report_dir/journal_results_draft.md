# Journal Results Draft

Generated UTC: `2026-04-26T00:14:13+00:00`

Source output directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/exact_pseudo_backtest_mature_1y_max_iter100`

Report package directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/exact_pseudo_backtest_mature_1y_max_iter100_report_package`

## Data Coverage

- Point forecast rows: `4780`.
- Revision forecast rows: `4760`.
- Failure rows: `0`.
- GDP release calendar rows: `960`.
- Bias convention: `forecast_error = forecast_value - realized_value`; all bias values are mean forecast errors under this convention.
- The headline 2005Q1--2024Q4 A/S/T GDP calendar is derived from ALFRED `GDPC1` vintage dates when available; fallback rows are documented in the calendar file.

## Estimation Diagnostics

Kalman/EM rows report both `convergence_rate` and `mean_iterations`. A zero convergence rate means the strict log-likelihood tolerance was not reached before the iteration cap; it does not mean the forecast failed. For a journal version, either report these as fixed-iteration EM estimates or rerun with a higher iteration cap and verify convergence.

| table | model_id | timing_mode | checkpoint_id | outcome_id | convergence_rate | mean_iterations | median_llf_relative_last_improvement | RMSE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 1.000 | 33.962 | 0.000 | 3.728 |
| point | revision_dfm_kalman_em | exact | pre_advance | A | 1.000 | 26.775 | 0.000 | 3.461 |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 1.000 | 35.063 | 0.000 | 0.671 |
| point | revision_dfm_kalman_em | exact | pre_second | S | 1.000 | 27.190 | 0.000 | 0.669 |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 1.000 | 34.600 | 0.000 | 0.374 |
| point | revision_dfm_kalman_em | exact | pre_third | T | 1.000 | 26.062 | 0.000 | 0.375 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 1.000 | 34.025 | 0.000 | 3.726 |
| point | revision_dfm_kalman_em | pseudo | pre_advance | A | 1.000 | 26.762 | 0.000 | 3.448 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | S | 1.000 | 34.886 | 0.000 | 0.670 |
| point | revision_dfm_kalman_em | pseudo | pre_second | S | 1.000 | 27.190 | 0.000 | 0.669 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | T | 1.000 | 34.638 | 0.000 | 0.374 |
| point | revision_dfm_kalman_em | pseudo | pre_third | T | 1.000 | 26.087 | 0.000 | 0.375 |

## Headline Point Forecast Winners

| timing_mode | checkpoint_id | target_id | best_models | best_RMSE | best_MAE | best_bias | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | A | standard_dfm; release_dfm | 3.066 | 1.626 | 0.561 | 80 |
| exact | pre_second | S | no_revision | 0.570 | 0.400 | -0.066 | 79 |
| exact | pre_third | T | no_revision | 0.362 | 0.240 | -0.048 | 80 |
| pseudo | pre_advance | A | standard_dfm; release_dfm | 3.052 | 1.618 | 0.585 | 80 |
| pseudo | pre_second | S | no_revision | 0.570 | 0.400 | -0.066 | 79 |
| pseudo | pre_third | T | no_revision | 0.362 | 0.240 | -0.048 | 80 |

Main reading:

- Under exact timing, the point-forecast winner by RMSE is release/factor-structured for all three headline checkpoints in this build.
- Standard DFM and release DFM tie at the advance checkpoint in the current factor-regression approximation because they use the same information before any current-quarter GDP release is observed.
- The later-release result remains the cleanest release-structure evidence: known same-quarter GDP releases materially reduce the S/T forecasting problem.

## Headline Revision Forecast Winners

| timing_mode | checkpoint_id | revision_target_id | best_models | best_RMSE | best_MAE | best_bias | best_sign_accuracy | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | DELTA_SA | monthly_mixed_frequency_kalman_em | 0.565 | 0.401 | 0.026 | 0.582 | 79 |
| exact | pre_second | DELTA_TS | revision_dfm_kalman_em | 0.361 | 0.238 | -0.051 | 0.570 | 79 |
| exact | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 1.002 | 0.470 | 0.293 | 0.000 | 80 |
| pseudo | pre_advance | DELTA_SA | monthly_mixed_frequency_kalman_em | 0.565 | 0.400 | 0.026 | 0.582 | 79 |
| pseudo | pre_second | DELTA_TS | revision_dfm_kalman_em | 0.361 | 0.238 | -0.051 | 0.570 | 79 |
| pseudo | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 1.002 | 0.470 | 0.293 | 0.000 | 80 |

Revision interpretation:

- The Kalman/EM GDP revision model and the full joint indicator-revision model improve some adjacent revision RMSE cells.
- Sign accuracy should be interpreted cautiously; it is a direction statistic for often-small revision increments, not the main evidence.

## Exact Versus Pseudo Timing

| model_id | checkpoint_id | target_id | exact | pseudo | exact_minus_pseudo_RMSE |
| --- | --- | --- | --- | --- | --- |
| ar | pre_advance | A | 7.137 | 7.137 | 0.000 |
| ar | pre_second | S | 6.942 | 6.942 | 0.000 |
| ar | pre_third | T | 6.854 | 6.854 | 0.000 |
| bridge | pre_advance | A | 4.874 | 4.853 | 0.020 |
| bridge | pre_second | S | 4.543 | 4.542 | 0.000 |
| bridge | pre_third | T | 4.402 | 4.399 | 0.003 |
| indicator_revision_only_dfm_kalman_em | pre_advance | A | 3.785 | 3.784 | 0.001 |
| indicator_revision_only_dfm_kalman_em | pre_second | S | 0.603 | 0.603 | 0.000 |
| indicator_revision_only_dfm_kalman_em | pre_third | T | 0.374 | 0.374 | 0.000 |
| joint_indicator_revision_dfm_full_kalman_em | pre_advance | A | 3.728 | 3.726 | 0.002 |
| joint_indicator_revision_dfm_full_kalman_em | pre_second | S | 0.671 | 0.670 | 0.001 |
| joint_indicator_revision_dfm_full_kalman_em | pre_third | T | 0.374 | 0.374 | -0.000 |
| midas_umidas | pre_advance | A | 13.366 | 13.554 | -0.188 |
| midas_umidas | pre_second | S | 4.770 | 4.763 | 0.008 |
| midas_umidas | pre_third | T | 6.190 | 6.187 | 0.004 |
| monthly_mixed_frequency_kalman_em | pre_advance | A | 4.570 | 4.570 | 0.001 |
| monthly_mixed_frequency_kalman_em | pre_second | S | 0.599 | 0.599 | -0.000 |
| monthly_mixed_frequency_kalman_em | pre_third | T | 0.374 | 0.370 | 0.004 |
| no_revision | pre_advance | A | 7.269 | 7.269 | 0.000 |
| no_revision | pre_second | S | 0.570 | 0.570 | 0.000 |
| no_revision | pre_third | T | 0.362 | 0.362 | 0.000 |
| release_dfm | pre_advance | A | 3.066 | 3.052 | 0.014 |
| release_dfm | pre_second | S | 0.691 | 0.690 | 0.000 |
| release_dfm | pre_third | T | 0.445 | 0.445 | -0.000 |
| revision_dfm_kalman_em | pre_advance | A | 3.461 | 3.448 | 0.013 |
| revision_dfm_kalman_em | pre_second | S | 0.669 | 0.669 | 0.000 |
| revision_dfm_kalman_em | pre_third | T | 0.375 | 0.375 | 0.000 |
| standard_dfm | pre_advance | A | 3.066 | 3.052 | 0.014 |
| standard_dfm | pre_second | S | 2.923 | 2.916 | 0.007 |
| standard_dfm | pre_third | T | 2.907 | 2.906 | 0.001 |

Negative exact-minus-pseudo values mean exact event timing lowers RMSE. Positive values mean pseudo timing has lower RMSE in that cell.

Revision timing gaps:

| model_id | checkpoint_id | revision_target_id | exact | pseudo | exact_minus_pseudo_RMSE |
| --- | --- | --- | --- | --- | --- |
| ar | pre_advance | DELTA_SA | 0.678 | 0.678 | 0.000 |
| ar | pre_second | DELTA_TS | 0.408 | 0.408 | 0.000 |
| ar | pre_third | DELTA_MT | 3.889 | 3.889 | 0.000 |
| bridge | pre_advance | DELTA_SA | 0.718 | 0.722 | -0.004 |
| bridge | pre_second | DELTA_TS | 0.492 | 0.492 | -0.001 |
| bridge | pre_third | DELTA_MT | 2.129 | 2.130 | -0.001 |
| indicator_revision_only_dfm_kalman_em | pre_advance | DELTA_SA | 0.570 | 0.570 | 0.000 |
| indicator_revision_only_dfm_kalman_em | pre_second | DELTA_TS | 0.361 | 0.361 | 0.000 |
| indicator_revision_only_dfm_kalman_em | pre_third | DELTA_MT | 1.002 | 1.002 | 0.000 |
| joint_indicator_revision_dfm_full_kalman_em | pre_advance | DELTA_SA | 0.643 | 0.644 | -0.001 |
| joint_indicator_revision_dfm_full_kalman_em | pre_second | DELTA_TS | 0.362 | 0.362 | 0.000 |
| joint_indicator_revision_dfm_full_kalman_em | pre_third | DELTA_MT | 1.004 | 1.004 | 0.000 |
| midas_umidas | pre_advance | DELTA_SA | 13.867 | 13.497 | 0.370 |
| midas_umidas | pre_second | DELTA_TS | 3.124 | 3.124 | -0.000 |
| midas_umidas | pre_third | DELTA_MT | 8.189 | 8.185 | 0.004 |
| monthly_mixed_frequency_kalman_em | pre_advance | DELTA_SA | 0.565 | 0.565 | 0.000 |
| monthly_mixed_frequency_kalman_em | pre_second | DELTA_TS | 0.379 | 0.378 | 0.001 |
| monthly_mixed_frequency_kalman_em | pre_third | DELTA_MT | 1.028 | 1.028 | 0.000 |
| no_revision | pre_advance | DELTA_SA | 0.570 | 0.570 | 0.000 |
| no_revision | pre_second | DELTA_TS | 0.361 | 0.361 | 0.000 |
| no_revision | pre_third | DELTA_MT | 1.002 | 1.002 | 0.000 |
| release_dfm | pre_advance | DELTA_SA | 0.642 | 0.641 | 0.001 |
| release_dfm | pre_second | DELTA_TS | 0.364 | 0.364 | -0.000 |
| release_dfm | pre_third | DELTA_MT | 1.154 | 1.154 | 0.000 |
| revision_dfm_kalman_em | pre_advance | DELTA_SA | 0.647 | 0.647 | 0.001 |
| revision_dfm_kalman_em | pre_second | DELTA_TS | 0.361 | 0.361 | 0.000 |
| revision_dfm_kalman_em | pre_third | DELTA_MT | 1.004 | 1.004 | -0.000 |
| standard_dfm | pre_advance | DELTA_SA | 0.642 | 0.641 | 0.001 |
| standard_dfm | pre_second | DELTA_TS | 0.367 | 0.367 | 0.000 |
| standard_dfm | pre_third | DELTA_MT | 1.115 | 1.114 | 0.001 |

## Robustness Winners

| subsample | timing_mode | checkpoint_id | target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- |
| full_sample | exact | pre_advance | A | standard_dfm; release_dfm | 3.066 | 80 |
| full_sample | exact | pre_second | S | no_revision | 0.570 | 79 |
| full_sample | exact | pre_third | T | no_revision | 0.362 | 80 |
| full_sample | pseudo | pre_advance | A | standard_dfm; release_dfm | 3.052 | 80 |
| full_sample | pseudo | pre_second | S | no_revision | 0.570 | 79 |
| full_sample | pseudo | pre_third | T | no_revision | 0.362 | 80 |
| exclude_pandemic | exact | pre_advance | A | standard_dfm; release_dfm | 1.808 | 78 |
| exclude_pandemic | exact | pre_second | S | no_revision | 0.561 | 77 |
| exclude_pandemic | exact | pre_third | T | no_revision | 0.363 | 78 |
| exclude_pandemic | pseudo | pre_advance | A | standard_dfm; release_dfm | 1.806 | 78 |
| exclude_pandemic | pseudo | pre_second | S | no_revision | 0.561 | 77 |
| exclude_pandemic | pseudo | pre_third | T | no_revision | 0.363 | 78 |
| pre_gfc | exact | pre_advance | A | standard_dfm; release_dfm | 1.270 | 12 |
| pre_gfc | exact | pre_second | S | release_dfm | 0.580 | 12 |
| pre_gfc | exact | pre_third | T | revision_dfm_kalman_em | 0.182 | 12 |
| pre_gfc | pseudo | pre_advance | A | standard_dfm; release_dfm | 1.270 | 12 |
| pre_gfc | pseudo | pre_second | S | release_dfm | 0.580 | 12 |
| pre_gfc | pseudo | pre_third | T | revision_dfm_kalman_em | 0.182 | 12 |
| gfc_and_recovery | exact | pre_advance | A | standard_dfm; release_dfm | 1.389 | 28 |
| gfc_and_recovery | exact | pre_second | S | no_revision | 0.719 | 28 |
| gfc_and_recovery | exact | pre_third | T | monthly_mixed_frequency_kalman_em | 0.513 | 28 |
| gfc_and_recovery | pseudo | pre_advance | A | standard_dfm; release_dfm | 1.406 | 28 |
| gfc_and_recovery | pseudo | pre_second | S | no_revision | 0.719 | 28 |
| gfc_and_recovery | pseudo | pre_third | T | monthly_mixed_frequency_kalman_em | 0.506 | 28 |
| post_gfc_pre_pandemic | exact | pre_advance | A | bridge | 0.904 | 20 |
| post_gfc_pre_pandemic | exact | pre_second | S | joint_indicator_revision_dfm_full_kalman_em | 0.405 | 19 |
| post_gfc_pre_pandemic | exact | pre_third | T | monthly_mixed_frequency_kalman_em | 0.256 | 20 |
| post_gfc_pre_pandemic | pseudo | pre_advance | A | bridge | 0.906 | 20 |
| post_gfc_pre_pandemic | pseudo | pre_second | S | joint_indicator_revision_dfm_full_kalman_em | 0.405 | 19 |
| post_gfc_pre_pandemic | pseudo | pre_third | T | monthly_mixed_frequency_kalman_em | 0.250 | 20 |
| post_pandemic | exact | pre_advance | A | ar | 2.336 | 16 |
| post_pandemic | exact | pre_second | S | no_revision | 0.213 | 16 |
| post_pandemic | exact | pre_third | T | release_dfm | 0.238 | 16 |
| post_pandemic | pseudo | pre_advance | A | ar | 2.336 | 16 |
| post_pandemic | pseudo | pre_second | S | no_revision | 0.213 | 16 |
| post_pandemic | pseudo | pre_third | T | release_dfm | 0.238 | 16 |

Revision robustness winners:

| subsample | timing_mode | checkpoint_id | revision_target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- |
| full_sample | exact | pre_advance | DELTA_SA | monthly_mixed_frequency_kalman_em | 0.565 | 79 |
| full_sample | exact | pre_second | DELTA_TS | revision_dfm_kalman_em | 0.361 | 79 |
| full_sample | exact | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 1.002 | 80 |
| full_sample | pseudo | pre_advance | DELTA_SA | monthly_mixed_frequency_kalman_em | 0.565 | 79 |
| full_sample | pseudo | pre_second | DELTA_TS | revision_dfm_kalman_em | 0.361 | 79 |
| full_sample | pseudo | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 1.002 | 80 |
| exclude_pandemic | exact | pre_advance | DELTA_SA | monthly_mixed_frequency_kalman_em | 0.538 | 77 |
| exclude_pandemic | exact | pre_second | DELTA_TS | revision_dfm_kalman_em | 0.361 | 77 |
| exclude_pandemic | exact | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.531 | 78 |
| exclude_pandemic | pseudo | pre_advance | DELTA_SA | monthly_mixed_frequency_kalman_em | 0.537 | 77 |
| exclude_pandemic | pseudo | pre_second | DELTA_TS | revision_dfm_kalman_em | 0.361 | 77 |
| exclude_pandemic | pseudo | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.531 | 78 |
| pre_gfc | exact | pre_advance | DELTA_SA | standard_dfm; release_dfm | 0.577 | 12 |
| pre_gfc | exact | pre_second | DELTA_TS | joint_indicator_revision_dfm_full_kalman_em | 0.194 | 12 |
| pre_gfc | exact | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.372 | 12 |
| pre_gfc | pseudo | pre_advance | DELTA_SA | standard_dfm; release_dfm | 0.577 | 12 |
| pre_gfc | pseudo | pre_second | DELTA_TS | joint_indicator_revision_dfm_full_kalman_em | 0.194 | 12 |
| pre_gfc | pseudo | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.372 | 12 |
| gfc_and_recovery | exact | pre_advance | DELTA_SA | monthly_mixed_frequency_kalman_em | 0.680 | 28 |
| gfc_and_recovery | exact | pre_second | DELTA_TS | monthly_mixed_frequency_kalman_em | 0.505 | 28 |
| gfc_and_recovery | exact | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.748 | 28 |
| gfc_and_recovery | pseudo | pre_advance | DELTA_SA | monthly_mixed_frequency_kalman_em | 0.679 | 28 |
| gfc_and_recovery | pseudo | pre_second | DELTA_TS | monthly_mixed_frequency_kalman_em | 0.505 | 28 |
| gfc_and_recovery | pseudo | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.748 | 28 |
| post_gfc_pre_pandemic | exact | pre_advance | DELTA_SA | joint_indicator_revision_dfm_full_kalman_em | 0.401 | 19 |
| post_gfc_pre_pandemic | exact | pre_second | DELTA_TS | standard_dfm | 0.224 | 19 |
| post_gfc_pre_pandemic | exact | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.445 | 20 |
| post_gfc_pre_pandemic | pseudo | pre_advance | DELTA_SA | joint_indicator_revision_dfm_full_kalman_em | 0.401 | 19 |
| post_gfc_pre_pandemic | pseudo | pre_second | DELTA_TS | standard_dfm | 0.224 | 19 |
| post_gfc_pre_pandemic | pseudo | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.445 | 20 |
| post_pandemic | exact | pre_advance | DELTA_SA | revision_dfm_kalman_em | 0.205 | 16 |
| post_pandemic | exact | pre_second | DELTA_TS | standard_dfm | 0.227 | 16 |
| post_pandemic | exact | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.210 | 16 |
| post_pandemic | pseudo | pre_advance | DELTA_SA | revision_dfm_kalman_em | 0.206 | 16 |
| post_pandemic | pseudo | pre_second | DELTA_TS | standard_dfm | 0.227 | 16 |
| post_pandemic | pseudo | pre_third | DELTA_MT | no_revision; indicator_revision_only_dfm_kalman_em | 0.210 | 16 |

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
| pre_advance | A | standard_dfm; release_dfm | 3.066 | 80 |
| pre_second | S | no_revision | 0.570 | 79 |
| pre_third | T | no_revision | 0.362 | 80 |

Pseudo headline winners:

| checkpoint_id | target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- |
| pre_advance | A | standard_dfm; release_dfm | 3.052 | 80 |
| pre_second | S | no_revision | 0.570 | 79 |
| pre_third | T | no_revision | 0.362 | 80 |

## Figures

- `figures/point_rmse_by_model_exact.png`
- `figures/point_rmse_by_model_pseudo.png`
- `figures/revision_rmse_by_model_exact.png`
- `figures/exact_minus_pseudo_point_gaps.png`
