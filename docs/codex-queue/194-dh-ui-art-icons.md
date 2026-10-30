# Phiếu 194 · Dragonhold · Đường ảnh UI: gắn 36 icon đã nhận thay SVG, emoji và rêu CSS

**Nguồn:**
- `docs/games/map1/UI_IMAGERY.md` §8.3: "Script chuẩn bị `scripts/ui-art/prepare.mjs` … `ICONS` trả `<img>` theo bảng URL"; §5.1: rêu CSS `dh.css:88-118` "**bỏ ngay**".
- `docs/HANDOFF_CURRENT.md` §3: "Ảnh đã nhận, chờ gắn … 137 (8), 138 (10), 139 (9)", 140 (chín icon); "Chưa có làn gắn ảnh UI".
- `AGENTS.md` (chủ dự án 28/10): không icon vẽ bằng CSS, không emoji; mọi chi tiết UI có ảnh thật.
- Chủ dự án 30/10: "tăng thêm việc cho codex cho tôi".

**Báo cáo:** `docs/codex-queue/194-report.md` (repo cha, tiếng Việt), thư mục `docs/codex-queue/194/`.

**Không trùng:** 137–140, 161, 163, 164 chỉ vẽ ảnh; 080 là ô đất; 171 là manifest media; 180 và 192 là nút Settings, nút Sound. Phiếu này dựng đường ảnh UI và gắn icon.

> **Chạy lại (30/10, 08:44, điều phối):** lượt đầu (08:28) bị ngắt vì chủ dự án đổi tài khoản Codex (401 `token_revoked`). Các thay đổi chưa commit trong worktree là việc dở của chính phiếu này. Đọc `git status` và `git diff`, giữ phần đúng, làm tiếp cho đủ phiếu, rồi kiểm như thường; ghi đè báo cáo cũ nếu có.

## Chỉ chạy khi

- Phiếu 187 đã chạy xong (có `docs/codex-queue/187-report.md`). Tốt nhất Claude đã duyệt và commit 187; chưa commit thì vẫn chạy theo ý dưới.
- Nếu lúc bắt đầu `git status --short -uall` còn đúng các file của 187 (`README.md`, `src/app/app.ts`, `src/app/learning.ts`, `src/app/portal.ts`, `src/ui/results.ts`, `tests/app/portal.test.ts`, `tests/ui/results-screen.test.ts`, `vite.config.ts`, `tests/portal-build.test.ts`, `docs/changelog/2026-10-29-portal-link.md`):
  - làm tiếp trên đó, không hoàn tác;
  - lưu `git status --short -uall` và `git diff` lúc bắt đầu vào `194/start-status.txt`, `194/start.diff`;
  - báo cáo ghi rõ đoạn nào của `results.ts`, `README.md` là của 194.
- Có file lạ khác thì dừng, ghi vào báo cáo.

## Luật chung (phiếu mã)

- **Nơi làm:** worktree `games/.wt-dh-codex` (nhánh `dh-codex`). cwd của làn là repo cha (`.`), như 168, 169; chạy `pnpm` trong thư mục worktree.
- **Đầu ra media:** `public/assets` của worktree là liên kết tới `games/dragon-hold/public/assets` (checkout chính). WebP và `manifest.json` của script đi qua liên kết đó vào `games/dragon-hold/public/assets/dragon-hold/ui/icons/` (Git bỏ qua, qua `.git/info/exclude`). Đây là chỗ duy nhất của checkout chính được ghi.
- **Ảnh nguồn, chỉ đọc:** `../dragon-hold/art-src` (checkout chính: `/Users/toandx/htdocs/typing-game/games/dragon-hold/art-src`). Worktree không có `art-src/ui`, nên mọi lệnh truyền `--art-src`.
- Git chỉ đọc. Test trước, mã sau. Chú thích tiếng Anh, ngắn.
- Chữ người chơi thấy là tiếng Anh. Ván vàng và luật chơi không đổi.
- File tạm, fixture test, tờ xem nằm trong `tmp/` của worktree (Git bỏ qua). Không ghi ra ngoài repo, kể cả thư mục tạm của hệ điều hành.
- Đây là phiếu mã: không sinh ảnh, không sửa ảnh. Công cụ chỉ đổi định dạng và thu nhỏ (tinh thần `docs/games/ART_ACCEPTANCE.md` §5): không làm nét, không đổi màu, không phóng to, không cắt.

## Đầu vào

