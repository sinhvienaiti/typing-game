import json
import re
import sys

from scratch.b15_r05_p1 import PART_DATA as p1
from scratch.b15_r05_p2 import PART_DATA as p2
from scratch.b15_r05_p3 import PART_DATA as p3
from scratch.b15_r05_p4 import PART_DATA as p4
from scratch.b15_r05_p5 import PART_DATA as p5

all_r05 = p1 + p2 + p3 + p4 + p5
assert len(all_r05) == 500, f"Expected 500 items, got {len(all_r05)}"

batch_file = "content/english/qa-batches/batch-15.json"
with open(batch_file, "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]
start_idx = 2000
end_idx = 2500

prohibited = [
    "số nhiều của", "viết tắt của", "viết tắt từ", "động từ chia",
    "dạng số nhiều", "dạng quá khứ", "dạng phân từ", "dạng thay thế của",
    "dạng biến thể của", "thường số nhiều", "quá khứ của"
]

for i, reviewed in enumerate(all_r05):
    idx = start_idx + i
    original = records[idx]
    
    assert reviewed["id"] == original["id"], f"ID mismatch at {idx}: {reviewed['id']} vs {original['id']}"
    assert reviewed["hw"] == original["hw"], f"HW mismatch at {idx}: {reviewed['hw']} vs {original['hw']}"
    
    vi = reviewed["vi"]
    hw = reviewed["hw"]
    rid = reviewed["id"]
    
    assert len(vi) <= 35, f"Length > 35 at {idx} ({hw}): len={len(vi)} '{vi}'"
    assert len(vi) > 0, f"Empty vi at {idx} ({hw})"
    assert not vi.lower().startswith("xem "), f"Crawler artifact 'xem' at {idx} ({hw}): '{vi}'"
    
    for p in prohibited:
        assert p.lower() not in vi.lower(), f"Prohibited phrase '{p}' found at {idx} ({hw}): '{vi}'"
        
    ipa = reviewed["ipa"]
    assert ipa.startswith("/") and ipa.endswith("/"), f"Malformed IPA at {idx} ({hw}): '{ipa}'"
    assert ipa.count("/") == 2, f"Slash count != 2 at {idx} ({hw}): '{ipa}'"
    assert not ipa.startswith("/ ") and not ipa.endswith(" /"), f"Boundary spaces in IPA at {idx} ({hw}): '{ipa}'"
    
    assert reviewed["status"] == "reviewed", f"Status not reviewed at {idx} ({hw})"
    
    # Merge
    records[idx] = reviewed

batch["reviewedCount"] = 2500

with open(batch_file, "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print(f"Successfully verified and merged Round 5 (records {start_idx} to {end_idx - 1}) into {batch_file}")
