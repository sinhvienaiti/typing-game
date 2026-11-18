# Phiếu 232 · Wordwoven · Kiểm lại độc lập 200 và 203 phần A

Ngày 30/10/2026. Claude làm thay Codex (chủ dự án 15:25: tạm dừng Codex). Chỉ đọc: không sửa mã, ảnh hay golden của 200 và 203. Mọi lệnh `pnpm` chạy trong bản chép. Không dùng dev server, trình duyệt hay mạng.

## 1. Bảng tổng

| Phiếu | Kết luận | P0 | P1 | P2 | P3 |
|---|---|---:|---:|---:|---:|
| 200 · ảnh màn tựa và thẻ kết | **Commit sau khi sửa** F1 (và nên sửa F2), rồi kiểm trình duyệt | 0 | 1 | 1 | 1 |
| 203 A · năm sửa C10 | **Commit được về kỹ thuật**; nên sửa F3–F5 trước khi gửi giám khảo C10 | 0 | 0 | 3 | 1 |

Mọi số mà hai báo cáo ghi đều đo lại khớp (mục 3). Các phát hiện đều là chỗ mà test Node không thấy.

## 2. Điều kiện, mốc, bản chép

- Có `200-report.md` và `203-report.md`. `.wt-td-ui` ở nhánh `td-ui`, HEAD `2a1f61d7da2e…`.
- Lượt 14:47 và lượt chạy lại 15:13–15:20 bị cắt. Đã xóa `tmp/codex-232/` (70 MB) và `232/` (43 file) đúng theo ghi chú chạy lại. Lúc bắt đầu chưa có `232-report.md`.
- `status --short -uall` có **25 đường**: 13 của 200 và 12 của 203. **0 đường lạ, 0 đường thiếu.** `diff --check` exit 0. `diff --quiet -- src/kit src/sim src/typing src/content tests/golden` exit 0. Không có file chưa theo dõi trong các thư mục đó.
- 203 không đụng file của 200: `td.css` trùng ảnh chụp đầu lượt 203 (`203/200-diff-before.json`). 11/11 SHA-256 trong `203/verification.json` trùng file hiện tại.
- Bản chép dựng theo 224 §"Dựng bản chép":
  - 372 file `ls-files -co` khớp 372/372 SHA-256;
  - `public/` chép bằng `rsync -aL`, 163 file (ground và ui là nội dung thật);
  - `node_modules` là thư mục thật, có 11 symlink;
  - sáu ảnh nguồn chép vào `art-src/ui` để chạy `--check`.
- Hai bản phụ để tách số:
  - `tree-200` là bản chép đã trả 12 đường của 203 về HEAD;
  - `tree-base` là HEAD; 0 file theo dõi lệch HEAD.
- Môi trường: Node 24.22.0, pnpm 11.21.0. Bằng chứng: [before.json](232/before.json), [copy.json](232/copy.json).

## 3. Số chạy lại cạnh số báo cáo

| Kiểm | Báo cáo | 232 đo lại |
|---|---:|---:|
| `pnpm check` HEAD | 392 test (suy ra) | **42 file / 392 test**, exit 0 |
| `pnpm check` chỉ có 200 | 43 / 405 | **43 / 405**, exit 0, kit 42/42 |
| `pnpm check` có 200 và 203 | 46 / 426 | **46 / 426**, exit 0, kit 42/42, 12,3 s |
| Gói `/`: HEAD → 200 → 203 (byte gzip, trần 85.000) | 81.583 → 82.314 → 83.233 | **81.583 → 82.314 → 83.233**, còn dư 1.767 |
| Gói `/?title=0` | 83.041 → 83.754 → 84.677 | **83.041 → 83.754 → 84.677**, còn dư **323** |
| Phần 3D (trần 260 kB) | 171,83 → 172,347 kB | **171.833 → 172.347 B** |
| Dòng `.ts` ngoài kit (trần 16.500) | 13.101 → 13.231 | **13.060 (HEAD) → 13.101 → 13.231** |
| Golden | 2/2 `same:true` | **2/2 `same:true`**, `changed {}`, 19.660 tick / 389 lệnh; boss 5.695 / 49 |
| `prepare-ui.mjs --check` | exit 0 | **exit 0**; chạy thêm một lần: `0 written, 16 fresh` |
| Media 16 file | 1.121.340 B | **1.121.340 B**; 16/16 đúng px, byte và md5 so với `200/media.json` |
| Hai nền ≤ 400 kB | 256.422 / 332.700 | **256.422 / 332.700** |
| `node --check` cho hai kịch bản và script ảnh | exit 0 | **exit 0 ×3** |
| Quét emoji (203) | 20 file, 23 lần khớp, 19 cặp | **20 / 23 / 19** (bộ đếm riêng) |
| Lưới A1 và ca A2 | 1.128 hộp, 24 ca | tính lại 21×18 + 30×25 = **1.128**; 4×3×2 = **24** |

