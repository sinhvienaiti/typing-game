# Test trước khi sửa · quyết định 13:28

- Test ngưỡng V và hai diện miễn: chạy đỏ trước khi sửa `auditEdgeKeys` (thiếu bộ đếm và chưa miễn vùng tối ở mọi alpha); sau sửa chạy xanh.
- Test ảnh WebP cũ: 9 qua, 1 lỗi vì High còn 12 điểm ở q95. Sau đó bổ sung kiểm hợp đồng của quyết định 13:28: không được có điểm chưa khai báo; mọi điểm còn lại phải được ghi đủ tọa độ/RGBA trong manifest, q95 và đúng quyết định. Bộ kiểm vẫn bắt mọi điểm không có trong hồ sơ.
- Nhật ký gốc: `tmp/199/test-before-residual-decision.log`.
