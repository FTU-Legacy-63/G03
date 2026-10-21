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

_Logic: User’s OMO Decision → Commercial Banks Submit Bids → Auction Allocation → Realized Supply / Withdrawal + Maturity → Total Supply Volume → Liquidity Gap → Interbank Rate_

Trong đó, Liquidity Gap đo mức thiếu/thừa thanh khoản; Interbank Rate được ước lượng từ trạng thái thanh khoản bằng mô hình hồi quy.

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
| Liquidity Gap + Interbank Rate (T−30) | Áp lực thanh khoản lên thị trường LNH | Liquidity Gap → Interbank Rate (calculated by regression model) | Interbank Rate (T) |

- Formula and Rules:
  - Xác định Bid Demand của ngân hàng
    - Banks’ Forecasted Liquidity Demand = Scenario liquidity demand + Unmet liquidity demand - Start Maturity Volume − End Maturity Volume (Cách tính toán từng thành phần ở mục 2)
    - Bid Demand = 1.5 × Forecast Liquidity Demand
    - Nghiệp vụ phù hợp với định hướng: 
      Buy / Reverse Repo khi Forecasted Liquidity Demand > 0 
      Sell / Repo khi Forecasted Liquidity Demand < 0 
      Không có nghiệp vụ phù hợp định hướng khi Forecasted LD = 0
  - Xác định Cash Bid và Bid Rate
    _Đấu thầu lãi suất_
      - Trọng số phân bổ Cash Bid giữa các ngân hàng Weight: random [0.01, 1]
      - Total Cash Bid = |Bid Demand| nếu nghiệp vụ phù hợp về định hướng
                                = (Offered Volume × 30-50%) nếu nghiệp vụ không phù hợp về định hướng 
      - Cash Bid each bank = Total Cash Bid × Weight(i) / Σ Weights
      - Win rate = Interbank(prev. phase) + |Z| nếu nghiệp vụ phù hợp về định hướng
                       = Interbank(prev. phase) - |Z| nếu nghiệp vụ không phù hợp về định hướng
      Z ~ Normal(mean 0.6, sd 0.58)
      - Bid rates: Bid rate của ngân hàng ở thứ tự ưu tiên cao nhất = Win rate. 
      + Đối với nghiệp vụ bơm thanh khoản, các mức lãi suất được sắp xếp từ cao xuống thấp.
      + Đối với nghiệp vụ hút thanh khoản, các mức lãi suất được sắp xếp từ thấp lên cao.
      + Bid rate của ngân hàng ở thứ tự ưu tiên tiếp theo = Bid rate của ngân hàng ở thứ tự ưu tiên liền trước - d (Buy / Reverse Repo) hoặc + d (Sell / Repo) 
      d = random [0.01, 0.10]
      - Settlement rate: Single-price: 1 win rate cho tất các các ngân hàng trúng thầu 
                         Multi-price: mỗi ngân hàng trúng thầu ở một mức lãi suất khác nhau
    _Đấu thầu khối lượng_
      - Weight = 5+U, 4+U, 3+U, 2+U, 1+U (U random [0,1) ) 
      - Total Cash Bid = Base × Factor 
      - Base = |Bid Demand| nếu nghiệp vụ phù hợp về định hướng 
                  = Offered Volume nếu nghiệp vụ không phù hợp về định hướng 
      - Factor (Floor = 0.5%, Cap = 5.0%): 
      + OMO Rate < Floor : Factor = 10-30%; nhân thêm 30-50% nếu nghiệp vụ không phù hợp về định hướng 
      + Floor ≤ OMO Rate ≤ Cap: Factor = 90-100% với các nghiệp vụ bơm thanh khoản; Factor = 80-90% với các nghiệp vụ hút thanh khoản
      + OMO Rate > Cap: Factor = 80-90% với các nghiệp vụ bơm thanh khoản; Factor = 90-100% với các nghiệp vụ hút thanh khoản
      - Win rate = OMO rate được người chơi nhập
  - Xác định Bid Volume, Price
    Available Inventory for Real Volume : Outright purchase = Tất cả tín phiếu chưa đáo hạn đang lưu hành
                                          Reverse Repo = TP còn hạn ≥ 60 ngày 
                                          Sell / Repo = Không giới hạn
    - Nghiệp vụ bơm thanh khoản: Hệ thống tham chiếu các tín phiếu chưa đáo hạn theo FIFO (từ lô phát hành cũ nhất đến mới nhất), và sử dụng lãi suất cùng số ngày còn lại của từng lô để xác định giá tham chiếu. 
    Unit Price = 1/ (1 + Bill Rate * Remaining Days / 36500)
    Bid Volume = Cash Bid / Unit Price
    - Nghiệp vụ hút thanh khoản: Bid Volume = Cash Bid × (1 + Settlement rate × 90 / 36500).
    - Tổng khối lượng có thể thực hiện Total Real Volume = min(Offered Volume, Total Bid Volume, Available Inventory)
    - Awarded Volume của từng ngân hàng
    + Đấu thầu lãi suất: phân bổ theo thứ tự ưu tiên cho đến khi hết Total Real Volume.
    + Đấu thầu khối lượng: phân bổ theo tỷ lệ với Bid Volume của từng ngân hàng.
    - Price: số tiền mặt thực tế NHNN trả (bơm) hoặc thu (hút) cho khối lượng trúng thầu. Tổng Price của 5 ngân hàng (mang dấu + với nghiệp vụ bơm và dấu - với nghiệp vụ hút) chính là Supply. 
    + Buy Securities: Tổng giá (Unit Price) của các phần tín phiếu được mua, theo FIFO.
    + Reverse Repo: tính tương tự, nhưng chỉ lấy các tín phiếu còn ít nhất 60 ngày đến khi đáo hạn.
    + Sell Securities và Repo: Real Volume / (1 + Settlement rate × 90 / 36500).
    Với Sell Securities: đồng thời bổ sung vào thị trường một lô tín phiếu mới kỳ hạn 90 ngày, với lãi suất bằng Settlement rate.
  - Khoản đáo hạn
    - Maturity Volume = Σ dòng tiền của các khoản có ngày đáo hạn ≤ ngày kết thúc phase (> 0: bơm thanh khoản, < 0: hút thanh khoản)
    - Tín phiếu NHNN (90 ngày) : Maturity Volume = Face value
    - Repo (60 ngày): Maturity Volume = Price × (1 + Lãi suất giao dịch × 60 / 36500)
    - Reverse Repo (60 ngày): - Price × (1 + Lãi suất giao dịch × 60 / 36500)
    Nếu tín phiếu cơ sở đáo hạn trước khi hợp đồng Reverse Repo kết thúc. Khi tín phiếu đó đáo hạn, mệnh giá được ghi nhận thành dòng tiền dương; phần tín phiếu đã đáo hạn được đánh dấu để không tính lại khi hợp đồng Reverse Repo kết thúc. 
  - Xác định trạng thái thanh khoản thực tế
    - Unmet Liquidity Demand = Liquidity Gap (prev. phase)
    - Scenario Liquidity Demand (quyết định bởi scenario designer)
    - Real Liquidity Demand = Scenario LD + Unmet LD
    - Supply = Tổng Price mà 5 ngân hàng trả / nhận để NHNN thực hiện nghiệp vụ
    - Total supply = Supply + Maturity Volume 
    - Liquidity Gap = Real Liquidity Demand - Total Supply (Gap > 0: thiếu thanh khoản, gap < 0: dư thanh khoản)
  - Lãi suất liên ngân hàng
    - Theoretical Interbank Rate: 0.069 × Interbank(prev. phase) + 0.000123 × Liquidity Gap + 3.584
    - Interbank Rate = MIN( 20, MAX(0, Theoretical Interbank Rate) )
  - Công thức vĩ mô
    - User input: Lạm phát kì vọng tại thời điểm cuối 3 phase tiếp theo (%)
    - Lãi suất thực kì vọng (Không hiển thị cho người chơi) = Lãi suất LNH - Lạm phát kì vọng
    - Khoảng bù sản lượng Output Gap (Ko hiển thị) = η * Output Gap kì trước − σ(Lãi suất thực kì vọng - Lãi suất thực trung tính)
    + Output gap đầu phase 1: 0
    + Hệ số trì trệ của Output Gap (η): 0.6 
    + Độ nhạy của Output Gap theo khe hở lãi suất thực (σ) = 0.25
    + LSTTT: 2.0%/năm.
    - Tăng trưởng GDP GDP Growth (%) = Tăng trưởng GDP tiềm năng + (Output Gap kì hiện tại - Output Gap kì trước)
     Tăng trưởng GDP tiềm năng = 6%
    - Tỉ lệ lạm phát Inflation Rate = β.Lạm phát kì vọng + (1 - β - κ). Lạm phát kì trước + κ.(GDP Growth - Potential GDP Growth)
    + β = 0.25
    + Độ nhạy của Lạm phát theo chênh lệch Tăng trưởng GDP so với Tăng trưởng GDP tiềm năng (κ): 0.1
  
