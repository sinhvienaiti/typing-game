# Phiếu 124 · Dragonhold · Ảnh nguồn Tripo cho các mốc của ải: cổng, tường, tháp, tượng rồng (6 ảnh)

**Nguồn:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md`, bible Dragonhold; thứ tự 8). Cảnh map L2-cau chấm 6,5/10 theo mức chợ: sạch, đọc rõ, nhưng như một công viên xanh; không có ải, không có pháo đài, không có vật nào làm người chơi nhỏ lại. Phiếu này vẽ ảnh nguồn 2D để **chủ dự án dựng 3D trên Tripo** (bằng tay trên web). Codex chỉ vẽ ảnh nguồn; không gọi Tripo.

**Báo cáo:** `docs/codex-queue/124-report.md`.

**Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5: tờ "bản sinh | bản hậu kỳ" cho mỗi ảnh; công cụ không được xóa, san phẳng hay phủ phần vẽ; ngưỡng số mâu thuẫn với tranh thì dừng và ghi lại; tự chấm trên bản hậu kỳ.

**Thứ tự:** sau 123.

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận mới:** ảnh được chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp` (xem các công trình đổ nát ở cảnh xa: lớn, cũ, nhiều chi tiết). Không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ (tách nền, cắt, thêm lề) thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/124/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex; gọi Tripo, Meshy hay API 3D nào;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, khung trong ảnh; cờ và biển không có chữ hay hình hiệu.
- **KA1 md5:** `md5 -r` mọi file trong `games/dragon-hold/art-src/` (đệ quy) trước khi ghi (`_review/124/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, mức chợ, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: dáng lớn, cổ, hùng; chất liệu đá, sắt, gỗ thật; chi tiết hoàn thiện mà vẫn gom thành khối lớn. 7 là gọn nhưng thường. 5 là đúng vật nhưng sai tầm (đồ chơi, dễ thương). Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2, mỗi tiêu chí 0–2. "Dùng tiếp" được 2 khi ảnh dựng 3D được (một khối liền, chân phẳng, góc nhìn đúng).
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**.
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8. Sau đó Claude gửi chủ dự án danh sách dựng Tripo.

## Phiếu

**Nơi ghi:** `games/dragon-hold/art-src/landmarks/` (thư mục mới).

**Chỉ được ghi:**
- `landmarks/<tên>.tryN.png`, `.tryN.prompt.txt`, bản chọn `<tên>.png`, `<tên>.prompt.txt`;
- `games/dragon-hold/art-src/_review/124-*.jpg`, `games/dragon-hold/art-src/_review/124/`;
- `docs/codex-queue/124-report.md`.

**Đọc trước (chỉ đọc):** ảnh tham chiếu; prompt Tripo đã dùng của game: `games/dragon-hold/art-src/houses/herb-hut.prompt.txt`, `traps/spikes.prompt.txt` (giữ phần View, Framing, Light, Build); tờ model `games/.wt-dh-mappilot/tmp/map-pilot-a2/sheets/kit3-models-sheet.jpg` (kiểu vẽ tay của model đang có: vách đá, đèn, hàng rào); ảnh 119, 120 nếu đã có.

### Khối prompt (nguyên văn)

Mỗi prompt = **MODEL** + phần riêng + **TAIL** + dòng nền.

**MODEL**
```text
Image-to-3D source picture of ONE object for a stylized 3D fantasy strategy game; it will become a static 3D model. Stylized hand-painted 3D game art for Dragonhold, an epic mountain pass guarded by a fire dragon, like a premium hand-painted 3D game asset: weathered cream granite, dark forged iron, old timber and pine, hand-painted textures with visible brush strokes, big confident shapes with a few large details instead of many small ones, a silhouette that still reads from a high top-down camera, grand and ancient rather than cute; matte surfaces, no glossy shine.
```

**TAIL**
```text
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a model standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it. Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals. Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats. No text, letters, numbers, emblems, signature or watermark.
```

**Dòng nền:** vật không có xanh lá → nền G `Flat pure #00FF00 green background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no green at all.`; vật có rêu hay lá thông → nền M `Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.` Ghi nền đã dùng.

### Sáu ảnh (vuông, cạnh 1254 px như ảnh Tripo của game)

| Tên | Cỡ thật | Phần riêng |
|---|---|---|
| `hold-gate` | rộng 18 m, cao 16 m | `The Hold gate: a fortress gatehouse of big cream granite blocks spanning a road, a great round arch with a dark iron portcullis half raised, two square towers with crenellations on either side, carved dragon-head corbels under the battlements, two unlit iron braziers on the towers.` |
| `hold-wall` | dài 12 m, cao 10 m | `A straight segment of the fortress wall of the Hold: cream granite blocks, crenellations along the top, a walkway behind them, two buttresses; both short ends are cut flat and plain so segments can join in a line.` |
| `watchtower` | cao 14 m | `A tall round watchtower of cream granite with arrow slits, a wooden hoarding near the top, a conical dark slate roof and an iron dragon-shaped weathervane.` |
| `dragon-statue` | cao 12 m | `A giant ancient statue of a dragon carved from weathered granite, seated upright on a square plinth, wings folded, head raised and facing forward, deep carved scales, a little dark moss in the carvings.` |
| `ruined-arch` | cao 8 m | `An old ruined arch of granite over a road: one side whole, the other side broken at half height, fallen blocks at its foot attached to the base, a few pine saplings growing from the cracks.` |
| `brazier` | cao 3 m | `A tall iron brazier on a square granite plinth: four forged dragon claws hold the bowl, unlit, a little soot on the rim.` |

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/dragon-hold/art-src/` (đệ quy).
2. **Khổ:** vuông, cạnh 1254 px (công cụ trả khác thì cắt giữa rồi đổi cỡ, ghi lệnh).
3. **Nền sạch:** 10 px mép bốn phía là màu nền, mỗi kênh lệch ≤ 12; trong vật, px có hue trong ±12° của màu nền và S > 0,5 chiếm ≤ 0,5 %.
4. **Một vật, chân phẳng ở đáy:** tách nền (lệnh như phiếu 106 mục 4, ghi lệnh); đáy hộp bao cách mép dưới ≤ 12 % chiều cao; lề trái, phải, trên ≥ 3 %; đúng một vùng liền có diện tích > 1 % ảnh.
5. **Màu tín hiệu:** px có hue 0–60° hoặc 160–200° với S > 0,6 và V > 0,7 chiếm ≤ 3 % vật.
6. **Không chữ, không hình hiệu** trên cờ, biển, khiên.
7. **Tờ thang** `_review/124-scale.jpg`: sáu bản chọn đã tách nền, đặt trên một vạch đất chung theo cỡ thật (cột Cỡ thật), cạnh `games/dragon-hold/art-src/enemies/moss-grunt.png` thu về 1,8 m làm thước. Xem: mốc có làm lính nhỏ lại không.
8. **Tờ so với tham chiếu** `_review/124-vs-ref.jpg`: tờ thang cạnh ảnh tham chiếu, cùng cao 640 px; hàng dưới là tờ model `kit3-models-sheet.jpg` cắt một hàng, để thấy kiểu vẽ có hợp model đang có không. Ghi một dòng: "đứng cạnh được" hay "chưa", và vì sao.
9. **KA5 mức chợ:** M và Q cho từng bản chọn, ở cỡ đầy đủ và ở 256 px.

**Xong khi:** sáu ảnh có bản chọn, qua mục 2–6, mỗi ảnh tự chấm M ≥ 8 và Q ≥ 8. Ảnh nào không đạt sau 3 lượt thì giữ bản tốt nhất, ghi rõ chỗ thiếu. Việc dựng 3D (6 model Tripo) là của chủ dự án.
