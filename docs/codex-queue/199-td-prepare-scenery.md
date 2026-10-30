# Phiếu 199 · Wordwoven · C9: `prepare-scenery.mjs`, atlas màu và pháp tuyến cùng manifest từ tám cây 116

> **Chạy lại (30/10, 11:10, điều phối):** lượt 10:44 bị ngắt giữa chừng vì Codex hết hạn mức (10:52). Worktree `games/.wt-td-scenery` không sạch: `package.json`, `scripts/td/prepare-scenery.mjs`, `scripts/td/scenery-set.json`, `tests/td-scenery-prep.test.ts` là **việc dở của chính phiếu này**. Đọc `git diff`, giữ phần đúng, làm tiếp đến hết phiếu. File lạ ngoài tập đó thì dừng.

**Nguồn:**
- Chủ dự án 29/10/2026: "tăng thêm việc cho codex cho tôi".
- `docs/games/MAP1_PRODUCTION.md` C9 (P0, G2, 22 h): "`scripts/td/prepare-scenery.mjs` (atlas WebP)".
- `docs/td/BUILD_1C_MAP1.md` §7 (trong worktree): `scripts/td/prepare-scenery.mjs` làm "Atlas cảnh" cho bước C9.
- TK §23.10 (`docs/td/TYPING_DEFENSE_DESIGN.md`): "tách nền theo khóa màu, cắt sát, lề 8 px, thêm viền mực, nở màu, tạo pháp tuyến phồng và tấm bóng, xếp atlas, ghi manifest".
- `docs/CODEX_QUEUE.md`, dòng 116: "Sẵn sàng gắn qua `prepare-scenery`, viền mực tắt". `docs/games/ART_DIRECTION_2026-10-28.md` §10: billboard v3, v4 tắt viền mực, giữ pháp tuyến phồng.

**Không trùng:** 106 (đã rút), 116–118 (chỉ vẽ ảnh), 095 và 097 (đất).

**Phân việc:** làn Claude kế của Wordwoven (L3) giữ phần dựng 3D (`src/view/3d/scenery.ts`, đất, đường) và đọc manifest của phiếu này. `scripts/` là việc của Codex.

**Làn:** `s1` (một làn Codex), cwd của làn là repo cha (`.`): WebP đi qua liên kết vào `games/typing-defense` (checkout chính), báo cáo nằm ở `docs/codex-queue/` của repo cha. Chạy `pnpm` trong thư mục worktree.

**Báo cáo:** `docs/codex-queue/199-report.md`, thư mục `docs/codex-queue/199/` (chỉ số liệu JSON và Markdown; ảnh kiểm nằm ở `tmp/` của worktree).

**Chỉ chạy khi** Claude đã:
- cắt worktree `games/.wt-td-scenery`, nhánh `td-scenery`, từ `td-1c` `2a1f61d`;
- liên kết `art-src/*` và `public/assets/typing-defense/{ui,ground,models/*}` như `games/.wt-td-1c`;
- tạo `public/assets/typing-defense/scenery/` là thư mục thật (để `manifest.json` nằm trong Git), trong đó `meadow` là liên kết tới `games/typing-defense/public/assets/typing-defense/scenery/meadow/` của checkout chính (thư mục này chưa có ngày 30/10: Claude tạo trước);
- chạy `pnpm install --offline` trong worktree.

Chưa có thì dừng, ghi vào báo cáo.

## Nơi làm

- Worktree `games/.wt-td-scenery`, nhánh `td-scenery`. `git status` phải sạch trước khi làm.
- WebP ghi vào `public/assets/typing-defense/scenery/meadow/`. File đi qua liên kết vào checkout chính, sẵn cho `media:push` của Claude.
- Manifest ghi vào `public/assets/typing-defense/scenery/manifest.json` (thư mục thật, Git theo dõi).
- Ảnh kiểm ghi vào `games/.wt-td-scenery/tmp/199/`.
- Chỉ đọc: `art-src/scenery/`, `art-src/_review/116/`, `art-src/_review/117/`, báo cáo 116–118, `scripts/td/prepare-ground.mjs` (khuôn mẫu), `scripts/td/media-budget.mjs`.

## Đầu vào

- **Tám ảnh 116 đã nhận** (`docs/codex-queue/accept-29-10b/verdict.md`): `art-src/scenery/meadow/{almond-tree,mountain-pine,bamboo-clump,canopy-block}-{v3,v4}.png`.
  - RGB trên nền `#FF00FF`, **không có kênh alpha**.
- **Alpha đã tách:** `art-src/_review/116/handoff-v2/<tên>.final/alpha.png` (RGBA, cùng cỡ PNG chính).
  - Dùng alpha này. RGB phần vật lấy từ PNG chính; kiểm hai file lệch ≤ 2/255 trong mặt nạ.
  - Thiếu file thì tự tách khóa M đúng cách ở `116-report.md` §3: hue 250–345° và S > 0,15, hoặc lệch kênh tối đa tới `#FF00FF` ≤ 60. Không xóa vùng theo diện tích.
