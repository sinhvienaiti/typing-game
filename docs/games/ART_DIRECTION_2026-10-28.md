# Chỉ đạo mỹ thuật ba game theo mức chợ (28/10/2026)

Ba game: **Dragonhold** (`games/dragon-hold`), **Wordwoven** (`games/typing-defense`, trước là Lời Gọi), **Last Line** (`games/typing-survival`). Không đụng Tu Tiên.

**Vì sao có tài liệu này.** Tối 28/10, chủ dự án chê ảnh của ta "xấu đến thậm tệ": quê mùa, dưới mức thị trường. Ảnh mẫu của chủ dự án nằm ở `games/<id>/art-src/_refs/owner-epic-2026-10-28.webp` (cùng một file ở cả ba game): một cảnh MMO thương mại có hẻm núi sa mạc hùng vĩ, một quái thú khổng lồ bay trên trời, một anh hùng khoác áo choàng, ánh sáng điện ảnh, chiều sâu rất lớn và HUD đầy đủ. Riêng Wordwoven bị chê "như thôn quê"; chủ dự án muốn "đẹp và hùng vĩ".

Ta trượt vì đã chấm ảnh theo khối phong cách của chính mình ("cozy storybook folk valley" của Wordwoven, "storybook misty pine forest" của Dragonhold) và theo số đo kỹ thuật. Ta chưa bao giờ so ảnh với game trên chợ.

**Quyết định của chủ dự án (28/10 tối và 29/10 sáng):**
- mọi chữ người chơi đọc là tiếng Anh; tiếng Việt chỉ ở nghĩa của từ đang học;
- Wordwoven theo hướng sử thi: làm lại nền, trời, phông xa, màn tựa, ảnh chủ đạo, khung UI; giữ các model 3D và chỉnh ánh sáng; ghi lại model lệch hướng để dựng lại sau;
- mức chợ áp cho cả ba game: chấm lại nền, màn tựa, ảnh chủ đạo; cái nào dưới 8 thì làm lại;
- Last Line (29/10): nếu cần thì bỏ tàu vũ trụ; đổi UI, nền và nhân vật chính cho hợp hơn; mọi chi tiết có hình, có tiếng, có VFX, từ chữ đang gõ tới đòn đánh, chiêu và từng tiếng nhỏ của quái. Luật chơi (sim, súng, từ) giữ nguyên.

Tài liệu này đứng trên mọi khối STYLE cũ trong `games/*/docs/art-requests/` và trong prompt của các phiếu Codex trước 112. Luật điểm 2D từ 8, 3D từ 7 của `ART_ACCEPTANCE.md` vẫn giữ; tài liệu này đổi **thước chấm**: điểm M theo chợ (mục 1.3).

---

## 0. Tóm tắt

**Chấm lại** (chi tiết ở mục 5; tờ so ở `games/<id>/tmp/art-direction/`):

| Game | Số ảnh chấm | Giữ (≥ 8) | Làm lại | Điểm |
|---|---:|---:|---:|---|
| Wordwoven | 48 | 0 | 48 | 3,5–5 |
| Dragonhold | 9 | 0 | 9 | 3–6,5 |
| Last Line | 10 | 0 | 10 | 6–7 |

Không ảnh nào tới 8. Ảnh tốt nhất của ta là cảnh trận của Last Line (7): có không khí, có chiều sâu, nhưng là hành lang công nghiệp trống, và nhân vật chính là một con tàu nhỏ không mặt.

**Phiếu Codex mới: 112–129** (mục 6). Thứ tự theo cái người chơi thấy trước:
1. 112 Last Line: ảnh ý tưởng ba hướng, để chủ dự án chọn;
2. 113 Wordwoven: màn tựa, ảnh chủ đạo, logo "Wordwoven";
3. 114 Wordwoven: trời và phông xa cho map 1 3D;
4. 115 Wordwoven: khung UI và bảng (thay 110);
5. 116–118 Wordwoven: cảnh vật v3, v4 (viết lại 106);
6. 119 Dragonhold: màn tựa, ảnh chủ đạo, logo "Dragonhold";
7. 120 Dragonhold: trời và phông xa;
8. 121 Last Line: nền màn chính, nạp súng, hành trình, kết quả, logo (chờ chọn hướng);
9. 122–129: phần còn dưới 8 (đất, decal, mốc Tripo, bộ sân và UI Last Line, dựng lại nhà mái tranh).

**Last Line đổi hướng:** đề xuất hướng **B · Lightbearer** (một vệ binh khoác áo choàng, hai súng canh bay hai bên vai, giữ đường đắp cuối cùng ở mép hố đen). Chủ dự án chọn từ tờ của phiếu 112.

**Cần chủ dự án** (mục 9): chọn hướng Last Line; dựng Tripo cho các mốc (Dragonhold 6, Wordwoven 5) và cho nhân vật Last Line; đồng ý hay không việc dựng lại 6 nhà mái tranh của Wordwoven.

---

## 1. Mức chợ

### 1.1 Ảnh chủ đạo và nền của game thương mại có gì

Tôi gọi tên game chỉ để làm mốc so, không tải ảnh nào. Mốc so: Genshin Impact (vùng Liyue: rừng đá vôi, rất gần thế giới của Wordwoven), Honkai: Star Rail, Destiny 2 (khoa học viễn tưởng huyền thoại, vệ binh khoác áo choàng), Diablo IV và Hades (camera nhìn xuống mà vẫn hùng vĩ), Rise of Kingdoms và Call of Dragons (chiến thuật nhìn từ trên), Kingdom Rush Vengeance (phòng thủ tháp), League of Legends (tranh nhân vật), Warcraft (đồ họa vẽ tay khối chắc), Mass Effect và Warframe (trạm vũ trụ, hố đen).

**Quy mô và chiều sâu.**
- Luôn có bốn tầng: gần (khung cảnh, đá, lan can, cây sát mép ảnh), giữa (nơi hành động xảy ra), xa (núi, tháp, công trình) và trời.
- Mỗi tầng xa hơn thì nhạt hơn, lam hơn, mềm hơn. Có sương hay bụi nằm giữa các tầng.
- Đường dẫn mắt (sông, đường, cầu, bậc thang) chạy từ gần vào xa.

**Mốc làm người chơi nhỏ lại.**
- Có ít nhất một vật to gấp chục, gấp trăm lần nhân vật: quái thú bay, tháp đá cao hàng trăm mét, tượng khổng lồ, cổng thành, hố đen.
- Người xem đọc được thước đo: nhân vật nhỏ đứng cạnh vật lớn.
- Ảnh mẫu của chủ dự án làm đúng cách đó: anh hùng nhìn từ sau, quái thú khổng lồ trên trời, hẻm núi chạy ra xa.

**Ánh sáng và không khí điện ảnh.**
- Ánh sáng có hướng rõ: nắng thấp (bình minh, chiều tà) hay ngược sáng. Bóng dài.
- Viền sáng (rim) tách hình khỏi nền.
- Tia nắng qua mây, bụi hay sương trong vệt sáng; sương đọng thấp.
- Có một điểm sáng nhất, và đó là nơi mắt phải nhìn.

**Kịch bản màu.**
- Hai họ màu chính đối nhau: bóng lạnh (ngọc, lam) và sáng ấm (vàng, cam).
- Một màu nhấn nhỏ (son đỏ, tím) chỉ dùng cho điểm quan trọng.
- Màu bão hòa nhất chỉ ở nơi hành động; nền dịu hơn.

**Mức chi tiết vẽ thật.**
- "Vẽ tay mà như thật": đá có vân, nứt, rêu; nước có phản chiếu; lá có khối sáng tối. Không phải hình phẳng có viền mực.
- Chi tiết gom thành khối lớn, đọc được ở cỡ nhỏ. Không nhiễu vụn.
- Nhân vật và nhà có thể "chibi" khối chắc (như Clash of Clans, Rise of Kingdoms), nhưng thế giới quanh chúng vẫn hùng vĩ. Đây là chìa khóa cho ba game của ta: model giữ khối chắc, thế giới và ánh sáng lên tầm.

**Màn tựa và ảnh chủ đạo bố cục thế nào.**
- Một khoảnh khắc, một điểm nhấn: anh hùng hay rồng ở một phần ba ảnh, mốc khổng lồ ở phần ba kia.
- Có chỗ trống yên cho logo (thường trên giữa hay trên trái) và cho menu (thường dưới trái).
- Logo là hình vẽ có chất liệu (kim loại, đá, ngọc), không phải chữ font trơn.
- Có bản ngang (màn tựa) và bản dọc (thẻ cửa hàng, cổng game).

**Khung UI và icon.**
- Khung có chất liệu thật (kim loại, đá, kính, sơn mài), viền và góc có chi tiết, lòng khung tối và đều để chữ đọc rõ.
- Icon vẽ có khối, ánh sáng, viền, trên nền đồng bộ; không emoji, không icon CSS.
- Mỗi trạng thái (thường, chọn, khóa) có hình khác nhau.
- Một hệ khung cho cả game: cùng vật liệu, cùng góc, cùng màu nhấn.

### 1.2 Camera nhìn xuống vẫn hùng vĩ thế nào

Wordwoven nhìn xuống 55° từ 58 m; Dragonhold nghiêng 40–75°. Ở các góc đó người chơi gần như không thấy chân trời. Game nhìn xuống trên chợ (Diablo IV, Rise of Kingdoms, Kingdom Rush) làm hùng vĩ bằng:
- **đất là tranh:** nhiều sắc, chất liệu thật, đường và sân đọc rõ; không phải bãi cỏ một màu;
- **mốc ngay mép sân:** vách đá, tượng, cổng, tháp đá cao lọt vào khung từ trên xuống;
- **mép thế giới:** sân đứng trên cao nguyên, mép là vực, thác đổ xuống biển mây;
- **bóng khổng lồ:** bóng mây và bóng quái thú trôi qua sân;
- **ánh sáng:** nắng xiên tạo bóng dài, sương thấp ở chỗ trũng, đèn sáng về đêm;
- **camera màn tựa và lúc hạ góc:** lúc đó mới thấy trời và phông xa, nên phông vẫn phải đạt.

