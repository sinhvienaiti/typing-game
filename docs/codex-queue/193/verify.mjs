// Isolated ticket check: filesystem fetch, simulated DOM and WebAudio; no server or browser.
import assert from 'node:assert/strict';
import { readFile, readdir } from 'node:fs/promises';
import { resolve, dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
const root = resolve(dirname(fileURLToPath(import.meta.url)), '../../..');
const { Window } = await import('/Users/toandx/htdocs/typing-game/shared/game-kit/node_modules/happy-dom/lib/index.js');
const win = new Window({ url: 'http://local.invalid/' });
for (const key of ['window', 'document', 'localStorage', 'sessionStorage', 'HTMLElement', 'Element', 'Node', 'Event', 'CustomEvent', 'KeyboardEvent', 'PointerEvent', 'MutationObserver', 'getComputedStyle']) globalThis[key] = key === 'window' ? win : typeof win[key] === 'function' && key === 'getComputedStyle' ? win[key].bind(win) : win[key];
const fetched = [], started = [], nodes = [], byteUrls = new WeakMap();
const tick = (ms = 0) => new Promise((done) => setTimeout(done, ms));
globalThis.fetch = async (url) => {
  const path = String(url);
  assert(path.startsWith('/assets/typing-defense/'), 'only local game assets');
  fetched.push(path);
  const bytes = await readFile(join(root, 'public', path));
  return { ok: true, json: async () => JSON.parse(bytes), arrayBuffer: async () => {
    const result = bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
    byteUrls.set(result, path); return result;
  } };
};
class Param {
  value = 1;
  setValueAtTime(v) { this.value = v; }
  setTargetAtTime(v) { this.value = v; }
  exponentialRampToValueAtTime(v) { this.value = v; }
  linearRampToValueAtTime(v) { this.value = v; }
  cancelScheduledValues() {}
}
class AudioNode {
  constructor(ctx, options = {}) { this.context = ctx; Object.assign(this, options); this.outputs = []; nodes.push(this); }
  connect(node) { this.outputs.push(node); return node; }
  disconnect() { this.outputs = []; }
}
class Gain extends AudioNode { constructor(ctx, options = {}) { super(ctx); this.gain = new Param(); this.gain.value = options.gain ?? 1; } }
class Source extends AudioNode {
  start(...args) { this.startArgs = args; started.push(this); }
  stop(at) { this.stopAt = at; }
}
class Tone extends Source { frequency = new Param(); }
class Filter extends AudioNode { frequency = new Param(); Q = new Param(); }
class Context {
  currentTime = 0; state = 'running'; sampleRate = 48000;
  destination = new AudioNode(this);
  resume() { this.state = 'running'; return Promise.resolve(); }
  createGain() { return new Gain(this); }
  createBufferSource() { return new Source(this); }
  decodeAudioData(bytes) { return Promise.resolve({ duration: 1, url: byteUrls.get(bytes) }); }
  createBuffer(channels, frames) { return { sampleRate: 48000, getChannelData: () => new Float32Array(frames) }; }
}
Object.assign(globalThis, { AudioContext: Context, GainNode: Gain, AudioBufferSourceNode: Source, DynamicsCompressorNode: AudioNode, ConvolverNode: AudioNode, OscillatorNode: Tone, BiquadFilterNode: Filter, StereoPannerNode: AudioNode });
const { mountQuick, settingsRows, soundRows, applyQuick } = await import('../../../src/app/quick.ts');
const { loadSettings, DEFAULT_KEYBOARD_SOUND, BUILT_IN_KEYS } = await import('../../../src/app/prefs.ts');
const { TypingAudio } = await import('../../../src/view/audio-min.ts');
const { installKeys } = await import('../../../src/app/input.ts');
const { compileDeck } = await import('../../../src/typing/decks.ts');
const { Session } = await import('../../../src/app/session.ts');
const { hashHex } = await import('../../../src/sim/hash.ts');
const { loadKeyboardCatalog, keyboardFiles } = await import('../../../src/kit/feedback/typing-fx/audio.ts');
let checks = 0;
const check = (condition, message) => { assert(condition, message); checks++; };
const settings = loadSettings();
check(DEFAULT_KEYBOARD_SOUND === 'bright-clack' && settings.keyboard === 'bright-clack', 'owner-selected Bright Clack default');
check(!settingsRows().some((r) => /quality|fxStyle|learnIpa/.test(r.id)), 'no unsupported settings');
check(!soundRows([]).some((r) => r.id === 'voice'), 'no nonfunctional Voice row');
check(!applyQuick(settings, 'master', NaN) && !applyQuick(settings, 'mode', 'wrong'), 'reject bad values');
const catalog = await loadKeyboardCatalog('/assets/typing-defense/audio/keys/', { fallback: [] });
assert.deepEqual(catalog.options.map((c) => c.value), ['off', 'deep', 'warm', 'rounded', 'solid', 'crisp', 'clear', 'bright-clack']); checks++;
for (const choice of catalog.options.slice(1)) {
  const manifest = JSON.parse(await readFile(join(root, 'public', choice.manifest), 'utf8'));
  const files = keyboardFiles(manifest, choice.manifest.slice(0, choice.manifest.lastIndexOf('/') + 1));
  check(files.key.length === 10 && files.space.length === 3, choice.value + ': 13 samples');
  for (const file of [...files.key, ...files.space, choice.preview]) check(file.endsWith('.ogg') && (await readFile(join(root, 'public', file))).length > 0, 'staged OGG ' + file);
  check(!(await readdir(join(root, 'public/assets/typing-defense/audio/keys', choice.value))).some((p) => p.endsWith('.wav')), 'no WAV in ' + choice.value);
}
const audio = new TypingAudio(settings);
const notices = [];
let titleUp = false, priorPause = false, quit = 0;
let quick;
// Same ordering as main.ts: page capture is registered before the lazy overlay.
win.addEventListener('keydown', (event) => {
  if (quick?.blocking || event.code === 'F1' || event.code === 'F2') return;
  if (titleUp) { event.preventDefault(); event.stopImmediatePropagation(); }
}, true);
quick = await mountQuick(settings, { audio: () => audio, quit: () => { titleUp = true; quit++; }, countdown: () => titleUp || priorPause ? 0 : 5, notice: (s) => notices.push(s) });
audio.resume();
const deck = compileDeck(['apple', 'book', 'cat', 'bird', 'house', 'door', 'flower'].map((text, i) => ({ id: '' + i, text, level: 1 })));
const session = new Session({ seed: 1, sandbox: true, deck });
const actions = [];
const sent = [];
installKeys(win, { send: (command) => { if (titleUp || priorPause || quick.blocking) return false; sent.push(command); session.send(command); return true; }, act: (action) => actions.push(action), onVietnamese() {}, allowUntrusted: true, blocked: () => titleUp || quick.blocking, typed: (space, native) => quick.typed(space, native) });
const press = (key, code, target = document.body) => target.dispatchEvent(new win.KeyboardEvent('keydown', { key, code, bubbles: true, cancelable: true }));
const frame = (now) => { session.paused = priorPause || titleUp || quick.blocking; session.frame(now); };
const click = (selector) => { const el = quick.root.querySelector(selector); assert(el, selector); el.click(); return el; };
const slider = (id, value) => { const el = quick.root.querySelector(`[data-row="${id}"] input`); el.value = '' + value; el.dispatchEvent(new win.Event('input', { bubbles: true })); };
const settle = async () => { for (let i = 0; i < 12; i++) await tick(2); };
await settle();
check(!notices.length, 'all initial media loaded');
check(quick.root.querySelectorAll('.kit-qs__corner img').length === 2, 'both real-art corners');
for (const onTitle of [true, false]) for (const panel of ['settings', 'sound']) {
  titleUp = onTitle;
  click(`.kit-qs__corner[data-panel="${panel}"]`);
  check(quick.panel === panel && quick.blocking, 'mouse open ' + panel);
  press('Escape', 'Escape'); await settle();
  check(!quick.blocking, 'Escape closes ' + panel);
  press(panel === 'settings' ? 'F1' : 'F2', panel === 'settings' ? 'F1' : 'F2');
  check(quick.panel === panel, 'shortcut opens ' + panel + ' over title=' + onTitle);
  click(`.kit-qs__dialog[data-panel="${panel}"] .kit-qs__close`); await settle();
  check(!quick.blocking, 'mouse close ' + panel);
}
titleUp = false;
frame(0); frame(20);
const before = hashHex(session.world), beforeTick = session.world.tick, beforeLog = session.log.length;
press('F2', 'F2');
press('a', 'KeyA'); press(' ', 'Space'); press('Backspace', 'Backspace'); frame(40);
check(hashHex(session.world) === before && session.world.tick === beforeTick && session.log.length === beforeLog, 'panel freezes hash, tick, log and typing');
slider('master', 50); slider('keyboardVolume', 80); slider('effects', 0);
slider('music', 40); slider('ui', 30);
check(loadSettings().master === 50 && loadSettings().keyboardVolume === 80 && loadSettings().sfx === 0 && loadSettings().music === 40 && loadSettings().ui === 30, 'save every volume change immediately');
check(Math.abs(audio.master.gain.value - .25) < 1e-9 && Math.abs(audio.musicBus.gain.value - .16) < 1e-9 && Math.abs(audio.uiBus.gain.value - .126) < 1e-9, 'existing music/effects mix preserved and Interface independent');
const sample = quick.root.querySelector('.kit-keyboards__option[data-value="warm"]');
sample.dispatchEvent(new win.PointerEvent('pointerenter', { pointerType: 'mouse' }));
const hoverBefore = started.length; await tick(180);
check(started.length > hoverBefore && started.at(-1).buffer.url.endsWith('/warm/preview.ogg'), 'hover fetches correct pack preview');
check(started.at(-1).startArgs[2] === 1 && started.at(-1).stopAt === started.at(-1).startArgs[0] + 1, 'preview exactly one second');
check(started.at(-1).outputs[0].gain.value === .4, 'preview Master × Keyboard = 0.4');
sample.dispatchEvent(new win.PointerEvent('pointerleave', { pointerType: 'mouse' }));
check(started.at(-1).stopAt <= .031, 'leaving fades preview');
sample.click(); await settle();
check(loadSettings().keyboard === 'warm', 'selection saved');
const countBefore = started.length;
press('Escape', 'Escape');
check(quick.blocking && quick.root.querySelector('.kit-qs__digit').textContent === '3', '3 countdown blocks input');
press('z', 'KeyZ'); frame(60);
check(session.world.tick === beforeTick && started.length === countBefore, 'countdown blocks sim and key sound');
await tick(6); check(quick.root.querySelector('.kit-qs__digit').textContent === '2', '2 countdown');
await tick(6); check(quick.root.querySelector('.kit-qs__digit').textContent === '1', '1 countdown');
await tick(8); check(!quick.blocking, 'countdown releases');
quick.wake();
press('a', 'KeyA');
check(started.at(-1).buffer.url.includes('/warm/key-'), 'C10 plays selected key sample with Effects zero');
check(started.at(-1).outputs[0].outputs[0].gain.value === .4, 'gameplay Master × Keyboard = 0.4');
press(' ', 'Space'); check(started.at(-1).buffer.url.includes('/warm/space-'), 'space uses space set');
press('Backspace', 'Backspace'); check(started.at(-1).buffer.url.includes('/warm/key-'), 'backspace uses key set');
for (const tag of ['input', 'textarea', 'div']) {
  const native = document.createElement(tag);
  if (tag === 'input') native.type = 'text';
  if (tag === 'div') native.setAttribute('contenteditable', '');
  document.body.append(native);
  const logBefore = sent.length, soundsBefore = started.length;
  press('b', 'KeyB', native); press(' ', 'Space', native); press('Backspace', 'Backspace', native);
  check(started.length === soundsBefore + 3 && started.at(-1).buffer.url.includes('/warm/key-'), tag + ': native typing, space and backspace play chosen pack');
  check(sent.length === logBefore, tag + ': native text does not reach C10');
  native.remove();
}
const focusWarm = quick.root.querySelector('.kit-keyboards__option[data-value="warm"]');
press('F2', 'F2');
const focusBefore = started.length;
focusWarm.focus();
await tick(180);
check(started.length > focusBefore && started.at(-1).buffer.url.endsWith('/warm/preview.ogg'), 'keyboard focus previews the right pack');
press('Escape', 'Escape'); await settle();
press('F2', 'F2');
click('.kit-keyboards__option[data-value="off"]');
press('Escape', 'Escape'); await settle();
const offBefore = started.length; press('c', 'KeyC'); quick.typed(true);
check(started.length === offBefore, 'Off schedules no keyboard audio');
press('F2', 'F2'); click('.kit-keyboards__option[data-value="deep"]'); await settle();
click('[data-toggle="muted"]');
check(settings.muted && quick.root.querySelector('.kit-qs__corner[data-panel="sound"] img').src.includes('hud-sound-muted'), 'mute persists and switches art');
press('Escape', 'Escape'); await settle();
const muteBefore = started.length; press('c', 'KeyC');
check(started.length === muteBefore && loadSettings().muted, 'muted schedules no key');
press('F2', 'F2'); click('[data-toggle="muted"]'); slider('master', 0);
press('Escape', 'Escape'); await settle();
const zeroBefore = started.length; press('d', 'KeyD');
check(started.length === zeroBefore, 'Master zero schedules no key');
press('F2', 'F2'); slider('master', 50); click('.kit-keyboards__option[data-value="bamboo"]');
press('Escape', 'Escape'); await settle();
const bambooBefore = started.length; audio.key();
check(started.length > bambooBefore && settings.keyboard === BUILT_IN_KEYS, 'original Bamboo remains playable');
check(audio.keyBus.gain.value === .4 && audio.sfx.gain.value === 0, 'original keys independent of Effects');
settings.master = 0; audio.apply(settings);
const bambooZero = started.length; audio.key();
check(started.length === bambooZero, 'Master zero schedules no original Bamboo key');
settings.master = 50; audio.apply(settings);
press('F1', 'F1'); click('[data-row="pace"] button'); click('input[value="learn"]');
check(!loadSettings().pace && loadSettings().mode === 'learn', 'real game options save');
press('Escape', 'Escape'); await settle();
priorPause = true; press('F1', 'F1'); press('Escape', 'Escape');
check(!quick.blocking && priorPause, 'existing pause retained without new countdown');
priorPause = false; press('F1', 'F1'); click('[data-action="quit"]');
check(quit === 1 && titleUp && !quick.blocking, 'Quit returns to title without countdown');
check(!fetched.some((p) => p.endsWith('.wav')), 'no WAV requested');
quick.destroy(); win.happyDOM.cancelAsync();
// A removed pack falls back to the first available pack; an explicit Off survives.
for (const [saved, wanted] of [['removed-pack', 'deep'], ['off', 'off']]) {
  settings.keyboard = saved;
  quick = await mountQuick(settings, { audio: () => audio, quit() {}, countdown: () => 0, notice: (s) => notices.push(s) });
  await settle();
  check(settings.keyboard === wanted, saved + ': correct catalogue fallback');
  quick.destroy();
}
// Compare a paused presentation run to a control at the same simulation ticks.
const control = new Session({ seed: 9, sandbox: true, deck });
const presented = new Session({ seed: 9, sandbox: true, deck });
for (let t = 0; t < 100; t++) {
  if (t % 13 === 0) for (const run of [control, presented]) run.send({ t: 'key', letter: t % 26, atMs: t * 20 });
  if (t === 30) {
    const pausedHash = hashHex(presented.world);
    presented.paused = true;
    for (let frame = 0; frame < 10; frame++) presented.frame(frame * 20);
    check(hashHex(presented.world) === pausedHash, 'presentation pause leaves deterministic state untouched');
    presented.paused = false;
  }
  control.tick(); presented.tick();
}
check(hashHex(control.world) === hashHex(presented.world), 'same commands and ticks retain the same match hash');
assert.deepEqual(control.log, presented.log); checks++;
console.log(JSON.stringify({ checks, catalog: catalog.options.map((c) => c.label), samples: 91, previews: 7, fetched: fetched.length, notices, result: 'PASS', limits: 'Simulated DOM/audio; no layout, acoustic or full-game suite claim.' }, null, 2));
