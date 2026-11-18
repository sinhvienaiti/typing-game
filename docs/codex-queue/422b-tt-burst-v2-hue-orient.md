# Phiếu 422b: Màu lửa `fire-big-burst` và hướng `earth-ring-burst` (tách từ 422 sau 3 vòng phản biện)


Phản biện: PASS (Sonnet, 16/11; tách sau 3 vòng)
## Bối cảnh
Chụp 421 (`typing-game-review/owner-review/2026-11-16/tu-tien/burst-v2/burst-v2-grid.jpg`): `fire-big-burst-v2` ngả đỏ, `earth-ring-burst-v2` dựng đứng thành đĩa gai thay vì nằm theo đất. Mẫu lửa owner đã duyệt: `typing-game-review/owner-review/2026-11-16/tu-tien/burst-samples/fire-impact.v1-try2.sheet.png`. Chạy sau 422 trong làn B; chỉ sửa `games/.wt-ic-lab-all/src/lab/burst-v2.ts`.

## Việc
1. `fire-big-burst-v2`: thêm tint/gradient map trong bảng của `burst-v2.ts` để vùng sáng về cam vàng.
2. `earth-ring-burst-v2`: đặt thẻ nằm theo mặt đất (như decal nghiêng), không billboard đứng.

## Nghiệm thu (Codex tự đo)
- Vùng sáng = các pixel có luma > 0,15 ở khung đỉnh, chụp camera chơi 55°, 1280×720. Hue trung bình (HSV, độ) của vùng sáng `fire-big-burst-v2` nằm trong 25°–45°.
- Mặt đất lab là mặt phẳng y = 0, pháp tuyến (0, 1, 0) trong không gian thế giới. Pháp tuyến thẻ `earth-ring-burst-v2` (trục +Z cục bộ của mesh thẻ quy ra thế giới) lệch ≤ 20° so với (0, 1, 0).
- Kiểm kiểu 0 lỗi; các số đo của 422 không xấu đi. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/422b-report.md`.
