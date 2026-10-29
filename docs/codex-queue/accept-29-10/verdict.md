# Chấm nhận ảnh 29/10: phiếu 113, 114, 115 (Wordwoven), 137, 138, 139 (Dragonhold)

Người chấm: Claude (chấm lại độc lập, theo `ART_DIRECTION_2026-10-28.md` §1.3 và `ART_ACCEPTANCE.md` §2.2). Nhận khi **M ≥ 8 và Q ≥ 8**. Q ghi theo thứ tự Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp.

Tôi xem từng ảnh ở cỡ đầy đủ và ở cỡ trong game, không chỉ tờ của Codex. Tờ so của tôi (cùng thư mục):
- `113-vs-ref.jpg`: ảnh mẫu, nền tựa (bản giao và try1), keyart, poster, mock logo của Codex và của tôi;
- `114-ring-vs-ref.jpg`: ảnh mẫu, ảnh ghép ngày, vòng ghép trời và núi 140, vệt tím ở mép 140-a, trời trước và sau hậu kỳ, rùa trời;
- `115-frames-vs-ref.jpg`: ảnh mẫu, mock HUD, khung 9-slice ở try1, bản giao và corrected-v2;
- `dh-icons-137-139.jpg`: 31 icon ở 112 px, ở cỡ 1080p và 720p (phóng ×3, không làm mượt) trên nền vỏ cây và kem, dải cỡ thật ×2, icon yếu, màu model kiến gai.

## Tổng

| Phiếu | Game | Nhận | Làm lại | Ghi chú |
|---|---|---:|---:|---|
| 113 | Wordwoven | 3 | 2 | Logo và huy hiệu: nhận **bản sạch trong `_review/113/delivery-alpha/`**, không phải bản đang nằm ở `ui/title-epic/` |
| 114 | Wordwoven | 2 | 7 | Hai rùa đạt; cả bảy ô vòng hỏng ở bước hậu kỳ, tranh gốc tốt |
| 115 | Wordwoven | 4 | 5 | Năm khung 9-slice bị hậu kỳ vứt mất phần vẽ; bốn ảnh không 9-slice đạt |
| 137 | Dragonhold | 8 | 2 | armour, danger |
| 138 | Dragonhold | 10 | 0 | |
| 139 | Dragonhold | 9 | 2 | flag-pull, swarm |
| **Cộng** | | **36** | **18** | |

Chín trong mười tám ảnh phải làm lại **chỉ cần sửa lại hậu kỳ từ lượt sinh đã có** (113 nền tựa, bảy ô của 114 trừ trời đêm, năm khung 115). Phải sinh mới: poster 113, trời đêm b của 114, button-active 115 (dựng từ nút đã sửa), bốn icon.

**Người chấm thứ ba (`ART_ACCEPTANCE` §4).** Điểm của tôi và của Codex nằm hai phía ngưỡng ở: nền tựa và poster 113 (Codex 8,5, tôi 7,5), các ô 114 (8 và 6–6,5), năm khung 115 (7,5–8 và 4–4,5, lệch từ 2 điểm), armour, danger, flag-pull, swarm (8 và 7–7,5). Lỗi của 113 nền tựa, 114 và 115 đo được và thấy ngay trên tờ so (hộp tối nung vào ảnh, dải phẳng, khung mất phần vẽ), nên tôi đề nghị sửa luôn thay vì chấm thêm. Poster và bốn icon thì người thứ ba có thể xem nếu điều phối muốn tranh luận.

---

## 113 · Wordwoven · màn tựa, ảnh chủ đạo, logo

