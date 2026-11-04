# Vòng ngọc Clear Wind: ngọc trắng viền vàng nhạt

**Mục tiêu:** đĩa ngọc trên kiếm giống ảnh đã duyệt `art-src/weapons/clearwind-src3q.v4-try1.png` (ngọc trắng có nét chạm, bóng nhẹ; viền vàng nhạt) ở cả Kim và Hỏa.
**Cách đã chốt:** chunk `RING` trong `sword-material.ts` theo mặt nạ hình học đo lúc nạp (`jadeRingOf`). 259b mở tham số để Claude chỉnh trong lab.
**Nghiệm thu:** Kiểm 8 (0 điểm ảnh khác ngoài mặt nạ khi bloom 0); Kiểm 9 (L ≥ cũ + 0,04, IQR ≤ 0,75); tấm so cho anh.
**Phiếu:** `docs/codex-queue/259-tt-jade-ring-material.md`, `259b-tt-jade-ring-fixes.md`. Worktree `games/.wt-immortality-cultivation-codex` (chưa commit).

## Nhật ký
- 04/11 20:27 · Codex · 259 xong (theo bản phiếu trước lần sửa 20:32).
- 05/11 00:05 · Claude (làn 2) · kiểm trình duyệt: đạt 6, 7, 11; trượt 8 (tràn mép), 9 (Kim tối hơn: 0,825 → 0,808), 10 (đo không phân giải được). Hỏa đã trắng.
- 05/11 00:10 · Claude · gửi anh tấm so (ghi rõ chưa đạt); viết 259b.
