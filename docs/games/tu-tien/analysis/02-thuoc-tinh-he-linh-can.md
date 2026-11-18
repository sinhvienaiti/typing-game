# Tu Tiên thủ ải thú triều — 02. Thuộc tính, hệ linh căn và mô hình chỉ số

> **Phạm vi:** chỉ số nhân vật, tài nguyên (sinh lực, linh lực, "niệm lực"), linh căn và ngũ hành, khắc chế, trường phái vũ khí, kháng, chí mạng, hệ của thú, trần chỉ số.
> **Nguồn:** video QCBH chủ dự án quay (khung hình 0:00–0:12, 2:16, 3:20–4:16), Codex V2.2 (`TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md`), tài liệu và mã của Rồng Giữ Ải, `docs/games/BALANCE.md`.
> **Ký hiệu nguồn:** [video], [Codex §x], [web: url], [trí nhớ] (nhớ từ trước, chưa kiểm). **Mọi con số trong mục 4–5 là số thử**, chưa có dữ liệu chơi thật.
> **Trạng thái:** phân tích và đề xuất. Chưa sửa mã.

## 1. Tóm tắt

- QCBH có khoảng **37 con số** trên một trang nhân vật [video 0:00]. Game thủ ải gõ chữ cần đọc được trong **1 giây**. Đề xuất: **HUD 3 thanh + 6 chỉ số chính + 5 chỉ số phụ**, bỏ hẳn nhóm chỉ số chỉ phục vụ thế giới mở (thọ mệnh, tâm tình, cước lực, kỹ nghệ…).
- **Dùng ngũ hành 5 hệ (Kim, Mộc, Thủy, Hỏa, Thổ)**, không chép 6 linh căn của QCBH. Lôi, Phong, Băng là **dị hệ** mở sau, mỗi dị hệ thuộc một hệ gốc trong vòng khắc. Lý do: có vòng tương sinh, tương khắc kinh điển, người Việt đọc được ngay, và là bản sắc riêng.
- **Hai vòng, hai việc:** tương **khắc** quyết định sát thương lên thú (chọn ô nào để gõ). Tương **sinh** tạo phản ứng giữa hai đòn liên tiếp (phối hợp trong đội, hoặc giữa chủ hệ và phụ hệ khi chơi solo).
- **Không có chí mạng ngẫu nhiên.** "Hội tâm" là **từ gõ Chớp** (đúng hết, nhanh hơn nhịp riêng của người chơi). "Bạo kích" là chỉ số RPG nhân thêm cho từ Hội tâm. Đây là luật D03 của Rồng Giữ Ải, chuyển sang cho tu tiên.
- **Đòn gõ bỏ qua Giáp. Hệ thì có tác dụng.** Giáp chỉ chặn đánh nền, pet và trận. Hai loại kháng của QCBH (kháng công pháp, kháng linh căn) gộp thành **Giáp** và **Kháng hệ**.
- **"Niệm lực" tách làm hai:** **Thần thức** là sức chứa hành trang trước trận (đan, pháp bảo). **Định Tâm** là thanh trong trận, nạp bằng chất lượng từ, dùng cho Tuyệt kỹ.
- **MVP 3 hệ người chơi (Thủy, Mộc, Hỏa)** tạo đủ một chuỗi sinh Thủy→Mộc→Hỏa, vừa khít trận Tam Tài 3 người. Thú có đủ 5 hệ dưới dạng thẻ dữ liệu.
- **Tái dùng nhiều:** công thức giáp `G/(G+100)` trần 75 %, bảng hệ số kết quả từ, trạng thái giảm dần, bot gõ giống người đều đã có trong `games/dragon-hold` và `shared/game-kit/balance`.

## 2. QCBH làm thế nào (chỉ phần liên quan)

### 2.1 Trang nhân vật trong video

Đọc từ khung `t000` phóng to [video 0:00–0:12]:

| Nhóm | Chỉ số (giá trị trong video) | Vai trò, theo nhãn và theo bối cảnh |
|---|---|---|
| Thuộc tính | Thọ mệnh 19/120 · Tâm tình 77/100 · Thể chất 99/100 · Tinh lực 14/80 | Tuổi và tuổi thọ; tâm trạng; thể trạng/thương tích; sức hành động ngoài thế giới [video]. Tâm tình giảm khi đọc sách công pháp; thọ mệnh khởi đầu 80 năm, tăng khi đột phá [web: gamepretty] |
| Thuộc tính | Sinh lực 810/916 · Linh lực 213/253 · Niệm lực 194/242 · May mắn 80 · Ngộ tính 101 | 3 thanh trong trận và 2 chỉ số ngầm [video]. Ngộ tính là tốc học và lĩnh ngộ công pháp; May mắn là xác suất việc tốt; cả hai không tăng vĩnh viễn sau khi tạo nhân vật [web: gamepretty] |
| Chiến đấu | Tấn công 74 · Phòng ngự 39 · Cước lực 600 · Kháng công pháp · Kháng linh căn | Cước lực là tốc độ đi trên bản đồ thế giới, Di tốc là tốc độ trong trận [web: gamepretty] |
| Chiến đấu | Hội tâm 86 · Hộ tâm 63 · Di tốc 446 · Bạo kích 250 % · Kháng bạo 50 % | Hội tâm là chỉ số tỉ lệ chí mạng, Hộ tâm là chống chí mạng, Bạo kích là hệ số sát thương chí mạng, Kháng bạo giảm hệ số đó [trí nhớ, khớp nhãn trong video] |
| Công pháp | Đao 5 · Thương 6 · Kiếm 67 · Quyền 28 · Chưởng 4 · Chỉ 5 | Độ tinh thông 6 loại vũ khí. Người chơi trong video dồn vào Kiếm [video] |
| Linh căn | Hỏa 18 · Thủy 3 · Lôi 6 · Phong 15 · Thổ 15 · Mộc 16 | 6 linh căn quyết định linh kỹ hệ nào mạnh lên [web: earlyguides tóm tắt qua tìm kiếm; trí nhớ]. **Không có Kim** [video] |
| Kỹ nghệ | Luyện đan 37 · Luyện khí 47 · Phong thủy 34 · Họa phù 14 · Dược liệu 17 · Khoáng thạch 39 | Nghề ngoài trận [video] |
| Hành trang | Giới chỉ, Tọa kỵ, Phục sức; 5 ô đạo cụ | Ghi chú trong game: 5 ô đạo cụ mang vào trận, chỉ chứa đan dược và pháp bảo, mỗi ô tối đa 5 đan. **"Hạn mức Niệm lực cao nhất 99/242"**: tổng niệm lực của đồ mang theo bị trần bởi Niệm lực tối đa [video 0:00] |

