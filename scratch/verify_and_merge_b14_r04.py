import json
import re
import sys

from b14_r04_p1 import reviewed_records as p1
from b14_r04_p2 import reviewed_records as p2
from b14_r04_p3 import reviewed_records as p3
from b14_r04_p4 import reviewed_records as p4
from b14_r04_p5 import reviewed_records as p5

all_r04 = p1 + p2 + p3 + p4 + p5

print(f"Total entries in R04: {len(all_r04)}")
assert len(all_r04) == 500, f"Expected 500 entries, got {len(all_r04)}"

batch_path = "content/english/qa-batches/batch-14.json"
with open(batch_path, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

items = batch_data["records"]
start_idx = 1500
end_idx = 2000

errors = []
forbidden_patterns = [
    r"Số nhiều của",
    r"Xem ",
    r"Dạng ",
    r"Viết tắt",
    r"Động từ chia",
    r"\bdạng\b",
    r"\bnhư\b",
    r"\bthường số nhiều\b"
]

valid_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}

for i, entry in enumerate(all_r04):
    idx = start_idx + i
    orig = items[idx]
    
    # check id match
    if entry["id"] != orig["id"]:
        errors.append(f"Index {idx}: ID mismatch {entry['id']} != {orig['id']}")
    if entry["hw"] != orig["hw"]:
        errors.append(f"Index {idx}: HW mismatch {entry['hw']} != {orig['hw']}")
    
    # check vi length
    vi = entry.get("vi", "")
    if len(vi) > 35:
        errors.append(f"Entry {entry['id']} ({entry['hw']}): vi length {len(vi)} > 35: '{vi}'")
    if not vi:
        errors.append(f"Entry {entry['id']} ({entry['hw']}): vi is empty")
    if vi.endswith(".") and not vi.endswith("..."):
        errors.append(f"Entry {entry['id']} ({entry['hw']}): vi ends with trailing dot: '{vi}'")
        
    for pat in forbidden_patterns:
        if re.search(pat, vi, re.IGNORECASE):
            errors.append(f"Entry {entry['id']} ({entry['hw']}): vi matched forbidden pattern '{pat}': '{vi}'")
            
    # check IPA
    ipa = entry.get("ipa", "")
    if not (ipa.startswith("/") and ipa.endswith("/") and len(ipa) > 2 and ipa.count("/") == 2):
        errors.append(f"Entry {entry['id']} ({entry['hw']}): invalid IPA '{ipa}'")
    elif ipa.startswith("/ ") or ipa.endswith(" /"):
        errors.append(f"Entry {entry['id']} ({entry['hw']}): IPA has leading/trailing space inside slashes '{ipa}'")
        
    # check POS
    pos = entry.get("pos", "")
    if pos not in valid_pos:
        errors.append(f"Entry {entry['id']} ({entry['hw']}): invalid POS '{pos}'")
        
    # check status
    if entry.get("status") != "reviewed":
        errors.append(f"Entry {entry['id']} ({entry['hw']}): status != reviewed")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for err in errors[:25]:
        print("  -", err)
    if len(errors) > 25:
        print(f"  ... and {len(errors) - 25} more errors")
    sys.exit(1)

print("Validation PASSED for all 500 entries!")

# Merge into batch-14
for i, entry in enumerate(all_r04):
    idx = start_idx + i
    items[idx] = entry

batch_data["reviewedCount"] = 2000
if batch_data["reviewedCount"] == len(batch_data["records"]):
    batch_data["status"] = "completed"
else:
    batch_data["status"] = "pending"

with open(batch_path, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print("Successfully merged Round 4 into batch-14.json! Reviewed count: 2000/5000")
