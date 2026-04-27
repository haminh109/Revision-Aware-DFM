# Journal Results Draft

Generated UTC: `2026-04-26T11:07:07+00:00`

Source output directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/sensitivity_window_rolling_max_iter2`

Report package directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/sensitivity_window_rolling_max_iter2_report_package`

## Data Coverage

- Point forecast rows: `264`.
- Revision forecast rows: `264`.
- Failure rows: `0`.
- GDP release calendar rows: `960`.
- Bias convention: `forecast_error = forecast_value - realized_value`; all bias values are mean forecast errors under this convention.
- The headline 2005Q1--2024Q4 A/S/T GDP calendar is derived from ALFRED `GDPC1` vintage dates when available; fallback rows are documented in the calendar file.

## Estimation Diagnostics

Kalman/EM rows report `convergence_rate`, `mean_iterations`, and relative final log-likelihood improvement. Mixed-frequency rows also carry numerical guard counts in the forecast-level CSV when a finite fallback is used. For a journal version, report these diagnostics next to the headline evidence rather than treating the estimator as a black box.

| table | model_id | timing_mode | checkpoint_id | outcome_id | convergence_rate | mean_iterations | median_llf_relative_last_improvement | RMSE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 0.000 | 2.000 | 0.123 | 0.793 |
| point | revision_dfm_kalman_em | exact | pre_advance | A | 0.000 | 2.000 | 0.163 | 0.731 |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 0.000 | 2.000 | 0.125 | 0.474 |
| point | revision_dfm_kalman_em | exact | pre_second | S | 0.000 | 2.000 | 0.163 | 0.364 |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 0.000 | 2.000 | 0.124 | 0.417 |
| point | revision_dfm_kalman_em | exact | pre_third | T | 0.000 | 2.000 | 0.164 | 0.345 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 0.000 | 2.000 | 0.123 | 0.779 |
| point | revision_dfm_kalman_em | pseudo | pre_advance | A | 0.000 | 2.000 | 0.163 | 0.702 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | S | 0.000 | 2.000 | 0.125 | 0.473 |
| point | revision_dfm_kalman_em | pseudo | pre_second | S | 0.000 | 2.000 | 0.163 | 0.362 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | T | 0.000 | 2.000 | 0.124 | 0.418 |
| point | revision_dfm_kalman_em | pseudo | pre_third | T | 0.000 | 2.000 | 0.163 | 0.347 |

## Headline Point Forecast Winners

| timing_mode | checkpoint_id | target_id | best_models | best_RMSE | best_MAE | best_bias | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.537 | 0.461 | -0.461 | 4 |
| exact | pre_second | S | no_revision | 0.185 | 0.139 | 0.032 | 4 |
| exact | pre_third | T | no_revision | 0.154 | 0.136 | -0.136 | 4 |
| pseudo | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.541 | 0.471 | -0.471 | 4 |
| pseudo | pre_second | S | no_revision | 0.185 | 0.139 | 0.032 | 4 |
| pseudo | pre_third | T | no_revision | 0.154 | 0.136 | -0.136 | 4 |

Main reading:

- The advance checkpoint should be read as a monthly-information problem: bridge/MIDAS/DFM-style monthly predictors are the relevant benchmark family before any same-quarter GDP estimate is observed.
- The second and third checkpoints should be read against the no-revision benchmark. If no-revision wins, that is a substantive empirical result: official early GDP estimates are hard to improve on in point RMSE.
- State-space value should be evaluated through the full evidence package: uncertainty calibration, mature-target robustness, revision-risk diagnostics, and mechanism tables, not only the winner table.

## Headline Revision Forecast Winners

