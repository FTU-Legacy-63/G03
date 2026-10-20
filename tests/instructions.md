**Backend Testing**
<br> Đặt  file test_engine.py vào cùng thư mục với central_bank_engine_v13.py, mở Terminal tại thư mục đó rồi chạy lệnh:
python -m pytest -v test_engine.py
<br>

**Frontend Testing**
<br> - Cách 1: Tại giao diện game, sao chép code rồi dán trong Console.
<br> - Cách 2: Cài đặt Node.js, đặt file test_frontend.cjs vào cùng thư mục với omo_refactored_v64(4).html, mở Terminal tại thư mục đó rồi chạy lệnh: 
python -m pytest -v test_engine.py --test test_frontend_additional.cjs
