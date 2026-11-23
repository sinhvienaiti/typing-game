import json
import re
import sys

from b14_r09_p1 import records as P1_DATA
from b14_r09_p2 import records as P2_DATA
from b14_r09_p3 import P3_DATA
from b14_r09_p4 import P4_DATA
from b14_r09_p5 import P5_DATA

BATCH_FILE = "content/english/qa-batches/batch-14.json"
FORBIDDEN_CRAWLER = [
    "số nhiều của", "xem ", "dạng ", "viết tắt", "động từ chia", "như ", "thường số nhiều"
]

all_data = P1_DATA + P2_DATA + P3_DATA + P4_DATA + P5_DATA
print(f"Total reviewed records to verify: {len(all_data)}")

if len(all_data) != 500:
    print(f"ERROR: Expected 500 records, got {len(all_data)}")
    sys.exit(1)

with open(BATCH_FILE, "r", encoding="utf-8") as f:
    batch_json = json.load(f)

records = batch_json["records"]
slice_start = 4000
slice_end = 4500
raw_slice = records[slice_start:slice_end]

errors = []
for i, (rev, raw) in enumerate(zip(all_data, raw_slice)):
    rec_num = slice_start + i
    # ID check
    expected_id = f"lex.en.100k.{rec_num+65002:06d}"
    if rev["id"] != expected_id:
        errors.append(f"Row {rec_num} ({rev.get('hw')}): ID mismatch, expected {expected_id}, got {rev.get('id')}")
    if rev["id"] != raw["id"]:
        errors.append(f"Row {rec_num}: ID mismatch with raw, {rev['id']} vs {raw['id']}")
    if rev["hw"] != raw["hw"]:
        errors.append(f"Row {rec_num}: Headword mismatch, {rev['hw']} vs {raw['hw']}")

    # Vi length check
    vi = rev.get("vi", "")
    if not vi:
        errors.append(f"Row {rec_num} ({rev['hw']}): empty vi")
    if len(vi) > 35:
        errors.append(f"Row {rec_num} ({rev['hw']}): vi length {len(vi)} > 35 chars: '{vi}'")

    # Forbidden crawler patterns
    vi_lower = vi.lower()
    for pat in FORBIDDEN_CRAWLER:
        if pat in vi_lower:
            errors.append(f"Row {rec_num} ({rev['hw']}): vi contains crawler artifact '{pat}': '{vi}'")

    # IPA check
    ipa = rev.get("ipa", "")
    if not ipa:
        errors.append(f"Row {rec_num} ({rev['hw']}): empty ipa")
    elif not (ipa.startswith("/") and ipa.endswith("/")):
        errors.append(f"Row {rec_num} ({rev['hw']}): ipa not enclosed in slashes: '{ipa}'")
    elif ipa.count("/") != 2:
        errors.append(f"Row {rec_num} ({rev['hw']}): ipa must have exactly 2 slashes, got {ipa.count('/')}: '{ipa}'")
    elif ipa.startswith("/ ") or ipa.endswith(" /"):
        errors.append(f"Row {rec_num} ({rev['hw']}): ipa has boundary space: '{ipa}'")

    # POS check
    valid_pos = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num"}
    if rev.get("pos") not in valid_pos:
        errors.append(f"Row {rec_num} ({rev['hw']}): invalid pos '{rev.get('pos')}'")

    # Status check
    if rev.get("status") != "reviewed":
        errors.append(f"Row {rec_num} ({rev['hw']}): status is not 'reviewed'")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for e in errors[:30]:
        print("  -", e)
    if len(errors) > 30:
        print(f"  ... and {len(errors)-30} more errors.")
    sys.exit(1)

print("All 500 records passed validation perfectly!")

# Perform merge
for i, rev in enumerate(all_data):
    records[slice_start + i] = rev

batch_json["reviewedCount"] = 4500

with open(BATCH_FILE, "w", encoding="utf-8") as f:
    json.dump(batch_json, f, ensure_ascii=False, indent=2)

print(f"Successfully merged 500 records into {BATCH_FILE}. reviewedCount is now 4500.")
