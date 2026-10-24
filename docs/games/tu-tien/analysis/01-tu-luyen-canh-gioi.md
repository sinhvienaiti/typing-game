# Tu Tiên Thủ Ải: 01. Tu luyện, cảnh giới và tiến trình (phân tích, 24/10/2026)

> **Phạm vi:** cảnh giới và đột phá, mini-game tĩnh tọa (cầu ngộ/cầu ma trong video), ngộ tính, học và luyện công pháp, tâm ma, thọ mệnh, khí vận (kiểu NTCM) làm bổ trợ cho từng lượt, tiến trình lâu dài (meta) so với tiến trình trong lượt (run), chỗ của tu luyện **giữa các trận thú triều**.
> **Đã đọc:** Codex V2.2 §0–§1, §10, §14–§19, §21–§24, §27, §29; khung hình video (`crop/t*.jpg`, `dense/med_01..30`); `docs/games/dragon-lane/04-stages-maps-progression.md` (§8–§10), `01-core-combat-learning.md` §6.5–6.7; `docs/games/BALANCE.md`; `games/space-typing/docs/survival/SURVIVAL_MODE_PLAN.md` §4.0; `shared/learning/README.md`; đầu tệp `shared/game-kit/typing/*`, `balance/gates.ts`.
> **Ký hiệu nguồn:** [video] là bản ghi của chủ dự án · [Codex doc] là tệp V2.2 · [web: url] · [trí nhớ] là chưa xác minh. **Mọi con số trong mục 4 là số thử**, chỉnh sau khi chạy bot và cho người chơi thật thử.
> **Tệp liên quan (các phân tích khác viết song song):** combat, kỹ năng, shop, pet và đội nằm ở các tệp khác trong `analysis/`. Chỗ nào chạm sang mảng của họ, tài liệu này chỉ nêu giao diện và đánh dấu "phối hợp".

## 1. Tóm tắt

1. **Tách hai tầng tiến trình.** Cảnh giới, công pháp và Đạo Ấn **giữ mãi** (meta). Khí Vận và Cơ Duyên **chỉ sống trong một Thú Triều** (run). Đây là điểm hay nhất của QCBH: tiến trình dài và chậm, nhưng mỗi lượt vẫn có lựa chọn build mới. Ta giữ nguyên tắc này và gói nó vào vòng thủ ải.
2. **Không có thế giới mở.** Tu luyện diễn ra ở **Sơn Môn**, một màn hub duy nhất có 4–7 điểm bấm được. Giữa hai trận trong cùng một Thú Triều có **Doanh Trại**, một màn nghỉ dài 60–90 giây. Không bản đồ du hành, không NPC, không thời gian thế giới.
3. **Tu vi đến từ trận thủ ải.** Hạ thú cho Thú Hạch, Thú Hạch tự luyện hóa thành tu vi khi kết trận. Mini-game **không bắt buộc** để lên tu vi. Mini-game chỉ dùng để **lĩnh ngộ công pháp**, tức là học từ mới của công pháp đó.
4. **7 cảnh giới × 3 kỳ** khớp với 7 mốc K0–K6 của Codex §10.2. Đột phá đại cảnh giới là **Độ Kiếp**: một trận thủ nhỏ 2–3 phút. Không tung xác suất thất bại, thua thì đánh lại và không mất vật liệu. Khi qua, người chơi chọn 1 trong 3 **Đạo Ấn** vĩnh viễn.
5. **Đổi vai của chữ trong tĩnh tọa.** Minh là từ mới của khẩu quyết công pháp. Chữ Thường là từ đến hạn ôn. Loại chữ phải tránh đổi tên thành **Tạp Niệm** và chỉ lấy từ đã thuộc. **Tâm Ma** trở thành một thanh đo, cộng với kẻ địch trong Độ Kiếp mang **chính những từ người học còn yếu**: đối mặt tâm ma cũng là ôn bài.
6. **Bỏ thọ mệnh.** Thọ mệnh chỉ có nghĩa khi có thời gian thế giới và luân hồi. Với game học, nó tạo áp lực "hết giờ" mà không đổi lại gì. Ngộ tính được giữ, nhưng **tính từ bằng chứng học thật** (số từ đã thuộc) và có trần.
7. **MVP:** 2 cảnh giới, Độ Kiếp solo, tĩnh tọa tầng 1, 6 công pháp, 12 Khí Vận, 18 Cơ Duyên, thanh Tâm Ma cùng Ôn Tâm, Sơn Môn 4 điểm. Hộ pháp đột phá theo đội, tĩnh tọa chọn theo nghĩa và cảnh giới 3–7 để sau MVP.

## 2. QCBH làm thế nào (chỉ phần đáng học)

