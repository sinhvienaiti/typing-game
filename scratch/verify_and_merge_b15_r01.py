import json
import re
import sys

ALLOWED_POS = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}
FORBIDDEN_VI_PATTERNS = [
    r"Số nhiều của",
    r"Xem\b",
    r"Dạng\b",
    r"Viết tắt\b",
    r"Động từ chia\b",
    r"\bdạng\b",
    r"\bnhư\b",
    r"\bthường số nhiều\b"
]

import b15_r01_p1
import b15_r01_p2
import b15_r01_p3
import b15_r01_p4
import b15_r01_p5

merged_data = {}
for p in [b15_r01_p1, b15_r01_p2, b15_r01_p3, b15_r01_p4, b15_r01_p5]:
    for attr in ["P1_DATA", "P2_DATA", "P3_DATA", "P4_DATA", "P5_DATA", "DATA"]:
        if hasattr(p, attr):
            val = getattr(p, attr)
            if isinstance(val, dict):
                merged_data.update(val)
            elif isinstance(val, list):
                for item in val:
                    merged_data[item["id"]] = item

print(f"Total reviewed entries in B15 R01: {len(merged_data)}")
if len(merged_data) != 500:
    print(f"ERROR: Expected 500 entries, got {len(merged_data)}")
    sys.exit(1)

# Load batch-15.json
with open("content/english/qa-batches/batch-15.json", "r", encoding="utf-8") as f:
    batch_json = json.load(f)

items = batch_json["records"]
print(f"Batch 15 total items: {len(items)}")

# Round 1 covers indices 0 to 499 (IDs 070002 to 070501)
errors = []
for i in range(0, 500):
    item = items[i]
    item_id = item["id"]
    if item_id not in merged_data:
        errors.append(f"Missing item {item_id} at index {i}")
        continue
    
    rev = merged_data[item_id]
    
    # Check hw match
    if item["hw"] != rev["hw"]:
        errors.append(f"HW mismatch for {item_id}: batch has {item['hw']}, rev has {rev['hw']}")
        
    # Check vi length
    vi = rev["vi"]
    if not vi:
        errors.append(f"Empty vi for {item_id}")
    elif len(vi) > 35:
        errors.append(f"vi length > 35 ({len(vi)}) for {item_id} ({rev['hw']}): {vi}")
        
    # Check forbidden patterns
    for pat in FORBIDDEN_VI_PATTERNS:
        if re.search(pat, vi, re.IGNORECASE):
            errors.append(f"Forbidden pattern '{pat}' in {item_id} ({rev['hw']}): {vi}")
            
    # Check pos
    pos = rev["pos"]
    if pos not in ALLOWED_POS:
        errors.append(f"Invalid pos '{pos}' in {item_id} ({rev['hw']})")
        
    # Check ipa
    ipa = rev["ipa"]
    if not ipa or not (ipa.startswith("/") and ipa.endswith("/")) or ipa.count("/") != 2 or ipa.startswith("/ ") or ipa.endswith(" /"):
        errors.append(f"Invalid ipa '{ipa}' in {item_id} ({rev['hw']})")
        
    # Check status
    if rev["status"] != "reviewed":
        errors.append(f"Invalid status '{rev['status']}' in {item_id}")

if errors:
    print(f"Found {len(errors)} errors:")
    for e in errors[:25]:
        print("  -", e)
    sys.exit(1)

print("All 500 records passed validation! Updating batch-15.json...")

for i in range(0, 500):
    item = items[i]
    item_id = item["id"]
    rev = merged_data[item_id]
    item["pos"] = rev["pos"]
    item["ipa"] = rev["ipa"]
    item["vi"] = rev["vi"]
    item["status"] = rev["status"]
    if "notes" in rev:
        item["notes"] = rev["notes"]

batch_json["reviewedCount"] = 500
batch_json["status"] = "pending"

with open("content/english/qa-batches/batch-15.json", "w", encoding="utf-8") as f:
    json.dump(batch_json, f, ensure_ascii=False, indent=2)

print("Successfully merged Batch 15 Round 1 into batch-15.json!")
