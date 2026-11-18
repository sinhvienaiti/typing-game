# Rồng Giữ Ải — 02. Quái, Tướng địch và Boss (thiết kế, 23/10/2026)

> Game **Rồng Giữ Ải** (`dragon-hold`). Đây là tài liệu thiết kế số 02.
> **Dựa trên:** `research/market.md`, `research/codebase-and-split.md`, `research/art-pipeline.md`; mã Space Typing `src/enemies/{kinds,skills,elite}.ts`, `src/boss/typing-mechanics.ts`; thiết kế TD mục 10, 13, 14, 18; kế hoạch Sinh Tồn mục 4.5, 5.
> **Số chuẩn: `00-canon.md`** (đơn vị W, tải gõ, bậc, boss W, đường cong, mức khó, cổng bot). Khi lệch, 00 thắng. Bot chỉnh số trong dữ liệu. Luật giữ nguyên.
> Món phe ta do 03 chốt; ma trận mã khắc chế → món ở 03 §0.3. Gán nhóm từ lên quái chỉ ở 01 §6.2.
> Bản sửa 23/10: phe Bầy Héo, W theo từ Vừa, ngân sách đợt theo tải gõ, trình bày từng tướng và boss, buff quân của boss.

## 0. Tóm tắt

1. Phe địch là **Bầy Héo**: sinh vật rừng bị **Hắc Vụ** (sương tím xám) làm Héo, quên tên mình, hóa dữ. Có 8 họ và **32 loài thường**: 8 bay, 9 hai chân, 7 bốn chân, 8 bò hoặc bầy.
2. Máu đo bằng **W**. 1 W = sát thương một từ **Vừa** ở sức chuẩn của chương (00 §4.1). W của mỗi loài **không đổi** suốt 520 ải. Độ khó đến từ cơ chế, không đến từ phồng máu.
3. **Chữ xuyên giáp** (00 D03). Giáp và kháng chỉ chặn quân ta. **Khiên chữ** thì chặn chữ. Hai lớp này buộc người chơi phối hợp gõ với bẫy và lính.
4. **Bầy dùng chung một từ cụm.** Màn hình đông quái mà ít chữ, không chồng chữ.
5. **14 tướng địch:** 8 Đội trưởng, 6 Thống lĩnh. Mỗi tướng có hào quang vẽ trên đất, kỹ năng chủ động, hiệu ứng khi chết, và **Ấn Phá**.
6. **20 boss**, 2–4 pha, dùng **12 cơ chế gõ** (5 cơ chế lấy từ Space Typing). Mọi đòn đều báo trước. Mỗi boss có buff cho quân theo pha (mục 4.5).
7. Đợt quái sinh theo **toán có hình**, nhịp đều, 2–3 đỉnh mỗi đợt. Ngân sách đợt đo bằng **tải gõ** (00 §4.4); **đe dọa** chỉ chọn thành phần. Có luật trộn cho 1–4 đường và thẻ báo đợt.
8. **520 ải = 26 chương × 20 ải.** Mỗi chương có cái mới: loài, tướng, combo, biến chủng, luật Hắc Vụ, song boss.
9. Cần khoảng **63 model Tripo mới**. Dùng lại Draconis, `lieutenant-nature`, hình tạm của quái bay Space, logic 14 hành vi và 5 cơ chế boss.

## 1. Luật chung

### 1.1 Phe địch và 8 họ

Hắc Vụ (sương tím xám, không phát sáng) trào lên từ các khe núi. Thú rừng và Yêu Rêu hít phải thì **Héo**: quên tên thật, một lớp **vỏ Héo** mọc lên người, chúng hóa dữ. Chúng kéo về **Bệ Rồng** ở giữa bản đồ, nơi hai Rồng canh giữ (05 §1.2: Rồng gọi đúng tên thì lời thành lửa).
Khi quái chết, vỏ Héo vỡ, một đốm sáng nhỏ bay về rừng, thân tan về thiên nhiên (lá, rêu, đá, khói). **Không có máu.** Game học dành cho mọi lứa tuổi.

| Họ | Mã | Gồm | Vùng hay gặp | Chất liệu (dùng cho âm trúng, chết) | Dấu hình |
|---|---|---|---|---|---|
| Yêu Rêu | `moss` | Yêu tinh lùn áo rêu, Chằn | Rừng thông, đồng cỏ | Vải ướt, gỗ | Mặt nạ vỏ cây |
| Thú Mục | `beast` | Sói, heo, nai, gấu, linh miêu, lửng | Mọi vùng | Lông, thịt dày | Vết nứt sáng trên lông |
| Bọ Gai | `bug` | Kiến, ong, bọ, nhện | Rừng mưa, hẻm đỏ | Vỏ kitin giòn | Gai đen |
| Nấm Ma | `spore` | Nấm phồng, nấm nổ | Đầm lầy, rừng phép | Thịt nấm mềm | Mũ đốm sáng |
| Đá Rễ | `stone` | Người đá (cổ thụ ở boss) | Hẻm đỏ, núi lửa | Đá, gỗ | Rêu, tinh thể |
| Cánh Đêm | `wing` | Dơi, bướm, quạ, cú, diều hâu | Mọi vùng | Lông vũ, màng | Cánh viền khói |
| Sương Đen | `mist` | Pháp sư, phù thủy, hồn | Rừng phép, đầm lầy | Sương, vải, thủy tinh | Áo choàng khói |
| Thủy Quái | `tide` | Cóc, cua, lươn | Sông, bờ biển | Nước, vỏ | Bóng ướt |

- **Dấu Héo (00 D02), cũng là dòng MATCH chung trong prompt 2D của mọi quái:** "mảng vỏ Héo xám tro như than nguội phủ một phần thân; khe nứt và mắt sáng vàng úa `#C8D24A`; phần còn lại giữ màu tự nhiên của loài". Vàng úa tách rõ khỏi tán tím lam của cảnh. Kiểm bằng bài nheo mắt (TD 23.1). **Chặn mọi việc tạo ảnh quái** tới khi chủ dự án duyệt hai ảnh thử của cùng một loài (E09) có dấu này.

### 1.2 Đơn vị và bậc

- **W:** 1 W = một từ Vừa ở sức chuẩn của chương; máu = W × 90 × g(c) (00 §4.1). Quái nhiều W mang nhiều từ nối nhau.
- **Giáp G0–G3** chặn 0 / 30 / 55 / 75 % sát thương vật lý của quân ta (lính chặn, bẫy gai, bẫy nổ). **Kháng K0–K3** chặn phép (nhà phép, bẫy sét, kỹ năng Rồng). **Chữ không bị giáp, kháng chặn.** Thang G ở 00 §4.2.
- **Khiên chữ:** mỗi lớp là một từ D1 viền bạc, phải gõ trước từ chính. Ngoài gõ, chỉ **Bùa Phá Chữ** và **Xung của Đài Khuếch Chữ** phá được (mã PHÁ-chữ, 03 §0.3).
- **Tốc:** S1 1,2–1,6 · S2 1,7–2,3 · S3 2,4–3,2 · S4 3,3–4,5 m/s. Đường dài 24–40 m, nên quái S2 đi hết đường mất 15–20 s.
- **Đòn quái** ghi theo thang máu Hỏa Long 1.000 ở C1 (01 §2.2), nhân g(c) theo chương.
- **Đe dọa (ĐĐ)** ≈ 3 × W × tốc / 2 + điểm kỹ năng (0 / 2 / 5 phá, khiên, hồi, ẩn / 8 triệu hồi, chở quân). Bầy tính 40 %. ĐĐ chỉ dùng để chọn **thành phần** đợt (mục 5.4).
- Mức khó: 00 §4.10. Lời Thề: 04 §10. Luật không đổi.

| Bậc | W | Giáp/Kháng | Tốc | Suất chặn | Đòn lên Rồng | ĐĐ mỗi con |
|---|---|---|---|---|---|---|
| Bầy | 0,3–0,5 | G0/K0 | S3–S4 | 0,25 | 2–3 | 0,6–0,7 |
| Nhỏ | 0,8–1,2 | G0–1/K0–1 | S2–S4 | 1 | 5–9 | 3–11 |
| Vừa | 2–3 | G0–2/K0–2 | S1–S3 | 1–2 | 8–22 | 9–19 |
| Nặng | 4–6 | G1–3/K1 | S1 | 2 | 15–28 | 13–17 |
| Khổng lồ | 8–10 | G3/K2 | S1 | 3 | 45 | 21 |
| Đội trưởng | 5–7 | Theo loài | S1–S3 | 2 | 15–25 | 30 |
| Thống lĩnh | 10–12 | G2–3/K2–3 | S1–S2 | 3 | 25–40 | 60 |
| Boss | 29–72 (00 §4.7) | Theo boss | S1–S2 | Không chặn | Theo đòn | — |

### 1.3 Khi tới gần: trạng thái và mục tiêu

Mỗi quái đi qua 4 trạng thái: **Đi → Bị chặn → Tới tầm → Đánh Rồng**. Quái tới Bệ Rồng không biến mất. Nó đứng lại đánh Rồng cho tới khi chết.

- **Mục tiêu theo vai:** chạy, chém, tank: lính chặn trên đường → Rồng · bắn xa: lính chặn trong tầm → nhà phép trong tầm → Rồng · phá nhà: nhà, lính chặn trong 6 m quanh đường → Rồng · phá bẫy: bẫy gần nhất trong 8 m quanh đường (Quạ Trộm: bẫy bất kỳ) · hồi, khiên, triệu hồi: đứng sau toán, chỉ đánh khi hết đồng minh · bay: không bị chặn, đánh Rồng hoặc nhà tùy vai.
- **Tầm:** Cận ≤ 1,5 m (chém, cắn, húc, kẹp) · Lao 1,5–5 m (vồ, tự nổ, quấn) · Xa 8–14 m (bắn, phun, ném) · Rất xa 16–22 m (bắn tỉa, pháo).
- **Báo trước:** đòn ≥ 15 máu Rồng, hoặc đòn phá đồ, báo ≥ 0,6 s. Quái Nặng, Khổng lồ báo ≥ 0,9 s. Boss báo ≥ 1,2 s (Dễ × 1,5; Khó × 0,85). Đòn nhỏ của Bầy và Nhỏ không cần báo.

### 1.4 Chữ trên đầu quái

Tài liệu này chỉ giữ **dải độ dài** D1–D5. Độ dài thật theo E của người chơi (01 §3.4). **Nhóm từ nào lên quái nào: chỉ 01 §6.2.**

| Bậc độ dài | Dải (ở E 25–44) | Dùng cho |
|---|---|---|
| D1 | 3–4 chữ cái | Cụm bầy, khiên chữ, kén, mảnh tách, từ ngắt nhỏ |
| D2 | 4–6 | Quái Nhỏ |
| D3 | 5–7 | Quái Vừa, Nặng, từng từ của tướng |
| D4 | 7–8 | Từ cuối của Khổng lồ và tướng, Ấn Phá, từ ngắt lớn (cột Từ Khẩn của 01 §3.4) |
| D5 | Chuỗi chủ đề 3–5 từ đơn | Đại chiêu boss, đòn kết (00 D19; không dùng câu) |

- Quái chậm và to có nhiều thời gian đọc, nên nhận từ cần học theo 01 §6.2. Từ mới **không** lên quái bay, quái nhanh, tinh anh, tướng, Ấn Phá, từ ngắt.
- **Quái nhiều W:** hiện từ hiện tại và dải chấm (số từ còn lại). Sát thương của bẫy, lính làm mất chấm. Từ đang gõ dở thì giữ (bảo hộ khóa, 01 §3.3).
- **Bầy:** mỗi cụm 4–10 con có **một từ cụm** D1 trên con đầu. Gõ xong thì Rồng phun lửa vào cụm: 1 W loại Chữ cho mỗi con trong 3 m.
- **Trần chữ và Vùng Chữ:** 01 §3.2 và 00 §5. Trần là hằng số của luật, không theo bậc máy (00 D10). Quái chưa có chữ hiện một chấm.
- **Từ ngắt:** viền cam (05 §4.3). Thời gian gõ ≥ 1,6 lần thời gian dự kiến theo tốc gõ. Theo luật chữ đầu của 01 §3.3: **không bao giờ trùng chữ đầu với chữ đang sống**.
- **Chữ đặc biệt:** *ẩn* (hiện `• • •`, cần LỘ; luật chữ bị che ở 01 §3.3), *thì thầm* (chỉ IPA, tự phát âm theo kênh phát âm 01 §6.4, gợi chữ đầu), *khung giờ* (chữ "ngủ" khi tắt, 01 §3.3), *viền đồng* (tinh anh, có thưởng).

