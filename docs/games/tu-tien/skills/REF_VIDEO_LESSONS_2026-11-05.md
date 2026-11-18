# Học từ video quảng cáo "Khế Ước Rồng" (05/11/2026)

**Anh (05/11 22:05):** "tôi muốn bạn xem video này, và đánh giá những kỹ năng mà chúng ta có thể học hỏi để làm theo".

**Nguồn:** `~/Downloads/1793890576259_…mp4`, 47 giây, quay màn hình điện thoại một quảng cáo game nhập vai mobile; vùng chơi chỉ 480×272.

**Cách xem:**
- Claude xem toàn bộ (8 tấm ghép, 3 khung mỗi giây), đo nhịp từng chiêu ở 8 khung mỗi giây và so với lab phím 8.
- Hai agent Claude đọc độc lập, không thấy kết luận của Claude: một theo tay nghề VFX, một theo cảm giác đánh và độ hợp với game gõ chữ của mình.
- Claude kiểm lại những gì agent nói về code của mình: `damage-compile.ts`, `telegraphs.ts`, `pickups.ts`, `ban-quyet.ts`; trong `src/audio` không có hạ nhạc.
- Khung hình ở `typing-game-review/captures/tu-tien/ref-video-0511/`; 12 khoảnh khắc ở `owner-review/2026-11-05/tu-tien/ref-video-lessons/highlights-12.jpg`.

**Luật:** chỉ học cấu trúc và nhịp. Không đưa khung hình này cho AI nào làm tham chiếu, không chép tên hay hình. Mọi hình vẫn làm từ ảnh của mình anh đã duyệt.

## 1. Đánh giá chung

- **Điểm:** cả hai bên đều chấm khoảng **7/10** so với VFX game nhập vai mobile thương mại. Hai món mạnh nhất (mưa sao băng chéo, cột sáng vàng) khoảng 8/10.
- **Kỹ năng không có gì lạ:** cầu lửa, ấn lửa nổ, mưa sao băng, cột sáng, luồng lửa duy trì, rồng năng lượng, ba vết vuốt. Mình đã có hoặc đã lên danh sách gần hết.
- **Video bán sức mạnh bằng cách khác:** một con số combo to lớn dần tới 699, nhịp lên–nghỉ–lên, có báo trước mỗi cú lớn, đất còn cháy sau đòn, và một cao trào đánh boss.
- **Điểm yếu cần tránh:**
  - Chiêu của người chơi và đòn boss cùng một màu đỏ cam, trên thảm hồng.
  - Sáng gần trắng xóa 1–2,5 giây liền, che cả nhân vật lẫn boss.
  - Phía người tung chiêu gần như trống.
  - Tắt nhanh 0,3–0,4 giây sau khi giữ đỉnh.
  - Boss chết rất nhạt.
  - Bảng nhận đồ che giữa màn trên, đúng chỗ quái và chữ của mình đi vào.

## 2. Nên học (có số đo)

