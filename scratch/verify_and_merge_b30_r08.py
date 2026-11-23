import json

parts = []
for p in range(1, 6):
    with open(f"scratch/b30_r08_p{p}.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} has {len(data)} items"
        parts.extend(data)

assert len(parts) == 500, f"Expected 500 items, got {len(parts)}"

with open("content/english/qa-batches/batch-30.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]
assert len(records) == 5000, f"Expected 5000 records in batch-30, got {len(records)}"

# Verify matching IDs
for i in range(500):
    expected_id = records[3500 + i]["id"]
    part_id = parts[i]["id"]
    assert expected_id == part_id, f"ID mismatch at index {3500+i}: expected {expected_id}, got {part_id}"

# Validate quality gates
for item in parts:
    assert len(item["vi"]) <= 35, f"vi too long: {item['hw']} -> {len(item['vi'])}: {item['vi']}"
    assert item["status"] == "reviewed", f"Status not reviewed: {item['hw']}"
    ipa = item["ipa"]
    if item["pos"] != "phrase" or ipa != "":
        assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Invalid IPA: {item['hw']} -> {ipa}"
        assert not ipa.startswith("/ ") and not ipa.endswith(" /"), f"Boundary space in IPA: {ipa}"

# Merge into records
for i in range(500):
    records[3500 + i] = parts[i]

batch["records"] = records
batch["reviewedCount"] = 4000
batch["status"] = "in-progress"

with open("content/english/qa-batches/batch-30.json", "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print("Batch 30 Round 8 successfully verified and merged! reviewedCount = 4000")
