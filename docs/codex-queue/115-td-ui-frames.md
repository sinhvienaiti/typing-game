# Phiếu 115 · Wordwoven · Khung UI và bảng sử thi: ngọc, đá vôi, vàng lá (9 ảnh)

**Nguồn:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md`, bible Wordwoven; thứ tự 3). Thay phiếu 110 đã rút (khung gỗ tre và giấy, đúng lối "thôn quê" mà chủ dự án chê). HUD của Wordwoven hôm nay là bảng CSS giấy kem phẳng. Phiếu này chỉ làm **khung, bảng, nút, dải**. Icon và hình nhỏ của từng ô thuộc lượt rà hình UI (`docs/games/map1/UI_IMAGERY.md`, `UI_IMAGERY_CODEX.md`, khi có); phiếu này không làm lại các mục ở đó.

**Báo cáo:** `docs/codex-queue/115-report.md`.

**Thứ tự:** sau 114.

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận mới:** ảnh được chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp` (xem HUD của nó: khung có chi tiết, viền kim loại, icon thật). Lấy mức hoàn thiện; không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ (tách nền, cắt, làm đều cạnh) thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/115/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, chữ ký trong ảnh. Chữ thử ở mục Kiểm 5 chỉ nằm trong ảnh kiểm, và là tiếng Anh.
- **KA1 md5:** `md5 -r` mọi file trong `games/typing-defense/art-src/ui/` (đệ quy) trước khi ghi (`_review/115/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, mức chợ, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: chất liệu thật, viền và góc có chi tiết hoàn thiện, đọc rõ ở cỡ nhỏ, hợp với cảnh sử thi. 7 là gọn nhưng thường. 5 là đúng việc nhưng sai tầm (quê, mộc, giấy). 4 là phẳng như CSS. Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2, mỗi tiêu chí 0–2.
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**.
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8.

## Phiếu

**Nơi ghi:** `games/typing-defense/art-src/ui/frames-epic/` (thư mục mới).

**Chỉ được ghi:**
- `ui/frames-epic/<tên>.tryN.png`, `.tryN.prompt.txt`, bản chọn `<tên>.png`, `<tên>.prompt.txt`, `<tên>.alpha.png`, `<tên>.json`;
- `games/typing-defense/art-src/_review/115-*.jpg`, `games/typing-defense/art-src/_review/115/`;
- `docs/codex-queue/115-report.md`.

**Đọc trước (chỉ đọc):** ảnh tham chiếu; màn HUD hôm nay `games/typing-defense/tmp/map1-audit/sheet-1920x1080.jpg`; màn tựa mới `ui/title-epic/` (phiếu 113) và ảnh ghép `_review/114-composite-day.jpg` (phiếu 114) nếu đã có, để cùng màu.

### Khối prompt (nguyên văn)

Mỗi prompt = **STYLE-UI** + phần riêng + dòng nền M.

**STYLE-UI**
```text
Premium high-fantasy game interface art for Wordwoven, a majestic realm inspired by northern Vietnam: carved pale limestone and polished dark jade lacquer, gold-leaf trim and fine bronze inlay, ornament drawn from Dong Son bronze-drum sun-star rings and cloud-scroll patterns, small cinnabar-red and lantern-amber accents. Crisp, finished and richly detailed like the interface of a top commercial fantasy game, with clean bevels, soft inner shadow and a subtle warm rim light, readable at small size. Shown flat and straight on, no perspective, no scenery. No text, letters, numbers, signature or watermark.
```

**FRAME** (dán sau phần riêng của ảnh có 9-slice)
```text
The border is the same all the way along each straight side, so the middle of every side can be stretched; all ornament sits in the four corners. The inner field is a calm, even dark surface for text.
```

**Dòng nền M:** `Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.`

**SAME** (cho `button-active`): `Same object as the attached image: identical shape, size, position and colours. Change only what is described.`

### Chín ảnh

| Tên | Khổ | 9-slice | Phần riêng |
|---|---|---|---|
| `panel-large` | 1024 × 1024 | có | `A large dialog panel for pause, settings and results screens: a dark jade lacquer field framed by a carved pale limestone border with a thin gold-leaf inner rim and bronze cloud-scroll corner pieces.` + FRAME |
| `plate-long` | 1536 × 512 | có | `A long horizontal HUD plate for a resource bar: a dark jade lacquer strip with a thin carved limestone edge, gold-leaf rim and small bronze end caps shaped like cloud scrolls.` + FRAME |
| `button` | 1536 × 512 | có | `A wide button: a carved limestone tablet with a dark jade inset, a thin gold-leaf rim and small bronze corner studs, at rest.` + FRAME |
| `button-active` | 1536 × 512 | có | `The same button, selected: the gold-leaf rim glows warm amber, a soft golden light rises from the inset edges.` Đính kèm `button` đã chọn với dòng SAME |
| `banner` | 1536 × 512 | không | `A ceremonial banner for Day and Night titles and wave starts: a long dark jade lacquer ribbon with carved gold-leaf edges, swallow-tail ends and a small Dong Son sun-star medallion at each end.` |
| `tooltip` | 1024 × 1024 | có | `A small tooltip card: dark jade lacquer with a thin gold-leaf rim and tiny bronze corner pins, very little ornament.` + FRAME |
| `portrait-ring` | 1024 × 1024 | không | `A round portrait frame for hero portraits: a bronze ring engraved with the Dong Son sun-star rays, gold-leaf inner rim, small jade inlays at the four quarters. The centre of the ring is empty and filled with the flat background colour.` |
| `crest` | 1024 × 1024 | không | `A header crest ornament: a Dong Son sun-star medallion in bronze and gold leaf with two cloud-scroll wings, to sit on the top edge of a panel.` |
| `divider` | 1536 × 512 | không | `An ornamental horizontal divider line: a thin gold-leaf rule with a small jade lozenge at the centre and cloud-scroll tips at both ends.` |

**Hậu kỳ:**
1. Tách nền bằng `tools/art-normalize/key-alpha.sh` (đọc README) thành `<tên>.alpha.png`. `portrait-ring`: lòng ring cũng trong suốt.
2. **9-slice** (bốn ảnh có cột "có", và `button-active` dùng cùng đường cắt với `button`): chọn bốn đường cắt (px) sao cho cạnh giữa là phần lặp được. Ghi `<tên>.json`: `{ "size": [W, H], "slice": { "left": L, "right": R, "top": T, "bottom": B }, "fill": "#rrggbb" }`, `fill` là màu trung vị của lòng.
3. Dựng thử bằng ImageMagick: mỗi khung 9-slice ở 3 cỡ (480 × 160, 320 × 320, 720 × 120), kéo giãn cạnh giữa, giữ nguyên góc.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/typing-defense/art-src/ui/` (đệ quy).
2. **Khổ** đúng bảng; khác thì cắt giữa rồi thu bằng Lanczos, ghi lệnh.
3. **Alpha sạch:** min 0, max 255; 0 % px có alpha > 0 mà hue 285–330° và S > 0,5; không viền hồng ở phóng 4× (`_review/115-edge.jpg`); đốm rời nhỏ hơn 20 px: 0.
4. **Cạnh kéo được** (khung 9-slice): trong dải cạnh giữa, độ lệch chuẩn luma theo chiều kéo ≤ 0,05; không chi tiết riêng (đinh, hoa văn) trong dải đó.
5. **Lòng đọc chữ được:** in thử chữ tiếng Anh màu kem `#f3ead2`, cỡ 24 px, lên lòng `panel-large`, `plate-long`, `button`, `tooltip`: "Gold 120 · Rice 40", "Resume", "Archer Tower · Level 2". Tương phản WCAG ≥ 7. Ghi số.
6. **Tờ dựng thử** `_review/115-sheet.jpg`: chín bản gốc; ba cỡ dựng thử của mỗi khung 9-slice; `button` và `button-active` cạnh nhau.
7. **Tờ trong cảnh** `_review/115-mock.jpg`: một HUD giả 1920 × 1080 trên ảnh màn tựa mới (113) hay ảnh ghép 114 (nếu chưa có thì trên `games/typing-defense/tmp/map1-audit/sheet-1920x1080.jpg` phóng một ô): `plate-long` trên trái có chữ thử, `banner` trên giữa ("Night 1"), `panel-large` giữa có ba `button` ("Resume", "Settings", "Main Menu"), `portrait-ring` dưới trái. Chữ tiếng Anh.
8. **Tờ so với tham chiếu** `_review/115-vs-ref.jpg`: `115-mock.jpg` đặt cạnh ảnh tham chiếu, cùng cao 640 px; hàng dưới là HUD hôm nay (cắt từ `sheet-1920x1080.jpg`). Ghi một dòng: "đứng cạnh được" hay "chưa", và vì sao.
9. **Đọc ở cỡ nhỏ:** `portrait-ring` và `crest` ở 64 px; khung 9-slice ở cỡ 320 × 96. Ghi nhận ra không.
10. **KA5 mức chợ:** M và Q cho từng bản chọn; M thêm một điểm chung trên `115-mock.jpg`.

**Xong khi:** chín ảnh có bản chọn, qua mục 2–5 và 9, mỗi ảnh tự chấm M ≥ 8 và Q ≥ 8, và điểm M chung của `115-mock.jpg` ≥ 8. Ảnh nào không đạt sau 3 lượt thì giữ bản tốt nhất, ghi rõ chỗ thiếu.
