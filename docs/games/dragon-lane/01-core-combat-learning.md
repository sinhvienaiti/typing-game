# Rồng Giữ Ải — 01. Vòng chơi, chiến đấu và học (23/10/2026)

> Phần thiết kế 01 của **Rồng Giữ Ải** (id `dragon-hold`, 00 D01).
> Nguồn: yêu cầu chủ dự án 23/10, ba bản nghiên cứu ở `research/`, TD (`TYPING_DEFENSE_DESIGN.md` mục 6, 21), Survival (`SURVIVAL_MODE_PLAN.md` mục 6), mã `shared/learning`.
> **Số chuẩn, bảng phím, ngân sách chữ, cổng bot: `00-canon.md`** (thắng khi lệch). Tài liệu này giữ luật của vòng ải, gõ, Rồng và học.
> Bản sửa 23/10: áp các điểm phản biện (công thức sát thương, ngân sách chữ, khóa, học không thành chép, lọc từ, phím Mac).

## 0. Tóm tắt và luật khóa

**Một câu:** Hai Rồng đứng giữa bản đồ rừng vẽ tay. Quái tới từ 1–4 đường và từ trên trời. Mỗi quái mang một từ tiếng Anh trên đầu. Gõ đúng từ thì Hỏa Long phun lửa vào nó. Bạch Long che chắn, hồi máu, đẩy lùi. Lính chặn, bẫy, nhà phép mua ở cửa hàng giữ đường và gom quái. Gõ là nguồn sát thương chính. Quân ta chủ yếu là hỗ trợ.

**Luật khóa:**

1. Gõ là đòn chính. Phe ta chủ yếu khống chế: chặn, làm chậm, giam, nổ cụm, tăng sức.
2. Quái có máu thật. Mọi nguồn (gõ, bẫy, lính, phép) trừ cùng một thanh máu.
3. Từ đã gắn lên quái thì **không đổi, không chuyển** sang quái khác, tới khi quái chết. Ngoại lệ duy nhất: Từ Ngắt khi quái niệm kỹ năng (mục 3.6).
4. Mọi chữ đang sống có **chữ đầu khác nhau**. Gõ chữ đầu là khóa từ đó.
5. Từ trên quái **không hết hạn**. Áp lực đến từ quái đi tới và đánh, không đến từ đồng hồ chữ.
6. Độ dài từ theo **tốc độ riêng E** của người chơi và **bậc quái**. Không theo số đợt.
7. **Chuẩn thắng ẩu.** Sai nhiều thì đòn yếu và mất Chuỗi. Nhanh chỉ là thưởng thêm.
8. Độ khó đến từ cơ chế: số đường, thành phần đợt, hào quang tướng địch, kỹ năng quái, boss. Không ép gõ nhanh hơn.
9. Phím chữ chỉ để gõ. Lệnh theo bảng phím 00 §6 (Mac trước, đọc `event.code`).
10. Quái tới đều theo nhịp sinh (02 §5). Đợt khó thì có nhiều bầy và nhiều đường hơn, không đổ cả đàn một lúc.
11. Học luôn đọc được: khung học nằm ngoài canvas, không rung, không bị hiệu ứng đè.
12. Game chỉ gửi sự kiện học. Độ thuộc do lõi chung `shared/learning` tính.

## 1. Vòng chơi

### 1.1 Ba vòng lồng nhau

| Vòng | Dài | Người chơi làm gì |
|---|---|---|
| Ải | 4–12 phút | Bày binh, gõ hạ quái qua các đợt, mua sắm giữa đợt, hạ boss |
| Chương | 20 ải (~2,5 giờ) | Một vùng đất, một chủ đề từ vựng. Ải 5, 15 là Ải Tướng; 9, 19 là Ải Ôn; 10 boss nhỏ; 20 boss chương (04 §1.2) |
| Hành trình | 26 chương = 520 ải | Mở vùng mới, Rồng mạnh dần ngoài trận, kho đồ lớn dần, ôn từ qua nhiều ải |

### 1.2 Một ải từ đầu tới cuối

| Pha | Dài | Việc chính |
|---|---|---|
| Lều Chuẩn Bị | Không giới hạn | Xem bản đồ, số đường, đường bay, danh sách đợt (họ quái, tướng địch, boss). Chọn Bộ Mang Theo (03 §4). Chọn mức khó. **Học trước 8 từ mới** (mục 6.5) |
| Bày binh | Không giới hạn | Đặt bẫy, lính chặn, nhà phép bằng vàng đầu ải. Chưa có quái, chưa có chữ. Enter để bắt đầu |
| Rồng ra mắt | 3 s | Hỏa Long chạy Intro. Bạch Long nói một câu (Guide_Talk). Esc bỏ qua |
| Báo đợt | 6 s | Thẻ báo: đường nào sáng, họ quái, số con, dấu tinh anh, dấu tướng địch |
| Đợt | 40–70 s | Quái sinh theo toán (02 §5). Gõ, dùng kỹ năng, dùng đồ |
| Nghỉ giữa đợt | 00 §4.5 | Hai Rồng hồi máu (00 §4.5). Cửa hàng mở. Chọn Long Ấn nếu có. Thẻ Ôn (mục 6.5). Xem trước đợt kế. Gọi sớm |
| Lặng trước boss | 12 s | Không sinh toán mới. Boss chạy Intro trong khung nhỏ góc màn. Chuỗi đóng băng |
| Đợt boss | 00 §4.7 | Boss 2–4 pha, quái hộ tống theo nhịp |
| Kết ải | — | Sao, thưởng, Sổ Từ Ải, Ôn trận tùy chọn 60–90 s |

- Đồng hồ nghỉ **chỉ chạy khi không có bảng nào mở** (bảng Long Ấn, Thẻ Ôn, cài đặt). Dải món và vòng menu đặt món không dừng đồng hồ. Hết giờ thì đợt kế vào. Thẻ học đang mở thì đợt không tự vào.
- Mỗi lần nghỉ chỉ mở một bảng tại một lúc, theo thứ tự: Long Ấn → Thẻ Ôn; sau đó là lúc mua, đặt.
- Gọi sớm (Shift + Enter): số Vàng và Long Nộ ở 00 §4.5.
- Đợt chỉ kết thúc khi mọi quái của đợt đã chết. Đợt kế không đè lên đợt trước, trừ luật ải riêng "Đợt dồn".

### 1.3 Loại ải, số đợt, thời lượng

Bảng số đợt, độ dài đợt, giờ nghỉ, thời lượng theo loại ải: **00 §4.5** (nguồn duy nhất). Số quái mỗi ải theo chương: 00 §4.8.

### 1.4 Một đợt

Bộ sinh đợt (toán, nhịp, đỉnh, lặng, trộn đường, quái bay, tướng mỗi đợt) chỉ có ở **02 §5**. Tải gõ của đợt theo 00 §4.4. Tài liệu này chỉ giữ ba luật công bằng:

- Lịch sinh là dữ liệu cố định theo seed. Chạy lại ra y hệt.
- Nhiều đường thì toán sinh **so le** ít nhất 0,6 s, để quái không tới mọi phía cùng lúc.
- Quái bay đi đường bay riêng, trong trần của 00 §4.5 (bài học Kingdom Rush 5).

## 2. Hai Rồng ở giữa

### 2.1 Bệ Rồng và các vòng

| Vòng (từ tâm) | Bán kính | Ý nghĩa |
|---|---|---|
| Bệ Rồng | 4 m | Hai Rồng đứng ở đây. Không phá được |
| Vòng Cận | 6 m | Quái cận chiến dừng ở đây để đánh Rồng |
| Vòng Nguy | 10 m | Thẻ chữ có gạch đỏ "gần", được ưu tiên mang chữ |
| Vòng Bắn | 10–16 m | Quái đánh xa dừng trong dải này để bắn |
| Vùng Chữ | ≤ 26 m theo đường | Quái vào đây mới được xét gắn chữ |
| Vùng chơi | 28–32 m | Cổng sinh ở rìa. Đường dài 24–36 m |

