# Làn Codex (chạy ở làn A) · Duyệt đợt làm thử `redo-01`

Làm **đúng như** `docs/work/codex-lanes/lane-C-video-review.md` (thước chấm, kết luận, prompt làm lại, đầu ra, ranh giới), với ba khác biệt:

1. **Chỉ một đợt:** `.local/video-review/todo/redo-01.json`, kết quả ghi vào `.local/video-review/results/redo-01.json`. Không làm đợt `batch-*`, vì làn C đang làm các đợt đó.
2. **So trước và sau.** Mỗi việc `<job>-q1` là bản làm lại của `<job>`, theo prompt mới mà làn C viết ở `results/batch-01.json`.
   - Thêm trường `before` vào mục kết quả: `overall` cũ của `<job>` trong `batch-01.json`.
   - Ghi một dòng: prompt mới có sửa được đúng điều đã chê không.
3. **Các mục không có `-q1`:**
   - `foe-rock-impact-shatter-r3` và `results-victory-rays-loop-r2`: lần làm lại vì cụt mép và vì vòng lặp không liền.
   - `i2v-yin-yang-void-mirror-manifest-r3`: ảnh đầu đã thu nhỏ 85 % để không cụt mép.
   - `metal-sparkle`: việc mới.
   - Chấm như thường. Với việc có 2 take, chọn `best`.

**Báo cáo:** thêm một đoạn ≤ 8 dòng vào `docs/codex-queue/laneC-report.md`, tiêu đề `redo-01 (làm thử)`:
- số đạt trên 10 việc làm thử;
- điểm trung bình trước và sau;
- 2 việc tăng điểm nhiều nhất và 2 việc không tăng;
- nhận định: làm lại bằng prompt có đưa clip lên 8 được không, hay cần ảnh hoặc cách khác.

**Model `gpt-6.1-sol`, mức `high`.**

## Hết hạn mức
Ghi phần đã xong vào `redo-01.partial.json`. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
