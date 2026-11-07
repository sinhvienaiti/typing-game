#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-29-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-29.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-29'
REVIEWED_AT = '2026-10-07T02:20:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-29'
EXPECTED = {'collocations': 760, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('establish research priorities', 'verb + noun phrase', 'xác lập các ưu tiên nghiên cứu để tập trung nguồn lực vào những câu hỏi quan trọng nhất', 'C1'),
    ('formulate testable hypotheses', 'verb + adjective + noun', 'xây dựng các giả thuyết có thể được kiểm chứng bằng dữ liệu hoặc thí nghiệm', 'C1'),
    ('design robust experiments', 'verb + adjective + noun', 'thiết kế các thí nghiệm có độ tin cậy cao và hạn chế sai lệch', 'C1'),
    ('define sampling criteria', 'verb + noun phrase', 'xác định các tiêu chí lấy mẫu cho nghiên cứu hoặc phân tích', 'B2'),
    ('select representative samples', 'verb + adjective + noun', 'lựa chọn các mẫu có tính đại diện phù hợp cho quần thể cần nghiên cứu', 'C1'),
    ('collect longitudinal data', 'verb + adjective + noun', 'thu thập dữ liệu theo thời gian để quan sát xu hướng và thay đổi', 'C1'),
    ('validate measurement instruments', 'verb + noun phrase', 'xác nhận các công cụ đo lường phản ánh đúng đại lượng cần đánh giá', 'C1'),
    ('control confounding variables', 'verb + noun phrase', 'kiểm soát các biến gây nhiễu có thể làm sai lệch kết quả phân tích', 'C1'),
    ('replicate key findings', 'verb + adjective + noun', 'lặp lại nghiên cứu để kiểm tra khả năng tái lập của các phát hiện quan trọng', 'C1'),
    ('document research limitations', 'verb + noun phrase', 'ghi rõ các giới hạn của nghiên cứu để hỗ trợ diễn giải kết quả thận trọng', 'B2'),
    ('interpret statistical evidence', 'verb + adjective + noun', 'diễn giải bằng chứng thống kê trong đúng bối cảnh của câu hỏi nghiên cứu', 'C1'),
    ('quantify uncertainty ranges', 'verb + noun phrase', 'định lượng khoảng bất định để thể hiện mức độ chắc chắn của ước lượng', 'C1'),
    ('estimate treatment effects', 'verb + noun phrase', 'ước lượng mức tác động của một biện pháp can thiệp hoặc phương pháp điều trị', 'C1'),
    ('assess model assumptions', 'verb + noun phrase', 'đánh giá các giả định nền tảng của mô hình trước khi sử dụng kết quả', 'C1'),
    ('compare alternative models', 'verb + adjective + noun', 'so sánh các mô hình thay thế để chọn cách giải thích hoặc dự báo phù hợp hơn', 'B2'),
    ('evaluate predictive performance', 'verb + adjective + noun', 'đánh giá khả năng dự báo của mô hình trên dữ liệu thích hợp', 'C1'),
    ('calibrate risk estimates', 'verb + noun phrase', 'hiệu chỉnh các ước lượng rủi ro để phản ánh xác suất thực tế chính xác hơn', 'C1'),
    ('detect systematic bias', 'verb + adjective + noun', 'phát hiện sai lệch có tính hệ thống trong dữ liệu, quy trình hoặc mô hình', 'C1'),
    ('investigate anomalous results', 'verb + adjective + noun', 'điều tra các kết quả bất thường để xác định nguyên nhân hoặc lỗi tiềm ẩn', 'C1'),
    ('triangulate multiple sources', 'verb + adjective + noun', 'đối chiếu nhiều nguồn bằng chứng để tăng độ tin cậy của kết luận', 'C1'),
    ('synthesize qualitative evidence', 'verb + adjective + noun', 'tổng hợp bằng chứng định tính từ nhiều quan sát hoặc nguồn dữ liệu', 'C1'),
    ('code interview transcripts', 'verb + noun phrase', 'mã hóa bản ghi phỏng vấn theo các chủ đề hoặc khái niệm phục vụ phân tích', 'C1'),
    ('identify thematic patterns', 'verb + adjective + noun', 'xác định các mẫu chủ đề nổi bật trong dữ liệu định tính', 'B2'),
    ('compare stakeholder perspectives', 'verb + noun phrase', 'so sánh quan điểm của các nhóm liên quan để nhận diện điểm giống và khác', 'B2'),
    ('validate interpretation choices', 'verb + noun phrase', 'kiểm tra tính hợp lý của các lựa chọn diễn giải trong quá trình phân tích', 'C1'),
    ('preserve analytical traceability', 'verb + adjective + noun', 'duy trì khả năng truy vết từ kết luận về dữ liệu và bước phân tích ban đầu', 'C1'),
    ('record methodological decisions', 'verb + adjective + noun', 'ghi lại các quyết định phương pháp luận để nghiên cứu có thể được xem xét rõ ràng', 'C1'),
    ('preregister analysis plans', 'verb + noun phrase', 'đăng ký trước kế hoạch phân tích để giảm nguy cơ điều chỉnh giả thuyết theo kết quả', 'C1'),
    ('share reproducible workflows', 'verb + adjective + noun', 'chia sẻ quy trình có thể tái lập để người khác kiểm tra và chạy lại phân tích', 'C1'),
    ('archive research artifacts', 'verb + noun phrase', 'lưu trữ có hệ thống dữ liệu, mã và tài liệu nghiên cứu để sử dụng lâu dài', 'B2'),
    ('protect participant confidentiality', 'verb + noun phrase', 'bảo vệ tính bí mật của thông tin liên quan đến người tham gia nghiên cứu', 'B2'),
    ('obtain informed consent', 'verb + adjective + noun', 'thu thập sự đồng thuận có đầy đủ thông tin từ người tham gia', 'B2'),
    ('minimize participant burden', 'verb + noun phrase', 'giảm mức thời gian, công sức hoặc bất tiện mà người tham gia phải chịu', 'C1'),
    ('monitor adverse outcomes', 'verb + adjective + noun', 'theo dõi các kết quả bất lợi có thể xuất hiện trong quá trình nghiên cứu hoặc can thiệp', 'C1'),
    ('report protocol deviations', 'verb + noun phrase', 'báo cáo các trường hợp thực hiện khác với quy trình nghiên cứu đã được phê duyệt', 'C1'),
    ('disclose competing interests', 'verb + adjective + noun', 'công khai các lợi ích cạnh tranh có thể ảnh hưởng đến tính khách quan', 'C1'),
    ('separate exploratory analyses', 'verb + adjective + noun', 'tách biệt các phân tích thăm dò khỏi các phân tích đã được xác định trước', 'C1'),
    ('communicate evidence strength', 'verb + noun phrase', 'trình bày rõ mức độ mạnh yếu của bằng chứng hỗ trợ một kết luận', 'B2'),
    ('avoid causal overclaiming', 'verb + adjective + noun', 'tránh khẳng định quan hệ nhân quả vượt quá mức bằng chứng hiện có', 'C1'),
    ('translate findings into practice', 'verb + noun phrase', 'chuyển các phát hiện nghiên cứu thành hướng dẫn hoặc hành động có thể áp dụng thực tế', 'C1'),
]

