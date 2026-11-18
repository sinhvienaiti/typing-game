"""Tuyến Cuối scenarios: "Liên thanh 3 s" and friends (BATCH1_BRIEF §3.3, §3.5, §4.1).

Numbers from the game's audio code (games/typing-survival, read only, 24/10/2026):
  - src/audio/theme-audio.ts BUSES: guns 0.42 (duck 0.5), impacts 0.6 (0.5), kills 0.55 (0.56), alerts 0.8 (0.8),
    keys 0.5 (0.6); each bus insert = level gain -> DynamicsCompressorNode (threshold -12 dB, knee 6, ratio 8,
    attack 2 ms, release 140 ms) -> the kit bus node (gain x duck, setTargetAtTime tau 50 ms) -> master; no master
    limiter. HIT_GATHER_MS 38, kill bursts at most 4 in 120 ms.
  - src/view/combat.ts:139 a sound for even rounds only; theme-audio.ts:145 every sound starts at the frame's
    currentTime; kit SceneAudio: one file per id, playbackRate x U(0.95, 1.05) for every sound, the duck starts when
    the spoken word starts (PRONUNCIATION_EVENT).
  - content/guns.ts XUNG: 24 rounds in 2.4 s (10 rounds/s); kit feedback tiers: T2-T3 add the low layer, T4+ the tail.

Two playback configurations (BATCH1_BRIEF §3.3):
  current   the game today: even rounds only, one file, +-5 % rate, starts on 60 Hz frame boundaries, no bed or
            tail, every bus compressor 2 ms / 140 ms, duck from the voice start.
  proposed  the contract for the wiring step: every round, sets A and B alternating, simulation time, a mechanical
            bed under the burst (gun.xung.loop, in 45 ms, out 100 ms) and gun.xung.tail at ceasefire, at most
            4 gun voices (the oldest is stolen with a 25 ms fade), the same id at least 30 ms apart, pitch and
            level per the brief (A +-40 cent, B +-70 cent, +-1 dB; other ids per their card), guns and impacts
            compressors 15 ms / 300 ms, duck from the request.

Levels: one-shots enter their bus at the card's proposed file level (LUFS-M max -20), so every candidate of an id
sits at the same level; the shots of a gun set are scaled together so the stream of rounds reaches the same
LUFS-S max for every candidate (BATCH1_BRIEF §3.5: "stem súng ... cùng LUFS-S max"), which keeps the A/B step of
a set. The bed sits `bed_db` under the mean LUFS-M max of the A shots (-16 or -11 dB), the ceasefire tail 4 dB
under it. The spoken word (speechSynthesis) is outside the game's graph: added after the master.
Approximations (said in every report): the compressor is a peak detector with attack/release smoothing and
Chromium's make-up gain, without the 6 ms look-ahead; frames are an even 60 Hz.

Scenarios:
  ts-xung-3s        two words 1.4 s apart, Xung firing 0.05-2.95 s (30 rounds), hits 150-300 ms after each round
                    (T1, 9 % T2 with the low layer), one big hit (T4: head, low layer, tail) at 2.30 s, ceasefire
                    at 3.05 s. 4.0 s.
  ts-xung-3s-kills  the same with kills (35 % of hits break a swarm foe, at most 4 in 120 ms), an elite at 1.90 s
                    and the second word perfect (word.perfect). 4.0 s.
  ts-tia-3s         a word, then Tia for 2.5 s: one pulse every 0.1 s on foes (gun.tia.pulse), kills. 3.4 s.
  ts-breach         Xung firing, two words, the line breached at 1.20 s (hurt.breach). 3.2 s.
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
GAME = "typing-survival"
SCENARIOS = ("ts-xung-3s", "ts-xung-3s-kills", "ts-tia-3s", "ts-breach")
FRAME_S = 1.0 / 60.0
ONE_SHOT_LUFS_M = -20.0          # cards: loudness.proposal lufs-m-max -20 (plan §4.3.3, §5.1 step 4)
GUN_STREAM_LUFS_S = -20.0        # every gun set: the stream of rounds at the same LUFS-S max
TAIL_UNDER_SHOT_DB = 4.0
SCENE_GAIN_DB = -6.0             # every render: near the board's -23 LUFS-M target, same for all items

TYPING_SURVIVAL = {
    "game": GAME,
    "source": "games/typing-survival/src/audio/theme-audio.ts BUSES and bus inserts, src/kit/audio/scene-audio.ts (read 24/10/2026)",
    "buses": {"keys": (0.5, 0.6), "guns": (0.42, 0.5), "impacts": (0.6, 0.5), "kills": (0.55, 0.56),
              "alerts": (0.8, 0.8), "ui": (0.55, 0.7), "music": (0.9, 0.63)},
    "duck_tau_s": 0.05,
    "comp": {"threshold_db": -12.0, "knee_db": 6.0, "ratio": 8.0, "attack_s": 0.002, "release_s": 0.14},
    "comp_proposed": {"guns": {"attack_s": 0.015, "release_s": 0.30}, "impacts": {"attack_s": 0.015, "release_s": 0.30}},
}
BUS = {"gun.xung": "guns", "gun.xung.loop": "guns", "gun.xung.tail": "guns", "hit.t1": "impacts", "hit.t2": "impacts",
       "hit.t4": "impacts", "gun.tia.pulse": "impacts", "kill.swarm": "kills", "kill.elite": "kills",
       "word.load": "alerts", "word.perfect": "alerts", "hurt.breach": "alerts"}
GUN_CENTS = {"A": 40.0, "B": 70.0}
GUN_DB = 1.0
MAX_GUN_VOICES = 4
STEAL_FADE_S = 0.025
SAME_ID_GAP_S = 0.030


def card(sid: str) -> dict:
    p = env.LAB / "specs" / GAME / f"{sid}.yaml"
    return (yaml.safe_load(p.read_text("utf-8")) or {}) if p.is_file() else {}


def card_rand(sid: str) -> tuple[float, float]:
    r = card(sid).get("randomisation") or {}
    return float(r.get("pitch_cents") or 0.0), float(r.get("gain_db") or 0.0)


_CACHE: dict[str, np.ndarray] = {}


def load_mono(path: Path, lufs_m: float | None = ONE_SHOT_LUFS_M) -> np.ndarray:
    """The file at 48 kHz, mono (the cards say mono), at `lufs_m` LUFS-M max (None: as stored)."""
    key = f"{path}|{lufs_m}"
    if key in _CACHE:
        return _CACHE[key]
    x, sr = sf.read(str(path), always_2d=True, dtype="float64")
    if sr != SR:
        import soxr
        x = soxr.resample(x, sr, SR, quality="VHQ")
    m = x.mean(axis=1)
    if lufs_m is not None:
        m = m * mixer.db_to_gain(lufs_m - measure.lufs_m_max(m, SR))
    _CACHE[key] = m
    return m


def _files(v) -> list[Path]:
    if v is None:
        return []
    if isinstance(v, (str, Path)):
        return [Path(v).expanduser()]
    return [Path(p).expanduser() for p in v]


@dataclass
class Ev:
    t: float
    audio: np.ndarray            # mono
    bus: str
    pan: float = 0.0
    slot: str = ""
    label: str = ""
    gun: bool = False            # counts toward the 4-voice cap of the weapon
    fade_in_s: float = 0.0
    fade_out_s: float = 0.0


@dataclass
class Scene:
    scenario: str
    config: str
    events: list[Ev] = field(default_factory=list)
    voices: list[mixer.Voice] = field(default_factory=list)
    marks: list[dict] = field(default_factory=list)
    rounds: list[float] = field(default_factory=list)      # scheduled times of the rounds that sound
    fire: tuple[float, float] | None = None                 # firing span (first round, ceasefire)
    played: list[str] = field(default_factory=list)          # gun files in play order (variant repetition)
    notes: list[str] = field(default_factory=list)
    stem_bus: str = "guns"                                  # the bus the burst numbers read


class Builder:
    def __init__(self, scenario: str, slots: dict, config: str, delay_s: float, bed_db: float):
        self.sc = Scene(scenario, config)
        self.slots, self.config, self.delay, self.bed_db = slots, config, delay_s, bed_db
        self.pat = random.Random(f"{scenario}:pattern")       # timing, tiers, pans: same for every candidate
        self.var = random.Random(f"{scenario}:variants")      # which variant, pitch, level
        self.last: dict[str, list[int]] = {}
        self.word = 0

    # -- timing and variation
    def when(self, t: float) -> float:
        return float(np.ceil(t / FRAME_S - 1e-9) * FRAME_S) if self.config == "current" else t

    def jitter(self, sid: str, key: str | None = None) -> tuple[float, float]:
        if self.config == "current":                          # kit SceneAudio: playbackRate x U(0.95, 1.05)
            return 1200 * np.log2(self.var.uniform(0.95, 1.05)), 0.0
        if key in GUN_CENTS:
            c, d = GUN_CENTS[key], GUN_DB
        else:
            c, d = card_rand(sid)
        return self.var.uniform(-c, c), self.var.uniform(-d, d)

    def pick(self, sid: str, files: list[Path]) -> Path:
        """Random variant, never one of the last two (plan §5.3); the current game has one file per id."""
        if len(files) == 1 or self.config == "current":
            return files[0]
        recent = self.last.setdefault(sid, [])
        avoid = min(2, len(files) - 1)
        k = self.var.randrange(len(files))
        for _ in range(50):
            if k not in recent[-avoid:]:
                break
            k = self.var.randrange(len(files))
        recent.append(k)
        return files[k]

    def one(self, sid: str, t: float, pan: float = 0.0, key: str | None = None, files=None, label: str | None = None,
            gun: bool = False, lufs_m: float | None = ONE_SHOT_LUFS_M, gain_db: float = 0.0) -> Ev | None:
        fl = files if files is not None else _files(self.slots.get(sid))
        if not fl:
            return None
        f = self.pick(f"{sid}:{key}" if key else sid, fl)
        cents, db = self.jitter(sid, key)
        y = mixer.varispeed(load_mono(f, lufs_m), cents) * mixer.db_to_gain(db + gain_db)
        ev = Ev(t=self.when(t), audio=y, bus=BUS[sid], pan=pan, slot=sid, label=label or sid, gun=gun)
        self.sc.events.append(ev)
        self.sc.marks.append({"t": round(ev.t, 4), "id": label or sid, "file": f.name, "cents": round(cents, 1),
                              "db": round(db + gain_db, 2), "pan": pan})
        return ev

    # -- game actions
    def word_done(self, t: float, perfect: bool = False):
        w = voices.WORDS[self.word % len(voices.WORDS)]
        v = voices.VOICES[self.word % len(voices.VOICES)]
        self.word += 1
        sid = "word.perfect" if perfect and self.slots.get("word.perfect") else "word.load"
        self.one(sid, t, pan=-0.35)
        self.sc.voices.append(mixer.Voice(t_request=t, t_start=t + self.delay, audio=voices.load(v, w), word=w, voice=v))

    def burst(self, t0: float, n: int, ceasefire: float):
        """n rounds every 100 ms from t0; the gun's sounds by configuration."""
        gun = self.slots.get("gun.xung")
        sets = gun if isinstance(gun, dict) else {"A": _files(gun)}
        # "B_db" (batch 1c): set B is set A's whole takes played lower (BATCH1_BRIEF §3.2: B 4-6 dB under A);
        # the batch 1 sets are rendered files, B already lower, no offset
        b_db = float(sets.get("B_db") or 0.0)
        rounds = [t0 + 0.1 * k for k in range(n)]
        self.sc.fire = (t0, ceasefire)
        shots: list[Ev] = []
        for k, t in enumerate(rounds):
            if self.config == "current" and k % 2:
                continue                                        # combat.ts:139: even rounds only
            key = "A" if (k % 2 == 0 or "B" not in sets) else "B"
            ev = self.one("gun.xung", t, pan=0.0, key=key if self.config != "current" else None, files=sets[key],
                          label=f"gun.xung.{key}", gun=True, lufs_m=None, gain_db=b_db if key == "B" else 0.0)
            if ev is not None:
                shots.append(ev)
                self.sc.rounds.append(ev.t)
                self.sc.played.append(self.sc.marks[-1]["file"])
        # one gain for the whole stream: the same LUFS-S max for every candidate set
        if shots:
            n_s = int((ceasefire + 0.6) * SR)
            st = np.zeros(n_s)
            for ev in shots:
                a = int(round(ev.t * SR))
                y = ev.audio[: max(0, n_s - a)]
                st[a:a + y.size] += y
            g = mixer.db_to_gain(GUN_STREAM_LUFS_S - measure.lufs_s_max(st, SR))
            for ev in shots:
                ev.audio = ev.audio * g
            a_lvl = [measure.lufs_m_max(load_mono(f, None) * g, SR) for f in sets.get("A", [])]
            self.shot_lufs_m = float(np.mean(a_lvl)) if a_lvl else GUN_STREAM_LUFS_S
            self.sc.notes.append(f"stream gain {20 * np.log10(g):+.1f} dB; A shot LUFS-M max {self.shot_lufs_m:.1f}")
        if self.config == "proposed":
            loop = _files(self.slots.get("gun.xung.loop"))
            if loop and shots:
                y = load_mono(loop[0], None)
                y = y * mixer.db_to_gain(self.shot_lufs_m - self.bed_db - measure.lufs_m_max(y, SR))
                start = int(self.pat.random() * y.size)          # each burst starts somewhere in the loop
                y = np.concatenate([y[start:], y[:start]])
                span = int((ceasefire + 0.1 - t0) * SR)
                y = np.tile(y, int(np.ceil(span / y.size)) + 1)[:span]
                self.sc.events.append(Ev(t=t0, audio=y, bus="guns", slot="gun.xung.loop", label="gun.xung.loop",
                                         fade_in_s=0.045, fade_out_s=0.1))
                self.sc.marks.append({"t": t0, "id": "gun.xung.loop", "file": loop[0].name, "until": ceasefire + 0.1,
                                      "db_under_shot": self.bed_db})
            tail = _files(self.slots.get("gun.xung.tail"))
            if tail and shots:
                y = load_mono(tail[0], None)
                y = y * mixer.db_to_gain(self.shot_lufs_m - TAIL_UNDER_SHOT_DB - measure.lufs_m_max(y, SR))
                self.sc.events.append(Ev(t=ceasefire, audio=y, bus="guns", slot="gun.xung.tail", label="gun.xung.tail"))
                self.sc.marks.append({"t": ceasefire, "id": "gun.xung.tail", "file": tail[0].name})
        return rounds

    def hits(self, rounds: list[float], kills: float = 0.0, t4_at: float | None = None):
        """Each round hits 150-300 ms later (T1, 9 % T2: crit 5 % + clean 4 %), gathered for 38 ms."""
        raw = []
        for t in rounds:
            raw.append((t + self.pat.uniform(0.15, 0.30), 2 if self.pat.random() < 0.09 else 1, self.pat.uniform(-0.5, 0.5)))
        raw.sort()
        groups, cur = [], None
        for t, tier, pan in raw:
            if cur is None or t - cur[0] >= 0.038:
                cur = [t, tier, [pan]]
                groups.append(cur)
            else:
                cur[1] = max(cur[1], tier)
                cur[2].append(pan)
        if t4_at is not None:
            groups.append([t4_at, 4, [0.1]])
        kill_times: list[float] = []
        for t, tier, pans in sorted(groups, key=lambda g: g[0]):
            pan = float(np.mean(pans))
            at = t + 0.038
            sid = "hit.t4" if tier >= 4 else "hit.t2" if tier >= 2 else "hit.t1"
            if not self.slots.get(sid):
                sid = "hit.t1"
            self.one(sid, at, pan=pan)
            if kills > 0 and tier < 4 and self.pat.random() < kills:
                kt = t + self.pat.uniform(0.0, 0.01)
                recent = [k for k in kill_times if kt - k <= 0.12]
                if len(recent) < 4:                           # theme-audio.ts BURSTS: 4 in 120 ms
                    kill_times.append(kt)
                    self.one("kill.swarm", kt, pan=pan)


