# Phiếu 433b — Kim mưa kiếm, sửa theo phân cảnh

Ngày **17/11/2026**. Đã sửa mã lab và kiểm CPU; **chờ Claude chụp lại, kiểm console và đo p95 toàn khung ≤ 16,7 ms**. Chưa nghiệm thu hình ảnh 8,5.

## Tệp đã ghi

- `games/.wt-ic-lab-all/src/lab/metal-ult-rain.ts`.
- `docs/codex-queue/433b-report.md` — báo cáo này, kèm probe chạy lại được.

Không cần đổi chỗ nối trong `metal-ult-layered.ts`: mặc định vẫn là mưa kiếm, `?metalUlt=ring` vẫn chọn vành cũ. Không ghi đường dẫn khác, không tạo media, không chạy build hoặc bộ test game; không commit, push, đổi nhánh hay thao tác dọn Git. Giữ nguyên sửa đổi của các tác nhân khác. Hạn mức đã được đọc; áp dụng đúng miễn trừ được owner ghi trong phiếu.

## Những gì đã sửa

Theo `VFX_STANDARD`, loại ultimate; dùng lại hình của repo từ `ult-storyboard-samples-431.jpg` làm đối chiếu. Mã chỉ đặt, chuyển động, nhuộm và làm mờ thành phần có sẵn.

| Phần | Bản 433b |
| --- | --- |
| Trận trời | Đường kính cố định **14 m**, cao **10,5 m**; hiện trong **0,3 s**, giữ nguyên tới **2,4 s**, mờ hết ở 3,1 s. Cắt phần đệm đen của ô atlas để nét trận chiếm thẻ; tăng sắc vàng và lõi sáng, RGB đầu ra mỗi lớp chặn **≤ 0,9**. |
| Tia rủ | **20 thẻ dọc** dùng ô blade số 8 của `metal-ult/metal-ult.atlas.png`, dài 3–6 m, chạy nhẹ quanh trận, mờ dần xuống dưới. |
| Kiếm thường | Chiều cao thực theo kế hoạch **2,807–3,451 m**; tăng bề ngang 1,35 lần để rõ hơn từ trên. Vẫn dùng GLB/PBR và texture gốc. |
| Nhịp rơi | Ba nhóm bắt đầu **0,6 / 1,05 / 1,5 s**, 16 kiếm/nhóm, cách nhau **28,125 ms**. Kiểm ở 60 Hz không có khoảng trống từ 0,6 tới trước 2,4 s. |
| Kiếm cuối | Cao **9,2 m**, bắt đầu **2,0 s**, chạm **2,4 s**. |
| Vệt | Mỗi kiếm có vệt vàng **3,029–6 m**, đi từ sau chuôi và mờ dần về đuôi. Cắt đệm ngang của ô blade: trước đây hình chỉ chiếm khoảng 10% bề ngang thẻ, khiến vệt gần như mất. |
| Cắm đất | Mọi kiếm, kể cả kiếm cuối, phát `metal-impact-v2`; thêm sáu tia/glint từ art có sẵn cho mỗi điểm chạm. Tốc độ impact đưa đủ 32 khung vào 1,1 s. |
| Vết nứt | Ô tĩnh số 8 của `metal-ground-mark.atlas.png`, nằm ngang, xoay theo seed; cỡ **2,9 m**, kiếm cuối **9 m**; mỗi vết mờ trong **1,5 s** từ lúc chạm. Không vẽ nứt bằng mã. |
| Cú kết | Giữ `metal-big-burst-v2`, tăng thẻ thành **10 m**, cùng thời điểm host strike và âm hiện có. Lóe/mark không bị thêm thời gian chờ sáng ở đầu. |
| Dư âm | Tăng kho bụi/glint từ **147 lên 441**, tăng kích thước, độ sáng và độ tản; xuất hiện so le từ 2,6 s, về kho hết ở 4 s. |

Giữ nguyên đường sát thương, chọn mục tiêu, số kiếm 49, seed 433 và âm đã nối. Tối đa **272.930 tam giác kiếm**, tám kho thẻ + một draw kiếm; thêm một texture ground-mark. Chi phí GPU phải đo trực tiếp.

## Đã kiểm

`node node_modules/typescript/bin/tsc --noEmit`: **0 lỗi** trên toàn worktree. Probe dùng hình học GLB thật; chỉ thay giải mã ảnh trình duyệt bằng texture CPU rỗng.

