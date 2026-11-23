import json
import re

allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
prohibited_patterns = [
    r"^Số nhiều của",
    r"^Xem\s+",
    r"^Viết tắt của",
    r"%%.*%%",
    r"^Động từ chia",
]

parts = []
for p in range(1, 6):
    with open(f"scratch/b28_r02_p{p}.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} does not have 100 items"
        parts.extend(data)

assert len(parts) == 500, f"Total items is {len(parts)}, expected 500"

expected_keys = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

for i, item in enumerate(parts):
    expected_id = f"lex.en.200k.{35502+i:06d}"
    assert item["id"] == expected_id, f"ID mismatch at {i}: {item['id']} vs {expected_id}"
    assert list(item.keys()) == expected_keys, f"Keys mismatch at {item['id']}: {list(item.keys())}"
    assert item["status"] == "reviewed", f"Status not reviewed at {item['id']}"
    assert item["pos"] in allowed_pos, f"Invalid POS at {item['id']}: {item['pos']}"
    assert 0 < len(item["vi"]) <= 35, f"Invalid VI length ({len(item['vi'])}) at {item['id']}: {item['vi']}"
    
    for pat in prohibited_patterns:
        assert not re.search(pat, item["vi"], re.IGNORECASE), f"Prohibited pattern {pat} in {item['vi']} at {item['id']}"
    
    if item["pos"] != "phrase":
        ipa = item["ipa"]
        assert ipa.startswith("/") and ipa.endswith("/"), f"IPA slashes missing at {item['hw']}: {ipa}"
        assert ipa.count("/") == 2, f"IPA count of / != 2 at {item['hw']}: {ipa}"
        assert not ipa.startswith("/ ") and not ipa.endswith(" /"), f"IPA spaces at boundary in {item['hw']}: {ipa}"

with open("content/english/qa-batches/batch-28.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

assert len(batch["records"]) == 5000, f"Batch 28 records count is {len(batch['records'])}"

# Merge slice 500:1000
batch["records"][500:1000] = parts
batch["reviewedCount"] = 1000
batch["status"] = "in-progress"

with open("content/english/qa-batches/batch-28.json", "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print("Batch 28 Round 2 verified and merged successfully into batch-28.json!")
