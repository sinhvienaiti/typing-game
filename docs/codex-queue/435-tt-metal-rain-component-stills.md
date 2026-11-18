# Phiếu 435: Ảnh thành phần cho Kim mưa kiếm (nguồn để làm video Firefly và decal)


Phản biện: PASS (Sonnet, 17/11)
## Bối cảnh
Owner 17/11 chọn "Video Firefly ghép mảnh nhỏ" cho Kim mưa kiếm vì bản dựng bằng code chỉ ~5/10 (`typing-game-review/owner-review/2026-11-17/tu-tien/metal-sword-rain-r3.jpg`). Luật thành phần (owner 12/11): mỗi ảnh/clip chỉ một thành phần, code đặt, nhân bản và định thời. Phân cảnh đích: `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg` (nửa trái).

## Việc
Dùng công cụ `image_gen`: **2 mẫu trước** (thành phần a và b), ghép `metal-rain-comp-samples-435.jpg`, dừng và ghi báo cáo để Claude gửi owner; chỉ khi được giao tiếp mới làm c. Tổng tối đa 6 lần. 1024×1024 trên nền đen tuyệt đối, một thành phần giữa khung, lề ≥ 12 %, lưu `games/immortality-cultivation/art-src/concept/ult-metal/rain-components/<tên>.v1-try<k>.png`, prompt thật trong `.prompt.txt`.
Ảnh tham chiếu bắt buộc mọi lần (ghi đường dẫn): phân cảnh Kim ở trên (nửa trái: ánh vàng, chất kim loại, trận pháp), thanh kiếm đã duyệt `games/immortality-cultivation/art-src/concept/ult-metal/tripo-src/ult-metal-sword.v1-try1.png`.
- **a. `sword-fall-streak`:** một thanh kiếm tu tiên rơi thẳng đứng mũi hướng xuống, nhìn hơi chéo từ trên xuống, kèm vệt sáng vàng dài mờ dần phía trên (như khung 2 phân cảnh); phát sáng dịu, vệt mềm có nhiều sợi sáng, không đường thẳng cứng như kim.
- **b. `formation-sky`:** vòng trận pháp vàng nằm ngang nhìn chéo từ dưới lên hoặc từ trên chéo xuống (bầu dục đúng phối cảnh), nhiều lớp vòng, phù văn cổ, tia sáng rủ xuống mềm từ viền (như khung 1 phân cảnh); không người, không quái.
- **c. `ground-cracks-gold`:** vết nứt nhỏ phát sáng vàng trên đá, nhìn chéo ~55°, nền đen, nứt toả ra từ một điểm; lề rộng.
Phong cách game tu tiên thương mại cao cấp, chân thật. Không chữ, không watermark.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
`docs/codex-queue/435-report.md`.
