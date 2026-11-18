# Phiếu 451d: Bảo kính Nhật Luân, vẽ lại theo tông hệ Quang, kèm góc nghiêng và mặt sau

Phản biện: PASS (Sonnet, 18/11)

## Bối cảnh
Owner 18/11 chọn mẫu A, Nhật Luân Kính (`light-relic-mirror-a.v1-try1.png`). Hai giám khảo chấm mù (`docs/work/tasks/blind-judging-v5b-relic.md`) cho 7.6–8.2 và chỉ ra ba lỗi:
- màu cam vàng và mặt kính như dung nham khiến bảo kính giống hệ Hỏa, không giống hệ Quang;
- lông vũ và hoa văn chạm quá mảnh, Tripo khó dựng;
- ảnh chưa cho thấy độ dày và mặt sau.

Owner chọn "Vẽ lại tông Quang".

## Việc
Dùng công cụ `image_gen`, tối đa 3 lần.

Ảnh đầu vào là ảnh của dự án, ghi đường dẫn vào prompt:
- `games/immortality-cultivation/art-src/lab/vfx/light/stills/light-relic-mirror-a.v1-try1.png`: giữ dáng, bố cục phượng ôm vành và viên ngọc ở đỉnh.
- `games/immortality-cultivation/art-src/lab/vfx/light/stills/light-ray-a2.v1-try2.png`: tông sáng của tia đã chọn.

Ảnh là một bảng 3 góc (trước 3/4, nghiêng thấy độ dày, sau), 1536×1024. Nền xám trơn, ánh sáng đều, không bóng đổ, lề ≥ 6 % mọi phía.
- **Màu hệ Quang:** vàng nhạt pha trắng ngà và vàng champagne, không có cam hay đỏ lửa. Viên ngọc ở đỉnh đổi thành kim cương hoặc ngọc trắng ấm.
- **Mặt kính:** đá mặt trăng trắng ấm, có vân sáng mềm như ánh bình minh. Mặt kính đặc, không trong suốt, không có vân dung nham.
- **Khối:** lông vũ và hoa văn vẽ dày và khối hơn, gom thành các mảng lớn; không có sợi mảnh hay chi tiết rời. Vành dày khoảng 12–15 % đường kính. Mọi phần nối liền nhau.
- **Mặt sau:** có hoa văn chạm đơn giản và một núm ở giữa.
- Sang trọng, cuốn hút như pháp bảo trong game tu tiên thương mại. Không hào quang, không tia sáng, không chữ, không watermark.

Lưu ở `games/immortality-cultivation/art-src/lab/vfx/light/stills/light-relic-mirror-a.v2-try<k>.png`, mỗi ảnh kèm `.prompt.txt`. Ghép tờ so sánh v1 | v2 tên `light-relic-mirror-451d.jpg`; nếu không ghi được thư mục review thì để ở `/private/tmp/typing-game-451d/`.

## Ràng buộc
Không sửa code, không làm video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh. Không dùng ảnh của game khác.

## Giao nộp
`docs/codex-queue/451d-report.md`, gồm danh sách ảnh.
