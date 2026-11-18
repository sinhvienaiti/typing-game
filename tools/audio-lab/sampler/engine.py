"""Render notes with multisampled instruments to 48 kHz audio (numpy + soxr).

Rules from the plan (§3.2): pitch shift by resampling, never more than 3 semitones (the cap counts
the note distance, the note's cents and the tuning correction together). Velocity picks the layer,
round robin rotates within a layer, sustained articulations fade over `release` after note-off,
one-shots ring to the end of the sample (their natural tail). Nothing is time-stretched.
"""
from __future__ import annotations

import math
import random
from dataclasses import dataclass, field, asdict
from pathlib import Path

import numpy as np
import soundfile as sf
import soxr

from sampler.instrument import Instrument, Zone
from sampler.naming import midi_to_note, note_to_midi

SR = 48000
MAX_SHIFT_CAP = 3.0           # semitones, plan §3.2
GUARD_DBFS = -1.0


class OutOfRange(ValueError):
    pass


@dataclass
class Note:
    start: float                      # seconds
    midi: int | None = None           # pitched: MIDI note; unpitched: optional key-map note
    velocity: int = 100
    duration: float = 0.5             # seconds until note-off
    instrument: str | None = None     # id registered in the Sampler; None = the only/first one
    key: str | None = None            # unpitched key name (or articulation override)
    cents: float = 0.0                # extra detune, counts against the shift cap
    gain_db: float = 0.0
    pan: float = 0.0                  # -1 left .. +1 right
    choke: bool = False               # fade at note-off even for one-shots


@dataclass
class Render:
    audio: np.ndarray                 # float32, shape (frames, 2)
    sr: int
    report: dict = field(default_factory=dict)

    def write(self, path: str | Path, subtype: str = "PCM_24") -> Path:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        sf.write(str(path), self.audio, self.sr, subtype=subtype)
        return path


def db2amp(db: float) -> float:
    return 10.0 ** (db / 20.0)


