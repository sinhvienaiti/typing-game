import json
import sys
from b13_r07_p1 import P1_RECORDS
from b13_r07_p2 import P2_RECORDS
from b13_r07_p3 import P3_RECORDS
from b13_r07_p4 import P4_RECORDS
from b13_r07_p5 import P5_RECORDS

all_r07 = P1_RECORDS + P2_RECORDS + P3_RECORDS + P4_RECORDS + P5_RECORDS
assert len(all_r07) == 500, f"Expected 500 records, got {len(all_r07)}"

ALLOWED_POS = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}
FORBIDDEN_CRAWLER_ARTIFACTS = ["số nhiều của", "xem ", "dạng trần thuật", "từ viết tắt", "từ sai chính tả", "ngôi thứ ba"]

errors = []
for idx, r in enumerate(all_r07):
    hw = r["hw"]
    pos = r["pos"]
    ipa = r["ipa"]
    vi = r["vi"]
    status = r["status"]
    
    if pos not in ALLOWED_POS:
        errors.append(f"[{idx}] {hw}: invalid pos '{pos}'")
    if not ipa.startswith("/") or not ipa.endswith("/") or ipa.count("/") != 2 or len(ipa) <= 2:
        errors.append(f"[{idx}] {hw}: invalid ipa '{ipa}'")
    if ipa.startswith("/ ") or ipa.endswith(" /"):
        errors.append(f"[{idx}] {hw}: leading/trailing space in ipa '{ipa}'")
    if not vi:
        errors.append(f"[{idx}] {hw}: empty vi")
    if len(vi) > 35:
        errors.append(f"[{idx}] {hw}: vi too long ({len(vi)} chars): '{vi}'")
    for artifact in FORBIDDEN_CRAWLER_ARTIFACTS:
        if artifact in vi.lower():
            errors.append(f"[{idx}] {hw}: crawler artifact '{artifact}' in vi: '{vi}'")
    if status != "reviewed":
        errors.append(f"[{idx}] {hw}: status not 'reviewed': '{status}'")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for err in errors[:20]:
        print("  -", err)
    sys.exit(1)

print("All 500 records in Round 7 passed quality assertions!")

# Load batch-13.json
batch_path = "content/english/qa-batches/batch-13.json"
with open(batch_path, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

records = batch_data["records"]
assert len(records) == 5000, f"Expected 5000 records in batch-13, found {len(records)}"

# Verify matching IDs and headwords in slice 3000:3500
for i in range(500):
    orig = records[3000 + i]
    new_r = all_r07[i]
    assert orig["id"] == new_r["id"], f"ID mismatch at {3000 + i}: {orig['id']} vs {new_r['id']}"
    assert orig["hw"] == new_r["hw"], f"HW mismatch at {3000 + i}: {orig['hw']} vs {new_r['hw']}"

# Replace slice
records[3000:3500] = all_r07
batch_data["reviewedCount"] = 3500

with open(batch_path, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print("Successfully merged Round 7 into batch-13.json! reviewedCount updated to 3500.")
