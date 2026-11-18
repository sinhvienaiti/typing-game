# Brief bộ bốn góc: nhân vật chính, hướng C mượn cổ Nhật Bình của A · 12/11/2026

Theo canon D63 (hai tầng, hợp đồng trang phục) và nghiên cứu `HEROINE_RESEARCH_2026-11-11.md`. Bộ này là **ảnh nguồn dựng model 3D**, không phải tranh đẹp để ngắm: mọi chọn lựa ưu tiên rig, Tripo và cỡ 66 px từ camera sau lưng.

## Số đo trước khi vẽ
- Camera 55°, FOV 28°, nhìn từ phía nam về bắc: thấy lưng, vai, đỉnh đầu. Cỡ trên màn 66 px ở 1080p (44 px ở 720p); khi zoom cận khoảng 200–300 px.
- Màu cấm ở cường độ cao: đỏ `#FF4A4A`, cam `#FFB020`, vàng kim `#FFC83A`, xanh ngọc `#7FF5E0`. Sân đá vôi xám xanh.
- Ngân sách model: nhân vật chính 20.000 mặt trở lên (`MODEL_QUALITY.md`), texture 2048 ở High.

## Thiết kế (một người, trùng chân dung A ở tóc, diadem, màu)
- **Mặt và tóc:** mặt sạch kiểu donghua cao cấp (da mịn, nét rõ, không lỗ chân lông, không tả thực ảnh), bình thản, hơi nghiêm; tóc đen búi cao thành **một khối đặc, cao hơn chân dung A khoảng 30 %**, diadem ngọc trắng và vàng cũ dày bản nhưng không thành mão, hai tua ngắn (xương phụ).
- **Thân trên:** áo lụa trắng ngà cổ cao kín, dài tới giữa đùi, **tấm cổ Nhật Bình chữ nhật vắt qua hai vai: lõi chàm, rìa ngoài trắng ngà viền vàng cũ bản rộng (≥ 4 % chiều cao người)**, vai vuông, rìa sáng để không chìm vào nền đá xám (Gemini 12/11), ống tay bó từ khuỷu xuống cổ tay, bắp tay có nếp nhẹ. Hoa văn: một phượng lớn thêu vàng cũ ở **giữa lưng** (ấn tròn, đường kính bằng 25 % chiều cao người), mây và hạc (như chân dung A) thành dải viền dày ở gấu áo; vạt hò chéo và đường tà của ngũ thân rõ; không hoa văn nhỏ rải đều.
- **Thắt lưng:** gấm chàm rộng, khoá vàng cũ, **tấm hộ eo** thêu phượng nhỏ, ngọc bội trắng đục treo bên trái, hai đuôi lưng ngắn tới gối (xương phụ).
- **Thân dưới:** quần ống rộng chàm thẫm gom thành hai ống lớn, bó ở cổ chân; giày cao cổ chàm viền vàng cũ.
- **Vũ khí:** kiếm Thanh Phong trong vỏ sơn mài chàm, đeo ngang **thấp ở xương cùng, ngay dưới ấn phượng**, chuôi bên phải nghiêng 10°; lưỡi thép xanh nhạt chỉ thấy ở góc có rút kiếm.
- **Không có:** dải lụa dài, áo choàng, váy, hào quang, ánh sáng phép, vật bay (tất cả là VFX hoặc bộ A sau).
- **Màu:** trắng ngà 60, chàm 30, vàng cũ 10; ngọc trắng đục; thép xanh nhạt.

## Bộ ảnh (cùng một chat, cùng khổ 3:4, cùng chiều cao người, nền `#00FF00`, lề ≥ 8 %, đèn mềm một nguồn trên phải 45°, không bóng đổ)
1. **Tờ turnaround** 4 cột: trước, trái, sau, phải, A-pose (tay hở thân 30°), chân phẳng, cùng chiều cao từng cột.
2. **Trước** riêng, A-pose.
3. **Sau** riêng: thấy gáy, búi tóc, cổ Nhật Bình, ấn phượng, kiếm sau lưng, đuôi thắt lưng; không thấy mặt.
4. **Trái** riêng (vai trái về phía người xem).
5. **Ba phần tư từ trên 30°**, dáng sẵn sàng, một tay nắm chuôi: chỉ để kiểm cách đọc ở camera chơi, không đưa Tripo.
Mỗi ảnh ghi lại danh sách 10 chi tiết nhận dạng trong prompt: diadem, búi tóc, cổ Nhật Bình, ấn phượng lưng, thắt lưng và tấm hộ eo, ngọc bội trái, đuôi lưng, ống tay bó, quần ống rộng, giày, kiếm sau lưng.

## Kiểm trước khi chấm
- Bảng nhất quán 10 chi tiết × 4 góc; mốc chiều cao (đỉnh diadem, vai, thắt lưng, gấu áo, gối) chênh ≤ 3 % giữa các góc; sau thật là sau.
- Ô kiểm 66 px từ góc sau và góc ba phần tư: 3 khối (tóc đen, vai chàm, thân trắng), ấn phượng còn đọc ra.
- Hình bóng đen: vai vuông, kiếm ngang, chân mở; không sừng, không mặt che.

## Chấm và sau đó
Hai giám khảo mù ≥ 8,5 (bản sắc, nhất quán, dựng được, sức hút, đúng cỡ chơi) → Tripo multiview, `--dry-run`, một model → rig của ta, 8 clip → lab, chấm ≥ 9 cho chuyển động. Bộ A (lễ) làm ngay sau theo cùng thân chuẩn.
