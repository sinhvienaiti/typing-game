# Phiếu 208 · Wordwoven · `deploy:pack` 0 lỗi: nguồn cổng game lúc build, danh sách model được đóng gói, bỏ `dist/.vite`

**Nguồn:**
- `docs/games/MAP1_PRODUCTION.md` §2.1, cổng G7 của Wordwoven: "Trượt … origin cha ghi cứng; dist mang 19,8 MB GLB không dùng".
- Cùng tài liệu §2.2, A9: "`deploy.config` bỏ `models` và `.vite` tới khi 1C nạp model, `VITE_PORTAL_ORIGINS`".
- `docs/codex-queue/170-report.md` §5: "Gói production còn đỏ: cần nguồn portal production và bước lọc manifest model thừa theo §11". Bộ kiểm gói báo **69 lỗi**: 1 `local-host` (`src/app/learning.ts:15`), 68 `missing-model` (34 model × 2 bậc).
- Chủ dự án 30/10: "tăng thêm việc cho codex cho tôi".

**Tên biến:** `VITE_PORTAL_URL`, như phiếu 187 (Dragonhold). Không dùng `VITE_PORTAL_ORIGINS` của tài liệu cũ. Ba game phải dùng cùng một tên. Phiếu này là nửa Wordwoven của việc "nguồn cầu học".

**Không trùng:** 170 (chỉ ghi lỗi), 187 (Dragonhold), 105/105b (nút cổng Dragonhold), 111/111b (bộ kiểm gói của kit), 091 (từ vựng ghim).

**Báo cáo:** `docs/codex-queue/208-report.md` (repo cha, tiếng Việt), thư mục `docs/codex-queue/208/`.

## Trước phiếu (việc của Claude)

- Claude duyệt và commit phiếu 170 trong `games/.wt-td-codex`.
- Phần của 170 chưa commit lúc viết phiếu: lượt đồng bộ kit (`src/kit/**`), `package.json`, `README.md`, `src/app/retry.ts`, `scripts/td/b9.ts`, `docs/td/BUILD_1B.md`, `docs/td/PLAYTEST_1B.md`, `tests/td-flow.test.ts`, `tests/td-b9.test.ts`, `tests/deploy-pack.test.ts`, `docs/changelog/2026-10-29-pack-and-kit.md`.
- Lúc bắt đầu mà các file đó vẫn chưa commit: làm tiếp trên chúng, không hoàn tác. Ghi rõ ở đầu báo cáo. Liệt kê file của 170 và file của 208 thành hai nhóm riêng.
- Trước khi sửa một file 170 cũng sửa mà chưa commit (`package.json`, `README.md`, `tests/deploy-pack.test.ts`…), chép nó vào `docs/codex-queue/208/before/` để Claude tách phần của hai phiếu.

## Luật chung (phiếu mã)

- **Nơi làm:** worktree `games/.wt-td-codex`, nhánh `td-codex` (dòng `a2-days`). cwd của làn là repo cha (`.`). Mọi lệnh `pnpm` chạy trong worktree đó. Báo cáo và bằng chứng ghi ở repo cha.
- Kiểm nhánh và `git status --short -uall` trước khi làm. Chỉ được có file của 170 (mục trên). Có file lạ thì dừng, ghi lại.
- Được dùng git chỉ đọc. **Cấm** mọi lệnh git có ghi.
- Test trước, mã sau. Chú thích tiếng Anh, ngắn.
- Phiếu không thêm chữ người chơi thấy. Buộc phải thêm thì là tiếng Anh.
- Ván vàng và luật chơi không đổi.
- **Mẫu, chỉ đọc:** `docs/codex-queue/187-report.md` §2; mã của 187: `src/app/portal.ts`, `vite.config.ts`, `tests/portal-build.test.ts` trong `games/.wt-dh-codex` (hoặc ở `main` Dragonhold nếu đã gộp). Nếu `docs/codex-queue/207-report.md` đã có, đọc thêm để tên hàm và hành vi khớp.

## Đọc trước

- `docs/codex-queue/170-report.md` §4–5 và `170/deploy-findings.json`: đủ 69 phát hiện.
- `src/app/learning.ts`: `createLearningBridge({ gameId })` không truyền `parentOrigin` (dòng 14–15).
- Kit, chỉ đọc: `src/kit/learning/contract.ts:22` (`PARENT_ORIGIN`), `bridge.ts:115,248,292`.
- `public/assets/typing-defense/models/manifest.json`: có trong Git, 34 mục, khóa dạng `<kind>/<id>`. Nhánh `a2-days` không nạp model nào (game là canvas 2D).
- `scripts/bundle-budget.mjs`: đọc `dist/.vite/manifest.json` ngay trong `pnpm build`.
- `docs/games/DEPLOY_INDEPENDENCE.md` §4 (hàng 4 và 6), §9, §11.