### 1.3 Thang 0–10 (điểm M, mức chợ)

| Điểm | Nghĩa | Mốc |
|---|---|---|
| 10 | Ảnh chủ đạo hàng đầu thế giới | — |
| **9** | Thương mại cao cấp: quái thú khổng lồ, hẻm núi sâu, ánh sáng điện ảnh, HUD đầy đủ | **Ảnh mẫu của chủ dự án** |
| **8** | **Phát hành được (mức nhận).** Có mốc lớn, ít nhất ba tầng sâu và trời, ánh sáng có hướng, màu theo kịch bản, chi tiết hoàn thiện. Có thể thiếu "khoảnh khắc trầm trồ" | Chưa có ảnh nào của ta |
| 7 | Indie dễ chịu. Gọn, cùng bộ, có không khí; quy mô và ánh sáng thường; không có gì làm người chơi nhỏ lại | Cảnh trận Last Line (`arena/concept-fight.png`); bốn ảnh ải của phiếu 109 |
| 6 | Gọn mà chung chung. Ánh sáng phẳng, không mốc | Cảnh map Dragonhold ở góc nghiêng; phông `pine-river-far-015` |
| 5 | Tranh đẹp nhưng sai tầm: ấm cúng, quê, nhỏ, dễ thương | `title-dusk.png` của Wordwoven; huy hiệu 096 của Dragonhold |
| 4 | Hình phẳng như clip-art, viền mực, khối đồ chơi | Cảnh vật meadow v1, v2; phông `w1-silverfall` |
| 3 | Bản thử: màu phẳng, không chất liệu | Ô đất 095 của Wordwoven; sân 3D hôm nay |
| 0–2 | Hỏng, thiếu, khung gỡ lỗi | Bản 2D đĩa tròn và emoji của Wordwoven |

### 1.4 Cách chấm từ nay

- Mỗi ảnh có hai điểm: **M** (mức chợ, thang 1.3) và **Q** (5 tiêu chí của `ART_ACCEPTANCE.md` §2.2). Ảnh nhận khi **M ≥ 8 và Q ≥ 8**.
- Ảnh là một phần của cảnh (ô đất, ô phông, cây cảnh, mảnh sân) chấm M trên **ảnh ghép** dựng bằng script, không chấm lẻ.
- Mỗi phiếu có **tờ so với ảnh mẫu**: ảnh mới đặt cạnh ảnh mẫu của chủ dự án, cùng chiều cao, kèm một dòng "đứng cạnh được" hay "chưa".
- Người chấm thứ hai khi M ở 7,5–8,5, như luật cũ.
- Model 3D vẫn theo luật 7 điểm (Q). Điểm M của một cảnh 3D chấm trên ảnh chụp trong game.

---

## 2. Bible Wordwoven

### 2.1 Bản sắc

Giữ thế giới đá vôi lấy cảm hứng từ miền Bắc Việt Nam: tháp đá vôi Hạ Long và Tràng An, thác bạc, ruộng bậc thang như những bậc thang khổng lồ, đền đá cổ, hội đèn lồng. Nhưng nâng lên thành một **cõi huyền ảo hùng vĩ**: tháp đá cao hàng trăm mét, quái thú bay giữa các đỉnh (rùa trời mang phế tích trên mai, gợi từ Rùa Vàng), thời tiết mạnh (giông vỡ nắng, sương dày, mưa đèn lồng về đêm). Không còn làng quê ấm cúng: không nhà tranh, không cối xay gió, không đồi chè, không cầu vồng.

Hình nhận diện riêng: vòng trống đồng Đông Sơn (mặt trời mười sáu tia, chim lạc, sếu bay), mây cuộn, rồng thời Lý trên lan can đá. Không dùng hình tôn giáo (không tượng Phật, bàn thờ, lư hương, chuông chùa), theo TK §22.1.

Chủ đề "Wordwoven": chữ dệt thành ánh sáng. Sợi chỉ vàng nối tháp với tháp khi người chơi gõ; không bao giờ thành chữ đọc được trong ảnh.

### 2.2 Khối prompt (nguyên văn, prompt bắt đầu bằng các khối này)

**STYLE** (mọi ảnh cảnh: màn tựa, ảnh chủ đạo, trời, phông, cảnh vật, đất)
```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.
```

**STYLE-UI** (khung, bảng, nút, logo, huy hiệu; ở logo, câu cuối được thay bằng khối chữ logo)
```text
Premium high-fantasy game interface art for Wordwoven, a majestic realm inspired by northern Vietnam: carved pale limestone and polished dark jade lacquer, gold-leaf trim and fine bronze inlay, ornament drawn from Dong Son bronze-drum sun-star rings and cloud-scroll patterns, small cinnabar-red and lantern-amber accents. Crisp, finished and richly detailed like the interface of a top commercial fantasy game, with clean bevels, soft inner shadow and a subtle warm rim light, readable at small size. Shown flat and straight on, no perspective, no scenery. No text, letters, numbers, signature or watermark.
```

**MAP** (dán sau STYLE cho mọi thứ nằm trên sân 3D: cảnh vật, đất, decal)
```text
Asset for a 3D strategy game seen from a high camera looking 55 degrees down from 58 metres: every shape must read at that distance, so group detail into big masses with strong light-dark contrast, keep edges clean, and avoid fine noise, tiny scattered bits and thin strands.
```

**SCENERY** (cây cỏ, đá billboard; thay khối §3.2 cũ của `03-2d-scenery-ui-vfx.md`)
```text
Single scenery cut-out for a 3D game that shows plants and rocks as painted billboards: exactly one object, whole and complete, centred, its base at the bottom centre of the image, a small empty margin on every side. Seen from the front, a little above eye level, about 15 degrees down. Soft even light from the front and above: no cast shadow, no sun direction, each big mass a little darker on its underside. Natural, grand and believable rather than cute: no outline, no ink line, no cartoon shapes. No ground, no soil, no grass and no pebbles around the base: the base ends cleanly. No blur, no glow, no see-through parts, no thin strands, no tiny scattered leaves, no floating bits.
```

**MODEL** (ảnh nguồn Tripo cho mốc và nhà mới; xem phiếu 128, 129): khối chắc như model đang có, nhưng cổ, chạm khắc, sang; vật liệu đá vôi, đồng xanh rỉ, vàng lá, gỗ sơn son. Nguyên văn ở phiếu 128.

Các khối RING, SKY (phông vòng), GROUND, CLIFF (đất, vách), TOP (decal) nằm nguyên văn trong phiếu 114, 122, 123.

### 2.3 Luật màu

- **Bóng:** ngọc và xanh mòng két (teal), không đen. **Sáng:** vàng ấm. **Nước, sương:** bạc. **Đá:** trắng đá vôi, xám ấm.
- **Cỏ:** ngọc ngả teal (hue 80–150°), độ bão hòa trung vị ≤ 0,55. Không dùng xanh lá chuối, xanh nõn rực của bộ cũ.
- **Nhấn:** son đỏ (mái ngói, cờ), hổ phách đèn lồng. Chỉ dùng ở điểm nhỏ.
- **Đường và sân:** sáng hơn cỏ ít nhất 0,15 luma, để làn quái đọc rõ từ trên cao.
- Màu tín hiệu của game (xanh ngọc của chữ đang gõ, đỏ báo đòn, vàng đồng xu) không dùng thành mảng lớn trên nền.
- Không hồng tươi, tím tươi (để tách nền khóa màu `#FF00FF`).

### 2.4 Luật ánh sáng

- **Ngày** (Day 1–5): nắng chiều vàng, mặt trời cao 35–45°, đến từ một hướng cố định của thế giới (làn L chốt; mặc định tây nam). Bóng dài, rõ. Tia nắng qua mây ở trời. Bóng mây trôi qua sân.
- **Đêm** (Night 1–5): trăng lam bạc, thấp; đèn lồng hổ phách là nguồn sáng ấm (đèn trên nhà, đèn trôi trên trời). Sương dày hơn ngày.
- **Boss** (Mộc Tinh): trời và sương ngả màu boss 20 % (TK §23.8), có thể thêm chớp xa.
- **Ảnh 2D trên sân** (cây cảnh, đất) vẽ ánh sáng phẳng; game chiếu sáng chúng bằng cùng đèn với model. **Ảnh phông** chiếu từ trên và hơi sau người xem để lật ghép được.

### 2.5 Đọc được từ camera 55° ở 58 m

- Sân nhìn từ trên: mọi chi tiết nhỏ hơn 15 cm là nhiễu. Vẽ bằng mảng lớn.
- Ba lớp đọc: đường (sáng nhất), cỏ (vừa), rừng mép (tối nhất). Nhà và quái nằm trên nền vừa, nên luôn nổi.
- Mốc khổng lồ đặt **ngoài** sân (ngoài nửa cạnh 48 m) để không che làn, và **đủ cao** để lọt khung ở camera mặc định (tháp đá vôi 30–40 m, tượng 20 m).
- Thẻ chữ, chữ gõ và đòn đánh vẫn là thứ sáng nhất màn hình. Nền dưới thẻ chữ không sáng hơn luma 0,6.

### 2.6 Nên và không nên

