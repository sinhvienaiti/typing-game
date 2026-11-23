import json

# Load parts
all_round_items = []
for p in range(1, 6):
    with open(f"scratch/b30_r02_p{p}.json") as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} has {len(data)} items, expected 100"
        all_round_items.extend(data)

assert len(all_round_items) == 500, f"Expected 500 items, got {len(all_round_items)}"

# Load target batch
batch_file = "content/english/qa-batches/batch-30.json"
with open(batch_file) as f:
    batch = json.load(f)

records = batch["records"]
assert len(records) == 5000, f"Expected 5000 records in batch, got {len(records)}"

# Verify matching slice [500:1000]
target_slice = records[500:1000]
for idx, (target, reviewed) in enumerate(zip(target_slice, all_round_items)):
    assert target["id"] == reviewed["id"], f"ID mismatch at {idx}: target {target['id']} vs reviewed {reviewed['id']}"
    assert target["hw"].lower() == reviewed["hw"].lower(), f"HW mismatch at {idx}: target {target['hw']} vs reviewed {reviewed['hw']}"
    assert len(reviewed["vi"]) <= 35, f"VI too long at {idx}: {reviewed['vi']}"
    assert reviewed["pos"] in ["noun", "verb", "adj", "adv", "phrase", "intj", "prep", "conj", "pron", "det", "num"]
    assert reviewed["ipa"] == "" or (reviewed["ipa"].startswith("/") and reviewed["ipa"].endswith("/")), f"Invalid IPA at {idx}: {reviewed['ipa']}"
    assert reviewed["status"] == "reviewed"

# Apply merge
records[500:1000] = all_round_items
batch["reviewedCount"] = 1000
batch["status"] = "in-progress"

with open(batch_file, "w") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print("Batch 30 Round 2 merged successfully! Total reviewed in batch: 1000/5000")
