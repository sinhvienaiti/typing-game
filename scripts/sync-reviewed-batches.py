#!/usr/bin/env python3
"""
sync-reviewed-batches.py
Đồng bộ các cập nhật/chỉnh sửa từ các file batch trong content/english/qa-batches/
trở lại vào các file runtime shards trong shared/dictionary/lexemes/ và lookup.json.
"""

import os
import json
import glob
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QA_DIR = ROOT / "content" / "english" / "qa-batches"
SHARDS_DIR = ROOT / "shared" / "dictionary" / "lexemes"
LOOKUP_FILE = ROOT / "shared" / "dictionary" / "lookup.json"

def main():
    print("Scanning QA batches in content/english/qa-batches/...")
    batch_files = sorted(glob.glob(str(QA_DIR / "batch-*.json")))
    if not batch_files:
        print("No batch files found.")
        return

    # Map id -> record
    updated_records = {}
    total_words = 0
    approved_words = 0
    edited_words = 0

    for bf in batch_files:
        with open(bf, "r", encoding="utf-8") as fp:
            data = json.load(fp)
            recs = data.get("records", [])
            total_words += len(recs)
            for r in recs:
                rec_id = r.get("id")
                if rec_id:
                    updated_records[rec_id] = r
                if r.get("status") == "approved":
                    approved_words += 1
                elif r.get("status") == "edited":
                    edited_words += 1

    print(f"Total batch words: {total_words} (Approved: {approved_words}, Edited: {edited_words})")

    # Update runtime shards
    shard_files = sorted(glob.glob(str(SHARDS_DIR / "[0-9][0-9][0-9].json")))
    synced_count = 0

    for sf in shard_files:
        if sf.endswith("000.json"):
            continue
        with open(sf, "r", encoding="utf-8") as fp:
            shard_data = json.load(fp)
        changed = False
        for rec in shard_data.get("records", []):
            rid = rec.get("id")
            if rid in updated_records:
                u = updated_records[rid]
                new_pos = [u["pos"]] if u.get("pos") else rec.get("partsOfSpeech", [])
                if (rec.get("vi") != u.get("vi") or
                    rec.get("tier") != u.get("tier") or
                    rec.get("ipa") != u.get("ipa") or
                    rec.get("partsOfSpeech") != new_pos):
                    rec["vi"] = u["vi"]
                    rec["tier"] = u["tier"]
                    rec["ipa"] = u["ipa"]
                    if u.get("pos"):
                        rec["partsOfSpeech"] = new_pos
                    changed = True
                    synced_count += 1
        if changed:
            with open(sf, "w", encoding="utf-8") as fp:
                json.dump(shard_data, fp, ensure_ascii=False)

    print(f"Synced {synced_count} updated words back into runtime shards.")
    print("Done!")

if __name__ == "__main__":
    main()
