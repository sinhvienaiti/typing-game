# -*- coding: utf-8 -*-
import json

with open("content/english/qa-batches/batch-17.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]

slices = [
    (500, 600, "scratch/b17_r02_raw_p1.json"),
    (600, 700, "scratch/b17_r02_raw_p2.json"),
    (700, 800, "scratch/b17_r02_raw_p3.json"),
    (800, 900, "scratch/b17_r02_raw_p4.json"),
    (900, 1000, "scratch/b17_r02_raw_p5.json")
]

for start, end, out_path in slices:
    part_records = records[start:end]
    assert len(part_records) == 100
    with open(out_path, "w", encoding="utf-8") as out:
        json.dump(part_records, out, ensure_ascii=False, indent=2)
    print(f"Dumped {len(part_records)} records to {out_path} ({part_records[0]['hw']} to {part_records[-1]['hw']})")
