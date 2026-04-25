# Table 1. Headline Point-Forecast Performance

Source: `outputs/frozen/submission_final/headline_point_results.csv`.

Note: Rows are sorted by snapshot mode, GDP release target, and RMSE. Lower RMSE/MAE is better; relative RMSFE is computed against the designated benchmark in the frozen evaluation pipeline.

| snapshot_mode | target_id | checkpoint_id | model_id | RMSE | MAE | bias | relative_RMSFE | DM_test | DM_test_small_sample | n_forecasts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exact | A | pre_advance | bridge | 5.151 | 2.156 | -0.641 | 0.715 | 0.285 | 0.288 | 80 |
| exact | A | pre_advance | standard_dfm | 5.21 | 2.203 | -0.874 | 0.723 | 0.324 | 0.327 | 80 |
| exact | A | pre_advance | ar | 7.201 | 2.518 | 0.135 | 1.0 |  |  | 80 |
| exact | A | pre_advance | revision_dfm | 7.309 | 2.683 | -0.267 | 1.015 | 0.711 | 0.712 | 80 |
| exact | A | pre_advance | release_dfm | 7.379 | 2.676 | -0.354 | 1.025 | 0.369 | 0.372 | 80 |
| exact | S | pre_second | release_dfm | 0.669 | 0.458 | -0.029 | 0.095 | 0.156 | 0.159 | 80 |
| exact | S | pre_second | revision_dfm | 0.671 | 0.46 | -0.027 | 0.096 | 0.156 | 0.159 | 80 |
| exact | S | pre_second | bridge | 4.996 | 2.202 | -0.586 | 0.713 | 0.287 | 0.29 | 80 |
| exact | S | pre_second | standard_dfm | 5.17 | 2.315 | -0.854 | 0.738 | 0.325 | 0.328 | 80 |
| exact | S | pre_second | ar | 7.007 | 2.577 | 0.048 | 1.0 |  |  | 80 |
| exact | T | pre_third | revision_dfm | 0.364 | 0.241 | 0.047 | 0.053 | 0.147 | 0.15 | 80 |
| exact | T | pre_third | release_dfm | 0.37 | 0.243 | 0.044 | 0.054 | 0.147 | 0.15 | 80 |
| exact | T | pre_third | bridge | 5.051 | 2.233 | -0.592 | 0.731 | 0.29 | 0.293 | 80 |
| exact | T | pre_third | standard_dfm | 5.17 | 2.357 | -0.87 | 0.749 | 0.322 | 0.325 | 80 |
| exact | T | pre_third | ar | 6.906 | 2.598 | 0.028 | 1.0 |  |  | 80 |
| pseudo | A | pre_advance | standard_dfm | 5.065 | 2.216 | -0.919 | 0.703 | 0.296 | 0.299 | 80 |
| pseudo | A | pre_advance | bridge | 5.121 | 2.299 | -0.454 | 0.711 | 0.265 | 0.268 | 80 |
| pseudo | A | pre_advance | ar | 7.201 | 2.518 | 0.135 | 1.0 |  |  | 80 |
| pseudo | A | pre_advance | revision_dfm | 7.294 | 2.673 | -0.258 | 1.013 | 0.752 | 0.754 | 80 |
| pseudo | A | pre_advance | release_dfm | 7.363 | 2.665 | -0.343 | 1.023 | 0.415 | 0.418 | 80 |
| pseudo | S | pre_second | revision_dfm | 0.667 | 0.458 | -0.027 | 0.095 | 0.156 | 0.159 | 80 |
| pseudo | S | pre_second | release_dfm | 0.668 | 0.458 | -0.029 | 0.095 | 0.156 | 0.159 | 80 |
| pseudo | S | pre_second | bridge | 5.122 | 2.269 | -0.62 | 0.731 | 0.288 | 0.291 | 80 |
| pseudo | S | pre_second | standard_dfm | 5.206 | 2.339 | -0.861 | 0.743 | 0.327 | 0.33 | 80 |
| pseudo | S | pre_second | ar | 7.007 | 2.577 | 0.048 | 1.0 |  |  | 80 |
| pseudo | T | pre_third | revision_dfm | 0.388 | 0.251 | 0.057 | 0.056 | 0.148 | 0.15 | 80 |
| pseudo | T | pre_third | release_dfm | 0.392 | 0.252 | 0.053 | 0.057 | 0.148 | 0.15 | 80 |
| pseudo | T | pre_third | bridge | 5.037 | 2.237 | -0.64 | 0.729 | 0.292 | 0.295 | 80 |
| pseudo | T | pre_third | standard_dfm | 5.172 | 2.34 | -0.879 | 0.749 | 0.319 | 0.322 | 80 |
| pseudo | T | pre_third | ar | 6.906 | 2.598 | 0.028 | 1.0 |  |  | 80 |
