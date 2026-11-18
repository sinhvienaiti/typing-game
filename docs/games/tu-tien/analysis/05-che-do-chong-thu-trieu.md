# 05 · Chế độ lõi: chống ải thú triều

> **Mảng:** vòng chơi lõi của game tu tiên, giữ một ải trước các đợt yêu thú. Viết ngày 24/10/2026.
> **Đầu vào:** đề xuất Codex V2.2 (`TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md`), khung hình video Quỷ Cốc Bát Hoang (QCBH) chủ dự án quay (0:00–4:16), `docs/games/BALANCE.md`, `docs/games/SPLIT_PLAN.md`, `docs/games/dragon-lane/*`, mã `games/dragon-hold` (M0a), `games/typing-defense`, `games/typing-survival`.
> **Trạng thái:** đề xuất để chủ dự án duyệt. **Mọi con số là số thử.** Bot (`kit/balance`) và buổi chơi thử của chủ dự án sẽ chốt số.
> **Ký hiệu nguồn:** [video] là khung hình chủ dự án quay. [Codex §x] là tài liệu V2.2. [web: url] là nguồn web đã đọc. [trí nhớ] là điều nhớ được nhưng chưa kiểm.

## 1. Tóm tắt

- **Lõi game:** giữ một ải trên núi. Giữa ải có **Hộ Ải Đại Trận**. Thú triều tràn qua 1–3 cổng thú và một đường trời. Người chơi đi lại tự do, đứng trong trận để nhận gia trì hoặc ra ngoài chặn đầu, nhặt đồ. Kỹ năng phát ra khi người chơi gõ (hoặc nói) đúng từ tiếng Anh trên ô kỹ năng.
- **Cách gõ:** lấy **ô kỹ năng + đánh nền tự động** của Codex làm nền. Không gắn từ lên mọi con thú như Rồng Giữ Ải. Chỉ tinh thú, thú tướng và Thú Vương mang **từ Ấn** để phá thế.
- **Vật được giữ:** một thanh **Trận Lực** chung. Trận Lực về 0 là thua. **Trận nhãn** là vai đảm nhiệm, không có máu riêng. Thú có thể chiếm nhãn để tắt nó (đúng Codex §14.3).
- **Nhịp:** dùng mô hình tải gõ của Rồng Giữ Ải (`02 §5`) và bộ điều nhịp của `kit/balance` (BALANCE §4). Một trận triều thường có 5–6 đợt (5–7 phút). **Đại Triều** cuối chương có 10 đợt và Thú Vương (~12 phút).
- **Boss:** lớp chính là **phá thế** (phương án 3 của Codex). Mỗi đòn lớn có ít nhất hai cách giải: chạy khỏi vùng, nấp sau Trận Trụ, dựng khiên, hoặc gõ Ấn.
- **Solo trước:** solo thuần, rồi solo kèm bot bù ghế (Tam Tài). Đội người thật 2–3 làm sau. Thất Tinh 7 ghế là sự kiện tuần, làm sau cùng.
- **Nên làm game mới**, có repo riêng. Chép phần sim của Rồng Giữ Ải và dùng kit chung. Không nên làm thành mode bên trong `dragon-hold` (lý do ở §7.1).
- **MVP:** 1 ải, 1 lớp kiếm tu (5 ô), 5 họ thú, 1 thú tướng, 1 Thú Vương, 4 cơ quan, trận mẫu 10 đợt, chỉ solo, chỉ Typing. Kèm cổng bot B1–B9.

## 2. QCBH làm thế nào (chỉ phần liên quan)

