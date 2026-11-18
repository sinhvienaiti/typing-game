# Lô Codex 1 cho map 1 (28/10/2026)

**Đã tách thành phiếu (28/10, điều phối viên):** phiếu ảnh 094–099 của lô là 095–100 trong hàng (số +1); phiếu 100 của lô là 094; phiếu mã 101–105 giữ số. Xem `docs/CODEX_QUEUE.md`.

Nguồn: `MAP1_PRODUCTION.md` (cùng thư mục). Mỗi mục `## Phiếu` dưới đây tách thành `docs/codex-queue/<số>-<tên>.md`. Khối "Luật chung" ở mục 1 chép nguyên vào đầu mỗi phiếu cùng loại.

## 0. Hàng chạy

**Đã có, không viết lại:**
- Lane M1 (ảnh): 088 sân Tuyến Cuối, 089 chân dung quái Tuyến Cuối.
- Lane M2 (sửa ảnh bằng công cụ, rồi mã nhỏ): 093 liền mép ô đất Rồng, 090 từ vựng ghim Tuyến Cuối, 092 `window.__survival`, 091 từ vựng ghim Lời Gọi.

**Lô này:** ảnh trước, mã sau. Không chạy phiếu ảnh và phiếu mã cùng lúc (luật hạn mức 27/10).

| # | Phiếu | Game | Việc gốc | Loại | Model |
|---|---|---|---|---|---|
| 094 | Sáu ô đất meadow | Lời Gọi | I1 · P0 · G2 | Ảnh | `gpt-6.1-sol` high |
| 095 | Huy hiệu và chữ màn tựa | Rồng Giữ Ải | DH-14 · P1 · G5 | Ảnh | `gpt-6.1-sol` high |
| 096 | Hai tờ decal mặt đất | Lời Gọi | I2 · P1 · G2 | Ảnh | `gpt-6.1-sol` high |
| 097 | Năm ô Rice Field theo trạng thái | Lời Gọi | I3 · P1 · G2 | Ảnh | `gpt-6.1-sol` high |
| 098 | Ghost Flame: tờ tham chiếu và flipbook chết | Lời Gọi | I4 · P1 · G3 | Ảnh | `gpt-6.1-sol` high |
| 099 | Decal nứt rễ và dải bọt thác | Lời Gọi | I5 (phần còn lại) · P1 · G3 | Ảnh | `gpt-6.1-sol` high |
| 100 | Từ vựng ghim trong repo game | Rồng Giữ Ải | DH-01 · P0 · G7 | Mã nhỏ | `gpt-6.1-sol` high |
| 101 | Hai câu chữ của map 1 | Rồng Giữ Ải | DH-16 · P1 · G5 | Mã vặt | `gpt-6-luna` medium |
| 102 | Cổng DevTools không trùng | Kit (mọi game) | A11 · P1 · G1 | Mã nhỏ | `gpt-6.1-sol` high |
| 103 | Thẻ kết và dải nghĩa | Lời Gọi | A6, A8 · P2 · G5, G3 | Mã nhỏ | `gpt-6.1-sol` high |
| 104 | Ba nhãn nhỏ | Tuyến Cuối | TS-M1-18 (phần không cần quyết) · P2 · G5 | Mã nhỏ | `gpt-6.1-sol` high |
| 105 | Nút "Về cổng game", bỏ `ui-preview` ở production | Rồng Giữ Ải | DH-24, DH-23 (phần 1) · P2 · G5, G7 | Mã nhỏ | `gpt-6.1-sol` high |

**Dòng thêm vào lane** (`.local/codex-lane-mac-m1.txt` và `-m2.txt`):

```
# M1, nối sau 089
094-td-meadow-ground | docs/codex-queue/094-td-meadow-ground.md | . | high | workspace-write | gpt-6.1-sol
095-dh-title-emblem | docs/codex-queue/095-dh-title-emblem.md | . | high | workspace-write | gpt-6.1-sol
096-td-ground-decals | docs/codex-queue/096-td-ground-decals.md | . | high | workspace-write | gpt-6.1-sol
097-td-rice-field | docs/codex-queue/097-td-rice-field.md | . | high | workspace-write | gpt-6.1-sol
098-td-ghost-flame | docs/codex-queue/098-td-ghost-flame.md | . | high | workspace-write | gpt-6.1-sol
099-td-root-foam | docs/codex-queue/099-td-root-foam.md | . | high | workspace-write | gpt-6.1-sol
# M2, nối sau 091
100-dh-vocab-pin | docs/codex-queue/100-dh-vocab-pin.md | . | high | workspace-write | gpt-6.1-sol
101-dh-text-fixes | docs/codex-queue/101-dh-text-fixes.md | . | medium | workspace-write | gpt-6-luna
102-kit-cdp-port | docs/codex-queue/102-kit-cdp-port.md | . | high | workspace-write | gpt-6.1-sol
103-td-sheet-cards | docs/codex-queue/103-td-sheet-cards.md | . | high | workspace-write | gpt-6.1-sol
104-ts-small-labels | docs/codex-queue/104-ts-small-labels.md | . | high | workspace-write | gpt-6.1-sol
105-dh-portal-button | docs/codex-queue/105-dh-portal-button.md | . | high | workspace-write | gpt-6.1-sol
```

**Claude làm trước khi lane chạy:**
1. Tạo worktree Rồng cho 100, 101, 105: `git -C games/dragon-hold worktree add ../.wt-dh-codex -b dh-codex 02fe9c7`, rồi `pnpm install` trong đó.
2. Kiểm `games/.wt-td-codex` và `games/.wt-ts-codex` còn đó (091, 090, 092 dùng trước).
3. Thêm 12 dòng vào bảng `docs/CODEX_QUEUE.md`, trạng thái "Chờ chạy".
4. Nếu chủ dự án chốt tên ải 1 khác "Ải 1 · Cầu và Suối" trước khi M2 tới 101, sửa phiếu 101.

**Dự phòng:** nếu tới trưa 30/10 lane M2 chưa tới 100, làn T của Claude tự làm DH-01 theo phiếu này và bỏ 100 khỏi lane.

---

## 1. Luật chung

### 1.1. Phiếu ảnh (chép vào 094–099)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Luật điểm:** ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2). Lỗi sửa được thì sửa bằng công cụ trước (ImageMagick 7, `tools/art-normalize`, script Python hay Node viết riêng). Chưa đạt thì sửa prompt đúng chỗ thiếu, **tối đa 3 lượt sinh mỗi ảnh**.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/<số phiếu>/`, chạy lại được. Ảnh kiểm ở `_review/<số phiếu>-*.jpg`.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
  - mọi lệnh git;
  - sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, chữ ký, khung, viền trong ảnh (trừ phần chữ logo của 095).