### 1.5 Trúng đòn, chết, âm, VFX, ra mắt

- **Trúng đòn, 3 lớp:** (1) thuộc tính instanced như Sinh Tồn 5.5: lóe 1–4 khung, giật lùi giả, co giãn 0,91 / 1,07; (2) clip Hit trộn 0,25 s cho quái có xương; (3) mảnh theo chất liệu họ. Quái Nặng trở lên không giật lùi, chỉ khựng và bắn mảnh.
- **Chết:** clip Death hoặc rơi, rồi vỏ Héo vỡ, một đốm sáng nhỏ bay về rừng, thân tan theo chất liệu trong 1–1,5 s. Tiếng "xác nhận hạ" khác tiếng trúng.
- **Âm:** mỗi loài có 4 khe `enemy.<id>.attack|hit|death|skill`. Khe lấy từ **bộ âm của lớp** (05 §7.1) rồi đổi cao độ theo cỡ, chất liệu theo họ, giọng theo loài. Chỉ tướng và boss có bộ âm riêng (mục 3.4, 4.5). Lệch cao độ ngẫu nhiên ±6 %. Tối đa 3 tiếng giống nhau mỗi 100 ms (như `defense/view/sounds.ts`). Ưu tiên: boss > tướng > kỹ năng > đòn > trúng. Nguồn và giấy phép: DESIGN.md §7. File âm đi qua `pnpm media:push`, không vào Git.

- **Màu VFX phe địch:** đỏ = đòn sắp trúng phe ta (vạch, vòng, đếm lùi) · cam = sắp nổ, Từ Ngắt · **vàng úa** = hào quang, buff của địch (màu phe Héo; mỗi loại buff có hoa văn và icon riêng: kiếm = đòn, khiên = giáp, chân gió = tốc, lá = hồi, xích = kháng khống chế, mắt = ẩn chữ, thoi = kháng phép, trống = tốc đánh) · lục úa = địch hồi máu · bạc = khiên chữ.
- Xanh ngọc (sức gõ) và vàng kim (tiền) để dành cho phe ta (TD 23.3).
- **Ra mắt (CGI):** loài mới có thẻ góc 3 s, không dừng trận: model xoay, tên, một dòng "làm gì", một dòng "khắc chế" (đã ghi vào Sổ Quái, 06 §5). Tướng có khung cận cảnh 2 s. Boss có cảnh 3–4 s bằng clip Intro và một câu thoại có phụ đề. Trận vẫn chạy. Thẻ ra mắt không chặn việc gán chữ (01 §3.3).

### 1.6 Mã khắc chế

Món thật cho từng mã, cùng ải mở: **03 §0.3** (ma trận khắc chế, nguồn duy nhất). Bảng dưới chỉ là ví dụ món đã có trong 03.

| Mã | Nghĩa | Món, kỹ năng ví dụ (03, 01) |
|---|---|---|
| CHẶN | Lính chặn giữ chân | Vệ Binh Rêu, Gấu Khiên Đá |
| CHẬM | Vùng làm chậm | Bùn Lầy, Cột Chậm, Gai Chông |
| GIAM | Giam đứng yên | Lưới Dây Leo, Lồng Đá, Pháp Sư Dây Leo |
| NỔ | Nổ cụm | Bom Hạt Thông, Mìn Ấn, Hạt Giống Nổ |
| ĐẨY | Đẩy lùi | Gió Cuốn (Bạch Long), Cọc Bật |
| LƯỚI | Kéo quái bay xuống thấp, cho lính đánh được | Lưới Phóng, Gió Cuốn |
| LỘ | Lộ diện, hiện chữ ẩn | Đèn Đom Đóm, Tháp Canh |
| PHÁ | Phá giáp (Gai Sắt, Lưới Gai, Long Ấn Phá Vỏ) hoặc phá khiên chữ (Bùa Phá Chữ, Xung Đài Khuếch Chữ) | Ghi rõ PHÁ-giáp hay PHÁ-chữ ở 03 §0.3 |
| CÂM | Khóa kỹ năng, tắt hào quang | Chuông Bạc, Sét Câm, Lời Thề Bạch Vũ, Ấn Phá |
| RUNG | Đánh quái dưới đất | Trống Đất |
| PHUN | Đòn lan của Rồng | Phun Lửa, Thiên Hỏa, Spit_Big |
| NGẮT | Gõ từ ngắt | Người chơi |
| ƯT | Gõ hạ nó trước | Người chơi |

## 2. 32 loài quái thường

### 2.1 Chỉ số, chữ, khắc chế

| # | id | Tên | Họ | Dáng | Vai | Bậc · W | Giáp/Kháng | Tốc | Chặn | ĐĐ | Chữ | Mở | Khắc chế |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E01 | `thorn-wasp` | Ong Gai | bug | Bay | Bắn xa | Nhỏ 1 | G0/K0 | S3 2,6 | — | 6 | D2 | C1 | LƯỚI, PHUN |
| E02 | `bat-swarm` | Dơi Muội | wing | Bay | Lao bầy | Bầy 0,35 | G0/K0 | S3 3,0 | — | 0,6 | Cụm D1 | C2 | PHUN, LƯỚI |
| E03 | `ember-moth` | Bướm Tro | wing | Bay | Tự nổ vào nhà | Nhỏ 0,8 | G0/K0 | S3 2,8 | — | 8 | D1–D2 | C6 | LƯỚI, ƯT |
| E04 | `crow-thief` | Quạ Trộm | wing | Bay | Trộm lượt nạp | Nhỏ 1,2 | G0/K0 | S3 3,0 | — | 10 | D2, viền đồng khi mang đồ | C7 | LƯỚI, ƯT |
| E05 | `mist-wraith` | Hồn Sương | mist | Bay thấp | Xuyên chặn | Nhỏ 1 | Miễn vật lý/K0 | S2 2,0 | Xuyên | 10 | Thì thầm D2 | C7 | Rồng, nhà phép, LỘ |
| E06 | `hawk-carrier` | Diều Hâu Khói | wing | Bay | Chở quân | Vừa 3 | G0/K1 | S2 2,4 | — | 19 | D3 | C8 | LƯỚI, ƯT, PHUN |
| E07 | `veil-moth` | Ngài Màn Sương | wing | Bay | Ẩn chữ | Vừa 2 | G0/K2 | S2 2,0 | — | 11 | D3 | C9 | LỘ, ƯT, LƯỚI |
| E08 | `owl-seer` | Cú Mắt Tím | wing | Bay | Bắn tỉa | Vừa 2 | G0/K1 | S2 2,0 | — | 11 | D3, ngắt D2 | C10 | NGẮT, LƯỚI |
| E09 | `moss-grunt` | Yêu Rêu Lính | moss | 2 chân | Chém | Nhỏ 1 | G1/K0 | S2 2,0 | 1 | 3 | D2 | C1 | CHẶN, NỔ |
| E10 | `moss-runner` | Yêu Rêu Chạy | moss | 2 chân | Lao nhanh | Nhỏ 0,8 | G0/K0 | S4 3,8 | 1 | 7 | D1–D2 | C2 | CHẬM, GIAM |
| E11 | `moss-archer` | Yêu Rêu Cung | moss | 2 chân | Bắn xa | Nhỏ 1,2 | G0/K0 | S2 2,0 | 1 | 7 | D2 | C2 | NỔ, Rồng |
| E12 | `forest-ogre` | Chằn Rừng | moss | 2 chân | Tank chém | Nặng 5 | G2/K1 | S1 1,5 | 2 | 13 | D3 × 4 + D4 | C3 | PHÁ, GIAM |
| E13 | `moss-shieldbearer` | Yêu Rêu Khiên | moss | 2 chân | Khiên | Vừa 2 | G2/K0 | S2 1,8 | 1 | 10 | Khiên D1 + D3 | C3 | PHÁ, NỔ, CÂM |
| E14 | `moss-sapper` | Yêu Rêu Đặt Mìn | moss | 2 chân | Phá nhà | Nhỏ 1,2 | G0/K0 | S3 2,6 | 1 | 11 | D2, ngắt D1 | C4 | ƯT, ĐẨY |
| E15 | `mist-shaman` | Pháp Sư Sương | mist | 2 chân | Hồi máu | Vừa 2,5 | G0/K2 | S2 1,8 | 1 | 12 | D3, ngắt D1 | C5 | NGẮT, CÂM, ƯT |
| E16 | `hex-witch` | Phù Thủy Nguyền | mist | 2 chân | Nguyền | Vừa 2,5 | G0/K2 | S2 1,8 | 1 | 12 | D3 | C10 | CÂM, ƯT |
| E17 | `stone-golem` | Người Đá Rêu | stone | 2 chân | Tank, ném đá | Khổng lồ 9 | G3/K2 | S1 1,2 | 3 | 21 | D3 × 8 + D4 | C10 | GIAM, PHÁ, CÂM |
| E18 | `blight-wolf` | Sói Mục | beast | 4 chân | Lao bầy | Nhỏ 1,2 | G0/K0 | S4 3,6 | 1 | 8 | D2 | C3 | CHẬM, GIAM, NỔ |
| E19 | `tusk-boar` | Heo Nanh Đá | beast | 4 chân | Húc | Vừa 3 | G1/K0 | S2 2,2 | 2 | 12 | D3 | C4 | ĐẨY, GIAM |
| E20 | `toad-spitter` | Cóc Độc | tide | 4 chân | Pháo vùng | Vừa 3 | G1/K0 | S1 1,5 | 1 | 9 | D3 | C5 | NỔ, Rồng |
| E21 | `moss-stag` | Nai Rêu | beast | 4 chân | Hồi vùng | Vừa 3 | G1/K1 | S2 2,0 | 2 | 14 | D3 | C6 | ƯT, CÂM, PHUN |
| E22 | `tunnel-badger` | Lửng Đào Hang | beast | 4 chân | Đào, phá bẫy | Vừa 2 | G1/K0 | S2 2,2 | Không khi đào | 12 | D2, ẩn khi đào | C7 | RUNG, GIAM |
| E23 | `shadow-lynx` | Linh Miêu Bóng | beast | 4 chân | Tàng hình | Vừa 2 | G0/K1 | S3 3,0 | 1 | 14 | D3, ẩn | C9 | LỘ, GIAM |
| E24 | `bramble-bear` | Gấu Gai | beast | 4 chân | Tank | Nặng 6 | G2/K1 | S1 1,6 | 2 | 16 | D3 × 5 + D4 | C10 | GIAM, PHÁ, CÂM |
| E25 | `thorn-ant` | Kiến Gai | bug | Bò | Bầy | Bầy 0,4 | G0/K0 | S3 2,8 | 0,25 | 0,7 | Cụm D1 | C1 | PHUN, NỔ, CHẬM |
| E26 | `puffball` | Nấm Phồng | spore | Bò | Tách đôi | Vừa 2 (+3 × 0,5) | G0/K1 | S1 1,4 | 1 | 9 | D3; con D1 | C4 | NỔ, PHUN |
| E27 | `acid-beetle` | Bọ Axit | bug | Bò | Ăn giáp lính | Nhỏ 1 | G1/K0 | S2 2,3 | 1 | 5 | D2 | C5 | ĐẨY, PHUN |
| E28 | `web-spider` | Nhện Tơ | bug | Bò | Trói lính, bọc bẫy | Nhỏ 1,2 | G0/K1 | S3 2,6 | 1 | 11 | D2 | C6 | ƯT, PHUN |
| E29 | `shell-crab` | Cua Mai Khiên | tide | Bò | Tank khung giờ | Nặng 4 | G3/K1 | S1 1,4 | 2 | 13 | D3, chỉ khi mai mở | C8 | GIAM, PHÁ |
| E30 | `river-eel` | Lươn Sông | tide | Bò (rắn) | Phục từ sông | Vừa 2 | G0/K1 | S3 3,0 | 1 | 14 | D3 | C8 | GIAM, ƯT |
| E31 | `brood-spider` | Nhện Mẹ | bug | Bò | Triệu hồi | Nặng 4 | G1/K1 | S1 1,5 | 2 | 17 | D3; kén D1 | C9 | ƯT, NỔ, PHUN |
| E32 | `spore-bloater` | Nấm Nổ Mê | spore | Bò | Tự nổ khống chế | Vừa 2 | G0/K1 | S1 1,4 | 1 | 9 | D2 | C11 | ƯT, ĐẨY |

