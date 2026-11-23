import json

with open("content/english/qa-batches/batch-20.json") as f:
    batch20 = json.load(f)

# Round 3 covers records 1000 to 1499 (500 records)
r3_records = batch20["records"][1000:1500]
assert len(r3_records) == 500

for p in range(5):
    p_data = r3_records[p*100 : (p+1)*100]
    with open(f"scratch/b20_r03_raw_p{p+1}.json", "w") as f_out:
        json.dump(p_data, f_out, ensure_ascii=False, indent=2)
    print(f"Part {p+1}: {p_data[0]['hw']} ({p_data[0]['id']}) to {p_data[-1]['hw']} ({p_data[-1]['id']})")

print("Dumped all 5 raw parts for Round 3.")
