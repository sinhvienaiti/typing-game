# Tầm đánh của chiêu, phần 1: đo hiện trạng (03/11/2026, đêm)

**Câu của anh (03/11, đêm):** "skill hiện tại phạm vi nó vẫn quá bé, nó cần được rộng hơn hoặc nhiều hướng hơn chứ bé như này, quái tấn công dồn dập với số lượng đông thì thua mất".

Phần 1 chỉ đo, chưa đề xuất số mới. Nó trả lời bốn câu:
1. Mỗi chiêu hôm nay trúng vùng nào, bao nhiêu con, tốn gì.
2. Triều thú đông và nhanh tới đâu.
3. Tốc hạ thú của người chơi so với tốc thú tới, ở 30, 45, 60, 80 WPM với độ chính xác 90 % và 97 %: gãy ở đâu.
4. Vùng trúng thật của từng chiêu, vẽ trên khung camera chơi lúc triều đông nhất.

Phần 2 (sau khi anh đọc) mới đề xuất tầm, hướng và số.

**Phạm vi đo:**
- Mã game ở HEAD `c5267d0` của `games/immortality-cultivation`; lab chiêu chạy trên máy chủ riêng không HMR, dựng từ bản sao `git archive` của HEAD đó.
- Bài đo chỉ đọc mã, chạy bot và lab. Không sửa `src`, `scripts`, `tests`, docs của game.
- Đường dẫn file dưới đây tính từ `games/immortality-cultivation/`.
- Mọi số ở K0, preset Cân bằng; 1 W = 90 máu.

## 0. Kết luận chính

1. **Chiêu với tới quá ngắn so với đường thú đi.**
   - Người chơi đứng trên Tâm nhãn, 3 m sau Trận Tâm. Mọi tầm tính từ người chơi: Phi Kiếm 10 m, ô 1 12 m, ô 2 14 m, tâm ô 4 trong 12 m, tâm tuyệt kỹ trong 14 m.
   - Đường thú từ cổng tới mép Trận Tâm dài 21,8 m. Thú đi **65 % quãng đường ngoài tầm ô 1** và 74 % ngoài tầm Phi Kiếm.
   - Thời gian để hạ một con trong tầm ô 1 chỉ 5,2 s (Thạch Thử) tới 6,4 s (Phong Lang). Hỏa Nha bay chỉ còn 2,8 s.
   - Trong 42–49 % số giây của đợt, có thú sống nhưng không con nào trong 12 m: người chơi ngồi chờ, rồi phải dọn tất cả trong vài giây cuối.
2. **Chiêu vùng trúng ít thú.**
   - Đo trên bot: ô 2 trúng trung bình 2,0 con mỗi lần, ô 4 trúng 4,6 con mỗi lần tung (hạ 2,8), tuyệt kỹ trúng 3,9 con mỗi loạt.
   - Trong khi đó, lúc đỉnh đợt 5–6 có trung bình 25–44 con sống (nhiều nhất 52).
   - Diện tích: ô 2 phủ 1,6 % sân, ô 4 phủ 2,7 %, tuyệt kỹ 10,9 %.
3. **Gãy ngay khi mở cổng thứ hai.**
   - Đợt 1 chỉ có cổng A: 5–8 % thú lọt tới Trận Tâm, Trận Lực mất 2–4 %.
   - Đợt 2 có cả A và B: 10–17 % thú lọt, Trận Lực mất 21–31 % chỉ trong một đợt (8 hồ sơ của đề bài).
   - Mỗi chiêu nhắm một điểm hoặc một hướng, còn hai cổng cách nhau 30 m, chỉ gặp nhau trong khoảng 10 m quanh Trận Tâm.
4. **Kết quả 340 trận bot (17 hồ sơ × 20 seed):**
   - Gần như mọi hồ sơ thua. Hồ sơ khá nhất là 80 WPM 97 %, thắng 40 %; Nhanh thắng 10 %, Khá 5 %, 30 WPM 97 % thắng 5 %; mọi hồ sơ khác 0 %.
   - Đa số thua ở đợt 5–6. P = 67–83 % (đích 15–35 %), Q = 72–95 % (đích 50–70 %), S trung vị 0.
   - Cổng chung trượt: B1, B3, CB3. Đạt: B2, B5, CB1, CB2.
5. **Gõ nhanh hơn không cứu được.**
   - Từ 30 WPM 90 % lên 80 WPM 97 %, tốc hạ chỉ tăng từ 0,81 lên 1,14 con/s (+41 %).
   - Nhịp k nén triều thêm 54 % (k từ 0,85 lên 1,30).
   - Lý do: chiêu bị chặn bởi tầm và hồi chiêu, không phải bởi tốc gõ.
6. **Sức ra đòn thật chỉ bằng 57 % số đợt được thiết kế.**
   - Bot Chuẩn ra 43 W mỗi phút đánh. Đợt được tính theo D_ref thử 75 W/phút (`rules.ts:248`, `measured: false` ở `rules.ts:247`).
   - Ba chiêu vùng chỉ đạt khoảng nửa số canon ước: ô 2 ra 8,5 W/phút (canon ước ~18), ô 4 6,5 (~11), tuyệt kỹ 4,7 (~8). Phi Kiếm còn thấp hơn: 3,7 (~12).
7. **Thử trong bộ nhớ (không phải đề xuất):**
   - Chỉ tăng tầm ×1,5, hoặc chỉ đứng lên trước 9 m: 45 WPM 97 % từ thắng 0 % lên 95–100 %, P 69 % → 34–37 %.
   - Chỉ tăng diện tích chiêu vùng ×2: thắng 25 %.
   - Thiếu tầm là nguyên nhân chính. Diện tích không đủ vì mỗi lần tung có trần sát thương cố định.

## 1. Dấu chân từng chiêu

### 1.1 Luật trong sim (cái quyết định thắng thua)

Sân 40 × 26 m = 1 040 m². "Vùng tầm" là nơi chiêu được phép nhắm tới, không phải vùng trúng.