| timing_mode | checkpoint_id | revision_target_id | best_models | best_RMSE | best_MAE | best_bias | best_sign_accuracy | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | DELTA_SA | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.185 | 0.139 | 0.032 | 0.000 | 4 |
| exact | pre_second | DELTA_TS | standard_dfm | 0.074 | 0.064 | -0.019 | 1.000 | 4 |
| exact | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.527 | 0.509 | 0.075 | 0.000 | 4 |
| pseudo | pre_advance | DELTA_SA | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.185 | 0.139 | 0.032 | 0.000 | 4 |
| pseudo | pre_second | DELTA_TS | standard_dfm | 0.074 | 0.064 | -0.019 | 1.000 | 4 |
| pseudo | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.527 | 0.509 | 0.075 | 0.000 | 4 |

Revision interpretation:

- No-revision is the primary benchmark for adjacent GDP revisions because many realized revisions are small and the zero-revision forecast is hard to beat.
- Sign accuracy should be interpreted with thresholded diagnostics; near-zero revisions can make raw direction accuracy look weak even when magnitude forecasts are useful.

## Exact Versus Pseudo Timing

| model_id | checkpoint_id | target_id | exact | pseudo | exact_minus_pseudo_RMSE |
| --- | --- | --- | --- | --- | --- |
| ar | pre_advance | A | 0.911 | 0.911 | 0.000 |
| ar | pre_second | S | 0.749 | 0.749 | 0.000 |
| ar | pre_third | T | 0.585 | 0.585 | 0.000 |
| bridge | pre_advance | A | 1.110 | 1.050 | 0.060 |
| bridge | pre_second | S | 0.988 | 1.048 | -0.060 |
| bridge | pre_third | T | 1.141 | 1.106 | 0.035 |
| indicator_revision_only_dfm_kalman_em | pre_advance | A | 0.629 | 0.618 | 0.012 |
| indicator_revision_only_dfm_kalman_em | pre_second | S | 0.452 | 0.451 | 0.001 |
| indicator_revision_only_dfm_kalman_em | pre_third | T | 0.431 | 0.431 | -0.001 |
| joint_indicator_revision_dfm_full_kalman_em | pre_advance | A | 0.793 | 0.779 | 0.015 |
| joint_indicator_revision_dfm_full_kalman_em | pre_second | S | 0.474 | 0.473 | 0.001 |
| joint_indicator_revision_dfm_full_kalman_em | pre_third | T | 0.417 | 0.418 | -0.001 |
| midas_umidas | pre_advance | A | 1.501 | 1.412 | 0.088 |
| midas_umidas | pre_second | S | 0.336 | 0.326 | 0.010 |
| midas_umidas | pre_third | T | 0.521 | 0.521 | 0.000 |
| monthly_mixed_frequency_kalman_em | pre_advance | A | 0.537 | 0.541 | -0.004 |
| monthly_mixed_frequency_kalman_em | pre_second | S | 0.376 | 0.376 | -0.000 |
| monthly_mixed_frequency_kalman_em | pre_third | T | 0.398 | 0.399 | -0.001 |
| no_revision | pre_advance | A | 0.911 | 0.911 | 0.000 |
| no_revision | pre_second | S | 0.185 | 0.185 | 0.000 |
| no_revision | pre_third | T | 0.154 | 0.154 | 0.000 |
| release_dfm | pre_advance | A | 1.398 | 1.427 | -0.029 |
| release_dfm | pre_second | S | 0.257 | 0.258 | -0.000 |
| release_dfm | pre_third | T | 0.156 | 0.155 | 0.000 |
| revision_dfm_kalman_em | pre_advance | A | 0.731 | 0.702 | 0.029 |
| revision_dfm_kalman_em | pre_second | S | 0.364 | 0.362 | 0.002 |
| revision_dfm_kalman_em | pre_third | T | 0.345 | 0.347 | -0.002 |
| spf | pre_advance | A | 0.703 | 0.703 | 0.000 |
| spf | pre_second | S | 0.825 | 0.825 | 0.000 |
| spf | pre_third | T | 0.891 | 0.891 | 0.000 |
| standard_dfm | pre_advance | A | 1.398 | 1.427 | -0.029 |
| standard_dfm | pre_second | S | 1.378 | 1.406 | -0.028 |
| standard_dfm | pre_third | T | 1.475 | 1.421 | 0.054 |

