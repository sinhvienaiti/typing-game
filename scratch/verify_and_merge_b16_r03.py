import json
import sys
sys.path.append('scratch')

import b16_r03_p1, b16_r03_p2, b16_r03_p3, b16_r03_p4, b16_r03_p5

p1 = b16_r03_p1.data
p2 = b16_r03_p2.data
p3 = b16_r03_p3.data
p4 = b16_r03_p4.data
p5 = b16_r03_p5.data

reviewed_items = p1 + p2 + p3 + p4 + p5
assert len(reviewed_items) == 500, f"Expected 500 items, got {len(reviewed_items)}"

# Verify items
for idx, item in enumerate(reviewed_items):
    assert len(item['vi']) <= 35, f"vi length > 35 at {item['id']} ({item['hw']}): {item['vi']} (len {len(item['vi'])})"
    assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"invalid ipa at {item['id']}: {item['ipa']}"
    assert item['status'] == 'reviewed', f"status not reviewed at {item['id']}"

with open('content/english/qa-batches/batch-16.json', 'r', encoding='utf-8') as f:
    batch = json.load(f)

records = batch['records']
assert len(records) == 5000, f"Expected 5000 records in batch-16, got {len(records)}"

# Check matching IDs and headwords
for i in range(500):
    rec = records[1000 + i]
    rev = reviewed_items[i]
    assert rec['id'] == rev['id'], f"ID mismatch at {i}: {rec['id']} vs {rev['id']}"
    assert rec['hw'] == rev['hw'], f"HW mismatch at {i}: {rec['hw']} vs {rev['hw']}"

# Merge reviewed records
for i in range(500):
    records[1000 + i] = reviewed_items[i]

batch['reviewedCount'] = 1500

with open('content/english/qa-batches/batch-16.json', 'w', encoding='utf-8') as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print(f"Successfully merged Round 3 into batch-16.json! Reviewed count: {batch['reviewedCount']}/5000")