| Nên | Không nên |
|---|---|
| Tháp đá vôi cao, thác bạc, sương, đền đá cổ, bậc thang đá, rồng thời Lý, trống đồng | Nhà tranh, vách tre, chòi gỗ quê, cối xay gió, đồi chè, cầu vồng, cột đèn biển sọc đỏ trắng |
| Cây bàng cổ thụ, thông núi đá, tre gai cao, lau bạc, dã quỳ, sim | Cây tròn như kẹo bông, bụi dâu tây, hoa cúc hoạt hình |
| Vẽ tay mà như thật, khối lớn, không viền mực | Viền mực đen đều, tô màu phẳng, khối tròn đồ chơi |
| Ánh nắng xiên, bóng dài, sương thấp, tia nắng | Ánh sáng phẳng đều khắp, không bóng |
| Quái thú trời khổng lồ, bóng của nó trôi qua sân | Trời trống chỉ có mây bông |
| Khung UI sơn mài ngọc, đá vôi chạm, vàng lá, đồng | Giấy kem, gỗ tre, bảng CSS phẳng, emoji |

### 2.7 Model 3D: giữ và chỉnh ánh sáng

Model Wordwoven (chủ dự án đếm 117; `art-src/3d` có 159 file GLB kể cả bản phụ) là đồ họa vẽ tay khối chắc, màu tươi, kiểu "đồ chơi vinyl" (xem `games/.wt-td-1c/tmp/lane-l/td-1c-models-sheet.jpg`). Giữ hết. Cho chúng sống chung với nền sử thi bằng một **StylePack mới "Epic"**, thay StylePack "Sách tranh" (TK §23.12) ở `src/view/3d/stage.ts` của làn L:

| Mục | Sách tranh (hôm nay) | Epic (mới) |
|---|---|---|
| Tone map | Neutral, bão hòa ×1,15 | Filmic (ACES hay AgX), bão hòa ×0,95; màu đồ chơi gắt nhất (vàng rơm, cam) giảm thêm 10–15 % bằng uniform theo vật liệu |
| Nắng chính | `#fff0d2` 2,6, cao vừa | Vàng ấm `#ffdca8`, cao 35–45°, mạnh hơn; bóng 2048 (High) sắc, dài |
| Ánh trời | Hemisphere `#e4eefc` / `#7a8a55` 1,35 | Trời ngọc `#a9d2d6`, đất teal tối `#33463c`, yếu hơn, để bóng ngả teal |
| Viền | Không | Đèn ngược lạnh trắng 0,4 từ phía đối nắng; rim 15 % trong shader billboard |
| Che sáng | — | SSAO hay GTAO ở High; đốm bóng tiếp đất ở Medium |
| Sương | Fog mờ sữa 170–420 m | Sương theo độ cao + theo khoảng cách, màu lấy từ dải sương của phông 114 (ngày vàng bạc, đêm teal tối) |
| Bóng mây | — | Texture mây trôi nhân 0,75–0,85 trên đất; bóng rùa trời (114 `sky-beast-top`) trôi qua sân mỗi Ngày một lần |
| Bloom | 0,25 | 0,35, chỉ trên đèn lồng, VFX, chữ (ngưỡng cao) |
| Phân màu | Tách tông nhẹ, sữa | Bóng teal, sáng vàng; vignette 0,15 |
| Đêm | — | Trăng lam `#9fb4ff` thấp; ≤ 8 đèn điểm cho đèn lồng và cửa sổ; cửa sổ nhà phát sáng nếu model có mặt nạ |
| Billboard cảnh | Viền mực chuẩn bằng script | Tắt viền mực cho bộ v3, v4; giữ ramp 3 bậc, đáy tối 25 %, rim 15 % |

Đo lại ngân sách khung và draw call của C0 §6 sau khi đổi (SSAO và đèn ngược tốn thêm).

### 2.8 Model lệch hướng (dựng lại sau, phiếu 129)

Chỉ ghi ở đây. Không dựng lại khi chưa có ý chủ dự án. Hôm nay chỉnh ánh sáng và giảm màu là đủ cho bản chơi thử.

| Model | Vì sao lệch | Ưu tiên |
|---|---|---|
| `buildings/archer` (Archer Tower) và bộ cấp `kits/archer-kit-l2`, `-l3` | Mái tranh rơm, chòi gỗ | P2, map 1 dùng |
| `buildings/barracks`, `barracks-v2` (Barracks) và `kits/barracks-kit-l2`, `-l3` | Mái tranh, vách tre | P2, map 1 dùng |
| `buildings/farm`, `farm-ao-ca`, `farm-nuong` (Rice Field) và `kits/farm-kit-l2`, `-l3` | Chòi tranh, bù nhìn | P2, map 1 dùng |
| `landmarks/choi-canh-doi` (Lookout) | Chòi tranh | P2, map 1 dùng |
| `buildings/lumber` (Lumber Camp), `buildings/infirmary` (Herb House) | Mái tranh | P3 |
| `landmarks/nha-rai-da` | Nhà sàn mái tranh | P3 |
| `landmarks/hai-dang` | Hải đăng sọc đỏ trắng, lạc thế giới | P3 |
| `heroes/lam` (Lam) | Mèo ninja áo hoodie, giày thể thao: đồ đường phố hiện đại | P3 (chỉ hộp cát) |
| `animals/piggy` | Heo đất (ống heo) dễ thương | P3 |
| `props/rao-tre`, `landmarks/cau-tre` | Rào, cầu tre quê | P3; giữ được nếu chỉ thấy nhỏ |

Giữ, chỉ chỉnh ánh sáng: Fort (`keep` và bộ cấp: đá trắng, mái ngói đỏ, hợp hướng mới), Cannon Tower, Gold Mine, Seal Dais, Calligraphy Tower (`scribe`), cầu gỗ, vách thác, gốc đa, Draconis, Mộc Tinh, mọi loài quái, lính, thợ, Thư Đồng, Tre (cần xem lại khi có ý chủ dự án), đạn, đồ rơi.

---

## 3. Bible Dragonhold

### 3.1 Bản sắc

Một **ải núi có rồng giữ**: thung lũng xanh sâu, sông chảy xiết qua cầu đá cũ, hai bên là vách đá hoa cương khổng lồ và đỉnh tuyết. Ngang ải là cổng pháo đài cổ ("the Hold"), tượng rồng khổng lồ tạc vào vách. Rừng thông leo lên sườn núi; sương sớm đọng trong thung. Bầy héo màu tím xám bò ra từ rừng. Hỏa Long đỏ cam canh cổng.

Giữ của bộ cũ: rừng thông, sông và cầu, lính rêu, sói héo, màu tím xám của bầy héo, rồng đỏ cam. Bỏ: đồi thông dịu không có mốc, trời kem phẳng, rồng con dễ thương.

### 3.2 Khối prompt (nguyên văn)

**STYLE**
```text
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
```

**STYLE-UI**
```text
Premium high-fantasy game interface art for Dragonhold, a mountain pass guarded by a fire dragon: weathered cream granite and dark forged iron, hammered gold trim, ember-orange enamel and glowing dragon-fire accents, carved dragon-scale and pine-bough ornament, small muted-violet accents. Crisp, finished and richly detailed like the interface of a top commercial fantasy strategy game, with clean bevels, soft inner shadow and a subtle warm rim light, readable at small size. Shown flat and straight on, no perspective, no scenery. No text, letters, numbers, signature or watermark.
```

**MODEL** (ảnh nguồn Tripo; nguyên văn cùng khối TAIL ở phiếu 124)
```text
Image-to-3D source picture of ONE object for a stylized 3D fantasy strategy game; it will become a static 3D model. Stylized hand-painted 3D game art for Dragonhold, an epic mountain pass guarded by a fire dragon, like a premium hand-painted 3D game asset: weathered cream granite, dark forged iron, old timber and pine, hand-painted textures with visible brush strokes, big confident shapes with a few large details instead of many small ones, a silhouette that still reads from a high top-down camera, grand and ancient rather than cute; matte surfaces, no glossy shine.
```

### 3.3 Luật màu và ánh sáng

- **Bóng:** xanh thông sẫm, lam đá phiến. **Sáng:** vàng bình minh, cam than hồng của lửa rồng. **Đá:** hoa cương kem. **Nhấn:** tím xám của bầy héo.
- **Luật tín hiệu cũ giữ nguyên trên sân:** đỏ, cam, vàng, xanh ngọc tươi không thành mảng lớn trên map và model (dành cho lửa rồng, báo đòn, vàng). Ảnh màn tựa và ảnh chủ đạo được dùng cam vàng của bình minh và lửa thoải mái, vì không có trận trên đó.
- **Ánh sáng map:** bình minh, nắng cao 25–35°, xiên dọc thung lũng để vách đá đổ bóng dài; sương theo độ cao đọng ở lòng sông; viền ấm trên vách. Không có đêm ở map 1.
- **Cỏ:** bỏ màu cỏ sân bóng tươi của bản A2; ngả xanh thông và ô liu, có mảng vàng nắng.

### 3.4 Nên và không nên

| Nên | Không nên |
|---|---|
| Vách hoa cương cao, đỉnh tuyết, cổng và tường ải, tượng rồng tạc vách, thác mảnh | Đồi thoải không mốc, công viên cỏ xanh tròn trịa |
| Rồng lớn, dữ, trưởng thành | Rồng con dễ thương |
| Bình minh, bóng dài, sương trong thung | Trời kem phẳng, ánh sáng đều |
| Sắt rèn, hoa cương, vàng búa, men cam | Gỗ mộc, lá cây làm mái (trừ Herb Hut đã có) |

### 3.5 Model và map

- **Model đang có giữ hết** (vẽ tay khối chắc, kiểu Warcraft; hợp hướng mới): lính rêu, sói héo, ong gai, kiến gai, cờ rêu, Grove Warden, Herb Hut, ba bẫy, bộ kit3 (đèn, rào, vách đá, cầu tàu, cỏ). Herb Hut mái lá hơi dễ thương; giữ, chỉnh màu.
- **Thiếu mốc:** cổng ải, tường ải, tháp canh, tượng rồng, vòm đổ, lò lửa. Phiếu 124 vẽ ảnh nguồn; chủ dự án dựng 6 model Tripo.
- **Làn R (map):** đặt cổng và tường ải ở đầu ải, sau Dragon Platform; vách hai bên cao gấp đôi; tượng rồng trên vách; đổi bảng màu đất (`paint.ts` `PINE_RIVER_GROUND`) sang thông và ô liu; nắng thấp, sương theo độ cao; camera màn tựa hạ thấp 12–20° quay quanh map, phía sau là trời và phông của phiếu 120.

