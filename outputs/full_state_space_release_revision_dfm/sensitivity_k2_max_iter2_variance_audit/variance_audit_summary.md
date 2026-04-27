# Variance Audit

Generated UTC: `2026-04-26T11:05:30+00:00`

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
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 8.0329 | 8.1671 | 8.2143 | 2.8540 | 0.5318 | 0.4826 | 5.9135 | 5.3664 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.0764 | 5.1338 | 5.1557 | 2.2638 | 0.3702 | 0.3285 | 6.8923 | 6.1146 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 4.2293 | 4.3594 | 4.5018 | 2.0885 | 0.2353 | 0.2223 | 9.3927 | 8.8754 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 8.0328 | 8.1672 | 8.2133 | 2.8539 | 0.5393 | 0.4831 | 5.9078 | 5.2919 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.0763 | 5.1338 | 5.1557 | 2.2638 | 0.3701 | 0.3286 | 6.8900 | 6.1166 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 4.2294 | 4.3592 | 4.5018 | 2.0884 | 0.2374 | 0.2234 | 9.3488 | 8.7968 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 11.2323 | 11.3549 | 11.4311 | 3.3680 | 0.5130 | 0.4443 | 7.5801 | 6.5647 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.3893 | 5.4409 | 5.4649 | 2.3311 | 0.4465 | 0.4198 | 5.5530 | 5.2209 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 4.3742 | 4.4848 | 4.6040 | 2.1181 | 0.2676 | 0.2343 | 9.0413 | 7.9138 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 11.2322 | 11.3549 | 11.4298 | 3.3679 | 0.5075 | 0.4404 | 7.6479 | 6.6365 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.3892 | 5.4409 | 5.4649 | 2.3311 | 0.4464 | 0.4201 | 5.5488 | 5.2219 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 4.3742 | 4.4846 | 4.6040 | 2.1181 | 0.2698 | 0.2359 | 8.9794 | 7.8509 | 1.0000 | 1.0000 | 1.0000 |
| midas_umidas | exact | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.4902 | 1.6879 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.8914 | 0.9209 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5217 | 0.9046 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.3176 | 1.6895 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.9139 | 0.9482 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5097 | 0.8772 |  |  |  |  | 0.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 13.7748 | 14.3111 | 14.3995 | 3.7680 | 0.4914 | 0.4571 | 8.2425 | 7.6674 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.2770 | 5.5896 | 5.8560 | 2.3611 | 0.4215 | 0.3677 | 6.4206 | 5.6019 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.8574 | 6.4184 | 6.4913 | 2.5087 | 0.3950 | 0.3505 | 7.1567 | 6.3517 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 13.7744 | 14.3104 | 14.3990 | 3.7680 | 0.4969 | 0.4679 | 8.0521 | 7.5824 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.2769 | 5.5896 | 5.8559 | 2.3611 | 0.4189 | 0.3660 | 6.4519 | 5.6359 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.8585 | 6.4184 | 6.4918 | 2.5088 | 0.3948 | 0.3494 | 7.1803 | 6.3542 | 1.0000 | 1.0000 | 1.0000 |
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
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.9611 | 6.3106 | 6.3524 | 2.4965 | 0.2107 | 0.1852 | 13.4789 | 11.8470 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 6.4315 | 6.4980 | 6.5296 | 2.5474 | 0.0854 | 0.1544 | 16.4985 | 29.8395 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.8451 | 8.0428 | 8.2555 | 2.8364 | 0.6029 | 0.5274 | 5.3780 | 4.7050 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.9611 | 6.3106 | 6.3521 | 2.4965 | 0.2107 | 0.1852 | 13.4788 | 11.8469 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 6.4314 | 6.4981 | 6.5296 | 2.5474 | 0.0854 | 0.1544 | 16.4985 | 29.8394 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.8453 | 8.0426 | 8.2555 | 2.8364 | 0.6029 | 0.5274 | 5.3780 | 4.7049 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 8.0387 | 8.3032 | 8.3629 | 2.8725 | 0.3007 | 0.3186 | 9.0154 | 9.5531 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 6.4093 | 6.4657 | 6.4999 | 2.5417 | 0.0852 | 0.1536 | 16.5426 | 29.8157 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 8.7571 | 8.9569 | 9.1799 | 2.9936 | 0.6498 | 0.5803 | 5.1588 | 4.6069 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 8.0386 | 8.3032 | 8.3627 | 2.8725 | 0.2945 | 0.3165 | 9.0767 | 9.7524 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 6.4093 | 6.4657 | 6.4999 | 2.5417 | 0.0852 | 0.1536 | 16.5426 | 29.8156 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 8.7573 | 8.9567 | 9.1799 | 2.9936 | 0.6499 | 0.5804 | 5.1582 | 4.6062 | 1.0000 | 1.0000 | 1.0000 |
| midas_umidas | exact | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.7500 | 0.6802 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.3750 | 0.4710 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 3.5733 | 3.2902 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.7479 | 0.6809 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.3927 | 0.4806 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 3.5907 | 3.3706 |  |  |  |  | 0.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.9419 | 8.5292 | 8.5866 | 2.8973 | 0.2402 | 0.2423 | 11.9569 | 12.0637 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 8.0381 | 8.5687 | 9.0283 | 2.9231 | 0.1060 | 0.1507 | 19.3928 | 27.5805 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 11.6892 | 12.6752 | 12.7954 | 3.5291 | 0.6809 | 0.5979 | 5.9023 | 5.1826 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.9419 | 8.5292 | 8.5866 | 2.8973 | 0.2405 | 0.2422 | 11.9615 | 12.0452 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 8.0381 | 8.5687 | 9.0282 | 2.9231 | 0.1057 | 0.1507 | 19.3924 | 27.6466 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 11.6908 | 12.6752 | 12.7971 | 3.5292 | 0.6792 | 0.5964 | 5.9179 | 5.1965 | 1.0000 | 1.0000 | 1.0000 |
| no_revision | exact | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2107 | 0.1852 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0854 | 0.1544 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6029 | 0.5274 |  |  |  |  | 0.0000 |
| no_revision | pseudo | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2107 | 0.1852 |  |  |  |  | 0.0000 |

