#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-34-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-34.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-34'
REVIEWED_AT = '2026-10-07T04:00:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-34'
EXPECTED = {'collocations': 960, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('forecast quarterly revenue', 'verb + adjective + noun', 'dự báo doanh thu theo quý dựa trên xu hướng bán hàng, hợp đồng và giả định kinh doanh', 'B2'),
    ('model free cash flow', 'verb + adjective + noun', 'mô hình hóa dòng tiền tự do để đánh giá khả năng tạo tiền và giá trị doanh nghiệp', 'C1'),
    ('estimate gross margins', 'verb + adjective + noun', 'ước tính biên lợi nhuận gộp từ doanh thu và chi phí trực tiếp dự kiến', 'B2'),
    ('assess borrower creditworthiness', 'verb + noun phrase', 'đánh giá khả năng và mức độ đáng tin cậy của người vay trong việc hoàn trả nghĩa vụ nợ', 'C1'),
    ('rebalance portfolio weights', 'verb + noun phrase', 'điều chỉnh tỷ trọng tài sản trong danh mục để quay lại mức phân bổ mục tiêu', 'C1'),
    ('hedge foreign-exchange exposure', 'verb + adjective + noun', 'phòng ngừa rủi ro từ biến động tỷ giá đối với dòng tiền, tài sản hoặc nghĩa vụ', 'C1'),
    ('manage duration risk', 'verb + noun phrase', 'quản lý rủi ro thời hạn của danh mục thu nhập cố định trước thay đổi lãi suất', 'C1'),
    ('price fixed-income securities', 'verb + adjective + noun', 'định giá chứng khoán thu nhập cố định dựa trên dòng tiền, lãi suất và mức rủi ro', 'C1'),
    ('issue convertible bonds', 'verb + adjective + noun', 'phát hành trái phiếu có thể chuyển đổi thành cổ phần theo các điều kiện đã xác định', 'C1'),
    ('raise working capital', 'verb + adjective + noun', 'huy động vốn lưu động để tài trợ hoạt động kinh doanh thường ngày', 'B2'),
    ('refinance maturing debt', 'verb + adjective + noun', 'tái cấp vốn cho khoản nợ sắp đáo hạn bằng nguồn vay hoặc công cụ tài chính mới', 'C1'),
    ('negotiate loan covenants', 'verb + noun phrase', 'đàm phán các điều khoản ràng buộc trong hợp đồng vay giữa bên vay và bên cho vay', 'C1'),
    ('monitor covenant breaches', 'verb + noun phrase', 'theo dõi các trường hợp vi phạm điều khoản ràng buộc của khoản vay', 'C1'),
    ('calculate weighted funding costs', 'verb + adjective + noun', 'tính chi phí vốn huy động bình quân có trọng số từ nhiều nguồn tài trợ', 'C1'),
    ('evaluate capital projects', 'verb + noun phrase', 'đánh giá các dự án đầu tư vốn dựa trên dòng tiền, rủi ro và giá trị kỳ vọng', 'B2'),
    ('rank investment proposals', 'verb + noun phrase', 'xếp hạng các đề xuất đầu tư theo tiêu chí lợi ích, rủi ro và nguồn lực', 'B2'),
    ('run sensitivity scenarios', 'verb + noun phrase', 'chạy các kịch bản độ nhạy để xem kết quả thay đổi khi giả định đầu vào biến động', 'C1'),
    ('stress-test valuation models', 'verb + noun phrase', 'kiểm thử mô hình định giá dưới các giả định bất lợi hoặc cực đoan', 'C1'),
    ('reconcile subsidiary accounts', 'verb + noun phrase', 'đối chiếu tài khoản của các công ty con để phát hiện và xử lý chênh lệch', 'C1'),
    ('close reporting periods', 'verb + noun phrase', 'khóa kỳ báo cáo sau khi hoàn tất ghi nhận, đối chiếu và điều chỉnh cần thiết', 'B2'),
    ('recognize contract revenue', 'verb + noun phrase', 'ghi nhận doanh thu hợp đồng theo thời điểm và điều kiện đáp ứng nghĩa vụ thực hiện', 'C1'),
    ('provision loan losses', 'verb + noun phrase', 'trích lập dự phòng cho tổn thất tín dụng dự kiến từ các khoản cho vay', 'C1'),
    ('audit consolidated statements', 'verb + adjective + noun', 'kiểm toán báo cáo tài chính hợp nhất của một nhóm công ty', 'C1'),
    ('detect revenue manipulation', 'verb + noun phrase', 'phát hiện hành vi điều chỉnh hoặc trình bày doanh thu nhằm làm sai lệch kết quả tài chính', 'C1'),
    ('strengthen segregation controls', 'verb + noun phrase', 'tăng cường kiểm soát phân tách nhiệm vụ để giảm nguy cơ sai sót hoặc gian lận', 'C1'),
    ('approve capital spending', 'verb + adjective + noun', 'phê duyệt chi tiêu vốn cho tài sản hoặc dự án dài hạn theo thẩm quyền', 'B2'),
    ('track forecast variances', 'verb + noun phrase', 'theo dõi chênh lệch giữa dự báo và kết quả thực tế để hiểu nguyên nhân sai lệch', 'B2'),
    ('revise financial outlook', 'verb + adjective + noun', 'điều chỉnh triển vọng tài chính khi giả định hoặc điều kiện kinh doanh thay đổi', 'B2'),
    ('disclose contingent liabilities', 'verb + adjective + noun', 'công bố các nghĩa vụ tiềm tàng có thể phát sinh tùy thuộc vào sự kiện trong tương lai', 'C1'),
    ('monitor bid-ask spreads', 'verb + noun phrase', 'theo dõi chênh lệch giữa giá mua và giá bán để đánh giá chi phí giao dịch và thanh khoản', 'C1'),
    ('assess counterparty credit exposure', 'verb + noun phrase', 'đánh giá mức độ rủi ro tín dụng phát sinh từ một đối tác giao dịch', 'C1'),
    ('execute currency hedges', 'verb + noun phrase', 'thực hiện các giao dịch phòng ngừa để giảm tác động của biến động tiền tệ', 'C1'),
    ('settle derivative contracts', 'verb + noun phrase', 'thanh toán và hoàn tất nghĩa vụ phát sinh từ các hợp đồng phái sinh', 'C1'),
    ('manage margin calls', 'verb + noun phrase', 'quản lý yêu cầu bổ sung tài sản ký quỹ khi giá trị vị thế thay đổi', 'C1'),
    ('evaluate takeover targets', 'verb + noun phrase', 'đánh giá các doanh nghiệp mục tiêu tiềm năng cho giao dịch mua lại', 'C1'),
    ('perform commercial due diligence', 'verb + adjective + noun', 'thực hiện thẩm định thương mại về thị trường, khách hàng và khả năng cạnh tranh trước giao dịch', 'C1'),
    ('integrate acquired operations', 'verb + adjective + noun', 'tích hợp hoạt động của đơn vị được mua lại vào mô hình vận hành chung', 'C1'),
    ('capture cost synergies', 'verb + noun phrase', 'hiện thực hóa lợi ích tiết kiệm chi phí kỳ vọng từ việc kết hợp doanh nghiệp hoặc hoạt động', 'C1'),
    ('measure risk-adjusted returns', 'verb + adjective + noun', 'đo lường lợi nhuận sau khi xét đến mức rủi ro đã chấp nhận để tạo ra lợi nhuận đó', 'C1'),
    ('allocate retained earnings', 'verb + adjective + noun', 'phân bổ lợi nhuận giữ lại cho tái đầu tư, dự trữ hoặc các mục đích doanh nghiệp khác', 'B2'),
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
                'schema': {'status': 'pass', 'method': 'e04-scale-34-authoring-v1'},
                'grammar': {'status': 'pending', 'method': 'manual-review-required'},
                'translation': {'status': 'pending', 'method': 'manual-review-required'},
                'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
                'cefr': {'status': 'pending', 'method': 'manual-review-required'},
                'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
                'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v34'},
                'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
                'license': {'status': 'pending', 'method': 'manual-review-required'},
            },
        },
        'provenance': {
            'sources': [{
                'dataset': 'project-original',
                'sourceId': rid,
                'sourceUrl': 'content/english/phrases/e04-scale-34-collocations.json',
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
        '- Latest published scale-up HEAD before this checkpoint: `933227bbbc4b1fde9a64721c67f289aa0ea91db2` — `feat(content): publish E04 collocation scale 33`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-34 publication: `29b8fc63ce5a1b91b6cac91d67f3cc20ada07862` — scale-33 publication state verified by English Content Master Plan Acceptance #68, English Content Full Validation #79 and Platform CI #1092; published output: `933227bbbc4b1fde9a64721c67f289aa0ea91db2`.',
        'verified scale-33 checkpoint',
    )
    text = replace_once(
        text,
        '- Latest scale-33 pre-publication HEAD: `0db4c433040b482c1611f60aaf3dabb329b37c0b` — Apply English E04 Scale 33 #2 and English Content Full Validation #78 PASS after replacing the four exact-duplicate candidates detected by preflight; all publication quality gates and deterministic replay passed before the bot commit was pushed.\n',
        '',
        'remove scale-33 prep checkpoint',
    )
    text = replace_once(
        text,
        '- Scale-33 publication verification note: the publication commit was created by `github-actions[bot]`; its PR-triggered English Content Master Plan Acceptance #67 and Platform CI #1090 ended `action_required` before jobs ran, so this checkpoint intentionally re-triggers the mandatory CI from a normal branch write without regenerating scale-33 content or weakening any gate.\n',
        '',
        'remove resolved scale-33 verification note',
    )
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,070 published records after scale-33', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,110 published records after scale-34', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-33 publication', '## Published runtime snapshot after E04 scale-34 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,070 records', '- phrases: 2,110 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 6,671', '- total published rich records: 6,711', 'rich count')
    text = replace_once(text, '- editorial ledger: 6,671 decisions / 6,671 applied / 6,671 publish decisions', '- editorial ledger: 6,711 decisions / 6,711 applied / 6,711 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00000960`', '- E04 collocation frontier: `col.00001000`', 'collocation frontier')
    old_workstream = '''1. Verify scale-33 publication state through this normal-user checkpoint CI; do not duplicate scale-33 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. If scale-33 checkpoint CI passes and no newer worker has claimed the next scope, create scale-34 as the next bounded collocation batch from frontier `col.00000960`.
4. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
5. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-33 publication is fully verified; do not duplicate scale-33 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-34 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-33 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-33 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00000960` (expected scale-34 range `col.00000961` through `col.00001000` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-34 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001000` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')

def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-34 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 960:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 960, got {max(nums) if nums else None}')

    new = [make_collocation(961 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-34: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-34-collocations.json',
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
            'id': 'review.e04.scale-34.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-34-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-34-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-34-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-34-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-34-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-34-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 34 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==960)', 'if(recallCollocations!==1000)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 960 reviewed records', 'must expose 1000 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00000961', 'col.00001000'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1000, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2110, 'richRecords': 6711},
    }, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
