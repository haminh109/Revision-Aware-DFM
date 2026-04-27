# Q1 Core Results Draft

Freeze: `outputs/full_state_space_release_revision_dfm/frozen/q1_manuscript_v1_core`

This draft uses only the frozen core run. Sensitivity runs are intentionally excluded and should be frozen separately.

## Acceptance Audit

The freeze is acceptable as the core manuscript evidence package.

- `FREEZE_FAILURE_AUDIT.csv`: all main and mature runs have `failure_rows = 0`.
- `STATE_SPACE_CONVERGENCE_MAIN_MAX_ITER100.csv`: all state-space models have `convergence_rate = 1.0` in the main max_iter=100 run.
- Compared with max_iter=50, max_iter=100 materially improves convergence. The monthly mixed-frequency Kalman model moves from a minimum convergence rate of 0.55 at max_iter=50 to 1.0 at max_iter=100.
- RMSE is stable between max_iter=50 and 100. For the monthly mixed-frequency Kalman model, mean RMSE changes by about `+0.00194` for point targets and `+0.00174` for revision targets, while convergence becomes complete.
- `STATE_SPACE_VARIANCE_POINT_MAIN_MAX_ITER100.csv`: monthly mixed-frequency Kalman has positive finite point forecast variances for all exact and pseudo checkpoint rows.
- `STATE_SPACE_COVARIANCE_SUMMARY_MAIN_MAX_ITER100.csv`: monthly mixed-frequency Kalman has `share_psd = 1.0`, zero matrix asymmetry, and positive minimum eigenvalues across all checkpoint and timing rows.
- SPF coverage is complete on the frozen common sample: point targets have 80, 79, and 80 forecasts for A, S, and T; revision targets have 79, 79, and 80 forecasts for DELTA_SA, DELTA_TS, and DELTA_MT.

Use `max_iter=100` as the headline run. Wording can safely say "Kalman/EM estimates with full convergence diagnostics" for the core run.

## Main Empirical Claim

The core result is not universal Kalman dominance. The evidence supports a stronger and more publishable Q1 claim:

Real-time GDP nowcasting under release ladders is dominated by different information sets at different stages. Before the advance release, professional forecast information is very strong. After the advance and second official GDP releases become known, the no-revision benchmark is hard to beat for point forecasts. State-space models add value mainly through density forecasts, revision-risk diagnostics, mature-target robustness, and mechanism evidence rather than through a simple winner table.

## Full-Sample Point Forecasts

Exact timing, max_iter=100:

| Checkpoint | Target | Best RMSE model | RMSE | MAE | Main interpretation |
|---|---:|---|---:|---:|---|
| pre_advance | A | SPF | 2.225 | 1.338 | External professional benchmark is strongest before the first GDP release. |
| pre_second | S | no_revision | 0.570 | 0.400 | The advance estimate is a very hard benchmark for the second release. |
| pre_third | T | no_revision | 0.362 | 0.240 | The second estimate is a very hard benchmark for the third release. |

Near-winners:

- At pre_advance, standard/release DFM has RMSE about `3.066`, and revision DFM Kalman has RMSE about `3.383`.
- At pre_second, the best state-space alternatives are close but do not beat no-revision: indicator-revision Kalman RMSE `0.591`, monthly mixed-frequency Kalman RMSE `0.595`.
- At pre_third, monthly mixed-frequency Kalman is very close to no-revision: RMSE `0.369` versus `0.362`.

Manuscript wording:

> The release ladder itself is a strong forecasting device. Once an official early GDP release is observed, a no-revision forecast is difficult to beat in point RMSE, especially for the second and third releases.

## Revision Forecasts

Exact timing, max_iter=100:

| Checkpoint | Revision target | Best RMSE model | RMSE | MAE | Interpretation |
|---|---:|---|---:|---:|---|
| pre_advance | DELTA_SA | no_revision / SPF / indicator-revision Kalman tie | 0.570 | 0.400 | Zero revision is hard to beat in magnitude. |
| pre_second | DELTA_TS | no_revision / SPF / indicator-revision Kalman tie | 0.361 | 0.238 | Zero revision remains hard to beat. |
| pre_third | DELTA_MT | no_revision / SPF / indicator-revision Kalman tie | 1.339 | 1.056 | Mature revisions are larger, but the zero-revision benchmark remains competitive. |

Directional revision evidence is different from magnitude evidence. The no-revision forecast has zero revision by construction and is not useful as a directional classifier. Among state-space models, sign accuracy is meaningful but mixed:

- DELTA_SA: monthly mixed-frequency Kalman sign accuracy `0.658`; revision DFM Kalman `0.658`.
- DELTA_TS: revision DFM Kalman `0.570`; monthly mixed-frequency Kalman `0.557`.
- DELTA_MT: revision DFM Kalman `0.463`; monthly mixed-frequency Kalman `0.388`.

Manuscript wording:

> Revision-aware state-space models produce nonzero revision-risk signals, but point-forecast RMSE confirms that the no-revision benchmark is a central empirical object rather than a weak strawman.

