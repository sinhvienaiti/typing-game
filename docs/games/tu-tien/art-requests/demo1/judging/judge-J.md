# Giám khảo J: chấm mù 26 ảnh gốc 2D cho Tripo (A01–A26)

Thang điểm: **M** là mức thị trường so với concept sheet AAA/AA (Genshin Impact, Where Winds Meet, Diablo IV, Black Myth: Wukong); 8 là ra mắt được nhưng bình thường, 8,5 là ngưỡng nhận, 9 là top của thể loại. **T** là độ hợp làm ảnh nguồn cho Tripo.

## Số đo khách quan (ImageMagick, trim fuzz 7 %)

Nền: cả 26 ảnh đều nền xám phẳng, giá trị 221–228, bốn góc lệch nhau tối đa 2 đơn vị, không có vignette hay gradient. Không thấy bóng đổ hay mặt đất. Điểm này đạt.

Lề (trái / phải / trên / dưới, % cạnh ảnh). Ngưỡng yêu cầu ≥ 6–8 % mọi phía. **Chỉ A02 đạt lề ở cả bốn phía.** 25 ảnh còn lại đều có ít nhất một cạnh dưới 6 %, nhiều ảnh dưới 2 %.

| Ảnh | L | R | T | B | Ảnh | L | R | T | B |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A01 | 3,3 | 2,8 | 20,1 | 19,0 | A14 | 17,3 | 17,3 | 2,4 | 4,2 |
| A02 | 11,5 | 11,5 | 8,7 | 10,0 | A15 | 17,0 | 18,6 | 3,8 | 3,0 |
| A03 | 3,7 | 2,2 | 8,1 | 9,7 | A16 | 15,7 | 16,1 | 2,3 | 3,4 |
| A04 | 28,2 | 28,2 | 2,2 | 4,4 | A17 | 3,2 | 2,2 | 2,1 | 3,2 |
| A05 | 0,8 | 0,9 | 3,4 | 4,0 | A18 | 3,9 | 3,9 | 14,6 | 16,8 |
| A06 | 13,9 | 13,4 | 1,7 | 2,5 | A19 | 27,7 | 27,8 | 1,4 | 2,0 |
| A07 | 4,1 | 4,0 | 2,3 | 5,0 | A20 | 17,5 | 16,7 | 2,1 | 4,2 |
| A08 | 4,2 | 4,5 | 1,6 | 6,1 | A21 | 1,6 | 1,5 | 2,6 | 2,7 |
| A09 | 2,2 | 1,7 | 7,8 | 11,1 | A22 | 2,1 | 2,2 | 15,6 | 10,7 |
| A10 | 14,5 | 14,4 | 3,1 | 4,4 | A23 | 24,8 | 24,9 | 2,1 | 5,9 |
| A11 | 3,7 | 2,2 | 8,1 | 9,8 | A24 | 20,8 | 19,7 | 1,0 | 2,7 |
| A12 | 27,9 | 29,3 | 1,8 | 3,6 | A25 | 35,1 | 35,1 | 2,6 | 3,1 |
| A13 | 1,7 | 1,0 | 6,9 | 12,2 | A26 | 44,2 | 44,2 | 2,8 | 3,2 |

Lỗi chung của các cặp đa góc nhìn: các cặp thú được xuất ở hai khổ khác nhau (ngang 1024×683 và vuông 1024×1024) với **tỉ lệ khác nhau**. Chiều cao chủ thể theo pixel: chuột 416 so với 833, sói 562 so với 956, lợn rừng 554 so với 947, sói chỉ huy 561 so với 969, sói vua 553 so với 956. Tripo multiview cần cùng khung, cùng tỉ lệ, cùng đường chân, nên không cặp thú nào dùng thẳng được. Cặp quạ (A05/A06) còn khác cả tư thế. A03 và A11 gần như là một ảnh (RMSE 4 %, chỉ lệch tông màu). A04 và A12 là cùng một thiết kế làm lại (RMSE 12 %).

---

## A01: chuột, nhìn ngang

**Thấy gì:** Một con chuột béo, lưng phủ các mảng vảy hình lá màu xám đá với ba sọc đen ngang lưng, mặt trắng kem giống chuột lang hay lửng hơn là chuột hung dữ, đuôi cong lên. Góc nhìn ngang trực giao, nền xám phẳng, ánh sáng khuếch tán từ trên, chất liệu mờ không phản quang, khung chạm sát mép trái và phải.

