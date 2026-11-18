# Phiếu 206 · Last Line · Đường ảnh UI (chọn → WebP → bảng), gắn icon súng, chân dung quái, ảnh ải vào các màn

**Nguồn:**
- `docs/games/map1/UI_IMAGERY.md` §4: "Game không tải ảnh nào. Không có `<img>`, `url()` hay `TextureLoader` cho ảnh."
- Cùng file, §8: "Script chuẩn bị đọc `art-src`, xuất WebP vào `public/assets/<game>/ui/…` và ghi `manifest.json` nhỏ"; "Mã đọc URL từ một bảng duy nhất"; "Ảnh lỗi thì ghi `console.warn` và để trống". §8.1: Last Line làm trước.
- `docs/games/MAP1_PRODUCTION.md` §3.2 mục 14: "TS-M1-10 · … Gắn icon súng và chân dung quái vào thẻ súng, đầu bến, bảng tin; chữ ≥ 26 px, không tràn."
- `docs/HANDOFF_CURRENT.md` §3: "Kiểm kê UI 29/10, việc của Claude (làn gắn ảnh, chưa mở): gắn icon súng 108 vào thẻ Nạp súng và hai bến chữ của Last Line; chân dung quái 089 vào thẻ ải".
- `AGENTS.md` (chủ dự án 28/10): "Every UI detail carries real art, not text alone."
- Chủ dự án 30/10/2026: "tăng thêm việc cho codex cho tôi".

HANDOFF giao việc gắn này cho làn Claude. Nay phần mã chuyển sang Codex; Claude kiểm trên trình duyệt.

**Không trùng:** 089, 108, 109, 121, 126, 157 chỉ vẽ ảnh; 149–153 vẽ icon UI (chưa nhận); 130 đổi chữ sang tiếng Anh; 191 làm nút Settings, nút Sound và tiếng phím. 194 là phiếu cùng khuôn cho Dragonhold: đọc làm mẫu, không sửa.

**Làn:** nối cuối làn Codex `s1` (một làn, chủ dự án 30/10), cwd `.`. Phiếu 211 chạy sau phiếu này trên cùng worktree.

**Báo cáo:** `docs/codex-queue/206-report.md` (repo cha, tiếng Việt), thư mục `docs/codex-queue/206/` (chỉ JSON, Markdown, log; ảnh xem nằm ở `tmp/206/` của worktree).

## Chỉ chạy khi

Claude đã:
- cắt worktree `games/.wt-ts-art`, nhánh `ts-art`, từ `main` Last Line (lúc viết phiếu là `79db628`; nếu Claude đã gộp nhánh khác vào `main` thì cắt từ `main` mới);
- chạy `pnpm install --offline` trong worktree đó.

Worktree riêng để phiếu này không đụng `.wt-ts-codex` (205, 207, 210) và `.wt-ts-typefx` (191, TF2). Kiểm trước khi làm: `git -C games/.wt-ts-art branch --show-current` là `ts-art`; có `games/.wt-ts-art/node_modules/.bin/vitest`. Thiếu một điều thì dừng, ghi vào báo cáo.

## Nơi làm và luật chung (phiếu mã)

- cwd của làn là repo cha. Lệnh `pnpm` chạy trong `games/.wt-ts-art`.
- Đường dẫn mã trong phiếu tính từ gốc worktree. Số dòng theo `79db628`; lệch thì tìm theo chuỗi.
- `git status --short -uall` phải sạch trước khi làm. Được dùng git chỉ đọc.
- **Ảnh nguồn, chỉ đọc:** `../typing-survival/art-src` (checkout chính). Worktree không có `art-src` (media, Git bỏ qua), nên mọi lệnh truyền `--art-src ../typing-survival/art-src`.
- **Media ra** ghi vào `public/assets/typing-survival/ui/` của worktree: thư mục thật, không liên kết (`deploy:pack` từ chối symlink). Không ghi vào checkout chính.
- File tạm, fixture test, tờ xem nằm ở `tmp/` của worktree. Không ghi ra ngoài repo, kể cả thư mục tạm của hệ điều hành: tạo `tmp/os-tmp/` của worktree và chạy mọi lệnh `pnpm`, `node`, `magick`, `cwebp` với `TMPDIR` và `MAGICK_TEMPORARY_PATH` trỏ vào đó (bộ đệm `tsx`, Vitest, ImageMagick). Xong thì xóa `tmp/os-tmp/`.
- Test trước, mã sau. Chú thích tiếng Anh, ngắn. Changelog tiếng Việt.
- Chữ người chơi thấy là tiếng Anh và **giữ nguyên**. Phiếu chỉ thêm ảnh.
- Luật chơi, số trong `src/content/**`, `src/sim/**`, ván vàng không đổi.
- Đây là phiếu mã: không sinh ảnh. Bước công cụ chỉ đổi định dạng, thu nhỏ, và cắt 16 : 9 cho nền (`docs/games/ART_ACCEPTANCE.md` §5). Không làm nét, không đổi màu, không phóng to, không phủ.
- Chỉ ảnh đã nhận (`ART_ACCEPTANCE.md`: ảnh 2D từ 8 điểm, chấm theo game thương mại) được vào `public/`. Ảnh chờ chấm nằm trong bảng chọn với `accepted: false` và không bao giờ vào `public/`.
- Ảnh là `<img>` trong HTML, không `url()` trong CSS: bắt được lỗi tải, có `alt`, test được bằng chuỗi. `theme.css` không thêm màu nào.
- **Đọc trước (chỉ đọc):**
  - `docs/codex-queue/194-dh-ui-art-icons.md` (cùng khuôn);
  - `docs/games/map1/UI_IMAGERY.md` §4.2–4.6 (cỡ từng chỗ) và §8.1;
  - `docs/CODEX_QUEUE.md`, hàng 089, 108, 109, 121, 126, 157 (trạng thái nhận);
  - mã: `src/view/screens.ts`, `src/view/screens-journey.ts`, `src/view/hud.ts`, `src/view/survival.css`, `src/app/journey.ts`, `src/app/menu.ts`, `src/app/main.ts` (dòng 255–345 và 597–601);
  - test mẫu không cần DOM: `tests/small-labels.test.ts`, `tests/english-ui.test.ts`;
  - kịch bản mẫu: `scripts/visual/scenarios/survival-s1-loadout.mjs`.

