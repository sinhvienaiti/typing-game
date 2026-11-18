# Critic 325, vòng 2 (06/11/2026): PASS

**Ba lỗi vòng 1 đã sửa đúng, không còn số hay đường dẫn cũ.**
- Dòng 135 ghi rồng 31 khung, khoảng 5,2 s. `range(0,121,4)` cho 31 khung, đúng với trim 0–121 bước 4 và 31 khung của atlas cũ.
- Dòng 138 dùng N/N+2. Bộ kiểm hôm nay in `333 task entries, 0 problems`. Dòng `hybrid … entries parse OK, … from this task` đúng định dạng của `validate-manifests.ts:28`.
- Dòng 60 dùng `TOOL_DIR / "ktx2" / "encode.mjs"`. `TOOL_DIR` có ở `pipeline.py:15`, và `launch.py` đổi thư mục khi chạy test nên đường dẫn tuyệt đối là cần.

**Không có mâu thuẫn mới.**
- `--fps 6` của rồng có vector, nên hợp lệ. Test đầu cuối chạy ở 12 khung/giây (fixture 24 khung/giây, bước 2).
- Lưới 4×8 là kết quả `atlas.grid(31 hoặc 32, 768, 432)`, tức 3072×3456, dưới 4096. Mặc định `--frames 64` sẽ vượt trần, nhưng cả hai lần chạy đều ghi `--frames 32`.
- Số liệu test `fixed_rate` (61 khung; 30 khung, `end` 60) khớp công thức.

**Khớp với mã:**
- Dòng code được trích: pipeline 323/368/387/476/484/523; `lab_batch` 270–277, 317–379, 371–378.
- Hàng bảng của rồng có `whiteFix: off`, sao chổi nằm trong thư mục `fire` nên dùng look `cool`. Đặt `post = None` cho kết quả giống bản vá `cool_dim`.
- Công thức `head.cellUv` tính lại ra [0.7745, 0.7629].
- Bộ test hiện có 54 test. Hai khoá `fps` và `look` mới không trùng khoá nào trong ba bảng.

**Ghi chú (không chặn):**
- Thêm hai test cho luật mới: "`--fps 6 --no-mv` → lỗi; `--max-atlas 256` → lỗi, `<out>` không có file mới".
- `__main__` chỉ bắt `FileNotFoundError`, `MediaError` và `VideoExportError`. Lỗi `look`, `fps` và `--max-atlas` nên ném `media.MediaError` (hoặc bắt thêm `ValueError`) để in lỗi gọn, không in traceback.
- Mục "Thư mục ảnh chụp" nên ghi tên thật: `<job>__v1.{sheet.jpg,preview.mp4,metrics.json}`. Xoá `<job>__v1.atlas.png` và `.json` (đã chép sang `hybrid/`).
- `node scripts/review-index.mjs` ghi `INDEX.md` ngoài danh sách được ghi; nên thêm `typing-game-review/INDEX.md` vào danh sách đó.
- Mục like không có `video` thì không có `peakTime`/`pivot`; test đầu cuối phải tạo `video`, `trim` và `timing` trong mục like.
