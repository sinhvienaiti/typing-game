import json

with open("content/english/qa-batches/batch-34.json") as f:
    batch = json.load(f)

allowed_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}

parts = []
for p in range(1, 6):
    with open(f"scratch/b34_r04_p{p}.json") as f:
        parts.extend(json.load(f))

assert len(parts) == 500, f"Expected 500, got {len(parts)}"

start = 1500
for i, rec in enumerate(parts):
    orig = batch["records"][start + i]
    assert rec["id"] == orig["id"], f"ID mismatch at {start+i}: {rec['id']} != {orig['id']}"
    assert rec["hw"] == orig["hw"], f"HW mismatch at {start+i}: {rec['hw']} != {orig['hw']}"
    assert rec["status"] == "reviewed"
    assert rec["pos"] in allowed_pos, f"Bad POS {rec['pos']} at {rec['hw']}"
    assert len(rec["vi"]) <= 35, f"VI > 35 at {rec['hw']}: {rec['vi']}"
    ipa = rec["ipa"]
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad IPA at {rec['hw']}: {ipa}"
    inner = ipa[1:-1]
    assert inner and not inner.startswith(" ") and not inner.endswith(" "), f"Space IPA at {rec['hw']}: {ipa}"
    batch["records"][start + i] = rec

batch["reviewedCount"] = 2000
batch["status"] = "in-progress"

with open("content/english/qa-batches/batch-34.json", "w") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print("Merged batch-34 round 4 (2000/5000) OK")
