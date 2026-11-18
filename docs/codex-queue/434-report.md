# Phiếu 434 — Tuyệt kỹ Lôi dây chuyền, bản lab đầu

Ngày 17/11/2026. **Đã dựng và kiểm CPU; chưa nghiệm thu hình, âm và p95 GPU.**

## Đã làm

- Thêm `games/.wt-ic-lab-all/src/lab/thunder-ult-chain.ts`.
- Chỉ nối trong `games/.wt-ic-lab-all/src/lab/skills-main.ts`: phím 8 và `__lab.showcase("ult-thunder-nine-heavens-v2")`, nạp trước khi chọn, cập nhật, reset, mặt nạ bảo vệ chữ và `__lab.thunderUlt()` để đọc probe.
- `?thunderUlt=old` đi vào runner cũ. Không sửa `showcase.ts`, `clip-skills.ts`, `metal-ult-*` hoặc `ult-camera-punch.ts`; chỉ gọi camera chung.
- Không sửa game chính, sim, test, script hoặc tài liệu game. Không tạo media, đổi nhánh, stage, commit hay chạy build/bộ test game.

Nguồn bố cục: nửa phải `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`, đã xem; dòng Lôi trong `ULT_CHOREOGRAPHY.md`. Theo `VFX_STANDARD`, `game-vfx-production`, `game-vfx-layered` và `game-vfx`. Mesh răng cưa là cách làm được phiếu chỉ định; các hình mây, lóe trúng, cột và dư điện đều tái dùng art, không sinh hình mới.

| Pha | Cách dựng |
|---|---|
| 0–0,6 s | Mây `thunder-five-cloud-ink-wg` trộn thường, tím tối, trôi vào trên đám quái; chớp trong mây; `thunder-charge` tại tay. |
| 0,6–1,9 s | Tối đa 14 quái, mỗi 0,1 s; chọn quái sống chưa trúng gần nhất tại từng bước, bắt đầu từ tay. Tia có 18 đoạn chính và hai nhánh ngắn, giữ 0,15 s rồi mờ 0,12 s. Thân tối đa 0,9/kênh; chỉ lõi rất mảnh HDR. |
| Mỗi lần nhảy | `thunder-impact-v3`, `thunder-sparkle`, shocked/giật tê; dùng đường hit/số sát thương hiện có của lab. |
| 2,0–2,4 s | Một `thunder-pillar-single-narrow` tại quái cuối còn sống; nếu nó chết thì chọn cụm sống đông nhất bán kính 4 m. Đây là atlas cắt từ Thunder Pillar đã có trong lab. `thunder-big-burst`, rung nhẹ và `UltCameraPunch` cùng tâm. |
| 2,4–3,5 s | Ba nhịp dư điện trên tối đa bốn quái, `thunder-five-lingering-arcs-wg`; mây tan. Tất cả instance được trả về pool lúc 3,5 s. |

Âm dùng lại hai take Lôi trong `art-src/lab/firefly-sprint-2026-11-05/sound/`: `tt-sfx-ult-thunder-edict/take1.wav` và `tt-sfx-pillar-thunder/take1.wav`; gain theo `fireflyGain`, fade và nhóm voice có trần của lab. Chưa nghe để kết luận chất lượng phối âm. Không có âm tổng hợp.

## Đã xác minh

Kiểm kiểu bằng TypeScript API, lấy nguyên options của `tsconfig.json`, gốc chương trình là module mới và `skills-main.ts` cùng các dependency: **strict + noUncheckedIndexedAccess, 0 diagnostic**. `git diff --check` trên chỗ nối không lỗi.

Probe Node 24 dùng metadata JSON thật, kiểm sự tồn tại atlas thật, thay riêng TextureLoader bằng texture CPU; **không giả nhận đã upload GPU/render**:

| Phép kiểm | Kết quả |
|---|---|
| 100 mục tiêu ở lưới 10 × 10 | 14 mục tiêu khác nhau, đúng nearest-neighbour ở từng bước; tie chọn slot nhỏ hơn. |
| Thứ tự fixture | `4, 3, 2, 1, 0, 10, 11, 12, 13, 14, 15, 5, 6, 7`. |
| Nhịp | Đầu 0,6 s; cuối 1,9 s; sét lớn 2,0 s; 9 hit trong cụm chót, 12 lần dư điện trong fixture. |
| Pool | Đỉnh 14 đối tượng sống; sau 4 s bằng 0; không drop. |
| Xoá/tung lại 5 vòng | Mỗi vòng xoá ở 2,2 s, rồi tung đủ 4 s: 11 Object3D, 9 geometry, 9 material, 0 instance khi nghỉ; không tăng tài nguyên. |
| Nạp/dispose | 8 atlas chỉ nạp một lần qua các lượt tung; dispose đủ 8 texture; dispose lặp lại an toàn. |
| Camera | Trở đúng vị trí và quaternion sau hoàn tất và khi xoá giữa chừng. |
| Bước thời gian lớn | `update(4)` cho cùng log nhảy như 240 bước 1/60 s; pool sạch. |
| Mục tiêu ít/chết | Quái đầu chết giữa chuỗi được bỏ qua; 3 quái thì đánh 3, không lặp; không quái thì không tạo đòn trúng giả. |
| Asset lỗi/đang tải | Retry chỉ tải mảnh thiếu; dispose trong khi 8 request đang chờ trả đủ 8 texture, không thêm lại scene. |
| Bản cũ | Probe hàm dispatcher thật trích từ `skills-main.ts`: mặc định gọi chain, `old` gọi `castClip8`, không chạy cả hai. |

Lệnh chạy lại strict, không chạy suite/build:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
node --input-type=module <<'JS'
import ts from './node_modules/typescript/lib/typescript.js';
import assert from 'node:assert/strict';
const config = ts.readConfigFile('tsconfig.json', ts.sys.readFile);
assert.equal(config.error, undefined);
const options = ts.parseJsonConfigFileContent(config.config, ts.sys, process.cwd()).options;
const files = ['src/lab/thunder-ult-chain.ts', 'src/lab/skills-main.ts'];
const diagnostics = ts.getPreEmitDiagnostics(ts.createProgram(files, options));
console.log(ts.formatDiagnosticsWithColorAndContext(diagnostics, {
  getCanonicalFileName: x => x, getCurrentDirectory: () => process.cwd(), getNewLine: () => '\n',
}));
assert.equal(diagnostics.length, 0);
console.log('PASS: strict, 0 diagnostic');
JS
```

## Còn cần Claude chạy

**p95 stress 100 quái: NOT MEASURED.** Shell phiên này thấy listener 3146 qua `lsof`, nhưng `curl --max-time 4 -sS http://127.0.0.1:3146/stress.html` trả lỗi 7, không kết nối được. Không khởi động server hoặc tìm đường vượt sandbox. Chưa có capture trình duyệt, video hay điểm 8,5. Cần xem độ rõ tia ở camera chơi, độ che của mây, nguồn cột từ mây xuống và nghe nhịp điện; chưa có điểm ở sáu mục scorecard hoặc hai lượt PASS hình.

Kịch bản dưới dùng host lab **đã chạy đúng worktree**, không build. Khác kịch bản stress cũ: gọi `__lab.showcase` của phiếu 434; **không gọi `__stress.cast()` vì hàm đó tung Ngũ Lôi phím G**. 100 quái trong cảnh stress hiện tại = 87 TargetField + 13 walker tạo tải render; chain nhắm 87 TargetField.

Tạo scenario tạm, chụp đúng 0,4/1,2/2,2/3,0 s ở camera chơi; đo 240 frame toàn khung qua `perf(1)` và quay 120 frame/30 fps. Clip lệnh này chỉ ghi hình; nghe âm trực tiếp trong lab.

