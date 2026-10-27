"""Lời Gọi scenarios: the word chain, a night alarm, the title menu (BATCH1_BRIEF §4.3, §4.4, §5 L1-L3, §7).

Numbers from the game's audio code (games/typing-defense/src/view/audio-min.ts, folk.ts; read only, 24/10/2026):
  - master gain (80/100)^2 = 0.64 -> DynamicsCompressorNode limiter (-3 dB, ratio 20, knee 0, attack 2 ms,
    release 120 ms) -> out; the settings default to master 80, sfx 80 (ui/settings.ts).
  - sfx gain 1.4 x (80/100)^2 = 0.896 -> master; sfx -> 0.12 -> reverb (ConvolverNode, reverbTail 0.8 s: white
    noise x (1 - k/n)^2.6 per channel, normalize) -> 0.5 -> master.
  - typing bus (word-hit, word-hit-bell, call alerts, keys): DynamicsCompressorNode (-18 dB, ratio 3, attack 3 ms,
    release 100 ms, knee 30 dB by default) -> sfx; world bus (shots, arrows, blasts, puffs, coins, leak): gain 0.9
    -> sfx; ui bus: straight into sfx.
  - only the music is ducked under a spoken word (0.35, tau 0.04 s / 0.17 s); there is no music file yet, so no bus
    is ducked here. The spoken word (speechSynthesis) is outside the game's graph: added after the master.
  - wordHit: step = sloppy ? 4 : 5 + min(5, chainTier + 1) (A4, then D5..C6 by tier: step 5 = C5 never plays);
    synth gains sloppy 0.07, ok 0.11, perfect/flash 0.14; flash bends up from -1 semitone in 90 ms; perfect and
    flash add the bell 20 ms later. BATCH1_BRIEF #21 lowers the scale an octave: A3 C4 D4 F4 G4 A4 C5.
  - caps: room() counts plays in a sliding 1 s window (arrows 4, puffs 8, coins 3, call alerts 3), blasts at most
    2 and puffs 3 per frame, a leak at least 0.8 s after the last; every sound starts at the frame's currentTime.
  - towers (content/slice-1a.ts): arrows every 0.7-0.9 s per tower, cannon every 2.2-2.6 s with splash.

Two playback configurations:
  current   the game today: every sound on the next 60 Hz frame boundary, the 1 s room() windows (a burst plays
            its first sounds and then nothing until the window clears: BATCH1_BRIEF L1).
  proposed  the contract for the wiring step (BATCH1_BRIEF L1, L2): simulation time, an evenly refilled token
            bucket per id instead of the window (arrows 4/s, puffs 8/s with a burst of 3 so a splash still kills
            three at once, coins 3/s, call alerts 3/s: 250, 125, 333, 333 ms between sounds once the burst is
            spent); the per-frame caps stay (blasts 2, puffs 3).

Levels: an event enters its bus at the middle of its card's mix target (LUFS-M max, plan §4.3.3), so every candidate
of an id sits at the same level and only the sound differs. word-hit follows the card text "−22 (bậc C) to −16
(bậc S)" by chain tier, a sloppy word 2 dB under tier 0. Cards without a range: call-chop −19 (the alert is as loud
as a mid word-hit in the code), coin −23 (the code's coin bell is the quietest world sound). Random pitch and level
per the card's randomisation group, from a generator seeded by the scenario only (the same for every candidate).
Approximations (said in every report): the compressors are peak detectors with attack/release smoothing, a quadratic
soft knee and Chromium's make-up gain, without the 6 ms look-ahead; the reverb noise is seeded (the game's is random
per load); frames are an even 60 Hz; keys are the game's own synth tick (folk.ts go()), there is no music yet.

The voice test sweeps the delay (0, 150, 400 ms) without and with a −6 dB duck of the typing and world buses
from the request (plan §6.2 step 4), which the game does not have today.

Scenarios:
  td-wordhit-chain  seven words 1.5 s apart (40 WPM, five keys each) climbing the chain: word-hit A3 (sloppy) C4 D4 F4
                    (perfect: + bell) G4 A4 C5 (flash: slide + bell), each with a Word Shot (wordshot-fire) and the
                    spoken word 150 ms after; three arrow towers (0.7, 0.7, 0.8 s), two cannons (1.8, 4.7, 7.7, 9.2 s); ink folk
                    dying (ink-puff) and coins (coin). 11.6 s.
  td-night          night: five words with word-hits and Word Shots, two arrow towers, a call "Chặt" lighting up twice
                    (call-chop), ink folk leaking into the keep twice (leak, 3.4 s and 7.2 s). 9.0 s.
  td-menu           the title menu: five steps (ui-move) and a choice (ui-pick), twice. 4.2 s.
"""
from __future__ import annotations

