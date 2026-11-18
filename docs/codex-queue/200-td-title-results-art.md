# Phiếu 200 · Wordwoven · Gắn ảnh đã nhận vào màn tựa và thẻ kết (nền 158, logo và favicon 113, crest, banner, divider 115)

> **Chạy lại (30/10, 12:58, điều phối):** lượt 11:54 đã gắn mã và xuất media nhưng chưa chạy kiểm. Các file chưa commit trong `games/.wt-td-ui` là việc của chính phiếu này; giữ nguyên. Chạy đủ mục kiểm: `pnpm check`, ngân sách gói trước và sau (mốc trước lấy bằng cách build ở `2a1f61d` trong `tmp/`, hoặc dùng số của `td-1c` nếu phiếu đã ghi), sửa nếu đỏ. Các lệnh kiểm của phiếu (`pnpm check`, build, đo gói, toàn bộ test) là **bắt buộc**. Điều phối Claude cho phép thay chủ dự án; điều này thắng mọi luật chung kiểu "không chạy build hay toàn bộ test suite". Không hỏi lại, cứ chạy và ghi số.

**Nguồn:**
- `docs/HANDOFF_CURRENT.md` §3: "Ảnh đã nhận, chờ gắn … 158 `title-backdrop.v2` (cắt 16:9 `1536x864+0+80`, logo `logo.alpha.png` khoảng 45 % rộng) … Chưa có làn gắn ảnh UI".
- `docs/games/map1/UI_IMAGERY.md` §3.1 và §3.7:
  - WW-01: dòng nạp cần "logo nhỏ 120 / 180 rộng";
  - WW-02: "favicon 32 / 64 … cắt từ huy hiệu 113";
  - WW-03: nền màn tựa là "ảnh chủ đạo sử thi, toàn màn";
  - WW-08: tên game là logo "Wordwoven";
  - WW-56: "huy hiệu thắng/thua … AD 115 `crest`".
- Chủ dự án 28/10 (`AGENTS.md`): mọi chi tiết UI có ảnh thật; không hình vẽ bằng mã, không tranh dự phòng.
- Chủ dự án 29/10: "tăng thêm việc cho codex cho tôi".

HANDOFF định giao việc gắn 158 và 115 cho làn Wordwoven kế của Claude. Nay phần màn tựa và thẻ kết chuyển sang Codex.

Không trùng: 113, 115, 158 (chỉ vẽ ảnh); 177 (biểu tượng ứng dụng, chỉ vẽ); 132 (chữ tiếng Anh, bỏ hình vẽ bằng mã ở màn tựa); 193 (nút Settings và loa).

**Báo cáo:** `docs/codex-queue/200-report.md` (tiếng Việt), thư mục `docs/codex-queue/200/`.

**Chỉ chạy khi** Claude đã:
- cắt worktree `games/.wt-td-ui`, nhánh `td-ui`, từ `td-1c` `2a1f61d`;
- liên kết `art-src/*` và `public/assets/typing-defense/*` như ở `games/.wt-td-1c` (ví dụ `public/assets/typing-defense/ui` trỏ tới `games/typing-defense/public/assets/typing-defense/ui`);
- chạy `pnpm install` trong worktree đó.

Chưa có thì dừng, ghi vào báo cáo.

## Nơi làm

- Worktree `games/.wt-td-ui`, nhánh `td-ui`. Làn Codex duy nhất (chủ dự án 30/10: một làn), chạy sau 199. cwd của làn là repo cha (`.`); lệnh `pnpm` chạy trong worktree.
- `git status --short -uall` phải sạch trước khi làm. Được dùng git chỉ đọc.
- Đường dẫn mã trong phiếu tính từ gốc worktree.
- Ghi media qua liên kết `public/assets/typing-defense/ui/` là đúng. Media đó dùng chung với cây chính; Claude chạy `media:push` từ đó.
- **Đọc trước (chỉ đọc):**
  - `docs/codex-queue/accept-29-10b/verdict.md` mục "158" và "Sẵn sàng gắn";
  - `docs/codex-queue/accept-29-10/verdict.md` mục 113 (logo, emblem) và 115 (crest, banner, divider);
  - mock vị trí logo: `games/typing-defense/art-src/_review/158/title-mock.jpg`;
  - `docs/games/ART_ACCEPTANCE.md` §5 (hậu kỳ không phá tranh); `accept-29-10b/verdict.md` mục 158, đoạn "Ruộng vàng chanh: không chặn" (hàng 158 trong `docs/games/ART_REPLACE_LATER.md` do Claude thêm, có thể chưa có);
  - mã: `src/ui/title.ts`, `title.css`, `sheets.ts`, `td.css` (dòng 190–215), `index.html`, `src/main.ts` (dòng nạp, quanh dòng 150);
  - mẫu: `scripts/td/prepare-ground.mjs` (script media), `tests/td-sheet-cards.test.ts` (test HTML không cần DOM);
  - kiểm: `scripts/bundle-budget.mjs`, `scripts/visual/scenarios/td-theme.mjs`.