---

## 4. Last Line: bước ý tưởng, rồi bible

### 4.1 Vì sao cần bước ý tưởng

Hôm nay nhân vật chính là tàu Vanguard (model của Space Typing), nhỏ ở đáy màn hình, không mặt, không tính cách. Hành lang thép trống, sọc cảnh báo cam đen, UI là chữ trên bảng xám. Chủ dự án cho phép bỏ tàu. Game gõ chữ là thị trường hẹp, nên cảm giác gõ phải đẹp và cuốn: chữ đang gõ phải biến thành đòn đánh nhìn thấy được.

Luật chơi không đổi. Mọi hướng dưới đây giữ: một làn thẳng, nhân vật đứng giữa đáy, hai bến súng hai bên (Bay 1, Bay 2), năm súng (Pulse Gun, Heat Beam, Scatter Gun, Rail Gun, Star Mortar), bầy quái tràn xuống, Armor, Rift, các ải. Chỉ đổi vỏ: view, model, UI, âm.

### 4.2 Ba hướng

| | **A · Iron Warden** | **B · Lightbearer** | **C · Rampart** |
|---|---|---|---|
| Nhân vật chính | Warden: người máy chiến đấu đi bộ cao 6 m, giáp than chì sọc cam, buồng lái xanh có phi công, hai pháo tay | Một vệ binh mặc giáp trắng vàng và than chì, áo choàng xanh sẫm dài, mũ có kính sáng lam; hai súng canh (sentinel) bay hai bên vai | Thành lũy khổng lồ chắn hành lang cuối; hai tháp pháo trên tường; người chỉ huy áo dài đứng giữa |
| Nơi chốn | Đường đắp thép công nghiệp của trạm VC-7, cần cẩu, tay cập cảng, hố đen sau cùng | Đường đắp khổng lồ bằng thép tối và đá cổ màu nhạt ở mép hố đen; vòng trạm vỡ, khối đá nghiêng trôi | Tường thành cắt ngang hành lang trạm; tháp súng, vòm khiên |
| Họ quái | Bầy Hố Đen: côn trùng cơ sinh học, vỏ kitin đen, gân cam (như hôm nay) | Hollow Swarm: sinh vật hư không bằng kính đen, vết nứt cam phát sáng; phía sau là quái vật hư không khổng lồ trồi lên từ hố đen | Bầy Hố Đen leo tường, tràn hành lang |
| Gõ chữ thành đòn | Mỗi chữ cái sáng một đốt trên ray nạp đạn dọc cánh tay; đủ từ thì cánh tay giật lùi và bắn | Mỗi chữ cái là một ký hiệu sáng bay từ bàn tay giơ lên vào súng canh, xếp thành vòng quanh nó; đủ từ thì súng bắn cả vòng ký hiệu thành loạt sáng; chuỗi dài thì áo choàng và kính sáng dần; gõ sai thì ký hiệu nứt, rơi thành tia lửa | Mỗi chữ cái là một dòng mã bắn chạy dọc nòng pháo; đủ từ thì tháp nã |
| Ngôn ngữ khung UI | Thép công nghiệp, đinh tán, sọc cảnh báo, chữ hổ phách | Kính khói tối, chỉ vàng trắng mảnh, đường chòm sao, ký hiệu ở góc; thẻ súng như tấm bia cổ vật | Màn chiến thuật quân sự, lưới, vạch đo |
| Khoảnh khắc chính | Người máy quỳ một gối, cánh tay Rail Gun xẻ một đường cháy xuyên bầy | Quái vật hư không trồi lên từ hố đen sau bầy, bóng của nó phủ đường đắp; vệ binh giơ tay, hai súng canh cùng bắn | Cả bức tường nã một loạt khi một đợt quái vỡ qua mép |
| Điểm M (dự đoán khi làm tốt) | **8**: đã có trên chợ, đọc rõ, hợp hai pháo tay; nhưng chung chung, ít cảm xúc | **9**: khớp ảnh mẫu (anh hùng áo choàng nhìn từ sau, quái thú khổng lồ trên trời); huyền thoại như Destiny; "chữ thành ánh sáng" rất riêng cho game gõ chữ | **7**: hoành tráng nhưng không có nhân vật để yêu; thủ thành bằng tháp pháo là dạng phổ biến |
| Giá 3D | 1 người máy + 5 mô-đun tay (Tripo, cứng, dễ) | 1 nhân vật người (Tripo có rig người; áo choàng cần xương phụ hoặc shader vải) + 5 súng canh (cứng, dễ); quái đổi vỏ bằng shader đám đông, không model mới; quái vật hư không là tấm 2D | 1 bức tường + 2 tháp pháo + 1 người chỉ huy |
| Rủi ro | Giống nhiều game người máy khác | Trộn huyền ảo và viễn tưởng phải giữ tay; nhân vật người cần clip (đứng, bắn trái, bắn phải, bị đánh, quỳ) | Camera sau tường khó thấy "người chơi" |

Giữ tàu (hôm nay) chấm 6,5–7: không phải "rõ ràng tốt nhất", nên không đề xuất giữ.

**Đề xuất: B · Lightbearer.** Lý do:
1. Bố cục trận của game (camera sau và trên nhân vật, nhìn dọc làn về hố đen) chính là bố cục ảnh mẫu của chủ dự án: anh hùng áo choàng nhìn từ sau, đối mặt quái thú khổng lồ.
2. "Chữ thành ánh sáng" cho cảm giác gõ đẹp nhất: mỗi phím có một ký hiệu bay vào súng, mỗi từ là một loạt bắn.
3. Hai súng canh bay hai bên vai khớp đúng hai bến súng; đổi súng là đổi súng canh, model riêng, dễ đọc.
4. Quái giữ dáng hiện có, chỉ đổi vật liệu (kính đen, nứt cam): rẻ.

**Phiếu 112** vẽ mỗi hướng hai ảnh 1536 × 1024 (cảnh trận từ camera game, ảnh chủ đạo). Chủ dự án chọn từ `games/typing-survival/art-src/_review/112-directions.jpg`.

### 4.3 Bible Last Line (hướng B, **chủ dự án chọn 29/10**)

Chủ dự án chọn hướng B · Lightbearer ngày 29/10/2026 sáng. Các phiếu 121, 125, 126, 127 và ảnh nguồn Tripo (phiếu 156) chạy theo mục này.

**STYLE**
```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
```

**STYLE-UI**
```text
Premium science-fiction game interface art for Last Line: dark smoked glass over graphite steel, fine white-gold filigree lines, thin constellation lines and small glyph marks at the corners, electric cyan and orange-gold light accents, a faint inner glow. Crisp, finished and richly detailed like the interface of a top commercial sci-fi action game, with clean bevels and sharp edges, readable at small size. Shown flat and straight on, no perspective, no scenery. No text, letters, numbers, signature or watermark.
```

Khối ARENA (mảnh sân) nguyên văn ở phiếu 125; khối CONCEPT STYLE và ba khối hướng ở phiếu 112.

**Luật màu:**
- Nền: navy vũ trụ và than chì, tối. Sáng: đĩa bồi tụ cam vàng ở cuối làn.
- Phe ta (nhân vật, súng canh, đạn): lam điện và trắng vàng. Phe quái: kính đen, nứt cam; Pack Leader nứt vàng kim; Shield Guard khiên lam (theo phiếu 089).
- Tím chỉ là nhấn nhỏ ở hư không và Rift.

**Luật ánh sáng:**
- Đèn chính là **ngược sáng** từ đĩa bồi tụ, chiếu về phía camera: mọi hình có viền sáng.
- Nhân vật được chiếu thêm bởi ánh lam của súng canh.
- **Sàn dưới dòng chữ luôn tối** (luật 088 và `FEEL_PASS_S1.md` §4.1 của game: nền dưới dòng chữ chỉ được sáng thêm 0,02). Hố đen, đèn mép, VFX là nơi sáng.

**Nên và không nên:**

| Nên | Không nên |
|---|---|
| Nhân vật áo choàng nhìn từ sau, súng canh bay, ký hiệu sáng | Tàu nhỏ không mặt |
| Đường đắp đá cổ và thép, vòng trạm vỡ, khối đá nghiêng, quái vật hư không khổng lồ | Hành lang công nghiệp trống, sọc cảnh báo cam đen khắp nơi |
| Kính khói, chỉ vàng trắng, chòm sao | Bảng xám phẳng toàn chữ |
| Ngược sáng, viền sáng, bụi trong vệt sáng | Sàn ướt bóng như ảnh chụp (`title-horizon.png`) |

**Model:**
- Tripo (chủ dự án): nhân vật Lightbearer (rig người: đứng, lướt trái phải, giơ tay bắn trái, bắn phải, bị đánh, quỳ, đứng dậy, thắng); 5 súng canh, mỗi súng một dáng theo icon súng có sẵn (`art-src/ui/icons/gun-*.png`).
- Quái: giữ lưới hiện có, đổi vật liệu chung "Bầy Hố Đen" trong `src/view/crowd.ts` thành kính đen có nứt cam.
- Quái vật hư không: tấm 2D có alpha (phiếu 125), trôi chậm trong hố đen.
- View chỉ đổi vỏ: tư thế lắc và lướt của tàu (`ship-rules.ts`) thành lướt và giật của nhân vật; socket nòng súng chuyển sang súng canh. Sim và ván vàng giữ nguyên.

---

## 5. Chấm lại ảnh hiện có

