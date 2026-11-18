# Phiếu 418: Ảnh tĩnh đúng góc 55° cho 10 clip bùng nổ trượt (làm khung đầu cho video)


Phản biện: PASS (Sonnet, 16/11, vòng 2)
## Bối cảnh
Loạt Firefly 16/11 (`typing-game-review/owner-review/2026-11-16/tu-tien/burst-remake/batch-sheets.jpg`): tạo từ mô tả chữ thì Firefly bỏ qua góc nhìn và vẽ khói/khí thành hoa văn đối xứng (mandala). Owner 16/11 chọn: "Đồng ý, ảnh trước rồi video". Luật owner 16/11, nguyên văn: "các video phải được tạo đảm bảo chất lượng và phù hợp góc nhìn, đảm bảo để code có thể tích hợp thêm 1 số hiệu ứng khi gây ra ở mặt đất, nhìn chân thật không bị cảm giác ảo" — tức clip phải đúng góc camera chơi (~55° nhìn xuống), chỉ năng lượng trên nền đen, có điểm chạm đất rõ để code gắn decal/bụi/ánh sáng, chân thật.

## Việc
`image_gen`, tối đa 14 lần, mỗi ảnh 1024×1024, lưu `games/immortality-cultivation/art-src/lab/vfx/<hệ>/stills-55/<clip>.v1-try<k>.png`, prompt thật trong `.prompt.txt`.
10 clip: `dark-ring-burst`, `water-ring-burst`, `poison-big-burst`, `poison-ring-burst`, `blood-big-burst`, `wood-big-burst`, `dark-big-burst-white`, `dark-ground-impact-white`, và hai clip bị cắt từ 414: `thunder-impact`, `star-ring-burst`.
Ảnh tham chiếu bắt buộc mọi lần (ghi đường dẫn): một khung đẹp nhất của clip được hai giám khảo chấm A — `art-src/lab/vfx/earth/earth-big-burst.atlas.png` hoặc `thunder/thunder-big-burst.atlas.png` (độ khối, ánh sáng); và `art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.png` (đúng góc camera chơi 42–55°).
Mỗi ảnh: **khoảnh khắc đỉnh** của hiệu ứng, nhìn chéo xuống ~55°, vòng/vụ nổ thành hình **bầu dục** đúng phối cảnh (không tròn phẳng nhìn thẳng từ trên); khối năng lượng có chiều cao, nổi lên từ một điểm chạm ở giữa-dưới; không đối xứng kiểu hoa văn, có hỗn loạn tự nhiên (khói cuộn bất đối xứng, tia lệch); lề ≥ 15 % mọi cạnh; nền đen tuyệt đối; không mặt đất, không vết cháy, không sinh vật, không chữ. Màu theo hệ (dark tím đen, water xanh nước, poison xanh lục độc, blood đỏ thẫm, wood xanh lục + gỗ, thunder tím trắng, star vàng trắng; bản `-white` là khói xám trắng trung tính).

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
Ảnh ghép `stills-55-sheet-418.jpg` trong `typing-game-review/owner-review/2026-11-16/tu-tien/burst-remake/` (nếu sandbox chặn, để trong `art-src/lab/vfx/` và ghi đường dẫn) và `docs/codex-queue/418-report.md`.
