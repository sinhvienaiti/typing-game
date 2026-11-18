# Phiếu 305 · Công cụ: một lệnh in toàn bộ trạng thái làm việc (luật tiết kiệm token, anh duyệt 06/11)

**Vì sao:** anh duyệt luật "một lệnh, không phải mười" (`.agents/skills/agent-orchestration/SKILL.md`, mục "the coordinator's token budget", luật 3). Phiên điều phối hiện phải gọi 6–10 lệnh nhỏ mỗi lần kiểm (ls, curl, tail), mỗi lệnh tốn khoảng 63 nghìn token. Phiếu này làm một script in tất cả trong một lần gọi.

**Model `gpt-6.1-sol`, mức `xhigh`.** Báo cáo: `docs/codex-queue/305-report.md` (tiếng Việt, ngắn).

## Được ghi
Chỉ `tools/agent-status/status.py`, `tools/agent-status/test_status.py`, `tools/agent-status/README.md` (mới) và báo cáo. **Cấm:** mọi lệnh git ghi; sửa file khác; gửi dữ liệu ra ngoài máy; mở cổng.

## Cách làm (đã chốt)
`python3 tools/agent-status/status.py [--json]`, chỉ dùng thư viện chuẩn Python 3.9. Không bao giờ ném lỗi: thiếu gì thì in `down` hoặc `missing`, mã thoát luôn 0. Mỗi yêu cầu HTTP có timeout 2 s, chỉ tới `127.0.0.1`.

Mặc định in tối đa khoảng 15 dòng chữ thường; `--json` in cùng dữ liệu dạng JSON:

1. **Giờ:** giờ máy (HH:MM).
2. **Video Firefly:**
   - `GET http://127.0.0.1:8841/done`: JSON `{id: [số take, …]}`, đếm số việc và số take.
   - Đọc `docs/work/tasks/firefly-sprint-video.json` (`jobs[].id`) để đếm việc còn lại: `id` chưa có thư mục chứa `*.mp4` trong `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/video/`.
   - Tên và giờ sửa của thư mục mới nhất trong thư mục đó.
   - Dạng: `video: up · 123 việc xong · còn 140 · mới nhất water-ribbon-loop 08:48`. Số "xong" đếm theo `/done`, có thể gồm việc không còn trong `jobs[]`; không cần cộng cho khớp.
3. **Âm Firefly:**
   - `GET http://127.0.0.1:8791/ping` (trả `ok`).
   - Đếm trạng thái trong `docs/work/tasks/firefly-sprint-sound.json` (`jobs[].state`): `done` là xong; có chữ `failed` là lỗi; có chữ `round` (ví dụ `round 1 done`) là đang làm dở; không có `state` là chờ.
   - Thư mục mới nhất trong `…/sound/`, kèm giờ.
4. **Lab:**
   - `GET http://127.0.0.1:4310/skills-lab.html` (mã HTTP).
   - `GET http://127.0.0.1:4330/typing-game-review/owner-review/2026-11-05/tu-tien/firefly-gallery/index.html` (mã HTTP).
5. **Codex:** các file `.local/codex-lane-mac-*.out` sửa trong 24 giờ, mỗi file in tên và dòng cuối không rỗng (tối đa 3 file mới nhất). Thêm `queue.sh: chạy` hoặc `không chạy`, dựa vào `ps` có tiến trình chứa `tools/codex-run/queue.sh`.
6. **Máy:**
   - Swap đã dùng (`sysctl vm.swapusage`, lấy giá trị `used`).
   - Dung lượng trống của `/Volumes/SS990TPRO` (`shutil.disk_usage`).
   - Cảnh báo `RAM!` khi swap đã dùng > 12 GB; `ĐĨA!` khi trống < 10 GB.

Đường dẫn gốc là repo, suy ra từ vị trí file script (`Path(__file__).resolve().parents[2]`), không dùng đường dẫn tuyệt đối có sẵn.

## Test (`test_status.py`, unittest)
- Mỗi phần đọc trạng thái là một hàm nhận gốc repo, URL và đường dẫn qua tham số (mặc định là giá trị thật), để test truyền thư mục tạm và cổng tắt. `test_status.py` tự thêm thư mục của nó vào `sys.path` trước khi `import status`, vì tên thư mục có dấu gạch.
- Khi mọi cổng tắt (dùng một cổng không ai nghe), mọi mục ra `down` và không ném lỗi.
- Đếm việc còn lại đúng trên một thư mục tạm có 2 việc, trong đó 1 việc có `take1.mp4`.
- Đếm trạng thái âm đúng trên một file JSON tạm có `done`, `failed (3 tries)` và một việc không có `state`.
- `--json` là JSON hợp lệ, có đủ các khoá `time`, `video`, `sound`, `lab`, `codex`, `machine`.

## Xong khi
- `python3 -m unittest tools/agent-status/test_status.py` qua.
- Chạy thật `python3 tools/agent-status/status.py` in ≤ 15 dòng, không lỗi. Dán kết quả vào báo cáo.
- README ngắn: cách chạy và ý nghĩa từng dòng.
