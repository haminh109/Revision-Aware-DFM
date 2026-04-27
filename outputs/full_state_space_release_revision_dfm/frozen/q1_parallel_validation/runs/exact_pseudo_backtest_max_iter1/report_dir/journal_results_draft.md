# Journal Results Draft

Generated UTC: `2026-04-26T16:28:55+00:00`

Source output directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/exact_pseudo_backtest_max_iter1`

Report package directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/exact_pseudo_backtest_max_iter1_report_package`

## Data Coverage

- Point forecast rows: `132`.
- Revision forecast rows: `132`.
- Failure rows: `0`.
- GDP release calendar rows: `960`.
- Bias convention: `forecast_error = forecast_value - realized_value`; all bias values are mean forecast errors under this convention.
- The headline 2005Q1--2024Q4 A/S/T GDP calendar is derived from ALFRED `GDPC1` vintage dates when available; fallback rows are documented in the calendar file.

## Estimation Diagnostics

Kalman/EM rows report `convergence_rate`, `mean_iterations`, and relative final log-likelihood improvement. Mixed-frequency rows also carry numerical guard counts in the forecast-level CSV when a finite fallback is used. For a journal version, report these diagnostics next to the headline evidence rather than treating the estimator as a black box.

| table | model_id | timing_mode | checkpoint_id | outcome_id | convergence_rate | mean_iterations | median_llf_relative_last_improvement | RMSE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 0.000 | 1.000 | 0.172 | 0.382 |
| point | revision_dfm_kalman_em | exact | pre_advance | A | 0.000 | 1.000 | 0.185 | 0.365 |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 0.000 | 1.000 | 0.172 | 0.175 |
| point | revision_dfm_kalman_em | exact | pre_second | S | 0.000 | 1.000 | 0.179 | 0.142 |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 0.000 | 1.000 | 0.172 | 0.264 |
| point | revision_dfm_kalman_em | exact | pre_third | T | 0.000 | 1.000 | 0.179 | 0.246 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 0.000 | 1.000 | 0.172 | 0.375 |
| point | revision_dfm_kalman_em | pseudo | pre_advance | A | 0.000 | 1.000 | 0.185 | 0.368 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | S | 0.000 | 1.000 | 0.172 | 0.175 |
| point | revision_dfm_kalman_em | pseudo | pre_second | S | 0.000 | 1.000 | 0.179 | 0.139 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | T | 0.000 | 1.000 | 0.172 | 0.263 |
| point | revision_dfm_kalman_em | pseudo | pre_third | T | 0.000 | 1.000 | 0.179 | 0.245 |

## Headline Point Forecast Winners

| timing_mode | checkpoint_id | target_id | best_models | best_RMSE | best_MAE | best_bias | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | A | ar | 0.289 | 0.287 | -0.035 | 2 |
| exact | pre_second | S | no_revision | 0.067 | 0.051 | -0.051 | 2 |
| exact | pre_third | T | release_dfm | 0.105 | 0.090 | -0.090 | 2 |
| pseudo | pre_advance | A | ar | 0.289 | 0.287 | -0.035 | 2 |
| pseudo | pre_second | S | no_revision | 0.067 | 0.051 | -0.051 | 2 |
| pseudo | pre_third | T | release_dfm | 0.105 | 0.090 | -0.090 | 2 |

Main reading:

- The advance checkpoint should be read as a monthly-information problem: bridge/MIDAS/DFM-style monthly predictors are the relevant benchmark family before any same-quarter GDP estimate is observed.
- The second and third checkpoints should be read against the no-revision benchmark. If no-revision wins, that is a substantive empirical result: official early GDP estimates are hard to improve on in point RMSE.
- State-space value should be evaluated through the full evidence package: uncertainty calibration, mature-target robustness, revision-risk diagnostics, and mechanism tables, not only the winner table.

## Headline Revision Forecast Winners

| timing_mode | checkpoint_id | revision_target_id | best_models | best_RMSE | best_MAE | best_bias | best_sign_accuracy | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | DELTA_SA | bridge | 0.052 | 0.043 | 0.030 | 1.000 | 2 |
| exact | pre_second | DELTA_TS | ar | 0.122 | 0.098 | -0.098 | 1.000 | 2 |
| exact | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.464 | 0.433 | 0.165 | 0.000 | 2 |
| pseudo | pre_advance | DELTA_SA | bridge | 0.052 | 0.044 | 0.028 | 1.000 | 2 |
| pseudo | pre_second | DELTA_TS | ar | 0.122 | 0.098 | -0.098 | 1.000 | 2 |
| pseudo | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.464 | 0.433 | 0.165 | 0.000 | 2 |

