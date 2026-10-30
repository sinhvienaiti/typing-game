# Phiếu 224 · Wordwoven · Kiểm lại độc lập 170 + 208 (kit tiếng Anh, `deploy:pack` 0 lỗi, nguồn portal lúc build) trên `td-codex` chưa commit

**Nguồn:**
- `docs/codex-queue/208-report.md`: "**Phần 170 vẫn chưa commit khi bắt đầu.**" và "Hoàn tất phần mã và kiểm được giao: production **69 → 0 lỗi** … Chờ Claude duyệt rồi commit."
- `docs/games/MAP1_PRODUCTION.md` §2.1, cổng G7 của Lời Gọi: "Từ vựng đọc từ repo cha qua nginx; origin cha ghi cứng; dist mang 19,8 MB GLB không dùng". Phiếu 170 và 208 sửa phần này. Claude đang dừng việc riêng (chủ dự án 30/10, khoảng 11:15), nên hai phiếu chưa ai duyệt.
- `tools/codex-run/README.md`, bảng "Chọn model": kiểm lại độc lập, phản biện dùng `gpt-6.1-sol` mức `xhigh`.

**Không trùng:**
- 170 và 208 là phiếu làm. Phiếu này chỉ đọc, chạy lại trong bản chép và báo; **không sửa gì**.
- 187 (Dragonhold) và 207 (Last Line) là việc cùng loại ở game khác; không đụng.
- Phiếu này không thay lượt duyệt, commit của Claude, cũng không thay bước kiểm G7 trên server và trình duyệt.

**Báo cáo:** `docs/codex-queue/224-report.md` (tiếng Việt) và thư mục `docs/codex-queue/224/` (JSON, Markdown, log, script; không ảnh, không chép `dist`). Cả hai ở repo cha.

## Chỉ chạy khi

Chạy từ gốc repo cha, trước mọi bước ghi; lưu lệnh và đầu ra vào `224/preflight.txt`:
1. `git -C games/.wt-td-codex branch --show-current` ra `td-codex`; `git -C games/.wt-td-codex rev-parse HEAD` ra `f9abfd09987dadd519233c2f38692758d35cefca`.
2. `git -C games/.wt-td-codex --no-optional-locks status --short -uall | diff - docs/codex-queue/208/status-final.txt` rỗng. Đó là 28 đường: 19 của 170, 12 của 208, 3 dùng chung (208-report §1).
3. Có đủ: `docs/codex-queue/208/208-only.patch`, `208/before/package.json`, `208/before/README.md`, `208/before/tests/deploy-pack.test.ts`, `208/dist-final.json`, `208/after.json`, `208/status-final.txt`, `208/run.py`, `docs/codex-queue/170/dist-inventory.json`, `170-td-pack-and-kit.md`, `168-ts-pack-and-kit.md`, `208-td-deploy-pack.md`, `170-report.md`.
4. `games/typing-defense/tmp/codex-224/` chưa có.
   - Có, và `docs/codex-queue/224/` cho thấy đó là lượt trước của chính phiếu này bị cắt: xóa thư mục đó, làm lại từ đầu.
   - Có mà không rõ của ai: dừng.
5. `node -v` từ 24 trở lên, `pnpm -v` ra `11.21.0`, có `/usr/bin/rsync` và `/usr/bin/patch`.

Sai một điều: dừng. Chỉ ghi báo cáo nêu điều nào sai, kèm đầu ra thật.

## Luật chung (phiếu kiểm lại)

- **Nơi làm:** làn s9, cwd là repo cha (`.`).
  - Worktree `games/.wt-td-codex` (nhánh `td-codex`) **chỉ đọc**.
  - Mọi lệnh `pnpm` chạy trong bản chép `games/typing-defense/tmp/codex-224/tree` (hay `tree-170` ở Việc 3), không bao giờ trong worktree.
  - Phiếu này **cho phép** chạy build và bộ test của Wordwoven, nhưng chỉ trong bản chép. Điều này ghi đè dòng "do not run the games' builds or test suites" của phần luật chung do runner chèn.
- **Git chỉ đọc:** `status`, `diff`, `show`, `ls-files`, `rev-parse`, `cat-file`, `log`.
  - `status` luôn kèm `--no-optional-locks` để không ghi index.
  - Không dùng `git apply`; tách patch bằng `/usr/bin/patch` (Việc 3).