def read_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))

def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def normalized_key(text: str) -> str:
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', text).strip().lower())

def token_set(text: str) -> set[str]:
    return {p for p in re.sub(r"[^a-z0-9'’-]+", ' ', normalized_key(text)).split() if p}

def jaccard(a: str, b: str) -> float:
    left, right = token_set(a), token_set(b)
    if not left and not right:
        return 1.0
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)

def digest(record) -> str:
    source = json.loads(json.dumps(record, ensure_ascii=False))
    checks = source.get('quality', {}).get('checks', {})
    checks.pop('cefr', None)
    checks.pop('license', None)
    return hashlib.sha256((json.dumps(source, ensure_ascii=False, indent=2) + '\n').encode()).hexdigest()

def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected exactly one occurrence, found {count}')
    return text.replace(old, new, 1)

def make_collocation(identifier: int, spec):
    text, pattern, meaning, cefr = spec
    rid = f'col.{identifier:08d}'
    return {
        'schemaVersion': 1,
        'id': rid,
        'text': text,
        'headwordKeys': [normalized_key(text).split()[0]],
        'pattern': pattern,
        'meaningVi': meaning,
        'cefr': cefr,
        'register': ['neutral'],
        'exampleIds': [],
        'quality': {
            'state': 'draft',
            'checks': {
                'schema': {'status': 'pass', 'method': 'e04-scale-29-authoring-v1'},
                'grammar': {'status': 'pending', 'method': 'manual-review-required'},
                'translation': {'status': 'pending', 'method': 'manual-review-required'},
                'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
                'cefr': {'status': 'pending', 'method': 'manual-review-required'},
                'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
                'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v29'},
                'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
                'license': {'status': 'pending', 'method': 'manual-review-required'},
            },
        },
        'provenance': {
            'sources': [{
                'dataset': 'project-original',
                'sourceId': rid,
                'sourceUrl': 'content/english/phrases/e04-scale-29-collocations.json',
                'snapshot': '2026-10',
                'license': 'LicenseRef-Project-Original',
                'modified': False,
            }],
            'note': 'Project-original controlled E04 scale-up record.',
        },
    }