| Phím lab | Chiêu (ô) | Hình, cỡ | Diện tích (% sân) | Tối đa thú mỗi lần | Đòn mỗi lần | Sát thương mỗi đòn | Giá gõ | Hồi / tài nguyên | Cách nhắm | Số nằm ở |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Phi Kiếm (đánh nền) | 1 mục tiêu, tầm 10 m | vùng tầm 314 m² (30 %); trúng 1 con | 1 | 1 kiếm, chạm +18 tick | 0,25 W = 23 máu vật lý; Thiết Giáp Trư (giáp G2, −55 %) còn 10 | không | 1,2 s | thú mềm, nếu không thì thú gần Trận Tâm nhất trong 10 m quanh người chơi | `src/content/data/school-kiem.ts:42`, `src/local/auto.ts:21-35`, `src/sim/combat.ts:304` |
| 1 | Ngự Kiếm Quyết (ô 1) | 3 kiếm đơn mục tiêu, tầm 12 m; mỗi kiếm xuyên 1 thú nhỏ trong 1,5 m quanh con trúng | vùng tầm 452 m² (43 %); điểm trúng 7 m² mỗi kiếm | 6 (3 + 3 xuyên) | 3 kiếm ở +6, +36, +66 tick | một từ = 100 máu × M_q chia 33/33/34; xuyên 50 % (17) | từ 3–5 chữ, nhóm thuộc hoặc đến hạn | 0 s; tối đa 2 băng chờ, mỗi băng 66 tick, nên ≤ 0,91 từ/s | mỗi kiếm chọn lúc bay: thú mềm, nếu không thì thú gần Trận Tâm nhất trong 12 m | `school-kiem.ts:52-53`, `src/sim/skills.ts:104-140`, `skills.ts:239-279`, `src/content/rules.ts:105` |
| 2 | Nhất Tuyến Xuyên Vân (ô 2) | đường thẳng 14 × 1,2 m, gốc ở người chơi | 16,8 m² (1,6 %) | không trần | 1, chạm +12 tick | 2,5 W = 225 máu con đầu, rồi 191, 158, 124, sàn 90 (−15 % mỗi con); Thế −20 | từ 4–7 chữ, nhóm đang học hoặc đến hạn | 8 s | hướng về thú mềm hoặc thú gần Trận Tâm nhất trong 14 m | `school-kiem.ts:63`, `skills.ts:142-160`, `skills.ts:281-316`, `rules.ts:106` |
| 3 | Hồi Kiếm Hộ Thân (ô 3) | vòng đỡ r 2 m tại chỗ đứng | 12,6 m² (1,2 %) | 0 (không gây sát thương) | đỡ 3 đòn trong 5 s | không | từ 3–5 chữ thuộc | 15 s | chỗ đứng | `school-kiem.ts:73`, `rules.ts:107` |
| 4 | Lưu Quang Bộ (ô 3, thay Hộ thân) | lướt 5 m | không | 0 | không | không | từ 3–5 chữ | 8 s | hướng đi hoặc con trỏ | `school-kiem.ts:83`, `rules.ts:113` |
| 5 | Lạc Kiếm Trận (ô 4) | vòng r 3 m giữ 5 s; tâm trong 12 m | 28,3 m² (2,7 %) | không trần, nhưng cả lần tung chỉ được 4 W | 10 nhịp, mỗi nhịp 0,5 s, mở ở +12 | 0,15 W = 14 máu mỗi nhịp mỗi con; chậm 20 %; **trần 4 W = 360 máu cho cả lần tung**; mỗi nhịp lấy tối đa 60 % máu một cụm bầy | từ 4–7 chữ, nhóm mới hoặc đang học | 12 s | con trỏ, nếu không thì cụm có **tổng W** lớn nhất trong 12 m | `school-kiem.ts:93`, `skills.ts:162-174`, `skills.ts:318-385`, `src/sim/targeting.ts:125` |
| 6 | Thiên Hà Kiếm Vũ (ô 5, tuyệt kỹ) | vòng r 6 m; tâm trong 14 m | 113 m² (10,9 %) | không trần (chia đều) | 3 loạt ở +30, +75, +120 | 10 W = 900 máu **chia đều**: mỗi loạt 300 máu chia cho số thú trong vòng, mỗi con ≤ 75 máu (0,83 W) một loạt; Thế −40; trần cụm 60 % | từ 5–8 chữ, nhóm đến hạn hoặc yếu | 100 Chân Nguyên: +5 mỗi từ sạch, +3 nếu có lỗi, nhân 1/k; khoảng 20–26 từ | con trỏ, nếu không thì cụm có tổng W lớn nhất trong 14 m | `school-kiem.ts:103`, `skills.ts:176-193`, `skills.ts:339-356`, `rules.ts:109`, `rules.ts:191` |
| 7 | Vạn Kiếm Triều Tông (mẫu cả sân, **chỉ có ở lab**) | cả sân, tự săn | 1 040 m² (100 %) | mọi thú | ~140 lần kiếm lao trong 2,3 s, rồi một nhát kết | số tạm của lab: 0,35 W mỗi đòn, nhát kết 1,5 W | (lab bấm phím) | (chưa có) | xếp hạng theo gần Trận Tâm, tinh anh, gần người chơi | `src/view/skills/myriad-swords.ts:138-147` (săn từ tick 30 tới 168, mỗi 0,1 s một loạt 5–7 kiếm), `src/lab/skills-main.ts:475`, `:521` |

**Luật chung của sát thương** (`src/sim/combat.ts`):
- Hệ số chất lượng từ M_q (`rules.ts:176`): Chớp 1,25 · Hoàn hảo 1,10 · Tốt 1,00 · Vừa 0,90 · Ẩu 0,60.
- Đòn gõ bỏ qua giáp.
- Một đòn vùng lấy tối đa 60 % máu một cụm bầy (`rules.ts:209`).
- Kiếm đến khi thú đã chết thì chuyển sang thú gần nhất trong 4 m, còn 50 % (`rules.ts:211`).
- Kiếm Tâm: từ Chớp ở ô 1 thêm 1 kiếm mang 1/3 từ, tối đa mỗi 3 s.
- Thú M0a đều vô hệ, nên khắc chế không đổi gì.

**Máu thú để so** (`src/content/data/beasts.ts`): Thạch Thử 30 máu, nên một kiếm ô 1 (33) hạ được một con. Phong Lang 90 máu: cần cả ba kiếm của một từ.

### 1.2 Lab vẽ khác luật sim ở đâu

| Phím | Lab vẽ và đánh | Sim tính thật | Hệ quả |
|---|---|---|---|
| 0 | thú gần **người chơi** nhất trong 10 m (`src/view/skills/sword-skills.ts:1422`) | thú gần **Trận Tâm** nhất trong 10 m | lab và game chọn hai con khác nhau |
| 1 | thú gần người chơi trong 12 m; xuyên tới **3 m** (`sword-skills.ts:1458-1465`) | gần Trận Tâm; xuyên **1,5 m** | vùng xuyên của lab rộng gấp 4 lần diện tích |
| 2 | dải rộng **2,0 m** (nửa rộng 0,6 m cộng 0,4 m thân thú, `sword-skills.ts:3675`); hướng về điểm cố định (0,2; −12) (`skills-main.ts:906`) | rộng 1,2 m tính theo tâm thú; hướng về thú gần Trận Tâm | lab trúng rộng gần gấp đôi |
| 5 | vòng **3,2 m** (`sword-skills.ts:4072`) ở điểm cố định (−5; −7) | 3,0 m ở cụm W lớn nhất trong 12 m | lệch nhỏ |
| 6 | 6 kiếm dẫn r 2,6 m trên con mồi nặng nhất, 3 đợt × 48 kiếm r 1,9 m (nửa rơi vào thú, nửa rơi theo lưới) trong khung **36 × 17 m** (`sword-skills.ts:282`, `:4283`, `:4409-4452`), thêm kiếm khổng lồ và xoáy hút; số hiện 2,0 W mỗi đòn (`skills-main.ts:475`) | **một** vòng r 6 m; mỗi con ≤ 0,83 W mỗi loạt | lab hứa gần cả sân (612 m², 59 %), sim chỉ 113 m² (10,9 %); số của lab cao gấp 2,4 lần trần của sim |
| 7 | cả sân (`myriad-swords.ts:158` và `:1719`: nhát kết trúng mọi thú cách đường chém tới 18,5 m) | không có | anh đã thấy "cả sân" ở phím 6 và 7, nhưng game chỉ có vòng 6 m |

