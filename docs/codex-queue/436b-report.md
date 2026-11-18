# Phiếu 436b — Sửa trang sức Tiên kiếm sương trăng

Đã sửa từ chính ảnh Moonfrost v1 bằng công cụ tích hợp `image_gen`, **1/4 lượt**. Bản mới giữ người, dáng, bố cục ba góc và bộ áo theo quan sát đối chiếu; thay trang sức theo góp ý owner. Dừng ở mẫu để owner xem, chưa chấm mù hoặc nghiệm thu 8,5.

## Tệp giao

| Tệp | Nội dung |
| --- | --- |
| [set-moonfrost.v2-try1.png](../../games/immortality-cultivation/art-src/heroine/fashion/set-moonfrost.v2-try1.png) | Ảnh sửa 1536×1024; chép nguyên đầu ra công cụ, không hậu kỳ PNG. |
| [set-moonfrost.v2-try1.prompt.txt](../../games/immortality-cultivation/art-src/heroine/fashion/set-moonfrost.v2-try1.prompt.txt) | Nguyên văn prompt đã gửi, có đường dẫn và vai trò của cả hai ảnh đầu vào. |
| [heroine-moonfrost-v2-436b.jpg](/private/tmp/typing-game-436b/heroine-moonfrost-v2-436b.jpg) | Tờ ghép 3072×1080: bản cũ bên trái, bản mới bên phải. ImageMagick chỉ ghép nguyên ảnh và thêm nhãn bên ngoài. |

## Nội dung đã sửa và kiểm tra

- Bỏ toàn bộ vòng kim loại, kiếm nhỏ và các chốt trang sức sau lưng; phục hồi mặt vải thêu. Góc nghiêng không còn cụm vật thể nhô ra sau lưng.
- Thay vương miện và trăng đứng cao bằng quan bạc–ngọc nhỏ ôm búi, trâm có chuỗi hạt ngắn; giữ búi tóc đen.
- Thay đai kim loại và chuỗi đá nhiều nhánh bằng đai lụa xanh băng, khóa bạc nhỏ, một ngọc bội trắng và tua chỉ xanh nhạt dài. Giữ kiếm trong vỏ bên hông.
- Giữ áo trắng–xanh, voan, tay áo, dáng đứng và ba góc trước–nghiêng–sau. Đây là nhận xét thị giác, không phải xác nhận trùng từng điểm ảnh.
- Đã xem ảnh đầu vào, đầu ra và tờ ghép đã lưu; xác nhận kích thước bằng ImageMagick, bản PNG lưu trong repo trùng SHA-256 với đầu ra công cụ. Nền xám, ánh sáng đều; không thấy chữ, watermark, trang sức phát sáng hay tia sáng trong PNG.

Hai ảnh đưa vào công cụ đều của dự án: ảnh đích `games/immortality-cultivation/art-src/heroine/fashion/set-moonfrost.v1-try1.png` và chân dung hỗ trợ `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/heroine/chan-dung-A.png`. Không gửi ảnh bên thứ ba. Đây là sửa nhỏ theo phiếu đã có phản biện PASS, không mở hướng thiết kế mới.

## Bàn giao và phần bỏ qua

Sandbox chỉ cho ghi repo và thư mục tạm, không cho ghi thư mục review bên cạnh repo. Vì vậy tờ ghép cùng `ABOUT.md` ở `/private/tmp/typing-game-436b/`. Claude cần chuyển hai tệp này vào `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/heroine-fashion-436b/`, rồi chạy `node scripts/review-index.mjs`. Chưa chuyển hoặc cập nhật chỉ mục; không đặt tờ ghép vào `art-src`, `public` hay `docs`.

Không tạo thêm ba lượt vì lượt đầu đã thể hiện các sửa đổi yêu cầu. Owner cần xem kích thước và độ thanh nhã của quan/trâm, cùng ngọc bội–tua eo trên tờ so sánh. Không sửa code, chạy build/test, làm video, dựng 3D, đổi nhánh, xóa hoặc ghi đè ảnh cũ; không commit/push/reset/clean/stash.
