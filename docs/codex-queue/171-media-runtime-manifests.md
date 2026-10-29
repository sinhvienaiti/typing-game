# Phiếu 171 · Công cụ media · Đưa các `manifest.json` runtime không nằm trong Git vào kho media

**Nguồn:** làn map Dragonhold 29/10: `games/dragon-hold/public/assets/dragon-hold/ground/manifest.json` và `decals/manifest.json` không vào Git (thư mục `public/assets` bị bỏ qua) mà cũng không lên Drive, vì nhóm `runtime` của `pnpm media:push` chỉ đếm ảnh và model. Máy khác kéo media về thì thiếu hai file này, bản build không có ô đất cho tới khi chạy `pnpm prepare-ground && pnpm prepare-decals`. Chủ dự án 29/10: Codex còn nhiều hạn mức, giao thêm việc.

**Báo cáo:** `docs/codex-queue/171-report.md`, thư mục `docs/codex-queue/171/`.

## Luật chung (phiếu mã)

- **cwd:** repo cha `/Users/toandx/htdocs/typing-game`.
- Được dùng git chỉ đọc. **Cấm** mọi lệnh git có ghi; **cấm chạy `pnpm media:push` hay `media:pull` thật** (chỉ Claude chạy; dùng `--dry-run`, `media:status`, `media:check` không mạng, và test).
- **Chỉ được ghi:** `scripts/media/**` (mã và test), `media/media.config.json`, `docs/MEDIA_STORAGE.md` (một mục ngắn), báo cáo.
- **Cấm:** đụng game, worktree, Tu Tiên; mạng.
- Test trước, mã sau (`pnpm media:test`). Chú thích tiếng Anh, ngắn.

## Việc

1. Đọc `scripts/media/media.mjs`, `media/media.config.json`, `docs/MEDIA_STORAGE.md` để hiểu nhóm `runtime` chọn file thế nào.
2. Cho nhóm `runtime` của mỗi game nhận **mọi file JSON dưới `public/assets/<id>/` mà Git bỏ qua** (dùng `git check-ignore` hay danh sách tracked của repo game để biết file nào không ở Git), trừ file cache và file tạm. File JSON đã nằm trong Git thì không đụng.
3. `media:status --only runtime` phải đếm hai manifest của Dragonhold là "Mới"; `media:push --dry-run --only runtime` liệt kê chúng; md5 của chúng vào `media.md5` khi Claude push thật.
4. Không đổi gì với nhóm `originals` và `private`.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. `pnpm media:test` xanh, ghi số ca trước và sau; có ca đỏ trước khi sửa cho đúng trường hợp JSON bị Git bỏ qua.
2. `pnpm media:status --only runtime` và `pnpm media:push --dry-run --only runtime`: lưu đầu ra vào `171/`, chỉ ra hai manifest của Dragonhold và mọi JSON khác vừa được nhận (ghi danh sách theo game).
3. Không có file nào của nhóm khác đổi trạng thái (so `media:status` trước và sau).
4. `git status --short -uall -- scripts/media media docs/MEDIA_STORAGE.md`: chỉ file được ghi.

**Xong khi:** bốn mục đạt. Claude chạy push thật sau khi duyệt.
