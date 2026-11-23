import json

def main():
    parts = []
    for i in range(1, 6):
        path = f"scratch/b21_r02_p{i}.json"
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert len(data) == 100, f"Expected 100 records in {path}, got {len(data)}"
            parts.extend(data)

    assert len(parts) == 500, f"Expected 500 records total, got {len(parts)}"

    batch_path = "content/english/qa-batches/batch-21.json"
    with open(batch_path, "r", encoding="utf-8") as f:
        batch_data = json.load(f)

    records = batch_data["records"]
    assert len(records) == 5000, f"Expected 5000 records in batch-21, got {len(records)}"

    start_idx = 500
    end_idx = 1000

    allowed_pos = ["noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"]

    for i, reviewed_item in enumerate(parts):
        idx = start_idx + i
        orig_item = records[idx]
        assert orig_item["id"] == reviewed_item["id"], f"ID mismatch at {idx}: {orig_item['id']} vs {reviewed_item['id']}"
        assert orig_item["hw"] == reviewed_item["hw"], f"HW mismatch at {idx}: {orig_item['hw']} vs {reviewed_item['hw']}"
        assert len(reviewed_item["vi"]) <= 35, f"vi too long at {idx}: {reviewed_item['vi']} ({len(reviewed_item['vi'])} chars)"
        assert reviewed_item["pos"] in allowed_pos, f"Invalid pos at {idx}: {reviewed_item['pos']}"
        assert reviewed_item["ipa"].startswith("/") and reviewed_item["ipa"].endswith("/") and reviewed_item["ipa"].count("/") == 2, f"Invalid ipa at {idx}: {reviewed_item['ipa']}"
        assert reviewed_item["status"] == "reviewed"

        # Preserve cefr, tier, notes
        reviewed_item["cefr"] = orig_item.get("cefr", "C2")
        reviewed_item["tier"] = orig_item.get("tier", "expanded")
        reviewed_item["notes"] = orig_item.get("notes", "")

        records[idx] = reviewed_item

    # Count reviewed
    reviewed_count = sum(1 for r in records if r["status"] == "reviewed")
    assert reviewed_count == 1000, f"Expected 1000 reviewed records, got {reviewed_count}"

    batch_data["records"] = records
    batch_data["reviewedCount"] = reviewed_count
    batch_data["status"] = "in-progress"

    with open(batch_path, "w", encoding="utf-8") as f:
        json.dump(batch_data, f, ensure_ascii=False, indent=2)

    print("Successfully verified and merged Round 2 into batch-21.json! reviewedCount = 1000")

if __name__ == "__main__":
    main()
