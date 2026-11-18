# Báo cáo phiếu 425 — Hai mẫu vương miện máu

Đã hoàn thành bước **2 mẫu trước**, đúng 2 lần gọi công cụ tích hợp `image_gen`; dừng để Claude gửi owner chọn. Chưa tạo mẫu 3–6.

## Tệp giao nộp

Thư mục ảnh: `games/immortality-cultivation/art-src/lab/vfx/blood/stills-55/`.

- `blood-crown.v2-try1.png` và `blood-crown.v2-try1.prompt.txt`.
- `blood-crown.v2-try2.png` và `blood-crown.v2-try2.prompt.txt`.
- `blood-crown-samples-425.jpg`: bảng hai mẫu theo bước lấy mẫu.
- `blood-crown-sheet-425.jpg`: cùng bảng, thêm tên giao nộp ở cuối phiếu để không bỏ sót yêu cầu. Hai JPG có cùng nội dung, nhãn mẫu 1 bên trái và mẫu 2 bên phải.
- Báo cáo: `docs/codex-queue/425-report.md`.

## Tham chiếu và cách tạo

Mỗi lần đều đính kèm đủ ba ảnh của dự án, theo đúng thứ tự sau; đường dẫn tuyệt đối và vai trò có trong từng prompt thật:

1. `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/burst-v2/owner-blood-crown-feedback.webp`: ảnh lỗi để tránh tia kim, vành đều và vũng nứt.
2. `games/immortality-cultivation/art-src/lab/vfx/water/stills-55/water-ring-burst.v1-try1.png`: dáng chất lỏng, vành cong dày và phối cảnh nhìn chéo xuống.
3. `games/immortality-cultivation/art-src/lab/vfx/blood/stills-55/blood-big-burst.v1-try1.png`: đỏ rượu vang, burgundy và ruby; đây là ảnh duy nhất khớp mẫu tên trong thư mục.

Công cụ được chọn theo phiếu: image_gen tạo **một thành phần vương miện chất lỏng**, làm ảnh nguồn cho bước video sau. Không tạo cả kỹ năng hay cảnh nền. Mẫu 1 nhấn vành trước dày, gấp nếp; mẫu 2 nhấn nhánh cong lệch bên trái và các giọt tròn tách khỏi đầu nhánh.

Công cụ trả ảnh gốc 1254×1254 dù prompt yêu cầu 1024×1024. Đã dùng ImageMagick để thu đều về 896×896, đặt giữa nền đen 1024×1024 và đưa nhiễu tối dưới ngưỡng 1% về đen. Không vẽ bổ sung, đổi hình hay cắt thân hiệu ứng. Bản gốc của công cụ được giữ nguyên tại `/Users/toandx/.codex/generated_images/01a1e4d7-ada6-7a91-ac30-ccda87edaad1/`:
- Mẫu 1: `exec-0bcf13ff-2996-4400-8996-4486ed25beed.png`.
- Mẫu 2: `exec-78575d78-1b46-426c-a094-4286ebba26fb.png`.

## Kiểm tra và gợi ý

Đã mở xem ba tham chiếu, hai ảnh tạo và bảng ghép sau chuẩn hóa. Hai PNG giao nộp đều 1024×1024 RGB, nền ngoài đen; không có chữ, sàn, vũng hay tia thẳng đều như ảnh owner phản ánh.

Đo hộp bao toàn bộ pixel khác đen sau chuẩn hóa:
| Mẫu | Hộp bao (rộng × cao + x + y) | Lề nhỏ nhất |
| --- | --- | --- |
| 1 | 652×522+183+242 | 183 px, khoảng 17,9% |
| 2 | 599×493+213+248 | 212 px, khoảng 20,7% |

**Gợi ý owner xem mẫu 2 trước:** nhánh chính cong rõ, đầu nhánh có giọt tròn và thân gọn; tông đỏ thẫm, bóng ướt. Mẫu 1 có vành trước nặng và rộng hơn, phù hợp nếu owner thích cảm giác chất lỏng dày. Đây là gợi ý chọn ảnh nguồn, chưa phải nghiệm thu hiệu ứng trong game.

Owner cần xem độ dày/độ bóng có đọc thành máu ướt hay quá giống ruby, độ sáng lõi giữa và góc nhìn có phù hợp lab 55° không. Hai mẫu đều có điểm sáng nhỏ ở tâm; không dùng điểm sáng này để kết luận chất lượng video hay tiếp đất trong runtime. Góc nhìn hiện được kiểm tra bằng mắt từ ảnh tham chiếu, chưa kiểm chứng bằng camera runtime. Chờ owner chọn trước bước ảnh/video tiếp theo.

## Dừng đúng phạm vi

Không làm video, âm thanh, mã nguồn, build/test, tích hợp game, chấm mù hoặc tạo thêm ảnh. Không xóa/ghi đè ảnh cũ, đổi nhánh, commit hay push. Không sao chép bảng sang thư mục review bên ngoài vì phiếu chỉ cho ghi các đường dẫn giao nộp nêu trên; Claude có thể chuyển bảng cho owner trong bước phối hợp tiếp theo.
