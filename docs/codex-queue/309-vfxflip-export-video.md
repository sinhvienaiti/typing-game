# Phiếu 309 · Công cụ: `vfxflip export-video` (xuất video 1080p cho chiêu lớn từ manifest)

**Vì sao:** phím 8 và 9 của lab Tu Tiên đã chuyển từ atlas 640×360, 6 khung/giây (mờ, anh chê 06/11) sang phát thẳng video 1080p, 24 khung/giây. Agent lab-flipbooks đã xuất tay 48 video. Phiếu này biến việc đó thành lệnh của công cụ `tools/vfx-flipbook`, để làm lại được cho clip mới.

**Model `gpt-6.1-sol`, mức `xhigh`.** Báo cáo: `docs/codex-queue/309-report.md` (tiếng Việt, ngắn).

## Lời giải đã chốt
Toàn bộ quy trình nằm ở `docs/work/tasks/lab-flipbooks.md`, mục "Cách xuất video 1080p cho chiêu lớn" (dòng 62–125: đầu vào, cách tính đoạn cắt, lệnh ffmpeg, trường `video`). Làm đúng như vậy, không đổi công thức.

1. Thêm lệnh con `export-video` vào `tools/vfx-flipbook/vfxflip/__main__.py`, theo cách khai báo của các lệnh hiện có:
   ```
   tools/vfx-flipbook/run.sh export-video --manifest <đường dẫn manifest.json> [--ids a,b,...] [--jobs 3] [--force] [--dry-run] [--repo-root <thư mục>]
   ```
   Chạy qua `run.sh` (venv `~/AudioLab`, `launch.py`), vì `media.py` cần numpy mà python hệ thống không có. `--repo-root` mặc định là `Path(__file__).resolve().parents[3]`; `source` của mục tính từ thư mục này, nên test truyền thư mục tạm.
   - Mặc định xuất mọi mục không lặp (`loop` khác `true`) và chưa có trường `video`. `--force` xuất lại cả mục đã có.
   - **Bỏ qua, không ném lỗi:** mục thiếu `trim` hay `timing`, hoặc `source` không phải một file `.mp4` có thật (ví dụ mục cũ ghi `source` bằng chữ trong `fire`, `aura`). In `skip <id>: <lý do>`.
   - Xuất lại khi `take` đổi (`lab-flipbooks.md` dòng 127): ghi `video.take`; nếu `video.take` có và khác `take` của mục thì xuất lại như đang dùng `--force`. Thiếu `video.take` (48 video đang có) thì coi như cùng take, không xuất lại.
   - `--dry-run` chỉ in kế hoạch: id, khung START và END, thời lượng, `peakTime`.
2. Viết phần lõi ở module mới `vfxflip/video_export.py`:
   - Đọc mục và file `<id>.json` cạnh manifest.
   - Tính `START = trim.start`, `END = trim.end`, `peakTime = timing.peak × trim.step / sourceFps` (nếu thiếu `sourceFps` thì dùng 24), làm tròn 3 chữ số thập phân. **`video.pivot` không chép từ mục:** tính theo toàn khung nguồn như `lab-flipbooks.md` dòng 119: `[(pivot.x × cropW + cropX) / srcW, (pivot.y × cropH + cropY) / srcH]`, với `source.crop = [cropX, cropY, cropW, cropH]`, `source.width = srcW`, `source.height = srcH` lấy từ `<id>.json` cạnh manifest; làm tròn 4 chữ số. Ví dụ đúng trong manifest thật: `expansion/myriad-lotus-domain` có `pivot` [0.4982, 0.4921] mà `video.pivot` [0.4981, 0.4916].
   - Chạy ffmpeg đúng lệnh ở mục 3: ghi file tạm, xong mới đổi tên.
   - Đọc `w`, `h` thật bằng ffprobe.
   - Ghi trường `video` theo mục 4 bằng cách ghi nguyên tử: `json.dumps(..., indent=1, ensure_ascii=False)` cộng một dòng trống cuối, ra file tạm rồi `os.replace`, giống cách các manifest hiện có được lưu. Mọi trường khác của mục giữ nguyên.
   - Chạy song song tối đa `--jobs` tiến trình.
3. Hàm tính toán (đoạn cắt, `peakTime`) tách riêng để test không cần ffmpeg.

## Được ghi
`tools/vfx-flipbook/vfxflip/__main__.py`, `tools/vfx-flipbook/vfxflip/video_export.py` (mới), `tools/vfx-flipbook/tests/test_video_export.py` (mới), README của công cụ nếu có, và báo cáo.

**Cấm:**
- mọi lệnh git ghi;
- sửa manifest thật trong `games/*/art-src` (chỉ dùng `--dry-run` trên manifest thật);
- sửa file ngoài danh sách được ghi;
- mạng.

## Test (pytest theo `tools/vfx-flipbook/pytest.ini`)
- Tính đoạn cắt và `peakTime` đúng trên 3 mục giả: `step` 4, `peak` 0; `step` 4, `peak` 7; thiếu `sourceFps`.
- `video.pivot` đúng công thức vùng cắt với một `source.crop` khác 0. Kiểm thêm bằng số thật của `expansion/myriad-lotus-domain` (đọc `pivot`, `<id>.json` và so với `video.pivot` đang có, sai lệch ≤ 0,0001).
- Bỏ qua mục `loop: true`, mục đã có `video` cùng `take` (trừ khi `--force`), và mục thiếu `trim`, `timing` hay `.mp4`. Xuất lại khi `take` đổi.
- Với một video nguồn tạo bằng ffmpeg `testsrc` 2 s ở 24 khung/giây trong thư mục tạm: xuất ra đúng số khung (`END − START`), 24 khung/giây, H.264, `yuv420p`, và manifest tạm có trường `video` đúng.
- Ghi manifest giữ nguyên các mục và trường khác.

## Xong khi
- Test cũ và test mới đều qua.
- Đã chạy `tools/vfx-flipbook/run.sh export-video --dry-run` trên `games/immortality-cultivation/art-src/lab/vfx/expansion/manifest.json` (30 mục, đều đã có `video`) và trên `.../vfx/fire/manifest.json`, rồi dán kết quả vào báo cáo. Kết quả phải là: expansion 0 mục cần xuất; fire liệt kê các mục sẽ xuất (khoảng 6) và các mục `skip` kèm lý do. Chỉ chạy thử, không xuất thật.
