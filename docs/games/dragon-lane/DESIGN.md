# Rồng Giữ Ải (Dragonhold) — Tài liệu tổng (23/10/2026)

> **Dành cho:** chủ dự án (duyệt), các agent làm hình, mã, âm, cân bằng.
> **Trạng thái:** thiết kế đã qua một vòng phản biện đầy đủ và đã sửa. Chưa có mã.
> **Cách đọc:** tài liệu này là bản tổng, không có số riêng. Số chuẩn ở `00-canon.md`. Chi tiết từng hệ ở các file 01–06. Tách ba game ở `../SPLIT_PLAN.md`.

## 0. Một trang

**Rồng Giữ Ải** là game thủ ải gõ phím 3D, nhìn từ trên xuống một sa bàn rừng vẽ tay. Hai Rồng đứng trên Bệ Rồng giữa bản đồ. Quái của **Bầy Héo** tới đều theo đợt qua 1–4 đường đất và một đường trời. Mỗi quái mang một từ tiếng Anh trên đầu. Gõ đúng từ thì **Hỏa Long** phun lửa vào nó. **Bạch Long** che chắn, hồi máu, đẩy lùi. Giữa các đợt, người chơi mua bẫy, nhà phép, lính chặn, máu, giáp, đồ tiêu hao. Phe ta ít "sát thủ": phần lớn là giữ chân, giam, nổ cụm, tăng sức.

| Mục | Chốt |
|---|---|
| Thể loại | Thủ ải gõ phím, quái đi đường, nhân vật ở giữa, 520 ải theo chương |
| Máy | Máy bàn trước (Mac là máy đo chuẩn), di động sau |
| Nhân vật chính | Hỏa Long (`heroes/draconis-v2`, Tối Thượng đổi sang `-v3`), Bạch Long (`guides/draconis-v4`) |
| Một ải | 4–10 phút: Lều Chuẩn Bị → Bày binh → 4–6 đợt xen nghỉ → (boss) → Kết ải |
| Hành trình | 26 chương × 20 ải = **520 ải** (Mùa 2 lên 600). Mỗi chương một vùng đất, một luật mới |
| Học | Mỗi ải 8 từ mới (Ải Ôn 0), ~3.600 từ mới cả hành trình; IPA, nghĩa Việt, phát âm; sự kiện học về lõi chung `shared/learning` |
| Khó lên bằng | Thành phần quái, số đường, hào quang tướng, kỹ năng quái, boss, khắc chế. **Không** bằng đòi gõ nhanh hơn |
| Hình | Tripo do chủ dự án làm từ ảnh 2D của Codex; AI không dựng model bằng mã (đất, sông, hạt, shader thì được) |
| Bản thử dọc (M0) | 1 bản đồ 2 đường, Hỏa Long ở giữa, 6 loại quái (bay, hai chân, bốn chân), 1 tướng, 3 bẫy, 2 hỗ trợ, cửa hàng giữa đợt, 10 đợt |

## 1. Tên, bối cảnh, giọng

| | |
|---|---|
| Tên | **Rồng Giữ Ải** · EN *Dragonhold* · id `dragon-hold` · cổng 3005 · `dragon.typing-game.local` |
| Thế giới | **Đại Ngàn Sương**: rừng thông, sông, tán tím lam, nắng dịu. Mỗi sinh vật có một tên thật. Rồng gọi đúng tên thì lời thành lửa, gió, khiên |
| Phe địch | **Bầy Héo**: sinh vật rừng hít phải sương **Hắc Vụ** (tím xám) thì quên tên, mọc **vỏ Héo** xám tro, khe nứt và mắt sáng vàng úa `#C8D24A`. Hạ quái là vỡ vỏ, một đốm sáng bay về rừng. Không máu |
| Giữa bản đồ | **Bệ Rồng** (không đền, không chùa, theo luật văn hóa TD 22.1) |
| Giọng | Ấm, sáng, dễ cho trẻ em. Bạch Long là người thầy; Hỏa Long là sức mạnh của lời |
| Vỏ UI | Gỗ khắc, vỏ cây sẫm, viền rêu; tiêu đề Cormorant Garamond; chữ trận Be Vietnam Pro |
| Nhạc | Dân ca rừng giả tưởng: sáo gỗ, đàn hạc, cello, trống khung, hợp xướng; 4 lớp theo nhịp trận |

## 2. Năm trụ cột

| # | Trụ cột | Nghĩa là | Luật giữ trụ cột |
|---|---|---|---|
| 1 | **Gõ là sức mạnh** | Mỗi từ đúng là một đòn lửa. Gõ gây 65–80 % sát thương | Chuẩn thắng ẩu: Ẩu chỉ ×0,6; không chí mạng ngẫu nhiên; bot không gõ luôn thua (00 §7, G6) |
| 2 | **Học luôn rõ và thật** | Từ, IPA, nghĩa luôn đọc được; học thật mới tính là thuộc | Khung học DOM không rung; từ mới chỉ trên quái chậm; nghĩa ẩn theo số lần **nhớ** đúng, không theo gõ chép (01 §6.3) |
| 3 | **Giữ ải bằng trí** | Ít sát thủ, nhiều khống chế; mỗi loại quái có khắc chế | Ma trận khắc chế (03 §0.3); trần phe ta 40 % sát thương; khống chế giảm dần |
| 4 | **Rừng tranh vẽ sống** | Sa bàn vẽ tay; mỗi loài có cách đi, đòn, tiếng, hiệu ứng riêng | Dấu Héo chung; bảng hành vi từng loài, tướng, boss (02 §2.2, §3.4, §4.5); báo trước luôn đỏ |
| 5 | **Hành trình dài mà công bằng** | 520 ải, không cày, không tiền thật | Sim tất định 60 Hz; tải gõ giữ trong một dải ở mọi chương; bot kiểm từng ải |

## 3. Vòng chơi

