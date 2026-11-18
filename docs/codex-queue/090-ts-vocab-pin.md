# Phiếu 090 · Tuyến Cuối · Bản chép từ vựng ghim trong repo game (cổng G7)

**Vì sao:** kiểm kê map 1 ngày 28/10 (TS-M1-02, P0, cổng G7: build production tự đủ). Hôm nay từ vựng chỉ có nhờ alias nginx hay plugin dev trỏ tới `shared/` của repo cha. Bản build đứng riêng rơi về "Từ dự phòng" (khoảng 60 từ, hash bộ bài `28a73ed5` thay vì `7f073fa2`). Test, bot và replay cũng đọc `../../../../shared`. Thiết kế: `docs/games/DEPLOY_INDEPENDENCE.md` §5 dòng 4 và 6, §8 (bản chép ghim, chỉ phần dùng).

**Báo cáo:** `docs/codex-queue/090-report.md`.

## Nơi làm

- **cwd:** repo cha `/Users/toandx/htdocs/typing-game` (để ghi báo cáo).
- **Mã:** worktree `games/.wt-ts-codex` (nhánh `ts-codex`, tách từ `main` `bf0e6f9`; `node_modules` đã cài). Mọi đường dẫn mã dưới đây tính từ worktree này.

**Chỉ được ghi:**
- `games/.wt-ts-codex/public/vocabulary/**` (file mới);
- `games/.wt-ts-codex/vocab.config.json` (mới);
- `games/.wt-ts-codex/tests/vocab-pin.test.ts` (mới);
- `games/.wt-ts-codex/tests/survival/typist-bot.ts`, `tests/survival/bot.ts`, `scripts/replay.ts`, `vite.config.ts`;
- `games/.wt-ts-codex/docs/changelog/2026-10-28-vocab-pin.md` (mới, tiếng Việt);
- `games/.wt-ts-codex/dist/` và cache trong `node_modules/` (Git bỏ qua, do `pnpm build`, `pnpm check` ghi);
- `$TMPDIR/ts-090-alone/**` (bản chép tạm của Kiểm 3);
- `docs/codex-queue/090-report.md`, `docs/codex-queue/090/` (log, số đo).

**Cấm:**
- mọi lệnh git có ghi (`add`, `commit`, `checkout`, `reset`, `stash`…). Được dùng lệnh git chỉ đọc: `show`, `log`, `diff`, `status`;
- sửa `src/kit/**` (chép từ kit, `pnpm check` kiểm sha256);
- sửa `src/**` ngoài danh sách trên, kể cả `src/app/vocab.ts`: trang vẫn tải `/vocabulary/` như cũ, Vite tự phục vụ `public/`;
- sửa file ở repo cha (nginx, `scripts/`, `shared/`): phần đó Claude làm sau;
- ghi vào `games/typing-survival` (cây chính), `games/.wt-ts-vfx`, game khác; đụng Tu Tiên;
- dev server, trình duyệt; media (ảnh, âm, GLB).

## Việc

1. **Số trước.** Trong worktree, chạy và lưu vào `docs/codex-queue/090/`:
   - `node --import tsx scripts/chapter-hashes.ts > docs/codex-queue/090/chapter-before.txt` (đường ra tính từ repo cha; dùng đường tuyệt đối);
   - `pnpm test` (ghi số test đạt).
2. **Chép bản ghim.** `pin` = `18338405eebd9cfdbd6d6bf666ea79361c00a564` (commit cuối của repo cha có sửa `shared/vocabulary`, 27/10). Với mỗi file `index.json`, `levels/001.json`, `levels/002.json`, `levels/003.json`, `ATTRIBUTION.md`:
   - `git -C /Users/toandx/htdocs/typing-game show <pin>:shared/vocabulary/<file> > games/.wt-ts-codex/public/vocabulary/<file>`;
   - không đọc từ cây làm việc của `shared/`.
3. **`vocab.config.json`** ở gốc worktree: `{ "pin": "<pin đủ 40 ký tự>", "files": [ năm đường ở trên, theo thứ tự đó ] }`.
4. **`public/vocabulary/vocab-manifest.json`:** `{ "pin": "<pin>", "version": <giá trị "version" của index.json>, "files": { "<đường>": "<sha256 hex>" } }`. Khóa ngoài theo thứ tự `pin`, `version`, `files`. Khóa của `files` xếp theo thứ tự mã ký tự, nên `ATTRIBUTION.md` đứng đầu. JSON thụt 2 dấu cách, có xuống dòng cuối file.
5. **Test, bot, replay đọc bản chép:**
   - `tests/survival/typist-bot.ts` dòng 275 và `tests/survival/bot.ts` dòng 49: `new URL("../../public/vocabulary/levels/…", import.meta.url)`;
   - `scripts/replay.ts` dòng 34: `new URL("../public/vocabulary/levels/…", import.meta.url)`; sửa câu chú thích dòng 8 cho đúng ("rebuilt from the pinned copy in public/vocabulary");
   - không đổi gì khác trong các hàm đó.
