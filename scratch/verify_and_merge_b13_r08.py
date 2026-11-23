import json
import sys

from b13_r08_p1 import P1_RECORDS
from b13_r08_p2 import P2_RECORDS
from b13_r08_p3 import P3_RECORDS
from b13_r08_p4 import P4_RECORDS
from b13_r08_p5 import P5_RECORDS

all_reviewed = P1_RECORDS + P2_RECORDS + P3_RECORDS + P4_RECORDS + P5_RECORDS

print(f"Total reviewed records: {len(all_reviewed)}")
assert len(all_reviewed) == 500, f"Expected 500 records, got {len(all_reviewed)}"

# Load batch-13.json
batch_path = "content/english/qa-batches/batch-13.json"
with open(batch_path, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

raw_slice = batch_data["records"][3500:4000]
assert len(raw_slice) == 500, f"Raw slice length is {len(raw_slice)}"

VALID_POS = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}

FORBIDDEN_PATTERNS = [
    "xem ", "số nhiều của", "dạng ", "từ viết tắt", "viết tắt của", 
    "chương trình", "động từ chia", "ngôi thứ ba"
]

errors = []

for idx, (rev, raw) in enumerate(zip(all_reviewed, raw_slice)):
    # Check ID match
    if rev["id"] != raw["id"]:
        errors.append(f"Record {idx}: ID mismatch: {rev['id']} vs {raw['id']}")
    
    # Check HW match
    if rev["hw"] != raw["hw"]:
        errors.append(f"Record {idx}: HW mismatch: {rev['hw']} vs {raw['hw']}")
        
    # Check Status
    if rev["status"] != "reviewed":
        errors.append(f"Record {idx} ({rev['hw']}): status is {rev['status']}")
        
    # Check POS
    if rev["pos"] not in VALID_POS:
        errors.append(f"Record {idx} ({rev['hw']}): invalid pos {rev['pos']}")
        
    # Check IPA
    ipa = rev["ipa"]
    if not (ipa.startswith("/") and ipa.endswith("/") and len(ipa) >= 3 and ipa.count("/") == 2):
        errors.append(f"Record {idx} ({rev['hw']}): invalid ipa format: {ipa}")
    elif ipa.startswith("/ ") or ipa.endswith(" /"):
        errors.append(f"Record {idx} ({rev['hw']}): ipa has internal boundary spaces: {ipa}")
        
    # Check VI
    vi = rev["vi"]
    if not vi or not isinstance(vi, str):
        errors.append(f"Record {idx} ({rev['hw']}): vi is empty or not string")
    else:
        if len(vi) > 35:
            errors.append(f"Record {idx} ({rev['hw']}): vi length {len(vi)} > 35: '{vi}'")
        vi_lower = vi.lower()
        for pat in FORBIDDEN_PATTERNS:
            if pat in vi_lower:
                errors.append(f"Record {idx} ({rev['hw']}): forbidden pattern '{pat}' in vi: '{vi}'")

    # Check schema preservation
    for key in ["cefr", "tier", "notes"]:
        if key not in rev:
            errors.append(f"Record {idx} ({rev['hw']}): missing key '{key}'")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for err in errors[:20]:
        print("  -", err)
    if len(errors) > 20:
        print(f"  ... and {len(errors) - 20} more errors")
    sys.exit(1)

print("All 500 records passed validation successfully!")

# Merge into batch-13.json
batch_data["records"][3500:4000] = all_reviewed
batch_data["reviewedCount"] = 4000

with open(batch_path, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print("Successfully merged into batch-13.json with reviewedCount = 4000!")
