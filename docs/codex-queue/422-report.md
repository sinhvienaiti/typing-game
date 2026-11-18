# Phiếu 422 — hiệu chỉnh burst v2 trong lab

Ngày 16/11/2026. **Đã sửa mã và kiểm CPU; chưa xác nhận nghiệm thu GPU trong lab.** Kiểm kiểu strict: **0 lỗi**. Raster CPU ở 1280×720: **15/15 clip có đối chứng đạt diện tích 90–130% và độ sáng đỉnh ≥ cũ**; `fire-impact` hiện ở **tick 0** sau khi bỏ 8 ô đầu. Hai khóa `fire-impact`, `metal-impact` không có nguồn cũ trong manifest, nên tỷ lệ là **N/A**, không lấy clip khác thay đối chứng.

## Tệp đã sửa và cách sửa

- `games/.wt-ic-lab-all/src/lab/burst-v2.ts`: bảng scale/intensity riêng cho 17 clip, nhân với tham số caller; fade mềm 15% đáy ở đầu ra premultiplied của shader; đọc `start` từ JSON và tính life bằng `(frames − start) / fps`.
- `games/.wt-ic-lab-all/art-src/lab/vfx/fire/fire-impact-v2.json`: `start: 8`, ghi rõ lý do; giữ nguyên atlas 32 ô, bảng `trim.indices` và 10 ô fade đuôi đã bake. `art-src` của worktree là symlink tới art dùng chung; chỉ sửa JSON này.
- `docs/codex-queue/422-report.md`: báo cáo và script tái đo/chụp.

Fade được nhân sau `vxTagMain`, nên tác dụng lên cả RGB additive có alpha 0 và RGBA có nhánh return/sharpen. Ở mép hình học `vUv.y = 0`, cả màu và alpha bằng 0. Cận trên alpha tại tâm hàng texel cuối của ô RGBA 256 px là **0,000008752**, nhỏ hơn 0,1; RGB additive có alpha đầu ra 0. Hook được phục hồi nếu caller gọi `layFlat` sau attach. Không fade đuôi lần hai.

`fire-impact` không có đoạn đen tuyệt đối trong atlas: ô 0 vẫn có một đốm sáng rất nhỏ. Sau chiếu và soft-ground ở cỡ 4 m, intensity 2, ô 8 là ô đầu có pixel luma tuyến tính > 0,15. Bỏ 8 ô đầu rút đoạn phát từ 2,667 s còn **2 s**; vẫn phát hết ô 31. Scrub `ONE_FRAME` giữ khả năng chọn ô tùy ý.

## Số đo đã chạy

Kết quả dưới là quét **từng tick 60 Hz**, tính lại đỉnh riêng cho hai bản. Độ sáng là trung bình 1% pixel sáng nhất của **toàn khung 1280×720**, không phải 1% riêng trong vùng hiệu ứng.

| Clip | Scale | Intensity | Pixel cũ → mới | Diện tích mới/cũ | Sáng cũ → mới |
| --- | ---: | ---: | ---: | ---: | ---: |
| fire-impact | 1 | 2 | N/A → 102 | N/A | N/A → 0,004931 |
| fire-big-burst | 1,687 | 1 | 487 → 532 | 109,24% | 0,024547 → 0,027180 |
| earth-ring-burst | 0,248 | 1,543 | 57 → 66 | 115,79% | 0,003138 → 0,003249 |
| metal-impact | 1 | 2 | N/A → 109 | N/A | N/A → 0,005754 |
| metal-big-burst | 1,615 | 1 | 520 → 642 | 123,46% | 0,023704 → 0,031366 |
| void-big-burst | 2,036 | 1 | 256 → 264 | 103,13% | 0,014470 → 0,016796 |
| wind-ring-burst | 0,773 | 1,323 | 724 → 776 | 107,18% | 0,039741 → 0,043571 |
| dark-ring-burst | 0,498 | 1,15 | 88 → 96 | 109,09% | 0,003960 → 0,004576 |
| water-ring-burst | 0,987 | 1,983 | 540 → 604 | 111,85% | 0,033598 → 0,035048 |
| poison-big-burst | 1,087 | 1 | 420 → 471 | 112,14% | 0,018212 → 0,025336 |
| poison-ring-burst | 1,127 | 1 | 513 → 573 | 111,70% | 0,023853 → 0,025986 |
| blood-big-burst | 0,401 | 8,871 | 114 → 136 | 119,30% | 0,009969 → 0,010566 |
| wood-big-burst | 0,505 | 1,15 | 276 → 281 | 101,81% | 0,013537 → 0,014561 |
| dark-big-burst-white | 1,246 | 3,068 | 3.233 → 3.564 | 110,24% | 0,339239 → 0,390067 |
| dark-ground-impact-white | 1,421 | 5,534 | 2.979 → 3.284 | 110,24% | 0,297297 → 0,327391 |
| thunder-impact | 0,585 | 1,15 | 210 → 235 | 111,90% | 0,011729 → 0,011745 |
| star-ring-burst | 0,819 | 1,15 | 409 → 439 | 107,33% | 0,021071 → 0,022300 |

