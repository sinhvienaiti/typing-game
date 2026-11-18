# Phiếu 155 · Dragonhold · Đường đá núi: hai ô đất và một tờ decal mép đường

**Nguồn:** chủ dự án 29/10/2026 sáng: "phần đường đi cũng phải làm thật đẹp, chứ đường đi nhìn như kiểu lấy ngón tay quệt dài như kia nó rất xấu". Luật chung cho đường của ba game ở `docs/games/PATH_QUALITY.md`. Bible Dragonhold ở `docs/games/ART_DIRECTION_2026-10-28.md` §3. Ô `path` hiện có (`games/dragon-hold/public/assets/dragon-hold/ground/pine-river/path.webp`) là một dải đất trơn; trên sân nó thành vệt màu đều, mép mờ. Phiếu này vẽ đường đá cổ của ải núi để làn map (R2) dựng đường thật.

**Báo cáo:** `docs/codex-queue/155-report.md`.

**Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5: tờ "bản sinh | bản hậu kỳ" cho mỗi ảnh; công cụ không được xóa, san phẳng hay phủ phần vẽ; ngưỡng số mâu thuẫn với tranh thì dừng và ghi lại; tự chấm trên bản hậu kỳ.

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận:** chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp` (xem mặt đất và đường đất đá trong cảnh: nhiều sắc độ, có hướng, có mép). Không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ (cắt, tách nền, làm liền mép) thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt`. Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/155/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, khung trong ảnh.
- **KA1 md5:** `md5 -r` mọi file trong `games/dragon-hold/art-src/` (đệ quy) trước khi ghi (`_review/155/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: chất liệu thật, nhiều sắc độ có chủ đích, có hướng chạy dọc đường, đọc rõ ở xa. 5 là đúng vật nhưng phẳng như đồ chơi. Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2, mỗi tiêu chí 0–2.
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**.
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8.

## Phiếu

**Nơi ghi:** `games/dragon-hold/art-src/ground-v3/road/` (thư mục mới).

**Chỉ được ghi:**
- `ground-v3/road/<tên>.tryN.png`, `.tryN.prompt.txt`, bản chọn `<tên>.png`, `<tên>.prompt.txt`, `.alpha.png` cho tờ decal;
- `games/dragon-hold/art-src/_review/155-*.jpg`, `games/dragon-hold/art-src/_review/155/`;
- `docs/codex-queue/155-report.md`.

**Đọc trước (chỉ đọc):** ảnh tham chiếu; `docs/games/PATH_QUALITY.md`; các ô đất đang dùng `games/dragon-hold/public/assets/dragon-hold/ground/pine-river/*.webp` (để đo luma và hợp màu); ảnh 120 nếu đã có (`games/dragon-hold/art-src/`).

### Khối prompt (nguyên văn)

Mỗi prompt = **STYLE** + **MAP** + **TOP** + phần riêng (+ dòng nền M cho tờ decal).

**STYLE** (ART_DIRECTION §3.2, nguyên văn)
```text
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
```

**MAP**
```text
Asset for a 3D strategy game seen from a high camera looking about 50 degrees down: every shape must read at that distance, so group detail into big masses with strong light-dark contrast, keep edges clean, and avoid fine noise, tiny scattered bits and thin strands. No large areas of bright red, orange, gold or turquoise; those colours are reserved for game signals.
```

**TOP**
```text
Seen straight from above with no perspective. Flat, even, shadowless light: no cast shadows and no sun direction, the game lights it. No outline and no ink line.
```

**Dòng nền M:** `Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.`

### Hai ô đất, 1024 × 1024, sRGB, không alpha, liền mép bốn phía

| Tên | Phần riêng |
|---|---|
| `road-flagstone` | `Seamless tileable texture, edges wrap on all four sides. An ancient mountain-pass road of worn cream granite flagstones, large irregular slabs fitted tightly in courses that run along the vertical axis of the image, the centre polished and slightly darker where centuries of feet and carts passed, two faint wheel ruts along the road, dark moss and pine needles in the joints, a few cracked slabs.` |
| `road-verge` | `Seamless tileable texture, edges wrap on all four sides. The worn verge of an old granite road: packed dark earth, coarse gravel, broken flagstone pieces and fallen pine needles mixed with thinning olive-green mountain grass, used between the road and the meadow.` |

### Tờ decal mép đường: lưới 4 × 2, 2048 × 1024, ô 512 × 512 (4 m), alpha

Sinh hai ảnh vuông 2 × 2 (bốn món mỗi ảnh, `road-edges-left`, `road-edges-right`), rồi ghép bằng script thành `road-edges.png` và `road-edges.alpha.png`, như phiếu 097 của Wordwoven. Mọi món nhìn từ trên, chạy dọc trục đứng của ô, đính kèm `road-flagstone` và `road-verge` đã chọn làm ảnh tham chiếu chất liệu với dòng `Use the attached images only for material and colour. Paint the new pieces as described.`

Tám món:
1. một hàng đá bờ hoa cương xếp thẳng;
2. đá bờ xếp theo khúc cong;
3. phiến đá lát vỡ tràn ra cỏ;
4. quạt sỏi ở mép đường;
5. khóm cỏ núi trùm qua mép đá;
6. vệt bánh xe có vũng nước phản trời lạnh;
7. một mảng rêu sẫm và lá thông lấp khe đá;
8. ba bậc đá thấp lún dưới cỏ.

Mép rõ, không viền mực; sau khi tách nền làm mềm alpha 6–12 px vào trong hình.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/dragon-hold/art-src/` (đệ quy).
2. **Khổ:** hai ô 1024², tờ decal 2048 × 1024; `magick identify` ra đúng; tờ decal có alpha.
3. **Liền mép:** dịch hai ô 50 % theo cả hai trục (`-roll +512+512`), xem ở cỡ đầy đủ: không thấy đường nối. Ghi "không thấy" hay chỉ chỗ thấy. Đo chênh luma trung bình của dải 8 px hai bên mép ≤ 0,03.
4. **Hướng dọc đường:** trong `road-flagstone`, năng lượng gradient theo trục ngang lớn hơn theo trục dọc ít nhất 1,2 lần (khe đá chạy dọc). Ghi tỷ số.
5. **Đọc ở xa:** luma trung bình `road-flagstone` ≥ luma `ground/pine-river/grass-a.webp` + 0,12; `road-verge` nằm giữa hai ô đó; tỷ lệ px bão hòa cao (S > 0,6, V > 0,7, hue 0–60° hay 160–200°) ≤ 2 %.
6. **Alpha sạch** (tờ decal): ngoài dải mép 12 px quanh vật, alpha là 0 hay 255; px có alpha > 0 mang màu nền (hue lệch ≤ 15° so với #FF00FF, S > 0,5) ≤ 0,2 %.
7. **Tờ thử** `_review/155-mock.jpg`, 2048 × 1152, nhìn từ trên: lát `grass-a` đang dùng; một đường cong chữ S rộng 4–5 m bằng `road-flagstone`, hai bên viền `road-verge` với mép nhiễu, rải 10–14 món decal dọc hai mép; một ngã ba. Kèm bản thu về 1024 × 576 (cỡ gần camera chơi). Xem bằng mắt và ghi một câu trả lời cho: **"Đường có trông như vệt quệt không?"** Nếu có, sửa và sinh lại.
8. **KA5 mức chợ:** M và Q cho ba bản chọn, ở cỡ đầy đủ và ở cỡ tờ thử thu nhỏ.

**Xong khi:** ba ảnh có bản chọn, qua mục 2–7, mỗi ảnh tự chấm M ≥ 8 và Q ≥ 8. Ảnh nào không đạt sau 3 lượt thì giữ bản tốt nhất, ghi rõ chỗ thiếu.
