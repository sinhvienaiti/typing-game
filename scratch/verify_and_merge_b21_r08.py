import json
import re

ALLOWED_POS = {"noun", "verb", "adj", "adv", "phrase", "intj", "prep", "conj", "pron", "det", "num"}

# 1. Load all 5 parts
all_round_items = []
for p in range(1, 6):
    path = f"scratch/b21_r08_p{p}.json"
    with open(path) as f:
        items = json.load(f)
        assert len(items) == 100, f"Part {p} has {len(items)} items"
        all_round_items.extend(items)

assert len(all_round_items) == 500, f"Total round items: {len(all_round_items)}"

# 2. Quality gate checks
for idx, item in enumerate(all_round_items):
    assert len(item["vi"]) <= 35, f"vi too long at {idx}: {item['hw']} -> {item['vi']} ({len(item['vi'])})"
    assert len(item["vi"]) > 0, f"empty vi at {idx}"
    assert not re.search(r"^(số nhiều của|xem\s+[a-zA-Z]|dạng\s+|viết tắt|động từ chia|%%)", item["vi"], re.IGNORECASE), f"crawler artifact found at {idx}: {item['vi']}"
    assert item["pos"] in ALLOWED_POS, f"invalid pos at {idx}: {item['pos']}"
    assert item["ipa"].startswith("/") and item["ipa"].endswith("/") and item["ipa"].count("/") == 2, f"invalid ipa at {idx}: {item['ipa']}"
    assert item["status"] == "reviewed"

# 3. Load batch-21.json
with open("content/english/qa-batches/batch-21.json") as f:
    batch_data = json.load(f)

records = batch_data["records"]
assert len(records) == 5000

# 4. Check alignment with batch records 3500..3999
start_idx = 3500
for i in range(500):
    b_idx = start_idx + i
    orig = records[b_idx]
    rev = all_round_items[i]
    assert orig["id"] == rev["id"], f"ID mismatch at {b_idx}: {orig['id']} vs {rev['id']}"
    assert orig["hw"] == rev["hw"], f"HW mismatch at {b_idx}: {orig['hw']} vs {rev['hw']}"
    # Replace
    records[b_idx] = rev

# Count reviewed
reviewed_count = sum(1 for r in records if r.get("status") == "reviewed")
print(f"Total reviewed in batch-21: {reviewed_count}/5000")
assert reviewed_count == 4000, f"Expected 4000 reviewed, got {reviewed_count}"

batch_data["reviewedCount"] = reviewed_count

with open("content/english/qa-batches/batch-21.json", "w") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print("Batch 21 Round 8 merged successfully!")
