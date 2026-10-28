# Phiếu 127 · Last Line · Khung UI và bảng: kính khói, chỉ vàng trắng, ánh lam (9 ảnh) · chờ chủ dự án chọn hướng

**Nguồn:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md`, bible Last Line; thứ tự 8). UI hôm nay là bảng CSS xám có sọc cam đen (chấm 6/10 theo mức chợ): gọn, đọc được, nhưng là chữ trên bảng phẳng. Phiếu này chỉ làm **khung, bảng, thẻ, nút, dải**. Icon và hình nhỏ của từng ô thuộc lượt rà hình UI (`docs/games/map1/UI_IMAGERY.md`, `UI_IMAGERY_CODEX.md`, khi có); không làm lại các mục ở đó.

**Chỉ chạy sau khi chủ dự án chọn hướng ở phiếu 112.** Phiếu viết cho hướng đề xuất **B · Lightbearer**. Chủ dự án chọn A (thép công nghiệp, sọc cảnh báo) hay C (màn chiến thuật quân sự) thì Claude thay khối STYLE-UI trước khi xếp phiếu vào làn.

**Báo cáo:** `docs/codex-queue/127-report.md`.

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận mới:** ảnh được chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/typing-survival/art-src/_refs/owner-epic-2026-10-28.webp`. Lấy mức chi tiết, ánh sáng, chiều sâu và cảm giác quy mô; không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ (tách nền, cắt, đổi khổ, chỉnh màu) thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/127/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, chữ ký, khung, viền, HUD trong ảnh. Mọi chữ hiện trong ảnh là tiếng Anh.
- **KA1 md5:** `md5 -r` mọi file trong `games/typing-survival/art-src/` (đệ quy) trước khi ghi (`_review/127/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, mức chợ, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: có mốc lớn làm người chơi nhỏ lại, ít nhất ba lớp sâu (gần, giữa, xa) và trời, ánh sáng có hướng, màu theo kịch bản, chi tiết hoàn thiện. 7 là game indie dễ chịu, nhưng quy mô và ánh sáng thường. 6 là gọn mà chung chung, ánh sáng phẳng. 5 là tranh đẹp nhưng sai tầm. 4 là hình phẳng kiểu clip-art. Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2, mỗi tiêu chí 0–2.
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**.
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8.

## Phiếu

**Nơi ghi:** `games/typing-survival/art-src/ui/frames-epic/` (thư mục mới).

**Chỉ được ghi:**
- `ui/frames-epic/<tên>.tryN.png`, `.tryN.prompt.txt`, bản chọn `<tên>.png`, `<tên>.prompt.txt`, `<tên>.alpha.png`, `<tên>.json`;
- `games/typing-survival/art-src/_review/127-*.jpg`, `games/typing-survival/art-src/_review/127/`;
- `docs/codex-queue/127-report.md`.

**Đọc trước (chỉ đọc):** ảnh tham chiếu (xem HUD: khung có chi tiết, icon thật); màn hôm nay `games/typing-survival/tmp/map1-audit/sheets/sheet-screens-1920x1080.jpg` và `sheet-c1s1-fight-1920x1080.jpg` (bến súng hai bên tàu, dòng chữ trên mũi tàu, thanh Armor, đồng hồ); `docs/codex-queue/115-td-ui-frames.md` (cách làm 9-slice, cách đo giống hệt).

### Khối prompt (nguyên văn)

Mỗi prompt = **STYLE-UI** + phần riêng + **FRAME** (ảnh có 9-slice) + dòng nền M.

**STYLE-UI**
```text
Premium science-fiction game interface art for Last Line: dark smoked glass over graphite steel, fine white-gold filigree lines, thin constellation lines and small glyph marks at the corners, electric cyan and orange-gold light accents, a faint inner glow. Crisp, finished and richly detailed like the interface of a top commercial sci-fi action game, with clean bevels and sharp edges, readable at small size. Shown flat and straight on, no perspective, no scenery. No text, letters, numbers, signature or watermark.
```

**FRAME**
```text
The border is the same all the way along each straight side, so the middle of every side can be stretched; all ornament sits in the four corners. The inner field is a calm, even dark surface for text.
```

**Dòng nền M:** `Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.`

**SAME** (cho `button-active`): `Same object as the attached image: identical shape, size, position and colours. Change only what is described.`

### Chín ảnh

| Tên | Khổ | 9-slice | Phần riêng |
|---|---|---|---|
| `panel-large` | 1024 × 1024 | có | `A large dialog panel for menus, briefings and results: dark smoked glass over a graphite steel frame, fine white-gold filigree along the inner edge, small glyph marks and thin constellation lines in the corners.` + FRAME |
| `bay-card` | 1536 × 512 | có | `A gun bay card that sits beside the hero: a dark smoked glass plate with a graphite steel rim, a thin bright line along the top edge where the gun's colour will glow, small white-gold corner brackets.` + FRAME |
| `word-plate` | 1536 × 512 | có | `A plate for the word being typed, above the hero: very dark smoked glass, a thin white-gold rim, a faint electric cyan inner glow along the bottom edge, nothing busy inside.` + FRAME |
| `plate-long` | 1536 × 512 | có | `A long HUD plate for the Armor bar and the timer: dark graphite steel with an inset glass channel, white-gold end caps with small glyph marks.` + FRAME |
| `button` | 1536 × 512 | có | `A wide button: a graphite steel tablet with a dark glass inset, thin white-gold rim, at rest.` + FRAME |
| `button-active` | 1536 × 512 | có | `The same button, selected: the rim glows electric cyan and a soft white-gold light rises from the inset edges.` Đính kèm `button` đã chọn với dòng SAME |
| `banner` | 1536 × 512 | không | `A stage banner: a long blade-shaped plate of dark glass and graphite steel, a bright white-gold line through its middle like an event horizon, small orange-gold flares at both tips.` |
| `portrait-ring` | 1024 × 1024 | không | `A round frame for foe and hero portraits: a graphite steel ring with white-gold filigree and four small glyph studs, a thin cyan inner rim. The centre of the ring is empty and filled with the flat background colour.` |
| `divider` | 1536 × 512 | không | `An ornamental horizontal divider: a thin white-gold line with a small diamond of cyan light at the centre and fine constellation dots at both ends.` |

**Hậu kỳ:** như phiếu 115: tách nền bằng `tools/art-normalize/key-alpha.sh` thành `<tên>.alpha.png` (lòng `portrait-ring` trong suốt); 9-slice ghi `<tên>.json` `{ "size": [W, H], "slice": { "left": L, "right": R, "top": T, "bottom": B }, "fill": "#rrggbb" }`; dựng thử ba cỡ (480 × 160, 320 × 320, 720 × 120).

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/typing-survival/art-src/` (đệ quy).
2. **Khổ** đúng bảng; khác thì cắt giữa rồi thu bằng Lanczos, ghi lệnh.
3. **Alpha sạch:** min 0, max 255; 0 % px có alpha > 0 mà hue 285–330° và S > 0,5; không viền hồng ở phóng 4× (`_review/127-edge.jpg`); đốm rời nhỏ hơn 20 px: 0.
4. **Cạnh kéo được** (khung 9-slice): trong dải cạnh giữa, độ lệch chuẩn luma theo chiều kéo ≤ 0,05; không chi tiết riêng trong dải đó.
5. **Lòng đọc chữ được:** in thử chữ tiếng Anh trắng `#f2f4f8`, cỡ 24 px: "Armor 100", "Pulse Gun", "Resume", "Stage 1 · First Watch"; và chữ gõ 42 px "thank" lên `word-plate`. Tương phản WCAG ≥ 7. Ghi số.
6. **Tờ dựng thử** `_review/127-sheet.jpg`: chín bản gốc; ba cỡ dựng thử của mỗi khung 9-slice; `button` và `button-active` cạnh nhau.
7. **Tờ trong cảnh** `_review/127-mock.jpg`: một màn trận giả 1920 × 1080 trên ảnh FIGHT của hướng đã chọn (112) hay ảnh ghép 125: hai `bay-card` hai bên nhân vật có chữ thử ("Pulse Gun · art", "Heat Beam · thank"), `word-plate` trên đầu nhân vật, `plate-long` trên trái ("Armor 100"), `banner` trên giữa ("Stage 1 · First Watch"). Chữ tiếng Anh.
8. **Tờ so với tham chiếu** `_review/127-vs-ref.jpg`: `127-mock.jpg` cạnh ảnh tham chiếu, cùng cao 640 px; hàng dưới là màn trận hôm nay (cắt từ `sheet-c1s1-fight-1920x1080.jpg`). Ghi một dòng: "đứng cạnh được" hay "chưa", và vì sao.
9. **KA5 mức chợ:** M và Q cho từng bản chọn; M thêm một điểm chung trên `127-mock.jpg`.

**Xong khi:** chín ảnh có bản chọn, qua mục 2–5, mỗi ảnh tự chấm M ≥ 8 và Q ≥ 8, điểm M chung của `127-mock.jpg` ≥ 8.
