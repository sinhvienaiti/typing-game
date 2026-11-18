"""Owner calibration of the critic (§4.6): versioned layer weights and L2 targets from blind ratings.

A calibration file (critic/calibration/owner-v<N>.json, schema `audiolab.critic.calibration/1`) holds
ordered rules. Each rule matches rank groups by family, group, game and/or id (regex) and either
  - scales the §4.5 layer weights (`weights.rules[].scale`, the freed weight goes to `to`, default L2,
    so the §4.4 cap on L4 is never exceeded), or
  - edits the §4.3.3 L2 targets of a group (`l2.rules[]`: `drop`, `weight`, `set`).
For one layer or one target feature the last matching rule wins. Owner-approved references (>= 5)
still replace a target's good band after the calibration (refs are better evidence).

L1 hygiene and L1b flags are never calibrated here: a file that names them is refused.

Which file is used: `--calibration PATH|VERSION|none` of `critic run`, else the environment variable
AUDIOLAB_CRITIC_CALIBRATION (same values), else the highest version in critic/calibration/.
"""
from __future__ import annotations

import json
import math
import os
import re
from dataclasses import dataclass, field
from pathlib import Path

from . import groups as G

SCHEMA = "audiolab.critic.calibration/1"
DIR = Path(__file__).resolve().parent / "calibration"
ENV = "AUDIOLAB_CRITIC_CALIBRATION"
LAYERS = ("L2", "L3", "L4", "L5")
TOP_KEYS = {"schema", "version", "date", "status", "basis_vi", "data", "agreement", "weights", "l2", "notes_vi"}
MATCH_KEYS = {"family", "group", "game", "id"}
FORBIDDEN = re.compile(r"^(l1b?|hygiene|gate)$", re.I)     # never calibrated here (§4.3.1, §4.3.2)
NONE = ("none", "off", "0", "")


class CalibrationError(ValueError):
    pass


def _match(m: dict, family: str | None, group: str | None, game: str | None, sid: str | None) -> bool:
    for k, v in m.items():
        vals = v if isinstance(v, list) else [v]
        if k == "id":
            if not sid or not any(re.search(p, sid) for p in vals):
                return False
        elif {"family": family, "group": group, "game": game}[k] not in vals:
            return False
    return True


def _bound(v, inf: float) -> float:
    return inf if v is None else float(v)


def _target(d: dict) -> G.Target:
    good, bad = d["good"], d.get("bad", d["good"])
    return G.Target(d["feature"], (_bound(good[0], -G.INF), _bound(good[1], G.INF)),
                    (_bound(bad[0], -G.INF), _bound(bad[1], G.INF)), float(d.get("weight", 1.0)),
                    d.get("low_vi", ""), d.get("high_vi", ""))


@dataclass
class Calibration:
    version: str
    path: str | None
    date: str | None = None
    weight_rules: list[dict] = field(default_factory=list)
    l2_rules: list[dict] = field(default_factory=list)
    doc: dict = field(default_factory=dict, repr=False)

    # ------------------------------------------------------------- layer weights (§4.5)
    def weights(self, plan: dict[str, float], *, family=None, group=None, game=None, sid=None) -> tuple[dict, list]:
        """(weights after the rules, ids of the rules applied). Sum is kept; L4 never grows."""
        scale: dict[str, float] = {}
        to: dict[str, str] = {}
        applied = []
        for r in self.weight_rules:
            if _match(r.get("match") or {}, family, group, game, sid):
                for L, s in (r.get("scale") or {}).items():
                    scale[L] = float(s)
                    to[L] = r.get("to", "L2")
                applied.append(r["id"])
        w = dict(plan)
        for L, s in scale.items():
            freed = w[L] * (1.0 - s)
            w[L] = w[L] * s
            dest = to[L]
            if dest in w and dest != L:
                w[dest] += freed
        return w, applied

    # ------------------------------------------------------------- L2 targets (§4.3.3)
    def targets(self, base: list[G.Target], *, family=None, group=None, game=None, sid=None) -> tuple[list, dict]:
        """(targets after the rules, {feature: rule id} of the features a rule changed)."""
        out = list(base)
        changed: dict[str, str] = {}
        for r in self.l2_rules:
            if not _match(r.get("match") or {}, family, group, game, sid):
                continue
            drop = set(r.get("drop") or [])
            if drop:
                out = [t for t in out if t.feature not in drop]
                changed.update({f: r["id"] for f in drop})
            for f, w in (r.get("weight") or {}).items():
                out = [G.Target(t.feature, t.good, t.bad, float(w), t.low_vi, t.high_vi) if t.feature == f else t
                       for t in out]
                changed[f] = r["id"]
            for d in r.get("set") or []:
                t = _target(d)
                if any(x.feature == t.feature for x in out):
                    out = [t if x.feature == t.feature else x for x in out]
                else:
                    out.append(t)
                changed[t.feature] = r["id"]
        return out, changed

    def to_json(self) -> dict:
        return {"version": self.version, "path": self.path, "date": self.date}


