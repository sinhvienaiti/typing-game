# Giám khảo mù Q: Phong Lang (sói linh bị ô nhiễm), D02 và D01

Thứ tự xem: D02 trước, D01 sau. Chỉ xem hai ảnh, không đọc tài liệu dự án.

---

## D02

### Thấy gì
Một con sói nhìn chéo ba phần tư từ phía trước bên trái, camera chỉ cao hơn lưng một chút (khoảng 20°). Sói hạ thấp đầu, chân dang rộng như đang rình, nhe răng gầm gừ, mắt phát sáng tím. Phần lông trắng bạc gần như trắng tuyết, render kiểu ảnh thật (lông rất chi tiết). Trên vai và hông có các vệt đen phân nhánh như cành cây, mờ và phẳng. Nền phòng chụp màu xám xanh chuyển dần (tối ở trên, sáng hơn ở sàn, thấy rõ đường chân trời mềm). Ánh sáng chính từ trên, có bóng đổ mềm dưới bụng và chân. Con vật chiếm khoảng 80 % chiều ngang. Lề: trái khoảng 14 %, phải khoảng 8,5 %, trên khoảng 16 %, dưới khoảng 11 %.

### M (tầm thị trường): **6,9**
- Chất render lông ở mức cao, dáng rình hạ đầu và miệng gầm có sức đe dọa thật. Đây là điểm mạnh nhất của cả hai ảnh.
- Về thiết kế, đây chỉ là một con sói thật dán thêm hình xăm đen. Ảnh không đọc ra "sói linh của thế giới tu tiên": không có dấu ấn linh thú, không có hình khối riêng (bờm, gai sống lưng, đuôi cách điệu, ấn chú). Đặt cạnh sói của Where Winds Meet hay Black Myth: Wukong thì nó là con sói phổ thông.
- Vệt ô nhiễm không ăn vào cơ thể: không rẽ lông, không sưng, không nứt da, không đọng mực, trông như decal vẽ đè lên lông. Đề bài yêu cầu chạy dọc sống lưng nhưng ảnh không có, chỉ có hai mảng ở vai và hông.
- Màu lông gần trắng, đọc thành sói Bắc Cực chứ không phải xám tro. Ở góc nhìn 55° và cao 40 px, nó sẽ thành một vệt sáng nhợt, các vân đen mảnh chỉ còn 1–2 px và mất hẳn.
- Silhouette là silhouette sói chuẩn, không có điểm nhận diện riêng.

### T (độ hợp làm nguồn Tripo): **6,8**
- Tốt: một khối duy nhất, bốn chân tách rời rõ, đuôi tách khỏi chân sau, lề đều đạt tối thiểu, không có hiệu ứng lớn.
- Chưa đạt:
  - Camera quá thấp (khoảng 20°, không phải 30–35°), nên mặt lưng, nơi người chơi sẽ nhìn thấy, bị thu ngắn.
  - Nền chuyển màu có sàn và đường chân trời, không phải nền phẳng đồng màu.
  - Có bóng đổ.
  - Mắt phát sáng là hiệu ứng phát quang, mesh không giữ được.
  - Miệng há sâu với răng và lưỡi: Tripo thường nặn thành khối rối.
  - Lông quá "ảnh thật" sẽ thành nhiễu bề mặt trên texture.
  - Bốn bàn chân không nằm trên một mặt phẳng rõ ràng do chân dang rộng.

### Năm việc cần sửa (quan trọng nhất trước)
1. **Viết lại thiết kế ô nhiễm cho ra chất tu tiên, đủ to để đọc ở 40 px.** Cho một dải mực đen đông cứng chạy liền dọc sống lưng, từ gáy đến gốc đuôi, có gờ hoặc gai mực cứng nổi khối mà mesh giữ được. Vân lan ra vai thì làm dày, rẽ lông, da nứt dưới vân. Thêm một ấn nứt trên trán. Mục tiêu là các khối đen lớn đọc được từ trên xuống, không phải nét cành cây mảnh.
2. **Nâng camera lên 30–35°** để thấy rõ mặt lưng, vai, hông và dải ô nhiễm trên sống lưng.
3. **Đổi lông sang xám tro thật**, có tương phản sáng tối: lưng sẫm hơn, mõm và chân tối dần. Hiện tại trắng gần tuyết, ở 40 px sẽ thành vệt nhợt không tách khỏi nền đá sáng.
4. **Đổi sang nền phẳng một màu, bỏ sàn, chân trời và bóng đổ.** Chiếu sáng đều hơn (bớt key từ trên), đúng chuẩn ảnh nguồn image-to-3D.
5. **Bỏ ánh phát quang ở mắt** (tím sẽ làm trong shader của game). Khép miệng lại thành gầm gừ nhe nanh (môi cong, răng cửa lộ, không há sâu). Đặt bốn bàn chân phẳng trên một mặt sàn.

