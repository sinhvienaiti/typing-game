# Phiếu 433d — Kim mưa kiếm: trận pháp và kiếm trong không gian 3D

Ngày **17/11/2026**. Đã sửa mã trong `games/.wt-ic-lab-all`; kiểm kiểu **0 lỗi**, probe hình học/camera/vòng đời đạt. **Chưa nghiệm thu hình và GPU:** host `http://127.0.0.1:3146/stress.html` không kết nối được trong phiên này. Chưa có capture, video, số p95 GPU hoặc xác nhận giải mã ảnh/biên dịch GLSL trong trình duyệt. Không dùng số CPU thay cho cổng 16,7 ms hay điểm hình 8,5.

## Tệp giao

Trong worktree `games/.wt-ic-lab-all/`:

- `src/lab/metal-ult-rain.ts`: mặt XZ thật, tia rủ/ribbon giao nhau trong thế giới, nguồn và đường bay kiếm GLB, probe khung.
- `src/lab/metal-ult-layered.ts`: camera còn 75% khoảng cách gốc; giữ lịch vào/giữ/trả.
- `src/lab/metal-ult-rain-check.mjs`: kiểm kiểu tập trung, GLB thật, số kiếm rơi, nguồn dưới trận, lịch chạm và trả pool.
- `src/lab/metal-ult-camera-check.mjs`: camera, hộp bao và hình học bất biến khi đổi góc chơi/trên thẳng đứng/sau lưng.
- `src/lab/metal-ult-rain-review.mjs`: lệnh Claude chụp góc chơi/Alt+1 và sau lưng/Alt+2, quay clip 4 giây, đo stress và console.

Báo cáo ở repo cha: `docs/codex-queue/433d-report.md`. Không sửa `ult-camera-punch.ts`, mã game hay công cụ dùng chung. Không tạo art/media mới, không đưa media vào Git, không đổi nhánh; không commit/push/reset/clean/stash; không chạy build hoặc bộ test game.

## Kết quả mã

- Trận dùng `metal-caster-seal`, mặt **XZ**, pháp tuyến **−Y**, hai mặt; cao **8 m**, đường kính **12 m**. Không dùng `formation-sky` hoặc `sword-fall-streak` làm thẻ. Hai ảnh 435 và storyboard 431 chỉ dùng để đối chiếu màu, độ mềm và bố cục.
- Fit một lần cho toàn bộ thể tích trận/tia rủ và 17 mẫu nhịp camera, rồi giữ nguyên tâm thế giới trong lượt tung. Vòng lắc trong **±3°**, nhịp sáng nhẹ. Tia rủ là 20 cặp mặt phẳng giao nhau, từ gần viền vòng xuống **y = 0,05 m**; không quay theo camera. Thu vòng từ 14 xuống 12 m vì vòng 14 m cùng tia rủ cao 8 m không có vị trí cố định vừa dưới thẻ tên suốt nhịp camera trong fixture.
- **49 kiếm dùng cùng GLB Tripo/PBR** cả lúc bay lẫn cắm, **5.570 tam giác/kiếm**; giữ texture, normal và roughness. Kiếm thường cao **5,010–5,929 m**. Chuôi xuất phát bên trong vòng, ở **y = 7,85 m**; cả lưỡi nằm dưới mặt trận. Kiếm hướng theo đường bay 3D tới điểm chạm đã chọn, rồi dựng về tư thế cắm nghiêng trong 0,1 giây. Ribbon giao nhau theo chính trục bay, cắt bớt phần đầu/đuôi của art vệt cũ và lọc mềm; không dùng thẻ kiếm phẳng. Độ dài ribbon thường giới hạn tới nguồn dưới trận.
- Kiếm cuối **16,5 m = 3 × cỡ chuẩn 5,5 m**, rơi xuyên qua vùng trời và cắm ở **2,4 s**; riêng kiếm này dài hơn độ cao trận. Giữ `metal-impact-v2`, ground mark **7,25 / 22,5 m**, dư âm bụi vàng và tan hết ở 4 s.
- Camera: **0,5 s** vào, giữ tới **2,6 s**, **0,6 s** trả; khoảng cách còn **75%**, góc **55° → 49°**, FOV **28° → 34° → 28°**. Tâm shot nằm 65% từ caster tới tâm mục tiêu, để cả vòng và tia rủ cùng vừa khung. Trả vị trí sai số **0 m** trong fixture; `?ultCam=0` vẫn hoạt động.
- Giữ ba đợt **0,6 / 1,05 / 1,5 s**, 36 kiếm nhắm mục tiêu + 12 kiếm rải + kiếm cuối, đường sát thương và lịch âm của host; nhánh `?metalUlt=ring` đạt kiểm tra cũ.

