# WEEK 4

**1. Project logic chain**

**Problem:**

Sinh viên hiểu cơ chế OMO nhưng gặp khó khăn khi áp dụng đưa ra quyết định can thiệp phù hợp vào tình huống thực tế và đánh giá tác động của quyết định đó.

**Target user:**

Sinh viên/HSSV quan tâm đến lĩnh vực Ngân hàng Nhà nước, quản trị ngân hàng và chính sách tiền tệ nhưng chưa có kiến thức chuyên sâu.

**User task:**

- Đọc các chỉ số thị trường tiền tệ (Nhu cầu thanh khoản hệ thống ngân hàng, Lãi suất liên ngân hàng).

- Đưa ra quyết định OMO: Người chơi đưa ra quyết định can thiệp lượng tiền thông qua OMO:

- Mua/Bán có kỳ hạn: Quyết định mua/bán tín phiếu NHNN từ các NHTM để bơm thêm lượng dự trữ khả dụng/Hút tiền từ hệ thống. Người chơi chọn đấu thầu lãi suất đơn giá/đa giá hoặc đấu thầu khối lượng và kỳ hạn.

- Phát hành/Mua lại Tín phiếu NHTW: Mua/Bán tín phiếu ngắn hạn để bơm/thu hồi tiền mặt khả dụng từ hệ thống NHTM. Người chơi chọn đấu thầu lãi suất đơn giá/đa giá hoặc đấu thầu khối lượng.

**Difficulty:**

- Khó xác định công thức/mô hình ước tính lãi suất trúng thầu và khối lượng đặt thầu phù hợp với dữ liệu thị trường.

- Không có dữ liệu công khai về lãi suất dự thầu và khối lượng đặt thầu của từng NHTM, nhóm xây dựng phương pháp ước tính và mô phỏng dữ liệu dự thầu để vận hành cơ chế đấu thầu trong game.

**Technology support:**

- Sử dụng mô hình hồi quy và các phương pháp thống kê để xác định mối quan hệ giữa Lãi suất liên ngân hàng qua đêm giữa 2 phase liên tiếp và ước tính lãi suất trúng thầu, khối lượng đặt thầu kết hợp dữ liệu thực từ báo cáo nghiệp vụ thị trường mở theo ngày để đối chiếu diễn biến và tác động.

- Với lãi suất dự thầu, tham khảo khoảng lãi suất dự thầu từ dữ liệu đấu thầu của NHNN, sau đó ngẫu nhiên trong khoảng phù hợp để tạo dữ liệu mô phỏng cho các NHTM.

**Input:**

_Input for next round_

| Output name | Meaning | Type | Unit | Example | Valid range |
| --- | --- | --- | --- | --- | --- |
| **Interbank Rate** | Lãi suất vay mượn giữa các NHTM trên thị trường liên ngân hàng | Float | % | 4.1% | 0% - 20% |
| **Liquidity Gap** | Nhu cầu thanh khoản còn lại của hệ thống sau hành động của người chơi | Float | Billion X’currency units | 10,000 | - |


_User-entered input_

| Input name | Meaning | Type | Unit | Example | Valid range |
| --- | --- | --- | --- | --- | --- |
| **OMO Auction Method** | Phương thức đấu thầu được sử dụng | Categorial |  | Volume auction | Interest-rate auction/Volume auction |
| **Pricing Method** | Phương thức xác định lãi suất trúng thầu | Categorical |  | Single-price | Single-price / Multi-price<br> |
| **OMO Action** | Quyết định của NHTW nhằm bơm hoặc hút thanh khoản | Categorical |  | Buy Securities | Reverse Repo/Repo/Buy Securities/Sell Securities |
| **Volume** | Khối lượng tín phiếu đấu thầu | Numeric | Billion X’currency units | 10,000 | ≥ 0 (Giới hạn bởi lượng tín phiếu còn tồn tại) |
| **Reverse repo/Repo rate** | Lãi suất áp dụng cho đấu thầu khối lượng | Numeric | %/year | 4.0 | 0-10% |

_Product information_

| Input name | Meaning | Type | Unit | Example | Valid range |
| --- | --- | --- | --- | --- | --- |
| **Face Value** | Mệnh giá của tín phiếu | Numerical | X’s currency units | 100 | 100bn |
| **Repo’s Maturity** | Kỳ hạn của khoản repo | Numeric | Days | 60 | 60 days |
| **SBV bill’s Maturity** | Kỳ hạn của tín phiếu | Integer | Days | 90 | 90 days |


**2. Financial logic and input–financial / logic–output mapping**

**Financial logic**

Quyết định bơm/hút tiền qua OMO làm thay đổi thanh khoản hệ thống, từ đó tác động đến lãi suất liên ngân hàng.

_Logic: User’s OMO Decision → Commercial Banks Submit Bids → Auction Allocation → Realized Supply / Withdrawal + Maturity → Total Supply Volume → Liquidity Gap → Liquidity Pressure → Liquidity adjusted volume (Total Supply Volume adjusted by Liquidity pressure) → Interbank Rate_