import json
import random
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import soundfile as sf
import yaml

from build import measure
from common import env

from . import metrics, mixer, voices

SR = mixer.SR
GAME = "typing-defense"
SCENARIOS = ("td-wordhit-chain", "td-night", "td-menu")
FRAME_S = 1.0 / 60.0
SCENE_GAIN_DB = -11.0          # every render: near the board's −23 LUFS-M target, the same for all items
SCENE_GAIN_BY = {"td-menu": -1.0}   # the menu has only UI ticks (cards −30..−22): near −27 LUFS-M instead of −37

LOI_GOI = {
    "game": GAME,
    "source": "games/typing-defense/src/view/audio-min.ts, folk.ts, ui/settings.ts (read 24/10/2026)",
    "master": 0.64, "sfx": 0.896, "world": 0.9, "verb_send": 0.12, "verb_return": 0.5, "verb_s": 0.8,
    "typing_comp": {"threshold_db": -18.0, "ratio": 3.0, "attack_s": 0.003, "release_s": 0.1, "knee_db": 30.0},
    "limiter": {"threshold_db": -3.0, "ratio": 20.0, "attack_s": 0.002, "release_s": 0.12, "knee_db": 0.0},
}
BUS = {"word-hit": "typing", "word-hit-bell": "typing", "call-chop": "typing", "key": "typing",
       "wordshot-fire": "world", "arrow-fire": "world", "ink-puff": "world", "blast": "world", "coin": "world",
       "leak": "world", "ui-move": "ui", "ui-pick": "ui"}
LEVEL_FALLBACK = {"call-chop": -19.0, "coin": -23.0, "key": -26.0}
WORD_HIT_TIER_DB = (-22.0, -20.5, -19.0, -17.5, -16.0)     # card text: −22 (bậc C) to −16 (bậc S)
SLOPPY_DB = -24.0
SCALE = ("A3", "C4", "D4", "F4", "G4", "A4", "C5")          # BATCH1_BRIEF #21
CURRENT_CAPS = {"arrow-fire": (4, 1.0), "ink-puff": (8, 1.0), "coin": (3, 1.0), "call-chop": (3, 1.0)}
PROPOSED_GAP_S = {"arrow-fire": 0.25, "ink-puff": 0.125, "coin": 0.333, "call-chop": 0.333}   # 1 / refill rate
PROPOSED_BURST = {"ink-puff": 3}                                                               # bucket size (default 1)
PER_FRAME = {"blast": 2, "ink-puff": 3}
LEAK_GAP_S = 0.8
DENSE = ("arrow-fire", "ink-puff", "coin", "blast")
WORD_COMPLETE = ("word-hit", "word-hit-bell", "wordshot-fire")


def card(sid: str) -> dict:
    p = env.LAB / "specs" / GAME / f"{sid}.yaml"
    return (yaml.safe_load(p.read_text("utf-8")) or {}) if p.is_file() else {}


def level_of(sid: str) -> float:
    if sid in LEVEL_FALLBACK:
        return LEVEL_FALLBACK[sid]
    rng = ((card(sid).get("loudness") or {}).get("mix_target") or {}).get("range")
    return float(sum(rng)) / 2.0 if rng else -20.0


def rand_of(sid: str) -> tuple[float, float]:
    """(cents, dB) of the card's randomisation group; word-hit climbs the scale instead (no random cents)."""
    if sid in ("word-hit",):
        return 0.0, 1.0
    if sid == "key":
        return 0.0, 0.0
    r = card(sid).get("randomisation") or {}
    return float(r.get("pitch_cents") or 0.0), float(r.get("gain_db") or 0.0)


_CACHE: dict[str, np.ndarray] = {}


