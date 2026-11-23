# -*- coding: utf-8 -*-
import json
import re

import sys
sys.path.insert(0, ".")

from scratch.b17_r01_p1 import part1
from scratch.b17_r01_p2 import part2
from scratch.b17_r01_p3 import part3
from scratch.b17_r01_p4 import reviewed_entries as part4
from scratch.b17_r01_p5 import reviewed_entries as part5

round1 = part1 + part2 + part3 + part4 + part5
assert len(round1) == 500, f"Expected 500 entries, got {len(round1)}"

valid_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}
crawler_patterns = ["Số nhiều của", "Xem ", "Dạng ", "Viết tắt", "Động từ chia", "%%"]

for idx, e in enumerate(round1):
    expected_id = f"lex.en.100k.{80002 + idx:06d}"
    assert e["id"] == expected_id, f"[{idx}] ID mismatch: {e['id']} != {expected_id}"
    assert e["pos"] in valid_pos, f"[{idx}] Invalid pos: {e['pos']} in {e['hw']}"
    assert e["ipa"].startswith("/") and e["ipa"].endswith("/"), f"[{idx}] Invalid IPA format: {e['ipa']} in {e['hw']}"
    assert e["ipa"].count("/") == 2, f"[{idx}] Slashes count != 2 in IPA: {e['ipa']} in {e['hw']}"
    assert not e["ipa"].startswith("/ ") and not e["ipa"].endswith(" /"), f"[{idx}] Boundary spaces in IPA: {e['ipa']}"
    assert len(e["vi"]) <= 35, f"[{idx}] vi too long ({len(e['vi'])} chars): {e['vi']} in {e['hw']}"
    assert len(e["vi"]) > 0, f"[{idx}] Empty vi: {e['hw']}"
    assert e["status"] == "reviewed", f"[{idx}] Invalid status: {e['status']} in {e['hw']}"
    for pat in crawler_patterns:
        assert pat not in e["vi"], f"[{idx}] Crawler pattern '{pat}' found in vi: {e['vi']}"

print("Round 1 (500 words) all passed QA validation!")

# Load batch-17.json
with open("content/english/qa-batches/batch-17.json", "r", encoding="utf-8") as f:
    batch_data = json.load(f)

records = batch_data["records"]
assert len(records) == 5000, f"Expected 5000 records in batch-17, got {len(records)}"

for i in range(500):
    assert records[i]["id"] == round1[i]["id"], f"Record {i} ID mismatch: {records[i]['id']} != {round1[i]['id']}"
    assert records[i]["hw"].lower() == round1[i]["hw"].lower(), f"Record {i} HW mismatch: {records[i]['hw']} != {round1[i]['hw']}"
    records[i]["pos"] = round1[i]["pos"]
    records[i]["ipa"] = round1[i]["ipa"]
    records[i]["vi"] = round1[i]["vi"]
    records[i]["status"] = "reviewed"

# Recount reviewed
reviewed_count = sum(1 for w in records if w["status"] == "reviewed")
batch_data["reviewedCount"] = reviewed_count
print(f"Updated batch-17 reviewedCount: {reviewed_count}/5000")

with open("content/english/qa-batches/batch-17.json", "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print("Saved updated content/english/qa-batches/batch-17.json successfully!")
