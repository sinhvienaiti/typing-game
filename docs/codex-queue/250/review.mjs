import fs from 'node:fs';
import {im, D, json} from './lib.mjs';

const records = JSON.parse(fs.readFileSync(`${D}/processed.json`));
const jobs = JSON.parse(fs.readFileSync(`${D}/jobs.json`));
const font = '/System/Library/Fonts/Supplemental/Arial.ttf';

const panels = {
  'dragon-hold': 'games/dragon-hold/art-src/ui/frames/panel-large.png',
  'typing-defense': 'games/typing-defense/art-src/ui/frames-epic/panel-large.v2.png',
  'typing-survival': 'games/typing-survival/art-src/ui/frames-epic/panel-large.png'
};

const titles = {
  'dragon-hold': 'Dragonhold',
  'typing-defense': 'Wordwoven',
  'typing-survival': 'Last Line'
};

const img = (p, w, h = w) => ['(', p, '-filter', 'Lanczos', '-resize', `${w}x${h}!`, ')'];
const put = (a, x, y) => [...a, '-geometry', `+${x}+${y}`, '-composite'];
const txt = (s, x, y, size = 16, color = '#f0e6cc') => [
  '-font', font, '-pointsize', String(size), '-fill', color, '-annotate', `+${x}+${y}`, s
];

const cropPanel = (g, w, h) => {
  const a = ['(', '-size', `${w}x${h}`, 'xc:none'];
  for (let x = 0; x < w; x += 400) {
    const ww = Math.min(400, w - x);
    a.push('(', panels[g], '-crop', `${ww}x${h}+200+200`, '+repage', ')', '-geometry', `+${x}+0`, '-composite');
  }
  a.push(')');
  return a;
};

function save(args, p) {
  fs.writeFileSync(p, im([...args, '-quality', '94', 'jpg:-']));
  console.log(`Saved review image: ${p}`);
}

function getIconPath(g, n) {
  const r = records.find(rec => rec.game === g && (rec.name === n || rec.baseName === n));
  if (r) {
    const job = jobs.find(j => j.id === r.id);
    return `${job.selectedDir}/${r.name}.png`;
  }
  const checkPaths = [
    `games/${g}/art-src/ui/quick-settings/selected/${n}.png`,
    `games/${g}/art-src/ui/quick-settings/${n}.png`,
    `games/${g}/art-src/ui/icons/${n}.png`
  ];
  for (const p of checkPaths) {
    if (fs.existsSync(p)) return p;
  }
  return checkPaths[0];
}

function makeSpecimen(g, n, label, size, width = 280) {
  const h = size + 16;
  const a = [
    '-size', `${width}x${h}`, 'xc:none',
    ...put(cropPanel(g, width, h), 0, 0),
    ...put(img(getIconPath(g, n), size), 8, 8),
    ...txt(label, size + 16, Math.round(size * 0.72) + 8, Math.max(11, Math.round(size * 0.55)))
  ];
  return im([...a, 'png:-']);
}