- **Không sửa lỗi tìm thấy.** Chỉ ghi phát hiện và cách sửa đề xuất. Claude sửa sau khi đọc báo cáo.
- Phiếu không thêm chữ người chơi thấy, không làm ảnh hay âm.

**Chỉ được ghi:**
- `games/typing-defense/tmp/codex-224/`: bản chép `tree/`, bản nguồn `tree-170/`, `tmpdir/`, file mốc `marker`. `tmp/` có trong `.gitignore` của game. Xóa hết ở Việc 9.
- `docs/codex-queue/224-report.md` và `docs/codex-queue/224/`.

**Cấm:**
- Ghi bất cứ gì trong `games/.wt-td-codex`, kể cả `node_modules/`, `dist/`, `tmp/`. Chạy `pnpm` hay `node` với cwd là worktree đó.
- `pnpm install`, `pnpm add`, `kit:sync`, `media:pull`. Chạy `pnpm` mà thiếu biến `pnpm_config_verify_deps_before_run=false` (xem "Dựng bản chép").
- Mọi lệnh git có ghi: commit, add, stash, checkout, reset, apply, worktree, clean.
- Worktree khác: `.wt-td-1c`, `.wt-td-keys`, `.wt-td-ui`, `.wt-td-scenery`, `.wt-td-vfx`, `.wt-play-typing-defense`. Checkout chính `games/typing-defense`: chỉ ghi trong `tmp/codex-224/`; đọc `src/kit/README.md` ở Việc 4 được.
- Dev server, trình duyệt, mạng.
- Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*`).
- Sửa phiếu 168, 170, 208, báo cáo và thư mục của chúng, `docs/CODEX_QUEUE.md`, file làn.

## Dựng bản chép (làm sau Việc 1)

Claude thử trước trên một bản chép ở thư mục tạm (30/10, 12:54) và gặp hai bẫy:
- **pnpm 11 kiểm phụ thuộc trước mỗi `pnpm run` và tự gọi `pnpm install`.**
  - Khi cả `node_modules` là một symlink tới worktree, lệnh dừng ngay: `ERR_PNPM_UNSAFE_MODULES_DIR … Refusing to remove the modules directory`.
  - Biến `pnpm_config_verify_deps_before_run=false` tắt bước này. Biến `npm_config_…` không có tác dụng.
  - Biến được kế thừa sang các `pnpm` con: `check` gọi `pnpm test` và `pnpm build`; `tests/deploy-pack.test.ts:43` gọi `pnpm run`.
- **Vite và Vitest ghi vào `node_modules`.**
  - Vite ghi file cấu hình tạm vào `node_modules/.vite-temp/`; Vitest ghi `node_modules/.vite/vitest/…/results.json`.
  - Nếu cả `node_modules` là symlink thì các file đó rơi vào worktree.
  - Vì vậy `node_modules` của bản chép là **thư mục thật**. Mỗi mục bên trong là symlink tuyệt đối tới mục cùng tên của worktree, trừ `.vite`, `.vite-temp` và `.pnpm-workspace-state-v1.json`.

Làm như vậy thì `pnpm check` xanh trong bản chép, và `find games/.wt-td-codex -newer <marker>` không ra dòng nào.

Lệnh, chạy từ gốc repo cha:

```sh
WT="$PWD/games/.wt-td-codex"; C="$PWD/games/typing-defense/tmp/codex-224"
mkdir -p "$C/tree" "$C/tree-170" "$C/tmpdir" && touch "$C/marker"
git -C "$WT" ls-files -co --exclude-standard -z | /usr/bin/rsync -a --from0 --files-from=- "$WT/" "$C/tree/"
git -C "$WT" ls-files -co --exclude-standard -z | /usr/bin/rsync -a --from0 --files-from=- "$WT/" "$C/tree-170/"
/usr/bin/rsync -a "$WT/public/" "$C/tree/public/"
/usr/bin/rsync -a "$WT/public/" "$C/tree-170/public/"
for d in tree tree-170; do
  mkdir "$C/$d/node_modules"
  for e in $(ls -A "$WT/node_modules"); do
    case "$e" in .vite|.vite-temp|.pnpm-workspace-state-v1.json) ;; *) ln -s "$WT/node_modules/$e" "$C/$d/node_modules/$e" ;; esac
  done