## Đầu vào

Đường tính từ `--art-src`. Tên vai (role) là tên file ra; đổi nguồn không đổi URL.

| Vai | Loại | Nguồn đã nhận (`accepted: true`) | Nguồn chờ (`accepted: false`) |
|---|---|---|---|
| `gun-xung`, `gun-tia`, `gun-tan`, `gun-ray`, `gun-phao` | `icon` | `ui/icons/gun-<tên>.norm.{64,128,256}.png` (108). `gun-phao` đọc `gun-phao-sao.norm` | `ui/icons/gun-<tên>.v2.{64,128,256}.png` (157) |
| `foe-swarm`, `foe-scout`, `foe-brute`, `foe-pack-leader`, `foe-shield-guard`, `foe-splitter` | `portrait` | `ui/foes/<tên>.png`, 1024 × 1024 RGBA (089) | `ui/foes/<tên>.v2.{64,128,256}.png` (157) |
| `foe-shard` | `portrait` | — | chưa có ảnh: `source: null` (`shard` thuộc 150) |
| `stage-c1-s1` … `stage-c1-s4` | `stage` | `ui/stages/c1-sN.png`, 1536 × 864 RGB (109, nhận tạm 8,5) | `ui/stages-v2/c1-sN.png` (126) |
| `bg-menu`, `bg-journey`, `bg-briefing`, `bg-loadout`, `bg-results-win`, `bg-results-lose` | `bg` | — | `ui/screens-epic/{menu,journey,briefing,loadout,results-win,results-lose}-bg.png`, 1536 × 1024 RGB (121) |

- Khóa súng trong mã: `GUN_KEYS` = `xung`, `tia`, `tan`, `ray`, `phao` (`src/content/guns.ts:12`). Loại quái: `KIND` (`src/content/foes.ts:15`).
- **Không dùng:** `.try*`, `.v1`, `nova*`, `title-horizon.png`, `boss/`, `frames-epic/`, `quick-settings/`, `results/`, `logo*`.
- Mỗi vai có đúng một mục `accepted: true`, hoặc không có mục nào.
- Khi Claude nhận 157, 126 hay 121, Claude chỉ đổi cờ trong bảng chọn rồi chạy lại script. Mã không đổi.

## Việc

1. **Bảng chọn** `scripts/ui-art/selection.json` (Git giữ; Claude sửa khi nhận ảnh):
   - `version`: số nguyên, bắt đầu 1. `entries`: 37 mục, đúng bảng Đầu vào.
   - Mỗi mục: `role`; `kind` (`icon`, `portrait`, `stage`, `bg`); `source` (đường tương đối `--art-src`, không đuôi `.png`, không đuôi cỡ, hoặc `null`); `accepted`; `ticket` (`"108"`…); `verdict` (chỗ ghi chấm, ví dụ `"CODEX_QUEUE 108: Nhận 29/10"`); `alt`; `crop` (chỉ `bg`: `"1536x864+0+80"`).
   - 15 mục nhận (5 súng, 6 quái, 4 ải). 22 mục chờ.
   - `alt` tiếng Anh, đúng tên trong mã: súng theo `GUN_SPECS[].name` ("Pulse Gun"…); quái "Swarm", "Scout", "Brute", "Pack Leader", "Shield Guard", "Splitter", "Shard"; ải theo `CHAPTER_1[].name` ("First Shift"…). Nền: `alt` là `""`.
