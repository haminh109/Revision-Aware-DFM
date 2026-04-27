# Journal Results Draft

Generated UTC: `2026-04-26T11:08:17+00:00`

Source output directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/sensitivity_exclude_covid_max_iter2`

Report package directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/sensitivity_exclude_covid_max_iter2_report_package`

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
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 0.000 | 2.000 | 0.080 | 0.518 |
| point | revision_dfm_kalman_em | exact | pre_advance | A | 0.000 | 2.000 | 0.123 | 0.511 |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 0.000 | 2.000 | 0.081 | 0.408 |
| point | revision_dfm_kalman_em | exact | pre_second | S | 0.000 | 2.000 | 0.126 | 0.383 |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 0.000 | 2.000 | 0.079 | 0.244 |
| point | revision_dfm_kalman_em | exact | pre_third | T | 0.000 | 2.000 | 0.123 | 0.225 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 0.000 | 2.000 | 0.080 | 0.505 |
| point | revision_dfm_kalman_em | pseudo | pre_advance | A | 0.000 | 2.000 | 0.123 | 0.481 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | S | 0.000 | 2.000 | 0.081 | 0.408 |
| point | revision_dfm_kalman_em | pseudo | pre_second | S | 0.000 | 2.000 | 0.126 | 0.382 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | T | 0.000 | 2.000 | 0.079 | 0.246 |
| point | revision_dfm_kalman_em | pseudo | pre_third | T | 0.000 | 2.000 | 0.123 | 0.228 |

## Headline Point Forecast Winners

| timing_mode | checkpoint_id | target_id | best_models | best_RMSE | best_MAE | best_bias | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.325 | 0.291 | -0.092 | 4 |
| exact | pre_second | S | bridge | 0.159 | 0.118 | -0.090 | 4 |
| exact | pre_third | T | release_dfm | 0.076 | 0.054 | -0.037 | 4 |
| pseudo | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.340 | 0.308 | -0.113 | 4 |
| pseudo | pre_second | S | no_revision | 0.185 | 0.139 | 0.032 | 4 |
| pseudo | pre_third | T | release_dfm | 0.076 | 0.054 | -0.038 | 4 |

Main reading:

- The advance checkpoint should be read as a monthly-information problem: bridge/MIDAS/DFM-style monthly predictors are the relevant benchmark family before any same-quarter GDP estimate is observed.
- The second and third checkpoints should be read against the no-revision benchmark. If no-revision wins, that is a substantive empirical result: official early GDP estimates are hard to improve on in point RMSE.
- State-space value should be evaluated through the full evidence package: uncertainty calibration, mature-target robustness, revision-risk diagnostics, and mechanism tables, not only the winner table.

## Headline Revision Forecast Winners

| timing_mode | checkpoint_id | revision_target_id | best_models | best_RMSE | best_MAE | best_bias | best_sign_accuracy | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | DELTA_SA | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.185 | 0.139 | 0.032 | 0.000 | 4 |
| exact | pre_second | DELTA_TS | ar | 0.098 | 0.080 | -0.060 | 1.000 | 4 |
| exact | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.527 | 0.509 | 0.075 | 0.000 | 4 |
| pseudo | pre_advance | DELTA_SA | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.185 | 0.139 | 0.032 | 0.000 | 4 |
| pseudo | pre_second | DELTA_TS | ar | 0.098 | 0.080 | -0.060 | 1.000 | 4 |
| pseudo | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.527 | 0.509 | 0.075 | 0.000 | 4 |

Revision interpretation:

- No-revision is the primary benchmark for adjacent GDP revisions because many realized revisions are small and the zero-revision forecast is hard to beat.
- Sign accuracy should be interpreted with thresholded diagnostics; near-zero revisions can make raw direction accuracy look weak even when magnitude forecasts are useful.

## Exact Versus Pseudo Timing