## 2. Mối đe dọa: triều thú

### 2.1 Sân, đường đi và tầm với

- **Sân:** Thanh Thạch Ải 40 × 26 m, Trận Tâm ở (0; 0), Kết Giới r 9 m (254 m², 24 % sân) (`rules.ts:279-321`).
- **Cổng:** A ở (−15; −18), B ở (15; −18), cách Trận Tâm 23,4 m và cách người chơi 25,8 m.
- **Đường trời:** vào từ hai góc (±20; −18), dài 26,9 m theo đường thẳng.
- **Đường đất** theo trường dòng chảy: 21,8 m từ cổng tới mép Trận Tâm (mép r 2 m), đo bằng `routeU`.
- **Người chơi** bắt đầu và đứng trên Tâm nhãn (0; +3) (`src/content/data/stage-m0a.ts:55`, `src/local/player.ts:16-17`). Bot dùng chính sách Đứng yên theo canon §18.3.
- **Vòng tầm cắt đường thú** (đi thẳng từ cổng về Trận Tâm):

| Chiêu | Tầm từ người chơi | Thú vào tầm khi còn cách Trận Tâm | Phần đường đi ngoài tầm |
|---|---|---|---|
| Phi Kiếm | 10 m | 7,5 m | 74 % |
| Ô 1 | 12 m | 9,5 m | 65 % |
| Ô 2 | 14 m | 11,6 m | 55 % |
| Ô 4 (tâm trong 12 m, cộng r 3 m) | 15 m | 12,6 m | 51 % |
| Tuyệt kỹ (tâm trong 14 m, cộng r 6 m) | 20 m | 17,6 m | 27 % |

**Vòng 12 m của ô 1 gần trùng Kết Giới 9 m.** Ô 1 chỉ chạm được thú khi thú đã vào Kết Giới.

### 2.2 Thú

Thời gian dưới đây là trung vị, đo trong sim khi không ai giết thú, k = 1 (`tmp/skill-reach/travel.ts`). "Còn trong tầm" là số giây từ khi thú vào tầm tới khi tới mép Trận Tâm hoặc chỗ dừng: đó là cửa sổ để hạ nó.

| Thú | Bậc | W | Máu | Tốc (m/s) | Đường | Tới mép hoặc chỗ dừng | Còn trong tầm 10 / 12 / 14 / 15 / 20 m |
|---|---|---|---|---|---|---|---|
| Thạch Thử | bầy, cụm 7 con | 0,33 | 30 | 1,6 | A, B | 13,9 s | 3,8 / 5,2 / 6,5 / 7,3 / 10,6 s |
| Phong Lang | nhỏ, bầy 3–5 | 1,0 | 90 | 1,4 | A, B | 15,8 s | 4,3–4,8 / 6,0–6,4 / 7,5–7,8 / 8,3–8,5 / 12,1 s |
| Hỏa Nha | nhỏ, bay, 2 con | 0,8 | 72 | 2,0 | trời | 11,1 s | 1,6 / 2,8 / 3,8 / 4,3 / 6,8 s |
| Nham Viên | vừa, ném đá | 2,0 | 180 | 1,0 | A, B | 12,6 s tới chỗ dừng (11 m cách đích) | 0 / 0 / 0,4 / 1,4 / 6,8 s |
| Thiết Giáp Trư | vừa, giáp G2 | 3,0 | 270 | 1,0 | A, B | 15 s tới điểm húc (10 m) | 0 / 0 / 2,8 / 3,9 / 9,2 s |
| Lang Đầu Đàn | tướng | 7,0 | 630 | 1,4 | A hoặc B | 17,7 s | 4,3 / 6,0 / 7,5 / 8,3 / 12,0 s |

- **Cắn mỗi giây ở mép Trận Tâm:** bầy 1, nhỏ 2, vừa 4 Trận Lực (`rules.ts:452`). Trận Lực solo là 1 000 (`rules.ts:315`).
- **Nham Viên và Thiết Giáp Trư dừng ngoài 12 m quanh người chơi.** Nham Viên đứng ném cách đích 11 m (`beasts.ts:100`). Con nhắm Trận Tâm đứng cách người chơi 11–14 m.
  - Ghi chú trong mã nói "đứng 11 m để ô 1 với tới **từ Trận Tâm**", nhưng người chơi đứng ở Tâm nhãn, 3 m sau đó.
  - Vì vậy Phi Kiếm không với tới chúng, ô 1 thường cũng không.
- **Giáp G2 của Thiết Giáp Trư** giảm 55 % đòn vật lý: Phi Kiếm và Kiếm Thung.

### 2.3 Đợt

Số dưới đây ở k = 1 (`src/content/data/waves.ts:63-209`, canon §13.3). Với người chơi có nhịp k, nhân tốc tới với k: k = 0,85 ở 30 WPM 90 %, lên tới 1,30 từ khoảng 55 WPM.

| Đợt | Dài | Số con (A / B / trời) | Con/s | Máu đợt | W/s | 8 s đông nhất | Phần đường trời |
|---|---|---|---|---|---|---|---|
| 1 | 40 s | 45 (45 / 0 / 0) | 1,13 | 30 W | 0,75 | 14 con (1,75/s) | 0 % |
| 2 | 45 s | 57 (26 / 31 / 0) | 1,27 | 42 W | 0,93 | 19 (2,38/s) | 0 % |
| 3 | 50 s | 71 (38 / 25 / 8) | 1,42 | 53 W | 1,06 | 20 (2,50/s) | 11 % |
| 4 | 55 s | 73 + ≤ 6 gọi (37 / 30 / 6) | 1,33 | 64 W | 1,16 | 21 (2,63/s) | 8 % |
| 5 | 55 s | 92 (47 / 39 / 6) | 1,67 | 68,6 W | 1,25 | 23 (2,88/s) | 7 % |
| 6 | 60 s | 107 + ≤ 6 gọi (54 / 45 / 8) | 1,78 | 84,6 W | 1,41 | 27 (3,38/s) | 7 % |

- **Đường trời** mang 28/445 con cả ải (6 %). Hỏa Nha bay thẳng từ hai góc sân, nên đường trời là thêm **hai hướng** nữa.
- **Máu đợt mỗi phút** ở k = 1: 45, 56, 64, 70, 75, 85 W. So với sức ra đòn đo được ở mục 3: bot Chuẩn ra 43 W mỗi phút đánh.
- **Cột máu đợt lấy theo canon §13.3**, đã gồm tinh anh và phần gọi tối đa. Cộng thẳng từ `waves.ts` (tinh anh ×1,6, chưa có phần gọi) ra 29,2 / 41,5 / 53,7 / 58,0 / 66,6 / 78,4 W. Phần chênh là Thiết Bì +2 W (`elites.ts:11`) và tối đa 6 W gọi ở đợt 4, 6.

