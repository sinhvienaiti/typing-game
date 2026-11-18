# Phiếu 211 · Last Line · Thay hình vẽ bằng mã (khóa CSS, đèn LED, sọc nguy hiểm, ký tự ★☆⚠⌨✓◀▶, thép chải) bằng icon 149–153 và khung 9-slice 127, kèm test quét

**Nguồn:**
- `AGENTS.md` (chủ dự án 28/10): "Nothing the player sees is a code-drawn stand-in for art: no SVG or canvas scenery, no CSS-shape icons, no emoji, no fallback paintings."
- `docs/games/map1/UI_IMAGERY.md` §5.3: bảng mọi chỗ Last Line vẽ bằng mã và ảnh thay. Ví dụ: "`survival.css:109-110` | ổ khóa CSS | `lock`"; "`src/view/theme.css:96-99`; `survival.css:16-25` | thép chải, 4 đinh, vát trên mọi bảng | khung 9-slice của AD".
- `docs/games/MAP1_PRODUCTION.md` §4.6, cổng G2: "quét không còn hình tạm (kể cả `?q=low`)".
- Chủ dự án 30/10: "tăng thêm việc cho codex cho tôi".

**Không trùng:**
- 127, 149–153: chỉ vẽ ảnh. Phiếu này chỉ gắn ảnh đã nhận.
- 206: đường ảnh UI của Last Line (bảng chọn, script chuẩn bị, `src/view/ui-art.ts`). Phiếu này dùng lại, không viết lại.
- 180, TF2, 191: nút Settings, nút Sound và bảng của chúng.
- Ngoài phiếu:
  - logo thay tên game phát sáng (121, LL-06);
  - trạm dựng bằng hình khối trong `scene.ts` (TS-M1-07, TS-M1-08, làn T);
  - mặt phím `keycap` (LL-11) và ô đạn `mag-*` (LL-40);
  - tấm dải chữ trên tàu `.sv-strip`: TF2 thay bằng dải chữ của kit.

**Báo cáo:** `docs/codex-queue/211-report.md` (repo cha, tiếng Việt), thư mục `docs/codex-queue/211/`.

## Chỉ chạy khi

Kiểm theo thứ tự. Thiếu một điều thì **dừng ngay**, ghi điều thiếu vào báo cáo, không sửa mã.

1. Có `docs/codex-queue/206-report.md`. Worktree `games/.wt-ts-art` có, nhánh `ts-art`.
2. Có đủ năm báo cáo `docs/codex-queue/149-report.md` … `153-report.md`.
3. Ít nhất một `docs/codex-queue/accept-*/verdict.md` ghi **Nhận** cho ít nhất một ảnh của 149–153 (tên và bản).
4. Một verdict ghi **Nhận** cho khung 127, ít nhất `panel-large`, và ghi đúng file được dùng.
   - `127-report.md`: cả chín `.alpha.png` còn pixel tím tối. Bản nhận có thể là một lượt tách nền mới.
   - Dùng đúng file verdict ghi. Không tự chọn `.alpha.png`.

Lúc kiểm phiếu (30/10 sáng) chưa điều nào đạt:
- 206 chưa chạy, chưa có `games/.wt-ts-art`;
- 149–153 chạy 30/10 khoảng 01:40–02:05 nhưng `image_gen` hết hạn mức (HTTP 429): 149, 150, 151, 153 chưa có ảnh; 152 có 7 bản chọn, chưa ai nhận. Cả năm phiếu đang chờ chạy lại trong làn `s1`;
- 127-report ghi chưa đạt (alpha còn tím); `accept-29-10`, `accept-29-10b` không chấm 127 hay 149–153.

Điều phối chỉ xếp phiếu này vào làn khi cả bốn điều trên đã đạt.

## Nơi làm

- Worktree `games/.wt-ts-art`, nhánh `ts-art`. Làn Codex `s1` (một làn), chạy sau 206 trên cùng nhánh.
- cwd của làn là repo cha (`.`). Lệnh git dùng `git -C games/.wt-ts-art`. Lệnh pnpm dùng `pnpm -C games/.wt-ts-art`. Script `node --import tsx …` chạy trong worktree.
- Trước khi làm, chạy `git -C games/.wt-ts-art status --short -uall` và `git -C games/.wt-ts-art branch --show-current`:
  - sạch: làm tiếp;
  - chỉ có file của 206 vì Claude chưa commit (đối chiếu `206-report.md`): làm tiếp, ghi danh sách vào báo cáo. Trước khi sửa một file mà 206 cũng sửa, chép nó vào `211/before/` để Claude tách hai phần;
  - có file khác, hay nhánh khác `ts-art`: dừng, ghi vào báo cáo.