- Hỏa Long bay lượn thấp, 2,5 m trên bệ. Quái cận chiến vẫn với tới. Bạch Long đứng trên bệ, quay về đường có nhiều quái nhất.
- Thời gian tới bệ (chương 1): đi bộ 1,8 m/s mất ~15 s; bốn chân nhanh 3,0 m/s ~9 s; bay 2,4 m/s ~11 s. Tốc từng loài ở tài liệu quái.

### 2.2 Vai và chỉ số gốc (cấp Rồng 1, chương 1)

| | Hỏa Long | Bạch Long |
|---|---|---|
| Model | `heroes/draconis-v2` (đỏ vàng, cánh màng). Tối Thượng đổi sang `heroes/draconis-v3` bản medium | `guides/draconis-v4` (trắng, đứng thẳng, cánh lông kem cam) |
| Vai | Đánh. Nhận mọi đòn gõ | Che chắn, hồi máu, khống chế. Chặn quái cận chiến ở bệ |
| Máu | 1.000 | 700 |
| Giáp / Kháng phép | 20 / 20 | 40 / 30 |
| Hỏa lực P | 100 | — |
| Chặn | Không | 2 quái cận chiến (quái to chiếm 2 suất) |
| Đánh trả | Không, chỉ đánh bằng gõ | 15 Đòn mỗi 1,5 s vào quái đang bị chặn |
| Hết máu | **Thua ải** (trừ khi có Lông Phượng, mục 5) | Kiệt sức 15 s: không chặn, không kỹ năng, không Từ Trợ. Dậy với 40 % máu |
| Có mặt | Từ ải 1 | Ải 1–10 làm người dẫn (chỉ nói). Vào trận từ ải 11 chương 1 (00 D21) |

**Clip:** Hỏa Long đứng Idle_Hover; đòn gõ Attack_L, Attack_R xen kẽ, Attack_Both khi Chớp, khi hạ Vừa trở lên, hoặc khi quái trong 6 m; bị đánh Hit (tối đa 1 lần mỗi 0,8 s); thua Death; thắng Victory; Từ Khẩn Boost. Bạch Long đứng Guide_Idle; Từ Khẩn Guide_Flap; thắng Guide_Hop rồi Guide_Wave. Bạch Long **thiếu** Hit, Down, Rise (mục 8). Trước khi có: chớp sáng shader khi trúng đòn, giữ Guide_Bow khi kiệt sức.

### 2.3 Đòn gõ của Hỏa Long

```
D = P × M_q × M_c × (1 + Σ tăng)      // sát thương một từ; số ở 00 §4.2
Đòn gõ là loại Chữ: không bị Giáp, Kháng chặn. Chỉ khiên chữ chặn chữ (phải gõ hết lớp khiên).
Bẫy, lính, nhà, kỹ năng: Vật lý hoặc Phép, giảm = G / (G + 100), trần 75 %.
```

- M_q theo kết quả chấm (mục 3.7). M_c theo bậc Chuỗi (mục 3.8). Bảng số: 00 §4.2.
- Sát thương **ghi sổ ở tick +12 (0,2 s)** sau khi gõ xong, bất kể xa gần. Cầu lửa (`skills/dragon-fireball`) bay sao cho chạm đúng tick đó. Quái > 6 m: Attack_L / Attack_R xen kẽ; ≤ 6 m: Attack_Both. Clip chỉ là hình, không đổi số.
- Không có chí mạng ngẫu nhiên. Thưởng đến từ Chớp và Chuỗi, người chơi đoán trước được.
- Quái chết trước khi đòn chạm: đòn rẽ sang quái có chữ gần nhất trong 4 m, 50 % sát thương. Không có thì tắt.
- Giáp vẫn có nghĩa: nó làm bẫy, lính, nhà yếu đi. Quái giáp dày cần Phá giáp hoặc để Rồng gõ.

**Số từ để hạ là bất biến.** Máu quái = W × 90 × g(c) (00 §4.1). 1 W = một từ Vừa. Cấp Rồng trong ải không tăng P, nên số từ không trôi trong ải.

| Bậc (02 §1.2) | W | Số từ Hoàn hảo, không hào quang |
|---|---|---|
| Nhỏ | 0,8–1,2 | 1 (Ẩu thì cần thêm 1 từ) |
| Vừa, Nặng | 2–6 | 2–5 |
| Tinh anh | W × 1,6 | theo W |
| Đội trưởng | 5–7 | 5–6 |
| Thống lĩnh (từ C11) | 10–12 | 9–10 |
| Boss | 29–72 (00 §4.7) | chia pha, cộng Cụm Ấn |

### 2.4 Kỹ năng, Tối Thượng, Long Nộ

Khi kỹ năng sẵn sàng, ô kỹ năng ở đáy màn sáng lên. Bấm Alt + số hoặc bấm chuột là dùng. **Chữ Chiêu** (từ đã thuộc, 3–5 chữ) chỉ hiện tối đa 2 cùng lúc theo ngân sách chữ (00 §5): Tối Thượng khi Long Nộ đầy, và kỹ năng sẵn sàng có hồi lâu nhất. Gõ Chữ Chiêu thì mạnh thêm 10 % và +1 Chuỗi. Chữ Chiêu không giữ chữ đầu khi người chơi tắt nó trong cài đặt. Nếu chuột đang rê trên một đường hoặc một quái lúc dùng, đích là chỗ đó; không thì theo đích mặc định.

- Cài đặt **"Tự dùng kỹ năng hỗ trợ"** (Khiên Lông Vũ, Gió Cuốn): Rồng tự dùng khi đích mặc định có ≥ 3 quái. Bật sẵn ở mức Dễ và hồ sơ trẻ em.
- Mỗi kỹ năng mở theo lịch dạy (04 §6.1). Kỹ năng chưa mở thì không có ô, không có chữ.

| Rồng | Kỹ năng | Phím | Hồi | Tác dụng (bậc 1 → bậc 2) | Đích mặc định | Clip |
|---|---|---|---|---|---|---|
| Hỏa Long | Nội tại Lửa Chữ | — | — | Từ Chớp đốt 0,2P mỗi giây trong 3 s | — | — |
| Hỏa Long | Phun Lửa | Alt+1 | 14 s | Nón 60°, dài 12 m: 1,5P → 2,0P, đốt 3 s | Đường có tổng máu quái lớn nhất trong 12 m | Attack_Both |
| Hỏa Long | Thiên Hỏa | Alt+2 | 24 s | Rơi sau 0,8 s, bán kính 4 m: 2,5P → 3,2P, choáng 1,0 s | Cụm quái đông nhất trong Vùng Chữ | Cast |
| Bạch Long | Nội tại Thầy Rồng | — | — | Mỗi từ mới gõ đúng: Hỏa Long hồi 2 % máu. Sinh Từ Trợ (mục 3.6) | — | Guide_Wave |
| Bạch Long | Khiên Lông Vũ | Alt+3 | 18 s | Khiên 150 → 220 cho Hỏa Long và mọi lính chặn trong 18 m, 6 s | Tự động | Guide_Bow |
| Bạch Long | Gió Cuốn | Alt+4 | 20 s | Quái mặt đất trong 9 m: đẩy lùi 5 m theo đường, chậm 40 % 3 s. Quái bay rơi xuống 2 s (chặn được, bẫy dính) | Quanh bệ | Guide_Flap |

