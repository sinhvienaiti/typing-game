"""Audio Lab paths and safe environment (Python side of common/env.sh).

Import before huggingface_hub / transformers / torch:

    from common import env
    env.apply()          # idempotent; run.sh already does it

All heavy data stays under AUDIOLAB_HOME (default ~/AudioLab), never in a repo.
"""
from __future__ import annotations

import os
from pathlib import Path

LAB = Path(__file__).resolve().parent.parent          # tools/audio-lab
REPO = LAB.parent.parent                              # typing-game root
GAMES = REPO / "games"                                # read-only for Audio Lab

HOME = Path(os.environ.get("AUDIOLAB_HOME", str(Path.home() / "AudioLab"))).expanduser()
MODELS = HOME / "models"
LIBRARIES = HOME / "libraries"
WORK = HOME / "work"
REVIEW = HOME / "review"
BIN = HOME / "bin"
CACHE = HOME / "cache"
VENV = HOME / ".venv"
HF_HOME = MODELS / "hf-cache"

BOARD_HOST = "127.0.0.1"
BOARD_PORT = 3191          # strict; 3192 only when 3191 is busy (say so in the log)
BOARD_PORT_FALLBACK = 3192

TOKEN_VARS = ("HF_TOKEN", "HUGGING_FACE_HUB_TOKEN", "HF_TOKEN_PATH")


def safe_env(online: bool | None = None) -> dict[str, str]:
    """Variables every Audio Lab process must run with."""
    if online is None:
        online = os.environ.get("AUDIOLAB_ONLINE") == "1"
    return {
        "AUDIOLAB_HOME": str(HOME),
        "HF_HOME": str(HF_HOME),
        "HF_HUB_DISABLE_IMPLICIT_TOKEN": "1",
        "HF_HUB_DISABLE_TELEMETRY": "1",
        "HF_HUB_DISABLE_PROGRESS_BARS": "1",
        "HF_HUB_OFFLINE": "0" if online else "1",
        "DO_NOT_TRACK": "1",
        "TOKENIZERS_PARALLELISM": "false",
        "TORCH_HOME": str(MODELS / "torch"),
        "MPLCONFIGDIR": str(CACHE / "matplotlib"),
        "MPLBACKEND": "Agg",
        "NUMBA_CACHE_DIR": str(CACHE / "numba"),
        "UV_CACHE_DIR": str(CACHE / "uv"),
        "UV_PYTHON_INSTALL_DIR": str(HOME / "python"),
        "UV_NO_CONFIG": "1",
        "UV_PYTHON_DOWNLOADS": "never",
        "UV_PYTHON_PREFERENCE": "only-managed",
    }


def apply(online: bool | None = None) -> None:
    """Set the safe environment in this process and drop any token."""
    for k in TOKEN_VARS:
        os.environ.pop(k, None)
    os.environ.update(safe_env(online))


def check() -> list[str]:
    """Return problems with the current process environment (empty = fine)."""
    problems = [f"{k} is set" for k in TOKEN_VARS if os.environ.get(k)]
    for k, v in safe_env().items():
        if k in ("HF_HUB_OFFLINE",):
            continue
        if os.environ.get(k) != v:
            problems.append(f"{k}={os.environ.get(k)!r}, expected {v!r}")
    if not HF_HOME.is_dir():
        problems.append(f"missing {HF_HOME}")
    return problems


GAME_SLUGS = ("dragon-hold", "typing-defense", "typing-survival", "space-typing")
FIXTURES = WORK / "_fixtures"            # poc40/: the 40-sound PoC set (CC0 + synthetic)
STAGING = REVIEW / "staging"             # mirrors games/<game>/art-src/audio while games/** is read-only


def _game(game: str) -> str:
    if game not in GAME_SLUGS:
        raise ValueError(f"unknown game {game!r}; expected one of {GAME_SLUGS}")
    return game


def work_dir(game: str, sound_id: str, run: str) -> Path:
    """~/AudioLab/work/<game>/<id>/<run>/ (created)."""
    p = WORK / _game(game) / sound_id / run
    p.mkdir(parents=True, exist_ok=True)
    return p


def art_src_staging(game: str) -> Path:
    """~/AudioLab/review/staging/<game>/art-src/audio (created).

    Same sub-layout as games/<game>/art-src/audio (specs/, recipes/, review/, licences/,
    SOURCES.json, licences.jsonl); copied into the game later, by the coordinator.
    """
    p = STAGING / _game(game) / "art-src" / "audio"
    p.mkdir(parents=True, exist_ok=True)
    return p


def game_dir(game: str) -> Path:
    """games/<game> in the parent repo. Read only for Audio Lab tools."""
    return GAMES / _game(game)
