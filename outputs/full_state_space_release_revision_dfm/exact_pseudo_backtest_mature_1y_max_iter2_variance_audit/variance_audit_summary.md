# Variance Audit

Generated UTC: `2026-04-26T11:04:17+00:00`

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
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 8.5140 | 8.8055 | 9.1072 | 2.9675 | 0.6365 | 0.6003 | 4.9432 | 4.6623 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 4.4320 | 4.4701 | 5.1835 | 2.1526 | 0.3529 | 0.3211 | 6.7044 | 6.1006 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 3.8300 | 3.8585 | 4.4312 | 1.9977 | 0.2293 | 0.2119 | 9.4261 | 8.7130 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 8.5141 | 8.8054 | 9.1064 | 2.9675 | 0.6407 | 0.5963 | 4.9764 | 4.6315 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 4.4320 | 4.4701 | 5.1835 | 2.1526 | 0.3520 | 0.3207 | 6.7115 | 6.1152 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 3.8300 | 3.8582 | 4.4312 | 1.9976 | 0.2310 | 0.2130 | 9.3796 | 8.6487 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 12.4383 | 12.8034 | 13.1788 | 3.5783 | 0.6383 | 0.5855 | 6.1117 | 5.6056 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.3718 | 5.4100 | 5.9307 | 2.3512 | 0.4557 | 0.4269 | 5.5075 | 5.1591 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 4.2823 | 4.3118 | 4.7920 | 2.1029 | 0.2680 | 0.2361 | 8.9058 | 7.8469 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 12.4384 | 12.8034 | 13.1777 | 3.5782 | 0.6323 | 0.5733 | 6.2419 | 5.6591 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.3718 | 5.4100 | 5.9307 | 2.3512 | 0.4547 | 0.4265 | 5.5124 | 5.1712 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 4.2823 | 4.3116 | 4.7920 | 2.1028 | 0.2698 | 0.2375 | 8.8535 | 7.7926 | 1.0000 | 1.0000 | 1.0000 |
| midas_umidas | exact | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.4902 | 1.6879 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.8914 | 0.9209 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5217 | 0.9046 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 1.3176 | 1.6895 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.9139 | 0.9482 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5097 | 0.8772 |  |  |  |  | 0.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 13.9999 | 14.4918 | 14.9883 | 3.8065 | 0.4717 | 0.4086 | 9.3170 | 8.0696 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.0811 | 5.6075 | 6.1348 | 2.3656 | 0.4964 | 0.4314 | 5.4841 | 4.7656 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.6320 | 6.1870 | 6.7502 | 2.4854 | 0.3053 | 0.2841 | 8.7494 | 8.1418 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | A | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 13.9991 | 14.4907 | 14.9866 | 3.8064 | 0.4855 | 0.4208 | 9.0456 | 7.8394 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | S | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.0809 | 5.6075 | 6.1347 | 2.3656 | 0.4941 | 0.4291 | 5.5128 | 4.7872 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | T | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.6331 | 6.1861 | 6.7502 | 2.4853 | 0.3053 | 0.2819 | 8.8169 | 8.1416 | 1.0000 | 1.0000 | 1.0000 |
| no_revision | exact | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6674 | 0.5998 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_second | S | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2107 | 0.1852 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_third | T | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0854 | 0.1544 |  |  |  |  | 0.0000 |
| no_revision | pseudo | pre_advance | A | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.6674 | 0.5998 |  |  |  |  | 0.0000 |

## Revision Forecast Audit