| File | M | Q | Kết luận | Vì sao |
|---|---:|---:|---|---|
| `ui/title-epic/title-backdrop.png` | 7,5 | 8 (2/1/2/2/1) | **Làm lại** (sửa hậu kỳ, một lượt sửa ảnh) | Tranh try1 đạt mức chợ (8,5: tháp đá vôi, rùa trời, pháo đài, bốn tầng sâu). Nhưng hậu kỳ nhân 0,56 một hộp chữ nhật (x 290–1246, y 38–434) và 0,62 góc dưới trái, nên trời vàng thành mảng xám đục, ranh hộp cắt qua đầu rùa. Rồng nhỏ và đỉnh tháp còn nằm đúng chỗ logo. |
| `ui/title-epic/keyart.png` | 8 | 8,5 (2/2/2/1,5/1) | **Nhận** | Rồng và Tree Spirit khổng lồ, lửa dẫn mắt, đọc rõ ở 384 px, khớp model. Trừ: rất dày, ít chỗ nghỉ; góc trên trái dành cho logo lại là vệt nắng sáng nhất. |
| `ui/title-epic/poster.png` | 7,5 | 7,5 (2/1/2/1,5/1) | **Làm lại** (sinh lượt 2) | Là keyart ép dọc: Tree Spirit nhỏ lại, không còn cao hơn vách; cánh phải của rồng bị mép cắt; nửa dưới chật tên, tháp, đèn; trời bão phía trên tối phẳng. |
| `logo` (`_review/113/delivery-alpha/logo.alpha.png`, `.512.png`) | 8,5 | 9 | **Nhận bản sạch** | Đúng chín chữ W-o-r-d-w-o-v-e-n. Ngọc nhạt viền vàng, chỉ vàng đan qua chữ, viền đồng sẫm giữ chữ đọc được cả trên trời sáng (tôi ghép thử trên try1). Bản trong `ui/title-epic/` còn 963 px (logo) và 38 px (512) mang sắc khóa hồng: **điều phối chép bốn file sạch đè lên bốn file đó** (Codex không được ghi đè). |
| `emblem` (`_review/113/delivery-alpha/emblem.alpha.png`, `.512.png`) | 8 | 9 | **Nhận bản sạch** | Sao 16 tia, sếu, mây, rồng trắng vàng ôm viền; ở 64 px còn nhận ra ấn tròn và mặt trời. Bản trong `ui/` còn 141 và 105 px hồng. |

## 114 · Wordwoven · trời và phông xa

M của ô vòng chấm trên vòng ghép (luật §1.4): **ảnh ghép ngày 6,5, đêm 6**. Từng tranh gốc (`.tryN.png`) đẹp, khoảng 8. Hỏng ở hậu kỳ:
- hai mép mỗi ô núi bị thay bằng một "vai" phẳng ở đúng 60/62 % và một khối sương màu phẳng, nối với núi bằng dốc nhòe;
- ô trời bị ép phẳng 20 % mỗi bên và cắt một dải kem phẳng từ 75 % trở xuống.

Khi xếp vòng, ta thấy những đảo núi và cục mây riêng lẻ, giữa chúng là các dải phẳng: một khoảng trống như mã vẽ, không phải dãy núi liền.

| File | M | Q | Kết luận | Vì sao |
|---|---:|---:|---|---|
| `sky-day-a.png` | 6,5 | 6,5 | **Làm lại** (hậu kỳ từ try1) | Mây thành một cục giữa nền gradient phẳng; đáy kem phẳng cắt cứng. Try1 tự nó tốt. |
| `sky-day-b.png` | 6,5 | 6,5 | **Làm lại** (hậu kỳ từ try1) | Như a; trong vòng ghép thành bốn "bức tranh" có khung. |
| `sky-night.png` | 6 | 6 | **Làm lại** (hậu kỳ, thêm ô b không trăng) | Như trên, và một ô dùng bốn lần nên vòng có bốn mặt trăng. |
| `layer-320.png` | 6,5 | 6,5 | **Làm lại** (hậu kỳ từ try3) | Vai phẳng và khối sương phẳng ở hai mép; vòng thành bốn cụm núi cách nhau bởi khoảng trống. |
| `layer-220.png` | 6,5 | 6,5 | **Làm lại** (hậu kỳ từ try2) | Như 320; dốc nhòe ở mép phải. |
| `layer-140-a.png` | 6,5 | 6 | **Làm lại** (hậu kỳ từ try2) | Như trên, thêm vệt cột tím dọc mép vách trái (104 px tím đậm; thấy rõ ở ×3) do lấp túi màu khóa bằng màu cùng cột. |
| `layer-140-b.png` | 6,5 | 6,5 | **Làm lại** (hậu kỳ từ try1) | Như trên; vòng a, b~, b, b~ thành bốn đảo. |
| `sky-beast.png` / `.alpha.png` | 8,5 | 8,5 (2/2/2/1,5/1) | **Nhận** | Rùa trời rất đạt, cùng bộ với rùa trên màn tựa, alpha sạch. Trừ: sương ở vây cắt cứng như bông đục, mép sương hơi ngả tím nhạt (sửa khi tiện: alpha sương theo độ sáng). |
| `sky-beast-top.png` / `.alpha.png` | 8 | 8 (1,5/2/2/1/1,5) | **Nhận** (làm nguồn bóng) | Chưa phải nhìn thẳng 90°, nhưng bóng 35 % mờ 24 px đọc ra con rùa, bốn vây, đầu đuôi; đủ cho việc của nó. |