def load_mono(path: Path, lufs_m: float) -> np.ndarray:
    key = f"{path}|{lufs_m}"
    if key in _CACHE:
        return _CACHE[key]
    x, sr = sf.read(str(path), always_2d=True, dtype="float64")
    if sr != SR:
        import soxr
        x = soxr.resample(x, sr, SR, quality="VHQ")
    m = x.mean(axis=1)
    m = m * mixer.db_to_gain(lufs_m - measure.lufs_m_max(m, SR))
    _CACHE[key] = m
    return m


def key_tick(n_typed: int) -> np.ndarray:
    """folk.ts go(typing, t, 880 * 2^(n/12), 0.08, 0.028): a short sine gliding down 4 % and a band of noise."""
    f = 880.0 * 2 ** (min(12, n_typed) / 12.0)
    hollow = 0.028
    n = int((hollow + 0.03) * SR)
    t = np.arange(n) / SR
    env_ = np.where(t < 0.001, 1e-4 * (0.08 / 1e-4) ** (t / 0.001), 0.08 * (1e-4 / 0.08) ** np.clip((t - 0.001) / hollow, 0, 1))
    ph = 2 * np.pi * np.cumsum(f * (0.96 ** np.clip(t / hollow, 0, 1))) / SR
    tone = np.sin(ph) * env_
    rng = np.random.default_rng(int(f))
    from scipy import signal
    b, a = signal.iirpeak(min(f * 2.3, SR / 2 - 100), 3.0, fs=SR)
    nz = signal.lfilter(b, a, rng.uniform(-1, 1, n))
    env2 = np.where(t < 0.001, 0.0, 0.064 * (1e-4 / 0.064) ** np.clip((t - 0.001) / 0.022, 0, 1))
    env2[t > 0.03] = 0.0
    return tone + nz * env2


def slide_up(x: np.ndarray, semis: float = -1.0, ramp_s: float = 0.09) -> np.ndarray:
    """playbackRate from 2^(semis/12) to 1 in ramp_s (exponential), like the flash note's bend (folk.ts tranh)."""
    n_out = x.size
    t = np.arange(n_out) / SR
    r0 = 2 ** (semis / 12.0)
    rate = np.where(t < ramp_s, r0 * (1.0 / r0) ** (t / ramp_s), 1.0)
    pos = np.concatenate([[0.0], np.cumsum(rate)[:-1]])
    return np.interp(pos, np.arange(x.size), x, right=0.0)


def reverb_tail(seconds: float = 0.8, seed: int = 7) -> np.ndarray:
    n = int(np.floor(seconds * SR))
    rng = np.random.default_rng(seed)
    k = np.arange(n) / n
    return np.stack([(rng.uniform(-1, 1, n)) * (1 - k) ** 2.6 for _ in range(2)], axis=1)


_IR: dict[float, np.ndarray] = {}


def convolver(x: np.ndarray, seconds: float) -> np.ndarray:
    """ConvolverNode with normalize=true (Chromium: RMS power over both channels, 0.00125 calibration)."""
    from scipy import signal
    if seconds not in _IR:
        _IR[seconds] = reverb_tail(seconds)
    ir = _IR[seconds]
    power = np.sqrt(np.sum(ir ** 2) / ir.size)
    scale = (1.0 / max(power, 0.000125)) * 0.00125 * (44100.0 / SR)
    return np.stack([signal.fftconvolve(x[:, c], ir[:, c])[: x.shape[0]] for c in range(2)], axis=1) * scale


@dataclass
class Ev:
    t: float
    audio: np.ndarray            # mono
    bus: str
    pan: float = 0.0
    slot: str = ""
    label: str = ""


