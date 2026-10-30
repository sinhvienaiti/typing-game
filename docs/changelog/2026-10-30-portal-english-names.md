# 30/10/2026 · Tên tiếng Anh và đường ảnh cổng game (phiếu 214)

## Yêu cầu

Theo luật ngôn ngữ và hình ảnh của chủ dự án ngày 28/10, ba thẻ cổng dùng
đúng tên Dragonhold, Wordwoven, Last Line và mô tả tiếng Anh. Biểu tượng
emoji của ba thẻ được bỏ, thay bằng đường ảnh thuộc nguồn của từng game.
Sáu mục cũ giữ nguyên mọi trường, thứ tự và giá trị.

## Thay đổi

- `portal/public/games.json`: đổi tên, mô tả; thay trường `icon` cũ bằng
  `art.icon` và `art.cover` ở ba mục mới. Giữ id, đường dẫn, nguồn và nhóm.
- Thêm `portal/src/game-card.ts`: helper thuần tính URL ảnh, metadata thẻ
  và xử lý lỗi ảnh một lần; chặn đường sai game, đường ngoài nguồn và các
  thành phần đường dẫn không hợp lệ. Mục có `art` không dùng glyph dự phòng.
- `portal/src/main.ts`: trang chủ và menu dùng model chung; ảnh có kích
  thước, alt, tải lười và giải mã bất đồng bộ. Ảnh lỗi tự ẩn; bìa lỗi ẩn
  cả khung. Menu giữ span biểu tượng để nhãn không lệch khi thiếu ảnh.
- `portal/src/styles.css`: thêm bố cục bìa 16:9, biểu tượng thẻ 48 px,
  biểu tượng menu 1,25 em và trạng thái ẩn. Giữ chiều cao tối thiểu 230 px;
  không thêm hình thay thế. Selector tiêu đề đủ độ ưu tiên để canh ảnh.
- `scripts/game-dir.sh`, `scripts/bootstrap.sh`: đổi nhãn console của ba
  game sang tên tiếng Anh; giữ logic, đối số và nhãn Tu Tiên.
- Thêm `portal/tests/game-card.test.mjs` và
  `portal/tests/fixtures/legacy-games.json`. Fixture lấy từ HEAD ban đầu;
  test viết trước mã và nạp helper TypeScript trực tiếp bằng Node 24.
- Báo cáo `docs/codex-queue/214-report.md`; log và đối chiếu phạm vi ở
  `docs/codex-queue/214/`. Không sửa chỉ mục changelog.

## Kiểm tra

Test nền: 11 qua, 0 lỗi. Lượt đỏ trước mã: 14 qua, 37 lỗi trên 51 test.
Sau mã: 51 qua, 0 lỗi, gồm 11 test learning bridge cũ. Build portal,
hai kiểm tra tích hợp và cú pháp hai script đều thoát 0. JS chính tăng
từ 607.871 lên 609.295 byte; CSS từ 127.133 lên 127.854 byte.
Các file của phiếu qua kiểm khoảng trắng; xem báo cáo về năm file chứng
cứ phiếu 194 xuất hiện ngoài phạm vi trong cây dùng chung.

## Claude còn làm

Nhận và duyệt ảnh phiếu 176, 177; chép bản icon 192 và chuyển bìa sang
WebP vào `public/assets/<id>/portal/` của từng game rồi chạy `media:push`.
Last Line hiện chưa có thư mục `public/assets/typing-survival/`.
Trước khi có ảnh, thẻ trở về bố cục chữ khi tải ảnh lỗi.

Kiểm bố cục trang chủ cổng ở 1280 và 1920, cả trước và sau khi gắn ảnh;
kiểm menu gọn khi ảnh thiếu. Duyệt đề xuất tên nhóm và thương hiệu trong
báo cáo, thêm hàng chỉ mục changelog khi commit. Phiếu này không chạy
trình duyệt, dev server, mạng, build/test game, tạo ảnh hay Git ghi.
