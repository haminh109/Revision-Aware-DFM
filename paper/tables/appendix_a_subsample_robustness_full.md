# Appendix Table A1. Full Subsample Robustness Results

Source: `outputs/frozen/submission_final/headline_point_subsample_robustness.csv`.

| sample_name | sample_label | snapshot_mode | target_id | checkpoint_id | model_id | RMSE_sample | MAE_sample | bias | relative_RMSFE | DM_test_sample | DM_test_small_sample_sample | n_forecasts_sample | rmse_change_sample_minus_full |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| no_pandemic | Exclude pandemic quarters | exact | A | pre_advance | bridge | 1.984 | 1.438 | -0.641 | 0.715 | 0.516 | 0.519 | 78 | -3.167 |
| no_pandemic | Exclude pandemic quarters | exact | A | pre_advance | standard_dfm | 1.988 | 1.48 | -0.874 | 0.723 | 0.397 | 0.4 | 78 | -3.221 |
| no_pandemic | Exclude pandemic quarters | exact | A | pre_advance | ar | 2.182 | 1.5 | 0.135 | 1.0 |  |  | 78 | -5.019 |
| no_pandemic | Exclude pandemic quarters | exact | A | pre_advance | release_dfm | 2.811 | 1.671 | -0.354 | 1.025 | 0.28 | 0.283 | 78 | -4.567 |
| no_pandemic | Exclude pandemic quarters | exact | A | pre_advance | revision_dfm | 2.965 | 1.697 | -0.267 | 1.015 | 0.295 | 0.298 | 78 | -4.344 |
| no_pandemic | Exclude pandemic quarters | exact | S | pre_second | release_dfm | 0.613 | 0.423 | -0.029 | 0.095 | 0.0 | 0.0 | 78 | -0.055 |
| no_pandemic | Exclude pandemic quarters | exact | S | pre_second | revision_dfm | 0.616 | 0.425 | -0.027 | 0.096 | 0.0 | 0.0 | 78 | -0.056 |
| no_pandemic | Exclude pandemic quarters | exact | S | pre_second | bridge | 2.146 | 1.521 | -0.586 | 0.713 | 0.655 | 0.657 | 78 | -2.85 |
| no_pandemic | Exclude pandemic quarters | exact | S | pre_second | standard_dfm | 2.184 | 1.61 | -0.854 | 0.738 | 0.644 | 0.646 | 78 | -2.986 |
| no_pandemic | Exclude pandemic quarters | exact | S | pre_second | ar | 2.274 | 1.59 | 0.048 | 1.0 |  |  | 78 | -4.734 |
| no_pandemic | Exclude pandemic quarters | exact | T | pre_third | revision_dfm | 0.364 | 0.239 | 0.047 | 0.053 | 0.0 | 0.0 | 78 | 0.0 |
| no_pandemic | Exclude pandemic quarters | exact | T | pre_third | release_dfm | 0.371 | 0.241 | 0.044 | 0.054 | 0.0 | 0.0 | 78 | 0.001 |
| no_pandemic | Exclude pandemic quarters | exact | T | pre_third | bridge | 2.185 | 1.55 | -0.592 | 0.731 | 0.566 | 0.569 | 78 | -2.866 |
| no_pandemic | Exclude pandemic quarters | exact | T | pre_third | standard_dfm | 2.227 | 1.661 | -0.87 | 0.749 | 0.542 | 0.545 | 78 | -2.944 |
| no_pandemic | Exclude pandemic quarters | exact | T | pre_third | ar | 2.349 | 1.637 | 0.028 | 1.0 |  |  | 78 | -4.557 |
| no_pandemic | Exclude pandemic quarters | pseudo | A | pre_advance | ar | 2.182 | 1.5 | 0.135 | 1.0 |  |  | 78 | -5.019 |
| no_pandemic | Exclude pandemic quarters | pseudo | A | pre_advance | standard_dfm | 2.208 | 1.532 | -0.919 | 0.703 | 0.892 | 0.892 | 78 | -2.857 |
| no_pandemic | Exclude pandemic quarters | pseudo | A | pre_advance | bridge | 2.285 | 1.614 | -0.454 | 0.711 | 0.466 | 0.469 | 78 | -2.836 |
| no_pandemic | Exclude pandemic quarters | pseudo | A | pre_advance | release_dfm | 2.804 | 1.662 | -0.343 | 1.023 | 0.286 | 0.29 | 78 | -4.559 |
| no_pandemic | Exclude pandemic quarters | pseudo | A | pre_advance | revision_dfm | 2.957 | 1.688 | -0.258 | 1.013 | 0.299 | 0.302 | 78 | -4.337 |
| no_pandemic | Exclude pandemic quarters | pseudo | S | pre_second | release_dfm | 0.613 | 0.423 | -0.029 | 0.095 | 0.0 | 0.0 | 78 | -0.055 |
| no_pandemic | Exclude pandemic quarters | pseudo | S | pre_second | revision_dfm | 0.615 | 0.425 | -0.027 | 0.095 | 0.0 | 0.0 | 78 | -0.052 |
| no_pandemic | Exclude pandemic quarters | pseudo | S | pre_second | bridge | 2.111 | 1.564 | -0.62 | 0.731 | 0.582 | 0.585 | 78 | -3.011 |
| no_pandemic | Exclude pandemic quarters | pseudo | S | pre_second | standard_dfm | 2.179 | 1.628 | -0.861 | 0.743 | 0.633 | 0.635 | 78 | -3.027 |
| no_pandemic | Exclude pandemic quarters | pseudo | S | pre_second | ar | 2.274 | 1.59 | 0.048 | 1.0 |  |  | 78 | -4.734 |
| no_pandemic | Exclude pandemic quarters | pseudo | T | pre_third | revision_dfm | 0.389 | 0.249 | 0.057 | 0.056 | 0.0 | 0.0 | 78 | 0.001 |
| no_pandemic | Exclude pandemic quarters | pseudo | T | pre_third | release_dfm | 0.394 | 0.25 | 0.053 | 0.057 | 0.0 | 0.0 | 78 | 0.001 |
| no_pandemic | Exclude pandemic quarters | pseudo | T | pre_third | bridge | 2.222 | 1.56 | -0.64 | 0.729 | 0.65 | 0.652 | 78 | -2.815 |
| no_pandemic | Exclude pandemic quarters | pseudo | T | pre_third | standard_dfm | 2.245 | 1.644 | -0.879 | 0.749 | 0.61 | 0.612 | 78 | -2.926 |
| no_pandemic | Exclude pandemic quarters | pseudo | T | pre_third | ar | 2.349 | 1.637 | 0.028 | 1.0 |  |  | 78 | -4.557 |
| post_gfc | Post-GFC | exact | A | pre_advance | bridge | 5.831 | 2.351 | -0.641 | 0.715 | 0.293 | 0.297 | 60 | 0.68 |
| post_gfc | Post-GFC | exact | A | pre_advance | standard_dfm | 5.854 | 2.349 | -0.874 | 0.723 | 0.324 | 0.328 | 60 | 0.645 |
| post_gfc | Post-GFC | exact | A | pre_advance | ar | 8.202 | 2.728 | 0.135 | 1.0 |  |  | 60 | 1.001 |
| post_gfc | Post-GFC | exact | A | pre_advance | revision_dfm | 8.333 | 2.988 | -0.267 | 1.015 | 0.702 | 0.704 | 60 | 1.024 |
| post_gfc | Post-GFC | exact | A | pre_advance | release_dfm | 8.41 | 2.994 | -0.354 | 1.025 | 0.367 | 0.371 | 60 | 1.032 |
| post_gfc | Post-GFC | exact | S | pre_second | release_dfm | 0.582 | 0.399 | -0.029 | 0.095 | 0.171 | 0.175 | 60 | -0.087 |
| post_gfc | Post-GFC | exact | S | pre_second | revision_dfm | 0.584 | 0.402 | -0.027 | 0.096 | 0.171 | 0.175 | 60 | -0.087 |
| post_gfc | Post-GFC | exact | S | pre_second | bridge | 5.619 | 2.339 | -0.586 | 0.713 | 0.297 | 0.301 | 60 | 0.623 |
| post_gfc | Post-GFC | exact | S | pre_second | standard_dfm | 5.764 | 2.418 | -0.854 | 0.738 | 0.324 | 0.328 | 60 | 0.594 |
| post_gfc | Post-GFC | exact | S | pre_second | ar | 7.958 | 2.761 | 0.048 | 1.0 |  |  | 60 | 0.951 |
| post_gfc | Post-GFC | exact | T | pre_third | revision_dfm | 0.395 | 0.257 | 0.047 | 0.053 | 0.163 | 0.167 | 60 | 0.031 |
| post_gfc | Post-GFC | exact | T | pre_third | release_dfm | 0.401 | 0.258 | 0.044 | 0.054 | 0.164 | 0.167 | 60 | 0.032 |
| post_gfc | Post-GFC | exact | T | pre_third | bridge | 5.648 | 2.309 | -0.592 | 0.731 | 0.295 | 0.299 | 60 | 0.598 |
| post_gfc | Post-GFC | exact | T | pre_third | standard_dfm | 5.744 | 2.442 | -0.87 | 0.749 | 0.318 | 0.322 | 60 | 0.574 |
| post_gfc | Post-GFC | exact | T | pre_third | ar | 7.825 | 2.798 | 0.028 | 1.0 |  |  | 60 | 0.918 |
| post_gfc | Post-GFC | pseudo | A | pre_advance | standard_dfm | 5.633 | 2.309 | -0.919 | 0.703 | 0.288 | 0.292 | 60 | 0.567 |
| post_gfc | Post-GFC | pseudo | A | pre_advance | bridge | 5.78 | 2.56 | -0.454 | 0.711 | 0.27 | 0.274 | 60 | 0.659 |
| post_gfc | Post-GFC | pseudo | A | pre_advance | ar | 8.202 | 2.728 | 0.135 | 1.0 |  |  | 60 | 1.001 |
| post_gfc | Post-GFC | pseudo | A | pre_advance | revision_dfm | 8.316 | 2.972 | -0.258 | 1.013 | 0.744 | 0.746 | 60 | 1.021 |
| post_gfc | Post-GFC | pseudo | A | pre_advance | release_dfm | 8.392 | 2.977 | -0.343 | 1.023 | 0.414 | 0.418 | 60 | 1.029 |
| post_gfc | Post-GFC | pseudo | S | pre_second | revision_dfm | 0.577 | 0.399 | -0.027 | 0.095 | 0.171 | 0.175 | 60 | -0.089 |
| post_gfc | Post-GFC | pseudo | S | pre_second | release_dfm | 0.582 | 0.4 | -0.029 | 0.095 | 0.171 | 0.175 | 60 | -0.087 |
| post_gfc | Post-GFC | pseudo | S | pre_second | bridge | 5.774 | 2.435 | -0.62 | 0.731 | 0.299 | 0.303 | 60 | 0.652 |
| post_gfc | Post-GFC | pseudo | S | pre_second | standard_dfm | 5.81 | 2.447 | -0.861 | 0.743 | 0.326 | 0.33 | 60 | 0.604 |
| post_gfc | Post-GFC | pseudo | S | pre_second | ar | 7.958 | 2.761 | 0.048 | 1.0 |  |  | 60 | 0.951 |
| post_gfc | Post-GFC | pseudo | T | pre_third | revision_dfm | 0.424 | 0.27 | 0.057 | 0.056 | 0.164 | 0.167 | 60 | 0.036 |
| post_gfc | Post-GFC | pseudo | T | pre_third | release_dfm | 0.429 | 0.27 | 0.053 | 0.057 | 0.164 | 0.167 | 60 | 0.037 |
| post_gfc | Post-GFC | pseudo | T | pre_third | bridge | 5.635 | 2.326 | -0.64 | 0.729 | 0.297 | 0.301 | 60 | 0.598 |
| post_gfc | Post-GFC | pseudo | T | pre_third | standard_dfm | 5.751 | 2.443 | -0.879 | 0.749 | 0.317 | 0.321 | 60 | 0.579 |
| post_gfc | Post-GFC | pseudo | T | pre_third | ar | 7.825 | 2.798 | 0.028 | 1.0 |  |  | 60 | 0.918 |
| pre_gfc | Pre-GFC | exact | A | pre_advance | release_dfm | 1.386 | 1.046 | -0.354 | 1.025 | 0.467 | 0.486 | 12 | -5.993 |
| pre_gfc | Pre-GFC | exact | A | pre_advance | revision_dfm | 1.404 | 1.099 | -0.267 | 1.015 | 0.476 | 0.495 | 12 | -5.905 |
| pre_gfc | Pre-GFC | exact | A | pre_advance | bridge | 1.486 | 1.266 | -0.641 | 0.715 | 0.665 | 0.678 | 12 | -3.665 |
| pre_gfc | Pre-GFC | exact | A | pre_advance | ar | 1.612 | 1.401 | 0.135 | 1.0 |  |  | 12 | -5.588 |
| pre_gfc | Pre-GFC | exact | A | pre_advance | standard_dfm | 1.649 | 1.272 | -0.874 | 0.723 | 0.917 | 0.92 | 12 | -3.561 |
| pre_gfc | Pre-GFC | exact | S | pre_second | release_dfm | 0.629 | 0.543 | -0.029 | 0.095 | 0.023 | 0.028 | 12 | -0.04 |
| pre_gfc | Pre-GFC | exact | S | pre_second | revision_dfm | 0.63 | 0.546 | -0.027 | 0.096 | 0.023 | 0.028 | 12 | -0.041 |
| pre_gfc | Pre-GFC | exact | S | pre_second | ar | 1.733 | 1.44 | 0.048 | 1.0 |  |  | 12 | -5.274 |
| pre_gfc | Pre-GFC | exact | S | pre_second | bridge | 1.82 | 1.503 | -0.586 | 0.713 | 0.808 | 0.816 | 12 | -3.175 |
| pre_gfc | Pre-GFC | exact | S | pre_second | standard_dfm | 1.882 | 1.498 | -0.854 | 0.738 | 0.728 | 0.739 | 12 | -3.288 |
| pre_gfc | Pre-GFC | exact | T | pre_third | release_dfm | 0.195 | 0.153 | 0.044 | 0.054 | 0.011 | 0.014 | 12 | -0.174 |
| pre_gfc | Pre-GFC | exact | T | pre_third | revision_dfm | 0.196 | 0.154 | 0.047 | 0.053 | 0.011 | 0.014 | 12 | -0.168 |
| pre_gfc | Pre-GFC | exact | T | pre_third | ar | 1.78 | 1.469 | 0.028 | 1.0 |  |  | 12 | -5.127 |
| pre_gfc | Pre-GFC | exact | T | pre_third | standard_dfm | 2.001 | 1.629 | -0.87 | 0.749 | 0.612 | 0.627 | 12 | -3.17 |
| pre_gfc | Pre-GFC | exact | T | pre_third | bridge | 2.056 | 1.701 | -0.592 | 0.731 | 0.519 | 0.536 | 12 | -2.995 |
| pre_gfc | Pre-GFC | pseudo | A | pre_advance | release_dfm | 1.4 | 1.057 | -0.343 | 1.023 | 0.497 | 0.516 | 12 | -5.962 |
| pre_gfc | Pre-GFC | pseudo | A | pre_advance | revision_dfm | 1.417 | 1.107 | -0.258 | 1.013 | 0.506 | 0.524 | 12 | -5.877 |
| pre_gfc | Pre-GFC | pseudo | A | pre_advance | bridge | 1.437 | 1.262 | -0.454 | 0.711 | 0.404 | 0.423 | 12 | -3.684 |
| pre_gfc | Pre-GFC | pseudo | A | pre_advance | standard_dfm | 1.573 | 1.207 | -0.919 | 0.703 | 0.907 | 0.911 | 12 | -3.492 |
| pre_gfc | Pre-GFC | pseudo | A | pre_advance | ar | 1.612 | 1.401 | 0.135 | 1.0 |  |  | 12 | -5.588 |
| pre_gfc | Pre-GFC | pseudo | S | pre_second | release_dfm | 0.629 | 0.544 | -0.029 | 0.095 | 0.023 | 0.028 | 12 | -0.039 |
| pre_gfc | Pre-GFC | pseudo | S | pre_second | revision_dfm | 0.631 | 0.546 | -0.027 | 0.095 | 0.023 | 0.028 | 12 | -0.036 |
| pre_gfc | Pre-GFC | pseudo | S | pre_second | ar | 1.733 | 1.44 | 0.048 | 1.0 |  |  | 12 | -5.274 |
| pre_gfc | Pre-GFC | pseudo | S | pre_second | bridge | 1.768 | 1.517 | -0.62 | 0.731 | 0.905 | 0.909 | 12 | -3.354 |
| pre_gfc | Pre-GFC | pseudo | S | pre_second | standard_dfm | 1.782 | 1.473 | -0.861 | 0.743 | 0.887 | 0.892 | 12 | -3.424 |
| pre_gfc | Pre-GFC | pseudo | T | pre_third | release_dfm | 0.195 | 0.153 | 0.053 | 0.057 | 0.011 | 0.014 | 12 | -0.197 |
| pre_gfc | Pre-GFC | pseudo | T | pre_third | revision_dfm | 0.196 | 0.154 | 0.057 | 0.056 | 0.011 | 0.014 | 12 | -0.192 |
| pre_gfc | Pre-GFC | pseudo | T | pre_third | ar | 1.78 | 1.469 | 0.028 | 1.0 |  |  | 12 | -5.127 |
| pre_gfc | Pre-GFC | pseudo | T | pre_third | standard_dfm | 1.977 | 1.59 | -0.879 | 0.749 | 0.664 | 0.678 | 12 | -3.195 |
| pre_gfc | Pre-GFC | pseudo | T | pre_third | bridge | 2.007 | 1.662 | -0.64 | 0.729 | 0.587 | 0.602 | 12 | -3.03 |