Gói `/?title=0` chỉ còn dư 323 B, nên việc sau trên đường vào thẳng sẽ chạm trần. Bằng chứng: [check.json](232/check.json), [check.txt](232/check.txt), [golden.txt](232/golden.txt), [prepare-ui.txt](232/prepare-ui.txt).

## 4. Phiếu 200, đọc diff và ảnh

- **Chỉ gắn ảnh đã nhận:**
  - logo và huy hiệu: `ui/title-epic/logo.alpha.png` và `emblem.alpha.png` có md5 trùng `_review/113/delivery-alpha/` (`56cfaf90…`, `e17611b2…`);
  - nền: `title-backdrop.v2.png` `4a526c42…`, khác bản bị trả `title-backdrop.png` `16950b69…`;
  - phiếu 115: dùng 3/4 ảnh không 9-slice được nhận (crest, banner, divider; không dùng portrait-ring). md5 trùng `_review/115/corrected*/`. Không dùng khung 9-slice nào.
- **Ảnh xuất làm lại độc lập:** dựng lại 16 file bằng đúng các bước ImageMagick vào thư mục tạm. 14/16 trùng byte. Hai favicon PNG khác byte (siêu dữ liệu PNG) nhưng 0 điểm ảnh khác (`compare -metric AE` = 0). Ba lần cắt alpha khớp `ui-picks.json`. Sáu nguồn có md5 trùng `200/sources-md5.json`. Xem [media-audit.json](232/media-audit.json).
- **Media không vào Git:**
  - `ls-files` có 0 file media;
  - 17/17 file trong `ui/` bị `check-ignore` (luật `public/assets/**`);
  - repo game không theo dõi file nào trong `ui/`.
- **URL:** `title-dusk` xuất hiện 0 lần trong `src/` và `index.html`. Tiền tố `/assets/typing-defense/ui/` chỉ có ở `src/ui/art.ts` và `index.html`.
- **Không vẽ bằng mã thay ảnh:** 0 dòng thêm có `svg`, gradient, `getContext` hay hình CSS. Ảnh lỗi thì bị ẩn. Khi ảnh lỗi chỉ hiện chữ "Wordwoven", đúng như phiếu cho phép.
- **Chữ người chơi thấy là tiếng Anh.**
- **Logo:** lề alpha trên đo được 153 px trên ảnh 2172 px, khớp mức bù 3,17vw trong `title.css`.
- **Lỗi:** F1 và F2 ở mục 6.

## 5. Phiếu 203 phần A, đọc diff và đột biến

- **Hàm thuần có test riêng:**
  - A1 dùng `keepIn` và `comboSide`;
  - A2 dùng `trayPointer`;
  - A3 dùng `typedShown`;
  - A4 dùng `rimAt`;
  - A5 dùng `stampStep`.

  Các hàm này không dùng DOM hay three. Phần đọc DOM nằm riêng ở `dom.ts`.
- **Mã mép khay khớp hướng:** `words.ts:164` đặt 0 trái, 1 phải, 2 trên, 3 dưới; pháp tuyến trong `trayPointer` theo đúng thứ tự đó.
- **Không đổi luật chơi, sim, bộ định tuyến hay golden.** 203 cũng không sửa ngoài vùng phiếu: không đụng README changelog hay BUILD_NOTES.
- **Bỏ nhánh lock/switch đóng dấu nhiều thẻ:** không làm mất gì. Theo `router.ts`, chỉ cặp bậc 2 mới có hai từ cùng chữ đầu.
- **Đột biến trong bản chép:** 9 lên năm sửa và 1 lên 200. Cả 10 đều đã trả lại; bản chép trùng 372/372 SHA-256 sau đó.

| # | Sửa | Đột biến | Đỏ / tổng | Bắt? |
|---|---|---|---:|---|
| M1 | A1 | `keepIn` bỏ kiểm hộp HUD | 7/18 | có |
| M2 | A1 nối | bỏ `fitElement(card.el…)` trong `draw` | 0/22 | **không** |
| M3 | A2 | giới hạn hướng 60° → 90° | 1/18 | có |
| M4 | A2 | cánh V lệch 0,8× | 2/18 | có |
| M5 | A3 | `draw` bỏ `typedShown` | 1/18 | có |
| M6 | A4 | nét cứng chỉ 1 khung (`t<17`) | 2/18 | có |
| M7 | A4 nối | `burst` bỏ outline cứng | 0/20 | **không** |
| M8 | A5 | tắt ở 67 ms thay 66 | 3/18 | có |
| M9 | A5 nối | dấu bắt đầu trễ 17 ms | 2/18 | có |
| M10 | 200 | thẻ thua mất `is-lost` | 1/13 | có |

