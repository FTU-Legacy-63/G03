# TESTING

## 1. Objective

Kiểm tra tính hợp lệ của dữ liệu đầu vào, hoạt động của cơ chế đấu thầu, việc tính toán thanh khoản và lãi suất liên ngân hàng, cũng như quá trình cập nhật các biến số kinh tế vĩ mô qua các giai đoạn.

## 2. Platforms

- Ngôn ngữ lập trình: Python và JavaScript.
- Giao diện: HTML, CSS và JavaScript.
- Backend: Python.
- Công cụ kiểm thử tự động: pytest.
- Môi trường triển khai: Render

## 3. Test table

| Nội dung kiểm thử                                   | Kết quả mong đợi                                                                                                                            | Kết quả thực tế |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| Khởi tạo trò chơi                                   | Trò chơi khởi tạo thành công với các tham số ban đầu như đã gán trong backend (Interbank Rate = 3.95%, Scenario Liquidity Demand = 4000 bn) | Pass            |
| Đọc Hướng dẫn chơi và các Learning Card             | Guide và Learning Card hiển thị trên pop-up window                                                                                          | Pass            |
| Nhập quyết định OMO hợp lệ                          | Hệ thống chấp nhận quyết định và xử lý được giai đoạn.                                                                                      | Pass            |
| Nhập khối lượng âm                                  | Hệ thống gửi thông báo dữ liệu không hợp lệ                                                                                                 | Pass            |
| Đấu thầu theo khối lượng nhưng thiếu lãi suất       | Hệ thống không cho phép gửi quyết định                                                                                                      | Pass            |
| Lãi suất vượt giới hạn cho phép                     | Hệ thống gửi thông báo dữ liệu không hợp lệ                                                                                                 | Pass            |
| Sắp xếp thứ tự ưu tiên của các ngân hàng            | Hệ thống chỉ cho phép tiếp tục khi thứ tự ưu tiên được sắp xếp theo đúng quy luật.                                                          | Pass            |
| Xử lý kết quả đấu thầu                              | Khối lượng dự thầu và kết quả phân bổ đúng theo quy tắc của financial logic và backend                                                      | Pass            |
| Cập nhật Interbank Rate và các chỉ số kinh tế vĩ mô | Các biến số được tính toán theo đúng quy tắc của financial logics và backend, phù hợp tương đối với quy luật kinh tế.                       | Pass            |
| Giải thích và đánh giá sau phase                    | Giải thích đúng với quy luật đã xây dựng, đúng với diễn biến thanh khoản và kinh tế đã xảy ra trong phase                                   | Pass            |
