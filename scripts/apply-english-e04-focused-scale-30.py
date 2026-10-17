#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-30-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-30.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-30'
REVIEWED_AT = '2026-10-07T02:28:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-30'
EXPECTED = {'collocations': 800, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('enforce access controls', 'verb + noun phrase', 'thực thi các biện pháp kiểm soát nhằm giới hạn quyền truy cập vào hệ thống hoặc dữ liệu', 'B2'),
    ('rotate encryption keys', 'verb + noun phrase', 'thay đổi định kỳ các khóa mã hóa để giảm rủi ro khi khóa cũ bị lộ', 'C1'),
    ('revoke compromised credentials', 'verb + adjective + noun', 'thu hồi thông tin xác thực đã bị lộ hoặc không còn đáng tin cậy', 'C1'),
    ('patch critical vulnerabilities', 'verb + adjective + noun', 'vá các lỗ hổng nghiêm trọng có thể gây rủi ro lớn cho hệ thống', 'B2'),
    ('harden exposed services', 'verb + adjective + noun', 'gia cố các dịch vụ có thể truy cập từ bên ngoài để giảm bề mặt tấn công', 'C1'),
    ('segment internal networks', 'verb + adjective + noun', 'phân đoạn mạng nội bộ để hạn chế phạm vi di chuyển của sự cố hoặc kẻ tấn công', 'C1'),
    ('isolate infected endpoints', 'verb + adjective + noun', 'cô lập các thiết bị đầu cuối bị nhiễm để ngăn mã độc tiếp tục lây lan', 'B2'),
    ('triage security alerts', 'verb + noun phrase', 'phân loại và ưu tiên các cảnh báo bảo mật để xử lý theo mức độ rủi ro', 'C1'),
    ('correlate threat indicators', 'verb + noun phrase', 'đối chiếu các chỉ dấu đe dọa để nhận diện mối liên hệ giữa nhiều tín hiệu', 'C1'),
    ('preserve forensic evidence', 'verb + adjective + noun', 'bảo toàn bằng chứng phục vụ điều tra pháp chứng mà không làm thay đổi dữ liệu gốc', 'C1'),
    ('reconstruct attack timelines', 'verb + noun phrase', 'tái dựng dòng thời gian của cuộc tấn công dựa trên log và bằng chứng thu thập được', 'C1'),
    ('contain lateral movement', 'verb + adjective + noun', 'kiềm chế việc kẻ tấn công di chuyển ngang giữa các hệ thống sau khi xâm nhập', 'C1'),
    ('eradicate malicious persistence', 'verb + adjective + noun', 'loại bỏ cơ chế duy trì hiện diện độc hại mà kẻ tấn công cài trong hệ thống', 'C1'),
    ('restore trusted backups', 'verb + adjective + noun', 'khôi phục dữ liệu từ các bản sao lưu đã được xác minh là đáng tin cậy', 'B2'),
    ('verify recovery integrity', 'verb + noun phrase', 'xác minh tính toàn vẹn của hệ thống và dữ liệu sau quá trình khôi phục', 'C1'),
    ('conduct tabletop exercises', 'verb + noun phrase', 'tổ chức diễn tập mô phỏng trên bàn để kiểm tra cách nhóm phản ứng trước sự cố', 'C1'),
    ('test incident playbooks', 'verb + noun phrase', 'kiểm thử các kịch bản hướng dẫn ứng phó sự cố để phát hiện điểm thiếu hoặc không thực tế', 'B2'),
    ('assign response ownership', 'verb + noun phrase', 'phân công rõ người hoặc nhóm chịu trách nhiệm cho từng phần của hoạt động ứng phó', 'B2'),
    ('escalate confirmed incidents', 'verb + adjective + noun', 'chuyển các sự cố đã được xác nhận lên cấp xử lý phù hợp theo quy trình', 'B2'),
    ('notify affected parties', 'verb + adjective + noun', 'thông báo cho các bên bị ảnh hưởng bằng thông tin phù hợp và đúng thời điểm', 'B2'),
    ('meet breach notification obligations', 'verb + noun phrase', 'đáp ứng các nghĩa vụ thông báo khi xảy ra vi phạm dữ liệu theo yêu cầu áp dụng', 'C1'),
    ('classify information assets', 'verb + noun phrase', 'phân loại tài sản thông tin theo mức độ nhạy cảm, giá trị hoặc yêu cầu bảo vệ', 'B2'),
    ('map data dependencies', 'verb + noun phrase', 'lập bản đồ các phụ thuộc dữ liệu giữa hệ thống, quy trình và dịch vụ', 'C1'),
    ('minimize privileged access', 'verb + adjective + noun', 'giảm quyền truy cập đặc quyền xuống mức tối thiểu cần thiết cho công việc', 'B2'),
    ('review dormant accounts', 'verb + adjective + noun', 'rà soát các tài khoản không hoạt động để xác định tài khoản cần vô hiệu hóa hoặc loại bỏ', 'B2'),
    ('monitor anomalous traffic', 'verb + adjective + noun', 'giám sát lưu lượng bất thường có thể cho thấy hành vi xâm nhập hoặc lạm dụng', 'C1'),
    ('detect credential stuffing', 'verb + noun phrase', 'phát hiện hành vi thử hàng loạt thông tin đăng nhập bị rò rỉ trên nhiều tài khoản', 'C1'),
    ('block malicious payloads', 'verb + adjective + noun', 'chặn các tải trọng độc hại trước khi chúng được thực thi hoặc chuyển tiếp', 'B2'),
    ('quarantine suspicious files', 'verb + adjective + noun', 'cách ly các tệp đáng ngờ để ngăn chúng gây ảnh hưởng trong khi được phân tích', 'B2'),
    ('tune detection rules', 'verb + noun phrase', 'tinh chỉnh các quy tắc phát hiện để tăng tín hiệu hữu ích và giảm cảnh báo sai', 'C1'),
    ('suppress noisy alerts', 'verb + adjective + noun', 'giảm hoặc chặn các cảnh báo nhiều nhiễu nhưng ít giá trị điều tra', 'C1'),
    ('prioritize remediation work', 'verb + noun phrase', 'ưu tiên công việc khắc phục dựa trên mức độ rủi ro, ảnh hưởng và khả năng khai thác', 'B2'),
    ('track vulnerability exposure', 'verb + noun phrase', 'theo dõi mức độ phơi nhiễm trước lỗ hổng của hệ thống theo thời gian', 'C1'),
    ('validate patch deployment', 'verb + noun phrase', 'xác nhận bản vá đã được triển khai đúng phạm vi và hoạt động như mong đợi', 'B2'),
    ('document security exceptions', 'verb + noun phrase', 'ghi lại các ngoại lệ bảo mật cùng lý do, phạm vi và biện pháp bù trừ', 'B2'),
    ('approve residual risk', 'verb + adjective + noun', 'phê duyệt phần rủi ro còn lại sau khi các biện pháp xử lý đã được áp dụng', 'C1'),
    ('enforce retention policies', 'verb + noun phrase', 'thực thi chính sách lưu giữ để dữ liệu được giữ đúng thời hạn quy định', 'B2'),
    ('dispose of sensitive records', 'verb + preposition + adjective + noun', 'tiêu hủy hoặc loại bỏ hồ sơ nhạy cảm theo phương thức an toàn và có kiểm soát', 'B2'),
    ('audit third-party access', 'verb + adjective + noun', 'kiểm toán quyền truy cập của bên thứ ba để phát hiện quyền thừa hoặc không còn hợp lệ', 'C1'),
    ('verify supplier controls', 'verb + noun phrase', 'xác minh các biện pháp kiểm soát của nhà cung cấp đáp ứng yêu cầu bảo mật đã thống nhất', 'C1'),
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
                'schema': {'status': 'pass', 'method': 'e04-scale-30-authoring-v1'},
                'grammar': {'status': 'pending', 'method': 'manual-review-required'},
                'translation': {'status': 'pending', 'method': 'manual-review-required'},
                'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
                'cefr': {'status': 'pending', 'method': 'manual-review-required'},
                'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
                'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v30'},
                'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
                'license': {'status': 'pending', 'method': 'manual-review-required'},
            },
        },
        'provenance': {
            'sources': [{
                'dataset': 'project-original',
                'sourceId': rid,
                'sourceUrl': 'content/english/phrases/e04-scale-30-collocations.json',
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
        '- Latest published scale-up HEAD before this checkpoint: `e28d43daecc41c312d51a9a4e1382f5152e2af16` — `feat(content): publish E04 collocation scale 29`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-30 publication: `e8c94d8bc9a6d58896acee3b7d0f0fd7279ab6cf` — scale-29 publication state verified by English Content Master Plan Acceptance #54 and Platform CI #1074; published output: `e28d43daecc41c312d51a9a4e1382f5152e2af16`.',
        'verified scale-29 checkpoint',
    )
    text = replace_once(
        text,
        '- Latest fully CI-verified pre-publication HEAD: `f602319c51c7aa39891837294114ca8384868d0a` — Apply English E04 Scale 29 #1, English Content Full Validation #68, English Content Master Plan Acceptance #52 and Platform CI #1072 all PASS.\n',
        '',
        'remove scale-29 prep checkpoint',
    )
    text = replace_once(
        text,
        '- Scale-29 publication verification note: the publication commit was created by `github-actions[bot]`; its PR-triggered English Content Master Plan Acceptance #53 and Platform CI #1073 ended `action_required` before jobs ran, so this checkpoint intentionally re-triggers the same mandatory CI from a normal branch write without regenerating scale-29 content or weakening any gate.\n',
        '',
        'remove resolved scale-29 verification note',
    )
    text = replace_once(
        text,
        '- E04 phrase/pattern architecture + current reviewed publication: complete — 1,910 published records after scale-29',
        '- E04 phrase/pattern architecture + current reviewed publication: complete — 1,950 published records after scale-30',
        'E04 count',
    )
    text = replace_once(
        text,
        '## Published runtime snapshot after E04 scale-29 publication',
        '## Published runtime snapshot after E04 scale-30 publication',
        'snapshot heading',
    )
    text = replace_once(text, '- phrases: 1,910 records', '- phrases: 1,950 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 6,511', '- total published rich records: 6,551', 'rich count')
    text = replace_once(
        text,
        '- editorial ledger: 6,511 decisions / 6,511 applied / 6,511 publish decisions',
        '- editorial ledger: 6,551 decisions / 6,551 applied / 6,551 publish decisions',
        'ledger count',
    )
    old_workstream = '''1. Verify scale-29 publication state through the normal-user checkpoint CI; do not duplicate scale-29 artifacts.
2. Check whether any evidence-backed E04 enrichment candidates already exist but are not yet reviewed/published; promote only if the exact evidence and digest review are valid.
3. If no safe pending enrichment exists, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
4. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
5. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-29 publication is fully verified; do not duplicate scale-29 artifacts.
2. The Acceptance #54 enrichment evidence scan found whole-phrase candidates only for the already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-30 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safe pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-29 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-29 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00000800` (expected scale-30 range `col.00000801` through `col.00000840` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-30 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from the new frontier `col.00000840` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')

def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-30 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 800:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 800, got {max(nums) if nums else None}')

    new = [make_collocation(801 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-30: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-30-collocations.json',
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
            'id': 'review.e04.scale-30.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-30-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-30-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-30-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-30-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-30-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-30-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 30 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==800)', 'if(recallCollocations!==840)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 800 reviewed records', 'must expose 840 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00000801', 'col.00000840'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 840, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 1950, 'richRecords': 6551},
    }, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
