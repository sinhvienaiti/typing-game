# Phiếu 126 · Last Line · Bốn ảnh ải v2 theo hướng mới (thay phiếu 109) · chờ chủ dự án chọn hướng

**Nguồn:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md`, bible Last Line; thứ tự 8). Phiếu 109 đã giao bốn ảnh ải (`art-src/ui/stages/c1-s1…c1-s4.png`, Claude chấm 7/10 theo mức chợ): chi tiết dày, màu mạnh, nhưng vẽ tàu Vanguard của hướng cũ, bố cục đối xứng giống nhau ở cả bốn ảnh, nhiều nhiễu, không có mốc riêng của từng ải. Giữ 109 làm ảnh tạm; phiếu này vẽ lại bốn ải theo hướng chủ dự án chọn.

**Chỉ chạy sau khi chủ dự án chọn hướng ở phiếu 112.** Phiếu viết cho hướng đề xuất **B · Lightbearer**. Chủ dự án chọn A hay C thì Claude thay khối STYLE và câu nhân vật trước khi xếp phiếu vào làn.

**Báo cáo:** `docs/codex-queue/126-report.md`.

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận mới:** ảnh được chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/typing-survival/art-src/_refs/owner-epic-2026-10-28.webp`. Lấy mức chi tiết, ánh sáng, chiều sâu và cảm giác quy mô; không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ (tách nền, cắt, đổi khổ, chỉnh màu) thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/126/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn (kể cả `ui/stages/*` của 109); xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, chữ ký, khung, viền, HUD trong ảnh. Mọi chữ hiện trong ảnh là tiếng Anh.
- **KA1 md5:** `md5 -r` mọi file trong `games/typing-survival/art-src/` (đệ quy) trước khi ghi (`_review/126/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, mức chợ, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: có mốc lớn làm người chơi nhỏ lại, ít nhất ba lớp sâu (gần, giữa, xa) và trời, ánh sáng có hướng, màu theo kịch bản, chi tiết hoàn thiện. 7 là game indie dễ chịu, nhưng quy mô và ánh sáng thường. 6 là gọn mà chung chung, ánh sáng phẳng. 5 là tranh đẹp nhưng sai tầm. 4 là hình phẳng kiểu clip-art. Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2, mỗi tiêu chí 0–2.
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**.
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8.

## Phiếu

**Nơi ghi:** `games/typing-survival/art-src/ui/stages-v2/` (thư mục mới).

**Chỉ được ghi:**
- `ui/stages-v2/<tên>.tryN.png`, `.tryN.prompt.txt`, bản chọn `<tên>.png`, `<tên>.prompt.txt`;
- `games/typing-survival/art-src/_review/126-*.jpg`, `games/typing-survival/art-src/_review/126/`;
- `docs/codex-queue/126-report.md`.

**Đọc trước (chỉ đọc):** ảnh tham chiếu; hai ảnh của hướng đã chọn (112) và bộ sân v2 (125) nếu đã có; `docs/codex-queue/109-ts-stage-art.md` (bốn ải, khổ, cách đo); `games/typing-survival/src/content/chapter-1.ts` (tên và mục tiêu từng ải); dáng quái `art-src/ui/foes/*.png`.

### Khối prompt (nguyên văn)

Mỗi prompt = **STYLE** + **STAGE** + phần riêng + dòng REF (đính kèm ảnh FIGHT của hướng đã chọn).

**STYLE**
```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
```

**STAGE**
```text
Shot: a stage illustration from a camera a little lower than the game camera, behind and above the hero at the bottom of the image, looking along the causeway toward the black hole. Each stage has its own clear landmark or event as the focal point, placed off centre; the composition is not symmetric. Big readable shapes, no fine noise.
```

**REF** (đính kèm ảnh của phiếu 112 hướng đã chọn): `Use the attached image only to keep the same hero, sentinel guns, foes, place, colours and materials. Paint the new scene as described.`

### Bốn ảnh, 1536 × 864 (16 : 9), nền đặc

| Tên | Ải | Phần riêng |
|---|---|---|
| `c1-s1` | 1 · First Watch (giữ 2:30) | `The first watch: the Lightbearer stands at the gate end of the causeway as the first wave of the Hollow Swarm pours toward her, a few faster scouts in front and one heavy brute behind; her left sentinel fires fast cyan pulses, her right one a wide orange heat beam; the broken station ring arches high on the left.` |
| `c1-s2` | 2 · Hunt the Pack Leader | `Three huge Pack Leaders with golden glowing cracks stride inside the swarm, each marked by a thin ring of light on the deck; the Lightbearer turns toward the nearest one; a tilted monolith on the right catches the disk light.` |
| `c1-s3` | 3 · The Rift | `A rift in space tears across the causeway, glowing orange and violet at its edges, and the swarm crawls out of it; shards of deck float up around the tear; the Lightbearer braces with her cape blown back.` |
| `c1-s4` | 4 · Bright Shields | `A wall of Shield Guards raises shields of blue light across the causeway, splitters behind them; the Lightbearer's sentinels hammer the shields, sparks flying; the void leviathan's shadow rises far behind in the black hole.` |

Tên ải trong cột Ải là gợi ý tiếng Anh cho cảnh; tên thật lấy theo `chapter-1.ts` và lượt dịch tiếng Anh. Ải nào khác bảng thì theo mã, ghi vào báo cáo.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/typing-survival/art-src/` (đệ quy).
2. **Khổ:** 1536 × 864 cho bốn bản chọn (cắt giữa rồi thu bằng Lanczos nếu công cụ trả khổ khác; ghi lệnh).
3. **Đọc ở cỡ nhỏ:** thu về 384 × 216: tách được nhân vật, bầy, và vật riêng của ải (Pack Leader, vết nứt, hàng khiên). Ghi "được" hay "không".
4. **Không chữ, không HUD.**
5. **Cùng bộ, khác bố cục:** luma trung bình bốn ảnh lệch ≤ 0,06, hue trung vị lệch ≤ 15°; nhưng vị trí điểm nhấn (vùng sáng nhất sau blur 64 px) của bốn ảnh không trùng nhau quá 10 % chiều rộng. Ghi số.
6. **Tờ** `_review/126-sheet.jpg`: bốn ảnh mới ở 768 px, hàng dưới bốn ảnh 109 ở 768 px để so.
7. **Tờ so với tham chiếu** `_review/126-vs-ref.jpg`: mỗi ảnh mới cạnh ảnh tham chiếu, cùng cao 480 px. Ghi một dòng cho mỗi ảnh: "đứng cạnh được" hay "chưa", và vì sao.
8. **KA5 mức chợ:** M và Q cho từng ảnh, ở cỡ đầy đủ và ở 384 px.

**Xong khi:** bốn ảnh có bản chọn, qua mục 2–5, mỗi ảnh tự chấm M ≥ 8 và Q ≥ 8.
