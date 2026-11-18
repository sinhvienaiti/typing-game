# Phiếu 236 · Admin: một Admin nhiều khu (Typing Feel, giai đoạn G5)

**Nguồn:**
- Thiết kế đã duyệt: `docs/games/TYPING_FEEL_SERVICE.md`. Chủ dự án duyệt cả 17 quyết định ngày 31/10, đúng theo đề xuất. Đọc kỹ:
  - §3.1 (Admin hôm nay);
  - §3.2 (cấu trúc mới);
  - §3.3, phần "Server không còn phụ thuộc Space";
  - §3.13 (quyền);
  - §9, dòng G5;
  - §10, câu 10 (tên và điều hướng) và câu 17 (Typing Content thành Learning Content ở All games).
- Chủ dự án 30/10: "về trang quản trị, chúng ta đã có sẵn rồi, bạn chỉ cần dựa vào nó, xử lý lại để gom các setting chung và cấu trúc lại nó cho phù hợp". Vì vậy **không làm Admin mới**: sửa Portal Admin V2.

**Chỉ làm G5.** Không làm G6:
- không làm kho bản sửa Typing Feel;
- không làm Publish, Rollback;
- không làm các trang Keyboard Sounds, Typing Effects, Release & History thật.

Không làm G7 (Format).

**Báo cáo:** `docs/codex-queue/236-report.md` (tiếng Việt) và thư mục `docs/codex-queue/236/`, cả hai **trong worktree**. Model `gpt-6.1-sol`, mức `high`.

## Nơi làm

- **Worktree riêng của repo cha:** `/Users/toandx/htdocs/typing-game-wt/admin-ia`, nhánh `admin-shared-ia`, tách từ `e373829a`. cwd của làn là worktree này. Mọi đường dẫn dưới đây tính từ gốc worktree.
- Lý do làm ở worktree riêng: ở repo chính, Claude đang làm G1 (`typing-feel/`, nginx feel, `validate-play-mode.mjs`) và G2 (`shared/game-kit`). Không mở, không sửa repo chính `/Users/toandx/htdocs/typing-game`.
- `games/space-typing` trong worktree là một worktree tách rời của repo Space ở `84777155`. Nó chỉ có file theo dõi, **không có media runtime**. Chỉ đọc nó.
- `node_modules` đã cài (gốc và `portal/`).
- Phiếu này **cho phép và bắt buộc** chạy build, toàn bộ test và mọi script kiểm nêu ở mục Kiểm. Điều này thắng mọi luật chung kiểu "không chạy build hay toàn bộ test".

## Chỉ chạy khi

1. Worktree ở nhánh `admin-shared-ia`.
2. `git status --short -uall` trống. Có đường lạ thì dừng và ghi vào báo cáo.
3. Cổng 3199 và 3100 trống (`lsof -nP -iTCP:3199 -sTCP:LISTEN`, tương tự với 3100). Bận thì không giết tiến trình nào: dừng phần kiểm trình duyệt, ghi vào báo cáo.
4. Lưu đầu ra của bước 2 vào `236/status-before.txt`.

## Mốc trước khi sửa (Claude đo 31/10 00:55, trong worktree này)

- **11 script đang đọc `portal/src/admin/space-typing.ts`:** `alternative-modes`, `duel`, `events`, `qa`, `phase-b`, `ranked`, `ui-assets`, `v2-design-system`, `ui`, `v2-media`, `v2-shell` (tiền tố `scripts/validate-space-admin-`). 8 xanh, 3 đỏ:
  - `qa`: đỏ vì ghim kiểm QA đã cũ ("QA audit is stale", SHA Space). Ngoài phạm vi. **Không đổi SHA ghim.**
  - `ui`: "Primary administrator navigation is missing Live Ops".
  - `v2-shell`: "Shop must not remain a primary navigation item in A2".
  - Ba script này cũng đỏ ở repo chính, tức là lỗi có sẵn.
- **`pnpm admin:test`:** 46/47. Ca `pinned Space Typing runtime tree bootstraps without binary copies or duplicate versions` đỏ **chỉ vì worktree không có media runtime của Space**; ở repo chính là 47/47. Ca này phải là ca đỏ duy nhất.
- `node scripts/validate-play-mode.mjs`: xanh. `portal` tsc: xanh.

Với `ui` và `v2-shell`:
- xem `git log` của script và của điều hướng để biết bên nào cũ;
- sửa bên cũ nếu nó nằm trong phần điều hướng bạn dời, kèm lý do trong báo cáo;
- nếu không, chỉ ghi đề xuất.

Không được thêm script đỏ mới.

## Việc

