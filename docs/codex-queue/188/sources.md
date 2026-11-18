# Phiếu 188 · Nguồn và giới hạn kiểm

Ngày kiểm: 29/10/2026. Nguồn chính là bản cài trên máy; `inventory.json` lưu nguyên văn LICENSE, đường dẫn `package.json`, phiên bản khóa, phiên bản cài và SHA-256. Không tải gói, cài gói hay chạy build/test.

## Nguồn ngoài máy

- meshoptimizer 0.18: [LICENSE.md tại tag v0.18](https://raw.githubusercontent.com/zeux/meshoptimizer/v0.18/LICENSE.md). File nhúng của three có nhãn `Built from meshoptimizer 0.18` và thông báo tác giả riêng; không được chỉ giữ LICENSE của three.
- KTX-Parse: [LICENSE của repo gốc](https://raw.githubusercontent.com/donmccurdy/KTX-Parse/main/LICENSE), MIT, Don McCurdy. Bản nhúng `ktx-parse.module.js` không có nhãn phiên bản hay LICENSE riêng trên máy. Khóa được bản **đi kèm three 0.170.0** bằng SHA-256, chưa khẳng định semver độc lập của KTX-Parse.
- zstddec: [LICENSE của repo gốc](https://raw.githubusercontent.com/donmccurdy/zstddec-wasm/main/LICENSE): MIT cho lớp JavaScript và BSD-3-Clause cho Zstandard bên trong WASM. Bản nhúng cũng không có nhãn semver; định danh bằng three 0.170.0 và SHA-256. Không coi BSD này là GPL; dùng điều khoản BSD đã công bố trong LICENSE của tác giả.
- [package.json của three tại r170](https://raw.githubusercontent.com/mrdoob/three.js/r170/package.json) xác nhận các ví dụ nằm trong gói, không phải các dependencies npm riêng. KTX-Parse và zstddec không có nút độc lập trong lockfile dự án.

Đã thử đọc lịch sử GitHub của hai file KTX-Parse và zstddec tại r170 để tìm semver: công cụ web không lấy được trang; truy cập HTTP trực tiếp từ shell không phân giải được DNS. Vì vậy không đoán phiên bản. Hai mục này là **điểm cần xác minh nguồn bản nhúng khi bật KTX2**, không phải kết luận gói không có giấy phép. Ba game hiện không nhập KTX2Loader.

## Phạm vi và cách đếm

- Đếm khóa `(tên, phiên bản)`, có cả dependencies gián tiếp trong `snapshots`, không đếm lặp các CSS subset/weight, addon three hay nhiều bản sao vật lý của cùng gói.
- `dependencies` được kiểm hết, kể cả `three` của Wordwoven đang chưa tới được từ entry HTML. Tách số gói khai báo khỏi số thực sự tới được trong đồ thị nhập hiện tại.
- Đồ thị từ entry HTML đi theo import/export có giá trị, import động chuỗi cố định và CSS `@import`; loại import type. `inventory.json` ghi từng cạnh cùng dòng nguồn, các cạnh không giải được và đồ thị addon three. Đây là kiểm nguồn bảo thủ, không thay cho thống kê tree-shaking của một build mới.
- Kit không có build độc lập. Kiểm các mô-đun dùng khi chơi, loại tests, công cụ Node và cấu hình Vitest. `three` đặt trong devDependencies của kit nhưng là import chạy thật, nên vẫn được kiểm và đếm riêng. Các bản `src/kit` của ba game chưa có quick-settings mới; không tự gán a11y-dialog cho game khi chưa đồng bộ/cài nó.
- Vite là devDependency có **mã của chính nó** chèn vào bản chơi: modulepreload polyfill và preload helper cho import động. Ghi riêng Vite 7.3.7 MIT, giữ thông báo của Vite core; các giấy phép của dependencies được đóng trong CLI Vite không tự động trở thành giấy phép bundle game.
- TypeScript chạy `--noEmit`; target ES2022; không có `tslib` trong lockfile hay import chạy thật. Rollup/esbuild tạo bundle/chuyển mã, không có package runtime tương ứng được nhập; các dấu hiệu helper CommonJS cũng không xuất hiện trong `dist` hiện có. Không tính toàn bộ công cụ build/test vào bản chơi. Danh sách devDependencies đã loại và phiên bản nằm trong `inventory.json`.
- `dist` có sẵn chỉ là bằng chứng bổ sung: đã thấy cả hai dấu hiệu helper Vite ở ba game, chunk meshopt ở Dragonhold/Last Line; không có LICENSE/NOTICE/Credits riêng trong cây `dist` kiểm được. Không khẳng định đây là bản phát hành cuối hay đã khớp HEAD.
- Basis Universal: README trên máy tại `shared/game-kit/node_modules/three/examples/jsm/libs/basis/README.md` chỉ Apache-2.0. `enableKtx2()` yêu cầu bên gọi cung cấp URL transcoder; ba game hiện không gọi, `public` của ba game không có JS/WASM transcoder. Chưa tính thành phần chưa phục vụ này vào bundle hiện tại. Trước khi triển khai KTX2 phải khóa đúng bản JS/WASM và kèm Apache-2.0/NOTICE của bản đó, bên cạnh Credits KTX-Parse/zstddec đã chuẩn bị.
- Chú thích trong `Triangle.closestPointToPoint` nhắc thuật toán của sách *Real-Time Collision Detection*; bản three công bố MIT. Không tự gán giấy phép khác chỉ từ một trích dẫn thuật toán.

## Cờ cần xử lý

Năm gói phông OFL-1.1 nằm ngoài danh sách cho phép của phiếu và §5; có bảy lượt dùng giữa ba game. OFL có điều khoản cho phép nhúng/phân phối kèm điều kiện, nhưng điều đó **không tự mở rộng danh sách của chủ dự án**. Giữ nguyên gói; chủ dự án quyết định bổ sung OFL cho phông hay giao thay phông. Credits đã giữ nguyên toàn bộ thông báo bản quyền và OFL, không suy diễn “miễn phí” thành “không cần thông báo”.

MIT/OFL không buộc một trang phải có đúng tên “Credits”, nhưng buộc giữ thông báo khi phân phối theo điều khoản tương ứng. Phiếu này chọn trang Credits làm nơi cung cấp toàn văn. Chỉ đưa file Markdown vào thư mục báo cáo chưa làm game công khai đáp ứng nghĩa vụ; cần tích hợp và đóng gói trong một phiếu được phép sửa mã.
