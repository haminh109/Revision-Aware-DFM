# Appendix Table A2. Full Scenario Robustness Results

Source: `outputs/frozen/submission_final/headline_point_scenario_robustness.csv`.

| scenario_name | scenario_label | snapshot_mode | target_id | checkpoint_id | model_id | RMSE_scenario | MAE_scenario | bias | relative_RMSFE | DM_test_scenario | DM_test_small_sample_scenario | n_forecasts_scenario | rmse_delta_scenario_minus_main |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| alternative_data_choice | Alternative Data Choice | exact | A | pre_advance | bridge | 4.909 | 2.101 | -0.641 | 0.715 | 0.284 | 0.287 | 80 | -0.243 |
| alternative_data_choice | Alternative Data Choice | exact | A | pre_advance | standard_dfm | 5.19 | 2.218 | -0.874 | 0.723 | 0.322 | 0.325 | 80 | -0.019 |
| alternative_data_choice | Alternative Data Choice | exact | A | pre_advance | ar | 7.201 | 2.518 | 0.135 | 1.0 |  |  | 80 | 0.0 |
| alternative_data_choice | Alternative Data Choice | exact | A | pre_advance | revision_dfm | 7.343 | 2.715 | -0.267 | 1.015 | 0.605 | 0.607 | 80 | 0.034 |
| alternative_data_choice | Alternative Data Choice | exact | A | pre_advance | release_dfm | 7.392 | 2.703 | -0.354 | 1.025 | 0.333 | 0.336 | 80 | 0.013 |
| alternative_data_choice | Alternative Data Choice | exact | S | pre_second | release_dfm | 0.67 | 0.459 | -0.029 | 0.095 | 0.156 | 0.159 | 80 | 0.002 |
| alternative_data_choice | Alternative Data Choice | exact | S | pre_second | revision_dfm | 0.673 | 0.461 | -0.027 | 0.096 | 0.156 | 0.159 | 80 | 0.002 |
| alternative_data_choice | Alternative Data Choice | exact | S | pre_second | bridge | 4.844 | 2.136 | -0.586 | 0.713 | 0.286 | 0.289 | 80 | -0.151 |
| alternative_data_choice | Alternative Data Choice | exact | S | pre_second | standard_dfm | 5.153 | 2.332 | -0.854 | 0.738 | 0.324 | 0.327 | 80 | -0.017 |
| alternative_data_choice | Alternative Data Choice | exact | S | pre_second | ar | 7.007 | 2.577 | 0.048 | 1.0 |  |  | 80 | 0.0 |
| alternative_data_choice | Alternative Data Choice | exact | T | pre_third | revision_dfm | 0.364 | 0.241 | 0.047 | 0.053 | 0.147 | 0.15 | 80 | -0.0 |
| alternative_data_choice | Alternative Data Choice | exact | T | pre_third | release_dfm | 0.369 | 0.243 | 0.044 | 0.054 | 0.147 | 0.15 | 80 | -0.0 |
| alternative_data_choice | Alternative Data Choice | exact | T | pre_third | bridge | 4.919 | 2.167 | -0.592 | 0.731 | 0.29 | 0.293 | 80 | -0.132 |
| alternative_data_choice | Alternative Data Choice | exact | T | pre_third | standard_dfm | 5.151 | 2.372 | -0.87 | 0.749 | 0.32 | 0.323 | 80 | -0.02 |
| alternative_data_choice | Alternative Data Choice | exact | T | pre_third | ar | 6.906 | 2.598 | 0.028 | 1.0 |  |  | 80 | 0.0 |
| alternative_data_choice | Alternative Data Choice | pseudo | A | pre_advance | standard_dfm | 5.045 | 2.221 | -0.919 | 0.703 | 0.294 | 0.297 | 80 | -0.02 |
| alternative_data_choice | Alternative Data Choice | pseudo | A | pre_advance | bridge | 5.084 | 2.235 | -0.454 | 0.711 | 0.259 | 0.262 | 80 | -0.037 |
| alternative_data_choice | Alternative Data Choice | pseudo | A | pre_advance | ar | 7.201 | 2.518 | 0.135 | 1.0 |  |  | 80 | 0.0 |
| alternative_data_choice | Alternative Data Choice | pseudo | A | pre_advance | revision_dfm | 7.286 | 2.696 | -0.258 | 1.013 | 0.785 | 0.786 | 80 | -0.008 |
| alternative_data_choice | Alternative Data Choice | pseudo | A | pre_advance | release_dfm | 7.378 | 2.691 | -0.343 | 1.023 | 0.373 | 0.376 | 80 | 0.015 |
| alternative_data_choice | Alternative Data Choice | pseudo | S | pre_second | revision_dfm | 0.669 | 0.46 | -0.027 | 0.095 | 0.156 | 0.159 | 80 | 0.002 |
| alternative_data_choice | Alternative Data Choice | pseudo | S | pre_second | release_dfm | 0.67 | 0.459 | -0.029 | 0.095 | 0.156 | 0.159 | 80 | 0.002 |
| alternative_data_choice | Alternative Data Choice | pseudo | S | pre_second | bridge | 4.82 | 2.178 | -0.62 | 0.731 | 0.277 | 0.28 | 80 | -0.302 |
| alternative_data_choice | Alternative Data Choice | pseudo | S | pre_second | standard_dfm | 5.188 | 2.354 | -0.861 | 0.743 | 0.326 | 0.329 | 80 | -0.018 |
| alternative_data_choice | Alternative Data Choice | pseudo | S | pre_second | ar | 7.007 | 2.577 | 0.048 | 1.0 |  |  | 80 | 0.0 |
| alternative_data_choice | Alternative Data Choice | pseudo | T | pre_third | release_dfm | 0.392 | 0.252 | 0.053 | 0.057 | 0.148 | 0.15 | 80 | -0.0 |
| alternative_data_choice | Alternative Data Choice | pseudo | T | pre_third | revision_dfm | 0.399 | 0.255 | 0.057 | 0.056 | 0.148 | 0.15 | 80 | 0.011 |
| alternative_data_choice | Alternative Data Choice | pseudo | T | pre_third | bridge | 4.896 | 2.179 | -0.64 | 0.729 | 0.29 | 0.293 | 80 | -0.141 |
| alternative_data_choice | Alternative Data Choice | pseudo | T | pre_third | standard_dfm | 5.153 | 2.355 | -0.879 | 0.749 | 0.318 | 0.321 | 80 | -0.019 |
| alternative_data_choice | Alternative Data Choice | pseudo | T | pre_third | ar | 6.906 | 2.598 | 0.028 | 1.0 |  |  | 80 | 0.0 |
| expanded_panel | Expanded Panel | exact | A | pre_advance | standard_dfm | 5.204 | 2.191 | -0.874 | 0.723 | 0.323 | 0.326 | 80 | -0.005 |
| expanded_panel | Expanded Panel | exact | A | pre_advance | bridge | 5.226 | 2.269 | -0.641 | 0.715 | 0.305 | 0.308 | 80 | 0.075 |
| expanded_panel | Expanded Panel | exact | A | pre_advance | ar | 7.201 | 2.518 | 0.135 | 1.0 |  |  | 80 | 0.0 |
| expanded_panel | Expanded Panel | exact | A | pre_advance | revision_dfm | 7.229 | 2.695 | -0.267 | 1.015 | 0.931 | 0.932 | 80 | -0.08 |
| expanded_panel | Expanded Panel | exact | A | pre_advance | release_dfm | 7.336 | 2.691 | -0.354 | 1.025 | 0.499 | 0.501 | 80 | -0.042 |
| expanded_panel | Expanded Panel | exact | S | pre_second | revision_dfm | 0.667 | 0.457 | -0.027 | 0.096 | 0.156 | 0.159 | 80 | -0.004 |
| expanded_panel | Expanded Panel | exact | S | pre_second | release_dfm | 0.671 | 0.457 | -0.029 | 0.095 | 0.156 | 0.159 | 80 | 0.002 |
| expanded_panel | Expanded Panel | exact | S | pre_second | bridge | 5.044 | 2.251 | -0.586 | 0.713 | 0.298 | 0.301 | 80 | 0.048 |
| expanded_panel | Expanded Panel | exact | S | pre_second | standard_dfm | 5.149 | 2.263 | -0.854 | 0.738 | 0.32 | 0.323 | 80 | -0.02 |
| expanded_panel | Expanded Panel | exact | S | pre_second | ar | 7.007 | 2.577 | 0.048 | 1.0 |  |  | 80 | 0.0 |
| expanded_panel | Expanded Panel | exact | T | pre_third | release_dfm | 0.369 | 0.243 | 0.044 | 0.054 | 0.147 | 0.15 | 80 | -0.0 |
| expanded_panel | Expanded Panel | exact | T | pre_third | revision_dfm | 0.373 | 0.246 | 0.047 | 0.053 | 0.147 | 0.15 | 80 | 0.009 |
| expanded_panel | Expanded Panel | exact | T | pre_third | bridge | 5.07 | 2.322 | -0.592 | 0.731 | 0.297 | 0.3 | 80 | 0.02 |
| expanded_panel | Expanded Panel | exact | T | pre_third | standard_dfm | 5.129 | 2.258 | -0.87 | 0.749 | 0.312 | 0.315 | 80 | -0.041 |
| expanded_panel | Expanded Panel | exact | T | pre_third | ar | 6.906 | 2.598 | 0.028 | 1.0 |  |  | 80 | 0.0 |
| expanded_panel | Expanded Panel | pseudo | A | pre_advance | standard_dfm | 5.055 | 2.18 | -0.919 | 0.703 | 0.294 | 0.297 | 80 | -0.011 |
| expanded_panel | Expanded Panel | pseudo | A | pre_advance | bridge | 5.171 | 2.397 | -0.454 | 0.711 | 0.289 | 0.292 | 80 | 0.05 |
| expanded_panel | Expanded Panel | pseudo | A | pre_advance | ar | 7.201 | 2.518 | 0.135 | 1.0 |  |  | 80 | 0.0 |
| expanded_panel | Expanded Panel | pseudo | A | pre_advance | revision_dfm | 7.218 | 2.702 | -0.258 | 1.013 | 0.958 | 0.959 | 80 | -0.076 |
| expanded_panel | Expanded Panel | pseudo | A | pre_advance | release_dfm | 7.326 | 2.701 | -0.343 | 1.023 | 0.535 | 0.538 | 80 | -0.036 |
| expanded_panel | Expanded Panel | pseudo | S | pre_second | release_dfm | 0.67 | 0.457 | -0.029 | 0.095 | 0.156 | 0.159 | 80 | 0.001 |
| expanded_panel | Expanded Panel | pseudo | S | pre_second | revision_dfm | 0.671 | 0.458 | -0.027 | 0.095 | 0.156 | 0.159 | 80 | 0.004 |
| expanded_panel | Expanded Panel | pseudo | S | pre_second | bridge | 5.139 | 2.351 | -0.62 | 0.731 | 0.3 | 0.303 | 80 | 0.017 |
| expanded_panel | Expanded Panel | pseudo | S | pre_second | standard_dfm | 5.194 | 2.292 | -0.861 | 0.743 | 0.324 | 0.327 | 80 | -0.012 |
| expanded_panel | Expanded Panel | pseudo | S | pre_second | ar | 7.007 | 2.577 | 0.048 | 1.0 |  |  | 80 | 0.0 |
| expanded_panel | Expanded Panel | pseudo | T | pre_third | release_dfm | 0.392 | 0.252 | 0.053 | 0.057 | 0.148 | 0.15 | 80 | -0.001 |
| expanded_panel | Expanded Panel | pseudo | T | pre_third | revision_dfm | 0.394 | 0.254 | 0.057 | 0.056 | 0.148 | 0.15 | 80 | 0.006 |
| expanded_panel | Expanded Panel | pseudo | T | pre_third | bridge | 5.07 | 2.323 | -0.64 | 0.729 | 0.301 | 0.304 | 80 | 0.033 |
| expanded_panel | Expanded Panel | pseudo | T | pre_third | standard_dfm | 5.137 | 2.257 | -0.879 | 0.749 | 0.311 | 0.314 | 80 | -0.035 |
| expanded_panel | Expanded Panel | pseudo | T | pre_third | ar | 6.906 | 2.598 | 0.028 | 1.0 |  |  | 80 | 0.0 |
