# Tu Tiên Thủ Ải: chọn cách gõ và giao diện

Map giữ nguyên. Tài liệu này tổng hợp 3 nguồn: Codex 392, Codex 392b và Gemini. Claude là người chốt.

## 1. So sánh từng câu hỏi

| Câu hỏi | Codex 392 | Codex 392b | Gemini |
|---|---|---|---|
| Gõ gì | Từ đơn trên dải kỹ năng. Quái thường không có từ. | Từ đơn trên 5 ô Bàn Quyết. Từ xoay theo hồ sơ học. | Từ trên 3–4 quái tuyến đầu, thêm từ khóa kỹ năng. |
| Cụm từ / câu | Không | Không. Chuỗi 3 từ chỉ thử cho tuyệt chiêu. | Cụm 2 từ khi WPM cao |
| Kích hoạt | Gõ đúng chữ cuối là ra chiêu, không cần Enter | Như 392. Không có mục tiêu thì giữ chiêu 3 s. | Ra ngay. Phím 1–5 khóa ô. |
| Tuyệt chiêu | Một từ 5–8 chữ | Gõ từ xong, bấm Space để tung | Gõ từ, rồi bấm Space đúng nhịp trên vòng bát quái |
| Thanh Space kiểu Audition | Không đề cập | Chỉ cho tuyệt chiêu, chỉ trong lab | Bỏ cho đòn thường. Chỉ giữ cho tuyệt chiêu. |
| Che chiến trường | Ước lượng tay 34,5% khung / 79,3% vùng giữa. Mục tiêu ≤17%. | Không đặt chữ hay thanh trên chiến trường | Nói chỉ còn 3,9%. Phép tính sai. |

## 2. Các điểm đồng ý

- Ba nguồn: mỗi từ gõ xong cho đúng một chiêu, ra ngay khi gõ đúng, không cần Enter.
- Ba nguồn: không dùng câu.
- Chỉ 392 bác bỏ hẳn việc gõ theo hàng đợi cố định (M3). 392b và Gemini không bàn điểm này.
- Các từ đang hiện có chữ đầu khác nhau, và không từ nào là tiền tố của từ khác. Code đã có luật này.
- 392b và Gemini: thanh Space không áp cho đòn thường hay 5 kỹ năng. 392b nêu lý do: nó phá nhịp gõ và tranh mắt với cảnh báo đòn đánh. 392 không nói gì về Space hay thanh thời gian.
- Chuẩn bị và chiến đấu là hai giao diện tách riêng. Mỗi lúc chỉ hiện một chế độ.
- Mọi chữ người chơi đọc là tiếng Anh.

## 3. Các điểm khác nhau, và Claude chọn gì

- **Có đặt từ lên quái không.** Gemini muốn có. Hai bản Codex không muốn. Claude chọn **không đặt từ lên quái thường**. Chỉ quái đặc biệt cần Seal hoặc Cleanse mới có nhãn, và nhãn đó dùng chung từ với dải kỹ năng. Lý do: nhãn trên quái che chiến trường và làm nhiều từ sống cùng lúc.
- **Cỡ chữ.** 392 và 392b đặt tối thiểu 28 px. Gemini đề xuất nhãn từ 18 px trong viên 22 px. Claude chọn **28 px**, vì từ nằm trên dải đáy chứ không trên quái.
- **Phím 1–5 khóa ô (Gemini).** Không chọn. Phím 1/2/3 giữ cho vật phẩm. Khóa ô bằng cách gõ chữ đầu, như code hiện tại.
- **Tuyệt chiêu.** Claude chọn phương án D của 392b, thêm một bậc thời gian tùy chọn kiểu Gemini. Gõ từ là "đã sẵn sàng". Bấm Space là "tung bây giờ". Space chỉ là thưởng: Perfect và Great tăng sức mạnh, Miss vẫn ra đòn ở sức mạnh gốc.
- **Thiếu cao trào có thể do phản hồi yếu (392b).** 392b cảnh báo rằng cảm giác thiếu cao trào có thể đến từ hiệu ứng và âm thanh yếu, không phải vì ít thao tác. Vì vậy lab phải so A có phản hồi đầy đủ trước khi kết luận cần thanh Space.
- **Lỗi gõ không chặn (Gemini).** Không chọn. Code hiện tại giữ lỗi và cho Backspace lùi. Lỗi gõ cũng là tín hiệu cho việc học.
- **Đổi dấu Telex sang phím QWERTY.** Không chọn. Gemini cho rằng NFD khôi phục đúng phím đã gõ. Điều này sai. Code hiện tại phát hiện IME và cảnh báo người chơi.
- **Phím 4 mở Learn/Review (392).** Đây là đề xuất mới, chưa có trong input-router. Để anh quyết.