Hai impact mới có intensity 2 để tăng độ rõ; chưa có tiêu chí tỷ lệ với bản cũ để nghiệm thu chúng. Không gọi 17/17 đạt tỷ lệ.

Kiểm thêm bằng luồng `FlipbookLibrary`/`FlipbookPool` thật của phiếu 421, điều chỉnh assertion cho scale/intensity/start mới: **17 JSON, 17 PNG, 17 đường KTX2 tồn tại, mỗi JSON chỉ nạp một lần, 0 cảnh báo/404**; giữ `?burst=old`, capacity/drop, tail, không sửa object options của caller, scrub và lưới 17 ô. Kiểm shader cả 17 clip có phép fade đáy sau lớp tag mask. `strict` và `noUncheckedIndexedAccess` bật, 425 tệp phụ thuộc, 0 chẩn đoán; không chạy build hay test suite game.

**Giới hạn:** CPU dùng pool đo độc lập, thông số mặc định (soft-ground 0,8 m, không vignette/sharpen), không mô phỏng mipmap, nén KTX2, hậu kỳ hoặc các thiết lập mà kit ghi thêm vào pool trong lab. Do đó bảng này là kết quả kiểm trước, chưa phải bằng chứng pixel GPU trong host. Không thể khẳng định sọc đã hết về thị giác hoặc nghiệm thu 8,5 từ mã. Đã thử khởi động Chrome đo riêng qua pipe, tiến trình kết thúc trước khi trả CDP; không mở được phép đo GPU. Không khởi động dev server; đã xóa profile tạm do lần thử đó tạo.

## Script đo CPU

Script đọc atlas bằng ImageMagick, giải mã sRGB sang tuyến tính, lấy mẫu song tuyến tính và chiếu từng pixel ở camera chơi thật (`fitCamera`, 55°, FOV 28°, 1280×720, không inset, vị trí 0/0/−6, cỡ caller 4 m). Nền đen; luma Rec.709 tuyến tính trước hậu kỳ; diện tích là số pixel luma > 0,15. Khung đỉnh là khung có diện tích lớn nhất; độ sáng là tổng 1% pixel sáng nhất toàn ảnh chia 9.216, gồm cả pixel đen nếu hiệu ứng nhỏ. Quét khung nguồn, kiểm thêm các tick 60 Hz ở bước xác minh cuối. Đây là raster CPU kiểm tra trước, không thay nghiệm thu GPU trong host có mipmap/KTX2/bloom/tone mapping.

Chạy tại gốc repo; không tạo file phụ. Thêm `TICKS=1` trước `node` để tái hiện đúng bảng trên (mặc định chỉ quét các ô nguồn):

```sh
python3 - <<'PY' | node --import ./games/.wt-ic-lab-all/node_modules/tsx/dist/loader.mjs --input-type=module
from pathlib import Path
s=Path('docs/codex-queue/422-report.md').read_text()
print(s.split('```javascript\n',1)[1].split('\n```',1)[0])
PY
```

