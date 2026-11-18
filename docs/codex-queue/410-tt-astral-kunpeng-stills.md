# Phiếu 410: Ảnh tham chiếu cho chiêu mở rộng Côn Bằng Tinh Hà


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Kiểm tra clip 15/11 loại `astral-kunpeng` vì có cảnh vẽ sẵn. Làm như 386/391/396/398/399/405/407: vẽ ảnh trước, dựng sau bằng thành phần. Côn Bằng là sinh vật chiêu thức bằng năng lượng (owner 05/11: sinh vật do chiêu gọi ra là hiệu ứng năng lượng trong suốt, không phải nhân vật).

## Việc
`image_gen`, tối đa 6 lần, 1536×1024, lưu `games/immortality-cultivation/art-src/concept/astral-kunpeng/kunpeng-<tên>.v1-try<k>.png`, prompt thật trong `.prompt.txt` cạnh ảnh.
Ảnh tham chiếu bắt buộc mọi lần tạo, ghi đường dẫn trong prompt:
- `games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.png` (góc camera, nền sân);
- `typing-game-review/captures/tu-tien/clip-content-audit/expansion__astral-kunpeng-leviathan.jpg` (chỉ lấy hình dáng và ánh sáng của Côn Bằng; bỏ cảnh nền);
- một atlas trong `games/immortality-cultivation/art-src/lab/vfx/star/`.
Thiếu ảnh bố cục thì dừng; thiếu ảnh khác thì ghi lại.

Vẽ:
1. Hai khoảnh khắc ở góc camera chơi trên nền đá lát xám tối: một Côn Bằng (cá voi khổng lồ hoá chim bằng) làm từ ánh sao xanh lam trong suốt lướt qua sân, đuôi bụi sao, đúng một điểm nhấn; không cảnh nền vẽ sẵn, không sinh vật nào khác.
2. Bảng thành phần trên nền đen tuyệt đối (lề ≥ 8 %): thân Côn Bằng nhìn ngang và nhìn trên (tách riêng), vây/cánh, đuôi bụi sao, bụi sao và sóng xung kích trên đất (decal).

Phong cách: game tu tiên thương mại, sang trọng, cuốn hút, nhiều lớp, ánh sáng điện ảnh. Không chữ, không watermark.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
Ảnh ghép `kunpeng-sheet-410.jpg` trong `art-src/concept/astral-kunpeng/` và `docs/codex-queue/410-report.md` (gợi ý bản tốt; owner/Claude chọn).