- Ghi HEAD. Ghi nhánh đã có phần của 191 và TF2 chưa (có `src/view/type-fx.ts` không).
- **Ảnh vào, chỉ đọc:** `games/typing-survival/art-src/` của checkout chính. Worktree không có `art-src` (nằm ngoài Git).
- **Ảnh ra:** WebP do script chuẩn bị của 206 ghi vào `public/assets/typing-survival/ui/` **của worktree**. Media không vào Git.
- Số dòng dưới đây theo `main` `79db628`. Lệch thì tìm theo chuỗi.

## Luật chung (phiếu mã)

- Được dùng git chỉ đọc. Test trước, mã sau. Chú thích tiếng Anh, ngắn.
- Chữ người chơi thấy là tiếng Anh, kể cả `alt` và `aria-label`.
- Luật chơi, ván vàng `tests/golden/s0-trace.json`, mã băm chương và mã băm bộ bài `7f073fa2` không đổi.
- File tạm, fixture, tờ xem nằm trong `tmp/` của worktree (Git bỏ qua). Không ghi ra ngoài repo, kể cả thư mục tạm của hệ điều hành: chạy mọi lệnh `pnpm`, `node`, `magick`, `cwebp` với `TMPDIR` và `MAGICK_TEMPORARY_PATH` trỏ vào `tmp/os-tmp/` của worktree (tạo trước, xóa khi xong), như phiếu 206.
- Phiếu mã: không sinh ảnh, không sửa ảnh.
  - Script chỉ đổi định dạng và thu nhỏ Lanczos.
  - Không làm nét, đổi màu, phóng to, cắt, phủ hay xóa phần vẽ (`docs/games/ART_ACCEPTANCE.md` §5).
- Mức nhận ảnh là việc của Claude: M ≥ 8 theo game thương mại (`docs/games/ART_DIRECTION_2026-10-28.md` §1.3), Q ≥ 8 (`ART_ACCEPTANCE.md` §2.2). Codex không tự chấm, không tự nhận.

## Đọc trước (chỉ đọc)

- `206-report.md`:
  - tên và định dạng bảng chọn;
  - lệnh script chuẩn bị và cờ `--check`;
  - API của `src/view/ui-art.ts`: hàm dựng `<img>`, chọn cỡ, xử lý ảnh lỗi;
  - cách CSS lấy URL ảnh.
- Báo cáo 127, 149–153 và mọi `docs/codex-queue/accept-*/verdict.md`.
- `docs/games/map1/UI_IMAGERY.md` §4 (cỡ từng ô ở 720p / 1080p), §5.3, §8.
- `games/typing-survival/art-src/ui/frames-epic/*.json`: sáu JSON 9-slice (`size`, `slice`, `fill`). Theo 127-report, nguồn là mật độ 4×.
- Mã trong worktree:
  - `src/view/theme.css` (khối "Surfaces drawn in CSS", khoảng dòng 95–104), `src/view/survival.css`;
  - `src/view/screens.ts`, `src/view/screens-journey.ts`, `src/view/hud.ts`, `src/view/strip.ts`;
  - `src/app/journey.ts`, `src/app/menu.ts` (kiểu `MenuItem`);
  - `tests/theme.test.ts`, `tests/english-ui.test.ts`.

## Luật chọn ảnh

- Gắn một ảnh chỉ khi một verdict ghi **Nhận** cho đúng tên và đúng bản.
- Ảnh "Làm lại", chưa chấm hay đang làm thì không gắn, dù file đã có trong `art-src`.
- Vai chưa có ảnh nhận thì giữ nguyên mã cũ.
  - Ghi vào danh sách còn lại (Việc 7): "chờ ảnh <tên> (phiếu N)".
  - Không thay bằng SVG, CSS, ký tự hay chữ mới.
