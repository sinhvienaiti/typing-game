import json
import sys

def main():
    parts = []
    for p in range(1, 6):
        path = f"scratch/b22_r10_p{p}.json"
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if len(data) != 100:
                print(f"Error: {path} has {len(data)} items, expected 100")
                sys.exit(1)
            parts.extend(data)

    if len(parts) != 500:
        print(f"Error: total items = {len(parts)}, expected 500")
        sys.exit(1)

    print("Checking 500 reviewed items for Round 10...")
    errors = []
    valid_pos = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"}
    required_keys = {"id", "hw", "pos", "ipa", "vi", "cefr", "tier", "status", "notes"}

    for idx, item in enumerate(parts):
        item_id = item.get("id", f"idx_{idx}")
        hw = item.get("hw", "")
        vi = item.get("vi", "")
        ipa = item.get("ipa", "")
        pos = item.get("pos", "")
        status = item.get("status", "")

        # Check keys
        extra_keys = set(item.keys()) - required_keys
        missing_keys = required_keys - set(item.keys())
        if extra_keys or missing_keys:
            errors.append(f"[{item_id}] Key mismatch: extra={extra_keys}, missing={missing_keys}")

        # Check status
        if status != "reviewed":
            errors.append(f"[{item_id}] Status is '{status}', expected 'reviewed'")

        # Check length of vi
        if not vi or len(vi) > 35:
            errors.append(f"[{item_id}] ({hw}) vi length invalid: {len(vi)} chars ('{vi}')")

        # Check IPA
        if not (ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2 and len(ipa) > 2):
            errors.append(f"[{item_id}] ({hw}) IPA invalid: '{ipa}'")
        if " /" in ipa or "/ " in ipa:
            errors.append(f"[{item_id}] ({hw}) IPA contains space near boundary: '{ipa}'")

        # Check pos
        if pos not in valid_pos:
            errors.append(f"[{item_id}] ({hw}) Invalid POS: '{pos}'")

        # Check crawler artifacts
        for artifact in ["Số nhiều của", "Xem ", "Dạng ", "Viết tắt", "Động từ chia", "%%"]:
            if artifact in vi:
                errors.append(f"[{item_id}] ({hw}) vi contains crawler artifact: '{artifact}'")

    if errors:
        print(f"FAIL: {len(errors)} errors found:")
        for e in errors[:30]:
            print("  ", e)
        if len(errors) > 30:
            print(f"  ... and {len(errors) - 30} more")
        sys.exit(1)

    print("ALL 500 items PASSED validation!")

    # Merge into batch-22.json
    batch_file = "content/english/qa-batches/batch-22.json"
    with open(batch_file, "r", encoding="utf-8") as f:
        batch_data = json.load(f)

    records = batch_data["records"]
    start_idx = 4500
    end_idx = 5000

    for i in range(500):
        target_idx = start_idx + i
        raw_rec = records[target_idx]
        rev_rec = parts[i]

        if raw_rec["id"] != rev_rec["id"]:
            print(f"Error: ID mismatch at index {target_idx}: {raw_rec['id']} vs {rev_rec['id']}")
            sys.exit(1)
        if raw_rec["hw"] != rev_rec["hw"]:
            print(f"Error: Headword mismatch at index {target_idx}: {raw_rec['hw']} vs {rev_rec['hw']}")
            sys.exit(1)

        records[target_idx] = rev_rec

    batch_data["reviewedCount"] = end_idx
    batch_data["status"] = "completed"

    with open(batch_file, "w", encoding="utf-8") as f:
        json.dump(batch_data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Successfully merged 500 records into {batch_file}.")
    print(f"Batch 22 status is now '{batch_data['status']}', reviewedCount = {batch_data['reviewedCount']}.")

if __name__ == "__main__":
    main()
