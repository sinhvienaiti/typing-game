# Phiếu 196 · Dragonhold · Ổ icon và khung thanh HUD (8 ảnh: ô kỹ năng, ô vật phẩm, ổ icon, ổ sao, khung máu và Rage)

**Nguồn:**
- Người chấm J2, gợi ý còn mở (`docs/HANDOFF_CURRENT.md` §3; `docs/codex-queue/accept-29-10/verdict.md`, mục "Ba lo ngại", ý 3): "Ảnh mẫu đặt icon trong ổ tròn kim loại … Nên làm ổ icon trong bộ khung UI Dragonhold và nâng cỡ tối thiểu lên khoảng 20 px".
- Kiểm kê UI 29/10 (`docs/games/map1/UI_IMAGERY.md`): DH-20 thanh máu, "khung thanh vẽ" (AD); DH-24 Dragon Rage, "khung thanh: AD"; DH-21 đến DH-23, DH-25 ô kỹ năng và ô đồ tiêu hao; DH-37 ô món ở cửa hàng.
- Chấm nhận lô 2 (`docs/codex-queue/accept-29-10b/verdict.md`, mục 140): "`star-unlit` đặt trong ổ sao trên nền tối".
- Chủ dự án 28/10 tối: mọi chi tiết UI có hình thật; không hình vẽ bằng mã. Chủ dự án 29/10: "tăng thêm việc cho codex".

**Báo cáo:** `docs/codex-queue/196-report.md` (tiếng Việt), thư mục `docs/codex-queue/196/`.

**Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5: tờ "bản sinh | bản hậu kỳ" cho mỗi ảnh; công cụ không được xóa, san phẳng hay phủ phần vẽ; ngưỡng số mâu thuẫn với tranh thì dừng và ghi lại; tự chấm trên bản hậu kỳ.

**Không trùng:** 162 (khung, bảng, nút; không có ổ hay thanh), 146 (mặt phím, đế thẻ chữ, huy hiệu, chấm cấp), 137–140 và 180 (icon). Phiếu này chỉ làm phần **chứa** icon và thanh.

**Sau phiếu này:** phiếu 194 chỉ thay SVG bằng ảnh icon, chưa có ổ. Một phiếu gắn sau 194 (chưa viết) đặt icon vào các ổ này và đọc file `.json`.

## Nơi làm và luật chung (phiếu ảnh)

- **Nơi làm:** repo cha `/Users/toandx/htdocs/typing-game` (thư mục làn `.`). Ảnh là media, không vào Git.
- **Chỉ được ghi:**
  - `games/dragon-hold/art-src/ui/sockets/` (thư mục mới);
  - `games/dragon-hold/art-src/_review/196-*.jpg` và `games/dragon-hold/art-src/_review/196/`;
  - `docs/codex-queue/196-report.md` và `docs/codex-queue/196/`.
- **Tối đa 3 lượt sinh mỗi ảnh.** Lượt sửa ảnh (đính kèm ảnh, dòng SAME) cũng tính là một lượt. Mỗi lượt sửa prompt đúng chỗ thiếu.
- **Mọi lượt** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Mức nhận:** M ≥ 8 theo game thương mại (`docs/games/ART_DIRECTION_2026-10-28.md` §1.3) và Q ≥ 8 (`docs/games/ART_ACCEPTANCE.md` §2.2: Đúng đề, Đọc được, Hợp bộ, Hình khối, Dùng tiếp, mỗi tiêu chí 0–2). "Dùng tiếp" chỉ được 2 khi mọi mục kiểm số đạt.
- **Không chữ, số, logo, chữ ký trong ảnh.** Chữ thử chỉ nằm trong tờ kiểm, và là tiếng Anh.
- **Script đã dùng** lưu ở `_review/196/`, có `README.md`, chạy lại được. Không giữ khung trung gian lớn; chỉ giữ tờ, số đo JSON và script.

## Đọc trước (chỉ đọc)

