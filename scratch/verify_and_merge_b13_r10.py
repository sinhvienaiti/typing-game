import json
import sys
import re

from b13_r10_p1 import P1_RECORDS
from b13_r10_p2 import P2_RECORDS
from b13_r10_p3 import P3_RECORDS
from b13_r10_p4 import P4_RECORDS
from b13_r10_p5 import P5_RECORDS

all_records = P1_RECORDS + P2_RECORDS + P3_RECORDS + P4_RECORDS + P5_RECORDS
print(f"Total reviewed records: {len(all_records)}")
assert len(all_records) == 500, f"Expected 500 records, got {len(all_records)}"

# Check IDs continuity: 064502 to 065001
start_id = 64502
end_id = 65001
for i, r in enumerate(all_records):
    expected_id = f"lex.en.100k.{start_id + i:06d}"
    assert r["id"] == expected_id, f"Record {i} has id {r['id']}, expected {expected_id}"

# Quality validation
VALID_POS = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}
FORBIDDEN = ["Số nhiều của", "Xem ", "Dạng ", "Viết tắt của", "Động từ chia", "dạng "]

errors = []
for r in all_records:
    # 1. vi length <= 35
    if len(r["vi"]) > 35:
        errors.append(f"[{r['id']}] {r['hw']}: vi length {len(r['vi'])} > 35 ('{r['vi']}')")
    
    # 2. forbidden crawler patterns
    for f in FORBIDDEN:
        if f.lower() in r["vi"].lower():
            errors.append(f"[{r['id']}] {r['hw']}: vi contains forbidden pattern '{f}' ('{r['vi']}')")
            
    # 3. pos valid
    if r["pos"] not in VALID_POS:
        errors.append(f"[{r['id']}] {r['hw']}: invalid pos '{r['pos']}'")
        
    # 4. ipa valid
    if not (r["ipa"].startswith("/") and r["ipa"].endswith("/") and r["ipa"].count("/") == 2 and len(r["ipa"]) >= 3):
        errors.append(f"[{r['id']}] {r['hw']}: invalid ipa '{r['ipa']}'")
    if r["ipa"].startswith("/ ") or r["ipa"].endswith(" /"):
        errors.append(f"[{r['id']}] {r['hw']}: boundary space in ipa '{r['ipa']}'")
        
    # 5. status reviewed
    if r["status"] != "reviewed":
        errors.append(f"[{r['id']}] {r['hw']}: status is '{r['status']}', expected 'reviewed'")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for e in errors[:25]:
        print("  ", e)
    sys.exit(1)
else:
    print("All 500 records passed quality validation successfully!")

# Load batch-13.json
batch_path = "content/english/qa-batches/batch-13.json"
with open(batch_path, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

# Verify slice
slice_records = batch_data["records"][4500:5000]
assert len(slice_records) == 500

for i, (orig, rev) in enumerate(zip(slice_records, all_records)):
    assert orig["id"] == rev["id"], f"Mismatch at index {i}: orig {orig['id']} vs rev {rev['id']}"
    assert orig["hw"] == rev["hw"], f"Mismatch headword at {orig['id']}: orig {orig['hw']} vs rev {rev['hw']}"
    # preserve cefr, tier, notes
    assert orig["cefr"] == rev["cefr"]
    assert orig["tier"] == rev["tier"]

# Merge into batch_data
batch_data["records"][4500:5000] = all_records
batch_data["reviewedCount"] = 5000
batch_data["status"] = "completed"

with open(batch_path, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"Merged Round 10 into batch-13.json. New reviewedCount = {batch_data['reviewedCount']}, status = {batch_data['status']}")
