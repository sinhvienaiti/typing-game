import json
import sys

# Load all 5 parts
parts = []
for p in range(1, 6):
    path = f"scratch/b23_r01_p{p}.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} does not have 100 records (got {len(data)})"
        parts.extend(data)

assert len(parts) == 500, f"Expected 500 records, got {len(parts)}"

# Load batch-23.json
batch_path = "content/english/qa-batches/batch-23.json"
with open(batch_path, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

records = batch_data["records"]
assert len(records) == 5000, f"Expected 5000 records in batch-23, got {len(records)}"

# Check and update records 0 to 499
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}

for i in range(500):
    orig = records[i]
    rev = parts[i]
    assert orig["id"] == rev["id"], f"ID mismatch at {i}: {orig['id']} vs {rev['id']}"
    assert orig["hw"] == rev["hw"], f"HW mismatch at {i}: {orig['hw']} vs {rev['hw']}"
    assert rev["status"] == "reviewed", f"Status not reviewed at {i}"
    assert len(rev["vi"]) <= 35, f"vi length > 35 at {i} ({rev['hw']}): {len(rev['vi'])} - {rev['vi']}"
    assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/") and rev["ipa"].count("/") == 2, f"IPA format invalid at {i} ({rev['hw']}): {rev['ipa']}"
    assert rev["pos"] in allowed_pos, f"POS invalid at {i} ({rev['hw']}): {rev['pos']}"
    records[i] = rev

batch_data["reviewedCount"] = 500
batch_data["status"] = "in-progress"

with open(batch_path, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print("Successfully verified and merged Round 1 into batch-23.json (500/5000 reviewed)")
