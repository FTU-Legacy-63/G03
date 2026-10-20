# REVISION SUMMARY

## 1. Tổng quan

WHO RUNS THE WORLD? là trò chơi mô phỏng nghiệp vụ thị trường mở của nhnn, kết hợp giao diện tương tác với một bộ máy xử lý nghiệp vụ ở phía máy chủ.

## 2. Các thành phần chính

- **Giao diện người dùng (Frontend):** HTML, CSS và JavaScript; cung cấp các màn hình nhập quyết định, xem thông tin thị trường và theo dõi kết quả.
- **Hệ thống mô phỏng (Backend):** Python; xử lý quyết định OMO, đấu thầu, thanh khoản, lãi suất liên ngân hàng, dòng tiền đáo hạn và các biến số kinh tế vĩ mô.
- **Kết nối frontend–backend (APIs):** giao diện gửi yêu cầu đến các API để khởi tạo trò chơi và xử lý từng giai đoạn.

## 3. Các nội dung sửa đổi quan trọng

- Hoàn thiện backend và tích hợp APIs để kết nối backend và frontend. <br>Hoàn thiện các logic xử lý nghiệp vụ và tính toán trong backend; sử dụng Flask để triển khai các API phục vụ trao đổi dữ liệu giữa backend và frontend.
- Điều chỉnh giao diện và bố cục các trang báo cáo.
  <br> Thay đổi thiết kế giao diện (background, tone màu và layout) nhằm cải thiện tính thẩm mĩ và trực quan.
- Thêm hành động sắp xếp hồ sơ dự thầu của NHTM để giúp người chơi hiểu hơn về cách sắp xếp thứ tự ưu tiên trong đấu thầu và tăng tính tương tác của game.
- Bỏ việc cố định lựa chọn về phương thức đấu thầu, cho phép người chơi lựa chọn tự do.
  <br> Theo dự định ban đầu, nhóm phát triển dự tính cố định phương thức đấu thầu (ĐT lãi suất / ĐT khối lượng) trong 2 phases đầu tiên để đảm bảo người chơi trải nghiệm tất cả các phương thức đấu thầu. Quyết định thay đổi này nhằm tăng tính chủ động trong quá trình ra quyết định và tạo điều kiện để đánh giá sự phù hợp của lựa chọn với bối cảnh thực tế của từng phase.
- Điều chỉnh các công thức kinh tế vĩ mô để thể hiện rõ hơn sự truyền dẫn của chính sách tiền tệ.
  <br> Rà soát và điều chỉnh các công thức tính toán Output Gap, tăng trưởng GDP và lạm phát, đồng thời cập nhật các tham số tương ứng. Các điều chỉnh hướng đến việc thể hiện rõ hơn cơ chế truyền dẫn của chính sách tiền tệ, trong đó quyết định điều hành lãi suất tác động đến lãi suất thực, qua đó ảnh hưởng đến các chỉ số kinh tế vĩ mô.
- Quy luật xây dựng giải thích và đánh giá quyết định người chơi sau mỗi phase được triển khai cụ thể cho bối cảnh riêng của từng phase.
  <br> Xây dựng quy tắc giải thích và đánh giá quyết định của người chơi gắn với điều kiện thanh khoản, trạng thái thị trường và diễn biến cụ thể của từng phase. Thay vì áp dụng một cách giải thích chung cho mọi tình huống như dự định ban đầu, nội dung phản hồi được thiết kế theo bối cảnh tương ứng, làm rõ mức độ phù hợp của quyết định với mục tiêu điều hành, tác động dự kiến và những điểm người chơi cần cân nhắc.
- Thiết kế giao diện và xây dựng quy luật đánh giá cho Final Summary sau toàn bộ 9 phases.
  <br> Xây dựng giao diện trang Final Summary tổng hợp các kết quả và diễn biến của các chỉ số quan trọng trong quá trình điều hành. Đồng thời, thiết lập các quy tắc đánh giá nhằm xem xét chất lượng các quyết định của người chơi xuyên suốt trò chơi, giúp người chơi nhìn lại tính nhất quán trong định hướng điều hành và kết quả đạt được sau toàn bộ quá trình.

## 4. Công việc có thể phát triển tiếp

- Mở rộng kiểm thử tự động.
- Kiểm tra tính nhất quán giữa dữ liệu frontend và backend.
- Hiệu chỉnh các tham số mô hình khi có cơ sở dữ liệu phù hợp.
- Cải thiện khả năng giải thích kết quả để hỗ trợ mục tiêu học tập.
