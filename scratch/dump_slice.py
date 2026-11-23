import json
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

with open('content/english/qa-batches/batch-02.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

records = data['records'][start:end]
for idx, r in enumerate(records, start=start+1):
    print(f"{idx}. {r['id']} | {r['hw']} | {r['pos']} | {r['vi']} | {r.get('ipa', '')}")
