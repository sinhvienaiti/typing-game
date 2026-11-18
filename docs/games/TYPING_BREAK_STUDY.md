# Typing Break: soi từng khung hình để học cách gõ và ô kỹ năng

Ngày 29/10/2026 · Nguồn: `typing_break.mov` ở gốc repo cha (83,45 s, 2034×1140, 60 fps) · Áp dụng cho Last Line (`games/typing-survival`), Dragonhold (`games/dragon-hold`), Wordwoven (`games/typing-defense`).

**Lời anh:** tua thật chậm để thấy từng cách xử lý khi gõ, và các hiệu ứng ô kỹ năng làm rất đẹp; nên học.

**Ta học gì, không học gì.** Typing Break dựng hình bằng khối cơ bản: hình trụ, quả cầu, khối hộp, nền phẳng một màu. Ta học cảm giác gõ và chuyển động của UI. Ta không chép đồ họa. Mức đồ họa của ta vẫn theo `ART_ACCEPTANCE.md` và chuẩn `VFX_STANDARD.md`.

**Video là gì.** Đây là bản quay màn hình. Máy đang mở trang Steam của Typing Break rồi phát video của một YouTuber (logo tròn xanh ở góc phải dưới). Vì vậy:
- Có lớp điều khiển YouTube từ 5,85 s đến 9,75 s và dòng chữ "Buy Typing Break" của Steam.
- Video bị cắt cảnh nhiều lần. Có cảnh cắt rơi đúng lúc nhận sát thương (§2.8).
- Ảnh bị nén. Viền sáng và tia mảnh nhòe hơn trong game thật một chút.
- File không có track âm thanh (§3).

**Cách làm.**
1. Tách khung 4 fps, làm 14 tờ tổng quan (24 khung mỗi tờ, có giờ).
2. Đo độ sáng và độ đổi theo từng khung 60 fps cho sáu vùng: toàn khung, thanh nhập, ô trái, ô phải, thanh máu, sân. Từ đó tìm cảnh cắt và lóe sáng.
3. Chọn 2–3 lần cho mỗi loại khoảnh khắc. Tách mọi khung 60 fps quanh sự kiện. Làm tờ 20 khung liền nhau, ghi số khung và ms so với sự kiện. Cắt phóng 1,5–2× vào ô kỹ năng, thanh nhập, quái khi trúng.
4. Số đo sáng là giá trị xám trung bình 0–255 của vùng, lấy mẫu nhỏ. Kích thước tính trên khung 2034×1140. Ô kỹ năng cao khoảng 95 px; chữ hoa trong ô cao khoảng 55 px.

Mọi ảnh nằm trong `tmp/typing-break-study/` (media, không vào Git). Số khung `fNNNN` là số khung tuyệt đối trong video (khung = giây × 60).

---

## §1 Dòng thời gian của video

| Thời điểm | Cảnh | Chuyện gì xảy ra |
|---|---|---|
| 0,00–5,85 s | Trang Steam | Ảnh bìa Typing Break, trình phát đang tải. Chưa có gameplay. |
| 5,85–12,70 s | Cảnh A: nền nâu, hành lang tường tím | Ô kỹ năng mang **từ thường**: trái `sour` (Turret, đếm 2), `five` (Fury); phải `path`→`scream` (Shotgun, đếm 2), `tire`→`law`→`sense` (Pistol). Shotgun bắn quạt tia mỗi 500 ms. Số sát thương chồng lên nhau. HP 92/100. 10,50 s gõ xong `SCREAM`; 12,25 s gõ xong `SOUR`. |
| 12,70 s | Cắt cảnh | Sang một đoạn khác: `derive`, `five`, `hide`, `upon`. Có quang sai màu (tách RGB) tắt dần 530 ms. HP còn 87/100. |
| 13,88 s | Chữ khu vực | "Stronghold / Nightfall" hiện ở đầu hành lang, "EXP:10" màu vàng trên thanh máu. |
| 13,98–21,70 s | Bảng nâng cấp | Tấm tím đập xuống. Ba thẻ A `Affix: Blood`, B `Eye for an Eye Lv.3`, C `Sturdy`. Nút REROLL (446, Spend 0 EXP). Đứng yên 7,7 s. |
| 21,75–31,15 s | Cảnh B: nền ô liu, quái là quả cầu đỏ có vòng máu | Ô mang **tên kỹ năng**: trái FLAME (2), TURRET, FURY; phải SNIPER, LASER, PISTOL (2). Gõ nhiều tên rồi bắn một lần. Laser xanh lơ, Flame đốt cam. 26,62 s SNIPER bắn. 27,20–27,75 s gõ `FLAME`. 30,25 s thanh nhập "FLAME S" (khung trong ảnh chụp của anh: `tmp/typing-break-study/stills/still_30.25.jpg`). |
| 31,18–41,70 s | Cảnh C: nền hồng tím, quái là khối đỏ, boss vòm có cung tím | `dance`, `five` / `pear`, `key`→`whom`→`love`→`tea`→`cow`→`ax`. 36,70–37,05 s một vệt cọ hồng quét kín màn hình. HP 73/100. |
| 41,75–49,65 s | Cảnh D: nền xanh ngọc, rào vàng | SANGUIVORE, FLAME, TURRET, FURY / SNIPER, LASER, PISTOL (3). Xếp hàng "FLAME TURRET LASER" rồi bắn ở 44,67 s. Tiếp "FLAME PISTOL" 46,25 s, "LASER" 47,6 s, "SNIPER" 48,8 s. |
| 49,70–60,30 s | Cảnh E: nền xanh rêu, boss nhiều khối có nhãn chữ (`make`, `defeat`, `indoor`) | Chỉ còn FURY và PISTOL. Thanh nhập giữ "FURY PISTOL". Phá khối boss có vết loang hồng ở 55,2 s, 57,5 s, 59,5 s. |
| 60,35–82,60 s | Cảnh F: nền cam, nhiều nhà đỏ | `cost`/`five`→`thing` / `weekly`, `hat`, `goose`, `god`, `fate`, `knot`, `king`, `grave`, `tool`, `answer`, `tea`, `nine`, `pint`. Gõ xong là bắn ngay. Số chí mạng 1456 ở 61,8 s. 64,0 s và 80,5 s có nổ lớn sát tường; 80,8 s "+3", HP 84→87. |
| 82,65–83,45 s | Trang Steam | Ảnh bìa game khác (Blood Typers). Hết. |

Tờ tổng quan: `tmp/typing-break-study/sheets/overview-sheet-01.jpg` đến `tmp/typing-break-study/sheets/overview-sheet-14.jpg` (mỗi tờ 6 s). HP theo thời gian: `tmp/typing-break-study/locate/sheet-hp-readout.jpg`.

**Luật chơi đọc được từ hình.**
- Mỗi ô kỹ năng là một tấm có chữ. Gõ đúng chữ trên tấm thì kích hoạt kỹ năng của tấm.
- Ở chế độ tên kỹ năng (cảnh B, D, E), các tên gõ ra xếp hàng trong thanh nhập, cách nhau bằng dấu cách. Mọi tấm trong hàng có viền trắng. Một phím (có lẽ Enter) bắn cả hàng cùng lúc.
- Ở chế độ từ thường (cảnh A, C, F), gõ xong một từ là kỹ năng chạy ngay. Từ trên tấm đổi sau mỗi lần dùng.
- Số nhỏ ở góc phải dưới tấm là số lần dùng còn lại. Tấm hết lượt chuyển tối và có vạch nạp.

---

## §2 Từng loại khoảnh khắc

