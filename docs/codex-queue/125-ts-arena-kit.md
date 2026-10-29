# Phiếu 125 · Last Line · Bộ sân trận v2: sàn, tường, vòng xa, hố đen, quái vật hư không (8 ảnh) · chờ chủ dự án chọn hướng

**Nguồn:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md`, bible Last Line; thứ tự 8). Bộ sân của phiếu 088 (`art-src/arena/*`) chấm 6–7/10 theo mức chợ: tối, chắc tay, nhưng là hành lang công nghiệp chung chung, không có mốc nào làm người chơi nhỏ lại ngoài hố đen.

**Chỉ chạy sau khi chủ dự án chọn hướng ở phiếu 112.** Phiếu viết cho hướng đề xuất **B · Lightbearer** (đường đắp đá và thép, vòng trạm vỡ, khối đá nghiêng). Chủ dự án chọn A hay C thì Claude thay khối STYLE và các câu cảnh trước khi xếp phiếu vào làn. Luật chơi và bố cục làn giữ nguyên.

**Báo cáo:** `docs/codex-queue/125-report.md`.

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận mới:** ảnh được chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/typing-survival/art-src/_refs/owner-epic-2026-10-28.webp`. Lấy mức chi tiết, ánh sáng, chiều sâu và cảm giác quy mô; không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ (tách nền, làm liền mép, ghép, chỉnh màu) thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/125/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn (kể cả `arena/*` của 088); xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, HUD, chữ ký trong ảnh. Ký hiệu khắc trên sàn là hình trừu tượng, không thành chữ đọc được.
- **KA1 md5:** `md5 -r` mọi file trong `games/typing-survival/art-src/` (đệ quy) trước khi ghi (`_review/125/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, mức chợ, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: có mốc lớn làm người chơi nhỏ lại, ít nhất ba lớp sâu và trời, ánh sáng có hướng, màu theo kịch bản, chi tiết hoàn thiện. 7 là game indie dễ chịu, nhưng quy mô và ánh sáng thường. 6 là gọn mà chung chung. 5 là đẹp nhưng sai tầm. 4 là phẳng. Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2, mỗi tiêu chí 0–2.
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**. Mảnh sân là một phần của cảnh: M chấm trên ảnh ghép (mục Kiểm 7).
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8.

## Phiếu

**Luật đọc chữ (giữ từ 088):** sàn và tường nằm sau chữ người chơi gõ và sau bầy quái. Chúng phải tối. Vùng sáng là hố đen ở xa, đèn chạy dọc mép, và VFX của game. `docs/FEEL_PASS_S1.md` §4.1 của game cho phép nền dưới dòng chữ sáng thêm tối đa 0,02.

**Nơi ghi:** `games/typing-survival/art-src/arena-v2/` (thư mục mới).

**Chỉ được ghi:**
- `arena-v2/<tên>.tryN.png`, `.tryN.prompt.txt`, bản chọn `<tên>.png`, `<tên>.prompt.txt`;
- `games/typing-survival/art-src/_review/125-*.jpg`, `games/typing-survival/art-src/_review/125/`;
- `docs/codex-queue/125-report.md`.

**Đọc trước (chỉ đọc):** ảnh tham chiếu; hai ảnh của hướng đã chọn ở phiếu 112 (`art-src/concepts/b-*.png` khi chọn B); bộ cũ `art-src/arena/*.prompt.txt` (khổ, alpha, giới hạn luma); `docs/codex-queue/088-report.md`; cảnh trận `games/typing-survival/tmp/map1-audit/sheets/sheet-c1s1-fight-1920x1080.jpg`.

### Khối prompt (nguyên văn)

Mỗi prompt = **STYLE** + **ARENA** + phần riêng (+ dòng nền khi có alpha).

**STYLE**
```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
```

**ARENA**
```text
Environment asset for a 3D typing action game. This layer sits behind the words the player types and behind the horde, so its surfaces stay dark: deep graphite and navy with only thin edge highlights, small cyan running lights and a few dim orange-gold reflections of the disk. No people, creatures, ships, weapons, HUD or glowing effects of the game.
```

**Dòng nền alpha:** `Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.` (`void-leviathan` có ánh tím nhỏ: thay bằng nền G `#00FF00` và câu "the subject contains no green at all".)

### Tám ảnh

**Đường đi (chủ dự án 29/10):** "phần đường đi cũng phải làm thật đẹp, chứ đường đi nhìn như kiểu lấy ngón tay quệt dài như kia nó rất xấu". Làn đường đắp là thứ người chơi nhìn suốt trận. `deck-tile` phải có chất liệu chạy dọc đường (tấm thép và phiến đá xếp theo hướng đi, khe nối, vết mòn giữa làn), `deck-edge` là một gờ thật có độ cao, và `deck-decals` dùng để phá sự lặp ở mép làn. Xem `docs/games/PATH_QUALITY.md` §2. Kiểm thêm trên tờ thử: làn không được trông như một dải màu đều có mép mờ.

| Tên | Khổ giao | Alpha | Phần riêng |
|---|---|---|---|
| `deck-tile` | 1024 × 1024, liền mép | không | `Seamless tileable deck texture, edges wrap on all four sides, seen straight from above with no perspective, flat shadowless light: big plates of dark graphite steel with bands of pale ancient stone set between them, worn smooth, faint dim cyan glyph inlays in the stone. One tile covers 6 by 6 metres.` |
| `deck-edge` | 1536 × 512, liền mép trái phải | có | `A long straight edge of the causeway seen from the side and a little above: a low parapet of pale ancient stone capped with dark steel, a line of small cyan running lights, below it the dark underside of the deck dropping into the void. Seamless from left to right.` |
| `wall-left` | 1024 × 2048 | có | `A tall structure rising beside the left side of the causeway, seen from the deck: a tilted monolith of dark stone wrapped in steel gantries, a broken segment of a station ring arching above it, thin cyan lights, the inner face lit softly by the orange-gold disk.` |
| `wall-right` | 1024 × 2048 | có | Như `wall-left` nhưng ở bên phải, khác dáng: `two stacked monoliths and a broken docking arm`; đính kèm `wall-left` đã chọn với dòng `Use the attached image only to match the style, colours and light. Paint a different structure as described.` |
| `far-ring` | 2048 × 1024 | có | `Far silhouettes at the end of the causeway: titanic broken station rings and tilted monoliths drifting in front of the accretion disk, dark against the light, with a thin bright rim along their edges.` |
| `sky-disk` | 1536 × 1024 | không | `The sky at the end of the causeway: a black hole with a blazing orange-gold accretion disk curving around it, the light bending over and under the dark centre, a deep navy starfield with faint violet nebula, a few far drifting fragments. The lower 25% fades into dark navy.` |
| `void-leviathan` | 1536 × 1024 | có | `A colossal void leviathan rising out of the black hole: a vast serpentine creature of black glass with glowing orange cracks along its body, a crown of long spines, six pale glowing eyes, its body fading into dark mist at the bottom.` |
| `deck-decals` | 2048 × 2048 (lưới 2 × 2) | có | Bốn decal nhìn từ trên, ánh sáng phẳng: `a scorch mark with glowing orange cracks`; `a heap of shattered black glass shards`; `a ring of cyan light glyphs on the deck, abstract, never readable letters, where the hero stands`; `a deep crack across a stone band`. Sinh bốn ảnh vuông rồi ghép bằng script như 088 |

**Khổ:** sinh ở khổ công cụ cho, rồi cắt, ghép hoặc đổi cỡ bằng Lanczos như phiếu 088; ghi lệnh. Tách nền bằng `tools/art-normalize/key-alpha.sh`.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/typing-survival/art-src/` (đệ quy).
2. **Khổ** đúng bảng; ảnh có alpha là RGBA.
3. **Alpha sạch:** min 0, max 255; 0 % px có alpha > 0 mà hue của màu nền (±12°) và S > 0,5; không viền hồng hay xanh ở phóng 4× (`_review/125-edge.jpg`); không đốm rời nhỏ hơn 20 px.
4. **Tối dưới chữ:** `deck-tile`, `deck-edge`, `wall-left`, `wall-right`: luma trung bình của px đục ≤ 0,16; px có luma > 0,8 ≤ 2 % (như 088). Ghi số.
5. **Liền mép:** `deck-tile` theo cách đo của phiếu 095 (`E ≤ 1,25 · I`); `deck-edge` liền trái phải (cùng cách, chỉ theo trục X).
6. **Không chữ:** vòng ký hiệu và vân khắc không thành chữ đọc được.
7. **Ảnh ghép và tờ so:**
   - `_review/125-composite.jpg`: 1536 × 1024 dựng bằng script theo góc camera trận (từ sau và trên nhân vật nhìn dọc làn): `sky-disk`, `void-leviathan`, `far-ring`, `wall-left`, `wall-right`, sàn lát `deck-tile` theo phối cảnh, hai `deck-edge`, decal vòng ký hiệu ở giữa đáy; thêm ảnh FIGHT của hướng đã chọn (112) bên cạnh để so;
   - `_review/125-vs-ref.jpg`: ảnh ghép cạnh ảnh tham chiếu, cùng cao 640 px; hàng dưới là `arena/concept-fight.png` cũ. Ghi một dòng: "đứng cạnh được" hay "chưa", và vì sao;
   - đo trên ảnh ghép: hộp x 35–65 %, y 55–68 % (chỗ dòng chữ) có luma trung bình ≤ 0,30.
8. **KA5 mức chợ:** M trên ảnh ghép; Q cho từng ảnh ở cỡ đầy đủ và ở 384 px.

**Xong khi:** tám ảnh có bản chọn, qua mục 2–6, ảnh ghép tự chấm M ≥ 8 và qua số đo dòng chữ, mỗi ảnh Q ≥ 8. Ảnh nào không đạt sau 3 lượt thì giữ bản tốt nhất, ghi rõ chỗ thiếu.
