import json
import re

batch_path = "content/english/qa-batches/batch-29.json"
with open(batch_path, "r", encoding="utf-8") as f:
    batch = json.load(f)

print(f"Current reviewedCount: {batch['reviewedCount']}")
assert batch['reviewedCount'] == 2000, f"Expected reviewedCount 2000, got {batch['reviewedCount']}"

all_new = []
for p in range(1, 6):
    part_path = f"scratch/b29_r05_p{p}.json"
    with open(part_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} length is {len(data)}, expected 100"
        all_new.extend(data)

assert len(all_new) == 500, f"Total new records length is {len(all_new)}, expected 500"

# Verify slice [2000:2500] in batch
for i in range(500):
    idx = 2000 + i
    orig = batch['records'][idx]
    new = all_new[i]
    assert orig['id'] == new['id'], f"ID mismatch at {idx}: orig {orig['id']} vs new {new['id']}"
    assert orig['hw'] == new['hw'], f"HW mismatch at {idx}: orig {orig['hw']} vs new {new['hw']}"
    assert new['status'] == 'reviewed'
    assert len(new['vi']) > 0 and len(new['vi']) <= 35, f"Invalid VI length at {idx}: {new['vi']}"
    if new['pos'] != 'phrase' and ' ' not in new['hw']:
        assert new['ipa'].startswith('/') and new['ipa'].endswith('/') and new['ipa'].count('/') == 2, f"Invalid IPA at {idx}: {new['ipa']}"

# Apply updates
for i in range(500):
    idx = 2000 + i
    batch['records'][idx] = all_new[i]

batch['reviewedCount'] = 2500
batch['status'] = 'in-progress'

with open(batch_path, "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print(f"Batch 29 Round 5 merged successfully. New reviewedCount: {batch['reviewedCount']}")
