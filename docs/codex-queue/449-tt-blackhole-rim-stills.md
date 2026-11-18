# Phiếu 449: Ảnh tĩnh viền sáng quanh lõi hố đen (Hư Không)

Phản biện: PASS (Sonnet, 18/11)

## Bối cảnh
Bản 447b (`typing-game-review/owner-review/2026-11-18/tu-tien/void-blackhole-lab-b.jpg`) đã có lõi cầu 3D đen, nhưng lõi chỉ là một khối đen đặc, nhìn như cái đĩa. Trong phân cảnh đã duyệt, quanh lõi có viền sáng mỏng.

Owner chọn ngày 18/11: "Thêm viền sáng + vành rực hơn". Viền sáng phải làm từ ảnh, không vẽ bằng code. Code sẽ đặt ảnh này ngay sau quả cầu, quay mặt về camera. Vì bóng của khối cầu nhìn từ góc nào cũng là hình tròn, nên viền luôn khớp.

## Việc
Dùng công cụ `image_gen`, đúng 3 lần (3 biến thể A–C, mỗi biến thể 1 lần).

Ảnh tham chiếu, chỉ dùng ảnh của dự án và ghi đường dẫn vào prompt:
- `games/immortality-cultivation/art-src/concept/ult-void/blackhole/void-blackhole-storyboard.v1-try1.png`, ô 2 và ô 3: viền sáng mỏng quanh quả cầu đen.
- `games/immortality-cultivation/art-src/concept/ult-void/blackhole/void-accretion-ring.v1-try1.png`: màu vàng trắng và chất liệu.

Yêu cầu chung cho mỗi ảnh:
- Khổ 1024×1024, nền đen tuyền.
- Ở giữa là một **hình tròn đen tuyền rỗng**, đường kính đúng 50 % bề ngang khung, mép tròn sắc.
- Quanh mép hình tròn có viền sáng vàng trắng, sát mép, rất mảnh ở trong, toả mềm ra ngoài tới khoảng 70–80 % bề ngang khung.
- Không vẽ quả cầu, vành bồi tụ hay chữ.

Ba biến thể:
- **A:** viền đều, mảnh, sáng như nhật hoa khi nhật thực.
- **B:** viền sáng hơn ở một bên, có vài tia lửa xoáy nhẹ theo mép.
- **C:** viền mảnh, kèm các sợi sáng rất mảnh bị hút cong vào mép.

Lưu ảnh ở `games/immortality-cultivation/art-src/concept/ult-void/blackhole/void-core-rim.v1-try<k>.png`, kèm `.prompt.txt` cùng tên.

Ghép tờ `void-core-rim-449.jpg` có nhãn A–C. Nếu sandbox không cho ghi vào thư mục review, để tờ ghép ở `/private/tmp/typing-game-449/`.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh. Không dùng ảnh của game hoặc truyện bên ngoài.

## Giao nộp
`docs/codex-queue/449-report.md`.
