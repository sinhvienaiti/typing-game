# Phiếu 422b — màu lửa và hướng vòng đất trong lab

Ngày 16/11/2026. **Đã sửa mã; kiểm kiểu và phép đo CPU đạt. Chưa nghiệm thu pixel GPU trong host.**

## Tệp đã sửa

- `games/.wt-ic-lab-all/src/lab/burst-v2.ts`.
- `docs/codex-queue/422b-report.md`.

Chỉ hai đường dẫn trên được sửa. Không tạo ảnh/âm thanh, không đổi nguồn atlas/JSON, không chạy build hay test suite game, không commit/push, không đổi nhánh. Đã đọc phiếu và báo cáo 422 trước khi sửa. Hạn mức đầu phiếu còn 20%.

## Thay đổi

- `fire-big-burst-v2`: thêm gradient hai đầu màu tuyến tính `[1, 0.42, 0.02]` → `[1, 0.72, 0.22]` ngay trong bảng. Shader áp dụng sau phần xuất màu của clip, trước tag mask và fade đáy. Chuẩn hóa gradient theo luma Rec.709 để giữ năng lượng từng pixel; alpha, hình dạng, thời gian, scale và intensity của lửa giữ nguyên. Xử lý trực tiếp RGB premultiplied, kể cả additive có alpha bằng 0.
- `earth-ring-burst-v2`: nhánh `flat: true` riêng; xoay mesh −90° quanh X và chiếu toàn bộ thẻ lên XZ, cao 0,01 m để tránh z-fighting. Đổi ngược tọa độ tâm instance trước khi áp model matrix, nên vị trí phát theo trục thế giới không bị xoay theo thẻ. Không dùng billboard cho nhánh này. Hiệu chỉnh scale `0,248 → 0,28`, intensity `1,543 → 1,7` để bù diện tích chiếu và giữ số đo 422.
- 15 clip còn lại giữ shader hình học và hiệu chỉnh cũ; khóa shader phân biệt flat, ground, billboard và gradient. Hook vẫn phục hồi sau caller gọi `layFlat`.

## Kết quả đã chạy

Camera thật từ `fitCamera`: nghiêng 55°, FOV 28°, 1280×720, không inset, vị trí hiệu ứng (0, 0, −6), cỡ caller 4 m. Raster CPU trên nền đen, giải mã atlas PNG từ sRGB về tuyến tính, lọc song tuyến tính, quét từng tick 60 Hz. Đỉnh là khung có nhiều pixel luma tuyến tính > 0,15 nhất; nếu bằng nhau chọn khung có độ sáng cao hơn. Độ sáng là trung bình 1% pixel sáng nhất toàn khung (9.216 pixel, kể cả phần đen).

| Tiêu chí | Kết quả |
| --- | --- |
| Hue lửa, trung bình HSV từ RGB sRGB hiển thị trong vùng sáng | **37,72°**, trong 25–45° |
| Hue nếu tính trực tiếp trên RGB tuyến tính | **27,33°**, cũng trong 25–45° |
| Pháp tuyến +Z của mesh earth quy ra thế giới | **(0, 1, 2,22×10⁻¹⁶)** |
| Góc với pháp tuyến đất (0, 1, 0) | **0°**, đạt ≤ 20° |
| Mặt phẳng các đỉnh earth | **y = 0,01 m** |
| Tâm instance kiểm tại (3, 0, −6) | Giữ đúng vị trí; sai số < 10⁻¹⁰ m |
| Kiểm kiểu strict + noUncheckedIndexedAccess | **0 lỗi**, 424 tệp phụ thuộc |
| Clip có đối chứng đạt diện tích 90–130%, sáng ≥ cũ | **15/15** |
| Alpha hàng texel cuối, cận trên lớn nhất | **0,000008752**, ≤ 0,1 |
| `fire-impact` xuất hiện | **tick 0**, ≤ 2 tick |

So với báo cáo 422: lửa giữ **532 px**, tỷ lệ **109,24%** so cũ; độ sáng **0,0271803645**. Earth giữ **66 px**, tỷ lệ **115,79%** so cũ; độ sáng tăng **0,003249 → 0,0035421191**. Các số đo 15 clip còn lại không đổi. Hai clip `fire-impact` và `metal-impact` không có đối chứng cũ trong manifest; tỷ lệ vẫn **N/A**, không tính vào 15/15.

