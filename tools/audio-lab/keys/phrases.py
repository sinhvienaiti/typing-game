"""Typing phrases for the owner's ears: a keyboard profile as the typing-feedback kit will play it.

The kit (shared/game-kit/feedback/typing-fx/audio.ts) plays a letter from the key set at 0.55 and the
spacebar from the space set at 0.6, takes the next variant of a shuffled round (never the same twice in a
row), and nudges each play by +-3 % playback rate and +-8 % level. The render does the same, with human
timing: inter-key intervals log-normal around 60000 / (5 * WPM) ms (CV ~0.3), a little longer around a
space. One fixed seed per phrase, so every profile and every set types the very same rhythm: only the
sound differs. No level matching here: the renders keep the files' own level, so a profile that is louder
than the others shows it.
"""
from __future__ import annotations

import numpy as np

from build import dsp

SR = 48000
PHRASE = "the quick brown fox jumps over the lazy dog"
KIT_GAIN = {"key": 0.55, "space": 0.6}     # TYPING_SOUND_MAP (key, space)
KIT_PITCH = 0.03                           # TypingSoundProfile.pitch default
KIT_LEVEL = 0.08                           # TypingSoundProfile.level default


class Picker:
    """VariantPicker of the kit: shuffled rounds, a new round never starts with the one just played."""

    def __init__(self, n: int, rng: np.random.Generator):
        self.n, self.rng, self.order, self.cursor, self.last = n, rng, list(range(n)), n, -1

    def next(self) -> int:
        if self.n == 1:
            return 0
        if self.cursor >= self.n:
            self.rng.shuffle(self.order)
            if self.order[0] == self.last:
                j = 1 + int(self.rng.integers(self.n - 1))
                self.order[0], self.order[j] = self.order[j], self.order[0]
            self.cursor = 0
        v = self.order[self.cursor]
        self.cursor += 1
        self.last = v
        return v


def schedule(text: str, wpm: float, seed: int, lead_s: float = 0.25) -> list[tuple[float, str]]:
    rng = np.random.default_rng(seed)
    mean = 60.0 / (5.0 * wpm)
    sigma = 0.3
    t, out = lead_s, []
    for i, ch in enumerate(text):
        out.append((t, "space" if ch == " " else "key"))
        k = mean * float(rng.lognormal(-sigma ** 2 / 2, sigma))
        if ch == " " or (i + 1 < len(text) and text[i + 1] == " "):
            k *= 1.15
        t += max(0.045, k)
    return out


def render(sets: dict[str, list[np.ndarray]], wpm: float, seed: int, text: str = PHRASE,
           tail_s: float = 0.4) -> tuple[np.ndarray, dict]:
    """Mono float mix of `text` typed at `wpm` with the profile's key and space sets."""
    ev = schedule(text, wpm, seed)
    rng = np.random.default_rng(seed + 1)
    pickers = {k: Picker(len(v), rng) for k, v in sets.items() if v}
    n = int((ev[-1][0] + tail_s) * SR) + SR // 2
    mix = np.zeros(n)
    played = []
    for t, part in ev:
        part = part if part in pickers else "key"
        idx = pickers[part].next()
        rate = 1.0 + float(rng.uniform(-KIT_PITCH, KIT_PITCH))
        gain = KIT_GAIN[part] * (1.0 + float(rng.uniform(-KIT_LEVEL, KIT_LEVEL)))
        y = sets[part][idx]
        y = dsp.resample(y, SR, SR / rate)[:, 0] if abs(rate - 1) > 1e-6 else y
        a = int(t * SR)
        b = min(n, a + len(y))
        mix[a:b] += gain * y[: b - a]
        played.append({"t": round(t, 4), "part": part, "variant": idx + 1, "rate": round(rate, 4), "gain": round(gain, 4)})
    end = int((ev[-1][0] + tail_s) * SR)
    return mix[:end], {"wpm": wpm, "seed": seed, "text": text, "events": played,
                       "kit": {"gain": KIT_GAIN, "pitch": KIT_PITCH, "level": KIT_LEVEL}}