Revision interpretation:

- No-revision is the primary benchmark for adjacent GDP revisions because many realized revisions are small and the zero-revision forecast is hard to beat.
- Sign accuracy should be interpreted with thresholded diagnostics; near-zero revisions can make raw direction accuracy look weak even when magnitude forecasts are useful.

## Exact Versus Pseudo Timing

| model_id | checkpoint_id | target_id | exact | pseudo | exact_minus_pseudo_RMSE |
| --- | --- | --- | --- | --- | --- |
| ar | pre_advance | A | 0.289 | 0.289 | 0.000 |
| ar | pre_second | S | 0.242 | 0.242 | 0.000 |
| ar | pre_third | T | 0.328 | 0.328 | 0.000 |
| bridge | pre_advance | A | 0.345 | 0.362 | -0.016 |
| bridge | pre_second | S | 0.219 | 0.302 | -0.082 |
| bridge | pre_third | T | 0.500 | 0.494 | 0.006 |
| indicator_revision_only_dfm_kalman_em | pre_advance | A | 0.354 | 0.351 | 0.003 |
| indicator_revision_only_dfm_kalman_em | pre_second | S | 0.168 | 0.169 | -0.000 |
| indicator_revision_only_dfm_kalman_em | pre_third | T | 0.278 | 0.278 | 0.001 |
| joint_indicator_revision_dfm_full_kalman_em | pre_advance | A | 0.382 | 0.375 | 0.007 |
| joint_indicator_revision_dfm_full_kalman_em | pre_second | S | 0.175 | 0.175 | -0.001 |
| joint_indicator_revision_dfm_full_kalman_em | pre_third | T | 0.264 | 0.263 | 0.001 |
| midas_umidas | pre_advance | A | 1.324 | 1.371 | -0.046 |
| midas_umidas | pre_second | S | 1.277 | 1.314 | -0.037 |
| midas_umidas | pre_third | T | 1.085 | 1.089 | -0.005 |
| monthly_mixed_frequency_kalman_em | pre_advance | A | 0.400 | 0.398 | 0.002 |
| monthly_mixed_frequency_kalman_em | pre_second | S | 0.129 | 0.128 | 0.001 |
| monthly_mixed_frequency_kalman_em | pre_third | T | 0.294 | 0.292 | 0.001 |
| no_revision | pre_advance | A | 0.320 | 0.320 | 0.000 |
| no_revision | pre_second | S | 0.067 | 0.067 | 0.000 |
| no_revision | pre_third | T | 0.185 | 0.185 | 0.000 |
| release_dfm | pre_advance | A | 0.686 | 0.675 | 0.011 |
| release_dfm | pre_second | S | 0.081 | 0.081 | -0.000 |
| release_dfm | pre_third | T | 0.105 | 0.105 | -0.000 |
| revision_dfm_kalman_em | pre_advance | A | 0.365 | 0.368 | -0.002 |
| revision_dfm_kalman_em | pre_second | S | 0.142 | 0.139 | 0.003 |
| revision_dfm_kalman_em | pre_third | T | 0.246 | 0.245 | 0.001 |
| spf | pre_advance | A | 0.718 | 0.718 | 0.000 |
| spf | pre_second | S | 0.749 | 0.749 | 0.000 |
| spf | pre_third | T | 0.934 | 0.934 | 0.000 |
| standard_dfm | pre_advance | A | 0.686 | 0.675 | 0.011 |
| standard_dfm | pre_second | S | 0.457 | 0.480 | -0.023 |
| standard_dfm | pre_third | T | 0.663 | 0.653 | 0.010 |

Negative exact-minus-pseudo values mean exact event timing lowers RMSE. Positive values mean pseudo timing has lower RMSE in that cell.

Revision timing gaps:

