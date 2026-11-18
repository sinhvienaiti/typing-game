# Phiếu 066 · MF-I2 · Maple Tree dự phòng, hai sắc

**Ngày:** 28/10/2026. **Trạng thái:** Chờ kết quả CL-05; chưa tạo ảnh, chưa đạt điều kiện hoàn tất phiếu.

## Điều kiện thực hiện

Phiếu 066 và `docs/tools/map-factory/TICKETS.md` §MF-I2 ghi: “Chỉ dùng nếu cây tán tròn có sẵn nhuộm sắc ấm dưới 8 điểm (CL-05).” `MAP_PLAN.md` §V7 yêu cầu thử nhuộm cây tán tròn có sẵn trước; hàng CL-05 yêu cầu chấm thử rồi mới gọi MF-I2 khi dưới 8.

Đã đọc kế hoạch, phiếu gốc, phiếu 066, luật duyệt ảnh và bộ prompt `03-pine-river-props.md`. Đã tìm kết quả CL-05 trong `docs/tools/map-factory`, `docs/codex-queue`, `docs/changelog`, `games/dragon-hold/docs` và `games/dragon-hold/art-src/_review`; chưa tìm thấy báo cáo hoặc điểm chấm cây nhuộm. Tìm các tên CL-05, Maple và cây ấm trong `games/dragon-hold/src` cũng chưa có kết quả. Đây là kết quả tìm kiếm trong các đường dẫn trên, không phải kết luận rằng cây nhuộm đã trượt.

Vì chưa có bằng chứng kích hoạt, giữ phiếu dự phòng: không gọi công cụ tạo ảnh, không tiêu lượt thử. Đã hỏi chủ dự án trong phiên làm việc về kết quả CL-05 hoặc chỉ định tạo dự phòng ngay; chưa nhận được trả lời tại thời điểm ghi báo cáo.

## File tạo ra

- `docs/codex-queue/066-report.md`: báo cáo này.
- `games/dragon-hold/art-src/_review/MF-I2/md5-before.txt`: MD5 trước của toàn bộ 154 file trong thư mục `props/pine-river`, lấy bằng `md5 -r`.
- `games/dragon-hold/art-src/_review/MF-I2/md5-after.txt`: MD5 sau của cùng thư mục, 154 file.
- `games/dragon-hold/art-src/_review/MF-I2/md5-diff.txt`: kết quả `diff -u`, rỗng, mã thoát 0.

## Kiểm bắt buộc

| Kiểm | Kết quả |
| --- | --- |
| KA1 · bảo toàn file cũ | 154/154 file giữ nguyên MD5; 0 file thêm, 0 file mất trong thư mục đích; diff rỗng |
| KA2 · khổ và nền | Chưa áp dụng: không có ảnh mới |
| KA3 · lề ≥ 24 px | Chưa áp dụng: không có ảnh mới |
| Mặt nạ tán · trung vị H/S/V | Chưa đo: không có ảnh mới |
| ΔE2000 so với #FF4A4A, #FFB020, #FFC83A, #C8D24A | Chưa đo cả bốn số: không có ảnh mới |
| KA4 ngoài tán | Chưa đo: không có ảnh mới |
| KA5 · năm tiêu chí, cỡ đầy đủ và 128 px | Chưa chấm; 0 lượt thử cho cả rust và copper |

Không có lượt chọn, bản chính, prompt hoặc tờ duyệt; không ghi điểm giả khi chưa có ảnh. Không chạy Git, build, test, dev server hay trình duyệt; không sửa mã, tài liệu khác hoặc file media có sẵn.

## Việc cần xem

Claude/chủ dự án cung cấp kết quả chấm cây nhuộm CL-05. Nếu dưới 8, kích hoạt tạo `maple-tree-rust` và `maple-tree-copper`, mỗi ảnh tối đa ba lượt, rồi kiểm đủ KA1–KA5 và ba kiểm riêng. Nếu cây nhuộm từ 8 điểm, bỏ qua MF-I2 theo kế hoạch. Chủ dự án cũng có thể chỉ định tạo dự phòng ngay để thay điều kiện này.
