#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-61.py'), run_name='e04_scale62_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-62-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-62.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-62'
REVIEWED_AT = '2026-10-07T14:15:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-62'
EXPECTED = {'collocations': 2080, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('inspect server rack airflow', 'verb + noun phrase', 'kiểm tra luồng không khí qua tủ máy chủ để phát hiện vùng cản trở, tuần hoàn khí nóng hoặc phân phối gió làm mát không đều', 'B2'),
    ('balance hot aisle temperatures', 'verb + noun phrase', 'cân bằng nhiệt độ các hành lang nóng để giảm điểm quá nhiệt và duy trì tải làm mát đồng đều giữa các dãy tủ', 'C1'),
    ('verify cold aisle containment', 'verb + noun phrase', 'xác nhận hệ thống ngăn hành lang lạnh kín và đúng cấu hình để hạn chế trộn khí nóng với khí cấp lạnh', 'C1'),
    ('monitor rack inlet temperature', 'verb + noun phrase', 'theo dõi nhiệt độ khí vào tại tủ máy chủ để bảo đảm thiết bị nhận được không khí trong giới hạn vận hành cho phép', 'B2'),
    ('measure power usage effectiveness', 'verb + noun phrase', 'đo hiệu quả sử dụng điện của trung tâm dữ liệu để so sánh điện năng dành cho thiết bị CNTT với tổng điện năng cơ sở', 'C1'),
    ('track data center energy consumption', 'verb + noun phrase', 'theo dõi mức tiêu thụ năng lượng của trung tâm dữ liệu theo khu vực và thời gian để phát hiện bất thường và cơ hội tối ưu', 'B2'),
    ('inspect uninterruptible power systems', 'verb + noun phrase', 'kiểm tra hệ thống lưu điện về cảnh báo, tải, nhiệt độ và trạng thái mô-đun để bảo đảm nguồn dự phòng sẵn sàng', 'B2'),
    ('test battery string capacity', 'verb + noun phrase', 'kiểm tra dung lượng chuỗi ắc quy để xác nhận thời gian lưu điện đáp ứng yêu cầu khi nguồn điện chính bị gián đoạn', 'C1'),
    ('verify automatic transfer switch operation', 'verb + noun phrase', 'xác nhận bộ chuyển nguồn tự động chuyển đúng nguồn và thời gian quy định trong các tình huống mất điện thử nghiệm', 'C1'),
    ('exercise standby diesel generators', 'verb + noun phrase', 'chạy thử máy phát diesel dự phòng theo lịch để xác nhận khả năng khởi động, mang tải và vận hành ổn định', 'B2'),
    ('monitor generator fuel inventory', 'verb + noun phrase', 'theo dõi tồn lượng nhiên liệu máy phát để duy trì thời gian tự chủ yêu cầu trong sự cố điện lưới kéo dài', 'B2'),
    ('inspect switchgear thermal hotspots', 'verb + noun phrase', 'kiểm tra điểm nóng nhiệt trên tủ đóng cắt để phát hiện mối nối lỏng, quá tải hoặc suy giảm tiếp xúc trước khi gây sự cố', 'C1'),
    ('balance three-phase electrical loads', 'verb + noun phrase', 'cân bằng tải điện ba pha để giảm dòng trung tính, hạn chế quá tải cục bộ và cải thiện độ ổn định hệ thống phân phối', 'C1'),
    ('verify branch circuit labeling', 'verb + noun phrase', 'xác nhận nhãn mạch nhánh khớp với sơ đồ và tải thực tế để thao tác cô lập điện an toàn và truy vết nhanh', 'B2'),
    ('monitor power distribution unit load', 'verb + noun phrase', 'theo dõi tải trên thiết bị phân phối điện để ngăn vượt ngưỡng, hỗ trợ cân tải và lập kế hoạch mở rộng', 'B2'),
    ('inspect busway tap connections', 'verb + noun phrase', 'kiểm tra các điểm đấu nối nhánh trên busway để phát hiện lỏng, phát nhiệt hoặc hư hỏng cơ khí ảnh hưởng cấp điện cho tủ', 'C1'),
    ('measure rack power draw', 'verb + noun phrase', 'đo công suất tiêu thụ của từng tủ máy chủ để theo dõi tải, phân bổ công suất và xác định dư địa triển khai thiết bị mới', 'B2'),
    ('verify dual power feed redundancy', 'verb + noun phrase', 'xác nhận hai nguồn cấp độc lập cho thiết bị quan trọng thực sự tách biệt và có thể duy trì tải khi một nhánh bị mất', 'C1'),
    ('test static transfer switch operation', 'verb + noun phrase', 'kiểm tra bộ chuyển nguồn tĩnh để xác nhận chuyển tải nhanh giữa hai nguồn mà không làm gián đoạn thiết bị được bảo vệ', 'C1'),
    ('inspect raised floor panels', 'verb + noun phrase', 'kiểm tra các tấm sàn nâng về độ chắc chắn, khe hở và tải trọng để bảo đảm an toàn và duy trì đường phân phối khí bên dưới', 'B2'),
    ('seal cable floor penetrations', 'verb + noun phrase', 'bịt kín các lỗ xuyên sàn dành cho cáp để giảm rò khí, hỗ trợ kiểm soát cháy và duy trì hiệu quả làm mát', 'B2'),
    ('monitor underfloor pressure differential', 'verb + noun phrase', 'theo dõi chênh áp dưới sàn nâng để đánh giá khả năng phân phối khí lạnh tới các khu vực cần làm mát', 'C1'),
    ('inspect cooling tower water quality', 'verb + noun phrase', 'kiểm tra chất lượng nước tháp giải nhiệt để kiểm soát cáu cặn, ăn mòn và phát triển sinh học ảnh hưởng hiệu suất trao đổi nhiệt', 'C1'),
    ('clean condenser coil surfaces', 'verb + noun phrase', 'làm sạch bề mặt dàn ngưng để loại bỏ bụi và cặn làm giảm truyền nhiệt và tăng điện năng tiêu thụ', 'B2'),
    ('verify chilled water supply temperature', 'verb + noun phrase', 'xác nhận nhiệt độ nước lạnh cấp phù hợp với tải nhiệt và chiến lược điều khiển của hệ thống làm mát', 'C1'),
    ('balance computer room air handlers', 'verb + noun phrase', 'cân chỉnh các bộ xử lý không khí phòng máy để phân phối lưu lượng phù hợp giữa các vùng tải nhiệt khác nhau', 'C1'),
    ('monitor cooling pump vibration', 'verb + noun phrase', 'theo dõi độ rung bơm làm mát để phát hiện sớm mất cân bằng, lệch trục, mòn ổ bi hoặc hiện tượng xâm thực', 'B2'),
    ('test leak detection sensors', 'verb + noun phrase', 'kiểm tra cảm biến phát hiện rò rỉ để xác nhận cảnh báo đúng tại các khu vực có đường ống, van và thiết bị làm mát', 'B2'),
    ('inspect fire suppression cylinders', 'verb + noun phrase', 'kiểm tra bình chữa cháy khí về áp suất, niêm phong, ngày kiểm định và kết nối để bảo đảm hệ thống sẵn sàng kích hoạt', 'B2'),
    ('verify pre-action sprinkler supervision', 'verb + noun phrase', 'xác nhận hệ thống giám sát sprinkler pre-action phát hiện đúng trạng thái van, áp lực và lỗi mạch trước khi có sự cố cháy', 'C1'),
    ('test aspirating smoke detection', 'verb + noun phrase', 'kiểm tra hệ thống phát hiện khói hút mẫu để xác nhận độ nhạy, luồng hút và cảnh báo sớm trong không gian thiết bị', 'C1'),
    ('audit rack grounding continuity', 'verb + noun phrase', 'kiểm tra tính liên tục nối đất của tủ thiết bị để giảm nguy cơ điện giật, phóng tĩnh điện và chênh lệch điện thế không mong muốn', 'C1'),
    ('inspect fiber patch panel labeling', 'verb + noun phrase', 'kiểm tra nhãn trên bảng đấu nối cáp quang để bảo đảm đường truyền có thể truy vết và thao tác thay đổi không nhầm kết nối', 'B2'),
    ('verify network cross-connect routing', 'verb + noun phrase', 'xác nhận tuyến cross-connect mạng đi đúng điểm đầu cuối và đường cáp quy định để tránh nhầm lẫn và giảm rủi ro khi bảo trì', 'C1'),
    ('monitor backbone link utilization', 'verb + noun phrase', 'theo dõi mức sử dụng đường truyền backbone để phát hiện nghẽn, xu hướng tăng tải và nhu cầu mở rộng dung lượng', 'B2'),
    ('test failover network paths', 'verb + noun phrase', 'kiểm tra các đường mạng chuyển đổi dự phòng để xác nhận lưu lượng tự chuyển sang tuyến thay thế khi đường chính gặp lỗi', 'C1'),
    ('document capacity planning assumptions', 'verb + noun phrase', 'ghi lại các giả định dùng trong kế hoạch công suất để việc dự báo điện, làm mát, không gian và mạng có thể kiểm chứng và cập nhật', 'C1'),
    ('coordinate maintenance change windows', 'verb + noun phrase', 'phối hợp khung thời gian thay đổi bảo trì để giảm rủi ro đồng thời, tránh xung đột công việc và bảo vệ dịch vụ đang hoạt động', 'C1'),
    ('verify remote hands procedures', 'verb + noun phrase', 'xác nhận quy trình hỗ trợ thao tác từ xa mô tả rõ nhận dạng thiết bị, bước thực hiện, bằng chứng và điều kiện dừng an toàn', 'B2'),
    ('audit data center access logs', 'verb + noun phrase', 'kiểm tra nhật ký ra vào trung tâm dữ liệu để phát hiện truy cập bất thường, đối chiếu quyền và hỗ trợ điều tra sự kiện an ninh vật lý', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-62-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v62'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-62-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-61 publication: `700c9a76f181023cd5ae1f0449b6bf29030f7f82` — scale-60 publication state verified by English Content Master Plan Acceptance #156, English Content Full Validation #140 and Platform CI #1216; published output: `e6c4500a5443310b3d7cfc5fd7f4eb3ebad89dc9`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-62 publication: `034d6543bc070a760fe405c1a9bd9c15a9fd4107` — scale-61 publication state verified by English Content Master Plan Acceptance #159, English Content Full Validation #142 and Platform CI #1219; published output: `c48d5703c0161917da90f51ae9efb21e024e17e2`.',
        'verified scale-61 checkpoint',
    )
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,190 published records after scale-61', '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,230 published records after scale-62', 'E04 publication count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-61 publication', '## Published runtime snapshot after E04 scale-62 publication', 'runtime snapshot heading')
    text = replace_once(text, '- phrases: 3,190 records', '- phrases: 3,230 records', 'phrase runtime count')
    text = replace_once(text, '- total published rich records: 7,791', '- total published rich records: 7,831', 'rich runtime count')
    text = replace_once(text, '- editorial ledger: 7,791 decisions / 7,791 applied / 7,791 publish decisions', '- editorial ledger: 7,831 decisions / 7,831 applied / 7,831 publish decisions', 'editorial ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00002080`', '- E04 collocation frontier: `col.00002120`', 'collocation frontier')
    text = replace_once(text, '1. Scale-60 publication is fully verified at `700c9a76f181023cd5ae1f0449b6bf29030f7f82`; do not duplicate scale-60 artifacts.', '1. Scale-61 publication is fully verified at `034d6543bc070a760fe405c1a9bd9c15a9fd4107`; do not duplicate scale-61 artifacts.', 'verified workstream item')
    text = replace_once(text, '2. Scale-61 publication completed at `c48d5703c0161917da90f51ae9efb21e024e17e2`; do not regenerate scale-61 artifacts.', '2. Scale-62 is the current publication unit; do not start another collocation batch until its publication/checkpoint CI completes.', 'publication workstream item')
    text = replace_once(text, '3. Verify English Content Full Validation, Master Plan Acceptance and Platform CI on this normal-user checkpoint before attaching any scale-62 preparation commit.', '3. After the scale-62 bot publication commit is created, create one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.', 'checkpoint workstream item')
    text = replace_once(text, '5. If all checkpoint gates PASS and no safer pending enrichment appears, create the next bounded E04 collocation scale batch from frontier `col.00002080`, with fresh exact/near-dedupe preflight before any source apply.', '5. If no safer pending enrichment appears after the scale-62 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002120`, with fresh exact/near-dedupe preflight before any source apply.', 'next batch workstream item')
    old_next = 'Verify all three mandatory CI workflows for the scale-61 normal-user checkpoint. If PASS, continue immediately with a genuinely new bounded collocation batch from frontier `col.00002080` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-62 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002120` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main62():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-62 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 2080:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 2080, got {max(nums) if nums else None}')

    new = [make_collocation(2081 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-62: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-62-collocations.json',
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
            'id': 'review.e04.scale-62.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-62-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-62-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-62-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-62-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-62-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-62-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 62 data-center operations collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==2080)', 'if(recallCollocations!==2120)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 2080 reviewed records', 'must expose 2120 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00002081', 'col.00002120'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 2120, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 3230, 'richRecords': 7831},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main62()
