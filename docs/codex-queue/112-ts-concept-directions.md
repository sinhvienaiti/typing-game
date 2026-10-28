# Phiếu 112 · Last Line · Ảnh ý tưởng cho ba hướng mới (6 ảnh), để chủ dự án chọn

**Nguồn:** chỉ đạo mỹ thuật 28/10 (`docs/games/ART_DIRECTION_2026-10-28.md`, mục Last Line, bước ý tưởng). Chủ dự án 29/10 sáng: "nếu cần thì bỏ tàu vũ trụ; đổi UI, nền và nhân vật chính của Last Line cho hợp hơn". Phiếu này vẽ ba hướng, mỗi hướng hai ảnh. Chủ dự án chọn một hướng từ tờ so. Phiếu không đổi gì trong game.

**Báo cáo:** `docs/codex-queue/112-report.md`.

**Thứ tự:** phiếu ảnh đầu tiên của lô chỉ đạo mỹ thuật. Chạy trước 113.

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận mới:** ảnh được chấm theo game thương mại, không theo bộ ảnh cũ của ta. Ảnh tham chiếu của chủ dự án: `games/typing-survival/art-src/_refs/owner-epic-2026-10-28.webp`. Lấy mức chi tiết, ánh sáng, chiều sâu và cảm giác quy mô; không chép nội dung.
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ (cắt, đổi khổ, chỉnh màu) thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3). Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/112/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ đọc được, số, logo, HUD, chữ ký, khung, viền trong ảnh.
- **KA1 md5:** `md5 -r` mọi file trong thư mục đích (đệ quy) trước khi ghi (`_review/112/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ (bắt buộc), hai điểm cho mỗi bản chọn:**
  - **M, mức chợ, 0–10:** 9 là ảnh tham chiếu của chủ dự án. 8 là mức phát hành được: có mốc lớn làm người chơi nhỏ lại, ít nhất ba lớp sâu (gần, giữa, xa) và trời, ánh sáng có hướng, màu theo kịch bản, chi tiết hoàn thiện. 7 là game indie dễ chịu, nhưng quy mô và ánh sáng thường. 6 là gọn mà chung chung, ánh sáng phẳng. 5 là tranh đẹp nhưng sai tầm (ấm cúng, quê, nhỏ). 4 là hình phẳng kiểu clip-art. Thang đầy đủ ở ART_DIRECTION §1.3.
  - **Q, 0–10:** 5 tiêu chí của `docs/games/ART_ACCEPTANCE.md` §2.2 (Đúng đề, Đọc được, Hợp bộ, Hình khối, Dùng tiếp), mỗi tiêu chí 0–2.
  - Ảnh đạt khi **M ≥ 8 và Q ≥ 8**. Chấm ở cỡ đầy đủ và cỡ nhỏ nêu trong phiếu.
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8.

## Phiếu

**Vì sao:** Last Line hôm nay là một tàu nhỏ ở đáy một hành lang thép trống, nhìn từ sau. Tàu không có mặt, không có tính cách, và lấy model của Space Typing. Chủ dự án muốn nhân vật chính, nền và UI hợp hơn, và muốn mọi chi tiết có hình, có tiếng, có VFX. Luật chơi giữ nguyên (sim, súng, từ). Chỉ đổi vỏ: view, model, UI.

**Nơi ghi:** `games/typing-survival/art-src/concepts/` (thư mục mới).

**Chỉ được ghi:**
- `concepts/<tên>.tryN.png`, `concepts/<tên>.tryN.prompt.txt`, `concepts/<tên>.png`, `concepts/<tên>.prompt.txt`;
- `games/typing-survival/art-src/_review/112-*.jpg`, `games/typing-survival/art-src/_review/112/`;
- `docs/codex-queue/112-report.md`.

**Đọc trước (chỉ đọc):**
- ảnh tham chiếu `games/typing-survival/art-src/_refs/owner-epic-2026-10-28.webp`;
- cảnh hôm nay: `games/typing-survival/art-src/arena/concept-fight.png`, `games/typing-survival/tmp/map1-audit/sheets/sheet-c1s1-fight-1920x1080.jpg`;
- dáng quái: `games/typing-survival/art-src/ui/foes/*.png` (phiếu 089); hình năm súng: `games/typing-survival/art-src/ui/icons/gun-*.png`;
- tên súng và quái: `games/typing-survival/src/content/guns.ts`, `foes.ts`.

**Bố cục trận phải giữ** (để luật chơi không đổi):
- một làn thẳng dài, chạy từ đáy ảnh lên phía hố đen;
- nhân vật chính đứng giữa đáy, trong một vòng sáng trên sàn;
- hai vũ khí, một bên trái và một bên phải nhân vật (hai bến súng của game);
- bầy quái tràn xuống từ cuối làn;
- ngay trên đầu nhân vật là chỗ game hiện chữ đang gõ: vùng đó tối và lặng.

### Cách ghép prompt

Mỗi prompt = khối **CONCEPT STYLE** nguyên văn + khối **hướng** (A, B hay C) nguyên văn + khối **cảnh** (FIGHT hay KEYART) nguyên văn. Không thêm câu phong cách khác.

**CONCEPT STYLE**
```text
Epic science-fiction game key art for Last Line, a typing action game set on the last causeway of a colossal space station at the edge of a black hole whose blazing orange-gold accretion disk fills the sky. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. No text, letters, numbers, signature, watermark, logo, HUD, frame or border.
```

**Hướng A · Iron Warden**
```text
Direction A, Iron Warden: the hero is Warden, a six-metre walking battle mech of scarred graphite armour with hazard-orange stripes, a glowing cyan cockpit with the pilot visible inside, and two heavy arm cannons, one on each arm. The deck is a heavy industrial steel causeway with hazard stripes, cargo cranes and docking arms. The foes are the Black Hole Swarm, biomechanical void insects of black chitin with glowing orange veins. Typing shows as segments of a glowing ammo rail along each arm that light up one by one. Mood: heavy, industrial, brave.
```

**Hướng B · Lightbearer**
```text
Direction B, Lightbearer: the hero is a lone armoured Lightbearer, a tall slender guardian in white-gold and graphite armour with a long dark-blue cape and a glowing cyan visor, with two floating sentinel guns of relic technology hovering at her shoulders, one on each side. The deck is a colossal causeway of dark steel and pale ancient stone, with tilted monoliths and broken station rings drifting at its edge. The foes are the Hollow Swarm, void creatures of black glass with glowing orange cracks, and far behind them a colossal void leviathan rises out of the black hole. Typing shows as small glyphs of light that fly from her raised hand into a sentinel and form a ring around it. Mood: mythic, lonely, heroic.
```

**Hướng C · Rampart**
```text
Direction C, Rampart: the hero is the Rampart, a colossal fortress wall built across the station's last corridor, with two giant turrets on its battlement, one on each side, and a commander in a long coat standing between them at a lit command rail. The corridor floor below leads to the black hole. The foes are the Black Hole Swarm, biomechanical void insects of black chitin with glowing orange veins, climbing the walls and pouring down the corridor. Typing shows as lines of glowing firing code that run along the turret barrels. Mood: military, massive, defiant.
```

**Cảnh FIGHT**
```text
Shot: a fight moment seen from the game camera, behind and above the hero, looking down one long straight lane toward the black hole at the top of the image. The hero stands at the bottom centre inside a glowing ring on the deck, about one fifth of the image height tall, with one weapon on the left and one on the right. The horde fills the far half of the lane and pours toward the hero. Both weapons fire up the lane: the left one a stream of fast cyan pulses, the right one a wide orange heat beam, with hits, sparks, smoke and falling foes. The area just above the hero's head stays darker and calm. Glyphs are abstract glowing shapes, never readable letters.
```

**Cảnh KEYART**
```text
Shot: a cinematic title key art from a low camera close behind and beside the hero. The hero is large in the left or right third, seen from behind or three-quarter back, facing the black hole and the oncoming horde across the causeway. A colossal landmark dwarfs the hero: the accretion disk and the station ruins around it. One clear focal point, strong value contrast between the hero's dark silhouette and the bright disk, and a calm area in the upper third for a logo.
```

Hướng C: "hero" trong hai khối cảnh là hai tháp pháo và người chỉ huy đứng giữa. Hướng B: quái vật khổng lồ của hư không (void leviathan) nên thấy rõ trong ảnh KEYART.

### Sáu ảnh, mỗi ảnh 1536 × 1024, nền đặc

| Tên file | Hướng | Cảnh |
|---|---|---|
| `a-iron-warden-fight` | A | FIGHT |
| `a-iron-warden-keyart` | A | KEYART |
| `b-lightbearer-fight` | B | FIGHT |
| `b-lightbearer-keyart` | B | KEYART |
| `c-rampart-fight` | C | FIGHT |
| `c-rampart-keyart` | C | KEYART |

Ảnh FIGHT vẽ trước, vì ảnh trận khó nhất. Ảnh KEYART của một hướng đính kèm ảnh FIGHT đã chọn của hướng đó, với dòng: `Use the attached image only to keep the same hero, weapons, foes, colours and materials. Paint the new shot as described.`

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/typing-survival/art-src/` (đệ quy).
2. **Khổ:** `magick identify` ra 1536 × 1024 cho sáu bản chọn. Công cụ trả khổ khác thì cắt giữa rồi thu bằng Lanczos; ghi lệnh.
3. **Không chữ, không HUD:** xem ở cỡ đầy đủ. Ký hiệu sáng không được thành chữ cái đọc được.
4. **Giữ bố cục trận** (ba ảnh FIGHT): làn thẳng lên phía trên; nhân vật giữa đáy; một vũ khí mỗi bên; bầy ở nửa xa. Ghi "có" hay "không" từng ý.
5. **Chỗ hiện chữ:** trong hộp x 35–65 %, y 55–68 % của ảnh FIGHT, luma trung bình ≤ 0,45 và không px nào có luma > 0,92 (`L = 0,2126R + 0,7152G + 0,0722B`, sRGB 0–1). Ghi số.
6. **Đọc ở cỡ nhỏ:** thu về 384 × 256. Tách được nhân vật, hai vũ khí, bầy, hố đen bằng mắt. Ghi "được" hay "không" cho từng ảnh.
7. **Tờ chọn hướng** `_review/112-directions.jpg`, cho chủ dự án xem:
   - hàng đầu: `concept-fight.png` hôm nay và ảnh tham chiếu của chủ dự án, cùng cao 512 px, nhãn "Today" và "Owner reference";
   - ba hàng sau, mỗi hướng một hàng: FIGHT và KEYART cao 512 px, rồi ảnh tham chiếu cao 512 px ở cột cuối;
   - nhãn tiếng Anh ở đầu mỗi hàng: "A · Iron Warden", "B · Lightbearer", "C · Rampart".
8. **Tờ so với tham chiếu** `_review/112-vs-ref.jpg`: mỗi bản chọn đặt cạnh ảnh tham chiếu, cùng cao 640 px. Dưới mỗi cặp ghi một dòng: "đứng cạnh được" hay "chưa", và vì sao (quy mô, ánh sáng, chi tiết, chiều sâu).
9. **KA5 mức chợ:** M và Q cho từng bản chọn, ở cỡ đầy đủ và ở 384 × 256.

**Xong khi:** sáu ảnh có bản chọn, qua mục 2–6, và mỗi ảnh tự chấm M ≥ 8, Q ≥ 8. Ảnh nào không đạt sau 3 lượt thì giữ bản tốt nhất, ghi rõ chỗ thiếu. Báo cáo kết thúc bằng một bảng ngắn: mỗi hướng, điểm M của hai ảnh, và một câu "hướng này mạnh ở đâu, yếu ở đâu" (không chọn thay chủ dự án).