- **Chiều cao theo mét:** `art-src/_review/116/visual-final/mock-layout.json`.
  - v3/v4: bàng 18/14, thông 14/10, tre 16/16, khối tán 10/14.
  - Không dùng bảng cũ `03-2d-scenery-ui-vfx.md` (bàng 8 m): v3, v4 là cổ thụ.
- **117 (10 ảnh) và 118 (8 ảnh):** đã giao, Claude chưa chấm nhận. Ghi vào tập với `accepted: false`. `tree-stump` nằm ở `scenery/shared/`.
- **Công cụ:** `magick` (ImageMagick 7), `cwebp`. Không có `toktx`, không có `sharp`, nên đầu ra là WebP. Không thêm gói npm.

## Việc

1. **Tập ảnh** `scripts/td/scenery-set.json` (Git theo dõi).
   - Mỗi mục: `id`, `type` (ví dụ `almond-tree`), `variant`, `kind`, `src`, `alpha` (nếu có), `key`, `heightM`, `ink`, `accepted`, `ticket`.
   - `kind` là một trong `tree`, `bamboo`, `canopy`, `bush`, `grass`, `flower`, `rock`, `log`, `stump`.
   - `key` là `#FF00FF` hay `#0000FF`, theo báo cáo của phiếu sinh ảnh.
   - 8 mục 116: `accepted: true`, `ink: false`.
   - 10 mục 117 và 8 mục 118: `accepted: false`. Chiều cao đề xuất lấy từ tờ cảnh của phiếu đó; ghi `heightSource`.
2. **Script** `scripts/td/prepare-scenery.mjs`, theo khuôn `prepare-ground.mjs`.
   - `node scripts/td/prepare-scenery.mjs` dựng.
   - `--check` chỉ báo thiếu hay cũ, không ghi gì, exit 1 khi có.
   - `--pending` xếp cả mục `accepted: false`, chỉ ghi vào `tmp/199/pending/`, không bao giờ ghi `public/`.
   - Lượt dựng thật chỉ đọc mục `accepted: true`.
   - Cùng đầu vào cho cùng byte đầu ra: thứ tự xếp cố định, số làm tròn 6 chữ số.
   - Logic thuần (xếp, chân, khử màu khóa, nở màu, pháp tuyến) là hàm export để test gọi. Đọc ghi ảnh qua `magick` dạng raw RGBA.
3. **Mỗi sprite.** Chỉ các bước `ART_ACCEPTANCE.md` §5 cho phép: cắt, tách nền, đổi cỡ, sửa mép.
   - Lấy alpha (mục Đầu vào). Cắt sát theo alpha ≥ 0,5.
   - Mật độ chung **72 px/m** ở High, tính trên chiều cao hộp sát.
   - Không phóng to. Ảnh nào nguồn dưới 72 px/m thì giữ cỡ nguồn, ghi `pxPerM` thật.
   - Lề 8 px mỗi phía (High).
   - Khử màu khóa chỉ ở dải mép 2 px phía trong. Chỉ sửa pixel gần màu khóa: lệch kênh ≤ 60, hoặc hue khóa ±20° và S > 0,5. Đếm số pixel đã sửa. Phần trong giữ nguyên byte.
   - Nở màu 8 px: phủ RGB của mép ra vùng alpha 0 trong lề. Lọc tuyến tính và mipmap sẽ không kéo màu khóa hay màu đen vào.
   - Viền mực tắt (`ink: false`). Gặp `ink: true` thì báo lỗi rõ và dừng, không vẽ viền.
   - Chân: y là hàng đặc thấp nhất; x là trung bình x của pixel đặc trong 2 % hàng dưới cùng.
   - Không nung đáy tối, rim, ramp, lệch màu hay lật vào atlas. Đó là việc shader và bộ rải của L3.
4. **Pháp tuyến phồng** từ alpha (TK §23.10).
   - Trường cao dạng vòm: khoảng cách tới mép, làm mượt. Đạo hàm ra pháp tuyến không gian tiếp tuyến.
   - +x sang phải, +y lên trên ảnh, z hướng camera. Mã hóa `n × 0,5 + 0,5`.
   - Trong vật z > 0. Ngoài vật là (0, 0, 1).
   - Medium dựng lại từ alpha ở cỡ Medium, không thu nhỏ ảnh pháp tuyến High.
