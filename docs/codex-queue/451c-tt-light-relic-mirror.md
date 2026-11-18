# Phiếu 451c: Bảo kính chiêu Ánh Sáng, vẽ lại cho sang (3 mẫu để owner chọn)

Phản biện: PASS (Sonnet, 18/11; vòng 1 thiếu nối liền các phần, đã sửa)

## Bối cảnh
Owner 18/11 xem hai mẫu thấu kính B1 và B2 của phiếu 451b và chê: "nhìn cả 2 đều chưa đạt, nhìn vẫn xấu và nhìn kém sang".

Claude thấy lỗi ở chỗ:
- Hai mẫu có dáng kính lúp cầm tay (một vòng tròn với một cán), nên trông như đồ dùng thường ngày.
- Chỉ có một lớp vành, hoa văn nhỏ và lặp lại.
- Không có chỗ nào làm điểm nhấn.

Hướng mới là một bảo kính tiên hiệp: pháp bảo lơ lửng, không có cán, gồm nhiều lớp vòng.

Ảnh này sẽ thay vật thể đang dựng bằng khối hình học trong code (`docs/work/tasks/vfx-code-drawn-audit.md`, mục Q3). Sau khi owner chọn, ảnh được dùng làm nguồn cho Tripo.

## Việc
Dùng công cụ `image_gen`, tối đa 3 lần (3 mẫu).

Ảnh tham chiếu, chỉ dùng ảnh của dự án và ghi đường dẫn vào mỗi prompt:
- `games/immortality-cultivation/art-src/concept/ult-light/ult-light-moment-a.v1-try1.png`: chỉ mượn bảng màu và độ bóng kim loại; không chép cảnh, hào quang hay tia sáng của ảnh này.
- `games/immortality-cultivation/art-src/lab/vfx/light/stills/light-ray-a2.v1-try2.png`: tông vàng hổ phách của tia sáng owner đã chọn.

Yêu cầu chung cho cả ba mẫu:
- Kích thước 1024×1024, nền xám trơn, ánh sáng đều, không bóng đổ.
- Góc nhìn 3/4 từ trước, vật nằm trọn trong khung, lề ≥ 8 %.
- Bảo kính tròn, không cán, gồm 2–3 vòng đồng tâm có độ dày, có chi tiết chạm nổi tinh xảo.
- Mặt kính là đá hổ phách đặc, có vân sáng bên trong, không trong suốt.
- Một điểm nhấn rõ, ví dụ viên ngọc lớn hoặc ấn phù ở tâm hay ở đỉnh.
- Cao cấp, sang trọng, cuốn hút như pháp bảo trong game tu tiên thương mại hàng đầu.
- Không hào quang, không tia sáng, không chữ, không watermark, không vật rời bay quanh.
- Khối đặc, liền nhau, để Tripo dựng được: mọi vòng, cánh sen và đế phải nối thật với nhau bằng chốt, thanh nối hoặc chạm liền khối; không phần nào lơ lửng tách rời.

Ba mẫu khác nhau về chất liệu và dáng:
- **A, Nhật Luân Kính:** vàng ròng chạm phượng hoàng ôm quanh vành, cánh phượng xoè thành vòng ngoài, viên hồng ngọc ở đỉnh.
- **B, Liên Hoa Kính:** nhiều lớp cánh sen bằng vàng và ngà xếp vòng quanh mặt kính, viền ngọc trai, đài sen bên dưới làm đế.
- **C, Thái Cực Kính:** hai vòng vàng và bạc lồng nhau lệch trục như hồn thiên nghi, khắc chữ triện cổ dạng hoa văn (không đọc được), viên ngọc bích ở tâm.

Lưu ở `games/immortality-cultivation/art-src/lab/vfx/light/stills/light-relic-mirror-<a|b|c>.v1-try1.png`, mỗi ảnh kèm `.prompt.txt`. Ghép thành một tờ `light-relic-mirror-451c.jpg`; nếu không ghi được thư mục review thì để ở `/private/tmp/typing-game-451c/`.

## Ràng buộc
Không sửa code, không làm video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh. Không dùng ảnh của game khác.

## Giao nộp
`docs/codex-queue/451c-report.md`, gồm danh sách ảnh.
