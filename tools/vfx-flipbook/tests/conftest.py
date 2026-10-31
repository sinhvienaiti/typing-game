"""Synthetic clips for the tests: numpy frames -> h264 MP4 in a throw-away VFXLab tree."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest

GAME = "synthetic"


def encode(frames: np.ndarray, path: Path, fps: int = 24) -> None:
    """frames (T, H, W, 3) float in [0, 1] -> MP4 (libx264, yuv420p, like Firefly's output)."""
    t, h, w, _ = frames.shape
    data = np.clip(np.round(frames * 255), 0, 255).astype(np.uint8).tobytes()
    path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-nostdin", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
                    "-s", f"{w}x{h}", "-framerate", str(fps), "-i", "-", "-c:v", "libx264", "-crf", "10",
                    "-preset", "veryfast", "-pix_fmt", "yuv420p", str(path)], input=data, check=True)


def blob(h: int, w: int, cx: float, cy: float, r: float, soft: float = 0.25) -> np.ndarray:
    """Soft disc, 1 inside, smooth falloff over soft x r."""
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    d = np.hypot(xx - cx, yy - cy) / max(r, 1e-3)
    return np.clip((1.0 + soft - d) / soft, 0.0, 1.0)


def fire(intensity: np.ndarray) -> np.ndarray:
    """Intensity map -> fire colours (white core, orange body, red edge)."""
    i = intensity[..., None]
    return np.clip(np.concatenate([i * 1.6, i ** 1.5 * 1.15, i ** 3 * 0.95], -1), 0, 1)


@pytest.fixture
def lab(tmp_path: Path):
    """A throw-away VFXLab home and table dir, with clip and table writers and the drawing helpers."""
    home = tmp_path / "VFXLab"
    table_dir = tmp_path / "tables"
    table_dir.mkdir()

    def add_clip(cid: str, frames: np.ndarray, version: str = "v1") -> Path:
        mp4 = home / "inbox" / "firefly" / GAME / cid / f"{cid}__{version}.mp4"
        encode(frames, mp4)
        mp4.with_suffix(".txt").write_text("Source: synthetic test clip\nPrompt: none\n", encoding="utf-8")
        return mp4

    def add_pair(cid: str, colour: np.ndarray, matte: np.ndarray, version: str = "v1") -> Path:
        """A Firefly transparent clip: <id>__vN.rgb.mp4 (colour over its own backdrop) + .alpha.mp4 (grey matte)."""
        d = home / "inbox" / "firefly" / GAME / cid
        encode(colour, d / f"{cid}__{version}.rgb.mp4")
        encode(np.repeat(matte[..., None], 3, -1), d / f"{cid}__{version}.alpha.mp4")
        (d / f"{cid}__{version}.txt").write_text("model: synthetic\nprompt: none\n", encoding="utf-8")
        return d / f"{cid}__{version}.rgb.mp4"

    def write_table(clips: dict, defaults: dict | None = None) -> None:
        (table_dir / f"{GAME}.json").write_text(json.dumps({"game": GAME, "defaults": defaults or {},
                                                            "clips": clips}), encoding="utf-8")

    return SimpleNamespace(home=home, table_dir=table_dir, add_clip=add_clip, add_pair=add_pair, write_table=write_table,
                           blob=blob, fire=fire, game=GAME)
