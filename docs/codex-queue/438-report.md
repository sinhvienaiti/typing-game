# Phiếu 438 — mây thể tích dùng chung

Đã làm phần mã và công cụ đo. **Chưa nghiệm thu hình ảnh hoặc hiệu năng GPU**: Chrome trong sandbox không mở được DevTools (`DevTools endpoint did not come up`). Không có số p95 hay độ phủ alpha thực để kết luận đạt.

## Các đường dẫn đã sửa

Tất cả mã ở `games/.wt-ic-lab-all/`:

- `src/lab/cloud-volume.ts`: API `CloudVolume`, một hộp 12 tam giác, một material `BackSide`, tối đa một lượt vẽ ở lượt render cảnh chính; raymarch 24 bước có dừng sớm, fbm 3D ba octave, nhiễu không dùng texture hoặc phép sin trong hàm băm. Mây có mép mềm, cuộn/trôi, đáy tối/đỉnh sáng, chớp đôi bên trong ở vị trí giả ngẫu nhiên theo seed, hiện/tan và chặn màu tuyến tính ở 0,9 mỗi kênh.
- `src/lab/cloud-volume-lab.ts`: ba bộ tham số Lôi/Độc/Ám, phím thử, API console và móc đồng hồ lab; giữ hook sẵn có của stress scene, không tạo vòng lặp riêng.
- `src/lab/cloud-volume-probe.ts`: đo alpha thật ở 1280×720, số lượt vẽ riêng của mây, bao hình chiếu và thống kê p50/p95.
- `src/lab/cloud-volume-capture.ts`: kịch bản đo/chụp cho Claude, ba kiểu × ba góc; chế độ `MEASURE_ONLY=1` không ghi tệp.
- `src/lab/cloud-volume-check.ts`: kiểm tra CPU độc lập, không chạy bộ test của game.
- `src/lab/skills-main.ts`: chỉ thêm import, đăng ký bộ thử ngay cạnh bảng phím và chuyển phím cho bộ thử. Tệp này đã có thay đổi của các phiếu khác trước khi làm; giữ nguyên chúng.

## Cách thử và nối API sau

Mở `/stress.html?cloud=thunder&ui=0&dpr=1` hoặc `/skills-lab.html?cloud=thunder&ui=0&dpr=1`; đổi `thunder` thành `poison` hoặc `dark`. **Q** hiện/tan mây; **0** trở về camera chơi, **1** góc trên, **2** sau lưng. Camera chơi và góc trên hiện dùng cùng camera mặc định 55° của lab. Phím riêng chỉ có khi URL chọn một trong ba kiểu mây; Alt+1/Alt+2 vẫn dùng được. Ô nhập liệu không kích hoạt phím thử.

API dùng lại: `new CloudVolume(parent, options)`, `configure(partial)`, `show()`, `hide()`, `update(dtSeconds)`, `clear()`, `dispose()`. `parent` là nhóm FX không có phép biến đổi. Tham số gồm `centre: {x,z}`, `radius`, `baseHeight`, `thickness`, `bottomColor`, `topColor`, `glowColor`, `glowIntensity`, `lightningIntensity`, `scrollSpeed` (m/s), `coverage`, `appearSeconds`, `dissolveSeconds`, `seed`.

Mặc định: tâm `(0,0)` trên mặt phẳng XZ, bán kính 12 m, đáy 6,5 m, dày 6,5 m; hiện 0,7 s, tan 1,4 s. Console: `__cloud438.show()`, `__cloud438.configure({...})`, `__cloud438.report()`, `__cloud438.probe(120)`. `probe` in tổng số quái, GPU/DPR, số lượt vẽ mây và chênh lệch bật/tắt, p95 CPU/toàn khung có chờ GPU, độ phủ alpha và cổng đạt/trượt. Cổng thời gian chỉ đạt khi đúng stress scene 100 quái, khung 1280×720 và GPU phần cứng. `await __cloud438.live(8)` đo thêm nhịp rAF; bỏ `fixed=1` khi dùng lệnh này.

## Đã kiểm

Chạy trong worktree:

```sh
node node_modules/typescript/bin/tsc --noEmit --pretty false
node --import tsx src/lab/cloud-volume-check.ts
```

- Kiểm kiểu: 0 lỗi. Không chạy build hoặc bộ test game.
- Kiểm CPU: đạt ở 15/30/60/120 Hz; hiện/tan và đổi ý giữa chừng liên tục, xử lý số không hợp lệ, giới hạn màu, giải phóng tài nguyên, giữ hook stress và không tăng thời gian khi vẽ nhiều lượt trong cùng khung.
- Bao hình chiếu ở camera chơi 1280×720, bán kính 12 m: rộng **64,4113%**, X từ **227,77 đến 1052,23 px**. Đây là bao hình học, **không phải** độ phủ alpha đã raster. Phần cao nhất của bao hình nằm ngoài cạnh trên khoảng 44,49 px.
- Cấu trúc một mesh/một material/một lượt vẽ; con số lượt vẽ thực, độ phủ alpha ≥60% và p95 ≤16,7 ms vẫn chờ probe GPU. Chưa kiểm biên dịch GLSL trên GPU và chưa chấm chất lượng hình ảnh.
- Đã thử lệnh đo trên host worktree có sẵn `127.0.0.1:3148`; CDP không khởi động được trong sandbox. Không khởi động hoặc tắt dev server của người khác.

## Lệnh đo và chụp cho Claude

Host worktree hiện có ở cổng 3148; đổi `BASE` nếu host thay cổng. Chỉ chạy một probe GPU tại một thời điểm.

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3148/stress.html MEASURE_ONLY=1 \
CHROME_FLAGS='--disable-gpu-vsync --disable-frame-rate-limit' \
node src/kit/tools/cdp-run.mjs src/lab/cloud-volume-capture.ts \
  --width=1280 --height=720 --dpr=1
```

Chụp cả ba kiểu ở camera chơi, phím 1 và phím 2 (9 JPG, `probe.json`, `ABOUT.md`):

```sh
BASE=http://127.0.0.1:3148/stress.html \
OUT=/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/cloud-438 \
CHROME_FLAGS='--disable-gpu-vsync --disable-frame-rate-limit' \
node src/kit/tools/cdp-run.mjs src/lab/cloud-volume-capture.ts \
  --width=1280 --height=720 --dpr=1
cd /Volumes/SS990TPRO/htdocs/typing-game
node scripts/review-index.mjs
```

Claude xem chuyển động cuộn và chớp, độ dày khi nhìn sau lưng, mây có che quái quá nhiều không, cạnh trên bị cắt và các cổng trong `probe.json`. Kịch bản chưa tạo video; nếu cần duyệt chuyển động thì quay thêm từ ba URL trên. Không có khung thô cần dọn trong lượt Codex này.

## Phần để lại đúng phạm vi

Không sửa/nối `thunder-ult-chain.ts`; không sửa sim, mã game chính, script/test game hiện có hoặc tài liệu Tu Tiên. Không tạo ảnh, video, âm thanh hoặc media; shader chất liệu được phiếu này cho phép rõ ràng. Không commit, đổi nhánh hoặc thao tác Git bị cấm. Chưa có kết luận đạt 8,5; Claude cần chạy đo và xem hình trên GPU thật trước khi nối vào kỹ năng.