**Long Nộ (0–100): một thanh chung cho hai Tối Thượng.** Đầy thì hiện **hai** Chữ Chiêu Tối Thượng. Dùng một cái là hết thanh. Đánh hay giữ là quyết định thật.

| Tối Thượng | Phím | Tác dụng | Clip |
|---|---|---|---|
| Viêm Đế (Hỏa Long) | Alt+5 | 10 s: Hỏa Long hóa `draconis-v3`. Mỗi từ gõ xong phun một tia xuyên dọc đường, rộng 2 m, dài 22 m, 1,2P mọi quái trúng. Hết giờ: Spit_Big bán kính 7 m, 4P | Intro (biến hình, lửa che 0,3 s), Spit, Spit_Big |
| Lời Thề Bạch Vũ (Bạch Long) | Alt+6 | 8 s: lính chặn, bẫy, nhà phép +40 % sức; bẫy nạp nhanh ×3; quái trong 20 m mất hào quang và không nhận hào quang mới; Hỏa Long hồi 15 % máu | Guide_Talk → Guide_Wave |

- Nạp Long Nộ: từ Chớp / Hoàn hảo / Tốt / Vừa / Ẩu +2,4 / +2,0 / +1,6 / +1,2 / +0,4 · hạ Vừa trở lên +2, tướng địch +8 · phá bộ phận boss +5 · Hỏa Long mất 4 % máu tối đa +1 · mỗi giây trong đợt +0,2 · gọi đợt sớm +5.
- Đích: người gõ đều 35 WPM dùng Tối Thượng mỗi 90–110 s, người 70 WPM ~65 s. Hồi tối thiểu 45 s. Long Nộ giữ qua các đợt, mất khi hết ải.
- Nếu đổi model trông vụng ở bài thử hình: giữ v2, thay Spit bằng Cast. Luật không đổi.

### 2.5 Cấp Rồng trong ải và Long Ấn

Hai Rồng dùng chung **Cấp Rồng** 1–10, về 1 khi vào ải mới. Mọi cách hạ quái (gõ, bẫy, lính) đều cho kinh nghiệm, nên lối chơi thiên hỗ trợ không bị chậm cấp.

- Kinh nghiệm: hạ một cụm bầy 2 · Nhỏ 2 · Vừa, Nặng 6 · tinh anh 10 · Đội trưởng 30 · Thống lĩnh 50 · từ mới gõ đúng lần đầu trong ải 3 · Thẻ Ôn đúng 2 · qua một pha boss 20.

| Lên cấp | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| Kinh nghiệm cộng dồn | 20 | 50 | 90 | 140 | 200 | 270 | 350 | 440 | 540 |
| Thưởng thêm | — | Long Ấn | — | Phun Lửa bậc 2 | Long Ấn | — | Thiên Hỏa, Khiên bậc 2 | Long Ấn | Gió Cuốn bậc 2 |

- Mỗi cấp: máu tối đa hai Rồng +5 % (hồi đúng phần tăng). **Cấp không tăng P** (00 D04). Sức tăng trong ải đến từ bậc kỹ năng và Long Ấn.
- Kiểm: ải thường chương 1 cho ~360–380 điểm → cấp 8. Ải boss → cấp 9–10.
- **Long Ấn** (mở ở C2 ải 24, 04 §6): đạt cấp 3, 6, 9 thì có một lượt chọn. Lượt chọn **chờ tới lần nghỉ kế**; không mở bảng giữa đợt. Chọn 1 trong 3 thẻ bằng phím 1 / 2 / 3, mỗi thẻ một nhóm. Đổi bộ thẻ 1 lần mỗi ải.

| Nhóm | Long Ấn (khởi điểm 12, thêm dần tới 24) |
|---|---|
| Lửa | **Lửa Lan:** từ hạ quái bắn 30 % sát thương sang quái trong 2,5 m · **Đuôi Lửa:** cứ 5 từ có 1 cầu lửa phụ 50 % vào quái có chữ khác · **Than Hồng:** đốt dài gấp đôi · **Phá Vỏ:** từ Chớp gây Phá giáp 4 s lên quái trúng (bẫy, lính đánh nó mạnh hơn) |
| Che chắn | **Vảy Rồng:** Hỏa Long +25 Giáp · **Lông Dày:** Khiên +50 % · **Tổ Ấm:** hồi giữa đợt 10 % → 20 % · **Gió Ngược:** Gió Cuốn hồi nhanh 30 % |
| Chữ | **Mắt Rồng:** Vùng Chữ +4 m · **Chuỗi Bền:** Ẩu chỉ mất 1/3 Chuỗi · **Học Giả:** từ mới cho gấp đôi kinh nghiệm, nghĩa hiện thêm 1 lần gặp · **Lời Nhanh:** Chữ Chiêu ngắn đi 1 chữ, kỹ năng hồi nhanh 10 % |

## 3. Gõ trên quái

### 3.1 Thẻ chữ

| Phần | Luật |
|---|---|
| Từ | 20 px ở 1080p (tối thiểu 16 px ở 720p), đậm. Chữ đầu sáng hơn và gạch chân. Chữ đã gõ đổi màu dần |
| Nghĩa | Dưới từ, chỉ khi mục 6.3 cho phép. ≥ 15 px ở 1080p (sàn 13 px). Chỉ nghĩa đầu tiên (cắt ở dấu ";"), tối đa 22 ký tự, dài hơn thì cắt bằng "…". Nghĩa đầy đủ ở khung học |
| Số thẻ mang nghĩa | Tối đa 4 cùng lúc. Ưu tiên từ mới, rồi quái gần nhất |
| Thanh máu | 3 px dưới thẻ. Vừa trở lên luôn hiện. Nhỏ chỉ hiện khi đã mất máu |
| Khung theo loại | Hình khung và biểu tượng riêng cho mỗi loại, màu theo 05 §4.3: quái thường nền tối trơn · tinh anh viền đồng, vương miện · tướng địch khung bạc, huy hiệu, chấm chuỗi · bộ phận boss viền tím than · Từ Ngắt cam, tia chớp · Từ Trợ xanh lá, chiếc lá |
| Gần, đang khóa | Trong Vòng Nguy: gạch đỏ dưới từ. Đang khóa: lớn 110 %, luôn nằm trên, quái có viền sáng, Hỏa Long quay đầu về nó |

- Thẻ xếp trong không gian màn hình. Chồng nhau thì đẩy ngang, rồi nâng thẻ ưu tiên thấp lên tối đa 3 bậc, kèm vạch nối. Vẫn chồng thì chỉ **khung** thẻ thu 85 %. **Chữ không bao giờ mờ, không bao giờ ẩn.** Quanh Bệ Rồng dùng vòng khe cố định (05 §4.3).
- Quái có chữ ra khỏi khung nhìn (do xoay camera): chip mang từ nằm ở mép màn, có mũi tên. **Không bao giờ phải xoay camera mới gõ được.**
- Khung học (từ lớn, IPA, nghĩa) nằm giữa đáy màn, là DOM ngoài canvas. Khi đang khóa từ, khung hiện theo mục 6.3.

### 3.2 Quái nào được mang chữ (1–4 đường)

- **Ngân sách chữ** (tổng chữ sống, suất chữ quái, trần chữ không thuộc quái): **00 §5**, nguồn duy nhất. Trần là hằng số của luật, không theo bậc máy.
- Mỗi 0,25 s, quái chưa có chữ trong Vùng Chữ được xếp theo đe dọa:

```
Đe dọa = 10 / thời gian tới bệ (s) × hệ số bậc   // Nhỏ 1 · Vừa, Nặng 1,5 · tinh anh 2 · Đội trưởng 3 · Thống lĩnh 4 · boss 5
       + 6 nếu đang đánh Rồng hoặc lính chặn
       + 8 nếu đang niệm kỹ năng
       + 5 nếu người chơi đã bấm chuột đánh dấu
```

