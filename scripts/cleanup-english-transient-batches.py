from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "content/english/batches/manifest.json"
RELEASE = ROOT / "content/english/releases/2026.10.0.json"
MASTER_PLAN = ROOT / "docs/ENGLISH_LEARNING_CONTENT_SYSTEM_MASTER_PLAN.md"

STALE_BATCH_IDS = {
    "e03.lexical-enrichment",
    "e06.sentence-exercise-scale",
}


def stable_json(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    batches = manifest.get("batches", [])
    found = {batch.get("id") for batch in batches} & STALE_BATCH_IDS
    if found != STALE_BATCH_IDS:
        missing = sorted(STALE_BATCH_IDS - found)
        raise SystemExit(f"transient batch cleanup anchor missing: {missing}")

    manifest["batches"] = [
        batch for batch in batches if batch.get("id") not in STALE_BATCH_IDS
    ]
    if any(
        "content/english/review-queues/" in record_set.get("path", "")
        for batch in manifest["batches"]
        for record_set in batch.get("recordSets", [])
    ):
        raise SystemExit("active batch manifest still contains transient review-queue paths")
    MANIFEST.write_text(stable_json(manifest), encoding="utf-8")

    release = json.loads(RELEASE.read_text(encoding="utf-8"))
    by_state = {}
    for batch in manifest["batches"]:
        state = batch.get("state")
        by_state[state] = by_state.get(state, 0) + 1
    release["batchStates"] = {
        "candidate": by_state.get("candidate", 0),
        "draft": by_state.get("draft", 0),
    }
    RELEASE.write_text(stable_json(release), encoding="utf-8")

    text = MASTER_PLAN.read_text(encoding="utf-8")
    anchor = "- The full 300-topic framework remains the curriculum/taxonomy; **36/300 topics now have reviewed rich runtime bodies**. Further expansion must continue as controlled CEFR slices rather than generating the remaining topics in bulk."
    note = anchor + "\n- Active batch metadata no longer references transient `content/english/review-queues/*` staging files. The superseded E03 lexical-enrichment and E06 sentence-exercise candidate batches were retired from the active manifest after their durable reviewed slices became the source of truth; E10 now validates only reproducible checked-in sources."
    if anchor not in text:
        raise SystemExit("master-plan transient-batch cleanup anchor missing")
    MASTER_PLAN.write_text(text.replace(anchor, note, 1), encoding="utf-8")


if __name__ == "__main__":
    main()
