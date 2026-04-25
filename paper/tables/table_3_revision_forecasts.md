# Table 3. GDP Release-Revision Forecasting Performance

Source: `outputs/frozen/submission_final/headline_revision_results.csv`.

Note: Revision forecasts are supporting evidence; they should not be interpreted as the central dominance claim of the paper.

| snapshot_mode | target_id | checkpoint_id | model_id | RMSE | MAE | bias | sign_accuracy | DM_test_small_sample | n_forecasts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exact | DELTA_SA | pre_advance | revision_dfm | 0.57 | 0.4 | 0.066 | 0.392 |  | 80 |
| pseudo | DELTA_SA | pre_advance | revision_dfm | 0.57 | 0.4 | 0.066 | 0.392 |  | 80 |
| exact | DELTA_TS | pre_second | revision_dfm | 0.361 | 0.238 | 0.054 | 0.405 |  | 80 |
| pseudo | DELTA_TS | pre_second | revision_dfm | 0.37 | 0.242 | 0.063 | 0.405 |  | 80 |