2. **Script** `scripts/ui-art/prepare.mjs`. `package.json` chỉ thêm một dòng `"ui-art:prepare": "node scripts/ui-art/prepare.mjs"`.
   - Lệnh: `pnpm ui-art:prepare [--art-src <dir>] [--out <dir>] [--table <file>] [--check] [--pending] [--help]`. Mặc định `--art-src art-src`, `--out public/assets/typing-survival/ui`, `--table src/view/ui-art.json`.
   - Chỉ dựng mục `accepted: true`.
   - **Cỡ ra (rộng, px):**
     - `icon`, `portrait`: 64, 128, 256 (vuông). Có `<source>.<cỡ>.png` thì lấy đúng file đó. Không có thì thu Lanczos (sRGB) từ `<source>.png` hay file lớn hơn gần nhất. Không có nguồn lớn hơn thì báo lỗi, không phóng to.
     - `stage`: 192, 384, 768, 1536 (16 : 9) từ `<source>.png`. Nguồn không đúng 16 : 9 thì báo lỗi, không tự cắt.
     - `bg`: cắt `crop` (giữa 16 : 9), rồi ra 1280 và 1536.
   - **Tên ra:** `<out>/<role>.<rộng>.webp`. 15 vai nhận cho 49 file WebP.
   - **WebP:** `cwebp -metadata none -m 6`.
     - `icon`, `portrait`: `-q 90 -alpha_q 100`.
     - `stage`, `bg`: `-q 84`.
     - Đo PSNR so với PNG cùng cỡ (`magick compare -metric PSNR`). `icon`, `portrait` dưới 35 dB thì xuất `-lossless` file đó. `stage`, `bg` dưới 35 dB thì `-q 92`; vẫn dưới thì ghi lại.
   - File trung gian ở `tmp/ui-art/work/`.
   - **Manifest media** `<out>/manifest.json` (Git bỏ qua, như mọi file dưới `public/assets/`): `version`; mỗi vai có `ticket`, `source`, `sourceMd5`; mỗi cỡ có `file`, `width`, `height`, `bytes`, `md5`, `psnr`, `lossless`.
   - Ghi **bảng chạy** (mục 3).
   - Dựng xong mọi file trong `tmp/` rồi mới chuyển vào chỗ. Manifest và bảng chạy ghi sau cùng, qua file tạm. Lỗi giữa chừng thì không file cũ nào bị thay.
   - Chạy lại với cùng nguồn: không ghi file nào (so md5 nguồn và cỡ).
   - Chỉ xóa file chính nó đã ghi (có trong manifest cũ), khi vai không còn mục nhận. Không đụng file khác dưới `public/assets/typing-survival/` (ví dụ `audio/` của 191).
   - `--check`: không ghi gì. Thoát 1 và nêu tên khi: thiếu file; md5 hay bytes lệch manifest; md5 nguồn đã đổi; bảng chạy lệch bảng chọn hay manifest; có `.webp` lạ mang tên vai. Thiếu `--art-src` thì thoát 2 kèm lời rõ.
   - `--pending`: dựng thêm các mục `accepted: false` có nguồn, **chỉ** vào `tmp/ui-art/pending/`. Không bao giờ ghi `public/` hay bảng chạy. In byte từng cỡ.
   - Logic thuần là hàm export để test gọi: `plan(selection, files)` trả danh sách việc; chọn nguồn từng cỡ; kiểm 16 : 9.
3. **Bảng chạy** `src/view/ui-art.json` (script sinh, Git giữ, không sửa tay):

   ```json
   { "version": 1, "base": "/assets/typing-survival/ui/",
     "roles": { "gun-xung": { "kind": "icon", "alt": "Pulse Gun", "rev": "1a2b3c4d", "widths": [64, 128, 256], "aspect": 1 } } }
   ```

   - Chỉ có vai có mục nhận và đã dựng.
   - `rev`: 8 ký tự đầu md5 nguồn, để đổi URL khi đổi ảnh (`?v=<rev>`). `aspect`: rộng / cao.
   - Không có đường `art-src` hay `.png` (file này vào gói JS).
   - Sắp theo tên vai, số làm tròn 6 chữ số, xuống dòng cuối file. Cùng đầu vào ra cùng byte.
   - Bảng nằm trong `src/` vì `tests/boundary.test.ts` chỉ cho `src/` nạp `src/**`.
