# Variance Audit

Generated UTC: `2026-04-26T11:07:16+00:00`

## Interpretation

- `share_positive_variance` and `share_finite_sd` should be 1.0 for state-space density rows.
- `mean_sd_to_rmse` far below 1 indicates under-dispersed predictive intervals; far above 1 indicates overly wide intervals.
- `share_psd` should be 1.0 for serialized release covariance matrices.

## Point Forecast Audit

| model_id | timing_mode | checkpoint_id | target_id | n_forecasts | n_variance | share_positive_variance | share_finite_sd | min_forecast_variance | median_forecast_variance | max_forecast_variance | mean_forecast_sd | empirical_error_sd | RMSE | mean_sd_to_rmse | mean_sd_to_empirical_error_sd | coverage_68 | coverage_90 | model_implied_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ar | exact | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4432 | 0.9107 |  |  |  |  | 0.0000 |
| ar | exact | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5284 | 0.7487 |  |  |  |  | 0.0000 |
| ar | exact | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6282 | 0.5853 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4432 | 0.9107 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5284 | 0.7487 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6282 | 0.5853 |  |  |  |  | 0.0000 |
| bridge | exact | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.2191 | 1.1097 |  |  |  |  | 0.0000 |
| bridge | exact | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.7918 | 0.9883 |  |  |  |  | 0.0000 |
| bridge | exact | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.7147 | 1.1406 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.1509 | 1.0501 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.8299 | 1.0479 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.7095 | 1.1059 |  |  |  |  | 0.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 14.1630 | 15.3242 | 16.6376 | 3.9165 | 0.7056 | 0.6294 | 6.2224 | 5.5506 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 11.5218 | 11.6263 | 11.6422 | 3.4065 | 0.5059 | 0.4517 | 7.5411 | 6.7339 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 10.6496 | 13.4715 | 13.5114 | 3.5700 | 0.4131 | 0.4306 | 8.2906 | 8.6426 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 14.1624 | 15.3237 | 16.6374 | 3.9164 | 0.6864 | 0.6176 | 6.3412 | 5.7058 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 11.5223 | 11.6263 | 11.6434 | 3.4065 | 0.5053 | 0.4511 | 7.5521 | 6.7417 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 10.6497 | 13.4701 | 13.5075 | 3.5697 | 0.4179 | 0.4315 | 8.2730 | 8.5429 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 19.0774 | 20.0918 | 21.3262 | 4.4869 | 0.8313 | 0.7935 | 5.6548 | 5.3976 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 11.8162 | 11.8906 | 11.9082 | 3.4462 | 0.5414 | 0.4740 | 7.2700 | 6.3657 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 10.7546 | 13.1638 | 13.1825 | 3.5416 | 0.4145 | 0.4168 | 8.4978 | 8.5453 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 19.0770 | 20.0911 | 21.3259 | 4.4869 | 0.8007 | 0.7787 | 5.7621 | 5.6039 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 11.8167 | 11.8911 | 11.9083 | 3.4463 | 0.5408 | 0.4734 | 7.2791 | 6.3725 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 10.7547 | 13.1625 | 13.1786 | 3.5414 | 0.4190 | 0.4179 | 8.4749 | 8.4512 | 1.0000 | 1.0000 | 1.0000 |
| midas_umidas | exact | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.5988 | 1.5006 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2688 | 0.3365 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5216 | 0.5210 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.5373 | 1.4123 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2939 | 0.3261 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5278 | 0.5210 |  |  |  |  | 0.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 31.2297 | 33.3705 | 35.4544 | 5.7726 | 0.3191 | 0.5371 | 10.7474 | 18.0898 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 17.8499 | 17.8755 | 17.8797 | 4.2273 | 0.4266 | 0.3758 | 11.2474 | 9.9087 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 14.2482 | 17.0466 | 19.8172 | 4.1141 | 0.3568 | 0.3976 | 10.3463 | 11.5309 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 31.2290 | 33.3701 | 35.4544 | 5.7726 | 0.3086 | 0.5414 | 10.6626 | 18.7087 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 17.8509 | 17.8763 | 17.8808 | 4.2274 | 0.4259 | 0.3759 | 11.2448 | 9.9251 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 14.2485 | 17.0463 | 19.8259 | 4.1144 | 0.3680 | 0.3987 | 10.3195 | 11.1791 | 1.0000 | 1.0000 | 1.0000 |
| no_revision | exact | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4432 | 0.9107 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2107 | 0.1852 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0854 | 0.1544 |  |  |  |  | 0.0000 |
| no_revision | pseudo | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4432 | 0.9107 |  |  |  |  | 0.0000 |

