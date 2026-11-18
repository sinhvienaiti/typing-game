# Phiếu 092 · Tuyến Cuối · Chỉ cài `window.__survival` ở dev hoặc khi có `?debug=1`

Hoàn tất năm mục Kiểm ngày 28/10/2026 trên worktree `games/.wt-ts-codex`. Bản production mặc định không cài handle; bản dev hoặc query có giá trị `debug=1` thì cài. Đối tượng handle giữ nguyên từng byte, gồm tên, thứ tự và nội dung mọi lệnh. Không chạy lệnh Git ghi, dev server hay trình duyệt.

## File mới và đã sửa

Đường dẫn dưới đây tính từ worktree:

- `src/app/dev.ts`: thêm hàm thuần `devHandleWanted(dev: boolean, search: string): boolean` và chú thích tiếng Anh ngắn; trả `dev || new URLSearchParams(search).get("debug") === "1"`.
- `src/app/main.ts`: chỉ thêm tên vào import từ `./dev`, sửa câu chú thích về điều kiện cài và đổi dòng gọi thành `if (devHandleWanted(import.meta.env.DEV, location.search)) installDevHandle({`. Không thụt lề lại đối tượng.
- `tests/dev-handle.test.ts`: mới, đúng chín dòng `it.each`, đủ chín ca của phiếu.
- `docs/changelog/2026-10-28-dev-handle.md`: mới, tiếng Việt.

Repo cha có báo cáo này và bằng chứng trong [092/](092/). Các lệnh kiểm ghi thêm vào `dist/` và cache dependency được Git bỏ qua. [Đối chiếu phạm vi](092/scope-check.txt) xác nhận `main.ts` chỉ có ba chỗ sửa được phép và toàn bộ **13 file bẩn có sẵn của phiếu 090 giữ nguyên từng byte**, so SHA-256 với [bản ghi trước sửa](092/090-before-sha256.json).

## Kiểm 1 · `pnpm check`

Chạy trong worktree trước khi sửa: exit **0**, [log đầy đủ](092/check-before.log):

```text
src/kit OK: 59 files match kit-manifest.json (kit 0.1.0, modules platform, input, vocab, speech, learning, three, tools, feedback, audio, balance)
 Test Files  15 passed (15)
      Tests  147 passed (147)
   Duration  4.47s (transform 1.06s, setup 0ms, collect 6.97s, tests 15.82s, environment 2ms, prepare 943ms)
✓ built in 847ms
```

Sau sửa và sau khôi phục đột biến: exit **0**, [log đầy đủ](092/check-after.log):

```text
src/kit OK: 59 files match kit-manifest.json (kit 0.1.0, modules platform, input, vocab, speech, learning, three, tools, feedback, audio, balance)
 Test Files  16 passed (16)
      Tests  156 passed (156)
   Duration  4.58s (transform 1.04s, setup 0ms, collect 7.12s, tests 16.52s, environment 1ms, prepare 854ms)
✓ built in 869ms
```

**156 = 147 + 9**, từ 15 lên 16 file test. Xác minh kit, typecheck và build đều đạt. Cảnh báo Vite chunk trên 500 kB đã có trước sửa (`BufferGeometryUtils`, 547,18 kB), không làm build hỏng.

## Kiểm 2 · Hash chương không đổi

Chạy `node --import tsx scripts/chapter-hashes.ts` trước và sau sửa: cả hai exit **0**, lần lượt lưu [chapter-before.txt](092/chapter-before.txt) và [chapter-after.txt](092/chapter-after.txt).

```text
152 chapter-before.txt
152 chapter-after.txt
diff -u chapter-before.txt chapter-after.txt: exit 0, đầu ra rỗng (0 byte)
SHA-256 cả hai: ae7e9859269b2aece6a7bacbd946dfa93b9a131aeb68a5f5dbed97830dfe626e
```

[Đầu ra diff](092/chapter.diff), [số đo](092/measurements.json). Không sửa sim, content, kit hay golden.

## Kiểm 3 · Đột biến đỏ, khôi phục xanh

Chỉ đổi giá trị so sánh `"1"` thành `"0"` trong `devHandleWanted`, chạy `pnpm vitest run tests/dev-handle.test.ts`: exit **1**, [log](092/mutation.log):

```text
⎯⎯⎯⎯⎯⎯⎯ Failed Tests 3 ⎯⎯⎯⎯⎯⎯⎯
 Test Files  1 failed (1)
      Tests  3 failed | 6 passed (9)
   Duration  358ms (transform 117ms, setup 0ms, collect 159ms, tests 4ms, environment 0ms, prepare 42ms)
```

Ba ca sai là production với `?debug=1`, `?card=1&debug=1`, `?debug=0`. Khôi phục nguyên byte `dev.ts` trong `finally`, rồi chạy lại cùng lệnh: exit **0**, [log](092/restored.log):

```text
 ✓ tests/dev-handle.test.ts (9 tests) 1ms
 Test Files  1 passed (1)
      Tests  9 passed (9)
   Duration  330ms (transform 105ms, setup 0ms, collect 144ms, tests 1ms, environment 0ms, prepare 32ms)
```

[mutation.json](092/mutation.json) ghi mã thoát, SHA-256 sau phục hồi và xác nhận byte khớp. Các lượt `pnpm check`, hash chương và build sau đó đều chạy với mã đã khôi phục.

