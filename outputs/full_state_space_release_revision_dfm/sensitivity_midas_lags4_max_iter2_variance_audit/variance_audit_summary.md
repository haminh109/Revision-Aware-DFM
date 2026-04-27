# Variance Audit

Generated UTC: `2026-04-26T11:06:41+00:00`

## Interpretation

- `share_positive_variance` and `share_finite_sd` should be 1.0 for state-space density rows.
- `mean_sd_to_rmse` far below 1 indicates under-dispersed predictive intervals; far above 1 indicates overly wide intervals.
- `share_psd` should be 1.0 for serialized release covariance matrices.

## Point Forecast Audit

| model_id | timing_mode | checkpoint_id | target_id | n_forecasts | n_variance | share_positive_variance | share_finite_sd | min_forecast_variance | median_forecast_variance | max_forecast_variance | mean_forecast_sd | empirical_error_sd | RMSE | mean_sd_to_rmse | mean_sd_to_empirical_error_sd | coverage_68 | coverage_90 | model_implied_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ar | exact | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6143 | 0.5449 |  |  |  |  | 0.0000 |
| ar | exact | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.8093 | 0.7383 |  |  |  |  | 0.0000 |
| ar | exact | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.7960 | 0.7105 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6143 | 0.5449 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.8093 | 0.7383 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.7960 | 0.7105 |  |  |  |  | 0.0000 |
| bridge | exact | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6000 | 0.5314 |  |  |  |  | 0.0000 |
| bridge | exact | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.1510 | 0.1588 |  |  |  |  | 0.0000 |
| bridge | exact | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.3116 | 0.4512 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5596 | 0.5049 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.1937 | 0.2284 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.3305 | 0.4030 |  |  |  |  | 0.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.9096 | 8.3164 | 8.3845 | 2.8689 | 0.5860 | 0.5310 | 5.4029 | 4.8956 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.2549 | 5.2968 | 5.3344 | 2.3012 | 0.3727 | 0.3280 | 7.0157 | 6.1746 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 4.0934 | 4.3740 | 4.6583 | 2.0906 | 0.2498 | 0.2345 | 8.9138 | 8.3676 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.9095 | 8.3165 | 8.3835 | 2.8689 | 0.5842 | 0.5237 | 5.4782 | 4.9104 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.2549 | 5.2968 | 5.3343 | 2.3012 | 0.3722 | 0.3277 | 7.0225 | 6.1834 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 4.0931 | 4.3737 | 4.6583 | 2.0906 | 0.2520 | 0.2357 | 8.8684 | 8.2950 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 11.0995 | 11.5133 | 11.6057 | 3.3811 | 0.5984 | 0.5184 | 6.5220 | 5.6499 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.5341 | 5.5748 | 5.6105 | 2.3608 | 0.4408 | 0.4078 | 5.7889 | 5.3563 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 4.2623 | 4.5011 | 4.7437 | 2.1211 | 0.2788 | 0.2442 | 8.6858 | 7.6090 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 11.0994 | 11.5134 | 11.6043 | 3.3811 | 0.5833 | 0.5053 | 6.6912 | 5.7966 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.5341 | 5.5747 | 5.6105 | 2.3608 | 0.4402 | 0.4076 | 5.7926 | 5.3632 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 4.2620 | 4.5009 | 4.7437 | 2.1211 | 0.2811 | 0.2459 | 8.6240 | 7.5467 | 1.0000 | 1.0000 | 1.0000 |
| midas_umidas | exact | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 2.0390 | 2.0171 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6460 | 0.7659 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.3249 | 0.5374 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.8912 | 2.0056 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6730 | 0.7805 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2899 | 0.5050 |  |  |  |  | 0.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 13.5129 | 14.5245 | 14.6156 | 3.7803 | 0.3601 | 0.3251 | 11.6272 | 10.4966 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.0539 | 5.6138 | 6.1306 | 2.3646 | 0.3925 | 0.3409 | 6.9366 | 6.0242 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.5980 | 6.7379 | 6.8138 | 2.5420 | 0.3695 | 0.3268 | 7.7794 | 6.8797 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 13.5123 | 14.5233 | 14.6142 | 3.7802 | 0.3703 | 0.3400 | 11.1177 | 10.2070 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.0538 | 5.6137 | 6.1305 | 2.3645 | 0.3885 | 0.3377 | 7.0026 | 6.0857 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.5990 | 6.7378 | 6.8151 | 2.5421 | 0.3687 | 0.3252 | 7.8159 | 6.8948 | 1.0000 | 1.0000 | 1.0000 |
| no_revision | exact | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6674 | 0.5998 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2107 | 0.1852 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0854 | 0.1544 |  |  |  |  | 0.0000 |
| no_revision | pseudo | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6674 | 0.5998 |  |  |  |  | 0.0000 |

