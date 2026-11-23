# -*- coding: utf-8 -*-
import json

def main():
    # 1. Load 5 parts
    round_items = []
    for p in range(1, 6):
        with open(f'scratch/b31_r04_p{p}.json', 'r', encoding='utf-8') as f:
            items = json.load(f)
            assert len(items) == 100, f"Part {p} has {len(items)} items"
            round_items.extend(items)
    
    assert len(round_items) == 500, f"Total items {len(round_items)} != 500"

    # 2. Load batch-31.json
    with open('content/english/qa-batches/batch-31.json', 'r', encoding='utf-8') as f:
        batch_data = json.load(f)

    records = batch_data['records']
    print(f"Loaded batch-31. Total records: {len(records)}, current reviewedCount: {batch_data.get('reviewedCount')}")

    # 3. Check records 1500:2000
    for idx, new_item in enumerate(round_items):
        target_idx = 1500 + idx
        orig_item = records[target_idx]
        assert orig_item['id'] == new_item['id'], f"ID mismatch at {target_idx}: {orig_item['id']} vs {new_item['id']}"
        assert orig_item['hw'] == new_item['hw'], f"HW mismatch at {target_idx}: {orig_item['hw']} vs {new_item['hw']}"
        # Update
        records[target_idx] = new_item

    # 4. Update metadata
    batch_data['reviewedCount'] = 2000
    batch_data['status'] = "in-progress"

    # 5. Full validation of first 2000 records
    allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
    expected_keys = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

    for i in range(2000):
        rec = records[i]
        assert list(rec.keys()) == expected_keys, f"Keys mismatch at {i}: {list(rec.keys())}"
        assert rec['status'] == 'reviewed', f"Status not reviewed at {i}: {rec['status']}"
        assert len(rec['vi']) <= 35, f"vi too long ({len(rec['vi'])}) at {i}: {rec['vi']}"
        assert rec['pos'] in allowed_pos, f"pos invalid at {i}: {rec['pos']}"
        if ' ' not in rec['hw']:
            assert rec['ipa'].startswith('/') and rec['ipa'].endswith('/') and len(rec['ipa']) > 2, f"invalid single word ipa at {i}: {rec['ipa']}"
        if ';' in rec['vi']:
            for part in rec['vi'].split(';')[1:]:
                assert part.startswith(' '), f"missing space after semicolon at {i}: {rec['vi']}"

    # 6. Save batch-31.json
    with open('content/english/qa-batches/batch-31.json', 'w', encoding='utf-8') as f:
        json.dump(batch_data, f, ensure_ascii=False, indent=2)

    print("Successfully merged and validated Round 4 in batch-31.json! Total reviewed: 2000/5000")

if __name__ == '__main__':
    main()