## Ảnh vào và đầu ra

Mọi ảnh vào đã nhận (M ≥ 8, Q ≥ 8, `ART_ACCEPTANCE.md`). Phiếu này không vẽ lại ảnh nào.

Nguồn ở `art-src/ui/` (chỉ đọc). Đầu ra ở `public/assets/typing-defense/ui/`: WebP, riêng favicon là PNG.

| Tên | Nguồn | Nhận | Bước công cụ | File ra (px) | Cỡ hiện, px CSS (720p / 1080p) |
|---|---|---|---|---|---|
| `title-backdrop` | `title-epic/title-backdrop.v2.png` 1536 × 1024 | 158: M 8, Q 8,5 | cắt `1536x864+0+80` | `title-backdrop.1280.webp` 1280 × 720; `title-backdrop.1536.webp` 1536 × 864 | toàn màn, `cover` |
| `logo` | `title-epic/logo.alpha.png` 2172 × 724 | 113: M 8,5, Q 9 | không cắt (mock 158 đo trên file nguyên) | rộng 180, 360, 576, 864, 1296, 1728 | màn tựa 45 % rộng màn (576 / 864); dòng nạp 120 / 180 |
| `favicon` | `title-epic/emblem.alpha.png` 1024 × 1024 | 113: M 8, Q 9 | cắt sát alpha, đệm thành vuông | `favicon-32.png`, `favicon-64.png` | tab trình duyệt |
| `crest` | `frames-epic/crest.alpha.png` 1024 × 1024 | 115: M 8,5, Q 9,5 | không | `crest.128.webp`, `crest.256.webp` | 96 / 128 |
| `banner` | `frames-epic/banner.alpha.png` 1536 × 512 | 115: M 8,5, Q 9 | cắt sát alpha | rộng 400, 800 | khoảng 340 |
| `divider` | `frames-epic/divider.alpha.png` 1536 × 512 | 115: M 8, Q 9 | cắt sát alpha | rộng 320, 640 | khoảng 280 |

- Đọc đúng `title-backdrop.v2.png`. `title-backdrop.png` là bản cũ bị trả (md5 khác).
- Logo theo chấm nhận 158 (45 % rộng), không theo cỡ 420 / 630 cũ của WW-08.
- Favicon chỉ dùng tạm tới khi 177 được nhận. Ghi `"until": "177"` ở mục đó.

## Việc

1. **Danh sách chọn** `scripts/td/ui-picks.json` (vào Git):
   - mỗi mục có `name`, `source`, `accepted` (true/false), `verdict` (file chấm, M, Q), bước cắt, danh sách file ra kèm cỡ px;
   - nội dung đúng bảng trên.
2. **`scripts/td/prepare-ui.mjs`**, theo mẫu `prepare-ground.mjs`:
   - đọc danh sách chọn; bỏ qua mục `accepted: false`;
   - có hàm thuần `plan(picks)` trả về danh sách việc, để test;
   - ImageMagick 7 (`magick`), sRGB, Lanczos;
   - chỉ cắt, cắt sát alpha, thu nhỏ. Không phóng to: file ra không rộng hơn nguồn sau khi cắt;
   - không chỉnh màu, không làm nét, không phủ, không làm tối (§5);
   - không sửa màu ruộng của 158. Đó là một lượt sửa ảnh sau, đã quyết ở `accept-29-10b/verdict.md` mục 158;
   - WebP chất lượng 82–88; ảnh có alpha thêm `-define webp:alpha-quality=100 -define webp:exact=true`;
   - `--check`: liệt kê file thiếu hay cũ hơn nguồn, không ghi gì, thoát 1 khi có;
   - chỉ ghi tên có trong danh sách. Không ghi đè hay xóa file khác (`title-dusk.webp` giữ nguyên).

   Chạy script một lần để ra media.
3. **`src/ui/art.ts`** là nơi duy nhất trong `src/` có URL ảnh UI:
   - URL, `srcset`, `sizes` cho từng tên, khớp danh sách chọn;
   - hàm gắn ảnh: ảnh lỗi thì `console.warn` (tên và URL) và ẩn ảnh. Không vẽ gì thay.
