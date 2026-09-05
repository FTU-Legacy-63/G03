1. # **Input dictionary**

   1.1. # **Financial overview information**

| Input name | Meaning | Type | Unit | Example | Valid range | Source/Owner |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| ideposit | Lãi suất tiền gửi không kì hạn (1 tháng) | Float | % | 2.1% | 0% \- 15% | Scenario Designer, Economic Model/ Hiền, Linh |
| ilending | Lãi suất cho vay bình quân | Float | % | 5.5% | 0% \- 20% | Scenario Designer, Economic Model/ Hiền, Linh |
| Liquidity Demand | Nhu cầu thanh khoản của toàn hệ thống | Float | Billion X’currency units | 10,000 | \- | Scenario Designer, Economic Model/ Hiền, Linh |
| Interbank Rate | Lãi suất vay mượn giữa các NHTM trên thị trường liên ngân hàng | Float | % p.a. | 4.1% | 0% \- 20% | Scenario Designer, Economic Model/ Hiền, Linh |
| Inflation | Lạm phát trong nền kinh tế so với phase trước | Float | %  | 4.2%  | \-5% \- 30% | Scenario Designer, Economic Model/ Hiền, Linh |
| Real GDP Growth | Tốc độ tăng trưởng GDP thực | Float | %  | 6.8%  | \-15% \- 15% | Scenario Designer, Economic Model/ Hiền, Linh |
| Unemployment Rate | Tỷ lệ thất nghiệp | Float | %  | 3.8%  | 0% \- 30% | Scenario Designer, Economic Model/ Hiền, Linh |
| Nominal Interest rate | Lãi suất danh nghĩa của nền kinh tế | Float | % | 0.0% | \-15% \- 20% | Scenario Designer, Economic Model/ Hiền, Linh |
| News / Event | Tin tức về các diễn biến nền kinh tế | String | \- | “Inflation rises above target...” | N/A | Scenario Designer, Economic Model/ Hiền, Linh |

   1.2. # **User-entered input**

| Input name | Meaning | Type | Unit | Example | Valid range | Source/Owner |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| OMO Auction Method  | Phương thức đấu thầu được sử dụng | Categorial |  | Volume auction  | Multiple Interest-rate auction/ Single Interest-rate Auction/Volume auction | User  |
| OMO Action | Quyết định của NHTW nhằm bơm hoặc hút thanh khoản | Categorical  |  | Buy Securities  | Reverse Repo/Repo/Buy Securities/Sell Securities  | User |
| Volume | Khối lượng tiền tín phiếu quyết định đấu thầu | Numeric  | Billion X’currency units  | 10,000 | ≥ 0  | User |
| Discount rate/Repo rate | Lãi suất áp dụng cho đấu thầu khối lượng | Numeric  | %/year  | 4.0 | 0-10% | User |
| Expected inflation | Lạm phát dự báo sau 1 tháng (5 phase) | Numeric  | % | 3 | 0-5% | User |

   1.3. # **Product information** 

| Input name | Meaning | Type | Unit | Example | Valid range | Source/Owner |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Face Value  | Mệnh giá của tín phiếu  | Numerical | X’s  currency units  | 100  | 100bn | Scenario Designer/Hiền |
| Repo’s Maturity  | Kỳ hạn của khoản repo  | Numeric | Days  | 14 | 14 days | Scenario Designer/Hiền |
| Treasury bill’s Maturity  | Kỳ hạn của tín phiếu  | Integer  | Days | 28   | 28 days  | Scenario Designer/Hiền |

   1.4. # **Assumptions / Limitations**  
* Giả định về nền kinh tế:  
  * Nền kinh tế đóng (không mô phỏng trade và international capital flows)  
  * MVP giả định các NHTM có phản ứng tương đối giống nhau  
  * GDP potential growth được giữ cố định trong mỗi Phase  
  * Inflation trong Economic Engine được coi là GDP-deflator inflation  
  * Thời gian giữa 2 phase tương đương 7 ngày trong thực tế  
* Không tính transaction cost trong MVP  
* OMO tạo tác động trong cùng một Phase (không có delay)  
* Hệ thống chỉ áp dụng phương thức xét thầu đơn giá  
* Kỳ hạn ảnh hưởng đến Liquidity gap theo tỉ lệ thuận  
* OMO Rate ≤ Expected Interbank Rate​ 

2. # **Source register**  
   2.1. # **Real data**  