Tờ so (ảnh mẫu đặt cạnh ảnh của ta, có nhãn điểm):
- `games/typing-defense/tmp/art-direction/sheet-wordwoven-vs-ref.jpg`
- `games/dragon-hold/tmp/art-direction/sheet-dragonhold-vs-ref.jpg`
- `games/typing-survival/tmp/art-direction/sheet-lastline-vs-ref.jpg`

### 5.1 Wordwoven (48 ảnh: giữ 0, làm lại 48)

| Ảnh | M | Vì sao | Mức |
|---|---:|---|---|
| `ui/title-dusk.png` | 5 | Hoàng hôn đẹp, có tháp đá xa, nhưng nhà tranh, tre, đường làng: đúng "thôn quê"; không mốc, không nhân vật, không chỗ logo | Làm lại (113) |
| `backdrops/w1-silverfall/sky-a.png`, `sky-a.v1.png` | 4,5 | Cầu vồng và mây bông như sách thiếu nhi; trời phẳng, không tia nắng | Làm lại (114) |
| `sky-b.png` | 4,5 | Mây bông đều, không kịch | Làm lại (114) |
| `layer-320.png`, `layer-320.v1.png` | 4,5 | Núi xa dịu nhưng thấp, nhỏ, không tầng | Làm lại (114) |
| `layer-220.png` | 4,5 | Đồi tròn có vách đá nhỏ, như đồ chơi | Làm lại (114) |
| `layer-140-a.png` | 3,5 | Đồi chè và cối xay gió: lạc thế giới, quê | Làm lại (114) |
| `layer-140-b.png` | 3,5 | Đồi chè tròn trịa, phẳng | Làm lại (114) |
| Cảnh vật `almond-tree`, `bamboo-clump`, `canopy-block`, `fern`, `reed-clump`, `tall-grass`, `rotten-log`, `rock-small`, `tree-stump` (v1, v2) | 4–4,5 | Hình dán khối tròn, viền mực đều, màu tươi: clip-art cho trẻ em | Làm lại (116–118) |
| `mountain-pine`, `rock-medium` (v1, v2) | 5 | Dáng khá hơn, nhưng vẫn viền mực, phẳng | Làm lại (116, 118) |
| `raspberry-bush`, `wildflowers` (v1, v2) | 4 | Dâu tây và cúc hoạt hình, không phải cây miền núi Việt | Làm lại (117) |
| Ô đất 095 `grass-a`, `grass-b-clover`, `dirt-road` | 3,5 | Xanh lá cây phẳng như sân bóng, đường vàng cam như đồ chơi; trên sân 3D là thứ chiếm cả màn hình | Làm lại (122) |
| Ô đất 095 `trail-worn` | 4 | Như trên | Làm lại (122) |
| Ô đất 095 `stream-bank`, `stone-yard` | 5 | Chất liệu được, màu dịu, nhưng vẫn phẳng, không hợp bộ mới | Làm lại (122) |
| Decal 097 `ground-decals-a`, `-b` | 4,5 | Vết đất vàng phẳng; tờ b có viền mực | Làm lại (123) |
| Ô ruộng 098 (5 trạng thái) | 5 | Hàng lúa đều, đọc được, nhưng màu rực, như vẽ tay trẻ em | Làm lại (123) |

Ngoài danh sách: sân 3D hôm nay (C3, bãi cỏ xanh một màu với đường vàng) chấm 3. Đất mới (122), cảnh vật mới (116–118), mốc (128) và StylePack Epic (2.7) là cách sửa.

### 5.2 Dragonhold (9 ảnh: giữ 0, làm lại 9)

| Ảnh | M | Vì sao | Mức |
|---|---:|---|---|
| `backdrops/pine-river-far-015.png` | 6 | Vẽ dịu, cùng bộ, có sương; nhưng đồi thông chung chung, không ải, không mốc, trời kem phẳng | Làm lại (120) |
| `pine-river-far-015.v1.png`, `pine-river-far.png`, `pine-river-far.v1.png`, `pine-river-far.seamless.png` | 5,5 | Như trên, ít tầng hơn | Làm lại (120) |
| `ui/title/title-emblem` (096) | 5,5 | Sạch, hoàn thiện, nhưng là rồng con dễ thương trên vòm đá nhỏ: mascot, không hùng | Làm lại (119) |
| `ui/title/title-logo` (096) | 3 | Chữ "Rồng Giữ Ải": tên cũ, nay game là Dragonhold; chữ đẹp nhưng kiểu sách tranh | Làm lại (119) |
| Map L2-cau A2, camera mặc định, 1920 (`a2-1920x1080-default-compare.jpg`) | 6,5 | Sạch, đọc rõ, cây vẽ tay đẹp; nhưng như công viên: cỏ xanh sân bóng, không ải, không pháo đài, ánh sáng không kịch | Làm lại: ánh sáng và màu (làn R), phông 120, mốc Tripo 124 |
| Map L2-cau A2, 12 góc 40/55/75° (`a2-1920x1080-contact-sheet.jpg`, cùng bản 1280) | 6–6,5 | Như trên; góc 75° còn phẳng hơn | Làm lại như trên |

Model kit3 (`kit3-models-sheet.jpg`): model, chấm theo luật 3D (Q từ 7): giữ.

### 5.3 Last Line (10 ảnh: giữ 0, làm lại 10)

| Ảnh | M | Vì sao | Mức |
|---|---:|---|---|
| `arena/concept-fight.png` (088) | 7 | Không khí mạnh, sâu, hố đen đẹp; nhưng hành lang công nghiệp trống, đối xứng, không mốc ngoài hố đen, không nhân vật | Làm lại sau khi chọn hướng (125) |
| `arena/far-structures.png` (088) | 6,5 | Bóng xa tối, dùng được; dáng chung chung | Làm lại (125) |
| `arena/hull-left.png`, `hull-right.png` (088) | 6 | Tấm thép tối, phẳng, lặp | Làm lại (125) |
| `arena/deck-decals.png` (088) | 6 | Dùng được; mũi tên chữ V là lối mòn | Làm lại (125) |
| Màn tựa đang chạy (`tmp/map1-audit/sheets/sheet-screens-1920x1080.jpg`) | 6,5 | Hố đen 3D ấn tượng; nhưng menu là bảng chữ, tàu nhỏ, sàn trống, chữ tiếng Việt | Làm lại (112 chọn hướng, 121, 127) |
| `ui/stages/c1-s1` … `c1-s4` (109, đã giao 29/10) | 7 | Chi tiết dày, màu mạnh; nhưng cả bốn ảnh cùng một bố cục đối xứng, nhiễu, và vẽ tàu của hướng cũ | Dùng tạm; làm lại sau khi chọn hướng (126) |

---

## 6. Phiếu Codex mới (112–129)

Luật chung của mọi phiếu: ghi vào `art-src` với tên mới, không ghi đè; khối STYLE nguyên văn; ảnh mẫu của chủ dự án; danh sách khổ; kiểm bắt buộc (md5 trước và sau, khổ, alpha sạch khi cần, tờ so với ảnh mẫu, KA5 mức chợ M và Q); tối đa 3 lượt mỗi ảnh; mọi chữ trong ảnh là tiếng Anh. Điều phối viên xếp phiếu vào `docs/CODEX_QUEUE.md`.

| Thứ tự | Phiếu | Game | Ảnh | Nội dung | Ghi chú |
|---:|---|---|---:|---|---|
| 1 | [112](../codex-queue/112-ts-concept-directions.md) | Last Line | 6 | Ảnh ý tưởng ba hướng: cảnh trận và ảnh chủ đạo mỗi hướng | Chủ dự án chọn hướng từ tờ `112-directions.jpg` |
| 2 | [113](../codex-queue/113-td-title-keyart.md) | Wordwoven | 5 | Nền màn tựa, ảnh chủ đạo (Draconis và Tree Spirit), ảnh dọc, logo "Wordwoven", huy hiệu | Logo kiểm chính tả từng chữ |
| 3 | [114](../codex-queue/114-td-sky-backdrops.md) | Wordwoven | 9 | Trời ngày a, b; trời đêm hội đèn lồng; vòng 320, 220, 140-a, 140-b; rùa trời và ảnh nhìn từ trên cho bóng | Cùng luật ghép vòng của bộ cũ |
| 4 | [115](../codex-queue/115-td-ui-frames.md) | Wordwoven | 9 | Bảng lớn, dải HUD, nút và nút chọn, băng rôn, chú thích, vòng chân dung, huy hiệu đầu bảng, gạch ngang | Thay 110 đã rút; 9-slice |
| 5 | [116](../codex-queue/116-td-scenery-trees.md) | Wordwoven | 8 | Cảnh vật v3, v4: bàng, thông núi, tre gai, khối tán | Viết lại 106 (phần 1) |
| 6 | [117](../codex-queue/117-td-scenery-understory.md) | Wordwoven | 10 | Cảnh vật v3, v4: dương xỉ, lau, cỏ voi, dã quỳ và huệ, sim | Viết lại 106 (phần 2) |
| 7 | [118](../codex-queue/118-td-scenery-rocks.md) | Wordwoven | 8 | Cảnh vật v3, v4: đá vôi vừa và nhỏ, khúc gỗ, gốc cây | Viết lại 106 (phần 3) |
| 8 | [119](../codex-queue/119-dh-title-keyart.md) | Dragonhold | 5 | Nền màn tựa, ảnh chủ đạo (Hỏa Long trên cổng ải), ảnh dọc, logo "Dragonhold", huy hiệu | Thay chữ logo 096 |
| 9 | [120](../codex-queue/120-dh-sky-backdrops.md) | Dragonhold | 6 | Trời bình minh a, b; đỉnh tuyết, vách tượng rồng, cổng ải, sườn thông | Cho camera màn tựa và màn kết quả |
| 10 | [121](../codex-queue/121-ts-menu-backgrounds.md) | Last Line | 7 | Nền màn chính, thẻ ải, nạp súng, hành trình, thắng, thua; logo "Last Line" | **Chờ chọn hướng** |
| 11 | [122](../codex-queue/122-td-ground-cliffs.md) | Wordwoven | 8 | Ô đất v2 (cỏ ngọc, cỏ rêu, đường đá lát cổ, mép đường, bờ suối, sân đá) và hai ô vách đá vôi | Đất chiếm cả màn hình ở camera chơi |
| 12 | [123](../codex-queue/123-td-decals-rice.md) | Wordwoven | 7 | Hai tờ decal v2, năm ô Rice Field v2 | Sau 122 |
| 13 | [124](../codex-queue/124-dh-landmarks-tripo.md) | Dragonhold | 6 | Ảnh nguồn Tripo: cổng ải, tường ải, tháp canh, tượng rồng, vòm đổ, lò lửa | **Chủ dự án dựng Tripo** |
| 14 | [125](../codex-queue/125-ts-arena-kit.md) | Last Line | 8 | Bộ sân v2: sàn, mép, hai tường, vòng xa, hố đen, quái vật hư không, decal | **Chờ chọn hướng** |
| 15 | [126](../codex-queue/126-ts-stage-art-v2.md) | Last Line | 4 | Bốn ảnh ải v2 | **Chờ chọn hướng**; thay 109 |
| 16 | [127](../codex-queue/127-ts-ui-frames.md) | Last Line | 9 | Khung UI: bảng lớn, thẻ bến súng, tấm chữ gõ, dải HUD, nút, băng rôn, vòng chân dung, gạch ngang | **Chờ chọn hướng** |
| 17 | [128](../codex-queue/128-td-landmarks-tripo.md) | Wordwoven | 5 | Ảnh nguồn Tripo: tượng tướng đá, cổng đá ba vòm, tháp đèn đá, tháp đá vôi có đình, bậc thang rồng | **Chủ dự án dựng Tripo** |
| 18 | [129](../codex-queue/129-td-rebuild-tripo.md) | Wordwoven | 6 | Ảnh nguồn Tripo để dựng lại sáu công trình mái tranh | **Chỉ khi chủ dự án đồng ý dựng lại** |

