import json

with open("content/english/qa-batches/batch-27.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]

for i in range(5):
    start = 3000 + i * 100
    end = start + 100
    slice_data = records[start:end]
    part = i + 1
    with open(f"scratch/b27_r07_raw_p{part}.json", "w", encoding="utf-8") as out:
        json.dump(slice_data, out, ensure_ascii=False, indent=2)
    print(f"Dumped Part {part}: indices {start} to {end-1}, IDs {slice_data[0]['id']} to {slice_data[-1]['id']}")