def _check(doc: dict, where: str) -> None:
    def bad(msg: str):
        raise CalibrationError(f"file hiệu chỉnh {where}: {msg}")

    if not isinstance(doc, dict) or doc.get("schema") != SCHEMA:
        bad(f"thiếu schema {SCHEMA}")
    for k in doc:
        if FORBIDDEN.match(k):
            bad(f"khóa '{k}': L1 và L1b không được hiệu chỉnh ở đây (mục 4.3.1, 4.3.2)")
        if k not in TOP_KEYS:
            bad(f"khóa lạ '{k}'")
    if not str(doc.get("version") or "").strip():
        bad("thiếu version")
    ids = set()
    for sect, kind in (("weights", "w"), ("l2", "t")):
        for r in ((doc.get(sect) or {}).get("rules") or []):
            if not r.get("id") or r["id"] in ids:
                bad(f"luật thiếu id hoặc trùng id ({r.get('id')})")
            ids.add(r["id"])
            for k in (r.get("match") or {}):
                if k not in MATCH_KEYS:
                    bad(f"luật {r['id']}: khóa khớp lạ '{k}'")
            grp = (r.get("match") or {}).get("group")
            for gk in (grp if isinstance(grp, list) else [grp] if grp else []):
                if gk not in G.GROUPS:
                    bad(f"luật {r['id']}: nhóm '{gk}' không có")
            for p in ([(r.get("match") or {}).get("id")] if isinstance((r.get("match") or {}).get("id"), str)
                      else (r.get("match") or {}).get("id") or []):
                try:
                    re.compile(p)
                except re.error as e:
                    bad(f"luật {r['id']}: regex id sai ({e})")
            if kind == "w":
                for L, s in (r.get("scale") or {}).items():
                    if L not in LAYERS:
                        bad(f"luật {r['id']}: lớp '{L}' không xếp hạng (chỉ {', '.join(LAYERS)})")
                    if not (isinstance(s, (int, float)) and 0.0 <= s <= 1.0):
                        bad(f"luật {r['id']}: hệ số của {L} phải trong 0–1 (chỉ hạ trọng số, không nâng)")
                if r.get("to", "L2") not in LAYERS or r.get("to") == "L4":
                    bad(f"luật {r['id']}: phần trọng số bớt ra không được dồn cho L4 (trần 0,1, mục 4.4)")
            else:
                for d in r.get("set") or []:
                    if not d.get("feature") or not isinstance(d.get("good"), list) or len(d["good"]) != 2:
                        bad(f"luật {r['id']}: mục tiêu cần feature và good [thấp, cao]")
                    if "bad" in d and (not isinstance(d["bad"], list) or len(d["bad"]) != 2):
                        bad(f"luật {r['id']}: bad phải là [thấp, cao]")
                    t = _target(d)
                    if not (t.bad[0] <= t.good[0] <= t.good[1] <= t.bad[1]):
                        bad(f"luật {r['id']}: {d['feature']}: cần bad thấp ≤ good thấp ≤ good cao ≤ bad cao")
                for f, w in (r.get("weight") or {}).items():
                    if not (isinstance(w, (int, float)) and w >= 0 and math.isfinite(w)):
                        bad(f"luật {r['id']}: trọng số của {f} phải ≥ 0")


def from_dict(doc: dict, path: str | None = None) -> Calibration:
    _check(doc, path or "(trong bộ nhớ)")
    return Calibration(version=str(doc["version"]), path=path, date=doc.get("date"),
                       weight_rules=list((doc.get("weights") or {}).get("rules") or []),
                       l2_rules=list((doc.get("l2") or {}).get("rules") or []), doc=doc)


def available(directory: Path = DIR) -> list[Path]:
    """Calibration files, oldest version first (owner-v1.json, owner-v2.json, ...)."""
    def key(p: Path):
        m = re.search(r"v(\d+)", p.stem)
        return (int(m.group(1)) if m else -1, p.name)
    return sorted(directory.glob("*.json"), key=key)


def load(which: str | Path | None = None, directory: Path = DIR) -> Calibration | None:
    """None when calibration is off (`none`) or no file exists."""
    if which is None:
        which = os.environ.get(ENV)
    if which is not None and str(which).strip().lower() in NONE:
        return None
    if which is None:
        files = available(directory)
        if not files:
            return None
        p = files[-1]
    else:
        p = Path(str(which)).expanduser()
        if not p.is_file():
            hits = [f for f in available(directory) if f.stem in (str(which), f"owner-v{which}", f"owner-{which}")]
            if not hits:
                raise CalibrationError(f"không thấy file hiệu chỉnh '{which}' (có: "
                                       f"{', '.join(f.name for f in available(directory)) or 'không có'})")
            p = hits[-1]
    try:
        doc = json.loads(p.read_text(encoding="utf-8"))
    except ValueError as e:
        raise CalibrationError(f"file hiệu chỉnh {p}: JSON sai ({e})") from e
    return from_dict(doc, str(p))


def spec_keys(spec) -> dict:
    """Match keys of a Spec object or a result's `spec` mapping."""
    get = spec.get if isinstance(spec, dict) else (lambda k, d=None: getattr(spec, k, d))
    return {"family": get("family"), "group": get("group"), "game": get("game"), "sid": get("id")}