| model_id | timing_mode | checkpoint_id | revision_target_id | n_forecasts | n_variance | share_positive_variance | share_finite_sd | min_forecast_variance | median_forecast_variance | max_forecast_variance | mean_forecast_sd | empirical_error_sd | RMSE | mean_sd_to_rmse | mean_sd_to_empirical_error_sd | coverage_68 | coverage_90 | model_implied_share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ar | exact | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2209 | 0.2226 |  |  |  |  | 0.0000 |
| ar | exact | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0900 | 0.0984 |  |  |  |  | 0.0000 |
| ar | exact | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5505 | 0.8213 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2209 | 0.2226 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0900 | 0.0984 |  |  |  |  | 0.0000 |
| ar | pseudo | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.5505 | 0.8213 |  |  |  |  | 0.0000 |
| bridge | exact | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2211 | 0.1963 |  |  |  |  | 0.0000 |
| bridge | exact | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.1314 | 0.2040 |  |  |  |  | 0.0000 |
| bridge | exact | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.3194 | 0.4736 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2317 | 0.2035 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.1325 | 0.2104 |  |  |  |  | 0.0000 |
| bridge | pseudo | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.3171 | 0.4719 |  |  |  |  | 0.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.2684 | 5.7290 | 6.2052 | 2.3926 | 0.2107 | 0.1852 | 12.9176 | 11.3537 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.3693 | 5.4162 | 6.3999 | 2.3754 | 0.0854 | 0.1544 | 15.3844 | 27.8245 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 8.2551 | 8.3060 | 9.1452 | 2.9153 | 0.3477 | 0.3260 | 8.9426 | 8.3848 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.2684 | 5.7290 | 6.2049 | 2.3926 | 0.2107 | 0.1852 | 12.9176 | 11.3537 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.3694 | 5.4162 | 6.3999 | 2.3754 | 0.0854 | 0.1544 | 15.3844 | 27.8244 | 1.0000 | 1.0000 | 1.0000 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 8.2551 | 8.3058 | 9.1452 | 2.9153 | 0.3477 | 0.3260 | 8.9425 | 8.3847 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 8.3868 | 8.7698 | 9.1663 | 2.9614 | 0.2949 | 0.2683 | 11.0356 | 10.0411 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.7314 | 5.7764 | 6.6593 | 2.4454 | 0.0853 | 0.1542 | 15.8622 | 28.6641 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 9.6078 | 9.6639 | 10.4890 | 3.1389 | 0.3490 | 0.3370 | 9.3144 | 8.9948 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 8.3868 | 8.7698 | 9.1660 | 2.9613 | 0.2876 | 0.2636 | 11.2355 | 10.2980 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 5.7315 | 5.7764 | 6.6593 | 2.4454 | 0.0853 | 0.1542 | 15.8622 | 28.6641 | 1.0000 | 1.0000 | 1.0000 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 9.6078 | 9.6637 | 10.4890 | 3.1389 | 0.3490 | 0.3370 | 9.3142 | 8.9947 | 1.0000 | 1.0000 | 1.0000 |
| midas_umidas | exact | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.7500 | 0.6802 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.3750 | 0.4710 |  |  |  |  | 0.0000 |
| midas_umidas | exact | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 2.5312 | 2.2432 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.7479 | 0.6809 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.3927 | 0.4806 |  |  |  |  | 0.0000 |
| midas_umidas | pseudo | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 2.4639 | 2.2136 |  |  |  |  | 0.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.5556 | 8.2075 | 8.8765 | 2.8635 | 0.2380 | 0.2190 | 13.0763 | 12.0313 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.5703 | 8.5062 | 9.4428 | 2.9123 | 0.1115 | 0.1559 | 18.6836 | 26.1283 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 13.1069 | 14.2079 | 15.3004 | 3.7664 | 0.3661 | 0.3441 | 10.9467 | 10.2877 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | DELTA_SA | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.5556 | 8.2075 | 8.8764 | 2.8635 | 0.2375 | 0.2187 | 13.0951 | 12.0554 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | DELTA_TS | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 7.5701 | 8.5062 | 9.4429 | 2.9123 | 0.1117 | 0.1565 | 18.6132 | 26.0720 | 1.0000 | 1.0000 | 1.0000 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | DELTA_MT | 4.0000 | 4.0000 | 1.0000 | 1.0000 | 13.1086 | 14.2062 | 15.3004 | 3.7663 | 0.3650 | 0.3433 | 10.9719 | 10.3191 | 1.0000 | 1.0000 | 1.0000 |
| no_revision | exact | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2107 | 0.1852 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_second | DELTA_TS | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.0854 | 0.1544 |  |  |  |  | 0.0000 |
| no_revision | exact | pre_third | DELTA_MT | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.3477 | 0.3260 |  |  |  |  | 0.0000 |
| no_revision | pseudo | pre_advance | DELTA_SA | 4.0000 | 0.0000 | 0.0000 | 0.0000 |  |  |  |  | 0.2107 | 0.1852 |  |  |  |  | 0.0000 |

