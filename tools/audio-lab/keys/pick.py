"""Gate, rank and choose a consistent family per profile (AUDIO_PIPELINE §4.5, §4.6 step 2, §5.2, §5.5).

Gate (hard): critic L1 PASS at stage final (clip in the float source, onset <= 2 ms, rise <= the card's limit, DC,
true peak, length, tail, 48 kHz mono) and the hit within 15 ms (pipeline.MAX_T_MAIN_MS). L1b flags lower Q only
(§4.3.2: flags in batch 1). The critic's `double_onset` on the key's release is the design (a press and its
upstroke) and costs nothing; anywhere else it is a flam.

Rank (within a profile and part, never across): the critic's combined score (L2 + L3 + L4, calibration
owner-v1) is built for game keys (key_ok: the voice-band proposal of §6.2 favours a bright tick) and would
pull a thock towards a click, so it is one input among four:

    Q = 0.35 fit + 0.25 z(audiobox PQ) + 0.20 z(AST "Typing" / "Computer keyboard") + 0.20 z(critic combined)
        - L1b penalties (flags only, §4.3.2: smeared attack 0.1, pre-echo / hiss / swirl / flam 0.4 ...)

fit = the profile's own targets (keys/specs/<profile>.yaml `fit:`), 0..1, mapped to -1..+1.

Family (§5.2): a set of n strokes from the pool, greedy around each possible medoid: add the best-Q stroke
whose mel distance (0-50 ms) to every member is >= the Kenney P10 pair distance (no near twins) and to the
medoid <= the Kenney P90 family mean (no outlier), preferring strokes of the same take (one keyboard).
A set is kept when its numbers fall in the Kenney P10-P90 ranges; sets are scored by mean Q minus a spread
penalty. The listening list (§4.6): the top set, the most different good set, and for ~30 % of profiles a
probe set from the lower half.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

import numpy as np

from keys import family

# L1b only flags in batch 1 (§4.3.2): a flag lowers Q, it never gates. A keystroke's finger touch before the bottom-out
# reads as a smeared attack to L1b (hf rise > 5 ms), so that flag weighs least.
L1B_PENALTY = {"smeared_attack": 0.1, "pre_echo": 0.4, "double_onset": 0.4}
# Shared-systems bar (SHARED_SYSTEMS_BAR.md, 29/10: 9+): a model artefact gates the stroke, it is never only ranked
L1B_GATE = {"hf_hiss", "phasey_swirl", "noise_floor", "pitch_wobble", "decoder_comb"}
AST_WANT = ("Typing", "Computer keyboard", "Typewriter")
W = {"fit": 0.35, "pq": 0.25, "ast": 0.20, "critic": 0.20}


def _z(vals: list[float | None]) -> list[float]:
    v = np.array([np.nan if x is None else float(x) for x in vals], dtype=float)
    ok = np.isfinite(v)
    if ok.sum() < 2 or np.nanstd(v) == 0:
        return [0.0] * len(vals)
    z = (v - np.nanmean(v)) / np.nanstd(v)
    return [float(np.clip(x, -3, 3)) if np.isfinite(x) else -1.0 for x in z]


def load_pool(run_dir: Path, card_by_part: dict[str, dict]) -> list[dict]:
    """Every stroke of a profile run with its features, critic verdict and scores."""
    idx = json.loads((run_dir / "strokes" / "_strokes.json").read_text("utf-8"))
    # presses of each take (strokes and the presses the slicer skipped), for the 150 ms isolation rule
    # (keys.strokes.ISOLATION_MS; re-checked here for runs sliced before the rule)
    from keys.strokes import ISOLATION_MS
    onsets: dict[str, list[float]] = {}
    for s in idx["strokes"]:
        p = json.loads((run_dir / "strokes" / f"{s['stem']}.proc.json").read_text("utf-8"))
        onsets.setdefault(s["take"], []).append(p["stroke"]["onset_ms"])
    for k in idx.get("skipped") or []:
        onsets.setdefault(k["take"], []).append(k["onset_ms"])
    pool = []
    for s in idx["strokes"]:
        proc = json.loads((run_dir / "strokes" / f"{s['stem']}.proc.json").read_text("utf-8"))
        cj = run_dir / "critic" / f"{s['stem']}.json"
        c = json.loads(cj.read_text("utf-8")) if cj.is_file() else None
        row = {"stem": s["stem"], "part": s["part"], "kind": s["kind"], "take": s["take"], "prompt": s["prompt_key"],
               "seed": s["seed"], "source_kind": s["source_kind"], "path": proc["path"], "proc": proc,
               "feat": proc["features"], "critic_json": str(cj) if c else None}
        why = []
        if c is None:
            why.append("chưa chấm")
        else:
            if c.get("verdict") != "PASS":
                why.append("L1: " + ", ".join(c["L1"].get("blocking") or c["L1"].get("failed") or ["?"]))
            rel = proc["stroke"].get("release_onset")
            rel_ms = None if rel is None else (rel - proc["stroke"]["onset"]) / 48 - proc["render"].get("tightened_ms", 0)
            pen, l1b = 0.0, []
            for f in c.get("flags") or []:
                if f.get("layer") != "L1b":
                    continue
                if f["id"] == "double_onset":
                    after = (f.get("value") or {}).get("after_ms")
                    if rel_ms is not None and after is not None and abs(after - rel_ms) <= 25:
                        continue              # the release: the design
                if f["id"] in L1B_GATE:
                    why.append(f"L1b {f['id']} (lỗi do mô hình)")
                pen += L1B_PENALTY.get(f["id"], 0.0)
                l1b.append(f["id"])
            row["l1b"], row["l1b_penalty"] = l1b, round(pen, 2)
            l3 = ((c.get("L3") or {}).get("scores") or {})
            row["pq"], row["ce"] = l3.get("PQ"), l3.get("CE")
            ast = ((c.get("L4") or {}).get("ast") or {}).get("top5") or []
            row["ast_top5"] = ast
            row["ast"] = max([p for lab, p in ast if lab in AST_WANT] or [0.0])
            clap = ((c.get("L4") or {}).get("clap") or {}).get("top3") or []
            row["clap_top3"] = clap
            row["critic_score"] = (c.get("score") or {}).get("combined")
            row["critic_rank"] = (c.get("score") or {}).get("rank")
            row["metrics"] = {k: (c.get("metrics") or {}).get(k) for k in
                              ("duration_ms", "attack_ms", "head_silence_ms", "true_peak_dbtp", "lufs_m_max",
                               "lufs_100ms_max", "centroid_hz", "key_1k4k_vs_4k8k_db")}
            row["flags"] = [f["id"] for f in c.get("flags") or []]
        if proc.get("raw_qa", {}).get("verdict") != "PASS":
            why.append("clip trong bản float")
        me = proc["stroke"]["onset_ms"]
        near = [o for o in onsets.get(s["take"], []) if o != me and abs(o - me) < ISOLATION_MS]
        if near:
            why.append(f"phím khác cách {min(abs(o - me) for o in near):.0f} ms")
        fit, parts = family.fit_score(row["feat"], (card_by_part[s["part"]].get("fit") or {}))
        row["fit"], row["fit_parts"] = fit, parts
        row["gate"] = "PASS" if not why else "BLOCK"
        row["why"] = why
        pool.append(row)
    for part in ("key", "space"):
        ok = [r for r in pool if r["part"] == part and r["gate"] == "PASS"]
        zp, za, zc = _z([r.get("pq") for r in ok]), _z([r.get("ast") for r in ok]), _z([r.get("critic_score") for r in ok])
        for r, a, b, c_ in zip(ok, zp, za, zc):
            r["z"] = {"pq": round(a, 3), "ast": round(b, 3), "critic": round(c_, 3), "fit": round(2 * r["fit"] - 1, 3)}
            r["Q"] = round(W["fit"] * r["z"]["fit"] + W["pq"] * a + W["ast"] * b + W["critic"] * c_ - r.get("l1b_penalty", 0), 4)
    return pool


def build_set(pool: list[dict], medoid: dict, n: int, ref: dict, prefer_take: bool = True,
              exclude: set[str] = frozenset()) -> list[dict] | None:
    d_min = max(ref["pair_mel_dist"]["p10"] * 0.5, 0.5)
    d_max = ref["mel_dist_mean"]["p90"]
    chosen = [medoid]
    cand = [r for r in pool if r is not medoid and r["stem"] not in exclude]
    while len(chosen) < n:
        best, best_v = None, -1e9
        for r in cand:
            if r in chosen:
                continue
            dm = family.mel_dist(r["feat"], medoid["feat"])
            if dm > d_max:
                continue
            if min(family.mel_dist(r["feat"], c["feat"]) for c in chosen) < d_min:
                continue
            v = r["Q"] - 0.15 * dm + (0.25 if prefer_take and r["take"] == medoid["take"] else 0.0)
            if v > best_v:
                best, best_v = r, v
        if best is None:
            return None
        chosen.append(best)
    return chosen


def set_report(members: list[dict], ref: dict) -> dict:
    st = family.family_stats([m["feat"] for m in members])
    keys = ("mel_dist_mean", "centroid_spread_cents", "peak_spread_cents", "env_corr_mean")
    inr = {k: ref[k]["p10"] <= st[k] <= ref[k]["p90"] for k in keys if k in ref}
    st["min_pair_ok"] = st["mel_dist_min"] >= max(ref["pair_mel_dist"]["p10"] * 0.5, 0.5)
    st["in_kenney_range"] = inr
    # the outlier: largest mean distance to the others
    md = [np.mean([family.mel_dist(a["feat"], b["feat"]) for b in members if b is not a]) for a in members]
    st["worst_member_mean_dist"] = round(float(max(md)), 3)
    st["outlier_ok"] = st["worst_member_mean_dist"] <= ref["mel_dist_mean"]["p90"]
    st["mean_Q"] = round(float(np.mean([m["Q"] for m in members])), 4)
    st["mean_fit"] = round(float(np.mean([m["fit"] for m in members])), 4)
    st["kinds"] = sorted({m["kind"] for m in members})
    st["takes"] = sorted({m["take"] for m in members})
    return st


def candidate_sets(pool: list[dict], part: str, n: int, ref: dict) -> list[dict]:
    """Every acceptable set (one per medoid and sub-pool), best first. Sub-pools: each prompt alone (one keyboard
    description), then the whole pool; full strokes (press + release) before mixed ones."""
    ok = [r for r in pool if r["part"] == part and r["gate"] == "PASS"]
    pools = []
    for prompt in sorted({r["prompt"] for r in ok}):
        sub = [r for r in ok if r["prompt"] == prompt]
        pools += [([r for r in sub if r["kind"] == "press+release"], f"prompt {prompt}, press+release"),
                  (sub, f"prompt {prompt}")]
    pools += [([r for r in ok if r["kind"] == "press+release"], "all, press+release"), (ok, "all")]
    out = []
    for kind_pool, label in pools:
        if len(kind_pool) < n:
            continue
        for med in sorted(kind_pool, key=lambda r: -r["Q"])[:30]:
            members = build_set(kind_pool, med, n, ref)
            if members is None:
                continue
            rep = set_report(members, ref)
            prompts = {m["prompt"] for m in members}
            score = (rep["mean_Q"] - 0.1 * max(0.0, rep["mel_dist_mean"] - ref["mel_dist_mean"]["p50"])
                     - 0.1 * (len(prompts) - 1) - 0.01 * (len(rep["takes"]) - 1))
            if not rep["min_pair_ok"] or not rep["outlier_ok"]:
                score -= 1.0
            if len(rep["kinds"]) > 1:
                score -= 0.15                 # a set where some keys have no upstroke sounds like two keyboards
            rep["prompts"] = sorted(prompts)
            out.append({"medoid": med["stem"], "pool": label, "members": [m["stem"] for m in members],
                        "score": round(score, 4), "report": rep})
    out.sort(key=lambda s: -s["score"])
    uniq, seen = [], set()
    for s in out:
        key = tuple(sorted(s["members"]))
        if key not in seen:
            seen.add(key)
            uniq.append(s)
    return uniq


def listening_list(sets: list[dict], pool: list[dict], probe: bool, seed: int) -> list[dict]:
    """§4.6 step 2 on sets: top, the most different good set (shares <= 30 % with the top), a probe from the lower half."""
    if not sets:
        return []
    by = {r["stem"]: r for r in pool}
    top = sets[0]
    med_top = by[top["medoid"]]["feat"]
    good = [s for s in sets[1:] if s["score"] >= top["score"] - 0.6
            and len(set(s["members"]) & set(top["members"])) <= 0.3 * len(top["members"])]
    out = [{**top, "role": "top"}]
    if good:
        far = max(good, key=lambda s: family.mel_dist(by[s["medoid"]]["feat"], med_top))
        out.append({**far, "role": "distinct"})
    if probe and len(sets) > 3:
        lower = [s for s in sets[len(sets) // 2:] if all(len(set(s["members"]) & set(o["members"])) <= 0.5 * len(s["members"]) for o in out)]
        if lower:
            out.append({**random.Random(seed).choice(lower), "role": "probe"})
    return out
