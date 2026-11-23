# scratch/dump_b17_r07_raw.py
import json

with open("content/english/qa-batches/batch-17.json") as f:
    data = json.load(f)

records = data["records"]

for p in range(5):
    start = 3000 + p * 100
    end = start + 100
    slice_data = records[start:end]
    fname = f"scratch/b17_r07_raw_p{p+1}.json"
    with open(fname, "w", encoding="utf-8") as out:
        json.dump(slice_data, out, ensure_ascii=False, indent=2)
    print(f"Dumped {len(slice_data)} records to {fname} (indices {start}..{end-1}, IDs {slice_data[0]['id']}..{slice_data[-1]['id']})")
