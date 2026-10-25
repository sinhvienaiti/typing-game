# Phiếu 014 · Tu Tiên Thủ Ải · thử 3 hướng gương mặt (6 ảnh)

**Bối cảnh:**
- Chủ dự án duyệt 10 chân dung của phiếu 009. Sau đó (25/10 chiều) chủ dự án thấy **gương mặt quá giống ảnh AI tràn lan trên mạng**, khiến game giống các game khác.
- Mọi nhân vật đang chung một khuôn "mặt idol AI": da sứ mịn, mắt to, cằm V, môi bóng, mặt đối xứng, gần như cùng một người.
- **Nguyên nhân một phần nằm ở prompt cũ:** "strikingly beautiful", "delicate harmonious facial features", "luminous natural skin", "match the attached portrait's face rendering". Mọi ảnh còn đính kèm cùng chân dung A, nên khuôn mặt bị chép sang tất cả.
- Phiếu 013 và 013b (ảnh nguồn 3D) **tạm dừng** tới khi chủ dự án chọn hướng mặt mới.

**Mục tiêu:** tạo bản so sánh để chủ dự án chọn. Cùng 2 nhân vật (Kiếm nữ, Kiếm nam), **giữ nguyên phục sức, bảng màu, pháp khí** của chân dung đã duyệt, **chỉ đổi gương mặt và cách vẽ** theo 3 hướng.

**Thư mục làm việc:** gốc repo `D:\typing-game`. Chỉ được ghi vào:
- `games/immortality-cultivation/art-src/face-test/` (ảnh và prompt);
- `games/immortality-cultivation/art-src/_review/014-face-test.jpg`;
- `games/immortality-cultivation/art-src/README-014.md`.

Không chạy git; không sửa ảnh và tài liệu có sẵn.

## Nguồn

- **Phục sức để giữ:** `art-src/roster/kiem-nu.png`, `roster/kiem-nam.png` và prompt cạnh ảnh.
  - Đính kèm chỉ để giữ áo, miện, kiếm, bảng màu. Viết rõ trong prompt: **không giữ khuôn mặt** của ảnh đính kèm.
- **Canon:** `docs/games/tu-tien/00-canon.md` D47 (quý phái, hoàng tộc, kín đáo, mọi lứa tuổi) và §21.1 (vẻ thủy mặc, game 3D nhìn từ trên).

## Ba hướng (mỗi hướng: Kiếm nữ + Kiếm nam, 1024 × 1536, nửa người như chân dung cũ)

| Mã | Hướng | Mô tả để viết prompt |
|---|---|---|
| H1 | **Tranh lụa Việt** | Vẽ trên lụa theo truyền thống tranh lụa Việt Nam:<br>• màu khoáng dịu, nét vẽ mảnh;<br>• mảng màu phẳng, đổ bóng rất nhẹ, thấy vân lụa;<br>• gương mặt vẽ bằng nét: mắt dài một mí hoặc hai mí nhẹ, mày thanh, mặt trái xoan đầy đặn.<br>Không chép tác phẩm hay họa sĩ cụ thể nào |
| H2 | **Tượng sơn mài và khắc gỗ cách điệu** | Nhân vật như một bức tượng 3D cách điệu cao:<br>• khối mặt đơn giản có mặt phẳng rõ, chất sơn mài và gỗ, ngọc;<br>• vẽ tay; mắt khắc hình hạt hạnh, không có da kiểu ảnh chụp.<br>Gần nhất với model 3D trong game, đọc rõ ở cỡ nhỏ |
| H3 | **Người thật, không mặt idol** | Bán tả thực nhưng là một người cụ thể:<br>• nét Việt rõ: sống mũi thấp vừa, gò má, mày tự nhiên;<br>• tuổi thật (nữ khoảng 28, nam khoảng 35); da có kết cấu thật, hơi bất đối xứng, trang điểm rất nhẹ;<br>• như chọn diễn viên đóng vai, không phải người mẫu.<br>Vẫn quý phái nhờ dáng và trang phục |

**Viết prompt:**
- Khẳng định điều cần có. Thêm một câu tránh khuôn mặt AI phổ biến: da sứ bóng, mắt to quá cỡ, cằm V nhọn, môi bóng, mặt đối xứng hoàn hảo, nét mặt idol.
- Nữ và nam phải là hai người khác hẳn nhau.
- Giữ luật D47: kín đáo, không gợi cảm, không chữ, không logo.

## Việc

1. Viết 6 prompt; lưu `face-test/<h1|h2|h3>-<nu|nam>.png` và `.prompt.txt` cạnh ảnh.
   - Ảnh hỏng rõ thì tạo lại tối đa 1 lần.
   - Mở xem từng ảnh. Kiểm riêng: khuôn mặt có còn giống mặt idol AI không. Nếu còn, sửa prompt và tạo lại, trong giới hạn 1 lần.
2. **Ảnh so sánh** `_review/014-face-test.jpg`: lưới 3 cột (H1, H2, H3) × 2 hàng (nữ, nam), có nhãn tiếng Việt. Thêm cột đầu là chân dung cũ để so.
   - Dùng ImageMagick trong WSL: `~/.local/bin/magick montage`, font `/mnt/c/Windows/Fonts/arial.ttf` để có dấu.
3. **Thêm một ô thu nhỏ:** cả 6 khuôn mặt ở cỡ 64 px cao, vì trong game nhân vật chỉ cao khoảng 64 px. Đặt ngay trong ảnh so sánh, hoặc thành tệp `_review/014-face-test-small.jpg`.
4. **Viết `README-014.md`:** mỗi hướng một đoạn ngắn, gồm điểm mạnh, điểm yếu, độ hợp với model 3D, và mức tránh được "mặt AI". Kết thúc bằng một đề xuất.

**Xong khi:** 6 ảnh, ảnh so sánh và README đã có.
