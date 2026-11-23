import json

with open("content/english/qa-batches/batch-13.json", "r", encoding="utf-8") as f:
    data = json.load(f)

records = data["records"]

for p in range(5):
    start = 3500 + p * 100
    end = start + 100
    slice_records = records[start:end]
    fname = f"scratch/b13_r08_raw_p{p+1}.json"
    with open(fname, "w", encoding="utf-8") as out:
        json.dump(slice_records, out, ensure_ascii=False, indent=2)
    print(f"Exported {fname}: {len(slice_records)} records, {slice_records[0]['hw']} to {slice_records[-1]['hw']}")