Ngoại lệ "magenta cả bốn mép" Codex nêu: tôi đồng ý đó là mâu thuẫn của phiếu. Ô núi chỉ cần magenta phía trên đường chân núi.

## 115 · Wordwoven · khung UI

Bốn khung 9-slice và nút: **lượt sinh try1 đạt mức chợ** (đá vôi chạm, góc đồng mặt trời, đầu mây cuộn, viền vàng, khoảng 8). Nhưng hậu kỳ cắt góc còn 32 px (tooltip 16 px) trên canvas 1024–1536, thay rail chạm bằng một đường chỉ mảnh, rồi trải lòng ngọc kín cả canvas. Bản giao nên là một tấm ngọc phẳng có viền mảnh, tức "bảng CSS" mà chỉ đạo cấm. Bản corrected-v2 chỉ tối hơn, vẫn phẳng. Mock HUD chung: **M 6**.

| File | M | Q | Kết luận | Vì sao |
|---|---:|---:|---|---|
| `panel-large` | 4,5 | 6 (1/2/1/1/1) | **Làm lại** (hậu kỳ từ try1) | Mất viền đá vôi chạm và bốn huy chương đồng; còn tấm ngọc có viền mảnh. |
| `plate-long` | 4 | 5,5 (1/2/1/0,5/1) | **Làm lại** (hậu kỳ từ try1) | Mất đầu mây cuộn; vân ngọc bị kéo thành sọc dọc (bản giao), corrected-v2 phẳng tối. |
| `button` | 4 | 5,5 (1/2/1/0,5/1) | **Làm lại** (hậu kỳ từ try1) | Mất huy chương mặt trời ở góc; như plate. |
| `button-active` | 4 | 5,5 (1/2/1/0,5/1) | **Làm lại** (dựng từ nút đã sửa) | Như button; bản sinh đã đổi dáng (SAME không giữ được). |
| `tooltip` | 4,5 | 6 (1/2/1/1/1) | **Làm lại** (hậu kỳ từ try1) | Bản giao là tấm ngọc trơn. Try1 (góc mặt trời nhỏ, cạnh trơn) hợp 9-slice hơn try2; Codex bỏ try1 vì "nhiều trang trí" nhưng ở cỡ tooltip góc chỉ còn 18–24 px. |
| `banner` | 8,5 | 9 | **Nhận** | Dải ngọc đuôi én, hai huy chương mặt trời, vàng lá; "Night 1" đọc rõ. Trang trí giữa mép ngoài brief nhưng hợp. |
| `portrait-ring` | 8 | 9 | **Nhận** | Vòng đồng khắc tia, bốn ngọc, lòng trong suốt; đọc được ở 64 px. |
| `crest` | 8,5 | 9,5 | **Nhận** | Đẹp nhất bộ: mặt trời Đông Sơn, cánh mây, điểm son. |
| `divider` | 8 | 9 | **Nhận** | Thoi ngọc giữa hơi to so với "small"; không sao. |

## 137 · Dragonhold · HUD và trạng thái

Cả bộ cùng chất liệu (granite kem, vàng búa, men than hồng), hoàn thiện như icon vật phẩm của game chiến thuật thương mại. Cỡ 720p (12–16 px) là giới hạn: icon vẽ chỉ còn dáng.