4. **`src/view/ui-art.ts`**: nơi duy nhất trong `src/` có URL ảnh UI.
   - **Vai:** `gunRole(key)`; `foeRole(kind)` (`mine` → `foe-swarm`, `leader` → `foe-pack-leader`, `shield` → `foe-shield-guard`, `shard` → `foe-shard`…); `stageRole(id)`; `rowRoles(row)`; `bgRole(screen)`.

     | Hàng (`CounterRow`) | Vai |
     |---|---|
     | `swarmFar`, `swarmNear` | `foe-swarm` |
     | `scout` | `foe-scout` |
     | `armoured` | `foe-brute`, `foe-pack-leader` |
     | `shield` | `foe-shield-guard` |
     | `splitter` | `foe-splitter`, `foe-shard` (chờ: ra rỗng) |

   - **`BOX`:** một bảng hằng số cỡ ô ở 720p cho mỗi chỗ gắn (bảng mục 5). Không rải số cỡ ở file khác.
   - **`pick(role, box)`:** ảnh 1x là cỡ nhỏ nhất ≥ `box × 1,5` (1080p: `--ui` = 1,5; `--ui` đi từ 0,8 tới 1,6, `src/app/main.ts:599`). Ảnh 2x là cỡ nhỏ nhất ≥ `box × 3`. Vượt cỡ lớn nhất thì lấy cỡ lớn nhất. 2x trùng 1x thì bỏ `srcset`. `box` là bề rộng ô ở 720p.
     - `srcset` dùng mật độ (`1x`, `2x`), không dùng `sizes`: `sizes` không đọc được biến `--ui`.
   - **`artHtml(role, place, opts?)`** trả `<img class="sv-art sv-art-<place>" src="…webp?v=<rev>" srcset="… 2x" width="<rộng 720p>" height="<cao 720p>" alt="" aria-hidden="true" decoding="async" draggable="false">`. Vai không có trong bảng chạy thì trả chuỗi rỗng.
     - Ảnh đứng cạnh chữ nói cùng tên là trang trí: `alt=""`, `aria-hidden="true"`. Ở phiếu này mọi chỗ đều vậy.
     - `opts.label` true thì `alt` lấy chữ tiếng Anh của bảng, bỏ `aria-hidden`.
   - **`artAttrs(role, place)`** trả đối tượng thuộc tính (hay `null`) cho `hud.ts` dựng bằng DOM. Cùng luật với `artHtml`.
   - **Vai thiếu** (chờ nhận, hay không có ảnh): không trả gì. `console.warn("[ui-art] no accepted image: <role>")` một lần mỗi vai mỗi trang. Có `resetArtWarnings()` cho test.
   - **`watchArt(target)`:** một listener `error` ở pha bắt (capture) cho `img.sv-art`. Gọi `console.warn("[ui-art] missing image: <url>")` một lần mỗi URL, rồi đặt `hidden = true`. Tách hàm xử lý, có export, để test bằng đối tượng giả (repo không có DOM giả).
5. **Gắn** (12 chỗ):

   | Mã | Chỗ (`79db628`) | Vai | Ô 720p (1080p), px CSS | Cách gắn |
   |---|---|---|---|---|
   | LL-15 | kho súng, `screens.ts:90` | `gun-<kind>` | 64 (96) | trong `header`, trước tên |
   | LL-17 | 4 hàng ải: `journey.ts:127` thêm `art`; vẽ ở `screens.ts:39` `item()` | `stage-<id>` | 96 × 54 (144 × 81) | sau `.sv-led`, trước chữ. Hàng khóa vẫn có ảnh, mờ theo `.is-off` sẵn có |
   | LL-18 | thẻ ải, dưới `h1` ở `screens-journey.ts:62` | `stage-<id>` | 760 × 120 (1140 × 180) | băng ảnh rộng theo thẻ, `object-fit: cover` |
   | LL-20 | `ul.sv-foes li`, `screens-journey.ts:70-72` | quái theo tên | 40 (60) | trước `<b>` tên |
   | LL-21 | "This stage teaches", `screens-journey.ts:73` | quái của mục dạy (`brute`, `leader`, `shield`, `splitter`) | 32 (48) | trước câu. `hunt`, `rift`, `missing` không ảnh |
   | LL-25 | 5 thẻ nạp súng, `screens-journey.ts:87-100` | `gun-<key>` | 72 (108) | khối riêng trên `header`, canh trái. Tên súng vẫn một dòng |
   | LL-26 | "Strong:", "Weak:", `screens-journey.ts:95-96` | quái theo hàng (bảng mục 4) | 20 (30) | trước nhãn từng hàng; chữ nối ", " giữ nguyên |
   | LL-27 | chip mối nguy, `screens-journey.ts:101-103` | quái theo hàng | 16 (24) | trong chip, trước nhãn. Dấu "⚠ " giữ nguyên |
   | LL-29 | thẻ trước trận, `screens.ts:116-125`; `main.ts:303-306` | `stage-<id>`; `gun-<key>` | ải 384 × 216 (576 × 324); súng 48 (72) | ảnh ải dưới vạch đầu thẻ; icon trước mỗi tên súng ở dòng hai. Ải thử `s0` không ảnh ải, không gọi vai ải |
   | LL-35 | thẻ ra mắt quái, `hud.ts:147,402` | quái theo `kind` | 48 (72) | ảnh bên trái chữ trong `.sv-fresh` |
   | LL-39 | bến, `hud.ts:164-168` | `gun-<key>` | 40 (60) | huy hiệu đứng trên mép trên tấm bến, phía xa tàu (bến 1, 3 bên trái; bến 2, 4 bên phải). Không đổi chiều cao 100 px, không đổi bố cục trong bến |
   | LL-53 | nút "Stage n" ở kết quả, `main.ts:262` thêm `art` | `stage-<id ải kế>` | 96 × 54 (144 × 81) | như LL-17 |

   Dữ liệu cần thêm (chỉ thêm trường, không đổi logic, chữ hay thứ tự):
   - `src/app/menu.ts`: `MenuItem` thêm `readonly art?: string` (vai).
   - `src/app/journey.ts`: hàng ải thêm `art`. `CardView` thêm `goodRows`, `poorRows` (`CounterRow[]`, cùng thứ tự với chữ `good`, `poor`). `ThreatView` thêm `row`.
   - `src/view/screens.ts`: `ScreenView` loại `intro` thêm `stage?: string` (id ải) và `guns?: readonly GunKey[]`.
   - `src/app/main.ts`: chỉ hai chỗ. `view("intro")` truyền `stage` (trừ `s0`) và `guns`. Mục `next` ở `items("end")` thêm `art`. Tối đa 4 dòng đổi.
   - `src/view/hud.ts`: icon bến, ảnh thẻ ra mắt, gọi `watchArt(root)` một lần trong constructor. Tối đa 20 dòng đổi. Không sắp lại mã có sẵn.
