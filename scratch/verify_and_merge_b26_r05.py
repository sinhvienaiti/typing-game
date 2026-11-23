import json

parts = []
for p in range(1, 6):
    with open(f"scratch/b26_r05_p{p}.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} has {len(data)} items"
        parts.extend(data)

assert len(parts) == 500, f"Expected 500 items, got {len(parts)}"

allowed_pos = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"}

for i, item in enumerate(parts):
    # Schema check
    expected_keys = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']
    assert list(item.keys()) == expected_keys, f"Item {i} invalid keys: {list(item.keys())}"
    assert item["status"] == "reviewed", f"Item {i} status not reviewed: {item['status']}"
    assert item["pos"] in allowed_pos, f"Item {i} invalid pos: {item['pos']}"
    assert 0 < len(item["vi"]) <= 35, f"Item {i} vi length invalid: {len(item['vi'])} - {item['vi']}"
    if item["pos"] != "phrase":
        assert item["ipa"].startswith("/") and item["ipa"].endswith("/") and item["ipa"].count("/") == 2, f"Item {i} invalid IPA: {item['ipa']}"
        assert "  " not in item["ipa"], f"Item {i} double spaces in IPA"
        assert not item["ipa"].startswith("/ ") and not item["ipa"].endswith(" /"), f"Item {i} boundary space in IPA"

# Load batch-26.json
with open("content/english/qa-batches/batch-26.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

# Verify IDs
for idx, (b_item, p_item) in enumerate(zip(batch["records"][2000:2500], parts)):
    assert b_item["id"] == p_item["id"], f"ID mismatch at index {2000+idx}: batch {b_item['id']} vs part {p_item['id']}"
    assert b_item["hw"] == p_item["hw"], f"HW mismatch at index {2000+idx}: batch {b_item['hw']} vs part {p_item['hw']}"

# Merge
batch["records"][2000:2500] = parts
batch["reviewedCount"] = 2500
batch["status"] = "in-progress"

with open("content/english/qa-batches/batch-26.json", "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print("Batch 26 Round 5 successfully merged (2500/5000 reviewed)")
