# Rồng Giữ Ải — 00. Luật chuẩn, số chuẩn, từ điển (23/10/2026)

> **Vai của tài liệu này:** nguồn duy nhất cho số, công thức, bảng phím, ngân sách chữ và cổng bot.
> Tài liệu 01–06 chỉ mô tả hệ và **trỏ về đây** khi cần số. Khi có lệch, tài liệu này thắng.
> Khi viết mã, các số ở đây chuyển vào `src/content/data/rules.json`. Từ đó, tài liệu trỏ tới khóa trong file đó.
> Mọi số là **số khởi điểm**. Bot chỉnh số trong dữ liệu. Luật không đổi khi chỉnh số.

## 1. Ai giữ hệ nào

| Hệ | Tài liệu chủ | Ghi chú |
|---|---|---|
| Số, công thức, phím, ngân sách chữ, cổng bot, mức khó | **00** (tài liệu này) | Thắng mọi tài liệu khác |
| Vòng ải, gõ, chữ, chấm từ, Chuỗi, hai Rồng, kỹ năng, học, sự kiện học | 01 | |
| Quái, biến chủng, tinh anh, tướng địch, boss, bộ sinh đợt, đường cong chương | 02 | Bộ sinh đợt chỉ ở 02 §5 |
| Phe ta: bẫy, nhà, lính, đồ tiêu hao, cửa hàng, Vàng, trang bị, ma trận khắc chế | 03 | |
| Thang ải, bản đồ, luật ải, lịch dạy, tiến trình lâu dài, chơi lại | 04 | |
| Hình, âm, UI trong trận, camera, kỹ thuật, kiểm hình | 05 | |
| Lưu, focus, cài đặt, màn ngoài trận, hướng dẫn người mới, đo lường, thành tựu | 06 | |
| Tách ba game, kit chung, portal, hạ tầng | `../SPLIT_PLAN.md` | |
| Tổng quan, mô hình cân bằng, sản xuất, kế hoạch xây | `DESIGN.md` | Bản tóm tắt, không có số riêng |

**Thứ tự ưu tiên khi lệch:** 00 → tài liệu chủ của hệ → tài liệu khác. Ai thấy lệch thì sửa tài liệu thua, không thêm luật mới.

## 2. Từ điển tên

| Dùng | Không dùng nữa | Nghĩa |
|---|---|---|
| Rồng Giữ Ải, id `dragon-hold`, lệnh `dh:*` | Dragon Lane, `dragon-lane`, `dl:*` | Tên game. Thư mục tài liệu giữ tên `dragon-lane/` tới khi chuyển vào repo game |
| Hỏa Long, Bạch Long | Rồng đỏ, Rồng trắng | Hai Rồng của người chơi |
| Bệ Rồng | Đền Trứng Rồng, Tổ | Bệ đá giữa bản đồ, bán kính 4 m |
| Bầy Héo | (phe "Hắc Vụ" như tên phe) | Phe quái: sinh vật bị Héo |
| Hắc Vụ | — | Sương tím xám gây Héo. Là nguồn, là lớp cảnh Hồi III, là boss B20 |
| Bộ Mang Theo | Túi Ải | Món mang vào ải (6–10) |
| Bầy · Nhỏ · Vừa · Nặng · Khổng lồ | T1, T2 (bậc quái của 01 cũ) | Bậc quái thường (02 §1.2) |
| Đội trưởng | Tướng quái | Tướng địch bậc 1, 5–7 W |
| Thống lĩnh | Đại Tướng | Tướng địch bậc 2, 10–12 W, từ C11 |
| D1–D5 | T1–T5 (độ dài chữ của 02 cũ) | Bậc độ dài chữ. T0–T5 chỉ dùng cho bậc phản hồi (05 §5) |
| Ấn Phá | Ấn (02 cũ) | Từ viền đồng trên tướng địch. Gõ xong: tắt hào quang |
| Ngọc Chữ | Ấn Chữ (ô trang bị) | Ô trang bị chung đổi một luật gõ |
| Thẻ Ôn | Chợ Học | Một thẻ ôn lúc nghỉ đợt (đã gộp) |
| Gốc Gọi Hồn | Đền Gọi Hồn | Nhà hồi sinh lính (luật văn hóa TD 22.1) |
| Xưởng Rồng | Lò Rèn, Chợ Rừng (bản đầu) | Nơi nâng cấp món và mua trang bị bằng Vảy |
| Chớp, Hoàn hảo, Tốt, Vừa, Ẩu | Tan | Kết quả một từ. Từ không hết hạn nên không có "Tan" |

## 3. Sổ quyết định (23/10/2026)