```text
Một ải (4–10 phút)
  Lều Chuẩn Bị: xem đợt, chọn Bộ Mang Theo, mức khó, Học trước 8 từ mới
  → Bày binh (đặt bẫy, lính, nhà bằng vàng đầu ải) → Enter
  → [ Báo đợt 6 s → Đợt 40–70 s (gõ, kỹ năng, đồ tiêu hao) → Nghỉ 20 s (cửa hàng, Long Ấn, Thẻ Ôn) ] × 4–6
  → Lặng 12 s → Boss (ải 10, 20) → Kết ải: sao, Vảy, Tri Thức, Sổ Từ Ải, Ôn trận

Một chương (20 ải, ~2,5 giờ)
  1–4 dạy loài mới · 5 Ải Tướng · 6–8 trộn · 9 Ải Ôn · 10 boss nhỏ · 11–14 loài mới thứ hai, combo
  · 15 Ải Tướng · 16–18 combo, luật ải · 19 Ải Ôn (Lửa Trại) · 20 boss chương (pha cuối sát hạch từ của chương)

Hành trình (520 ải, ~55 giờ)
  3 Hồi: Bìa Ngàn (C1–10) · Lõi Ngàn (C11–19) · Hắc Vụ (C20–26)
  Ngoài ải: Bậc Rồng (XP), Cây Long Mạch (Sao), Thư Viện Rồng (Tri Thức), Xưởng Rồng (Vảy)
  Chơi lại: sao, Dấu Thách, Vương Miện, Lời Thề, Ác Mộng, Ải Ngày, Ôn Ngày, Rừng Vô Tận, Tháp Rồng
```

## 4. Các hệ (tóm tắt và nơi đọc)

| Hệ | Tóm tắt | Tài liệu |
|---|---|---|
| Luật chuẩn, số, phím, cổng bot | Một nguồn duy nhất; sổ quyết định D01–D22; từ điển tên | `00-canon.md` |
| Gõ trên quái | Từ gắn lên quái không đổi, không hết hạn; mọi chữ sống có chữ đầu khác nhau; khóa mềm; bảo hộ khóa 1,2 s; độ dài từ theo tốc độ riêng E; ngân sách chữ ≤ 16 | 01 §3, 00 §5 |
| Chấm từ, Chuỗi | Chớp ×1,25 · Hoàn hảo ×1,10 · Tốt ×1,00 · Vừa ×0,90 · Ẩu ×0,60; Chuỗi 5 bậc tới ×1,16 | 01 §3.7–3.8, 00 §4.2 |
| Chữ đặc biệt | Ấn Phá, Từ Ngắt, Từ Trợ, Chữ Chiêu, Từ Khẩn, bộ phận boss, Cụm Ấn, Hỏi Nghĩa, Từ Nghe; luật đề bài chống chấm sai | 01 §3.6 |
| Hai Rồng | Hỏa Long nhận mọi đòn gõ, hết máu là thua; Bạch Long chặn 2 quái, khiên, gió; 4 kỹ năng, 2 Tối Thượng chung thanh Long Nộ; Cấp Rồng 1–10 trong ải; 24 Long Ấn | 01 §2 |
| Quái | 32 loài, 8 họ, 4 dáng; W là số từ để hạ; bầy dùng chung một từ cụm; 8 biến chủng; 12 thuộc tính tinh anh | 02 §1–2 |
| Tướng địch | 8 Đội trưởng, 6 Thống lĩnh; hào quang trên đất; Ấn Phá tắt hào quang; trình bày từng tướng | 02 §3 |
| Boss | 20 boss, 2–4 pha, 12 cơ chế gõ, buff quân theo pha; song boss C20–25; B20 Mẹ Hắc Vụ | 02 §4 |
| Đợt | Toán có hình, 2–3 đỉnh, quãng lặng; ngân sách = tải gõ, đe dọa chỉ chọn thành phần; trần quái sống là luật | 02 §5, 00 §4.4 |
| Phe ta | 13 bẫy (26 nhánh), 11 nhà phép, 7 lính, 10 đồ tiêu hao; Cộng Hưởng; Từ Kích; 16 trạng thái, 4 phản ứng nguyên tố | 03 §2, §6–11 |
| Cửa hàng, kinh tế | Vàng theo ngân sách ải; mua đủ lúc nghỉ, trong đợt chỉ đồ tiêu hao (C1–5); Vảy, Tri Thức ngoài ải | 03 §3–4, 00 §4.9 |
| Trang bị | Bản đầu: 10 ô × 3 món cố định, nâng 1–5 bằng Vảy; độ hiếm, dòng phụ để sau | 03 §5 |
| Ải, bản đồ | 16 mẫu bố cục 1–4 đường, 8 kit vùng đất + lớp Hắc Vụ; thư viện luật ải 54 mục; 78 ải dựng tay | 04 §1–5 |
| Lịch dạy | Mỗi ải tối đa một ý mới; bảng C1 từng ải, C2+ từng chương | 04 §6 |
| Học | Bộ từ 70–100 mỗi ải (mới, đến hạn, đang học, đã thuộc); từ nào lên quái nào; lọc từ nhạy cảm; một sự kiện có chấm mỗi từ mỗi ải | 01 §6 |
| Tiến trình | Bậc Rồng 1–40, Cây Long Mạch, Thư Viện Rồng 12 bậc, cấp món, Cấp Từ tách khỏi số ải | 04 §7–9 |
| Hình, camera, HUD | Sa bàn tranh vẽ, FOV 30°, nghiêng 40–75°, xoay tự do; thẻ chữ có icon theo loại; vòng khe quanh bệ; khung học hàng đợi | 05 §2–4 |
| Phản hồi, VFX, âm | Bậc T0–T5 qua `kit/feedback`; dừng hình không nuốt phím; 12 bus âm; bộ âm theo lớp | 05 §5–7 |
| Kỹ thuật | Repo riêng; kit chép từ Space; sim thuần TS; ngân sách hiệu năng 4 bậc; bậc máy không đổi luật | 05 §8–10 |
| Lưu, focus, cài đặt, màn ngoài trận, hướng dẫn, đo lường | Đầy đủ cho bản công khai | 06 |
| Tách ba game | Lời Gọi (TD), Tuyến Cuối (Sinh Tồn), Rồng Giữ Ải trên portal | `../SPLIT_PLAN.md` |