- `docs/codex-queue/115-td-ui-frames.md`: luật 9-slice, dòng nền M, dòng SAME, mục kiểm.
- `docs/codex-queue/162-dh-ui-frames.md`, `162-report.md` và `games/dragon-hold/art-src/ui/frames/*.json`: định dạng JSON (`size`, `slice`, `source`, `content`, `repeat`), cách giữ alpha ở độ phân giải gốc.
- `docs/codex-queue/146-report.md`: cách dẫn xuất `keycap-active` bằng lượt sửa ảnh, cách đo IoU cặp trạng thái.
- Ảnh tham chiếu của chủ dự án `games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp`: icon kỹ năng tròn trong vòng kim loại mảnh, nền ổ tối; thanh máu mảnh. Viền mảnh, icon gánh phần hình. Lấy mức hoàn thiện, không chép nội dung.
- Bộ khung 162 (`ui/frames/*.png`, tờ `_review/162-selected.jpg`): ổ phải cùng bộ (hoa cương kem, sắt rèn, vàng búa, đinh men than hồng).
- Icon để đặt vào ổ (`games/dragon-hold/art-src/ui/icons/`): 137 (`dragon-rage`, `chain`, `wave-horn`, `shield`), `armour.v2` (161, chưa nhận), 138, 139, 140 (`star-lit`, `star-unlit`, `stat-*`), cùng `gold`, `potion-small`, `skill-*`, món cửa hàng. Có bản `.v2` thì dùng `.v2`; ghi rõ dùng bản nào.
- Cỡ hiện tại trong game: `games/dragon-hold/src/ui/styles/dh.css` (`.dh-hp` dòng 449–503, `.dh-slot` 525–618, `.dh-rage` 620–655, `.dh-cell` 1009–1110). `--ui` là 0,8 ở 720p và 1,2 ở 1080p.

## Khối prompt (nguyên văn)

Mỗi prompt = **STYLE-UI** + phần riêng của ảnh + SOCKET hoặc BAR + dòng nền M. Prompt bằng tiếng Anh.

**STYLE-UI** (nguyên văn `ART_DIRECTION_2026-10-28.md` §3.2)
```text
Premium high-fantasy game interface art for Dragonhold, a mountain pass guarded by a fire dragon: weathered cream granite and dark forged iron, hammered gold trim, ember-orange enamel and glowing dragon-fire accents, carved dragon-scale and pine-bough ornament, small muted-violet accents. Crisp, finished and richly detailed like the interface of a top commercial fantasy strategy game, with clean bevels, soft inner shadow and a subtle warm rim light, readable at small size. Shown flat and straight on, no perspective, no scenery. No text, letters, numbers, signature or watermark.
```

**SOCKET** (dán sau phần riêng của bốn ổ)
```text
One interface socket, centred. A thin rim around a calm, empty, slightly recessed well where a small icon will sit later. The well holds nothing: no symbol, no gem, no glow, no pattern beyond faint material texture. The rim stays thin so the icon is the focus. Big simple shapes that still read at 24 pixels; no fine filigree.
```

**BAR** (dán sau phần riêng của hai thanh)
```text
One long horizontal bar frame, centred, filling about ninety percent of the width. All ornament sits in the two end caps; between them the rim is exactly the same all the way along, so the middle can be stretched. Inside runs one long, empty, dark recessed trough where a coloured fill will be drawn later. The trough holds nothing: no liquid, no glow, no colour fill, no marks, no dividers.
```

**Dòng nền M:** `Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.`
Tím xám của STYLE-UI lẫn vào nền khóa thì đổi ảnh đó sang nền G `#00FF00` (cùng câu, đổi màu), ghi lý do.

**SAME** (cho hai ảnh dẫn xuất): `Same object as the attached image: identical shape, size, position and colours. Change only what is described.`

## Tám ảnh

