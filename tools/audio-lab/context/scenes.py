"""Scenarios: candidates in a short game-like scene (BATCH1_BRIEF §3.5, §4.2, §7).

Rồng Giữ Ải (games/dragon-hold, read only):
  dh-cast-chain  word complete -> fire.cast (world, pan 0) and the spoken word -> fire.impact 0.6 s later,
                 one word every 1.5 s (40 WPM), impacts in the turn of map-events.ts (a, b) with the big
                 hit (c: tier 3+, perfect, flash) every third word; the forest bed under it. 9.6 s.
  dh-pack        a pack of quadrupeds arrives: their march loop fades in, a howl at 1.0 s and 4.6 s
                 (catalog gap 1.5 s), two words with fire.cast and impacts. 8 s.
  dh-trap        a swarm on the lane, words every 1.5 s, the pine bomb goes off at 2.2 s and 5.2 s. 7 s.
  dh-beds        the forest bed 3 times over (18 s) with the river, the wave horn at 3 s, the swarm and
                 quadruped marches coming in, the general's horn at 9.5 s, then four words of combat.
A slot is an id; each render puts one candidate in its slot and keeps every other slot fixed, so the
renders of one listening item differ only by that candidate. The random pitch, level and pan pattern
depends on the scenario only (same for every candidate).
"""
from __future__ import annotations

import json
import random
from pathlib import Path

import numpy as np
import soundfile as sf
import yaml

from build import measure
from common import env

from . import metrics, mixer, voices

SR = mixer.SR
SCENE_GAIN_DB = -4.0       # every render: impacts near the board's -23 LUFS-M target, same for all items
GAME = "dragon-hold"
IMPACT_GAIN_DB = {"a": 20 * np.log10(0.85), "b": 20 * np.log10(0.85), "c": 0.0}    # map-events.ts gain 0.85 / 1
# catalog.ts gainDb of the beds, relative to amb.forest (-10): river -18, swarm -17, quadruped -16
BED_REL_DB = {"amb.forest": 0.0, "amb.river": -8.0, "enemy.swarm.march": -7.0, "enemy.quadruped.march": -6.0}
FOREST_LUFS_I = -26.0      # card loudness.mix_target text: "LUFS-I theo tài liệu game (nền −26)"
BUS = {"fire.cast": "world", "fire.impact.a": "world", "fire.impact.b": "world", "fire.impact.c": "world",
       "enemy.quadruped.howl": "enemies", "trap.pine-bomb.trigger": "traps", "wave.horn": "stingers",
       "general.g01.horn": "enemies", "amb.forest": "ambience", "amb.river": "ambience",
       "enemy.swarm.march": "enemies", "enemy.quadruped.march": "enemies"}
SCENARIOS = ("dh-cast-chain", "dh-pack", "dh-trap", "dh-beds")
CARD_CENTS = {"fire.cast": 30, "fire.impact.a": 80, "fire.impact.b": 80, "fire.impact.c": 80,
              "enemy.quadruped.howl": 70, "trap.pine-bomb.trigger": 0}


def card(sid: str) -> dict:
    return yaml.safe_load((env.LAB / "specs" / GAME / f"{sid}.yaml").read_text("utf-8")) or {}


def mix_target(sid: str) -> tuple[str, float]:
    """(metric, level) where the id sits in the mix: the middle of the card's range (plan §4.3.3).
    load_slot() measures one-shots by LUFS-M max whatever the card's metric (see there)."""
    if sid in BED_REL_DB:
        return "lufs-i", FOREST_LUFS_I + BED_REL_DB[sid]
    t = ((card(sid).get("loudness") or {}).get("mix_target")) or {}
    rng = t.get("range") or [-19, -17]
    return t.get("metric") or "lufs-m-max", float(sum(rng)) / 2.0


_CACHE: dict[tuple[str, str], np.ndarray] = {}


def load_slot(sid: str, path: Path) -> np.ndarray:
    """The file at 48 kHz, at its mix level (mono stays mono so the panner works like the game's)."""
    key = (sid, str(path))
    if key in _CACHE:
        return _CACHE[key]
    x, sr = sf.read(str(path), always_2d=True, dtype="float64")
    if sr != SR:
        import soxr
        x = soxr.resample(x, sr, SR, quality="VHQ")
    if x.shape[1] == 2 and np.allclose(x[:, 0], x[:, 1]):
        x = x[:, :1]
    metric, level = mix_target(sid)
    # One-shots are placed by LUFS-M max (400 ms) even where the card names LUFS-S (3 s): the 3 s window
    # punishes short sounds (a 0.9 s pine bomb had to peak at 0 dBFS to reach -13.5 LUFS-S and drove the
    # master limiter 8 dB, while a 1.2 s take with a long sub needed 2.5 dB). Beds keep LUFS-I.
    metric = "lufs-i" if metric == "lufs-i" else "lufs-m-max"
    now = measure.loudness(x, SR, metric)
    y = x * mixer.db_to_gain(level - now)
    y = y[:, 0] if y.shape[1] == 1 else y
    _CACHE[key] = y
    return y


