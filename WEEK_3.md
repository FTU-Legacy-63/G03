# WEEK 3

# **1.** **Input dictionary**

   **1.1.** **Output-Input for next round**

| Input name | Meaning | Type | Unit | Example | Valid range | Source/Owner |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Interbank Rate | Lãi suất vay mượn giữa các NHTM trên thị trường liên ngân hàng | Float | % p.a. | 4.1% | 0% \- 20% | Scenario Designer, Economic Model/ Hiền, Linh |
| Liquidity Gap | Nhu cầu thanh khoản còn lại của hệ thống sau hành động của người chơi | Float | Billion X’currency units | 10,000 | - | Scenario Designer, Economic Model/ Hiền, Linh |

   **1.2.** **User-entered input**

| Input name | Meaning | Type | Unit | Example | Valid range | Source/Owner |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| OMO Auction Method  | Phương thức đấu thầu được sử dụng | Categorial |  | Volume auction  | Interest-rate auction/Volume auction | User  |
| Pricing Method | Phương thức xác định lãi suất trúng thầu | Categorical |  | Single-price | Single-price / Multi-price | User |
| OMO Action | Quyết định của NHTW nhằm bơm hoặc hút thanh khoản | Categorical  |  | Buy Securities  | Reverse Repo/Repo/Buy Securities/Sell Securities  | User |
| Volume | Khối lượng tín phiếu đấu thầu | Numeric  | Billion X’currency units  | 10,000 | ≥ 0  | User |
| Discount rate/Repo rate | Lãi suất áp dụng cho đấu thầu khối lượng | Numeric  | %/year  | 4.0 | 0-10% | User |


**After the player enters all the required inputs, Supply (in Logic Test file) is calculated and used in determining the interbank rate for the next round. Any remaining liquidity gap is carried forward and accumulated into the following round.**


   **1.3.** **Product information** 

| Input name | Meaning | Type | Unit | Example | Valid range | Source/Owner |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Face Value  | Mệnh giá của tín phiếu  | Numerical | X’s  currency units  | 100  | 100bn | Scenario Designer/Hiền |
| Repo’s Maturity  | Kỳ hạn của khoản repo  | Numeric | Days  | 60 | 60 days | Scenario Designer/Hiền |
| SBV bill’s Maturity  | Kỳ hạn của tín phiếu  | Integer  | Days | 90  | 90 days  | Scenario Designer/Hiền |

   **1.4.** **Assumptions / Limitations**  
* Giả định về nền kinh tế:  
  * Nền kinh tế đóng (không mô phỏng trade và international capital flows)
  * MVP giả định các NHTM có phản ứng tương đối giống nhau
  * Thời gian giữa 2 phase tương đương 30 ngày trong thực tế
  * Không tính transaction cost trong MVP
  * OMO tạo tác động trong cùng một Phase (không có delay)

# **2.** **Source register**  

   **2.1.** **Real data**  