| # | Quyết định | Lý do |
|---|---|---|
| D01 | Tên: Rồng Giữ Ải, EN Dragonhold, id `dragon-hold`, cổng 3005, `dragon.typing-game.local` | `gameId` ghi vĩnh viễn vào hồ sơ học; phải chốt trước sự kiện đầu tiên |
| D02 | Phe địch là **Bầy Héo**. Dấu hình chung: mảng vỏ Héo xám tro, khe nứt và mắt sáng vàng úa `#C8D24A`. Nguồn là **Hắc Vụ**: sương tím xám, không phát sáng | Vàng úa tách rõ khỏi tán tím lam của cảnh; một dòng MATCH cho mọi prompt quái |
| D03 | Đòn gõ là loại **Chữ**: không bị Giáp, Kháng chặn. Chỉ khiên chữ chặn chữ. Không có chí mạng ngẫu nhiên | Giáp làm khó quân ta, không làm khó tay gõ. Độ khó không đến từ tốc gõ |
| D04 | 1 W = sát thương một từ **Vừa** ở sức chuẩn của chương. Cấp Rồng trong ải không tăng P | Số từ để hạ quái không trôi trong ải |
| D05 | Bộ sinh đợt chỉ ở 02 §5. Ngân sách đợt đo bằng **tải gõ**; đe dọa (ĐĐ) chỉ dùng để chọn thành phần | Chương sau không đòi gõ nhanh hơn |
| D06 | ~~Nhịp đợt co giãn theo tốc gõ đo được, chỉ chậm lại (k_E ≥ 0,75)~~ **Thay bằng D23** | Bot 60 WPM thắng 100 % ở M0a: một chiều không đủ |
| D07 | Vàng theo ngân sách ải × số đường, chia cho quái theo ĐĐ | Không ngập vàng khi bầy đông |
| D08 | Trang bị bản đầu là **trang bị cố định**: không độ hiếm, không dòng phụ ngẫu nhiên, không rèn may rủi, không Chợ Rừng | Giá tính được; thêm sau khi có số đo người chơi |
| D09 | Chợ Học gộp vào Thẻ Ôn | Hai cơ chế ôn trùng nhau |
| D10 | Bậc máy không đổi luật sim: trần chữ, trần quái sống là hằng số | Máy yếu không được trận dễ hơn; mã băm và bot đúng mọi máy |
| D11 | Bảng phím chỉ dùng phím có trên Mac; đọc `event.code` | Máy chính của chủ dự án là Mac |
| D12 | Long Ấn chọn ở lần nghỉ kế, không mở bảng giữa đợt | Giảm việc phải nhìn khi đang gõ |
| D13 | Từ Kích để chế độ Tự tới hết C3 | Giảm quá tải đầu game |
| D14 | Mỗi từ chỉ gửi **một** sự kiện có chấm mỗi ải. Nghĩa ẩn theo số lần **nhớ** đúng, không theo độ thuộc thô | Gõ chép không được coi là đã thuộc |
| D15 | Lọc từ nhạy cảm khỏi mọi chỗ trong game | Kho có từ tục ở cấp thấp |
| D16 | Bản thử dọc (M0) tách khỏi chương 1 và chạy song song với việc tách game | Có thứ chơi được sớm |
| D17 | Kit chung **chép** từ Space; Space giữ bản gốc; shim Space hoãn | Không chạm lõi Space khi chưa cần |
| D18 | Không chuyển dữ liệu lưu của TD, Sinh Tồn sang host mới | Chưa có người chơi thật |
| D19 | Không dùng câu. "Câu dài" và D5 thay bằng **chuỗi chủ đề** (3–5 từ đơn cùng chủ đề) | Kho chưa có câu có nghĩa và IPA |
| D20 | Ải Ôn ở ải 9 và 19 mỗi chương | Ải nghỉ, ôn từ yếu |
| D21 | Bạch Long dẫn lời ở ải 1–10, vào trận từ ải 11 | Mỗi ải tối đa một ý mới |
| D22 | Model Rồng (v2, v3 medium, v4) vào bộ media riêng của game qua `pnpm media:push` | Game không phụ thuộc thư mục media của Space khi chạy |
| D23 | **Cân bằng nhiều yếu tố** theo `../BALANCE.md`: hồ sơ năng lực 13 yếu tố, nhịp k hai chiều (0,75–1,30) theo E hiệu dụng, bộ điều nhịp trong ải, Vùng Chữ tính bằng thời gian, áp lực liên tục, dải đích theo chế độ, bộ bot giống người. BALANCE.md §9.1 thay hàng k_E ở §4.4 | Chủ dự án (23/10): tránh quá dễ hay quá khó; cân theo tốc độ, độ chính xác và nhiều yếu tố khác |
| D24 | **Esc nhả khóa và bỏ các chữ đã gõ; số phím sai đã có trên từ vẫn giữ** tới khi từ xong hoặc mất (như Backspace), nên vẫn tính vào e và sự kiện học. Kit: `RouterRules.unlockErrors: "keep"` (24/10) | Esc không được xóa lỗi; câu này thay "Esc nhả khóa." ở 01 §3.3 |
| D25 | **Học trước không là lần nhớ.** Học trước gửi `review-card` kèm `hintUsed: true` (từ, IPA, nghĩa đang hiện). "Lần nhớ đúng" là lần đúng ở `meaning-recall`, `listening`, `review-card` **không** có `hintUsed` (24/10) | Gõ chép không được tính là thuộc (D14); áp cho cả bản lưu trên máy và mẫu đọc từ portal. Thay dòng "Lần nhớ đúng" ở 01 §6.3 và câu Học trước ở 01 §6.6 |
| D26 | **Tốc độ gõ E của ải không bao giờ ngầm là 35.** Chưa có số đo thì game hỏi tốc độ trước Học trước (thẻ tốc độ, gợi ý sẵn 35). Đã đo thì thẻ đặt số đo của hồ sơ lên đầu (E, a, CV). Đường dẫn có `?wpm=` thì dùng số đó. Hết mỗi ải, hồ sơ cập nhật theo BALANCE.md §2. Đã chọn theo đề xuất (24/10) | Rà soát 2: bot 25 WPM mở trang không có `?wpm` chơi với nhịp 35 và thua ở đợt 3; cùng bot với `?wpm=25` thắng, còn 82 % máu |

## 4. Số chuẩn

### 4.1 Đơn vị

```text
g(c)     = 1 + 0,02 × (c − 1)              // sức chuẩn theo chương: C1 1,00 · C10 1,18 · C20 1,38 · C26 1,50
P_ref(c) = 100 × g(c)                      // Hỏa lực P của "bộ đồ trung bình" ở chương c
1 W      = 0,9 × P_ref(c) = 90 × g(c) máu   // = một từ Vừa, Chuỗi bậc 0
Máu quái = W × 90 × g(c) × hệ số mức khó    // làm tròn số nguyên
```

