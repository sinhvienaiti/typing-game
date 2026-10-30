// Typing Feedback Lab: the kit's focus strip and key sounds over a captured game frame, driven by
// real typing (or the bot, or the capture script through window.__lab). Lab text is English.
import {
  DEFAULT_TYPING_FX,
  FocusStrip,
  TYPING_FX_INTENSITIES,
  TYPING_FX_INTENSITY_NAMES,
  TYPING_FX_SIZE_NAMES,
  TYPING_FX_SIZES,
  TYPING_FX_STYLE_NAMES,
  TYPING_FX_STYLES,
  TypingFxDriver,
  TypingSounds,
  KeyboardSoundPreview,
  loadKeyboardCatalog,
  type KeyboardSoundChoice,
  type TypingFxIntensity,
  type TypingFxProgress,
  type TypingFxSettings,
  type TypingFxSize,
  type TypingFxSink,
  type TypingFxStyle,
} from "../../../shared/game-kit/feedback/typing-fx";
import { KEYS_BASE } from "./profiles";
import { KeyboardSoundChoices } from "../../../shared/game-kit/ui/quick-settings";

type GameId = "dragon-hold" | "typing-survival" | "typing-defense";
type Game = { name: string; backdrop: string; levels: number; target: { x: number; y: number }; accent: string; anchorY: number };

/** Each game's frame (kept in tmp/backdrops), its typing colour and where its power sits in the frame (fractions). */
const GAMES: Readonly<Record<GameId, Game>> = {
  "dragon-hold": { name: "Dragonhold", backdrop: "/lab-backdrop/dragonhold.jpg", levels: 10, target: { x: 0.5, y: 0.53 }, accent: "#7ff5e0", anchorY: 0.2 },
  "typing-survival": { name: "Last Line", backdrop: "/lab-backdrop/lastline.jpg", levels: 3, target: { x: 0.5, y: 0.79 }, accent: "#5fd8ff", anchorY: 0.2 },
  "typing-defense": { name: "Wordwoven", backdrop: "/lab-backdrop/wordwoven.jpg", levels: 5, target: { x: 0.5, y: 0.835 }, accent: "#19c9a8", anchorY: 0.2 },
};

const $ = <T extends HTMLElement>(id: string): T => document.getElementById(id) as T;
const profileHost = $<HTMLElement>("profile");
let keyboardOptions: readonly KeyboardSoundChoice[] = [];
let keyboardPicker: KeyboardSoundChoices | null = null;
const profileNote = $<HTMLElement>("profileNote");
const stage = $<HTMLDivElement>("stage");
const backdrop = $<HTMLImageElement>("backdrop");
const panel = $<HTMLElement>("panel");

// ── Clock: real time, or a manual one the capture script steps ───────────
let manual = false;
let virtualNow = 0;
const clock = (): number => (manual ? virtualNow : performance.now());

// ── State ────────────────────────────────────────────────────────────────
let gameId: GameId = "dragon-hold";
let words: { en: string; vi: string }[] = [];
let wordIndex = 0;
let current = { en: "", vi: "" };
let typed = 0;
let errors = 0;
let combo = 0;
let wordSerial = 0;
let mode: "new" | "today" = "new";
const settings: TypingFxSettings = { ...DEFAULT_TYPING_FX };
try {
  const saved = JSON.parse(localStorage.getItem("typing-feedback-lab.keyboard") ?? "null") as { soundProfile?: string } | null;
  if (typeof saved?.soundProfile === "string") settings.soundProfile = saved.soundProfile;
} catch { /* Storage unavailable: keep a session-only choice. */ }

// ── Target: the game's power anchor through the backdrop's cover fit ─────
const targetPoint = (out: { x: number; y: number }): boolean => {
  const w = stage.clientWidth;
  const h = stage.clientHeight;
  const iw = backdrop.naturalWidth || 1920;
  const ih = backdrop.naturalHeight || 1080;
  const scale = Math.max(w / iw, h / ih);
  const t = GAMES[gameId].target;
  out.x = (w - iw * scale) / 2 + t.x * iw * scale;
  out.y = (h - ih * scale) / 2 + t.y * ih * scale;
  return true;
};

