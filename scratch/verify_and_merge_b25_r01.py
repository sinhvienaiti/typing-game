import json

batch_file = "content/english/qa-batches/batch-25.json"
parts_files = [f"scratch/b25_r1_p{i}.json" for i in range(1, 6)]

with open(batch_file, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

items = batch_data["records"]

reviewed_items = []
for pf in parts_files:
    with open(pf, "r", encoding="utf-8") as f:
        p_data = json.load(f)
        assert len(p_data) == 100, f"{pf} does not have 100 items, got {len(p_data)}"
        reviewed_items.extend(p_data)

assert len(reviewed_items) == 500, f"Expected 500 items, got {len(reviewed_items)}"

valid_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}

errors = []
for i in range(500):
    orig = items[i]
    rev = reviewed_items[i]
    if orig["id"] != rev["id"]:
        errors.append(f"ID mismatch at {i}: orig {orig['id']} vs rev {rev['id']}")
    if orig["hw"] != rev["hw"]:
        errors.append(f"HW mismatch at {i}: orig {orig['hw']} vs rev {rev['hw']}")
    if len(rev["vi"]) > 35:
        errors.append(f"VI too long at {i} ({rev['id']} - {rev['hw']}): {rev['vi']} (len {len(rev['vi'])})")
    if rev["pos"] not in valid_pos:
        errors.append(f"Invalid POS at {i} ({rev['id']}): {rev['pos']}")
    if not (rev["ipa"].startswith("/") and rev["ipa"].endswith("/") and rev["ipa"].count("/") == 2):
        errors.append(f"Invalid IPA at {i} ({rev['id']}): {rev['ipa']}")
    if rev["status"] != "reviewed":
        errors.append(f"Status not reviewed at {i} ({rev['id']}): {rev['status']}")

if errors:
    print(f"FAILED: {len(errors)} validation errors:")
    for err in errors[:20]:
        print(" -", err)
    exit(1)

# Merge
for i in range(500):
    items[i] = reviewed_items[i]

batch_data["reviewedCount"] = 500

with open(batch_file, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print("SUCCESS: Merged Batch 25 Round 1 (500 items) into batch-25.json!")
