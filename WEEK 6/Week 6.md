# WEEK 6
**1\. Core flow và components**  
Technical end-to-end flow: Frontend (omo_refactored_v64.html) → Flask API (app.py) → Python Engine (central_bank_engine_v13.py) → Results UI. Python engine là nguồn dữ liệu chuẩn cho tính toán.

- Frontend: Indicators, Decisions và Results; nhận quyết định OMO từ người dùng và hiển thị kết quả.  
- Flask API: phục vụ frontend; /api/start-game khởi tạo game; /api/run-phase thực thi Phase.  
- OMO Engine: xử lý Decision validation, auction, cung/cầu thanh khoản, truyền dẫn lãi suất liên ngân hàng, tồn kho tín phiếu, Repo/Reverse Repo và đáo hạn

**2\. Deployment hoặc working build**

| Item | Status |
| ----- | ----- |
| Public URL mở được | Checked |
| Link nằm trong README | README có chứa public URL |
| Thử trên thiết bị khác | Checked |
| Dependencies rõ | requirements.txt chứa flask, flask-cors, gunicor|
| Build command chạy | pip install \-r requirements.txt chạy thành công |
| Các file code/data được include | app.py, central_bank_engine_v13.py, omo_refactored_v64.html và requirements.txt nằm trong thư mục WEEK 6 |
| Secrets không nằm trong repo | Không commit API key, password hoặc credential |
| Có hướng dẫn chạy local | README giải thích cách setup và chạy local |
| Có backup demo | Có commit ổn định/video có thể dùng demo |

**3\. Test table**
<br>[Test table](https://github.com/FTU-Legacy-63/G03/blob/main/testing.md)

**4\. Bug log and critical fixes**

| Bug | Vị trí / Cách tái hiện | Expected | Actual | Severity | Status |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Game không gọi được API khi truy cập qua đường link public. | Frontend | Các request được gửi đến API của website đang chạy. | Code gọi 127.0.0.1, địa chỉ trỏ đến máy của người chơi thay vì server đã deploy. | Critical | ĐÃ SỬA  |
| Render không tìm thấy dependency file. | Render build khi file tên requirement.txt. | Render tìm thấy requirements.txt và cài đặt đầy đủ các thư viện cần thiết. | File được đặt tên requirement.txt hoặc không nằm trong thư mục mà Render sử dụng để build. | Critical | ĐÃ SỬA  |
| Double-click khiến một quyết định được gửi nhiều lần. | startGame() / submitDecision() | Mỗi quyết định chỉ được xử lý một lần và phase chỉ tiến lên theo đúng quy trình.| Mỗi lần click được coi là 1 lần gửi quyết định của 1 phase, gây cập nhật state trùng lặp. | Critical | ĐÃ SỬA |
| Người chơi khó có thể thay đổi trạng thái thanh khoản (Dư / Thiếu) giữa các phase nếu không có cú sốc kịch bản. | Backend | Người chơi có thể bơm hoặc hút quá so với nhu cầu thanh khoản. | Do Total Bid Volume bị giới hạn bởi nhu cầu thanh khoản thực tế và tác động của chiết khấu, trạng thái kinh tế có xu hướng duy trì gần giống phase trước, trừ khi xuất hiện cú sốc kịch bản. | Major | ĐÃ SỬA |
| Dữ liệu biểu đồ không khớp với Results và backend | Chart GDP/inflation | Các thành phần hiển thị cùng nguồn dữ liệu, cùng phase.| Biểu đồ dùng dữ liệu cũ hoặc không phản ánh kết quả gameplay thực tế. | Major | ĐÃ SỬA |
| Các bảng inventory trên trang Results không cập nhật sau khi chạy Phase. | Frontend | Các bảng hiển thị đúng trạng thái mới nhất (tính toán với backend) sau khi Phase hoàn tất. | Giao diện vẫn sử dụng dữ liệu cũ thay vì cập nhật theo dữ liệu mới từ Python backend. | Major | ĐÃ SỬA |
| Các chỉ số không thay đổi theo quy luật kinh tế thông thường | Công thức của các chỉ số vĩ mô | Thiếu thanh khoản nặng hơn thì GDP và lạm phát thấp hơn, và hai chỉ số cùng chiều. | GDP growth và inflation tăng mạnh khi thiếu thanh khoản nghiêm trọng. | Major | ĐÃ SỬA |

**5\. Scope freeze**

| Item | Status |
| ----- | ----- |
| Frozen scope | Mô phỏng OMO 9 Phases; Indicators → Decisions → Results; Flask API; Python OMO engine; auction; liquidity; inventory; Repo/Reverse Repo; maturity; interbank output. |
| Postponed feature | Các feature gameplay mới hoặc flow khái niệm mới ngoài phạm vi. |
| Known limitation | Deployment cuối, kiểm tra đa thiết bị, README hoàn chỉnh và backup demo vẫn cần được xác nhận. |
| Các thay đổi được phép sau freeze | Chỉ sửa critical bugs và tiếp tục testing. |

**6\. Contribution evidence** 
<br> \- Component completed by: Minh Ngọc, Minh Trang  
\- Integrated by: Khánh Linh  
\- Bug reported by: Bảo Hiền  
\- Fixed by: Minh Ngọc, Minh Trang, Khánh Linh

