07/11/2026 14:02 · Làn 1 chỉ xử lý #4 R2-2: sửa hai test trượt; blocked chờ Claude chạy toàn bộ Vitest theo “Đạt khi”; chỉ thị trực tiếp cấm chạy bộ test game, không tự mở cổng.
Đã sửa games/.wt-ic-lab-all/src/lab/skills-main.ts: chuyển khối present R2-2 (4 dòng, +4/−4 lượt này) lên trước chargeFill.update; sau cập nhật camera và stage, giữ liền chuỗi charge-fill → ambient → tags → render; không sửa test cũ.
ĐẠT: npx --no-install vitest run tests/lab/ambient-fx.test.ts tests/lab/charge-fill-fx.test.ts tests/lab/five-phase-clip.test.ts --maxWorkers=4 (48/48); npx --no-install tsc --noEmit; node --import tsx tests/lab/thunder-travel-r2-probe.mjs; git diff --check.
Giữ mã R2-2 lượt trước (+177/−1 dòng mã chạy): tp2 tắt giữ B8, lịch release/strike/damage/status giữ nguyên; probe kiểm socket theo camera, atlas/video một thân, tắt từng lớp, tái dùng bộ đệm, AST không cấp phát; trần cấu trúc ≤6 draw thêm, texture ≈42,64 MB cho cả R2, bước này dùng chung texture.
Bỏ qua build, bộ Vitest toàn game, trình duyệt, capture và đo GPU theo ranh giới lượt này; không sửa media/manifest/sim, không tạo ảnh/âm, không commit; chưa xác nhận p95, white-out hay nghiệm thu thị giác.
Claude cần chạy Vitest toàn bộ rồi quay/đo cảnh TP tp2 tắt/bật; mốc R0, R0+1/6 khung, H0, H0+1/6/8/18/33 khung (60 Hz); kiểm tay→trời→đích, pivot chân cột, một instance, sắc tím/chữ rõ, Δp95 ≤1,0 ms, p95 ≤11,5 ms trước #5; đã nhả khóa và dừng.

2026-11-07 14:02 — không có việc: chờ Claude chạy Vitest toàn bộ cho #4, đo và mở cổng #5; #6 và #8 chưa đủ điều kiện.
