# Variance Audit

Generated UTC: `2026-04-26T11:09:49+00:00`

## Interpretation

- `share_positive_variance` and `share_finite_sd` should be 1.0 for state-space density rows.
- `mean_sd_to_rmse` far below 1 indicates under-dispersed predictive intervals; far above 1 indicates overly wide intervals.
- `share_psd` should be 1.0 for serialized release covariance matrices.

## Point Forecast Audit

| model_id | timing_mode | checkpoint_id | target_id | n_forecasts | n_variance | share_positive_variance | share_finite_sd | min_forecast_variance | median_forecast_variance | max_forecast_variance | mean_forecast_sd | empirical_error_sd | RMSE | mean_sd_to_rmse | mean_sd_to_empirical_error_sd | coverage_68 | coverage_90 | model_implied_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ar | exact | pre_advance | A | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.2518 |  |  |  |  | 0.0000 |
| ar | exact | pre_second | S | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.2465 |  |  |  |  | 0.0000 |
| ar | exact | pre_third | T | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.2217 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_advance | A | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.2518 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_second | S | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.2465 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_third | T | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.2217 |  |  |  |  | 0.0000 |
| bridge | exact | pre_advance | A | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.2527 |  |  |  |  | 0.0000 |
| bridge | exact | pre_second | S | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.0718 |  |  |  |  | 0.0000 |
| bridge | exact | pre_third | T | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.0453 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_advance | A | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.3295 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_second | S | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.1244 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_third | T | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.0127 |  |  |  |  | 0.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | A | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 12.9835 | 12.9835 | 12.9835 | 3.6033 |  | 0.3461 | 10.4106 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | S | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 11.1618 | 11.1618 | 11.1618 | 3.3409 |  | 0.1188 | 28.1340 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | T | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 10.4550 | 10.4550 | 10.4550 | 3.2334 |  | 0.0104 | 311.5566 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | A | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 12.9835 | 12.9835 | 12.9835 | 3.6033 |  | 0.3513 | 10.2579 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | S | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 11.1618 | 11.1618 | 11.1618 | 3.3409 |  | 0.1193 | 28.0042 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | T | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 10.4550 | 10.4550 | 10.4550 | 3.2334 |  | 0.0113 | 285.1373 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 17.1807 | 17.1807 | 17.1807 | 4.1450 |  | 0.2539 | 16.3251 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 10.9970 | 10.9970 | 10.9970 | 3.3162 |  | 0.1680 | 19.7447 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 10.2349 | 10.2349 | 10.2349 | 3.1992 |  | 0.0233 | 137.5026 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 17.1807 | 17.1807 | 17.1807 | 4.1450 |  | 0.2605 | 15.9144 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | S | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 10.9970 | 10.9970 | 10.9970 | 3.3162 |  | 0.1684 | 19.6902 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | T | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 10.2349 | 10.2349 | 10.2349 | 3.1992 |  | 0.0223 | 143.2228 |  | 1.0000 | 1.0000 | 1.0000 |
| midas_umidas | exact | pre_advance | A | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.1015 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_second | S | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 1.7929 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_third | T | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 1.4545 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_advance | A | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.1283 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_second | S | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 1.8471 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_third | T | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 1.4587 |  |  |  |  | 0.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | A | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 17.1590 | 17.1590 | 17.1590 | 4.1423 |  | 0.4980 | 8.3188 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | S | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 10.2059 | 10.2059 | 10.2059 | 3.1947 |  | 0.0098 | 325.7454 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | T | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 11.4398 | 11.4398 | 11.4398 | 3.3823 |  | 0.1165 | 29.0237 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | A | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 17.1585 | 17.1585 | 17.1585 | 4.1423 |  | 0.4923 | 8.4141 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | S | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 10.2057 | 10.2057 | 10.2057 | 3.1946 |  | 0.0090 | 353.9538 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | T | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 11.4398 | 11.4398 | 11.4398 | 3.3823 |  | 0.1115 | 30.3398 |  | 1.0000 | 1.0000 | 1.0000 |
| no_revision | exact | pre_advance | A | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.1930 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_second | S | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.0939 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_third | T | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.1044 |  |  |  |  | 0.0000 |
| no_revision | pseudo | pre_advance | A | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.1930 |  |  |  |  | 0.0000 |

