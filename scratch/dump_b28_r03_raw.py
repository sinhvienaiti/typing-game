import json

with open("content/english/qa-batches/batch-28.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

# Round 3: records 1000 to 1499
records = batch["records"][1000:1500]
assert len(records) == 500

for p in range(5):
    part_records = records[p*100 : (p+1)*100]
    filename = f"scratch/b28_r03_raw_p{p+1}.json"
    with open(filename, "w", encoding="utf-8") as out:
        json.dump(part_records, out, ensure_ascii=False, indent=2)
    print(f"Wrote {filename}: {len(part_records)} records, IDs {part_records[0]['id']} to {part_records[-1]['id']}")
