# Phiếu 436k — Ảnh nguồn hair cards nữ chính

Ngày 18/11/2026. Phiếu đã có phản biện PASS (Sonnet, vòng 3).

**Đã tạo đủ bốn loại ảnh, dùng đủ 6/6 lần gọi `image_gen`. Số lọn đều đủ, nhưng chưa có tấm nào đạt toàn bộ chỉ tiêu kỹ thuật; không đánh dấu PASS.** Hai lượt vẽ lại dành cho A và C. Không có lỗi hạn mức dịch vụ hay thời điểm chờ do công cụ trả về.

## Nguồn và cách xuất

- Tham chiếu duy nhất: `games/immortality-cultivation/art-src/heroine/fashion/base-body.v6B-turn.v1-try2.png`, được đính kèm trực tiếp trong cả sáu lần gọi; chỉ lấy màu tóc đen ánh nâu và độ bóng.
- Mỗi prompt yêu cầu 2048×2048, nhưng công cụ đều trả **1254×1254**. Giữ nguyên sáu PNG gốc, không ghi đè. Bốn bản có hậu tố `.2048.png` được xuất thêm bằng ImageMagick: `-filter Lanczos -resize 2048x2048!`; đây là phóng ảnh, không phải ảnh gốc 2K.
- Không chỉnh sáng, sắp lại lọn, tách alpha hoặc vẽ thêm sợi bằng mã. Chưa dựng thẻ tóc hay tích hợp Blender.
- Thư mục ảnh và prompt: `games/immortality-cultivation/art-src/heroine/hair/`.
- Mỗi PNG có một tệp cùng tên gốc và đuôi `.prompt.txt`, lưu nguyên văn prompt đã gửi. Prompt của bản `.2048` là bản sao prompt nguồn; thao tác xuất được ghi ở trên.

## Toàn bộ ảnh gốc và số lọn

Các đường dẫn dưới đây tương đối với thư mục ảnh nêu trên. Đếm bằng mắt và đối chiếu các nhóm hình chiếu của điểm ảnh Y≥0,04; một lọn gồm nhiều sợi, không đếm từng sợi thành một lọn.

| Thứ tự gọi | PNG gốc | Số lọn | Bố cục | Y trung bình | Nhận xét |
| --- | --- | ---: | --- | ---: | --- |
| 1 | `hair-cards-a.v1-try1.png` | 8 | 1×8 | 0,16143 | Quá tối, khe 5–9 px ở ảnh gốc; giữ lại để đối chiếu. |
| 2 | `hair-cards-a.v1-try2.png` | 8 | 1×8 | 0,24953 | Sáng hơn rõ; vẫn thấp hơn 0,25, không làm tròn thành đạt. |
| 3 | `hair-cards-b.v1-try1.png` | 12 | 2×6 | 0,21403 | Có lọn hơi cong; quá rộng và còn tối. |
| 4 | `hair-cards-c.v1-try1.png` | 20 | 2×10 | 0,18831 | Có sợi bay nhưng phần lớn lọn còn dày; giữ lại để đối chiếu. |
| 5 | `hair-cards-d.v1-try1.png` | 6 | 2 hàng × 3 cột | 0,20181 | Đủ sáu xoắn; lọn lớn và toàn lưới lệch xuống dưới. |
| 6 | `hair-cards-c.v1-try2.png` | 20 | 2×10 | 0,21960 | Thu mảnh đáng kể, khe rộng; vẫn còn tối. |

## Bốn bản xuất 2048×2048 để xem xét

Số đo dưới đây tính lại trên **bản xuất**, không suy ra bằng cách nhân hệ số ảnh gốc. Kích thước bao gồm độ cong và sợi bay còn thấy ở ngưỡng đo. Khe ngang là khoảng trống giữa hộp bao của **hai lọn khác nhau** trong cùng hàng; các khoảng nhỏ giữa sợi thuộc cùng lọn không tính thành khe liên lọn.

| PNG xuất | Số lọn | Rộng × dài/cao của các lọn (px) | Khe ngang nhỏ nhất | Khe giữa hàng | Lề ngoài nhỏ nhất | Y trung bình |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| `hair-cards-a.v1-try2.2048.png` | 8 | 193–224 × 1775–1791 | 21 px | — | 73 px | 0,24905 |
| `hair-cards-b.v1-try1.2048.png` | 12 | 228–260 × 922–954 | 82 px | 70 px | 34 px | 0,21306 |
| `hair-cards-c.v1-try2.2048.png` | 20 | 46–84 × 879–892 | 118 px | 106 px | 62 px | 0,21710 |
| `hair-cards-d.v1-try1.2048.png` | 6 | 578–607 × 618–641 | 29 px | 38 px | 96 px | 0,20154 |