- §5.3 cho phép "bỏ" ba thứ: sọc dưới tiêu đề, chấm nhấp nháy, đèn LED. Không có ảnh nhận thì bỏ hẳn phần tử, không giữ hình CSS.
- Chỉ gắn ảnh của 127 và 149–153. `word-plate` và `portrait-ring` của 127 không dùng ở phiếu này.

## Việc

1. **Đưa ảnh vào đường của 206.**
   - Thêm mục cho mọi ảnh đã nhận vào bảng chọn của 206, đúng định dạng 206 đặt (nguồn, cỡ, phiếu nhận).
   - Icon 149–152 và mảnh 153: cỡ xuất theo hàm chọn cỡ của 206. `--ui` của Last Line là 1 ở 720p, 1,5 ở 1080p. Màn mật độ 2 cần ảnh ≥ 3 lần cạnh ô ở `--ui` 1.
   - Khung 127: script 206 chưa có loại khung thì thêm mục `frames`. Mỗi khung:
     - file nguồn đúng như verdict ghi;
     - `slice` chép từ JSON của 127;
     - WebP ở khổ gốc (1024 × 1024 hay 1536 × 512), giữ alpha, `-strip`, quality 90, alpha-quality 100;
     - PSNR dưới 35 dB thì xuất lossless file đó, ghi lại;
     - thư mục `public/assets/typing-survival/ui/frames/`.
   - `--check` báo lỗi khi `slice` trong bảng lệch JSON nguồn.
   - URL cho CSS theo đúng cách 206 chọn. 206 chưa có đường cho CSS thì:
     - đặt biến `--art-<tên>` và `--frame-<tên>` (`url()`) trong `theme.css` (luật `AGENTS.md` của game: mọi bề mặt là biến của `theme.css`);
     - một test so từng biến với bảng chọn (cùng file, cùng `?v=`). Không lập bảng URL thứ hai.
   - Không `import` ảnh vào bundle, không base64.
   - Chạy script để xuất. Log vào `211/prepare.log`; `--check` thoát 0, log vào `211/check.log`.

2. **Khung 9-slice thay thép chải, đinh, vát** (§5.3 dòng 1).
   - Gắn theo phần tử, không theo `.sv-panel`:

     | Phần tử | Khung |
     |---|---|
     | `.sv-card`: mọi thẻ màn (tựa, Options, Armory, Profile, Paused, thẻ trước trận, kết quả, Hành trình, thẻ ải, Nạp súng) | `panel-large` |
     | `.sv-hp`, `.sv-clock`, `.sv-kills`, `.sv-goal` | `plate-long` |
     | `.sv-slot`, `.sv-bay-lock` | `bay-card` |
     | `.sv-item`, `.sv-start` | `button`; khi `.is-on` thì `button-active` |

   - CSS mỗi hộp:
     - `border-style: solid`;
     - `border-image-source` là biến khung;
     - `border-image-slice` đúng bốn số của JSON, có `fill`;
     - `border-image-repeat: stretch`;
     - `border-image-width` theo cỡ góc dưới đây.
   - **Cỡ góc:** cạnh hiển thị = `slice / d × --ui` px.
     - `d` là số nhỏ nhất trong {4, 6, 8, 12, 16, 24} sao cho trên + dưới ≤ 50 % chiều cao nhỏ nhất của hộp và trái + phải ≤ 40 % chiều rộng nhỏ nhất.
     - Hộp có `height` hay `min-height` thì dùng số đó. Không có thì ước từ CSS: padding trên + dưới + cỡ chữ lớn nhất × 1,25.
     - Ghi phép tính từng hộp.
   - Hộp đã có khung:
     - `background-color: transparent` (màu nền vuông sẽ lộ ở góc trong suốt của tranh);
     - bỏ `border-radius` và hai bóng vát `inset`;
     - bóng đổ ngoài và vầng sáng trạng thái (`.is-active`, `.is-on`) giữ;
     - bỏ quy tắc màu viền không còn tác dụng (`border-left-color` của `.sv-item.is-on`, `.sv-start.is-on`).
   - Không đổi `padding`, `width`, `height`, `font-size`. Bố cục giữ nguyên.
   - Xóa `--brushed`, `--plate-light`, `--rivet`, `--rivet-size` và mọi chỗ dùng chúng khi mọi hộp dùng chúng đã có khung nhận. Hộp nào chưa có khung nhận thì giữ cho hộp đó, ghi vào danh sách còn lại.

