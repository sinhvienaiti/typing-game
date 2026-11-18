# Phiếu 423: Quay 3 clip về bản cũ trong lab; làm mềm mép dưới 2 clip khói trắng


Phản biện: PASS (Sonnet, 16/11, vòng 2)
## Bối cảnh
Ảnh cận cảnh 17 clip (`typing-game-review/owner-review/2026-11-16/tu-tien/burst-v2/burst-v2-closeups.jpg`): bản -v2 kém bản cũ ở `poison-big-burst`, `blood-big-burst`, `thunder-impact` (co thành một cột mảnh). Hai clip `dark-big-burst-white-v2`, `dark-ground-impact-white-v2` bị cắt thẳng ở mép dưới; `dark-big-burst-white-v2` còn một mảnh rời dưới đám khói. Owner 16/11 đồng ý: giữ bản cũ cho 3 clip (sẽ làm lại trên Firefly), làm mềm mép dưới 2 clip khói.

## Việc
1. `games/.wt-ic-lab-all/src/lab/burst-v2.ts`: bỏ 3 dòng ánh xạ `poison-big-burst`, `blood-big-burst`, `thunder-impact` sang -v2 (lab dùng lại bản cũ). Ngoài 3 dòng này, chỉ đổi 2 dòng khói trắng ở mục 2.
2. Đóng gói lại hai atlas khói trắng thành `-v2b` (không ghi đè `-v2`): đáy mỗi khung mờ dần trong 15–20 % chiều cao dưới cùng (alpha tuyến tính về 0), xoá mảnh rời bên dưới đám khói chính (thành phần liên thông nhỏ hơn 2 % diện tích sáng); cho phép bảng trỏ từng dòng tới hậu tố riêng: `burst-v2.ts` hiện cứng hậu tố "-v2" ở kiểm id (dòng ~44), tên ktx2 (~57) và URL json (~80) — đổi thành đọc hậu tố từ bảng (mặc định "-v2"), rồi đặt 2 dòng khói trắng sang "-v2b"; đóng gói bằng `tools/vfx-flipbook/` (`run.sh`, cấu hình `immortality-cultivation.json`, bước ktx2 trong `tools/vfx-flipbook/ktx2`) như phiếu 414/419; cập nhật `VFX_LIBRARY.md`.

## Nghiệm thu
- Kiểm kiểu 0 lỗi. Script đo cho 2 atlas `-v2b`: ở mọi khung, hàng pixel đáy có alpha ≤ 0,05 và alpha tăng đơn điệu trong dải mờ; không còn thành phần liên thông rời < 2 % diện tích sáng. Probe: 3 tên quay về đúng file cũ.
- Chỉ sửa `games/.wt-ic-lab-all/src/lab/burst-v2.ts`, file mới `-v2b` trong `art-src/lab/vfx/dark/`, `VFX_LIBRARY.md`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/423-report.md`.