@dataclass
class Scene:
    scenario: str
    config: str
    slots: dict
    delay: float
    events: list[Ev] = field(default_factory=list)
    voices: list[mixer.Voice] = field(default_factory=list)
    marks: list[dict] = field(default_factory=list)
    asked: dict = field(default_factory=dict)        # id -> scheduled times (before caps)
    played: dict = field(default_factory=dict)       # id -> times that sound (after caps, after frame snap)
    word: int = 0
    requests: list = field(default_factory=list)

    def __post_init__(self):
        self.rng = random.Random(f"{self.scenario}:pattern")
        self._win: dict[str, list[float]] = {}
        self._frame: dict[tuple[str, int], int] = {}
        self._last: dict[str, float] = {}
        self._tokens: dict[str, tuple[float, float]] = {}

    def when(self, t: float) -> float:
        return float(np.ceil(t / FRAME_S - 1e-9) * FRAME_S) if self.config == "current" else t

    def allowed(self, sid: str, t: float) -> bool:
        """The caps of the configuration (scheduled time t, already snapped)."""
        fr = int(round(t / FRAME_S))
        if sid in PER_FRAME:
            k = (sid, fr)
            if self._frame.get(k, 0) >= PER_FRAME[sid]:
                return False
        if sid == "leak":
            if t - self._last.get(sid, -1e9) < LEAK_GAP_S:
                return False
        elif self.config == "current" and sid in CURRENT_CAPS:
            mx, win = CURRENT_CAPS[sid]
            lst = [x for x in self._win.get(sid, []) if t - x <= win]
            if len(lst) >= mx:
                self._win[sid] = lst
                return False
            self._win[sid] = lst + [t]
        elif self.config == "proposed" and sid in PROPOSED_GAP_S:
            cap, gap = PROPOSED_BURST.get(sid, 1), PROPOSED_GAP_S[sid]
            tok, last = self._tokens.get(sid, (float(cap), t))
            tok = min(float(cap), tok + (t - last) / gap)
            if tok < 1.0 - 1e-9:
                self._tokens[sid] = (tok, t)
                return False
            self._tokens[sid] = (tok - 1.0, t)
        if sid in PER_FRAME:
            self._frame[(sid, fr)] = self._frame.get((sid, fr), 0) + 1
        self._last[sid] = t
        return True

    def one(self, sid: str, t: float, pan: float = 0.0, gain_db: float = 0.0, audio: np.ndarray | None = None,
            label: str | None = None, file: Path | None = None) -> None:
        """Ask for a sound at simulation time t; the caps run in time order in finish()."""
        if t < 0:                       # before the scene starts (the first word's early keys)
            return
        cents_r, db_r = rand_of(sid)
        cc = (self.rng.random() * 2 - 1) * cents_r          # drawn even when the slot is empty: same pattern for all
        dd = (self.rng.random() * 2 - 1) * db_r
        self.requests.append((t, len(self.requests), sid, pan, gain_db + dd, cc, audio, label, file))

    def finish(self) -> None:
        """The simulation asks in any order (towers first, then words); the game hears it in time order."""
        for t, _, sid, pan, gdb, cc, audio, label, file in sorted(self.requests, key=lambda r: (r[0], r[1])):
            self.asked.setdefault(sid, []).append(round(t, 4))
            if audio is None:
                f = file or self.slots.get(sid)
                if f is None or isinstance(f, dict):      # an empty slot (word-hit: a set without this note)
                    continue
                audio = load_mono(Path(f), level_of(sid))
            ts = self.when(t)
            if not self.allowed(sid, ts):
                continue
            y = mixer.varispeed(audio, cc) * mixer.db_to_gain(gdb)
            self.events.append(Ev(t=ts, audio=y, bus=BUS[sid], pan=pan, slot=sid, label=label or sid))
            self.played.setdefault(sid, []).append(round(ts, 4))
            self.marks.append({"t": round(ts, 3), "id": label or sid, "cents": round(cc, 1), "db": round(gdb, 2), "pan": pan})
        self.requests = []

    def keys(self, t_done: float, letters: int = 5, step: float = 0.28):
        """The word's letters (the game's synth tick, a semitone up per letter); the last one completes the word."""
        for k in range(letters):
            self.one("key", t_done - step * (letters - 1 - k), audio=_key_at_level(k + 1), label="key")

    def word_done(self, t: float, note: str | None, level_db: float, bell: bool = False, flash: bool = False,
                  shot_pan: float | None = None):
        """Word complete: the word-hit note (and bell), a Word Shot, the spoken word `delay` later."""
        w = voices.WORDS[self.word % len(voices.WORDS)]
        v = voices.VOICES[self.word % len(voices.VOICES)]
        self.word += 1
        hits = self.slots.get("word-hit")
        f = (hits.get(note) if isinstance(hits, dict) else hits) if note else None
        y = None
        if f is not None:
            y = load_mono(Path(f), level_db)
            if flash:
                y = slide_up(y)
        if note:
            self.one("word-hit", t, audio=y, label=f"word-hit {note}" + (" (Chớp)" if flash else ""))
        if bell:
            self.one("word-hit-bell", t + 0.02)
        self.one("wordshot-fire", t, pan=self.rng.choice([-0.35, -0.2, 0.2, 0.35]) if shot_pan is None else shot_pan)
        self.voices.append(mixer.Voice(t_request=t, t_start=t + self.delay, audio=voices.load(v, w), word=w, voice=v))

    def kill(self, t: float, pan: float, coin_p: float = 0.6):
        """An ink folk dies (puff); it drops a coin by the simulation, whether or not its puff sounded."""
        self.one("ink-puff", t, pan=pan)
        drop, delay = self.rng.random() < coin_p, 0.15 + self.rng.random() * 0.1
        if drop:
            self.one("coin", t + delay, pan=pan)


