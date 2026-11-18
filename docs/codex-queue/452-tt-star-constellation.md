# Phiếu 452 (chòm sao): Ảnh tĩnh chòm Bắc Đẩu trên trời cho tuyệt kỹ Tinh Tú

Phản biện: PASS (Sonnet, 18/11)

## Bối cảnh
Tuyệt kỹ Tinh Tú (`docs/games/tu-tien/ULT_CHOREOGRAPHY.md`, dòng Tinh Tú): người tung vẽ một chòm sao trên trời. Sau đó từng viên sao băng rơi chéo, bắn tỉa từng con quái. Kế hoạch: `docs/work/tasks/star-ult-plan.md`.

Chòm sao là một thành phần riêng. Code sẽ dán nó lên một mặt phẳng 3D nằm ngang trên trời, cao khoảng 14 m, phía sau đàn quái. Vì vậy ảnh phải **nhìn thẳng từ trên xuống 90°**, theo luật camera của owner ngày 17/11.

Phiếu này chỉ vẽ ảnh tĩnh để owner chọn. Sau khi owner chọn, ảnh sẽ được làm thành video "vẽ nét" bằng Firefly.

## Việc
Dùng công cụ `image_gen`, đúng 2 lần: 2 biến thể, mỗi biến thể 1 lần.

Ảnh tham chiếu (chỉ ảnh của dự án, ghi đường dẫn vào prompt):
- `games/immortality-cultivation/art-src/concept/ult-storyboards/star-storyboard.v1-try1.png`, ô trên trái: chòm sao mở, góc cạnh, nút sao vàng trắng, quầng tím chàm. Chỉ lấy màu và chất liệu, không lấy góc nhìn 55°.
- `games/immortality-cultivation/art-src/concept/ult-star/ult-star-components.v1-try1.png`, ô dưới thứ ba: một mảnh chòm sao trên nền đen. Lấy cách trình bày và chất liệu nút sao.
- `games/immortality-cultivation/art-src/concept/ult-metal/sky-formation/sky-formation-simple-a.v1-try1.png`: cách trình bày đã được duyệt cho một mảng trên trời nhìn từ trên xuống (nền đen, một lớp, nét dày, có khoảng tối để nhìn xa vẫn đọc được).

Mỗi ảnh 1536×1024, nền đen tuyền, chỉ một thành phần, mọi phần sáng nằm trong vùng 10–90 % theo cả hai chiều, **nhìn thẳng từ trên xuống 90°** (texture phẳng, không vẽ sẵn phối cảnh hay elip). Không vẽ đất, quái, nhân vật, mây dày hay chữ đọc được.

Chung cho cả hai:
- Đúng **7 nút sao** xếp theo hình **Bắc Đẩu Thất Tinh**: bốn sao làm gàu, ba sao làm cán. Chòm sao chiếm khoảng 75 % bề ngang khung.
- Mỗi nút là một ngôi sao vàng trắng có tia chữ thập ngắn và quầng tím nhạt. Lõi trắng không quá 30 % đường kính nút. Nút cuối cán (Dao Quang) to hơn khoảng 1,4 lần.
- Các nút nối nhau bằng **dải năng lượng vàng ấm có độ dày** (khoảng 1–1,5 % bề ngang khung) và có hạt lấp lánh dọc theo dải. Không vẽ nét chỉ mảnh, không vẽ que.
- Là sơ đồ sao mở, góc cạnh. Không vòng tròn, không mandala, không trận đồ đồng tâm.
- Phần tỏa sáng phụ dịu, không trắng xoá. Chỉ các nút sao là sáng nhất.

Hai biến thể:
1. **`star-constellation` A:** như trên, thêm một làn tinh vân tím chàm mỏng, mờ, bám dọc theo các dải nối. Giữa các phần vẫn đen tuyền.
2. **`star-constellation` B:** như trên, không có tinh vân. Bên cạnh mỗi nút có một hoạ tiết triện cổ nhỏ, mảnh, mờ (kiểu tinh đồ cổ Trung Hoa, không phải chữ đọc được). Dải nối dày hơn A một chút.

Lưu ảnh ở `games/immortality-cultivation/art-src/lab/vfx/star-ult/stills/<tên>.v1-try<k>.png` (k = 1 cho A, 2 cho B), kèm `.prompt.txt`. Ghép tờ `star-constellation-452.jpg` có nhãn A/B vào `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/star-ult/`. Nếu sandbox không cho ghi vào thư mục review, để tờ ghép ở `/private/tmp/typing-game-452/`.

## Ràng buộc
Không sửa code, không làm video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh. Không dùng ảnh của game khác hay ảnh bên thứ ba.

## Giao nộp
`docs/codex-queue/452a-report.md`.
