# Rồng Giữ Ải — 04. Ải, bản đồ và tiến trình (23/10/2026)

> **Phạm vi:** thang ải, vùng đất và bản đồ 1–4 đường, mở khóa, độ khó theo vị trí ải, thư viện luật ải, sao, tiến trình lâu dài, kinh tế liên ải, chơi lại và vòng ngày, từ vựng theo ải, cách soạn ải bằng dữ liệu, kế hoạch sản xuất hình.
> **Khớp với:** 00 (số chuẩn, cổng bot), 01 (vòng chơi, sao, bộ từ mỗi ải), 02 (họ quái, tướng, boss, bộ sinh đợt), 03 (món phe ta, tiền trong ải, trang bị, lịch mở món), 05 (hình, kỹ thuật), 06 (lưu, màn ngoài trận, hướng dẫn người mới). Các chỗ lệch ở mục 13 **đã áp** vào 01–03 ngày 23/10.
> **Đã đọc thêm:** `research/*.md`; Space Typing `docs/survival/SURVIVAL_MODE_PLAN.md` (4.0), `docs/td/TYPING_DEFENSE_DESIGN.md` (15, 20, 21, 22.1); `shared/vocabulary` (100 cấp, 18.000 từ; 101 chủ đề chỉ phủ 1.177 từ); `shared/learning/README.md`.
> Tên Rồng theo 01: **Hỏa Long** (`heroes/draconis-v2`, Viêm Đế dùng `-v3`), **Bạch Long** (`guides/draconis-v4`). Giữa bản đồ là **Bệ Rồng**.

## 0. Tóm tắt
1. **520 ải = 26 chương × 20 ải** (như 01, 02), chia **3 Hồi**. Mùa sau thêm chương bằng dữ liệu; Mùa 2 (C27–30) đưa lên 600 ải.
2. **Chu kỳ 20 ải** theo 02, thêm **2 Ải Ôn** (9, 19) làm ải nghỉ: 364 thường, 52 Ải Tướng, 52 Ải Ôn, 26 boss nhỏ, 26 boss chương.
3. **Bản đồ là dữ liệu:** 16 mẫu bố cục (1–4 đường) + 8 kit vùng đất + biến thể + seed. Có **lớp Hắc Vụ** cho Hồi III và kit Khe Hắc Vụ cho C26. Mỗi kit có một **cơ chế chữ ký**.
4. **Mỗi ải một vẻ:** 5 ô luật (12 mục tiêu, 16 hiểm họa, 8 luật học, 8 luật quân, 10 biến cố) ghép theo ràng buộc. Script sinh, bot kiểm, khóa mã băm. 78 ải dựng tay.
5. **Độ khó** = thành phần đợt theo đe dọa của 02 × hệ số vị trí s(i) × loại ải, trong khi **tải gõ giữ trong dải** của 00 §4.4. Khó đến từ cơ chế; tốc gõ không phải đòn bẩy.
6. **Sao theo 01** (máu Hỏa Long). Thêm **Dấu Thách** (mục tiêu phụ) và **Huy hiệu Học** (01).
7. **Cấp Từ tách khỏi số ải.** Hồ sơ học chung chọn từ; ải chọn số lượng: 8 từ mới ở ải thường, 0 ở Ải Ôn. ~140 từ mới mỗi chương.
8. **Lâu dài:** Bậc Rồng 1–40, Cây Long Mạch (Sao), trang bị cố định và cấp món theo 03 (Vảy Rồng), Thư Viện Rồng (Tri Thức). Món mở theo lịch 03, không ngẫu nhiên, không rơi đồ ngẫu nhiên ở bản đầu.
9. **Mỗi ải độc lập.** Vàng không mang sang. Lần đầu thưởng đủ, chơi lại 30 %. Đường chính không cần cày.
10. **Sản xuất:** ~216 model Tripo (118 cảnh, 63 quái của 02, 31 món của 03, 4 nhà làng), ~750 ảnh Codex. Phát hành theo lát 3 chương; ải chỉ mở khi kit và quái của chương qua duyệt hình.

## 1. Khung Hành Trình
### 1.1 Ba Hồi
| Hồi | Chương | Ải | Vùng | Điểm nhấn |
|---|---|---|---|---|
| **I. Bìa Ngàn** | C1–10 | 1–200 | 8 kit, lần đầu ghé | Dạy mọi hệ. 2 đường từ C2, 3 từ C5, 4 từ C8 |
| **II. Lõi Ngàn** | C11–19 | 201–380 | 8 kit, biến thể mới (thu, bão, đêm, đông tuyết, mùa hoa) | Thống lĩnh, biến chủng, combo; Lời Thề |
| **III. Hắc Vụ** | C20–26 | 381–520 | 6 vùng Hắc Vụ + Khe Hắc Vụ | Luật Hắc Vụ mỗi chương, song boss, boss cuối B20 |

- Thời lượng theo loại ải: 00 §4.5 (ải thường 6–8,5 phút, ải boss chương 8–10 phút, Ải Ôn 3–4 phút). Một chương ~2–2,5 giờ; đường chính ~55 giờ.
- Màn Hành Trình là tranh vẽ Đại Ngàn Sương. Mỗi chương là một con đường 20 nút; nút có hình theo loại ải.

### 1.2 Chu kỳ 20 ải
| Ải | Loại | Nội dung | Số trong 520 |
|---|---|---|---|
| 1–4 | Thường | Dạy loài mới thứ nhất (02). Ải 1 dựng tay | |
| 5 | **Ải Tướng** | Đợt cuối có Đội trưởng; từ C11 có Thống lĩnh (02 mục 4.4) | 52 (cùng ải 15) |
| 6–8 | Thường | Trộn | |
| 9 | **Ải Ôn** | Ải nghỉ: đe dọa ×0,6, không từ mới, Tri Thức ×2 | 52 (cùng ải 19) |
| 10 | **Boss nhỏ** | Dựng tay. C1–4 Đội trưởng mạnh; từ C5 boss của chương c−3, bản rút gọn (02) | 26 |
| 11–14 | Thường | Loài mới thứ hai, combo | 364 thường cả thang |
| 15 | **Ải Tướng** | Như ải 5, đội hộ tống dày hơn | |
| 16–18 | Thường | Combo và luật ải; đỉnh chương | |
| 19 | **Ải Ôn** | Ôn từ của chương; **Lửa Trại**: xem trước đòn, pha, luật gõ của boss | |
| 20 | **Boss chương** | Dựng tay. B01–B19, song boss C20–25, B20 ở C26. Pha cuối có sát hạch từ (7.3) | 26 |

