import json

with open("content/english/qa-batches/batch-14.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]

slices = [
    (3000, 3100, "scratch/b14_r07_raw_p1.json"),
    (3100, 3200, "scratch/b14_r07_raw_p2.json"),
    (3200, 3300, "scratch/b14_r07_raw_p3.json"),
    (3300, 3400, "scratch/b14_r07_raw_p4.json"),
    (3400, 3500, "scratch/b14_r07_raw_p5.json"),
]

for start, end, outpath in slices:
    part = records[start:end]
    with open(outpath, "w", encoding="utf-8") as out:
        json.dump(part, out, ensure_ascii=False, indent=2)
    print(f"Wrote {len(part)} records ({part[0]['id']} - {part[-1]['id']}, {part[0]['hw']} - {part[-1]['hw']}) to {outpath}")
