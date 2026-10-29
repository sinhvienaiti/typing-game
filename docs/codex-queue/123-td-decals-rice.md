# Phiếu 123 · Wordwoven · Decal mặt đất v2 và năm ô Rice Field v2 (7 ảnh giao)

**Nguồn:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md`, bible Wordwoven; thứ tự 8). Decal của 097 (4,5/10) và ô ruộng của 098 (5/10) theo kiểu sách tranh cũ: màu rực, hình như đồ chơi, tờ b có viền mực. Bộ mới đi với ô đất v2 của phiếu 122.

**Báo cáo:** `docs/codex-queue/123-report.md`.

**Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5: tờ "bản sinh | bản hậu kỳ" cho mỗi ảnh; công cụ không được xóa, san phẳng hay phủ phần vẽ; ngưỡng số mâu thuẫn với tranh thì dừng và ghi lại; tự chấm trên bản hậu kỳ.

**Thứ tự:** sau 122 (dùng bản chọn của 122 để thử ghép).

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận mới:** ảnh được chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp`. Không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/123/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn (kể cả `scenery/meadow/decals/*`, `scenery/meadow/rice/*`); xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, khung trong ảnh.
- **KA1 md5:** `md5 -r` mọi file trong `games/typing-defense/art-src/scenery/` (đệ quy) trước khi ghi (`_review/123/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, mức chợ, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: chất liệu thật, hòa vào đất, đọc rõ ở xa, hợp cảnh sử thi. 7 là gọn nhưng thường. 5 là đúng vật nhưng sai tầm (đồ chơi). 4 là phẳng kiểu clip-art. Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2, mỗi tiêu chí 0–2.
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**. M chấm trên ảnh ghép thử (mục Kiểm 6).
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8.

## Phiếu

**Nơi ghi:** `games/typing-defense/art-src/scenery/meadow/decals-v2/` và `games/typing-defense/art-src/scenery/meadow/rice-v2/` (thư mục mới).

**Chỉ được ghi:**
- `decals-v2/ground-decals-a.*`, `decals-v2/ground-decals-b.*`, `decals-v2/road-edges-c.*` (lượt sinh `-left.tryN.*`, `-right.tryN.*`; hai nửa chọn `-left.png`, `-right.png`; tờ ghép `.png` trên nền `#FF00FF`; `.alpha.png`);
- `rice-v2/<tên>.tryN.png`, `.tryN.prompt.txt`, `<tên>.png`, `<tên>.prompt.txt`;
- `games/typing-defense/art-src/_review/123-*.jpg`, `games/typing-defense/art-src/_review/123/`;
- `docs/codex-queue/123-report.md`.

**Đọc trước (chỉ đọc):** ảnh tham chiếu; `docs/codex-queue/097-td-ground-decals.md` và `098-td-rice-field.md` (lưới, thang, hàng lúa, cách đo giữ nguyên); ô đất v2 của phiếu 122 (`scenery/meadow/ground-v2/`).

### Khối prompt (nguyên văn)

Mỗi prompt = **STYLE** + **MAP** + **TOP** + phần riêng (+ dòng nền M cho decal).

**STYLE**
```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.
```

**MAP**
```text
Asset for a 3D strategy game seen from a high camera looking 55 degrees down from 58 metres: every shape must read at that distance, so group detail into big masses with strong light-dark contrast, keep edges clean, and avoid fine noise, tiny scattered bits and thin strands.
```

**TOP**
```text
Seen straight from above with no perspective. Flat, even, shadowless light: no cast shadows and no sun direction, the game lights it. No outline and no ink line.
```

**Dòng nền M:** `Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.`

### Decal: ba tờ, mỗi tờ lưới 4 × 2, 2048 × 1024, ô 512 × 512 (4 m)

Sinh hai ảnh vuông 2 × 2 (bốn món mỗi ảnh, `-left` và `-right`), rồi ghép bằng script thành một tờ, như 097.

- **Tờ a (đất):** đất mòn sáng ×2; đất dưới tán (sẫm, lá rụng) ×2; ngã ba của ba lối mòn ×1; mẩu lối mòn thẳng ×1; mẩu lối mòn cong ×1; một mảng đá lát cổ lún dưới cỏ ×1. Mép mềm làm bằng công cụ: sau khi tách nền, làm mềm alpha 12–24 px vào trong hình.
- **Tờ b (vật nhỏ):** khóm hoa dã quỳ vàng nhìn từ trên ×1; khóm hoa huệ trắng ×1; sỏi đá vôi rải ×2; lá bàng đỏ rụng ×1; gốc cây cổ thụ nhìn từ trên ×1; vòng vụn gỗ (dấu cây luật đã chặt) ×1; một vũng nước nhỏ có lá sen ×1. Mép rõ, không viền mực.

- **Tờ c (mép đường, chủ dự án 29/10: đường không được trông như vệt quệt, xem `docs/games/PATH_QUALITY.md`):** mọi món nhìn từ trên, chạy dọc trục đứng của ô, hợp với `road-paved` và `trail-worn` của 122 (đính kèm hai ô đó làm ảnh tham chiếu chất liệu). Viên đá bờ vôi xếp thẳng ×1; viên đá bờ xếp theo khúc cong ×1; phiến đá lát vỡ tràn ra cỏ ×1; quạt sỏi vôi ở mép đường ×1; khóm cỏ trùm qua mép đá ×1; vệt bánh xe có vũng nước bạc ×1; ngã ba có ba phiến đá lớn mòn ×1; bậc đá ba phiến lún dưới cỏ ×1. Mép rõ, không viền mực; làm mềm alpha 6–12 px.

### Rice Field: năm ô 1024 × 1024, sRGB, không alpha, liền mép

`rice-flooded` (ruộng ngập nước bạc, phản chiếu trời), `rice-seedling` (mạ non), `rice-green` (lúa xanh ngọc), `rice-ripe` (lúa chín vàng óng), `rice-stubble` (gốc rạ). Luật hàng như 098: một ô phủ 4 × 4 m; hàng lúa chạy dọc, đúng 8 hàng, cách đều 128 px; bốn ô có cây có hàng ở cùng vị trí. Sinh `rice-green` trước, dùng làm ảnh tham chiếu cho ba ô kia với dòng `Same rows as the attached image: identical row positions and spacing. Change only the crop stage as described.` Phần riêng của mỗi ô thêm câu `Seamless tileable texture, edges wrap on all four sides.`

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/typing-defense/art-src/scenery/` (đệ quy).
2. **Decal:** `.alpha.png` đúng 2048 × 1024, RGBA; đủ 8/8 ô có vật; bbox mỗi vật cách mép ô ≥ 24 px; vật chiếm ≥ 35 % ô. Tách nền sạch: 0 % px có alpha > 0 mà hue 285–330° và S > 0,5. Mép mềm tờ a: trong mỗi ô, px alpha 0,1–0,9 chiếm ≥ 10 % số px có alpha > 0.
3. **Rice:** `magick identify` 1024 × 1024, sRGB, không alpha; mép liền `E ≤ 1,25 · I` (cách đo của 095); chu kỳ hàng 128 ± 4 px; lệch pha giữa hai ô có cây ≤ 8 px.
4. **Màu:**
   - decal tờ a: hue trung vị của các món đất lệch ≤ 12° so với `ground-v2/trail-worn.png` (phiếu 122);
   - rice: `rice-seedling`, `rice-green` hue 75–140°, S trung vị ≤ 0,55; `rice-ripe` hue 38–55°; `rice-stubble` hue 25–50°, S ≤ 0,35; `rice-flooded` S ≤ 0,30, luma 0,45–0,70.
5. **Không viền mực:** dải 3 px ngoài cùng của mỗi món decal có luma trung vị ≥ 0,6 × luma trung vị của món đó.
6. **Ảnh ghép và tờ so:**
   - `_review/123-on-ground.jpg`: mỗi món decal ghép lên ô đất v2 đúng thang (ô decal 512 px trên ô đất 1024 px), thu về 1280 px rộng; ghi món nào trông như dán, món nào hòa vào đất;
   - `_review/123-terraces.jpg`: năm ô rice lát 3 × 3 cạnh nhau, rồi một thửa ruộng bậc thang giả (ba bậc, bờ đá `ground-v2/courtyard.png` hay `trail-worn.png` làm bờ) dựng bằng script;
   - `_review/123-vs-ref.jpg`: hai ảnh trên cạnh ảnh tham chiếu, cùng cao 640 px; hàng dưới là decal và rice cũ (097, 098). Ghi một dòng: "đứng cạnh được" hay "chưa", và vì sao.
7. **KA5 mức chợ:** M trên hai ảnh ghép; Q cho từng tờ và từng ô ở cỡ đầy đủ và ở 256 px.

**Xong khi:** hai tờ decal và năm ô rice qua mục 2–5; hai ảnh ghép tự chấm M ≥ 8; mỗi ảnh Q ≥ 8. Ảnh nào không đạt sau 3 lượt thì giữ bản tốt nhất, ghi rõ chỗ thiếu.