Negative exact-minus-pseudo values mean exact event timing lowers RMSE. Positive values mean pseudo timing has lower RMSE in that cell.

Revision timing gaps:

| model_id | checkpoint_id | revision_target_id | exact | pseudo | exact_minus_pseudo_RMSE |
| --- | --- | --- | --- | --- | --- |
| ar | pre_advance | DELTA_SA | 0.276 | 0.276 | 0.000 |
| ar | pre_second | DELTA_TS | 0.429 | 0.429 | 0.000 |
| ar | pre_third | DELTA_MT | 23.127 | 23.127 | 0.000 |
| bridge | pre_advance | DELTA_SA | 0.251 | 0.260 | -0.009 |
| bridge | pre_second | DELTA_TS | 0.282 | 0.285 | -0.002 |
| bridge | pre_third | DELTA_MT | 1.329 | 1.325 | 0.004 |
| indicator_revision_only_dfm_kalman_em | pre_advance | DELTA_SA | 0.185 | 0.185 | 0.000 |
| indicator_revision_only_dfm_kalman_em | pre_second | DELTA_TS | 0.154 | 0.154 | 0.000 |
| indicator_revision_only_dfm_kalman_em | pre_third | DELTA_MT | 0.527 | 0.527 | 0.000 |
| joint_indicator_revision_dfm_full_kalman_em | pre_advance | DELTA_SA | 0.347 | 0.344 | 0.003 |
| joint_indicator_revision_dfm_full_kalman_em | pre_second | DELTA_TS | 0.153 | 0.153 | 0.000 |
| joint_indicator_revision_dfm_full_kalman_em | pre_third | DELTA_MT | 0.575 | 0.575 | 0.000 |
| midas_umidas | pre_advance | DELTA_SA | 0.887 | 0.844 | 0.043 |
| midas_umidas | pre_second | DELTA_TS | 0.555 | 0.556 | -0.001 |
| midas_umidas | pre_third | DELTA_MT | 1.846 | 1.803 | 0.042 |
| monthly_mixed_frequency_kalman_em | pre_advance | DELTA_SA | 0.235 | 0.235 | -0.000 |
| monthly_mixed_frequency_kalman_em | pre_second | DELTA_TS | 0.175 | 0.176 | -0.000 |
| monthly_mixed_frequency_kalman_em | pre_third | DELTA_MT | 0.571 | 0.571 | 0.001 |
| no_revision | pre_advance | DELTA_SA | 0.185 | 0.185 | 0.000 |
| no_revision | pre_second | DELTA_TS | 0.154 | 0.154 | 0.000 |
| no_revision | pre_third | DELTA_MT | 0.527 | 0.527 | 0.000 |
| release_dfm | pre_advance | DELTA_SA | 0.236 | 0.235 | 0.000 |
| release_dfm | pre_second | DELTA_TS | 0.092 | 0.092 | -0.000 |
| release_dfm | pre_third | DELTA_MT | 0.996 | 0.994 | 0.002 |
| revision_dfm_kalman_em | pre_advance | DELTA_SA | 0.348 | 0.344 | 0.004 |
| revision_dfm_kalman_em | pre_second | DELTA_TS | 0.154 | 0.154 | -0.000 |
| revision_dfm_kalman_em | pre_third | DELTA_MT | 0.573 | 0.573 | 0.000 |
| spf | pre_advance | DELTA_SA | 0.185 | 0.185 | 0.000 |
| spf | pre_second | DELTA_TS | 0.154 | 0.154 | 0.000 |
| spf | pre_third | DELTA_MT | 0.527 | 0.527 | 0.000 |
| standard_dfm | pre_advance | DELTA_SA | 0.236 | 0.235 | 0.000 |
| standard_dfm | pre_second | DELTA_TS | 0.074 | 0.074 | -0.000 |
| standard_dfm | pre_third | DELTA_MT | 0.728 | 0.723 | 0.005 |

