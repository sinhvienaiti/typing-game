# Phiếu ảnh Codex cho icon và mảnh UI nhỏ của map 1

Ngày 29/10/2026. Nguồn: `docs/games/map1/UI_IMAGERY.md`, mục 2–4 và 9.

**Đây là dàn ý.**
- Mỗi mục `## UIC-…` sẵn để tách thành `docs/codex-queue/<số>-<tên>.md`.
- Điều phối đặt số khi tách. Ngày 29/10 các số 122–129 và từ 133 còn trống.
- Khối "Luật chung" ở mục 1 chép nguyên vào đầu mỗi phiếu.

**Phạm vi:**
- Chỉ có icon, mảnh UI nhỏ và chân dung nhỏ.
- Nền, màn tựa, ảnh chủ đạo, logo và khung UI lớn thuộc làn chỉ đạo mỹ thuật (AD), phiếu từ 112.

**Phong cách:**
- Mọi phiếu ghi **"style: to take the art director's new STYLE block"**. Không chép khối STYLE sách tranh cũ.
- Khối mới nằm ở `docs/games/ART_DIRECTION_2026-10-28.md` (AD đang viết) và trong phiếu AD của từng game:
  - Wordwoven: 113, 115;
  - Dragonhold: 119;
  - Last Line: 121, đổi theo hướng chủ dự án chọn ở 112.
- Tài liệu cũ của từng game chỉ dùng cho định dạng: nền khóa, lề, cỡ, luật đọc ở cỡ nhỏ.

## 0. Thứ tự

| Thứ tự | Phiếu | Game | Số ảnh | Chờ gì |
|---|---|---|---:|---|
| 1 | UIC-WW-1 Loại lời gọi | Wordwoven | 10 | khối STYLE-UI của 115 (đã có) |
| 2 | UIC-WW-3 HUD và hệ thống | Wordwoven | 12 | như trên |
| 3 | UIC-WW-2 Tem hạng và sao | Wordwoven | 8 | như trên |
| 4 | UIC-WW-4 Nút và thẻ nhà | Wordwoven | 10 | như trên |
| 5 | UIC-DH-1 HUD và trạng thái | Dragonhold | 10 | khối STYLE-UI của 119 (đã có) |
| 6 | UIC-DH-2 Hệ thống và học | Dragonhold | 10 | như trên |
| 7 | UIC-DH-3 Bản đồ và thẻ chữ | Dragonhold | 11 | như trên |
| 8 | UIC-DH-4 Kết quả | Dragonhold | 10 | như trên |
| 9 | UIC-WW-5 Menu, âm lượng, hồ sơ | Wordwoven | 12 | — |
| 10 | UIC-WW-6 Chế độ và số kết quả | Wordwoven | 8 | — |
| 11 | UIC-LL-1 HUD trận | Last Line | 10 | **chủ dự án chọn hướng ở 112** |
| 12 | UIC-LL-2 Thẻ ải và nạp súng | Last Line | 11 | như trên |
| 13 | UIC-LL-3 Menu và kết quả | Last Line | 12 | như trên |
| 14 | UIC-LL-4 Cài đặt, hồ sơ, Rift (P2) | Last Line | 11 | như trên |
| 15 | UIC-WW-7 Mảnh UI nhỏ | Wordwoven | 7 | 115 được nhận (khớp khung) |
| 16 | UIC-DH-5 Mảnh UI nhỏ | Dragonhold | 8 | AD có khung Dragonhold, hoặc điều phối cho làm trước |
| 17 | UIC-LL-5 Mảnh UI nhỏ | Last Line | 7 | hướng 112 |
| 18 | UIC-DH-6 Chân dung rồng, huy hiệu tốc độ | Dragonhold | 7 | Claude dựng ảnh tham chiếu từ GLB rồng |
| 19 | UIC-DH-7 Chân dung quái, vải cờ | Dragonhold | 8 | Claude thử cắt chân dung từ ảnh ý tưởng trước; dưới 8 mới chạy |
| 20 | UIC-WW-8 Người làng, lính, ruộng, trạng thái | Wordwoven | 10 | — |
| 21 | UIC-WW-9 Chân dung quái | Wordwoven | 9 | — |

**Cộng:** 21 phiếu, 201 ảnh.
- Thêm 6 phiếu vẽ lại có điều kiện ở mục 5.
- Theo luật hạn mức 27/10, không chạy phiếu ảnh cùng lúc với phiếu mã trên cùng làn.

## 1. Luật chung (chép vào mọi phiếu)

**Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.

**Luật điểm:**
- Ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2), chấm **so với game thương mại**.
- Tham chiếu mức hoàn thiện: `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp`.
  - Xem HUD của ảnh đó: icon kỹ năng tròn trong vòng kim loại, khung chân dung có huy hiệu, icon hệ thống rõ nét.
  - Lấy mức hoàn thiện, không chép nội dung.
- Lỗi sửa được thì sửa bằng công cụ trước: ImageMagick 7, `tools/art-normalize`, script riêng.
- Chưa đạt thì sửa prompt đúng chỗ thiếu. Tối đa **3 lượt sinh mỗi ảnh**.

**Lượt sinh và file:**
- Mọi lượt giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3).
- Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **File giao mỗi ảnh:**
  - `<tên>.png`: bản gốc 1024 × 1024, sRGB, RGBA sau khi tách nền;
  - `<tên>.256.png`, `<tên>.128.png`, `<tên>.64.png`: thu Lanczos trực tiếp từ bản gốc;
  - không làm nét bản 64.

**Prompt:**
- Viết bằng tiếng Anh.
- Mỗi prompt = khối STYLE mới của AD cho game đó + khối KIND (ICON, PORTRAIT hay PART) của phiếu + phần riêng của ảnh + dòng nền.
- **style: to take the art director's new STYLE block.**

**Nền:**
- Theo tài liệu định dạng của game:
  - Dragonhold và Wordwoven: nền khóa phẳng `#FF00FF` (M) hay `#00FF00` (G). Chọn màu không có trong vật. Rồi tách alpha.
  - Last Line: nền trong suốt như bộ 015. Công cụ không cho trong suốt thì dùng M rồi tách.