```javascript
import { readFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
const root = '/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all/';
const THREE = await import(root + 'node_modules/three/build/three.module.js');
const { BURST_V2, BURST_BOTTOM_FADE } = await import(root + 'src/lab/burst-v2.ts');
const { fitCamera } = await import(root + 'src/view/renderer.ts');
const W = 1280, H = 720, TOP = Math.ceil(W * H * .01), SIZE = 4, Z = -6;
const camera = new THREE.PerspectiveCamera(28, W / H, 1, 400);
const fit = fitCamera(camera, W / H);
console.log(JSON.stringify({ camera: fit, position: camera.position.toArray(), width: W, height: H, size: SIZE, z: Z }));
const sin = Math.sin(55 * Math.PI / 180), cos = Math.cos(55 * Math.PI / 180);
const tan = Math.tan(14 * Math.PI / 180), cy = camera.position.y, cz = camera.position.z;
const length = Math.hypot(cy, cz - Z), gc = (cz - Z) / length, gs = cy / length;
const smooth = (a, b, v) => { const x = Math.max(0, Math.min(1, (v - a) / (b - a))); return x * x * (3 - 2 * x); };
const linear = Array.from({ length: 256 }, (_, x) => { x /= 255; return x <= .04045 ? x / 12.92 : ((x + .055) / 1.055) ** 2.4; });
const fract = x => x - Math.floor(x), mix = (a, b, x) => a + (b - a) * x;
const hash = (x, y) => fract(Math.sin(x * 127.1 + y * 311.7) * 43758.5453);
const noise = (x, y) => { const a = Math.floor(x), b = Math.floor(y), u = smooth(0, 1, fract(x)), v = smooth(0, 1, fract(y)); return mix(mix(hash(a, b), hash(a + 1, b), u), mix(hash(a, b + 1), hash(a + 1, b + 1), u), v); };
function atlas(folder, meta, file) {
  const cell = typeof meta.cell === 'number' ? [meta.cell, meta.cell] : meta.cell;
  const [cw, ch] = cell, aw = cw * meta.cols;
  const rgba = execFileSync('/opt/homebrew/bin/magick', [folder + file, '-depth', '8', 'rgba:-'], { maxBuffer: 100 * 1024 ** 2 });
  const frames = Array.from({ length: meta.frames }, (_, f) => {
    const p = new Float32Array(cw * ch * 4);
    for (let y = 0; y < ch; y++) for (let x = 0; x < cw; x++) {
      const src = ((Math.floor(f / meta.cols) * ch + y) * aw + f % meta.cols * cw + x) * 4, dst = (y * cw + x) * 4;
      for (let k = 0; k < 3; k++) p[dst + k] = linear[rgba[src + k]];
      p[dst + 3] = rgba[src + 3] / 255;
    }
    return p;
  });
  return { ...meta, cw, ch, pixels: frames };
}
function sample(meta, frame, u, v, out) {
  u = Math.max(.004, Math.min(.996, u)); v = Math.max(.004, Math.min(.996, v));
  const x = u * meta.cw - .5, y = (1 - v) * meta.ch - .5;
  const x0 = Math.floor(x), y0 = Math.floor(y), a = x - x0, b = y - y0, f = meta.pixels[frame];
  for (let k = 0; k < 4; k++) out[k] = mix(mix(f[(y0 * meta.cw + x0) * 4 + k], f[(y0 * meta.cw + x0 + 1) * 4 + k], a), mix(f[((y0 + 1) * meta.cw + x0) * 4 + k], f[((y0 + 1) * meta.cw + x0 + 1) * 4 + k], a), b);
}
function footprint(meta, ground, size, fade) {
  const points = [], aspect = meta.cw / meta.ch, px = meta.pivot[0], py = 1 - meta.pivot[1];
  const projected = [];
  for (const u of [0, 1]) for (const v of [0, py, 1]) {
    const x = (u - px) * aspect * size, y = (v - py) * size;
    const world = ground ? new THREE.Vector3(x, Math.max(y, 0) / gc, Z - Math.min(y, 0) / gs) : new THREE.Vector3(x, y * cos, Z - y * sin);
    world.project(camera); projected.push([(world.x + 1) * W / 2, (1 - world.y) * H / 2]);
  }
  const x0 = Math.max(0, Math.floor(Math.min(...projected.map(p => p[0])))), x1 = Math.min(W - 1, Math.ceil(Math.max(...projected.map(p => p[0]))));
  const y0 = Math.max(0, Math.floor(Math.min(...projected.map(p => p[1])))), y1 = Math.min(H - 1, Math.ceil(Math.max(...projected.map(p => p[1]))));
  for (let y = y0; y <= y1; y++) for (let x = x0; x <= x1; x++) {
    const rx = ((x + .5) / W * 2 - 1) * tan * W / H, ry = (1 - (y + .5) / H * 2) * tan;
    const dy = ry * cos - sin, dz = -ry * sin - cos;
    let t, u, v, wy;
    if (ground) {
      t = (Z - cz) / dz; wy = cy + t * dy; u = px + t * rx / (aspect * size); v = py + wy * gc / size;
      if (v < py) { t = -cy / dy; wy = 0; u = px + t * rx / (aspect * size); v = py - (cz + t * dz - Z) * gs / size; }
    } else {
      t = (cy * sin + (cz - Z) * cos) / -(dy * sin + dz * cos); wy = cy + t * dy;
      u = px + t * rx / (aspect * size); v = py + (wy * cos - (cz + t * dz - Z) * sin) / size;
    }
    if (u < 0 || u > 1 || v < 0 || v > 1) continue;
    const border = smooth(0, .025, Math.min(u, 1 - u, v, 1 - v));
    const down = Math.max(.12, -dy / Math.hypot(rx, dy, dz));
    const soft = ground ? 1 : smooth(0, .8, wy / down);
    const bottom = fade ? smooth(0, BURST_BOTTOM_FADE, v) : 1;
    points.push([u, v, border * soft * bottom]);
  }
  return points;
}
function scan(meta, ground, scale = 1, intensity = 1, fade = false, ticks = false) {
  const points = footprint(meta, ground, SIZE * scale, fade), a = [], c0 = [], c1 = [];
  let peak = { area: -1, bright: 0, frame: 0 }, first = null;
  const start = meta.start ?? 0, end = meta.frames - 1;
  const times = ticks ? Array.from({ length: Math.ceil((meta.frames - start) / meta.fps * 60) }, (_, t) => start + t / 60 * meta.fps) : Array.from({ length: meta.frames - start }, (_, i) => start + i);
  for (const frame of times) {
    a.length = 0; let area = 0; const f0 = Math.min(end, Math.floor(frame)), f1 = Math.min(end, f0 + 1), w = Math.min(1, frame - f0);
    for (const [u, v, soft] of points) {
      sample(meta, f0, u, v, c0); sample(meta, f1, u, v, c1);
      let r, g, b;
      if (meta.mode === 'smoke') {
        const lum = Math.max(...c0.slice(0, 3).map((c, k) => mix(c, c1[k], w))), ta = mix(c0[3], c1[3], w);
        const d = ta < .999 ? ta : Math.sqrt(lum), n = noise(u * 6, v * 6) * .65 + noise(u * 15, v * 15) * .35;
        const alpha = smooth(.05, .5, d + (n - .5) * .25) * smooth(-.14, .1, n * .6 + d * .55);
        r = g = b = mix(.95, 1.4, smooth(.25, .95, v)) * alpha;
      } else if (meta.channels === 'rgba' || meta.mode === 'rgba') {
        r = mix(c0[0] * c0[3], c1[0] * c1[3], w); g = mix(c0[1] * c0[3], c1[1] * c1[3], w); b = mix(c0[2] * c0[3], c1[2] * c1[3], w);
      } else { r = mix(c0[0], c1[0], w); g = mix(c0[1], c1[1], w); b = mix(c0[2], c1[2], w); }
      const l = (.2126 * r + .7152 * g + .0722 * b) * soft * intensity;
      if (l > .15) area++; a.push(l);
    }
    if (area > 0 && first === null) first = (frame - start) / meta.fps * 60;
    if (area >= peak.area) {
      a.sort((x, y) => y - x); const bright = a.slice(0, TOP).reduce((s, v) => s + v, 0) / TOP;
      if (area > peak.area || bright > peak.bright) peak = { area, bright, frame };
    }
  }
  return { ...peak, firstTick: first };
}
const results = [];
for (const row of BURST_V2) {
  const folder = root + 'art-src/lab/vfx/' + row.id.split('-')[0] + '/';
  const json = JSON.parse(readFileSync(folder + row.id + '-v2.json'));
  const m = JSON.parse(readFileSync(folder + 'manifest.json')).flipbooks[row.key];
  const newer = atlas(folder, json, json.image), older = m ? atlas(folder, m, m.file) : null;
  const old = older ? scan(older, false) : null;
  let scale = row.scale, intensity = row.intensity;
  if (process.env.CALIBRATE && old) {
    for (let i = 0; i < 8; i++) {
      for (let j = 0; j < 5; j++) {
        const n = scan(newer, row.ground, scale, intensity, true);
        scale *= Math.max(.5, Math.min(2, Math.sqrt(old.area * 1.1 / Math.max(1, n.area))));
        scale = Math.max(.1, Math.min(4, scale));
      }
      const n = scan(newer, row.ground, scale, intensity, true);
      if (n.bright >= old.bright * 1.04) break;
      intensity *= Math.min(1.7, Math.max(1.15, old.bright * 1.06 / Math.max(1e-9, n.bright)));
    }
    scale = Math.ceil(scale * 1000) / 1000; intensity = Math.ceil(intensity * 1000) / 1000;
  }
  const newerStats = scan(newer, row.ground, scale, intensity, true, !!process.env.TICKS);
  const oldStats = process.env.TICKS && older ? scan(older, false, 1, 1, false, true) : old;
  const bottomAlpha = json.channels === 'rgba' ? smooth(0, BURST_BOTTOM_FADE, .5 / newer.ch) * smooth(0, .025, .5 / newer.ch) : 0;
  const ratio = oldStats ? newerStats.area / oldStats.area : null;
  const result = { id: row.id, scale, intensity, old: oldStats, newer: newerStats, ratio, bottomAlpha, pass: ratio === null ? null : ratio >= .9 && ratio <= 1.3 && newerStats.bright >= oldStats.bright };
  results.push(result); console.log(JSON.stringify(result));
}
if (!process.env.CALIBRATE && results.some(r => r.pass === false || r.bottomAlpha > .1 || r.id === 'fire-impact' && !(r.newer.firstTick <= 2))) process.exitCode = 1;
```

