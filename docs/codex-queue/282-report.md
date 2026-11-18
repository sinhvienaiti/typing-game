# Báo cáo phiếu 282 · W2 thành flipbook

Đã hoàn tất chuyển **54/54 take của 18 việc**, không lỗi và không thiếu đầu ra. Có **18 ảnh ghép + 18 MP4 so ba take**, video lớn nhất **2,20 MB**, đều dưới 30 MB. Chưa gắn vào game hoặc chọn take thay anh.

## Tệp đã ghi

- `tools/vfx-flipbook/immortality-cultivation.json`: đúng bốn trường `game`, `doc`, `defaults`, `clips`; 18 id W2. `doc` trỏ `docs/work/tasks/firefly-sprint.md`; aspect đối chiếu bằng ffprobe, không có cảnh báo lệch aspect.
- `.local/vfxlab/inbox/firefly/immortality-cultivation/<id>/<id>__v<N>.mp4`: đủ 54 video, đều là hard link tới take N gốc. Giữ prompt nguyên văn ở `.prompt.txt`; `.txt` là metadata riêng cho bộ đọc của công cụ.
- `.local/vfxlab/out/immortality-cultivation/<id>/<id>__v<N>.{atlas.png,json,sheet.jpg,preview.mp4,metrics.json}`: **270 tệp**, kèm `summary.json`.
- `.local/vfxlab/review/<id>.jpg` và `<id>.mp4`: đủ 18 cặp, nhãn id và take 1–3. [Mục lục xem](../../.local/vfxlab/review/README.md), `index.json`, `ABOUT.md`; ảnh ghép giữ toàn bộ sheet, MP4 ghép ba preview cạnh nhau, giữ tỉ lệ và cặp nền tối/sáng. Dùng Arial; ffmpeg tại máy không có `drawtext`, nên nhãn được ghép bằng ảnh chữ trong cache.
- `.local/vfxlab/tools/review_282.py`: đồng bộ inbox, ghép bản xem và kiểm đầu ra; `finish_282.py`: hoàn tất lô, chạy kiểm thử sau và giải mã MP4.
- `.local/vfxlab/audit/`: MD5 trước/sau, manifest, kết quả kiểm từng take, log chuyển đổi, kiểm thử, giải mã video và trạng thái Git.
- `docs/codex-queue/282-report.md`: báo cáo này.

## Cấu hình và số khung

- Burst `fire-spark-spray-w2` và impact `metal-light-pillar-hit-w2`: mỗi take **32 khung, 256×256**. Đoạn giới hạn mặc định dài 64 khung nguồn, lấy 32 mẫu bước 2.
- 10 việc loop: mỗi take **48 khung, crossfade 8**; gồm mọi id chứa `loop`, `flow`, `drift`, `rising`. Hai charge `twin-fire-spiral-charge-w2` và `fire-charge-gather-w2` cũng loop theo prompt gốc “seamless continuous loop”.
- Strip ngang: **512×288**, `axis: horizontal`, `layout: strip-x`. `light-column-*`: **144×256**, `axis: vertical`, `layout: bbox`, giữ cột dọc theo video 9:16.
- `fire-smoke-roll-white-w2` dùng **nền trắng, blend normal**, đúng prompt và video gốc. Các chất liệu còn lại dùng additive trên nền đen theo cấu hình mẫu.
- Tổng đầu ra: **30 take × 48 khung; 15 × 32; 6 × 31; 1 × 30; 2 × 29**. Chín take không phải burst/impact giữ cách chọn 24–32 khung tự nhiên của công cụ: smoke v1/v2/v3 = 31/31/30; sword-rain = 31/31/31; death-soul = 29/31/29. Không sửa bộ xử lý hoặc thêm khung giả để ép tròn 32.

## Kiểm bắt buộc