## Density Evidence

Density metrics give the state-space models a clearer role.

Point density CRPS winners under exact timing:

| Checkpoint | Target | Best density models | CRPS |
|---|---:|---|---:|
| pre_advance | A | SPF | 1.066 |
| pre_second | S | no_revision | 0.300 |
| pre_third | T | indicator-revision Kalman | 0.187 |

Revision density CRPS winners under exact timing:

| Checkpoint | Revision target | Best density models | CRPS |
|---|---:|---|---:|
| pre_advance | DELTA_SA | SPF / no_revision | 0.300 |
| pre_second | DELTA_TS | revision DFM Kalman | 0.184 |
| pre_third | DELTA_MT | no_revision / SPF | 0.752 |

This supports a Q1-style narrative: state-space structure is not always the lowest-RMSE point forecast, but it is useful for uncertainty quantification at specific release stages, especially around the third-release target and the second-to-third revision.

## Mature-Target Robustness

Mature robustness does not overturn the main point-forecast finding.

- For mature_1y, mature_3y, and mature_latest, point forecast winners remain SPF before advance and no-revision before second/third.
- For revision robustness, monthly mixed-frequency Kalman wins DELTA_SA under mature_1y, mature_3y, and mature_latest.
- Revision DFM Kalman wins DELTA_TS only under mature_1y. For mature_3y and mature_latest, no-revision/SPF/indicator-revision tie on DELTA_TS.
- DELTA_MT is again dominated by no-revision/SPF/indicator-revision ties across mature variants.

Manuscript wording:

> The mature-target variants strengthen the central conclusion: official early releases are hard benchmarks, but the mixed-frequency Kalman system contributes to revision-risk measurement, especially for advance-to-second revisions.

## Key Frozen Tables To Use

Use these files for the manuscript:

- Full point RMSE/MAE/bias: `runs/exact_pseudo_backtest_max_iter100/report_dir/point_metrics_full.csv`
- Full revision RMSE/MAE/bias: `runs/exact_pseudo_backtest_max_iter100/report_dir/revision_metrics_full.csv`
- SPF common sample: `runs/exact_pseudo_backtest_max_iter100/evidence_dir/common_sample_spf_point.csv`
- SPF revision common sample: `runs/exact_pseudo_backtest_max_iter100/evidence_dir/common_sample_spf_revision.csv`
- Bootstrap loss differences: `runs/exact_pseudo_backtest_max_iter100/evidence_dir/bootstrap_loss_difference_point.csv`
- Revision bootstrap loss differences: `runs/exact_pseudo_backtest_max_iter100/evidence_dir/bootstrap_loss_difference_revision.csv`
- Density point metrics: `runs/exact_pseudo_backtest_max_iter100/evidence_dir/density_point_metrics.csv`
- Density revision metrics: `runs/exact_pseudo_backtest_max_iter100/evidence_dir/density_revision_metrics.csv`
- Revision threshold diagnostics: `runs/exact_pseudo_backtest_max_iter100/evidence_dir/revision_threshold_diagnostics.csv`
- Release mechanism analysis: `runs/exact_pseudo_backtest_max_iter100/evidence_dir/release_mechanism_analysis.csv`
- Mature robustness winners: `MATURE_ROBUSTNESS_WINNERS_FROM_FREEZE.csv`

## Draft Results Paragraph

In the full 2005Q1-2024Q4 real-time evaluation, the ranking of models depends sharply on the release stage. Before the advance release, the SPF benchmark is the strongest point forecast, with RMSE 2.225 against 3.066 for the best internal DFM benchmark and 3.383 for the GDP revision Kalman model. After the advance estimate is observed, however, the no-revision benchmark dominates point forecasting: it attains RMSE 0.570 before the second release and 0.362 before the third release. The monthly mixed-frequency Kalman model is close at the third-release checkpoint, with RMSE 0.369, but does not overturn the no-revision benchmark in point loss.

The state-space contribution is clearer outside the simple point-winner comparison. The max_iter=100 Kalman/EM run has full convergence across state-space rows and finite, positive, PSD predictive covariance diagnostics for the monthly mixed-frequency Kalman model. Density evidence shows that state-space models are competitive where release uncertainty is most relevant: indicator-revision Kalman has the best point-density CRPS before the third release, and revision DFM Kalman has the best revision-density CRPS for DELTA_TS. Mature-target robustness further shows that the monthly mixed-frequency Kalman model wins DELTA_SA across mature target variants. These results motivate a release-ladder interpretation rather than a universal-dominance claim: early official GDP releases are difficult point-forecast benchmarks, while state-space structure adds value through uncertainty, revision-risk measurement, and mechanism diagnostics.

## Next Freeze

Run sensitivity separately after this core draft:

- `q1_manuscript_v1_sensitivity_k`
- `q1_manuscript_v1_sensitivity_midas`
- `q1_manuscript_v1_sensitivity_rolling`
- `q1_manuscript_v1_sensitivity_exclude_covid`

Do not mix these into the core freeze.
