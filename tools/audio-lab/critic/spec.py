"""Spec cards (L0, YAML) as the critic reads them.

The specs lane owns the card format; the critic reads these keys and ignores the rest.
Every key is optional; a nested `critic:` mapping overrides top-level keys.

    id: gun.xung                  # sound id; also used to infer the group
    game: typing-survival
    group: shot_gun               # critic group (python -m critic groups)
    family: ban                   # §4.6 family slug (default: from the group)
    duration_ms: [80, 350]        # range, or a target number (±20 %), or a mapping:
                                  # {target_ms, tolerance_pct | tolerance_ms} (specs lane `duration:`)
                                  # or {min_ms, max_ms}; aliases: durationMs, length_ms, lengthMs, duration_s
    loop: false
    stereo: false                 # allow stereo (music, ambience, end stinger)
    dirty: true                   # §4.4 intentionally dirty family
    pitched: false
    attack_max_ms: 10             # override §4.3.1 limits (owner-approved only); null = not checked
    head_max_ms: 5                # null = not checked (loops, music)
    rate_hz: 5                    # game rhythm for the 3-4 s repetition of short sounds
    bpm: 96, bars: 8, beats_per_bar: 4      # loops and music: exact length check
    intent: "a heavy industrial autocannon shot"   # informational; never a quality score
    clap: {labels: [...], expected: [...], contrast: [[good, bad], ...]}
    ast: {expected: ["Gunshot, gunfire"], forbid: [Speech]}
    refs: [path, ...]             # approved references (files or dirs), relative to the card
    references: [{path: ...}]     # specs-lane form, used when `refs` is empty
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any

import yaml

from . import groups as G


@dataclass
class Spec:
    group: str = "generic"
    group_source: str = "default"
    id: str | None = None
    game: str | None = None
    family: str = "khac"
    duration_ms: tuple[float, float] | None = None   # explicit, from the card only
    duration_target_ms: float | None = None
    duration_tol: float = 0.20                       # §4.3.1 relative tolerance around duration_ms
    loop: bool = False
    stereo_ok: bool = False
    dirty: bool = False
    pitched: bool = False
    attack_max_ms: float | None = None
    head_max_ms: float | None = 5.0                  # None = head silence not checked
    rate_hz: float = 3.0
    bpm: float | None = None
    bars: float | None = None
    beats_per_bar: float = 4.0
    intent: str | None = None
    clap_labels: list[str] | None = None
    clap_expected: list[str] = field(default_factory=list)
    clap_contrast: list[tuple[str, str]] = field(default_factory=list)
    ast_expected: list[str] = field(default_factory=list)
    ast_forbid: list[str] = field(default_factory=list)
    refs: list[str] = field(default_factory=list)
    path: str | None = None
    raw: dict = field(default_factory=dict, repr=False)

    @property
    def group_obj(self) -> G.Group:
        return G.get(self.group)

    @property
    def group_dur_ms(self) -> tuple[float, float] | None:
        return self.duration_ms or self.group_obj.dur_ms

    def to_json(self) -> dict[str, Any]:
        d = asdict(self)
        d.pop("raw", None)
        d["duration_ms"] = list(self.duration_ms) if self.duration_ms else None
        d["clap_contrast"] = [list(p) for p in self.clap_contrast]
        d["group_name_vi"] = self.group_obj.name_vi
        d["family_name_vi"] = G.FAMILIES.get(self.family, self.family)
        return d


def _num(v) -> float | None:
    try:
        return None if v is None else float(v)
    except (TypeError, ValueError):
        return None


def _or(v, default):
    n = _num(v)
    return default if n is None else n


def _duration(raw: dict) -> tuple[tuple[float, float] | None, float | None, float]:
    """(range_ms, target_ms, relative tolerance). A target with tolerance_ms becomes an exact range."""
    tol = 0.20
    v = None
    for k in ("duration_ms", "durationMs", "length_ms", "lengthMs", "duration"):
        if k in raw:
            v = raw[k]
            break
    scale = 1.0
    if v is None and "duration_s" in raw:
        v, scale = raw["duration_s"], 1000.0
    if v is None:
        return None, None, tol
    if isinstance(v, dict):
        lo = _num(v.get("min_ms", v.get("min")))
        hi = _num(v.get("max_ms", v.get("max")))
        t = _num(v.get("target_ms", v.get("target")))
        if t is not None:
            t_ms = _num(v.get("tolerance_ms"))
            t_pct = _num(v.get("tolerance_pct"))
            if t_ms is not None:          # music: exact length within ±tolerance_ms (§4.3.1)
                return (t - t_ms, t + t_ms), t, 0.0
            if t_pct is not None:
                tol = t_pct / 100.0
            return (t, t), t, tol
        if lo is not None and hi is not None:
            return (lo * scale, hi * scale), None, tol
        return None, None, tol
    if isinstance(v, (list, tuple)) and len(v) == 2:
        return (float(v[0]) * scale, float(v[1]) * scale), None, tol
    t = _num(v)
    return ((t * scale, t * scale), t * scale, tol) if t is not None else (None, None, tol)


def _refs(raw: dict, base: Path) -> list[str]:
    items = raw.get("refs") or []
    if not items:
        items = [r.get("path") if isinstance(r, dict) else r for r in (raw.get("references") or [])]
    out = []
    for r in items:
        if not r:
            continue
        p = Path(str(r)).expanduser()
        out.append(str(p if p.is_absolute() else (base / p).resolve()))
    return out


def from_mapping(raw: dict | None, path: str | None = None, group_override: str | None = None,
                 sound_id: str | None = None, game: str | None = None) -> Spec:
    orig = dict(raw or {})
    raw = dict(orig)
    raw.update(raw.pop("critic", None) or {})
    sid = raw.get("id") or sound_id
    if group_override:
        gkey, src = group_override, "cli"
    elif raw.get("group") in G.GROUPS:
        gkey, src = raw["group"], "spec"
    elif G.infer_group(sid):
        gkey, src = G.infer_group(sid), "id"
    else:
        gkey, src = "generic", "default"
    g = G.get(gkey)
    rng, target, tol = _duration(raw)
    clap = raw.get("clap") or {}
    ast = raw.get("ast") or {}
    exp = clap.get("expected") or []
    base = Path(path).parent if path else Path.cwd()
    return Spec(
        group=gkey, group_source=src, id=sid, game=raw.get("game") or game,
        family=raw.get("family") or g.family,
        duration_ms=rng, duration_target_ms=target, duration_tol=tol,
        loop=bool(raw.get("loop", g.loop)),
        stereo_ok=bool(raw.get("stereo", g.stereo_ok)),
        dirty=bool(raw.get("dirty", g.dirty)),
        pitched=bool(raw.get("pitched", g.pitched)),
        attack_max_ms=_num(raw.get("attack_max_ms")) if "attack_max_ms" in raw else g.attack_max_ms,
        # an explicit null means "not checked", like attack_max_ms (specs lane: loops have no head check)
        head_max_ms=_num(raw.get("head_max_ms")) if "head_max_ms" in raw else g.head_max_ms,
        rate_hz=_or(raw.get("rate_hz"), g.rate_hz),
        bpm=_num(raw.get("bpm")), bars=_num(raw.get("bars")),
        beats_per_bar=_num(raw.get("beats_per_bar")) or 4.0,
        intent=raw.get("intent") or raw.get("prompt"),
        clap_labels=list(clap["labels"]) if clap.get("labels") else None,
        clap_expected=[exp] if isinstance(exp, str) else list(exp),
        clap_contrast=[tuple(p) for p in (clap.get("contrast") or []) if len(p) == 2],
        ast_expected=list(ast.get("expected") or []),
        ast_forbid=list(ast.get("forbid") or []),
        refs=_refs(raw, base), path=path, raw=orig,
    )


def load_cards(path: str | Path) -> list[Spec]:
    """A YAML file (one card or a list of cards) or a directory of *.yaml / *.yml."""
    p = Path(path)
    files = sorted([*p.glob("**/*.yaml"), *p.glob("**/*.yml")]) if p.is_dir() else [p]
    out: list[Spec] = []
    for f in files:
        docs = list(yaml.safe_load_all(f.read_text(encoding="utf-8")))
        for doc in docs:
            for raw in (doc if isinstance(doc, list) else [doc]):
                if isinstance(raw, dict):
                    out.append(from_mapping(raw, str(f)))
    return out


def match(stem: str, cards: list[Spec]) -> Spec | None:
    """Card whose id is the longest prefix of the file stem (gun.xung-3 -> gun.xung)."""
    if len(cards) == 1 and not cards[0].id:
        return cards[0]
    s = stem.lower()
    best = None
    for c in cards:
        cid = (c.id or "").lower()
        if cid and s.startswith(cid) and (len(s) == len(cid) or not s[len(cid)].isalnum() or s[len(cid)] == "v"):
            if best is None or len(cid) > len(best.id or ""):
                best = c
    if best is None and len(cards) == 1:
        return cards[0]
    return best


def stem_id(stem: str) -> str:
    """Best-effort id from a candidate file name: 'gun.xung-3' -> 'gun.xung', 'hit.t1_v02' -> 'hit.t1'."""
    import re
    return re.sub(r"(?:[-_ ](?:v|take|seed|s)?\d+)+$", "", stem, flags=re.I) or stem