## Revision Forecast Audit

| model_id | timing_mode | checkpoint_id | revision_target_id | n_forecasts | n_variance | share_positive_variance | share_finite_sd | min_forecast_variance | median_forecast_variance | max_forecast_variance | mean_forecast_sd | empirical_error_sd | RMSE | mean_sd_to_rmse | mean_sd_to_empirical_error_sd | coverage_68 | coverage_90 | model_implied_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ar | exact | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.1712 | 0.2763 |  |  |  |  | 0.0000 |
| ar | exact | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2362 | 0.4287 |  |  |  |  | 0.0000 |
| ar | exact | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 20.1462 | 23.1268 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.1712 | 0.2763 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2362 | 0.4287 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 20.1462 | 23.1268 |  |  |  |  | 0.0000 |
| bridge | exact | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2361 | 0.2512 |  |  |  |  | 0.0000 |
| bridge | exact | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2752 | 0.2825 |  |  |  |  | 0.0000 |
| bridge | exact | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.9995 | 1.3287 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2359 | 0.2597 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2710 | 0.2846 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.9425 | 1.3247 |  |  |  |  | 0.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 17.0116 | 19.3612 | 21.7383 | 4.3929 | 0.2107 | 0.1852 | 23.7173 | 20.8459 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 16.5784 | 16.7097 | 16.7693 | 4.0856 | 0.0854 | 0.1544 | 26.4605 | 47.8569 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 17.1009 | 22.4902 | 22.5491 | 4.5922 | 0.6029 | 0.5274 | 8.7070 | 7.6172 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 17.0113 | 19.3609 | 21.7380 | 4.3928 | 0.2107 | 0.1852 | 23.7172 | 20.8458 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 16.5791 | 16.7099 | 16.7713 | 4.0856 | 0.0854 | 0.1544 | 26.4611 | 47.8579 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 17.1009 | 22.4878 | 22.5438 | 4.5919 | 0.6029 | 0.5274 | 8.7065 | 7.6168 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 21.4633 | 23.3575 | 25.2970 | 4.8301 | 0.3199 | 0.3465 | 13.9379 | 15.1005 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 16.3279 | 16.4240 | 16.4536 | 4.0506 | 0.0855 | 0.1533 | 26.4215 | 47.3515 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 20.9561 | 26.4934 | 26.5578 | 5.0064 | 0.6473 | 0.5750 | 8.7069 | 7.7337 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 21.4630 | 23.3571 | 25.2968 | 4.8301 | 0.3129 | 0.3440 | 14.0421 | 15.4379 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 16.3285 | 16.4242 | 16.4554 | 4.0507 | 0.0855 | 0.1533 | 26.4222 | 47.3525 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 20.9562 | 26.4907 | 26.5536 | 5.0062 | 0.6472 | 0.5749 | 8.7083 | 7.7350 | 1.0000 | 1.0000 | 1.0000 |
| midas_umidas | exact | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5800 | 0.8867 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4515 | 0.5553 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 2.0777 | 1.8459 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6016 | 0.8439 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4671 | 0.5564 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 2.0449 | 1.8035 |  |  |  |  | 0.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 20.8367 | 24.4900 | 28.0940 | 4.9339 | 0.2415 | 0.2351 | 20.9823 | 20.4275 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 29.6088 | 29.6931 | 29.7204 | 5.4478 | 0.1168 | 0.1755 | 31.0457 | 46.6450 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 28.4760 | 34.3177 | 40.1996 | 5.8377 | 0.6563 | 0.5712 | 10.2203 | 8.8946 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 20.8366 | 24.4904 | 28.0936 | 4.9339 | 0.2423 | 0.2352 | 20.9804 | 20.3664 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 29.6112 | 29.6946 | 29.7226 | 5.4480 | 0.1169 | 0.1757 | 31.0004 | 46.5988 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 28.4752 | 34.3303 | 40.1991 | 5.8382 | 0.6556 | 0.5706 | 10.2310 | 8.9052 | 1.0000 | 1.0000 | 1.0000 |
| no_revision | exact | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2107 | 0.1852 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0854 | 0.1544 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6029 | 0.5274 |  |  |  |  | 0.0000 |
| no_revision | pseudo | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2107 | 0.1852 |  |  |  |  | 0.0000 |

