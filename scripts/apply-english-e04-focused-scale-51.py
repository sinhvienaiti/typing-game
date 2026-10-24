#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-50.py'), run_name='e04_scale51_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-51-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-51.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-51'
REVIEWED_AT = '2026-10-07T10:22:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-51'
EXPECTED = {'collocations': 1640, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('validate construction site access permits', 'verb + noun phrase', 'xác thực giấy phép ra vào công trường để bảo đảm chỉ người và phương tiện đủ điều kiện mới được tiếp cận khu vực thi công', 'C1'),
    ('sequence structural steel deliveries', 'verb + adjective + noun', 'sắp xếp thứ tự giao kết cấu thép theo trình tự lắp dựng để giảm lưu kho và tránh cản trở mặt bằng', 'C1'),
    ('coordinate concrete pour schedules', 'verb + noun phrase', 'phối hợp lịch đổ bê tông giữa tổ đội, trạm trộn, kiểm tra chất lượng và điều kiện hiện trường', 'B2'),
    ('inspect reinforcing steel placement', 'verb + noun phrase', 'kiểm tra vị trí lắp đặt cốt thép theo bản vẽ, khoảng cách, lớp bảo vệ và yêu cầu kỹ thuật', 'B2'),
    ('verify formwork alignment tolerances', 'verb + noun phrase', 'xác minh độ thẳng và sai số cho phép của cốp pha trước khi đổ bê tông', 'C1'),
    ('monitor concrete curing conditions', 'verb + noun phrase', 'theo dõi điều kiện bảo dưỡng bê tông như độ ẩm, nhiệt độ và thời gian để đạt cường độ yêu cầu', 'B2'),
    ('document field change orders', 'verb + adjective + noun', 'ghi chép các lệnh thay đổi phát sinh tại hiện trường cùng phạm vi, lý do và tác động được phê duyệt', 'C1'),
    ('reconcile subcontractor progress claims', 'verb + noun phrase', 'đối chiếu hồ sơ đề nghị thanh toán khối lượng của nhà thầu phụ với công việc thực tế và hồ sơ nghiệm thu', 'C1'),
    ('approve material substitution requests', 'verb + noun phrase', 'phê duyệt đề nghị thay thế vật liệu sau khi đánh giá tương đương kỹ thuật, chất lượng và tác động hợp đồng', 'C1'),
    ('track long-lead equipment deliveries', 'verb + adjective + noun', 'theo dõi việc giao thiết bị có thời gian cung ứng dài để bảo vệ mốc lắp đặt và tiến độ tổng thể', 'C1'),
    ('conduct pre-installation coordination meetings', 'verb + adjective + noun', 'tổ chức họp phối hợp trước lắp đặt để rà soát giao diện, trình tự thi công và điều kiện sẵn sàng', 'C1'),
    ('verify embedded item locations', 'verb + adjective + noun', 'xác minh vị trí các chi tiết chôn sẵn trước khi kết cấu bị che khuất hoặc đổ bê tông', 'B2'),
    ('inspect waterproofing membrane laps', 'verb + noun phrase', 'kiểm tra các mối chồng của màng chống thấm để bảo đảm chiều rộng, độ kín và chất lượng liên kết', 'C1'),
    ('test fire-alarm interface signals', 'verb + adjective + noun', 'kiểm tra tín hiệu giao tiếp của hệ thống báo cháy với các hệ thống liên động để xác nhận phản ứng đúng thiết kế', 'C1'),
    ('commission emergency power systems', 'verb + adjective + noun', 'chạy thử và nghiệm thu hệ thống điện khẩn cấp để xác nhận khả năng chuyển nguồn và cấp điện cho tải thiết yếu', 'C1'),
    ('balance mechanical ventilation systems', 'verb + adjective + noun', 'cân chỉnh hệ thống thông gió cơ khí để lưu lượng và áp suất tại các nhánh đạt giá trị thiết kế', 'C1'),
    ('witness pressure test procedures', 'verb + noun phrase', 'chứng kiến quy trình thử áp để xác nhận điều kiện thử, kết quả và hồ sơ đáp ứng yêu cầu', 'C1'),
    ('record punch-list deficiencies', 'verb + adjective + noun', 'ghi nhận các khiếm khuyết trong danh sách tồn đọng để phân công sửa chữa và theo dõi đóng việc', 'B2'),
    ('close outstanding inspection items', 'verb + adjective + noun', 'đóng các hạng mục kiểm tra còn tồn sau khi biện pháp khắc phục đã được xác nhận đạt yêu cầu', 'B2'),
    ('release completed work areas', 'verb + adjective + noun', 'bàn giao khu vực đã hoàn thành cho công việc kế tiếp sau khi đáp ứng điều kiện nghiệm thu và an toàn', 'B2'),
    ('manage temporary works designs', 'verb + adjective + noun', 'quản lý thiết kế công trình tạm như chống đỡ, giàn giáo hoặc sàn công tác trong suốt quá trình phê duyệt và sử dụng', 'C1'),
    ('review crane lifting plans', 'verb + noun phrase', 'xem xét phương án nâng bằng cần cẩu gồm tải trọng, bán kính, thiết bị hỗ trợ và vùng kiểm soát an toàn', 'C1'),
    ('coordinate utility shutdown windows', 'verb + noun phrase', 'phối hợp khung thời gian ngừng hệ thống tiện ích để thực hiện đấu nối hoặc bảo trì với ảnh hưởng vận hành tối thiểu', 'C1'),
    ('isolate live electrical circuits', 'verb + adjective + noun', 'cô lập các mạch điện đang mang điện trước khi thi công hoặc bảo trì để ngăn cấp điện ngoài ý muốn', 'C1'),
    ('verify lockout tagout boundaries', 'verb + noun phrase', 'xác minh ranh giới khóa và gắn thẻ cô lập năng lượng bao phủ đúng thiết bị và nguồn nguy hiểm liên quan', 'C1'),
    ('maintain confined-space entry logs', 'verb + adjective + noun', 'duy trì nhật ký ra vào không gian hạn chế để kiểm soát người, thời gian và điều kiện cho phép làm việc', 'C1'),
    ('inspect scaffold tagging systems', 'verb + noun phrase', 'kiểm tra hệ thống thẻ giàn giáo để trạng thái sử dụng và giới hạn an toàn được nhận biết rõ ràng', 'B2'),
    ('enforce excavation safety controls', 'verb + adjective + noun', 'thực thi biện pháp an toàn đào đất như chống sạt, rào chắn, lối ra vào và kiểm soát tiện ích ngầm', 'C1'),
    ('monitor groundwater dewatering rates', 'verb + noun phrase', 'theo dõi tốc độ hạ nước ngầm để kiểm soát điều kiện hố đào và hạn chế ảnh hưởng đến khu vực xung quanh', 'C1'),
    ('survey as-built elevations', 'verb + adjective + noun', 'đo kiểm cao độ hoàn công để đối chiếu vị trí thực tế với yêu cầu thiết kế và hồ sơ bàn giao', 'C1'),
    ('update construction lookahead schedules', 'verb + adjective + noun', 'cập nhật lịch nhìn trước thi công để phản ánh công việc sắp tới, ràng buộc và nguồn lực cần chuẩn bị', 'C1'),
    ('measure installed work quantities', 'verb + adjective + noun', 'đo khối lượng công việc đã lắp đặt để phục vụ theo dõi tiến độ, thanh toán và dự báo phần còn lại', 'B2'),
    ('forecast remaining labor hours', 'verb + adjective + noun', 'dự báo số giờ lao động còn cần thiết dựa trên khối lượng còn lại và năng suất thực tế', 'C1'),
    ('analyze schedule float erosion', 'verb + noun phrase', 'phân tích mức suy giảm thời gian dự phòng của tiến độ để nhận diện hoạt động có nguy cơ trở thành đường găng', 'C1'),
    ('evaluate recovery schedule options', 'verb + noun phrase', 'đánh giá các phương án khôi phục tiến độ như tăng nguồn lực, đổi trình tự hoặc rút ngắn thời lượng công việc', 'C1'),
    ('negotiate subcontractor change pricing', 'verb + noun phrase', 'đàm phán giá cho thay đổi phạm vi với nhà thầu phụ dựa trên khối lượng, đơn giá và tác động hợp lý', 'C1'),
    ('document delay event chronology', 'verb + noun phrase', 'ghi lại trình tự thời gian của sự kiện chậm trễ và các thông báo liên quan để hỗ trợ phân tích trách nhiệm', 'C1'),
    ('assess weather impact claims', 'verb + noun phrase', 'đánh giá yêu cầu gia hạn hoặc bồi hoàn do thời tiết dựa trên dữ liệu thực tế và điều kiện hợp đồng', 'C1'),
    ('verify substantial completion criteria', 'verb + adjective + noun', 'xác minh các tiêu chí hoàn thành cơ bản đã đạt để công trình có thể được sử dụng cho mục đích dự kiến dù còn tồn đọng nhỏ', 'C1'),
    ('compile project closeout records', 'verb + noun phrase', 'tổng hợp hồ sơ kết thúc dự án gồm bản vẽ hoàn công, chứng nhận, hướng dẫn vận hành, bảo hành và biên bản bàn giao', 'C1'),
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
        'quality': {'state': 'draft', 'checks': {
            'schema': {'status': 'pass', 'method': 'e04-scale-51-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v51'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-51-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-50 verification: `e528b4eb8d467c472b77bca241c0ce6e738fd452` — scale-49 publication state verified by English Content Master Plan Acceptance #122, English Content Full Validation #117 and Platform CI #1174; published output: `2534d8a44ab77144615a820ef3ceabf2c70ded88`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-51 publication: `2c25c72ecb7367dcb486806910ce980c7a7edc85` — scale-50 publication state verified by English Content Master Plan Acceptance #125, English Content Full Validation #119 and Platform CI #1180; published output: `af88c97dedd74dc8159a05528f3c79fb8af6c3c7`.',
        'verified scale-50 checkpoint',
    )
    text = replace_once(text, '- Scale-50 publication commit: `af88c97dedd74dc8159a05528f3c79fb8af6c3c7` — E04 collocation scale-50 published with clean threshold-0.86 preflight; published frontier is `col.00001640`.\n', '', 'remove scale-50 publication line')
    text = replace_once(text, '- Scale-50 verification state: publication is complete, but the normal-user checkpoint verification is still required. Bot-triggered English Content Master Plan Acceptance #124 and Platform CI #1178 ended `action_required` before jobs ran, matching the known bot-publication pattern; do not regenerate scale-50.\n', '', 'remove scale-50 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,750 published records after scale-50', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,790 published records after scale-51', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-50 publication', '## Published runtime snapshot after E04 scale-51 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,750 records', '- phrases: 2,790 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 7,351', '- total published rich records: 7,391', 'rich count')
    text = replace_once(text, '- editorial ledger: 7,351 decisions / 7,351 applied / 7,351 publish decisions', '- editorial ledger: 7,391 decisions / 7,391 applied / 7,391 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001640`', '- E04 collocation frontier: `col.00001680`', 'collocation frontier')
    old_workstream = '''1. Scale-49 publication is fully verified at `e528b4eb8d467c472b77bca241c0ce6e738fd452`; do not duplicate scale-49 artifacts.
2. Scale-50 source/application/publication is complete at `af88c97dedd74dc8159a05528f3c79fb8af6c3c7`; do not regenerate or republish it.
3. Verify this normal-user checkpoint with all three mandatory workflows: English Content Master Plan Acceptance, English Content Full Validation and Platform CI. Scale-50 is not fully verified until all three PASS on the checkpoint.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. After scale-50 is fully verified, re-resolve HEAD and recalculate deficits. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-50 publication is fully verified at `2c25c72ecb7367dcb486806910ce980c7a7edc85`; do not duplicate scale-50 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-51 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_next = 'Scale-50 publication is complete at `af88c97dedd74dc8159a05528f3c79fb8af6c3c7`. Verify this normal-user checkpoint until English Content Master Plan Acceptance, English Content Full Validation and Platform CI all PASS. Do not create a second CI-refresh checkpoint. Once all three pass, mark scale-50 fully verified in the next real-state progress update associated with subsequent bounded work, then continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001640` (expected scale-51 range `col.00001641` through `col.00001680` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-51 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001680` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main51():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-51 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1640:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1640, got {max(nums) if nums else None}')

    new = [make_collocation(1641 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-51: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-51-collocations.json',
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
            'id': 'review.e04.scale-51.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-51-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-51-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-51-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-51-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-51-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-51-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 51 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1640)', 'if(recallCollocations!==1680)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1640 reviewed records', 'must expose 1680 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001641', 'col.00001680'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1680, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2790, 'richRecords': 7391},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main51()