## 5. Mô hình cân bằng (các số khớp nhau)

### 5.1 Đơn vị

- **g(c) = 1 + 0,02 × (c − 1):** sức chuẩn của chương (C1 1,00 · C10 1,18 · C20 1,38 · C26 1,50).
- **1 W = một từ Vừa = 90 × g(c) máu.** Hỏa Long có P = 100 × g(c). Một từ Hoàn hảo = 1,22 W; Chớp = 1,39 W; Ẩu = 0,67 W.
- Đòn gõ là loại **Chữ**: giáp, kháng không chặn. Giáp chỉ làm khó bẫy, lính, nhà.
- Bot 95 % chính xác: trung bình **một từ gõ ≈ 1,0 W hiệu dụng** (1,26 W thô, trừ phần thừa khi hạ quái nhỏ và lúc đổi mục tiêu).

### 5.2 Sức gõ ở 25 / 35 / 60 WPM

```text
C(E) = 60 / (0,45 + 12 × (ℓ̄ + 1) / (E × d))   từ mỗi phút;  d = 0,86 (trộn độ quen)
```

| Người chơi | ℓ̄ (độ dài từ trung bình) | Giây mỗi từ | Từ mỗi phút | W/s | Nhịp đợt k_E |
|---|---|---|---|---|---|
| 25 WPM | 4,5 | 3,52 | 17,0 | 0,28 | 0,75 (đợt giãn 33 %) |
| **35 WPM (tham chiếu)** | 4,5 | 2,64 | **22,7** | **0,38** | 1,00 |
| 60 WPM | 5,5 | 1,96 | 30,6 | 0,51 | 1,00 (nên chọn Khó) |

- k_E = clamp(C(E) / 22,7; 0,75; 1,00) chỉ giãn **thời gian** đợt cho người chậm. Thành phần quái, W, mã băm ải giữ nguyên.

### 5.3 Tải gõ: giống nhau ở mọi chương

```text
W_gõ(đợt) = Σ W quái (mỗi cụm bầy tính 1, mỗi lớp khiên chữ tính 1)
Tải L     = W_gõ / (22,7 × phút của đợt)
```

| Đợt | Tải trung bình | Đỉnh 6–10 s |
|---|---|---|
| Đợt 1 | 0,55–0,65 | — |
| Đợt giữa | 0,75–1,00 | ≤ 1,15 |
| Đợt cuối | 1,05–1,25 | ≤ 1,15 (C1) → ≤ 1,40 (C18+) |

Tải trên 1,0 là cố ý: phần dư do bẫy, lính, nhà, kỹ năng gánh. **Chương sau không đòi thêm W gõ mỗi phút.** Đe dọa trên mỗi W gõ tăng từ ~1,6 (C1) lên ~12 (C26) nhờ quái nhanh, kỹ năng, hào quang, nhiều đường và nhiều bầy (một cụm 8–10 con chỉ là 1 từ).

### 5.4 Ví dụ A: ải thường C1, 1 đường, người 35 WPM

| Đợt | Dài | Tải | W_gõ | Thành phần ví dụ |
|---|---|---|---|---|
| 1 | 50 s | 0,60 | 11 | 9 Yêu Rêu Lính (1 W) + 2 cụm kiến |
| 2 | 55 s | 0,75 | 16 | 13 Yêu Rêu Lính + 3 cụm kiến |
| 3 | 60 s | 0,85 | 19 | 14 Yêu Rêu Lính + 3 Ong Gai + 2 cụm kiến |
| 4 | 60 s | 0,95 | 22 | 16 Yêu Rêu Lính + 4 Ong Gai + 2 cụm kiến |
| 5 | 65 s | 1,05 | 26 | 18 Yêu Rêu Lính + 5 Ong Gai + 3 cụm kiến (đỉnh 1,15) |
| **Cộng** | 290 s | 0,86 | **94** | ~82 quái Nhỏ + 12 cụm (~55 kiến) ≈ **137 con** (00 §4.8: 100–140) |

- **Máu:** Yêu Rêu Lính 1 W = 90 máu. Hỏa Long Hoàn hảo 110, Vừa 90: một từ là chết; Ẩu 60: cần thêm một từ.
- **Sức gõ 35 WPM:** 0,38 W/s × 290 s × 85 % (lúc chờ quái vào Vùng Chữ) ≈ **93 W**. Gõ một mình gần đủ: đúng cổng G5 (chỉ gõ thắng ≥ 70 % ở ải 1–10). Bẫy và lính bù phần đỉnh.
- **Sức gõ 25 WPM:** k_E = 0,75 → đợt dài 387 s → 0,28 × 387 × 85 % ≈ **93 W**. Bằng người 35 WPM, chỉ chậm hơn.
- **Sức gõ 60 WPM:** 0,51 × 290 × 85 % ≈ 126 W, dư 34 %. Người nhanh nên chọn mức Khó (W × 1,15 → cần 108 W) và Lời Thề sau này.
- **Vàng:** 200 + 900 × 1,0 × 1,0 = **1.100**. Dựng tối đa bản đồ 1 đường ~3.100 Vàng: chỉ đủ 35 %, phải chọn.

### 5.5 Ví dụ B: ải thường C20, 3 đường, người 35 WPM

