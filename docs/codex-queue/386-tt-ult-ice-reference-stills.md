# Phiếu 386: Ảnh tham chiếu cho tuyệt kỹ băng (vẽ trước, dựng sau)

Phản biện: PASS (Sonnet, 16/11)

## Bối cảnh
Owner 16/11/2026 về bản lưới 3D của phiếu 385: "xấu đến đáng sợ… tự style… bạn nên tạo ảnh trước, sau đó làm theo ảnh đó". Bản video cũ `ult-ice-cold-silence` bị loại vì có tượng thú vẽ sẵn. Owner thích mật độ tinh thể và độ hoành tráng của video đó.

## Việc
Dùng công cụ `image_gen`. Tối đa 8 lần `image_gen`. Mỗi ảnh 1536×1024, lưu vào `games/immortality-cultivation/art-src/concept/ult-ice/`, đặt tên `ult-ice-<tên>.v1-try<k>.png`, và lưu prompt thật đã dùng vào file `.prompt.txt` cạnh ảnh.

Ảnh tham chiếu bắt buộc (đưa vào mọi lần tạo, ghi đường dẫn vào từng prompt):
- `games/immortality-cultivation/art-src/lab/vfx/ice/ice-ground-mark.atlas.png`
- `games/immortality-cultivation/art-src/lab/vfx/ice/ice-big-burst.atlas.png`
- `typing-game-review/captures/tu-tien/clip-content-audit/ult__ult-ice-cold-silence.jpg`: chỉ lấy mật độ tinh thể, ánh sáng và chất băng; tuyệt đối không có thú, tượng hay hình người.

Cần vẽ:
1. **Hai ảnh khoảnh khắc chiêu**, góc camera chơi (nhìn chéo xuống 42–55°), trên nền đá lát xám tối. Mặt sân phủ băng trong có vết nứt. Các cụm tinh thể kim cương sắc nét, trong suốt, lõi xanh băng, viền sáng trắng, cao thấp xen kẽ. Có sương lạnh, bông tuyết, ánh lấp lánh. Đúng một điểm nhấn sáng ở tâm. Không có sinh vật nào.
2. **Bảng thành phần trên nền đen tuyệt đối**, một thành phần mỗi ô, nhìn thẳng ngang, cách lề ≥ 8 %:
   - một tấm 4 biến thể cụm tinh thể;
   - một tấm mảnh vỡ băng và bụi lấp lánh;
   - một tấm mặt băng nứt nhìn từ trên xuống (texture vuông, tile được);
   - một tấm vỏ băng bọc một khối tròn trung tính (không vẽ con thú), nhìn ngang và nhìn trên.

Phong cách: game tu tiên thương mại, sang trọng, cuốn hút, chi tiết nhiều lớp, ánh sáng điện ảnh. Không chữ, không watermark.

## Ràng buộc
- Không sửa code, không tạo video, không xoá hay ghi đè ảnh có sẵn.
- Không commit, không đưa media vào Git, không đổi nhánh.

## Giao nộp
- Một ảnh ghép tất cả các bản `ult-ice-sheet-386.jpg` trong cùng thư mục.
- Báo cáo `docs/codex-queue/386-report.md`: danh sách file, prompt đã dùng, bản nào đạt nhất theo Codex và lý do (chỉ là ý kiến, không phải điểm duyệt).