[DATABASE 2.0.xlsx](https://docs.google.com/spreadsheets/d/1GDpEZRkXhVWKvsum6EEYFXGNjwku5HiF/edit?gid=520085657#gid=520085657)

   **2.2.** **Sample data**  
* **Đấu thầu lãi suất đơn giá**

Mô phỏng: NHTW muốn phát hành 1.000 tỷ đồng tín phiếu để hút thanh khoản. Các NHTM quyết định lãi suất và khối lượng dự thầu.

Quy tắc: Xếp lãi suất từ thấp → cao, cộng dồn khối lượng đến khi đủ 1.000 tỷ đồng. Tất cả lệnh trúng thầu áp dụng một mức lãi suất chung bằng lãi suất tại lệnh biên.

| STT | NHTM | LS dự thầu | KL đặt thầu (tỷ) | KL cộng dồn (tỷ) | KL trúng (tỷ) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | Bank A | 5,15% | 150 | 150 | 150 |
| 2 | Bank A | 5,20% | 100 | 250 | 100 |
| 3 | Bank B | 5,25% | 100 | 350 | 100 |
| 4 | Bank C | 5,35% | 200 | 550 | 200 |
| 5 | Bank D | 5,35% | 200 | 750 | 200 |
| 6 | Bank D | 5,40% | 200 | 950 | 200 |
| 7 | Bank E | 5,49% | 100 | 1.050 | 50 |
| 8 | Bank B | 5,50% | 100 | 1.150 | 0 |
| 9 | Bank C | 5,60% | 200 | 1.350 | 0 |
| 10 | Bank F | 5,70% | 200 | 1.550 | 0 |

Bước 1 – Xếp lệnh: Xếp lãi suất dự thầu từ thấp đến cao.

Bước 2 – Cộng dồn: Trước mức 5,49%, tổng khối lượng được chấp nhận là 950 tỷ đồng.

Bước 3 – Xác định lệnh biên: NHTW cần thêm 50 tỷ đồng nên nhận 50/100 tỷ của Bank E tại 5,49%.

Bước 4 – Xác định lãi suất: Do đấu thầu đơn giá, toàn bộ 1.000 tỷ đồng trúng thầu đều áp dụng 5,49%/năm.

| Chỉ tiêu | Kết quả |
| :---- | :---- |
| Khối lượng chào thầu | 1.000 tỷ |
| Tổng khối lượng dự thầu | 1.550 tỷ |
| Khối lượng trúng thầu | 1.000 tỷ |
| Lãi suất trúng thầu chung | 5,49%/năm |
| Bid-to-cover | 1,55 lần |
| Lệnh biên | Bank E – 5,49% |
| Phân bổ lệnh biên | 50/100 tỷ |

* **Đấu thầu đa giá** 

Mô phỏng: NHTW muốn phát hành 1.000 tỷ đồng tín phiếu. Các NHTM quyết định lãi suất và khối lượng dự thầu.

Quy tắc: Xếp lãi suất từ thấp → cao, cộng dồn đến khi đủ 1.000 tỷ đồng. Khác với đơn giá, mỗi lệnh trúng thầu áp dụng chính lãi suất mà lệnh đó đã đặt.

| STT | NHTM | LS dự thầu | KL đặt (tỷ) | KL cộng dồn | KL trúng |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | Bank A | 5,15% | 150 | 150 | 150 |
| 2 | Bank A | 5,20% | 100 | 250 | 100 |
| 3 | Bank B | 5,25% | 100 | 350 | 100 |
| 4 | Bank C | 5,35% | 200 | 550 | 200 |
| 5 | Bank D | 5,35% | 200 | 750 | 200 |
| 6 | Bank D | 5,40% | 200 | 950 | 200 |
| 7 | Bank E | 5,49% | 100 | 1.050 | 50 |
| 8 | Bank B | 5,50% | 100 | 1.150 | 0 |
| 9 | Bank C | 5,60% | 200 | 1.350 | 0 |
| 10 | Bank F | 5,70% | 200 | 1.550 | 0 |

Bước 1 – Xếp lệnh: Xếp lãi suất từ thấp đến cao.

Bước 2 – Cộng dồn: Trước mức 5,49%, tổng khối lượng được chấp nhận là 950 tỷ đồng.

Bước 3 – Xác định lệnh biên: Chấp nhận thêm 50/100 tỷ tại mức 5,49% để đủ 1.000 tỷ đồng.

Bước 4 – Xác định lãi suất: Do đấu thầu đa giá, mỗi lệnh trúng áp dụng lãi suất dự thầu của chính lệnh đó, thay vì tất cả cùng hưởng 5,49% như đơn giá.

| Chỉ tiêu | Kết quả |
| :---- | :---- |
| Khối lượng chào thầu | 1.000 tỷ |
| Tổng khối lượng dự thầu | 1.550 tỷ |
| Khối lượng trúng thầu | 1.000 tỷ |
| Khoảng LS trúng thầu | 5,15%–5,49%/năm |
| LS trúng thầu cao nhất | 5,49%/năm |
| LS bình quân gia quyền | ≈ 5,31%/năm |
| Lệnh biên | Bank E – 5,49% |
| Phân bổ lệnh biên | 50/100 tỷ |

* **Đấu thầu khối lượng**   
Mô phỏng: NHTW muốn phát hành 1.000 tỷ đồng tín phiếu, kỳ hạn 28 ngày. NHTW ấn định trước lãi suất 5,50%/năm, các NHTM chỉ quyết định khối lượng dự thầu.

Quy tắc: Nếu tổng khối lượng dự thầu ≤ khối lượng chào thầu thì chấp nhận toàn bộ. Nếu tổng khối lượng dự thầu \> khối lượng chào thầu thì phân bổ theo tỷ lệ.

| NHTM | LS cố định | KL đặt thầu (tỷ) | KL trúng (tỷ) |
| :---- | :---- | :---- | :---- |
| Bank A | 5,50% | 180 | 150,0 |
| Bank B | 5,50% | 250 | 208,3 |
| Bank C | 5,50% | 120 | 100,0 |
| Bank D | 5,50% | 300 | 250,0 |
| Bank E | 5,50% | 200 | 166,7 |
| Bank F | 5,50% | 150 | 125,0 |
| Tổng |   | 1.200 | 1.000 |

Bước 1 – NHTW ấn định lãi suất: Lãi suất áp dụng chung là 5,50%/năm.

Bước 2 – NHTM đặt khối lượng: Tổng nhu cầu \= 1.200 tỷ đồng \> 1.000 tỷ đồng chào thầu.

Bước 3 – Xác định tỷ lệ phân bổ: Tỷ lệ phân bổ \= 1.000 / 1.200 \= 83,33%.

Bước 4 – Phân bổ: Mỗi NHTM được phân bổ khoảng 83,33% khối lượng đã đặt, tổng cộng 1.000 tỷ đồng.

| Chỉ tiêu | Kết quả |
| :---- | :---- |
| Khối lượng chào thầu | 1.000 tỷ |
| Tổng khối lượng dự thầu | 1.200 tỷ |
| Khối lượng trúng thầu | 1.000 tỷ |
| Lãi suất áp dụng chung | 5,50%/năm |
| Tỷ lệ phân bổ | 83,33% |
| Bid-to-cover | 1,20 lần |  

**Ownership và status**   
Source added by Hiền and Trang  
Structure designed by Hiền and Trang  
Data processed by Hiền and Trang

# **3.** **Data flow**  
Scenario (with Liquidity Demand) → Users determines OMO amount (→ Commercial banks submit bids) → System liquidity → Interbank rate  

# **4.** **Logic test**    
| Input | Expected Output | Calculation and Actual Output | Status |
| :---- | :---- | :---- | :---- |
| **TH1: Liquidity Shortage**<br><br>Real Liquidity Demand = 10,000<br><br>Supply = 7,000<br><br>Maturity = -2,000<br><br>Interbank Rate (Previous Phase) = 4% | Unmet Demand (Liquidity Gap) > 0<br><br>Interbank Rate (T) ↑ | **Total Supply Volume = 7,000 - 2,000 = 5,000**<br><br>→ Liquidity Gap = 10,000 - 5,000 = 5,000<br><br>→ Liquidity Pressure = 0.5<br><br>→ Liquidity Adjusted Volume = 5,000 × 0.5 = 2,500<br><br>→ **Interbank Rate (T) = 0.069 × Interbank Rate (T-30) + 0.000123 × Liquidity Adjusted Volume + 3.584 = 4.17** | Pass |
| **TH2: Liquidity Balance**<br><br>Real Liquidity Demand = 10,000<br><br>Supply = 8,000<br><br>Maturity = 2,000<br><br>Interbank Rate (Previous Phase) = 4% | Unmet Demand = 0<br><br>Interbank Rate (T) ↓ | Total Supply Volume = 10,000<br><br>→ Liquidity Gap = 0<br><br>→ Liquidity Pressure = 0<br><br>→ Liquidity Adjusted Volume = 0<br><br>→ **Interbank Rate (T) = 3.86** | Pass |
| **TH3: Excess Liquidity**<br><br>Real Liquidity Demand = 10,000<br><br>Supply = 10,000<br><br>Maturity = 2,000<br><br>Interbank Rate (Previous Phase) = 4% | Unmet Demand < 0<br><br>Interbank Rate (T) ↓ | Total Supply Volume = 12,000<br><br>→ Liquidity Gap = -2,000<br><br>→ Liquidity Pressure = -0.2<br><br>→ Liquidity Adjusted Volume = -2,400<br><br>→ **Interbank Rate (T) = 3.56** | Pass |

[Logic Test.xlsx](https://docs.google.com/spreadsheets/d/1ZoAsCYlYXYfGKCg94ibXo2z694SpF1s7/edit?usp=sharing&ouid=117177009192919491601&rtpof=true&sd=true)  
**Ownership và status**   
Structure designed by Ngọc and Linh  
Validation tested by Ngọc and Linh  
Logic integration by Ngọc and Linh 