class Builder:
    def __init__(self, slots: dict[str, Path], scenario: str, delay_s: float):
        self.slots, self.events, self.voices, self.marks = slots, [], [], []
        self.rng = random.Random(f"{scenario}:pattern")
        self.delay = delay_s
        self.word = 0

    def shot(self, sid: str, t: float, pan: float = 0.0, gain_db: float = 0.0, cents: float | None = None,
             db: float = 0.0):
        if sid not in self.slots:
            return
        c = CARD_CENTS.get(sid, 0) if cents is None else cents
        cc = (self.rng.random() * 2 - 1) * c
        dd = (self.rng.random() * 2 - 1) * db
        y = mixer.varispeed(load_slot(sid, self.slots[sid]), cc) * mixer.db_to_gain(gain_db + dd)
        self.events.append(mixer.Event(t=t, audio=y, bus=BUS[sid], pan=pan, label=sid, slot=sid))
        self.marks.append({"t": round(t, 3), "id": sid, "cents": round(cc, 1), "db": round(gain_db + dd, 2), "pan": pan})

    def bed(self, sid: str, t0: float, t1: float, level: float = 1.0, pan: float = 0.0, ramp_s: float = 0.4):
        if sid not in self.slots:
            return
        y = load_slot(sid, self.slots[sid])
        start = int(self.rng.random() * y.shape[0])          # engine.ts: start somewhere in the loop
        y = np.concatenate([y[start:], y[:start]], axis=0)
        # engine.ts bed(): the gain starts at 0 and ramps to the level (setTargetAtTime, tau = ramp / 3)
        self.events.append(mixer.Event(t=t0, audio=y, bus=BUS[sid], pan=pan, label=sid, slot=sid, loop_end=t1,
                                       level_curve=[(t0, level, ramp_s / 3.0)]))
        self.marks.append({"t": round(t0, 3), "id": sid, "until": t1, "level": level, "pan": pan})

    def word_done(self, t: float, impact: str | None):
        """Word complete: fire.cast and the spoken word now, the fireball lands 0.6 s later."""
        w = voices.WORDS[self.word % len(voices.WORDS)]
        v = voices.VOICES[self.word % len(voices.VOICES)]
        self.word += 1
        self.shot("fire.cast", t, pan=0.0, db=1.0)
        self.voices.append(mixer.Voice(t_request=t, t_start=t + self.delay, audio=voices.load(v, w), word=w, voice=v))
        if impact:
            sid = f"fire.impact.{impact}"
            self.shot(sid, t + 0.6, pan=self.rng.choice([-0.3, -0.15, 0.15, 0.3]), gain_db=IMPACT_GAIN_DB[impact], db=1.0)


def build(scenario: str, slots: dict[str, Path], delay_s: float = 0.15) -> tuple[Builder, float]:
    b = Builder(slots, scenario, delay_s)
    if scenario == "dh-cast-chain":
        dur = 9.6
        b.bed("amb.forest", 0.0, dur)
        for i, k in enumerate("abcabc"):
            b.word_done(0.5 + 1.5 * i, k)
    elif scenario == "dh-pack":
        dur = 8.0
        b.bed("amb.forest", 0.0, dur)
        b.bed("enemy.quadruped.march", 0.6, dur, level=0.7, pan=0.25)
        b.shot("enemy.quadruped.howl", 1.0, pan=-0.35, db=1.5)
        b.word_done(2.6, "a")
        b.word_done(4.1, "b")
        b.shot("enemy.quadruped.howl", 4.6, pan=0.3, db=1.5)
        b.word_done(5.6, "a")
    elif scenario == "dh-trap":
        dur = 7.0
        b.bed("amb.forest", 0.0, dur)
        b.bed("enemy.swarm.march", 0.0, dur, level=0.8, pan=-0.2)
        for i, k in enumerate("abab"):
            b.word_done(0.6 + 1.5 * i, k)
        b.shot("trap.pine-bomb.trigger", 2.2, pan=0.2)
        b.shot("trap.pine-bomb.trigger", 5.2, pan=-0.15)
    elif scenario == "dh-beds":
        dur = 18.0
        b.bed("amb.forest", 0.0, dur)
        b.bed("amb.river", 0.0, dur, pan=0.0)
        b.shot("wave.horn", 3.0)
        b.bed("enemy.swarm.march", 4.0, dur, level=1.0, pan=-0.3, ramp_s=2.0)
        b.bed("enemy.quadruped.march", 6.5, dur, level=0.8, pan=0.3, ramp_s=2.0)
        b.shot("general.g01.horn", 9.5, pan=0.1)
        for i, k in enumerate("abca"):
            b.word_done(12.0 + 1.5 * i, k)
    else:
        raise ValueError(f"không có kịch bản {scenario!r}; có {', '.join(SCENARIOS)}")
    return b, dur