### 1.3 Mở khóa
- Thắng ải n mở ải n+1. Thắng boss chương mở chương sau. Thắng C10, C19 mở Hồi sau.
- Đường chính **không chặn bằng sao**. Thua thì chơi lại; giữ 30 % tiền đã kiếm (01 mục 5). Thua 2 lần liền: gợi ý hạ độ khó, đổi Bộ Mang Theo. Không ép.
- Ải đã qua luôn chơi lại được. Nút "Tiếp" luôn trỏ ải mới nhất.
- **Đường tắt** cho người đã quen: Ải Sát Hạch (dựng tay, nén mọi cơ chế đã dạy) sau C1 nhảy tới C4 (ải 61); Sát Hạch thứ hai nhảy tới C8 (ải 141). Nhận mọi món đã mở trên đường và trang bị bằng "bộ đồ trung bình". Ải bị bỏ qua vẫn mở để lấy sao, thưởng lần đầu.

## 2. Vùng đất
### 2.1 Tám kit và cơ chế chữ ký
| Kit (mã) | Chương (biến thể) | Họ hay gặp (02) | Cơ chế chữ ký | Chủ đề từ |
|---|---|---|---|---|
| Rừng thông có sông (`pine-river`, ảnh mẫu) | C1 xuân, C2 hè, C11 thu, C17 đông tuyết | Yêu Rêu, Thú Mục | **Cầu và suối:** cầu là điểm nghẽn; lội suối chậm 30 % và Ướt; lũ ngập cầu 10 s | nature.* |
| Rừng phép tím lam (`violet-glade`) | C3 sáng, C9 đêm, C18 mùa hoa | Nấm Ma, Sương Đen | **Nấm sáng:** gõ từ trên nấm để ru ngủ quái quanh nó 3 s | health.*, home.* |
| Đồng cỏ đồi (`hill-meadow`) | C4 hè, C13 bão | Thú Mục, Yêu Rêu | **Đồi và gió:** bệ nhà trên đồi +25 % tầm; gió đổi hướng mỗi đợt, quái bay xuôi gió +30 % tốc | food.*, everyday.* |
| Đầm lầy (`mire`) | C5 sương sớm, C12 đêm đom đóm | Thủy Quái, Nấm Ma | **Phục kích:** quái trồi từ nước gần bệ (bọt báo 3 s); bùn chậm lính chặn | people.*, education.* |
| Rừng mưa (`rainforest`) | C6 mưa, C14 đêm | Bọ Gai, Cánh Đêm | **Đường mọc:** dây leo mở, đóng lối theo đợt; thẻ đợt báo trước | shopping.*, transport.* |
| Hẻm đá đỏ (`red-canyon`) | C7 trưa, C16 đêm | Đá Rễ, Bọ Gai | **Đá lở:** gõ từ trên vách để thả đá chắn một đường 15 s | work.* |
| Bờ biển đá (`rock-coast`) | C8 hoàng hôn, C15 bão | Thủy Quái, Cánh Đêm | **Thủy triều:** đoạn ven biển ngập theo nhịp 40 s; quái lội chậm, Lươn, Cua nhanh hơn | travel.*, communication.* |
| Núi lửa (`volcano`) | C10 tro, C19 phun trào | Đá Rễ, Sương Đen | **Nham phun:** miệng nham phun theo nhịp 20 s, đốt cả hai phe | technology.*, society.* |

- Cơ chế chữ ký có ở ≥ 50 % ải thường của chương trong kit đó. Sau lần đầu, nó thành hiểm họa khách (5.3) ở kit khác.
- **Vật bản đồ mang chữ** (nấm sáng, vách đá lở, cổng ấn): tối đa 1 cùng lúc, tính vào trần 16 chữ sống, theo luật chữ đầu duy nhất của 01 mục 3.3. Không gõ thì không phạt.
- Theo luật văn hóa TD 22.1: không thần, không nơi thờ. Thành cổ, cầu đá, cối xay là mốc cảnh được.

### 2.2 Hồi III: Hắc Vụ
| Chương | Kit nền + lớp Hắc Vụ | Luật Hắc Vụ (02 mục 4.4) | Song boss (02) |
|---|---|---|---|
| C20 | Hẻm đá đỏ | Sương lan | B07 + B11 |
| C21 | Đầm lầy | Quái chết để vũng hồi máu 3 s | B05 + B12 |
| C22 | Rừng phép tím lam | Tướng hồi sinh một lần | B09 + B16 |
| C23 | Bờ biển đá | Thủy triều đổi đường mỗi 2 đợt | B08 + B15 |
| C24 | Núi lửa | Mưa tro tắt một bẫy mỗi 20 s | B10 + B13 |
| C25 | Rừng thông có sông (bản đổ nát) | Mọi tướng có Ấn | B14 + B19 |
| C26 | **Khe Hắc Vụ** (`mist-rift`, kit nhỏ) | Mọi thứ | B20 Mẹ Hắc Vụ |

- **Lớp Hắc Vụ** là tham số: sương tím theo bán kính, LUT xám lạnh, tán héo theo mặt nạ, 3 prop héo mỗi kit (cây chết, đá nứt, gốc mục). Không cần kit mới.
- Tổng vùng đất đường chính: 19 (kit × biến thể) + 6 Hắc Vụ + 1 Khe = **26**, mỗi chương một vùng. Thêm 1 biến thể chơi lại mỗi kit (đêm trăng hoặc tuyết) cho Ác Mộng, Ải Ngày, Tháp Rồng: **34 vùng đất**.

### 2.3 Biến thể đổi gì
- Không model mới: sắc tán (mặt nạ), LUT và giờ, sương, hạt, 2–4 ô đất, 1 tấm cỏ hoa, tuyết theo pháp tuyến (`research/art-pipeline.md` mục 9). Gần đường không dùng màu ngữ nghĩa (05 mục 2.2); lá thu đỏ để xa đường.

## 3. Bản đồ: 1–4 đường
### 3.1 Mười sáu mẫu bố cục
| Đường | Mẫu (mở từ) |
|---|---|
| 1 | `L1-thang`, `L1-s` chữ S dài (C1); `L1-xoan` xoắn nửa vòng quanh bệ (C1, ải 11) |
| 2 | `L2-doi` hai phía đối nhau, `L2-l` chữ L, `L2-tach` một cổng tách hai rồi nhập gần bệ (C2); `L2-cau` một nhánh qua cầu, một nhánh lội suối (C2, kit có sông) |
| 3 | `L3-t`, `L3-y` (C5); `L3-quat` quạt 120°, `L3-lech` ba cổng dồn một nửa bản đồ (C6) |
| 4 | `L4-thap` chữ thập, `L4-x` (C8, từ ải 11); `L4-chongchong` cong một chiều, `L4-haicap` hai cặp nhập thành hai (C10); `L4-vong` chạy vòng quanh bệ rồi vào (C13) |

- Mốc mở số đường theo 02 mục 5.5. Mỗi mẫu rung điểm theo seed trong hành lang cho phép; 16 mẫu × 34 vùng × seed đủ cho 520 ải không trùng hình.
- **Đường** là đường đất. Đường bay là lớp riêng (0–2 cung), gắn được vào mọi mẫu. Sông, cầu, đồi, vách là "dấu" địa hình (`research/art-pipeline.md` mục 2, 5).

