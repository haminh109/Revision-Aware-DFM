# Q2 Manuscript Results Brief

Source freeze: `outputs/full_state_space_release_revision_dfm/frozen/q2_manuscript_best_v1`.
Generated UTC in manifest: `2026-04-25T16:37:10+00:00`. SPF benchmark was not used (`spf_forecasts = null`).
Main headline run: `max_iter=100`, full sample, 4780 point forecast records and 4760 revision forecast records.

## Run Integrity

| scope         |   failures |
|:--------------|-----------:|
| main_50       |          0 |
| main_100      |          0 |
| mature_1y     |          0 |
| mature_3y     |          0 |
| mature_latest |          0 |
| init_seed_1   |          0 |
| init_seed_2   |          0 |
| init_seed_3   |          0 |
| init_seed_4   |          0 |
| init_seed_5   |          0 |

All main, robustness, and initialization seed runs report zero failure rows when `failures=0`.

## Headline Point RMSE Winners: Main `max_iter=100`

| timing_mode   | checkpoint_id   | target_id   | winner_models             |   winner_RMSE |   n_forecasts |
|:--------------|:----------------|:------------|:--------------------------|--------------:|--------------:|
| exact         | pre_advance     | A           | standard_dfm; release_dfm |        3.0659 |            80 |
| exact         | pre_second      | S           | no_revision               |        0.5697 |            79 |
| exact         | pre_third       | T           | no_revision               |        0.3622 |            80 |
| pseudo        | pre_advance     | A           | standard_dfm; release_dfm |        3.0517 |            80 |
| pseudo        | pre_second      | S           | no_revision               |        0.5697 |            79 |
| pseudo        | pre_third       | T           | no_revision               |        0.3622 |            80 |

## Headline Revision RMSE Winners: Main `max_iter=100`

| timing_mode   | checkpoint_id   | revision_target_id   | winner_models                                      |   winner_RMSE |   n_forecasts |
|:--------------|:----------------|:---------------------|:---------------------------------------------------|--------------:|--------------:|
| exact         | pre_advance     | DELTA_SA             | no_revision; indicator_revision_only_dfm_kalman_em |        0.5697 |            79 |
| exact         | pre_second      | DELTA_TS             | no_revision; indicator_revision_only_dfm_kalman_em |        0.3614 |            79 |
| exact         | pre_third       | DELTA_MT             | no_revision; indicator_revision_only_dfm_kalman_em |        1.3387 |            80 |
| pseudo        | pre_advance     | DELTA_SA             | no_revision; indicator_revision_only_dfm_kalman_em |        0.5697 |            79 |
| pseudo        | pre_second      | DELTA_TS             | no_revision; indicator_revision_only_dfm_kalman_em |        0.3614 |            79 |
| pseudo        | pre_third       | DELTA_MT             | no_revision; indicator_revision_only_dfm_kalman_em |        1.3387 |            80 |

Interpretation: `standard_dfm`/`release_dfm` win the advance point nowcast; `no_revision` is the hard benchmark for S/T point forecasts and baseline revision targets. The manuscript should not claim universal dominance of the structured Kalman models.

## State-Space Convergence: Main `max_iter=100`

| model_id                                    |   rows |   min_convergence_rate |   median_convergence_rate |   max_mean_iterations |   max_median_llf_relative_last_improvement |
|:--------------------------------------------|-------:|-----------------------:|--------------------------:|----------------------:|-------------------------------------------:|
| indicator_revision_only_dfm_kalman_em       |     12 |                      1 |                         1 |               31.962  |                                     0.0001 |
| joint_indicator_revision_dfm_full_kalman_em |     12 |                      1 |                         1 |               32.6203 |                                     0.0001 |
| monthly_mixed_frequency_kalman_em           |     12 |                      1 |                         1 |               42.9875 |                                     0.0001 |
| revision_dfm_kalman_em                      |     12 |                      1 |                         1 |               24.8228 |                                     0.0001 |

Main-run convergence is clean for all tracked state-space models, including `monthly_mixed_frequency_kalman_em`.

## Variance And Covariance Audit: Main `max_iter=100`

| table    | model_id                                    |   min_share_positive_variance |   min_share_finite_sd |   mean_sd_to_rmse_min |   mean_sd_to_rmse_max |   coverage_90_min |   coverage_90_max |
|:---------|:--------------------------------------------|------------------------------:|----------------------:|----------------------:|----------------------:|------------------:|------------------:|
| point    | indicator_revision_only_dfm_kalman_em       |                             1 |                     1 |                0.5444 |                1.0611 |            0.8125 |            0.9375 |
| point    | joint_indicator_revision_dfm_full_kalman_em |                             1 |                     1 |                0.4638 |                1.014  |            0.775  |            0.9375 |
| point    | monthly_mixed_frequency_kalman_em           |                             1 |                     1 |                0.5162 |                1.0352 |            0.8875 |            0.95   |
| point    | revision_dfm_kalman_em                      |                             1 |                     1 |                0.5504 |                1.0135 |            0.875  |            0.9375 |
| revision | indicator_revision_only_dfm_kalman_em       |                             1 |                     1 |                1.0535 |                1.5931 |            0.9367 |            0.975  |
| revision | joint_indicator_revision_dfm_full_kalman_em |                             1 |                     1 |                0.9739 |                1.5921 |            0.8861 |            0.9875 |
| revision | monthly_mixed_frequency_kalman_em           |                             1 |                     1 |                0.9391 |                1.5496 |            0.9114 |            0.975  |
| revision | revision_dfm_kalman_em                      |                             1 |                     1 |                1.0154 |                1.5902 |            0.8734 |            0.975  |