- Sức phe ta (sát thương, máu của bẫy, nhà, lính) và sát thương quái lên phe ta cũng nhân g(c). Số trong 03 và 02 là số ở C1.
- Thời gian khống chế, tầm, tốc **không** nhân g(c).
- "Bộ đồ trung bình": tài khoản đi đường chính một lần, tiêu Vảy theo kịch bản mẫu, không chơi lại, không Lời Thề. Nguồn của g(c): Bậc Rồng (≤ +18 %), Cây Long Mạch nhánh Lửa (≤ +8 %), trang bị Vuốt (≤ +15 %). 1,18 × 1,08 × 1,15 ≈ 1,47 ≈ g(26).

### 4.2 Đòn gõ và sát thương

```text
D = P × M_q × M_c × (1 + Σ tăng từ Long Ấn, trang bị, Đài Khuếch Chữ, Đánh dấu)
```

| Kết quả (01 §3.7) | Điều kiện | M_q | Bằng bao nhiêu W |
|---|---|---|---|
| Chớp | e = 0 và t_k ≤ 0,85 × t_exp | 1,25 (+ đốt Lửa Chữ) | 1,39 |
| Hoàn hảo | e = 0 | 1,10 | 1,22 |
| Tốt | e = 1, từ ≥ 6 chữ | 1,00 | 1,11 |
| Vừa | e = 1, từ ≤ 5 chữ | 0,90 | 1,00 |
| Ẩu | e ≥ 2 (Cụm Ấn: e ≥ 3) | 0,60 | 0,67 |

| Bậc Chuỗi | 0 (0–4) | 1 (5–9) | 2 (10–19) | 3 (20–39) | 4 (40+) |
|---|---|---|---|---|---|
| M_c | 1,00 | 1,04 | 1,08 | 1,12 | 1,16 |

| Loại sát thương | Ai gây | Bị chặn bởi |
|---|---|---|
| **Chữ** | Đòn gõ, Long Hống, tia Viêm Đế, đòn lan của từ (Lửa Lan, từ cụm bầy) | Không gì, trừ khiên chữ (phải gõ hết lớp) |
| Vật lý (VL) | Lính, bẫy gai, bẫy nổ gỗ, đòn quái cận chiến | Giáp |
| Phép | Phun Lửa, Thiên Hỏa, Spit_Big, nhà phép, bẫy sét, băng; đòn phép của quái | Kháng phép |
| Chuẩn | Độc | Không gì |

```text
giảm = G / (G + 100), trần 75 %      Phá giáp: G × 0,5
Bậc giáp G0 / G1 / G2 / G3 = G 0 / 43 / 122 / 300 = giảm 0 / 30 / 55 / 75 %   (Kháng K0–K3 cùng thang)
```

- Quái và lính dùng bậc. Hai Rồng dùng số thô: Hỏa Long Giáp 20, Kháng 20; Bạch Long Giáp 40, Kháng 30 (01 §2.2).
- **Không có chí mạng ngẫu nhiên** ở bất kỳ đâu. Mọi RNG của sim theo seed.
- Đòn chạm ở tick +12 (0,2 s) sau phím cuối. Quái chết trước khi đòn chạm: đòn rẽ sang quái có chữ gần nhất trong 4 m, 50 %.
- Dễ tổn thương: Đánh dấu +15 %, trong Lồng Đá +20 %, cửa sổ phá thế boss +50 %. Khác nguồn thì nhân, cùng nguồn lấy mạnh nhất.

### 4.3 Sức gõ

```text
C(E) = 60 / (0,45 + 12 × (ℓ̄ + 1) / (E × d))     từ mỗi phút
d    = 0,86 (trộn: đã thuộc 1,00 · đang học, đến hạn 0,85 · từ mới 0,70)
ℓ̄    = độ dài trung bình theo dải E (01 §3.4): 4,5 chữ khi E < 45; 5,5 khi 45–64; 6,0 khi ≥ 65
```

- Bot 95 % chính xác (60 WPM: 97 %): trung bình một từ gây ~1,26 W; trừ phần thừa khi hạ quái nhỏ và lúc đổi mục tiêu (×0,80) còn **~1,0 W hiệu dụng mỗi từ**.

| E (WPM) | ℓ̄ | Giây mỗi từ | C (từ/phút) | W/s hiệu dụng | W mỗi phút |
|---|---|---|---|---|---|
| 25 | 4,5 | 3,52 | 17,0 | 0,28 | 17 |
| **35 (tham chiếu)** | 4,5 | 2,64 | **22,7** | **0,38** | **22,7** |
| 60 | 5,5 | 1,96 | 30,6 | 0,51 | 30,6 |

### 4.4 Tải gõ và nhịp

```text
W_gõ(đợt) = Σ W quái thường, tinh anh, tướng + số cụm bầy (mỗi cụm 1) + số lớp khiên chữ
Tải L     = W_gõ / (22,7 × phút của đợt)                 // đo ở E tham chiếu 35 WPM
k_E       = clamp(C(E) / 22,7 ; 0,75 ; 1,00)            // khoảng sinh × 1 / k_E
```

| Đợt trong ải | Tải trung bình đợt | Đỉnh ngắn (6–10 s) |
|---|---|---|
| Đợt 1 | 0,55–0,65 | — |
| Đợt giữa | 0,75–1,00 | ≤ 1,15 |
| Đợt cuối | 1,05–1,25 | ≤ L_đỉnh của ải (bảng 4.8), trần cứng 1,40 |
| Cửa sổ Cụm Ấn | ≤ 0,90 | — |
| Ải Ôn | ≤ 0,75 | ≤ 0,85 |