---

## D01

### Thấy gì
Cùng thiết kế sói, nhìn chéo ba phần tư lệch về phía hông trái nhiều hơn, camera khoảng 20–25° hơi cao hơn D02. Sói đứng hạ đầu, miệng hé, mắt tím phát sáng nhẹ. Lông xám bạc sẫm hơn D02 một chút, render mượt kiểu AI, ít chi tiết lông hơn. Vân đen bóng, dày, như mực hoặc dầu đông lại: một chùm cành ở vai và một mảng loang ở hông, kèm vết nứt nhỏ trên trán. Nền xám tím gần như phẳng đồng màu, có bóng đổ mềm dưới thân. Con vật chỉ chiếm khoảng 63 % chiều ngang và nằm lệch xuống dưới: lề trên khoảng 30 %, lề dưới khoảng 10 %, lề trái khoảng 17 %, lề phải khoảng 19 %.

### M (tầm thị trường): **6,5**
- Vân đen bóng và mảng loang ở hông đọc ra "mực" rõ hơn D02, gần đề bài hơn. Lông xám hơn, gần "xám tro" hơn.
- Thế nhưng biểu cảm yếu: miệng hé như đang thở, không gầm, tai dựng bình thường, không xù lông gáy, nên độ đe dọa thấp hơn D02 rõ rệt.
- Render mượt, nhựa và kém chi tiết hơn, có cảm giác ảnh AI tầm trung.
- Thiết kế vẫn là sói thật cộng decal, không có dấu ấn linh thú tu tiên. Vân vẫn chưa chạy dọc sống lưng.
- Silhouette chuẩn sói, đuôi rủ sát chân sau nên mất một mảng nhận diện.

### T (độ hợp làm nguồn Tripo): **6,4**
- Tốt: nền gần phẳng đồng màu (tốt hơn D02), không có sàn hay chân trời rõ. Vân bóng nổi có thể cho chút khối trên mesh. Lề đều rộng.
- Chưa đạt:
  - Con vật quá nhỏ trong khung (khoảng 63 % ngang, lề trên 30 % bỏ phí), nên Tripo nhận ít điểm ảnh cho chi tiết.
  - Đuôi rủ đè lên chân sau phải, gần như dính thành một khối: rủi ro mesh dính đuôi vào chân rất cao.
  - Camera vẫn thấp hơn 30–35°.
  - Có bóng đổ.
  - Mắt phát sáng.
  - Miệng hé có lưỡi và răng.

### Năm việc cần sửa (quan trọng nhất trước)
1. **Tách đuôi khỏi chân sau**: đuôi hơi nhấc và chĩa ra sau, xa chân, có khoảng nền rõ giữa đuôi và chân. Hiện tại đây là lỗi mesh nặng nhất.
2. **Phóng to con vật cho chiếm 80–85 % khung**, căn giữa theo chiều dọc, cắt bỏ khoảng trống 30 % phía trên (giữ lề 6–8 % mỗi bên).
3. **Sửa biểu cảm và dáng cho có sức đe dọa**: tai cụp ra sau, lông gáy và lông dọc sống lưng dựng, môi cong nhe nanh, thân rình thấp như D02 nhưng miệng không há sâu.
4. **Giữ chất vân mực bóng nhưng viết lại thành thiết kế tu tiên**: dải mực đông cứng liền mạch dọc sống lưng có gờ hoặc gai nổi khối, vân vai làm dày hơn, ấn nứt trán rõ hơn. Tất cả phải đọc được từ trên xuống ở 40 px.
5. **Nâng camera lên 30–35°, bỏ bóng đổ, bỏ ánh phát quang ở mắt**, render chi tiết lông và chất liệu sắc hơn (bớt bề mặt nhựa mượt).

---

## Bảng tổng kết

| Ảnh | M | T | Kết luận một dòng |
| --- | --- | --- | --- |
| D02 | 6,9 | 6,8 | Sói thật render đẹp, dáng rình đe dọa tốt, nhưng chỉ là sói dán decal, lông gần trắng, camera thấp, nền chuyển màu có bóng đổ. |
| D01 | 6,5 | 6,4 | Vân mực bóng hợp đề hơn và nền phẳng hơn, nhưng con vật quá nhỏ trong khung, đuôi dính chân sau, biểu cảm yếu, render nhựa. |

Nếu buộc phải chọn, tôi gửi D02 cho Tripo vì khối hình rõ hơn, đuôi tách chân và con vật chiếm đủ khung. Cả hai đều không đạt 8,5 ở cả M lẫn T.
