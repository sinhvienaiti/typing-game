import json

with open("content/english/qa-batches/batch-20.json") as f:
    batch20 = json.load(f)

# Round 4 covers records 1500 to 1999 (500 records)
r4_records = batch20["records"][1500:2000]
assert len(r4_records) == 500

for p in range(5):
    p_data = r4_records[p*100 : (p+1)*100]
    with open(f"scratch/b20_r04_raw_p{p+1}.json", "w") as f_out:
        json.dump(p_data, f_out, ensure_ascii=False, indent=2)
    print(f"Part {p+1}: {p_data[0]['hw']} ({p_data[0]['id']}) to {p_data[-1]['hw']} ({p_data[-1]['id']})")

print("Dumped all 5 raw parts for Round 4.")
