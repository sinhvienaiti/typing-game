# Phiếu 424: Cắt 2 clip dáng rộng (sét, huyết) thành flipbook -v3 và nối vào lab


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Owner 16/11 đồng ý làm lại 3 clip theo dáng rộng. Kết quả Firefly (`typing-game-review/owner-review/2026-11-16/tu-tien/burst-remake/wide/wide-sheets.jpg`): `thunder-impact.v4-try2` (A), `blood-big-burst.v4-try1` (B). Độc trượt, làm cách khác. Lab hiện dùng bản cũ cho hai clip này (phiếu 423).

## Việc
1. Cắt `games/immortality-cultivation/art-src/lab/vfx/thunder/firefly-raw/thunder-impact.v4-try2.mp4` và `.../blood/firefly-raw/blood-big-burst.v4-try1.mp4` thành `<clip>-v3.atlas.png`, `.json`, `.uastc.ktx2` bằng `tools/vfx-flipbook/` như phiếu 419/420 (lưới 8×4, 32 khung, lề ≥ 10 % mọi khung, tail fade, pivot ở điểm chạm đất, giữ phối cảnh 55°). Không ghi đè bản cũ.
2. `games/.wt-ic-lab-all/src/lab/burst-v2.ts`: thêm lại 2 dòng ánh xạ cho `thunder-impact` và `blood-big-burst` với hậu tố "-v3" (bảng đã đọc hậu tố từng dòng sau 423).
3. Cập nhật `docs/games/tu-tien/skills/VFX_LIBRARY.md`.

## Nghiệm thu
- Script đo lề ≥ 10 % mọi khung (PNG) cho 2 bộ -v3; json cùng khoá với atlas cũ; probe: 2 tên nạp đúng -v3, không 404; kiểm kiểu 0 lỗi.
- Ảnh trước/sau 8 khung mỗi clip trong `typing-game-review/captures/tu-tien/burst-v3/` (nếu sandbox chặn, để `/private/tmp` và ghi đường dẫn).
- Chỉ ghi file mới trong `art-src/lab/vfx/{thunder,blood}/`, sửa `burst-v2.ts` và `VFX_LIBRARY.md`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/424-report.md`.
