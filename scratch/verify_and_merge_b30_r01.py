import json
from datetime import datetime, timezone

parts = []
for p in range(1, 6):
    with open(f"scratch/b30_r01_p{p}.json") as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} has {len(data)} items, expected 100"
        parts.extend(data)

assert len(parts) == 500, f"Total items {len(parts)}, expected 500"

# Schema validation
valid_pos = {"noun", "verb", "adj", "adv", "phrase", "intj", "prep", "conj", "pron", "det", "num"}
banned_vi_markers = ["Số nhiều của", "Xem ", "Dạng ", "Viết tắt của", "Động từ chia", "%%"]

for idx, item in enumerate(parts):
    assert item["status"] == "reviewed", f"Item {idx} status != reviewed"
    vi = item["vi"]
    assert len(vi) <= 35, f"Item {idx} ({item['hw']}) VI too long ({len(vi)}): {vi}"
    for m in banned_vi_markers:
        assert m not in vi, f"Item {idx} has banned marker '{m}': {vi}"
    assert item["pos"] in valid_pos, f"Item {idx} invalid pos: {item['pos']}"
    ipa = item["ipa"]
    if ipa != "":
        assert ipa.startswith("/") and ipa.endswith("/"), f"Item {idx} invalid IPA format: {ipa}"
        assert ipa.count("/") == 2, f"Item {idx} IPA does not have exactly 2 slashes: {ipa}"

# Load batch-30.json
with open("content/english/qa-batches/batch-30.json") as f:
    batch = json.load(f)

# Verify ID alignment
for i in range(500):
    expected_id = batch["records"][0 + i]["id"]
    actual_id = parts[i]["id"]
    assert expected_id == actual_id, f"ID mismatch at {i}: expected {expected_id}, got {actual_id}"
    batch["records"][0 + i] = parts[i]

batch["reviewedCount"] = 500
batch["status"] = "in-progress"
batch["updatedAt"] = datetime.now(timezone.utc).isoformat()

with open("content/english/qa-batches/batch-30.json", "w") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print("Batch 30 Round 1 merged successfully! (500/5000 reviewed)")
