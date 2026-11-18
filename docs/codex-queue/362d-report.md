# Phiếu 362d · Hỏa Nha và Thạch Thử v4

Đã tạo đủ bốn ảnh final tại `games/immortality-cultivation/art-src/beasts/`:
- `hoa-nha.v4-{q,front}-final.png`
- `thach-thu.v4-{q,front}-final.png`

Mỗi final có `.prompt.txt`: prompt nguyên văn, đường dẫn tham chiếu, lịch sử chọn ảnh và phép hậu kỳ. Bốn file `*.v4-{q,front}-raw.png` giữ lần sinh đầu; ba final được tinh chỉnh tiếp có đường dẫn nguồn sinh cuối ghi trong prompt, không ghi đè raw.

Hỏa Nha có trán quạ tròn, mỏ đen dài dày, mắt than đỏ sẫm và cổ xù. Thạch Thử có tai đá rách sẫm, lông tro bết, da nứt, răng vàng ố và dáng chồm.

## Kiểm tra

| Ảnh | Rộng vật | Cao vật | Lề nhỏ nhất |
| --- | ---: | ---: | ---: |
| Hỏa Nha q | 744 px | 678 px | 140 px |
| Hỏa Nha trước | 808 px | 678 px | 108 px |
| Thạch Thử q | 718 px | 566 px | 153 px |
| Thạch Thử trước | 814 px | 566 px | 105 px |

Canvas 1024², nền `#00FF00`; rộng 70,12–79,49%; lề ≥10,25%; lệch chiều cao mỗi cặp 0%. Script kiểm liên thông bốn hướng: mỗi ảnh một khối. Tấm ghép nền tối không thấy viền xanh sau khóa nền.

`bestiary-362d-sheet.jpg` gồm v3 | v4 ở hai góc và cả năm con trong ô 66 px. Tự chấm mặt yếu nhất: Hỏa Nha 8,5; Thạch Thử 8,5; đồng bộ bộ 8,5. Đây là tự chấm nguồn 2D, chưa phải nghiệm thu độc lập trong game. Anh xem hàng 66 px ở 100%.

Đã dùng 8/10 lượt sinh, 12/12 lượt xem. Giữ nguyên v2, v3 và ba loài còn lại. Không làm tích hợp, dựng Tripo, build/test hoặc Git vì ngoài phiếu.
