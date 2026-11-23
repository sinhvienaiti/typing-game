import json

with open("content/english/qa-batches/batch-26.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]
r06_records = records[2500:3000]
assert len(r06_records) == 500, f"Expected 500 records, got {len(r06_records)}"

for p in range(5):
    part_records = r06_records[p*100 : (p+1)*100]
    with open(f"scratch/b26_r06_raw_p{p+1}.json", "w", encoding="utf-8") as out_f:
        json.dump(part_records, out_f, ensure_ascii=False, indent=2)

print("Dumped b26_r06 raw parts 1-5 successfully")
