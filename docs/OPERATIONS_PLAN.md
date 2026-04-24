# Operations Plan

## Mục đích của file này

File này là bản hướng dẫn vận hành cho repo hiện tại, để trả lời 4 câu hỏi:

1. Repo này hiện đã có gì.
2. `Stage 0`, `Stage 1`, `Stage 2` thực chất đang đảm nhiệm việc gì.
3. Khi validate lại 3 stage, ta sẽ kiểm cái gì và vì sao.
4. Sau khi 3 stage pass, pipeline tiếp theo sẽ nối vào đâu để đi tới mô hình nowcasting thật sự.

---

## Tổng quan ngắn

Repo hiện tại **chưa phải modeling repo hoàn chỉnh**, nhưng đã là một **data-and-semantics repo khá tốt**.

Nó đã đi được tới:

- `Stage 0`: raw data foundation
- `Stage 1`: bronze normalization
- `Stage 2`: silver semantic/governance layer

Điều này có nghĩa là repo hiện tại đã giải quyết khá nhiều phần khó:

- tải và lưu `RTDSM`, `ALFRED`, `BEA`, release calendars
- chuẩn hóa raw artifacts thành các bảng dùng được
- tách biệt rõ:
  - GDP release-stage targets
  - GDP complete vintage history
  - indicator metadata
  - release-calendar semantics
  - source limitations

Điều repo **chưa làm xong** là phần downstream pipeline cho nghiên cứu:

- exact information-set builder
- forecast-origin snapshot builder
- transformed model-ready panels
- benchmark forecasting
- release-structured DFM
- revision-aware layer
- evaluation tables và paper artifacts

---

## Stage 0 hiện đang có ý nghĩa gì

`Stage 0` là tầng **raw-data foundation**.

Mục tiêu:

- đảm bảo repo có đủ raw inputs cần thiết
- khóa được provenance của dữ liệu
- không để downstream pipeline phụ thuộc vào download ad hoc

Artifacts/chức năng chính:

- `data/raw/rtdsm/routput/*`
- `data/raw/alfred/vintage_dates/*`
- `data/raw/alfred/series_observations/*`
- `data/raw/bea/api/*`
- `data/raw/calendars/*`
- `scripts/download_alfred_and_calendars.py`
- `scripts/download_bea.py`
- `scripts/build_census_proxy_calendar.py`
- `scripts/validate_stage0.py`

Điểm mạnh:

- raw inputs đã khá đầy đủ
- có validation report
- đã có Census proxy calendar để xử lý chỗ official Census calendar bị chặn

Điểm cần nhớ:

- Stage 0 chỉ đảm bảo **data presence + raw reproducibility**
- Stage 0 chưa đảm bảo dữ liệu đó đã sẵn sàng cho modeling

---

## Stage 1 hiện đang có ý nghĩa gì

`Stage 1` là tầng **bronze normalization**.

Mục tiêu:

- parse raw files thành bảng dài, có schema ổn định
- giữ nguyên nghĩa của raw source
- không tự ý harmonize quá sớm

Artifacts chính:

- `data/bronze/targets/gdp_release_targets.csv`
- `data/bronze/targets/gdp_complete_vintages_long.csv`
- `data/bronze/indicators/alfred_monthly_long.csv`
- `data/bronze/calendars/release_calendar_master.csv`

Ý nghĩa từng artifact:

- `gdp_release_targets.csv`
  - chứa GDP release-stage từ RTDSM
  - giữ riêng `first`, `second`, `third`, `most_recent`

- `gdp_complete_vintages_long.csv`
  - chứa lịch sử vintage GDP đầy đủ
  - dùng cho mature target, revision logic, và robustness

- `alfred_monthly_long.csv`
  - là panel indicator dài theo `series_id`, `observation_date`, `realtime_start`
  - đây là raw modeling backbone quan trọng nhất cho indicators

- `release_calendar_master.csv`
  - hợp nhất BEA/BLS/Fed/Census proxy thành một bảng calendar chuẩn hóa

Điểm mạnh:

