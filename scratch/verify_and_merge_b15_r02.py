import json
import re
import sys

from b15_r02_p1 import data as p1
from b15_r02_p2 import data as p2
from b15_r02_p3 import data as p3
from b15_r02_p4 import data as p4
from b15_r02_p5 import data as p5

all_data = p1 + p2 + p3 + p4 + p5
print(f"Total entries to merge: {len(all_data)}")
assert len(all_data) == 500, f"Expected 500, got {len(all_data)}"

# Quality checks
allowed_pos = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num"}
forbidden_patterns = [
    r"Số nhiều của", r"Xem\s", r"Dạng\s", r"Viết tắt", r"Động từ chia",
    r"\bnhư\b", r"\bdạng\b"
]

errors = []
for i, item in enumerate(all_data):
    w_id = item["id"]
    hw = item["hw"]
    vi = item["vi"]
    pos = item["pos"]
    ipa = item["ipa"]
    
    # 1. Length check
    if len(vi) > 35:
        errors.append(f"[{w_id}] '{hw}' vi exceeds 35 chars ({len(vi)}): '{vi}'")
    
    # 2. Forbidden patterns
    for pat in forbidden_patterns:
        if re.search(pat, vi, re.IGNORECASE):
            errors.append(f"[{w_id}] '{hw}' vi matches forbidden '{pat}': '{vi}'")
            
    # 3. IPA slashes
    if not (ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2 and len(ipa) > 2):
        errors.append(f"[{w_id}] '{hw}' invalid IPA: '{ipa}'")
    if ipa.startswith("/ ") or ipa.endswith(" /"):
        errors.append(f"[{w_id}] '{hw}' IPA has boundary spaces: '{ipa}'")
        
    # 4. POS check
    if pos not in allowed_pos:
        errors.append(f"[{w_id}] '{hw}' invalid POS: '{pos}'")

if errors:
    print(f"FAILED with {len(errors)} errors:")
    for e in errors[:30]:
        print("  -", e)
    if len(errors) > 30:
        print(f"  ... and {len(errors) - 30} more.")
    sys.exit(1)

print("All quality checks PASSED!")

# Merge into batch-15.json
batch_path = "content/english/qa-batches/batch-15.json"
with open(batch_path, "r", encoding="utf-8") as f:
    batch = json.load(f)

# Verify range 500 to 999
for idx, reviewed in enumerate(all_data):
    batch_idx = 500 + idx
    original = batch["records"][batch_idx]
    if original["id"] != reviewed["id"]:
        raise ValueError(f"ID mismatch at index {batch_idx}: {original['id']} vs {reviewed['id']}")
    if original["hw"] != reviewed["hw"]:
        raise ValueError(f"HW mismatch at index {batch_idx}: {original['hw']} vs {reviewed['hw']}")
    
    # Update fields while preserving schema
    original["pos"] = reviewed["pos"]
    original["ipa"] = reviewed["ipa"]
    original["vi"] = reviewed["vi"]
    original["cefr"] = reviewed["cefr"]
    original["tier"] = reviewed["tier"]
    original["status"] = "reviewed"
    original["notes"] = reviewed.get("notes", "")

batch["reviewedCount"] = 1000

with open(batch_path, "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"Successfully merged 500 items (indices 500..999) into {batch_path}!")
