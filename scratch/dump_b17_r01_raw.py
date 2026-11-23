import json

batch_file = "content/english/qa-batches/batch-17.json"
with open(batch_file, "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]

for i in range(5):
    start = i * 100
    end = start + 100
    slice_data = records[start:end]
    fname = f"scratch/b17_r01_raw_p{i+1}.json"
    with open(fname, "w", encoding="utf-8") as out:
        json.dump(slice_data, out, ensure_ascii=False, indent=2)
    print(f"Dumped {fname}: {slice_data[0]['id']} ({slice_data[0]['hw']}) to {slice_data[-1]['id']} ({slice_data[-1]['hw']})")
