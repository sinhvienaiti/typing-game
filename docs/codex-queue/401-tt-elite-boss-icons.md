# Phiếu 401: Icon nhận biết quái tinh anh và boss


Phản biện: PASS (Sonnet, 16/11; 402 sau khi sửa hai chỗ critic chỉ ra)
## Bối cảnh
Owner 16/11/2026: "quái đặc biệt cũng k cần mang nhãn trên đầu, có thêm icon dạng tinh anh, boss hoặc gì tương tự để nhận biết rõ là được". Bản UI 394 để sẵn chỗ cắm nhưng chưa có art; luật repo cấm icon vẽ bằng CSS hay emoji.

## Việc
`image_gen`, tối đa 8 lần, mỗi ảnh 1024×1024 trên nền đen tuyệt đối (để tách alpha), lưu `games/immortality-cultivation/art-src/ui/icons/foe-<elite|boss>-<kiểu>.v1-try<k>.png`, prompt thật trong `.prompt.txt` cạnh ảnh.
Ảnh tham chiếu bắt buộc mọi lần tạo (đúng bộ UI đã duyệt), ghi đường dẫn trong prompt:
- `games/immortality-cultivation/art-src/ui/icons/hud-coin-jade-jewel-crest.v1-try1.png`;
- `games/immortality-cultivation/art-src/ui/frames/ban-quyet-jewel-crest.v1-try1.png`.

Vẽ:
1. **Tinh anh:** huy hiệu nhỏ dạng ấn ngọc/khiên tu tiên, viền vàng kim, lõi bạc xanh, 2 phương án.
2. **Boss:** huy hiệu lớn và uy hơn, vương miện hoặc ấn đỏ son với ngọc, viền vàng kim, 2 phương án.
Yêu cầu: hình khối rõ, đọc được ở 24–32 px trên nền đá xám tối của sân; không chữ, không watermark; một vật thể giữa khung, lề ≥ 10 %. Phong cách sang trọng, cùng chất liệu với bộ UI tham chiếu.
Sau đó xuất bản thu nhỏ 32 và 48 px của mỗi ảnh (giống cách bộ `hud-coin-*` đã làm), nền trong suốt.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
Ảnh ghép `foe-icons-sheet-401.jpg` (cả bản lớn và bản 32 px đặt trên nền đá xám) trong `art-src/ui/icons/` và `docs/codex-queue/401-report.md`; owner/Claude chọn bản dùng.
