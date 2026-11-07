# Luồng Codex 3 · LÀM-LẠI-BLENDER: nâng 2 mẫu D1 cho đạt, rồi mới làm lô

Quy trình đã chốt: `.agents/skills/game-vfx-production/references/path-to-8.md` (§1, §2, §4). Nhận xét về D1 ở `docs/work/consult/codex-path-to-8.md` §8:
- 2 mẫu tự chấm 6,5, kỹ thuật tốt;
- tia quá nhỏ trong khung, toả tròn đều từ tâm, chỉ có 16 khung (chuẩn burst cần ≥ 24);
- khói vón thành cục tròn như bông;
- đổi sang Cycles không cải thiện. Chỗ nghẽn nằm ở thiết kế hình, chuyển động và phân lớp.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/laneS3-report.md` (tiếng Việt).

## Chạy Blender
Chỉ qua dịch vụ (Blender sập trong sandbox): viết `.local/blender-queue/<tên>.req` (dòng 1 là script trong `tools/blender-vfx/*.py`, dòng 2 là thư mục ra trong `.local/`), rồi chờ `<tên>.done`. Engine tên `BLENDER_EEVEE` hoặc `CYCLES`. Thử nhỏ trước.

## Danh sách việc (lần lượt; xong và tự kiểm mới sang việc kế)
1. **S3-1 · Tia trúng đòn có hướng** (`beast-hit-spark-burst`, vai trò lớp trúng đòn nhẹ trên quái):
   - vài tia chính dài, thuôn, đi theo hướng lực đánh (một hướng chính quạt khoảng 60°), tách khỏi lớp hạt rất mịn;
   - chớp lõi mảnh;
   - quầng màu ngà và ngọc nhạt có tiết chế;
   - chiếm 55–65 % khung;
   - ≥ 24 khung trong khoảng 0,6–0,7 s, có hạt render đủ dày, không nhân đôi khung.
2. **S3-2 · Khói mực chết có sợi** (`beast-death-ink-smoke`):
   - khói kéo thành sợi, có khe rỗng theo hướng bay lên và toả ra;
   - viền sáng nhạt;
   - tan hết về alpha 0;
   - không vón cục tròn;
   - thử một bản khối nhiễu có cuộn xoáy theo hướng và, nếu kịp trong ≤ 10 phút render, một bản Mantaflow nhỏ;
   - đánh giá ở cỡ chết thật trên quái (khoảng 1,3–1,6 lần bề ngang thân ở camera chơi).
3. **S3-3 · So với Firefly ở cùng cỡ:**
   - đặt mỗi mẫu cạnh clip Firefly đang dùng trong lab, cùng cỡ màn và trên nền sáng và tối (tấm ghép 6 khung mỗi bên);
   - kiểm tầng A đủ 5 ô (§1);
   - ghi rõ mẫu Blender có hơn không và hơn ở đâu.
   - Gửi qua báo cáo; **dừng ở đây** cho tới khi anh duyệt.
4. **S3-4 trở đi:** các dòng `todo` trong `docs/work/tasks/vfx-streams/stream-3-blender.md` (luồng 2 điền khi phân loại). **Chưa làm** cho tới khi Claude ghi vào làn rằng anh đã duyệt mẫu.

Đầu ra mỗi mẫu ở `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/blender/<job>/v<n>/`:
- PNG RGBA;
- MP4 nền đen;
- tấm 6 khung trên nền sáng và tối;
- script snapshot;
- `render.json` (seed cố định, thời gian render).
Script dùng chung đặt ở `tools/blender-vfx/`: sửa có ghi chú, không phá recipe cũ.

## Khoá khi ghi file danh sách (bắt buộc, 3 luồng cùng ghi)
Trước khi sửa bất kỳ file nào trong `docs/work/tasks/vfx-streams/`, phải giữ khoá. Các bước:
1. Lấy khoá bằng `mkdir docs/work/tasks/vfx-streams/.lock`. Nếu thất bại thì chờ 5 giây rồi thử lại, tối đa 5 phút.
2. Đọc lại file ngay sau khi giữ khoá, sửa, rồi ghi nguyên tử.
3. Nhả khoá bằng `rmdir docs/work/tasks/vfx-streams/.lock`.
Không giữ khoá lâu hơn thời gian ghi.

## Ranh giới
- **Chỉ ghi:**
  - `tools/blender-vfx/`;
  - `.local/blender-queue/`, `.local/blender-samples/`, `.local/s3/`;
  - `art-src/lab/vfx-redo-2026-11-07/blender/`;
  - ô của mình trong `stream-3-blender.md`;
  - báo cáo.
- **Không:** sửa manifest hay mã lab; lệnh git ghi; mở cổng mạng; mở trình duyệt.

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
