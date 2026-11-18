# Phiếu 102 · Cổng DevTools không trùng khi nhiều làn chạy song song

Đã hoàn tất sáu mục kiểm của phần kit tại repo cha `/Users/toandx/htdocs/typing-game`. Không chạy Chrome, dev server, `kit:sync`, build hay bộ test của game; không sửa bản chép trong game, golden hoặc Tu Tiên.

## File của phiếu

- `shared/game-kit/tools/cdp-port.mjs`: thêm `portArg` và `readActivePort`; mặc định cổng 0, xác thực cổng cố định, đọc file trong profile riêng, thử lại khi `ENOENT`, lỗi hết giờ có đường file. Bộ đọc file, đồng hồ, hàm chờ truyền vào được.
- `shared/game-kit/tools/cdp-run.mjs`: thay cổng ngẫu nhiên bằng helper; đọc cổng trước lần gọi HTTP DevTools đầu tiên khi không có cổng cố định. Giữ các cờ Chrome khác và phần còn lại của runner.
- `shared/game-kit/tools/cdp-port.test.ts`: 27 test cho các trường hợp yêu cầu, biên cổng, CRLF, giá trị rỗng/sai định dạng và lỗi đọc khác `ENOENT`. File chưa được Git theo dõi đã có lúc bắt đầu phiên này; giữ nguyên nội dung và chạy lại bước đỏ trước khi thêm mã.
- `shared/game-kit/DRIFT.md`: thêm một dòng về khác biệt với Space và việc Claude cần đồng bộ.
- `docs/codex-queue/102-report.md`: báo cáo này.
- `docs/codex-queue/102/`: log, [số đo](102/metrics.json), [kết quả đột biến](102/mutations.json) và [changelog](102/2026-10-29-cdp-port.md). Hai log `01`, `02` có sẵn được giữ nguyên; log `03` trở đi là kiểm lại trong phiên này.

## Kết quả kiểm

| Mục | Lệnh / phép kiểm | Kết quả và bằng chứng |
|---|---|---|
| 1 | `pnpm --dir shared/game-kit test` | Trước: **673/673**, **45/45 file** trong [log nền có sẵn](102/01-baseline-test.log). Kiểm lại nền với `--exclude tools/cdp-port.test.ts`: **673/673**, mã thoát 0 ([03](102/03-baseline-recheck.log)). Test mới đỏ trước mã do chưa có helper, mã thoát 1 ([04](102/04-test-first-recheck.log)). Sau sửa: **700/700**, **46/46 file**, mã thoát 0 ([05](102/05-tests-green.log)); sau khôi phục đột biến: **700/700**, mã thoát 0 ([11](102/11-tests-restored.log)). Tăng **27 test**. |
| 2 | `pnpm --dir shared/game-kit typecheck` | Mã thoát **0**, **0 lỗi** trước và sau đột biến ([06](102/06-typecheck.log), [12](102/12-typecheck-final.log)). |
| 3 | `node --check shared/game-kit/tools/cdp-run.mjs` | Mã thoát **0**, **0 lỗi cú pháp** ([07](102/07-syntax.log), log rỗng). |
| 4 | `grep -n "Math.random\|9300" shared/game-kit/tools/cdp-run.mjs` | **0 dòng**, mã thoát **1** đúng nghĩa không có kết quả ([08](102/08-random-search.log), log rỗng). |
| 5a | Bỏ đọc lại khi thiếu file: thay `continue` bằng `throw error` | Test đỏ: **2 lỗi, 25 đạt/27**, mã thoát **1** ([09](102/09-mutation-no-retry.log)). Bắt được mất thử lại và mất lỗi hết giờ có đường file. |
| 5b | Bỏ kiểm khoảng `CDP_PORT`: bỏ điều kiện `< 1024` và `> 65535` | Test đỏ: **4 lỗi, 23 đạt/27**, mã thoát **1** ([10](102/10-mutation-no-env-range.log)). Các giá trị `80`, `0`, `1023`, `65536` bị test bắt. |
| 6 | `git status --short -- shared/game-kit` | Đúng **4 file** trong danh sách cho phép: runner, helper, test, DRIFT ([14](102/14-kit-status.log)). |

Hai đột biến chạy lần lượt, luôn khôi phục trong `finally`. SHA-256 helper sau khôi phục: `ac2389605a7d6d4b552a7aa14622b8240afb126c835c85c06df0b00fec783c2b`; kiểm lại **700 test xanh**. Kiểm thêm `git diff --check -- shared/game-kit`: mã thoát **0** ([13](102/13-diff-check.log)).

Test chờ file dùng đồng hồ giả: có file ở lần đọc thứ ba thì đọc **3 lần**, chờ **2 lần × 50 ms**. Trường hợp hết giờ 100 ms với nhịp 40 ms: đọc **4 lần**, chờ **40 + 40 + 20 ms**, không chờ thật. Dòng sai làm lỗi sau **1 lần đọc**, **0 lần chờ**.

## Điều chỉnh so với mô tả phiếu

- Mã hiện tại dùng `/json/list`, không có `/json/version`. Giữ `/json/list` theo yêu cầu giữ nguyên hành vi khác; cổng được đọc trước lần nối này.
- Không ghi `docs/changelog/2026-10-29-*.md` vì đường dẫn đó không có trong danh sách «Chỉ được ghi». Changelog nằm trong `docs/codex-queue/102/2026-10-29-cdp-port.md`, là đường dẫn được phép.
- Test mới và hai log đầu đã có trong workspace. Không ghi đè chúng; kiểm lại nền bằng cách loại riêng test đang đỏ, rồi xác nhận test mới đỏ trước khi thêm helper.

## Claude / chủ repo cần xem

Đọc diff và chạy lại sáu mục kiểm. Khi đồng bộ cần mang theo `cdp-port.mjs` cạnh runner; sửa bản riêng của Rồng và Space theo phiếu. Sau đó chạy **3 làn song song × 20 lượt**, yêu cầu **0 lượt trùng cổng**. Phiên này chưa xác nhận con số thực nghiệm đó vì phiếu cấm chạy Chrome và `kit:sync`. `CDP_PORT` là lựa chọn cố định có chủ ý; phép đo nhiều làn dùng chế độ mặc định cổng 0.