## Việc

1. **Mốc đầu**, trước khi sửa mã:
   - chạy `pnpm deploy:pack`;
   - chạy bộ kiểm `--json` trên chính `dist` đó, lưu `208/pack-before.json`;
   - lưu inventory `dist` (số file, byte, SHA-256) vào `208/dist-before.json`;
   - lưu SHA-256 của `src/kit/**`, hai file golden và `public/assets/typing-defense/models/manifest.json` vào `208/before.json`.
2. **Test trước:** viết test của mục 6, chạy, ghi số đỏ và xanh vào `208/tests-before.json`.
3. **Nguồn cổng game lúc build** (cách của 187):
   - Biến Vite `VITE_PORTAL_URL`: URL HTTP(S) tuyệt đối, không thông tin đăng nhập. Sai thì build dừng, báo rõ.
   - Mặc định **trống** ở bản phát hành.
   - Biến trống: cầu học dùng host không có parent. Bị nhúng vẫn giữ hàng đợi học cục bộ. Không gửi tin, không xả hàng đợi. `requestFocus` không làm gì.
   - Có biến: `parentOrigin` là phần nguồn của URL. Chỉ gửi và nhận tin với nguồn đó.
   - `vite.config.ts` thay khai báo `PARENT_ORIGIN` của `src/kit/learning/contract.ts` **trong bộ nhớ biên dịch**, như plugin của 187. Không đúng một khai báo thì build dừng. File kit trên đĩa giữ nguyên byte.
   - Giữ export `LAZY`, `chunkOf`, `manualChunks` và chuỗi `port: 3006` trong `vite.config.ts`. `tests/td-chunks.test.ts` và `tests/boundary.test.ts` đọc chúng.
   - Cầu học vẫn ở chunk Học (`docs/td/BUILD_1B.md` §20). Không kéo nó vào chunk vào game.
   - Wordwoven không có nút "Back to portal". Không thêm.
4. **Danh sách model được đóng gói:**
   - File mới, có trong Git: `deploy-models.json` ở gốc game, dạng `{ "models": [] }`. Mỗi phần tử là một khóa của manifest model (ví dụ `buildings/keep`). Trên `a2-days` danh sách **trống**.
   - Script mới `scripts/deploy/prune.mjs <dist>`, chạy sau build:
     - danh sách trống: xóa cả `<dist>/assets/typing-defense/models/`;
     - có phần tử: giữ file mọi bậc của các khóa đó (đường dẫn từ URL, bỏ `?v=`); xóa mọi file khác dưới `models/`; ghi lại `manifest.json` **trong `dist`** chỉ với các khóa đó, các trường khác giữ nguyên;
     - khóa không có trong manifest, hay URL ra ngoài `models/`: mã 1, nói rõ khóa nào, không xóa gì;
     - không có thư mục `models/`: không làm gì, mã 0;
     - xóa `<dist>/.vite/`;
     - in một dòng: số file và byte đã bỏ, các khóa được giữ.
   - Script chỉ ghi trong thư mục `dist` được truyền. Không đụng `public/`. Thư mục không có `index.html` thì từ chối.
   - `deploy:pack` = `pnpm build && node scripts/deploy/prune.mjs dist && node src/kit/tools/deploy/check-pack.mjs dist --game typing-defense`. `deploy:pack:local` như vậy, thêm `--allow-local-host`.
   - `pnpm build` một mình **không đổi**. Nó vẫn giữ `.vite` cho `bundle-budget.mjs`. Nó vẫn giữ model cho `pnpm check`, cho `build:local` của repo cha (nginx đọc `dist`) và cho nhánh 3D.
5. **Tài liệu:**
   - `README.md` của game: cách dùng `VITE_PORTAL_URL` (bản phát hành để trống; demo nhà: `VITE_PORTAL_URL=https://typing-game.local/ pnpm deploy:pack:local`); `deploy-models.json` là gì; bước lọc chạy ở lệnh nào.
   - Ghi chú cho làn L (Claude, nhánh `td-1c`): ở mốc C13, làn L điền `deploy-models.json` từ `STARTER` và `NIGHT_1` trong `scripts/td/media-budget.mjs` của `td-1c`. Ghi ở README và trong báo cáo. Không mở, không sửa `.wt-td-1c`.
   - `docs/changelog/<ngày>-deploy-pack.md` của game: thay đổi, số trước và sau.
   - Cuối báo cáo, mục "Việc của Claude":
     - `build:td` và `dev:td:app` của repo cha cần `VITE_PORTAL_URL=https://typing-game.local/`, để cổng nhà còn nhận focus và sự kiện học. Ghi đúng dòng lệnh đề xuất.
     - Những chỗ tài liệu còn ghi `VITE_PORTAL_ORIGINS`: `DEPLOY_INDEPENDENCE.md` §9, §11; `MAP1_PRODUCTION.md` §2.2 A9.