1. **Vỏ và khu (§3.2):**
   - Đổi tên `portal/src/admin/space-typing.ts` thành `portal/src/admin/admin-shell.ts`, giữ mã. Tên hiện: **Typing Game Admin**.
   - Thêm:
     - `portal/src/admin/areas/registry.ts`;
     - `areas/space-typing.ts`: `NAV_GROUPS` dời sang, giữ mọi nhóm, trừ Media Library và Roles & Permissions;
     - `areas/shared.ts`: khu **All games**.
   - Mỗi khu khai `{ id, label, base, navGroups, renderPage }`.
   - Đầu thanh bên có nút chọn khu `All games | Space Typing`.
   - Breadcrumb theo tên khu, ví dụ "All games / Learning Content", "Space Typing / Ships".
   - Nhóm **Administration** ở cuối thanh bên của mọi khu, gồm Media Library `/admin/media` và Roles & Permissions `/admin/roles`.
   - **Audit chưa làm thì không hiện** (luật P12: không route chết).
   - Giữ nhận diện P10: giao diện tối kiểu chỉ huy, Exo 2 / Be Vietnam Pro. Chữ giao diện bằng tiếng Anh như hôm nay.
2. **Khu All games ở G5.** Chỉ hiện trang có thật:
   - **Overview** (`/admin/shared`), chỉ đọc:
     - bảng "Games using Typing Feel" lấy từ `admin/typing-feel/consumers.json` (file mới):
       - bốn dòng: Last Line `survival.typing-game.local`, Dragonhold `dragon.typing-game.local`, Wordwoven `td.typing-game.local`, Monkeytype `monkeytype.typing-game.local`;
       - cột: tên, host, đã đọc Typing Feel chưa (hôm nay: chưa, còn bản chép), nút mở game.
     - ô "Typing Feel catalogue": đọc `typing-feel/public/v1/keys/keys-manifest.json` nếu có (revision, số bộ); không có thì hiện "Not imported yet". Ở worktree này thư mục đó chưa có. Đó là đúng, vì G1 làm ở repo chính.
     - Server phục vụ qua route có token, ví dụ `GET /api/admin/shared/overview`.
   - **Learning Content** (`/admin/shared/learning-content`): chính trang Typing Content hôm nay, đổi tên, chỉ đọc. Nó đọc dữ liệu chung (`shared/vocabulary`, `shared/typing-texts`).
     - Nó phải chạy được **khi thiếu Space**. Nếu API hôm nay (`/api/admin/space-typing/typing-content/catalog`, `admin/server.mjs:276`) phụ thuộc phần khởi động của Space, thêm route `/api/admin/shared/learning-content/catalog` và giữ route cũ làm bí danh.
   - **Không** thêm Keyboard Sounds, Typing Effects, Release & History (G6).
3. **Định tuyến:**
   - `portal/src/main.ts` định tuyến `/admin` và `/admin/*`. `/admin` mở All games (`/admin/shared`).
   - Nút portal "Space Admin" (`main.ts:450`) thành **"Admin"**, trỏ `/admin`.
   - Mọi URL `/admin/space-typing/*` cũ vẫn chạy. Ba đường chuyển, qua một bảng chuyển đường trong `normalizedAdminPath` (`history.replaceState`; **không** dùng `NAV_ALIASES`):
     - `/admin/space-typing/media` → `/admin/media`;
     - `/admin/space-typing/roles` → `/admin/roles`;
     - đường Typing Content cũ → `/admin/shared/learning-content`.
4. **Bảng lệnh nhanh** (`space-typing-command.ts`): thêm các mục của All games và Administration.
5. **Server chạy khi thiếu Space (§3.3):**
   - Bọc mọi phần khởi động cần Space trong khối có bắt lỗi:
     - 13 hợp đồng (`server.mjs:48–60`);
     - `SpaceTypingRevisionStore`, `store.initialize`;
     - `bootstrapMediaReferences`;
     - `MusicAssetService`.
   - Thêm biến `TYPING_GAME_ADMIN_SPACE_DIR` (mặc định `games/space-typing`) cho mọi chỗ server đọc Space, để test giả được cảnh thiếu Space.
   - Khi thiếu Space:
     - `/api/admin/space-typing/*` và `/api/runtime/space-typing/*` trả 503, JSON `{ "error": "space-typing-not-checked-out" }`;
     - khu Space hiện "Space Typing is not checked out";
     - **trừ** Media V2 (`/api/admin/space-typing/media/*`, `/api/runtime/space-typing/media/*`): vẫn chạy;
     - All games vẫn chạy.
   - Thêm test Node cho cả hai cảnh (có Space, thiếu Space) vào `admin:test`.
6. **Quyền (§3.13, câu 9):** thêm `shared.publish` vào `ADMIN_PERMISSIONS`, đánh dấu nguy hiểm, có trong Super Admin. G5 chưa có nút nào dùng nó.
   - Chỉ thêm khi không phá test quyền hiện có. Có vướng thì để lại cho G6 và ghi vào báo cáo.
7. **nginx và `validate-play-mode`:**
   - Trong `infra/nginx/typing-game.local.play.conf`:
     - đổi `location /api/admin/space-typing/` thành `location /api/admin/` (vẫn sang 3199);
     - thêm `location /api/runtime/typing-feel/` sang 3199.
   - `dev.conf` không cần sửa (Vite chuyển `/api/admin`). Kiểm `portal/vite.config.ts` có chuyển `/api/runtime/typing-feel` không; thiếu thì thêm.
   - `scripts/validate-play-mode.mjs:311` đổi chuỗi bắt buộc thành `location /api/admin/`.
   - **Chỉ sửa đúng các dòng đó.** Repo chính đang thêm block `feel.typing-game.local` vào cùng hai file nginx và thêm kiểm feel vào `validate-play-mode.mjs`. Sửa ít dòng thì lúc gộp không vướng. **Không** thêm block feel.