Ghi chú cho điều phối viên:
- 112, 113, 114 đã commit trước (`db06cbcb`) để làn ảnh M chạy ngay.
- Các phiếu Last Line 121, 125, 126, 127 nằm chờ tới khi chủ dự án chọn hướng. Trong lúc chờ, làn ảnh chạy 113–120, 122–124, 128.
- Phiếu 109 (đã giao): đề xuất **nhận làm ảnh tạm** (7/10, vẽ tàu của hướng cũ) để thẻ ải không trống, rồi thay bằng 126.
- Icon và hình nhỏ từng ô thuộc lượt rà hình UI (`docs/games/map1/UI_IMAGERY.md`, `UI_IMAGERY_CODEX.md`). Lúc tôi viết, hai file đó chưa có. Phiếu 115 và 127 chỉ làm khung; lượt rà hình UI dùng STYLE-UI ở mục 2.2 và 4.3 cho icon.

---

## 7. Model: chỉnh ánh sáng và dựng lại

### 7.1 Chỉnh ánh sáng (không tốn tiền, làn Claude)

| Game | Làm gì | Ai, ở đâu |
|---|---|---|
| Wordwoven | StylePack "Epic" theo bảng 2.7 cho mọi model 3D và billboard; tắt viền mực billboard v3, v4; sương lấy màu phông 114; bóng mây và bóng rùa trời | Làn L, `src/view/3d/stage.ts` và shader billboard (C2, C9) |
| Dragonhold | Nắng bình minh thấp 25–35° xiên dọc thung; sương theo độ cao; đổi bảng màu đất sang thông và ô liu; viền ấm trên vách; camera màn tựa thấp | Làn R, `src/view/stage.ts`, `paint.ts`, `maps/scene.ts` |
| Last Line | Ngược sáng từ đĩa bồi tụ; viền sáng trên quái; vật liệu đám đông kính đen nứt cam (hướng B) | Làn T hay V, `src/view/scene.ts`, `crowd.ts` (sau khi chọn hướng) |

### 7.2 Dựng lại hay dựng mới (tốn credit Tripo, chủ dự án dựng tay trên web)

| Game | Model | Số | Phiếu ảnh nguồn | Khi nào |
|---|---|---:|---|---|
| Dragonhold | Cổng ải, tường ải, tháp canh, tượng rồng, vòm đổ, lò lửa | 6 | 124 | Sau khi 124 được nhận |
| Wordwoven | Tượng tướng đá, cổng đá, tháp đèn, tháp đá vôi có đình, bậc thang rồng | 5 | 128 | Sau khi 128 được nhận |
| Last Line | Nhân vật chính + 5 súng canh (hướng B), hay người máy + 5 mô-đun (A), hay tường + 2 tháp + chỉ huy (C) | 4–6 | Viết sau khi chọn hướng (dùng ảnh 112 làm mẫu) | Sau khi chủ dự án chọn |
| Wordwoven | Archer Tower, Barracks, Lumber Camp, Herb House, Rice Field, Lookout (mái tranh → đá và ngói), kèm bộ cấp | 6 (+ bộ cấp) | 129 | Chỉ khi chủ dự án đồng ý (P2) |

Ước chừng 30 credit một model (đợt 4: 2 model, 60 credit): 17 model mới khoảng 510 credit; thêm 6 nhà dựng lại khoảng 180 credit, chưa tính bộ cấp. Chủ dự án có khoảng 4.000 credit web.

---

## 8. Phủ phản hồi (VFX và tiếng) theo sự kiện

Chủ dự án 29/10: mọi chi tiết có hình, có tiếng, có VFX: từ chữ đang gõ tới đòn đánh, chiêu và từng tiếng nhỏ, kể cả quái. Bảng dưới liệt kê từng sự kiện: lớp VFX (theo `VFX_STANDARD.md` §3: năm pha **A** gồng, **R** phát ở người ra đòn, **T** bay, **I** trúng, **F** dư âm; UI theo lớp mở, chạm, đóng), tiếng, hôm nay có gì, và bible đòi gì.

**Hiện trạng tiếng (cả ba game):** mọi tiếng là **tổng hợp bằng mã WebAudio**, chưa có file âm nào (`games/dragon-hold/docs/audio/M0_SOUND_LIST.md`, `games/typing-defense/docs/audio/THEME_SOUND_LIST.md`, `games/typing-survival/docs/audio/THEME_SOUND_LIST.md`). File thật làm qua `docs/games/AUDIO_PIPELINE.md` (Audio Lab, Stable Audio 3). Lượt rà hình UI và âm của agent khác sẽ ghi trạng thái âm chi tiết ở `docs/games/map1/UI_IMAGERY.md`; lúc viết, file đó chưa có, nên cột "Hôm nay" dưới đây lấy từ ba danh sách âm và kiểm kê map 1. Ở Wordwoven, tiếng phím đúng và sai giữ tổng hợp (TK §24.6: bắt đầu dưới 20 ms); hai game kia được dùng file nếu đầu file không có lặng.

Ký hiệu cột "Hôm nay": **có** (đủ hay gần đủ), **thiếu pha** (có nhưng chưa đủ năm pha hay chưa qua giám khảo), **chưa** (không có), **synth** (tiếng tổng hợp, chưa có file).

### 8.1 Dragonhold

