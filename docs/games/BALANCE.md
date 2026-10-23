# Cân bằng game theo nhiều yếu tố (dùng chung cho 3 game)

> **Yêu cầu của chủ dự án (23/10/2026):** phải thiết kế để game cân bằng, tránh quá dễ hoặc quá khó gây nhàm chán. Cân bằng dựa trên nhiều yếu tố: tốc độ gõ, tỉ lệ chính xác và nhiều yếu tố khác.
> **Áp dụng cho:** Rồng Giữ Ải (`dragon-hold`), Lời Gọi (`typing-defense`), Tuyến Cuối (`typing-survival`).
> **Thứ tự ưu tiên:** file này giữ khung chung: yếu tố, chỉ số, bộ điều nhịp, bot, cổng. Số riêng của từng game nằm trong tài liệu chuẩn của game đó, và phải trỏ về đây. Riêng Rồng Giữ Ải: mục 9.1 của file này thay quyết định D06 và hàng k_E ở `dragon-lane/00-canon.md` §4.4.

## 0. Vì sao cần làm lại

- Bản M0a của Rồng Giữ Ải: bot 25, 35 và 60 WPM đều thắng 100 %, máu Rồng còn 100 %. Quái chết khi mới đi được khoảng 23 % đường trong Vùng Chữ. Gần như không con nào tới được Bệ Rồng.
- Gốc lỗi thứ nhất: độ khó chỉ được đo bằng **một số**, là tải gõ của một người chuẩn 35 WPM.
- Gốc lỗi thứ hai: game chỉ co giãn theo người chơi theo **một chiều**. Nhịp đợt chậm lại cho người gõ chậm; người gõ nhanh thì phải tự chọn mức Khó.
- Gốc lỗi thứ ba: quái chỉ gây hại khi đi tới nơi. Hàng đợi chữ ngắn hơn quãng đường nhiều, nên gõ đủ nhanh là không bao giờ thấy áp lực.
- Tuyến Cuối bị lỗi ngược lại: bot 25 WPM chỉ thắng 11/24 sau khi chỉnh cho 35 WPM.
- Kết luận: game phải đo **người đang chơi** theo nhiều mặt, rồi giữ trận trong **vùng cuốn**: đủ căng để không chán, đủ công bằng để không nản.

## 1. Nguyên tắc

1. **Khó theo chính người chơi**, không theo người trung bình. Hai người gõ 25 và 60 WPM đều phải thấy căng vừa phải.
2. **Đo nhiều yếu tố.** Tốc độ và độ chính xác là hai trong mười ba yếu tố (mục 2).
3. **Điều chỉnh nhỏ, có giới hạn, không lộ.** Không để quái tự chết, không đổi máu quái đang sống, không "cao su" thấy rõ.
4. **Học luôn rõ.** Độ khó không bao giờ được ép người chơi bỏ qua nghĩa, IPA, phát âm.
5. **Tất định.** Mọi điều chỉnh tính từ tham số đầu ải hoặc từ trạng thái trong trận. Cả hai ghi vào replay, nên cùng seed và cùng phím vẫn ra cùng mã băm.
6. **Công bằng khi so điểm.** Lời Thề, Vương Miện, bảng xếp hạng, Duel tắt bộ điều nhịp và dùng tham số cố định.
7. **Khó lên bằng nhiều trục.** Thêm thành phần, đường, kỹ năng, hào quang, khắc chế. Không bắt người chơi gõ nhanh hơn sức mình.
8. **Đo được mới tính.** Mỗi đòn bẩy có chỉ số đo và cổng bot.

## 2. Hồ sơ năng lực: 13 yếu tố

Mỗi game giữ một hồ sơ cho mỗi người chơi. Mỗi yếu tố có giá trị và **độ tin** (số mẫu). Khi chưa đủ mẫu, game dùng giá trị mặc định của chế độ, rồi trộn dần sang số đo.