| model_id | checkpoint_id | revision_target_id | exact | pseudo | exact_minus_pseudo_RMSE |
| --- | --- | --- | --- | --- | --- |
| ar | pre_advance | DELTA_SA | 0.061 | 0.061 | 0.000 |
| ar | pre_second | DELTA_TS | 0.122 | 0.122 | 0.000 |
| ar | pre_third | DELTA_MT | 0.661 | 0.661 | 0.000 |
| bridge | pre_advance | DELTA_SA | 0.052 | 0.052 | 0.000 |
| bridge | pre_second | DELTA_TS | 0.169 | 0.176 | -0.007 |
| bridge | pre_third | DELTA_MT | 0.515 | 0.519 | -0.004 |
| indicator_revision_only_dfm_kalman_em | pre_advance | DELTA_SA | 0.067 | 0.067 | 0.000 |
| indicator_revision_only_dfm_kalman_em | pre_second | DELTA_TS | 0.185 | 0.185 | 0.000 |
| indicator_revision_only_dfm_kalman_em | pre_third | DELTA_MT | 0.464 | 0.464 | 0.000 |
| joint_indicator_revision_dfm_full_kalman_em | pre_advance | DELTA_SA | 0.076 | 0.074 | 0.002 |
| joint_indicator_revision_dfm_full_kalman_em | pre_second | DELTA_TS | 0.184 | 0.184 | -0.000 |
| joint_indicator_revision_dfm_full_kalman_em | pre_third | DELTA_MT | 0.499 | 0.499 | -0.000 |
| midas_umidas | pre_advance | DELTA_SA | 0.962 | 0.962 | -0.001 |
| midas_umidas | pre_second | DELTA_TS | 0.638 | 0.658 | -0.020 |
| midas_umidas | pre_third | DELTA_MT | 4.458 | 4.453 | 0.005 |
| monthly_mixed_frequency_kalman_em | pre_advance | DELTA_SA | 0.054 | 0.054 | 0.000 |
| monthly_mixed_frequency_kalman_em | pre_second | DELTA_TS | 0.186 | 0.186 | 0.000 |
| monthly_mixed_frequency_kalman_em | pre_third | DELTA_MT | 0.501 | 0.501 | 0.001 |
| no_revision | pre_advance | DELTA_SA | 0.067 | 0.067 | 0.000 |
| no_revision | pre_second | DELTA_TS | 0.185 | 0.185 | 0.000 |
| no_revision | pre_third | DELTA_MT | 0.464 | 0.464 | 0.000 |
| release_dfm | pre_advance | DELTA_SA | 0.059 | 0.059 | -0.000 |
| release_dfm | pre_second | DELTA_TS | 0.138 | 0.138 | 0.000 |
| release_dfm | pre_third | DELTA_MT | 0.644 | 0.642 | 0.003 |
| revision_dfm_kalman_em | pre_advance | DELTA_SA | 0.074 | 0.074 | 0.000 |
| revision_dfm_kalman_em | pre_second | DELTA_TS | 0.184 | 0.184 | -0.000 |
| revision_dfm_kalman_em | pre_third | DELTA_MT | 0.505 | 0.505 | -0.000 |
| spf | pre_advance | DELTA_SA | 0.067 | 0.067 | 0.000 |
| spf | pre_second | DELTA_TS | 0.185 | 0.185 | 0.000 |
| spf | pre_third | DELTA_MT | 0.464 | 0.464 | 0.000 |
| standard_dfm | pre_advance | DELTA_SA | 0.059 | 0.059 | -0.000 |
| standard_dfm | pre_second | DELTA_TS | 0.125 | 0.125 | -0.000 |
| standard_dfm | pre_third | DELTA_MT | 0.647 | 0.647 | -0.000 |

## Robustness Winners

