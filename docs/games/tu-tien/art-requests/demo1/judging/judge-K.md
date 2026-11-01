# Giám khảo K: chấm mù 26 ảnh nguồn 2D cho Tripo

Thứ tự chấm: A26 lùi về A01. Mỗi ảnh có M (mức thị trường, so với concept sheet AAA/AA xianxia và fantasy: Genshin Impact, Where Winds Meet, Diablo IV, Black Myth: Wukong) và T (độ phù hợp làm nguồn Tripo). Mốc của M: 8 là bán được nhưng bình thường, 8,5 là ngưỡng nhận, 9 là hàng đầu.

Lề được đo trên file bằng cách cắt nền (fuzz 7 %), ghi theo thứ tự Trái / Phải / Trên / Dưới. Nền của cả bộ là xám phẳng RGB 221–227, không có bóng đổ, không có mặt đất.

**Lỗi chung của cả bộ:** 25/26 ảnh có ít nhất một cạnh lề dưới 6 %, thường là cạnh theo chiều dài của vật (vật được phóng cho chạm khung). Chỉ A02 đạt lề ở cả bốn cạnh. Vì nền phẳng nên sửa được bằng cách nới canvas cùng màu nền, không cần vẽ lại. Ngoài ra, các cặp nhiều góc nhìn (trước/ngang) dùng hai khổ canvas khác nhau (vuông 1024 và ngang 1024×683) nên vật không cùng tỉ lệ pixel giữa hai góc. Tripo multiview cần hai góc cùng khổ và cùng chiều cao vật.

---

## A26: phi kiếm, bản mảnh

**Thấy gì:** Một thanh kiếm thẳng đứng nhìn chính diện trực giao: lưỡi xám thép hẹp, sống giữa màu kem ánh vàng, chắn tay ba cánh như đài sen, chuôi quấn dây xanh navy, núm tròn màu ngà có mũi nhọn nhỏ. Nền xám phẳng, ánh sáng studio đều, chất liệu là CG mịn gần như chưa có texture. Lề 44 / 44 / 2,8 / 3,2 %: mũi và núm gần chạm mép trên, mép dưới.

- **M: 6,6**. Hình dáng chung chung, giống kiếm fantasy phương Tây. Chưa có dấu ấn tiên hiệp (ngọc khảm, vân mây, kiếm tuệ). Chất kim loại phẳng, không có độ sâu.
- **T: 6,3**. Chỉ một góc chính diện nên Tripo không biết độ dày và mặt cắt lưỡi. Lề trên, dưới không đạt. Chắn tay cánh mỏng.

Sửa:
1. Nới lề trên, dưới lên ≥ 8 %.
2. Thêm góc 3/4 hoặc góc nghiêng 90° cho thấy độ dày lưỡi, sống kiếm và mặt cắt hình thoi.
3. Thêm nhận diện tiên hiệp: chắn tay vân mây hoặc đầu thú, ngọc bích khảm ở chắn và núm.
4. Phân vùng chất liệu: thép có vệt mài và rãnh máu khắc hoa văn, tách hẳn khỏi phần kim loại màu kem.
5. Làm dày cánh chắn tay và mũi núm để lưới 3D giữ được.

## A25: phi kiếm, bản rộng

**Thấy gì:** Thanh kiếm rộng bản nhìn chính diện: lưỡi màu kem trắng, viền xám, rãnh giữa xanh navy, chắn tay hai cánh cong rộng, chuôi quấn xanh, núm ngà. Nền xám phẳng, ánh sáng đều. Chất liệu trông như nhựa hoặc xương sơn, không ra thép. Lề 35 / 35 / 2,6 / 3,1 %.

- **M: 6,4**. Lưỡi kem đọc thành đồ chơi hay kiếm gỗ. Rãnh xanh trông như sơn phẳng. Đứng dưới A26 về độ tin.
- **T: 6,3**. Chỉ có góc chính diện, không có thông tin độ dày. Lề trên, dưới không đạt.

Sửa:
1. Đổi lưỡi sang thép hoặc ngọc có phản xạ thật; bỏ màu kem phẳng.
2. Nới lề trên, dưới ≥ 8 %.
3. Thêm góc 3/4 hoặc góc nghiêng để định độ dày.
4. Chọn một trong hai bản (A25 hoặc A26) làm hướng chính. Hai bản hiện chung chuôi và núm nên dễ lẫn.
5. Rãnh giữa nên là rãnh khắc có độ sâu (có cạnh sáng, cạnh tối), không phải dải màu.

## A24: cột phong ấn lưới (totem)

**Thấy gì:** Một đĩa đá tròn có hoa văn ô lưới chéo, được kẹp trong vành đá tối có bốn khóa, gắn đứng vào cột đá cao trên đế bậc vuông, nhìn 3/4 từ trên xuống khoảng 30°. Đá xám nhạt khảm đá phiến xanh đậm, hoa văn chữ triện kiểu Hy Lạp, vẽ tay stylised, nền xám phẳng, sáng từ trên trái. Lề 21 / 20 / 1,0 / 2,7 %: đỉnh cột gần chạm mép trên.

