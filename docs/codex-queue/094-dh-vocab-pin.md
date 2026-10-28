# Phiếu 094 · Rồng Giữ Ải · Bản chép từ vựng ghim trong repo game (cổng G7)

**Vì sao:** cổng production G7 của map 1 đòi bản build tự đủ, không đọc file của repo cha. Hôm nay Rồng có từ vựng chỉ nhờ alias nginx hay plugin dev trỏ tới `shared/` của repo cha. Rồng không có bộ từ dự phòng, nên bản đứng riêng có bộ bài 0 chữ và màn không chơi được. Thiết kế: `docs/games/DEPLOY_INDEPENDENCE.md` §3 dòng 1 và 3, §8. Làm cùng mẫu với phiếu 090 (Tuyến Cuối) và 091 (Lời Gọi). Phần báo lỗi khi bộ bài rỗng là việc của Claude, không thuộc phiếu này.

**Báo cáo:** `docs/codex-queue/094-report.md`.

## Nơi làm

- **cwd:** repo cha `/Users/toandx/htdocs/typing-game`.
- **Mã:** worktree `games/.wt-dh-codex` (nhánh `dh-codex`, tách từ `main` 02fe9c7; `node_modules` đã cài). Phiếu 080 có thể đã sửa worktree này trước: **giữ nguyên** thay đổi của 080, không hoàn lại.

**Chỉ được ghi:**
- `games/.wt-dh-codex/public/vocabulary/**` (file mới; **không** ghi vào `public/assets/`, đó là symlink tới media thật);
- `games/.wt-dh-codex/vocab.config.json` (mới);
- `games/.wt-dh-codex/tests/vocab-pin.test.ts` (mới);
- `games/.wt-dh-codex/vite.config.ts`;
- `games/.wt-dh-codex/scripts/balance/deck.ts`: chỉ câu chú thích dòng 2 ("100 words from shared/vocabulary levels 1–3"). Sửa cho đúng nguồn thật của bộ bài bot, đọc mã để biết; không đổi mã;
- `games/.wt-dh-codex/AGENTS.md`: chỉ dòng 130 (hàng `pnpm dev` của bảng Commands): bỏ đoạn "serves `/vocabulary/` and `/typing-texts/` from the parent `shared/`", ghi từ vựng là bản ghim ở `public/vocabulary/`;
- `games/.wt-dh-codex/docs/changelog/2026-10-28-vocab-pin.md` (mới, tiếng Việt);
- `games/.wt-dh-codex/dist/` và cache trong `node_modules/` (Git bỏ qua);
- `$TMPDIR/dh-094-alone/**` (bản chép tạm của Kiểm 3);
- `docs/codex-queue/094-report.md`, `docs/codex-queue/094/`.

**Cấm:**
- mọi lệnh git có ghi. Được dùng `git show`, `git log`, `git diff`, `git status`;
- sửa `src/**` (kể cả `src/kit/**` và `src/app/learning.ts`), `tests/golden/**`;
- sửa file ở repo cha (nginx, `scripts/`, `shared/`);
- ghi vào `games/dragon-hold` (cây chính) hay worktree khác (`.wt-dh-mappilot`, `.wt-dh-vfx`, `.wt-dh-mapcodex`…); đụng game khác, đụng Tu Tiên;
- dev server, trình duyệt; media.

## Việc

1. **Số trước:** trong worktree chạy `pnpm test`; ghi số file và số test đạt vào `docs/codex-queue/094/before.txt` (đường tuyệt đối).
2. **Chép bản ghim.** `pin` = `18338405eebd9cfdbd6d6bf666ea79361c00a564`. File: `index.json`, `levels/001.json` … `levels/100.json`, `ATTRIBUTION.md`, tổng 102 file (Rồng lưu level theo người chơi, cần cả 100 level). Với mỗi file:
   - `git -C /Users/toandx/htdocs/typing-game show <pin>:shared/vocabulary/<file> > games/.wt-dh-codex/public/vocabulary/<file>`;
   - không đọc từ cây làm việc của `shared/`.
