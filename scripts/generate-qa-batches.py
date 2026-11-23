#!/usr/bin/env python3
"""
generate-qa-batches.py
Chia toàn bộ kho từ vựng thành các file Batch độc lập (5,000 từ / file)
phục vụ quy trình QA manual từng dòng, từng file độc lập qua các phiên chat.
"""

import os
import re
import json
import glob
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QA_DIR = ROOT / "content" / "english" / "qa-batches"
QA_DIR.mkdir(parents=True, exist_ok=True)

RE_WIK_META = re.compile(
    r"(?:Dạng|dạng|thì|phân từ|ngôi)\s+.*?(?:của|from)\s+([a-zA-Z\-_]+)",
    re.IGNORECASE
)

# 1. Load all records from shards 001..200
print("Loading all records from shared/dictionary/lexemes/...")
shards = sorted(glob.glob(str(ROOT / "shared" / "dictionary" / "lexemes" / "[0-9][0-9][0-9].json")))
all_recs = []
for s in shards:
    if s.endswith("000.json"):
        continue
    with open(s, "r", encoding="utf-8") as fp:
        all_recs.extend(json.load(fp).get("records", []))

print(f"Loaded {len(all_recs)} records.")

# 2. Build base lemma map for auto-resolving Wiktionary meta glosses
base_map = {}
for r in all_recs:
    hw = r["headword"].lower()
    vi = r.get("vi", "")
    if hw not in base_map and not RE_WIK_META.search(vi) and len(vi) > 1:
        base_sense = vi.split(";")[0].strip()
        base_map[hw] = base_sense

def clean_vi_text(text: str) -> str:
    if not text:
        return ""
    # Strip wiki templates and tags
    t = re.sub(r"\{\{[^\}]*\}\}", "", text)
    t = re.sub(r"[\{\}]", "", t)
    t = re.sub(r"<[^>]+>", "", t)
    # Strip domain tags in parens
    t = re.sub(r"\([^\)]*(?:học|toán|y học|sinh học|quân sự|hàng hải|kỹ thuật|thực vật|động vật)[^\)]*\)", "", t, flags=re.I)
    # Strip unclosed parenthesis at end, e.g. "Drogheda (thành phố Ireland"
    t = re.sub(r"[\(\[][^\)\]]*$", "", t)
    # Strip rogue unmatched parentheses/brackets
    t = re.sub(r"[\(\)\[\]]", "", t)
    # Normalize spaces
    t = unicodedata.normalize("NFC", t)
    t = re.sub(r"\s+", " ", t).strip(",; ")
    return t

def fix_inflected_vi(form: str, base: str, base_vi: str, pos: str) -> str:
    b = base_vi.split(";")[0].strip().rstrip(".")
    if b and b[0].isupper() and not any(w[0].isupper() for w in b.split()[1:]):
        b = b[0].lower() + b[1:]
    if (form.endswith("s") or form.endswith("es")) and pos == "noun":
        if b.startswith("các ") or b.startswith("những "):
            return b
        return f"các {b}"
    if form.endswith("ing"):
        if b.startswith("đang ") or b.startswith("sự "):
            return b
        return f"đang {b}; sự {b}"
    if form.endswith("ed"):
        if b.startswith("đã "):
            return b
        return f"đã {b}"
    return b

def smart_trim(t: str, max_len: int = 38) -> str:
    t = t.strip(";,- ")
    if len(t) <= max_len:
        return t
    if ";" in t:
        parts = [p.strip() for p in t.split(";") if p.strip()]
        cur = parts[0]
        for p in parts[1:]:
            cand = f"{cur}; {p}"
            if len(cand) <= max_len:
                cur = cand
            else:
                break
        if len(cur) <= max_len:
            return cur
    if "," in t:
        parts = [p.strip() for p in t.split(",") if p.strip()]
        cur = parts[0]
        for p in parts[1:]:
            cand = f"{cur}, {p}"
            if len(cand) <= max_len:
                cur = cand
            else:
                break
        if len(cur) <= max_len:
            return cur
    sub = t[:max_len]
    last_space = sub.rfind(" ")
    if last_space > 15:
        return sub[:last_space].strip(";,- ")
    return sub.strip(";,- ")

# 3. Pre-clean all records
print("Applying smart pre-cleaner...")
cleaned_recs = []
sensitive_words = {"vulvar slit", "vulva", "clitoris"}

