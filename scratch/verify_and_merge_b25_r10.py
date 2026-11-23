import json

parts = []
for p in range(1, 6):
    with open(f'scratch/b25_r10_p{p}.json') as f:
        data = json.load(f)
        assert len(data) == 100, f'Part {p} length is {len(data)}, expected 100'
        parts.extend(data)

assert len(parts) == 500, f'Total length is {len(parts)}, expected 500'

expected_start = 24502
for i, item in enumerate(parts):
    expected_id = f'lex.en.200k.{expected_start + i:06d}'
    assert item['id'] == expected_id, f'Index {i}: id {item["id"]} != expected {expected_id}'
    assert item['status'] == 'reviewed', f'Index {i}: status is {item["status"]}'
    assert len(item['vi']) <= 35, f'Index {i}: vi len {len(item["vi"])} > 35: {item["vi"]}'
    assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f'Index {i}: bad ipa {item["ipa"]}'
    assert item['pos'] in {'noun', 'verb', 'adj', 'adv', 'intj', 'prep', 'conj', 'pron', 'det', 'num', 'phrase'}, f'Index {i}: bad pos {item["pos"]}'

print('All 500 entries in Batch 25 Round 10 passed validation checks!')

with open('content/english/qa-batches/batch-25.json') as f:
    batch = json.load(f)

assert len(batch['records']) == 5000, f'Batch records count is {len(batch["records"])}, expected 5000'
assert batch['reviewedCount'] == 4500, f'Expected current reviewedCount 4500, got {batch["reviewedCount"]}'

# Verify alignment
for i in range(500):
    assert batch['records'][4500 + i]['id'] == parts[i]['id'], f'Mismatch at {4500 + i}: batch has {batch["records"][4500 + i]["id"]}, part has {parts[i]["id"]}'

# Merge
batch['records'][4500:5000] = parts
batch['reviewedCount'] = 5000
batch['status'] = 'completed'

with open('content/english/qa-batches/batch-25.json', 'w', encoding='utf-8') as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
    f.write('\n')

print('Successfully merged Round 10 (4500-4999) into batch-25.json. Batch 25 is 100% COMPLETED (5000/5000)!')
