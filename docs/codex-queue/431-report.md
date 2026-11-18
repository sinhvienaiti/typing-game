# Phiếu 431 — Hai mẫu phân cảnh Kim và Lôi

Ngày: 17/11/2026. Trạng thái: **đã làm 2 mẫu, dừng để Claude gửi owner duyệt theo phiếu**.

## Đã làm

Thư mục: `games/immortality-cultivation/art-src/concept/ult-storyboards/`.

| Tệp | Nội dung |
|---|---|
| `metal-storyboard.v1-try1.png` | Kim: trận pháp trên trời → mưa kiếm rơi thẳng → kiếm lớn kết đòn → kiếm tan thành bụi vàng. |
| `metal-storyboard.v1-try1.prompt.txt` | Nguyên văn prompt đã gửi image_gen, đủ đường dẫn và vai trò ba ảnh tham chiếu. |
| `thunder-storyboard.v1-try1.png` | Lôi: tụ mây → sét nối từ quái này sang quái khác → sét lớn từ mây → điện dư tan. |
| `thunder-storyboard.v1-try1.prompt.txt` | Nguyên văn prompt đã gửi image_gen, đủ đường dẫn và vai trò hai ảnh tham chiếu. |
| `ult-storyboard-samples-431.jpg` | Bảng ghép ngang 3072×1024; **Kim bên trái, Lôi bên phải**. Giữ nguyên kích thước hai ảnh, không chèn chữ. |
| `ult-storyboard-samples-431.prompt.txt` | Cách đọc bảng và lệnh ImageMagick thật dùng để ghép; bảng này không gọi image_gen thêm. |

Mỗi PNG là 1536×1024, bốn khung 2×2. Đọc trong từng hệ: **trên trái → trên phải → dưới trái → dưới phải**, tương ứng **tụ lực → phát chiêu → trúng đòn → dư âm**.

Công cụ: image_gen tích hợp, **2 lần gọi / tối đa 14**, mỗi hệ một lần. Chép nguyên PNG được sinh vào đường dẫn trên; chỉ bảng JPEG dùng ImageMagick để ghép. Không sửa hoặc ghi đè ảnh tham chiếu.

## Tham chiếu thực sự đã đưa vào công cụ

- Cả hai: `games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.png` — chỉ lấy góc nhìn và sân đá, bỏ bố cục vòng tròn và băng.
- Kim: `games/immortality-cultivation/art-src/concept/ult-metal/ult-metal-moment-a.v1-try1.png` — màu vàng và chất liệu.
- Kim: `games/immortality-cultivation/art-src/concept/ult-metal/tripo-src/ult-metal-sword.v1-try1.png` — kiếm đã duyệt, lưỡi bạc chạm mây và chuôi vàng.
- Lôi: `games/immortality-cultivation/art-src/lab/vfx/thunder/thunder-big-burst.atlas.png` — điện tím, lõi trắng và nhánh mảnh; không lấy bố cục atlas.

Đã xem các ảnh tham chiếu trước khi sinh. Không dùng ảnh bên thứ ba. Dùng image_gen vì phiếu yêu cầu phân cảnh 2D để duyệt trước khi dựng; đây là minh họa trình diễn theo `ULT_CHOREOGRAPHY.md`, chưa phải thành phần VFX để đưa vào game.

## Kiểm tra và điểm owner cần xem

- Đã kiểm tra kích thước bằng ImageMagick và xem trực tiếp hai ảnh cùng bảng ghép.
- Cả tám khung có người tung chiêu nhỏ ở dưới giữa, quay lưng, sân đá nhìn chéo xuống và đàn quái phía trước; không có chữ hoặc watermark nhìn thấy.
- Kim có nguồn trên không, kiếm hướng mũi xuống, kiếm lớn ở nhịp trúng đòn và bụi vàng ở dư âm; không có vòng trận pháp dưới đất.
- Lôi có đường sét nối qua nhiều quái ở khung phát chiêu, khác rõ với sét lớn từ mây ở khung trúng đòn; không có vòng tròn dưới đất.
- **Kim, khung tụ lực:** mép trận pháp trên trời hơi sát và bị cắt nhẹ ở biên trên. Owner xem có cần nới khoảng trống trên đầu ở lượt tiếp theo.
- Góc nhìn khoảng 55° được yêu cầu trong prompt và kiểm bằng mắt; ảnh sinh không chứng minh được thông số camera chính xác. Các đợt kiếm là gợi ý bằng nhiều độ cao trong ảnh tĩnh, chưa kiểm chứng nhịp 2–3 đợt trong chuyển động.
- Đây là hai mẫu chờ duyệt bố cục và cách ra chiêu; **chưa chấm mù, chưa nghiệm thu 8,5 trong bản chơi**.

## Đã dừng đúng phạm vi

Chưa tạo Tinh Tú, Quang, Phong, Thổ, Băng: phiếu yêu cầu dừng sau hai mẫu, chỉ làm tiếp khi được giao. Không tạo video, không sửa code hoặc tài liệu thiết kế Tu Tiên, không chạy build hay bộ kiểm thử, không đổi nhánh hoặc thực hiện lệnh Git ghi dữ liệu.

Claude gửi bảng ghép cho owner và ghi nhận ý kiến về hai cách trình diễn trước khi giao lượt tiếp theo. Không gặp giới hạn công cụ trong lượt này.
