# Phiếu 168 · Last Line · Theo kit tiếng Anh, lệnh `deploy:pack`

**Nguồn:** chủ dự án 29/10: Codex còn nhiều hạn mức, giao thêm việc. Kit cha vừa sang tiếng Anh (phiếu 154) và có bộ kiểm gói deploy (111, 111b); cổng G7 của map 1 (`docs/games/MAP1_PRODUCTION.md`) cần mỗi game đóng gói tự đủ (`docs/games/DEPLOY_INDEPENDENCE.md` §11).

**Báo cáo:** `docs/codex-queue/168-report.md`.

## Luật chung (phiếu mã)

- **Nơi làm:** worktree `games/.wt-ts-codex` (nhánh `ts-codex`), cwd của phiếu. Worktree bắt đầu với **một lượt đồng bộ kit chưa commit của Claude** (`src/kit/**`, từ kit cha `1b1fe6cf`: kit đã sang tiếng Anh ở phiếu 154, có bộ kiểm gói `src/kit/tools/deploy/check-pack.mjs` của phiếu 111/111b). Lượt đồng bộ đó là một phần diff của phiếu này; **không sửa gì trong `src/kit/**`**.
- Được dùng git chỉ đọc. **Cấm** mọi lệnh git có ghi.
- **Cấm:** sửa kit cha `shared/game-kit`; chạy `kit:sync`; dev server, trình duyệt; mạng; đụng game khác, worktree khác, Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*`); media vào Git.
- Test trước, mã sau. Chú thích tiếng Anh, ngắn. Chữ người chơi thấy là tiếng Anh (luật 28/10 trong `AGENTS.md`); tiếng Việt chỉ ở nghĩa từ.
- Ván vàng (golden) không đổi; luật chơi không đổi.
- **Báo cáo:** `docs/codex-queue/168-report.md` (repo cha) và thư mục `docs/codex-queue/168/`, tiếng Việt, ghi số.

## Việc

1. **Theo kit mới:** kit nay mặc định tiếng Anh (`PERFECT`, `ADVICE_EN`). Bỏ phần đè tiếng Anh của game nếu kit đã cho cùng kết quả (`src/app/english.ts` lời khuyên; nhãn PERFECT ghi đè trong view). Chữ người chơi thấy không được đổi; test so chữ giữ xanh.
2. **`deploy:pack`:** thêm script `deploy:pack` = `pnpm build` rồi `node src/kit/tools/deploy/check-pack.mjs dist --game typing-survival`, và `deploy:pack:local` thêm `--allow-local-host` (bản demo nhà). Ghi cách dùng vào README của game (một đoạn ngắn).
3. **Chạy thật** `pnpm deploy:pack`, lưu đầu ra JSON vào `docs/codex-queue/168/`. Mỗi lỗi ghi: thật hay báo nhầm. **Biết trước:** gói còn đường `/assets/space-typing/` (model tàu mượn của Space Typing). Không sửa phần này: hướng B (chủ dự án chọn 29/10) bỏ tàu, model mới do chủ dự án dựng. Ghi danh sách mọi file và chỗ trong mã trỏ sang Space để làn sau thay.

**Kiểm:** `pnpm check` xanh (kể cả `verify-kit`); test thời gian đỏ khi máy tải nặng thì chạy riêng ba lần, ghi số; `git status --short -uall`: chỉ `src/kit/**` của lượt đồng bộ, các file của mục 1–2, test, README, `docs/changelog/<ngày>-pack-and-kit.md`.