| # | Bài học | Video làm thế nào | Mình đang có | Làm cho Tu Tiên | Ưu tiên |
|---|---|---|---|---|---|
| 1 | **Báo trước cú từ trời** | Kim sáng mảnh từ trời cắm xuống, vòng sáng mở trên đất 0,5–0,8 s trước sao băng; cột sáng có chớp sao 4 cánh 0,3–0,4 s trước | Chưa có (phím 8 đánh luôn) | Gõ xong từ: chỉ sáng mảnh + ấn trên đất (từ tranh đã duyệt) đánh dấu từng con 0,15–0,25 s rồi mới giáng. Ấn nằm dưới quái, không ở tầm chữ | Cao |
| 2 | **Đánh chéo từ trời** | 3–6 sao băng vào chéo từ một góc trên, cách nhau 0,2–0,35 s, từ trời xuống đất 0,13–0,25 s | Phím 8 chỉ đánh thẳng đứng | Thêm dạng sao băng nghiêng 15–25°, đuôi ngắn (≤ 2 m), mỗi con trúng một con quái được đánh dấu, tối đa khoảng 8 con một lúc, cả trận mưa ≤ 2,5 s. Cột trụ vẫn thẳng đứng như anh dặn | Cao |
| 3 | **Đất còn cháy sau đòn** | Sau loạt sao băng, đất cháy 1,5–2 s rồi còn than hồng và vết cháy | Clip phím 8 tắt gần như ngay sau đỉnh | Mỗi cú chạm để lại vết cháy hay vết nứt từ tranh vẽ, kèm 6–12 hòn than, tan dần (erosion) 1,5–2,5 s; giới hạn số vết khi đông | Cao |
| 4 | **Vòng xoáy trên đất ở chỗ trúng** | 2–3 lưỡi liềm lửa xoay phẳng quanh con bị trúng, 0,4–0,6 s, bán kính đúng vùng sát thương | Có vòng chạm, chưa xoay, chưa khớp bán kính | Lớp chạm cho chiêu vùng: liềm xoay một vòng mỗi 0,5 s, bán kính lấy từ bán kính trúng thật, để người chơi đọc được vùng | Cao |
| 5 | **Một con số làm "nhân vật chính"** | Số combo to, nét nghiêng, vệt mực đỏ sau lưng, sáng lên mỗi lần tăng, 4 → 699 | Không có. Kit có `multiplierForStreak` nhưng không HUD nào dùng | **Chuỗi từ sạch** (Tốt trở lên); Chớp và Hoàn hảo thêm chớp vàng; gõ Ẩu thì tan như mực, không tắt bụp. Mốc 10/25/50/100 nâng độ rực của chiêu. **Cần anh quyết** (mục 4) | Cao |
| 6 | **Nhịp lên–nghỉ–lên** | Bùng 3–4 s, nghỉ 3–5 s, cao trào ở boss | Có sóng nóng và nguội (`director.ts`), có nghỉ đợt | Đợt 1 chiêu đơn, đợt 2 chiêu vùng, tinh anh hay boss thì tuyệt kỹ hệ; mọi cảnh phủ cả màn ≤ 2,5–4 s để chữ quay lại | Vừa |
| 7 | **Cột sáng làm đòn kết** | Cột vàng giữ 0,9–1,2 s, dưới chân có đĩa vàng và tia; trên boss có thêm cánh lửa xòe trên đất | Có (phím 8: Thiên Phạt) | Lõi trắng ≤ 25 % bề ngang, thân ≤ 0,9 mỗi kênh, có sợi hay phù văn chạy bên trong cho khỏi phẳng; tắt bằng erosion 0,6–0,8 s, không tắt trong 0,3 s như video | Vừa |
| 8 | **Ba vết song song** | Ba lưỡi liềm hay vuốt đỏ cam xếp song song | Lưỡi liềm đều 14 hệ (vừa duyệt) | Chiêu bắn 3 lưỡi liềm đều song song (mỗi lưỡi một cú, một tia lửa), vết trên đất giữ 0,6 s rồi tàn chậm | Vừa |
| 9 | **Cảnh báo đòn boss** | Vẽ viền trước, rồi lấp đầy từ nguồn, rồi đánh đúng hình đó; đòn kéo vệt dài trên sàn | Có, còn tốt hơn: `telegraphs.ts` tô đỏ #FF4A4A, có sọc, viền, dấu "!", có từ để gõ trả lời | Thêm: viền sáng lên trong 0,3 s cuối; sau đòn còn sương đỏ mờ khoảng 1 s; né được thì bóng mờ lướt ra và chữ "Dodged". Giữ khung cảnh báo ≥ 1,4 s (video chỉ 0,5–0,7 s, quá ngắn với người gõ) | Vừa |
| 10 | **Luồng duy trì theo nhịp gõ** | Luồng lửa xoáy đổ vào boss khoảng 2 s, rất nhiều cú | Chưa có: chiêu của mình là từng phát | Chiêu duy trì: mỗi từ đúng nối thêm 0,8–1 s và một nhịp đập; gõ sai thì luồng tàn chậm. Luồng hẹp (≤ 1 m), ≤ 60 % đục trên quái. **Cần anh quyết** (cơ chế mới) | Vừa |
| 11 | **Lặng trước cú lớn** | Tiếng nhỏ hẳn 0,3–0,5 s ngay trước vài cú lớn (có thể chỉ do nhạc quảng cáo) | Không có (`src/audio` không có hạ nhạc) | Hạ nhạc và nền 6–8 dB trong 0,25–0,4 s trước tuyệt kỹ, lúc Thú Vương ra và cú đánh của boss | Vừa |
| 12 | **Số sát thương** | Số nhỏ, ba màu, chồng nhau | Có, chặt hơn: gộp mỗi 125 ms, tối đa 8 số, né chữ, chí mạng viền vàng | Chỉ thêm dòng "×N hits" dưới số tổng của chiêu nhiều cú | Thấp |
| 13 | **Ngọc rơi bay về** | Ngọc tím có biểu tượng bay về nhân vật | Có Linh Sa bay về ô HUD (`pickups.ts`) | Ngọc theo độ hiếm cho đồ hiếm, có hào quang; bay về ô HUD, không bay qua vùng chữ | Thấp |
| 14 | **Boss lộ diện trước** | Boss đứng xa từ đợt trước, im lặng rồi mới vào | Có thẻ Thú Vương ở đợt nghỉ | Cho Thú Vương đứng ở mép sân (không chữ, không đánh được) ở đợt trước; rồi lặng, gầm, hiện thanh máu mỏng | Thấp |

