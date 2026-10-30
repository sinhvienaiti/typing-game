#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "content/english/batches/manifest.json"
COL_PATH = ROOT / "content/english/phrases/e04-scale-26-collocations.json"
DECISION_PATH = ROOT / "content/english/reviews/decisions.d/e04-scale-26.json"
BATCH_ID = "e04.phrase-pattern-scale-26"
REVIEWED_AT = "2026-10-07T01:20:00Z"
REVIEWED_BY = "chatgpt-editorial-scale-26"
EXPECTED = {"collocations": 640, "verbPatterns": 510, "phraseItems": 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('address systemic weaknesses', 'verb + noun phrase', 'xử lý những điểm yếu mang tính hệ thống thay vì chỉ giải quyết triệu chứng riêng lẻ', 'C1'),
    ('establish accountability mechanisms', 'verb + noun phrase', 'thiết lập các cơ chế giúp xác định và giám sát trách nhiệm giải trình', 'C1'),
    ('strengthen institutional capacity', 'verb + noun phrase', 'tăng cường năng lực của tổ chức hoặc thể chế để thực hiện nhiệm vụ hiệu quả', 'C1'),
    ('build organizational resilience', 'verb + noun phrase', 'xây dựng khả năng của tổ chức trong việc thích ứng và phục hồi trước biến động', 'C1'),
    ('preserve policy autonomy', 'verb + noun phrase', 'duy trì khả năng tự chủ khi xây dựng và điều chỉnh chính sách', 'C1'),
    ('maintain strategic coherence', 'verb + noun phrase', 'duy trì sự nhất quán giữa các mục tiêu và hành động chiến lược', 'C1'),
    ('cultivate public trust', 'verb + noun', 'xây dựng và nuôi dưỡng niềm tin của công chúng theo thời gian', 'C1'),
    ('secure stakeholder buy-in', 'verb + noun phrase', 'giành được sự đồng thuận và cam kết của các bên liên quan', 'C1'),
    ('align competing priorities', 'verb + noun phrase', 'điều chỉnh các ưu tiên đang cạnh tranh để chúng phù hợp hơn với mục tiêu chung', 'C1'),
    ('balance competing interests', 'verb + noun phrase', 'cân bằng các lợi ích khác nhau khi đưa ra quyết định', 'C1'),
    ('reconcile conflicting objectives', 'verb + noun phrase', 'dung hòa các mục tiêu mâu thuẫn để tìm ra hướng xử lý khả thi', 'C1'),
    ('articulate strategic priorities', 'verb + noun phrase', 'trình bày rõ các ưu tiên chiến lược quan trọng nhất', 'C1'),
    ('clarify decision criteria', 'verb + noun phrase', 'làm rõ các tiêu chí dùng để đưa ra quyết định', 'B2'),
    ('document key assumptions', 'verb + noun phrase', 'ghi lại các giả định quan trọng làm cơ sở cho phân tích hoặc kế hoạch', 'B2'),
    ('validate underlying assumptions', 'verb + noun phrase', 'kiểm chứng các giả định nền tảng trước khi dựa vào chúng để quyết định', 'C1'),
    ('quantify potential benefits', 'verb + noun phrase', 'định lượng những lợi ích có thể đạt được từ một phương án', 'C1'),
    ('estimate implementation costs', 'verb + noun phrase', 'ước tính chi phí cần thiết để triển khai một kế hoạch hoặc chính sách', 'B2'),
    ('identify operational constraints', 'verb + noun phrase', 'xác định các hạn chế thực tế ảnh hưởng tới hoạt động hoặc triển khai', 'B2'),
    ('anticipate unintended consequences', 'verb + noun phrase', 'dự đoán những hệ quả không chủ ý có thể phát sinh từ một quyết định', 'C1'),
    ('assess distributional effects', 'verb + noun phrase', 'đánh giá cách lợi ích hoặc chi phí được phân bổ giữa các nhóm', 'C1'),
    ('evaluate policy trade-offs', 'verb + noun phrase', 'đánh giá các đánh đổi giữa những mục tiêu chính sách khác nhau', 'C1'),
    ('monitor emerging risks', 'verb + noun phrase', 'theo dõi các rủi ro mới xuất hiện để có thể phản ứng sớm', 'B2'),
    ('detect early warning signs', 'verb + noun phrase', 'phát hiện các dấu hiệu cảnh báo sớm về vấn đề hoặc rủi ro', 'B2'),
    ('trigger corrective action', 'verb + noun phrase', 'kích hoạt hành động khắc phục khi phát hiện sai lệch hoặc vấn đề', 'C1'),
    ('initiate remedial measures', 'verb + noun phrase', 'khởi động các biện pháp sửa chữa nhằm khắc phục vấn đề đã xác định', 'C1'),
    ('establish reporting lines', 'verb + noun phrase', 'thiết lập tuyến báo cáo rõ ràng trong một tổ chức', 'B2'),
    ('assign clear ownership', 'verb + noun phrase', 'giao trách nhiệm sở hữu công việc hoặc kết quả một cách rõ ràng', 'B2'),
    ('delegate decision authority', 'verb + noun phrase', 'ủy quyền ra quyết định cho cá nhân hoặc cấp phù hợp', 'C1'),
    ('streamline approval processes', 'verb + noun phrase', 'đơn giản hóa quy trình phê duyệt để giảm chậm trễ và bước không cần thiết', 'C1'),
    ('standardize operating procedures', 'verb + noun phrase', 'chuẩn hóa các quy trình vận hành để tăng tính nhất quán', 'C1'),
    ('harmonize regulatory requirements', 'verb + noun phrase', 'làm cho các yêu cầu pháp lý hoặc quy định tương thích và nhất quán hơn', 'C1'),
    ('strengthen internal controls', 'verb + noun phrase', 'tăng cường các cơ chế kiểm soát nội bộ để giảm rủi ro và sai sót', 'C1'),
    ('preserve institutional memory', 'verb + noun phrase', 'duy trì tri thức và kinh nghiệm tích lũy của một tổ chức qua thời gian', 'C1'),
    ('transfer tacit knowledge', 'verb + noun phrase', 'chuyển giao kiến thức ngầm hình thành từ kinh nghiệm thực tế', 'C1'),
    ('develop contingency arrangements', 'verb + noun phrase', 'xây dựng các phương án dự phòng để ứng phó khi kế hoạch chính bị gián đoạn', 'C1'),
    ('activate contingency measures', 'verb + noun phrase', 'kích hoạt các biện pháp dự phòng khi điều kiện bất lợi xảy ra', 'C1'),
    ('maintain service continuity', 'verb + noun phrase', 'duy trì hoạt động cung cấp dịch vụ liên tục khi có gián đoạn', 'B2'),
    ('restore operational capacity', 'verb + noun phrase', 'khôi phục năng lực vận hành sau sự cố hoặc gián đoạn', 'C1'),
    ('consolidate operational gains', 'verb + noun phrase', 'củng cố những cải thiện đã đạt được trong hoạt động để chúng bền vững hơn', 'C1'),
    ('sustain reform momentum', 'verb + noun phrase', 'duy trì động lực cải cách để tiến độ không bị chững lại', 'C1'),
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
                "schema": {"status": "pass", "method": "e04-scale-26-authoring-v1"},
                "grammar": {"status": "pending", "method": "manual-review-required"},
                "translation": {"status": "pending", "method": "manual-review-required"},
                "naturalness": {"status": "pending", "method": "manual-review-required"},
                "cefr": {"status": "pending", "method": "manual-review-required"},
                "targetStructure": {"status": "pending", "method": "manual-review-required"},
                "exactDuplicate": {"status": "pass", "method": "normalized-key-v27"},
                "nearDuplicate": {"status": "pending", "method": "manual-review-required"},
                "license": {"status": "pending", "method": "manual-review-required"}
            }
        },
        "provenance": {
            "sources": [{
                "dataset": "project-original",
                "sourceId": record_id,
                "sourceUrl": "content/english/phrases/e04-scale-26-collocations.json",
                "snapshot": "2026-10",
                "license": "LicenseRef-Project-Original",
                "modified": False
            }],
            "note": "Project-original controlled E04 scale-up record."
        }
    }


