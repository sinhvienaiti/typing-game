"""Minimal SFZ reader: enough to take key centres, key/velocity ranges and offsets from the
VCSL / VSCO-2-CE mapping files. Not a full SFZ player (no opcodes are executed).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from sampler.naming import note_to_midi

HEADER_RE = re.compile(r"<(\w+)>")
OPCODE_RE = re.compile(r"([A-Za-z_][A-Za-z0-9_]*)=")
KEY_OPCODES = {"pitch_keycenter", "lokey", "hikey", "key", "sw_last", "sw_lokey", "sw_hikey"}
INT_OPCODES = {"lovel", "hivel", "offset", "seq_length", "seq_position", "transpose", "tune", "end"}
FLOAT_OPCODES = {"volume", "ampeg_release", "ampeg_attack", "ampeg_decay", "ampeg_sustain", "amp_veltrack",
                 "pan"}
LEVELS = ("control", "global", "master", "group", "region")


@dataclass
class Region:
    sample: Path                       # resolved file path (may not exist)
    sample_raw: str
    opcodes: dict = field(default_factory=dict)

    def get(self, k, default=None):
        return self.opcodes.get(k, default)

    @property
    def keycenter(self) -> int | None:
        k = self.opcodes.get("pitch_keycenter", self.opcodes.get("key"))
        return k if isinstance(k, int) else None


def _value(name: str, raw: str):
    raw = raw.strip()
    if name in KEY_OPCODES:
        try:
            return note_to_midi(raw) if not raw.lstrip("-").isdigit() else int(raw)
        except ValueError:
            return raw
    if name in INT_OPCODES:
        try:
            return int(float(raw))
        except ValueError:
            return raw
    if name in FLOAT_OPCODES:
        try:
            return float(raw)
        except ValueError:
            return raw
    return raw


def _parse_line(line: str) -> list[tuple[str, str]]:
    """Opcodes on one line; `sample=` values may contain spaces (run to the next opcode)."""
    out = []
    matches = list(OPCODE_RE.finditer(line))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(line)
        out.append((m.group(1), line[m.end():end]))
    return out


def parse_sfz(path: str | Path, text: str | None = None) -> list[Region]:
    path = Path(path)
    if text is None:
        text = path.read_text(errors="replace")
    scopes: dict[str, dict] = {lvl: {} for lvl in LEVELS}
    current = None
    regions: list[Region] = []

    def close_region():
        if current == "region" and scopes["region"]:
            ops = {}
            for lvl in ("global", "master", "group", "region"):
                ops.update(scopes[lvl])
            if "sample" in ops:
                raw = ops["sample"].strip()
                base = scopes["control"].get("default_path", "").strip()
                rel = (base + raw).replace("\\", "/")
                regions.append(Region(sample=(path.parent / rel), sample_raw=raw, opcodes=ops))

    for raw_line in text.splitlines():
        line = raw_line.split("//", 1)[0]
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        pos = 0
        for hm in list(HEADER_RE.finditer(line)) + [None]:
            chunk = line[pos:hm.start()] if hm else line[pos:]
            for k, v in _parse_line(chunk):
                if current is not None:
                    scopes[current][k] = _value(k, v) if k != "sample" else v.strip()
            if hm is None:
                break
            close_region()
            name = hm.group(1).lower()
            if name in LEVELS:
                current = name
                for lvl in LEVELS[LEVELS.index(name):]:   # a header resets its level and those below
                    scopes[lvl] = {}
            else:
                current = None
            pos = hm.end()
    close_region()
    return regions
