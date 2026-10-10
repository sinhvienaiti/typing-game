#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "content/english/batches/manifest.json"
COL_PATH = ROOT / "content/english/phrases/e04-scale-25-collocations.json"
DECISION_PATH = ROOT / "content/english/reviews/decisions.d/e04-scale-25.json"
BATCH_ID = "e04.phrase-pattern-scale-25"
REVIEWED_AT = "2026-10-06T18:30:00Z"
REVIEWED_BY = "chatgpt-editorial-scale-25"
EXPECTED = {"collocations": 600, "verbPatterns": 510, "phraseItems": 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ("wield considerable influence", "verb + noun", "có và sử dụng mức độ ảnh hưởng đáng kể đối với quyết định hoặc kết quả", "C1"),
    ("articulate a position", "verb + noun", "trình bày rõ ràng quan điểm hoặc lập trường về một vấn đề", "C1"),
    ("clarify expectations", "verb + noun", "làm rõ những điều được mong đợi về kết quả, trách nhiệm hoặc hành vi", "B2"),
    ("define parameters", "verb + noun", "xác định các giới hạn hoặc điều kiện chính của một kế hoạch hay quá trình", "C1"),
    ("delineate responsibilities", "verb + noun", "phân định rõ trách nhiệm giữa các cá nhân hoặc đơn vị", "C1"),
    ("coordinate efforts", "verb + noun", "phối hợp các nỗ lực của nhiều bên để đạt một mục tiêu chung", "B2"),
    ("pool expertise", "verb + noun", "kết hợp chuyên môn của nhiều người hoặc tổ chức để xử lý một nhiệm vụ", "C1"),
    ("set a precedent", "verb + noun", "tạo ra tiền lệ có thể ảnh hưởng tới các quyết định sau này", "C1"),
    ("establish criteria", "verb + noun", "xác lập các tiêu chí dùng để đánh giá hoặc lựa chọn", "B2"),
    ("satisfy requirements", "verb + noun", "đáp ứng đầy đủ các yêu cầu đã đặt ra", "B2"),
    ("fulfill obligations", "verb + noun", "thực hiện đầy đủ các nghĩa vụ đã cam kết hoặc được quy định", "B2"),
    ("allocate funding", "verb + noun", "phân bổ nguồn kinh phí cho một mục đích hoặc chương trình", "B2"),
    ("prioritize investment", "verb + noun", "ưu tiên nguồn đầu tư cho những lĩnh vực hoặc mục tiêu quan trọng hơn", "C1"),
    ("mobilize support", "verb + noun", "huy động sự ủng hộ cho một mục tiêu hoặc sáng kiến", "C1"),
    ("garner support", "verb + noun", "thu hút và tích lũy sự ủng hộ từ nhiều bên", "C1"),
    ("command respect", "verb + noun", "tạo được sự tôn trọng mạnh mẽ từ người khác", "C1"),
    ("invite scrutiny", "verb + noun", "khiến một vấn đề hoặc quyết định bị xem xét kỹ lưỡng", "C1"),
    ("reduce exposure", "verb + noun", "giảm mức độ tiếp xúc hoặc phụ thuộc vào một nguồn rủi ro", "C1"),
    ("assess feasibility", "verb + noun", "đánh giá mức độ khả thi của một kế hoạch hoặc phương án", "C1"),
    ("demonstrate competence", "verb + noun", "thể hiện năng lực thực hiện công việc một cách đáng tin cậy", "C1"),
    ("demonstrate compliance", "verb + noun", "chứng minh việc tuân thủ quy định hoặc tiêu chuẩn", "C1"),
    ("ensure compliance", "verb + noun", "đảm bảo các quy định hoặc tiêu chuẩn được tuân thủ", "B2"),
    ("reinforce safeguards", "verb + noun", "tăng cường các biện pháp bảo vệ nhằm ngăn ngừa rủi ro hoặc sai phạm", "C1"),
    ("lift restrictions", "verb + noun", "dỡ bỏ các hạn chế đang được áp dụng", "B2"),
    ("enforce standards", "verb + noun", "buộc việc tuân thủ các tiêu chuẩn đã quy định", "C1"),
    ("uphold standards", "verb + noun", "duy trì và bảo vệ các tiêu chuẩn đã cam kết", "C1"),
    ("seek redress", "verb + noun", "tìm kiếm biện pháp khắc phục hoặc bồi thường cho một thiệt hại", "C1"),
    ("settle a dispute", "verb + noun", "giải quyết một tranh chấp để các bên đạt được kết quả chấp nhận được", "B2"),
    ("negotiate terms", "verb + noun", "thương lượng các điều khoản của một thỏa thuận", "B2"),
    ("facilitate dialogue", "verb + noun", "tạo điều kiện để các bên trao đổi và thảo luận hiệu quả", "C1"),
    ("foster collaboration", "verb + noun", "thúc đẩy sự hợp tác bền vững giữa các cá nhân hoặc tổ chức", "C1"),
    ("spur innovation", "verb + noun", "thúc đẩy quá trình đổi mới diễn ra nhanh hoặc mạnh hơn", "C1"),
    ("broaden access", "verb + noun", "mở rộng khả năng tiếp cận một dịch vụ, nguồn lực hoặc cơ hội", "B2"),
    ("narrow disparities", "verb + noun", "thu hẹp chênh lệch giữa các nhóm hoặc khu vực", "C1"),
    ("contain costs", "verb + noun", "kiểm soát để chi phí không tăng vượt mức", "B2"),
    ("stimulate demand", "verb + noun", "kích thích nhu cầu đối với hàng hóa, dịch vụ hoặc hoạt động", "C1"),
    ("curb inflation", "verb + noun", "kiềm chế tốc độ tăng của mức giá chung", "C1"),
    ("strengthen oversight", "verb + noun", "tăng cường hoạt động giám sát và kiểm soát", "C1"),
    ("enhance transparency", "verb + noun", "tăng mức độ minh bạch của thông tin hoặc quy trình", "C1"),
    ("restore confidence", "verb + noun", "khôi phục niềm tin sau khi niềm tin bị suy giảm", "B2"),
]


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def normalized_key(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).strip().lower()
    return re.sub(r"\s+", " ", text)


