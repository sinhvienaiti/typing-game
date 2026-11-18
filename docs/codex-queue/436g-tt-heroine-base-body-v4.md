# Phiếu 436g: Nữ chính, thân nền mặc định v4 (làm trước, thời trang để sau)

Phản biện: PASS (Sonnet, 18/11; vòng 1 thiếu lề, khe giữa hình, hướng góc, đã sửa)

## Bối cảnh
Owner 18/11: "sao không tạo nhân vật mặc định trước, còn về thời trang sẽ tạo sau?"

Hướng làm: thân nền mặc định là một bộ xương và một thân dùng chung. Nó đi trước: qua 8.5 rồi Tripo, rồi rig. Các bộ thời trang làm sau, mặc lên đúng thân này như các slot đồ.

Hai giám khảo chấm mù bảng `base-body.v3-turn.v1-try1.png` (`docs/work/tasks/heroine-blind-judging-436f.md`):
- sức hút 8.0 và 8.2;
- độ hợp làm Tripo 8.3 và 8.3;
- nhất quán giữa các góc và mặt sau đạt.

Các lỗi cần sửa:
- tay chỉ mở khoảng 20–30°;
- không có khe giữa hai đùi và hai gối;
- hình nhỏ hơn các bảng khác 4–6 %;
- ở góc nghiêng, sống mũi và cằm chưa khớp với mặt trước;
- da và mặt chưa đủ hoàn thiện.

## Việc
Dùng công cụ `image_gen`, tối đa 4 lần.

Ảnh đầu vào cho mọi lần gọi. Chỉ dùng ảnh của dự án và ghi đường dẫn vào prompt:
- (a) Mặt: `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/heroine/chan-dung-A.png`.
- (b) Thân, tỷ lệ và ba góc: `games/immortality-cultivation/art-src/heroine/fashion/base-body.v3-turn.v1-try1.png`.

Bảng 3 góc (trước, nghiêng, sau), 1536×1024. Giữ nguyên tỷ lệ 8,5 đầu và dáng trưởng thành của v3. Chỉ sửa những điểm sau:
1. **Dáng chữ A:** tay mở 35–45° so với thân, lòng bàn tay hướng vào đùi, hai bàn chân cách nhau bằng chiều rộng hông. Phải thấy rõ khe giữa hai đùi và hai gối. Tay không che thân, bàn tay duỗi mở, không cầm vật gì, không vật rời (sẵn để rig).
2. **Kích thước hình:** cả ba hình cao bằng nhau, đứng trên cùng một đường chân. Đỉnh đầu (gồm búi tóc) cách mép trên ≥ 40 px, lòng bàn chân cách mép dưới ≥ 40 px, chiều cao hình khoảng 900 px. Lề trái và phải ≥ 40 px; giữa hai hình cạnh nhau, khe trống ≥ 60 px (tay không chạm hình bên cạnh).
3. **Hướng ba góc:** góc trước nhìn thẳng; góc nghiêng nhìn ngang; góc sau là lưng thật, thấy rõ gáy và búi tóc.
   **Góc nghiêng:** nhìn ngang đúng 90°. Sống mũi, cằm và môi khớp với mặt trước và với ảnh (a).
4. **Độ hoàn thiện:** da mịn có khối, mặt sắc nét như nhân vật game tu tiên thương mại cao cấp, cuốn hút và sang trọng.
5. **Trang phục nền:** đồ lót ôm thân, vải đặc trung tính, không ren, không voan, không vật liệu xuyên thấu. Giày đế bằng hoặc gót thấp dày. Không trang sức rời. Tóc búi gọn, sát đầu.
6. **Nền và ánh sáng:** nền xám trơn, ánh sáng đều, không bóng đổ, không hào quang, không chữ, không watermark.

Sau mỗi ảnh, tự đo ba số: góc mở tay, khe giữa hai gối (px) và chiều cao hình (px). Nếu chưa đạt mục 1 hoặc 2 thì sửa lại, vẫn trong giới hạn 4 lần.

Lưu ở `games/immortality-cultivation/art-src/heroine/fashion/base-body.v4-turn.v1-try<k>.png`, mỗi ảnh kèm `.prompt.txt`. Ghép thêm một tờ so sánh v3 | v4 tên `heroine-base-v4-436g.jpg`; nếu không ghi được thư mục review thì để ở `/private/tmp/typing-game-436g/`.

## Ràng buộc
- Không đưa ảnh của game khác vào công cụ.
- Không sửa code, không làm video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
`docs/codex-queue/436g-report.md`, gồm danh sách ảnh và ba số đo của từng ảnh.