| model_id | checkpoint_id | target_id | exact | pseudo | exact_minus_pseudo_RMSE |
| --- | --- | --- | --- | --- | --- |
| ar | pre_advance | A | 0.545 | 0.545 | 0.000 |
| ar | pre_second | S | 0.738 | 0.738 | 0.000 |
| ar | pre_third | T | 0.711 | 0.711 | 0.000 |
| bridge | pre_advance | A | 0.531 | 0.505 | 0.026 |
| bridge | pre_second | S | 0.159 | 0.228 | -0.070 |
| bridge | pre_third | T | 0.451 | 0.403 | 0.048 |
| indicator_revision_only_dfm_kalman_em | pre_advance | A | 0.531 | 0.524 | 0.007 |
| indicator_revision_only_dfm_kalman_em | pre_second | S | 0.328 | 0.328 | 0.000 |
| indicator_revision_only_dfm_kalman_em | pre_third | T | 0.235 | 0.236 | -0.001 |
| joint_indicator_revision_dfm_full_kalman_em | pre_advance | A | 0.518 | 0.505 | 0.013 |
| joint_indicator_revision_dfm_full_kalman_em | pre_second | S | 0.408 | 0.408 | 0.000 |
| joint_indicator_revision_dfm_full_kalman_em | pre_third | T | 0.244 | 0.246 | -0.002 |
| midas_umidas | pre_advance | A | 1.688 | 1.689 | -0.002 |
| midas_umidas | pre_second | S | 0.921 | 0.948 | -0.027 |
| midas_umidas | pre_third | T | 0.905 | 0.877 | 0.027 |
| monthly_mixed_frequency_kalman_em | pre_advance | A | 0.325 | 0.340 | -0.015 |
| monthly_mixed_frequency_kalman_em | pre_second | S | 0.341 | 0.338 | 0.003 |
| monthly_mixed_frequency_kalman_em | pre_third | T | 0.327 | 0.325 | 0.002 |
| no_revision | pre_advance | A | 0.600 | 0.600 | 0.000 |
| no_revision | pre_second | S | 0.185 | 0.185 | 0.000 |
| no_revision | pre_third | T | 0.154 | 0.154 | 0.000 |
| release_dfm | pre_advance | A | 0.585 | 0.567 | 0.018 |
| release_dfm | pre_second | S | 0.237 | 0.238 | -0.000 |
| release_dfm | pre_third | T | 0.076 | 0.076 | 0.000 |
| revision_dfm_kalman_em | pre_advance | A | 0.511 | 0.481 | 0.030 |
| revision_dfm_kalman_em | pre_second | S | 0.383 | 0.382 | 0.001 |
| revision_dfm_kalman_em | pre_third | T | 0.225 | 0.228 | -0.003 |
| spf | pre_advance | A | 0.703 | 0.703 | 0.000 |
| spf | pre_second | S | 0.825 | 0.825 | 0.000 |
| spf | pre_third | T | 0.891 | 0.891 | 0.000 |
| standard_dfm | pre_advance | A | 0.585 | 0.567 | 0.018 |
| standard_dfm | pre_second | S | 0.400 | 0.419 | -0.019 |
| standard_dfm | pre_third | T | 0.566 | 0.529 | 0.036 |

Negative exact-minus-pseudo values mean exact event timing lowers RMSE. Positive values mean pseudo timing has lower RMSE in that cell.

Revision timing gaps:

| model_id | checkpoint_id | revision_target_id | exact | pseudo | exact_minus_pseudo_RMSE |
| --- | --- | --- | --- | --- | --- |
| ar | pre_advance | DELTA_SA | 0.223 | 0.223 | 0.000 |
| ar | pre_second | DELTA_TS | 0.098 | 0.098 | 0.000 |
| ar | pre_third | DELTA_MT | 0.630 | 0.630 | 0.000 |
| bridge | pre_advance | DELTA_SA | 0.196 | 0.204 | -0.007 |
| bridge | pre_second | DELTA_TS | 0.204 | 0.210 | -0.006 |
| bridge | pre_third | DELTA_MT | 0.555 | 0.560 | -0.004 |
| indicator_revision_only_dfm_kalman_em | pre_advance | DELTA_SA | 0.185 | 0.185 | 0.000 |
| indicator_revision_only_dfm_kalman_em | pre_second | DELTA_TS | 0.154 | 0.154 | 0.000 |
| indicator_revision_only_dfm_kalman_em | pre_third | DELTA_MT | 0.527 | 0.527 | 0.000 |
| joint_indicator_revision_dfm_full_kalman_em | pre_advance | DELTA_SA | 0.310 | 0.307 | 0.003 |
| joint_indicator_revision_dfm_full_kalman_em | pre_second | DELTA_TS | 0.154 | 0.154 | -0.000 |
| joint_indicator_revision_dfm_full_kalman_em | pre_third | DELTA_MT | 0.573 | 0.573 | -0.000 |
| midas_umidas | pre_advance | DELTA_SA | 0.680 | 0.681 | -0.001 |
| midas_umidas | pre_second | DELTA_TS | 0.471 | 0.481 | -0.010 |
| midas_umidas | pre_third | DELTA_MT | 3.290 | 3.371 | -0.080 |
| monthly_mixed_frequency_kalman_em | pre_advance | DELTA_SA | 0.239 | 0.239 | 0.000 |
| monthly_mixed_frequency_kalman_em | pre_second | DELTA_TS | 0.150 | 0.150 | 0.000 |
| monthly_mixed_frequency_kalman_em | pre_third | DELTA_MT | 0.592 | 0.591 | 0.002 |
| no_revision | pre_advance | DELTA_SA | 0.185 | 0.185 | 0.000 |
| no_revision | pre_second | DELTA_TS | 0.154 | 0.154 | 0.000 |
| no_revision | pre_third | DELTA_MT | 0.527 | 0.527 | 0.000 |
| release_dfm | pre_advance | DELTA_SA | 0.222 | 0.222 | -0.000 |
| release_dfm | pre_second | DELTA_TS | 0.113 | 0.113 | 0.000 |
| release_dfm | pre_third | DELTA_MT | 0.648 | 0.645 | 0.002 |
| revision_dfm_kalman_em | pre_advance | DELTA_SA | 0.320 | 0.318 | 0.003 |
| revision_dfm_kalman_em | pre_second | DELTA_TS | 0.154 | 0.154 | -0.000 |
| revision_dfm_kalman_em | pre_third | DELTA_MT | 0.574 | 0.574 | -0.000 |
| spf | pre_advance | DELTA_SA | 0.185 | 0.185 | 0.000 |
| spf | pre_second | DELTA_TS | 0.154 | 0.154 | 0.000 |
| spf | pre_third | DELTA_MT | 0.527 | 0.527 | 0.000 |
| standard_dfm | pre_advance | DELTA_SA | 0.222 | 0.222 | -0.000 |
| standard_dfm | pre_second | DELTA_TS | 0.102 | 0.103 | -0.000 |
| standard_dfm | pre_third | DELTA_MT | 0.655 | 0.654 | 0.001 |

