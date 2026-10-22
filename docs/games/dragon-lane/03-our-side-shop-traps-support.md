# Rồng Giữ Ải — 03. Phe ta: cửa hàng, bẫy, nhà phép, lính chặn, chỉ số

Ngày 23/10/2026. Game **Rồng Giữ Ải** (`dragon-hold`). Tài liệu này chốt mọi thứ của **phe ta**: tiền trong ải, cửa hàng, trang bị Rồng, thuốc và đồ tiêu hao, bẫy, nhà phép, lính chặn và người hỗ trợ, cách gõ chạm vào chúng, chỉ số chung, trạng thái, ma trận khắc chế.

**Số chuẩn, công thức sát thương, bảng phím, cổng bot: `00-canon.md`.** Khi lệch: 00 thắng, rồi tài liệu chủ của hệ (00 §1). Chiêu của hai Rồng: 01. Quái, tướng, boss: 02. Ải, tiến trình: 04.
Giữ luật nền của Typing Defense (TD): mô phỏng tất định 60 Hz, máu và tiền là số nguyên, RNG theo seed; chữ cái a–z chỉ để gõ, không làm phím tắt; kết quả từ dùng tên chung Chớp / Hoàn hảo / Tốt / Vừa / Ẩu. Nguồn nghiên cứu: `research/market.md`, `research/codebase-and-split.md`, `research/art-pipeline.md`.
Bản sửa 23/10: bỏ chí mạng, đòn gõ loại Chữ, Vàng theo ngân sách ải, trang bị cố định cho bản đầu, ma trận khắc chế và 5 món mới, phím Mac, giảm quá tải trong đợt.

## 0. Bản chốt
### 0.1 Mười luật khóa của phe ta
1. **Gõ là nguồn sát thương chính.** Rồng gây 65–80 % tổng sát thương lên quái. Bẫy, nhà, lính chủ yếu **khống chế và giữ**.
2. **Ít "sát thủ".** Chỉ 2 thứ tự gây sát thương đều: Thợ Săn Cú và Tháp Canh, cả hai yếu và chuyên quái bay. Bẫy nổ có, nhưng dùng một lần rồi nạp lại.
3. **Không có dòng chữ riêng cho nhà và bẫy.** Gõ lên quái tự nạp bẫy và nhà gần đó (Cộng Hưởng, mục 10). Chỉ bẫy lớn có **Từ Kích** tùy chọn, trong trần chữ của 00 §5 (C1–3: chế độ Tự, không có Từ Kích).
4. **Bẫy, nhà, lính đặt vào ô có sẵn** của bản đồ (`slots`: `trap`, `house`, `block`). Không đặt tự do. Dễ đọc, dễ cho bot, dễ kiểm bản đồ.
5. **Bộ Mang Theo:** 6 món đầu game, 8 món từ ải 21, tối đa 10. Chọn trước ải sau khi xem thẻ báo đợt.
6. **Lúc nghỉ đợt: đủ việc** (đặt, nâng, bán, dời, mua). **Trong đợt (giảm quá tải):** C1–C5 chỉ dùng đồ tiêu hao và sửa nhà; từ C6 thêm "đặt nhanh" tối đa 1 món mỗi đợt (dựng 2 s). Không nâng, không bán, không dời trong đợt. Giá không đổi.
7. **Giá trong ải không đổi theo chương.** Sức phe ta nhân g(c) theo chương (00 §4.1); người chơi mạnh thêm bằng cấp món, trang bị và Thư Viện Rồng (ngoài ải).
8. **Ba tiền:** Vàng (trong ải), Tri Thức (ngoài ải, từ việc học), Vảy Rồng (ngoài ải, từ chiến thắng). Không tiền thật, không gacha.
9. **Khống chế có giảm dần** trên cùng một quái, và quái lớn kháng một phần. Không có khóa chết vĩnh viễn.
10. **Bot quyết số** theo bảng cổng 00 §7.

### 0.2 Số chính (trỏ về 00)
| Thứ | Số |
|---|---|
| Hỏa lực P của Hỏa Long | 100 ở C1, nhân g(c) (00 §4.1). 1 W = 90 × g(c) máu |
| Hệ số kết quả từ | 00 §4.2: Chớp ×1,25 · Hoàn hảo ×1,10 · Tốt ×1,00 · Vừa ×0,90 · Ẩu ×0,60 |
| Chí mạng | **Không có** (00 D03). Trang bị, Long Ấn không cộng chí mạng |
| Giáp, Kháng | Giảm = G / (G + 100), trần 75 %. Bậc G0 / G1 / G2 / G3 = G 0 / 43 / 122 / 300 = 0 / 30 / 55 / 75 % |
| Vàng mỗi ải | Công thức 00 §4.9: 200 đầu ải + 900 × hệ số đường × hệ số loại ải; chia cho quái theo ĐĐ |
| Gọi đợt sớm | 2 Vàng mỗi giây còn lại, tối đa 40; +5 Long Nộ (00 §4.5) |
| Nghỉ đợt | 00 §4.5: Dễ chờ Enter · Thường 20 s · Khó 15 s |
| Nâng cấp | Cấp 2 = 70 % giá gốc · Cấp 3 = 100 % · Nhánh = 120 % |
| Bán | Hoàn 70 % tổng đã chi. Bán trong cùng lần nghỉ đã mua: hoàn 100 % |

### 0.3 Ma trận khắc chế (nguồn duy nhất)

Mỗi mã khắc chế của 02 có ít nhất một món hoặc kỹ năng ngoài gõ, mở **trước hoặc cùng chương** loài đầu tiên cần nó. `stages:validate` kiểm luật này (cổng G19). Ải 1–5 của C1 được miễn (đang dạy gõ).

| Mã | Món, kỹ năng (ải mở) | Loài, tướng cần sớm nhất |
|---|---|---|
| CHẶN | Vệ Binh Rêu (6) · Gấu Khiên Đá (C5) | E09 (C1) |
| CHẬM | Gai Chông (2) · Cột Chậm (C2) · Bùn Lầy (C2) | E10 (C2), E18 (C3) |
| GIAM | Lưới Dây Leo (C3) · Lồng Đá (C6) · Pháp Sư Dây Leo (C6) | E12, G02 (C3) |
| NỔ | Bom Hạt Thông (14) · Hạt Giống Nổ (C2) · Mìn Ấn (C4) | E11 (C2), E26 (C4) |
| ĐẨY | Gió Cuốn của Bạch Long (C2) · Cọc Bật (C7) | E14, E19 (C4) |
| LƯỚI | Lưới Phóng (13) · Gió Cuốn (C2) | E01 (C1 ải 12) |
| LỘ | Tháp Canh (C6) · **Đèn Đom Đóm** (C6, mới) | E05 (C7), E07, E23 (C9) |
| PHÁ-giáp | Gai Sắt, Lưới Gai (nhánh, từ C8) · Long Ấn Phá Vỏ (C2) | E12 (C3; có GIAM thay) |
| PHÁ-chữ | **Bùa Phá Chữ** (C3, mới) · Xung của Đài Khuếch Chữ (C5) | E13 (C3), G03 (C4) |
| CÂM | **Chuông Bạc** (C2, mới) · Lời Thề Bạch Vũ (C2) · Sét Câm (nhánh, từ C8) | G01 (C1 ải 5: miễn; có Ấn Phá), E15 (C5) |
| RUNG | **Trống Đất** (C4, mới) | E22 (C7), B18 |
| PHUN | Phun Lửa (3) · Thiên Hỏa (C2) | E25 (4), E01 |

