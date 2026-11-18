# Phiếu 436c: Nữ chính, hai bộ thời trang Jade-luxe và Crimson-phoenix (ảnh 2D)

Phản biện: PASS (Sonnet, 17/11; vòng 1 chỉ lỗi đường dẫn tuyệt đối, đã sửa)

## Bối cảnh
Ngày 17/11 owner duyệt cách làm trang sức của Moonfrost v2 (436b) và đồng ý vẽ tiếp hai bộ còn lại theo đúng hướng đó. Câu của owner: "đồng ý".

Ở bản trước, owner đã chê trang sức: "ai lại vẽ cái vòng toàn kiếm đằng sau như 1 đồ trang sức thế kia". Vì vậy trang sức phải là đồ hán phục thật, nhỏ và tinh tế: quan búi tóc, trâm hoặc bộ diêu có chuỗi hạt ngắn, đai lụa, ngọc bội, tua chỉ, hoa tai nhỏ. Không vòng kim loại, không kiếm nhỏ làm trang sức, không vật nhô ra sau lưng, không vương miện cao.

## Việc
Dùng công cụ `image_gen`, tối đa 4 lần (mỗi bộ tối đa 2).

Mỗi bộ là một bảng 3 góc (trước, nghiêng, sau), kích thước 1536×1024. Giữ đúng người, khuôn mặt, dáng chữ A, tỷ lệ cơ thể, nền xám trơn và ánh sáng đều như Moonfrost v2.

Ảnh đầu vào bắt buộc (chỉ ảnh của dự án, ghi đường dẫn vào prompt):
- `games/immortality-cultivation/art-src/heroine/fashion/base-body.v1-try1.png`: thân nền, người và dáng.
- `games/immortality-cultivation/art-src/heroine/fashion/set-moonfrost.v2-try1.png`: mức độ và cỡ trang sức đã duyệt, bố cục ba góc.
- `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/heroine/chan-dung-A.png`: khuôn mặt.

1. **`set-jade-luxe`** (Ngọc tu sang trọng hiện đại):
   - lụa xanh ngọc bích đậm và ngà, cắt gọn hiện đại, áo khoác ngoài dáng dài có cổ đứng, thêu chỉ vàng nhạt hoạ tiết mây;
   - trang sức ngọc: quan ngọc nhỏ, trâm ngọc có hạt ngọc trai, đai lụa với khóa vàng nhỏ, ngọc bội xanh, tua chỉ;
   - kiếm trong vỏ bên hông;
   - tỷ lệ màu ~60/30/10.
2. **`set-crimson-phoenix`** (Phượng kiếm đỏ thẫm):
   - lụa đỏ thẫm và đen, viền vàng; voan đỏ nhiều lớp ở tà; hoạ tiết lông phượng thêu (thêu trên vải, không phải vật nhô ra);
   - trang sức: bộ diêu phượng nhỏ bằng vàng gắn búi, hoa tai hạt đỏ, đai lụa đen khóa vàng, ngọc bội đỏ, tua chỉ;
   - kiếm trong vỏ bên hông;
   - tỷ lệ màu ~60/30/10.

Mỗi phần (tóc, đầu, áo, đai, kiếm) vẽ rõ ranh giới để sau tách mô hình.

Phong cách: nhân vật game tu tiên thương mại cao cấp, cuốn hút, sang trọng, thời trang. Không chữ, không watermark, không hào quang hay hiệu ứng sáng.

Lưu ảnh ở `games/immortality-cultivation/art-src/heroine/fashion/<tên>.v1-try<k>.png`, kèm prompt thật trong `.prompt.txt` cùng tên. Ghép tờ `heroine-sets-436c.jpg` gồm Moonfrost v2, Jade và Crimson. Nếu sandbox không cho ghi thư mục review, để tờ ghép ở `/private/tmp/typing-game-436c/`.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
`docs/codex-queue/436c-report.md`.
