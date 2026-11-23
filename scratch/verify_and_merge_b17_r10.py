import json

def main():
    print("Loading batch-17.json...")
    with open("content/english/qa-batches/batch-17.json") as f:
        batch17 = json.load(f)

    records = batch17["records"]
    assert len(records) == 5000, f"Expected 5000 records, got {len(records)}"

    # Load all 5 parts of round 10
    round10_records = []
    for p_idx in range(1, 6):
        mod = __import__(f"scratch.b17_r10_p{p_idx}", fromlist=[f"p{p_idx}_data", "reviewed_records"])
        data = getattr(mod, f"p{p_idx}_data", getattr(mod, "reviewed_records", None))
        assert len(data) == 100, f"Part {p_idx} has {len(data)} items, expected 100"
        round10_records.extend(data)

    assert len(round10_records) == 500, f"Round 10 total: {len(round10_records)}, expected 500"

    # Verify against records 4500-4999
    start_idx = 4500
    for i, reviewed in enumerate(round10_records):
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
    batch17["reviewedCount"] = 5000
    batch17["status"] = "completed"

    # Verify that all 5000 records are reviewed
    all_reviewed = [r for r in records if r.get("status") == "reviewed"]
    assert len(all_reviewed) == 5000, f"Expected 5000 reviewed, got {len(all_reviewed)}"

    print("Writing updated batch-17.json...")
    with open("content/english/qa-batches/batch-17.json", "w", encoding="utf-8") as f:
        json.dump(batch17, f, ensure_ascii=False, indent=2)

    print("Successfully merged Round 10 into batch-17.json! Batch 17 is now 100% completed (5000/5000 words)!")

if __name__ == "__main__":
    main()