3. **Sọc nguy hiểm** (§5.3 dòng 2, 3).
   - `.sv-hazard` dưới tiêu đề (`survival.css:26`; `screens.ts:69,79,88,100,111,120,129`; `screens-journey.ts:53,63,86`):
     - `divider` đã nhận: đổi lớp thành `.sv-divider`; cao `calc(14px * var(--ui))`, `background-size: 100% auto`, căn giữa;
     - không nhận: bỏ phần tử ở mọi chỗ.
   - `.sv-banner` (`survival.css:55`): bỏ `border-image: var(--hazard) 6`.
     - `banner` đã nhận thì làm đế: giữ tỉ lệ 3 : 1, chữ căn giữa nửa trên (127-report: đường sáng nằm nửa dưới).
     - Bề rộng đủ cho chuỗi băng rôn dài nhất trong 70 % giữa. Ước 0,62 em mỗi ký tự, cộng `letter-spacing`.
     - Gom mọi chuỗi đưa vào băng rôn (`hud.ts`, và `src/app/main.ts` chỉ đọc). Ghi chuỗi dài nhất và phép ước.
     - Không nhận thì chỉ bỏ sọc, giữ dải nền màu.
   - `.sv-slot::before`, `::after` (`survival.css:85-88`): bỏ sọc `--hazard-gun`.
     - `::before` (rãnh mờ): bỏ. Khung `bay-card` đã có đường trên.
     - `::after` là thanh nạp: giữ bề rộng theo `--load`, nền một màu `var(--gun)`.
   - Xóa `--hazard`, `--hazard-volt`, `--hazard-gun`, `--hazard-dim` khỏi `theme.css` khi không còn chỗ dùng.
   - `--segments` (mặt nạ thanh giáp và ô đạn) giữ; vào danh sách còn lại.

4. **Khóa, chấm, đèn** (§5.3 dòng 4, 5).
   - Ổ khóa bến (`hud.ts:160` `i.sv-lock`; `survival.css:109-110`): `<img>` `lock` (149), 24 / 36. Xóa hai quy tắc CSS vẽ ổ khóa.
   - Chấm nhấp nháy ở nhãn trạm (`screens.ts:66` `.sv-dot`; `survival.css:180`):
     - `station-crest` (150) đã nhận thì thay chấm, 20 / 30, không nhấp nháy;
     - không nhận thì bỏ chấm;
     - bỏ `.sv-dot` khỏi luật giảm chuyển động (`survival.css:278`).
   - Đèn mục menu (`screens.ts:47` `.sv-led`; `survival.css:195,198`):
     - `led-off`; mục đang chọn `led-on` (153), 8 / 12;
     - không nhận thì bỏ đèn. Mục chọn vẫn rõ nhờ `button-active` và vầng sáng.