- **M: 6,3**
- **T: 6,8**

Sửa:
1. Đưa vào khung cùng khổ và cùng tỉ lệ với A02, lề ≥ 8 % hai bên (hiện 3,3 % và 2,8 %).
2. Thiết kế lại đầu cho ra quái vật: mõm dài, răng cửa lộ, mắt hẹp; hiện đầu hiền như thú cưng.
3. Cho vảy lá một ý nghĩa chất liệu rõ (đá, sừng hay lông cứng); hiện trông như giấy dán.
4. Thêm một điểm nhấn tu tiên (vân linh khí, vết ấn, mắt phát sáng nhạt bằng màu, không hiệu ứng).
5. Tách chân sau khỏi bụng rõ hơn để mesh không dính khối.

## A02: chuột, nhìn trước

**Thấy gì:** Cùng con chuột nhìn thẳng từ trước, thân tròn như quả bóng, mặt trắng kem cười nhẹ, tai hồng, bốn bàn chân móng xám. Nền xám phẳng, ánh sáng khuếch tán đều, khung là ảnh duy nhất trong bộ có lề đủ cả bốn phía.

- **M: 6,2**
- **T: 7,2**

Sửa:
1. Đổi biểu cảm: đang cười hiền, phải ra vẻ đe dọa hoặc tham lam.
2. Khớp tỉ lệ với A01 (chủ thể cao 833 px ở đây so với 416 px ở A01).
3. Thân hình cầu đọc như chuột hamster; cần ngực hẹp hơn, vai gồ, đầu thấp.
4. Làm vùng bụng và chân trước có khe hở rõ để Tripo không đúc liền khối.
5. Cân lại mảng sọc đen lưng cho khớp với A01 (ở A01 sọc rộng hơn và cách xa hơn).

## A03: sói, nhìn ngang

**Thấy gì:** Sói xám xanh, bụng và chân kem, lông vẽ thành các chùm nhọn kiểu painterly, đuôi xù dài, đứng bốn chân ngang trực giao. Nền xám phẳng, ánh sáng mềm, tương phản thấp, mũi và chóp đuôi gần chạm mép.

- **M: 6,8**
- **T: 6,8**

Sửa:
1. Lề trái và phải 3,7 % và 2,2 %: thu nhỏ để đạt ≥ 8 %.
2. Khớp tỉ lệ và khổ với A04.
3. Thêm dấu ấn tu tiên (vân linh văn trên vai, mắt có màu yêu khí); hiện là sói thường.
4. Làm chóp đuôi đặc hơn, bỏ sợi lông mảnh mà mesh không giữ được.
5. Tăng tương phản và hướng sáng rõ hơn để khối vai và hông đọc được.

## A04: sói, nhìn trước

**Thấy gì:** Sói nhìn thẳng từ trước, đối xứng, chân dài, ngực kem, mép hơi cong như đang cười. Nền xám phẳng, ánh sáng khuếch tán, tai chạm sát mép trên.

- **M: 6,6**
- **T: 6,5**

Sửa:
1. Lề trên 2,2 %: thu nhỏ cho đủ ≥ 8 %.
2. Bỏ nét cười: kẻ thù cần khóe miệng xệ, nhe nanh nhẹ.
3. Chân quá dài và thẳng như cột; rút ngắn cẳng, cho khuỷu rõ.
4. Khớp tỉ lệ với A03 (956 px so với 562 px).
5. Lông ngực vẽ rõ khối lớn, bớt vảy nhỏ lặp lại.

## A05: quạ, nhìn trước, xòe cánh

**Thấy gì:** Quạ đen xám, ngực và mảng giữa cánh kem, hai cánh xòe phẳng hết cỡ, chân thõng với móng cong. Nhìn thẳng trực giao, nền xám phẳng, chóp cánh gần như chạm hai mép ảnh.

- **M: 6,8**
- **T: 4,5**

Sửa:
1. Lề trái và phải chỉ 0,8 % và 0,9 %: thu nhỏ mạnh hoặc gập cánh nửa chừng.
2. Thống nhất tư thế với A06; hai ảnh hiện không thể làm cặp đa góc nhìn.
3. Lông cánh sơ cấp tách rời và mỏng: gộp thành mảng dày để mesh giữ được.
4. Thêm đế hoặc tư thế đậu cho Tripo có mặt đáy; tư thế bay không có điểm tựa.
5. Thêm nét yêu điểu tu tiên (mắt ba con, lông đuôi dài, vân ấn trên cánh).

