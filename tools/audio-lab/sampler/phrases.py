"""Short test phrase per instrument: shows range, velocity layers, round robin and tails."""
from __future__ import annotations

from sampler.engine import Note
from sampler.instrument import Instrument

STEP = 0.25        # seconds between hits (eighths at 120 BPM)
PENTA = (0, 2, 4, 7, 9, 12)


def test_phrase(inst: Instrument, max_shift: float = 3.0, name: str | None = None) -> tuple[list[Note], float]:
    """Return (notes, suggested length in seconds before tails)."""
    name = name or inst.id
    notes: list[Note] = []
    t = 0.0
    if inst.pitched:
        play = set(inst.playable(max_shift))
        roots = inst.roots()
        center = roots[len(roots) // 2]
        line = [center + d for d in PENTA if center + d in play] or [center]
        hold = 0.45 if inst.mode == "sustain" else 0.2
        for m in line:                                   # 1) climb: range and pitch mapping
            notes.append(Note(t, m, 90, hold, name))
            t += STEP
        t += STEP
        for v in (30, 60, 90, 120):                       # 2) velocity layers on one note
            notes.append(Note(t, center, v, hold, name))
            t += STEP * 2
        for _ in range(4):                                # 3) round robin: same note, same velocity
            notes.append(Note(t, center, 100, hold, name))
            t += STEP
        t += STEP
        chord = [m for m in (center, center + 4, center + 7) if m in play]
        for m in chord:                                   # 4) held chord: release / natural tail
            notes.append(Note(t, m, 96, 1.2, name))
        t += 1.2
    else:
        for key in inst.keys()[:8]:
            for v in (40, 80, 120):                       # layers per key
                notes.append(Note(t, None, v, 0.2, name, key=key))
                t += STEP
            for _ in range(3):                            # round robin
                notes.append(Note(t, None, 100, 0.2, name, key=key))
                t += STEP
            t += STEP
    return notes, t