- Classification:
  - Supply: Lượng tiền bơm/hút thực tế
    - Supply > 0: NHNN bơm thanh khoản vào hệ thống.
    - Supply < 0: NHNN hút thanh khoản khỏi hệ thống.
  - Maturity Volume:
    - Maturity Volume > 0: KL đáo hạn làm tăng thanh khoản trong hệ thống
    - Maturity Volume = 0: Không có khối lượng giao dịch đáo hạn.
    - Maturity Volume < 0: KL đáo hạn làm giảm thanh khoản trong hệ thống.
  - Real Liquidity Demand/Gap/Pressure:
    - Real Liquidity Demand/Gap/Pressure > 0: Thiếu thanh khoản.
    - Real Liquidity Demand/Gap/Pressure = 0: Cân bằng thanh khoản.
    - Real Liquidity Demand/Gap/Pressure < 0: Thừa thanh khoản.

**Explainability:**

_Liquidity Gap (không hiển thị cho người chơi)_

Ví dụ: Liquidity Gap sau OMO = +600 tỷ đồng.

- **Kết quả:** Hệ thống còn thiếu 600 tỷ đồng thanh khoản.
- **Vì sao:** Khối lượng thanh khoản được phân bổ qua phiên OMO chưa đủ để bù đắp toàn bộ mức thiếu thanh khoản của hệ thống.
- **Input ảnh hưởng:** Real Liquidity Demand trước OMO, khối lượng trúng thầu và khối lượng đáo hạn.
- **Assumption:** Liquidity Gap > 0 - thiếu thanh khoản; Liquidity Gap < 0 - dư thanh khoản.
- **Cách hiểu output:** Sau can thiệp, hệ thống vẫn cần bổ sung 600 tỷ đồng để trở về trạng thái cân bằng thanh khoản.
- **Output không khẳng định:** Kết quả phản ánh trạng thái thanh khoản tổng hợp của hệ thống, không có nghĩa tất cả NHTM đều thiếu 600 tỷ đồng thanh khoản.