- **Lượt 1:** mỗi đường có quái trong 20 m được ít nhất 1 chữ, cho con đe dọa cao nhất của đường đó. Quái bay tính là một "đường trời".
- **Lượt 2:** suất còn lại chia theo đe dọa trên toàn bản đồ. Suất khẩn chỉ cho: quái trong Vòng Nguy, quái đang niệm, tướng địch, bộ phận boss.
- Quái không có chữ vẫn bị bẫy, lính, kỹ năng đánh. Cuối chương, phần lớn đám đông do bẫy và kỹ năng xử lý; chữ dành cho con nguy hiểm nhất. Đó là chiến thuật cốt lõi.

### 3.3 Chữ đầu duy nhất và khóa

Dùng lại lõi gõ của TD (`router`, `letters`, `picker`, `scorer`) qua bộ dùng chung `shared/game-kit`, chỉ đổi cấu hình.

- Tầng 1: mọi chữ sống có chữ đầu khác nhau. Chữ đầu vừa trả nghỉ 1,0 s. Giữ 3 chữ đầu dự trữ cho chữ ưu tiên cao. Tránh q, x, z, j làm chữ đầu ở cấp từ vựng ≤ 10.
- Tầng 2 (dự phòng): hai chữ đầu, gạch chân cả hai, khi hết chữ cái trống (cấp từ vựng ≤ 3: khi còn ≤ 5).
- Không hai từ giống nhau cùng sống. Không hai từ có khoảng cách sửa chữ ≤ 1 ("form" và "from").
- Thứ tự giữ chữ đầu: Cụm Ấn boss → Từ Ngắt → chữ quái khẩn → Từ Khẩn → chữ quái thường → Chữ Chiêu → Từ Trợ → Từ Kích → vật bản đồ. **Từ Ngắt cũng theo luật này; không bao giờ trùng chữ đầu với chữ đang sống.**
- Khóa theo TD 6.15. Từ đang khóa mới gõ đúng 1 chữ mà phím kế là chữ đầu của từ khác thì **đổi khóa mềm**, không tính lỗi cho từ cũ. Backspace xóa một chữ. Esc nhả khóa.

**Bảo hộ khóa.** Quái đang bị khóa và đã gõ ≥ 1 chữ thì không chết vì nguồn khác trong 1,2 s. Nó giữ lại 1 máu và có viền "đang gõ". Gõ xong trong 1,2 s thì đòn gõ hạ nó, có sự kiện học. Quá 1,2 s thì nguồn khác hạ được; khi đó nhả khóa, không phạt, không gửi sự kiện học, phím kế không mất. Cổng G11: mất khóa ≤ 5 %.

**Chữ bị che, chữ bị thay** (luật chung cho mọi cơ chế ở 02, 04):

| Tình huống | Luật |
|---|---|
| Chữ bị ẩn (Màn Phấn, tàng hình, tối, sương lan) | Coi như **chưa có chữ**: không giữ chữ đầu, không gõ được, chỉ hiện chip "• • •". Khi lộ ra thì gán chữ mới, có ân hạn 0,5 s trước khi quái được xếp đe dọa khẩn. Không gửi sự kiện học cho chữ ẩn |
| Tối, sương | Ghi là "Vùng Chữ co lại" trên thẻ ải (ví dụ còn 14 m). Không che chữ đã gán |
| Khiên chữ mới, Từ Ngắt mới | Chỉ thay chữ **chưa bị gõ**. Chữ đang khóa thì lớp mới xếp hàng sau, hiện khi chữ hiện tại xong |
| Chữ "ngủ" (mai đóng, khung giờ tắt) | Chữ mờ, không nhận phím. Phím gõ vào nó không tính lỗi; tiến độ đã gõ được giữ; khi chữ thức thì gõ tiếp |
| Thẻ ra mắt loài mới | Không chặn việc gán chữ |

### 3.4 Độ dài từ theo bậc quái và tốc độ E

E là tốc độ riêng (WPM), đo và cập nhật như TD 6.6 (mức nền B, sàn theo độ khó). Bảng là số chữ của **một** từ.

| E (WPM) | Nhỏ thường | Nhỏ nhanh, bay | Vừa, Nặng, tinh anh | Tướng địch (mỗi từ) | Chữ Chiêu, Từ Trợ, Từ Ngắt | Từ Khẩn | Bộ phận boss | Cụm Ấn boss |
|---|---|---|---|---|---|---|---|---|
| < 25 | 3–5 | 3–4 | 4–6 | 4–6 | 3–4 | 6–7 | 4–6 | 2 từ × 3–5 |
| 25–44 | 3–6 | 3–5 | 4–7 | 5–7 | 3–5 | 7–8 | 5–7 | 2–3 từ × 3–6 |
| 45–64 | 4–7 | 3–5 | 5–8 | 5–8 | 3–5 | 7–9 | 5–8 | 3 từ × 4–7 |
| ≥ 65 | 4–8 | 4–6 | 6–9 | 6–9 | 4–5 | 8–10 | 6–9 | 3–4 từ × 4–8 |

- Thiếu từ đủ dài ở cấp từ vựng thấp: rút dải xuống 1 chữ, hoặc thay một từ dài bằng 2 từ ngắn nối nhau. Ghi "thiếu từ" để bot báo.
- Kho từ chung có 18.000 mục, chỉ 3 mục nhiều chữ, không có câu. Vì vậy Cụm Ấn, đòn kết và mọi chỗ cũ ghi "câu" đều là **chuỗi chủ đề**: 3–5 từ đơn cùng chủ đề (00 D19). Chỉ dùng câu khi `shared/typing-texts` có câu kèm nghĩa Việt và IPA từng từ.
- 02 dùng ký hiệu D1–D5 cho dải độ dài; độ dài thật luôn lấy theo bảng này và E.

### 3.5 Quái nhiều từ và chữ nối

- Quái còn máu sau một từ: từ kế hiện sau 0,25 s ở trạng thái **khóa mềm**. Phím kế đúng chữ đầu của nó thì gõ tiếp. Phím kế là chữ đầu của quái khác thì đổi sang quái kia, không phạt.
- Tướng địch hiện **chuỗi 3 từ**: từ hiện tại sáng, hai từ sau mờ (chưa giữ chữ đầu). **Ấn Phá** (viền đồng): ở Đội trưởng là từ thứ 3, 6, 9… của chuỗi; ở Thống lĩnh là một từ riêng cạnh tên, hiện lại 15 s sau khi bị gõ.

### 3.6 Chữ đặc biệt