### 2.2 Trong trận

- HUD đáy có 3 thanh **Sinh lực / Linh lực / Niệm lực**, 5 ô đan, 4 ô chiêu (võ kỹ hồi 0,2–0,3 s, linh kỹ, tuyệt kỹ, thân pháp) và nút "Trốn" [video 2:16, `t136`].
- Linh lực tụt từ 213 còn 153 sau vài chiêu [video `t000` → `t136`]: chiêu tốn linh lực.
- Niệm lực từ 194 còn 172 trong trận boss [video `boss_06`]. Theo trí nhớ, niệm lực bị tiêu khi dùng pháp bảo [trí nhớ, chưa kiểm].
- Số chí mạng hiện riêng: "Bạo Kích −82", "Bạo Kích −23" [video `t136`, 1:40–3:20]. Chí mạng là ngẫu nhiên theo tỉ lệ [trí nhớ].
- Combat nhìn từ trên xuống, kiểu bắn đạn dày (bullet hell) [web: en.wikipedia.org/wiki/Tale_of_Immortal].

### 2.3 Hệ, khắc chế, mệnh cách

- Theo những gì kiểm được, **QCBH không có vòng khắc kiểu kéo–búa–bao giữa 6 linh căn.** Linh căn là trục **đầu tư** (hệ nào mạnh), không phải trục **đối đầu** [trí nhớ; không tìm được nguồn web nói ngược lại].
- Mệnh cách đầu game: chọn 3 trong danh sách có thể đổi lại; có phẩm xám → đỏ; nhiều mệnh cách đổi chỉ số lấy cái giá (ví dụ tăng ngộ tính, giảm sức hút) [web: gamepretty; wikipedia]. Lớp phủ của stream ghi "NTCM dự kiến" là các mệnh cách nhận sau khi đột phá, ví dụ một mệnh cách cộng lôi lực khi đánh xa [video overlay; trí nhớ: NTCM nhận ở mốc đột phá].
- Cảnh giới: tên video có "Kết tinh chi lộ" [video]. Danh sách 10 cảnh giới và chênh lệch cảnh giới làm đổi sát thương là [trí nhớ, chưa kiểm].
- **Không tìm được nguồn xác nhận sự kiện "thú triều" trong QCBH** [web: tìm kiếm không ra]. Thủ ải thú triều là luật của dự án, không phải sao chép.

### 2.4 Bài học cho ta

| QCBH làm | Giữ ý | Đổi cho game gõ chữ thủ ải |
|---|---|---|
| Rất nhiều chỉ số, đọc trong menu lúc rảnh | Cảm giác "nhân vật có chiều sâu" | Chiều sâu nằm ở trang chi tiết. Trong trận chỉ đọc 3 thanh và 1 viền màu trên ô chiêu |
| Linh căn = hệ nào mạnh | Đầu tư theo hệ | Thêm **vòng khắc** để hệ thành **quyết định trong trận**, không chỉ là con số build |
| Chí mạng ngẫu nhiên + Bạo kích | Số to, cảm giác sướng | Hội tâm đến từ **tay gõ**, không đến từ xúc xắc |
| Niệm lực trần hành trang | Đánh đổi mang gì vào trận | Giữ trần (Thần thức), bỏ thanh thứ ba trong trận |
| Kháng công pháp / kháng linh căn | Hai đường giải khác nhau | Giáp (đánh nền) và Kháng hệ (chiêu hệ) |

## 3. Codex V2.2 nói gì về mảng này

Codex **không có mục riêng** cho linh căn, ngũ hành hay bảng chỉ số. Những gì liên quan nằm rải rác:

| Mục | Codex nói | Đề xuất | Lý do |
|---|---|---|---|
| §14.2 dòng Ngũ Hành | Trận 5 vị trí, "chuyển hóa/khắc chế theo luật" | **Giữ, làm mở rộng** | Luật cụ thể có ở mục 4.4 dưới đây. Trận 5 người để sau 2–3 người |
| §14.2 câu cuối | Thuộc tính đến từ kỹ năng, pháp bảo, bot; không khóa vào nhân vật hiếm | **Giữ** | Hệ phải lấy được qua pháp bảo, đan, bot; không bán hệ |
| §16 | Kháng nguyên tố đổi chiến thuật; tránh miễn nhiễm tuyệt đối | **Giữ, thêm số** | Sàn hệ số 0,60 (mục 4.3) |
| §21 Chí mạng | "Trần xác suất/hệ số theo giai đoạn" | **Sửa** | Bỏ xác suất. Hội tâm = từ Chớp. Chỉ giữ hệ số Bạo kích có trần |
| §21 các dòng khác | Bucket damage, CDR ≤ 30 %, giảm sát thương không bất tử, khiên, hút máu có quota | **Giữ, gán số** | Bảng trần ở mục 4.7 |
| §11 | 24 trường phái thiết kế tay | **Sửa** | Gộp thành **hình đòn × hệ** (mục 4.5): 5 hình × 5 hệ sinh ra combo từ dữ liệu, rồi mới làm tay vài trường phái đặc biệt |
| §9.1 | Đánh nền 15–30 % output | **Giữ** | Giáp chỉ chặn phần này (mục 4.3) |
| §10.2 | Hồ sơ K0–K6 (F/S/R/H) | **Giữ** | Dùng làm mốc cho hệ số tăng g(K) |
| §12.5 | Cùng ID lấy mạnh nhất, cùng nhóm cộng có trần | **Giữ** | Áp cho buff hệ và kháng hệ |
| §17.1 | Ngộ tính tách khỏi mức thuộc tiếng Anh | **Giữ** | Ngộ tính chỉ dùng ngoài trận (tu luyện) |
| §22.1 | Chi phí từ theo độ dài; ô phòng thủ không luôn nhận từ khó | **Giữ, mở rộng** | Ô khắc hệ cũng không được nhận từ dài hơn |
| §26.5 | Ngữ pháp VFX theo hệ | **Giữ** | Dùng chung cho nhận diện hệ của thú |
| §1.6 "định tâm" khi đứng yên trong trận | Thưởng RPG cho đứng yên | **Sửa tên** | Thanh Định Tâm ở mục 4.2 nạp bằng **chất lượng từ**. Thưởng đứng yên đổi tên "Tĩnh tọa", để hai thứ không trùng tên |