- Đủ vai đề bài yêu cầu: lao (E02, E10, E18, E25), bắn xa (E01, E11, E20, E08), chém (E09, E19, E12), tank (E12, E17, E24, E29), hồi (E15, E21), triệu hồi (E06, E31), phá (E04, E07, E22, E28, E16), tách (E26), đào (E22, E30), khiên (E13, E29), phá nhà (E14, E03, E27).

### 2.2 Hành vi và trình bày

| # | Di chuyển | Đòn khi gần (tầm · sát thương · nhịp · báo) | Kỹ năng | Trúng đòn / chết | Âm: đánh · trúng · chết · kỹ năng | VFX | Gốc Space |
|---|---|---|---|---|---|---|---|
| E01 | Lượn sóng cao 3–4 m, dừng lơ lửng cách mục tiêu 10 m | Ngòi gai 10 m · 5 · 1,6 s · chổng bụng 0,4 s | Ngòi Độc (hồi 10 s): lính trúng bị Độc 4 s, −50 % hồi máu | Chao cánh, lùi 0,5 m / Rơi xoáy, nảy trên đất | Vo ve gắt + "phụt" · tách cánh · rè tắt dần · rít cao | Vệt ngòi lục chanh, phấn ong | `scout`, `pulse-shot` |
| E02 | Đàn 6–8 con xoáy theo đường bay, tản khi trúng | Lao cắn · 2 · 0,7 s | — | Lật nghiêng / Rơi xoay như lá, tan muội | Chít chít · bụp lông · chít tắt · — | Khói muội, đốm mắt vàng úa | `mine` |
| E03 | Bay chập chờn cao 2,5 m, chọn nhà phép hoặc bẫy gần nhất | Lao nổ tro 2 m · 40 vào nhà/bẫy, bẫy "ngạt" 4 s · cánh rực 0,8 s | — (bị giết thì không nổ) | Phấn rơi, chao / Tan tro lấp lánh | Phạch phạch · sột phấn · xì tan · phụt cháy | Phấn tro cam hồng, vệt lửa nhỏ | `mine` |
| E04 | Bay vòng cao 6 m rồi sà xuống | Sà cướp 1 lượt nạp của bẫy hoặc đồ hỗ trợ · bóng sà 0,8 s; rồi bay về cổng | Giết khi đang mang: trả đồ + 5 vàng | Lông bay, chệch hướng / Rơi xoáy, đồ rơi lấp lánh | Quạ kêu khàn · phạch lông · quạ tắt · "keng" lấy đồ | Lông đen, đốm sáng của đồ mang | `leech` |
| E05 | Lướt xuyên lính và rào, nhấp nháy | Chạm lạnh 1 m · 8 · 1,2 s; Rồng bị Lạnh: −15 % sát thương lan 3 s | Mờ (hồi 8 s): 1,5 s không nhắm được | Thân gợn như khói rách / Tan thành sương xoáy | Thì thầm · xoẹt khói · thở dài tan · tiếng vọng | Sương tím xám nhạt (Hắc Vụ), vệt mờ | `cloaker` |
| E06 | Bay cao 6 m thẳng về Bệ Rồng, quặp 2 Yêu Rêu Lính hoặc 1 Đặt Mìn | Thả quân cách Bệ Rồng 10 m · vòng thả 1 s; sau đó mổ 10 / 1,6 s | Giết trước khi thả: quân rơi choáng 2 s | Lảo đảo, quân treo lắc / Rơi nghiêng, khói đuôi | Rít dài · phạch · rít tắt · gió vỗ cánh mạnh | Khói đen đuôi, vòng thả | `carrier` |
| E07 | Lơ lửng trên toán, bám con nhiều máu nhất | Phấn ngứa · 8 · 2 s | Màn Phấn (thụ động): chữ quái trong 4 m bị ẩn | Phấn tung, rung / Cánh rơi chậm như lá | Vỗ êm · sột phấn · rơi xào · leng keng mờ | Phấn lam tím, vòng 4 m mờ | `jammer`, `signal-jam` |
| E08 | Bay tới chỗ đậu ở rìa 16–20 m rồi đậu | Tia Mắt 20 m · 50 vào nhà hoặc lính · nạp 2 s, vạch đỏ, từ ngắt | Tia (hồi 8 s) | Xù lông, xoay đầu / Rơi khỏi cành, lông bay | Hú trầm · phập lông · hú tắt · ngân điện | Vạch ngắm đỏ, tia vàng úa | `sniper`, `sniper-shot` |
| E09 | Lom khom, lắc lư; bị chặn thì đánh lính | Chém dao đá 1,2 m · 8 · 1,4 s · giơ dao 0,5 s | — | Giật đầu, mũ rêu rơi lá / Ngã ngửa, thân tan thành rêu khô | Hét "hây" khàn · bụp vải ướt · ré ngắn · — | Lá rêu bay, vệt chém trắng mảnh | `scout` |
| E10 | Chạy nước rút, cúi thấp | Đâm dao găm · 6 · 0,9 s | Lướt (thụ động): lần đầu bị chặn thì trượt qua | Loạng choạng 0,3 s / Lăn hai vòng rồi nằm | Thở dốc · bụp nhẹ · "éc" · gió lướt | Bụi sau chân, vệt lướt mờ | `mine` |
| E11 | Đi rồi dừng cách mục tiêu 12 m; bị áp sát thì lùi 2 m | Tên 12 m · 7 · 1,8 s · kéo dây 0,6 s | Tên Lửa (hồi 12 s): bẫy trúng tên phải nạp thêm 3 s | Cung lệch, mất phát đang kéo / Quỳ xuống, cung gãy | Bật dây "tưng" · bụp vải · rên · lửa phụt | Vệt tên, mũi lửa cam | `scout`, `burst-volley` |
| E12 | Bước nặng, rung đất nhẹ | Nện chày vòng 2 m · 25 · 2,2 s · vòng đỏ 0,9 s | Gầm (hồi 16 s, báo 0,8 s): quân trong 5 m +20 % đòn 6 s | Khựng vai, vụn vỏ cây bắn / Quỳ gối rồi đổ sập, rung nhẹ camera | Gầm trầm · bịch thịt dày · rống dài + đổ ầm · gầm vang | Sóng bụi vòng, mảnh gỗ | `tank` |
| E13 | Đi đầu toán, khiên giơ trước | Đập khiên · 10 · 1,6 s, đẩy lính lùi 0,5 m | Khiên Chữ (hồi 14 s, báo 0,6 s): 3 quân gần nhất +1 lớp khiên chữ | Khiên lóe, trượt lùi; khiên vỡ thì văng / Khiên rơi úp, người ngã sau | Hô ngắn · cộp gỗ dày · khiên lăn · cộp khiên ba nhịp | Vòm khiên viền bạc, mảnh gỗ | `shield`, `barrier-shell` |
| E14 | Vác thùng thuốc, chạy tới nhà hoặc lính gần đường | Đặt thùng: ngòi 3 s (từ ngắt D1 trên thùng), nổ 2,5 m · 60 vào nhà/lính | Chết thì thùng nổ nhỏ 1,5 m, **hại quái quanh nó** | Thùng lắc, ngòi xèo mạnh / Thùng rơi, nổ nhỏ | Cười khặc · bụp · nổ đùng · xèo ngòi | Ngòi lửa, vòng đếm lùi, khói nổ | `mine` |
| E15 | Đi sau toán, giữ cách 4 m | Cầu sương 9 m · 8 · 2 s | Suối Sương (hồi 10 s): khi ≥ 2 quái trong 6 m dưới 70 % máu, niệm 2,5 s (từ ngắt), hồi 30 % | Gậy chao, sương rò / Tan vào sương, gậy rơi | Lẩm bẩm · bụp vải · thở dài tan · chuông gió ngược | Vòng lục nhạt khi niệm, hạt lá sáng | `healer`, `repair-wave` |
| E16 | Đi sau, đứng cách 12 m để niệm | Tia nguyền 12 m · 10 · 2 s | Nguyền Bẫy (hồi 14 s, báo 1 s): tắt 1 bẫy hoặc nhà phép 6 s. Nguyền Chuẩn (từ C12, hồi 20 s): 6 s, mỗi phím sai hồi 3 % máu quái trong 8 m | Mũ lệch, rít / Cười rồi tan thành sương tím xám | Cười khanh khách · bụp vải · gào tan · niệm + chuông | Ký hiệu nguyền xoay trên mục tiêu | `oppressor`, `curse-mark` |
| E17 | Bước rất chậm, miễn đẩy, đi qua rào thì phá rào | Đấm đất vòng 2,5 m · 45 · 2,5 s · vòng đỏ 1 s | Ném Đá (hồi 12 s): vòng 2 m cách 14 m vào nhà, báo 1,5 s. Rêu Phủ (dưới 50 %): +1 lớp khiên chữ một lần | Đá vụn bắn, không lùi / Vỡ thành 5 khối đá lăn, rêu bay | Rền đá · cộp đá · đổ ầm dài · đá nghiến | Bụi đá, sóng đất, mảnh đá | `tank`, `destroyer` |
| E18 | Bầy 3–5 con, chạy vòng cung | Cắn · 9 · 1 s; vồ qua 1 lính chặn, báo 0,5 s | Tru (thụ động): ≥ 3 sói trong 6 m thì +15 % tốc | Rên, chùn chân sau / Lăn nghiêng, tan khói từ vết nứt | Gầm gừ + "phập" · ẳng · ẳng dài · tru ngắn | Vết nứt vàng úa, khói muội | `scout` + `swift` |
| E19 | Đi lắc đầu; cách mục tiêu 8 m thì cào đất rồi húc | Húc thẳng 8 m · 20, hất lính 3 m · vạch đỏ 1 s; sau húc choáng 1,5 s, nhận +25 % | Húc (hồi 9 s) | Hếch mõm, lùi nửa bước / Trượt dài theo đà | Ụt ịt khàn · bịch · rống tắt · cào đất + rống | Bụi cào, vệt húc, sao choáng | `destroyer` |
| E20 | Nhảy cóc từng quãng 2 m, dừng cách 14 m | Nhổ độc vòng cầu 14 m · vũng 2 m tồn 4 s, 6/s lên lính · vòng cam 1,2 s | Nuốt (hồi 15 s): nuốt 1 con bầy gần, hồi 20 % | Phồng má, giật / Xẹp, lật ngửa | Ộp trầm · bẹp ướt · ộp tắt · phun "phụt" | Vũng độc lục, bong bóng | `destroyer` |
| E21 | Đi thong thả; trúng đòn lần đầu thì nhảy tránh 2 m | Húc sừng · 12 · 1,8 s | Mầm Rêu (hồi 12 s): 3 mầm quanh nó, quái đứng trên hồi 3 %/s trong 6 s. PHUN đốt được mầm | Giật sừng, lá rơi / Quỵ xuống, rêu phủ thân, mọc nấm nhỏ | Khịt mũi · bộp lông · rên dài · lá xào | Mầm sáng lục nhạt, lá rơi | `healer` |
| E22 | Chui đất ở cổng, đi ngầm (vệt đất gồ), trồi ở bẫy gần nhất | Cào · 9 · 1,2 s | Đào Bẫy: trồi tại bẫy, lôi bẫy lên trong 3 s (từ ngắt D1). Thành công: bẫy hỏng, đặt lại được hoàn 50 % | Rúc đầu / Nằm bẹp, đất phủ | Sột soạt đất · bịch · kít · đất vỡ | Vệt đất gồ, đất văng | `cloaker` + `mine` |
| E23 | Tàng hình (bóng gợn), đi vòng ngoài đường; lộ khi cách mục tiêu 6 m hoặc đứng dưới đèn | Vồ nhà phép hoặc lính tuyến sau · 22 · cúi rạp 0,6 s; rồi cào 10 / 1 s | Ẩn Lại (hồi 12 s) sau mỗi lần vồ | Hiện rõ 1 s, xù lông / Hiện nguyên hình, tan bóng | Gừ khẽ · xì · gào ngắn · vút | Bóng gợn khúc xạ, mắt vàng úa | `cloaker` |
| E24 | Đi bốn chân, đứng hai chân khi đánh | Tát · 28 · 2 s | Gầm Rung (hồi 14 s, báo 1 s): lính trong 3 m choáng 1,5 s. Cuồng dưới 40 % máu: +30 % tốc đánh | Gai rung, lùi nhẹ / Ngã nghiêng nặng, gai rụng | Gầm trầm · bịch lông dày · rống dài · gầm rung | Gai bắn, bụi | `tank` |
| E25 | Dòng zigzag trong cụm 6–10, bám mép đường | Cắn · 3 · 0,8 s | — | Bật ngửa, chân quẫy / Lật bụng, mờ trong 1 s | Tách tách · cộp vỏ nhỏ · rắc giòn · — | Vụn vỏ đen, bụi đất | `mine` |
| E26 | Lăn và nảy chậm | Húc nhẹ · 6 · 1,5 s | Tách (khi chết): 3 Nấm Con 0,5 W, S3 | Nhún lún, phụt bụi / Nổ "bụp" thành 3 con | Bập bùng · bụp mềm · bụp + lách tách · — | Mây bào tử nâu nhạt | `splitter` |
| E27 | Bò thẳng tới lính chặn | Phun axit · 6, lính −1 bậc giáp 8 s | Chết để vũng axit 1,5 m trong 3 s, ăn giáp lính | Vỏ rạn / Vỡ, axit trào | Lách cách · cộp vỏ · xèo vỡ · xèo | Axit lục chanh bốc khói | `mine`, `drain-pulse` |
| E28 | Bò nhanh, leo đá ven đường, dừng cách 8 m | Cắn · 7 · 1,2 s | Bắn Tơ (hồi 8 s, sợi sáng 0,6 s): trói 1 lính 3 s, hoặc bọc 1 bẫy 5 s | Co chân / Co quắp, tơ đứt bay | Lạo xạo · bộp · rít khẽ · "xẹt" tơ | Sợi tơ ánh bạc, kén | `oppressor`, `bind-field` |
| E29 | Bò ngang theo đường; mai đóng 3 s, mở 3 s | Kẹp · 20 · 2 s · giơ càng 0,7 s | Đóng Mai (hồi 6 s): nhận 2 đòn trong 1 s thì đóng ngay. Đóng mai thì chữ "ngủ": mờ, không nhận, gõ vào không tính lỗi, giữ tiến độ (01 §3.3) | Mai kêu "keng", nảy / Lật ngửa, càng co | Lách cách càng · keng mai · rắc vỏ · cạch đóng | Tia lửa nhỏ trên mai, bọt nước | `shield` |
| E30 | Sinh từ sông, bơi ngầm (gợn nước), lên bờ ở đoạn đường gần sông nhất, trườn chữ S | Quấn lính 1,5 s rồi cắn 12; với Rồng: quất đuôi 12 / 1,5 s | Lặn (hồi 10 s): nếu sông trong 6 m thì rút xuống, hồi 20 % | Quằn / Duỗi thẳng, chìm hoặc tan | Rít nhớt · bẹp · rít tắt · tõm | Gợn nước, nước bắn | `cloaker` |
| E31 | Bò chậm, lưng mang túi trứng | Cắn · 15 · 1,8 s | Đẻ Kén (hồi 9 s): kén D1 0,5 W, nở 4 nhện con (bầy) sau 5 s | Túi trứng rung / Túi vỡ, nhớt văng | Lạo xạo nặng · bộp · rít + nhớt · ục ục | Kén tơ, nhớt | `carrier`, `summon-scout` |
| E32 | Lăn chậm về phía cụm lính | Chạm lính thì nổ mây 3 m: lính "ngủ" 3 s, quái trong mây hồi 10 % · phồng to 1 s | Bị giết từ xa: chỉ nổ nhỏ 1,5 m, không hồi | Phồng to dần / Xẹp xì hơi | Ọc ọc · bụp · xì dài · nổ bụp lớn | Mây bào tử vàng úa nhạt, chữ "Zzz" trên lính | `mine` + `volatile` |

