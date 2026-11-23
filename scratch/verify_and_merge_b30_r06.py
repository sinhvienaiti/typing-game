import json

ALLOWED_POS = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
EXPECTED_KEYS = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

# 1. Load the 5 parts
all_round_items = []
for p in range(1, 6):
    with open(f"scratch/b30_r06_p{p}.json", "r", encoding="utf-8") as f:
        part_data = json.load(f)
        assert len(part_data) == 100, f"Part {p} length is {len(part_data)}, expected 100"
        all_round_items.extend(part_data)

assert len(all_round_items) == 500, f"Expected 500 items, got {len(all_round_items)}"

# 2. Load batch-30.json
batch_path = "content/english/qa-batches/batch-30.json"
with open(batch_path, "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]
assert len(records) == 5000, f"Expected 5000 records, got {len(records)}"

# Check slice [2500:3000]
target_slice = records[2500:3000]
assert len(target_slice) == 500, f"Expected 500 records in slice, got {len(target_slice)}"

for idx, (orig, rev) in enumerate(zip(target_slice, all_round_items)):
    assert orig["id"] == rev["id"], f"ID mismatch at {idx}: orig {orig['id']} vs rev {rev['id']}"
    assert orig["hw"] == rev["hw"], f"HW mismatch at {idx}: orig {orig['hw']} vs rev {rev['hw']}"
    assert list(rev.keys()) == EXPECTED_KEYS, f"Keys mismatch at {idx} ({rev['hw']}): {list(rev.keys())}"
    assert rev["pos"] in ALLOWED_POS, f"Invalid pos '{rev['pos']}' at {idx} ({rev['hw']})"
    assert len(rev["vi"]) <= 35, f"Vietnamese too long at {idx} ({rev['hw']}): '{rev['vi']}' ({len(rev['vi'])} chars)"
    assert rev["status"] == "reviewed", f"Status not reviewed at {idx} ({rev['hw']})"
    if rev["pos"] != "phrase":
        assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/"), f"Invalid IPA at {idx} ({rev['hw']}): {rev['ipa']}"
        assert rev["ipa"].count("/") == 2, f"IPA slashes != 2 at {idx} ({rev['hw']}): {rev['ipa']}"

# Apply slice replacement
records[2500:3000] = all_round_items
batch["records"] = records
batch["reviewedCount"] = 3000
batch["status"] = "in-progress"

with open(batch_path, "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print("Batch 30 Round 6 (2500-2999) successfully verified and merged! reviewedCount = 3000.")
