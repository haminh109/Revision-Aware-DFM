# Revision-Aware Real-Time U.S. GDP Nowcasting

## Bản Report Theo Format Paper

Lưu ý: file này là bản narrative viết tay để giúp đọc bài theo format paper. Sau các nâng cấp state-space mới nhất, số liệu nguồn chuẩn để đọc kết quả hiện tại là `outputs/reports/submission_mode_report.md` và các bảng trong `outputs/tables/headline_*.csv`.

### 1. Title

**Release-Structured and Revision-Aware Real-Time Nowcasting of U.S. GDP**

### 2. Abstract

Bài nghiên cứu này đánh giá liệu việc mô hình hóa đúng cấu trúc công bố dữ liệu GDP theo từng vòng phát hành (`advance`, `second`, `third`) và tận dụng thông tin real-time có giúp cải thiện nowcast GDP Mỹ hay không. Pipeline được xây dựng trên dữ liệu real-time từ `RTDSM`, `ALFRED`, cùng release calendar lịch sử để tái tạo information set theo checkpoint trong quý. Bộ benchmark gồm `AR`, `bridge regression`, `standard DFM`, `release-structured DFM`, và phần mở rộng `revision-aware DFM`.

Kết quả headline cho thấy mô hình cấu trúc có lợi thế rõ rệt tại các checkpoint gắn trực tiếp với vòng công bố GDP. Với `advance GDP`, `release_dfm` đạt `RMSE = 4.862` trong exact real-time, thấp hơn `AR = 7.201` và `bridge = 5.151`. Với `second GDP`, `revision_dfm` cho kết quả tốt nhất với `RMSE = 0.600`, nhỉnh hơn `release_dfm = 0.637`. Với `third GDP`, `release_dfm` tốt nhất với `RMSE = 0.380`. So sánh exact với pseudo real-time cho thấy timing chính xác nhìn chung giúp các structured models hơn là các baseline đơn giản, đặc biệt ở `advance` và `third` releases. Tuy nhiên, thống kê `DM p-value` hiện chưa đủ mạnh để khẳng định superiority theo chuẩn inference nghiêm ngặt, nên kết quả nên được trình bày như bằng chứng thực nghiệm có triển vọng hơn là kết luận quyết định.

### 3. Introduction

Nowcasting GDP trong môi trường real-time là một bài toán vừa học thuật vừa thực tiễn vì nhà nghiên cứu và thị trường không quan sát một “GDP thật” duy nhất, mà quan sát chuỗi phát hành và chuỗi revision qua thời gian. Nếu information set được dựng sai, kết quả forecasting sẽ bị leakage và làm sai lệch đánh giá mô hình. Vì vậy, đóng góp chính của nghiên cứu này không chỉ nằm ở mô hình, mà còn nằm ở việc xây dựng một release-consistent real-time pipeline để tái hiện chính xác tập thông tin mà mô hình thực sự có thể nhìn thấy ở từng thời điểm.

Nghiên cứu này theo đuổi hai câu hỏi. Thứ nhất, liệu mô hình `release-structured` có cải thiện dự báo GDP ở các vòng phát hành sớm so với các benchmark đơn giản hơn hay không. Thứ hai, liệu các revision ngắn hạn giữa các vòng phát hành có mang tính dự báo được một phần hay không. Về mặt thực nghiệm, bài này đặt trọng tâm vào `advance`, `second`, và `third` GDP releases; phần mature target và revision forecasting được xem là lớp mở rộng hỗ trợ diễn giải chứ không phải trung tâm của paper.

### 4. Related Literature

Khung bài này đứng trên bốn nhánh literature chính.

Thứ nhất là literature về mixed-frequency nowcasting, điển hình là `Giannone, Reichlin, and Small (2008)` và `Banbura and Modugno (2014)`, nhấn mạnh vai trò của ragged-edge data và dynamic factor models trong dự báo vĩ mô ngắn hạn.

