# Phiếu 436: Nữ chính — thân nền chung và các bộ thời trang thay được (ảnh 2D)


Phản biện: PASS (Sonnet, 17/11)
## Bối cảnh
Owner 17/11: "phần thiết kế thời trang rất quan trọng, sau này sẽ có thể đổi quần áo của nhân vật, nên phải phát triển theo hướng này"; và "hướng phong cách lúc tạo nhân vật, người chơi có thể chọn… thời trang thì sẽ được chọn". Nên không chọn một phong cách: vẽ **một thân nền** dùng chung và **nhiều bộ thời trang** mặc lên đúng thân nền đó. Hệ ô trang phục và 3 hướng: `docs/games/tu-tien/source/ref-board-characters-fashion-2026-11-17.md` (mục "Proposed outfit slot system" và các hướng nữ chính). Phân tích lỗi bản cũ: `docs/codex-queue/388-report.md` (vai vuông, thứ bậc thị giác, tỷ lệ màu).

## Việc
Dùng công cụ `image_gen`: **2 mẫu trước** — (1) thân nền, (2) bộ thời trang "Tiên kiếm sương trăng" mặc trên đúng thân nền đó — ghép `heroine-samples-436.jpg`, dừng và ghi báo cáo để Claude gửi owner. Chỉ khi được giao tiếp mới vẽ 2 bộ còn lại. Tổng tối đa 10 lần. 1536×1024, lưu `games/immortality-cultivation/art-src/heroine/fashion/<tên>.v1-try<k>.png`, prompt thật trong `.prompt.txt`.
Ảnh tham chiếu bắt buộc (ghi đường dẫn; chỉ ảnh của dự án, **không** dùng ảnh game khác): `typing-game-review/owner-review/2026-11-12/tu-tien/heroine/chan-dung-A.png` (khuôn mặt, khí chất trưởng thành đã được khen), `games/immortality-cultivation/art-src/heroine/dir-a-front.v1-try2.png` (tỷ lệ cơ thể).
1. **Thân nền** (`base-body`): bảng 3 góc (trước, nghiêng, sau) tư thế chữ A cho rig, cùng một người: lớp áo lót ôm sát trung tính (xám ngà, không hoa văn), tóc buộc gọn để thấy cổ và vai, tỷ lệ kiếm tu cao ráo, vai vuông nhẹ. Ánh sáng đều, nền xám trơn, không bóng đổ, không hiệu ứng sáng.
2. **Bộ "Tiên kiếm sương trăng"** (`set-moonfrost`): cùng 3 góc, cùng tư thế và tỷ lệ, mặc lên đúng thân nền: voan trắng xanh nhạt nhiều lớp, tay áo dài, đai bạc, tà áo xẻ có dải lụa dài; vương miện trăng khuyết (ô đầu), vật đeo lưng hình vòng kiếm (ô lưng). Tỷ lệ màu ~60/30/10. Mỗi phần (tóc, đầu, bộ áo, đai, lưng, kiếm) vẽ rõ ranh giới để tách thành mô hình riêng.
Hai bộ sau (khi được giao tiếp): `set-jade-luxe` (Ngọc tu sang trọng hiện đại) và `set-crimson-phoenix` (Phượng kiếm đỏ thẫm), cùng quy tắc.
Phong cách: nhân vật game tu tiên thương mại cao cấp, cuốn hút, sang trọng, thời trang, nhiều lớp chất liệu. Không chữ, không watermark. Không vẽ hào quang hay hiệu ứng (để VFX làm).

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
`docs/codex-queue/436-report.md` (kèm bảng các ô trang phục thấy trong ảnh và chỗ nào cần sửa để tách mô hình).
