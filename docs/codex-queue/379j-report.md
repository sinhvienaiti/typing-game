# 379j · Chưa đạt

Đã lưu `S/thunder-energy-sharp.v2-try{1,2}.png`, `S/thunder-energy-sharp-frames.v2-try{1,2}.png`, bốn prompt nguyên văn và `S/thunder-energy-379j-sheet.jpg`; S theo phiếu.

Đo bằng Python/ImageMagick: HSL L>0,5; hue trung bình tròn, bỏ điểm vô sắc; lõi L>0,9, S<0,15. So với v4 tương ứng:

| Bản | ΔS | ΔH | Lõi/trước |
| --- | ---: | ---: | ---: |
| Cột 1 | −0,004 | 4,16° | 0,644 |
| Cột 2 | +0,067 | 5,17° | 0,602 |
| Dải 1 | −0,084 | 9,95° | 0,939 |
| Dải 2 | −0,070 | 0,90° | 1,003 |

Cả bốn FAIL. Sheet dùng cột 1/dải 2. MAE xám BT.709: 2,26%/3,33%; lệch tâm hàng tia theo R≥250: 2,89/2,18 px. Đường gãy cùng bố cục, chưa bảo toàn từng pixel.

Tự chấm nguồn chính/tia phụ/độ dày/nét sét/đúng màu: 8,5/8,5/8/8/8; cuối **8/10**.

Hết 4/4 lượt. Giữ bản cũ; cần anh xem sheet.