- Dải tải **giống nhau ở mọi chương**. Chương sau khó hơn nhờ thành phần quái, số đường, hào quang, kỹ năng, khắc chế. Số W gõ mỗi phút không tăng theo chương.
- Tải trên 1,0 là cố ý. Phần dư do bẫy, lính, nhà, kỹ năng gánh.
- k_E chỉ giãn **thời gian** (khoảng sinh, giờ đợt). Thành phần, W, mã băm của ải giữ nguyên. Ví dụ E = 25: k_E = 0,75, toán sinh thưa hơn 33 %.
- Bot của cổng "chuẩn thắng ẩu" chạy với k_E = 1 để so trên cùng nhịp.

**Nhịp theo hồ sơ (D23 thay k_E ở trên; BALANCE.md §4.1, §9.1). Số đang dùng từ M0a** (`src/content/rules.ts` `PACE`):

```text
E_eff = E × (0,6 + 0,4 × a²) × (1 − 0,5 × CV), giữ trong [0,7 E ; E]
k     = clamp(C(E_eff) / C_ref ; 0,75 ; 1,30)      C_ref = C(E_eff của bot Chuẩn 35 WPM, 95 %, CV 0,25) ≈ 19,6 từ/phút
T_a   = 8 s × biên / k, không dưới 2 lần thời gian một từ của người đó; + 1 thời gian từ cho mỗi từ thêm trong chuỗi của quái   // Vùng Chữ tính bằng thời gian
biên  = 1 + 3,0 × P(từ Ẩu ở độ chính xác a) + 0,6 × CV                // BALANCE.md §2 yếu tố 3 và 4
```

- Biên thời gian nhân cả T_a và độ chờ của Héo lan. Ví dụ: 85 %, CV 0,35 → × 1,88; 95 %, CV 0,25 → × 1,22; 99 %, CV 0,2 → × 1,12.
- E, a, CV lấy từ hồ sơ (D26): `?wpm=`, thẻ tốc độ, hoặc số đo của hồ sơ. Không có a, CV thì dùng 95 % và 0,25.

### 4.5 Loại ải, đợt, nghỉ

| Loại ải | Đợt | Dài mỗi đợt | Thời lượng ở 35 WPM |
|---|---|---|---|
| Ải dạy (C1 ải 1–4) | 4 | 40–50 s | 4–5 phút |
| Thường C1–C5 | 5 | 50–65 s | 6–7 phút |
| Thường C6+ | 6 | 50–70 s | 7–8,5 phút |
| Ải Tướng (5, 15) | 5 (C1–5) / 6; tướng ở đợt cuối | 50–70 s | 7–9 phút |
| Ải Ôn (9, 19) | 4 | 40–50 s | 3–4 phút |
| Boss nhỏ (10) | 4 đợt rồi boss | đợt 50–60 s; boss 60–90 s | 6–7 phút |
| Boss chương (20) | 5 đợt rồi boss (bảng 4.7) | đợt 50–65 s | 8–10 phút; C26 ≤ 12 phút |

| Mục | Số | Ghi chú |
|---|---|---|
| Nghỉ giữa đợt | Thường 20 s · Khó 15 s · Dễ chờ Enter | Đồng hồ chỉ chạy khi **không có bảng nào mở** |
| Lặng trước boss | 12 s | Không sinh toán mới; quái cũ vẫn đi |
| Hồi giữa đợt | Hỏa Long, Bạch Long +10 % máu tối đa | Tổ Ấm, Thư Viện: tối đa 20 % |
| Gọi sớm (Shift + Enter) | 2 Vàng mỗi giây còn lại, tối đa 40; +5 Long Nộ | |
| Bạch Long gục | Kiệt sức 15 s, dậy với 40 % máu | Không thua |
| Trần quái bay (theo ĐĐ đợt) | C1–3 15 % · C4–8 25 % · C9+ 30 % | Không ải nào quá 35 % số con |
| Tướng địch mỗi đợt | C1–4: chỉ Ải Tướng, boss nhỏ · C5–13: ≤ 1 · C14+: ≤ 2 · 3 chỉ ở đỉnh cuối ải boss từ C20 | W tướng ≤ 35 % W_gõ của đợt (40 % ở đợt cuối Ải Tướng) |

### 4.6 Bậc quái

| Bậc | W | Từ Hoàn hảo để hạ | ĐĐ mỗi con | Ghi chú |
|---|---|---|---|---|
| Bầy | 0,3–0,5 | 0 riêng (một từ cụm cho cả cụm 4–10 con) | 0,6–0,7 | |
| Nhỏ | 0,8–1,2 | 1 | 3–11 | Vừa (1,0 W) hạ được con ≤ 1,0 W |
| Vừa | 2–3 | 2–3 | 9–19 | |
| Nặng | 4–6 | 4–5 | 13–17 | |
| Khổng lồ | 8–10 | 7–9 | 21 | |
| Tinh anh | W × 1,6 | — | ĐĐ × 1,6 | |
| Đội trưởng | 5–7 | 5–6 | 30 | |
| Thống lĩnh | 10–12 | 9–10 | 60 | Từ C11 |
| Boss | 29–72 | bảng 4.7 | — | |

- Chữ trên quái nhiều W là chuỗi từ nối nhau (01 §3.5).
- Mức khó nhân W của mọi bậc trừ Bầy và Nhỏ (bảng 4.10). Nhỏ luôn chết sau 1 từ không Ẩu.