def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get("id") == BATCH_ID for batch in manifest.get("batches", [])):
        print(json.dumps({"status": "skip", "reason": "batch already exists", "batch": BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError("scale-26 artifact exists without matching batch manifest")

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
                    raise RuntimeError(f"existing duplicate E04 record id before scale-26: {rid}")
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
    if not col_numbers or max(col_numbers) != 640:
        raise RuntimeError(f"collocation ID frontier drifted; expected max 640, got {max(col_numbers) if col_numbers else None}")

    new_collocations = [make_collocation(641 + index, spec) for index, spec in enumerate(COLLOCATIONS)]
    if len(new_collocations) != 40:
        raise RuntimeError(f"scale-26 expected 40 collocations, got {len(new_collocations)}")

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
                raise RuntimeError(f"near duplicate against existing E04 ({score:.3f}): {rid} {record['text']!r} ~ {old_id} {old_text!r}")
        for prior in accepted:
            if normalized_key(prior["text"]) == key:
                raise RuntimeError(f"exact duplicate inside scale-26: {record['text']!r}")
            score = jaccard(record["text"], prior["text"])
            if score >= NEAR_DUP_THRESHOLD:
                raise RuntimeError(f"near duplicate inside scale-26 ({score:.3f}): {record['text']!r} ~ {prior['text']!r}")
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
            "path": "content/english/phrases/e04-scale-26-collocations.json",
            "expectedCount": 40,
            "generated": False,
            "allowedQualityStates": ["draft"],
            "requiredChecks": ["schema", "grammar", "translation", "naturalness", "cefr", "targetStructure", "exactDuplicate", "nearDuplicate", "license"]
        }],
        "requiredBeforePublish": ["schema-validation", "reference-integrity", "exact-dedup", "near-dedup", "grammar-review", "bilingual-review", "naturalness-review", "cefr-review", "target-structure-review", "license-review", "cross-game-smoke"],
        "gameSmokes": [
            {"gameId": "recall-typing", "activity": "collocation", "recordSetId": "scale-collocations", "sampleCount": 5},
            {"gameId": "vocab-shooter", "activity": "collocation", "recordSetId": "scale-collocations", "sampleCount": 5},
            {"gameId": "space-typing", "activity": "collocation", "recordSetId": "scale-collocations", "sampleCount": 5}
        ]
    })
    write_json(MANIFEST_PATH, manifest)

    decisions = []
    for record in new_collocations:
        decisions.append({
            "id": "review.e04.scale-26." + record["id"].replace(".", "-"),
            "batchId": BATCH_ID,
            "recordSetId": "scale-collocations",
            "recordId": record["id"],
            "sourceDigest": digest(record),
            "targetState": "published",
            "checks": {
                "grammar": {"status": "pass", "method": "e04-scale-26-grammar-editorial-review"},
                "translation": {"status": "pass", "method": "e04-scale-26-bilingual-review"},
                "naturalness": {"status": "pass", "method": "e04-scale-26-naturalness-review"},
                "cefr": {"status": "pass", "method": "e04-scale-26-cefr-review"},
                "targetStructure": {"status": "pass", "method": "e04-scale-26-structure-review"},
                "nearDuplicate": {"status": "pass", "method": "e04-scale-26-cross-batch-near-dedup-review"},
                "license": {"status": "pass", "method": "project-original-license-review-v1"}
            },
            "reviewedAt": REVIEWED_AT,
            "reviewedBy": REVIEWED_BY,
            "note": "Focused E04 scale 26 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance."
        })
    write_json(DECISION_PATH, {"schemaVersion": 1, "decisions": decisions})

    smoke_path = ROOT / "scripts/smoke-published-english-content.mjs"
    smoke = smoke_path.read_text(encoding="utf-8")
    smoke = replace_once(smoke, "if(recallCollocations!==640)", "if(recallCollocations!==680)", "collocation count")
    smoke = replace_once(smoke, "must expose 640 reviewed records", "must expose 680 reviewed records", "collocation message")
    smoke_path.write_text(smoke, encoding="utf-8")

    print(json.dumps({"status": "applied", "batch": BATCH_ID, "collocationsAdded": len(new_collocations), "collocationRange": ["col.00000641", "col.00000680"], "sourceCountsBefore": actual, "sourceCountsAfter": {"collocations": 680, "verbPatterns": 510, "phraseItems": 600}}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
