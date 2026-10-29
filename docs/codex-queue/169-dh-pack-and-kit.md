# Phiếu 169 · Dragonhold · Theo kit tiếng Anh, lệnh `deploy:pack`, từ vựng trong bản build

**Nguồn:** chủ dự án 29/10: Codex còn nhiều hạn mức, giao thêm việc. Kit cha vừa sang tiếng Anh (phiếu 154) và có bộ kiểm gói deploy (111, 111b); cổng G7 của map 1 (`docs/games/MAP1_PRODUCTION.md`) cần mỗi game đóng gói tự đủ (`docs/games/DEPLOY_INDEPENDENCE.md` §11).

**Báo cáo:** `docs/codex-queue/169-report.md`.

## Luật chung (phiếu mã)

- **Nơi làm:** worktree `games/.wt-dh-codex` (nhánh `dh-codex`), cwd của phiếu. Worktree bắt đầu với **một lượt đồng bộ kit chưa commit của Claude** (`src/kit/**`, từ kit cha `1b1fe6cf`: kit đã sang tiếng Anh ở phiếu 154, có bộ kiểm gói `src/kit/tools/deploy/check-pack.mjs` của phiếu 111/111b). Lượt đồng bộ đó là một phần diff của phiếu này; **không sửa gì trong `src/kit/**`**.
- Được dùng git chỉ đọc. **Cấm** mọi lệnh git có ghi.
- **Cấm:** sửa kit cha `shared/game-kit`; chạy `kit:sync`; dev server, trình duyệt; mạng; đụng game khác, worktree khác, Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*`); media vào Git.
- Test trước, mã sau. Chú thích tiếng Anh, ngắn. Chữ người chơi thấy là tiếng Anh (luật 28/10 trong `AGENTS.md`); tiếng Việt chỉ ở nghĩa từ.
- Ván vàng (golden) không đổi; luật chơi không đổi.
- **Báo cáo:** `docs/codex-queue/169-report.md` (repo cha) và thư mục `docs/codex-queue/169/`, tiếng Việt, ghi số.

## Việc

1. **Theo kit mới:** hai test đang đỏ vì so chữ Việt cũ của báo cáo dev trong kit: `tests/sim/bot-run.test.ts` (đợi "Vùng cuốn: Cân bằng"; kit nay "Balanced"). Sửa kỳ vọng theo chữ tiếng Anh của kit, không nới test. `tests/ui/tags-bodies.test.ts` là test đo thời gian (1,18 ms so với trần 1 ms khi máy bận): chạy riêng ba lần; xanh thì ghi số, không sửa. Bỏ phần đè `NUMBER_FEEL` (nhãn PERFECT) trong `src/view/fx.ts` nếu kit đã cho cùng kết quả; giữ test nhãn PERFECT.
2. **`deploy:pack`** như phiếu 168, với `--game dragon-hold`.
3. **Từ vựng trong bản build:** làn map ghi "bản build hiện tại không có từ vựng (DH-01)". Kiểm `dist/vocabulary/` sau `pnpm build`: có `index.json`, `vocab-manifest.json`, các level mà manifest liệt kê, `ATTRIBUTION.md`. Thiếu thì sửa đường chép trong build (Vite `publicDir` hay script chép) cho đủ, có test.
4. **Chạy thật** `pnpm deploy:pack`, lưu JSON vào `docs/codex-queue/169/`, ghi mỗi lỗi thật hay nhầm; lỗi thật trong phạm vi phiếu thì sửa.

**Kiểm:** như phiếu 168.
