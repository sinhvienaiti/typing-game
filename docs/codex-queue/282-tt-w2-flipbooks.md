# Phiếu 282 · Tu Tiên · Công cụ: đổi 54 take video W2 thành flipbook bằng `tools/vfx-flipbook`

**Loại việc:** công cụ và xử lý media (`gpt-6.1-sol`, mức `xhigh`). Phiếu ngắn theo luật làm gọn 05/11, không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/282-report.md`.

## Bối cảnh
- Sáng 05/11, Firefly Video (model Adobe) tạo 18 việc "chất liệu thuần" kiểu câu lệnh W2 (anh chọn "Chạy W2"), mỗi việc 3 take, nền đen.
- Take nằm ở `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/video/<id>-w2/take<N>.mp4`, kèm `take<N>.prompt.txt`.
- Danh sách việc, gồm khung hình và mục đích dùng: `docs/work/tasks/firefly-sprint-video.json`, trường `jobs`.
- Mục tiêu: có flipbook sẵn để Claude so trong lab và anh chọn take. Chưa gắn vào game.

## Công cụ
`tools/vfx-flipbook/`. Đọc `run.sh`, `launch.py`, `vfxflip/` và hai cấu hình mẫu `typing-survival.json`, `dragon-hold.json`.

## Việc
1. **Viết `tools/vfx-flipbook/immortality-cultivation.json`** theo đúng định dạng hai tệp mẫu: `game`, `doc`, `defaults`, `clips`.
   - Một mục cho mỗi id `-w2`, với `aspect` khớp video và `loop: true` cho id có `loop`, `flow`, `drift` hoặc `rising` trong tên.
   - Cỡ ô và số khung theo loại:
     - burst hay impact: 32 khung, 256×256;
     - loop: 48 khung, có `crossfade`;
     - strip ngang (`strip-*`, `light-column-*`): cỡ ô theo khung hình và `axis` đúng.
   - `doc`: `docs/work/tasks/firefly-sprint.md`.
2. **Dùng một `VFXLAB_HOME` trong repo:** `.local/vfxlab`. Sandbox không ghi được `~/VFXLab`.
3. **Đưa take vào inbox của công cụ:** `.local/vfxlab/inbox/firefly/immortality-cultivation/<id>/<id>__v<N>.mp4`, với take N thành vN. Dùng hard link (`ln`), hoặc chép nếu không link được; không sửa file gốc.
4. **Chạy** `tools/vfx-flipbook/run.sh all immortality-cultivation`. Python lấy từ venv Audio Lab như `run.sh` mặc định, hoặc đặt `VFXFLIP_PY` nếu venv nằm chỗ khác.
5. **Tấm xem cho anh:** một ảnh ghép mỗi việc từ `sheet.jpg` của 3 take, nhãn id và take; và một MP4 ghép `preview.mp4` của 3 take cạnh nhau, dưới 30 MB. Lưu ở `.local/vfxlab/review/`.

### Được ghi
`tools/vfx-flipbook/immortality-cultivation.json`, `.local/vfxlab/**`, script mới trong `.local/vfxlab/tools/`, và `docs/codex-queue/282-report.md`.

### Cấm
Sửa `tools/vfx-flipbook/vfxflip/**`, `run.sh`, `launch.py` và các tệp game; lệnh git ghi; mở cổng mạng; tải gói; tạo ảnh, âm hay video mới.

## Kiểm bắt buộc
1. `tools/vfx-flipbook/run.sh test -q` qua, trước và sau.
2. Mỗi take có đủ đầu ra (`atlas.png`, `json`, `sheet.jpg`, `preview.mp4`, `metrics.json`), hoặc ghi lý do vì sao không.
3. MD5 của mọi take gốc trong `art-src` không đổi (so trước và sau).
4. `git status --short` ở repo cha chỉ thêm `tools/vfx-flipbook/immortality-cultivation.json` và báo cáo; `.local/` vốn bị git bỏ qua.

## Claude làm sau
Chép tấm xem sang `typing-game-review/owner-review/`, gửi anh chọn take, rồi đưa take được chọn vào lab.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