## A06: quạ, ba phần tư, giơ cánh

**Thấy gì:** Quạ nghiêng ba phần tư sang trái, một cánh giơ cao ra sau, đuôi xòe, hai chân thõng với móng cong. Nền xám phẳng, ánh sáng mềm, cánh kia bị che hoàn toàn, chóp cánh và móng sát mép trên và dưới.

- **M: 7,0**
- **T: 5,0**

Sửa:
1. Cho thấy cả hai cánh; Tripo sẽ phải đoán cánh bị che.
2. Lề trên 1,7 % và dưới 2,5 %: thu nhỏ.
3. Đặt quạ đậu trên chân để có đáy phẳng.
4. Đồng bộ tư thế với A05 hoặc bỏ một ảnh.
5. Hạ góc máy lên khoảng 30° từ trên để đọc được lưng.

## A07: vượn, nhìn trước

**Thấy gì:** Vượn đứng thẳng tư thế gần chữ A, toàn thân phủ vảy hình lá màu xám kem, cẳng tay và cẳng chân màu đá đen, vai có vân mây cuộn, mặt khỉ cau mày. Nhìn trước trực giao, nền xám phẳng, ánh sáng khuếch tán, đầu sát mép trên.

- **M: 7,2**
- **T: 7,4**

Sửa:
1. Lề trên 2,3 % và hai bên khoảng 4 %: thu nhỏ khoảng 15 %.
2. Vảy lá đồng loạt một cỡ làm thân như quả atisô; cần thứ bậc lớn, trung, nhỏ.
3. Vân mây vai là điểm sáng nhất, nên lặp lại nhẹ ở đùi hoặc lưng để thành motif.
4. Đuôi lộ một mẩu ở hông, đọc như vật dính; cho đuôi dài và rõ hơn.
5. Tăng dáng nặng: hạ vai, gập gối nhẹ, để tạo khí thế quái vật.

## A08: vượn, nhìn sau

**Thấy gì:** Cùng con vượn nhìn từ sau, mào vảy nhọn trên đầu, vân mây cuộn trên hai bả vai, đuôi cuộn chéo qua hông. Nền xám phẳng, ánh sáng đều, khớp tư thế và mảng màu với A07.

- **M: 7,0**
- **T: 7,3**

Sửa:
1. Lề trên 1,6 %: thu nhỏ.
2. Đuôi cuộn chéo nằm áp sát mông và đùi, dễ dính khối; tách khỏi thân.
3. Lưng thiếu điểm nhấn; thêm vân hoặc vết sẹo.
4. Vảy lưng lặp đều, cần phân bậc như A07.
5. Kiểm khớp đuôi với A07 (ở A07 đuôi ngắn, ở A08 dài và cuộn).

## A09: lợn rừng giáp đá, nhìn ngang

**Thấy gì:** Lợn rừng to, lưng và vai phủ các tấm giáp đá phiến xám sẫm có nứt, lông kem lốm đốm, nanh cong trắng ngà, đuôi xù. Nhìn ngang trực giao, nền xám phẳng, chất liệu đá có vân nhỏ và mép sắc, mõm và đuôi chạm sát hai mép.

- **M: 7,4**
- **T: 7,0**

Sửa:
1. Lề trái 2,2 % và phải 1,7 %: thu nhỏ.
2. Khớp tỉ lệ và khổ với A10.
3. Giáp đá cần dấu hiệu tu tiên (vân phù khắc, đường nứt ánh linh thạch bằng màu) để khác giáp quái fantasy chung.
4. Đuôi xù mảnh: làm khối đặc hơn.
5. Tăng tương phản lông kem với giáp để đọc được ở cỡ nhỏ trong game.

## A10: lợn rừng giáp đá, nhìn trước

**Thấy gì:** Lợn rừng nhìn thẳng, trán phủ một dải giáp đá xếp lớp như mũi thuyền, nanh trắng hai bên mõm, mắt nâu cau, bốn chân móng guốc nặng. Nền xám phẳng, ánh sáng mềm, khớp vật liệu với A09.

- **M: 7,4**
- **T: 7,1**