6. **Test** (viết ở mục 2, xanh ở đây):
   - Nguồn cổng: biến trống; URL hợp lệ có đường dẫn; URL sai; URL có thông tin đăng nhập; giao thức khác HTTP(S).
   - Cầu học khi biến trống: nhúng bằng host giả vẫn không gửi tin, hàng đợi giữ nguyên.
   - Cầu học khi có biến: `postMessage` tới đúng nguồn; tin từ nguồn khác bị bỏ.
   - Build ở cả hai chế độ, bằng cấu hình Vite thật, đầu ra trong `tmp/` và tự xóa: trống thì không còn `typing-game.local`; có biến thì có đúng nguồn đó. File kit trên đĩa không đổi.
   - Lọc: danh sách trống xóa `models/` và `.vite/`, giữ file khác; danh sách một khóa giữ đúng file của khóa đó, manifest chỉ còn khóa đó; khóa lạ trả mã 1 và không xóa gì; không có `models/` vẫn qua; `public/` của fixture không đổi.
   - `tests/deploy-pack.test.ts`: fixture chép thêm `scripts/deploy/prune.mjs` và `deploy-models.json`. Thêm ca build giả có manifest model trỏ tới GLB thiếu: `deploy:pack` vẫn mã 0, `dist/.vite` không còn.

## Cấm

- Mọi lệnh git có ghi.
- Sửa `src/kit/**`; chạy `kit:sync`; sửa kit cha `shared/game-kit`.
- Sửa hay xóa `public/assets/typing-defense/models/manifest.json` hay media trong `public/`. Lọc chỉ làm trên `dist`.
- Nới bộ kiểm gói, thêm cờ bỏ qua, hay tải model cho đủ để làm xanh.
- Dev server, trình duyệt, mạng, `media:pull`.
- Sửa `package.json` của repo cha, nginx, hay tài liệu repo cha (`docs/games/**`). Claude làm sau, theo mục "Việc của Claude". (`package.json` của game được sửa ở Việc 4.)
- Đụng game khác, worktree khác (nhất là `.wt-td-1c`, `.wt-td-keys`; `.wt-dh-codex` chỉ đọc), Tu Tiên.
- Media vào Git.

## Kiểm (ghi số)

1. `pnpm check` xanh: số file test, số test, số file kit. Test thời gian đỏ khi máy bận thì chạy riêng ba lần.
2. `pnpm td:golden:check`: `same: true` cho cả ván thường và ván boss.
3. Ngân sách trang: `/` ≤ 85 kB gzip, `/?title=0` ≤ 85 kB. Ghi số trước (170: 79,60 và 81,07 kB) và sau.
4. `pnpm deploy:pack`: mã 0, **0 lỗi**. JSON bộ kiểm ở `208/pack-after.json`. Inventory ở `208/dist-after.json`: số file, byte; không còn `assets/typing-defense/models/`, không còn `.vite/`. Quét HTML, JS, CSS, JSON của gói: **0** chuỗi `typing-game.local`.
5. `VITE_PORTAL_URL=https://typing-game.local/ pnpm deploy:pack:local`: mã 0, 0 lỗi; JSON ở `208/pack-local.json`. Chạy bộ kiểm chế độ production trên chính gói demo đó: phải còn 1 lỗi `local-host`. Lưu `208/pack-local-production.json`.
6. Bảng trước và sau: 69 lỗi → 0; số file và byte của gói; mỗi nhóm lỗi hết vì sao.
7. SHA-256 sau của `src/kit/**`, hai file golden, `public/assets/typing-defense/models/manifest.json` khớp `208/before.json`. `git diff --check` mã 0.
8. `git status --short -uall`: chỉ file của phiếu này, cộng file của 170 nếu chưa commit (nhóm riêng). Ghi riêng các dòng `package.json` đã đổi, để Claude gộp với `td-1c` và `td-keys`.

**Xong khi:** gói production 0 lỗi; gói demo có biến đạt; sáu mục việc và tám mục kiểm có số. Claude duyệt rồi commit.