- Logic 14 hành vi của Space (`kinds.ts`, `skills.ts`) **chép** vào kit chung làm "hành vi gốc", rồi thêm tham số. Không import Space Typing.

### 2.3 Biến chủng (chương 12–19, không cần model mới)

Biến chủng dùng lại model và rig, đổi vật liệu bằng mã, thêm **một luật**, một nét hình và một lớp tiếng riêng. Mỗi chương từ 12 tới 19 có một biến chủng.

| Biến chủng | Từ loài | Luật mới | Hình riêng | Tiếng riêng | Chương |
|---|---|---|---|---|---|
| Nấm Đầm | E26 | Nấm Con gây Độc lên lính | Mũ lục rêu ướt, bọt nổi | Bụp ướt, lục bục | C12 |
| Ong Sấm | E01 | Ngòi nảy sang lính thứ hai | Cánh có tia điện lam trắng, vệt ngòi chẻ đôi | Rè điện trên tiếng vo ve | C13 |
| Linh Miêu Đêm | E23 | Ẩn lại một lần sau từ đầu tiên trúng nó | Lông chàm sẫm, đuôi để vệt mờ | Gừ thì thầm, "vút" kép | C14 |
| Cua San Hô | E29 | Mai mở 2 s, đóng 4 s; khi đóng phản 30 % sát thương bẫy | Mai san hô hồng nhạt, gai nhỏ | "Keng" cao, lách cách giòn | C15 |
| Người Đá Hồng Ngọc | E17 | Đá ném để lại vệt lửa 4 s | Vân đá đỏ sẫm giảm bão hòa (không trùng đỏ báo trước), tro bay | Rền đá kèm lửa phụt | C16 |
| Sói Băng | E18 | Cắn làm lính chậm 30 % trong 3 s; trên tuyết +10 % tốc | Lông trắng xanh, hơi lạnh ở mõm | Tru vọng, cắn có tiếng băng nứt | C17 |
| Nai Hoa | E21 | Mầm thành hoa, nổ phấn ngủ 2 s lên lính | Gạc nở hoa trắng, cánh hoa rơi | Leng keng nhỏ khi bước | C18 |
| Kiến Lửa | E25 | Chết để đốm lửa 1 m trong 2 s | Vỏ nâu than, đốm cam âm ỉ | Lách tách lửa khi chết | C19 |

### 2.4 Tinh anh (thuộc tính ghép)

- Tinh anh: W × 1,6, chữ viền đồng kèm biểu tượng thuộc tính, luôn rơi túi thưởng. Có hai kiểu nhóm: 3–5 con giống nhau cùng thuộc tính, hoặc Đội trưởng kèm lính.

| Nhóm | Thuộc tính và tác dụng |
|---|---|
| Tấn công | **Cuồng Nộ:** dưới 40 % máu +30 % tốc, +30 % đòn · **Nổ Khi Chết:** nổ 2,5 m sau 1,2 s (vòng cam), hại lính và nhà · **Lửa Mục:** vệt cháy 3 s trên đường, lính đứng trên bị cháy · **Đòn Kép:** đòn xa bắn hai phát |
| Phòng thủ | **Giáp Đá:** +1 bậc giáp · **Khiên Sương:** +1 lớp khiên chữ, mọc lại sau 12 s · **Tái Sinh:** 3 s không trúng đòn thì hồi 2 %/s · **Gai Ngược:** lính chặn đánh nó bị phản 20 % |
| Khống chế | **Nhanh:** +25 % tốc · **Xuyên Chặn:** bỏ qua chặn một lần · **Kháng Bẫy:** chậm, giam, đẩy còn 50 % thời gian · **Hút Nạp:** bẫy kích vào nó phải nạp lâu gấp đôi |

- **Cặp cấm:** Nhanh + Xuyên Chặn; Nhanh + Cuồng Nộ; Khiên Sương + Tái Sinh; Kháng Bẫy + Hút Nạp.
- **Số thuộc tính:** C1–2 không có tinh anh; C3–6: 1 (từ ải 10); C7–12: 2; C13–14: 2–3; C15–19: 3; C20+: 3–4 (4 chỉ cho tinh anh đi lẻ và ở C26). Tỉ lệ tinh anh: 0 % → 15 % số quái.

## 3. Tướng địch

### 3.1 Luật

- **Hào quang** là vòng vẽ trên đất (decal), nền vàng úa kèm hoa văn và icon theo loại buff (mục 1.5). Quân trong vòng có biểu tượng nhỏ trên thẻ chữ. Hào quang cùng loại không cộng dồn, lấy cái mạnh nhất. Mỗi quân nhận tối đa 2 hào quang.
- **Đội trưởng:** 5–7 W, 1 hào quang bán kính 6 m, 1 kỹ năng. Chữ D3 nối nhau, từ cuối D4. **Ấn Phá** là từ thứ 3, 6… của chuỗi (01 §3.5).
- **Thống lĩnh** (từ C11): 10–12 W, 2 hào quang bán kính 9 m, 1 kỹ năng mạnh, vùng rộng. **Ấn Phá**: một từ D4 viền đồng bên cạnh tên. Gõ Ấn Phá thì tắt hào quang 8 s và tướng khựng 1,5 s. Ấn Phá hiện lại sau 15 s. Từ C13 Thống lĩnh mang thêm 1 thuộc tính tinh anh, từ C20 mang 2.
- **Khi Thống lĩnh chết:** quân trong 12 m **Hoảng** 4 s (−30 % tốc, nhận +20 % sát thương). Đây là phần thưởng cho việc dồn tướng.
- CÂM tắt hào quang trong thời gian câm. Tướng ra ở đỉnh đợt, đi giữa toán hộ tống.
- **Tướng ăn vào ngân sách đợt:** W của tướng ≤ 35 % W_gõ của đợt (40 % ở đợt cuối Ải Tướng). Số tướng mỗi đợt theo 00 §4.5: C1–4 chỉ ở Ải Tướng và boss nhỏ; C5–13 tối đa 1; C14+ tối đa 2; 3 chỉ ở đỉnh cuối ải boss từ C20. Ví dụ đợt cuối C14 (65 s, tải 1,2): W_gõ ≈ 29,5, trần tướng ≈ 10 W: một Thống lĩnh, hoặc hai Đội trưởng nhỏ.

### 3.2 Đội trưởng

| # | id | Tên | Dáng · mở | W · giáp | Hào quang (6 m) | Kỹ năng | Khi chết | Khắc chế |
|---|---|---|---|---|---|---|---|---|
| G01 | `moss-banner` | Yêu Rêu Cầm Cờ | 2 chân · C1 ải 5 | 6 · G1 | Xung Phong: +15 % tốc | Cắm Cờ (hồi 16 s, báo 1 s): cờ đứng 8 s, quân trong 5 m +25 % đòn; cờ có từ D1 để nhổ | Quân gần chùn 1 s | ƯT, Ấn Phá; CÂM từ C2 |
| G02 | `alpha-wolf` | Sói Đầu Đàn | 4 chân · C3 | 7 · G1 | Bầy Săn: thú +15 % tốc, +15 % đòn | Tru Trăng (hồi 18 s, báo 1,2 s): thú trong 10 m hồi 15 % và vồ qua chặn ở lần kế | Sói lùi 2 s | GIAM, CHẬM |
| G03 | `shield-sergeant` | Cai Khiên Gỗ | 2 chân · C4 | 7 · G2 | Tường Khiên: +1 bậc giáp | Khiên Đồng Loạt (hồi 18 s, báo 1 s): 5 quân gần nhất +1 lớp khiên chữ | Mọi khiên chữ nó cấp vỡ | PHÁ, NỔ, CÂM |
| G04 | `ant-matron` | Kiến Chúa Thợ | Bò · C5 | 7 · G2 | Bầy Đông: bầy +40 % máu | Đẻ Bầy (hồi 12 s): cụm 6 kiến tại chỗ | Bầy trong 8 m chậm 30 % 3 s | NỔ, ƯT |
| G05 | `mist-elder` | Trưởng Lão Sương | 2 chân · C6 | 7 · K2 | Suối Sương: hồi 1,5 %/s | Gọi Hồn (hồi 20 s, niệm 3 s, từ ngắt D2): hồi sinh tối đa 3 quái Nhỏ vừa chết trong 5 s, 50 % máu | Quân mất hồi máu 6 s | NGẮT, CÂM, ƯT |
| G06 | `web-weaver` | Nhện Dệt | Bò · C7 | 7 · K1 | Lưới Tơ: bẫy trong vòng nạp chậm × 1,5 | Bọc Tơ (hồi 14 s): bọc 2 bẫy 6 s | Bẫy bị bọc nạp lại ngay | PHUN, ƯT |
| G07 | `drum-ogre` | Chằn Đánh Trống | 2 chân · C8 | 7 · G2 | Trống Trận: +20 % tốc đánh | Trống Rung (hồi 15 s, báo 1 s): lính trong 6 m choáng 1,5 s | Trống vỡ: quân trong 6 m choáng 1 s | GIAM, CÂM |
| G08 | `crow-captain` | Quạ Đầu Đàn | Bay · C9 | 6 · K1 | Mắt Quạ: quân bay +1 bậc kháng, miễn LƯỚI lần đầu | Gọi Đàn (hồi 16 s): 3 Quạ Trộm sà vào bẫy | Quân bay hạ thấp 3 s, lính đánh được | LƯỚI, Rồng |