## 4. Đề xuất cho game thủ ải thú triều

### 4.1 Đổi chỉ số QCBH sang mô hình gọn

| QCBH | Ta | Ghi chú |
|---|---|---|
| Sinh lực | **Sinh lực** (`hp`) | Giữ |
| Linh lực | **Linh lực** (`ling`) | Giữ; nạp bằng chữ đúng (4.2) |
| Niệm lực | **Thần thức** (`senseCap`, ngoài trận) + **Định Tâm** (`focus`, trong trận) | Tách sức chứa hành trang khỏi thanh chiêu cuối |
| Tấn công | **Công** (`atk`) | Gốc 100 ở K0 |
| Phòng ngự | **Thủ** (`def`) | Giảm = Thủ/(Thủ+100), trần 75 % |
| Di tốc | **Thân pháp** (`move`) | m/s trong trận |
| Bạo kích | **Bạo kích** (`critMul`) | Chỉ nhân cho từ Hội tâm |
| Hội tâm | Không còn là chỉ số | Hội tâm = từ Chớp |
| Hộ tâm, Kháng bạo | Chỉ thú tinh anh và boss có `critResist` | Người chơi không cần |
| Kháng công pháp | **Giáp** (`armor`), chủ yếu ở thú | Chặn đánh nền, pet, trận |
| Kháng linh căn | **Kháng hệ** (`elemRes[e]`) | Theo từng hệ |
| 6 linh căn số | **Linh căn**: chủ hệ + phụ hệ + phẩm 1–5 | Một biểu tượng thay 6 con số |
| 6 công pháp vũ khí | **Hình đòn** của từng chiêu; tinh thông theo chiêu | Không có 6 thanh tinh thông |
| Ngộ tính | **Ngộ tính** (chỉ ngoài trận) | Thuộc mảng tu luyện, có trần |
| Thọ mệnh, Tâm tình, Thể chất, Tinh lực, May mắn, Cước lực | **Bỏ** | Không có thế giới mở; không giới hạn giờ chơi của người học; may mắn là RNG không công bằng |
| 6 kỹ nghệ | **Bỏ khỏi trang chỉ số** | Nếu có luyện đan, họa phù thì thuộc mảng shop, kinh tế |

**Bố cục đọc nhanh:**

- **HUD trong trận:** thanh Sinh lực, thanh Linh lực, vòng Định Tâm quanh ô Tuyệt kỹ. Mỗi ô chiêu có **viền hệ** (biểu tượng + màu) và **đèn khắc** (sáng khi mục tiêu hiện tại bị hệ đó khắc).
- **Trang 1 nhân vật (6 số):** Công, Thủ, Thân pháp, Bạo kích, Hồi linh, Linh căn (biểu tượng chủ/phụ + phẩm).
- **Trang 2 chi tiết (5 số):** Kháng hệ ×5 (một hàng biểu tượng), Xuyên giáp, Giảm hồi chiêu, Thần thức, Ngộ tính.
- Tổng 13 số, so với khoảng 37 số của QCBH.

### 4.2 Tài nguyên và nhịp gõ (số thử)

| Tài nguyên | Nạp | Tiêu | Trần |
|---|---|---|---|
| Linh lực (gốc 100 ở K0) | +3/s tự hồi; **+1,5 cho mỗi ký tự đúng của từ đã hoàn thành**, tối đa 12/từ; không tính ký tự xóa đi gõ lại | Chiêu hệ 20–40; thân pháp đặc biệt 15 | Tối đa 100 → 180 (K6) |
| Định Tâm (0–100) | Chớp +10, Hoàn hảo +6, Tốt hoặc Vừa +3, Ẩu 0; **+0,5/s** khi đang trong vùng trận | Tuyệt kỹ 100; góp hợp trận | Không giảm khi bị đánh |
| Thần thức (ngoài trận) | Theo cảnh giới: 60 → 160 | Mỗi đan 8–15, pháp bảo 30–60 | Tổng đồ mang ≤ Thần thức |

- **Ô liên tục (vô hệ) không tốn linh lực.** Codex §0 yêu cầu luôn có việc để gõ, nên linh lực không bao giờ được chặn việc gõ.
- **Kiểm nhịp (35 WPM, bot Chuẩn):** khoảng 0,33 từ/s × 5,5 ký tự ≈ 1,8 ký tự/s → +2,7 linh lực/s từ chữ, cộng 3/s tự hồi = 5,7/s. Một chiêu 30 linh lực có lại sau khoảng 5,3 s, khớp hồi chiêu 5–8 s ở Codex §12.3. Ở 25 WPM: khoảng 5,0/s. Ở 60 WPM: khoảng 7,4/s, nhưng bị hồi chiêu chặn. Chênh lệch nhỏ vì đã có phần tự hồi làm sàn.
- **Định Tâm:** bot Chuẩn có Tuyệt kỹ khoảng mỗi 50–60 s; bot 25 WPM khoảng mỗi 70 s nhờ phần +0,5/s.

