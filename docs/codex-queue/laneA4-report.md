# Làn A4 · Hai mẫu ảnh nguồn cho image-to-video

07/11/2026. Đủ **4 PNG + 4 prompt**, đúng 2 mẫu × 2 bản, dùng `image_gen` tích hợp 4 lần; không gặp hạn mức. Khổ thật **1254 × 1254**, đúng 1:1 (công cụ xuất khác yêu cầu 1024). Đã xem cả bốn ảnh và bảng ghép.

`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/`.

Ảnh: `S/{boss-entrance-vortex,blood-ring-burst}-still.v1-try{1,2}.png`, mỗi ảnh có `.prompt.txt` cùng gốc tên, lưu nguyên văn prompt và đường dẫn tham chiếu.

**Bảng gửi anh:** [samples.jpg](../../.local/still-samples-0711/samples.jpg), 1328 × 1388; hàng trên cổng, hàng dưới vòng Huyết; trái try1, phải try2. Đề xuất **try2 của cả hai mẫu**, chờ anh chọn.

## Nguồn đã đưa vào mỗi lượt vẽ

Đúng 3 ảnh nội bộ: `S/foe-boss-phase-roar.v1-try2.png` (phiếu 321, chỉ màu Lang Vương và lớp năng lượng); `games/immortality-cultivation/art-src/lab/vfx/sigils/blood/blood-arcs.png` (chất huyết quang); một khung của clip tương ứng, cắt từ `.local/video-review/sheets/<job>__take1.jpg` vào `.local/still-samples-0711/<job>-reference-frame.png`. Cổng chọn 10% vì dải xoáy rõ, ít sét; vòng chọn 25% vì vành còn mảnh. Chỉ giữ bố cục khung cũ, sửa lỗ tim thành tròn/oval và sửa vòng đứng thành ellipse nằm ngang. Không đưa ảnh bên thứ ba vào công cụ.

## Tự chấm /10 theo thước làn C

Tổng là phán đoán, không lấy trung bình. Chuyển động **KĐG** vì đây là ảnh tĩnh; các điểm chỉ dùng chọn ứng viên ≥8, không phải PASS video hoặc nghiệm thu 8,5 trong game.

| Ảnh | Cuốn hút | Nhiều lớp | Lực | Chuyển động | Đúng việc | Kỹ thuật | Tổng | Kết luận |
| --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |
| boss-entrance-vortex try1 | 8 | 8,5 | 8 | KĐG | 8,5 | 7,5 | 7,8 | Oval đen rõ, nhiều dải khí; lề trên/dưới còn hẹp. |
| boss-entrance-vortex try2 | 8,5 | 8,5 | 8 | KĐG | 8,5 | 8 | **8,3** | Ứng viên: lỗ tròn, xoáy bất đối xứng, lề rộng; nét sáng vẫn hơi giống dải lụa. |
| blood-ring-burst try1 | 8 | 8,5 | 7,5 | KĐG | 8 | 7 | 7,6 | Ellipse rỗng rõ, có giọt; vành trước dày và lề ngang quá hẹp. |
| blood-ring-burst try2 | 8 | 8,5 | 8 | KĐG | 8 | 8 | **8,1** | Ứng viên: vành mảnh nhiều lớp, bụi pha lê, ellipse nằm ngang; cần video để chứng minh lực bung. |

## Kiểm tra và điểm anh cần xem

- Cả bốn PNG sao chép nguyên bản, SHA-256 khớp nguồn công cụ; không hậu kỳ. Số đo và băm ở `.local/still-samples-0711/checks.json`.
- Hộp sáng ngưỡng xám 2%: cổng try1 `1045×1085+105+75`, try2 `767×777+239+197`; vòng try1 `1154×560+52+329`, try2 `997×452+126+380`. Không chạm mép; lề ngang vòng try2 khoảng 10%, còn ít hơn yêu cầu prompt.
- Nền nhìn đen nhưng một số góc còn **1–2/255**, chưa đạt RGB 0 tuyệt đối; cần quyết định chuẩn hóa trước I2V. Không thấy chữ/logo, sói, vũ khí hay vật thừa trên ảnh mới.
- Anh xem độ oai của cổng, độ mảnh/thoáng và phối cảnh vòng Huyết. Góc 55° được yêu cầu trong prompt nhưng không thể xác nhận chính xác từ tranh; hai vòng nhìn khá dẹt. Khói đỏ sẫm tinh, sao/glint nổi hơn khói.
- Chưa làm lô, video, âm thanh, tích hợp hoặc chấm mù/runtime vì ngoài phiếu. Không sửa nguồn cũ, không mở trình duyệt, không chạy build/test hoặc Git ghi.

