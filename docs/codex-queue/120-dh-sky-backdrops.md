# Phiếu 120 · Dragonhold · Trời và phông xa của ải rồng (6 ảnh)

**Nguồn:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md`, bible Dragonhold; thứ tự 6). Phông cũ `backdrops/pine-river-far*.png` (đồi thông sương, trời kem) chấm 5,5/10 theo mức chợ: dịu, đẹp, nhưng không có ải, không có vách lớn, không có mốc nào. Bộ mới là một ải núi có pháo đài.

**Báo cáo:** `docs/codex-queue/120-report.md`.

**Thứ tự:** sau 119.

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận mới:** ảnh được chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp`. Lấy mức chi tiết, ánh sáng, chiều sâu và cảm giác quy mô; không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ (tách nền, làm khớp mép, chỉnh màu) thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/120/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn (kể cả `backdrops/pine-river-far*`); xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, chữ ký, khung, viền trong ảnh. (Phiếu này không cần chữ; nếu có biển thì phải là tiếng Anh.)
- **KA1 md5:** `md5 -r` mọi file trong `games/dragon-hold/art-src/backdrops/` (đệ quy) trước khi ghi (`_review/120/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, mức chợ, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: có mốc lớn làm người chơi nhỏ lại, ít nhất ba lớp sâu (gần, giữa, xa) và trời, ánh sáng có hướng, màu theo kịch bản, chi tiết hoàn thiện. 7 là game indie dễ chịu, nhưng quy mô và ánh sáng thường. 6 là gọn mà chung chung, ánh sáng phẳng. 5 là tranh đẹp nhưng sai tầm. 4 là hình phẳng kiểu clip-art. Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2, mỗi tiêu chí 0–2.
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**. Ô phông là một phần của vòng: M chấm trên ảnh ghép (mục Kiểm 7); Q chấm từng ô.
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8.

## Phiếu

**Vì sao và dùng ở đâu:** trong trận, camera Dragonhold nghiêng 40–75° nên không thấy trời. Phông này dùng ở:
- camera màn tựa: hạ thấp 12–20°, quay chậm quanh map thật, thấy ải, vách và trời phía sau (DH-13);
- màn kết quả, màn tải, và lúc zoom xa hết cỡ.
Vòng trụ như Wordwoven: mỗi ảnh là một phần tư vòng, đặt ở 170, 260 và 380 m (làn R chốt số); ô điểm nhấn (`-a`) một lần, ô trơn lật ngang xen kẽ.

**Nơi ghi:** `games/dragon-hold/art-src/backdrops/pass-epic/` (thư mục mới).

**Chỉ được ghi:**
- `backdrops/pass-epic/<tên>.tryN.png`, `.tryN.prompt.txt`, bản chọn `<tên>.png`, `<tên>.prompt.txt`, `<tên>.alpha.png`;
- `games/dragon-hold/art-src/_review/120-*.jpg`, `games/dragon-hold/art-src/_review/120/`;
- `docs/codex-queue/120-report.md`.

**Đọc trước (chỉ đọc):** ảnh tham chiếu; `backdrops/pine-river-far-015.prompt.txt` (luật mép cũ); ảnh của phiếu 119 (`ui/title-epic/title-backdrop.png`, `keyart.png`) nếu đã có, để cùng màu và nắng; cảnh map `games/.wt-dh-mappilot/tmp/map-pilot-a2/sheets/a2-1920x1080-default-compare.jpg`.

### Khối prompt (nguyên văn)

Ghép prompt: ô trời = **STYLE** + **SKY** + phần riêng; ô núi = **STYLE** + **RING** + phần riêng + dòng nền M.

**STYLE**
```text
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
```

**SKY**
```text
Sky band of a 360-degree backdrop for a 3D game, one quarter of the ring, viewed straight ahead at a level horizon. No land, no mountains, no birds, no dragons and no sun disc. The bottom 20% of the image fades into a flat haze of one colour. The left 8% and the right 8% are plain open sky with the same colour at every height on both sides, and no cloud touches or crosses the left or right edge, so tiles join side by side and when mirrored. Landscape 1536 x 1024.
```

**RING**
```text
Backdrop tile for a 3D game: one wide strip of distant scenery that wraps around the play area as one quarter of a ring, viewed straight ahead at a level horizon: no tilt, no fisheye, no perspective lines. Dawn light comes from above and slightly behind the viewer, so both side edges are lit the same: warm gold on the peaks and cliff faces, cool slate-blue shade low down, a soft rim of light along the skyline, no cast shadow pointing left or right. Farther parts are paler, bluer and softer through haze, with mist pooling below the skyline. The top edge of the land against the background is one crisp, solid line: no mist, haze or cloud crosses it. No people and no animals. The left 8% and the right 8% of the image are calm and plain, and the skyline meets both side edges at exactly the height given in the item, so tiles join side by side and also when mirrored. Landscape 1536 x 1024.
```

**Dòng nền M:** `Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.`

**MATCH** (ô thứ hai của cùng loại): `Use the attached image only to match the style, colours, outline and light. Paint a different tile as described.`

### Sáu ảnh

| Tên | Đặt ở đâu | Nền | Phần riêng của prompt |
|---|---|---|---|
| `sky-dawn-a` | vòm trời, 1 lần (phía mặt trời mọc) | đặc | `Dawn over the mountains: deep slate-blue at the top edge, long bands of cloud lit gold and ember-orange from below, a bright warm glow low in the centre where the sun is about to rise, fans of faint god rays; the bottom haze is pale gold.` |
| `sky-dawn-b` | vòm trời, 3 lần, lật xen kẽ | đặc | `Early morning over the mountains: deep slate-blue at the top edge fading to pale gold lower down, scattered long clouds with gold-lit undersides, no glow in the centre; the bottom haze is pale gold.` Đính kèm `sky-dawn-a` với dòng MATCH |
| `layer-far` | vòng 380 m, 4 lần, lật xen kẽ | M | `Layer at 380 metres: a colossal far range of snow-capped granite peaks in pale blue-grey, sharp summits catching the first gold light, two or three overlapping layers, the tallest summit reaching 12% from the top of the image, thin mist below the skyline. The skyline meets both side edges at exactly 58% from the top. Above the skyline the image is the flat background colour. Below, the peaks fade into a flat pale slate-blue haze that is solid from 80% down to the bottom edge.` |
| `layer-mid` | vòng 260 m, 4 lần, lật xen kẽ | M | `Layer at 260 metres: sheer granite cliffs and buttresses with dark pine forest on their ledges, one cliff face carved into a giant ancient dragon statue with folded wings, a tall thin waterfall falling into mist. The skyline stays between 12% and 60% from the top, and meets both side edges at exactly 60%. Above the skyline the image is the flat background colour. Below, everything fades into a flat blue-green haze that is solid from 80% down to the bottom edge.` |
| `layer-near-a` | vòng 170 m, 1 lần (đầu ải, sau Dragon Platform) | M | `Layer at 170 metres, the accent tile: the Hold, an ancient fortress wall of cream granite with square towers and a great arched gate built across the pass between two colossal cliffs, iron braziers glowing on the battlements, banners without any emblem or letters, dark pines at the foot of the wall. The skyline stays between 10% and 62% from the top, and meets both side edges at exactly 62%. Above the skyline the image is the flat background colour. Below, everything fades into a flat deep pine-green haze that is solid from 85% down to the bottom edge.` |
| `layer-near-b` | vòng 170 m, 3 lần, lật xen kẽ | M | `Layer at 170 metres: steep granite slopes covered in dark pine forest, a few bare rock spurs, mist in the gullies, no buildings. The skyline stays between 15% and 62% from the top, and meets both side edges at exactly 62%. Above the skyline the image is the flat background colour. Below, everything fades into a flat deep pine-green haze that is solid from 85% down to the bottom edge.` Đính kèm `layer-near-a` với dòng MATCH |

**Hậu kỳ:** bốn ô núi tách nền bằng `tools/art-normalize/key-alpha.sh` (đọc README) thành `<tên>.alpha.png`, cùng khổ nguồn. Ô trời không cần alpha.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/dragon-hold/art-src/backdrops/` (đệ quy).
2. **Khổ:** 1536 × 1024 cho cả sáu. Khổ khác thì cắt giữa rồi thu bằng Lanczos; ghi lệnh.
3. **Nền sạch** (ô núi): 10 px mép bốn phía là màu nền, mỗi kênh lệch ≤ 12; trong vật, px có hue trong ±12° của màu nền và S > 0,5 chiếm ≤ 0,5 %. Sau khi tách: alpha min 0, max 255; số cột có dải alpha 0,05–0,95 dày hơn 3 px ở đường chân núi chiếm ≤ 5 %; không viền hồng ở phóng 4× (`_review/120-edge.jpg`).
4. **Mép ghép:** ô núi: đường chân núi ở cột 0 và cột cuối đúng độ cao của ô (58, 60 hay 62 %), lệch ≤ 1 % chiều cao; màu dưới chân núi ở hai mép lệch ≤ 8/255 mỗi kênh (trung bình theo hàng). Ô trời: dải 8 % trái và phải, trung bình từng hàng, lệch ≤ 6/255; không mây chạm mép. Mép chưa khớp thì làm khớp bằng công cụ (pha hai dải mép bằng mặt nạ cosin) trước khi sinh lại; ghi số trước và sau.
5. **Thử vòng** `_review/120-ring.jpg`: mỗi vòng xếp ô, ô lật, ô, ô lật (mỗi ô rộng 384 px); vòng 170 xếp `a`, `b` lật, `b`, `b` lật. Ghi "không thấy đường nối" hay chỉ chỗ thấy.
6. **Đọc ở cỡ nhỏ:** ảnh ghép (mục 7) thu về 384 px rộng: nhận ra tường ải và cổng, tượng rồng, đỉnh tuyết không. Ghi từng ý.
7. **Ảnh ghép và tờ so:**
   - `_review/120-composite.jpg`: một khung 1536 × 1024 ghép `sky-dawn-a`, `layer-far`, `layer-mid`, `layer-near-a` theo alpha, từ xa tới gần;
   - `_review/120-vs-ref.jpg`: ảnh ghép đặt cạnh ảnh tham chiếu, cùng cao 640 px; hàng dưới là `backdrops/pine-river-far-015.png` cũ cho thấy trước và sau. Ghi một dòng: "đứng cạnh được" hay "chưa", và vì sao.
8. **Màu tín hiệu:** 0 % px của vật có hue 285–330° và S > 0,5.
9. **KA5 mức chợ:** M trên ảnh ghép; Q cho từng ô, ở cỡ đầy đủ và ở 384 px.

**Xong khi:** sáu ảnh có bản chọn, qua mục 2–5 và 8; ảnh ghép tự chấm M ≥ 8; mỗi ô Q ≥ 8. Ô nào không đạt sau 3 lượt thì giữ bản tốt nhất, ghi rõ chỗ trượt và đề xuất cách khác.
