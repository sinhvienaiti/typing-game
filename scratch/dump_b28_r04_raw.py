import json

with open("content/english/qa-batches/batch-28.json", "r", encoding="utf-8") as f:
    batch = json.load(f)

records = batch["records"]
assert len(records) == 5000

# Round 4 is records 1500 to 2000
r4 = records[1500:2000]
assert len(r4) == 500
assert r4[0]["id"] == "lex.en.200k.036502"
assert r4[-1]["id"] == "lex.en.200k.037001"

for p in range(5):
    part = r4[p*100 : (p+1)*100]
    assert len(part) == 100
    with open(f"scratch/b28_r04_raw_p{p+1}.json", "w", encoding="utf-8") as f_out:
        json.dump(part, f_out, ensure_ascii=False, indent=2)

print("Round 4 raw parts 1-5 dumped successfully!")