const strip = new FocusStrip({
  root: stage,
  anchor: { x: 0.5, y: GAMES[gameId].anchorY },
  palette: { accent: GAMES[gameId].accent },
  settings,
  target: targetPoint,
  autoTick: false,
  reducedMotion: false,
  clock,
  zIndex: 20,
});

// ── Sounds: ticket-189 catalogue and the shared ticket-190 picker ──
const sounds = new TypingSounds({ keyVoices: 6, wordVoices: 2 });
const loadReport: Record<string, string> = {};
const keyboardPreview = new KeyboardSoundPreview({
  sounds,
  levels: () => ({ master: Number($<HTMLInputElement>("masterVolume").value), keyboard: settings.volume, muted: $<HTMLInputElement>("masterMuted").checked }),
  onLoad: (result) => { loadReport[result.id] = `${result.state}: ${result.keys} keys, ${result.spaces} spaces`; },
});
/** Selection and startup share the same progressive loader and cancellation lifecycle. */
async function useProfile(id: string, preview = true): Promise<void> {
  settings.soundProfile = id;
  keyboardPicker?.sync(id);
  try { localStorage.setItem("typing-feedback-lab.keyboard", JSON.stringify({ soundProfile: id })); } catch { /* Session only. */ }
  const choice = keyboardOptions.find((p) => p.value === id);
  if (choice) keyboardPreview.select(choice, preview);
}

function startAudio(): void {
  sounds.resume();
}

// ── "Today": a stand-in for the games' small tag over the target ─────────
const todayEl = $<HTMLDivElement>("today");
const today: TypingFxSink = {
  setWord(text, meaning) {
    todayEl.innerHTML = [...text].map((ch) => `<b>${ch}</b>`).join("") + `<span class="m">${meaning}</span>`;
    const pt = { x: 0, y: 0 };
    targetPoint(pt);
    todayEl.style.left = pt.x + "px";
    todayEl.style.top = pt.y - stage.clientHeight * 0.09 + "px";
    todayEl.hidden = mode !== "today";
  },
  key(index) {
    const b = todayEl.children[index] as HTMLElement | undefined;
    if (b === undefined) return;
    b.className = "t";
    void b.offsetWidth;
    b.className = "t j";
  },
  wrong(index) {
    const b = todayEl.children[index] as HTMLElement | undefined;
    if (b !== undefined) b.className = "p";
  },
  complete() {
    todayEl.hidden = true;
  },
  clear() {
    todayEl.hidden = true;
  },
};

/** Routes the driver's calls to the look being compared; sounds hear both. */
const look: TypingFxSink = {
  setWord: (t, m, n, now, mask) => {
    strip.setWord(t, m, n, now, mask);
    today.setWord?.(t, m, n, now, mask);
  },
  key: (i, now) => (mode === "new" ? strip.key(i, now) : today.key(i, now)),
  wrong: (i, now, key) => (mode === "new" ? strip.wrong(i, now, key) : today.wrong?.(i, now)),
  stray: (now) => strip.stray(now),
  back: (n, now) => strip.back(n, now),
  complete: (p, c, now) => (mode === "new" ? strip.complete(p, c, now) : today.complete?.(p, c, now)),
  clear: (now) => (mode === "new" ? strip.clear(now) : today.clear?.(now)),
};
const driver = new TypingFxDriver([look, sounds]);
const progress: TypingFxProgress = { kind: "show", word: 0, text: "", meaning: "", typed: 0, combo: 0 };

// ── Typing (the Lab's own tiny model; the games keep theirs) ─────────────
const gloss = (vi: string): string => (vi.split(";")[0] ?? vi).split(",").slice(0, 2).join(",").trim();

