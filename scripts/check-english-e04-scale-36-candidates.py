#!/usr/bin/env python3
from __future__ import annotations

import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPLY = ROOT / "scripts/apply-english-e04-focused-scale-36.py"
scope = runpy.run_path(str(APPLY), run_name="e04_scale36_preflight")

manifest = scope["read_json"](scope["MANIFEST_PATH"])
normalized_key = scope["normalized_key"]
jaccard = scope["jaccard"]
threshold = scope["NEAR_DUP_THRESHOLD"]
candidates = scope["COLLOCATIONS"]

existing = []
ids = set()
for batch in manifest.get("batches", []):
    if batch.get("phase") != "E04" or batch.get("category") != "phrases":
        continue
    for record_set in batch.get("recordSets", []):
        records = scope["read_json"](ROOT / record_set["path"]).get("records", [])
        for record in records:
            rid = record.get("id")
            if rid in ids:
                raise RuntimeError(f"existing duplicate E04 record id: {rid}")
            ids.add(rid)
            value = record.get("text") or record.get("pattern") or ""
            if value:
                existing.append((rid, value))

exact_map = {}
for rid, text in existing:
    exact_map.setdefault(normalized_key(text), []).append(rid)

conflicts = []
for index, spec in enumerate(candidates, start=1041):
    text = spec[0]
    key = normalized_key(text)
    exact = exact_map.get(key, [])
    near = []
    for old_id, old_text in existing:
        score = jaccard(text, old_text)
        if score >= threshold and normalized_key(old_text) != key:
            near.append({"id": old_id, "text": old_text, "score": round(score, 3)})
    if exact or near:
        conflicts.append({"candidateId": f"col.{index:08d}", "text": text, "exactIds": exact, "near": near})

for left in range(len(candidates)):
    for right in range(left + 1, len(candidates)):
        score = jaccard(candidates[left][0], candidates[right][0])
        if score >= threshold:
            conflicts.append({
                "candidateId": f"col.{1041 + left:08d}",
                "text": candidates[left][0],
                "insideBatchNear": {
                    "candidateId": f"col.{1041 + right:08d}",
                    "text": candidates[right][0],
                    "score": round(score, 3),
                },
            })

print(json.dumps({
    "candidateCount": len(candidates),
    "existingE04Texts": len(existing),
    "threshold": threshold,
    "conflictCount": len(conflicts),
    "conflicts": conflicts,
}, ensure_ascii=False, indent=2))
if conflicts:
    raise SystemExit(1)