| # | Yếu tố | Đo thế nào | Dùng để |
|---|---|---|---|
| 1 | **Tốc gõ E** | WPM thực trong trận (EWMA), tách theo độ quen của từ | Nhịp k, độ dài từ, khoảng sinh |
| 2 | **Độ chính xác a** | Phím đúng / tổng phím; tỉ lệ từ không lỗi | Tỉ lệ từ mới, chuẩn thắng ẩu, gợi ý luyện |
| 3 | **Thói sửa lỗi** | Tỉ lệ Backspace, tỉ lệ từ Ẩu, số lần bỏ khóa | Biên thời gian, lời khuyên chậm mà chắc |
| 4 | **Độ đều** | Hệ số biến thiên thời gian mỗi từ | Người không đều được biên an toàn lớn hơn |
| 5 | **Thời gian nhận từ** | Từ lúc từ hiện tới phím đầu, tách theo từ mới / đang học / đã thuộc | Thời gian báo trước, chỗ đặt từ mới |
| 6 | **Vốn từ** | Độ thuộc từ ở lõi học chung, cấp từ đang học | Cấp từ của ải, tỉ lệ từ mới mỗi đợt |
| 7 | **Chia chú ý** | Tốc độ rơi bao nhiêu khi có ≥ 6 chữ sống hoặc nhiều đường | Số đường cùng sinh, đỉnh đợt |
| 8 | **Chiến thuật** | Phần sát thương phe ta, vàng dư, món đặt đúng chỗ, đổi món theo quái | Gợi ý xây, độ chặt của kinh tế |
| 9 | **Phản xạ báo trước** | Tỉ lệ xử lý đúng đòn đã báo trước (khóa đúng quái, dùng kỹ năng) | Thời gian báo trước, số đòn lớn mỗi đợt |
| 10 | **Xu hướng gần đây** | Thắng/thua liên tiếp, máu còn, số lần gần thua, số lần bỏ dở | Biết người chơi đang chán hay đang nản |
| 11 | **Mệt trong phiên** | Tốc độ và độ chính xác tụt dần trong phiên dài | Giảm nhẹ nhịp, gợi ý nghỉ |
| 12 | **Hồ sơ và mục tiêu** | Trẻ em hay người lớn; chế độ đã chọn (Thư giãn, Cân bằng, Thử thách, Học) | Dải đích của các chỉ số (mục 3) |
| 13 | **Nhập liệu** | Bộ gõ tiếng Việt đang bật, bàn phím lạ (đo lỗi theo phím) | Chỉ cảnh báo và gợi ý; không đổi độ khó |

- Hồ sơ lưu riêng ở từng game (khóa `<game>.skill`). Nếu portal có độ thuộc từ (`lookup` của lõi học) thì yếu tố 6 lấy từ đó.
- Hồ sơ chỉ cập nhật sau mỗi ải hoặc mỗi đợt, không giữa từ. Một ải tệ không kéo hồ sơ tụt mạnh: EWMA nặng 0,25 cho ải mới, và loại ngoại lệ (bỏ dở, AFK).
- Màn **Hồ sơ gõ** cho người chơi xem tốc độ, độ chính xác, thời gian nhận từ mới, độ đều, và một câu khuyên ngắn. Người học thấy mình tiến bộ.

## 3. Chỉ số trải nghiệm (đo trong trận)

Bot và người thật đo cùng các chỉ số này. Báo cáo cân bằng in đủ các chỉ số.

| Chỉ số | Định nghĩa | Nói lên |
|---|---|---|
| **Thắng** | Tỉ lệ thắng ải | Tổng quát |
| **Biên an toàn S** | Máu (hoặc mạng) còn lúc kết ải | Dễ quá hay khó quá |
| **Áp lực P** | Phần thời gian đợt có mối nguy thật: quái trong vòng gần, Rồng (tàu, Lũy) đang mất máu, đòn lớn đang báo | Có căng không |
| **Nhàn I** | Phần thời gian đợt không có chữ nào để gõ và không có quyết định nào | Chán |
| **Ngộp O** | Phần thời gian chữ sống chạm trần, hoặc hàng đợi > 4 từ, hoặc người chơi bỏ khóa liên tục | Nản |
| **Gần thua N** | Số lần máu xuống dưới 30 % rồi sống lại | Khoảnh khắc đáng nhớ |
| **Quãng đường khi chết Q** | Quái đã đi bao nhiêu phần đường khi bị hạ (trung vị) | Sức gõ so với áp lực |
| **Phần phe ta** | Phần sát thương không do gõ | Gõ vẫn là chính |
| **Học** | Từ mới gặp đủ lần, nghĩa đọc được, sự kiện học đúng luật | Học không bị lấn |

### Dải đích theo chế độ

| Chỉ số | Thư giãn | Cân bằng | Thử thách |
|---|---|---|---|
| Thắng | ≥ 92 % | 75–90 % | 50–75 % |
| Biên S (trung vị) | ≥ 70 % | 35–65 % | 15–45 % |
| Áp lực P | 5–15 % | 15–35 % | 30–50 % |
| Nhàn I | ≤ 20 % | ≤ 10 % | ≤ 5 % |
| Ngộp O | ≤ 3 % | ≤ 8 % | ≤ 15 % |
| Gần thua N (trung bình mỗi ải) | ~0 | 0,3–1 | 1–2 |
| Quãng Q (trung vị) | ≤ 45 % | 50–70 % | 60–80 % |

