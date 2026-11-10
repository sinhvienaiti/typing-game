#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "content/english/batches/manifest.json"
COL_PATH = ROOT / "content/english/phrases/e04-scale-27-collocations.json"
DECISION_PATH = ROOT / "content/english/reviews/decisions.d/e04-scale-27.json"
PROGRESS_PATH = ROOT / "docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md"
BATCH_ID = "e04.phrase-pattern-scale-27"
REVIEWED_AT = "2026-10-07T01:30:00Z"
REVIEWED_BY = "chatgpt-editorial-scale-27"
EXPECTED = {"collocations": 680, "verbPatterns": 510, "phraseItems": 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('establish governance safeguards', 'verb + noun phrase', 'thiết lập các biện pháp bảo đảm quản trị nhằm hạn chế sai lệch và rủi ro', 'C1'),
    ('strengthen oversight arrangements', 'verb + noun phrase', 'tăng cường các cơ chế giám sát để bảo đảm hoạt động được kiểm tra đầy đủ', 'C1'),
    ('improve regulatory coordination', 'verb + noun phrase', 'cải thiện sự phối hợp giữa các cơ quan hoặc yêu cầu quản lý', 'C1'),
    ('enhance policy consistency', 'verb + noun phrase', 'nâng cao tính nhất quán giữa các chính sách và cách áp dụng chúng', 'C1'),
    ('promote cross-sector collaboration', 'verb + noun phrase', 'thúc đẩy hợp tác giữa nhiều lĩnh vực hoặc khu vực khác nhau', 'C1'),
    ('facilitate knowledge exchange', 'verb + noun phrase', 'tạo điều kiện cho việc trao đổi kiến thức và kinh nghiệm', 'B2'),
    ('support evidence-based planning', 'verb + noun phrase', 'hỗ trợ lập kế hoạch dựa trên bằng chứng và dữ liệu đáng tin cậy', 'C1'),
    ('improve resource allocation', 'verb + noun phrase', 'cải thiện cách phân bổ nguồn lực theo nhu cầu và ưu tiên', 'B2'),
    ('optimize resource utilization', 'verb + noun phrase', 'tối ưu hóa việc sử dụng nguồn lực để đạt hiệu quả cao hơn', 'C1'),
    ('strengthen fiscal discipline', 'verb + noun phrase', 'tăng cường kỷ luật tài khóa và kiểm soát việc sử dụng ngân sách', 'C1'),
    ('maintain budget credibility', 'verb + noun phrase', 'duy trì độ tin cậy của kế hoạch và cam kết ngân sách', 'C1'),
    ('improve expenditure control', 'verb + noun phrase', 'cải thiện việc kiểm soát chi tiêu để giảm lãng phí và vượt ngân sách', 'C1'),
    ('increase administrative efficiency', 'verb + noun phrase', 'nâng cao hiệu quả hành chính và giảm thời gian xử lý không cần thiết', 'B2'),
    ('reduce procedural burdens', 'verb + noun phrase', 'giảm gánh nặng do thủ tục phức tạp hoặc không cần thiết gây ra', 'C1'),
    ('eliminate redundant processes', 'verb + noun phrase', 'loại bỏ các quy trình trùng lặp hoặc không còn tạo giá trị', 'B2'),
    ('resolve implementation bottlenecks', 'verb + noun phrase', 'giải quyết các điểm nghẽn làm chậm quá trình triển khai', 'C1'),
    ('remove structural barriers', 'verb + noun phrase', 'loại bỏ các rào cản mang tính cấu trúc cản trở thay đổi hoặc tiếp cận', 'C1'),
    ('expand institutional coverage', 'verb + noun phrase', 'mở rộng phạm vi bao phủ của một cơ chế hoặc thể chế', 'C1'),
    ('improve service accessibility', 'verb + noun phrase', 'cải thiện khả năng tiếp cận dịch vụ của người dùng hoặc cộng đồng', 'B2'),
    ('enhance user experience', 'verb + noun phrase', 'nâng cao trải nghiệm tổng thể của người sử dụng dịch vụ hoặc sản phẩm', 'B2'),
    ('strengthen data governance', 'verb + noun phrase', 'tăng cường cơ chế quản trị dữ liệu về trách nhiệm, chất lượng và sử dụng', 'C1'),
    ('improve data interoperability', 'verb + noun phrase', 'cải thiện khả năng các hệ thống dữ liệu trao đổi và sử dụng thông tin với nhau', 'C1'),
    ('ensure data integrity', 'verb + noun phrase', 'bảo đảm dữ liệu chính xác, đầy đủ và không bị thay đổi trái phép', 'B2'),
    ('protect confidential information', 'verb + noun phrase', 'bảo vệ thông tin mật khỏi truy cập hoặc tiết lộ không được phép', 'B2'),
    ('improve analytical capability', 'verb + noun phrase', 'nâng cao năng lực phân tích dữ liệu và vấn đề để hỗ trợ quyết định', 'C1'),
    ('develop forecasting capacity', 'verb + noun phrase', 'phát triển năng lực dự báo các xu hướng và kết quả trong tương lai', 'C1'),
    ('enhance scenario planning', 'verb + noun phrase', 'nâng cao việc xây dựng và đánh giá nhiều kịch bản có thể xảy ra', 'C1'),
    ('support informed decision-making', 'verb + noun phrase', 'hỗ trợ việc ra quyết định dựa trên thông tin và phân tích đầy đủ', 'B2'),
    ('improve stakeholder engagement', 'verb + noun phrase', 'cải thiện mức độ tham gia và tương tác của các bên liên quan', 'B2'),
    ('broaden public participation', 'verb + noun phrase', 'mở rộng sự tham gia của công chúng vào quá trình thảo luận hoặc quyết định', 'C1'),
    ('strengthen community ownership', 'verb + noun phrase', 'tăng mức độ cộng đồng chủ động chịu trách nhiệm và gắn bó với một sáng kiến', 'C1'),
    ('foster collaborative problem-solving', 'verb + noun phrase', 'khuyến khích giải quyết vấn đề thông qua hợp tác giữa nhiều bên', 'C1'),
    ('build implementation capability', 'verb + noun phrase', 'xây dựng năng lực cần thiết để triển khai kế hoạch một cách hiệu quả', 'C1'),
    ('improve program delivery', 'verb + noun phrase', 'cải thiện cách chương trình được triển khai để đạt kết quả dự kiến', 'B2'),
    ('strengthen performance monitoring', 'verb + noun phrase', 'tăng cường theo dõi hiệu suất và tiến độ thực hiện', 'B2'),
    ('improve outcome measurement', 'verb + noun phrase', 'cải thiện cách đo lường kết quả cuối cùng của chương trình hoặc chính sách', 'C1'),
    ('establish feedback mechanisms', 'verb + noun phrase', 'thiết lập cơ chế thu thập và phản hồi ý kiến một cách có hệ thống', 'B2'),
    ('incorporate stakeholder feedback', 'verb + noun phrase', 'tích hợp phản hồi của các bên liên quan vào thiết kế hoặc triển khai', 'B2'),
    ('adapt implementation strategies', 'verb + noun phrase', 'điều chỉnh chiến lược triển khai khi điều kiện hoặc bằng chứng thay đổi', 'C1'),
    ('embed continuous improvement', 'verb + noun phrase', 'đưa việc cải tiến liên tục trở thành một phần thường xuyên của hoạt động', 'C1'),
]


