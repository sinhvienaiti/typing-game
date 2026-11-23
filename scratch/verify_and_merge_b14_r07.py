import json
import re
import sys

# Load parts
import b14_r07_p1
import b14_r07_p2
import b14_r07_p3
import b14_r07_p4
import b14_r07_p5

combined_updates = {}
for p in [b14_r07_p1, b14_r07_p2, b14_r07_p3, b14_r07_p4, b14_r07_p5]:
    if hasattr(p, "updates"):
        combined_updates.update(p.updates)
    elif hasattr(p, "records"):
        for rec in p.records:
            combined_updates[rec["id"]] = {
                "pos": rec["pos"],
                "ipa": rec["ipa"],
                "vi": rec["vi"]
            }

print(f"Total entries to review in Round 7: {len(combined_updates)}")
assert len(combined_updates) == 500, f"Expected 500 entries, got {len(combined_updates)}"

expected_ids = [f"lex.en.100k.{i:06d}" for i in range(68002, 68502)]
assert list(combined_updates.keys()) == expected_ids, "IDs do not match expected range 068002 - 068501"

forbidden_patterns = [
    r"Số nhiều của",
    r"\bXem\b",
    r"\bDạng\b",
    r"\bViết tắt\b",
    r"\bĐộng từ chia\b",
    r"\bdạng\b",
    r"\bnhư\b",
    r"thường số nhiều",
]

errors = []
valid_pos = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "num", "det"}

batch_path = "content/english/qa-batches/batch-14.json"
with open(batch_path, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

items = batch_data["records"]
start_idx = 3000
end_idx = 3500

for i in range(500):
    idx = start_idx + i
    orig = items[idx]
    w_id = orig["id"]
    if w_id not in combined_updates:
        errors.append(f"Missing update for {w_id} at index {idx}")
        continue
    
    update = combined_updates[w_id]
    vi = update.get("vi", "")
    ipa = update.get("ipa", "")
    pos = update.get("pos", "")
    
    # Check vi length
    if len(vi) > 35:
        errors.append(f"[{w_id}] vi too long ({len(vi)} chars): '{vi}'")
    if not vi:
        errors.append(f"[{w_id}] vi is empty")
    
    # Check forbidden patterns
    for pat in forbidden_patterns:
        if re.search(pat, vi, re.IGNORECASE):
            errors.append(f"[{w_id}] vi matches forbidden pattern '{pat}': '{vi}'")
            
    # Check IPA
    if not ipa.startswith("/") or not ipa.endswith("/"):
        errors.append(f"[{w_id}] ipa missing slashes: '{ipa}'")
    if ipa.count("/") != 2:
        errors.append(f"[{w_id}] ipa slashes count != 2: '{ipa}'")
    if len(ipa) <= 2:
        errors.append(f"[{w_id}] ipa empty between slashes: '{ipa}'")
    if ipa.startswith("/ ") or ipa.endswith(" /"):
        errors.append(f"[{w_id}] ipa contains boundary space: '{ipa}'")
        
    # Check POS
    if pos not in valid_pos:
        errors.append(f"[{w_id}] pos invalid: '{pos}'")

if errors:
    print(f"FAILED validation with {len(errors)} errors:")
    for err in errors:
        print("  -", err)
    sys.exit(1)

print("Validation PASSED! Merging into batch-14.json...")

for i in range(500):
    idx = start_idx + i
    orig = items[idx]
    w_id = orig["id"]
    update = combined_updates[w_id]
    orig["vi"] = update["vi"]
    orig["ipa"] = update["ipa"]
    orig["pos"] = update["pos"]
    orig["status"] = "reviewed"

batch_data["reviewedCount"] = 3500
if batch_data["reviewedCount"] == len(batch_data["records"]):
    batch_data["status"] = "completed"
else:
    batch_data["status"] = "pending"

with open(batch_path, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully merged 500 records into {batch_path}. New reviewedCount: {batch_data['reviewedCount']}")
