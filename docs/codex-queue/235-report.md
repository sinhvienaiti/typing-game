# Phiếu 235 · Dragonhold · Sửa F2, F3, F4 của kiểm lại 222

**Xong cả ba lỗi, chưa commit.** Claude (Opus 5.5) làm thay Codex theo lệnh chủ dự án 30/10 15:25. Lượt dừng trước bị thay: `status-before.txt`, `preflight.json` và mọi file khác trong `235/` đều là của lượt này.

- F2: màn tựa có lớp gốc riêng `.dh-title-screen`.
- F3: màn tựa mặc định có nút **Retry**.
- F4: test thường chỉ dùng fixture nằm trong repo game.

Số chung:
- `pnpm check`: **70 file / 607 test → 73 file / 625 đạt + 1 bỏ qua**; kit 75; build xanh.
- Golden 10/10, English UI 9/9.
- Gói production: 0 lỗi, 402 file.
- Bản chép sạch không có `tmp/map1-audit` vẫn xanh.
- 8/9 đột biến làm test mới đỏ. Ca còn lại là đột biến tương đương (giải thích ở F3).

## Điều kiện đầu vào

| Điều kiện | Kết quả |
| --- | --- |
| Có `222-report.md` | Có |
| Worktree `games/.wt-dh-codex`, nhánh `dh-codex` | Đúng; HEAD `6aa593a2dce6637cccbe24a58709b86f7127f607`, đầu và cuối như nhau |
| Status chỉ có đường đã biết | **56 = 51 (222) + 5 (223)**: 26 M, 30 mới; 0 đường lạ, 0 đường thiếu ([preflight.json](235/preflight.json)) |
| `df` | 48 GB trống |

## F2 · CSS màn tựa tràn sang tiêu đề khác

**Test (mới):** `tests/ui/title-css.test.ts`, 3 test.
- Test đọc `dh.css` và `title.css` thật, kể cả khối `@media`.
- Test tìm mọi `el(doc, "<tag>", "… dh-title …")` trong `src/ui` và `src/app`: **10 tiêu đề**. Trong đó có đúng sáu chỗ 222 nêu: hud 291, shop-strip 177, wave-card 145 và 161, results 232 và 249. Bốn chỗ thêm: debut-card 92, placement-ui 245, 511 và 527.
- Mỗi tiêu đề không được nhận `position`, `inset`, `z-index`, `background*`, `pointer-events`. Phép so khớp thận trọng: bỏ qua tổ tiên, coi pseudo-class là khớp.

**Đỏ trước sửa:** 3/3 đỏ. Có **50 lần tràn** (10 tiêu đề × 5 thuộc tính), tất cả từ quy tắc `.dh-title` của `title.css`, không lần nào từ `dh.css`. Log: [red-final-tests.log](235/red-final-tests.log).

**Sửa:**
- `src/ui/styles/title.css:1–13`: bốn selector gốc đổi từ `.dh-title` sang `.dh-title-screen`, kể cả `[hidden]` và `[data-backdrop="live"]`. Các lớp con `dh-title__*` giữ tên, vì hai test cũ (`title.test.ts`, `deck-app.test.ts`) dùng chúng mà phiếu không cho sửa.
- `src/ui/title.ts:38–39`: gốc màn tựa là `"dh-title-screen dh-title"`.
  - Mọi bố cục chỉ nằm trên `.dh-title-screen`.
  - Token `dh-title` giữ lại để chữ màn tựa vẫn dùng kiểu chữ `dh.css:87–95` như trước, không đổi hình.
  - `title.test.ts:43,95` tìm gốc qua `dh-title`, và phiếu không cho sửa file này.

**Xanh sau sửa:** 3/3.
- `.dh-title` chỉ còn 6 thuộc tính kiểu chữ: font-family, font-variant-numeric, font-weight, letter-spacing, color, text-shadow.
- `title.css` không còn selector `.dh-title` trần.
- Gốc màn tựa vẫn có `position:absolute; inset:0; z-index:40; pointer-events:auto`.

**Đột biến:**

| Mã | Đột biến | Test mới đỏ |
| --- | --- | --- |
| M2a | Quy tắc gốc của `title.css` về lại `.dh-title` | 3 |
| M2b | Gốc trong `title.ts` chỉ còn lớp `dh-title` | 1 |

## F3 · Màn tựa mặc định mất đường Retry

**Test (mới), 14 test:**
- `tests/ui/title-retry.test.ts` (6 test): state thuần, DOM của màn tựa, phím, chuột, cổng, dispose.
- `tests/app/title-retry.test.ts` (8 test): app thật như `deck-app.test.ts`, gồm ba lý do lỗi, lỗi hai lần, cổng, dispose giữa chừng, và hai test cho loader.