### 4.3 Công thức sát thương (số thử, tính bằng số nguyên phần nghìn như `dragon-hold`)

```text
Đòn gõ:   D = P_chiêu × (Công/100) × M_q × M_hệ × (1 + Σbuff, trần +50 %) × M_dễ_tổn_thương
Đánh nền: D = P_nền × (Công/100) × M_hệ_vũ_khí × (1 − G_hd/(G_hd+100), trần 0,75)
Thú đánh ta: D = P_thú × g(K) × M_hệ_ngược × (1 − Thủ/(Thủ+100), trần 0,75) × (1 − Kháng hệ)
```

**M_q, kết quả một từ** (lấy từ `dragon-lane/00-canon.md` §4.2, đổi riêng dòng Chớp):

| Kết quả | Điều kiện | M_q |
|---|---|---|
| **Hội tâm** (Chớp) | Không lỗi và t ≤ 0,85 × t_kỳ_vọng **của chính người chơi** (từ `SkillProfile`) | **Bạo kích**: gốc 1,30, trần 1,80 |
| Hoàn hảo | Không lỗi | 1,10 |
| Tốt | 1 lỗi, từ ≥ 6 chữ | 1,00 |
| Vừa | 1 lỗi, từ ≤ 5 chữ | 0,90 |
| Ẩu | ≥ 2 lỗi | 0,60 |

- Boss có Kháng bạo k (0–40 %): Bạo kích hiệu dụng = 1 + (Bạo kích − 1) × (1 − k).
- **Kiểm kỳ vọng** (bot Chuẩn: khoảng 30 % Chớp, 45 % Hoàn hảo, 15 % Tốt hoặc Vừa, 10 % Ẩu): M_q trung bình ≈ 1,10 với Bạo kích 1,30, và ≈ 1,25 với Bạo kích 1,80. Đầu tư tối đa vào Bạo kích cho khoảng +14 %, không thành đáp án duy nhất.
- t_kỳ_vọng tính theo hồ sơ riêng, nên người 25 WPM và người 60 WPM có **cùng tỉ lệ Hội tâm** khi gõ đều tay. Đây là luật công bằng chính của mô hình.

**M_hệ:**

| Quan hệ | Hệ số |
|---|---|
| Hệ chiêu **khắc** hệ thú | ×1,30 |
| Không liên quan, hoặc vô hệ | ×1,00 |
| Hệ thú **khắc** hệ chiêu (bị khắc) | ×0,80 |
| Linh căn | Chiêu thuộc chủ hệ: +5/10/15/20/25 % theo phẩm 1–5. Phụ hệ: nửa mức đó |
| Kháng hệ của thú | −10 đến −30 %, cộng vào M_hệ |
| **Trần, sàn** | M_hệ × linh căn ≤ **1,60**; sau kháng ≥ **0,60**. Không có miễn nhiễm (Codex §16) |

- **Đòn gõ bỏ qua Giáp.** Giáp chỉ chặn đánh nền, pet, trận, đồng minh. Đây là luật D03 của Rồng Giữ Ải: giáp làm khó quân tự động, không làm khó tay gõ.
- Thú khắc hệ chính của người chơi thì đánh người đó ×1,20 (`M_hệ_ngược`). **Luật này mở sau MVP**, khi đã kiểm người chơi đọc được hệ.

### 4.4 Ngũ hành: khắc cho sát thương, sinh cho phản ứng

```text
Tương khắc (sát thương):  Kim → Mộc → Thổ → Thủy → Hỏa → Kim
Tương sinh (phản ứng):    Mộc → Hỏa → Thổ → Kim → Thủy → Mộc
Dị hệ (sau MVP):          Lôi thuộc Kim · Phong thuộc Mộc · Băng thuộc Thủy
```

Dị hệ dùng quan hệ khắc, sinh của hệ gốc, thêm một trạng thái riêng: Lôi nảy 2 mục tiêu, Phong đẩy và gom, Băng làm đóng băng thú đang Ướt. Gán Phong vào Mộc theo quẻ Tốn. Gán Lôi vào Kim để hai dị hệ không cùng dồn vào Mộc. Đây là **lựa chọn của dự án**, không phải cách hiểu duy nhất.

**Ấn của từng hệ** (mỗi chiêu hệ để lại 1 ấn trên thú trong 5 s):

| Hệ | Ấn | Tác dụng thử | Vai trong thủ ải |
|---|---|---|---|
| Kim | Phá giáp | Giáp ×0,5 trong 5 s | Giúp đánh nền, pet, đồng đội diệt thú giáp |
| Mộc | Triền | Chậm 30 % trong 3 s; thú nhỏ bị giam 1 s (giảm dần) | Giữ bầy ở xa trận |
| Thủy | Ướt | Chậm 15 %; mở phản ứng | Chuẩn bị cho đồng đội |
| Hỏa | Thiêu | Sát thương theo thời gian, tối đa 3 lớp | Dọn bầy |
| Thổ | Chấn | Khựng 0,5 s; đòn lên thanh thế của boss ×1,5 | Phá thế boss, chặn thú phá cổng |

**Phản ứng tương sinh:** thú đang mang ấn A trúng chiêu B, với A sinh B. Phản ứng tiêu ấn. Mỗi thú hồi phản ứng 3 s.

| Chuỗi | Tên tạm | Kết quả thử | Có trong MVP |
|---|---|---|---|
| Mộc → Hỏa | Liệu Nguyên | Thiêu lan sang tối đa 4 thú trong 2 m | Có |
| Thủy → Mộc | Dưỡng Mộc | Giam 1,5 s (giảm dần); hồi 2 % hộ trận | Có |
| Hỏa → Thổ | Tro Kết | Thú thường khựng 1 s, Giáp −30 % | Không |
| Thổ → Kim | Khai Phong | Đòn Kim ×1,4; Phá giáp kéo dài gấp đôi | Không |
| Kim → Thủy | Hàn Lưu | Thủy nảy sang 2 thú; người kích hồi 8 linh lực | Không |

