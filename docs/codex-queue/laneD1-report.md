# Làn D1 · Hai mẫu chất liệu Blender · 07/11/2026

Đã làm đủ **2 mẫu để anh xem**, chưa đạt chất lượng để làm lô. Chỉ render qua dịch vụ `tools/blender-vfx/render-service.sh`; không gọi Blender trực tiếp, không mở trình duyệt, không chạy build/test game.

## Tệp để xem

Mỗi thư mục có PNG RGBA trong `rgba/`, MP4 nền đen, tấm 6 khung `*.sheet.jpg`, tấm nền sáng `*.sheet-light.jpg`, prompt kèm từng hình, bản chụp script, `render.json` và `validation.json`.

- Tia lửa: [.local/blender-samples/beast-hit-spark-burst/](../../.local/blender-samples/beast-hit-spark-burst/); [MP4](../../.local/blender-samples/beast-hit-spark-burst/beast-hit-spark-burst.mp4), [6 khung](../../.local/blender-samples/beast-hit-spark-burst/beast-hit-spark-burst.sheet.jpg).
- Khói mực: [.local/blender-samples/beast-death-ink-smoke/](../../.local/blender-samples/beast-death-ink-smoke/); [MP4](../../.local/blender-samples/beast-death-ink-smoke/beast-death-ink-smoke.mp4), [6 khung](../../.local/blender-samples/beast-death-ink-smoke/beast-death-ink-smoke.sheet.jpg), [nền sáng](../../.local/blender-samples/beast-death-ink-smoke/beast-death-ink-smoke.sheet-light.jpg).
- Script dùng lại: [tools/blender-vfx/README.md](../../tools/blender-vfx/README.md), `spark_burst.py`, `ink_smoke.py`, `common.py`, `finish_samples.py`. Không sửa mã lab, manifest hoặc `art-src`.

## Tự chấm theo thước làn C

Điểm tổng là phán đoán, không lấy trung bình. Đây là tự chấm mẫu ngoài game, chưa phải duyệt độc lập trong play host.

| Mẫu | Cuốn hút | Chi tiết | Lực | Chuyển động | Đúng việc | Kỹ thuật | Cũ → redo-01 → D1 | Kết luận |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| beast-hit-spark-burst | 6 | 6 | 6 | 8 | 8 | 9 | 5 → 5 → **6,5** | REDO |
| beast-death-ink-smoke | 6 | 6,5 | 6 | 7 | 8 | 9 | 6 → 6 → **6,5** | REDO |

**Tia lửa:** một chớp ngà, 42 hạt có đuôi thuôn và 22 đốm phụ; ngọc nhạt đã xuất hiện, tắt nhanh, không phát thêm đợt cuối. Tuy nhiên ở cỡ toàn khung vẫn khá nhỏ, các tia còn tỏa hướng tâm, quầng và lấp lánh phụ yếu; chưa có sức hấp dẫn của VFX thương mại cao cấp.

**Khói:** bung nhanh rồi giảm mật độ và bị xói; lề sạch, đã tan hết cuối clip. Thân tối hiện rõ khi ghép lên nền sáng, không dùng luma-key làm mất mực đen. Tuy nhiên các cụm còn tròn như bông, thiếu sợi xoáy kéo dài và viền sáng thanh, nên chưa đạt 8. Dùng khối nhiễu động có giới hạn thay Mantaflow; chuyển động là biến đổi trường nhiễu, không phải mô phỏng dòng khói vật lý.

## Kiểm tra và thời gian

| Mẫu | Xuất | Render bản đủ | Lề nhỏ nhất ở alpha > 2/255 |
| --- | --- | ---: | ---: |
| Tia lửa | 16 PNG, 512×512, 24 fps, 0,667 s | **3,605 s** | 174 px |
| Khói | 36 PNG, 512×512, 24 fps, 1,5 s | **30,004 s** | 117 px |

- Blender 5.2.2 LTS, EEVEE, camera trực giao cao 55°. Đã thử 64 px trước bản đủ; đã sửa API compositor 5.2. Không có lần Blender sập.
- Cả hai: alpha trên bốn mép bằng 0 trong mọi khung; khung cuối alpha bằng 0. `ffprobe` xác nhận MP4 đủ số khung, 512×512, 24 fps.
- Seed cố định 71101/71102. Render lại 5 khung/mẫu bằng tiến trình mới: **10/10 khớp toàn bộ pixel RGBA**, sai khác lớn nhất 0; [reproducibility.json](../../.local/blender-samples/reproducibility.json). Hash tệp PNG khác do metadata ngày/giờ render.
- Thử khói Cycles CPU, 16 samples: 3 khung mất **84,5 s** (24,8–31,4 s/khung), không cải thiện đủ để bù thời gian; bản 36 khung cùng cấu hình sẽ vượt 10 phút nên không render đủ bằng Cycles. [So engine](../../.local/blender-samples/probes/engine-comparison.jpg).
- Tham chiếu duy nhất là hai tấm `.local/video-review/sheets/<job>__take1.jpg` được giao. Không tạo ảnh AI hoặc dùng ảnh bên thứ ba.

## Kết luận

**Blender phù hợp để kiểm soát thời lượng, lề và alpha cho lô chất liệu; hai script hiện tại chưa đủ đẹp để chạy lô tự động.** EEVEE đủ nhanh, còn giới hạn chính là tạo xoáy khói, phân lớp sáng và nhịp tia có hướng. Bước tiếp theo nên thử Mantaflow ở độ phân giải thấp cho khói và cải thiện phân lớp tia trước khi mở lô.

Chưa cắt flipbook vì cả hai dưới 8; chưa đưa vào game hoặc `art-src`. Anh cần xem hai MP4 ở cỡ hit/death thực tế, nhất là độ nhỏ của tia và cảm giác khói còn tròn. PNG của hai bản đủ được giữ nguyên; ảnh thử thừa được dọn, giữ phép đo và tấm so engine.