def build(scenario: str, slots: dict, config: str = "proposed", delay_s: float = 0.15, bed_db: float = 16.0) -> tuple[Scene, float]:
    b = Builder(scenario, slots, config, delay_s, bed_db)
    b.shot_lufs_m = GUN_STREAM_LUFS_S
    if scenario in ("ts-xung-3s", "ts-xung-3s-kills"):
        dur = 4.0
        kills = scenario.endswith("kills")
        b.word_done(0.0)
        rounds = b.burst(0.05, 30, 3.05)
        b.word_done(1.40, perfect=kills)
        b.hits(rounds, kills=0.35 if kills else 0.0, t4_at=2.30)
        if kills:
            b.one("kill.elite", 1.90, pan=0.2)
    elif scenario == "ts-tia-3s":
        dur = 3.4
        b.word_done(0.0)
        b.sc.fire = (0.05, 2.55)
        b.sc.stem_bus = "impacts"
        for k in range(25):
            t = 0.05 + 0.1 * k
            ev = b.one("gun.tia.pulse", t, pan=b.pat.uniform(-0.3, 0.3))
            if ev is not None:
                b.sc.rounds.append(ev.t)
            if b.pat.random() < 0.25:
                b.one("kill.swarm", t + 0.02, pan=b.pat.uniform(-0.5, 0.5))
        b.word_done(1.40)
    elif scenario == "ts-breach":
        dur = 3.2
        b.word_done(0.0)
        rounds = b.burst(0.05, 24, 2.45)
        b.hits(rounds)
        b.one("hurt.breach", 1.20, pan=0.0)
        b.word_done(1.80)
    else:
        raise ValueError(f"không có kịch bản {scenario!r}; có {', '.join(SCENARIOS)}")
    _cap_gun_voices(b.sc)
    return b.sc, dur


