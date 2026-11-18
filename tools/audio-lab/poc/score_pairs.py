"""score_pairs.py - how often does each critic prefer the good original over its degraded copy?

Usage: python -I score_pairs.py  (run from the poc dir; reads out/*.json, prints markdown)
"""
import json
import os
from collections import defaultdict

O = "out"


def stem(p):
    return os.path.splitext(os.path.basename(p))[0]


def load():
    crit = json.load(open(f"{O}/critics.json"))
    critd = json.load(open(f"{O}/critics_degraded.json"))
    ana = {stem(m["file"]): m for m in json.load(open(f"{O}/analyze/_all_metrics.json"))}
    ana.update({stem(m["file"]): m for m in json.load(open(f"{O}/analyze_degraded/_all_metrics.json"))})
    scores = defaultdict(dict)
    for src in (crit, critd):
        for path, v in src.get("aes", {}).items():
            s = stem(path)
            for ax in ("CE", "CU", "PQ"):
                scores[s][f"AES {ax}"] = v[ax]
        for key, lab in (("clap_unfused", "CLAP-unfused"), ("clap_larger_general", "CLAP-larger")):
            for path, v in src.get(key, {}).items():
                s = stem(path)
                scores[s][f"{lab} intent cos"] = v["intent_cos"]
                scores[s][f"{lab} PAM clean"] = v["pam_clean_prob"]
                scores[s][f"{lab} P(punchy)"] = v["quality_probs"][0]
        for path, v in src.get("ast", {}).items():
            scores[stem(path)]["AST top1 conf"] = v[0][1]
    import re
    for fn in (f"{O}/listener.json", f"{O}/listener_degraded.json"):
        if os.path.exists(fn):
            for name, v in json.load(open(fn)).items():
                if name.startswith("_"):
                    continue
                st = stem(name)
                scores[st]["ALM-0.6B says clean"] = 1.0 if v["clean_yn"].strip().lower().startswith("yes") else 0.0
                mm = re.search(r"\d+", v["punch"])
                scores[st]["ALM-0.6B punch 1-10"] = float(mm.group()) if mm else 0.0
    for s, m in ana.items():
        pen = sum(3 if f["level"] == "FAIL" else 1 for f in m["qa_flags"])
        scores[s]["Rules (-penalty)"] = -pen
    return scores


def main():
    sc = load()
    critics = list(next(iter(sc.values())).keys())
    critics = sorted({c for v in sc.values() for c in v})
    origs = sorted({s.split("__")[0] for s in sc if "__" in s})
    kinds = ["clipped", "muddy", "thin"]
    res = {c: {k: [0, 0] for k in kinds} for c in critics}
    for o in origs:
        for k in kinds:
            d = f"{o}__{k}"
            for c in critics:
                if c in sc[o] and c in sc.get(d, {}):
                    a, b = sc[o][c], sc[d][c]
                    res[c][k][1] += 1
                    res[c][k][0] += 1 if a > b else (0.5 if a == b else 0)
    print("| Critic | clipped | muddy | thin | total |")
    print("|---|---|---|---|---|")
    for c in critics:
        r = res[c]
        tot = sum(v[0] for v in r.values()), sum(v[1] for v in r.values())
        print(f"| {c} | " + " | ".join(f"{r[k][0]:g}/{r[k][1]}" for k in kinds) + f" | **{tot[0]:g}/{tot[1]}** |")
    print()
    print("Synthetic archetypes (higher = better for every column):")
    names = ["syn_punchy_impact", "syn_weak_click", "syn_muddy_low", "syn_clipped_harsh"]
    print("| Critic | punchy | weak | muddy | clipped | punchy ranked #1? | clipped ranked last? |")
    print("|---|---|---|---|---|---|---|")
    for c in critics:
        vals = [sc[n].get(c) for n in names]
        if None in vals:
            continue
        best = max(range(4), key=lambda i: vals[i])
        worst = min(range(4), key=lambda i: vals[i])
        print(f"| {c} | " + " | ".join(f"{v:.3f}" if isinstance(v, float) else str(v) for v in vals)
              + f" | {'yes' if best == 0 else 'no (' + names[best][4:] + ')'} | {'yes' if worst == 3 else 'no (' + names[worst][4:] + ')'} |")


if __name__ == "__main__":
    main()
