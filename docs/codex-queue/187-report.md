# Phiếu 187 · Dragonhold · Cổng game cấu hình lúc build

Hoàn tất phần mã và các kiểm tra của phiếu. `pnpm check` xanh **509/509 test**,
golden **10/10**, kit **75/75**. `pnpm deploy:pack` production đạt **0 lỗi,
0 tham chiếu `typing-game.local`**. Demo có đặt URL cũng đạt. Chờ Claude duyệt
rồi commit; phiên này không chạy lệnh Git ghi.

## 1. Mốc đầu và đúng hai tham chiếu

Worktree `games/.wt-dh-codex`, nhánh `dh-codex`, HEAD
`6aa593a2dce6637cccbe24a58709b86f7127f607`; `git status --short -uall`
ban đầu trống. [Mốc đầu và SHA-256](187/before.json).
Đã đọc báo cáo 169 cùng JSON kiểm gói, inventory, trạng thái và bằng chứng
xác minh trong `169/`; tái hiện trên HEAD hiện tại trước khi sửa mã.

| Nguồn trước sửa | Dòng, chuỗi và đường sử dụng |
| --- | --- |
| `src/kit/learning/contract.ts` | Dòng 22: `export const PARENT_ORIGIN = "https://typing-game.local";`. `src/app/app.ts:221` và `src/app/learning.ts:246` tạo cầu nối mà không truyền `parentOrigin`; kit dùng mặc định này để gửi/nhận tin. |
| `src/app/portal.ts` | Dòng 4: `return (origin ?? "https://typing-game.local") + "/";`. `src/ui/results.ts:256` gọi bằng `VITE_PORTAL_ORIGINS` chưa đặt, nên nút về nguồn nhà. |

Bundle nền `assets/index-D6L5QOut.js` có đúng **2** lần, tại offset 105152 và
290327. Bộ kiểm tính **1 lỗi** vì cả hai nằm trong cùng file.
[Nguồn, dòng và ngữ cảnh bundle](187/local-host-before.json),
[JSON bộ kiểm trước sửa](187/pack-before.json).

## 2. Mã, test và hướng dẫn đã làm

- `src/app/portal.ts`: `portalHome` nhận một URL HTTP(S) tuyệt đối, mặc định
  `null`, giữ đường dẫn/query/fragment và từ chối URL sai hoặc chứa thông tin
  đăng nhập. `createPortalBridge` dùng phần nguồn của `VITE_PORTAL_URL` cho
  `postMessage`. Không đặt URL thì dùng host không có parent, giữ hàng đợi
  học cục bộ ngay cả khi bị nhúng, không gửi tin hay xả nhầm hàng đợi.
- `src/app/app.ts`, `src/app/learning.ts`: cả hai nơi tạo cầu nối đều đi qua
  hàm này; vẫn nhận cầu nối được truyền sẵn trong test.
- `src/ui/results.ts`: khi biến trống, không tạo nút “Back to portal”.
  Trái/phải vẫn giữ Retry/Replay hợp lệ; bỏ gợi ý đổi nút khi chỉ có một nút.
  Có URL thì hiện nút, giữ `target="_top"`, điều hướng bằng chuột hoặc Enter.
  Không đổi giữ màn thắng 2,6 giây, chọn từ, nghe từ hoặc phím thử mức dễ hơn.
- `vite.config.ts`: đọc biến môi trường Vite và thay đúng khai báo
  `PARENT_ORIGIN` trong bộ nhớ biên dịch. File kit trên đĩa không đổi. Chỉ
  truyền tùy chọn ở nơi gọi chưa loại được fallback khỏi bundle của lớp kit;
  plugin xử lý nguồn còn lại đó. Nếu không còn đúng một khai báo, build dừng
  để kiểm lại, không bỏ qua hay nới bộ kiểm gói.
- `tests/app/portal.test.ts`, `tests/ui/results-screen.test.ts` và test mới
  `tests/portal-build.test.ts`: URL trống/hợp lệ/sai, màn thắng/thua, bàn phím
  với một/hai nút, hàng đợi, nguồn nhận/gửi tin; test build thực thi JavaScript
  do cấu hình Vite thật tạo ra trong Node và kiểm fallback đã đổi. Fixture ở
  `tmp/` tự xóa, không cần server hoặc trình duyệt.
- `README.md`: ghi cách build độc lập, cổng production, demo nhà và chuyển
  từ `VITE_PORTAL_ORIGINS` sang `VITE_PORTAL_URL`.
- `docs/changelog/2026-10-29-portal-link.md`: ghi thay đổi và số đo.

Demo nhà dùng lệnh có sẵn, không cần thêm script hay thay `package.json`:

```sh
VITE_PORTAL_URL=https://typing-game.local/ pnpm deploy:pack:local
```

Không đặt biến thì `pnpm deploy:pack` tự đủ theo phạm vi kiểm gói. Nếu môi
trường đang có giá trị, dùng `VITE_PORTAL_URL= pnpm deploy:pack` để tắt rõ.
`--allow-local-host` chỉ cho phép nguồn local, không tự đặt URL.

## 3. Kiểm tra và số đo

