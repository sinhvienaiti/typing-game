"""Combined score, ranks, "ask the owner" (§4.5) and the listening list (§4.6 step 2).

Within one rank group (same sound id, else same critic group), every layer becomes a z-score
over the files that passed L1; the combined score is the §4.5 weighted sum. Layers that did not
run drop out and the remaining weights are renormalised. Blocked files are never ranked.
"""
from __future__ import annotations

import hashlib
import math
import random

import numpy as np

from .audio import fnum
from .thresholds import LEARNED, PROBE_RATE, RANK_GAP_ASK, TOP_READ, WEIGHTS, Z_FLOOR

LAYERS = ("L2", "L3", "L4", "L5")


def stage_for(dirty: bool, n_refs: int) -> str:
    if n_refs >= LEARNED["ref5"]:
        if dirty and n_refs < LEARNED["ref10_dirty"]:
            return "ref5-dirty"
        return "ref5"
    return "batch1-dirty" if dirty else "batch1"


def rank_key(r: dict) -> str:
    """Same sound id (from a card, or a known id pattern) ranks together; otherwise the group."""
    sp = r["spec"]
    if sp.get("id") and (sp.get("path") or sp.get("group_source") == "id"):
        return f"id:{sp['id']}"
    return f"group:{sp['group']}"


def _layer_value(r: dict, layer: str) -> float | None:
    if layer == "L2":
        return (r.get("L2") or {}).get("score")
    if layer == "L3":
        s = ((r.get("L3") or {}).get("scores")) or {}
        return None if s.get("PQ") is None else (s["PQ"] + s.get("CE", s["PQ"])) / 2
    if layer == "L4":
        l4 = r.get("L4") or {}
        return l4.get("score") if l4.get("available") else None
    if layer == "L5":
        l5 = r.get("L5") or {}
        return l5.get("nearest_sim") if l5.get("available") else None
    return None


def _z(vals: list[float | None], floor: float) -> list[float | None]:
    xs = [v for v in vals if v is not None]
    if len(xs) < 2:
        return [0.0 if v is not None else None for v in vals]
    mu, sd = float(np.mean(xs)), max(float(np.std(xs)), floor)
    return [None if v is None else (v - mu) / sd for v in vals]


def _ranks(vals: list[float | None]) -> list[int | None]:
    order = sorted([i for i, v in enumerate(vals) if v is not None], key=lambda i: -vals[i])
    out: list[int | None] = [None] * len(vals)
    for k, i in enumerate(order):
        out[i] = k + 1
    return out


DIST_FEATURES = ("centroid_hz", "duration_ms", "attack_ms", "crest_db", "tail_ms", "punch_db", "mud_share",
                 "share_below_150", "share_above_3k")


# Beds and music loops: attack, tail and punch mean nothing for a 6 s loop (batch 0b review);
# colour, level movement and width tell two loops apart.
LOOP_DIST_FEATURES = ("centroid_hz", "rolloff85_hz", "flatness", "mud_share", "share_below_150", "share_above_3k",
                      "lufs_m_range_db", "stereo_correlation")


def _vec(r: dict) -> np.ndarray:
    m = r.get("metrics") or {}
    loop = bool((r.get("spec") or {}).get("loop"))
    out = []
    for f in (LOOP_DIST_FEATURES if loop else DIST_FEATURES):
        v = m.get(f)
        v = (1.0 if f == "stereo_correlation" else 0.0) if v is None else float(v)
        out.append(math.log1p(max(v, 0.0)) if f in ("centroid_hz", "rolloff85_hz", "duration_ms", "attack_ms", "tail_ms") else v)
    return np.array(out)


# L4 flags that do not ask the owner until AST is calibrated on owner ratings (§4.6; ours).
UNCALIBRATED_FLAGS = {"ast_expected_missing", "ast_low_conf"}


def _flag_asks(f: dict, have: dict[str, int], n_elig: int) -> bool:
    if f["layer"] == "L4":
        if f["id"] in UNCALIBRATED_FLAGS:
            return False
        return n_elig >= 2 and 0 < have.get(f["id"], 0) < n_elig
    return f["layer"] in ("L1b", "L5")


def ask_stats(results: list[dict]) -> dict:
    """Share of files that ask the owner, and of each flag type (for summary.md and REPORT.md)."""
    el = [r for r in results if r["verdict"] != "BLOCK"]
    n = len(el)
    by: dict[str, dict] = {}
    for r in el:
        for f in r.get("flags", []):
            k = f"{f['layer']}:{f['id']}"
            e = by.setdefault(k, {"files": 0, "ask": 0})
            e["files"] += 1
            e["ask"] += bool(f.get("ask"))
    return {"n": n, "ask_owner": sum(1 for r in el if r["ask_owner"]["value"]), "flags": dict(sorted(by.items()))}