Bảng chi tiết ở [mutations.json](232/mutations.json).

## 6. Phát hiện

Chi tiết từng phát hiện ở [findings.json](232/findings.json). Đường dẫn dưới đây tính từ `games/.wt-td-ui/`.

**F1 · P1 · 200 · `src/ui/td.css:217, 228–229`, `src/ui/theme.css:50`.**
- Lỗi: hộp tiêu đề cố định 84 px, còn 56 px khi cao ≤ 800 px. Nhưng banner cao 84,15 px (340 px rộng), hay 74,25 px (300 px rộng).
- Thêm vào đó, gạch son `.vd-sheet h2::after` (4 px + lề 4 px) thành hàng lưới thứ hai.
- Kết quả: nội dung tràn khoảng **26 px ở 1280×720** và 8 px ở 1920×1080. Tiêu đề có `position: relative`, nên phần tràn vẽ đè lên dòng sau: sao khi thắng, dòng gợi ý khi thua.
- Số này tính từ CSS, chưa đo trên trình duyệt.
- Tái tạo: `td-theme` ở 1280×720, thẻ thua. So `.td-result-banner` `.bottom` với `.td-hint-line` `.top`.
- Sửa:
  - `.td-result-heading` dùng `height: auto` hoặc `min-height`; hoặc cho banner `height: 56px; width: auto`;
  - thêm `.td-result-heading::after { content: none }`;
  - `td-theme` kiểm đáy banner ≤ đỉnh dòng sau.

**F2 · P2 · 200 · `src/ui/td.css:217`, `src/ui/sheets.ts:100`.**
- Lỗi: chữ tiêu đề màu `#fff3d6` chỉ đọc được khi có banner. Lúc banner đang tải, hay bị lỗi và ẩn, chữ nằm thẳng trên giấy.
- Tương phản: **1,01 : 1** trên `#fff4d6`, 1,09 trên `#f5e9cc`, 1,33 trên `#e6d4ab`. Mực `#2b2118` đạt 10,8–14,4 : 1.
- Sửa: tiêu đề mặc định màu mực. Callback `loaded` của `bindArt` thêm lớp `has-banner`; chỉ đổi sang màu kem khi có lớp đó. Test: banner lỗi thì không có lớp `has-banner`.

**F3 · P2 · 203 · `src/view/words/feel.css:5`, `cards.ts:307–333`.**
- Lỗi: dấu chữ có cỡ riêng `clamp(26px, 30px*--ui, 32px)`. Chữ trên thẻ là `clamp(18px, 22px*--ui, 24px)`.
- Vì vậy trước khi nhân bậc, dấu đã to **1,44×** chữ (720p) và 1,33× (1080p).
- Khung đầu thực tế 3,47× / 3,20× thay vì 2,4×.
- Ở bậc "1,0" (50–66 ms), dấu vẫn to 1,11–1,44× chữ bên dưới, tùy thẻ đang phóng 1,0–1,2×.
- Bản cũ dùng `::before` nên kế thừa đúng cỡ chữ.
- Sửa: lấy cỡ chữ từ `.k` (`getComputedStyle(source).fontSize`), hoặc nhân `scale` với chiều cao rect của chữ / chiều cao của dấu. Test: chữ nguồn 18 px thì ở t = 50 dấu cao 18 px.

**F4 · P2 · 203 · `cards.ts:144`, `feel.css:3,5`.**
- Lỗi: bậc chuỗi không còn đổi dấu sang màu vàng. Mã không còn đặt `--tier`; `--tier: 0` không còn ai đọc; quầng của `.td-key-stamp` cố định `#7ff5e0`.
- Bản cũ trộn màu sang `#ffc75c` theo bậc. Phiếu A5 ghi "`--tier` cộng thêm như nay"; hiện chỉ giữ phần cỡ.
- Sửa: đặt lại `--tier` khi có sự kiện `chain` và trả `color-mix` vào `.td-key-stamp`. Test: CSS của dấu dùng `var(--tier)`.

