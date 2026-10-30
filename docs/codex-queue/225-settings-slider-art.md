# Phiếu 225 · Ba game · Ảnh thanh trượt cho bảng Sound (rãnh `sliderTrack`, núm `sliderThumb`), 3 × 2 ảnh mức game thương mại

**Nguồn:**
- `docs/codex-queue/193-report.md`: "**Chưa có ảnh riêng cho track/thumb slider** trong art được giao; dùng range native của kit. Không tự vẽ ảnh thay. Claude cần quyết phần art này".
- `docs/games/IN_GAME_SETTINGS.md` §4: "Mọi icon, khung bảng, thanh trượt, nút là ảnh thật theo phong cách game (luật 28/10, không vẽ bằng mã)."
- `AGENTS.md` (chủ dự án 28/10): "Every UI detail carries real art, not text alone." và "Art must reach commercial-game level."
- Kit đã nhận sẵn hai ảnh này:
  - `shared/game-kit/ui/quick-settings/types.ts:110–115`: `QuickSkin { panel, button, sliderThumb, sliderTrack }`;
  - `shared/game-kit/ui/quick-settings/css.ts:72–76`: rãnh cao `s(10)`, ảnh kéo giãn `100% 100%`; núm là ô vuông `s(22)`, ảnh kéo giãn `100% 100%`.
- Chưa có ảnh thanh trượt nào: `find` trên `art-src` của ba game không ra file nào tên `*slider*`; chưa phiếu nào đặt ảnh này.

**Không trùng:**
- 180: chín icon bảng cài đặt (đã có, dùng làm tham chiếu bộ).
- 115/160 (Wordwoven), 162 (Dragonhold), 127 (Last Line): khung bảng và nút.
- 191, 192, 193: gắn bảng và tiếng phím, dùng range native của kit.
- 196 (Dragonhold, ổ icon HUD), 206 (Last Line, đường ảnh UI).
- Gắn ảnh vào `QuickSkin` của từng game là một phiếu mã sau, không thuộc phiếu này.

**Báo cáo:** `docs/codex-queue/225-report.md` (tiếng Việt) và thư mục `docs/codex-queue/225/` (JSON, Markdown, `.txt` và script; **không ảnh**). Cả hai ở repo cha.

## Chỉ chạy khi

Kiểm trước mọi lời gọi `image_gen`, ghi đầu ra vào `225/preflight.txt`:
1. Thư mục `games/<id>/art-src/ui/quick-settings/sliders/` chưa có, hoặc rỗng, ở cả ba game (`dragon-hold`, `typing-defense`, `typing-survival`). Có file: dừng, không ghi đè.
2. Không có file `games/<id>/art-src/_review/225*` nào.
3. Có đủ các ảnh tham chiếu ở mục "Tham chiếu" và ba file prompt PART ở mục "Prompt".
4. `/opt/homebrew/bin/magick -version` ra ImageMagick 7.
5. `date` từ **19:48 ngày 30/10/2026** giờ Việt Nam trở đi. Đó là giờ reset `image_gen` mà 145, 149, 153, 196, 201 cùng báo (`resets_at` 1793364445–1793364446, tức 19:47:25–26). Sớm hơn: không gọi `image_gen`; ghi báo cáo "chờ hạn mức ảnh" kèm giờ máy, lưu prompt đã viết vào `225/prompts.json`, rồi dừng.

Sai một điều: dừng, chỉ ghi báo cáo nêu điều nào sai.

**Luật hạn mức:**
- Lời gọi `image_gen` **đầu tiên** trả 429 hay `usage_limit_reached`: dừng ngay.
  - Ghi báo cáo với giờ reset công cụ trả về (`resets_at`, đổi sang giờ Việt Nam) và 0 ảnh.
  - Lưu lỗi vào `225/generation-error.json`, prompt đã viết vào `225/prompts.json`.
  - Không gọi lại; không dùng công cụ, CLI hay API tạo ảnh khác.
  - Hai phiếu 196 và 201 đã gặp lỗi này ngày 30/10, `resets_at` 19:47:26 giờ Việt Nam.
- Gặp 429 ở lời gọi sau: ngừng gọi tiếp; vẫn hậu kỳ, kiểm và báo cáo các ảnh đã có.

## Luật chung (phiếu ảnh)

**Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game` (cwd của làn, `.`). Không worktree, không `pnpm`. Ảnh là media, không vào Git (`art-src` và `tmp/` có trong `.gitignore` của cả ba game).

**Luật điểm** (như phiếu 180, mục "Luật chung"):
- Ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2), chấm **so với game thương mại**, không so với ảnh cũ của dự án.
- Hậu kỳ theo `ART_ACCEPTANCE.md` §5:
  - mỗi ảnh có tờ "bản sinh | bản hậu kỳ";
  - công cụ chỉ cắt, tách nền, đổi cỡ, sửa mép, chỉnh sáng nhẹ toàn ảnh (±10 %);
  - không xóa, san phẳng, phủ màu hay thay phần vẽ;
  - ngưỡng số mâu thuẫn với tranh (muốn đạt số phải làm bẩn tranh): dừng, giữ tranh, ghi mâu thuẫn để Claude quyết.
- Tối đa **3 lượt sinh mỗi ảnh**. Mỗi lượt sau sửa prompt đúng chỗ thiếu.
- Mọi lượt giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt`. Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`. Mỗi bản thu cũng có `.prompt.txt` cạnh nó, như bộ 180.

**Chỉ được ghi:**
- `games/{dragon-hold,typing-defense,typing-survival}/art-src/ui/quick-settings/sliders/` (thư mục mới);
- `games/{dragon-hold,typing-defense,typing-survival}/art-src/_review/225-*` (file mới: tờ xem, tờ so sánh);
- `games/{dragon-hold,typing-defense,typing-survival}/tmp/codex-225/` cho ảnh trung gian. Cuối phiếu xóa bằng `node tools/capture-prune/prune.mjs <thư mục> --min-age-min 0` (xem danh sách), rồi thêm `--apply`;
- `docs/codex-queue/225-report.md`, `docs/codex-queue/225/`.

**Cấm:**
- Chữ, số, chữ cái, logo, chữ ký, khung hay viền vẽ quanh vật trong ảnh.
- Ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`. Đụng bộ 180 trong `ui/quick-settings/` và `ui/quick-settings/selected/`.
- Mọi lệnh git; sửa mã hay tài liệu ngoài báo cáo. Nhất là `shared/game-kit/ui/quick-settings/**`: `css.ts` đang có thay đổi chưa commit của người khác.
- Chép ảnh vào `public/` (Claude chép khi gắn).
- Dev server, trình duyệt, mạng ngoài công cụ tạo ảnh. Công cụ, CLI, API tạo ảnh khác.
- Game khác (Space Typing…), Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*`), mọi `games/.wt-*`.

## Ảnh kit sẽ vẽ ra sao (đọc trước)

- **Thang:** `css.ts:24` `s(px) = px × --kit-qs-s`. `quick-settings.ts:273` đặt `--kit-qs-s = quickScale(chiều cao host)`; `logic.ts:181–184`: `clamp(cao / 720, 1, 1,5)`. Vậy ở 720p thang là 1, ở 1080p là 1,5.
- **Rãnh:** cao 10 px (720p) và 15 px (1080p). Rộng bằng ô range: `flex: 1 1 8em; min-width: 6em` (`css.ts:51`), cỡ chữ `s(15)` (`css.ts:29`).
  - Bảng rộng tối đa `s(560)`, lề hai bên `s(20)` (`css.ts:42`).
  - Hàng gồm icon `s(24)`, nhãn `9.5em`, hai khe `s(10)` (`css.ts:47`).
  - Ô số `2.4em` (`css.ts:53`), khe `s(8)` (`css.ts:50`).
  - Kết quả ở 720p: khoảng 90 px (tối thiểu) tới 290 px; khoảng 210 px ở hàng Master có nút tắt tiếng. Ở 1080p nhân 1,5.
- **Núm:** ô vuông 22 px (720p), 33 px (1080p), tâm trùng tâm rãnh (`margin-top: s(-6)`). Tâm núm chạy từ `núm/2` tới `rộng − núm/2`.
- **Màu nền dưới ảnh:** kit vẽ màu `--kit-qs-line` (mặc định `#4A505C`) dưới cả hộp rãnh, và `--kit-qs-text` (mặc định `#F3F4F6`) dưới ô vuông của núm (`css.ts:73–76`, mặc định ở `css.ts:10–20`). Phần trong suốt của ảnh sẽ lộ các màu đó. Phiếu này không sửa CSS. Báo cáo ghi điều này cho phiếu gắn sau.
- Kit không vẽ phần "đã đầy" của rãnh: ảnh rãnh không có mức đầy, không vạch chia.