### 2.4 Bao nhiêu con sống cùng lúc, mật độ

**Số con sống lúc đỉnh mỗi đợt.** Đo trên bot, trung bình 20 seed, trong ngoặc là lớn nhất. Đây là số "sống cùng lúc" thật, vì nó đã tính phần người chơi kịp hạ.

| Hồ sơ | Đợt 1 | Đợt 2 | Đợt 3 | Đợt 4 | Đợt 5 | Đợt 6 |
|---|---|---|---|---|---|---|
| 30 WPM 97 % | 16 (20) | 21 (22) | 24 (27) | 22 (32) | 27 (37) | 31 (40) |
| 45 WPM 97 % | 20 (21) | 23 (26) | 25 (30) | 24 (34) | 31 (38) | 34 (41) |
| 60 WPM 97 % | 22 (23) | 23 (25) | 26 (30) | 29 (39) | 31 (36) | 41 (47) |
| 80 WPM 97 % | 22 (23) | 23 (25) | 25 (27) | 28 (37) | 30 (35) | 39 (46) |
| Chuẩn (35 WPM 95 %) | 19 (22) | 22 (25) | 24 (28) | 24 (30) | 29 (39) | 33 (38) |

- **Đỉnh riêng từng đường ở đợt 6** (45 WPM 97 %): cổng A 19 con, cổng B 16, trời 3.
- **Trong Kết Giới cùng lúc nhiều nhất:** 6, 9, 12, 8, 15, 15 con (đợt 1 tới 6).
- **Mật độ quanh mỗi thú lúc đỉnh** (ảnh chụp sim, 5 hồ sơ):
  - trung bình 3,3–4,4 con khác trong 1,5 m (khoảng 0,5–0,6 con/m²);
  - 5,5–6,7 con trong 3 m (khoảng 0,2 con/m²);
  - 7–13 con trong 6 m (0,06–0,11 con/m²).
- **Lúc sinh ra:** cụm Thạch Thử 7 con trong ±0,8 m (khoảng 2,7 con/m²), bầy Phong Lang trong ±1,2 m (`rules.ts:308-309`).
- **Khoảng cách giữa các toán:** luật cổng cho mỗi cổng một toán mỗi 1,5 s (`rules.ts:495`). Các toán nối nhau trên một đường cách khoảng 2–5 m.
- **Thú trong tầm ô 1 theo thời gian** (seed 1, mọi giây của đợt):
  - chỉ 15–22 % số thú sống nằm trong 12 m quanh người chơi;
  - 42–49 % số giây có thú sống mà không con nào trong 12 m (Chuẩn 181/428 s, 45 WPM 97 % 189/412 s, 80 WPM 97 % 145/298 s).

## 3. Tốc hạ so với tốc tới

### 3.1 Cách đo

**`pnpm ic:balance` chưa chạy được.** `scripts/balance/run.ts` của làn 7 vẫn là chỗ trống (in `TODO(lane-7)` rồi thoát). Bài này viết một bot đo riêng, để ngoài Git: `tmp/skill-reach/bot.ts`.

Bot chơi đúng đường của trang game:
- **Lõi trận:** `createMatchRunner` của `src/app/match.ts`, sim và lớp `local` thật.
- **Cách gõ:** `HumanTypist` của kit (nhận từ theo độ quen, lỗi theo a, độ đều CV, chú ý giảm khi đông, mệt).
- **Thứ tự chọn ô** theo canon §18.3: Tẩy → Ấn → ô 5 → ô 2 → ô 4 → ô 3 → ô 1.
  - Hộ thân chỉ dùng khi có đòn đang báo.
  - Chiến thuật Vừa đôi khi bỏ một ô đã sẵn 1–2 s.
  - Bot chỉ gõ một chiêu khi có thú trong tầm của nó.
- **Vị trí:** Đứng yên trên Tâm nhãn; nhắm đất để sim tự chọn cụm.
- **Mua sắm:** Kiếm Thung ở dải 1 lúc chuẩn bị; mỗi lần nghỉ mua theo thứ tự dải 2, Lôi Phù Trụ, Phong Ấn Võng, rồi nâng cấp.
- **Trận:** bộ điều nhịp bật, preset Cân bằng, bộ từ khởi đầu lạnh (40 từ nền và 8 từ mới, như `buildDeck` dựng cho người mới).
- **Ma trận:** 17 hồ sơ × 20 seed = 340 trận, mỗi trận khoảng 0,2 s. Có 8 hồ sơ theo đề bài và 9 bot chuẩn của BALANCE §6.
- **Kiểm lại:** cả ma trận (cả các biến thể ở mục 5.6) chạy lại lúc 23:35 ngày 03/11 vào một thư mục riêng. Cả 520 file kết quả trùng từng byte với lần đầu: sim tất định, HEAD vẫn là `c5267d0`, và các commit trong ngày 03/11 chỉ đổi `src/view`, `src/lab`, `scripts`, `tests` và docs, không đụng luật.

### 3.2 Mỗi chiêu hạ được bao nhiêu thú mỗi giây

Đo trên mọi giây đánh (đợt, lặng, Vương) của 20 seed. Cách đọc ô:
- ô 1: "từ/phút · con hạ/s";
- ô 2 và ô 4: "lần tung/phút · con trúng mỗi lần · con hạ/s";
- tuyệt kỹ: "lần/phút · con trúng mỗi loạt · con hạ/s";
- Phi Kiếm: "phát/phút · con hạ/s".

| Hồ sơ | k | Từ/phút | Ô 1 | Ô 2 | Ô 4 | Tuyệt kỹ | Phi Kiếm | Tổng con hạ/s | W/phút |
|---|---|---|---|---|---|---|---|---|---|
| 30 WPM 90 % | 0,85 | 22,3 | 9,3 · 0,33 | 4,7 · 2,0 · 0,14 | 2,9 · 4,3 · 0,12 | 1,0 · 3,6 · 0,08 | 23 · 0,14 | 0,81 | 36 |
| 30 WPM 97 % | 0,89 | 25,2 | 11,1 · 0,40 | 4,8 · 1,9 · 0,14 | 3,0 · 4,4 · 0,13 | 1,2 · 3,8 · 0,10 | 22 · 0,13 | 0,90 | 40 |
| 45 WPM 90 % | 1,04 | 27,8 | 13,5 · 0,45 | 4,9 · 2,0 · 0,14 | 3,1 · 4,9 · 0,15 | 1,0 · 4,4 · 0,09 | 22 · 0,12 | 0,95 | 42 |
| 45 WPM 97 % | 1,09 | 30,6 | 15,2 · 0,54 | 5,0 · 2,0 · 0,15 | 3,3 · 4,7 · 0,15 | 1,2 · 3,8 · 0,10 | 20 · 0,10 | 1,05 | 46 |
| 60 WPM 90 % | 1,30 | 33,4 | 17,8 · 0,59 | 5,1 · 2,1 · 0,16 | 3,4 · 5,2 · 0,18 | 1,0 · 5,0 · 0,10 | 21 · 0,11 | 1,14 | 51 |
| 60 WPM 97 % | 1,30 | 35,5 | 19,0 · 0,64 | 5,2 · 2,0 · 0,16 | 3,4 · 5,0 · 0,16 | 1,1 · 4,0 · 0,10 | 18 · 0,09 | 1,15 | 52 |
| 80 WPM 90 % | 1,30 | 35,1 | 19,0 · 0,63 | 5,3 · 2,0 · 0,16 | 3,3 · 5,0 · 0,16 | 1,1 · 4,4 · 0,09 | 19 · 0,09 | 1,14 | 50 |
| 80 WPM 97 % | 1,30 | 38,6 | 20,9 · 0,66 | 5,1 · 2,0 · 0,15 | 3,4 · 4,5 · 0,15 | 1,3 · 3,9 · 0,10 | 18 · 0,08 | 1,14 | 56 |

