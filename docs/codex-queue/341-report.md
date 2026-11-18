# Phiếu 341 · Bộ lễ A trên thân 340 · 12/11/2026

Đã tạo đủ **4 loại ảnh + prompt nguyên văn + tấm ghép A/C**, giữ thêm **2 ảnh vẽ lại**. **Chưa nghiệm thu chất lượng:** đường xẻ từ hông còn đọc như nẹp, nền trong vùng sinh chưa đồng nhất hoàn toàn, chưa xác minh được mốc gối giải phẫu. Không sửa mã, không chạy build/test, không mở cổng mạng, không ghi Git; không sửa hoặc xóa tài sản có sẵn trước phiếu.

## File và thân chuẩn

Đã đọc [báo cáo 340](340-report.md). Phiếu 340 đã kết thúc với đủ ảnh, nhưng báo cáo của nó tự ghi chưa đạt để chuyển Tripo. Phiếu này dùng đúng các bản **try1** mà đề bài 341 chỉ định làm thân chuẩn, không tự đổi sang bộ được đề nghị trong báo cáo 340.

Trong `H = games/immortality-cultivation/art-src/heroine/`:

- `outfit-a-turnaround.v1-try1.png`, `outfit-a-front.v1-try1.png`, `outfit-a-back.v1-try1.png`, `outfit-a-left.v1-try1.png`: đủ bốn tên yêu cầu.
- **Bộ đề nghị chủ xem:** `outfit-a-turnaround.v1-try2.png`, `outfit-a-front.v1-try1.png`, `outfit-a-back.v1-try2.png`, `outfit-a-left.v1-try1.png`.
- Mỗi PNG có `<tên bỏ .png>.prompt.txt` cạnh nó; cả sáu prompt đều liệt kê 10 chi tiết A và câu **“same body, face, hair, diadem, height and A-pose as the reference turnaround”**.
- [outfit-a-341-sheet.jpg](../../games/immortality-cultivation/art-src/heroine/outfit-a-341-sheet.jpg): trước/sau của C và A, người cùng cao 480 px; ô người cao 66 px và bản phóng 4×; tờ xoay A thu nhỏ. Có `outfit-a-341-sheet.prompt.txt` mô tả phép ghép cơ học.
- `outfit-a-341-measurements.json`: số đo ImageMagick, bbox từng cột, màu góc, phần nền xanh chuẩn/gần chuẩn, nguồn gốc ảnh và phép chuẩn hóa.

Đã mở đủ 7 tham chiếu được giao bằng `view_image`: bốn ảnh thân 340, hai hướng A và chân dung Kiếm Tu. Chỉ dùng ảnh riêng của repo. Lời gọi sinh tờ đầu có prompt ghi nguồn gốc cả 7 ảnh; sau lỗi giới hạn 5 tệp đính kèm, lời gọi thành công chỉ đính kèm **bốn ảnh 340 + dir-a-front.v1-try2.png**, tương ứng ảnh 1–5 trong prompt. Hai nguồn 6–7 đã được xem nhưng **không đính kèm ở lượt đó**. Tờ try2 dùng thêm hướng sau A và chân dung. Mỗi lượt còn lại đính kèm đúng 5 ảnh được liệt kê trong prompt.

## Hạn mức và vẽ lại

**7 lời gọi image_gen:** 1 lỗi kiểm tra tham số (quá 5 đường dẫn, không sinh ảnh), 4 ảnh gốc, 2 lượt vẽ lại. Dừng ở trần 7 kể cả lời gọi lỗi; không dùng lượt thứ 8. **14 ảnh được mở bằng view_image**: 7 tham chiếu, 6 PNG sinh ra và 1 tấm ghép. Không gọi agent hay giám khảo ngoài.

Hai lượt vẽ lại:
1. Tờ xoay try2: sửa hai đuôi lưng thành một cặp ở phía sau, làm tấm sau riêng rõ hơn, yêu cầu ấn phượng thêu phẳng và đường xẻ hông mở. Điểm hợp đồng ước tính trước sửa 7,3; sau sửa 7,6. Khe xẻ vẫn chưa đủ thuyết phục.
2. Sau try2: sửa ảnh sau yếu về nhất quán vì try1 biến ấn tròn thành mảng thêu không tròn; đã khôi phục đường viền tròn. Cảm giác phù hiệu cứng vẫn còn.

Không gặp HTTP 429, thông báo hết quota hoặc giờ phải chờ. Đã giao đủ loại file; không tự mở một vòng sinh tiếp.

## Kiểm cơ học bằng ImageMagick 7

Dùng `/opt/homebrew/bin/magick`; nhận nền quanh `#00FF00` bằng fuzz 12%, lấy bbox alpha ở ngưỡng 50%. Chỉ cắt phần nền trống, đổi kích thước **đồng đều toàn người** rồi thêm khung xanh để khớp khổ/chiều cao 340. Không kéo giãn từng chi, không nắn cơ thể, không vẽ sửa áo. Gốc sinh còn nguyên tại đường dẫn `generated_images` ghi trong JSON.