5. **Ký tự làm icon** (§5.3 dòng 6). Cỡ là px CSS ở 1280 × 720 / 1920 × 1080.

   | Chỗ | Ký tự | Thay bằng | Cỡ |
   |---|---|---|---|
   | `screens.ts:44` giá trị cài đặt | ◀ ▶ | `arrow` (153); bên trái lật bằng `transform: scaleX(-1)`. Bỏ `.sv-item.is-on .sv-arrow` (`survival.css:204`, tô màu ký tự) | 12 / 18 |
   | `screens-journey.ts:120` hàng sao kết quả | ★ ☆ | `star-lit`, `star-unlit` (151); `alt` "Star earned", "Star not earned" | 28 / 42 |
   | `journey.ts:127` nhãn ải | ★ ☆ | trường mới `stars?: number` (0–3) của `MenuItem` (`src/app/menu.ts`). `item()` vẽ ba ảnh sao sau nhãn. Nhãn không còn ký tự. Ải khóa không có sao | 18 / 27 |
   | `screens-journey.ts:102` chip mối nguy chưa phủ | ⚠ | `warning` (150) | 16 / 24 |
   | `screens-journey.ts:106` "START · ⚠ UNCOVERED" | ⚠ | `warning` (150) trước "UNCOVERED" | 16 / 24 |
   | `hud.ts:377,380` `.sv-warn` báo Rift | ⚠ | `rift` (152) trước chữ "Rift" | 24 / 36 |
   | `hud.ts:386` đếm ngược cạnh dòng chữ | ◀ ▶ ⚠ | `strip.warn(text, side)` giữ chữ ký. `hud.ts` truyền chữ không ký tự ("Rift · 3.0 s"). `warn()` trong `strip.ts` thêm `rift` trước chữ và `arrow` về phía tường (`side < 0`: bên trái, lật) | 16 / 24 |
   | `survival.css:60` `.sv-notice::before` | ⌨ | `keyboard` (149): `content: ""`, ảnh nền từ biến | 16 / 24 |
   | `strip.ts:172,179` dòng xong | ✓ | `check` (149), một `<img>` sau chữ. `setDone()` nhận cờ, không nhận ký tự trong chuỗi | 16 / 24 |
   | `screens-journey.ts:43` câu luật học | ✓ | câu thành "… Finished words get a check mark."; `<dd>` thêm ảnh `check` ngay sau câu (chuỗi vẫn qua `escapeHtml`) | 16 / 24 |

   - `<img>` dựng bằng hàm của 206 (`src/view/ui-art.ts`): có `width`, `height`, `decoding="async"`, `draggable="false"`. Ảnh chỉ trang trí thì `alt=""` và `aria-hidden="true"`.
   - Không `filter`, `opacity` hay `mix-blend-mode` để đổi màu ảnh. `star-unlit` để nguyên ảnh. Quy tắc làm mờ cả mục tắt (`.is-off`) đang có thì giữ.
   - Ảnh lỗi khi tải: dùng bộ xử lý của 206 (`console.warn` một lần mỗi URL, ẩn ảnh). Không chữ, ký tự hay hình thay.
   - Mũi tên `↑ ↓ ← →` trong `<kbd>` là tên phím, không thuộc phiếu này (mặt phím LL-11).

6. **Hàng sao đọc được ở 28 px** (LL-50).
   - `.sv-star-row img`: `width` và `height` là `calc(28px * var(--ui))`.
   - Cỡ xuất ≥ 84 px (bản 128).
   - Bỏ `.sv-star-row b` và hai quy tắc tô màu ký tự (`survival.css:257,259`).
   - Nhãn dưới sao giữ cỡ chữ hiện có.

7. **Quét hình vẽ bằng mã.**
   - Module `scripts/no-code-drawn.ts` export `scan(root)`, trả danh sách `{ file, line, kind, text }`.
   - Chạy riêng: `node --import tsx scripts/no-code-drawn.ts --json <file>` ghi danh sách ra file.
   - Phạm vi: `src/**` trừ `src/kit/**`, và `index.html`.
   - **TS:** chỉ chuỗi (string, template), đọc bằng TypeScript như `tests/english-ui.test.ts`. Chú thích không tính.
     - Cấm `\p{Extended_Pictographic}`, U+FE0F;
     - cấm ★ ☆ ✓ ✔ ✕ ✗ ⚠ ⌨ ◀ ▶ ● ○ ■ □ ◆ ◇.
   - **CSS** (`src/view/*.css`, bỏ chú thích):
     - `content:` có ký tự ngoài ASCII;
     - `repeating-linear-gradient(`, `radial-gradient(`, `conic-gradient(`;
     - biến `--brushed`, `--rivet`, `--plate-light`, `--hazard*`;
     - `border-radius: 50%`;
     - selector `.sv-lock`, `.sv-dot`, `.sv-led` còn vẽ bằng `border` hay `background` không phải biến ảnh.
   - Danh sách cho phép `tests/no-code-drawn.allow.json` (vào Git). Mỗi mục có:
     - `file`, `kind`, `text` (chuỗi khớp, không theo số dòng), `count`;
     - `reason`;
     - `waits`: phiếu hay ảnh đang chờ, hay `"keep"`.
   - Mục `"keep"` theo §5.3 "Giữ": tia lửa phím `.sv-strip-spark`, viền đỏ `.sv-vignette`, màn che `.sv-overlay`, `--segments` của thanh đo.
   - Mục chờ: mọi vai chưa có ảnh nhận; `.sv-ledbar` (thanh âm lượng); `.sv-hints kbd` (LL-11); `.sv-mags i` (LL-40); tên game phát sáng (121).
   - Test đỏ khi:
     - có khớp không trong danh sách;
     - số khớp vượt `count`;
     - mục trong danh sách không còn khớp (danh sách phải luôn đúng).