- **36 icon đã nhận**, `art-src/ui/icons/<tên>.{64,128,256}.png` (RGBA). Luật cỡ: `docs/codex-queue/accept-29-10/verdict.md` mục 137, 138, 139 và `accept-29-10b/verdict.md` mục "Sẵn sàng gắn".
  - 137 (8): `wave-horn`, `chain`, `dragon-rage`, `shield`, `phase-prep`, `phase-fight`, `phase-break`, `fast-forward`;
  - 138 (10): `pause`, `camera-reset`, `keyboard`, `speaker`, `check`, `new-word`, `deny`, `lock`, `upgrade`, `sell`;
  - 139 (9): `lane-bridge`, `lane-stream`, `lane-sky`, `slot-trap`, `slot-house`, `slot-hold`, `seal-lit`, `seal-unlit`, `edge-arrow`;
  - 140 (9): `star-lit`, `star-unlit`, `stat-accuracy`, `stat-new-words`, `stat-words-seen`, `retry`, `status-learned`, `status-review`, `status-new`.
- **17 icon tạm, kiểu cũ**, `art-src/icons/normalized/<nguồn>.{64,256}.png` (RGBA), cho các ô mà bản `.v2` của 163, 164 còn chờ chấm:
  - `gold`, `skill-fire-breath`, `skill-sky-fire`, `skill-roar` (nguồn `015-skill-roar`, như UI_IMAGERY DH-22), `skill-ultimate`, `potion-small`;
  - `spikes`, `pine-bomb`, `net-launcher`, `moss-warden`, `herb-hut`, `dragon-heart`, `hard-scale`;
  - `enemy-general`, `family-moss`, `family-beast`, `family-bug`.
- **Không dùng:** mọi file `.v2`, `.v3`, `.try*`, `.alpha`, `.final`, `.warm`, `rejected-*`; các tên chưa nhận `armour`, `danger`, `flag-pull`, `swarm`, `easier`, `pace-*`.
- Mẫu script: `scripts/assets/prepare-ground.mjs` (đổi xong mọi file rồi mới ghi; manifest ghi sau cùng qua file tạm). `magick` và `cwebp` có sẵn.

## Việc

1. **Bảng chọn** `src/ui/ui-art.json` (vào Git):
   - `version`: số nguyên, bắt đầu 1. `icons`: 53 mục.
   - Mỗi mục: `name` (tên ảnh); `keys` (tên mã đang gọi `icon()`, ví dụ `gold` có `["coin"]`); `alt` (tiếng Anh); `source` (đường tương đối `--art-src`, không đuôi cỡ, ví dụ `ui/icons/wave-horn`, `icons/normalized/015-skill-roar`); `sizes` `[64, 128, 256]`; `accepted` (số phiếu nhận, ví dụ `"137"`, hay `null`); `interim` (true cho 17 icon cũ).
   - Một `name` hay một `key` chỉ thuộc một mục.
   - Khi 163, 164 được nhận, Claude chỉ sửa `source` sang `.v2` và `interim` sang false. Mã không đổi.
2. **Script** `scripts/ui-art/prepare.mjs`; lệnh `pnpm prepare-ui-art --art-src <dir> [--out <dir>] [--check]`:
   - mỗi cỡ lấy đúng file cỡ đó (`<source>.<cỡ>.png`). Thiếu thì thu Lanczos từ cỡ lớn hơn gần nhất (icon cũ: 128 từ 256). Không có cỡ lớn hơn thì báo lỗi, không phóng to;
   - xuất `public/assets/dragon-hold/ui/icons/<name>.<cỡ>.webp`: giữ alpha, `-strip`, quality 90, alpha-quality 100;
   - đo PSNR từng WebP so với PNG cùng cỡ. Dưới 35 dB thì xuất lossless file đó và ghi lại;
   - ghi `manifest.json` cùng thư mục: `version`; mỗi tên có `interim`, `source`, md5 từng file nguồn, và mỗi cỡ `file`, `width`, `height`, `bytes`, `md5`;
   - lỗi giữa chừng thì không file cũ nào bị thay;
   - `--check` không ghi gì. Thoát 1 và nêu tên file khi: thiếu file; md5 hay bytes lệch manifest; manifest có tên ngoài bảng; md5 nguồn đã đổi;
   - `--help` in cách dùng.