done
```

Mỗi lệnh `pnpm` (thay `<script>`; `tree` hay `tree-170`):

```sh
C="$PWD/games/typing-defense/tmp/codex-224"
cd "$C/tree" && env -u VITE_PORTAL_URL pnpm_config_verify_deps_before_run=false TMPDIR="$C/tmpdir" pnpm <script>
```

Khi cần đặt `VITE_PORTAL_URL`, thay `-u VITE_PORTAL_URL` bằng `VITE_PORTAL_URL=<giá trị>` trong cùng lệnh `env`.

Số lúc viết phiếu:
- `ls-files -co --exclude-standard` ra **328** đường, trong đó 9 file dưới `public/`.
- Chép đủ `public/` thêm 1 file bị `.gitignore` bỏ qua: `public/assets/typing-defense/ui/title-dusk.webp`. Tổng **329** file ngoài `node_modules`.
- `node_modules/` của worktree có 14 mục; mỗi bản chép có **11** symlink.

## Việc

1. **Mốc đầu** `224/before.json`, trước khi chép:
   - nhánh, HEAD, `status --short -uall`;
   - đường, byte và SHA-256 của 329 file: 328 đường của `ls-files -co --exclude-standard` cộng mọi file dưới `public/`;
   - SHA-256 của 34 file `src/kit/**`, `tests/golden/td-1a.json`, `tests/golden/td-1b-boss.json`, `public/assets/typing-defense/models/manifest.json`; so với `docs/codex-queue/208/after.json` (37 hash);
   - mục cấp 1 của `node_modules/` (tên, loại, mtime) và mtime của mọi `node_modules/.vite/vitest/*/results.json`;
   - `ls games/typing-defense/tmp` (để so ở Kiểm 10).
2. **Bản chép** như mục trên. Lưu `224/copy.json`: manifest SHA-256 của `tree/` (trừ `node_modules`) so với mốc đầu; số file; danh sách symlink trong `tree/node_modules`.
3. **Tách phần 170 và phần 208.**
   - `/usr/bin/patch -R -p1 -E -d "$C/tree-170" < docs/codex-queue/208/208-only.patch`. Ghi mã thoát và đầu ra vào `224/split.log`.
   - Kỳ vọng:
     - mã 0, 12 file được vá, không còn `*.rej` hay `*.orig`;
     - 7 file mới của 208 bị xóa;
     - `src/app/learning.ts` và `vite.config.ts` bằng byte `git -C games/.wt-td-codex show HEAD:<đường>`;
     - `package.json`, `README.md`, `tests/deploy-pack.test.ts` bằng byte `docs/codex-queue/208/before/<đường>`;
     - so mọi file nguồn của `tree-170` với `HEAD`: đúng **19** đường khác (14 sửa, 5 mới), trùng "Nhóm 170" của 208-report §1. Không tính `node_modules/` và file bị `.gitignore` bỏ qua `public/assets/typing-defense/ui/title-dusk.webp` (không có trong `HEAD`, nên nếu tính sẽ thành đường thứ 20).
   - Chạy trong `tree-170`: `pnpm check`, rồi `pnpm deploy:pack`, rồi `node src/kit/tools/deploy/check-pack.mjs dist --game typing-defense --json > /Users/toandx/htdocs/typing-game/docs/codex-queue/224/pack-170.json`. Inventory `dist` (đường, byte, SHA-256) vào `224/dist-170.json`; so từng file với `docs/codex-queue/170/dist-inventory.json` (khóa `entries`).
   - Kỳ vọng của trạng thái 170 (170-report §3–4):
     - 37 file / 380 test xanh, kit 33/33;
     - `deploy:pack` mã 1 với 69 lỗi theo trường `code`: 1 `local-host` ở `assets/learn-*.js`, 68 `missing-model`;
     - 55 file;
     - 54 file trùng SHA-256 với inventory 170. Chỉ `.vite/manifest.json` khác, vì nó chứa đường tương đối từ bản chép tới `node_modules` thật (dài hơn).
     - Số byte chênh tùy chỗ đặt bản chép: file đó có 60 đường `node_modules/…`, mỗi đường dài thêm đúng phần tiền tố tương đối.
       - Lượt thử của Claude (bản chép trong scratchpad, tiền tố `../../../../../../../../Users/toandx/htdocs/typing-game/games/.wt-td-codex/`, 75 ký tự): 1.209.837 byte so với 1.205.337, chênh 4.500 = 60 × 75.
       - Ở `games/typing-defense/tmp/codex-224/tree-170` tiền tố là `../../../../.wt-td-codex/` (25 ký tự): kỳ vọng chênh **1.500** byte, tổng **1.206.837** byte, `.vite/manifest.json` **16.655** byte (170: 15.155). Ghi số đo thật; khác số này thì giải thích bằng tiền tố thật trong file.
   - Lưu `224/paths.json`: mỗi đường trong 28 đường gắn `170`, `208` hay `cả hai`, kèm số dòng thêm và bớt.
   - Đường nào không thuộc hai nhóm, hay patch không áp sạch: phát hiện P1.
4. **Đọc diff và tìm lỗi.**
   - Đối chiếu từng mục "Việc", "Cấm", "Kiểm" của `docs/codex-queue/170-td-pack-and-kit.md` (và phần "Kiểm" của `168-ts-pack-and-kit.md` mà 170 dẫn), cùng `208-td-deploy-pack.md`, với diff thật. Mỗi mục ghi: đạt, thiếu hay sai, kèm `file:dòng`.
   - Đọc kỹ những chỗ sau. Đường tính từ worktree; số dòng lúc viết phiếu.
   - `src/app/portal.ts:2–11`, hàm `portalHome`:
     - chuỗi trống hay chỉ có khoảng trắng; khoảng trắng hai đầu và ở giữa;
     - `user@`, `:pass@`, `@` trống;
     - giao thức `javascript:`, `data:`, `file:`, `ftp:`, `ws:`; URL tương đối;
     - URL có cổng, query, fragment;
     - production có nên nhận `http:` không.
   - `src/app/learning.ts:8–33`: `standaloneHost`, `createPortalBridge`, singleton lười `learningBridge()`. Đọc cùng kit:
     - `src/kit/learning/bridge.ts:115` (nguồn mặc định), `:122` (xả hàng đợi khi bị nhúng), `:149` (`flushQueue`), `:177` (`requestFocus`), `:248` (lọc nguồn tin đến), `:292` (`postMessage`);
     - `src/kit/learning/contract.ts:22` (`PARENT_ORIGIN`).
   - Câu hỏi cho phần cầu học:
     - Biến trống mà bị nhúng: có tin nào ra ngoài không, hàng đợi có mất không?
     - Có biến: chỉ đúng một nguồn được gửi và nhận?
     - Cầu học còn nằm ở chunk Học không (`docs/td/BUILD_1B.md` §20, `tests/td-chunks.test.ts`)?
   - `vite.config.ts:30–55`: `replacePortalOrigin` và plugin `wordwoven-portal-origin`.
     - Chỉ thay ở `src/kit/learning/contract.ts`; 0 hay 2 khai báo làm build dừng.
     - Điều gì xảy ra khi `id` của Vite có query (`?v=`, `?import`), khác hoa thường, hay là đường thật qua symlink? Khi file không bao giờ qua `transform`: build có báo lỗi không, hay gói lặng lẽ mang nguồn mặc định?
     - Dòng kết thúc CRLF.
     - Plugin cũng chạy lúc `pnpm dev`; `loadEnv` đọc cả `.env*` của game.
     - Vẫn giữ export `LAZY`, `chunkOf`, `manualChunks` và chuỗi `port: 3006`.
   - `scripts/deploy/prune.mjs`:
     - không bao giờ xóa ngoài `dist` được truyền;
     - từ chối symlink ở mọi cấp (`:7–14`, `:36–39`, `:48–50`), kể cả symlink nằm sâu dưới `models/` hay `.vite/`;
     - `modelPath` (`:16–30`) với `%2e%2e`, `\`, `?`, `#`, URL tuyệt đối;
     - mọi kiểm xong trước lần ghi hay xóa đầu tiên (`:68`);
     - khóa trùng, phần tử không phải chuỗi, manifest không có `models`;
     - dòng thông báo (`:86`).
   - `deploy-models.json` (`{ "models": [] }`): script đọc nó từ cạnh script (`:42`), không từ cwd. README của game có nói đúng như vậy không?
   - **Kit:**
     - 31 file module bằng byte `git show 1b1fe6cfacdc81a55d13af202da0f42023455313:shared/game-kit/<đường>` (repo cha, chỉ đọc);
     - `src/kit/README.md` do `scripts/sync-game-kit.mjs` sinh (dòng 125, 246), so byte với `games/typing-defense/src/kit/README.md`;
     - `src/kit/verify-kit.mjs` so byte với export `VERIFY_SOURCE` của `scripts/sync-game-kit.mjs` (dòng 135). `import` script đó không chạy `main`: `main` chỉ chạy khi gọi trực tiếp;
     - `src/kit/kit-manifest.json` ghi `parentCommit` đó và `parentDirty: true`;
     - ghi số file khớp và khác.
   - **Tên file chơi thử:**
     - `src/app/retry.ts:71` tải `wordwoven-playtest-s<seed>-n<ngày>-<tick>.json`;
     - `scripts/td/b9.ts:5–6,14` nhận cả `loi-goi-choi-thu-*`;
     - `docs/td/PLAYTEST_1B.md:32,58`, `docs/td/BUILD_1B.md:547`;
     - còn chỗ nào trong `src/`, `scripts/`, `tests/`, `docs/td/` (trừ changelog cũ) nhắc tên cũ như tên hiện hành không.
   - **Test mới và test sửa:** `tests/portal.test.ts`, `portal-build.test.ts`, `deploy-prune.test.ts`, `deploy-pack.test.ts`, `td-b9.test.ts`, `td-flow.test.ts`.
     - Test khẳng định hành vi thật (Vite thật, tiến trình `prune.mjs` và `check-pack.mjs` thật) hay chỉ khẳng định mock?
     - Fixture trong `tmp/` có tự xóa cả khi test đỏ không?
     - Timeout 20 s 170 đặt cho test CLI có che lỗi treo không?