## 4. Mô hình đề xuất

**Nhịp một wave**
1. Chuẩn bị: có lời mời "Learn words" (không tự bật lên), mở shop bằng Backquote. Bấm Enter để bắt đầu.
2. Cảnh báo wave 5 s.
3. Chiến đấu: kiếm bay tự đánh quái. Người chơi gõ từ kỹ năng.
4. Nghỉ giữa wave: chọn Shop hoặc Review, không hiện cả hai cùng lúc.

**Gõ gì**
- **Quái thường:** không gõ. Kiếm bay tự đánh.
- **Quái đặc biệt:** gõ từ Seal hoặc Cleanse, nối bằng một vạch ngắn với ô trên dải.
- **5 ô kỹ năng:**
  - Ô 1: từ 3–5 chữ.
  - Ô 2: từ 4–7 chữ, hồi chiêu 8 s. Nhận từ đã gặp trong trận này (theo 392b), không nhận từ hoàn toàn mới.
  - Ô 3: phòng thủ.
  - Ô 4: từ 4–7 chữ, hồi chiêu 12 s. Trong wave 1–2, đây là ô duy nhất nhận từ mới.
  - Vai trò ô giữ cố định, ví dụ nhãn "Strike". Từ thì xoay theo hồ sơ học.
- **Tuyệt chiêu (D):** khi Chân Nguyên đầy, ô 5 hiện một từ quen 5–8 chữ. Gõ xong thì ô chuyển sang "Ultimate ready · Space". Bấm Space để tung. Không có mục tiêu thì báo "No target" và không mất thanh. Luật theo 392b:
  - Tối đa một tuyệt chiêu ở trạng thái sẵn sàng.
  - Trạng thái sẵn sàng mất khi hết wave hoặc khi chết, để chặn việc tích trữ cho boss.
  - Không nhận Space bấm sớm trước khi gõ xong (không đệm phím).

**Thanh Space kiểu Audition:** chỉ dùng cho tuyệt chiêu, và thử trong lab trước. Một con trỏ quét một lần. Mọi con số dưới đây đều **chưa kiểm chứng**: quét 1200 ms, vùng Perfect 200 ms, Great 500 ms, hệ số x1.10 / x1.05 / x1.00. Hệ số này **thay thế, không nhân chồng** lên hệ số Chop (392b cảnh báo chồng lên sẽ thành x1.375). Kết quả thời gian không tính vào WPM, độ chính xác hay việc học.

**Luật phím**
- Số từ sống tối đa là 8. Ở chế độ Relaxed/Learning là 5.
- Esc nhả khóa. Backspace lùi một chữ.
- Phím 1/2/3 là vật phẩm. Space chỉ dùng cho tuyệt chiêu, và không nhận khi đang mở bảng.
- Tối đa 8 từ mới mỗi 20 phút.
- Gõ khi có gợi ý thì ghi `hintUsed:true`.

## 5. Bố cục giao diện

- Dải gõ thấp nằm trong dải đáy hiện có (khoảng 13% chiều cao), kèm một dòng nghĩa và IPA cho từ đang khóa.
- Thanh trạng thái mỏng 2,7%: Máu và Năng lượng ở trái, Lõi ở giữa, Wave / Settings / Sound ở phải.
- Shop là ngăn bên phải rộng 24%. Ngăn này thu lại khi đặt trụ để thấy đủ 6 ô.
- Mục tiêu che phủ: khi chiến đấu căng nhất, giao diện che **≤17%** khung, và không đè lên Lõi, cổng, ô trụ hay cảnh báo.
- Con số 34,5% hiện nay **chưa kiểm chứng**. Nó được đo tay bằng hình chữ nhật trên một ảnh chụp. Sẽ đo lại bằng DOM.

