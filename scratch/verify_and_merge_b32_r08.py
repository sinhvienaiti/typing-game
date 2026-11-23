import json

# Load all 5 parts
all_parts = []
for p in range(1, 6):
    with open(f'scratch/b32_r08_p{p}.json') as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} has {len(data)} items"
        all_parts.extend(data)

assert len(all_parts) == 500, f"Total items: {len(all_parts)}"

# Load batch-32
with open('content/english/qa-batches/batch-32.json') as f:
    batch = json.load(f)

records = batch['records']
assert len(records) == 5000

# Check slice 3500:4000
target_slice = records[3500:4000]
for i, (new_r, old_r) in enumerate(zip(all_parts, target_slice)):
    assert new_r['id'] == old_r['id'], f"Mismatch id at {i}: {new_r['id']} vs {old_r['id']}"
    assert new_r['hw'] == old_r['hw'], f"Mismatch hw at {i}: {new_r['hw']} vs {old_r['hw']}"
    assert len(new_r['vi']) <= 35, f"Length violation at {i} ({new_r['hw']}): {len(new_r['vi'])}"
    assert new_r['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {new_r['pos']}"
    if ' ' not in new_r['hw']:
        assert new_r['ipa'].startswith('/') and new_r['ipa'].endswith('/') and new_r['ipa'].count('/') == 2, f"Invalid ipa at {i}: {new_r['ipa']}"
    assert new_r['status'] == 'reviewed'

# Replace in batch
records[3500:4000] = all_parts
batch['records'] = records
batch['reviewedCount'] = 4000
batch['status'] = 'in-progress'

with open('content/english/qa-batches/batch-32.json', 'w') as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print("Batch 32 Round 8 merged successfully. reviewedCount = 4000.")