| Mục | Kết quả |
| --- | --- |
| Kiếm đang rơi ở 0,8 / 1,2 / 1,6 / 2,0 s | **8 / 17 / 17 / 17**, mọi mốc ≥ 4 |
| Thời gian rơi mỗi kiếm, gồm kiếm cuối | **0,400–0,514 s** |
| Kiếm cuối bắt đầu / chạm | **2,0 / 2,4 s** |
| Va chạm / slot trả ở 4 s | **49 / 49** |
| Kho thẻ, instance kiếm, tam giác kiếm ở 4 s | **0 / 0 / 0**; phép ngừng hoạt động |
| Nạp atlas riêng recipe | **0 lỗi**; năm ảnh atlas và một GLB nạp một lần qua các lượt tung lại |
| Năm vòng tung/xóa, bước 15 Hz, xóa/dispose khi còn nạp | **PASS**, không tạo lại mesh/geometry/material/mảng thuộc tính |
| Kiếm hướng mũi xuống; không có hit giả vào mục tiêu chết | **PASS** |
| Nhánh vành cũ | **PASS** qua probe CPU 100 mục tiêu |
| Lập kế hoạch / p95 cập nhật riêng recipe CPU | Khoảng **0,782 / 0,159 ms** ở lượt đo đầu; không phải thời gian toàn khung |

### Hai atlas từng báo lỗi

Trong nguồn hiện tại, cả `metal-slash-arc` và `metal-crescent-sym` **đều có PNG, JSON và UASTC KTX2**; PNG 4096×2304 đã được ImageMagick đọc thành công. Manifest Kim trỏ tới đúng các tên có trên đĩa. Hai tệp lab được phép sửa không tham chiếu hai id này; recipe chỉ nạp seal, impact-v2, big-burst-v2, ground-mark và atlas metal-ult.

Vì vậy không bỏ atlas hợp lệ hoặc đổi bộ nạp dùng chung ngoài phạm vi phiếu. **Chưa xác nhận 0 lỗi console trên host**: phải tải lại trang, kiểm URL/status chính xác nếu lỗi cũ còn lặp. Nguồn nạp hai atlas đó nằm ở thư viện element dùng chung, ngoài hai tệp được phép.

## Chạy lại kiểm CPU

