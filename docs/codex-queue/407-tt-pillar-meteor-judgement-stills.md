# Phiếu 407: Ảnh tham chiếu cho hai chiêu trụ: Thiên Thạch Hỏa và Thẩm Phán Quang


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Kiểm tra clip 15/11 loại `pillar-fire-meteor` (cảnh vẽ sẵn) và `pillar-light-judgement` (sinh vật vẽ sẵn). Làm như các phiếu 386/391/396/398/399/405: vẽ ảnh trước, dựng sau theo thành phần. Owner 12/11: hiệu ứng làm từ thành phần dùng lại, không vẽ cả cảnh trong một ảnh để dùng thẳng.

## Việc
`image_gen`, tối đa 8 lần (khoảng 4 mỗi chiêu), 1536×1024, lưu `games/immortality-cultivation/art-src/concept/pillar-<meteor|judgement>/pillar-<tên>.v1-try<k>.png`, prompt thật trong `.prompt.txt` cạnh ảnh.
Ảnh tham chiếu bắt buộc mọi lần tạo, ghi đường dẫn trong prompt:
- `games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.png` (góc camera, nền sân, mức chi tiết đã duyệt);
- `typing-game-review/captures/tu-tien/clip-content-audit/ult__pillar-fire-meteor.jpg` hoặc `ult__pillar-light-judgement.jpg` (chỉ lấy chất liệu, ánh sáng; tuyệt đối không cảnh vẽ sẵn, không sinh vật);
- một atlas cùng hệ trong `games/immortality-cultivation/art-src/lab/vfx/fire/` hoặc `.../light/`.
Thiếu ảnh tham chiếu bố cục thì dừng; thiếu ảnh khác thì ghi lại.

Mỗi chiêu vẽ: một khoảnh khắc ở góc camera chơi (nhìn chéo xuống 42–55°) trên nền đá lát xám tối, vùng trụ đường kính khoảng 6 m, đúng một điểm nhấn; và một bảng thành phần trên nền đen tuyệt đối (lề ≥ 8 %): 4 biến thể hình chính nhìn ngang, mảnh/hạt, vết trên đất nhìn từ trên (tile được), vòng ấn dưới chân (decal).
- Thiên Thạch Hỏa: một khối thiên thạch nóng chảy rơi chéo, đuôi lửa, va đất thành hố than hồng và sóng lửa.
- Thẩm Phán Quang: cột sáng vàng trắng từ trời giáng xuống, vòng phù văn trên đất, tia sáng mảnh và bụi sáng.

Phong cách: game tu tiên thương mại, sang trọng, cuốn hút, nhiều lớp, ánh sáng điện ảnh. Không chữ, không watermark.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
Ảnh ghép `pillar-<meteor|judgement>-sheet-407.jpg` mỗi chiêu và `docs/codex-queue/407-report.md` (gợi ý bản tốt; owner/Claude chọn).