Probe trực tiếp bằng `FlipbookPool`, không chạy test suite: 17/17 clip giữ fade đáy sau nhánh main; chỉ 1 clip có gradient, chỉ 1 clip có shader flat; `layFlat` rồi `update(0)` phục hồi hook đúng; capacity/drop, `ONE_FRAME` scrub, options của caller và `?burst=old` không fetch đều đạt. Pháp tuyến và mặt phẳng đo trên matrixWorld của mesh thật sau attach/update.

## Tái đo CPU

Lệnh dưới dùng lại raster đã ghi trong báo cáo 422, bổ sung đúng hình học flat và gradient 422b; không ghi tệp phụ.

```sh
python3 - <<'PY' | node --import ./games/.wt-ic-lab-all/node_modules/tsx/dist/loader.mjs --input-type=module
from pathlib import Path
s = Path('docs/codex-queue/422-report.md').read_text().split('```javascript\n', 1)[1].split('\n```', 1)[0]
s = s.replace('function footprint(meta, ground, size, fade)', 'function footprint(meta, ground, size, fade, flat = false)')
s = s.replace('const world = ground ?', 'const world = flat ? new THREE.Vector3(x, .01, Z - y) : ground ?')
s = s.replace('if (ground) {\n      t =', 'if (flat) { t = (.01 - cy) / dy; wy = .01; u = px + t * rx / (aspect * size); v = py - (cz + t * dz - Z) / size; } else if (ground) {\n      t =')
s = s.replace('fade = false, ticks = false)', 'fade = false, ticks = false, flat = false, gradient = undefined)')
s = s.replace('SIZE * scale, fade)', 'SIZE * scale, fade, flat)')
s = s.replace('let area = 0;', 'let area = 0; let hue = 0, hueLinear = 0;')
s = s.replace('const l = (.2126 * r', """
      if (gradient) {
        const light = (.2126 * r + .7152 * g + .0722 * b) * soft * intensity / Math.max(1e-12, fade ? smooth(0, BURST_BOTTOM_FADE, v) : 1);
        const ramp = gradient[0].map((c,k) => mix(c, gradient[1][k], smooth(0,1,light)));
        const gain = (.2126 * r + .7152 * g + .0722 * b) / (.2126 * ramp[0] + .7152 * ramp[1] + .0722 * ramp[2]);
        [r,g,b] = ramp.map(c => c * gain);
      }
      const l = (.2126 * r""")
s = s.replace('if (l > .15) area++; a.push(l);', """
      if (l > .15) {
        area++;
        const rgb = [r,g,b].map(c => c * soft * intensity);
        function hsv(c) {
          const hi=Math.max(...c),lo=Math.min(...c),d=hi-lo;
          if (d < 1e-9) return 0;
          return ((hi===c[0]?(c[1]-c[2])/d:hi===c[1]?2+(c[2]-c[0])/d:4+(c[0]-c[1])/d)*60+360)%360;
        }
        hueLinear += hsv(rgb);
        hue += hsv(rgb.map(c => { c=Math.max(0,Math.min(1,c)); return c<=.0031308?12.92*c:1.055*c**(1/2.4)-.055; }));
      }
      a.push(l);""")
s = s.replace('peak = { area, bright, frame };', 'peak = { area, bright, frame, hue: hue / area, hueLinear: hueLinear / area };')
s = s.replace('true, !!process.env.TICKS)', 'true, true, row.flat, row.gradient)')
s = s.replace('process.env.TICKS && older', 'older')
print(s)
PY
```

## Phần còn thiếu và owner cần xem

Chưa chụp/đo được GPU trong host: Chrome riêng qua debugging pipe không trả CDP, kết nối `Browser.getVersion` hết thời gian; công cụ trình duyệt có sẵn trả **“The browser access host is unavailable”**. Đã dừng tiến trình probe và dọn profile tạm của mình. Không mở dev server, không tạo capture ngoài phạm vi cho phép.

Các con số trên là kiểm trước bằng CPU, **không thay bằng chứng pixel GPU, KTX2/mipmap, tone mapping/bloom hay nghiệm thu thị giác 8,5**. Owner/coordinator cần xem lại hai clip trong host lab và chạy chụp theo scenario cuối báo cáo 422 khi trình duyệt hoạt động; xác nhận màu cam vàng theo mẫu `fire-impact.v1-try2.sheet.png` và vòng earth nằm theo sân.

