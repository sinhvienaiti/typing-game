# Phiếu 102 · Kit · Cổng DevTools không trùng khi nhiều làn chạy song song

**Nguồn:** lô Codex 1 của bản kiểm kê map 1 (`docs/games/map1/CODEX_BATCH.md`, phiếu 102). Phiếu 100 của lô (từ vựng Rồng) là phiếu **094** trong hàng; mọi chỗ ghi "phiếu 100" ở đây đã đổi thành 094.

**Báo cáo:** `docs/codex-queue/102-report.md`.

## Luật chung (phiếu mã)

- **cwd:** repo cha `/Users/toandx/htdocs/typing-game` (để ghi báo cáo). Mã nằm trong worktree nêu ở từng phiếu; mọi đường dẫn mã tính từ worktree đó.
- **Được dùng git chỉ đọc:** `show`, `log`, `diff`, `status`, `ls-tree`. **Cấm** mọi lệnh git có ghi (`add`, `commit`, `checkout`, `reset`, `stash`, `worktree`…).
- **Cấm:**
  - sửa `src/kit/**` của game (bản chép từ kit, có kiểm sha256);
  - sửa file golden hay chạy lệnh cập nhật golden (`dh:golden:update`, `td:golden:update`…);
  - ghi vào cây chính của game (`games/<id>`), worktree khác, game khác; đụng Tu Tiên;
  - sửa file ở repo cha (nginx, `scripts/`, `shared/`), trừ khi phiếu cho phép;
  - dev server, trình duyệt (sandbox không mở được cổng); media (ảnh, âm, GLB).
- **Cách làm:** test trước, mã sau. Chú thích trong mã bằng tiếng Anh, ngắn. Chuỗi người chơi thấy: câu tiếng Việt, danh từ game tiếng Anh (`docs/games/NAMES_EN.md`).
- **Mỗi phiếu có changelog** `docs/changelog/2026-10-29-<tên>.md` trong worktree, tiếng Việt: làm gì, vì sao, số đo.
- **Báo cáo** `docs/codex-queue/<số>-report.md` và thư mục `docs/codex-queue/<số>/` (log, số đo): file đã đổi; đầu ra của từng mục Kiểm, có số; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chạy lại kiểm, đọc diff, kiểm trên trình duyệt ở 1280 và 1920 khi phiếu đụng giao diện, rồi commit trên nhánh của worktree và gộp.

## Phiếu

**Vì sao:** kiểm kê map 1 (A11, P1, cổng G1). `cdp-run.mjs` chọn cổng DevTools ngẫu nhiên `9300 + random * 600`. Ngày 28/10, ba làn trình duyệt chạy song song đã trùng cổng: script của làn Rồng điều khiển Chrome của lượt Lời Gọi 1920 sang trang Rồng ở giây 171. Bằng chứng hỏng mà không báo gì.

**Nơi làm:** repo cha, thư mục `shared/game-kit/tools/`. (Claude có thể cho chạy trong một worktree repo cha sạch như phiếu 037; khi đó mọi đường dưới đây tính từ worktree đó.)

**Chỉ được ghi:**
- `shared/game-kit/tools/cdp-run.mjs`;
- `shared/game-kit/tools/cdp-port.mjs` (mới);
- `shared/game-kit/tools/cdp-port.test.ts` (mới);
- `shared/game-kit/DRIFT.md` (thêm một mục ngắn: sửa gì so với bản nguồn của Space);
- `docs/codex-queue/102-report.md`, `docs/codex-queue/102/`.

**Cấm thêm:** sửa bản chép trong game (`games/*/src/kit/tools/cdp-run.mjs`, `games/dragon-hold/scripts/visual/cdp-run.mjs`, `games/space-typing/scripts/visual/cdp-run.mjs`); chạy Chrome; chạy `kit:sync`. Phần đó Claude làm sau.

**Việc:**
1. **`cdp-port.mjs`**, hai hàm thuần, chú thích tiếng Anh:
   - `portArg(env)`: nếu `env.CDP_PORT` có giá trị thì phải là số nguyên 1024–65535, trả `{ arg: "--remote-debugging-port=<N>", fixed: N }`; giá trị sai thì ném lỗi nêu giá trị. Không có thì trả `{ arg: "--remote-debugging-port=0", fixed: null }`.
   - `readActivePort(profileDir, { timeoutMs = 10000, pollMs = 50, readFile, now, sleep })`: đọc `<profileDir>/DevToolsActivePort`, lấy dòng đầu làm cổng. Chưa có file thì chờ và đọc lại tới hết giờ. Hết giờ thì ném lỗi có đường file. Dòng đầu không phải số nguyên 1–65535 thì ném lỗi ngay. `readFile`, `now`, `sleep` truyền vào được để test không phải chờ thật.
2. **`cdp-run.mjs`:** bỏ `Math.random`. Dùng `portArg(process.env)` khi mở Chrome. Nếu `fixed` là `null` thì lấy cổng bằng `readActivePort(profile)` (thư mục profile đã là `mkdtempSync` riêng mỗi lượt) trước khi nối tới `/json/version`. Giữ nguyên mọi hành vi khác và mọi cờ Chrome.
3. **`cdp-port.test.ts`** (vitest của kit, `shared/game-kit/vitest.config.ts`):
   - file có `"9222\n/devtools/browser/abc"` thì ra 9222;
   - file chưa có ở hai lần đọc đầu, có ở lần ba thì ra đúng cổng, và số lần gọi `sleep` khớp;
   - file không bao giờ có thì ném lỗi có đường file khi hết giờ (đồng hồ giả, không chờ thật);
   - dòng đầu là `abc`, `0`, `70000` thì ném lỗi;
   - `CDP_PORT=9555` ra `fixed: 9555`; `CDP_PORT=abc`, `CDP_PORT=80` ném lỗi; không có `CDP_PORT` ra cổng 0.

**Kiểm (bắt buộc):**
1. `pnpm --dir shared/game-kit test` xanh; ghi số test trước và sau.
2. `pnpm --dir shared/game-kit typecheck` sạch.
3. `node --check shared/game-kit/tools/cdp-run.mjs` đạt.
4. `grep -n "Math.random\|9300" shared/game-kit/tools/cdp-run.mjs`: rỗng.
5. **Đột biến:** bỏ bước đọc lại khi chưa có file; bỏ kiểm khoảng của `CDP_PORT`. Mỗi đột biến phải làm test đỏ; xong thì trả lại.
6. `git status --short -- shared/game-kit`: chỉ các file trong "Chỉ được ghi".

**Xong khi:** sáu mục đạt. Sau đó Claude: `kit:sync` vào bốn game, sửa tay bản riêng của Rồng và Space, rồi chạy 3 lượt song song × 20 lần: 0 lượt trùng cổng.
