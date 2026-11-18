# Phiếu 452c: Ánh kim cương, điểm nhấn của tuyệt kỹ Tinh Tú

Phản biện: PASS (Sonnet, 18/11)

## Bối cảnh
Theo kế hoạch `docs/work/tasks/star-ult-plan.md` (hàng 10), viên sao băng thứ bảy nổ thành ánh kim cương. Đây là điểm nhấn duy nhất của chiêu và là lớp duy nhất được sáng HDR. Code đặt nó thành billboard cỡ 4–5 m ở điểm chạm. Sau khi owner chọn mẫu, ảnh sẽ được làm thành video bung nở rồi tắt.

## Việc
Dùng công cụ `image_gen`, đúng 3 lần.

Ảnh tham chiếu, chỉ dùng ảnh của dự án và ghi đường dẫn vào prompt:
- `games/immortality-cultivation/art-src/lab/vfx/star-ult/stills/star-constellation.v1-try1.png`: màu và kiểu tia sáng của sao.

Mỗi ảnh 1024×1024, nền đen tuyền, nhìn thẳng mặt. Một ánh lóe kim cương: lõi trắng ≤ 30 % đường kính, nhiều tia sắc như mặt cắt kim cương, quầng vàng trắng và tím chàm nhạt, có vài hạt lấp lánh. Lề ≥ 12 %. Không chữ, không vật khác.
- A: tám tia chính dài, tia phụ ngắn xen kẽ.
- B: hình ngôi sao kim cương nhiều mặt, ánh khúc xạ cầu vồng nhẹ ở mép.
- C: vòng sáng mỏng quanh lõi, tia chữ thập dài.

Lưu ở `games/immortality-cultivation/art-src/lab/vfx/star-ult/stills/star-diamond-glint.v1-try<k>.png`, mỗi ảnh kèm `.prompt.txt`. Ghép thành một tờ `star-diamond-452c.jpg`; nếu không ghi được thư mục review thì để ở `/private/tmp/typing-game-452c/`.

## Ràng buộc
Không sửa code, không làm video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh. Không dùng ảnh của game khác.

## Giao nộp
`docs/codex-queue/452c-report.md`, gồm danh sách ảnh.
