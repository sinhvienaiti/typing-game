"""Licence policy (AUDIO_PIPELINE.md §3.5, §10.2, §10.7) and variation limits (§5.3).

One table to edit when the owner approves a new licence. Licence ids are SPDX where
one exists, otherwise LicenseRef-*.
"""
from __future__ import annotations

import re

# Allowed licences. "cond" names the extra check licence_check applies.
ALLOWED: dict[str, dict] = {
    "CC0-1.0": {"url": "https://creativecommons.org/publicdomain/zero/1.0/", "attribution": False},
    "MIT": {"url": "https://opensource.org/license/mit", "attribution": False},
    "Apache-2.0": {"url": "https://www.apache.org/licenses/LICENSE-2.0", "attribution": False},
    # Permissive weights/tools used only on this machine (AST critic).
    "BSD-3-Clause": {"url": "https://opensource.org/license/bsd-3-clause", "attribution": False},
    "CC-BY-4.0": {"url": "https://creativecommons.org/licenses/by/4.0/", "attribution": True, "cond": "credits"},
    "CC-BY-3.0": {"url": "https://creativecommons.org/licenses/by/3.0/", "attribution": True, "cond": "credits"},
    # Project synth code (build/synth.py) and the owner's own recordings.
    "LicenseRef-AudioLab-code": {"url": "tools/audio-lab", "attribution": False},
    "LicenseRef-owner-recording": {"url": "licences/owner-recordings.txt", "attribution": False},
    # Conditional (§10.2).
    "LicenseRef-other-recording": {"url": "licences/release-<name>-<date>.txt", "attribution": False,
                                   "cond": "release"},
    "LicenseRef-Stability-Community-2024": {"url": "https://stability.ai/community-license-agreement",
                                            "attribution": False, "cond": "stability"},
    "LicenseRef-ElevenLabs-paid": {"url": "https://elevenlabs.io/terms-of-use", "attribution": False,
                                   "cond": "subscription"},
    "LicenseRef-Sonniss-GDC-2.0": {"url": "https://sonniss.com/gdc-bundle-license/", "attribution": False,
                                   "cond": "no-ai"},
}

# Aliases seen in older rows or in the plan's examples.
ALIASES = {
    "CC0": "CC0-1.0",
    "Stability-Community-2024": "LicenseRef-Stability-Community-2024",
    "BSD-3": "BSD-3-Clause",
}

# Always refused (§3.5, §10.2): non-commercial, Sampling+, no-derivatives, research-only,
# free-tier generators, BBC, Pixabay.
DENIED_PATTERNS = [
    re.compile(p, re.I) for p in (
        r"(^|[-_ ])NC([-_ ]|$)", r"non[-_ ]?commercial", r"sampling[-_ ]?(\+|plus)", r"(^|[-_ ])ND([-_ ]|$)",
        r"research", r"elevenlabs[-_ ]?free", r"\bsuno\b", r"\budio\b", r"\bbbc\b", r"pixabay",
    )
]

# Models whose weights are non-commercial (§3.5): refused even if a row claims otherwise.
DENIED_MODELS = [
    re.compile(p, re.I) for p in (
        r"audiogen", r"musicgen", r"magnet", r"mmaudio", r"woosh", r"tangoflux", r"audiox",
        r"audioldm", r"thinksound", r"prismaudio", r"qwen2\.5-omni-3b", r"audio[-_ ]?flamingo",
        r"essentia",
    )
]

# Libraries whose audio must never enter an AI step (§10.2, §10.3); ~/AudioLab/libraries/_no-ai/ (§11).
NO_AI_LIBRARIES = ("sonniss",)
NO_AI_PREFIX = "_no-ai/"


def is_sonniss(row: dict) -> bool:
    return any(lib in str(row.get(k, "")).lower() for lib in NO_AI_LIBRARIES
               for k in ("library", "pack", "licence", "path"))


def source_problem(row: dict) -> str | None:
    """Why a source/library row may not be used at all (None = usable)."""
    state = classify(row.get("licence"))
    if state != "allowed":
        return f"giấy phép {row.get('licence')!r} ({state})"
    if row.get("commercial_ok") is False:
        return "commercial_ok=false"
    return None

# Layer tools that are generative models (an AI step by definition).
AI_TOOLS = re.compile(r"stable-audio|ace-step|moss|elevenlabs|magenta|lora|audio-to-audio", re.I)

SYNTH_TOOL = "audiolab-synth"
SYNTH_LICENCE = "LicenseRef-AudioLab-code"


def canonical(licence: str | None) -> str | None:
    if licence is None:
        return None
    return ALIASES.get(licence, licence)


def is_denied(licence: str) -> bool:
    return any(p.search(licence) for p in DENIED_PATTERNS)


def classify(licence: str | None) -> str:
    """'allowed' | 'denied' | 'unknown' | 'missing'."""
    lic = canonical(licence)
    if not lic:
        return "missing"
    if is_denied(lic):
        return "denied"
    return "allowed" if lic in ALLOWED else "unknown"


def licence_url(licence: str) -> str | None:
    entry = ALLOWED.get(canonical(licence) or "")
    return entry["url"] if entry else None


def model_denied(name: str) -> bool:
    return any(p.search(name or "") for p in DENIED_MODELS)


# §5.3: per-group limits for baked variants (cents, dB). None = §5.3 sets no limit.
# Names follow the spec cards (specs/taxonomy.py RANDOMISATION); "—" in §5.3 means 0.
VARIATION_LIMITS: dict[str, tuple[float, float] | None] = {
    "key-ok": (50, 1),
    "key-bad": (30, 0),
    "word-reward": (30, 1),
    "rare-fixed": (0, 0),     # rare reward, UI, alarm, stinger: never random
    "shot": (100, 2),
    "hit-small": (150, 2),
    "hit-heavy": (80, 1),
    "blast": (150, 0),
    "death-swarm": (300, 3),
    "none": (0, 0),           # loops, music
    "default": None,          # no §5.3 group yet (death-big, creature, ambience...)
}
GROUP_ALIASES = {
    "fixed": "rare-fixed", "ui": "rare-fixed", "alarm": "rare-fixed", "stinger": "rare-fixed",
    "swarm-death": "death-swarm", "loop": "none", "music": "none",
    "death-big": "default", "creature": "default", "ambience": "default",
}


def group_name(group: str | None) -> str | None:
    return GROUP_ALIASES.get(group, group) if group else group
