# Phiếu 318 · Vệt chém Ám nền trắng

Đã gọi `image_gen` **4 lần**: 3 dáng ban đầu và 1 lần vẽ lại heavy vì điểm đúng dáng dưới 8. Đã chép bằng `cp -n`, giữ cả hai bản heavy. Không gặp giới hạn công cụ.

Thư mục D: `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/`. Đã thêm 4 PNG và 4 tệp `.prompt.txt` cùng tên. Mỗi prompt giữ nguyên câu dáng và đuôi đã chỉ định, thay chất liệu, đổi nền trắng và thêm câu giới hạn màu; ghi đủ đường dẫn ảnh tham chiếu. Mỗi lần gọi đính kèm đúng ảnh `dark-slash-<dáng>.v1-try1.png` và `dark-comet-white.v1-try1.png`, đã mở bằng `view_image` trước khi tạo.

Đã xem ảnh sinh ra và bản thu nhỏ rộng 200 px trong bộ nhớ, không ghi ảnh kiểm tra. Điểm **tự chấm** 0–10; chung là trung bình bốn mặt, làm tròn một chữ số.

| Ảnh trong D | Khổ thật | Cuốn hút | Đúng dáng | Rõ ở 200 px | Sạch | Chung | Nhận xét |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `dark-slash-quick-white.v1-try1.png` | 1672 × 941 | 8,4 | 8,8 | 8,5 | 8,0 | **8,4** | Vệt mảnh thuôn sắc, thân khói hiện rõ; chi tiết lấp lánh mất bớt khi thu nhỏ. |
| `dark-slash-heavy-white.v1-try1.png` | 1670 × 942 | 8,5 | 7,2 | 8,8 | 8,0 | **8,1** | Khối khói dày có lực nhưng hướng cong lệch ảnh dáng, nên đã vẽ lại. |
| `dark-slash-heavy-white.v1-try2.png` | 1672 × 941 | 8,6 | 8,9 | 9,0 | 8,0 | **8,6** | Hướng quét gần bản nền đen hơn, khói cuộn dày và mép chém rõ; đề xuất xem bản này. |
| `dark-slash-thrust-white.v1-try1.png` | 1670 × 942 | 8,5 | 8,8 | 8,6 | 8,0 | **8,5** | Mũi đâm dài nhọn và vòng xoáy gốc phân biệt rõ, thân khói còn đọc được ở 200 px. |

**Anh cần xem:** thân khói của cả ba dáng, heavy bản 2 và độ đỏ của mép chém. Nền nhìn trắng nhưng chưa trắng thuần RGB 255: các góc đã đo nằm khoảng 253–255 mỗi kênh; giữ nguyên ảnh sinh ra, không hậu kỳ. Các bản là ảnh tạo mới theo tham chiếu, chưa căn khớp từng pixel với bản nền đen để ghép hai lớp. Chưa nghiệm thu trong game hay chấm mù độc lập.

Không bỏ sót dáng; không vẽ lại quick/thrust vì các mặt đều ≥ 8. Không tích hợp, xử lý nền hoặc căn lớp vì ngoài phiếu. Chỉ thêm ảnh/prompt trong D và báo cáo này; không sửa/xóa tệp cũ, chạy build/test, mở cổng mạng hay dùng lệnh Git ghi.
