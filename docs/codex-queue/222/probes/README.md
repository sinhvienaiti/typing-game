# Test dò của phiếu 222

Ba ca hồi quy riêng, chạy sau toàn bộ kiểm ngoại tuyến trên bản chép, mã 1: 3/3 đỏ đúng F2/F3/F4. Không đưa vào tổng 593 test gốc; không sửa sản phẩm để làm xanh.

Muốn tái hiện, chép `integration.test.ts` vào `tests/_probe-222/` của một bản chép Dragonhold cùng mốc. Chạy binary Vitest cục bộ: `node_modules/.bin/vitest run tests/_probe-222`. Lượt 222 dùng binary trực tiếp vì pnpm tự yêu cầu cài phụ thuộc. `run.log` giữ đầu ra.

Probe CSS chứng minh selector và thuộc tính áp lên lớp heading dùng chung; không phải ảnh render hoặc nghiệm thu layout. Probe Retry dùng state/DOM thật với DOM stub; probe fixture chứng minh đường bắt buộc nằm ngoài repo.
