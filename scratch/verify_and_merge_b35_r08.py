import json

with open("content/english/qa-batches/batch-35.json") as f:
    batch = json.load(f)

merged = []
for p in range(1, 6):
    with open(f"scratch/b35_r08_p{p}.json") as pf:
        merged.extend(json.load(pf))

assert len(merged) == 500
start = 3500
for i, r in enumerate(merged):
    assert batch["records"][start + i]["id"] == r["id"], f"Mismatch at {start + i}"
    assert r["status"] == "reviewed"
    batch["records"][start + i] = r

batch["reviewedCount"] = 4000
batch["status"] = "in-progress"

with open("content/english/qa-batches/batch-35.json", "w") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)

print("Merged batch-35 round 8 (4000/5000 in-progress) OK")
