# Phiếu 453 · Thay hình ba lớp tuyệt kỹ Ánh Sáng

Hoàn tất trong lab ngày 18/11/2026. Không commit, không đổi nhánh, không chạy build hoặc bộ test của game.

## File đã sửa

- `games/.wt-ic-lab-all/src/lab/light-ult-fan-space.ts`: thay FanBeams bằng một quad 4:1 cho mỗi tia B, cộng màu, chỉ xoay/đặt/co giãn đều/nhuộm màu/mờ theo nhịp cũ. Bỏ shader vẽ tia, torus, sphere và cylinder. Giữ 11 tia, các góc, đích và mốc thời gian; tia kết vẫn ở giữa. GLB giữ đủ 11.676 tam giác và các texture màu/normal/kim loại/độ nhám. Chỉ tách nhóm tam giác mặt kính để dùng emissive nhẹ, không thêm bề mặt hay mặt nạ. Điểm cầm lấy từ đỉnh thật ở mép dưới; `bbox` chiếu hộp bao thật của model, `grip` đo tay tới đúng hai điểm bám.
- `games/.wt-ic-lab-all/src/lab/light-ult-ground.ts`: ảnh C nguyên tỷ lệ trên quad nằm ngang, đỉnh ảnh neo tại chân người tung, mở theo trục quạt, cộng màu và mờ theo nhịp cũ.
- `games/.wt-ic-lab-all/src/lab/light-ult-fan.ts`: nối camera cho thẻ tia và đưa ba tài nguyên mới vào bước nạp/sẵn sàng. Không sửa logic chọn đích, nhịp trúng, nổ, hạt, camera hoặc âm.
- `games/.wt-ic-lab-all/src/lab/light-ult-review-453.mjs`: kịch bản dựa trên review-g, chọn `ult-light`, tung bằng phím 8, đổi góc bằng sự kiện Alt+1/Alt+2, ghi ảnh/video/âm và đo GPU. Phần ghi dữ liệu kiểm tra không chạy trong lượt đo hiệu năng.

Ba lớp có chú thích `// 453` kèm tên nguồn.

## Nguồn được dùng

- Tia B: `games/immortality-cultivation/art-src/lab/vfx/light/stills/light-ray-a2.v1-try2.png` (2048×512).
- Vệt đất C: `games/immortality-cultivation/art-src/lab/vfx/light/stills/light-ground-wedge.v1-try3.png` (1024×1024).
- Bảo kính: `games/.wt-ic-lab-all/art-src/lab/vfx/light/models3d/tripo/light-relic-mirror.tripo.v1.glb`, thu phóng đều để chiều cao bao ngoài bằng 1,032 m của vành kính cũ.
- Ánh môi trường: `games/.wt-ic-lab-all/art-src/lab/lookdev/misty_pines_2k.hdr` (qua symlink tới art-src của game chính). Gắn riêng vào vật liệu bảo kính, cường độ 0,85; renderer three r170 tự tạo PMREM cho bản đồ equirectangular này. Không đổi ánh sáng toàn lab.

## Kiểm cuối

| Kiểm | Kết quả | Ngưỡng |
| --- | --- | --- |
| `node_modules/.bin/tsc --noEmit` | 0 lỗi | 0 lỗi |
| Diện tích trắng, RGB từng kênh ≥ 0,95 | 0.0700955% lớn nhất / 256 khung kiểm | ≤ 6% |
| Màu tuyến tính lớp tia phụ và vệt đất | tối đa 0.9/kênh; opacity ≤ 1 | ≤ 0,9/kênh |
| p95 tổng CPU + GPU đồng bộ `readPixels` | 6.10 ms | ≤ 16,7 ms |
| p95 CPU | 1.50 ms | tham khảo |
| Co giãn thẻ tia | x = y = z ở mọi mẫu; 4 đỉnh/thẻ | giữ tỷ lệ ảnh |
| Lệch trục tia kết | ≤ 0.00000121° | giữ giữa quạt |
| Sai lệch tay tới điểm bám thật | tối đa 2.86 cm ở 16 mốc hai góc | báo đúng số thật |
| Hộp bao bảo kính | nằm trong khung ở cả 16 mốc | đúng GLB và máy quay |
| Lỗi JavaScript | 0 | 0 |

Máy: `ANGLE (Apple, ANGLE Metal Renderer: Apple M4, Unspecified Version)`. High, 1280×720, DPR 1, nền `#353a40`. Hiệu năng: 100 quái (87 mục tiêu + 13 con đi), một lượt làm nóng và ba lượt × 240 khung; p95 lấy trên 720 khung sau làm nóng. Giữ nguyên bloom và các lớp còn lại.

Lệnh chạy từ `games/.wt-ic-lab-all`:

```sh
node_modules/.bin/tsc --noEmit
node src/kit/tools/cdp-run.mjs src/lab/light-ult-review-453.mjs --width=1280 --height=720 --dpr=1
```

## Giao owner

- [Ảnh hai góc, các pha](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/light-ult-453.jpg).
- [Video hai góc có âm gốc](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/light-ult-453.mp4): 8 giây, 1280×720, 30 fps; 4 giây Alt+1 rồi 4 giây Alt+2.
- Dữ liệu: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-453/measure.json` và `summary.json`; giữ 16 ảnh pha cùng các clip hai góc. Đã thêm một dòng vào ABOUT.md của thư mục owner-review.
- Owner xem quạt tia ở 0,9 s, ánh kim và mép cầm bảo kính ở góc sau; đây là giao nộp lab, chưa tự nhận nghiệm thu mỹ thuật hay đưa vào game chính.

## Việc không làm và giới hạn

- Không tạo thêm ảnh/model/âm: đã có đúng ba nguồn được duyệt; không dùng ảnh bên thứ ba làm đầu vào công cụ tạo ảnh.
- Không sửa game chính, các lớp khác hoặc cảnh báo ngoài phạm vi. Lab vẫn báo nhiều KTX2Loader và atlas Kim `metal-crescent-sym` lỗi nhánh Canvas2D; ba tài nguyên Ánh Sáng nạp thành công, không có exception trong lượt chụp/đo.
- Điểm cầm đã chỉnh từ sai lệch tối đa 10,33 cm xuống 2.86 cm; giữ giới hạn tầm tay của rig, không đổi chiều dài xương.
- Chrome của lượt chụp đã đóng và profile tạm được runner xoá trong `finally`. Chỉ dọn khung thô do phiếu này tạo; không xoá ảnh nguồn hoặc model.
