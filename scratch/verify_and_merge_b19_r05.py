import json

from scratch.b19_r05_p1 import reviewed_p1
from scratch.b19_r05_p2 import reviewed_p2
from scratch.b19_r05_p3 import reviewed_p3
from scratch.b19_r05_p4 import reviewed_p4
from scratch.b19_r05_p5 import reviewed_p5

round_data = reviewed_p1 + reviewed_p2 + reviewed_p3 + reviewed_p4 + reviewed_p5
assert len(round_data) == 500, f"Expected 500 records, got {len(round_data)}"

batch_file = "content/english/qa-batches/batch-19.json"
with open(batch_file, "r", encoding="utf-8") as f:
    batch = json.load(f)

start_idx = 2000
for i, item in enumerate(round_data):
    idx = start_idx + i
    target = batch["records"][idx]
    assert target["id"] == item["id"], f"ID mismatch at {idx}: {target['id']} vs {item['id']}"
    assert target["hw"] == item["hw"], f"hw mismatch at {idx}: {target['hw']} vs {item['hw']}"
    
    target["pos"] = item["pos"]
    target["ipa"] = item["ipa"]
    target["vi"] = item["vi"]
    target["status"] = "reviewed"

batch["reviewedCount"] = 2500

with open(batch_file, "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print("Batch 19 Round 5 merged successfully! Reviewed count: 2500/5000")