- **M: 7,2**. Chế tác gọn, đọc rõ khối. Nhưng ô lưới trông như nắp thùng gỗ hay cửa sổ, chưa ra "lưới phong ấn". Hoa văn là chữ triện Hy Lạp, không phải bùa chú hay bát quái.
- **T: 6,8**. Góc nhìn tốt, đế phẳng. Lề trên gần 0. Vành đá có khe hở sau đĩa dễ thành vỏ mỏng hoặc dính khối sai.

Sửa:
1. Nới lề trên ≥ 8 % (hiện 1 %).
2. Thiết kế lại mặt đĩa thành lưới phong ấn: dây xích hoặc lưới thừng đan qua phù triện, có độ sâu rõ.
3. Vành và đĩa: hoặc liền khối hẳn, hoặc tách xa ≥ độ dày vành, để Tripo không tạo màng.
4. Thay chữ triện Hy Lạp bằng hồi văn và vân mây Trung Hoa hoặc Việt.
5. Cho đỉnh cột một đầu mái hoặc đầu thú để bóng dáng từ xa khác hẳn A23 và A19.

## A23: cột sét

**Thấy gì:** Cột đá tối hình tháp vát, đỉnh là tinh thể ngũ giác màu kem, đế bát giác bậc. Các dải sét zigzag màu xanh viền đá kem chạy dọc ba mặt. Góc nhìn gần ngang mắt, chỉ chếch xuống khoảng 15°. Đá vẽ tay stylised, nền xám phẳng, sáng từ trên trái. Lề 25 / 25 / 2,1 / 5,9 %.

- **M: 7,0**. Khối rõ và đọc chức năng nhanh. Nhưng zigzag sét là kiểu decal hoạt hình (Hearthstone, Overwatch), không phải lôi văn hay trống sét của tiên hiệp. Đá và chi tiết lặp lại kiểu bộ prop chung.
- **T: 7,2**. Bóng dáng một khối, đế phẳng. Mặt trên gần như không thấy. Lề trên không đạt.

Sửa:
1. Nâng camera lên 30–35° cho thấy mặt trên đế và đỉnh.
2. Nới lề trên ≥ 8 %.
3. Thay zigzag bằng lôi văn xoắn (hoa văn sấm cổ) hoặc cột thu lôi bằng đồng.
4. Thêm một chất liệu thứ hai (đồng xanh, sắt) cho đỉnh và vòng đai; hiện chỉ có đá.
5. Làm tinh thể đỉnh có mặt cắt trong và rõ hơn (không thêm hiệu ứng phát sáng), cho có điểm nhấn.

## A22: dải gai kiếm

**Thấy gì:** Một tấm nền đá phiến tối hình chữ nhật có rãnh xanh, cắm năm cọc đá sáng màu xiên chéo trong các ổ đá có hoa văn xoắn. Nhìn 3/4 từ trên khoảng 35°. Đá vẽ tay stylised, rêu nhẹ, nền xám phẳng, không bóng. Lề 2,1 / 2,2 / 15,6 / 10,7 %.

- **M: 6,9**. Đọc như một bẫy cọc đá chung chung. Không thấy "kiếm": không có cạnh lưỡi, không có kim loại, không có chuôi hay chắn. Khái niệm lệch so với tên.
- **T: 7,4**. Đế phẳng, góc nhìn chuẩn, mặt trên đọc tốt. Lề trái, phải không đạt.

Sửa:
1. Thay cọc đá bằng lưỡi kiếm kim loại (cạnh sắc, sống, chắn nhỏ ở ổ) để đúng tên "gai kiếm".
2. Nới lề trái, phải ≥ 8 %.
3. Cho các lưỡi cao thấp khác nhau và nghiêng theo nhịp để bóng dáng có hướng.
4. Thêm trận văn trên mặt nền thay cho rãnh xanh trơn.
5. Bớt rêu ở ổ cắm. Rêu lặp đều năm ổ trông như dán mẫu.

## A21: tùng già

**Thấy gì:** Cây tùng thân xoắn vặn, vỏ xám nâu sần nhiều thớ, rễ toả rộng trên nền. Tán là bốn cụm lá tròn như đám mây màu xanh lam lục. Nhìn ngang hơi chếch, vẽ painterly bán thực, nền xám phẳng. Lề 1,6 / 1,5 / 2,6 / 2,7 %: tán gần chạm cả hai mép bên.

- **M: 7,4**. Dáng bonsai Á Đông đẹp, thân giàu chi tiết. Nhưng tán đọc như bông cải hay cây bách xù, không ra lá kim thông. Rễ mảnh, đầu nhọn, kiểu vẽ tay chưa có trọng lượng.
- **T: 5,3**. Cây là loại khó nhất cho Tripo: tán bông, cành mảnh, rễ đầu nhọn, không có đế phẳng, góc ngang. Lề hỏng bốn cạnh.

Sửa:
1. Nới lề bốn cạnh ≥ 8 %.
2. Đặt gốc lên một tảng đá hoặc bệ phẳng để có đế, và gom rễ thành khối dày.
3. Vẽ tán thành các tầng lá kim xòe phẳng (kiểu tùng Hoàng Sơn) có mép rõ, không dùng cụm bông.
4. Nâng camera 3/4 từ trên ~30° để thấy mặt trên các tầng tán.
5. Bớt số cành nhỏ, làm dày cành còn lại để lưới giữ được.