```sh
cat > /tmp/typing-game-434-thunder-review.mjs <<'JS'
import { mkdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
export default async function(page) {
  const out = process.env.OUT;
  if (!out) throw new Error('Cần OUT riêng cho lượt chụp này');
  mkdirSync(out, { recursive: true });
  const about = 'purpose: Phiếu 434, sét dây chuyền và sét lớn\nmade-by: Claude chạy scenario trong báo cáo Codex\ndoc: docs/codex-queue/434-report.md\ndelete-when: Owner duyệt xong và không cần đối chiếu\n';
  writeFileSync(join(out, 'ABOUT.md'), about);
  const url = new URL(process.env.BASE || 'http://127.0.0.1:3146/stress.html');
  for (const [k, v] of Object.entries({ fixed: '1', ui: '0', dpr: '1', q: 'high', herd: 'march' })) url.searchParams.set(k, v);
  url.searchParams.delete('auto'); url.searchParams.delete('thunderUlt');
  const ev = async code => {
    const r = await page.eval(code); if (r?.evalError) throw new Error(r.evalError); return r;
  };
  const wait = async code => {
    for (let i = 0; i < 240; i++) { if (await ev(code)) return; await page.sleep(250); }
    throw new Error('Chưa sẵn sàng: ' + code);
  };
  await page.goto(url.href, { settle: 1500 });
  await wait('window.__lab?.ready && window.__stress?.ready');
  await wait('window.__lab.thunderUlt().ready');
  const start = () => ev(`(() => {
    const l = window.__lab; l.reset(); l.setHerd('march'); l.camera('play'); l.viewMode('top'); l.step(45);
    const population = Array.from({ length: 87 }, (_, i) => l.beast(i)).filter(b => b.alive).length
      + window.__stress.report().walkers.instances;
    if (population !== 100) throw new Error('Cảnh chưa đủ 100 quái: ' + population);
    l.showcase('ult-thunder-nine-heavens-v2');
    if (l.thunderUlt().mode !== 'chain' || !l.thunderUlt().active) throw new Error('Host chưa có phiếu 434');
    return population;
  })()`);
  const seek = time => ev(`(() => {
    let r = window.__lab.thunderUlt().last;
    for (let i = 0; i < 1200 && r.clock < ${time} - 1e-8; i++) {
      window.__lab.step(1, Math.min(1/60, ${time} - r.clock)); r = window.__lab.thunderUlt().last;
    }
    if (Math.abs(r.clock - ${time}) > 1e-7) throw new Error('Sai mốc: ' + r.clock);
    return r;
  })()`);
  await start(); await ev('window.__lab.step(240); true'); // Làm ấm shader và atlas.
  await start();
  const phases = [];
  for (const t of [0.4, 1.2, 2.2, 3.0]) {
    phases.push(await seek(t)); await page.shot(join(out, `434-${t.toFixed(1)}s.png`));
  }
  await start();
  const measured = await ev(`(() => {
    const rows = [];
    for (let i = 0; i < 240; i++) {
      const p = window.__lab.perf(1);
      rows.push({ cpu: p.cpu[0], total: p.total[0], draws: p.drawCalls, triangles: p.triangles, gpu: p.gpu });
    }
    return { rows, state: window.__lab.thunderUlt(), memory: window.__lab.memory() };
  })()`);
  const sorted = measured.rows.map(r => r.total).sort((a, b) => a - b);
  const p95 = sorted[Math.ceil(sorted.length * 0.95) - 1];
  const result = { url: url.href, viewport: [page.width, page.height], dpr: 1, population: 100,
    p95TotalMs: p95, gateMs: 16.7, pass: p95 <= 16.7, phases, measured,
    note: 'total = CPU + chờ GPU qua readPixels; không phải khoảng rAF. Chưa chấm hình/âm.' };
  writeFileSync(join(out, '434-stress.json'), JSON.stringify(result, null, 2));
  if (measured.state.active || measured.state.live !== 0) throw new Error('Pool chưa sạch sau 4 s');
  const frames = join(out, 'frames'); mkdirSync(frames, { recursive: true });
  writeFileSync(join(frames, 'ABOUT.md'), about);
  await start();
  for (let f = 0; f < 120; f++) {
    await ev('window.__lab.step(2); true');
    const shot = await page.send('Page.captureScreenshot', { format: 'jpeg', quality: 90 });
    writeFileSync(join(frames, `f${String(f).padStart(4, '0')}.jpg`), Buffer.from(shot.data, 'base64'));
  }
  // Kiểm fallback trên cùng host, sau khi đã thu đủ capture của chain.
  url.searchParams.set('thunderUlt', 'old'); await page.goto(url.href, { settle: 1500 });
  await wait('window.__lab?.ready');
  await ev(`(() => {
    const l = window.__lab; l.showcase('ult-thunder-nine-heavens-v2');
    if (l.thunderUlt().mode !== 'old' || l.thunderUlt().active || l.clipSkill()?.id !== 'ult-thunder-nine-heavens-v2')
      throw new Error('Fallback cũ sai'); return true;
  })()`);
  return { out, p95TotalMs: p95, pass: result.pass, oldFallback: true };
}
JS

export TG_ROOT=/Volumes/SS990TPRO/htdocs/typing-game
export REVIEW_ROOT=/Volumes/SS990TPRO/htdocs/typing-game-review
export RUN_DAY=$(date +%Y-%m-%d)
export RUN_ID=$(date +%H%M%S)
export OUT="$REVIEW_ROOT/captures/tu-tien/434-thunder-chain-$RUN_ID"
export BASE=http://127.0.0.1:3146/stress.html
cd "$TG_ROOT/games/.wt-ic-lab-all"
"$TG_ROOT/.local/bin/heavy.sh" --gpu node src/kit/tools/cdp-run.mjs /tmp/typing-game-434-thunder-review.mjs --width=1920 --height=1080 --dpr=1
ffmpeg -y -framerate 30 -i "$OUT/frames/f%04d.jpg" -t 4 -c:v libx264 -pix_fmt yuv420p -crf 18 "$OUT/434-thunder-chain-4s.mp4"
/opt/homebrew/bin/magick montage -font /System/Library/Fonts/Supplemental/Arial.ttf -pointsize 22 -fill white -background '#11151c' -label '0.4 s' "$OUT/434-0.4s.png" -label '1.2 s' "$OUT/434-1.2s.png" -label '2.2 s' "$OUT/434-2.2s.png" -label '3.0 s' "$OUT/434-3.0s.png" -tile 2x2 -geometry 960x540+4+4 "$OUT/434-phases.jpg"
export OWNER_OUT="$REVIEW_ROOT/owner-review/$RUN_DAY/tu-tien/434-thunder-chain-$RUN_ID"
mkdir -p "$OWNER_OUT"
cp "$OUT/ABOUT.md" "$OWNER_OUT/ABOUT.md"
ln "$OUT/434-thunder-chain-4s.mp4" "$OUT/434-phases.jpg" "$OUT/434-stress.json" "$OWNER_OUT/"
cd "$TG_ROOT"
node tools/capture-prune/prune.mjs "$OUT/frames" --min-age-min 0
node tools/capture-prune/prune.mjs "$OUT/frames" --min-age-min 0 --apply
node scripts/review-index.mjs
```

Chỉ báo đạt cổng p95 khi `434-stress.json` có `pass: true`, GPU thật, đúng độ phân giải/settings và không có lỗi shader/asset trong log runner. Sau đó Claude xem sheet/clip, nghe âm và gửi owner; chưa gán điểm hình hoặc PASS 8,5 từ kết quả CPU này.
