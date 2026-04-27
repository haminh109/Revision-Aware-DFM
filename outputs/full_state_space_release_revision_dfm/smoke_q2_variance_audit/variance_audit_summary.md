# Variance Audit

Generated UTC: `2026-04-25T15:12:05+00:00`

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
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | A | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 8.2960 | 8.2960 | 8.2960 | 2.8803 |  | 0.2634 | 10.9362 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | S | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 5.2549 | 5.2549 | 5.2549 | 2.2924 |  | 0.0037 | 624.1386 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | T | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 4.6327 | 4.6327 | 4.6327 | 2.1524 |  | 0.0905 | 23.7713 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | A | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 8.2960 | 8.2960 | 8.2960 | 2.8803 |  | 0.2697 | 10.6784 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | S | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 5.2549 | 5.2549 | 5.2549 | 2.2924 |  | 0.0052 | 441.7337 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | T | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 4.6327 | 4.6327 | 4.6327 | 2.1524 |  | 0.0913 | 23.5852 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 11.4869 | 11.4869 | 11.4869 | 3.3892 |  | 0.1131 | 29.9669 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 5.5341 | 5.5341 | 5.5341 | 2.3525 |  | 0.1095 | 21.4900 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 4.7206 | 4.7206 | 4.7206 | 2.1727 |  | 0.0279 | 77.9365 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 11.4869 | 11.4869 | 11.4869 | 3.3892 |  | 0.1206 | 28.1032 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | S | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 5.5341 | 5.5341 | 5.5341 | 2.3525 |  | 0.1109 | 21.2188 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | T | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 4.7206 | 4.7206 | 4.7206 | 2.1727 |  | 0.0286 | 75.9805 |  | 1.0000 | 1.0000 | 1.0000 |
| midas_umidas | exact | pre_advance | A | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.7891 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_second | S | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 1.3700 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_third | T | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.3576 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_advance | A | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.8088 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_second | S | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 1.3948 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_third | T | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.3518 |  |  |  |  | 0.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | A | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 14.4961 | 14.4961 | 14.4961 | 3.8074 |  | 0.2477 | 15.3716 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | S | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 5.0539 | 5.0539 | 5.0539 | 2.2481 |  | 0.1122 | 20.0423 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | T | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 6.7208 | 6.7208 | 6.7208 | 2.5925 |  | 0.0260 | 99.7077 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | A | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 14.4949 | 14.4949 | 14.4949 | 3.8072 |  | 0.2367 | 16.0855 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | S | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 5.0538 | 5.0538 | 5.0538 | 2.2481 |  | 0.1140 | 19.7173 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | T | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 6.7208 | 6.7208 | 6.7208 | 2.5924 |  | 0.0199 | 130.2136 |  | 1.0000 | 1.0000 | 1.0000 |
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
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | DELTA_SA | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 6.5249 | 6.5249 | 6.5249 | 2.5544 |  | 0.0939 | 27.2033 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | DELTA_TS | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 6.6878 | 6.6878 | 6.6878 | 2.5861 |  | 0.1044 | 24.7709 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | DELTA_MT | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 8.4656 | 8.4656 | 8.4656 | 2.9096 |  | 0.5985 | 4.8615 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 6.5249 | 6.5249 | 6.5249 | 2.5544 |  | 0.0939 | 27.2033 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | DELTA_TS | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 6.6878 | 6.6878 | 6.6878 | 2.5861 |  | 0.1044 | 24.7709 |  | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | DELTA_MT | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 8.4656 | 8.4656 | 8.4656 | 2.9096 |  | 0.5985 | 4.8615 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | DELTA_SA | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 8.4804 | 8.4804 | 8.4804 | 2.9121 |  | 0.0591 | 49.2709 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | DELTA_TS | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 6.6393 | 6.6393 | 6.6393 | 2.5767 |  | 0.1035 | 24.9051 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | DELTA_MT | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 9.3944 | 9.3944 | 9.3944 | 3.0650 |  | 0.6785 | 4.5175 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | DELTA_SA | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 8.4804 | 8.4804 | 8.4804 | 2.9121 |  | 0.0580 | 50.1891 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | DELTA_TS | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 6.6393 | 6.6393 | 6.6393 | 2.5767 |  | 0.1035 | 24.9049 |  | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | DELTA_MT | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 9.3944 | 9.3944 | 9.3944 | 3.0650 |  | 0.6785 | 4.5175 |  | 1.0000 | 1.0000 | 1.0000 |
| midas_umidas | exact | pre_advance | DELTA_SA | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.3403 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_second | DELTA_TS | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.1160 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_third | DELTA_MT | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 1.6343 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_advance | DELTA_SA | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.3458 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_second | DELTA_TS | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.1144 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_third | DELTA_MT | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 1.6536 |  |  |  |  | 0.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | DELTA_SA | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 8.8726 | 8.8726 | 8.8726 | 2.9787 |  | 0.0055 | 543.1470 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | DELTA_TS | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 7.6366 | 7.6366 | 7.6366 | 2.7634 |  | 0.0509 | 54.3353 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | DELTA_MT | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 13.2511 | 13.2511 | 13.2511 | 3.6402 |  | 0.6698 | 5.4349 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | DELTA_SA | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 8.8726 | 8.8726 | 8.8726 | 2.9787 |  | 0.0059 | 503.2365 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | DELTA_TS | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 7.6365 | 7.6365 | 7.6365 | 2.7634 |  | 0.0501 | 55.1360 |  | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | DELTA_MT | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 13.2511 | 13.2511 | 13.2511 | 3.6402 |  | 0.6679 | 5.4502 |  | 1.0000 | 1.0000 | 1.0000 |
| no_revision | exact | pre_advance | DELTA_SA | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.0939 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_second | DELTA_TS | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.1044 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_third | DELTA_MT | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.5985 |  |  |  |  | 0.0000 |
| no_revision | pseudo | pre_advance | DELTA_SA | 1.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  |  | 0.0939 |  |  |  |  | 0.0000 |