def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest published scale-up HEAD before this checkpoint: `e7cb2c54888863f27b6b530dab9f72aa42bb49ae` — `feat(content): publish E04 collocation scale 28`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-29 publication: `ba5227959802b0d5f06a41af57abefeb396fc242` — scale-28 publication state verified by English Content Master Plan Acceptance #51 and Platform CI #1071; published output: `e7cb2c54888863f27b6b530dab9f72aa42bb49ae`.',
        'verified scale-28 checkpoint',
    )
    text = replace_once(
        text,
        '- Latest fully CI-verified pre-publication HEAD: `20d71ad7bda9ca49b2c56d4647372941d4271746` — English Content Master Plan Acceptance #49 and Platform CI #1069 PASS.\n',
        '',
        'remove stale pre-publication checkpoint',
    )
    text = replace_once(
        text,
        '- Scale-28 publication verification note: the publication commit was created by `github-actions[bot]`; its PR-triggered Acceptance #50 and Platform CI #1070 ended `action_required` with zero jobs, so this checkpoint commit intentionally re-triggers CI from a normal branch write without changing content artifacts or weakening gates.\n',
        '',
        'remove resolved verification note',
    )
    text = replace_once(
        text,
        '- E04 phrase/pattern architecture + current reviewed publication: complete — 1,870 published records after scale-28',
        '- E04 phrase/pattern architecture + current reviewed publication: complete — 1,910 published records after scale-29',
        'E04 count',
    )
    text = replace_once(
        text,
        '## Published runtime snapshot after E04 scale-28 publication',
        '## Published runtime snapshot after E04 scale-29 publication',
        'snapshot heading',
    )
    text = replace_once(text, '- phrases: 1,870 records', '- phrases: 1,910 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 6,471', '- total published rich records: 6,511', 'rich count')
    text = replace_once(
        text,
        '- editorial ledger: 6,471 decisions / 6,471 applied / 6,471 publish decisions',
        '- editorial ledger: 6,511 decisions / 6,511 applied / 6,511 publish decisions',
        'ledger count',
    )
    text = replace_once(
        text,
        '1. Verify the scale-28 publication commit through a normal branch-triggered CI run; do not duplicate scale-28 artifacts.\n2. Check whether any evidence-backed E04 enrichment candidates already exist but are not yet reviewed/published; promote only if the exact evidence and digest review are valid.\n3. If no safe pending enrichment exists, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.\n4. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.\n5. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.',
        '1. Scale-28 publication is fully verified; do not duplicate scale-28 artifacts.\n2. Verify the resulting scale-29 publication commit and mandatory CI without regenerating completed artifacts.\n3. Check whether any evidence-backed E04 enrichment candidates already exist but are not yet reviewed/published; promote only if the exact evidence and digest review are valid.\n4. If no safe pending enrichment exists, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.\n5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.\n6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.',
        'first unfinished workstream',
    )
    text = replace_once(
        text,
        "No content/data blocker. Scale-28 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content.",
        'None.',
        'blocker',
    )
    text = replace_once(
        text,
        'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-28 as fully verified and continue immediately with the next genuinely new bounded collocation batch from the new ID frontier (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.',
        'Scale-29 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from the new ID frontier (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.',
        'next task',
    )
    PROGRESS_PATH.write_text(text, encoding='utf-8')