5. **Atlas.**
   - High: `meadow/color.high.webp` và `meadow/normal.high.webp`, 4096².
   - Medium: `meadow/color.medium.webp` và `meadow/normal.medium.webp`, 2048², cùng uv với High. Màu thu nhỏ Lanczos ×0,5.
   - Tấm bóng: `meadow/shadow.high.webp`, 1024², xám một kênh, dáng từ alpha làm mờ nhẹ, cùng bố cục uv. Bóng theo dáng tranh chỉ có ở High; Medium dùng bóng tròn trong shader của L3.
   - Xếp: rect không chồng nhau. Góc và cỡ rect chia hết cho 4 ở High, để Medium vẫn nguyên pixel.
   - Không vừa thì giảm mật độ chung cùng một hệ số cho mọi sprite, ghi số cuối.
   - WebP màu: chất lượng 86–90, `-define webp:alpha-quality=100`, `-define webp:exact=true`. Thiếu `exact` thì RGB dưới alpha 0 bị xóa, mất phần nở màu.
   - WebP pháp tuyến: chất lượng 90, không alpha.
   - TK muốn KTX2 khi có `toktx`. Chưa có, nên manifest ghi `"format": "webp"`.
6. **Manifest** `public/assets/typing-defense/scenery/manifest.json`. Khung tối thiểu cho billboard của L3:

   ```json
   {
     "version": 1, "region": "meadow", "format": "webp",
     "uvOrigin": "top-left", "alphaCutoff": 0.5, "marginPx": 8, "bleedPx": 8,
     "tiers": {
       "high":   { "size": 4096, "color": "meadow/color.high.webp",   "normal": "meadow/normal.high.webp" },
       "medium": { "size": 2048, "color": "meadow/color.medium.webp", "normal": "meadow/normal.medium.webp" }
     },
     "shadow": { "size": 1024, "file": "meadow/shadow.high.webp", "tiers": ["high"] },
     "normal": { "space": "tangent", "x": "right", "y": "up", "encode": "n*0.5+0.5" },
     "sprites": [
       { "id": "almond-tree-v3", "type": "almond-tree", "variant": "v3", "kind": "tree", "ink": false,
         "uv": [0, 0, 0, 0], "px": [0, 0], "foot": [0.5, 0],
         "heightM": 18, "sizeM": [0, 0], "pxPerM": 72,
         "source": "scenery/meadow/almond-tree-v3.png", "sha256": "…" }
     ]
   }
   ```

   - `uv`: [x0, y0, x1, y1] của rect có lề, chia cho cỡ atlas, gốc ở góc trên trái ảnh.
   - `px`: cỡ rect ở High.
   - `foot`: điểm chân trong rect, [0..1], tính từ trái và **từ đáy**.
   - `heightM`: từ chân tới đỉnh hộp sát. `sizeM`: cỡ quad cả lề, theo mét (`px / pxPerM`).
   - `sha256` của từng nguồn, để `--check` biết khi ảnh đổi.
   - Chỉ có mục `accepted: true`.
   - Cần thêm trường thì ghi trong đặc tả ở báo cáo. Không đổi tên các trường trên.
7. **package.json:** chỉ thêm một dòng `"td:scenery": "node scripts/td/prepare-scenery.mjs"`.
8. **Test trước, mã sau.** File `tests/td-scenery-prep.test.ts` (vitest).
   - Xếp: rect không chồng, nằm trong atlas, chia hết cho 4. Không vừa thì báo.
   - Chân: alpha giả có thân lệch tâm. y đúng hàng đặc thấp nhất (lệch ≤ 2 % chiều cao hộp sát), x đúng tâm thân.
   - Mép: RGBA giả có viền magenta. Sau khử và nở màu, không pixel nào trong dải 8 px quanh mép còn màu khóa. Phần trong không đổi byte.
   - Pháp tuyến: đĩa giả. z > 0 trong đĩa, x cùng dấu với phía mép, (0, 0, 1) ở ngoài.
   - Tập ảnh: id không trùng, `heightM` > 0, `ink` là false, mọi mục 117 và 118 `accepted: false`.
   - Manifest (chỉ đọc JSON, luôn chạy): uv trong [0, 1], rect không chồng, chỉ id đã nhận, `sizeM` khớp `px / pxPerM`.
   - Ảnh đầu ra: giải mã bằng `magick`. Không còn màu khóa ở mép. z của pháp tuyến > 0 ở mọi pixel có alpha ≥ 0,5. Cỡ đúng 4096, 2048, 1024. Bỏ qua khi thiếu WebP hay `magick`, để `pnpm check` vẫn xanh ở checkout chưa kéo media.
