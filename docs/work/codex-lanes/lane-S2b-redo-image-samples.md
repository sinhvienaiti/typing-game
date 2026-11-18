# Luồng Codex 2 · Bước S2b · Làm lại video có hình: 2 mẫu ảnh đầu, cùng danh sách làm lại từ ảnh cũ

Anh (07/11 12:00): "đồng ý, chạy thêm song song phần video lại để video đạt chất lượng tốt như vậy mới ra được lab tốt được". Làm **sau khi T0 xong**: `docs/work/tasks/vfx-streams/stream-2-image.md` phải đã có dòng. Chưa có thì ghi "chờ T0" vào báo cáo rồi dừng.

Quy trình: `.agents/skills/game-vfx-production/references/path-to-8.md` §2 (chẩn đoán), §4 (nhãn), §5 (ảnh đầu cho image-to-video), §7 (bước nhỏ). Kiểu ảnh anh đã duyệt: 2 bản try2 ở `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/` (`boss-entrance-vortex-still.v1-try2.png`, `blood-ring-burst-still.v1-try2.png`): khí năng lượng trong suốt nhiều dải, lõi mảnh, sao nhỏ, đốm sáng, nền đen thuần, lề rộng.

**Model `gpt-6.1-sol`, mức `high`.** Một lần chạy, **tối đa 12 ảnh xem**. Báo cáo: thêm ≤ 10 dòng vào `docs/codex-queue/laneS2-report.md`.

## Việc
1. **Danh sách làm lại từ ảnh cũ** (cột ảnh `giữ`: ảnh đúng, video hỏng). Không vẽ gì. Với **mọi** dòng `giữ`, viết một mục việc Firefly vào `.local/s2/i2v-jobs.json` (mảng):
   - các trường: `id` = `<job>-i2v2`, `image` (URL `http://127.0.0.1:8864/still/<tên ảnh>`, chỉ khi ảnh nằm trong `stills/skills/` và tên đúng dạng `<id>.v<n>-try<k>.png`; không đúng thì ghi `needsCopy: true` cùng đường dẫn ảnh), `frame: "first"`, `ar`, `aspect` (chuỗi JSON **không có dấu cách**, ví dụ `{"height":1080,"width":1920}`), `takes: 2`, `use`, `source`;
   - `prompt` viết theo §5: câu khẳng định, nói rõ cái gì chuyển động, giữ nguyên hình của ảnh, nền đen, camera cố định, lề rộng; không nhờ clip tự tan (engine lo).
   - Claude sẽ đọc file này và chạy Firefly.
2. **Ảnh đầu mới: 2 mẫu.** Lấy **2 dòng đầu** có ảnh `sửa` hoặc `mới` theo thứ tự ưu tiên, mỗi dòng vẽ 2 bản (`try1`, `try2`) bằng image_gen:
   - **bắt buộc** đưa ảnh tham chiếu của ta: 2 ảnh try2 làm kiểu, cùng ảnh nội bộ gần nhất của chính việc đó (ảnh cũ, hoặc khung đẹp nhất của clip cũ trong `.local/video-review/sheets/`) để giữ bố cục;
   - ghi đường dẫn tham chiếu vào `.prompt.txt`; không dùng ảnh của bên thứ ba.
   - Lưu `<job>-still.v1-try<k>.png` cùng `.prompt.txt` vào `stills/skills/`.
   - Tự chấm theo thước tầng A (§1) cộng vẻ đẹp; ghi bản đề xuất.
   - Ghép 4 ảnh thành `.local/s2/still-samples-2.jpg` để Claude gửi anh. **Chưa vẽ thêm** cho tới khi anh duyệt.
3. Cập nhật cột trạng thái các dòng đã xử lý trong `stream-2-image.md` (theo luật khoá): `i2v-ready` cho dòng `giữ`; `sample-drawn` cho 2 dòng có mẫu.

## Ranh giới
- **Chỉ ghi:**
  - ảnh mới trong `stills/skills/`;
  - `.local/s2/`;
  - `docs/work/tasks/vfx-streams/stream-2-image.md` (có khoá);
  - báo cáo.
- **Không:** sửa video, manifest hay mã; chạy Firefly; lệnh git ghi; mở trình duyệt.

## Hết hạn mức
Khi image_gen báo hết lượt, giữ file đã có và ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