| Tên | Khổ giao | Cỡ trong game 720p / 1080p | Phần riêng (EN) |
|---|---|---|---|
| `skill-slot` | 1024 × 1024 | ô 37 / 55, icon 21 / 31 | `A square skill slot with softly rounded corners for a dragon's fire skills: a thin rim of dark forged iron edged with hammered gold, a tiny ember-orange enamel stud at each corner, faint carved dragon-scale texture on the rim; the well is dark forged iron with a soft inner shadow.` |
| `skill-slot-ready` | như trên | như trên | Dẫn xuất từ `skill-slot` đã chọn (đính kèm, dòng SAME): `The same skill slot, ready to use: the hammered-gold rim glows with warm ember light and a soft ember glow rises from the inner edge of the well; the centre of the well stays dark and empty.` |
| `item-cell` | 1024 × 1024 | ô 46 / 70, icon 32 / 48 | `A square item cell for a build shop: a thin rim of weathered cream granite with a fine hammered-gold inner line, small carved pine-bough ornaments at the four corners; the well is dark charcoal iron with a soft inner shadow.` |
| `item-cell-armed` | như trên | như trên | Dẫn xuất từ `item-cell` đã chọn (đính kèm, dòng SAME): `The same item cell, picked and waiting for confirmation: the hammered-gold inner line and the corner ornaments shine bright warm gold; the well stays dark and empty.` |
| `icon-socket` | 1024 × 1024 | ổ 22 / 32, icon 16 / 24; thử thêm ổ 28 / 40, icon 20 / 30 | `A small round socket for a tiny status icon: a thin ring of dark forged iron with a hammered-gold outer bevel and four tiny rivets; the well is a smooth dark iron dish with a soft inner shadow.` |
| `star-socket` | 1024 × 1024 | ổ 48 / 72, sao 37 / 55 | `A round socket for a result star: a ring of dark forged iron with a hammered-gold edge and one small ember-orange enamel stud at the top; the well is a recessed dish of weathered cream granite, so both a dark iron star and a gold star read on it.` |
| `hp-bar-frame` | 1536 × 512 | cao 22 / 32, máng ≥ 13 / 19 | `A health bar frame for the dragon, about a quarter of the image tall: end caps of cream granite and forged iron carved as small dragon-scale clasps, each set with an ember-orange enamel stone; a thin hammered-gold rim along the top and bottom edges.` |
| `rage-bar-frame` | 1536 × 512 | cao 14 / 20, máng ≥ 7 / 11 | `A slim rage meter frame, about a sixth of the image tall, slimmer and simpler than a health bar: forged iron end caps shaped like small flame-tongue clasps with ember-orange enamel; a thin hammered-gold rim along the edges.` |

Hai ảnh dẫn xuất **không sinh mới từ đầu**. Ánh sáng nằm trong dáng vật; quầng ngoài, nếu có, mỏng (≤ 3 % cạnh ảnh).

## Việc

1. **KA1 trước:** `md5 -r` mọi file trong `games/dragon-hold/art-src/ui/` (đệ quy), lưu `_review/196/md5-before.txt`.
2. **Sinh sáu ảnh gốc** theo bảng, rồi hai ảnh dẫn xuất từ bản chọn. Ghi số lần gọi công cụ mỗi ảnh.
3. **Tách nền:** thuật toán `tools/art-normalize/key-alpha.sh` (đọc README), như 162: global, protect-interior, no-key-hue. Thư mục làm việc trong `_review/196/`; không ghi vào công cụ chung. Ra `<tên>.alpha.png` ở **độ phân giải gốc** của lượt sinh.
4. **Bản `<tên>.png`:** thu Lanczos từ alpha gốc về khổ giao. Không cắt phần vẽ. Ảnh dẫn xuất lệch vị trí thì chỉ được dời và đổi cỡ cho khớp bản gốc.
5. **File `<tên>.json`** cho mọi ảnh, tọa độ tính trên `<tên>.alpha.png`:
   - chung: `size`, `source`, `content` `[x0, y0, x1, y1]` (bỏ lề trong suốt);
   - bốn ổ và hai ô: `well` `[x0, y0, x1, y1]`, `well_shape` (`"square"` hay `"circle"`), `icon_fit` (tỷ lệ cạnh icon trên cạnh ô, theo cột cỡ của bảng);
   - hai thanh: 3-slice `slice` `{ "left": L, "right": R, "top": 0, "bottom": 0 }`, `repeat` (`"stretch"` hay `"round"`), `trough` `[x0, y0, x1, y1]`, `trough_radius`. Đường cắt nằm ở mép trong của nắp; `L + R` nhỏ hơn bề rộng `content`;
   - ảnh dẫn xuất: cùng số với ảnh gốc, thêm `"derived_from"`.
