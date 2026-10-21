# GROUP README

## Tên sản phẩm

[WHO RUNS THE WORLD?](https://who-runs-the-world-xajm.onrender.com/)

## Mã nhóm

G03

## Thành viên

| Họ tên | Mã sinh viên | Vai trò chính |
|---|---|---|
| Vũ Lưu Minh Ngọc | 2412380037 | Backend Develop |
| Nguyễn Bảo Hiền | 2412380017 | Game Logic & Scenario Design |
| Nguyễn Minh Trang | 2412380049 | UI/UX & User Experience |
| Nguyễn Khánh Linh | 2413380027 | Economic Model |

## Mô tả ngắn về sản phẩm

WHO RUNS THE WORLD? - Game mô phỏng điều hành chính sách tiền tệ, tập trung vào nghiệp vụ thị trường mở (OMO), trong đó người chơi đóng vai Ban điều hành Nghiệp vụ thị trường mở thuộc NHNN và đưa ra quyết định dựa trên tình hình kinh tế của một quốc gia.

Người chơi phải cân bằng giữa kiểm soát lạm phát, hỗ trợ tăng trưởng kinh tế và duy trì ổn định tài chính thông qua các quyết định chính sách và dự báo kinh tế.

## Vấn đề sản phẩm giải quyết

Sinh viên quan tâm đến lĩnh vực Ngân hàng Nhà nước và chính sách tiền tệ thường gặp khó khăn trong việc hiểu mối quan hệ giữa các chỉ số kinh tế và tác động của quyết định chính sách chính sách tiền tệ. 

Việc học lý thuyết đơn thuần chưa cho người học cơ hội trực tiếp thử nghiệm các quyết định và quan sát hệ quả của chúng.

WHO RUNS THE WORLD? biến các khái niệm về chính sách tiền tệ thành một môi trường mô phỏng, cho phép người chơi ra quyết định → quan sát kết quả → học từ sai lầm → điều chỉnh chính sách.

## Người dùng mục tiêu

Sinh viên/HSSV quan tâm đến lĩnh vực Ngân hàng Nhà nước, quản trị ngân hàng và chính sách tiền tệ nhưng chưa có kiến thức chuyên sâu.

## Tính năng chính

- Cho phép người chơi đóng vai Ban điều hành Nghiệp vụ thị trường mở và điều hành chính sách tiền tệ thông qua nghiệp vụ thị trường mở (OMO).
- Mô phỏng nền kinh tế thông qua nhiều giai đoạn (phases), trong đó mỗi phase tương đương 30 ngày và kết quả của phase trước được carry forward sang phase tiếp theo.
- Scenario / News Panel: Cung cấp bối cảnh kinh tế cho người chơi
- Guide & Learning Cards: Hướng dẫn chơi game và Thẻ học tập cung cấp kiến thức cơ bản về các chỉ số quan trọng.
- Indicators: Hiển thị các chỉ tiêu thanh khoản và các chỉ số kinh tế trong phase hiện tại
- OMO Decision: Cho phép người chơi chọn Auction Type, Pricing Method, OMO Action, Volume và Rate
- OMO Auction Engine: Mô phỏng phản ứng và lệnh dự thầu của các NHTM; MVP giả định các NHTM có phản ứng tương đối giống nhau.
- Economic Engine: Mô phỏng chuỗi tác động: OMO → System Liquidity → Interbank Rate → Macroeconomic Indicators.
- Outcome / Result: Hiển thị kết quả của quyết định OMO

## Hướng dẫn sử dụng

### 1. Sử dụng qua URL trực tiếp (Online)

Người chơi có thể truy cập trò chơi trực tiếp thông qua trình duyệt mà không cần cài đặt phần mềm.

1. Mở đường dẫn: [https://who-runs-the-world-xajm.onrender.com/](https://who-runs-the-world-xajm.onrender.com/)
2. Nhập tên đội chơi (**Team Name**) và chọn **Start Operations**.
3. Đọc báo cáo để nắm bắt tình hình kinh tế vĩ mô, thanh khoản và lãi suất liên ngân hàng. Người chơi có thể tham khảo Guide và các Learning Cards (nhấn vào biểu tượng ? bên cạnh các chỉ số) để tìm hiểu thêm về các khái niệm và chỉ số kinh tế.
4. Đưa ra quyết định nghiệp vụ thị trường mở (OMO), bao gồm lựa chọn công cụ, phương thức đấu thầu, khối lượng và lãi suất. Tại các phase 1, 4, 7, người chơi cần phải nhập Expected Inflation.
5. Sắp xếp hồ sơ dự thầu theo đúng thứ tự ưu tiên của nghiệp vụ tương ứng (tham khảo Learning Card của OMO Instrument).
6. Xem kết quả đấu thầu, phê duyệt giao dịch và theo dõi tác động của quyết định lên thị trường.
7. Tiếp tục thực hiện các giai đoạn (Phase) cho đến khi hoàn thành trò chơi.

### 2. Sử dụng trên máy chủ

Đối với người dùng muốn chạy trò chơi trực tiếp từ mã nguồn trên máy tính:

**Bước 1: Chuẩn bị môi trường**

- Cài đặt Python 3 trên máy tính.

- Tải toàn bộ mã nguồn dự án về máy, giữ nguyên cấu trúc thư mục và đảm bảo các file cần thiết như app.py, central_bank_engine_v13.py, omo_refactored_v64.html, requirements.txt và các asset được đặt đúng vị trí.

**Bước 2: Cài đặt thư viện**

Mở Terminal tại thư mục chứa dự án và chạy:

```bash
pip install -r requirements.txt
```

**Bước 3: Khởi động máy chủ**

```bash
python app.py
```

**Bước 4: Truy cập trò chơi**

Mở trình duyệt và truy cập địa chỉ máy chủ được hiển thị trong Terminal (thông thường là `http://127.0.0.1:5000`).

**Bước 5: Bắt đầu chơi**

Nhập tên đội, chọn **Start Operations** và thực hiện các bước tương tự như hướng dẫn sử dụng trực tuyến.

**Lưu ý:** Khi chạy trên máy chủ cục bộ, cần duy trì Terminal và tiến trình Python trong suốt thời gian chơi.
