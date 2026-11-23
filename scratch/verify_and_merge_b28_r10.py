import json

# 1. Load 5 parts
all_round = []
for p in range(1, 6):
    with open(f"scratch/b28_r10_p{p}.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} length is {len(data)}, expected 100"
        all_round.extend(data)

assert len(all_round) == 500, f"Total round items is {len(all_round)}, expected 500"

# 2. Strict validation
expected_start = 39502
for i, item in enumerate(all_round):
    expected_id = f"lex.en.200k.{expected_start + i:06d}"
    assert item["id"] == expected_id, f"ID mismatch at index {i}: expected {expected_id}, got {item['id']}"
    assert item["status"] == "reviewed", f"Status not reviewed for {item['id']}"
    vi = item["vi"]
    assert len(vi) > 0 and len(vi) <= 35, f"Invalid VI length ({len(vi)}) at {item['id']}: {vi}"
    assert not any(bad in vi for bad in ["Số nhiều của", "Xem ", "Dạng ", "Viết tắt của", "Động từ chia", "%%"]), f"Crawler garbage in {item['id']}: {vi}"
    hw = item["hw"]
    ipa = item["ipa"]
    if " " not in hw:
        assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Invalid IPA at {item['id']}: '{ipa}'"
        assert not ipa.startswith("/ ") and not ipa.endswith(" /"), f"Boundary space in IPA at {item['id']}: '{ipa}'"
    else:
        if ipa:
            assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Invalid phrase IPA at {item['id']}: '{ipa}'"

# 3. Load batch-28.json
with open("content/english/qa-batches/batch-28.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

items = batch["records"]
assert len(items) == 5000, f"Batch 28 items length is {len(items)}, expected 5000"

# Check IDs match slice [4500:5000]
for idx, (b_item, r_item) in enumerate(zip(items[4500:5000], all_round)):
    assert b_item["id"] == r_item["id"], f"Batch item ID {b_item['id']} != Round item ID {r_item['id']} at {4500 + idx}"
    assert b_item["hw"] == r_item["hw"], f"HW mismatch at {4500 + idx}: {b_item['hw']} vs {r_item['hw']}"
    items[4500 + idx] = r_item

batch["records"] = items
batch["reviewedCount"] = 5000
batch["status"] = "completed"

with open("content/english/qa-batches/batch-28.json", "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print("Batch 28 Round 10 verified and merged successfully! Batch 28 is now COMPLETED (5000/5000)!")
