# Tu Tiên Thủ Ải: 04. Vật phẩm, kinh tế, cửa hàng

Ngày 24/10/2026. Đây là bản phân tích đề xuất, chưa phải luật đã chốt. **Mọi con số đều là số thử** cho tới khi bot và người thật chơi kiểm.
Phạm vi: tiền tệ, những gì rơi trong thú triều, mua gì giữa hai đợt và mua gì giữa hai lần chơi, đan và phù, pháp bảo và trang bị, chế tạo, sơn môn ngoài ải, chống cày, loot khi chơi đội.
Các mảng khác (combat, trận pháp, tu luyện, quái) do tài liệu phân tích khác lo. Tài liệu này chỉ nói phần **giá, nguồn thu, phần thưởng và vật phẩm** của các mảng đó.

Đã đọc: Codex V2.2 (`TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md` §0, §1.7, §9–§15, §19–§22, §25, §27), video QCBH của chủ dự án (khung `t000`–`t256`), Rồng Giữ Ải `docs/games/dragon-lane/00-canon.md` §4.9, `03` §3–§6 và §12, `04` §8–§10, mã `games/dragon-hold/src/sim/economy.ts` và `shop.ts`, Lời Gọi `games/space-typing/docs/td/TYPING_DEFENSE_DESIGN.md` §15–§17, Tuyến Cuối `SURVIVAL_MODE_PLAN.md` §4.0d, skill `progression-economy` và báo cáo review `games/space-typing/docs/changelog/2026-10-21-code-review.md` #23.

Ký hiệu nguồn: **[video tNNN]** là khung ở giây NNN của video chủ dự án quay. **[Codex §x]** là tài liệu V2.2. **[web: url]** là trang web đã đọc. **[trí nhớ]** là hiểu biết sẵn có, chưa kiểm.

## 1. Tóm tắt

- **Ba loại tiền, không hơn.** **Linh Sa** chỉ dùng trong ải và mất khi hết ải. **Văn Khí** giữ mãi và chỉ đến từ việc học. **Thú Hạch** giữ mãi và đến từ chiến thắng, boss. Đây là khung ba tiền Vàng / Tri Thức / Vảy Rồng đã chốt ở Rồng Giữ Ải, chỉ đổi tên và bối cảnh.
- **Linh Sa theo ngân sách ải**, không theo số đầu thú. Linh Sa ghi sổ ngay tick thú chết. Kinh tế chặt: không bao giờ mua đủ mọi thứ, mỗi lần mua là một quyết định. Bầy đông cuối game không làm ngập tiền.
- **Mua theo thời điểm.** Trước ải chọn Hành Nang (bộ món mang theo). Nghỉ đợt mua đủ thứ ở Trận Phường. Trong đợt chỉ dùng đan, phù bằng phím tắt hoặc chuột. Ngoài ải nâng pháp bảo, mở công thức, mở ô.
- **Đan và phù trong trận không cần gõ.** Dùng bằng Alt+1/2/3 hoặc click, hồi chung 8 s. Gõ là việc của kỹ năng. Bắt gõ đúng lúc nguy cấp sẽ phạt đúng người gõ chậm. Phần học gắn vào Thẻ Ôn, khóa chữ Bảo Hạp và Linh Mạch, mọi chỗ đều tùy chọn.
- **Chế tạo tối thiểu.** Bản đầu không có túi vật liệu, không có phẩm vật liệu, không gộp 5 thành 1. Nhãn đồ rơi kiểu QCBH chỉ để tạo cảm giác, tự quy ra tiền. Sau MVP có **Đan Lô**: một bài nhớ nghĩa, nâng phẩm công thức đan vĩnh viễn, không sinh kho đan để tích trữ.
- **Trang bị cố định ở bản đầu.** Pháp bảo bản mệnh, Hộ Thân Y và Ngọc Bội, mỗi phái 2 món cho mỗi ô. Không độ hiếm, không dòng phụ ngẫu nhiên, nâng cấp 1–5 bằng Thú Hạch.
- **Đội công bằng.** Mỗi người có ví riêng. Linh Sa chia đều theo ghế, không theo đòn kết liễu. Bảo Hạp tách riêng cho từng người. Bot có ví để xây phần ghế của nó nhưng không đổi ra tiền ngoài ải. Khi online, server quyết loot và kết toán đúng một lần mỗi ván.
- **Chống cày.** Đường chính không cần chơi lại. Chơi lại nhận 30 %. Văn Khí có trần mềm theo ngày. Không thể lực, không gacha, không bán sức mạnh. Tài khoản nâng hết chỉ mạnh hơn bộ đồ trung bình tối đa 25 %.

## 2. QCBH làm thế nào (chỉ phần đáng học)

