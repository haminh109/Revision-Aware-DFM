# Table 4. Robustness Winner Summary

Sources: `outputs/frozen/submission_final/headline_point_subsample_robustness.csv` and `outputs/frozen/submission_final/headline_point_scenario_robustness.csv`.

Note: This table combines winner rows from subsample and scenario robustness checks. Full robustness rows are provided in appendix tables.

| robustness_type | robustness_variant | variant_label | snapshot_mode | target_id | model_id | RMSE | MAE | DM_test_small_sample | n_forecasts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scenario | alternative_data_choice | Alternative Data Choice | exact | A | bridge | 4.909 | 2.101 | 0.287 | 80 |
| scenario | alternative_data_choice | Alternative Data Choice | exact | S | release_dfm | 0.67 | 0.459 | 0.159 | 80 |
| scenario | alternative_data_choice | Alternative Data Choice | exact | T | revision_dfm | 0.364 | 0.241 | 0.15 | 80 |
| scenario | alternative_data_choice | Alternative Data Choice | pseudo | A | standard_dfm | 5.045 | 2.221 | 0.297 | 80 |
| scenario | alternative_data_choice | Alternative Data Choice | pseudo | S | revision_dfm | 0.669 | 0.46 | 0.159 | 80 |
| scenario | alternative_data_choice | Alternative Data Choice | pseudo | T | release_dfm | 0.392 | 0.252 | 0.15 | 80 |
| scenario | expanded_panel | Expanded Panel | exact | A | standard_dfm | 5.204 | 2.191 | 0.326 | 80 |
| scenario | expanded_panel | Expanded Panel | exact | S | revision_dfm | 0.667 | 0.457 | 0.159 | 80 |
| scenario | expanded_panel | Expanded Panel | exact | T | release_dfm | 0.369 | 0.243 | 0.15 | 80 |
| scenario | expanded_panel | Expanded Panel | pseudo | A | standard_dfm | 5.055 | 2.18 | 0.297 | 80 |
| scenario | expanded_panel | Expanded Panel | pseudo | S | release_dfm | 0.67 | 0.457 | 0.159 | 80 |
| scenario | expanded_panel | Expanded Panel | pseudo | T | release_dfm | 0.392 | 0.252 | 0.15 | 80 |
| subsample | no_pandemic | Exclude pandemic quarters | exact | A | bridge | 1.984 | 1.438 | 0.519 | 78 |
| subsample | no_pandemic | Exclude pandemic quarters | exact | S | release_dfm | 0.613 | 0.423 | 0.0 | 78 |
| subsample | no_pandemic | Exclude pandemic quarters | exact | T | revision_dfm | 0.364 | 0.239 | 0.0 | 78 |
| subsample | no_pandemic | Exclude pandemic quarters | pseudo | A | ar | 2.182 | 1.5 |  | 78 |
| subsample | no_pandemic | Exclude pandemic quarters | pseudo | S | release_dfm | 0.613 | 0.423 | 0.0 | 78 |
| subsample | no_pandemic | Exclude pandemic quarters | pseudo | T | revision_dfm | 0.389 | 0.249 | 0.0 | 78 |
| subsample | post_gfc | Post-GFC | exact | A | bridge | 5.831 | 2.351 | 0.297 | 60 |
| subsample | post_gfc | Post-GFC | exact | S | release_dfm | 0.582 | 0.399 | 0.175 | 60 |
| subsample | post_gfc | Post-GFC | exact | T | revision_dfm | 0.395 | 0.257 | 0.167 | 60 |
| subsample | post_gfc | Post-GFC | pseudo | A | standard_dfm | 5.633 | 2.309 | 0.292 | 60 |
| subsample | post_gfc | Post-GFC | pseudo | S | revision_dfm | 0.577 | 0.399 | 0.175 | 60 |
| subsample | post_gfc | Post-GFC | pseudo | T | revision_dfm | 0.424 | 0.27 | 0.167 | 60 |
| subsample | pre_gfc | Pre-GFC | exact | A | release_dfm | 1.386 | 1.046 | 0.486 | 12 |
| subsample | pre_gfc | Pre-GFC | exact | S | release_dfm | 0.629 | 0.543 | 0.028 | 12 |
| subsample | pre_gfc | Pre-GFC | exact | T | release_dfm | 0.195 | 0.153 | 0.014 | 12 |
| subsample | pre_gfc | Pre-GFC | pseudo | A | release_dfm | 1.4 | 1.057 | 0.516 | 12 |
| subsample | pre_gfc | Pre-GFC | pseudo | S | release_dfm | 0.629 | 0.544 | 0.028 | 12 |
| subsample | pre_gfc | Pre-GFC | pseudo | T | release_dfm | 0.195 | 0.153 | 0.014 | 12 |