| Loại | Xuất hiện khi | Nhóm từ | Gõ xong thì | Không gõ thì |
|---|---|---|---|---|
| Từ Tinh Anh | Quái tinh anh | Đến hạn ôn | Đòn thường. Dài hơn quái Nhỏ 1 chữ | — |
| Ấn Phá | Đội trưởng: từ thứ 3, 6, 9… Thống lĩnh: từ riêng cạnh tên | Đến hạn ôn | Tắt hào quang 8 s; khựng 0,5 s (Thống lĩnh 1,5 s) | Hào quang vẫn chạy |
| Từ Ngắt | Quái niệm kỹ năng (thanh niệm 2,5–4 s). Thay chữ **chưa bị gõ** của quái đó; chữ đang khóa thì gõ xong chữ cũ cũng tính là ngắt | Đã thuộc | Hủy kỹ năng, choáng 1 s, vẫn tính sát thương | Kỹ năng ra như thiết kế |
| Từ Trợ | Lính chặn < 50 % máu; bẫy đang nạp; Hỏa Long dính hiệu ứng xấu. Cần Bạch Long đang đứng. Mỗi mục tiêu hồi 12 s, tối đa 2 cùng lúc. Không đặt trong 10 m quanh bệ | Đã thuộc, đang học | Hồi 30 % máu lính và khiên 2 s / nạp bẫy ngay / giải hiệu ứng | Tắt sau 8 s, không phạt |
| Chữ Chiêu | Kỹ năng sẵn sàng, trong trần 2 của 00 §5 | Đã thuộc | Dùng kỹ năng, +10 % sức, +1 Chuỗi | Chờ ở ô kỹ năng |
| Từ Khẩn | 1 lần mỗi đợt, khi ≥ 3 quái trong Vòng Cận hoặc Hỏa Long < 35 % máu | Đã thuộc, dài | Long Hống: 3P loại Chữ mọi quái trong 10 m, đẩy lùi 6 m, ngắt mọi kỹ năng đang niệm | Ở HUD tới hết đợt |
| Bộ phận boss | Boss có 2–4 bộ phận, mỗi bộ phận một từ | Đến hạn ôn | Phá bộ phận: boss mất một kiểu đánh, nhận sát thương lớn | — |
| Cụm Ấn boss | Boss báo đòn lớn. Chuỗi chủ đề 2–4 từ | Đến hạn ôn, cùng chủ đề | Hủy đòn, choáng boss 3 s, 4P | Đòn rơi xuống |
| Từ Hỏi Nghĩa | Pha boss từ chương 3 (ô trả lời riêng); luật ải "Nghĩa" trên quái thường (thẻ hiện nghĩa, chữ đầu và số ô: `b _ _ _`). Thẻ boss hiện nghĩa tiếng Việt, từ loại và số ô chữ | Đang học | Boss: như Cụm Ấn. Quái thường: đòn thường | Mốc gợi ý chung: 3 s hiện IPA, 6 s hiện chữ đầu; đòn boss rơi theo công thức báo trước dưới đây |
| Từ Nghe | Luật ải "Nghe" trên quái thường (loa, chữ đầu, số ô); boss cơ chế NE (loa, số ô, ô trả lời riêng). Phát âm khi chữ hiện | Đang học, đã thuộc | Đòn thường | Tab nghe lại. Tắt tiếng: hiện IPA và số ô chữ |

**Luật đề bài cho Hỏi Nghĩa và Nghe** (tránh chấm sai người gõ đúng, tránh dò chữ đầu):

- Chỉ hỏi từ có **nghĩa đầu tiên duy nhất** trong bộ từ của ải. Không chọn được thì chấp nhận mọi từ cùng nghĩa có trong bộ, ghi `userAnswer`.
- Nghe: loại nhóm đồng âm (right/write, sea/see, week/weak…), hoặc chấp nhận cả nhóm.
- Thẻ hỏi mở một **ô trả lời** riêng như cửa sổ Cụm Ấn: mọi phím chữ vào ô đó, không khóa theo chữ đầu, không giữ chữ đầu. Chấm cả từ khi đủ số ô hoặc khi bấm Enter. Nhờ vậy không dò được chữ đầu bằng phím thử.

**Công bằng với đòn boss:**

```
Thời gian báo trước = 1,0 + 1,6 × 12 × (Σ số chữ + số từ) / (E × d)   giây, tối thiểu 4 s
Ví dụ 3 từ × 5 chữ, E = 35, d = 1: 1,0 + 1,6 × 12 × 18 / 35 ≈ 10,9 s
```
- Trong cửa sổ Cụm Ấn: không sinh Từ Trợ, Từ Kích mới, không phát âm, Chuỗi không bị trừ. Tối đa 4 từ boss cùng lúc (00 §5).
- Ngưỡng đổi pha của từng boss: bảng 02 §4.3 (nguồn duy nhất). Mỗi pha thêm một luật gõ.

### 3.7 Chấm một từ: chuẩn và nhanh

```
e      = số phím sai khi đang khóa từ đó (không tính đổi khóa mềm, không tính phím lạc)
t_k    = thời gian từ phím đầu tới phím cuối của từ
t_exp  = 12 × (số chữ − 1) / (E × d)
d      = đã thuộc 1,00 · đang học 0,85 · từ mới 0,70 · Hỏi Nghĩa, Nghe 0,60
```

| Kết quả | Điều kiện | M_q | Chuỗi |
|---|---|---|---|
| Chớp | e = 0 và t_k ≤ 0,85 × t_exp | 1,25 + đốt (Lửa Chữ) | +1 |
| Hoàn hảo | e = 0 | 1,10 | +1 |
| Tốt | e = 1 và từ ≥ 6 chữ | 1,00 | +1 |
| Vừa | e = 1 và từ ≤ 5 chữ | 0,90 | Giữ nguyên |
| Ẩu | e ≥ 2 (Cụm Ấn: e ≥ 3) | 0,60 | Chia đôi |

| Yếu tố | Trong trận | Với việc học |
|---|---|---|
| Chuẩn từng từ | M_q, Chuỗi, Long Nộ. Quái Nhỏ ≤ 1,0 W vẫn chết khi Vừa; Ẩu thì cần thêm 1 từ | Chỉ e = 0 tính là đúng (mục 6.6) |
| Nhanh | Chớp: +25 % và đốt. Không có thưởng nào chỉ cần nhanh mà ẩu | Không ảnh hưởng |
| Chuẩn cả ải ≥ 95 % | +10 % Vảy Rồng của ải (Vàng không mang ra khỏi ải) | Một điều kiện của Huy hiệu Học |
| Phím lạc | Tiếng "tóc" nhỏ, chỉ vào thống kê | — |
| Sai 3 phím trong một từ | Chữ kế sáng lên, nghĩa hiện lại | Ghi `hintUsed` |

- Ví dụ: người 50 WPM ẩu 85 % trung bình M_q ~0,85; người 35 WPM chuẩn 98 % trung bình ~1,10. Người chuẩn hạ quái Vừa 2 W bằng 2 từ, người ẩu thường cần 3. Bot kiểm điều này (00 §7, G7).

### 3.8 Chuỗi

Một số cho cả ải. Không mất khi Rồng bị đánh. Đóng băng khi nghỉ giữa đợt, lặng trước boss, cửa sổ Cụm Ấn.

| Bậc | Chuỗi | M_c | Long Nộ nạp thêm | Hình, tiếng |
|---|---|---|---|---|
| 0 | 0–4 | 1,00 | — | — |
| 1 | 5–9 | 1,04 | +5 % | Lửa trên miệng Hỏa Long cam sáng |
| 2 | 10–19 | 1,08 | +10 % | Tiếng phím lên một nốt |
| 3 | 20–39 | 1,12 | +15 % | Lửa chuyển vàng, viền màn ấm nhẹ |
| 4 | 40+ | 1,16 | +20 % | Lửa trắng xanh, cầu lửa có vệt dài |

- Từ đặc biệt (Ấn Phá, Từ Ngắt, Cụm Ấn, Từ Khẩn) gõ tốt: +2. Mốc 10, 25, 50, 100: Bạch Long nói một câu ngắn, chữ nổi "Chuỗi 25!".
- Bỏ dở một từ để đổi sang quái khác không trừ Chuỗi. Chọn mục tiêu là chiến thuật.

### 3.9 Phím và chuột

