# Phiếu 448: Ảnh tĩnh hào quang cho kiếm lớn (mưa kiếm Kim)

Phản biện: PASS (Sonnet, 18/11)

## Bối cảnh
Ngày 18/11 owner nhận xét về kiếm lớn: "kiếm to đang tự dùng code để làm viền ánh sáng nhìn rất xấu, cần sửa lại k dùng code". Viền đang dùng là flipbook lông nhọn `aura-metal-feather-mantle`, phủ thêm một lớp nhuộm vàng phẳng.

Hào quang mới phải là ảnh thật, owner chọn mẫu rồi mới đưa vào game. Ảnh đặt phía sau kiếm lớn như một lớp nền. Kiếm thật (mô hình Tripo) vẫn nằm ở trước.

## Việc
Dùng công cụ `image_gen`, đúng 4 lần: 4 biến thể A–D, mỗi biến thể vẽ 1 lần.

Ảnh tham chiếu (chỉ dùng ảnh của dự án, ghi đường dẫn vào prompt):
- `games/immortality-cultivation/art-src/concept/ult-metal/rain-components/sword-fall-streak.v1-try1.png`: dáng thanh kiếm và chất khí tiên vàng mảnh quanh kiếm.
- `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`, nửa trái, ô dưới trái: kiếm lớn cắm giữa trận, có ánh vàng toả ra.

Yêu cầu chung cho mọi ảnh:
- Kích thước 1024×1024, nền đen tuyền.
- Chỉ vẽ **hào quang**, không vẽ kiếm. Giữa ảnh để trống một khe dọc hình thanh kiếm mũi chĩa xuống (rộng khoảng 12 %, cao khoảng 70 %), đúng chỗ kiếm thật sẽ đặt vào.
- Hào quang ôm sát quanh khe đó. Lề ≥ 8 %.
- Phong cách sang trọng, mềm và sáng: ánh vàng kim nhiều lớp, khí tiên mảnh, hạt lấp lánh. Không gai, không lông nhọn, không vòng tròn, không chữ.

Bốn biến thể:
- **A:** quầng sáng vàng mềm ôm dọc kiếm, mờ dần ra ngoài, có vài tia sáng mảnh.
- **B:** các dải khí tiên mảnh bốc lên dọc hai bên kiếm như lửa vàng nhẹ.
- **C:** quầng sáng hình thoi dài, mũi phía trên và dưới loé thành ngôi sao.
- **D:** ánh sáng thần thánh: tia sáng dọc rủ từ trên xuống quanh kiếm, kèm hạt sáng.

Lưu ảnh ở `games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/giant-sword-aura.v1-try<k>.png`, kèm `.prompt.txt` cùng tên.

Ghép tờ `giant-sword-aura-448.jpg` có nhãn A–D, kèm một hàng xem thử: mỗi ảnh hào quang đặt sau ảnh kiếm `sword-fall-streak` trên nền đá tối. Nếu sandbox không cho ghi thư mục review, để tờ ghép ở `/private/tmp/typing-game-448/`.

## Ràng buộc
Không sửa code, không làm video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh. Không dùng ảnh của game khác.

## Giao nộp
`docs/codex-queue/448-report.md`.
