# -*- coding: utf-8 -*-
import json

# Load all 5 parts
all_parts = []
for p in range(1, 6):
    with open(f'scratch/b31_r10_p{p}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} len is {len(data)}"
        all_parts.extend(data)

assert len(all_parts) == 500, f"Total items is {len(all_parts)}"

# Check batch-31.json
with open('content/english/qa-batches/batch-31.json', 'r', encoding='utf-8') as f:
    batch = json.load(f)

records = batch['records']
assert len(records) == 5000, f"Batch 31 records len is {len(records)}"

# Check slices 4500 to 5000
for i, (new_rec, old_rec) in enumerate(zip(all_parts, records[4500:5000])):
    assert new_rec['id'] == old_rec['id'], f"ID mismatch at {i}: {new_rec['id']} vs {old_rec['id']}"
    assert new_rec['hw'] == old_rec['hw'], f"HW mismatch at {i}: {new_rec['hw']} vs {old_rec['hw']}"

# Replace records 4500 to 5000
records[4500:5000] = all_parts

# Update metadata
batch['reviewedCount'] = 5000
batch['status'] = 'completed'

with open('content/english/qa-batches/batch-31.json', 'w', encoding='utf-8') as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print("Batch 31 Round 10 successfully merged! Batch 31 is now COMPLETED (5000/5000)!")
