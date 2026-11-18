# Phiếu 113 · Wordwoven · Màn tựa sử thi, ảnh chủ đạo, logo "Wordwoven" (5 ảnh)

**Nguồn:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md`, bible Wordwoven; thứ tự 1). Chủ dự án 28/10 tối chê màn tựa Wordwoven "như thôn quê"; muốn "đẹp và hùng vĩ". `title-dusk.png` (chấm 5/10 theo mức chợ) được thay. Game nay tên **Wordwoven** (trước là Lời Gọi): mọi chữ trong ảnh là tiếng Anh.

**Báo cáo:** `docs/codex-queue/113-report.md`.

**Thứ tự:** sau 112, trước 114.

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận mới:** ảnh được chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp`. Lấy mức chi tiết, ánh sáng, chiều sâu và cảm giác quy mô; không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ (tách nền, cắt, đổi khổ, chỉnh màu) thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/113/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn (kể cả `ui/title-dusk.png`); xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, chữ ký, khung, viền trong ảnh, trừ chữ logo "Wordwoven" của ảnh `logo`. Mọi chữ hiện trong ảnh là tiếng Anh.
- **KA1 md5:** `md5 -r` mọi file trong `games/typing-defense/art-src/ui/` (đệ quy) trước khi ghi (`_review/113/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, mức chợ, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: có mốc lớn làm người chơi nhỏ lại, ít nhất ba lớp sâu (gần, giữa, xa) và trời, ánh sáng có hướng, màu theo kịch bản, chi tiết hoàn thiện. 7 là game indie dễ chịu, nhưng quy mô và ánh sáng thường. 6 là gọn mà chung chung, ánh sáng phẳng. 5 là tranh đẹp nhưng sai tầm (ấm cúng, quê, nhỏ). 4 là hình phẳng kiểu clip-art. Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2, mỗi tiêu chí 0–2.
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**. Logo và huy hiệu chấm M theo logo của game thương mại.
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8.

## Phiếu

**Nơi ghi:** `games/typing-defense/art-src/ui/title-epic/` (thư mục mới).

**Chỉ được ghi:**
- `ui/title-epic/<tên>.tryN.png`, `.tryN.prompt.txt`, bản chọn `<tên>.png`, `<tên>.prompt.txt`, `<tên>.alpha.png`, `<tên>.512.png`;
- `games/typing-defense/art-src/_review/113-*.jpg`, `games/typing-defense/art-src/_review/113/`;
- `docs/codex-queue/113-report.md`.

**Đọc trước (chỉ đọc):**
- ảnh tham chiếu (ở trên);
- màn tựa cũ `games/typing-defense/art-src/ui/title-dusk.png` (để thấy cái cần bỏ: nhà tranh, làng quê, quy mô nhỏ);
- dáng chuẩn của model 3D: Draconis `games/typing-defense/art-src/heroes/draconis.png`; Fort `buildings/keep.png` và `kits/keep-kit-l3.png`; Mộc Tinh (Tree Spirit) `bosses/moc-tinh.png`. Model giữ nguyên, nên ảnh phải khớp màu và dáng của chúng.

### Khối prompt (nguyên văn)

**STYLE** (mở đầu prompt của `title-backdrop`, `keyart`, `poster`)
```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.
```

**STYLE-UI** (mở đầu prompt của `logo` và `emblem`; ở `logo`, câu cuối "No text, ..." được thay bằng khối LOGO)
```text
Premium high-fantasy game interface art for Wordwoven, a majestic realm inspired by northern Vietnam: carved pale limestone and polished dark jade lacquer, gold-leaf trim and fine bronze inlay, ornament drawn from Dong Son bronze-drum sun-star rings and cloud-scroll patterns, small cinnabar-red and lantern-amber accents. Crisp, finished and richly detailed like the interface of a top commercial fantasy game, with clean bevels, soft inner shadow and a subtle warm rim light, readable at small size. Shown flat and straight on, no perspective, no scenery. No text, letters, numbers, signature or watermark.
```

**REF** (dán khi đính kèm ảnh nhân vật hay công trình): `The attached image is the official look of this character or building. Keep its colours, markings, materials and proportions; only the pose, view, light and scale may change.`

### Năm ảnh

| Tên | Khổ | Nền | Nội dung (phần riêng của prompt, dán sau STYLE) |
|---|---|---|---|
| `title-backdrop` | 1536 × 1024 | đặc | Xem khối TITLE dưới |
| `keyart` | 1536 × 1024 | đặc | Xem khối KEYART; đính kèm `draconis.png`, `moc-tinh.png`, `keep-kit-l3.png` với dòng REF |
| `poster` | 1024 × 1536 | đặc | Cùng khoảnh khắc với `keyart`, dựng lại theo khổ dọc cho thẻ game ở cổng game và ảnh giới thiệu; đính kèm `keyart` đã chọn với dòng `Use the attached image only to keep the same characters, place, light and colours. Recompose it as a tall poster as described.` Chỗ trống trên cùng cho logo |
| `logo` | ảnh rộng ~3 : 1 | `#FF00FF` | Xem khối LOGO |
| `emblem` | 1024 × 1024 | `#FF00FF` | Xem khối EMBLEM |

**TITLE**
```text
Scene: a vast karst bay at golden hour, seen from a high carved-stone terrace. Foreground left: a carved limestone balustrade with two hanging lanterns. Midground: the Fort, an ancient white-stone temple-fortress with tiered red-tile roofs and a tall pagoda tower, stands on a karst plateau above rice terraces that climb toward it like giant stairs, and a silver waterfall falls from the plateau into mist. Far: dozens of colossal karst towers in many layers of mist over a winding jade river. Sky: towering golden clouds with god rays; a colossal sky turtle carrying moss-covered temple ruins and small trees on its shell glides between two far towers; hundreds of small amber lanterns rise from the valley; a white-gold dragon flies small but clear across the light. The upper middle third is calm open sky for the logo. The lower left third is calmer and a little darker for the menu.
```

**KEYART**
```text
Scene: the key moment of the game. In the foreground right a white-gold dragon with gold-and-black markings and orange-tipped wings dives toward the viewer, breathing a stream of fire. Below, on a karst plateau, the Fort's towers fire glowing arrows, and threads of golden light weave between the towers like stitching, abstract, never readable letters. Across the jade river a colossal ancient tree giant, the Tree Spirit, rises out of the forest, taller than the lower cliffs of the karst towers, its roots tearing the ground, lanterns scattering around it. Karst towers and a silver waterfall behind, storm light breaking through clouds, god rays. One clear focal point on the dragon and the tree giant. A calm area in the upper left for the logo.
```

**LOGO** (thay câu cuối của STYLE-UI)
```text
Game logo lettering that reads exactly Wordwoven: one word, nine letters W-o-r-d-w-o-v-e-n, a capital W and lower-case o-r-d-w-o-v-e-n, on one line. The letters are carved from pale jade with a polished gold-leaf rim and a thin dark-bronze outline; one glowing golden thread weaves over and under the letters like stitching; a small brush-stroke swash sits under the word. Epic, premium, crisp and easy to read, like the logo of a top commercial fantasy game. Centred, nothing else in the image. Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the logo contains no pink, magenta or bright purple at all.
```

**EMBLEM** (dán sau STYLE-UI)
```text
A round bronze-and-jade seal emblem: a Dong Son sun-star with sixteen rays at the centre, a ring of flying cranes and cloud scrolls around it, a thin coiled white-gold dragon wrapping the rim, gold-leaf edges. Whole emblem centred with an empty margin on every side. Reads clearly at 64 pixels. Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the emblem contains no pink, magenta or bright purple at all.
```

**Hậu kỳ (`logo`, `emblem`):** tách nền bằng `tools/art-normalize/key-alpha.sh` (đọc README). Ra `<tên>.alpha.png` (cạnh dài bằng nguồn, không phóng to) và `<tên>.512.png` (cạnh dài 512 px). Ba ảnh nền đặc không cần alpha.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/typing-defense/art-src/ui/` (đệ quy).
2. **Khổ:** `title-backdrop`, `keyart` 1536 × 1024; `poster` 1024 × 1536; `emblem` 1024 × 1024; `logo` cạnh dài ≥ 1536 ở nguồn. Khổ khác thì cắt giữa rồi thu bằng Lanczos, không phóng to; ghi lệnh.
3. **Chính tả logo:** cắt phóng 4× từng chữ cái, đặt cạnh cùng từ "Wordwoven" in bằng một font hệ thống (ghi tên font). Đúng 9 chữ cái W-o-r-d-w-o-v-e-n, không thiếu, không thừa, không chữ lạ. Sai một chữ là loại lượt đó.
4. **Không chữ lạc:** ba ảnh nền đặc và `emblem` không có chữ, số nào. Sợi chỉ vàng trong `keyart` không thành chữ đọc được.
5. **Alpha sạch** (`logo`, `emblem`): min 0, max 255; 0 % px có alpha > 0 mà hue 285–330° và S > 0,5; không viền hồng ở phóng 4× (`_review/113-edge.jpg`); đốm rời nhỏ hơn 20 px: 0; bbox cách mép ≥ 24 px.
6. **Chỗ cho logo và menu** (`title-backdrop`, trên bản cắt 16 : 9 ở giữa, 1536 × 864): vùng logo x 25–75 %, y 6–30 % có độ lệch chuẩn luma ≤ 0,12; vùng menu x 3–35 %, y 55–92 % có độ lệch chuẩn luma ≤ 0,14. Ghi số. Dựng `_review/113-title-mock.jpg`: bản cắt 16 : 9, `logo.alpha.png` rộng 45 % ở giữa trên, một khối xám 30 % × 35 % ở góc dưới trái cho menu. Xem: logo đọc rõ, cảnh vẫn hùng vĩ.
7. **Khớp model:** cắt Draconis và Tree Spirit trong `keyart`, đặt cạnh `draconis.png`, `moc-tinh.png` (`_review/113-models.jpg`). Draconis: thân trắng vàng, vằn vàng đen, đầu cánh cam. Ghi "khớp" hay chỗ lệch.
8. **Đọc ở cỡ nhỏ:** `keyart`, `poster` thu về 384 px cạnh dài; `emblem` ở 64 px. Ghi: nhận ra rồng, cây khổng lồ, tháp đá không; nhận ra huy hiệu không.
9. **Tờ so với tham chiếu** `_review/113-vs-ref.jpg`: `title-mock`, `keyart`, `poster` và ảnh tham chiếu, cùng cao 640 px; hàng dưới là `title-dusk.png` cũ cho thấy trước và sau. Dưới mỗi ảnh mới ghi một dòng: "đứng cạnh được" hay "chưa", và vì sao.
10. **KA5 mức chợ:** M và Q cho từng bản chọn, ở cỡ đầy đủ và ở 384 px (logo ở 512 px).

**Xong khi:** năm ảnh có bản chọn, qua mục 2–8, và mỗi ảnh tự chấm M ≥ 8, Q ≥ 8. Logo sau 3 lượt vẫn sai chính tả thì ghi "không đạt, dùng font" kèm lượt tốt nhất; Claude dựng chữ bằng font của game. Ảnh khác không đạt sau 3 lượt thì giữ bản tốt nhất, ghi rõ chỗ thiếu.