| Đợt | Dài | Tải | W_gõ |
|---|---|---|---|
| 1 | 55 s | 0,60 | 12,5 |
| 2 | 60 s | 0,80 | 18,2 |
| 3 | 60 s | 0,90 | 20,4 |
| 4 | 65 s | 1,00 | 24,6 |
| 5 | 65 s | 1,10 | 27,1 |
| 6 | 70 s | 1,25 (đỉnh 1,40) | 33,1 |
| **Cộng** | 375 s | 0,96 | **136** |

- **Thành phần ví dụ:** 36 cụm bầy × 8 con (288 con, 36 W_gõ) + 40 quái Nhỏ (40 W) + 14 quái Vừa (35 W) + 3 quái Nặng (15 W) + 1 Thống lĩnh (10 W) = 136 W_gõ, **346 con**, 83 % là bầy (00 §4.8: 330–430).
- **Máu:** 1 W = 90 × 1,38 = 124 máu. Hỏa Long trung bình P = 138, Hoàn hảo 152 = 1,22 W (giống C1). Thống lĩnh 10 W = 1.240 máu ≈ 9 từ ≈ 24 s gõ.
- **Sức gõ 35 WPM:** 0,38 × 375 × 85 % ≈ **120 W**. Thiếu ~16 W_gõ (12 %). Bẫy nổ hạ khoảng 1/3 số cụm bầy (Bom Hạt Thông, Mìn Ấn, Cột Sét), lính chặn và nhà giữ quái Nhỏ: phe ta gánh phần thiếu. Đúng cổng G8 (phe ta 20–35 % sát thương).
- **Vàng:** 200 + 900 × 1,45 = **1.505**. Dựng tối đa 3 đường ~7.500 Vàng: đủ 20 %.
- Người 25 WPM: đợt giãn 33 %, sức gõ lại ≈ 120 W. Khó hơn C1 vì quái nhanh hơn, hào quang, 3 đường, khắc chế; **không** vì phải gõ nhanh hơn.

### 5.6 Boss

```text
W_boss = round(0,38 × 0,7 × t)   // t: giây đích ở 35 WPM; 0,7 vì hộ tống và cơ chế chiếm một phần sức gõ
```

| Boss | W | Máu | 35 WPM | 25 WPM (k_E 0,75) |
|---|---|---|---|---|
| B01 Lợn Lòi Chúa (C1) | 30 | 2.700 | ~110 s | ~150 s |
| B10 Kỳ Nhông Dung Nham (C10) | 40 | 4.250 | ~150 s | ~205 s |
| B19 Hắc Long (C19) | 48 | 5.870 | ~180 s | ~240 s |
| Song boss C20–25 | 52–56 (hai thân) | ~6.500–7.500 | ~200 s | ~270–290 s |
| B20 Mẹ Hắc Vụ (C26) | 72 | 9.720 | ~270 s | ~6 phút |

- Ải boss chương = 5 đợt (~6 phút) + boss: 8–10 phút ở 35 WPM; C26 ≤ 12 phút.

### 5.7 Phe ta và tiền

| Mục | Số |
|---|---|
| Phần sát thương phe ta | 20–35 % mỗi ải, trần 40 %; khống chế cứng ≤ 35 % thời gian sống của quái |
| Sức phe ta theo chương | Sát thương, máu bẫy, nhà, lính nhân g(c); cấp món +6 % mỗi cấp, tối đa +24 % |
| Vàng mỗi ải | 200 + 900 × (1,00 / 1,25 / 1,45 / 1,60 theo số đường) × hệ số loại ải; chia cho quái theo đe dọa |
| Vảy cả đường chính | ~4.700; chỗ tiêu 6.920 (cấp món 3.720 + trang bị 3.200): đủ ~68 % |
| Tri Thức | ~25 mỗi ải; Thư Viện 12 bậc ≈ 5.100: mở hết ở ải 200–250 |

### 5.8 Cổng bot chính (đầy đủ ở 00 §7)

| Cổng | Ngưỡng |
|---|---|
| Bot 35 WPM, bộ đồ trung bình | Thắng 75–90 % ải thường; 3 sao ≤ 60 % từ C3 |
| Bot 25 WPM | Thắng ≥ 70 % tới C5, ≥ 55 % sau đó (Dễ ≥ 75 %) |
| Chỉ gõ, không mua | Thắng ≥ 70 % ải 1–10; thua ≥ 60 % từ ải 21 |
| Không gõ | Thua 100 % từ ải 2 |
| Chuẩn thắng ẩu | 35 WPM 98 % hạ quái nhanh hơn 50 WPM 85 % |
| Học | Từ mới không lên độ thuộc ≥ 70 trong ải đầu gặp nó |

## 6. Số lượng nội dung

| Nhóm | Số | Ghi chú |
|---|---|---|
| Ải | 520 = 364 thường + 52 Ải Tướng + 52 Ải Ôn + 26 boss nhỏ + 26 boss chương | 78 ải dựng tay; Mùa 2 lên 600 |
| Chương, Hồi | 26 chương, 3 Hồi | Mỗi chương một vùng, một luật mới |
| Bản đồ | 16 mẫu bố cục (1–4 đường) × 34 vùng × seed | 8 kit + biến thể + lớp Hắc Vụ + Khe Hắc Vụ |
| Thư viện luật ải | 12 mục tiêu, 16 hiểm họa, 8 luật học, 8 luật quân, 10 biến cố | ~180.000 tổ hợp |
| Quái thường | 32 loài: 8 bay, 9 hai chân, 7 bốn chân, 8 bò hoặc bầy | 8 biến chủng, 12 thuộc tính tinh anh |
| Tướng địch | 14: 8 Đội trưởng, 6 Thống lĩnh | |
| Boss | 20, 12 cơ chế gõ; 6 cặp song boss | |
| Rồng | 2 Rồng, 4 kỹ năng, 2 Tối Thượng, 2 nội tại, 24 Long Ấn | Ô Rồng thứ 3, 4 để sẵn |
| Bẫy | 13, mỗi bẫy 2 nhánh cấp 3 (26 nhánh), 6 chuỗi bẫy làm sẵn | |
| Nhà phép | 11 | |
| Lính chặn, hỗ trợ | 7 | Chỉ 2 "sát thủ": Thợ Săn Cú, Tháp Canh |
| Đồ tiêu hao, mua trong ải | 10 đồ tiêu hao + Tim Rồng, Vảy Cứng, Lông Bạc | |
| Trang bị | 10 ô × 3 món cố định = 30 | |
| Trạng thái | 16, 4 phản ứng nguyên tố | |
| Tiến trình | Bậc Rồng 40, Cây Long Mạch 5 nhánh × 7 bậc, Thư Viện 12 bậc | |
| Học | ~140 từ mới mỗi chương, ~3.600 cả hành trình | |
| Thành tựu | 40 (14 về học) | |