def combine(results: list[dict], n_refs: int | None = None, seed: int = 0, calibration=None) -> dict:
    """Mutates every result (adds `score`, `ask_owner`, `read_card`); returns batch-level info.

    `n_refs` forces the approved-reference count; by default each rank group uses the largest
    reference set among its files (result["refs"]["n"]). `calibration` (critic/calibration.py) scales
    the §4.5 weights per family, group or id from owner ratings (§4.6); None = the plan's weights."""
    groups: dict[str, list[dict]] = {}
    for r in results:
        groups.setdefault(rank_key(r), []).append(r)
    listen = {}
    for gk, rs in groups.items():
        dirty = any(r["spec"].get("dirty") for r in rs)
        n = n_refs if n_refs is not None else max(((r.get("refs") or {}).get("n") or 0) for r in rs)
        stage = stage_for(dirty, n)
        plan = dict(zip(LAYERS, WEIGHTS[stage]))
        w, cal_rules = dict(plan), []
        cal = calibration.version if calibration is not None else None
        if calibration is not None:
            from .calibration import spec_keys
            w, cal_rules = calibration.weights(w, **spec_keys(rs[0]["spec"]))
        elig = [r for r in rs if r["verdict"] != "BLOCK"]
        raw = {L: [_layer_value(r, L) for r in elig] for L in LAYERS}
        avail = {L: any(v is not None for v in raw[L]) and w[L] > 0 for L in LAYERS}
        tot = sum(w[L] for L in LAYERS if avail[L]) or 1.0
        used = {L: (w[L] / tot if avail[L] else 0.0) for L in LAYERS}
        z = {L: _z(raw[L], Z_FLOOR[L]) for L in LAYERS}
        comb = []
        for i, r in enumerate(elig):
            parts = {L: z[L][i] for L in LAYERS if used[L] > 0 and z[L][i] is not None}
            c = sum(used[L] * v for L, v in parts.items())
            comb.append(c)
            r["score"] = {"combined": fnum(c, 4), "stage": stage, "rank_group": gk,
                          "weights_plan": dict(plan), "weights_used": {L: fnum(v, 3) for L, v in used.items()},
                          "calibration": cal, "calibration_rules": cal_rules,
                          "z": {L: fnum(v, 3) for L, v in parts.items()}}
        rk = _ranks([c for c in comb])
        r2 = _ranks(raw["L2"])
        r3 = _ranks([None if v is None else v for v in raw["L3"]])
        for i, r in enumerate(elig):
            r["score"].update({"rank": rk[i], "rank_l2": r2[i], "rank_l3": r3[i], "n_ranked": len(elig)})
        for r in rs:
            if r["verdict"] == "BLOCK":
                r["score"] = {"combined": None, "stage": stage, "rank_group": gk, "rank": None,
                              "rank_l2": None, "rank_l3": None, "n_ranked": len(elig),
                              "weights_plan": dict(plan), "weights_used": None,
                              "calibration": cal, "calibration_rules": cal_rules, "z": {}}
        # ask the owner (§4.5). Ours, until the learned layers are calibrated on owner ratings (§4.6):
        # AST "expected label missing" / "low confidence" never ask (they fired on most batch-0 files),
        # and an L4 flag asks only when it separates candidates of this id (some have it, some not):
        # a flag every candidate shares describes the id or the model, not a candidate.
        have: dict[str, int] = {}
        for r in elig:
            for fid in {f["id"] for f in r.get("flags", []) if f["layer"] == "L4"}:
                have[fid] = have.get(fid, 0) + 1
        for r in rs:
            reasons = []
            for f in r.get("flags", []):
                f["ask"] = _flag_asks(f, have, len(elig))
            if r["verdict"] != "BLOCK":
                s = r["score"]
                if used["L3"] > 0 and s["rank_l2"] and s["rank_l3"] and abs(s["rank_l2"] - s["rank_l3"]) > RANK_GAP_ASK:
                    reasons.append(f"L2 xếp hạng {s['rank_l2']}, L3 xếp hạng {s['rank_l3']} (lệch quá {RANK_GAP_ASK} bậc)")
                for f in r.get("flags", []):
                    if f["ask"]:
                        reasons.append(f"{f['layer']}: {f['msg_vi']}")
            r["ask_owner"] = {"value": bool(reasons), "reasons": reasons}
        # listening list (§4.6 step 2). Entries are result stems (unique per run), not file names.
        order = sorted(elig, key=lambda r: r["score"]["rank"] or 1e9)
        entry = {"rank_group": gk, "stage": stage, "top": None, "distinct": None, "probe": None,
                 "weights_used": {L: fnum(v, 3) for L, v in used.items()}}
        if order:
            top = order[0]
            entry["top"] = top["file"]["stem"]
            rest = order[1:]
            if rest:
                V = np.stack([_vec(r) for r in order])
                sd = V.std(axis=0)
                sd[sd == 0] = 1.0
                d = np.linalg.norm((V[1:] - V[0]) / sd, axis=1)
                distinct = rest[int(np.argmax(d))]
                entry["distinct"] = distinct["file"]["stem"]
                h = int(hashlib.sha256(f"{seed}:{gk}".encode()).hexdigest()[:8], 16)
                rng = random.Random(h)
                if rng.random() < PROBE_RATE:
                    # §4.6 step 2: a probe is drawn from the machine's lower half only (flagged files
                    # already ranked there are in it; a flagged file in the upper half is not a probe)
                    half = len(order) // 2
                    pool = [r for r in order[max(1, half):] if r is not distinct]
                    if pool:
                        entry["probe"] = rng.choice(pool)["file"]["stem"]
        listen[gk] = entry
        names = {entry["top"], entry["distinct"], entry["probe"]} - {None}
        for r in rs:
            rank = (r.get("score") or {}).get("rank")
            r["read_card"] = bool(r["ask_owner"]["value"] or r["file"]["stem"] in names
                                  or (rank is not None and rank <= TOP_READ))
    return {"listen": listen}
