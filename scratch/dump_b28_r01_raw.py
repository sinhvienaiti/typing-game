import json

batch_path = "content/english/qa-batches/batch-28.json"
with open(batch_path, "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]
assert len(records) == 5000

for p in range(5):
    start_idx = p * 100
    end_idx = start_idx + 100
    part_slice = records[start_idx:end_idx]
    assert len(part_slice) == 100
    out_file = f"scratch/b28_r01_raw_p{p+1}.json"
    with open(out_file, "w", encoding="utf-8") as out_f:
        json.dump(part_slice, out_f, ensure_ascii=False, indent=2)
    first_id = part_slice[0]['id']
    first_hw = part_slice[0]['hw']
    last_id = part_slice[-1]['id']
    last_hw = part_slice[-1]['hw']
    print(f"Dumped Part {p+1}: [{start_idx}:{end_idx}] ({first_id} {first_hw} -> {last_id} {last_hw}) to {out_file}")
