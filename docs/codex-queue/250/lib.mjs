import fs from 'node:fs';
import {execFileSync} from 'node:child_process';

export const M = '/opt/homebrew/bin/magick';
export const D = 'docs/codex-queue/250';

export const im = (a, input) => execFileSync(M, a, {
  input,
  maxBuffer: 120 * 1024 * 1024,
  timeout: 30000,
  env: {...process.env, MAGICK_THREAD_LIMIT: '1'}
});

export const json = (p, v) => fs.writeFileSync(p, JSON.stringify(v, null, 2) + '\n');
export const dim = p => im(['identify', '-format', '%w %h', p]).toString().trim().split(' ').map(Number);
export const raw = (p, w, h = w) => im([p, ...(w ? ['-filter', 'Lanczos', '-resize', `${w}x${h}!`] : []), '-depth', '8', 'rgba:-']);

export function box(b, w, h, t = 16) {
  let x0 = w, y0 = h, x1 = -1, y1 = -1;
  for (let y = 0; y < h; y++) {
    for (let x = 0; x < w; x++) {
      if (b[(y * w + x) * 4 + 3] > t) {
        x0 = Math.min(x0, x);
        x1 = Math.max(x1, x);
        y0 = Math.min(y0, y);
        y1 = Math.max(y1, y);
      }
    }
  }
  if (x1 < 0) return [0, 0, w, h];
  return [x0, y0, x1 - x0 + 1, y1 - y0 + 1];
}

export function mask(b, t = 16) {
  return Uint8Array.from({length: b.length / 4}, (_, i) => +(b[i * 4 + 3] > t));
}

export function iou(a, b) {
  let n = 0, d = 0;
  for (let i = 0; i < a.length; i++) {
    n += (a[i] && b[i]) ? 1 : 0;
    d += (a[i] || b[i]) ? 1 : 0;
  }
  return d ? n / d : 0;
}

export const lum = (r, g, b) => (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255;

export function hsv(r, g, b) {
  let mx = Math.max(r, g, b), mn = Math.min(r, g, b), d = mx - mn, h = 0;
  if (d) {
    h = mx === r ? ((g - b) / d) % 6 : mx === g ? (b - r) / d + 2 : (r - g) / d + 4;
    h = (h * 60 + 360) % 360;
  }
  return [h, mx ? d / mx : 0, mx / 255];
}

export function clean(b, w, h) {
  const m = mask(b, 127);
  let repaired = 0;
  for (let y = 0; y < h; y++) {
    for (let x = 0; x < w; x++) {
      const i = (y * w + x) * 4, a = b[i + 3];
      if (a > 0 && a < 255) {
        let v0 = false, v1 = false;
        for (let yy = Math.max(0, y - 3); yy <= Math.min(h - 1, y + 3); yy++) {
          for (let xx = Math.max(0, x - 3); xx <= Math.min(w - 1, x + 3); xx++) {
            if (m[yy * w + xx]) v1 = true;
            else v0 = true;
          }
        }
        if (!(v0 && v1) || a <= 2 || a >= 253) {
          b[i + 3] = a >= 128 ? 255 : 0;
          repaired++;
        }
      }
    }
  }
  return repaired;
}

export const png = (b, w, h) => im(['-size', `${w}x${h}`, '-depth', '8', 'rgba:-', '-colorspace', 'sRGB', '-define', 'png:color-type=6', 'png:-'], b);