### 3.2 Số đường theo chương
| Chương | Tỉ lệ ải 1 / 2 / 3 / 4 đường |
|---|---|
| C1 | 100 / 0 / 0 / 0 % |
| C2–4 | 30 / 70 / 0 / 0 % |
| C5–7 | 15 / 50 / 35 / 0 % (hẻm đỏ C7: thêm `L1-s` dài) |
| C8–14 | 10 / 35 / 35 / 20 % |
| C15–19 | 10 / 25 / 35 / 30 % |
| C20–26 | 5 / 25 / 35 / 35 % |

- Ải 1 của chương ít đường nhất chương. Boss chương 2–4 đường theo kịch bản. Không quá 3 ải liền nhau cùng mẫu.

### 3.3 Chỗ đặt quân
- Theo 03: bẫy, nhà, lính đặt vào **ô có sẵn** (`slots`: `trap`, `house`, `block`). Bản đồ sinh ô theo luật 03 (mỗi đường 3–5 ô bẫy, 2–3 điểm giữ; bệ nhà vòng trong 7–10 m, vòng ngoài 14–20 m).
- Dữ liệu bản đồ lưu thêm **vùng xây** và **vùng cấm**. Nếu chủ dự án chọn đặt tự do (ý 21/10 với Rift Defense), ô thành "điểm gợi ý" cho bàn phím và bot, không phải soạn lại 520 ải (Câu hỏi 3).

## 4. Độ khó tăng dần
### 4.1 Công thức
```text
Đe dọa đợt(c, i, w) = ĐĐ_đợt(c, w) của 02 mục 5.4 × s(i) × hệ số loại ải × hệ số mức khó (01 mục 5)
```

| i | 1 | 2 | 3 | 4 | 5 T | 6 | 7 | 8 | 9 Ôn | 10 B | 11 | 12 | 13 | 14 | 15 T | 16 | 17 | 18 | 19 Ôn | 20 B |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| s(i) | 0,85 | 0,88 | 0,90 | 0,93 | 1,00 | 0,93 | 0,95 | 0,97 | 0,60 | 1,05 | 0,98 | 1,00 | 1,02 | 1,05 | 1,10 | 1,05 | 1,08 | 1,10 | 0,60 | 1,20 |

- B_c của 02 tăng ~×1,085 mỗi chương, nên đầu chương sau ≈ 0,85 × 1,085 / 1,20 ≈ **77 % đỉnh chương trước**. Khớp răng cưa "≈ 75 %" của 02.
- **s(i) nhân đe dọa (thành phần), không nhân W gõ mỗi phút.** Tải đỉnh của từng ải: L_đỉnh(i) = 1,10 + 0,30 × (s(i) − 0,85) / 0,35, kẹp trong [1,10 ; L_đỉnh của chương ở 00 §4.8], trần cứng 1,40. Ải Ôn: tải ≤ 0,75 (00 §4.4).
- Số đợt, thời lượng: 00 §4.5. Toán, nhịp, quái sống, trần quái bay theo giai đoạn: 02 mục 5.3. Thuộc tính tinh anh, tướng mỗi đợt, combo, biến chủng: 02 mục 3.1, 6.1–6.3.

### 4.2 Đòn bẩy của tài liệu này
| Đòn bẩy | Bắt đầu | Tăng thế nào |
|---|---|---|
| Số đường | C1 | 1 → 2 (C2) → 3 (C5) → 4 (C8) |
| Cơ chế chữ ký, hiểm họa | C1 ải 14 | Hiểm họa bản địa; thêm 1 hiểm họa khách từ C11 |
| Luật học khó | C2 | Phủ 20 % quái; 30 % từ C11 |
| Luật quân | C4 | Tối đa 1 mỗi ải; khoảng 1 ải trong 4 |
| Mục tiêu khác "Giữ Vững" | C1 ải 17 | ~25 % ải thường ở Hồi I, ~40 % ở Hồi II–III |
| Ô luật bật cùng lúc (ngoài mục tiêu) | — | Tối đa 2 (Hồi I), 3 (Hồi II), 4 (Hồi III) |

### 4.3 Cổng bot của thang ải
- **Bảng cổng duy nhất: 00 §7.** Các cổng sinh ra từ tài liệu này: G2 không quá dễ, G17 thời lượng, G18 Ải Ôn là nghỉ, G21 đường cong, G22 Dấu Thách.
- **"Bộ đồ trung bình"** = tài khoản chỉ đi đường chính một lần, tiêu Vảy theo kịch bản mẫu, không chơi lại, không Lời Thề (00 §4.1).
- Không đạt thì chỉnh hệ số đe dọa của ải ±10 % trong dữ liệu, hoặc đổi seed. Không sửa mã.

## 5. Thư viện luật ải
### 5.1 Cách ghép
```text
Ải = Bố cục + Mục tiêu + [Hiểm họa] + [Luật học] + [Luật quân] + [Biến cố] + Đội quái (02) + Kế hoạch từ (01 mục 6.1; mục 7 ở đây)
```
- Thẻ ải ở Lều Chuẩn Bị (01 mục 1.2) ghi đủ: số đường, họ quái, luật, Dấu Thách, số từ mới. Không có luật ẩn.

### 5.2 Mục tiêu (12)
| Mục tiêu (mở) | Luật | Mục tiêu (mở) | Luật |
|---|---|---|---|
| Giữ Vững `hold` (C1) | Hạ hết đợt cuối (mặc định, 01) | Phá Tổ `nest` (C3) | Tổ ở cổng sinh liên tục; gõ chuỗi 3 từ dài để phá |
| Diệt Tướng `general` (C1, Ải Tướng) | Hạ tướng trước khi tới Bệ Rồng | Cứu Dân `rescue` (C3) | Dân bị nhốt dọc đường; gõ để thả; quái bắt dân thì mất thưởng |
| Hạ Boss `boss` (C1) | Kịch bản boss | Thắp Đèn `beacon` (C4) | Gõ thắp 3 đèn cổ; đủ 3 thì sương tan, đợt cuối yếu đi |
| Giữ Kho `granary` (C1 ải 17) | Kho cách bệ 8–12 m; mất kho là thua | Đua Trăng `moon` (C5) | Hạ đủ N quái trước khi trăng lặn |
| Giữ Cầu `bridge` (C2) | Cầu có máu; cầu sập mở lối tắt vào bệ | Săn Quái Vàng `gold-hunt` (C6) | Quái vàng chạy vòng rồi trốn; hạ đủ 3 |
| Hộ Tống `escort` (C2) | Xe dân đi ngang bản đồ; quái nhắm xe | Thu Linh Thạch `crystal` (C7) | Gõ để thu linh thạch trên đường trước khi quái nhặt |

### 5.3 Hiểm họa (16)
Mọi hiểm họa báo trước ≥ 3 s và **không che, không đổi chữ**. Chữ ẩn chỉ đến từ quái có mã ẩn chữ (02), luôn có cách LỘ. (N) = nặng: không đi cùng luật học khó.