| Hệ | QCBH làm gì | Nguồn | Điều ta học |
|---|---|---|---|
| Cảnh giới | 10 cảnh giới 练气 → 登仙, mỗi cảnh chia sơ/trung/hậu kỳ (30 bậc) | [web: https://www.18183.com/ggbh/202103/3322171.html] | Thang dài, chia nhỏ để luôn thấy thanh tiến độ |
| Đột phá Trúc Cơ | Ba đường: Thiên đạo (6 loại linh khí + đan tăng tỷ lệ, qua thì có 6 lựa chọn thuộc tính), Địa đạo (1 loại, 3 lựa chọn), Nhân đạo (không vật liệu, 1 lựa chọn). Người chơi chọn 1 | [web: 18183 như trên] | Đột phá là **sự kiện có chuẩn bị** và **thưởng bằng lựa chọn**. Chuẩn bị kỹ thì có nhiều lựa chọn hơn |
| Tỷ lệ thất bại, lưu rồi tải lại | Đột phá có thể hỏng. Người chơi lưu trước, tải lại để đổi dòng thưởng | [web: https://www.toutiao.com/zixun/7509290130461673472/, trích đoạn tìm kiếm] | **Không học.** Tung số rồi lưu/tải là trải nghiệm xấu, nhất là với trẻ em |
| Khí vận | 先天气运 chọn lúc tạo nhân vật. 逆天改命 (NTCM) chọn khi đột phá đại cảnh giới | [web: toutiao như trên]; lớp phủ của stream ghi kế hoạch NTCM "3 Huyết linh, 1 huyết ma, chấn thiên, hổ phách, thất tinh kiếm bộc…" [video 0:00–4:16] | Người chơi **lên kế hoạch build** quanh dòng khí vận. Đây là động lực chơi lại |
| Học công pháp | Một phiên ngắn: người tu sĩ ngồi thiền, cầu xanh/trắng mang chữ 悟 trôi quanh thân, cầu đỏ mang chữ 魔 xuất hiện về cuối phiên. Giữa thân có bộ đếm 悟 (ví dụ "35") và dấu 魔 | [video, med_04→med_21] | Mini-game ngắn, đọc được ngay, có vật tốt và vật xấu |
| HUD tĩnh tọa | "Ngộ tính hiện tại 101 · Tỷ lệ sinh ra ngộ cầu 90% · Tốc độ di chuyển của cầu: Cực chậm · Tiến độ tu luyện" | [video, med_08/med_15] | **Ngộ tính đổi luật mini-game** (tỷ lệ cầu, tốc độ cầu). Chỉ số có cảm giác vì người chơi thấy nó tác động |
| Thời lượng và chi phí | Phiên dài khoảng 15–20 giây. Kết phiên hiện "Linh Thạch −400 · Tâm tình −6 · Diệu Bản Huyền −1" | [video, med_04→med_22] | Học là một khoản **đầu tư** (tiền, sách, tâm trạng). Phiên phải ngắn |
| Luật cầu | Thu cầu ngộ, phá cầu ma. Luyện mở dòng, tham ngộ điều chỉnh dòng | [Codex doc §17, R11–R12] | Chỉ từ khung hình thì không xác nhận được cách bấm; quan sát được con trỏ di chuyển giữa các cầu [video] |
| Chỉ số nhân vật | Thọ mệnh 19/120, Tâm tình, Thể chất, Tinh lực, Sinh/Linh/Niệm lực, May mắn, Ngộ tính 101; 6 hệ công pháp, 6 linh căn, 6 kỹ nghệ; 5 ô đạo cụ có trần theo Niệm lực | [video 0:00–0:12, med_28] | **Quá nhiều chỉ số** cho game gõ chữ. Chỉ giữ thứ người chơi quyết định được giữa hai trận |
| Thọ mệnh, luân hồi | Tuổi tăng theo thời gian thế giới. Đột phá kéo dài thọ. Hết thọ thì chết và sang đời sau | [trí nhớ]; review nói người chơi viết truyện "life by life" [web: https://gamegeeker.com/games/tale-of-immortal-1468810/review?market=US] | Phụ thuộc thế giới mở và thời gian trôi. Không hợp với ta |
| Thú triều | Có cảnh chiến đấu "兽潮" riêng (mod đặt nhạc nền riêng cho nó) | [web: trích đoạn tìm kiếm từ changelog mod trên Steam Workshop, chưa mở trang gốc] | Luật chi tiết (giữ cổng thành theo chu kỳ) là [trí nhớ], chưa xác minh. Ta **lấy thú triều làm trục chính**, còn QCBH chỉ coi nó là một sự kiện |
| Kết trận | Cuộn giấy "Chiến đấu kết thúc · Thu hoạch được đạo cụ" | [video t256] | Màn kết gọn, phần thưởng đọc được ngay |

**Rút ra cho ta.** (a) Có hai nhịp: cảnh giới chậm, build nhanh. (b) Đột phá là cột mốc có nghi thức. (c) Học kỹ năng là một mini-game ngắn có giá. (d) Chỉ số phải đổi được luật chơi mà người chơi nhìn thấy. Không lấy: tung số thất bại, lưu/tải để đổi kết quả, thọ mệnh, tâm tình, cước lực, kỹ nghệ chơi tay, quan hệ NPC, bản đồ du hành.

## 3. Codex V2.2 nói gì về mảng này: giữ, sửa, bỏ

| § | Codex đề xuất | Quyết định | Lý do |
|---|---|---|---|
| §10.1–10.2 | Hồ sơ F/S/R/H, mốc K0–K6, "không bắt buộc 7 cảnh giới" | **Giữ, sửa nhẹ:** K0–K6 = 7 cảnh giới (mục 4.2). Hồ sơ F/S/R/H là của **trường phái**, không phải của cảnh giới | Mỗi mốc có tên và nghi thức đột phá thì thang tiến trình dễ hiểu hơn |
| §10.3–10.4 | Bảo vệ đầu game; lớp sớm vẫn còn giá trị cuối game | **Giữ** | Đúng với game học: không ai phải "chịu yếu" mấy giờ đầu |
| §17.1 | Năm tiến trình tách nhau: tu vi, tư chất, ngộ tính, thành thạo, mức thuộc tiếng Anh | **Giữ nguyên tắc tách, gộp còn 4:** bỏ "tư chất", nhập vào **tầng công pháp** (4.4) | Game thủ ải không cần hai trục cùng đo "giỏi một hướng công pháp" |
| §18.1 | Ba loại chữ Minh / Thường / Tâm ma (gõ Tâm ma thì bị phạt) | **Sửa:** Minh = từ mới của khẩu quyết; Thường = từ đến hạn ôn; loại phải tránh đổi tên **Tạp Niệm**, chỉ lấy từ người học đã thuộc (độ thuộc ≥ 70) | Phạt việc gõ một **từ mới** tiếng Anh là thông điệp sai. Tạp Niệm là từ đã thuộc nên tránh nó chỉ là kỹ năng tập trung. "Tâm ma" để dành cho hệ ở 4.7 |
| §18.3–18.6 | 3–4 điểm đọc, vòng đời 3 pha, bảng ngân sách theo preset, lệch lịch xuất hiện | **Giữ** | Đã cân nhắc kỹ khả năng đọc và tính khả thi (§23.3) |
| §18.7 | Chọn bằng từ, tránh tiền tố trùng | **Giữ, cài bằng kit:** dùng `letters.ts` bậc 1 (chữ đầu duy nhất) **giữa các loại**; bậc 2 (chung chữ đầu, khác chữ thứ hai) chỉ cho phép trong cùng một loại | Kit đã có sẵn và đã được kiểm |
| §18.8 | Minh hết hạn khi đang gõ: giữ phần đã nhập ở dạng "quá hạn" đến khi người chơi xong hoặc hủy | **Sửa:** dùng **ân hạn khóa** của kit (`session.ts`, `protectS` 1,2 s). Hết ân hạn thì bỏ từ, ghi "lost", và **tha** phím lạc kế tiếp | Đơn giản hơn, đã có code, vẫn chặn được ký tự rơi sang Tạp Niệm (RV17) |
| §18.9–18.10 | Chấm riêng gõ / chọn lọc / đúng hạn; tiến độ chắc chắn, không tung số | **Giữ, thêm sàn:** hoàn thành phiên luôn cho ≥ 40 % tiến độ lĩnh ngộ | Không bao giờ ra về tay trắng |
| §18.11 | Phiên 60–90 giây, chỉ dùng cho học công pháp và mốc tham ngộ | **Giữ**, thêm **thẻ Khẩu Quyết** 20–40 giây trước phiên (không tính giờ) | Từ mới phải được giới thiệu trước khi bị đặt hạn giờ (như Học Trước của Rồng, 01 §6.5) |
| §18.12 | Tạm dừng che vùng chữ | **Giữ** | Không có gì để sửa |
| §19 | Sáu hoạt động tu luyện khác | **Bỏ ở MVP:** Dẫn khí nhập mạch, Thiên thư tái cấu, Linh thú đồng tâm. **Giữ:** Đột phá (thành Độ Kiếp, 4.3), Tham ngộ biến chiêu (thành một màn chọn, không phải mini-game), Phòng luyện | Mỗi mini-game thêm vào là thêm chi phí và thêm "việc nhà" (§19.2 của Codex cũng cảnh báo điều này) |
| §19.2 | Không biến tu luyện thành danh sách việc phải làm; không thêm sáu loại tiền | **Giữ, làm luật cứng:** tối đa 3 loại tiền cho mảng này (4.10) | |
| §0.2 ý 7 | Không bắt gõ Tâm ma để thanh lọc trong mini-game | **Giữ trong tĩnh tọa.** Thêm Tâm Ma ở **Độ Kiếp** dưới dạng kẻ địch mang từ yếu | Khác bối cảnh: tĩnh tọa luyện tập trung, còn Độ Kiếp là lúc đối mặt điểm yếu |
| §21 | Trần chỉ số theo nhóm | **Giữ**, áp thêm cho Khí Vận × Đạo Ấn × tầng công pháp (4.9) | Ba nguồn bổ trợ dễ nhân chéo nhau |
| §22.2 | Preset tách độ khó ngôn ngữ và RPG; Voice có hồ sơ thời hạn riêng | **Giữ** | |
| §27 P5 | Tu luyện để ở bước 5 | **Sửa:** làm **bản thử tĩnh tọa song song với P1** (mức S–M, độc lập combat). Cảnh giới và Độ Kiếp vẫn chờ combat P3 | Kiểm sớm khả năng đọc chữ và lịch Minh bằng bot gõ |
| (thiếu) | Codex chưa nói tu vi đến từ đâu, hub ra sao, phần nào giữ mãi, phần nào theo lượt, thọ mệnh, khí vận | **Bổ sung** ở mục 4 | |

## 4. Đề xuất cho game chống ải thú triều

### 4.1 Khung: Sơn Môn và Thú Triều

```text
SƠN MÔN (hub, 1 màn) ──chọn Thú Triều──▶ THÚ TRIỀU = lượt chơi (run): Trận 1 … Trận 6 → Thú Vương
  ▲  Tĩnh Thất, Độ Kiếp Đài,               │ giữa hai trận: DOANH TRẠI (60–90 s): hồi phục, Cơ Duyên,
  │  Đan Các, Trận Đài…                     │ mua nhanh, 1 Thẻ Ôn, xem trận kế
  └── mang về: tu vi, Thú Hạch, Linh Thạch, bí kíp, thuần thục công pháp ◀──┘ (Khí Vận, Cơ Duyên mất)
```

- Một **Thú Triều** gồm 6 trận và 1 trận Thú Vương (số thử; MVP dùng 4 + 1). Mỗi trận 4–6 phút. Cả lượt khoảng 35–45 phút. **Mốc lưu** đặt ở trận 4 (giống Mốc ải 5 của Tuyến Cuối).
- Thua giữa lượt: về Sơn Môn, **giữ toàn bộ tu vi đã nhận**, giữ 50 % Thú Hạch và Linh Thạch của lượt, mất Khí Vận và Cơ Duyên. Có thể đánh lại từ Mốc.
- Đường chính: 21 Thú Triều, mỗi Thú Triều ứng với một kỳ cảnh giới (4.2). Mùa sau thêm cảnh giới hoặc thêm "Triều Luân Hồi" (chơi lại có luật khó) bằng dữ liệu.

### 4.2 Cảnh giới

Tên dùng hệ cảnh giới phổ biến của tiểu thuyết tu tiên, **tránh chuỗi đặc trưng của QCBH** (Kết Tinh, Cụ Linh, Ngộ Đạo, Vũ Hóa, Đăng Tiên).

| Mốc | Cảnh giới | Thú Triều (đường chính) | Mở thêm (số thử, phối hợp với tệp combat) |
|---|---|---|---|
| K0 | Luyện Khí | 1–3 | 4 ô kỹ năng, 1 pháp khí, 3 ô đan |
| K1 | Trúc Cơ | 4–6 | Ô kỹ năng thứ 5, Đạo Ấn 1, mở Tham Ngộ |
| K2 | Kim Đan | 7–9 | Ô tuyệt kỹ, ô đan thứ 4, Đạo Ấn 2 |
| K3 | Nguyên Anh | 10–12 | Ô kỹ năng thứ 6, vai trận thứ hai, Đạo Ấn 3 |
| K4 | Hóa Thần | 13–15 | Thăng công pháp lên tầng 3, Đạo Ấn 4 |
| K5 | Luyện Hư | 16–18 | Ô đan thứ 5, Đạo Ấn 5 |
| K6 | Hợp Thể | 19–21 | Đạo Ấn 6, mở Triều Luân Hồi |

- Mỗi cảnh giới có **sơ, trung, hậu kỳ**: tổng cộng 21 kỳ (k = 1…21). Lên kỳ nhỏ là **tự động** khi thanh tu vi đầy. Lên cảnh giới lớn phải qua Độ Kiếp.
- **Tu vi cần cho kỳ k** = 100 × 1,18^(k−1) (số thử): kỳ 1 cần 100, kỳ 6 cần 229, kỳ 21 cần 2.739, cộng cả thang khoảng 17.400.
- **Tu vi một lần đi đường chính của Thú Triều k** ≈ 1,1 × tu vi kỳ k. Chia ra: 70 % từ các trận thường (Thú Hạch tự luyện hóa), 20 % từ Thú Vương lần đầu, 10 % từ học (Ôn Tâm, Thẻ Ôn). Chơi lại cho 30 %. Như vậy **đường chính không cần cày** (cùng luật với Rồng 04 §8.4, §9).
- **Hệ số cảnh giới** R = 1 + 0,05 × (k − 1) + 0,08 × (số đại cảnh giới đã qua) nhân vào máu, linh lực và công nền. Ở kỳ 21, R ≈ 2,48. Độ khó của quái theo **R kỳ vọng** của Thú Triều đó. Một tài khoản đã nâng hết chỉ được mạnh hơn "bộ đồ trung bình" tối đa **25 %** (luật của Rồng 04 §8.4). Sức gõ và chiến thuật vẫn quyết định.

### 4.3 Đột phá: Độ Kiếp Đài

**Điều kiện:** đạt hậu kỳ viên mãn, đã hạ Thú Vương của Thú Triều cuối cảnh giới (tự đánh hoặc cùng đội, có đóng góp hữu ích), có 1 **Phá Cảnh Đan**. Thú Vương lần đầu luôn rơi đủ nguyên liệu cho viên đan này. **Không có tỷ lệ thất bại.** Thua Độ Kiếp thì không mất gì và đánh lại ngay.

**Trận Độ Kiếp** kéo dài 2–3 phút. Nhân vật ngồi giữa một vòng trận. Đây là ngoại lệ có chủ đích của luật di chuyển tự do: người đột phá **là trận nhãn**. Phối hợp với tệp combat.

| Pha | Diễn biến | Người chơi gõ gì |
|---|---|---|
| 1. Lôi Kiếp | Sét đánh vào các ô có báo trước ≥ 3 s | Từ trên **ấn hộ thân** (từ ôn đến hạn); gõ xong thì dựng khiên ở ô đó |
| 2. Tâm Ma | 3 + ⌊Tâm Ma/20⌋ hình bóng (3–8 con) tiến vào vòng trận | Mỗi tâm ma mang **một từ yếu** của chính người chơi (độ thuộc thấp nhất, sai nhiều). Nghĩa hiện mờ sau 2 s nếu chưa gõ |
| 3. Ngưng Cảnh | Chuỗi 3–5 từ khẩu quyết của cảnh giới (từ đã học trong cảnh giới này) | Gõ lần lượt; mỗi từ hiện nghĩa tiếng Việt, che 1–2 chữ cái (luật "Thiếu Chữ" của Rồng 04 §5.4) |

- **Kết quả:** phẩm chất cảnh giới Hạ, Trung hoặc Thượng phẩm, tính từ máu còn lại và độ chính xác. Chênh lệch chỉ ±3 % chỉ số nền, cộng màu hào quang và danh hiệu. Có thể **Củng Cố** (đánh lại Độ Kiếp) bất cứ lúc nào để nâng phẩm. Không có kết quả xấu nào là vĩnh viễn.
- **Đạo Ấn:** sau khi qua, chọn 1 trong 3 Đạo Ấn vĩnh viễn. Mỗi lần rút từ một bộ 9 ấn theo vai: công, hộ, trợ, triệu, trận. Ví dụ: "Kiếm Ý Bất Tán" cho phi kiếm nền tự hồi về tay sau khi trúng (giới hạn số lần mỗi giây); "Hậu Thổ Hộ Thân" tăng khiên khi đứng yên trong vùng trận (bonus định tâm, Codex §1.6). Ở Sơn Môn có thể **đổi lại** bằng Linh Thạch.

### 4.4 Công pháp: bí kíp → lĩnh ngộ → thuần thục → tham ngộ → thăng tầng

| Bước | Luật (số thử) |
|---|---|
| **Bí kíp** | Rơi ra từ Thú Vương, mua ở Đan Các/Tàng Kinh Các, hoặc thưởng Cơ Duyên. Chỉ mất khi đã học xong (sách không mất nếu phiên học chưa đạt) |
| **Lĩnh ngộ** | Đạt 100 điểm qua các phiên tĩnh tọa (4.5) ở Tĩnh Thất. Mỗi phiên tốn 3 Thú Hạch đúng bậc. Khi bắt đầu lĩnh ngộ, game chọn **6 từ khẩu quyết** từ hồ sơ học (từ mới ở mép Cấp Từ) và **lưu vào bản lưu của người chơi** |
| **Thuần thục** 0–100 mỗi tầng | +1 cho mỗi lần thi triển hợp lệ (tối đa 20 mỗi trận); +10 khi hạ Thú Vương có công pháp trong bộ; Phòng Luyện +5 mỗi phiên (tối đa 2 phiên/ngày). Thi triển hụt (ngoài tầm) không tính (Codex §1.5) |
| **Tham ngộ** | Ở thuần thục 50 và 100: chọn 1 trong 2 biến chiêu đã xem trước (Ngộ tính ≥ 75 thì 1 trong 3). Đổi lại sau: tốn Thú Hạch, có xem trước, không tung số |
| **Thăng tầng** (tầng 1 → 3) | Đủ 3 điều kiện: thuần thục 100; mỗi từ khẩu quyết đã được **gõ đúng ≥ 3 lần** trong trận (tức là đã tiếp xúc đủ, **không** đòi độ thuộc); 8 Thú Hạch. Tầng mới thêm 6 từ khẩu quyết và một phiên tĩnh tọa ngắn để học chúng. Tầng 3 mở từ Hóa Thần |

- **Khẩu quyết vào combat (phối hợp tệp combat):** ô kỹ năng của công pháp rút khoảng 50 % từ khẩu quyết của nó (ưu tiên từ có độ thuộc < 70) và 50 % từ bài của trận. Nhờ vậy từ học trong tĩnh tọa **được lặp lại tự nhiên** khi đánh. Độ thuộc của từ **không** làm chiêu mạnh hơn (luật Rồng 01 §6.7: không ai có lý do né từ mới).
- Dữ liệu là bảng, không chứa từ:

```jsonc
// content/techniques/kiem.phi-kiem.json (số thử)
{ "id": "kiem.phi-kiem", "school": "kiem", "slot": "vo-ky", "tiers": 3,
  "learn": { "points": 100, "costPerSession": { "thuHach": 3 }, "mantraWords": 6 },
  "mastery": { "perCast": 1, "capPerBattle": 20, "perBoss": 10, "trainingRoom": 5 },
  "insight": [ { "at": 50, "pick": ["xuyen", "tach-doi"] }, { "at": 100, "pick": ["hoi-kiem", "ho-than", "kiem-vu"] } ],
  "tierUp": { "mastery": 100, "mantraCorrectEach": 3, "cost": { "thuHach": 8 }, "minRealm": [0, 0, 4] } }
```

### 4.5 Tĩnh Thất: mini-game tĩnh tọa (bản của ta)

**Trước phiên:** thẻ Khẩu Quyết hiện 6 từ mới, mỗi từ có IPA, nghĩa và phát âm. Người chơi gõ lại mỗi từ một lần, không tính giờ (luật "Học trước" của Rồng 01 §6.5).

**Trong phiên:** dài 60 s. Tu sĩ ngồi giữa màn. Có 3–4 **điểm đọc** xếp theo cung rộng (Codex §18.3). Chữ nằm trong "liên hoa ấn" (khung hình hoa sen): Minh có viền sáng và dấu ☼, Thường viền trơn, Tạp Niệm viền gai và dấu ✕. Ngoài màu còn khác **hình viền và biểu tượng**, nên không phụ thuộc vào việc phân biệt màu.

| Loại | Lấy từ đâu | Vòng đời đọc được (E = tốc gõ kỳ vọng, `tempo.ts`) | Gõ xong đúng hạn | Để trôi |
|---|---|---|---|---|
| **Minh** | 6 từ khẩu quyết; mỗi từ xuất hiện ≥ 2 lần; lần đầu luôn hiện nghĩa | L = 1,0 s đọc + 1,6 × `typeSeconds(len, E)` + 1,0 s đệm (35 WPM, 6 chữ: khoảng 5,8 s) | +5 điểm lĩnh ngộ | Mất phần thưởng của mảnh đó; không phạt |
| **Thường** | Từ ôn đến hạn (`review priority`) | 1,5 × L | +2 điểm | Không phạt |
| **Tạp Niệm** | Từ có độ thuộc ≥ 70, khác chủ đề phiên; không bao giờ là từ mới | 2 × L (lảng vảng lâu để thử sự tập trung) | −4 điểm, +6 Tâm Ma (tối đa +30 mỗi phiên) | Tan đi, không phạt |

- **Điểm phiên** = 40 (hoàn thành phiên) + 5 × Minh + 2 × Thường − 4 × Tạp Niệm, kẹp trong [40; 100], cộng dồn qua các phiên. Một người chơi khá bắt được khoảng 12 Minh và 4 Thường, đạt 100 trong 1 phiên. Một người chơi mới bắt khoảng 6 Minh và 3 Thường, được 76 và cần phiên thứ hai.
- **Ngân sách cùng lúc** theo bảng preset của Codex §18.5 (Làm quen 2–3 chữ, Tiêu chuẩn 3–4, Thử thách khoảng 4). Mỗi preset đặt dải độ dài từ theo E bằng `lengthBand`. Hai chữ Minh **không bao giờ hết hạn cùng một cửa sổ** (§18.6). Bot `typist.ts` chạy 25/35/60/90 WPM để kiểm rằng ngưỡng 100 điểm **đạt được trong ≤ 2 phiên** ở mọi tốc độ.
- **Chữ đầu:** Minh, Thường và Tạp Niệm sống cùng lúc phải có chữ đầu khác nhau (`letters.ts` bậc 1). Từ đang khóa mà hết hạn thì được giữ thêm 1,2 s (ân hạn khóa); hết ân hạn thì phím lạc kế tiếp được tha (`session.ts`).
- **Tầng 2: Minh Tâm** (sau MVP, mở từ Kim Đan, dành cho từ có độ thuộc ≥ 40): bỏ dấu ☼/✕. Giữa thân tu sĩ hiện một **"tâm đề"** là nghĩa tiếng Việt hoặc tên một chủ đề. Từ khớp tâm đề là Minh; từ gần giống về chính tả hoặc khác chủ đề là Tạp Niệm. Lúc này **tránh Tạp Niệm đòi hiểu nghĩa thật**, không còn là nhận diện màu. Phản hồi sau phiên cho thấy nghĩa đúng của mọi từ đã gặp.
- **Âm thanh** (luật Q6 của `tools/audio-lab/DECISIONS.md` và luật chỉ dùng tiếng thu thật CC0): nền là gió núi và chuông đồng thật. Bắt Minh là tiếng chuông ngân dài. Lĩnh ngộ thành công là tiếng chuông lớn có vang. Không dùng tiếng "bụp", "pop" hay tiếng đồ chơi.

### 4.6 Ngộ tính

- **Ngộ tính = 50 + min(50; ⌊N70 / 25⌋) + thưởng Đạo Ấn/Khí Vận (≤ +10)**, trong đó N70 là số từ có độ thuộc ≥ 70 trong lõi học chung (Mastery v1, `shared/learning/README.md`). Từ thuộc ở game khác của portal cũng được tính. Ngộ tính nằm trong dải 50–110. Chiều tác động là **học thật → chỉ số RPG**. Chiều ngược lại bị cấm: Ngộ tính không bao giờ được coi là bằng chứng biết từ (Codex RV22).
- **Tác động** (có trần, nhìn thấy được, giống HUD của QCBH [video]): vòng đời Minh +1 % cho mỗi 5 Ngộ tính trên 50 (tối đa +12 %); Tham ngộ có 3 lựa chọn khi Ngộ tính ≥ 75; sàn điểm phiên tăng từ 40 lên 45 khi Ngộ tính ≥ 90. Ngộ tính không tự gõ, không tự bắt Minh, không làm Tạp Niệm vô hại.

### 4.7 Tâm Ma: thanh đo 0–100

| Tăng | Giảm | Tác động |
|---|---|---|
| Gõ xong Tạp Niệm: +6 (≤ +30 mỗi phiên) | **Ôn Tâm** ở Tĩnh Thất (3 phút ôn từ đến hạn, dùng `review-session`): −15 khi làm xong, thêm −10 nếu đúng ≥ 80 % | **Chỉ ở Độ Kiếp:** số tâm ma = 3 + ⌊Tâm Ma/20⌋. Từ 70 trở lên, pha 2 có thêm một "Tâm Ma Chủ" mang chuỗi 3 từ yếu |
| **Nợ ôn:** hồ sơ có > 80 từ đến hạn thì +5 mỗi khi vào Thú Triều (tối đa +20 mỗi ngày) | Hạ tâm ma trong Độ Kiếp: −5 mỗi con | **Không** gây bất lợi trong trận thủ ải. Người học không bị phạt trong trận chính vì quên bài |

- Ý tưởng cốt lõi: **tâm ma sinh từ những gì đã học mà bỏ quên**, nên cách trừ tâm ma là ôn. Thanh Tâm Ma luôn hiện ở Sơn Môn, kèm một câu giải thích ngắn.

### 4.8 Thọ mệnh: bỏ

Bỏ, vì game không có thời gian thế giới, không luân hồi, không di sản qua đời sau. Đồng hồ thọ mệnh sẽ thành áp lực ngày tháng (cảm giác sợ lỡ) hoặc thành một con số trang trí. Nếu chủ dự án muốn giữ chất "giành giật với số mệnh", có thể đặt **Mệnh Đăng**: 2 lần hồi sinh trong một Thú Triều, hồi lại ở Mốc. Đây là luật của lượt chơi, thuộc tệp combat quyết định. Chỉ số **Thọ nguyên** có thể hiện ở bảng nhân vật như lời mô tả cảnh giới, không có cơ chế.

### 4.9 Khí Vận và Cơ Duyên: bổ trợ trong lượt

| Lúc | Chọn | Kho (MVP) |
|---|---|---|
| Vào Thú Triều | 1 trong 3 **Khí Vận**, theo bậc Thường / Hiếm / Thiên Mệnh | 12 |
| Doanh Trại sau trận 2 và trận 4 | 1 trong 3 **Cơ Duyên**: bổ trợ nhỏ hơn, có thể nối với Khí Vận thành "song mệnh" | 18 |
| Tùy chọn khi vào Thú Triều | **Hung Cát:** tự bật 1–3 điều kiện khó để tăng thưởng (giống Lời Thề của Rồng) | 8 |

- **Ví dụ** (tên của ta, số thử): *Kiếm Tâm Thông Minh*: từ gõ không lỗi làm phi kiếm nền bắn thêm 1 đạn (tối đa 2 lần/giây). *Hậu Tích Bạc Phát*: trận 1–2 −10 % công, từ trận 4 +20 %. *Thú Hạch Hữu Duyên*: +25 % Thú Hạch, −10 % Linh Thạch. *Bất Động Như Sơn*: đứng yên trong vùng trận +15 % hộ thể. *Học Nhi Thời Tập*: lần đầu gõ đúng một từ mới hồi 2 % linh lực (tối đa 10 lần mỗi trận). Hung Cát *Huyết Nguyệt*: quái +20 % máu, thưởng +30 %.
- **Trần:** Khí Vận, Cơ Duyên, Đạo Ấn và tầng công pháp được xếp vào các **bucket** của Codex §21. Trong cùng một họ chỉ lấy giá trị mạnh nhất. Không Khí Vận nào cho lợi thế riêng cho một kênh nhập (Typing, Voice hay Hybrid).
- Không có Khí Vận nào chỉ mua được bằng tiền thật. Không có hộp ngẫu nhiên.

### 4.10 Cái gì giữ mãi, cái gì theo lượt

| Thứ | Trong Thú Triều | Qua Thú Triều | Thua Thú Triều |
|---|---|---|---|
| Cảnh giới, tu vi, Đạo Ấn, công pháp, thuần thục, trang bị | Giữ | Giữ | **Giữ** (tu vi đã nhận không mất) |
| **Linh Thạch** (tiền mua sắm) | Tích lũy | Giữ | Giữ 50 % phần của lượt |
| **Thú Hạch** (nguyên liệu tu luyện, có bậc theo cảnh giới) | Tích lũy | Giữ | Giữ 50 % phần của lượt |
| Khí Vận, Cơ Duyên, Hung Cát | Có hiệu lực | Mất | Mất |
| Máu, linh lực | Hồi 30 % giữa hai trận, cộng đan | Đầy lại | Đầy lại |
| Tâm Ma | Thanh đo | Giữ | Giữ |
| Độ thuộc từ | Lõi học chung, game **không tự tính** | | |

**Ba loại tiền là trần cứng** của mảng này: Linh Thạch, Thú Hạch và tu vi (tu vi không tiêu được). Tâm Ma là thanh đo, không phải tiền.

### 4.11 Sơn Môn và Doanh Trại

- **Sơn Môn** là một bức tranh 2D có chiều sâu (núi, mây, lầu gác), không đi lại. Mỗi điểm chọn bằng chuột hoặc phím 1–7. Thứ tự mở dần theo lịch dạy.

| Phím | Điểm | Việc | MVP |
|---|---|---|---|
| 1 | Thú Triều Đài | Chọn Thú Triều, mức khó, Hung Cát; xem thẻ triều (họ thú, Thú Vương, số từ mới) | Có |
| 2 | Tĩnh Thất | Lĩnh ngộ, Ôn Tâm, Tham Ngộ, Phòng Luyện | Có |
| 3 | Đan Các | Đan dược, phù (shop thuộc tệp khác) | Có |
| 4 | Độ Kiếp Đài | Đột phá, Củng Cố | Có |
| 5 | Tàng Kinh Các | Sổ công pháp, khẩu quyết, Sổ Từ | Sau |
| 6 | Luyện Khí Phòng | Trang bị (tệp khác) | Sau |
| 7 | Trận Đài | Đội hình, bot, phòng chờ đội | Khi có đội |

- **Doanh Trại** là màn nghỉ giữa hai trận, dài tối đa 90 s. Solo có thể dừng đồng hồ. Đội có nút "Sẵn sàng" và hạn 60 s. Nội dung: hồi phục, Cơ Duyên (sau trận 2 và 4), mua nhanh đan, 1 **Thẻ Ôn** gồm 3 câu (như Rồng 01 §6.5), xem trước trận kế.

**Một phiên chơi mẫu (khoảng 40 phút):** Sơn Môn 3 phút (Ôn Tâm, chọn Thú Triều và Khí Vận) → trận 1–2 → Doanh Trại (Cơ Duyên) → trận 3–4 (Mốc) → Doanh Trại → trận 5–6 → Thú Vương → về Sơn Môn: lĩnh ngộ một bí kíp mới (khoảng 2 phút) và Độ Kiếp nếu đủ điều kiện.

### 4.12 MVP và sau MVP

| MVP | Sau MVP |
|---|---|
| 2 cảnh giới (Luyện Khí, Trúc Cơ) × 3 kỳ; 6 Thú Triều × (4 trận + Thú Vương) | Cảnh giới 3–7, Thú Triều 6 + 1, Triều Luân Hồi |
| Độ Kiếp solo, 3 pha; Đạo Ấn: bộ 9 ấn, có đổi lại | Hộ pháp đột phá theo đội; Củng Cố; Tâm Ma Chủ |
| Tĩnh tọa tầng 1 + thẻ Khẩu Quyết; 6 công pháp, tầng 1–2, 1 mốc Tham Ngộ | Tầng 2 Minh Tâm (chọn theo nghĩa); tầng 3; Đồng Tu (tĩnh tọa song song cả đội) |
| Ngộ tính (công thức 4.6), Tâm Ma, Ôn Tâm | Phẩm chất cảnh giới có hiệu ứng hình ảnh riêng |
| 12 Khí Vận, 18 Cơ Duyên, 3 Hung Cát | Song mệnh, kho 40+ |
| Sơn Môn 4 điểm, lưu cục bộ | Tàng Kinh Các, Luyện Khí Phòng, đồng bộ tài khoản |
| **Bỏ hẳn:** thọ mệnh có cơ chế, tâm tình, cước lực, kỹ nghệ chơi tay (luyện đan, họa phù…), bản đồ du hành, quan hệ NPC, luân hồi, tỷ lệ đột phá thất bại, đổi kết quả bằng tải lại | Kỹ nghệ chỉ có thể quay lại dưới dạng **bậc mở khóa** của shop |

## 5. Solo và đội (2–3 người; 7 người là mở rộng; bot bù chỗ)

| Chủ đề | Solo | Đội 2–3 (bot bù chỗ trống) | Đại trận 7 (mở rộng) |
|---|---|---|---|
| Tĩnh tọa | Cá nhân, dừng được | Vẫn cá nhân. Ai cũng tĩnh tọa ở Sơn Môn của mình; không có hàng đợi chung | Như đội |
| Tu vi, Thú Hạch, Linh Thạch | Của mình | **Mỗi người nhận phần của mình**, không chia nhau. Rơi đồ theo từng người (Codex §1.7) | Như đội |
| Chênh cảnh giới | Không áp dụng | **Áp Cảnh:** Thú Triều có "cảnh đề cử". Người cao hơn bị hạ về cảnh đề cử + 1 kỳ (lợi thế tối đa khoảng +6 %). Người thấp hơn được nâng lên cảnh đề cử − 1 kỳ để chơi cùng bạn | Bắt buộc Áp Cảnh |
| Chống "kéo cấp" | Không áp dụng | Người được nâng nhận tu vi theo **Thú Triều đúng kỳ của mình** (×1,0), không theo triều cao. Muốn đột phá vẫn phải tự qua Độ Kiếp | Như đội |
| Thú Vương tính cho điều kiện đột phá | Tự hạ | Có mặt và có đóng góp hữu ích (Codex §22.3) thì được tính | Như đội |
| Khí Vận, Cơ Duyên | Tự chọn | Mỗi người tự chọn. Khí Vận loại "đồng khí" (tác dụng cả đội) theo luật một họ chỉ lấy mạnh nhất, nên 3 người cùng chọn không cộng dồn | Tối đa 2 Khí Vận đồng khí cho cả trận |
| Độ Kiếp | Một mình (MVP) | **Hộ Pháp** (sau MVP): một người đột phá, đồng đội giữ vòng trận chống thú triều nhỏ. Tâm ma chỉ người đột phá gõ được, vì đó là từ yếu của chính người đó. Hộ pháp nhận Linh Thạch và điểm Nhân Quả (danh hiệu). Solo thì bot làm hộ pháp | Không áp dụng |
| Bot | | Có chỉ số theo cảnh đề cử. **Không nhận tu vi**, không tạo sự kiện học, không có túi đồ (Codex §15, RV15) | Như đội |
| Mất kết nối | | Tu vi và đồ đã nhận được lưu sau mỗi trận. Bot thay chỗ theo Codex §15 | |
| Tạm dừng | Được | Không dừng trong trận. Doanh Trại có hạn 60 s | |

- **Luật công bằng cốt lõi:** mỗi người gõ từ của **hồ sơ học riêng**, theo dải độ dài của tốc gõ riêng (BALANCE §4.1). Không bảng nào so Ngộ tính hay cảnh giới giữa người học. Bảng xếp hạng (nếu có) tách theo solo / đội có bot / đội người và theo kênh nhập.
- Dữ liệu tu luyện nhỏ (dưới 20 KB JSON) nên lưu cục bộ trước, đồng bộ sau qua Worker tài khoản hiện có (D1, gói miễn phí). Phòng đội chỉ cần đọc cảnh giới đã khai, rồi áp Áp Cảnh. Sửa bản lưu cục bộ chỉ có tác dụng tới mức trần của Áp Cảnh.

## 6. Gắn với học tiếng Anh (Typing / Voice / Hybrid)

| Lúc | Từ nào | Cách học | `activityType` gửi về lõi chung | Chặn quá tải |
|---|---|---|---|---|
| Thẻ Khẩu Quyết | 6 từ mới của công pháp | Xem nghĩa, IPA, nghe, gõ lại; không tính giờ | `review-card` | ≤ 6 từ mỗi phiên; ≤ 12 từ mới khẩu quyết mỗi lần về Sơn Môn |
| Tĩnh tọa: Minh | Từ khẩu quyết (lần đầu có nghĩa) | Gõ có hạn giờ | `meditation-pick` (mới, ghi theo luật "một sự kiện có chấm cho mỗi từ mỗi phiên") | Preset Làm quen cho trẻ em và người mới; không giảm giờ và tăng mật độ cùng lúc |
| Tĩnh tọa: Thường | Từ đến hạn ôn | Gõ | `meditation-pick` | Tối đa 1/3 số chữ của phiên |
| Tĩnh tọa: Tạp Niệm | Từ đã thuộc (≥ 70) | Nhận ra và **không** gõ | Không gửi sự kiện (không ghi "sai tiếng Anh") | Màn kết ghi "chọn nhầm", không ghi "gõ sai" (Codex §18.2) |
| Minh Tâm (tầng 2) | Từ có độ thuộc ≥ 40 | Chọn theo nghĩa hoặc chủ đề | `meaning-recall` | Chỉ mở cho từ có độ thuộc ≥ 40 |
| Độ Kiếp: Tâm Ma | Từ yếu nhất, đến hạn | Gõ; nghĩa hiện sau 2 s | `typing-elite` | 3–8 từ mỗi lần |
| Độ Kiếp: Ngưng Cảnh | Khẩu quyết của cảnh giới | Thiếu chữ, có nghĩa | `meaning-recall` | 3–5 từ |
| Ôn Tâm | Từ đến hạn của mọi game portal | Phiên ôn chung (`review-session`, `mixed-review`) | `review-card` | 3 phút |
| Thăng tầng | Khẩu quyết | Gõ đúng ≥ 3 lần trong trận | (đã gửi từ trận) | Đòi **tiếp xúc đủ lần**, không đòi độ thuộc |

- **Nợ ôn:** khi > 80 từ đến hạn, số từ mới mỗi trận giảm còn 4 (luật Rồng 04 §7.2) và thanh Tâm Ma tăng (4.7). Khi > 150 từ đến hạn, Thú Triều Đài gợi ý "Ôn Tâm trước". Chỉ gợi ý, không chặn.
- **Voice và Hybrid** trong tĩnh tọa đóng vai **niệm khẩu quyết** (đọc to), rất hợp với bối cảnh. Dùng hồ sơ thời hạn riêng: vòng đời Minh +1,5 s. Chỉ kết quả nhận dạng cuối cùng đã được chấp nhận mới tính. **Tạp Niệm không bao giờ bị kích hoạt bởi kết quả tạm thời hoặc độ tin thấp** (Codex §22.2, RV31). Âm thanh nền và giọng TTS phải được tách khỏi micro (RV37).
- **Tách hai loại kết quả** ở màn kết phiên: phần học (từ mới đã gặp, độ chính xác, từ cần ôn) và phần RPG (điểm lĩnh ngộ, Tâm Ma). Bot và hộ pháp bot không tạo sự kiện học.

## 7. Tái sử dụng và chi phí sản xuất

| Cần | Dùng lại | Ghi chú |
|---|---|---|
| Từ sống, khóa, ân hạn, tha phím lạc | `shared/game-kit/typing/session.ts`, `router` | Luật hết hạn của Minh |
| Chữ đầu không trùng | `shared/game-kit/typing/letters.ts` | Bậc 1 giữa các loại chữ |
| Rút từ không lặp, ngân sách chữ sống | `shared/game-kit/typing/picker.ts`, `budget.ts` | Mỗi loại chữ là một nguồn có trần riêng |
| Vòng đời, chấm từ, tốc gõ E, dải độ dài | `shared/game-kit/typing/scorer.ts` (`typeSeconds`, `gradeWord`), `tempo.ts` | Công thức L ở 4.5 |
| Bot gõ giống người, cổng cân bằng | `shared/game-kit/balance/typist.ts`, `profile.ts`, `bands.ts`, `gates.ts` | Kiểm "đạt 100 trong ≤ 2 phiên" và Độ Kiếp |
| Sự kiện học, tra độ thuộc | `shared/game-kit/learning/{bridge,events,contract}.ts`; `shared/learning/{query,core}.mjs` | Ngộ tính (N70), từ yếu cho Tâm Ma |
| Ôn Tâm | `shared/learning/review-session.mjs`, `mixed-review.mjs` | Không viết thêm bộ ôn mới |
| Kho từ, lọc từ nhạy cảm | `shared/game-kit/vocab/vocabulary.ts`, `content-filter.ts`; `shared/vocabulary` | Khẩu quyết, Tạp Niệm |
| Giọng | `shared/game-kit/speech`, `shared/voice` | Niệm khẩu quyết |
| RNG có seed, lưu an toàn | `shared/game-kit/platform/rng.ts`, `safe-storage.ts` | Lịch chữ có seed để tái hiện |
| Mẫu thiết kế tiến trình | `docs/games/dragon-lane/04-stages-maps-progression.md` §8–10; `06-other-systems.md` §1, §4; `01-core-combat-learning.md` §6.5–6.7; `games/space-typing/docs/survival/SURVIVAL_MODE_PLAN.md` §4.0 (chọn cửa, bảng giữ/mất, Trạm Mẹ); `docs/games/BALANCE.md` | Luật "không cày", trần +25 %, chơi lại 30 % |

| Hạng mục | Mức | Ghi chú |
|---|---|---|
| Bản thử tĩnh tọa (canvas 2D + kit typing + bot kiểm) | **M** | Làm được độc lập với combat |
| Dữ liệu cảnh giới, tu vi, mở khóa, lưu | **S** | |
| Vòng đời công pháp (lĩnh ngộ, thuần thục, tham ngộ, thăng tầng) | **M** | Phụ thuộc deck combat |
| Độ Kiếp solo (dùng lại engine trận) | **M** | Thêm 3 pha, tâm ma mang từ yếu |
| Khí Vận và Cơ Duyên (30 mục và trần bucket) | **M** | Nặng về nội dung và cân bằng |
| Sơn Môn và Doanh Trại (UI) | **M**; tranh: **M** | Tranh 2D do Codex vẽ; không cần model 3D |
| Hộ Pháp đội | **L** | Cần netcode đội (Durable Objects) |
| Tầng 2 Minh Tâm | **M** | Cần dữ liệu nghĩa và chủ đề sạch (101 chủ đề chỉ phủ 1.177 từ) |
| Âm thanh (chuông, gió, sấm Độ Kiếp; thu thật CC0) | **S–M** | Theo luật Q6 |

## 8. Rủi ro và câu hỏi cho chủ dự án

| Rủi ro | Cách giảm |
|---|---|
| Từ mới bị đặt hạn giờ làm người mới hoặc trẻ em ngộp | Thẻ Khẩu Quyết không giờ; preset Làm quen; Minh lần đầu có nghĩa; bot kiểm ở 25 WPM |
| "Đừng gõ từ này" gửi thông điệp học sai | Tạp Niệm chỉ lấy từ đã thuộc; không gửi sự kiện học; phản hồi ghi "chọn nhầm" |
| Học trở thành cổng chặn sức mạnh | Thăng tầng đòi tiếp xúc, không đòi độ thuộc; Ngộ tính chỉ là phần thưởng có trần |
| Cày cuốc | Bot với "bộ đồ trung bình" phải qua đường chính; tu vi đường chính ≈ 1,1 × nhu cầu |
| Hub phình thành thế giới mở | Luật cứng: một màn, không đi lại, tối đa 7 điểm |
| Khí Vận × Đạo Ấn × công pháp nhân chéo nhau | Bucket và trần của Codex §21; mô phỏng chồng bổ trợ trước khi thêm nội dung |
| Giống QCBH quá mức | Tên, UI, tranh, luật của ta; bỏ chuỗi cảnh giới riêng của QCBH; không làm cầu tròn mang chữ Hán |

1. **Tiến trình meta và run chia thế nào?** *Đề xuất:* cảnh giới, công pháp, Đạo Ấn giữ mãi; Khí Vận và Cơ Duyên theo từng Thú Triều; thua vẫn giữ tu vi.
2. **Có giữ thọ mệnh không?** *Đề xuất:* bỏ cơ chế; nếu muốn chất "giành mệnh" thì dùng Mệnh Đăng (2 lần hồi sinh mỗi Thú Triều), do tệp combat quyết.
3. **Bao nhiêu cảnh giới, dùng tên gì?** *Đề xuất:* 7 cảnh giới × 3 kỳ (Luyện Khí → Hợp Thể), là tên phổ biến của thể loại, không dùng chuỗi Kết Tinh, Cụ Linh… của QCBH.
4. **Đổi "chữ Tâm ma" trong tĩnh tọa thành Tạp Niệm, còn Tâm Ma thành thanh đo cộng kẻ địch mang từ yếu ở Độ Kiếp?** *Đề xuất:* có.
5. **Đột phá có tỷ lệ thất bại không?** *Đề xuất:* không. Độ Kiếp là bài kiểm tra kỹ năng, thua thì đánh lại miễn phí, phẩm chất nâng được bằng Củng Cố.
6. **Mini-game có bắt buộc để lên tu vi không?** *Đề xuất:* không. Chỉ bắt buộc khi lĩnh ngộ công pháp mới (đó là lúc học từ mới).
7. **Gắn từ khẩu quyết vào ô kỹ năng trong trận (khoảng 50 %)?** *Đề xuất:* có, cần tệp combat xác nhận rằng bộ rút chữ còn đủ chữ đầu trống.
8. **Hub đi lại được hay một màn tĩnh?** *Đề xuất:* một màn tĩnh ở MVP; nhân vật đi lại trong Sơn Môn để sau, nếu bản thử cho thấy cần.
9. **Hộ Pháp đột phá theo đội làm tính năng đội đầu tiên ngoài Thú Triều?** *Đề xuất:* có, sau MVP; solo dùng bot hộ pháp.
10. **Chênh cảnh giới khi chơi cùng bạn?** *Đề xuất:* Áp Cảnh hai chiều (hạ người cao, nâng người thấp), tu vi tính theo kỳ của chính người nhận.
11. **Thưởng hằng ngày?** *Đề xuất:* không phạt khi bỏ ngày; chỉ Ôn Tâm có trần mềm mỗi ngày, giống Ôn Ngày của Rồng 04 §10.
