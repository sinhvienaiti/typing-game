# Phiếu 436k: Nữ chính, bộ ảnh sợi tóc cho tóc dạng thẻ (hair cards) trong Blender

Phản biện: PASS (Sonnet, 18/11; vòng 3, đã sửa bố cục, độ sáng, số lần vẽ)

## Bối cảnh
Owner 18/11 chê tóc của mô hình 3D: "tóc tai mắt mũi miệng khá kém chất lượng". Tóc Tripo là một khối đặc. Owner chỉ cho dùng công cụ miễn phí: Tripo, Firefly, Blender.

Cách làm: dựng tóc dạng thẻ (hair cards) trong Blender. Đó là nhiều dải mặt phẳng, mỗi dải dán ảnh một lọn tóc. Phiếu này làm phần ảnh lọn tóc. Màu và kiểu tóc lấy theo bản v6B owner đã chọn.

## Việc
Dùng công cụ `image_gen`, tối đa 6 lần (4 tấm, thêm 2 lần vẽ lại nếu cần).

Ảnh tham chiếu (của dự án, ghi đường dẫn vào prompt): `games/immortality-cultivation/art-src/heroine/fashion/base-body.v6B-turn.v1-try2.png`, chỉ lấy màu tóc (đen ánh nâu) và độ bóng.

Mỗi lần gọi vẽ một tấm 2048×2048, nền đen tuyền (để tách ra làm kênh trong suốt sau). Các lọn tóc nằm thẳng đứng, gốc ở trên, ngọn ở dưới, không chồng lên nhau, cách nhau ≥ 24 px, lề ≥ 32 px. Tóc thật, sợi mảnh rõ từng sợi, có ánh bóng chạy dọc lọn (dạng dải sáng ngang kiểu tóc đen bóng). Không có đầu người, da, phụ kiện hay chữ.

Tóc phải sáng đủ để tách khỏi nền đen: thân lọn màu nâu đen có trung độ rõ (đo: độ sáng trung bình của các điểm ảnh thuộc lọn, bỏ nền đen < 0,04, phải ≥ 0,25 trên thang 0–1), có dải bóng sáng; ngọn lọn thuôn mảnh nhưng vẫn thấy được. Kênh trong suốt sẽ lấy theo độ sáng, không cần vẽ mặt nạ riêng.

1. `hair-cards-a`: 1 hàng, 8 lọn dày, chạy từ trên xuống dưới trong lề, rộng 160–220 px, dài 1600–1800 px (lớp tóc nền).
2. `hair-cards-b`: 2 hàng × 6 lọn vừa, rộng 90–140 px, dài 800–950 px mỗi hàng, có lọn hơi cong.
3. `hair-cards-c`: 2 hàng × 10 lọn mảnh và sợi tóc bay, rộng 20–60 px, dài 600–950 px mỗi hàng (tóc con, mai tóc).
4. `hair-cards-d`: lưới 3 × 2 ô, lưới đặt giữa tấm, mỗi ô 600×600 px; trong mỗi ô một lọn cuộn tròn kiểu búi tóc (xoắn ốc) đường kính khoảng 500 px, cách mép ô ≥ 32 px; gốc lọn ở phía trên của vòng xoắn, ngọn thuôn ở tâm.

Sau mỗi tấm, đếm số lọn, kiểm khe ≥ 24 px, đo độ sáng lọn và kiểm gốc lọn ở trên (đầu dày phía trên, ngọn thuôn phía dưới). Thiếu lọn hoặc lọn chồng nhau thì vẽ lại tấm đó, trong giới hạn 6 lần; còn thiếu thì ghi rõ trong báo cáo.

Lưu ở `games/immortality-cultivation/art-src/heroine/hair/<tên>.v1-try1.png`, mỗi ảnh kèm `.prompt.txt` (tạo thư mục nếu chưa có). Ghép thành một tờ `hair-cards-436k.jpg`; nếu không ghi được thư mục review thì để ở `/private/tmp/typing-game-436k/`.

## Ràng buộc
Không sửa code, không làm video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh. Không dùng ảnh của game khác.

## Giao nộp
`docs/codex-queue/436k-report.md`, gồm danh sách ảnh và số lọn đếm được trong mỗi tấm.