Thứ hai là literature về liên kết monthly indicators với quarterly GDP, đặc biệt `Mariano and Murasawa (2003)`, cung cấp logic tổng hợp tín hiệu tần suất cao vào một latent quarterly activity state.

Thứ ba là literature về real-time data và forecast evaluation với vintages, như `Croushore and Stark` và `Koenig, Dolmas, and Piger`, nhấn mạnh rằng forecast evaluation chỉ có ý nghĩa nếu information set được dựng đúng theo thời gian công bố lịch sử.

Thứ tư là literature về revisions, tiêu biểu là `Jacobs and van Norden`, và gần hơn là các nghiên cứu revision-aware nowcasting. Phần `revision_dfm` trong repo này hiện đã được triển khai thành một structural latent-state state-space model cho ladder `A/S/T/M`, nên phần revision forecasting không còn chỉ là approximation thực dụng như trước.

### 5. Data and Real-Time Design

#### 5.1 Data Sources

Nghiên cứu dùng ba lớp dữ liệu chính:

- `RTDSM` cho GDP release structure và vintage history
- `ALFRED` cho monthly indicators theo vintage
- historical release calendars để xác định availability timing

Panel chỉ báo v1 gồm 17 series, chia thành các block chính: labor, production, income-spending, housing-orders-inventories, và financial-survey variables. Thiết kế này đủ rộng để phản ánh business-cycle conditions nhưng vẫn đủ gọn để đảm bảo tính reproducible.

#### 5.2 Targets

Các target point forecasts chính là:

- `A`: advance GDP release
- `S`: second GDP release
- `T`: third GDP release

Các revision targets là:

- `DELTA_SA = S - A`
- `DELTA_TS = T - S`

Main sample cho backtest chạy trên `2005Q1-2024Q4`, với burn-in từ `1995Q1`. Các quý `2020Q2-2020Q3` được đánh dấu riêng để làm pandemic robustness.

#### 5.3 Forecast Origins

Mỗi quý được đánh giá tại 6 checkpoints:

- `m1_end`
- `m2_labor`
- `m3_spending_trade_inventories`
- `pre_advance`
- `pre_second`
- `pre_third`

Trong phần headline paper, mỗi target chỉ được đọc tại checkpoint có ý nghĩa kinh tế trực tiếp:

- `A` tại `pre_advance`
- `S` tại `pre_second`
- `T` tại `pre_third`

Thiết kế này tránh việc đưa các checkpoint “tautological” vào bảng chính, tức các thời điểm mà target gần như đã được công bố hoặc bị neo quá sát release.

### 6. Methodology

#### 6.1 Benchmark Models

Repo hiện triển khai bốn baseline chính:

- `AR`
- `bridge`
- `standard_dfm`
- `release_dfm`

`AR` là benchmark tối thiểu, đại diện cho forecast purely autoregressive theo từng target.

`bridge` dùng block features tổng hợp từ monthly indicators và là benchmark empirical mạnh ở giai đoạn sớm trong quý.

`standard_dfm` đóng vai trò benchmark factor model không mô hình hóa rõ release rounds.

`release_dfm` là mô hình cốt lõi của paper, trong đó measurement structure phân biệt các vòng phát hành GDP khác nhau.

#### 6.2 Revision-Aware Extension

`revision_dfm` mở rộng `release_dfm` bằng cách thêm tầng dự báo revisions. Trong kết quả hiện tại, mô hình này hoạt động tốt nhất ở `second` release, nhưng phần này nên được mô tả như một extension có giá trị hơn là contribution duy nhất của bài.

### 7. Empirical Results

#### 7.1 Main Headline Results

Kết quả quan trọng nhất của bài có thể tóm tắt như sau:

| Target | Headline checkpoint | Best exact model | RMSE | Best pseudo model | RMSE |
|:--|:--|:--|--:|:--|--:|
| `A` | `pre_advance` | `release_dfm` | 4.862 | `release_dfm` | 5.060 |
| `S` | `pre_second` | `revision_dfm` | 0.600 | `revision_dfm` | 0.610 |
| `T` | `pre_third` | `release_dfm` | 0.380 | `release_dfm` | 0.395 |

