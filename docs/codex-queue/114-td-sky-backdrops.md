# Phiếu 114 · Wordwoven · Trời và phông xa sử thi cho map 1 3D (9 ảnh)

**Nguồn:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md`, bible Wordwoven; thứ tự 2). Bộ `backdrops/w1-silverfall/` cũ (cầu vồng, đồi chè, cối xay gió) chấm 4–4,5/10 theo mức chợ và được thay bằng bộ mới cùng luật ghép vòng.

**Báo cáo:** `docs/codex-queue/114-report.md`.

**Thứ tự:** sau 113.

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận mới:** ảnh được chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp`. Lấy mức chi tiết, ánh sáng, chiều sâu và cảm giác quy mô; không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ (tách nền, làm khớp mép, chỉnh màu) thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/114/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn (kể cả cả bộ `backdrops/w1-silverfall/`); xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, chữ ký, khung, viền trong ảnh. (Ảnh này không có chữ; nếu có biển hay chữ thì phải là tiếng Anh, nhưng phiếu này không cần chữ nào.)
- **KA1 md5:** `md5 -r` mọi file trong `games/typing-defense/art-src/backdrops/` (đệ quy) trước khi ghi (`_review/114/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, mức chợ, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: có mốc lớn làm người chơi nhỏ lại, ít nhất ba lớp sâu (gần, giữa, xa) và trời, ánh sáng có hướng, màu theo kịch bản, chi tiết hoàn thiện. 7 là game indie dễ chịu, nhưng quy mô và ánh sáng thường. 6 là gọn mà chung chung, ánh sáng phẳng. 5 là tranh đẹp nhưng sai tầm (ấm cúng, quê, nhỏ). 4 là hình phẳng kiểu clip-art. Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2, mỗi tiêu chí 0–2.
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**. Ô phông là một phần của vòng: M chấm trên ảnh ghép (mục Kiểm 7); Q chấm từng ô.
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8.

## Phiếu

**Vì sao và dùng ở đâu:** map 1 (`w1-silverfall`) lên 3D (bước 1C, làn L, C9). Phông xa là ba vòng trụ quanh sân ở 140, 220 và 320 m, thêm vòm trời. Mỗi ảnh là một phần tư vòng; mỗi vòng có 4 ô. Ô điểm nhấn (`-a`) đặt một lần, ô trơn đặt ở các chỗ còn lại, lật ngang xen kẽ (cách cũ của `03-2d-scenery-ui-vfx.md` §6).
- Camera mặc định (55° ở 58 m, FOV 38°) không thấy chân trời. Phông hiện khi người chơi nghiêng camera thấp (30–40°), khi zoom xa, và ở camera màn tựa. Lúc đó phông phải hùng vĩ: tháp đá vôi cao hàng trăm mét, thác bạc, đền đá cổ, quái thú trời.
- Quái thú trời là một tấm riêng có alpha. Game cho nó bay chậm dọc vòng trời, và đổ bóng mờ qua sân (dùng ảnh nhìn từ trên). Ở camera nhìn xuống, cái bóng khổng lồ trôi qua sân là cách rẻ nhất cho người chơi thấy quy mô.
- Model 3D (nhà, quái, Draconis) giữ nguyên. Làn L chỉnh ánh sáng cho chúng theo bible; phông phải cùng hướng nắng và cùng màu sương để hai thứ sống chung.

**Nơi ghi:** `games/typing-defense/art-src/backdrops/w1-silverfall-epic/` (thư mục mới).

**Chỉ được ghi:**
- `backdrops/w1-silverfall-epic/<tên>.tryN.png`, `.tryN.prompt.txt`, bản chọn `<tên>.png`, `<tên>.prompt.txt`, `<tên>.alpha.png`;
- `games/typing-defense/art-src/_review/114-*.jpg`, `games/typing-defense/art-src/_review/114/`;
- `docs/codex-queue/114-report.md`.

**Đọc trước (chỉ đọc):** ảnh tham chiếu; bộ cũ `backdrops/w1-silverfall/*.prompt.txt` (luật mép vẫn dùng); `games/typing-defense/docs/art-requests/td/03-2d-scenery-ui-vfx.md` §3.3, §3.8, §6; màn tựa mới của phiếu 113 nếu đã có (`ui/title-epic/title-backdrop.png`), để cùng màu.

### Khối prompt (nguyên văn)

Ghép prompt:
- ô trời: **STYLE** + **SKY** + phần riêng;
- ô núi: **STYLE** + **RING** + phần riêng + dòng nền M;
- quái thú trời: **STYLE** + phần riêng + dòng nền M.

**STYLE**
```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.
```

**SKY**
```text
Sky band of a 360-degree backdrop for a 3D game, one quarter of the ring, viewed straight ahead at a level horizon. No land, no hills, no towers, no birds, no beasts and no sun disc. The bottom 20% of the image fades into a flat haze of one colour. The left 8% and the right 8% are plain open sky with the same colour at every height on both sides, and no cloud touches or crosses the left or right edge, so tiles join side by side and when mirrored. Landscape 1536 x 1024.
```

**RING**
```text
Backdrop tile for a 3D game: one wide strip of distant scenery that wraps around the play area as one quarter of a ring, viewed straight ahead at a level horizon: no tilt, no fisheye, no perspective lines. Light comes from above and slightly behind the viewer, so both side edges are lit the same: warm gold light on the tops and faces of the towers, cool jade-teal shade low down, a soft rim of light along the skyline, no cast shadow pointing left or right. Farther parts are paler, bluer and softer through atmospheric haze and drifting mist below the skyline. The top edge of the land against the background is one crisp, solid line: no mist, haze or cloud crosses it. No people and no animals. The left 8% and the right 8% of the image are calm and plain, and the skyline meets both side edges at exactly the height given in the item, so tiles join side by side and also when mirrored. Landscape 1536 x 1024.
```

**Dòng nền M** (dán cuối prompt): `Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.`

**SAME** (dán trước dòng nền của `sky-beast-top`): `Same creature as the attached image: identical body, shell, ruins, colours and proportions. Change only the view, as described.`

### Chín ảnh

| Tên | Đặt ở đâu | Nền | Phần riêng của prompt |
|---|---|---|---|
| `sky-day-a` | vòm trời, 1 lần | đặc | `Late afternoon over the karst realm: deep blue at the top edge, towering golden cumulus clouds with sunlit tops and soft lavender-teal undersides, fans of sun rays breaking down from behind the clouds near the centre, high thin cirrus; the bottom haze is pale gold-white.` |
| `sky-day-b` | vòm trời, 3 lần, lật xen kẽ | đặc | `Late afternoon over the karst realm: deep blue at the top edge, scattered golden cumulus clouds of different sizes with soft lavender-teal undersides, high thin cirrus, no sun rays; the bottom haze is pale gold-white.` Đính kèm `sky-day-a` với dòng `Use the attached image only to match the style, colours and light. Paint a different sky as described.` |
| `sky-night` | vòm trời ban đêm (Đêm 1–5) | đặc | `Night of the lantern festival: a deep indigo sky, a large pale moon half hidden behind silver-edged clouds, a soft milky way, and hundreds of small warm amber floating lanterns rising in drifting streams, many low and fewer high; the bottom haze is dark teal.` |
| `layer-320` | vòng 320 m, 4 lần, lật xen kẽ | M | `Layer at 320 metres: a colossal far range of limestone karst towers in pale blue-grey, tall needle and dome shapes overlapping in three faint layers, the tallest tops reaching 15% from the top of the image, thin mist bands between them below the skyline. The skyline meets both side edges at exactly 60% from the top. Above the skyline the image is the flat background colour. Below, the towers fade into a flat pale blue-teal haze that is solid from 80% down to the bottom edge.` |
| `layer-220` | vòng 220 m, 4 lần, lật xen kẽ | M | `Layer at 220 metres: mid-distance karst towers with sheer pale cliffs and dark jade forest on their tops, two silver waterfalls falling from their cliffs into mist, rice terraces climbing one lower slope like giant green-and-gold stairs, the ruins of an ancient stone temple on one tower top. The skyline stays between 15% and 60% from the top, and meets both side edges at exactly 60%. Above the skyline the image is the flat background colour. Below, the towers fade into a flat blue-green haze that is solid from 80% down to the bottom edge.` |
| `layer-140-a` | vòng 140 m, 1 lần (hướng bắc, sau thác của map) | M | `Layer at 140 metres, the accent tile: a near karst wall with a colossal ancient stone gate carved into the rock, a long stairway climbing to it past rice terraces, a big silver waterfall falling beside the gate into mist, small amber lanterns along the stairway, jade forest on the ledges. The skyline stays between 10% and 62% from the top, and meets both side edges at exactly 62%. Above the skyline the image is the flat background colour. Below, everything fades into a flat soft jade haze that is solid from 85% down to the bottom edge.` |
| `layer-140-b` | vòng 140 m, 3 lần, lật xen kẽ | M | `Layer at 140 metres: near karst towers with jade forest on their tops and rice terraces on their lower slopes, a few lone pines on the ledges, one thin waterfall, no buildings. The skyline stays between 15% and 62% from the top, and meets both side edges at exactly 62%. Above the skyline the image is the flat background colour. Below, everything fades into a flat soft jade haze that is solid from 85% down to the bottom edge.` Đính kèm `layer-140-a` với dòng MATCH như `sky-day-b`. |
| `sky-beast` | tấm bay dọc vòng trời | M | `A colossal sky turtle inspired by the Golden Turtle of Vietnamese legend, seen from the side as it glides to the right: a vast domed shell carrying moss-covered stone temple ruins, small trees and hanging vines, long flowing fin-like flippers, ancient jade-and-bronze scales, mist trailing from its flippers. The whole body is inside the image with an empty margin on every side. Light from above and slightly behind the viewer, a soft warm rim along its back. Landscape 1536 x 1024.` |
| `sky-beast-top` | bóng trôi qua sân | M | `The same colossal sky turtle seen from directly above, flippers spread wide, the temple ruins and trees on its shell, whole body inside the image with an empty margin. Flat even light. Square 1024 x 1024.` Đính kèm `sky-beast` đã chọn với dòng SAME |

**Hậu kỳ:** ô núi và hai tấm quái thú tách nền bằng `tools/art-normalize/key-alpha.sh` (đọc README) thành `<tên>.alpha.png`, cùng khổ nguồn. Ô trời không cần alpha.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/typing-defense/art-src/backdrops/` (đệ quy).
2. **Khổ:** 1536 × 1024 cho tám ảnh; `sky-beast-top` 1024 × 1024. Khổ khác thì cắt giữa rồi thu bằng Lanczos; ghi lệnh.
3. **Nền sạch** (ô núi, quái thú): 10 px mép bốn phía là màu nền, mỗi kênh lệch ≤ 12; trong vật, px có hue trong ±12° của màu nền và S > 0,5 chiếm ≤ 0,5 %. Sau khi tách: alpha min 0, max 255; viền đường chân núi: số cột có dải alpha 0,05–0,95 dày hơn 3 px chiếm ≤ 5 %; không viền hồng ở phóng 4× (`_review/114-edge.jpg`).
4. **Mép ghép:**
   - ô núi: đường chân núi ở cột 0 và cột cuối nằm đúng độ cao của ô (60 % hay 62 %), lệch ≤ 1 % chiều cao; màu dưới chân núi ở hai mép lệch ≤ 8/255 mỗi kênh theo từng hàng (trung bình);
   - ô trời: dải 8 % trái và 8 % phải, lấy trung bình màu từng hàng, lệch ≤ 6/255; không mây chạm mép.
   Mép chưa khớp thì làm khớp bằng công cụ (pha hai dải mép bằng mặt nạ cosin) trước khi sinh lại; ghi số trước và sau.
5. **Thử vòng** `_review/114-ring.jpg`: mỗi vòng xếp ô, ô lật, ô, ô lật cạnh nhau (mỗi ô rộng 384 px); vòng 140 xếp `a`, `b` lật, `b`, `b` lật. Xem chỗ nối ở cỡ đầy đủ; ghi "không thấy đường nối" hay chỉ chỗ thấy.
6. **Đọc ở cỡ nhỏ:** ảnh ghép (mục 7) thu về 384 px rộng: còn nhận ra tháp đá, thác, cổng đá, quái thú không. Ghi từng ý.
7. **Ảnh ghép và tờ so:**
   - `_review/114-composite-day.jpg`: một khung 1536 × 1024 ghép `sky-day-a`, `sky-beast.alpha` (thu 45 %, giữa trên), `layer-320`, `layer-220`, `layer-140-a` theo alpha, từ xa tới gần;
   - `_review/114-composite-night.jpg`: cùng cách với `sky-night`; ba lớp núi nhân màu tối xanh (ví dụ ×0,45 với ánh lam), ghi công thức;
   - `_review/114-vs-ref.jpg`: hai ảnh ghép đặt cạnh ảnh tham chiếu, cùng cao 640 px; hàng dưới là ảnh ghép của bộ cũ `w1-silverfall` (`sky-a`, `layer-320`, `layer-220`, `layer-140-a`) cho thấy trước và sau. Dưới mỗi ảnh mới ghi một dòng: "đứng cạnh được" hay "chưa", và vì sao;
   - `_review/114-beast-shadow.jpg`: `sky-beast-top.alpha` thành bóng (đen 35 %, mờ 24 px) đặt trên một ảnh chụp sân 3D có sẵn, ví dụ `games/.wt-td-1c/tmp/lane-l/td-1c-ground-sheet-1920x1080.jpg` (chỉ đọc); xem bóng có đọc ra hình con rùa không.
8. **Màu tín hiệu:** 0 % px của vật có hue 285–330° và S > 0,5.
9. **KA5 mức chợ:** M trên hai ảnh ghép; Q cho từng ô, ở cỡ đầy đủ và ở 384 px.

**Xong khi:** chín ảnh có bản chọn, qua mục 2–5 và 8; ảnh ghép ngày và đêm tự chấm M ≥ 8; mỗi ô Q ≥ 8. Ô nào không đạt sau 3 lượt thì giữ bản tốt nhất, ghi rõ chỗ trượt và đề xuất cách khác.