| File | M | Q | Kết luận | Vì sao |
|---|---:|---:|---|---|
| `wave-horn` | 8 | 9 | **Nhận** | Sừng cong đai sắt; ở 16 px còn dáng lưỡi liềm. |
| `chain` | 8 | 9 | **Nhận** | Ba mắt xích, đọc là xích ở 16 px. |
| `dragon-rage` | 8 | 8,5 | **Nhận** | Đẹp ở cỡ lớn; ở 16 px mắt mất, còn một ngọn lửa cam (vẫn khác dáng mọi icon khác). |
| `armour` | 7,5 | 6,5 (2/0,5/2/1/1) | **Làm lại** | Dáng cao hẹp: ở 12 px là một que, ở 18 px như chiếc lá. Không đọc là giáp. |
| `shield` | 8 | 9 | **Nhận** | Khiên tròn có thập tự; cùng dáng tròn với `pause` và `slot-house` (IoU 0,92–0,985), chỉ khác lòng. |
| `phase-prep` | 8 | 8,5 | **Nhận** | Ở 16 px thành cụm "đồ nghề", ở 24 px rõ búa và cọc. Đủ cho chỉ báo pha có nhãn. |
| `phase-fight` | 8,5 | 9 | **Nhận** | Hai kiếm chéo và lửa, rõ cả ở 16 px. |
| `phase-break` | 8 | 9 | **Nhận** | Lửa trại và khói, rõ. |
| `fast-forward` | 8 | 9 | **Nhận** | Hai chevron, rõ. |
| `danger` | 7 | 6,5 (1/1,5/1/2/1) | **Làm lại** | Là tia sét, không phải dấu cảnh báo cam đỏ: trên quái đang gồng, tia sét dễ đọc thành "điện, choáng". Gamma 2,6 làm phai thành kem nhạt, lệch bộ; trên nền kem chỉ chênh 0,14. |

## 138 · Dragonhold · hệ thống và học

| File | M | Q | Kết luận | Vì sao |
|---|---:|---:|---|---|
| `pause` | 8,5 | 9 | **Nhận** | Hai thanh granite trên đĩa sắt, rõ ở 16 px. |
| `camera-reset` | 8 | 8,5 | **Nhận** | Mắt rồng và mũi tên quay về; mũi tên mờ ở 16 px, mắt vẫn rõ. |
| `keyboard` | 8 | 9 | **Nhận** | Bàn phím đá, rõ ở 24 px. |
| `speaker` | 8 | 8,5 | **Nhận** | Kèn đồng; hai cung âm dính nhau ở 14 px nhưng vẫn là "loa". |
| `check` | 8,5 | 9 | **Nhận** | Dấu kiểm đá dát than hồng, rõ ở 14 px. |
| `new-word` | 8 | 9 | **Nhận** | Sao bốn cánh vàng. Ít chất liệu hơn bộ một chút, chấp nhận được. |
| `deny` | 8 | 8,5 | **Nhận** | Chữ X sắt có than đỏ; ở 16 px cùng dáng X với `phase-fight` (khác chỗ dùng). |
| `lock` | 8,5 | 9 | **Nhận** | Ổ khóa vảy rồng, quai và thân còn ở 12 px. |
| `upgrade` | 8 | 8 | **Nhận** | Ở 16 px bậc đá thành một khối, chevron nhỏ; rõ ở 24 px. Sát ngưỡng. |
| `sell` | 8 | 8 | **Nhận** | Găng và đồng vàng; ở 16 px còn dáng bàn tay. Sát ngưỡng. |

## 139 · Dragonhold · bản đồ và thẻ chữ

| File | M | Q | Kết luận | Vì sao |
|---|---:|---:|---|---|
| `lane-bridge` | 8 | 9 | **Nhận** | Vòm cầu đá rõ ở 16 px. |
| `lane-stream` | 8 | 8,5 | **Nhận** | Dòng nước bạc lam chữ S, rõ. |
| `lane-sky` | 8 | 8,5 | **Nhận** | Cánh dơi tím đá phiến, rõ ở 24 px, vừa đủ ở 16 px. |
| `slot-trap` | 8 | 9 | **Nhận** | Khung sắt vuông trên đất, rõ trên cỏ. |
| `slot-house` | 8 | 8,5 | **Nhận** | Bệ granite tròn; hơi trơn (chia ba như cái bánh) nhưng đúng đề, nổi trên cỏ. |
| `slot-hold` | 8 | 9 | **Nhận** | Cột cờ đuôi én trên chân đá, rõ. |
| `seal-lit` | 8 | 8,5 | **Nhận** | Ấn tím có nứt sáng; ở 10 px là chấm tím sáng. Cặp với unlit IoU 0,996. |
| `seal-unlit` | 8 | 8,5 | **Nhận** | Cùng dáng, tối và nứt; khác trạng thái rõ ở 14 px. |
| `flag-pull` | 7 | 6,5 (1/1/2/1,5/1) | **Làm lại** | Đọc thành "nắm tay cầm giáo": lá cờ Héo chỉ còn một chùm tua tím nhỏ, cục đất nhỏ. Ở 18 px là một khối. |
| `swarm` | 7 | 6,5 (1/1/1/2/1,5) | **Làm lại** | Ba con kiến giáp kem vàng: lệch model kiến gai (nâu sẫm, mai đá xám, mắt vàng lục), lại trùng màu phe ta. Ở 18–22 px thành một con bọ. |
| `edge-arrow` | 8 | 9 | **Nhận** | Đầu tên than hồng, rõ cả ở 10 px. |