## 1. Vai phe ta và ngân sách sát thương
| Nguồn | Vai | Tỉ lệ sát thương mục tiêu (bot Cân bằng 35 WPM) |
|---|---|---|
| Hỏa Long (đòn từ, chiêu) | Sát thương chính | 65–80 % |
| Bạch Long | Hỗ trợ: hồi, khiên, đẩy, tăng sức. Gần như không gây sát thương | ≤ 5 % |
| Bẫy | Nổ cụm, giam, làm chậm, kéo, đẩy | 12–25 % |
| Nhà phép | Hào quang, khiên, hồi, đánh dấu | ≤ 5 % (Tháp Canh) |
| Lính chặn, người hỗ trợ | Giữ đường, khiêu khích, hồi lính | ≤ 10 % |

- **Trần cứng:** sát thương không đến từ gõ ≤ 40 % tổng, đo theo từng ải. Vượt thì giảm số trong dữ liệu, không thêm luật.
- **Sàn cứng:** bot không gõ (mua đồ tối ưu) thua trước hết đợt 3 ở mọi ải. Ai không gõ thì không thắng.
- Phe ta làm người gõ chậm **sống sót**, không làm họ thắng thay. Giá trị của bẫy đo bằng **giây quái bị giữ**, không bằng số quái giết.

## 2. Mô hình chỉ số
### 2.1 Khối chỉ số chung
Mọi vật có máu (Rồng, quái, lính, nhà) dùng một khối chỉ số. Thiếu trường nào thì lấy mặc định.

| Chỉ số | id | Nghĩa | Ai có |
|---|---|---|---|
| Máu | `hp`, `hpMax` | Hết thì ngã (lính), Đổ Nát (nhà), thua (Hỏa Long) | Mọi vật |
| Khiên | `shield` | Máu tạm, bị trừ trước. Không hồi. Tối đa = 50 % máu tối đa | Mọi vật |
| Giáp | `armor` | Giảm sát thương Vật lý theo G / (G + 100) | Mọi vật |
| Kháng phép | `resist` | Như Giáp, cho sát thương Phép | Mọi vật |
| Tốc chạy | `speed` | m/s trên đường | Quái, lính |
| Tốc đánh, tầm | `attackRate`, `range` | Đòn mỗi giây; m (cận ≤ 1,5 m) | Quái, lính, nhà đánh |
| Sức nặng | `weight` | Nhỏ 1 · Vừa 1 · To 2 · Khổng lồ 3 · Boss: không chặn | Quái |
| Kiên định | `tenacity` | Giảm thời gian khống chế. Trần 80 % | Quái, Rồng, lính |
| Sức Chữ | `wordPower` | Hệ số đòn từ, gốc 1,0 | Rồng |
| Tư thế | `stance` | Đất · Bay thấp (≤ 3,5 m) · Bay cao | Quái |
| Thẻ | `tags` | Họ, cỡ, nguyên tố, `sapper`, `breaker`… | Quái |

### 2.2 Công thức sát thương
```
dmg  = round( base × g(c) × hệ_kết_quả × sức_chữ × (1 − giảm) × dễ_tổn_thương × hào_quang ), tối thiểu 1
giảm = G_hd / (G_hd + 100), trần 0,75          // đòn loại Chữ: giảm = 0
G_hd = max(0, G × (1 − phá_giáp) − xuyên)
```

- **Bốn loại sát thương (00 §4.2):** **Chữ** (đòn gõ, Long Hống, tia Viêm Đế, đòn lan của từ) không bị gì chặn, trừ khiên chữ. Vật lý (VL) bị Giáp chặn. Phép (P) bị Kháng phép chặn. Chuẩn (C) không gì chặn, chỉ dùng cho Độc.
- **Đòn từ của Hỏa Long luôn là loại Chữ.** Clip đổi theo khoảng cách (> 6 m Attack_L/R với cầu lửa; ≤ 6 m Attack_Both), số không đổi. Không có chí mạng ngẫu nhiên. Hệ quả: giáp là việc của bẫy, lính, nhà; Phá giáp làm quân ta đánh quái giáp dày tốt hơn.
- Nguyên tố (Lửa, Băng, Sét, Độc, Gió, Đất, Sáng) **không phải loại sát thương**. Chúng là thẻ gắn trạng thái và phản ứng (mục 2.4).
- Dễ tổn thương: Đánh dấu +15 %, trong Lồng Đá +20 %, cửa sổ phá thế của boss +50 %. Áp cho mọi loại, kể cả Chữ. Cùng nguồn không cộng; khác nguồn thì nhân. Làm tròn một lần ở cuối. Mọi RNG theo seed.
- **Luật bàn phím:** Rồng bị choáng thì đòn xếp hàng, hoãn tối đa 0,8 s, tối đa 3 đòn. Chữ đã gõ không bao giờ mất vì Rồng bị khống chế.

### 2.3 Trạng thái
| Trạng thái | id | Tác dụng | Cộng dồn | Tướng địch | Boss |
|---|---|---|---|---|---|
| Chậm | `slow` | −x % tốc chạy | Lấy mạnh nhất. Trần 60 % | Trần 45 % | Trần 30 % |
| Choáng | `stun` | Đứng, không đánh, ngắt niệm | Giảm dần | Theo Kiên định | Chỉ trong cửa sổ phá thế |
| Giam | `root` | Đứng, không đánh cận. Quái tầm xa vẫn bắn | Giảm dần | Theo Kiên định | Không |
| Đóng băng | `freeze` | Như Choáng. Bay thấp rơi xuống thành quái đất | Giảm dần | Theo Kiên định | Chỉ trong cửa sổ phá thế |
| Hạ Cánh | `grounded` | Bay thấp thành quái đất 3 s: bị chặn, ăn bẫy sàn | Không | 50 % thời gian | Không |
| Đẩy lùi | `knockback` | Lùi theo đường: quãng ÷ sức nặng | — | Khổng lồ ×0,25 | Miễn |
| Kéo | `pull` | Trượt về tâm bẫy | — | Như Đẩy lùi | Miễn |
| Cháy | `burn` | 5 P/s, 4 s | 3 lớp | Như thường | Như thường |
| Độc | `poison` | 6 C/s, 4 s, −50 % hồi máu | Lấy mạnh nhất | Như thường | Như thường |
| Ướt | `wet` | Mở phản ứng Sét, Băng. Lửa xóa Ướt | Làm mới | Như thường | Như thường |
| Dầu | `oiled` | −15 % tốc. Mở phản ứng Lửa | Làm mới | Như thường | Như thường |
| Đánh dấu | `mark` | +15 % sát thương nhận | Không | Như thường | Như thường |
| Phá giáp | `sunder` | Giáp ×0,5 | Không | Như thường | Như thường |
| Câm | `silence` | Không dùng kỹ năng, ngắt niệm, **tắt hào quang** | Không | Như thường | 50 % thời gian |
| Lộ diện | `reveal` | Hết tàng hình | Không | — | — |
| Khiêu khích | `taunt` | Buộc đánh nguồn khiêu khích | Không | 50 % thời gian | Miễn |

**Luật khống chế cứng** (Choáng, Giam, Đóng băng):
- Lần 2 trên cùng quái trong 10 s: ×0,6 thời gian. Lần 3: ×0,3. Sau lần 3: **Vững** 4 s, miễn khống chế cứng.
- Kiên định gốc: Nhỏ, Vừa 0 % · To 15 % · Tinh anh +15 % · Tướng địch 35 % · Boss 60 %. Hào quang tướng địch có thể cộng thêm (phần quái).
- Mỗi quái hiện tối đa 5 biểu tượng trạng thái. Thứ tự: khống chế, rồi dấu, rồi sát thương theo thời gian. Biểu tượng nằm **dưới** thanh máu, không che thẻ chữ.

**Trạng thái phe ta:**
- Tốt: Khiên (Vòm Khiên, Bạch Long, thuốc), Hồi (Nhà Thuốc Lá, Thầy Lang Nấm), Kiên Cố (+G), Hăng (+tốc đánh), Vững (miễn khống chế cứng), Thanh tẩy (xóa 1 hiệu ứng xấu).
- Xấu (từ quái): Cháy, Độc, Choáng (chỉ lính), Phá giáp, Câm (nhà tắt hào quang), Nguyền (−50 % hồi máu).