_KEYS: dict[int, np.ndarray] = {}


def _key_at_level(n: int) -> np.ndarray:
    if n not in _KEYS:
        x = key_tick(n)
        _KEYS[n] = x * mixer.db_to_gain(level_of("key") - measure.lufs_m_max(x, SR))
    return _KEYS[n]


def _towers(sc: Scene, dur: float, towers: list[tuple[float, float, float]], kill_p: float = 0.35):
    shots = sorted((t0 + k * per, pan) for per, t0, pan in towers for k in range(int((dur - 0.6 - t0) / per) + 1))
    for t, pan in shots:
        sc.one("arrow-fire", t, pan=pan)            # the sim fires whether or not the sound plays
        if sc.rng.random() < kill_p:
            sc.kill(t + 0.32, pan * 0.6)


def build(scenario: str, slots: dict, config: str = "proposed", delay_s: float = 0.15) -> tuple[Scene, float]:
    sc = Scene(scenario, config, slots, delay_s)
    if scenario == "td-wordhit-chain":
        dur = 11.6
        grades = [("A3", SLOPPY_DB, False, False), ("C4", WORD_HIT_TIER_DB[0], False, False),
                  ("D4", WORD_HIT_TIER_DB[1], False, False), ("F4", WORD_HIT_TIER_DB[2], True, False),
                  ("G4", WORD_HIT_TIER_DB[3], False, False), ("A4", WORD_HIT_TIER_DB[4], False, False),
                  ("C5", WORD_HIT_TIER_DB[4], True, True)]
        _towers(sc, dur, [(0.7, 0.25, -0.55), (0.7, 0.6, 0.5), (0.8, 0.1, -0.15)])
        # two cannon towers (2.2-2.6 s each), placed between the spoken words so the fixed blast never decides
        # the voice test of another id
        for k, t in enumerate((1.8, 4.7, 7.7, 9.2)):
            sc.one("blast", t, pan=0.25)
            for j in range(3):                      # the splash kills three at once (one frame)
                sc.kill(t + 0.004 * j, 0.25)
        for i, (note, lv, bell, flash) in enumerate(grades):
            t = 0.9 + 1.5 * i
            sc.keys(t)
            sc.word_done(t, note, lv, bell=bell, flash=flash)
            sc.kill(t + 0.38, sc.rng.choice([-0.3, 0.3]))
    elif scenario == "td-night":
        dur = 9.0
        _towers(sc, dur, [(0.8, 0.2, -0.5), (0.9, 0.55, 0.45)], kill_p=0.3)
        notes = [("C4", WORD_HIT_TIER_DB[0]), ("D4", WORD_HIT_TIER_DB[1]), ("F4", WORD_HIT_TIER_DB[1]),
                 ("G4", WORD_HIT_TIER_DB[2]), ("A4", WORD_HIT_TIER_DB[2])]
        for i, (note, lv) in enumerate(notes):
            t = 0.8 + 1.6 * i
            sc.keys(t)
            sc.word_done(t, note, lv)
            sc.kill(t + 0.38, sc.rng.choice([-0.3, 0.3]))
        for t in (1.6, 5.9):
            sc.one("call-chop", t, pan=0.0)
        sc.one("leak", 3.4, pan=-0.4)
        sc.one("leak", 7.2, pan=0.4)
    elif scenario == "td-menu":
        dur = 4.2
        for t in (0.3, 0.55, 0.78, 1.0, 1.25, 2.6, 2.85):
            sc.one("ui-move", t)
        for t in (1.9, 3.4):
            sc.one("ui-pick", t)
    else:
        raise ValueError(f"không có kịch bản {scenario!r}; có {', '.join(SCENARIOS)}")
    sc.finish()
    return sc, dur


