import json
import sys
import os

sys.path.insert(0, os.path.abspath("."))

def main():
    print("Loading batch-18.json...")
    with open("content/english/qa-batches/batch-18.json") as f:
        batch18 = json.load(f)

    records = batch18["records"]
    assert len(records) == 5000, f"Expected 5000 records, got {len(records)}"

    # Load all 5 parts of round 7
    round07_records = []
    for p_idx in range(1, 6):
        mod = __import__(f"scratch.b18_r07_p{p_idx}", fromlist=["data"])
        data = getattr(mod, "data")
        assert len(data) == 100, f"Part {p_idx} has {len(data)} items, expected 100"
        round07_records.extend(data)

    assert len(round07_records) == 500, f"Round 7 total: {len(round07_records)}, expected 500"

    # Verify against records 3000-3499
    start_idx = 3000
    for i, reviewed in enumerate(round07_records):
        idx = start_idx + i
        raw = records[idx]

        assert reviewed["id"] == raw["id"], f"ID mismatch at {idx}: {reviewed['id']} vs {raw['id']}"
        assert reviewed["hw"] == raw["hw"], f"HW mismatch at {idx}: {reviewed['hw']} vs {raw['hw']}"
        assert reviewed["cefr"] == raw["cefr"], f"CEFR mismatch at {idx}: {reviewed['cefr']} vs {raw['cefr']}"
        assert reviewed["tier"] == raw["tier"], f"TIER mismatch at {idx}: {reviewed['tier']} vs {raw['tier']}"
        assert reviewed["notes"] == raw["notes"], f"NOTES mismatch at {idx}: {reviewed['notes']} vs {raw['notes']}"
        assert reviewed["status"] == "reviewed", f"Status must be reviewed at {idx}"
        assert len(reviewed["vi"]) <= 35, f"Vietnamese too long (>35) at {idx}: {reviewed['vi']}"
        assert reviewed["ipa"].startswith("/") and reviewed["ipa"].endswith("/") and reviewed["ipa"].count("/") == 2, f"Bad IPA at {idx}: {reviewed['ipa']}"
        assert reviewed["pos"] in ["noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"], f"Bad POS at {idx}: {reviewed['pos']}"

        # Replace in records
        records[idx] = reviewed

    # Update metadata
    batch18["reviewedCount"] = 3500
    batch18["status"] = "in-progress"

    # Verify that exactly 3500 records are reviewed
    all_reviewed = [r for r in records if r.get("status") == "reviewed"]
    assert len(all_reviewed) == 3500, f"Expected 3500 reviewed, got {len(all_reviewed)}"

    print("Writing updated batch-18.json...")
    with open("content/english/qa-batches/batch-18.json", "w", encoding="utf-8") as f:
        json.dump(batch18, f, ensure_ascii=False, indent=2)

    print("Successfully merged Round 7 into batch-18.json! Batch 18 progress: 3500/5000 words!")

if __name__ == "__main__":
    main()