6. **Nền màn** (chờ 121, gắn sẵn):

   | Mã | Màn | Vai |
   |---|---|---|
   | LL-12 | màn chính, `screens.ts:62-75` | `bg-menu` |
   | LL-16 | Hành trình, `screens-journey.ts:49-57` | `bg-journey` |
   | LL-23 | thẻ ải, `screens-journey.ts:59-76` | `bg-briefing` |
   | LL-24 | nạp súng, `screens-journey.ts:78-111` | `bg-loadout` |
   | LL-49 | kết quả, `screens.ts:126-141` | `bg-results-win` hay `bg-results-lose` theo `won` |

   - Nền là `<img class="sv-art sv-bg">` đứng đầu chuỗi HTML của màn. Phủ kín overlay (`position: absolute; inset: 0; object-fit: cover`), nằm dưới thẻ.
   - Màn che sẵn có của overlay (`--veil`, `--veil-edge`) phải nằm trên ảnh nền và dưới thẻ, để chữ đọc rõ.
   - Thiếu nền thì màn hình giống hệt hôm nay.
   - Hôm nay sáu vai này đều chờ: HTML không có ảnh nền, mỗi vai một `console.warn` (mục 4).
7. **Thiếu ảnh không vẽ thay.** Không SVG, hình CSS, canvas, emoji hay ký tự. Không khung, nền hay viền giữ chỗ cho ảnh thiếu. Không thẻ bọc thêm làm đổi khoảng cách. Bố cục khi thiếu ảnh giống hôm nay.
8. **CSS** (`src/view/survival.css`, khối mới cuối file, chú thích `UI art (Codex 206)`):
   - Mỗi chỗ một lớp `.sv-art-<place>`. Cỡ `calc(<N>px * var(--ui))` theo `BOX`. `flex: none`.
   - `object-fit: contain` cho `icon`, `portrait`; `cover` cho `stage`, `bg`.
   - Không màu mới. Không `filter`, `mix-blend-mode`, `opacity`, `border-radius` trên ảnh. `tests/theme.test.ts` phải xanh.
   - `[hidden]` của ảnh lỗi phải thắng mọi `display` mới: dùng `:not([hidden])` (luật trong `AGENTS.md` của game, lượt test 27/10).
   - Không đổi cỡ chữ nào. Từ trên bến 32 px, từ dài co tới 26 px (`hud.ts:54` `MIN_FIT`; `docs/BUILD_S1.md` §3). Bến đang gõ giữ 22 px.