Chia công: phản ứng ghi **50 % cho người đặt ấn, 50 % cho người kích**. Theo Codex §22.3, không thưởng cho đòn kết liễu cuối.

### 4.5 Trường phái = hình đòn × hệ

Codex §11 có 24 trường phái. QCBH có 6 loại vũ khí và 6 linh căn. Ta tách hai trục độc lập:

| Hình đòn | Mẫu vũ khí | Tác dụng | Hợp với |
|---|---|---|---|
| Đơn | Kiếm (phi kiếm) | Một mục tiêu, đi xa, xuyên giáp nhẹ | Tinh anh, thú bay |
| Xuyên | Thương, tên | Một đường thẳng | Hàng thú trên đường hẹp |
| Quạt | Đao, quyền | Hình nón gần | Bầy áp sát trận |
| Vùng | Phù, trận | Vòng tròn trên mặt đất, có trễ | Cụm đông, chỗ thắt cổ chai |
| Chuỗi | Chưởng, chỉ | Nảy 2–3 mục tiêu | Bầy rải rác |

- Một chiêu = 1 hình + 1 hệ (hoặc vô hệ) + số liệu. **5 × 6 = 30 tổ hợp** sinh từ dữ liệu. Chỉ làm tay các chiêu Tuyệt kỹ và trường phái đặc biệt.
- Nhân vật có **truyền thừa** (thiên về 1–2 hình) và **linh căn** (chủ/phụ hệ). Kiếm tu hệ Hỏa và Kiếm tu hệ Thủy là hai build khác nhau mà không cần thêm lớp.

### 4.6 Hệ của thú và điểm yếu (MVP có đủ 5 hệ dưới dạng thẻ)

| Hệ | Thú mẫu (tên tạm) | Hành vi | Bị khắc bởi | Điểm yếu cơ chế cùng hướng |
|---|---|---|---|---|
| Vô hệ | Lang bầy | Đông, nhanh, máu thấp | — | Hình Quạt hoặc Vùng |
| Kim | Thiết giáp trùng | Giáp G2 (55 %), chậm, cắn cổng | **Hỏa** | Đánh nền yếu; cần đòn gõ hoặc Phá giáp |
| Hỏa | Xích nha (bay) | Bắn cầu lửa vào hộ trận từ xa | **Thủy** | Hình Đơn hoặc Xuyên; Ướt làm rơi xuống |
| Thổ | Thạch quy | Khiên phía trước, không đẩy lùi được, phá cổng | **Mộc** | Triền giữ lại; đánh vòng sau |
| Thủy | Thủy hồ (sau MVP) | Lẩn, để vũng Ướt làm chậm phe ta | **Thổ** | Chấn lộ hình |
| Mộc | Đằng yêu (sau MVP) | Hồi máu đồng loại trong vùng rễ | **Kim** | Diệt nguồn hồi trước |

- **Điểm yếu cơ chế và điểm yếu hệ cùng chỉ một hướng.** Người chơi chỉ cần nhớ "thú này sợ hệ gì", không phải học hai bảng.
- Tinh anh có thêm **một** dòng kháng (ví dụ Kháng Hỏa 20 %), không được miễn nhiễm.
- **Boss "Ngũ Hành Luân Chuyển":** đổi hệ theo pha. Báo trước 3 s bằng màu vòng chân và biểu tượng. Mỗi pha có một cửa sổ cho hệ khắc nó, và một đường giải không cần hệ (Thổ phá thế, hoặc đơn giản là né).
- Máu thử ở K1 (solo): thú nhỏ 45, vừa 160, giáp 350, tinh anh 700, boss 4.500. Đội: máu × (1 + 0,8 × (n − 1)), với n là số chỗ kể cả bot, chốt lúc vào trận (Codex §15).
- Kiểm nhanh: ô liên tục P = 50 hạ thú nhỏ bằng 1 từ không Ẩu. Chiêu hệ P = 110 khắc thú vừa: 110 × 1,1 × 1,3 ≈ 157, cộng đánh nền là đủ. Boss 4.500 với khoảng 31 sát thương/s (gõ + nền) mất khoảng 2,4 phút.

### 4.7 Trần chỉ số (gán số cho Codex §21)

| Hệ | Trần thử |
|---|---|
| Giảm sát thương (Thủ + buff + đan) | ≤ 75 %, theo công thức G/(G+100) |
| Giảm hồi chiêu | ≤ 30 % (Codex) |
| Bạo kích | 1,30 → 1,80 |
| Hệ số hệ (khắc × linh căn × đồ) | ≤ 1,60; sau kháng ≥ 0,60 |
| Kháng hệ của người chơi | ≤ 40 % mỗi hệ |
| Buff sát thương (mọi nguồn) | ≤ +50 %; cùng ID lấy mạnh nhất |
| Thân pháp | ≤ +40 % gốc (gốc 4,0 m/s) |
| Hút sinh lực | ≤ 5 % sát thương đòn gõ; quota 30 HP/s cho cả chủ và pet |
| Linh lực từ chữ | ≤ 12 mỗi từ |
| Khống chế cứng trên cùng thú | Lần 2 ×0,6, lần 3 ×0,3, sau đó miễn 4 s (luật Rồng Giữ Ải) |

- Tăng theo cảnh giới: Công, Sinh lực, Thủ tăng theo g(K) = 1,12^K (K0–K6 → ×1,00 đến ×1,97). Thú trong ải cảnh giới K cũng nhân g(K). Theo Codex §21.1, cảnh giới không nâng mức thuộc từ.
- Mệnh cách (tương đương NTCM của QCBH, tên và nội dung phải của ta): chọn 3 lúc tạo nhân vật. **Mỗi mệnh cách có cái giá** và đi qua cùng bucket, cùng trần ở trên. Không có mệnh cách cộng tỉ lệ Hội tâm.

### 4.8 Hệ tạo quyết định trong một trận thú triều