Các ca:
- lỗi rồi Retry thì nạp lại; Start bật khi bộ từ hợp lệ, rồi vào trận đúng 1 lần;
- **Retry hai lần liền (Enter, Enter, click) chỉ nạp thêm 1 lần**: `load` tổng cộng 2 lần, gồm lượt đầu;
- sau khi có bộ từ, bấm Retry hay Enter không nạp thêm;
- loader: đang bận thì `load()` trả false; sau khi có bộ từ hoặc sau dispose thì không nạp.

**Đỏ trước sửa:** 13/14 đỏ. Ca cổng xanh sẵn, đúng như mong đợi vì cổng vốn dùng được.

**Sửa:**
- `src/app/deck-boot.ts:6–46` · `createDeckLoader`: tách đường phục hồi của 195 (cũ `deck-boot.ts:73–89`), không có bảng lỗi.
  - Mỗi lần chỉ một lượt nạp (`:37`); sau khi có bộ từ thì đóng (`:32`); dispose cũng đóng (`:44`).
  - Lỗi khác loại được đổi thành `DeckBuildError("load-failed", 0)`.
  - `startDeckBoot` (`?title=0`) dùng lại loader này (`:115–124`), giữ nguyên hành vi.
- `src/ui/title-state.ts:21–29`:
  - `retryTitle`: chỉ chạy từ `blocked`; chỉ bỏ nguồn `words`, giữ ba nguồn còn lại.
  - `wantsRetry`: Enter ở ô 0 khi `blocked`.
  - `titleAction` không đổi, nên `title-state.test.ts:21` vẫn đúng.
- `src/ui/title.ts`:
  - `:26`: thêm tùy chọn `onRetry`.
  - `:63`: nút `dh-title__retry`, dùng ảnh `retry` có sẵn và chữ "Retry".
  - `:95–108`: ô 0 là Retry khi bộ từ lỗi hoặc đang nạp lại; khi nạp, nút tắt và ghi "Loading words…".
  - `:125–131`: nếu loader từ chối thì giữ trạng thái `blocked`.
  - `:134`: Enter gọi Retry.
  - `:139–144`: hover và focus.
  - `:152`: lần settle `words` xóa cờ đang nạp lại.
- `src/app/app.ts:26,917–926,936,942`: đường màn tựa dùng `createDeckLoader`. Màn tựa gọi `onRetry: () => titleDeck.load()`. `deckBoot` là loader nên app.dispose đóng nó. Bỏ import `DeckBuildError` không còn dùng.
- Start vẫn tắt tới khi trạng thái `ready`. Back to portal vẫn ở ô 1 (test app và test DOM).

**Xanh sau sửa:** 14/14. Các test cũ liên quan cũng xanh: title 10, title-state 7, deck-app 10, deck-boot 9.

**Đột biến:**

| Mã | Đột biến | Test mới đỏ |
| --- | --- | --- |
| M3a | App không truyền `onRetry` (không có nút Retry) | 5 |
| M3b | Enter không gọi Retry | 7 |
| M3c | Loader bỏ chặn "đang bận" | 1 |
| M3e | Loader không đóng sau khi có bộ từ | 1 |
| M3f | dispose không đóng loader | 1 |
| M3d | `retry()` bỏ kiểm `blocked` | **0, đột biến tương đương** |

M3d không đỏ vì hai chốt khác đã chặn: nút Retry bị `disabled` khi không ở `blocked`, và `wantsRetry` đòi trạng thái `blocked`. Chốt trong `retry()` chỉ là phòng thủ thêm. Chi tiết: [mutations.json](235/mutations.json); mọi file được khôi phục và kiểm SHA-256.

## F4 · Test thường cần dữ liệu ngoài repo

**Đỏ trước sửa:** bản chép sạch với test cũ cho **1 đỏ / 623 đạt (624)**. Lỗi `ENOENT .../codex-235/dragon-hold/tmp/map1-audit/feel-35-1280/samples.json`. Log: [clean-before-f4.log](235/clean-before-f4.log).

**Sửa:**
- `tests/fixtures/idle-samples.json`: **21 dòng, 633 byte**, theo dạng mẫu audit. Fixture có:
  - một khoảng 2 s bị cắt còn 0,5 s;
  - một khoảng trống ở cuối đợt, một trước nghỉ, một ở cuối mẫu.
- Số tính tay khớp script:
  - trước: 9 s, trống 7,5 s, **83,3 %**, 5 khoảng;
  - sau (nhìn trước 1,5 s, ×1,75): 8,1 s, trống 6,6 s, **81,6 %**;
  - nhìn trước 0 s: ×1,75 là 74,1 %, ×2 là 71,4 %.