3. **`icon()` trả `<img>`** (`src/ui/skin.ts:127-185`):
   - mọi `name` và `key` của bảng trả `<img class="dh-art" src="/assets/dragon-hold/ui/icons/<name>.<cỡ>.webp?v=<version>" width="<ô>" height="<ô>" alt="" aria-hidden="true" decoding="async" draggable="false">`;
   - tham số mới `{ box?: number; label?: boolean }`. `box` là cạnh ô ở `--ui` = 1, mặc định 20 (như `.dh-icon`). Chọn cỡ nhỏ nhất ≥ `box × 2,4` (`--ui` tối đa 1,2, màn mật độ 2). `label: true` thì `alt` lấy chữ của bảng, bỏ `aria-hidden`;
   - CSS: `.dh-icon > img` và `.dh-btn img` đầy ô, `object-fit: contain`, như SVG hôm nay;
   - xóa SVG của mọi tên đã thay (bảng A) và SVG của `foeIcon`. Chỉ còn SVG: `armour` (chờ 161), `dragon`, `white-dragon` (chờ chân dung UIC-DH-6);
   - nút chỉ có icon (tạm dừng, camera, nghe từ) có `aria-label` tiếng Anh, đúng chữ `title` đang có.
4. **Ảnh lỗi:**
   - `installSkin` gắn một listener `error` ở pha bắt (capture) trên `document`, cho `img.dh-art`;
   - gọi `console.warn("[ui-art] missing image: <url>")` một lần mỗi URL, rồi ẩn ảnh (`hidden`);
   - không SVG, không emoji, không chữ thay;
   - tách phần xử lý thành hàm nhỏ có export, để test bằng đối tượng giả (repo không có DOM giả).
5. **Gắn.** Số dòng theo `dh-codex` 6aa593a cộng diff 187; lệch thì tìm theo chuỗi.

   **A. Thay hình vẽ bằng mã:**

   | Mã đang gọi | Ảnh | Chỗ |
   |---|---|---|
   | `coin` | `gold` (tạm) | `hud.ts:238`, `shop-strip.ts:250` |
   | `breath`, `skyfire`, `roar`, `inferno` | `skill-fire-breath`, `skill-sky-fire`, `skill-roar`, `skill-ultimate` (tạm) | `hud.ts:56-61,311,321-324,337` |
   | `potion`, `small-potion` | `potion-small` (tạm) | `hud.ts:328`, ô món |
   | `spikes`, `pine-bomb`, `net-launcher`, `herb-hut`, `moss-warden`, `dragon-heart`, `hard-scale` | cùng tên (tạm) | `shop-strip.ts:247`, `placement-ui.ts:520,601` |
   | `crown` | `enemy-general` (tạm) | `wave-card.ts:257,282`, `debut-card.ts:116` |
   | `foeIcon(gait, color)` | `family-<family>` theo trường `family` của quái hay tướng (tạm) | `wave-card.ts:258`, `debut-card.ts:116` |
   | `wing` | `lane-sky` | `wave-card.ts:249,259,274` |
   | `shield` | `shield` | `hud.ts:295` |
   | `pause` | `pause` | `hud.ts:259` |
   | `camera` | `camera-reset` | `hud.ts:265` |
   | `bar`, `rune`, `flag` | `slot-trap`, `slot-house`, `slot-hold` | `placement-ui.ts:419,602` |
   | `star` | `star-lit` hay `star-unlit` theo số sao | `results.ts:239` và lúc hiện kết quả |
   | `speaker`; SVG `SPEAKER`; emoji loa (U+1F50A) | `speaker` | `results.ts:348`; `learning-frame.ts:181,618` |
   | ký tự dấu đúng (U+2713) | `check` | `learning-frame.ts:325` |

   **B. Thêm icon trước chữ đang có (chữ giữ nguyên):**

   | Ảnh | Chỗ |
   |---|---|
   | `wave-horn` | ô Wave, `hud.ts:243-246` |
   | `chain` | ô Chain, `hud.ts:247-251` |
   | `phase-prep`, `phase-fight`, `phase-break` | dòng pha `hud.ts:421-433`: prep → `phase-prep`; warning, wave → `phase-fight`; break → `phase-break`; thắng, thua không icon |
   | `dragon-rage` | nhãn Dragon Rage `hud.ts:332`; nút gọi sớm `wave-card.ts:365-366`, trước "+N Dragon Rage" |
   | `deny` | toast của sự kiện `rejected` (`hud.ts:509`); toast khác không icon |
   | `lane-bridge`, `lane-stream` | tên đường `wave-card.ts:249`, theo `lane.id` (`cau`, `suoi`); đường trời vẫn `lane-sky` |
   | `phase-break` | chip "Breather", `wave-card.ts:289` |
   | `upgrade`, `sell` | menu ô `placement-ui.ts:531,537`, cạnh phím `=` và `-` |
   | `new-word` | huy hiệu NEW ở khung học, `learning-frame.ts:326` |
   | `gold`, `stat-accuracy`, `stat-new-words`, `stat-words-seen` | năm ô số `results.ts:299,322` (hai ô Gold dùng `gold`) |
   | `status-learned`, `status-new`, `status-review`, `check` | viên trạng thái Wordbook `results.ts:340`: `new` (Learned) → `status-learned`; `fresh` (New) → `status-new`; `review` → `status-review`; `good` → `check`; `miss` không icon |
   | `retry` | nút Replay/Retry, `results.ts:356`. Nút "easier" không icon (`easier` chưa nhận) |

   **C. Chỉ chuẩn bị, chưa gắn (ghi lý do vào báo cáo):** `fast-forward`, `keyboard` (chỗ dùng ở `src/app`, ngoài phiếu); `seal-lit`, `seal-unlit`, `edge-arrow` (`src/ui/tags.ts`, ngoài phiếu); `lock` (giao diện chưa có chỗ khóa).