## Robustness Winners

| subsample | timing_mode | checkpoint_id | target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- |
| full_sample | exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.325 | 4 |
| full_sample | exact | pre_second | S | bridge | 0.159 | 4 |
| full_sample | exact | pre_third | T | release_dfm | 0.076 | 4 |
| full_sample | pseudo | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.340 | 4 |
| full_sample | pseudo | pre_second | S | no_revision | 0.185 | 4 |
| full_sample | pseudo | pre_third | T | release_dfm | 0.076 | 4 |
| exclude_pandemic | exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.325 | 4 |
| exclude_pandemic | exact | pre_second | S | bridge | 0.159 | 4 |
| exclude_pandemic | exact | pre_third | T | release_dfm | 0.076 | 4 |
| exclude_pandemic | pseudo | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.340 | 4 |
| exclude_pandemic | pseudo | pre_second | S | no_revision | 0.185 | 4 |
| exclude_pandemic | pseudo | pre_third | T | release_dfm | 0.076 | 4 |
| post_pandemic | exact | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.325 | 4 |
| post_pandemic | exact | pre_second | S | bridge | 0.159 | 4 |
| post_pandemic | exact | pre_third | T | release_dfm | 0.076 | 4 |
| post_pandemic | pseudo | pre_advance | A | monthly_mixed_frequency_kalman_em | 0.340 | 4 |
| post_pandemic | pseudo | pre_second | S | no_revision | 0.185 | 4 |
| post_pandemic | pseudo | pre_third | T | release_dfm | 0.076 | 4 |

Revision robustness winners:

| subsample | timing_mode | checkpoint_id | revision_target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- |
| full_sample | exact | pre_advance | DELTA_SA | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.185 | 4 |
| full_sample | exact | pre_second | DELTA_TS | ar | 0.098 | 4 |
| full_sample | exact | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.527 | 4 |
| full_sample | pseudo | pre_advance | DELTA_SA | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.185 | 4 |
| full_sample | pseudo | pre_second | DELTA_TS | ar | 0.098 | 4 |
| full_sample | pseudo | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.527 | 4 |
| exclude_pandemic | exact | pre_advance | DELTA_SA | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.185 | 4 |
| exclude_pandemic | exact | pre_second | DELTA_TS | ar | 0.098 | 4 |
| exclude_pandemic | exact | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.527 | 4 |
| exclude_pandemic | pseudo | pre_advance | DELTA_SA | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.185 | 4 |
| exclude_pandemic | pseudo | pre_second | DELTA_TS | ar | 0.098 | 4 |
| exclude_pandemic | pseudo | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.527 | 4 |
| post_pandemic | exact | pre_advance | DELTA_SA | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.185 | 4 |
| post_pandemic | exact | pre_second | DELTA_TS | ar | 0.098 | 4 |
| post_pandemic | exact | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.527 | 4 |
| post_pandemic | pseudo | pre_advance | DELTA_SA | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.185 | 4 |
| post_pandemic | pseudo | pre_second | DELTA_TS | ar | 0.098 | 4 |
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
| pre_advance | A | monthly_mixed_frequency_kalman_em | 0.325 | 4 |
| pre_second | S | bridge | 0.159 | 4 |
| pre_third | T | release_dfm | 0.076 | 4 |

Pseudo headline winners:

| checkpoint_id | target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- |
| pre_advance | A | monthly_mixed_frequency_kalman_em | 0.340 | 4 |
| pre_second | S | no_revision | 0.185 | 4 |
| pre_third | T | release_dfm | 0.076 | 4 |

## Figures

- `figures/point_rmse_by_model_exact.png`
- `figures/point_rmse_by_model_pseudo.png`
- `figures/revision_rmse_by_model_exact.png`
- `figures/exact_minus_pseudo_point_gaps.png`