Mỗi mục có bảng từng lớp theo khung. "0 ms" là khung sự kiện. Tờ "20 khung liền" chạy từ −100 ms đến +217 ms; tờ "quét" lấy cách một khung đến khoảng +600 ms.

### 2.1 Đứng yên (idle-1 f1710, idle-2 f4070)

| Lớp | Thấy gì |
|---|---|
| Tấm kỹ năng | Đứng im. Không nhấp nhô, không thở, không lóe. |
| Thanh nhập | Trống. Không có con trỏ nhấp nháy. |
| Sân | Quái trôi xuống chậm. Đạn quái là quả cầu đỏ phát sáng nhỏ, bay thẳng về người chơi. |
| Mảnh vụn | Mảnh quái chết nằm lại trên nền. Chúng là lịch sử trận đánh. |

Nhận xét: khi đứng yên, UI hoàn toàn tĩnh. Mọi chuyển động của UI đều do phím gây ra. Nhờ vậy mỗi phím đều nổi rõ.

Tờ: `tmp/typing-break-study/moments/idle-1/sheet-idle.jpg`, `tmp/typing-break-study/moments/idle-1/sheet-consec-20f.jpg`, `tmp/typing-break-study/moments/idle-2/sheet-consec-20f.jpg`.

### 2.2 Gõ một chữ

**Lần 1, chữ F của FLAME ở cảnh B (f1632).** Chữ F khớp cả FLAME và FURY.

