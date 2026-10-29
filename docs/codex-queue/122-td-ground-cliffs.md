# Phiếu 122 · Wordwoven · Ô đất v2 và vách đá vôi cho sân 3D (8 ảnh)

**Nguồn:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md`, bible Wordwoven; thứ tự 8). Sáu ô đất của phiếu 095 chấm 3,5/10 theo mức chợ: cỏ xanh lá cây phẳng như sân bóng, đường vàng cam như đồ chơi. Ở camera 55° từ 58 m, đất chiếm gần hết màn hình, nên đất là thứ quyết định sân có hùng vĩ hay không. Phiếu thêm hai ô vách đá vôi để làn L dựng tháp đá và mép cao nguyên bằng mã (địa hình được dựng bằng mã; vật thì không).

**Báo cáo:** `docs/codex-queue/122-report.md`.

**Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5: tờ "bản sinh | bản hậu kỳ" cho mỗi ảnh; công cụ không được xóa, san phẳng hay phủ phần vẽ; ngưỡng số mâu thuẫn với tranh thì dừng và ghi lại; tự chấm trên bản hậu kỳ.

**Thứ tự:** sau 121 (nhóm "còn dưới 8"). Làn L cần trước C9 nếu được.

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận mới:** ảnh được chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp` (xem mặt đất: đất, đá, cỏ khô có chất liệu thật, nhiều sắc, không phẳng). Không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ (làm liền mép, chỉnh màu) thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/122/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn (kể cả `scenery/meadow/ground/*` của 095); xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, khung trong ảnh.
- **KA1 md5:** `md5 -r` mọi file trong `games/typing-defense/art-src/scenery/` (đệ quy) trước khi ghi (`_review/122/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, mức chợ, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: chất liệu thật, nhiều sắc độ có chủ đích, đọc rõ làn đường ở xa, hợp cảnh sử thi. 7 là gọn nhưng thường. 5 là đúng chất liệu nhưng sai tầm (đồ chơi, phẳng). 4 là màu phẳng kiểu clip-art. Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2, mỗi tiêu chí 0–2. "Dùng tiếp" chỉ được 2 khi mọi số đo của phiếu đạt.
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**. M chấm trên mặt đất thử (mục Kiểm 7).
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8.

**Đo chung** (cùng cách của phiếu 095):
- `L = 0,2126R + 0,7152G + 0,0722B` trên sRGB 0–1.
- **Độ rối** = trung bình `|L − box5×5(L)|`, biên tuần hoàn.
- **Mép liền:** `E` = trung bình `|L(cột 0) − L(cột N−1)|` và `|L(hàng 0) − L(hàng N−1)|`; `I` = trung bình độ lệch giữa hai px kề nhau bên trong theo X và Y. Đạt khi `E ≤ 1,25 · I`. Chưa liền thì làm liền bằng cách của phiếu 093 (`roll` nửa ô, phủ chữ thập giữa bằng mặt nạ cosin) và đo thêm chữ thập: tỉ số ≤ 1,25.
- **Đốm lặp:** box-blur 129 px tuần hoàn trên `L`, lấy `p95 − p5`.

## Phiếu

**Nơi ghi:** `games/typing-defense/art-src/scenery/meadow/ground-v2/` (thư mục mới).

**Chỉ được ghi:**
- `ground-v2/<tên>.tryN.png`, `.tryN.prompt.txt`, bản chọn `<tên>.png`, `<tên>.prompt.txt`;
- `games/typing-defense/art-src/_review/122-*.jpg`, `games/typing-defense/art-src/_review/122/`;
- `docs/codex-queue/122-report.md`.

**Đọc trước (chỉ đọc):** ảnh tham chiếu; ô cũ `scenery/meadow/ground/*.png` và `095-report.md` (cách đo); sân 3D hôm nay `games/.wt-td-1c/tmp/lane-l/td-1c-ground-sheet-1920x1080.jpg`; ảnh ghép của phiếu 114 nếu đã có (cùng màu sương và nắng).

### Khối prompt (nguyên văn)

Mỗi prompt = **STYLE** + **MAP** + **GROUND** (sáu ô đất) hay **CLIFF** (hai ô vách) + phần riêng.

**STYLE**
```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.
```

**MAP**
```text
Asset for a 3D strategy game seen from a high camera looking 55 degrees down from 58 metres: every shape must read at that distance, so group detail into big masses with strong light-dark contrast, keep edges clean, and avoid fine noise, tiny scattered bits and thin strands.
```

**GROUND**
```text
Seamless tileable ground texture, edges wrap on all four sides, seen straight from above with no perspective. One tile covers 8 by 8 metres of ground. Flat, even, shadowless light: no cast shadows and no sun direction, the game lights it. Rich natural material with several close tones in big soft patches, painted detail no smaller than about 15 centimetres. No standing objects, no plants taller than the ground cover, no people or animals.
```

**CLIFF**
```text
Seamless tileable cliff texture, edges wrap on all four sides, seen straight on as a flat vertical rock face with no perspective. One tile covers 12 by 12 metres of cliff. Flat, even, shadowless light: no cast shadows and no sun direction, the game lights it. No sky, no ground line, no plants sticking out of the face.
```

### Tám ô (1024 × 1024, sRGB 8 bit, không alpha)

| Tên | Phần riêng |
|---|---|
| `grass-jade` | `Lush jade meadow grass of a high karst plateau: deep jade and teal-green blades in big soft swathes, gold-lit patches where the grass is drier, a few darker clumps.` |
| `grass-moss` | `The same meadow grass mixed with thick dark moss and small creeping clover, slightly darker and cooler than the meadow.` (đính kèm `grass-jade` đã chọn, dòng `Use the attached image only to match the style, colours and scale. Paint a different ground as described.`) |
| `road-paved` | `An ancient paved road of worn pale limestone slabs, big irregular slabs fitted tightly, fine moss in the joints, edges rounded by centuries of feet; the slabs run along the vertical axis of the image.` |
| `trail-worn` | `The worn edge of an old road: packed pale earth and broken limestone pieces mixed with thinning grass, used between the road and the meadow.` |
| `stream-bank` | `A riverbank of wet dark river stones and pale pebbles in grey silt, a few patches of moss, wet sheen painted as lighter tones.` |
| `courtyard` | `A temple-fortress courtyard of large square limestone flagstones laid in a regular grid, warm cream with grey veins, thin dark joints, a few cracked slabs.` |
| `cliff-face` | CLIFF + `A sheer limestone karst cliff: pale grey-white rock with deep vertical fluted grooves carved by rain, dark streaks where water runs, small ledges with dark jade moss.` |
| `cliff-moss` | CLIFF + `The same karst cliff heavily covered in dark jade moss and hanging vines in big masses, rock showing between them.` (đính kèm `cliff-face` đã chọn với dòng như trên) |

**Thang:** một ô đất phủ 8 × 8 m (khoảng 7,8 mm mỗi px); một ô vách phủ 12 × 12 m. Chi tiết nhỏ hơn 15 cm thành nhiễu ở camera chơi.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/typing-defense/art-src/scenery/` (đệ quy).
2. `magick identify`: 1024 × 1024, sRGB, không kênh alpha.
3. **Mép liền:** `E ≤ 1,25 · I` cho cả tám ô. Ghi `E`, `I`, tỉ số trước và sau khi làm liền.
4. **Độ rối:** hai ô cỏ ≤ 0,035; bốn ô đất đá ≤ 0,045; hai ô vách ≤ 0,055.
5. **Đốm lặp:** `p95 − p5` ≤ 0,09 cho ô cỏ; ≤ 0,12 cho ô còn lại.
6. **Màu đi với nhau** (trung vị trên cả ô):
   - hue hai ô cỏ trong 80–150° (ngả ngọc, không xanh lá chuối); hai ô cỏ lệch ≤ 10° hue và ≤ 0,06 luma; S trung vị của cỏ ≤ 0,55 (bộ cũ quá rực);
   - luma `road-paved` ≥ luma `grass-jade` + 0,15, và luma `courtyard` ≥ luma `grass-jade` + 0,15 (đường và sân đọc rõ ở xa);
   - `trail-worn` nằm giữa `grass-jade` và `road-paved` về luma;
   - luma `stream-bank` ≤ luma `road-paved` − 0,10;
   - 0 % px có hue 285–330° và S > 0,5.
7. **Mặt đất thử và tờ so:**
   - `_review/122-tiles.jpg`: mỗi ô một cột: ô ở 512 px, rồi ô lát 3 × 3 thu về 512 px;
   - `_review/122-mock.jpg`: mặt đất thử 2048 × 1152 lát `grass-jade` có mảng `grass-moss`, một dải `road-paved` viền `trail-worn`, một suối viền `stream-bank`, một sân `courtyard`, và một bờ vách `cliff-face` / `cliff-moss` dựng đứng ở mép (có thể phối cảnh đơn giản bằng script); thu về 1280 px rộng; mặt nạ mềm vẽ bằng script;
   - `_review/122-vs-ref.jpg`: `122-mock.jpg` cạnh ảnh tham chiếu và cạnh một khung sân 3D hôm nay (cắt từ `td-1c-ground-sheet-1920x1080.jpg`), cùng cao 640 px. Ghi một dòng: "đứng cạnh được" hay "chưa", và vì sao.
   Xem bằng mắt ở cỡ đầy đủ. Ghi "không thấy đường nối, không thấy lặp" hay chỉ chỗ thấy.
8. **KA5 mức chợ:** M trên `122-mock.jpg`; Q cho từng ô ở cỡ đầy đủ và ở 256 px.

**Xong khi:** tám ô qua mục 2–6, `122-mock.jpg` tự chấm M ≥ 8, mỗi ô Q ≥ 8. Ô nào không đạt sau 3 lượt thì ghi rõ chỗ trượt và đề xuất cách khác.
