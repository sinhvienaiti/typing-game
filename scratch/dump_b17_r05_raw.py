# scratch/dump_b17_r05_raw.py
import json

with open("content/english/qa-batches/batch-17.json", "r", encoding="utf-8") as f:
    d = json.load(f)

records = d["records"]
assert len(records) == 5000

for p, (start, end) in enumerate([(2000, 2100), (2100, 2200), (2200, 2300), (2300, 2400), (2400, 2500)], start=1):
    slice_records = records[start:end]
    assert len(slice_records) == 100
    out_path = f"scratch/b17_r05_raw_p{p}.json"
    with open(out_path, "w", encoding="utf-8") as out_f:
        json.dump(slice_records, out_f, ensure_ascii=False, indent=2)
    print(f"Dumped Part {p}: {slice_records[0]['id']} ({slice_records[0]['hw']}) to {slice_records[-1]['id']} ({slice_records[-1]['hw']})")
