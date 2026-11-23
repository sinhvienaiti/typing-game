import json
import re

ALLOWED_POS = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}

def verify_and_merge():
    all_round_items = []
    for part in range(1, 6):
        path = f"scratch/b27_r08_p{part}.json"
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert len(data) == 100, f"Part {part} has {len(data)} items, expected 100"
            all_round_items.extend(data)
            
    assert len(all_round_items) == 500, f"Expected 500 items, got {len(all_round_items)}"
    
    # Check ID sequence
    start_id = 33502
    for i, item in enumerate(all_round_items):
        expected_id = f"lex.en.200k.{start_id + i:06d}"
        assert item["id"] == expected_id, f"Item {i} has id {item['id']}, expected {expected_id}"
        assert item["status"] == "reviewed", f"Item {item['id']} status is {item['status']}"
        assert len(item["vi"]) <= 35, f"Item {item['id']} vi length {len(item['vi'])} > 35: {item['vi']}"
        assert item["pos"] in ALLOWED_POS, f"Item {item['id']} invalid pos: {item['pos']}"
        
        # Single word IPA check
        hw = item["hw"]
        ipa = item["ipa"]
        if " " not in hw:
            assert ipa.startswith("/") and ipa.endswith("/"), f"Single word {hw} invalid ipa format: {ipa}"
            assert len(ipa) > 2, f"Single word {hw} has empty IPA"
            assert not ipa.startswith("/ ") and not ipa.endswith(" /"), f"Single word {hw} has space inside slash: {ipa}"
        else:
            if ipa != "":
                assert ipa.startswith("/") and ipa.endswith("/"), f"Multi-word {hw} invalid ipa format: {ipa}"
                assert not ipa.startswith("/ ") and not ipa.endswith(" /"), f"Multi-word {hw} space inside slash: {ipa}"

    print("All 500 items verified successfully!")
    
    # Load batch-27.json
    batch_file = "content/english/qa-batches/batch-27.json"
    with open(batch_file, "r", encoding="utf-8") as f:
        batch_data = json.load(f)
        
    slice_start = 3500
    slice_end = 4000
    
    # Check existing ids in slice
    for idx, (old_item, new_item) in enumerate(zip(batch_data["records"][slice_start:slice_end], all_round_items)):
        assert old_item["id"] == new_item["id"], f"Mismatch at index {slice_start + idx}: old {old_item['id']} vs new {new_item['id']}"
        assert old_item["hw"] == new_item["hw"], f"HW mismatch at index {slice_start + idx}: old {old_item['hw']} vs new {new_item['hw']}"

    # Replace slice
    batch_data["records"][slice_start:slice_end] = all_round_items
    batch_data["reviewedCount"] = 4000
    batch_data["status"] = "in-progress"
    
    with open(batch_file, "w", encoding="utf-8") as f:
        json.dump(batch_data, f, ensure_ascii=False, indent=2)
        
    print(f"Batch 27 updated successfully! reviewedCount: {batch_data['reviewedCount']}")
    
    # Update INDEX.md
    index_file = "content/english/qa-batches/INDEX.md"
    with open(index_file, "r", encoding="utf-8") as f:
        index_content = f.read()
        
    target_line = "| 27 | `batch-27.json` | 5000 | bell toad ... imams | Phase 2 (100k-200k Expanded & Phrases) | ⏳ in-progress (3500/5000) |"
    replacement_line = "| 27 | `batch-27.json` | 5000 | bell toad ... imams | Phase 2 (100k-200k Expanded & Phrases) | ⏳ in-progress (4000/5000) |"
    
    assert target_line in index_content, f"Target line not found in INDEX.md: {target_line}"
    index_content = index_content.replace(target_line, replacement_line)
    
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(index_content)
        
    print("INDEX.md updated successfully!")

if __name__ == "__main__":
    verify_and_merge()