9. **Kịch bản trình duyệt** `scripts/visual/scenarios/survival-ui-art.mjs`. **Chỉ viết, không chạy**; Claude chạy ở 1280 × 720 và 1920 × 1080.
   - Đi như `survival-s1-loadout.mjs`: màn chính → Hành trình → thẻ ải 1 → nạp súng (phím 1, 2) → thẻ trước trận → trận. Rồi kho súng.
   - Ngay sau dòng xóa `survival.stages`, đặt `localStorage` `survival.guide` thành `{"started":true,"hint":true}`. Phiếu 210 (nhánh `ts-codex`) chọn sẵn Pulse Gun và Heat Beam ở lần đầu, nên sau khi gộp phím 1, 2 sẽ bỏ chọn thay vì chọn. Khi chưa có 210, khóa này không ai đọc.
   - Mỗi màn:
     - mọi `img.sv-art` đã tải (`complete` và `naturalWidth > 0`);
     - cỡ hiện bằng `BOX × --ui`, lệch ≤ 1 px;
     - không phần tử nào tràn (`scrollWidth > clientWidth + 1`);
     - thẻ nằm trọn trong cửa sổ, không cuộn.
   - Trong trận: từ trên bến ≥ 26 px; không gì tràn trong bến; icon bến nằm trong cửa sổ và không chồng lên dòng chữ `.sv-strip`.
   - Byte ảnh từng màn, đo bằng `performance.getEntriesByType("resource")` (lọc `/assets/typing-survival/ui/`).
   - `console.warn` có tiền tố `[ui-art]`: chỉ các vai đang chờ, không có `missing image`.
   - 0 lỗi console, 0 ngoại lệ. Ảnh chụp vào `OUT_DIR`.
   - Không sửa kịch bản cũ. Kiểm cũ còn chuỗi tiếng Việt ("khắc: Rail Gun", "ẢI 1", "Trận thử") thì chỉ ghi vào báo cáo.
10. **Tờ xem** (chỉ để Claude xem; không chép vào `docs`, `art-src`, `public`):
    - `tmp/206/sheet.jpg`, dưới 1 MB: mỗi vai đã nhận, mọi cỡ ra. PNG nguồn và WebP cạnh nhau ở cỡ hiện 720p và 1080p. Trên `#0d1013` (`--steel-900`) và trên xám sáng `#d9dde2`. Nhãn: vai, cỡ, byte, PSNR.
    - `tmp/206/pending-sheet.jpg`: cùng kiểu, cho lượt `--pending`.
    - Xong thì dọn file trung gian của mình: `node tools/capture-prune/prune.mjs games/.wt-ts-art/tmp/206 --min-age-min 0` (xem danh sách trước), rồi thêm `--apply`. Giữ hai tờ. Xóa `tmp/ui-art/` của mình.
11. **Tài liệu:**
    - README của game: một đoạn ngắn về `pnpm ui-art:prepare` và cách Claude bật ảnh khi nhận (đổi cờ, chạy lại, `media:push`).
    - `AGENTS.md` của game: một dòng ở phần Layout, nêu bảng chọn, script, bảng chạy, và chỉ `src/view/ui-art.ts` có URL ảnh UI.
    - Changelog `docs/changelog/<ngày>-ui-art.md` (tiếng Việt): mã LL đã gắn, vai còn chờ, số đo.

## Test (viết trước)

Vitest chạy môi trường `node`. Không thêm thư viện DOM. Test HTML bằng chuỗi, như `tests/small-labels.test.ts`.

1. **Bảng chọn:** 37 mục; 15 mục nhận đúng danh sách Đầu vào; mọi mục 157, 126, 121 có `accepted: false`; mỗi vai tối đa một mục nhận; `alt` khớp tên trong mã, không có tiếng Việt; mọi `bg` có `crop`.
2. **Bảng chạy ↔ bảng chọn** (luôn chạy, không cần media): vai trong `src/view/ui-art.json` đúng bằng vai có mục nhận và có nguồn; `widths` đúng loại; `rev` là 8 ký tự hex; không có chuỗi `art-src` hay `.png`.
3. **Mọi vai mã gọi có trong bảng chọn:** mọi `GUN_KEYS`, mọi `KIND` (kể cả `shard`), mọi id `CHAPTER_1`, mọi `CounterRow`, sáu nền.
4. **`pick()`:**
   - ô 40 → 64, 2x 128;
   - ô 20 → 64, không `srcset`;
   - ô 72 → 128, 2x 256;
   - ải ô 96 → 192, 2x 384;
   - ải ô 384 → 768, 2x 1536;
   - ải ô 760 → 1536, không `srcset`.
5. **HTML từng màn** (`renderScreen`, `renderJourney`):
   - kho súng: 5 ảnh `gun-*`;
   - Hành trình: 4 ảnh `stage-c1-s*`;
   - thẻ ải c1-s1: băng `stage-c1-s1`; mỗi quái trong danh sách một chân dung; ghi chú dạy có `foe-brute`;
   - nạp súng c1-s1 và c1-s4: 5 icon; dòng Strong/Weak và chip có chân dung đúng hàng;
   - thẻ trước trận c1-s1 với `xung`, `tia`: ảnh ải và 2 icon. Ải thử: 2 icon, không ảnh ải, không warn;
   - kết quả thắng c1-s1: mục "Stage 2" có `stage-c1-s2`;
   - mỗi `<img>` có `width`, `height`, `alt`, `decoding="async"`.
