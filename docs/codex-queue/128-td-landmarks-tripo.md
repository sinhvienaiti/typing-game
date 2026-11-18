# Phiếu 128 · Wordwoven · Ảnh nguồn Tripo cho các mốc khổng lồ quanh sân (5 ảnh)

**Nguồn:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md`, bible Wordwoven; thứ tự 8). Ở camera mặc định (55° từ 58 m) người chơi không thấy chân trời, nên phông xa của 114 không đủ để sân trông hùng vĩ. Cần vài mốc khổng lồ đứng ngay mép sân (ngoài nửa cạnh 48 m), đủ cao để lọt vào khung từ trên xuống: tượng đá, cổng đá, tháp đá vôi. Phiếu này vẽ ảnh nguồn 2D để **chủ dự án dựng 3D trên Tripo** (bằng tay trên web). Codex chỉ vẽ ảnh nguồn; không gọi Tripo.

**Báo cáo:** `docs/codex-queue/128-report.md`.

**Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5: tờ "bản sinh | bản hậu kỳ" cho mỗi ảnh; công cụ không được xóa, san phẳng hay phủ phần vẽ; ngưỡng số mâu thuẫn với tranh thì dừng và ghi lại; tự chấm trên bản hậu kỳ.

**Thứ tự:** chỉ là thứ tự hàng đợi, không phải phụ thuộc nội dung. Chạy ngay, không chờ phiếu khác (Claude 29/10).

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận mới:** ảnh được chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp` (xem các công trình đổ nát trên vách xa: lớn, cổ, nhiều chi tiết). Không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ (tách nền, cắt, thêm lề) thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/128/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex; gọi Tripo, Meshy hay API 3D nào;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, khung trong ảnh; biển, bia không có chữ;
  - hình tôn giáo: không tượng thần, Phật, bàn thờ, lư hương, chuông chùa (luật TK §22.1 của game).
