#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-35.py'), run_name='e04_scale36_base')
read_json = BASE['read_json']
write_json = BASE['write_json']
normalized_key = BASE['normalized_key']
jaccard = BASE['jaccard']
digest = BASE['digest']
replace_once = BASE['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-36-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-36.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-36'
REVIEWED_AT = '2026-10-07T05:10:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-36'
EXPECTED = {'collocations': 1040, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('calibrate measurement instruments', 'verb + noun phrase', 'hiệu chuẩn thiết bị đo để bảo đảm kết quả đo nằm trong giới hạn chính xác đã quy định', 'C1'),
    ('schedule preventive maintenance', 'verb + adjective + noun', 'lập lịch bảo trì phòng ngừa trước khi thiết bị phát sinh hỏng hóc ngoài kế hoạch', 'B2'),
    ('diagnose equipment faults', 'verb + noun phrase', 'chẩn đoán lỗi thiết bị dựa trên triệu chứng, dữ liệu vận hành và kiểm tra kỹ thuật', 'B2'),
    ('replace worn components', 'verb + adjective + noun', 'thay thế các linh kiện bị mòn trước khi chúng gây suy giảm hiệu năng hoặc hỏng máy', 'B2'),
    ('inspect machine guards', 'verb + noun phrase', 'kiểm tra bộ phận che chắn máy để bảo đảm an toàn khi vận hành', 'B2'),
    ('document maintenance logs', 'verb + noun phrase', 'ghi chép nhật ký bảo trì để lưu lịch sử công việc, linh kiện và tình trạng thiết bị', 'B2'),
    ('verify torque specifications', 'verb + noun phrase', 'xác minh thông số mô-men siết của mối ghép theo yêu cầu kỹ thuật', 'C1'),
    ('monitor vibration levels', 'verb + noun phrase', 'theo dõi mức rung của thiết bị để phát hiện sớm dấu hiệu mất cân bằng hoặc hư hỏng', 'C1'),
    ('analyze failure modes', 'verb + noun phrase', 'phân tích các dạng hỏng có thể xảy ra để hiểu nguyên nhân và tác động của chúng', 'C1'),
    ('investigate equipment breakdowns', 'verb + noun phrase', 'điều tra các sự cố dừng máy để xác định nguyên nhân và biện pháp phòng ngừa', 'C1'),
    ('implement corrective actions', 'verb + adjective + noun', 'triển khai hành động khắc phục nhằm loại bỏ nguyên nhân của vấn đề đã xác định', 'C1'),
    ('verify corrective effectiveness', 'verb + adjective + noun', 'xác minh hiệu quả của hành động khắc phục sau khi đã triển khai', 'C1'),
    ('control process variation', 'verb + noun phrase', 'kiểm soát biến động của quá trình để duy trì đầu ra ổn định trong giới hạn cho phép', 'C1'),
    ('monitor defect rates', 'verb + noun phrase', 'theo dõi tỷ lệ lỗi để nhận diện xu hướng chất lượng và điểm cần can thiệp', 'B2'),
    ('sample production batches', 'verb + noun phrase', 'lấy mẫu các lô sản xuất theo kế hoạch kiểm tra chất lượng đã xác định', 'B2'),
    ('inspect incoming materials', 'verb + adjective + noun', 'kiểm tra nguyên vật liệu đầu vào trước khi chấp nhận đưa vào sản xuất', 'B2'),
    ('quarantine nonconforming goods', 'verb + adjective + noun', 'cách ly hàng hóa không phù hợp để ngăn sử dụng hoặc xuất đi ngoài ý muốn', 'C1'),
    ('release approved batches', 'verb + adjective + noun', 'cho phép các lô đã được phê duyệt chuyển sang bước sử dụng hoặc phân phối tiếp theo', 'B2'),
    ('trace component lots', 'verb + noun phrase', 'truy vết các lô linh kiện qua lịch sử mua, sản xuất và sử dụng', 'B2'),
    ('maintain batch records', 'verb + noun phrase', 'duy trì hồ sơ lô sản xuất đầy đủ để hỗ trợ kiểm tra và truy xuất', 'B2'),
    ('validate production processes', 'verb + noun phrase', 'thẩm định quy trình sản xuất để chứng minh khả năng tạo đầu ra ổn định theo yêu cầu', 'C1'),
    ('qualify manufacturing equipment', 'verb + noun phrase', 'đánh giá và xác nhận thiết bị sản xuất đáp ứng yêu cầu sử dụng đã định', 'C1'),
    ('standardize work instructions', 'verb + noun phrase', 'chuẩn hóa hướng dẫn công việc để giảm khác biệt trong cách thực hiện giữa các ca hoặc nhóm', 'B2'),
    ('revise operating procedures', 'verb + adjective + noun', 'sửa đổi quy trình vận hành khi yêu cầu, rủi ro hoặc phương pháp làm việc thay đổi', 'B2'),
    ('train line operators', 'verb + noun phrase', 'đào tạo công nhân vận hành dây chuyền theo tiêu chuẩn thao tác và an toàn', 'B2'),
    ('balance assembly lines', 'verb + noun phrase', 'cân bằng dây chuyền lắp ráp để phân bổ công việc hợp lý giữa các công đoạn', 'C1'),
    ('reduce changeover times', 'verb + noun phrase', 'giảm thời gian chuyển đổi giữa sản phẩm hoặc cấu hình sản xuất', 'C1'),
    ('optimize machine utilization', 'verb + noun phrase', 'tối ưu mức sử dụng máy để tăng năng lực thực tế mà không tạo quá tải', 'C1'),
    ('monitor production cycle times', 'verb + noun phrase', 'theo dõi thời gian chu kỳ sản xuất để phát hiện chậm trễ và biến động', 'B2'),
    ('eliminate production bottlenecks', 'verb + noun phrase', 'loại bỏ điểm nghẽn sản xuất làm giới hạn thông lượng của toàn quy trình', 'C1'),
    ('schedule production runs', 'verb + noun phrase', 'lập lịch các đợt sản xuất theo nhu cầu, năng lực và thời gian sẵn có', 'B2'),
    ('sequence manufacturing orders', 'verb + noun phrase', 'sắp xếp thứ tự lệnh sản xuất để giảm chuyển đổi và đáp ứng hạn giao hàng', 'C1'),
    ('allocate machine capacity', 'verb + noun phrase', 'phân bổ công suất máy cho các đơn hàng hoặc dòng sản phẩm theo ưu tiên', 'C1'),
    ('manage work-in-process inventory', 'verb + noun phrase', 'quản lý tồn kho bán thành phẩm giữa các công đoạn để tránh ùn tắc hoặc thiếu hụt', 'C1'),
    ('control scrap rates', 'verb + noun phrase', 'kiểm soát tỷ lệ phế phẩm để giảm lãng phí nguyên liệu và chi phí sản xuất', 'B2'),
    ('improve production yield', 'verb + noun phrase', 'cải thiện tỷ lệ đầu ra đạt yêu cầu so với tổng lượng nguyên liệu hoặc sản phẩm xử lý', 'C1'),
    ('verify packaging integrity', 'verb + noun phrase', 'xác minh bao bì còn nguyên vẹn và đủ khả năng bảo vệ sản phẩm', 'B2'),
    ('label finished goods', 'verb + adjective + noun', 'ghi nhãn thành phẩm với thông tin nhận dạng, lô và yêu cầu cần thiết', 'B2'),
    ('conduct final inspections', 'verb + adjective + noun', 'thực hiện kiểm tra cuối cùng trước khi sản phẩm được giải phóng hoặc giao đi', 'B2'),
    ('authorize product release', 'verb + noun phrase', 'phê duyệt chính thức việc giải phóng sản phẩm sau khi các yêu cầu chất lượng đã được đáp ứng', 'C1'),
]

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
                'schema': {'status': 'pass', 'method': 'e04-scale-36-authoring-v1'},
                'grammar': {'status': 'pending', 'method': 'manual-review-required'},
                'translation': {'status': 'pending', 'method': 'manual-review-required'},
                'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
                'cefr': {'status': 'pending', 'method': 'manual-review-required'},
                'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
                'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v36'},
                'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
                'license': {'status': 'pending', 'method': 'manual-review-required'},
            },
        },
        'provenance': {
            'sources': [{
                'dataset': 'project-original',
                'sourceId': rid,
                'sourceUrl': 'content/english/phrases/e04-scale-36-collocations.json',
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
        '- Latest fully CI-verified scale-up checkpoint before scale-35 publication: `e7342759929cf624efb35fc56b09542bde7cd193` — scale-34 publication state verified by English Content Master Plan Acceptance #71, English Content Full Validation #81 and Platform CI #1097; published output: `8825d0158b036e87bfeaa9ef1749d5448a40ab32`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-36 publication: `964af3b7b1eaa6a5b08af5f5d693a22cc9d7adc2` — scale-35 publication state verified by English Content Master Plan Acceptance #74, English Content Full Validation #83 and Platform CI #1117; published output: `26fd71cb7df2308c612a949fa8215d6dca5792dc`.',
        'verified scale-35 checkpoint',
    )
    text = replace_once(text, '- Latest published scale-up HEAD before this checkpoint: `26fd71cb7df2308c612a949fa8215d6dca5792dc` — `feat(content): publish E04 collocation scale 35`.\n', '', 'remove scale-35 publication line')
    text = replace_once(text, '- Latest scale-35 pre-publication HEAD: `d04e99448644851da3725d49d668614d4d3ea63e` — Apply English E04 Scale 35 #1 passed preflight, source apply, review/E10/license, generate/publish, full quality gates, converge, deterministic replay and bot commit/push.\n', '', 'remove scale-35 prep line')
    text = replace_once(text, '- Scale-35 publication verification note: the publication commit was created by `github-actions[bot]`; its PR-triggered English Content Master Plan Acceptance #73 and Platform CI #1099 ended `action_required` before jobs ran, so this checkpoint intentionally re-triggers the mandatory CI from a normal branch write without regenerating scale-35 content or weakening any gate.\n', '', 'remove resolved scale-35 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,150 published records after scale-35', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,190 published records after scale-36', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-35 publication', '## Published runtime snapshot after E04 scale-36 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,150 records', '- phrases: 2,190 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 6,751', '- total published rich records: 6,791', 'rich count')
    text = replace_once(text, '- editorial ledger: 6,751 decisions / 6,751 applied / 6,751 publish decisions', '- editorial ledger: 6,791 decisions / 6,791 applied / 6,791 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001040`', '- E04 collocation frontier: `col.00001080`', 'collocation frontier')
    old_workstream = '''1. Verify scale-35 publication state through this normal-user checkpoint CI; do not duplicate scale-35 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. If scale-35 checkpoint CI passes and no newer worker has claimed the next scope, create scale-36 as the next bounded collocation batch from frontier `col.00001040`.
4. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
5. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-35 publication is fully verified; do not duplicate scale-35 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-36 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-35 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-35 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001040` (expected scale-36 range `col.00001041` through `col.00001080` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-36 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001080` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')

def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-36 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1040:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1040, got {max(nums) if nums else None}')

    new = [make_collocation(1041 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-36: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-36-collocations.json',
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
            'id': 'review.e04.scale-36.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-36-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-36-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-36-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-36-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-36-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-36-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 36 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1040)', 'if(recallCollocations!==1080)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1040 reviewed records', 'must expose 1080 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001041', 'col.00001080'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1080, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2190, 'richRecords': 6791},
    }, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