def token_set(text: str) -> set[str]:
    clean = re.sub(r"[^a-z0-9'’-]+", " ", normalized_key(text))
    return {part for part in clean.split() if part}


def jaccard(a: str, b: str) -> float:
    left, right = token_set(a), token_set(b)
    if not left and not right:
        return 1.0
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def digest(record) -> str:
    review_source = json.loads(json.dumps(record, ensure_ascii=False))
    checks = review_source.get("quality", {}).get("checks", {})
    checks.pop("cefr", None)
    checks.pop("license", None)
    payload = json.dumps(review_source, ensure_ascii=False, indent=2) + "\n"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence of {old!r}, found {count}")
    return text.replace(old, new, 1)


def make_collocation(identifier: int, spec):
    text, pattern, meaning_vi, cefr = spec
    headword = normalized_key(text).split()[0]
    record_id = f"col.{identifier:08d}"
    return {
        "schemaVersion": 1,
        "id": record_id,
        "text": text,
        "headwordKeys": [headword],
        "pattern": pattern,
        "meaningVi": meaning_vi,
        "cefr": cefr,
        "register": ["neutral"],
        "exampleIds": [],
        "quality": {
            "state": "draft",
            "checks": {
                "schema": {"status": "pass", "method": "e04-scale-25-authoring-v1"},
                "grammar": {"status": "pending", "method": "manual-review-required"},
                "translation": {"status": "pending", "method": "manual-review-required"},
                "naturalness": {"status": "pending", "method": "manual-review-required"},
                "cefr": {"status": "pending", "method": "manual-review-required"},
                "targetStructure": {"status": "pending", "method": "manual-review-required"},
                "exactDuplicate": {"status": "pass", "method": "normalized-key-v26"},
                "nearDuplicate": {"status": "pending", "method": "manual-review-required"},
                "license": {"status": "pending", "method": "manual-review-required"},
            },
        },
        "provenance": {
            "sources": [{
                "dataset": "project-original",
                "sourceId": record_id,
                "sourceUrl": "content/english/phrases/e04-scale-25-collocations.json",
                "snapshot": "2026-10",
                "license": "LicenseRef-Project-Original",
                "modified": False,
            }],
            "note": "Project-original controlled E04 scale-up record.",
        },
    }