def render_mix(sc: Scene, dur: float, profile: dict = LOI_GOI, duck_db: float = 0.0) -> dict:
    """duck_db < 0: what plan §6.2 step 4 would add (typing and world dipped from the request to the word's end,
    down 80 ms, up 400 ms like Rồng Giữ Ải); the game today ducks only the music."""
    n = int(round(dur * SR))
    pre: dict[str, np.ndarray] = {}
    for ev in sc.events:
        a = int(round(ev.t * SR))
        if a >= n:
            continue
        y = ev.audio[: n - a]
        buf = pre.setdefault(ev.bus, np.zeros((n, 2)))
        buf[a:a + y.size] += mixer.pan(y, ev.pan)
    zero = np.zeros((n, 2))
    gr_t = np.zeros(n)
    typing = pre.get("typing", zero)
    if np.any(typing):
        c = profile["typing_comp"]
        typing, gr_t = mixer.compressor(typing, c["threshold_db"], c["ratio"], c["attack_s"], c["release_s"], c["knee_db"])
    stems = {"typing": typing, "world": pre.get("world", zero) * profile["world"], "ui": pre.get("ui", zero)}
    if duck_db < 0 and sc.voices:
        ch = []
        for v in sc.voices:
            ch += [(v.t_request, mixer.db_to_gain(duck_db), 0.08 / 3), (v.t_start + v.audio.shape[0] / SR, 1.0, 0.4 / 3)]
        curve = mixer.target_curve(n, ch, start=1.0)[:, None]
        stems["typing"], stems["world"] = stems["typing"] * curve, stems["world"] * curve
    sfx = (stems["typing"] + stems["world"] + stems["ui"]) * profile["sfx"]
    wet = convolver(sfx * profile["verb_send"], profile["verb_s"]) * profile["verb_return"] if np.any(sfx) else zero
    lim = profile["limiter"]
    game, gr = mixer.compressor((sfx + wet) * profile["master"], lim["threshold_db"], lim["ratio"], lim["attack_s"],
                                lim["release_s"], lim["knee_db"])
    voice = np.zeros((n, 2))
    for v in sc.voices:
        a = int(round(v.t_start * SR))
        if a < n:
            y = mixer.pan(v.audio, 0.0)[: n - a]
            voice[a:a + y.shape[0]] += y
    return {"mix": game + voice, "game": game, "voice": voice, "pre": pre, "stems": stems, "gr_db": gr,
            "gr_typing_db": gr_t, "wet": wet}


def spacing(times: list[float], asked: list[float]) -> dict:
    """How a dense id sounds against what the simulation asked for: plays, drops, gaps, clusters."""
    t = np.array(sorted(times))
    out = {"asked": len(asked), "played": int(t.size), "dropped": len(asked) - int(t.size)}
    if t.size >= 2:
        d = np.diff(t)
        out.update({"longest_silence_s": round(float(d.max()), 3), "interval_sd_ms": round(float(d.std() * 1000), 1),
                    "max_in_250ms": int(max(np.sum((t >= x) & (t < x + 0.25)) for x in t))})
    return out


def caps_report(scenario: str, slots: dict, delay_s: float) -> dict:
    """Both configurations' schedules for the dense ids (no audio: same pattern, caps only)."""
    out = {}
    for cfg in ("current", "proposed"):
        sc, _ = build(scenario, slots, cfg, delay_s)
        out[cfg] = {sid: spacing(sc.played.get(sid, []), sc.asked.get(sid, [])) for sid in DENSE if sc.asked.get(sid)}
    return out


def _focus(sc: Scene, focus: str, dur: float) -> np.ndarray:
    n = int(round(dur * SR))
    st = np.zeros((n, 2))
    for ev in sc.events:
        if ev.slot != focus:
            continue
        a = int(round(ev.t * SR))
        y = ev.audio[: max(0, n - a)]
        st[a:a + y.size] += mixer.pan(y, ev.pan)
    return st


