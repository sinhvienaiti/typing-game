# B9 · Điều tra glError 1282 của A/B hybrid

**Chưa đạt B9:** chưa xác định lệnh GL gây lỗi trên Mac, chưa có bản sửa được chứng minh bằng test đỏ → xanh. Không sửa theo phỏng đoán hoặc xóa lỗi để đổi số đo.

Đã làm sau B8, trong `games/.wt-ic-lab-all`, nhánh `codex/lab-all`:
- Thêm `tests/lab/hybrid-prewarm.test.ts`: **5 test Node**, renderer giả dùng bộ upload **thật** `WebGLTextures` của Three 0.170, GL giả kiểm thứ tự cấp phát. Cả `meteor` và `azure-cloud-dragon` đều chạy qua `HybridAB.load/update`: màu và vector ASTC đều có `texStorage2D` trước bốn `compressedTexSubImage2D`, lần update sau không upload lại. Test đối chứng cố tình gọi subimage trước cấp phát sinh 1282; đây là kiểm bộ giả, **không phải tái hiện lỗi trong mã cũ**.
- Hai ca tiêm lỗi trước `update` chứng minh: cùng thứ tự upload đúng vẫn báo `state().glError = 1282`, vì `warm()` chỉ đọc `getError()` cuối bước. Điều này chứng minh khả năng ghi nhận lỗi từ trước, **chưa chứng minh lỗi thực tế thuộc trường hợp đó**.
- Đọc `hybrid-ab.ts`, `FlipbookPool.attach`, loader/thay thế/dispose và đường comet. A/B không gọi `compileAsync`; `attach` chỉ đổi dữ liệu CPU. Loader đợi tải/transcode xong trước khi công bố atlas; Three tự cấp phát trước subimage. Chưa có bằng chứng để sửa `hybrid-ab.ts` hoặc `flipbook.ts`, nên giữ nguyên hai file, hình và các số đo.

Kiểm tra bản cuối: `npx --no-install tsc --noEmit` sạch; `npx --no-install vitest run --maxWorkers=4` qua **125 file / 1.514 test**. Có cảnh báo fixture Node sẵn có về URL tương đối của sigil và DOM giả không có WebGL; không có test trượt.

**Claude cần kiểm trong trình duyệt:** mở riêng `?ab=meteor` và `?ab=azure-cloud-dragon` với prewarm mặc định, lấy tên lệnh GL đầu tiên sinh 1282, tham số và stack. Phân biệt lỗi đã tồn tại trước `HybridAB.warm()` với lỗi sau từng `initTexture` màu/vector; nếu lỗi từ prewarm toàn cảnh, lấy đúng lệnh/stack đó. Có thể đối chiếu `prewarm=0` khi điều tra. Sau khi có bản sửa, kiểm lại hai URL mặc định không gắn bộ trace: console không còn 1282, `__lab.ab().glError === 0`, chạy qua hai chu kỳ và khởi động lại, giữ nguyên hình/số đo. Test hiện tại chỉ kiểm thứ tự cấp phát, không mô phỏng đủ driver, shader hoặc toàn bộ prewarm của lab.

Không mở trình duyệt/cổng mạng, không build, không sửa ngoài test và báo cáo, không chạy lệnh Git ghi. Không phải hết hạn mức; bước còn thiếu là trace GL thực tế, đã hỏi bổ sung trong phiên.