## A20: đá vôi

**Thấy gì:** Một khối đá vôi cao dạng tháp, nhiều khe nứt dọc như cột, vệt đá xám đậm, rêu xanh ở đỉnh và một gờ bên trái. Nhìn 3/4 từ trên khoảng 25–30°, vẽ painterly stylised, sáng mềm từ trên trái, nền xám phẳng. Lề 17,5 / 16,7 / 2,1 / 4,2 %.

- **M: 7,6**. Prop tốt nhất bộ. Khối chắc, vân nứt hợp lý, gợi đá karst. Nhưng vẫn là vách đá chung chung; chưa có đặc trưng karst Hạ Long hay Quế Lâm (hốc xói, chân lõm, rãnh nước chảy). Rêu phẳng như sơn.
- **T: 7,6**. Một khối liền, đọc được mặt trên. Lề trên không đạt. Đáy chưa thấy rõ là phẳng.

Sửa:
1. Nới lề trên ≥ 8 %.
2. Cho thấy đáy cắt phẳng (một mặt đáy rõ).
3. Thêm hốc xói, chân đá lõm và rãnh nước dọc để có chất karst Á Đông.
4. Cho rêu có độ dày và mép rủ, không phải mảng màu.
5. Giảm độ đều của các khe nứt; thêm một hai mảng mặt lớn yên tĩnh cho mắt nghỉ.

## A19: cột đá

**Thấy gì:** Cột đá vuông vát, chia ba đốt bằng hai đai, giữa có huy hiệu kim cương chạm nổi, rêu loang, đế loe nhiều khối. Nhìn 3/4 từ trên khoảng 35°, vẽ tay stylised, nền xám phẳng. Lề 27,7 / 27,8 / 1,4 / 2,0 %.

- **M: 6,9**. Cột phế tích fantasy phương Tây chung chung, không có nét tiên hiệp. Vết nứt rải đều khắp mặt gây nhiễu. Rêu lặp mẫu.
- **T: 7,2**. Khối đơn, đế phẳng, mặt trên đọc tốt. Lề trên, dưới gần chạm.

Sửa:
1. Nới lề trên, dưới ≥ 8 %.
2. Thay huy hiệu kim cương bằng chạm vân mây, đầu thú hoặc ô phù văn (không có chữ đọc được).
3. Giảm nứt nhỏ, giữ vài vết lớn có chủ đích.
4. Làm đầu cột có mũ hoặc gờ mái để bóng dáng khác cột thường.
5. Đổi nhịp rêu: dày ở chân và gờ đai, sạch ở mặt đứng.

## A18: tâm trận (đĩa)

**Thấy gì:** Một bệ đá tròn nhiều bậc nhìn 3/4 từ trên khoảng 30°. Có ba nan toả ra mang tấm khảm kim cương, các vòng đá phiến tối đồng tâm, và một tinh thể bát diện màu kem ở giữa. Đá vẽ tay stylised, rêu nhẹ, nền xám phẳng, sáng trên trái. Lề 3,9 / 3,9 / 14,6 / 16,8 %.

- **M: 7,3**. Thiết kế gọn, đọc tốt từ trên. Bố cục ba nan kiểu triskelion phương Tây, không ra trận pháp (bát quái, cửu cung, sao bắc đẩu). Tinh thể đơn giản. Rãnh tối phẳng.
- **T: 7,9**. Nguồn Tripo tốt nhất bộ: đế phẳng, mặt trên đọc rõ, một khối. Chỉ lề trái, phải hụt.

Sửa:
1. Nới lề trái, phải ≥ 8 %.
2. Đổi bố cục sang bát quái tám cung, hoặc chín ô có quẻ khắc (không có chữ đọc được).
3. Cho tinh thể giữa nhiều mặt cắt hơn và chất ngọc trong (không thêm glow).
4. Cho rãnh tối có độ sâu với cạnh vát; hiện như dải sơn.
5. Bớt rêu lặp ở vòng ngoài.

## A17: cổng đá

**Thấy gì:** Một cổng kiểu bài phường nhìn 3/4 từ trên khoảng 25°: hai trụ đá xây vát có đai hoa văn tết, cột và xà gỗ, hệ đấu củng, mái ngói ống tối có đầu đao cong vút. Vẽ tay stylised, rêu nhẹ, nền xám phẳng, sáng trên trái. Lề 3,2 / 2,2 / 2,1 / 3,2 %: chạm gần cả bốn mép.

- **M: 7,6**. Prop mang chất Á Đông rõ nhất bộ, mái và đấu củng thuyết phục. Đai hoa văn tết trông như nút Celtic. Đầu đao cuộn như sừng, thiếu tượng thú đầu nóc (si vẫn). Chất đá tốt, chất gỗ còn phẳng.
- **T: 6,9**. Bóng dáng rõ, lòng cổng mở, mái đọc được. Lề hỏng bốn cạnh. Hai chân rời nhau, mái chìa xa.

