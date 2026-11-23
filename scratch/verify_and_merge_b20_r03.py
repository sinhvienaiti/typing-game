import json

# Verify all 5 parts of round 3
round3_all = []
for p in range(1, 6):
    with open(f"scratch/b20_r03_p{p}.json") as f:
        data = json.load(f)
        assert len(data) == 100, f"Part {p} does not have 100 items"
        round3_all.extend(data)

assert len(round3_all) == 500, f"Round 3 does not have 500 items, got {len(round3_all)}"

# Check batch 20
with open("content/english/qa-batches/batch-20.json") as f:
    batch20 = json.load(f)

print(f"Batch 20 total records: {len(batch20['records'])}")
print(f"Current reviewedCount: {batch20['reviewedCount']}")

# Check that slice 1000:1500 matches round3_all IDs
for i in range(500):
    rec = batch20["records"][1000 + i]
    r_item = round3_all[i]
    assert rec["id"] == r_item["id"], f"Mismatch at {i}: {rec['id']} vs {r_item['id']}"
    assert rec["hw"] == r_item["hw"], f"HW mismatch at {i}: {rec['hw']} vs {r_item['hw']}"
    # Update record
    batch20["records"][1000 + i] = r_item

batch20["reviewedCount"] = 1500

with open("content/english/qa-batches/batch-20.json", "w") as f:
    json.dump(batch20, f, ensure_ascii=False, indent=2)

print("Batch 20 Round 3 merged successfully! Reviewed count is now 1500.")
