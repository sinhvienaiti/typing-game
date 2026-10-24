"use strict";
/* Listening Board client (AUDIO_PIPELINE.md §7).
   Blind: the page only knows labels A, B, C...; file names, roles and scores stay on the server.
   Loudness: every file plays at the gain the server measured, so louder never wins.
   Keyboard first; all text for the owner is Vietnamese. */

// ------------------------------------------------------------------ helpers
function h(tag, attrs, ...kids) {
  const el = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (v === undefined || v === null || v === false) continue;
    if (k === "class") el.className = v;
    else if (k === "text") el.textContent = v;
    else if (k.startsWith("on")) el.addEventListener(k.slice(2), v);
    else if (k === "data") for (const [dk, dv] of Object.entries(v)) el.dataset[dk] = dv;
    else el.setAttribute(k, v === true ? "" : String(v));
  }
  for (const kid of kids.flat(Infinity)) {
    if (kid === null || kid === undefined || kid === false) continue;
    el.append(kid instanceof Node ? kid : String(kid));
  }
  return el;
}
const kbd = (t) => h("kbd", {}, t);
const enc = encodeURIComponent;
const fmt = (v, digits = 1) => Number(v).toLocaleString("vi-VN", { maximumFractionDigits: digits }).replace("-", "−");
const signed = (v) => (v > 0 ? "+" : v < 0 ? "−" : "±") + fmt(Math.abs(v), 1);
const clock = (ms) => {
  const s = Math.floor(ms / 1000);
  return String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0");
};
// Seeded random (FNV-1a hash -> mulberry32): the loop pattern is the same for every candidate.
function rng(seedText) {
  let a = 2166136261 >>> 0;
  for (let i = 0; i < seedText.length; i++) a = Math.imul(a ^ seedText.charCodeAt(i), 16777619) >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const api = {
  async get(path) {
    const r = await fetch(path, { cache: "no-store" });
    const j = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(j.error || r.statusText);
    return j;
  },
  async post(path, body) {
    const r = await fetch(path, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
    const j = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(j.error || r.statusText);
    return j;
  },
};

// ------------------------------------------------------------------ state
const S = {
  cfg: null, list: null, sess: null,
  phase: "boot",          // list | start | item | done
  idx: 0, sel: 0, ctx: "alone", device: null,
  drafts: {}, reveals: {},
  overlay: null, image: null,
  msg: null,
  elapsedBase: 0, elapsedMark: null, itemMark: null,
  warnedLong: false, saving: false,
};
const app = () => document.getElementById("app");
const cur = () => S.sess.items[S.idx];
const nCands = () => cur().candidates.length;
const tagByCode = () => Object.fromEntries(S.cfg.tags.map((t) => [t.code, t.name]));

function elapsed() { return S.elapsedBase + (S.elapsedMark ? performance.now() - S.elapsedMark : 0); }
function runTimer(on) {
  if (on && S.elapsedMark === null) S.elapsedMark = performance.now();
  if (!on && S.elapsedMark !== null) { S.elapsedBase += performance.now() - S.elapsedMark; S.elapsedMark = null; }
}
function itemTime(stop) {
  const d = S.sess && S.phase === "item" ? draft(cur()) : null;
  if (d && S.itemMark !== null) { d.ms += performance.now() - S.itemMark; S.itemMark = stop ? null : performance.now(); }
  return d ? d.ms : 0;
}

function draft(it) {
  let d = S.drafts[it.key];
  if (!d) {
    const r = it.rating || {};
    const tags = {};
    for (const [k, v] of Object.entries(r.tags || {})) tags[k] = [...v];
    d = {
      stars: { ...(r.stars || {}) }, tags, pick: r.pick || null, pickAuto: !!r.pickAuto, none: !!r.none,
      note: r.note || "", dropped: new Set(r.dropped || []), listens: {}, heard: new Set(), ms: 0, dirty: false,
    };
    S.drafts[it.key] = d;
  }
  return d;
}

function say(text, kind = "") { S.msg = text ? { text, kind } : null; renderStatus(); }

// ------------------------------------------------------------------ audio
const AU = { ctx: null, master: null, buffers: new Map(), pending: new Map(), live: new Set(), play: null, raf: 0, token: 0 };

function audioCtx() {
  if (!AU.ctx) {
    const C = window.AudioContext || window.webkitAudioContext;
    AU.ctx = new C({ latencyHint: "interactive" });
    AU.master = AU.ctx.createGain();
    // Same safety limiter for every candidate; gains already keep single plays under -1 dBTP.
    const lim = AU.ctx.createDynamicsCompressor();
    lim.threshold.value = -1; lim.knee.value = 0; lim.ratio.value = 20; lim.attack.value = 0.002; lim.release.value = 0.08;
    AU.master.connect(lim).connect(AU.ctx.destination);
  }
  if (AU.ctx.state === "suspended") AU.ctx.resume().catch(() => {});
  return AU.ctx;
}
function audioUrl(it, label, n) { return `/api/audio/${enc(S.sess.session)}/${enc(it.key)}/${label}/${n}`; }
function ctxUrl(it, label, key) { return `/api/ctx/${enc(S.sess.session)}/${enc(it.key)}/${label}/${enc(key)}`; }
// A rendered context (scene, burst) plays a file made for each candidate; only items that have one offer it.
function ctxInfo(key) { return S.cfg.contexts.find((x) => x.key === key); }
function isRendered(key) { const c = ctxInfo(key); return !!(c && c.rendered); }
function available(it, c) { return !!c && c.enabled && (!c.rendered || (it && (it.rendered || []).includes(c.key))); }
function buffer(it, label, n, url) {
  url = url || audioUrl(it, label, n);
  if (AU.buffers.has(url)) return Promise.resolve(AU.buffers.get(url));
  if (!AU.pending.has(url)) {
    const p = fetch(url)
      .then((r) => { if (!r.ok) throw new Error("không tải được âm (" + r.status + ")"); return r.arrayBuffer(); })
      .then((b) => audioCtx().decodeAudioData(b))
      .then((buf) => { AU.buffers.set(url, buf); return buf; })
      .finally(() => AU.pending.delete(url));
    AU.pending.set(url, p);
  }
  return AU.pending.get(url);
}
function preload(it) {
  if (!it) return;
  for (const c of it.candidates) c.files.forEach((_, n) => buffer(it, c.label, n).catch(() => {}));
}
// Playing = scheduled sound not yet over (does not rely on animation frames running).
function isPlaying(label) {
  const p = AU.play;
  if (!p || !AU.ctx || AU.ctx.currentTime > p.t0 + p.dur + 0.05) return false;
  return label === undefined || p.label === label;
}
function stopAudio() {
  AU.token++;
  for (const s of AU.live) { try { s.stop(); } catch (_) { /* already stopped */ } }
  AU.live.clear();
  AU.play = null;
  cancelAnimationFrame(AU.raf);
  paintPlayback();
}
function output(ctxKey) {
  const c = audioCtx();
  if (ctxKey !== "small") return AU.master;
  const hp = c.createBiquadFilter();       // small speaker: high-pass 200 Hz (§2, §6.1 F)
  hp.type = "highpass"; hp.frequency.value = S.cfg.smallSpeakerHz; hp.Q.value = Math.SQRT1_2;
  hp.connect(AU.master);
  return hp;
}
function source(buf, out, when, rate, gainDb) {
  const c = AU.ctx;
  const src = c.createBufferSource();
  src.buffer = buf;
  src.playbackRate.value = rate;
  const g = c.createGain();
  g.gain.value = Math.pow(10, gainDb / 20);
  src.connect(g).connect(out);
  src.start(when);
  AU.live.add(src);
  src.onended = () => AU.live.delete(src);
  return src;
}

async function play(pos, { set = false, once = false } = {}) {
  const it = cur(), d = draft(it);
  const cand = it.candidates[pos];
  stopAudio();
  const token = AU.token;
  audioCtx();
  const ctxKey = S.ctx;
  d.heard.add(ctxKey);
  if (cand) d.listens[cand.label] = (d.listens[cand.label] || 0) + 1;
  const out = output(ctxKey);
  try {
    if (isRendered(ctxKey)) await playRendered(it, cand, ctxKey, out, token);
    else if (ctxKey === "loop" && !once) await playLoop(it, set ? null : cand, out, token);
    else await playOnce(it, cand, out, token);
  } catch (err) {
    say(err.message, "err");
  }
  renderCards();
}
async function playOnce(it, cand, out, token) {
  const n = (cand._next = ((cand._next ?? -1) + 1) % cand.files.length);   // rotate variants
  const buf = await buffer(it, cand.label, n);
  if (token !== AU.token) return;
  const t0 = AU.ctx.currentTime + 0.03;
  source(buf, out, t0, 1, cand.files[n].gainDb);
  AU.play = { label: cand.label, kind: "once", t0, dur: buf.duration, n, of: cand.files.length, events: [] };
  animate();
}
async function playRendered(it, cand, key, out, token) {
  if (!cand) { say("Chọn một bản để nghe bản dựng.", "warn"); return; }
  const buf = await buffer(it, cand.label, 0, ctxUrl(it, cand.label, key));
  if (token !== AU.token) return;
  const t0 = AU.ctx.currentTime + 0.03;
  source(buf, out, t0, 1, 0);          // renders of one item share one level, set when they were made
  AU.play = { label: cand.label, kind: "once", t0, dur: buf.duration, n: 0, of: 1, events: [] };
  animate();
}
async function playLoop(it, cand, out, token) {
  const d = draft(it), p = it.loop;
  const pool = [];
  const add = (c) => c.files.forEach((f, n) => pool.push({ label: c.label, n, gainDb: f.gainDb }));
  if (cand) add(cand); else it.candidates.filter((c) => !d.dropped.has(c.label)).forEach(add);
  if (!pool.length) { say("Không còn bản nào để lặp.", "warn"); return; }
  const bufs = await Promise.all(pool.map((v) => buffer(it, v.label, v.n)));
  if (token !== AU.token) return;
  const t0 = AU.ctx.currentTime + 0.05;
  const count = p.count || 20;
  if (p.seamless) {          // beds: back to back, sample exact, to hear the seam
    const src = source(bufs[0], out, t0, 1, pool[0].gainDb);
    src.loop = true;
    src.stop(t0 + bufs[0].duration * count);
    AU.play = { label: pool[0].label, kind: "seamless", t0, dur: bufs[0].duration * count, period: bufs[0].duration, count, events: [] };
    animate();
    return;
  }
  const rt = rng(`${S.sess.session}:${it.key}:loop`);      // timing, pitch, level: same for all candidates
  const rv = rng(`${S.sess.session}:${it.key}:variant`);   // which variant plays
  const avoid = Math.max(0, Math.min(p.avoid ?? 2, pool.length - 1));
  const gap = (p.gap_ms ?? 30) / 1000;
  const recent = [], events = [];
  let t = t0, last = -1;
  for (let i = 0; i < count; i++) {
    const cents = (rt() * 2 - 1) * (p.cents || 0);
    const db = (rt() * 2 - 1) * (p.db || 0);
    const off = (rt() * (p.offset_ms || 0)) / 1000;
    const step = (p.interval_ms / 1000) * (1 + (p.jitter || 0) * (rt() * 2 - 1));
    let k = Math.floor(rv() * pool.length);
    for (let guard = 0; recent.includes(k) && guard < 50; guard++) k = Math.floor(rv() * pool.length);
    recent.push(k);
    if (recent.length > avoid) recent.shift();
    let when = t + off;
    if (last >= 0 && when - last < gap) when = last + gap;
    source(bufs[k], out, when, Math.pow(2, cents / 1200), pool[k].gainDb + db);
    events.push({ when, label: pool[k].label, dur: bufs[k].duration / Math.pow(2, cents / 1200) });
    last = when;
    t += step;
  }
  const end = Math.max(...events.map((e) => e.when + e.dur));
  AU.play = { label: cand ? cand.label : null, kind: "loop", t0, dur: end - t0, count, events };
  animate();
}
function animate() {
  cancelAnimationFrame(AU.raf);
  const step = () => {
    const p = AU.play;
    if (!p) return paintPlayback();
    const now = AU.ctx.currentTime;
    if (now > p.t0 + p.dur + 0.05) { AU.play = null; paintPlayback(); return; }
    paintPlayback(now);
    AU.raf = requestAnimationFrame(step);
  };
  AU.raf = requestAnimationFrame(step);
}
function paintPlayback(now) {
  const p = AU.play;
  let sounding = null, played = 0;
  if (p && now !== undefined) {
    for (const e of p.events) if (e.when <= now) { played++; sounding = e.label; }
    if (p.kind === "seamless") played = Math.min(p.count, Math.floor((now - p.t0) / p.period) + 1);
  }
  document.querySelectorAll(".card").forEach((card) => {
    const label = card.dataset.label;
    const mine = p && (p.label === label || (p.label === null && p.events.some((e) => e.label === label)));
    card.classList.toggle("playing", !!(p && p.label === label));
    card.classList.toggle("sounding", !!(p && p.label === null && sounding === label));
    const fill = card.querySelector(".track i");
    const time = card.querySelector(".ptime");
    const btn = card.querySelector(".play");
    if (btn) btn.textContent = p && p.label === label ? "■" : "▶";
    if (!fill || !time) return;
    if (!mine || now === undefined) {
      fill.style.width = "0%";
      time.textContent = card.dataset.dur || "";
      return;
    }
    const frac = Math.max(0, Math.min(1, (now - p.t0) / p.dur));
    fill.style.width = (frac * 100).toFixed(1) + "%";
    if (p.kind === "once") time.textContent = fmt(Math.max(0, now - p.t0), 2) + " s" + (p.of > 1 ? ` · bản ${p.n + 1}/${p.of}` : "");
    else time.textContent = `Lặp ${Math.max(1, played)}/${p.count}`;
  });
}

// ------------------------------------------------------------------ rating logic
function autoPick(it, d) {
  if (d.none || (d.pick && !d.pickAuto)) return;
  const labels = it.candidates.map((c) => c.label);
  d.pick = null; d.pickAuto = false;
  if (labels.length < 2 || it.mode === "variants" || !labels.every((l) => d.stars[l])) return;
  const best = Math.max(...labels.map((l) => d.stars[l]));
  const top = labels.filter((l) => d.stars[l] === best);
  if (top.length === 1) { d.pick = top[0]; d.pickAuto = true; }
}
function missing(it, d) {
  const out = [];
  if (it.mode === "variants") return out;
  const noStars = it.candidates.map((c) => c.label).filter((l) => !d.stars[l]);
  if (noStars.length) out.push("còn thiếu sao cho " + noStars.join(", ") + " (⇧1–5)");
  if (it.candidates.length > 1 && !d.pick && !d.none) out.push("chọn bản tốt nhất (V) hoặc bấm 0 nếu không bản nào đạt");
  return out;
}
function touch(it, d) { d.dirty = true; autoPick(it, d); renderCards(); renderPalette(); renderActions(); }
function selected() { return cur().candidates[S.sel]; }
function setStars(n) {
  const it = cur(), d = draft(it), c = selected();
  if (n === 0) delete d.stars[c.label]; else d.stars[c.label] = n;
  touch(it, d);
}
function toggleTag(name) {
  const it = cur(), d = draft(it), c = selected();
  const list = d.tags[c.label] || (d.tags[c.label] = []);
  const i = list.indexOf(name);
  if (i >= 0) list.splice(i, 1); else list.push(name);
  touch(it, d);
}
function togglePick() {
  const it = cur(), d = draft(it), c = selected();
  if (it.mode === "variants" || it.candidates.length < 2) return;
  if (d.pick === c.label && !d.pickAuto) { d.pick = null; d.pickAuto = false; }
  else { d.pick = c.label; d.pickAuto = false; d.none = false; }
  touch(it, d);
}
function toggleNone() {
  const it = cur(), d = draft(it);
  if (it.mode === "variants") return;
  d.none = !d.none;
  if (d.none) { d.pick = null; d.pickAuto = false; }
  touch(it, d);
}
function toggleDrop() {
  const it = cur(), d = draft(it), c = selected();
  if (it.mode !== "variants") return;
  if (d.dropped.has(c.label)) d.dropped.delete(c.label); else d.dropped.add(c.label);
  touch(it, d);
}
function select(pos, autoplay) {
  if (pos < 0 || pos >= nCands()) return;
  S.sel = pos;
  renderCards(); renderPalette();
  if (autoplay) play(pos, { once: cur().mode === "variants" });
}
function setContext(key) {
  const c = S.cfg.contexts.find((x) => x.key === key);
  if (!available(cur(), c)) return;
  stopAudio();
  S.ctx = key;
  renderHead(); renderCards();
}
function stepContext(dir) {
  const keys = S.cfg.contexts.filter((c) => available(cur(), c)).map((c) => c.key);
  setContext(keys[(keys.indexOf(S.ctx) + dir + keys.length) % keys.length]);
}

async function save() {
  const it = cur(), d = draft(it);
  const need = missing(it, d);
  if (need.length) { say("Chưa lưu: " + need.join("; ") + ".", "warn"); return false; }
  if (S.saving) return false;
  S.saving = true;
  const tags = {};
  for (const [k, v] of Object.entries(d.tags)) if (v.length) tags[k] = v;
  const body = {
    session: S.sess.session, item: it.key, context: S.ctx, contexts_heard: [...d.heard], device: S.device,
    stars: d.stars, pick: d.none ? null : d.pick, pick_auto: d.pickAuto, none: d.none, tags, note: d.note.trim(),
    listens: d.listens, item_ms: Math.round(itemTime(false)), session_ms: Math.round(elapsed()), dropped: [...d.dropped],
  };
  try {
    const r = await api.post("/api/rate", body);
    it.rating = { stars: { ...d.stars }, pick: body.pick, pickAuto: d.pickAuto, none: d.none, tags, note: body.note, dropped: [...d.dropped], rev: r.rev };
    d.dirty = false;
    if (r.reveal) S.reveals[it.key] = r.reveal;
    S.sess.rated = S.sess.items.filter((x) => x.rating).length;
    const shown = r.reveal ? "Thẻ ảnh và số đo hiện bên dưới." : "Thẻ ảnh và số đo mở khi chấm xong cả phiên.";
    say(r.rev > 1 ? `Đã lưu lại (lần ${r.rev}). ${shown} Enter để sang id tiếp.` : `Đã lưu. ${shown} Enter để sang id tiếp.`, "ok");
    renderAll();
    return true;
  } catch (err) {
    say("Không lưu được: " + err.message, "err");
    return false;
  } finally {
    S.saving = false;
  }
}
async function enter(skip) {
  const it = cur(), d = draft(it);
  if (skip) return go(S.idx + 1);
  if (it.rating && !d.dirty) return go(S.idx + 1);
  await save();
}
async function go(i) {
  if (!S.sess) return;
  stopAudio();
  itemTime(true);
  if (i < 0) { say("Đây là id đầu tiên.", "warn"); return; }
  if (i >= S.sess.items.length) { S.idx = S.sess.items.length; S.phase = "done"; runTimer(false); pushState(); renderAll(); return; }
  S.idx = i; S.sel = 0; S.phase = "item";
  const it = cur();
  S.ctx = it.contexts[0] || "alone";
  S.msg = null;
  S.itemMark = performance.now();
  runTimer(true);
  preload(it);
  preload(S.sess.items[i + 1]);
  pushState();
  renderAll();
  if (it.rating && !S.reveals[it.key]) {
    try { S.reveals[it.key] = await api.get(`/api/reveal/${enc(S.sess.session)}/${enc(it.key)}`); renderCards(); } catch (_) { /* not rated on server */ }
  }
}
function pushState() {
  const q = new URLSearchParams();
  if (S.sess) q.set("s", S.sess.session);
  if (S.sess && S.phase === "item") q.set("i", String(S.idx + 1));
  history.replaceState(null, "", "?" + q.toString());
  if (S.sess && S.device) {
    api.post("/api/state", { session: S.sess.session, elapsedMs: Math.round(elapsed()), device: S.device, index: S.idx }).catch(() => {});
  }
}

// ------------------------------------------------------------------ rendering
function renderAll() {
  const root = app();
  root.replaceChildren();
  if (S.phase === "list") return root.append(viewList());
  root.append(viewTop());
  if (S.phase === "done") root.append(viewDone());
  else if (S.phase === "item" || S.phase === "start") root.append(viewItemShell(), viewLegend());
  if (S.phase === "start") root.append(viewStart());
  if (S.overlay === "help") root.append(viewHelp());
  if (S.overlay === "image") root.append(viewImage());
  if (S.phase === "item" || S.phase === "start") { renderHead(); renderCards(); renderPalette(); renderActions(); renderStatus(); }
  renderTop();
}

function viewTop() {
  return h("header", { class: "top" },
    h("div", { class: "brand" }, "Bảng Nghe", h("small", {}, "v" + S.cfg.version)),
    h("div", { class: "title", id: "top-title" }),
    h("div", { class: "prog", id: "top-prog" }),
    h("div", { class: "timer", id: "top-timer", title: "Thời gian nghe của phiên" }),
    h("button", { class: "chip", id: "top-device", title: "Đổi thiết bị nghe", onclick: () => { if (S.phase === "item") { stopAudio(); S.phase = "start"; renderAll(); } } }),
    h("button", { class: "chip", title: "Phím tắt (?)", onclick: () => { S.overlay = "help"; renderAll(); } }, "?"));
}
function renderTop() {
  if (!S.sess) return;
  const title = document.getElementById("top-title");
  if (!title) return;
  title.textContent = S.sess.title;
  const n = S.sess.items.length, rated = S.sess.items.filter((x) => x.rating).length;
  const prog = document.getElementById("top-prog");
  const fill = h("i");
  fill.style.width = ((100 * rated) / n).toFixed(1) + "%";      // CSSOM: allowed by the CSP
  prog.replaceChildren(
    h("span", {}, S.phase === "item" ? `Id ${S.idx + 1}/${n}` : `${n} id`),
    h("span", { class: "bar", title: `Đã chấm ${rated}/${n}` }, fill),
    h("span", {}, `đã chấm ${rated}`));
  renderTimer();
  const dev = document.getElementById("top-device");
  dev.textContent = S.device ? S.cfg.devices[S.device] : "Chưa chọn thiết bị";
}
function renderTimer() {
  const t = document.getElementById("top-timer");
  if (!t || !S.sess) return;
  const ms = elapsed(), max = S.sess.maxMinutes * 60000;
  t.textContent = clock(ms) + " / " + clock(max);
  t.classList.toggle("over", ms > max);
  if (ms > max && !S.warnedLong && S.phase === "item") {
    S.warnedLong = true;
    say(`Đã quá ${fmt(S.sess.maxMinutes, 0)} phút. Nên nghỉ tai, rồi làm tiếp ở phiên sau.`, "warn");
  }
}

function viewItemShell() {
  const note = h("input", {
    id: "note", class: "note", type: "text", maxlength: "500", autocomplete: "off", spellcheck: "false",
    placeholder: "Ghi chú ngắn (phím /), ví dụ: B có lực nhưng đuôi dài",
    oninput: (e) => { const it = cur(), d = draft(it); d.note = e.target.value; d.dirty = true; renderActions(); },
  });
  if (cur()) note.value = draft(cur()).note;
  return h("main", { class: "main" },
    h("section", { class: "itemhead", id: "head" }),
    h("section", { class: "cards", id: "cards", "aria-label": "Các bản nghe mù" }),
    h("section", { class: "palette", id: "palette" }),
    h("footer", { class: "actions" }, note,
      h("button", { class: "btn bad", id: "btn-none", onclick: toggleNone }),
      h("button", { class: "btn", id: "btn-back", onclick: () => go(S.idx - 1) }, "← Id trước ", kbd("⌫")),
      h("button", { class: "btn primary", id: "btn-save", onclick: () => enter(false) })),
    h("div", { class: "status", id: "status", role: "status", "aria-live": "polite" }));
}
function renderHead() {
  const el = document.getElementById("head");
  if (!el || S.phase === "start" && !S.sess.items.length) return;
  const it = cur() || S.sess.items[0];
  const fam = S.cfg.families[it.family] || it.family;
  el.replaceChildren(
    h("div", { class: "who" },
      h("h1", {}, it.id),
      h("div", { class: "meta" }, h("span", { class: "chip" }, it.modeLabel), fam ? h("span", { class: "chip" }, fam) : null,
        it.candidates.length > 1 ? h("span", { class: "chip" }, `${it.candidates.length} bản`) : null,
        it.desc ? h("span", { class: "desc" }, it.desc) : null)),
    h("div", {},
      h("nav", { class: "ctxs", "aria-label": "Bối cảnh nghe" },
        S.cfg.contexts.filter((c) => !c.rendered || available(it, c)).map((c) => h("button", {
          class: (c.key === S.ctx ? "on " : "") + (it.contexts.includes(c.key) ? "sug" : ""),
          disabled: !available(it, c), title: c.hint || (it.contexts.includes(c.key) ? "Gợi ý cho họ âm này" : ""),
          onclick: () => setContext(c.key),
        }, c.key === "loop" ? `Lặp ${it.loop.count || 20} lần` : c.label, !c.enabled ? h("small", {}, " (giai đoạn 3)") : null))),
      h("div", { class: "ctxhint" }, kbd("↑"), " ", kbd("↓"), " đổi bối cảnh · ", ctxHint(it))));
}
function ctxHint(it) {
  if (S.ctx === "loop") {
    const p = it.loop;
    if (p.seamless) return `lặp liền ${p.count || 20} lần để nghe mối nối`;
    return `${p.count || 20} lần, cách ~${fmt(p.interval_ms, 0)} ms, ±${fmt(p.cents, 0)} cent, ±${fmt(p.db, 1)} dB`;
  }
  if (S.ctx === "small") return `lọc cao ${fmt(S.cfg.smallSpeakerHz, 0)} Hz`;
  if (isRendered(S.ctx)) return ctxInfo(S.ctx).hint || "bản dựng sẵn";
  return "phát riêng từng bản";
}

function renderCards() {
  const el = document.getElementById("cards");
  if (!el || !cur()) return;
  const it = cur(), d = draft(it), rev = S.reveals[it.key];
  el.style.setProperty("--n", String(Math.min(it.candidates.length, 4)));
  el.classList.toggle("many", it.candidates.length > 4);
  const need = d.dirty || !it.rating;
  el.replaceChildren(...it.candidates.map((c, pos) => {
    const stars = d.stars[c.label] || 0;
    const tags = d.tags[c.label] || [];
    const dur = c.files[0].durationMs;
    const picked = d.pick === c.label && !d.none;
    const rv = rev && rev.candidates.find((x) => x.label === c.label);
    const card = h("article", {
      class: "card" + (pos === S.sel ? " sel" : "") + (picked ? " picked" : "") + (d.dropped.has(c.label) ? " dropped" : ""),
      data: { label: c.label, dur: dur ? fmt(dur / 1000, 2) + " s" + (c.files.length > 1 ? ` · ${c.files.length} biến thể` : "") : "" },
      onclick: (e) => { if (e.target === card) select(pos, false); },
    },
    h("div", { class: "head" },
      h("span", { class: "lab" }, c.label), kbd(String(pos + 1)),
      h("span", { class: "grow" }, d.listens[c.label] ? `nghe ${d.listens[c.label]} lần` : "chưa nghe"),
      picked ? h("span", { class: "badge " + (d.pickAuto ? "auto" : "pick"), title: d.pickAuto ? "Tự chọn vì có nhiều sao nhất; bấm V để chọn tay" : "" }, d.pickAuto ? "tốt nhất (sao)" : "tốt nhất") : null,
      d.dropped.has(c.label) ? h("span", { class: "badge drop" }, "bỏ") : null),
    c.note ? h("div", { class: "cnote", title: "Nhãn ghi sẵn cho bản này" }, c.note) : null,
    h("div", { class: "player" },
      h("button", { class: "play", "aria-label": `Phát bản ${c.label}`, onclick: () => { if (isPlaying(c.label)) stopAudio(); else { S.sel = pos; play(pos, { once: it.mode === "variants" }); } } }, "▶"),
      h("div", { class: "track" }, h("i")),
      h("span", { class: "ptime" }, "")),
    h("div", { class: "stars", role: "group", "aria-label": `Số sao cho ${c.label}` },
      [1, 2, 3, 4, 5].map((n) => h("button", {
        class: n <= stars ? "on" : "", "aria-label": `${n} sao`, title: `⇧${n}`,
        onclick: () => { S.sel = pos; setStars(stars === n ? 0 : n); },
      }, "★")),
      need && !stars && it.mode !== "variants" ? h("span", { class: "need" }, "chưa chấm") : null),
    h("div", { class: "ctags" }, tags.length ? tags.map((t) => h("span", {}, t)) : h("span", { class: "empty" }, "chưa có nhãn")),
    h("div", { class: "row" },
      it.mode === "variants"
        ? h("button", { class: "btn bad" + (d.dropped.has(c.label) ? " on" : ""), onclick: () => { S.sel = pos; toggleDrop(); } }, d.dropped.has(c.label) ? "Đã bỏ" : "Bỏ bản này", kbd("X"))
        : it.candidates.length > 1
          ? h("button", { class: "btn" + (picked ? " on" : ""), onclick: () => { S.sel = pos; togglePick(); } }, picked ? "Bản tốt nhất" : "Chọn bản này", kbd("V"))
          : null),
    rv ? viewReveal(it, c, rv) : null);
    return card;
  }));
  paintPlayback(AU.play && AU.ctx ? AU.ctx.currentTime : undefined);
}
// The card keeps six measurements; the lightbox (I) shows all of them.
const PRIMARY = ["Dài", "Độ to", "Đỉnh", "Lên", "Crest", "Chỉnh"];
function measureList(rows) {
  return h("dl", {}, rows.map((m) => [h("dt", { title: m.hint || "" }, m.label),
    h("dd", { title: m.hint || "" }, (m.signed ? signed(m.value) : fmt(m.value, Math.abs(m.value) < 1 ? 3 : 1)) + (m.unit ? " " + m.unit : ""))]));
}
function flagList(flags, max) {
  const shown = flags.slice(0, max);
  return h("div", { class: "flags" }, shown.map((f) => h("span", { class: /FAIL|chặn/.test(f) ? "fail" : "" }, f)),
    flags.length > shown.length ? h("span", { class: "more" }, `+${flags.length - shown.length}`) : null);
}
function viewReveal(it, c, rv) {
  const cardUrl = (n) => `/api/card/${enc(S.sess.session)}/${enc(it.key)}/${c.label}/${n}`;
  const thumb = rv.cards.length
    ? h("button", { class: "thumb", title: "Phóng to (I)", onclick: () => openImage(c.label) },
      h("img", { src: cardUrl(rv.cards[0]), alt: `Thẻ phân tích bản ${c.label}`, loading: "lazy" }))
    : h("div", { class: "nocard" }, "Chưa có thẻ ảnh của bộ phê bình");
  return h("div", { class: "reveal" }, thumb, measureList(rv.measures.filter((m) => PRIMARY.includes(m.label))),
    rv.flags.length ? flagList(rv.flags, 3) : null);
}
function renderPalette() {
  const el = document.getElementById("palette");
  if (!el || !cur()) return;
  const c = selected(), d = draft(cur());
  const on = new Set(d.tags[c.label] || []);
  el.replaceChildren(
    h("h2", {}, "Nhãn cho bản đang chọn ", h("b", {}, c.label), " (bấm phím chữ để bật/tắt)"),
    h("div", { class: "tags" }, S.cfg.tags.map((t) => h("button", { class: "tag" + (on.has(t.name) ? " on" : ""), onclick: () => toggleTag(t.name) },
      kbd(t.code.replace("Key", "")), t.name))));
}
function renderActions() {
  if (!cur() || (S.phase !== "item" && S.phase !== "start")) return;
  const it = cur(), d = draft(it);
  const none = document.getElementById("btn-none");
  const saveBtn = document.getElementById("btn-save");
  if (!none || !saveBtn) return;
  none.hidden = it.mode === "variants";
  none.classList.toggle("on", d.none);
  none.replaceChildren(it.candidates.length > 1 ? "Không bản nào đạt " : "Không đạt ", kbd("0"));
  const done = it.rating && !d.dirty;
  saveBtn.replaceChildren(done ? (S.idx + 1 < S.sess.items.length ? "Id tiếp " : "Kết thúc ") : (it.rating ? "Lưu lại " : "Lưu "), kbd("Enter"));
  document.getElementById("btn-back").disabled = S.idx === 0;
}
function renderStatus() {
  const el = document.getElementById("status");
  if (!el) return;
  el.className = "status" + (S.msg && S.msg.kind ? " " + S.msg.kind : "");
  el.textContent = S.msg ? S.msg.text : "";
}
function viewLegend() {
  const items = [
    [["Space"], "phát / dừng"], [["1–9"], "chọn bản và phát"], [["⇧1–5"], "sao"], [["V"], "bản tốt nhất"],
    [["0"], "không bản nào đạt"], [["chữ"], "nhãn"], [["↑", "↓"], "bối cảnh"], [["Enter"], "lưu / id tiếp"],
    [["⌫"], "id trước"], [["/"], "ghi chú"], [["I"], "phóng thẻ"], [["?"], "trợ giúp"],
  ];
  return h("footer", { class: "legend" }, items.map(([keys, text]) => h("span", {}, keys.map((k) => [kbd(k), " "]), text)));
}

function viewStart() {
  const s = S.sess, n = s.items.length, rated = s.items.filter((x) => x.rating).length;
  const resume = rated > 0 && S.idx < n;
  const est = Math.max(1, Math.round((n - rated) * 1.5));     // about 1.5 min per id (SESSION_0A.md)
  const pick = (dev) => { S.device = dev; renderAll(); };
  return h("div", { class: "overlay" }, h("div", { class: "modal", role: "dialog", "aria-modal": "true", "aria-label": "Bắt đầu phiên" },
    h("h2", {}, s.title),
    h("p", { class: "hint" }, `${n} id · đã chấm ${rated} · còn khoảng ${est} phút nghe`),
    n > s.maxItems ? h("p", { class: "warn" }, `Phiên có ${n} id, kế hoạch khuyên tối đa ${s.maxItems} id để tai không mỏi.`) : null,
    h("h3", {}, "Bạn đang nghe bằng gì?"),
    h("div", { class: "choices" },
      h("button", { class: "btn" + (S.device === "headphones" ? " on" : ""), onclick: () => pick("headphones") }, kbd("1"), "Tai nghe"),
      h("button", { class: "btn" + (S.device === "speakers" ? " on" : ""), onclick: () => pick("speakers") }, kbd("2"), "Loa")),
    h("p", { class: "hint" }, "Giữ âm lượng máy ở một mức cố định suốt phiên: chỉnh cho dễ chịu ở id đầu tiên rồi không đổi nữa."),
    h("p", { class: "hint" }, "Các bản đã được cân cùng độ to. Nhãn A, B, C xếp ngẫu nhiên cho từng id. " +
      (s.revealAt === "end" ? "Thẻ ảnh và số đo chỉ mở khi bạn chấm xong cả phiên." : "Thẻ ảnh và số đo chỉ hiện sau khi bạn chấm.")),
    h("div", { class: "go" },
      h("button", { class: "btn", onclick: () => { S.sess = null; loadList(); } }, "Danh sách phiên"),
      h("button", { class: "btn primary", disabled: !S.device, onclick: begin },
        resume ? `Tiếp tục từ id ${S.idx + 1} ` : "Bắt đầu ", kbd("Enter")))));
}
function begin() {
  if (!S.device) return;
  audioCtx();
  go(S.idx);
}
function viewHelp() {
  const rows = [
    ["Space", "Phát hoặc dừng bản đang chọn (bối cảnh hiện tại). Ở lượt biến thể và bối cảnh Lặp 20 lần: phát cả bộ"],
    ["1 – 9", "Chọn bản A, B, C… và phát ngay"],
    ["← →", "Chọn bản trước hoặc sau, không phát"],
    ["⇧1 – ⇧5", "Chấm 1–5 sao cho bản đang chọn (⇧0 xóa sao)"],
    ["V", "Chọn bản tốt nhất (nếu không chọn, bản có nhiều sao nhất được chọn khi không hòa)"],
    ["0", "Không bản nào đạt"],
    ["X", "Lượt biến thể: bỏ hoặc giữ bản đang chọn"],
    ["chữ", "Bật hoặc tắt nhãn cho bản đang chọn (bảng dưới)"],
    ["↑ ↓", "Đổi bối cảnh: Một mình, Lặp (đúng nhịp chơi; 20 lần, hoặc 8 lần với âm phát thưa), Loa nhỏ"],
    ["Enter", "Lưu điểm; Enter lần nữa để sang id tiếp. ⇧Enter: bỏ qua, không lưu"],
    ["⌫", "Quay lại id trước"],
    ["/", "Viết ghi chú (Enter để lưu, Esc để thoát ô ghi chú)"],
    ["I", "Phóng to thẻ ảnh (chỉ sau khi chấm)"],
    ["Esc", "Dừng phát, đóng cửa sổ"],
  ];
  return h("div", { class: "overlay", onclick: (e) => { if (e.target === e.currentTarget) closeOverlay(); } },
    h("div", { class: "modal", role: "dialog", "aria-modal": "true", "aria-label": "Phím tắt" },
      h("h2", {}, "Phím tắt"),
      h("dl", { class: "keys" }, rows.map(([k, v]) => [h("dt", {}, kbd(k)), h("dd", {}, v)])),
      h("div", { class: "tagkeys" }, S.cfg.tags.map((t) => h("span", {}, kbd(t.code.replace("Key", "")), " ", t.name))),
      h("div", { class: "go" }, h("button", { class: "btn primary", onclick: closeOverlay }, "Đóng ", kbd("Esc")))));
}
function openImage(label) {
  const it = cur(), rv = S.reveals[it.key];
  const c = rv && rv.candidates.find((x) => x.label === (label || selected().label));
  if (!c) { say(S.sess.revealAt === "end" ? "Thẻ và số đo mở khi chấm xong cả phiên." : "Chấm xong mới xem được thẻ và số đo.", "warn"); return; }
  S.image = { label: c.label, rv: c, src: c.cards.length ? `/api/card/${enc(S.sess.session)}/${enc(it.key)}/${c.label}/${c.cards[0]}` : null };
  S.overlay = "image";
  renderAll();
}
function viewImage() {
  const rv = S.image.rv;
  return h("div", { class: "overlay lightbox", onclick: closeOverlay },
    h("div", { class: "lbwrap" },
      S.image.src ? h("img", { src: S.image.src, alt: `Thẻ phân tích bản ${S.image.label}` }) : h("div", { class: "nocard" }, "Chưa có thẻ ảnh"),
      h("aside", {}, h("h3", {}, `Bản ${S.image.label}`), measureList(rv.measures), rv.flags.length ? flagList(rv.flags, 20) : null,
        h("p", {}, "Esc hoặc I để đóng"))));
}
function closeOverlay() { S.overlay = null; S.image = null; renderAll(); }

function viewDone() {
  const s = S.sess, n = s.items.length, rated = s.items.filter((x) => x.rating).length;
  return h("main", { class: "page" },
    h("h1", {}, rated === n ? "Xong phiên" : "Hết danh sách"),
    h("p", { class: "sub" }, rated === n ? "Cảm ơn bạn. Điểm đã được ghi lại." : `Còn ${n - rated} id chưa chấm. Bấm ⌫ để quay lại.`),
    h("div", { class: "stats" },
      h("div", {}, h("b", {}, `${rated}/${n}`), h("span", {}, "id đã chấm")),
      h("div", {}, h("b", {}, clock(elapsed())), h("span", {}, "thời gian nghe")),
      h("div", {}, h("b", {}, S.device ? S.cfg.devices[S.device] : "—"), h("span", {}, "thiết bị"))),
    rated === n && s.revealAt === "end" ? h("p", { class: "hint" }, "Thẻ ảnh và số đo của mọi id đã mở: bấm ⌫ để xem lại từng id.") : null,
    h("p", {}, "Điểm ghi vào: ", h("span", { class: "path" }, s.ratingsFile)),
    h("div", { class: "go" },
      h("button", { class: "btn", onclick: () => go(n - 1) }, "← Id cuối ", kbd("⌫")),
      h("button", { class: "btn primary", onclick: () => { S.sess = null; loadList(); } }, "Danh sách phiên ", kbd("Enter"))));
}
function viewList() {
  const L = S.list || { sessions: [], errors: [] };
  return h("main", { class: "page" },
    h("h1", {}, "Bảng Nghe"),
    h("p", { class: "sub" }, "Nghe mù, đã cân độ to. Chọn một phiên để bắt đầu."),
    L.sessions.length ? h("div", { class: "list" }, L.sessions.map((s, i) => h("button", { class: "srow", onclick: () => openSession(s.session) },
      kbd(String(i + 1)),
      h("span", {}, h("div", { class: "t" }, s.title), h("div", { class: "m" }, `${s.game} · lô ${s.batch || "—"} · ${s.session}`)),
      h("span", { class: "m" + (s.rated >= s.items ? " done" : "") }, `${s.rated}/${s.items} id`),
      h("span", {}, "Mở →"))))
      : h("p", { class: "hint" }, "Chưa có phiên nào. Tạo phiên demo: bash tools/audio-lab/run.sh board demo"),
    L.errors.length ? h("div", { class: "errors" }, h("b", {}, "Phiên lỗi (bị bỏ qua):"), L.errors.map((e) => h("div", {}, e))) : null);
}

// ------------------------------------------------------------------ keyboard
function onKey(e) {
  if (e.metaKey || e.ctrlKey || e.altKey) return;
  const active = document.activeElement;
  if (active && active.id === "note") {
    if (e.isComposing || e.keyCode === 229) return;            // Vietnamese IME composing
    if (e.key === "Escape") { e.preventDefault(); active.blur(); }
    else if (e.key === "Enter") { e.preventDefault(); active.blur(); enter(e.shiftKey); }
    return;
  }
  if (active && active.tagName === "BUTTON" && (e.code === "Space" || e.code === "Enter")) active.blur();
  const code = e.code;
  if (S.overlay) {
    if (code === "Escape" || code === "Enter" || code === "KeyI" || (code === "Slash" && e.shiftKey)) { e.preventDefault(); closeOverlay(); }
    return;
  }
  if (S.phase === "list") {
    const L = (S.list && S.list.sessions) || [];
    if (/^Digit[1-9]$/.test(code) && L[+code.slice(5) - 1]) openSession(L[+code.slice(5) - 1].session);
    else if (code === "Enter" && L.length) openSession((L.find((s) => s.rated < s.items) || L[0]).session);
    return;
  }
  if (code === "Slash" && e.shiftKey) { e.preventDefault(); S.overlay = "help"; renderAll(); return; }
  if (S.phase === "start") {
    if (code === "Digit1") { S.device = "headphones"; renderAll(); }
    else if (code === "Digit2") { S.device = "speakers"; renderAll(); }
    else if (code === "Enter") { e.preventDefault(); begin(); }
    return;
  }
  if (S.phase === "done") {
    if (code === "Backspace") { e.preventDefault(); go(S.sess.items.length - 1); }
    else if (code === "Enter") { e.preventDefault(); S.sess = null; loadList(); }
    return;
  }
  if (S.phase !== "item") return;
  audioCtx();
  if (e.repeat && !["ArrowLeft", "ArrowRight"].includes(code)) { e.preventDefault(); return; }
  const tags = tagByCode();
  const digit = /^Digit([0-9])$/.exec(code);
  if (digit) {
    e.preventDefault();
    const n = +digit[1];
    if (e.shiftKey) { if (n <= 5) setStars(n); }
    else if (n === 0) toggleNone();
    else if (n <= nCands()) select(n - 1, true);
    return;
  }
  switch (code) {
    case "Space":
      e.preventDefault();
      if (isPlaying()) stopAudio();
      else play(S.sel, { set: cur().mode === "variants" && S.ctx === "loop" });
      return;
    case "Enter": e.preventDefault(); enter(e.shiftKey); return;
    case "Backspace": e.preventDefault(); go(S.idx - 1); return;
    case "ArrowLeft": e.preventDefault(); select(Math.max(0, S.sel - 1), false); return;
    case "ArrowRight": e.preventDefault(); select(Math.min(nCands() - 1, S.sel + 1), false); return;
    case "ArrowUp": e.preventDefault(); stepContext(-1); return;
    case "ArrowDown": e.preventDefault(); stepContext(1); return;
    case "KeyV": togglePick(); return;
    case "KeyX": toggleDrop(); return;
    case "KeyI": openImage(); return;
    case "Slash": e.preventDefault(); document.getElementById("note")?.focus(); return;
    case "Escape": stopAudio(); say(""); return;
    default:
      if (tags[code] && !e.shiftKey) { e.preventDefault(); toggleTag(tags[code]); }
  }
}

// ------------------------------------------------------------------ boot
async function loadList() {
  S.phase = "list";
  stopAudio();
  runTimer(false);
  history.replaceState(null, "", "?");
  try { S.list = await api.get("/api/sessions"); } catch (err) { S.list = { sessions: [], errors: [err.message] }; }
  renderAll();
}
async function openSession(sid, index) {
  try {
    const s = await api.get(`/api/session/${enc(sid)}`);
    S.sess = s; S.drafts = {}; S.reveals = {}; S.warnedLong = false;
    S.device = s.state.device || null;
    S.elapsedBase = s.state.elapsedMs || 0; S.elapsedMark = null;
    S.idx = Number.isInteger(index) ? Math.max(0, Math.min(index, s.items.length - 1)) : Math.min(s.resumeIndex, s.items.length - 1);
    S.phase = "start";
    S.sel = 0;
    S.ctx = s.items[S.idx].contexts[0] || "alone";
    preload(s.items[S.idx]);
    renderAll();
  } catch (err) {
    S.list = { sessions: (S.list && S.list.sessions) || [], errors: [err.message] };
    S.phase = "list";
    renderAll();
  }
}
async function boot() {
  try { S.cfg = await api.get("/api/config"); } catch (err) { app().textContent = "Không kết nối được máy chủ Bảng Nghe: " + err.message; return; }
  document.addEventListener("keydown", onKey);
  document.addEventListener("visibilitychange", () => {
    if (S.phase !== "item") return;
    if (document.visibilityState === "hidden") { runTimer(false); itemTime(true); stopAudio(); pushState(); }
    else { runTimer(true); S.itemMark = performance.now(); }
  });
  setInterval(renderTimer, 1000);
  setInterval(() => { if (S.phase === "item") pushState(); }, 15000);
  const q = new URLSearchParams(location.search);
  S.list = await api.get("/api/sessions").catch(() => ({ sessions: [], errors: [] }));
  const sid = q.get("s") || (S.list.sessions.length === 1 ? S.list.sessions[0].session : null);
  if (sid) await openSession(sid, q.get("i") ? Number(q.get("i")) - 1 : undefined);
  else { S.phase = "list"; renderAll(); }
}
window.__board = { S, AU };   // for the browser check
boot();