Sửa:
1. Lề trên 3,1 % và dưới 4,4 %: thu nhỏ.
2. Khớp tỉ lệ với A09 (947 px so với 554 px).
3. Mắt hơi buồn; cho ánh nhìn hung hơn.
4. Lông giữa các tấm giáp vẽ dạng sợi mảnh; gộp khối.
5. Thêm một điểm nhấn thứ bậc (vết sẹo, chiếc nanh gãy) để nhận diện.

## A11: sói chỉ huy (có lẽ), nhìn ngang

**Thấy gì:** Một con sói giống A03 đến từng chùm lông, cùng tư thế, cùng hình bóng, chỉ lạnh tông và kem sáng hơn chút. Nền xám phẳng, ánh sáng mềm, mũi và đuôi sát mép.

- **M: 6,0**
- **T: 6,8**

Sửa:
1. Làm lại hẳn: không có dấu hiệu chỉ huy nào (giáp, sẹo, bờm, kích thước, phù hiệu); RMSE so với A03 chỉ 4 %.
2. Cho to hơn, bờm dày, một tấm giáp vai hoặc vòng cổ có ấn.
3. Lề trái và phải 3,7 % và 2,2 %: thu nhỏ.
4. Khớp tỉ lệ với A12.
5. Đổi màu chủ đạo rõ (sói đen đầu bạc chẳng hạn) để đọc ra khác sói thường.

## A12: sói chỉ huy (có lẽ), nhìn trước

**Thấy gì:** Sói nhìn thẳng, cùng thiết kế với A04, lông kem nhạt hơn và mảng xám xanh hơn. Nền xám phẳng, tai sát mép trên.

- **M: 5,9**
- **T: 6,4**

Sửa:
1. Thiết kế khác hẳn sói thường (như A11 mục 1–2).
2. Lề trên 1,8 %: thu nhỏ.
3. Bỏ nét mặt hiền; cần vẻ ra lệnh.
4. Chân dài như cột: chỉnh giải phẫu.
5. Khớp tỉ lệ với A11.

## A13: sói vua (boss), nhìn ngang

**Thấy gì:** Sói đen xám to, mặt gầm gừ, ba tấm đá phiến lớn đặt trên vai và lưng như giáp, đuôi xù dài. Nhìn ngang, nền xám phẳng, ánh sáng mềm, mõm và đuôi gần chạm mép.

- **M: 7,1**
- **T: 6,6**

Sửa:
1. Lề trái 1,7 % và phải 1,0 %: thu nhỏ mạnh.
2. Giáp đá trông như đá đặt lên lưng; cho mọc từ thân hoặc buộc bằng xích, dây ấn.
3. Boss cần dấu hiệu vương giả: vương miện xương, bờm bạc, vân ấn trên trán.
4. Khớp tỉ lệ với A14.
5. Chóp đuôi và lông cổ mảnh: gộp khối.

## A14: sói vua (boss), nhìn trước

**Thấy gì:** Sói vua nhìn thẳng, ngực kem rộng, hai tấm giáp đá lớn như giáp vai, một tấm trên đỉnh lưng, móng vuốt to. Nền xám phẳng, ánh sáng đều, đầu sát mép trên.

- **M: 7,2**
- **T: 6,7**

Sửa:
1. Lề trên 2,4 %: thu nhỏ.
2. Giáp đá ba tấm ở A13 nhưng nhìn trước ra hai vai và một đỉnh: thống nhất số và vị trí.
3. Thêm dấu hiệu boss như A13 mục 3.
4. Mặt cần hung hơn; hiện vẫn hơi điềm đạm.
5. Khớp tỉ lệ với A13.

## A15: nữ kiếm tu, nhìn trước

**Thấy gì:** Cô gái trẻ dựng theo lối CG bán tả thực, mặc hán phục trắng và xanh tím than thêu chỉ vàng hình mây và hạc, đeo mũ cài vàng, ngọc bội có tua, tay buông chéo kiểu chữ A, đi ủng thêu. Nền xám phẳng, ánh sáng studio đều, **không có thanh kiếm nào**.

- **M: 7,8**
- **T: 6,6**

Sửa:
1. Thêm kiếm (đeo hông hoặc cầm); hiện là trang phục thời trang, không phải kiếm tu.
2. Gộp các lớp váy xẻ và dải vải thõng từ vai thành ít mảng dày; Tripo sẽ đúc liền hoặc thủng.
3. Lề trên 3,8 % và dưới 3,0 %: thu nhỏ.
4. Chuyển về cùng lối vẽ với thú và đạo cụ, hoặc ngược lại; mặt tả thực lệch hẳn bộ.
5. Tách tay khỏi ống tay rộng một khoảng rõ để rig được.