## Covariance Matrix Audit

| model_id | timing_mode | checkpoint_id | n_matrices | share_psd | max_asymmetry | min_eigenvalue_min | min_eigenvalue_median | max_eigenvalue_median |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | 4.0000 | 1.0000 | 0.0000 | 2.9802 | 3.1544 | 23.8155 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | 4.0000 | 1.0000 | 0.0000 | 3.1403 | 3.1723 | 11.5150 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | 4.0000 | 1.0000 | 0.0000 | 2.9600 | 3.0557 | 8.3682 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | 4.0000 | 1.0000 | 0.0000 | 2.9802 | 3.1544 | 23.8135 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | 4.0000 | 1.0000 | 0.0000 | 3.1402 | 3.1723 | 11.5150 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | 4.0000 | 1.0000 | 0.0000 | 2.9601 | 3.0555 | 8.3677 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | 4.0000 | 1.0000 | 0.0000 | 3.0511 | 3.2130 | 24.8903 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | 4.0000 | 1.0000 | 0.0000 | 3.2012 | 3.2295 | 12.9214 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | 4.0000 | 1.0000 | 0.0000 | 3.0340 | 3.1233 | 9.1724 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | 4.0000 | 1.0000 | 0.0000 | 3.0511 | 3.2130 | 24.8903 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | 4.0000 | 1.0000 | 0.0000 | 3.2012 | 3.2295 | 12.9213 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | 4.0000 | 1.0000 | 0.0000 | 3.0341 | 3.1231 | 9.1721 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | 4.0000 | 1.0000 | 0.0000 | 3.5643 | 3.8972 | 29.4693 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | 4.0000 | 1.0000 | 0.0000 | 3.5150 | 3.7342 | 13.1355 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | 4.0000 | 1.0000 | 0.0000 | 3.5348 | 3.8829 | 11.0746 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | 4.0000 | 1.0000 | 0.0000 | 3.5642 | 3.8972 | 29.4662 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | 4.0000 | 1.0000 | 0.0000 | 3.5150 | 3.7342 | 13.1354 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | 4.0000 | 1.0000 | 0.0000 | 3.5354 | 3.8829 | 11.0745 |
| revision_dfm_kalman_em | exact | pre_advance | 4.0000 | 1.0000 | 0.0000 | 3.0049 | 3.0237 | 26.6681 |
| revision_dfm_kalman_em | exact | pre_second | 4.0000 | 1.0000 | 0.0000 | 3.0198 | 3.1170 | 12.9958 |
| revision_dfm_kalman_em | exact | pre_third | 4.0000 | 1.0000 | 0.0000 | 3.0000 | 3.0322 | 9.0864 |
| revision_dfm_kalman_em | pseudo | pre_advance | 4.0000 | 1.0000 | 0.0000 | 3.0049 | 3.0237 | 26.6674 |
| revision_dfm_kalman_em | pseudo | pre_second | 4.0000 | 1.0000 | 0.0000 | 3.0198 | 3.1170 | 12.9959 |
| revision_dfm_kalman_em | pseudo | pre_third | 4.0000 | 1.0000 | 0.0000 | 3.0000 | 3.0323 | 9.0871 |