## Covariance Matrix Audit

| model_id | timing_mode | checkpoint_id | n_matrices | share_psd | max_asymmetry | min_eigenvalue_min | min_eigenvalue_median | max_eigenvalue_median |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | 4.0000 | 1.0000 | 0.0000 | 8.3520 | 9.5269 | 31.6277 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | 4.0000 | 1.0000 | 0.0000 | 8.2830 | 8.3482 | 21.8044 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | 4.0000 | 1.0000 | 0.0000 | 8.2235 | 10.6458 | 21.7952 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | 4.0000 | 1.0000 | 0.0000 | 8.3516 | 9.5268 | 31.6251 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | 4.0000 | 1.0000 | 0.0000 | 8.2833 | 8.3483 | 21.8054 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | 4.0000 | 1.0000 | 0.0000 | 8.2236 | 10.6446 | 21.7904 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | 4.0000 | 1.0000 | 0.0000 | 8.2195 | 9.2526 | 32.9667 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | 4.0000 | 1.0000 | 0.0000 | 8.1605 | 8.2087 | 24.1999 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | 4.0000 | 1.0000 | 0.0000 | 8.1198 | 10.2480 | 23.3162 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | 4.0000 | 1.0000 | 0.0000 | 8.2189 | 9.2525 | 32.9642 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | 4.0000 | 1.0000 | 0.0000 | 8.1608 | 8.2088 | 24.2007 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | 4.0000 | 1.0000 | 0.0000 | 8.1198 | 10.2468 | 23.3127 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | 4.0000 | 1.0000 | 0.0000 | 9.1268 | 11.1100 | 59.3496 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | 4.0000 | 1.0000 | 0.0000 | 12.9899 | 13.0188 | 36.5568 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | 4.0000 | 1.0000 | 0.0000 | 8.9938 | 10.9335 | 27.9340 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | 4.0000 | 1.0000 | 0.0000 | 9.1268 | 11.1101 | 59.3477 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | 4.0000 | 1.0000 | 0.0000 | 12.9909 | 13.0194 | 36.5579 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | 4.0000 | 1.0000 | 0.0000 | 8.9941 | 10.9334 | 27.9405 |
| revision_dfm_kalman_em | exact | pre_advance | 4.0000 | 1.0000 | 0.0000 | 7.7839 | 8.9415 | 35.3239 |
| revision_dfm_kalman_em | exact | pre_second | 4.0000 | 1.0000 | 0.0000 | 7.7647 | 8.9456 | 26.3544 |
| revision_dfm_kalman_em | exact | pre_third | 4.0000 | 1.0000 | 0.0000 | 7.7275 | 8.8779 | 21.4191 |
| revision_dfm_kalman_em | pseudo | pre_advance | 4.0000 | 1.0000 | 0.0000 | 7.7838 | 8.9413 | 35.3231 |
| revision_dfm_kalman_em | pseudo | pre_second | 4.0000 | 1.0000 | 0.0000 | 7.7652 | 8.9459 | 26.3560 |
| revision_dfm_kalman_em | pseudo | pre_third | 4.0000 | 1.0000 | 0.0000 | 7.7276 | 8.8766 | 21.4169 |
