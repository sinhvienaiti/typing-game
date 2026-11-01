// Frame sequences of the Lab's focus strip on a stepped clock (exact frame times, not wall time).
// Run with the kit's CDP driver while the Lab serves on 4192, through the shared GPU lock:
//   .local/bin/heavy.sh --gpu node shared/game-kit/tools/cdp-run.mjs tools/typing-feedback-lab/scripts/capture.mjs --width=1920 --height=1080
// Env: URL (default http://127.0.0.1:4192/), OUT_DIR (default tools/typing-feedback-lab/tmp/frames),
// STYLES (comma list), GAME (dragon-hold | typing-survival | typing-defense), INTENSITY (default normal),
// REDUCED=1, COMBO (combo before the word, default 3), LOAD=1 (Last Line's Load host mode: words fly into the
// stand-in bay; frames are tagged "<size>-load").
// For each style: 13 frames over 1 s around a key, a wrong key and a word complete.
import { mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";

export const OFFSETS = [0, 17, 33, 50, 67, 83, 100, 133, 167, 200, 300, 500, 1000];

export default async function capture(page) {
  const url = process.env.URL ?? "http://127.0.0.1:4192/";
  const out = process.env.OUT_DIR ?? "tools/typing-feedback-lab/tmp/frames";
  const styles = (process.env.STYLES ?? "stamp,flare,smash,shatter,rune,minimal").split(",");
  const game = process.env.GAME ?? "dragon-hold";
  const intensity = process.env.INTENSITY ?? "normal";
  const reduced = process.env.REDUCED === "1";
  const combo = Number(process.env.COMBO ?? 3);
  const load = process.env.LOAD === "1";
  await page.goto(url, { settle: 400 });
  await page.eval("window.__lab.ready.then(() => true)");
  await page.eval(`window.__lab.game(${JSON.stringify(game)}, 1).then(() => true)`);
  await page.eval("(window.__lab.panel(false), document.fonts.ready.then(() => true))");
  if (load) await page.eval("(window.__lab.load(true), true)");
  const view = await page.eval("({ w: innerWidth, h: innerHeight, size: parseFloat(getComputedStyle(document.querySelector('.tfx')).getPropertyValue('--tfx-size')) })");
  const { w, h, size } = view;
  // The strip and the canvas around it; the word's release in a half-size full frame.
  const strip = { x: Math.round(w / 2 - 7 * size), y: Math.round(0.2 * h - 1.7 * size), width: Math.round(14 * size), height: Math.round(4.6 * size) };
  const full = { x: 0, y: 0, width: w, height: h, scale: 960 / w };
  const tag = `${w}x${h}` + (load ? "-load" : "");
  const report = { view, strip, game, intensity, reduced, combo, styles: {} };
  for (const style of styles) {
    const dir = join(out, tag, style);
    mkdirSync(dir, { recursive: true });
    await page.eval(`(() => { const L = window.__lab; L.configure({ style: ${JSON.stringify(style)}, intensity: ${JSON.stringify(intensity)} }); L.reduced(${reduced}); L.freeze(); L.setCombo(${combo}); L.word('thank', 'cảm ơn, cám ơn'); return true; })()`);
    const T = 100000;
    // A key: "t" and "h" settle first, then frames around "a".
    await page.eval(`(() => { const L = window.__lab; L.at(${T}); L.press('t'); L.at(${T + 300}); L.press('h'); L.at(${T + 600}); L.press('a'); return true; })()`);
    for (const off of OFFSETS) {
      await page.eval(`(window.__lab.at(${T + 600 + off}), true)`);
      await page.shot(join(dir, `key-${String(off).padStart(4, "0")}.jpg`), { clip: strip });
    }
    // A wrong key while "n" is due.
    await page.eval(`(() => { const L = window.__lab; L.at(${T + 2000}); L.press('x'); return true; })()`);
    for (const off of OFFSETS) {
      await page.eval(`(window.__lab.at(${T + 2000 + off}), true)`);
      await page.shot(join(dir, `wrong-${String(off).padStart(4, "0")}.jpg`), { clip: strip });
    }
    // The word: "n", then "k" completes it (perfect: the wrong key above broke it, so start clean).
    await page.eval(`(() => { const L = window.__lab; L.at(${T + 3000}); L.setCombo(${combo}); L.word('thank', 'cảm ơn, cám ơn'); ['t','h','a','n'].forEach((c, i) => { L.at(${T + 3000} + i * 120); L.press(c); }); L.at(${T + 3600}); L.press('k'); return true; })()`);
    for (const off of OFFSETS) {
      await page.eval(`(window.__lab.at(${T + 3600 + off}), true)`);
      await page.shot(join(dir, `word-${String(off).padStart(4, "0")}.jpg`), { clip: full });
    }
    report.styles[style] = await page.eval("window.__lab.stats()");
  }
  writeFileSync(join(out, tag, "capture.json"), JSON.stringify(report, null, 2));
  return { tag, styles: styles.length, frames: styles.length * OFFSETS.length * 3 };
}
