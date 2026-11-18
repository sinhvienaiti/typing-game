# Phiếu 436 — Thân nền chung và mẫu Tiên kiếm sương trăng

Đã tạo **đúng hai mẫu**, mỗi mẫu một lần bằng công cụ tích hợp `image_gen`: **2/10 lượt**. Dừng ở bước gửi mẫu cho owner theo phiếu; chưa vẽ hai bộ còn lại. Đây là ảnh nguồn để xem thiết kế, **chưa được chấm mù, chưa đạt nghiệm thu 8,5 và chưa dùng để dựng 3D**.

## Tệp giao

| Tệp | Nội dung |
| --- | --- |
| [base-body.v1-try1.png](../../games/immortality-cultivation/art-src/heroine/fashion/base-body.v1-try1.png) | Thân nền áo ôm xám ngà, tóc búi gọn; ba góc trước, nghiêng trái, sau; 1536×1024. |
| [base-body.v1-try1.prompt.txt](../../games/immortality-cultivation/art-src/heroine/fashion/base-body.v1-try1.prompt.txt) | Nguyên văn prompt đã gửi, có đường dẫn hai ảnh tham chiếu. |
| [set-moonfrost.v1-try1.png](../../games/immortality-cultivation/art-src/heroine/fashion/set-moonfrost.v1-try1.png) | Bộ Tiên kiếm sương trăng mặc lên chính tờ thân nền làm ảnh đích; ba góc tương ứng; 1536×1024. |
| [set-moonfrost.v1-try1.prompt.txt](../../games/immortality-cultivation/art-src/heroine/fashion/set-moonfrost.v1-try1.prompt.txt) | Nguyên văn prompt đã gửi, gồm thân nền và hai ảnh tham chiếu bắt buộc. |
| [heroine-samples-436.jpg](/private/tmp/typing-game-436/heroine-samples-436.jpg) | Tờ ghép 1536×2160, thân nền trên và trang phục dưới; giữ nguyên toàn bộ hai ảnh, chỉ thêm nhãn ngoài ảnh bằng ImageMagick. |

**Vị trí tờ ghép:** sandbox phiên này chỉ cho ghi trong repo và thư mục tạm, không cho ghi thư mục SSD bên cạnh repo. Vì vậy tờ ghép và `ABOUT.md` đang ở `/private/tmp/typing-game-436/`. Claude cần chuyển chúng vào `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/heroine-fashion-436/`, rồi chạy `node scripts/review-index.mjs`. Chưa cập nhật chỉ mục; không đặt ảnh ghép vào `art-src`, `public` hay `docs`.

## Tham chiếu và cách tạo

- Khuôn mặt và khí chất: `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/heroine/chan-dung-A.png`.
- Tỷ lệ toàn thân: `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/heroine/dir-a-front.v1-try2.png`.
- Đã đọc hệ ô trang phục trong `docs/games/tu-tien/source/ref-board-characters-fashion-2026-11-17.md` và phân tích phiếu 388. Chỉ gửi hai ảnh của dự án nêu trên vào công cụ; lượt Moonfrost có thêm thân nền vừa tạo. Không gửi ảnh hay bảng tham chiếu của game khác.
- Tờ thân nền được tạo trước, lưu vào repo, rồi dùng chính file đó làm ảnh đích cho lượt mặc đồ. Không sửa, vẽ lại hay đổi kích thước hai PNG sau khi chép từ đầu ra của công cụ. Hai file prompt giữ đúng yêu cầu đã gửi, kể cả các chi tiết công cụ chưa làm đúng.

## Các ô trang phục và chỗ cần sửa trước khi tách mô hình