5. **Chạy lại trong `tree/`.** Mỗi lệnh lưu log và `{lệnh, env, mã thoát, giây}` vào `224/`.
   1. `pnpm check`, biến `VITE_PORTAL_URL` vắng.
   2. `pnpm td:golden:check`.
   3. **Production, biến vắng:** `pnpm deploy:pack`. Rồi `node src/kit/tools/deploy/check-pack.mjs dist --game typing-defense --json` vào `224/pack-absent.json`. Inventory `dist` (đường, byte, SHA-256) vào `224/dist-absent.json`.
   4. **Production, biến trống** như `docs/codex-queue/208/run.py:17` (`VITE_PORTAL_URL=''`): `pnpm deploy:pack`. JSON vào `224/pack-empty.json`, inventory vào `224/dist-empty.json`; so từng file với `docs/codex-queue/208/dist-final.json`.
   5. **Demo nhà:** `VITE_PORTAL_URL=https://typing-game.local/`, `pnpm deploy:pack:local`. JSON chế độ local (thêm `--allow-local-host`) vào `224/pack-local.json`. Rồi chạy bộ kiểm chế độ production trên chính `dist` đó, vào `224/pack-local-production.json`.
   6. **Quét gói** sau mỗi gói 3, 4, 5, vào `224/scan.json`. Trên mọi file HTML, JS, CSS, JSON, `.webmanifest`, `.txt` trong `dist`:
      - số chuỗi `typing-game.local` theo từng file;
      - mọi tiền tố `/assets/<tên>/` khác nhau và số lần gặp;
      - số file `.glb`, `.gltf`, `.bin`;
      - có `dist/.vite/` hay `dist/assets/typing-defense/models/` không.
   - Test thời gian đỏ khi máy bận: chạy riêng file đó ba lần (`pnpm exec vitest run tests/<file>`, cùng biến môi trường), ghi số.
   - **Số Claude thấy ở lượt thử** (để so; không phải bằng chứng, Codex tự đo):
     - `pnpm check`: 40 file / 414 test xanh, `src/kit OK: 33 files`;
     - golden: hai ván `same: true`, 19.660 và 5.695 tick;
     - gói 3: 0 lỗi, 53 file / 1.167.486 byte;
     - gói 4: 53/53 SHA-256 trùng `208/dist-final.json`, 1.167.750 byte;
     - gói 5: 0 lỗi; cả ba gói chỉ có tiền tố `/assets/typing-defense/`.
   - **Hai chỗ khác 208 đã rõ nguyên nhân.** Không ghi là lỗi, trừ khi đo ra khác mô tả:
     - Gói 3 nhỏ hơn gói 208 264 byte, chỉ ở `assets/learn-*.js` (8.273 so với 8.537 byte). Biến vắng thì `portalHome(undefined)` được gập thành hằng; 208 build với chuỗi trống. Vì thế ngân sách `/?title=0` là 81,16 kB thay vì 81,30 kB.
     - Dòng `Pruned 2 files, … bytes` lớn hơn 38.123 của 208. `dist/.vite/manifest.json` chứa đường tương đối từ bản chép tới `node_modules` thật của worktree. File đó bị xóa trước bước kiểm gói. Lượt thử của Claude ở scratchpad ra 42.623 (thêm 60 × 75); ở `tmp/codex-224/tree` kỳ vọng **39.623** (thêm 60 × 25), như mục tách 170 ở Việc 3.
