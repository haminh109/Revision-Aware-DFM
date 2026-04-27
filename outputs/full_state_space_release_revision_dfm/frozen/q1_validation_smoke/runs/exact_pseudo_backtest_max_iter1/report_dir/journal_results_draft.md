# Journal Results Draft

Generated UTC: `2026-04-26T11:09:39+00:00`

Source output directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/exact_pseudo_backtest_max_iter1`

Report package directory: `/Users/haaminh109/Desktop/Minh/Tài liệu học tập (DSEB)/Kì 6/Time Series/RADFM/paper_project/outputs/full_state_space_release_revision_dfm/exact_pseudo_backtest_max_iter1_report_package`

## Data Coverage

- Point forecast rows: `66`.
- Revision forecast rows: `66`.
- Failure rows: `0`.
- GDP release calendar rows: `960`.
- Bias convention: `forecast_error = forecast_value - realized_value`; all bias values are mean forecast errors under this convention.
- The headline 2005Q1--2024Q4 A/S/T GDP calendar is derived from ALFRED `GDPC1` vintage dates when available; fallback rows are documented in the calendar file.

## Estimation Diagnostics

Kalman/EM rows report `convergence_rate`, `mean_iterations`, and relative final log-likelihood improvement. Mixed-frequency rows also carry numerical guard counts in the forecast-level CSV when a finite fallback is used. For a journal version, report these diagnostics next to the headline evidence rather than treating the estimator as a black box.

| table | model_id | timing_mode | checkpoint_id | outcome_id | convergence_rate | mean_iterations | median_llf_relative_last_improvement | RMSE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 0.000 | 1.000 | 0.172 | 0.254 |
| point | revision_dfm_kalman_em | exact | pre_advance | A | 0.000 | 1.000 | 0.185 | 0.351 |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 0.000 | 1.000 | 0.172 | 0.168 |
| point | revision_dfm_kalman_em | exact | pre_second | S | 0.000 | 1.000 | 0.173 | 0.169 |
| point | joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 0.000 | 1.000 | 0.172 | 0.023 |
| point | revision_dfm_kalman_em | exact | pre_third | T | 0.000 | 1.000 | 0.185 | 0.070 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 0.000 | 1.000 | 0.172 | 0.260 |
| point | revision_dfm_kalman_em | pseudo | pre_advance | A | 0.000 | 1.000 | 0.185 | 0.359 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | S | 0.000 | 1.000 | 0.172 | 0.168 |
| point | revision_dfm_kalman_em | pseudo | pre_second | S | 0.000 | 1.000 | 0.173 | 0.168 |
| point | joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | T | 0.000 | 1.000 | 0.172 | 0.022 |
| point | revision_dfm_kalman_em | pseudo | pre_third | T | 0.000 | 1.000 | 0.185 | 0.068 |

## Headline Point Forecast Winners

| timing_mode | checkpoint_id | target_id | best_models | best_RMSE | best_MAE | best_bias | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | A | midas_umidas | 0.102 | 0.102 | -0.102 | 1 |
| exact | pre_second | S | monthly_mixed_frequency_kalman_em | 0.010 | 0.010 | 0.010 | 1 |
| exact | pre_third | T | indicator_revision_only_dfm_kalman_em | 0.010 | 0.010 | -0.010 | 1 |
| pseudo | pre_advance | A | midas_umidas | 0.128 | 0.128 | -0.128 | 1 |
| pseudo | pre_second | S | monthly_mixed_frequency_kalman_em | 0.009 | 0.009 | 0.009 | 1 |
| pseudo | pre_third | T | indicator_revision_only_dfm_kalman_em | 0.011 | 0.011 | -0.011 | 1 |

Main reading:

- The advance checkpoint should be read as a monthly-information problem: bridge/MIDAS/DFM-style monthly predictors are the relevant benchmark family before any same-quarter GDP estimate is observed.
- The second and third checkpoints should be read against the no-revision benchmark. If no-revision wins, that is a substantive empirical result: official early GDP estimates are hard to improve on in point RMSE.
- State-space value should be evaluated through the full evidence package: uncertainty calibration, mature-target robustness, revision-risk diagnostics, and mechanism tables, not only the winner table.

## Headline Revision Forecast Winners

| timing_mode | checkpoint_id | revision_target_id | best_models | best_RMSE | best_MAE | best_bias | best_sign_accuracy | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exact | pre_advance | DELTA_SA | revision_dfm_kalman_em | 0.000 | 0.000 | -0.000 | 1.000 | 1 |
| exact | pre_second | DELTA_TS | ar | 0.025 | 0.025 | -0.025 | 1.000 | 1 |
| exact | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.599 | 0.599 | 0.599 | 0.000 | 1 |
| pseudo | pre_advance | DELTA_SA | joint_indicator_revision_dfm_full_kalman_em | 0.000 | 0.000 | -0.000 | 1.000 | 1 |
| pseudo | pre_second | DELTA_TS | bridge | 0.022 | 0.022 | 0.022 | 1.000 | 1 |
| pseudo | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.599 | 0.599 | 0.599 | 0.000 | 1 |

Revision interpretation:

- No-revision is the primary benchmark for adjacent GDP revisions because many realized revisions are small and the zero-revision forecast is hard to beat.
- Sign accuracy should be interpreted with thresholded diagnostics; near-zero revisions can make raw direction accuracy look weak even when magnitude forecasts are useful.

## Exact Versus Pseudo Timing

| model_id | checkpoint_id | target_id | exact | pseudo | exact_minus_pseudo_RMSE |
| --- | --- | --- | --- | --- | --- |
| ar | pre_advance | A | 0.252 | 0.252 | 0.000 |
| ar | pre_second | S | 0.246 | 0.246 | 0.000 |
| ar | pre_third | T | 0.222 | 0.222 | 0.000 |
| bridge | pre_advance | A | 0.253 | 0.330 | -0.077 |
| bridge | pre_second | S | 0.072 | 0.124 | -0.053 |
| bridge | pre_third | T | 0.045 | 0.013 | 0.033 |
| indicator_revision_only_dfm_kalman_em | pre_advance | A | 0.346 | 0.351 | -0.005 |
| indicator_revision_only_dfm_kalman_em | pre_second | S | 0.119 | 0.119 | -0.001 |
| indicator_revision_only_dfm_kalman_em | pre_third | T | 0.010 | 0.011 | -0.001 |
| joint_indicator_revision_dfm_full_kalman_em | pre_advance | A | 0.254 | 0.260 | -0.007 |
| joint_indicator_revision_dfm_full_kalman_em | pre_second | S | 0.168 | 0.168 | -0.000 |
| joint_indicator_revision_dfm_full_kalman_em | pre_third | T | 0.023 | 0.022 | 0.001 |
| midas_umidas | pre_advance | A | 0.102 | 0.128 | -0.027 |
| midas_umidas | pre_second | S | 1.793 | 1.847 | -0.054 |
| midas_umidas | pre_third | T | 1.455 | 1.459 | -0.004 |
| monthly_mixed_frequency_kalman_em | pre_advance | A | 0.498 | 0.492 | 0.006 |
| monthly_mixed_frequency_kalman_em | pre_second | S | 0.010 | 0.009 | 0.001 |
| monthly_mixed_frequency_kalman_em | pre_third | T | 0.117 | 0.111 | 0.005 |
| no_revision | pre_advance | A | 0.193 | 0.193 | 0.000 |
| no_revision | pre_second | S | 0.094 | 0.094 | 0.000 |
| no_revision | pre_third | T | 0.104 | 0.104 | 0.000 |
| release_dfm | pre_advance | A | 0.174 | 0.143 | 0.031 |
| release_dfm | pre_second | S | 0.015 | 0.016 | -0.000 |
| release_dfm | pre_third | T | 0.036 | 0.035 | 0.000 |
| revision_dfm_kalman_em | pre_advance | A | 0.351 | 0.359 | -0.008 |
| revision_dfm_kalman_em | pre_second | S | 0.169 | 0.168 | 0.000 |
| revision_dfm_kalman_em | pre_third | T | 0.070 | 0.068 | 0.002 |
| spf | pre_advance | A | 0.347 | 0.347 | 0.000 |
| spf | pre_second | S | 0.441 | 0.441 | 0.000 |
| spf | pre_third | T | 0.545 | 0.545 | 0.000 |
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
| joint_indicator_revision_dfm_full_kalman_em | pre_advance | DELTA_SA | 0.001 | 0.000 | 0.001 |
| joint_indicator_revision_dfm_full_kalman_em | pre_second | DELTA_TS | 0.104 | 0.104 | -0.000 |
| joint_indicator_revision_dfm_full_kalman_em | pre_third | DELTA_MT | 0.660 | 0.660 | -0.000 |
| midas_umidas | pre_advance | DELTA_SA | 1.279 | 1.283 | -0.004 |
| midas_umidas | pre_second | DELTA_TS | 0.871 | 0.899 | -0.028 |
| midas_umidas | pre_third | DELTA_MT | 5.944 | 5.954 | -0.010 |
| monthly_mixed_frequency_kalman_em | pre_advance | DELTA_SA | 0.075 | 0.075 | 0.000 |
| monthly_mixed_frequency_kalman_em | pre_second | DELTA_TS | 0.064 | 0.064 | 0.000 |
| monthly_mixed_frequency_kalman_em | pre_third | DELTA_MT | 0.649 | 0.648 | 0.001 |
| no_revision | pre_advance | DELTA_SA | 0.094 | 0.094 | 0.000 |
| no_revision | pre_second | DELTA_TS | 0.104 | 0.104 | 0.000 |
| no_revision | pre_third | DELTA_MT | 0.599 | 0.599 | 0.000 |
| release_dfm | pre_advance | DELTA_SA | 0.002 | 0.002 | 0.000 |
| release_dfm | pre_second | DELTA_TS | 0.054 | 0.054 | 0.000 |
| release_dfm | pre_third | DELTA_MT | 0.906 | 0.902 | 0.004 |
| revision_dfm_kalman_em | pre_advance | DELTA_SA | 0.000 | 0.002 | -0.001 |
| revision_dfm_kalman_em | pre_second | DELTA_TS | 0.104 | 0.104 | -0.000 |
| revision_dfm_kalman_em | pre_third | DELTA_MT | 0.669 | 0.669 | -0.000 |
| spf | pre_advance | DELTA_SA | 0.094 | 0.094 | 0.000 |
| spf | pre_second | DELTA_TS | 0.104 | 0.104 | 0.000 |
| spf | pre_third | DELTA_MT | 0.599 | 0.599 | 0.000 |
| standard_dfm | pre_advance | DELTA_SA | 0.002 | 0.002 | 0.000 |
| standard_dfm | pre_second | DELTA_TS | 0.037 | 0.037 | -0.000 |
| standard_dfm | pre_third | DELTA_MT | 0.913 | 0.913 | -0.000 |

## Robustness Winners

| subsample | timing_mode | checkpoint_id | target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- |
| full_sample | exact | pre_advance | A | midas_umidas | 0.102 | 1 |
| full_sample | exact | pre_second | S | monthly_mixed_frequency_kalman_em | 0.010 | 1 |
| full_sample | exact | pre_third | T | indicator_revision_only_dfm_kalman_em | 0.010 | 1 |
| full_sample | pseudo | pre_advance | A | midas_umidas | 0.128 | 1 |
| full_sample | pseudo | pre_second | S | monthly_mixed_frequency_kalman_em | 0.009 | 1 |
| full_sample | pseudo | pre_third | T | indicator_revision_only_dfm_kalman_em | 0.011 | 1 |
| exclude_pandemic | exact | pre_advance | A | midas_umidas | 0.102 | 1 |
| exclude_pandemic | exact | pre_second | S | monthly_mixed_frequency_kalman_em | 0.010 | 1 |
| exclude_pandemic | exact | pre_third | T | indicator_revision_only_dfm_kalman_em | 0.010 | 1 |
| exclude_pandemic | pseudo | pre_advance | A | midas_umidas | 0.128 | 1 |
| exclude_pandemic | pseudo | pre_second | S | monthly_mixed_frequency_kalman_em | 0.009 | 1 |
| exclude_pandemic | pseudo | pre_third | T | indicator_revision_only_dfm_kalman_em | 0.011 | 1 |
| post_pandemic | exact | pre_advance | A | midas_umidas | 0.102 | 1 |
| post_pandemic | exact | pre_second | S | monthly_mixed_frequency_kalman_em | 0.010 | 1 |
| post_pandemic | exact | pre_third | T | indicator_revision_only_dfm_kalman_em | 0.010 | 1 |
| post_pandemic | pseudo | pre_advance | A | midas_umidas | 0.128 | 1 |
| post_pandemic | pseudo | pre_second | S | monthly_mixed_frequency_kalman_em | 0.009 | 1 |
| post_pandemic | pseudo | pre_third | T | indicator_revision_only_dfm_kalman_em | 0.011 | 1 |

Revision robustness winners:

| subsample | timing_mode | checkpoint_id | revision_target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- | --- | --- |
| full_sample | exact | pre_advance | DELTA_SA | revision_dfm_kalman_em | 0.000 | 1 |
| full_sample | exact | pre_second | DELTA_TS | ar | 0.025 | 1 |
| full_sample | exact | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.599 | 1 |
| full_sample | pseudo | pre_advance | DELTA_SA | joint_indicator_revision_dfm_full_kalman_em | 0.000 | 1 |
| full_sample | pseudo | pre_second | DELTA_TS | bridge | 0.022 | 1 |
| full_sample | pseudo | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.599 | 1 |
| exclude_pandemic | exact | pre_advance | DELTA_SA | revision_dfm_kalman_em | 0.000 | 1 |
| exclude_pandemic | exact | pre_second | DELTA_TS | ar | 0.025 | 1 |
| exclude_pandemic | exact | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.599 | 1 |
| exclude_pandemic | pseudo | pre_advance | DELTA_SA | joint_indicator_revision_dfm_full_kalman_em | 0.000 | 1 |
| exclude_pandemic | pseudo | pre_second | DELTA_TS | bridge | 0.022 | 1 |
| exclude_pandemic | pseudo | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.599 | 1 |
| post_pandemic | exact | pre_advance | DELTA_SA | revision_dfm_kalman_em | 0.000 | 1 |
| post_pandemic | exact | pre_second | DELTA_TS | ar | 0.025 | 1 |
| post_pandemic | exact | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.599 | 1 |
| post_pandemic | pseudo | pre_advance | DELTA_SA | joint_indicator_revision_dfm_full_kalman_em | 0.000 | 1 |
| post_pandemic | pseudo | pre_second | DELTA_TS | bridge | 0.022 | 1 |
| post_pandemic | pseudo | pre_third | DELTA_MT | no_revision; spf; indicator_revision_only_dfm_kalman_em | 0.599 | 1 |

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
| pre_advance | A | midas_umidas | 0.102 | 1 |
| pre_second | S | monthly_mixed_frequency_kalman_em | 0.010 | 1 |
| pre_third | T | indicator_revision_only_dfm_kalman_em | 0.010 | 1 |

Pseudo headline winners:

| checkpoint_id | target_id | best_models | best_RMSE | best_n_forecasts |
| --- | --- | --- | --- | --- |
| pre_advance | A | midas_umidas | 0.128 | 1 |
| pre_second | S | monthly_mixed_frequency_kalman_em | 0.009 | 1 |
| pre_third | T | indicator_revision_only_dfm_kalman_em | 0.011 | 1 |

## Figures

- `figures/point_rmse_by_model_exact.png`
- `figures/point_rmse_by_model_pseudo.png`
- `figures/revision_rmse_by_model_exact.png`
- `figures/exact_minus_pseudo_point_gaps.png`