## Lệnh chụp lưới cũ | mới cho Claude

Dùng host của **worktree `games/.wt-ic-lab-all`** đã được Claude mở, không dùng host game chính. Lệnh trích lại scenario từ báo cáo 421, đổi tên, tăng các mốc cuối để thấy cả đỉnh smoke cũ 6 fps. Chụp **1280×720, DPR 1**, camera chơi 55°. Hai ô impact ở nửa cũ trống là đúng dữ liệu.

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game
python3 - <<'PY'
from pathlib import Path
s = Path('docs/codex-queue/421-report.md').read_text()
scenario = s.split("cat > /private/tmp/421-burst-capture.mjs <<'JS'\n", 1)[1].split('\nJS\n', 1)[0]
scenario = scenario.replace('phiếu 421', 'phiếu 422').replace('421-report.md', '422-report.md')
scenario = scenario.replace('[0, 6, 12, 24, 48, 72, 96, 120, 144, 160]', '[0, 2, 6, 12, 24, 48, 72, 96, 120, 144, 160, 192, 216, 240, 288, 320]')
Path('/private/tmp/422-burst-capture.mjs').write_text(scenario + '\n')
PY

cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3068/skills-lab.html \
OUT_DIR=/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/burst-v2-422 \
/Volumes/SS990TPRO/htdocs/typing-game/.local/bin/heavy.sh --gpu \
node src/kit/tools/cdp-run.mjs /private/tmp/422-burst-capture.mjs --width=1280 --height=720 --dpr=1