Diễn giải ngắn gọn:

- Với `advance GDP`, structured models cải thiện đáng kể so với `AR` và nhỉnh hơn `bridge`.
- Với `second GDP`, `revision_dfm` là mô hình tốt nhất, cho thấy revision layer có thêm giá trị sau khi `advance` release đã xuất hiện.
- Với `third GDP`, `release_dfm` lại là mô hình tốt nhất, còn revision layer không vượt được bản release-structured đơn thuần.

#### 7.2 Comparison Against Benchmarks

Ở `pre_advance`, `release_dfm` exact có `RMSE = 4.862`, trong khi `bridge = 5.151` và `AR = 7.201`. Điều này cho thấy cấu trúc factor + release timing tạo ra lợi thế thực nghiệm có ý nghĩa kinh tế, dù chưa đủ mạnh về mặt test thống kê.

Ở `pre_second`, `revision_dfm` exact có `RMSE = 0.600`, tốt hơn `release_dfm = 0.637`, và bỏ xa `bridge = 4.996` cũng như `AR = 7.007`. Đây là điểm mạnh nhất hiện nay của extension revision-aware.

Ở `pre_third`, `release_dfm` exact có `RMSE = 0.380`, tốt hơn `revision_dfm = 0.401` và tốt hơn rất xa `bridge = 5.051`, `AR = 6.906`, `standard_dfm = 4.726`.

#### 7.3 Statistical Caution

Mặc dù relative RMSFE khá ấn tượng ở một số target, các `DM_test` hiện chủ yếu nằm quanh `0.15-0.29`, chưa cho bằng chứng mạnh theo ngưỡng conventional significance. Điều này có nghĩa là:

- bài có narrative thực nghiệm tốt
- nhưng nếu nhắm journal submission, cần thận trọng khi dùng ngôn ngữ “significantly better”
- nên ưu tiên phrasing kiểu “economically meaningful improvement” hoặc “systematic reduction in RMSE”

### 8. Exact vs Pseudo Real-Time

So sánh exact với pseudo real-time là một trong những phần có ích nhất để định vị paper.

Kết quả headline cho thấy:

- với `A`, `release_dfm` exact tốt hơn pseudo khoảng `0.198 RMSE`
- với `S`, `revision_dfm` exact tốt hơn pseudo khoảng `0.010 RMSE`
- với `T`, `release_dfm` exact tốt hơn pseudo khoảng `0.015 RMSE`

Điểm này quan trọng vì nó cho phép bài nhấn mạnh rằng việc dựng đúng event timing không chỉ là hygiene issue, mà còn có thể tạo khác biệt thực nghiệm cho structured models.

Tuy vậy, exact timing không phải lúc nào cũng thắng. Ví dụ `bridge` exact ở `A` lại kém pseudo nhẹ khoảng `0.030 RMSE`. Điều này gợi ý rằng lợi ích của exact timing không đồng đều giữa các lớp mô hình và cần được trình bày như một kết quả thực nghiệm, không phải một tiên đề.

### 9. Revision Forecasting Results

Revision forecasting hiện cho tín hiệu “có nội dung nhưng chưa mạnh”.

Đối với `DELTA_SA`:

- exact `RMSE = 0.598`
- sign accuracy khoảng `0.582`

Đối với `DELTA_TS`:

- exact `RMSE = 0.366`
- sign accuracy khoảng `0.544`

Diễn giải hợp lý nhất là:

- revisions có thành phần dự báo được ở mức hạn chế
- nhưng predictive content hiện chưa đủ mạnh để biến revision forecasting thành contribution trung tâm
- phần này phù hợp hơn với vai trò extension hoặc supplementary result

### 10. Pandemic Robustness