### 3.3 Thống lĩnh

| # | id | Tên | Dáng · mở | W · giáp | Hai hào quang (9 m) | Kỹ năng | Khắc chế |
|---|---|---|---|---|---|---|---|
| G09 | `thorn-warlord` | Thống Lĩnh Gai Đen (Yêu Rêu cưỡi Heo Nanh) | Cưỡi · C11 | 12 · G2 | Giáp Gai +1 giáp; Hiệu Lệnh +20 % đòn | Lệnh Xung Phong (hồi 22 s, tù và báo 2 s): mọi quân **trên cùng đường** +30 % tốc 6 s | Ấn Phá, CÂM, GIAM |
| G10 | `thorn-matron` | Mụ Gai | 2 chân · C12 | 11 · K3 | Gai Ngược (lính đánh quân trong vòng bị phản 25 %); Mạch Rừng hồi 1,5 %/s | Rừng Gai (hồi 20 s, vòng 6 m báo 1,5 s): gai trói lính 3 s, bẫy trong vòng tắt 4 s | Ấn Phá, ƯT, PHUN |
| G11 | `elk-king` | Nai Chúa Sừng Đá | 4 chân · C13 | 12 · G3 | Kiên Định: khống chế −50 % thời gian; Giáp Rêu +1 giáp | Húc Mở Đường (hồi 18 s, vạch 2 s, từ ngắt D3): phá 1 lính chặn hoặc rào trên đường | Ấn Phá, NGẮT, PHÁ-giáp |
| G12 | `mist-hierophant` | Đại Tư Tế Sương | Bay thấp · C14 | 11 · K3 | Màn Sương: chữ quân trong vòng ẩn khi cách Bệ Rồng > 12 m (luật chữ ẩn 01 §3.3); Hồn Giáp: +1 lớp khiên chữ mỗi 15 s | Khiên Sương Lớn (hồi 24 s): khiên chuỗi 3 từ phủ vòng 8 s; vỡ khiên thì quân choáng 1,5 s | Ấn Phá, LỘ, CÂM |
| G13 | `storm-harpy` | Nữ Vương Diều Bão | Bay · C15 | 10 · K2 | Gió Thuận: quân bay +25 % tốc, đạn quân +30 % tầm; Cánh Thép: quân bay +1 giáp | Lốc Xoáy (hồi 20 s, vòng 4 m báo 1,5 s): hất lính ra khỏi đường 3 m, bẫy trong vòng tắt 3 s | Ấn Phá, LƯỚI |
| G14 | `stone-marshal` | Nguyên Soái Đá | 2 chân khổng lồ · C16 | 12 · G3 | Tường Đá: miễn đẩy, +1 giáp; Che Chắn: quân trong vòng nhận −40 % sát thương bẫy nổ | Dậm Đất (hồi 18 s, vòng 5 m báo 1,5 s): phá bẫy trong vòng (hoàn 50 %), lính choáng 2 s | Ấn Phá, GIAM, CÂM |

- Nhóm buff cho quân: tốc, đòn, tốc đánh, giáp, kháng, khiên chữ, hồi máu, hồi sinh, kháng khống chế, ẩn chữ, làm chậm bẫy, miễn đẩy, phản đòn, tầm bắn. Đủ cho mỗi chương có tổ hợp mới.

### 3.4 Trình bày từng tướng

Cùng các cột như 2.2. Mọi đòn ≥ 15 máu báo trước bằng màu đỏ. Hào quang: nền vàng úa và hoa văn theo loại (mục 1.5). Mỗi tướng có bộ âm riêng (không lấy từ lớp). Clip bắt buộc ở mục 7.2.

| # | Di chuyển | Đòn gần (tầm · sát thương · nhịp · báo) | Trúng / chết | Âm: đánh · trúng · chết · kỹ năng | VFX chữ ký | Ra mắt (2 s) |
|---|---|---|---|---|---|---|
| G01 | Đi giữa toán, cờ phất theo bước; cắm cờ thì đứng 1 s | Đâm cán cờ 1,5 m · 14 · 1,6 s · giơ cờ 0,5 s | Cờ rung, lùi nửa bước / Cờ gãy đổ, thân tan thành rêu | Hô "xông" khàn · bụp vải dày · cờ rách · tù và ngắn | Vòng vân mũi tên; cờ cắm có cột sáng vàng úa | Phất cờ, hô |
| G02 | Chạy vòng cung dẫn bầy, dừng hú trên gò | Vồ 4 m · 22 · 2 s · cúi rạp 0,7 s | Gầm, lùi / Lăn, khói tan từ vết nứt | Gầm gừ trầm · ẳng nặng · tru dài tắt · tru trăng | Vòng vân móng; tru: sóng vòng lan 10 m | Tru trên đá |
| G03 | Bước đều, khiên trước, gõ khiên theo nhịp | Đập khiên 1,5 m · 18 · 1,8 s, đẩy lính 1 m · giơ khiên 0,6 s | Khiên lóe bạc / Khiên vỡ, ngã ngửa | Hô nhịp · cộp gỗ dày · khiên lăn · ba tiếng gõ khiên | Vòng vân khiên; khiên chữ bạc mọc trên 5 quân | Đập khiên ba lần |
| G04 | Bò chậm, bụng phồng, kiến quanh chân | Cắn kẹp 1,5 m · 15 · 1,5 s | Bụng rung / Bụng xẹp, vỏ nứt | Lạo xạo nặng · cộp vỏ dày · rắc vỡ và rít · ục ục khi đẻ | Vòng vân tổ ong; đất nứt, kiến trào | Ngẩng đầu, râu rung |
| G05 | Lướt chậm sau toán, gậy chạm đất mỗi 2 s | Cầu sương 10 m · 12 · 2,2 s | Áo khói rách / Tan vào sương, gậy rơi | Lẩm bẩm trầm · xoẹt vải · thở dài vang · chuông gió ngược | Vòng vân lá; Gọi Hồn: cột khói lục úa trên chỗ quái vừa chết | Giơ gậy, sương xoáy |
| G06 | Leo đá ven đường, thả tơ treo mình | Cắn 1,5 m · 14 · 1,4 s | Co chân / Co quắp, tơ đứt | Lạo xạo · bộp · rít khẽ · "xẹt" tơ dài | Vòng vân mạng nhện; kén tơ bạc trên bẫy | Thả tơ từ cao xuống |
| G07 | Bước nặng theo nhịp trống | Nện dùi vòng 2 m · 28 · 2,2 s · giơ dùi 0,9 s | Khựng / Trống vỡ, đổ sập | Gầm · bịch thịt dày · trống vỡ và đổ ầm · trống ba nhịp | Vòng vân sóng âm; Trống Rung: vòng đỏ báo 1 s | Đánh trống |
| G08 | Bay vòng cao 7 m, sà khi gọi đàn | Mổ sà · 12 · 1,6 s · bóng sà 0,6 s | Lông bay / Rơi xoáy | Quạ khàn · phạch · quạ tắt dài · kêu gọi đàn | Vòng vân lông vũ trên đất dưới nó | Xòe cánh kêu |
| G09 | Heo phi, người cầm giáo | Đâm giáo 2 m · 30 · 2 s · giơ giáo 0,8 s | Heo hếch, người lắc / Ngã khỏi heo, cả hai tan | Hô lệnh vang · bịch nặng · rống và đổ · tù và dài | 2 vòng 9 m (gai, kiếm); Lệnh Xung Phong: vệt sáng dọc đường | Heo chồm, tù và |
| G10 | Đi chậm, gai mọc theo bước | Quất roi gai 4 m · 22 · 1,8 s · vung 0,6 s | Gai co / Hóa bụi gai khô rồi tan | Cười khàn · xào lá · gãy cành · rễ trồi | Vòng vân gai và lá; Rừng Gai: gai trồi vòng 6 m báo 1,5 s | Gai mọc quanh |
| G11 | Đi oai, dừng cào đất trước húc | Húc 8 m · 40 · vạch đỏ 2 s, từ ngắt | Sừng tóe đá / Quỵ, sừng đá vỡ | Khịt trầm · cộc đá · rống dài · cào đất và rống | Vòng vân sừng và khiên; vạch húc | Ngẩng sừng |
| G12 | Lơ lửng 1 m, áo khói kéo dài | Tia sương 12 m · 18 · 2 s · tay giơ 0,6 s | Áo rách khói / Tan thành sương lớn | Ngâm trầm · vút thủy tinh · thở dài vọng · hợp xướng ngược | Vòng vân mắt và khiên; vòm khói bạc | Dang tay, sương dâng |
| G13 | Bay cao, lượn rộng, lao xuống | Lao móng 6 m · 25 · bóng sà 0,8 s | Chao cánh / Rơi xoáy | Rít cao · phạch lông · rít tắt · gió hú | Vòng vân gió; cột gió báo vòng 1,5 s | Vỗ cánh tạo gió |
| G14 | Bước rung đất, rêu rơi | Đấm vòng 3 m · 45 · 2,5 s · vòng đỏ 1 s | Đá vụn, không lùi / Vỡ thành khối đá lớn | Rền đá · cộc đá dày · đổ ầm dài · đá nghiến và dậm | Vòng vân đá và khiên; nứt đất vòng 5 m | Dậm chân, đá bay |

## 4. Boss

### 4.1 Luật

- **Ra mắt:** lặng trước boss 12 s (01 §1.2), không sinh toán mới. Cảnh Intro 3–4 s trong khung nhỏ. Quái cũ trên sân vẫn đi.
- **Pha theo ngưỡng máu.** Chuyển pha: boss gầm 2,5 s, miễn sát thương, từ ngắt cũ bị hủy. Lần đầu gặp cơ chế mới thì hiện một dòng giải thích.
- **Tối đa 2 cơ chế cùng lúc** và **một từ ngắt tại một thời điểm.** Không có đòn ngẫu nhiên không báo.
- Đòn thường báo trên đất ≥ 1,2 s. Đại chiêu nạp 3–6 s (như Space: 3,4–6,8 s) kèm từ ngắt.
- Thua một cơ chế không thua ngay. Chỉ mất máu Rồng, mất đồ hoặc thêm quân.
- Boss không bị chặn, lính bị đẩy dạt. Chậm tối đa 30 %. Giam, choáng còn nửa thời gian, trừ khi boss đang Dễ Tổn Thương.
- **Thời lượng và W:** công thức và bảng ở **00 §4.7** (W_boss = 0,38 × 0,7 × t, cỡ theo bot 35 WPM). Cột W ở bảng 4.3 đã tính theo đó.
- **Đòn kết:** dưới 5 % máu hiện một từ xanh ngọc (boss chương: chuỗi chủ đề 2–3 từ). Gõ xong thì boss gục ngay, có cảnh đẹp.
- **Buff cho quân:** mỗi boss có ít nhất một buff cho quân theo pha, có báo trước, có khắc chế (mục 4.5).
- Cỡ trên màn ≥ 120 px ở 1080p (art-pipeline 6).

### 4.2 Mười hai cơ chế gõ

| Mã | Tên | Cách chơi | Nguồn |
|---|---|---|---|
| ĐY | Điểm yếu | Bộ phận mang từ (nanh, càng, tim). Phá bộ phận thì tắt một đòn hoặc boss khuỵu 4 s | Space `weak-point` |
| KC | Khiên chuỗi | 3–5 từ đánh số, gõ đúng thứ tự. Sai thứ tự: không tính, không phạt | Space `shield-sequence` |
| NG | Từ ngắt | Đại chiêu nạp, hiện từ đỏ. Gõ kịp: hủy đòn, boss choáng 2–3 s, Dễ Tổn Thương +50 % trong 6 s | Space `interrupt-charge` |
| CN | Cuồng nộ | 8 s mưa từ D1, mỗi từ 0,5 W. Hết giờ không phạt | Space `rapid-rage` |
| NC | Nguyền chuẩn | 6–8 s: mỗi phím sai hồi 1 % máu boss. Không sai phím nào: đòn cuối × 1,5 | Space `accuracy-curse` |
| HN | Hỏi nghĩa | Hiện nghĩa tiếng Việt, từ loại và số ô chữ của 2–4 từ đã học trong ải; gõ từ tiếng Anh vào ô trả lời riêng. Luật đề bài (nghĩa duy nhất, nhận mọi từ cùng nghĩa trong bộ, không dò được chữ đầu) và mốc gợi ý (3 s IPA, 6 s chữ đầu): 01 §3.6 | Mới (học) |
| NE | Nghe | Boss "nói" từ qua kênh phát âm chung (01 §6.4); thẻ chỉ có loa và số ô chữ; Tab nghe lại; loại nhóm đồng âm; tắt tiếng thì hiện IPA | Mới (học) |
| KG | Khung giờ | Chỉ nhận chữ khi lõi mở 3–4 s trong mỗi 6–8 s | Typing of the Dead |
| TT | Tìm thân thật | 3–4 bản sao, mỗi bản một từ; giữa sân hiện một nghĩa. Gõ đúng thân thật: choáng; gõ bản sao: bản sao tan | Mới (học) |
| CD | Chuỗi chủ đề | 3–5 từ đơn cùng chủ đề, gõ liền (00 D19; không dùng câu); dùng cho Đại chiêu cuối và đòn kết | TD (đổi) |
| SB | Song boss | Hai thân. Hạ một thân thì phải hạ thân kia trong 10–15 s, nếu không nó hồi sinh với 50 % máu | Mới |
| ĐK | Đòn kết | Mục 4.1 | TD 18.9 |

