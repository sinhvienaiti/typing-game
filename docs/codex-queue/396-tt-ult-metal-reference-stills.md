# Phiếu 396: Ảnh tham chiếu cho tuyệt kỹ Kim (Geng)


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Clip `ult-metal-geng` bị loại vì có sinh vật vẽ sẵn (kiểm tra 15/11). Làm như phiếu 386 và 391: vẽ ảnh trước, dựng sau.

## Việc
`image_gen`, tối đa 8 lần, 1536×1024, lưu `games/immortality-cultivation/art-src/concept/ult-metal/ult-metal-<tên>.v1-try<k>.png`, prompt thật trong `.prompt.txt` cạnh ảnh.
Ảnh tham chiếu bắt buộc, đưa vào mọi lần tạo và ghi đường dẫn trong prompt:
- `games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.png` (bố cục, camera, mật độ đã duyệt);
- `typing-game-review/captures/tu-tien/clip-content-audit/ult__ult-metal-geng.jpg` (chỉ chất kim loại, ánh sáng; không sinh vật);
- một atlas trong `games/immortality-cultivation/art-src/lab/vfx/metal/`.
Thiếu ảnh bố cục thì dừng và báo; thiếu ảnh clip thì bỏ qua và ghi lại.

Vẽ:
1. Hai khoảnh khắc chiêu, góc camera chơi (nhìn chéo xuống 42–55°), nền đá lát xám tối: hàng trăm lưỡi kiếm khí vàng kim cắm dày ở vành sân 30 m và rải khắp, vết chém sáng trên mặt đất, tia kim loại, đúng một điểm nhấn ở tâm. Không sinh vật, không cảnh vẽ sẵn.
2. Bảng thành phần trên nền đen tuyệt đối, một thành phần mỗi ô, lề ≥ 8 %: 4 biến thể cụm kiếm/lưỡi khí nhìn ngang; mảnh vỡ kim loại và tia lửa; mặt đất vết chém nhìn từ trên (tile được); vòng kiếm xoay dưới chân (nhìn trên, làm decal, không bọc thân).

Phong cách: game tu tiên thương mại, sang trọng, cuốn hút, nhiều lớp, ánh sáng điện ảnh. Không chữ, không watermark.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
Ảnh ghép `ult-metal-sheet-396.jpg` cùng thư mục và `docs/codex-queue/396-report.md` (bản Codex thấy tốt nhất chỉ là gợi ý; owner/Claude chọn).
