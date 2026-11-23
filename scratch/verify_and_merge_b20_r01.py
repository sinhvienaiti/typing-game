import json

# Load all 5 parts
all_round_data = []
for p in range(1, 6):
    with open(f'scratch/b20_r01_p{p}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} has {len(data)} items instead of 100"
        all_round_data.extend(data)

assert len(all_round_data) == 500, f"Total round items {len(all_round_data)} != 500"

# Rigorous validation
for idx, item in enumerate(all_round_data):
    assert len(item['vi']) <= 35, f"vi too long at {idx} ({item['hw']}): {item['vi']}"
    assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"invalid ipa at {idx} ({item['hw']}): {item['ipa']}"
    assert item['status'] == 'reviewed'
    assert item['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det'], f"invalid pos: {item['pos']} at {idx}"

# Load batch-20.json
batch_path = 'content/english/qa-batches/batch-20.json'
with open(batch_path, 'r', encoding='utf-8') as f:
    batch = json.load(f)

# Verify start index 0
for i in range(500):
    expected_id = batch['records'][i]['id']
    actual_id = all_round_data[i]['id']
    assert expected_id == actual_id, f"ID mismatch at {i}: expected {expected_id}, got {actual_id}"
    batch['records'][i] = all_round_data[i]

# Count total reviewed in batch
reviewed_count = sum(1 for r in batch['records'] if r.get('status') == 'reviewed')
batch['reviewedCount'] = reviewed_count
if reviewed_count == batch['wordCount']:
    batch['status'] = 'completed'
else:
    batch['status'] = 'in-progress'

with open(batch_path, 'w', encoding='utf-8') as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print(f"Batch 20 Round 1 merged successfully! Total reviewed: {reviewed_count}/5000, status: {batch['status']}")