6. **Đột biến**, sau khi đã lưu số của Việc 5. Chỉ sửa trong `tree/`.
   - Mỗi lần: sửa một file, chạy file test nêu, chép lại file gốc từ worktree, kiểm SHA-256 bằng mốc.
   - **M1** `vite.config.ts:31–35`: `replacePortalOrigin` trả `code` không thay. `tests/portal-build.test.ts` phải đỏ.
   - **M2** `src/app/learning.ts:23`: luôn dùng `host: options.host`. `tests/portal.test.ts` phải đỏ.
   - **M3** `scripts/deploy/prune.mjs:85`: bỏ dòng xóa `.vite`. `tests/deploy-prune.test.ts` hay `tests/deploy-pack.test.ts` phải đỏ.
   - **M4** `src/app/retry.ts:71`: tên tải về trở lại `loi-goi-choi-thu-`. `tests/td-b9.test.ts` phải đỏ.
   - Được thêm tối đa 4 đột biến nữa ở chỗ Việc 4 thấy test hở. Ghi mỗi cái: sửa gì, file test, số đỏ và xanh.
   - Lưu `224/mutations.json`. Đột biến nào vẫn xanh: phát hiện P2 "test không bắt".
   - Lượt thử của Claude: M1 3 đỏ, M2 1 đỏ, M3 5 đỏ trên hai file, M4 1 đỏ.
   - Cuối cùng manifest `tree/` phải bằng mốc đầu.
