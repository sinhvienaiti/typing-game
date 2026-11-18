# Phiếu 391: Ảnh tham chiếu cho tuyệt kỹ Mộc (vẽ trước, dựng sau)


Phản biện: PASS (Sonnet, 16/11, vòng 2)
## Bối cảnh
Owner duyệt hướng làm chiêu băng v3 "tạm đẹp": vẽ ảnh tham chiếu trước, rồi dựng bằng thành phần. Clip cũ `ult-wood-primordial-tree` bị loại vì có sinh vật vẽ sẵn (kiểm tra 15/11). Làm tiếp chiêu Mộc theo cùng cách phiếu 386.

## Việc
Dùng `image_gen`, tối đa 8 lần, mỗi ảnh 1536×1024, lưu vào `games/immortality-cultivation/art-src/concept/ult-wood/`, tên `ult-wood-<tên>.v1-try<k>.png`, prompt thật lưu cạnh ảnh trong `.prompt.txt`.

Ảnh tham chiếu bắt buộc (đưa vào mọi lần tạo, ghi đường dẫn vào prompt):
- `games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.png` (bố cục, góc camera, mật độ đã được duyệt);
- `typing-game-review/captures/tu-tien/clip-content-audit/ult__ult-wood-primordial-tree.jpg` nếu có (chỉ lấy chất gỗ, lá, ánh sáng; tuyệt đối không sinh vật);
- bộ mộc có sẵn trong `games/immortality-cultivation/art-src/lab/vfx/wood/` nếu có (chọn 1 atlas).

Nếu thiếu ảnh tham chiếu bố cục băng, dừng và báo. Nếu thiếu ảnh clip Mộc, bỏ qua ảnh đó và ghi trong báo cáo.

Cần vẽ:
1. Hai ảnh khoảnh khắc chiêu ở góc camera chơi (nhìn chéo xuống 42–55°) trên nền đá lát xám tối: rễ và dây leo ngọc bích phát sáng mọc lan khắp sân 30 m theo vòng sóng, gai gỗ và chồi non nhô lên dày ở vành, lá và bào tử sáng bay, đúng một điểm nhấn ở tâm (một mầm cây thần sáng). Không sinh vật, không cảnh vẽ sẵn.
2. Bảng thành phần trên nền đen tuyệt đối, một thành phần mỗi ô, lề ≥ 8 %: 4 biến thể cụm rễ/gai gỗ nhìn ngang; lá, bào tử và mảnh gỗ vỡ; mặt đất phủ rễ nhìn từ trên (tile được); vòng dây leo trói quanh chân (nhìn trên, để làm decal xoay, không bọc thân).

Phong cách: game tu tiên thương mại, sang trọng, cuốn hút, chi tiết nhiều lớp, ánh sáng điện ảnh. Không chữ, không watermark.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn. Không commit, không đưa media vào Git, không đổi nhánh.

## Giao nộp
Ảnh ghép `ult-wood-sheet-391.jpg` trong cùng thư mục và báo cáo `docs/codex-queue/391-report.md` (file, prompt, bản Codex thấy đạt nhất và lý do; đây chỉ là gợi ý, owner/Claude chọn bản dùng).