- **Bảng phím: 00 §6** (nguồn duy nhất cho 01, 03, 05). Tóm tắt: a–z chỉ để gõ; Backspace xóa một chữ; Esc nhả khóa → đóng bảng → tạm dừng; Tab nghe lại; Alt + 1…6 kỹ năng và Tối Thượng; Alt + 7…9 đồ tiêu hao; Alt + 0 camera; số 1…9 chọn món để đặt; Backquote sửa món đã đặt; Shift + Enter gọi sớm. **Space** bị nuốt; trong Cụm Ấn từ tự nối.
- Tạm dừng (Esc) che chữ. Mất focus giữa đợt thì tự dừng (06 §2).
- **Chuột trái vào quái:** đánh dấu (ưu tiên mang chữ, làm đích kỹ năng). **Rê chuột** hoặc **giữ Alt khi đang khóa:** thẻ thông tin quái (tên, đặc tính, kỹ năng, hào quang, khắc chế).
- Lớp đầu vào giữ luật `keys.ts`: bỏ phím IME đang soạn, phím giữ lặp, phím có Ctrl / Meta, phím `isTrusted === false`. Phím lệnh đọc `event.code`.

### 3.10 Tải gõ: thước đo để thiết kế đợt

```
Sức gõ C(E) = 60 / (0,45 + 12 × (ℓ̄ + 1) / (E × d))   từ mỗi phút      // E = 35, ℓ̄ = 4,5, d = 0,86 → C ≈ 22,7
Tải đợt L   = W_gõ của đợt / (22,7 × số phút của đợt)                 // định nghĩa W_gõ: 00 §4.4
```
- Bảng sức gõ ở 25 / 35 / 60 WPM, dải tải từng đợt, nhịp co giãn k_E: **00 §4.3–4.4**.
- Dải tải giống nhau ở mọi chương. Tải trên 1,0 là cố ý: phần dư do bẫy, lính chặn, nhà phép và kỹ năng gánh. Đó là chỗ cửa hàng có giá trị thật.

## 4. Khi quái tới gần

### 4.1 Quái tới gần làm gì

Số đòn của từng loài (tầm, sát thương, nhịp, báo trước) chỉ ở **02 §2.2, §3.4, §4.5**. Bảng dưới chỉ là kiểu hành động.

| Kiểu quái | Dừng ở đâu | Hành động |
|---|---|---|
| Cận chiến hai chân | Lính chặn trên đường; không có thì Vòng Cận | Chém, đâm |
| Cận chiến bốn chân | Như trên | Cắn, húc. Một số con vồ qua lính chặn |
| Đánh xa | Dải 10–16 m | Bắn, ném (Vật lý hoặc Phép) |
| Bay | Vòng 6–8 m, cao 3 m, không bị chặn | Lao, phun |
| Tướng địch | 8 m | Đòn riêng, cộng kỹ năng và hào quang |
| Boss | Theo kịch bản | Đòn lớn, luôn báo trước (mục 3.6) |

- Quái đang đánh vẫn giữ chữ. Thẻ của nó lên suất khẩn, có gạch đỏ.
- Mỗi đòn đánh phải có động tác vung báo trước ≥ 0,3 s. Hoạt ảnh, tiếng, hiệu ứng riêng từng loài ở tài liệu quái.

### 4.2 Ai bị đánh

| Kẻ đánh | Thứ tự chọn mục tiêu |
|---|---|
| Cận chiến | Lính chặn trên đường (còn suất) → Bạch Long (còn suất chặn) → Hỏa Long |
| Đánh xa | Lính chặn đang chặn đồng đội của nó trong tầm → Hỏa Long |
| Bay | Hỏa Long. Quái bay có kỹ năng phá bẫy thì nhắm bẫy trước |
| Quái phá (sapper) | Bẫy hoặc nhà phép gần đường nhất → lính chặn |
| Tướng địch | Lính chặn mạnh nhất trong tầm → Hỏa Long |
| Boss | Theo pha. Mỗi pha ít nhất một đòn nhắm lính chặn và nhà phép |

- Lính chặn có 1–3 suất chặn (tài liệu cửa hàng). Quái to chiếm 2 suất. Quái bay không bị chặn. Đồ khiêu khích đè lên bảng này trong thời gian tác dụng.

### 4.3 Máu, giáp, hồi máu của Rồng

- Công thức giáp ở 00 §4.2. Rồng nhận cả Vật lý và Phép. Giảm tối đa 75 %.
- Trong đợt **không tự hồi máu**. Hồi chỉ đến từ Bạch Long, đồ hỗ trợ, nhà phép. Hồi giữa đợt: 00 §4.5.
- Máu, giáp mua thêm ở cửa hàng. Ngân sách khởi điểm: cuối chương 1, cửa hàng nâng được máu Hỏa Long lên khoảng ×1,5 và giáp +30.
- Kiểm nhanh (số đòn 02 §2.2): 3 Yêu Rêu Lính (8 mỗi 1,4 s) đánh Hỏa Long gây ~17 mỗi giây, sau Giáp 20 còn ~14. Hỏa Long chịu ~70 s. Một đợt để lọt 5–6 con là mất 25–35 % máu, mà hồi giữa đợt chỉ 10 %. Để quái lọt là thiệt dồn qua các đợt, nhưng không thua ngay.

## 5. Thắng, thua, sao, thử lại

| Mục | Luật |
|---|---|
| Thắng | Hạ hết quái của đợt cuối (cả boss) khi Hỏa Long còn sống |
| Thua | Hỏa Long hết máu và không còn Lông Phượng. Hoặc trượt mục tiêu riêng của ải (tài liệu ải) |
| Lông Phượng | Đồ tiêu hao (03 §6.3), mở ở C2, tối đa 1 mỗi ải: tự kích khi Hỏa Long hết máu, dậy với 40 % máu, kèm một Long Hống miễn phí |
| Bạch Long gục | Không thua. Kiệt sức 15 s |
| Sao | 1 sao: thắng. 2 sao: Hỏa Long còn ≥ 50 % máu. 3 sao: còn ≥ 80 % và không dùng Lông Phượng |
| Huy hiệu Học (riêng, không phải sao) | Độ chuẩn ≥ 90 % và mọi từ mới của ải được gõ đúng ít nhất 1 lần |
| Thử lại từ đợt trước | 1 lần mỗi lần chơi ải: quay về đầu lần nghỉ trước đợt vừa thua, giữ đồ đã có lúc đó. Ải đó tối đa 2 sao |
| Khi thua hoặc bỏ ải | Giữ 30 % tiền tài khoản đã kiếm trong ải. Sự kiện học đã gửi vẫn giữ. Không mất gì khác |
| Chống nản | Chạy nhanh × 2 khi nghỉ hoặc khi không còn chữ sống; nút chơi lại ải; bỏ qua ải sau 3 lần thua cho hồ sơ trẻ em (06 §10) |

**Độ khó tự chọn:** bảng duy nhất ở **00 §4.10**. Mức khó không đổi độ dài từ, vì từ đi theo E.

## 6. Học trong trận

### 6.1 Bộ từ của ải

Mỗi ải có một chủ đề và dải cấp từ vựng (tài liệu ải). Khi nạp ải, game hỏi lõi học chung qua portal (`typing-game:learning:v1:query`) rồi dựng bộ 70–100 từ.

| Nhóm | Định nghĩa (theo `shared/learning`) | Tỉ lệ | Giới hạn |
|---|---|---|---|
| Mới | Chưa có bản ghi trong hồ sơ | 12–15 % | 8 mỗi ải (ải boss 6), tối đa 2 mỗi đợt |
| Đến hạn, yếu | `nextReviewAt` ≤ bây giờ, hoặc độ thuộc < 40 | 35 % | Theo Smart Priority, từ mọi game nguồn |
| Đang học | Độ thuộc 40–69 | 30 % | Trong dải cấp của ải |
| Đã thuộc | Độ thuộc ≥ 70 | 20 % | Cho chữ cần phản xạ |