### 2.4 Phản ứng nguyên tố
| Phản ứng | Điều kiện | Kết quả |
|---|---|---|
| Điện Giật | Sét trúng quái Ướt | Sát thương Sét ×1,5, nhảy thêm 2 con. Hết Ướt |
| Băng Sâu | Băng trúng quái Ướt | Đóng băng ×1,5 thời gian |
| Bùng Cháy | Lửa trúng quái Dầu | Nổ 60 P trong 2 m, Cháy 3 lớp lên quái trong vùng. Hết Dầu |
| Vỡ Băng | Đòn VL ≥ 80 trúng quái Đóng băng | Đòn đó ×1,5, hết băng |

- **Sông của bản đồ** cho Ướt: quái lội qua sông bị Ướt 4 s sau khi lên bờ. Người chơi đọc bản đồ để đặt Cột Sét sau khúc sông.
- Mỗi nguyên tố một màu cố định cho vòng đất, hạt và biểu tượng: Lửa cam, Băng lam nhạt, Sét vàng tím, Độc xanh lá vàng, Gió trắng ngà, Đất nâu, Sáng vàng nhạt, Giam xanh rêu.

## 3. Tiền và kinh tế
### 3.1 Ba loại tiền
| Tiền | Ở đâu | Từ đâu | Dùng cho |
|---|---|---|---|
| Vàng | Trong ải, mất khi hết ải | Ngân sách ải (00 §4.9): hạ quái, hết đợt, gọi sớm, Học trước, Thẻ Ôn, biến cố; Giếng Vàng ngoài ngân sách | Bẫy, nhà, lính, nâng cấp, sửa, thuốc, Tim Rồng, Vảy Cứng, Lông Bạc |
| Tri Thức | Ngoài ải, giữ mãi | Chỉ từ học: từ mới gõ đúng, từ đến hạn đúng, Thẻ Ôn, Ải Ôn, Huy hiệu Học (00 §4.9) | Thư Viện Rồng (mục 12.2) |
| Vảy Rồng | Ngoài ải, giữ mãi | Sao ải lần đầu (3 / 5 / 8), boss (+20), Ải Tướng (+5), chơi lại (30 %) | Cấp món 1–5, trang bị cố định ở Xưởng Rồng, mở nhánh (giá ở 00 §4.9) |

- Tri Thức chỉ đến từ học: học tốt là đường mạnh lên chắc nhất, giống kế hoạch Sinh Tồn. Vàng dư cuối ải đổi Vảy = min(3; floor(Vàng dư / 100)). Không đáng để giữ Vàng.

### 3.2 Nguồn Vàng mục tiêu (bot Cân bằng)
Theo công thức 00 §4.9: hạ quái 60 % (chia theo ĐĐ, cụm bầy trả một lần) · hết đợt 25 % · gọi sớm, Học trước, biến cố 15 % · Giếng Vàng thêm tối đa 12 %. Vàng không tăng theo số đầu quái, nên bầy đông cuối game không làm ngập vàng. Cổng G13: Vàng mỗi ải trong ±15 % công thức.

### 3.3 Chống lăn cầu tuyết
- Không lãi suất. Giếng Vàng tối đa 1 cái mỗi ải, chỉ ra Vàng trong đợt. Nâng cấp kém hiệu quả dần: cấp 2 +45 % hiệu lực, cấp 3 +35 % nữa, nhánh +25 % và một tính chất mới.
- Hiệu ứng cùng loại không cộng dồn (hai Cột Chậm chồng vùng: lấy mạnh nhất). Trần chỗ tiêu là số ô của bản đồ.
- **Dựng tối đa theo bố cục** (mọi ô, cấp 3 = 2,7 × giá gốc): 1 đường (4 ô bẫy, 2 điểm giữ, 5 bệ nhà) ~3.100 Vàng; 4 đường (16 ô bẫy, 10 điểm giữ, 10 bệ) ~9.800 Vàng. Vàng ải chỉ đủ 15–35 % (00 §4.9): không bao giờ mua hết, phải chọn đường nào giữ bằng gì.

## 4. Cửa hàng
### 4.1 Khi nào mua gì
| Lúc | Mở gì | Ghi chú |
|---|---|---|
| Trước ải (Lều Chuẩn Bị) | Bộ Mang Theo (6–10 món), xem trang bị hai Rồng, 2–3 ô tiêu hao | Thẻ báo cả ải: đường nào, họ quái nào, có tướng địch, có boss. Món khắc chế đợt có viền sáng |
| Nghỉ đợt | Đủ cửa hàng: đặt, nâng, bán, dời (dời mất 10 %), thuốc, Tim Rồng, Vảy Cứng | Thẻ báo đợt kế. Đặt xong ngay. Một bảng mở tại một lúc (01 §1.2) |
| Trong đợt | C1–5: chỉ đồ tiêu hao (Alt + 7/8/9) và sửa nhà. Từ C6: thêm **đặt nhanh** 1 món mỗi đợt | Món mới dựng 2 s (thanh tiến trên ô). Không nâng, bán, dời. Không mở bảng lớn |
| Ngoài ải (Xưởng Rồng) | Cấp món, trang bị cố định bằng Vảy (mục 5) | Bản đầu không có Chợ Rừng (00 D08) |

- Cửa hàng trong ải **không ngẫu nhiên**, không đổi hàng. Mọi món trong Bộ Mang Theo luôn có.
- **Chợ Học đã gộp vào Thẻ Ôn** (01 §6.5, 00 D09): một thẻ, tối đa 3 câu, một mức thưởng.