- **Ô 1 gánh 41–58 % số thú hạ.** Ô 1 chiếm 39–52 % sát thương gõ, quá trần 30 % của CB3.
- **Ba chiêu vùng cộng lại chỉ hạ 0,34–0,44 con/s.**
- **Chiêu vùng không lớn lên theo tốc gõ:** ô 2 đứng ở ~5 lần/phút (hồi 8 s), ô 4 ~3,3 lần/phút (hồi 12 s), tuyệt kỹ ~1,1 lần/phút (Chân Nguyên). Số con trúng mỗi lần đứng ở 2, 4,5 và 4.
- **Ô 1 không bị chặn bởi trần băng** (tối đa 54 từ/phút) mà bởi tầm: mỗi trận có 5–7 lần ô 1 tắt vì 3 s không có thú trong 12 m.

**Sức ra đòn đo được so với ước của canon** (bot Chuẩn, W mỗi phút đánh, canon ước trong ngoặc, `rules.ts:251`): ô 1 15,4 (10) · ô 2 8,5 (18) · ô 4 6,5 (11) · tuyệt kỹ 4,7 (8) · Phi Kiếm 3,7 (12) · cơ quan 4,5 (hỗ trợ 16). Tổng 43 W/phút, canon ước 75.

### 3.3 Từng đợt: tốc tới theo kế hoạch so với tốc hạ đo được

Mỗi ô ghi bốn số:
1. Tốc tới theo kế hoạch ở k của hồ sơ / tốc hạ đo được (con/s).
2. Thời gian đợt kéo dài quá kế hoạch.
3. Phần thú lọt tới Trận Tâm (cắn, ném, bổ nhào, húc).
4. Trận Lực mất trong đợt.

Bộ điều nhịp có thể giãn khoảng sinh tối đa ±15 %. Đợt 5 và 6 chỉ tính các seed còn sống tới đó; đợt thua tính tới lúc thua.

| Hồ sơ | Đợt 1 | Đợt 2 | Đợt 3 | Đợt 4 | Đợt 5 | Đợt 6 |
|---|---|---|---|---|---|---|
| 30 WPM 90 % | 0,95 / 0,75 · +13 s · 8 % · −4 % | 1,07 / 0,76 · +23 s · 17 % · −29 % | 1,20 / 0,86 · +24 s · 33 % · −30 % | 1,12 / 0,79 · +34 s · 27 % · −37 % | 1,42 / 0,93 · 28 % · −23 % | 1,51 / 1,18 · 31 % · −19 % |
| 30 WPM 97 % | 1,00 / 0,79 · +12 s · 5 % · −4 % | 1,12 / 0,82 · +19 s · 12 % · −24 % | 1,26 / 0,91 · +22 s · 19 % · −27 % | 1,18 / 0,87 · +29 s · 18 % · −26 % | 1,49 / 1,04 · 26 % · −29 % | 1,58 / 1,17 · 20 % · −20 % |
| 45 WPM 90 % | 1,17 / 0,84 · +15 s · 7 % · −4 % | 1,32 / 0,83 · +26 s · 13 % · −31 % | 1,48 / 1,03 · +21 s · 24 % · −26 % | 1,38 / 0,94 · +30 s · 18 % · −26 % | 1,74 / 1,14 · 31 % · −30 % | 1,85 / 1,16 · 22 % · −19 % |
| 45 WPM 97 % | 1,22 / 0,88 · +15 s · 5 % · −4 % | 1,38 / 0,88 · +24 s · 12 % · −28 % | 1,54 / 1,11 · +19 s · 19 % · −24 % | 1,44 / 1,01 · +27 s · 13 % · −22 % | 1,82 / 1,19 · 30 % · −32 % | 1,94 / 1,37 · 15 % · −18 % |
| 60 WPM 90 % | 1,46 / 1,00 · +14 s · 6 % · −2 % | 1,65 / 1,01 · +22 s · 11 % · −21 % | 1,85 / 1,15 · +24 s · 19 % · −27 % | 1,73 / 1,12 · +28 s · 20 % · −26 % | 2,17 / 1,35 · 31 % · −39 % | 2,32 / 1,48 · 13 % · −13 % |
| 60 WPM 97 % | 1,46 / 1,00 · +15 s · 6 % · −2 % | 1,65 / 0,99 · +23 s · 11 % · −22 % | 1,85 / 1,13 · +25 s · 12 % · −27 % | 1,73 / 1,16 · +26 s · 15 % · −23 % | 2,17 / 1,37 · 30 % · −34 % | 2,32 / 1,56 · 10 % · −19 % |
| 80 WPM 90 % | 1,46 / 1,01 · +14 s · 6 % · −2 % | 1,65 / 0,97 · +24 s · 11 % · −23 % | 1,85 / 1,13 · +25 s · 14 % · −27 % | 1,73 / 1,13 · +27 s · 16 % · −24 % | 2,17 / 1,31 · 24 % · −33 % | 2,32 / 1,52 · 17 % · −19 % |
| 80 WPM 97 % | 1,46 / 0,99 · +15 s · 6 % · −2 % | 1,65 / 1,00 · +23 s · 10 % · −22 % | 1,85 / 1,23 · +20 s · 10 % · −21 % | 1,73 / 1,18 · +25 s · 11 % · −22 % | 2,17 / 1,36 · 22 % · −29 % | 2,32 / 1,62 · 9 % · −20 % |

**Đường gãy:**
- **Đợt 1 (một cổng):** mọi hồ sơ giữ được. Chỉ 5–8 % thú lọt, Trận Lực mất 2–4 %. Đợt vẫn kéo dài thêm 12–15 s, vì tốc hạ 0,75–1,0 con/s thấp hơn tốc tới 0,95–1,46.
- **Đợt 2 (hai cổng A + B):** gãy ở mọi hồ sơ.
  - 10–17 % thú lọt, Trận Lực mất 21–31 % trong một đợt.
  - Tốc hạ gần như không đổi (0,76–1,01 con/s), trong khi tốc tới tăng lên 1,07–1,65.
