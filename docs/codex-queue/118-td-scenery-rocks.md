# Phiếu 118 · Wordwoven · Cảnh vật v3, v4 sử thi: đá và gỗ (8 ảnh)

**Nguồn:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md`, bible Wordwoven; thứ tự 4). Phần 118 (đá, gỗ mục, gốc cây) của bản viết lại phiếu 106 đã rút (xem phiếu 116 để biết vì sao). v3, v4 theo kiểu mới thành bộ chuẩn; v1, v2 cũ thôi dùng khi Claude tích hợp (không xóa).

**Báo cáo:** `docs/codex-queue/118-report.md`.

**Thứ tự:** sau 117.

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận mới:** ảnh được chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp`. Lấy mức chi tiết, ánh sáng và chất liệu; không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ (tách nền, cắt, thêm lề, chỉnh màu) thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/118/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn (kể cả v1, v2 và `.v1.png`); xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, khung trong ảnh.
- **KA1 md5:** `md5 -r` mọi file trong `games/typing-defense/art-src/scenery/` (đệ quy) trước khi ghi (`_review/118/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, mức chợ, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: dáng hùng, chất liệu thật (vỏ cây, lá, đá), chi tiết hoàn thiện mà vẫn gom thành khối lớn, hợp cảnh sử thi. 7 là gọn nhưng thường. 5 là đúng vật nhưng sai tầm (dễ thương, đồ chơi). 4 là phẳng kiểu clip-art. Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2, mỗi tiêu chí 0–2.
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**.
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8.

## Phiếu

**Vì sao:** cây cỏ là thứ người chơi thấy nhiều nhất trên sân 3D, ở camera 55° từ 58 m. Hôm nay chúng như hình dán tròn trịa có viền mực, cạnh nhà và quái Tripo bóng bẩy. Bộ mới vẽ thật hơn, hùng hơn, không viền mực, để hợp với trời và phông của 114. Mỗi loại cần ≥ 4 biến thể (TK §23.10); phiếu này làm 2, đợt sau làm thêm 2. Claude tắt viền mực của script `prepare-scenery` cho bộ này khi tích hợp.

**Nơi ghi:** `games/typing-defense/art-src/scenery/meadow/` (12 loại) và `games/typing-defense/art-src/scenery/shared/` (`tree-stump`), tên `<loại>-v3.*` và `<loại>-v4.*`.

**Chỉ được ghi:**
- `<loại>-v3.tryN.png`, `<loại>-v3.tryN.prompt.txt`, bản chọn `<loại>-v3.png`, `<loại>-v3.prompt.txt` (và cùng thế cho `-v4`), chỉ với các loại trong bảng của phiếu này;
- `games/typing-defense/art-src/_review/118-*.jpg`, `games/typing-defense/art-src/_review/118/`;
- `docs/codex-queue/118-report.md`.

**Đọc trước (chỉ đọc):** ảnh tham chiếu; v1, v2 của từng loại (để biết loại vật và khổ; không theo kiểu vẽ của chúng); `games/typing-defense/docs/art-requests/td/03-2d-scenery-ui-vfx.md` §3.8 (dòng nền); ảnh ghép `_review/114-composite-day.jpg` (phiếu 114) nếu đã có; bản chọn của phiếu 116 (`*-v3.png`, `*-v4.png` của `almond-tree`, `bamboo-clump`, `canopy-block`, `mountain-pine`), để cùng kiểu vẽ, màu và nắng.

### Khối prompt (nguyên văn)

Mỗi prompt = **STYLE** + **MAP** + **SCENERY** + phần riêng + dòng nền theo §3.8.

**STYLE**
```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.
```

**MAP**
```text
Asset for a 3D strategy game seen from a high camera looking 55 degrees down from 58 metres: every shape must read at that distance, so group detail into big masses with strong light-dark contrast, keep edges clean, and avoid fine noise, tiny scattered bits and thin strands.
```

**SCENERY**
```text
Single scenery cut-out for a 3D game that shows plants and rocks as painted billboards: exactly one object, whole and complete, centred, its base at the bottom centre of the image, a small empty margin on every side. Seen from the front, a little above eye level, about 15 degrees down. Soft even light from the front and above: no cast shadow, no sun direction, each big mass a little darker on its underside. Natural, grand and believable rather than cute: no outline, no ink line, no cartoon shapes. No ground, no soil, no grass and no pebbles around the base: the base ends cleanly. No blur, no glow, no see-through parts, no thin strands, no tiny scattered leaves, no floating bits.
```

**Dòng nền** (§3.8): vật có xanh lá, không hồng hay tím → nền M `#FF00FF`; vật có cả xanh lá và hồng hay tím → nền B `#0000FF`; vật không có xanh lá → nền G `#00FF00`. Dán đúng câu của §3.8. Ghi nền đã dùng cho từng ảnh.

**Hai biến thể phải khác nhau rõ:** khác hướng nghiêng, chiều cao, số và cách xếp khối tán hay khối đá. Ghi trong prompt khác ở đâu.

### Tám ảnh

| Loại | Vật (dán vào phần riêng) | `v3` | `v4` | Khổ |
|---|---|---|---|---|
| `rock-medium` | `A weathered limestone karst boulder: pale grey-white stone with sharp fluted ridges and deep vertical grooves carved by rain, dark jade moss in the hollows.` | `tall, a pointed top leaning left` | `wide and low, split in two blocks` | vuông, cạnh ≥ 1254 |
| `rock-small` | `A small weathered limestone rock with sharp fluted ridges and a cap of dark jade moss.` | `rounded, one tall side` | `flat slab with a raised edge` | ngang 1536 × 1024 |
| `rotten-log` | `A fallen ancient log of a giant forest tree: deep cracked bark, a broken hollow end, thick moss and small ferns growing on top.` | `long and straight, the hollow end on the right` | `shorter, bent, a broken branch stub rising` | ngang 1536 × 1024 |
| `tree-stump` (ở `scenery/shared/`) | `An old stump of a giant tree: wide buttress roots, cracked grey bark, a flat weathered top with growth rings, moss on the roots.` | `tall, a jagged broken top` | `low and wide, a clean cut top` | vuông, cạnh ≥ 1254 |

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/typing-defense/art-src/scenery/` (đệ quy).
2. **Khổ:** `magick identify`, đúng cột Khổ; cạnh dài ≥ 1024.
3. **Nền sạch:** 10 px mép bốn phía là màu nền, mỗi kênh lệch ≤ 12; trong vật (px lệch màu nền > 60 ở một kênh), px có hue trong ±12° của màu nền và S > 0,5 chiếm ≤ 0,5 %.
4. **Một vật, chân ở đáy:** tách nền (`magick <ảnh> -fuzz 18% -fill none -draw "color 0,0 floodfill" -alpha extract -trim -format '%X %Y %w %h' info:` hay cách tương đương, ghi lệnh); đáy hộp bao cách mép dưới ≤ 12 % chiều cao; lề trái, phải, trên ≥ 3 %; đúng một vùng liền có diện tích > 1 % ảnh.
5. **Không viền mực:** dải 3 px ngoài cùng của vật (sau tách nền) có luma trung vị ≥ 0,6 × luma trung vị của cả vật. Ghi số. (Bộ cũ có viền đen, trượt mục này.)
6. **v3 khác v4:** tỉ lệ rộng : cao của hộp bao, hoặc vị trí cột cao nhất, lệch nhau ≥ 15 %. Ghi bảng.
7. **Đọc ở cỡ nhỏ:** mỗi ảnh thu về 128 px cạnh dài: nhận ra loại cây không. Ghi.
8. **Tờ so** `_review/118-sheet.jpg`: mỗi loại một hàng v1, v2 (cũ), v3, v4 (mới), cùng cao 256 px, trên nền `#3f5a48`, có nhãn.
9. **Tờ trong cảnh và so với tham chiếu:**
   - `_review/118-mock.jpg`: 1536 × 1024, một khoảnh đất đá dựng bằng script: các bản chọn đã tách nền rải thành cụm, cỡ theo mét (đá vừa 2–4 m, đá nhỏ 0,6–1,2 m, khúc gỗ 4–6 m, gốc cây 1,5–2,5 m; người lính cao 1,8 m làm thước), cạnh cây của 116 và 117 nếu có, không thì trên nền dốc màu ngọc;
   - `_review/118-vs-ref.jpg`: `118-mock.jpg` cạnh ảnh tham chiếu, cùng cao 640 px. Ghi một dòng: "đứng cạnh được" hay "chưa", và vì sao.
10. **KA5 mức chợ:** M và Q cho từng bản chọn, ở cỡ đầy đủ và ở 128 px; thêm một điểm M chung trên `118-mock.jpg`.

**Xong khi:** tám ảnh có bản chọn, qua mục 2–7, mỗi ảnh tự chấm M ≥ 8 và Q ≥ 8, điểm M chung của `118-mock.jpg` ≥ 8. Loại nào không đạt sau 3 lượt thì giữ bản tốt nhất, ghi rõ chỗ thiếu.