## A16: nữ kiếm tu, nhìn sau

**Thấy gì:** Cùng nhân vật nhìn từ sau, búi tóc với mũ cài vàng, vạt áo giữa trắng thêu mây vàng, hai vạt xanh có hạc, ống tay loe. Nền xám phẳng, ánh sáng đều, khớp tốt với A15 về hoa văn và màu.

- **M: 7,6**
- **T: 6,6**

Sửa:
1. Thêm kiếm hoặc vỏ kiếm sau lưng, khớp với A15 sau khi sửa.
2. Gộp lớp váy và dải vải như A15.
3. Lề trên 2,3 %: thu nhỏ.
4. Lưng thiếu điểm nhấn hình bóng; cân nhắc dải lụa dày bay hoặc kiếm chéo lưng.
5. Thống nhất lối vẽ với cả bộ như A15.

## A17: cổng đá

**Thấy gì:** Cổng kiểu bài lâu: hai trụ xây đá hộc phủ rêu, cột gỗ, xà gỗ có ô đan hình thắt nút, mái ngói ống đầu cong. Góc ba phần tư từ trên khoảng 30°, lối vẽ tay kiểu stylized, nền xám phẳng, khung chạm sát bốn mép.

- **M: 7,5**
- **T: 7,2**

Sửa:
1. Lề cả bốn phía 2–3 %: thu nhỏ khoảng 20 %.
2. Hoa văn đan thắt nút đọc như Celtic; đổi sang hồi văn, vân mây hoặc ô chữ triện.
3. Đầu đao cong như sừng chuối; làm theo đầu đao, kìm nóc Á Đông.
4. Mái ngắn so với lối đi; tăng độ vươn mái và chiều cao lối đi cho uy nghi.
5. Thêm một bảng biển trống (không chữ) ở giữa xà để cổng đọc ra cửa ải.

## A18: đĩa trận nhãn (formation heart)

**Thấy gì:** Bệ tròn bằng đá ba bậc, ba cánh chia đều có ô hình thoi, các rãnh vòng đá sẫm, một khối tinh thể trắng hình chóp ở tâm, rêu ở mép. Góc ba phần tư từ trên khoảng 35°, lối vẽ tay, nền xám phẳng, chạm gần mép trái và phải.

- **M: 7,0**
- **T: 8,0**

Sửa:
1. Lề trái và phải 3,9 %: thu nhỏ.
2. Ba cánh đối xứng đọc như bệ dịch chuyển fantasy; đổi sang bát quái hoặc tám cánh có quẻ khắc.
3. Tinh thể trung tâm quá thô; cho dáng linh thạch có mặt cắt.
4. Rãnh vòng nên khắc phù văn nổi (hình, không chữ đọc được).
5. Thêm chiều cao ở viền ngoài để khối rõ khi camera xa.

## A19: cột đá

**Thấy gì:** Cột đá vuông thon dần, ba đai xây nhô, mặt giữa khắc ô thoi, chân bệ gồm khối đá vỡ phủ rêu. Góc ba phần tư từ trên khá dốc khoảng 40°, lối vẽ tay, nền xám phẳng, chạm sát mép trên và dưới.

- **M: 6,7**
- **T: 7,4**

Sửa:
1. Lề trên 1,4 % và dưới 2,0 %: thu nhỏ.
2. Thiết kế chung chung; thêm đầu cột chạm đấu củng hoặc đầu thú để ra Á Đông.
3. Ô thoi khắc rỗng nghĩa; thay bằng phù văn hay vân mây.
4. Chân bệ vỡ không phẳng ở mép trước; chuẩn hóa đáy.
5. Giảm góc máy về 30–35° để thân cột không bị ngắn đi.

## A20: đá vôi

**Thấy gì:** Khối đá vôi cao kiểu núi đá Hạ Long, mặt chẻ dọc, vệt xám sẫm chảy, rêu xanh ở đỉnh và một gờ bên trái. Góc ba phần tư từ trên, vẽ bán tả thực, nền xám phẳng, sát mép trên.

- **M: 7,5**
- **T: 7,3**

