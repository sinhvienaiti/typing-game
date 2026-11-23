import json
import re
import sys
import importlib

FORBIDDEN_REGEX = re.compile(r"^(Số nhiều của|Xem|Dạng|Viết tắt|Động từ chia|thường số nhiều)\b|\b(như|dạng)\b", re.IGNORECASE)
VALID_POS = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}

parts = ["b14_r08_p1", "b14_r08_p2", "b14_r08_p3", "b14_r08_p4", "b14_r08_p5"]

all_records = []
for p in parts:
    mod = importlib.import_module(p)
    recs = getattr(mod, "records", None) or getattr(mod, "updates", None)
    if isinstance(recs, dict):
        all_records.extend(recs.values())
    elif isinstance(recs, list):
        all_records.extend(recs)
    else:
        print(f"Error: {p} has neither records nor updates")
        sys.exit(1)

print(f"Total records collected: {len(all_records)}")
assert len(all_records) == 500, f"Expected 500 records, got {len(all_records)}"

errors = []
id_map = {}

for idx, r in enumerate(all_records):
    rec_id = r["id"]
    hw = r["hw"]
    pos = r["pos"]
    ipa = r["ipa"]
    vi = r["vi"]
    status = r["status"]
    
    id_map[rec_id] = r
    
    if len(vi) > 35:
        errors.append(f"[{rec_id}] ({hw}) vi length {len(vi)} > 35: '{vi}'")
        
    m = FORBIDDEN_REGEX.search(vi)
    if m:
        errors.append(f"[{rec_id}] ({hw}) forbidden pattern '{m.group(0)}' in vi: '{vi}'")
        
    if not ipa.startswith("/") or not ipa.endswith("/") or ipa.count("/") != 2 or len(ipa) <= 2:
        errors.append(f"[{rec_id}] ({hw}) invalid ipa: '{ipa}'")
        
    if pos not in VALID_POS:
        errors.append(f"[{rec_id}] ({hw}) invalid pos: '{pos}'")
        
    if status != "reviewed":
        errors.append(f"[{rec_id}] ({hw}) status not reviewed: '{status}'")

if errors:
    print(f"Found {len(errors)} validation errors:")
    for e in errors:
        print("  - " + e)
    sys.exit(1)

print("All 500 records validated successfully!")

# Merge into batch-14.json
batch_path = "content/english/qa-batches/batch-14.json"
with open(batch_path, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

# Find records in batch-14
recs = batch_data.get("records") or batch_data.get("items")
updated_count = 0

for item in recs:
    item_id = item["id"]
    if item_id in id_map:
        new_data = id_map[item_id]
        item["pos"] = new_data["pos"]
        item["ipa"] = new_data["ipa"]
        item["vi"] = new_data["vi"]
        item["status"] = "reviewed"
        updated_count += 1

print(f"Updated {updated_count} records in batch-14.json")
assert updated_count == 500, f"Expected 500 updates, got {updated_count}"

# Recalculate reviewedCount
total_reviewed = sum(1 for item in recs if item.get("status") == "reviewed")
batch_data["reviewedCount"] = total_reviewed
print(f"Batch-14 total reviewed count: {total_reviewed}/5000")

with open(batch_path, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print("batch-14.json successfully saved!")
