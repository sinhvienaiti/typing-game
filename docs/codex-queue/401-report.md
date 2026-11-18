# Phiếu 401 — Icon nhận biết quái tinh anh và boss

Ngày: 16/11/2026. **Đã tạo đủ bốn phương án, chờ owner/Claude chọn. Chưa nối code, chưa nghiệm thu trong game.**

## Đã làm

Dùng `image_gen` tích hợp **4/8 lượt**, mỗi lượt một huy hiệu. Cả bốn lượt đều cấp trực tiếp đúng hai ảnh tham chiếu của phiếu:

- `games/immortality-cultivation/art-src/ui/icons/hud-coin-jade-jewel-crest.v1-try1.png`;
- `games/immortality-cultivation/art-src/ui/frames/ban-quyet-jewel-crest.v1-try1.png`.

Hai mẫu đầu E1/B1 đã hiện trực tiếp cho owner trước khi tạo E2/B2. Không gửi ảnh bên thứ ba cho công cụ. Không tạo video, âm thanh hay ảnh quái vật.

Tất cả ảnh dưới đây nằm trong `games/immortality-cultivation/art-src/ui/icons/`:

| Mã trên tấm ghép | Phương án | Ảnh lớn 1024×1024 |
| --- | --- | --- |
| E1 | Tinh anh: khiên ngọc, lõi bạc xanh, viền vàng | `foe-elite-jade-shield.v1-try1.png` |
| E2 | Tinh anh: ấn ngọc hình thoi bậc, lõi bạc xanh, viền vàng | `foe-elite-jade-seal.v1-try1.png` |
| B1 | Boss: vương miện ba đỉnh, men đỏ son và ngọc, viền vàng | `foe-boss-imperial-crown.v1-try1.png` |
| B2 | Boss: ấn đỏ son bát giác, ngọc giữa và vai mây vàng | `foe-boss-cinnabar-seal.v1-try1.png` |

Mỗi ảnh lớn có hai bản cùng tên gốc, thêm `-32.png` và `-48.png`: **8 PNG RGBA trong suốt**. Cả 12 PNG đều có `.prompt.txt` cùng tên chứa prompt thực đã gửi, hai đường dẫn tham chiếu và ghi chú xử lý xác định. Bản lớn ghi đường dẫn ảnh nguồn công cụ, còn giữ nguyên tại thư mục mặc định.

**Tấm ghép để chọn:** `foe-icons-sheet-401.jpg` (1640×1060), kèm `.prompt.txt` mô tả cách ghép. Có bốn ảnh lớn, các hàng 24/32/48 px thật và cặp nguồn sinh / sau chuẩn hóa. Hàng 32/48 dùng đúng file PNG giao nộp; hàng 24 chỉ là preview, không tạo thêm asset runtime.

Nền tấm ghép lấy cục bộ từ ảnh sân sẵn có `games/immortality-cultivation/art-src/ground/thanh-thach/court-paving.v2.png`, giảm sáng ×0,60 để đối chiếu trên đá xám tối. Ảnh nền này **không** được gửi cho `image_gen`; tấm ghép không phải capture game. Font Arial tại đường dẫn hệ thống được chỉ định trong phiếu.

## Kiểm tra

- Đã mở xem cả hai ảnh tham chiếu, bốn ảnh sinh và tấm ghép cuối. Huy hiệu xanh có đường bao khiên/thoi; huy hiệu đỏ có đường bao vương miện/ấn rộng. Không thấy chữ hoặc watermark trên huy hiệu. Đánh giá này chỉ phục vụ giao mẫu, không phải điểm chấm mù.
- Công cụ trả ảnh 1254×1254 dù prompt yêu cầu 1024×1024. Đã chuẩn hóa bằng ImageMagick 7: xóa vùng gần đen nối với mép bằng liên thông 8 hướng, ngưỡng `max(R,G,B) ≤16/255`; giữ màu vật thể, trim, thu Lanczos và căn giữa. Tinh anh nằm trong ô 760×760; boss trong ô 800×800. Ảnh lớn ghép trên nền đen tuyệt đối RGB(0,0,0), RGB opaque 1024×1024.
- Lề vật thể trên ảnh lớn (trái / trên / phải / dưới, px): E1 **212/132/213/132**; E2 **132/138/132/138**; B1 **112/201/112/201**; B2 **112/130/112/130**. Tất cả vượt 10%; đã kiểm tra dải ngoài 102 px toàn bộ là RGB(0,0,0).
- Thu nhỏ theo bộ `hud-coin-*`: trim alpha, Lanczos trong ô 26×26 trên canvas 32×32 hoặc ô 40×40 trên canvas 48×48. Đã kiểm tra kích thước, alpha có đủ 0 và 255, mép ngoài trong suốt; lề alpha >8/255 ít nhất 3 px ở bản 32 và 4 px ở bản 48.
- Không xóa hoặc ghi đè ảnh có sẵn. Tấm ghép thử đầu bị lệch bố cục do trạng thái gravity của ImageMagick; giữ nguyên thành `foe-icons-sheet-401-layout1.jpg`, chỉ để bảo toàn file. **Không dùng bản layout1 để chọn art.** Tấm ghép tên chuẩn đã sửa tọa độ và mở kiểm tra.

## Bỏ qua và owner cần xem

- Không dùng bốn lượt sinh còn lại: đã đủ hai phương án cho mỗi cấp theo phiếu; chưa có lựa chọn yêu cầu sửa từ owner.
- Không sửa mã, public assets, docs Tu Tiên, scripts hoặc tests; không chạy build/test game, không đổi nhánh, commit, push, reset, clean hoặc stash. Không tạo video theo ràng buộc phiếu.
- Chưa có hai giám khảo mù, điểm ≥8,5 hoặc kiểm tra tại vị trí trên đầu quái trong built play host. Phiếu này chỉ giao art cho owner/Claude chọn; chưa tuyên bố nghiệm thu thị giác hay khả năng đọc trong combat thực.
- Owner mở `foe-icons-sheet-401.jpg` ở **100%**, chọn **E1 hoặc E2**, **B1 hoặc B2**, xem rõ nhất hàng 24/32 px. Claude nối hai mẫu được chọn vào chỗ cắm UI 394 rồi kiểm tra tại góc máy và cỡ thực trong game.

**Trạng thái bàn giao:** đủ ảnh lớn, bản 32/48 alpha, prompt và tấm ghép; chờ chọn mẫu, tích hợp và nghiệm thu runtime.
