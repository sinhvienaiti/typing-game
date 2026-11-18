# Phiếu 452b: Đầu và đuôi sao băng cho tuyệt kỹ Tinh Tú

Phản biện: PASS (Sonnet, 18/11)

## Bối cảnh
Kế hoạch tuyệt kỹ Tinh Tú nằm ở `docs/work/tasks/star-ult-plan.md` (hàng 6 và 7): bảy viên sao băng rơi chéo, mỗi viên bắn tỉa một con quái. Owner đã chọn chòm sao mẫu A (`games/immortality-cultivation/art-src/lab/vfx/star-ult/stills/star-constellation.v1-try1.png`). Đầu và đuôi sao băng là hai thành phần riêng; code đặt chúng thành billboard, xoay theo hướng bay và phóng to thu nhỏ đều.

## Việc
Dùng công cụ `image_gen`, đúng 5 lần.

Ảnh tham chiếu, chỉ dùng ảnh của dự án và ghi đường dẫn vào prompt:
- `games/immortality-cultivation/art-src/lab/vfx/star-ult/stills/star-constellation.v1-try1.png`: màu vàng trắng, quầng tím chàm, kiểu tia chữ thập.
- `games/immortality-cultivation/art-src/concept/ult-storyboards/star-storyboard.v1-try1.png`: dáng sao băng rơi chéo.

Yêu cầu chung: nền đen tuyền, chỉ một thành phần, không chữ, không đất, không quái.
1. **Đầu sao băng A, B, C** (`star-meteor-head`): 1024×1024, nhìn ngang. Một lõi sao vàng trắng có quầng tím chàm, không đuôi dài. Lõi trắng ≤ 30 % đường kính. Lề ≥ 12 %.
   - A: tia chữ thập bốn cánh.
   - B: tám tia mảnh như kim cương.
   - C: lõi tròn, quầng nhiều lớp.
2. **Đuôi sao băng A, B** (`star-meteor-trail`): 1536×1024. Dải nằm ngang, đầu sáng ở mép phải, tan dần về trái. Dải có độ dày, kiểu chuỗi hạt sáng vàng xen tím chàm. Mọi phần sáng nằm trong vùng 10–90 % theo chiều dọc.
   - A: dải liền, hạt sáng dọc theo dải.
   - B: chuỗi hạt rời, to dần về phía đầu.

Lưu ở `games/immortality-cultivation/art-src/lab/vfx/star-ult/stills/<tên>.v1-try<k>.png`, mỗi ảnh kèm `.prompt.txt`. Ghép thành một tờ `star-meteor-452b.jpg`; nếu không ghi được thư mục review thì để ở `/private/tmp/typing-game-452b/`.

## Ràng buộc
Không sửa code, không làm video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh. Không dùng ảnh của game khác.

## Giao nộp
`docs/codex-queue/452b-report.md`, gồm danh sách ảnh.