| model_id                                    |   min_share_psd |   min_min_eigenvalue |   max_asymmetry |
|:--------------------------------------------|----------------:|---------------------:|----------------:|
| indicator_revision_only_dfm_kalman_em       |               1 |               0.0261 |               0 |
| joint_indicator_revision_dfm_full_kalman_em |               1 |               0.0289 |               0 |
| monthly_mixed_frequency_kalman_em           |               1 |               0.0573 |               0 |
| revision_dfm_kalman_em                      |               1 |               0.0406 |               0 |

All key state-space covariance matrices in the main run are PSD with finite positive predictive variance. Coverage/calibration should still be discussed because advance densities are relatively under-dispersed while mature-revision densities can be wide.

## Initialization Stability Including Mixed-Frequency Model

| table    | model_id                                    |   min_n_seeds |   max_rmse_range |   median_rmse_range |   min_convergence_rate |   max_mean_iterations |
|:---------|:--------------------------------------------|--------------:|-----------------:|--------------------:|-----------------------:|----------------------:|
| point    | indicator_revision_only_dfm_kalman_em       |             5 |           0.0499 |              0.0081 |                      1 |               44.25   |
| point    | joint_indicator_revision_dfm_full_kalman_em |             5 |           0.2586 |              0.0441 |                      1 |               44.5833 |
| point    | monthly_mixed_frequency_kalman_em           |             5 |           0      |              0      |                      1 |               36.625  |
| point    | revision_dfm_kalman_em                      |             5 |           0.1865 |              0.001  |                      1 |               26.6667 |
| revision | indicator_revision_only_dfm_kalman_em       |             5 |           0      |              0      |                      1 |               44.25   |
| revision | joint_indicator_revision_dfm_full_kalman_em |             5 |           0.0485 |              0.0013 |                      1 |               44.5833 |
| revision | monthly_mixed_frequency_kalman_em           |             5 |           0      |              0      |                      1 |               36.625  |
| revision | revision_dfm_kalman_em                      |             5 |           0.0261 |              0.0001 |                      1 |               26.6667 |

This table is computed from raw seed runs because the built-in initialization stability CSV does not include `monthly_mixed_frequency_kalman_em`.

## Mature-Target Robustness Winners

