import json
import sys

# Load parts
sys.path.insert(0, "scratch")
from b16_r01_p1 import PART_DATA as p1
from b16_r01_p2 import data as p2
from b16_r01_p3 import data as p3
from b16_r01_p4 import data as p4
from b16_r01_p5 import data as p5

reviewed_500 = p1 + p2 + p3 + p4 + p5
assert len(reviewed_500) == 500, f"Expected 500 records, got {len(reviewed_500)}"

# Load target batch
batch_path = "content/english/qa-batches/batch-16.json"
with open(batch_path, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

records = batch_data["records"]
assert len(records) == 5000, f"Expected 5000 records in batch-16, got {len(records)}"

# Strict quality checks & merging
for idx, new_entry in enumerate(reviewed_500):
    orig = records[idx]
    assert new_entry["id"] == orig["id"], f"ID mismatch at {idx}: {new_entry['id']} vs {orig['id']}"
    assert new_entry["hw"] == orig["hw"], f"HW mismatch at {idx}: {new_entry['hw']} vs {orig['hw']}"
    
    # Check vi length
    vi = new_entry["vi"]
    assert len(vi) <= 35, f"vi too long at {idx} ({new_entry['hw']}): {len(vi)} chars: {vi}"
    
    # Check ipa
    ipa = new_entry["ipa"]
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Invalid IPA at {idx} ({new_entry['hw']}): {ipa}"
    
    # Check status
    assert new_entry["status"] == "reviewed", f"Status not reviewed at {idx}: {new_entry['status']}"
    
    # Preserve original metadata
    new_entry["cefr"] = orig.get("cefr", "C2")
    new_entry["tier"] = orig.get("tier", "expanded")
    new_entry["notes"] = orig.get("notes", "")

    # Replace in records
    records[idx] = new_entry

# Update reviewedCount
batch_data["reviewedCount"] = 500

with open(batch_path, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print("Batch 16 Round 1 merged successfully into batch-16.json! reviewedCount set to 500.")