[DATABASE 2.0.xlsx](https://docs.google.com/spreadsheets/d/1GDpEZRkXhVWKvsum6EEYFXGNjwku5HiF/edit?gid=520085657#gid=520085657)

   2.2. # **Sample data**  
* **Đấu thầu lãi suất đơn giá** 

Mô phỏng: NHTW muốn bán/phát hành 1.000 tỷ đồng tín phiếu để hút thanh khoản. Các NHTM gửi cả lãi suất và khối lượng dự thầu.  
**Quy tắc mô phỏng:** vì NHTW là bên phát hành/bán tín phiếu, các mức lãi suất dự thầu thấp hơn được ưu tiên trước. Các lệnh được cộng dồn cho đến khi đạt khối lượng 1.000 tỷ đồng.

| STT | NHTM | LS dự thầu | KL đặt thầu (tỷ) | KL cộng dồn (tỷ) | KL trúng (tỷ) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | Bank A | 5,15% | 150 | 150 | 150 |
| 2 | Bank A | 5,20% | 100 | 250 | 100 |
| 3 | Bank B | 5,25% | 100 | 350 | 100 |
| 4 | Bank C | 5,35% | 200 | 550 | 200 |
| 5 | Bank D | 5,35% | 200 | 750 | 200 |
| 6 | Bank D | 5,40% | 200 | 950 | 200 |
| **7** | **Bank E** | **5,49%** | **100** | **1.050** | **50** |
| 8 | Bank B | 5,50% | 100 | 1.150 | 0 |
| 9 | Bank C | 5,60% | 200 | 1.350 | 0 |
| 10 | Bank F | 5,70% | 200 | 1.550 | 0 |

**Bước 1 \- Xếp lệnh:** xếp lãi suất dự thầu từ thấp lên cao.

**Bước 2 \- Cộng dồn khối lượng:** tại các mức lãi suất thấp hơn 5,49%, tổng khối lượng cộng dồn là 950 tỷ đồng.

**Bước 3 \- Xác định mức cắt:** NHTW còn cần 50 tỷ đồng để đủ 1.000 tỷ, nên chỉ chấp nhận 50/100 tỷ tại mức 5,49%.

*Lãi suất trúng thầu (cut-off) \= 5,49%/năm*

*Tổng khối lượng trúng thầu \= 1.000 tỷ đồng*

**Bước 4 \- Đấu thầu đơn giá:** toàn bộ các lệnh trúng thầu được áp dụng cùng một mức lãi suất là 5,49%/năm.

| Chỉ tiêu | Kết quả |
| :---- | :---- |
| Khối lượng chào thầu | 1.000 tỷ đồng |
| Tổng khối lượng dự thầu | 1.550 tỷ đồng |
| Lãi suất trúng thầu chung | 5,49%/năm |
| Khối lượng trúng thầu | 1.000 tỷ đồng |
| Bid-to-cover | 1,55 lần |
| Lệnh biên | Bank E – 5,49% |
| Phân bổ lệnh biên | 50/100 tỷ |

* **Đấu thầu khối lượng**   
  - Khối lượng chào thầu: 1.000 tỷ đồng.  
  - Kỳ hạn: 28 ngày.  
  - Phương thức: đấu thầu khối lượng.  
  - Lãi suất do người chơi/NHNN ấn định: 5,50%/năm.  
  - Mỗi NHTM chỉ quyết định khối lượng muốn đặt thầu

| NHTM | Lãi suất áp dụng | Khối lượng đặt thầu (tỷ đồng) | Khối lượng trúng thầu (tỷ đồng) |
| :---- | :---- | :---- | :---- |
| A | 5,50% | 180 | **150.0** |
| B | 5,50% | 250 | **208.3** |
| C | 5,50% | 120 | **100.0** |
| D | 5,50% | 300 | **250.0** |
| E | 5,50% | 200 | **166.7** |
| F | 5,50% | 150 | **125.0** |

Tổng khối lượng đặt thầu \= 1.200 tỷ đồng; khối lượng chào thầu \= 1.000 tỷ đồng. Vì tổng cầu lớn hơn lượng chào, áp dụng phân bổ theo tỷ lệ. Mỗi NHTM có một nhu cầu giao dịch khác nhau. Khi NHNN công bố mức lãi suất cố định, khối lượng đặt thầu của từng NHTM dựa trên nhu cầu và mức hấp dẫn của lãi suất so với điều kiện thị trường. Bộ số liệu ban đầu được thiết kế để tạo được cả tình huống dư cầu và thiếu cầu.

- Lãi suất cố định \> 0\.  
- Khối lượng đặt thầu của từng NHTM ≥ 0\.  
- Khối lượng trúng của từng NHTM không vượt khối lượng đặt.  
- Tổng khối lượng trúng không vượt Q\_offer.  
- Nếu tổng cầu nhỏ hơn Q\_offer thì Q\_actual phải bằng tổng cầu.  
- Nếu tổng cầu lớn hơn Q\_offer thì tổng phân bổ phải bằng Q\_offer.  
* **Đấu thầu đa giá** 

– Khối lượng gọi thầu: 1.000 tỷ đồng.

– Phương thức: đấu thầu lãi suất đa giá.

– Mỗi NHTM/nhà đầu tư quyết định mức lãi suất dự thầu và khối lượng dự thầu.

– Các lệnh dự thầu được xếp theo lãi suất từ thấp đến cao. Khối lượng được cộng dồn cho đến khi đạt khối lượng gọi thầu.

– Mỗi lệnh trúng thầu được hưởng đúng mức lãi suất mà lệnh đó đã đăng ký (đặc trưng của đấu thầu đa giá).

| STT | Nhà đầu tư | Lãi suất đăng ký (%/năm) | Khối lượng đăng ký (Tỷ đồng) | Khối lượng cộng dồn (Tỷ đồng) | Khối lượng trúng thầu (Tỷ đồng) | Lãi suất trúng thầu (%/năm) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | A | 5,15% | 150 | 150 | 150 | 5,15% |
| 2 | A | 5,20% | 100 | 250 | 100 | 5,20% |
| 3 | A | 5,25% | 100 | 350 | 100 | 5,25% |
| 4 | B | 5,35% | 200 | 550 | 200 | 5,35% |
| 5 | D | 5,35% | 200 | 750 | 200 | 5,35% |
| 6 | D | 5,40% | 200 | 950 | 200 | 5,40% |
| 7 | B | 5,49% | 100 | 1.050 | 50 | 5,49% |
| 8 | B | 5,50% | 100 | 1.150 | – | – |
| 9 | C | 5,50% | 200 | 1.350 | – | – |
| 10 | D | 5,50% | 200 | 1.550 | – | – |
| 11 | F | 5,50% | 200 | 1.750 | – | – |
| 12 | C | 5,60% | 300 | 2.050 | – | – |
| 13 | D | 5,60% | 200 | 2.250 | – | – |
| 14 | D | 5,70% | 200 | 2.450 | – | – |
| 15 | E | 5,70% | 50 | 2.500 | – | – |
| 16 | B | 6,00% | 100 | 2.600 | – | – |
| 17 | G | 6,00% | 100 | 2.700 | – | – |
| 18 | H | 6,20% | 200 | 2.900 | – | – |
| **Tổng** |   |   | **2.900** |   | **1.000** |   |

**Kết quả phiên đấu thầu**

**– Khối lượng đăng ký:** 2.900 tỷ đồng.

**– Khối lượng trúng thầu:** 1.000 tỷ đồng.

**– Lãi suất trúng thầu:** từ 5,15%/năm đến 5,49%/năm.

**– Lãi suất trúng thầu cao nhất (lệnh biên):** 5,49%/năm.

**– Phân bổ lệnh biên:** 50/100 tỷ đồng.

**– Lãi suất trúng thầu bình quân gia quyền:** 5,312%/năm.

**Cách xác định kết quả:** NHNN/KBNN lần lượt chấp nhận các lệnh có lãi suất thấp nhất cho đến khi đủ 1.000 tỷ đồng. Sau 6 lệnh đầu, khối lượng cộng dồn là 950 tỷ đồng nên tại mức 5,49% chỉ cần nhận thêm 50 tỷ đồng. Vì đây là đấu thầu đa giá, từng lệnh trúng thầu áp dụng chính lãi suất dự thầu của lệnh đó, không dùng một mức lãi suất chung.

**Bình quân gia quyền:** (150×5,15% \+ 100×5,20% \+ 100×5,25% \+ 200×5,35% \+ 200×5,35% \+ 200×5,40% \+ 50×5,49%) / 1.000 \= 5,312%/năm.

**Điều kiện logic dùng cho mô hình/game**

– Lãi suất dự thầu \> 0\.

– Khối lượng dự thầu của mỗi NHTM ≥ 0\.

– Khối lượng trúng thầu của từng lệnh không vượt khối lượng đăng ký.

– Tổng khối lượng trúng thầu không vượt khối lượng gọi thầu.

– Lệnh được xét theo thứ tự lãi suất từ thấp đến cao; lệnh biên có thể được phân bổ một phần.

– Trong đấu thầu đa giá, lãi suất áp dụng cho từng lệnh trúng thầu \= lãi suất đăng ký của chính lệnh đó.

**Ownership và status**   
Source added by Hiền and Trang  
Structure designed by Hiền and Trang  
Data processed by Hiền and Trang

3. # **Data flow**  
Scenario (with Liquidity Demand) → Users determines OMO amount (→ Commercial banks submit bids) → System liquidity → Interbank rate  → Lending/Deposit Rate, Liquidity and Macroeconomic Indicators

4. # **Logic test**    
[Logic Test.xlsx](https://docs.google.com/spreadsheets/d/1DJ0j1gI4LMp_c7ggH9LKNvD9Bb5KaY1g/edit?gid=737625714#gid=737625714)  
**Ownership và status**   
Structure designed by Linh  
Logic integration by Linh

5. # **Owner and status** 

- Structure designed by Ngọc and Linh  
- Validation tested by Ngọc and Linh  
- Logic integration by Ngọc and Linh 

