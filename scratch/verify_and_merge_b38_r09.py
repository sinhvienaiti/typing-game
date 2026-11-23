import json

VALID_POS = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}
BAD_PREFIXES = ("các ", "những ", "Số nhiều của", "Xem ", "Cách viết khác", "Dạng ", "Thgt ")

with open("content/english/qa-batches/batch-38.json") as f:
    batch = json.load(f)

updates = {}
for p in range(1, 6):
    part = json.load(open(f"scratch/b38_r09_p{p}.json"))
    assert len(part) == 100, f"Part {p} len={len(part)}"
    for sid, hw, pos, ipa, vi in part:
        assert sid not in updates, f"Dup sid {sid}"
        assert pos in VALID_POS, f"Bad pos {pos} for {sid}"
        assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad ipa {ipa} for {sid}"
        assert 0 < len(vi) <= 35, f"Bad vi len {len(vi)} ({vi}) for {sid}"
        assert "/" not in vi, f"Slash in vi ({vi}) for {sid}"
        for pref in BAD_PREFIXES:
            assert not vi.startswith(pref), f"Bad prefix in {sid}: {vi}"
        updates[sid] = (hw, pos, ipa, vi)

assert len(updates) == 500
matched = 0
for rec in batch["records"][4000:4500]:
    sid = rec["id"].split(".")[-1]
    hw, pos, ipa, vi = updates[sid]
    assert rec["hw"] == hw, f"HW mismatch {sid}: {rec['hw']} vs {hw}"
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    matched += 1

assert matched == 500
batch["reviewedCount"] = 4500
batch["status"] = "in-progress"
with open("content/english/qa-batches/batch-38.json", "w") as f:
    json.dump(batch, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("Merged batch-38 round 9 (4500/5000) OK")
