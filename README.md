# GROUP README

## Tên sản phẩm

WHO RUNS THE WORLD?

## Mã nhóm

G03

## Thành viên

| Họ tên | Mã sinh viên | Vai trò chính |
|---|---|---|
| Vũ Lưu Minh Ngọc | 2412380037 | Game Engine & Backend Developer |
| Nguyễn Bảo Hiền | 2412380017 | Economic Model & Finance |
| Nguyễn Minh Trang | 2412380049 | UI/UX & Learning Experience |
| Nguyễn Khánh Linh | 2413380027 | Game Logic & Scenario Designer |

## Mô tả ngắn về sản phẩm

WHO RUNS THE WORLD? - Game mô phỏng điều hành chính sách tiền tệ, trong đó người chơi đóng vai Ngân hàng Trung ương và đưa ra quyết định lãi suất dựa trên tình hình kinh tế của một quốc gia.

Người chơi phải cân bằng giữa kiểm soát lạm phát, hỗ trợ tăng trưởng kinh tế và duy trì ổn định tài chính thông qua các quyết định chính sách và dự báo kinh tế.

## Vấn đề sản phẩm giải quyết

Sinh viên quan tâm đến lĩnh vực Ngân hàng Nhà nước và chính sách tiền tệ thường gặp khó khăn trong việc hiểu mối quan hệ giữa các chỉ số kinh tế và tác động của quyết định chính sách.

Việc học lý thuyết đơn thuần chưa cho người học cơ hội trực tiếp thử nghiệm các quyết định và quan sát hệ quả của chúng.

WHO RUNS THE WORLD? biến các khái niệm về chính sách tiền tệ thành một môi trường mô phỏng, cho phép người chơi ra quyết định → quan sát kết quả → học từ sai lầm → điều chỉnh chính sách.

## Người dùng mục tiêu

Sinh viên/HSSV quan tâm đến lĩnh vực Ngân hàng Nhà nước, quản trị ngân hàng và chính sách tiền tệ nhưng chưa có kiến thức chuyên sâu.

## Tính năng chính

- Cho phép người chơi đóng vai Central Bank và điều hành chính sách tiền tệ thông qua nghiệp vụ thị trường mở (OMO).
- Mô phỏng nền kinh tế thông qua nhiều giai đoạn (phases), trong đó mỗi phase tương đương 7 ngày và kết quả của phase trước được carry forward sang phase tiếp theo.
- Mỗi phase cung cấp một economic scenario với các thông tin như Deposit Rate, Lending Rate, Liquidity Demand, Interbank Rate, Inflation, Real GDP Growth, Unemployment Rate, Nominal Interest Rate và News/Event.
- Cho phép người chơi lựa chọn OMO Auction Method: Interest-rate auction hoặc Volume auction.
- Cho phép người chơi lựa chọn OMO Action nhằm bơm hoặc hút thanh khoản: Reverse Repo/Repo/Buy Securities/Sell Securities.
- Cho phép người chơi quyết định Volume; đối với đấu thầu khối lượng, người chơi/NHTW ấn định Discount rate/Repo rate.
- Cho phép người chơi đưa ra Expected Inflation để thể hiện dự báo của mình về nền kinh tế.
- Mô phỏng phản ứng và lệnh dự thầu của các NHTM; MVP giả định các NHTM có phản ứng tương đối giống nhau.
- Với đấu thầu lãi suất, hệ thống xếp lệnh theo lãi suất, cộng dồn khối lượng, xác định mức cắt và khối lượng trúng thầu; MVP hiện áp dụng phương thức xét thầu đơn giá.
- Với đấu thầu khối lượng, NHTW ấn định lãi suất và các NHTM quyết định khối lượng đặt thầu; nếu tổng cầu lớn hơn khối lượng chào thầu, hệ thống phân bổ theo tỷ lệ.
- Sử dụng Economic Engine để mô phỏng chuỗi tác động: OMO → System Liquidity → Interbank Rate → Lending/Deposit Rate, Liquidity và Macroeconomic Indicators.
- Sử dụng real data làm cơ sở cho các biến kinh tế và dữ liệu OMO; sample/simulated data được sử dụng cho dữ liệu dự thầu NHTM khi dữ liệu thực tế không sẵn có.
- Áp dụng các logic test để kiểm tra các điều kiện như khối lượng trúng không vượt khối lượng đặt, tổng khối lượng trúng không vượt khối lượng chào thầu và phân bổ đúng trong trường hợp dư cầu/thiếu cầu.