function push(kind: TypingFxProgress["kind"], now: number): void {
  progress.kind = kind;
  progress.word = wordSerial;
  progress.text = current.en;
  progress.meaning = gloss(current.vi);
  progress.typed = typed;
  progress.combo = combo;
  progress.perfect = kind === "done" ? errors === 0 : undefined;
  progress.key = kind === "wrong" ? lastKey : undefined;
  driver.progress(progress, now);
}

function showWord(word: { en: string; vi: string }, now = clock()): void {
  current = word;
  typed = 0;
  errors = 0;
  wordSerial += 1;
  push("show", now);
}

function nextWord(now = clock()): void {
  if (words.length === 0) return;
  wordIndex = (wordIndex + 1) % words.length;
  showWord(words[wordIndex]!, now);
}

const keyTimes: number[] = [];
let pendingKeyAt = -1;
const latency = { last: 0, max: 0, sum: 0, n: 0 };

let lastKey = "";

function type(letter: string, now = clock()): void {
  if (current.en === "") return;
  lastKey = letter;
  keyTimes.push(performance.now());
  if (typed < current.en.length && current.en[typed] === letter) {
    typed += 1;
    if (typed === current.en.length) {
      combo = errors === 0 ? combo + 1 : 0;
      push("done", now);
      // The next word arrives at once; the strip shows it after the release gap.
      nextWord(now);
    } else push(typed === 1 ? "lock" : "advance", now);
  } else {
    errors += 1;
    push("wrong", now);
  }
}

function backspace(now = clock()): void {
  if (typed === 0) return;
  typed -= 1;
  push("back", now);
  if (typed === 0) push("show", now);
}

window.addEventListener("keydown", (event) => {
  if (event.target instanceof HTMLElement && event.target.closest("select,input,button,.kit-keyboards")) return;
  if (event.metaKey || event.ctrlKey || event.altKey) return;
  if (event.key === "`") {
    togglePanel();
    return;
  }
  startAudio();
  if (event.key === "Backspace") {
    event.preventDefault();
    backspace();
    return;
  }
  if (/^[a-zA-Z]$/.test(event.key)) {
    event.preventDefault();
    pendingKeyAt = event.timeStamp;
    type(event.key.toLowerCase());
  }
});
window.addEventListener("pointerdown", () => startAudio(), { once: true });

// ── Bot ──────────────────────────────────────────────────────────────────
let botRate = 0;
let botNext = 0;
function botStep(now: number): void {
  if (botRate <= 0 || manual) return;
  const gap = 1000 / botRate;
  if (botNext < now - gap) botNext = now;
  // Catch up inside the frame: at 60 Hz, 15 keys a second is sometimes two keys in one frame.
  while (now >= botNext) {
    botNext += gap;
    const want = current.en[typed];
    if (want === undefined) return;
    type(Math.random() < 0.04 ? "q" : want, now);
  }
}

// ── Frame loop and readouts ──────────────────────────────────────────────
const frameTimes: number[] = [];
/** The strip's own work per frame (ms), the last 240 frames. */
const updateTimes: number[] = [];
let lastFrame = 0;
let lastReadout = 0;
const readouts = $<HTMLElement>("readouts");

function frame(t: number): void {
  if (pendingKeyAt >= 0) {
    const ms = t - pendingKeyAt;
    latency.last = ms;
    latency.max = Math.max(latency.max, ms);
    latency.sum += ms;
    latency.n += 1;
    pendingKeyAt = -1;
  }
  if (lastFrame > 0) {
    frameTimes.push(t - lastFrame);
    if (frameTimes.length > 240) frameTimes.shift();
  }
  lastFrame = t;
  botStep(performance.now());
  if (!manual) {
    const t0 = performance.now();
    strip.update(clock());
    updateTimes.push(performance.now() - t0);
    if (updateTimes.length > 240) updateTimes.shift();
  }
  if (t - lastReadout > 250) {
    lastReadout = t;
    renderReadouts();
  }
  requestAnimationFrame(frame);
}

