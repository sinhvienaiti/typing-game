# Phiếu 188 · Kiểm giấy phép ba game và kit

Ngày: 29/10/2026. Người làm: Codex. Chờ Claude duyệt rồi commit; không chạy lệnh Git ghi.

## 1. Kết quả

Đã kiểm dependencies và dependencies gián tiếp theo bốn lockfile, đối chiếu phiên bản cài thực tế, đọc `package.json` và LICENSE trên máy. Đã thêm **21 dòng** vào [THIRD_PARTY.md](../games/THIRD_PARTY.md), chia theo Dragonhold, Wordwoven, Last Line và kit; **giữ nguyên toàn bộ nội dung cũ**.

**Có 5 gói OFL-1.1 ngoài danh sách cho phép**, tương ứng 7 lượt dùng phông giữa ba game. Không phát hiện GPL, AGPL, LGPL, giấy phép tùy chỉnh hay thiếu LICENSE trong các gói npm thuộc phạm vi chạy đã kiểm. Đây chưa phải kết luận site đã đủ điều kiện phát hành: phông cần quyết định của chủ dự án và thông báo giấy phép chưa được tích hợp vào game.

## 2. Số gói và giấy phép

Đếm theo `(tên, phiên bản)` trong từng thành phần; không đếm lặp CSS weight/subset hay addon three. Cột dependencies gồm cả gián tiếp, không gồm devDependencies thuần build/test.

| Thành phần | Dependencies trực tiếp | Gián tiếp | Tổng dependencies | MIT | OFL-1.1 |
|---|---:|---:|---:|---:|---:|
| Dragonhold | 4 | 0 | 4 | 1 | 3 |
| Wordwoven | 3 | 0 | 3 | 1 | 2 |
| Last Line | 3 | 0 | 3 | 1 | 2 |
| shared/game-kit | 1 | 1 | 2 | 2 | 0 |
| Tổng lượt theo thành phần | 11 | 1 | 12 | 5 | 7 |

Kit còn nhập **three 0.170.0, MIT**, tuy khai báo ở devDependencies; tính thêm vào nhóm chạy của kit thành **3 gói npm MIT**. Gộp và khử trùng cả ba game với kit: **8 gói npm duy nhất = 3 MIT + 5 OFL-1.1**.

Nhóm riêng mã nhúng và helper từ công cụ build:

| Thành phần | Thêm vào bản chạy/khả năng của kit | Giấy phép |
|---|---|---|
| Dragonhold | meshoptimizer 0.18 (đóng trong three), Vite 7.3.7 (polyfill và helper preload) | 2 MIT |
| Wordwoven | Vite 7.3.7 | 1 MIT |
| Last Line | meshoptimizer 0.18, Vite 7.3.7 | 2 MIT |
| Kit | meshoptimizer 0.18; KTX-Parse và zstddec/Zstandard trong nhánh KTX2 tùy chọn | 2 MIT; 1 MIT AND BSD-3-Clause |

Nếu tính cả thành phần nhúng/helper và nhánh kit tùy chọn, có **12 thành phần duy nhất = 6 MIT + 5 OFL-1.1 + 1 MIT AND BSD-3-Clause**. Đây là đếm theo biểu thức giấy phép; biểu thức cuối yêu cầu giữ cả hai giấy phép.

Đồ thị từ entry hiện tại cho kết quả thực dùng bảo thủ (kể cả nhúng/helper): **Dragonhold 6 = 3 MIT + 3 OFL; Wordwoven 3 = 1 MIT + 2 OFL; Last Line 5 = 3 MIT + 2 OFL**. `three` của Wordwoven vẫn được kiểm và ghi sổ vì nằm trong dependencies, nhưng **không được nhập từ entry hiện tại**. Không gán meshoptimizer cho Wordwoven. `a11y-dialog`/`focusable-selectors` mới có ở kit, chưa có trong dependencies/lockfile và bản kit đang dùng của ba game.

## 3. Cờ và điểm cần chủ dự án xem

| Gói | Phiên bản khóa = cài | Giấy phép | Game dùng |
|---|---|---|---|
| @fontsource/be-vietnam-pro | 5.3.0 | OFL-1.1, ngoài danh sách | Cả ba |
| @fontsource/cormorant-garamond | 5.3.0 | OFL-1.1, ngoài danh sách | Dragonhold |
| @fontsource/noto-sans | 5.3.0 | OFL-1.1, ngoài danh sách | Dragonhold |
| @fontsource/baloo-2 | 5.3.0 | OFL-1.1, ngoài danh sách | Wordwoven |
| @fontsource/chakra-petch | 5.3.0 | OFL-1.1, ngoài danh sách | Last Line |

Chủ dự án cần quyết định cho phép OFL-1.1 riêng cho phông hay giao thay phông. OFL cho phép nhúng/phân phối theo điều kiện, nhưng không nằm trong danh sách của phiếu; không tự duyệt ngoại lệ.

