# WEEK 5

## 1. Features

### Main features - OMO Decision & Simulation

| Feature | Mô tả | Nếu bỏ, có thể thực hiện core tasks không? |
| --- | --- | --- |
| Instructions | Hướng dẫn cách chơi game | Không |
| Scenario / News Panel | Cung cấp bối cảnh kinh tế cho người chơi | Không |
| Economic Situation | Hiển thị các chỉ tiêu thanh khoản trong phase hiện tại | Không |
| OMO Decision | Người chơi chọn Auction Type, Pricing Method, OMO Action, Volume và Rate | Không |
| OMO Auction Engine | Xử lý bid, phân bổ volume và xác định kết quả đấu thầu | Không |
| Economic Engine | Tạo ngẫu nhiên KL dự thầu và LS dự thầu của các NHTM; Tính Total Supply Volume và Liquidity Gap; Tính Interbank Rate sau can thiệp | Không |
| Outcome / Result | Hiển thị kết quả của quyết định OMO | Không |
| Next-round State Update | Dùng kết quả hiện tại làm trạng thái đầu vào cho lượt tiếp theo | Không |

### Core features

| Feature | Mô tả | Nếu bỏ, có thể thực hiện core tasks không? |
| --- | --- | --- |
| Economic Situation | Hiển thị các chỉ tiêu thanh khoản trong phase hiện tại | Không |
| OMO Decision | Người chơi chọn Auction Type, Pricing Method, OMO Action, Volume và Rate | Không |
| OMO Auction Engine | Xử lý bid, phân bổ volume và xác định kết quả đấu thầu | Không |
| Economic Engine | Tạo ngẫu nhiên KL dự thầu và LS dự thầu của các NHTM; Tính Total Supply Volume và Liquidity Gap; Tính Interbank Rate sau can thiệp | Không |
| Outcome / Result | Hiển thị kết quả của quyết định OMO | Không |

### Supporting features

| Tính năng | Chức năng | Nếu bỏ, có thể thực hiện core tasks không? |
| --- | --- | --- |
| Input Guidance | Giải thích Auction Type, Pricing Method, OMO Action, Volume, Rate | Có |
| Indicator Guidance | Giải thích ý nghĩa của Liquidity Demand, Interbank Rate, Liquidity Gap... | Có |
| Result Explanation / Explainability | Giải thích tại sao Liquidity Gap và Interbank Rate thay đổi | Có |
| Validation | Cảnh báo input không hợp lệ hoặc volume/rate không phù hợp với auction type | Có |
| Phase Report | Tổng kết kết quả sau mỗi phase | Có |

### Optional features

| Tính năng | Giá trị | Mức độ ưu tiên |
| --- | --- | --- |
| Replay / Restart Scenario | Chơi lại một scenario | Medium |
| Player Profile / Login | Lưu thông tin người chơi | Medium |
| Achievement / Badge | Tăng gamification | Medium |
| Community | Các user trong cùng community có thể xem được outcome của nhau | Medium |
| Export Report / PDF | Cho phép lưu kết quả | Low |
| Theme / Dark Mode | Cải thiện UI | Low |
| Sound / Animation | Tăng trải nghiệm game | Low |

## 2. User goal

| Tiêu chí kiểm tra | Tính năng / cách thiết kế giúp thỏa mãn tiêu chí |
| --- | --- |
| User có biết bắt đầu ở đâu? | Scenario page là điểm bắt đầu của mỗi phase. Trang này hiển thị tình trạng kinh tế, các chỉ báo chính và thông tin về trạng thái của nền kinh tế hiện tại để người chơi ra quyết định. |
| Mỗi bước có phục vụ goal không? | Flow được thiết kế theo chuỗi Scenario → Economic Data → Decision → Auction Result + Updated Indicators + Explanation → Next Phase. Mỗi bước cung cấp thông tin hoặc thực hiện tính toán để user ra quyết định OMO và quan sát tác động của quyết định. |
| Có bước nào không cần thiết không? | Chỉ hiển thị thông tin cần thiết để người chơi ra quyết định ở từng phase; các giải thích lý thuyết chi tiết được đặt trong “?” |
| Output có dẫn tới next action rõ không? | Sau khi submit OMO, các chỉ số được cập nhật, cho người chơi thấy kết quả của decision. Kèm status/message giải thích kết quả và nút “Next Phase”. Ở phase tiếp theo, trạng thái từ phase trước được carry forward. |

## 3. User flow

### Happy Path

| Step | User action | System response | Evidence |
| --- | --- | --- | --- |
| 1 | Start Phase | Hiển thị scenario và các chỉ tiêu kinh tế/thanh khoản hiện tại | Scenario page + Economic Dashboard |
| 2 | Xem Liquidity Demand, Interbank Rate | Hệ thống hiển thị dữ liệu | Economic Dashboard |
| 3 | Chọn Auction Method | Hệ thống cập nhật các trường input phù hợp với loại đấu thầu | Decision Area |
| 4 | Chọn Pricing Method nếu sử dụng Interest-rate Auction | Hệ thống hiển thị phương thức pricing tương ứng | Decision Area |
| 5 | Chọn OMO Action | Hệ thống xác định hướng tác động: bơm hoặc hút thanh khoản | Decision Area |
| 6 | Nhập Volume và nếu chọn Volume Auction nhập Repo/Reverse Repo Rate | Hệ thống kiểm tra tính hợp lệ của input | Input validation |
| 7 | Nhấn Submit | Hệ thống chạy auction engine và xác định winning bids / real volume | Auction Result |
| 8 | Xem kết quả đấu thầu | Hiển thị Real Volume và Execution Rate/Rate Range | Auction Result |
| 9 | Xem kết quả tài chính | Hệ thống tính Total Supply, Liquidity Gap, Liquidity Pressure và Interbank Rate (T) và hiển thị kết quả Interbank Rate (T) | Outcome Dashboard |
| 10 | Đọc Explanation | Hệ thống giải thích tại sao liquidity và interbank rate thay đổi | Explanation panel |
| 11 | Nhấn Next Phase | Kết quả hiện tại được lưu làm trạng thái cho lượt tiếp theo | Transaction Log + Updated State |