## 6. Hiệu ứng vòng đời của từ

Luật của 392: các từ khác luôn đứng yên và dễ đọc. Chỉ từ đang khóa được chuyển động. Các chi tiết đánh dấu *(Claude đề xuất)* chưa có nguồn nào nêu, sẽ chấm trong lab.

1. **Xuất hiện:** chữ đầu được nhấn mạnh. Từ mờ dần hiện ra *(Claude đề xuất)*.
2. **Đang gõ:** chữ đã gõ chuyển vàng, chữ kế tiếp có gạch dưới sáng. Chỉ từ đang khóa nhô lên một chút. Gõ sai thì viền lóe 150 ms. Từ đang hồi chiêu có vòng đếm và hiện mờ, không gạch dưới.
3. **Gõ xong:** phát tiếng đọc từ và âm ra chiêu. Ô hiện từ mới sau khi từ cũ đã tan. *(Claude đề xuất)*: từ tấn công bay lên, tan thành hạt sáng trong khoảng 0,6 s. Từ phòng thủ rơi nhẹ rồi mờ đi.
4. **Giữ chiêu không có mục tiêu:** ô báo "Waiting for target". Hết 3 s thì từ vỡ và mờ đi.

## 7. Bài thử trong lab cho anh

Lab có 4 lượt, mỗi lượt 75–90 s, cùng một wave, đổi thứ tự giữa các lượt:
- **A:** gõ từ kỹ năng như mục 4, phản hồi hình và tiếng đầy đủ.
- **D:** A, thêm tuyệt chiêu "gõ rồi bấm Space".
- **C:** D, thêm thanh hoặc vòng thời gian cho tuyệt chiêu.
- **B:** tuyệt chiêu bằng chuỗi 3 từ.

Sau mỗi lượt, anh chấm từ 1 đến 5 cho Kiểm soát, Thích thú và Phân tâm. Một phương án đạt khi Thích thú hơn A ít nhất 1 điểm, độ chính xác giảm không quá 3 điểm, và mỗi lượt lỡ tối đa thêm 1 lần phòng thủ. Anh nhận video so sánh và link lab kèm phím.

## 8. Câu hỏi cho anh

1. Tuyệt chiêu nên là D (gõ rồi bấm Space) hay C (D thêm vòng thời gian kiểu Audition)? Hay anh thử cả hai trong lab rồi chọn? Lưu ý: nếu A với phản hồi mạnh đã đủ cao trào thì có thể không cần thanh Space.
2. Có bỏ việc tự bật Learn/Review, thay bằng lời mời tùy chọn mở bằng phím 4 không?
3. Có cho quái đặc biệt mang nhãn từ Seal trên đầu không, hay chỉ hiện trên dải kỹ năng?

---
Nguồn: docs/codex-queue/392-report.md, 392b-report.md, docs/games/tu-tien/source/gemini-typing-gameplay-ui-2026-11-16.md. Bản nháp qua critic (FAIL), đã sửa theo các điểm phải sửa.

## Owner chốt (16/11/2026)
- Bỏ hẳn vạch chạy kiểu Audition: "chắc k cần dụng của audition vì khả năng nó không phù hợp". Tuyệt kỹ: gõ từ rồi Space để tung (D), không có vòng thời gian.
- Quái đặc biệt không mang nhãn từ trên đầu; chỉ có icon nhận biết (tinh anh, boss…).
- Quái hiện thanh máu chỉ khi đã dính sát thương (owner đề xuất). Kỹ thuật: một instanced mesh cho mọi thanh máu, vài draw call, ẩn khi đầy máu.
- Bỏ hẳn thẻ "Học trước · Từ mới của trận": "tại sao phải bật từ mới của trận làm gì, nó là vô nghĩa, đừng có đem mấy cái không phù hợp vào game như vậy". Không tự bật, không phím mở. Từ mới chỉ gặp ngay trong trận, trên ô kỹ năng, kèm một dòng nghĩa nhỏ cho từ đang gõ.