Sửa:
1. Nới lề bốn cạnh ≥ 8 %.
2. Thay đai nút tết bằng hồi văn hoặc vân mây.
3. Thêm tượng thú đầu nóc và đầu đao chuẩn; bỏ đầu cuộn như sừng.
4. Thêm biển ngang trơn (không chữ) trên xà để cổng có trọng tâm.
5. Đặt hai trụ lên chung một bậc đá phẳng để Tripo có một mặt đáy liền.

## A16: nữ kiếm tu, nhìn sau

**Thấy gì:** Nữ nhân vật nhìn thẳng từ sau, đứng chữ A tay buông chéo. Áo Hán phục trắng thêu mây vàng, các vạt navy thêu hạc, tay áo rộng, váy nhiều lớp, quần navy, ủng viền vàng, búi tóc cài miện vàng. Đây là render bán thực PBR, vải gần như ảnh thật, nền xám phẳng. Lề 15,7 / 16,1 / 2,3 / 3,4 %.

- **M: 8,0**. Chi tiết thêu và chất vải ngang tầm MMO Trung Quốc. Nhưng không có kiếm hay vỏ kiếm, không có gì của một kiếm tu. Nhiều lớp vải mỏng chồng nhau.
- **T: 6,6**. Góc sau dùng được cho cặp multiview. Tay áo rủ chạm váy nên Tripo sẽ dính tay vào thân. Các vạt và gấu váy mỏng. Lề trên, dưới không đạt.

Sửa:
1. Dang tay 35–45° cho tay áo tách hẳn khỏi váy.
2. Thêm kiếm và vỏ kiếm (đeo lưng hoặc hông), khớp với ảnh trước.
3. Nới lề trên, dưới ≥ 8 %.
4. Gộp bớt lớp vạt mỏng thành ít mảng dày hơn; nâng gấu váy để lộ rõ chân.
5. Thống nhất kiểu render với bộ thú và prop (hoặc ngược lại). Hiện nhân vật lệch hẳn phong cách.

## A15: nữ kiếm tu, nhìn trước

**Thấy gì:** Cùng nhân vật nhìn thẳng trước, đứng chữ A, mặt bán thực xinh. Áo trắng thêu mây vàng, vạt navy thêu hạc, đai lưng có khóa vàng, ngọc bội treo tua rua, miện vàng chạm lọng. Render PBR bán thực, sáng studio đều, nền xám phẳng. Lề 17,0 / 18,6 / 3,8 / 3,0 %.

- **M: 8,1**. Cao nhất bộ về độ hoàn thiện. Nhưng đọc là tiểu thư hay cung nữ, không phải kiếm tu: không vũ khí, không hộ cổ tay, váy dài cản chuyển động. Mặt đẹp nhưng chung chung.
- **T: 6,9**. Đối xứng, tư thế chữ A. Tay áo phủ lên váy, hai chân sát nhau dưới váy, tua rua và chạm lọng miện mảnh như sợi. Lề trên, dưới không đạt.

Sửa:
1. Thêm yếu tố chiến đấu: kiếm đeo hông, móc đai, hộ cổ tay, vạt váy xẻ ngắn hơn.
2. Dang tay để tay áo tách khỏi thân; đứng dạng chân cho hai ống tách nhau.
3. Nới lề trên, dưới ≥ 8 %.
4. Làm dày chạm lọng miện và tua rua (hoặc bỏ tua rua) để lưới giữ được.
5. Đối chiếu trước và sau: dải đai rủ chỉ thấy ở ảnh sau, ngọc bội chỉ thấy ở ảnh trước. Cần khớp cả hai.

## A14: vua sói, nhìn trước

**Thấy gì:** Con sói khổng lồ nhìn thẳng trước ngang mắt. Lông đen, xám và kem vẽ thành các vảy lông như lá, hai bên vai và lưng có các tảng đá phiến như giáp. Render stylised mềm, sáng phẳng phía trước, nền xám phẳng. Lề 17,3 / 17,3 / 2,4 / 4,2 %.

- **M: 7,0**. Chưa có khí chất boss: không mào, không bờm vua, không vân linh thú. Tảng đá trông như dán lên lưng chứ không mọc từ thân. Mặt hơi cười, kém uy.
- **T: 6,6**. Góc trước ngang mắt nên không thấy lưng. Khối thân ở góc này phình rộng hơn so với thân thon ở ảnh ngang A13. Lề trên không đạt.

Sửa:
1. Thống nhất khối thân và vị trí đá giữa trước và ngang: ở A14 đá chìa ra hai bên, ở A13 đá nằm dọc sống lưng.
2. Cho đá mọc từ thân thành bờm hoặc vương miện đá, kèm vân phát sáng khắc (không glow).
3. Tăng tỉ lệ đầu và bờm, nét mặt dữ hơn để đọc ngay là boss.
4. Nới lề trên ≥ 8 %.
5. Thêm một ảnh 3/4 từ trên để Tripo thấy lưng.

## A13: vua sói, nhìn ngang

