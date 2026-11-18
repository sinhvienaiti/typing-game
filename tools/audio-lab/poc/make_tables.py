"""make_tables.py - markdown tables for report.md from out/*.json (run from the poc dir)."""
import json
import os

O = "out"


def stem(p):
    return os.path.splitext(os.path.basename(p))[0]


rows = json.load(open(f"{O}/analyze/_all_metrics.json"))
crit = json.load(open(f"{O}/critics.json"))
lis = json.load(open(f"{O}/listener.json"))

print("### Technical metrics (analyze.py)\n")
print("| File | profile | dur s | peak dBFS | TP dBTP | LUFS-M max | crest dB | attack ms | punch dB | HF@hit dB | centroid Hz | low/mid/high % | laptop loss dB | clips | loop | verdict: flags |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for r in rows:
    lmh = "/".join(f"{v*100:.0f}" for v in r["low_mid_high_share"])
    flags = ", ".join(f["rule"] for f in r["qa_flags"]) or "-"
    print(f"| {stem(r['file'])} | {r['profile']} | {r['duration_s']:.2f} | {r['peak_dbfs']} | {r['true_peak_dbtp']} | "
          f"{r['lufs_momentary_max']} | {r['crest_factor_db']} | {r['attack_ms_10_90']} | {r['punch_db_early20_vs_100_300']} | "
          f"{r['transient_hf_share_db']} | {r['spectral_centroid_hz']:.0f} | {lmh} | {r['laptop_speaker_loss_db']} | "
          f"{r['clipped_samples']} | {r['loop_score'] if r['profile'] == 'loop' else ''} | **{r['qa_verdict']}**: {flags} |")

print("\n### Learned critics on the originals\n")
print("| File | AES CE | AES CU | AES PC | AES PQ | CLAP-unfused top quality probe (p) | CLAP-larger top quality probe (p) | CLAP-unfused category #1 | CLAP-larger category #1 | AST top-2 | ALM-0.6B caption | ALM clean? |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|")
short = {"a punchy, powerful, high quality impact sound effect": "punchy",
         "a weak, thin, quiet little click": "weak",
         "a harsh, distorted, clipped, overdriven noise": "harsh",
         "a muddy, boomy, muffled low thud": "muddy"}
for path, a in crit["aes"].items():
    cu = crit["clap_unfused"][path]
    cl = crit["clap_larger_general"][path]
    ast = crit["ast"][path]
    li = lis.get(os.path.basename(path), {})
    pu = max(cu["quality_probs"])
    pl = max(cl["quality_probs"])
    cap = li.get("caption", "")
    cap = (cap[:70] + "...") if len(cap) > 70 else cap
    print(f"| {stem(path)} | {a['CE']} | {a['CU']} | {a['PC']} | {a['PQ']} | {short[cu['quality_top']]} ({pu}) | "
          f"{short[cl['quality_top']]} ({pl}) | {cu['category_top3'][0][0]} | {cl['category_top3'][0][0]} | "
          f"{ast[0][0]} {ast[0][1]}, {ast[1][0]} {ast[1][1]} | {cap} | {li.get('clean_yn', '')} |")

log = crit["_log"]
print("\n### Run log (critics.py, first run incl. download)\n")
print("```")
print(json.dumps(log, indent=1))
print(json.dumps(lis.get("_log", {})))
print("```")