### 4.7 Boss: W và thời lượng

```text
W_boss = round(0,38 × 0,7 × t)    // t: giây đích ở 35 WPM; 0,7 vì hộ tống và cơ chế chiếm một phần sức gõ
```

| Chương | t đích | W_boss |
|---|---|---|
| C1–C5 (B01–B05) | 110–125 s | 30–33 (B04: 2 × 16) |
| C6–C12 (B06–B12) | 130–155 s | 35–41 |
| C13–C19 (B13–B19) | 160–180 s | 43–48 (B14: 18 + 26) |
| C20–C25 (song boss) | 195–210 s | 52–56 cho hai thân |
| C26 (B20) | 270 s | 72 |
| Boss nhỏ (ải 10) | 60–90 s | 16–24 |

- Người 25 WPM (k_E = 0,75) cần khoảng 1,35 lần t. Ví dụ B20: ~6 phút. Mức Dễ: W × 0,85.
- Ngưỡng pha của từng boss ở bảng 02 §4.3 (nguồn duy nhất).
- Thời gian báo trước đòn lớn: công thức 01 §3.6, tối thiểu 4 s; mức khó nhân theo bảng 4.10.

### 4.8 Đường cong 26 chương

ĐĐ đợt 1 (B_c) chỉ dùng để chọn **thành phần**. Tải gõ theo bảng 4.4. Số quái mỗi ải tăng nhờ bầy (một từ cho cả cụm) và nhờ bẫy, không nhờ tăng W gõ.

| C | g(c) | B_c | L_đỉnh | Đường tối đa | Quái mỗi ải thường | Quái sống đỉnh | Bầy (% số con) | Tinh anh (% số con · thuộc tính) |
|---|---|---|---|---|---|---|---|---|
| 1 | 1,00 | 18 | 1,15 | 1 | 100–140 | 20 | 40 % | 0 |
| 2 | 1,02 | 21 | 1,15 | 2 | 110–150 | 20 | 40 % | 0 |
| 3 | 1,04 | 25 | 1,20 | 2 | 120–160 | 25 | 45 % | 3 % · 1 |
| 4 | 1,06 | 28 | 1,20 | 2 | 130–170 | 35 | 45 % | 5 % · 1 |
| 5 | 1,08 | 32 | 1,25 | 3 | 140–190 | 50 | 50 % | 5 % · 1 |
| 6 | 1,10 | 37 | 1,25 | 3 | 150–200 | 50 | 50 % | 6 % · 1 |
| 7 | 1,12 | 41 | 1,25 | 3 | 160–210 | 60 | 55 % | 7 % · 2 |
| 8 | 1,14 | 46 | 1,30 | 4 | 170–230 | 70 | 55 % | 8 % · 2 |
| 9 | 1,16 | 50 | 1,30 | 4 | 180–240 | 80 | 60 % | 9 % · 2 |
| 10 | 1,18 | 55 | 1,30 | 4 | 190–260 | 100 | 60 % | 10 % · 2 |
| 11 | 1,20 | 60 | 1,30 | 4 | 200–270 | 100 | 60 % | 10 % · 2 |
| 12 | 1,22 | 65 | 1,30 | 4 | 210–280 | 100 | 65 % | 11 % · 2 |
| 13 | 1,24 | 70 | 1,35 | 4 | 220–300 | 110 | 65 % | 11 % · 2–3 |
| 14 | 1,26 | 75 | 1,35 | 4 | 230–310 | 120 | 65 % | 12 % · 2–3 |
| 15 | 1,28 | 80 | 1,35 | 4 | 250–330 | 160 | 70 % | 12 % · 3 |
| 16 | 1,30 | 85 | 1,35 | 4 | 260–350 | 160 | 70 % | 13 % · 3 |
| 17 | 1,32 | 90 | 1,35 | 4 | 270–360 | 160 | 70 % | 13 % · 3 |
| 18 | 1,34 | 95 | 1,40 | 4 | 280–380 | 160 | 75 % | 14 % · 3 |
| 19 | 1,36 | 100 | 1,40 | 4 | 290–390 | 160 | 75 % | 14 % · 3 |
| 20 | 1,38 | 105 | 1,40 | 4 | 330–430 | 220 | 80 % | 15 % · 3–4 |
| 21 | 1,40 | 111 | 1,40 | 4 | 330–440 | 220 | 80 % | 15 % · 3–4 |
| 22 | 1,42 | 117 | 1,40 | 4 | 340–450 | 220 | 80 % | 15 % · 3–4 |
| 23 | 1,44 | 122 | 1,40 | 4 | 340–460 | 220 | 80 % | 15 % · 3–4 |
| 24 | 1,46 | 128 | 1,40 | 4 | 350–470 | 220 | 80 % | 15 % · 3–4 |
| 25 | 1,48 | 134 | 1,40 | 4 | 350–480 | 220 | 80 % | 15 % · 3–4 |
| 26 | 1,50 | 140 | 1,40 | 4 | 350–500 | 220 | 80 % | 15 % · 4 |

- **Quái sống đỉnh** là trần của luật sim, mọi bậc máy (D10). Chạm trần thì toán mới chờ ở cổng; đồng hồ đợt không dừng; tải được tính lại.
- Hệ số vị trí trong chương s(i) và L_đỉnh của từng ải: 04 §4.1.
- Phần sát thương và khống chế của phe ta theo chương: cổng G8 (mục 7), đo bằng bot mỗi chương.

### 4.9 Kinh tế

**Vàng (trong ải, mất khi hết ải):**