**Thấy gì:** Cùng con sói nhìn ngang hướng trái, đứng bốn chân, đuôi bông. Ba tảng đá phiến đặt dọc vai và lưng, lông đen xám có mảng xanh xám và kem. Render stylised mềm, nền xám phẳng. Lề 1,7 / 1,0 / 6,9 / 12,2 %.

- **M: 7,2**. Dáng ngang khoẻ, đuôi đẹp. Nhưng về bóng dáng chỉ khác sói thường ở mấy tảng đá; tư thế y hệt A03 và A11.
- **T: 6,2**. Mõm và đuôi gần chạm mép. Lệch khối so với A14. Khác khổ canvas so với ảnh trước.

Sửa:
1. Nới lề trái, phải ≥ 8 %.
2. Khớp bố trí đá với ảnh trước.
3. Cho tư thế khác sói thường (đầu hạ, vai cao, chân trước rộng) để bóng dáng boss tách khỏi sói con.
4. Đưa cả cặp về cùng khổ canvas và cùng chiều cao vật.
5. Tăng độ tương phản giữa lông và đá; hiện hai chất lẫn vào nhau ở vai.

## A12: sói (nhìn trước)

**Thấy gì:** Sói xám và kem nhìn thẳng trước ngang mắt, đứng thẳng. Lông vảy lá, mặt bình thản, chân dài thẳng. Render stylised mềm, nền xám phẳng. Lề 27,9 / 29,3 / 1,8 / 3,6 %.

- **M: 6,6**. Sói thật chung chung, không có dấu linh thú. Chân trước dài và thẳng như ngựa. Gần trùng với A04: khác ảnh xám chỉ 11 %, cùng thiết kế đổi tông màu.
- **T: 6,9**. Bóng dáng đơn, chân tách. Lề trên không đạt. Ngang mắt nên không thấy lưng.

Sửa:
1. Nếu đây là sói chỉ huy: phải có dấu phân biệt rõ (giáp vai, sẹo, tai rách, cỡ lớn hơn, bờm). Hiện chỉ đổi màu.
2. Nới lề trên ≥ 8 %.
3. Rút chân trước ngắn lại, hạ vai cho đúng tỉ lệ sói.
4. Thêm vân linh thú (vệt đá hay vân mây trên lông).
5. Khớp khổ canvas với ảnh ngang.

## A11: sói (nhìn ngang)

**Thấy gì:** Sói xám và kem nhìn ngang hướng trái, đuôi bông, bờm cổ. Render stylised mềm, nền xám phẳng. Lề 3,7 / 2,2 / 8,1 / 9,7 %.

- **M: 6,8**. Sói ngang chuẩn nhưng bình thường. Bóng dáng trùng gần như tuyệt đối với A03: khung cắt giống hệt, khác ảnh xám 2,9 %. Đây là một con được tô lại màu.
- **T: 7,0**. Bóng dáng sạch, bốn chân tách. Lề trái, phải hụt. Khác khổ với ảnh trước.

Sửa:
1. Phân biệt với A03 bằng bóng dáng, không chỉ bằng màu.
2. Nới lề trái, phải ≥ 8 %.
3. Đưa về cùng khổ với ảnh trước.
4. Thêm vân linh thú hoặc phụ kiện theo vai trò.
5. Cho đuôi dày gốc hơn; phần chóp đuôi rời rạc.

## A10: lợn rừng giáp, nhìn trước

**Thấy gì:** Lợn rừng to nhìn thẳng trước ngang mắt. Thân phủ các phiến đá xám chồng như vảy tê tê, lông kem ở ngực và chân, nanh cong màu ngà, móng guốc to. Render stylised mềm, nền xám phẳng. Lề 14,5 / 14,4 / 3,1 / 4,4 %.

- **M: 7,5**. Con thú mạnh nhất bộ: bóng dáng đặc trưng, đọc ngay là giáp. Phiến giáp còn mỏng như lá và thiếu mòn cạnh. Chưa có dấu tiên hiệp.
- **T: 7,1**. Một khối đặc, bốn chân tách. Lề trên, dưới hụt. Ngang mắt nên không thấy lưng.

Sửa:
1. Nới lề trên, dưới ≥ 8 %.
2. Cho phiến giáp dày hơn, có cạnh vát mòn và vết sứt.
3. Thêm một ảnh 3/4 từ trên để thấy lớp giáp lưng.
4. Tách rõ ranh giới giáp và lông ở chân (hiện hai lớp lẫn nhau).
5. Thêm vân khắc hoặc linh văn trên phiến đầu để có nhận diện thể loại.

## A09: lợn rừng giáp, nhìn ngang

**Thấy gì:** Cùng con lợn nhìn ngang hướng trái. Phiến đá phủ đầu, vai, lưng và chân, thân kem loang xám, đuôi búi. Render stylised mềm, nền xám phẳng. Lề 2,2 / 1,7 / 7,8 / 11,1 %.

- **M: 7,5**. Khớp thiết kế với ảnh trước, dáng nặng nề tốt. Phiến giáp như lá dán, chưa có độ dày.
- **T: 6,8**. Mõm và đuôi gần chạm mép. Khác khổ canvas với A10.

