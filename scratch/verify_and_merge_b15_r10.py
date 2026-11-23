import json
import re
import sys
import os

sys.path.insert(0, os.getcwd())

from scratch.b15_r10_p1 import PART_DATA as p1
from scratch.b15_r10_p2 import PART_DATA as p2
from scratch.b15_r10_p3 import PART_DATA as p3
from scratch.b15_r10_p4 import PART_DATA as p4
from scratch.b15_r10_p5 import PART_DATA as p5

all_r10 = p1 + p2 + p3 + p4 + p5
assert len(all_r10) == 500, f"Expected 500 items, got {len(all_r10)}"

batch_file = "content/english/qa-batches/batch-15.json"
with open(batch_file, "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]
start_idx = 4500
end_idx = 5000

prohibited = [
    "số nhiều của", "viết tắt của", "viết tắt từ", "động từ chia",
    "dạng số nhiều", "dạng quá khứ", "dạng phân từ", "dạng thay thế của",
    "dạng biến thể của", "thường số nhiều", "quá khứ của"
]

valid_pos = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "num", "det"}

for i, reviewed in enumerate(all_r10):
    idx = start_idx + i
    original = records[idx]

    assert reviewed["id"] == original["id"], f"ID mismatch at {idx}: {reviewed['id']} vs {original['id']}"
    assert reviewed["hw"] == original["hw"], f"HW mismatch at {idx}: {reviewed['hw']} vs {original['hw']}"

    vi = reviewed["vi"]
    assert len(vi) <= 35, f"vi length exceeds 35 at {idx} ({reviewed['hw']}): len={len(vi)} -> {vi}"

    vi_lower = vi.lower()
    for p in prohibited:
        assert p not in vi_lower, f"Prohibited phrase '{p}' at {idx} ({reviewed['hw']}): {vi}"
    assert not vi_lower.startswith("xem "), f"Leading 'xem ' at {idx} ({reviewed['hw']}): {vi}"

    assert reviewed["pos"] in valid_pos, f"Invalid POS '{reviewed['pos']}' at {idx} ({reviewed['hw']})"

    ipa = reviewed["ipa"]
    assert ipa.startswith("/") and ipa.endswith("/"), f"Invalid IPA slashes at {idx} ({reviewed['hw']}): {ipa}"
    assert ipa.count("/") == 2, f"IPA does not have exactly 2 slashes at {idx} ({reviewed['hw']}): {ipa}"
    assert not ipa.startswith("/ ") and not ipa.endswith(" /"), f"Boundary space in IPA at {idx} ({reviewed['hw']}): {ipa}"

    assert reviewed["status"] == "reviewed", f"Status not reviewed at {idx} ({reviewed['hw']})"

    # Preserve original schema attributes
    reviewed["cefr"] = original["cefr"]
    reviewed["tier"] = original["tier"]
    reviewed["notes"] = original["notes"]

    # Assign merged record
    records[idx] = reviewed

batch["reviewedCount"] = 5000

with open(batch_file, "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print("Batch 15 Round 10 (records 4500-4999, IDs 074502-075001) verified and merged successfully!")
print(f"Total reviewed count updated to: {batch['reviewedCount']}/5000 -> BATCH 15 100% COMPLETED!")
