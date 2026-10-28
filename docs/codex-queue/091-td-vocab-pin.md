# Phiếu 091 · Lời Gọi · Bản chép từ vựng ghim trong repo game (cổng G7)

**Vì sao:** cổng production G7 của map 1 đòi build tự đủ, không đọc file của repo cha. Hôm nay Lời Gọi chỉ có từ vựng nhờ alias nginx hay plugin dev trỏ tới `shared/` của repo cha. Bản đứng riêng rơi về khoảng 150 từ dự phòng, và `pnpm test` hỏng 9 test ở bản clone riêng (ENOENT `shared/vocabulary`). Thiết kế: `docs/games/DEPLOY_INDEPENDENCE.md` §4 dòng 1–3, §8.

**Báo cáo:** `docs/codex-queue/091-report.md`.

## Nơi làm

- **cwd:** repo cha `/Users/toandx/htdocs/typing-game` (để ghi báo cáo).
- **Mã:** worktree `games/.wt-td-codex` (nhánh `td-codex`, tách từ `a2-days` `a5cc147`; `node_modules` đã cài). Mọi đường dẫn mã dưới đây tính từ worktree này.

**Chỉ được ghi:**
- `games/.wt-td-codex/public/vocabulary/**` (file mới);
- `games/.wt-td-codex/vocab.config.json` (mới);
- `games/.wt-td-codex/tests/vocab-pin.test.ts` (mới);
- `games/.wt-td-codex/tests/td/typing.ts`, `scripts/td/replay.ts`, `vite.config.ts`;
- `games/.wt-td-codex/docs/changelog/2026-10-28-vocab-pin.md` (mới, tiếng Việt);
- `docs/codex-queue/091-report.md`, `docs/codex-queue/091/` (log, số đo).

**Cấm:**
- mọi lệnh git có ghi (`add`, `commit`, `checkout`, `reset`, `stash`…). Được dùng lệnh git chỉ đọc: `show`, `log`, `diff`, `status`;
- sửa `src/kit/**` (chép từ kit, `verify-kit` kiểm sha256);
- sửa `src/**`, kể cả `src/app/vocab.ts`: trang vẫn tải `/vocabulary/` như cũ, Vite tự phục vụ `public/`;
- sửa file golden (`tests/golden/**`) hay chạy `td:golden:update`;
- sửa file ở repo cha (nginx, `scripts/`, `shared/`): phần đó Claude làm sau;
- ghi vào `games/typing-defense` (cây chính), `games/.wt-td-vfx`, `games/.wt-play-typing-defense`, game khác; đụng Tu Tiên;
- dev server, trình duyệt; media (ảnh, âm, GLB).

## Việc

1. **Số trước:** trong worktree chạy `pnpm test` và `pnpm td:golden:check`; ghi số test đạt và đầu ra vào `docs/codex-queue/091/before.txt` (đường tuyệt đối).
2. **Chép bản ghim.** `pin` = `18338405eebd9cfdbd6d6bf666ea79361c00a564` (commit cuối của repo cha có sửa `shared/vocabulary`, 27/10). Với mỗi file `index.json`, `levels/001.json` … `levels/005.json`, `ATTRIBUTION.md` (7 file; 5 level vì `VOCAB_LEVELS = 5` ở `src/app/vocab.ts`):
   - `git -C /Users/toandx/htdocs/typing-game show <pin>:shared/vocabulary/<file> > games/.wt-td-codex/public/vocabulary/<file>`;
   - không đọc từ cây làm việc của `shared/`.
3. **`vocab.config.json`** ở gốc worktree: `{ "pin": "<pin đủ 40 ký tự>", "files": [ bảy đường ở trên, theo thứ tự đó ] }`.
4. **`public/vocabulary/vocab-manifest.json`:** `{ "pin": "<pin>", "version": <giá trị "version" của index.json>, "files": { "<đường>": "<sha256 hex>" } }`. Khóa xếp theo thứ tự chữ; JSON thụt 2 dấu cách, có xuống dòng cuối file.
5. **Test và replay đọc bản chép:**
   - `tests/td/typing.ts` dòng 23: `new URL("../../public/vocabulary/levels/…", import.meta.url)`; sửa chú thích đầu file (dòng 2–3) cho đúng;
   - `scripts/td/replay.ts` dòng 31: `new URL("../../public/vocabulary/levels/…", import.meta.url)`; sửa câu chú thích dòng 7 ("rebuilt from the pinned copy in public/vocabulary");
   - không đổi gì khác.
6. **Bỏ plugin dev** trong `vite.config.ts`: Lời Gọi không cần mount nào (không gọi `/typing-texts/`, không dùng model của Space). Bỏ dòng `plugins: [serveSharedFolders(…)]`, chú thích của nó, và import `serveSharedFolders`. Bỏ cả `join`, `root` nếu không còn ai dùng; còn dùng thì giữ.
7. **Test mới `tests/vocab-pin.test.ts`** (vitest, chỉ đọc file trong repo game):
   - bảy file của `vocab.config.json` có trong `public/vocabulary/`, và sha256 từng file khớp `vocab-manifest.json`;
   - `pin` của manifest bằng `pin` của config; `version` của manifest bằng `version` của `index.json`;
   - mọi level 1 … `VOCAB_LEVELS` (import từ `src/app/vocab.ts`) có file;
   - không còn file nào trong `src/`, `tests/`, `scripts/` chứa chuỗi `shared/vocabulary` ở dạng đường dẫn đọc file. Được phép trong chú thích của `src/kit/**`.
8. **Changelog** `docs/changelog/2026-10-28-vocab-pin.md`: làm gì, vì sao (G7), cách cập nhật bản ghim (chạy lại bước 2–4 với pin mới), số đo.

## Kiểm (bắt buộc, ghi đầu ra vào báo cáo)

1. `pnpm check` trong worktree: xanh. Ghi số test đạt trước và sau; sau = trước + số ca của `vocab-pin.test.ts`.
2. `pnpm td:golden:check`: đạt như trước, và `git -C games/.wt-td-codex diff --stat -- tests/golden` rỗng.
3. **Đứng riêng:** chép worktree (trừ `node_modules`) sang một thư mục tạm **ngoài** repo cha, ví dụ `$TMPDIR/td-091-alone/game`, để `../../shared` không còn. Ở đó:
   - `ln -s` thư mục `node_modules` của worktree vào;
   - `pnpm test` xanh (hôm nay hỏng 9 test ở đây);
   - `pnpm build` xong, và `dist/vocabulary/` có đủ bảy file cộng `vocab-manifest.json`, cùng sha256.
   Xóa thư mục tạm sau khi ghi số.
4. **Đột biến (mỗi cái chạy `pnpm vitest run tests/vocab-pin.test.ts`, phải đỏ; xong thì trả lại):**
   - đổi một byte của `public/vocabulary/levels/004.json`;
   - xóa dòng `ATTRIBUTION.md` khỏi manifest;
   - đổi `pin` trong config.
5. `grep -rn "shared/vocabulary" src tests scripts vite.config.ts` trong worktree: chỉ còn chú thích trong `src/kit/**`. Dán đầu ra.
6. `git -C games/.wt-td-codex status --short`: chỉ có các file trong "Chỉ được ghi". Dán đầu ra.

## Báo cáo `docs/codex-queue/091-report.md`

Tiếng Việt: file đã đổi và mới; đầu ra của sáu mục Kiểm, có số; chỗ nào phải làm khác phiếu và vì sao.

**Xong khi:** sáu mục Kiểm đạt. Claude chạy lại, duyệt diff, rồi commit trên `td-codex` và gộp vào `a2-days`.