### 4.3 Hai mươi boss

| # | id | Tên | Chương | Dáng · model | W | Pha và cơ chế | Đòn chính và báo trước |
|---|---|---|---|---|---|---|---|
| B01 | `tuskfather` | Lợn Lòi Chúa Nanh Rêu | C1 | 4 chân · mới | 30 | P1 húc; P2 (60 %) ĐY hai nanh, mỗi nanh 2 từ; ĐK | Húc thẳng, vạch đỏ 1,5 s; sau húc choáng 2 s (nhận × 1,5); gọi 4 cụm kiến |
| B02 | `moss-chieftain` | Tù Trưởng Yêu Rêu | C2 | 2 chân · mới | 31 | P1 gọi toán; P2 (60 %) KC 3 từ trên cột tô tem, vỡ khiên thì choáng 3 s | Ném rìu xoáy vào lính, vòng 2 m báo 1,5 s |
| B03 | `thorn-queen` | Nữ Hoàng Ong Gai | C3 | Bay · mới | 32 | P1 mưa ngòi; P2 (65 %) NG "Tổ Vàng" nạp 4 s; P3 (30 %) CN | 5 vòng nhỏ báo 1,2 s; ngắt hỏng thì ra 6 ong |
| B04 | `twin-wolves` | Song Lang Gió và Bóng | C4 | 4 chân × 2 · G02 phóng to | 2 × 16 | SB suốt trận; P2 (mỗi con 50 %) mỗi con hiện một từ ngắt "Song Hú" | Vồ luân phiên vào lính; hú thành công thì hồi 20 % cho con kia |
| B05 | `bog-toad-king` | Cóc Vương Đầm Lầy | C5 | 4 chân nặng · mới | 33 | P1 nuốt lính; P2 (60 %) ĐY túi họng 3 từ; P3 (25 %) HN 3 từ | Lưỡi kéo, vạch 1,2 s; lính bị nuốt 6 s, gõ từ nhả D2 trên bụng cóc để nhả sớm; gọi nòng nọc (bầy) |
| B06 | `web-matriarch` | Nhện Chúa Tơ Tím | C6 | Bò · mới | 35 | P1 giăng tơ một đường; P2 (65 %) KG: treo xuống 3 s mỗi 7 s; P3 (30 %) KC 4 từ khi cuộn kén hồi máu | Tơ bọc mọi bẫy trên một đường; mạng tơ mang một từ D2, gõ xong thì Rồng đốt tơ; đẻ kén |
| B07 | `canyon-colossus` | Khổng Lồ Hẻm Đỏ | C7 | 2 chân khổng lồ · mới | 36 | P1 dậm đất; P2 (60 %) ĐY ba tinh thể (vai, lưng, gối; vỡ gối thì khuỵu 4 s); P3 (25 %) NG "Lở Núi" D4 | Sóng vòng loang báo 1,5 s; ném tảng vòng 3 m báo 2 s; ngắt hỏng: −15 % máu Rồng, lính choáng |
| B08 | `tide-crab` | Cua Mai Núi | C8 | Bò · mới | 37 | P1 KG mai 4 s mở / 4 s đóng; P2 (60 %) ĐY hai càng, 3 từ mỗi càng; P3 (25 %) NE "bài hát sóng" | Kẹp lính; nước dâng làm đường ven sông chậm 30 %; gọi cua con |
| B09 | `night-bat-lord` | Chúa Dơi Đêm | C9 | Bay · mới | 39 | P1 sân tối; P2 (60 %) TT ba bóng dơi; P3 (25 %) NG "Hút Sinh Lực", chuỗi 3 từ D1 | Tối: Vùng Chữ co còn 14 m, nới thêm 6 m quanh Đèn Đom Đóm (01 §3.3); bám Rồng hút 2 % máu/s tới khi gõ xong |
| B10 | `magma-salamander` | Kỳ Nhông Dung Nham | C10 | 4 chân · mới | 40 | P1 vệt dung nham; P2 (65 %) KG lặn dung nham, trồi ở cổng khác; P3 (30 %) NC + CN | Phun lửa hình nón báo 1,2 s; vũng sôi báo 2 s trước khi trồi |
| B11 | `rotwood-ancient` | Cổ Thụ Mục | C11 | Cây đi · mới | 40 | P1 rễ trói, mọc 3 mầm D1 hồi máu cho nó; P2 (65 %) KC vỏ 4 từ; P3 (30 %) HN, gọi Nai Rêu; ĐK là chuỗi chủ đề 3 từ | Rễ trồi vòng 1,2 s; mầm sống 10 s |
| B12 | `spore-mother` | Mẹ Nấm | C12 | Khối nấm · mới | 41 | Mỗi lần mất 25 % máu tách 2 Nấm Con 3 W, phải hạ trong 20 s kẻo nhập lại; P2 ĐY 3 mũ; P3 CN | Mây ngủ lên lính báo 1,5 s |
| B13 | `storm-beetle` | Bọ Hung Sấm | C13 | Bay lơ lửng · `lieutenant-nature` | 43 | P1 KC khiên điện 3 từ mỗi 20 s; P2 (60 %) NG "Lôi Đình" D3, gọi Bọ Axit; P3 (25 %) KG cánh mở 3 s, đóng 4 s | Sét nối các nhà phép, vạch báo 1,5 s |
| B14 | `mist-knight` | Kỵ Sĩ Sương | C14 | Cưỡi ngựa ma · mới | 18 + 26 | P1 ngựa (18 W) phi xuyên lính; P2 (ngựa chết) kỵ sĩ đi bộ, KC 4 từ, gọi Hồn Sương; P3 (30 %) NE "lời nguyền thì thầm" | Phi thẳng, vạch dài 1,5 s; chém vòng 3 m báo 1 s |
| B15 | `river-serpent` | Thủy Xà Sông Lam | C15 | Rắn · mới | 45 | P1 KG trồi 4 s ở hai khúc sông; P2 (60 %) ĐY 4 đốt vây, phá từ đuôi lên đầu; P3 (25 %) NG "Hồng Thủy" cụm 2 từ | Quật đuôi vào nhà gần sông; ngắt hỏng: nước tràn một đường 8 s, đẩy lính |
| B16 | `raven-sage` | Quạ Ảo Thuật | C16 | 2 chân · mới | 45 | P1 TT 4 bản sao mỗi 20 s; P2 (60 %) NC + HN, mỗi câu sai thêm 1 bản sao; P3 (25 %) chuỗi chủ đề 4 từ để phá gương | Bắn lông vũ quạt 3 tia, báo 1 s |
| B17 | `frost-stag` | Hươu Băng Hắc Vụ | C17 | 4 chân · mới | 47 | P1 hào quang hồi 2 %/s mọi quái trong 10 m; P2 (65 %) ĐY hai nhánh gạc, mỗi nhánh 3 từ, gãy thì tắt hồi; P3 (30 %) NG "Bão Tuyết" + KC | Băng phủ đường, lính trượt; gọi Sói Băng |
| B18 | `deep-centipede` | Rết Ngàn Đốt | C18 | Bò đào · mới | 47 | P1 đào ngầm, trồi với 6 đốt mang từ D2 (ĐY); P2 (50 %) tách hai nửa (SB 15 s); P3 CN | Nứt đất vòng báo 1,5 s trước khi trồi xuyên lính |
| B19 | `black-wyrm` | Hắc Long | C19 | Bay · `draconis-v3` đổi vật liệu | 48 | P1 phun lửa vào nhà; P2 (65 %) "song đấu": NG, gõ kịp thì Hỏa Long phun ngược (Cast; đang Viêm Đế thì Spit); P3 (30 %) KC 5 từ + CN; ĐK là chuỗi chủ đề 4 từ | Phun lửa nón báo 1,5 s; Spit_Big vòng 4 m báo 2 s |
| B20 | `mist-mother` | Mẹ Hắc Vụ | C26 | Khối sương và tim · mới | 72 | P1 sương phủ, gọi đủ họ; P2 (75 %) ĐY 3 tim trên 3 đường, 4 từ mỗi tim, tim hồi nhau nếu không hạ hết trong 20 s; P3 (45 %) HN và NE luân phiên; P4 (20 %) CN + NG "Nuốt Rừng" cụm 3 từ; ĐK là chuỗi 4 từ đầu tiên người chơi học ở C1 | Mọi đòn báo ≥ 1,5 s; mỗi pha một màu sương |

### 4.4 Boss nhỏ và Hắc Hóa

- **Ải 10 mỗi chương:** C1–4 dùng Đội trưởng mạnh: W 16, 2 pha, thêm một kỹ năng. Từ C5 dùng boss của chương c−3, bản rút gọn: 2 pha, W 16–24 (00 §4.7).
- **Ải 5 và 15:** Ải Tướng. Đợt cuối có Đội trưởng; từ C11 có Thống lĩnh. Trần W tướng theo mục 3.1.
- **C20–25: song boss Hắc Hóa.** Boss A đánh pha 1–2; khi A còn 30 % máu thì boss B vào sân. Mỗi boss có thêm một cơ chế mà bản gốc chưa có. Tổng W hai thân 52–56 (00 §4.7).

| Chương | Song boss | Luật Hắc Vụ của chương (luôn ghi trên thẻ ải, báo trước) |
|---|---|---|
| C20 | B07 + B11 | Sương lan: Vùng Chữ co còn 18 m; Đèn Đom Đóm nới thêm 6 m (01 §3.3) |
| C21 | B05 + B12 | Quái chết để vũng hồi máu 3 s |
| C22 | B09 + B16 | Tướng hồi sinh một lần |
| C23 | B08 + B15 | Thủy triều đổi đường mỗi 2 đợt (báo trước 1 đợt) |
| C24 | B10 + B13 | Mưa tro tắt một bẫy mỗi 20 s (vòng báo 2 s) |
| C25 | B14 + B19 | Đội trưởng cũng có Ấn Phá riêng cạnh tên, như Thống lĩnh |

### 4.5 Trình bày từng boss và buff cho quân

Mỗi boss có bộ âm và nhạc riêng (05 §6.4, §7.2). Buff cho quân có báo trước (cột sáng hoặc tiếng gầm ≥ 1 s, icon trên thẻ chữ quân) và luôn có khắc chế ngoài gõ. Lời Thề Bạch Vũ xóa mọi buff trong 20 m (01 §2.4).