## 7. Sản xuất hình và âm

### 7.1 Ai làm gì

| Người làm | Làm gì | Không làm |
|---|---|---|
| **Chủ dự án (Tripo)** | Model 3D từ ảnh 2D: cảnh, quái, tướng, boss, bẫy, nhà, lính, nhà Làng Rồng; rig và chọn clip có sẵn của Tripo; duyệt ảnh 3 góc × 4 hướng | — |
| **Codex CLI** (Claude điều khiển, đăng nhập ChatGPT) | Ảnh 2D nguồn cho mọi model (2 góc), ô đất, decal, tấm cỏ hoa, phông xa, icon (~90), khung UI gỗ khắc, tranh Hành Trình, tranh truyện chương, màn nạp | Không làm model |
| **AI với Blender** (bộ công cụ có sẵn) | Chỉ chuyển động trên lưới có sẵn: đổi tên clip, khóa gốc, thêm clip cắn, vồ, húc, bay; clip Hit, Down, Rise cho Bạch Long; đổi vật liệu (Hắc Long) | Không dựng lưới, không tạc model |
| **AI trong mã** | Đất cao độ, sông, đường, decal, hạt, shader, đám đông, giữ chỗ hộp trong hộp cát | Không dựng model nhân vật hay cảnh bằng mã |
| **Âm** | Thư viện CC0, công cụ âm AI có gói thương mại (ghi công cụ, ngày, prompt, giấy phép như TD 24.9), tiếng gõ tổng hợp bằng mã, `shared/voice` cho phát âm Anh, giọng đọc tiếng Việt dựng sẵn | Không đưa file âm vào Git |

- Mọi ảnh, âm, model đi Google Drive qua `pnpm media:push`. Không vào Git.

### 7.2 Danh sách theo lát

| Lát (mốc) | Tripo (chủ dự án) | Codex | Âm |
|---|---|---|---|
| **Mẫu duyệt** (đầu M0) | 3 sinh vật: E09 Yêu Rêu Lính, E18 Sói Mục, E01 Ong Gai (4 clip mỗi con) | 2 ảnh thử dấu Héo cho E09; ảnh nguồn 3 loài | — |
| **M0** bản thử dọc | +4 sinh vật: E11, E19, E25, G01; 12 cây, đá, bụi của kit rừng thông; Gai Chông, Bom Hạt Thông, Lưới Phóng, Vệ Binh Rêu, Nhà Thuốc Lá (5) → **~24 model** | ~60 ảnh: nguồn cho 24 model, 8 ô đất, 4 decal, phông, ~20 icon | ~50 tiếng: gõ (mã), cầu lửa 3, Phun Lửa, bộ lớp hai chân, bốn chân, bay, bầy, G01, 3 bẫy × 2, 2 hỗ trợ × 2, UI 4, tù và, thắng, thua, Hỏa Long trúng, ngã; 1 bản nhạc 2 lớp + 1 bản tướng |
| **M2** chương 1 | B01; 5 prop còn lại của kit | ~40 | +20: B01, Bạch Long, Long Hống; thoại Bạch Long ải 1–20 (~60 câu) |
| **M3** C2–C3 | 8 quái, tướng, 2 boss; kit rừng phép 12 prop; 8 món; 4 nhà làng | ~120 | Bộ lớp còn lại; nhạc rừng phép; 2 boss |
| **M4** C4–C6 (công khai) | ~12 quái, tướng, boss; 3 kit (36 prop); ~10 món | ~200 | Nhạc 3 kit; boss; tranh truyện có giọng |
| **M5–M7** | Phần còn lại: ~150 model | ~330 | Phần còn lại |
| **Cộng** | **~216 model** (~400 lượt tính tạo lại) | **~750 ảnh** (chưa tính tranh truyện ~78–156 tấm) | ~600 file âm, ~10 bản nhạc kit và boss, ~180 câu thoại |

- **Giảm rủi ro hoạt ảnh:** quái thường chỉ cần 4 clip (Idle, Move, Attack, Death). Trúng đòn bằng phản ứng instanced; kỹ năng bằng VFX. Tướng, boss mới đủ bộ clip (02 §7.2).
- **Ước Tripo:** ~75 credit mỗi sinh vật theo giá API, ~4.700 credit cho 63 sinh vật; thời gian của chủ dự án 50–80 giờ cho tạo, rig, chọn clip. Lên lịch theo số giờ mỗi tuần anh cho biết (Câu hỏi 4).
- **Bộ âm theo lớp, không theo loài** (9 lớp); tướng và boss có bộ riêng. Nhạc: mỗi kit 1 bản 4 lớp, không phải mỗi chương 2 bản.

## 8. Kỹ thuật (tóm tắt)