| Lượt | Kết quả | Bằng chứng |
| --- | --- | --- |
| `pnpm deploy:pack` trước sửa | Mã **1**, 5,246 giây; 1 lỗi, 2 tham chiếu local | [Lệnh](187/deploy-pack-before.json), [log](187/deploy-pack-before.log), [JSON gói](187/pack-before.json) |
| Test trước sửa mã | **23 đỏ/9 xanh**, 3 file; đúng các hành vi cần đổi | [Kết quả JSON](187/tests-before-results.json), [log](187/tests-before.log) |
| Test liên quan sau sửa | **32/32 xanh**, 3 file, 1,133 giây cả lệnh | [Kết quả JSON](187/tests-after-results.json), [lệnh](187/tests-after.json), [log](187/tests-after.log) |
| `pnpm check` | Mã **0**, **12,825 giây**; **57 file, 509/509 test**, TypeScript và Vite xanh | [Lệnh](187/check.json), [log](187/check.log) |
| Golden M0 | **10/10 xanh** trong lượt check; hai file golden giữ nguyên hash | [Log check](187/check.log), [xác minh](187/verification.json) |
| Test thời gian tag | **21/21 xanh** trong lượt check, không có lỗi thời gian; không cần chạy riêng ba lần | [Log check](187/check.log) |
| `pnpm deploy:pack` sau sửa | Mã **0**, 4,505 giây; **0 lỗi, 0 local** | [Lệnh](187/deploy-pack-after.json), [log](187/deploy-pack-after.log), [JSON gói](187/pack-after.json) |
| `VITE_PORTAL_URL=https://typing-game.local/ pnpm deploy:pack:local` | Mã **0**, 4,174 giây; **0 lỗi**, 3 tham chiếu local được cấu hình rõ | [Lệnh và biến](187/deploy-pack-local.json), [log](187/deploy-pack-local.log), [JSON gói](187/pack-local.json) |
| Kiểm chính gói demo bằng chế độ production | Mã **1**, một lỗi `local-host`; bộ kiểm vẫn chặn nguồn nhà | [JSON](187/pack-local-production.json), [lệnh](187/check-pack-local-production.json) |
| Dựng lại production để bàn giao | `pnpm deploy:pack` mã **0**, 5,534 giây; inventory khớp gói production đã kiểm | [Lệnh](187/deploy-pack-final.json), [log](187/deploy-pack-final.log), [JSON cuối](187/pack-final.json) |
| Phạm vi và Git | `git diff --check` mã **0**; chỉ 10 file của việc này | [Trạng thái cuối](187/status-final.txt), [xác minh](187/verification.json) |

Lệnh package xuất dạng chữ như phiếu 169. Sau mỗi lần đóng gói, chạy bộ kiểm
kit với `--json` trên chính `dist` đó, lưu JSON thuần vào `pack-*.json`;
`deploy-pack-*.json` lưu lệnh, biến cổng, thời gian và mã thoát. Không trộn log
build vào JSON kiểm gói. [Trình ghi bằng chứng](187/run.py).

Production trước/sau đều **240 file**: **33.653.981 → 33.654.248 byte**
(tăng 267 byte). Demo: **33.654.591 byte**. Quét riêng toàn bộ HTML/JS/CSS/JSON
production thấy **0** chuỗi `typing-game.local`; [inventory và SHA-256](187/production-bundle.json).
Ba nguồn thông tin ngoài vẫn như nền: `catlikecoding.com`,
`developer.download.nvidia.com`, `kit.invalid`; không nằm trong `problems`.
Vite vẫn cảnh báo chunk game trên 600 kB, không chặn build/kiểm gói.

Giữ nguyên SHA-256 **76 file kit** kể cả manifest, **20 file sim**, **4 file
typing**, **8 file content**, **2 file golden**. `verify-kit` kiểm 75 file trong
manifest; vì vậy số 75 và 76 nói về hai tập khác nhau.
[Xác minh cuối](187/verification.json). `dist` bàn giao là production không đặt cổng.

## 4. Bỏ qua và cần chủ dự án xem

- Không chạy server, trình duyệt, mạng, build/test game khác, `kit:sync`
  hoặc lệnh Git ghi theo giới hạn phiếu. Không sửa kit, media, luật chơi,
  golden hay Tu Tiên. Không tạo ảnh/âm thanh vì không thuộc việc này.
- Kiểm nút dùng DOM stub và mã build chạy trong Node. Chưa nhận định cảm
  quan, kiểm HTTP hoặc chứng nhận toàn bộ G7; những lượt đó cần phạm vi riêng.
- Không đổi giao thức bắt tay `hello`/`ack` của kit: đó là bước B riêng trong
  tài liệu triển khai độc lập. Với cổng đã cấu hình, hành vi xả hàng đợi của
  kit hiện có vẫn được giữ.
- Chủ dự án cần Claude duyệt plugin thay mặc định khi biên dịch và lựa chọn
  ẩn nút khi không đặt URL, rồi commit. Chưa commit hoặc push.

Báo cáo/bằng chứng chỉ nằm ở `docs/codex-queue/187-report.md` và `187/` của
repo cha. Các thay đổi game chỉ nằm trong worktree được giao.