| # | Quan sát | Nguồn | Bài học cho ta (không chép tên, UI, hình) |
|---|---|---|---|
| 1 | Arena 2D nhìn chéo từ trên, nền thủy mặc (rừng trúc, nghĩa địa). Nhân vật đi tự do. Phi kiếm tự bay vào đám quái. Có chữ "Bạo Kích", số sát thương đỏ | [video] 1:40–3:20, t160, t184 | Di chuyển tự do kèm đánh nền tự động đủ tạo cảm giác "tu sĩ ngự kiếm". Codex §1 đã chốt hướng này |
| 2 | Thanh dưới: Sinh lực, Linh lực, Niệm lực; 5 ô đan dược có số lượng; 4 ô kỹ năng (võ kỹ hồi 0,2–0,3 s, linh kỹ, tuyệt kỹ, thân pháp); nút "Trốn" | [video] t160, boss_08 | Gọn: một ô liên tục, vài ô hồi chiêu, một ô thân pháp. Ta thay 5 ô đan bằng cơ quan đặt giữa đợt, vì hai tay đang gõ |
| 3 | Kỹ năng thân pháp có hồi chiêu 20 s, tốn 25 Linh lực, có tầm và hệ Hỏa. Có 6 dòng "tu luyện kỹ năng" mở dần (1/6, tiến độ 220/300) | [video] t120 | Kỹ năng gồm hiệu ứng gốc và các dòng mở dần theo luyện tập. Ta cho dòng mở bằng số từ đã dùng đúng (việc học là luyện chiêu) |
| 4 | Quái đi theo bầy (lính giáo xương, hồn, dơi). Có bộ đếm quái còn lại. Phòng sạch quái thì "Trốn" đổi thành "Rời" và hiện vòng sáng dẫn sang phòng khác | [video] t120, t184, boss_03 | Mỗi đợt có số quái hữu hạn và kết thúc rõ. Nút Rút lui có cái giá (§4.10) |
| 5 | Đồ rơi có nhãn tên trên đất (Hạ Phẩm Hồn Thạch, Linh Thạch, thảo dược). Pet nhỏ theo chủ | [video] t184, t160 | Đồ thường tự hút, đồ hiếm đánh dấu (Codex §1.7). Pet làm sau MVP |
| 6 | Boss thú khổng lồ có thanh máu trên đỉnh (8877/10794). Đuôi quét thành một vạch dài. Nổ bụi lửa. Bãi đá đứng làm vật che. Gần chết hiện "Nhấn E để hấp thu yêu thú" | [video] boss_03–28, t252 | Vật che trên sân (Trận Trụ) là một cách giải đòn lớn. Đòn kết tùy chọn để thu lõi thú (Thu Hồn, §4.5) |
| 7 | Bản đồ phòng ở góc phải trên, nút đỏ là boss | [video] t120 | Ta không làm phụ bản nhiều phòng. Thẻ đợt báo trước cổng nào ra gì (§4.7) |
| 8 | Boss gắn với vùng theo hệ và theo cấp. Có boss thế giới. Có boss bắt buộc phải hạ để đột phá hoàn mỹ. Có nhiệm vụ "hàng phục yêu thú" | [web: https://kosgames.com/tale-of-immortal-all-bosses-guide-5887/] | Thú Vương mỗi chương là cửa đột phá cảnh giới (§4.9). Mỗi ải có một hệ chủ đạo |
| 9 | Có sự kiện yêu thú kéo đến thành, người chơi cùng NPC giữ thành, thưởng theo đóng góp | [trí nhớ], chưa tìm được nguồn xác nhận | Chỉ lấy ý "thưởng theo đóng góp đúng vai", không lấy luật cụ thể |
| 10 | Mini-game tu luyện thu cầu ngộ, tránh cầu tâm ma | [video] 0:14–0:44, [Codex §17–18] | Thuộc mảng tu luyện. Ở đây chỉ nối thưởng: Yêu Đan và tàn trang công pháp từ thú triều đi vào tu luyện |

**Không lấy:** thế giới mở, du hành, NPC, hội thoại, phụ bản nhiều phòng, cách bày thanh HUD và tên kỹ năng, quái của QCBH. Nhiều quái trong QCBH lấy từ Sơn Hải Kinh. Ta tự vẽ, tự đặt tên Thú Vương; nếu dùng thần thoại thì diễn giải hình riêng (Codex §20).

## 3. Codex V2.2 nói gì về mảng này

Codex chưa thiết kế riêng chế độ thú triều. §0 và §8 chỉ ghi đó là "một hoạt động/một mode". Nay chủ dự án chốt thú triều là **lõi** của game, nên năm phương án của Codex trở thành các lớp bên trong chế độ này.

| Mục Codex | Quyết định | Lý do |
|---|---|---|
| §0, §1.1–1.4: đi tự do, Typing/Voice/Hybrid, một từ là một giao dịch | **Giữ** | Nền đã chốt. Một hành động chỉ chốt một lần, áp được cho cả đội |
| §1.5: nhãn chiêu khi di chuyển; không có đích thì không tiêu hồi chiêu | **Giữ** | Tránh phạt người gõ đúng mà quái vừa chết |
| §1.6: trong trận/ngoài trận tách khỏi đứng yên/di chuyển | **Giữ, thêm số**: liên kết nhãn r 3 m, Kết Giới r 9 m, đệm 1,5 s, phai 3 s, nối lại 1 s | Codex mới ghi "1–2 s đệm, chưa chốt" |
| §1.7: nhặt đồ, loot cá nhân | **Giữ** | Đội không tranh đồ |
| §1.9, §9.2: 4–6 ô, một ô liên tục, một ô tự cứu | **Giữ**: kiếm tu MVP có 5 ô + ô Hợp Trận | Luôn có từ để gõ. Đây là cách sửa lỗi "Nhàn I" mà Rồng Giữ Ải M0a đang trượt (§4.7) |
| §3 thân pháp/trận vị | **Giữ ở dạng gốc**: Trận Trụ, cổng, Thú Huyệt là các điểm có giá trị | Đi ra ngoài phải có lý do. Không cần mở một phương án riêng |
| §4 ngự kiếm truy kích | **Để sau MVP**: màn "truy Thú Vương bỏ chạy" sau Đại Triều | Tốn camera và dựng màn. Không cần cho vòng lõi |
| §5 phá thế/phản chế | **Giữ, làm lớp boss chính** | Hợp với giữ ải: đọc đòn rồi chọn cách giải. Codex cũng xếp ưu tiên cao |
| §6 ngưng thời lập chiêu | **Bỏ khỏi thú triều** | Dừng thời gian mâu thuẫn với áp lực liên tục (BALANCE §5) và với đội chơi thời gian thực. Có thể làm mode luận kiếm solo riêng |
| §7 điều quân nhiều tuyến | **Để sau**: biến thể "Đa Tuyến" có đệ tử NPC giữ cổng | Cần AI và UI tốt. Thêm tải chú ý |
| §8: một phụ bản một cơ chế chính, tối đa một cơ chế phụ | **Giữ** | Mỗi trận triều có một luật ải (§4.9) |
| §9.1: đánh nền 15–25 % sát thương | **Sửa**: gõ 60–70 %, đánh nền 12–18 %, cơ quan + trận 15–25 %. Cổng: gõ ≥ 55 % | Trụ cột "gõ là sức chính" (BALANCE B5, Rồng Giữ Ải trụ 1) |
| §10.2: mốc K0–K6 | **Giữ**: mỗi chương gắn một mốc K gợi ý | Khó tăng theo thành phần thú, không theo đòi gõ nhanh |
| §14.2–14.4: Lưỡng Nghi, Tam Tài, Thất Tinh; nhãn là vai; HP cá nhân + hộ trận chung; nạp không đồng bộ | **Giữ toàn bộ** | Đúng nhu cầu solo/đội. Không có máu cho từng công trình |
| §15: bot | **Giữ**. Thêm: khóa phiên bản trận theo số ghế lúc vào | Máu thú không co giãn giữa trận |
| §16, §16.1: vai quái, công thức T_gõ = 12 × ký tự / WPM | **Sửa công thức**: cộng thời gian đọc, nhận từ, hoạt ảnh, trễ kênh; nhân biên 1,6 (§6) | Công thức Codex bỏ quên thời gian nhận từ (BALANCE §6: 0,35–1,6 s) |
| §21–22: trần chỉ số, công bằng, đóng góp support | **Giữ** | Dùng cho thưởng đội (§5) |
| §26.8: thử 1/3/7 người × 50/100/200/300 quái | **Giữ**, làm **trước** khi vẽ hàng loạt | Bài học Rồng Giữ Ải: chạy bench trước |
| Codex không có mô hình đợt, nhịp, kinh tế trong trận | **Thêm** từ `dragon-lane/02 §5`, `03 §3–4` và BALANCE | Đã có mã chạy và có cổng bot |

## 4. Đề xuất cho game chống ải thú triều

### 4.1 Bản đồ một ải (MVP: Thanh Thạch Ải)

```text
   [Cổng Thú A]            ~ đường trời (Hỏa Nha) ~            [Cổng Thú B]
        \\   ô1      ô2                              ô3      ô4   //
         \\_____  ▲Trận Trụ     (hẻm giữa, hẹp)     ▲Trận Trụ ____//
                \__________________     ________________/
                        ô5      (  Kết Giới r 9 m  )      ô6
                [Nhãn Công]        ◎ TRẬN TÂM           [Nhãn Dưỡng]
                                   [Nhãn Thủ]
                 ═══════════ Sơn Môn (nền phía sau, không đánh) ═══════════
```

- Sân khoảng **40 × 26 m**. Camera cố định thấy cả ải ở 1080p (~33 px/m). Người cao ~55 px, Thú Vương ≥ 120 px (luật của `dragon-lane/02 §4.1`). Góc nghiêng 3/4 như [video]. Hình 2D có chiều sâu (Codex §26).
- **Đường thú:** mỗi cổng là một trường hướng (flow field) dẫn tới Trận Tâm. Thú không bị buộc vào làn hẹp như Rồng Giữ Ải, nhưng đi theo hành lang đọc được. Đường trời bỏ qua cơ quan đặt trên đất.
- **Trận Trụ (2 cột đá):** chặn đạn ném, chặn cú húc của boss (§4.5). Mỗi cột chịu 2 cú húc rồi nứt tới hết trận. Đây là vật che theo kiểu [video] boss, nhưng có luật rõ.
- **Ô cơ quan:** 6 ô cố định (ô1–ô6), chỉ hiện lúc bày trận và lúc nghỉ. Giống quyết định "ô có sẵn" của Rồng Giữ Ải (DESIGN §11, câu 8).
- **Không có tường, cổng hay nhà có máu** trong bản đầu (Codex §14.3).

### 4.2 Trận pháp: vật được giữ

| Thành phần | Luật (số thử) |
|---|---|
| **Trận Tâm** | Thanh **Trận Lực** 1.000 (solo). Thú vào Kết Giới thì cắn Trận Tâm. Về 0 là thua |
| **Kết Giới** (r 9 m) | Thú trong vùng chậm 15 %. Người chơi trong vùng nhận −10 % sát thương. Ra khỏi vùng: đệm 1,5 s, phần gia trì phai trong 3 s. Vào lại: nối lại sau 1 s. Ra vào nhiều lần không cộng dồn (Codex §1.6) |
| **Trận nhãn** (r 3 m) | **Công:** +12 % sát thương chiêu của người giữ nhãn, cột kiếm tự bắn 0,1 W mỗi 2 s. **Thủ:** Trận Tâm nhận −25 % sát thương từ thú trong góc của nhãn, khiên của người giữ nhãn ×1,2. **Dưỡng:** hồi 0,4 % Trận Lực mỗi giây nếu người giữ nhãn gõ xong một từ trong 3 s gần nhất, hồi đồng đội trong 6 m. Solo thuần có một **Tâm nhãn** gộp cả ba tác dụng ở mức 2/3 |
| **Chiếm nhãn** | Thú loại "chiếm chốt" (Codex §16) đứng trên nhãn 3 s thì nhãn tắt tới khi nó chết. Đồng thời hiện một từ **Tẩy** ngắn (D1–D2) trên nhãn: ai gõ xong thì nhãn sáng lại sau 1 s. Không có máu cho nhãn |
| **Trận Ý** | Mỗi từ hợp lệ do người đang liên kết nhãn gõ xong cho +1, tối đa +1 mỗi 0,6 s. Cần 24 điểm để đầy. Ở 35 WPM khoảng 70 s đầy một lần. Pet, bot và đánh nền không nạp (Codex §14.3) |
| **Hợp Trận** | Khi Trận Ý đầy, ô thứ 6 hiện **Kết Ấn** là chuỗi chủ đề 2 từ, gõ trong 8 s. Solo: 2,5 W lên mọi thú trong Kết Giới, cụm bầy chịu tối đa 60 % máu cụm (BALANCE §9.1). Hợp Trận gây tối đa 12 % sát thương cả trận. Đội: xem §5 |

### 4.3 Người chơi trong trận

- **Di chuyển:** mũi tên hoặc chuột phải (click-to-move). WASD chỉ dùng qua chế độ Tab (Codex §1.2). Tốc chạy 5 m/s. Không chặn thân đồng đội.
- **Đánh nền:** phi kiếm 0,2 W mỗi 2,4 s, tầm 9 m. Tự chọn thú gần Trận Tâm nhất, trừ khi người chơi click đặt mục tiêu mềm. Giáp chặn đánh nền và cơ quan.
- **Chiêu gõ bỏ qua giáp và kháng** (giống `dragon-lane/02 §1.2`), nên gõ luôn có giá trị.

| Ô | Kiếm tu MVP | Tác dụng (số thử) | Hồi | Khi đang đi |
|---|---|---|---|---|
| 1 | Kiếm Khí (liên tục) | 1 W lên một mục tiêu: mục tiêu mềm, nếu không có thì thú gần Trận Tâm nhất trong 12 m | 0 | Được |
| 2 | Kiếm Vũ | Vùng r 3 m tại cụm đông nhất trong 12 m (hoặc điểm chuột), 0,6 W mỗi con, tối đa 8 con | 8 s | Được |
| 3 | Phá Thế Trảm | Nón 90° tầm 3 m, 1,5 W, −25 Thế. Thú thường choáng 1 s | 10 s | Dừng 0,3 s, có báo |
| 4 | Hộ Thể Quyết (tự cứu) | Khiên bằng 25 % Sinh lực trong 6 s | 15 s | Được |
| 5 | Lưu Quang Bộ (thân pháp) | Lướt 6 m theo hướng đang đi hoặc hướng chuột. Không miễn thương (Codex §3.3) | 6 s | — |
| 6 | Kết Ấn (Hợp Trận) | §4.2 | Theo Trận Ý | Được |

- Từ trên mỗi ô **đổi sau mỗi lần dùng**. Mọi từ đang hiện (ô, Ấn, Tẩy) có **chữ đầu khác nhau** và không là tiền tố của nhau (`kit/typing/letters`, Codex §1.4).
- **Trọng thương:** Sinh lực 600 (mốc K0). Về 0 thì nằm 8 s rồi hồi sinh ở Trận Tâm, Trận Lực −5 %. Trọng thương không làm thua. Đồng đội đứng cạnh 2 s thì thời gian còn một nửa.

### 4.4 Yêu thú: họ, bậc, hệ

Bậc và W lấy theo `dragon-lane/02 §1.2`. **1 W** là sát thương một từ Vừa ở ô liên tục của bộ tham chiếu 100 (Codex §10.2) tại mốc K của ải. Máu = W × 90 ở chương 1.

| Mã | Tên | Họ · hệ | Bậc · W | Tốc | Vai (Codex §16) | Đòn chính · báo trước | Khắc chế |
|---|---|---|---|---|---|---|---|
| T01 | Thạch Thử | Thử · Thổ | Bầy 0,4 W, cụm 6–8 con | S3 | Bầy áp sát | Gặm 2 mỗi 1 s, không báo | Kiếm Vũ, Lôi Phù Trụ, Kiếm Thung |
| T02 | Phong Lang | Lang · Phong | Nhỏ 1 W, đi đàn 3–5 | S3 | Áp sát, vồ qua người chặn | Vồ 4 m, 12 sát thương, báo 0,6 s | Kiếm Khí, Phong Ấn Võng |
| T03 | Hỏa Nha | Điểu · Hỏa | Nhỏ 0,8 W, bay | S3 | Quấy người, bỏ qua cơ quan đất | Mổ sà 5, bóng sà 0,5 s | Kiếm Khí, Mê Vụ (mất mục tiêu), Võng (kéo xuống) |
| T04 | Nham Viên | Viên · Thổ | Vừa 2 W | S1 | Bắn xa vào nhãn và Trận Tâm | Ném đá 12 m, 15 sát thương, báo 0,8 s; Trận Trụ chặn | Lưu Quang Bộ để áp sát, Phá Thế Trảm |
| T05 | Thiết Giáp Trư | Giáp · Kim | Vừa 3 W, giáp G2, có Thế 30 | S1, húc S3 | Giáp dày, chiếm nhãn | Húc 8 m, 40 sát thương, vạch đỏ 0,9 s | Chiêu gõ (xuyên giáp), Võng, Trận Trụ |
| G01 | Lang Đầu Đàn (thú tướng) | Lang · Phong | 7 W, Thế 60, 1 Ấn | S2 | Hỗ trợ địch | Hào quang 6 m: sói +15 % tốc. Tru Đàn: gọi 3 sói, báo 1 s | Ấn, Phá Thế Trảm, CÂM (sau MVP) |
| V01 | Thiết Bối Lang Vương | Lang · Kim | 40 W, Thế 100 | S2 | Thú Vương | §4.5 | |

- **Hệ:** khắc chế đổi ±20 % sát thương, không có miễn nhiễm tuyệt đối (Codex §16). Bộ hệ do file thuộc tính chốt. Mỗi ải có một hệ chủ đạo.
- **Tinh thú:** thú thường mang 1–2 thuộc tính tinh anh, có thanh Thế 40 và một từ Ấn. MVP có 3 thuộc tính: **Cuồng** (+30 % tốc), **Thiết Bì** (+2 W, giáp +1 bậc), **Hồi Nguyên** (hồi 1,5 %/s khi 3 s không trúng đòn). Bộ đủ 12 thuộc tính theo mẫu `dragon-lane/02 §2.4`.
- **Sau MVP:** Huyễn Hồ (niệm phép, hồi bầy, tạo ảo ảnh), Độc Mãng (vũng độc, làm chậm), Nham Quy (khổng lồ có mai che), Lôi Điêu (bay, sét nối các nhãn), thú đào hang trồi giữa sân. Mỗi họ có thêm 2–3 loài theo vùng.
- **Trình bày:** trúng đòn là **vệt mực** chứ không phải máu. Chết thì tan thành mực và một đốm linh quang. Như vậy hợp nét thủy mặc, hợp mọi lứa tuổi, và cùng luật "không máu" với các game trên portal.

### 4.5 Thú Vương mẫu: Thiết Bối Lang Vương (cuối chương 1)

Luật chung theo `dragon-lane/02 §4.1`: đòn thường báo trên đất ≥ 1,2 s; đại chiêu nạp 3–6 s; **tối đa 2 cơ chế cùng lúc, một từ Ấn mỗi lúc**; không có đòn ngẫu nhiên không báo.

- **W 40** (= round(0,38 × 0,7 × 150 s), công thức `00 §4.7`). Máu 3.600. Đích: ~150 s ở 35 WPM, ~200 s ở 25 WPM (k = 0,75).
- **Thanh Thế 100.** Gõ Ấn −35. Phá Thế Trảm −25. Phong Ấn Võng −15. Mỗi W sát thương chiêu −1. Thế về 0 thì **phá thế**: Vương ngã 6 s, nhận sát thương ×1,5. Sau đó 15 s Thế không giảm (Codex §5.3, chống khóa boss mãi).

| Pha | Đòn và báo trước | Cách giải (≥ 2) |
|---|---|---|
| P1 (100–60 %) | **Vồ Xé:** nón đỏ 6 m báo 1,2 s vào người chơi gần nhất. **Tru Gọi Đàn** mỗi 20 s: 1 cụm Thạch Thử + 2 Phong Lang, sóng vòng báo 1 s | Lướt hoặc đi ra khỏi nón; Hộ Thể. Kiếm Vũ cho đàn |
| P2 (60–30 %) | **Thiết Bối Xung:** vạch đỏ từ Vương tới Trận Tâm, nạp 3 s. Từ Ấn (D3, từ đã thuộc) hiện trên Vương | (a) Gõ Ấn, cộng Phá Thế Trảm, để phá thế: hủy cú húc. (b) Đứng sau Trận Trụ: Vương đâm cột, choáng 2 s (không tính phá thế). (c) Dựng Hộ Thể rồi đứng chặn: nhận một nửa. Không giải: Trận Lực −8 %, người trong vạch bị hất 3 m |
| P3 (< 30 %) | **Cuồng:** tốc +25 %. Gọi Đàn mỗi 12 s. Thiết Bối Xung mỗi 15 s | Như P2. Cơ quan Võng giảm Thế |
| Kết (< 5 %) | Hiện **Thu Hồn**: một từ chủ đề D4 màu ngọc, 6 s | Gõ kịp: +1 Yêu Đan Thượng phẩm. Không gõ: Vương vẫn chết bởi sát thương thường, không bị phạt |

- Chuyển pha: Vương gầm 2,5 s, miễn sát thương, từ Ấn cũ bị hủy (`dragon-lane/02 §4.1`).
- Ấn có tác dụng trong 16 m, không cần đường nhìn, để lớp tầm xa không phải lao vào.
- Âm: gầm phải trầm, vang và nặng như con thú to. Bước chân rung đất. Cấm âm "bụp/thụp" (`tools/audio-lab/DECISIONS.md` Q6). Chỉ dùng tiếng thu âm thật CC0, kiểm giấy phép từng trang.

### 4.6 Cơ quan (đặt giữa đợt, tự kích hoạt)

| Cơ quan | Đặt ở | Tác dụng (cấp 1, số thử) | Giá · nâng cấp | Mạnh với |
|---|---|---|---|---|
| Kiếm Thung | Dải đất 4 m | Chậm 25 %, 0,05 W/s lên mỗi thú trong dải | 60 · +70 | Bầy, sói |
| Lôi Phù Trụ | Trụ | Mỗi 3 s đánh xích 3 mục tiêu, 0,4 W mỗi mục tiêu | 120 · +90 | Cụm bầy |
| Mê Vụ Trận | Vùng r 4 m | Chậm 30 %. Thú bay mất mục tiêu 2 s. Nham Viên trong vùng ném trượt 50 % | 90 · +70 | Bay, bắn xa |
| Phong Ấn Võng | Trụ | Mỗi 10 s trói thú nặng nhất trong tầm 3 s (thú bay bị kéo xuống). −15 Thế | 100 · +80 | Giáp, tướng, Vương |

- Tiền trong trận là **Trận Nguyên**: 150 lúc đầu, cộng ~950 chia theo quái, cuối đợt và sự kiện. Cách chia theo `games/dragon-hold/src/sim/economy.ts`. Dựng hết 6 ô cấp 3 tốn ~2.600, nên người chơi chỉ đủ ~40 % và phải chọn.
- MVP chưa có từ kích hoạt cơ quan (giống Rồng Giữ Ải M0, quyết định D13). Cơ quan, đánh nền và Hợp Trận cộng lại gây tối đa 45 % sát thương cả trận.

### 4.7 Nhịp đợt và bộ điều nhịp

```text
Bày trận (xem thẻ đợt, Học trước 8 từ, đặt cơ quan) → Enter
  → [ Tù và báo 5 s → Đợt 35–60 s → Nghỉ 15 s (cơ quan, Thẻ Ôn, nhặt đồ) ] × N
  → Lặng 12 s → Thú Vương → Kết trận (sao, thưởng, Sổ Từ)
```

- **Tải gõ** dùng mô hình `dragon-lane/02 §5.4`: W_gõ(đợt) = L × 22,7 × số phút. Một cụm bầy tính 1 W_gõ, vì một Kiếm Vũ diệt được cụm. Tải giữ trong một dải ở mọi chương. Khó tăng bằng thành phần thú, không bằng số từ mỗi phút.
- **Đỉnh và lặng:** mỗi đợt có 2–3 đỉnh dài 6–10 s (nhịp ×1,6), lặng ≥ 8 s (nhịp ×0,4). Mỗi cổng ra tối đa một toán mỗi 1,5 s (`02 §5.3`). Trần thú sống là 60 (MVP), là luật cố định, không đổi theo cấu hình máy. Muốn nâng thì chạy bench trước.
- **Áp lực liên tục** (BALANCE §5): Nham Viên ném vào nhãn và Trận Tâm khi trong tầm, Hỏa Nha quấy người chơi, thú trong Kết Giới cắn Trận Lực. Gõ nhanh và chuẩn thì mất ít Trận Lực hơn một cách liên tục.
- **Sửa lỗi "Nhàn I" của Rồng Giữ Ải M0a** (`games/dragon-hold/docs/changelog/2026-10-24-m0a-round2-gate.md`: I của bot Chuẩn 20,5 %, phần lớn vì quái chưa vào Vùng Chữ). Ở đây ô kỹ năng luôn có từ, nên I chỉ tính lúc không có thú nào trong tầm. Thời gian thú đi từ cổng tới Kết Giới đặt 8–12 s với thú Nhỏ, để bot Chuẩn hạ thú ở Q 55–70 % quãng đường.
- **Nhịp k hai chiều** theo BALANCE §4.1: k = clamp(C(E_eff) / C_ref; 0,75; 1,30).
- **Bộ điều nhịp** (`kit/balance/director.ts`): cứ 5 s xét một lần. Mỗi bậc là một trong: khoảng sinh ±7 %; thêm hoặc bớt một thuộc tính tinh anh ở toán kế; dời đỉnh ±3 s; lặng ±3 s; rơi một Linh Dịch (+5 % Trận Lực) khi gần thua, tối đa một lần mỗi đợt. **Không bao giờ** đổi máu thú đang sống, đổi pha boss, đổi từ hay đổi cách chấm. Tắt ở Vô Tận, bảng xếp hạng và đội xếp hạng.
- **Thẻ đợt** lúc nghỉ: mỗi cổng có biểu tượng họ, số con, dấu đặc biệt (cánh là bay, búa là chiếm nhãn, vương miện là thú tướng, sừng là Vương) và một dải nhịp cho thấy đỉnh rơi vào giây nào (`02 §5.6`).

### 4.8 Trận mẫu 10 đợt: "Đại Triều Thanh Thạch Ải" (số thử)

Ải cuối chương 1, solo, người tham chiếu 35 WPM. Các họ đã được dạy ở các trận 1–4 của chương. Trận Lực 1.000.

| Đợt | Dài | Tải L (đỉnh) | W_gõ | Thành phần | Ghi chú |
|---|---|---|---|---|---|
| 1 | 35 s | 0,60 | 8 | 6 Phong Lang + 2 cụm Thạch Thử | 1 cổng |
| 2 | 40 s | 0,70 | 11 | 6 Phong Lang + 3 cụm + 1 Nham Viên | 2 cổng |
| 3 | 45 s | 0,80 | 14 | 4 Phong Lang + 3 cụm + 4 Hỏa Nha + 2 Nham Viên | Mở đường trời |
| 4 | 50 s | 0,90 | 17 | 5 Phong Lang + 3 cụm + 1 Thiết Giáp Trư + 2 Nham Viên + 3 Hỏa Nha | Lần đầu có thú chiếm nhãn |
| 5 | 55 s | 1,00 (1,15) | 21 | **Lang Đầu Đàn** (7) + 6 Phong Lang + 3 cụm + 1 Giáp Trư + 2 Hỏa Nha | Tướng 33 % ≤ trần 35 % (`02 §3.1`) |
| 6 | 45 s | 0,75 | 13 | 4 cụm + 3 Nham Viên + 1 Giáp Trư | **Đợt thở.** Thú Huyệt hiện ở cổng B (3 W, tùy chọn): phá được thì đợt 7 bớt 1 cụm mỗi đỉnh, +60 Trận Nguyên |
| 7 | 55 s | 1,00 | 21 | 6 Phong Lang + 4 cụm + 2 Giáp Trư + 2 Nham Viên + 1 Hỏa Nha | Gọng kìm: 2 cổng cùng ra |
| 8 | 60 s | 1,10 | 25 | 7 Phong Lang + 5 cụm + 2 Giáp Trư + 2 Nham Viên + 4 Hỏa Nha | |
| 9 | 60 s | 1,20 (1,35) | 27 | Lang Đầu Đàn + 6 Phong Lang + 5 cụm + 1 Giáp Trư **tinh anh Thiết Bì** (5) + 2 Nham Viên | Đỉnh cuối mạnh nhất |
| 10 | 30 s + Vương | 0,80 rồi Vương | 9 + 40 | Hộ tống 2 cụm + 4 Phong Lang, rồi lặng 12 s, rồi Thiết Bối Lang Vương | §4.5 |
| **Cộng** | **~12 phút** | TB 0,93 (đợt 1–9) | **157 + 49** | **~310 con, 73 % là bầy** (32 cụm × ~7) | Cảm giác "triều", nhưng chỉ ~206 từ cần gõ |

- **Sức gõ 35 WPM:** 0,38 W/s × 445 s × 0,9 ≈ 152 W, gần bằng 157 W_gõ của đợt 1–9. Nhưng các đỉnh 1,15–1,35 kéo dài 6–10 s thì vượt sức gõ. Kiếm Vũ hồi 8 s, nên không theo kịp một cụm mỗi 4 s lúc đỉnh. Phần dư do đánh nền (~37 W), cơ quan và Hợp Trận gánh. Thiếu chúng thì thú lọt vào Kết Giới.
- **25 WPM:** k = 0,75 nên đợt giãn 33 %, sức gõ quy đổi ≈ 152 W. Trận dài ~15 phút. **60 WPM:** k nén tới 1,30.
- **Cổng bot cho trận này** (thêm vào B1–B9 của BALANCE §7): bot Chuẩn thắng 75–90 %, S 35–65 %. **Chỉ gõ** (không cơ quan, không Hợp Trận) thắng ≤ 40 %. **Không gõ** thua trước hết đợt 3. Phần sát thương do gõ ≥ 55 %. Tải đỉnh ≤ 1,40. Từ sống ≤ 9.
- Nếu bot cho S > 65 % thì tăng đe dọa của thành phần (tốc, tinh anh, cổng), **không** tăng W_gõ (BALANCE §1.7).

### 4.9 Cấu trúc chương, cảnh giới và chơi lại

- **Thế giới:** **Biên Ải** là dải ải nằm giữa nhân giới và vùng hoang thú. Tông môn của người chơi trấn giữ các ải. Tông môn là một màn chọn chức năng (cửa hàng, tu luyện, cơ quan, sau này có pet), không phải thế giới mở.
- **Một chương = một ải** (địa danh), gắn một mốc K gợi ý (K0–K6, Codex §10.2) và một hệ chủ đạo. Một chương có 8 trận:

| Trận | Loại | Đợt | Mục đích |
|---|---|---|---|
| 1–3 | Dạy | 5 | Mỗi trận dạy một họ thú hoặc một cơ quan mới. Loài mới ra lẻ 3 lần trước khi trộn (`02 §5.6`) |
| 4 | Thú tướng | 6 | Tướng ở đỉnh đợt cuối |
| 5 | Ôn | 4 | Từ ôn đến hạn, thưởng Tri Thức. Thú dễ |
| 6–7 | Trộn + luật ải | 6 | Một luật ải mỗi trận: sương che, đêm, lũ cuốn một cổng, mưa sét |
| 8 | **Đại Triều** | 10 | Thú Vương. Hạ lần đầu được vật phẩm đột phá cảnh giới (nối mảng tu luyện; ý từ [web: kosgames]) |

- **Khó tăng theo** (BALANCE §1.7): số cổng (1 → 2 → 3 + đường trời), họ mới, tinh anh, thú tướng có hào quang, hệ khắc, luật ải, Thú Vương nhiều pha hơn. Đầu chương sau dễ hơn đỉnh chương trước khoảng 25 % đe dọa (răng cưa, `02 §5.4`). Thú Vương từ chương 4 có thêm cơ chế gõ lấy từ bảng 12 cơ chế của `02 §4.2`, như Khiên chuỗi, Hỏi nghĩa, Nghe.
- **Chơi lại:** sao từng trận. **Triều Vô Tận** (tắt bộ điều nhịp, bảng riêng). **Triều Ngày** (seed theo ngày). **Đại Thú Triều tuần** cho đội 3 người hoặc Thất Tinh 7 người (sau MVP).

### 4.10 Thắng, thua, thưởng

- **Thắng:** hết đợt cuối (và hạ Thú Vương nếu có) khi Trận Lực > 0. **Sao:** Trận Lực ≥ 70 % được ★★★, ≥ 40 % ★★, > 0 ★.
- **Thua:** Trận Lực về 0. Màn thua có gợi ý dựa trên số đo (BALANCE §4.3) và nút chơi lại.
- **Rút lui** (ý từ nút "Trốn" trong [video]): giữ 50 % nguyên liệu đã nhặt. Không được sao, không được vật phẩm đột phá.

| Thưởng | Khi nào | Dùng vào | Ghi chú |
|---|---|---|---|
| Trận Nguyên | Trong trận | Cơ quan | Về 0 khi hết trận |
| Linh Thạch | Kết trận, theo sao và số thú | Cửa hàng tông môn | Mảng kinh tế chốt giá |
| Yêu Đan (theo họ, hệ, phẩm) | Tinh thú, tướng, Vương, Thu Hồn | Pet, luyện đan/khí, tu luyện | Mảng pet và tu luyện chốt cách dùng |
| Nguyên liệu vùng | Rơi trên đất, tự hút r 3 m | Kỹ nghệ | Cuối trận tự gom phần còn lại (Codex §1.7) |
| Tàn trang công pháp | Hạ Vương lần đầu, 3 sao | Học kỹ năng, mở dòng kỹ năng | |
| Tri Thức, Sổ Từ | Theo việc học | Thư viện | Lõi học chung |
| Công Huân | Đội, theo đóng góp đúng vai | Cửa hàng đội | Không thưởng theo đòn kết liễu (Codex §22.3) |

### 4.11 MVP và sau MVP

| MVP (solo, Typing) | Sau MVP |
|---|---|
| 1 ải Thanh Thạch, camera cố định, 2 cổng + đường trời, 2 Trận Trụ, 6 ô cơ quan | Nhiều ải, sân lớn có camera theo người, hang thú trồi giữa sân |
| Trận Tâm, Kết Giới, Tâm nhãn, Trận Ý, Hợp Trận solo, chiếm nhãn | Lưỡng Nghi, Tam Tài có bot (M1), đội online 2–3 (M2), Thất Tinh (M4+) |
| Kiếm tu 5 ô + Kết Ấn, đánh nền, trọng thương | Lớp support, ngự thú, trận sư; pet; 24 trường phái (Codex §11) |
| 5 họ thú, 3 thuộc tính tinh anh, Lang Đầu Đàn, Thiết Bối Lang Vương | 12 thuộc tính tinh anh, thú tướng có hào quang, Vương nhiều cơ chế gõ |
| 4 cơ quan, Trận Nguyên, cửa hàng lúc nghỉ | Từ kích hoạt cơ quan, cộng hưởng, thẻ Cơ Duyên chọn 1 trong 3 lúc nghỉ |
| Trận mẫu 10 đợt + 2 trận dạy 5 đợt | Chương 8 trận, luật ải, Vô Tận, Triều Ngày, Đại Thú Triều tuần |
| Học trước, Thẻ Ôn, sự kiện học, Hồ sơ gõ | Voice/Hybrid (M1), Hỏi nghĩa, Nghe trên Vương |
| `kit/balance` trong sim, bot, cổng B1–B9, golden, kịch bản trình duyệt | Truy kích Vương bỏ chạy (Codex §4), Đa Tuyến (Codex §7) |

## 5. Solo và đội

| Hình thức | Ghế | Trận | Phiên bản trận | Máu thú (hệ số thử) | Trận Lực |
|---|---|---|---|---|---|
| Solo thuần | 1 | Đơn trận (Tâm nhãn) | S1 | ×1,0 | 1.000 |
| Solo + 2 bot | 3 | Tam Tài | T3 | ×2,4 | 1.800 |
| Đội 2 người | 2 | Lưỡng Nghi | T2 | ×1,7 | 1.400 |
| Đội 2 người + 1 bot, hoặc đội 3 người | 3 | Tam Tài | T3 | ×2,4 | 1.800 |
| Thất Tinh (sự kiện) | 7 | Thất Tinh | T7 | ×5,0 | 3.500 |

- **Khóa phiên bản trận lúc vào** theo số ghế. Bot lấp ghế trống trước trận. Không sinh thêm bot giữa đợt. Người rớt mạng: giữ chỗ 20 s, rồi bot nhận thay ở biên một hành động. Máu thú không co giãn giữa trận (Codex §15).
- Hệ số ×2,4 cho 3 ghế (không phải ×3) vì đòn vùng chồng nhau và cần phối hợp. Bot đo lại từng phiên bản.
- **Từ của ai người nấy gõ.** Không có cuộc đua gõ cùng một từ. Mục tiêu tự chọn có thể trùng, nhưng sát thương thừa không tính vào đóng góp. Loot chia riêng cho từng người.
- **Hợp Trận khi chơi đội** (nạp không đồng bộ, Codex §14.4): mỗi nhãn tự nạp Trận Ý. Khi ≥ 2/3 nhãn đầy (Tam Tài), mỗi người nhận Kết Ấn 2 từ của riêng mình, gõ trong 8 s. Sức Hợp Trận = 40 % + 20 % cho mỗi người gõ xong. Người chậm làm Hợp Trận yếu đi, không hủy nó.
- **Từ Ấn khi chơi đội:** mỗi người thấy một từ Ấn của riêng mình. Mỗi Ấn giảm 35 / √(số ghế) Thế, để đội không khóa boss quá dễ. Sau phá thế có 15 s kháng.
- **Công bằng khi tốc gõ lệch nhau:**
  - Độ dài từ theo E của từng người (`kit/typing/config`). Hồi chiêu như nhau.
  - Nhịp k của trận lấy theo E_eff trung vị của đội, kẹp trong [0,85; 1,15].
  - Nhãn Thủ và nhãn Dưỡng ít phụ thuộc tốc gõ, hợp với người chậm. Ai giữ nhãn nào thì chọn ở Bày trận.
  - Màn kết trận hiện đóng góp theo vai: sát thương, khiên đã đỡ, hồi, Thế đã phá, Trận Ý đã nạp. Không có bảng xếp hạng sát thương.
  - Thưởng nền như nhau cho mọi người hoàn thành. Thưởng theo vai tối đa +10 %.
- **Bot:** dùng hồ sơ Chuẩn của `kit/balance/typist.ts`, giữ đúng vai, không phản ứng 0 giây. Bot không tạo sự kiện học, không có túi loot riêng (Codex §15).
- **Mạng (sau MVP), theo luật chỉ dùng Cloudflare Free:** sim tất định 60 Hz (như Rồng Giữ Ải), nên chỉ cần **chuyển tiếp lệnh** (lockstep). Một Durable Object mỗi phòng nhận lệnh của từng tick, gom 10 lần mỗi giây, gửi lại cho mọi máy. Mỗi 600 tick các máy so mã băm. Ước lượng: một trận 3 người 8 phút ≈ 14.400 tin WebSocket. Nếu tin vào được tính 20 tin = 1 request thì là ≈ 720 request. Nằm trong hạn mức miễn phí 100.000 request/ngày và 13.000 GB-s/ngày của DO, **[trí nhớ], phải kiểm lại trên trang giá Cloudflare**. Không cần server tính sim.

## 6. Gắn với học tiếng Anh

| Từ | Ở đâu | Lúc nào | Luật |
|---|---|---|---|
| Từ mới (8 mỗi trận) | Ô Kiếm Khí, ô Hộ Thể | Đợt 1–4 và lúc lặng | Không đặt từ mới lên Ấn, Tẩy hay Kết Ấn. Từ mới ghim ≥ 2,5 s trong khung học (Rồng Giữ Ải M0a đo được 2.637 ms) |
| Từ đang học, từ ôn | Mọi ô | Cả trận | Đổi từ sau mỗi lần dùng, theo lịch ôn của lõi học |
| Từ Ấn | Tinh thú, tướng, Vương | Lúc nạp đại chiêu | Chỉ từ đã thuộc, D2–D3. Không trùng chữ đầu với từ đang sống |
| Từ Tẩy | Nhãn bị chiếm | Khi bị chiếm | D1–D2, đã thuộc |
| Kết Ấn | Ô 6 | Trận Ý đầy | Chuỗi chủ đề 2 từ (luật D5 của `dragon-lane`), không gấp: 8 s |
| Thu Hồn | Vương < 5 % | Cuối trận | Từ chủ đề của chương, D4. Trượt không bị phạt |
| Thẻ Ôn | Lúc nghỉ | Mỗi lần nghỉ, tùy chọn | Hỏi nghĩa hoặc nghe. Đồng hồ trận dừng. +Trận Nguyên nhỏ. Lớp chữ chiến đấu ẩn khi thẻ mở (sửa lỗi lộ đáp án của Rồng Giữ Ải M0a) |
| Học trước, Sổ Từ | Trước và sau trận | | Một sự kiện học có chấm cho mỗi từ mỗi trận, `gameId` của game mới (`kit/learning`) |

- **Chống quá tải:** tối đa **9 từ sống** cùng lúc (6 ô + ≤ 2 Ấn + ≤ 1 Tẩy hoặc Thu Hồn). Chữ đầu khác nhau, không từ nào là tiền tố của từ khác. Mỗi trận chỉ dạy một ý mới. Không bao giờ đồng thời bắt né vị trí, gõ Ấn và gõ Tẩy (Codex §16.2).
- **Cửa sổ cho từ gấp** (sửa Codex §16.1): T = đọc 0,4 s + nhận từ (đã thuộc 0,35–0,6 s) + 12 × (ℓ + 1) / (E × 0,86) + hoạt ảnh 0,2 s + trễ kênh, nhân biên 1,6. Thời gian nạp của Thiết Bối Xung (3 s ở 35 WPM, từ D3) phải ≥ T. Ở 25 WPM, k giãn tương ứng.
- **Voice/Hybrid:** đi chung giao dịch hành động (Codex §1.4). Trễ kênh cho Voice tạm cộng 0,6–1,0 s, đo khi có runtime. Kết quả ASR đến muộn không bắn vào Ấn đã hết. Âm phát âm của game không được kích hoạt chiêu. MVP chỉ có Typing; M1 thêm Voice dựa trên kinh nghiệm runtime của Space Typing.
- **Gõ chuẩn thắng gõ ẩu:** cách chấm Chớp / Hoàn hảo / Tốt / Vừa / Ẩu nhân sát thương ×1,25 / 1,10 / 1,00 / 0,90 / 0,60 (`dragon-lane/00 §4.2`). Không có chí mạng ngẫu nhiên từ gõ. Dòng kỹ năng mở theo số từ dùng **đúng** (ý từ [video] t120).

## 7. Tái sử dụng và chi phí

### 7.1 Game mới hay mode của Rồng Giữ Ải

| | Rồng Giữ Ải | Lời Gọi | Tuyến Cuối | **Thú triều tu tiên** |
|---|---|---|---|---|
| Gõ vào đâu | Từ trên mỗi quái | Lời gọi của nhà và dân | Từ nạp súng | Ô kỹ năng + Ấn trên tinh thú |
| Nhân vật | Rồng đứng yên giữa bệ | Tướng và Trợ Thủ tự đi | Bến súng cố định | **Đi tự do**, ra vào trận |
| Hình | 3D Tripo, three.js | Canvas 2D | three.js | 2D có chiều sâu (Codex §26) |
| Đội | Không | Không | Không | 1–3 người, 7 là sự kiện |
| Ngoài trận | Làng Rồng | Làng | Trạm Mẹ | Tông môn, tu luyện, pet |

**Đề xuất: làm game mới** (repo con riêng, ví dụ `games/tu-tien`, cổng 3008, theo `SPLIT_PLAN.md` §3 và §9–10). Lý do:

1. Cách điều khiển khác hẳn.
2. Giọng và hình khác: Rồng Giữ Ải là rừng ấm, cho trẻ em.
3. Cần mạng cho đội.
4. Phần ngoài trận khác.
5. Rồng Giữ Ải M0a còn trượt cổng B1/B7; ghép thêm mode vào sẽ làm chậm cả hai.

Phần sim thì gần như giống nhau, nên **chép** module của Rồng Giữ Ải (mỗi file ghi `// Source: …`, luật của `games/dragon-hold/AGENTS.md`). Khi cả hai game cùng dùng ổn định, mới đưa phần chung (đợt, sinh quái, hào quang, báo trước, cơ quan) lên `shared/game-kit/defense`. Kit chỉ chứa thứ ≥ 2 game dùng.

### 7.2 Dùng lại cụ thể

| Thứ | Đường dẫn | Dùng để |
|---|---|---|
| Gõ | `shared/game-kit/typing/{router,letters,picker,scorer,session,tempo,budget,config,decks}.ts` | Định tuyến từ của ô, Ấn, Tẩy; chữ đầu khác nhau; chấm; ngân sách chữ |
| Cân bằng | `shared/game-kit/balance/{profile,flow,director,pace,typist,gates,bands}.ts` | Hồ sơ 13 yếu tố, FlowMeter, bộ điều nhịp, bot gõ giống người, cổng B1–B9 |
| Học, nhập, phát âm | `shared/game-kit/{learning,input,speech,vocab}/` | Sự kiện học, phím, từ vựng, phát âm |
| Phản hồi, âm, nền | `shared/game-kit/{feedback,audio,platform,three,ui}/` | Dừng hình, số sát thương, rung; bus âm; RNG, vòng khung; nạp model |
| Sim thủ ải | `games/dragon-hold/src/sim/{waves,spawn,director,movement,boss,auras,traps,placement,shop,economy,status,combat,fixed,hash}.ts` | Luồng đợt, toán sinh, trần quái sống, báo trước, hào quang, bẫy thành cơ quan, kinh tế, số nguyên tất định |
| Công cụ kiểm | `games/dragon-hold/scripts/balance/`, `tests/golden`, `scripts/visual/scenarios/dh-{telegraphs,placement,focus,keyboard-only,learning-frame}.mjs` | Ma trận bot, mã băm, kịch bản trình duyệt |
| Thiết kế thủ ải | `docs/games/dragon-lane/02-enemies-generals-bosses.md` §1–5, `03-our-side-shop-traps-support.md` §0.3, `00-canon.md` | Bậc, W, báo trước, tướng, 12 cơ chế gõ của boss, khắc chế, ngân sách chữ |
| Lời Gọi | `games/typing-defense/src/view/{debug-2d,fx-2d,boss-2d}.ts`, `src/ui/profile.ts`; TK §0.2 luật 8 | Vẽ 2D, kho hạt cố định, đỉnh boss, Hồ sơ gõ; gõ trực tiếp lên quái chỉ để phá cơ chế |
| Tuyến Cuối | `games/typing-survival/src/sim/{pace,plan,hazards}.ts`, `src/content/threat.ts`, `src/view/crowd.ts`; `docs/SURVIVAL_MODE_PLAN.md` §4.0 | Luật ải, chấm đe dọa cho bot và thẻ đợt, đám đông, cấu trúc chương |
| Space Typing | `games/space-typing/server/duel/ws-server.ts`, `cloud/src/chat.ts`, `cloud/wrangler.jsonc`; skill `voice-typing-runtime` | Phòng thời gian thực, mẫu Durable Object, Voice/Hybrid |
| Âm | `docs/games/AUDIO_PIPELINE.md`, `tools/audio-lab/DECISIONS.md` Q6 | Âm đúng hình và cỡ của hành động, CC0 thu âm thật |

### 7.3 Chi phí ước lượng

S là vài ngày cho một làn agent. M là 1–2 tuần. L là hơn 2 tuần, hoặc cần nhiều giờ của chủ dự án.

| Hạng mục | Cỡ | Ghi chú |
|---|---|---|
| Khung repo, kit sync, portal, nginx | S | Theo mẫu tách ba game |
| Sim đợt, sinh quái, điều nhịp, kinh tế, cơ quan (chép và sửa) | M | Thay làn bằng trường hướng |
| Người chơi đi tự do, va chạm, click-to-move trên lưới nhỏ | M | Mới hoàn toàn |
| Ô kỹ năng, đánh nền, nhắm mục tiêu, Ấn, Tẩy | M | Router của kit có sẵn |
| Trận Tâm, Kết Giới, nhãn, Trận Ý, Hợp Trận | M | |
| Thú Vương có Thế và pha | M | Theo mẫu `boss.ts` |
| Bot di chuyển + gõ, báo cáo, cổng | M | `typist` có sẵn; thiếu chính sách di chuyển |
| Hình 2D có chiều sâu: cảnh, nhân vật, 5 họ, Vương, cơ quan, VFX mực | **L** | Chủ dự án tham gia. Mảng mỹ thuật chốt cách làm |
| Âm thu thật CC0, nhạc | M | Theo Audio Lab |
| Bot Tam Tài (M1) | M | |
| Đội online lockstep trên Durable Object (M2) | **L** | Đồng bộ, mất kết nối, kiểm mã băm |
| Thất Tinh, nhiều chương | L | Sau cùng |

## 8. Rủi ro và câu hỏi cho chủ dự án

### 8.1 Rủi ro

| Rủi ro | Giảm bằng |
|---|---|
| Ô luôn có từ nên người chơi gõ dồn Kiếm Khí mà không cần nghĩ | Mục tiêu tự chọn ưu tiên thú gần Trận Tâm; ô hồi chiêu mạnh hơn hẳn; Ấn và chiếm nhãn bắt phải chọn. Đo "chiến thuật Tốt hơn Kém ≥ 10 điểm %" (B6) |
| Quá dễ: lặp lại lỗi Rồng Giữ Ải M0a (mọi bot thắng 100 % ở vòng đầu) | Áp lực liên tục, đường ngắn, bộ điều nhịp, cổng B1/B2 ngay từ hộp xám |
| Quá tải chú ý khi vừa đi, vừa gõ, vừa đọc báo trước, lại chơi đội | Trần 9 từ, 2 cơ chế, 1 Ấn; mũi tên và click-to-move; theo dõi Ngộp O |
| Đông sprite cộng VFX làm tụt khung hình | Bench 50/100/200/300 thú trước khi vẽ hàng loạt (Codex §26.8); trần 60 thú sống ở MVP |
| Nhiều hướng × nhiều clip làm nổ khối lượng vẽ; chủ dự án không chấp nhận chuyển động cứng | Thú 4 hướng có lật gương. Cân nhắc dựng sprite từ model Tripo bằng Blender (quy trình anh đang dùng) |
| Mạng đội phức tạp, hạn mức Free | Lockstep chỉ chuyển lệnh; làm sau MVP solo; kiểm hạn mức trước M2 |
| Phình phạm vi: tu luyện, pet, 24 trường phái | MVP chỉ 1 lớp, solo. Mảng khác nối qua phần thưởng |
| Giống QCBH | Thế giới, tên, hình, HUD riêng; vệt mực thay máu; không phụ bản nhiều phòng |

### 8.2 Câu hỏi (mỗi câu có phương án đề xuất)

| # | Câu hỏi | Đề xuất |
|---|---|---|
| 1 | Làm game mới hay mode của Rồng Giữ Ải? | **Game mới**, chép sim của Rồng Giữ Ải, dùng kit chung (§7.1) |
| 2 | Gõ vào ô kỹ năng (Codex) hay gõ từ trên từng con thú (Rồng Giữ Ải)? | **Ô kỹ năng + đánh nền**, chỉ tinh thú, tướng, Vương mang Ấn |
| 3 | Vật được giữ là một Trận Lực chung, nhãn không có máu nhưng có thể bị chiếm? | **Có** (Codex §14.3) |
| 4 | Người chơi gục thì thua ngay, hay nằm 8 s rồi hồi sinh, chỉ thua khi Trận Lực về 0? | **Hồi sinh sau 8 s**, Trận Lực −5 % |
| 5 | Độ dài trận: thường 5–6 đợt (5–7 phút), Đại Triều 10 đợt + Vương (~12 phút)? | **Có**. Trận mẫu §4.8 dùng làm bản thử đầu |
| 6 | Thứ tự: solo → bot bù ghế → đội online 2–3 → Thất Tinh là sự kiện tuần? | **Có** |
| 7 | Trúng đòn là vệt mực, không có máu? | **Có**: hợp thủy mặc, hợp mọi lứa tuổi |
| 8 | MVP chỉ Typing, Voice/Hybrid ở M1? | **Có**. Kiến trúc giao dịch hành động làm đúng từ đầu |
| 9 | Mạng đội: lockstep chuyển lệnh qua Durable Object trên gói Free? | **Có**. Kiểm hạn mức trước M2 |
| 10 | Vẽ 2D bằng three.js (camera nghiêng, sprite atlas, dùng lại view của Rồng Giữ Ải và Tuyến Cuối) hay PixiJS / Canvas 2D (như Lời Gọi)? | **three.js**, không thêm thư viện mới. Chờ mảng mỹ thuật và hiệu năng chốt sau bench |
| 11 | Rút lui giữ 50 % nguyên liệu, không sao, không vật phẩm đột phá? | **Có** |
| 12 | Thế giới "Biên Ải" và Thú Vương tự thiết kế, không dùng danh sách thú của QCBH? | **Có**. Thần thoại chung được dùng nếu diễn giải hình riêng |
| 13 | Hạ Thú Vương cuối chương là điều kiện đột phá cảnh giới? | **Có**, nhưng phải có đường lấy chắc chắn (Codex §10.3). Mảng tu luyện chốt |