| # | Di chuyển | Trúng / đổi pha / chết | Âm chữ ký | VFX chữ ký | Buff cho quân theo pha · khắc chế | Ra mắt |
|---|---|---|---|---|---|---|
| B01 | Đi vòng, cào đất, húc thẳng | Nanh mẻ dần; P2 nanh sáng vàng úa; đổ nghiêng | Rống trầm, vó dậm | Bụi húc, rêu bay | P2 Bầy Đông: kiến trong 8 m +30 % máu · PHUN, Bom Hạt Thông | Phá rào gỗ lao ra |
| B02 | Đi giữa toán, cắm cột tô tem | Cột nứt theo khiên; ngã ôm cột | Trống trận, hô | Cột tô tem khắc rêu | P1 +20 % đòn quân trong 10 m; P2 +1 lớp khiên chữ mỗi 20 s · Bùa Phá Chữ, Chuông Bạc | Bước qua cổng gỗ |
| B03 | Bay lượn trên tổ | Cánh rách; rơi xoáy | Vo ve trầm | Phấn ong vàng úa | P2 ong trong 12 m +25 % tốc; P3 ong +1 lớp khiên chữ · Lưới Phóng, Cột Chậm | Tổ vỡ, bay ra |
| B04 | Hai sói vờn hai bên đường | Mỗi con lóe màu riêng; tru khi con kia chết | Song hú | Gió trắng và bóng chàm | P2 Song Hú: thú +20 % tốc đánh 6 s (từ ngắt) · NGẮT, GIAM | Hai bóng lao từ hai cổng |
| B05 | Nhảy nặng từng quãng | Túi họng xẹp dần; lật ngửa | Ộp vang | Vũng độc lục | P2 nòng nọc +1 bậc giáp; P3 quái trong vũng hồi 2 %/s · Bom Hạt Thông, Chuông Bạc | Trồi khỏi bùn |
| B06 | Treo tơ, đổi đường | Kén rung; rơi khỏi tơ | Lạo xạo, tơ căng | Tơ bạc, kén | P2 quái trên đường có tơ +30 % tốc; P3 kén hồi quân · PHUN, Lời Thề | Thả xuống giữa sân |
| B07 | Bước rất chậm, rung đất | Tinh thể vỡ; khuỵu gối | Rền đá | Bụi đá, nứt đất | P2 quân trong 10 m −40 % sát thương bẫy nổ; P3 miễn đẩy · Chuông Bạc, Lồng Đá | Đá lở mở lối |
| B08 | Bò ngang hai bờ sông | Càng gãy; lật ngửa | Lách cách lớn, sóng | Bọt nước, mai sáng | P1 cua con +1 bậc giáp khi mai đóng; P3 quái ven sông +25 % tốc · Lưới Dây Leo, Bùn Lầy | Trồi từ sông |
| B09 | Bay vòng, sà xuống Rồng | Cánh rách; rơi vào bóng tối | Rít dơi, vọng | Bóng tối vùng, mắt vàng úa | P1 Vùng Chữ co (Tối); P2 dơi hút máu hồi 10 % · Đèn Đom Đóm, Lưới Phóng | Trăng bị che |
| B10 | Bò trên vệt nham, lặn trồi | Vảy nguội đen dần | Xèo nham, gầm | Vệt nham, tro | P2 quái trên vệt nham +20 % đòn, miễn Chậm · Bùn Lầy (Ướt tắt nham), Ấn Băng | Trồi khỏi nham |
| B11 | Rễ kéo thân đi | Vỏ bong mảng; gục thành gốc | Gỗ kẽo kẹt | Rễ trồi, mầm | P1 mầm hồi boss; P3 Nai Rêu +1 lớp khiên chữ · PHUN, Chuông Bạc | Cây cổ thụ đứng dậy |
| B12 | Lăn, phồng xẹp | Mũ rách; xẹp thành đống | Bụp mềm, ọc ọc | Mây bào tử | Mỗi lần tách: Nấm Con kháng khống chế 50 % · Bom Hạt Thông, Nấm Độc | Nấm mọc phồng to |
| B13 | Bay lơ lửng thấp | Vỏ nứt tia điện; rơi đổ | Rè điện, sấm | Sét nối nhà | P1 quân bay +1 lớp khiên chữ mỗi 20 s; P3 quân +20 % tốc đánh · Chuông Bạc, Lời Thề | Sấm đánh xuống |
| B14 | Ngựa phi, rồi đi bộ | Ngựa tan khói; kỵ sĩ gục | Vó ma, giáp lạnh | Khói xám, kiếm sương | P2 Hồn Sương miễn chặn, +1 lớp khiên chữ · Đèn Đom Đóm, Chuông Bạc | Phi qua màn sương |
| B15 | Trồi, lặn hai khúc sông | Vây vỡ từ đuôi; chìm | Sóng, rít dài | Nước tràn | P2 quái ven sông hồi 2 %/s; P3 nước tràn đẩy lính · Lồng Đá, Chuông Bạc | Sóng dâng cao |
| B16 | Đi nhịp, đổi chỗ với bản sao | Gương nứt; vỡ lông | Quạ cười, gương vỡ | Lông, ảnh gương | P1 quân bay ẩn chữ 3 s sau mỗi lần đổi chỗ; P2 quân +1 bậc kháng · Đèn Đom Đóm, Tháp Canh | Bước ra từ gương |
| B17 | Đi oai, băng lan theo bước | Gạc gãy; quỵ trên băng | Gió tuyết, chuông băng | Băng phủ đường | P1 hồi 2 %/s quân trong 10 m; P3 quân miễn Chậm, Đóng băng · Chuông Bạc, Lời Thề | Bão tuyết mở ra |
| B18 | Đào ngầm, trồi xuyên | Đốt rụng; tách đôi | Đất nứt, lách cách | Nứt đất vòng | P2 mỗi nửa: quân quanh nó +20 % đòn · Trống Đất, Bom Hạt Thông | Trồi giữa sân |
| B19 | Bay vòng cao, sà phun | Vảy đen bong; rơi | Gầm rồng trầm | Lửa đen viền vàng úa | P1 quân trong 12 m +1 bậc kháng; P3 cuồng nộ toàn sân +20 % tốc 8 s · Lời Thề, Chuông Bạc | Hai rồng đối mặt |
| B20 | Khối sương trôi giữa ba đường | Tim vỡ từng cái; sương tan | Hợp xướng ngược, tim đập | Mỗi pha một màu sương | P1 +1 bậc giáp; P2 tim hồi quân; P3 quân bay ẩn chữ; P4 cuồng nộ · Lời Thề, Ấn Phá trên tim | Rừng tối dần |

## 5. Đợt và nhịp sinh

### 5.1 Ải và đợt

- Số đợt, độ dài đợt, giờ nghỉ, thời lượng theo loại ải: **00 §4.5** (nguồn duy nhất). Tải từng đợt: 00 §4.4.
- Ải 6 đợt có một **đợt thở** ở đợt 4: tải −20 % so với đường.
- Mọi lần sinh dùng luồng RNG riêng theo seed (`platform/rng`), để bot chạy lại y hệt.
- Nhịp co giãn theo tốc gõ k_E (00 §4.4): mọi khoảng sinh × 1 / k_E. Thành phần không đổi.

### 5.2 Toán: đơn vị sinh

| Dạng | Số con | Khoảng cách trong toán | Dùng cho |
|---|---|---|---|
| Lẻ | 1 | — | Nặng, Khổng lồ, loài đặc biệt |
| Đôi | 2 | 0,8 s | Nhỏ, Vừa |
| Hàng | 3–6 | 0,6 s | Nhỏ |
| Cụm bầy | 4–10 | Cùng lúc, lệch 0,5 m | Bầy (một từ cụm) |
| Hộ tống | 1 Nặng hoặc tướng + 2–6 | Lính trước và sau 1 s | Tướng, Khiên, Pháp Sư |
| Gọng kìm | 2 toán, 2 đường | Cùng lúc | Từ C4 |
| Đàn bay | 2–5 con bay | 0,5 s | Đường bay |

### 5.3 Nhịp, đỉnh, lặng

- Mỗi đợt có 2–3 **đỉnh** dài 6–10 s, nhịp × 1,6. Giữa hai đỉnh có **lặng** ≥ 8 s, nhịp × 0,4. Đỉnh cuối mạnh nhất.
- **Không đổ đàn:** mỗi cổng sinh tối đa một toán mỗi 1,5 s.
- **Trần quái sống là hằng số của luật** (00 §4.8, D10), giống nhau ở mọi bậc máy. Chạm trần thì toán mới chờ ở cổng; đồng hồ đợt không dừng. Bậc máy chỉ đổi cách vẽ (05 §8).
- Không có "sàn quái sống" kéo lịch lên sớm. Quãng lặng luôn được giữ.
- Mẫu một đợt 60 s: 0–8 s mở (2 toán nhỏ, 1 đường) → 8–18 s đỉnh 1 (2 đường) → 18–28 s lặng → 28–40 s đỉnh 2 (tướng hoặc quái Nặng) → 40–48 s lặng → 48–60 s đỉnh 3 (bầy + bay).

| Giai đoạn | Chương | Toán mỗi đợt | Nhịp toán | Cỡ toán (Nhỏ) | Quái sống: thường / đỉnh | Bay tối đa |
|---|---|---|---|---|---|---|
| Học | 1–3 | 6–10 | 4–6 s | 1–3 | 6–12 / 20–25 | 15 % ĐĐ |
| Mở rộng | 4–8 | 9–14 | 3–5 s | 2–4 | 12–30 / 35–70 | 25 % |
| Trộn | 9–14 | 12–18 | 2,5–4 s | 3–5 | 25–60 / 80–120 | 30 % |
| Dày | 15–19 | 15–22 | 2–3,5 s | 3–6 | 40–90 / 160 | 30 % |
| Hắc Hóa | 20–26 | 18–26 | 1,5–3 s | 4–6 | 60–120 / 220 | 30 % |

- Phần lớn quái lúc đỉnh muộn là bầy và quái Nhỏ, chết bằng từ cụm, PHUN và bẫy. Người chơi không phải gõ 200 từ: một cụm 8–10 con chỉ là 1 từ.

### 5.4 Ngân sách đợt: tải gõ trước, đe dọa sau

Hai bước, theo thứ tự (00 D05):

```
Bước 1 — W_gõ(đợt) = L(w) × 22,7 × phút của đợt     // L(w) theo 00 §4.4, giống nhau ở mọi chương
Bước 2 — chọn thành phần sao cho ĐĐ đợt ≈ B_c × (1 + 0,14 × (w − 1)) × s(i)  mà W_gõ vẫn đúng bước 1
B_c (đợt 1): bảng 00 §4.8 (C1 18 · C5 32 · C10 55 · C15 80 · C20 105 · C26 140)
```

- ĐĐ trên mỗi W gõ tăng dần theo chương: từ ~1,6 ở C1 tới ~12 ở C26. Đe dọa tăng nhờ quái nhanh hơn, nhiều kỹ năng hơn, nhiều bầy hơn (bầy đông nhưng một cụm chỉ 1 W gõ), tinh anh, hào quang, nhiều đường hơn. **Số W phải gõ mỗi phút không tăng.**
- Tướng ăn vào W_gõ của đợt, trần ở mục 3.1.
- Đầu chương sau ≈ 75 % đe dọa đỉnh chương trước (răng cưa); tải gõ thì giữ trong dải.
- Mỗi ải tối đa 8 loài thường. Mỗi đợt tối đa 3 loài phá (phá nhà, phá bẫy, trộm) và 1 nguồn ẩn chữ.
- Hồi máu, khiên, triệu hồi chỉ ra trong toán hộ tống có ≥ 3 quân.
- Ví dụ số khớp nhau: DESIGN.md §5 (ải thường C1 và C20).

### 5.5 Trộn theo đường

| Số đường | Có từ | Luật trộn |
|---|---|---|
| 1 | C1 và ải dạy | Mọi toán một đường |
| 2 | C2 | Đường chính nhận 60–70 % ĐĐ; đổi bên ít nhất một lần mỗi ải. Gọng kìm từ C4 |
| 3 | C5 | **Đường đặc trưng:** mỗi đường có một họ chính (≥ 60 % ĐĐ của đường), thẻ đợt báo trước |
| 4 | C8 (từ ải 11) | Mỗi đỉnh tối đa 2 đường cùng chạy (C8–14), 3 đường (C15–19), 4 đường chỉ ở đỉnh cuối ải boss và từ C20 |
| Đường nhập | — | Toán từ hai nhánh tới chỗ nhập lệch nhau ≥ 3 s, để chữ không chồng |
| Sông | C8 | Lươn và Cua sinh ở điểm sông, tính vào đường gần nhất |

### 5.6 Thẻ báo đợt

- Hiện trong lúc nghỉ và trong cửa hàng. Mỗi cổng có: biểu tượng họ, số con, dấu riêng (cánh = bay, búa = phá, mũi khoan = đào, mặt nạ = ẩn chữ, vương miện = tướng, sừng = boss).
- Có một dải nhịp nhỏ cho thấy đỉnh rơi vào giây nào. Người chơi lên kế hoạch được.
- **Ải dạy loài mới:** loài đó ra lẻ 3 lần trước khi trộn, và ải tặng một lượt món khắc chế nó.

## 6. Đường cong độ khó 520 ải

### 6.1 Khung chương

- 26 chương × 20 ải. Trong một chương (04 §1.2): ải 1–4 dạy loài mới thứ nhất; ải 5 Ải Tướng; 6–8 trộn; **9 Ải Ôn**; 10 boss nhỏ; 11–14 loài mới thứ hai, combo; 15 Ải Tướng; 16–18 combo và luật ải; **19 Ải Ôn** (Lửa Trại); 20 boss chương.
- Sau 520 ải: thêm chương mới (mùa) bằng dữ liệu, cùng bộ máy.

