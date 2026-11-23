import json

VALID_POS = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}

reviewed = []
for i in range(1, 6):
    part = json.load(open(f"scratch/b38_r06_reviewed_p{i}.json"))
    assert len(part) == 100
    reviewed.extend(part)

assert len(reviewed) == 500
for r in reviewed:
    assert r["status"] == "reviewed", r
    assert r["pos"] in VALID_POS, r
    assert 0 < len(r["vi"]) <= 35, r
    assert "/" not in r["vi"], r
    assert r["ipa"].count("/") == 2 and not r["ipa"].startswith("/ ") and not r["ipa"].endswith(" /"), r

batch_path = "content/english/qa-batches/batch-38.json"
batch = json.load(open(batch_path))
by_id = {r["id"]: r for r in reviewed}

count = 0
for idx, r in enumerate(batch["records"]):
    if r["id"] in by_id:
        batch["records"][idx] = by_id[r["id"]]
        count += 1

assert count == 500, count
batch["reviewedCount"] = sum(1 for r in batch["records"] if r["status"] == "reviewed")
assert batch["reviewedCount"] == 3000, batch["reviewedCount"]

json.dump(batch, open(batch_path, "w"), ensure_ascii=False, indent=2)
print("Merged batch-38 round 6 (3000/5000) OK")
