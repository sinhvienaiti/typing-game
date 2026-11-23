# verify_and_merge_b16_r10.py
import json
from b16_r10_p1 import part1
from b16_r10_p2 import part2
from b16_r10_p3 import part3
from b16_r10_p4 import part4
from b16_r10_p5 import part5

all_r10 = part1 + part2 + part3 + part4 + part5
assert len(all_r10) == 500, f"Expected 500 items, got {len(all_r10)}"

# Validate all items
for idx, r in enumerate(all_r10):
    assert len(r["vi"]) <= 35, f"vi length > 35 at index {idx} ({r['hw']}): {len(r['vi'])} - {r['vi']}"
    assert r["ipa"].startswith("/") and r["ipa"].endswith("/") and r["ipa"].count("/") == 2, f"Invalid IPA at index {idx} ({r['hw']}): {r['ipa']}"
    assert r["status"] == "reviewed"
    assert r["pos"] in ["noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "num", "det"], f"Invalid pos: {r['pos']} in {r['hw']}"

batch_file = "content/english/qa-batches/batch-16.json"
with open(batch_file, "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]
assert len(records) == 5000, f"Expected 5000 records, got {len(records)}"

# Check ID alignment
for i, rev in enumerate(all_r10):
    rec_idx = 4500 + i
    orig = records[rec_idx]
    assert orig["id"] == rev["id"], f"ID mismatch at {rec_idx}: orig {orig['id']} vs rev {rev['id']}"
    assert orig["hw"].lower() == rev["hw"].lower(), f"HW mismatch at {rec_idx}: orig {orig['hw']} vs rev {rev['hw']}"
    
    # Preserve cefr, tier, notes
    rev["cefr"] = orig["cefr"]
    rev["tier"] = orig["tier"]
    rev["notes"] = orig.get("notes", "")
    
    # Apply
    records[rec_idx] = rev

batch["records"] = records
batch["reviewedCount"] = 5000

with open(batch_file, "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"Successfully merged 500 records into {batch_file}! Reviewed count: {batch['reviewedCount']}/5000")