6. **Chữ không đổi:**
   - trước khi sửa mã, ghi `tests/golden/ui-text-206.json` từ mã cũ: chữ của mọi màn ở test 5, sau khi bỏ thẻ HTML và gộp khoảng trắng;
   - sau khi gắn, chữ phải giống hệt;
   - không sinh lại file này sau khi đã sửa mã.
7. **Vai thiếu:**
   - `bg-menu` đang chờ: HTML màn chính không có `<img`, không `<svg`, không phần tử mới;
   - `console.warn` đúng một lần, có tên vai; vẽ lại không warn thêm;
   - chip hàng `splitter` có `foe-splitter`, không có gì thay `foe-shard`.
8. **Ảnh lỗi:** hàm xử lý với `img.sv-art` giả: warn một lần mỗi URL, `hidden = true`. Ảnh không có lớp `sv-art` thì bỏ qua.
9. **HUD:** `artAttrs` cho mọi `GUN_KEYS` ở chỗ bến, và cho mọi quái được dạy ở chỗ thẻ ra mắt: đúng URL, đúng cỡ.
10. **Script** (`tests/ui-art-prepare.test.ts`; fixture nhỏ trong `tmp/ui-art-test/`, test tự dọn; bỏ qua khi thiếu `magick` hay `cwebp`):
    - icon đủ 64/128/256 lấy đúng file; portrait chỉ có 1024 thì thu ra ba cỡ; ải 16 : 9 ra bốn cỡ; nền cắt rồi ra hai cỡ;
    - nguồn nhỏ hơn cỡ ra thì lỗi; ải không 16 : 9 thì lỗi;
    - chỉ mục nhận được dựng; `--pending` chỉ ghi vào `tmp/`;
    - manifest khớp md5, bytes, khổ; bảng chạy khớp bảng chọn;
    - chạy lần hai không ghi file nào; `--check` thoát 0; đổi một byte thì thoát 1 và nêu file;
    - lỗi giữa chừng: file cũ, manifest cũ, bảng chạy cũ giữ nguyên byte.
11. **Media thật** (bỏ qua khi chưa có `public/assets/typing-survival/ui/manifest.json`): mọi file có mặt; md5, bytes, khổ khớp manifest.

## Cấm

- Mọi lệnh git có ghi.
- Sửa `src/kit/**`; chạy đồng bộ kit. Sửa `src/sim/**`, `src/content/**`, `index.html`, `.gitignore`, `media.md5`.
- Dev server, trình duyệt, mạng. Cài hay thêm gói npm.
- Ghi vào checkout chính `games/typing-survival` (kể cả `art-src/`, `public/`).
- Đụng worktree khác (`.wt-ts-codex`, `.wt-ts-typefx`, `.wt-ts-vfx`, `.wt-play-typing-survival`, mọi `.wt-dh-*`, `.wt-td-*`), game khác, Tu Tiên.
- Sinh ảnh mới. Sửa, đổi tên, xóa ảnh nguồn. Làm nét, đổi màu, phóng to, phủ tranh.
- Đưa ảnh vào Git. Ghi ra ngoài repo.
- Vẽ thay ảnh bằng SVG, hình CSS, canvas, emoji hay ký tự. Thêm ký tự làm icon. Thêm `filter`, `mix-blend-mode`, `opacity` để đổi màu ảnh.
- Đổi chữ người chơi thấy, cỡ chữ, thứ tự mục, phím.
- Đưa mục `accepted: false` vào `public/` hay bảng chạy.
- Làm việc của phiếu khác:
  - nút Settings, nút Sound, tiếng phím (191, TF2);
  - sao, khóa, cảnh báo, nút, icon menu (149–153, chưa nhận). Dấu "⚠", "★☆" có sẵn giữ nguyên;
  - khung UI vẽ (AD); logo, favicon (121); ảnh tàu (LL-10, LL-13).

## Kiểm (ghi số)

1. `pnpm check` xanh: số test trước và sau. Test thời gian đỏ khi máy bận thì chạy riêng ba lần.
2. **Ván vàng:**
   - md5 của `tests/golden/s0-trace.json` trước và sau trùng nhau;
   - `node --import tsx scripts/chapter-hashes.ts` chạy trước khi sửa và sau khi xong; lưu `206/chapter-hashes-before.txt`, `206/chapter-hashes-after.txt`; `diff` rỗng.
3. `tests/english-ui.test.ts`, `tests/theme.test.ts`, `tests/boundary.test.ts`, `tests/small-labels.test.ts` xanh. `node --check scripts/visual/scenarios/survival-ui-art.mjs` mã 0.
4. `pnpm ui-art:prepare --art-src ../typing-survival/art-src`:
   - số file (49 WebP và manifest), tổng byte mỗi cỡ, PSNR nhỏ nhất mỗi loại, file nào lossless hay `-q 92`;
   - lưu `206/prepare.log`;
   - chạy lần hai: 0 file ghi; ghi thời gian chạy.
