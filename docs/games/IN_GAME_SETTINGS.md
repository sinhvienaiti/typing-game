# Cài đặt ngay trong trận: nút bánh răng và nút loa

Chủ dự án, 29/10/2026: "trong mỗi game đều phải có icon setting để hiển thị setting chung và icon loa để setting cho phần các loại âm thanh mà user có thể setting, tránh việc phải ra ngoài màn cài đặt mới có thể setting được."

Áp cho Dragonhold, Wordwoven, Last Line và mọi game sau này. Dựng một lần trong kit (`shared/game-kit/ui/quick-settings/`), mỗi game chỉ gắn và đổi da.

## 1. Hai nút luôn có trong trận

| Nút | Icon | Mở ra |
|---|---|---|
| **Settings** | bánh răng (ảnh thật theo phong cách game) | bảng cài đặt chung |
| **Sound** | cái loa; đổi sang loa gạch chéo khi tắt tiếng hết | bảng âm thanh |

- Có ở mọi màn chơi và cả màn tựa, cùng một góc trong cả ba game (mặc định góc trên phải), không che thẻ chữ, không đè HUD khác. Cỡ nút ít nhất 32 px ở 720p, có viền sáng khi trỏ chuột.
- **Mở bằng chuột**; phím gõ chữ không được vô tình mở bảng. Thêm phím tắt không trùng chữ cái: `F1` cho Settings, `F2` cho Sound. `Esc` đóng bảng.
- **Khi bảng mở, trận tạm dừng và ô gõ chữ ngừng nhận phím**; đóng bảng thì đếm ngược ngắn (3, 2, 1) rồi chơi tiếp. Thay đổi có hiệu lực ngay, không cần nút Lưu; lưu vào save của game.
- Bảng là lớp phủ trên trận (thấy trận mờ phía sau), không chuyển sang màn khác.

## 2. Bảng âm thanh (nút loa)

| Mục | Kiểu | Ghi chú |
|---|---|---|
| Master | thanh trượt 0–100 và nút tắt tiếng | |
| Music | thanh trượt | |
| Effects | thanh trượt | tiếng trận, kỹ năng, quái |
| Keyboard sound | chọn: Off, Creamy Linear, Deep Thock, Marbly, Clean Clack, Soft Dome (id `creamy`, `thock`, `marbly`, `clack`, `dome`; đổi 29/10 sau khi chủ dự án trả bộ cũ) | nghe thử ngay khi chọn (một chuỗi gõ ngắn) |
| Keyboard volume | thanh trượt | |
| Voice | thanh trượt | đọc từ, phát âm, lời thoại |
| Interface | thanh trượt | tiếng nút, bảng |

Khi kéo thanh trượt thì phát một mẫu âm của nhóm đó để nghe được mức mới.

## 3. Bảng cài đặt chung (nút bánh răng)

Phần chung của kit:
- **Typing effects:** kiểu chữ (Stamp mặc định, Flare, Smash, Shatter, Rune, Minimal), cường độ (Off, Low, Normal, High, Ultra), cỡ dải chữ (Medium, Large, Huge); có ô xem thử nhỏ.
- **Graphics:** mức chất lượng (Low, Medium, High, Ultra), giảm chuyển động.
- **Learning:** hiện nghĩa tiếng Việt, hiện phiên âm (nếu game có).
- Nút **Resume** và **Quit to title**.

Mỗi game thêm mục riêng của mình (ví dụ camera, độ khó, gợi ý).

## 4. Hình và chữ

- Chữ tiếng Anh (luật 28/10); tên kiểu và hồ sơ là tiếng Anh.
- Mọi icon, khung bảng, thanh trượt, nút là ảnh thật theo phong cách game (luật 28/10, không vẽ bằng mã). Icon: phiếu Codex 180; khung: phiếu 115/160 (Wordwoven), 162 (Dragonhold), 127 (Last Line).

## 5. Kiểm

- Mở và đóng hai bảng bằng chuột, `F1`, `F2`, `Esc` ở 1280 và 1920, trong trận và ở màn tựa.
- Khi bảng mở: trận dừng, phím chữ không vào ô gõ; đóng thì đếm ngược rồi chơi tiếp, không mất từ đang gõ.
- Đổi từng mục có hiệu lực ngay và còn sau khi tải lại trang.
- Không che thẻ chữ hay HUD; tương phản chữ trong bảng WCAG ≥ 7.