## Robustness Winners

| subsample | timing_mode | checkpoint_id | target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- |
| full_sample | exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.537 | 4 |
| full_sample | exact | pre_second | S | no_revision | 0.185 | 4 |
| full_sample | exact | pre_third | T | no_revision | 0.154 | 4 |
| full_sample | pseudo | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.541 | 4 |
| full_sample | pseudo | pre_second | S | no_revision | 0.185 | 4 |
| full_sample | pseudo | pre_third | T | no_revision | 0.154 | 4 |
| exclude_pandemic | exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.537 | 4 |
| exclude_pandemic | exact | pre_second | S | no_revision | 0.185 | 4 |
| exclude_pandemic | exact | pre_third | T | no_revision | 0.154 | 4 |
| exclude_pandemic | pseudo | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.541 | 4 |
| exclude_pandemic | pseudo | pre_second | S | no_revision | 0.185 | 4 |
| exclude_pandemic | pseudo | pre_third | T | no_revision | 0.154 | 4 |
| post_pandemic | exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.537 | 4 |
| post_pandemic | exact | pre_second | S | no_revision | 0.185 | 4 |
| post_pandemic | exact | pre_third | T | no_revision | 0.154 | 4 |
| post_pandemic | pseudo | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.541 | 4 |
| post_pandemic | pseudo | pre_second | S | no_revision | 0.185 | 4 |
| post_pandemic | pseudo | pre_third | T | no_revision | 0.154 | 4 |

Revision robustness winners:

| subsample | timing_mode | checkpoint_id | revision_target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- |
| full_sample | exact | pre_advance | DELTA_SA | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.185 | 4 |
| full_sample | exact | pre_second | DELTA_TS | standard_dfm | 0.074 | 4 |
| full_sample | exact | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.527 | 4 |
| full_sample | pseudo | pre_advance | DELTA_SA | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.185 | 4 |
| full_sample | pseudo | pre_second | DELTA_TS | standard_dfm | 0.074 | 4 |
| full_sample | pseudo | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.527 | 4 |
| exclude_pandemic | exact | pre_advance | DELTA_SA | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.185 | 4 |
| exclude_pandemic | exact | pre_second | DELTA_TS | standard_dfm | 0.074 | 4 |
| exclude_pandemic | exact | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.527 | 4 |
| exclude_pandemic | pseudo | pre_advance | DELTA_SA | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.185 | 4 |
| exclude_pandemic | pseudo | pre_second | DELTA_TS | standard_dfm | 0.074 | 4 |
| exclude_pandemic | pseudo | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.527 | 4 |
| post_pandemic | exact | pre_advance | DELTA_SA | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.185 | 4 |
| post_pandemic | exact | pre_second | DELTA_TS | standard_dfm | 0.074 | 4 |
| post_pandemic | exact | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.527 | 4 |
| post_pandemic | pseudo | pre_advance | DELTA_SA | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.185 | 4 |
| post_pandemic | pseudo | pre_second | DELTA_TS | standard_dfm | 0.074 | 4 |
| post_pandemic | pseudo | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.527 | 4 |

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
| pre_advance | A | monthly_mixed_frequency_kalman_em | 0.537 | 4 |
| pre_second | S | no_revision | 0.185 | 4 |
| pre_third | T | no_revision | 0.154 | 4 |

Pseudo headline winners:

| checkpoint_id | target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- |
| pre_advance | A | monthly_mixed_frequency_kalman_em | 0.541 | 4 |
| pre_second | S | no_revision | 0.185 | 4 |
| pre_third | T | no_revision | 0.154 | 4 |

## Figures

- `figures/point_rmse_by_model_exact.png`
- `figures/point_rmse_by_model_pseudo.png`
- `figures/revision_rmse_by_model_exact.png`
- `figures/exact_minus_pseudo_point_gaps.png`