## Tham chiếu

- **Mức hoàn thiện:** `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp`. Xem để lấy mức hoàn thiện của HUD (vòng kim loại, vát, ánh viền); không chép nội dung; **không đính kèm** vào lời gọi (như 180).
- **Bộ của từng game**, đính kèm mỗi lời gọi:

| Game | Ảnh đính kèm (tính từ `games/<id>/art-src/`) |
|---|---|
| Dragonhold (`dragon-hold`) | `ui/quick-settings/selected/hud-settings.png`, `ui/quick-settings/selected/vol-master.png`, `ui/parts/keycap.png` |
| Wordwoven (`typing-defense`) | `ui/quick-settings/selected/hud-settings.png`, `ui/quick-settings/selected/vol-master.png`, `ui/frames-epic/crest.png` |
| Last Line (`typing-survival`) | `ui/quick-settings/selected/hud-settings.png`, `ui/quick-settings/selected/vol-master.png`, `concepts/b-lightbearer-keyart.png` |

- Lời gọi của núm đính kèm thêm `ui/quick-settings/sliders/slider-track.png` (bản 1024×64 đã chọn của cùng game), để rãnh và núm thành một cặp.

## Prompt

Prompt tiếng Anh, ghép đúng thứ tự:
1. **Khối STYLE-UI nguyên văn** của game trong `docs/games/ART_DIRECTION_2026-10-28.md`: Wordwoven §2.2, Dragonhold §3.2, Last Line §4.3 (hướng B).
2. **Khối PART nguyên văn**, lấy đoạn PART trong file prompt của phiếu 146 (Dragonhold, đã sinh và nhận ảnh) và 145, 153 (Wordwoven, Last Line: prompt đã viết, lượt sinh 30/10 gặp 429 nên chưa có ảnh; 0 PNG trong `ui/parts/` của hai game này):
   - Dragonhold: đoạn `KIND PART: …` của `games/dragon-hold/art-src/ui/parts/keycap.prompt.txt`;
   - Wordwoven: đoạn `Game interface PART: …` của `games/typing-defense/art-src/ui/parts/card-plate.try1.prompt.txt`;
   - Last Line: đoạn `KIND PART: …` của `games/typing-survival/art-src/ui/parts/keycap.try1.prompt.txt`.
   - Với **rãnh**, bỏ câu về cỡ vật (Dragonhold: "The object occupies 70 percent of the canvas long edge…"; Wordwoven: "The visible object occupies 70% of the longest canvas dimension…"). Phần riêng thay câu đó.
3. **Phần riêng** của ảnh (bảng dưới).
4. Dòng tham chiếu: `Reference images: match the material finish of this game; reference content is not part of the requested object.`
5. **Dòng nền nguyên văn** từ cùng file prompt PART ở bước 2:
   - Dragonhold, Wordwoven: nền phẳng `#FF00FF`, cấm hồng, tím, magenta trong vật. Lượt đầu thấy vật có tím: lượt sau dùng `#00FF00` và ghi lại.
   - Last Line: nền trong suốt thật (RGBA), đoạn `Background: actual transparent background, RGBA. …` của `keycap.try1.prompt.txt`. Với rãnh, thay ba câu từ `Exactly one centered object on a 1024 x 1024 square canvas, …` tới `Empty transparent margins on every side.` bằng: `Exactly one object, the groove, centred on a 1536 x 1024 canvas, empty transparent margins on every side.` Với núm, giữ nguyên đoạn đó. Công cụ không cho trong suốt thì dùng `#FF00FF` rồi tách.

**Phần riêng (EN, chép nguyên văn vào prompt):**