6. **Bỏ mount từ vựng của plugin dev**, giữ mount model của Space (việc model là TS-M1-01, Claude làm sau). Trong `vite.config.ts`:
   - truyền `routes: {}` cho `serveSharedFolders`;
   - bỏ hằng `sharedRoot` và biến môi trường `SHARED_DIR`;
   - sửa chú thích cho đúng: từ vựng nay là `public/vocabulary/`, bản ghim theo `vocab.config.json`.
7. **Test mới `tests/vocab-pin.test.ts`** (vitest, chỉ đọc file trong repo game):
   - năm file của `vocab.config.json` có trong `public/vocabulary/`, và sha256 từng file khớp `vocab-manifest.json`;
   - `pin` của manifest bằng `pin` của config; `version` của manifest bằng `version` của `index.json`;
   - mọi level mà trang hỏi (1, 2, 3; xem `loadVocab` trong `src/app/vocab.ts`) có file: lấy trường `file` của level n trong `index.json` (như `loadRawVocabularyLevel` của kit) và kiểm file đó có trong `public/vocabulary/`;
   - `deckHash(buildDeck([level 1, 2, 3]))` bằng `"7f073fa2"` (`deckHash` từ `src/app/vocab.ts`, `buildDeck` từ `src/content/deck.ts`);
   - quét mọi file trong `src/` (trừ `src/kit/**`), `tests/`, `scripts/`: không có lần nào chứa chuỗi tìm, kể cả trong chú thích. **Ghép chuỗi tìm từ hai phần** (`"shared" + "/vocabulary"`) để test không tự bắt chính nó.
8. **Changelog** `docs/changelog/2026-10-28-vocab-pin.md`: làm gì, vì sao (G7), cách cập nhật bản ghim (chạy lại bước 2–4 với pin mới), số đo.

## Kiểm (bắt buộc, ghi đầu ra vào báo cáo)

1. `pnpm check` trong worktree: xanh. Ghi số test đạt trước và sau; sau = trước + số ca của `vocab-pin.test.ts`.
2. **Hash vàng không đổi:**
   - chạy lại `chapter-hashes.ts` ra `chapter-after.txt`; `diff` với `chapter-before.txt` rỗng (152 dòng);
   - `tests/s0-trace.test.ts` đạt, và `git -C games/.wt-ts-codex diff --stat -- tests/golden` rỗng.
3. **Đứng riêng:** chép worktree (trừ `node_modules`) sang một thư mục tạm **ngoài** repo cha, ví dụ `$TMPDIR/ts-090-alone/game`, để `../../shared` không còn. Ở đó:
   - `ln -s` thư mục `node_modules` của worktree vào;
   - `pnpm --config.verify-deps-before-run=false test` xanh. Không gọi `pnpm test` trơn: pnpm 11 kiểm dependency, đòi cài lại và dừng với `ERR_PNPM_UNSAFE_MODULES_DIR` vì `node_modules` là symlink. Có thể thay bằng `./node_modules/.bin/vitest run`;
   - `pnpm --config.verify-deps-before-run=false build` xong (hoặc `./node_modules/.bin/tsc --noEmit && ./node_modules/.bin/vite build`), và `dist/vocabulary/` có đủ năm file cộng `vocab-manifest.json`, cùng sha256.
   Ghi số rồi xóa bằng `rm -rf "$TMPDIR/ts-090-alone"`: không có `/` cuối, không xóa riêng `node_modules`. Hôm nay ở bản chép riêng, 5/14 file test hỏng vì ENOENT `…/shared/vocabulary/levels/001.json`; sau phiếu phải 14/14 file đạt và đủ số test.
4. **Đột biến (mỗi cái chạy `pnpm vitest run tests/vocab-pin.test.ts`, phải đỏ; xong thì trả lại):**
   - đổi một byte của `public/vocabulary/levels/002.json`;
   - xóa dòng `ATTRIBUTION.md` khỏi manifest;
   - đổi `pin` trong config.
5. `grep -rn "shared/vocabulary" src tests scripts vite.config.ts` trong worktree: chỉ còn dòng trong `src/kit/**`. Dán đầu ra.
6. `git -C games/.wt-ts-codex status --short -uall`: chỉ có các file trong "Chỉ được ghi". Dán đầu ra.

**Số trước, đã đo ngày 28/10 trên `bf0e6f9`** (để đối chiếu): `pnpm test` 14 file, 142/142; `chapter-hashes.ts` 152 dòng, chạy khoảng 15 s.

## Báo cáo `docs/codex-queue/090-report.md`

Tiếng Việt: file đã đổi và mới; đầu ra của sáu mục Kiểm, có số; chỗ nào phải làm khác phiếu và vì sao.

**Xong khi:** sáu mục Kiểm đạt. Claude chạy lại, duyệt diff, rồi commit trên `ts-codex` và gộp vào `main`.