7. **Bảng đối chiếu** `224/claims.json`, chép vào báo cáo. Một dòng cho mỗi kiểm bắt buộc:
   - của 170: mọi dòng số ở bảng §3 và §4 của 170-report (37 file / 380 test, kit 33/33, golden 6/6, sim ≤ 2 ms, ngân sách 79,60 / 81,07 kB, `git diff --check`, 69 lỗi production, 68 lỗi local, 55 file / 1.205.337 byte);
   - của 208: tám mục "Kiểm" (bảng §3 của 208-report).
   - Cột: phiếu, kiểm, số phiếu báo, số đo lại, khớp hay không, giải thích, bằng chứng.
   - Chênh từ 37/380 lên 40/414: giải thích bằng số file và số test của 208 đếm từ log.
   - `git -C games/.wt-td-codex diff --check` (chỉ đọc): mã thoát.
8. **Phát hiện.** Bảng, mỗi dòng:
   - mức: **P0** chặn commit; **P1** phải sửa trước khi nhận G7; **P2** nên sửa; **P3** ghi chú;
   - `file:dòng`;
   - kịch bản hỏng cụ thể (đầu vào → kết quả sai);
   - cách sửa đề xuất và test nên thêm.

   Thêm một mục **"Cần trình duyệt của Claude"**: những gì chỉ kiểm được khi chạy thật. Ví dụ:
   - nhúng trong portal nhà với `VITE_PORTAL_URL=https://typing-game.local/`: phím đầu tới game, sự kiện học tới portal;
   - mở riêng, không portal: hàng đợi học giữ nguyên;
   - gói production trên server tĩnh: không request tới host khác.
9. **Dọn.**
   - Khi log ở `224/` đã đủ và Kiểm 1 đã chạy: `rm -rf games/typing-defense/tmp/codex-224`. Thư mục do chính phiếu tạo và không có ảnh chụp, nên không cần `tools/capture-prune`.
   - Kiểm thư mục đã mất.

## Kiểm (ghi số)

