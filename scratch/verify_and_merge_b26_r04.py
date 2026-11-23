import json

all_r04 = []
for p in range(1, 6):
    with open(f'scratch/b26_r04_p{p}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} length is {len(data)}, expected 100"
        all_r04.extend(data)

assert len(all_r04) == 500, f"Expected 500 records, got {len(all_r04)}"

allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
expected_keys = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

for idx, item in enumerate(all_r04):
    exp_id = f"lex.en.200k.{26502 + idx:06d}"
    assert item['id'] == exp_id, f"ID mismatch at {idx}: expected {exp_id}, got {item['id']}"
    assert len(item['vi']) <= 35, f"Overlong vi at {item['id']} ({item['hw']}): {len(item['vi'])} chars: {item['vi']}"
    assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"Bad IPA at {item['id']} ({item['hw']}): {item['ipa']}"
    assert not item['ipa'][1:].startswith(' ') and not item['ipa'][:-1].endswith(' '), f"Space in IPA at {item['id']}: {item['ipa']}"
    assert item['pos'] in allowed_pos, f"Bad pos at {item['id']}: {item['pos']}"
    assert item['status'] == 'reviewed', f"Bad status at {item['id']}"
    assert list(item.keys()) == expected_keys, f"Keys mismatch at {item['id']}"

with open('content/english/qa-batches/batch-26.json', 'r', encoding='utf-8') as f:
    batch = json.load(f)

assert len(batch['records']) == 5000, f"Batch size mismatch: {len(batch['records'])}"
for idx in range(500):
    assert batch['records'][1500 + idx]['id'] == all_r04[idx]['id']

batch['records'][1500:2000] = all_r04
batch['reviewedCount'] = 2000
batch['status'] = 'in-progress'

with open('content/english/qa-batches/batch-26.json', 'w', encoding='utf-8') as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print("Batch 26 updated: reviewedCount = 2000 / 5000")

# Update INDEX.md
with open('content/english/qa-batches/INDEX.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.startswith('| [batch-26.json]'):
        new_lines.append('| [batch-26.json](./batch-26.json) | 5,000 | `200k.025002` - `200k.030001` | ⏳ in-progress (2000/5000) | Round 4 completed (2000/5000 words reviewed) |\n')
    else:
        new_lines.append(line)

with open('content/english/qa-batches/INDEX.md', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("INDEX.md updated successfully")
