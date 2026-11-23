import json

with open("content/english/qa-batches/batch-17.json") as f:
    data = json.load(f)

records = data["records"]

for part_idx in range(5):
    start = 3500 + part_idx * 100
    end = start + 100
    slice_data = records[start:end]
    filename = f"scratch/b17_r08_raw_p{part_idx + 1}.json"
    with open(filename, "w", encoding="utf-8") as f_out:
        json.dump(slice_data, f_out, ensure_ascii=False, indent=2)
    print(f"Dumped {len(slice_data)} records to {filename} (indices {start}..{end-1}, IDs {slice_data[0]['id']}..{slice_data[-1]['id']}, words {slice_data[0]['hw']}..{slice_data[-1]['hw']})")