- **KA1 md5:** `md5 -r` mọi file trong `games/typing-defense/art-src/` (đệ quy) trước khi ghi (`_review/128/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, mức chợ, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: dáng lớn, cổ, hùng; chất liệu đá, đồng, gỗ thật; chi tiết hoàn thiện mà vẫn gom thành khối lớn. 7 là gọn nhưng thường. 5 là đúng vật nhưng sai tầm (đồ chơi, quê). Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2, mỗi tiêu chí 0–2. "Dùng tiếp" được 2 khi ảnh dựng 3D được (một khối liền, chân phẳng, góc nhìn đúng).
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**.
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8. Sau đó Claude gửi chủ dự án danh sách dựng Tripo.

## Phiếu

**Nơi ghi:** `games/typing-defense/art-src/landmarks-epic/` (thư mục mới).

**Chỉ được ghi:**
- `landmarks-epic/<tên>.tryN.png`, `.tryN.prompt.txt`, bản chọn `<tên>.png`, `<tên>.prompt.txt`;
- `games/typing-defense/art-src/_review/128-*.jpg`, `games/typing-defense/art-src/_review/128/`;
- `docs/codex-queue/128-report.md`.

**Đọc trước (chỉ đọc):** ảnh tham chiếu; prompt Tripo đã dùng của game `games/typing-defense/art-src/buildings/keep.prompt.txt` (giữ phần Camera, base, light, build); `games/typing-defense/docs/art-requests/td/02-tripo-buildings-props.md` §3.1, §3.5, §3.7; tờ model `games/.wt-td-1c/tmp/lane-l/td-1c-models-sheet.jpg` (kiểu model đang có, khối chắc, màu vẽ tay); ảnh 113, 114 nếu đã có.

### Khối prompt (nguyên văn)

Mỗi prompt = **MODEL** + phần riêng + **TAIL** + dòng nền.

**MODEL**
```text
Single 3D-ready concept image of one landmark for an epic high-fantasy strategy game, Wordwoven, a majestic realm inspired by northern Vietnam, made as a premium hand-painted 3D game asset: thick sturdy proportions and a bold silhouette that still reads clearly from high above, so it sits with chunky stylized buildings, but grand, ancient and finely carved rather than cute or rustic. Materials: weathered pale limestone with grey seams and dark jade moss, aged bronze with green patina, gold-leaf trim worn thin, dark red lacquered timber, small cinnabar-red accents. Matte hand-painted colours with soft, simple shading.
```

**TAIL**
```text
Camera: front three-quarter view, the subject turned about 30 degrees so its front face and its right side both show, looking down from about 35 degrees above, near-orthographic with no perspective distortion. The whole subject is in frame from its base to its top, centred, with a small even margin; nothing is cropped. Its base is cut flat like a model standing on a table: no ground, grass, loose rocks, path or props around it, and no shadow under it. Flat, even front lighting: no cast shadows, no strong highlights, no rim light, no glow. No painted black outlines. One connected solid object: every part touches the main body and nothing floats; moss, vines and leaves grouped into a few big solid masses. No fire, smoke, particles, magic glow or light rays. No people, animals or creatures. No text, letters, numbers, logos or signatures. No frame, border or second view.
```

**Dòng nền:** vật có rêu xanh → nền M `Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.`; vật không có xanh lá → nền G `Flat pure #00FF00 green background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no green at all.` Ghi nền đã dùng.

### Năm ảnh (vuông, cạnh 1254 px)

| Tên | Cỡ thật | Phần riêng |
|---|---|---|
| `guardian-statue` | cao 22 m | `A colossal ancient stone statue of a guardian general of old Vietnam, standing on a square plinth, both hands resting on the hilt of a long sword planted point-down, carved lamellar armour and a crested helmet, face calm and stern, moss in the folds, one shoulder chipped by time.` |
| `stone-gate` | rộng 18 m, cao 16 m | `A colossal ceremonial gate of carved limestone with three arches, the middle one tallest, under curved tiled roofs with upturned corners, carved cloud scrolls and Dong Son sun-star rings on the pillars, vines hanging from one side.` |
| `lantern-tower` | cao 14 m | `A tall slender lantern tower of stacked limestone tiers, each tier holding four aged bronze lanterns (unlit), a small curved tiled roof on top, dragon-carved corner brackets.` |
| `karst-pillar` | cao 34 m | `A single limestone karst pillar: sheer pale fluted cliffs, a cap of dark jade forest on top, a small ancient pavilion with a curved tiled roof perched on the very top, a thin waterfall streak down one face, vines on the ledges.` |
| `dragon-stair` | rộng 8 m, cao 10 m | `An ancient carved stone stairway climbing a rock spur, with long undulating dragon balustrades in the style of the Ly dynasty on both sides, worn steps, moss in the joints, a small landing at the top.` |

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/typing-defense/art-src/` (đệ quy).
2. **Khổ:** vuông, cạnh 1254 px (công cụ trả khác thì cắt giữa rồi đổi cỡ, ghi lệnh).
3. **Nền sạch:** 10 px mép bốn phía là màu nền, mỗi kênh lệch ≤ 12; trong vật, px có hue trong ±12° của màu nền và S > 0,5 chiếm ≤ 0,5 %.
4. **Một vật, chân phẳng ở đáy:** tách nền (lệnh như phiếu 106 mục 4, ghi lệnh); đáy hộp bao cách mép dưới ≤ 12 % chiều cao; lề trái, phải, trên ≥ 3 %; đúng một vùng liền có diện tích > 1 % ảnh.
5. **Không chữ, không hình tôn giáo.**
6. **Tờ thang** `_review/128-scale.jpg`: năm bản chọn đã tách nền, đặt trên một vạch đất chung theo cỡ thật, cạnh `games/typing-defense/art-src/buildings/keep.png` thu về 8 m (Fort) và `units/linh-giao.png` thu về 1,8 m làm thước. Xem: mốc có làm Fort và lính nhỏ lại không, có hợp kiểu model đang có không.
7. **Tờ so với tham chiếu** `_review/128-vs-ref.jpg`: tờ thang cạnh ảnh tham chiếu, cùng cao 640 px; hàng dưới là một hàng của `td-1c-models-sheet.jpg`. Ghi một dòng: "đứng cạnh được" hay "chưa", và vì sao.
8. **KA5 mức chợ:** M và Q cho từng bản chọn, ở cỡ đầy đủ và ở 256 px.

**Xong khi:** năm ảnh có bản chọn, qua mục 2–5, mỗi ảnh tự chấm M ≥ 8 và Q ≥ 8. Ảnh nào không đạt sau 3 lượt thì giữ bản tốt nhất, ghi rõ chỗ thiếu. Việc dựng 3D (5 model Tripo) là của chủ dự án.