Trong đó, Liquidity Gap đo mức thiếu/thừa thanh khoản; Liquidity Pressure phản ánh mức độ mất cân đối; Interbank Rate được ước lượng từ trạng thái thanh khoản bằng mô hình hồi quy.

**Main output:**

- Liquidity Gap: Nhu cầu thanh khoản của hệ thống chưa được đáp ứng từ phase trước.

- Lãi suất liên ngân hàng ước tính sau can thiệp.

**User action:**

- Đánh giá kết quả với số liệu trước vòng chơi và giải thích được đưa ra.

- Điều chỉnh quyết định OMO cho lượt tiếp theo.

**Mapping**

| Input | Financial meaning | Process | Output |
| --- | --- | --- | --- |
| Auction Method + Pricing Method + OMO Action + Rate/Volume | Cơ chế phân bổ OMO | OMO Action + Pricing Method + Auction Method + Rate + Volume → Commercial Banks Submit Bids → Auction Allocation → Khối lượng/lãi suất trúng thầu theo phương thức đấu thầu → Supply | Auction result và Supply |
| Scenario + Previous Phase Result | Nhu cầu thanh khoản thực tế của hệ thống | Market Conditions + Unmet Liquidity Demand → Real Liquidity Demand | Real Liquidity Demand |
| Supply + Maturity + Real Liquidity Demand | Trạng thái cung-cầu thanh khoản | Supply + Maturity + Real Liquidity Demand → Total Supply Volume → Liquidity Gap | Liquidity Gap |
| Liquidity Gap + Interbank Rate (T−30) | Áp lực thanh khoản lên thị trường LNH | Liquidity Gap → Liquidity pressure → Liquidity adjusted volume → Interbank Rate (calculated by regression model) | Interbank Rate (T) |


**Rule for Auction Result**

_Interest-rate auction_
  - Tạo Bid Rate:
      - Win rate = Interbank (T-30) ± Random Spread (dựa theo normal distribution từ dữ liệu thực tế)
      - Bid Rate = Win rate ± Random Spread (tham khảo theo khoảng giá trị từ dữ liệu đấu thầu tín phiếu kho bạc thực tế)
  - Tạo Bid Volume: Bid Volumeᵢ = Weightᵢ / Tổng Weight × Total Bid Volume (trong đó Weight được random trong khoảng 0 đến 1)
  - Xếp các Bid rate và Bid volume theo thứ tự phù hợp với hướng OMO.
  - Phân bổ khối lượng đặt thầu và trúng thầu phù hợp với cách thức đấu thầu và các tình huống kinh tế
  - Single-price: các bid trúng được áp dụng cùng mức lãi suất trúng thầu.
  - Multi-price: mỗi bid trúng được áp dụng chính mức lãi suất mà ngân hàng đã bid.
    
_Volume auction_
  - Tạo Bid Volume: Bid Volumeᵢ = Weightᵢ / Tổng Weight × Total Bid Volume (trong đó Weight được random trong khoảng 0 đến 1 và thêm hệ số từ cao đến thấp)
  - Phân bổ khối lượng đặt thầu và trúng thầu phù hợp với cách thức đấu thầu và các tình huống kinh tế

_Formula_
  - Total Supply Volume = Supply + Maturity
  - Liquidity Gap = Real Liquidity Demand − Total Supply Volume
  - Liquidity Pressure = Liquidity Gap / |Real Liquidity Demand|
  - Interbank Rate (T) = β₀ + β₁ Interbank Rate (T−30) + β₂ Liquidity Adjusted Volume (β₀, β₁, β₂ lấy từ kết quả regression của nhóm kèm sự điều chỉnh cho phù hợp)

_Classification:_
- Supply: Lượng tiền bơm/hút thực tế
  Supply > 0: NHNN bơm thanh khoản vào hệ thống.
  Supply < 0: NHNN hút thanh khoản khỏi hệ thống.
- Maturity:
  Maturity > 0 khi có tín phiếu, repo đáo hạn
  Maturity = 0 khi không có tín phiếu, repo, reverse repo đáo hạn
  Maturity < 0 khi reverse repo đáo hạn
- Real Liquidity Demand/Gap/Pressure:
  Real Liquidity Demand/Gap/Pressure > 0: Thiếu thanh khoản.
  Real Liquidity Demand/Gap/Pressure = 0: Cân bằng thanh khoản.
  Real Liquidity Demand/Gap/Pressure < 0: Thừa thanh khoản.

_Explainability_
- Liquidity Demand > 0: Hệ thống có nhu cầu bổ sung thanh khoản.
- Liquidity Demand < 0: Hệ thống có dư thừa thanh khoản
**→ Khi Liquidity Demand tăng, áp lực lên nguồn vốn trên thị trường liên ngân hàng có xu hướng tăng, từ đó tạo áp lực tăng lên Interbank Rate. Ngược lại, nhu cầu thanh khoản giảm làm giảm áp lực lên nguồn vốn và có xu hướng kéo lãi suất xuống.**



**7. Sample Calculation và Logic Test**