- `tests/app/idle-estimate.test.ts`, đường dẫn tính từ `__dirname`:
  - `:7–16`: hằng số và hàm phụ;
  - `:26–37`: chạy CLI trên fixture; kết quả phải bằng `estimateIdle` chạy trong tiến trình; fixture không đổi byte;
  - `:38–51`: fixture dưới 50 KB và nằm trong gốc game; quét `tests/`, không file nào có `resolve|join|readFileSync|existsSync("../…`;
  - `:52–60`: phép đối chiếu với audit thật thành **lệnh kiểm tùy chọn**, `DH_IDLE_AUDIT_SAMPLES=/đường/tuyệt/đối/samples.json pnpm exec vitest run tests/app/idle-estimate.test.ts`. Không đặt biến hoặc thiếu file thì bỏ qua.

**Xanh sau sửa:**

| Cách chạy | Kết quả |
| --- | --- |
| Mặc định | 5 đạt + 1 bỏ qua |
| Có `DH_IDLE_AUDIT_SAMPLES` trỏ tới mẫu thật | 6/6; tái hiện 52,4 / 47,8 / 38,6 |
| Đường không tồn tại | 5 đạt + 1 bỏ qua |

SHA-256 của mẫu thật trước và sau: `d9e42203…f0f7`, không đổi. Logs: [f4-default.log](235/f4-default.log), [f4-optional-audit.log](235/f4-optional-audit.log), [f4-optional-missing.log](235/f4-optional-missing.log).

**Đột biến M4a:** thêm lại một lệnh đọc `resolve("../dragon-hold/tmp/…")` vào test thì test chặn đỏ (1).

## Kiểm

| Kiểm | Trước | Sau |
| --- | --- | --- |
| `pnpm check`: kit → test → tsc → build | mã 0; kit 75; **70 file / 607 test** (= 593 của 222 + 14 của 223) | mã 0; kit 75; **73 file / 625 đạt + 1 bỏ qua (626)**; tsc và Vite xanh |
| Golden riêng | — | **10/10**, MD5 `m0.json` `75f74947dac170d05fd659f99417940e`, như 222; không diff `tests/golden` |
| English UI riêng | — | **9/9** |
| `pnpm deploy:pack` production (không có `VITE_PORTAL_URL`) | 222: 402 file, 35.061.724 B | mã 0; ok; **0 lỗi**; 402 file; **35.062.747 B** (+1.023 B, mã Retry và CSS); localHost 0; 0 file chứa `typing-game.local` |
| Bản chép sạch `games/dragon-hold/tmp/codex-235/clean` | test cũ: 1 đỏ / 624 | **73 file / 625 đạt + 1 bỏ qua**, mã 0 |

Phần tăng 19 test gồm 3 F2, 6 + 8 F3, và 2 ở idle-estimate (một test chặn và một test tùy chọn; test đọc mẫu thật được thay bằng test fixture).

Dựng bản chép sạch theo mục "Dựng bản chép" của 224:
- `git ls-files -co --exclude-standard`: 480 file, gồm 5 file mới của 235; `public/` chép riêng;
- `node_modules` là thư mục thật, mỗi mục bên trong là symlink;
- biến `pnpm_config_verify_deps_before_run=false`, `TMPDIR` riêng.

Hai điểm khác bản chép của 224:
1. `public/assets` của worktree là symlink tương đối (`../../dragon-hold/public/assets`), nên trong bản chép thay bằng symlink tuyệt đối tới cùng thư mục, như 222 đã làm.
2. Bản chép không có `tmp/`, và không có `../dragon-hold` bên cạnh.

Trong lúc chạy bản chép, `find` worktree mới hơn marker ra **0 dòng**. Đã xóa cả `games/dragon-hold/tmp/codex-235`.

## Phạm vi và status

[status-after.txt](235/status-after.txt): **61 đường = 56 + 5 file mới**:
- `tests/ui/title-css.test.ts`, `tests/ui/title-retry.test.ts`, `tests/app/title-retry.test.ts`;
- `tests/fixtures/idle-samples.json`;
- `docs/changelog/2026-10-30-fix-222-title-retry-fixture.md`.

Trong 56 đường cũ, chỉ 6 file đổi hash, đều nằm trong danh sách được sửa:

| File | Dòng thêm / bớt |
| --- | --- |
| `title.css` | +5 / −4 |
| `title.ts` | +51 / −17 |
| `title-state.ts` | +9 / −0 |
| `app.ts` | +14 / −11 |
| `deck-boot.ts` | +55 / −22 |
| `idle-estimate.test.ts` | +44 / −8 |

Toàn bộ diff ở [fix.diff](235/fix.diff); bản gốc ở `235/before/`.

