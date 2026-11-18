# Phiếu 440: Ảnh tĩnh "nổ ánh sáng lăng kính" cho cú kết của Quang

Phản biện: PASS (Sonnet, 17/11, vòng 3)

## Bối cảnh
Ngày 17/11 owner đồng ý đổi cách làm cú nổ cuối của chiêu Quang. Sau 4 lần sửa bằng code (439 đến 439d), cú nổ vẫn nhỏ và yếu. Cách mới theo luật "thành phần trước":
1. Vẽ một thành phần ảnh tĩnh, owner duyệt.
2. Làm Firefly image-to-video từ ảnh đó.
3. Codex gắn video vào điểm trúng.

Phiếu này chỉ làm bước 1.

## Việc
Dùng công cụ `image_gen`, tối đa 4 lần: 4 biến thể, mỗi biến thể 1 lần.

Ảnh tham chiếu (chỉ ảnh của dự án, ghi đường dẫn vào prompt):
- `games/immortality-cultivation/art-src/concept/ult-storyboards/light-storyboard.v1-try1.png`: lấy ô dưới trái làm đích về hình và độ lực của cú nổ.
- `games/immortality-cultivation/art-src/concept/ult-light/ult-light-moment-a.v1-try1.png`: lấy màu và chất liệu (vàng ấm, lõi trắng, tia hổ phách, hạt lấp lánh).

Mỗi biến thể là **một** cú nổ ánh sáng, không có gì khác trong khung:
- Nhìn từ camera chơi chếch xuống khoảng 55°, đặt ở tâm khung.
- Nền đen tuyền, để code cộng sáng lên cảnh.
- Lõi trắng ấm nhỏ (≤ 30 % là trắng), quanh lõi có:
  - tia sao (starburst) mềm dài ngắn khác nhau;
  - tia lửa lăng kính bắn tỏa có vệt;
  - quầng vàng hổ phách;
  - hạt lấp lánh.
- Điểm chạm đất là một chấm sáng nhỏ (không phải mặt phẳng hay mặt đất) nằm ở giữa theo chiều ngang, ở 62 % chiều cao khung tính từ trên, để code gắn decal và ánh sáng.
- Không vẽ mặt đất, quái, nhân vật hay chữ. Không vòng tròn đồng tâm, không mandala.
- Khung an toàn chung cho cả A, B, C, D: mọi phần sáng nằm trong vùng từ 12 % đến 88 % theo cả hai chiều (lề ≥ 12 % mỗi cạnh). Chấm chạm đất (62 % từ trên) là **đáy** cú nổ; phần sáng phía trên đáy cao tối đa tới mốc 12 % (tức ≤ 50 % chiều cao khung), phần dưới đáy (tia lửa văng) tối đa tới mốc 88 %. Bề ngang mọi biến thể ≤ 76 % bề rộng. Kích thước 1024×1024.

Bốn biến thể khác nhau về dáng:
- A: tia sao 8 cánh nghiêng theo phối cảnh;
- B: bùng dọc lên cao như cột lửa sáng ngắn;
- C: hoa sáng nở xòe thấp sát đất;
- D: cầu sáng vỡ ra nhiều mảnh lăng kính.

Lưu `games/immortality-cultivation/art-src/lab/vfx/light/stills-55/light-prism-burst.v1-try<k>.png`, kèm `.prompt.txt`. Ghép tờ `light-prism-burst-440.jpg` có nhãn A–D. Nếu sandbox không cho ghi thư mục review, để tờ ghép ở `/private/tmp/typing-game-440/`.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh. Không dùng ảnh của game khác.

## Giao nộp
`docs/codex-queue/440-report.md`.
