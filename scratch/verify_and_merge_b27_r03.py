import json

parts = []
for p in range(1, 6):
    with open(f"scratch/b27_r03_p{p}.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} length {len(data)} != 100"
        parts.extend(data)

assert len(parts) == 500, f"Total records {len(parts)} != 500"

valid_pos = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"}

for i, word in enumerate(parts):
    expected_id = f"lex.en.200k.{31002 + i:06d}"
    assert word["id"] == expected_id, f"Index {i}: id {word['id']} != {expected_id}"
    assert word["pos"] in valid_pos, f"Index {i} ({word['hw']}): invalid pos {word['pos']}"
    if word["pos"] != "phrase":
        assert word["ipa"].startswith("/") and word["ipa"].endswith("/"), f"Index {i} ({word['hw']}): invalid ipa {word['ipa']}"
        assert word["ipa"].count("/") == 2, f"Index {i} ({word['hw']}): ipa slash count != 2: {word['ipa']}"
        assert "  " not in word["ipa"], f"Index {i} ({word['hw']}): double spaces in ipa: {word['ipa']}"
        assert not word["ipa"].startswith("/ ") and not word["ipa"].endswith(" /"), f"Index {i} ({word['hw']}): boundary space in ipa: {word['ipa']}"
    assert len(word["vi"]) <= 35, f"Index {i} ({word['hw']}): vi length {len(word['vi'])} > 35: '{word['vi']}'"
    assert word["status"] == "reviewed", f"Index {i} ({word['hw']}): status not reviewed"
    for forbidden in ["Số nhiều của", "Xem ", "Dạng ", "Viết tắt", "Động từ chia", "%%"]:
        assert forbidden not in word["vi"], f"Index {i} ({word['hw']}): forbidden crawler artifact '{forbidden}' in vi: '{word['vi']}'"

batch_file = "content/english/qa-batches/batch-27.json"
with open(batch_file, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

assert len(batch_data["records"]) == 5000, f"Batch 27 records count {len(batch_data['records'])} != 5000"

# Verify slice [1000:1500] IDs and HWs
for i in range(500):
    orig = batch_data["records"][1000 + i]
    new_w = parts[i]
    assert orig["id"] == new_w["id"], f"ID mismatch at {1000+i}: orig {orig['id']} vs new {new_w['id']}"
    assert orig["hw"].lower() == new_w["hw"].lower(), f"HW mismatch at {1000+i}: orig {orig['hw']} vs new {new_w['hw']}"

# Merge
batch_data["records"][1000:1500] = parts
batch_data["reviewedCount"] = 1500
batch_data["status"] = "in-progress"

with open(batch_file, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully merged Round 3 into {batch_file}, reviewedCount set to {batch_data['reviewedCount']}, status set to {batch_data['status']}.")
