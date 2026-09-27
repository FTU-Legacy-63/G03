# WEEK 6
**1\. Core flow và components**  
Technical end-to-end flow: Frontend (index.html) → Flask API (app.py) → Python Engine (central\_bank\_engine.py) → Results UI. Python engine là nguồn dữ liệu chuẩn cho tính toán.

- Frontend: Indicators, Decisions và Results; nhận quyết định OMO từ người dùng và hiển thị kết quả.  
- Flask API: phục vụ index.html; /api/start-game khởi tạo game; /api/run-phase thực thi Phase.  
- OMO Engine: xử lý Decision validation, auction, cung/cầu thanh khoản, truyền dẫn lãi suất liên ngân hàng, tồn kho T-bill, Repo/Reverse Repo và đáo hạn

**2\. Deployment hoặc working build**

| Item | Status |
| ----- | ----- |
| Public URL mở được | Checked |
| Link nằm trong README | README có chứa public URL. |
| Thử trên thiết bị khác | Checked |
| Dependencies rõ | requirements.txt chứa flask, flask-cors, gunicorn. |
| Build command chạy | pip install \-r requirements.txt chạy thành công. |
| Các file code/data được include | app.py, central\_bank\_engine.py, index.html và requirements.txt nằm trong thư mục WEEK 6\. |
| Secrets không nằm trong repo | Không commit API key, password hoặc credential. |
| Có hướng dẫn chạy local | README giải thích cách setup và chạy local. |
| Có backup demo | Có commit ổn định/video/screenshot hoặc bản backup có thể dùng demo. |

**3\. Test table**

| Case | Input | Expected | Actual | Status |
| ----- | ----- | ----- | ----- | ----- |
| Normal | Start game; 02/02/2025; lãi suất 3.95% | Game khởi tạo; trả về tồn kho T-bill. | start\_game khởi tạo CentralBankGame và trả current date, rate và inventory. | PASS |
| Normal | Interest-rate auction hợp lệ \+ action hợp lệ \+ volume \> 0 | Decision được chấp nhận; auction được thực hiện. | Decision.validate() chấp nhận tổ hợp hợp lệ; run\_phase trả kết quả auction/liquidity. | PASS |
| Normal | Buy Securities / Reverse Repo với T-bill khả dụng | Bơm thanh khoản; inventory giảm theo volume thực hiện. | Engine giới hạn hai action này theo T-bill khả dụng/đủ điều kiện. | PASS |
| Normal | Sell Securities / Repo | Hút thanh khoản; Sell tạo lot; Repo tạo vị thế đang hoạt động. | Engine ghi nhận trạng thái inventory/Repo. | PASS |
| Boundary | Volume \= 0 | UI từ chối submit. | submitDecision() cảnh báo và dừng trước khi gọi API. | PASS |
| Boundary | Auction rate \= 0% hoặc 10% trong Volume auction | Giá trị biên được chấp nhận. | Decision.validate() chấp nhận khoảng bao gồm cả 0–10%. | PASS |
| Invalid | Volume âm | Request bị từ chối; không thực thi Phase. | Decision.validate() raise ValueError: Volume must be \>= 0\. | PASS |
| Invalid | Volume auction nhưng không có auction rate | Request bị từ chối. | Decision.validate() yêu cầu auction rate. | PASS |
| Invalid | Interest-rate auction nhưng không có pricing method | Request bị từ chối. | Decision.validate() yêu cầu Single-price hoặc Multi-price. | PASS |
| Financial | Thực hiện OMO có kỳ hạn rồi đến maturity | Đáo hạn đảo chiều tác động của nghiệp vụ có kỳ hạn và ghi nhận dòng tiền. | process\_maturities() xóa item đã đáo hạn và ghi maturity\_events. | PASS |
| Financial | So sánh RLD, total supply và gap | Gap \= RLD \- total supply. | run\_phase() tính và lưu liquidity\_gap tương ứng. | PASS |
| Integration | Chạy Phase từ public Render URL trên thiết bị khác | API same-origin truy cập được; Results hiển thị. | Checked | PASS |

**4\. Bug log and critical fixes**

|  | Vị trí / Cách tái hiện | Expected | Actual | Severity | Trạng thái sửa |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Các bảng inventory trên Results không cập nhật sau khi chạy Phase. | index.html — legacy renderer; chạy Phase rồi kiểm tra các bảng inventory. | Hiển thị trạng thái hiện tại từ Python backend. | Legacy JS renderer đọc state JS cũ thay vì state từ server. | Major | ĐÃ SỬA |
| Deployment public gọi API localhost. | index.html — startGame/submitDecision trên public URL. | Gọi API same-origin của deployment. | 127.0.0.1 trỏ tới máy của người dùng. | Critical | ĐÃ SỬA  |
| Render không tìm thấy dependency file. | Render build khi file tên requirement.txt. | Build tìm thấy requirements.txt. | requirements.txt không nằm trong build working directory. | Critical | ĐÃ SỬA  |

**5\. Scope freeze**

| Item | Status |
| ----- | ----- |
| Frozen scope | Mô phỏng OMO 3 Phase; Indicators → Decisions → Results; Flask API; Python OMO engine; auction; liquidity; inventory; Repo/Reverse Repo; maturity; interbank output. |
| Postponed feature | Các feature gameplay mới hoặc flow khái niệm mới ngoài phạm vi integration/testing được hoãn. |
| Known limitation | Deployment cuối, kiểm tra đa thiết bị, README hoàn chỉnh và backup demo vẫn cần được xác nhận. |
| Các thay đổi được phép sau freeze | Chỉ sửa critical bugs, major clarity issues, deployment, documentation và test failures. |

**6\. contribution evidence** 
\- Component completed by: Minh Ngọc, Minh Trang  
\- Integrated by: Khánh Linh  
\- Bug reported by: Bảo Hiền  
\- Fixed by: Minh Ngọc, Minh Trang, Khánh Linh