| Hệ | Quan sát | Nguồn | Bài học cho game mình |
|---|---|---|---|
| Tiền tệ | Màn bản đồ có ba số cạnh ba biểu tượng: tinh thể xanh 448, đồng tiền 214, thẻ 9. Nghĩa của hai số sau chưa xác định | [video t008] | Ít tiền hiện trên HUD là dễ đọc |
| Linh thạch là tiền chính | Có thành tựu "sở hữu 1.000 linh thạch" và "sở hữu 100 điểm cống hiến". Có thiên phú rút tu vi mỗi lần tiêu linh thạch | [web: https://vandal.elespanol.com/logros/pc/tale-of-immortal/105448], [web: https://www.18183.com/ggbh/202103/3322148.html] | Tiền tông môn (cống hiến) là tiền thứ hai. Game mình không cần |
| Thị trấn, dịch vụ | Phường Thị, Công Xưởng, Treo Thưởng Bảng, Tửu Quán, Khách Sạn, Truyền Tống Trận | [video t008] | Một hub ít nhà, mỗi nhà một việc. Lấy ý "bảng truy nã" cho việc ngày (sau MVP) |
| Túi đồ | 7 tab: Toàn bộ, Đan phù, Thư tịch, Trang bị, Vật liệu, Đạo cụ, Đặc thù. Lưới ô rất lớn | [video t000, t004] | Túi rộng là gánh quản lý kho. Game học không nên có |
| Trang bị | 3 ô: nhẫn, tọa kỵ, phục sức. Pháp Bảo và Khí Linh là hai mục riêng | [video t004] | Ít ô trang bị, pháp bảo là trung tâm bản sắc |
| Vật phẩm mang vào trận | 5 ô đạo cụ, chỉ chứa đan dược và pháp bảo, mỗi ô tối đa 5 đan. Tổng mang theo bị giới hạn bởi Niệm lực (thanh 99/242) | [video t004, chú thích trên màn] | Ô có hạn và số mỗi ô có hạn là đủ. Bỏ lớp "trần theo chỉ số" để khỏi thêm một chỉ số |
| HUD trận | Dải 5 ô phím 1–5 có số lượng (2/5/5/5/1), ô thứ 5 là pháp bảo. Hai ô đan cùng hiện số 17 sau khi dùng | [video t124, t160] | Có vẻ là hồi chung theo nhóm đan (suy luận từ hình). Giữ dải ô có số đếm và hồi chung |
| Rơi đồ | Nhãn tên nằm trên đất, màu theo phẩm: trắng cho hạ phẩm, xanh lá cho trung phẩm và thảo dược. Có đá, linh thạch, thảo dược, gỗ, mảnh vũ khí của quái. Có vò sành đập được | [video t124, t180, t060] | Màu phẩm dễ đọc, nhãn tên tạo cảm giác "giàu". Nhưng chữ nhãn tranh chỗ với chữ trên quái của game mình |
| Kết trận | Cuộn "Chiến đấu kết thúc · Thu hoạch được đạo cụ". Phòng dọn xong có cột sáng sang phòng sau, nút "Trốn" đổi thành "Rời" | [video t256, t200] | Màn tổng kết thu hoạch là khoảnh khắc thưởng. Giữ |
| Nghề phụ | 6 kỹ nghệ có điểm: Luyện đan 37, Luyện khí 47, Phong thủy 34, Họa phù 14, Dược liệu 17, Khoáng thạch 39 | [video t004] | Sáu nghề là cả một game phụ. Quá rộng cho game thủ ải |
| Tăng nghề, vật liệu | Bản cũ: điểm nghề lên nhờ sách nghề do boss định kỳ rơi. Vật liệu kỹ năng có phẩm, gộp 5 phẩm thấp thành 1 phẩm cao (1 G1 cần 25 G3), người viết gọi là "đắt khủng khiếp". Vật liệu pháp bảo có "tạp chất" | [web: https://kosgames.com/?p=5884] (hướng dẫn cũ) | Gộp phẩm là vòng cày thuần. Không lấy |
| Luyện pháp bảo | Tự luyện pháp bảo, triệu khí linh, luyện đan, họa phù, phong thủy | [web: https://www.instant-gaming.com/en/8227-buy-gui-gu-ba-huang-tale-of-immortal-pc-game-steam/] | Pháp bảo có "hồn" là chất tu tiên. Ở game mình: khí linh làm ngoại hình hoặc lời thoại, không thêm chỉ số |
| Vật phẩm làm đòn bẩy xã hội | NPC đòi bí tịch, chọn "Cho hắn" hoặc "Không cho" | [video t088] | Ngoài phạm vi thủ ải. Bỏ |
| Thú triều tấn công thành | Có sự kiện thú triều đánh thành ở thế giới mở | [trí nhớ], tìm web không ra nguồn | Không dựa vào chi tiết này |
| Đan dược | Có thiên phú làm đan đã uống bị đẩy ra trong 10 s để nhặt dùng lại | [web: https://www.18183.com/ggbh/202103/3322148.html] | Đan có thể có biến tấu theo nội tại. Để sau |

**Rút ra:** QCBH mạnh ở cảm giác "nhặt được nhiều thứ có tên" và ở dải ô đan có số đếm. Nó yếu (với mục tiêu của mình) ở chỗ kho đồ mênh mông, sáu nghề và vòng gộp phẩm. Game mình giữ cảm giác, bỏ khâu quản lý kho.

## 3. Codex V2.2 nói gì về mảng này

| § | Codex nói | Giữ / Sửa / Bỏ | Lý do |
|---|---|---|---|
| §0 | Không xây thành, bang hội, đấu giá, mô phỏng NPC phức tạp | **Giữ** | Không có chợ giữa người chơi, không đấu giá |
| §1.7 | Tiền và nguyên liệu thường tự hút trong bán kính gần. Sau trận gom phần còn lại. Đồ đặc biệt đánh dấu, tới gần tương tác. Bí mật tùy chọn. Loot cá nhân. Nhặt chỉ chốt một lần. Bot không sinh túi | **Giữ, sửa một điểm** | Sửa "gom sau trận" thành **ghi sổ ngay tick thú chết** (Lời Gọi §17.4). Hình đồng bay chỉ là hình, không bao giờ mất tiền vì hình |
| §10.3 | Mảnh ghép thiết yếu có đường nhận chắc chắn, không giấu sau đồ hiếm | **Giữ** | Pháp bảo, công thức, ô đều mở theo lịch hoặc theo boss |
| §10.5 | Thưởng bí mật là lựa chọn thêm. Đồ thường thu dọn tránh chênh thu nhập chỉ do phải chạy nhặt | **Giữ, thêm trần** | Linh Mạch và Bảo Hạp lấy từ quỹ "khác" 15 %, nên người đứng trận và người chạy chênh nhau tối đa khoảng 8 % Linh Sa |
| §11 | Phái Đan: đan công kích không cần thuộc recipe | **Sửa (ghi chú)** | Tách "Đan tu" (lớp nhân vật) khỏi "đan tiêu hao" (vật phẩm). Hai thứ không dùng chung kho, không dùng chung tiền |
| §11.2, §13.1 | Trang phục, ngoại hình pet không thêm sức mạnh mua ngoài. Tiến hóa pet dùng vật liệu có đường nhận chắc chắn | **Giữ** | Vật liệu pet tính bằng Thú Hạch, không thêm loại tiền |
| §13.3 | Pet không nhân suất buff hay loot | **Giữ** | Pet nhặt hộ Linh Sa trong vùng, nhưng không tạo thêm Bảo Hạp |
| §14.3 | Người đi nhặt đồ không sinh thêm bot vào chỗ họ | **Giữ** | |
| §15 | Bot không có túi loot riêng chuyển cho người thật. Không khóa vật liệu cốt lõi khỏi người chơi solo | **Giữ, sửa một điểm** | Bot **có ví Linh Sa trong ải** để xây phần ghế của nó. Ví đó không đổi ra tiền ngoài ải, không chuyển cho người |
| §19.2 | Không tạo sáu loại tiền và shop cho sáu minigame | **Giữ, nâng thành luật** | Trần cứng: 3 loại tiền. Muốn thêm tiền mới phải bỏ một loại cũ |
| §21 | Trần chỉ số: hồi chiêu giảm tối đa 30 %, chí mạng có trần | **Giữ** | Đan, phù, pháp bảo đều tính vào các trần này |
| §21.1 | Mỗi nhánh có ít nhất hai hướng đồ. Đồ hỗ trợ tăng bảo hộ. Bộ cơ bản nhận chắc chắn, không cần roll hoàn hảo. Ngoại trang tách sức mạnh | **Giữ, sửa** | Bản đầu dùng **trang bị cố định**, không roll gì cả (như quyết định D08 của Rồng Giữ Ải) |
| §22.3 | Thưởng phổ thông dựa trên hoàn thành và tham gia hữu ích, tránh last-hit | **Giữ** | Áp thẳng vào cách chia Linh Sa trong đội (mục 5) |
| §25.4, RV15, RV33 | Bot nhân loot. Người đứng trận mất đồ, người chạy giành hết | **Giữ làm ca kiểm** | Thành cổng kiểm E5, E6 ở mục 4.10 |
| §27 P4, P6 | Loot cá nhân khi chơi cùng bot. Đồng bộ loot khi co-op người thật | **Giữ, sửa** | Online: server quyết rơi đồ và kết toán (bài học #23 của Space: client tự in tiền) |
| (chưa có) | Codex chưa nêu tên tiền, giá, cửa hàng giữa đợt, đan trong trận, chế tạo | **Bổ sung** | Mục 4 dưới đây |

## 4. Đề xuất cho game chống ải thú triều

### 4.1 Mười luật khóa
1. **Ba tiền:** Linh Sa (trong ải), Văn Khí (học), Thú Hạch (thắng). Không tiền thật, không gacha, không hộp ngẫu nhiên trả phí.
2. **Linh Sa theo ngân sách ải**, chia 60 % hạ thú, 25 % hết đợt, 15 % học và khám phá. Không lãi suất, không nhà sinh tiền vô hạn.
3. **Giá trong ải không đổi** theo chương. Sức phe ta tăng theo đường chuẩn của chương (g(c), như Rồng Giữ Ải 00 §4.1). Người chơi mạnh thêm nhờ pháp bảo, Thư Lâu và cảnh giới.
4. **Mua chỉ lúc chuẩn bị và lúc nghỉ đợt.** Trong đợt chỉ dùng đồ đã có. Không mở bảng lớn khi thú đang tràn.
5. **Không gõ để mua, đặt, nâng.** Gõ để đánh, để học và để mở thưởng tùy chọn.
6. **Không túi vật liệu ở bản đầu.** Mọi đồ rơi có tên đều tự quy ra Linh Sa hoặc Thú Hạch.
7. **Trang bị cố định:** món nào làm gì đọc được ngay, giá tính được, không reroll.
8. **Ghi sổ ngay tick xảy ra.** Hình chỉ là hình. Nhặt một món chỉ chốt một lần.
9. **Loot cá nhân, ví cá nhân** trong đội. Bot không tạo thưởng ngoài ải.
10. **Đường chính không cần cày.** Bot dùng "bộ đồ trung bình" (đi một lần, không chơi lại) vẫn phải qua được mọi ải.

### 4.2 Ba tiền tệ (số thử)

| Tiền | Ở đâu | Nguồn | Dùng cho |
|---|---|---|---|
| **Linh Sa**: cát linh khí, thú tan ra thành cát | Trong ải, mất khi hết ải | Ngân sách ải: hạ thú 60 %, hết đợt 25 %, khác 15 % (Học trước, Thẻ Ôn, Bảo Hạp, Linh Mạch, gọi đợt sớm) | Trận kỳ, cơ quan phòng thủ, nâng cấp, sửa, đan, phù, bùa thân (+máu, +giáp trong ải) |
| **Văn Khí**: khí của chữ nghĩa | Ngoài ải, giữ mãi | **Chỉ từ học:** từ mới gõ đúng lần đầu +1, từ đến hạn ôn đúng +1, Thẻ Ôn đúng +1, Huy hiệu Học +5, Ải Ôn ×2 | Thư Lâu: ô đan thứ 3, ô Hành Nang, Linh Sa đầu ải, công thức đan và phù mới, thi lên cấp từ |
| **Thú Hạch**: lõi thú vương rơi khi hạ boss | Ngoài ải, giữ mãi | Sao lần đầu 3 / 5 / 8, boss chương +20, ải tinh anh +5, chơi lại 30 %, thua giữ 30 %, Linh Sa dư đổi tối đa 3 | Mở và nâng pháp bảo, trang bị. Cấp trận kỳ, cơ quan 1–5. Tiến hóa pet |

```text
Linh Sa ải = 200 (đầu ải; Thư Lâu ≤ +100) + 900 × f_hướng × f_loại          // thử, chép 00 §4.9 của Rồng Giữ Ải
f_hướng (số cửa thú triều tràn vào): 1 → 1,00 · 2 → 1,25 · 3 → 1,45 · 4 → 1,60
f_loại : ải dạy 0,6 · thường 1,0 · tinh anh 1,1 · ôn 0,6 · boss chương 1,2
Linh Sa dư cuối ải → Thú Hạch = min(3; floor(dư / 100))
Văn Khí: trần mềm 300 mỗi ngày, phần vượt × 0,25
Thư Lâu bậc k = 50 × 1,35^(k − 1) Văn Khí, 10 bậc, tổng ≈ 2.700
Pháp bảo: mở 40 Thú Hạch; cấp 2 / 3 / 4 / 5 = 30 / 50 / 80 / 120
Trận kỳ, cơ quan: cấp 2 / 3 / 4 / 5 = 10 / 20 / 35 / 55 Thú Hạch, mỗi cấp +6 % hiệu lực chính
```

- Đặt mục tiêu: Linh Sa chỉ đủ dựng 15–35 % mức tối đa của bản đồ. Người chơi luôn phải chọn giữ cửa nào bằng gì (cổng G13, G14 của Rồng Giữ Ải).
- Cảnh giới (tu vi) **không** là tiền và không tiêu được. Mảng tu luyện sở hữu nó. Mảng này chỉ yêu cầu: vật phẩm đột phá (nếu có) phát chắc chắn từ boss chương, không bán, không rơi ngẫu nhiên.

### 4.3 Vòng chơi: mua gì, lúc nào

| Lúc | Làm gì | Tiền | Ghi chú |
|---|---|---|---|
| Trước ải (Trận Đài) | Xem thẻ báo thú triều: cửa nào, họ thú nào, boss. Chọn Hành Nang 6 món (8 từ chương 2, tối đa 10). Đổi pháp bảo. **Học trước** từ mới của ải | Linh Sa (Học trước +5 mỗi từ, tối đa +40) | Món khắc chế thú của ải có viền sáng |
| Nghỉ đợt (Dễ: chờ Enter · Thường: 20 s · Khó: 15 s; đồng hồ dừng khi mở bảng) | Mua, đặt, nâng, bán trận kỳ và cơ quan. Mua đan, phù, bùa thân. **Thẻ Ôn** (tối đa 3 câu). Mở **khóa chữ Bảo Hạp** | Linh Sa | Bán hoàn 70 %, bán trong cùng lần nghỉ hoàn 100 %. Nâng cấp 2 = 70 % giá gốc, cấp 3 = 100 % |
| Trong đợt | Dùng đan, phù: Alt+1/2/3 hoặc click. Sửa cơ quan đổ. Linh Mạch (tùy chọn). Từ chương 6: **đặt nhanh** 1 món mỗi đợt, dựng 2 s | (đã mua) | Không nâng, không bán, không mở bảng lớn |
| Cuối ải | Cuộn **Thu Hoạch**: Linh Sa dư → Thú Hạch, Thú Hạch, Văn Khí, sao, từ đã học | — | Học và RPG báo **tách dòng** (Codex §17.1) |
| Ngoài ải (Sơn Môn) | Thư Lâu (Văn Khí), Bảo Khí Lò (Thú Hạch), Sổ Bảo Vật (xem mọi món, món chưa mở hiện bóng và nơi mở) | Văn Khí, Thú Hạch | Không có thời gian chờ xây |

### 4.4 Rơi đồ trong thú triều

| Bậc thú | Linh Sa (ghi ngay) | Hình cát bay | Bảo Hạp cá nhân | Khác |
|---|---|---|---|---|
| Bầy (mỗi con) | Theo phần đe dọa; cả cụm trả một lần khi con cuối chết | 1 hạt | — | — |
| Thường | Theo phần đe dọa | 1–2 hạt | — | — |
| Tinh anh | Theo phần đe dọa | 3 hạt và 1 hạt lớn | 100 %, hộp nhỏ | — |
| Thú tướng | Theo phần đe dọa | 6 hạt | Hộp vừa | — |
| Thú vương (boss) | Theo phần đe dọa | 10 hạt | Hộp lớn | **Thú Hạch hiện hình** bay về ngực nhân vật (lần đầu: thưởng boss) |

- **Linh Sa:** công thức chia quỹ theo phần đe dọa đã hạ, giống `onEnemyKilled` của Rồng Giữ Ải. Hạt cát: bung, nảy, lơ lửng 0,15 s, rồi hút về ô Linh Sa trên HUD (Lời Gọi §17.4). Vòng hút tự động khoảng 6 m quanh nhân vật (thử). Hạt ngoài vòng vẫn được ghi sổ, chỉ bay chậm hơn.
- **Bảo Hạp:** mỗi người thấy hộp của riêng mình. Nội dung lấy từ quỹ "khác", không bao giờ là sức mạnh vĩnh viễn: hộp nhỏ 15–25 Linh Sa, hộp vừa 30–45, hộp lớn 60–90, hoặc thay bằng 1 đan, phù đang có trong Hành Nang nếu ô còn chỗ (thử). Hộp **tự mở khi hết đợt**. Không ai mất hộp vì không chạy tới.
- **Linh Mạch** (khám phá ngoài trận, tùy chọn): từ đợt 3, mỗi người có tối đa 1 mạch mỗi đợt, cách trận 12–18 m, tồn tại 25 s. Đứng cạnh thì thu trong 1,5 s (trúng đòn thì ngắt), hoặc gõ chữ khai mạch để thu ngay. Mỗi mạch 15–25 Linh Sa. Tổng Bảo Hạp và Linh Mạch tối đa khoảng 8 % Linh Sa của ải.
- **Nhãn đồ:** Linh Sa thường không có nhãn chữ. Đồ hiếm (Bảo Hạp, Thú Hạch) có biểu tượng và một nhãn ngắn. Nhãn vẽ **dưới** thẻ chữ của thú, không che chữ (Codex §26.9). Màu theo bậc: trắng ngà cho thường, lục ngọc cho tinh anh, tím cho thú tướng, vàng kim cho thú vương. Không dùng đỏ, vì đỏ là màu nguy hiểm.
- **Vật liệu chỉ để tạo không khí:** thú có thể rơi "nanh sói linh", "lá linh thảo" như nhãn trong QCBH, nhưng đó chỉ là **hình** của một khoản Linh Sa đã ghi. Không có túi vật liệu.

### 4.5 Đan và phù (đồ tiêu hao, số ở chương 1, thử)

Có 2 ô, ô thứ 3 mở ở Thư Lâu. Mỗi ô giữ tối đa 3 viên hoặc 3 lá. Hồi chung 8 s. Mua bằng Linh Sa, không mang sang ải sau. Dùng bằng Alt+1/2/3 (Linux: Shift) hoặc click. Không xóa chữ đang gõ dở.

| Món | Tác dụng | Giá | Mở | Ghi chú |
|---|---|---|---|---|
| Hồi Xuân Đan | Hồi 25 % máu trong 2 s | 30 | Ải 4 | Đan đầu tiên, dạy ô đồ |
| Đại Hoàn Đan | Hồi 50 %, giải Cháy, Độc, Nguyền | 60 | Chương 3 | |
| Tĩnh Tâm Đan | Giải khống chế. Miễn khống chế cứng 4 s | 45 | Chương 2 | Khắc chế thú gầm choáng |
| Kim Thân Phù | Khiên = 20 % máu tối đa, 8 s, cho bản thân | 40 | Chương 2 | |
| Hộ Trận Phù | Khiên 150 × g(c) cho lõi ải và trận kỳ trong vùng, 10 s | 50 | Chương 4 | Đồ đội: ai dùng cũng có lợi cho cả đội |
| Lôi Hỏa Phù | Ném vùng 3 m: 150 × g(c) sát thương phép | 50 | Chương 2 | Mặc định ném vào cụm đông nhất. Chuột chọn điểm được |
| Định Thân Phù | Mọi thú Chậm 40 % trong 4 s (boss 20 %) | 70 | Chương 5 | |
| Hoàn Hồn Đan | Tự kích khi gục: dậy với 40 % máu. Tối đa 1 viên mỗi ải | 150 | Chương 2 | Đã dùng thì không được 3 sao |

- **Không gõ để dùng đan, phù ở MVP.** Lý do: đan là nút cứu nguy. Bắt gõ đúng lúc máu thấp phạt người gõ chậm (cổng B3 của BALANCE.md). Thêm 2–3 chữ trên dải ô sẽ vượt ngân sách chú ý (Codex §1.9). Phương án "Dẫn Dược" (gõ hoặc nói một từ ôn ngắn trên ô thì đan +25 %) để thử ở P4, xem mục 8.
- Đan và phù tính vào trần chung của Codex §21: khiên có trần theo đối tượng, giảm sát thương có bucket riêng. Định Thân và Tĩnh Tâm theo luật khống chế giảm dần.
- Bùa thân trong ải (giống Tim Rồng, Vảy Cứng của Rồng Giữ Ải): **Huyết Phù** +10 % máu tối đa (80 / 120 / 160 Linh Sa, tối đa 3 lần) và **Giáp Phù** +15 giáp (70 / 105 / 140, tối đa 3 lần).

### 4.6 Trận Phường: cửa hàng giữa đợt

- Hàng bán là các món trong Hành Nang: trận kỳ, cơ quan, đan, phù, bùa thân. Danh sách trận kỳ, cơ quan và tác dụng do tài liệu trận pháp và combat quyết. Tài liệu này chỉ chốt **luật giá**:
  - Giá cấp 1 đặt sao cho "điểm hiệu dụng mỗi Linh Sa" của mọi món nằm trong 0,8–1,2 lần món tham chiếu (cách định giá của Rồng Giữ Ải 03 §13.1).
  - Nâng cấp kém hiệu quả dần: cấp 2 +45 %, cấp 3 +35 % nữa. Nhánh mở ở cấp 3, phải mở trước bằng Thú Hạch.
  - Hiệu ứng cùng loại chồng vùng thì lấy mạnh nhất, không cộng.
- Cửa hàng **không ngẫu nhiên**, không đổi hàng. Mọi món trong Hành Nang luôn có.
- **Thương Nhân Du Phương** (biến cố, sau MVP): một xe hàng ghé 15 s giữa đợt, giảm 20 % giá. Tối đa 1 lần mỗi ải. Không ra trong ải boss.

### 4.7 Pháp bảo và trang bị (cố định ở bản đầu)

| Ô (mở) | Vai | Ví dụ món 1 → món 2 (phái Kiếm, thử) | Ghi chú |
|---|---|---|---|
| Pháp Bảo Bản Mệnh (ải 3) | Tăng chiêu chính của phái | **Thanh Phong Kiếm**: chiêu Kiếm +6 → +18 % (cấp 1 → 5) · **Song Ảnh Kiếm** (boss chương 2): đòn gõ liên tục thêm 1 kiếm phụ 30 → 50 % sát thương | Mỗi phái MVP có 2 món. Đổi màu VFX và tiếng của chiêu, không đổi model nhân vật |
| Hộ Thân Y (ải 11) | Sống sót | **Áo Vân Tằm**: máu +70 → +210, kháng +8 → +24 · **Áo Huyền Giáp** (boss chương 3): dưới 30 % máu thì nhận khiên 15 → 25 %, 1 lần mỗi đợt | Dùng chung mọi phái |
| Ngọc Bội (chương 2) | Hỗ trợ việc học, không tăng sát thương thô | **Ngọc Tĩnh Tâm**: từ mới gõ Hoàn hảo thì đòn +15 → +30 % · **Ngọc Ôn Cố**: kết quả "Ẩu" chỉ còn ×0,70 → ×0,80 thay vì ×0,60 | Chép ý Ngọc Chữ của Rồng Giữ Ải: không bao giờ làm chữ khó đọc hơn hoặc dài hơn |

- Ngân sách: Pháp bảo ≤ +15 % hiệu dụng. Cả tài khoản nâng hết ≤ +25 % so với bộ đồ trung bình ở cùng chương. Trần này **bao gồm** cả cảnh giới, pet và Thư Lâu. Giá trị tuyệt đối vẫn tăng theo cảnh giới, nhưng thú cũng tăng theo g(c).
- **Khí Linh** (sau MVP): tên, giọng và hình hồn của pháp bảo. Mở ở cấp 5. Chỉ là ngoại hình và lời thoại, không thêm chỉ số.
- **Độ hiếm, dòng phụ, rèn may rủi:** chỉ cân nhắc sau bản công khai, khi số đo cho thấy người chơi muốn thêm chiều sâu (Rồng Giữ Ải 03 §5.2).

### 4.8 Chế tạo tối thiểu

| Giai đoạn | Làm gì | Vì sao |
|---|---|---|
| **MVP** | Không có xưởng. **Đan phương, phù phương** mở ở Thư Lâu bằng Văn Khí: mở xong thì món đó vào được Hành Nang và bán ở Trận Phường | Chế tạo trở thành "học được công thức nhờ học tiếng Anh". Không cần kho, không cần vật liệu |
| **Sau MVP: Đan Lô** | Một bài 1–2 phút ngoài ải. Thẻ công thức ghi nghĩa tiếng Việt của 3 "dược liệu" (là từ đến hạn ôn của người chơi). Người chơi gõ hoặc nói từ tiếng Anh đúng. Đủ đúng thì công thức lên phẩm: Hạ → Trung (+10 % hiệu lực) → Thượng (+20 %), vĩnh viễn | Thay cái hay của QCBH (luyện đan thành phẩm) bằng bài nhớ nghĩa thật (sự kiện `meaning-recall`). Không sinh kho đan để tích trữ |
| **Sau MVP: Luyện Khí** | Mở nhánh A/B của pháp bảo bằng Thú Hạch, chọn và đặt lại miễn phí | Giữ lựa chọn build, bỏ roll |
| **Không làm** | Sáu nghề có điểm riêng, gộp phẩm 5:1, vật liệu có tạp chất, hái thuốc và đào khoáng cày ngoài thế giới | Game thủ ải không có thế giới mở. Mỗi nghề là một vòng cày |

- Đan Lô có trần: tối đa 3 lần thử mỗi ngày, mỗi công thức tối đa 1 bậc mỗi ngày. Sai không mất gì, chỉ ghi kết quả học. Dùng gợi ý (IPA, nghe) thì vẫn qua nhưng được ghi là "có gợi ý" (Codex §19.1).

### 4.9 Sơn Môn: hub ngoài ải

| Nơi | Tiền | Làm gì | MVP? |
|---|---|---|---|
| Trận Đài | — | Chọn ải, xem thẻ báo, Hành Nang, đổi pháp bảo, Học trước | Có |
| Thư Lâu | Văn Khí | 10 bậc: ô đan 3, ô Hành Nang 9 và 10, Linh Sa đầu ải +20 / +40 / +60 / +100, hồi giữa đợt 15 → 20 %, mở đan phương và phù phương, thi lên cấp từ | Có |
| Bảo Khí Lò | Thú Hạch | Mở và nâng pháp bảo, áo, ngọc. Cấp trận kỳ, cơ quan. Mở nhánh | Có |
| Sổ Bảo Vật | — | Xem mọi món, món chưa mở hiện bóng và nơi mở | Có |
| Đan Lô | (không tiêu tiền) | Bài nhớ nghĩa nâng phẩm công thức | Sau |
| Bảng Truy Thú | Thú Hạch | 3 việc mỗi ngày, ví dụ: ôn đúng 30 từ, hạ 2 thú tướng, giữ lõi ải không mất máu. Thưởng dồn tối đa 3 ngày, bỏ ngày không bị phạt | Sau |
| Tàng Y Các | Danh hiệu, thành tựu | Ngoại trang, khung tên, màu VFX. Không bán sức mạnh | Sau |

### 4.10 Chống cày, chống lạm phát và các cổng kiểm

- Thắng ải lần đầu thưởng đủ. Chơi lại 30 %. Thua giữ 30 %. Sao chỉ tính một lần mỗi ải.
- Không thể lực, không giới hạn lượt. Nhắc nghỉ sau 30 phút (20 phút với hồ sơ trẻ em).
- Không ô "sinh Linh Sa" chồng được. Nếu có món kiểu Giếng Vàng thì tối đa 1 cái mỗi ải, trần +12 %.
- Cổng bot (theo BALANCE.md B1–B9 và cổng của Rồng Giữ Ải):

| Cổng | Kiểm gì | Ngưỡng thử |
|---|---|---|
| E1 | Linh Sa mỗi ải khớp công thức | Trong ±15 %. Dư cuối ải ≤ 15 % |
| E2 | Gõ là sức chính | Bot "Không gõ, mua tối ưu" thua trước hết đợt 3 ở mọi ải trừ chế độ Thư giãn |
| E3 | Không món nào là đáp án duy nhất | Mọi món nằm trong 0,8–1,2 điểm mỗi Linh Sa. Bot "Tham một nhóm" không thắng hơn bot Cân bằng quá 10 điểm % |
| E4 | Đường chính không cần cày | Bot 35 WPM với bộ đồ trung bình thắng ≥ 55 % mọi ải không phải boss |
| E5 | Đứng trận và chạy nhặt | Chênh Linh Sa giữa bot đứng trận và bot đi Linh Mạch ≤ 10 % |
| E6 | Bot và pet không nhân loot | Số Bảo Hạp mỗi người như nhau dù có 0, 1 hay 2 pet, bot |
| E7 | Học có lời | Bot làm đủ Thẻ Ôn và Học trước có ≥ 10 % Linh Sa hơn bot bỏ qua. Không bao giờ quá 15 % |

### 4.11 Dữ liệu

```text
src/content/data/economy/
  currencies.json      3 tiền: id, phạm vi (run | account), nguồn hợp lệ (danh sách id), trần ngày
  consumables.json     đan, phù, bùa thân: hiệu ứng, giá, chồng, hồi, chương mở, mã khắc chế
  loot.json            bậc thú → hạt hình, hộp, tỉ lệ; nội dung hộp theo quỹ "khác"
  artifacts.json       pháp bảo, áo, ngọc: hiệu ứng theo cấp, nơi mở, giá Thú Hạch
  library.json         Thư Lâu 10 bậc
  rewards.json         sao, boss, chơi lại, thua, đổi Linh Sa dư; mã nguồn thu (server registry)
```

```jsonc
{ "id": "lightning-fire-talisman", "kind": "talisman", "slotUse": "throw",
  "effect": { "kind": "area-damage", "radiusM": 3, "base": 150, "type": "spell", "scalesWithChapter": true },
  "cost": 50, "stackMax": 3, "cooldownGroup": "item", "cooldownMs": 8000,
  "unlock": { "chapter": 2, "library": null }, "counters": ["SWARM"], "icon": "talisman-thunder", "sfx": "item.talisman.thunder" }
```

- Mọi số nằm trong dữ liệu. Test dữ liệu kiểm: giá trong dải, mỗi món có biểu tượng, âm, VFX, nơi mở, mã khắc chế. Mỗi mã khắc chế của thú có ít nhất một món mở trước hoặc cùng chương (giống ma trận 03 §0.3).

### 4.12 Chia MVP và sau MVP

| MVP (khớp P1–P4 của Codex §27) | Sau MVP |
|---|---|
| 3 tiền, quỹ Linh Sa 60/25/15, ghi sổ ngay, hình cát bay | Đan Lô (nhớ nghĩa nâng phẩm), Luyện Khí nhánh A/B, Khí Linh |
| Trận Phường giữa đợt, bán và hoàn tiền, đặt nhanh từ chương 6 | Thương Nhân Du Phương, "Dẫn Dược" (nếu thử đạt) |
| 6 đan, phù đầu (Hồi Xuân, Tĩnh Tâm, Kim Thân, Lôi Hỏa, Định Thân, Hoàn Hồn) và 2 bùa thân | Hộ Trận Phù, Đại Hoàn Đan, đan hồi linh lực (tính vào trần hồi chiêu 30 %) |
| Bảo Hạp cá nhân (tinh anh, boss) và khóa chữ trong lúc nghỉ | Bảng Truy Thú, Tàng Y Các, danh vọng sơn môn (không tiêu được) |
| Linh Mạch bản đơn giản: thu 1,5 s, chữ khai mạch tùy chọn | Chế độ vô tận "Thú Triều Vô Tận" với lượt chọn Cơ Duyên 1 trong 3 (Tuyến Cuối §4.0d) |
| Pháp bảo cố định 3 ô, mỗi phái MVP 2 món, cấp 1–5 | Độ hiếm, dòng phụ (nếu số đo cần), chuyển Linh Sa cho đồng đội trong ải |
| Thư Lâu 10 bậc, Bảo Khí Lò, Sổ Bảo Vật, cuộn Thu Hoạch | Server kết toán cho co-op người thật (P6) |

## 5. Solo và đội

| Vấn đề | Solo | Đội 2–3 (7 người là mở rộng) | Luật công bằng |
|---|---|---|---|
| Ví Linh Sa | 1 ví | Mỗi ghế 1 ví, kể cả ghế bot | Không có quỹ chung. Không ai tiêu tiền của người khác |
| Ngân sách | Theo công thức 4.2 | **Mỗi ghế nhận đủ ngân sách như solo.** Độ khó đội do mảng thú và encounter chỉnh, kinh tế không cắt | Không phạt người chơi đội bằng tiền ít hơn |
| Linh Sa hạ thú | Tất cả về mình | Quỹ 60 % của mỗi ghế trả theo **tổng đe dọa cả đội đã hạ** | Không tranh đòn kết liễu. Người hỗ trợ, hộ trận nhận như người dọn bầy (Codex §22.3) |
| Linh Sa hết đợt | Về mình | Mọi ghế còn hoạt động | Ghế treo máy quá 30 s (không từ hợp lệ, không di chuyển, không chết, không tạm dừng) thì bot tiếp quản. Phần của người đó trong đợt đó không đổi ra thưởng ngoài ải |
| Quỹ "khác" 15 % | Học trước, Thẻ Ôn, Bảo Hạp, Linh Mạch | **Của ai người đó nhận** | Học của ai thì thưởng cho người đó. Bot không làm Thẻ Ôn |
| Bảo Hạp | Của mình | Mỗi người một hộp riêng, rơi theo luồng RNG riêng (seed của ván và id ghế) | Không giành hộp. Không ai thấy hộp của người khác |
| Linh Mạch | 1 mạch mỗi đợt | Mỗi người 1 mạch riêng ở vị trí khác nhau | Pet nhặt Linh Sa đã lộ, nhưng không thu Linh Mạch hộ |
| Đan, phù | Của mình | Của mình. Hộ Trận Phù có lợi cho cả đội nhưng người dùng tự trả | Không có đan "cứu cả đội" rẻ hơn đan cá nhân |
| Bot | Bot bù ghế dùng ví của ghế đó, mua theo luật bot Cân bằng | Như solo | Ví bot không đổi ra Thú Hạch, Văn Khí. Hết ải thì xóa |
| Thưởng ngoài ải | Theo 4.2 | **Mỗi người nhận như solo** (sao, boss, chơi lại) | Không có vật liệu sức mạnh chỉ có trong đội (Codex §15). Đội chỉ có thêm danh hiệu, ngoại trang |
| Văn Khí | Từ học của mình | Từ học của mình | Bot, pet, đánh nền không tạo học thay người (Codex §22.2) |
| Rời giữa chừng | Lưu ảnh chụp ở đầu mỗi lần nghỉ để chơi tiếp | Bot thay ghế. Người rời nhận thưởng ngoài ải theo số đợt đã tham gia hữu ích, nhân 30 % (như "thua giữ 30 %") | Rời không được thưởng nhiều hơn chơi hết |
| Đại trận 7 ghế | — | Cùng luật. Trận Phường chỉ cho mỗi ghế đặt trên nhãn trận của ghế mình | Không ai chiếm hết ô đặt |
| Giao dịch | — | Không tặng, không đổi đồ ngoài ải. Chuyển Linh Sa trong ải để sau MVP, tối đa 30 % mỗi lần nghỉ | Chặn cày hộ, buôn tài khoản |

**Online (co-op người thật, P6):** Durable Object của phòng chạy mô phỏng có seed và quyết mọi lần rơi đồ. Client chỉ vẽ. Cuối ải, server kết toán **một giao dịch cho mỗi người** (có biên nhận), ghi vào D1. Nguồn thu là một **danh sách cố định ở server**: sao, boss, chơi lại, Văn Khí theo sự kiện học đã nhận. Không có kênh "earn" chung để client tự báo số (bài học #23 trong `2026-10-21-code-review.md`). Ghi một lần mỗi ván giữ lượng ghi trong mức miễn phí của Cloudflare.

## 6. Gắn với học tiếng Anh (Typing / Voice / Hybrid)

| Chỗ | Từ nào | Lúc nào | Bắt buộc? | Thưởng | Sự kiện học |
|---|---|---|---|---|---|
| Học trước (Trận Đài) | Từ mới của ải | Trước ải | Không | +5 Linh Sa mỗi từ, tối đa +40 | Có ghi |
| Thẻ Ôn | Từ đến hạn ôn, từ yếu. Câu nhớ nghĩa, nghe | Nghỉ đợt, đồng hồ dừng | Không (tắt được trong cài đặt) | +10 Linh Sa mỗi câu đúng, tối đa 3 câu, và Văn Khí | `review-card`, `meaning-recall` |
| Khóa chữ Bảo Hạp | 1 từ đã thuộc hoặc đến hạn, 3–6 chữ | Nghỉ đợt | Không. Hộp vẫn tự mở | Gõ hoặc nói đúng thì hộp +50 % | `typing-skill` |
| Chữ khai mạch (Linh Mạch) | 1 từ đã thuộc hoặc đến hạn, 3–5 chữ. Chỉ hiện khi nhân vật cách mạch dưới 4 m | Trong đợt | Không. Đứng thu 1,5 s cũng được | Thu ngay, không bị ngắt | `typing-skill` |
| Nhãn đồ hiếm | Tên tiếng Anh của đồ (ví dụ `fang`, `herb`), hiện kèm nghĩa | Khi rơi | — | Chỉ tiếp xúc, **không chấm, không tính là đã học** | Không |
| Đan Lô (sau MVP) | Từ đến hạn, gõ từ nghĩa tiếng Việt | Ngoài ải | Không | Nâng phẩm công thức | `meaning-recall` |
| Văn Khí | Mọi từ học hợp lệ của người đó | Mọi lúc | — | Thư Lâu | Gom từ các sự kiện trên |

**Chống quá tải:**
- **Không từ mới nào gắn vào vật phẩm.** Vật phẩm chỉ dùng từ đã thuộc hoặc đến hạn ôn. Từ mới chỉ xuất hiện trên thú chậm và ở Học trước.
- Trong đợt, số chữ không thuộc kỹ năng và không thuộc thú **tối đa 1 mỗi người** (chữ khai mạch, và chỉ khi đứng gần). Thú boss đang ra đòn thì không hiện chữ khai mạch.
- Chữ vật phẩm đi chung bộ phân giải với ô kỹ năng (Codex §1.4): không trùng nguyên từ, không có cặp mà từ này là tiền tố trọn vẹn của từ kia. Không cướp từ đang gõ dở.
- **Voice:** khóa chữ Bảo Hạp và chữ khai mạch nói được. Thẻ Ôn dùng profile riêng (độ trễ, nhận chưa chắc thì không phạt). **Hybrid:** mỗi chữ có đúng một kênh sở hữu. Đan, phù dùng phím nên không đụng kênh nào.
- Học không bao giờ làm thua: bỏ qua mọi chữ vật phẩm chỉ mất phần thưởng thêm, tối đa khoảng 8–15 % Linh Sa (cổng E7).

## 7. Tái sử dụng và chi phí sản xuất

| Dùng lại | Đường dẫn | Dùng cho | Chi phí |
|---|---|---|---|
| Quỹ vàng ải (60/25/15, cụm bầy trả một lần, hết đợt tăng 10 %) | `games/dragon-hold/src/sim/economy.ts` | Linh Sa: chép kèm header `// Source:`, đổi tên | S |
| Cửa hàng theo pha, đồ tiêu hao, hồi chung, bán hoàn, đặt nhanh | `games/dragon-hold/src/sim/shop.ts`, `ui/shop-strip.ts` | Trận Phường, dải ô đan | S–M |
| Luật kinh tế, giá, Thư Viện, trang bị cố định, cổng bot | `docs/games/dragon-lane/00-canon.md` §4.9, `03` §3–§6 và §12–§13, `04` §8–§10 | Số thử của tài liệu này | — |
| Rơi đồ và thu nhặt (bung, nảy, lơ lửng, hút, ghi sổ ngay) | `games/space-typing/docs/td/TYPING_DEFENSE_DESIGN.md` §17.4; `games/space-typing/src/rewards/combat-credit-drops.ts` | Hạt Linh Sa, Thú Hạch bay về nhân vật | M |
| Kho vĩnh viễn và lượt chọn trong chương | `games/space-typing/docs/survival/SURVIVAL_MODE_PLAN.md` §4.0d | Chế độ vô tận sau MVP | M |
| Ví, giao dịch có biên nhận, chống đếm hai lần | `games/space-typing/src/persistence/account-transactions.ts`, `src/economy/wallet-rules.ts` (xem skill `progression-economy`) | Lưu Văn Khí, Thú Hạch | M |
| Ví server, danh sách nguồn thu | `games/space-typing/cloud/src/wallet.ts`; lỗi #23 trong `docs/changelog/2026-10-21-code-review.md` | Kết toán co-op | L (đi cùng netcode P6) |
| Hợp đồng Admin cửa hàng | `games/space-typing/contracts/space-typing-admin-shop.v1.json` | Nếu cần chỉnh giá qua Admin (sau MVP) | M |
| Sự kiện học | `shared/game-kit/learning/events.ts` (`LearningEvent`), `bridge.ts` | Thẻ Ôn, khóa chữ, Đan Lô | S |
| RNG có seed theo luồng | `shared/game-kit/platform/rng.ts` | Luồng loot riêng cho từng ghế | S |
| Bot gõ giống người, cổng | `shared/game-kit/balance/typist.ts`, `gates.ts`; `docs/games/BALANCE.md` | Cổng E1–E7 | M |
| Số bay, phản hồi | `shared/game-kit/feedback/numbers.ts`, `profiles.ts` | "+Linh Sa", cuộn Thu Hoạch | S |

**Tài sản mới (ước lượng):** khoảng 40 biểu tượng 2D (8 đan, phù; 6 pháp bảo; 6 áo, ngọc; 3 tiền; 3 hộp; Linh Mạch; nút Thư Lâu), do Codex vẽ. Không cần model 3D. 8 VFX đồ tiêu hao và 3 VFX hộp mở, dùng hệ hạt sẵn có của cảnh 2D.
**Âm (luật Q6 trong `tools/audio-lab/DECISIONS.md`, chỉ dùng thu âm CC0):** Linh Sa về HUD là tiếng chuông ngọc hoặc pha lê nhỏ, cao dần theo chuỗi. Thú Hạch là tiếng ngân trầm, dài. Bảo Hạp là tiếng khóa gỗ, đồng mở rồi một chuỗi ngân. Đan là tiếng nút hồ lô bật ra rồi tiếng khí hồi. Phù là tiếng giấy bùa cháy rồi tiếng sét hoặc lửa đúng cỡ. **Không** dùng "bụp", "pop" hay tiếng đồ chơi.

| Hạng mục | Chi phí |
|---|---|
| Sim kinh tế và cửa hàng (chép từ Rồng Giữ Ải, đổi dữ liệu) | S–M |
| Dữ liệu 8 đan, phù và 2 bùa thân, test dữ liệu | S |
| Rơi đồ, hút, nhãn, Bảo Hạp, Linh Mạch, cuộn Thu Hoạch | M |
| Pháp bảo cố định (3 ô × 2 món × số phái MVP), Bảo Khí Lò | M |
| Thư Lâu, Sổ Bảo Vật, Trận Đài, Hành Nang (UI ngoài ải) | M |
| Lưu và giao dịch cục bộ | M |
| Kết toán server cho co-op | L |
| Đan Lô (sau MVP) | M |
| Biểu tượng, VFX, âm | M (phụ thuộc Codex vẽ và Audio Lab) |

## 8. Rủi ro và câu hỏi cho chủ dự án

**Rủi ro:**

| Rủi ro | Hậu quả | Giảm thiểu |
|---|---|---|
| Lạm phát, cầu tuyết | Ải sau quá dễ | Ngân sách cố định mỗi ải. Giá không đổi. Linh Sa dư đổi tối đa 3 Thú Hạch. Trần +25 % cho tài khoản |
| Cày | Người học bỏ học để farm | Không gộp phẩm, không vật liệu. Chơi lại 30 %. Trần ngày cho Văn Khí. Cổng E4 |
| Nhãn đồ che chữ | Gõ sai, khó đọc | Đồ thường không có nhãn chữ. Nhãn nằm dưới thẻ chữ. Gộp khi quá nhiều |
| Quá tải chữ trong đợt | Người mới loạn | Tối đa 1 chữ vật phẩm mỗi người. Không từ mới trên vật phẩm. Đan dùng bằng phím |
| Tranh loot, ăn theo trong đội | Mâu thuẫn, người hỗ trợ thiệt | Chia theo ghế và đe dọa cả đội. Hộp riêng. Luật treo máy |
| Client tự in tiền | Phá kinh tế online | Server quyết loot, danh sách nguồn thu cố định, kết toán một lần có biên nhận |
| Chơi với bot để farm | Thưởng ảo | Bot không có thưởng ngoài ải. Solo kèm bot nhận như solo |
| Đặt tên, hình gần QCBH | Rủi ro bản quyền, mất bản sắc | Thuật ngữ thể loại chung (đan, phù, pháp bảo) nhưng tên món, tên tiền, UI là của mình (Codex §20) |

**Câu hỏi (mỗi câu có phương án đề xuất; anh không trả lời thì làm theo đề xuất):**

1. **Ba tiền Linh Sa / Văn Khí / Thú Hạch?** Đề xuất: có, giống khung đã chốt của Rồng Giữ Ải. Cách khác: gộp Thú Hạch vào Văn Khí. Cách này đơn giản hơn nhưng mất phần thưởng cho chiến thắng.
2. **Đan, phù dùng bằng phím hay bằng gõ từ?** Đề xuất: MVP dùng Alt+1/2/3 và chuột. Ở P4 thử "Dẫn Dược" tùy chọn (gõ hoặc nói từ ôn thì đan +25 %), giữ lại chỉ khi người mới không bị quá tải.
3. **Có mang đan tự luyện từ ngoài vào ải không?** Đề xuất: không. Đan Lô sau MVP nâng phẩm công thức vĩnh viễn, không sinh kho đan để tích trữ.
4. **Trang bị ngẫu nhiên (độ hiếm, dòng phụ) như QCBH?** Đề xuất: cố định ở bản đầu. Thêm chiều sâu sau bản công khai nếu số đo cho thấy người chơi cần.
5. **Ví đội: riêng từng người chia đều, hay quỹ chung?** Đề xuất: ví riêng, chia đều theo ghế và theo đe dọa cả đội đã hạ. Quỹ chung dễ cãi nhau và khó cho bot.
6. **Cho tặng, giao dịch giữa người chơi?** Đề xuất: không có ngoài ải. Chuyển Linh Sa trong ải để sau MVP, có trần.
7. **Cửa hàng tiền thật hoặc ngoại trang trả phí?** Đề xuất: bản đầu không có. Ngoại trang đến từ thành tựu. Nếu sau này bán ngoại trang thì phải quyết riêng và không bao giờ bán sức mạnh, không gacha.
8. **Thể lực hoặc giới hạn lượt chơi như Warp của Space?** Đề xuất: không. Game học không nên chặn người muốn ôn thêm. Chỉ dùng trần mềm cho thưởng.
9. **Vật phẩm đột phá cảnh giới?** Đề xuất: boss chương phát chắc chắn, không bán, không rơi ngẫu nhiên. Mảng tu luyện chốt luật đột phá.
10. **Linh Mạch (đi ra ngoài trận để thu) có vào MVP?** Đề xuất: có, bản đơn giản (thu 1,5 s, chữ khai mạch tùy chọn). Đây là lý do cụ thể để rời trận (Codex §0) và chênh thu nhập đã giới hạn ≤ 10 %.