- Dải đích **giống nhau với mọi tốc độ gõ**. Đây là điểm mới: người 25 và 60 WPM cùng chơi Cân bằng phải rơi vào cùng dải.
- Hồ sơ trẻ em dùng dải Thư giãn, trừ khi phụ huynh đổi.

## 4. Đòn bẩy (game đổi độ khó bằng gì)

### 4.1 Trước ải (đặt theo hồ sơ, ghi vào replay)

| Đòn bẩy | Theo yếu tố | Giới hạn |
|---|---|---|
| **Nhịp k** (giãn hoặc nén khoảng sinh và giờ đợt) | E, độ đều, mệt | k = clamp(C(E_eff) / C_ref ; 0,75 ; 1,30). Hai chiều: người nhanh bị nén, người chậm được giãn |
| E hiệu dụng `E_eff` | E, a, độ đều | E_eff = E × (0,6 + 0,4 × a²) × (1 − 0,5 × CV), giữ trong [0,7E ; E] |
| Độ dài từ | E | Theo bảng riêng của game (Rồng: 01 §3.4) |
| Tỉ lệ từ mới mỗi đợt | a, vốn từ, thời gian nhận từ mới | Thấp hơn khi a < 90 % hoặc nhận từ mới > 1,5 s; không dưới mức hẹn của ải học |
| Thời gian báo trước đòn lớn | Phản xạ báo trước | × 0,85–1,5; không dưới mức tối thiểu của game |
| Số đường sinh cùng lúc ở đỉnh | Chia chú ý | Giảm 1 đường ở đỉnh khi tốc độ rơi > 35 % lúc đông |
| Gợi ý mức khó | Xu hướng | Thắng dễ 2 ải liền (S ≥ 90 %, I ≥ 20 %): gợi ý lên; thua 2 lần liền: gợi ý xuống. Chỉ gợi ý, không ép |

### 4.2 Trong ải: Bộ điều nhịp

- Mỗi 5 s (300 tick), bộ điều nhịp tính **độ căng** τ từ P, I, O và biên máu của 20 s gần nhất.
- Nếu τ thấp hơn dải đích của chế độ quá 3 cửa sổ liền: tăng một bậc. Nếu cao hơn quá 2 cửa sổ liền: giảm một bậc. Có trễ (hysteresis), mỗi đợt đổi tối đa 2 bậc.
- **Mỗi bậc** là một trong các việc sau, tùy game:
  - khoảng sinh của toán kế ± 7 %;
  - thêm hoặc bớt **một** thuộc tính tinh anh ở toán kế;
  - dời đỉnh đợt sớm hoặc muộn vài giây;
  - quãng lặng sau đỉnh dài hoặc ngắn ± 3 s;
  - rơi một vật hỗ trợ (bình máu, vàng nhỏ) khi gần thua, tối đa 1 lần mỗi đợt.
- **Trần mỗi ải:** tổng thay đổi khoảng sinh ±15 %; W và danh sách loài của ải không đổi quá ±10 %.
- **Không bao giờ:** đổi máu quái đang sống, cho quái tự chết, đổi luật gõ, đổi điểm chấm từ.
- Tắt ở Lời Thề, Vương Miện, xếp hạng, Duel. Cài đặt có một dòng: "Nhịp tự điều theo cách bạn gõ: Bật/Tắt" (mặc định Bật).
- Bộ điều nhịp đọc trạng thái sim và chạy trong sim, nên vẫn tất định. Mỗi lần đổi ghi một sự kiện `pace` vào nhật ký để soi lại.

### 4.3 Sau ải

- Cập nhật hồ sơ, gợi ý mức, đổi tỉ lệ từ mới cho ải sau.
- Màn kết ải có một dòng ngắn về cách chơi, ví dụ: "Bạn gõ nhanh nhưng hay sai chữ đầu: chậm lại một nhịp sẽ được Hoàn hảo nhiều hơn."

## 5. Áp lực phải nối với sức gõ

Áp lực không được chỉ đến từ "quái tới nơi". Mỗi game phải có **áp lực liên tục**, tỉ lệ với thời gian quái còn sống:

- quái bắn xa gây sát thương nhỏ đều đặn khi còn trong tầm;
- hào quang tướng, đòn báo trước, quái phá công trình;
- vòng gần có hiệu ứng xấu cho phe ta khi quái đứng lâu.

Như vậy, gõ nhanh và chính xác hơn sẽ mất ít máu hơn một cách liên tục. Sao và biên an toàn phản ánh đúng tay nghề. Thắng hay thua đến từ các đỉnh đợt, nơi chiến thuật (bẫy, kỹ năng, chọn mục tiêu) quyết định.

## 6. Bot giống người

Bot phải chơi như người, không như máy. Mỗi bot là một bộ tham số:

| Tham số | Ý nghĩa |
|---|---|
| E, a | Tốc độ và độ chính xác mỗi phím |
| CV | Độ đều: thời gian mỗi từ có nhiễu theo log-normal |
| Nhận từ | Độ trễ phím đầu theo độ quen: đã thuộc 0,35–0,6 s · đang học 0,5–0,9 s · mới 0,8–1,6 s |
| Sửa lỗi | Xác suất Backspace sau lỗi; xác suất bỏ khóa |
| Chọn mục tiêu | Tỉ lệ chọn quái nguy nhất / quái gần nhất / từ nhìn thấy trước |
| Chú ý | Tốc độ rơi khi đông; thời gian "nhìn" khi đặt món hay mở bảng |
| Chiến thuật | Kém / Vừa / Tốt: thứ tự mua, chỗ đặt, dùng kỹ năng sớm hay muộn |
| Mệt | Tốc độ tụt x % mỗi 10 phút |

### Bộ bot chuẩn

| Bot | E | a | CV | Chiến thuật | Đại diện |
|---|---|---|---|---|---|
| Trẻ em | 15 | 88 % | 0,40 | Kém | Hồ sơ trẻ em |
| Mới | 25 | 92 % | 0,35 | Vừa | Người mới tập gõ |
| Chậm chắc | 25 | 99 % | 0,20 | Vừa | Gõ chậm nhưng chuẩn |
| **Chuẩn** | 35 | 95 % | 0,25 | Vừa | Người chơi tham chiếu |
| Khá | 50 | 96 % | 0,20 | Tốt | |
| Ẩu | 50 | 85 % | 0,35 | Vừa | Gõ nhanh nhưng ẩu |
| Nhanh | 70 | 97 % | 0,15 | Tốt | Người gõ giỏi |
| Không gõ | 0 | — | — | Tốt | Kiểm "gõ là sức chính" |
| Chỉ gõ | 35 | 95 % | 0,25 | Không mua | Kiểm "hỗ trợ cần thiết" |

- **Hiệu chỉnh bằng người thật:** mỗi lần chủ dự án chơi thử, game xuất nhật ký (hồ sơ và chỉ số). Bot cùng E và a chạy lại cùng ải; chỉ số của bot phải lệch người thật ≤ 15 %. Lệch hơn thì sửa tham số bot trước, rồi mới chỉnh game.

## 7. Cổng cân bằng chung

Mỗi game chạy ma trận **bot × chế độ × seed** (≥ 20 seed) trên mọi ải mẫu. Bộ điều nhịp bật, trừ khi ghi khác.

| # | Cổng | Ngưỡng |
|---|---|---|
| B1 | Cùng vùng cuốn | Ở chế độ Cân bằng, mọi bot từ Mới tới Nhanh nằm trong dải đích mục 3 (thắng, S, P, I, O) |
| B2 | Không quá dễ | Không bot nào có S trung vị ≥ 90 % kèm I ≥ 20 % ở Cân bằng |
| B3 | Không quá khó | Bot Mới thắng ≥ 70 % ở Cân bằng; bot Trẻ em thắng ≥ 85 % ở Thư giãn |
| B4 | Chuẩn thắng ẩu | Bot Chậm chắc có S cao hơn bot Ẩu cùng ải; bot Chuẩn hạ quái nhanh hơn bot Ẩu |
| B5 | Gõ là sức chính | Bot Không gõ thua ở mọi chế độ trừ Thư giãn của Lời Gọi (thiết kế riêng của game đó) |
| B6 | Chiến thuật có nghĩa | Cùng E và a, chiến thuật Tốt hơn Kém ≥ 10 điểm % thắng ở Cân bằng và Thử thách |
| B7 | Bộ điều nhịp nhẹ tay | Trung bình ≤ 3 bậc mỗi đợt; tổng khoảng sinh trong ±15 %; tắt nó thì bot Chuẩn vẫn ở trong dải đích (chỉ bot lệch xa mới cần nó) |
| B8 | Học không bị lấn | Cổng học riêng của game vẫn đạt ở mọi bot |
| B9 | Khớp người thật | Sau mỗi buổi chơi thử: chỉ số bot cùng hồ sơ lệch ≤ 15 % |