## Đã kiểm

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
node node_modules/typescript/bin/tsc --noEmit
node src/lab/metal-ult-rain-check.mjs
node src/lab/metal-ult-camera-check.mjs
node --check src/lab/metal-ult-rain-review.mjs
```

- Kiểm kiểu toàn worktree và kiểm kiểu tập trung: **0 lỗi**. Cú pháp kịch bản review: đạt.
- Qua 240 bước/60 Hz: vòng, toàn bộ tia rủ và caster vừa khung; không giao thẻ tên. Probe độc lập thêm yaw **0° / 20,05°**, có/không thẻ tên, đối chiếu 360 điểm trên biên. Mép vòng thấp nhất **93,92 px = 13,04%** khi không có thẻ; **172,01 px** với fixture thẻ kết thúc ở y = 154 px.
- Hình học và các buffer của trận/tia/ribbon/ground mark không đổi khi chiếu bằng camera chơi, trên thẳng đứng 90° và sau lưng; pháp tuyến vòng −Y, ribbon có bề rộng ở cả X và Z. Đây là kiểm tọa độ CPU, chưa phải xem ảnh thật.
- **Ít nhất 8 kiếm GLB đang rơi** trong mọi bước ở 0,8–2,0 s, cao hơn yêu cầu 4. Tất cả kiếm thường bắt đầu dưới vòng và hướng theo quỹ đạo 3D. **49/49** chạm, **49/49 slot trả ở 4 s**; năm lượt tung/xóa, nạp chậm rồi clear/dispose đều đạt; không tạo lại pool sau mỗi lượt tung.
- Camera 15/60/120 Hz, có/không parent, bật/tắt shot và phục hồi hook: đạt. Tối đa **272.930 tam giác kiếm**. Lượt cuối: lập kế hoạch **1,116 ms**, p95 cập nhật recipe CPU **0,199 ms**; không phải p95 GPU.
- Probe đọc GLB thật và kiểm đường dẫn atlas nhưng thay bộ nạp ảnh bằng texture CPU. Vì vậy **chưa xác nhận 0 lỗi nạp ảnh trên trình duyệt**.

Hộp bao `[trái; trên; phải; dưới]` tại **1280×720**, thẻ tên tới y = 154 px:

| Giờ | Vòng (px) | Cả tia rủ, bao bảo thủ (px) |
| --- | --- | --- |
| 0,4 s | `[420,41; 192,75; 859,59; 523,07]` | `[411,29; 187,41; 868,71; 679,50]` |
| 1,2 s | `[417,78; 191,14; 862,22; 523,34]` | `[408,57; 185,81; 871,43; 682,69]` |
| 2,4 s | `[417,78; 191,14; 862,22; 523,34]` | `[408,57; 185,81; 871,43; 682,69]` |

Tâm vòng fixture cố định **(0; 8; −0,23888) m** ở cả ba mốc. Không lấy các số này thay hình chiếu của host thật.

## Claude chạy tiếp

Cần host phục vụ **đúng worktree này**, không chạy build. Kịch bản từ chối host thiếu trường 433d.

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3146/stress.html \
VIEWS=top,behind \
OUT=/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/metal-ult-rain-433d \
ART_MAGICK=/opt/homebrew/bin/magick \
../../.local/bin/heavy.sh --perf node src/kit/tools/cdp-run.mjs \
  src/lab/metal-ult-rain-review.mjs --width=1280 --height=720 --dpr=1
```

Mặc định tạo 8 ảnh, 2 sheet, **`433d-top-4s.mp4`**, `433d-measure.json`, `ABOUT.md`; cập nhật chỉ mục review. Clip gồm 96 khung mô phỏng ở 24 fps, dài đúng 4 giây, **không thu âm**. Khung video riêng từng lượt nằm trong `typing-game-review/captures/tu-tien/metal-ult-rain-433d/frames-<mã>/`; sau mã hóa, kịch bản chạy prune xem trước rồi `--apply` cho đúng thư mục nó tạo.

`top` chính là camera chơi 55°/nút **1** trong lab; phím tắt thực tế là **Alt+1**. `behind` là nút **2**, phím **Alt+2**; số 1/2 riêng đang dùng để tung chiêu, không sửa bộ phím ngoài phạm vi. Góc sau lưng tự nạp `?ultCam=0` để shot không ghi đè góc của host. Camera 90° chỉ có probe tọa độ, chưa có lệnh host để chụp góc này.

Đo ở góc chơi với **87 TargetField + 13 walker = 100 quái**, bắt buộc p95 toàn khung qua `readPixels` **≤ 16,7 ms**, đủ kiếm rơi, trả pool và tài nguyên GPU ổn định qua năm lượt. Kịch bản kiểm `assetsReady`, lỗi GLB/ảnh, console và exception; thất bại sẽ báo lỗi. Chỉ lấy số, không ghi capture: thêm **`METRICS_ONLY=1`**. Bỏ video: **`CLIP=0`**. Đối chiếu camera tắt: dùng BASE có `?ultCam=0`, VIEWS=top và OUT riêng.

Owner cần xem độ mềm ribbon/tia rủ, hướng kiếm tỏa từ dưới vòng tới quái, vòng 12 m, kiếm cuối 16,5 m và hình chiếu sau lưng. **Còn chờ p95 GPU, console/nạp ảnh thật, capture/video và duyệt hình; chưa chấm đạt 8,5.**