## Revision Forecast Audit

| model_id | timing_mode | checkpoint_id | revision_target_id | n_forecasts | n_variance | share_positive_variance | share_finite_sd | min_forecast_variance | median_forecast_variance | max_forecast_variance | mean_forecast_sd | empirical_error_sd | RMSE | mean_sd_to_rmse | mean_sd_to_empirical_error_sd | coverage_68 | coverage_90 | model_implied_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ar | exact | pre_advance | DELTA_SA | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.0053 |  |  |  |  | 0.0000 |
| ar | exact | pre_second | DELTA_TS | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.0248 |  |  |  |  | 0.0000 |
| ar | exact | pre_third | DELTA_MT | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.9346 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_advance | DELTA_SA | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.0053 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_second | DELTA_TS | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.0248 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_third | DELTA_MT | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.9346 |  |  |  |  | 0.0000 |
| bridge | exact | pre_advance | DELTA_SA | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.0131 |  |  |  |  | 0.0000 |
| bridge | exact | pre_second | DELTA_TS | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.0277 |  |  |  |  | 0.0000 |
| bridge | exact | pre_third | DELTA_MT | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.7275 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_advance | DELTA_SA | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.0164 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_second | DELTA_TS | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.0224 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_third | DELTA_MT | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.7331 |  |  |  |  | 0.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | DELTA_SA | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 15.9726 | 15.9726 | 15.9726 | 3.9966 |  | 0.0939 | 42.5620 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | DELTA_TS | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 16.3018 | 16.3018 | 16.3018 | 4.0375 |  | 0.1044 | 38.6738 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | DELTA_MT | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 17.7440 | 17.7440 | 17.7440 | 4.2124 |  | 0.5985 | 7.0382 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 15.9726 | 15.9726 | 15.9726 | 3.9966 |  | 0.0939 | 42.5620 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | DELTA_TS | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 16.3017 | 16.3017 | 16.3017 | 4.0375 |  | 0.1044 | 38.6738 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | DELTA_MT | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 17.7440 | 17.7440 | 17.7440 | 4.2124 |  | 0.5985 | 7.0382 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | DELTA_SA | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 18.2873 | 18.2873 | 18.2873 | 4.2764 |  | 0.0009 | 5029.3310 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | DELTA_TS | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 15.8093 | 15.8093 | 15.8093 | 3.9761 |  | 0.1039 | 38.2800 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | DELTA_MT | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 18.6565 | 18.6565 | 18.6565 | 4.3193 |  | 0.6603 | 6.5410 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | DELTA_SA | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 18.2873 | 18.2873 | 18.2873 | 4.2764 |  | 0.0003 | 13629.1819 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | DELTA_TS | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 15.8093 | 15.8093 | 15.8093 | 3.9761 |  | 0.1039 | 38.2795 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | DELTA_MT | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 18.6565 | 18.6565 | 18.6565 | 4.3193 |  | 0.6604 | 6.5406 |  | 1.0000 | 1.0000 | 1.0000 |
| midas_umidas | exact | pre_advance | DELTA_SA | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 1.2791 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_second | DELTA_TS | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.8707 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_third | DELTA_MT | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 5.9443 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_advance | DELTA_SA | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 1.2831 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_second | DELTA_TS | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.8991 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_third | DELTA_MT | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 5.9543 |  |  |  |  | 0.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | DELTA_SA | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 17.5393 | 17.5393 | 17.5393 | 4.1880 |  | 0.0754 | 55.5477 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | DELTA_TS | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 16.4206 | 16.4206 | 16.4206 | 4.0522 |  | 0.0640 | 63.2916 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | DELTA_MT | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 21.5700 | 21.5700 | 21.5700 | 4.6444 |  | 0.6490 | 7.1566 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | DELTA_SA | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 17.5394 | 17.5394 | 17.5394 | 4.1880 |  | 0.0753 | 55.6174 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | DELTA_TS | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 16.4204 | 16.4204 | 16.4204 | 4.0522 |  | 0.0638 | 63.4959 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | DELTA_MT | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 21.5700 | 21.5700 | 21.5700 | 4.6443 |  | 0.6482 | 7.1655 |  | 1.0000 | 1.0000 | 1.0000 |
| no_revision | exact | pre_advance | DELTA_SA | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.0939 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_second | DELTA_TS | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.1044 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_third | DELTA_MT | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.5985 |  |  |  |  | 0.0000 |
| no_revision | pseudo | pre_advance | DELTA_SA | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.0939 |  |  |  |  | 0.0000 |