class Sampler:
    def __init__(self, sr: int = SR, max_shift: float = MAX_SHIFT_CAP, rr_mode: str = "cycle",
                 seed: int = 0, veltrack: float = 0.5, trim_db: float = -50.0, trim: bool = True):
        if not 0.0 <= max_shift <= MAX_SHIFT_CAP:
            raise ValueError(f"max_shift must be within 0..{MAX_SHIFT_CAP} semitones (plan §3.2)")
        if rr_mode not in ("cycle", "random"):
            raise ValueError("rr_mode must be cycle or random")
        self.sr, self.max_shift, self.rr_mode = sr, max_shift, rr_mode
        self.veltrack, self.trim_db, self.trim = veltrack, trim_db, trim
        self.seed = seed
        self.rng = random.Random(seed)
        self.instruments: dict[str, Instrument] = {}
        self._rr: dict[tuple, int] = {}
        self._raw: dict[Path, tuple[np.ndarray, int, int]] = {}
        self._shifted: dict[tuple, np.ndarray] = {}

    # ----- setup -----

    def add(self, inst: Instrument, name: str | None = None) -> str:
        name = name or inst.id
        self.instruments[name] = inst
        return name

    def _inst(self, name: str | None) -> tuple[str, Instrument]:
        if name is None:
            if not self.instruments:
                raise KeyError("no instrument loaded")
            name = next(iter(self.instruments))
        if name not in self.instruments:
            raise KeyError(f"instrument '{name}' not loaded")
        return name, self.instruments[name]

    # ----- zone choice -----

    def pick(self, note: Note) -> tuple[str, Instrument, Zone, float]:
        """Return (instrument name, instrument, zone, total shift in semitones)."""
        name, inst = self._inst(note.instrument)
        vel = max(1, min(127, int(note.velocity)))
        cap = self.max_shift + 1e-6
        if inst.pitched:
            if note.midi is None:
                raise ValueError(f"{name}: pitched note needs midi")
            key = note.key if note.key in inst.keys() else inst.default_key
            cands = [z for z in inst.zones if z.key == key]
            roots = sorted({z.root for z in cands})

            def eff(root):   # effective shift with this root's tuning (layer-average)
                tunes = [z.tune_cents for z in cands if z.root == root]
                return (note.midi - root) + (note.cents + sum(tunes) / len(tunes)) / 100.0

            # nearest root first; on a tie prefer shifting up from the lower sample
            order = sorted(roots, key=lambda r: (abs(eff(r)), -r if eff(r) >= 0 else 1000 - r))
            layer = None
            for root in order:
                cand = self._layer([z for z in cands if z.root == root], vel)
                if all(abs(note.midi - z.root + (note.cents + z.tune_cents) / 100.0) <= cap for z in cand):
                    layer = cand
                    break
            if layer is None:
                raise OutOfRange(f"{name}: {midi_to_note(note.midi)} needs {eff(order[0]):+.2f} st "
                                 f"from {midi_to_note(order[0])} (cap {self.max_shift})")
        else:
            key = note.key or (inst.key_for_midi(note.midi) if note.midi is not None else None) or inst.default_key
            group = [z for z in inst.zones if z.key == key]
            if not group:
                raise OutOfRange(f"{name}: no key '{key}' (keys: {', '.join(inst.keys())})")
            if abs(note.cents) / 100.0 > cap:
                raise OutOfRange(f"{name}: detune {note.cents} cents exceeds the cap")
            layer = self._layer(group, vel)
        zone = self._round_robin(name, layer)
        shift = ((note.midi - zone.root) if inst.pitched else 0.0) + (note.cents + zone.tune_cents) / 100.0
        if abs(shift) > cap:
            raise OutOfRange(f"{name}: shift {shift:+.2f} st exceeds the cap {self.max_shift}")
        return name, inst, zone, shift

    @staticmethod
    def _layer(group: list[Zone], vel: int) -> list[Zone]:
        """Zones of the velocity layer that holds `vel` (nearest range if the map has a gap)."""
        layer = [z for z in group if z.lovel <= vel <= z.hivel]
        if not layer:
            best = min(group, key=lambda z: min(abs(vel - z.lovel), abs(vel - z.hivel)))
            layer = [z for z in group if (z.lovel, z.hivel) == (best.lovel, best.hivel)]
        return sorted(layer, key=lambda z: (z.rr, str(z.path)))

    def _round_robin(self, name: str, layer: list[Zone]) -> Zone:
        if len(layer) == 1:
            return layer[0]
        z0 = layer[0]
        k = (name, z0.key, z0.root, z0.lovel, z0.hivel)
        last = self._rr.get(k, -1)
        if self.rr_mode == "cycle":
            i = (last + 1) % len(layer)
        else:
            choices = [i for i in range(len(layer)) if i != last]
            i = self.rng.choice(choices)
        self._rr[k] = i
        return layer[i]

    # ----- audio -----

    def _load(self, path: Path) -> tuple[np.ndarray, int, int]:
        """(stereo float32 audio, file sample rate, trimmed frames), cached."""
        if path in self._raw:
            return self._raw[path]
        x, sr = sf.read(str(path), dtype="float32", always_2d=True)
        if x.shape[1] == 1:
            x = np.repeat(x, 2, axis=1)
        elif x.shape[1] > 2:
            x = x[:, :2]
        trimmed = 0
        if self.trim and len(x):
            a = np.abs(x).max(axis=1)
            peak = float(a.max())
            if peak > 0:
                first = int(np.argmax(a > peak * db2amp(self.trim_db)))
                trimmed = max(0, first - int(0.001 * sr))
                x = x[trimmed:].copy()
                n = min(len(x), max(1, int(0.0005 * sr)))
                if trimmed:
                    x[:n] *= np.linspace(0.0, 1.0, n, dtype=np.float32)[:, None]
        n = min(len(x), int(0.005 * sr))       # 5 ms fade at the very end, against cut tails
        if n > 1:
            x[-n:] *= np.linspace(1.0, 0.0, n, dtype=np.float32)[:, None]
        self._raw[path] = (x, sr, trimmed)
        return self._raw[path]

    def _audio(self, zone: Zone, shift: float) -> np.ndarray:
        k = (zone.path, round(shift, 5))
        if k in self._shifted:
            return self._shifted[k]
        x, sr, _ = self._load(zone.path)
        ratio = 2.0 ** (shift / 12.0)
        if abs(ratio - 1.0) < 1e-9 and sr == self.sr:
            y = x
        else:   # claiming a higher input rate plays the sample faster: pitch up by `ratio`
            y = soxr.resample(x, sr * ratio, self.sr, quality="VHQ").astype(np.float32)
        self._shifted[k] = y
        return y

    def velocity_gain(self, vel: int) -> float:
        return (max(1, min(127, vel)) / 127.0) ** (2.0 * self.veltrack)

    def render(self, notes: list[Note], length: float | None = None, tail: str = "keep",
               on_out_of_range: str = "error", normalize: str = "guard") -> Render:
        """tail: keep (let the last tails ring), cut (stop at `length`), wrap (fold tails past
        `length` back to the start, for seamless loops). normalize: guard (only if peak > -1 dBFS),
        peak (to -1 dBFS), none."""
        if tail not in ("keep", "cut", "wrap"):
            raise ValueError("tail must be keep, cut or wrap")
        if tail != "keep" and not length:
            raise ValueError(f"tail={tail} needs length")
        if on_out_of_range not in ("error", "skip"):
            raise ValueError("on_out_of_range must be error or skip")
        self._rr.clear()                       # same notes in, same audio out
        self.rng = random.Random(self.seed)
        voices, rows, skipped = [], [], []
        for i, n in enumerate(sorted(notes, key=lambda n: n.start)):
            try:
                name, inst, zone, shift = self.pick(n)
            except OutOfRange as e:
                if on_out_of_range == "error":
                    raise
                skipped.append({"i": i, "start": n.start, "midi": n.midi, "key": n.key, "reason": str(e)})
                continue
            y = self._audio(zone, shift)
            start = int(round(n.start * self.sr))
            env_end = len(y)
            if inst.mode == "sustain" or n.choke:
                off = max(1, int(round(n.duration * self.sr)))
                rel = max(1, int(round(inst.release * self.sr)))
                if off < len(y):
                    env_end = min(len(y), off + rel)
            g = db2amp(n.gain_db) * self.velocity_gain(n.velocity)
            pan = max(-1.0, min(1.0, n.pan))
            gl, gr = min(1.0, 1.0 - pan), min(1.0, 1.0 + pan)
            v = y[:env_end] * np.array([g * gl, g * gr], dtype=np.float32)
            if env_end < len(y):
                off = max(1, int(round(n.duration * self.sr)))
                t = np.arange(env_end - off, dtype=np.float32)
                v[off:] *= np.exp(-6.9078 * t / max(1, env_end - off))[:, None]   # -60 dB at the end
            voices.append((start, v))
            rows.append({
                "i": i, "instrument": name, "start": round(n.start, 6), "duration": round(n.duration, 6),
                "midi": n.midi, "note": midi_to_note(n.midi) if n.midi is not None and inst.pitched else None,
                "key": zone.key, "velocity": n.velocity, "sample": zone.file or str(zone.path),
                "root": zone.root, "shift_st": round(shift, 4), "tune_cents": round(zone.tune_cents, 1),
                "layer": [zone.lovel, zone.hivel], "rr": zone.rr, "frames": len(v),
            })
        end = max((s + len(v) for s, v in voices), default=0)
        total = int(round(length * self.sr)) if length else end
        buf = np.zeros((max(end, total, 1), 2), dtype=np.float32)
        for s, v in voices:
            buf[s:s + len(v)] += v
        if length:
            if tail == "wrap":
                out = buf[:total].copy()
                for k in range(total, len(buf), total):
                    seg = buf[k:k + total]
                    out[:len(seg)] += seg
                buf = out
            elif tail == "cut":
                buf = buf[:total].copy()
                n = min(len(buf), int(0.01 * self.sr))
                if n > 1:
                    buf[-n:] *= np.linspace(1.0, 0.0, n, dtype=np.float32)[:, None]
        peak = float(np.abs(buf).max()) if len(buf) else 0.0
        gain_db = 0.0
        if peak > 0 and (normalize == "peak" or (normalize == "guard" and peak > db2amp(GUARD_DBFS))):
            gain_db = GUARD_DBFS - 20 * math.log10(peak)
            buf *= db2amp(gain_db)
        out_peak = float(np.abs(buf).max()) if len(buf) else 0.0
        report = {
            "sr": self.sr, "frames": len(buf), "duration": round(len(buf) / self.sr, 4),
            "peak_dbfs": round(20 * math.log10(out_peak), 2) if out_peak > 0 else None,
            "gain_applied_db": round(gain_db, 2), "normalize": normalize, "tail": tail,
            "loop_length": length if tail == "wrap" else None,
            "max_shift_st": self.max_shift, "rr_mode": self.rr_mode, "veltrack": self.veltrack,
            "instruments": {k: {"id": v.id, "pitched": v.pitched, "mode": v.mode, "release": v.release,
                                "source": v.source, "notes": v.notes} for k, v in self.instruments.items()},
            "notes": rows, "skipped": skipped, "sources": self._sources(rows),
        }
        return Render(audio=buf, sr=self.sr, report=report)

    def _sources(self, rows: list[dict]) -> list[dict]:
        used = {}
        for inst in self.instruments.values():
            for z in inst.zones:
                key = z.file or str(z.path)
                if any(r["sample"] == key for r in rows):
                    used[key] = {"file": key, "sha256": z.sha256, "licence": z.licence, "pack_path": z.pack_path}
        return sorted(used.values(), key=lambda d: d["file"])


