import fs from 'node:fs';
import path from 'node:path';
import {im, dim, raw, box, clean, png, hsv, json, D} from './lib.mjs';

const jobs = JSON.parse(fs.readFileSync(`${D}/jobs.json`));
const processedRecords = [];

for (const j of jobs) {
  console.log(`Processing job: ${j.id} (${j.name})`);
  const src = j.source;
  const [w, h] = dim(src);
  const revDir = `games/${j.game}/art-src/_review/250`;
  fs.mkdirSync(revDir, {recursive: true});

  // 1. Load raw bytes
  const b = raw(src);
  let keyRemoved = 0;

  // 2. Remove pure magenta chromakey completely (including dark edge fringes)
  for (let i = 0; i < b.length; i += 4) {
    const [hu, s, v] = hsv(b[i], b[i + 1], b[i + 2]);
    // Magenta hue is around 300 deg (265 to 335). Remove all saturated magenta.
    if (Math.abs(hu - 300) <= 35 && s > 0.25) {
      b[i + 3] = 0;
      keyRemoved++;
    }
  }

  // 3. Compute bounding box of visible content (alpha > 16)
  const bounds = box(b, w, h, 16);
  const [x, y, cw, ch] = bounds;
  const longEdge = Math.max(cw, ch);
  // Pad so that bounding box occupies 70% of canvas
  const pw = Math.ceil(longEdge / 0.70);
  const ph = pw;

  // 4. Crop, repage, and extend to padded square
  const sourcePng = png(b, w, h);
  const padded = im([
    'png:-',
    '-crop', `${cw}x${ch}+${x}+${y}`,
    '+repage',
    '-background', 'none',
    '-gravity', 'center',
    '-extent', `${pw}x${ph}`,
    'png:-'
  ], sourcePng);

  const prefix = `${revDir}/${j.name}`;
  const outputs = [];

  // 5. Generate scaled outputs: 1024, 256, 128, 64
  for (const s of [1024, 256, 128, 64]) {
    const rb = im([
      'png:-',
      '-filter', 'Lanczos',
      '-resize', `${s}x${s}!`,
      '-depth', '8',
      'rgba:-'
    ], padded);

    // Clean alpha boundary
    const repaired = clean(rb, s, s);
    const dest = `${prefix}${s === 1024 ? '' : '.' + s}.processed.png`;
    fs.writeFileSync(dest, png(rb, s, s));
    outputs.push({
      file: dest,
      size: [s, s],
      alphaRepaired: repaired
    });
  }

  // 6. Generate "bản sinh | bản hậu kỳ" comparison sheet (512x256)
  const compSheet = `${revDir}/${j.name}-compare.jpg`;
  im([
    '-size', '512x256', 'xc:#20242b',
    '(', src, '-filter', 'Lanczos', '-resize', '240x240', ')',
    '-geometry', '+8+8', '-composite',
    '(', outputs[1].file, '-resize', '240x240', ')',
    '-geometry', '+264+8', '-composite',
    compSheet
  ]);

  processedRecords.push({
    id: j.id,
    game: j.game,
    name: j.name,
    baseName: j.baseName,
    version: j.version,
    label: j.label,
    panel: j.panel,
    type: j.type,
    attempt: j.attempt,
    size720: j.size720,
    size1080: j.size1080,
    source: src,
    keyRemoved,
    bbox: bounds,
    paddedSize: [pw, ph],
    compareSheet: compSheet,
    outputs
  });
}

json(`${D}/processed.json`, processedRecords);
console.log(`Processed ${processedRecords.length} records successfully.`);