for r in all_recs:
    hw = r["headword"]
    hw_l = hw.lower()
    if hw_l in sensitive_words:
        continue

    pos = r.get("partsOfSpeech", ["unknown"])[0]
    vi = r.get("vi", "")
    tier = r.get("tier", "expanded")
    ipa = r.get("ipa", "")

    # Fix common core lemmas
    if hw_l == "are":
        vi = "thì, là, ở (số nhiều)"
        pos = "verb"
        tier = "core"
    elif hw_l == "back" and pos == "adj":
        vi = "ở phía sau; lùi lại"
    elif hw_l == "is":
        vi = "thì, là, ở (số ít)"
        pos = "verb"
        tier = "core"

    # Fix Wiktionary grammatical meta descriptions
    m = RE_WIK_META.search(vi)
    if m:
        base = m.group(1).lower()
        if base in base_map:
            vi = fix_inflected_vi(hw_l, base, base_map[base], pos)

    # General cleaning & smart trimming
    vi = clean_vi_text(vi)
    vi = smart_trim(vi, max_len=38)

    cleaned_recs.append({
        "id": r.get("id"),
        "hw": hw,
        "pos": pos,
        "ipa": ipa,
        "vi": vi,
        "cefr": r.get("cefr", "B1"),
        "tier": tier,
        "status": "pending",
        "notes": ""
    })

print(f"Total cleaned records for QA batches: {len(cleaned_recs)}")

# 4. Partition into batches of 5,000 words
BATCH_SIZE = 5000
total_batches = (len(cleaned_recs) + BATCH_SIZE - 1) // BATCH_SIZE
batches_manifest = []

for b_idx in range(total_batches):
    start = b_idx * BATCH_SIZE
    end = min(start + BATCH_SIZE, len(cleaned_recs))
    batch_records = cleaned_recs[start:end]
    batch_num = b_idx + 1
    batch_file = f"batch-{batch_num:02d}.json"
    batch_path = QA_DIR / batch_file

    first_hw = batch_records[0]["hw"]
    last_hw = batch_records[-1]["hw"]

    batch_payload = {
        "batchId": batch_num,
        "batchFile": batch_file,
        "wordCount": len(batch_records),
        "headwordRange": f"{first_hw} ... {last_hw}",
        "status": "pending",
        "reviewedCount": 0,
        "records": batch_records
    }

    with open(batch_path, "w", encoding="utf-8") as fp:
        json.dump(batch_payload, fp, ensure_ascii=False, indent=2)

    batches_manifest.append({
        "batchId": batch_num,
        "file": batch_file,
        "wordCount": len(batch_records),
        "range": f"{first_hw} ... {last_hw}",
        "phase": "Phase 1 (100k Core & Standard)" if batch_num <= 20 else "Phase 2 (100k-200k Expanded & Phrases)",
        "status": "pending"
    })
    print(f"Generated {batch_file}: {len(batch_records)} words ({first_hw} ... {last_hw})")

# 5. Write master INDEX.md and manifest.json
manifest_path = QA_DIR / "manifest.json"
with open(manifest_path, "w", encoding="utf-8") as fp:
    json.dump({"schemaVersion": 1, "totalBatches": total_batches, "batchSize": BATCH_SIZE, "batches": batches_manifest}, fp, ensure_ascii=False, indent=2)

index_md_path = QA_DIR / "INDEX.md"
with open(index_md_path, "w", encoding="utf-8") as fp:
    fp.write("# Kế hoạch & Tiến độ QA Thủ Công Từng Batch (5,000 từ / file)\n\n")
    fp.write("> **Mô hình làm việc:** Mỗi file chứa đúng 5,000 từ độc lập (~1.5 MB). Bạn có thể mở từng phiên chat riêng biệt để xử lý từng batch mà không bị ảnh hưởng hay conflict lẫn nhau.\n\n")
    fp.write("| Batch | File | Số lượng | Dải từ vựng | Nhóm | Trạng thái |\n")
    fp.write("| :---: | :--- | :---: | :--- | :--- | :---: |\n")
    for b in batches_manifest:
        fp.write(f"| {b['batchId']:02d} | `{b['file']}` | {b['wordCount']} | {b['range']} | {b['phase']} | ⏳ `{b['status']}` |\n")

print(f"Successfully generated {total_batches} batches and INDEX.md in {QA_DIR}")