| subsample | timing_mode | checkpoint_id | target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- |
| full_sample | exact | pre_advance | A | ar | 0.289 | 2 |
| full_sample | exact | pre_second | S | no_revision | 0.067 | 2 |
| full_sample | exact | pre_third | T | release_dfm | 0.105 | 2 |
| full_sample | pseudo | pre_advance | A | ar | 0.289 | 2 |
| full_sample | pseudo | pre_second | S | no_revision | 0.067 | 2 |
| full_sample | pseudo | pre_third | T | release_dfm | 0.105 | 2 |
| exclude_pandemic | exact | pre_advance | A | ar | 0.289 | 2 |
| exclude_pandemic | exact | pre_second | S | no_revision | 0.067 | 2 |
| exclude_pandemic | exact | pre_third | T | release_dfm | 0.105 | 2 |
| exclude_pandemic | pseudo | pre_advance | A | ar | 0.289 | 2 |
| exclude_pandemic | pseudo | pre_second | S | no_revision | 0.067 | 2 |
| exclude_pandemic | pseudo | pre_third | T | release_dfm | 0.105 | 2 |
| post_pandemic | exact | pre_advance | A | ar | 0.289 | 2 |
| post_pandemic | exact | pre_second | S | no_revision | 0.067 | 2 |
| post_pandemic | exact | pre_third | T | release_dfm | 0.105 | 2 |
| post_pandemic | pseudo | pre_advance | A | ar | 0.289 | 2 |
| post_pandemic | pseudo | pre_second | S | no_revision | 0.067 | 2 |
| post_pandemic | pseudo | pre_third | T | release_dfm | 0.105 | 2 |

Revision robustness winners:

| subsample | timing_mode | checkpoint_id | revision_target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- |
| full_sample | exact | pre_advance | DELTA_SA | bridge | 0.052 | 2 |
| full_sample | exact | pre_second | DELTA_TS | ar | 0.122 | 2 |
| full_sample | exact | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.464 | 2 |
| full_sample | pseudo | pre_advance | DELTA_SA | bridge | 0.052 | 2 |
| full_sample | pseudo | pre_second | DELTA_TS | ar | 0.122 | 2 |
| full_sample | pseudo | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.464 | 2 |
| exclude_pandemic | exact | pre_advance | DELTA_SA | bridge | 0.052 | 2 |
| exclude_pandemic | exact | pre_second | DELTA_TS | ar | 0.122 | 2 |
| exclude_pandemic | exact | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.464 | 2 |
| exclude_pandemic | pseudo | pre_advance | DELTA_SA | bridge | 0.052 | 2 |
| exclude_pandemic | pseudo | pre_second | DELTA_TS | ar | 0.122 | 2 |
| exclude_pandemic | pseudo | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.464 | 2 |
| post_pandemic | exact | pre_advance | DELTA_SA | bridge | 0.052 | 2 |
| post_pandemic | exact | pre_second | DELTA_TS | ar | 0.122 | 2 |
| post_pandemic | exact | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.464 | 2 |
| post_pandemic | pseudo | pre_advance | DELTA_SA | bridge | 0.052 | 2 |
| post_pandemic | pseudo | pre_second | DELTA_TS | ar | 0.122 | 2 |
| post_pandemic | pseudo | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.464 | 2 |

## Suggested Report Claim

A defensible Q1-style claim from this build is: real-time GDP nowcasting under a release ladder is best understood as a timing- and target-dependent forecast problem. Before the advance release, monthly information dominates. Before second and third releases, no-revision is a hard benchmark, so the contribution of release-ladder state-space modeling must be shown through uncertainty, revision-risk, mature-target robustness, and mechanism evidence as well as point accuracy.

## Reporting Cautions

- Do not mix these full state-space outputs with older frozen outputs unless the table explicitly labels the build.
- If the paper claims full Kalman/EM estimation, cite the files in this package and the exact/pseudo backtest outputs, not the older factor-regression-only report.
- The current generated package is traceable to forecast CSVs, but model selection should still be described as out-of-sample RMSE ranking rather than proof of universal dominance.
- One S-release quarter has incomplete RTDSM target coverage in the current data, so S and DELTA_SA/DELTA_TS headline cells have 79 forecasts rather than 80.

## Quick Narrative Anchors

Exact headline winners:

| checkpoint_id | target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- |
| pre_advance | A | ar | 0.289 | 2 |
| pre_second | S | no_revision | 0.067 | 2 |
| pre_third | T | release_dfm | 0.105 | 2 |

Pseudo headline winners:

| checkpoint_id | target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- |
| pre_advance | A | ar | 0.289 | 2 |
| pre_second | S | no_revision | 0.067 | 2 |
| pre_third | T | release_dfm | 0.105 | 2 |

## Figures

- `figures/point_rmse_by_model_exact.png`
- `figures/point_rmse_by_model_pseudo.png`
- `figures/revision_rmse_by_model_exact.png`
- `figures/exact_minus_pseudo_point_gaps.png`