- **Lề:** vật nằm giữa. Hộp bao (alpha > 16) có cạnh dài bằng 68–72 % cạnh ảnh, lệch tâm ≤ 2 %. Như phiếu 108.

**Cấm:**
- chữ, số, chữ cái, logo, chữ ký, khung hay viền vẽ trong ảnh. Tên tiếng Anh do game đặt bằng font;
- ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
- mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo);
- dev server, trình duyệt, mạng ngoài công cụ tạo ảnh;
- ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
- đụng `.wt-*`.

**Kiểm bắt buộc, ghi số vào báo cáo:**
1. **KA1 md5:**
   - `md5 -r` mọi file trong các thư mục đích trước khi ghi, lưu `_review/<số>/md5-before.txt`;
   - chạy lại sau khi giao, lưu `md5-after.txt`;
   - `diff` chỉ có dòng thêm.
2. **Khổ:**
   - `magick identify -format '%f %wx%h %[channels]\n'` cho mọi file giao;
   - bản gốc 1024², `srgba`; ba bản thu đúng 256², 128², 64².
3. **Alpha sạch:**
   - ngoài dải mép 3 px quanh vật, mọi pixel có alpha 0 hay 255;
   - pixel có alpha > 0 mang màu nền khóa (hue lệch ≤ 15° so với màu khóa, S > 0,5) chiếm ≤ 0,2 %;
   - ghi hai số đó cho từng ảnh.
4. **Đọc được ở cỡ trong game:**
   - thu bản gốc về đúng cỡ 720p và 1080p ghi trong bảng của phiếu;
   - đặt lên màu nền HUD của game:
     - Dragonhold: vỏ cây `#2b2118` và kem `#f1e3c4`;
     - Wordwoven: ngọc sẫm và đá vôi (lấy từ `panel-large` của 115 khi có; tạm dùng `#1f3b33`, `#e8e1cf`);
     - Last Line: than chì `#14181f` và thép sáng `#8c96a3`;
   - **tương phản:** chênh luma trung bình giữa vật và nền ≥ 0,25 trên ít nhất một trong hai nền tối;
   - **dáng riêng:** ở 32 px, mặt nạ alpha của hai ảnh bất kỳ trong phiếu có IoU ≤ 0,80. Cặp sáng/tắt của cùng một vật thì ngược lại, IoU ≥ 0,95;
   - ghi bảng IoU lớn nhất từng ảnh.
5. **Tờ xem** `_review/<số>-sheet.jpg`:
   - hàng 1: bản gốc ở 256 px;
   - hàng 2: cỡ 1080p trên hai nền;
   - hàng 3: cỡ 720p trên hai nền;
   - hàng 4: cạnh 4 icon có sẵn của game đó và một mảnh của ảnh tham chiếu chủ dự án, cùng cao.
   - Dưới mỗi ảnh ghi tên.
6. **KA5 tự chấm:**
   - 5 tiêu chí của ART_ACCEPTANCE §2.2 (Đúng đề, Đọc được, Hợp bộ, Hình khối, Dùng tiếp), mỗi tiêu chí 0–2;
   - chấm ở cỡ gốc và cỡ 720p;
   - "Dùng tiếp" chỉ được 2 khi mọi kiểm số đo đạt.

**Báo cáo** `docs/codex-queue/<số>-report.md`, tiếng Việt:
- prompt đã sửa gì từng lượt;
- bảng số đo;
- điểm KA5;
- đường dẫn tờ xem;
- chỗ nào làm khác phiếu và vì sao.

Script đã dùng lưu ở `_review/<số>/`, chạy lại được.

**Xong khi:**
- đủ mọi ảnh và ba bản thu;
- mọi kiểm 1–5 đạt, có số;
- KA5 ≥ 8 cho mọi ảnh;
- có báo cáo.
- **Nhận** khi Claude chấm lại ≥ 8. Claude là người chép ảnh vào `public/` khi gắn.

## 2. Wordwoven

**Chung cho các phiếu Wordwoven:**
- **Phong cách:** style: to take the art director's new STYLE block (bible Wordwoven; khối STYLE-UI của phiếu 115: ngọc sẫm, đá vôi chạm, vàng lá, đồng Đông Sơn).
- **Định dạng theo** `games/typing-defense/docs/art-requests/td/03-2d-scenery-ui-vfx.md` §3 (khối ICON, PORTRAIT; nền G, M; cạnh dài ≥ 1024). Không chép câu "storybook" của §3.1.
- **Ảnh tham chiếu bắt buộc đính kèm:**
  - ảnh chọn của 115 khi có (`games/typing-defense/art-src/ui/frames/`), để icon hợp khung;
  - ảnh chủ đạo 113 khi có.
- Chưa có 115 thì phiếu chờ.
- **Thư mục `_review`:** `games/typing-defense/art-src/_review/<số>-*.jpg` và `_review/<số>/`.

## UIC-WW-1 · Wordwoven · Mười loại lời gọi (10 ảnh, P1)

**Vì sao:**
- Thẻ chữ, đầu thẻ gọi và bong bóng gọi hôm nay dùng emoji 🏹 🔨 🌾 🪓 ⛏️ 📖 🔥 ✋ ⚓ 🛡️ (`src/view/words/cards.ts:27,33`; `src/ui/td.css:159`).
- Dòng phần tử: WW-44, WW-46, WW-65.

