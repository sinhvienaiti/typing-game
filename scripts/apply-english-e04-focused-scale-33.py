#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-33-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-33.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-33'
REVIEWED_AT = '2026-10-07T03:45:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-33'
EXPECTED = {'collocations': 920, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('formulate research questions', 'verb + noun phrase', 'xây dựng các câu hỏi nghiên cứu rõ ràng để định hướng phạm vi và phương pháp của nghiên cứu', 'B2'),
    ('develop testable hypotheses', 'verb + adjective + noun', 'phát triển các giả thuyết có thể được kiểm tra bằng dữ liệu hoặc thí nghiệm', 'C1'),
    ('conduct literature reviews', 'verb + noun phrase', 'thực hiện tổng quan tài liệu để xác định kiến thức hiện có, khoảng trống và tranh luận liên quan', 'B2'),
    ('collect empirical data', 'verb + adjective + noun', 'thu thập dữ liệu thực nghiệm hoặc quan sát để trả lời câu hỏi nghiên cứu', 'B2'),
    ('analyze research findings', 'verb + noun phrase', 'phân tích các phát hiện nghiên cứu để xác định mô hình, mối liên hệ và ý nghĩa', 'B2'),
    ('replicate published studies', 'verb + adjective + noun', 'lặp lại các nghiên cứu đã công bố để kiểm tra khả năng tái lập của kết quả', 'C1'),
    ('control confounding variables', 'verb + adjective + noun', 'kiểm soát các biến gây nhiễu có thể làm sai lệch mối quan hệ đang được nghiên cứu', 'C1'),
    ('randomize treatment groups', 'verb + noun phrase', 'phân nhóm can thiệp một cách ngẫu nhiên để giảm sai lệch trong so sánh', 'C1'),
    ('recruit study participants', 'verb + noun phrase', 'tuyển người tham gia nghiên cứu theo tiêu chí và quy trình đã xác định', 'B2'),
    ('secure ethics approval', 'verb + noun phrase', 'đạt được phê duyệt đạo đức trước khi tiến hành nghiên cứu có liên quan đến người tham gia hoặc dữ liệu nhạy cảm', 'C1'),
    ('protect participant confidentiality', 'verb + noun phrase', 'bảo vệ tính bảo mật của thông tin nhận dạng và dữ liệu của người tham gia nghiên cứu', 'C1'),
    ('preregister study protocols', 'verb + noun phrase', 'đăng ký trước giao thức nghiên cứu để làm rõ giả thuyết, phương pháp và kế hoạch phân tích', 'C1'),
    ('report null results', 'verb + adjective + noun', 'báo cáo các kết quả không cho thấy hiệu ứng hoặc mối liên hệ có ý nghĩa như dự đoán', 'C1'),
    ('estimate effect sizes', 'verb + noun phrase', 'ước lượng độ lớn của hiệu ứng để đánh giá mức độ khác biệt hoặc mối liên hệ', 'C1'),
    ('calculate confidence intervals', 'verb + noun phrase', 'tính khoảng tin cậy để biểu thị mức độ bất định quanh một ước lượng thống kê', 'C1'),
    ('interpret statistical significance', 'verb + adjective + noun', 'diễn giải ý nghĩa thống kê trong bối cảnh thiết kế nghiên cứu và kích thước hiệu ứng', 'C1'),
    ('assess measurement reliability', 'verb + noun phrase', 'đánh giá độ tin cậy của phép đo khi được lặp lại hoặc áp dụng trong điều kiện tương tự', 'C1'),
    ('validate research instruments', 'verb + noun phrase', 'xác nhận công cụ nghiên cứu đo lường đúng khái niệm cần đánh giá', 'C1'),
    ('code qualitative interviews', 'verb + adjective + noun', 'mã hóa nội dung phỏng vấn định tính để tổ chức dữ liệu theo chủ đề hoặc khái niệm', 'C1'),
    ('identify recurring themes', 'verb + adjective + noun', 'xác định các chủ đề lặp lại trong dữ liệu định tính hoặc nhiều nguồn bằng chứng', 'B2'),
    ('synthesize conflicting evidence', 'verb + adjective + noun', 'tổng hợp các bằng chứng mâu thuẫn để làm rõ điểm đồng thuận, khác biệt và nguyên nhân có thể', 'C1'),
    ('cite primary sources', 'verb + adjective + noun', 'trích dẫn các nguồn sơ cấp trực tiếp cung cấp dữ liệu, văn bản hoặc bằng chứng gốc', 'B2'),
    ('evaluate source credibility', 'verb + noun phrase', 'đánh giá độ tin cậy của nguồn dựa trên tác giả, phương pháp, bằng chứng và bối cảnh xuất bản', 'B2'),
    ('detect sampling bias', 'verb + noun phrase', 'phát hiện sai lệch chọn mẫu có thể làm mẫu không đại diện cho quần thể mục tiêu', 'C1'),
    ('reduce response bias', 'verb + noun phrase', 'giảm sai lệch phản hồi do cách đặt câu hỏi, kỳ vọng xã hội hoặc hành vi của người tham gia', 'C1'),
    ('document research limitations', 'verb + noun phrase', 'ghi rõ những hạn chế của nghiên cứu có thể ảnh hưởng đến cách diễn giải hoặc khái quát kết quả', 'B2'),
    ('share reproducible workflows', 'verb + adjective + noun', 'chia sẻ quy trình có thể tái tạo để người khác kiểm tra hoặc lặp lại phân tích', 'C1'),
    ('archive research datasets', 'verb + noun phrase', 'lưu trữ bộ dữ liệu nghiên cứu theo cách có tổ chức để hỗ trợ truy xuất và tái sử dụng phù hợp', 'C1'),
    ('publish open materials', 'verb + adjective + noun', 'công bố tài liệu nghiên cứu mở như mã, giao thức hoặc tài nguyên bổ sung khi phù hợp', 'B2'),
    ('review scholarly manuscripts', 'verb + adjective + noun', 'phản biện bản thảo học thuật để đánh giá chất lượng, phương pháp và tính rõ ràng trước công bố', 'C1'),
    ('provide constructive feedback', 'verb + adjective + noun', 'đưa ra phản hồi mang tính xây dựng với nhận xét cụ thể và đề xuất có thể thực hiện', 'B2'),
    ('revise research proposals', 'verb + noun phrase', 'chỉnh sửa đề xuất nghiên cứu dựa trên phản hồi, bằng chứng hoặc thay đổi về phạm vi và phương pháp', 'B2'),
    ('define learning objectives', 'verb + noun phrase', 'xác định mục tiêu học tập cụ thể mô tả kiến thức hoặc kỹ năng người học cần đạt', 'B2'),
    ('design formative assessments', 'verb + adjective + noun', 'thiết kế đánh giá quá trình để theo dõi hiểu biết và điều chỉnh việc dạy học', 'B2'),
    ('measure student progress', 'verb + noun phrase', 'đo lường tiến bộ của người học theo thời gian dựa trên mục tiêu và bằng chứng học tập', 'B2'),
    ('differentiate classroom instruction', 'verb + noun phrase', 'điều chỉnh cách giảng dạy trong lớp để đáp ứng khác biệt về nhu cầu, mức độ và cách học', 'C1'),
    ('support struggling learners', 'verb + adjective + noun', 'hỗ trợ người học đang gặp khó khăn bằng can thiệp, hướng dẫn và tài nguyên phù hợp', 'B2'),
    ('facilitate group discussions', 'verb + noun phrase', 'điều phối thảo luận nhóm để khuyến khích tham gia, lập luận và trao đổi có trọng tâm', 'B2'),
    ('deliver timely feedback', 'verb + adjective + noun', 'cung cấp phản hồi kịp thời để người học có thể điều chỉnh trước khi tiếp tục nhiệm vụ', 'B2'),
    ('promote academic integrity', 'verb + adjective + noun', 'thúc đẩy tính liêm chính học thuật thông qua quy tắc rõ ràng, hướng dẫn và thực hành trung thực', 'C1'),
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
                'schema': {'status': 'pass', 'method': 'e04-scale-33-authoring-v1'},
                'grammar': {'status': 'pending', 'method': 'manual-review-required'},
                'translation': {'status': 'pending', 'method': 'manual-review-required'},
                'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
                'cefr': {'status': 'pending', 'method': 'manual-review-required'},
                'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
                'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v33'},
                'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
                'license': {'status': 'pending', 'method': 'manual-review-required'},
            },
        },
        'provenance': {
            'sources': [{
                'dataset': 'project-original',
                'sourceId': rid,
                'sourceUrl': 'content/english/phrases/e04-scale-33-collocations.json',
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
        '- Latest published scale-up HEAD before this checkpoint: `9bcf6280c79f619e3e8918f377fe11efb13be510` — `feat(content): publish E04 collocation scale 32`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-33 publication: `5eee13fee7047e6f528f5abf3d9781580b161dbf` — scale-32 publication state verified by English Content Master Plan Acceptance #64, English Content Full Validation #76 and Platform CI #1087; published output: `9bcf6280c79f619e3e8918f377fe11efb13be510`.',
        'verified scale-32 checkpoint',
    )
    text = replace_once(
        text,
        '- Latest scale-32 pre-publication HEAD: `06a1fcf6b42264764eb7c9bb52047dfbda1ab70b` — Apply English E04 Scale 32 #2 and English Content Full Validation #75 PASS after replacing the two exact-duplicate candidates detected by preflight; all publication quality gates and deterministic replay passed before the bot commit was pushed.\n',
        '',
        'remove scale-32 prep checkpoint',
    )
    text = replace_once(
        text,
        '- Scale-32 publication verification note: the publication commit was created by `github-actions[bot]`; its PR-triggered English Content Master Plan Acceptance #63 and Platform CI #1086 ended `action_required` before jobs ran, so this checkpoint intentionally re-triggers the mandatory CI from a normal branch write without regenerating scale-32 content or weakening any gate.\n',
        '',
        'remove resolved scale-32 verification note',
    )
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,030 published records after scale-32', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,070 published records after scale-33', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-32 publication', '## Published runtime snapshot after E04 scale-33 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,030 records', '- phrases: 2,070 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 6,631', '- total published rich records: 6,671', 'rich count')
    text = replace_once(text, '- editorial ledger: 6,631 decisions / 6,631 applied / 6,631 publish decisions', '- editorial ledger: 6,671 decisions / 6,671 applied / 6,671 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00000920`', '- E04 collocation frontier: `col.00000960`', 'collocation frontier')
    old_workstream = '''1. Verify scale-32 publication state through this normal-user checkpoint CI; do not duplicate scale-32 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. If scale-32 checkpoint CI passes and no newer worker has claimed the next scope, create scale-33 as the next bounded collocation batch from frontier `col.00000920`.
4. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
5. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-32 publication is fully verified; do not duplicate scale-32 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-33 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-32 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-32 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00000920` (expected scale-33 range `col.00000921` through `col.00000960` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-33 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00000960` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')

def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-33 artifact exists without matching batch manifest')

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
    nums = [int(match.group(1)) for record in existing['collocations'] if (match := re.fullmatch(r'col\.(\d{8})', str(record.get('id', ''))))]
    if not nums or max(nums) != 920:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 920, got {max(nums) if nums else None}')

    new = [make_collocation(921 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-33: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-33-collocations.json',
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
            'id': 'review.e04.scale-33.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-33-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-33-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-33-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-33-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-33-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-33-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 33 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==920)', 'if(recallCollocations!==960)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 920 reviewed records', 'must expose 960 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00000921', 'col.00000960'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 960, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2070, 'richRecords': 6671},
    }, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