## Revision Forecast Audit

| model_id | timing_mode | checkpoint_id | revision_target_id | n_forecasts | n_variance | share_positive_variance | share_finite_sd | min_forecast_variance | median_forecast_variance | max_forecast_variance | mean_forecast_sd | empirical_error_sd | RMSE | mean_sd_to_rmse | mean_sd_to_empirical_error_sd | coverage_68 | coverage_90 | model_implied_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ar | exact | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2209 | 0.2226 |  |  |  |  | 0.0000 |
| ar | exact | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0900 | 0.0984 |  |  |  |  | 0.0000 |
| ar | exact | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5710 | 0.6296 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2209 | 0.2226 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0900 | 0.0984 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5710 | 0.6296 |  |  |  |  | 0.0000 |
| bridge | exact | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2211 | 0.1963 |  |  |  |  | 0.0000 |
| bridge | exact | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.1314 | 0.2040 |  |  |  |  | 0.0000 |
| bridge | exact | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5680 | 0.5553 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2317 | 0.2035 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.1325 | 0.2104 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5726 | 0.5597 |  |  |  |  | 0.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.7585 | 6.5441 | 6.5927 | 2.5209 | 0.2107 | 0.1852 | 13.6105 | 11.9627 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 6.6878 | 6.7407 | 6.7871 | 2.5960 | 0.0854 | 0.1544 | 16.8130 | 30.4083 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.6343 | 8.0651 | 8.4929 | 2.8388 | 0.6029 | 0.5274 | 5.3826 | 4.7089 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.7585 | 6.5441 | 6.5925 | 2.5209 | 0.2107 | 0.1852 | 13.6104 | 11.9626 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 6.6878 | 6.7406 | 6.7870 | 2.5960 | 0.0854 | 0.1544 | 16.8130 | 30.4082 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.6340 | 8.0649 | 8.4929 | 2.8388 | 0.6029 | 0.5274 | 5.3825 | 4.7089 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.8870 | 8.5002 | 8.5588 | 2.8912 | 0.2924 | 0.3100 | 9.3259 | 9.8880 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 6.6393 | 6.6880 | 6.7315 | 2.5859 | 0.0853 | 0.1537 | 16.8238 | 30.3299 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 8.5361 | 8.9814 | 9.4230 | 2.9959 | 0.6415 | 0.5726 | 5.2318 | 4.6705 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.8870 | 8.5002 | 8.5585 | 2.8912 | 0.2852 | 0.3074 | 9.4047 | 10.1370 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 6.6393 | 6.6879 | 6.7314 | 2.5858 | 0.0853 | 0.1537 | 16.8236 | 30.3295 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 8.5357 | 8.9813 | 9.4230 | 2.9959 | 0.6415 | 0.5726 | 5.2317 | 4.6703 | 1.0000 | 1.0000 | 1.0000 |
| midas_umidas | exact | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4719 | 0.4098 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.1537 | 0.3679 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.3064 | 1.2330 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4809 | 0.4165 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.1408 | 0.3719 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.1391 | 1.1751 |  |  |  |  | 0.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.6351 | 8.8947 | 8.9548 | 2.9301 | 0.2431 | 0.2389 | 12.2639 | 12.0552 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.6366 | 8.6157 | 9.5280 | 2.9283 | 0.1068 | 0.1503 | 19.4821 | 27.4111 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 11.2061 | 13.2688 | 13.3901 | 3.5730 | 0.6744 | 0.5923 | 6.0324 | 5.2983 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.6350 | 8.8947 | 8.9547 | 2.9301 | 0.2430 | 0.2387 | 12.2744 | 12.0568 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.6365 | 8.6156 | 9.5280 | 2.9283 | 0.1065 | 0.1502 | 19.4923 | 27.5069 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 11.2076 | 13.2688 | 13.3934 | 3.5732 | 0.6724 | 0.5906 | 6.0501 | 5.3140 | 1.0000 | 1.0000 | 1.0000 |
| no_revision | exact | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2107 | 0.1852 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0854 | 0.1544 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6029 | 0.5274 |  |  |  |  | 0.0000 |
| no_revision | pseudo | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2107 | 0.1852 |  |  |  |  | 0.0000 |

