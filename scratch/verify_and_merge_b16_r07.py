import json
import sys
import os

sys.path.insert(0, os.path.abspath('.'))

def merge_round_7():
    with open('content/english/qa-batches/batch-16.json', 'r', encoding='utf-8') as f:
        batch_data = json.load(f)

    all_reviewed = []
    for i in range(1, 6):
        mod = __import__(f'scratch.b16_r07_p{i}', fromlist=['reviewed_entries', 'records'])
        entries = getattr(mod, 'reviewed_entries', None) or getattr(mod, 'records', None)
        assert entries is not None, f"Could not find entries in part {i}"
        all_reviewed.extend(entries)

    print(f"Total reviewed entries for Round 7: {len(all_reviewed)}")
    assert len(all_reviewed) == 500

    start_idx = 3000
    end_idx = 3500

    for idx, new_entry in enumerate(all_reviewed):
        batch_idx = start_idx + idx
        orig_entry = batch_data['records'][batch_idx]
        assert orig_entry['id'] == new_entry['id'], f"ID mismatch at {batch_idx}: orig {orig_entry['id']} vs new {new_entry['id']}"
        assert orig_entry['hw'] == new_entry['hw'], f"HW mismatch at {batch_idx}: orig {orig_entry['hw']} vs new {new_entry['hw']}"

        # Update reviewed fields
        orig_entry['pos'] = new_entry['pos']
        orig_entry['ipa'] = new_entry['ipa']
        orig_entry['vi'] = new_entry['vi']
        orig_entry['status'] = 'reviewed'

    # Recalculate batch reviewedCount
    reviewed_count = sum(1 for r in batch_data['records'] if r.get('status') == 'reviewed')
    batch_data['reviewedCount'] = reviewed_count
    print(f"Updated batch reviewedCount: {reviewed_count}/{len(batch_data['records'])}")
    assert reviewed_count == 3500, f"Expected 3500 reviewed, got {reviewed_count}"

    with open('content/english/qa-batches/batch-16.json', 'w', encoding='utf-8') as f:
        json.dump(batch_data, f, ensure_ascii=False, indent=2)

    print("Batch 16 Round 7 successfully merged!")

if __name__ == '__main__':
    merge_round_7()