**F5 · P2 · 203 · `tests/td-c10-r5.test.ts`.**
- Lỗi: M2 (bỏ kẹp thẻ ở `cards.ts:288`) và M7 (bỏ outline ở `cards.ts:107`) vẫn xanh.
- Sửa, thêm hai test:
  - `draw()` với một thẻ cắt hộp chip: kỳ vọng có `translate` và `card.x` bị dời;
  - `read()` một `wordHit`: kỳ vọng `outline` chứa `#FFF0D8` và `outlineOffset` bằng `out − width`.

**Ghi chú P3:**
- **N1 (203, `3d/words.ts:499`, `dom.ts:5–6`):** mỗi khung, `fitElement` ghi rồi đọc `getBoundingClientRect` cho từng thẻ, dấu và chữ bay. Chữ sai giữ `opacity: 1` inline sau khi WAAPI đã tắt, nên bị đo mãi. Cần đo thời gian khung.
- **N2 (200, `prepare-ui.mjs:44–47`):** `--check` chỉ so mtime. File sai cỡ mà mới hơn nguồn vẫn qua.

## 7. Cần trình duyệt của Claude

- **Màn tựa ở 1280×720 và 1920×1080 (`td-theme`):**
  - logo rộng 0,45, mép vẽ ở khoảng 5,5vh;
  - phụ đề kem và dòng `.tt-keys` còn đọc được, vì lớp tối toàn tranh đã bỏ;
  - góc trên phải trống khoảng 200×90 cho phiếu 193;
  - favicon 200 `image/png`;
  - nền lỗi thì nền phẳng `#1c1824`.
- **Thẻ kết ở hai cỡ:**
  - F1: đo đáy banner và gạch son so với sao và dòng gợi ý;
  - chữ "Village saved" và "Fort fallen" có chạm huy chương hai đầu banner không;
  - thẻ thắng có 5 từ ôn không phải cuộn ở 720p;
  - chữ 13 px của khối ≤ 800 px còn đọc được không;
  - crest lúc thua (`grayscale 0.5`, `brightness 0.75`) còn đọc là thua không;
  - F2: chặn URL banner rồi xem tiêu đề.
- **Thẻ chữ sau năm sửa (`td-1c-words` High, hai cỡ):**
  - `key-dark` và `key-multi`: cỡ dấu so với chữ (F3), màu theo bậc (F4), dấu hiện ngay khung phím;
  - `word-dark`: tỷ số sáng khung đầu / đỉnh ≥ 0,95. Nét 4–6 px giữ đủ sáng tới khoảng 169 ms rồi tắt hẳn trong một khung; xem có thành cú "pop" không;
  - `combo`: ×N đủ dấu ×;
  - `tray-in`, `tray-type`, `tray`: V ở mép trái và mép dưới;
  - số khung `boxAudit.overHud` và `offScreen`. Bộ đo chạy mỗi rAF với `getComputedStyle`, có thể làm nặng khung; so thời gian khung khi có và không có nó (N1).

## 8. Dọn và phạm vi

- `find games/.wt-td-ui games/typing-defense/public -newer marker`: **0 dòng**. Đo lại sau khi xóa bản chép: vẫn 0.
- Worktree giữ nguyên:
  - status 25 dòng, trước = sau;
  - 372/372 SHA-256 bằng nhau;
  - `node_modules` vẫn 14 mục;
  - mtime `results.json` của Vitest không đổi.
- 17 file `ui/` của checkout chính có md5 không đổi. 0 file mới hơn marker trong `art-src/ui/title-epic`, `frames-epic` và `_review/113`.
- Đã xóa `games/typing-defense/tmp/codex-232` (197 MB, gồm ba cây chép và 16 ảnh dựng lại); lệnh `ls` xác nhận đã mất. Không có khung chụp nên không cần `capture-prune`.
- Repo cha: dòng mới của phiếu này chỉ có `docs/codex-queue/232/` (12 file, 76 KB) và báo cáo này. Dòng mới của làn khác (230, 234, `learning-sample-types`, `portal/tests/learning-bridge.test.mjs`) không đụng. Xem [cleanup.json](232/cleanup.json).
- Không có tờ JPG: các phát hiện đã đo được bằng số.

## 9. Việc của Claude

1. Sửa F1 và F2 trong `td.css` (cùng `sheets.ts` nếu dùng lớp `has-banner`). Chạy `td-theme` ở hai cỡ. Chạy `media:push` theo `200/media.json`, rồi commit 200.
2. Với 203: sửa F3, F4 và thêm hai test của F5 (nhỏ, cùng vùng `words/`). Hoặc commit nguyên trạng rồi mở phiếu sửa. Chạy `td-1c-words` ở hai cỡ, gửi hai giám khảo C10 mức 8.
3. Sau đó gộp `td-keys` (193) vào `td-ui` và giải xung đột màn tựa như phiếu 200 đã ghi.