**Chỉ được ghi:** `games/typing-defense/art-src/ui/calls/` (thư mục mới), `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN, cho prompt) | Cỡ trong game 720p / 1080p |
|---|---|---|
| `call-power` | a drawn bow with a glowing word-arrow on the string (tower power shot) | 18 / 24 trên thẻ; 20 / 24 ở đầu thẻ |
| `call-build` | a mason's hammer striking a carved limestone block | như trên |
| `call-harvest` | a sickle crossing a heavy golden rice sheaf | như trên |
| `call-chop` | an axe bitten into a round log | như trên |
| `call-mine` | a pickaxe over a glinting gold ore chunk | như trên |
| `call-quiz` | an unrolled scroll with a bronze question seal (no letters) | như trên |
| `call-spell` | a burning phoenix feather with flame trailing (Fire Feather Rain call) | như trên |
| `call-interrupt` | a raised palm stopping a war drum (Interrupt) | như trên |
| `call-anchor` | a bronze anchor with a short chain (Anchor) | như trên |
| `call-shield-break` | a cracked dome shield splitting apart (Shield Break) | như trên |

**Kiểm riêng:**
- Đọc được ở **18 px**. Đặt cả 10 ảnh trong một hàng ở 18 px trên đế thẻ chữ hôm nay. Chụp từ `games/typing-defense/tmp/ui-imagery/sheet-td-theme-1280.jpg`, ô thẻ "enough".
- Ghi tên đọc ra của từng ảnh.
- Hai ảnh không được cùng dáng tổng (IoU ≤ 0,80 ở 18 px).

**Xong khi:** như luật chung, và 10/10 ảnh đọc được ở 18 px.

## UIC-WW-2 · Wordwoven · Tem hạng và sao (8 ảnh, P1)

**Vì sao:**
- Tem hạng là chữ trong dấu tròn CSS (`cards.ts:24,93,118`; `td.css:183-187`).
- Sao là ký tự "★☆" (`title.ts:29`, `sheets.ts:94`).
- Dòng phần tử: WW-13, WW-50, WW-57.

**Chỉ được ghi:** `games/typing-defense/art-src/ui/grades/` (mới), `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `grade-flash` | a round bronze seal with a lightning bolt relief, bright gold rim | 36 / 44 |
| `grade-perfect` | a round gold-leaf seal with a radiant Dong Son sun-star | 36 / 44 |
| `grade-good` | a round jade seal with a single carved lotus | 36 / 44 |
| `grade-fair` | a round plain bronze seal with a simple ring motif | 36 / 44 |
| `grade-sloppy` | a round dull clay seal, chipped edge, smudged ink | 36 / 44 |
| `grade-redeemed` | a cracked round seal mended with a glowing gold seam | 36 / 44 |
| `star-lit` | a five-point star of gold leaf with warm inner glow | 16 / 20 ở màn tựa; 28 / 34 ở kết quả |
| `star-unlit` | the same star in dark bronze, no glow | như trên |

**Kiểm riêng:**
- Sáu tem cùng khung tròn, khác hình giữa. Bóng ngoài IoU ≥ 0,90; hình giữa phải phân biệt được ở 36 px.
- `star-lit` và `star-unlit` IoU ≥ 0,95.

## UIC-WW-3 · Wordwoven · HUD và hệ thống (12 ảnh, P1)

**Dòng phần tử:** WW-19, WW-20, WW-22–25, WW-28, WW-29, WW-36, WW-49.

**Chỉ được ghi:** `games/typing-defense/art-src/ui/icons/` (mới), `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `seeds` | a small cloth pouch spilling rice seeds | 20 / 24 |
| `day` | a sun disc rising over limestone peaks | 20 / 24 |
| `night` | a crescent moon with a single star over peaks | 20 / 24 |
| `night-call` | a bronze gong with a crescent moon emblem (call the night early) | 24 / 29 |
| `review-book` | a closed bound book with a jade ribbon marker (review book) | 16 / 20 |
| `chain` | three linked bronze rings glowing at the joints (typing chain) | 16 / 20 |
| `pause` | two upright carved limestone bars on a jade disc | 16 / 20 |
| `play` | a carved triangle pointing right on a jade disc | 16 / 20 |
| `sound-on` | a bronze bell ringing with sound arcs | 16 / 20 |
| `sound-off` | the same bell, silent, a slash of jade across it | 16 / 20 |
| `close` | a crossed pair of carved stone bars | 16 / 20 |
| `warning` | a triangular bronze plaque with a raised exclamation spike (no letters) | 16 / 20 |

**Kiểm riêng:**
- Cặp `pause` và `play` cùng đĩa nền: viền đĩa IoU ≥ 0,90.
- Cặp `sound-on` và `sound-off`: IoU ≥ 0,85.

## UIC-WW-4 · Wordwoven · Nút và thẻ nhà (10 ảnh, P1)

**Dòng phần tử:** WW-27, WW-34, WW-35, WW-39, WW-41, WW-43.

**Chỉ được ghi:** `games/typing-defense/art-src/ui/icons/`, `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `build` | a builder's hammer over a blueprint scroll | 24 / 29 |
| `hire-villager` | a villager's conical hat with a small plus-shaped jade token (no letters) | 24 / 29 |
| `ultimate` | a dragon feather igniting into a rain of fire (Fire Feather Rain) | 24 / 29 |
| `sell` | a stack of gold coins sliding out of an open palm | 16 / 20 |
| `upgrade` | a rising stone step with a gold chevron | 16 / 20 |
| `send` | a jade arrow flying from a hand | 16 / 20 |
| `undo` | a curling return arrow of bronze | 16 / 20 |
| `lock` | a bronze padlock with a jade keyhole | 16 / 20 |
| `level-pip-lit` | a small gold-leaf lozenge, glowing | 8 / 10 |
| `level-pip-unlit` | the same lozenge in dark bronze | 8 / 10 |

**Kiểm riêng:**
- Cặp pip IoU ≥ 0,95.
- Pip đọc được ở 8 px: sáng và tắt chênh luma ≥ 0,30.

## UIC-WW-5 · Wordwoven · Menu, âm lượng, hồ sơ (12 ảnh, menu P1, còn lại P2)

**Dòng phần tử:** WW-12, WW-14, WW-17, WW-55.