1. **Worktree nguyên:**
   - `status --short -uall` trước và sau đều bằng `208/status-final.txt`;
   - 329 SHA-256 trước và sau bằng nhau; HEAD `f9abfd09987dadd519233c2f38692758d35cefca`;
   - `find games/.wt-td-codex -newer games/typing-defense/tmp/codex-224/marker -not -path '*/.git/*' | wc -l` ra 0 (chạy trước Việc 9);
   - mục cấp 1 của `node_modules/` và mtime các `results.json` không đổi.
2. **Bản chép bằng worktree:** 329/329 SHA-256 trùng; 11 symlink trong mỗi `node_modules` của bản chép.
3. **`pnpm check`** trong `tree/`:
   - số file và test xanh, đỏ, so với 40/414;
   - dòng `src/kit OK: n files`, so với 33;
   - `tsc` và `vite build` qua; hai dòng ngân sách trang.
4. **`td:golden:check`:** 2/2 `same: true`, số tick từng ván.
5. **Gói:**
   - mỗi gói: mã thoát, số lỗi theo `code` (kỳ vọng 0), số file và byte;
   - biến vắng: 53 file; biến trống: 53 file / 1.167.750 byte, 53/53 SHA-256 trùng `208/dist-final.json`;
   - cả hai gói production: 0 chuỗi `typing-game.local`, 0 `.glb`, không `.vite/`, không `models/`;
   - demo nhà: mã 0, 0 lỗi. Bộ kiểm production trên gói demo: đúng 1 lỗi `local-host`;
   - tiền tố `/assets/<tên>/` của game khác (`space-typing`, `dragon-hold`, `typing-survival`, `immortality-cultivation`…): 0.
6. **Tách 170/208:** mã `patch`, 12 file; 19 đường 170; 3 file chung trùng `208/before/`. Trạng thái 170: 37/380, 69 lỗi (1 + 68), 55 file, 54/55 SHA-256 trùng inventory 170; byte tổng và chênh ở `.vite/manifest.json` (kỳ vọng 1.206.837 và 1.500, xem Việc 3).
7. **Kit:** 31/31 file module trùng commit `1b1fe6cf`; `README.md` và `verify-kit.mjs` trùng bản sinh; `verify-kit` 33/33.
8. **Đột biến:** 4/4 đỏ khi sửa, xanh khi trả lại (cùng các đột biến thêm nếu có).
9. **Phát hiện:** đếm theo mức P0–P3, mỗi cái có `file:dòng`.
10. **Dọn và phạm vi:**
    - `games/typing-defense/tmp/codex-224` không còn; `ls games/typing-defense/tmp` bằng lúc đầu. Thư mục của phiếu khác xuất hiện hay mất trong lúc chạy (ví dụ `codex-226` của phiếu 226, cùng làn hay làn khác) thì liệt kê riêng, không đụng, không tính là lỗi của phiếu này;
    - `git --no-optional-locks status --porcelain -uall` của repo cha trước và sau: dòng mới do phiếu này chỉ là `docs/codex-queue/224-report.md` và `docs/codex-queue/224/…`;
    - dòng mới khác (làn s7, s8 chạy cùng lúc) liệt kê riêng, không đụng.

## Báo cáo

`docs/codex-queue/224-report.md`, tiếng Việt, có số:
- **Kết luận đầu tiên**, một trong ba: commit được ngay; commit được sau khi sửa các P0–P1 nêu; không nên commit (vì sao).
- Preflight; mốc đầu; bản chép; tách 170/208 và trạng thái 170.
- Đối chiếu "Việc", "Cấm", "Kiểm" của 170 và 208 (bảng).
- Bảng đối chiếu số (Việc 7); bảng gói và quét; kit; đột biến.
- Bảng phát hiện theo mức; mục "Cần trình duyệt của Claude".
- Dọn và phạm vi (Kiểm 1, 10).
- Mục **"Việc của Claude"**: thứ tự duyệt và commit đề xuất (170 rồi 208, theo `208/208-only.patch`); sửa nào làm trước khi commit; bước nào cần trình duyệt.

Script đã dùng lưu ở `224/`, chạy lại được từ gốc repo cha.

**Xong khi:** chín việc và mười mục kiểm có số; worktree nguyên; bản chép đã xóa; có báo cáo.

**Làn:** s9, sau 221. Model `gpt-6.1-sol`, mức `xhigh` (kiểm lại độc lập). Dòng làn:
`224-td-pack-recheck | docs/codex-queue/224-td-pack-recheck.md | . | xhigh | workspace-write | gpt-6.1-sol`
