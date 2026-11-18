# Phiếu 436b: Nữ chính — vẽ lại trang sức bộ Tiên kiếm sương trăng


Phản biện: PASS (Claude, 17/11; phiếu sửa nhỏ một ảnh theo đúng góp ý owner)
## Bối cảnh
Owner 17/11 xem mẫu 436 (`typing-game-review/owner-review/2026-11-17/tu-tien/heroine-fashion/heroine-samples-436.jpg`): "bạn đang vẽ các trang sức quá xấu và không hợp, ai lại vẽ cái vòng toàn kiếm đằng sau như 1 đồ trang sức thế kia". Lỗi do brief: vòng kiếm đeo lưng là ý "vầng kiếm bay" — thứ đó là **hiệu ứng ánh sáng (VFX) bay quanh người**, không phải đồ đeo bằng kim loại. Thân nền và phần áo voan giữ nguyên.

## Việc
Dùng công cụ `image_gen`, tối đa 4 lần. Sửa từ ảnh `games/immortality-cultivation/art-src/heroine/fashion/set-moonfrost.v1-try1.png` (dùng làm ảnh gốc để chỉnh, giữ nguyên người, dáng, áo), lưu `set-moonfrost.v2-try<k>.png` cùng thư mục, prompt thật trong `.prompt.txt`. Ảnh tham chiếu thêm: `typing-game-review/owner-review/2026-11-12/tu-tien/heroine/chan-dung-A.png`.
1. **Bỏ hẳn** vòng kiếm sau lưng. Lưng chỉ có tà áo, dải lụa phiêu đới (piaodai) mềm bay nhẹ hoặc để trơn.
2. **Trang sức tóc** theo kiểu Hán phục thật, thanh nhã, ít mà tinh: một quan nhỏ bạc–ngọc ôm búi tóc, 1–2 trâm bộ diêu có chuỗi ngọc rủ ngắn, hoa văn trăng/mây chạm bạc; không vương miện to, không chi chít.
3. **Đai và vật đeo eo:** đai lụa có khóa bạc nhỏ, một ngọc bội trắng với tua dài xanh nhạt; kiếm đeo bên hông trong vỏ (giữ như cũ nếu đẹp).
4. Trang sức không phát sáng, không tia sáng (hào quang do VFX làm).
Ba góc trước, nghiêng, sau như cũ; nền xám trơn; ánh sáng đều. Không chữ, không watermark.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
Ảnh ghép `heroine-moonfrost-v2-436b.jpg` (bản cũ | bản mới) và `docs/codex-queue/436b-report.md`.
