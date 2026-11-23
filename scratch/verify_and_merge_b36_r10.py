import json

valid_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}

all_new = []
for p in range(1, 6):
    with open(f"scratch/b36_r10_p{p}.json") as f:
        part = json.load(f)
    assert len(part) == 100, f"Part {p} len={len(part)}"
    all_new.extend(part)

assert len(all_new) == 500

with open("content/english/qa-batches/batch-36.json") as f:
    batch = json.load(f)

start = 4500
orig_slice = batch["records"][start:start + 500]
assert len(orig_slice) == 500

for orig, new in zip(orig_slice, all_new):
    assert orig["id"] == new["id"], f"ID mismatch: {orig['id']} vs {new['id']}"
    assert orig["hw"] == new["hw"], f"Word mismatch: {orig['hw']} vs {new['hw']}"
    assert new["pos"] in valid_pos, f"Bad POS: {new}"
    assert 0 < len(new["vi"]) <= 35, f"Bad len: {new['id']} {new['hw']} ({len(new['vi'])}): {new['vi']}"
    assert "/" not in new["vi"], f"Slash in vi: {new}"
    assert new["ipa"].count("/") == 2 and not new["ipa"].startswith("/ ") and not new["ipa"].endswith(" /"), f"Bad IPA: {new}"
    assert new["status"] == "reviewed"

for idx, new in enumerate(all_new):
    rec = batch["records"][start + idx]
    rec["pos"] = new["pos"]
    rec["ipa"] = new["ipa"]
    rec["vi"] = new["vi"]
    rec["status"] = "reviewed"

assert all(r["status"] == "reviewed" for r in batch["records"]), "Not all reviewed in batch-36!"
batch["reviewedCount"] = 5000
batch["status"] = "completed"

with open("content/english/qa-batches/batch-36.json", "w") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
    f.write("\n")

print("Merged batch-36 round 10 (5000/5000) COMPLETED OK")