1. **Trước trận (Thám báo):** bảng đợt hiện hệ chiếm đa số của từng đợt và của boss. Người chơi chọn 4–6 ô chiêu từ công pháp đã học, 1 pháp bảo (có thể khác hệ), đan kháng hệ. Tổng đồ mang ≤ Thần thức.
2. **Giữa đợt (nghỉ 15 s):** đổi 1 ô miễn phí. Đội đổi **hệ hộ trận** (mục 5) theo đợt sắp tới.
3. **Trong đợt:** viền ô khắc sáng theo mục tiêu mềm hoặc theo mối nguy gần nhất. Quyết định là gõ từ của ô khắc lên thú nguy hiểm, hay gõ ô liên tục để giữ linh lực, hay đặt ấn cho đồng đội kích phản ứng.
4. **Boss:** đổi hệ theo pha. Có thể giữ chiêu khắc chờ pha phù hợp, hoặc dùng Thổ phá thế bất kể hệ.
5. **Giới hạn quá tải:** mỗi đợt **tối đa 2 hệ chủ đạo**. Mỗi thú hiện **một** biểu tượng hệ. Không ghi chữ về hệ trên thẻ từ.

### 4.9 Mô hình dữ liệu (TypeScript, bản nháp)

```ts
type Element = "kim" | "moc" | "thuy" | "hoa" | "tho";
type Variant = "loi" | "phong" | "bang";               // sau MVP; parent: kim, moc, thuy
type Shape = "single" | "pierce" | "cone" | "area" | "chain";
type WordResult = "crit" | "perfect" | "good" | "fair" | "sloppy";

interface CultivatorStats {                              // số thô; nhân g(K) khi vào ải
  hpMax: number; lingMax: number; lingRegen: number;   // 600 · 100 · 3/s ở K0
  atk: number; def: number; move: number;              // 100 · 20 · 4.0
  critMulPm: number;                                   // 1300..1800 (permille)
  cdrPm: number;                                       // ≤ 300
  root: { main: Element; sub?: Element; grade: 1|2|3|4|5 };
  elemResPm: Partial<Record<Element, number>>;         // ≤ 400 mỗi hệ
  senseCap: number;                                    // Thần thức, ngoài trận
  insight: number;                                     // Ngộ tính, chỉ dùng cho tu luyện
}
interface SkillDef {
  id: string; shape: Shape; element: Element | "none"; variant?: Variant;
  power: number; lingCost: number; cdMs: number; seal?: Element;  // ấn để lại
  slotKind: "continuous" | "skill" | "guard" | "ultimate" | "movement";
}
interface BeastDef {
  id: string; element: Element | "none"; armorTier: 0|1|2|3;      // G 0/43/122/300
  elemResPm?: Partial<Record<Element, number>>;                   // ≤ 300
  critResistPm?: number; tenacityPm: number; hp: number; tags: string[];
}
const ELEMENT_RULES = { counterPm: 1300, counteredPm: 800, capPm: 1600, floorPm: 600,
  rootBonusPm: [50, 100, 150, 200, 250], subRootFactor: 0.5, sealMs: 5000, reactionIcdMs: 3000 };
```

- Mọi phép tính dùng số nguyên phần nghìn, RNG theo seed. Như vậy replay, bot và đội online (Durable Object làm trọng tài) cho cùng kết quả. Không có chí mạng ngẫu nhiên nên không cần đồng bộ xúc xắc giữa các máy.

### 4.10 MVP và sau MVP

| MVP | Sau MVP |
|---|---|
| 3 thanh HUD, trang chỉ số 6 + 5 | Mệnh cách đầy đủ, đồ có dòng phụ |
| 5 hệ là thẻ của thú; thú Vô hệ, Kim, Hỏa, Thổ | Thú Thủy, Mộc; boss đổi hệ 3 pha |
| Người chơi dùng 3 hệ: Thủy, Mộc, Hỏa; chủ hệ + phụ hệ (phụ hệ mở ở K2) | Kim, Thổ cho người chơi; 3 dị hệ |
| Khắc ×1,30 / ×0,80; linh căn phẩm 1–3 | Phẩm 4–5; thú khắc người ×1,20 |
| 2 phản ứng: Liệu Nguyên, Dưỡng Mộc | 3 phản ứng còn lại |
| Hội tâm = Chớp; Bạo kích 1,30–1,50 | Bạo kích tới 1,80; Kháng bạo của boss |
| 3 hình đòn: Đơn, Quạt, Vùng | Xuyên, Chuỗi |
| Giáp G0–G2 | G3, Xuyên giáp trên đồ |

Thứ tự dạy: ải 1–2 chỉ có vô hệ. Ải 3 dạy khắc (thú Kim + chiêu Hỏa, viền ô sáng). Ải 5 thêm hệ thứ hai. Ải 8 dạy phản ứng. Mỗi lần **một** luật mới, giống nhịp "mỗi 5 ải một món" của Rồng Giữ Ải.

## 5. Solo và đội

| | Solo (1 người, có thể có bot) | Đội 2–3 người (+ bot bù) | Mở rộng 5 hoặc 7 người |
|---|---|---|---|
| Phủ hệ | Chủ + phụ + 1 pháp bảo = 3 hệ | Mỗi người 2 hệ; đội phủ 4–5 hệ | Trận Ngũ Hành: mỗi chỗ 1 hệ |
| Chuỗi sinh | Chủ sinh phụ (ví dụ Mộc → Hỏa) được tính là chuỗi 2 | Thủy → Mộc → Hỏa giữa 3 người = Tam Tài đủ chuỗi | Ngũ Hành đủ vòng sinh |
| Hộ trận | Hệ của hộ trận = chủ hệ của người chơi | Đội chọn hệ hộ trận giữa đợt (người giữ nhãn chọn, hoặc bỏ phiếu) | Nhãn theo vai (Codex §14.3) |

**Luật công bằng:**