## Kiểm 4 · Bản build vẫn chứa handle

`pnpm build`: exit **0**, [log đầy đủ](092/build.log):

```text
transforming...
✓ 148 modules transformed.
(!) Some chunks are larger than 500 kB after minification. Consider:
✓ built in 904ms
```

Sau đó chạy đúng `grep -c "__survival" dist/assets/*.js`: exit **0**, [đầu ra](092/grep-survival.txt):

```text
dist/assets/BufferGeometryUtils-Dnx6px1C.js:0
dist/assets/GLTFLoader-BM60796l.js:0
dist/assets/index-QH-na8l4.js:1
dist/assets/meshopt_decoder.module-BbCP70j-.js:0
```

Có **1 dòng khớp** trong bundle `index-QH-na8l4.js`; các chunk khác là 0. Chuỗi vẫn nằm trong bản build, điều kiện mới kiểm soát lúc cài handle.

## Kiểm 5 · Phạm vi Git

`git -C games/.wt-ts-codex diff --stat`: exit **0**, [log](092/diff-stat.txt):

```text
 scripts/replay.ts            | 4 ++--
 src/app/dev.ts               | 5 +++++
 src/app/main.ts              | 8 ++++----
 tests/survival/bot.ts        | 2 +-
 tests/survival/typist-bot.ts | 2 +-
 vite.config.ts               | 5 ++---
 6 files changed, 15 insertions(+), 11 deletions(-)
```

`git -C games/.wt-ts-codex status --short -uall`: exit **0**, [log](092/status-after.txt):

```text
 M scripts/replay.ts
 M src/app/dev.ts
 M src/app/main.ts
 M tests/survival/bot.ts
 M tests/survival/typist-bot.ts
 M vite.config.ts
?? docs/changelog/2026-10-28-dev-handle.md
?? docs/changelog/2026-10-28-vocab-pin.md
?? public/vocabulary/ATTRIBUTION.md
?? public/vocabulary/index.json
?? public/vocabulary/levels/001.json
?? public/vocabulary/levels/002.json
?? public/vocabulary/levels/003.json
?? public/vocabulary/vocab-manifest.json
?? tests/dev-handle.test.ts
?? tests/vocab-pin.test.ts
?? vocab.config.json
```

Đúng **17 đường dẫn = 13 của phiếu 090 + 4 của phiếu 092**. `diff --stat` chỉ liệt kê các file đã được theo dõi; hai file mới của 092 xuất hiện trong `status`. `git -C games/.wt-ts-codex diff --check`: exit **0**, [đầu ra rỗng](092/diff-check.txt). [Diff mã nguồn](092/source.diff) chỉ có hàm thuần mới và ba chỗ sửa được phép trong `main.ts`.

## Kịch bản trong `scripts/`

Đã đọc nguồn và lần theo import: **16/16 kịch bản chạy trình duyệt** lấy `DEV_URL` trực tiếp hoặc qua `survival-s0-lib.mjs` / `survival-s1-lib.mjs`. `common.mjs:5` đặt `DEV_URL = process.env.URL ?? "http://127.0.0.1:3007/"`. Danh sách, đều dưới `scripts/visual/scenarios/`:

- `survival-feel-guns.mjs`
- `survival-feel-ship.mjs`
- `survival-feel.mjs`
- `survival-s0-balance.mjs`
- `survival-s0-boot.mjs`
- `survival-s0-fight.mjs`
- `survival-s0-frames.mjs`
- `survival-s0-keys.mjs`
- `survival-s0-menu.mjs`
- `survival-s0-perf.mjs`
- `survival-s1-guns.mjs`
- `survival-s1-hazards.mjs`
- `survival-s1-latency.mjs`
- `survival-s1-loadout.mjs`
- `survival-s1-perf.mjs`
- `survival-s1-stage.mjs`

[Đối chiếu kịch bản](092/scripts-audit.txt) ghi đường đi tới `DEV_URL`. Ba file `survival-*-lib.mjs` là thư viện dùng chung, không phải kịch bản có hàm chạy mặc định. Không tìm thấy kịch bản riêng chạy build/preview và đọc `__survival`. `scripts/replay.ts` chỉ nhắc `window.__survival.snapshot()` trong chú thích, rồi đọc JSON đã lưu trong Node.

`URL` có thể được trỏ thủ công sang bản build. Các hàm điều hướng hiện tự ghép `/index.html?...`, nên Claude cần thêm `debug=1` vào **query cuối cùng của trang mở**, không chỉ nối query vào `DEV_URL`. Không sửa bất kỳ kịch bản nào theo phiếu.

## Việc bỏ qua và phần Claude kiểm

Không chạy dev server, trình duyệt, media, build hay test game khác; không ghi vào cây chính Tuyến Cuối, worktree VFX, Tu Tiên hoặc mã ngoài danh sách được phép. Không commit, push, reset, clean hay stash.

Claude kiểm trình duyệt ba trạng thái: dev có handle; bản build mặc định không có; bản build thêm `?debug=1` có handle. Sau đó duyệt diff và commit theo quy trình của chủ repo. Năm mục Kiểm trong phạm vi phiếu đều đạt.
