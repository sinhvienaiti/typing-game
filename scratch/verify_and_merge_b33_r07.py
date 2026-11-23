import json

with open('content/english/qa-batches/batch-33.json') as f:
    batch = json.load(f)

merged = []
for part in range(1, 6):
    with open(f'scratch/b33_r07_p{part}.json') as f:
        merged.extend(json.load(f))

assert len(merged) == 500
start = 3000
for i, item in enumerate(merged):
    orig = batch['records'][start + i]
    assert item['id'] == orig['id'], f"id mismatch at {start+i}"
    assert item['hw'] == orig['hw'], f"hw mismatch at {start+i}"
    assert item['status'] == 'reviewed', f"status not reviewed at {start+i}"
    assert len(item['vi']) <= 35, f"vi too long at {start+i}"
    assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"bad ipa at {start+i}"
    assert not item['ipa'][1:-1].startswith(' ') and not item['ipa'][1:-1].endswith(' '), f"space in ipa at {start+i}"
    batch['records'][start + i] = item

batch['reviewedCount'] = 3500
batch['status'] = 'in-progress'

with open('content/english/qa-batches/batch-33.json', 'w') as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
print("Successfully merged batch-33 round 7 (3500/5000)")
