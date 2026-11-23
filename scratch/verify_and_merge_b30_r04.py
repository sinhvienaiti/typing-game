import json
from datetime import datetime, timezone

# 1. Load parts
p1 = json.load(open("scratch/b30_r04_p1.json", encoding="utf-8"))
p2 = json.load(open("scratch/b30_r04_p2.json", encoding="utf-8"))
p3 = json.load(open("scratch/b30_r04_p3.json", encoding="utf-8"))
p4 = json.load(open("scratch/b30_r04_p4.json", encoding="utf-8"))
p5 = json.load(open("scratch/b30_r04_p5.json", encoding="utf-8"))

r04_items = p1 + p2 + p3 + p4 + p5
assert len(r04_items) == 500, f"Expected 500 items, got {len(r04_items)}"

# 2. Load batch-30
b30_path = "content/english/qa-batches/batch-30.json"
b30 = json.load(open(b30_path, encoding="utf-8"))
assert len(b30["records"]) == 5000, f"Expected 5000 items in batch-30, got {len(b30['records'])}"

# 3. Check ID alignment for [1500:2000]
for idx, (orig, rev) in enumerate(zip(b30["records"][1500:2000], r04_items)):
    assert orig["id"] == rev["id"], f"ID mismatch at {idx}: {orig['id']} vs {rev['id']}"
    assert orig["hw"] == rev["hw"], f"HW mismatch at {idx}: {orig['hw']} vs {rev['hw']}"

# 4. Replace items
b30["records"][1500:2000] = r04_items
b30["reviewedCount"] = 2000
b30["status"] = "in-progress"
b30["updatedAt"] = datetime.now(timezone.utc).isoformat()

# 5. Full validation of reviewed records [0:2000]
allowed_pos = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"}
for i in range(2000):
    item = b30["records"][i]
    assert item["status"] == "reviewed", f"Item {i} ({item['id']}) status not reviewed"
    assert len(item["vi"]) <= 35, f"Item {i} ({item['id']}) VI > 35: {item['vi']}"
    assert item["pos"] in allowed_pos, f"Item {i} ({item['id']}) invalid pos: {item['pos']}"
    if item["pos"] != "phrase":
        assert item["ipa"].startswith("/") and item["ipa"].endswith("/") and item["ipa"].count("/") == 2, f"Item {i} ({item['id']}) invalid IPA: {item['ipa']}"

with open(b30_path, "w", encoding="utf-8") as f:
    json.dump(b30, f, ensure_ascii=False, indent=2)

print("Batch 30 Round 4 merged successfully! Reviewed count: 2000 / 5000")
