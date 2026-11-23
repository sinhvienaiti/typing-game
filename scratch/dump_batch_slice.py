import json
import sys

batch_file = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

with open(batch_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

records = data['records'][start:end]
for idx, r in enumerate(records, start=start+1):
    print(f"{idx}. {r['id']} | {r['hw']} | {r['pos']} | {r['vi']} | {r.get('ipa', '')}")