Sửa:
1. Lề trên 2,1 % và dưới 4,2 %: thu nhỏ.
2. Hình bóng giống một khối nón; thêm vai, hốc hay mái nhô cho dáng đá kỳ.
3. Đáy có tảng tròn lồi ra trước, không phẳng; cắt bằng đáy.
4. Rêu nên có độ dày khối, không chỉ là màu vẽ.
5. Cân lối vẽ với các đạo cụ stylized còn lại (A17–A19).

## A21: tùng già

**Thấy gì:** Cây cổ thụ thân xoắn vặn vỏ sần, bốn tán lá thành từng đám mây tròn màu xanh xám, rễ bám xòe trên mặt đất. Nhìn gần ngang hơi từ trên, nền xám phẳng, tán chạm sát mép trái và phải.

- **M: 7,4**
- **T: 4,8**

Sửa:
1. Lề hai bên 1,6 % và 1,5 %: thu nhỏ mạnh.
2. Tán lá đọc như bách xù hay sồi, không phải tùng; cần chùm lá kim dạng quạt, dày lớp.
3. Tán gồm hàng ngàn chùm lá nhỏ: Tripo sẽ ra khối nhòe; nên làm thân bằng Tripo, tán bằng card lá riêng.
4. Rễ xòe đầu mảnh và ở các độ cao khác nhau: cho đáy phẳng, rễ dày.
5. Thêm góc từ trên 30° để đọc được mặt trên của tán.

## A22: dải gai kiếm (bẫy)

**Thấy gì:** Bệ đá đen chữ nhật có rãnh xanh lam, năm cột đá trắng hình lăng trụ chéo về trước cắm trong ổ có hoa văn xoắn ốc. Góc ba phần tư từ trên khoảng 30°, lối vẽ tay kiểu WoW, nền xám phẳng, chạm sát mép trái và phải.

- **M: 6,7**
- **T: 7,4**

Sửa:
1. Gai là lăng trụ đá cùn, không phải kiếm; làm thành lưỡi kiếm có chuôi chìm, mũi sắc, sống kiếm.
2. Lề trái và phải khoảng 2 %: thu nhỏ.
3. Rãnh xanh đọc như nước; nếu là trận văn, khắc hoa văn rõ.
4. Bệ đơn điệu; thêm viền hồi văn và ổ cắm dạng vỏ kiếm.
5. Cho gai đứng thẳng hoặc xếp so le để đọc chức năng bẫy từ trên.

## A23: cột sét

**Thấy gì:** Cột đá đen thon lục giác, khảm đường zigzag xanh lam viền kem như tia sét, đỉnh là khối tinh thể kem, chân bệ bậc nhiều góc. Nhìn gần chính diện chỉ hơi từ trên khoảng 15°, lối vẽ tay kiểu WoW/Hearthstone, nền xám phẳng, chạm sát mép trên.

- **M: 6,6**
- **T: 7,2**

Sửa:
1. Zigzag là ký hiệu sét quá thẳng thừng, đọc như game châu Âu; dùng lôi văn Á Đông (vân sấm hình xoắn vuông).
2. Nâng góc máy lên 30–35° cho thấy mặt trên.
3. Lề trên 2,1 % và dưới 5,9 %: thu nhỏ.
4. Đỉnh tinh thể quá lớn và mập; cho dạng lôi châu hoặc cột thu sét có vòng đồng.
5. Ô kem dọc giữa trống rỗng; khắc phù hình.

## A24: cột phong ấn lưới (sealing-net totem)

**Thấy gì:** Bệ vuông bậc, một trụ cao bên phải có hồi văn, giữ một đĩa tròn lưới ô đan chéo trong vòng đá có các khóa kẹp. Góc ba phần tư từ trên khoảng 30°, lối vẽ tay, nền xám phẳng, chạm sát mép trên và dưới.

- **M: 7,0**
- **T: 6,8**

Sửa:
1. Lề trên 1,0 % và dưới 2,7 %: thu nhỏ.
2. Đọc như giá gương, cồng hay khiên, không phải cột phong ấn; cho lưới phủ ra, dây xích, bùa treo bằng khối.
3. Khe giữa đĩa và vòng rất hẹp; Tripo sẽ lấp hoặc thủng thất thường; nới rộng hoặc gộp.
4. Hoa văn đĩa nên là ô lưới thật, không phải chữ thập kiểu cửa sổ.
5. Thêm đỉnh trụ có điểm nhấn (đầu thú, chuông) cho hình bóng thú vị.

