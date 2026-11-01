// Load test of the focus strip and key sounds on the real clock: the Lab's bot types 15 keys a second
// (4 % wrong keys) for each style at Normal and Ultra, then real key events (CDP) measure key → frame.
// A perf run takes the whole GPU pool:
//   .local/bin/heavy.sh --perf node shared/game-kit/tools/cdp-run.mjs tools/typing-feedback-lab/scripts/perf.mjs --width=1920 --height=1080
// Env: URL, OUT_DIR, SECONDS (per cell, default 6), STYLES, INTENSITIES, PROFILE (keyboard profile, default
// creamy; a pending one is silent, so voices read 0 until the Audio Lab stages it), LOAD=1 (Last Line's Load host mode,
// GAME=typing-survival by default then; the report is perf-<size>-load.json).
import { mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

export default async function perf(page) {
  const url = process.env.URL ?? "http://127.0.0.1:4192/";
  const out = process.env.OUT_DIR ?? "tools/typing-feedback-lab/tmp/perf";
  const seconds = Number(process.env.SECONDS ?? 6);
  const styles = (process.env.STYLES ?? "stamp,flare,smash,shatter,rune,minimal").split(",");
  const intensities = (process.env.INTENSITIES ?? "normal,ultra").split(",");
  const profile = process.env.PROFILE ?? "creamy";
  const load = process.env.LOAD === "1";
  await page.goto(url, { settle: 500 });
  await page.eval("window.__lab.ready.then(() => true)");
  await page.eval("(window.__lab.panel(false), true)");
  if (load) await page.eval(`window.__lab.game(${JSON.stringify(process.env.GAME ?? "typing-survival")}, 1).then(() => (window.__lab.load(true), true))`);
  // A click starts audio (the flag allows autoplay; the click makes it explicit), then the profile loads.
  await page.mouse(20, 20, "mousePressed");
  await page.mouse(20, 20, "mouseReleased");
  await page.eval(`window.__lab.profile(${JSON.stringify(profile)}).then(() => window.__lab.loadReport)`);
  await page.eval(`(() => {
    window.__perf = { long: 0, longMs: 0 };
    new PerformanceObserver((list) => { for (const e of list.getEntries()) { window.__perf.long += 1; window.__perf.longMs = Math.max(window.__perf.longMs, e.duration); } }).observe({ type: "longtask", buffered: false });
    return true;
  })()`);
  const cells = [];
  for (const intensity of intensities) {
    for (const style of styles) {
      await page.eval(`(() => { const L = window.__lab; L.configure({ style: ${JSON.stringify(style)}, intensity: ${JSON.stringify(intensity)} }); L.strip.stats.maxParticles = 0; window.__perf.long = 0; window.__perf.longMs = 0; window.__peakVoices = 0; window.__voiceTimer = setInterval(() => { window.__peakVoices = Math.max(window.__peakVoices, L.sounds.activeVoices()); }, 20); L.bot(15); return true; })()`);
      const before = await page.eval("window.__lab.stats()");
      await sleep(seconds * 1000);
      const after = await page.eval("(() => { const s = window.__lab.stats(); clearInterval(window.__voiceTimer); window.__lab.bot(0); return { ...s, long: window.__perf.long, longMs: window.__perf.longMs, peakVoices: window.__peakVoices, stolen: window.__lab.sounds.stolen }; })()");
      cells.push({
        style,
        intensity,
        keys: after.keys - before.keys,
        words: after.words - before.words,
        fps: Math.round(1000 / after.meanFrame),
        frameP95: Number(after.frameP95.toFixed(2)),
        updateP95: Number(after.updateP95.toFixed(3)),
        updateMax: Number(after.updateMax.toFixed(3)),
        peakParticles: after.maxParticles,
        cap: after.cap,
        stolenParticles: after.stolen,
        peakVoices: after.peakVoices,
        longTasks: after.long,
        longestTaskMs: Math.round(after.longMs),
        heapMB: Number((after.heap / 1048576).toFixed(1)),
      });
      await sleep(600);
    }
  }
  // Real key events at ~15 a second: the Lab measures each key to the next frame.
  await page.eval("(window.__lab.configure({ style: 'stamp', intensity: 'normal' }), true)");
  let typed = 0;
  for (let k = 0; k < 75; k += 1) {
    const text = await page.eval("[...document.querySelectorAll('.tfx-layer.is-on .tfx-g')].filter((g) => g.style.display !== 'none').map((g) => g.firstChild.textContent).join('')");
    const due = await page.eval("[...document.querySelectorAll('.tfx-layer.is-on .tfx-g')].findIndex((g) => g.classList.contains('is-due'))");
    const ch = text[Math.max(0, due)] ?? "e";
    await page.key(ch);
    typed += 1;
    await sleep(40);
  }
  const latency = await page.eval("window.__lab.stats().latency");
  const report = { url, seconds, profile, load, landed: load ? await page.eval("window.__lab.landed()") : null, sounds: await page.eval("window.__lab.loadReport"), cells, latency: { keys: typed, ...latency } };
  mkdirSync(out, { recursive: true });
  const size = await page.eval("innerWidth + 'x' + innerHeight");
  writeFileSync(join(out, `perf-${size}${load ? "-load" : ""}.json`), JSON.stringify(report, null, 2));
  return report;
}