- Repo riêng `games/dragon-hold` (submodule). Vite 7, TS, `three@0.170.0` ghim.
- Mã dùng chung ở `shared/game-kit`, **chép** vào `src/kit/` bằng `kit:sync` có kiểm sha256. Kit chép **từ** Space; Space giữ bản gốc (`../SPLIT_PLAN.md` §4).
- Sim thuần TS, tất định 60 Hz, số nguyên, RNG theo seed; không `three`, `window`, `Date`, `Math.random` trong `sim/`, `typing/`, `content/`.
- Thẻ chữ, khung học là DOM trên canvas. Đám đông quái và lính bằng texture xương instanced; chỉ Rồng, tướng, boss là `SkinnedMesh`.
- Ngân sách High trên Mac 1080p: khung trung bình ≤ 8 ms, p95 ≤ 12 ms, ≤ 150 draw call, 220 quái vẽ đầy đủ. Bậc máy chỉ đổi cách vẽ.
- Cây thư mục, ranh giới, kịch bản hình `dh-*`: 05 §9–10.

## 9. Kế hoạch xây theo mốc

Mỗi mốc có bốn loại cổng: **test** tự động, **kịch bản trình duyệt** (`dh-*`, gõ thật qua CDP), **hiệu năng**, **chủ dự án chơi thử**. Mỗi mốc có changelog riêng (`docs/changelog/<ngày>-<chủ đề>.md`) và một vòng phản biện độc lập trước khi qua cổng.

### M0 — Bản thử dọc (chạy song song với việc tách game)

| Phần | Nội dung |
|---|---|
| Bản đồ | 1 bản đồ **2 đường** (`L2-cau`: một nhánh qua cầu, một nhánh lội suối) trên kit rừng thông có sông, bản rút gọn; 1 đường trời |
| Rồng | **Hỏa Long ở giữa**: đòn gõ, Phun Lửa (Alt + 1), Thiên Hỏa (Alt + 2), Long Hống (Từ Khẩn), Long Nộ và Viêm Đế (thử đổi sang v3). Bạch Long đứng cạnh làm người dẫn (clip Guide có sẵn), chưa đánh |
| Quái (6 loại) | E09 Yêu Rêu Lính (**hai chân**, cận chiến) · E11 Yêu Rêu Cung (hai chân, bắn xa) · E18 Sói Mục (**bốn chân**, bầy nhỏ, vồ qua chặn) · E19 Heo Nanh Đá (bốn chân, húc) · E01 Ong Gai (**bay**, bắn) · E25 Kiến Gai (bò, cụm bầy một từ) |
| Tướng | G01 Yêu Rêu Cầm Cờ: hào quang Xung Phong, Cắm Cờ, Ấn Phá |
| Phe ta | **3 bẫy:** Gai Chông, Bom Hạt Thông, Lưới Phóng · **2 hỗ trợ:** Vệ Binh Rêu (lính chặn), Nhà Thuốc Lá (nhà phép) · Bình Máu Nhỏ · Tim Rồng, Vảy Cứng |
| Cửa hàng | Mở **giữa các đợt** (nghỉ 20 s): đặt, nâng, bán; dải Bộ Mang Theo; đặt bằng chuột và bàn phím (00 §6) |
| Đợt | **10 đợt**, tải theo 00 §4.4 (đợt 1 0,6 → đợt 10 1,25), tướng ở đợt 5 và đợt 10, đỉnh và quãng lặng theo 02 §5 |
| Gõ và học | Thẻ chữ, chữ đầu duy nhất, khóa mềm, bảo hộ khóa, ngân sách chữ, khung học (IPA, nghĩa, hàng đợi), phát âm, Học trước, Thẻ Ôn; sự kiện học `dragon-hold` (xếp hàng cục bộ nếu portal chưa nối) |
| Âm, hình | Phản hồi T0–T5, báo trước đỏ, bộ âm M0 (mục 7.2), nhạc 2 lớp |
| Công cụ | Sim tất định, `dh:balance` với bot 0 / 25 / 35 / 60 WPM trên bản đồ M0; **bench đám đông có xương** (`defense-bench` chế độ `bones`, `vat`) làm **đầu tiên** |

Chia nhỏ: **M0a** hộp xám (đủ luật, hộp thay model, đất và sông thủ tục) → **M0b** hình (3 model mẫu duyệt trước, rồi 4 model còn lại và prop) → **M0c** âm, VFX, đánh bóng, chủ dự án chơi.

| Cổng M0 | Ngưỡng |
|---|---|
| Test | Golden: cùng seed ra cùng mã băm; test ranh giới; test bố cục thẻ (không chồng, không ẩn chữ sống); test hợp đồng sự kiện học; test ngân sách chữ |
| Trình duyệt | `dh-words`, `dh-learning-frame`, `dh-hitstop-keys`, `dh-placement`, `dh-focus`, `dh-keyboard-only` (bản đồ M0), `dh-telegraphs`; 0 lỗi console |
| Hiệu năng | Bench trước: 220 quái đám đông có xương, đủ 3 dáng: High trên Mac trung bình ≤ 8 ms, p95 ≤ 12 ms; Low trên laptop yếu ≤ 16 ms. Không đạt thì hạ trần quái của luật rồi chạy lại bot |
| Bot | 35 WPM thắng 75–90 %; 25 WPM thắng ≥ 70 %; chỉ gõ thắng ≤ 40 % ở 10 đợt; không gõ thua trước đợt 3; tải đỉnh ≤ 1,40 |
| Chủ dự án | Duyệt dấu Héo (2 ảnh thử E09), 3 model mẫu và hoạt ảnh, ảnh bản đồ 3 góc × 4 hướng; chơi 10 đợt, chấm cảm giác đòn, VFX, âm; nói "đạt" hoặc ghi điều cần sửa |

### M1 — Khung hệ thống (vẫn trên bản đồ M0)

Lưu đủ lớp, ảnh chụp chơi tiếp (06 §1); focus, tạm dừng (06 §2); cài đặt, đổi phím (06 §3); màn ngoài trận cơ bản: Tiêu đề, hồ sơ, Kết ải, Màn thua, menu dừng (06 §4); dữ liệu ải, `stages:gen`, `stages:validate` (gồm luật khắc chế G19); Bạch Long vào trận (clip Hit, Down, Rise bằng Blender), Khiên, Gió Cuốn; kênh phát âm và luật học 01 §6.3; chuyển tài liệu vào repo game.