| Game · ảnh | Khổ sinh | Phần riêng |
|---|---|---|
| Dragonhold · `slider-track` | 1536 × 1024 | `A long, straight, perfectly level slider groove for a volume control, shown flat and straight on: a recessed channel of dark forged iron with a faint warm sheen, bordered along both long edges by a thin bright line of hammered warm gold, made to sit on a dark weathered bark-brown panel. The channel is a medium-dark iron tone, clearly lighter than near-black. Short rounded forged-iron end caps, each no longer than 5 percent of the groove length, with one tiny gold stud. The long middle is plain and continuous, with quiet even texture and the same brightness from end to end, so it can be stretched sideways. No fill level, no tick marks, no notches, no knob, no symbols. The groove is about 1400 pixels long and 88 pixels high, centred on a 1536 x 1024 canvas.` |
| Dragonhold · `slider-thumb` | 1024 × 1024 | `A round slider knob, shown flat and straight on: a slightly domed disc of hammered warm gold set in a ring of dark forged iron, a small glowing ember-orange enamel centre, fine dragon-scale texture only on the iron ring. Much brighter than the dark iron groove it slides on. A bold, simple round silhouette that still reads as a knob at 22 pixels. The face carries no symbol. Square 1024 x 1024; the knob's diameter is 70 percent of the canvas, exactly centred.` |
| Wordwoven · `slider-track` | 1536 × 1024 | `A long, straight, perfectly level slider groove for a volume control, shown flat and straight on: a recessed channel of polished dark jade lacquer, bordered along both long edges by a thin gold-leaf rim, with small bronze cloud-scroll end caps, each no longer than 5 percent of the groove length. The jade channel is a medium-dark tone, clearly lighter than near-black, with quiet lacquer depth. The long middle is plain and continuous, with the same brightness from end to end, so it can be stretched sideways. No fill level, no tick marks, no notches, no knob, no symbols. The groove is about 1400 pixels long and 88 pixels high, centred on a 1536 x 1024 canvas.` |
| Wordwoven · `slider-thumb` | 1024 × 1024 | `A round slider knob, shown flat and straight on: a polished pale limestone and gold-leaf disc in a fine bronze bezel, a small dark jade cabochon at the centre, a faint Dong Son sun-star ring engraved on the rim only. Much brighter than the dark jade groove it slides on. A bold, simple round silhouette that still reads as a knob at 22 pixels. The face carries no symbol. Square 1024 x 1024; the knob's diameter is 70 percent of the canvas, exactly centred.` |
| Last Line · `slider-track` | 1536 × 1024 | `A long, straight, perfectly level slider groove for a volume control, shown flat and straight on: a recessed channel of dark smoked glass over graphite steel, a fine white-gold filigree line along both long edges, and one thin, faint electric-cyan glow line running the full length inside the glass. Short clipped graphite end caps, each no longer than 5 percent of the groove length. The glass reads medium-dark, clearly lighter than near-black. The long middle is plain and continuous, with the same brightness from end to end, so it can be stretched sideways. No fill level, no tick marks, no notches, no glyphs, no knob. The groove is about 1400 pixels long and 88 pixels high, centred on a 1536 x 1024 canvas.` |
| Last Line · `slider-thumb` | 1024 × 1024 | `A round slider knob, shown flat and straight on: a machined disc of ivory-white ceramic and white-gold, a small smoked-glass lens at the centre, one thin electric-cyan light seam around the lens. Much brighter than the smoked-glass groove it slides on. A bold, simple round silhouette that still reads as a knob at 22 pixels. The face carries no symbol or glyph. Square 1024 x 1024; the knob's diameter is 70 percent of the canvas, exactly centred.` |

Sửa phần riêng ở lượt 2–3 khi cần, ghi rõ sửa gì và vì sao.

## Việc

1. **Mốc KA1.** Với mỗi game:

   ```sh
   find games/<id>/art-src/ui/quick-settings -type f -print0 | sort -z | xargs -0 md5 -r > docs/codex-queue/225/md5-before-<id>.txt
   ```

   Ghi thêm `ls games/<id>/art-src/_review | grep '^225'` (kỳ vọng rỗng).
2. **Sinh rãnh**, từng game: lời gọi `image_gen` khổ 1536 × 1024 với prompt ở trên và ba ảnh bộ đính kèm. Lưu `sliders/slider-track.tryN.png` và `.tryN.prompt.txt`.
3. **Hậu kỳ rãnh:**
   - tách nền khóa thành alpha (`tools/art-normalize`, `export ART_MAGICK=/opt/homebrew/bin/magick`, hay magick trực tiếp);
   - cắt theo hộp bao alpha > 16;
   - `magick <bản cắt> -filter Lanczos -resize 1024x64! sliders/slider-track.png`;
   - `magick <bản cắt> -filter Lanczos -resize 512x32! sliders/slider-track.512.png`, thu thẳng từ bản cắt;
   - ghi hộp bao, tỉ lệ rộng/cao của nó và hệ số co theo x, y. Tỉ lệ lệch hơn 15 % so với 16 : 1 thì ghi rõ (co không đều làm méo đầu rãnh).