- Stage 1 đã tạo ra các bảng bronze đúng kiểu research pipeline cần
- `alfred_monthly_long.csv` rất giá trị vì nó đã gom long-form vintage panel

Điểm cần nhớ:

- Bronze layer cố tình chưa “khép logic nghiên cứu”
- tức là chưa tạo exact forecast snapshots, chưa áp transformation, chưa model-ready

---

## Stage 2 hiện đang có ý nghĩa gì

`Stage 2` là tầng **silver semantics and governance**.

Mục tiêu:

- gắn meaning và machine-readable contracts cho dữ liệu bronze
- nói rõ cái gì là target, cái gì là indicator, cái gì là official timing, cái gì là proxy timing
- giữ limitation visible thay vì giấu đi

Artifacts chính:

- `data/silver/targets/target_definition_table.csv`
- `data/silver/targets/gdp_release_stage_silver.csv`
- `data/silver/targets/gdp_complete_vintages_silver.csv`
- `data/silver/indicators/indicator_metadata.csv`
- `data/silver/indicators/indicator_release_map.csv`
- `data/silver/calendars/release_block_taxonomy.csv`
- `data/silver/calendars/release_calendar_silver.csv`
- `data/silver/calendars/calendar_coverage_metadata.csv`
- `data/silver/governance/source_limitations_registry.csv`

Điểm mạnh:

- repo đã có semantic contracts tương đối rõ
- downstream pipeline có thể đọc `silver` thay vì suy đoán từ raw/bronze
- `source_limitations_registry.csv` đặc biệt hữu ích để tránh leakage hoặc assumptions sai

Điểm cần nhớ:

- Silver layer vẫn chưa phải exact-real-time nowcast layer
- nó mới là tầng “chuẩn bị đúng ngữ nghĩa” cho pipeline đó

---

## Kết luận về bronze và silver

Nếu bạn chưa chắc `bronze` và `silver`, có thể hiểu ngắn như sau:

- `bronze` = dữ liệu đã parse sạch từ raw, nhưng vẫn gần raw source
- `silver` = dữ liệu bronze đã được gắn semantic meaning và rule để downstream dùng an toàn hơn

Trong repo này:

- `bronze` là nơi ta lấy dữ liệu nền để build modeling inputs
- `silver` là nơi ta lấy mapping/metadata/governance để build đúng information set

Nói cách khác:

- **bronze trả lời “dữ liệu là gì ở dạng bảng”**
- **silver trả lời “dữ liệu đó nên được hiểu và dùng như thế nào”**

---

## Việc mình sẽ làm trước tiên

Trước khi nối pipeline mới, mình sẽ **validate lại cả 3 stage** theo đúng repo hiện tại.

### Validation pass 1: structural and scripted rerun

Mục tiêu:

- đảm bảo scripts hiện tại vẫn chạy được trên máy này
- xác nhận artifacts hiện có không chỉ là file tồn tại mà còn tái tạo được

Sẽ chạy:

- `scripts/validate_stage0.py`
- `scripts/validate_stage1.py`
- `scripts/validate_stage2.py`

và nếu cần:

- rerun một phần hoặc toàn bộ các build scripts của từng stage

### Validation pass 2: semantic spot checks

Mục tiêu:

- xác nhận các bảng quan trọng thật sự consistent

Sẽ kiểm ít nhất:

- khóa uniqueness của bronze/silver tables
- date/quarter formats
- release-stage ordering
- consistency giữa:
  - `gdp_release_targets.csv`
  - `gdp_release_stage_silver.csv`
  - `target_definition_table.csv`
- consistency giữa:
  - `release_calendar_master.csv`
  - `release_calendar_silver.csv`
  - `indicator_release_map.csv`
  - `calendar_coverage_metadata.csv`
- coverage của `alfred_monthly_long.csv` so với `indicator_metadata.csv`

### Validation pass 3: downstream-readiness review

Mục tiêu:

- xem repo này đã đủ để nối modeling pipeline chưa

Mình sẽ chốt rõ:

- cái gì dùng được ngay
- cái gì cần patch nhỏ
- cái gì còn thiếu phải xây thêm trước modeling

