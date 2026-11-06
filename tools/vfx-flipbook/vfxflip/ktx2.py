"""Local Basis Universal WASM encoder; no global executables or network required."""
from __future__ import annotations

import json
import os
import subprocess
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image

from . import pipeline


class Ktx2Error(RuntimeError):
    pass


def encode(png: Path, output: Path, codec: str, transfer: str = "srgb", *,
           uastc_level: int = 2, etc1s_quality: int = 150) -> dict:
    raw_path = temporary = None
    try:
        with Image.open(png) as image:
            rgba = np.asarray(image.convert("RGBA"))
        h, w = rgba.shape[:2]
        with tempfile.NamedTemporaryFile(dir=output.parent, prefix=f".{output.name}.", suffix=".rgba",
                                         delete=False) as handle:
            raw_path = Path(handle.name)
            handle.write(rgba.tobytes())
        with tempfile.NamedTemporaryFile(dir=output.parent, prefix=f".{output.name}.", suffix=".tmp",
                                         delete=False) as handle:
            temporary = Path(handle.name)
        result = subprocess.run([
            "node", str(pipeline.TOOL_DIR / "ktx2" / "encode.mjs"), "--raw", str(raw_path),
            "--width", str(w), "--height", str(h), "--out", str(temporary), "--codec", codec,
            "--transfer", transfer, "--uastc-level", str(uastc_level), "--etc1s-quality", str(etc1s_quality)],
            capture_output=True, text=True)
        if result.returncode:
            raise Ktx2Error(f"KTX2 {codec}: {result.stderr.strip()} {result.stdout[-1000:]}")
        info = json.loads(result.stdout.strip().splitlines()[-1])
        if (info["width"], info["height"], info["bytes"]) != (w, h, temporary.stat().st_size):
            raise Ktx2Error("KTX2: kích thước đầu ra không khớp")
        os.replace(temporary, output)
        return info
    except (OSError, ValueError, KeyError, IndexError) as exc:
        raise Ktx2Error(f"không mã hoá được {output}: {exc}") from exc
    finally:
        for path in (raw_path, temporary):
            if path is not None:
                path.unlink(missing_ok=True)