**Changelog:** `docs/changelog/<ngày>-no-code-drawn.md` của game (tiếng Việt): dòng §5.3 nào đã thay, bằng ảnh nào của phiếu nào, chỗ còn chờ, số đo ở mục Kiểm.

## Test (viết trước, ghi số đỏ trước khi sửa mã)

1. `tests/no-code-drawn.test.ts` (mới): quét ở Việc 7.
   - Chạy lệnh `--json` trên mã chưa sửa, lưu `211/remaining-before.json`.
   - Sau khi sửa, lưu `211/remaining-after.json`.
2. `tests/ui-art-wiring.test.ts` (mới). Test hàm dựng chuỗi (`menu`, `renderScreen`, `renderJourney`, hàm hàng sao) và hàm thuần tách ra từ `hud.ts`, `strip.ts`:
   - mục có giá trị: hai ảnh `arrow`, ảnh trái có lớp lật; không ◀ ▶;
   - mục chọn có `led-on`, mục khác `led-off` (hay không đèn khi ảnh chưa nhận);
   - hàng sao: ba `<img>`; số `star-lit` bằng số sao; không ★ ☆;
   - nhãn ải: không ★ ☆; ải mở có ba ảnh sao; ải khóa không sao;
   - chip mối nguy chưa phủ và nút START có `warning`; không ⚠;
   - báo Rift: chữ không ⚠ ◀ ▶; có `rift`; mũi tên đúng phía theo `side`;
   - dòng xong: có `check`; chuỗi không ✓;
   - bến khóa ra `lock`.
   - Cần DOM thì viết stub nhỏ bằng tay. Không thêm gói (jsdom, happy-dom).
3. `tests/theme.test.ts`:
   - dòng 33 đòi `--hazard`, `--rivet`. Đổi theo nghĩa: đòi biến các khung đã gắn. Ghi lý do;
   - thêm: mỗi `border-image-slice` trong CSS bằng `slice` của khung đó trong bảng chọn;
   - thêm: `border-image-width` đúng `slice / d` theo bảng ở Việc 2.
4. Test của 206 và mọi test khác vẫn xanh. Test so ký tự hay lớp đã bỏ thì đổi theo nghĩa. Ghi từng test đã đổi và lý do.

## Cấm

- Mọi lệnh git có ghi; sửa `src/kit/**`; chạy `kit:sync`.
- Dev server, trình duyệt, mạng. Thêm gói npm.
- Sửa các file đang thuộc làn khác:
  - `src/app/main.ts`, `input.ts`, `quick.ts`, `settings.ts`, `keyboard.ts` (191);
  - `src/view/type-fx*.ts`, `typing-feel.ts` (TF2);
  - `src/audio/**`, `src/sim/**`, `src/content/**`, `src/view/scene.ts`.