6. **Bỏ rêu CSS** `src/ui/styles/dh.css:87-118`: `.dh-panel::before`, `.dh-panel::after` và hai dòng chú thích.
   - Giữ biến `--dh-moss`, `--dh-moss-hi` (`app.css:91` còn dùng).
   - Bảng gỗ CSS giữ tới khi có khung vẽ (162).
   - Kiểm không quy tắc nào khác cần hai giả phần tử đó.
7. **Cỡ ô** (cạnh ở `--ui` = 1; 720p nhân 0,8, 1080p nhân 1,2):
   - mặc định 20 (16 / 24 px);
   - `retry`, `status-*`, năm ô số kết quả: 25 (20 / 30 px). Verdict 29/10b: `retry`, `status-learned` ≥ 20 px ở 720p;
   - sao: 46 (37 / 55 px);
   - loa và dấu đúng ở khung học: 18 (14 / 22 px); loa ở Thẻ Ôn: 22 (18 / 26 px);
   - `star-unlit` để nguyên ảnh: không vẽ ổ bằng CSS, không filter làm sáng. Ổ sao vẽ thật đến ở phiếu 196;
   - không thêm `filter`, `mix-blend-mode` hay `opacity` để đổi màu ảnh. Quy tắc trạng thái tắt, thiếu tiền đang có thì giữ và ghi lại.
8. **README** của game: một đoạn ngắn về `pnpm prepare-ui-art`. **Changelog:** `docs/changelog/<ngày>-ui-art-icons.md`.

## Test (viết trước)

1. **Bảng chọn:** 53 mục; 36 mục `accepted` khớp danh sách trên; 17 mục `interim`; tên và key không trùng. Mọi `name` và `key` qua `icon()` ra `<img>` đúng mẫu URL, có `width`, `height`, `decoding="async"`; không `<svg`, không emoji.
2. **Chỗ gọi:** gom mọi tên `icon()` mà `src/ui` dùng (chuỗi trong `icon("…")`, `SKILL_SLOTS`, `ULT_SLOT`, `kindIcon`, id món đặt, đồ dùng, nâng cấp rồng). Mỗi tên phải thuộc bảng hay danh sách `STILL_SVG` = `armour`, `dragon`, `white-dragon`, có ghi lý do trong test.
3. **Chọn cỡ:** ô 20 → `.64.webp`; ô 46 → `.128.webp`; ô 120 → `.256.webp`.
4. **Script, fixture trong `tmp/ui-art-test/`** (test tự dọn):
   - một icon có 64/128/256, một icon chỉ có 64/256;
   - ra ba WebP mỗi tên, đúng khổ, còn alpha; manifest khớp md5 và bytes;
   - `--check` thoát 0; đổi một byte thì thoát 1 và nêu file;
   - thiếu cỡ lớn hơn thì lỗi; file cũ và manifest cũ giữ nguyên byte.