def _cap_gun_voices(sc: Scene) -> None:
    """At most 4 gun voices; a new one steals the oldest with a 25 ms fade; the same id 30 ms apart."""
    if sc.config != "proposed":
        return
    active: list[Ev] = []
    for ev in sorted([e for e in sc.events if e.gun], key=lambda e: e.t):
        active = [a for a in active if a.t + a.audio.size / SR > ev.t]
        if len(active) >= MAX_GUN_VOICES:
            old = min(active, key=lambda a: a.t)
            keep = int((ev.t - old.t) * SR)
            f = int(STEAL_FADE_S * SR)
            y = old.audio[: keep + f].copy()
            y[keep:] *= np.linspace(1.0, 0.0, y.size - keep)
            old.audio = y
            active.remove(old)
        active.append(ev)


# ---------------------------------------------------------------- the mix

def render_mix(sc: Scene, dur: float, profile: dict = TYPING_SURVIVAL, duck_from: str | None = None) -> dict:
    n = int(round(dur * SR))
    pre: dict[str, np.ndarray] = {}
    for ev in sc.events:
        a = int(round(ev.t * SR))
        if a >= n:
            continue
        y = ev.audio[: n - a].copy()
        if ev.fade_in_s:
            k = min(y.size, int(ev.fade_in_s * SR))
            y[:k] *= np.linspace(0, 1, k)
        if ev.fade_out_s:
            k = min(y.size, int(ev.fade_out_s * SR))
            y[-k:] *= np.linspace(1, 0, k)
        buf = pre.setdefault(ev.bus, np.zeros((n, 2)))
        buf[a:a + y.size] += mixer.pan(y, ev.pan)
    duck_from = duck_from or ("voice" if sc.config == "current" else "request")
    comp, post, gr, duck = {}, {}, {}, {}
    for bus, x in pre.items():
        c = dict(profile["comp"])
        if sc.config == "proposed":
            c.update(profile["comp_proposed"].get(bus, {}))
        y, g = mixer.compressor(x, c["threshold_db"], c["ratio"], c["attack_s"], c["release_s"], c["knee_db"])
        gain, dk = profile["buses"][bus]
        ch = []
        for v in sc.voices:
            t0 = v.t_request if duck_from == "request" else v.t_start
            ch += [(t0, dk, profile["duck_tau_s"]), (v.t_start + v.audio.shape[0] / SR, 1.0, profile["duck_tau_s"])]
        curve = mixer.target_curve(n, ch, start=1.0) if ch else np.ones(n)
        comp[bus], gr[bus], duck[bus] = y, g, curve
        post[bus] = y * gain * curve[:, None]
    game = sum(post.values()) if post else np.zeros((n, 2))
    voice = np.zeros((n, 2))
    for v in sc.voices:
        a = int(round(v.t_start * SR))
        if a < n:
            y = mixer.pan(v.audio, 0.0)[: n - a]
            voice[a:a + y.shape[0]] += y
    return {"mix": game + voice, "game": game, "voice": voice, "pre": pre, "comp": comp, "stems": post,
            "gr": gr, "duck": duck, "duck_from": duck_from}