def render(scenario: str, slots: dict, out_wav: Path, focus: str | None = None, config: str = "proposed",
           delay_s: float = 0.15, sweep: bool = True, png: bool = True) -> dict:
    """Render one scene: <out>.wav (24-bit stereo, SCENE_GAIN_DB applied), <out>.json and <out>.png."""
    sc, dur = build(scenario, slots, config, delay_s)
    res = render_mix(sc, dur)
    starts = [v.t_start for v in sc.voices]
    m: dict = {"mix": metrics.mix_numbers(res["mix"]), "limiter": metrics.limiter_stats(res["gr_db"]),
               "typing_compressor": metrics.limiter_stats(res["gr_typing_db"])}
    if starts:
        m["voice"] = metrics.voice_clarity(res["game"], res["voice"], starts)
    if focus and focus in BUS:
        fs = _focus(sc, focus, dur)
        if np.any(fs):
            m["focus_small_speaker_loss_db"] = metrics.small_speaker_loss(fs)
            m["focus_share_1k4k_db"] = metrics.slot_share(res["pre"], fs, 1000, 4000)
            m["focus_lufs_m_max_in_mix"] = round(measure.lufs_m_max(fs, SR), 2)
            m["focus_plays"] = len(sc.played.get(focus, []))
        if focus in WORD_COMPLETE and slots.get(focus):
            v = slots[focus]
            files = list(v.values()) if isinstance(v, dict) else [v]
            decays = []
            for f in files:
                x, _ = sf.read(str(f), always_2d=True, dtype="float64")
                decays.append(metrics.band_decay(x)["drop_db_at_100ms"])
            m["focus_band_decay"] = {"drop_db_at_100ms": decays, "min_db": min(decays),
                                     "pass_15db": bool(min(decays) >= 15.0)}
    caps = caps_report(scenario, slots, delay_s)
    if caps.get("proposed"):
        m["caps"] = caps
    if sweep and starts:
        sw = []
        for duck in (0.0, -6.0):
            for d in (0.0, 0.15, 0.4):
                s2, _ = build(scenario, slots, config, d)
                r2 = render_mix(s2, dur, duck_db=duck)
                vc = metrics.voice_clarity(r2["game"], r2["voice"], [v.t_start for v in s2.voices])
                sw.append({"duck_sfx_db": duck, "delay_s": d, "min_db": vc["min_db"], "median_db": vc["median_db"]})
        m["voice_sweep"] = sw
        worst = min((r for r in sw if r["duck_sfx_db"] == 0.0), key=lambda r: r["min_db"])
        m["voice_with_duck"] = next(r for r in sw if r["duck_sfx_db"] == -6.0 and r["delay_s"] == delay_s) \
            if any(r["delay_s"] == delay_s for r in sw) else None
        m["voice_worst"] = {**worst, "min_db_voice_minus6": round(worst["min_db"] - 6.0, 1)}
    doc = {"schema": "audiolab.context.render/1", "scenario": scenario, "game": GAME, "config": config, "focus": focus,
           "slots": {k: ({kk: str(vv) for kk, vv in v.items()} if isinstance(v, dict) else str(v)) for k, v in slots.items()},
           "duration_s": dur, "voice_delay_s": delay_s, "scene_gain_db": SCENE_GAIN_BY.get(scenario, SCENE_GAIN_DB),
           "levels_lufs_m": {k: level_of(k) for k in BUS if k != "word-hit"} | {"word-hit": list(WORD_HIT_TIER_DB),
                                                                               "word-hit sloppy": SLOPPY_DB},
           "timeline": [mk for mk in sc.marks if mk["id"] != "key"],
           "words": [{"t_request": v.t_request, "t_start": v.t_start, "word": v.word, "voice": v.voice} for v in sc.voices],
           "profile": LOI_GOI["source"],
           "approximations": "Bộ nén là bộ dò đỉnh có làm mượt bắt/nhả, gối mềm bậc hai và bù mức tự động của Chromium, "
                             "không có nhìn trước 6 ms; nhiễu của vang là nhiễu có seed (game sinh ngẫu nhiên mỗi lần "
                             "nạp); khung hình đều 60 Hz; tiếng phím là tiếng tổng hợp của chính game (folk.ts go()); "
                             "giọng đọc là giọng macOS `say`, cộng sau master như speechSynthesis; chưa có nhạc nền.",
           "metrics": m}
    out_wav.parent.mkdir(parents=True, exist_ok=True)
    gain_db = SCENE_GAIN_BY.get(scenario, SCENE_GAIN_DB)
    sf.write(str(out_wav), (res["mix"] * mixer.db_to_gain(gain_db)).astype(np.float32), SR, subtype="PCM_24")
    doc["file"] = str(out_wav)
    from build import ledger
    doc["sha256"] = ledger.sha256_file(out_wav)
    if png:
        doc["card"] = str(draw(out_wav.with_suffix(".png"), res, sc, doc))
    out_wav.with_suffix(".json").write_text(json.dumps(doc, ensure_ascii=False, indent=1, default=float), "utf-8")
    return doc


