"""Test fixtures built at run time (no audio files in Git)."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import soundfile as sf

SR = 48000


def impact(seed: int = 0, ms: float = 180.0, sr: int = SR) -> np.ndarray:
    rng = np.random.default_rng(seed)
    n = int(sr * ms / 1000)
    t = np.arange(n) / sr
    x = rng.standard_normal(n) * np.exp(-t / 0.03) + 0.6 * np.sin(2 * np.pi * 180 * t) * np.exp(-t / 0.06)
    return x / np.max(np.abs(x))


def make_library(root: Path, licence: str = "CC0-1.0", files: int = 3, **flags) -> Path:
    """A fake pack under root/testlib/pack1 with a pack row in root/SOURCES.jsonl."""
    pack = root / "testlib" / "pack1"
    (pack / "Audio").mkdir(parents=True, exist_ok=True)
    for i in range(files):
        stereo = np.stack([impact(i), 0.8 * impact(i)], axis=1)
        sf.write(str(pack / "Audio" / f"hit_{i:03d}.wav"), 0.7 * stereo, 44100, subtype="PCM_16")
    (pack / "LICENSE-2026-10-23.txt").write_text(f"Test pack licence copy ({licence}), 2026-10-23\n")
    row = {"library": "testlib", "pack": "Pack One", "version": "1.0", "year": 2026, "path": "testlib/pack1",
           "file": "pack1.zip", "sha256": "0" * 64, "url": "https://example.invalid/pack1.zip",
           "page": "https://example.invalid/pack1", "author": "Test", "licence": licence,
           "licence_copy": "testlib/pack1/LICENSE-2026-10-23.txt", "downloaded": "2026-10-23",
           "commercial_ok": True, "attribution_required": False, "ai_input_allowed": True,
           "raw_redistribution_allowed": True, "files": files}
    row.update(flags)
    with open(root / "SOURCES.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")
    return root


def recipe(game: str = "typing-survival", sid: str = "hit.test", count: int = 4, seed: int = 811,
           library: bool = True) -> dict:
    layers = [
        {"id": "body", "role": "body",
         "source": {"synth": "noise_burst", "params": {"color": "pink", "durMs": 150, "hpHz": 200, "lpHz": 900}},
         "gainDb": -6, "vary": {"gainDb": [-1, 1]}},
        {"id": "sub", "role": "sub", "source": {"synth": "sub_thump", "params": {"durMs": 140}}, "gainDb": -4},
        {"id": "ring", "role": "sweetener", "source": {"synth": "fm_ping", "params": {"carrierHz": 2100}},
         "gainDb": -18, "offsetMs": 2, "vary": {"pitchCents": [-60, 60]}},
    ]
    if library:
        layers.insert(0, {
            "id": "attack", "role": "attack", "source": {"library": "testlib/pack1/Audio/hit_000.wav"},
            "filters": [{"type": "highpass", "hz": 400}], "fadeOutMs": 20,
            "vary": {"pitchCents": [-50, 50], "swap": [{"library": "testlib/pack1/Audio/hit_001.wav"},
                                                       {"library": "testlib/pack1/Audio/hit_002.wav"}]}})
    return {
        "schema": "audiolab.recipe/1", "game": game, "id": sid, "group": "hit-heavy", "channels": 1,
        "layers": layers,
        "chain": {"saturation": {"driveDb": 3, "mix": 0.3}, "maxLengthMs": 500},
        "variants": {"count": count, "seed": seed, "pitchCents": [-80, 80], "gainDb": [-1, 1]},
        "export": {"path": "sfx/hits/hit-test"},
    }