| Hiểm họa (gốc) | Luật | Hiểm họa (gốc) | Luật |
|---|---|---|---|
| Lũ Suối `flood` (rừng thông) | Cầu ngập 10 s, quái đi bộ đổi đường vòng | Mưa Rừng `rain` (rừng mưa) | Tắt bẫy lửa; bẫy sét +50 % |
| Bào Tử `spores` (rừng phép) | Mây bào tử hồi 2 % máu/s cho quái; gõ nấm sáng để đốt | Thủy Triều `tide` (bờ biển) | Ven biển ngập theo nhịp 40 s |
| Sương Mù `fog` (rừng phép) | Thân quái ngoài 18 m mờ; chữ vẫn rõ | Đá Lở `rockfall` (hẻm đỏ, N) | Đá chặn một đường 15 s, quái dồn sang đường khác |
| Gió Lốc `wind` (đồng cỏ) | Quái bay xuôi gió +30 % tốc | Nắng Gắt `heat` (hẻm đỏ) | Lính chặn mất 1 % máu/s ngoài bóng đá |
| Cỏ Cháy `grassfire` (đồng cỏ, N) | Lửa lan trên cỏ khô, đốt bẫy gỗ và quái | Băng Trơn `ice` (biến thể đông) | Quái trượt +25 % tốc; Ấn Băng ×1,5 |
| Phục Kích `ambush` (đầm lầy, N) | Quái trồi từ nước gần bệ | Nham Phun `lava` (núi lửa, N) | Miệng nham phun theo nhịp 20 s |
| Bùn Sâu `mud` (đầm lầy) | Chậm lính chặn và quái đi bộ 30 % | Đêm Trăng `night` (biến thể đêm) | Chỉ thấy thân quái gần đèn và Tháp Canh; chữ vẫn rõ |
| Dây Mọc `vines` (rừng mưa) | Lối mở, đóng theo đợt | Cổng Ấn `portal` (Hồi III, N) | Quái chui cổng sang đường khác; gõ ấn đóng 15 s |

### 5.4 Luật học (8)
Luật học chỉ áp cho **20–30 % quái** có dấu riêng. Quái còn lại theo luật Chuẩn. Từ đặc biệt dùng tên của 01 mục 3.6.

| Luật | Quái mang gì | Gõ gì | Dữ liệu | Mở |
|---|---|---|---|---|
| Chuẩn | Từ; IPA, nghĩa theo độ thuộc (01 mục 6.3) | Từ | levels | C1 |
| Nghĩa | Từ Hỏi Nghĩa trên quái thường | Từ tiếng Anh | `vi` | C2 |
| Nghe | Từ Nghe: thẻ chỉ có loa | Từ nghe được | Giọng đọc | C3 |
| Phiên Âm | Chỉ IPA | Từ | `ipa` | C4 |
| Thiếu Chữ | Che 1–2 chữ cái, không che chữ đầu | Cả từ | levels | C5 |
| Chủ Đề | Từ chủ đề của chương phát sáng | Từ; +50 % vàng | topics | C6 |
| Từ Loại | Chỉ động từ nạp Năng cho nhà (03 mục 10.2) | Từ | parts-of-speech (~300 từ) | C9 |
| Cụm Từ | Tướng mang chuỗi 2–3 từ cùng chủ đề | Cả chuỗi | levels + topics | C11 |

- Nghe: tối đa 1 quái loa trên sân. Tắt tiếng thì tự đổi sang Phiên Âm. Từ Loại dùng rộng hơn khi `shared/vocabulary` có thêm dữ liệu.
- **Trên quái thường**, Nghĩa, Nghe, Phiên Âm luôn hiện **chữ đầu và số ô chữ** (ví dụ `b _ _ _`). Gõ như thường theo luật chữ đầu, nên không dò được gì bằng phím thử. Thử thách là nhớ phần còn lại. Ở boss (HN, NE) dùng ô trả lời riêng (01 §3.6).
- Đề bài theo luật 01 §3.6: nghĩa duy nhất trong bộ từ, loại nhóm đồng âm. Từ nhạy cảm không bao giờ vào (01 §6.1).

### 5.5 Luật quân (8) và biến cố (10)
| Luật quân (mở) | Luật | Biến cố | Luật |
|---|---|---|---|
| Ít Người (C4) | Tối đa 2 lính chặn | Thương Nhân Ghé | Gõ từ trên xe hàng: mua nhanh 15 s, giá −20 % |
| Cấm Nổ (C4) | Không bẫy nổ | Mưa Vàng | Gõ từ ngắn trên túi vàng để nhặt |
| Chỉ Bẫy (C6) | Không lính chặn, không nhà | Đồng Minh Rừng | Một thú rừng chặn giúp 1 đợt |
| Túi Cố Định (C6) | Không vàng từ hạ quái; vàng đầu ×2,5 | Quái Vàng | Mang từ hiếm, chạy ngang rồi trốn |
| Không Thuốc (C8) | Không mua máu, giáp trong ải | Tướng Lạc | Một Đội trưởng lang thang ra giữa đợt |
| Chợ Bẫy (C8) | Bẫy −40 % giá; nhà +40 % | Cơn Gấp | 20 s sinh gấp đôi, vàng ×2 |
| Một Vệ Binh (C10) | 1 lính chặn, máu ×3 | Sao Băng | Gõ từ dài để gọi sao băng nổ một cụm |
| Bộ Của Ải (C12) | Ải chọn sẵn 6 món | Rương Cổ, Lời Cầu Cứu, Nhật Thực | Gõ chuỗi chủ đề 3 từ mở rương · dân chạy về bệ, giữ họ sống · 20 s quái +1 bậc giáp, vàng ×2 |

- Biến cố: không trong 10 s đầu đợt, không hai cái cùng lúc, tối đa 1 mỗi ải.

### 5.6 Ràng buộc khi sinh
- 20 ải liền nhau không trùng bộ ba (mục tiêu, hiểm họa, luật học).
- **Chưa dạy thì chưa dùng** (`unlocks.json`). Mỗi ải tối đa 1 ý mới. Mỗi chương ≥ 1 thứ chưa gặp.
- Luật học khó (Nghĩa, Nghe, Phiên Âm, Thiếu Chữ) không đi cùng hiểm họa nặng, cũng không đi cùng luật quân.
- Ải boss: không hiểm họa, không biến cố ngẫu nhiên. Ải Ôn: không hiểm họa nặng, không luật quân, không Cơn Gấp.
- Hiểm họa khách tối đa 1 mỗi ải, từ C11. Hồi III cộng luật Hắc Vụ của chương, nên trừ 1 ô luật khác.
- Tổ hợp: 12 × 17 × 9 × 9 × 11 ≈ 180.000, chưa kể bố cục và đội quái. Đủ cho 520 ải và Mùa sau.

### 5.7 Sao, Dấu Thách, Huy hiệu Học
| Dấu | Điều kiện | Ải Ôn |
|---|---|---|
| Sao 1–3 | Theo 01 mục 5: thắng · Hỏa Long ≥ 50 % máu · ≥ 80 % và không Lông Phượng | Thắng · độ chuẩn ≥ 90 % · không hỏng từ nào hai lần |
| **Dấu Thách** | Mục tiêu phụ ghi trên thẻ ải | Mọi từ yếu được gõ đúng |
| Huy hiệu Học | Theo 01: độ chuẩn ≥ 90 % và mọi từ mới gõ đúng ≥ 1 lần | — |