def render(scenario: str, slots: dict[str, Path], out_wav: Path, focus: str | None = None,
           delay_s: float = 0.15, duck_from: str = "request", sweep: bool = True, png: bool = True) -> dict:
    """Render one scene, write <out>.wav (24-bit stereo, SCENE_GAIN_DB applied), <out>.json and <out>.png."""
    b, dur = build(scenario, slots, delay_s)
    res = mixer.render(b.events, b.voices, dur, mixer.DRAGON_HOLD, duck_from=duck_from)
    starts = [v.t_start for v in b.voices]
    out = {"schema": "audiolab.context.render/1", "scenario": scenario, "game": GAME, "focus": focus,
           "slots": {k: str(v) for k, v in slots.items()}, "duration_s": dur, "voice_delay_s": delay_s,
           "duck_from": duck_from, "scene_gain_db": SCENE_GAIN_DB, "timeline": b.marks,
           "words": [{"t_request": v.t_request, "t_start": v.t_start, "word": v.word, "voice": v.voice} for v in b.voices],
           "mix_targets": {k: mix_target(k) for k in slots},
           "profile": mixer.DRAGON_HOLD["source"],
           "approximations": "Bộ nén là bộ dò đỉnh có làm mượt bắt/nhả cộng bù mức tự động của Chromium, không có "
                             "nhìn trước 6 ms; vang rừng dùng đúng bộ sinh của mixer.ts; giọng đọc là giọng macOS "
                             "`say`, cộng sau master như speechSynthesis."}
    m: dict = {"mix": metrics.mix_numbers(res["mix"]), "limiter": metrics.limiter_stats(res["gr_db"])}
    if starts:
        m["voice"] = metrics.voice_clarity(res["game"], res["voice"], starts)
    world = res["stems"].get("world")
    if world is not None:
        m["small_speaker_loss_world_db"] = metrics.small_speaker_loss(world)
    if focus and focus in slots:
        fstem = _focus_stem(b, focus, dur)
        bus = BUS[focus]
        m["focus_small_speaker_loss_db"] = metrics.small_speaker_loss(fstem)
        m["focus_share_1k4k_db"] = metrics.slot_share(res["stems"], fstem * res["duck"][bus][:, None], 1000, 4000)
        if focus in CARD_CENTS:
            x, _ = sf.read(str(slots[focus]), always_2d=True, dtype="float64")
            m["focus_band_decay"] = metrics.band_decay(x)
    if sweep and starts:
        sw = []
        for cfg in ("voice", "request"):
            for d in (0.0, 0.15, 0.4):
                bb, _ = build(scenario, slots, d)
                r2 = mixer.render(bb.events, bb.voices, dur, mixer.DRAGON_HOLD, duck_from=cfg)
                vc = metrics.voice_clarity(r2["game"], r2["voice"], [v.t_start for v in bb.voices])
                sw.append({"duck_from": cfg, "delay_s": d, "min_db": vc["min_db"], "median_db": vc["median_db"]})
        m["voice_sweep"] = sw
        worst = min(sw, key=lambda r: r["min_db"])
        m["voice_worst"] = {**worst, "min_db_voice_minus6": round(worst["min_db"] - 6.0, 1)}
    out["metrics"] = m
    out_wav.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(out_wav), (res["mix"] * mixer.db_to_gain(SCENE_GAIN_DB)).astype(np.float32), SR, subtype="PCM_24")
    out["file"] = str(out_wav)
    out["sha256"] = measure_sha(out_wav)
    if png:
        from . import card as C
        out["card"] = str(C.draw(out_wav.with_suffix(".png"), res, b, out))
    out_wav.with_suffix(".json").write_text(json.dumps(out, ensure_ascii=False, indent=1, default=float), "utf-8")
    return out


def _focus_stem(b: Builder, focus: str, dur: float) -> np.ndarray:
    n = int(round(dur * SR))
    st = np.zeros((n, 2))
    for ev in b.events:
        if ev.slot != focus:
            continue
        y = mixer.stereo(ev.audio) if ev.audio.ndim == 2 else mixer.pan(ev.audio, ev.pan)
        a = int(round(ev.t * SR))
        if ev.loop_end is not None:
            e = min(n, int(round(ev.loop_end * SR)))
            reps = int(np.ceil((e - a) / y.shape[0])) + 1
            y = np.tile(y, (reps, 1))[: e - a]
        y = y[: n - a]
        st[a:a + y.shape[0]] += y
    return st


def measure_sha(p: Path) -> str:
    from build import ledger
    return ledger.sha256_file(p)
