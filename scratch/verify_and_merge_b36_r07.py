import json

ALLOWED_POS = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}

parts = []
for i in range(1, 6):
    with open(f"scratch/b36_r07_p{i}.json", "r", encoding="utf-8") as f:
        p = json.load(f)
    assert len(p) == 100, f"Part {i} length {len(p)} != 100"
    parts.extend(p)

assert len(parts) == 500
for r in parts:
    assert r["status"] == "reviewed", f"bad status: {r['id']}"
    assert r["pos"] in ALLOWED_POS, f"bad pos: {r['id']} {r['pos']}"
    vi = r["vi"]
    assert 0 < len(vi) <= 35, f"bad vi len ({len(vi)}): {r['id']} {r['hw']} -> {vi}"
    assert "/" not in vi, f"slash in vi: {r['id']} {r['hw']} -> {vi}"
    ipa = r["ipa"]
    assert ipa.count("/") == 2 and len(ipa) > 2, f"bad ipa: {r['id']} {r['hw']} -> {ipa}"
    assert not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"ipa space: {r['id']} {r['hw']} -> {ipa}"

with open("content/english/qa-batches/batch-36.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

start = 3000
for idx, r in enumerate(parts):
    orig = batch["records"][start + idx]
    assert orig["id"] == r["id"] and orig["hw"] == r["hw"], f"mismatch at {start + idx}"
    batch["records"][start + idx] = r

batch["reviewedCount"] = 3500
batch["status"] = "in-progress"

with open("content/english/qa-batches/batch-36.json", "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
    f.write("\n")

print("batch-36 round 7 verified and merged (3500/5000)")