def _env_db(x: np.ndarray, win_s: float = 0.01) -> tuple[np.ndarray, np.ndarray]:
    m = x.mean(axis=1) if x.ndim == 2 else x
    hop = int(win_s * SR)
    n = m.shape[0] // hop
    e = np.sqrt(np.mean(m[: n * hop].reshape(n, hop) ** 2, axis=1) + 1e-12)
    return np.arange(n) * win_s, 20 * np.log10(e)


def draw(path: Path, res: dict, sc: Scene, doc: dict) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    from critic import audio as A

    fig, ax = plt.subplots(3, 1, figsize=(15, 9), sharex=True, gridspec_kw={"height_ratios": [3, 2, 1]})
    t, g = _env_db(res["game"])
    ax[0].plot(t, g, color="0.6", lw=0.8, label="game mix (không giọng)")
    focus = doc.get("focus")
    if focus:
        fs = _focus(sc, focus, doc["duration_s"])
        if np.any(fs):
            tf, ef = _env_db(fs)
            ax[0].plot(tf, ef, color="tab:orange", lw=0.9, label=f"ứng viên: {focus} (trước bus)")
    tv, v = _env_db(res["voice"])
    ax[0].plot(tv, v, color="tab:blue", lw=0.9, label="giọng đọc")
    vc = (doc.get("metrics") or {}).get("voice") or {}
    for w, snr in zip(doc.get("words") or [], vc.get("per_word_db") or []):
        ax[0].axvspan(w["t_start"], w["t_start"] + 0.3, color="tab:green" if snr >= 10 else "tab:red", alpha=0.15)
        ax[0].text(w["t_start"], -6, f"{w['word']}\n{snr:+.0f} dB", fontsize=7, va="top")
    for mk in doc.get("timeline") or []:
        if focus and not str(mk["id"]).startswith(focus):
            continue
        ax[0].axvline(mk["t"], color="0.8", lw=0.5)
        ax[0].text(mk["t"], -73, str(mk["id"]).replace("word-hit ", ""), fontsize=6, rotation=90, va="bottom")
    ax[0].set_ylim(-75, 0)
    ax[0].set_ylabel("dBFS (RMS 10 ms)")
    ax[0].legend(loc="upper right", fontsize=8)
    gm, vm = res["game"].mean(axis=1), res["voice"].mean(axis=1)
    tb, gb = _env_db(A.band(gm, SR, 1000, 4000))
    _, vb = _env_db(A.band(vm, SR, 1000, 4000))
    ax[1].plot(tb, gb, color="0.45", lw=0.8, label="game mix 1–4 kHz")
    ax[1].plot(tb[: vb.size], vb, color="tab:blue", lw=0.8, label="giọng 1–4 kHz")
    ax[1].set_ylim(-85, -5)
    ax[1].legend(loc="upper right", fontsize=8)
    tg = np.arange(res["gr_db"].size) / SR
    ax[2].plot(tg, res["gr_db"], color="tab:red", lw=0.8, label="bộ giới hạn master (dB ép)")
    ax[2].plot(tg, res["gr_typing_db"], color="tab:purple", lw=0.7, label="nén bus typing (dB ép)")
    ax[2].set_ylim(-10, 0.5)
    ax[2].set_xlabel("s")
    ax[2].legend(loc="lower right", fontsize=7, ncol=2)
    m = doc.get("metrics") or {}
    title = (f"{doc['scenario']} · {doc['config']} · {Path(path).stem} · giọng 1–4 kHz min {vc.get('min_db')} dB · "
             f"tệ nhất (quét) {(m.get('voice_worst') or {}).get('min_db')} dB · đỉnh {m['mix']['true_peak_dbtp']} dBTP · "
             f"ép >3 dB {m['limiter']['time_over_3db_pct']} % · loa nhỏ (ứng viên) {m.get('focus_small_speaker_loss_db')} dB")
    fig.suptitle(title, fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=80)
    plt.close(fig)
    return path