- Thiếu nhóm nào thì bù bằng từ của dải cấp ải, theo thứ tự danh sách (từ thông dụng trước).
- **Lọc từ nhạy cảm (00 D15).** Kho chung có từ tục và từ người lớn ngay ở cấp thấp (cấp 4–5, 8, 15, 21–23). Từ có cờ `sensitive` không bao giờ vào bộ từ, Thẻ Ôn, Sổ Từ, Chữ Chiêu hay bất kỳ chữ nào trong game. Hồ sơ trẻ em loại thêm nhóm bạo lực và chất cấm (cờ `mature`: kill, gun, drug, suicide…). Khi cờ chưa có trong `shared/vocabulary`, game dùng danh sách chặn riêng có test (mục 6.8).
- **Khởi động lạnh** (hồ sơ trống): 50 từ đầu của cấp hiện tại làm "đã thuộc tạm" cho chữ phản xạ. Từ mới vẫn tối đa 8.
- Portal không trả lời trong 2 s (chơi ngoài portal): dùng bản lưu cục bộ lần trước; sự kiện học xếp hàng chờ gửi.
- Không lặp một từ trong ải tới khi dùng hết nhóm đó (luật `WordPicker`). Bộ chọn từ nhận RNG theo seed.

### 6.2 Từ nào lên quái nào

| Nhóm | Đặt lên | Không bao giờ đặt lên |
|---|---|---|
| Mới | Nhỏ, Vừa đi bộ chậm (S1–S2), khi còn ≥ 14 m tới bệ. Quái mang từ mới đi chậm 15 % (vầng sáng nhẹ báo hiệu) | Quái bay, quái nhanh, quái đang đánh, tinh anh, tướng địch, Ấn Phá, Từ Ngắt, Chữ Chiêu, Từ Khẩn, Cụm Ấn |
| Đến hạn, yếu | Tinh anh, tướng địch, Ấn Phá, bộ phận boss, Cụm Ấn, Từ Hỏi Nghĩa, Từ Kích | Quái bay nhanh |
| Đang học | Nhỏ, Vừa mọi loại, Từ Trợ | — |
| Đã thuộc | Quái nhanh, quái bay, Từ Ngắt, Chữ Chiêu, Từ Khẩn, Từ Trợ | — |

- Lý do: chữ cần phản xạ dùng từ đã quen; chữ có nhiều thời gian đọc dùng từ cần học. Người chơi không bị ép học từ mới dưới áp lực.
- Bảng này là **nguồn duy nhất** cho việc gán nhóm từ lên quái. 02 chỉ giữ dải độ dài (D1–D5), không có cột nguồn từ.

### 6.3 Hiện IPA và nghĩa theo độ thuộc

**Vấn đề đã sửa (00 D14):** gõ trên quái là **gõ chép** (từ hiện sẵn). Lõi chung `calculateMastery` đưa một từ mới gõ đúng 1 lần lên ~84, gõ đúng 3 lần trong một ải lên ~92. Nếu ẩn nghĩa theo độ thuộc thô thì từ lần gặp thứ 3 người chơi mất nghĩa dù chưa lần nào phải **tự nhớ**. Vì vậy:

- **"Lần nhớ đúng"** = lần đúng ở `meaning-recall`, `listening` hoặc `review-card` (đọc từ `recentSamples` của hồ sơ). Gõ chép không tính.
- Nghĩa và IPA ẩn theo **số lần nhớ đúng**, không theo độ thuộc thô.

| Mức của từ | Thẻ trên quái | Khung học khi đang khóa | Sau khi hạ |
|---|---|---|---|
| Mới (chưa có bản ghi) | Từ + nghĩa + chip "MỚI" | Từ + IPA + nghĩa | Phát âm. Khung giữ "từ · nghĩa ✓" (mục dưới) |
| Chưa nhớ (< 2 lần nhớ đúng) | Từ + nghĩa (trong trần 4 thẻ của 3.1) | Từ + IPA + nghĩa | Phát âm nếu độ thuộc < 40 |
| Đã nhớ (≥ 2 lần nhớ đúng, độ thuộc < 70) | Chỉ từ | Từ + IPA. Nghĩa hiện **sau khi gõ xong** (nhớ lại) | Nghĩa 0,8 s |
| Thuộc (≥ 2 lần nhớ đúng và độ thuộc ≥ 70) | Chỉ từ | Không vào khung; chỉ đổi màu chữ trên thẻ | Không hiện |

**Khung học là hàng đợi có ưu tiên** (khung đổi quá nhanh khi gõ 35–45 WPM):

- Từ mới và từ độ thuộc < 40 được **ghim ≥ 2,5 s** sau khi hạ. Từ khác không thay được chúng trong lúc ghim.
- Từ "Thuộc" không vào khung.
- Dòng nhỏ **"Vừa học"** dưới khung giữ 3 từ mới gần nhất (từ · nghĩa). Bấm Tab khi không khóa từ nào: nghe lại từ đầu dòng.
- Một thời gian giữ duy nhất: 2,5 s cho từ mới, độ thuộc < 40; 0,8 s cho từ khác. 05 §4.4 vẽ theo số này.

- Sai 3 phím trong một từ: nghĩa hiện lại.
- `hintUsed = true` khi nghĩa hoặc IPA **đang hiện** (trên thẻ hoặc khung) trong lúc gõ từ đó, kể cả do cài đặt "Luôn hiện IPA", "Luôn hiện nghĩa", mức Dễ, hồ sơ trẻ em.
- Hồ sơ trẻ em và mức Dễ: nghĩa luôn hiện.

### 6.4 Phát âm

- Tự phát (mặc định): từ mới khi bị khóa lần đầu trong ải và khi hạ; từ độ thuộc < 40 khi hạ. Từ độ thuộc ≥ 40 không tự phát.
- Luôn phát: Thẻ Ôn, Học trước, Sổ Từ Ải. Từ Nghe phát khi chữ hiện (đó là đề bài).
- Tab nghe lại từ đang khóa hoặc vừa hạ, ghi `replayUsed`.
- **Một kênh phát âm duy nhất**, có hàng chờ, hai lần phát cách nhau ≥ 2,5 s (số duy nhất; 05 dùng số này). Thứ tự: Từ Nghe và cơ chế NE của boss > từ mới > từ yếu. Quá 2 s chưa tới lượt thì bỏ. Quái "thì thầm" (02) không tự phát khi đang có NE.
- Không phát trong cửa sổ Cụm Ấn, khi boss báo đòn, khi Bạch Long đang nói.
- Tắt tiếng hoặc bật "phụ đề âm": Từ Nghe, quái thì thầm, NE hiện IPA và số ô chữ thay cho tiếng.
- Khi phát: tiếng đòn và va chạm hạ 6 dB, nhạc hạ 4 dB (xuống 80 ms, lên 400 ms). Không tắt hẳn tiếng nào.
- Giọng theo cài đặt giọng chung (`shared/voice`). Cài đặt trong game: Tắt / Chỉ từ mới / Từ mới và từ yếu (mặc định) / Mọi từ hạ.

### 6.5 Học trước ải, ôn giữa đợt, ôn cuối ải

| Lúc | Nội dung | Thưởng | Bắt buộc |
|---|---|---|---|
| Lều Chuẩn Bị: Học trước | 8 từ mới của ải: từ, IPA, nghĩa, phát âm. Gõ lại mỗi từ một lần, không giới hạn giờ | +5 vàng đầu ải mỗi từ đúng (tối đa +40) | Không |
| Nghỉ giữa đợt: **Thẻ Ôn** (đã gộp Chợ Học, 00 D09) | Tối đa 3 câu từ đợt vừa xong: từ Ẩu → từ có `hintUsed` → từ mới. Kiểu câu xoay vòng: nghe rồi gõ từ; xem nghĩa rồi gõ từ; từ chương 3 thêm chọn nghĩa đúng 1 trong 3 bằng **phím 1 / 2 / 3** (khi thẻ mở, phím số thuộc thẻ) | Mỗi câu đúng: +10 Vàng, +1 Tri Thức, +2 kinh nghiệm. Sai: không mất gì, hiện lại từ, nghĩa, IPA | Không. Đồng hồ nghỉ dừng khi thẻ mở. Tắt được trong cài đặt |
| Kết ải: Sổ Từ Ải | Danh sách từ đã gặp: mới học, gõ sai, cần ôn. Bấm để nghe | — | — |
| Kết ải: Ôn trận | 60–90 s. Từ Ẩu → từ có gợi ý → từ mới. Nghĩa, phát âm, gõ lại | +10 % tiền tài khoản của ải | Không |