| Cổng M1 | Ngưỡng |
|---|---|
| Test | Hàm chuyển lưu với file mẫu; khe A/B khi hỏng; `stages:validate` bắt lỗi cố ý |
| Trình duyệt | `dh-meta-screens`, `dh-focus` trong khung portal, `dh-keyboard-only` qua cả màn ngoài trận |
| Hiệu năng | Nạp ải ≤ 1 s cùng kit; sim headless ≤ 0,3 ms mỗi bước ở đỉnh, ≥ 200× thời gian thực trung bình |
| Chủ dự án | Đóng tab giữa ải rồi chơi tiếp được; chơi 2 ải bằng bàn phím |

### M2 — Chương 1 (20 ải)

20 ải dựng tay theo lịch dạy 04 §6.1; lời dẫn Bạch Long ải 1–6 (06 §5); Ải Ôn, Lửa Trại; boss B01; bộ đồ C1; Hành Trình 1 chương; sự kiện học gửi thật qua portal.

| Cổng M2 | Ngưỡng |
|---|---|
| Bot | G1–G12, G16–G18 trên 20 ải |
| Trình duyệt | Mọi `dh-*`; `dh-boss` với B01 |
| Chủ dự án | Chơi ải 1–6 như người mới (không đọc tài liệu); chơi B01; duyệt thoại, nhạc |

### M3 — C2–C3 (60 ải)

2 đường; Thiên Hỏa, Gió Cuốn, Long Ấn, Từ Trợ, Lời Thề Bạch Vũ; món C2–3; kit rừng phép; Làng Rồng (Hang, Thư Viện, Xưởng), trang bị cố định, Bậc Rồng, Long Mạch; luật học Nghĩa, Nghe; B02, B03; ải thường sinh bằng `stages:gen`.

| Cổng M3 | Ngưỡng |
|---|---|
| Bot | Toàn bảng 00 §7 trên 60 ải, chạy lấy mẫu (00 §8) |
| Chủ dự án | Duyệt kit rừng phép; chơi mỗi chương ải 1, 10, 20 |

### M4 — C4–C6 (120 ải) — **bản công khai đầu**

3 đường; Từ Kích, Cộng Hưởng; luật học Phiên Âm, Thiếu Chữ, Chủ Đề; 3 kit; B04–B06; Vương Miện, Ải Ngày, Ôn Ngày; đo lường cục bộ, thành tựu; adapter Smart Review `dragon-hold-review-dataset.mjs`; tranh truyện.

| Cổng M4 | Ngưỡng |
|---|---|
| Bot | Toàn bảng trên 120 ải, khóa mã băm từng ải |
| Hiệu năng | `dh-perf` ở 4 bậc |
| Chủ dự án | Duyệt phát hành |

### M5 — C7–C10 (200 ải, hết Hồi I) · M6 — C11–C19 (380 ải, Hồi II) · M7 — C20–C26 (**520 ải**, Hồi III)

Theo bảng chương 02 §6.1 và lịch 04 §6.2: 4 đường, sông sinh quái, chữ ẩn và LỘ (M5); Thống lĩnh, biến chủng, Lời Thề, hiểm họa khách (M6); lớp Hắc Vụ, song boss, B20 (M7). Mỗi mốc: bot toàn bảng trên mọi ải mới, mọi `dh-*`, chủ dự án duyệt hình từng kit và chơi boss chương.

### M8 — Mùa 2 và giai đoạn sau

C27–30 (600 ải); trang bị sâu (độ hiếm, dòng phụ) nếu số đo cho thấy cần; đồng bộ tài khoản; Rồng thứ 3, 4; di động.

### Làn song song (nhiều agent cùng lúc, mỗi làn chỉ ghi vào thư mục của mình)

| Làn | Bắt đầu | Chỉ ghi vào | Agent |
|---|---|---|---|
| Sim: trận, đợt, quái | M0a | `src/sim/{world,waves,spawn,combat,boss,auras}`, `src/content/data/enemies*` | 1 |
| Sim: phe ta, cửa hàng | M0a | `src/sim/{traps,houses,units,shop,economy,status}`, `data/our-side` | 1 |
| Gõ và học | M0a | `src/sim/words`, `src/ui/{tags,learning-frame}`, `src/app/learning` | 1 |
| View: đất, sông, camera | M0a | `src/view/{stage,terrain,water,scatter,camera}` | 1 |
| View: đám đông, Rồng, VFX (bench trước) | M0a | `src/view/{crowd,actors,heroes,fx,telegraphs,hpbars}` | 1 |
| UI: HUD, cửa hàng, đặt món | M0a | `src/ui/{hud,shop-strip,placement,wave-card,results}` | 1 |
| Âm | M0b | `src/audio`, danh sách âm | 1 |
| Bot và cân bằng | M0a | `scripts/balance`, `tests/sim`, `tests/golden` | 1 |
| Hình (prompt Codex, Blender, nạp model) | Ngay | `art-src/` (ngoài Git), `scripts/models`, manifest | 1 (+ chủ dự án) |
| Kit và tách game | Ngay | `shared/game-kit`, `games/typing-survival`, `games/typing-defense` | 2–3 (`../SPLIT_PLAN.md` §13) |
| Hạ tầng, portal | Ngay | `infra/`, `portal/`, script repo cha | 1 |
| Phản biện | Mỗi cổng | Chỉ đọc | 1 mỗi làn |

- Khoảng 12–14 agent chạy cùng lúc ở M0 mà không ghi chồng file. Dữ liệu dùng chung (`src/content/types.ts`, `rules.json`) do làn Sim trận giữ; làn khác đề nghị đổi qua người điều phối.
- Đổi kit đi qua repo cha rồi `kit:sync`. Không agent nào sửa `src/kit/` trong game. Không đụng `games/.wt-*` đang có người làm.