4. **Màn tựa** (`title.ts`, `title.css`):
   - nền là `title-backdrop` (`srcset` 1280w và 1536w, `cover`, mờ vào như hiện nay);
   - bỏ `title-dusk.webp` khỏi mã. Không dùng nó làm tranh dự phòng;
   - nền lỗi: nền phẳng `#1c1824` và `console.warn`, như hiện nay;
   - logo là ảnh trong `h1.tt-name`: rộng 45 % màn, giữa ngang, mép trên khoảng 5–6 % cao màn, như mock 158;
   - phụ đề nằm dưới logo;
   - tên đọc màn hình là "Wordwoven", đúng một lần, cả khi có ảnh lẫn khi ảnh lỗi;
   - logo lỗi: ẩn ảnh, hiện chữ "Wordwoven" kiểu hiện nay, `console.warn`;
   - logo cần đọc rõ hơn thì chỉ thêm một vệt tối mềm hình elip (độ mờ ≤ 0,35) sau logo bằng CSS. Không hộp, không hình;
   - menu giữ chỗ cũ ở góc dưới trái;
   - chừa trống góc trên phải (khoảng 200 × 90 px CSS) cho nút của phiếu 193;
   - sửa gọn: không đổi tên class, không sắp lại mã có sẵn, để lúc gộp với 193 ít xung đột.
5. **Favicon và dòng nạp** (`index.html`, `src/main.ts`):
   - thay `<link rel="icon" href="data:,">` bằng hai `<link rel="icon" type="image/png">` cho `favicon-32.png` và `favicon-64.png`;
   - dòng nạp: logo nhỏ (120 / 180 px CSS) thay chữ "Wordwoven", sau đó là chữ "loading words…";
   - logo nhỏ lỗi: ẩn ảnh, hiện chữ "Wordwoven", `console.warn`;
   - ảnh có thể lỗi trước khi `main.ts` chạy: xét cả `complete` và `naturalWidth`, không chỉ sự kiện `error`.
6. **Thẻ kết** (`sheets.ts`, `td.css`):
   - `crest` ở giữa trên, nằm trong thẻ. Thẻ có `overflow-y: auto`, phần nhô ra ngoài sẽ bị cắt;
   - thắng: crest đủ màu;
   - thua: cùng crest, chỉ lọc CSS cả ảnh (ví dụ `grayscale(0.5) brightness(0.75)`). Không vẽ thêm;
   - `banner` nằm sau tiêu đề "Village saved" / "Fort fallen". Tiêu đề vẫn là chữ thật, đọc rõ trên dải;
   - `divider` nằm giữa bảng số và "To review". Không có danh sách ôn thì đặt trước các nút;
   - ba ảnh này là trang trí: `alt=""`, `aria-hidden="true"`;
   - chỉ tải khi thẻ kết hiện, không tải ở "/";
   - ở cửa sổ thấp (≤ 800 px) crest được nhỏ còn 72 px nếu cần, để thẻ kết ở 1280 × 720 không phải cuộn (Claude kiểm);
   - thẻ tạm dừng không đổi.
7. **Kịch bản `td-theme`** (chỉ sửa, không chạy):
   - nền tải từ `title-backdrop.*.webp`; `painted: true` và `drawn: 0` giữ nguyên;
   - logo tải xong (`naturalWidth > 0`), rộng 40–50 % cửa sổ, tên đọc màn hình là "Wordwoven";
   - favicon trả 200 `image/png`;
   - thẻ kết có crest, banner, divider tải xong.
8. **Test trước, mã sau.** Vitest chạy môi trường `node`; không thêm thư viện DOM. Test HTML bằng chuỗi hay đối tượng giả, như `tests/td-sheet-cards.test.ts`. Test không đòi file media có mặt.
   - Danh sách chọn khớp `art.ts` hai chiều; mỗi mục có `accepted` và `verdict`.
   - `plan()`: cắt `1536x864+0+80`; cỡ đúng bảng; không file nào phóng to; bỏ qua mục `accepted: false`.
   - HTML màn tựa: logo là ảnh có `alt="Wordwoven"`; nền có `srcset`; không `svg`; không `title-dusk`.
   - HTML thẻ kết: thắng và thua đều có crest, banner, divider; thua có lớp làm mờ; thẻ tạm dừng không có ba ảnh này.
   - Ảnh lỗi: `console.warn` có URL, ảnh bị ẩn.
   - `index.html`: favicon trỏ đúng URL của `art.ts`; không còn `data:,`; dòng nạp có ảnh và chữ "loading words…".