| Ảnh A | Khổ px | Người cao px | So chiều cao 340 | Lề trái / phải / trên / dưới (%) |
|---|---:|---:|---:|---|
| Tờ try1 | 2048×1152 | 876 | 0% toàn bộ | 13,82 / 13,82 / 11,98 / 11,98 |
| **Tờ try2** | **2048×1152** | **876** | **0% toàn bộ** | **13,92 / 13,92 / 11,98 / 11,98** |
| Trước try1 | 1152×1536 | 1152 | 0% | 25,00 / 25,09 / 12,50 / 12,50 |
| Sau try1 | 1152×1536 | 1152 | 0% | 24,39 / 24,48 / 12,50 / 12,50 |
| **Sau try2** | **1152×1536** | **1152** | **0%** | **24,48 / 24,48 / 12,50 / 12,50** |
| Trái try1 | 1152×1536 | 1152 | 0% | 38,45 / 38,54 / 12,50 / 12,50 |

Bốn cột trước/trái/sau/phải: 340 cao **874 / 873 / 876 / 873 px**; A try2 cao **871 / 870 / 876 / 870 px**. Sai lệch theo cột tối đa **0,344%**; chênh giữa bốn cột A **0,685%**. Đỉnh búi A ở y=142/144/138/144; đế giày y=1012/1013/1013/1013, cùng đường trong 1 px. Đạt chiều cao ≤3% và lề ≥8%. Số đo sau chuẩn hóa **không tự chứng minh** cùng thân giải phẫu.

**Nền:** bốn góc của cả sáu PNG đều RGB **(0,255,0)**. Phần sinh nằm trong bbox vẫn có xanh hơi khác; ranh khung có thể thấy khi nhìn kỹ. Tỉ lệ pixel xanh đúng tuyệt đối / xanh gần chuẩn trên toàn khung: tờ try2 **45,12% / 78,37%**, trước **62,57% / 85,33%**, sau try2 **61,72% / 83,80%**, trái **82,75% / 89,65%**. Đây không phải tỉ lệ màu trang phục. **Chưa đạt nền toàn phần đồng nhất #00FF00.** Không thấy bóng đổ mặt đất; nguồn sáng được yêu cầu trên phải 45°, chưa xác thực góc sáng bằng hình học.

### Mốc vai, eo, gối

Đối chiếu ảnh đã chuẩn hóa, dùng tọa độ pixel ImageMagick. Phải tách mốc vải nhìn thấy khỏi khớp xương bị che:

| Mốc nhìn thấy | 340 → A | Chênh / chiều cao 1152 px | Kết luận |
|---|---|---:|---|
| Mép trên cổ/vai trước, hàng đầu có bề ngang >300 px | y455 → y456 | 1 px = 0,087% | Đạt cho **mốc vải**, chưa phải tâm khớp vai |
| Mép trên cổ/vai sau, cùng cách dò | y455 → khoảng y454–455 | ≤1 px = 0,087% | Đạt cho mốc vải |
| Mép trên đai eo trước, dải chàm tại x518–636 | y609 → y611 | 2 px = 0,174% | Đạt cho mốc đai |
| Mép trên đai eo trái, dải chàm tại x510–550 | y610 → y611 | 1 px = 0,087% | Đạt cho mốc đai |
| Eo sau | Bị ấn/kiếm che ở bộ 340 | Chưa đo độc lập | Không gán số giả |
| Tâm khớp vai / đường gối giải phẫu | Áo che; gối cũng bị quần 340 che | Chưa xác minh | **Chưa chứng nhận ≤3%** |

Cổ/vai trước tại y460 rộng **315 → 333 px** (+5,7%); sau **314 → 339 px** (+8,0%). Đây là độ rộng **trang phục**, đúng hướng vai A rộng hơn C; không coi là thay đổi bề ngang thân. Khuôn mặt, búi tóc và diadem giữ được ý chính nhưng vẫn có sai lệch nét nhỏ do sinh lại, chưa thể gọi khóa danh tính tuyệt đối.

## Bảng nhất quán 10 chi tiết × 4 góc

Đối chiếu bộ đề nghị xem; góc phải chỉ lấy từ tờ try2. “Khuất” không có nghĩa thiếu. “Có” chỉ xác nhận hình nhìn thấy, không tự động xác nhận toàn bộ cấu tạo.