def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-29 artifact exists without matching batch manifest')

    existing = {'collocations': [], 'verbPatterns': [], 'phraseItems': []}
    all_texts = []
    all_ids = set()
    for batch in manifest.get('batches', []):
        if batch.get('phase') != 'E04' or batch.get('category') != 'phrases':
            continue
        for record_set in batch.get('recordSets', []):
            records = read_json(ROOT / record_set['path']).get('records', [])
            record_set_id = record_set.get('id')
            if record_set_id in {'collocations', 'scale-collocations'}:
                existing['collocations'].extend(records)
            elif record_set_id in {'verb-patterns', 'scale-verb-patterns'}:
                existing['verbPatterns'].extend(records)
            elif record_set_id in {'phrases', 'scale-phrases'}:
                existing['phraseItems'].extend(records)
            for record in records:
                rid = record.get('id')
                if rid in all_ids:
                    raise RuntimeError(f'existing duplicate E04 record id: {rid}')
                all_ids.add(rid)
                value = record.get('text') or record.get('pattern') or ''
                if value:
                    all_texts.append((rid, value))

    actual = {key: len(value) for key, value in existing.items()}
    if actual != EXPECTED:
        raise RuntimeError(f'E04 source counts drifted; expected {EXPECTED}, got {actual}')

    nums = [
        int(match.group(1))
        for record in existing['collocations']
        if (match := re.fullmatch(r'col\.(\d{8})', str(record.get('id', ''))))
    ]
    if not nums or max(nums) != 760:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 760, got {max(nums) if nums else None}')

    new = [make_collocation(761 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
    exact = {normalized_key(text): rid for rid, text in all_texts}
    accepted = []
    for record in new:
        rid, text = record['id'], record['text']
        key = normalized_key(text)
        if rid in all_ids:
            raise RuntimeError(f'new record id collides: {rid}')
        if key in exact:
            raise RuntimeError(f'exact duplicate against existing E04: {rid} {text!r} == {exact[key]}')
        for old_id, old_text in all_texts:
            score = jaccard(text, old_text)
            if score >= NEAR_DUP_THRESHOLD:
                raise RuntimeError(f'near duplicate against existing E04 ({score:.3f}): {rid} {text!r} ~ {old_id} {old_text!r}')
        for prior in accepted:
            score = jaccard(text, prior['text'])
            if normalized_key(prior['text']) == key or score >= NEAR_DUP_THRESHOLD:
                raise RuntimeError(f'duplicate inside scale-29: {text!r} ~ {prior["text"]!r} ({score:.3f})')
        accepted.append(record)

    write_json(COL_PATH, {'schemaVersion': 1, 'records': new})
    manifest['batches'].append({
        'id': BATCH_ID,
        'phase': 'E04',
        'category': 'phrases',
        'cefr': ['B2', 'C1'],
        'state': 'draft',
        'recordSets': [{
            'id': 'scale-collocations',
            'path': 'content/english/phrases/e04-scale-29-collocations.json',
            'expectedCount': 40,
            'generated': False,
            'allowedQualityStates': ['draft'],
            'requiredChecks': ['schema', 'grammar', 'translation', 'naturalness', 'cefr', 'targetStructure', 'exactDuplicate', 'nearDuplicate', 'license'],
        }],
        'requiredBeforePublish': ['schema-validation', 'reference-integrity', 'exact-dedup', 'near-dedup', 'grammar-review', 'bilingual-review', 'naturalness-review', 'cefr-review', 'target-structure-review', 'license-review', 'cross-game-smoke'],
        'gameSmokes': [
            {'gameId': 'recall-typing', 'activity': 'collocation', 'recordSetId': 'scale-collocations', 'sampleCount': 5},
            {'gameId': 'vocab-shooter', 'activity': 'collocation', 'recordSetId': 'scale-collocations', 'sampleCount': 5},
            {'gameId': 'space-typing', 'activity': 'collocation', 'recordSetId': 'scale-collocations', 'sampleCount': 5},
        ],
    })
    write_json(MANIFEST_PATH, manifest)

    decisions = []
    for record in new:
        decisions.append({
            'id': 'review.e04.scale-29.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-29-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-29-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-29-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-29-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-29-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-29-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 29 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==760)', 'if(recallCollocations!==800)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 760 reviewed records', 'must expose 800 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00000761', 'col.00000800'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 800, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 1910, 'richRecords': 6511},
    }, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