**Chỉ được ghi:** `games/typing-defense/art-src/ui/icons/`, `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `menu-start` | a village gate opening onto a path at dawn, small emblem scale | 24 / 36 |
| `menu-continue` | a bookmark ribbon on an open storybook | 24 / 36 |
| `menu-settings` | a bronze gear with jade inlay | 24 / 36 |
| `menu-learn` | an open book with a glowing word-lantern above it | 24 / 36 |
| `menu-profile` | a typist's brush and seal on a record card | 24 / 36 |
| `vol-master` | a large bronze gong | 20 / 24 |
| `vol-music` | a bamboo flute with two notes of light | 20 / 24 |
| `vol-effects` | a small hand drum struck by a stick | 20 / 24 |
| `stat-speed` | a running horse silhouette in gold relief | 20 / 24 |
| `stat-accuracy` | a jade target with an arrow in the centre | 20 / 24 |
| `stat-new-word` | a sprouting seedling growing out of a book | 20 / 24 |
| `stat-evenness` | a balanced bronze scale | 20 / 24 |

## UIC-WW-6 · Wordwoven · Chế độ và số kết quả (8 ảnh, P1 / P2)

**Dòng phần tử:** WW-15, WW-57, WW-58.

**Chỉ được ghi:** `games/typing-defense/art-src/ui/icons/`, `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `mode-relax` | a lotus floating on calm water | 20 / 24 |
| `mode-learn` | a scroll with a jade brush | 20 / 24 |
| `mode-balanced` | crossed sword and brush | 20 / 24 |
| `mode-challenge` | a flaming spear point | 20 / 24 |
| `stat-nights` | a moon over a fortified wall (nights held) | 20 / 24 |
| `stat-foes` | a broken enemy mask | 20 / 24 |
| `stat-words` | a fan of word cards | 20 / 24 |
| `record-ribbon` | a gold-leaf ribbon rosette (new record) | 32 / 40 |

## UIC-WW-7 · Wordwoven · Mảnh UI nhỏ (7 ảnh, P1)

**Vì sao:** thẻ chữ là "đèn lồng giấy" CSS (`td.css:151`). Đế tem, mặt phím, chấm và nhãn nhân vật đều là CSS. 115 chưa có các mảnh này.
- Nếu AD nhận `card-plate` và `stamp-seal` vào phiếu khung, bỏ hai ảnh đó khỏi đây.
- Dòng phần tử: WW-10, WW-28, WW-31, WW-45, WW-47, WW-50.

**Chỉ được ghi:** `games/typing-defense/art-src/ui/parts/` (mới), `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN) | Khổ gốc | Cỡ 720p / 1080p |
|---|---|---|---|
| `keycap` | a small carved limestone key cap, flat top, soft bevel | 1024² | 16 / 20 cao |
| `card-plate` | a word card plate: dark jade lacquer field, thin gold-leaf rim, small bronze end caps; plain stretchable middle | 1536 × 512 | cao 34 / 37, rộng theo chữ |
| `card-plate-review` | the same plate with a pale jade field for review words | 1536 × 512 | như trên |
| `stamp-seal` | an empty round bronze seal disc to sit behind grade icons | 1024² | 36 / 44 |
| `pip-lit` | a tiny round jade bead, glowing | 1024² | 8 / 10 |
| `pip-unlit` | the same bead, dark | 1024² | 8 / 10 |
| `agent-badge` | a tiny round bronze number disc, plain face | 1024² | 20 / 20 |

**Kiểm riêng:**
- `card-plate` và `card-plate-review` là 9-slice.
- Dựng thử bằng ImageMagick ở 3 cỡ: 120 × 34, 220 × 37, 360 × 37. Giữ góc, kéo giãn cạnh giữa.
- Trong dải giữa, độ lệch chuẩn luma theo chiều kéo ≤ 0,05.
- Ghi ô cắt 9-slice (trái, phải, trên, dưới, px).

## UIC-WW-8 · Wordwoven · Người làng, lính, ruộng, trạng thái (10 ảnh, P1)

**Dòng phần tử:** WW-39, WW-40, WW-41, WW-61, WW-63, WW-67.

**Chỉ được ghi:** `games/typing-defense/art-src/portraits/units/` (mới) cho 5 chân dung, `games/typing-defense/art-src/ui/icons/` cho 5 icon, `_review/<số>*`, báo cáo.

**Tham chiếu:**
- 5 chân dung đính kèm ảnh nguồn 3D `games/typing-defense/art-src/units/` và `workers/` (`worker-base` cùng bộ đầu, dụng cụ), để mặt và đồ khớp model.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `farmer` | bust portrait of a rice farmer with conical hat and sickle, three-quarter view, inside a circle | 24 / 29 (Low); 20 / 24 trong thẻ |
| `villager` | bust portrait of a villager with a carrying pole | như trên |
| `builder` | bust portrait of a builder with a hammer and headband | như trên |
| `miner` | bust portrait of a miner with a pickaxe and lamp | như trên |
| `soldier` | bust portrait of a village soldier with spear and round shield | như trên |
| `rice-ripe` | a single heavy golden rice plant, bowed | 20 / 24 |
| `rice-growing` | a young green rice plant | 20 / 24 |
| `rice-empty` | a wet empty paddy square with a seed hole | 20 / 24 |
| `status-burn` | a small ember flame | 16 / 20 |
| `status-stun` | three small stars circling | 16 / 20 |

**Kiểm riêng (chân dung):**
- Mặt nằm trong vòng tròn bán kính 0,45 cạnh ảnh.
- Ở 24 px vẫn thấy mắt và đồ nghề. Ghi có hay không từng ảnh.
- Đặt 5 chân dung cạnh `portraits/draconis.png` ở 54 px, để xem hợp bộ.

## UIC-WW-9 · Wordwoven · Chín chân dung quái (9 ảnh, P1)

**Dòng phần tử:** WW-63, WW-64. Sau này dùng cho thẻ ra mắt quái nếu điều phối mở.

**Chỉ được ghi:** `games/typing-defense/art-src/portraits/enemies/` (mới), `_review/<số>*`, báo cáo.

**Tham chiếu bắt buộc:** ảnh nguồn 3D cùng tên ở `games/typing-defense/art-src/enemies/`. Quái phải giống model trong game.

| Tên | Nguồn tham chiếu | Cỡ 720p / 1080p |
|---|---|---|
| `hopping-zombie` | `enemies/cuong-thi.png` | 24 / 29 (Low); 64 / 77 ở thẻ ra mắt |
| `zombie-leader` | `enemies/cuong-thi-lead-hat.png` + `cuong-thi.png` | như trên |
| `river-serpent` | `enemies/thuong-luong.png`, `-front` | như trên |
| `raccoon-dog` | `enemies/tanuki.png` | như trên |
| `split-blob` | `enemies/nuppeppo.png` | như trên |
| `little-blob` | `enemies/nuppeppo.png`, nhỏ và tròn hơn | như trên |
| `sapling` | `enemies/mam-go.png` | như trên |
| `troll` | `enemies/troll.png`, `-back` | như trên |
| `ghost-flame` | `vfx/ma-troi-wisp.png`, `ma-troi-sheet.png` (phiếu 099) | như trên |

**Kiểm riêng:**
- Ở 24 px, chín bóng khác nhau từng đôi (IoU ≤ 0,80).
- Màu chính khớp ảnh nguồn: hue trung vị lệch ≤ 15°.

## 3. Dragonhold

**Chung cho các phiếu Dragonhold:**
- **Phong cách:** style: to take the art director's new STYLE block (bible Dragonhold; khối STYLE-UI của phiếu 119: sử thi, ải núi, đá granite, lửa than hồng).
- **Định dạng theo** `docs/games/dragon-lane/art-requests/m0/05-icons.md`:
  - đọc được ở 32–64 px;
  - mỗi icon có dáng riêng, không chỉ khác màu (mù màu đỏ–lục, 05 §4.3);
  - nền M hay G.
- Không chép câu "storybook… misty pine forest".
- **Ảnh tham chiếu bắt buộc:**
  - `games/dragon-hold/art-src/ui/icons/skill-fire-breath.png` và `gold.png`, để xem cỡ vật trong ô;
  - ảnh chọn của 119 khi có.
- **Thư mục `_review`:** `games/dragon-hold/art-src/_review/<số>-*.jpg` và `_review/<số>/`.

## UIC-DH-1 · Dragonhold · HUD và trạng thái (10 ảnh, P1)

**Dòng phần tử:** DH-09–11, DH-18, DH-19, DH-24, DH-31, DH-34, DH-35, DH-54, DH-55.

**Chỉ được ghi:** `games/dragon-hold/art-src/ui/icons/<tên>*` (tên mới, không trùng file có sẵn), `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `wave-horn` | a curved war horn bound in iron (wave) | 16 / 24 |
| `chain` | a chain of three ember-lit links (typing chain) | 16 / 24 |
| `dragon-rage` | a dragon eye wreathed in flame (Dragon Rage) | 16 / 24 |
| `armour` | an overlapping dragon-scale armour plate | 12 / 18 |
| `shield` | a round rune shield of granite and bronze | 12 / 18 |
| `phase-prep` | a hammer resting on a stake bundle (set up traps) | 16 / 24 |
| `phase-fight` | two crossed blades over a flame | 16 / 24 |
| `phase-break` | a small campfire with a rising smoke curl (rest between waves) | 16 / 24 |
| `fast-forward` | two stacked ember chevrons pointing right | 16 / 24 |
| `danger` | a jagged red-orange warning sigil, hammered metal (enemy wind-up) | sprite 3D khoảng 24 / 36 |