### Error Path

### Error 1 - Missing input

Ví dụ user chưa nhập Volume.

| Step | User action | System response | Evidence |
| --- | --- | --- | --- |
| 1 | Chọn OMO Action | Hệ thống hiển thị các trường hợp cần nhập | Decision Area |
| 2 | Nhấn Submit nhưng bỏ trống Volume | Hệ thống không chạy auction | Validation message |
| 3 | Nhập Volume hợp lệ | Hệ thống xác nhận input | Validated input |
| 4 | Nhấn Submit | Auction được thực hiện | Auction Result |

### Error 2 - Invalid input

Ví dụ: User nhập Volume = −3,500 hoặc Repo/Reverse repo rate = -4% trong khi Volume và Repo/Reverse repo rate phải là một giá trị dương.

| Step | User action | System response | Evidence |
| --- | --- | --- | --- |
| 1 | Nhập Volume và Repo/Reverse repo rate không hợp lệ | Hệ thống phát hiện lỗi | Validation warning |
| 2 | Sửa Volume, Repo/Reverse repo rate | Hệ thống kiểm tra lại | Valid input |
| 3 | Submit | Auction được thực hiện | Auction Result |

## 4. Interface

### Input design

| Input | Interface label | Type / unit | Required? | Valid input / range | Example / default | User guidance / validation |
| --- | --- | --- | --- | --- | --- | --- |
| OMO Auction Method | Auction Method | Categorical | Required | Interest-rate Auction / Volume Auction | Interest-rate Auction | Determines whether banks bid rates or volumes |
| Pricing Method | Pricing Method | Categorical | Conditional | Single-price / Multi-price | Single-price | Available only for Interest-rate Auction |
| OMO Action | Action | Categorical | Required | Buy Securities / Sell Securities / REPO / Reverse REPO | - | Determines the direction of liquidity impact |
| Volume | Volume (billion) | Numeric, billion | Required | > 0; within the system's allowed auction limit | 3500 | Enter the target transaction volume |
| Repo/ Reverse repo Rate | Auction Rate (%) | Numeric, % per year | Conditional | Within the allowed rate range | 4.00% | Available only for Volume Auction |

### Output design

**Main results (with comparison)**
- Interbank Rate: Interbank Rate: 4.27% (↑ +0.27%)

**Supporting outputs: Auction Result**
| Output | Example | Purpose |
| --- | --- | --- |
| Real Volume | 3,500 billion | Cho biết lượng giao dịch thực tế được thực hiện |
| Execution Rate | 4.00% | Cho biết mức lãi suất thực hiện |

**Explanation**

- Why did the Liquidity Gap become positive? The liquidity injected/absorbed through OMO, together with maturing OMO transactions, resulted in total supply below the system's liquidity demand.

- Why did the interbank rate increase? Liquidity Gap is positive because liquidity demand is higher than total supply. The resulting liquidity shortage creates upward pressure on the interbank rate..

**Limitation: Hiển thị ở vị trí không nổi bật**

- Model limitation: The interbank rate is estimated using the designer's regression model and previous-period market conditions. It is a simulation result and does not represent a forecast of the actual market rate.

- Interpretation note: Liquidity Gap reflects the aggregate liquidity position of the system. It does not imply that every commercial bank has the same liquidity position.

**Next Action: Cuối giao diện người dùng**

- Submit →

- Next Phase →

### Interface Explainability

| Element | Purpose | Example |
| --- | --- | --- |
| Short explanation | Mô tả trạng thái của kết quả mà người chơi tạo ra | “The banking system is in liquidity shortage.” |
| Breakdown | Thể hiện các yếu tố / chỉ số ảnh hưởng đến chỉ số hiện tại | Liquidity Demand − Total Supply = Liquidity Gap |
| Reason statement | Giải thích lí do dẫn đến kết quả mà người chơi tạo ra | “Liquidity demand exceeded total liquidity supply.” |
| Warning | Làm nổi bật các chỉ số không nằm trong vùng an toàn của người chơi | ⚠ / red highlight |
| Assumption box | Làm rõ các giả thuyết của game và mô hình áp dụng trong game | “Interbank rate is estimated using the simulated liquidity condition and previous rate.” |
| Tooltip | Giải thích ngắn về ý nghĩa của các chỉ số | ? beside “Interbank Rate” |
| Comparison | Thể hiện sự thay đổi của chỉ số so với phase trước | 4.27% ↑ 0.27% |

## 5. Working interface draft

[INTERFACE DRAFT](https://kipsoos.github.io/WTFAID/)

## 6. Revision evidence

- Thiết kế flow: Minh Ngọc, Khánh Linh

- Viết input: Minh Ngọc, Khánh Linh

- Triển khai: Khánh Linh, Minh Trang

- Explanation: Bảo Hiền, Khánh Linh

- Kiểm tra error path: Bảo Hiền

- Tích hợp: Minh Trang

