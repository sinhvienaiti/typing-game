# Phiếu 429: Ảnh nguồn sạch cho Tripo — kiếm Kim và mảnh kính Hư Không (không vệt sáng)


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Mẫu Tripo đầu tiên (`typing-game-review/owner-review/2026-11-16/tu-tien/ult-3d-models/tripo-metal-sample.jpg`) dựng từ ảnh có vệt sáng quấn quanh kiếm: Tripo biến vệt sáng thành dây vàng mảnh rối và chất vàng bị đục. Owner 16/11 chọn: "Vẽ lại ảnh nguồn sạch rồi Tripo lại". Ánh sáng, vệt và phát sáng sẽ do VFX trong game làm, ảnh nguồn chỉ cần hình khối vật thể.

## Việc
Dùng công cụ `image_gen`: **2 mẫu trước** (1 Kim, 1 Hư Không), ghép `tripo-src-samples-429.jpg`, dừng và ghi báo cáo để Claude gửi owner. Chỉ khi được giao tiếp mới làm thêm; tổng tối đa 8 lần. 1024×1024, lưu `games/immortality-cultivation/art-src/concept/ult-<metal|void>/tripo-src/<tên>.v1-try<k>.png`, prompt thật trong `.prompt.txt`.
Ảnh tham chiếu bắt buộc mọi lần (ghi đường dẫn): ảnh nguồn cũ `games/immortality-cultivation/art-src/concept/ult-metal/ult-metal-blade-src.v1.png` (hình dáng cụm 3 kiếm, cần giữ), ảnh thành phần `.../ult-metal/ult-metal-components.v1-try2.png` hoặc `.../ult-void/ult-void-components.v1-try2.png`.
Yêu cầu chung (để Tripo dựng tốt): một vật thể đặc, nhìn 3/4 từ trên hơi chéo, ánh sáng studio đều mềm, **không vệt sáng, không hạt, không quầng, không bloom, không dây hay sợi mảnh**, nền xám trung tính trơn, lề ≥ 12 %, hình khối rõ, bề mặt chi tiết.
- Kim: cụm 3 thanh kiếm tu tiên cắm đất (giữ dáng ảnh cũ), lưỡi thép bạc sáng có khắc hoa văn, đốc và chắn kiếm vàng chạm trổ, chân là khối đá/kim loại vỡ nhỏ.
- Hư Không: cụm 3–4 mảnh kính tinh thể tím trong, cạnh sắc, có vết nứt bên trong, đế là mảnh vỡ nhỏ.
Phong cách vật phẩm game tu tiên thương mại cao cấp. Không chữ, không watermark.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
`docs/codex-queue/429-report.md`.