Tệp checker 433 giữ nguyên và còn kỳ vọng lịch cũ; dùng đoạn dưới để thay kỳ vọng **trong bộ nhớ**, không ghi thêm tệp. Các kiểm GLB, pool, tài nguyên, sát thương và nhánh vành của 433 vẫn chạy.

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
node node_modules/typescript/bin/tsc --noEmit
node --input-type=module <<'NODE'
import { readFileSync } from 'node:fs';
const report = readFileSync('../../docs/codex-queue/433b-report.md', 'utf8');
const code = report.split('<!-- 433b-cpu-probe -->').at(-1).split('```js\n')[1].split('\n```')[0];
await import('data:text/javascript;base64,' + Buffer.from(code).toString('base64'));
NODE
```

<!-- 433b-cpu-probe -->
```js
import { registerHooks } from 'node:module';
import { readFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';
import assert from 'node:assert/strict';
const checker = pathToFileURL(resolve('src/lab/metal-ult-rain-check.mjs')).href;
let probe = readFileSync(new URL(checker), 'utf8');
const replace = (from, to) => {
  assert.ok(probe.includes(from), 'Checker 433 đã đổi: ' + from);
  probe = probe.replaceAll(from, to);
};
replace('assert.equal(imageLoads, 4)', 'assert.equal(imageLoads, 5)');
replace('assert.equal(textures.length, 7)', 'assert.equal(textures.length, 8)');
replace('assert.equal(r.rain.waveCounts[1], 1)', 'assert.equal(r.rain.waveCounts[1], 6)');
replace('[0.6, 1.2, 1.8]', '[0.6, 1.05, 1.5]');
replace('const savedPlan = rain.slots.map(s => ({ ...s }));', `const savedPlan = rain.slots.map(s => ({ ...s }));
  const ordinary = savedPlan.filter(s => s.wave >= 0), giant = savedPlan.at(-1), fallingSamples = [];
  assert.ok(ordinary.every(s => s.length >= 2.2 && s.length <= 3.5));
  assert.ok(giant.length >= 8 && giant.length <= 10);
  assert.ok(savedPlan.every(s => s.impact - s.birth >= 0.35 && s.impact - s.birth <= 0.6));
  assert.ok(savedPlan.every(s => s.trail >= 3 && s.trail <= 6));
  assert.ok(r.rain.sealDiameterM >= 10 && r.rain.sealDiameterM <= 14);
  assert.ok(r.rain.sealHeightM >= 9 && r.rain.sealHeightM <= 12);
  assert.equal(rain.group.children.find(o => o.name === 'fx-metal-rain-seal-rays').geometry.getAttribute('iAt').count, 20);
  assert.equal(rain.group.children.find(o => o.name === 'fx-metal-rain-dust').geometry.getAttribute('iAt').count, 441);`);
replace('for (let wave = 0; wave < 3; wave++)', `if (frame >= 36 && frame < 144) assert.ok(r.rain.fallingSwords > 0, 'Khoảng trống mưa kiếm ở ' + now);
    if ([48, 72, 96, 120].includes(frame)) {
      const falling = rain.slots.filter(s => s.state === 1).length;
      assert.equal(falling, r.rain.fallingSwords); assert.ok(falling >= 4);
      fallingSamples.push({ clock: now, falling });
    }
    for (const [k, s] of rain.slots.entries()) if (s.state === 1) {
      const card = rain.group.children.find(o => o.name === 'fx-metal-rain-trails');
      assert.ok(Math.abs(card.geometry.getAttribute('iSize').getY(k) - s.trail) < 1e-6);
    }
    for (const [k, s] of rain.slots.entries()) if (s.state === 2 && now - s.impact < 1.49) {
      const card = rain.group.children.find(o => o.name === 'fx-metal-rain-ground-marks');
      assert.equal(card.geometry.getAttribute('iClock').getY(k), 1.5);
      assert.ok(Math.abs(card.geometry.getAttribute('iClock').getX(k) - s.impact) < 1e-6);
    }
    for (let wave = 0; wave < 3; wave++)`);
replace('strictErrors: diagnostics.length, waveFrames', `strictErrors: diagnostics.length,
    swordHeightM: [Math.min(...ordinary.map(s => s.length)), Math.max(...ordinary.map(s => s.length))],
    giantHeightM: giant.length, giantBirth: giant.birth, fallingSamples,
    fallDurationS: [Math.min(...savedPlan.map(s => s.impact - s.birth)), Math.max(...savedPlan.map(s => s.impact - s.birth))],
    trailLengthM: [Math.min(...savedPlan.map(s => s.trail)), Math.max(...savedPlan.map(s => s.trail))],
    sealDiameterM: r.rain.sealDiameterM, sealHeightM: r.rain.sealHeightM, atlasLoadErrors: rain.loadError === null ? 0 : 1,
    waveFrames`);
registerHooks({ load(url, context, next) {
  return url === checker ? { format: 'module', shortCircuit: true, source: probe } : next(url, context);
} });
await import(checker);
```

## Lệnh chụp và đo cho Claude

Lượt này không mở server hoặc trình duyệt. Kết nối tới `127.0.0.1:3146` không thành công. Claude dùng host đã phục vụ đúng worktree, đổi `BASE` theo cổng thực tế:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3146/stress.html \
OUT=/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/metal-ult-rain-433b \
ART_MAGICK=/opt/homebrew/bin/magick \
node src/kit/tools/cdp-run.mjs src/lab/metal-ult-rain-review.mjs \
  --width=1920 --height=1080 --dpr=1
```

Giữ nguyên kịch bản 433 theo phạm vi cho phép: chụp hai góc tại 0,4 / 1,2 / 2,4 / 3,2 s; tên tệp vẫn có tiền tố `433-`, thư mục riêng là `433b`. Kịch bản tạo `ABOUT.md` và cập nhật chỉ mục; sửa trường `doc` của ABOUT sang báo cáo này khi Claude chạy. Đo stress 100 quái, cả hai góc, p95 toàn khung có `readPixels` **≤ 16,7 ms**, tài nguyên GPU ổn định qua năm lượt. Xem `433-measure.json`, console và exceptions trước khi nghiệm thu.

**Owner cần xem:** trận vàng và tia rủ ở 0,4 s; kiếm/vệt đang rơi ở 1,2 s; kiếm cuối, tia lửa và vết nứt ở 2,4 s; mật độ bụi ở 3,2 s. So trực tiếp với nửa trái phân cảnh 431. Chưa có ảnh/video mới, số đo GPU, xác nhận console host hoặc chấm mù trong lượt này; các mục đó để Claude thực hiện như phiếu 433.
