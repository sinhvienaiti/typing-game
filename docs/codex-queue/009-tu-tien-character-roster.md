# Phiếu 009 · Tu Tiên Thủ Ải · chân dung concept cho cả danh sách nhân vật

**Bối cảnh:** chủ dự án hỏi vì sao chỉ có một ảnh nhân vật. Canon mới thêm **D49**: mỗi trường phái có 1 nam và 1 nữ để người chơi chọn. Năm trường phái: Kiếm, Thổ thể (MVP), Phù, Hỏa, Ngự thú (sau MVP). Tất cả theo phong cách quý phái của **D47**.

Chạy **sau** phiếu 008, để dùng thiết kế nữ Kiếm tu mới làm chuẩn phong cách.

**Thư mục làm việc:** gốc repo `D:\typing-game`. Được ghi vào:
- `docs/games/tu-tien/art-requests/m0b/06-roster.md` (file prompt mới);
- `games/immortality-cultivation/art-src/roster/` (ảnh);
- `games/immortality-cultivation/art-src/README-roster.md`.

Không chạy git.

## Nguồn

- `docs/games/tu-tien/00-canon.md`: §3 (D03, D47, D48, D49), §11 ngũ hành, §12 trường phái, và bản sắc "sơn thủy huyền ảo chất Việt".
- Bộ prompt đã có: `docs/games/tu-tien/art-requests/m0b/` (giữ cùng khối phong cách chung). Ảnh nữ Kiếm tu mới của phiếu 008 dùng làm tham chiếu phong cách.

## Việc

1. **Viết `06-roster.md`.** Mỗi nhân vật có một khối prompt chân dung, gồm:
   - tên tạm theo canon;
   - trường phái, hệ, bảng màu;
   - trang phục riêng nhưng cùng một gia đình phong cách (lụa nhiều lớp, viền thêu, ngọc, miện hoặc trâm; nam có phong thái vương giả, nữ thanh tú quý phái);
   - vũ khí hoặc pháp khí: Kiếm (kiếm), Thổ thể (găng hoặc trượng đá, giáp ngọc thổ), Phù (bút và phù lục), Hỏa (quạt hoặc ấn lửa), Ngự thú (sáo, kèm một linh thú nhỏ).
   - Không gợi cảm, không hở hang, hợp mọi lứa tuổi.
   - Không chép tên, trang phục hay hình của game khác.
2. **Tạo 10 chân dung** (5 trường phái × nam, nữ):
   - nữ Kiếm tu dùng bản đã chọn ở phiếu 008, không tạo lại;
   - cộng 1 ảnh "đội hình" xếp cả 10 nhân vật cạnh nhau để xem tổng thể;
   - lưu vào `art-src/roster/<truong-phai>-<nam|nu>.png`, kèm prompt.
   - Ảnh hỏng rõ thì tạo lại tối đa 1 lần.
3. **Viết `README-roster.md`**: bảng nhân vật, nhận xét, câu hỏi để chủ dự án chọn hoặc sửa.

**Không làm ảnh nguồn 3D** ở phiếu này. Ảnh 3D chỉ làm sau khi chủ dự án duyệt.

**Xong khi:** prompt viết xong; đủ 9 chân dung mới cộng ảnh đội hình (hoặc ghi lý do); README đã viết.