- **Đợt 3–5:** mỗi đợt mất 21–39 % Trận Lực. Phần lớn trận thua ở đợt 5 (9 cụm bầy) hoặc 6.
- **Người gõ nhanh không thoát:** 60 WPM 90 % thua ở đợt 5 trong 14/20 seed, nặng hơn 30 WPM 97 % (7/20). Nhịp k 1,30 nén triều thêm 30 %, mà tầm và hồi chiêu không đổi.

### 3.4 Chỉ số chung của BALANCE.md (20 seed mỗi hồ sơ, Cân bằng, bộ điều nhịp bật)

Dải đích Cân bằng (BALANCE §3, dải chung theo canon D15): Thắng 75–90 % · S trung vị 35–65 % · P 15–35 % · I ≤ 10 % · O ≤ 8 % · N 0,3–1 · Q trung vị 50–70 %.

Các cột không có trong dải đích:
- "Phần phe ta" là sát thương không do gõ.
- "Gõ" là phần sát thương gõ (CB2 cần ≥ 55 %).
- "Ô 1/gõ" là phần ô 1 trong sát thương gõ (CB3 cần ≤ 30 %).
- "Phút" là thời lượng trận, tính tới lúc thua.

| Hồ sơ | k | Thắng | S | P | I | O | N | Q | Phe ta | Gõ | Ô 1/gõ | Phút | Thua ở đợt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 30 WPM 90 % | 0,85 | 0 % | 0 % | 74,0 % | 0,6 % | 0 % | 0 | 79 % | 21 % | 80 % | 39 % | 8,0 | 4: 3 · 5: 16 · 6: 1 |
| 30 WPM 97 % | 0,89 | 5 % | 0 % | 71,1 % | 0,7 % | 0 % | 0,05 | 77 % | 20 % | 81 % | 42 % | 9,1 | 4: 1 · 5: 7 · 6: 11 |
| 45 WPM 90 % | 1,04 | 0 % | 0 % | 71,3 % | 0,3 % | 0 % | 0 | 76 % | 19 % | 82 % | 45 % | 7,7 | 5: 17 · 6: 3 |
| 45 WPM 97 % | 1,09 | 0 % | 0 % | 68,8 % | 0,4 % | 0 % | 0 | 75 % | 18 % | 83 % | 48 % | 8,2 | 5: 7 · 6: 13 |
| 60 WPM 90 % | 1,30 | 0 % | 0 % | 71,7 % | 0,2 % | 0 % | 0 | 76 % | 17 % | 84 % | 48 % | 7,1 | 5: 14 · 6: 6 |
| 60 WPM 97 % | 1,30 | 0 % | 0 % | 68,9 % | 0,6 % | 0 % | 0 | 73 % | 16 % | 85 % | 51 % | 7,8 | 5: 7 · 6: 13 |
| 80 WPM 90 % | 1,30 | 0 % | 0 % | 69,9 % | 0,6 % | 0 % | 0 | 74 % | 17 % | 84 % | 51 % | 7,5 | 5: 9 · 6: 11 |
| 80 WPM 97 % | 1,30 | 40 % | 0 % | 67,2 % | 1,2 % | 0 % | 0,40 | 72 % | 15 % | 85 % | 52 % | 8,4 | 5: 3 · 6: 9 |
| Trẻ em (15 WPM 88 %) | 0,75 | 0 % | 0 % | 82,7 % | 0,2 % | 0 % | 0 | 95 % | 30 % | 72 % | 22 % | 5,4 | 3: 15 · 4: 5 |
| Mới (25 WPM 92 %) | 0,75 | 0 % | 0 % | 74,5 % | 0,4 % | 0 % | 0 | 82 % | 23 % | 78 % | 37 % | 8,5 | 4: 5 · 5: 12 · 6: 3 |
| Chậm chắc (25 WPM 99 %) | 0,79 | 0 % | 0 % | 71,4 % | 0,6 % | 0,01 % | 0 | 78 % | 21 % | 80 % | 39 % | 9,9 | 5: 9 · 6: 11 |
| Chuẩn (35 WPM 95 %) | 1,00 | 0 % | 0 % | 72,1 % | 0,3 % | 0 % | 0 | 76 % | 19 % | 81 % | 44 % | 8,5 | 5: 10 · 6: 10 |
| Khá (50 WPM 96 %) | 1,21 | 5 % | 0 % | 69,9 % | 0,6 % | 0 % | 0,05 | 75 % | 17 % | 83 % | 48 % | 8,6 | 5: 2 · 6: 17 |
| Ẩu (50 WPM 85 %) | 1,05 | 0 % | 0 % | 73,0 % | 0,3 % | 0,07 % | 0 | 77 % | 19 % | 82 % | 45 % | 7,5 | 4: 4 · 5: 10 · 6: 6 |
| Nhanh (70 WPM 97 %) | 1,30 | 10 % | 0 % | 68,2 % | 1,3 % | 0 % | 0,10 | 73 % | 16 % | 85 % | 51 % | 8,4 | 5: 2 · 6: 16 |
| Không gõ | — | 0 % | 0 % | 81,6 % | 0 % | 0 % | 0 | 100 % | 100 % | 0 % | 0 % | 1,0 | 1: 20 |
| Chỉ gõ (35 WPM 95 %, không mua) | 1,00 | 0 % | 0 % | 75,4 % | 0,5 % | 0 % | 0 | 79 % | 10 % | 91 % | 42 % | 7,8 | 4: 2 · 5: 13 · 6: 5 |

- **Chia sát thương của bot Chuẩn:** đánh nền 8,4 % (canon §7.3 đích 12–18 %), cơ quan 10,4 %. Trong sát thương gõ: ô 2 24,5 %, ô 4 18,6 %, tuyệt kỹ 13,2 %.
- **Học:** không đo, vì bot không gửi sự kiện học. Các cổng HC không chạy trong bài này.

**Cổng chung:**

| Cổng | Kết quả | Chi tiết |
|---|---|---|
| B1 | **trượt** | Mới → Nhanh: Thắng 0–10 %, S 0 %, P 68–75 %, Q 73–82 %. I và O nằm trong dải |
| B2 | đạt | không bot nào quá dễ |
| B3 | **trượt** | Mới thắng 0 % (cần ≥ 70 %). Trẻ em chạy ở Cân bằng chứ không ở Thư giãn như cổng yêu cầu, nên chưa chấm |
| B4 | không phân định | Chậm chắc và Ẩu cùng S 0. Q của Chuẩn 76 %, của Ẩu 77 %: Chuẩn hạ sớm hơn không đáng kể |
| B5 | đạt | Không gõ thua 20/20 ngay đợt 1 |
| B6–B9 | không chạy | |
| CB1 | đạt | |
| CB2 | đạt | Chuẩn: phần gõ 81 %, seed thấp nhất 79 % |
| CB3 | **trượt** | ô 1 chiếm 37–52 % sát thương gõ ở Mới → Nhanh |
| CB9 | không chấm được | Chuẩn thua mọi seed |