```text
Vàng ải = 200 (đầu ải; Thư Viện ≤ +100) + 900 × f_đường × f_loại
f_đường: 1 đường 1,00 · 2 đường 1,25 · 3 đường 1,45 · 4 đường 1,60
f_loại : Ải dạy 0,6 · Thường 1,0 · Ải Tướng 1,1 · Ải Ôn 0,6 · Boss nhỏ 1,1 · Boss chương 1,2
Chia 900 × f: hạ quái 60 % (theo tỉ lệ ĐĐ từng con; cụm bầy trả một lần) · hết đợt 25 % (đợt sau +10 % so với đợt trước) · gọi sớm, Học trước, biến cố 15 %
```

- Giếng Vàng nằm ngoài ngân sách này, trần +12 %. Học trước: +5 mỗi từ đúng, tối đa +40.
- Ví dụ: C1, 1 đường, ải thường: 1.100 Vàng. C14, 4 đường: 1.640 Vàng.
- Dựng tối đa (mọi ô, cấp 3 = 2,7 × giá gốc): 1 đường ~3.100 Vàng; 4 đường ~9.800 Vàng. Vàng ải chỉ đủ **15–35 %**: luôn phải chọn.
- Vàng dư cuối ải: đổi Vảy = min(3; floor(dư / 100)). Chuẩn cả ải ≥ 95 %: +10 % Vảy của ải.

**Ngoài ải (giữ mãi):**

| Tiền | Nguồn | Tổng ước tính đường chính | Tiêu vào |
|---|---|---|---|
| Vảy Rồng | Sao lần đầu 3 / 5 / 8; boss +20; Ải Tướng +5; chơi lại 30 %; thua giữ 30 % | ~4.700 | Cấp món 1–5 (31 món đặt được: 13 bẫy, 11 nhà, 7 lính; × 120 = 3.720) và trang bị cố định (10 ô × 320 = 3.200). Tổng 6.920: đủ ~68 % |
| Tri Thức | Từ mới gõ đúng lần đầu +1; từ đến hạn đúng +1; Thẻ Ôn +1; Ải Ôn ×2; Huy hiệu Học +5 | ~25 mỗi ải; trần mềm 300 mỗi ngày | Thư Viện Rồng 12 bậc, giá 50 × 1,35^(k − 1), tổng ≈ 5.100: mở hết ở khoảng ải 200–250 |
| XP Rồng, Sao | 04 §8.1, §8.2 | Bậc 36 ở C26; 1.560 Sao | Bậc Rồng, Cây Long Mạch |

- Giá cấp món: cấp 2 / 3 / 4 / 5 = 10 / 20 / 35 / 55 Vảy, mỗi cấp +6 % hiệu lực chính (trần +24 %).
- Trang bị cố định: mua 40 Vảy, nâng cấp 2–5 = 30 / 50 / 80 / 120 Vảy.

### 4.10 Mức khó

| | Dễ | Thường | Khó |
|---|---|---|---|
| W quái (trừ Bầy, Nhỏ) | × 0,85 | × 1,00 | × 1,15 |
| Sát thương quái | × 0,7 | × 1,0 | × 1,2 |
| Tốc quái | × 0,9 | × 1,0 | × 1,05 |
| Khoảng sinh | × 1,15 | × 1,0 | × 1,0 |
| Nghỉ đợt | Chờ Enter | 20 s | 15 s |
| Báo trước đòn | × 1,5 | × 1,0 | × 0,85 |
| Nghĩa trên thẻ | Luôn hiện | Theo 01 §6.3 | Chỉ lần gặp đầu |
| Nguyền Chuẩn (02) | Tắt | Bật từ C12 | Bật từ C12 |
| Vảy thưởng | × 0,8 | × 1,0 | × 1,25 |
| Vương Miện, Lời Thề | Không | Có | Có |
| Héo lan (BALANCE.md §5) | × 0,5 | × 1,0 | × 0,9 |
| Dải đích của bộ điều nhịp (BALANCE.md §3) | Thư giãn | Cân bằng | Thử thách |

- Đổi mức ở Lều Chuẩn Bị trước mỗi ải. Không đổi giữa ải. Sao tính như nhau ở mọi mức.
- Hồ sơ trẻ em mặc định Dễ. Thua 2 lần liền ở một ải: gợi ý hạ một mức, không ép.
- Héo lan ở Khó nhẹ hơn Thường (× 0,9) vì Khó đã nặng hơn nhờ các hàng khác của bảng và dải Thử thách.
- **Héo lan (áp lực liên tục, D23; số từ M0a, `rules.ts` `PRESSURE`):** mỗi nhịp 2 s, mỗi mục tiêu còn chờ trong Vùng Chữ rỉ Héo vào Hỏa Long (sát thương chuẩn). Mục tiêu còn chờ: từ của nó đã hiện lâu hơn độ chờ (một từ ở tốc E thô của người chơi × biên thời gian, mục 4.4), hoặc nó đứng trong vùng mà chưa có từ. Một cụm bầy là một mục tiêu.
  - 13,5 HP/s trong Vùng Chữ; 27 HP/s trong Vòng Nguy (10 m); 50 % mức vùng khi lính của ta đang chặn nó. Tối đa 2 mục tiêu mỗi nhịp.
  - × g(c) × hệ số Héo của mức (bảng trên) × √k × độ dày theo đợt: 25 % ở đợt 1, cộng 12 % mỗi đợt (133 % ở đợt 10).

## 5. Ngân sách chữ

```text
A        = số chữ cái có ≥ 3 từ hợp lệ trong bộ từ của ải (luật TD 6.5)
N_max    = min(16 ; A − 3)                  // tổng chữ sống mọi loại
K_quái   ≥ max(6 ; 0,6 × N_max)              // suất chữ dành cho quái, trong đó 2 suất khẩn
S_khác   ≤ 4                                 // mọi chữ không thuộc quái cộng lại
```