## 8. Kiến trúc

- **Kit chung `shared/game-kit/balance/`** (TS thuần, tất định, có test):
  - `SkillProfile`: lưu, trộn, độ tin của 13 yếu tố.
  - `FlowMeter`: tính P, I, O, S, N, Q theo cửa sổ.
  - `PaceDirector`: bậc, trễ, trần, nhật ký `pace`; game cấp bảng "bậc nghĩa là gì".
  - `HumanTypist`: mô hình gõ của bot (mục 6).
  - `effectiveE`, `paceK` và bảng dải đích mục 3.
- Mỗi game nối kit vào sim của mình, cấp bảng bậc riêng, và in báo cáo cân bằng theo mục 3 và 7.

## 9. Áp dụng cho từng game

### 9.1 Rồng Giữ Ải (thay D06 và k_E ở 00 §4.4)

- **Nhịp k hai chiều** theo mục 4.1. Người 60 WPM không còn thắng dễ ở Cân bằng.
- **Vùng Chữ tính bằng thời gian** thay cho 26 m cố định. Thời gian tiếp cận T_a của một quái Nhỏ ở nhịp k = 1 đặt sao cho bot Chuẩn hạ nó ở Q ≈ 55–70 % đường. Quái nhanh có T_a ngắn hơn, nhưng vẫn ≥ 2 lần thời gian gõ một từ của người đó.
- **Áp lực liên tục** theo mục 5: Yêu Rêu Cung, Ong Gai bắn Bệ Rồng khi trong tầm; Heo húc gây sát thương khi tới; hào quang tướng làm quái nhanh hơn. Máu Hỏa Long đặt sao cho bot Chuẩn còn S 35–65 %.
- **Kỹ năng vùng không quét sạch:** mỗi kỹ năng vùng (Thiên Hỏa, Phun Lửa) gây ≤ 15 % tổng sát thương cả ải; cụm bầy chịu tối đa 60 % máu cụm từ một đòn vùng.
- **Kinh tế chặt:** vàng ải chỉ đủ phủ khoảng một đỉnh của một đường; chọn món là quyết định thật (cổng G14 giữ nguyên).
- **Bậc của bộ điều nhịp:** khoảng sinh ± 7 %, một thuộc tính tinh anh, dời đỉnh, quãng lặng, rơi bình máu khi gần thua.
- Cổng G1–G3 của 00 §7 đọc theo dải mục 3 và cổng B1–B9 ở trên.

### 9.2 Lời Gọi

- Đã có ngân sách chú ý (≤ 8 s gõ mỗi 20 s) và bốn chế độ. Bổ sung: hồ sơ năng lực, FlowMeter cho Ngày và Đêm, nhịp k cho tần suất lời gọi và cường độ Đêm.
- Bộ điều nhịp chỉ đổi cường độ Đêm (khoảng sinh, một tinh anh) và tần suất lời gọi Ngày, trong ngân sách chú ý.
- Cổng 4–7 của BUILD_1A6 giữ nguyên. Thêm B1–B9 với bộ bot chuẩn.

### 9.3 Tuyến Cuối

- Bot 25 WPM đang thắng 11/24: thêm nhịp k cho tốc sinh, tốc quái và kích thước đỉnh tràn, để bot Mới thắng ≥ 70 % ở Cân bằng.
- Bộ điều nhịp đổi kích thước đỉnh tràn, khoảng sinh, một tinh anh; không đổi máu quái đang sống.
- Thêm các chế độ Thư giãn, Cân bằng, Thử thách cho 600 ải. Lời Thề và xếp hạng tắt bộ điều nhịp.

## 10. Lộ trình

1. Kit `balance` với test (hồ sơ, FlowMeter, bộ điều nhịp, bot gõ giống người).
2. Rồng Giữ Ải: nối kit, làm 9.1, báo cáo và cổng mới; chạy lại bot cả ma trận.
3. Tuyến Cuối: nối kit, làm 9.3.
4. Lời Gọi: nối kit, làm 9.2.
5. Màn Hồ sơ gõ và dòng cài đặt "Nhịp tự điều" ở cả ba game.
6. Chủ dự án chơi thử; xuất nhật ký; hiệu chỉnh bot (B9); chỉnh số trong dữ liệu.