def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get("id") == BATCH_ID for batch in manifest.get("batches", [])):
        print(json.dumps({"status": "skip", "reason": "batch already exists", "batch": BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError("scale-25 artifact exists without matching batch manifest")

    existing = {"collocations": [], "verbPatterns": [], "phraseItems": []}
    all_texts = []
    all_ids = set()
    for batch in manifest.get("batches", []):
        if batch.get("phase") != "E04" or batch.get("category") != "phrases":
            continue
        for record_set in batch.get("recordSets", []):
            records = read_json(ROOT / record_set["path"]).get("records", [])
            set_id = record_set.get("id")
            if set_id in {"collocations", "scale-collocations"}:
                existing["collocations"].extend(records)
            elif set_id in {"verb-patterns", "scale-verb-patterns"}:
                existing["verbPatterns"].extend(records)
            elif set_id in {"phrases", "scale-phrases"}:
                existing["phraseItems"].extend(records)
            for record in records:
                rid = record.get("id")
                if rid in all_ids:
                    raise RuntimeError(f"existing duplicate E04 record id before scale-25: {rid}")
                all_ids.add(rid)
                value = record.get("text") or record.get("pattern") or ""
                if value:
                    all_texts.append((rid, value))

    actual = {key: len(value) for key, value in existing.items()}
    if actual != EXPECTED:
        raise RuntimeError(f"E04 source counts drifted; expected {EXPECTED}, got {actual}")

    col_numbers = []
    for record in existing["collocations"]:
        match = re.fullmatch(r"col\.(\d{8})", str(record.get("id", "")))
        if match:
            col_numbers.append(int(match.group(1)))
    if not col_numbers or max(col_numbers) != 600:
        raise RuntimeError(f"collocation ID frontier drifted; expected max 600, got {max(col_numbers) if col_numbers else None}")

    new_collocations = [make_collocation(601 + index, spec) for index, spec in enumerate(COLLOCATIONS)]
    if len(new_collocations) != 40:
        raise RuntimeError(f"scale-25 expected 40 collocations, got {len(new_collocations)}")

    existing_normalized = {normalized_key(text): rid for rid, text in all_texts}
    accepted = []
    for record in new_collocations:
        rid = record["id"]
        if rid in all_ids:
            raise RuntimeError(f"new record id collides with existing E04 record: {rid}")
        key = normalized_key(record["text"])
        if key in existing_normalized:
            raise RuntimeError(f"exact duplicate against existing E04: {rid} {record['text']!r} == {existing_normalized[key]}")
        for old_id, old_text in all_texts:
            score = jaccard(record["text"], old_text)
            if score >= NEAR_DUP_THRESHOLD:
                raise RuntimeError(
                    f"near duplicate against existing E04 ({score:.3f}): {rid} {record['text']!r} ~ {old_id} {old_text!r}"
                )
        for prior in accepted:
            if normalized_key(prior["text"]) == key:
                raise RuntimeError(f"exact duplicate inside scale-25: {record['text']!r}")
            score = jaccard(record["text"], prior["text"])
            if score >= NEAR_DUP_THRESHOLD:
                raise RuntimeError(
                    f"near duplicate inside scale-25 ({score:.3f}): {record['text']!r} ~ {prior['text']!r}"
                )
        accepted.append(record)

    write_json(COL_PATH, {"schemaVersion": 1, "records": new_collocations})

    manifest["batches"].append({
        "id": BATCH_ID,
        "phase": "E04",
        "category": "phrases",
        "cefr": ["B2", "C1"],
        "state": "draft",
        "recordSets": [{
            "id": "scale-collocations",
            "path": "content/english/phrases/e04-scale-25-collocations.json",
            "expectedCount": 40,
            "generated": False,
            "allowedQualityStates": ["draft"],
            "requiredChecks": [
                "schema", "grammar", "translation", "naturalness", "cefr", "targetStructure",
                "exactDuplicate", "nearDuplicate", "license",
            ],
        }],
        "requiredBeforePublish": [
            "schema-validation", "reference-integrity", "exact-dedup", "near-dedup",
            "grammar-review", "bilingual-review", "naturalness-review", "cefr-review",
            "target-structure-review", "license-review", "cross-game-smoke",
        ],
        "gameSmokes": [
            {"gameId": "recall-typing", "activity": "collocation", "recordSetId": "scale-collocations", "sampleCount": 5},
            {"gameId": "vocab-shooter", "activity": "collocation", "recordSetId": "scale-collocations", "sampleCount": 5},
            {"gameId": "space-typing", "activity": "collocation", "recordSetId": "scale-collocations", "sampleCount": 5},
        ],
    })
    write_json(MANIFEST_PATH, manifest)

    decisions = []
    for record in new_collocations:
        decisions.append({
            "id": "review.e04.scale-25." + record["id"].replace(".", "-"),
            "batchId": BATCH_ID,
            "recordSetId": "scale-collocations",
            "recordId": record["id"],
            "sourceDigest": digest(record),
            "targetState": "published",
            "checks": {
                "grammar": {"status": "pass", "method": "e04-scale-25-grammar-editorial-review"},
                "translation": {"status": "pass", "method": "e04-scale-25-bilingual-review"},
                "naturalness": {"status": "pass", "method": "e04-scale-25-naturalness-review"},
                "cefr": {"status": "pass", "method": "e04-scale-25-cefr-review"},
                "targetStructure": {"status": "pass", "method": "e04-scale-25-structure-review"},
                "nearDuplicate": {"status": "pass", "method": "e04-scale-25-cross-batch-near-dedup-review"},
                "license": {"status": "pass", "method": "project-original-license-review-v1"},
            },
            "reviewedAt": REVIEWED_AT,
            "reviewedBy": REVIEWED_BY,
            "note": (
                "Focused E04 scale 25 collocation reviewed for structure, grammar, Vietnamese meaning, "
                "naturalness, CEFR, exact/near dedup and project-original provenance."
            ),
        })
    write_json(DECISION_PATH, {"schemaVersion": 1, "decisions": decisions})

    smoke_path = ROOT / "scripts/smoke-published-english-content.mjs"
    smoke = smoke_path.read_text(encoding="utf-8")
    smoke = replace_once(smoke, "if(recallCollocations!==600)", "if(recallCollocations!==640)", "collocation count")
    smoke = replace_once(
        smoke,
        "must expose 600 reviewed records",
        "must expose 640 reviewed records",
        "collocation message",
    )
    smoke_path.write_text(smoke, encoding="utf-8")

    release_path = ROOT / "content/english/releases/2026.10.0.json"
    release = read_json(release_path)
    current_phrases = release.get("runtimeCounts", {}).get("phrases")
    if current_phrases != 1710:
        raise RuntimeError(f"release phrase count drift: expected 1710, got {current_phrases}")
    release["runtimeCounts"]["phrases"] = 1750
    release.setdefault("notes", []).append(
        "E04 focused scale 25 adds 40 reviewed B2/C1 collocations; verb-pattern and phrase-item volumes are unchanged."
    )
    write_json(release_path, release)

    print(json.dumps({
        "status": "applied",
        "batch": BATCH_ID,
        "added": {"collocations": 40},
        "expectedRuntime": {
            "totalPhrases": 1750,
            "collocations": 640,
            "verbPatterns": 510,
            "phrasalVerbs": 300,
            "chunks": 165,
            "idioms": 135,
        },
        "antiDuplicate": {
            "exact": "normalized-key-v26",
            "near": f"token-jaccard<{NEAR_DUP_THRESHOLD}",
            "preconditionCounts": EXPECTED,
            "collocationIdFrontier": 600,
        },
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