**Kiểm riêng:**
- `armour` và `shield` đọc được ở **12 px**: phân biệt nhau, IoU ≤ 0,70.
- `danger` đọc được trên ảnh chụp cảnh trận `games/dragon-hold/tmp/map1-audit/sheets/sheet-08-feel-35wpm-1280-moments.jpg`: chênh luma ≥ 0,25 với cỏ.

## UIC-DH-2 · Dragonhold · Hệ thống và học (10 ảnh, P1)

**Dòng phần tử:** DH-03, DH-06, DH-12, DH-13, DH-26, DH-38, DH-44, DH-48, DH-51, DH-53, DH-59, DH-61, DH-67.

**Chỉ được ghi:** `games/dragon-hold/art-src/ui/icons/<tên>*`, `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `pause` | two upright granite bars on an iron disc | 16 / 24 |
| `camera-reset` | a dragon-eye lens with a curling return arrow | 16 / 24 |
| `keyboard` | a compact carved stone keyboard | 24 / 36 |
| `speaker` | a bronze horn speaker with sound arcs (listen) | 14 / 22 |
| `check` | an ember-gold check mark carved in stone | 14 / 22 |
| `new-word` | a sparkling ember star burst (new word) | 14 / 22 |
| `deny` | a crossed pair of iron bars over a red ember | 16 / 24 |
| `lock` | a heavy iron padlock with a dragon-scale face | 12 / 18 |
| `upgrade` | a rising granite step with an ember chevron | 16 / 24 |
| `sell` | gold coins tumbling from an open gauntlet | 16 / 24 |

**Kiểm riêng:** `speaker`, `check`, `new-word` đọc được ở **14 px**.

## UIC-DH-3 · Dragonhold · Bản đồ và thẻ chữ (11 ảnh, P1)

**Dòng phần tử:** DH-29, DH-31, DH-41, DH-43, DH-47, DH-49, DH-50.

**Chỉ được ghi:** `games/dragon-hold/art-src/ui/icons/<tên>*`, `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `lane-bridge` | an old stone arch bridge (Bridge Road) | 16 / 24 |
| `lane-stream` | a fast stream between rocks (Stream Road) | 16 / 24 |
| `lane-sky` | a spread bat-like wing (sky lane, flyers) | 16 / 24 |
| `slot-trap` | a square iron trap frame set in earth | 24 / 36 |
| `slot-house` | a round granite foundation pad | 24 / 36 |
| `slot-hold` | a planted war banner pole on a stone base (hold point) | 24 / 36 |
| `seal-lit` | a violet blight seal stone, glowing (Break Seal pip) | 10 / 14 |
| `seal-unlit` | the same seal stone, dark and cracked | 10 / 14 |
| `flag-pull` | a hand pulling a blight banner out of the ground | 18 / 22 |
| `swarm` | a cluster of three thorn ants (swarm tag) | 18 / 22 |
| `edge-arrow` | a short ember arrowhead (off-screen foe) | 10 / 14 |