5. `pnpm ui-art:prepare --check --art-src ../typing-survival/art-src`: thoát 0. Lưu `206/check.log`.
6. `--pending`: byte từng vai chờ ở mỗi cỡ; tổng byte nếu Claude nhận cả 157, 126, 121. Lưu `206/pending.json`.
7. **Byte ảnh từng màn**, ở DPR 1 và DPR 2, tính từ bảng chạy và manifest: màn chính, kho súng, Hành trình, thẻ ải 1, nạp súng ải 1, thẻ trước trận ải 1, trận ải 1, kết quả thắng ải 1. Lưu `206/bytes-per-screen.json`. Màn nào trên 1 MB ở DPR 2 thì đánh dấu cho Claude.
8. `pnpm deploy:pack` trước khi sửa và sau khi xong: số lỗi không tăng. Lưu `206/deploy-pack-before.json`, `206/deploy-pack-after.json`. Ghi số ảnh UI trong `dist/`.
9. md5 mọi file nguồn đã đọc, trước và sau, trùng nhau. Lưu `206/sources-md5.json`.
10. `grep`: chuỗi `/assets/typing-survival/ui/` chỉ có trong `src/view/ui-art.ts` và `src/view/ui-art.json`. Diff không thêm `<svg`, ký tự `\p{Extended_Pictographic}` hay `url(` nào.
11. `git diff --numstat`: `src/app/main.ts` ≤ 4 dòng đổi; `src/view/hud.ts` ≤ 20 dòng đổi.
12. `git status --short -uall` chỉ có:
    - `scripts/ui-art/selection.json`, `scripts/ui-art/prepare.mjs`, `package.json`;
    - `src/view/ui-art.ts`, `src/view/ui-art.json`, `src/view/screens.ts`, `src/view/screens-journey.ts`, `src/view/hud.ts`, `src/view/survival.css`;
    - `src/app/journey.ts`, `src/app/menu.ts`, `src/app/main.ts`;
    - test mới, `tests/golden/ui-text-206.json`;
    - `scripts/visual/scenarios/survival-ui-art.mjs`;
    - `README.md`, `AGENTS.md`, `docs/changelog/<ngày>-ui-art.md`.

    `git check-ignore -v`: một file WebP và `public/assets/typing-survival/ui/manifest.json` bị bỏ qua; `src/view/ui-art.json` không bị bỏ qua.
13. `206/media-files.txt`: đường, byte, md5 mọi file trong `public/assets/typing-survival/ui/`, cho `media:push` của Claude.

## Báo cáo phải có

- Bảng gắn: mỗi mã LL → file:dòng sau khi sửa → vai → ô.
- Danh sách vai đang chờ, phiếu nhận tương ứng, và cách Claude bật từng vai.
- Những chỗ bố cục Codex không thấy được, cần Claude nhìn: icon bến cạnh mũi súng và vạch đáy; băng ảnh thẻ ải; chiều cao thẻ nạp súng ở 720p; thẻ ra mắt quái; nền màn khi bật.

**Xong khi:** mười một mục việc, mười một test và mười ba mục kiểm đạt. Claude duyệt diff, chạy `survival-ui-art` trên trình duyệt ở 1280 × 720 và 1920 × 1080, xem tay thẻ ra mắt quái và màn kết quả, rồi commit. Sau khi gộp `ts-art` vào `main`, Claude chạy lại `pnpm ui-art:prepare` ở checkout chính rồi `media:push`.

**Rủi ro (cho Claude):**
- `main.ts` và `hud.ts` cũng đang sửa ở `ts-typefx` (TF2, 191). Phiếu này giữ sửa nhỏ; gộp trước hay sau đều phải giải tay hai file này.
- 210 (ở `.wt-ts-codex`) cũng sửa `screens-journey.ts`, `journey.ts`, `hud.ts`, `survival.css` và `main.ts`. Claude gộp theo thứ tự, giữ phần của cả hai.
- `drawScreen()` thay `innerHTML` mỗi lần đổi chọn (`main.ts:340`), nên ảnh được tạo lại. Có thể chớp: xem trên trình duyệt; nếu chớp thì làn sau giữ nút ảnh giữa các lần vẽ.
- Codex không thấy bố cục. Vị trí icon bến, băng ảnh thẻ ải và chiều cao thẻ nạp súng có thể phải dời.
- 108 và 089 vẽ theo hướng cũ; 157 (hướng B) còn chờ chấm (Pack Leader ở 34 px tương phản 0,249). Nếu chỉ nhận một phần 157, hai hướng sẽ đứng cạnh nhau.
