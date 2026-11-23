# scratch/verify_and_merge_b17_r04.py
import json
import sys
import re

import b17_r04_p1 as p1
import b17_r04_p2 as p2
import b17_r04_p3 as p3
import b17_r04_p4 as p4
import b17_r04_p5 as p5

BATCH_PATH = "content/english/qa-batches/batch-17.json"

def main():
    with open(BATCH_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    records = data["records"]
    assert len(records) == 5000, f"Expected 5000 records, got {len(records)}"

    p1_records = getattr(p1, "reviewed_records", getattr(p1, "reviewed_entries", None))
    p2_records = getattr(p2, "reviewed_records", getattr(p2, "reviewed_entries", None))
    p3_records = getattr(p3, "reviewed_records", getattr(p3, "reviewed_entries", None))
    p4_records = getattr(p4, "reviewed_records", getattr(p4, "reviewed_entries", None))
    p5_records = getattr(p5, "reviewed_records", getattr(p5, "reviewed_entries", None))

    all_reviewed = (
        p1_records +
        p2_records +
        p3_records +
        p4_records +
        p5_records
    )
    assert len(all_reviewed) == 500, f"Expected 500 reviewed records, got {len(all_reviewed)}"

    # Check ID alignment
    for i, rev in enumerate(all_reviewed):
        idx = 1500 + i
        orig = records[idx]
        assert orig["id"] == rev["id"], f"ID mismatch at {idx}: orig {orig['id']} vs rev {rev['id']}"
        assert orig["hw"] == rev["hw"], f"HW mismatch at {idx}: orig {orig['hw']} vs rev {rev['hw']}"
        # Validate schema & constraints
        assert len(rev["vi"]) <= 35, f"vi too long at {rev['id']}: {len(rev['vi'])} chars: {rev['vi']}"
        assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/") and rev["ipa"].count("/") == 2, f"Bad IPA at {rev['id']}: {rev['ipa']}"
        assert rev["pos"] in ["noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "num", "det"], f"Bad pos at {rev['id']}: {rev['pos']}"
        assert rev["status"] == "reviewed", f"Status not reviewed at {rev['id']}"
        assert "%%" not in rev["vi"], f"Crawler artifact in vi at {rev['id']}"
        assert not rev["vi"].startswith("Số nhiều của"), f"Crawler artifact in vi at {rev['id']}"
        assert not rev["vi"].startswith("Xem "), f"Crawler artifact in vi at {rev['id']}"
        assert not rev["vi"].startswith("Dạng "), f"Crawler artifact in vi at {rev['id']}"
        # Keep cefr, tier, notes intact
        assert rev["cefr"] == orig["cefr"]
        assert rev["tier"] == orig["tier"]
        assert rev["notes"] == orig["notes"]

        # Update record
        records[idx] = rev

    # Check reviewedCount
    rev_count = sum(1 for r in records if r.get("status") == "reviewed")
    print(f"Total reviewed count in batch-17: {rev_count}/5000")
    assert rev_count == 2000, f"Expected 2000 reviewed, got {rev_count}"

    data["reviewedCount"] = rev_count

    with open(BATCH_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Batch 17 Round 4 merged successfully!")

if __name__ == "__main__":
    main()
