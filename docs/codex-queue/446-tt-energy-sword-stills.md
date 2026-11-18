# Phiếu 446: Ảnh tĩnh kiếm năng lượng (kiếm nhỏ của mưa kiếm Kim)

Phản biện: PASS (Sonnet, 18/11, vòng 3)

## Bối cảnh
Owner (18/11): "kiếm đang quá xấu, tôi đã nói với mưa kiếm, chỉ kiếm to là dùng hình, các kiếm con nên dùng dạng năng lượng cơ mà". Phiếu 433g vẫn dùng mô hình Tripo cho kiếm nhỏ, phủ thêm emissive. Cách đó sai.

Kiếm nhỏ phải là **kiếm năng lượng** làm từ ảnh thật, không vẽ bằng code. Các bước:
1. Vẽ ảnh tĩnh.
2. Owner chọn.
3. Code đặt mỗi kiếm nhỏ thành một tấm ảnh quay theo trục rơi, gắn vệt D đã chọn.

## Việc
Dùng công cụ `image_gen`, đúng 4 lần (4 biến thể A–D, mỗi biến thể 1 lần).

Ảnh tham chiếu (chỉ ảnh của dự án; ghi đường dẫn vào prompt):
- `games/immortality-cultivation/art-src/concept/ult-metal/rain-components/sword-fall-streak.v1-try1.png`: lấy dáng kiếm và màu vàng ấm. Không vẽ lại kiếm kim loại đặc.
- `games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/sword-trail.v1-try4.png`: vệt D owner đã chọn. Kiếm phải hợp với vệt này.

Quy tắc chung cho cả 4 biến thể:
- Mỗi ảnh một thanh kiếm dựng đứng, mũi chĩa xuống, trên nền đen tuyền, 1024×1024.
- Kiếm chiếm 60–70 % chiều cao khung, nằm giữa, lề ≥ 12 %.
- Kiếm phải là **kiếm khí năng lượng**: thân trong mờ màu vàng kim, lõi sáng trắng ấm dọc sống kiếm, mép kiếm toả khí sáng mảnh, chuôi đơn giản cũng bằng ánh sáng. Không kim loại đặc, không chi tiết chạm khắc nặng.
- Kiếm vẫn phải đọc rõ là thanh kiếm khi thu nhỏ còn khoảng 30 px.
- Không chữ, không vòng.

Bốn biến thể:
- **A:** kiếm khí gọn, thẳng, viền sáng sắc.
- **B:** kiếm khí có hai sợi khí mảnh chạy dọc theo thân, lượn nhẹ, không khép thành vòng.
- **C:** kiếm khí như pha lê ánh sáng, cạnh vát lấp lánh.
- **D:** kiếm khí mờ ảo, mép tan thành khí ở chuôi.

Lưu ảnh ở `games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/energy-sword.v1-try<k>.png`, kèm `.prompt.txt` cho mỗi ảnh.

Ghép tờ `energy-sword-446.jpg` có nhãn A–D. Thêm một hàng: mỗi kiếm thu nhỏ còn 30 px, đặt trên nền đá tối. Nếu sandbox không cho ghi vào thư mục review, để tờ ghép ở `/private/tmp/typing-game-446/`.

## Ràng buộc
Không sửa code, không làm video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh. Không dùng ảnh của game khác.

## Giao nộp
`docs/codex-queue/446-report.md`.