4. **Sinh núm**, từng game: khổ 1024 × 1024, ba ảnh bộ cộng `slider-track.png` đã chọn của game đó.
5. **Hậu kỳ núm:**
   - tách nền;
   - chỉ cắt hay thêm lề để hộp bao alpha > 16 có cạnh dài bằng 68–72 % cạnh ảnh, lệch tâm ≤ 2 %;
   - `slider-thumb.png` 1024², rồi `slider-thumb.256.png`, `.128.png`, `.64.png` thu Lanczos thẳng từ bản 1024. Không làm nét bản 64.
6. **Tờ "bản sinh | bản hậu kỳ"** cho mỗi ảnh (ART_ACCEPTANCE §5), cùng cỡ: `games/<id>/art-src/_review/225-slider-track-compare.jpg` và `225-slider-thumb-compare.jpg`.
7. **Kiểm số** bằng script `docs/codex-queue/225/audit.mjs` (node + magick, như `games/typing-defense/art-src/_review/180/audit-selected.mjs`). Kết quả vào `225/metrics.json`. Chưa đạt thì sửa bằng công cụ trong giới hạn §5, hoặc sinh lại (≤ 3 lượt).
8. **Tờ xem** và **KA5** (mục Kiểm 6, 7).
9. **Dọn** ảnh trung gian trong `tmp/codex-225/` bằng `tools/capture-prune/prune.mjs` như trên. Chạy lại md5 thành `225/md5-after-<id>.txt`.

## Kiểm (ghi số cho từng ảnh)

Luma trong phiếu: `Y = 0,2126 R + 0,7152 G + 0,0722 B` trên giá trị sRGB 0–1, như hàm `luma` trong `audit-selected.mjs` của 180. Trung bình tính trên pixel có alpha ≥ 128, sau khi đặt lên màu nền.

**Màu bảng** (tối / sáng):
- Dragonhold `#2b2118` / `#f1e3c4`;
- Wordwoven `#061e16` / `#b8aa94` (180-report dòng 78 đo từ `frames-epic/panel-large.v2.png`); ghi thêm số trên `#1f3b33` / `#e8e1cf` để đối chiếu;
- Last Line `#14181f` / `#8c96a3`.

1. **KA1:** `diff md5-before-<id>.txt md5-after-<id>.txt` chỉ có dòng thêm, và chỉ dưới `ui/quick-settings/sliders/`. Mọi file cũ (bộ 180, kể cả `selected/`) không đổi: lúc viết phiếu là 164 file ở Dragonhold, 162 ở Wordwoven, 162 ở Last Line; ghi số thật của `md5-before`.
2. **Khổ** (`magick identify -format '%f %wx%h %[channels]\n'`):
   - `slider-track.png` 1024×64 và `slider-track.512.png` 512×32, `srgba`;
   - `slider-thumb.png` 1024×1024 `srgba`, và đúng ba bản 256², 128², 64².
3. **Alpha sạch:**
   - ngoài dải mép 3 px quanh vật, mọi pixel có alpha 0 hay 255;
   - pixel có alpha > 0 mang màu khóa (hue lệch ≤ 15° so với màu khóa, S > 0,5) chiếm ≤ 0,2 %;
   - ghi hai số cho mỗi ảnh.
   - Riêng rãnh: tỉ lệ pixel alpha 255 trong 80 % giữa của bản 1024×64 (mục tiêu ≥ 0,90, vì kit vẽ `--kit-qs-line` dưới hộp rãnh).
4. **Kéo giãn** (kit kéo rãnh `100% 100%`):
   - dựng rãnh từ `slider-track.png` (1024×64) bằng `-filter Lanczos -resize WxH!` ở 90×10, 210×10, 290×10 (720p) và 135×15, 315×15, 435×15 (1080p), đặt lên màu bảng tối;
   - với mỗi bản: lấy luma trung bình từng cột trong 80 % giữa bề ngang; độ lệch chuẩn của các số đó **≤ 0,05**;
   - **đầu rãnh** đo trên bản 1024×64: từ mỗi đầu, cột đầu tiên mà từ đó 16 cột liền có luma trung bình nằm trong ±0,03 quanh trung vị của 80 % giữa. Bề rộng mỗi đầu **≤ 6 %** (≤ 61 px). Tỉ lệ này giữ nguyên ở mọi cỡ, vì kit co đều;
   - ghi bảng số.
