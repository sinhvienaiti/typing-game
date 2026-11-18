# Phiếu 451b — Thấu kính và vệt quạt Ánh Sáng

Ngày: 18/11/2026. Phản biện đầu vào: PASS (Sonnet, theo phiếu). Đã tạo đủ 5 ảnh bằng 5 lần gọi công cụ tích hợp `image_gen`; không gọi lại và không dùng công cụ tạo ảnh khác.

## Tệp giao nộp

Tất cả PNG nằm trong [thư mục stills](../../games/immortality-cultivation/art-src/lab/vfx/light/stills/), đều có kích thước **1024×1024**. Prompt nguyên văn nằm cạnh từng ảnh, tên cùng gốc và đuôi `.prompt.txt`.

| Mẫu | Ảnh | Prompt | Lề trống nhỏ nhất |
| --- | --- | --- | --- |
| B1 — vành ngọc chạm bạc | [light-lens-b1.v1-try1.png](../../games/immortality-cultivation/art-src/lab/vfx/light/stills/light-lens-b1.v1-try1.png) | [Prompt B1](../../games/immortality-cultivation/art-src/lab/vfx/light/stills/light-lens-b1.v1-try1.prompt.txt) | 117 px / 11,43% |
| B2 — vành vàng mặt trời | [light-lens-b2.v1-try1.png](../../games/immortality-cultivation/art-src/lab/vfx/light/stills/light-lens-b2.v1-try1.png) | [Prompt B2](../../games/immortality-cultivation/art-src/lab/vfx/light/stills/light-lens-b2.v1-try1.prompt.txt) | 106 px / 10,35% |
| A — vệt trơn | [light-ground-wedge.v1-try1.png](../../games/immortality-cultivation/art-src/lab/vfx/light/stills/light-ground-wedge.v1-try1.png) | [Prompt A](../../games/immortality-cultivation/art-src/lab/vfx/light/stills/light-ground-wedge.v1-try1.prompt.txt) | 74 px / 7,23% |
| B — vân sen mờ | [light-ground-wedge.v1-try2.png](../../games/immortality-cultivation/art-src/lab/vfx/light/stills/light-ground-wedge.v1-try2.png) | [Prompt B](../../games/immortality-cultivation/art-src/lab/vfx/light/stills/light-ground-wedge.v1-try2.prompt.txt) | 74 px / 7,23% |
| C — tia mảnh | [light-ground-wedge.v1-try3.png](../../games/immortality-cultivation/art-src/lab/vfx/light/stills/light-ground-wedge.v1-try3.png) | [Prompt C](../../games/immortality-cultivation/art-src/lab/vfx/light/stills/light-ground-wedge.v1-try3.prompt.txt) | 74 px / 7,23% |

Tờ ghép: [light-lens-wedge-451b.jpg](/private/tmp/typing-game-451b/light-lens-wedge-451b.jpg). Hàng trên: B1, B2; hàng dưới: A, B, C. Thư mục có [ABOUT.md](/private/tmp/typing-game-451b/ABOUT.md).

Dùng thư mục dự phòng được phiếu cho phép vì sandbox chỉ cho ghi repo và thư mục tạm, không cho ghi `/Volumes/SS990TPRO/htdocs/typing-game-review/`. Không cập nhật chỉ mục review bên ngoài sandbox.

## Tham chiếu và xử lý

**Cả hai ảnh sau đều được đính kèm thực tế vào từng lần gọi**, đồng thời có đường dẫn tuyệt đối trong mỗi prompt:

- [light-storyboard.v1-try1.png](../../games/immortality-cultivation/art-src/concept/ult-storyboards/light-storyboard.v1-try1.png): thấu kính tròn cầm tay và hướng quạt tia.
- [ult-light-moment-a.v1-try1.png](../../games/immortality-cultivation/art-src/concept/ult-light/ult-light-moment-a.v1-try1.png): bảng màu vàng–hổ phách và chất liệu.

Công cụ trả ảnh gốc 1254×1254. Dùng ImageMagick 7 để chuẩn hoá, không vẽ thêm hình:

- Thấu kính: làm đều vùng nền nối với góc ngoài bằng màu xám `#808080` (flood-fill, fuzz 6%), thu ảnh vào ô 840×840, thêm nền xám để đạt 1024×1024. Giữ hình dáng, hoa văn, một cán và mặt kính đặc.
- Vệt quạt: đặt điểm đen ở 1% để loại nhiễu nền, cắt phần đen thừa, thu đồng tỷ lệ vào ô 880×880 rồi thêm nền đen đạt 1024×1024. Giữ nguyên hình quạt và chi tiết do công cụ tạo.
- Tờ ghép dùng Arial tại `/System/Library/Fonts/Supplemental/Arial.ttf`.

Đã mở xem hai ảnh tham chiếu, hai mẫu thấu kính và tờ ghép cuối. Đã kiểm tra bằng dữ liệu pixel: đủ 5 PNG, đúng kích thước, đủ lề, nền ngoài xám đồng nhất hoặc đen RGB(0,0,0), đủ 5 prompt có cả hai đường dẫn tham chiếu.

## Owner cần xem

Chọn **B1 hoặc B2** làm hướng nguồn Tripo, và **A/B/C** cho vệt quạt. B có nét sen kéo dài kèm một số tia mảnh; C có thêm hạt sáng theo ảnh tham chiếu. Ba đỉnh quạt đều nằm giữa phía dưới, nhưng khoảng lùi mép dưới khác nhau (A: 94 px; B: 152 px; C: 126 px). Góc mở được yêu cầu khoảng 60° trong prompt; chưa đo góc của đường biên mềm.

Đây là các phương án chờ owner chọn, chưa phải xác nhận đạt 8,5 trong game. Chưa gửi Tripo, chưa ghép vào hiệu ứng hoặc đánh giá trong play host vì nằm ngoài phiếu.

Không bỏ ảnh nào trong 5 ảnh được yêu cầu. Không sửa code, không làm video, không chạy build/test game, không sửa docs Tu Tiên, không thay ảnh đã có trước phiếu và không thao tác commit/push/đổi nhánh.