| Nguồn chữ không thuộc quái | Trần riêng | Khi nào hiện |
|---|---|---|
| Chữ Chiêu | 2 | Tối Thượng khi Long Nộ đầy, và một kỹ năng sẵn sàng có hồi lâu nhất. Kỹ năng khác dùng Alt + số |
| Từ Khẩn | 1 | 01 §3.6 |
| Từ Trợ | 2 | Cần Bạch Long đang đứng |
| Từ Kích | 0 (C1–3, chế độ Tự) · 1 (C4–5) · 2 (C6+) | Không hiện khi ≥ 12 chữ quái đang sống |
| Pháo Hiệu Rồng | 1 | Khi người chơi dùng |
| Vật bản đồ, mục tiêu, biến cố | 1 | Theo luật ải |

- Ví dụ cấp từ 1: A ≈ 16 → N_max = 13, K_quái ≥ 8, chữ khác ≤ 4.
- **Cửa sổ Cụm Ấn, mưa từ CN:** tối đa 4 từ boss cùng lúc, lấy từ suất quái. Không sinh Từ Trợ, Từ Kích mới.
- **Chú ý:** ngoài chữ quái, trên màn chỉ có **một loại chữ đặc biệt mới** tại một lúc (loại người chơi gặp chưa quá 3 lần).
- Hệ chưa mở (04 §6) thì không có chữ và không giữ chữ đầu.
- Bot ghi nghẽn chữ đầu theo từng nguồn.

## 6. Bảng phím (nguồn duy nhất)

Phím lệnh đọc theo `event.code`, không theo ký tự (Option + số trên Mac sinh ¡ ™ £). "Alt" là Option trên Mac. Linux dùng Shift thay Alt cho phím số, như TD 8.3. Không dùng Insert, Delete, PageUp, Pause, F1–F12.