Hai file nhúng KTX-Parse và zstddec không có nhãn semver hay LICENSE độc lập trong gói three. Đã đọc LICENSE repo gốc, ghi đúng MIT và MIT + BSD-3-Clause; xác định bản thực tế bằng **three 0.170.0 + SHA-256 từng file**, chưa đoán semver riêng. Cần xác minh nguồn phiên bản trước khi bật nhánh này. Ba game chưa dùng KTX2; Basis Universal transcoder chưa được phục vụ trong `public` của chúng. Trước khi bật phải bổ sung đúng Apache-2.0/NOTICE của bản transcoder JS/WASM được chọn. [Nguồn và giới hạn kiểm](188/sources.md) ghi rõ các URL, lần đọc mạng không thành công và phạm vi kết luận.

Các dòng cũ nói three.js/a11y-dialog “không bắt buộc” ghi công đã được **đính chính bằng phần bổ sung**: MIT yêu cầu giữ bản quyền và văn bản cho phép khi phân phối. MIT không bắt đặt tên trang là Credits. Không thay hay xóa dòng cũ.

`dist` có sẵn ở ba game có helper Vite; Dragonhold/Last Line có chunk meshopt. Không tìm thấy file LICENSE/NOTICE/Credits riêng trong ba cây `dist`, các chunk JS không chứa nguyên văn thông báo MIT. Cần tích hợp các khối Credits và kiểm gói phát hành trong một phiếu cho phép sửa mã; không kết luận về bản deploy ở máy chủ từ các `dist` cũ này.

## 4. Đã làm và bàn giao

- [Sổ THIRD_PARTY](../games/THIRD_PARTY.md): thêm 21 dòng, nhóm theo game/kit, đủ tên, phiên bản, nguồn máy, giấy phép, phạm vi dùng và nghĩa vụ thông báo.
- [Credits Dragonhold](188/credits-dragon-hold.md), [Credits Wordwoven](188/credits-typing-defense.md), [Credits Last Line](188/credits-typing-survival.md): nguyên văn LICENSE/bản quyền của gói đang dùng; Wordwoven có khối three dự phòng tách riêng.
- [Credits kit](188/credits-game-kit.md): a11y-dialog 8.1.5, focusable-selectors 0.8.4, three, meshoptimizer và các khối KTX2 có điều kiện.
- [inventory.json](188/inventory.json), [inventory-summary.json](188/inventory-summary.json): phiên bản lock/cài, closure dependencies, LICENSE nguyên văn, SHA-256 và đồ thị import có dòng nguồn. [embedded-evidence.json](188/embedded-evidence.json): định danh file nhúng, helper Vite và bằng chứng `dist` cũ. [counts.json](188/counts.json): số tổng hợp.
- [licenses/](188/licenses/): bản sao thông báo trên máy, Vite core và bản chép LICENSE repo gốc cho các file nhúng. [sources.md](188/sources.md): liên kết nguồn và cách diễn giải.
- [inventory.mjs](188/inventory.mjs), [write-docs.py](188/write-docs.py), [verify.py](188/verify.py): mã kiểm kê/kết xuất/kiểm tài liệu; chỉ ghi đường dẫn phiếu cho phép. Kết xuất sổ có chốt dừng nếu phần 188 đã tồn tại, không tự ghi đè lần hai.

Không tải/cài/gỡ gói, không sửa package.json, lockfile, mã game hay UI; không chạy build/test game. Không làm ảnh/âm thanh vì phiếu chỉ kiểm giấy phép thư viện. Không đọc hay sửa cây Tu Tiên. Không kiểm các devDependencies thuần build/test như thư viện chạy: @types/node 24.19.2, @types/three 0.170.0, tsx 4.23.15, TypeScript 6.0.3, Vitest 3.2.7, happy-dom 21.0.4 (kit). TypeScript chạy `--noEmit`; Vite được giữ riêng vì có mã nhúng; Rollup 4.64.12/esbuild 0.28.2 trong lock là công cụ tạo/chuyển bundle, không phải package runtime được nhập. Không kiểm tài sản khác, phiên bản trên máy chủ hay repo Space Typing vì ngoài bốn thành phần của phiếu.

## 5. Kiểm phạm vi và tính toàn vẹn

[verification.json](188/verification.json) ghi kiểm đối chiếu phiên bản, closure dependencies, SHA-256 LICENSE, Credits giữ nguyên văn, đủ 21 dòng tám cột, và toàn bộ nội dung sổ cũ là tiền tố không đổi. Bốn package.json và bốn lockfile còn đúng SHA-256 lúc kiểm kê.

Đã chạy `git status --short -uall` và lưu [lúc bắt đầu](188/status-start.txt), [lúc kết thúc](188/status-final.txt). Workspace vốn có nhiều thay đổi và file chưa theo dõi của các làn khác; không thể tuyên bố toàn bộ status chỉ có file phiếu 188. [scope.json](188/scope.json) phân biệt phần có sẵn, thay đổi xuất hiện thêm và danh sách file phiếu này ghi; **mọi đường dẫn phiếu này ghi đều nằm trong vùng được phép**. Giữ nguyên `188/status-before.txt` đã có trước lượt làm. Không xử lý hay dọn thay đổi của người khác.