**Kiểm riêng:**
- `slot-trap`, `slot-house`, `slot-hold` đọc được ở 24 px trên ảnh mặt đất của `sheet-04-words-crowd.jpg`.
- Cặp `seal-lit` và `seal-unlit` IoU ≥ 0,95.

## UIC-DH-4 · Dragonhold · Kết quả (10 ảnh, P1)

**Dòng phần tử:** DH-60, DH-65–68.

**Chỉ được ghi:** `games/dragon-hold/art-src/ui/icons/<tên>*`, `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `star-lit` | a five-point star of hammered gold with ember glow | 37 / 55 |
| `star-unlit` | the same star in dark iron | 37 / 55 |
| `stat-accuracy` | an arrow split in the centre of a target | 20 / 30 |
| `stat-new-words` | a glowing rune book opening | 20 / 30 |
| `stat-words-seen` | a stack of carved word tablets | 20 / 30 |
| `retry` | a circular ember arrow around a dragon scale | 16 / 24 |
| `easier` | a downward step with a soft feather | 16 / 24 |
| `status-learned` | a gold check seal | 14 / 20 |
| `status-review` | a bookmarked page with a small flame | 14 / 20 |
| `status-new` | an ember sprout | 14 / 20 |

## UIC-DH-5 · Dragonhold · Mảnh UI nhỏ (8 ảnh, P1)

**Vì sao:**
- Mặt phím, đế thẻ chữ, huy hiệu cấp và chấm cấp đều là CSS (`dh.css:138-151,361-374,1170-1243`; `tags.ts:495-501`).
- Dòng phần tử: DH-05, DH-16, DH-33, DH-40, DH-45, DH-46.
- Nếu AD mở phiếu khung Dragonhold và nhận các mảnh này, bỏ chúng khỏi đây.

**Chỉ được ghi:** `games/dragon-hold/art-src/ui/parts/` (mới), `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN) | Khổ gốc | Cỡ 720p / 1080p |
|---|---|---|---|
| `keycap` | a small carved granite key cap with iron rim, flat top | 1024² | 14 / 20 cao |
| `keycap-active` | the same, ember glow on the rim | 1024² | như trên |
| `tag-plate-enemy` | a dark slate word plate with a thin iron rim; plain stretchable middle | 1536 × 512 | cao 26 / 32 |
| `tag-plate-general` | the same with a double bronze rim and small horn studs | 1536 × 512 | như trên |
| `tag-plate-urgent` | the same with an ember-red rim | 1536 × 512 | như trên |
| `level-badge` | a small round iron badge with dragon-scale rim, empty face | 1024² | 16 / 24 |
| `pip-lit` | a tiny ember bead | 1024² | 6 / 9 |
| `pip-unlit` | the same bead, dark iron | 1024² | 6 / 9 |

**Kiểm riêng:**
- Ba `tag-plate-*` là 9-slice. Dựng thử ở 80 × 26, 160 × 26, 240 × 32. Dải giữa có độ lệch chuẩn luma ≤ 0,05.
- **Chữ trắng 20 px đặt trên đế phải đọc rõ:** tương phản WCAG ≥ 4,5 giữa chữ `#f5ecd8` và trung vị dải giữa.

## UIC-DH-6 · Dragonhold · Chân dung rồng và huy hiệu tốc độ (7 ảnh, P1)

**Dòng phần tử:** DH-05, DH-15, DH-17, DH-60.

**Chỉ được ghi:** `games/dragon-hold/art-src/ui/portraits/` (mới) cho 3 chân dung, `games/dragon-hold/art-src/ui/icons/` cho 4 huy hiệu, `_review/<số>*`, báo cáo.

**Tham chiếu bắt buộc:**
- Claude dựng trước 3 góc nhìn của `games/dragon-hold/public/assets/dragon-hold/models/heroes/draconis-v3/draconis-v3.high.glb` (Hỏa Long) và của GLB trong `guides/draconis-v4/` (Bạch Long), bằng `.local/bin/render-glb-views.py`, vào `games/dragon-hold/art-src/_refs/dragons/`.
- Màu Hỏa Long theo phiếu 119: vảy đỏ cam, bụng kem ấm, sừng và gai nâu sẫm. Bạch Long màu ngọc trai.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `hoa-long` | bust portrait of the red-orange fire dragon Hoa Long, three-quarter view, fierce and proud, ember light from below, inside a circle | 46 / 70 |
| `hoa-long-hurt` | the same pose, wounded: scales cracked, eye narrowed, smoke from the nostrils | 46 / 70 |
| `bach-long` | bust portrait of the pearl-white guide dragon Bach Long, calm, cool light | 19 / 29 |
| `pace-hatchling` | a dragon egg cracking open (beginner typing pace) | 20 / 30 |
| `pace-young` | a young dragon head, small horns | 20 / 30 |
| `pace-adult` | an adult dragon head, full horns | 20 / 30 |
| `pace-elder` | an elder dragon head crowned with flame | 20 / 30 |

**Kiểm riêng:**
- `hoa-long` và `hoa-long-hurt` cùng tư thế: IoU mặt nạ ≥ 0,90.
- Ở 46 px thấy mắt và sừng.
- `bach-long` ở 19 px vẫn khác `hoa-long` về màu và dáng.
- Bốn huy hiệu tăng dần rõ, xếp đúng thứ tự khi nhìn ở 20 px. Ghi có hay không.

## UIC-DH-7 · Dragonhold · Chân dung quái và vải cờ (8 ảnh, P1)

**Dòng phần tử:** DH-30, DH-52, DH-56.

**Trước phiếu này:**
- Claude thử cắt chân dung từ ảnh ý tưởng có sẵn bằng công cụ (`UI_IMAGERY.md` §8.3 bước 6).
- Ảnh nào cắt đạt ≥ 8 thì bỏ khỏi phiếu.

**Chỉ được ghi:** `games/dragon-hold/art-src/ui/portraits/` cho 7 chân dung, `games/dragon-hold/art-src/ui/banners/` (mới) cho vải cờ, `_review/<số>*`, báo cáo.

