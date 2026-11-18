# Phiếu 436j: Nữ chính, thân nền v6: cao hơn, quyến rũ hơn, da trắng hồng, mặt đẹp hơn (2 mẫu để owner chọn)

Phản biện: PASS (Sonnet, 18/11)

## Bối cảnh
Owner 18/11 xem mô hình Tripo dựng từ thân nền v5B và nhận xét:

> "1 là hơi lùn, 2 là body chưa quyến rũ, 3 là nước da không trắng hồng, 4 là gương mặt đang chưa đẹp, về cơ bản nhìn giống búp bê chứ chưa có nét đẹp quyến rũ"

Claude thấy các lỗi gây ra cảm giác búp bê:
- mắt to và tròn;
- mặt phẳng, thiếu khối xương gò má và đường hàm;
- da xám hồng nhạt;
- đường cong cơ thể còn hiền.

Bản v6 sửa từ nguồn 2D. Owner chọn mẫu xong mới dựng Tripo lại.

## Việc
Dùng công cụ `image_gen`, tối đa 4 lần: 2 mẫu, mỗi mẫu được sửa 1 lần.

Ảnh đầu vào cho mọi lần gọi. Chỉ dùng ảnh của dự án và ghi đường dẫn vào prompt:
- (a) Dáng chữ A, ba góc và đồ lót: `games/immortality-cultivation/art-src/heroine/fashion/base-body.v5B-turn.v2-try1.png`.
- (b) Nét mặt gốc: `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/heroine/chan-dung-A.png`.

Bảng 3 góc (trước nhìn thẳng, nghiêng 90°, sau thấy đúng lưng), 1536×1024. Giữ các điểm đã đạt:
- dáng chữ A đối xứng, tay mở 35–45° ở cả ba góc, trọng tâm chia đều hai chân;
- ngón tay tách nhau, chân trần, có khe từ háng xuống mắt cá;
- nền xám trơn, ánh sáng đều, không bóng đổ;
- lề ≥ 40 px mọi phía, khe giữa các hình ≥ 60 px;
- đồ lót ôm thân bằng vải đặc, mặt vải **mờ, không bóng**.

Phần sửa:
1. **Cao hơn:** tỷ lệ 9 đầu. Chân dài: khoảng từ háng xuống đất ≥ 52 % chiều cao. Cẳng chân thon dài, cổ dài. Chiều cao hình khoảng 900 px.
2. **Thân quyến rũ:** ngực đầy, eo rất thon và cao, hông và mông tròn đầy, đùi thon. Đường cong chữ S rõ ở góc nghiêng. Gợi cảm có chừng mực kiểu game thương mại, không hở thêm.
3. **Da trắng hồng:** trắng sứ ấm có sắc hồng ở má, môi, khớp gối và khuỷu tay. Có ánh trong nhẹ (subsurface). Không xám, không vàng.
4. **Mặt đẹp kiểu người trưởng thành, không kiểu búp bê:** mắt phượng dài vừa phải (không to tròn), đuôi mắt hơi xếch, ánh mắt đưa tình. Gò má cao có khối, đường hàm thon (V-line). Sống mũi thanh, môi đầy màu hồng đào. Trang điểm nhẹ. Nét đẹp quyến rũ như nữ chính game tu tiên thương mại cao cấp, vẫn nhận ra là người trong ảnh (b).
5. **Ánh sáng:** ánh sáng studio đều nhưng ấm hơn, làm rõ khối mặt và đường cong. Không có điểm chói.

Hai mẫu khác nhau ở mức độ:
- A: quyến rũ thanh lịch, mắt đưa tình nhẹ.
- B: quyến rũ đậm hơn: đường cong rõ hơn, môi đầy hơn, ánh mắt sắc và mời gọi.

Sau mỗi ảnh tự đo: số đầu, tỷ lệ từ háng xuống đất so với chiều cao (%), góc mở tay ở cả ba góc, chiều cao hình (px), lề nhỏ nhất (px). Chưa đạt thì dùng lần sửa của mẫu đó.

Lưu ở `games/immortality-cultivation/art-src/heroine/fashion/base-body.v6<A|B>-turn.v1-try<k>.png`, mỗi ảnh kèm `.prompt.txt`. Ghép một tờ `heroine-base-v6-436j.jpg` gồm v5B | v6A | v6B, có ô phóng to mặt của mỗi bản. Nếu không ghi được thư mục review thì để ở `/private/tmp/typing-game-436j/`.

## Ràng buộc
- Không đưa ảnh của game khác vào công cụ.
- Không sửa code, không làm video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
`docs/codex-queue/436j-report.md`, gồm danh sách ảnh, số đo từng ảnh, và bản đề xuất của mỗi mẫu.
