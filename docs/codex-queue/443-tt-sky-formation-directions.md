# Phiếu 443: Ba hướng thiết kế trận pháp trên trời (ảnh 2D để owner chọn)

Phản biện: PASS (Sonnet, 17/11)

## Bối cảnh
Ngày 17/11 owner chê trận pháp trên trời của chiêu Kim: "vòng trận pháp cũng quá xấu, nó không hề nhìn đẹp chút nào, góc nhìn có vẻ nó cũng đang sao, có vẻ phần thiết kế cho trận pháp ở trên trời cần được phân tích và làm tỉ mỉ hơn". Ảnh lỗi: `typing-game-review/owner-review/2026-11-17/tu-tien/metal-sword-mix.jpg` (khung 1,2 s).

Claude phân tích ra các lỗi:
- Đĩa vòng chỉ có một lớp, nét vàng mảnh, nằm gần sát đầu quái nên trông như hình vẽ dưới đất.
- Không có chiều sâu và không có lớp chồng.
- Tia sáng chiếu sai hướng.

Luật của owner cho trận pháp:
- Phải là trận pháp tu tiên huyền bí: vòng chữ cổ, bát quái, hoa sen. Không dùng hình học cơ bản.
- Vòng phải là dải năng lượng dày, nhiều lớp, đang chuyển động. Không dùng nét mảnh.
- Vật thể trên trời phải là hình 3D thật, nhìn đúng ở camera chơi.

Ngày 17/11 owner chọn "làm tiếp trận pháp" và muốn được xem các hướng thiết kế trước khi dựng.

## Việc
Dùng công cụ `image_gen`, tối đa 6 lần (3 hướng; mỗi hướng tối đa 2 lần).

Ảnh tham chiếu (chỉ dùng ảnh của dự án, ghi đường dẫn vào prompt):
- `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`, nửa trái, ô trên trái: lấy camera, cảnh, chất liệu và màu vàng.
- `games/immortality-cultivation/art-src/concept/ult-metal/rain-components/formation-topdown.v1-try1.png`: lấy hoạ tiết chữ cổ. Cách trình bày phải làm lại, không bê nguyên.

Mỗi hướng là **một khung cảnh** 1536×1024 nhìn từ camera chơi chếch xuống 55°. Người tung chiêu nhỏ ở giữa đáy khung, nhìn từ sau lưng; đàn quái ở phía trước; nền đá tối.

Trận pháp treo **cao trên trời**, phía trên và phía sau đàn quái, có các dấu hiệu độ cao rõ ràng:
- khoảng trống lớn giữa trận pháp và quái;
- ánh sáng rủ xuống từ mặt dưới trận;
- một vùng sáng mờ in trên mặt đất bên dưới.

Trận pháp gồm 3–5 lớp vòng dày, đặt ở các độ cao khác nhau, quay ngược chiều nhau. Mặt dưới các lớp phát sáng. Hoạ tiết là chữ cổ, bát quái hoặc sen. Chỉ có một điểm nhấn sáng nhất.

Ba hướng:
- **A, Kiếm trận:** vòng chữ cổ dày, quanh vành treo hàng trăm thanh kiếm chĩa xuống.
- **B, Bát quái thiên môn:** các lớp bát quái chồng tầng, ở giữa là cửa sáng.
- **C, Sen vàng:** đài sen vàng nhiều cánh mở từ trời, cánh sen là các dải năng lượng.

Phong cách: game tu tiên thương mại cao cấp, cuốn hút, sang trọng, nhiều lớp chi tiết. Không chữ, không watermark.

Lưu ảnh ở `games/immortality-cultivation/art-src/concept/ult-metal/sky-formation/sky-formation-<a|b|c>.v1-try<k>.png`, kèm `.prompt.txt` cho mỗi ảnh. Ghép tờ `sky-formation-443.jpg` có nhãn A, B, C. Nếu sandbox không cho ghi thư mục review thì để tờ ghép ở `/private/tmp/typing-game-443/`.

## Ràng buộc
Không sửa code, không làm video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh. Không dùng ảnh của game khác.

## Giao nộp
`docs/codex-queue/443-report.md`.