## 4. Bảng dấu chân

**Ảnh:** `games/immortality-cultivation/tmp/shots/skill-reach/footprints.jpg` (1 936 × 2 238, ngoài Git).

**Cách dựng:**
- **Nền:** khung của lab chiêu ở camera chơi (55°, FOV 28°, cả sân), ẩn thú đứng tạm và nhân vật. Chụp từ máy chủ riêng không HMR (HEAD `c5267d0`), 1920 × 1080.
- **Phép chiếu:** dựng lại đúng `fitCamera` của `src/view/renderer.ts` (lề 0,03, chừa 2,5 m trên đầu, không trừ thanh Bàn Quyết). Khoảng cách camera ra 53,509 m, khớp số lab tự báo (53,509 m).
- **Lúc chụp:** đỉnh đợt 6 của bot 45 WPM 97 %, seed 1: 38 con sống, cổng A 19, cổng B 18, trời 1.
- **Vùng trúng** của từng chiêu tính bằng chính hàm của sim tại tick đó: `nearestToHeart`, `densestPoint`, đường 14 × 1,2 m, vòng r 3 m và r 6 m.
- **Màu:** đỏ là thú bị trúng, trắng là không trúng, tam giác xanh là người chơi. Nét vàng đứt là vùng lab vẽ khi khác sim. Vòng trắng chấm là vòng tầm.

**Tám ô trong ảnh:**

| Ô | Cái đọc được |
|---|---|
| Triều lúc đỉnh | 15 con trong 10 m, 19 con trong 12 m; 19 con còn ở phía cổng, ngoài tầm mọi chiêu trừ tuyệt kỹ |
| Phím 0 | trúng 1/38 |
| Phím 1 | trúng 1/38 (con đầu đứng một mình, không có thú nhỏ trong 1,5 m để xuyên) |
| Phím 2 | trúng 4/38; đường bắn từ người chơi lên phía bắc, lệch khoảng 25° so với luồng cổng A, nên chỉ trùng luồng vài mét |
| Phím 3 và 4 | 0 sát thương |
| Phím 5 | trúng 8/38 |
| Phím 6 | trúng 17/38, toàn bộ ở cụm quanh Trận Tâm; khung mưa kiếm của lab phủ 59 % sân |
| Phím 7 | 38/38 nếu thành luật |

## 5. Gãy ở đâu và vì sao

### 5.1 Tầm

- **Mọi tầm tính từ người chơi**, mà người chơi đứng 3 m sau Trận Tâm. Thú đi 21,8 m, nhưng chỉ 5,2–6,4 s cuối nằm trong tầm ô 1, và 3,8–4,8 s cuối trong tầm Phi Kiếm.
- **Không kịp nhân lực gõ.** 42–49 % giây của đợt không có thú nào trong 12 m, nên sức gõ bị bỏ phí. Từ/phút chỉ tăng từ 22 lên 39 khi WPM tăng từ 30 lên 80. Q trung vị 72–82 %: thú chết ở ba phần tư đường, ngay trong Kết Giới.
- **Thú đứng xa bị bỏ sót.** Nham Viên và Thiết Giáp Trư dừng ngoài 12 m nếu nhắm Trận Tâm.
- **Chứng cứ** (mục 5.6): chỉ cần thêm tầm, hoặc chỉ cần đứng lên trước, là thắng 95–100 % ở 45 WPM 97 %.

### 5.2 Hướng

- **Mỗi lần tung đi một hướng hoặc một điểm:**
  - Phi Kiếm và ô 1: một con;
  - ô 2: một đường từ người chơi tới một con;
  - ô 4 và tuyệt kỹ: một vòng ở cụm nặng nhất.
- **Triều tới từ bốn phía** khi cả hai cổng và đường trời mở: hai cổng đất cách nhau 30 m, đường trời vào từ hai góc sân.
- **Gãy đúng lúc cổng B mở (đợt 2).** Phần thú lọt tăng từ 5–8 % lên 10–17 %, Trận Lực mất tăng từ 2–4 % lên 21–31 % mỗi đợt.
- **Ô 2 khó trúng nhiều con.** Gốc đường luôn ở người chơi, nên đường chỉ trùng một đoạn ngắn với luồng thú đi chéo từ cổng. Trung bình chỉ 2,0 con mỗi lần (lớn nhất 6–8).
- **Lúc đỉnh,** tuyệt kỹ trúng 17 con quanh Trận Tâm nhưng 0 con ở hai cổng.

### 5.3 Số mục tiêu và ngân sách mỗi lần tung

- **Ngân sách sát thương của chiêu vùng là cố định**, nên trúng thêm thú không thêm sát thương:
  - ô 4 tối đa 4 W cho cả lần tung;
  - tuyệt kỹ 10 W chia đều, mỗi con ≤ 0,83 W một loạt;
  - ô 2 giảm 15 % mỗi con tới sàn 40 %;
  - mỗi đòn vùng lấy tối đa 60 % máu một cụm bầy.
- **Thử tăng diện tích ×2 trong bộ nhớ** (ô 2 rộng 2,4 m, ô 4 r 6 m, tuyệt kỹ r 12 m): thắng chỉ lên 5–25 % ở 35–45 WPM.
- **"Cụm đặc nhất" tính theo tổng W, không theo số con** (`targeting.ts:125`). Một Thiết Giáp Trư (3 W) thắng một cụm 7 Thạch Thử (2,31 W), nên ô 4 có thể đổ cả 5 s vào một con.
- **Ô 1 là chiêu đơn mục tiêu**, xuyên chỉ 1,5 m. Nó vẫn gánh hơn nửa số thú hạ.

### 5.4 Giá gõ và hồi chiêu

- **Chiêu vùng bắn quá thưa:**
  - ô 2: từ 4–7 chữ, hồi 8 s;
  - ô 4: từ 4–7 chữ thuộc nhóm mới hoặc đang học (nhận từ chậm hơn), hồi 12 s;
  - tuyệt kỹ: từ 5–8 chữ và 20–26 từ để đầy Chân Nguyên.
  - Cộng lại khoảng 9,5 lần tung vùng mỗi phút, hạ 0,34–0,44 con/s.
- **Triều tới nhanh hơn nhiều:** ở k 1–1,30, đợt 6 mang 1,8–2,3 con/s, và 3,4–4,4 con/s trong 8 s đông nhất.
- **Ô 1 không hồi chiêu nhưng không gỡ được thế này:** nó cũng phải chờ thú vào 12 m.

### 5.5 Nhịp k và D_ref

- **Nhịp k nén triều cho người gõ nhanh:** k = 1,30 từ khoảng 55 WPM (`rules.ts:265`). Hồi chiêu tính theo giây, tầm không đổi, nên người gõ nhanh gặp triều đặc hơn 30 % với cùng tầm. Kết quả: 60 WPM thua sớm hơn 30 WPM 97 %.
- **Máu đợt tính theo D_ref thử 75 W/phút**, nhưng bot Chuẩn chỉ ra 43 W mỗi phút đánh. Từ đợt 2, máu đợt mỗi phút (56 W) đã vượt sức ra đòn của người chơi tham chiếu.