---

## Sửa cho từng ảnh làm lại (dán vào phiếu làm lại)

### 113 `title-backdrop` (hậu kỳ, một lượt sửa ảnh)
1. Bỏ hẳn bước làm tối trong `title-colour-command.json`. Lấy lại `title-backdrop.try1.png`, không nung hộp tối hay vignette nào vào tranh.
2. Sửa ảnh try1 (tính là lượt 2):
   ```text
   Edit the attached image. Remove the small white-gold serpent dragon from the upper-middle sky and fill that area with the same golden-hour blue sky and soft clouds around it. Paint the same small dragon again flying low over the river valley in the left third, at about 35% from the top, below the tops of the far karst towers. Keep everything else identical: composition, the Fort, the sky turtle, the lanterns, light and colours. No text.
   ```
3. Độ đọc của logo do UI màn tựa lo: logo đã có viền đồng sẫm, đọc được trên try1 (xem mock của tôi). Nếu cần, thêm một vệt mờ tối dạng elip mềm (≤ 0,35) sau logo ở lớp UI. Menu nằm trên bảng 115, không cần làm tối tranh.
4. Đổi kiểm 6 của phiếu: bỏ ngưỡng độ lệch chuẩn luma ≤ 0,12 (chỉ đạt được bằng cách làm bẩn tranh). Thay bằng: trong dải logo (x 25–75 %, y 6–30 % của bản cắt 16 : 9) không có rồng, rùa hay đỉnh tháp; đỉnh tháp chỉ được chạm mép dưới nét lượn của logo.

### 113 `poster` (sinh lượt 2, đính kèm `keyart.png`)
```text
Recompose the attached key art as a tall 1024 x 1536 poster. The white-gold dragon is large in the upper middle, diving down-left, its whole body and both wings inside the frame. The Tree Spirit is huge in the lower left, rising out of the forest with its head at about 45% height, clearly taller than every cliff around it. The Fort's red-roofed towers are small in the lower-right corner. Fewer elements: at most three glowing arrow streaks, a few lanterns, and calm mist across the bottom 15%. The top 22% is storm sky with soft god rays, not flat dark, kept empty for the logo. Same characters, place, colours and light as the attached image.
```
Kiểm thêm: ở 384 px, cây phải cao hơn mọi vách quanh nó; cánh rồng không chạm mép.

### 114, bảy ô vòng (làm lại hậu kỳ từ các lượt đã có; chỉ sinh thêm `sky-night-b`)
1. **Không làm phẳng mép.** Vòng xếp A, A lật, A, A lật nên mọi chỗ nối giữa ô và bản lật của chính nó trùng pixel sẵn; không cần dải 8 % lặng, không cần vai phẳng. Giữ núi và mây chạy ra tận mép như trong `.tryN.png`.
2. **Ô núi:** bỏ vai phẳng và khối sương phẳng ở hai mép. Chỉ cần độ cao đường chân núi ở cột 0 và cột cuối bằng nhau: nắn dọc nhẹ 10 % ngoài cùng, không san phẳng. Đáy mờ dần vào màu sương bằng gradient dọc mềm, bắt đầu từ 85–90 %. Các khe giữa đảo phải biến mất.
3. **Chỗ nối a ↔ b** (vòng 140: a.phải ↔ b.phải và b.trái ↔ a.trái; trời ngày cũng vậy):
   - ghép dải [a | b lật], sửa ảnh dải 15 % quanh chỗ nối bằng `Continue the karst range naturally across the middle; keep both sides unchanged.`, rồi cắt lại;
   - hoặc sinh b bằng cách vẽ tiếp từ 25 % mép phải của a.
4. **Vệt tím:** khử sắc khóa ở dải mép 2–3 px bằng cách kéo màu về đá cạnh bên (giảm bão hòa, xoay hue), không lấp bằng màu cùng cột. Soi ×4 cả bốn ô núi.
5. **Ô trời:** lấy lại try1, không ép phẳng hai bên. Chỉ hòa 15 % đáy vào một màu sương chung với lớp 320, bằng gradient mềm, không cắt cứng.
6. **Trời đêm:** sinh thêm `sky-night-b` (đính kèm `sky-night`):
   ```text
   Same night sky style, colours and lanterns as the attached image, but no moon: the milky way continues across, fewer lanterns, high thin clouds.
   ```
   Vòng đêm: a một lần, b ba lần lật xen kẽ. Đây là ảnh thứ mười, cần sửa phiếu.