cd /Volumes/SS990TPRO/htdocs/typing-game
BURST_OUT=/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/burst-v2-422
for tick in 000 002 006 012 024 048 072 096 120 144 160 192 216 240 288 320; do
  /opt/homebrew/bin/magick "$BURST_OUT/old-$tick.jpg" "$BURST_OUT/v2-$tick.jpg" +append "$BURST_OUT/old-v2-$tick.jpg"
done
node scripts/review-index.mjs
```

Scenario tự tạo `ABOUT.md` và JSON chú giải 17 ô; cũ luôn bên trái. Đây là ảnh kiểm thị giác trên sân lab, **không dùng ảnh JPEG có nền sân để tính chỉ tiêu luma trên nền đen**. Đo GPU nghiệm thu cần tách hiệu ứng trên nền đen, giữ cùng camera/cỡ, quét đủ từng tick và đo riêng đỉnh hai bản theo định nghĩa đầu báo cáo. Đặc biệt kiểm lại các pool mà kit sửa softM/vignette/sharpen/layFlat, cùng đường KTX2 đang dùng; không suy từ bảng CPU rằng chúng đã đạt.

## Bỏ qua và phần owner cần xem

- **Giữ cho 422b:** màu `fire-big-burst` và hướng `earth-ring-burst`; không đổi hướng thẻ hay tông màu nguồn trong phiếu này.
- **Chưa chạy được:** phép đo GPU, chụp lưới và nhận xét thị giác về sọc đáy; các lệnh ở trên để Claude chạy tại host lab. Hai impact thiếu đối chứng nên không thể báo tỷ lệ 90–130% cho chúng.
- Owner cần xem fire/void có đủ lực, water có giữ được vòng lớn, bốn mép chạm đất có hết sọc, và `fire-impact` có hiện đúng lúc. Kiểm riêng Huyết và hai smoke trắng vì hệ số intensity cao có thể tạo cảm giác khác sau tone mapping/bloom. Các hệ số giảm diện tích, nhất là Thổ, cũng cần nhìn lại trong pool thực của kit trước khi chốt.

Không tạo ảnh/âm thanh mới; không sửa atlas, manifest chung, game chính, `src/view`, `skills-main`, `anim-*`, `*-ult-*`, các tệp của tác nhân khác hay bảng việc. Không build/test suite, đổi nhánh, stage, commit, push, reset, clean hoặc stash. Làm một luồng; quota lúc nhận phiếu còn **22%**, trên ngưỡng 15%.