**Tham chiếu bắt buộc:** ảnh nguồn cùng tên ở `games/dragon-hold/art-src/enemies/` và `generals/moss-banner.png`. Quái phải giống model M0b.

| Tên | Nguồn | Cỡ 720p / 1080p |
|---|---|---|
| `moss-grunt` | `enemies/moss-grunt.png` | 22 / 34 ở chip đợt; 77 / 115 ở thẻ ra mắt |
| `moss-archer` | `enemies/moss-archer.png` | như trên |
| `blight-wolf` | `enemies/blight-wolf.png`, `-front` | như trên |
| `tusk-boar` | `enemies/tusk-boar.png`, `-front` | như trên |
| `thorn-wasp` | `enemies/thorn-wasp.png`, `-side` | như trên |
| `thorn-ant` | `enemies/thorn-ant.png`, `-front` | như trên |
| `moss-banner` | `generals/moss-banner.png` (Moss Bannerman) | như trên; thêm viền vương miện bằng mã |
| `banner-cloth` | vải cờ Bầy Héo: vải tro rách, ấn mắt tím, viền vàng úa; khổ 1024 × 1536, mép rách có alpha | texture cờ trên sân, khoảng 60 / 90 cao |

**Kiểm riêng:**
- Ở 22 px, 7 bóng khác nhau từng đôi (IoU ≤ 0,80). Quái bay (`thorn-wasp`) và bầy (`thorn-ant`) không lẫn nhau.
- `banner-cloth` đọc được trên `sheet-12-heo-lan-hp-loss-1280.jpg` ở 60 px: ấn mắt thấy rõ.

## 4. Last Line

**Chung cho các phiếu Last Line:**
- **Chờ chủ dự án chọn hướng ở phiếu 112:** A Iron Warden, B Lightbearer hay C Rampart.
- **Phong cách:** style: to take the art director's new STYLE block (bible Last Line, khối STYLE-UI của phiếu 121 theo hướng đã chọn).
- **Định dạng theo** `games/typing-survival/docs/art-requests/015-s1-s2.md`:
  - hình khối gọn, đọc được ở 32–64 px;
  - nền trong suốt, lề 15 % như 108.
- Không chép câu "industrial pictogram… gunmetal" nếu hướng mới khác.
- **Ảnh tham chiếu bắt buộc:**
  - `games/typing-survival/art-src/ui/icons/gun-xung.norm.256.png` (cỡ vật);
  - ảnh chọn của 121 khi có.
- **Thư mục `_review`:** `games/typing-survival/art-src/_review/<số>-*.jpg` và `_review/<số>/`.
- `--ui` của Last Line là 1 ở 720p và 1,5 ở 1080p.

## UIC-LL-1 · Last Line · HUD trận (10 ảnh, P1)

**Dòng phần tử:** LL-17, LL-30, LL-31, LL-33, LL-34, LL-37, LL-41, LL-43, LL-44.

**Chỉ được ghi:** `games/typing-survival/art-src/ui/icons/<tên>*` (tên mới; không trùng `gun-*`, `nova*`), `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `armour` | a segmented hull armour plate | 20 / 30 |
| `clock` | a countdown dial with a sweeping hand | 20 / 30 |
| `kills` | a black-glass foe shard shattering | 20 / 30 |
| `surge` | a rising wave of black shards under an alarm chevron (horde surge) | 28 / 42 |
| `repair-pod` | a supply repair pod with a glowing wrench emblem | 28 / 42 |
| `keyboard` | a compact armoured keyboard | 16 / 24 |
| `check` | a check mark etched on a small plate | 16 / 24 |
| `bay-full` | a gun bay with a full glowing magazine | 16 / 24 |
| `streak` | three linked clean sparks (clean streak) | 16 / 24 |
| `lock` | a heavy padlock on a bay door | 24 / 36 |

**Kiểm riêng:** đặt cả 10 ảnh lên tấm bến của `games/typing-survival/tmp/map1-audit/sheets/sheet-c1s1-fight-1280x720.jpg`. Tương phản ≥ 0,25 với `--bay-glass`.

## UIC-LL-2 · Last Line · Thẻ ải và nạp súng (11 ảnh, P1)

**Dòng phần tử:** LL-02, LL-05, LL-16, LL-19, LL-20, LL-22, LL-26–28, LL-32.

**Chỉ được ghi:**
- `games/typing-survival/art-src/ui/icons/<tên>*`;
- `games/typing-survival/art-src/ui/foes/shard*` (không ghi đè 6 chân dung có sẵn);
- `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `objective` | a target reticle around a planted flag | 20 / 30 |
| `hazard` | a cracked hexagonal hazard plate | 20 / 30 |
| `learning-rule` | an open data book with a bolt of light | 20 / 30 |
| `equipment` | two guns crossed on a rack | 20 / 30 |
| `warning` | a warning triangle with a raised spike (no letters) | 16 / 24 |
| `new-badge` | a starburst ribbon badge, plain face (new) | 16 / 24 |
| `station-crest` | the station emblem: a ring and spire at the edge of a black hole | 20 / 30 |
| `chapter-crest` | the chapter 1 corridor emblem: a long causeway between two pylons | 32 / 48 |
| `load-guns` | a magazine sliding into a gun | 20 / 30 |
| `back` | a return arrow on a plate | 20 / 30 |
| `shard` | foe portrait: Shard, a small fragment of the horde (black glass, glowing cracks), same framing as `ui/foes/swarm.png` | 20 / 30 trong thẻ; 40 / 60 ở thẻ ải |

**Kiểm riêng:** đặt `shard` cạnh 6 chân dung có sẵn ở 40 px. Cùng khung, cùng ánh sáng. Ghi hợp bộ hay không.

## UIC-LL-3 · Last Line · Menu và kết quả (12 ảnh, P1)

**Dòng phần tử:** LL-09, LL-48, LL-50, LL-51, LL-53.

