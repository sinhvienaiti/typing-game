# Phiếu 436h: Nữ chính, thân nền v5, tăng sức hút (2 mẫu để owner chọn)

Phản biện: PASS (Sonnet, 18/11; vòng 1 lỗi dồn trọng tâm một chân và thiếu tự đo, đã sửa)

## Bối cảnh
Owner 18/11 nói "mục sức hút rất quan trọng" và chọn sửa sức hút trước rồi mới dựng Tripo.

Hai giám khảo chấm mù bản v4 (`docs/work/tasks/heroine-blind-judging-436g.md`):
- sức hút 7.9 và 8.1;
- độ nhất quán 7.9, vì ở góc nghiêng tay buông thẳng;
- độ hợp làm Tripo 8.7 và 8.4.

Lý do sức hút thấp: hình trông như một base mesh chung, chưa có chất tiên hiệp.

Owner nhấn thêm: "tôi muốn mục sức hút nó cần quyến rũ hơn nữa". Cả hai mẫu đều phải quyến rũ rõ rệt theo kiểu game thương mại, gợi cảm có chừng mực, không hở quá mức.

## Việc
Dùng công cụ `image_gen`, tối đa 4 lần: 2 mẫu, mỗi mẫu được sửa 1 lần.

Ảnh đầu vào cho mọi lần gọi. Chỉ dùng ảnh của dự án và ghi đường dẫn vào prompt:
- (a) Thân, tỷ lệ, dáng và ba góc: `games/immortality-cultivation/art-src/heroine/fashion/base-body.v4-turn.v1-try2.png`.
- (b) Mặt gốc: `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/heroine/chan-dung-A.png`.

Bảng 3 góc (trước, nghiêng, sau), 1536×1024. Giữ nguyên các điểm đạt của v4: tỷ lệ 8,5 đầu, tay mở 35–45°, chiều cao hình khoảng 900 px, lề ≥ 40 px mọi phía, khe giữa các hình ≥ 60 px, nền xám trơn, ánh sáng đều, không bóng đổ.

Phần sửa:
1. **Mặt cách điệu kiểu tiên hiệp cao cấp:** mắt phượng sắc, ánh mắt đưa tình, viền mi rõ, lông mày thanh, môi màu hồng đào tinh tế, gương mặt thanh tú và cuốn hút. Vẫn nhận ra là người trong ảnh (b).
2. **Tóc:** búi cao đầy đặn kiểu cổ trang. Khối tóc đặc, không có sợi bay rời. Có chỗ để cắm trâm nhưng không vẽ trâm.
3. **Dáng:** cổ dài hơn, vai mềm và thon, eo thon và cao. Đường cong rõ hơn v4: ngực đầy hơn, hông và đùi tròn đầy hơn. Trọng tâm chia đều hai chân, dáng đối xứng để rig; sức hút đến từ đường cong hông mềm và tư thế cổ, vai thanh. Đường cong đầy hơn nhưng vẫn là thân trung tính để mặc các bộ đồ sau.
4. **Da:** có ánh trong nhẹ (subsurface). Ánh sáng studio ấm hơn nhưng vẫn đều, không có điểm chói.
5. **Góc nghiêng:** tay cũng mở theo dáng chữ A. Mặt và búi tóc khớp với góc trước.
6. **Chân:** có khe rõ từ háng xuống mắt cá. Ngón tay hơi tách nhau. Chân trần, hoặc giày bệt vẽ thành khối riêng gọn.
7. **Đồ lót:** ôm thân, vải đặc trung tính, không ren, không trong suốt, không trang sức rời.

Hai mẫu khác nhau ở khí chất của mặt:
- A: lạnh lùng, cao quý, kiểu tiên nữ băng.
- B: dịu dàng, quyến rũ, kiểu tiên nữ hoa.

Sau mỗi ảnh tự đo: góc mở tay (cả góc nghiêng), khe gối (px), chiều cao hình (px), lề nhỏ nhất (px). Chưa đạt thì dùng lần sửa của mẫu đó.

Lưu ở `games/immortality-cultivation/art-src/heroine/fashion/base-body.v5<A|B>-turn.v1-try<k>.png`, mỗi ảnh kèm `.prompt.txt`. Ghép thêm một tờ `heroine-base-v5-436h.jpg` gồm v4 | v5A | v5B, có thêm ô phóng to mặt của mỗi bản. Nếu không ghi được thư mục review thì để ở `/private/tmp/typing-game-436h/`.

## Ràng buộc
- Không đưa ảnh của game khác vào công cụ.
- Không sửa code, không làm video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
`docs/codex-queue/436h-report.md`, gồm danh sách ảnh, số đo từng ảnh, và bản đề xuất cuối của mỗi mẫu (A, B).
