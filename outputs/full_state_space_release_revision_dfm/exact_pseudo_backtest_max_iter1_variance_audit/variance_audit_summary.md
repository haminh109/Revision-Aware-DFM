# Variance Audit

Generated UTC: `2026-04-26T16:29:06+00:00`

## Interpretation

- `share_positive_variance` and `share_finite_sd` should be 1.0 for state-space density rows.
- `mean_sd_to_rmse` far below 1 indicates under-dispersed predictive intervals; far above 1 indicates overly wide intervals.
- `share_psd` should be 1.0 for serialized release covariance matrices.

## Point Forecast Audit

| model_id | timing_mode | checkpoint_id | target_id | n_forecasts | n_variance | share_positive_variance | share_finite_sd | min_forecast_variance | median_forecast_variance | max_forecast_variance | mean_forecast_sd | empirical_error_sd | RMSE | mean_sd_to_rmse | mean_sd_to_empirical_error_sd | coverage_68 | coverage_90 | model_implied_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ar | exact | pre_advance | A | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4061 | 0.2894 |  |  |  |  | 0.0000 |
| ar | exact | pre_second | S | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.3417 | 0.2417 |  |  |  |  | 0.0000 |
| ar | exact | pre_third | T | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4451 | 0.3282 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_advance | A | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4061 | 0.2894 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_second | S | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.3417 | 0.2417 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_third | T | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4451 | 0.3282 |  |  |  |  | 0.0000 |
| bridge | exact | pre_advance | A | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4741 | 0.3453 |  |  |  |  | 0.0000 |
| bridge | exact | pre_second | S | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.1624 | 0.2191 |  |  |  |  | 0.0000 |
| bridge | exact | pre_third | T | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5307 | 0.4997 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_advance | A | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5096 | 0.3617 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_second | S | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2005 | 0.3016 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_third | T | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4844 | 0.4935 |  |  |  |  | 0.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | A | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 12.9835 | 13.0110 | 13.0384 | 3.6071 | 0.5007 | 0.3542 | 10.1849 | 7.2036 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | S | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 11.1618 | 11.1865 | 11.2112 | 3.3446 | 0.2299 | 0.1683 | 19.8690 | 14.5504 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | T | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 10.4550 | 10.4780 | 10.5010 | 3.2370 | 0.2707 | 0.2781 | 11.6383 | 11.9580 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | A | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 12.9835 | 13.0110 | 13.0384 | 3.6071 | 0.4962 | 0.3509 | 10.2807 | 7.2696 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | S | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 11.1618 | 11.1865 | 11.2111 | 3.3446 | 0.2306 | 0.1688 | 19.8137 | 14.5058 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | T | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 10.4550 | 10.4780 | 10.5010 | 3.2370 | 0.2694 | 0.2775 | 11.6632 | 12.0153 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 17.1807 | 17.2156 | 17.2504 | 4.1492 | 0.5170 | 0.3822 | 10.8558 | 8.0262 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 10.9970 | 11.0208 | 11.0447 | 3.3198 | 0.2466 | 0.1745 | 19.0233 | 13.4607 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 10.2349 | 10.2569 | 10.2789 | 3.2026 | 0.2798 | 0.2639 | 12.1373 | 11.4459 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 17.1807 | 17.2156 | 17.2505 | 4.1492 | 0.5113 | 0.3754 | 11.0533 | 8.1155 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | S | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 10.9970 | 11.0208 | 11.0447 | 3.3198 | 0.2474 | 0.1750 | 18.9666 | 13.4207 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | T | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 10.2349 | 10.2569 | 10.2789 | 3.2026 | 0.2786 | 0.2632 | 12.1664 | 11.4973 | 1.0000 | 1.0000 | 1.0000 |
| midas_umidas | exact | pre_advance | A | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.2507 | 1.3245 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_second | S | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.4241 | 1.2774 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_third | T | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6833 | 1.0849 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_advance | A | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.2770 | 1.3708 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_second | S | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.4537 | 1.3144 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_third | T | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6808 | 1.0895 |  |  |  |  | 0.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | A | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 17.1590 | 17.1925 | 17.2261 | 4.1464 | 0.5426 | 0.4003 | 10.3575 | 7.6418 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | S | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 10.2059 | 10.6695 | 11.1330 | 3.2656 | 0.1357 | 0.1289 | 25.3282 | 24.0685 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | T | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 11.4398 | 11.4662 | 11.4925 | 3.3862 | 0.3641 | 0.2935 | 11.5358 | 9.2992 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | A | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 17.1585 | 17.1921 | 17.2256 | 4.1463 | 0.5408 | 0.3979 | 10.4212 | 7.6673 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | S | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 10.2057 | 10.6693 | 11.1330 | 3.2656 | 0.1344 | 0.1282 | 25.4793 | 24.2994 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | T | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 11.4398 | 11.4662 | 11.4925 | 3.3862 | 0.3601 | 0.2921 | 11.5921 | 9.4034 | 1.0000 | 1.0000 | 1.0000 |
| no_revision | exact | pre_advance | A | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4254 | 0.3196 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_second | S | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0602 | 0.0667 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_third | T | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0955 | 0.1847 |  |  |  |  | 0.0000 |
| no_revision | pseudo | pre_advance | A | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4254 | 0.3196 |  |  |  |  | 0.0000 |