Sửa:
1. Nới lề trái, phải ≥ 8 %.
2. Cùng khổ và cùng chiều cao vật với A10.
3. Làm dày phiến giáp, thêm độ chồng và bóng giữa các phiến.
4. Kiểm tra độ phủ giáp ở chân sau so với ảnh trước.
5. Cho đuôi dày hơn hoặc ngắn lại để lưới không gãy.

## A08: vượn, nhìn sau

**Thấy gì:** Vượn khổng lồ nhìn thẳng từ sau, đứng chữ A. Lông xám kem vẽ thành các vảy lá cạnh sắc, cẳng tay và cẳng chân xám đen, vai có vân xoắn đen, đuôi cong sang trái. Render stylised gần low-poly, nền xám phẳng. Lề 4,2 / 4,5 / 1,6 / 6,1 %.

- **M: 7,2**. Khối cơ ổn. Lông vảy đều đặn nên đọc như quả thông hay atisô, thiếu lọn lông. Vân xoắn vai là điểm tiên hiệp duy nhất trong nhóm thú.
- **T: 7,3**. Chữ A tách tay tốt cho rig. Đuôi khớp bên với ảnh trước. Lề trên và hai bên hụt.

Sửa:
1. Nới lề trên ≥ 8 %, hai bên ≥ 6 %.
2. Đổi lông vảy đều thành lọn lông to nhỏ khác nhau, có hướng chảy.
3. Làm đuôi dày hơn ở gốc và gắn rõ vào thân.
4. Thêm phụ kiện tiên hiệp (vòng kim cô, đai vải, hộ cổ tay) để thoát khỏi kiểu vượn tuyết chung.
5. Cho mảng xám đen ở tay chân bớt khối vuông ghép mảnh.

## A07: vượn, nhìn trước

**Thấy gì:** Cùng con vượn nhìn trước: mặt khỉ màu da, tai hồng, mày nhíu, râu cằm, mào lông nhọn, cơ ngực rõ, đuôi ló bên phải. Render stylised, nền xám phẳng. Lề 4,1 / 4,0 / 2,3 / 5,0 %.

- **M: 7,4**. Mặt có cá tính, gợi Tề Thiên. Lông vẫn đều như vảy. Tổng thể là vượn tuyết fantasy hơn là linh thú.
- **T: 7,5**. Tư thế, ngón tay tách, một khối rõ. Lề hụt nhẹ.

Sửa:
1. Nới lề trên ≥ 8 %, hai bên ≥ 6 %.
2. Phá nhịp lông vảy, thêm lọn lông dài ở vai và cẳng tay.
3. Thêm phụ kiện hay vân linh thú như ở A08.
4. Làm rõ ngón chân, móng chân to hơn.
5. Nét mặt dữ hơn: nanh, mắt sâu.

## A06: quạ, 3/4

**Thấy gì:** Quạ đen đứng nhìn 3/4 ngang, một cánh giơ cao, cánh kia khuất. Cổ và lông phủ cánh màu kem xám, chân và móng mảnh, đuôi xòe. Render stylised mềm, nền xám phẳng. Lề 13,9 / 13,4 / 1,7 / 2,5 %.

- **M: 7,1**. Lông và dáng ổn, mắt sắc. Quạ thường, không có dấu linh điểu.
- **T: 5,4**. Tư thế động một cánh, cánh kia bị che nên Tripo phải đoán. Lông đầu cánh tách sợi. Chân mảnh, không có đế. Lề trên, dưới hụt.

Sửa:
1. Đổi sang tư thế trung tính: hai cánh mở cân đối hoặc gập sát thân, cả hai cùng thấy.
2. Nới lề trên, dưới ≥ 8 %.
3. Gộp lông thành từng nhóm dày, bỏ khe hở giữa các sợi lông bay.
4. Làm chân và móng dày hơn; cân nhắc cho đậu trên đế hay cành đá.
5. Thêm dấu linh điểu (vân trên cánh, mắt khác màu, lông đầu riêng).

## A05: quạ, nhìn trước cánh xòe

**Thấy gì:** Quạ nhìn thẳng trước, hai cánh dang hết cỡ như chữ T, chân dạng, móng quặp. Lông đen có mảng kem ở cổ và cánh. Render stylised mềm, nền xám phẳng. Lề 0,8 / 0,9 / 3,4 / 4,0 %: đầu cánh chạm gần sát mép.

- **M: 7,2**. Đối xứng, đọc rõ, cánh đẹp. Thân nhỏ so với sải cánh. Vẫn là quạ thật.
- **T: 6,0**. Tư thế chữ T tốt cho rig cánh. Lề trái, phải gần 0. Đầu lông bay tách rời. Chân mảnh.

Sửa:
1. Nới lề trái, phải ≥ 8 % (hiện dưới 1 %).
2. Gộp đầu lông bay thành mảng liền có răng cưa nông.
3. Làm chân dày hơn, ngón ngắn hơn.
4. Ghép đôi với một ảnh ngang hoặc từ trên cùng khổ để định độ dày thân và cánh.
5. Cho thân to hơn một chút so với sải cánh để đọc tốt ở cỡ nhỏ trong game.

## A04: sói (nhìn trước, tông vàng cát)