5. **Ảnh lỗi:** hàm xử lý gọi `console.warn` một lần mỗi URL và ẩn ảnh.
6. **Không emoji:** chuỗi (string và template, cách đọc như `tests/english-ui.test.ts`) trong `src/ui/**/*.ts` và `content:` trong CSS của `src/ui/**` không có `\p{Extended_Pictographic}`, U+FE0F, U+2713, U+2714. Chú thích có dấu đúng thì đổi thành chữ.
7. **Khung học và kết quả:** markup dòng từ đã gõ và Thẻ Ôn có ảnh `check`, `speaker`, không còn ký tự cũ. Tách hàm thuần nếu cần để test.

## Cấm

- Mọi lệnh git có ghi.
- Sửa `src/kit/**`, `src/view/**`, `src/app/**`, `src/sim/**`, `src/content/**`, `src/ui/tags.ts`. Chạy đồng bộ kit.
- Dev server, trình duyệt, mạng.
- Ghi vào `games/dragon-hold` (checkout chính), trừ `public/assets/dragon-hold/ui/icons/` qua liên kết (mục Luật chung); ghi vào worktree khác (`.wt-dh-vfx`, `.wt-dh-keys`, `.wt-dh-models`, `.wt-dh-mappilot`, `.wt-td-*`, `.wt-ts-*`). Đụng game khác, Tu Tiên.
- Đưa ảnh vào Git. Ghi ra ngoài repo.
- Vẽ icon thay bằng SVG, CSS, canvas, emoji hay ký tự. Sửa ảnh nguồn. Sinh ảnh mới.
- Nút Settings, nút Sound trong trận (192, ảnh 180): không đụng. `speaker` của 138 chỉ dùng cho nút nghe từ và khung học.

## Kiểm (ghi số)

1. `pnpm check` xanh: số test trước và sau. Test thời gian đỏ khi máy bận thì chạy riêng ba lần.
2. Ván vàng: `tests/golden/golden.test.ts` xanh; md5 của `tests/golden/m0.json` trước và sau trùng nhau.
3. `tests/english-ui.test.ts` xanh.
4. `pnpm prepare-ui-art --art-src ../dragon-hold/art-src`: số file (53 × 3 WebP và manifest), tổng byte mỗi cỡ, PSNR nhỏ nhất mỗi cỡ, file nào phải lossless. Đầu ra vào `194/prepare.log`.
5. `pnpm prepare-ui-art --check --art-src ../dragon-hold/art-src`: thoát 0, đầu ra vào `194/check.log`.
6. `pnpm deploy:pack`: 0 lỗi; JSON vào `194/deploy-pack.json`; ghi số ảnh UI trong `dist/`.
7. **Tờ xem** `tmp/ui-art/194-sheet.jpg` của worktree (dưới 1 MB): 53 icon; mỗi icon có PNG nguồn và WebP cạnh nhau ở 64 px, trên vỏ cây `#2b2118` và kem `#f1e3c4`; tên dưới mỗi ô. Chỉ để Claude xem, không giao, không chép vào `docs` hay `public`.
8. **Bảng gắn:** mỗi tên trong 36 → chỗ gắn (file:dòng) hay "chỉ chuẩn bị" kèm lý do. Danh sách SVG còn lại trong `src/ui`: tên, file, dòng, chờ phiếu nào.
9. `git status --short -uall`: chỉ file của phiếu này (file của 187, nếu còn, ghi riêng). `git -C ../dragon-hold check-ignore -v public/assets/dragon-hold/ui/icons/<một tên>.64.webp public/assets/dragon-hold/ui/icons/manifest.json` (chạy ở checkout chính, vì trong worktree đường này nằm sau liên kết): cả hai bị bỏ qua. `src/ui/ui-art.json` không bị bỏ qua.
10. `194/media-files.txt`: đường, byte, md5 mọi file trong `public/assets/dragon-hold/ui/icons/`, cho `media:push` của Claude.

**Xong khi:** tám mục việc, bảy test và mười mục kiểm đạt. Claude duyệt diff, commit, rồi xem trên trình duyệt ở 1280 và 1920. Sau khi gộp vào `main`, Claude chạy lại `pnpm prepare-ui-art` ở checkout chính rồi `media:push`.

**Rủi ro (cho Claude):**
- 192 sửa `hud.ts` ở `.wt-dh-keys`; `dh-vfx` (V-dh2) sửa UI. Gộp theo thứ tự map-pilot → dh-vfx → dh-codex; chờ đụng độ ở `hud.ts`, `dh.css`.
- 17 icon kiểu cũ có thể lệch bộ cạnh bộ mới tới khi 163, 164 được nhận. Khi đó chỉ sửa bảng chọn.