## Covariance Matrix Audit

| model_id | timing_mode | checkpoint_id | n_matrices | share_psd | max_asymmetry | min_eigenvalue_min | min_eigenvalue_median | max_eigenvalue_median |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | 1.0000 | 1.0000 | 0.0000 | 3.2608 | 3.2608 | 23.9967 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | 1.0000 | 1.0000 | 0.0000 | 3.2594 | 3.2594 | 11.7185 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | 1.0000 | 1.0000 | 0.0000 | 3.2531 | 3.2531 | 8.8026 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | 1.0000 | 1.0000 | 0.0000 | 3.2608 | 3.2608 | 23.9967 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | 1.0000 | 1.0000 | 0.0000 | 3.2594 | 3.2594 | 11.7185 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | 1.0000 | 1.0000 | 0.0000 | 3.2531 | 3.2531 | 8.8026 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | 1.0000 | 1.0000 | 0.0000 | 3.3170 | 3.3170 | 25.1246 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | 1.0000 | 1.0000 | 0.0000 | 3.3160 | 3.3160 | 13.0516 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | 1.0000 | 1.0000 | 0.0000 | 3.3116 | 3.3116 | 9.5491 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | 1.0000 | 1.0000 | 0.0000 | 3.3170 | 3.3170 | 25.1246 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | 1.0000 | 1.0000 | 0.0000 | 3.3161 | 3.3161 | 13.0517 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | 1.0000 | 1.0000 | 0.0000 | 3.3116 | 3.3116 | 9.5491 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | 1.0000 | 1.0000 | 0.0000 | 4.0883 | 4.0883 | 29.8434 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | 1.0000 | 1.0000 | 0.0000 | 3.3489 | 3.3489 | 12.2082 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | 1.0000 | 1.0000 | 0.0000 | 4.0731 | 4.0731 | 11.4902 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | 1.0000 | 1.0000 | 0.0000 | 4.0882 | 4.0882 | 29.8387 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | 1.0000 | 1.0000 | 0.0000 | 3.3488 | 3.3488 | 12.2076 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | 1.0000 | 1.0000 | 0.0000 | 4.0731 | 4.0731 | 11.4901 |
| revision_dfm_kalman_em | exact | pre_advance | 1.0000 | 1.0000 | 0.0000 | 2.9109 | 2.9109 | 26.2759 |
| revision_dfm_kalman_em | exact | pre_second | 1.0000 | 1.0000 | 0.0000 | 3.3021 | 3.3021 | 13.3641 |
| revision_dfm_kalman_em | exact | pre_third | 1.0000 | 1.0000 | 0.0000 | 2.9055 | 2.9055 | 8.8029 |
| revision_dfm_kalman_em | pseudo | pre_advance | 1.0000 | 1.0000 | 0.0000 | 2.9109 | 2.9109 | 26.2758 |
| revision_dfm_kalman_em | pseudo | pre_second | 1.0000 | 1.0000 | 0.0000 | 3.3021 | 3.3021 | 13.3642 |
| revision_dfm_kalman_em | pseudo | pre_third | 1.0000 | 1.0000 | 0.0000 | 2.9055 | 2.9055 | 8.8029 |