// 1. Dragonhold Review Sheet
{
  const g = 'dragon-hold';
  const rs = records.filter(r => r.game === g);
  const colWidth = 260;
  const sheetWidth = rs.length * colWidth + 40;
  const sheetHeight = 880;

  let a = [
    '-size', `${sheetWidth}x${sheetHeight}`, 'xc:#121418',
    ...txt('Dragonhold · Phiếu 250 · Quick-Panel Icons — Kiểm tra cỡ thật 1× và so sánh', 20, 30, 20)
  ];

  for (let i = 0; i < rs.length; i++) {
    const r = rs[i];
    const x = 20 + i * colWidth;
    const s720 = r.size720;
    const s1080 = r.size1080;

    a.push(
      ...put(img(r.outputs.find(o => o.size[0] === 256).file, 220), x + 10, 50),
      ...txt(r.name, x + 10, 290, 15, '#ffd277'),
      ...txt(r.label, x + 10, 310, 13, '#c8cdd4')
    );

    const spec1080 = makeSpecimen(g, r.name, `${r.label} (1080p)`, s1080, 240);
    const f1080 = `games/${g}/art-src/_review/250/${r.name}.1080p.png`;
    fs.writeFileSync(f1080, spec1080);
    a.push(
      ...put(['(', f1080, ')'], x, 335),
      ...txt(`1080p · ${s1080}px · 1×`, x + 5, 330, 11, '#8fa0b5')
    );

    const spec720 = makeSpecimen(g, r.name, `${r.label} (720p)`, s720, 240);
    const f720 = `games/${g}/art-src/_review/250/${r.name}.720p.png`;
    fs.writeFileSync(f720, spec720);
    a.push(
      ...put(['(', f720, ')'], x, 400),
      ...txt(`720p · ${s720}px · 1×`, x + 5, 395, 11, '#8fa0b5')
    );

    a.push(
      ...put(cropPanel(g, 120, 120), x + 5, 455),
      ...put(['(', r.outputs.find(o => o.size[0] === 1024).file, '-filter', 'Lanczos', '-resize', `${s720}x${s720}!`, '-filter', 'point', '-resize', '400%', ')'], x + 12, 465),
      ...txt('720p ×4 (point)', x + 120, 500, 12, '#8fa0b5')
    );

    a.push(...put(cropPanel(g, 240, 48), x, 600));
    const compIcons = ['vol-master', 'vol-music', 'vol-keyboard.r3', 'vol-keyboard-volume.r2'];
    for (let c = 0; c < compIcons.length; c++) {
      const cPath = getIconPath(g, compIcons[c]);
      if (fs.existsSync(cPath)) {
        a.push(...put(img(cPath, 24), x + 12 + c * 58, 612));
      }
    }
    a.push(...txt('Cặp so sánh trong bảng (24px)', x + 5, 665, 11, '#8fa0b5'));

    a.push(...put(cropPanel(g, 240, 48), x, 690));
    const oldPath = `games/${g}/art-src/ui/quick-settings/selected/${r.baseName}.png`;
    if (fs.existsSync(oldPath)) {
      a.push(
        ...put(img(oldPath, s720), x + 30, 702),
        ...txt('Cũ', x + 35, 750, 12, '#e06060')
      );
    } else {
      a.push(...txt('(Mới)', x + 25, 715, 12, '#888888'));
    }
    a.push(
      ...put(img(r.outputs.find(o => o.size[0] === 1024).file, s720), x + 140, 702),
      ...txt('Mới (r2/r3)', x + 130, 750, 12, '#60e060')
    );
  }

  save(a, `games/${g}/art-src/_review/250-sheet.jpg`);
  save(a, `${D}/250-sheet-dragonhold.jpg`);

  // Dragonhold Vertical Panels Mockup
  let pMock = [
    '-size', '960x650', 'xc:#121418',
    ...txt('Dragonhold · Bảng Sound & Settings đầy đủ ở 720p 1× (Panel thật)', 20, 30, 18)
  ];
  pMock.push(...txt('Bảng Âm thanh (Sound)', 30, 65, 15, '#ffd277'));
  const dhSoundRows = [
    ['vol-master', 'Master Volume'],
    ['vol-music', 'Music'],
    ['vol-effects', 'Effects'],
    ['vol-keyboard.r3', 'Keyboard Sound'],
    ['vol-keyboard-volume.r2', 'Keyboard Volume'],
    ['vol-voice', 'Voice'],
    ['vol-interface', 'Interface']
  ];
  for (let r = 0; r < dhSoundRows.length; r++) {
    const [name, lbl] = dhSoundRows[r];
    const y = 80 + r * 42;
    pMock.push(
      ...put(cropPanel(g, 380, 38), 30, y),
      ...put(img(getIconPath(g, name), 24), 40, y + 7),
      ...txt(lbl, 74, y + 25, 14, '#e6decb')
    );
  }

  pMock.push(...txt('Bảng Cài đặt (Settings)', 500, 65, 15, '#ffd277'));
  const dhSettingsRows = [
    ['gfx-quality', 'Quality'],
    ['gfx-motion', 'Reduced Motion'],
    ['learn-meaning', 'Vietnamese Meaning'],
    ['learn-ipa', 'Pronunciation (IPA)']
  ];
  for (let r = 0; r < dhSettingsRows.length; r++) {
    const [name, lbl] = dhSettingsRows[r];
    const y = 80 + r * 42;
    pMock.push(
      ...put(cropPanel(g, 380, 38), 500, y),
      ...put(img(getIconPath(g, name), 24), 510, y + 7),
      ...txt(lbl, 544, y + 25, 14, '#e6decb')
    );
  }
  save(pMock, `games/${g}/art-src/_review/250-panels.jpg`);
  save(pMock, `${D}/250-panels-dragonhold.jpg`);
}