- Đổi tấm `.sv-strip` hay dải chữ của kit. Trong `strip.ts` chỉ sửa `warn()` và `setDone()`.
- Đụng nút Settings, nút Sound và bảng của chúng (180, TF2, 191).
- Gắn ảnh chưa có dòng **Nhận**. Gắn ảnh ngoài 127 và 149–153.
- SVG, canvas, emoji, ký tự, gradient hay hình CSS thay ảnh thiếu. Thêm trang trí CSS mới.
- Sửa, chép đè, xóa file trong `art-src`. Đưa ảnh vào Git. Xử lý ảnh làm đổi phần vẽ (§5).
- Ghi vào `games/typing-survival` (checkout chính), worktree khác (`.wt-ts-typefx`, `.wt-ts-codex`, `.wt-ts-vfx`, `.wt-play-*`, `.wt-dh-*`, `.wt-td-*`), game khác.
- Đụng Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`).
- Sửa tài liệu repo cha (`docs/games/**`). Claude cập nhật §5.3 sau.
- Ghi ra ngoài repo.

## Kiểm (ghi số)

1. `pnpm check` xanh: số file test, số test trước và sau, số file `verify-kit`. Test thời gian đỏ khi máy bận thì chạy riêng ba lần.
2. **Ván vàng:**
   - sha256 `tests/golden/s0-trace.json` trước và sau trùng;
   - `node --import tsx scripts/chapter-hashes.ts` trước và sau, lưu `211/chapter-before.txt`, `211/chapter-after.txt`; `diff` rỗng;
   - `tests/vocab-pin.test.ts` xanh.
3. **Gói:** `pnpm deploy:pack` trước và sau. Chạy `node src/kit/tools/deploy/check-pack.mjs dist --game typing-survival --json` trên mỗi `dist`, lưu `211/pack-before.json`, `211/pack-after.json`. Không lỗi mới; đếm theo loại.
4. **Quét:** số khớp trước và sau theo loại; danh sách còn lại kèm lý do.
5. **Bảng §5.3:** mỗi dòng → ảnh (tên, bản, phiếu, file verdict và dòng) → trạng thái: "đã thay", "bỏ (§5.3 cho phép)", "chờ nhận", "ngoài phiếu".
6. **Bảng khung:** phần tử → khung → `slice` → `d` → cạnh góc hiển thị ở `--ui` 1 và 1,5 → cỡ hộp dùng để tính.
7. **Tờ xem** `tmp/ui-art/211-sheet.jpg` của worktree (dưới 1 MB):
   - mỗi khung dựng 9-slice theo `slice` và `d` **đọc từ CSS** (không gõ tay), ở cỡ hộp của Việc 2, `--ui` 1 và 1,5, trên `#14181f`;
   - mỗi icon ở cỡ CSS, trên `#14181f` và `#8c96a3`;
   - hàng sao ở 28 và 42 px; cặp mũi tên (trái lật);
   - tên dưới mỗi ô.
   - Tờ chỉ để Claude xem. Không chép vào `docs` hay `public`.
8. **Media:** `211/media.txt` liệt kê mọi file script ghi vào `public/assets/typing-survival/ui/` (đường, khổ, byte, md5) và tổng kB thêm cho lần chơi đầu. `git check-ignore -v` cho một WebP: bị bỏ qua. Claude chạy `media:push`.
9. **Chữ:** liệt kê mọi chuỗi mới người chơi thấy hay trình đọc màn hình đọc (`alt`, `aria-label`): tiếng Anh. `tests/english-ui.test.ts` xanh.
10. **Phạm vi:**
    - `git -C games/.wt-ts-art status --short -uall`: chỉ file của phiếu này, cộng `docs/changelog/<ngày>-no-code-drawn.md`. File 206 chưa commit (nếu có) ghi riêng;
    - `git diff --check` sạch;
    - `grep` các file đã sửa: không `<svg`, emoji, `gradient` mới.
11. **Kịch bản trình duyệt** đọc nền bến hay lớp đã bỏ: liệt kê file, dòng, lý do. Ví dụ f8 ở `scripts/visual/scenarios/survival-feel.mjs:458-470` đọc alpha nền bến. Không sửa, không chạy.

**Xong khi:** bảy việc, bốn test và mười một mục kiểm đạt, có số trong báo cáo. Claude duyệt diff, commit, rồi xem trên trình duyệt ở 1280 và 1920 mọi màn: tựa, Options, Armory, Profile, Hành trình, thẻ ải, Nạp súng, thẻ trước trận, HUD trận (cả bến khóa và báo Rift), Paused, kết quả. Sau khi gộp, Claude chạy lại script chuẩn bị ở checkout chính rồi `media:push`.

**Rủi ro (cho Claude):**
- Đổi khung chạm mọi màn. Codex không thấy bố cục; tờ 9-slice chỉ là ước. Góc đè chữ hay góc teo ở hộp nhỏ (`d` tới 24) chỉ thấy trên trình duyệt.
- `ts-typefx` (191, TF2) cũng sửa `hud.ts`, `strip.ts`, `survival.css`, `theme.css`. Phiếu này chỉ chạm `updateWarn` và dòng khóa bến trong `hud.ts`, `warn()` và `setDone()` trong `strip.ts`. Báo cáo ghi từng khúc để gộp.
- Phiếu bị chặn tới khi Claude nhận ảnh 149–153 và khung 127.
- Mật độ 4× của khung là giả định của 127-report. Claude chốt `d` sau khi xem.
