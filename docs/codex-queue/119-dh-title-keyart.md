# Phiếu 119 · Dragonhold · Màn tựa sử thi, ảnh chủ đạo, logo "Dragonhold" (5 ảnh)

**Nguồn:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md`, bible Dragonhold; thứ tự 5). Game nay tên **Dragonhold** (trước là Rồng Giữ Ải), nên chữ logo "Rồng Giữ Ải" của phiếu 096 thôi dùng. Huy hiệu 096 (rồng nhỏ đậu trên vòm đá) chấm 5,5/10 theo mức chợ: dễ thương, nhỏ, không có ải. Mọi chữ trong ảnh là tiếng Anh.

**Báo cáo:** `docs/codex-queue/119-report.md`.

**Thứ tự:** sau 118 (sau các phiếu Wordwoven 113–118).

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận mới:** ảnh được chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp`. Lấy mức chi tiết, ánh sáng, chiều sâu và cảm giác quy mô; không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ (tách nền, cắt, đổi khổ, chỉnh màu) thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/119/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn (kể cả `ui/title/*` của phiếu 096); xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, chữ ký, khung, viền trong ảnh, trừ chữ logo "Dragonhold" của ảnh `logo`. Mọi chữ hiện trong ảnh là tiếng Anh.
- **KA1 md5:** `md5 -r` mọi file trong `games/dragon-hold/art-src/ui/` (đệ quy) trước khi ghi (`_review/119/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, mức chợ, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: có mốc lớn làm người chơi nhỏ lại, ít nhất ba lớp sâu (gần, giữa, xa) và trời, ánh sáng có hướng, màu theo kịch bản, chi tiết hoàn thiện. 7 là game indie dễ chịu, nhưng quy mô và ánh sáng thường. 6 là gọn mà chung chung, ánh sáng phẳng. 5 là tranh đẹp nhưng sai tầm (ấm cúng, nhỏ, dễ thương). 4 là hình phẳng kiểu clip-art. Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2, mỗi tiêu chí 0–2.
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**. Logo và huy hiệu chấm M theo logo của game thương mại.
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8.

## Phiếu

**Nơi ghi:** `games/dragon-hold/art-src/ui/title-epic/` (thư mục mới).

**Chỉ được ghi:**
- `ui/title-epic/<tên>.tryN.png`, `.tryN.prompt.txt`, bản chọn `<tên>.png`, `<tên>.prompt.txt`, `<tên>.alpha.png`, `<tên>.512.png`;
- `games/dragon-hold/art-src/_review/119-*.jpg`, `games/dragon-hold/art-src/_review/119/`;
- `docs/codex-queue/119-report.md`.

**Đọc trước (chỉ đọc):**
- ảnh tham chiếu (ở trên);
- màu Hỏa Long: `games/dragon-hold/art-src/ui/title/title-emblem.png` (vảy đỏ cam, bụng kem ấm, sừng và gai nâu sẫm) và các icon `ui/icons/skill-fire-breath.png`, `skill-sky-fire.png`, `dragon-heart.png`;
- dáng quái: `games/dragon-hold/art-src/enemies/moss-grunt.png`, `blight-wolf.png`, `moss-archer.png`, `generals/moss-banner.png` (lính rêu, sói héo, cờ rêu; vải tím xám, gân vàng xanh);
- cảnh map hôm nay: `games/.wt-dh-mappilot/tmp/map-pilot-a2/sheets/a2-1920x1080-default-compare.jpg` (sông, cầu gỗ, rừng thông, vách đá).

### Khối prompt (nguyên văn)

**STYLE** (mở đầu prompt của `title-backdrop`, `keyart`, `poster`)
```text
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
```

**STYLE-UI** (mở đầu prompt của `logo` và `emblem`; ở `logo`, câu cuối "No text, ..." được thay bằng khối LOGO)
```text
Premium high-fantasy game interface art for Dragonhold, a mountain pass guarded by a fire dragon: weathered cream granite and dark forged iron, hammered gold trim, ember-orange enamel and glowing dragon-fire accents, carved dragon-scale and pine-bough ornament, small muted-violet accents. Crisp, finished and richly detailed like the interface of a top commercial fantasy strategy game, with clean bevels, soft inner shadow and a subtle warm rim light, readable at small size. Shown flat and straight on, no perspective, no scenery. No text, letters, numbers, signature or watermark.
```

**REF** (khi đính kèm `title-emblem.png` cho màu rồng): `Use the attached image only for the dragon's colours and markings: red-orange scales, warm cream belly, dark brown horns and spines. Paint a grand, fierce, adult dragon, not a cute one.`

### Năm ảnh

| Tên | Khổ | Nền | Nội dung |
|---|---|---|---|
| `title-backdrop` | 1536 × 1024 | đặc | STYLE + khối TITLE |
| `keyart` | 1536 × 1024 | đặc | STYLE + khối KEYART; đính kèm `title-emblem.png` với dòng REF, và `moss-grunt.png`, `blight-wolf.png` với dòng `Use the attached images only for the foes' shapes and colours.` |
| `poster` | 1024 × 1536 | đặc | STYLE + cùng khoảnh khắc với `keyart`, dựng lại theo khổ dọc; đính kèm `keyart` đã chọn với dòng `Use the attached image only to keep the same characters, place, light and colours. Recompose it as a tall poster as described.` Chỗ trống trên cùng cho logo |
| `logo` | ảnh rộng ~3 : 1 | `#FF00FF` | STYLE-UI (thay câu cuối) + khối LOGO |
| `emblem` | 1024 × 1024 | `#FF00FF` | STYLE-UI + khối EMBLEM |

**TITLE**
```text
Scene: the pass at dawn, seen from high on the rampart of the fortress. Foreground: the worn granite battlement with an iron brazier burning, a dragon-head carving on the merlon. Midground: the fortress gate spans the pass between two colossal cliffs carved with giant dragon statues; below it the river runs fast under an old stone bridge through a deep green valley of pines, mist pooling between the trees. Far: snow-capped peaks catching the first gold light, ridge after ridge fading into blue haze. Sky: a great dawn sky with long gold-lit clouds and god rays; a red-orange fire dragon flies along the cliffs, large enough to read but not filling the frame. The upper middle third is calm open sky for the logo; the lower left third is calmer and a little darker for the menu.
```

**KEYART**
```text
Scene: the key moment of the game. A huge red-orange fire dragon with a warm cream belly and dark horns stands on top of the fortress gate, wings half open, breathing a roaring stream of fire down onto the stone bridge. On the bridge and the valley road a horde of moss creatures and blight wolves with violet rags and glowing yellow-green eyes charges out of the dark pine forest toward the gate; fire, embers and smoke light the scene. Colossal cliffs with carved dragon statues on both sides, snow peaks behind, dawn light from the side, long shadows across the valley. One clear focal point on the dragon. A calm area in the upper left for the logo.
```

**LOGO** (thay câu cuối của STYLE-UI)
```text
Game logo lettering that reads exactly Dragonhold: one word, ten letters D-r-a-g-o-n-h-o-l-d, a capital D and lower-case r-a-g-o-n-h-o-l-d, on one line. The letters are forged dark iron with a hammered gold rim, their cracks glowing with ember-orange dragon fire; a small dragon wing curls from the top of the D and a thin fire swash runs under the word. Epic, premium, crisp and easy to read, like the logo of a top commercial fantasy strategy game. Centred, nothing else in the image. Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the logo contains no pink, magenta or bright purple at all.
```

**EMBLEM** (dán sau STYLE-UI)
```text
A heraldic shield emblem: a fortress gate between two mountain peaks in cream granite, a red-orange fire dragon coiled over the gate with spread wings, a ring of hammered gold and dark iron around it, small ember glow in the dragon's mouth. Whole emblem centred with an empty margin on every side. Reads clearly at 64 pixels. Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the emblem contains no pink, magenta or bright purple at all.
```

**Hậu kỳ (`logo`, `emblem`):** tách nền bằng `tools/art-normalize/key-alpha.sh` (đọc README). Ra `<tên>.alpha.png` (cạnh dài bằng nguồn, không phóng to) và `<tên>.512.png` (cạnh dài 512 px). Ba ảnh nền đặc không cần alpha.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/dragon-hold/art-src/ui/` (đệ quy).
2. **Khổ:** `title-backdrop`, `keyart` 1536 × 1024; `poster` 1024 × 1536; `emblem` 1024 × 1024; `logo` cạnh dài ≥ 1536 ở nguồn. Khổ khác thì cắt giữa rồi thu bằng Lanczos, không phóng to; ghi lệnh.
3. **Chính tả logo:** cắt phóng 4× từng chữ cái, đặt cạnh cùng từ "Dragonhold" in bằng một font hệ thống (ghi tên font). Đúng 10 chữ cái D-r-a-g-o-n-h-o-l-d, không thiếu, không thừa, không chữ lạ. Sai một chữ là loại lượt đó.
4. **Không chữ lạc:** ba ảnh nền đặc và `emblem` không có chữ, số nào.
5. **Alpha sạch** (`logo`, `emblem`): min 0, max 255; 0 % px có alpha > 0 mà hue 285–330° và S > 0,5; không viền hồng ở phóng 4× (`_review/119-edge.jpg`); đốm rời nhỏ hơn 20 px: 0; bbox cách mép ≥ 24 px.
6. **Chỗ cho logo và menu** (`title-backdrop`, trên bản cắt 16 : 9 ở giữa, 1536 × 864): vùng logo x 25–75 %, y 6–30 % có độ lệch chuẩn luma ≤ 0,12; vùng menu x 3–35 %, y 55–92 % có độ lệch chuẩn luma ≤ 0,14. Ghi số. Dựng `_review/119-title-mock.jpg`: bản cắt 16 : 9, `logo.alpha.png` rộng 45 % ở giữa trên, một khối xám 30 % × 35 % ở góc dưới trái cho menu.
7. **Đúng game:** rồng đỏ cam, bụng kem, sừng sẫm (so với `title-emblem.png`); quái là lính rêu và sói héo, không phải quái khác. Cắt đặt cạnh nhau ở `_review/119-models.jpg`; ghi "khớp" hay chỗ lệch.
8. **Đọc ở cỡ nhỏ:** `keyart`, `poster` thu về 384 px cạnh dài; `emblem` ở 64 px. Ghi: nhận ra rồng, cổng ải, bầy quái, vách đá không; nhận ra huy hiệu không.
9. **Tờ so với tham chiếu** `_review/119-vs-ref.jpg`: `title-mock`, `keyart`, `poster` và ảnh tham chiếu, cùng cao 640 px; hàng dưới là `ui/title/title-emblem.png` và `backdrops/pine-river-far.png` cũ cho thấy trước và sau. Dưới mỗi ảnh mới ghi một dòng: "đứng cạnh được" hay "chưa", và vì sao.
10. **KA5 mức chợ:** M và Q cho từng bản chọn, ở cỡ đầy đủ và ở 384 px (logo ở 512 px).

**Xong khi:** năm ảnh có bản chọn, qua mục 2–8, và mỗi ảnh tự chấm M ≥ 8, Q ≥ 8. Logo sau 3 lượt vẫn sai chính tả thì ghi "không đạt, dùng font" kèm lượt tốt nhất; Claude dựng chữ bằng font của game. Ảnh khác không đạt sau 3 lượt thì giữ bản tốt nhất, ghi rõ chỗ thiếu.