### 4.2 Giao diện và phím
- Dải món dưới màn hình, theo Bộ Mang Theo; mỗi ô có biểu tượng, giá, phím số. Bấm ô trống trên bản đồ: vòng menu các món đặt được ở ô đó. Bấm món đã đặt: nâng, nhánh, Kích (Tự / Chữ), bán.
- **Phím: bảng 00 §6** (nguồn duy nhất). Tóm tắt: số 1…9 chọn món và vào chế độ đặt ở ô gợi ý; mũi tên đổi ô; Enter đặt; Esc hủy. Backquote (`` ` ``) vào chế độ sửa: mũi tên chọn món đã đặt, `=` nâng (bấm 2 lần), `-` bán (bấm 2 lần). Đồ tiêu hao: Alt + 7 / 8 / 9 (Linux: Shift). Không dùng Insert, PageUp, Delete, Tab cho việc đặt.
- Mọi việc có nút chuột tương ứng. Rê chuột lên món: vòng tầm trên đất, một dòng tác dụng, số trước và sau khi nâng.

## 5. Trang bị hai Rồng (bản đầu: trang bị cố định)

**Bản đầu (00 D08):** mỗi ô có 3 món cố định, không độ hiếm, không dòng phụ ngẫu nhiên, không rèn may rủi, không phân rã. Món thứ nhất của ô mở khi ô mở; món 2 và 3 mở khi thắng boss chương ghi trong bảng. Mua 40 Vảy; nâng cấp 2–5: 30 / 50 / 80 / 120 Vảy (00 §4.9). Đổi món đeo miễn phí ở Lều Chuẩn Bị. Không có chí mạng.

### 5.1 Ô và món

| Ô (mở) | Món 1 (cấp 1 → 5) | Món 2 | Món 3 |
|---|---|---|---|
| Vuốt (C1 ải 3) | Vuốt Đá: Sức Chữ +4 → +12 % | Vuốt Hổ Phách (C6): từ Chớp +10 → +30 % | Vuốt Bão (C12): từ Chớp làm Ướt quái trong 3 m, 2 → 4 s |
| Hỏa Châu (C1 ải 15) | Hỏa Châu Đỏ: chiêu Lửa +8 → +24 % | Hỏa Châu Lam (C8): Phun Lửa hồi nhanh 8 → 20 % | Tim Núi Lửa (C16): chiêu Lửa để lại Dầu 2 → 4 s |
| Vảy Giáp (C1 ải 17) | Vảy Sồi: Máu +80 → +240, Giáp +8 → +24 | Vảy Gai (C10): phản 10 → 25 % đòn cận chiến | Vỏ Rùa Cổ (C18): dưới 30 % máu, Khiên 15 → 25 % máu, 1 lần mỗi đợt |
| Nhẫn Lửa (C2) | Nhẫn Lửa: từ Chớp +6 → +18 % | Nhẫn Chuỗi (C7): Ẩu chỉ trừ 60 → 40 % Chuỗi | Nhẫn Nộ (C11): nạp Long Nộ +6 → +18 % |
| Trượng Lông (ải 11) | Trượng Lông: hồi và khiên +8 → +24 % | Trượng Gió (C9): Gió Cuốn đẩy thêm 1 → 3 m | Lông Bình Minh (C17): 10 từ Hoàn hảo liên tiếp, hồi 8 → 15 % máu mọi lính |
| Áo Lông (ải 11) | Áo Lông Kem: Máu +70 → +210, Kháng +8 → +24 | Áo Sương (C10): kiệt sức ngắn đi 2 → 5 s | Áo Bình Minh (C19): dậy với thêm 10 → 25 % máu |
| Thánh Thư (C2) | Thư Gió: hồi chiêu −4 → −12 % | Thư Lá (C8): Từ Trợ hồi thêm 10 → 25 % | Thư Cổ (C14): Lời Thề Bạch Vũ dài thêm 1 → 3 s |
| Nhẫn Gió (C3) | Nhẫn Gió: Kiên định phe ta +6 → +18 % | Nhẫn Mây (C9): Khiên Lông Vũ +10 → +25 % | Nhẫn Sao (C15): Bạch Long chặn thêm 1 suất (cấp 5) |
| Ngọc Chữ (C3) | Ngọc Kiên Nhẫn: từ mới gõ Hoàn hảo +15 → +30 % đòn, hồi 0,5 → 1 % máu | Ngọc Ôn Bài (C6): Từ Kích Hoàn hảo nạp lại bẫy ngay, 1 lần mỗi đợt mỗi bẫy | Ngọc Vững Tay (C12): Ẩu ×0,70 → ×0,80 thay vì ×0,60; Chớp chỉ ×1,15 |
| Bùa Rừng (C4) | Bùa Rêu: hiệu lực bẫy, lính, nhà +6 → +18 % | Bùa Rễ Mẹ (C15): lính ngã để lại rễ, Giam quái trong 2 m, 1 → 2 s | Bùa Mạch Đất (C20): bẫy hồi nhanh 5 → 15 % |

- Trang bị **không đổi model**. Chỉ đổi màu hạt chiêu và biểu tượng 2D.
- Ngọc Chữ không bao giờ làm từ khó đọc hơn, không đổi độ dài từ, không phạt nặng lỗi.
- Tổng: 30 món. Mỗi ô đeo 1 món, nâng hết 1 món mỗi ô = 3.200 Vảy (00 §4.9).

### 5.2 Giai đoạn sau (khi có số đo người chơi)

Độ hiếm (5 bậc), dòng phụ có trần, rèn +1 → +10, phân rã, Chợ Rừng, nội tại Huyền Thoại rơi ở Ác Mộng: **chỉ thêm sau bản công khai**, khi có đo lường cục bộ (06 §7) cho thấy người chơi muốn thêm chiều sâu. Khi thêm, mọi dòng phụ "chí mạng" đổi thành "Sức Chữ khi Chớp" và tổng sức vẫn nằm trong ngân sách mục 5.3.

### 5.3 Ngân sách sức mạnh ngoài ải
- Đường chuẩn g(c) (00 §4.1): bộ đồ trung bình ở C26 mạnh gấp 1,5 lần C1. Nguồn: Bậc Rồng ≤ +18 %, Cây Long Mạch nhánh Lửa ≤ +8 %, trang bị Vuốt ≤ +15 %.
- Cấp món 1–5: +6 % hiệu lực chính mỗi cấp (trần +24 %). Sức bẫy, nhà, lính còn nhân g(c) tự động, nên không yếu dần về cuối (cổng G8).
- Thư Viện Rồng (Tri Thức): ô, Vàng đầu, hồi giữa đợt (mục 12.2).
- Tài khoản nâng hết chỉ mạnh hơn bộ đồ trung bình tối đa 25 %, như TD 15.4.

## 6. Máu, giáp và đồ tiêu hao
### 6.1 Máu Rồng
- Hỏa Long là **mạng** của ải: hết máu là thua. Gốc 1.000 máu, Giáp 20, Kháng phép 20 ở chương 1.
- Bạch Long: 700 máu. Ngã thì kiệt sức 15 s, dậy với 40 % máu; trong lúc đó mất hỗ trợ (00 §4.5).
- Giữa hai đợt: hai Rồng hồi 10 % máu tối đa (Thư Viện, Long Ấn Tổ Ấm: tối đa 20 %).

### 6.2 Mua trong ải
| Món | Tác dụng | Giá | Giới hạn mỗi ải |
|---|---|---|---|
| Tim Rồng | +10 % máu tối đa Hỏa Long, hồi luôn phần tăng | 80 / 120 / 160 | 3 |
| Vảy Cứng | +15 Giáp Hỏa Long | 70 / 105 / 140 | 3 |
| Lông Bạc | +15 Kháng phép Hỏa Long | 70 / 105 / 140 | 3 |

### 6.3 Đồ tiêu hao
2 ô, ô thứ 3 mở bằng Thư Viện. Mỗi ô giữ tối đa 3 cái. Mua bằng Vàng trong ải, không mang sang ải sau.

| Món | Tác dụng | Giá | Hồi chung |
|---|---|---|---|
| Bình Máu Nhỏ | Hồi 25 % máu Hỏa Long trong 2 s | 30 | 8 s |
| Bình Máu Lớn | Hồi 50 %, xóa Cháy, Độc, Nguyền | 60 | 8 s |
| Thuốc Vảy Đá | +60 Giáp Hỏa Long 15 s | 40 | 8 s |
| Khiên Lá Sồi | Khiên 150 cho mọi lính và nhà 10 s | 50 | 8 s |
| Tù Và Gọi Rừng | 2 Vệ Binh Rêu tạm 15 s trên đường (đích mặc định: đường có quái gần tâm nhất) | 60 | 8 s |
| Bột Thời Gian | Mọi quái Chậm 40 % 4 s (boss 20 %) | 70 | 8 s |
| Hạt Giống Nổ | Ném bom 150 VL trong 3 m (đích mặc định: cụm đông nhất) | 50 | 8 s |
| **Bùa Phá Chữ** (mới, C3) | Ném vùng 4 m: phá 1 lớp khiên chữ của mọi quái trong vùng; quái mất khiên Choáng 0,5 s (mã PHÁ-chữ) | 45 | 8 s |
| **Lông Phượng** (mới, C2) | Tự kích khi Hỏa Long hết máu: dậy với 40 % máu, kèm một Long Hống miễn phí (01 §5). Tối đa 1 mỗi ải. Có Lông Phượng thì 3 sao chỉ khi không dùng nó | 150 | — |
| Pháo Hiệu Rồng | Một lần mỗi đợt. Hiện một Từ Khẩn trên Rồng: độ dài theo cột Từ Khẩn của 01 §3.4 (theo E), lấy từ đã học. Gõ xong: nổ 300 P trong 10 m quanh tâm, đẩy lùi 4 m. Ngòi = thời gian báo trước của 01 §3.6, tối thiểu 4 s; hết ngòi chưa xong thì tự nổ với 50 % sức (van an toàn như bom EMP của ZType). Chữ nằm trong trần 4 chữ không thuộc quái (00 §5) | 90 | 1 lần mỗi đợt |

## 7. Bẫy
### 7.1 Luật chung
- Đặt vào **ô bẫy** trên đường (`slots.kind = "trap"`). Mỗi đường 3–5 ô, cách nhau 5–7 m, không ô nào trong 8 m quanh tâm.
- Ba kiểu: **Sàn** (trúng quái đất, quái bị Hạ Cánh, quái bay bị Đóng băng rơi), **Trụ** (đứng bên đường, trúng cả bay thấp), **Ẩn** (quái không thấy, trúng con đầu tiên).
- **Một lần rồi nạp lại**, trừ Gai Chông và Bùn Lầy chạy liên tục. Vòng hồi hiện quanh bẫy.
- **Kích:** bẫy lớn có hai chế độ, đổi bằng vòng menu. **Tự**: kích khi đủ ngưỡng quái trong vùng. **Chữ**: hiện Từ Kích, gõ để kích, hiệu lực ×1,3 (mục 10.3). Mặc định **Tự tới hết C3** (00 D13); từ C4 mặc định Chữ. Người chơi đổi được mặc định trong cài đặt.
- **Quái phá bẫy** (thẻ `sapper`, phần quái) làm bẫy **Kẹt** 10 s, không phá hẳn. Hạ quái đó thì gỡ Kẹt ngay. Thợ Bẫy Sóc gỡ Kẹt một lần mỗi đợt. Đẩy và Kéo không đưa quái ra khỏi đường.

### 7.2 Danh sách bẫy
| # | Bẫy | id | Kiểu | Tác dụng cấp 1 | Vùng | Hồi | Giá | Kích |
|---|---|---|---|---|---|---|---|---|
| 1 | Gai Chông | `spikes` | Sàn, liên tục | Chậm 25 %, 8 VL/s | Dải 4 m | — | 50 | — |
| 2 | Bùn Lầy | `mire` | Sàn, liên tục | Chậm 40 %, Ướt | Tròn 4 m | — | 60 | — |
| 3 | Cọc Bật | `spring-log` | Sàn | Đẩy lùi 6 m ÷ sức nặng, Choáng 0,5 s | 2,5 m | 14 s | 70 | Tự |
| 4 | Mìn Ấn | `rune-mine` | Ẩn | 260 P lên con đầu tiên, 100 P quanh 2 m. Ưu tiên quái To | 2 m | 30 s | 80 | Tự |
| 5 | Lưới Phóng | `net-launcher` | Trụ | Bắn lưới quái bay thấp gần nhất: Hạ Cánh 3 s | 10 m | 15 s | 80 | Tự |
| 6 | Bom Hạt Thông | `pine-bomb` | Sàn | 120 VL, đẩy 2 m | 3 m | 22 s | 90 | Tự (≥ 3 quái) / Chữ |
| 7 | Nấm Độc | `spore-cap` | Sàn | Mây 6 s: Độc 6 C/s, −50 % hồi máu | 3 m | 20 s | 90 | Tự |
| 8 | Hố Gió | `gale-pit` | Sàn | Kéo quái trong 5 m về tâm 1,2 s | 5 m | 16 s | 100 | Tự (≥ 3 quái) / Chữ |
| 9 | Lưới Dây Leo | `vine-snare` | Sàn | Giam tối đa 4 quái 2,5 s | 3 m | 18 s | 100 | Tự |
| 10 | Ấn Băng | `frost-glyph` | Sàn | Đóng băng 2 s | 3 m | 26 s | 120 | Tự |
| 11 | Cột Sét | `storm-post` | Trụ | 70 P chuỗi 5 con, −15 % mỗi nhảy | Nhảy 4 m | 12 s | 130 | Tự (≥ 2 quái) / Chữ |
| 12 | Lồng Đá | `stone-cage` | Sàn | Giam 1 quái 4 s (kể cả To, tướng địch theo Kiên định). Trong lồng nhận +20 % đòn từ | 2 m | 35 s | 140 | Tự (quái nặng nhất ≥ Vừa) / Chữ |
| 13 | **Trống Đất** (mới) | `earth-drum` | Trụ | Mỗi lần rung vòng 4 m: quái đang đào bị lôi lên mặt đất (Lộ diện, Choáng 0,5 s); quái đất Chậm 20 % 1 s (mã RUNG) | 4 m | 10 s | 90 | Tự |

- Số trong bảng là ở C1; sát thương và máu nhân g(c) theo chương (00 §4.1), thời gian không đổi.

### 7.3 Nâng cấp và nhánh
- Cấp 2: +45 % hiệu lực chính (sát thương, thời gian, số quái). Cấp 3: +35 % nữa và −15 % hồi.
- Nhánh mở ở cấp 3, chọn 1 trong 2. Nhánh phải mở trước bằng Vảy ở Thư Viện (mục 12).

| Bẫy | Nhánh A | Nhánh B |
|---|---|---|
| Gai Chông | Gai Độc: thêm Độc 2 s | Gai Sắt: Phá giáp |
| Bùn Lầy | Nhựa Thông: thêm Dầu | Đầm Sâu: Chậm 55 %, quái To chậm thêm 10 % |
| Cọc Bật | Cọc Đôi: hai lần đẩy cách 1 s | Cọc Choáng: Choáng 1,5 s, không đẩy |
| Mìn Ấn | Mìn Chùm: 3 mìn nhỏ 120 P | Mìn Hút: kéo 3 m trước khi nổ |
| Lưới Phóng | Lưới Kép: 2 quái mỗi lần | Lưới Gai: Hạ Cánh + Phá giáp |
| Bom Hạt Thông | Bom Lửa: Lửa, Cháy 2 lớp | Bom Đất: Choáng 1 s, không đẩy |
| Nấm Độc | Nấm Mê: quái trong mây đánh nhầm nhau 2 s (không lên tướng địch) | Nấm Lan: mây đi theo đường 4 m |
| Hố Gió | Lốc Xoáy: kéo cả bay thấp | Hố Sâu: giữ ở tâm thêm 1 s (Giam) |
| Lưới Dây Leo | Dây Gai: 15 VL/s khi bị giam | Dây Hút: hồi 3 % máu lính gần khi giam |
| Ấn Băng | Băng Vỡ: hết băng thì nổ 80 P | Sương Giá: để lại vùng Chậm 30 % 5 s |
| Cột Sét | Sét Xích: 8 nhảy | Sét Câm: con đầu bị Câm 2 s |
| Lồng Đá | Lồng Đôi: 2 quái | Lồng Gương: quái trong lồng nhận +35 % đòn từ |

### 7.4 Chuỗi bẫy thiết kế sẵn
| Chuỗi | Thứ tự trên đường | Tại sao hay |
|---|---|---|
| Gom rồi nổ | Bùn Lầy → Hố Gió → Bom Hạt Thông | Chậm làm cụm dày, kéo gom, bom nổ cả cụm |
| Sông điện | Khúc sông → Cột Sét | Ướt từ sông làm sét ×1,5 và nhảy thêm |
| Đông rồi vỡ | Ấn Băng ở chỗ Rồng đánh vuốt (≤ 6 m) | Đòn vuốt VL ≥ 80 kích Vỡ Băng |
| Dầu và lửa | Bùn Lầy (Nhựa Thông) → chiêu Lửa của Hỏa Long | Bùng Cháy cả cụm |
| Kéo trời xuống | Lưới Phóng → Gai Chông → Vệ Binh Rêu | Quái bay thành quái đất, bị chặn và ăn bẫy sàn |
| Lồng cho tướng | Lồng Đá (Lồng Gương) cạnh Đài Khuếch Chữ | Tướng địch đứng yên, nhận đòn từ +35 % và +22 % |

## 8. Nhà phép và công trình hỗ trợ
### 8.1 Luật chung
- Đặt vào **bệ nhà** (`slots.kind = "house"`). Vòng trong 7–10 m quanh tâm: 4–6 bệ. Vòng ngoài 14–20 m, gần chỗ đường tách hoặc nhập: 2–4 bệ.
- Nhà có máu (600 ở cấp 1, +40 % mỗi cấp). Quái thẻ `breaker` và quái tầm xa có thể đánh nhà. Hết máu thì Đổ Nát: tắt, không mất. Sửa bằng 30 % giá đã chi, hoặc tự sửa 50 % khi hết đợt.
- Hào quang cùng loại không cộng; lấy mạnh nhất. Câm từ quái làm nhà tắt hào quang trong thời gian đó. Mỗi nhà có **Năng** (5 đèn lồng nhỏ, mục 10.2). Đủ đèn thì phát một **Xung**.

### 8.2 Danh sách nhà
| # | Nhà | id | Tác dụng cấp 1 | Xung (khi đủ Năng) | Vùng | Giá | Giới hạn |
|---|---|---|---|---|---|---|---|
| 1 | Cột Chậm | `slow-totem` | Chậm 20 % (cả quái bay) | Chậm 50 % 2 s | 8 m | 90 | — |
| 2 | Chuông Gió | `wind-chime` | Phe ta +30 % Kiên định | Thanh tẩy 1 hiệu ứng xấu cho mọi đồng minh trong vùng | 8 m | 100 | — |
| 3 | Tháp Canh | `watchtower` | Lộ diện tàng hình. Đánh dấu quái mạnh nhất mỗi 6 s. Bắn quái bay 12 VL/1 s | Đánh dấu 5 quái | 16 m | 110 | 2 |
| 4 | Giếng Vàng | `gold-well` | +4 Vàng mỗi 10 s trong đợt | +15 Vàng | 6 m (chỉ để nạp Năng) | 120 | 1 |
| 5 | Nhà Thuốc Lá | `herb-hut` | Hồi 1,5 % máu tối đa mỗi giây cho đồng minh (cả Rồng) | Hồi 10 % tức thì | 7 m | 120 | — |
| 6 | Lò Rèn Dã Chiến | `field-forge` | Bẫy trong vùng hồi nhanh 15 % | Nạp đầy bẫy hồi lâu nhất | 12 m | 120 | — |
| 7 | Đài Khuếch Chữ | `word-amp` | Quái trong vùng nhận +15 % đòn từ | +40 % trong 4 s | 10 m | 130 | — |
| 8 | Gốc Gọi Hồn | `revive-root` | Lính trong vùng hồi sinh nhanh 40 % | Hồi sinh ngay 1 lính ngã, kèm Khiên 150 | 12 m | 130 | — |
| 9 | Vòm Khiên | `shield-dome` | Mỗi 20 s: Khiên 150 cho đồng minh trong vòm | Vòm chặn đạn quái 3 s | 6 m | 140 | — |
| 10 | **Đèn Đom Đóm** (mới) | `firefly-lamp` | Lộ diện quái tàng hình trong vùng; chữ ẩn trong vùng hiện lại; Vùng Chữ không co trong vùng đèn (Đêm, Sương lan) (mã LỘ) | Lộ diện mọi quái trên đường gần nhất 4 s | 9 m | 80 | 3 |
| 11 | **Chuông Bạc** (mới) | `silver-bell` | Mỗi 12 s: Câm 2 s quái có hào quang hoặc đang niệm gần nhất trong vùng (mã CÂM; tướng địch 50 % thời gian) | Câm mọi quái trong vùng 2 s | 10 m | 110 | 2 |

- Gốc Gọi Hồn (tên cũ "Đền Gọi Hồn") vẽ thành gốc cây có nụ sáng, theo luật văn hóa TD 22.1.
- Đài Khuếch Chữ: Xung còn **phá 1 lớp khiên chữ** của mọi quái trong vùng (mã PHÁ-chữ).
- Cấp 2 / 3 theo luật 3.3. Nhánh ở cấp 3 (ví dụ Tháp Canh → Tháp Cú Đêm: thấy xa 22 m; hoặc Tháp Lửa Hiệu: đánh dấu kèm Phá giáp).
- Đài Khuếch Chữ đặt ở **bệ ngoài** để phủ một cửa đường. Đây là cách người chơi "tăng sức gõ" mà vẫn phải chọn hướng.

## 9. Lính chặn và người hỗ trợ
### 9.1 Luật chặn
- Đặt vào **điểm giữ** (`slots.kind = "block"`), 2–3 điểm mỗi đường. Lính đứng trong dây giữ 4 m quanh điểm.
- **Suất chặn:** quái dừng khi tổng suất chặn ≥ sức nặng của nó. Chưa đủ thì đi tiếp 50 % tốc. Quái bay và quái thẻ `phase` không bị chặn. Boss không bị chặn.
- Tối đa 3 quái đánh một lính. Lính đánh quái đang chặn nó trước. Lính hồi 4 % máu mỗi giây sau 3 s không bị đánh.
- **Ngã:** lính để lại một nụ cây, hồi sinh tại chỗ sau thời gian hồi sinh, đủ máu. Hết đợt: mọi lính hồi sinh ngay.
- Khiêu khích theo bảng 2.3. Tối đa 6 đơn vị (Thư Viện lên 8). Lính tạm từ Tù Và không tính.

### 9.2 Danh sách đơn vị
| # | Đơn vị | id | Vai | Chặn | Máu | Giáp / KP | Đòn | Kỹ năng | Hồi sinh | Giá |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Người Rơm Mồi | `straw-decoy` | Mồi | 1 | 260 | G0 / K0 | Không | Khiêu khích liên tục quái tầm xa trong 9 m. Ngã: rơm bay, Chậm 30 % 3 s trong 3 m | 10 s | 40 |
| 2 | Vệ Binh Rêu | `moss-warden` | Chặn | 2 | 450 | G1 / K0 | 12 VL / 1,2 s | — | 14 s | 70 |
| 3 | Thợ Bẫy Sóc | `squirrel-trapper` | Hỗ trợ bẫy | 0 | 180 | G0 / K0 | Không | Bẫy trong 8 m hồi nhanh 25 %. Gỡ Kẹt 1 lần mỗi đợt | 12 s | 80 |
| 4 | Thầy Lang Nấm | `mushroom-healer` | Hồi | 0 | 200 | G0 / K1 | Không | Hồi 30 máu mỗi 1,5 s cho lính thấp máu nhất trong 7 m | 14 s | 90 |
| 5 | Thợ Săn Cú | `owl-hunter` | Sát thủ chống bay | 0 | 240 | G0 / K0 | 16 VL / 0,8 s, tầm 12 m | Chỉ nhắm quái bay; không có quái bay thì bắn quái đất 50 % | 14 s | 100 |
| 6 | Pháp Sư Dây Leo | `vine-shaman` | Khống chế | 0 | 220 | G0 / K1 | Không | Mỗi 9 s: Giam 2 s một quái đang đánh lính (ưu tiên To) trong 8 m | 16 s | 110 |
| 7 | Gấu Khiên Đá | `stone-bear` | Chặn nặng | 3 | 1.000 | G2 / K1 | 20 VL / 1,5 s, quét 2 m | Mỗi 12 s: Khiêu khích quái đất trong 6 m, 3 s | 22 s | 150 |

- Thợ Săn Cú tối đa 2. Không có lính bắn đất chuyên dụng: đó là việc của Rồng.
- Cấp 2 / 3: +40 % máu, +25 % đòn, kỹ năng mạnh thêm. Nhánh ở cấp 3 (ví dụ Vệ Binh Rêu → Vệ Binh Gai: phản 15 % đòn cận; hoặc Vệ Binh Cổ Thụ: chặn 3, chậm hơn 30 %).
- **Mọi đơn vị cần model Tripo có rig và clip** Idle, Walk, Attack hoặc Skill, Death (Người Rơm: Idle, Death). Trúng đòn bằng phản ứng instanced. Gấu Khiên Đá và Thợ Bẫy Sóc rig bốn chân; còn lại rig hai chân. Lính vẽ bằng **đám đông có xương** như quái, không dùng `SkinnedMesh` (05 §8). Khi chưa có model: khối giữ chỗ đơn giản, chỉ trong hộp cát dev.
- Giáp, Kháng theo bậc (00 §4.2). Máu, đòn nhân g(c) theo chương.

## 10. Gõ phím chạm vào phe ta
### 10.1 Nguyên tắc
- **Làm:** gõ quái đứng gần bẫy và nhà thì chúng mạnh lên (Cộng Hưởng); Chuỗi gõ tốt tăng sức cả phe ta; bẫy lớn có Từ Kích tùy chọn, không tan, bỏ qua không phạt; Từ Kích lấy từ ôn, gõ là ôn bài.
- **Không làm:** dòng chữ riêng cho nhà như TD; gõ để mua, đặt, nâng; gõ để nạp mọi bẫy; chữ phe ta che chữ quái.

### 10.2 Cộng Hưởng
- Đòn từ trúng quái **đang đứng trong vùng** một bẫy đang hồi: bẫy đó −0,8 s hồi. Chớp hoặc Hoàn hảo: −1,2 s.
- Trần: Cộng Hưởng rút tối đa 50 % thời gian hồi gốc mỗi chu kỳ của bẫy.
- Đòn từ **hạ** quái đứng trong vùng một nhà: nhà +1 Năng. 5 Năng thì phát Xung (bảng 8.2), rồi về 0. Năng giữ qua đợt.
- Hệ quả: chọn mục tiêu là quyết định. Đánh quái trong vùng bẫy để nạp bẫy, hay đánh quái nguy hiểm đang ở chỗ khác.

### 10.3 Từ Kích
- Hiện trên bẫy ở chế độ Chữ, khi bẫy sẵn sàng và có ít nhất 1 quái trong vùng. Mặc định chế độ Tự tới hết C3 (00 D13).
- Từ 3–5 chữ, lấy từ **từ ôn đến hạn** hoặc từ đã thuộc (01 §6.2). Chữ đầu theo luật 01 §3.3.
- Thẻ chữ nhỏ hơn thẻ quái, viền xanh ngọc, icon bánh răng, không rung, không có đồng hồ. Gõ xong: kích ngay, hiệu lực ×1,3 (Hoàn hảo ×1,4). Sự kiện học `typing-skill` (01 §6.6). Không gõ: bẫy tự kích khi đủ ngưỡng của chế độ Tự, hiệu lực ×1,0. Không mất gì.
- Trần Từ Kích theo chương và trần chung 4 chữ không thuộc quái: **00 §5** (C4–5: 1; C6+: 2). Không đặt Từ Kích trên bẫy trong 10 m quanh Bệ Rồng (05 §4.3). Khi trên màn đã có ≥ 12 chữ quái: không hiện Từ Kích mới.

### 10.4 Chuỗi tăng sức phe ta
Chuỗi chung của trận, luật ở 01 §3.8 (đổi bậc theo kết quả từ; Ẩu chia đôi).

- Bậc 5: lính và nhà +5 % sát thương và hồi. Bậc 10: +10 %, lính hồi thêm 1 % máu mỗi giây. Bậc 20: +15 %, bẫy hồi nhanh 10 %. Bậc 40: +20 %, mỗi 10 s Khiên 50 cho mọi lính.
- Hiện bằng một vệt sáng chạy dọc các ô bẫy và bệ nhà, đổi màu theo bậc. Người chơi thấy phe ta "sáng lên" khi gõ đều.

## 11. Cộng hưởng giữa bẫy, nhà, lính và chiêu Rồng
Tên và số chiêu theo 01 §2.4. Mỗi chiêu mang một thẻ nguyên tố.

| Ghép | Cách chạy | Kết quả |
|---|---|---|
| Phun Lửa của Hỏa Long (Attack_Both, Lửa) + Nhựa Thông | Lửa trúng quái Dầu | Bùng Cháy |
| Gió Cuốn của Bạch Long (Guide_Flap, Gió) + Hố Gió | Gió đẩy quái về tâm hố | Cụm dày hơn cho Bom |
| Lời Thề Bạch Vũ (Guide_Talk, Sáng) + Gốc Gọi Hồn | Lính được tăng sức, hồi sinh thêm nhanh | Lính chặn gần như không vắng |
| Thiên Hỏa (Cast, Lửa) + Bùn Lầy | Lửa xóa Ướt, nhưng Nhựa Thông thì Bùng Cháy | Người chơi chọn nhánh bùn theo chiêu |
| Gấu Khiên Đá khiêu khích + Nấm Độc | Quái dồn quanh gấu, trong mây độc | Độc lên cả cụm |
| Người Rơm Mồi + Mìn Ấn | Quái tầm xa đi vào để bắn rơm | Mìn trúng quái To |
| Tháp Canh + tướng địch tàng hình | Lộ diện và Đánh dấu | Rồng gõ được và +15 % |
| Pháp Sư Dây Leo + Lồng Đá | Giam nối Giam (theo luật giảm dần) | Tướng địch bị giữ lâu ở vùng Đài Khuếch Chữ |

- Mọi ghép mạnh đều phải có **khắc chế** từ phần quái: quái miễn Ướt, quái `sapper`, quái bay, hào quang Kiên định, quái Câm nhà.

## 12. Mở khóa và tăng trưởng
### 12.1 Nhịp mở món (500+ ải, chương 20 ải)
| Khoảng ải | Mở |
|---|---|
Lịch này khớp lịch dạy 04 §6 và ma trận 0.3. Mỗi ải tối đa một ý mới.

| Khoảng ải | Mở |
|---|---|
| 1–20 (C1) | Gai Chông (ải 2), Vệ Binh Rêu (6), Bình Máu Nhỏ (7), Lưới Phóng (13, sau quái bay đầu tiên ở ải 12), Bom Hạt Thông (14), Nhà Thuốc Lá (16), Tim Rồng và Vảy Cứng (17) |
| 21–40 (C2) | Cột Chậm, Thợ Săn Cú, Bùn Lầy, Hạt Giống Nổ, **Chuông Bạc**, Pháo Hiệu Rồng, **Lông Phượng** |
| 41–60 (C3) | **Bùa Phá Chữ** (trước Yêu Rêu Khiên), Hố Gió, Người Rơm Mồi, Lưới Dây Leo, Lò Rèn Dã Chiến, Bình Máu Lớn |
| 61–80 (C4) | **Trống Đất**, Cột Sét, Thầy Lang Nấm, Vòm Khiên, Mìn Ấn, Khiên Lá Sồi, Thuốc Vảy Đá |
| 81–100 (C5) | Ấn Băng, Gấu Khiên Đá, Đài Khuếch Chữ, Nấm Độc, Bột Thời Gian, Tù Và Gọi Rừng |
| 101–120 (C6) | **Đèn Đom Đóm**, Tháp Canh, Lồng Đá, Pháp Sư Dây Leo, Thợ Bẫy Sóc |
| 121–140 (C7) | Chuông Gió, Gốc Gọi Hồn, Cọc Bật, Giếng Vàng, Lông Bạc |
| 141–300 (C8–15) | 26 nhánh cấp 3 (13 bẫy × 2), mỗi chương mở 3–4 nhánh bằng Vảy; nhánh nhà và lính theo cùng nhịp |
| 201+ | Lời Thề (04 §10); Vương Miện từ C3 |
| 301+ | Thử thách chơi lại (chỉ bẫy, không lính, 1 mạng); trang bị giai đoạn sau nếu đã thêm (mục 5.2) |

- Ô trang bị: theo bảng 5.1 (Vuốt ở ải 3, Bạch Long ở ải 11, Ngọc Chữ ở C3, Bùa Rừng ở C4).

### 12.2 Thư Viện Rồng (Tri Thức)

12 bậc, mở lần lượt, giá bậc k = 50 × 1,35^(k − 1) Tri Thức (00 §4.9). Tổng ≈ 5.100; người học đều (~25 Tri Thức mỗi ải) mở hết ở khoảng ải 200–250.

| Bậc | Giá | Mở | Bậc | Giá | Mở |
|---|---|---|---|---|---|
| 1 | 50 | Vàng đầu ải +20 | 7 | 303 | Ô Bộ Mang Theo 9 |
| 2 | 68 | Ô tiêu hao thứ 3 | 8 | 409 | Vàng đầu ải +60 |
| 3 | 91 | Vàng đầu ải +40 | 9 | 552 | Hồi giữa đợt 20 % |
| 4 | 123 | Hồi giữa đợt 15 % | 10 | 745 | Số đơn vị 8 |
| 5 | 166 | Số đơn vị 7 | 11 | 1.006 | Ô Bộ Mang Theo 10 |
| 6 | 224 | Thi lên cấp từ (04 §7.4) | 12 | 1.358 | Vàng đầu ải +100 |

- Ô Bộ Mang Theo 8 mở sẵn ở ải 21, không tốn Tri Thức.

## 13. Cân bằng bằng bot
### 13.1 Cách chạy
- Mô phỏng headless, tất định. Đích tốc độ và cách lấy mẫu (để một lượt kiểm chạy trong khoảng 45 phút trên 10 nhân, không phải hàng trăm giờ): **00 §8**. Lệnh `pnpm dh:balance` in báo cáo cho từng ải và từng món.
- Trước khi chạy sim, lọc giải tích tải gõ và Vàng theo công thức 00 §4.4, §4.9. Món và số chỉ sửa trong dữ liệu (`data/our-side/*.json`), không sửa mã.

| Bot | WPM | Chính xác | Chọn mục tiêu | Mua |
|---|---|---|---|---|
| Không Gõ | 0 | — | — | Tối ưu (tìm kiếm) |
| Chỉ Gõ | 35 | 95 % | Đe dọa cao nhất | Không mua gì |
| Chậm | 25 | 95 % | Gần tâm trước | Cân bằng |
| Cân Bằng | 35 | 95 % | Đe dọa cao nhất | Cân bằng |
| Nhanh | 60 | 97 % | Đe dọa + Cộng Hưởng | Cân bằng |
| Tham Bẫy / Tham Lính / Tham Nhà | 35 | 95 % | Như Cân Bằng | ≥ 60 % Vàng vào một nhóm |

- **Cách mua của bot Cân bằng:** mỗi lần nghỉ, chấm từng món theo "điểm hiệu dụng mỗi Vàng" với đợt kế (đọc thẻ báo đợt), chọn điểm cao nhất, giữ 10 % Vàng dự phòng cho thuốc.
- **Điểm hiệu dụng** (dùng cho lần định giá đầu): 1 sát thương = 1 điểm. 1 quái-giây bị Giam, Choáng, Đóng băng = 12 điểm. 1 quái-giây Chậm 40 % = 4 điểm. 1 quái-giây bị chặn = 8 điểm. 1 máu hồi hay khiên cho phe ta = 0,8 điểm. Giá cấp 1 đặt sao cho điểm mỗi Vàng của mọi món nằm trong 0,8–1,2 lần Gai Chông.
- Tìm kiếm bộ đồ: 50 thứ tự mua có ràng buộc, 3 seed, trên 2 ải đại diện mỗi chương; giữ 20 % tốt nhất (00 §8).

### 13.2 Cổng
**Bảng cổng duy nhất: 00 §7.** Các cổng sinh ra từ tài liệu này: G5 hỗ trợ cần thiết, G6 gõ là sức chính, G8 phần phe ta theo chương, G13 Vàng, G14 món, G15 khống chế, G19 khắc chế có trước. Thêm một cổng riêng: bot Cân Bằng gõ ≥ 50 % Từ Kích hiện ra và tải gõ không tăng quá 10 % vì Từ Kích.

## 14. Dữ liệu, mã và tài sản
- Mã của Rồng Giữ Ải: `src/sim/stats.ts` (khối chỉ số, công thức), `src/sim/status.ts` (trạng thái, giảm dần, phản ứng), `src/sim/traps.ts`, `src/sim/houses.ts`, `src/sim/units.ts`, `src/sim/shop.ts`, `src/sim/resonance.ts`. Viết mới theo kiểu dữ liệu TD. Không import `src/status/engine.ts` của Space Typing (gắn với tàu).
- Dữ liệu: `src/content/data/our-side/traps.json`, `houses.json`, `units.json`, `consumables.json`, `equipment.json` (trang bị cố định). Test dữ liệu: giá, hồi, vùng nằm trong khoảng; mỗi món có biểu tượng, âm, VFX, chuỗi mở, mã khắc chế; ma trận 0.3 khớp lịch mở.
- Sự kiện học: không có loại riêng. Từ Kích, Pháo Hiệu Rồng ghi `typing-skill`; Thẻ Ôn ghi `review-card` hoặc `meaning-recall` (nguồn duy nhất 01 §6.6).
- Tài sản cần (Codex vẽ 2D → Tripo): 13 model bẫy (không rig; clip mở, đóng làm trong Blender nếu cần), 11 model nhà (Đổ Nát bằng shader nứt), 7 đơn vị có rig hai chân hoặc bốn chân, ~90 biểu tượng 2D (cửa hàng, trang bị, trạng thái).
- Mỗi món có VFX đặt, kích, trúng, hồi xong (hạt instanced chép từ `vfx.ts`) và âm đặt, kích, trúng; mỗi đơn vị có âm đánh, trúng, ngã, hồi sinh. Bộ âm riêng của game.
- Không đưa ảnh, âm, model vào Git. Media đi Google Drive qua `pnpm media:push`.

## 15. Câu hỏi cho chủ dự án (đã có mặc định)
| # | Câu hỏi | Mặc định nếu không trả lời |
|---|---|---|
| 1 | Thua khi nào: Hỏa Long hết máu, hay có thêm "Tổ" ở giữa? | Hỏa Long hết máu là thua. Bạch Long ngã thì kiệt sức 15 s (00 §4.5) |
| 2 | Từ Kích mặc định? | Tự tới hết C3, Chữ từ C4 (00 D13). Không gõ thì bẫy vẫn tự kích, không phạt |
| 3 | Mua và đặt trong đợt? | C1–5 chỉ đồ tiêu hao và sửa; từ C6 "đặt nhanh" 1 món mỗi đợt, dựng 2 s |
| 4 | Thời gian nghỉ đợt ở mức Thường | 20 s, đồng hồ dừng khi có bảng mở (00 §4.5) |
| 5 | Trang bị có đổi hình Rồng không? | Không. Chỉ đổi màu hạt và biểu tượng. Đổi hình cần model Tripo riêng, để sau |
| 6 | Chỉ 2 "sát thủ" (Thợ Săn Cú, Tháp Canh), cả hai chuyên quái bay. Có cần thêm? | Không thêm. Gõ vẫn là sát thương chính |
| 7 | Thẻ Ôn (đã gộp Chợ Học) bật sẵn? | Bật, tắt được trong cài đặt |
| 8 | Tên món: tiếng Việt thuần, phong cách rừng như bảng trên? | Giữ, đổi được trong dữ liệu |
| 9 | Bản đầu dùng trang bị cố định (không độ hiếm, không dòng phụ ngẫu nhiên, không rèn may rủi)? | Có (00 D08). Thêm chiều sâu sau bản công khai nếu số đo cho thấy cần |