| Sự kiện | VFX bible đòi | Tiếng bible đòi | Hôm nay (VFX · tiếng) |
|---|---|---|---|
| Phím đúng | Chữ trên thẻ lóe vàng than, một tia lửa nhỏ bay từ chữ về miệng Hỏa Long (A của đòn chữ) | Tách gỗ khô ngắn, cao độ lên theo chữ | có (chữ bật, tia lửa) · synth `type.key` |
| Phím sai | Thẻ rung 2 khung, chữ nứt viền tím xám, tàn tro rơi | Tiếng xì than tắt, thấp | có · synth `type.miss` |
| Xóa, đổi mục tiêu | Con trỏ trên thẻ lùi; vòng mục tiêu nhảy sang quái mới | Tick nhỏ | có · synth `type.back`, `type.switch` |
| Xong từ (đòn chữ) | Đủ 5 pha: miệng rồng gồng sáng (A), lóe và giật đầu (R), cầu lửa có thân và vệt (T), nổ theo chất liệu: rêu tung bụi xanh, vỏ cây văng mảnh (I), vết cháy, khói, tàn (F) | Hít lửa, phụt, rít, nổ 3 lớp | thiếu pha (bước 1a: 7 và 7,5, lõi trắng quá to) · synth `type.word`, `fire.cast`, `fire.impact.a/b/c` |
| Trúng nhiều quái | Một vụ nổ cỡ √N, mảnh mỗi con | Một tiếng nặng hơn | có một phần · synth `impact.multi` |
| Dragon Rage đầy, chiêu sẵn | Vảy rồng rực, khung chiêu trên HUD sáng, tia lửa quanh icon | Gầm ngắn trầm | thiếu · synth `dragon.rage`, `dragon.skill-ready` |
| Fire Breath | Đủ 5 pha: hít, nón lửa cuộn, vết cháy trên làn | Hít sâu, gầm lửa dài | thiếu pha (DH-07) · synth `dragon.breath` |
| Sky Fire | Đủ 5 pha: rồng bay lên, bóng tròn báo chỗ rơi, mưa lửa, hố cháy | Gầm vang, rít rơi, nổ dồn | thiếu pha (đang làm) · synth `dragon.skyfire.cast/impact` |
| Dragon Roar | Vòng méo không khí, quái lùi, bụi bay | Gầm sâu có vang 0,6 s | thiếu pha · synth `dragon.roar` |
| Inferno | Đủ 5 pha, tia lửa lớn, biển lửa, màn rung nhẹ | Gầm, lửa nổ lớn, đuôi dài | thiếu pha (có tia) · synth `dragon.inferno` |
| Rồng lên cấp, uống thuốc | Vòng lửa vàng từ chân lên, số bay | Hợp âm 2 nốt; tiếng uống | chưa · synth `dragon.level`, `dragon.potion` |
| Rồng bị đánh, máu thấp, ngã | Vảy lóe đỏ, mảnh vảy; máu thấp viền đỏ màn hình và tim đập; ngã: lửa tắt dần | Rên, nhịp tim, gầm tắt | thiếu · synth `dragon.hurt/low/heartbeat/down` |
| Quái ra (mọi họ) | Sương tím xám bốc ở mép rừng, quái bước ra, cỏ héo dưới chân | Họ hai chân: rên gỗ; bốn chân: gầm gừ; bay: vo ve; bầy: lạo xạo | chưa · synth `enemy.*.spawn` |
| Quái đi | Bụi chân, cỏ rạp, vệt héo mờ sau bầy | Bước chân theo họ (lặp) | có một phần · synth `enemy.*.march` |
| Quái gồng, đánh, bắn | Vòng đỏ báo dưới chân (≥ 0,6 s), vung tay, mũi tên gai bay | Rít gồng, đập, phựt | thiếu pha (bước 4 đang làm) · synth `windup/attack/shoot`, `warn.telegraph` |
| Quái trúng | Lóe trắng 60 ms, mảnh theo chất liệu (rêu, lông, vỏ, cánh) | Theo chất liệu | có một phần · synth `enemy.*.hit` |
| Quái chết | Cháy thành tro và sợi héo bay lên, rơi đồng | Theo họ + chuông hạ | thiếu · synth `enemy.*.death`, `kill.chime` |
| Moss Bannerman (G01) | Tù và, cắm cờ có vòng hào quang, chết: cờ đổ, hào quang vỡ | Tù và, đập, vỡ kính | thiếu pha · synth `general.g01.*`, `general.aura.break` |
| Spikes, Pine Bomb, Net Launcher | Đặt: bụi và chốt khóa; kích: gai bật, bom nổ quả thông, lưới bung trùm | Cạch lên dây; phập, nổ, phựt lưới | thiếu pha (DH-07) · synth `trap.*.arm/trigger` |
| Herb Hut | Đặt: mái lá mọc; nhịp: vòng lá xanh lan, lá xoay quanh người được hồi | Lá xào xạc, chuông nhỏ | thiếu pha · synth `house.herb.place/pulse` |
| Grove Warden | Đặt: rễ trồi; bị đánh: vỏ văng; ngã: tan thành lá | Gỗ cộc, rên gỗ | thiếu pha · synth `unit.warden.*`, `unit.hit` |
| Đợt bắt đầu, xong | Làn quái sáng lên (có), băng rôn đợt có khung 119; xong: bụi lắng, ánh vàng | Tù và ải; hợp âm xong đợt | có một phần · synth `wave.horn`, `wave.clear` |
| Thắng, thua | Thắng: rồng gầm trên cổng, pháo lửa; thua: lửa tắt, sương tím tràn | Nhạc chốt thắng, thua | có một phần (giữ 2,6 s) · synth `stinger.victory/defeat` |
| Thưởng (vàng) | Đồng bay về ô Gold, ô nảy | Tiếng đồng theo thang | có một phần · synth `ui.gold` |
| UI mở, chạm, đóng | Bảng trượt và mờ vào trong khung STYLE-UI; nút lóe viền vàng búa; đóng ngược lại | Đá chạm nhẹ, sắt cạch, gió nhẹ khi đóng | chưa có khung thật · synth `ui.select/confirm/deny` |
| Học (từ mới, đúng, sai) | Thẻ học có khung, chữ lóe | Chuông nhẹ | có · synth `learn.*` |
| Nền | Sương trôi, chim, nước sông, lá rơi | Gió rừng, suối, chim; nhạc 4 lớp (Forest, Wave, Surge, General) | có (nước, cây đung đưa) · synth `amb.*`, nhạc 2 lớp |
| Boss | Map 1 chưa có boss; khi có: đủ 5 pha mỗi đòn, đổi pha có sương và trời ngả màu | Chủ đề riêng | chưa |

### 8.2 Wordwoven

| Sự kiện | VFX bible đòi | Tiếng bible đòi | Hôm nay (VFX · tiếng) |
|---|---|---|---|
| Phím đúng | Chữ trên thẻ thành nét mực vàng; một sợi chỉ vàng mảnh chạy từ thẻ vào nhà (chủ đề "woven") | Gỗ tre gõ, theo thang ngũ cung | có (2D) · synth `key-right` (giữ synth) |
| Phím sai | Nét mực nhòe, thẻ rung, giọt mực rơi | Phách tre lệch | có (2D) · synth `key-wrong` |
| Xong từ | Thẻ bung chữ cái bay vào nhà (T), nhà đáp một đòn (I) | Chuông đồng nhỏ | có (2D) · synth `word-hit`, `word-hit-bell` |
| Chuỗi | Sợi chỉ xanh ngọc nối hai nhà 0,45 s; số chuỗi nảy | Nốt thêm theo bậc chuỗi | có (2D) · synth `chain-callout` |
| Lời gọi hiện (Power, Build, Harvest, Chop, Mine, Quiz) | Thẻ mọc từ mái nhà với icon loại gọi (phiếu UI) | Trống cơm, ống tre, liềm, rìu, cuốc, chuông | có (2D) · synth `call-*` |
| Word Shot | Đầu đạn xanh ngọc, vệt chữ cái của từ vừa gõ, đủ 5 pha | Phụt mạnh + "ting" cao | có một phần (2D) · synth `wordshot-fire` |
| Fort (nỏ) | Đủ 5 pha: lên dây, phát, mũi nỏ vệt trắng, cắm, rung | Tchk, phập | 2D đơn giản · chưa riêng |
| Archer Tower | Đủ 5 pha (C11): dây cung chớp, tên trắng, trúng thock; Mưa Tên | Thwip ×4 biến thể, thock | 2D thiếu R, I · synth `arrow-fire` |
| Cannon Tower | Đủ 5 pha: lửa nòng, khói, bóng chỗ rơi, nổ bụi, vết cháy | Thoomp, rít, nổ 3 lớp | 2D thiếu · synth `blast` |
| Calligraphy Tower | Cọ vung, dải mực đuổi, vỡ thành chữ | Swish, giấy | 2D · synth `ink-puff` |
| Barracks, lính | Lính ra cổng có bụi; đâm giáo vệt trắng; chết tan thành chữ bay lên | Trống da, hô "Hup!", xoạt, phập | 2D đơn giản · chưa riêng |
| Gold Mine, Rice Field, Lumber Camp | Cuốc tóe lửa và đồng bay; lúa vọt và bó lúa bay; rìu bổ và gỗ bay về HUD | Ching theo nốt; bụp, sột; cộc | 2D một phần · synth `coin` |
| Seal Dais, Herb House | Sóng chữ gợn đúng bán kính; lá xoay quanh người được hồi | Chuông gió, hợp âm thủy tinh; nồi sôi | chưa (map 1 chưa dùng hết) · chưa |
| Xây, nâng cấp, bán, bị đánh, đổ nát, sửa | Giàn tre và bụi, model mọc 1,2 s; bộ cấp rơi nảy; tháo thành ván; lóe đỏ và mảnh; sập bụi lớn; tia lửa vàng | Búa "hò dô", stinger 2 nốt, ầm | chưa (3D: C6) · chưa |
| Draconis: cầu lửa, nón lửa, gầm | Đủ 5 pha mỗi đòn; vòng méo không khí | Whoom, rít, nổ 2 lớp; gầm sâu | 2D một phần · chưa riêng |
| Fire Feather Rain (Tối Thượng) | Ảnh trượt chân dung, bay cao rải lông, bóng tròn báo 0,8 s, vũng than | Trống to dần theo Chữ Chiêu | có (2D, `FxView`) · chưa riêng |
| Thư Đồng (Helper) | Bụi phấn, nét phấn lóe, hoảng có lông rơi | "Chíp", "lạch bạch", "á" | 2D một phần · chưa |
| Quái ra | Theo loài: Hopping Zombie nhảy ra từ sương; Ghost Flame lóe xanh; River Serpent trồi khỏi nước có bọt; Sapling mọc từ đất | Theo loài | chưa · chưa |
| Quái đi | Theo loài (nhảy, trôi, bò); bụi, nước, lửa ma | Theo loài (lặp) | chưa · chưa |
| Quái đánh | Báo trước bằng decal trên đất; vòng nước River Serpent; trống Raccoon Dog | Theo loài | 2D một phần · chưa |
| Quái trúng | Theo chất liệu (TK §23.8): giấy "bụp", lông "thịch", bột "bọp", vảy nước "cạch", đá "cộc", hồn "vút" | Như cột trái | 2D chung một kiểu · chưa |
| Quái chết | Theo loài: bùa giấy cháy, lửa ma tan, rắn chìm, khối tách đôi (Split Blob) | Theo loài | 2D mọi loài giống nhau · chưa |
| Zombie Leader (Neo), Troll (Phá Khiên) | Vòng hào quang dẫn bầy; vòm khiên đồng trên Troll, vỡ khi gõ | Tù và; khiên "đoang", vỡ | 2D · synth (trong `audio-min.ts`) |
| Mộc Tinh (boss) | Trồi lên có đá và rễ; decal Rễ Trồi báo ≥ 1,2 s; hạt rơi; Rễ hút sinh khí; pha 2; rút lui; trời và sương ngả màu boss | Gầm gỗ, rễ nứt đất, "cộp" | 2D có (`boss-2d.ts`) · synth một phần |
| Thưởng | Đồng, Rice, Wood, Word Shard bay cong về ô HUD; Chest khi boss rút | Đồng theo thang, sột lúa, cộc gỗ, ting | 2D một phần · synth `coin` |
| Ngày bắt đầu, Đêm xuống | Bình minh: sương tan, nắng quét qua sân; đêm: trời 114 `sky-night`, đèn lồng bay lên, băng rôn 115 | Gà gáy xa, chiêng làng; dế, gió đêm | 2D đổi màu · synth `dawn`, `night-fall` |
| Lọt quái, thua | Fort lóe đỏ, cột khói; thua: đèn lồng tắt dần | Cồng trầm | 2D · synth `leak`, `defeat` |
| UI mở, chạm, đóng | Bảng 115 mở bằng nét vàng lá chạy quanh viền; nút sáng hổ phách; đóng thu về | Gỗ sơn mài chạm, chuông đồng nhỏ, giấy | bảng CSS · synth `ui-move/pick/off/lamp` |
| Nền | Mây trôi, bóng mây, thác, đèn lồng, chim | Thác, gió, chim; nhạc calm, tension, boss | 2D · synth `amb-*`, `music-*` |

