import json

parts = []
for p in range(1, 6):
    with open(f'scratch/b26_r01_p{p}.json') as f:
        data = json.load(f)
        assert len(data) == 100, f'Part {p} length is {len(data)}, expected 100'
        parts.extend(data)

assert len(parts) == 500, f'Total length is {len(parts)}, expected 500'

expected_start = 25002
for i, item in enumerate(parts):
    expected_id = f'lex.en.200k.{expected_start + i:06d}'
    assert item['id'] == expected_id, f'Index {i}: id {item["id"]} != expected {expected_id}'
    assert item['status'] == 'reviewed', f'Index {i}: status is {item["status"]}'
    assert len(item['vi']) <= 35, f'Index {i}: vi len {len(item["vi"])} > 35: {item["vi"]}'
    assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f'Index {i}: bad ipa {item["ipa"]}'
    assert item['pos'] in {'noun', 'verb', 'adj', 'adv', 'intj', 'prep', 'conj', 'pron', 'det', 'num', 'phrase'}, f'Index {i}: bad pos {item["pos"]}'

print('All 500 entries in Batch 26 Round 1 passed validation checks!')

with open('content/english/qa-batches/batch-26.json') as f:
    batch = json.load(f)

assert len(batch['records']) == 5000, f'Batch records count is {len(batch["records"])}, expected 5000'
assert batch['reviewedCount'] == 0, f'Expected current reviewedCount 0, got {batch["reviewedCount"]}'

# Verify alignment
for i in range(500):
    assert batch['records'][i]['id'] == parts[i]['id'], f'Mismatch at {i}: batch has {batch["records"][i]["id"]}, part has {parts[i]["id"]}'

# Merge
batch['records'][0:500] = parts
batch['reviewedCount'] = 500
batch['status'] = 'in-progress'

with open('content/english/qa-batches/batch-26.json', 'w', encoding='utf-8') as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
    f.write('\n')

print('Successfully merged Round 1 (0-499) into batch-26.json. Reviewed count: 500/5000!')