## Revision Forecast Audit

| model_id | timing_mode | checkpoint_id | revision_target_id | n_forecasts | n_variance | share_positive_variance | share_finite_sd | min_forecast_variance | median_forecast_variance | max_forecast_variance | mean_forecast_sd | empirical_error_sd | RMSE | mean_sd_to_rmse | mean_sd_to_empirical_error_sd | coverage_68 | coverage_90 | model_implied_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ar | exact | pre_advance | DELTA_SA | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0644 | 0.0608 |  |  |  |  | 0.0000 |
| ar | exact | pre_second | DELTA_TS | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.1034 | 0.1221 |  |  |  |  | 0.0000 |
| ar | exact | pre_third | DELTA_MT | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6582 | 0.6609 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_advance | DELTA_SA | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0644 | 0.0608 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_second | DELTA_TS | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.1034 | 0.1221 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_third | DELTA_MT | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6582 | 0.6609 |  |  |  |  | 0.0000 |
| bridge | exact | pre_advance | DELTA_SA | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0606 | 0.0522 |  |  |  |  | 0.0000 |
| bridge | exact | pre_second | DELTA_TS | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.1873 | 0.1689 |  |  |  |  | 0.0000 |
| bridge | exact | pre_third | DELTA_MT | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4909 | 0.5150 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_advance | DELTA_SA | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0622 | 0.0519 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_second | DELTA_TS | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.1914 | 0.1763 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_third | DELTA_MT | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4938 | 0.5190 |  |  |  |  | 0.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | DELTA_SA | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 15.9726 | 16.0094 | 16.0463 | 4.0012 | 0.0602 | 0.0667 | 59.9982 | 66.4926 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | DELTA_TS | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 16.3018 | 16.3386 | 16.3753 | 4.0421 | 0.0955 | 0.1847 | 21.8873 | 42.3436 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | DELTA_MT | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 17.7440 | 17.7661 | 17.7882 | 4.2150 | 0.6126 | 0.4636 | 9.0911 | 6.8809 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 15.9726 | 16.0094 | 16.0462 | 4.0012 | 0.0602 | 0.0667 | 59.9982 | 66.4925 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | DELTA_TS | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 16.3017 | 16.3385 | 16.3753 | 4.0421 | 0.0955 | 0.1847 | 21.8873 | 42.3436 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | DELTA_MT | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 17.7440 | 17.7661 | 17.7882 | 4.2150 | 0.6126 | 0.4636 | 9.0911 | 6.8809 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | DELTA_SA | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 18.2873 | 18.3272 | 18.3671 | 4.2810 | 0.0755 | 0.0761 | 56.2561 | 56.7059 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | DELTA_TS | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 15.8093 | 15.8440 | 15.8786 | 3.9804 | 0.0957 | 0.1844 | 21.5811 | 41.5753 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | DELTA_MT | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 18.6565 | 18.6797 | 18.7028 | 4.3220 | 0.6431 | 0.4991 | 8.6600 | 6.7201 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | DELTA_SA | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 18.2873 | 18.3272 | 18.3670 | 4.2810 | 0.0746 | 0.0743 | 57.5943 | 57.4231 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | DELTA_TS | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 15.8093 | 15.8439 | 15.8786 | 3.9804 | 0.0957 | 0.1844 | 21.5809 | 41.5750 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | DELTA_MT | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 18.6565 | 18.6797 | 18.7028 | 4.3220 | 0.6432 | 0.4991 | 8.6594 | 6.7196 | 1.0000 | 1.0000 | 1.0000 |
| midas_umidas | exact | pre_advance | DELTA_SA | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.2313 | 0.9617 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_second | DELTA_TS | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4475 | 0.6383 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_third | DELTA_MT | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 5.6884 | 4.4579 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_advance | DELTA_SA | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.2284 | 0.9624 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_second | DELTA_TS | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.4665 | 0.6579 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_third | DELTA_MT | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 5.6616 | 4.4534 |  |  |  |  | 0.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | DELTA_SA | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 17.5393 | 17.5795 | 17.6197 | 4.1928 | 0.0599 | 0.0537 | 78.0447 | 69.9454 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | DELTA_TS | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 16.4206 | 17.2991 | 18.1775 | 4.1579 | 0.1355 | 0.1864 | 22.3078 | 30.6782 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | DELTA_MT | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 21.5700 | 21.5938 | 21.6176 | 4.6469 | 0.6607 | 0.5013 | 9.2699 | 7.0336 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | DELTA_SA | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 17.5394 | 17.5796 | 17.6197 | 4.1928 | 0.0599 | 0.0537 | 78.1284 | 69.9413 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | DELTA_TS | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 16.4204 | 17.2990 | 18.1776 | 4.1579 | 0.1355 | 0.1862 | 22.3285 | 30.6771 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | DELTA_MT | 2.0000 | 2.0000 | 1.0000 | 1.0000 | 21.5700 | 21.5939 | 21.6178 | 4.6469 | 0.6601 | 0.5007 | 9.2799 | 7.0402 | 1.0000 | 1.0000 | 1.0000 |
| no_revision | exact | pre_advance | DELTA_SA | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0602 | 0.0667 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_second | DELTA_TS | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0955 | 0.1847 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_third | DELTA_MT | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6126 | 0.4636 |  |  |  |  | 0.0000 |
| no_revision | pseudo | pre_advance | DELTA_SA | 2.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0602 | 0.0667 |  |  |  |  | 0.0000 |