8. **Script kiểm:**
   - Sửa 11 script đang đọc `space-typing.ts` sang `admin-shell.ts` và `areas/space-typing.ts`, giữ đúng ý kiểm của chúng.
   - Thêm `scripts/validate-admin-shared-ia.mjs` và script `admin:ia:validate` trong `package.json`. Nó kiểm:
     - registry chỉ có khu thật;
     - `/admin` mở All games;
     - bảng chuyển đường có đủ ba đường;
     - Administration có ở mọi khu;
     - không mục điều hướng nào trỏ tới trang không có renderer;
     - danh sách URL cũ đều phân giải được;
     - nút portal là "Admin".
9. **Trình duyệt (bắt buộc):**
   - Chạy server admin:
     - `TYPING_GAME_ADMIN_PORT=3199`;
     - `TYPING_GAME_ADMIN_DATA_DIR=<worktree>/tmp/236-admin-data`, để không đụng `.local` của repo chính;
     - token mặc định `local-dev`.
   - Chạy Vite của portal (`pnpm --dir portal dev`, cổng 3100).
   - Chrome headless qua CDP, theo cách `tools/audio-lab/board/tools/cdp-run.mjs`. Chụp ở 1280×800 và 1920×1080:
     - `/admin`;
     - `/admin/shared`;
     - `/admin/shared/learning-content`;
     - `/admin/space-typing`;
     - một trang Space, ví dụ Ships;
     - `/admin/media`;
     - `/admin/roles`;
     - ba URL cũ được chuyển.
   - Ghi JSON "URL mở → URL cuối, tiêu đề, breadcrumb, lỗi console".
   - Chạy thêm một lần với `TYPING_GAME_ADMIN_SPACE_DIR` trỏ tới thư mục không có. Cho thấy All games chạy và khu Space hiện thông báo.
   - Ảnh để dưới `tmp/236/` của worktree. Xong thì:
     - giữ một contact sheet và JSON trong `docs/codex-queue/236/`;
     - xoá ảnh thô **của mình**: `node tools/capture-prune/prune.mjs tmp/236 --apply`, chạy trước một lần không có `--apply`;
     - tắt server và Vite mình đã mở.

## Chỉ được sửa

- `portal/src/admin/**`, `portal/src/main.ts`; `portal/vite.config.ts`, chỉ phần proxy.
- `admin/server.mjs`, `admin/admin-security.mjs`; các module `admin/*.mjs` cần cho việc chạy khi thiếu Space; `admin/typing-feel/consumers.json` (mới); file mới cho route overview; test admin mới hoặc đã có.
- 11 script `scripts/validate-space-admin-*.mjs` nêu trên; `scripts/validate-admin-shared-ia.mjs` (mới).
- `scripts/validate-play-mode.mjs`, chỉ dòng kiểm location nêu ở mục 7. `infra/nginx/typing-game.local.play.conf`, chỉ hai location nêu ở mục 7.
- `package.json`, chỉ mục `scripts`: danh sách `admin:test`, `admin:ia:validate`.
- `docs/codex-queue/236-report.md`, `docs/codex-queue/236/**`, `tmp/236/**`.

## Cấm

- Mọi lệnh Git ghi: commit, add, stash, reset, checkout, switch, rebase, worktree.
- Repo chính `/Users/toandx/htdocs/typing-game`.
- `games/**`, kể cả `games/space-typing` (chỉ đọc). Tu Tiên.
- `typing-feel/` (G1), `shared/game-kit/**` (G2), `docs/games/TYPING_FEEL_SERVICE.md` (Claude cập nhật).
- File media.
- Mạng ngoài máy.
- Giết tiến trình mình không mở.

## Kiểm (bắt buộc, ghi số trước và sau)

1. `pnpm --dir portal build` (tsc và vite build), `pnpm --dir portal test`.
2. `pnpm admin:test`: chỉ ca bootstrap media nêu trên được đỏ.
3. 11 script `validate-space-admin-*`: không thêm script đỏ.
4. `pnpm admin:ia:validate`.
5. `node scripts/validate-play-mode.mjs` và `node --test scripts/validate-play-mode.test.mjs`.
6. `git diff --check`, rồi `git status --short -uall` lưu vào `236/status-after.txt`.
7. Mục 9 (trình duyệt).

## Báo cáo

Báo cáo bằng tiếng Việt, gồm:
- danh sách file đã sửa hoặc tạo, mỗi file một dòng nói làm gì;
- bảng kiểm trước và sau, có mã thoát;
- kết luận về `ui` và `v2-shell`;
- những gì để lại cho G6;
- mọi chỗ bạn phải đoán.
