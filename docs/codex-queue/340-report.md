# Phiếu 340 · Bộ bốn góc nhân vật chính · 12/11/2026

Đã tạo đủ 5 loại ảnh bằng `image_gen`, **8 lần gọi** gồm 3 lần vẽ lại; mở **9 ảnh** bằng `view_image`. Chỉ thêm file trong `games/immortality-cultivation/art-src/heroine/` (H) và báo cáo này. Không sửa mã, không chạy build/test, không gọi Tripo, không dùng ảnh ngoài repo.

**Bộ đề nghị xem:** `turnaround.v1-try2.png`, `view-front.v1-try1.png`, `view-back.v1-try2.png`, `view-left.v1-try1.png`, `view-play.v1-try2.png`. Các tên `try1` yêu cầu đều có; giữ cả 3 bản thử lại và đủ 8 `.prompt.txt` nguyên văn, kèm đường dẫn tham chiếu. Tấm ghép: [turnaround-340-sheet.jpg](../../games/immortality-cultivation/art-src/heroine/turnaround-340-sheet.jpg), có mô tả ghép riêng `.prompt.txt`. Số đo và nguồn gốc: `H/measurements-340.json`.

## Kiểm cơ học

ImageMagick 7; nhận nền bằng fuzz 12% quanh xanh chuẩn, lấy bbox alpha ở ngưỡng 50%. Chỉ cắt nền trống, đổi kích thước đồng đều và thêm khung xanh; không vẽ sửa người. Gốc chưa xử lý giữ nguyên trong thư mục generated_images; JSON ghi đường dẫn từng ảnh và phép biến đổi.

| Ảnh chọn | Khổ px | Người cao px | Lề trái / phải / trên / dưới (%) |
|---|---:|---:|---|
| Tờ xoay try2 | 2048×1152 | 876, cả bộ | 14,16 / 14,16 / 11,98 / 11,98 |
| Trước try1 | 1152×1536 | 1152 | 24,91 / 25,00 / 12,50 / 12,50 |
| Sau try2 | 1152×1536 | 1152 | 24,39 / 24,48 / 12,50 / 12,50 |
| Trái try1 | 1152×1536 | 1152 | 39,67 / 39,76 / 12,50 / 12,50 |
| Góc chơi try2 | 1152×1536 | 1152 | 25,26 / 25,35 / 12,50 / 12,50 |

Bốn góc ngoài của mọi PNG cuối: RGB **(0,255,0)**. Phần nền gốc bên trong vùng cắt vẫn hơi khác xanh chuẩn, thấy ranh khung khi nhìn kỹ; chưa thay nền toàn phần. Chênh chiều cao 4 ảnh riêng: **0%** sau chuẩn hóa. Bốn cột trước/trái/sau/phải trên tờ try2: gốc **882 / 881 / 883 / 881 px**, chênh **0,227%**; chân gần cùng đường, sai lệch khoảng 1 px. Lề ≥8% và chênh ≤3% đạt.

## Nhất quán 11 chi tiết × 4 góc

Đối chiếu tờ xoay try2 với các ảnh riêng; góc phải chỉ có trong tờ. “Có” nghĩa là quan sát được, không đồng nghĩa đúng mọi kích thước. “Không (khuất)” không phải thiếu cấu tạo.

| Chi tiết | Trước | Trái | Sau | Phải (tờ) |
|---|---|---|---|---|
| Diadem ngọc trắng / vàng cũ | Có | Có | Có | Có |
| Búi tóc cao, khối đặc | Có | Có | Có | Có |
| Cổ lõi chàm, rìa ngà | Có | Có | Có | Có |
| Ấn phượng lưng | Không (khuất) | Có, cạnh | Có | Có, cạnh |
| Thắt lưng / tấm hộ eo | Có / Có | Có / cạnh | Có / khuất | Có / cạnh |
| Ngọc bội bên trái | Có | Có | Có ở ảnh riêng try2; khuất trên tờ | Không (khuất) |
| Hai đuôi lưng | Không (khuất) | Có 1, còn lại khuất | Có 2 | Có 1, còn lại khuất |
| Ống tay bó | Có | Có | Có | Có |
| Quần ống rộng | Có | Có | Có | Có |
| Giày cao cổ | Có | Có | Có | Có |
| Kiếm thấp ngang xương cùng | Không (khuất) | Có, đầu vỏ | Có, chuôi phải | Có, chuôi |

Lưng thật là lưng: không thấy mặt, mắt hay vạt khóa trước. Góc chơi có đủ các chi tiết thấy được từ sau, tay phải nắm chuôi; tấm hộ eo trước bị khuất.

## Ô 66 px, tự chấm và vẽ lại

Tấm ghép đặt ảnh sau/góc chơi cạnh bản thu **toàn khung cao 66 px → phóng 4×**, đồng thời thêm bản **người cao đúng 66 px → 4×**. Ba khối tóc đen, vai chàm có rìa ngà và thân ngà còn tách được ở cả hai góc. Phượng chỉ còn thành mảng ấn tròn vàng/chàm, **không đọc rõ con phượng**; chi tiết dày ở cổ và gấu bị nhập.

| Mặt chấm | Điểm tự chấm sau cùng / 10 |
|---|---:|
| Cùng người chân dung A | 8,0 |
| Nhất quán các góc | 8,0 |
| Gom khối để dựng mesh | 7,7 |
| Sang, cuốn hút | 8,3 |
| Đọc ở 66 px | 7,6 |
| **Mặt yếu nhất** | **7,6** |

Ba lần vẽ lại: tờ xoay try2 sửa thiếu hai đuôi phía sau; ảnh sau try2 sửa ấn cứng như tấm giáp, thêm ngọc trái; góc chơi try2 sửa camera quá ngang (bản đầu khoảng 7,2 ở tiêu chí camera). Camera cuối nhìn xuống rõ hơn, nhưng **30° chưa được xác thực bằng hình học**. Ấn sau try2 bớt dày nhưng còn cảm giác phù hiệu. Không gọi lần thứ 9.

**Chưa đạt brief để chuyển Tripo:** rìa ngà khoảng 2–3% chiều cao người, chưa tới ≥4%; đường kính ấn sau khoảng 16–17%, chưa đạt 25%; hò chéo có nhưng đường tà ngũ thân còn yếu; hoa văn nhỏ trên quần và thân vẫn nhiều. Mặt donghua sạch nhưng giống A chưa đủ để coi là khóa danh tính. Tự chấm không phải hai giám khảo mù, không phải nghiệm thu 8,5.

Không bỏ loại ảnh nào. Dừng đúng trần 8 lượt của phiếu, không gặp HTTP 429 hay giờ chờ từ công cụ. Chủ xem tấm ghép và các sai lệch trên trước khi quyết định lượt tiếp theo; chưa gửi ảnh nào sang Tripo.