# ---------------------------------------------------------------- burst numbers (BATCH1_BRIEF §3.5)

def _env_db(x: np.ndarray, win_s: float = 0.005, hop_s: float = 0.001) -> tuple[np.ndarray, np.ndarray]:
    m = x.mean(axis=1) if x.ndim == 2 else x
    win, hop = int(win_s * SR), int(hop_s * SR)
    c = np.concatenate([[0.0], np.cumsum(m ** 2)])
    starts = np.arange(0, max(1, m.size - win), hop)
    e = (c[starts + win] - c[starts]) / win
    return (starts + win / 2) / SR, 10 * np.log10(e + 1e-14)


def burst_numbers(res: dict, sc: Scene) -> dict:
    out: dict = {"stem_bus": sc.stem_bus}
    guns = res["comp"].get(sc.stem_bus)
    if guns is None or not sc.rounds or sc.fire is None:
        return out
    t, e = _env_db(guns)
    r = sorted(sc.rounds)
    dips = []
    for a, b in zip(r, r[1:]):
        pk = e[(t >= a) & (t < a + 0.03)]
        tr = e[(t >= a + 0.02) & (t < b + 0.002)]
        if pk.size and tr.size:
            dips.append(min(60.0, float(pk.max() - tr.min())))     # digital silence: capped at 60 dB
    if dips:
        out["dip_median_db"] = round(float(np.median(dips)), 1)
        out["dip_max_db"] = round(float(np.max(dips)), 1)
        out["dip_pass"] = bool(np.median(dips) <= 12.0 and np.max(dips) <= 18.0)
    f0, f1 = sc.fire[0], r[-1] + 0.1
    sel = (t >= f0) & (t < f1)
    win = int(0.3 / 0.001)
    from scipy.ndimage import maximum_filter1d
    ref = maximum_filter1d(e, size=win, mode="nearest")
    gap = float(np.mean((e[sel] < ref[sel] - 20.0))) if np.any(sel) else None
    out["gap_time_pct"] = None if gap is None else round(100 * gap, 1)
    out["gap_pass"] = gap is not None and gap <= 0.05
    # onset regularity: detected rises on the gun stem vs a perfectly even grid
    on = []
    for a in r:                       # the first point within 6 dB of the round's own 30 ms peak (the crack's front)
        w = np.flatnonzero((t >= a - 0.004) & (t < a + 0.03))
        if w.size:
            k = w[np.argmax(e[w] >= e[w].max() - 6.0)]
            on.append(float(t[k]))
    if len(on) > 2:
        iv = np.diff(on)
        out["onset_interval_ms"] = round(1000 * float(np.median(iv)), 1)
        out["onset_sd_ms"] = round(1000 * float(np.std(iv)), 2)
        out["onset_pass"] = bool(np.std(iv) * 1000 <= 8.0)
    # force: the gun stem (pre bus gain) over the firing span
    from critic import audio as A
    gm = guns.mean(axis=1)[int(f0 * SR):int(f1 * SR)]
    tot = float(np.sum(gm ** 2)) + 1e-14

    def share(lo, hi):
        return float(np.sum(A.band(gm, SR, lo, hi) ** 2)) / tot
    sh = {"40_150": share(40, 150), "150_500": share(150, 500), "2k_6k": share(2000, 6000)}
    out["stem_share"] = {k: round(v, 3) for k, v in sh.items()}
    out["force_bands_pass"] = bool(0.20 <= sh["40_150"] <= 0.40 and sh["150_500"] >= 0.25 and 0.05 <= sh["2k_6k"] <= 0.15)
    out["small_speaker_loss_db"] = metrics.small_speaker_loss(guns[int(f0 * SR):int(f1 * SR)])
    out["small_speaker_pass"] = out["small_speaker_loss_db"] is not None and out["small_speaker_loss_db"] <= 4.0
    g = -res["gr"][sc.stem_bus][int(f0 * SR):int(f1 * SR)]
    out["pump_median_db"] = round(float(np.median(g)), 2)
    out["pump_swing_db"] = round(float(np.percentile(g, 90) - np.percentile(g, 10)), 2)
    out["pump_pass"] = bool(np.median(g) <= 3.0 and out["pump_swing_db"] <= 2.0)
    # ceasefire: no drop over 6 dB within 10 ms after the last round; down 60 dB within 800 ms
    st = res["stems"][sc.stem_bus]
    ts, es = _env_db(st, 0.02)                    # 20 ms RMS: noise and ringing beat by +-5 dB at 5 ms
    fire_lvl = float(np.percentile(es[(ts >= f0) & (ts < r[-1])], 90))
    # the floor is the -60 dB the ceasefire must reach: a step from -85 to digital silence (an exponential
    # tail meeting the file's end) is inaudible and is not a cut
    es = np.maximum(es, fire_lvl - 60.0)
    last = max(r[-1] + 0.06, sc.fire[1] - 0.01)    # from the ceasefire (the last round's own decay is not a cut)
    after = (ts >= last) & (ts < last + 0.8)
    if np.any(after):
        ea = es[after]
        k10 = 10
        drops = ea[:-k10] - ea[k10:] if ea.size > k10 else np.array([0.0])
        out["stop_max_drop_10ms_db"] = round(float(drops.max()), 1)
        below = np.flatnonzero(ea <= fire_lvl - 60.0)
        out["stop_to_minus60_ms"] = round(1000 * float(ts[after][below[0]] - r[-1]), 0) if below.size else None
        out["stop_pass"] = bool(drops.max() <= 6.0 and below.size > 0)
    rep = sum(1 for a, b in zip(sc.played, sc.played[1:]) if a == b)
    out["repeat_in_a_row"] = rep
    out["repeat_pass"] = rep == 0 or sc.config == "current"
    return out