- Đường chính có **1.560 sao**, 520 Dấu Thách, 520 Huy hiệu Học. Sao làm ngân sách Cây Long Mạch (8.2).
- Dấu Thách lấy từ danh sách: không lính chặn nào ngã; không dùng Pháo Hiệu Rồng; hạ tướng trong 20 s đầu; không bẫy nào bị Kẹt; thắng với ≤ 5 món; gọi sớm ≥ 3 đợt; không mua máu; không bỏ Từ Kích nào; gõ ≥ 5 Ấn Phá; giữ đủ dân.

## 6. Lịch dạy và mở
### 6.1 Chương 1 (ải 1–20): tối đa một ý mới mỗi ải

Bảng gồm cả hệ của Rồng (01), món (03), quái (02) và luật ải. **Hệ chưa mở thì không có chữ, không giữ chữ đầu, không có ô** (00 §5). Kịch bản lời dẫn của Bạch Long cho ải 1–6: 06 §5.

| Ải | Mở hoặc dạy | Ải | Mở hoặc dạy |
|---|---|---|---|
| 1 | Gõ từ → Hỏa Long ra đòn; khung học; Yêu Rêu Lính; 1 đường | 11 | **Bạch Long** vào trận, **Khiên Lông Vũ** (Alt + 3) |
| 2 | Bày binh và **Gai Chông** (bẫy đầu) | 12 | Quái bay đầu tiên: Ong Gai (đường trời) |
| 3 | **Phun Lửa** (Alt + 1, Chữ Chiêu); ô Vuốt | 13 | **Lưới Phóng** (kéo quái bay xuống) |
| 4 | Từ cụm bầy: Kiến Gai | 14 | **Bom Hạt Thông** (nổ cụm); cầu và suối (cơ chế chữ ký) |
| 5 | Ải Tướng: Yêu Rêu Cầm Cờ, hào quang, **Ấn Phá** | 15 | Ải Tướng: **Long Nộ, Viêm Đế** (Alt + 5); ô Hỏa Châu |
| 6 | **Vệ Binh Rêu** (lính chặn) | 16 | **Nhà Thuốc Lá** (nhà phép đầu) |
| 7 | **Bình Máu Nhỏ** (Alt + 7) | 17 | **Tim Rồng, Vảy Cứng**; ô Vảy Giáp; mục tiêu Giữ Kho; Dấu Thách đầu |
| 8 | Gọi đợt sớm (Shift + Enter) | 18 | **Từ Khẩn**, Long Hống |
| 9 | Ải Ôn đầu tiên: Học trước, Thẻ Ôn | 19 | Ải Ôn, Lửa Trại (xem trước boss) |
| 10 | Boss nhỏ: Đội trưởng mạnh (W 16, 02 §4.4) | 20 | Boss B01 Lợn Lòi Chúa Nanh Rêu |

- Chuỗi có từ ải 1, chỉ dạy bằng chú thích nhỏ ở ải 1–3. Không tính là ý mới.
- Ải 17 có ba món nhưng một ý: "mua máu, giáp cho Hỏa Long".

### 6.2 Từ chương 2
| Chương | Món mới (03 mục 12.1) | Hệ Rồng và học (01) | Thứ mới của thang ải và hệ khác |
|---|---|---|---|
| C2 | Cột Chậm, Thợ Săn Cú, Bùn Lầy, Hạt Giống Nổ, Chuông Bạc, Pháo Hiệu Rồng, Lông Phượng | Thiên Hỏa (ải 22), Long Ấn (ải 24), Gió Cuốn (ải 26), Từ Trợ (ải 28), Lời Thề Bạch Vũ và chọn giữa hai Tối Thượng (ải 35); ô Nhẫn Lửa, Thánh Thư | 2 đường; Bộ Mang Theo 8 ô; luật Nghĩa; Giữ Cầu, Hộ Tống |
| C3 | Bùa Phá Chữ, Hố Gió, Người Rơm Mồi, Lưới Dây Leo, Lò Rèn Dã Chiến, Bình Máu Lớn | Câu chọn nghĩa ở Thẻ Ôn; ô Ngọc Chữ, Nhẫn Gió | Kit rừng phép; luật Nghe; Phá Tổ, Cứu Dân; Vương Miện; Ải Ngày |
| C4 | Trống Đất, Cột Sét, Thầy Lang Nấm, Vòm Khiên, Mìn Ấn, Khiên Lá Sồi, Thuốc Vảy Đá | **Từ Kích** (mặc định Chữ); Cộng Hưởng hiện số; ô Bùa Rừng | Phiên Âm; luật quân; Gọng kìm (02) |
| C5 | Ấn Băng, Gấu Khiên Đá, Đài Khuếch Chữ, Nấm Độc, Bột Thời Gian, Tù Và Gọi Rừng | — | 3 đường; Thiếu Chữ; Rừng Vô Tận |
| C6 | Đèn Đom Đóm, Tháp Canh, Lồng Đá, Pháp Sư Dây Leo, Thợ Bẫy Sóc | **Đặt nhanh** trong đợt (03 §0.1) | Chủ Đề |
| C7 | Chuông Gió, Gốc Gọi Hồn, Cọc Bật, Giếng Vàng, Lông Bạc | — | Mọi mục tiêu đã mở |
| C8–10 | 3–4 nhánh cấp 3 mỗi chương | — | 4 đường (C8 ải 11); Từ Loại; Ác Mộng, Tháp Rồng, Boss Tuần (sau C10) |
| C11–15 | 3–4 nhánh mỗi chương | — | Hồi II: Thống lĩnh; Cụm Từ; hiểm họa khách; Lời Thề (ải 201); ô Rồng thứ 3 nếu có model |
| C16–19 | Món 3 của các ô trang bị (03 §5.1) | — | Biến chủng, combo ba loài (02) |
| C20–26 | — | — | Hồi III: luật Hắc Vụ, song boss, Cổng Ấn; ô Rồng thứ 4 nếu có model; B20 |

- Từ C8, cái mới mỗi 3–5 ải đến từ quái, tướng, combo, luật, kit; không chỉ từ món.

## 7. Từ vựng theo ải
### 7.1 Cấp Từ và dải cấp của ải
- **Cấp Từ** (1–100) lấy từ hồ sơ học chung. Ải quyết định **bao nhiêu** từ mới, từ ôn và luật học; hồ sơ quyết định **từ nào**. Từ đã gặp ở game khác của portal tính là đã gặp.
- **Dải cấp của ải** = [Cấp Từ − 3; Cấp Từ]. 01 mục 6.1 lấy từ "đang học", "đã thuộc" và từ bù trong dải này. Từ mới lấy ở mép chưa gặp của Cấp Từ.
- **Lên Cấp Từ** khi ≥ 85 % từ của cấp đã gặp và ≥ 60 % đạt độ thuộc ≥ 40. Một cấp ~181 từ ≈ 1,3 chương.
- **Chủ đề** của ải là chủ đề của kit (2.1). 101 chủ đề chỉ phủ 1.177 từ, nên chủ đề là gia vị: từ chủ đề lên tướng, quái vàng, luật Chủ Đề. Phần còn lại theo Cấp Từ.

