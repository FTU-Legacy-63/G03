# SOLUTION STRUCTURE

## 1. Product Direction

- Sản phẩm là một ứng dụng mô phỏng giáo dục, trong đó người chơi đóng vai **Ban Điều hành Nghiệp vụ Thị trường mở của NHTW tại Quốc gia X**.
- Mục tiêu cốt lõi: giúp người chơi hiểu cách NHTW sử dụng **Nghiệp vụ Thị trường Mở (OMO)**, cụ thể là **đấu thầu tín phiếu**, để điều tiết thanh khoản và tác động đến lãi suất thị trường tiền tệ.

---

## 2. Core User Flow

**Scenario → Economic Data → User Analysis → OMO Decision → Auction → Economic Engine → Updated Indicators → Outcome & Report → Next Phase**

Kết quả của phase trước được giữ lại và trở thành trạng thái ban đầu của phase tiếp theo.

---

## 3. Initial Required Information

### Macroeconomic Indicators

- Real GDP Growth
- Inflation
- Unemployment rate 
- Credit Growth
- ...

### Banking & Money Market Indicators

- Thanh khoản hệ thống ngân hàng
- Lãi suất liên ngân hàng
- Các nghiệp vụ OMO đang đáo hạn nếu có

### Auction Information

- Mua/Bán tín phiếu
- Khối lượng
- Kỳ hạn
- Phương thức đấu thầu
- Lãi suất áp dụng nếu sử dụng đấu thầu khối lượng

### Thông tin ẩn của NHTM

Game mô phỏng:

- Nhu cầu thanh khoản
- Khối lượng muốn giao dịch
- Mức lãi suất chấp nhận
- Chiến lược đặt thầu

---

## 4. Core Process Type

**State(t) + Scenario(t) + User Decision(t) → Auction Engine → Economic Engine → State(t+1)**

Quy trình:

**Phân tích → Quyết định → Đấu thầu → Mô phỏng → Giải thích**

Auction Engine xác định:

- Khối lượng đặt thầu
- Khối lượng trúng thầu
- Lãi suất áp dụng/trúng thầu
- Kết quả phân bổ

Economic Engine sau đó cập nhật:

**OMO → Thanh khoản → Lãi suất liên ngân hàng**

Tác động dài hạn được thể hiện theo hướng:

**Lãi suất → Tín dụng/Cung tiền → Tổng cầu → GDP/Lạm phát**

---

## 5. MVP Flow for Each Phase

### Phase 1 – Đấu thầu khối lượng

1. Người chơi nhận Market Dashboard và scenario.
2. Game quy định phương thức **đấu thầu khối lượng**.
3. Người chơi đưa ra quyết định OMO.
4. NHTW xác định lãi suất.
5. NHTM mô phỏng quyết định khối lượng đặt thầu.
6. Game xác định khối lượng trúng thầu.
7. Thanh khoản và lãi suất liên ngân hàng được cập nhật.
8. Game giải thích kết quả.

### Phase 2 – Đấu thầu lãi suất

1. Người chơi nhận scenario mới.
2. Game quy định phương thức **đấu thầu lãi suất**.
3. Người chơi đưa ra quyết định OMO.
4. NHTM mô phỏng gửi khối lượng và lãi suất dự thầu.
5. Game xác định khối lượng và lãi suất trúng thầu.
6. Các chỉ số thị trường được cập nhật.
7. Game giải thích cơ chế hình thành lãi suất.

### Phase 3 – Auction Trade-off

1. Người chơi nhận Market Dashboard và mục tiêu điều hành.
2. Phân tích điều kiện thị trường.
3. Quyết định mua/bán tín phiếu.
4. Quyết định khối lượng và kỳ hạn.
5. Tự lựa chọn **đấu thầu khối lượng hoặc đấu thầu lãi suất**.
6. NHTM phản ứng và gửi lệnh dự thầu.
7. Game chạy Auction Engine.
8. Xác định kết quả đấu thầu.
9. Economic Engine cập nhật thanh khoản và lãi suất.
10. Game trả về Decision-Consequence Card.
11. Người chơi điều chỉnh chiến lược cho vòng tiếp theo.

---

