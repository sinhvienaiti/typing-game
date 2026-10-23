"""Pair test (port of the PoC score_pairs.py): how often each layer prefers the original over its
degraded copy `<stem>__clipped|muddy|thin`. Input: one or more critic output directories."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

KINDS = ("clipped", "muddy", "thin")


def _values(r: dict) -> dict[str, float]:
    v: dict[str, float] = {}
    gate = 0.0 if r["verdict"] == "BLOCK" else 1.0
    l2 = (r.get("L2") or {}).get("score")
    if l2 is not None:
        v["L2 (điểm mục tiêu)"] = l2
        v["L1 rồi L2 (bộ chấm)"] = gate + l2
    v["L1 (qua cổng)"] = gate
    v["L1b (−số cờ)"] = -len((r.get("L1b") or {}).get("flags") or [])
    for ax in ("PQ", "CE", "CU"):
        s = ((r.get("L3") or {}).get("scores") or {}).get(ax)
        if s is not None:
            v[f"AES {ax}"] = s
    pam = ((r.get("L4") or {}).get("clap") or {}).get("pam_clean")
    if pam is not None:
        v["CLAP PAM sạch"] = pam
    return v


def load(dirs: list[str]) -> dict[str, dict[str, float]]:
    out = {}
    for d in dirs:
        for f in Path(d).glob("*.json"):
            if f.name.startswith("_"):
                continue
            r = json.loads(f.read_text(encoding="utf-8"))
            if r.get("schema", "").startswith("audiolab.critic.file/"):
                out[Path(r["file"]["name"]).stem] = _values(r)
    return out


def table(scores: dict[str, dict[str, float]]) -> str:
    critics = sorted({c for v in scores.values() for c in v})
    origs = sorted({s.split("__")[0] for s in scores if "__" in s})
    res = {c: {k: [0.0, 0] for k in KINDS} for c in critics}
    for o in origs:
        for k in KINDS:
            d = f"{o}__{k}"
            for c in critics:
                if c in scores.get(o, {}) and c in scores.get(d, {}):
                    a, b = scores[o][c], scores[d][c]
                    res[c][k][1] += 1
                    res[c][k][0] += 1 if a > b else (0.5 if a == b else 0)
    lines = ["| Lớp | Clip | Đục | Mỏng | Tổng |", "|---|---|---|---|---|"]
    for c in critics:
        r = res[c]
        if not any(v[1] for v in r.values()):
            continue
        tot = sum(v[0] for v in r.values()), sum(v[1] for v in r.values())
        cell = lambda x: f"{x[0]:g}/{x[1]}".replace(".", ",")
        lines.append(f"| {c} | " + " | ".join(cell(r[k]) for k in KINDS) + f" | **{cell(tot)}** |")
    return "\n".join(lines)


def main(dirs: list[str]) -> None:
    print(table(load(dirs)))