**Chỉ được ghi:** `games/typing-survival/art-src/ui/icons/<tên>*`, `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `menu-play` | a forward chevron lit from within | 24 / 36 |
| `menu-journey` | a route map with three waypoints | 24 / 36 |
| `menu-mode` | a three-position dial | 24 / 36 |
| `menu-armory` | a gun rack with two guns | 24 / 36 |
| `menu-settings` | a gear with a cooling fin | 24 / 36 |
| `menu-profile` | a typist ID card with a hand print | 24 / 36 |
| `star-lit` | a five-point star with a bright core | 28 / 42 |
| `star-unlit` | the same star, dark | 28 / 42 |
| `retry` | a circular arrow around a shard | 20 / 30 |
| `next-stage` | a double forward chevron over a door | 20 / 30 |
| `stat-time` | an hourglass in a metal frame | 24 / 36 |
| `stat-accuracy` | a crosshair with a hit in the centre | 24 / 36 |

## UIC-LL-4 · Last Line · Cài đặt, hồ sơ, Rift (11 ảnh, P2)

**Dòng phần tử:** LL-13, LL-14, LL-36, LL-44, LL-51.

**Chỉ được ghi:** `games/typing-survival/art-src/ui/icons/<tên>*`, `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `sfx` | a speaker grille with a spark | 20 / 30 |
| `music` | a waveform over a speaker | 20 / 30 |
| `shake` | a screen frame with motion ticks | 20 / 30 |
| `reduced-motion` | the same frame, calm, a small anchor | 20 / 30 |
| `read-aloud` | a mouth grille with sound arcs | 20 / 30 |
| `pace-director` | a dial with a hand that follows a curve | 20 / 30 |
| `quality` | a lens with three facets | 20 / 30 |
| `stat-wpm` | a speed gauge needle high | 24 / 36 |
| `stat-new-word` | a new data chip lighting up | 24 / 36 |
| `stat-evenness` | a level bar with a centred bubble | 24 / 36 |
| `rift` | a jagged violet tear in space | 24 / 36 |

## UIC-LL-5 · Last Line · Mảnh UI nhỏ (7 ảnh, P1)

**Vì sao:** đèn LED, ô đạn, mũi tên chọn giá trị và mặt phím đều là CSS hay ký tự (`survival.css:93-98,174,195,198`; `screens.ts:44`).
- Dòng phần tử: LL-09, LL-11, LL-40.

**Chỉ được ghi:** `games/typing-survival/art-src/ui/parts/` (mới), `_review/<số>*`, báo cáo.

| Tên | Nội dung (EN) | Khổ gốc | Cỡ 720p / 1080p |
|---|---|---|---|
| `keycap` | a small armoured key cap, flat top | 1024² | 16 / 24 cao |
| `keycap-active` | the same, lit rim | 1024² | như trên |
| `led-on` | a small round indicator lamp, lit | 1024² | 8 / 12 |
| `led-off` | the same lamp, off | 1024² | 8 / 12 |
| `mag-empty` | an empty magazine cell | 1024² | 10 / 15 |
| `mag-full` | the same cell, full and glowing | 1024² | 10 / 15 |
| `arrow` | a short chevron pointing right (left is mirrored in code) | 1024² | 12 / 18 |

**Kiểm riêng:**
- Các cặp sáng/tắt IoU ≥ 0,95.
- `mag-full` và `mag-empty` chênh luma ≥ 0,30 ở 10 px.

## 5. Phiếu vẽ lại có điều kiện

**Điều kiện chạy:** chỉ chạy khi AD chấm bộ icon có sẵn dưới 8 theo mức chợ. Kết quả chấm ghi ở `docs/games/ART_DIRECTION_2026-10-28.md` hay `ART_REPLACE_LATER.md`.

**Cách làm:**
- Giữ nguyên tên file cũ: bản mới ghi cạnh bản cũ thành `<tên>.v2.png`. Claude đổi sang khi gắn, không ghi đè.
- Mỗi phiếu đính kèm ảnh cũ làm tham chiếu vật (giữ đồ vật, đổi phong cách).

| Phiếu | Game | Ảnh | Chỉ được ghi |
|---|---|---|---|
| UIC-DH-R1 | Dragonhold | `spikes`, `pine-bomb`, `net-launcher`, `moss-warden`, `herb-hut`, `potion-small`, `dragon-heart`, `hard-scale`, `gold`, `call-wave`, `enemy-general` (11) | `games/dragon-hold/art-src/ui/icons/<tên>.v2*` |
| UIC-DH-R2 | Dragonhold | `skill-fire-breath`, `skill-sky-fire`, `skill-roar`, `skill-ultimate`, `family-moss`, `family-beast`, `family-bug`, `aura-speed`, `aura-attack`, `hard-scale.warm` (10) | như trên |
| UIC-WW-R1 | Wordwoven | `buildings/keep`, `archer`, `cannon`, `barracks`, `gold-mine`, `farm`; `lanterns/lantern-unlit`, `lantern-lit` (8) | `games/typing-defense/art-src/ui/<thư mục>/<tên>.v2*` |
| UIC-WW-R2 | Wordwoven | `resources/gold`, `wood`, `food`, `lives`, `knowledge`, `wave`; `lanterns/lantern-blazing` (7) | như trên |
| UIC-WW-R3 | Wordwoven | `portraits/draconis`, `helper-cham-happy`, `helper-cham-scared`, `helper-phay-happy`, `helper-phay-scared`, `helper-gach-happy`, `helper-gach-scared`, `narrator`, `moc-tinh` (9) | `games/typing-defense/art-src/portraits/<tên>.v2*` |
| UIC-LL-R | Last Line | `gun-xung`, `gun-tia`, `gun-tan`, `gun-ray`, `gun-phao-sao`; `foes/swarm`, `scout`, `brute`, `pack-leader`, `shield-guard`, `splitter` (11) | `games/typing-survival/art-src/ui/icons/<tên>.v2*`, `ui/foes/<tên>.v2*` |

- **Kiểm:** như luật chung, cộng một tờ so cũ–mới cùng cỡ 64 px.
- **Xong khi:** như luật chung.
- UIC-LL-R chạy sau khi chủ dự án chọn hướng 112, nếu hướng đó bỏ tàu hay đổi kiểu súng.
