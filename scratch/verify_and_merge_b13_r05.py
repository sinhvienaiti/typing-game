import json

from b13_r05_p1 import items as p1
from b13_r05_p2 import items as p2
from b13_r05_p3 import items as p3
from b13_r05_p4 import items as p4
from b13_r05_p5 import items as p5

all_items = p1 + p2 + p3 + p4 + p5
print(f"Total reviewed items in Round 5: {len(all_items)}")
assert len(all_items) == 500, f"Expected 500 items, got {len(all_items)}"

batch_file = "content/english/qa-batches/batch-13.json"
with open(batch_file, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

raw_slice = batch_data["records"][2000:2500]
assert len(raw_slice) == 500, f"Expected raw slice 500 items, got {len(raw_slice)}"

valid_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det'}
crawler_flags = ["Xem ", "Số nhiều của", "Dạng ", "Viết hoa ", "Dạng thay thế", "một thành phố", "Pasa,", "Pha sa"]

for idx, (rev, raw) in enumerate(zip(all_items, raw_slice)):
    assert rev["id"] == raw["id"], f"ID mismatch at {idx}: {rev['id']} vs {raw['id']}"
    assert rev["hw"] == raw["hw"], f"HW mismatch at {idx}: {rev['hw']} vs {raw['hw']}"
    assert rev["pos"] in valid_pos, f"Bad POS at {idx} ({rev['hw']}): {rev['pos']}"
    assert rev["status"] == "reviewed", f"Status not reviewed at {idx}: {rev['status']}"
    
    ipa = rev["ipa"]
    assert ipa.startswith("/") and ipa.endswith("/"), f"Bad IPA format at {idx} ({rev['hw']}): {ipa}"
    assert ipa.count("/") == 2, f"Bad slash count in IPA at {idx} ({rev['hw']}): {ipa}"
    assert len(ipa) > 2, f"Empty IPA at {idx} ({rev['hw']})"
    inner_ipa = ipa[1:-1]
    assert inner_ipa == inner_ipa.strip(), f"Whitespace in IPA at {idx} ({rev['hw']}): {ipa}"
    
    vi = rev["vi"]
    assert len(vi) > 0, f"Empty vi at {idx} ({rev['hw']})"
    assert len(vi) <= 35, f"vi too long ({len(vi)} chars) at {idx} ({rev['hw']}): {vi}"
    for flag in ["Số nhiều của", "Xem ", "Dạng trần thuật"]:
        assert flag not in vi, f"Crawler artifact '{flag}' in vi at {idx} ({rev['hw']}): {vi}"

print("All 500 records passed strict quality assertions!")

# Merge into batch-13.json
batch_data["records"][2000:2500] = all_items
batch_data["reviewedCount"] = 2500

with open(batch_file, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print("Merged Round 5 into batch-13.json and updated reviewedCount to 2500.")
