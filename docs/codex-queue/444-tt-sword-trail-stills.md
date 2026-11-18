# Phiếu 444: Ảnh tĩnh vệt sáng kiếm bay (thành phần cho mưa kiếm Kim)

Phản biện: PASS (Sonnet, 17/11)

## Bối cảnh
Ngày 17/11 owner xem bản 433f và chê vệt sáng sau kiếm: "hào quang vệt sáng của kiếm đang nhìn rất xấu, rất thô… vệt sáng sau kiếm nhìn rất to, không phù hợp dạng vệt sáng thể hiện kiếm bay chút nào, nó cần được làm bằng cách khác để có vệt sáng hào quang đẹp hơn". Ảnh lỗi: `typing-game-review/owner-review/2026-11-17/tu-tien/metal-rain-f.jpg`.

Cách mới làm theo luật "thành phần trước":
1. Vẽ ảnh tĩnh một vệt sáng kiếm bay, không vẽ kiếm.
2. Owner chọn một mẫu.
3. Code gắn vệt đó phía sau mỗi thanh kiếm, kéo dài theo tốc độ rơi.

## Việc
Dùng công cụ `image_gen`, tối đa 4 lần (4 biến thể, mỗi biến thể 1 lần).

Ảnh tham chiếu, chỉ dùng ảnh của dự án và ghi đường dẫn vào prompt:
- `games/immortality-cultivation/art-src/concept/ult-metal/rain-components/sword-fall-streak.v1-try1.png`: lấy màu vàng ấm và chất khí tiên mảnh quanh kiếm. Không vẽ lại thanh kiếm.
- Nửa trái của `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`, ô trên phải: lấy cảm giác vệt sáng mảnh của kiếm đang rơi.

Yêu cầu chung cho cả 4 biến thể:
- Mỗi ảnh có **một** vệt sáng dọc trên nền đen tuyền, kích thước 1024×1024.
- Đầu vệt (nơi kiếm sẽ nằm) ở dưới, tại 85 % chiều cao. Đuôi vệt tan dần lên phía trên tới khoảng 10 %.
- Vệt **mảnh**: chỗ rộng nhất ≤ 8 % bề ngang khung. Lõi sáng trắng ấm rất mảnh, thuôn nhọn về đuôi. Quầng vàng hổ phách mỏng, mờ dần ra mép.
- Có lấp lánh: vài hạt sáng nhỏ rơi rớt dọc vệt.
- Không vẽ kiếm, không chữ, không vòng.

Bốn biến thể:
- **A:** một vệt thẳng mảnh như sao băng, đuôi dài tan mềm.
- **B:** vệt thẳng mảnh, có hai sợi khí tiên rất mảnh xoắn nhẹ quanh lõi.
- **C:** vệt mảnh, đuôi tách thành 2–3 sợi sáng mảnh như lông vũ.
- **D:** vệt mảnh, đuôi kéo thành chuỗi hạt sáng lấp lánh thưa dần.

Lưu ảnh ở `games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/sword-trail.v1-try<k>.png`, kèm `.prompt.txt` cùng tên.

Ghép tờ `sword-trail-444.jpg` có nhãn A–D. Nếu sandbox không cho ghi vào thư mục review thì để tờ ghép ở `/private/tmp/typing-game-444/`.

## Ràng buộc
Không sửa code, không làm video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh. Không dùng ảnh của game khác.

## Giao nộp
`docs/codex-queue/444-report.md`.