| Khung | ms | Tấm kỹ năng (cắt 1×) | Thanh nhập (cắt 2×) |
|---|---|---|---|
| f1626–1631 | −100…−16 | Yên. | Trống. |
| f1632 | 0 | Một chữ F khổng lồ màu tím nhạt (#D9CCE6) hiện trên **mọi tấm khớp** (FLAME và FURY). Cao khoảng 3,4× chữ trên tấm. Đặt lệch lên trên gần một chiều cao tấm, lệch trái, nghiêng ~8° theo chiều kim đồng hồ. Phẳng, không bóng. | Chữ F hiện ngay, cỡ lớn, kèm chùm tia trắng 4–8 cánh nhọn ở tâm chữ. |
| f1633 | +16 | F nhỏ lại ~3,0×, trượt xuống phía chữ của nó. | Một đĩa trắng đặc (Ø ≈ 1,9× chiều cao chữ, mép mờ) che chữ. |
| f1634 | +33 | ~2,5×, gần chạm chỗ. | Đĩa vỡ thành mảnh trắng; vòng bắt đầu hiện. |
| f1635 | +50 | **Đóng xuống 1,0×** đúng chữ F của tấm. Chữ trên tấm giữ màu tím nhạt, nghĩa là đã gõ. | Vòng tối (đen nâu) dày, mảnh trắng bay ra. |
| f1636–1637 | +66…+83 | Chữ L tiếp theo bắt đầu đóng xuống, chỉ trên FLAME. Chữ F của FURY trở lại màu trắng ngà ngay khung đó (FURY không còn khớp). | Vòng nở ra ~1,3× rồi thành nét trắng. |
| f1638 | +100 | L đóng xuống. | Khung "đen": mảnh và vòng màu tối, gần như đảo màu, chỉ 1 khung. |
| f1639–1645 | +116…+216 | A đóng xuống ở f1643. | Sau mỗi chữ: lại đĩa trắng → vòng tối → cung mảnh. Chữ đứng yên ở cỡ cuối, màu trắng ngà, bóng đổ tối lệch xuống phải ~4 px. |

**Lần 2, chữ C của COST ở cảnh F (f4121), cắt 1,5×.**

| Khung | ms | Thanh nhập |
|---|---|---|
| f4115–4120 | −100…−16 | Trống. |
| f4121 | 0 | Chữ "c" hiện ở **~2,3×** cỡ cuối, màu trắng xám, đặt cao (đè lên rào và thanh máu). Một tia lửa trắng nhỏ ở tâm, 2–3 vệt trắng xiên. |
| f4122 | +16 | Đĩa trắng đặc Ø ≈ 1,9× chiều cao chữ, có quầng. Bên trong là bóng mảnh tối. Vệt trắng và đen tỏa ra. Cỡ chữ đã về 1,0× nhưng bị đĩa che. |
| f4123 | +33 | Đĩa thành **vòng trắng dày** (nét ≈ 20% bán kính). |
| f4124–4125 | +50…+66 | Vòng chuyển **tối** (gần đen), dày hơn, Ø ≈ 2,1× chữ. Mảnh trắng bên trong. |
| f4126 | +83 | Vòng thành **cung trắng mảnh** hở một phía, Ø ≈ 2,3× chữ. Chữ C hiện rõ, đứng yên. |
| f4127–4129 | +100…+133 | Cung đổi sang nét tối, xoay ~40° mỗi khung, mờ dần. |
| f4130 | +150 | Sạch. Chỉ còn chữ C. Tổng hiệu ứng một chữ: **150 ms**. |
| f4132 | +183 | Chữ O tiếp theo: lặp lại y hệt. |

Đây chính là "con trỏ vòng" trong ảnh của anh: vòng cung tối quanh chữ vừa gõ, không phải con trỏ thật.

**Lần 3, gõ FURY ở cảnh E (f3315).** F (f3312), U (f3315), R (f3322), Y (f3327) đều có chữ tím lớn đóng xuống tấm FURY và vòng ở thanh nhập. Nhịp gõ của người chơi 80–120 ms một chữ. Hiệu ứng 150 ms nên các chữ gối lên nhau. Không chữ nào bị chậm lại vì hiệu ứng.

Thêm:
- Chữ trong thanh nhập luôn căn giữa. Thêm chữ thì cả dòng nhảy sang trái, không có chuyển tiếp.
- Rung màn hình: đo vị trí thanh máu thấy cả cảnh dịch lên 12–14 px rồi về chỗ, có vọt nhẹ ~4 px, xong trong ~130 ms (f1638–1646). Rung này trùng một phát bắn, không phải mỗi phím. Phần lớn phím không làm rung.

Tờ: `tmp/typing-break-study/moments/letter-1/sheet-slots-a.jpg`, `tmp/typing-break-study/moments/letter-1/sheet-input-2x-a.jpg`, `tmp/typing-break-study/moments/letter-2/sheet-input-2x.jpg`, `tmp/typing-break-study/moments/letter-2/sheet-scan-step2.jpg`, `tmp/typing-break-study/moments/letter-3/sheet-hud-strip.jpg`, `tmp/typing-break-study/locate/sheet-input-sceneB-a.jpg`, `tmp/typing-break-study/locate/sheet-input-sceneB-b.jpg`, `tmp/typing-break-study/locate/sheet-input-hat.jpg`, cùng các tờ `sheet-consec-20f.jpg` trong `letter-1`, `letter-2`, `letter-3`.

### 2.3 Gõ sai

**Không tìm thấy lần gõ sai nào trong 83 s.** Đã làm:
- Quét điểm ảnh đỏ trong thanh nhập ở cả 5004 khung. Chỉ 4 khung có đỏ, đều do thanh máu lọt vào vùng cắt khi màn hình rung.
- Xem từng khung lúc gõ "FURY PISTOL" (f3333–3386), "HAT" (f3774–3827) và các đoạn gõ ở cảnh B. Người chơi gõ sạch.

Có thể game bỏ qua phím không khớp tấm nào (không hiện chữ). Không có bằng chứng. Phản hồi gõ sai của ta đã có ở cả ba game và nên giữ (§5).

Tờ: `tmp/typing-break-study/moments/wrong-1/sheet-input-no-error.jpg`.

### 2.4 Gõ xong một từ

**Lần 1, KEY trên tấm Pistol (đếm 5) ở cảnh C, f1914 = khung ngay sau chữ Y.**

| Khung | ms | Tấm "key" (cắt 1×) |
|---|---|---|
| f1907–1913 | −116…−16 | Chữ e rồi y đóng xuống như §2.2. Tấm màu xanh đen (#3A3D55) có **một dải sáng hơn (tím nhạt) ở bên trái**, rộng ~30% tấm. |
| f1914 | 0 | **Viền trắng bật lên**: dày, có quầng rộng, mép ngoài vượt tấm ~10% mỗi phía. Cả tấm sáng lên: vùng ô phải tăng từ 108 lên **128 (+18%)**. |
| f1915 | +16 | Viền còn to; tấm lệch lên trái vài px (giật). Sáng 124. |
| f1916–1918 | +33…+66 | Viền co về sát tấm, dày ~8 px, màu trắng hồng (#F4E4F0), quầng mềm. Sáng 118. |
| f1919–1937 | +83…+383 | Viền đứng yên. Dải sáng bên trái co dần từ ~30% xuống ~12%. Súng của người chơi bắn từng phát. |
| f1939 | +416 | Viền tắt. Tấm tối hẳn. Một **vạch sáng mảnh ở mép dưới** mọc từ trái sang phải: 25% → 40% → 65% → 80% trong ~116 ms. |
| f1947 | +550 | Viền bật lại (lóe lần hai), tấm sáng lên. |

**Lần 2, LOVE trên cùng tấm, rồi đổi từ (f2135).** Cả vòng từ lúc gõ đến lúc đổi từ.

| Khung | ms | Thấy gì |
|---|---|---|
| f2113–2133 | −366…−33 | l, o, v, e đóng xuống từng chữ. |
| f2135 | 0 | Viền trắng bật, tấm sáng. |
| f2135–2149 | 0…+233 | Viền đứng; dải sáng trái co ~40% → ~12%. |
| f2151–2157 | +266…+366 | Viền tắt; vạch nạp ở mép dưới mọc 0 → 70%. |
| f2159–2167 | +400…+533 | Viền lóe lần hai, rồi đứng. |
| f2169 | +566 | Viền tắt. Dải sáng trái **đầy lại ~90%** trong một khung. |
| f2170–2175 | +583…+666 | **Từ "love" bị bóp ngang**: rộng 1,0 → 0,75 → 0,35 → 0,25 → một vạch → mất. 100 ms, nhanh dần (ease-in). Chiều cao chữ giữ nguyên. |
| f2176–2179 | +683…+733 | Tấm trống 66 ms. |
| f2180 | +750 | Từ mới "tea" hiện ngay ở cỡ đủ, không phóng to dần. Dải sáng bắt đầu co lại từ đầu. |

Dải sáng bên trái có lẽ là đồng hồ của từ (thời gian trước khi từ tự đổi, hoặc cửa sổ thưởng). Hình không cho biết luật.

**Lần 3, FATE ở cảnh F (f3962).** Gõ xong thì viền tấm `fate` bật sáng (ánh ấm) ở f3963. Thanh nhập giữ "FATE" ~130 ms rồi xóa ở f3970. Súng bắn ở f3972 (lóe nòng lớn). Từ `fate` bị bóp ngang f3972–3975 và tấm trống đến f3979. Chế độ từ thường không cần Enter.

Tờ: `tmp/typing-break-study/moments/word-1/sheet-slot-a.jpg`, `tmp/typing-break-study/moments/word-1/sheet-slot-b.jpg`, `tmp/typing-break-study/moments/word-1/sheet-scan-step2.jpg`, `tmp/typing-break-study/moments/word-2/sheet-word-cycle-love-tea.jpg`, `tmp/typing-break-study/moments/word-3/sheet-hud-strip.jpg`, cùng `sheet-consec-20f.jpg` trong `word-1`, `word-2`, `word-3`.

### 2.5 Chọn ô kỹ năng, chờ và bắn

**Lần 1, chọn FLAME ở cảnh B (chữ E cuối đóng xuống f1650; viền bật f1651).** Cắt 1,5× tấm FLAME.

| Khung | ms từ chữ cuối | Thấy gì |
|---|---|---|
| f1650 | 0 | E khổng lồ đóng xuống. |
| f1651 | +16 | **Viền trắng nổ ra**: dày ~25 px (≈ 1/4 chiều cao tấm), mép ngoài vượt tấm ~11% mỗi phía, quầng trắng ấm. Vùng ô trái sáng từ 103 lên **144 (+40%)**. Toàn khung +6% (85→90). |
| f1652 | +33 | Viền còn to. Sáng 140. |
| f1653–1655 | +50…+83 | Viền co: mép ngoài vượt ~5% rồi ~3%. Sáng 137 → 132 → 126. |
| f1656–1661 | +100…+183 | Viền dày ~12 px, vượt ~2%. Sáng 117–124 (có một nhịp nhỏ). |
| f1662 trở đi | +200… | Viền đứng ở ~8 px, quầng mềm. Tấm hơi sáng hơn lúc thường. Hết. |

Đường cong: nhảy vọt trong 1 khung, rồi tắt dần kiểu hàm mũ. Một nửa độ sáng mất sau ~70 ms; về gần nền sau ~100 ms; viền ổn định sau ~200 ms.

**Lần 2, chọn LASER rồi bắn cả hàng ở cảnh D.** Thanh nhập: "FLAME TURRET LASER".

| Khung | ms từ lúc bắn (f2680) | Tấm | Thanh nhập và sân |
|---|---|---|---|
| f2672–2673 | −133…−116 | FLAME, TURRET có viền trắng mảnh (đang xếp hàng), mặt tấm sáng nhạt. | "…TURRET LASE", vòng cung tối. |
| f2674 | −100 | R đóng xuống LASER. Viền LASER nổ to, mép vượt ~12%, mặt tấm ngả trắng be. Vùng ô phải 122 → **172 (+41%)**. | Chùm tia trắng ở chữ R. |
| f2675–2677 | −83…−50 | Viền giữ to, co dần ~1,05×. Sáng giữ 169 (giữ 66 ms). | Mảnh tối và trắng. |
| f2678–2679 | −33…−16 | Viền về ~6 px. Sáng 143 → 140. | "…TURRET LASER" đầy đủ, cung trắng. |
| f2680 | 0 | **Mọi viền tắt cùng một khung.** TURRET (không có số đếm) chuyển tối (hồng xám đục, ~#6E5A62) và có ô hồng nhỏ ở mép trái (~12%), co về một nét mảnh ở f2682. FLAME (đếm 2) vẫn hồng sáng. Số đếm không đổi. | Thanh nhập xóa sạch; chỉ còn bóng mờ chữ R cuối 1–2 khung. **Laser bắn**: tia đứng xanh lơ, lõi trắng, rộng ~36 px, từ súng lên tận đỉnh màn hình. Sao trắng lóe ở chân tia. |
| f2681–2693 | +16…+216 | TURRET tối, chờ nạp. | Lửa cam bám quái (Flame), số sát thương 26, 6, 2 xếp chồng. Tia kéo dài hơn 600 ms. |

TURRET sáng lại khoảng 1,8 s sau (tờ tổng quan 46,5 s).

**Lần 3, FURY bật lại ở cảnh E (f3406).** Tấm FURY có viền trắng to f3406–3408, về viền mảnh từ f3409 (~50 ms). PISTOL giữ viền mảnh suốt. Trong cảnh này, tấm có viền nghĩa là kỹ năng đang chạy.

Tờ: `tmp/typing-break-study/moments/skill-1/sheet-flame-plate-select.jpg`, `tmp/typing-break-study/moments/skill-2/sheet-right-slots-bar.jpg`, `tmp/typing-break-study/moments/skill-2/sheet-left-slots.jpg`, `tmp/typing-break-study/moments/skill-2/sheet-scan-step2.jpg`, `tmp/typing-break-study/moments/skill-3/sheet-hud-strip.jpg`, cùng `sheet-consec-20f.jpg` trong `skill-1`, `skill-2`, `skill-3`.

### 2.6 Đạn đang bay

**Lần 1, Pistol ở cảnh E (f3010).** Một phát mỗi 180–200 ms.

| Khung | ms | Thấy gì |
|---|---|---|
| f3009 | −16 | Tia lửa trắng nhỏ dựng đứng ở nòng. |
| f3010 | 0 | **Quầng sáng ấm** (#FFF1DC) tròn quanh nòng, bán kính ~150 px, mép rất mềm, chiếu sáng nền. Một **kim trắng** dài ~250 px, rộng 2–3 px, đầu nhọn bắt đầu bay. |
| f3011–3015 | +16…+83 | Kim bay lên ~130 px mỗi khung (~8000 px/s, vượt hết sân trong ~100 ms). Quầng tắt trong 3–4 khung. Kim hơi nghiêng theo hướng mục tiêu. |
| f3016 | +100 | Trúng (xem §2.7). |

**Lần 2, Laser ở cảnh B (f1365).** Tia liên tục xanh lơ (viền #7FD3E6, lõi trắng), rộng ~36 px, chạy hết chiều cao màn hình, kéo dài hơn 700 ms. Sao trắng ở chân tia chớp tắt từng khung. Tia quét nhẹ theo góc. Quái dính Flame có viền cam phát sáng và lửa nhỏ bay lên.

**Lần 3, Shotgun ở cảnh A (f375).** Một phát mỗi 500 ms.
- f375 (0): một vương miện tia trắng ngắn ở nòng (lóe báo trước, 1 khung).
- f376–377 (+16…+33): quầng trắng bán kính ~330 px. Toàn khung sáng 75 → 88 (+17%). Quạt 8–10 vệt trắng, góc ~60°.
- f379–383 (+66…+133): sao nổ vàng trắng có gai (~80 px) ở chỗ vệt chạm tường và quái.
- f385–391 (+166…+266): vệt mảnh dần và tắt. Sáng về 75 sau ~250 ms.

Tờ: `tmp/typing-break-study/moments/projectile-1/sheet-scan-step2.jpg`, `tmp/typing-break-study/moments/projectile-2/sheet-scan-step2.jpg`, `tmp/typing-break-study/moments/hit-1/sheet-scan-step2.jpg`, cùng `sheet-consec-20f.jpg` trong `projectile-1`, `projectile-2`, `hit-1`.

### 2.7 Trúng, hạ, chí mạng

**Trúng: kim Pistol vào khối boss (f3016), cắt 2×.**

| Khung | ms | Mục tiêu | Số sát thương |
|---|---|---|---|
| f3016 | 0 | Khối bị trúng chuyển **trắng đặc**, cháy sáng, có quầng. Tia lửa trắng nhỏ ở chân. | — |
| f3017–3019 | +16…+50 | Vẫn trắng, mờ dần một chút. | "10" hiện ở **~3×** cỡ cuối, trắng ngà (#EDE6DA), bóng tối, lệch trái dưới chỗ trúng. |
| f3020–3024 | +66…+133 | Trắng → xám nhạt → về màu gốc. | Co 3× → ~1,3×, trượt lên phải. Nhanh lúc đầu, chậm lúc cuối (ease-out). |
| f3025–3032 | +150…+266 | Bình thường. | Đứng ở 1,0× (chữ cao ~35 px), trôi lên rất chậm. |

**Trúng nhiều: SNIPER vào 4 quả cầu ở cảnh B (f1599).** Cả 4 quả chuyển trắng đặc có quầng cùng lúc. Giữ trắng ~3 khung (50 ms). Nhạt dần sang hồng rồi về đỏ trong ~200 ms (f1601–1613). Vòng máu của mỗi quả hiện lại, ngắn đi. Số "50" lớn trên mỗi quả.

**Hạ: phá một khối boss ở cảnh E (f3309).**

| Khung | ms | Thấy gì |
|---|---|---|
| f3307 | −33 | "21" lớn bật ra, tia lửa trắng. |
| f3309 | 0 | Khối chuyển trắng. Hàng loạt số 45, 35 bung ra. |
| f3311–3313 | +33…+66 | **Vết loang sơn hồng** (#F08A8A) bung từ chỗ trúng, mép nhòe có gai, to gấp ~1,5× sau mỗi 2 khung. |
| f3315 | +100 | Loang lớn nhất (~300×250 px). Một **vòng mực đen dày** nở ra (bán kính ~120 px), đĩa trắng phía sau. |
| f3317–3325 | +133…+266 | Loang lan, vệt mực đen chém ngang. Vòng nở ~180 px và mảnh dần. Hồng bắt đầu vỡ thành mảnh. |
| f3327–3331 | +300…+366 | Loang tan thành mảnh, co lại. Khối boss biến mất. Mảnh vụn tím xám nằm lại trên nền. |

**Hạ: nhà nổ sát tường ở cảnh F (f4831).** Toàn khung sáng 100 → **124 (+23%)**, giữ 5 khung (83 ms). Rồi **tối hơn nền** (97–99) vì khói mực đen trong ~150 ms. Sau cùng là mảnh đỏ văng ra và nằm lại.

**Chí mạng: số 1456 ở cảnh F (f3707).** Số hiện ở **~2,5×**, to bằng một phần ba hành lang. Co về ~1,2× trong ~100 ms. Đứng lại hơn 1 s. Màn hình +12% trong 3 khung. Không có hiệu ứng combo riêng: không bộ đếm combo, không chữ "COMBO". Cái gọi là combo ở đây chỉ là nhiều kỹ năng bắn cùng lúc (§2.5).

Tờ: `tmp/typing-break-study/moments/projectile-1/sheet-hit-2x.jpg`, `tmp/typing-break-study/moments/kill-1/sheet-scan-step2.jpg`, `tmp/typing-break-study/moments/kill-2/sheet-scan-step2.jpg`, `tmp/typing-break-study/moments/combo-1/sheet-scan-step2.jpg`, `tmp/typing-break-study/moments/heal-1/sheet-scan-step2.jpg`, cùng `sheet-consec-20f.jpg` trong `kill-1`, `kill-2`, `combo-1`.

### 2.8 Nhận sát thương (damage-1, f762 = khung đầu sau cảnh cắt)

HP từ 92/100 thành 87/100 qua một cảnh cắt. Đoạn mới mở đầu khi hiệu ứng đang mạnh nhất. Vì vậy không biết khung bắt đầu. Có lẽ đây là phản hồi nhận đòn.

| Khung | ms | Thấy gì |
|---|---|---|
| f762–f779 | 0…+283 | **Quang sai màu** tỏa từ tâm: viền chữ và vật tách thành đỏ, xanh lá, xanh lam. Tách mạnh nhất ở mép màn hình, ~20–30 px. Chữ trên tấm như cầu vồng. Thanh máu đỏ đậm hơn thường. |
| f782–f791 | +333…+483 | Tách giảm rõ. |
| f794 | +533 | Còn rất nhẹ. |
| f797 | +583 | Hết. |

Đường cong: giữ gần như phẳng ~300 ms, rồi tắt nhanh trong ~230 ms (ease-in khi tắt). Không thấy rung màn hình hay chớp đỏ toàn khung.

Tờ: `tmp/typing-break-study/moments/damage-1/sheet-hud-crop.jpg`, `tmp/typing-break-study/moments/damage-1/sheet-consec-20f.jpg`.

### 2.9 Lên cấp, nâng cấp (levelup-1, f839 = tấm tím xuất hiện)

| Khung | ms | Thấy gì |
|---|---|---|
| f833 | −100 | "Stronghold / Nightfall" hiện ở đầu hành lang: chữ đơn cách, giãn chữ, trắng mảnh. "EXP:10" màu vàng đè thanh máu. |
| f839 | 0 | **Một tấm tím (#6A2BB0) to bằng hành lang đập từ trên xuống**, đã che một phần ba sân. Nút REROLL nằm trên tấm. |
| f841 | +33 | Tấm che kín hành lang. Các tấm kỹ năng hai bên tối đi. "EXP:10" ở đáy. |
| f843 | +66 | Thẻ A bay vào từ phải trên, thẻ B từ trái. |
| f845–847 | +100…+133 | Thẻ C bay vào từ phải. Mỗi thẻ trễ nhau ~1 khung. |
| f849 | +166 | Ba thẻ đứng yên. Không nảy, không vọt. |

Thẻ: nền xanh đen (#2B2F3F), ô vuông trắng có chữ đen A/B/C (phím chọn), tiêu đề chữ đơn cách, mô tả nhỏ. REROLL: tấm xám, chữ đậm, ô cam (#C77B2E) ghi giá. Chọn bằng cách gõ chữ cái của thẻ.

Tờ: `tmp/typing-break-study/moments/levelup-1/sheet-scan-step2.jpg`, `tmp/typing-break-study/moments/levelup-1/sheet-consec-20f.jpg`.

### 2.10 Chuyển UI

**Lần 1, đổi từ trên tấm (ui-1, f2169).** Xem bảng lần 2 ở §2.4: bóp ngang 100 ms, trống 66 ms, từ mới hiện ngay. Đồng hồ trái đầy lại cùng khung bắt đầu bóp.

**Lần 2, vệt cọ quét kín màn hình (ui-2, f2208).** Những nét cọ hồng cá hồi (#E89A94, gần đục) xoáy vào từ trên (f2202), phủ ~70% màn hình ở f2208–2216, thoát ra phía dưới ở f2220–2222. Tổng ~330 ms. Sau vệt cọ, quái đã ở chỗ khác, như có một bước nhảy thời gian. Không chắc đây là chuyển cảnh của game hay của người dựng video.

**Lần 3, hồi máu (heal-1, f4849).** Chữ "+3" màu xanh lá hiện ngay cạnh súng, không phóng to. Số máu đổi 84 → 87 và thanh máu dài ra **ngay trong một khung**, không chạy dần.

Tờ: `tmp/typing-break-study/moments/ui-1/sheet-wordswap.jpg`, `tmp/typing-break-study/moments/ui-2/sheet-scan-step2.jpg`, `tmp/typing-break-study/moments/heal-1/sheet-consec-20f.jpg`.

---

## §3 Âm thanh

**File không có âm thanh.** `ffprobe` chỉ thấy một luồng: video h264. Không có luồng audio nào để tách WAV hay tìm điểm bắt đầu âm.

Vì vậy không trả lời được: có tiếng cho mỗi chữ không, tiếng gõ xong từ, tiếng trúng, hay cao độ có tăng dần không.

Việc nên làm:
- Nếu anh còn bản có tiếng (video gốc trên YouTube hoặc tự quay khi chơi), chạy lại bước 3 với bản đó. Các khung sự kiện ở §2 dùng lại được.
- Trong lúc chờ, ta giữ âm của ta: Last Line đã có một nốt ngũ cung cho mỗi phím đúng (`typing-feel.ts`). Âm vẫn theo `AUDIO_PIPELINE.md`.

---

## §4 Danh mục kỹ thuật

Mỗi kỹ thuật có tên, thông số và lý do nó dễ đọc. Thời gian tính ở 60 fps (1 khung ≈ 16,7 ms).

| # | Tên | Thông số | Vì sao dễ đọc |
|---|---|---|---|
| T1 | **Chữ đóng dấu lên mọi đích khớp** | Chữ vừa gõ hiện bản sao lớn trên mọi tấm có tiền tố khớp. Cỡ 3,4× → 3,0× → 2,5× rồi **đóng 1,0×** ở khung thứ 4 (~50 ms). Bắt đầu cao hơn chữ đích ~1 chiều cao tấm, lệch trái ~0,3 em, nghiêng ~8°, trượt về đúng chỗ. Màu tím nhạt #D9CCE6, phẳng. Chữ đã gõ giữ màu đó. Tấm không còn khớp trả màu ngay trong khung kế tiếp. | Mắt không cần nhìn thanh nhập vẫn biết tấm nào đang khớp. Phím có "trọng lượng": từ trên rơi xuống. Rất nhanh nên không làm chậm người gõ. |
| T2 | **Ấn chữ ở thanh nhập, hai tông** | Khung 0: chữ ~2,3×. Khung 1: đĩa trắng đặc Ø 1,9× chiều cao chữ che chữ, chữ đã về 1,0× bên dưới. Khung 2: vòng trắng dày (nét 20% bán kính). Khung 3–4: vòng tối gần đen, Ø 2,1×. Khung 5: cung trắng mảnh Ø 2,3×, hở một phía. Khung 6–8: cung tối xoay ~40°/khung, mờ dần. Xong ở 150 ms. Kèm 4–8 mảnh nhọn trắng, xen 1 khung mảnh tối. | Trắng và đen cùng có nên đọc được trên mọi nền. Đĩa trắng che lúc chữ đổi cỡ, nên mắt chỉ thấy "đập". Vòng cung làm con trỏ, chỉ chỗ chữ tiếp theo. |
| T3 | **Viền chọn nổ rồi co** | Khung 0: viền trắng ấm, dày ~25% chiều cao tấm, mép ngoài vượt tấm 10–12% mỗi phía, quầng rộng. Vùng tấm sáng +40% (gõ xong một tên) hoặc +18% (gõ xong một từ thường). Có thể giữ 2–4 khung. Rồi tắt kiểu hàm mũ: nửa sáng mất sau ~70 ms; viền về ~8 px và vượt ~2% sau ~100 ms; đứng yên từ ~200 ms. Toàn khung chỉ +6%. | Một khung "chói" báo đã xong, rồi viền mảnh ở lại báo trạng thái. Lóe gắn vào đúng tấm, không chói cả màn hình. |
| T4 | **Hàng chờ nhiều kỹ năng, bắn một lần** | Tên gõ ra xếp trong thanh nhập, cách nhau dấu cách. Mỗi tấm trong hàng giữ viền mảnh và mặt sáng nhạt. Lúc bắn: mọi viền tắt **cùng một khung**, thanh nhập xóa, mọi kỹ năng ra cùng lúc. | Người chơi thấy rõ mình đã "nạp" gì. Lúc bắn có một khoảnh khắc gọn, đồng bộ. |
| T5 | **Tấm hết lượt: tối và vạch nạp** | Tấm hết lượt đổi sang màu đục tối (~#6E5A62), có ô màu ở mép trái rồi một nét mảnh mọc dần. Tấm còn lượt giữ màu sáng. Nạp xong (~1,8 s với TURRET) thì sáng lại. | Phân biệt "dùng được" và "đang chờ" chỉ bằng độ sáng. Đọc được bằng khóe mắt. |
| T6 | **Đồng hồ của từ trong tấm** | Một dải sáng hơn nằm sau chữ, ở mép trái, co dần. Khi từ đổi, dải đầy lại ~90% trong một khung. | Báo thời gian mà không cần số hay vạch riêng. |
| T7 | **Bóp ngang để đổi từ** | Từ cũ bị bóp chiều ngang 1,0 → 0 trong 100 ms, nhanh dần (ease-in). Trống 66 ms. Từ mới hiện ngay ở cỡ đủ. Tổng ~180 ms. | Giống lật một tấm bảng. Khoảng trống ngắn giúp mắt biết đây là từ mới, không phải từ cũ bị sửa. |
| T8 | **Nhịp viền khi kỹ năng đang chạy** | Kỹ năng kéo dài (Pistol): viền sáng 270–420 ms; tắt và một vạch nạp mảnh ở mép dưới chạy 0 → 80% trong ~116 ms; rồi viền lóe lại. Lặp lại tới khi hết. | Tấm "thở" theo nhịp bắn. Người chơi biết kỹ năng còn chạy và lúc nào ra phát tiếp. |
| T9 | **Chớp trắng mục tiêu** | Cả quái hoặc khối chuyển trắng đặc có quầng. Giữ 2–3 khung (33–50 ms). Về màu gốc trong 130–200 ms. | Báo trúng rõ nhất có thể, trên mọi màu quái. |
| T10 | **Số sát thương đập** | Hiện ở ~3× (chí mạng ~2,5× của cỡ lớn hơn), co về 1,0× trong ~150 ms, nhanh lúc đầu. Chữ đứng đậm hẹp, trắng ngà #EDE6DA, bóng tối. Số lớn có ánh vàng. | Lúc đầu to để thấy, sau nhỏ để không che. |
| T11 | **Quầng nòng và kim đạn** | Quầng ấm #FFF1DC tròn quanh nòng, bán kính ~150 px (Pistol) đến ~330 px (Shotgun), sáng toàn khung tới +17%, tắt trong 4–15 khung. Đạn là kim trắng 2–3 × 250 px, ~8000 px/s. Laser: cột xanh lơ ~36 px, lõi trắng, sao ở chân. | Quầng chiếu sáng nền nên phát bắn "có sức". Kim mảnh và nhanh nên không rối mắt. |
| T12 | **Nổ hai tông và vết loang** | Khung đầu: trắng (đĩa hoặc toàn vùng, +23% sáng, 1–5 khung). Rồi mực đen: vòng dày, vệt chém, khói (tối hơn nền 2–3%, ~150 ms). Rồi màu: loang sơn hồng #F08A8A hoặc mảnh vụn. Cùng ngôn ngữ với T2, chỉ to hơn. | Cùng một bộ hình (đĩa trắng, vòng đen, mảnh nhọn) cho phím, trúng và nổ. Cả game trông như một hệ thống. |
| T13 | **Mảnh vụn nằm lại** | Mảnh của quái chết nằm trên nền suốt màn. | Sân kể lại trận đánh; người chơi thấy mình đã làm được nhiều. |
| T14 | **Quang sai màu khi nhận đòn** | Tách RGB tỏa từ tâm, ~20–30 px ở mép. Giữ ~300 ms, tắt trong ~230 ms. Không rung, không chớp đỏ. | Báo bị đánh bằng cả màn hình mà không che chữ cần gõ. |
| T15 | **Bảng nâng cấp đập xuống** | Tấm nền rơi từ trên trong 2 khung. Ba thẻ bay vào từ ba phía, mỗi thẻ trễ 1 khung, đứng yên ở ~166 ms. Không nảy. Mỗi thẻ có ô phím chữ A/B/C. | Nhanh và cứng, hợp nhịp gõ. Chọn bằng bàn phím, không cần chuột. |
| T16 | **Rung có chọn lọc** | Cả cảnh dịch 12–14 px rồi về, vọt ~4 px, ~130 ms. Chỉ với phát bắn nặng, không với mỗi phím. | Rung hiếm nên còn ý nghĩa. |

**Typing Break làm chưa tốt, ta không chép:**
- **Đồ họa là khối cơ bản.** Trụ, cầu, hộp, nền phẳng một màu, không chất liệu. Ta giữ mức đồ họa của ta.
- **Số sát thương quá dày.** Hàng chục số chồng lên nhau và ở lại hơn 1 s (cảnh A và F). Che quái và che nhau. Ta phải giới hạn số và gộp số.
- **Chớp trắng nối nhau.** Khi nhiều kỹ năng cùng chạy, sân gần như trắng xóa (cảnh D). Khó thấy quái nào còn sống.
- **Chữ trên tấm có lúc mờ.** Chữ trắng ngà trên tấm hồng nhạt hoặc tím nhạt (cảnh B, D) có độ tương phản thấp. Chữ tím nhạt "đã gõ" gần như lẫn với chữ chưa gõ.
- **Nhãn chữ trên quái quá nhỏ** (`make`, `defeat` trên boss ở cảnh E).
- **Không thấy phản hồi gõ sai.** Ba game của ta đã có, và nên giữ.
- **Số máu nhảy ngay**, thanh máu không chạy dần, "+3" không bật. Ta làm tốt hơn được.
- **Thanh nhập nhảy khi căn giữa.** Thêm chữ là cả dòng giật sang trái.
- **Chỉ có hình, không có hướng dẫn.** Số đếm, dải đồng hồ trong tấm không có chú thích. Người mới khó hiểu.

---

## §5 Áp dụng vào ba game

Mỗi mục ghi: hôm nay mã đang làm gì, rồi thay đổi đề xuất với thông số. Thông số dưới đây tính ở 60 fps; ms là chuẩn, khung chỉ để tham khảo. Tên trong game dùng tiếng Anh.

### 5.1 Last Line (`games/typing-survival`)

**Hai ô từ cạnh tàu (bays), `src/view/hud.ts` và `survival.css`.**

Hôm nay:
- Tấm kính `.sv-slot`, tên súng `.sv-gun` 12 px, từ `.sv-word` 32 px, nghĩa `.sv-mean` 15 px.
- Thanh nạp sọc 5 px ở mép trên (`--load`). Đèn băng đạn `.sv-mags i`.
- Khi khóa (`is-active`): viền màu súng, vòng 2 px, quầng 26 px, `transition 0.15s`. Ô kia `is-dim` 0,72.
- Mỗi chữ đúng chỉ đổi màu `.sv-typed` và gạch chân 2 px. Không có pop trong ô.
- Phím lạc làm chữ đầu `.sv-head` nảy 1,15× → 1× trong 200 ms.
- Gõ xong: `sv-load` 0,35 s, `sv-perfect` 0,5 s.

Đề xuất:
1. **Chữ đóng dấu (T1) lên mọi ô khớp.** Phím đầu tiên: bản sao chữ hiện trên mọi ô có từ bắt đầu bằng chữ đó, trước khi khóa. Sau khi khóa: chỉ trên ô đã khóa.
   - Cỡ 2,6× → 2,0× → 1,5× → 1,0× trong 50 ms (bậc theo khung, không nội suy mượt).
   - Bắt đầu cao hơn chữ đích 28 px, lệch trái 10 px, nghiêng −8°. Trượt về đúng chữ.
   - Màu: mực súng pha 40% trắng nóng #FFF0D8. Phẳng, không bóng.
   - Ô hết khớp trả màu trong một khung.
2. **Viền khóa nổ rồi co (T3)**, thay `transition 0.15s`.
   - 0 ms: viền 6 px trắng nóng #FFF0D8, mép ngoài vượt ô 10%, quầng 40 px. Ô sáng +35% (`filter: brightness(1.35)`).
   - 0–100 ms: co về vòng 2 px màu súng và quầng 26 px như hiện nay. Hàm mũ, tau ~35 ms.
   - Giữ `is-dim` cho ô kia.
3. **Gõ xong: lóe viền lần hai**, ngay trước `sv-load`: viền vượt 6%, ô sáng +18% trong 80 ms.
4. **Đổi từ bằng bóp ngang (T7).** Từ cũ (cả nghĩa) `scaleX` 1 → 0 trong 100 ms, ease-in. Trống 60 ms. Từ mới hiện ngay ở 1,0×. Thanh nạp `--load` về 0 cùng lúc từ cũ bắt đầu bóp.
5. **Đèn băng đạn bật khi đổi.** Đèn vừa sáng hay vừa tắt: 1,4× → 1× trong 120 ms, khung đầu trắng nóng. Typing Break không làm điều này; ta thêm để số đếm rõ hơn. Giữ nhỏ.

**Dòng chữ đang gõ phía trên tàu (strip), `src/view/strip.ts`.**

Hôm nay:
- Chữ 42 px. Mỗi phím đúng pop 1,25× (tau 24 ms), hạ 6 px, đổi màu từ trắng nóng sang mực súng trong 120 ms.
- Tia `.sv-strip-spark` 170 px, tám tia, vòng 44 px nở 1 → 2,3×, mờ trong 80 ms.
- Mép tấm `is-key` 45 ms.
- Gõ sai: gạch đỏ 220 ms, tấm đỏ 120 ms, chữ ma đỏ 250 ms. DOM không rung.

Đề xuất:
1. **Ấn chữ hai tông (T2)**, thay vòng nở 80 ms.
   - Chữ vào ở 1,9× trong 1 khung, rồi 1,0×.
   - Đĩa trắng nóng Ø 1,9× chiều cao chữ (~60 px), 1 khung.
   - Vòng trắng dày 2 khung → vòng tối rgba(20,12,12,0.85) Ø 2,1× trong 2 khung → cung trắng mảnh Ø 2,3× trong 1 khung → cung tối xoay 40°/khung trong 3 khung. Xong ở 150 ms.
   - Dùng `steps()` trong keyframes để đổi theo bậc, không mượt.
   - Giữ tám tia 80 ms. Thêm một khung mảnh tối ở khung thứ 3.
   - Cung tối là con trỏ: nó nằm ở chỗ chữ tiếp theo.
2. **Bỏ nảy khi căn giữa.** Typing Break để dòng giật. Ta trượt dòng 60 ms ease-out khi bề rộng đổi.
3. **Giữ phản hồi gõ sai** như hiện nay. Typing Break không có gì tốt hơn để học.

**Súng bắn, `src/view/typing-feel.ts`, `gunfx.ts`, `shots.ts`.**

Hôm nay: mỗi phím có tia điện 3D từ chữ về lõi tàu, vòng sàn, lõi sáng dần, nòng gom lửa. Không có phát bắn mỗi phím. Lúc nạp: lõi lóe 45 ms, dòng chảy lõi → nòng 50 ms.

Đề xuất (bổ sung pha R và I theo `VFX_STANDARD.md`):
1. **Quầng nòng (T11).** Mỗi phát: quầng ấm #FFF1DC bán kính bằng 2,5 lần bề ngang tàu ở khung đầu, tắt trong 70 ms. Scatter dùng quầng to hơn 2× và tắt trong 250 ms, như Shotgun.
2. **Kim đạn.** Pulse và Rail: kim trắng lõi, viền màu súng, rộng 3 px, dài 18% chiều cao màn, bay hết làn trong ~100 ms.
3. **Chớp trắng quái (T9).** Giữ 40 ms, về màu gốc trong 150 ms.
4. **Số sát thương đập (T10).** 3× → 1× trong 150 ms, ease-out. Tối đa 6 số trên màn. Số cùng một quái trong 300 ms thì gộp và cộng dồn.
5. **Rung camera 3D có chọn lọc (T16)** cho Rail và Star Mortar: 1,2% chiều cao màn, tắt trong 130 ms. DOM vẫn không rung.
6. **Nhận đòn (T14).** Tách RGB tỏa tâm 18 px ở mép, giữ 300 ms, tắt trong 230 ms. Chữ đang gõ không bị tách (vẽ HUD sau lớp hậu kỳ).

### 5.2 Dragonhold (`games/dragon-hold`)

**Nhãn từ trên quái, `src/ui/tags.ts`.**

Hôm nay:
- Thân rgba(35,28,23,0.9), viền 1,5 px, chữ 20 px (16–26).
- Khóa: `scale(1.1)`, nhảy ngay, viền #7FF5E0.
- Mỗi phím: chữ `.j` chạy `dh-letter` 170 ms (−5 px, 1,45× ở 35%); cả nhãn `is-tick` −3 px trong 140 ms.
- Gõ sai: `is-shake` 180 ms, chữ cần gõ nền hồng.
- Xong: 6–8 tia chữ #7FF5E0 trong 520 ms, nhãn mờ và nâng 14 px trong 160 ms.

Đề xuất:
1. **Chữ đóng dấu (T1)** thay `dh-letter`. Bản sao 2,4× → 1,8× → 1,3× → 1,0× trong 50 ms, bắt đầu cao 16 px, nghiêng −8°, màu #7FF5E0 pha 40% trắng. Áp lên **mọi nhãn khớp** với phím đầu, như Typing Break. Người chơi thấy ngay nhãn nào sẽ bị khóa.
2. **Khóa: viền nổ rồi co (T3)** thay nhảy `scale(1.1)`. 0 ms: thân 1,16×, viền 3 px trắng nóng, nhãn sáng +35%. Về 1,1× và viền #7FF5E0 trong 90 ms, hàm mũ.
3. **Xong: lóe hai tông (T12 cỡ nhỏ)** trước khi nhãn bay. Khung 0 thân trắng nóng; khung 1–2 vòng tối quanh nhãn, Ø 1,4× bề ngang nhãn; rồi tia #7FF5E0 như hiện nay. Quái nhận đòn chớp trắng 40 ms, về màu trong 150 ms (T9).
4. **Giới hạn số.** Bảng nhãn đã đông. Số sát thương tối đa 6 trên màn và gộp số (tránh lỗi của Typing Break).

**Nút kỹ năng: Fire Breath ⌥1, Sky Fire ⌥2, Dragon Roar, Inferno, `src/ui/hud.ts`.**

Hôm nay:
- Nút gỗ 46×46 px, biểu tượng 26 px, ô phím ⌥1 / ⌥2.
- Hồi chiêu: nêm tối hình nón rgba(10,7,5,0.78) và số giây 15 px.
- Sẵn sàng `is-ready`: vòng hổ phách tĩnh, quầng 10 px.
- Bấm: `is-pressed` 0,18 s co 0,92; không được: `is-nope` rung.
- Không có lóe khi ra chiêu. Không có số đếm.
- Inferno: lớp phủ theo cơn giận; khi cháy, `dh-glow` 0,8 s.
- Dragon Roar: không hồi chiêu, chữ "Từ Khẩn", sau khi dùng mờ 0,55.

Đề xuất:
1. **Ra chiêu: viền nổ rồi co (T3).** Khung bấm: viền 4 px trắng nóng #FFF0D8, mép ngoài vượt nút 12%, nút sáng +40%. Giữ 2 khung. Về viền 2 px hổ phách trong 100 ms, hàm mũ. Sau đó mới vào trạng thái hồi chiêu. Giữ `is-pressed` co 0,92 ở khung đầu để có cảm giác nhấn.
2. **Hồi chiêu: tối và vạch nạp (T5).** Nút `brightness(0.55)`. Giữ nêm hình nón, thêm vạch 3 px ở mép dưới chạy theo tiến độ.
3. **Sẵn sàng: lóe lại (T3 nhỏ).** Hết hồi chiêu: 1,12× → 1× trong 120 ms, viền trắng nóng 1 khung rồi về vòng hổ phách. Hôm nay vòng hiện ra im lặng; nên có một nhịp để người chơi biết mà dùng.
4. **Inferno đang cháy: nhịp viền (T8)** thay `dh-glow` 0,8 s chung chung. Mỗi nhịp đốt: viền lóe trắng nóng 50 ms rồi về. Vạch dưới chạy giữa hai nhịp.
5. **Dragon Roar:** khi gõ từ khẩn xong, lóe viền T3 rồi bóp ngang (T7) ô chữ "Từ Khẩn" trong 100 ms trước khi mờ 0,55.
6. **Phím tắt đóng dấu (T1 nhỏ):** bấm ⌥1 thì ô phím "⌥1" đóng dấu 1,8× → 1× trong 50 ms.

**Thanh xây (build bar), `src/ui/shop-strip.ts`.**

Hôm nay: ô 58×78 px (44×42 khi vào trận), ô phím số, huy hiệu đếm `.dh-cell__badge`, trạng thái `is-poor`, `is-blocked`, `is-on`, `is-armed` (vòng vàng 2000 ms). Không có phản hồi gõ.

Đề xuất:
1. **Chọn ô (`is-armed`): viền nổ rồi co (T3)**: vượt 10%, sáng +30%, về vòng vàng #F2C14E trong 100 ms.
2. **Huy hiệu đếm bật** khi số đổi: 1,4× → 1× trong 120 ms, khung đầu trắng nóng.
3. **Ô chưa mua được:** tối 0,55 và vạch dưới cho tiền còn thiếu (T5), thay chỉ xám giá.
4. **Xây xong:** chớp trắng công trình 40 ms trên sân (T9) và mảnh vụn nằm lại khi công trình bị phá (T13).

### 5.3 Wordwoven (`games/typing-defense`)

**Thẻ gọi trên dân làng và tháp, `src/view/words/cards.ts`, `ui/td.css`.**

Hôm nay:
- Thẻ giấy #FFFAEA → #FFE8B0, viền mực 2 px, tre trên dưới.
- Chữ 18–24 px. Hạt ●●○ đếm số từ còn lại. Vạch thời gian 3 px, chuyển hổ phách khi còn dưới 1,5 s.
- Khóa: 1,1× (1,2× và lệch 18 px khi đã gõ 2 chữ), nhảy ngay không chuyển tiếp. Thẻ khác mờ 0,7.
- Mỗi phím: chữ `.k` chạy `td-key` 0,18 s (−4 px, 1,5×, #19C9A8).
- Gõ sai: thẻ rung 6 px trong 220 ms, chữ cần gõ hồng.
- Xong: thẻ hiện "từ · nghĩa" trên nền ngọc 1000 ms rồi gập 200 ms; dấu chấm điểm nâng 28 px, mờ trong 900 ms, không phóng to khi vào.

Đề xuất:
1. **Chữ đóng dấu (T1)** thay `td-key`. 2,4× → 1,0× trong 50 ms (bậc 2,4 / 1,8 / 1,3 / 1,0), bắt đầu cao 14 px, nghiêng −8°, màu #19C9A8. Áp lên **mọi thẻ khớp** với phím đầu.
2. **Khóa: viền nổ rồi co (T3)** thay nhảy ngay. 0 ms: thẻ 1,16×, viền ngọc 4 px có quầng trắng, sáng +30%. Về 1,1× trong 90 ms, hàm mũ. Lúc lên 1,2×: cũng 90 ms, không nhảy.
3. **Hạt đếm bật** khi một từ trong lời gọi xong: hạt vừa đổi 1,5× → 1× trong 120 ms, khung đầu trắng.
4. **Vạch thời gian đầy lại có nhịp (T6).** Lời gọi mới: vạch từ 0 lên đầy trong 120 ms. Typing Break đầy ngay; ta thêm nhịp ngắn để mắt thấy thẻ mới.
5. **Xong: lóe viền (T3) 80 ms** trước nền ngọc. **Dấu chấm điểm đóng xuống:** 2,0× → 1,0× trong 60 ms, kèm một vòng tối Ø 1,6× trong 2 khung. Hôm nay dấu chỉ nâng và mờ.
6. **Thẻ được thay: bóp ngang (T7)** 100 ms, trống 60 ms, thẻ mới hiện ngay, thay cho gập dọc.
7. **Tháp hoặc dân nhận lời gọi:** chớp trắng 40 ms, về màu trong 150 ms (T9).

---

## §6 Mười thay đổi đáng làm nhất (xếp theo tác động)

1. **Chữ đóng dấu lên mọi đích khớp (T1)** ở cả ba game: ô của Last Line, nhãn của Dragonhold, thẻ của Wordwoven. 2,4–2,6× → 1,0× trong 50 ms, nghiêng −8°, rơi từ trên. Người chơi thấy ngay đích nào khớp.
2. **Ấn chữ hai tông ở dòng gõ của Last Line (T2).** Đĩa trắng 1 khung → vòng trắng → vòng tối → cung xoay, xong ở 150 ms. Cung tối làm con trỏ.
3. **Viền khóa nổ rồi co (T3)** thay các phép nhảy `scale` và `transition 0.15s`: vượt 10–16%, sáng +30–40%, về trong 90–100 ms theo hàm mũ. Dùng cho ô Last Line, nhãn Dragonhold, thẻ Wordwoven, ô thanh xây.
4. **Chớp trắng mục tiêu khi trúng (T9)** ở cả ba game: giữ 40 ms, về màu trong 150 ms.
5. **Vòng đời nút kỹ năng Dragonhold:** lóe khi ra chiêu → tối và vạch nạp → lóe khi sẵn sàng (T3, T5). Nhịp viền cho Inferno đang cháy (T8).
6. **Số sát thương đập có giới hạn (T10):** 3× → 1× trong 150 ms, tối đa 6 số, gộp số cùng quái trong 300 ms.
7. **Bóp ngang để đổi từ (T7):** 100 ms bóp, 60 ms trống, từ mới hiện ngay. Cho ô Last Line và thẻ Wordwoven.
8. **Quầng nòng và kim đạn cho súng Last Line (T11):** quầng ấm 70 ms (Scatter 250 ms), kim đạn qua làn trong ~100 ms.
9. **Số đếm bật khi đổi:** đèn băng đạn Last Line, hạt đếm Wordwoven, huy hiệu thanh xây Dragonhold: 1,4–1,5× → 1× trong 120 ms.
10. **Nhận đòn bằng tách RGB (T14)** giữ 300 ms, tắt trong 230 ms, không che chữ đang gõ; rung camera chỉ cho đòn nặng (T16).

**Sáu tờ hữu ích nhất:**
- `tmp/typing-break-study/moments/letter-1/sheet-slots-a.jpg`: chữ đóng dấu lên tấm (T1).
- `tmp/typing-break-study/moments/letter-2/sheet-input-2x.jpg`: ấn chữ hai tông ở thanh nhập (T2).
- `tmp/typing-break-study/moments/skill-1/sheet-flame-plate-select.jpg`: viền chọn nổ rồi co (T3).
- `tmp/typing-break-study/moments/word-2/sheet-word-cycle-love-tea.jpg`: gõ xong → nhịp viền → bóp ngang đổi từ (T7, T8).
- `tmp/typing-break-study/moments/skill-2/sheet-right-slots-bar.jpg`: chọn LASER và bắn cả hàng (T3, T4, T11).
- `tmp/typing-break-study/moments/projectile-1/sheet-hit-2x.jpg`: chớp trắng và số sát thương đập (T9, T10).
