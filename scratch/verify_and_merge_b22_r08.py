import json
import sys

ALLOWED_POS = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"}
FORBIDDEN_VI = ["Số nhiều của", "Xem ", "Dạng ", "Viết tắt", "Động từ chia", "%%"]

all_reviewed = []
for p in range(1, 6):
    file_path = f"scratch/b22_r08_p{p}.json"
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} has {len(data)} items, expected 100"
        all_reviewed.extend(data)

print(f"Loaded {len(all_reviewed)} reviewed records for Round 8.")

errors = []
for i, r in enumerate(all_reviewed):
    hw = r.get("hw", "")
    vi = r.get("vi", "")
    pos = r.get("pos", "")
    ipa = r.get("ipa", "")
    status = r.get("status", "")

    if status != "reviewed":
        errors.append(f"Item {i} ({hw}): status is '{status}', expected 'reviewed'")
    if not vi:
        errors.append(f"Item {i} ({hw}): vi is empty")
    elif len(vi) > 35:
        errors.append(f"Item {i} ({hw}): vi length {len(vi)} > 35: '{vi}'")
    for fb in FORBIDDEN_VI:
        if fb in vi:
            errors.append(f"Item {i} ({hw}): vi contains forbidden pattern '{fb}': '{vi}'")
    if pos not in ALLOWED_POS:
        errors.append(f"Item {i} ({hw}): pos '{pos}' not in ALLOWED_POS")
    if not (ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2 and len(ipa) > 2):
        errors.append(f"Item {i} ({hw}): invalid ipa format '{ipa}'")
    if ipa.startswith("/ ") or ipa.endswith(" /"):
        errors.append(f"Item {i} ({hw}): ipa has boundary space: '{ipa}'")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for err in errors[:20]:
        print("  -", err)
    sys.exit(1)

print("Validation passed successfully!")

# Merge into batch-22.json
batch_path = "content/english/qa-batches/batch-22.json"
with open(batch_path, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

records = batch_data["records"]
start_idx = 3500
end_idx = 4000

for i, rev in enumerate(all_reviewed):
    orig = records[start_idx + i]
    if orig["id"] != rev["id"]:
        raise ValueError(f"ID mismatch at {start_idx + i}: orig {orig['id']} vs rev {rev['id']}")
    if orig["hw"] != rev["hw"]:
        raise ValueError(f"HW mismatch at {start_idx + i}: orig {orig['hw']} vs rev {rev['hw']}")
    records[start_idx + i] = rev

batch_data["reviewedCount"] = 4000
with open(batch_path, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully merged Round 8 (records {start_idx} to {end_idx - 1}). Reviewed count updated to {batch_data['reviewedCount']}.")