## Covariance Matrix Audit

| model_id | timing_mode | checkpoint_id | n_matrices | share_psd | max_asymmetry | min_eigenvalue_min | min_eigenvalue_median | max_eigenvalue_median |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | 4.0000 | 1.0000 | 0.0000 | 2.8790 | 3.2703 | 24.0489 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | 4.0000 | 1.0000 | 0.0000 | 3.2594 | 3.2855 | 11.8043 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | 4.0000 | 1.0000 | 0.0000 | 2.8592 | 3.0641 | 8.3904 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | 4.0000 | 1.0000 | 0.0000 | 2.8790 | 3.2703 | 24.0490 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | 4.0000 | 1.0000 | 0.0000 | 3.2594 | 3.2855 | 11.8041 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | 4.0000 | 1.0000 | 0.0000 | 2.8589 | 3.0639 | 8.3900 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | 4.0000 | 1.0000 | 0.0000 | 2.9613 | 3.3257 | 25.1836 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | 4.0000 | 1.0000 | 0.0000 | 3.3160 | 3.3404 | 13.1389 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | 4.0000 | 1.0000 | 0.0000 | 2.9445 | 3.1352 | 9.1987 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | 4.0000 | 1.0000 | 0.0000 | 2.9613 | 3.3257 | 25.1838 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | 4.0000 | 1.0000 | 0.0000 | 3.3161 | 3.3404 | 13.1388 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | 4.0000 | 1.0000 | 0.0000 | 2.9443 | 3.1351 | 9.1984 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | 4.0000 | 1.0000 | 0.0000 | 3.3963 | 4.0989 | 29.8997 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | 4.0000 | 1.0000 | 0.0000 | 3.3489 | 3.7510 | 13.1721 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | 4.0000 | 1.0000 | 0.0000 | 3.3676 | 4.0838 | 11.5081 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | 4.0000 | 1.0000 | 0.0000 | 3.3962 | 4.0989 | 29.8949 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | 4.0000 | 1.0000 | 0.0000 | 3.3488 | 3.7510 | 13.1718 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | 4.0000 | 1.0000 | 0.0000 | 3.3682 | 4.0838 | 11.5080 |
| revision_dfm_kalman_em | exact | pre_advance | 4.0000 | 1.0000 | 0.0000 | 2.9109 | 2.9337 | 26.4804 |
| revision_dfm_kalman_em | exact | pre_second | 4.0000 | 1.0000 | 0.0000 | 2.9257 | 3.1206 | 13.0111 |
| revision_dfm_kalman_em | exact | pre_third | 4.0000 | 1.0000 | 0.0000 | 2.9055 | 2.9427 | 8.8997 |
| revision_dfm_kalman_em | pseudo | pre_advance | 4.0000 | 1.0000 | 0.0000 | 2.9109 | 2.9336 | 26.4798 |
| revision_dfm_kalman_em | pseudo | pre_second | 4.0000 | 1.0000 | 0.0000 | 2.9257 | 3.1206 | 13.0111 |
| revision_dfm_kalman_em | pseudo | pre_third | 4.0000 | 1.0000 | 0.0000 | 2.9055 | 2.9427 | 8.9002 |
