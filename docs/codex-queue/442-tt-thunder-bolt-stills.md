# Phiếu 442: Ảnh tĩnh tia sét năng lượng dày cho tuyệt kỹ Lôi

Phản biện: PASS (Sonnet, 17/11)

## Bối cảnh
Owner nhận xét ngày 17/11: "tia lôi nhìn vẫn xấu quá nhỉ, nó như các cái que ấy, không thể áp dụng dạng năng lượng to hơn dầy hơn". Owner chọn làm theo cách đã áp dụng cho cú nổ của Quang: ảnh tĩnh → owner chọn → Firefly image-to-video → Codex gắn vào. Phiếu này chỉ làm bước ảnh tĩnh.

## Việc
Dùng công cụ `image_gen`, tối đa 4 lần (4 biến thể, mỗi biến thể 1 lần).

Ảnh tham chiếu (chỉ ảnh của dự án, ghi đường dẫn vào prompt):
- `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`, nửa phải: hình, màu và độ dày của tia sét. Ô dưới trái là cú sét lớn.
- `games/immortality-cultivation/art-src/lab/vfx/light/stills-55/light-prism-burst.v1-try4.png`: cách trình bày đã được duyệt (một thành phần, nền đen, lề, chấm đáy).

Quy tắc chung cho cả 4 biến thể:
- Mỗi ảnh chỉ có **một** thành phần trên nền đen tuyền, nhìn từ camera chơi chếch xuống khoảng 55°.
- Kích thước 1024×1024. Mọi phần sáng nằm trong vùng 12–88 % theo cả hai chiều.
- Tia sét phải là **dòng năng lượng dày**: thân rộng, lõi trắng tím (lõi ≤ 30 % là trắng), quầng tím điện dày nhiều lớp, có nhánh phụ, có hạt điện lấp lánh. Không phải nét mảnh hay que.
- Không vẽ mặt đất, quái, nhân vật, mây hay chữ. Không vòng tròn, không mandala.

Bốn biến thể:
- **A: cú sét lớn đánh thẳng xuống.** Thân dày chiếm khoảng 12–18 % bề ngang khung, đi từ mép trên vùng an toàn xuống chấm đáy ở 80 % chiều cao. Có 6–10 nhánh phụ tỏa ra, chân sét bùng sáng ở chấm đáy.
- **B: như A**, nhưng thân xoắn hai luồng năng lượng quấn nhau.
- **C: một đoạn sét nối ngang giữa hai quái** (sét dây chuyền). Đoạn sét dày nằm ngang, nghiêng theo phối cảnh, hai đầu có chấm sáng neo, có nhánh phụ ngắn.
- **D: như C**, nhưng dạng dải plasma cuộn sóng, dày hơn.

Lưu ảnh ở `games/immortality-cultivation/art-src/lab/vfx/thunder/stills-55/thunder-bolt-thick.v1-try<k>.png`, kèm `.prompt.txt`.
Ghép tờ `thunder-bolt-thick-442.jpg` có nhãn A–D. Nếu sandbox không cho ghi thư mục review thì để ở `/private/tmp/typing-game-442/`.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh, không dùng ảnh của game khác.

## Giao nộp
`docs/codex-queue/442-report.md`.
