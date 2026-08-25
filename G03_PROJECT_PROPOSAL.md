# PROJECT PROPOSAL

**1.  Problem Direction**

_Pain point:_ Sinh viên hiểu các khái niệm về cung tiền và các công cụ thực hiện chính sách tiền tệ như nghiệp vụ thị trường mở (OMO) ở mức lý thuyết, nhưng khó hình dung cách NHTW thực hiện và cách các quyết định dẫn đến thay đổi về thanh khoản, cung tiền và các biến số kinh tế vĩ mô.

_Giải pháp của game:_ Tạo lập môi trường cho sinh viên có thể thực hiện các quyết định liên quan đến Nghiệp vụ Thị trường Mở (OMO) để điều tiếtcung tiền và thanh khoản hệ thống.

**2.  Target User**

Sinh viên khối ngành Kinh tế, Tài chính - Ngân hàng tại Việt Nam muốn tìm hiểu về công cụ thực hiện chính sách tiền tệ của NHTWVN Nghiệp vụ Thị trường Mở (OMO) nhưng chưa có kiến thức sâu.

**3.  User task**

_Người chơi sẽ đóng vai trò là Ban Điều hành Nghiệp vụ Thị trường mở của NHTW. Trong mỗi Phase người chơi đối mặt với một kịch bản vĩ mô cụ thể và phải thực thi nhiệm vụ đưa nền kinh tế về trạng thái cân bằng mục tiêu thông qua:_

**Phân tích báo cáo vĩ mô:** Đọc các chỉ số vĩ mô thực tế (Tăng trưởng GDP, Lạm phát, Thất nghiệp, Nợ công/GDP), các thông tin thị trường, chỉ số thị trường tiền tệ (Thanh
khoản hệ thống ngân hàng, Lãi suất liên ngân hàng).

**Đưa ra quyết định OMO: Người chơi đưa ra quyết định can thiệp lượng tiền thông qua OMO:**

- Mua/Bán có kỳ hạn: Quyết định mua/bán tín phiếu từ các NHTM để bơm thêm lượng dự trữ khả dụng/Hút tiền từ hệ thống. Người chơi chọn đấu thầu lãi suất hoặc đấu thầu khối lượng và kỳ hạn.

- Phát hành/Mua lại Tín phiếu NHTW: Mua/Bán tín phiếu ngắn hạn để bơm/thu hồi tiền mặt khả dụng từ hệ thống NHTM. Người chơi chọn đấu thầu lãi suất hoặc đấu thầu khối lượng.

- Xử lý sự kiện đặc biệt (Scenario-specific decision): Đưa ra các quyết định phụ để đối phó với các cú sốc (như cú sốc thuế, thiên tai, đóng băng tín dụng, khủng hoảng địa chính trị).

**4.  Desired User Outcome**

- Hiểu bản chất Cung tiền là một dòng chảy được điều tiết liên tục qua OMO.

- Hiểu được cơ chế vận hành của Nghiệp vụ Thị trường mở và kết quả, ảnh hưởng của các quyết định lên các kênh truyền dẫn.

**5.  Product Statement**

Một trò chơi mô phỏng nghiệp vụ thị trường mở (OMO), trong đó người chơi đóng vai Ban Điều hành Nghiệp vụ Thị trường mở của NHTW, phân tích tình hình thị trường tiền tệ, thực hiện quyết định đấu thầu tín phiếu và quan sát tác động của quyết định đến thanh khoản hệ thống ngân hàng, lãi suất thị trường, cùng nền kinh tế nói chung.

**6.  Main Output**

- Giao diện Dashboard, bảng Chỉ số: Giao diện Web hiển thị các chỉ số tài chính - kinh tế

- Economic Engine: Tính toán tự động dựa trên các phương trình vĩ mô cốt lõi, phản hồi kết quả và vẽ đồ thị xu hướng vĩ mô sau mỗi lượt chơi.

- Report: KPI Card và Chart thể hiện performance của người chơi qua các phases, giải thích kênh truyền dẫn nào đã hoạt động hiệu quả hoặc thất bại trong lượt chơi của họ.

**7.  Product Pattern**

Scenario → Economic Data → User Analysis → Policy Decision → Economic Engine → Updated Economic Indicators → Outcome and Report → Next Phase

_Each phase represents a new economic condition and the outcome of the previous phase is carried forward._

**8.  Finance and Banking Relevance**

Trò chơi mô phỏng các nguyên lý và nghiệp vụ thực tế của NHTW thông qua các mô hình kinh tế như New Keynesian IS Curve, New Keynesian Phillips Curve, Okun's Law

2 Kênh truyền dẫn được mô phỏng:

- Kênh Lãi suất (main focus): Quyết định đấu thầu mua tín phiếu nói chung bơm tiền làm giảm lãi suất liên ngân hàng, kéo lãi suất cho vay thực xuống, ... thúc đẩy GDP tăng trưởng.

- Kênh Tín dụng: Quyết định đấu thầu bán Tín phiếu nói chung hút tiền làm cạn kiệt thanh khoản, các NHTM bắt buộc phải siết chặt vòi tín dụng đối với nền kinh tế kiềm chế tổng cầu hạ nhiệt lạm phát.

**9.  Feasibility**

-   Tính khả thi về công nghệ: Game được xây dựng bằng các công nghệ Web (HTML, CSS cho giao diện tương tác; Chart.js hoặc D3.js để vẽ đồ thị động). Economic Engine chỉ bao gồm các phương trình đại số cơ bản.

-   Tính khả thi về học thuật: Hệ thống phương trình cốt lõi (IS, Phillips, Okun, Debt Dynamics) được xây dựng trên cơ sở lý thuyết kinh tế học New Keynesian. Các tham số nhạy cảm có thể được chuẩn hóa qua các bước calibration dựa trên dữ liệu lịch sử thực tế của Việt Nam và các nền kinh tế mới nổi.
