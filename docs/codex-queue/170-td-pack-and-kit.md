# Phiếu 170 · Wordwoven · Theo kit tiếng Anh, `deploy:pack`, tên file chơi thử tiếng Anh

**Nguồn:** chủ dự án 29/10: Codex còn nhiều hạn mức, giao thêm việc. Kit cha vừa sang tiếng Anh (phiếu 154) và có bộ kiểm gói deploy (111, 111b); cổng G7 của map 1 (`docs/games/MAP1_PRODUCTION.md`) cần mỗi game đóng gói tự đủ (`docs/games/DEPLOY_INDEPENDENCE.md` §11).

**Báo cáo:** `docs/codex-queue/170-report.md`.

## Luật chung (phiếu mã)

- **Nơi làm:** worktree `games/.wt-td-codex` (nhánh `td-codex`), cwd của phiếu. Worktree bắt đầu với **một lượt đồng bộ kit chưa commit của Claude** (`src/kit/**`, từ kit cha `1b1fe6cf`: kit đã sang tiếng Anh ở phiếu 154, có bộ kiểm gói `src/kit/tools/deploy/check-pack.mjs` của phiếu 111/111b). Lượt đồng bộ đó là một phần diff của phiếu này; **không sửa gì trong `src/kit/**`**.
- Được dùng git chỉ đọc. **Cấm** mọi lệnh git có ghi.
- **Cấm:** sửa kit cha `shared/game-kit`; chạy `kit:sync`; dev server, trình duyệt; mạng; đụng game khác, worktree khác, Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*`); media vào Git.
- Test trước, mã sau. Chú thích tiếng Anh, ngắn. Chữ người chơi thấy là tiếng Anh (luật 28/10 trong `AGENTS.md`); tiếng Việt chỉ ở nghĩa từ.
- Ván vàng (golden) không đổi; luật chơi không đổi.
- **Báo cáo:** `docs/codex-queue/170-report.md` (repo cha) và thư mục `docs/codex-queue/170/`, tiếng Việt, ghi số.

## Việc

1. **Theo kit mới:** test đang đỏ: `tests/td-flow.test.ts` (đợi `| Cân bằng | standard |`; kit nay `| Balanced |`). Sửa kỳ vọng theo kit, kể cả chữ "THIẾU SỐ", "ĐẠT" nếu kit đã đổi; không nới test.
2. **`deploy:pack`** như phiếu 168, với `--game typing-defense`.
3. **Tên file chơi thử:** nút "Copy playtest data" tải về `loi-goi-choi-thu-*.json` (`src/app/retry.ts`). Đổi thành `wordwoven-playtest-*.json`. `scripts/td/b9.ts` và mọi script đọc file này nhận **cả hai mẫu tên** (file cũ của người chơi thử vẫn đọc được). Cập nhật tài liệu chơi thử trong `docs/` của game nhắc tên file (chỉ dòng tên file).
4. **Chạy thật** `pnpm deploy:pack`, lưu JSON vào `docs/codex-queue/170/`, ghi mỗi lỗi thật hay nhầm.

**Kiểm:** như phiếu 168, thêm test cho mục 3 (tên mới khi tải; `b9.ts` đọc được tên cũ và mới).