6. **Dựng thử thanh** bằng ImageMagick: kéo đoạn giữa, giữ nguyên nắp.
   - `hp-bar-frame`: dài 220, 320, 480 ở cao 22 px; dài 330, 480, 720 ở cao 32 px.
   - `rage-bar-frame`: dài 120, 180, 260 ở cao 14 px; dài 180, 270, 390 ở cao 20 px.
   - Vẽ phần đầy thử vào máng (máu 62 % cam than hồng, Rage 40 %). Phần đầy chỉ có trong tờ kiểm, mô phỏng việc của mã.
7. **Đặt icon vào ổ** ở cỡ 720p và 1080p của bảng:
   - `skill-slot`: bốn `skill-*`; `skill-slot-ready` với `skill-fire-breath`;
   - `item-cell`: `spikes`, `pine-bomb`, `net-launcher`, `moss-warden`, `herb-hut`, `potion-small`, `dragon-heart`, `hard-scale`; `item-cell-armed` với `spikes`;
   - `icon-socket`: `dragon-rage`, `chain`, `wave-horn`, `gold`, `shield`, `armour`, `stat-accuracy`;
   - `star-socket`: `star-lit` và `star-unlit`.
8. **Mock HUD** `_review/196-mock.jpg`, 1280 × 720:
   - nền là một khung trận cắt từ `games/dragon-hold/tmp/map1-audit/sheets/sheet-08-feel-35wpm-1280-moments.jpg` (hay `sheet-02-keyboard-only-1280.jpg`), chỉ đọc;
   - `plate-long` của 162 làm đế; trên đó `hp-bar-frame` có phần đầy 62 % và chữ thử "1,240 / 2,000";
   - `rage-bar-frame` có phần đầy 40 %, bên trái `dragon-rage` trong `icon-socket`;
   - bốn `skill-slot` có icon kỹ năng (một ô là `skill-slot-ready`), hai ô đồ tiêu hao có `potion-small`;
   - dải cửa hàng tám `item-cell` có icon món (một ô là `item-cell-armed`);
   - chip đợt có `wave-horn` và `chain` trong `icon-socket`.
9. **Mock kết quả** `_review/196-results-mock.jpg`, 1280 × 720: nền cắt từ `sheet-09-feel-end-screens-1280.jpg`; `panel-large` của 162; ba `star-socket` (hai `star-lit`, một `star-unlit`); ba icon `stat-*` trong `icon-socket` ở 20 / 30 px. Chữ thử tiếng Anh ("Hold kept", "Accuracy 96%").
10. **Tờ so tham chiếu** `_review/196-vs-ref.jpg`: hai mock cạnh ảnh tham chiếu của chủ dự án, cùng cao 640 px. Ghi một dòng: "đứng cạnh được" hay "chưa", và vì sao.
11. **KA1 sau:** chạy lại md5, lưu `_review/196/md5-after.txt`, `diff` chỉ có dòng thêm, mọi dòng thêm nằm dưới `ui/sockets/`.

## Cấm

- Mọi lệnh git có ghi; sửa mã hay tài liệu (trừ báo cáo của phiếu).
- Ghi vào `public/`, `src/`, `games/dragon-hold/tmp/` hay ngoài repo.
- Ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`. Khung 162 và icon 137–140 chỉ đọc.
- Dev server, trình duyệt, mạng ngoài công cụ tạo ảnh.
- Đụng worktree `games/.wt-*`, game khác, Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`).
- Chữ, số, logo, chữ ký trong ảnh giao.
- Làm sáng, làm tối, phủ hay xóa phần vẽ để qua một ngưỡng số (§5). Chỉnh sáng toàn ảnh tối đa ±10 %.

## Kiểm (ghi số vào báo cáo)