# ---------------------------------------------------------------- render

def render(scenario: str, slots: dict, out_wav: Path, focus: str | None = None, config: str = "proposed",
           delay_s: float = 0.15, bed_db: float = 16.0, sweep: bool = True, png: bool = True) -> dict:
    sc, dur = build(scenario, slots, config, delay_s, bed_db)
    res = render_mix(sc, dur)
    m: dict = {"mix": metrics.mix_numbers(res["mix"]),
               "game_peak_dbtp": round(measure.true_peak_db(res["game"], SR), 2)}
    starts = [v.t_start for v in sc.voices]
    if starts:
        m["voice"] = metrics.voice_clarity(res["game"], res["voice"], starts)
    m["burst"] = burst_numbers(res, sc)
    if focus and focus in BUS:
        fstem = _focus(sc, focus, dur)
        if np.any(fstem):
            m["focus_small_speaker_loss_db"] = metrics.small_speaker_loss(fstem)
            m["focus_share_1k4k_db"] = metrics.slot_share(res["pre"], fstem, 1000, 4000)
        fl = slots.get(focus)
        if focus in ("word.load", "word.perfect") and fl:
            x, _ = sf.read(str(_files(fl if not isinstance(fl, dict) else fl.get("A"))[0]), always_2d=True, dtype="float64")
            m["focus_band_decay"] = metrics.band_decay(x)
    if sweep and starts:
        sw = []
        for d in (0.0, 0.15, 0.4):
            s2, _ = build(scenario, slots, config, d, bed_db)
            r2 = render_mix(s2, dur)
            vc = metrics.voice_clarity(r2["game"], r2["voice"], [v.t_start for v in s2.voices])
            sw.append({"duck_from": r2["duck_from"], "delay_s": d, "min_db": vc["min_db"], "median_db": vc["median_db"]})
        m["voice_sweep"] = sw
        worst = min(sw, key=lambda r: r["min_db"])
        m["voice_worst"] = {**worst, "min_db_voice_minus6": round(worst["min_db"] - 6.0, 1)}
    doc = {"schema": "audiolab.context.render/1", "scenario": scenario, "game": GAME, "config": config, "focus": focus,
           "slots": {k: ({kk: (vv if isinstance(vv, (int, float)) else [str(p) for p in _files(vv)])
                          for kk, vv in v.items()} if isinstance(v, dict)
                         else [str(p) for p in _files(v)]) for k, v in slots.items()},
           "duration_s": dur, "voice_delay_s": delay_s, "duck_from": res["duck_from"], "bed_db_under_shot": bed_db,
           "scene_gain_db": SCENE_GAIN_DB, "timeline": sc.marks, "notes": sc.notes,
           "words": [{"t_request": v.t_request, "t_start": v.t_start, "word": v.word, "voice": v.voice} for v in sc.voices],
           "profile": TYPING_SURVIVAL["source"],
           "approximations": "Bộ nén là bộ dò đỉnh có làm mượt bắt/nhả cộng bù mức tự động của Chromium, không có nhìn "
                             "trước 6 ms; khung hình đều 60 Hz; giọng đọc là giọng macOS `say`, cộng sau master như "
                             "speechSynthesis; chưa có nhạc nền và kill.chime (tổng hợp trong mã).",
           "metrics": m}
    out_wav.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(out_wav), (res["mix"] * mixer.db_to_gain(SCENE_GAIN_DB)).astype(np.float32), SR, subtype="PCM_24")
    doc["file"] = str(out_wav)
    from build import ledger
    doc["sha256"] = ledger.sha256_file(out_wav)
    if png:
        doc["card"] = str(draw(out_wav.with_suffix(".png"), res, sc, doc))
    out_wav.with_suffix(".json").write_text(json.dumps(doc, ensure_ascii=False, indent=1, default=float), "utf-8")
    return doc


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