_Interbank Rate_

Ví dụ: Interbank Rate giảm từ 4,30% xuống 4,10%.

- **Kết quả:** Lãi suất liên ngân hàng sau OMO được ước tính ở mức 4,10%.
- **Vì sao:** OMO làm giảm mức thiếu thanh khoản của hệ thống, từ đó giảm áp lực vay vốn trên thị trường liên ngân hàng.
- **Input ảnh hưởng:** Liquidity Demand sau OMO và Interbank Rate của kỳ trước.
- **Assumption:** Interbank Rate được ước tính bằng mô hình hồi quy dựa trên điều kiện thanh khoản mô phỏng và dữ liệu lãi suất kỳ trước.
- **Cách hiểu output:** Mức giảm từ 4,30% xuống 4,10% thể hiện áp lực thanh khoản trên thị trường liên ngân hàng đã giảm trong mô phỏng.
- **Output không khẳng định:** 4,10% không phải dự báo lãi suất liên ngân hàng thực tế và không khẳng định OMO là yếu tố duy nhất quyết định lãi suất.


_Auction Result_

Ví dụ: NHNN chào bơm 1.000 tỷ đồng và 900 tỷ đồng được phân bổ cho các NHTM trúng thầu.

- **Kết quả:** Tổng khối lượng tiền thực tế được phân bổ là 900 tỷ đồng.
- **Vì sao:** Kết quả được xác định từ Bid Rate, Bid Volume của các NHTM và rule của cơ chế đấu thầu được lựa chọn.
- **Input ảnh hưởng:** Khối lượng OMO chào thầu, Bid Rate, Bid Volume, Auction Method và Pricing Method.
- **Assumption:** Bid của các NHTM được mô phỏng theo rule và phân phối dữ liệu được nhóm xác định.
- **Cách hiểu output:** 900 tỷ đồng là khối lượng thực tế đi qua cơ chế đấu thầu và được sử dụng để cập nhật thanh khoản sau OMO.

**7. Sample Calculation và Logic Test**