### 7.2 Từ mới theo loại ải
| Loại ải | Từ mới (01: tối đa 2 mỗi đợt) | Ghi chú |
|---|---|---|
| Thường, Ải Tướng | 8 | Học trước ở Lều Chuẩn Bị (01 mục 6.5) |
| Boss nhỏ, boss chương | 6 | Từ mới chỉ ở đợt trước boss; boss dùng từ đến hạn và từ của chương |
| Ải Ôn | 0 | 70 % từ yếu của chương + từ đến hạn của hồ sơ; Nghe, Nghĩa, Phiên Âm xoay vòng |

- Một chương: 16 × 8 + 2 × 6 = **140 từ mới**. Người mới đi hết 520 ải với ~3.600 từ mới, tới khoảng Cấp Từ 20–24. Phần còn lại của kho cho Mùa sau, Ác Mộng, Ải Ngày và người học nhanh.
- **Nợ ôn:** hồ sơ có > 80 từ đến hạn thì từ mới mỗi ải còn 4. > 150 thì Ải Ngày hôm đó thành Ôn Ngày.
- Từ mới chỉ lên quái chậm, theo 01 mục 6.2. Học không làm thua.

### 7.3 Boss chương là bài sát hạch
- Pha cuối của boss chương dùng **từ mới của chương này** qua Từ Hỏi Nghĩa và Từ Nghe (01 mục 3.6, 02 cơ chế HN, NE). Luật chưa dạy thì pha đó dùng Chuẩn.
- Ải 19 (Lửa Trại) ôn đúng các từ boss sẽ hỏi: 5 từ khó nhất chương, nghe, xem nghĩa, gõ lại.
- Sai không thua ngay: đòn boss rơi xuống, như 01.

### 7.4 Nhảy cấp
| Cách | Làm gì | Kết quả |
|---|---|---|
| **Bài xếp lớp** (lần đầu, tùy chọn, 4 phút) | 40 từ từ cấp 1–100, chọn kiểu tìm nhị phân | Đặt Cấp Từ ban đầu. Không bỏ qua ải |
| **Thi lên cấp** (Thư Viện Rồng, 1 lần mỗi ngày) | 30 từ của 5 cấp kế, gõ theo nghĩa | ≥ 85 % thì Cấp Từ +5 |
| **Đường tắt** | Ải Sát Hạch (1.3) | Nhảy ải, không nhảy Cấp Từ |

## 8. Tiến trình lâu dài
### 8.1 Bậc Rồng (ngoài ải)
"Cấp Rồng" 1–10 trong ải là của 01 mục 2.5. **Bậc Rồng** là cấp tài khoản của đôi Rồng, giữ mãi.

```text
XP cần (b → b+1) = 400 + 120·(b − 1)                          // tới bậc 40: 104.520
XP mỗi ải        = (60 + 6·(c − 1)) × m_loại × (0,8 + 0,1·sao)  // c: chương; chơi lại ×0,3
m_loại: Thường 1 · Ải Tướng 1,5 · Boss nhỏ 2 · Boss chương 3 · Ôn 0,8
```
- Đi một lần: hết C3 ~bậc 7, hết Hồi I ~17, hết Hồi II ~28, hết C26 ~36. Bậc 40 nhờ chơi lại và Ải Ngày.
- Mỗi bậc: +1 % máu hai Rồng, +0,5 % Sức Chữ. Mỗi 3 bậc mở 1 Long Ấn mới (12 → 24, như 01). Bậc 10, 20, 30, 40: màu áo, câu thoại, khung tên.
- **Rồng thêm:** 01 để sau bản đầu. Ô Rồng thứ 3 mở ở đầu Hồi II, thứ 4 ở đầu Hồi III, chỉ khi có model Tripo (Câu hỏi 5).

### 8.2 Cây Long Mạch (Sao)
- 5 nhánh, chỉ về hai Rồng (không chồng Thư Viện Rồng của 03): **Lửa** (đòn từ, Phun Lửa, Thiên Hỏa), **Vảy** (máu, giáp Hỏa Long), **Lông** (khiên, hồi của Bạch Long), **Nộ** (Long Nộ, Tối Thượng), **Chữ** (Chuỗi, Chớp, Từ Khẩn).
- Mỗi nhánh 7 bậc, mỗi bậc chọn 1 trong 2. Giá bậc k = 10 + 6·(k − 1) Sao → 196 mỗi nhánh, **980 cả cây** (63 % số sao).
- Sao không bị tiêu: cây dùng tổng sao đã có làm ngân sách. Đặt lại miễn phí. Trần cả cây +15 % hiệu dụng.

### 8.3 Trang bị và món: mở ở đâu (bản đầu, không rơi ngẫu nhiên)
Bản đầu dùng trang bị cố định (03 §5, 00 D08). Không có rơi đồ ngẫu nhiên.

| Nguồn | Mở gì |
|---|---|
| Lịch ô (03 §5.1) | Món 1 của mỗi ô, khi ô mở |
| Boss chương ghi trong bảng 03 §5.1 | Món 2 hoặc 3 của một ô: mở để mua ở Xưởng Rồng bằng Vảy |
| Ải Tướng lần đầu | +5 Vảy (00 §4.9) |

- **Sổ Trang Bị** hiện mọi món, món chưa mở hiện bóng và nơi mở.
- **Cấp món** (1–5, Vảy Rồng, 00 §4.9): trần theo Hồi: Hồi I ≤ 3, Hồi II ≤ 4, Hồi III ≤ 5.
- Rơi đồ ngẫu nhiên, độ hiếm, Huyền Thoại ở Ác Mộng: giai đoạn sau (03 §5.2).

### 8.4 Làng Rồng và ngân sách sức mạnh
| Nơi | Tiền | Làm gì |
|---|---|---|
| Hang Rồng | XP, Sao | Bậc Rồng, Cây Long Mạch, Long Ấn đã mở |
| Thư Viện Rồng (03 §12.2) | Tri Thức | 12 bậc: ô Bộ Mang Theo, ô tiêu hao, số đơn vị, Vàng đầu, hồi giữa đợt; Sổ Từ, Thi lên cấp |
| Xưởng Rồng (03 §5) | Vảy Rồng | Cấp món 1–5, nhánh, trang bị cố định |

- Bậc Rồng (+18 % Sức Chữ ở bậc 36, +39 % máu ở bậc 40) và Long Mạch (+15 %) **nằm trong** đường g(c) của 00 §4.1. Không có Chợ Rừng, Lò Rèn ở bản đầu (00 D08).
- Màn và đường đi giữa các nơi trong Làng Rồng: 06 §4.
- Tài khoản nâng hết mạnh hơn "bộ đồ trung bình" ở cùng ải tối đa 25 % (03). Sức gõ và cách đặt quân vẫn quyết định.