- **Kiểm chung (bắt buộc, ghi số vào báo cáo):**
  - **KA1 md5:** `md5 -r` mọi file trong thư mục đích trước khi ghi (`_review/<số>/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
  - **KA5 tự chấm:** 5 tiêu chí của ART_ACCEPTANCE §2.2 (Đúng đề, Đọc được, Hợp bộ, Hình khối, Dùng tiếp), mỗi tiêu chí 0–2, ở cỡ đầy đủ và cỡ nhỏ nêu trong phiếu. "Dùng tiếp" chỉ được 2 khi mọi kiểm số đo của phiếu đạt.
- **Báo cáo** `docs/codex-queue/<số>-report.md`, tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm KA5; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại ≥ 8. Claude mới là người chép ảnh vào `public/` khi tích hợp.

**Đo chung cho ô đất** (094, 097; cùng cách của `067-report.md` §4 và phiếu 093):
- `L = 0,2126R + 0,7152G + 0,0722B` trên sRGB 0–1.
- **Độ rối** = trung bình `|L − box5×5(L)|`, biên tuần hoàn.
- **Mép liền:** `E` = trung bình `|L(cột 0) − L(cột N−1)|` và `|L(hàng 0) − L(hàng N−1)|`; `I` = trung bình độ lệch giữa hai px kề nhau bên trong ảnh theo X và Y. Đạt khi `E ≤ 1,25 · I`. Nếu ảnh sinh ra chưa liền, được làm liền bằng cách của phiếu 093 (`roll` nửa ô, phủ chữ thập giữa bằng mặt nạ cosin); khi đó đo thêm chữ thập: tỉ số ≤ 1,25.
- **Đốm lặp:** box-blur 129 px tuần hoàn trên `L`, lấy `p95 − p5`.

### 1.2. Phiếu mã (chép vào 100–105)

- **cwd:** repo cha `/Users/toandx/htdocs/typing-game` (để ghi báo cáo). Mã nằm trong worktree nêu ở từng phiếu; mọi đường dẫn mã tính từ worktree đó.
- **Được dùng git chỉ đọc:** `show`, `log`, `diff`, `status`, `ls-tree`. **Cấm** mọi lệnh git có ghi (`add`, `commit`, `checkout`, `reset`, `stash`, `worktree`…).
- **Cấm:**
  - sửa `src/kit/**` của game (bản chép từ kit, có kiểm sha256);
  - sửa file golden hay chạy lệnh cập nhật golden (`dh:golden:update`, `td:golden:update`…);
  - ghi vào cây chính của game (`games/<id>`), worktree khác, game khác; đụng Tu Tiên;
  - sửa file ở repo cha (nginx, `scripts/`, `shared/`), trừ khi phiếu cho phép;
  - dev server, trình duyệt (sandbox không mở được cổng); media (ảnh, âm, GLB).
- **Cách làm:** test trước, mã sau. Chú thích trong mã bằng tiếng Anh, ngắn. Chuỗi người chơi thấy: câu tiếng Việt, danh từ game tiếng Anh (`docs/games/NAMES_EN.md`).
- **Mỗi phiếu có changelog** `docs/changelog/2026-10-29-<tên>.md` trong worktree, tiếng Việt: làm gì, vì sao, số đo.
- **Báo cáo** `docs/codex-queue/<số>-report.md` và thư mục `docs/codex-queue/<số>/` (log, số đo): file đã đổi; đầu ra của từng mục Kiểm, có số; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chạy lại kiểm, đọc diff, kiểm trên trình duyệt ở 1280 và 1920 khi phiếu đụng giao diện, rồi commit trên nhánh của worktree và gộp.

---

## 2. Phiếu ảnh

## Phiếu 094 · Lời Gọi · Sáu ô đất meadow cho mặt đất 3D map 1

**Vì sao:** kiểm kê map 1 (I1, P0, cổng G2). Map 1 lên 3D (bước 1C). Mặt đất w1-silverfall vẽ bằng shader đất (C3), trộn các ô đất này theo mặt nạ đường, suối, sân Fort. Hôm nay không có ô đất nào; `art-src/scenery/meadow/` chỉ có cây, bụi, đá.

**Nơi ghi:** `games/typing-defense/art-src/scenery/meadow/ground/` (thư mục mới).

**Chỉ được ghi:**
- `ground/<tên>.tryN.png`, `ground/<tên>.tryN.prompt.txt`, `ground/<tên>.png`, `ground/<tên>.prompt.txt`;
- `games/typing-defense/art-src/_review/094-*.jpg`, `games/typing-defense/art-src/_review/094/`;
- `docs/codex-queue/094-report.md`.

**Sáu ô** (`<tên>`):

| Tên | Nội dung |
|---|---|
| `grass-a` | Cỏ đồng chính: xanh mạ non ấm, vệt cọ lớn, vài mảng sáng tối rất nhẹ |
| `grass-b-clover` | Cùng nền cỏ với `grass-a`, thêm mảng cỏ ba lá tròn cỡ 30–60 cm và vài đốm hoa trắng to; không chấm li ti |
| `dirt-road` | Đường đất nện vàng nâu, hai vệt bánh xe mờ chạy dọc ảnh, sỏi vẽ thành mảng |
| `trail-worn` | Mép đường mòn: đất nén lẫn cỏ thưa; dùng ở dải chuyển giữa cỏ và đường |
| `stream-bank` | Bờ suối: bùn ướt và sỏi cuội tròn, nâu xám ấm |
| `stone-yard` | Sân lát quanh Fort và quặng: đá ong và đá vôi trắng, viên to không đều, mạch vữa mờ |

**Thang và góc nhìn:**
- Một ô phủ 8 × 8 m trên mặt đất (1024 px, khoảng 7,8 mm mỗi px).
- Camera chơi nhìn xuống 55° từ 58 m. Chi tiết nhỏ hơn 15 cm sẽ thành nhiễu, nên vẽ bằng mảng màu lớn và vệt cọ.
- Nhìn thẳng từ trên xuống, không phối cảnh. Ánh sáng phẳng, không bóng đổ, không hướng nắng.

**Phong cách:**
- Đọc `games/typing-defense/art-src/scenery/meadow/tall-grass-v1.prompt.txt`. Giữ câu đầu về phong cách nhà (storybook, bảng màu young-rice green, ripe-rice gold, river silver, bamboo brown, limestone white).
- **Khác cây cảnh:** ô đất không có viền mực, không có vật đứng (không cây, bụi, đá nổi khối, người, vật nuôi). Chỉ có vệt cọ mềm.
- Ảnh tham chiếu màu: `games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-a.png` và các ô của `games/typing-defense/tmp/map1-audit/sheet-keyframes.jpg` (màu dải đất của bản 2D hôm nay).
- Prompt viết bằng tiếng Anh, có câu "seamless tileable texture, edges wrap on all four sides".

**Cỡ:** sinh ảnh vuông, rồi thu về 1024 × 1024 (Lanczos), sRGB 8 bit, không alpha.

**Kiểm (bắt buộc):**
1. KA1 md5 trên `games/typing-defense/art-src/scenery/`.
2. `magick identify`: 1024 × 1024, sRGB, không kênh alpha.
3. **Mép liền** (mục 1.1): `E ≤ 1,25 · I` cho cả sáu ô. Ghi `E`, `I`, tỉ số trước và sau khi làm liền.
4. **Độ rối:** hai ô cỏ ≤ 0,030; bốn ô còn lại ≤ 0,040.
5. **Đốm lặp:** `p95 − p5` ≤ 0,08 cho hai ô cỏ, ≤ 0,10 cho bốn ô còn lại.
6. **Màu đi với nhau** (trung vị trên cả ô):
   - hue của hai ô cỏ trong 75–110°; hai ô cỏ lệch nhau ≤ 8° hue và ≤ 0,05 luma (trộn không thấy ranh);
   - luma `dirt-road` ≥ luma `grass-a` + 0,08 (đường sáng hơn cỏ, đọc được làn);
   - luma `stone-yard` ≥ luma `grass-a` + 0,10, và S ≤ 0,30;
   - luma `stream-bank` ≤ luma `dirt-road` − 0,05;
   - 0 % px có hue 285–330° và S > 0,5.
7. **Ảnh kiểm:**
   - `_review/094-tiles.jpg`: mỗi ô một cột: ô ở 512 px, rồi ô lát 3 × 3 thu về 512 px;
   - `_review/094-mock.jpg`: một mặt đất thử 2048 × 1152 lát `grass-a`, có mảng `grass-b-clover`, một dải `dirt-road` viền `trail-worn`, một dải suối viền `stream-bank`, một sân `stone-yard`; mặt nạ mềm vẽ bằng script; thu về rộng 1280 px để giống khoảng cách chơi.
   Xem bằng mắt ở cỡ đầy đủ. Ghi "không thấy đường nối, không thấy lặp" hoặc chỉ chỗ thấy.
8. **KA5** ở cỡ đầy đủ và ở cỡ thu 256 px.

**Xong khi:** cả sáu ô qua mục 2–6 và tự chấm ≥ 8. Ô nào không đạt sau 3 lượt thì ghi rõ chỗ trượt và đề xuất cách khác.

---

## Phiếu 095 · Rồng Giữ Ải · Huy hiệu và chữ logo cho màn tựa

**Vì sao:** kiểm kê map 1 (DH-14, P1, cổng G5). Rồng chưa có màn tựa; mở game là gặp ngay câu hỏi tốc độ. Claude sẽ làm màn tựa trên nền cảnh map (DH-13) và cần một hình tựa.

**Lưu ý chữ:** công cụ tạo ảnh hay viết sai dấu tiếng Việt. Vì vậy phiếu tách làm hai phần. Phần A (huy hiệu không chữ) là bắt buộc. Phần B (chữ logo) là thử: chỉ nhận khi đúng hết dấu. Nếu không, Claude đặt chữ bằng font của game.

**Nơi ghi:** `games/dragon-hold/art-src/ui/title/` (thư mục mới).

**Chỉ được ghi:**
- `ui/title/title-emblem.*`, `ui/title/title-logo.*` (các dạng `.tryN.png`, `.tryN.prompt.txt`, `.png`, `.prompt.txt`, `.alpha.png`, `.256.png`);
- `games/dragon-hold/art-src/_review/095-*.jpg`, `games/dragon-hold/art-src/_review/095/`;
- `docs/codex-queue/095-report.md`.

**Phong cách:**
- Câu phong cách nhà ở dòng đầu `games/dragon-hold/art-src/backdrops/pine-river-far.prompt.txt` (storybook, rừng thông sương, moss green, pine blue, muted violet, warm cream).
- Màu Hỏa Long: xem `games/dragon-hold/art-src/ui/icons/skill-fire-breath.png`, `skill-sky-fire.png`, `dragon-heart.png`.

**Phần A, `title-emblem` (bắt buộc):**
- Hỏa Long (rồng lửa đỏ cam, bụng kem ấm, sừng và gai sẫm) cuộn quanh hoặc đậu trên một cổng ải bằng đá cũ, hai bên có cây thông, một lọn lửa nhỏ.
- Toàn khối là một huy hiệu tròn trịa, rộng hơn cao (khoảng 4 : 3), để chữ đặt bên dưới.
- Đọc được dáng ở 64 px. Không chữ, không số.
- Nền `#FF00FF` phẳng để tách; vật không có màu hồng hay tím sáng.

**Phần B, `title-logo` (thử, tối đa 3 lượt):**
- Chữ vẽ tay "Rồng Giữ Ải" màu kem ấm, viền xanh thông sẫm, ánh than hồng nhẹ; nét cọ có chân.
- Đúng từng chữ: R-ồ-n-g, G-i-ữ, Ả-i. Ba dấu phải đúng: `ồ` (o, mũ, huyền), `ữ` (ư, ngã), `Ả` (A hoa, hỏi).
- Nền `#FF00FF`.

**Hậu kỳ:** tách nền bằng `tools/art-normalize` (hay ImageMagick, ghi lệnh). Ra `<tên>.alpha.png` cạnh dài 1024 px và `<tên>.256.png` cạnh dài 256 px.

**Kiểm (bắt buộc):**
1. KA1 md5 trên `games/dragon-hold/art-src/ui/`.
2. **Tách nền sạch:** 0 % px có alpha > 0 mà hue 285–330° và S > 0,5; không viền hồng ở 4× phóng (`_review/095-edge.jpg`).
3. **Lề:** bbox của vật cách mép ảnh ≥ 32 px ở bản 1024.
4. **Ảnh kiểm** `_review/095-proof.jpg`: mỗi bản chọn trên nền tối `#14201a` và nền sáng `#efe6d2`, ở 1024, 256 và 64 px. Ghi: ở 64 px còn nhận ra rồng và cổng không.
5. **Chính tả (phần B):** cắt phóng 4× từng chữ có dấu, đặt cạnh cùng chữ in bằng một font hệ thống có dấu tiếng Việt (ghi tên font). Sai một chữ hay một dấu là loại lượt đó.
6. **KA5** ở 1024 và 256 px.

**Xong khi:** `title-emblem` có alpha, qua mục 2–4 và tự chấm ≥ 8. Phần B: hoặc một bản đúng chính tả và ≥ 8, hoặc ghi "không đạt sau N lượt, dùng font" kèm ảnh lượt tốt nhất.

---

## Phiếu 096 · Lời Gọi · Hai tờ decal mặt đất

**Vì sao:** kiểm kê map 1 (I2, P1, cổng G2). Shader đất của C3 cần decal để mặt đất không phẳng: chỗ đất mòn, ngã ba, khóm hoa, gốc cây, dấu cây luật đã chặt.

**Cần trước:** phiếu 094 (dùng `grass-a.png` để thử ghép). Nếu 094 chưa có `grass-a.png`, ghép thử trên màu phẳng `#7fa651` và ghi rõ.

**Nơi ghi:** `games/typing-defense/art-src/scenery/meadow/decals/` (thư mục mới).

**Chỉ được ghi:**
- `decals/ground-decals-a.*`, `decals/ground-decals-b.*` (bản sinh `.tryN.*` và hai nửa `-left`, `-right`; bản ghép `.png` trên nền `#FF00FF`; `.alpha.png`);
- `games/typing-defense/art-src/_review/096-*.jpg`, `games/typing-defense/art-src/_review/096/`;
- `docs/codex-queue/096-report.md`.

**Cách làm:** mỗi tờ là lưới 4 × 2, 2048 × 1024, ô 512 × 512. Sinh hai ảnh vuông 2 × 2 (bốn món mỗi ảnh), rồi ghép bằng script thành một tờ.

**Nội dung:**
- **Tờ a (đất):** đất mòn ×2, đất dưới tán (sẫm, có lá kim và lá mục) ×2, mảng ngã ba (ba nhánh đất mòn gặp nhau) ×1, mẩu lối mòn thẳng ×1, mẩu lối mòn cong ×1, chỗ đất trống nhỏ ×1.
- **Tờ b (vật nhỏ):** khóm hoa dại ×2 (trắng và vàng, điểm son nhỏ), sỏi rải ×2, lá rụng ×1, gốc cây nhìn từ trên ×1, vòng vụn gỗ (dấu cây luật đã chặt) ×1, mảng cỏ ba lá ×1.

**Luật vẽ:**
- Nhìn thẳng từ trên xuống, ánh sáng phẳng, không bóng đổ.
- Thang như 094: 128 px mỗi mét; một ô 512 px là 4 m.
- Tờ a không có viền mực; mép mềm làm bằng công cụ: sau khi tách nền, làm mềm alpha 12–24 px vào trong hình.
- Tờ b có viền mực mảnh như cây cảnh meadow, mép rõ.

**Kiểm (bắt buộc):**
1. KA1 md5 trên `games/typing-defense/art-src/scenery/`.
2. `.alpha.png` đúng 2048 × 1024, RGBA. Đủ 8/8 ô có vật; bbox mỗi vật cách mép ô ≥ 24 px; vật chiếm ≥ 35 % diện tích ô.
3. **Tách nền sạch:** 0 % px có alpha > 0 mà hue 285–330° và S > 0,5.
4. **Mép mềm của tờ a:** trong mỗi ô, px có alpha 0,1–0,9 chiếm ≥ 10 % số px có alpha > 0.
5. **Màu:** hue trung vị các món đất của tờ a lệch ≤ 12° so với `dirt-road.png` của 094.
6. **Ảnh kiểm** `_review/096-on-grass.jpg`: mỗi món ghép lên `grass-a.png` đúng thang (ô decal 512 px trên ô đất 1024 px), thu về rộng 1280 px. Ghi: món nào trông như dán, món nào hòa vào đất.
7. **KA5** ở cỡ đầy đủ và cỡ thu 128 px mỗi ô.

**Xong khi:** hai tờ qua mục 2–5 và tự chấm ≥ 8.

---

## Phiếu 097 · Lời Gọi · Năm ô Rice Field theo trạng thái

**Vì sao:** kiểm kê map 1 (I3, P1, cổng G2). Ở 3D, Rice Field đổi mặt ruộng theo trạng thái (C6). Hôm nay chưa có ảnh nào.

**Nơi ghi:** `games/typing-defense/art-src/scenery/meadow/rice/` (thư mục mới).

**Chỉ được ghi:**
- `rice/<tên>.tryN.png`, `rice/<tên>.tryN.prompt.txt`, `rice/<tên>.png`, `rice/<tên>.prompt.txt`;
- `games/typing-defense/art-src/_review/097-*.jpg`, `games/typing-defense/art-src/_review/097/`;
- `docs/codex-queue/097-report.md`.

**Năm ô:** `rice-flooded` (bùn ngập nước, ánh trời bạc, chưa cấy), `rice-seedling` (mạ non), `rice-green` (lúa xanh), `rice-ripe` (lúa chín vàng), `rice-stubble` (gốc rạ).

**Luật vẽ:**
- Nhìn thẳng từ trên xuống, ánh sáng phẳng, liền mép cả bốn phía, 1024 × 1024, sRGB, không alpha.
- Một ô phủ 4 × 4 m. Hàng lúa chạy dọc ảnh, đúng 8 hàng mỗi ô, cách đều 128 px.
- Bốn ô có cây (`seedling`, `green`, `ripe`, `stubble`) có hàng ở **cùng vị trí**, để đổi trạng thái không bị nhảy. Cách đề xuất: sinh `rice-green` trước, rồi dùng nó làm ảnh tham chiếu cho ba ô kia; được dời ngang bằng công cụ cho khớp hàng.
- Phong cách như 094 (không viền mực, vệt cọ lớn).

**Kiểm (bắt buộc):**
1. KA1 md5 trên `games/typing-defense/art-src/scenery/`.
2. `magick identify`: 1024 × 1024, sRGB, không alpha.
3. **Mép liền** (mục 1.1): `E ≤ 1,25 · I` cho cả năm ô.
4. **Hàng lúa** (bốn ô có cây): lấy trung bình `L` theo từng cột, tính tự tương quan. Chu kỳ 128 ± 4 px. Độ lệch pha giữa hai ô bất kỳ ≤ 8 px.
5. **Màu** (trung vị):
   - `rice-seedling`, `rice-green`: hue 80–120°;
   - `rice-ripe`: hue 40–55°;
   - `rice-stubble`: hue 25–50°, S ≤ 0,35;
   - `rice-flooded`: S ≤ 0,30, luma 0,45–0,65.
6. **Ảnh kiểm:**
   - `_review/097-states.jpg`: năm ô cạnh nhau ở 512 px, rồi mỗi ô lát 3 × 3 thu về 512 px;
   - `_review/097-swap.gif` hoặc tờ 4 khung: cùng một chỗ đổi `seedling` → `green` → `ripe` → `stubble`, để thấy hàng có nhảy không.
7. **KA5** ở cỡ đầy đủ và 256 px.

**Xong khi:** năm ô qua mục 2–5 và tự chấm ≥ 8.

---

## Phiếu 098 · Lời Gọi · Ghost Flame: tờ tham chiếu và flipbook chết

**Vì sao:** kiểm kê map 1 (I4, P1, cổng G3). Ghost Flame không có model; trong game là sprite VFX. Flipbook bay lượn `ma-troi-wisp` đã có từ phiếu 043 (9/10). Còn thiếu: tờ tham chiếu (`ma-troi-sheet.prompt.txt` có prompt mà chưa có ảnh) và cảnh chết (lửa tắt thành tia lấp lánh như thủy tinh), để C7 và C11 làm cái chết theo loài.

**Nơi ghi:** `games/typing-defense/art-src/vfx/`.

**Chỉ được ghi:**
- `vfx/ma-troi-sheet.tryN.png`, `vfx/ma-troi-sheet.tryN.prompt.txt`, `vfx/ma-troi-sheet.png` (file mới; **không sửa** `ma-troi-sheet.prompt.txt` có sẵn);
- `vfx/ma-troi-death.tryN.png`, `.tryN.prompt.txt`, `vfx/ma-troi-death.png`, `.prompt.txt`, `.alpha.png`;
- `games/typing-defense/art-src/_review/098-*.jpg`, `games/typing-defense/art-src/_review/098/`;
- `docs/codex-queue/098-report.md`.

**Phần A, `ma-troi-sheet`:** sinh đúng theo `ma-troi-sheet.prompt.txt` (tờ tham chiếu, nền xanh navy, không cần alpha). Dùng cho giám khảo và làn VFX, không vào game.

**Phần B, `ma-troi-death`:**
- Mở đầu bằng hai đoạn đầu của `vfx/ma-troi-wisp.prompt.txt` (phong cách nhà và luật FLIPBOOK lưới 4 × 4, 1024², ô 256, lề ≥ 24 px).
- FLIPBOOK một lần, 16 khung, nền đen `#000000`:
  - khung 1 giống khung 1 của `ma-troi-wisp` về cỡ và màu;
  - khung 2–5: lửa co lại, chập chờn, mắt nhắm ở khung 4–5;
  - khung 6–10: vỡ thành 6–10 tia nhỏ trắng xanh như thủy tinh;
  - khung 11–16: tia rơi chậm, nhỏ dần tới hết; không mờ dần kiểu trong suốt.
- Hậu kỳ alpha theo cách của phiếu 043: đổi ảnh sáng trên nền đen sang RGBA thẳng (`games/typing-defense/art-src/_review/043/refine-alpha.py`; ghi bản đã dùng).

**Kiểm (bắt buộc):**
1. KA1 md5 trên `games/typing-defense/art-src/vfx/`: chỉ có file mới; `ma-troi-sheet.prompt.txt` và `ma-troi-wisp.*` giữ nguyên md5.
2. `ma-troi-death.alpha.png`: 1024 × 1024, RGBA; đủ 16/16 ô có hình; lề ≥ 24 px mỗi ô; viền nền 0 px (như 043).
3. **Khớp với wisp:** bbox khung 1 lệch ≤ 10 % so với bbox khung 1 của `ma-troi-wisp.alpha.png`; hue trung vị lệch ≤ 10°.
4. **Tắt hẳn:** tổng alpha khung 16 ≤ 5 % tổng alpha khung 1.
5. **Ảnh kiểm** `_review/098-sheet.jpg`: 16 khung thu về ô 64 px trên `backdrops/w1-silverfall/sky-a.png` và trên cùng nền nhân RGB 0,25 (như 043); cạnh đó là `ma-troi-sheet.png`.
6. **KA5:** `ma-troi-death` ở cỡ đầy đủ và ô 64 px; `ma-troi-sheet` chỉ chấm Đúng đề và Hợp bộ.

**Xong khi:** `ma-troi-death` qua mục 2–4 và tự chấm ≥ 8; `ma-troi-sheet` có ảnh đúng prompt.

---

## Phiếu 099 · Lời Gọi · Decal nứt rễ báo trước và dải bọt thác

**Vì sao:** kiểm kê map 1 (I5, P1, cổng G3). Phiếu 043 đã xong phần chấm lại và ba ảnh mới. Còn thiếu hai ảnh cho bước 1C:
- đòn Rễ Trồi của Mộc Tinh phải có decal báo trước trên đất ≥ 1,2 s (C8, VFX_STANDARD pha A);
- vách Thác Bạc cần dải bọt chảy lặp được (C9).

**Nơi ghi:** `games/typing-defense/art-src/vfx/`.

**Chỉ được ghi:**
- `vfx/root-crack-warn.*`, `vfx/waterfall-foam.*` (`.tryN.png`, `.tryN.prompt.txt`, `.png`, `.prompt.txt`, `.alpha.png`);
- `games/typing-defense/art-src/_review/099-*.jpg`, `games/typing-defense/art-src/_review/099/`;
- `docs/codex-queue/099-report.md`.

**Phong cách:** mở đầu bằng hai đoạn đầu của `vfx/ma-troi-wisp.prompt.txt`, như phiếu 043.

**`root-crack-warn`:**
- FLIPBOOK một lần, 16 khung, lưới 4 × 4, 1024², nền `#FF00FF` (mép rõ, mềm bằng dải tông bên trong).
- Nhìn thẳng từ trên xuống: các vết nứt mực tím nâu sẫm, giữa mỗi vết có một đường sáng mảnh màu son cam (màu báo nguy), tỏa ra từ tâm ô.
- Khung 1–10: vết nứt lan từ tâm ra tới ≥ 80 % bán kính ô. Khung 11–16: giữ nguyên, sáng lên hai nhịp.
- Đọc được ở ô 64 px.

**`waterfall-foam`:**
- Texture lặp theo chiều dọc (cuộn từ trên xuống), 1024², nền đen `#000000`.
- Vệt bọt trắng bạc với hai ba dải tông xanh xám, sọc chạy dọc, không có vật khác.
- Alpha lấy theo độ sáng như hai ảnh lặp của 043. Mép trái và phải mờ dần trong 4 % bề rộng (làm bằng công cụ).

**Kiểm (bắt buộc):**
1. KA1 md5 trên `games/typing-defense/art-src/vfx/`: chỉ có file mới.
2. `root-crack-warn.alpha.png`: 16/16 ô; lề ≥ 24 px; 0 % px có alpha > 0 mà hue 285–330° và S > 0,5; diện tích alpha không giảm từ khung 1 tới khung 10; ở khung 10 vết nứt chạm ≥ 80 % bán kính ô.
3. `waterfall-foam.alpha.png`: liền mép trên dưới, `E ≤ 1,25 · I` đo theo Y trên cả `L` và alpha; alpha trung bình ở 4 % cột ngoài cùng mỗi bên ≤ 0,05.
4. **Ảnh kiểm:**
   - `_review/099-crack.jpg`: 16 khung ở ô 64 px ghép lên `grass-a.png` của 094 (nếu chưa có thì nền `#7fa651`);
   - `_review/099-foam.jpg`: dải bọt lát 1 × 3 theo chiều dọc trên màu vách đá `#8a8f94`.
5. **KA5** ở cỡ đầy đủ và cỡ nhỏ (ô 64 px; bọt thu về 256 px).

**Xong khi:** hai ảnh qua mục 2–3 và tự chấm ≥ 8.

---

## 3. Phiếu mã

## Phiếu 100 · Rồng Giữ Ải · Bản chép từ vựng ghim trong repo game (cổng G7)

**Vì sao:** kiểm kê map 1 (DH-01, P0, cổng G7). Bản build không có `/vocabulary/`. Trên server tĩnh, `/vocabulary/index.json` trả 404: quái không có chữ, Hỏa Long thua ở đợt 1, người chơi không được báo gì. Hôm nay từ vựng chỉ có nhờ alias nginx hay plugin dev trỏ tới `shared/` của repo cha. Thiết kế: `docs/games/DEPLOY_INDEPENDENCE.md` §3 dòng 1 và 3, §8. Làm như phiếu 090 (Tuyến Cuối) và 091 (Lời Gọi).

**Nơi làm:** worktree `games/.wt-dh-codex` (nhánh `dh-codex`, tách từ `main` `02fe9c7`; Claude tạo sẵn và cài `node_modules`).

**Chỉ được ghi:**
- `public/vocabulary/**` (file mới);
- `vocab.config.json` (mới);
- `tests/vocab-pin.test.ts` (mới);
- `vite.config.ts`;
- `docs/changelog/2026-10-29-vocab-pin.md` (mới);
- `docs/codex-queue/100-report.md`, `docs/codex-queue/100/`.

**Cấm thêm** (ngoài luật chung): sửa `src/**`, kể cả nơi tải `/vocabulary/` (trang vẫn tải như cũ, Vite tự phục vụ `public/`); sửa `scripts/balance/**`.

**Việc:**
1. **Số trước:** chạy `pnpm test` trong worktree, ghi số test đạt vào `docs/codex-queue/100/before.txt`.
2. **Danh sách file:** `git -C /Users/toandx/htdocs/typing-game ls-tree --name-only 18338405eebd9cfdbd6d6bf666ea79361c00a564 shared/vocabulary/levels/`. Phải có đủ `001.json` tới `100.json`; thiếu thì dừng và báo.
3. **Chép bản ghim** (pin `18338405eebd9cfdbd6d6bf666ea79361c00a564`, commit cuối có sửa `shared/vocabulary`, 27/10). Với `index.json`, `levels/001.json` … `levels/100.json`, `ATTRIBUTION.md`: `git -C /Users/toandx/htdocs/typing-game show <pin>:shared/vocabulary/<file> > games/.wt-dh-codex/public/vocabulary/<file>`. Không đọc cây làm việc của `shared/`.
4. **`vocab.config.json`** ở gốc worktree: `{ "pin": "<40 ký tự>", "files": [ 102 đường ở trên, theo thứ tự đó ] }`.
5. **`public/vocabulary/vocab-manifest.json`:** `{ "pin", "version" (lấy từ index.json), "files": { "<đường>": "<sha256 hex>" } }`; khóa xếp theo chữ; thụt 2 dấu cách; có xuống dòng cuối file.
6. **`vite.config.ts`:** bỏ `serveSharedFolders`, hằng `sharedRoot` và dòng import nếu không còn dùng. Sửa chú thích: từ vựng nay ở `public/vocabulary/`, bản ghim theo `vocab.config.json`. Nếu plugin còn phục vụ đường nào khác ngoài `/vocabulary/` và `/typing-texts/` thì dừng và báo.
7. **Test `tests/vocab-pin.test.ts`** (vitest, chỉ đọc file trong repo game):
   - đủ 102 file của config, sha256 khớp manifest;
   - `pin` của manifest bằng của config; `version` của manifest bằng của `index.json`;
   - **mọi level mã có thể hỏi đều có file.** Tìm trong `src/app/learning.ts` (khoảng dòng 315) và `src/kit/vocab/` mức level lớn nhất có thể lưu và việc tải `[L, L+1]`. Test lấy giới hạn đó từ mã (import hằng nếu có), không ghi số cứng. Nếu mã có thể hỏi level 101 thì ghi vào báo cáo như một lỗi cho Claude, không sửa `src/`;
   - không file nào trong `src/` (trừ `src/kit/**`), `tests/`, `scripts/`, `vite.config.ts` đọc đường `shared/vocabulary`.
8. **Changelog** `docs/changelog/2026-10-29-vocab-pin.md`: làm gì, vì sao (G7), cách cập nhật bản ghim (chạy lại bước 2–5 với pin mới), cỡ thêm vào gói deploy (khoảng 2,67 MB, lần chơi đầu chỉ tải level L và L+1).

**Kiểm (bắt buộc, ghi đầu ra vào báo cáo):**
1. `pnpm check` trong worktree xanh (verify-kit, test, build). Số test sau = trước + số ca của `vocab-pin.test.ts`.
2. **Golden giữ:** `tests/golden/golden.test.ts` đạt; `git -C games/.wt-dh-codex diff --stat -- tests/golden` rỗng.
3. **Đứng riêng:** chép worktree (trừ `node_modules`) sang thư mục tạm **ngoài** repo cha (ví dụ `$TMPDIR/dh-100-alone/game`), `ln -s` thư mục `node_modules` của worktree vào. Ở đó `pnpm test` xanh, `pnpm build` xong, và `dist/vocabulary/` có đủ 102 file cộng manifest, cùng sha256. Xóa thư mục tạm sau khi ghi số.
4. **Đột biến** (mỗi cái chạy `pnpm vitest run tests/vocab-pin.test.ts`, phải đỏ; xong thì trả lại): đổi một byte của `levels/050.json`; xóa dòng `ATTRIBUTION.md` khỏi manifest; đổi `pin` trong config; xóa file `levels/100.json`.
5. `grep -rn "shared/vocabulary" src tests scripts vite.config.ts`: chỉ còn trong `src/kit/**`. Dán đầu ra.
6. `git -C games/.wt-dh-codex status --short`: chỉ có các file trong "Chỉ được ghi". Dán đầu ra.

**Xong khi:** sáu mục Kiểm đạt. Sau đó Claude: kiểm bản build trên server tĩnh không alias (quái có chữ, 0 request hỏng), làm DH-02 (thông báo khi deck rỗng, bỏ alias nginx), commit và gộp.

---

## Phiếu 101 · Rồng Giữ Ải · Hai câu chữ của map 1

**Vì sao:** kiểm kê map 1 (DH-16, P1, cổng G5).
- Tên ải 1 vẫn ghi "Bản thử: Cầu và Suối".
- Câu thua khi chưa gõ phím nào nói "Hỏa Long dùng Fire Breath", nhưng Fire Breath là chiêu riêng (phím chiêu 1). Đòn chữ là phun lửa thường.

**Nơi làm:** worktree `games/.wt-dh-codex`, **sau phiếu 100**. Giữ nguyên mọi thay đổi của 100.

**Chỉ được ghi:**
- `src/content/data/stages.ts` (chỉ dòng `nameVi` của ải 1, khoảng dòng 13);
- `src/ui/results.ts` (chỉ câu của nhánh `cause === "typing"` trong `starHint`, khoảng dòng 196);
- file test trong `tests/` đang khớp hai chuỗi cũ (tìm bằng `grep -rn "Bản thử\|dùng Fire Breath hạ" tests`);
- `docs/changelog/2026-10-29-text-fixes.md` (mới);
- `docs/codex-queue/101-report.md`.

**Việc:**
1. `nameVi: "Bản thử: Cầu và Suối"` → `nameVi: "Ải 1 · Cầu và Suối"` (dấu `·` U+00B7, có cách hai bên).
2. Câu thua: `". Gõ chữ trên đầu quái để Hỏa Long dùng Fire Breath hạ chúng."` → `". Gõ chữ trên đầu quái để Hỏa Long phun lửa vào chúng."`. Không đổi câu của nhánh `blight` và nhánh cuối.
3. Sửa test theo chuỗi mới. Thêm một ca nếu chưa có test nào kiểm câu của nhánh `typing`.

**Kiểm (bắt buộc):**
1. `pnpm check` xanh.
2. `grep -rn "Bản thử" src tests`: rỗng. `grep -rn "Fire Breath hạ" src tests`: rỗng.
3. Golden giữ: `git -C games/.wt-dh-codex diff --stat -- tests/golden` rỗng.
4. `git -C games/.wt-dh-codex diff --stat`: chỉ các file trong "Chỉ được ghi" và file của phiếu 100.

**Xong khi:** bốn mục đạt. Claude xem thẻ đợt, màn kết quả ở 1280 và 1920 để chắc chữ không tràn.

---

## Phiếu 102 · Kit · Cổng DevTools không trùng khi nhiều làn chạy song song

**Vì sao:** kiểm kê map 1 (A11, P1, cổng G1). `cdp-run.mjs` chọn cổng DevTools ngẫu nhiên `9300 + random * 600`. Ngày 28/10, ba làn trình duyệt chạy song song đã trùng cổng: script của làn Rồng điều khiển Chrome của lượt Lời Gọi 1920 sang trang Rồng ở giây 171. Bằng chứng hỏng mà không báo gì.

**Nơi làm:** repo cha, thư mục `shared/game-kit/tools/`. (Claude có thể cho chạy trong một worktree repo cha sạch như phiếu 037; khi đó mọi đường dưới đây tính từ worktree đó.)

**Chỉ được ghi:**
- `shared/game-kit/tools/cdp-run.mjs`;
- `shared/game-kit/tools/cdp-port.mjs` (mới);
- `shared/game-kit/tools/cdp-port.test.ts` (mới);
- `shared/game-kit/DRIFT.md` (thêm một mục ngắn: sửa gì so với bản nguồn của Space);
- `docs/codex-queue/102-report.md`, `docs/codex-queue/102/`.

**Cấm thêm:** sửa bản chép trong game (`games/*/src/kit/tools/cdp-run.mjs`, `games/dragon-hold/scripts/visual/cdp-run.mjs`, `games/space-typing/scripts/visual/cdp-run.mjs`); chạy Chrome; chạy `kit:sync`. Phần đó Claude làm sau.

**Việc:**
1. **`cdp-port.mjs`**, hai hàm thuần, chú thích tiếng Anh:
   - `portArg(env)`: nếu `env.CDP_PORT` có giá trị thì phải là số nguyên 1024–65535, trả `{ arg: "--remote-debugging-port=<N>", fixed: N }`; giá trị sai thì ném lỗi nêu giá trị. Không có thì trả `{ arg: "--remote-debugging-port=0", fixed: null }`.
   - `readActivePort(profileDir, { timeoutMs = 10000, pollMs = 50, readFile, now, sleep })`: đọc `<profileDir>/DevToolsActivePort`, lấy dòng đầu làm cổng. Chưa có file thì chờ và đọc lại tới hết giờ. Hết giờ thì ném lỗi có đường file. Dòng đầu không phải số nguyên 1–65535 thì ném lỗi ngay. `readFile`, `now`, `sleep` truyền vào được để test không phải chờ thật.
2. **`cdp-run.mjs`:** bỏ `Math.random`. Dùng `portArg(process.env)` khi mở Chrome. Nếu `fixed` là `null` thì lấy cổng bằng `readActivePort(profile)` (thư mục profile đã là `mkdtempSync` riêng mỗi lượt) trước khi nối tới `/json/version`. Giữ nguyên mọi hành vi khác và mọi cờ Chrome.
3. **`cdp-port.test.ts`** (vitest của kit, `shared/game-kit/vitest.config.ts`):
   - file có `"9222\n/devtools/browser/abc"` thì ra 9222;
   - file chưa có ở hai lần đọc đầu, có ở lần ba thì ra đúng cổng, và số lần gọi `sleep` khớp;
   - file không bao giờ có thì ném lỗi có đường file khi hết giờ (đồng hồ giả, không chờ thật);
   - dòng đầu là `abc`, `0`, `70000` thì ném lỗi;
   - `CDP_PORT=9555` ra `fixed: 9555`; `CDP_PORT=abc`, `CDP_PORT=80` ném lỗi; không có `CDP_PORT` ra cổng 0.

**Kiểm (bắt buộc):**
1. `pnpm --dir shared/game-kit test` xanh; ghi số test trước và sau.
2. `pnpm --dir shared/game-kit typecheck` sạch.
3. `node --check shared/game-kit/tools/cdp-run.mjs` đạt.
4. `grep -n "Math.random\|9300" shared/game-kit/tools/cdp-run.mjs`: rỗng.
5. **Đột biến:** bỏ bước đọc lại khi chưa có file; bỏ kiểm khoảng của `CDP_PORT`. Mỗi đột biến phải làm test đỏ; xong thì trả lại.
6. `git status --short -- shared/game-kit`: chỉ các file trong "Chỉ được ghi".

**Xong khi:** sáu mục đạt. Sau đó Claude: `kit:sync` vào bốn game, sửa tay bản riêng của Rồng và Space, rồi chạy 3 lượt song song × 20 lần: 0 lượt trùng cổng.

---

## Phiếu 103 · Lời Gọi · Thẻ kết và dải nghĩa lúc rời đi

**Vì sao:** kiểm kê map 1 (A6, A8, P2).
- **A6:** thẻ kết ghi "Knowledge 0" cả khi không chơi chế độ Học (`src/ui/sheets.ts:96`).
- **A8:** dải nghĩa lúc thẻ rời đi đè lên thẻ kế ("kind · loại, hạng, kiểu" dưới "walk", Đêm 3, 1280). Bước tách cột chưa tính hộp của dải nghĩa (trạng thái `mean`, `src/view/words/cards.ts`).

**Nơi làm:** worktree `games/.wt-td-codex` (nhánh `td-codex`), **sau phiếu 091**. Giữ nguyên mọi thay đổi của 091.

**Chỉ được ghi:**
- `src/ui/sheets.ts`;
- `src/view/words/cards.ts`, `src/view/words/lanes.ts`;
- test mới hoặc sửa trong `tests/` cho hai việc này;
- `docs/changelog/2026-10-29-sheet-cards.md` (mới);
- `docs/codex-queue/103-report.md`, `docs/codex-queue/103/`.

**Trần cứng (Lời Gọi đang sát trần):**
- gói `/` gzip hôm nay 84,91 kB, trần 85,00 kB: sau phiếu không được vượt trần;
- mã `.ts` 10.499 / 10.500 dòng: sau phiếu không được vượt 10.500. Nếu phải thêm dòng, rút gọn trong cùng file mà không đổi hành vi. Không làm được thì dừng ở A6 và báo phần A8.

**Việc:**
1. **A6:** chỉ hiện dòng "Knowledge" khi ván ở chế độ `learn` hoặc `w.knowledge > 0`. Lấy chế độ từ chỗ đang dựng thẻ kết (kiểu `Mode`, xem `src/app/retry.ts`). Ghi vào báo cáo cách lấy chế độ.
2. **A8:** đưa hộp của dải nghĩa (thẻ ở trạng thái `mean`, kéo dài `MS.mean` = 1000 ms) vào bước tách cột, để thẻ kế không nằm đè lên dải nghĩa. Không đổi thời gian, màu, chữ của thẻ.
3. **Test:**
   - A6: thẻ kết ngoài chế độ Học với `knowledge = 0` không có chữ "Knowledge"; chế độ Học có; ngoài Học mà `knowledge = 3` có.
   - A8: nếu bước tách cột là hàm thuần thì thêm ca: hai thẻ cùng cột, thẻ trên đang `mean`, thẻ dưới không chồng lên hộp dải nghĩa. Nếu chưa thuần, tách phần tính hộp ra hàm thuần nhỏ và test hàm đó.

**Kiểm (bắt buộc):**
1. `pnpm test`: số đạt sau = trước + ca mới; `tsc` sạch.
2. `pnpm td:golden:check` giống hệt.
3. `pnpm build`: ghi cỡ gzip của gói `/` trước và sau.
4. Đếm dòng `.ts` theo cách của repo (tìm script hay test trần dòng trong `tests/`, ghi tên): trước và sau.
5. **Đột biến:** bỏ điều kiện chế độ của A6; bỏ hộp dải nghĩa khỏi bước tách cột. Mỗi cái phải làm test đỏ.
6. `git -C games/.wt-td-codex status --short`: chỉ các file trong "Chỉ được ghi" và file của 091.

**Xong khi:** sáu mục đạt và hai trần giữ. Sau đó Claude chạy `td-1b-story`, `td-theme` và cảnh Đêm 3 ở 1280 và 1920.

---

## Phiếu 104 · Tuyến Cuối · Ba nhãn nhỏ

**Vì sao:** kiểm kê map 1 (TS-M1-18, P2, cổng G5). Phiếu này chỉ làm ba việc không cần chủ dự án quyết. Tên ải 2 và kiểu chữ hoa của biển "Swarm RÚT LUI!" chờ chủ dự án (HANDOFF §5), **không sửa**.

**Nơi làm:** worktree `games/.wt-ts-codex` (nhánh `ts-codex`), **sau phiếu 090 và 092**. Giữ nguyên thay đổi của hai phiếu đó.

**Chỉ được ghi:**
- `src/view/hud.ts`;
- `src/view/screens-journey.ts`, `src/view/screens.ts`;
- file định nghĩa `ruleDetail` và `LEARN_RULES` nếu nằm ở file khác (ghi tên vào báo cáo; chỉ sửa chuỗi);
- test mới hoặc sửa trong `tests/`;
- `docs/changelog/2026-10-29-small-labels.md` (mới);
- `docs/codex-queue/104-report.md`.

**Cấm thêm:** sửa `src/sim/**`, `src/content/**` (trừ chuỗi `ruleDetail` nếu nằm ở đó); đổi luật, số, thứ tự màn.

**Việc:**
1. **Bến 3:** bản R1 chưa có Mốc, nên bỏ chữ "MỞ Ở MỐC" ở `hud.ts:161`. Bến 3 khóa hiện cùng dấu khóa như bến 4. Sửa chú thích ở `hud.ts:18` cho đúng.
2. **Esc ở thẻ ải:** hôm nay không làm gì. Cho Esc quay về màn nạp súng, giữ bộ súng đã chọn. Theo cách các màn khác đang xử lý Esc.
3. **Câu Luật học** (`screens-journey.ts:67`, phần `ruleDetail(stage)`): viết lại mỗi câu tối đa 14 từ, câu tiếng Việt thường, danh từ game tiếng Anh, bỏ thuật ngữ nội bộ. Ghi bảng câu cũ và câu mới vào báo cáo để Claude duyệt chữ.

**Kiểm (bắt buộc):**
1. `pnpm check` xanh; ghi số test trước và sau.
2. **Băm chương giữ:** `node --import tsx scripts/chapter-hashes.ts` trước và sau, `diff` rỗng (152 dòng).
3. `grep -rn "MỞ Ở MỐC" src`: rỗng.
4. Test cho Esc ở thẻ ải nếu màn có bộ test DOM; nếu không, ghi rõ để Claude kiểm bằng `survival-s1-loadout`.
5. `git -C games/.wt-ts-codex status --short`: chỉ các file trong "Chỉ được ghi" và file của 090, 092.

**Xong khi:** năm mục đạt. Claude kiểm thẻ ải, nạp súng, đầu bến ở 1280 và 1920.

---

## Phiếu 105 · Rồng Giữ Ải · Nút "Về cổng game" ở màn kết quả; bỏ `ui-preview` khỏi bản production

**Vì sao:** kiểm kê map 1.
- **DH-24 (P2, G5):** màn kết quả chỉ có "Chơi lại"; không có lối về cổng game.
- **DH-23 phần 1 (P2, G7):** bản build còn chunk `ui-preview` (trang thử HUD trên thế giới giả, `src/main.ts:15`), chỉ cần ở dev.
- Hàm lấy địa chỉ cổng game viết một lần ở đây; màn tựa (DH-13) và màn cài đặt (DH-15) của Claude dùng lại.

**Nơi làm:** worktree `games/.wt-dh-codex`, **sau phiếu 100 và 101**. Giữ nguyên thay đổi của hai phiếu đó.

**Chỉ được ghi:**
- `src/app/portal.ts` (mới);
- `src/ui/results.ts` và file CSS của màn kết quả (ghi tên);
- `src/main.ts` (chỉ dòng nạp `ui-preview`);
- `tests/app/portal.test.ts` (mới), test màn kết quả trong `tests/ui/`;
- `docs/changelog/2026-10-29-portal-button.md` (mới);
- `docs/codex-queue/105-report.md`, `docs/codex-queue/105/`.

**Cấm thêm:** sửa `src/kit/learning/**` (nguồn portal trong kit là việc của DEPLOY_INDEPENDENCE §9, Claude làm sau).

**Việc:**
1. **`src/app/portal.ts`:** `export function portalHome(origins: string | undefined): string`. Lấy nguồn đầu tiên khác rỗng trong danh sách phân cách dấu phẩy (đã `trim`); không có thì `"https://typing-game.local"`. Trả về nguồn đó cộng `/`. Chỗ gọi truyền `import.meta.env.VITE_PORTAL_ORIGINS`.
2. **Màn kết quả:**
   - thêm nút thứ hai "Về cổng game", nhãn phím `Esc` theo kiểu của nút "Chơi lại" (`keyLabel`);
   - nút là thẻ `<a href="<portalHome>" target="_top">`, để khi game nằm trong khung của portal thì cả trang về cổng;
   - phím mũi tên trái, phải, lên, xuống chuyển tiêu điểm giữa hai nút; Enter bấm nút đang chọn; Esc bấm "Về cổng game";
   - nếu Esc ở màn kết quả đang có việc khác thì dừng và báo, không đổi.
3. **`src/main.ts:15`:** chỉ nạp `./ui/ui-preview` khi `import.meta.env.DEV`, để Vite bỏ chunk này khỏi bản production. Sửa chú thích dòng 3 cho đúng.
4. **Test:**
   - `portalHome(undefined)`, `portalHome("")`, `portalHome(" https://a.example , https://b.example")`;
   - màn kết quả có hai nút; Esc kích hoạt nút về cổng; mũi tên chuyển tiêu điểm.

**Kiểm (bắt buộc):**
1. `pnpm check` xanh; ghi số test trước và sau.
2. Golden giữ: `git -C games/.wt-dh-codex diff --stat -- tests/golden` rỗng.
3. Sau `pnpm build`: `ls dist/assets | grep -i preview` rỗng; `grep -l "startUiPreview" dist/assets/*.js` rỗng. Ghi tổng cỡ `dist/assets/*.js` trước và sau.
4. **Đột biến:** bỏ điều kiện `import.meta.env.DEV` thì kiểm 3 phải thấy chunk; đổi giá trị mặc định của `portalHome` thì test phải đỏ.
5. `git -C games/.wt-dh-codex status --short`: chỉ các file trong "Chỉ được ghi" và file của 100, 101.

**Xong khi:** năm mục đạt. Claude kiểm màn thắng và màn thua ở 1280 và 1920, bằng phím, cả khi mở trong portal qua `https://typing-game.local`.

---

## 4. Để lô sau (chưa giao)

- **I6** khung HUD 9-slice cho Lời Gọi: chỉ khi giám khảo chấm HUD dưới 8 sau C12.
- **Script kiểm deploy chung** (DH-23 phần 2, DEPLOY_INDEPENDENCE §11): `shared/game-kit/tools/deploy/`, sau khi cả ba game có từ vựng ghim.
- **`VITE_PORTAL_ORIGINS` cho cả ba game** (DEPLOY_INDEPENDENCE §9 bước A): sau 105, dùng lại cách của `portalHome`.
- **A7** nhãn kho cây của Lời Gọi: không làm ở 2D; C10 thay bằng tooltip 3D.
- **TS-M1-18 phần còn lại:** tên ải 2 và kiểu chữ biển, sau khi chủ dự án chốt.
