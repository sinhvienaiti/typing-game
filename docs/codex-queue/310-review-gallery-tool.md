# Phiếu 310 · Công cụ: trang xem lại ảnh và video Firefly thành công cụ dùng lại được

**Vì sao:** tối 05/11 Claude dựng tay một trang cho anh duyệt 161 việc video, 260 bản và 137 ảnh, kèm trạng thái lab (`tools/review-gallery/build.py` và `serve.mjs`, vừa chép từ scratchpad, đang có đường dẫn cứng tới đợt 05/11). Phiếu này làm nó dùng được cho mọi đợt và có test.

**Model `gpt-6.1-sol`, mức `xhigh`.** Báo cáo: `docs/codex-queue/310-report.md` (tiếng Việt, ngắn).

## Lời giải đã chốt
0. **Trước khi sửa:** chạy `build.py` hiện tại một lần, ghi ra tệp tạm (sửa tạm hằng `OUT` trong bản sao, không ghi đè trang của anh). Giữ HTML đó làm mẫu so sánh.
1. **`build.py` thành CLI:** `python3 tools/review-gallery/build.py --sprint <thư mục đợt> --lab <thư mục art-src/lab> --jobs '<glob, tính từ gốc repo>' --root <htdocs> --out <index.html> [--notes notes.json]`. **Mọi lần chạy kiểm và test đều truyền `--out` ra tệp tạm**, không ghi đè trang của anh.
   - Mặc định: `--sprint` là `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05`, `--lab` là thư mục cha của nó, `--jobs` là `docs/work/tasks/*.json`, và `--out` như hiện tại.
   - Gốc repo suy từ vị trí file (`Path(__file__).resolve().parents[2]`). Thư mục htdocs (gốc của máy chủ) là cha của gốc repo.
   - Bảng `NOTE`, tập `STONE`, thư mục bị loại và các chữ trên trang chuyển ra file JSON tuỳ chọn `--notes`: `{ "title", "h1", "lead", "notes": {id: lý do}, "stone": [ids], "rejectedDirs": {"video-rejected-dark-purple": "<lý do>"} }`. Không dùng glob cho thư mục bị loại; chỉ các thư mục có tên trong `rejectedDirs`.
   - Thêm file mẫu `tools/review-gallery/notes-2026-11-05.json` chứa đúng các giá trị và chữ đang có trong mã (cả h1 "tối 05/11" và đoạn lead có link lab 4310).
   - `--root` (htdocs) là gốc để tính URL; mặc định là cha của gốc repo. Test truyền thư mục tạm.
   - Giữ nguyên cách chia nhóm, nhãn tiếng Việt, cách đọc trạng thái lab (manifest nào nhắc `/video/<id>/take` thì việc đó đã vào lab) và cách phát video (chỉ phát khi rê chuột, mỗi lúc một video).
   - Tách logic (gom việc, xếp nhóm, trạng thái) thành hàm thuần để test được. Phần ghi HTML gọi các hàm đó.
2. **`serve.mjs`:** đọc gốc từ `--root` (mặc định là htdocs suy từ vị trí file) và cổng `--port` (mặc định 4330); vẫn nhận cổng ở vị trí đầu như cách `launch.json` đang gọi (`serve.mjs 4330`). Giữ chặn đường dẫn ra ngoài gốc, hỗ trợ Range và chỉ nghe 127.0.0.1.
3. **README ngắn:** cách dựng, cách chạy máy chủ, và mục `.claude/launch.json` "review-gallery" đang trỏ tới bản ở scratchpad. Ghi rõ người dùng cần đổi đường dẫn sang `tools/review-gallery/serve.mjs`; Codex không sửa `launch.json`.

## Được ghi
`tools/review-gallery/build.py`, `serve.mjs`, `notes-2026-11-05.json` (mới), `test_build.py` (mới), `README.md` (mới), và báo cáo. **Cấm:** mọi lệnh git ghi; sửa file khác (kể cả `.claude/launch.json` và trang trong `typing-game-review`); mạng ngoài máy.

## Test (`test_build.py`, unittest, chỉ thư viện chuẩn)
- Thư mục tạm giả một đợt có 3 việc video:
  - một việc có trong manifest (trạng thái "Trong lab");
  - một việc nằm trong `stone` (đã gỡ);
  - một việc chưa xử lý.
- Thêm một thư mục bị loại có tên trong `rejectedDirs` của file notes tạm, và một thư mục `video-rejected-khac` không có tên ở đó (phải bị bỏ qua). Kiểm số việc theo nhóm và trạng thái.
- Việc có `image` hoặc `still` trỏ tới ảnh có thật thì ra ảnh gốc; ảnh không có thật thì không ra.
- HTML sinh ra có đủ các mục nav và không còn đường dẫn tuyệt đối `/Volumes`.

## Xong khi
- Test qua.
- Bản mới chạy với `--notes tools/review-gallery/notes-2026-11-05.json --out <tệp tạm>` trên cùng dữ liệu cho cùng số việc, số bản, số ảnh và trạng thái từng thẻ như HTML mẫu ở bước 0 (so bằng mã: lấy `data-state` và id từng thẻ của hai file). Dán hai dòng tổng vào báo cáo.
