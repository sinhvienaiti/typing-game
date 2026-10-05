from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET_PATH = ROOT / "content/english/targets/long-term.json"

PERSISTENT_SOURCES = {
    "common-mistakes": [
        {"path": "content/english/sentences/e06-reviewed-common-mistakes.json", "collection": "records"},
        {"path": "content/english/sentences/e05-scale-a1-01-common-mistakes.json", "collection": "records"},
        {"path": "content/english/sentences/e05-scale-a1-02-common-mistakes.json", "collection": "records"},
        {"path": "content/english/sentences/e05-scale-a1-03-common-mistakes.json", "collection": "records"},
        {"path": "content/english/sentences/e05-scale-a1-04-common-mistakes.json", "collection": "records"},
    ],
    "example-sentences": [
        {"path": "content/english/sentences/pilot-sentences.json", "collection": "records"},
        {"path": "content/english/sentences/e05-scale-a1-01-sentences.json", "collection": "records"},
        {"path": "content/english/sentences/e05-scale-a1-02-sentences.json", "collection": "records"},
        {"path": "content/english/sentences/e05-scale-a1-03-sentences.json", "collection": "records"},
        {"path": "content/english/sentences/e05-scale-a1-04-sentences.json", "collection": "records"},
        {"path": "content/english/sentences/e06-reviewed-typing-text-sentences.json", "collection": "records"},
        {"path": "content/english/sentences/e06-reviewed-translation-sentences.json", "collection": "records"},
    ],
    "translation-pairs": [
        {"path": "content/english/sentences/e06-reviewed-translations.json", "collection": "records"},
    ],
    "cloze-exercises": [
        {"path": "content/english/sentences/e06-reviewed-cloze.json", "collection": "records"},
    ],
    "sentence-transformations": [
        {
            "path": "content/english/sentences/e06-reviewed-exercises.json",
            "collection": "records",
            "filterField": "type",
            "filterValues": ["transformation"],
        },
    ],
    "dialogue-examples": [
        {"path": "content/english/sentences/e06-reviewed-dialogues.json", "collection": "records"},
    ],
}


def stable_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def main() -> None:
    doc = json.loads(TARGET_PATH.read_text(encoding="utf-8"))
    targets = {target.get("id"): target for target in doc.get("targets", [])}
    missing = sorted(set(PERSISTENT_SOURCES) - set(targets))
    if missing:
        raise SystemExit(f"missing locked E11 targets: {missing}")

    retired_prefix = "content/english/review-queues/"
    for target_id, sources in PERSISTENT_SOURCES.items():
        target = targets[target_id]
        old_sources = target.get("sources", [])
        if not any(str(source.get("path", "")).startswith(retired_prefix) for source in old_sources):
            if old_sources != sources:
                raise SystemExit(
                    f"{target_id}: sources already changed by another worker; refusing to overwrite"
                )
        target["sources"] = sources

    for target in doc.get("targets", []):
        for source in target.get("sources", []):
            if str(source.get("path", "")).startswith(retired_prefix):
                raise SystemExit(
                    f"retired review-queue source remains for {target.get('id')}: {source.get('path')}"
                )

    TARGET_PATH.write_text(stable_json(doc), encoding="utf-8")


if __name__ == "__main__":
    main()