---

## Pipeline tiếp theo sẽ nối vào đâu

Sau khi `Stage 0-2` pass, mình sẽ coi đó là **data contract layer đã khóa** và nối tiếp bằng một tầng mới.

Tên làm việc:

- `Stage 3`: exact information-set and snapshot layer
- `Stage 4`: modeling and evaluation layer

---

## Stage 3 dự kiến: information-set pipeline

Đây là phần quan trọng nhất để biến repo từ data repo thành research repo.

### Output chính cần xây

- `event_panel`
- `forecast_origin_schedule`
- `snapshot_panel_exact`
- `snapshot_panel_pseudo`
- `target_panel_model_ready`

### Việc cụ thể

1. Dựng `event_panel`
   - hợp nhất indicator vintages với release calendar support
   - mỗi observation phải biết:
     - `series_id`
     - `observation_date`
     - `realtime_start`
     - `realtime_end`
     - `availability_date`
     - `availability_time_et`
     - `calendar_support_type`

2. Dựng `forecast_origin_schedule`
   - 6 checkpoints mỗi quarter:
     - `M1 end`
     - `M2 labor`
     - `M3 spending/trade/inventories`
     - `pre_advance`
     - `pre_second`
     - `pre_third`

3. Dựng `snapshot_panel_exact`
   - tại mỗi forecast origin, chỉ giữ thông tin thực sự available tại thời điểm đó

4. Dựng `snapshot_panel_pseudo`
   - monthly pseudo-real-time comparison panel

5. Áp transformation và standardization real-time
   - không dùng full-sample moments
   - chỉ dùng information available up to forecast origin

### Kết quả mong muốn

Sau Stage 3, repo phải có thể trả lời:

- “ở ngày forecast origin này, model được nhìn thấy chính xác dữ liệu nào?”

Nếu chưa trả lời được câu này, chưa được move sang modeling.

---

## Stage 4 dự kiến: modeling and evaluation

Khi Stage 3 ổn, mới nối modeling.

### Benchmark stack v1

- `AR`
- `Bridge`
- `Standard DFM`
- `Release-structured DFM`

### Extension v2

- `Revision-aware DFM`
- revision forecast tables
- exact vs pseudo ablation

### Output chính

- `forecast_results`
- `metrics_summary`
- point forecast tables cho `A/S/T`
- revision forecast tables cho `Δ_SA`, `Δ_TS`, `Δ_MT`
- ablation table `exact vs pseudo`
- figure `within-quarter nowcast path`
- figure `forecast update decomposition`

---

## Quy tắc làm việc từ đây

Từ thời điểm này, mình sẽ dùng repo này theo nguyên tắc:

1. Không phá vỡ contract của `Stage 0-2`.
2. Nếu cần sửa dữ liệu hoặc mapping, phải sửa có kiểm soát và log lý do.
3. Không trộn `bronze` và `silver` semantics vào modeling layer một cách âm thầm.
4. Mọi step mới phải reproducible bằng script, không notebook thủ công.
5. Exact-real-time discipline được ưu tiên hơn model complexity.

---

## Thứ tự thực thi mà mình sẽ dùng

1. Validate lại `Stage 0`
2. Validate lại `Stage 1`
3. Validate lại `Stage 2`
4. Review chênh lệch giữa validation reports cũ và rerun mới
5. Chốt patch nếu có lỗi hoặc semantic drift
6. Thêm `Stage 3` pipeline
7. Thêm benchmark modeling
8. Thêm evaluation/reporting

---

## Trạng thái hiện tại

Theo những gì mình đã xem sơ bộ:

- repo này **dùng được**
- foundation đã tốt hơn repo trống rất nhiều
- phần nên tin dùng nhất hiện tại là:
  - `raw`
  - `bronze`
  - `silver`
  - validation reports

Phần chưa nên tin là đã “xong nghiên cứu”:

- exact information-set construction
- model-ready forecast snapshots
- forecasting and paper outputs

Nói ngắn gọn:

Repo này là một **base rất tốt để tiếp tục**, chứ không phải điểm cuối.