| Việc | Phím | Ghi chú |
|---|---|---|
| Gõ | a–z | Chỉ để gõ. Phím IME đang soạn, phím giữ lặp, phím có Ctrl hoặc Cmd bị bỏ |
| Xóa một chữ của từ đang khóa | Backspace (Mac: delete) | |
| Nhả khóa → đóng bảng → menu dừng | Esc | Theo thứ tự. Esc cũng là phím tạm dừng |
| Nghe lại từ đang khóa hoặc vừa hạ | Tab | Chỉ việc này trong trận |
| Bắt đầu ải; nộp ô trả lời | Enter | Ô trả lời (Cụm Ấn, Hỏi Nghĩa) mở thì Enter nộp |
| Gọi đợt sớm | Shift + Enter | |
| Kỹ năng 1–4 | Alt + 1…4 | |
| Tối Thượng | Alt + 5 (Viêm Đế), Alt + 6 (Lời Thề Bạch Vũ) | |
| Đồ tiêu hao | Alt + 7 / 8 / 9 | |
| Camera về chuẩn; bấm lại: toàn cảnh 75° | Alt + 0 | |
| Xoay, nghiêng camera | ← → / ↑ ↓ | Khi không ở chế độ đặt hoặc sửa |
| Zoom | Alt + ↑ / ↓ | |
| Tua nhanh × 2 (bật, tắt) | Alt + → | Chỉ khi nghỉ, hoặc không còn chữ sống và quái trong Vùng Chữ (06 §10) |
| Chọn món trong dải Bộ Mang Theo, vào chế độ đặt | 1…9 (không Alt) | Ô gợi ý sáng lên |
| Trong chế độ đặt | ← → ↑ ↓ đổi ô · Enter đặt · Esc hủy | Phím chữ vẫn gõ quái |
| Chế độ sửa món đã đặt | `` ` `` (Backquote) | Mũi tên đổi món · `=` nâng (bấm 2 lần) · `-` bán (bấm 2 lần) · Esc thoát |
| Thẻ thông tin quái đang khóa | Giữ Alt | |
| Chọn Long Ấn; chọn đáp án Thẻ Ôn | 1 / 2 / 3 | Chỉ khi bảng đó mở (lúc nghỉ); phím số thuộc bảng |
| Lều Chuẩn Bị | Mũi tên chọn · Enter thêm, bỏ · Tab đổi cột · Esc lùi | Không có trận, Tab không trùng |
| Màn ngoài trận | Mũi tên, Enter, Esc | 06 §4 |

- Chuột: trái vào quái là đánh dấu; trái vào ô là đặt; phải kéo xoay camera; lăn chuột zoom. Mọi việc có đường bàn phím.
- Màn cài đặt có **đổi phím** cho mọi phím lệnh không phải chữ (06 §3).
- Kiểm bằng `dh-keyboard-only` trên bố cục Mac và Linux.

## 7. Cổng bot (bảng duy nhất)

Bot: 25 WPM 95 %, 35 WPM 95 %, 60 WPM 97 %, trừ khi ghi khác. "Đồ TB" là bộ đồ trung bình (mục 4.1). Mức Thường, trừ khi ghi khác. 20 seed mỗi lượt.

| # | Cổng | Bot | Phạm vi | Ngưỡng |
|---|---|---|---|---|
| G1 | Thắng chuẩn | 35, đồ TB | Ải thường, Ải Tướng | Thắng 75–90 % |
| G2 | Không quá dễ | 35, đồ TB | Từ C3 | 3 sao ≤ 60 % |
| G3 | Người chậm đi được | 25, đồ TB | C1–C5 / C6+ | Thắng ≥ 70 % / ≥ 55 %; mức Dễ ≥ 75 % |
| G4 | Boss | 35 / 25, đồ TB | Ải boss | 35: thắng 60–85 %; 25: ≥ 45 % (Dễ ≥ 70 %) |
| G5 | Hỗ trợ cần thiết | 35, chỉ gõ, không mua | Ải 1–10 / ải 21+ | Thắng ≥ 70 % / thua ≥ 60 % |
| G6 | Gõ là sức chính | 0 WPM, mua tối ưu | Từ ải 2 | Thua 100 %, trước hết đợt 3 |
| G7 | Chuẩn thắng ẩu | 35 WPM 98 % so với 50 WPM 85 %, k_E = 1 | 5 ải mẫu mỗi chương | Bot chuẩn hạ quái nhanh hơn |
| G8 | Phần phe ta | 35, đồ TB | Mỗi chương | Sát thương không do gõ 20–35 %, trần 40 %; khống chế của bẫy nằm trong ±25 % mức C1 |
| G9 | Không ngộp | Mọi bot | Mọi ải | Tải đỉnh ≤ 1,40; cửa sổ Cụm Ấn ≤ 0,90; chữ sống ≤ N_max |
| G10 | Đọc được | 35 | Cấp từ ≤ 3, bố cục 4 đường | Rơi xuống tầng 2 chữ đầu < 1 lần mỗi phút |
| G11 | Không mất công gõ | 35 | Mọi ải | Mất khóa vì nguồn khác ≤ 5 % số khóa |
| G12 | Học | 35 | Mọi ải | Đủ từ mới đã hẹn; mỗi từ mới gặp ≥ 2 lần; không từ mới trên quái bay, quái nhanh, quái đang đánh; không từ mới nào lên độ thuộc ≥ 70 trong ải đầu gặp nó |
| G13 | Vàng | 35 | Mọi ải | Vàng ải trong ±15 % công thức 4.9; vàng dư ≤ 15 % |
| G14 | Món | Tham Bẫy, Tham Lính, Tham Nhà | Mọi ải từ C3 | Mỗi bot thắng ≥ 40 %, không hơn Cân Bằng quá 15 điểm %; mỗi món có trong 5–70 % bộ tốt nhất |
| G15 | Khống chế | 35 | Mọi ải | Mỗi quái bị khống chế cứng ≤ 35 % thời gian sống |
| G16 | Long Nộ | 35 | Từ C1 ải 15 | Tối Thượng mỗi 90–110 s |
| G17 | Thời lượng | 35 | Mọi ải | Trong dải bảng 4.5 |
| G18 | Ải Ôn là nghỉ | 25 | Ải 9, 19 | Thắng ≥ 90 % |
| G19 | Khắc chế có trước | `stages:validate` | Từ C1 ải 6 | Không loài, tướng nào ra trước khi có ít nhất một món hoặc kỹ năng khắc chế ngoài gõ (03 §0.3) |
| G20 | Chú ý | 35 | Mọi ải | Quyết định không phải gõ ≤ 6 mỗi phút trong đợt |
| G21 | Đường cong | 35 | Mọi ải | Độ khó đo được lệch đường cong ≤ 15 % |
| G22 | Dấu Thách | 35 | Ải có Dấu Thách | Đạt ≥ 25 %; không mục tiêu phụ nào 0 % |

- Ải không đạt: chỉnh hệ số trong dữ liệu (±10 %) hoặc đổi seed. Không sửa mã.
- **Ngoại lệ của bản thử dọc M0 (người điều phối chốt ngày 23/10/2026):**
  - G5 trên bản đồ M0 (10 đợt, có tướng) dùng ngưỡng của DESIGN §9: chỉ gõ thắng ≤ 40 %. Ngưỡng ≥ 70 % ở ải 1–10 của bảng trên áp dụng cho chương 1 thật (M2), nơi ải ngắn hơn và dạy dần.
  - Máu Hỏa Long cấp 1 ở M0 là 460 (bot chỉnh), thay mức 1.000 của 01 §2.2. Đây là số tạm, xem lại sau buổi chủ dự án chơi thử.
  - Đợt 10 của M0 được phép chạm đỉnh tải 1,40 (trần cứng), vượt trần 1,15 của đợt giữa C1–C2. Đo được sau vòng cân bằng 23/10: đỉnh 1,39 (tải trung bình đợt 1,15).
  - Cổng B1–B9 của `../BALANCE.md` §7 áp dụng cho M0 cùng G1–G9.
- Cổng in báo cáo từ M1. Thành cổng cứng khi một lát phát hành được khóa.

## 8. Hiệu năng sim và sức chạy bot

| Mục | Đích |
|---|---|
| Một bước sim 60 Hz ở đỉnh 300 quái, 30 bẫy, 10 nhà, 8 lính | ≤ 0,3 ms (headless) |
| Trung bình cả ải, headless | ≥ 200 lần thời gian thực |
| Lọc giải tích trước khi chạy sim | Tải gõ và Vàng tính bằng công thức; ải lệch > 25 % bị loại ngay |
| Kiểm cổng mỗi lần đổi dữ liệu | 5 ải mẫu mỗi chương (130 ải) + ải bị đổi × 20 seed × 5 bot ≈ 13.000 lượt ≈ 7,6 giờ CPU ≈ 45 phút trên 10 nhân |
| Tìm bộ đồ của bot | 2 ải đại diện mỗi chương × 3 seed × 50 thứ tự mua ≈ 7.800 lượt ≈ 4,5 giờ CPU |
| Khóa một lát phát hành | Mọi ải của lát × 20 seed × 5 bot; chạy đêm, song song nhiều nhân |
