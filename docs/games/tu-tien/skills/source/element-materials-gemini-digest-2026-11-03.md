# Element materials research, Gemini (Argon, mức Cao), 03/11/2026: bản tóm tắt

Chat gốc ba phần, cùng đề bài với ChatGPT: https://gemini.google.com/app/97e6c98e9290f0ca. Trang Gemini chặn gửi văn bản về máy cục bộ, nên ở đây chỉ có bản tóm tắt do Claude ghi; nguyên văn còn trong chat. Đây là ý kiến thứ hai, chưa kiểm nguồn. Các tham chiếu Gemini dẫn chỉ ghi "Baidu Baike: …", không có link.

## Phần 1 và 2: từng hệ

| Hệ | Luật (Gemini) | Phép thử đọc ở 55° | Làm rẻ khi | Tham chiếu Gemini nêu |
|---|---|---|---|---|
| Metal | không cong, không lực cản; đội hình khóa cứng rồi lao thẳng; khựng 3 khung khi trúng | đường cắt thẳng trắng lam vượt quá mục tiêu 2 m, cộng khựng 2 khung | vệt mềm Gauss, đường cong trơn | Honkai: Star Rail (Yanqing, Jing Yuan), donghua Perfect World, Naraka: Bladepoint |
| Fire | hút vào điểm nóng rồi nổ; đội hình co 40 % trong 3 khung rồi bung | nhịp co 3 khung rồi bùng, viền bồ hóng tím than quanh lõi vàng | chỉ cộng sáng, không có lớp bồ hóng tối, nên thành canh hồng nhạt và lẫn với đỏ cảnh báo | Doupo Cangqiong (Phật Nộ Hỏa Liên: lặng 0,2 s trước khi nổ), Black Myth: Wukong (Tam Muội Chân Hỏa: lõi vàng trắng, mép khói mực), Vương Giả Vinh Diệu (Chu Du: viền than quanh lửa đất) |
| Water | đi theo đường cong chữ S, để lại dòng nước nối các mục tiêu, kéo thú vào sống dòng | dải chữ S có mép bọt trắng bậc thang trên vùng nước chàm đậm | lưới xanh nhạt trong mờ, mép mềm | Vương Giả Vinh Diệu (Đại Kiều), Genshin (Neuvillette, Tartaglia), donghua Ngũ Hành Sơn |
| Thunder | phán xét từ trên: đường bay gãy khúc, sét giáng dọc từ mép trên khung | cột sét dọc chạm mép trên màn hình, nhánh đất 12 fps, thú lóe kiểu X-quang 2 khung | dải nhiễu sin trơn ở 60 fps như sợi mì neon | Genshin (Raiden Shogun), donghua Phàm Nhân Tu Tiên (Cửu Thiên Thần Lôi), Naraka |
| Wood | sinh trưởng: hạt nảy dây giữa đường bay, mọc thành bụi tre, lồng gai, tán sen | dây xoắn ốc mọc dài ra phía trước, bung thành rễ và tre khi trúng | hạt xanh neon phẳng, không có màu vỏ cây tối | Genshin (Nahida, Baizhu, Alhaitham), Đấu La Đại Lục (Lam Ngân Hoàng), Vương Giả (Tang Khải, Diêu) |
| Earth | khối lượng: trọng lực đạn đạo, phun đá như domino, đập dừng hẳn không nảy | cột bazan góc cạnh vân vàng phun lần lượt, đập dừng chết | đá tròn như củ khoai, khói nâu đục | Genshin (Zhongli), Black Myth (Thạch Tiên Phong, Hoàng Phong Đại Thánh), Phàm Nhân Tu Tiên |
| Wind | áp suất: dòng xoắn tốc độ cao và tâm áp thấp hút vào rồi văng ra | dải xoắn lồng nhau và vòng Mach quanh một mắt áp thấp tối | khói xám mờ trôi chậm | Genshin (Wanderer, Xiao, Kazuha), Naraka (Temulch), donghua Perfect World |
| Ice | ngưng đọng: kết tinh tức thì, đứng yên 0 fps rồi vỡ giòn | vệt và tháp pha lê đứng yên 0,35 s, thú khựng rồi cùng vỡ | dùng đường cong của Thủy, quả cầu tuyết mềm | Genshin (Ayaka, Shenhe, Wriothesley), Doupo Cangqiong (Hải Ba Đông), Vương Giả (Vương Chiêu Quân, Chân Cơ) |

## Phần 3: sản xuất (chỗ khác hoặc thêm so với ChatGPT)

- **Thân lửa bằng "trường nhiệt"** (đáng dùng cho clip lửa trên nền đen, kể cả của Dragonhold):
  - Coi độ sáng clip là nhiệt độ 0–1, rồi tô theo bốn vùng, blend premultiplied (One, OneMinusSrcAlpha):
    - nhiệt dưới 0,12 bị bào bằng nhiễu thành 0, để mép lưỡi lửa sắc;
    - 0,12–0,35 là mép nguội bồ hóng tím than `#240715`, alpha 0,85, che 85 % nền sáng quanh lửa;
    - 0,35–0,80 là thân son `#D93800` tới hổ phách `#FFB703`, alpha 0,95;
    - trên 0,80 là lõi trắng vàng `#FFFDF0` nhân 2,2, chỉ phần này bloom.
  - Cách này chữa đúng lỗi "lửa thành lớp màn" của lửa rồng.
- **Blender cho nước:** Gemini nói **không đáng** cho sóng, dòng kiếm, vùng nước, vì flipbook là tấm phẳng, không uốn theo đường chữ S. Chỉ có thể làm một tấm nổ tung bọt, mà Firefly cộng bào mép bằng shader còn nhanh hơn. ChatGPT nói "có, có chọn lọc" cho 3–4 cú va chạm lớn. Hai bên cùng đồng ý thân nước là lưới cộng shader.
- **Kênh trong suốt:** không bao giờ lấy độ sáng làm alpha cho vật chất tối (nước chàm, đá, cành, băng), vì phần tối sẽ thành trong suốt. Nước dùng lưới cộng mặt nạ SDF; đá dùng lưới đục; lá dùng alpha cắt 0,5.
- **Ngân sách 1,0 ms ở High:**

| Phần | Trần |
|---|---|
| lưới đục, cắt | 0,20 ms |
| dải và flipbook trong mờ | 0,45 ms (chồng tối đa 2,5 lớp, tấm cắt sát hình bát giác) |
| dấu trên đất | 0,10 ms (tối đa 16) |
| pass méo một phần tư độ phân giải | 0,12 ms |
| bloom có sẵn | 0,13 ms |

  Medium 0,6 ms, Low 0,35 ms.
- **Thứ tự:** Hỏa, rồi Thủy, rồi Sabre và Spear với ba hệ đầu để chứng minh ma trận 3 × 3, rồi các hệ còn lại.
