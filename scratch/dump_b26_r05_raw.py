import json

with open('content/english/qa-batches/batch-26.json', 'r', encoding='utf-8') as f:
    batch = json.load(f)

records = batch['records'][2000:2500]
assert len(records) == 500, f"Expected 500 records, got {len(records)}"

for i in range(5):
    p_records = records[i*100:(i+1)*100]
    with open(f'scratch/b26_r05_raw_p{i+1}.json', 'w', encoding='utf-8') as pf:
        json.dump(p_records, pf, ensure_ascii=False, indent=2)

print("Dumped b26_r05_raw_p1 through p5 successfully")