**Thấy gì:** Sói xám và vàng cát nhìn thẳng trước ngang mắt, đứng thẳng, lông vảy lá, mặt cười nhẹ. Render stylised mềm, nền xám phẳng. Lề 28,2 / 28,2 / 2,2 / 4,4 %.

- **M: 6,6**. Cùng thiết kế với A12, chỉ đổi tông ấm. Chân dài thẳng, mặt hiền, không đáng sợ.
- **T: 6,9**. Bóng dáng sạch, chân tách. Lề trên hụt.

Sửa:
1. Tách thiết kế khỏi A12 (cỡ, bóng dáng, phụ kiện), không chỉ đổi màu.
2. Nới lề trên ≥ 8 %.
3. Sửa tỉ lệ chân trước.
4. Nét mặt hung hơn (môi kéo, nanh).
5. Cùng khổ với ảnh ngang A03.

## A03: sói (nhìn ngang, tông vàng cát)

**Thấy gì:** Sói xám và vàng cát nhìn ngang hướng trái, tư thế và bóng dáng trùng A11. Render stylised mềm, nền xám phẳng. Lề 3,7 / 2,2 / 8,1 / 9,7 %.

- **M: 6,7**. Sói chung, không nhận diện tiên hiệp. Trùng bóng dáng với A11.
- **T: 7,0**. Sạch, bốn chân tách. Lề hai bên hụt.

Sửa:
1. Cho bóng dáng riêng so với A11.
2. Nới lề trái, phải ≥ 8 %.
3. Đưa về cùng khổ với A04.
4. Thêm vân linh thú.
5. Làm dày gốc đuôi.

## A02: chuột, nhìn trước

**Thấy gì:** Chuột béo tròn nhìn thẳng trước ngang mắt, mặt trắng kem, tai tròn hồng, mắt đen tròn, lông vảy lá xám có sọc đen trên lưng, chân đen móng to. Render stylised mềm, nền xám phẳng. Lề 11,5 / 11,5 / 8,7 / 10,0 %.

- **M: 6,4**. Đọc là chuột hamster hay chuột lang dễ thương, không phải chuột yêu thú thù địch. Thân như quả bóng.
- **T: 7,6**. Ảnh duy nhất đạt lề bốn cạnh; bóng dáng đặc, chân tách. Ngang mắt nên không thấy lưng.

Sửa:
1. Đổi nét mặt sang hung: mắt hẹp đỏ, răng cửa lộ, mõm dài.
2. Kéo dài mõm và thân, bớt tròn cho khớp ảnh ngang A01.
3. Thêm dấu yêu thú (gai lưng, vân đá) để hợp bộ.
4. Cùng khổ canvas với A01.
5. Tai nhỏ hơn cho khớp ảnh ngang (ở A01 tai nhỏ hơn hẳn).

## A01: chuột, nhìn ngang

**Thấy gì:** Chuột béo dài nhìn ngang hướng trái, lông vảy lá xám, ba sọc đen trên lưng, đuôi dày cong lên. Render stylised mềm, nền xám phẳng. Lề 3,3 / 2,8 / 20,1 / 19,0 %.

- **M: 6,5**. Gần chuột chù hay opossum hơn chuột yêu thú. Đọc vô hại.
- **T: 7,0**. Bóng dáng đặc, đuôi dày giữ được. Lề hai bên hụt. Khối và tai không khớp A02.

Sửa:
1. Khớp tai và khối đầu với A02 (hoặc ngược lại).
2. Nới lề trái, phải ≥ 8 %.
3. Nét mặt hung hơn, răng cửa lộ.
4. Thêm dấu yêu thú.
5. Đưa về cùng khổ với A02.

---

## Bảng tổng