function renderReadouts(): void {
  const now = performance.now();
  while (keyTimes.length > 0 && now - keyTimes[0]! > 1000) keyTimes.shift();
  const sorted = [...frameTimes].sort((a, b) => a - b);
  const mean = sorted.reduce((a, b) => a + b, 0) / Math.max(1, sorted.length);
  const p95 = sorted[Math.floor(sorted.length * 0.95)] ?? 0;
  const r = strip.readout();
  const heap = (performance as Performance & { memory?: { usedJSHeapSize: number } }).memory?.usedJSHeapSize;
  const rows: [string, string][] = [
    ["FPS", (1000 / Math.max(1, mean)).toFixed(0)],
    ["Frame p95", p95.toFixed(1) + " ms"],
    ["Strip update p95", ([...updateTimes].sort((a, b) => a - b)[Math.floor(updateTimes.length * 0.95)] ?? 0).toFixed(2) + " ms"],
    ["Particles", `${r.particles} / ${r.cap}`],
    ["Peak particles", String(strip.stats.maxParticles)],
    ["Flying letters", String(r.flying)],
    ["Voices", `${sounds.activeVoices()} (cut ${sounds.stolen})`],
    ["Keys / s", String(keyTimes.length)],
    ["Key → frame", latency.n ? `${latency.last.toFixed(1)} ms (max ${latency.max.toFixed(1)})` : "-"],
    ["Combo", String(combo)],
    ["Sound files", loadReport[settings.soundProfile] ?? "-"],
    ["JS heap", heap ? (heap / 1048576).toFixed(1) + " MB" : "-"],
  ];
  readouts.innerHTML = rows.map(([k, v]) => `<dt>${k}</dt><dd>${v}</dd>`).join("");
}

// ── Panel ────────────────────────────────────────────────────────────────
function segment<T extends string>(id: string, values: readonly T[], label: (v: T) => string, current: () => T, pick: (v: T) => void): void {
  const host = $<HTMLDivElement>(id);
  host.innerHTML = values.map((v) => `<button type="button" data-v="${v}">${label(v)}</button>`).join("");
  const sync = (): void => host.querySelectorAll("button").forEach((b) => b.classList.toggle("is-on", b.dataset.v === current()));
  host.addEventListener("click", (event) => {
    const button = (event.target as HTMLElement).closest("button");
    if (!button?.dataset.v) return;
    pick(button.dataset.v as T);
    sync();
    (button as HTMLButtonElement).blur();
  });
  sync();
}

segment<TypingFxStyle>("styles", TYPING_FX_STYLES, (v) => TYPING_FX_STYLE_NAMES[v], () => settings.style, (v) => {
  settings.style = v;
  strip.configure({ style: v });
});
segment<TypingFxIntensity>("intensity", TYPING_FX_INTENSITIES, (v) => TYPING_FX_INTENSITY_NAMES[v], () => settings.intensity, (v) => {
  settings.intensity = v;
  strip.configure({ intensity: v });
});
segment<TypingFxSize>("sizes", TYPING_FX_SIZES, (v) => TYPING_FX_SIZE_NAMES[v], () => settings.size, (v) => {
  settings.size = v;
  strip.configure({ size: v });
});
$<HTMLInputElement>("reduced").addEventListener("change", (event) => strip.setReducedMotion((event.target as HTMLInputElement).checked));

$<HTMLDivElement>("ab").addEventListener("click", (event) => {
  const button = (event.target as HTMLElement).closest("button");
  if (!button?.dataset.ab) return;
  mode = button.dataset.ab as "new" | "today";
  document.querySelectorAll<HTMLButtonElement>("#ab button").forEach((b) => b.classList.toggle("is-on", b === button));
  strip.el.style.visibility = mode === "new" ? "" : "hidden";
  showWord(current);
  button.blur();
});