1. **PASS trước:** `tools/vfx-flipbook/run.sh test -q` → **23/23**, 8,95 giây.
2. **PASS chuyển đổi:** `tools/vfx-flipbook/run.sh all immortality-cultivation` → **54 flipbook, 0 lỗi**. Lúc đầu có 53 take; take gold-dust v3 đến trong lúc xử lý và đã được đưa vào lượt cuối.
3. **PASS sau:** `tools/vfx-flipbook/run.sh test -q` → **23/23**, 8,18 giây. Cả hai lượt đặt cache và thư mục tạm dưới `.local/vfxlab`, không ghi `~/VFXLab`.
4. **PASS đầu ra:** đủ 5 tệp/take; PNG/JPG mở được; kích thước atlas, ô, số khung, chỉ số trim và loop khớp metadata. **72/72 MP4** (54 preview + 18 video ghép) giải mã toàn bộ bằng ffmpeg, không lỗi. Chi tiết: `audit/verification.json`, `audit/video-decode.json`.
5. **PASS MD5:** **54/54 video W2 giữ nguyên**. Đồng thời so toàn bộ **78 video take** có trong thư mục sprint ở thời điểm ghi nhận, không video gốc nào đổi MD5. Các cặp `audit/sources-before.json` / `sources-after.json` và `audit/all-video-md5-before.json` / `all-video-md5-after.json` lưu giá trị trước/sau; `audit/verification.json` lưu kết quả đối chiếu. Không tệp công cụ có sẵn nào đổi nội dung.
6. **Phạm vi Git:** phần phiếu này chỉ thêm cấu hình và báo cáo; `git check-ignore .local/vfxlab` xác nhận toàn bộ lab bị bỏ qua. Repo vốn có nhiều thay đổi sẵn. So trạng thái trước/sau còn xuất hiện hai phiếu mới do luồng khác, nên phép kiểm “toàn repo chỉ thêm hai đường” **không đạt nguyên văn vì thay đổi đồng thời**; không sửa hoặc dọn các phiếu đó:

```text
?? docs/codex-queue/282-report.md
?? docs/codex-queue/283-tt-skill-prewarm-shared.md
?? docs/codex-queue/284-tt-jade-soft-cap.md
?? tools/vfx-flipbook/immortality-cultivation.json
```

Các lệnh dùng môi trường:

```sh
export VFXLAB_HOME=/Volumes/SS990TPRO/htdocs/typing-game/.local/vfxlab
export TMPDIR="$VFXLAB_HOME/tmp"
# Python mặc định của run.sh: /Users/toandx/AudioLab/.venv/bin/python
# Kiểm thử thêm PYTEST_ADDOPTS để đặt cache_dir và --basetemp trong VFXLAB_HOME.
tools/vfx-flipbook/run.sh all immortality-cultivation
```

## Cần xem khi chọn take

**20/54 take có cờ kỹ thuật**, 34 take không có cờ. Không có cờ loop-seam. Giữ nguyên các cờ từ công cụ; chúng chưa phải phán quyết chất lượng hình ảnh. `mustard` là phép kiểm màu lửa của công cụ hiện có, cần xem trực tiếp khi áp dụng cho bụi vàng hoặc glint.

| Việc | Take và cờ |
| --- | --- |
| `light-column-strike-w2` | v1: white-core 0,34 + mustard; v2: mustard; v3: white-core 0,31 + mustard |
| `light-column-loop-w2` | v3: white-core 0,30 theo số đã làm tròn |
| `cutin-sparkle-motes-drift-w2` | v1/v2/v3: mustard 44/44/45 khung |
| `strip-fire-sheath-flow-w2` | v1/v2: tile-seam 2,35/1,13; v3 không có cờ |
| `fire-smoke-roll-white-w2` | v1/v3: black-residue 2,0 theo số đã làm tròn |
| `metal-sword-light-streak-w2` | v1: edge-cut top |
| `metal-light-pillar-hit-w2` | v2: mustard 1 khung |
| `sword-rain-streaks-w2` | v1/v2/v3: mustard 1 khung/take |
| `death-soul-threads-w2` | v2: mustard 1 khung |
| `gold-dust-motes-loop-w2` | v1/v2/v3: mustard 42/42/39 khung |

## Không làm và bàn giao

Không bỏ qua take nào. Không tạo nội dung AI mới, không tải gói, mở cổng, chạy build/test game, sửa mã công cụ bị cấm, sửa game hay chạy lệnh Git ghi. Chỉ chuyển đổi media và ghép các bản xem được yêu cầu. Đã bỏ khung JPG kiểm bố cục riêng; giữ các bản ghép cần bàn giao.

Claude chép bộ xem từ `.local/vfxlab/review/` sang `typing-game-review/owner-review/`, cập nhật mục lục theo quy định, gửi anh chọn take rồi đưa take được chọn vào lab. Bước này nằm ngoài phạm vi ghi của phiếu 282. Chưa chấm hoặc nhận đạt 8,5 cho bất kỳ take nào.

Không gặp hạn mức công cụ hoặc mốc giờ phải đợi.
