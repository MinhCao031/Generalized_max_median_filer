# Generalized_max_median_filer

- Trong project có sử dụng 2 phương pháp lọc ảnh dựa trên phương pháp lọc trung vị, đó là 
  + Max median filter
  + Generalized max median filer. 
- Khái niệm và phương pháp lọc được đề cập trong [file báo cáo](https://github.com/MinhCao031/Generalized_max_median_filer/raw/main/Report.pdf)

- Trong các file được đính kèm:
  + File funcs.py chứa tất cả các hàm cần thiết. Các file khác sẽ import từ file này.
  + File extend.py thực hiện việc kéo dài bức ảnh về phía các cạnh, dùng để demo cho 
bài báo cáo này cũng như phục vụ cho việc xử lý các pixel ở gần biên khi áp dụng 
các bộ lọc max/median. Để minh họa việc kéo dài ảnh chỉ cần chạy lệnh:
python extend.py
  + File max_median_filter.py tiến hành lọc ảnh theo bộ lọc max/median thông 
thường. Để xem kết quả của phép lọc max/median thường chỉ cần chạy lệnh:
python max_median_filter.py
  + File generalized_max_median_filter.py tiến hành lọc ảnh theo bộ lọc max/median
tổng quát. Để xem kết quả của phép lọc max/median tổng quát chỉ cần chạy lệnh:
python generalized_max_median_filter.py