5. **Đọc được ở cỡ trong game:**
   - dựng thanh ở 720p (rãnh 210×10, núm 22 px) và 1080p (rãnh 315×15, núm 33 px), núm ở 50 %, trên cả hai màu bảng;
   - luma núm trừ luma rãnh (phần rãnh không bị núm che): **≥ 0,25** trên ít nhất một màu bảng tối;
   - luma rãnh so với màu bảng tối: chênh **≥ 0,12**;
   - ghi số trên cả màu sáng. Luma nền tham khảo: `#2b2118` 0,135; `#061e16` 0,095; `#14181f` 0,093.
6. **Tờ xem** `games/typing-defense/art-src/_review/225-sheet.jpg` (kèm `225-sheet.prompt.txt` ghi lệnh dựng). Mỗi game một hàng:
   - thanh ở 0, 50, 100 % cỡ 720p, trên màu tối rồi màu sáng;
   - cùng như vậy ở cỡ 1080p;
   - icon `vol-master` của bộ 180 (`selected/vol-master.png`) ở 20 px và 28 px trên màu tối;
   - một mảnh HUD của ảnh chủ dự án, cùng chiều cao với khối 1080p;
   - bản phóng ×3 (lọc `point`) của thanh 720p ở 50 % trên màu tối;
   - một ô **"kit hôm nay"**: thanh 720p ở 50 % với `#4A505C` dưới hộp rãnh và `#F3F4F6` dưới ô vuông 22 px của núm (`css.ts:73–76`);
   - dưới mỗi ảnh ghi tên (font `/System/Library/Fonts/Supplemental/Arial.ttf`).
7. **KA5 tự chấm** mỗi ảnh:
   - 5 tiêu chí của thang 10 điểm, ART_ACCEPTANCE §1 (Đúng đề, Đọc được trong game, Hợp bộ, Hình khối, Dùng được cho bước sau), mỗi tiêu chí 0–2; ngưỡng đạt theo §2.2;
   - chấm trên bản hậu kỳ, ở cỡ gốc và cỡ 720p;
   - "Dùng tiếp" chỉ được 2 khi Kiểm 1–5 của ảnh đó đạt.
   - Xong chỉ khi mọi ảnh từ 8 điểm. Sau 3 lượt vẫn dưới 8: giữ bản tốt nhất nếu từ 7, ghi thiếu gì (ART_ACCEPTANCE §2.2). Claude chấm lại.
8. **Số lời gọi:** mỗi ảnh ≤ 3, tổng ≤ 18; ghi bảng.

## Báo cáo

`docs/codex-queue/225-report.md`, tiếng Việt:
- preflight; số lời gọi công cụ mỗi ảnh; lỗi hạn mức nếu có (giờ reset);
- prompt đầy đủ của từng lượt và đã sửa gì so với lượt trước (prompt cũng nằm trong `225/prompts.json`);
- bảng số Kiểm 1–5 cho sáu ảnh; điểm KA5 ở cỡ gốc và 720p;
- đường dẫn mọi file giao, tờ so sánh, tờ xem;
- chỗ làm khác phiếu và vì sao; mâu thuẫn giữa số và tranh (ART_ACCEPTANCE §5) nếu có;
- mục **"Việc của Claude"**:
  - chấm lại sáu ảnh;
  - phiếu gắn sau: mỗi game truyền `skin.sliderTrack` và `skin.sliderThumb` (URL ảnh trong `public/` do Claude chép);
  - `css.ts:73–76` vẽ `--kit-qs-line` dưới rãnh và `--kit-qs-text` dưới ô vuông của núm; khi có ảnh, màu nền đó cần trong suốt (xem ô "kit hôm nay");
  - `pnpm media:push` để sao lưu ảnh mới.

Script lưu ở `docs/codex-queue/225/`, chạy lại được từ gốc repo cha: `node docs/codex-queue/225/audit.mjs`.

**Xong khi:** đủ sáu ảnh và các bản thu; Kiểm 1–5 đạt, có số; KA5 từ 8 cho mọi ảnh; có tờ xem và báo cáo. **Nhận** khi Claude chấm lại từ 8.

**Làn:** s8, đặt cuối (sau 227), vì hạn mức công cụ ảnh mà 196 và 201 gặp reset lúc 19:47 ngày 30/10. Phiếu chỉ ghi thư mục mới, nên không đụng các phiếu đọc `art-src` ở s7 (194, 197) và s9 (200). Model `gpt-6.1-sol`, mức `high`. Dòng làn:
`225-settings-slider-art | docs/codex-queue/225-settings-slider-art.md | . | high | workspace-write | gpt-6.1-sol`
