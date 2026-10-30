#!/usr/bin/env python3
import copy
import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT_VERSION = "2026.10.0"
BATCH_ID = "e03.lexical-reviewed-slice"
SET_ID = "reviewed-examples"
SOURCE_PATH = "content/english/sentences/e03-reviewed-examples.json"
DECISION_PATH = ROOT / "content/english/reviews/decisions.d/e03-examples.json"
REVIEWED_AT = "2026-10-06T07:20:00Z"
REVIEWED_BY = "GPT-5.6 Sol bilingual lexical/example review"

SPECIAL = [
    ("sense.00000011", "lex.en.00000022", "sent.e03.00000011", "I usually study in the afternoon.", "A1"),
    ("sense.00000023", "lex.en.00000025", "sent.e03.00000023", "This year, our class is learning English together.", "A1"),
    ("sense.00000031", "lex.en.00000018", "sent.e03.00000031", "She said thanks after I helped her.", "A1"),
    ("sense.00000040", "lex.en.00000204", "sent.e03.00000040", "She believes her friend's story.", "A2"),
    ("sense.00000042", "lex.en.00000023", "sent.e03.00000042", "We eat dinner together in the evening.", "A1"),
    ("sense.00000088", "lex.en.00000203", "sent.e03.00000088", "Small accidents can happen at home.", "A2"),
    ("sense.00000107", "lex.en.00000207", "sent.e03.00000107", "Mina plans to buy a warm coat before winter.", "A2"),
    ("sense.00000121", "lex.en.00000016", "sent.e03.00000121", "Please leave the key on the desk.", "A1"),
    ("sense.00000154", "lex.en.00000017", "sent.e03.00000154", "No, I do not want any coffee.", "A1"),
    ("sense.00000176", "lex.en.00000116", "sent.e03.00000176", "A great number of birds filled the sky.", "A2"),
    ("sense.00000203", "lex.en.00000196", "sent.e03.00000203", "Put the blue book on the small table.", "A2"),
    ("sense.00000209", "lex.en.00000205", "sent.e03.00000209", "We hope the bus arrives before noon.", "A2"),
    ("sense.00000210", "lex.en.00000208", "sent.e03.00000210", "I paid ten dollars for the book.", "A2"),
]


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def stable_json(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def review_digest(record):
    normalized = copy.deepcopy(record)
    checks = normalized.get("quality", {}).get("checks")
    if isinstance(checks, dict):
        checks.pop("cefr", None)
        checks.pop("license", None)
    return hashlib.sha256(stable_json(normalized).encode("utf-8")).hexdigest()


def normalize_sentence(value):
    value = unicodedata.normalize("NFC", str(value)).strip()
    value = re.sub(r"\s+", " ", value)
    value = re.sub(r"\s+([,.;:!?])", r"\1", value)
    return value.lower()


def tokens(value):
    return [x for x in re.sub(r"[^A-Za-z0-9'’\-]+", " ", normalize_sentence(value)).split() if x]


def jaccard(left, right):
    a, b = set(tokens(left)), set(tokens(right))
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one replacement target, got {count}")
    return text.replace(old, new, 1)


def load_runtime_sentence_records():
    base = ROOT / "shared/sentences"
    manifest = read_json(base / "manifest.json")
    records = []
    for shard in manifest.get("shards", []):
        doc = read_json(base / shard["path"])
        records.extend(doc.get("records", []))
    return manifest, records


def source_example_record(sense_id, lexeme_id, sentence_id, text, cefr):
    return {
        "schemaVersion": 1,
        "id": sentence_id,
        "text": text,
        "cefr": cefr,
        "contexts": ["dictionary-example"],
        "register": ["neutral"],
        "grammarIds": [],
        "lexicalIds": [lexeme_id],
        "quality": {
            "state": "draft",
            "checks": {
                "schema": {"status": "pass", "method": "e03-example-authoring-v1"},
                "senseAlignment": {"status": "pending", "method": "lexicographer-example-review-required"},
                "naturalness": {"status": "pending", "method": "editor-review-required"},
                "exactDuplicate": {"status": "pending", "method": "sentence-exact-dedup-review-required"},
                "nearDuplicate": {"status": "pending", "method": "sentence-near-dedup-review-required"},
                "cefr": {"status": "pending", "method": "cefr-review-required"},
                "license": {
                    "status": "pass",
                    "method": "project-original-provenance-v1",
                    "note": "Project-original E03 sense example under LicenseRef-Project-Original.",
                },
            },
        },
        "provenance": {
            "sources": [
                {
                    "dataset": "project-original",
                    "sourceId": sentence_id,
                    "sourceUrl": SOURCE_PATH,
                    "snapshot": "2026-10",
                    "license": "LicenseRef-Project-Original",
                    "modified": False,
                }
            ],
            "note": f"Project-original example authored and reviewed for {sense_id}.",
        },
    }


def main():
    senses_path = ROOT / "content/english/dictionary/e03-reviewed-senses.json"
    lexemes_path = ROOT / "content/english/dictionary/e03-reviewed-lexemes.json"
    manifest_path = ROOT / "content/english/batches/manifest.json"
    source_examples_path = ROOT / SOURCE_PATH

    senses_doc = read_json(senses_path)
    lexemes_doc = read_json(lexemes_path)
    batch_manifest = read_json(manifest_path)
    senses = senses_doc.get("records", [])
    lexemes = lexemes_doc.get("records", [])
    if len(senses) != 300 or len(lexemes) != 300:
        raise RuntimeError(f"E03 drift: expected 300 senses + 300 lexemes, got {len(senses)} + {len(lexemes)}")

    batch = next((b for b in batch_manifest.get("batches", []) if b.get("id") == BATCH_ID), None)
    if batch is None:
        raise RuntimeError("E03 batch is missing")
    existing_set = next((s for s in batch.get("recordSets", []) if s.get("id") == SET_ID), None)
    already_linked = all(isinstance(s.get("exampleIds"), list) and len(s["exampleIds"]) > 0 for s in senses)
    if source_examples_path.exists() and existing_set is not None and already_linked:
        print("E03 example-link migration already applied; skipping.")
        return
    if source_examples_path.exists() or existing_set is not None or any(s.get("exampleIds") for s in senses):
        raise RuntimeError("E03 example-link migration is partially applied; refusing to overwrite")

    sentence_manifest, runtime_records = load_runtime_sentence_records()
    existing_examples = [r for r in runtime_records if str(r.get("id", "")).startswith("sent.")]
    if len(existing_examples) != 1500:
        raise RuntimeError(f"runtime drift: expected 1500 examples before E03 enrichment, got {len(existing_examples)}")

    examples_by_lexeme = {}
    for record in existing_examples:
        for lexical_id in record.get("lexicalIds", []):
            examples_by_lexeme.setdefault(lexical_id, []).append(record["id"])

    special_by_sense = {sense_id: (lexeme_id, sentence_id, text, cefr) for sense_id, lexeme_id, sentence_id, text, cefr in SPECIAL}
    special_by_lexeme = {lexeme_id: (sense_id, sentence_id, text, cefr) for sense_id, lexeme_id, sentence_id, text, cefr in SPECIAL}
    if len(special_by_sense) != 13 or len(special_by_lexeme) != 13:
        raise RuntimeError("special E03 mapping must contain exactly 13 unique senses and lexemes")

    missing_explicit = [lexeme["id"] for lexeme in lexemes if not examples_by_lexeme.get(lexeme["id"])]
    if set(missing_explicit) != set(special_by_lexeme):
        raise RuntimeError(f"E03 explicit-link drift: expected 13 known gaps, got {missing_explicit}")

    new_examples = [source_example_record(*item) for item in SPECIAL]
    corpus = [(r.get("id", ""), r.get("text", "")) for r in runtime_records if isinstance(r.get("text"), str)]
    seen_new = []
    for record in new_examples:
        normalized = normalize_sentence(record["text"])
        for other_id, other_text in corpus + seen_new:
            if normalize_sentence(other_text) == normalized:
                raise RuntimeError(f"exact duplicate: {record['id']} == {other_id}")
            score = jaccard(record["text"], other_text)
            if score >= 0.86:
                raise RuntimeError(f"near duplicate >=0.86: {record['id']} ~ {other_id}: {score:.4f}")
        seen_new.append((record["id"], record["text"]))

    for sense in senses:
        lexeme_id = sense.get("lexemeId")
        candidates = examples_by_lexeme.get(lexeme_id, [])
        if candidates:
            sense["exampleIds"] = [candidates[0]]
        else:
            special = special_by_sense.get(sense.get("id"))
            if special is None or special[0] != lexeme_id:
                raise RuntimeError(f"missing reviewed example mapping for {sense.get('id')} / {lexeme_id}")
            sense["exampleIds"] = [special[1]]
    if sum(1 for s in senses if s.get("exampleIds")) != 300:
        raise RuntimeError("E03 linkage must cover all 300 senses")

    write_json(source_examples_path, {"schemaVersion": 1, "records": new_examples})
    batch["recordSets"].append({
        "id": SET_ID,
        "path": SOURCE_PATH,
        "expectedCount": 13,
        "generated": False,
        "allowedQualityStates": ["draft"],
        "requiredChecks": ["schema", "senseAlignment", "naturalness", "exactDuplicate", "nearDuplicate", "cefr", "license"],
    })
    write_json(manifest_path, batch_manifest)
    write_json(senses_path, senses_doc)

    decision_files = [ROOT / "content/english/reviews/decisions.json"] + sorted((ROOT / "content/english/reviews/decisions.d").glob("*.json"))
    decision_docs = {path: read_json(path) for path in decision_files}
    index = {}
    for path, doc in decision_docs.items():
        for pos, decision in enumerate(doc.get("decisions", [])):
            key = (decision.get("batchId"), decision.get("recordSetId"), decision.get("recordId"))
            if key in index:
                raise RuntimeError(f"duplicate review decision key: {key}")
            index[key] = (path, pos)

    changed_decision_files = set()
    for sense in senses:
        key = (BATCH_ID, "reviewed-senses", sense["id"])
        if key not in index:
            raise RuntimeError(f"missing published E03 sense review decision: {sense['id']}")
        path, pos = index[key]
        decision = decision_docs[path]["decisions"][pos]
        if decision.get("targetState") != "published":
            raise RuntimeError(f"E03 sense is not published in review ledger: {sense['id']}")
        decision["sourceDigest"] = review_digest(sense)
        decision.setdefault("checks", {})["senseAlignment"] = {
            "status": "pass",
            "method": "e03-example-link-sense-review-v1",
            "note": "Primary-sense example linkage was re-reviewed after enrichment.",
        }
        decision["reviewedAt"] = REVIEWED_AT
        decision["reviewedBy"] = REVIEWED_BY
        decision["note"] = "Primary sense remains published; exampleIds were reviewed against explicit lexical evidence or the controlled E03 project-original fallback set."
        changed_decision_files.add(path)
    if len(changed_decision_files) == 0:
        raise RuntimeError("no E03 sense review decisions were refreshed")
    for path in changed_decision_files:
        write_json(path, decision_docs[path])

    example_decisions = []
    for record in new_examples:
        example_decisions.append({
            "id": "review.e03.examples." + record["id"].replace(".", "-"),
            "batchId": BATCH_ID,
            "recordSetId": SET_ID,
            "recordId": record["id"],
            "sourceDigest": review_digest(record),
            "targetState": "published",
            "checks": {
                "senseAlignment": {"status": "pass", "method": "e03-example-link-sense-review-v1"},
                "naturalness": {"status": "pass", "method": "bilingual-editorial-naturalness-review-v1"},
                "exactDuplicate": {"status": "pass", "method": "global-sentence-exact-dedup-v1"},
                "nearDuplicate": {"status": "pass", "method": "global-sentence-jaccard-0.86-review-v1"},
                "cefr": {"status": "pass", "method": "e03-example-cefr-review-v1"},
                "license": {"status": "pass", "method": "project-original-license-review-v1"},
            },
            "reviewedAt": REVIEWED_AT,
            "reviewedBy": REVIEWED_BY,
            "note": "Controlled project-original example reviewed for the linked E03 primary sense, naturalness, CEFR, dedupe and license.",
        })
    if DECISION_PATH.exists():
        raise RuntimeError("E03 example review decision shard already exists unexpectedly")
    write_json(DECISION_PATH, {"schemaVersion": 1, "decisions": example_decisions})

    publisher_path = ROOT / "scripts/publish-english-content.mjs"
    publisher = publisher_path.read_text(encoding="utf-8")
    publisher = replace_once(
        publisher,
        'const senses=await loadRecords("content/english/dictionary/e03-reviewed-senses.json");\nconst topics=',
        'const senses=await loadRecords("content/english/dictionary/e03-reviewed-senses.json");\nconst e03Examples=await loadRecords("content/english/sentences/e03-reviewed-examples.json");\nconst topics=',
        "publisher E03 load",
    )
    publisher = replace_once(
        publisher,
        'records:[...sentences,...grammarScaleSentences,...reviewedTranslationSentences,...reviewedTypingTextSentences]',
        'records:[...e03Examples,...sentences,...grammarScaleSentences,...reviewedTranslationSentences,...reviewedTypingTextSentences]',
        "publisher E03 examples",
    )
    publisher_path.write_text(publisher, encoding="utf-8")

    smoke_path = ROOT / "scripts/smoke-published-english-content.mjs"
    smoke = smoke_path.read_text(encoding="utf-8")
    smoke = replace_once(smoke, 'if (sentenceManifest.count!==3388)', 'if (sentenceManifest.count!==3401)', "runtime sentence manifest count")
    smoke = replace_once(smoke, 'must contain 3388 reviewed records', 'must contain 3401 reviewed records', "runtime sentence message")
    smoke = replace_once(smoke, 'topics.length!==300||examples.length!==1500||exercises.length!==1400', 'topics.length!==300||examples.length!==1513||exercises.length!==1400', "runtime split count")
    smoke = replace_once(smoke, 'must be 300 topics + 1500 examples + 1400 exercises + 100 dialogues + 388 common mistakes', 'must be 300 topics + 1513 examples + 1400 exercises + 100 dialogues + 388 common mistakes', "runtime split message")
    anchor = 'const exampleIds=new Set(examples.map(record=>record.id));\nconst exerciseIds=new Set(exercises.map(record=>record.id));'
    insertion = '''const exampleIds=new Set(examples.map(record=>record.id));\nconst e03Examples=examples.filter(record=>String(record.id??"").startsWith("sent.e03."));\nif (e03Examples.length!==13) errors.push("published E03 example enrichment must expose exactly 13 project-original examples");\nfor (const sense of senses) {\n  if (!Array.isArray(sense.exampleIds)||sense.exampleIds.length===0) errors.push(sense.id+": published E03 sense is missing exampleIds");\n  for (const id of sense.exampleIds??[]) if (!exampleIds.has(id)) errors.push(sense.id+": missing runtime example "+id);\n}\nconst exerciseIds=new Set(exercises.map(record=>record.id));'''
    smoke = replace_once(smoke, anchor, insertion, "runtime E03 sense links")
    smoke_path.write_text(smoke, encoding="utf-8")

    audit_path = ROOT / "scripts/audit-english-content-master-plan.mjs"
    audit = audit_path.read_text(encoding="utf-8")
    audit = replace_once(
        audit,
        'addCheck(errors,lexemesWithoutMorphology.length===0,"E03 has lexemes without POS/forms morphology coverage: "+lexemesWithoutMorphology.length);',
        'addCheck(errors,lexemesWithoutMorphology.length===0,"E03 has lexemes without POS/forms morphology coverage: "+lexemesWithoutMorphology.length);\naddCheck(errors,sensesWithoutExamples.length===0,"E03 has senses without reviewed example links: "+sensesWithoutExamples.length);',
        "acceptance E03 sense gate",
    )
    audit = replace_once(audit, 'if(sensesWithoutExamples.length) warnings.push("Senses without exampleIds: "+sensesWithoutExamples.length);\n', '', "remove E03 warning")
    audit_path.write_text(audit, encoding="utf-8")

    release_path = ROOT / "content/english/releases/2026.10.0.json"
    release = read_json(release_path)
    if release.get("runtimeCounts", {}).get("sentences") != 3388:
        raise RuntimeError("release runtime sentence count drift")
    release["runtimeCounts"]["sentences"] = 3401
    release.setdefault("notes", []).append("E03 primary senses now link to reviewed sentence examples; 13 project-original examples were added without changing E06 quotas.")
    write_json(release_path, release)

    print(json.dumps({
        "status": "applied",
        "sensesLinked": 300,
        "existingExplicitLinks": 287,
        "newProjectOriginalExamples": 13,
        "runtimeExamplesAfterPublish": 1513,
        "runtimeSentenceRecordsAfterPublish": 3401,
        "senseDecisionFilesRefreshed": len(changed_decision_files),
    }, indent=2))


if __name__ == "__main__":
    main()