## Covariance Matrix Audit

| model_id | timing_mode | checkpoint_id | n_matrices | share_psd | max_asymmetry | min_eigenvalue_min | min_eigenvalue_median | max_eigenvalue_median |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | 1.0000 | 1.0000 | 0.0000 | 7.9681 | 7.9681 | 28.8022 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | 1.0000 | 1.0000 | 0.0000 | 7.9547 | 7.9547 | 20.8129 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | 1.0000 | 1.0000 | 0.0000 | 7.9430 | 7.9430 | 17.3885 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | 1.0000 | 1.0000 | 0.0000 | 7.9681 | 7.9681 | 28.8022 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | 1.0000 | 1.0000 | 0.0000 | 7.9547 | 7.9547 | 20.8129 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | 1.0000 | 1.0000 | 0.0000 | 7.9430 | 7.9430 | 17.3885 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | 1.0000 | 1.0000 | 0.0000 | 7.9038 | 7.9038 | 30.7543 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | 1.0000 | 1.0000 | 0.0000 | 7.8996 | 7.8996 | 21.2028 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | 1.0000 | 1.0000 | 0.0000 | 7.8867 | 7.8867 | 17.6298 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | 1.0000 | 1.0000 | 0.0000 | 7.9038 | 7.9038 | 30.7542 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | 1.0000 | 1.0000 | 0.0000 | 7.8996 | 7.8996 | 21.2029 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | 1.0000 | 1.0000 | 0.0000 | 7.8867 | 7.8867 | 17.6298 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | 1.0000 | 1.0000 | 0.0000 | 8.4120 | 8.4120 | 29.1272 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | 1.0000 | 1.0000 | 0.0000 | 7.6606 | 7.6606 | 18.8762 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | 1.0000 | 1.0000 | 0.0000 | 8.3803 | 8.3803 | 17.5516 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | 1.0000 | 1.0000 | 0.0000 | 8.4120 | 8.4120 | 29.1253 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | 1.0000 | 1.0000 | 0.0000 | 7.6605 | 7.6605 | 18.8756 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | 1.0000 | 1.0000 | 0.0000 | 8.3802 | 8.3802 | 17.5515 |
| revision_dfm_kalman_em | exact | pre_advance | 1.0000 | 1.0000 | 0.0000 | 7.2063 | 7.2063 | 31.4421 |
| revision_dfm_kalman_em | exact | pre_second | 1.0000 | 1.0000 | 0.0000 | 7.8614 | 7.8614 | 21.5967 |
| revision_dfm_kalman_em | exact | pre_third | 1.0000 | 1.0000 | 0.0000 | 7.1901 | 7.1901 | 16.6824 |
| revision_dfm_kalman_em | pseudo | pre_advance | 1.0000 | 1.0000 | 0.0000 | 7.2063 | 7.2063 | 31.4420 |
| revision_dfm_kalman_em | pseudo | pre_second | 1.0000 | 1.0000 | 0.0000 | 7.8614 | 7.8614 | 21.5968 |
| revision_dfm_kalman_em | pseudo | pre_third | 1.0000 | 1.0000 | 0.0000 | 7.1901 | 7.1901 | 16.6824 |