| Ảnh | Vật | M | T | Kết luận một dòng |
| --- | --- | --- | --- | --- |
| A26 | Phi kiếm mảnh | 6,6 | 6,3 | Kiếm phương Tây chung, chỉ một góc, lề trên dưới 3 %; không qua |
| A25 | Phi kiếm rộng | 6,4 | 6,3 | Lưỡi kem như nhựa, đồ chơi; không qua |
| A24 | Cột phong ấn lưới | 7,2 | 6,8 | Khối gọn nhưng đĩa đọc như nắp thùng, lề trên 1 %; không qua |
| A23 | Cột sét | 7,0 | 7,2 | Zigzag hoạt hình, camera thấp; không qua |
| A22 | Dải gai kiếm | 6,9 | 7,4 | Cọc đá, không thấy kiếm; nguồn Tripo ổn nếu nới lề; không qua |
| A21 | Tùng già | 7,4 | 5,3 | Dáng đẹp nhưng tán bông cải, không đế, lề 1,5 %; không qua |
| A20 | Đá vôi | 7,6 | 7,6 | Prop tốt nhất, thiếu chất karst, lề trên hụt; không qua |
| A19 | Cột đá | 6,9 | 7,2 | Cột phế tích phương Tây chung; không qua |
| A18 | Tâm trận | 7,3 | 7,9 | Nguồn Tripo tốt nhất, thiết kế triskelion không ra trận pháp; không qua |
| A17 | Cổng đá | 7,6 | 6,9 | Chất Á Đông rõ nhất, hoa văn Celtic, lề bốn cạnh 2–3 %; không qua |
| A16 | Nữ kiếm tu, sau | 8,0 | 6,6 | Gần ngưỡng về độ chi tiết, không kiếm, tay dính váy; không qua |
| A15 | Nữ kiếm tu, trước | 8,1 | 6,9 | Cao nhất bộ, đọc là tiểu thư không phải kiếm tu; không qua |
| A14 | Vua sói, trước | 7,0 | 6,6 | Thiếu khí chất boss, khối lệch so với ảnh ngang; không qua |
| A13 | Vua sói, ngang | 7,2 | 6,2 | Chỉ là sói thường thêm đá, lề 1 %; không qua |
| A12 | Sói, trước | 6,6 | 6,9 | Trùng A04 chỉ đổi màu, chân như ngựa; không qua |
| A11 | Sói, ngang | 6,8 | 7,0 | Bóng dáng trùng A03 (khác 2,9 %); không qua |
| A10 | Lợn rừng giáp, trước | 7,5 | 7,1 | Thú mạnh nhất, giáp mỏng như lá; không qua |
| A09 | Lợn rừng giáp, ngang | 7,5 | 6,8 | Khớp ảnh trước, lề 2 %, khác khổ; không qua |
| A08 | Vượn, sau | 7,2 | 7,3 | Lông vảy kiểu quả thông, rig tốt; không qua |
| A07 | Vượn, trước | 7,4 | 7,5 | Mặt có cá tính, vẫn là vượn tuyết chung; không qua |
| A06 | Quạ, 3/4 | 7,1 | 5,4 | Một cánh khuất, tư thế động, chân mảnh; không qua |
| A05 | Quạ, cánh xòe | 7,2 | 6,0 | Cánh chạm mép dưới 1 %, lông tách sợi; không qua |
| A04 | Sói, trước (vàng cát) | 6,6 | 6,9 | Cùng thiết kế A12; không qua |
| A03 | Sói, ngang (vàng cát) | 6,7 | 7,0 | Cùng bóng dáng A11; không qua |
| A02 | Chuột, trước | 6,4 | 7,6 | Duy nhất đạt lề, nhưng là hamster dễ thương; không qua |
| A01 | Chuột, ngang | 6,5 | 7,0 | Vô hại, khối và tai không khớp A02; không qua |

**Không ảnh nào đạt 8,5 về M.** Cao nhất là A15 (8,1) và A16 (8,0). Về T, cao nhất là A18 (7,9). Không ảnh nào nên gửi Tripo ở trạng thái hiện tại. Nếu buộc phải thử một ảnh để kiểm tra đường ống thì chọn A18 hoặc A20 sau khi nới canvas, nhưng đó chỉ là thử đường ống, không phải nghiệm thu.

## Độ thống nhất phong cách

Bộ ảnh **không** đọc như một phong cách. Thứ duy nhất đồng nhất là nền xám phẳng (RGB 221–227) và bảng màu xám, đen, kem với điểm xanh navy. Cách dựng thì tách thành bốn nhóm:

- **Nhóm thú (A01–A14):** render 3D stylised mềm, lông vẽ thành vảy lá đều nhau, ánh sáng phẳng chính diện gần như không có hướng, góc trực giao ngang mắt.
- **Nhóm prop đá (A17–A19, A22–A24):** vẽ tay kiểu World of Warcraft/Hearthstone, cạnh vát sáng sắc, AO đậm, đèn chính từ trên trái, góc 3/4 từ trên.
- **A20 và A21:** painterly bán thực.
- **Nhân vật (A15–A16):** render PBR gần ảnh thật kiểu MMO Trung Quốc, vải và mặt thực hơn hẳn mọi thứ còn lại.
- **Hai thanh kiếm (A25–A26):** CG trơn, gần như không có texture.

Đặt nữ kiếm tu bán thực cạnh con chuột lông vảy hoạt hình và cột sét Hearthstone là chỗ vỡ nặng nhất. Tiếp theo là độ dày chi tiết: thêu chỉ vàng li ti, đặt cạnh vảy lông to bản, đặt cạnh khối đá vát. Hướng sáng và độ tương phản cũng khác nhau: thú gần như không có bóng tự thân, prop có bóng khối rõ.

Về nhận diện tiên hiệp, chỉ cổng A17, tùng A21 và trang phục A15/A16 đọc ra Á Đông. Prop còn lại dùng chữ triện Hy Lạp, nút Celtic, triskelion và sét zigzag. Thú là động vật thật, chưa có vân linh thú, trừ vân xoắn ở vai vượn. Sói và sói chỉ huy là cùng một thiết kế đổi màu (A03/A11 khác ảnh xám 2,9 %, A04/A12 khác 11 %).

Cách sửa: chọn một phong cách chủ (stylised vẽ tay của nhóm prop là gần thể loại nhất), render lại nhân vật và thú theo đó với cùng một đèn trên trái, đưa vào một bộ motif tiên hiệp chung (vân mây, hồi văn, lôi văn, bát quái), và chuẩn hoá khổ canvas cùng lề 8 % cho toàn bộ.
