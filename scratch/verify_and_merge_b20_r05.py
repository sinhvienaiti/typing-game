import json
import re

batch_file = "content/english/qa-batches/batch-20.json"
with open(batch_file, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

# Load 5 parts
parts = []
for p in range(1, 6):
    fn = f"scratch/b20_r05_p{p}.json"
    with open(fn, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} has {len(data)} items"
        parts.extend(data)

assert len(parts) == 500, f"Expected 500 items, got {len(parts)}"

start_idx = 2000
end_idx = 2500

for i, new_item in enumerate(parts):
    curr_idx = start_idx + i
    orig_item = batch_data["records"][curr_idx]
    
    assert orig_item["id"] == new_item["id"], f"ID mismatch at {curr_idx}: {orig_item['id']} vs {new_item['id']}"
    assert orig_item["hw"] == new_item["hw"], f"HW mismatch at {curr_idx}: {orig_item['hw']} vs {new_item['hw']}"
    assert new_item["status"] == "reviewed", f"Status not reviewed at {curr_idx}"
    assert len(new_item["vi"]) <= 35, f"vi length > 35 at {curr_idx}: {new_item['vi']}"
    assert new_item["ipa"].startswith("/") and new_item["ipa"].endswith("/") and new_item["ipa"].count("/") == 2, f"Invalid IPA at {curr_idx}: {new_item['ipa']}"
    assert not re.search(r"(Số nhiều của|Xem|Dạng|Viết tắt|Động từ chia|%%)", new_item["vi"]), f"Crawler trash at {curr_idx}: {new_item['vi']}"

    # Replace
    batch_data["records"][curr_idx] = new_item

# Update metadata
batch_data["reviewedCount"] = end_idx
print(f"Batch 20 reviewedCount updated to {batch_data['reviewedCount']}/{batch_data['wordCount']}")

with open(batch_file, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully merged Round 5 into {batch_file}")