| Input | Expected output | Sample Calculation and Actual Output | Status |
| --- | --- | --- | --- |
| **TH1: Liquidity shortage**<br>Real Liquidity Demand = 10,000 <br>Volume = 7,000 <br>Maturity = -2,000<br>Interbank Rate (T-30) = 4% | Unmet Demand (Liquidity Gap) > 0 <br>Interbank Rate (T) ↑<br> | VD: Đấu thầu lãi suất - Mua tín phiếu: <br>NHTM tham gia đấu thầu<br>→ Sắp xếp các NHTM theo thứ tự bid rate phù hợp với OMO Action (giảm dần)<br>→ Phân bổ khối lượng đến khi đạt khối lượng trúng thầu = 7,000<br>→ **Auction Result: Supply = 6,953**<br><br>Total Supply Volume = 6,953 - 2000 = 4,953<br>→ Liquidity Gap = 10,000 - 4,953 = 5,047 <br>→ **Interbank Rate (T) = 0.069*Interbank Rate (T-30)+0.000123*Liquidity Gap+3.584 = 4.48** | Pass |
| **TH2 - Liquidity Balance**<br>Real Liquidity Demand = 10,000<br>Volume = 8,000<br>Maturity = 2,000<br>Interbank Rate (T-30) = 4% | Unmet Demand ~ 0 (nhỏ)<br>Interbank Rate (T) ↓ | VD: Đấu thầu lãi suất - Mua tín phiếu: <br>NHTM tham gia đấu thầu<br>→ Sắp xếp các NHTM theo thứ tự bid rate phù hợp với OMO Action (giảm dần)<br>→ Phân bổ khối lượng đến khi đạt khối lượng trúng thầu = 8,000<br>→ **Auction Result: Supply = 7936**<br><br>Total Supply Volume = 9936<br>→ Liquidity Gap = 64<br>→ **Interbank Rate (T) = 3.87** | Pass |
| **TH3 - Excess Liquidity**<br>Real Liquidity Demand = 10,000<br>Volume = 10,000<br>Maturity = 2,000<br>Interbank Rate (T-30) = 4% | Unmet Demand < 0<br>Interbank Rate (T) ↓<br> | VD: Đấu thầu Khối lượng - Mua tín phiếu:<br>NHTM tham gia đấu thầu<br>→ Sắp xếp các NHTM theo thứ tự KL dự thầu phù hợp với OMO Action (giảm dần)<br>→ Phân bổ khối lượng đến khi đạt khối lượng trúng thầu = 10,000<br>→ **Auction Result: Supply = 9926**<br><br>Total Supply Volume = 11926<br>→ Liquidity Gap = -1926<br>→ **Interbank Rate (T) = 3.62** | Pass |

[Logic Test.xlsx](https://docs.google.com/spreadsheets/d/1h-B_Q1Yzh-WT_OCM6hdJqnkMXHDwMgyo/edit?gid=1908828182#gid=1908828182)  


**8. Technical Readiness**
- Coding environment: VS Code
- Framework: HTML, CSS, JavaScript
- Data storage: CSV/JSON
- Deployment: Render
- AI-assisted coding: ChatGPT
- Fallback: Excel prototype nếu web chưa hoàn thiện

**→ Đánh giá: Công cụ miễn phí, dễ triển khai và phù hợp với prototype; hạn chế là mô hình chủ yếu chạy phía client và dữ liệu được lưu tĩnh**


**9. Midterm Assessment**

_Midterm Checklist_

| Assessment area | Evidence | Status |
| --- | --- | --- |
| Project Direction | README, Project Proposal, Solution Structure | Ready |
| Input & Evidence Readiness | Week 3 (Source & Database) | Ready |
| Financial Logic | Week 4 (Formula, Rules, Regression & Logic Test) | Ready |
| Product Structure & Progress | Week 3 (Technical Readiness), Week 4 (Logic Test), Week 5 (User Flow) | Ready |
| Group Footprint | README, weekly updates | Ready |
| Individual Contribution | Evidence at the of each weekly submission | Ready |

_Individual Contribution_

| Member | Contribution up to Midterm | Most Important Output | Next Responsibility |
| --- | --- | --- | --- |
| Nguyễn Bảo Hiền - Game Logic & Scenario Designer | Source research, data collection, data cleaning and explanation development | Source & Database | Complete scenarios and connect them to the game logic |
| Nguyễn Minh Trang - UI/UX & Learning Experience | Source research, data collection, data cleaning and Working interface demo | Regression Dataset & Database | Develop UI/UX and frontend |
| Vũ Lưu Minh Ngọc - Game Engine & Backend Developer | Group coordination, data/formula verification, formula revision and regression | Regression & Logic Test | Develop backend/game engine and integrate the financial logic |
| Nguyễn Khánh Linh - Economic Model | Formula research, model structuring, regression and economic-model development | Regression & Logic Test | Complete and refine the Economic Engine |
