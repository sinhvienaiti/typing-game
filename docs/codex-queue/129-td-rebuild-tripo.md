# Phiếu 129 · Wordwoven · Ảnh nguồn Tripo để dựng lại sáu công trình mái tranh (6 ảnh) · chỉ chạy khi chủ dự án đồng ý dựng lại

**Nguồn:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md`, mục "Model phải dựng lại"). Chủ dự án giữ toàn bộ model của Wordwoven và cho chỉnh ánh sáng; model lệch hẳn hướng sử thi thì ghi lại để dựng sau. Sáu công trình dưới đây có mái tranh rơm, vách tre, chòi gỗ: đúng cái "thôn quê" chủ dự án chê. Phiếu vẽ bản mới cùng chức năng, cùng chân đế và cùng chỗ socket, bằng đá vôi, ngói, đồng.

**Chỉ chạy khi chủ dự án đồng ý dựng lại trên Tripo** (6 model dựng tay trên web, P2). Cho tới lúc đó phiếu nằm chờ; làn L chỉnh ánh sáng model cũ (bible §Wordwoven, cách chỉnh ánh sáng).

**Báo cáo:** `docs/codex-queue/129-report.md`.

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận mới:** ảnh được chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp` (xem các công trình trên vách xa: cổ, nhiều chi tiết). Không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ (tách nền, cắt, thêm lề) thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/129/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex; gọi Tripo, Meshy hay API 3D nào;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, khung trong ảnh; biển, bia không có chữ;
  - hình tôn giáo: không tượng thần, Phật, bàn thờ, lư hương, chuông chùa (luật TK §22.1 của game).