9. **Tờ kiểm** trong `tmp/199/`, mỗi tờ JPG dưới 1 MB.
   - `atlas.jpg`: atlas màu High trên nền ca rô, cạnh atlas pháp tuyến và tấm bóng, thu về rộng 2048.
   - `sprites.jpg`: mỗi sprite một hàng. **Ảnh giao 116 | ô atlas**, cùng cao (tờ "bản sinh | bản hậu kỳ" của §5). Thêm pháp tuyến, bản chiếu sáng thử (đèn trên trái, ramp 3 bậc, đáy tối 25 %) và vạch chân. Nhãn: id, `heightM`, `pxPerM`.
   - `edges-x4.jpg`: hai chỗ mép tệ nhất mỗi sprite, phóng ×4, không làm mượt, trên nền `#3f5a48` và trên nền trắng.
   - File ảnh trung gian của mình để riêng trong `tmp/199/work/`. Xong thì xóa: `node tools/capture-prune/prune.mjs games/.wt-td-scenery/tmp/199/work`, chạy ở gốc repo cha (chạy thử trước, rồi thêm `--apply`). Không chạy prune trên cả `tmp/199`: công cụ xóa mọi ảnh cũ hơn 30 phút mà tên không có `sheet`, nên sẽ xóa ba tờ và `pending/`. Giữ ba tờ và `pending/`.
10. **Changelog** `docs/changelog/<ngày>-scenery-atlas.md` trong worktree, tiếng Việt.

## Cấm

- Mọi lệnh git có ghi. Được dùng git chỉ đọc.
- Sửa file trong `src/**`, nhất là `src/view/3d/*` (việc của L3) và `src/kit/**`. Chạy đồng bộ kit.
- Dev server, trình duyệt, mạng, cài gói.
- Ghi vào `art-src/**` (kể cả `_review/`). Sửa, đổi tên hay xóa ảnh 116–118.
- Chỉnh màu, sáng, làm mượt hay xóa phần vẽ của tranh (`ART_ACCEPTANCE.md` §5). Ngưỡng số mâu thuẫn với tranh thì dừng, giữ tranh, ghi lại để Claude quyết.
- Đụng worktree khác (`.wt-td-1c`, `.wt-td-keys`, `.wt-td-codex` và các worktree Dragonhold, Last Line), game khác, Tu Tiên.
- Đưa ảnh vào Git. Ghi ra ngoài repo.
- Đổi luật chơi hay ván vàng.

## Kiểm (ghi số)

1. `pnpm check` xanh (ghi số test). `pnpm td:golden:check` bằng.
2. `pnpm td:scenery` chạy hai lần: lượt hai không ghi file nào. `pnpm td:scenery --check` exit 0. Ghi thời gian chạy.
3. Bảng mỗi sprite: cỡ nguồn, hộp sát, rect trong atlas, `pxPerM`, chân lệch tâm rect (% rộng; trên 15 % thì đánh dấu cho Claude), số pixel đã khử màu khóa, số pixel màu khóa còn ở mép (phải là 0), z nhỏ nhất trong vật.
4. Độ đầy atlas High (% diện tích).
5. Cỡ từng file WebP. Chạy `node scripts/td/media-budget.mjs --json` trước và sau, lưu `199/media-budget-before.json` và `199/media-budget-after.json`.
   - Phải đạt: High tổng ≤ 16 MB, Medium tổng ≤ 9 MB, bộ khởi động ≤ 3,5 MB.
   - Đích cho phần cảnh với tám cây: Medium ≤ 0,8 MB (cảnh nằm trọn trong bộ khởi động), High ≤ 2,5 MB.
   - Vượt đích thì ghi số và đề xuất cách hạ. Không hạ dưới 64 px/m ở High khi chưa hỏi Claude.
6. Lượt `--pending` (thêm 117, 118): còn vừa 4096² ở mật độ nào; byte High và Medium thêm bao nhiêu; bộ khởi động còn dưới 3,5 MB không.
7. `git check-ignore -v`: `scenery/manifest.json` không bị bỏ qua; mọi `.webp` bị bỏ qua.
8. `git status --short -uall` trong worktree chỉ có: `scripts/td/prepare-scenery.mjs`, `scripts/td/scenery-set.json`, `tests/td-scenery-prep.test.ts`, `package.json`, `public/assets/typing-defense/scenery/manifest.json`, `docs/changelog/<ngày>-scenery-atlas.md`. `git diff --stat -- src` rỗng.
9. Danh sách media cho `media:push` của Claude: đường dẫn trong checkout chính (`games/typing-defense/public/assets/typing-defense/scenery/meadow/`), cỡ, md5.

## Báo cáo phải có

- Đặc tả manifest ngắn: trường, đơn vị, gốc uv, chiều pháp tuyến, cách tính quad và chân. Đủ để L3 viết `scenery.ts` mà không cần đọc script.
- Mâu thuẫn giữa số và tranh nếu có: ảnh nào, Claude cần quyết gì.

**Xong khi:** có script, tập ảnh, manifest, test và ba tờ kiểm; chín mục kiểm đạt và có số. Claude duyệt, commit, chạy `media:push`.