7. Kiểm nhận: vòng ghép đọc thành một dãy núi và một vòm trời liền; không dải phẳng nào rộng quá 5 % một ô; chấm M trên vòng ghép, không chấm trên ảnh ghép một ô.

### 115, năm khung (hậu kỳ từ try1; `button-active` dựng lại từ nút đã sửa)
1. Dùng tranh try1 làm khung (tooltip cũng dùng **try1**). Cắt theo vật, **giữ độ phân giải gốc**, không thu góc về 32 px.
2. Đặt đường cắt 9-slice ở mép trong của trang trí góc, đo trên bản đã cắt. Ước lượng của tôi:
   - panel khoảng 11 % cạnh (≈ 125 px trên vật 1137 px);
   - tooltip ≈ 85 px;
   - plate: trái và phải ≈ 150 px (đầu mây), trên và dưới ≈ 40 px;
   - button: trái và phải ≈ 110 px, trên và dưới ≈ 40 px.
   Cỡ góc khi hiện do CSS quyết (`border-image-width`, ví dụ góc panel 48–56 px ở 1080p). Ghi thêm `"display"` vào JSON.
3. Rail đá vôi có hoa văn chạm: không kéo giãn, dùng `border-image-repeat: round` (ghi `"repeat": "round"` vào JSON) với đoạn cắt đúng một chu kỳ hoa văn. Nếu lặp thấy lộ, sửa ảnh rail bằng `Make the straight sides plain bevelled limestone moulding, uniform along their length; keep the corners unchanged.`
4. Lòng chữ: giữ ngọc sơn mài của try1, chỉ làm tối lòng (nhân khoảng 0,7) tới khi WCAG ≥ 7; không thay lòng bằng tấm phẳng.
5. `button-active`: lấy đúng `button` đã sửa, thêm ánh hổ phách lên viền vàng (sáng viền trong và quầng ngoài 6–10 px), cùng alpha cộng quầng. Không dùng dáng của bản sinh lại.
6. Đổi kiểm 4 của phiếu: với rail dùng `round`, thay "độ lệch chuẩn luma ≤ 0,05" bằng "đoạn rail lặp liền (thử ghép 3 lần)". Dựng lại mock: ở 1080p, góc đồng và rail đá phải thấy được.

### 137 `armour` (sinh lượt 2)
```text
A broad dragon-scale cuirass seen straight from the front, about as wide as it is tall, with two rounded shoulder plates, overlapping cream scale rows, a thick dark forged-iron rim and one ember stud at the centre; a compact silhouette that fills a square; not a shield, not a pendant.
```
Kiểm: ở 12 và 18 px đọc ra áo giáp có vai; IoU với `shield` ≤ 0,70.

### 137 `danger` (sinh lượt 3)
Nếu điều phối cho rằng tia sét chấp nhận được thì chỉ sửa công cụ: lấy try2, gamma ≤ 1,3, viền sắt sẫm. Còn không, sinh lại:
```text
A red-orange enamel warning crest of hammered iron: a sharp upward-pointing triangle with a jagged glowing ember crack across its centre, a thick dark iron rim, a hot red-orange core; reads as danger at a glance; no letters, no lightning bolt.
```
Hậu kỳ: gamma ≤ 1,3. Kiểm chênh luma ≥ 0,25 trên cỏ ở cả vùng tối và vùng sáng nhờ viền sẫm, không nhờ làm phai.

### 139 `flag-pull` (sinh lượt 3)
```text
An armoured gauntlet at the lower right gripping a broken pole and yanking a tattered violet-grey blight banner up out of a clod of dark earth; the banner is large, about half of the icon, with torn edges and a faint violet glow; the pull reads as a diagonal up to the right.
```

### 139 `swarm` (sinh lượt 2, đính kèm `enemies/thorn-ant.tripo.png`)
```text
Three thorn ants in a tight triangle, matching the attached enemy: dark brown chitin, grey stone-like back plates, short thorns, small yellow-green eyes; seen from a high three-quarter view; big bodies with short thick legs so the group reads at 18 pixels; a faint muted-violet blight glow under them; no gold, no cream armour.
```
Kiểm: ở 18 px vẫn thấy hơn một thân; màu khớp model.