- **KA1 md5:** `md5 -r` mọi file trong `games/typing-defense/art-src/` (đệ quy) trước khi ghi (`_review/129/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, mức chợ, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: dáng chắc, cổ, sang; chất liệu đá, đồng, gỗ thật; chi tiết hoàn thiện mà vẫn gom thành khối lớn. 7 là gọn nhưng thường. 5 là đúng vật nhưng sai tầm (đồ chơi, quê). Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2, mỗi tiêu chí 0–2. "Dùng tiếp" được 2 khi ảnh dựng 3D được (một khối liền, chân phẳng, góc nhìn đúng).
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**.
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8. Sau đó Claude gửi chủ dự án danh sách dựng Tripo.

## Phiếu

**Nơi ghi:** `games/typing-defense/art-src/buildings-epic/` (thư mục mới).

**Chỉ được ghi:**
- `buildings-epic/<tên>.tryN.png`, `.tryN.prompt.txt`, bản chọn `<tên>.png`, `<tên>.prompt.txt`;
- `games/typing-defense/art-src/_review/129-*.jpg`, `games/typing-defense/art-src/_review/129/`;
- `docs/codex-queue/129-report.md`.

**Đọc trước (chỉ đọc):** ảnh tham chiếu; ảnh và prompt cũ của từng công trình (cột Bản cũ); `games/typing-defense/docs/art-requests/td/02-tripo-buildings-props.md` §3.1–§3.7 (góc nhìn, vòng chiếm chỗ và chiều cao, socket, bộ cấp, bảng kiểm); tờ model `games/.wt-td-1c/tmp/lane-l/td-1c-models-sheet.jpg` (kiểu model đang có, khối chắc, màu vẽ tay); ảnh 113, 114 nếu đã có.

### Khối prompt (nguyên văn)

Mỗi prompt = **MODEL** + phần riêng + **TAIL** + dòng nền.

**MODEL**
```text
Single 3D-ready concept image of one game building for an epic high-fantasy strategy game, Wordwoven, a majestic realm inspired by northern Vietnam, made as a premium hand-painted 3D game asset: thick sturdy proportions and a bold silhouette that still reads clearly from high above, so it sits with chunky stylized buildings, but grand, ancient and finely carved rather than cute or rustic. Materials: weathered pale limestone with grey seams and dark jade moss, aged bronze with green patina, gold-leaf trim worn thin, dark red lacquered timber, small cinnabar-red accents. Matte hand-painted colours with soft, simple shading.
```

**TAIL**
```text
Camera: front three-quarter view, the subject turned about 30 degrees so its front face and its right side both show, looking down from about 35 degrees above, near-orthographic with no perspective distortion. The whole subject is in frame from its base to its top, centred, with a small even margin; nothing is cropped. Its base is cut flat like a model standing on a table: no ground, grass, loose rocks, path or props around it, and no shadow under it. Flat, even front lighting: no cast shadows, no strong highlights, no rim light, no glow. No painted black outlines. One connected solid object: every part touches the main body and nothing floats; moss, vines and leaves grouped into a few big solid masses. No fire, smoke, particles, magic glow or light rays. No people, animals or creatures. No text, letters, numbers, logos or signatures. No frame, border or second view.
```

**Dòng nền:** vật có rêu xanh → nền M `Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.`; vật không có xanh lá → nền G `Flat pure #00FF00 green background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no green at all.` Ghi nền đã dùng.

### Sáu ảnh (vuông, cạnh 1254 px)

Mỗi ảnh đính kèm ảnh cũ với dòng **BUILDREF2**: `The attached image shows the old version of this building. Keep its footprint, height, front face, door position, assist platform at the front right and the open spots for its fittings; replace its thatch, bamboo and rustic timber with the materials described.`

| Tên | Bản cũ | Cỡ (§3.2) | Phần riêng |
|---|---|---|---|
| `archer` | `buildings/archer.png` | S, cao 6–7 m | `Archer Tower: a slender square tower of carved limestone with arrow slits, a timber gallery at the top under a curved dark-red tiled roof with upturned corners, bronze corner caps, a small banner pole without any emblem.` |
| `barracks` | `buildings/barracks-v2.png` | M, cao 4,5–5 m | `Barracks: a sturdy hall of limestone blocks and dark red lacquered timber under a double curved tiled roof, a wide gate with bronze studs, a rack of spears built into the side wall, a war drum on a stone stand by the gate.` |
| `lumber` | `buildings/lumber.png` | L, cao 5–6 m | `Lumber Camp: a timber workshop on a limestone base under a long curved tiled roof, a big saw frame of dark timber with bronze fittings, neat stacks of logs bound with bronze bands.` |
| `infirmary` | `buildings/infirmary.png` | M, cao 5–6 m | `Herb House: a round limestone pavilion with a curved tiled roof, carved herb and cloud patterns on its pillars, bronze medicine jars along the wall, bundles of dried herbs under the eaves.` |
| `farm` | `buildings/farm.png` | XL, đỉnh chòi khoảng 5 m | `Rice Field: a terraced paddy edged with fitted limestone walls, still silver water and green rice, a small watch pavilion of limestone and dark timber with a curved tiled roof at one corner, a stone water channel.` |
| `lookout` | `landmarks/choi-canh-doi.png` | mốc, cao 8–10 m | `Lookout: a tall stone watch pavilion on a limestone base with a stairway, a timber gallery under a curved tiled roof, bronze lantern hooks (no lanterns).` |

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/typing-defense/art-src/` (đệ quy).
2. **Khổ:** vuông, cạnh 1254 px (công cụ trả khác thì cắt giữa rồi đổi cỡ, ghi lệnh).
3. **Nền sạch:** 10 px mép bốn phía là màu nền, mỗi kênh lệch ≤ 12; trong vật, px có hue trong ±12° của màu nền và S > 0,5 chiếm ≤ 0,5 %.
4. **Một vật, chân phẳng ở đáy:** tách nền (lệnh như phiếu 106 mục 4, ghi lệnh); đáy hộp bao cách mép dưới ≤ 12 % chiều cao; lề trái, phải, trên ≥ 3 %; đúng một vùng liền có diện tích > 1 % ảnh.
5. **Không chữ, không hình tôn giáo.**
6. **Tờ trước và sau** `_review/129-before-after.jpg`: mỗi công trình một hàng: ảnh cũ, ảnh mới, cùng cao 384 px; thêm `buildings/keep.png` (Fort) ở đầu tờ để so kiểu. Ghi: chân đế, chiều cao, mặt trước, bục trợ lực và chỗ socket có giữ đúng không (theo §3.3 của 02).
7. **Tờ so với tham chiếu** `_review/129-vs-ref.jpg`: tờ trước và sau cạnh ảnh tham chiếu, cùng cao 640 px; hàng dưới là một hàng của `td-1c-models-sheet.jpg`. Ghi một dòng: "đứng cạnh được" hay "chưa", và vì sao.
8. **KA5 mức chợ:** M và Q cho từng bản chọn, ở cỡ đầy đủ và ở 256 px.

**Xong khi:** sáu ảnh có bản chọn, qua mục 2–5, mỗi ảnh tự chấm M ≥ 8 và Q ≥ 8. Ảnh nào không đạt sau 3 lượt thì giữ bản tốt nhất, ghi rõ chỗ thiếu. Việc dựng 3D (6 model Tripo) là của chủ dự án; Claude chạy preset, socket và bộ cấp như các nhà cũ.