### 8.3 Last Line (hướng B; chữ nghiêng là phần đổi theo hướng)

| Sự kiện | VFX bible đòi | Tiếng bible đòi | Hôm nay (VFX · tiếng) |
|---|---|---|---|
| Phím đúng | *Một ký hiệu sáng bay từ bàn tay vào súng canh, xếp vòng*; chữ trên tấm chữ đổi màu súng; vạch sáng trên sàn (có) | Tinh thể chạm, cao độ lên theo chữ | có (tia vào lõi tàu, vạch sàn) · synth `key.ok` |
| Phím sai | *Ký hiệu nứt, rơi thành tia lửa*; tấm chữ rung | Kính rạn ngắn | có một phần · synth `key.bad` |
| Nạp từ (xong từ) | *Vòng ký hiệu đóng lại quanh súng canh*, lóe nạp | Khóa nạp, hợp âm ngắn | có · synth `word.load` |
| Từ hoàn hảo, bến đầy | Vòng vàng trắng, *áo choàng lóe*; bến đầy: viền bến sáng đều | Chuông cao; tiếng đầy | có một phần · synth `word.perfect`, `word.full` |
| Chuỗi | *Kính mũ và áo choàng sáng dần theo bậc*; số chuỗi nảy | Nốt thêm mỗi bậc | có một phần · synth `streak.up` |
| Pulse Gun | Đủ 5 pha: nòng gom chữ (A), sao đầu và lưỡi lửa (R), viên lam có đuôi sao chổi (T), lóe theo chất liệu (I), vết cháy (F) | Xung, đuôi | thiếu pha (TS-M1-05 trượt giám khảo: 5,5) · synth `gun.xung`, `.tail` |
| Heat Beam | Đủ 5 pha: lóe mồi, tia cam lõi cam, cháy sàn, khói | Bắt đầu, lặp, tắt, nhịp | thiếu pha (5) · synth `gun.tia.*` |
| Scatter Gun | Đủ 5 pha: chùm 6 viên xòe, lóe nòng rộng, mưa tia | Nổ chùm | thiếu pha (TS-M1-16) · synth `gun.tan.fire` |
| Rail Gun | Đủ 5 pha: nạp có vòng điện, tia thẳng xuyên, vệt ion lưu | Vo nạp, nổ tia | thiếu pha · synth `gun.ray.armed/charge/fire` |
| Star Mortar | Đủ 5 pha: phóng cầu vồng, bóng chỗ rơi, nổ vùng, hố sao | Phụt, rít, nổ | thiếu pha · synth `gun.phao.launch/burst` |
| Trúng (nhẹ, vừa, nặng), trúng Vỏ, khiên | Lóe 2–6 khung, số bay; Vỏ: tia lửa kim loại; khiên lam gợn, vỡ thành mảnh | 3 bậc trúng; keng; khiên ù, vỡ | có · synth `hit.t1/t2/t4`, `hit.armour`, `shield.*` |
| Quái ra | *Nứt trên mặt kính hư không mở ra, quái bò khỏi vết nứt*; bầy tràn qua mép đường đắp | Kính nứt, lạo xạo | chưa · chưa |
| Quái đi | Bầy dạt như sóng, nứt cam nhấp nháy theo nhịp | Lạo xạo theo cỡ bầy (lặp) | có một phần · chưa riêng |
| Scout bắn | Báo trước ánh lam ở nòng, viên đạn có thể bắn hạ | Rít, nổ nhỏ | có · synth `foe.shot`, `foe.shot.down` |
| Brute, Pack Leader | Brute gồng đập có vòng báo; Pack Leader gầm tù và, vòng vàng quanh | Đập nặng; tù và | có một phần · synth `leader.horn` |
| Splitter | Vỡ đôi thành Shard có lóe | Kính vỡ đôi | có · synth `foe.split` |
| Quái chết | *Kính đen vỡ vụn, nứt cam tắt dần*; quái lớn: cầu lửa, mây khói nằm trên sàn, mảnh văng (có) | Swarm: vụn kính; Elite: nổ nặng; Pack Leader: rơi | có (đòn chết lớn) · synth `kill.swarm/elite`, `leader.down` |
| Nhân vật bị đánh, thủng tuyến, mất Armor | *Giáp lóe khiên lam, áo choàng giật*, khói và tia lửa (có ở tàu) | Va chạm, báo động | có (tàu) · synth `hurt.breach/hull/drain` |
| Tiếp tế | Vòng xanh lá từ trên xuống, Armor tăng | Tiếng sửa | có một phần · synth `support.repair` |
| Rift | Báo trước ≥ 1 s, vết nứt mở cam tím, quái chui ra | Báo, xé không gian | có · synth `rift.warn/open` |
| Đợt dồn (surge) | *Quái vật hư không ngẩng lên trong hố đen*, đĩa sáng rực | Báo động, nhạc lên lớp surge | có một phần · synth `alarm.surge`, `music.surge` |
| Kết thúc thắng, thua, sao | Băng rôn 0,9 s (có) trên nền 121; sao bay vào ô | Nhạc chốt; ting sao | có · synth `end.win/lose`, `star.get` |
| UI mở, chạm, đóng | Bảng 127 mở bằng một đường sáng trắng vàng quét ngang; nút lóe lam | Kính chạm, ù thấp | bảng CSS · synth `ui.move/select/back` |
| Nền | Bụi trôi trong vệt sáng, mảnh trạm trôi, đĩa xoáy | Ù trầm của hố đen, gió mặt trời; nhạc calm, surge | có một phần · synth `music.calm/surge` |
| Boss | R3 của game (chưa làm); khi có: quái vật hư không là boss, đủ 5 pha mỗi đòn | Chủ đề riêng | chưa |

**Thứ tự làm âm thật** (đề xuất, theo cái người chơi nghe nhiều nhất): tiếng của đòn chữ và các súng → trúng và chết của quái → quái ra và đi → UI → nền và nhạc. Mỗi lượt Audio Lab làm theo `AUDIO_PIPELINE.md`; chủ dự án nghe duyệt.

---

## 9. Việc cần chủ dự án

1. **Chọn hướng Last Line** (A, B hay C) khi phiếu 112 xong: xem `games/typing-survival/art-src/_review/112-directions.jpg`. Đề xuất: B. Bốn phiếu 121, 125, 126, 127 và việc dựng nhân vật chờ quyết định này.
2. **Dựng Tripo** (bằng tay trên web, khoảng 30 credit một model):
   - Dragonhold 6 mốc (phiếu 124): khoảng 180 credit;
   - Wordwoven 5 mốc (phiếu 128): khoảng 150 credit;
   - Last Line nhân vật và 5 súng canh (sau khi chọn hướng): khoảng 180 credit.
3. **Đồng ý hay không** dựng lại 6 nhà mái tranh của Wordwoven (phiếu 129, khoảng 180 credit cộng bộ cấp). Nếu không, ta chỉ chỉnh ánh sáng và giảm màu.
4. **Tên nhân vật Last Line:** "Lightbearer" là tên tạm của hướng B. Chủ dự án có thể đặt tên riêng.
5. **Phiếu 109:** đề xuất nhận bốn ảnh ải làm ảnh tạm (7/10) tới khi 126 xong.

---

## 10. Ghi chú cho các làn

- **Không dựng hình bằng mã thay tranh** (luật 28/10): bầu trời, phông, cây, khung UI đều là ảnh thật. Địa hình (tháp đá vôi, mép cao nguyên, vách) được dựng bằng mã, phủ texture vách của phiếu 122.
- **Billboard v3, v4** (116–118): tắt viền mực của `prepare-scenery`; giữ pháp tuyến phồng, ramp, đáy tối, rim.
- **Phông vòng** (114, 120): luật ghép như bộ cũ: ô `-a` một lần, ô trơn lật ngang xen kẽ; đường chân núi ở mép đúng độ cao ghi trong phiếu.
- **Rùa trời** (114): tấm `sky-beast` bay chậm dọc vòng trời (một vòng mỗi Ngày); `sky-beast-top` thành bóng mờ 35 % trôi qua sân, không che thẻ chữ quá 0,4 s.
- **Logo:** dùng bản Codex chỉ khi đúng chính tả; nếu không, dựng chữ bằng font của game với hiệu ứng.
- **Ảnh chụp kiểm** đặt trong `tmp/` của game; xóa ảnh thô bằng `tools/capture-prune/prune.mjs` sau khi chấm, giữ tờ so.
- **Chấm sau khi tích hợp:** một giám khảo độc lập chấm cảnh trong game theo thang 1.3 (M), ở 1280 và 1920, ba góc nghiêng × bốn hướng cho Wordwoven và Dragonhold; mỗi khung ≥ 8.
