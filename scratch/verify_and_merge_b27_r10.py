import json
import re

ALLOWED_POS = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"}
BANNED_CRAWLER = ["Số nhiều của", "Xem ", "Dạng ", "Viết tắt của", "Động từ chia", "%%"]
VULGAR = ["cứt", "địt", "lồn", "buồi", "cặc", "chịch"]

all_reviewed = []
for p in range(1, 6):
    path = f"scratch/b27_r10_p{p}.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 100, f"{path} has {len(data)} items, expected 100"
        all_reviewed.extend(data)

assert len(all_reviewed) == 500, f"Total items {len(all_reviewed)} != 500"

# Verify all items
for idx, item in enumerate(all_reviewed):
    exp_id = f"lex.en.200k.{34502+idx:06d}"
    assert item["id"] == exp_id, f"ID error at {idx}: {item['id']} vs {exp_id}"
    assert item["pos"] in ALLOWED_POS, f"Invalid POS {item['pos']} at {item['hw']}"
    assert len(item["vi"]) <= 35, f"vi too long ({len(item['vi'])}): {item['vi']} at {item['hw']}"
    assert len(item["vi"].strip()) > 0, f"vi empty at {item['hw']}"
    for b in BANNED_CRAWLER:
        assert b not in item["vi"], f"Crawler artifact '{b}' in {item['hw']}: {item['vi']}"
    for v in VULGAR:
        assert v not in item["vi"], f"Vulgar word '{v}' in {item['hw']}: {item['vi']}"
    assert item["status"] == "reviewed", f"Status must be reviewed at {item['hw']}"
    
    if " " in item["hw"]:
        assert item["pos"] == "phrase", f"Phrase pos expected for {item['hw']}"
    else:
        assert item["ipa"].startswith("/") and item["ipa"].endswith("/"), f"IPA slashes missing at {item['hw']}: {item['ipa']}"
        assert item["ipa"].count("/") == 2, f"IPA count of / != 2 at {item['hw']}: {item['ipa']}"
        assert not item["ipa"].startswith("/ ") and not item["ipa"].endswith(" /"), f"Boundary space in IPA at {item['hw']}: {item['ipa']}"

# Load batch-27.json
batch_path = "content/english/qa-batches/batch-27.json"
with open(batch_path, "r", encoding="utf-8") as f:
    batch = json.load(f)

assert len(batch["records"]) == 5000, f"Batch 27 length != 5000, got {len(batch['records'])}"

# Verify slice [4500:5000] matches IDs and hw
for i in range(500):
    batch_item = batch["records"][4500 + i]
    rev_item = all_reviewed[i]
    assert batch_item["id"] == rev_item["id"], f"Batch ID mismatch at {4500+i}: {batch_item['id']} vs {rev_item['id']}"
    assert batch_item["hw"] == rev_item["hw"], f"Batch HW mismatch at {4500+i}: {batch_item['hw']} vs {rev_item['hw']}"

# Replace slice [4500:5000]
batch["records"][4500:5000] = all_reviewed
batch["reviewedCount"] = 5000
batch["status"] = "completed"

# Check all 5000 records in batch-27 are reviewed
for r in batch["records"]:
    assert r["status"] == "reviewed", f"Unreviewed record found: {r['id']} {r['hw']}"

with open(batch_path, "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print("Batch 27 slice [4500:5000] successfully verified and merged. Batch 27 is 100% completed!")

# Update INDEX.md line for batch 27
index_path = "content/english/qa-batches/INDEX.md"
with open(index_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

found = False
for i, line in enumerate(lines):
    if "| 27 |" in line:
        lines[i] = "| 27 | batch-27.json | 5000 | ✅ completed (5000/5000) | `lex.en.200k.030002` - `lex.en.200k.035001` |\n"
        found = True
        break

assert found, "Could not find batch 27 in INDEX.md"
with open(index_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("INDEX.md successfully updated for batch 27 (✅ completed (5000/5000)).")
