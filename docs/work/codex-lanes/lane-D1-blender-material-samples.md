# Làn Codex D · Việc D1 · Tự làm lại video chất liệu bằng Blender: 2 mẫu

Bối cảnh (07/11 09:15):
- Anh muốn một làn tự duyệt và tự làm lại video.
- Codex không dùng được Firefly: Firefly cần trình duyệt đã đăng nhập, chỉ Claude điều khiển được.
- Đợt làm thử đêm qua (`docs/codex-queue/laneC-report.md`, mục `redo-01`) cho thấy làm lại bằng prompt Firefly không lên 8 (0/10, trung bình 5,60 → 5,95). Làn C khuyên:
  - hình có dáng (rồng, cổng, ấn): vẽ ảnh khoá hình rồi làm image-to-video;
  - **chất liệu thuần** (tia, khói, bụi, mực): mô phỏng bằng Blender để kiểm soát nhịp bung, tan và lề khung.
- Máy có **Blender 5.2.2** ở `/Applications/Blender.app/Contents/MacOS/Blender`; chạy không cần mạng.

Việc này làm **2 mẫu** để anh xem, chưa làm lô.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/laneD1-report.md` (tiếng Việt, ngắn).

## Hai mẫu (làm lại 2 việc làn C đã chê; lời chê trong `.local/video-review/results/batch-01.json` và `redo-01.json`)
1. **`beast-hit-spark-burst`** (hình trúng đòn nhẹ trên quái):
   - chớp trúng gọn màu ngà và ngọc nhạt;
   - một nhịp tia lửa mảnh, thuôn đuôi, bắn ra nhanh rồi nguội và tắt nhanh;
   - vài lấp lánh phụ;
   - dài khoảng 0,5–0,7 s.
2. **`beast-death-ink-smoke`** (quái chết tan thành khói mực):
   - phụt khói mực đen có viền sáng nhạt, bung ra rồi thưa dần và tan hết;
   - không cắt mép khung;
   - dài khoảng 1,2–1,5 s.

**Chung:**
- 512 × 512, 24 khung/giây, nền trong suốt. Xuất cả PNG RGBA và MP4 nền đen để xem.
- Lề rộng, hình chính không chạm mép.
- Nhìn từ camera chơi cao khoảng 55 độ.
- Tham chiếu là tấm khung clip cũ (`.local/video-review/sheets/<job>__take1.jpg`) để giữ màu và cỡ. Không dùng ảnh của bên thứ ba.

## Cách làm
- Script Python cho Blender đặt ở `tools/blender-vfx/` (mới, dùng lại được cho lô sau): một file mỗi loại chất liệu, tham số ở đầu file, chạy bằng `Blender -b --factory-startup -P <script> -- <out>`.
- Sandbox chỉ ghi được trong repo. Đặt `TMPDIR`, `BLENDER_USER_CONFIG`, `BLENDER_USER_SCRIPTS`, `BLENDER_USER_DATAFILES`, `BLENDER_USER_RESOURCES` vào `.local/blender-home/`. Đầu ra vào `.local/blender-samples/<job>/`.
- Tia lửa dùng hạt phát sáng có vệt chuyển động. Khói dùng Mantaflow (hoặc khối nhiễu động nếu Mantaflow quá chậm). Render EEVEE; nếu EEVEE không chạy được ở chế độ nền thì dùng Cycles CPU với số mẫu thấp.
- Mỗi mẫu dựng tấm 6 khung giống `.local/video-review/build-sheets.py` (10, 25, 40, 55, 70, 90 %). Tự chấm theo thước của `docs/work/codex-lanes/lane-C-video-review.md`, ghi trước và sau so với điểm cũ.
- Nếu tự chấm ≥ 8: cắt flipbook thử bằng `tools/vfx-flipbook` vào `.local/blender-samples/<job>/flipbook/`, chưa đưa vào `art-src`.

## Ranh giới
- **Chỉ ghi:** `tools/blender-vfx/`, `.local/blender-home/`, `.local/blender-samples/`, báo cáo.
- **Không:** sửa video, ảnh, manifest hay mã lab; lệnh git ghi; mở cổng mạng; mở trình duyệt.
- Render nặng thì giữ cỡ nhỏ (thời gian mỗi mẫu ≤ 10 phút trên máy). Ghi thời gian render vào báo cáo.

## Đạt khi
- Có đủ 2 mẫu: PNG, MP4, tấm 6 khung, điểm tự chấm có lý do.
- Script chạy lại cho ra cùng kết quả (seed cố định).
- Báo cáo nói rõ Blender có hợp để làm lô chất liệu hay không: chất lượng, thời gian, giới hạn.

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
