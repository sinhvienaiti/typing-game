import fs from 'node:fs';
import {im, raw, box, mask, iou, lum, hsv, json, D} from './lib.mjs';

const records = JSON.parse(fs.readFileSync(`${D}/processed.json`));
const jobs = JSON.parse(fs.readFileSync(`${D}/jobs.json`));
const panels = {
  'dragon-hold': 'games/dragon-hold/art-src/ui/frames/panel-large.png',
  'typing-defense': 'games/typing-defense/art-src/ui/frames-epic/panel-large.v2.png',
  'typing-survival': 'games/typing-survival/art-src/ui/frames-epic/panel-large.png'
};

function alphaAudit(p, w, h) {
  const b = raw(p);
  const m = mask(b, 127);
  let partial = 0, key = 0, vis = 0;
  for (let y = 0; y < h; y++) {
    for (let x = 0; x < w; x++) {
      const i = (y * w + x) * 4;
      const a = b[i + 3];
      if (a > 0) {
        vis++;
        const [hu, s, v] = hsv(b[i], b[i + 1], b[i + 2]);
        if (Math.abs(hu - 300) <= 15 && s > 0.5) key++;
      }
      if (a > 0 && a < 255) {
        let v0 = false, v1 = false;
        for (let yy = Math.max(0, y - 3); yy <= Math.min(h - 1, y + 3); yy++) {
          for (let xx = Math.max(0, x - 3); xx <= Math.min(w - 1, x + 3); xx++) {
            if (m[yy * w + xx]) v1 = true;
            else v0 = true;
          }
        }
        if (!(v0 && v1)) partial++;
      }
    }
  }
  return {
    size: [w, h],
    bbox: box(b, w, h),
    partialOutside3px: partial,
    keyHuePercent: vis > 0 ? (key / vis) * 100 : 0
  };
}

function opening(m, w, h) {
  let e = new Uint8Array(m.length);
  let d = new Uint8Array(m.length);
  for (let y = 0; y < h - 1; y++) {
    for (let x = 0; x < w - 1; x++) {
      e[y * w + x] = m[y * w + x] && m[y * w + x + 1] && m[(y + 1) * w + x] && m[(y + 1) * w + x + 1];
    }
  }
  for (let y = 0; y < h; y++) {
    for (let x = 0; x < w; x++) {
      for (let yy = Math.max(0, y - 1); yy <= y; yy++) {
        for (let xx = Math.max(0, x - 1); xx <= x; xx++) {
          if (e[yy * w + xx]) d[y * w + x] = 1;
        }
      }
    }
  }
  return d;
}

const auditReport = {
  icons: [],
  pairs: []
};

for (const r of records) {
  const job = jobs.find(j => j.id === r.id);
  const p1024 = `${job.selectedDir}/${r.name}.png`;
  const s = r.size720;
  const hi = r.size1080;

  // Render at 720p size
  const b = raw(p1024, s);
  const m = mask(b, 128);
  const bb = box(b, s, s, 128);
  const opened = opening(m, s, s);
  const count = m.reduce((a, v) => a + v, 0);

  // Background panel patch
  const panelPath = panels[r.game];
  const patch = im([panelPath, '-crop', `${s}x${s}+208+208`, '+repage', '-depth', '8', 'rgba:-']);

  let fg = 0, bg = 0, n = 0;
  for (let i = 0; i < m.length; i++) {
    if (m[i]) {
      const j = i * 4;
      const a = b[j + 3] / 255;
      fg += lum(b[j] * a + patch[j] * (1 - a), b[j + 1] * a + patch[j + 1] * (1 - a), b[j + 2] * a + patch[j + 2] * (1 - a));
      bg += lum(patch[j], patch[j + 1], patch[j + 2]);
      n++;
    }
  }

  // Alpha metrics across all sizes
  const sizes = [1024, 256, 128, 64];
  const alphaMetrics = sizes.map(sz => {
    const filePath = `${job.selectedDir}/${r.name}${sz === 1024 ? '' : '.' + sz}.png`;
    return alphaAudit(filePath, sz, sz);
  });

  const openingRetention = count > 0 ? (opened.reduce((a, v) => a + v, 0) / count) * 100 : 0;
  const coverage = (bb[2] * bb[3]) > 0 ? (count / (bb[2] * bb[3])) * 100 : 0;
  const contrast = n > 0 ? (fg / n) - (bg / n) : 0;

  auditReport.icons.push({
    id: r.id,
    game: r.game,
    name: r.name,
    label: r.label,
    panel: r.panel,
    type: r.type,
    size720: s,
    size1080: hi,
    delivered1024: p1024,
    alphaMetrics,
    openingRetention,
    coverage,
    contrastOnPanel: contrast,
    panelMeanLuma: n > 0 ? bg / n : 0,
    objectMeanLuma: n > 0 ? fg / n : 0
  });
}

// Compute IoU pairs for icons within each game
for (const g of ['dragon-hold', 'typing-defense', 'typing-survival']) {
  const gIcons = auditReport.icons.filter(i => i.game === g);
  for (let i = 0; i < gIcons.length; i++) {
    for (let j = i + 1; j < gIcons.length; j++) {
      const a = gIcons[i];
      const b = gIcons[j];
      const bA = raw(a.delivered1024, 24);
      const bB = raw(b.delivered1024, 24);
      const mA = mask(bA, 128);
      const mB = mask(bB, 128);
      const vIoU = iou(mA, mB);
      auditReport.pairs.push({
        game: g,
        a: a.name,
        b: b.name,
        iou24: vIoU
      });
    }
  }
}

json(`${D}/audit-metrics.json`, auditReport);
console.log('Audit metrics generated successfully for all 20 icons.');