| C | Vùng (kit · biến thể) | Loài mới | Tướng mới | Đường tối đa | Thuộc tính tinh anh | Combo hoặc luật mới | Boss ải 20 |
|---|---|---|---|---|---|---|---|
| 1 | Rừng thông có sông · xuân | E25, E09, E01 | G01 | 1 | 0 | Từ cụm bầy | B01 |
| 2 | Rừng thông · hè | E10, E11, E02 | — | 2 | 0 | Bầy bay đầu tiên; quái đứng bắn | B02 |
| 3 | Rừng phép tím lam · sáng | E12, E13, E18 | G02 | 2 | 1 | Khiên chữ; Khiên + Cung | B03 |
| 4 | Đồng cỏ đồi · hè | E26, E19, E14 | G03 | 2 | 1 | Gọng kìm | B04 |
| 5 | Đầm lầy · sương sớm | E15, E20, E27 | G04 | 3 | 1 | Từ ngắt; Pháp Sư + Chằn | B05 |
| 6 | Rừng mưa · mưa | E28, E03, E21 | G05 | 3 | 1 | Phá bẫy; Nhện Tơ + Heo | B06 |
| 7 | Hẻm đá đỏ · trưa | E22, E05, E04 | G06 | 3 | 2 | Chữ thì thầm; Lửng + Kiến | B07 |
| 8 | Bờ biển đá · hoàng hôn | E29, E30, E06 | G07 | 4 | 2 | Sông sinh quái; Diều Hâu + Đặt Mìn; Cua + Lươn | B08 |
| 9 | Rừng phép · đêm | E23, E07, E31 | G08 | 4 | 2 | Chữ ẩn; Ngài + Linh Miêu | B09 |
| 10 | Núi lửa · tro | E17, E08, E16, E24 | — | 4 | 2 | Cú + Phù Thủy | B10 |
| 11 | Rừng thông · thu | E32 | G09 | 4 | 2 | Thống lĩnh và Ấn Phá riêng; Người Đá + Kiến | B11 |
| 12 | Đầm lầy · đêm đom đóm | Nấm Đầm | G10 | 4 | 2 | Nguyền Chuẩn; Nấm Phồng + Nai | B12 |
| 13 | Đồng cỏ · bão | Ong Sấm | G11 | 4 | 2–3 | Thống lĩnh mang thuộc tính | B13 |
| 14 | Rừng mưa · đêm | Linh Miêu Đêm | G12 | 4 | 2–3 | Hai tướng khác hào quang | B14 |
| 15 | Bờ biển · bão | Cua San Hô | G13 | 4 | 3 | 3 đường cùng đỉnh | B15 |
| 16 | Hẻm đỏ · đêm | Người Đá Hồng Ngọc | G14 | 4 | 3 | Thống lĩnh + Đội trưởng | B16 |
| 17 | Rừng thông · đông tuyết | Sói Băng | — | 4 | 3 | Đường băng, lính trượt | B17 |
| 18 | Rừng phép · mùa hoa | Nai Hoa | — | 4 | 3 | Combo ba loài | B18 |
| 19 | Núi lửa · phun trào | Kiến Lửa | — | 4 | 3 | Mọi combo | B19 |
| 20–25 | Sáu vùng Hắc Vụ | — | — | 4 | 3–4 | Luật Hắc Vụ (mục 4.4); ≤ 2 tướng mỗi đợt, 3 ở đỉnh cuối ải boss | Song boss |
| 26 | Tim Hắc Vụ | — | — | 4 | 4 | Mọi thứ | B20 |

### 6.2 Combo (cặp hợp sức)

| Combo | Vì sao khó | Cách giải | Từ |
|---|---|---|---|
| Khiên + Cung (E13 + E11) | Cung đứng sau khiên chữ | Gõ khiên trước, NỔ vào cụm cung đứng yên | C3 |
| Pháp Sư + Chằn (E15 + E12) | Chằn trâu lại được hồi | NGẮT phép hồi, CÂM | C5 |
| Nhện Tơ + Heo (E28 + E19) | Tơ trói lính, heo húc thẳng vào Rồng | Hạ nhện trước, ĐẨY heo | C6 |
| Lửng + Kiến (E22 + E25) | Lửng lôi bẫy lên, kiến tràn qua | RUNG, PHUN cụm | C7 |
| Diều Hâu + Đặt Mìn (E06 + E14) | Mìn rơi xuống sau tuyến chặn | LƯỚI, hạ diều hâu trước khi thả | C8 |
| Cua + Lươn (E29 + E30) | Cua chặn đường, lươn phục từ sông | GIAM ở bờ sông, gõ lươn khi lên bờ | C8 |
| Ngài + Linh Miêu (E07 + E23) | Chữ ẩn cộng tàng hình | LỘ ở chỗ nhập đường | C9 |
| Cú + Phù Thủy (E08 + E16) | Bẫy bị nguyền, nhà bị bắn tỉa | NGẮT tia cú, CÂM phù thủy | C10 |
| Người Đá + Kiến (E17 + E25) | Người Đá phá rào, bầy tràn qua | GIAM người đá xa rào, PHUN bầy | C11 |
| Nấm Phồng + Nai (E26 + E21) | Nấm con đứng trên mầm hồi | PHUN đốt mầm, NỔ | C12 |

### 6.3 Đòn bẩy độ khó

- **Đòn bẩy (cách tăng → trần):** thành phần đợt (thêm loài, vai khó → 8 loài mỗi ải) · combo (0 → 3 mỗi ải) · tướng (0 → 2 mỗi đợt; 3 chỉ ở đỉnh cuối ải boss) · tinh anh (thuộc tính 0 → 4, tỉ lệ 0 → 15 %, có cặp cấm) · đường (1 → 4; số đường cùng đỉnh 1 → 4) · biến chủng (một mỗi chương C12–19) · boss (2 → 4 pha, song boss; tối đa 2 cơ chế cùng lúc) · mật độ bầy (20 → 220 quái lúc đỉnh) · luật Hắc Vụ (một mỗi chương C20–25, luôn báo trước).
- **Không phải đòn bẩy:** W của loài, tốc gõ (chữ co theo tốc đo được, nhịp giãn theo k_E), máu thô (đi theo g(c)), **số W gõ mỗi phút** (tải giữ trong dải 00 §4.4).
- **Bot kiểm từng ải:** bảng cổng duy nhất ở **00 §7** (G1–G22).

## 7. Model: dùng lại và làm mới

### 7.1 Dùng lại từ Space Typing

| Nguồn | Dùng làm | Ghi chú |
|---|---|---|
| `heroes/draconis-v3` | B19 Hắc Long (clip Spit, Spit_Big) | Đổi vật liệu bằng mã, không sửa lưới. Dùng bản medium |
| `bosses/lieutenant-nature` (bọ sáu chân) | B13 Bọ Hung Sấm, bay lơ lửng bằng `Boss_Idle_Hover` | Có Hit, Death, Intro. Đòn bằng VFX. Chủ dự án duyệt dáng |
| G02 `alpha-wolf` (model mới) | B04 Song Lang, phóng 1,6 lần, hai màu | Không tốn model riêng |
| `enemies/nature-*`, `shadow-*`, `frost-*` | Hình tạm cho loài bay trong hộp cát dev | Chỉ có Idle, dáng tàu. Không dùng ở bản chủ dự án chơi thử |
| `skills/dragon-fireball` | Đạn lửa khi từ trúng quái | — |
| `kinds.ts`, `skills.ts`, `elite.ts`, `typing-mechanics.ts` | Hành vi gốc, kỹ năng, tinh anh, 5 cơ chế boss | Chép vào kit, không import |

### 7.2 Model mới (Tripo, tổng 63)

**Quái thường chỉ bắt buộc 4 clip:** Idle, Move (Walk, Run, Fly hoặc Crawl), Attack, Death. Trúng đòn dùng phản ứng instanced (mục 1.5, lớp 1); kỹ năng dùng VFX cộng clip Attack tua khác nhịp. Nhờ vậy giảm việc Blender và rủi ro chất lượng. Tướng, boss có bộ clip đầy đủ.

| Nhóm | Số | Loài | Rig Tripo | Clip bắt buộc | Blender làm thêm (chỉ chuyển động, không dựng lưới) |
|---|---|---|---|---|---|
| Hai chân | 9 | E09–E17 | Biped v1.0 | Idle, Walk (Run cho E10, E14), Attack (Slash, Shoot hoặc Throw), Death | Đổi tên `Enemy_*`, khóa gốc |
| Bốn chân | 7 | E18–E24 | Quadruped | Idle, Walk hoặc Run, Attack (cắn, húc, vồ), Death | Cắn, vồ, húc, nhảy cóc (E20), đào (E22) |
| Bay | 8 | E01–E08 | Avian hoặc `build_winged_rig` | Fly, Attack (lao, bắn), Death (rơi) | `make_flight_clips` |
| Bò nhiều chân | 5 | E25, E27, E28, E29, E31 | Hexapod hoặc octopod | Crawl, Attack, Death | Kẹp (E29), đẻ kén (E31) |
| Rắn | 1 | E30 | Serpentine | Slither, Attack (quấn), Death, Dive | — |
| Không rig | 2 | E26, E32 | Không | — (nảy, phồng, xẹp bằng shader) | — |
| Đội trưởng | 8 | G01–G08 | Theo dáng | Idle, Move, Attack, Cast, Hit, Death, Intro (bảng 3.4) | Như nhóm dáng |
| Thống lĩnh | 6 | G09–G14 | Theo dáng; G09 người cưỡi heo là một model | Như Đội trưởng, thêm Stagger | Như nhóm dáng |
| Boss | 17 | B01–B20 trừ B04, B13, B19 | Theo dáng | Intro, Idle, Move, Attack_A, Attack_B, Cast, Stagger, Phase, Hit, Death | Nhiều nhất; B20 phần lớn là VFX |

- Quái thường, bầy và mảnh tách vẽ bằng **đám đông có xương** (texture xương instanced). Chỉ Rồng, tướng, boss dùng `SkinnedMesh` (05 §8).
- Cần `ModelKind` mới (`units`) bắt buộc có clip Idle, Move, Attack, Death.
- Ước tính theo giá API: khoảng 75 credit mỗi model (rig 25 + 5 clip) → khoảng 4.700 credit cho 63 model. Gói web có thể khác. Hỏi chủ dự án số giờ Tripo mỗi tuần (DESIGN.md §11).
- **Thứ tự làm (DESIGN.md §7, §9):**
  1. **Mẫu duyệt hoạt ảnh:** E09 (hai chân), E18 (bốn chân), E01 (bay). Chủ dự án duyệt dáng, rig, 4 clip trước khi đặt lô lớn.
  2. **Bản thử dọc M0:** thêm E11, E19, E25 và G01 (7 model).
  3. **Lát C1–3:** thêm E02, E10, E12, E13, G02, B01–B03 (tổng 14 cho C1–3).
  4. Sau đó mỗi lát 3 chương.

## 8. Câu hỏi cho chủ dự án (đã có mặc định)

1. Phe "Bầy Héo" (vỏ Héo xám tro, nứt vàng úa) do sương "Hắc Vụ" gây ra, giữa bản đồ là "Bệ Rồng", tên Việt của quái như trên? **Mặc định:** giữ (00 D02). Anh duyệt hai ảnh thử E09 trước khi làm ảnh quái hàng loạt. Đổi tên tùy ý, luật không đổi.
2. Quái chết thì "sương tan, thú hiền lại", không có máu? **Mặc định:** có, hợp game học cho mọi lứa tuổi.
3. Chữ thì thầm (Hồn Sương, từ C7), boss Hỏi nghĩa và Nghe có thể khó với người mới. **Mặc định:** bật, có gợi ý IPA và chữ đầu; có tùy chọn trợ năng "luôn hiện chữ".
4. Nguyền Chuẩn (phím sai làm quái hồi máu). **Mặc định:** chỉ từ C12, chỉ ở Phù Thủy và boss; tắt ở mức Dễ.
5. Dùng `draconis-v3` đổi màu làm Hắc Long và `lieutenant-nature` làm Bọ Hung Sấm? **Mặc định:** có, sau khi anh xem ảnh chụp 3 góc.
6. Ngân sách Tripo khoảng 4.700 credit cho 63 model. **Mặc định:** làm theo lát, 14 model cho C1–3 trước, đo chất lượng rồi mới làm tiếp.
7. C20–25 dùng song boss Hắc Hóa thay vì 6 boss mới. **Mặc định:** song boss. Nếu muốn boss mới thì thêm 6 model.
