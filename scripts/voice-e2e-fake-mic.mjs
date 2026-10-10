// End-to-end Voice check without a microphone: the real Portal VoiceHost and
// Vosk runtime run in headless Chrome; the "microphone" is a synthetic stream
// playing spoken words (macOS `say`), so capture → worklet → Vosk → final
// matcher → detections all run as in the game.
//
//   pnpm dev:portal                       # Portal dev server on 127.0.0.1:3100
//   pnpm voice:e2e                        # default words, 30 s
//   pnpm voice:e2e -- --seconds=45 --stress --words=galaxy,shield,code
//
// --stress blocks the page main thread 30 ms out of every 40 ms (the game
// shares that thread), to check overload recovery. The report includes bounded
// capture→main-thread, main-thread→decoder-ACK and event-loop timing evidence so
// an overload can be localized instead of hidden by increasing the audio queue.
import { execFileSync, spawn } from "node:child_process";
import { mkdtempSync, readFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { summarizeVoiceProfile } from "./voice-profile-summary.mjs";

const flag = (name, fallback) => {
  const hit = process.argv.find((a) => a.startsWith("--" + name + "="));
  return hit === undefined ? fallback : hit.slice(name.length + 3);
};
const words = flag("words", "galaxy,shield,code,planet,reactor,focus,orbit,typing,sister,energy,laser,comet,rocket,meteor,captain,signal")
  .split(",").map((w) => w.trim().toLowerCase()).filter(Boolean);
const seconds = Number(flag("seconds", "30"));
const stress = process.argv.includes("--stress");
const portal = flag("portal", "http://127.0.0.1:3100");
const chrome = process.env.CHROME_PATH ?? "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";

const work = mkdtempSync(join(tmpdir(), "voice-e2e-"));
const aiff = join(work, "speech.aiff"), wav = join(work, "speech.wav");
execFileSync("say", ["-v", "Samantha", "-r", "170", "-o", aiff, words.join(". [[slnc 600]] ") + "."]);
execFileSync("ffmpeg", ["-hide_banner", "-loglevel", "error", "-y", "-i", aiff, "-af", "apad=pad_dur=4", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", wav]);
const wavB64 = readFileSync(wav).toString("base64");

const scenario = `(async () => {
  const bytes = Uint8Array.from(atob("${wavB64}"), (c) => c.charCodeAt(0));
  const feed = new AudioContext();
  const buffer = await feed.decodeAudioData(bytes.buffer);
  const mic = feed.createMediaStreamDestination();
  const player = feed.createBufferSource(); player.buffer = buffer; player.loop = true; player.connect(mic); player.start();
  navigator.mediaDevices.getUserMedia = async () => mic.stream;
  const words = ${JSON.stringify(words)};
  const { createBrowserVoiceHost } = await import("/src/voice/host-factory.mjs");
  const events = [];
  const host = createBrowserVoiceHost((event) => events.push(event));
  await host.start(0);
  if (!events.some((e) => e.type === "ready")) return { detections: [], errors: events.filter((e) => e.type === "error").map((e) => e.message), profile: {} };

  const runtime = host.runtime;
  const profile = {
    pcmBlocks: 0,
    overflowEvents: 0,
    maxPending: 0,
    captureDispatchMs: [],
    decodeAckMs: [],
    eventLoopLagMs: [],
  };
  const keep = (values, value) => {
    if (!Number.isFinite(value) || value < 0) return;
    if (values.length >= 512) values.shift();
    values.push(value);
  };

  // BrowserVoiceRuntime uses TypeScript-private (not #private) members. The E2E
  // profiler wraps them only in this temporary test page; production behavior
  // and Voice protocol messages are untouched.
  const originalCaptureMessage = runtime.captureMessage.bind(runtime);
  runtime.captureMessage = (message) => {
    if (message?.type === "pcm") {
      profile.pcmBlocks++;
      message.__profileReceivedAtMs = performance.now();
      if (Number.isFinite(message.audioTimeMs))
        keep(profile.captureDispatchMs, runtime.audio.currentTime * 1000 - message.audioTimeMs);
    }
    originalCaptureMessage(message);
    profile.maxPending = Math.max(profile.maxPending, runtime.pending?.length ?? 0);
  };
  const originalAcknowledge = runtime.acknowledge.bind(runtime);
  runtime.acknowledge = (generation) => {
    const pending = runtime.pending?.[0];
    if (Number.isFinite(pending?.__profileReceivedAtMs))
      keep(profile.decodeAckMs, performance.now() - pending.__profileReceivedAtMs);
    originalAcknowledge(generation);
  };
  const originalOverloaded = runtime.overloaded.bind(runtime);
  runtime.overloaded = () => {
    profile.overflowEvents++;
    originalOverloaded();
  };

  let expectedTick = performance.now() + 20;
  const eventLoopTimer = setInterval(() => {
    const now = performance.now();
    keep(profile.eventLoopLagMs, Math.max(0, now - expectedTick));
    expectedTick = now + 20;
  }, 20);
  const stressTimer = ${stress} ? setInterval(() => {
    const end = performance.now() + 30;
    while (performance.now() < end);
  }, 40) : null;

  host.checkVocabulary({ ...host.session, requestId: "e2e", forms: words });
  const targets = words.map((w, i) => ({ unitId: "u" + i, unitVersion: 1, eligibilityVersion: 1, capability: "word", forms: [w], eligible: true, eligibleFromSample: 0 }));
  await host.applyTargets({ ...host.session, snapshotId: "e2e-1", registryRevision: 1, publishedAtSample: runtime.nowSample(), sampleRate: 16000, targets });
  await new Promise((r) => setTimeout(r, ${seconds} * 1000));
  clearInterval(eventLoopTimer);
  if (stressTimer !== null) clearInterval(stressTimer);
  const result = {
    detections: events.filter((e) => e.type === "detection").map((e) => e.form),
    errors: events.filter((e) => e.type === "error").map((e) => e.message),
    profile,
  };
  await host.stop();
  return result;
})()`;

const port = 9600 + Math.floor(Math.random() * 300);
const profile = join(work, "profile");
const browser = spawn(chrome, ["--headless=new", "--remote-debugging-port=" + port, "--autoplay-policy=no-user-gesture-required", "--no-first-run", "--user-data-dir=" + profile, "about:blank"], { stdio: "ignore" });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let exitCode = 1;
try {
  let pages = [];
  for (let i = 0; i < 80 && !pages.length; i++) {
    try { pages = (await (await fetch("http://127.0.0.1:" + port + "/json/list")).json()).filter((p) => p.type === "page"); } catch {}
    if (!pages.length) await sleep(250);
  }
  const ws = new WebSocket(pages[0].webSocketDebuggerUrl);
  await new Promise((ok) => ws.addEventListener("open", ok, { once: true }));
  let id = 0; const pending = new Map();
  ws.addEventListener("message", (e) => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); } });
  const send = (method, params = {}) => new Promise((ok) => { const n = ++id; pending.set(n, ok); ws.send(JSON.stringify({ id: n, method, params })); });
  await send("Runtime.enable"); await send("Page.enable");
  await send("Page.navigate", { url: portal + "/" });
  await sleep(3000);
  const reply = await send("Runtime.evaluate", { expression: scenario, awaitPromise: true, returnByValue: true });
  const result = reply.result?.result?.value;
  if (result === undefined) throw new Error(JSON.stringify(reply.result).slice(0, 500));
  const missing = words.filter((w) => !result.detections.includes(w));
  const profileSummary = summarizeVoiceProfile(result.profile);
  console.log(JSON.stringify({
    stress,
    seconds,
    detections: result.detections.length,
    missing,
    errors: result.errors,
    profile: profileSummary,
  }, null, 1));
  // Timing is evidence, not an acceptance threshold: real-microphone/hardware
  // latency gates remain manual. E2E failure semantics stay recognition/error-only.
  exitCode = missing.length === 0 && result.errors.length === 0 ? 0 : 1;
} finally {
  browser.kill("SIGKILL");
  setTimeout(() => rmSync(work, { recursive: true, force: true }), 300);
  process.exitCode = exitCode;
}
