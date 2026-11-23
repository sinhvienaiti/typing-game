import json, re

# 1. Load parts
all_round_items = []
for p in range(1, 6):
    fn = f'scratch/b32_r02_p{p}.json'
    with open(fn, 'r', encoding='utf-8') as f:
        items = json.load(f)
        assert len(items) == 100, f"Part {p} has {len(items)} items, expected 100"
        all_round_items.extend(items)

assert len(all_round_items) == 500, f"Total items {len(all_round_items)}, expected 500"

# 2. Check IDs
for idx, it in enumerate(all_round_items):
    expected_id = f"lex.en.200k.{55502 + idx:06d}"
    assert it['id'] == expected_id, f"Item {idx} ID mismatch: {it['id']} vs {expected_id}"
    assert it['status'] == 'reviewed'
    assert len(it['vi']) <= 35, f"vi length > 35 for {it['id']}: {it['vi']}"
    assert it['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase']
    if it['ipa'] != '':
        assert it['ipa'].startswith('/') and it['ipa'].endswith('/') and it['ipa'].count('/') == 2
    elif ' ' not in it['hw']:
        raise AssertionError(f"Single word missing IPA: {it['id']} ({it['hw']})")

print("All 500 items validated successfully against quality gates!")

# 3. Load batch-32.json and merge
with open('content/english/qa-batches/batch-32.json', 'r', encoding='utf-8') as f:
    batch = json.load(f)

records = batch['records']
assert len(records) == 5000, f"Expected 5000 records, got {len(records)}"

# Check that records[500:1000] match IDs
for i in range(500):
    assert records[500 + i]['id'] == all_round_items[i]['id']
    assert records[500 + i]['hw'] == all_round_items[i]['hw']

# Replace records 500 to 999
records[500:1000] = all_round_items
batch['reviewedCount'] = 1000
batch['status'] = 'in-progress'

with open('content/english/qa-batches/batch-32.json', 'w', encoding='utf-8') as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print(f"batch-32.json successfully updated! reviewedCount: {batch['reviewedCount']}")
