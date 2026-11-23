import json
import re
import sys

import b14_r02_p1 as m1
import b14_r02_p2 as m2
import b14_r02_p3 as m3
import b14_r02_p4 as m4
import b14_r02_p5 as m5

def get_records(m):
    return getattr(m, "records", getattr(m, "reviewed_records", None))

all_records = get_records(m1) + get_records(m2) + get_records(m3) + get_records(m4) + get_records(m5)
print(f"Total reviewed records loaded: {len(all_records)}")

if len(all_records) != 500:
    print(f"ERROR: Expected 500 records, got {len(all_records)}")
    sys.exit(1)

# Quality Gates
FORBIDDEN_PATTERNS = [
    r"Số nhiều của",
    r"Xem ",
    r"Dạng ",
    r"Viết tắt",
    r"Động từ chia",
    r"\bdạng\b",
    r"\bnhư\b"
]

VALID_POS = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}

errors = []
for i, rec in enumerate(all_records):
    idx = 65502 + i
    expected_id = f"lex.en.100k.{idx:06d}"
    if rec["id"] != expected_id:
        errors.append(f"Record {i}: ID mismatch. Expected {expected_id}, got {rec['id']}")

    hw = rec.get("hw", "")
    if not hw:
        errors.append(f"Record {i} ({rec['id']}): Empty headword")

    vi = rec.get("vi", "")
    if not vi:
        errors.append(f"Record {i} ({hw}): Empty vi")
    if len(vi) > 35:
        errors.append(f"Record {i} ({hw}): Length {len(vi)} > 35: '{vi}'")

    for pat in FORBIDDEN_PATTERNS:
        if re.search(pat, vi, re.IGNORECASE):
            errors.append(f"Record {i} ({hw}): forbidden pattern '{pat}' in vi: '{vi}'")

    if vi.endswith(".") and not vi.endswith("..."):
        errors.append(f"Record {i} ({hw}): vi ends with trailing dot: '{vi}'")

    ipa = rec.get("ipa", "")
    if not ipa:
        errors.append(f"Record {i} ({hw}): Empty IPA")
    elif not (ipa.startswith("/") and ipa.endswith("/")):
        errors.append(f"Record {i} ({hw}): IPA must start and end with slash: '{ipa}'")
    elif ipa.count("/") != 2:
        errors.append(f"Record {i} ({hw}): IPA must contain exactly 2 slashes: '{ipa}'")

    pos = rec.get("pos", "")
    if pos not in VALID_POS:
        errors.append(f"Record {i} ({hw}): Invalid pos '{pos}'")

    if rec.get("status") != "reviewed":
        errors.append(f"Record {i} ({hw}): Status must be 'reviewed', got '{rec.get('status')}'")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for e in errors[:25]:
        print(" -", e)
    if len(errors) > 25:
        print(f" ... and {len(errors) - 25} more.")
    sys.exit(1)

print("All 500 records passed 100% Quality Gate validation!")

# Merge into batch-14.json
BATCH_FILE = "content/english/qa-batches/batch-14.json"
with open(BATCH_FILE, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

for i in range(500):
    batch_data["records"][500 + i] = all_records[i]

batch_data["reviewedCount"] = 1000
if batch_data["reviewedCount"] == len(batch_data["records"]):
    batch_data["status"] = "completed"
else:
    batch_data["status"] = "pending"

with open(BATCH_FILE, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully merged 500 records into {BATCH_FILE}!")
print(f"Batch 14 reviewedCount is now {batch_data['reviewedCount']}/{len(batch_data['records'])}.")
