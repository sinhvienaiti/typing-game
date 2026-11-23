import json
from scratch.b15_r04_p1 import PART_DATA as p1
from scratch.b15_r04_p2 import PART_DATA as p2
from scratch.b15_r04_p3 import PART_DATA as p3
from scratch.b15_r04_p4 import PART_DATA as p4
from scratch.b15_r04_p5 import PART_DATA as p5

all_reviewed = p1 + p2 + p3 + p4 + p5
assert len(all_reviewed) == 500, f"Expected 500 items, got {len(all_reviewed)}"

batch_file = "content/english/qa-batches/batch-15.json"
with open(batch_file, "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]
start_idx = 1500
end_idx = 2000

for i, rev in enumerate(all_reviewed):
    rec_idx = start_idx + i
    orig = records[rec_idx]
    assert orig["id"] == rev["id"], f"ID mismatch at index {rec_idx}: {orig['id']} vs {rev['id']}"
    assert orig["hw"] == rev["hw"], f"HW mismatch at index {rec_idx}: {orig['hw']} vs {rev['hw']}"
    assert len(rev["vi"]) <= 35, f"Vi len > 35 at index {rec_idx} ({rev['hw']}): {len(rev['vi'])} -> {rev['vi']}"
    assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/"), f"Bad IPA format: {rev['ipa']}"
    assert rev["ipa"].count("/") == 2, f"Bad slash count: {rev['ipa']}"
    assert rev["status"] == "reviewed", f"Status not reviewed at {rec_idx}"

    # Update record
    records[rec_idx]["pos"] = rev["pos"]
    records[rec_idx]["ipa"] = rev["ipa"]
    records[rec_idx]["vi"] = rev["vi"]
    records[rec_idx]["cefr"] = rev["cefr"]
    records[rec_idx]["tier"] = rev["tier"]
    records[rec_idx]["status"] = "reviewed"
    records[rec_idx]["notes"] = rev.get("notes", "")

# Verify total reviewed count
reviewed_count = sum(1 for r in records if r.get("status") == "reviewed")
assert reviewed_count == 2000, f"Expected 2000 reviewed records, found {reviewed_count}"
batch["reviewedCount"] = reviewed_count

with open(batch_file, "w", encoding="utf-8") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print(f"Successfully verified and merged Round 4! Total reviewedCount in batch-15.json is now {reviewed_count}.")