## A25: phi kiếm, nhìn trước

**Thấy gì:** Kiếm thẳng hai lưỡi, thân lưỡi trắng ngà, viền thép vát, rãnh máu xanh đậm giữa, chắn tay hình cánh sen thép đen, chuôi quấn dây xanh, núm cầu ngà. Nhìn chính diện trực giao, nền xám phẳng, mũi và núm sát mép trên dưới.

- **M: 6,5**
- **T: 6,2**

Sửa:
1. Thiết kế đơn giản, tỉ lệ kiếm châu Âu; làm thành kiếm Trung Hoa (thân hẹp hơn, chắn tay nhỏ, tua kiếm bằng khối).
2. Lề trên 2,6 % và dưới 3,1 %: thu nhỏ.
3. Cần ảnh ba phần tư hoặc cặp đa góc nhìn đúng; ảnh chính diện một mình cho mesh phẳng.
4. Mép lưỡi mỏng như giấy: cho dày tối thiểu để mesh giữ được.
5. Thêm chi tiết tu tiên trên thân (phù văn khắc nổi, ngọc khảm ở chắn tay).

## A26: phi kiếm, nhìn cạnh (có lẽ)

**Thấy gì:** Một thanh kiếm hẹp hơn nhiều so với A25, vẫn thấy lõi trắng ngà, vát thép và chắn tay cánh sen, chuôi xanh, núm cầu ngà. Nhìn chính diện, nền xám phẳng, mũi và núm sát mép trên dưới.

- **M: 6,2**
- **T: 5,3**

Sửa:
1. Nếu là góc nhìn cạnh thì sai: lưỡi nhìn cạnh phải là một vạch mỏng vài pixel, chắn tay phải thành thanh mỏng; hiện đọc như một thanh kiếm thứ hai hẹp hơn.
2. Vẽ lại đúng xoay 90° từ A25, cùng tâm, cùng chiều cao.
3. Lề trên và dưới khoảng 3 %: thu nhỏ.
4. Chắn tay cánh sen ở đây hẹp hơn A25 rất nhiều nhưng vẫn đủ cánh: không hợp lý về hình khối.
5. Cân nhắc thay cặp này bằng một ảnh ba phần tư nghiêng 30°.

---

## Bảng tổng hợp