9. **Tờ xem** ở `tmp/200/` của worktree (không đặt trong `docs`, `art-src`, `public`):
   - `files.jpg`: mọi file ra ở cỡ hiện, trên nền tối `#1c1824` và trên nền giấy của thẻ;
   - `title-mock-1280.jpg`, `title-mock-1920.jpg`: nền và logo ghép tĩnh, đúng vị trí CSS;
   - `favicon.jpg`: bản 32 và 64 trên tab sáng và tab tối, phóng ×4 không làm mượt;
   - `results-mock.jpg`: crest, banner, divider trên màu thẻ, bản thắng và bản thua.

   Đây là mock tĩnh, không phải nghiệm thu. Chỉ giữ bốn tờ này; không để khung thô.
10. **Changelog:** `docs/changelog/<ngày>-title-results-art.md` (tiếng Việt, nêu WW-01, WW-02, WW-03, WW-08, WW-56 đã gắn), cộng một hàng ở `docs/changelog/README.md`.

## Cấm

- Mọi lệnh git có ghi; sửa `src/kit/**`; chạy đồng bộ kit.
- Dev server, trình duyệt, mạng; thêm gói npm.
- Sinh ảnh mới hay sửa tranh. Ghi, đổi tên, xóa bất cứ gì trong `art-src/`.
- Ghi đè hay xóa file media có sẵn. Đưa ảnh vào Git.
- Ghi ra ngoài repo.
- Đụng worktree khác (`.wt-td-1c`, `.wt-td-keys`, `.wt-td-codex`, `.wt-td-vfx`, `.wt-play-*`), game khác, Tu Tiên.
- Sửa `src/view/**`, luật chơi, ván vàng.
- Làm việc của phiếu khác: nút Settings và loa (193); icon sao WW-57; bảng `panel-large` 115 (chưa nhận); tranh thắng thua 183.
- Hình vẽ bằng mã thay ảnh: SVG, hình CSS, canvas, emoji.
- Chữ người chơi thấy phải là tiếng Anh.

## Kiểm (ghi số)

1. `pnpm check` xanh (ghi số test). Test thời gian đỏ khi máy bận thì chạy riêng ba lần.
2. Gói khởi động "/" (in bởi `bundle-budget.mjs`) trước và sau, ≤ 85 kB gzip. Lưu `200/budget.json`.
3. `pnpm td:golden:check` giữ nguyên.
4. Mỗi file ra: px, byte, md5. Lưu `200/media.json`, ghi đường dẫn thật trong checkout chính `games/typing-defense/public/assets/typing-defense/ui/` (trong worktree `ui/` là liên kết); đây là danh sách media để Claude `media:push`. Mỗi file `title-backdrop` ≤ 400 kB.
5. `node scripts/td/prepare-ui.mjs --check` thoát 0 sau khi chạy. Chạy script lần hai không ghi file nào.
6. md5 sáu file nguồn trước và sau bằng nhau. Lưu `200/sources-md5.json`.
7. `grep`: `title-dusk` có 0 lần trong `src/` và `index.html`; chuỗi `/assets/typing-defense/ui/` chỉ có trong `src/ui/art.ts` và `index.html`.
8. Xem bốn tờ ở 100 %: không vệt khối, không dải màu, không viền hồng quanh logo và huy hiệu. Ghi nhận xét.
9. `git status --short -uall`: chỉ `scripts/td/prepare-ui.mjs`, `scripts/td/ui-picks.json`, `src/ui/art.ts`, các file `src/ui/` đã sửa, `index.html`, `src/main.ts`, test, `scripts/visual/scenarios/td-theme.mjs`, hai file changelog.

**Xong khi:** mười mục việc và chín mục kiểm đạt. Báo cáo ghi chỗ còn mở: crest thua riêng (nếu lớp làm mờ chưa đủ), icon sao WW-57, bảng 115, tranh 183, favicon chờ 177.

Sau đó Claude duyệt diff, chạy `td-theme` trên trình duyệt ở 1280 × 720 và 1920 × 1080, chạy `media:push`, rồi commit. Phiếu 193 sửa cùng màn tựa trên nhánh `td-keys` (cắt từ `a2-days`), nên Claude gộp `td-keys` vào `td-ui` sau 200 và 203 và giải xung đột màn tựa lúc đó (phiếu 204 cần phần của 193 trên `td-ui`).
