import json

with open('content/english/qa-batches/batch-03.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

records = data['records']
flags = []
for idx, r in enumerate(records):
    vi = r.get('vi', '')
    hw = r.get('hw', '')
    pos = r.get('pos', '')
    if len(vi) > 35:
        flags.append((idx+1, r['id'], hw, pos, vi, "LEN>35"))
    elif len(vi.strip()) <= 2:
        flags.append((idx+1, r['id'], hw, pos, vi, "VERY_SHORT"))
    elif any(k in vi for k in ["lồn", "cặc", "địt", "đĩ", "buồi", "chó"]):
        flags.append((idx+1, r['id'], hw, pos, vi, "VULGAR"))
    elif any(k in vi for k in ["hàng", "loại", "but see", "see also"]):
        flags.append((idx+1, r['id'], hw, pos, vi, "SUSPICIOUS"))

print(f"Total flags found in Batch 03: {len(flags)}")
for f in flags[:30]:
    print(f)