## Covariance Matrix Audit

| model_id | timing_mode | checkpoint_id | n_matrices | share_psd | max_asymmetry | min_eigenvalue_min | min_eigenvalue_median | max_eigenvalue_median |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| indicator_revision_only_dfm_kalman_em | exact | pre_advance | 4.0000 | 1.0000 | 0.0000 | 2.6336 | 2.8633 | 27.5138 |
| indicator_revision_only_dfm_kalman_em | exact | pre_second | 4.0000 | 1.0000 | 0.0000 | 2.6170 | 2.6400 | 10.9084 |
| indicator_revision_only_dfm_kalman_em | exact | pre_third | 4.0000 | 1.0000 | 0.0000 | 2.6284 | 2.6487 | 8.1804 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_advance | 4.0000 | 1.0000 | 0.0000 | 2.6336 | 2.8633 | 27.5137 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_second | 4.0000 | 1.0000 | 0.0000 | 2.6170 | 2.6400 | 10.9083 |
| indicator_revision_only_dfm_kalman_em | pseudo | pre_third | 4.0000 | 1.0000 | 0.0000 | 2.6284 | 2.6484 | 8.1800 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_advance | 4.0000 | 1.0000 | 0.0000 | 2.8804 | 3.0942 | 28.8161 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_second | 4.0000 | 1.0000 | 0.0000 | 2.8638 | 2.8863 | 14.0122 |
| joint_indicator_revision_dfm_full_kalman_em | exact | pre_third | 4.0000 | 1.0000 | 0.0000 | 2.8764 | 2.8968 | 9.8110 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_advance | 4.0000 | 1.0000 | 0.0000 | 2.8805 | 3.0942 | 28.8159 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_second | 4.0000 | 1.0000 | 0.0000 | 2.8638 | 2.8863 | 14.0121 |
| joint_indicator_revision_dfm_full_kalman_em | pseudo | pre_third | 4.0000 | 1.0000 | 0.0000 | 2.8764 | 2.8967 | 9.8107 |
| monthly_mixed_frequency_kalman_em | exact | pre_advance | 4.0000 | 1.0000 | 0.0000 | 3.3403 | 3.7027 | 30.6344 |
| monthly_mixed_frequency_kalman_em | exact | pre_second | 4.0000 | 1.0000 | 0.0000 | 3.3216 | 3.7053 | 14.6332 |
| monthly_mixed_frequency_kalman_em | exact | pre_third | 4.0000 | 1.0000 | 0.0000 | 3.3397 | 3.6881 | 12.4220 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_advance | 4.0000 | 1.0000 | 0.0000 | 3.3403 | 3.7027 | 30.6301 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_second | 4.0000 | 1.0000 | 0.0000 | 3.3215 | 3.7053 | 14.6329 |
| monthly_mixed_frequency_kalman_em | pseudo | pre_third | 4.0000 | 1.0000 | 0.0000 | 3.3404 | 3.6876 | 12.4202 |
| revision_dfm_kalman_em | exact | pre_advance | 4.0000 | 1.0000 | 0.0000 | 2.8822 | 3.1184 | 31.3659 |
| revision_dfm_kalman_em | exact | pre_second | 4.0000 | 1.0000 | 0.0000 | 2.9104 | 3.3035 | 15.0560 |
| revision_dfm_kalman_em | exact | pre_third | 4.0000 | 1.0000 | 0.0000 | 2.8773 | 2.9140 | 9.9092 |
| revision_dfm_kalman_em | pseudo | pre_advance | 4.0000 | 1.0000 | 0.0000 | 2.8822 | 3.1184 | 31.3658 |
| revision_dfm_kalman_em | pseudo | pre_second | 4.0000 | 1.0000 | 0.0000 | 2.9104 | 3.3035 | 15.0560 |
| revision_dfm_kalman_em | pseudo | pre_third | 4.0000 | 1.0000 | 0.0000 | 2.8772 | 2.9142 | 9.9100 |