## 6. Target Product Direction

Game gồm 3 phase:

- **Phase 1:** Học cơ chế đấu thầu khối lượng.
- **Phase 2:** Học cơ chế đấu thầu lãi suất.
- **Phase 3:** Tự lựa chọn phương thức đấu thầu và kỳ hạn dựa trên điều kiện thị trường.

Phase 3 tập trung vào trade-off giữa:

**Rate Control ↔ Price Discovery**

và:

**Policy Signaling ↔ Market Efficiency**

Không có một phương thức đấu thầu luôn tối ưu trong mọi scenario.

---

## 7. Product Interface

### 3 tabs chính

**Scenario**

- Bối cảnh kinh tế
- Market Dashboard
- Mục tiêu điều hành
- Thông tin hướng dẫn

**Decisions**

- Mua/Bán tín phiếu
- Khối lượng
- Kỳ hạn
- Phương thức đấu thầu
- Lãi suất nếu cần

**Reports**

- Kết quả đấu thầu
- Khối lượng OMO thực tế
- Lãi suất sau đấu thầu
- Thanh khoản hệ thống
- Lãi suất liên ngân hàng
- Decision-Consequence Card
- Các tác động kinh tế ở những kỳ tiếp theo

---

## 8. MVP Scope

- Giả lập một quốc gia duy nhất.
- Người chơi đóng vai Ban Điều hành Nghiệp vụ Thị trường mở.
- Công cụ quyết định giới hạn ở **mua/bán tín phiếu thông qua đấu thầu**.
- Đấu thầu khối lượng.
- Đấu thầu lãi suất.
- Mô phỏng hành vi đặt thầu của NHTM.
- Auction Engine.
- Economic Engine tập trung vào:

**OMO → Thanh khoản → Lãi suất liên ngân hàng**

- Decision-Consequence Card.
- Ba phase có trạng thái liên kết với nhau.

---

## 9. Target Scope

Nếu có đủ thời gian và dữ liệu:

- Mở rộng số lượng scenario.
- Calibration Auction Engine bằng dữ liệu Việt Nam.
- Mô phỏng hành vi NHTM chi tiết hơn.
- Mở rộng consequence layer:

**OMO → Lãi suất → Tín dụng/Cung tiền → GDP/Lạm phát**

- Bổ sung nhiều loại shock và điều kiện thị trường khác nhau.

---

## 10. Fallback Scope

Nếu dữ liệu hoặc mô hình quá phức tạp:

- Giữ nguyên cấu trúc 3 phase.
- Đơn giản hóa hành vi đặt thầu của NHTM.
- Sử dụng rule-based simulation cho một số biến không có dữ liệu.
- Mô hình định lượng cốt lõi chỉ tập trung vào:

**OMO → Thanh khoản → Lãi suất liên ngân hàng**

- GDP và lạm phát chỉ được thể hiện dưới dạng consequence/scenario.

---

## 11. Out of Scope for MVP

- Dự trữ bắt buộc.
- Can thiệp tỷ giá.
- Trần tăng trưởng tín dụng.
- Quyết định lãi suất chính sách.
- Chính sách tài khóa.
- Mô phỏng bảng cân đối chi tiết của từng NHTM.
- Dự báo chính xác GDP từ một phiên OMO.
- Tái hiện chính xác 100% nền kinh tế thực.
- Multiplayer.

---

## 12. Initial Route Hypothesis

1. Làm bản demo Excel để kiểm tra quy tắc đấu thầu và cách tính kết quả.
2. Thu thập dữ liệu OMO và thị trường liên ngân hàng Việt Nam.
3. Xây dựng Auction Engine cho đấu thầu khối lượng và đấu thầu lãi suất.
4. Xây dựng Economic Engine cho:

   **OMO → Thanh khoản → Lãi suất liên ngân hàng**

5. Xây Phase 1 để kiểm tra cơ chế đấu thầu khối lượng.
6. Xây Phase 2 để kiểm tra cơ chế đấu thầu lãi suất.
7. Xây Phase 3 để kiểm tra trade-off giữa hai phương thức.
8. Sau khi logic và mô hình ổn định, chuyển sang giao diện game.