1. **KA1 md5:** số dòng thêm, số dòng đổi hay mất (phải là 0).
2. **Khổ:** `magick identify -format '%f %wx%h %[channels]\n'` cho mọi file giao. `.png` đúng khổ bảng; `.alpha.png` là `srgba` ở khổ gốc.
3. **Alpha sạch:**
   - min 0, max 255;
   - ngoài dải mép 3 px quanh vật, alpha chỉ có 0 hay 255;
   - pixel alpha > 0 mang màu nền khóa (hue lệch ≤ 15°, S > 0,5) chiếm ≤ 0,2 %;
   - không viền hồng ở phóng 4× (`_review/196-edge.jpg`); đốm rời nhỏ hơn 20 px: 0.
4. **Cặp dẫn xuất** (`skill-slot` / `-ready`, `item-cell` / `-armed`):
   - IoU mặt nạ alpha > 16 ở 64 px ≥ 0,95;
   - hộp bao lệch ≤ 1 % cạnh ảnh;
   - luma trung bình của nửa giữa ổ (`well` thu 50 %) đổi ≤ 0,05 so với ảnh gốc, để ánh không phủ chỗ icon.
5. **JSON:** đủ tám file, đúng trường mục Việc 5; `well` và `trough` nằm trong `content`; máng cao ≥ 55 % `content` ở `hp-bar-frame`, ≥ 50 % ở `rage-bar-frame`.
6. **Đoạn giữa kéo được** (hai thanh): độ lệch chuẩn luma theo chiều kéo trong đoạn giữa; mục tiêu ≤ 0,05. Không đạt thì chọn lại đường cắt hay sinh lượt mới, không xóa vân. Vẫn không đạt thì ghi mâu thuẫn (§5).
7. **Tương phản icon trong ổ:** chênh luma (trung bình có trọng số alpha của icon, trung vị của `well`) cho từng cặp ở mục Việc 7. Mục tiêu ≥ 0,25; `star-unlit` trong `star-socket` bắt buộc ≥ 0,25. Ghi bảng; cặp nào dưới mức thì ghi, không sửa icon.
8. **Đọc ở 720p:** với từng ảnh, nhận ra không ở cỡ 720p (có, không, một dòng lý do). `icon-socket` ghi riêng hai cỡ 22 px và 28 px: cỡ nào đọc được icon.
9. **Tờ xem:**
   - `_review/196-raw-vs-final.jpg`: mỗi ảnh "bản sinh | bản hậu kỳ", cùng cỡ;
   - `_review/196-sheet.jpg`: hàng 1 tám bản chọn ở 256 px; hàng 2 cỡ 1080p có icon trên nền vỏ cây `#2b2118` và trên lòng `plate-long` của 162; hàng 3 như hàng 2 ở 720p; hàng 4 hai thanh ở ba độ dài có phần đầy thử; hàng 5 cạnh bốn khung 162 và một mảnh HUD của ảnh tham chiếu, cùng cao. Dưới mỗi ảnh ghi tên;
   - `_review/196-mock.jpg`, `196-results-mock.jpg`, `196-vs-ref.jpg` (mục Việc 8–10).
10. **KA5:** M và Q cho từng bản chọn, chấm trên bản hậu kỳ, ở cỡ gốc và cỡ 720p; M chung cho mỗi mock.

**Báo cáo** ghi: prompt đã sửa gì từng lượt; bảng số đo mục 1–8; điểm M và Q; đường dẫn các tờ; md5 của các file 162 đã dùng làm tham chiếu; chỗ nào làm khác phiếu và vì sao.

**Rủi ro:**
- Ngưỡng số có thể mâu thuẫn với tranh (đã gặp ở 146, 162, 180). Khi đó dừng, giữ tranh, ghi lại để Claude quyết.
- Khung 162 chưa được nhận. Nếu 162 làm lại, bộ này có thể phải theo; md5 ở báo cáo cho biết đã khớp bản nào.

**Xong khi:** tám ảnh có bản chọn, mọi `.tryN` và prompt, `.alpha.png` và `.json`; kiểm 1–10 có số; mỗi ảnh tự chấm M ≥ 8 và Q ≥ 8; hai mock M ≥ 8; có báo cáo. Ảnh nào sau 3 lượt chưa đạt thì giữ bản tốt nhất, ghi rõ chỗ thiếu. **Nhận** khi Claude chấm lại ≥ 8. Claude là người chép ảnh vào `public/` khi gắn.