## Covariance Matrix Audit

| model_id | timing_mode | checkpoint_id | n_matrices | share_psd | max_asymmetry | min_eigenvalue_min | min_eigenvalue_median | max_eigenvalue_median |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | 2.0000 | 1.0000 | 0.0000 | 7.9681 | 7.9864 | 28.8541 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | 2.0000 | 1.0000 | 0.0000 | 7.9547 | 7.9725 | 20.8517 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | 2.0000 | 1.0000 | 0.0000 | 7.9430 | 7.9608 | 17.4206 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | 2.0000 | 1.0000 | 0.0000 | 7.9681 | 7.9864 | 28.8542 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | 2.0000 | 1.0000 | 0.0000 | 7.9547 | 7.9725 | 20.8517 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | 2.0000 | 1.0000 | 0.0000 | 7.9430 | 7.9608 | 17.4206 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | 2.0000 | 1.0000 | 0.0000 | 7.9038 | 7.9215 | 30.8125 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | 2.0000 | 1.0000 | 0.0000 | 7.8996 | 7.9169 | 21.2419 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | 2.0000 | 1.0000 | 0.0000 | 7.8867 | 7.9040 | 17.6613 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | 2.0000 | 1.0000 | 0.0000 | 7.9038 | 7.9215 | 30.8125 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | 2.0000 | 1.0000 | 0.0000 | 7.8996 | 7.9169 | 21.2419 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | 2.0000 | 1.0000 | 0.0000 | 7.8867 | 7.9040 | 17.6613 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | 2.0000 | 1.0000 | 0.0000 | 8.4120 | 8.4316 | 29.1776 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | 2.0000 | 1.0000 | 0.0000 | 7.6606 | 8.0511 | 19.5020 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | 2.0000 | 1.0000 | 0.0000 | 8.3803 | 8.4000 | 17.5795 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | 2.0000 | 1.0000 | 0.0000 | 8.4120 | 8.4316 | 29.1758 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | 2.0000 | 1.0000 | 0.0000 | 7.6605 | 8.0511 | 19.5016 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | 2.0000 | 1.0000 | 0.0000 | 8.3802 | 8.4000 | 17.5795 |
| revision_dfm_kalman_em | exact | pre_advance | 2.0000 | 1.0000 | 0.0000 | 7.2063 | 7.2237 | 31.5020 |
| revision_dfm_kalman_em | exact | pre_second | 2.0000 | 1.0000 | 0.0000 | 7.2365 | 7.5490 | 21.0836 |
| revision_dfm_kalman_em | exact | pre_third | 2.0000 | 1.0000 | 0.0000 | 7.1901 | 7.5362 | 17.2709 |
| revision_dfm_kalman_em | pseudo | pre_advance | 2.0000 | 1.0000 | 0.0000 | 7.2063 | 7.2237 | 31.5020 |
| revision_dfm_kalman_em | pseudo | pre_second | 2.0000 | 1.0000 | 0.0000 | 7.2366 | 7.5490 | 21.0837 |
| revision_dfm_kalman_em | pseudo | pre_third | 2.0000 | 1.0000 | 0.0000 | 7.1901 | 7.5362 | 17.2709 |