1. **Thưởng "Sinh trận"** khi các chỗ tạo chuỗi sinh: +8 % sát thương chiêu và +10 % hồi linh lực. Trị số **giống nhau cho chuỗi 2 và chuỗi 3**, nằm trong bucket buff có trần. Đội đông không nhân thưởng (Codex §23.1).
2. **Ngân sách hệ của ải solo:** mỗi đợt có tối đa **1 hệ chủ đạo** mà bộ 3 hệ của người chơi không khắc được. Ải đội được trộn nhiều hơn.
3. **Không có nội dung phổ thông bắt buộc phải có một hệ.** Thiếu hệ khắc chỉ đưa hệ số về ×1,00, vì luôn có ô vô hệ và đường Thổ phá thế.
4. **Bot bù chỗ** chọn chủ hệ còn thiếu để nối chuỗi sinh. Người chơi đổi được trước trận. Bot dùng `HumanTypist`; bot không tạo mastery tiếng Anh (Codex §15).
5. **Hội tâm tính theo nhịp riêng**, nên người gõ chậm trong đội không bị người gõ nhanh át về tỉ lệ chí mạng. Người nhanh vẫn gõ được nhiều từ hơn; đóng góp đo theo việc hữu ích (Codex §22.3).
6. **Áp cảnh khi đi đội:** chỉ số của người cao cảnh giới được kẹp về tối đa K_ải + 1. Người mới vẫn có vai trò thật, người cũ vẫn mạnh hơn một chút.
7. **Phản ứng chia công 50/50.** Ấn hết hạn hoặc phản ứng trùng không tính là đóng góp.
8. **Bảng xếp hạng** tách solo, đội có bot, đội người, và tách preset, kênh nhập (Codex §22.2).

## 6. Gắn với học tiếng Anh

- **Từ trên ô chiêu luôn lấy từ bài học.** Hệ là thuộc tính của **chiêu**, không phải của **từ** (Codex §1.4). Không dùng "fire", "water" làm lệnh cố định.
- **Không để ô khắc nhận từ dài hơn.** Từ chia cho các ô theo dải độ dài của preset, độc lập với hệ (Codex §22.1). Nếu không, người chơi phải chọn giữa "đúng hệ" và "từ dễ", và việc học bị phạt.
- **Hội tâm là phần thưởng học:** gõ đúng hết, đều tay theo nhịp của chính mình. Thông điệp cuối ải: "28 % từ Hội tâm, thường mất ở chữ đầu".
- **Voice và Hybrid:** đi cùng giao dịch chiêu. Hội tâm cho Voice dùng **hồ sơ riêng**: nhận đúng ngay lần đầu, độ tin cao, trong t_kỳ_vọng của kênh Voice. Mục tiêu là cùng tỉ lệ Hội tâm khoảng 30 % ở bot tham chiếu của mỗi kênh. Voice không được thêm sát thương chỉ vì nói từ ngắn nhanh hơn (Codex §1.4).
- **Lộ từ vựng nhẹ:** tooltip và sách hệ ghi tên tiếng Anh: Metal, Wood, Water, Fire, Earth; Lightning, Wind, Ice. Màn kết ải có thể thêm 1 thẻ "từ của hệ" làm từ ôn **tùy chọn**. Không chèn vào trận.
- **Tránh quá tải:** thông tin hệ chỉ là **biểu tượng + màu** (đọc bằng mắt ngoại vi), không thêm chữ. Mỗi đợt tối đa 2 hệ. Luật hệ mở dần (mục 4.10). Khung học (nghĩa, IPA) không bao giờ bị viền hệ hay VFX phản ứng đè lên (luật chung trong `SPLIT_PLAN.md` §1.1).
- **Nhận diện hệ đặt hình trước màu:** Kim hình mũi kiếm, Mộc hình lá, Thủy hình giọt, Hỏa hình ngọn lửa, Thổ hình khối vuông. Màu Hỏa và Kim dễ trùng với màu nghĩa chung (đỏ nguy hiểm, vàng kim tiền), và còn phải tính người mù màu.

## 7. Tái sử dụng và chi phí

| Hạng mục | Dùng lại | Mới | Chi phí |
|---|---|---|---|
| Giảm theo Giáp/Thủ, trần 75 % | `games/dragon-hold/src/sim/combat.ts` (`reductionPm`, luồng `WordStrike`) | Thêm M_hệ, linh căn | S |
| Kết quả từ (Chớp…Ẩu), không chí mạng ngẫu nhiên | `docs/games/dragon-lane/00-canon.md` §4.2, D03 | Đổi Chớp → nhân Bạo kích | S |
| Trạng thái, giảm dần khống chế, dễ tổn thương, kiên định | `games/dragon-hold/src/sim/status.ts`; `03-our-side-shop-traps-support.md` §2.1–2.3 | 5 ấn hệ | S–M |
| Thẻ hệ, phản ứng | `games/dragon-hold/src/content/types.ts` (`Element`), `03-…` §2.4 (4 phản ứng) | Đổi bộ 7 nguyên tố sang ngũ hành + dị hệ; 5 phản ứng sinh | M |
| t_kỳ_vọng riêng, bot giống người, điều nhịp, cổng | `shared/game-kit/balance/` (`profile.ts`, `typist.ts`, `director.ts`, `gates.ts`); `docs/games/BALANCE.md` §2, §6, §7 | Cổng hệ (mục 8) | S |
| RNG theo seed, số sát thương, bậc phản hồi | `shared/game-kit/platform/rng.ts`, `shared/game-kit/feedback/numbers.ts`, `tiers.ts` | Kiểu số "Hội tâm", "Khắc" | S |
| Ngân sách chữ theo độ dài | `shared/game-kit/typing/` (`budget.ts`) | Luật ô khắc không nhận từ dài hơn | S |
| Trang nhân vật 6 + 5, HUD 3 thanh, viền hệ | Vỏ UI chung `shared/game-kit/ui` | Bố cục, icon 5 hệ + 3 dị hệ | M |
| VFX, SFX theo hệ (MVP 3 hệ × 2 chiêu + 2 phản ứng) | Ngữ pháp VFX Codex §26.5; quy trình âm `docs/games/AUDIO_PIPELINE.md` | Âm thu thật CC0, đúng hình và cỡ đòn (Q6) | **L** (MVP 3 hệ là M) |
| Thú theo hệ | Sprite 2D đổ màu + vòng hệ dưới chân | 3–5 bộ sprite + vòng | M |
| Mô phỏng cân bằng có hệ | Khung bot của `dragon-hold` (`dh:balance`) | Ma trận hệ × bot × seed | M |

