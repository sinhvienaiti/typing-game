import json

# Load all 5 parts
all_parts = []
for p in range(1, 6):
    with open(f'scratch/b29_r08_p{p}.json') as f:
        part_items = json.load(f)
        assert len(part_items) == 100, f"Part {p} has {len(part_items)} items instead of 100"
        all_parts.extend(part_items)

assert len(all_parts) == 500, f"Expected 500 items, got {len(all_parts)}"

# Load batch-29
with open('content/english/qa-batches/batch-29.json') as f:
    batch = json.load(f)

# Verify slice [3500:4000]
slice_items = batch['records'][3500:4000]
assert len(slice_items) == 500

valid_pos = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"}

for i, (rev, orig) in enumerate(zip(all_parts, slice_items)):
    assert rev['id'] == orig['id'], f"ID mismatch at {i}: {rev['id']} vs {orig['id']}"
    assert rev['hw'] == orig['hw'], f"HW mismatch at {i}: {rev['hw']} vs {orig['hw']}"
    assert rev['pos'] in valid_pos, f"Invalid POS at {i}: {rev['pos']}"
    assert len(rev['vi']) <= 35, f"VI too long ({len(rev['vi'])}) at {i}: {rev['vi']}"
    assert rev['status'] == 'reviewed', f"Status not reviewed at {i}"
    assert rev['ipa'].startswith('/') and rev['ipa'].endswith('/'), f"Invalid IPA at {i}: {rev['ipa']}"
    assert rev['ipa'].count('/') == 2, f"IPA slash count != 2 at {i}: {rev['ipa']}"
    assert "  " not in rev['vi'], f"Double space in VI at {i}: {rev['vi']}"

# Apply reviewed items
batch['records'][3500:4000] = all_parts
batch['reviewedCount'] = 4000
batch['status'] = 'in-progress'

with open('content/english/qa-batches/batch-29.json', 'w', encoding='utf-8') as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 8 merged successfully! Total reviewedCount: 4000/5000")