| Ô | Thấy trong ảnh | Việc cần làm rõ hoặc sửa |
| --- | --- | --- |
| Thân nền, mặt | Cùng dáng cao, eo và chân dài; cổ lộ, tóc búi; ba góc tương ứng. | Owner đối chiếu độ trưởng thành với chân dung A. Mặt trước thân nền còn hơi xoay; tay áo ngắn che một phần đường vai. Chưa phải bản đo giải phẫu hoặc bằng chứng chung skeleton. |
| Tóc | Búi đen gọn được giữ ở Moonfrost; gáy và vai không bị tóc dài phủ. | Tách khối búi và các lọn sát tai khỏi đầu; xác định mặt tiếp xúc với vương miện. Prompt cho phép đổi bạc trắng nhưng file giao vẫn giữ tóc đen. |
| Đầu | Vương miện bạc có trăng khuyết, vòng ôm đầu và giọt trang sức hai bên. | Làm rõ móc lắp; tách giọt treo khỏi tóc và tai, thống nhất điểm gắn giữa ba góc. |
| Bộ áo | Lớp trong trắng ngà, tà ngoài xanh băng, voan xuyên mờ, tay dài và vai có cấu trúc. | Giữ một mesh trang phục theo hệ ô đã chốt; xác định mặt trong, độ dày, lớp che thân và khe giữa các tà. Voan đang phủ chồng lên phần váy, chưa thể tách từ nét ảnh một cách chắc chắn. |
| Đai, đồ treo eo | Đai bạc, khóa trăng và chuỗi giọt xanh đọc được riêng với thân áo. | Các dây treo chạm hoa văn và vạt; cần đường biên, điểm gắn và khoảng hở rõ để không dính vào váy hoặc kiếm. |
| Dải lụa dài | Có các dải xanh dài dọc thân và vạt rủ nhiều lớp. | Ranh giới dải lụa với tà áo còn nhập nhau; cần xác định rõ hai dải độc lập, đầu gắn vào đai và phần chạy xương phụ. |
| Lưng | Vòng bạc và các chi tiết dạng kiếm thấy rõ ở góc sau; góc nghiêng thấy khoảng nhô khỏi áo. | Chốt số lượng chi tiết kiếm; hiện vòng thiên về trang sức với hai chi tiết kiếm hai bên. Giá đỡ cần bản vẽ rõ hơn; xác nhận không gắn nhầm vào áo hoặc vai khi tách. |
| Kiếm | Kiếm trong bao xanh bạc, nằm ngoài hông; có chuôi và đầu bao riêng. | Kiếm ở phía trái tờ nhìn trước, tức hông phải nhân vật, khác phía trái ghi trong prompt. Cần chốt bên đeo và đối chiếu lại góc nghiêng; bổ sung ranh giới kẹp bao, dây treo và mặt khuất. |
| Giày | Thấy ở cả ba góc, cùng bảng màu; thuộc bộ áo lúc ra mắt. | Đối chiếu gót và bàn chân với thân nền trước khi rig; áo che phần lớn cổ chân. |
| Hào quang, hiện diện | Không có lớp VFX vẽ vào ảnh; vòng lưng là vật thể bạc. | Để engine xử lý sau, ngoài phạm vi phiếu này. |

## Kiểm tra và điểm owner cần xem

Đã mở và xem **các file PNG đã lưu** cùng tờ ghép; ImageMagick xác nhận cả hai ảnh nguồn 1536×1024. Có đủ ba góc, toàn thân không bị cắt, nền xám, không chữ hoặc watermark trong ảnh nguồn, không bóng đổ xuống sàn hay hiệu ứng hào quang. Bố cục cơ thể và bàn tay giữa hai mẫu gần trùng nhau bằng quan sát, chưa đo sai lệch mốc hoặc xác nhận bằng mô hình. Đỉnh búi/vương miện khá sát mép trên, chưa đủ khoảng trống 7% đã yêu cầu trong prompt.

Moonfrost thể hiện được lớp lụa–voan, bạc và hình bóng tay áo dài. Bảng màu hướng tới trắng/xanh/bạc 60/30/10, nhưng trắng và xanh đều sáng nên thứ bậc còn mềm; chưa đo tỷ lệ diện tích màu. Vạt dài và voan che phần chân nhiều hơn ý định tà xẻ. Owner cần xem khí chất khuôn mặt, vai có quá cứng không, mức độ sang trọng của trang phục, vòng kiếm và độ rõ của dải lụa trước khi cho sửa hoặc giao tiếp.

Chưa tạo `set-jade-luxe` và `set-crimson-phoenix` vì phiếu yêu cầu dừng sau hai mẫu. Không chạy build/test, không sửa code, không video, không dựng 3D, không đổi nhánh hoặc thao tác commit/push/reset/clean/stash; không xóa hay ghi đè ảnh có sẵn.
