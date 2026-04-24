# Submission Mode

Mục tiêu của `submission mode` là biến pipeline nghiên cứu hiện tại thành một bộ artifacts dễ dùng hơn cho giai đoạn viết paper.

## Command

```bash
python -m realtime_gdp_nowcast.cli --root . build-submission-pack
```

## Artifacts chính

- `outputs/tables/headline_point_results.csv`
  - point-forecast results tại các checkpoint headline:
  - `A -> pre_advance`
  - `S -> pre_second`
  - `T -> pre_third`
- `outputs/tables/headline_revision_results.csv`
  - revision results tại các checkpoint headline:
  - `DELTA_SA -> pre_advance`
  - `DELTA_TS -> pre_second`
- `outputs/tables/headline_exact_vs_pseudo.csv`
  - bảng so sánh exact vs pseudo tại đúng các checkpoint headline
- `outputs/tables/headline_point_results_no_pandemic.csv`
  - headline point results sau khi loại `2020Q2`, `2020Q3`
- `outputs/tables/headline_point_pandemic_robustness.csv`
  - chênh lệch RMSE giữa full sample và no-pandemic sample
- `outputs/reports/submission_mode_report.md`
  - bản tóm tắt gần với logic viết paper hơn

## Nguyên tắc

1. Không đưa các checkpoint mà target đã được công bố vào headline results.
2. Exact-vs-pseudo phải so sánh trên cùng target và cùng checkpoint headline.
3. Pandemic robustness là bắt buộc cho headline point results.
4. Diagnostic outputs đầy đủ vẫn được giữ ở `metrics_summary.csv`, `point_forecast_table.csv`, `revision_forecast_table.csv`.