### 5.6 Thử trong bộ nhớ (chứng cứ, không phải đề xuất)

Ba biến thể chạy trong chính tiến trình bot, đổi đối tượng số trong bộ nhớ; file của game không đổi:
- **Đứng trước:** đứng ở (0; −6), 9 m trước Tâm nhãn, vẫn trong Kết Giới.
- **Tầm ×1,5:** Phi Kiếm 15 m, ô 1 18 m, ô 2 dài 21 m, tầm ô 4 18 m, tầm tuyệt kỹ 21 m; bán kính giữ nguyên.
- **Diện tích ×2:** ô 2 rộng 2,4 m, ô 4 r 6 m, tuyệt kỹ r 12 m; tầm và trần giữ nguyên.

20 seed mỗi dòng.

| Hồ sơ | Biến thể | Thắng | S | P | I | Q | Đợt 2: thú lọt · Trận Lực | W/phút |
|---|---|---|---|---|---|---|---|---|
| Chuẩn | hiện tại | 0 % | 0 % | 72 % | 0,3 % | 76 % | 14 % · −30 % | 43 |
| Chuẩn | đứng trước | 25 % | 0 % | 43 % | 0,6 % | 56 % | 6 % · −4 % | 54 |
| Chuẩn | tầm ×1,5 | 35 % | 0 % | 46 % | 0,4 % | 59 % | 7 % · −7 % | 55 |
| Chuẩn | diện tích ×2 | 5 % | 0 % | 68 % | 0,5 % | 73 % | 10 % · −27 % | 44 |
| 45 WPM 97 % | hiện tại | 0 % | 0 % | 69 % | 0,4 % | 75 % | 12 % · −28 % | 46 |
| 45 WPM 97 % | đứng trước | 100 % | 59 % | 34 % | 1,1 % | 50 % | 0 % · 0 % | 64 |
| 45 WPM 97 % | tầm ×1,5 | 95 % | 49 % | 37 % | 0,6 % | 52 % | 2 % · −2 % | 63 |
| 45 WPM 97 % | diện tích ×2 | 25 % | 0 % | 65 % | 0,8 % | 72 % | 10 % · −24 % | 48 |
| 80 WPM 97 % | hiện tại | 40 % | 0 % | 67 % | 1,2 % | 72 % | 10 % · −22 % | 56 |
| 80 WPM 97 % | đứng trước | 100 % | 77 % | 28 % | 0,8 % | 45 % | 0 % · 0 % | 77 |
| 80 WPM 97 % | tầm ×1,5 | 100 % | 72 % | 31 % | 1,5 % | 48 % | 2 % · 0 % | 76 |
| 80 WPM 97 % | diện tích ×2 | 65 % | 6 % | 64 % | 1,3 % | 70 % | 9 % · −17 % | 58 |

- **Thêm tầm (hoặc kéo người chơi lên) đổi cả trận:**
  - P về sát dải đích;
  - Q về 45–59 %;
  - đợt 2 gần như không còn thú lọt.
- **Diện tích ×2 gần như không đổi gì,** vì ngân sách mỗi lần tung, hồi chiêu và tầm vẫn như cũ.
- **Tầm không chữa được tất cả:**
  - Chuẩn vẫn chỉ thắng 25–35 %, phần lớn thua ở đợt 6, nơi tốc tới 1,8 con/s vượt sức hạ;
  - 80 WPM 97 % với tầm ×1,5 thì quá dễ ở đầu trận (S 72 %).
- Cân lại tầm, hướng, ngân sách và nhịp là việc của phần 2.

## 6. Giới hạn của bài đo

1. **Bot là của bài đo này, không phải làn 7.** Những điểm đơn giản hóa:
   - Không chuyển sang Backspace sau phím sai: kit từ chối phím sai, nên Backspace sẽ xóa một chữ đúng.
   - Chỉ gõ chiêu khi có thú trong tầm.
   - Không bấm chọn thú mềm, không đặt con trỏ, không dùng đan phù.
   - Không Học trước, không Thẻ Ôn, nên Linh Sa ít hơn người thật.
   - Mua sắm theo một thứ tự cố định.
   - Đứng yên (canon §18.3). Bot Cơ động chưa làm, nên I của nó chưa in.
2. **Bot Trẻ em chạy ở Cân bằng** để so cùng dải, nên B3 và HC3 phần Thư giãn chưa chấm.
3. **Số trong đề bài:** 30, 45, 60, 80 WPM dùng CV 0,25 và chiến thuật Vừa. Chín bot chuẩn dùng đúng bảng BALANCE §6.
4. **Dữ liệu lab** (khung mưa kiếm, điểm nhắm cố định của lab) đọc từ mã lab ở HEAD `c5267d0`.
5. **Ảnh nền là sân xám của lab,** chưa phải mỹ thuật của game. Game có thanh Bàn Quyết che phía dưới, nên khung thật có thể dịch nhẹ.
6. **20 seed mỗi hồ sơ.** Tỉ lệ thắng có sai số khoảng ±10 điểm %.

## 7. Tái lập

Từ `games/immortality-cultivation`. Mọi file nằm trong `tmp/skill-reach/`, ngoài Git. Số (JSON) và bảng dấu chân giữ lại; khung chụp thô, ảnh nền, các ô lẻ và bản sao máy chủ đã xóa, nên muốn dựng lại bảng thì chụp lại nền trước.

| Việc | Lệnh |
|---|---|
| Ma trận bot | `../../.local/bin/heavy.sh --cores=4 tmp/skill-reach/matrix.sh` |
| Gộp số | `node tmp/skill-reach/aggregate.mjs tmp/skill-reach/runs` → `tmp/skill-reach/aggregate.json` |
| Thời gian đi và cửa sổ trong tầm | `node_modules/.bin/tsx tmp/skill-reach/travel.ts 1` |
| Số đợt | `node_modules/.bin/tsx tmp/skill-reach/waves.ts` |
| Chụp nền | máy chủ riêng ở cổng 3197, dựng từ `git archive HEAD`, rồi `node src/kit/tools/cdp-run.mjs tmp/skill-reach/capture.mjs --width=1920 --height=1080` qua `heavy.sh --gpu` |
| Bảng dấu chân | `node tmp/skill-reach/sheet.mjs tmp/skill-reach/runs/w45a97-s1.json <nền> tmp/shots/skill-reach` |

Bot đọc các file sau, không sửa gì:
- `src/app/match.ts`
- `src/kit/balance/typist.ts`
- `src/sim/{targeting,field,pace}.ts`
- `src/typing/grading.ts`
- `tests/typing/world-fixture.ts` (bộ từ khởi đầu lạnh)

Khi `scripts/balance/run.ts` của làn 7 xong, phải đo lại bằng nó.