## 9. Kinh tế liên ải
| Tiền | Mang sang? | Nguồn theo thang ải | Ghi chú |
|---|---|---|---|
| Vàng | **Không** | Trong ải (03 mục 0.2, 3) | Dư cuối ải đổi điểm và tối đa 3 Vảy (03) |
| Vảy Rồng | Có | Sao lần đầu 3 / 5 / 8 (03); boss +20 (03); **Ải Tướng +5; Ải Ngày ×2; Lời Thề +10–100 %** | Chơi lại 30 % (03). Thua: giữ 30 % (01) |
| Tri Thức | Có | Học (03); **Ải Ôn ×2; Huy hiệu Học +5; Ôn Ngày ×2** | Trần mềm 300 mỗi ngày, vượt ×0,25 (như TD 15.3) |
| XP, Sao | Có | Mục 8.1, 8.2 | Sao chỉ tính một lần mỗi ải |

- Đi một lần ước ~4.700 Vảy (520 ải × ~6,5 + 52 boss × 20 + 52 Ải Tướng × 5). Giá ở 00 §4.9: cấp món và trang bị cố định cộng lại 6.920 Vảy, nên số Vảy đủ cho ~68 %. Người chơi phải chọn lối chơi.
- **Đường chính không bao giờ cần cày:** cổng bot dùng "bộ đồ trung bình" (4.3).
- Không tiền thật, không hộp ngẫu nhiên trả phí. Ván bị cờ gian lận (TD 21.8) chỉ nhận thưởng gốc.

## 10. Chơi lại và vòng ngày
| Vòng | Mở | Luật | Thưởng |
|---|---|---|---|
| Sao, Dấu Thách, Huy hiệu | Ngay | Chơi lại lấy dấu còn thiếu | Vảy, Tri Thức, Sao |
| **Vương Miện** | C3; ải Tướng, boss đã 3 sao | Một thử thách cố định: Không Lính Chặn, Chỉ Bẫy, Túi Cố Định, Một Mạng | 104 Vương Miện; màu áo Rồng |
| **Lời Thề** | Ải 201 | 12 luật khó tự bật: quái +1 bậc giáp (+15 %), mỗi toán +1 con (+20 %), quái bay ×1,5 (+15 %), tướng +1 thuộc tính (+20 %), không thuốc (+15 %), nghĩa ẩn (+10 %)…; cấm cặp quá khó | Vảy, Tri Thức tới +100 % |
| **Ác Mộng** | Sau C10 | Chơi lại một chương ở biến thể chơi lại: đe dọa ×1,5, tinh anh +1 thuộc tính, boss thêm một cơ chế | Huyền Thoại (từ C16), Vảy ×2 |
| **Rừng Vô Tận** | C5 | Một bản đồ, đợt mãi; tướng mỗi 10 đợt, boss mỗi 30 | Kỷ lục, Vảy theo mốc |
| **Ải Ngày** | C3 | Ải sinh theo ngày, món đã mở; từ đến hạn + từ mới | Vảy ×2, Tri Thức |
| **Ôn Ngày** | Ngay | 3 phút ôn từ đến hạn của mọi game portal | Tri Thức ×2 |
| 3 việc ngày | C3 | Ví dụ: gõ đúng 30 từ ôn; hạ 2 tướng; giam 10 quái | Vảy |
| **Tháp Rồng**, **Boss Tuần** | Sau C10 | 50 tầng, luật đổi mỗi tuần · một boss với 3 Lời Thề cố định | Kỷ lục, Vảy, mảnh đồ |

- **Không phạt khi bỏ ngày.** Thưởng ngày dồn tối đa 3 ngày. Chuỗi ngày chỉ là con số. Nhắc nghỉ sau 30 phút (20 phút hồ sơ trẻ em). Chạy cục bộ; bảng xếp hạng để sau.

## 11. Dữ liệu và cách soạn
### 11.1 Tệp (theo cây thư mục 05 mục 9.5; JSON vào Git, media không)
```text
src/content/data/
  kits/*.json             8 kit + mist-rift: ô đất, prop, biến thể, lớp Hắc Vụ, cơ chế chữ ký, chủ đề từ, artApproved
  chapters/c01…c26.json   kit + biến thể, loài và tướng mới (02), món mới (03), luật mới, boss, ải dựng tay
  stages/c01/s01…json     520 ải đã sinh và khóa; *.override.json là phần sửa tay
  layouts/*.json          16 mẫu bố cục + hành lang rung
  rules/{objectives,hazards,learning,army,events,oaths}.json · unlocks.json · rewards.json
src/stages/               sinh ải, validate-map, mã băm bố cục
scripts/                  stages:gen · stages:validate · dh:balance · render-map-guide
```

### 11.2 Một bản ghi ải
```jsonc
{ "id": "c06-s12", "n": 112, "chapter": 6, "idx": 12, "type": "normal",
  "map": { "kit": "rainforest", "variant": "rain", "layout": "L3-y", "seed": 81231, "paths": 3, "air": 1 },
  "rules": { "objective": "hold", "hazard": "vines", "learn": "meaning", "army": null, "event": "merchant" },
  "challenge": "no-blocker-down",
  "enemies": { "budget": 1.00, "species": ["E28", "E03", "E21"], "generals": [], "flyerCap": 0.25 },
  "vocab": { "new": 8, "topics": ["shopping.stores"], "learnShare": 0.2 },
  "teaches": null,
  "lock": { "hash": "…", "bot": { "25": 0.71, "35": 0.82, "60": 0.98 } } }
```
- Bản ghi không chứa từ. Từ chọn lúc vào ải, từ hồ sơ học và RNG theo seed. Đợt sinh lúc nạp từ ngân sách + loài + seed (02), nên chạy lại giống hệt.

### 11.3 Quy trình
1. Người thiết kế (AI) viết 9 file kit, 26 file chương, `unlocks.json`.
2. `stages:gen` điền 520 ải theo 1.2, 3.2 và ràng buộc 5.6.
3. `stages:validate`: luật hình học (`research/art-pipeline.md` mục 5), luật ô của 03, luật ghép 5.6, lịch dạy.
4. `dh:balance`: bot của 01, 02, 03 và cổng 4.3; chỉnh hệ số ±10 % hoặc đổi seed.
5. Dựng tay 78 ải (1, 10, 20 mỗi chương): bố cục, đợt kịch bản, boss.
6. Chủ dự án duyệt ảnh khung (`render-map-guide`) và chơi thử ải dựng tay.
7. Khóa mã băm. Đổi dữ liệu thì chạy lại bước 3–7.

