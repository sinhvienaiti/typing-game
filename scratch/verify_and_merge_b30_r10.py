import json

# Verify and merge Round 10 of Batch 30 (records 4500 to 4999)
parts = []
for p in range(1, 6):
    with open(f"scratch/b30_r10_p{p}.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} has {len(data)} items, expected 100"
        parts.extend(data)

assert len(parts) == 500, f"Total items {len(parts)}, expected 500"

ALLOWED_POS = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}
SCHEMA_KEYS = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

for item in parts:
    assert list(item.keys()) == SCHEMA_KEYS, f"Keys mismatch: {item}"
    assert len(item["vi"]) <= 35, f"vi too long: {item['hw']} ({len(item['vi'])}): {item['vi']}"
    assert item["pos"] in ALLOWED_POS, f"Invalid pos: {item['hw']} -> {item['pos']}"
    assert item["status"] == "reviewed", f"Invalid status: {item['hw']} -> {item['status']}"
    if item["pos"] != "phrase" or item["ipa"]:
        assert item["ipa"].startswith("/") and item["ipa"].endswith("/"), f"IPA slashes error: {item['hw']} -> {item['ipa']}"
        assert item["ipa"].count("/") == 2, f"IPA slash count error: {item['hw']} -> {item['ipa']}"

with open("content/english/qa-batches/batch-30.json", "r", encoding="utf-8") as f:
    b30 = json.load(f)

records = b30["records"]
assert len(records) == 5000, f"Batch 30 records count {len(records)} != 5000"

for idx, item in enumerate(parts):
    r_idx = 4500 + idx
    target = records[r_idx]
    assert target["id"] == item["id"], f"ID mismatch at {r_idx}: target {target['id']} != item {item['id']}"
    records[r_idx] = item

b30["reviewedCount"] = 5000
b30["status"] = "completed"

# Check all 5000 records in batch-30
for i, r in enumerate(records):
    assert r["status"] == "reviewed", f"Record {i} not reviewed: {r['id']}"

with open("content/english/qa-batches/batch-30.json", "w", encoding="utf-8") as f:
    json.dump(b30, f, ensure_ascii=False, indent=2)

print(f"Successfully merged Round 10 into batch-30.json! Status: {b30['status']}, Reviewed count: {b30['reviewedCount']}/5000")
