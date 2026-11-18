# Báo cáo 436e — Thân nền trưởng thành hơn và bốn bộ thời trang

Ngày: 17/11/2026. Đã tạo đủ ảnh bằng công cụ tích hợp `image_gen`: **5/7 lượt**, mỗi ảnh một lượt; không dùng lượt sửa.

## Ảnh và prompt đã lưu

Thư mục: `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/heroine/fashion/`.

| Ảnh | Kích thước | Nội dung |
| --- | --- | --- |
| `base-body.v3-try1.png` | 1536×1024 | Chỉnh trực tiếp v2: ngực đầy hơn nhẹ, hông/mông tròn hơn, đùi đầy hơn; giữ eo thon. |
| `crimson-bride.v1-try1.png` | 1024×1536 | Váy đỏ ôm xẻ đùi, ren khoét vai, voan đỏ, găng vàng, thêu phượng vàng. |
| `moon-blade.v1-try1.png` | 1024×1536 | Áo ngà ngắn, quần short, tất đen, choàng xanh băng một vai, đai bạc, khăn bạc che mắt và kiếm. |
| `jade-noble.v1-try1.png` | 1024×1536 | Áo xanh ngọc cổ đứng hai tà, quần ngà, áo khoác lửng tay rộng, viền vàng, trâm và ngọc bội lớn. |
| `shadow-spider.v1-try1.png` | 1024×1536 | Áo ren/da đen, hở eo nhẹ, nhiều dải váy đen–rêu, giáp tay vàng, vương miện gai nhỏ, mực trang trí trên tay. |

Mỗi ảnh có prompt thật cùng tên, đổi đuôi `.png` thành `.prompt.txt`; prompt ghi rõ đường dẫn và vai trò của cả hai ảnh đầu vào. PNG được sao chép nguyên bản từ đầu ra công cụ, không chỉnh sửa hình thể sau sinh ảnh.

Thân v3 dùng đúng `base-body.v2-try1.png` làm ảnh đích chỉnh sửa và `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/heroine/chan-dung-A.png` làm tham chiếu khuôn mặt. Cả bốn bộ đều nhận trực tiếp `base-body.v3-try1.png` và cùng ảnh mặt này; không đưa ảnh game khác vào công cụ.

## Tờ ghép để chủ dự án xem

- [Trước/sau thân nền](/private/tmp/typing-game-436e/body-v2-v3-436e.jpg), 3072×1024: **v2 bên trái, v3 bên phải**, cùng kích thước, không co kéo.
- [Bốn bộ thời trang](/private/tmp/typing-game-436e/heroine-lookbook-436e.jpg), 2080×3104: hàng trên crimson-bride / moon-blade; hàng dưới jade-noble / shadow-spider.
- `/private/tmp/typing-game-436e/ABOUT.md` ghi mục đích và điều kiện dọn thư mục.

Dùng thư mục dự phòng của phiếu vì thư mục review nằm ngoài vùng sandbox được phép ghi. Không ghi vào review và không chạy trình dựng chỉ mục của review.

## Kiểm tra và điểm cần xem

Đã kiểm tra kích thước, đủ năm cặp ảnh–prompt và xem trực tiếp từng đầu ra cùng hai tờ ghép. Quan sát thân v3 vẫn giữ ba góc, tư thế, chiều cao/chân dài, mặt, đồ lót xám, giày thấp, nền, ánh sáng và thước sát v2; mức tăng đường cong có chủ ý nhẹ. Mốc khoảng 7,9 đầu đã được chủ dự án chấp nhận được giữ làm hướng dẫn, không ép lại 8,5 đầu. Tỷ lệ eo/hông 0,7 là hướng dẫn trong prompt; ảnh 2D không xác nhận được số đo vòng cơ thể.

Bốn bộ có tư thế riêng, ánh sáng sân khấu, thấy trọn người và giày; không thấy chữ, watermark hay hào quang. Chủ dự án cần xem mức đầy đặn của v3 và độ giống mặt qua các góc. Riêng crimson-bride, mạng voan đang được vén sang bên để lộ mặt, chưa phủ kín mặt. Moon-blade có khăn bạc trong, vẫn thấy mắt.

Không tạo thêm lượt vì chưa thấy lệch người/mặt rõ cần sửa. Đây là ảnh giao để chủ dự án chọn; chưa có hai giám khảo độc lập và không tuyên bố đạt cổng chất lượng 8,5 hay đã được duyệt để đưa vào game.

Không sửa code, không làm video, không chạy build/test của game, không xóa/ghi đè ảnh cũ, không commit/push hay đổi nhánh. Không bỏ sót ảnh hoặc tờ ghép nào của phiếu.