---

## Chỗ lệch trong cùng game

**Wordwoven**
- Màn tựa, keyart, rùa trời (113, 114) cùng một thế giới và bảng màu; rùa của 114 khớp rùa của màn tựa. Tốt.
- Ba thứ ngọc khác nhau:
  - huy hiệu 113: ngọc lục bảo bão hòa;
  - logo: ngọc trắng nhạt;
  - khung 115: ngọc sơn mài gần đen.

  Nên chốt ba mẫu ngọc (sẫm, vừa, nhạt) trong phiếu sau và giữ huy hiệu ở mẫu vừa.
- Rồng trong keyart và poster là kiểu "đồ chơi vinyl" bóng (khớp model 3D) trên nền vẽ gần thực; lệch nhẹ nhưng bắt buộc vì phải khớp model.
- Ruộng bậc thang trên ô 140 và trên màn tựa là vàng chanh rực, ngoài luật cỏ của bible (hue 80–150°, S ≤ 0,55). Khi làm lại hậu kỳ 114 thì hạ bão hòa ruộng.

**Dragonhold**
- 31 icon mới cùng một bộ. Nhưng trong HUD chúng sẽ đứng cạnh các icon kiểu cũ còn dùng (viền mực, khối hoạt hình: `family-bug`, `aura-attack`, `call-wave`, `skill-*`, `gold`, `dragon-heart`). Hai phong cách lẫn trong một thanh HUD; cần một lượt vẽ lại các icon cũ bằng cùng STYLE-UI.
- `shield`, `pause`, `slot-house` cùng dáng tròn (IoU 0,92–0,985 ở 32 px); `deny` và `phase-fight` cùng dáng X. Mỗi cặp nằm ở chỗ khác nhau nên chấp nhận, nhưng đừng đặt hai cái cùng dáng trên một thanh.
- Chưa có ảnh chọn của 119 (màn tựa Dragonhold) lúc làm icon, nên chưa so được với key art của game.

## Ba lo ngại lớn nhất về hướng đi

1. **Hậu kỳ phá tranh tốt để qua số đo.** Ở bốn trong sáu phiếu, lượt sinh đã đạt nhưng bước công cụ làm hỏng nó để đạt một ngưỡng số:
   - hộp tối nung vào nền tựa để qua độ lệch chuẩn luma;
   - vai phẳng và sương phẳng ở ô vòng để qua luật mép;
   - khung UI bị vứt phần vẽ để qua "cạnh kéo ≤ 0,05";
   - gamma 2,6 làm phai `danger` để qua tương phản.

   Codex tự chấm 8 cho cả những bản đó. Đề nghị: mọi phiếu bắt buộc có tờ "bản sinh và bản hậu kỳ cạnh nhau"; cấm bước công cụ xóa phần vẽ; khi ngưỡng số mâu thuẫn với tranh thì dừng và hỏi Claude, không ép.
2. **Cảnh Wordwoven "dày kiểu AI".** Chỗ nào cũng chi tiết và bão hòa như nhau, không có vùng nghỉ, không phân tầng độ sáng. Ảnh mẫu đạt 9 vì có trời rộng yên, một anh hùng, một quái thú. Ta có quy mô và chất liệu, nhưng thiếu khoảng trống và trọng tâm, nên logo và UI phải tranh chỗ với tranh. Prompt sau nên đòi một kế hoạch độ sáng ("40 % khung là trời hay sương yên; chỉ vùng trọng tâm bão hòa đủ") và một trọng tâm.
3. **Thiết kế phiếu cho phông vòng và icon nhỏ.**
   - Phiếu 114 tự gây lỗi: ô một phần tư có mép lặng và vai cố định sẽ luôn thành các đảo lặp lại. Nên chuyển sang toàn cảnh 360° liền (vẽ nối tiếp từng ô từ ô trước, khép vòng bằng sửa ảnh chỗ nối) và trời đêm có đúng một mặt trăng.
   - Icon vẽ khối ở 10–16 px (cỡ 720p) chỉ còn dáng. Ảnh mẫu đặt icon trong ổ tròn kim loại, nét đơn, tương phản cao. Nên làm ổ icon trong bộ khung UI Dragonhold và nâng cỡ tối thiểu lên khoảng 20 px, thay vì thu icon vật phẩm xuống 12 px.
