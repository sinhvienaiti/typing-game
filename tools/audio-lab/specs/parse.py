"""Small parsers for the game sources: Markdown tables, TS snippets, durations, notes.

All readers open game files read-only; nothing here writes.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

MINUS = "−"  # Vietnamese docs write negatives with U+2212


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def vn_number(text: str) -> float | None:
    """'0,50' -> 0.5, '−4 dB' -> -4.0, '10_000' -> 10000.0; None when no number."""
    m = re.search(r"[-" + MINUS + r"]?\d[\d_]*(?:[.,]\d+)?", text)
    if not m:
        return None
    raw = m.group(0).replace(MINUS, "-").replace("_", "").replace(",", ".")
    return float(raw)


# ── Markdown ────────────────────────────────────────────────────────────────

@dataclass
class Table:
    heading: str            # nearest heading text (without #)
    heading_path: list[str]  # all enclosing headings, outermost first
    line: int               # 1-based line of the header row
    header: list[str]
    rows: list[dict[str, str]] = field(default_factory=list)
    row_lines: list[int] = field(default_factory=list)


def _cells(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def md_tables(text: str) -> list[Table]:
    """Every pipe table with its heading context."""
    lines = text.splitlines()
    tables: list[Table] = []
    path: list[tuple[int, str]] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        h = re.match(r"^(#{1,6})\s+(.*)$", line)
        if h:
            level = len(h.group(1))
            path = [p for p in path if p[0] < level] + [(level, h.group(2).strip())]
            i += 1
            continue
        if line.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{3,}", lines[i + 1]):
            header = _cells(line)
            t = Table(heading=path[-1][1] if path else "", heading_path=[p[1] for p in path], line=i + 1, header=header)
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                cells = _cells(lines[j])
                cells += [""] * (len(header) - len(cells))
                t.rows.append(dict(zip(header, cells)))
                t.row_lines.append(j + 1)
                j += 1
            tables.append(t)
            i = j
            continue
        i += 1
    return tables


def backticks(text: str) -> list[str]:
    return re.findall(r"`([^`]+)`", text)


def heading_line(text: str, needle: str) -> int | None:
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("#") and needle in line:
            return n
    return None


def line_of(text: str, needle: str) -> int | None:
    for n, line in enumerate(text.splitlines(), 1):
        if needle in line:
            return n
    return None


# ── TypeScript snippets ─────────────────────────────────────────────────────

def ts_string_array(text: str, name: str) -> list[str]:
    """Items of `export const NAME = [ "a", "b" ] as const` (or typed)."""
    m = re.search(r"\b" + re.escape(name) + r"\b[^=]*=\s*\[(.*?)\]", text, re.S)
    if not m:
        return []
    return re.findall(r'"([^"]+)"', m.group(1))


def ts_number_const(text: str, name: str) -> float | None:
    m = re.search(r"\b(?:const|readonly)?\s*" + re.escape(name) + r"\s*[:=]\s*([\d_.]+)", text)
    return float(m.group(1).replace("_", "")) if m else None


# ── Durations, tempo, pitches in prompt text ────────────────────────────────

_NUM = r"(\d+(?:[.,]\d+)?)"


def _ms(value: str, unit: str) -> float:
    v = float(value.replace(",", "."))
    return v * 1000.0 if unit == "s" else v


def parse_duration(text: str) -> dict | None:
    """Duration stated in a prompt or cell.

    Returns {"ms": float, "kind": "exact|max|total|loop|range", "min_ms"?, "max_ms"?} or None.
    Bars are handled by parse_bars (they need a tempo).
    """
    if not text:
        return None
    t = text.replace("–", "-").replace("—", "-")
    m = re.search(_NUM + r"\s*-\s*" + _NUM + r"\s*(ms|s)\b", t)
    if m:
        lo, hi = _ms(m.group(1), m.group(3)), _ms(m.group(2), m.group(3))
        return {"ms": (lo + hi) / 2, "kind": "range", "min_ms": lo, "max_ms": hi}
    m = re.search(_NUM + r"\s*(ms|s)\s+total", t)
    if m:
        return {"ms": _ms(m.group(1), m.group(2)), "kind": "total"}
    m = re.search(r"(?:seamless\s+)?loop[^.,;]*?\b" + _NUM + r"\s*(ms|s)\b", t, re.I)
    if m:
        return {"ms": _ms(m.group(1), m.group(2)), "kind": "loop"}
    m = re.search(r"(?:lặp|loop)\s+" + _NUM + r"\s*(ms|s)\b", t, re.I)
    if m:
        return {"ms": _ms(m.group(1), m.group(2)), "kind": "loop"}
    m = re.search(r"\b(?:under|below|dưới)\s+" + _NUM + r"\s*(ms|s)\b", t, re.I)
    if m:
        return {"ms": _ms(m.group(1), m.group(2)), "kind": "max"}
    # "(40 ms)" or ", 350 ms" or "1.6 s": take the last stated length (prompts end with it)
    found = re.findall(r"(?<![\w.])" + _NUM + r"\s*(ms|s)\b(?!\s*apart)", t)
    if found:
        v, u = found[-1]
        return {"ms": _ms(v, u), "kind": "exact"}
    return None


def parse_bars(text: str) -> dict | None:
    """'84 BPM, 16 bars' -> {"bpm": 84, "bars": 16}; either may be missing."""
    if not text:
        return None
    bpm = re.search(r"(\d+(?:\.\d+)?)\s*BPM", text)
    bars = re.search(r"(\d+)[- ]bars?\b", text, re.I) or re.search(r"(\d+)\s*ô nhịp", text)
    if not bpm and not bars:
        return None
    return {"bpm": float(bpm.group(1)) if bpm else None, "bars": int(bars.group(1)) if bars else None}


def bars_ms(bpm: float, bars: int, beats_per_bar: int = 4) -> float:
    return round(bars * beats_per_bar * 60_000.0 / bpm, 3)


def parse_pitches(text: str) -> list[str]:
    """Note names like C5, F#4, Bb3 (only when written with an octave)."""
    if not text:
        return []
    return re.findall(r"\b([A-G](?:#|b)?[0-8])\b", text)


def parse_variant_count(text: str) -> int | None:
    m = re.search(r"\b(?:make|render)\s+(\d+)\s+variants?\b", text or "", re.I)
    return int(m.group(1)) if m else None


def parse_caps(text: str) -> dict:
    """Rate limits written in Vietnamese cells: per second, per frame, min gap."""
    out: dict = {}
    t = text or ""
    m = re.search(r"tối đa\s+(\d+)\s+(?:lần\s+)?mỗi giây", t)
    if m:
        out["per_s"] = int(m.group(1))
    m = re.search(r"tối đa\s+(\d+)\s+(?:lần\s+)?mỗi khung", t)
    if m:
        out["per_frame"] = int(m.group(1))
    m = re.search(r"ít nhất\s+" + _NUM + r"\s*(ms|s)\b", t)
    if m:
        out["min_gap_ms"] = _ms(m.group(1), m.group(2))
    m = re.search(r"mỗi\s+(\d+)\s*ms\b", t)
    if m and "min_gap_ms" not in out:
        out["min_gap_ms"] = float(m.group(1))
    return out