const catalogueReady = (async () => {
  // No legacy five-pack fallback in the Lab: absence is visible, never mistaken for real media.
  const catalogue = await loadKeyboardCatalog(KEYS_BASE, { fallback: [] });
  keyboardOptions = catalogue.options;
  if (!keyboardOptions.some((p) => p.value === settings.soundProfile)) settings.soundProfile = keyboardOptions.find((p) => p.value !== "off")?.value ?? "off";
  profileNote.textContent = catalogue.state === "ready" ? "Hover or focus to hear one second. Choose a name to save; Listen previews only." : "Keyboard catalogue unavailable. Set LAB_KEYS to the ticket-189 staging folder and reload.";
  keyboardPicker = new KeyboardSoundChoices({
    document, options: keyboardOptions, label: "Keyboard sound",
    listenIcon: "/lab-keyboard-icon/hud-sound.64.png",
    onPreview: (choice, delay) => keyboardPreview.preview(choice, delay),
    onStop: () => keyboardPreview.stop(),
    onSelect: (choice) => { startAudio(); void useProfile(choice.value); },
  });
  profileHost.replaceChildren(keyboardPicker.element);
  keyboardPicker.sync(settings.soundProfile);
  await useProfile(settings.soundProfile, false);
})();

const volume = $<HTMLInputElement>("volume");
const volumeOut = $<HTMLElement>("volumeOut");
const setVolume = (): void => {
  settings.volume = Number(volume.value);
  sounds.setVolume(settings.volume);
  keyboardPreview.refreshVolume();
  volumeOut.textContent = Math.round(settings.volume * 100) + "%";
};
volume.addEventListener("input", setVolume);
setVolume();
const syncMaster = (): void => {
  const master = Number($<HTMLInputElement>("masterVolume").value);
  const muted = $<HTMLInputElement>("masterMuted").checked;
  sounds.muted = muted || master <= 0;
  sounds.setVolume(settings.volume * master);
  keyboardPreview.refreshVolume();
};
$<HTMLInputElement>("masterVolume").addEventListener("input", syncMaster);
$<HTMLInputElement>("masterMuted").addEventListener("change", syncMaster);
volume.addEventListener("input", syncMaster);

const gameSelect = $<HTMLSelectElement>("game");
const levelSelect = $<HTMLSelectElement>("level");
gameSelect.innerHTML = (Object.keys(GAMES) as GameId[]).map((id) => `<option value="${id}">${GAMES[id].name}</option>`).join("");
const fillLevels = (): void => {
  levelSelect.innerHTML = Array.from({ length: GAMES[gameId].levels }, (_, i) => `<option value="${i + 1}">Level ${i + 1}</option>`).join("");
};
gameSelect.addEventListener("change", () => {
  gameId = gameSelect.value as GameId;
  fillLevels();
  void setGame(gameId, 1);
});
levelSelect.addEventListener("change", () => void setGame(gameId, Number(levelSelect.value)));

$<HTMLButtonElement>("simWrong").addEventListener("click", () => {
  startAudio();
  errors += 1;
  push("wrong", clock());
});
$<HTMLButtonElement>("simPerfect").addEventListener("click", () => {
  startAudio();
  errors = 0;
  const rest = current.en.slice(typed);
  [...rest].forEach((ch, i) => setTimeout(() => type(ch), i * 66));
});
const comboTo = (n: number): void => {
  startAudio();
  combo = n - 1;
  errors = 0;
  const rest = current.en.slice(typed);
  [...rest].forEach((ch, i) => setTimeout(() => type(ch), i * 66));
};
$<HTMLButtonElement>("simCombo10").addEventListener("click", () => comboTo(10));
$<HTMLButtonElement>("simCombo25").addEventListener("click", () => comboTo(25));
$<HTMLButtonElement>("simSkip").addEventListener("click", () => {
  push("release", clock());
  nextWord();
});
$<HTMLDivElement>("bot").addEventListener("click", (event) => {
  const button = (event.target as HTMLElement).closest("button");
  if (!button?.dataset.bot) return;
  startAudio();
  botRate = Number(button.dataset.bot);
  document.querySelectorAll<HTMLButtonElement>("#bot button").forEach((b) => b.classList.toggle("is-on", b === button));
  button.blur();
});