Phương pháp: `Y=(0,2126R+0,7152G+0,0722B)/255` trên giá trị RGB sRGB mã hóa, thang 0–1; loại điểm ảnh Y<0,04 rồi lấy trung bình của phần còn lại. Đây là độ chói trên ảnh mã hóa, không phải phép tuyến tính hóa ánh sáng. Không dùng độ sáng của cả tấm vì nền chiếm diện tích lớn.

Số đo và chương trình đo nằm ở `/private/tmp/typing-game-436k/measure-native.json`, `measure-2048.json` và `measure.py`. Hộp bao từng lọn được lưu trong JSON. Hàng được chia theo khe đen thực tế, không cắt cứng giữa tấm; điều này cần thiết vì D lệch xuống. Với C sau phóng ảnh, các sợi trong cùng lọn có thể tách thành vài nhóm hình chiếu nhỏ; bảng vẫn đếm 10 lọn mỗi hàng theo khoảng cách và quan sát, không đếm các mảnh đó thành lọn mới.

## Kiểm tra và phần chưa đạt

- **Số lọn:** A 8, B 12, C 20, D 6; không thiếu lọn ở bất kỳ lần thử nào. Nhìn kiểm tra không thấy hai lọn độc lập chồng lên nhau.
- **Gốc–ngọn:** cả hai thử A, B và hai thử C đều đi từ phía trên xuống, phần thân dày ở trên và đuôi thuôn xuống dưới; C2 có gốc nhỏ vì là tóc con. D có đường sợi cuộn vào đầu thuôn tại tâm, nhưng điểm bắt đầu dày đúng vị trí 12 giờ không đủ rõ để xác nhận đạt.
- **A2:** dài nằm trong 1600–1800 px; có lọn rộng tới 224 px, vượt 220 px. Khe nhỏ nhất 21 px, thiếu 3 px so với yêu cầu. Độ sáng sát ngưỡng nhưng vẫn chưa đạt.
- **B:** lọn rộng 228–260 px, vượt 90–140 px; một số dài tới 954 px, vượt 950 px. Khe và lề đạt ở ngưỡng đo, độ sáng không đạt.
- **C2:** dài 879–892 px, khe và lề đạt; một số lọn có hộp bao rộng tới 84 px, vượt 60 px. Độ sáng không đạt. C1 rộng và tối hơn nên không dùng trong tờ ghép chính.
- **D:** cần sáu ô 600×600 px tại x=124…1924, y=424…1624, mỗi xoắn khoảng 500 px. Thực tế hộp bao tổng nằm x=96…1950, y=493…1797; lọn cao tới 641 px, không nằm gọn trong các ô quy định và lưới lệch xuống. Khe, lề ngoài đạt theo ngưỡng; kích thước, vị trí lưới và độ sáng không đạt.
- **Nền:** nhìn là đen, nhưng chưa đen tuyền tuyệt đối. Dải mép ngoài 32 px của bản xuất vẫn có nhiễu rất thấp: giá trị kênh lớn nhất A/C/D là 2/255, B là 7/255. Không tuyên bố mọi điểm ảnh nền đều RGB(0,0,0). Nhiễu này dưới ngưỡng loại 0,04 của phép đo.
- **Chi tiết:** nhìn thấy sợi nhỏ và dải bóng ngang; không có đầu người, da, phụ kiện, chữ hoặc lưới vẽ trong ảnh nguồn.

## Tờ ghép và giao nộp

- Tờ ghép đã mở kiểm tra: [hair-cards-436k.jpg](/private/tmp/typing-game-436k/hair-cards-436k.jpg), gồm A2, B1, C2, D1, có số lọn và cảnh báo chưa đạt ngay dưới mỗi tấm.
- Dùng đường dẫn dự phòng `/private/tmp/typing-game-436k/` vì quyền ghi của phiên không bao gồm thư mục `typing-game-review` bên cạnh repo. Có `ABOUT.md`; không ghi ra thư mục review và không chạy trình dựng lại chỉ mục ngoài phạm vi.
- Đã giữ 6 PNG gốc + 4 PNG xuất 2048, cùng 10 prompt; không xóa hay ghi đè ảnh có sẵn.
- Owner cần xem **độ sáng**, bề rộng B/C, khe A và bố cục D trước khi dùng cho tóc dạng thẻ. Đây là các nguồn còn lỗi kỹ thuật, chưa phải bộ atlas đạt đủ yêu cầu để giao thẳng sang Blender.
- Không vẽ thêm quá giới hạn sáu lần. Không sửa mã, không sửa tài liệu Tu Tiên, không làm âm thanh/video, không chạy build/test, không thực hiện thao tác Git.
