import json

with open("content/english/qa-batches/batch-30.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]

for i in range(5):
    start = 4000 + i * 100
    end = start + 100
    part_records = records[start:end]
    with open(f"scratch/b30_r09_raw_p{i+1}.json", "w", encoding="utf-8") as out:
        json.dump(part_records, out, ensure_ascii=False, indent=2)

print("Dumped 5 raw parts for Batch 30 Round 9!")