Đã giữ đúng phạm vi phiếu:
- Không sửa `src/sim/**`, `src/kit/**`, golden, `scripts/**`, `title.test.ts`, `deck-app.test.ts`, `deck-boot.test.ts`, và năm file của 223.
- Git chỉ đọc (`GIT_OPTIONAL_LOCKS=0`). Không commit, stash, reset hay đổi nhánh.
- Không chạy dev server, không mở trình duyệt, không dùng mạng.
- Không tạo ảnh, âm hay frame nào cần prune.
- Ở repo cha chỉ ghi `235-report.md` và `235/`. Các đường mới của 230, 232, 234 trong status cha là của làn khác.

Không làm F1 và F5, đúng phạm vi phiếu. Không chạy lại ba probe của 222, vì chúng phải chép vào `tests/` của worktree, là vùng phiếu không cho ghi. Các test mới đã phủ cả ba ý của probe.

## Cần trình duyệt của Claude

1. Ở **1280×720** và **1920×1080**, kiểm năm vùng sau không còn lớp nền tối phủ màn và không chặn chuột:
   - tiêu đề HUD "Hỏa Long";
   - "Loadout" của cửa hàng;
   - thẻ đợt và banner;
   - tiêu đề kết quả và "Wordbook";
   - tên trên thẻ ra mắt và bảng đặt.
2. Màn tựa ở hai cỡ: kiểm bố cục, nền, logo hoặc chữ thay logo. Kiểu chữ dự kiến không đổi, vì gốc vẫn có token `dh-title`.
3. **Retry khi tắt mạng.** Tải trang mặc định khi đã tắt mạng (hoặc chặn request vocabulary), rồi kiểm:
   - màn tựa hiện "Words could not load", Retry có ảnh `retry`, viền focus nằm trên Retry;
   - Start tắt;
   - bật mạng, nhấn Enter: nút chuyển "Loading words…" rồi Start bật;
   - làm lại bằng chuột;
   - tắt mạng lần nữa: Retry hiện lại.
4. Có `VITE_PORTAL_URL`: dùng → để sang "Back to portal" rồi Enter; kiểm `?title=0` vẫn ra bảng lỗi cũ của 195.
5. Dòng trạng thái khi đang nạp lại ghi "Loading 3 of 4 · dragons" (nguồn xong cuối cùng, theo cách tính của 197). Cần quyết định có đổi thành "Loading words…" không. Lượt này chưa đổi.

## Bằng chứng (`docs/codex-queue/235/`)

- Đầu vào: `preflight.json`, `status-before.txt`, `parent-status-before.txt`, `before/` (6 file gốc).
- Kiểm: `check-before.log`, `check-after.log`, `golden.log`, `english-ui.log`, `pack-prod.log`, `pack-prod.json`.
- Đỏ và xanh: `red-f2-f3.log` (lượt đỏ đầu, bản test trước khi thêm assert phím và sửa stub `ownerDocument`), `red-final-tests.log` (test cuối trên mã trước 235: 16 đỏ / 1 xanh), `clean-before-f4.log`, `clean-after.log`, `f4-*.log`.
- Đột biến: `mutations.json`.
- Diff và status: `fix.diff`, `status-after.txt`, `parent-status-after.txt`.

## Bổ sung 30/10 · Dòng trạng thái khi nạp lại (mục 5 ở trên)

Điều phối chốt: khi màn tựa nạp lại bộ từ sau Retry, dòng trạng thái ghi **"Loading words…"**, không ghi số đếm 197. Giữ token `dh-title` ở gốc màn tựa được chấp nhận. F1, F5 không đụng.

- Test trước: `tests/ui/title-retry.test.ts` thêm 3 test (nạp lại khi nguồn khác còn chạy hoặc đã xong; từ xong trước thì về lại "Loading 1 of 4 · words"; loader từ chối thì giữ câu lỗi). `tests/app/title-retry.test.ts` thêm 2 assert ở ca lỗi hai lần. Đỏ trước sửa: 2/3 (ca từ chối xanh sẵn, đúng mong đợi); log cũ từng hiện cả "Loading 0 of 4 · words".
- Sửa: `src/ui/title.ts:112–117`, nhánh `retrying ? "Loading words…"` trước số đếm.
- Đột biến bỏ nhánh này: 3 test đỏ (2 UI + 1 app); file khôi phục, SHA-256 khớp.
- Kiểm: `pnpm check` mã 0, kit 75, **73 file / 628 đạt + 1 bỏ qua**; golden 10/10, MD5 `m0.json` `75f74947…940e` không đổi; English UI 9/9; `deploy:pack` production ok, 0 lỗi, 402 file, 35.062.768 B (+21 B), localHost 0.
- Status worktree: vẫn 61 đường; chỉ `title.ts`, hai test title-retry và changelog 235 đổi nội dung. Chưa commit.