Khi loại `2020Q2-2020Q3`, RMSE của tất cả mô hình giảm mạnh, đặc biệt với `A`. Điều này cho thấy sample full-period đang bị chi phối đáng kể bởi shock đại dịch.

Tuy nhiên, điều quan trọng là ranking của structured models nhìn chung vẫn giữ được:

- `A`: `release_dfm` exact giảm từ `4.862` xuống `1.858`
- `S`: `revision_dfm` exact gần như giữ nguyên vị trí tốt nhất, dù lợi thế so với `release_dfm` rất nhỏ
- `T`: `release_dfm` exact vẫn là mô hình tốt nhất

Do đó, pandemic robustness hiện hỗ trợ narrative rằng kết quả chính không hoàn toàn do một vài quý cực đoan tạo ra, dù magnitude của errors bị phóng đại đáng kể trong full sample.

### 11. Interpretation for a Paper

Nếu viết theo logic journal paper, phần narrative nên đi như sau:

1. `Bridge` là benchmark đơn giản nhưng mạnh ở giai đoạn đầu trong quý.
2. Khi tiến gần release dates, `release_dfm` hoặc `revision_dfm` vượt lên rõ rệt.
3. Lợi ích của exact timing tập trung ở structured models nhiều hơn là ở AR hoặc bridge.
4. Revision forecasting có ích, nhưng chưa nên được đẩy thành headline contribution chính.

Một cách viết gọn cho phần core contribution là:

> Bài này cho thấy rằng khi information set được dựng theo historical release timing, release-structured factor models cải thiện nowcast U.S. GDP tại các release-relevant checkpoints so với simple benchmarks, và lợi ích của exact timing là có thật nhưng không đồng đều giữa các lớp mô hình.

### 12. Limitations

Ở trạng thái hiện tại, paper vẫn còn ba hạn chế lớn:

- `revision_dfm` đã là structural latent-state revision model cho GDP release ladder, nhưng vẫn là bản parsimonious two-state chứ chưa joint-estimate revisions của toàn bộ monthly indicator panel
- `DM_test` chưa đủ mạnh để tuyên bố superiority theo nghĩa inferential chặt
- kết quả phụ thuộc khá mạnh vào việc có hay không các quý pandemic trong sample

Ba điểm này không làm bài yếu đi, nhưng chúng quyết định cách framing. Bản thảo nên được viết như một empirical paper mạnh về design, data discipline, và structured forecast comparison, chứ chưa nên tự định vị như một definitive new theory of revisions.

### 13. Conclusion

Kết quả hiện tại ủng hộ ba kết luận chính.

Thứ nhất, release-structured modeling có giá trị rõ rệt cho GDP nowcasting ở các checkpoint sát vòng công bố, đặc biệt với `advance` và `third` releases.

Thứ hai, revision-aware extension có giá trị lớn nhất ở `second` release, nơi việc tận dụng thông tin từ `advance` release giúp giảm RMSE thêm một bước.

Thứ ba, exact real-time timing là một margin có ý nghĩa thực nghiệm, nhưng lợi ích của nó phụ thuộc vào kiến trúc mô hình.

Nếu mục tiêu là tiến tới một bản thảo có khả năng nộp journal, thì bản report này nên được dùng như “interpretation layer” giữa output kỹ thuật của repo và phần writing của paper. Nói cách khác: pipeline hiện đã đủ để bắt đầu viết bài nghiêm túc, nhưng trước khi submission thật, vẫn cần thêm vài robustness checks và một narrative rất kỷ luật.

### 14. Files You Should Read Next

Để hiểu bài nhanh nhất, nên đọc theo thứ tự này:

1. `outputs/reports/paper_style_report_vi.md`
2. `outputs/reports/submission_mode_report.md`
3. `outputs/tables/headline_point_results.csv`
4. `outputs/tables/headline_exact_vs_pseudo.csv`
5. `outputs/tables/headline_point_pandemic_robustness.csv`
6. `outputs/tables/headline_revision_results.csv`