| variant       | table    | timing_mode   | checkpoint_id   | target_id   | revision_target_id   | winner_models                                      |   winner_RMSE |
|:--------------|:---------|:--------------|:----------------|:------------|:---------------------|:---------------------------------------------------|--------------:|
| mature_1y     | point    | exact         | pre_advance     | A           |                      | standard_dfm; release_dfm                          |        3.0659 |
| mature_1y     | point    | exact         | pre_second      | S           |                      | no_revision                                        |        0.5697 |
| mature_1y     | point    | exact         | pre_third       | T           |                      | no_revision                                        |        0.3622 |
| mature_1y     | point    | pseudo        | pre_advance     | A           |                      | standard_dfm; release_dfm                          |        3.0517 |
| mature_1y     | point    | pseudo        | pre_second      | S           |                      | no_revision                                        |        0.5697 |
| mature_1y     | point    | pseudo        | pre_third       | T           |                      | no_revision                                        |        0.3622 |
| mature_1y     | revision | exact         | pre_advance     |             | DELTA_SA             | monthly_mixed_frequency_kalman_em                  |        0.565  |
| mature_1y     | revision | exact         | pre_second      |             | DELTA_TS             | revision_dfm_kalman_em                             |        0.3613 |
| mature_1y     | revision | exact         | pre_third       |             | DELTA_MT             | no_revision; indicator_revision_only_dfm_kalman_em |        1.0016 |
| mature_1y     | revision | pseudo        | pre_advance     |             | DELTA_SA             | monthly_mixed_frequency_kalman_em                  |        0.5648 |
| mature_1y     | revision | pseudo        | pre_second      |             | DELTA_TS             | revision_dfm_kalman_em                             |        0.3613 |
| mature_1y     | revision | pseudo        | pre_third       |             | DELTA_MT             | no_revision; indicator_revision_only_dfm_kalman_em |        1.0016 |
| mature_3y     | point    | exact         | pre_advance     | A           |                      | standard_dfm; release_dfm                          |        3.0659 |
| mature_3y     | point    | exact         | pre_second      | S           |                      | no_revision                                        |        0.5697 |
| mature_3y     | point    | exact         | pre_third       | T           |                      | no_revision                                        |        0.3622 |
| mature_3y     | point    | pseudo        | pre_advance     | A           |                      | standard_dfm; release_dfm                          |        3.0517 |
| mature_3y     | point    | pseudo        | pre_second      | S           |                      | no_revision                                        |        0.5697 |
| mature_3y     | point    | pseudo        | pre_third       | T           |                      | no_revision                                        |        0.3622 |
| mature_3y     | revision | exact         | pre_advance     |             | DELTA_SA             | monthly_mixed_frequency_kalman_em                  |        0.5626 |
| mature_3y     | revision | exact         | pre_second      |             | DELTA_TS             | no_revision; indicator_revision_only_dfm_kalman_em |        0.3614 |
| mature_3y     | revision | exact         | pre_third       |             | DELTA_MT             | no_revision; indicator_revision_only_dfm_kalman_em |        1.4192 |
| mature_3y     | revision | pseudo        | pre_advance     |             | DELTA_SA             | monthly_mixed_frequency_kalman_em                  |        0.5623 |
| mature_3y     | revision | pseudo        | pre_second      |             | DELTA_TS             | no_revision; indicator_revision_only_dfm_kalman_em |        0.3614 |
| mature_3y     | revision | pseudo        | pre_third       |             | DELTA_MT             | no_revision; indicator_revision_only_dfm_kalman_em |        1.4192 |
| mature_latest | point    | exact         | pre_advance     | A           |                      | standard_dfm; release_dfm                          |        3.0659 |
| mature_latest | point    | exact         | pre_second      | S           |                      | no_revision                                        |        0.5697 |
| mature_latest | point    | exact         | pre_third       | T           |                      | no_revision                                        |        0.3622 |
| mature_latest | point    | pseudo        | pre_advance     | A           |                      | standard_dfm; release_dfm                          |        3.0517 |
| mature_latest | point    | pseudo        | pre_second      | S           |                      | no_revision                                        |        0.5697 |
| mature_latest | point    | pseudo        | pre_third       | T           |                      | no_revision                                        |        0.3622 |
| mature_latest | revision | exact         | pre_advance     |             | DELTA_SA             | monthly_mixed_frequency_kalman_em                  |        0.5659 |
| mature_latest | revision | exact         | pre_second      |             | DELTA_TS             | no_revision; indicator_revision_only_dfm_kalman_em |        0.3614 |
| mature_latest | revision | exact         | pre_third       |             | DELTA_MT             | no_revision; indicator_revision_only_dfm_kalman_em |        1.3391 |
| mature_latest | revision | pseudo        | pre_advance     |             | DELTA_SA             | monthly_mixed_frequency_kalman_em                  |        0.5655 |
| mature_latest | revision | pseudo        | pre_second      |             | DELTA_TS             | no_revision; indicator_revision_only_dfm_kalman_em |        0.3614 |
| mature_latest | revision | pseudo        | pre_third       |             | DELTA_MT             | no_revision; indicator_revision_only_dfm_kalman_em |        1.3391 |

Mature-target robustness is where `monthly_mixed_frequency_kalman_em` becomes relevant for DELTA_SA in 1-year and 3-year maturity variants, while `no_revision` remains very strong for S/T and mature-latest baselines.

## Manuscript Wording Recommendations

- Use `max_iter=100` as the headline run because it has zero failures and clean main-run convergence/variance diagnostics.

- Use cautious wording: “fixed-iteration Kalman/EM estimates with convergence diagnostics,” not “strictly globally converged EM.”

- State clearly that no SPF file was provided for this freeze; SPF remains an external benchmark slot, not an empirical result in this package.

- Frame the main forecasting result as benchmark discipline: `no_revision` is very hard to beat after A/S releases; structured Kalman models add mechanism, density, and mature-target revision evidence rather than universal RMSE dominance.

- Mention the mixed-frequency warning seen during mature robustness as a numerical caveat, then point to the frozen convergence/variance audit for actual impact.


## Files Added By This Audit

- `FREEZE_FAILURE_AUDIT.csv`

- `HEADLINE_POINT_WINNERS_FROM_FREEZE.csv`

- `HEADLINE_REVISION_WINNERS_FROM_FREEZE.csv`

- `STATE_SPACE_CONVERGENCE_SUMMARY_MAIN_MAX_ITER100.csv`

- `STATE_SPACE_VARIANCE_SUMMARY_MAIN_MAX_ITER100.csv`

- `STATE_SPACE_COVARIANCE_SUMMARY_MAIN_MAX_ITER100.csv`

- `STATE_SPACE_CONVERGENCE_STABILITY_50_VS_100.csv`

- `STATE_SPACE_INITIALIZATION_STABILITY_INCLUDING_MIXED_FREQUENCY.csv`

- `STATE_SPACE_INITIALIZATION_STABILITY_SUMMARY.csv`

- `MATURE_ROBUSTNESS_WINNERS_FROM_FREEZE.csv`

- `EVIDENCE_PACKAGE_FILE_AUDIT.csv`
