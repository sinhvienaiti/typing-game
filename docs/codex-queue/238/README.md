# Hồ sơ phiếu 238

Bộ giao và số đo nằm ở [`art-src/_review/238/`](../../../games/typing-survival/art-src/_review/238/). Báo cáo chính: [`238-report.md`](../238-report.md).

- `generated-files.json`: bốn lần sinh thành công, nguồn công cụ, ảnh lưu và prompt nguyên văn. Shard chỉ sinh một lần rồi dùng cùng nguồn cho icon và chân dung.
- `verify.mjs`: kiểm đọc MD5, bản sao cũ, đúng khổ/kênh, prompt chọn, matte, IoU và hai bộ Shard giống nhau. Chạy từ repo cha bằng `node docs/codex-queue/238/verify.mjs`; không thêm `--save` trên hồ sơ đã chốt.
- Script hậu kỳ: `games/typing-survival/art-src/_review/238/process.mjs <tên> <lượt>`. Script chỉ nhận ba tên của phiếu; giữ nguyên `.try*`, tạo bản hậu kỳ mới và tờ cỡ nhỏ. Không chạy lại trên cùng tên/lượt đã có.
- `deliver.mjs` là script đã dùng để chép bản chọn và ghép tờ xem; giữ làm hồ sơ, không cần chạy lại. Nó có kiểm bản cũ trước khi ghi.

Chọn `objective.try2`, `station-crest.try3`, `shard.try2`. Các prompt gốc/chọn cạnh ảnh là nguồn truy vết của phiếu 238. Sidecar prompt cỡ thu cũ của phiếu 150 không nằm trong danh sách được sửa nên giữ nguyên; không dùng chúng để xác định lượt chọn mới.

Chưa có điểm chấm lại của Claude. Không tích hợp `public/` trong phiếu này.