### 6.6 Sự kiện học gửi về lõi chung

| Trường | Giá trị |
|---|---|
Mục này là **nguồn duy nhất** cho sự kiện học của game. 03, 04, 05 chỉ trỏ về đây.

| Trường | Giá trị |
|---|---|
| `gameId` | `dragon-hold` (00 D01; đăng ký ở `portal/public/games.json`) |
| `entityType` / `entityId` | `vocabulary` / từ tiếng Anh, chuẩn hóa NFKC, trim, chữ thường |
| `result` | `correct` khi e = 0. `wrong` khi e ≥ 1, kèm `errorType: "spelling"` (như sự kiện chiến đấu của Space: chỉ hoàn hảo mới tính đúng) |
| `responseMs` | t_k, từ phím đầu tới phím cuối |
| `hintUsed` | `true` khi nghĩa hoặc IPA đang hiện lúc gõ (mục 6.3), hoặc nghĩa hiện lại sau 3 lỗi |
| `replayUsed` | Đã bấm Tab nghe lại từ đó |
| `expectedAnswer`, `userAnswer` | Từ đúng; từ người chơi nộp (Hỏi Nghĩa, Nghe, Thẻ Ôn) |

- `activityType`: `typing-enemy` (quái thường, cụm bầy) · `typing-elite` (tinh anh, tướng địch, Ấn Phá) · `typing-boss` (bộ phận boss, từng từ trong Cụm Ấn) · `typing-skill` (Chữ Chiêu, Từ Ngắt, Từ Trợ, Từ Khẩn, Từ Kích, Pháo Hiệu Rồng, vật bản đồ) · `meaning-recall` (Từ Hỏi Nghĩa, câu chọn nghĩa ở Thẻ Ôn) · `listening` (Từ Nghe, NE) · `review-card` (Thẻ Ôn gõ lại, Học trước, Ôn trận).
- **Một sự kiện có chấm cho mỗi từ mỗi ải** (00 D14): lần gặp đầu gõ xong. Các lần sau trong cùng ải chỉ ghi cục bộ (Sổ Từ Ải, chọn Thẻ Ôn). Ngoại lệ: `meaning-recall`, `listening`, `review-card` luôn gửi, vì đó là lần nhớ thật.
- Không gửi khi: từ bỏ dở, quái chết vì nguồn khác, chữ đang ẩn, ván bị cờ gian lận (luật TD 21.8).
- Gửi theo lô mỗi 5 s, và khi hết đợt, hết ải, đóng tab. Mỗi tin `attempt` một sự kiện, như hợp đồng hiện có.
- Game không tự tính độ thuộc. Chỉ đọc độ thuộc từ kết quả truy vấn để chọn từ và quyết định hiện nghĩa.

### 6.7 Học thành sức mạnh (có giới hạn)

- Từ mới gõ đúng lần đầu: +3 kinh nghiệm Rồng, Hỏa Long hồi 2 % máu (Thầy Rồng). Gặp từ mới là có lợi.
- Từ đã thuộc **không** mạnh hơn từ mới. Không ai có lý do né từ mới.
- Từ mới không bao giờ nằm trên quái nguy hiểm (mục 6.2). Học không làm thua.

### 6.8 Việc cần ở repo cha (phụ thuộc)

| Việc | Vì sao | Nếu chưa có |
|---|---|---|
| Kit học nhận `gameId` làm tham số | `src/learning/shared.ts` của Space gắn cứng `space-typing` | Không gửi được sự kiện. Chặn bản chạy thử |
| Thêm `dragon-hold` vào `games.json` | Bridge kiểm `gameId` khớp game đang mở và origin khớp `appUrl` | Như trên |
| Truy vấn mới: tra bản ghi theo danh sách ≤ 200 `entityId` (`typing-game:learning:v1:lookup`), trả cả `recentSamples` | Truy vấn hiện có chỉ lọc, không biết từ nào **chưa có** bản ghi; mục 6.3 cần số lần nhớ đúng | Coi từ không có trong kết quả là từ mới; đếm lần nhớ từ bản lưu cục bộ |
| Lõi chung tách **sự kiện chép** với **sự kiện nhớ**: sự kiện chép (`typing-*`) không đẩy độ thuộc quá 60 | Gõ chép không phải bằng chứng đã thuộc; Smart Review đang tin nó | Game vẫn đúng nhờ mục 6.3, nhưng Smart Review của portal coi từ là đã thuộc sớm |
| Cờ `sensitive`, `mature` trong `shared/vocabulary`, có test | Lọc từ (mục 6.1) cho mọi game | Game dùng danh sách chặn riêng, có test |
| Portal gọi focus cho iframe khi nạp game và khi nhận `typing-game:request-focus` | Phím đầu tiên đang rơi vào trang portal (06 §2) | Lớp "bấm để bắt đầu" trong game |
| Thêm `dragon-hold` vào Smart Review (adapter `dragon-hold-review-dataset.mjs`), giọng nói portal | Danh sách game đang gắn cứng | Lát C4–6 (DESIGN.md §9) |

## 7. Cổng kiểm bằng bot

Bot gõ chạy trên mô phỏng tất định (60 Hz, seed). Ải không đạt thì không phát hành.

**Bảng cổng duy nhất: 00 §7** (G1–G22: bot, mức khó, phạm vi ải, ngưỡng). Các cổng sinh ra từ tài liệu này: G7 chuẩn thắng ẩu, G9 không ngộp, G10 đọc được, G11 không mất công gõ, G12 học (gồm "không từ mới nào lên ≥ 70 trong ải đầu gặp nó"), G16 Long Nộ.

## 8. Câu hỏi cho chủ dự án (đã có mặc định)

| # | Câu hỏi | Mặc định nếu không trả lời |
|---|---|---|
| 1 | Tên: Rồng Giữ Ải, id `dragon-hold`? | Đã chốt theo mặc định (00 D01) nếu không phản đối trước M0 |
| 2 | Cho thêm clip Hit, Down, Rise cho `draconis-v4` (Bạch Long) bằng công cụ Blender có sẵn, trên lưới và rig sẵn có, không dựng lại model? | Đồng ý. Trước khi có clip: chớp sáng shader và Guide_Bow |
| 3 | Tối Thượng Viêm Đế đổi tạm sang `draconis-v3` (bốn chân, Spit, Spit_Big) được không? | Được. Bài thử hình trông vụng thì giữ v2 và dùng Cast |
| 4 | Chỉ gõ không lỗi (e = 0) mới tính "đúng" trong sự kiện học, giống Space? | Giữ như Space |
| 5 | Bạch Long làm người dẫn ở ải 1–10, vào trận từ ải 11? | Đồng ý (00 D21) |
| 6 | Sau bản đầu có thêm Tướng khác ngoài hai Rồng (Tripo từ ảnh 2D)? | Có, sau bản đầu. Mỗi Tướng mới thay một trong hai ghế, cùng luật Long Nộ |
| 7 | Có chế độ nói (Voice / Hybrid như Space) cho game này? | Không ở bản đầu. Kiến trúc để ngỏ |
| 8 | Cho "Thử lại từ đợt trước" 1 lần mỗi lần chơi ải (tối đa 2 sao)? | Cho |
