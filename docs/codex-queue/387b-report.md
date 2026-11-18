# Báo cáo phiếu 387b · 16/11/2026

**Đã làm nền và chuyển ảnh; chưa nghiệm thu. Chờ sửa phạm vi phiếu do xung đột gate URL.** Không ghi Git, không chạy build.

## Điều kiện đầu vào

- Đã đọc xác nhận của Claude ở cuối `387a-report.md`: **387a nghiệm thu kỹ thuật ĐẠT; 387b được chạy tiếp**.
- Đọc §13.3–13.4, script `lane-width.mjs`, xem greybox `lane-w12.png` và tranh 384b.
- Phiếu ghi nhầm `map1-lane.v1-try3.png`: tệp không tồn tại. Tranh 384b thực tế là `art-src/concept/map1-lane.v2-try3.png`; chỉ xem tham chiếu, không nối vào runtime.
- Quota lúc vào việc: dùng 11%, còn 89%. Một làn, không giao agent khác.

## Đã làm

Các đường dẫn sau tương đối với `games/immortality-cultivation/`:

- `public/assets/ground/thanh-thach/{lane-paving,court-paving,court-cracked,formation-worn,moss-patch,rubble-edge}.v2.webp`: sáu ảnh chuyển từ PNG 383b, chất lượng 90, giữ 1024 × 1024. Tổng 1.713.502 byte; không tạo ảnh AI mới, không sửa ảnh nguồn.
- `media.md5`: thêm đúng sáu dòng checksum của WebP; giữ các mục có sẵn. Đã đối chiếu lại 6/6 MD5.
- `src/view/ground.ts`: một ShaderMaterial trộn sáu ô, lặp 4 m; lưới phủ x ±40, z −60…+16; khoảng cách lấy từ `stage.field.lane.pointsMm` qua hàm `corridors` hiện có, tính một lần trên lưới 0,5 m. Trong đường dùng ô lane; vai đường rộng 1 m trộn vụn/rêu; sân trộn ô nguyên/nứt bằng value noise, seed mặc định băm từ stage id; đĩa r 9 m dùng ô trận văn. Ngoài x ±22 chuyển dần sang sắc vực tối lấy từ `GROUND_COLOURS.surround`. Giữ viền mực, bỏ grid và decal thủ tục khỏi cảnh. Giải phóng sáu texture khi material bị dispose.
- `tests/view/ground.test.ts`: kiểm đúng sáu URL bằng loader giả, không đọc WebP; cấu hình texture và giải phóng; khoảng cách lấy từ điểm stage và đổi theo stage khác; phủ bốn góc camera ở cả ba kẹp x và hai kẹp z, 1920 × 1080 và 1280 × 720.
- `tests/view/stage.test.ts`: thay khẳng định nền thủ tục năm phần bằng nền ảnh và viền mực. Giữ các thay đổi 387a có sẵn.

## Kiểm tra

- `npm run typecheck`: package không có script này. Thay bằng `node node_modules/typescript/bin/tsc --noEmit -p tsconfig.json`: **xanh**. Không sửa package.
- `npm test -- --maxWorkers=4` dưới khóa CPU: **999/1000 test xanh, 91/92 file xanh**. Đã chạy lệnh nghiệm thu nêu cụ thể trong phiếu; không chạy build.
- Toàn bộ test nền mới và test stage đều xanh. Test vàng/replay hiện có xanh; không sửa sim, content, local, golden, camera, Ngũ Lôi hoặc tài liệu game.
- Một lỗi duy nhất: `tests/boundary.test.ts:273` chỉ cho URL bắt đầu `/assets/immortality-cultivation/`; cả sáu URL `/assets/ground/thanh-thach/` đúng theo thư mục phiếu đều bị chặn. Không sửa gate và không né kiểm bằng nối chuỗi/URL tương đối.
- Luma trung bình **trên WebP nguồn**: lane 105,085; court 91,2636; tỉ lệ **1,1514**. Đây chưa phải số trên ảnh chụp game. Shader có gain riêng cho lane/court; cần đo lại trong host trước khi xác nhận ≥1,15.
- `git diff --check` cho các tệp liên quan: xanh.

## Chưa làm và điều phối cần xử lý

1. **Sửa phạm vi phiếu để gỡ gate**: khuyến nghị cho phép đặt sáu ảnh và URL tại `public/assets/immortality-cultivation/ground/thanh-thach/`, cập nhật loader/test/MD5 tương ứng. Phương án còn lại là cho phép một ngoại lệ tường minh cho đúng sáu URL hiện tại trong boundary test. Đã hỏi chủ dự án, chưa tự chọn ngoài phạm vi.
2. Chưa có capture 387b, ABOUT.md, tấm ghép trước/sau/cạnh 384b, số luma từ ảnh chơi hoặc p95 High 1080p đỉnh đợt 3 trước/sau. Thư mục đích `typing-game-review/captures/tu-tien/map1-lane-build/387b/` nằm ngoài vùng được sandbox cho ghi; không chuyển capture sang thư mục khác trái quy định. House rules cũng cấm chạy build; chưa tạo bản build mới để đo. Không dùng ảnh 387a hoặc host cũ làm chứng cứ cho mã 387b.
3. Không có khung thô của tôi cần prune, không có máy chủ hoặc tab kiểm nào do tôi khởi tạo. Chưa dựng lại review index vì chưa tạo capture.
4. Chủ dự án/Claude cần xem nền trong host, đo lại luma/p95 và chấm chất lượng sau khi gỡ gate. Báo cáo này **không xác nhận đạt 8,5** và chưa đóng phiếu.

## Nghiệm thu kỹ thuật của Claude (16/11)

- Gỡ gate boundary (việc chuyển file thuần): sáu WebP chuyển sang `public/assets/immortality-cultivation/ground/thanh-thach/`; URL trong `src/view/ground.ts`, `tests/view/ground.test.ts` và đường dẫn trong `media.md5` sửa theo. `vitest` 1000/1000 xanh, `tsc --noEmit` sạch. Tranh 384b đúng tên là `map1-lane.v2-try3.png`.
- Ảnh chơi (dev server, `?prelearn=0&review=0`): `typing-game-review/captures/tu-tien/map1-lane-build/387b/`, ghép `387b-sheet.jpg` (387a | 387b | tranh 384b). Luma trên ảnh chơi 1080p: đường 97,1 / sân 61,3 = **1,58** (≥ 1,15).
- Nhận xét nhìn (chưa chấm 8,5): đường chữ S đọc rõ; nhưng toàn cảnh lạnh xanh xám, lặp ô 4 m thấy rõ, vai đường rêu/vụn và đĩa trận văn chưa nổi, chưa ấm và sang như tranh 384b. Cần một vòng chỉnh màu/biến thể (việc nghệ thuật sau), không chặn 387a/387c.
- **387b nghiệm thu kỹ thuật: ĐẠT.** p95 cảnh chơi có nền ảnh chưa đo riêng (bench 387c đo đám đông trên nền bench).