| Chi tiết A | Trước | Trái | Sau | Phải (tờ) |
|---|---|---|---|---|
| 1. Áo ngũ thân ngà dài bắp chân, ba tấm xẻ từ hông | Có ba vùng tà; **khe chưa rõ** | Có nẹp/gap chàm; **khe chưa rõ** | Có tà; **chưa loại trừ váy liền** | Tương tự trái |
| 2. Tấm sau rời tới gối | Khuất | Có cạnh rời | Có tấm chàm riêng | Có cạnh |
| 3. Cổ Nhật Bình chữ nhật chàm, rìa ngà/vàng rộng, vai vuông | Có, rộng hơn 340 | Có cấu tạo vắt vai | Có, rộng hơn 340 | Có |
| 4. Đai gấm chàm, trang sức vàng cũ | Có | Có | Có | Có |
| 5. Ngọc bội trắng bên trái | Có, bên phải ảnh | Có | Có, bên trái ảnh | Khuất |
| 6. Đúng hai đuôi lưng dài tới gối | Khuất phía sau; không thêm cặp trước | Có một, một khuất | Có hai | Có một, một khuất |
| 7. Tay bó từ khuỷu, tay trống, A-pose | Có | Có, A-pose chiếu cạnh | Có | Có |
| 8. Viền gấu mây hạc dày | Có | Có | Có | Có |
| 9. Ấn phượng lớn trên tấm sau; kiếm thấp xương cùng | Khuất | Có cạnh ấn và đầu vỏ | Có; ấn tròn nhưng vẫn như phù hiệu; kiếm không thấy xuyên vải | Có cạnh/chuôi |
| 10. Quần chàm bó cổ chân, giày cao cổ, ngà/chàm/vàng | Có phần dưới; quần phần trên bị tà che | Có phần dưới | Có phần dưới | Có phần dưới |

Sau thật là sau: chỉ thấy sau búi tóc, gáy và mặt sau áo; không có mặt, mắt hay khóa ngực. Kiếm thấp và nghiêng nhẹ, chuôi về bên phải người; **10° chưa đo xác thực**. Vị trí phía trước tấm vải là hợp lý qua hình; không thể kiểm va chạm 3D từ tranh.

Tỉ lệ màu 60/30/10 được yêu cầu ở mọi prompt và theo hướng chung; chưa tách vật liệu để xác nhận tỉ lệ diện tích chính xác. Họa tiết chi tiết vẫn đổi nét giữa ảnh riêng và tờ xoay, dù các mảng chính nhất quán.

## Ô 66 px, tự chấm và phần chủ cần xem

Tấm ghép có ô **người cao đúng 66 px**, kèm phóng 4× bằng nearest-neighbour cho C sau và A sau. Lượt mở tấm ghép trong ngân sách 14 ảnh phát hiện lỗi tọa độ ghép ở các ô nhỏ; đã sửa lệnh đặt gravity tường minh và kiểm pixel các góc ô bằng ImageMagick. Không mở ảnh lần thứ 15. Vì vậy **chưa tự nghiệm thu cảm nhận bằng mắt ở ô 66 px sau sửa**.

**Phân biệt đồng thời lưng và vai với C ở 66 px: KHÔNG / chưa chứng minh.** Mảng chàm kéo dài sau lưng A tạo khác biệt cấu trúc rõ ở ảnh lớn; vai sau chỉ rộng thêm khoảng **1,43 px** khi người cao 66 px, nên chưa đủ bằng chứng phân biệt vai ổn định. Chủ cần xem hai ô thật trên tấm ghép; bản phóng chỉ giúp soi pixel.

| Mặt tự chấm bộ sau sửa | Điểm / 10 | Điểm còn yếu |
|---|---:|---|
| Cùng thân với 340 | 8,0 | Mốc nhìn thấy gần khớp; khớp vai/gối và nét mặt chưa khóa tuyệt đối |
| Đúng hợp đồng trang phục | **7,6** | Khe xẻ hông chưa rõ; ấn còn giống phù hiệu; cấu tạo tấm sau trên tranh chưa đủ chứng minh mesh |
| Khác C ở lưng và vai | 7,8 | Lưng khác ở tấm dài; vai chỉ rộng vừa phải, chưa chứng minh ở 66 px |
| Sang, cuốn hút | 8,3 | Vật liệu và thêu phong phú, còn lặp mô típ và màu hơi ấm |
| **Mặt yếu nhất** | **7,6** | Đã dùng lượt vẽ lại; không nhận là đạt 8 hay 8,5 |

Tự chấm này không thay hai giám khảo mù hoặc nghiệm thu trong play host. Chưa chuyển Tripo, chưa dựng mesh, chưa tích hợp game. Chủ xem **tấm ghép, tờ try2 và sau try2**, đặc biệt khe xẻ hông, hình tròn ấn phượng, độ rộng vai và ô 66 px. Không bỏ loại ảnh nào; phần bỏ qua là đo khớp bị che và xác nhận chất lượng không có đủ bằng chứng, đã ghi rõ ở trên.