| Ảnh | M | T | Kết luận một dòng |
| --- | --- | --- | --- |
| A01 chuột ngang | 6,3 | 6,8 | Hiền như thú cưng, vảy giấy, lề hai bên dưới 3,5 %, lệch tỉ lệ với A02. |
| A02 chuột trước | 6,2 | 7,2 | Ảnh duy nhất đủ lề, nhưng mặt cười và thân cầu đọc ra chuột hamster. |
| A03 sói ngang | 6,8 | 6,8 | Sói thường gọn gàng, không chất tu tiên, lề hai bên hỏng. |
| A04 sói trước | 6,6 | 6,5 | Nét mặt cười, chân cột, sát mép trên. |
| A05 quạ xòe cánh | 6,8 | 4,5 | Cánh chạm mép (0,8 %), không đáy, lông mảnh, khác tư thế với A06. |
| A06 quạ ba phần tư | 7,0 | 5,0 | Dáng có lực nhưng mất một cánh, không đáy, sát mép. |
| A07 vượn trước | 7,2 | 7,4 | Thú tốt nhất, tư thế chữ A tốt cho rig, vảy lặp đơn điệu, sát mép trên. |
| A08 vượn sau | 7,0 | 7,3 | Khớp A07, lưng thiếu điểm nhấn, đuôi dính hông. |
| A09 lợn giáp ngang | 7,4 | 7,0 | Chất đá phiến tốt, chưa có dấu ấn tu tiên, lề hai bên dưới 2,5 %. |
| A10 lợn giáp trước | 7,4 | 7,1 | Khối nặng đọc rõ, lệch tỉ lệ với A09, sát mép trên. |
| A11 sói chỉ huy ngang | 6,0 | 6,8 | Bản sao A03 (RMSE 4 %), không có gì đọc ra chỉ huy. |
| A12 sói chỉ huy trước | 5,9 | 6,4 | Bản làm lại của A04, vô hiệu về vai trò. |
| A13 sói vua ngang | 7,1 | 6,6 | Có khí thế hơn nhưng giáp đá như đặt lên, lề chỉ 1 %. |
| A14 sói vua trước | 7,2 | 6,7 | Đọc được boss, giáp lệch số với A13, thiếu dấu hiệu vương giả. |
| A15 kiếm tu trước | 7,8 | 6,6 | Trang phục đẹp nhất bộ nhưng không có kiếm, lớp vải khó mesh, lệch lối vẽ. |
| A16 kiếm tu sau | 7,6 | 6,6 | Khớp A15, cùng các lỗi: thiếu kiếm, nhiều lớp vải, tả thực lệch bộ. |
| A17 cổng đá | 7,5 | 7,2 | Đạo cụ mạnh nhất, góc đúng, nhưng sát mép mọi phía và hoa văn như Celtic. |
| A18 đĩa trận nhãn | 7,0 | 8,0 | Nguồn Tripo tốt nhất bộ, thiết kế bệ dịch chuyển fantasy chung chung. |
| A19 cột đá | 6,7 | 7,4 | Dễ mesh nhưng vô danh, sát mép trên dưới. |
| A20 đá vôi | 7,5 | 7,3 | Chất đá Hạ Long tốt, dáng nón đơn điệu, đáy không phẳng. |
| A21 tùng già | 7,4 | 4,8 | Thân đẹp, tán không phải tùng, Tripo không làm nổi tán lá, chạm mép. |
| A22 dải gai kiếm | 6,7 | 7,4 | Gai là cột đá cùn, không đọc ra kiếm, sát mép hai bên. |
| A23 cột sét | 6,6 | 7,2 | Zigzag kiểu WoW, góc quá thấp, sát mép trên. |
| A24 cột phong ấn lưới | 7,0 | 6,8 | Đọc như giá gương hay cồng, khe hẹp khó mesh, chạm mép trên. |
| A25 phi kiếm trước | 6,5 | 6,2 | Kiếm châu Âu đơn giản, chỉ một góc chính diện. |
| A26 phi kiếm cạnh | 6,2 | 5,3 | Không phải góc nhìn cạnh đúng, đọc như thanh kiếm thứ hai. |

**Không ảnh nào đạt 8,5 về M. Chỉ A02 đạt lề; không ảnh nào đủ điều kiện gửi Tripo nguyên trạng.**

## Độ thống nhất phong cách

Bộ ảnh **không** đọc ra một phong cách. Nó tách thành ít nhất ba nhóm. (1) Thú (A01–A14): kiểu render mềm, tương phản thấp, ánh sáng khuếch tán chính diện không có hướng chính, chất mờ không phản quang; lông và vảy được cách điệu thành các mảng lá hay chùm nhọn. Ngay trong nhóm này cũng lệch: chuột và vượn dùng vảy lá như giấy cắt, sói dùng chùm lông painterly, lợn rừng có vân đá chi tiết và mép sắc hơn hẳn. (2) Đạo cụ và cơ quan (A17–A24): vẽ tay stylized kiểu WoW hay Genshin, viền vát sáng, ánh sáng có hướng từ trên trái, rêu, mảng xanh lam bão hòa ở A22–A24; nhóm này tự khớp nhau khá tốt, trừ A20 và A21 vẽ bán tả thực hơn. (3) Nữ kiếm tu (A15–A16): CG bán tả thực với da, mặt và vải thật, lệch hẳn khỏi cả thú lẫn đạo cụ; nhân vật này đặt cạnh con chuột hay cột sét sẽ như từ hai game khác nhau. Cặp kiếm (A25–A26) lại là render phẳng sạch, ít chi tiết, gần như vector. Điểm chung giữ được là nền xám 221–228 đồng đều và bảng màu (xám đá, kem, xanh tím than). Những gì phá sự thống nhất: mức tả thực khác nhau giữa nhân vật và phần còn lại; hướng sáng (khuếch tán ở thú, có hướng ở đạo cụ); góc máy (thú trực giao ngang và trước, đạo cụ ba phần tư từ trên, kiếm chính diện); khổ và tỉ lệ khác nhau trong cùng một cặp; giọng điệu (chuột và sói mặt hiền, vượn, lợn và sói vua hung). Motif Á Đông chỉ rải rác (vân mây ở vượn, hạc và mây ở kiếm tu, hồi văn ở A24), còn A17, A18, A22, A23 mang hoa văn fantasy phương Tây.