def parse_note_spec(spec: str, bpm: float | None = None) -> list[Note]:
    """'start:note:dur[:vel[:key]]' items split by spaces or commas; note = C5, 60 or a key name.
    With bpm, start and dur are in beats."""
    k = 60.0 / bpm if bpm else 1.0
    out = []
    for item in spec.replace(",", " ").split():
        parts = item.split(":")
        if len(parts) < 3:
            raise ValueError(f"note '{item}': need start:note:dur[:vel[:key]]")
        start, note, dur = float(parts[0]) * k, parts[1], float(parts[2]) * k
        vel = int(parts[3]) if len(parts) > 3 and parts[3] else 100
        key = parts[4] if len(parts) > 4 else None
        try:
            midi = note_to_midi(note)
        except ValueError:
            midi, key = None, note
        out.append(Note(start=start, midi=midi, velocity=vel, duration=dur, key=key))
    return out


def notes_from_json(items: list[dict], bpm: float | None = None) -> list[Note]:
    k = 60.0 / bpm if bpm else 1.0
    out = []
    for d in items:
        midi = d.get("midi")
        if midi is None and d.get("note") is not None:
            midi = note_to_midi(str(d["note"]))
        out.append(Note(start=float(d["start"]) * k, midi=midi, velocity=int(d.get("velocity", d.get("vel", 100))),
                        duration=float(d.get("duration", d.get("dur", 0.5))) * k, instrument=d.get("instrument"),
                        key=d.get("key"), cents=float(d.get("cents", 0.0)), gain_db=float(d.get("gain_db", 0.0)),
                        pan=float(d.get("pan", 0.0)), choke=bool(d.get("choke", False))))
    return out


def note_dict(n: Note) -> dict:
    return asdict(n)