// 2. Wordwoven Review Sheet
{
  const g = 'typing-defense';
  const rs = records.filter(r => r.game === g);
  const colWidth = 260;
  const sheetWidth = rs.length * colWidth + 40;
  const sheetHeight = 880;

  let a = [
    '-size', `${sheetWidth}x${sheetHeight}`, 'xc:#121418',
    ...txt('Wordwoven · Phiếu 250 · Quick-Panel Icons — Kiểm tra cỡ thật 1× và so sánh', 20, 30, 20)
  ];

  for (let i = 0; i < rs.length; i++) {
    const r = rs[i];
    const x = 20 + i * colWidth;
    const s720 = r.size720;
    const s1080 = r.size1080;

    a.push(
      ...put(img(r.outputs.find(o => o.size[0] === 256).file, 220), x + 10, 50),
      ...txt(r.name, x + 10, 290, 15, '#7ee7c8'),
      ...txt(r.label, x + 10, 310, 13, '#c8cdd4')
    );

    const spec1080 = makeSpecimen(g, r.name, `${r.label} (1080p)`, s1080, 240);
    const f1080 = `games/${g}/art-src/_review/250/${r.name}.1080p.png`;
    fs.writeFileSync(f1080, spec1080);
    a.push(
      ...put(['(', f1080, ')'], x, 335),
      ...txt(`1080p · ${s1080}px · 1×`, x + 5, 330, 11, '#8fa0b5')
    );

    const spec720 = makeSpecimen(g, r.name, `${r.label} (720p)`, s720, 240);
    const f720 = `games/${g}/art-src/_review/250/${r.name}.720p.png`;
    fs.writeFileSync(f720, spec720);
    a.push(
      ...put(['(', f720, ')'], x, 400),
      ...txt(`720p · ${s720}px · 1×`, x + 5, 395, 11, '#8fa0b5')
    );

    a.push(
      ...put(cropPanel(g, 120, 120), x + 5, 455),
      ...put(['(', r.outputs.find(o => o.size[0] === 1024).file, '-filter', 'Lanczos', '-resize', `${s720}x${s720}!`, '-filter', 'point', '-resize', '400%', ')'], x + 12, 465),
      ...txt('720p ×4 (point)', x + 120, 500, 12, '#8fa0b5')
    );

    a.push(...put(cropPanel(g, 240, 48), x, 600));
    const compIcons = ['vol-master', 'vol-music', 'vol-keyboard.r3', 'vol-keyboard-volume.r2'];
    for (let c = 0; c < compIcons.length; c++) {
      const cPath = getIconPath(g, compIcons[c]);
      if (fs.existsSync(cPath)) {
        a.push(...put(img(cPath, 24), x + 12 + c * 58, 612));
      }
    }
    a.push(...txt('Cặp so sánh trong bảng (24px)', x + 5, 665, 11, '#8fa0b5'));

    a.push(...put(cropPanel(g, 240, 48), x, 690));
    const oldPath = `games/${g}/art-src/ui/quick-settings/selected/${r.baseName}.png`;
    if (fs.existsSync(oldPath)) {
      a.push(
        ...put(img(oldPath, s720), x + 30, 702),
        ...txt('Cũ', x + 35, 750, 12, '#e06060')
      );
    } else {
      a.push(...txt('(Mới)', x + 25, 715, 12, '#888888'));
    }
    a.push(
      ...put(img(r.outputs.find(o => o.size[0] === 1024).file, s720), x + 140, 702),
      ...txt('Mới (r2/r3)', x + 130, 750, 12, '#60e060')
    );
  }

  save(a, `games/${g}/art-src/_review/250-sheet.jpg`);
  save(a, `${D}/250-sheet-wordwoven.jpg`);

  // Wordwoven Corner Buttons Test Sheet
  const skyPath = 'games/typing-defense/art-src/ui/title-epic/title-backdrop.v2.png';
  const groundPath = 'games/typing-defense/art-src/scenery/meadow/decals-v2/ground-decals-a.png';

  let cSheet = [
    '-size', '1000x520', 'xc:#121418',
    ...txt('Wordwoven · Nút góc màn hình (Loa & Loa tắt) trên nền sáng (32px 1× & 4× point)', 20, 30, 18)
  ];

  const cornerIcons = ['hud-sound.r2', 'hud-sound-muted.r2', 'hud-settings.r2'];
  const testBgs = [
    {name: 'Trời sáng (Title Sky)', crop: [skyPath, '240x80+400+100']},
    {name: 'Đất sáng (Map Ground)', crop: [groundPath, '240x80+100+100']},
    {name: 'Khung ngọc (Panel)', crop: [panels[g], '240x80+200+200']}
  ];

  for (let bIdx = 0; bIdx < testBgs.length; bIdx++) {
    const bg = testBgs[bIdx];
    const y = 60 + bIdx * 140;
    cSheet.push(...txt(bg.name, 30, y + 16, 14, '#ffd277'));

    for (let cIdx = 0; cIdx < cornerIcons.length; cIdx++) {
      const cName = cornerIcons[cIdx];
      const x = 30 + cIdx * 310;
      const cImgPath = getIconPath(g, cName);

      cSheet.push(
        ...put(['(', bg.crop[0], '-crop', bg.crop[1], '+repage', ')'], x, y + 26),
        ...put(img(cImgPath, 32), x + 12, y + 48),
        ...txt(`${cName} (32px)`, x + 54, y + 70, 13, '#ffffff'),
        ...put(['(', cImgPath, '-filter', 'Lanczos', '-resize', '32x32!', '-filter', 'point', '-resize', '400%', ')'], x + 200, y + 36)
      );
    }
  }

  save(cSheet, `games/${g}/art-src/_review/250-corner-buttons.jpg`);
  save(cSheet, `${D}/250-corner-buttons-wordwoven.jpg`);

  // Wordwoven Vertical Panels Mockup
  let pMock = [
    '-size', '960x650', 'xc:#121418',
    ...txt('Wordwoven · Bảng Sound & Settings đầy đủ ở 720p 1× (Panel ngọc thật)', 20, 30, 18)
  ];
  pMock.push(...txt('Bảng Âm thanh (Sound)', 30, 65, 15, '#7ee7c8'));
  const wwSoundRows = [
    ['vol-master', 'Master Volume'],
    ['vol-music', 'Music'],
    ['vol-effects', 'Effects'],
    ['vol-keyboard.r3', 'Keyboard Sound'],
    ['vol-keyboard-volume.r2', 'Keyboard Volume'],
    ['vol-voice', 'Voice'],
    ['vol-interface.r2', 'Interface']
  ];
  for (let r = 0; r < wwSoundRows.length; r++) {
    const [name, lbl] = wwSoundRows[r];
    const y = 80 + r * 42;
    pMock.push(
      ...put(cropPanel(g, 380, 38), 30, y),
      ...put(img(getIconPath(g, name), 24), 40, y + 7),
      ...txt(lbl, 74, y + 25, 14, '#e6decb')
    );
  }

  pMock.push(...txt('Bảng Cài đặt (Settings)', 500, 65, 15, '#7ee7c8'));
  const wwSettingsRows = [
    ['pace', 'Pace adapts to your typing'],
    ['story-mode', 'Story mode'],
    ['gfx-motion', 'Reduced motion'],
    ['learn-meaning', 'Vietnamese meaning'],
    ['learn-ipa', 'Pronunciation (IPA)']
  ];
  for (let r = 0; r < wwSettingsRows.length; r++) {
    const [name, lbl] = wwSettingsRows[r];
    const y = 80 + r * 42;
    pMock.push(
      ...put(cropPanel(g, 380, 38), 500, y),
      ...put(img(getIconPath(g, name), 24), 510, y + 7),
      ...txt(lbl, 544, y + 25, 14, '#e6decb')
    );
  }
  save(pMock, `games/${g}/art-src/_review/250-panels.jpg`);
  save(pMock, `${D}/250-panels-wordwoven.jpg`);
}

