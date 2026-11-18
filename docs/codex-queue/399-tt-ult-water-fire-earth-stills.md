# Phiếu 399: Ảnh tham chiếu cho ba tuyệt kỹ Thủy, Hỏa, Thổ


Phản biện: PASS (Sonnet, 16/11)

## Bối cảnh
Clip `ult-water-profound-sea-v2`, `ult-fire-one-spark`, `ult-earth-ink-peaks` bị loại vì có sinh vật hoặc cảnh vẽ sẵn (kiểm tra 15/11). Làm như 386/391/396: vẽ ảnh trước, dựng sau.

## Việc
`image_gen`, tối đa 12 lần tổng (khoảng 4 mỗi chiêu), 1536×1024, lưu `games/immortality-cultivation/art-src/concept/ult-<water|fire|earth>/ult-<hệ>-<tên>.v1-try<k>.png`, prompt thật trong `.prompt.txt` cạnh ảnh.
Ảnh tham chiếu bắt buộc mọi lần tạo, ghi đường dẫn trong prompt:
- `games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.png` (bố cục, camera, mật độ đã duyệt);
- ảnh clip tương ứng trong `typing-game-review/captures/tu-tien/clip-content-audit/` (`ult__ult-water-profound-sea-v2.jpg`, `ult__ult-fire-one-spark.jpg`, `ult__ult-earth-ink-peaks.jpg`): chỉ lấy chất liệu và ánh sáng, tuyệt đối không sinh vật;
- một atlas cùng hệ trong `games/immortality-cultivation/art-src/lab/vfx/<water|fire|earth>/` nếu có.
Thiếu ảnh bố cục thì dừng; thiếu ảnh khác thì ghi lại.

Mỗi chiêu vẽ: một khoảnh khắc ở góc camera chơi (nhìn chéo xuống 42–55°) trên nền đá lát xám tối, phủ sân 30 m, đúng một điểm nhấn ở tâm, không sinh vật, không cảnh vẽ sẵn; và một bảng thành phần trên nền đen tuyệt đối (lề ≥ 8 %): 4 biến thể hình chính nhìn ngang, mảnh/hạt, mặt đất nhìn từ trên (tile được), vòng trói dưới chân (decal, không bọc thân).
- Thủy: sóng nước trong xanh dâng thành vòng, giọt và bọt sáng, xoáy nước dưới chân.
- Hỏa: một tia lửa nhỏ nổ thành biển lửa vàng cam, than hồng, khói mỏng.
- Thổ: núi đá mực nhô lên từ mặt đất, vết nứt phát sáng vàng đất, bụi đá.

Phong cách: game tu tiên thương mại, sang trọng, cuốn hút, nhiều lớp, ánh sáng điện ảnh. Không chữ, không watermark.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
Một ảnh ghép mỗi chiêu `ult-<hệ>-sheet-399.jpg` và `docs/codex-queue/399-report.md` (gợi ý bản tốt; owner/Claude chọn).