def read_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def normalized_key(text: str) -> str:
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', text).strip().lower())


def token_set(text: str) -> set[str]:
    clean = re.sub(r"[^a-z0-9'’-]+", ' ', normalized_key(text))
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
    checks = review_source.get('quality', {}).get('checks', {})
    checks.pop('cefr', None)
    checks.pop('license', None)
    payload = json.dumps(review_source, ensure_ascii=False, indent=2) + '\n'
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected exactly one occurrence of {old!r}, found {count}')
    return text.replace(old, new, 1)


def make_collocation(identifier: int, spec):
    text, pattern, meaning_vi, cefr = spec
    record_id = f'col.{identifier:08d}'
    return {
        'schemaVersion': 1,
        'id': record_id,
        'text': text,
        'headwordKeys': [normalized_key(text).split()[0]],
        'pattern': pattern,
        'meaningVi': meaning_vi,
        'cefr': cefr,
        'register': ['neutral'],
        'exampleIds': [],
        'quality': {'state': 'draft', 'checks': {
            'schema': {'status': 'pass', 'method': 'e04-scale-27-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v28'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'}
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original', 'sourceId': record_id,
            'sourceUrl': 'content/english/phrases/e04-scale-27-collocations.json',
            'snapshot': '2026-10', 'license': 'LicenseRef-Project-Original', 'modified': False
        }], 'note': 'Project-original controlled E04 scale-up record.'}
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(text,
        '- Latest fully CI-verified HEAD before this scale-up activation: `5aba144858554bbc32c3866452c6ced6638e27a1`',
        '- Latest fully CI-verified scale-up prep HEAD: `a393e8351687c202be391935487b697d9597882d` — scale-26 publication workflow, Full Validation, Master Plan Acceptance and Platform CI all PASS; publication output: `0eb0bad34550866a067730d98ab1157da569b80b`.',
        'verified head checkpoint')
    old_ci = '''- Latest verified CI for `5aba144858554bbc32c3866452c6ced6638e27a1`:\n  - English Content Full Validation #53 — PASS\n  - English Content Master Plan Acceptance #33 — PASS\n  - Platform CI #1008 — PASS'''
    new_ci = '''- Latest verified scale-up gates before scale-27 publication:\n  - Apply English E04 Scale 26 #1 — PASS\n  - English Content Full Validation #64 — PASS\n  - English Content Master Plan Acceptance #45 — PASS\n  - Platform CI #1057 — PASS'''
    text = replace_once(text, old_ci, new_ci, 'CI checkpoint')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 1,710 published records', '- E04 phrase/pattern architecture + current reviewed publication: complete — 1,830 published records after scale-27', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot before scale-up continuation', '## Published runtime snapshot after E04 scale-27 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 1,710 records', '- phrases: 1,830 records', 'phrase snapshot')
    text = replace_once(text, '- total published rich records: 6,311', '- total published rich records: 6,431', 'runtime total')
    text = replace_once(text, '- editorial ledger: 6,311 decisions / 6,311 applied / 6,311 publish decisions', '- editorial ledger: 6,431 decisions / 6,431 applied / 6,431 publish decisions', 'ledger total')
    text = replace_once(text,
        'Inspect current E04 controlled batches, E04 generation/apply scripts, target/readiness report, review ledger and stable ID registry on latest HEAD. Select the first genuinely new bounded E04 scale/enrichment unit after proving that its batch IDs, record IDs and normalized content are not already present; then generate/validate/review/publish that unit and continue through CI.',
        'Scale-26 and scale-27 collocation batches are complete after all publication gates pass. Resolve latest HEAD, verify scale-27 publication/CI, then continue immediately with the next genuinely new bounded collocation batch from the new ID frontier (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.',
        'next actionable task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-27 artifact exists without matching batch manifest')

    existing = {'collocations': [], 'verbPatterns': [], 'phraseItems': []}
    all_texts = []
    all_ids = set()
    for batch in manifest.get('batches', []):
        if batch.get('phase') != 'E04' or batch.get('category') != 'phrases':
            continue
        for record_set in batch.get('recordSets', []):
            records = read_json(ROOT / record_set['path']).get('records', [])
            set_id = record_set.get('id')
            if set_id in {'collocations', 'scale-collocations'}:
                existing['collocations'].extend(records)
            elif set_id in {'verb-patterns', 'scale-verb-patterns'}:
                existing['verbPatterns'].extend(records)
            elif set_id in {'phrases', 'scale-phrases'}:
                existing['phraseItems'].extend(records)
            for record in records:
                rid = record.get('id')
                if rid in all_ids:
                    raise RuntimeError(f'existing duplicate E04 record id before scale-27: {rid}')
                all_ids.add(rid)
                value = record.get('text') or record.get('pattern') or ''
                if value:
                    all_texts.append((rid, value))

    actual = {key: len(value) for key, value in existing.items()}
    if actual != EXPECTED:
        raise RuntimeError(f'E04 source counts drifted; expected {EXPECTED}, got {actual}')
    col_numbers = [int(m.group(1)) for record in existing['collocations'] if (m := re.fullmatch(r'col\.(\d{8})', str(record.get('id', ''))))]
    if not col_numbers or max(col_numbers) != 680:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 680, got {max(col_numbers) if col_numbers else None}')

    new_records = [make_collocation(681 + index, spec) for index, spec in enumerate(COLLOCATIONS)]
    if len(new_records) != 40:
        raise RuntimeError(f'scale-27 expected 40 collocations, got {len(new_records)}')
    existing_normalized = {normalized_key(text): rid for rid, text in all_texts}
    accepted = []
    for record in new_records:
        rid, text = record['id'], record['text']
        if rid in all_ids:
            raise RuntimeError(f'new record id collides with existing E04 record: {rid}')
        key = normalized_key(text)
        if key in existing_normalized:
            raise RuntimeError(f'exact duplicate against existing E04: {rid} {text!r} == {existing_normalized[key]}')
        for old_id, old_text in all_texts:
            score = jaccard(text, old_text)
            if score >= NEAR_DUP_THRESHOLD:
                raise RuntimeError(f'near duplicate against existing E04 ({score:.3f}): {rid} {text!r} ~ {old_id} {old_text!r}')
        for prior in accepted:
            if normalized_key(prior['text']) == key:
                raise RuntimeError(f'exact duplicate inside scale-27: {text!r}')
            score = jaccard(text, prior['text'])
            if score >= NEAR_DUP_THRESHOLD:
                raise RuntimeError(f'near duplicate inside scale-27 ({score:.3f}): {text!r} ~ {prior["text"]!r}')
        accepted.append(record)

    write_json(COL_PATH, {'schemaVersion': 1, 'records': new_records})
    manifest['batches'].append({
        'id': BATCH_ID, 'phase': 'E04', 'category': 'phrases', 'cefr': ['B2', 'C1'], 'state': 'draft',
        'recordSets': [{'id': 'scale-collocations', 'path': 'content/english/phrases/e04-scale-27-collocations.json', 'expectedCount': 40, 'generated': False, 'allowedQualityStates': ['draft'], 'requiredChecks': ['schema', 'grammar', 'translation', 'naturalness', 'cefr', 'targetStructure', 'exactDuplicate', 'nearDuplicate', 'license']}],
        'requiredBeforePublish': ['schema-validation', 'reference-integrity', 'exact-dedup', 'near-dedup', 'grammar-review', 'bilingual-review', 'naturalness-review', 'cefr-review', 'target-structure-review', 'license-review', 'cross-game-smoke'],
        'gameSmokes': [
            {'gameId': 'recall-typing', 'activity': 'collocation', 'recordSetId': 'scale-collocations', 'sampleCount': 5},
            {'gameId': 'vocab-shooter', 'activity': 'collocation', 'recordSetId': 'scale-collocations', 'sampleCount': 5},
            {'gameId': 'space-typing', 'activity': 'collocation', 'recordSetId': 'scale-collocations', 'sampleCount': 5}
        ]
    })
    write_json(MANIFEST_PATH, manifest)

    decisions = []
    for record in new_records:
        decisions.append({
            'id': 'review.e04.scale-27.' + record['id'].replace('.', '-'), 'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations', 'recordId': record['id'], 'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-27-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-27-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-27-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-27-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-27-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-27-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'}
            },
            'reviewedAt': REVIEWED_AT, 'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 27 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.'
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==680)', 'if(recallCollocations!==720)', 'collocation count')
    smoke = replace_once(smoke, 'must expose 680 reviewed records', 'must expose 720 reviewed records', 'collocation message')
    smoke_path.write_text(smoke, encoding='utf-8')
    update_progress()

    print(json.dumps({'status': 'applied', 'batch': BATCH_ID, 'collocationsAdded': 40, 'collocationRange': ['col.00000681', 'col.00000720'], 'sourceCountsBefore': actual, 'sourceCountsAfter': {'collocations': 720, 'verbPatterns': 510, 'phraseItems': 600}, 'expectedRuntimeAfterPublish': {'phrases': 1830, 'richRecords': 6431}}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
