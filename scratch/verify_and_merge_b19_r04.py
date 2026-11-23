import json

from b19_r04_p1 import reviewed_p1
from b19_r04_p2 import reviewed_p2
from b19_r04_p3 import reviewed_p3
from b19_r04_p4 import reviewed_p4
from b19_r04_p5 import reviewed_p5

all_reviewed = reviewed_p1 + reviewed_p2 + reviewed_p3 + reviewed_p4 + reviewed_p5
assert len(all_reviewed) == 500, f"Expected 500 reviewed items, got {len(all_reviewed)}"

batch_path = "content/english/qa-batches/batch-19.json"
with open(batch_path, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

records = batch_data["records"]
start_idx = 1500
end_idx = 2000

for i, rev in enumerate(all_reviewed):
    rec_idx = start_idx + i
    raw = records[rec_idx]
    assert raw["id"] == rev["id"], f"ID mismatch at {rec_idx}: batch {raw['id']} vs rev {rev['id']}"
    assert raw["hw"] == rev["hw"], f"HW mismatch at {rec_idx}: batch {raw['hw']} vs rev {rev['hw']}"
    
    # Update fields
    raw["pos"] = rev["pos"]
    raw["ipa"] = rev["ipa"]
    raw["vi"] = rev["vi"]
    raw["status"] = "reviewed"

# Recount reviewed
reviewed_count = sum(1 for r in records if r.get("status") == "reviewed")
assert reviewed_count == 2000, f"Expected 2000 reviewed records, got {reviewed_count}"
batch_data["reviewedCount"] = reviewed_count

with open(batch_path, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"Batch 19 Round 4 merged successfully! reviewedCount: {reviewed_count}/5000")
