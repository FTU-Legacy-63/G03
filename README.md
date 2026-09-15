# GROUP README

## Tên sản phẩm

WHO RUNS THE WORLD?

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
- Indicators: Hiển thị các chỉ tiêu thanh khoản và các chỉ số kinh tế trong phase hiện tại
- OMO Decision: Cho phép người chơi chọn Auction Type, Pricing Method, OMO Action, Volume và Rate
- OMO Auction Engine: Mô phỏng phản ứng và lệnh dự thầu của các NHTM; MVP giả định các NHTM có phản ứng tương đối giống nhau.
- Economic Engine: Mô phỏng chuỗi tác động: OMO → System Liquidity → Interbank Rate → Lending/Deposit Rate, Liquidity và Macroeconomic Indicators.
- Sử dụng real data làm cơ sở cho các biến kinh tế và dữ liệu OMO; sample/simulated data được sử dụng cho dữ liệu dự thầu NHTM khi dữ liệu thực tế không sẵn có.
- Outcome / Result: Hiển thị kết quả của quyết định OMO