**Tổng cho mảng này:** MVP khoảng **M** (logic S–M vì dùng lại nhiều; phần lớn chi phí là hình và âm). Đầy đủ 5 hệ + dị hệ: **L**.

## 8. Rủi ro và câu hỏi cho chủ dự án

**Rủi ro chính:**

| Rủi ro | Mức | Cách giảm |
|---|---|---|
| Hệ thành "đáp án bắt buộc": thiếu hệ là thua | Cao | Sàn 0,60; ngân sách hệ solo; luôn có ô vô hệ + đường Thổ phá thế; cổng E1 |
| Người chơi nhìn viền hệ mà quên đọc nghĩa từ | Cao | Hệ chỉ là biểu tượng ngoại vi; không đặt hệ lên thẻ từ; đo thời gian nhìn khung học |
| Phản ứng + ấn + khắc quá nhiều khi đông thú | Cao | Tối đa 2 hệ mỗi đợt; MVP chỉ 2 phản ứng; 1 biểu tượng mỗi thú |
| Bạo kích + khắc + buff nhân chéo | Vừa | Trần 1,60 cho hệ, +50 % cho buff; kiểm tương tác (Codex §21) |
| Màu hệ trùng màu nghĩa chung | Vừa | Hình trước màu; kiểm chế độ mù màu |
| Người gõ nhanh át đội | Vừa | Hội tâm theo nhịp riêng; chia công phản ứng; áp cảnh |

**Cổng bot đề xuất** (thêm vào `BALANCE.md` §7 khi làm game):

- **E1:** bot dùng loadout hệ ngẫu nhiên vẫn đạt B3 (bot Mới thắng ≥ 70 % ở Cân bằng).
- **E2:** bot chọn hệ Tốt hơn bot chọn hệ Kém ≥ 8 điểm % thắng ở Thử thách. Hệ phải có ý nghĩa.
- **E3:** tỉ lệ Hội tâm của các bot 25 / 35 / 60 WPM lệch nhau ≤ 5 điểm %.
- **E4:** phần sát thương từ phản ứng ≤ 20 % tổng sát thương đội.

**Câu hỏi cho chủ dự án (mỗi câu kèm phương án đề xuất):**

| # | Câu hỏi | Đề xuất |
|---|---|---|
| Q1 | Dùng ngũ hành 5 hệ hay 6 linh căn kiểu QCBH (có Lôi, Phong, không Kim)? | **Ngũ hành 5 hệ**, Lôi/Phong/Băng làm dị hệ sau MVP. Có vòng khắc sinh rõ, khác QCBH |
| Q2 | Có chí mạng ngẫu nhiên không? | **Không.** Hội tâm = từ Chớp, Bạo kích là chỉ số. Giống D03 của Rồng Giữ Ải, công bằng và dễ đồng bộ online |
| Q3 | Đòn gõ có bị Giáp chặn không? | **Không.** Chỉ hệ ảnh hưởng đòn gõ; Giáp làm khó đánh nền, pet, trận |
| Q4 | Có giữ thanh Niệm lực thứ ba trong trận? | **Không.** Thần thức là sức chứa hành trang; Định Tâm nạp bằng chất lượng từ |
| Q5 | Chủ hệ chọn một lần hay đổi được? | **Chọn khi tạo nhân vật, đổi ở điểm nghỉ với giá thấp** (một viên đan tẩy linh căn), để người học thử nhiều hệ |
| Q6 | Ba hệ người chơi cho MVP? | **Thủy, Mộc, Hỏa:** đủ chuỗi sinh cho Tam Tài 3 người; VFX nước, lá, lửa dễ đọc |
| Q7 | Thú khắc hệ người chơi có đánh mạnh hơn (×1,20)? | **Có, nhưng mở sau MVP**, khi đã kiểm người chơi đọc được hệ |
| Q8 | Có giữ Thọ mệnh, Tâm tình, May mắn? | **Bỏ.** Không giới hạn thời gian của người học; May mắn là RNG khó công bằng |
| Q9 | Đội lệch cảnh giới xử lý thế nào? | **Áp cảnh:** kẹp về K_ải + 1 |
| Q10 | Tên hệ hiện tiếng Anh ở đâu? | **Tooltip, sách hệ và thẻ ôn cuối ải**; UI chính dùng tiếng Việt; không chèn vào trận |

## Nguồn

- Video QCBH chủ dự án quay: khung `t000`, `t004` (trang nhân vật, ghi chú hạn mức Niệm lực), `t136` (HUD trận, "Bạo Kích −82"), `dense/boss_06` (boss, Niệm lực 172/242), `dense/med_08` (tu luyện, Ngộ tính 101).
- [web: https://gamepretty.com/tale-of-immortal-how-to-create-a-good-starting-character-鬼谷八荒/] — Luck, Perception, Agility, Travel Speed, Mood, Lifespan, Destinies.
- [web: https://en.wikipedia.org/wiki/Tale_of_Immortal] — combat từ trên xuống kiểu bullet hell, chọn tối đa 3 mệnh cách, manual và mind skill.
- [web: https://earlyguides.com/tale-of-immortal/builds] (qua kết quả tìm kiếm) — 6 linh căn quyết định linh kỹ nào mạnh lên.
- [web: https://kosgames.com/tale-of-immortal-techniques-guide-5889/] — có dòng affix Martial RES, Spiritual RES, Crit; không có công thức.
- Dự án: `TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md` §1.4, §9–§12, §14–§17, §21–§23, §26.5; `docs/games/dragon-lane/00-canon.md` §3 D03, §4.2; `docs/games/dragon-lane/03-our-side-shop-traps-support.md` §2; `docs/games/BALANCE.md`; `docs/games/SPLIT_PLAN.md` §1.1.
