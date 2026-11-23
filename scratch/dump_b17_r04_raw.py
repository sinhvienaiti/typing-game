# -*- coding: utf-8 -*-
import json

with open("content/english/qa-batches/batch-17.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]
assert len(records) == 5000

for p in range(5):
    start = 1500 + p * 100
    end = start + 100
    slice_records = records[start:end]
    filename = f"scratch/b17_r04_raw_p{p+1}.json"
    with open(filename, "w", encoding="utf-8") as out:
        json.dump(slice_records, out, ensure_ascii=False, indent=2)
    print(f"Dumped Part {p+1} ({start} to {end-1}, hw: {slice_records[0]['hw']} .. {slice_records[-1]['hw']}) to {filename}")