function togglePanel(force?: boolean): void {
  const hidden = force ?? !panel.classList.contains("is-hidden");
  panel.classList.toggle("is-hidden", hidden);
  if (hidden) keyboardPreview.stop();
  else keyboardPicker?.sync(settings.soundProfile);
  $<HTMLButtonElement>("collapse").textContent = hidden ? "Show" : "Hide";
}
$<HTMLButtonElement>("collapse").addEventListener("click", () => togglePanel());

// ── Game and vocabulary ──────────────────────────────────────────────────
async function setGame(id: GameId, level: number): Promise<void> {
  gameId = id;
  const game = GAMES[id];
  backdrop.src = game.backdrop;
  await backdrop.decode().catch(() => undefined);
  strip.setPalette({ accent: game.accent });
  strip.setAnchor(0.5, game.anchorY);
  const response = await fetch(`/lab-vocab/${id}/levels/${String(level).padStart(3, "0")}.json`);
  const data = (await response.json()) as { entries: { en: string; vi: string }[] };
  words = data.entries.filter((e) => /^[a-z]{3,10}$/.test(e.en));
  // A fixed shuffle, so a session and a capture see the same words.
  let seed = 1 + level;
  for (let i = words.length - 1; i > 0; i -= 1) {
    seed = (seed * 16807) % 2147483647;
    const j = seed % (i + 1);
    [words[i], words[j]] = [words[j]!, words[i]!];
  }
  wordIndex = 0;
  showWord(words[0]!);
}

// ── Capture API (the frame-sequence script drives the Lab through this) ──
const ready = (async () => {
  fillLevels();
  await setGame(gameId, 1);
  await catalogueReady;
  await document.fonts.ready;
  strip.layout();
  showWord(current);
})();

Object.assign(window, {
  __lab: {
    ready,
    strip,
    sounds,
    configure(next: Partial<TypingFxSettings>) {
      Object.assign(settings, next);
      strip.configure(next);
    },
    async game(id: GameId, level = 1) {
      gameSelect.value = id;
      fillLevels();
      await setGame(id, level);
      strip.layout();
    },
    freeze() {
      virtualNow = 100000;
      manual = true;
      botRate = 0;
      strip.reset();
      strip.update(virtualNow);
    },
    at(ms: number) {
      virtualNow = ms;
      strip.update(ms);
    },
    word(en: string, vi: string) {
      showWord({ en, vi }, clock());
      strip.update(clock());
    },
    press(letter: string) {
      type(letter, clock());
    },
    setCombo(n: number) {
      combo = n;
    },
    reduced(on: boolean) {
      strip.setReducedMotion(on);
    },
    panel(show: boolean) {
      togglePanel(!show);
    },
    target() {
      const pt = { x: 0, y: 0 };
      targetPoint(pt);
      return pt;
    },
    stats: () => ({ updateP95: [...updateTimes].sort((a, b) => a - b)[Math.floor(updateTimes.length * 0.95)] ?? 0, updateMax: Math.max(0, ...updateTimes), ...strip.stats, ...strip.readout(), voices: sounds.activeVoices(), latency: { ...latency, mean: latency.n ? latency.sum / latency.n : 0 }, frameP95: [...frameTimes].sort((a, b) => a - b)[Math.floor(frameTimes.length * 0.95)] ?? 0, frames: frameTimes.length, meanFrame: frameTimes.reduce((a, b) => a + b, 0) / Math.max(1, frameTimes.length), heap: (performance as Performance & { memory?: { usedJSHeapSize: number } }).memory?.usedJSHeapSize ?? 0 }),
    /** The current word's rest and the next `n` words (for typing tests). */
    upcoming(n = 5) {
      const next = Array.from({ length: n }, (_, i) => words[(wordIndex + 1 + i) % words.length]!.en);
      return [current.en.slice(typed), ...next];
    },
    bot(rate: number) {
      botRate = rate;
    },
    profile: (id: string) => useProfile(id),
    loadReport,
  },
});

window.addEventListener("pagehide", () => keyboardPreview.stop());
requestAnimationFrame(frame);