// 3. Last Line Review Sheet
{
  const g = 'typing-survival';
  const rs = records.filter(r => r.game === g);
  const colWidth = 260;
  const sheetWidth = rs.length * colWidth + 40;
  const sheetHeight = 880;

  let a = [
    '-size', `${sheetWidth}x${sheetHeight}`, 'xc:#121418',
    ...txt('Last Line · Phiếu 250 · Quick-Panel Icons — Kiểm tra cỡ thật 1× và so sánh', 20, 30, 20)
  ];

  for (let i = 0; i < rs.length; i++) {
    const r = rs[i];
    const x = 20 + i * colWidth;
    const s720 = r.size720;
    const s1080 = r.size1080;

    a.push(
      ...put(img(r.outputs.find(o => o.size[0] === 256).file, 220), x + 10, 50),
      ...txt(r.name, x + 10, 290, 15, '#5eead4'),
      ...txt(r.label, x + 10, 310, 13, '#c8cdd4')
    );

    const spec1080 = makeSpecimen(g, r.name, `${r.label} (1080p)`, s1080, 240);
    const f1080 = `games/${g}/art-src/_review/250/${r.name}.1080p.png`;
    fs.writeFileSync(f1080, spec1080);
    a.push(
      ...put(['(', f1080, ')'], x, 335),
      ...txt(`1080p · ${s1080}px · 1×`, x + 5, 330, 11, '#8fa0b5')
    );

    const spec720 = makeSpecimen(g, r.name, `${r.label} (720p)`, s720, 240);
    const f720 = `games/${g}/art-src/_review/250/${r.name}.720p.png`;
    fs.writeFileSync(f720, spec720);
    a.push(
      ...put(['(', f720, ')'], x, 400),
      ...txt(`720p · ${s720}px · 1×`, x + 5, 395, 11, '#8fa0b5')
    );

    a.push(
      ...put(cropPanel(g, 120, 120), x + 5, 455),
      ...put(['(', r.outputs.find(o => o.size[0] === 1024).file, '-filter', 'Lanczos', '-resize', `${s720}x${s720}!`, '-filter', 'point', '-resize', '400%', ')'], x + 12, 465),
      ...txt('720p ×4 (point)', x + 120, 500, 12, '#8fa0b5')
    );

    a.push(...put(cropPanel(g, 240, 48), x, 600));
    const compIcons = ['vol-master', 'vol-music', 'vol-keyboard.r2', 'vol-keyboard-volume'];
    for (let c = 0; c < compIcons.length; c++) {
      const cPath = getIconPath(g, compIcons[c]);
      if (fs.existsSync(cPath)) {
        a.push(...put(img(cPath, 24), x + 12 + c * 58, 612));
      }
    }
    a.push(...txt('Cặp so sánh trong bảng (24px)', x + 5, 665, 11, '#8fa0b5'));

    a.push(...put(cropPanel(g, 240, 48), x, 690));
    const oldCheck = [
      `games/${g}/art-src/ui/quick-settings/selected/${r.baseName}.png`,
      `games/${g}/art-src/ui/icons/${r.baseName}.png`,
      `games/${g}/art-src/ui/icons/${r.baseName}.r2.png`
    ];
    let oldFound = null;
    for (const op of oldCheck) {
      if (fs.existsSync(op)) { oldFound = op; break; }
    }

    if (oldFound) {
      a.push(
        ...put(img(oldFound, s720), x + 30, 702),
        ...txt('Cũ', x + 35, 750, 12, '#e06060')
      );
    } else {
      a.push(...txt('(Mới)', x + 25, 715, 12, '#888888'));
    }
    a.push(
      ...put(img(r.outputs.find(o => o.size[0] === 1024).file, s720), x + 140, 702),
      ...txt('Mới (r2/r3)', x + 130, 750, 12, '#60e060')
    );
  }

  save(a, `games/${g}/art-src/_review/250-sheet.jpg`);
  save(a, `${D}/250-sheet-lastline.jpg`);

  // Last Line Vertical Panels Mockup
  let pMock = [
    '-size', '960x650', 'xc:#121418',
    ...txt('Last Line · Bảng Sound & Settings đầy đủ ở 720p 1× (Panel thép graphite)', 20, 30, 18)
  ];
  pMock.push(...txt('Bảng Âm thanh (Sound)', 30, 65, 15, '#5eead4'));
  const llSoundRows = [
    ['vol-master', 'Master Volume'],
    ['vol-music', 'Music'],
    ['vol-effects.r2', 'Effects'],
    ['vol-keyboard.r2', 'Keyboard Sound'],
    ['vol-keyboard-volume', 'Keyboard Volume'],
    ['vol-voice', 'Voice'],
    ['vol-interface.r2', 'Interface']
  ];
  for (let r = 0; r < llSoundRows.length; r++) {
    const [name, lbl] = llSoundRows[r];
    const y = 80 + r * 42;
    pMock.push(
      ...put(cropPanel(g, 380, 38), 30, y),
      ...put(img(getIconPath(g, name), 24), 40, y + 7),
      ...txt(lbl, 74, y + 25, 14, '#e6decb')
    );
  }

  pMock.push(...txt('Bảng Cài đặt (Settings)', 500, 65, 15, '#5eead4'));
  const llSettingsRows = [
    ['ship', 'Ship'],
    ['reduced-motion.r3', 'Reduced Motion'],
    ['quality.r2', 'Quality'],
    ['shake.r2', 'Screen Shake'],
    ['pace-director.r2', 'Adapt Pace'],
    ['read-aloud.r2', 'Read Words Aloud']
  ];
  for (let r = 0; r < llSettingsRows.length; r++) {
    const [name, lbl] = llSettingsRows[r];
    const y = 80 + r * 42;
    pMock.push(
      ...put(cropPanel(g, 380, 38), 500, y),
      ...put(img(getIconPath(g, name), 28), 508, y + 5),
      ...txt(lbl, 544, y + 25, 14, '#e6decb')
    );
  }
  save(pMock, `games/${g}/art-src/_review/250-panels.jpg`);
  save(pMock, `${D}/250-panels-lastline.jpg`);
}

console.log('All review sheets generated successfully for all three games.');
