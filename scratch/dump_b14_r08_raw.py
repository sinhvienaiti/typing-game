import json

with open("content/english/qa-batches/batch-14.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]

slices = [
    (3500, 3600, "scratch/b14_r08_raw_p1.json"),
    (3600, 3700, "scratch/b14_r08_raw_p2.json"),
    (3700, 3800, "scratch/b14_r08_raw_p3.json"),
    (3800, 3900, "scratch/b14_r08_raw_p4.json"),
    (3900, 4000, "scratch/b14_r08_raw_p5.json"),
]

for start, end, outpath in slices:
    part = records[start:end]
    with open(outpath, "w", encoding="utf-8") as out:
        json.dump(part, out, ensure_ascii=False, indent=2)
    print(f"Wrote {len(part)} records ({part[0]['id']} - {part[-1]['id']}, {part[0]['hw']} - {part[-1]['hw']}) to {outpath}")