## 3. Không nên theo

- **Chữ "Chí mạng" trên mọi cú:** canon D09 không có chí mạng ngẫu nhiên. Chí mạng của mình là Chớp và Hoàn hảo; chỉ hiện chữ **FLASH** ngắn cho đúng từ đạt Chớp.
- **Bảng nhận đồ giữa màn trên:** quái và chữ của mình đi vào từ đó. Dùng dòng tóm gọn ở góc theo vùng màn hình, tối đa 3 dòng, gộp theo món; cuộn lớn để giờ nghỉ đợt.
- **Trắng xóa ở người tung chiêu, cột lửa cao trên đầu nhân vật:** che vùng quái gần nhất và chữ của nó. Phía người tung chiêu thấp và ngắn (vòng dưới chân, hào quang, hạt bay ≤ 2 m, ≤ 0,4 s), chớp ≤ 0,9 mỗi kênh, chữ luôn vẽ trên cùng.
- **Một màu cho tất cả:** mỗi chiêu một màu riêng, đỏ #FF4A4A chỉ cho cảnh báo đòn địch.
- **Xoay camera, tự đẩy gần:** vị trí chữ phải đoán được. Chỉ cho đẩy rất nhẹ (≤ 3 %) ở tuyệt kỹ và cú đập của boss.
- **Dấu cộng xanh khi hồi máu:** đổi thành nhịp sáng ngọc và hạt khí.
- **Boss chết nhạt:** của mình cần hit-stop 0,12–0,2 s ở từ cuối, khung chạm, boss tan dần thành hạt khí của hệ trong khoảng 2 s, rồi tổng kết chuỗi và phần thưởng.

## 4. Cần anh quyết

**Anh duyệt cả 3 (05/11 22:20: "Duyệt cả 3").** Đã ghi vào canon D60, D61, D62. Việc: `docs/work/tasks/streak-counter.md`, `channel-skill.md`, `slanted-meteor.md`. D60 và D61 hỏi Gemini một vòng: `docs/work/consult/streak-channel-gemini.md`.

1. **Bộ đếm chuỗi từ** (bài học 5): canon §6.6 ghi HUD trong trận "chỉ có" Sinh lực, Chân Nguyên, Trận Lực và thanh Thế, nên thêm bộ đếm là đổi canon. Đề xuất: chỉ để nhìn (không đổi sát thương), đặt ở ô màn hình riêng ngoài hành lang quái, đếm từ sạch, mốc 10/25/50/100 nâng độ rực của chiêu.
2. **Chiêu duy trì theo nhịp gõ** (bài học 10): cơ chế mới, theo luật 05/11 phải hỏi Gemini một vòng trước khi làm.
3. **Sao băng nghiêng** (bài học 2): làm thêm dạng sao băng nghiêng 15–25° bên cạnh cột trụ thẳng đứng?

## 5. Làm được ngay mà không cần duyệt thêm (code, từ mai)

- Nối phím 8 và 9 vào đường phản hồi sẵn có của phím 0–7: số sát thương, quái phản ứng, đèn chạm trên đất, hit-stop. Hiện các chiêu này chỉ là lớp video đặt trên sân, chưa nối vào sim, nên quái đứng im.
- Kéo dài pha dư âm của clip lên 1,5–2,5 s bằng erosion và vết cháy từ tranh vẽ, thay vì tắt ngay sau đỉnh.
- Ấn đánh dấu trên đất 0,15–0,25 s trước mọi cú từ trời.
- Chữ "×N hits" dưới số tổng.