## 10. Rủi ro chính

| Rủi ro | Giảm bằng |
|---|---|
| Đám đông có xương không đạt hiệu năng | Bench đầu M0; hạ trần quái của luật nếu cần, rồi chạy lại bot |
| Hoạt ảnh Tripo không đạt mức chủ dự án muốn | 3 model mẫu duyệt trước lô lớn; 4 clip bắt buộc; trúng đòn và kỹ năng bằng VFX |
| Thời gian Tripo của chủ dự án | Lên lịch theo số giờ mỗi tuần; làm theo lát; mỗi lát chỉ đủ chương của nó |
| Học thành gõ chép | Nghĩa ẩn theo lần nhớ đúng; một sự kiện có chấm mỗi từ mỗi ải; việc ở lõi chung (01 §6.8) |
| Quá tải chú ý | Ngân sách chữ; một loại chữ mới tại một lúc; trong đợt chỉ đồ tiêu hao (C1–5); Long Ấn lúc nghỉ; cổng G20 |
| Quy mô | Bản thử dọc nhỏ, chạy song song với tách game; trang bị cố định; bộ âm theo lớp |
| Lệch tài liệu | 00 là nguồn duy nhất cho số; sổ quyết định; mỗi cổng có phản biện |

## 11. Câu hỏi cho chủ dự án (mỗi câu có mặc định)

| # | Câu hỏi | Mặc định nếu không trả lời |
|---|---|---|
| 1 | Tên Rồng Giữ Ải (`dragon-hold`), Lời Gọi (`typing-defense`), Tuyến Cuối (`typing-survival`)? | Dùng đúng các tên này |
| 2 | Phe Bầy Héo (vỏ xám tro, nứt vàng úa) do sương Hắc Vụ gây ra, không máu? | Giữ; anh duyệt 2 ảnh thử E09 trước khi làm ảnh quái hàng loạt |
| 3 | Bản thử dọc M0 như mục 9 (2 đường, 6 quái, 1 tướng, 3 bẫy, 2 hỗ trợ, 10 đợt), chạy song song với việc tách game? | Có |
| 4 | Mỗi tuần anh dành bao nhiêu giờ cho Tripo; quota tạo ảnh của Codex? | Giả định 6–8 giờ Tripo mỗi tuần; lát M0 cần ~24 model |
| 5 | Cho Blender thêm clip Hit, Down, Rise cho Bạch Long trên lưới có sẵn? | Có, chỉ chuyển động |
| 6 | Viêm Đế đổi tạm sang model v3? | Có; vụng thì giữ v2 với clip Cast |
| 7 | Bạch Long dẫn lời ở ải 1–10, vào trận từ ải 11? | Có |
| 8 | Đặt món vào ô có sẵn (không đặt tự do)? | Ô có sẵn, chỉ hiện khi đặt hoặc nghỉ |
| 9 | Bản đầu dùng trang bị cố định, chưa có độ hiếm, dòng phụ, rèn? | Có |
| 10 | 520 ải ở bản đầy đủ, Mùa 2 lên 600; công khai đầu khi đủ C1–6? | Có |
| 11 | Ải Ôn ở ải 9 và 19 mỗi chương? | Có |
| 12 | Chỉ gõ không lỗi (e = 0) mới tính đúng trong sự kiện học, như Space? | Có |
| 13 | Giọng Bạch Long và người kể: giọng AI tiếng Việt dựng sẵn, có giấy phép thương mại? | Có |
| 14 | Đồng bộ bản lưu qua tài khoản ở bản đầu? | Không; xuất, nhập file |
| 15 | Hồ sơ trẻ em được bỏ qua ải sau 3 lần thua (trừ boss chương)? | Có |
| 16 | Có chế độ nói (Voice, Hybrid như Space)? | Không ở bản đầu; kiến trúc để ngỏ |
| 17 | Song boss Hắc Hóa cho C20–25 thay vì 6 boss mới? | Có |
| 18 | Dùng `draconis-v3` đổi màu làm Hắc Long, `lieutenant-nature` làm Bọ Hung Sấm? | Có, sau khi anh xem ảnh 3 góc |

## 12. Sổ tài liệu

| File | Nội dung |
|---|---|
| `00-canon.md` | Ai giữ hệ nào, từ điển tên, sổ quyết định, số chuẩn, ngân sách chữ, bảng phím, cổng bot, sức chạy bot |
| `01-core-combat-learning.md` | Vòng ải, hai Rồng, gõ trên quái, chữ đặc biệt, chấm từ, Chuỗi, học trong trận, sự kiện học |
| `02-enemies-generals-bosses.md` | Phe Bầy Héo, 32 loài, biến chủng, tinh anh, 14 tướng, 20 boss, bộ sinh đợt, đường cong chương, model |
| `03-our-side-shop-traps-support.md` | Chỉ số, công thức, trạng thái, Vàng, cửa hàng, trang bị, bẫy, nhà, lính, ma trận khắc chế, lịch mở món |
| `04-stages-maps-progression.md` | Thang 520 ải, vùng đất, bản đồ, luật ải, lịch dạy, Cấp Từ, tiến trình, chơi lại, dữ liệu ải, lát hình |
| `05-presentation-audio-tech-split.md` | Hướng hình, camera, HUD, thẻ chữ, VFX, âm, hiệu năng, kiến trúc, kiểm hình |
| `06-other-systems.md` | Lưu, focus, cài đặt, màn ngoài trận, hướng dẫn người mới, thoại, đo lường, thành tựu, bản địa hóa, chống nản |
| `research/*.md` | Thị trường, mã nguồn và cách tách, quy trình hình |
| `../SPLIT_PLAN.md` | Tách ba game, kit chung, portal, hạ tầng, phần ở lại Space |
