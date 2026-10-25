# Phiếu 008 · Tu Tiên Thủ Ải · làm lại ảnh bản sắc theo nhận xét của chủ dự án (ưu tiên)

**Nhận xét của chủ dự án (25/10)** về hai ảnh bản sắc lượt 1:
1. **Ảnh nhân vật** (nữ kiếm tu) chưa đạt: cần **đẹp hơn, quý phái hơn, nhìn hoàng tộc hơn**.
2. **Ảnh giữ ải** chưa đạt: **phóng to quá**, làm tầm nhìn bé lại, khó nhìn toàn diện bản đồ và quái.

Đã thành luật trong canon: **D47** (nữ kiếm tu chính quý phái, hoàng tộc) và **D48** (camera luôn thấy toàn sân và cả triều thú). Đọc hai dòng này trong `docs/games/tu-tien/00-canon.md` §3, và §8.1 về sân 40 × 26 m, hai cổng, đường trời, Trận Tâm.

**Thư mục làm việc:** gốc repo `D:\typing-game`. Được ghi vào:
- `docs/games/tu-tien/art-requests/m0b/` (sửa prompt);
- `games/immortality-cultivation/art-src/` (ảnh);
- `games/immortality-cultivation/art-src/README-m0b.md` (cập nhật).

Không chạy git.

## Việc

1. **Sửa bộ prompt** `00-identity.md` và prompt của `kiem-tu` (ảnh chính và ảnh sau) theo D47:
   - nữ kiếm tu trẻ, đẹp thanh tú, dáng đứng thẳng, cốt cách cao quý;
   - trang phục lụa nhiều lớp màu trắng ngọc và lam sẫm, viền thêu vàng nhạt, họa tiết mây và hạc vương giả; miện nhỏ hoặc trâm ngọc; ngọc bội;
   - kiếm Thanh Phong của bậc vương giả;
   - không gợi cảm, không hở hang, hợp mọi lứa tuổi;
   - giữ chất "sơn thủy huyền ảo chất Việt" của canon;
   - ảnh nguồn 3D giữ đúng luật Tripo: tư thế A, nền `#E6E6E6`, không hiệu ứng.
2. **Sửa prompt ảnh cảnh ải** theo D48. Ảnh vẽ **đúng góc camera của game**:
   - nhìn từ trên xuống, nghiêng khoảng 50–55°, ống kính hẹp gần trực giao, không phối cảnh mạnh;
   - khung chứa **trọn sân 40 × 26 m có lề**: Trận Tâm ở giữa, 2 cổng thú, đường trời, 2 Trận Trụ, các ô cơ quan;
   - nữ kiếm tu nhỏ ở cạnh Trận Tâm;
   - thú triều tràn vào từ hai cổng, thú nhỏ nhưng **đọc được** hình dáng từng họ;
   - Thú Vương ở cổng xa;
   - núi non sương mù chỉ là viền ngoài sân, không chiếm khung.
3. **Tạo lại bằng `image_gen`**, mỗi ảnh tối đa 2 lượt, giữ bản tốt nhất:
   - **2 bản** chân dung, với 2 cách phục sức khác nhau để chủ dự án chọn;
   - **2 bản** cảnh ải, nghiêng 50° và 55°;
   - `cultivators/kiem-tu.png` và `kiem-tu-back.png` theo thiết kế mới (đính kèm bản chân dung tốt hơn làm tham chiếu thiết kế).
   - Ảnh cũ đổi tên `<tên>.v1.png`, không xóa.
4. **Cập nhật** `README-m0b.md`: so sánh cũ và mới, nhận xét từng ảnh, việc chủ dự án cần chọn.

**Xong khi:** đủ 6 ảnh mới (2 chân dung, 2 cảnh ải, 2 ảnh nguồn kiem-tu), prompt đã sửa, README đã cập nhật.