3. **`vocab.config.json`** ở gốc worktree: `{ "pin": "<pin đủ 40 ký tự>", "files": [ 102 đường, theo thứ tự: index.json, levels/001.json … levels/100.json, ATTRIBUTION.md ] }`.
4. **`public/vocabulary/vocab-manifest.json`:** `{ "pin": "<pin>", "version": <"version" của index.json>, "files": { "<đường>": "<sha256 hex>" } }`. Khóa ngoài theo thứ tự `pin`, `version`, `files`. Khóa của `files` xếp theo thứ tự mã ký tự, nên `ATTRIBUTION.md` đứng đầu. JSON thụt 2 dấu cách, có xuống dòng cuối file.
5. **Bỏ plugin dev** trong `vite.config.ts`: Rồng không gọi `/typing-texts/` và không dùng model của Space. Bỏ dòng `plugins: [serveSharedFolders({ sharedRoot })]`, hằng `sharedRoot` và chú thích của nó, import `serveSharedFolders`. Bỏ `join`, `fileURLToPath`, `root` nếu không còn ai dùng (đọc cả file trước khi bỏ).
6. **Test mới `tests/vocab-pin.test.ts`** (vitest, chỉ đọc file trong repo game):
   - 102 file của `vocab.config.json` có trong `public/vocabulary/`, và sha256 từng file khớp `vocab-manifest.json`;
   - `pin` của manifest bằng `pin` của config; `version` của manifest bằng `version` của `index.json`;
   - mỗi level trong mảng `levels` của `index.json` (1 … 100) có file theo trường `file` của nó;
   - mỗi level có ít nhất một mục sau `filterVocabularyEntries` (từ `src/kit/vocab`): bộ bài không bao giờ rỗng;
   - quét mọi file trong `src/` (trừ `src/kit/**`), `tests/`, `scripts/`, cùng `vite.config.ts`: không có lần nào chứa chuỗi tìm, kể cả trong chú thích. **Ghép chuỗi tìm từ hai phần** (`"shared" + "/vocabulary"`) để test không tự bắt chính nó.
7. **Changelog** `docs/changelog/2026-10-28-vocab-pin.md`: làm gì, vì sao (G7), cách cập nhật bản ghim, số đo.

## Kiểm (bắt buộc, ghi đầu ra vào báo cáo)

1. `pnpm check` trong worktree: xanh. Số test sau = trước + số ca của `vocab-pin.test.ts`.
2. **Golden không đổi:** `md5 -r tests/golden/*` trước và sau giống hệt; `git -C games/.wt-dh-codex diff --stat -- tests/golden src/sim src/content src/typing` rỗng.
3. **Đứng riêng:** chép worktree (trừ `node_modules`, và **không đi theo** symlink `public/assets`: dùng `rsync -a --exclude node_modules --exclude public/assets`) sang `$TMPDIR/dh-094-alone/game`, ngoài repo cha. Ở đó:
   - `ln -s` thư mục `node_modules` của worktree vào;
   - `pnpm --config.verify-deps-before-run=false test` xanh. Không gọi `pnpm test` trơn: pnpm 11 đòi cài lại và dừng với `ERR_PNPM_UNSAFE_MODULES_DIR` vì `node_modules` là symlink. Có thể thay bằng `./node_modules/.bin/vitest run`;
   - `pnpm --config.verify-deps-before-run=false build` xong, và `dist/vocabulary/` có đủ 102 file cộng `vocab-manifest.json`, cùng sha256.
   Ghi số rồi xóa bằng `rm -rf "$TMPDIR/dh-094-alone"`: không có `/` cuối.
4. **Đột biến** (mỗi cái chạy `pnpm vitest run tests/vocab-pin.test.ts`, phải đỏ; xong thì trả lại): đổi một byte của `public/vocabulary/levels/057.json`; xóa dòng `levels/100.json` khỏi manifest; đổi `pin` trong config.
5. `grep -rn "shared/vocabulary" src tests scripts vite.config.ts` trong worktree: chỉ còn dòng trong `src/kit/**`. Dán đầu ra.
6. `git -C games/.wt-dh-codex status --short -uall`: chỉ có file trong "Chỉ được ghi" (và file của phiếu 080 nếu nó chạy trước). Vì danh sách dài, dán số dòng theo thư mục, cộng các dòng ngoài `public/vocabulary/`.

## Báo cáo `docs/codex-queue/094-report.md`

Tiếng Việt: file đã đổi và mới; đầu ra sáu mục Kiểm, có số; chỗ nào phải làm khác phiếu và vì sao.

**Xong khi:** sáu mục Kiểm đạt. Claude chạy lại, duyệt diff, kiểm trên trình duyệt, rồi commit trên `dh-codex`.
