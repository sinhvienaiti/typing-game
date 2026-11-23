import json

batch_file = "content/english/qa-batches/batch-23.json"
with open(batch_file, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

records = batch_data["records"]
assert len(records) == 5000, f"Expected 5000 records, got {len(records)}"

# Load all 5 parts of round 2
p1 = json.load(open("scratch/b23_r02_p1.json"))
p2 = json.load(open("scratch/b23_r02_p2.json"))
p3 = json.load(open("scratch/b23_r02_p3.json"))
p4 = json.load(open("scratch/b23_r02_p4.json"))
p5 = json.load(open("scratch/b23_r02_p5.json"))

assert len(p1) == 100
assert len(p2) == 100
assert len(p3) == 100
assert len(p4) == 100
assert len(p5) == 100

r02_items = p1 + p2 + p3 + p4 + p5
assert len(r02_items) == 500

allowed_pos = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"}

for idx, item in enumerate(r02_items):
    rec_idx = 500 + idx
    orig = records[rec_idx]
    assert orig["id"] == item["id"], f"ID mismatch at {rec_idx}: {orig['id']} vs {item['id']}"
    assert orig["hw"] == item["hw"], f"HW mismatch at {rec_idx}: {orig['hw']} vs {item['hw']}"
    assert item["status"] == "reviewed", f"Status not reviewed at {rec_idx}"
    assert len(item["vi"]) <= 35, f"Vi too long at {rec_idx}: {item['vi']} ({len(item['vi'])})"
    assert len(item["vi"]) > 0, f"Vi empty at {rec_idx}"
    assert item["pos"] in allowed_pos, f"Invalid pos at {rec_idx}: {item['pos']}"
    ipa = item["ipa"]
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Invalid ipa at {rec_idx}: {ipa}"
    assert not ipa.startswith("/ ") and not ipa.endswith(" /"), f"Boundary space in ipa at {rec_idx}: {ipa}"
    
    # Merge
    records[rec_idx] = item

batch_data["reviewedCount"] = 1000

with open(batch_file, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print("Batch 23 Round 2 merged successfully! Reviewed count: 1000/5000")