def draw(path: Path, res: dict, sc: Scene, doc: dict) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    from critic import audio as A

    fig, ax = plt.subplots(3, 1, figsize=(15, 9), sharex=True, gridspec_kw={"height_ratios": [3, 2, 1]})
    t, g = _env_db(res["game"], 0.01, 0.005)
    ax[0].plot(t, g, color="0.6", lw=0.8, label="game mix (không giọng)")
    if "guns" in res["comp"]:
        tg, eg = _env_db(res["stems"]["guns"])
        ax[0].plot(tg, eg, color="tab:orange", lw=0.6, label="stem súng (RMS 5 ms)")
    focus = doc.get("focus")
    if focus and focus not in ("gun.xung", "gun.xung.loop", "gun.xung.tail"):
        fs = _focus(sc, focus, doc["duration_s"])
        if np.any(fs):
            tf, ef = _env_db(fs, 0.01, 0.005)
            ax[0].plot(tf, ef, color="tab:purple", lw=0.9, label=f"ứng viên: {focus} (trước bus)")
    tv, v = _env_db(res["voice"], 0.01, 0.005)
    ax[0].plot(tv, v, color="tab:blue", lw=0.9, label="giọng đọc")
    vc = (doc.get("metrics") or {}).get("voice") or {}
    for w, snr in zip(doc.get("words") or [], vc.get("per_word_db") or []):
        ax[0].axvspan(w["t_start"], w["t_start"] + 0.3, color="tab:green" if snr >= 10 else "tab:red", alpha=0.15)
        ax[0].text(w["t_start"], -6, f"{w['word']}\n{snr:+.0f} dB", fontsize=7, va="top")
    for r_ in sc.rounds:
        ax[0].axvline(r_, color="0.85", lw=0.4)
    if sc.fire:
        ax[0].axvline(sc.fire[1], color="k", lw=0.8, ls="--")
    ax[0].set_ylim(-75, 0)
    ax[0].set_ylabel("dBFS")
    ax[0].legend(loc="upper right", fontsize=8)
    gm, vm = res["game"].mean(axis=1), res["voice"].mean(axis=1)
    tb, gb = _env_db(A.band(gm, SR, 1000, 4000), 0.01, 0.005)
    _, vb = _env_db(A.band(vm, SR, 1000, 4000), 0.01, 0.005)
    ax[1].plot(tb, gb, color="0.45", lw=0.8, label="game mix 1–4 kHz")
    ax[1].plot(tb[: vb.size], vb, color="tab:blue", lw=0.8, label="giọng 1–4 kHz")
    ax[1].set_ylim(-85, -5)
    ax[1].legend(loc="upper right", fontsize=8)
    tt = np.arange(next(iter(res["gr"].values())).size) / SR if res["gr"] else np.zeros(1)
    for bus, c in res["gr"].items():
        ax[2].plot(tt, c, lw=0.7, label=f"nén {bus}")
    for bus, c in res["duck"].items():
        if np.any(c < 0.999):
            ax[2].plot(tt, 20 * np.log10(np.maximum(c, 1e-4)), lw=0.6, ls=":", label=f"hạ {bus}")
    ax[2].set_ylim(-12, 0.5)
    ax[2].set_xlabel("s")
    ax[2].legend(loc="lower right", fontsize=7, ncol=4)
    b = (doc.get("metrics") or {}).get("burst") or {}
    title = (f"{doc['scenario']} · {doc['config']} · {Path(path).stem} · trũng {b.get('dip_median_db')}/{b.get('dip_max_db')} dB · "
             f"hổng {b.get('gap_time_pct')} % · nhịp sd {b.get('onset_sd_ms')} ms · loa nhỏ {b.get('small_speaker_loss_db')} dB · "
             f"bơm {b.get('pump_median_db')}/{b.get('pump_swing_db')} dB · giọng min {vc.get('min_db')} dB · "
             f"đỉnh {doc['metrics']['mix']['true_peak_dbtp']} dBTP")
    fig.suptitle(title, fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=80)
    plt.close(fig)
    return path
