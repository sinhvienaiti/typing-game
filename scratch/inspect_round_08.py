import json

with open('content/english/qa-batches/batch-02.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

records = data['records'][3500:4000]
print(f"Slice range: index 3500-3999, total={len(records)}")
print(f"First: {records[0]['id']} ({records[0]['hw']})")
print(f"Last: {records[-1]['id']} ({records[-1]['hw']})")

# Let's inspect all 500 records by printing out in groups of 50 to see the words and meanings
for idx, r in enumerate(records):
    hw = r.get('hw', '')
    vi = r.get('vi', '')
    pos = r.get('pos', '')
    # Flags: length > 35, single word or suspicious crawler noise
    flag = ""
    if len(vi) > 35:
        flag += "[LEN>35] "
    if len(vi) < 3:
        flag += "[SHORT] "
    if any(k in vi for k in ["địt", "lồn", "buồi", "cặc", "đĩ", "chó", "đẻ"]):
        flag += "[VULGAR] "
    if any(k in vi for k in ["hàng", "loại", "sự", "cái"]):
        pass
    if flag:
        print(f"{idx+3501}. {r['id']} {hw} ({pos}): {vi} --> {flag}")
