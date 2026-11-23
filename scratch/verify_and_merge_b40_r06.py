import json

BAD_PREFIXES = ("các ", "những ", "số nhiều", "xem ", "cách viết", "dạng ", "thgt ", "danh từ số nhiều")
VALID_POS = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}

updates = {}
for p in range(1, 6):
    with open(f"scratch/b40_r06_p{p}.json") as f:
        part = json.load(f)
    assert len(part) == 100, f"p{p} len={len(part)}"
    for u in part:
        vi = u["vi"]
        ipa = u["ipa"]
        pos = u["pos"]
        assert 0 < len(vi) <= 35, f"{u['id']} vi len={len(vi)}: {vi!r}"
        assert "/" not in vi, f"{u['id']} slash in vi: {vi!r}"
        assert not vi.lower().startswith(BAD_PREFIXES), f"{u['id']} bad prefix: {vi!r}"
        assert pos in VALID_POS, f"{u['id']} bad pos: {pos!r}"
        assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"{u['id']} bad ipa: {ipa!r}"
        assert not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"{u['id']} ipa space: {ipa!r}"
        assert u["id"] not in updates, f"dup id {u['id']}"
        updates[u["id"]] = u

assert len(updates) == 500

with open("content/english/qa-batches/batch-40.json") as f:
    batch = json.load(f)

matched = 0
for r in batch["records"]:
    if r["id"] in updates:
        u = updates[r["id"]]
        r["pos"] = u["pos"]
        r["ipa"] = u["ipa"]
        r["vi"] = u["vi"]
        r["status"] = "reviewed"
        matched += 1

assert matched == 500, f"matched={matched}"
batch["reviewedCount"] = 3000
batch["status"] = "in-progress"

with open("content/english/qa-batches/batch-40.json", "w") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
    f.write("\n")

print("Merged batch-40 round 6 (3000/4998) OK")