- **Cổng hình:** chương chỉ mở cho người chơi khi kit có `artApproved` (bài 3 góc × 4 hướng) và mọi loài, tướng, boss của chương có model có rig. Hình tạm chỉ dùng trong hộp cát của dev.
- **Lưu:** thiết kế đầy đủ ở **06 §1** (lớp, khóa, lược đồ, phiên bản và hàm chuyển, ảnh chụp sim ở đầu mỗi lần nghỉ để chơi tiếp, bản dự phòng, xuất và nhập, nhiều hồ sơ). Độ thuộc từ nằm ở hồ sơ học của portal.

## 12. Kế hoạch sản xuất nội dung
### 12.1 Mỗi kit
| Hạng mục | Ai làm | Số | Ghi chú |
|---|---|---|---|
| Ảnh nguồn cảnh (3 cây, 2 bụi, 3 đá, gốc cây, khúc gỗ, 2 mốc cảnh) | Codex | 12 | 3/4 cao 30°, ánh sáng phẳng, nền khóa màu |
| Cảnh 3D không rig | **Chủ dự án, Tripo** | 12 | Face limit 10.000 → Blender `--kind props` |
| Ô đất 8; decal, cỏ hoa 4 tấm; phông xa, trời, gợn nước hoặc nham 4 | Codex | 16 | Ô đất nhìn thẳng từ trên, liền mép |
| Mỗi biến thể thêm (ô đổi, tấm cỏ hoa, phông) | Codex | 6 | |
| Lớp Hắc Vụ: ảnh nguồn 3 prop héo + 3 prop Tripo + 4 ảnh tấm | Codex, **Tripo** | 7 + 3 | Chỉ 6 kit của Hồi III |
| Thẻ vùng, tranh nút trên màn Hành Trình | Codex | 2 | |

- Thứ tự: kit gốc → bài A/B cây (chỉ kit đầu) → biến thể → lớp Hắc Vụ khi tới Hồi III.

### 12.2 Tổng
| Nhóm | Tripo (chủ dự án) | Codex | Nguồn số |
|---|---|---|---|
| 8 kit gốc | 96 | 8 × 30 = 240 | 12.1 |
| 11 biến thể đường chính + 8 biến thể chơi lại | — | 19 × 6 = 114 | 2.1, 2.2 |
| Lớp Hắc Vụ (6 kit) + kit Khe Hắc Vụ | 18 + 4 | 6 × 7 + 20 = 62 | 2.2 |
| Quái, tướng, boss | 63 | ~130 (2 góc mỗi model) | 02 mục 7.2 |
| Bẫy, nhà, lính (13 + 11 + 7) | 31 | ~62 + ~90 biểu tượng | 03 mục 14 |
| Nhà Làng Rồng (Hang Rồng, Thư Viện Rồng, Xưởng Rồng, Cổng Hành Trình) | 4 | 8 | 8.4 |
| Màn Hành Trình, thẻ chương, Sổ Trang Bị | — | ~50 | 1.1, 8.3 |
| **Cộng** | **~215** (tính tạo lại ≈ 400 lượt) | **~750** (chưa tính tranh truyện của 05) | |

### 12.3 Lát phát hành
Mốc xây đầy đủ (M0…M8, cổng, làn song song): **DESIGN.md §9**. Bảng dưới chỉ là phần hình của từng lát.

| Lát (mốc) | Chương | Ải mở | Hình cần thêm |
|---|---|---|---|
| 0 (M0, bản thử dọc) | — | 1 bản đồ 2 đường, 10 đợt | Kit rừng thông có sông (xuân), bản rút gọn; 7 model quái (E09, E11, E18, E19, E01, E25, G01); 3 bẫy, 2 lính hoặc nhà |
| 1 (M2) | C1 | 20 | Đủ kit rừng thông; B01; món của ải 1–20 |
| 2 (M3) | C2–3 | 60 | Biến thể hè; kit rừng phép; 14 model đầu của 02 đủ |
| 3 (M4, **công khai đầu**) | C4–6 | 120 | Kit đồng cỏ, đầm lầy, rừng mưa |
| 4–5 (M5) | C7–10 | 200 | Kit hẻm đỏ, bờ biển, núi lửa; hết Hồi I |
| 6–7 (M6) | C11–19 | 380 | Biến thể Hồi II, Thống lĩnh, biến chủng |
| 8 (M7) | C20–26 | **520** | Lớp Hắc Vụ, Khe Hắc Vụ, B20 |

- Dữ liệu ải và cổng bot của mỗi lát xong trước hình của lát đó (chạy với hình hộp trong hộp cát). Hình quyết định nhịp phát hành.

## 13. Đối chiếu với tài liệu khác (đã áp ngày 23/10)
| Điểm | Chốt | Đã sửa ở |
|---|---|---|
| Ải Ôn ở ải 9, 19 | Có (ải nghỉ, không từ mới) | 01 §1.1; 02 §6.1; 00 §4.5 |
| Boss chương dùng từ mới | 6 từ mới ở đợt trước boss; pha cuối sát hạch từ của chương | 01 §6.1 (bộ từ), mục 7.3 ở đây |
| Bom Hạt Thông | Mở ở ải 14 (lịch dạy mới 6.1) | 03 §12.1 |
| Lời Thề, thử thách chơi lại | Lời Thề ải 201, Vương Miện từ C3 | 03 §12.1 |
| Quái bay đầu tiên | Ải 12 của C1; Lưới Phóng ải 13 | 03 §12.1, §0.3 |
| Tên id game | `dragon-hold` | 01 §6.6; 00 D01 |
| Tên có "Đền" | Bệ Rồng; Gốc Gọi Hồn | 02 §1.1; 03 §8.2 |
| Bạch Long vào trận | Ải 11 (không phải ải 6) | 01 §2.2; 00 D21 |

## 14. Câu hỏi cho chủ dự án (đã có mặc định)
1. **Số ải:** 520 ở bản đầy đủ đầu tiên, Mùa 2 lên 600? Mặc định: có.
2. **Ải Ôn** (ải nghỉ) ở ải 9 và 19 mỗi chương? Mặc định: có. Cách khác: chỉ ải 19.
3. **Đặt quân:** ô có sẵn (03) hay đặt tự do trong vùng (ý anh ngày 21/10 cho Rift Defense)? Mặc định: ô có sẵn; dữ liệu giữ vùng xây để đổi sau.
4. **Đường tắt** cho người quen (nhảy tới ải 61 và 141 qua Ải Sát Hạch)? Mặc định: có.
5. **Rồng thứ 3, 4** (đầu Hồi II, Hồi III) bằng model Tripo mới? Mặc định: ra mắt với 2 Rồng; để sẵn ô.
6. **Vật bản đồ mang chữ** (nấm sáng, vách đá lở, cổng ấn), tối đa 1 cùng lúc? Mặc định: có.
7. **Ngân sách Tripo** ~216 model (~400 lượt): làm theo lát 12.3, bắt đầu bằng 3 model mẫu duyệt hoạt ảnh (E09, E18, E01)? Mặc định: có. Anh cho biết số giờ Tripo mỗi tuần để lên lịch.
8. **Công khai đầu** khi đủ C1–6 (120 ải)? Mặc định: có.
