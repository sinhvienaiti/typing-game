import json

def main():
    parts = []
    for i in range(1, 6):
        with open(f'scratch/b24_r6_p{i}.json') as f:
            data = json.load(f)
            assert len(data) == 100, f"Part {i} length {len(data)} != 100"
            parts.extend(data)

    assert len(parts) == 500, f"Total records {len(parts)} != 500"

    with open('content/english/qa-batches/batch-24.json') as f:
        batch = json.load(f)

    target_slice = batch['records'][2500:3000]
    assert len(target_slice) == 500

    valid_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
    expected_keys = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

    for i in range(500):
        src = target_slice[i]
        rev = parts[i]

        assert src['id'] == rev['id'], f"ID mismatch at {i}: {src['id']} != {rev['id']}"
        assert src['hw'] == rev['hw'], f"HW mismatch at {i}: {src['hw']} != {rev['hw']}"
        assert list(rev.keys()) == expected_keys, f"Keys mismatch at {i}: {list(rev.keys())}"
        assert rev['pos'] in valid_pos, f"Invalid POS at {i}: {rev['pos']}"
        assert rev['status'] == 'reviewed', f"Status not reviewed at {i}"

        # IPA
        ipa = rev['ipa']
        assert ipa.startswith('/') and ipa.endswith('/') and len(ipa) > 2, f"Invalid IPA at {i}: {ipa}"
        assert ipa.count('/') == 2, f"Multiple slashes in IPA at {i}: {ipa}"
        assert not ipa.startswith('/ ') and not ipa.endswith(' /'), f"Boundary space in IPA at {i}: {ipa}"

        # VI
        vi = rev['vi']
        assert 0 < len(vi) <= 35, f"VI length invalid at {i} ({rev['hw']}): {len(vi)} ({vi})"
        for bad in ['Số nhiều', 'Xem ', 'Dạng ', 'Viết tắt', '%%']:
            assert bad not in vi, f"Garbage in VI at {i}: {bad}"

    # Apply merge
    batch['records'][2500:3000] = parts
    batch['reviewedCount'] = 3000

    with open('content/english/qa-batches/batch-24.json', 'w', encoding='utf-8') as f:
        json.dump(batch, f, ensure_ascii=False, indent=2)

    print("Successfully verified and merged Batch 24 Round 6 (2500-2999). Total reviewedCount: 3000")

if __name__ == '__main__':
    main()