| Input | Expected output | Sample Calculation and Actual Output | Status |
| --- | --- | --- | --- |
| **TH1: Liquidity shortage**<br>Real Liquidity Demand = 10,000 <br>Volume = 7,000 <br>Maturity = -2,000<br>Interbank Rate (previous phase) = 4% | Unmet Demand (Liquidity Gap) > 0 <br>Interbank Rate (T) ↑<br> | VD: Đấu thầu lãi suất - Mua tín phiếu: <br>NHTM tham gia đấu thầu<br>→ Sắp xếp các NHTM theo thứ tự bid rate phù hợp với OMO Action (giảm dần)<br>→ Phân bổ khối lượng đến khi đạt khối lượng trúng thầu = 7,000<br>→ **Auction Result: Supply = 6,953**<br><br>Total Supply Volume = 6,953 - 2000 = 4,953<br>→ Liquidity Gap = 10,000 - 4,953 = 5,047 <br>→ Liquidity Pressure = 0.5047 <br>→ Liquidity Adjusted Volume = 5,047 * 0.5047 = 2,499.78<br>→ **Interbank Rate (T) = 0.069*Interbank Rate (T-30)+0.000123*Liquidity Adjusted Volume+3.584 = 4.17** | Pass |
| **TH2 - Liquidity Balance**<br>Real Liquidity Demand = 10,000<br>Volume = 8,000<br>Maturity = 2,000<br>Interbank Rate (previous phase) = 4% | Unmet Demand ~ 0 (nhỏ)<br>Interbank Rate (T) ↓ | VD: Đấu thầu lãi suất - Mua tín phiếu: <br>NHTM tham gia đấu thầu<br>→ Sắp xếp các NHTM theo thứ tự bid rate phù hợp với OMO Action (giảm dần)<br>→ Phân bổ khối lượng đến khi đạt khối lượng trúng thầu = 8,000<br>→ **Auction Result: Supply = 7936**<br><br>Total Supply Volume = 9936<br>→ Liquidity Gap = 64<br>→ Liquidity Pressure = 0,006<br>→ Liquidity Adjusted Volume = 63<br>→ **Interbank Rate (T) = 3.87** | Pass |
| **TH3 - Excess Liquidity**<br>Real Liquidity Demand = 10,000<br>Volume = 10,000<br>Maturity = 2,000<br>Interbank Rate (previous phase) = 4% | Unmet Demand < 0<br>Interbank Rate (T) ↓<br> | VD: Đấu thầu Khối lượng - Mua tín phiếu:<br>NHTM tham gia đấu thầu<br>→ Sắp xếp các NHTM theo thứ tự KL dự thầu phù hợp với OMO Action (giảm dần)<br>→ Phân bổ khối lượng đến khi đạt khối lượng trúng thầu = 10,000<br>→ **Auction Result: Supply = 9926**<br><br>Total Supply Volume = 11926<br>→ Liquidity Gap = -1926<br>→ Liquidity Pressure = -0.193<br>→ Liquidity Adjusted Volume = -2297<br>→ **Interbank Rate (T) = 3.58** | Pass |

[Logic Test.xlsx](https://docs.google.com/spreadsheets/d/1h-B_Q1Yzh-WT_OCM6hdJqnkMXHDwMgyo/edit?gid=1908828182#gid=1908828182)  


**8. Technical Readiness**
- Coding environment: VS Code
- Framework: HTML, CSS, JavaScript
- Data storage: CSV/JSON
- Deployment: GitHub Pages
- AI-assisted coding: ChatGPT/Gemini
- Fallback: Excel prototype nếu web chưa hoàn thiện

**→ Đánh giá: Công cụ miễn phí, dễ triển khai và phù hợp với prototype; hạn chế là mô hình chủ yếu chạy phía client và dữ liệu được lưu tĩnh**


**9. Midterm Assessment**

_Midterm Checklist_

| Assessment area | Evidence | Status |
| --- | --- | --- |
| Project Direction | README & Product Direction | Ready |
| Input & Evidence Readiness | Input Mapping, Source & Database | Ready |
| Financial Logic | Formula, Rules, Regression & Logic Test | Ready |
| Product Structure & Progress | Product Flow, Logic Test & Technical Readiness | Ready |
| Group Footprint | README, weekly documentation | Ready |
| Individual Contribution | Contribution evidence by member | Ready |

_Individual Contribution_

| Member | Contribution up to Midterm | Most Important Output | Next Responsibility |
| --- | --- | --- | --- |
| Nguyễn Bảo Hiền - Game Logic & Scenario Designer | Source research, data collection, variable selection and scenario development | Source & Database | Complete scenarios and connect them to the game logic |
| Nguyễn Minh Trang - UI/UX & Learning Experience | Source research, data collection, data cleaning and regression-data preparation | Regression Dataset & Database | Develop UI/UX and frontend |
| Vũ Lưu Minh Ngọc - Game Engine & Backend Developer | Group coordination, data/formula verification, formula revision and regression | Regression & Logic Test | Develop backend/game engine and integrate the financial logic |
| Nguyễn Khánh Linh - Economic Model | Formula research, model structuring, regression and economic-model development | Regression & Logic Test | Complete and refine the Economic Engine |

