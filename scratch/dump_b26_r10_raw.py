import json

with open("content/english/qa-batches/batch-26.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]
assert len(records) == 5000, f"Expected 5000 records, got {len(records)}"

for p in range(5):
    start = 4500 + p * 100
    end = start + 100
    part_slice = records[start:end]
    filename = f"scratch/b26_r10_raw_p{p+1}.json"
    with open(filename, "w", encoding="utf-8") as out:
        json.dump(part_slice, out, ensure_ascii=False, indent=2)
    print(f"Dumped {len(part_slice)} records ({part_slice[0]['id']} - {part_slice[-1]['id']}) to {filename}")
