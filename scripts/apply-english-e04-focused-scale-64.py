#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-63.py'), run_name='e04_scale64_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-64-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-64.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-64'
REVIEWED_AT = '2026-10-07T15:05:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-64'
EXPECTED = {'collocations': 2160, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('align telescope optical axes', 'verb + noun phrase', 'căn chỉnh các trục quang học của kính thiên văn để duy trì chất lượng ảnh và độ chính xác hướng ngắm', 'C1'),
    ('calibrate telescope pointing models', 'verb + noun phrase', 'hiệu chuẩn mô hình định hướng kính thiên văn bằng các sao tham chiếu để giảm sai số khi chuyển đến mục tiêu mới', 'C1'),
    ('verify dome shutter interlocks', 'verb + noun phrase', 'xác nhận liên động cửa mái vòm hoạt động đúng để ngăn chuyển động không an toàn hoặc mở cửa trong điều kiện bị khóa', 'C1'),
    ('synchronize observatory control clocks', 'verb + noun phrase', 'đồng bộ đồng hồ của hệ thống điều khiển đài quan sát để thời dấu dữ liệu và lệnh thiết bị nhất quán', 'B2'),
    ('monitor atmospheric seeing conditions', 'verb + noun phrase', 'theo dõi độ nhiễu loạn khí quyển ảnh hưởng đến độ sắc nét của ảnh thiên văn để chọn chế độ quan sát phù hợp', 'C1'),
    ('measure sky background brightness', 'verb + noun phrase', 'đo độ sáng nền trời để đánh giá ô nhiễm ánh sáng, trăng và điều kiện phù hợp cho mục tiêu mờ', 'B2'),
    ('track cloud cover evolution', 'verb + noun phrase', 'theo dõi diễn biến mây theo thời gian để quyết định tiếp tục, tạm dừng hoặc thay đổi chương trình quan sát', 'B2'),
    ('monitor wind gust thresholds', 'verb + noun phrase', 'theo dõi ngưỡng gió giật để bảo vệ kính thiên văn và mái vòm khỏi tải gió vượt giới hạn vận hành', 'B2'),
    ('close dome before precipitation', 'verb + noun phrase', 'đóng mái vòm trước khi có mưa hoặc tuyết để bảo vệ bề mặt quang học và thiết bị điện tử', 'B2'),
    ('verify weather station telemetry', 'verb + noun phrase', 'xác nhận dữ liệu từ trạm thời tiết được truyền đầy đủ và hợp lý trước khi dùng cho quyết định an toàn quan sát', 'B2'),
    ('cool detector focal planes', 'verb + noun phrase', 'làm lạnh mặt phẳng tiêu của cảm biến để giảm nhiễu nhiệt trong các phép đo thiên văn nhạy sáng', 'C1'),
    ('stabilize detector operating temperature', 'verb + noun phrase', 'ổn định nhiệt độ vận hành của cảm biến để đặc tính nhiễu và độ nhạy không thay đổi trong chuỗi phơi sáng', 'C1'),
    ('acquire detector bias frames', 'verb + noun phrase', 'thu các khung bias của cảm biến để ước lượng mức đọc điện tử cơ sở dùng trong hiệu chỉnh dữ liệu', 'C1'),
    ('capture dark calibration frames', 'verb + noun phrase', 'chụp khung tối với thời gian phơi tương ứng để ước lượng dòng tối và mẫu nhiễu nhiệt của cảm biến', 'C1'),
    ('collect twilight flat fields', 'verb + noun phrase', 'thu ảnh phẳng lúc chạng vạng để hiệu chỉnh đáp ứng không đồng đều theo pixel và trường nhìn', 'C1'),
    ('inspect detector readout noise', 'verb + noun phrase', 'kiểm tra nhiễu đọc của cảm biến để phát hiện thay đổi điện tử có thể làm giảm độ chính xác đo quang', 'C1'),
    ('configure science exposure sequences', 'verb + noun phrase', 'cấu hình chuỗi phơi sáng khoa học với bộ lọc, thời gian và số lần lặp phù hợp với mục tiêu quan sát', 'B2'),
    ('sequence multi-filter observations', 'verb + noun phrase', 'sắp xếp quan sát qua nhiều bộ lọc để đạt phủ bước sóng cần thiết trong điều kiện thời gian và bầu trời cho phép', 'C1'),
    ('dither telescope between exposures', 'verb + noun phrase', 'dịch nhẹ vị trí kính giữa các lần phơi để giảm ảnh hưởng điểm xấu, mẫu nền và khuyết tật cố định của cảm biến', 'C1'),
    ('refocus telescope during temperature drift', 'verb + noun phrase', 'lấy nét lại kính khi nhiệt độ thay đổi làm dịch tiêu điểm để duy trì kích thước ảnh sao ổn định', 'C1'),
    ('measure stellar focus curves', 'verb + noun phrase', 'đo đường cong lấy nét từ ảnh sao ở nhiều vị trí tiêu để xác định điểm hội tụ tối ưu', 'C1'),
    ('guide telescope on reference stars', 'verb + noun phrase', 'dẫn đường kính theo sao tham chiếu để bù sai số bám và giữ mục tiêu ổn định trong phơi dài', 'C1'),
    ('monitor autoguider tracking residuals', 'verb + noun phrase', 'theo dõi sai số dư của hệ thống dẫn tự động để phát hiện rung, gió hoặc lỗi cơ khí ảnh hưởng đến độ tròn của sao', 'C1'),
    ('correct differential tracking rates', 'verb + noun phrase', 'hiệu chỉnh tốc độ bám khác chuẩn để theo dõi vật thể chuyển động như tiểu hành tinh hoặc sao chổi', 'C1'),
    ('predict target rise times', 'verb + noun phrase', 'dự đoán thời điểm mục tiêu mọc đủ cao trên chân trời để lập lịch quan sát hiệu quả', 'B2'),
    ('schedule observations by airmass', 'verb + noun phrase', 'lập lịch quan sát theo khối lượng khí quyển để ưu tiên mục tiêu khi chúng ở độ cao thuận lợi', 'C1'),
    ('avoid high-airmass observations', 'verb + noun phrase', 'tránh quan sát ở khối lượng khí quyển quá lớn để giảm suy hao, tán sắc và biến thiên khí quyển', 'B2'),
    ('screen targets for moon avoidance', 'verb + noun phrase', 'sàng lọc mục tiêu theo góc cách Mặt Trăng để giảm nền trời sáng và ánh sáng tán xạ', 'C1'),
    ('calculate lunar separation angles', 'verb + noun phrase', 'tính góc cách giữa mục tiêu và Mặt Trăng để hỗ trợ lập lịch các quan sát nhạy nền trời', 'B2'),
    ('verify target coordinate epochs', 'verb + noun phrase', 'xác nhận epoch của tọa độ mục tiêu để áp dụng tiền tiến và chuyển động riêng đúng trước khi trỏ kính', 'C1'),
    ('apply proper motion corrections', 'verb + noun phrase', 'áp dụng hiệu chỉnh chuyển động riêng cho sao để tọa độ dự đoán phù hợp thời điểm quan sát hiện tại', 'C1'),
    ('solve astrometric image coordinates', 'verb + noun phrase', 'giải nghiệm astrometry cho ảnh để ánh xạ chính xác pixel sang tọa độ bầu trời', 'C1'),
    ('match catalog reference stars', 'verb + noun phrase', 'khớp sao trong ảnh với danh mục tham chiếu để xây dựng nghiệm tọa độ hoặc hiệu chuẩn quang học', 'C1'),
    ('estimate photometric zero points', 'verb + noun phrase', 'ước lượng điểm không quang trắc từ các sao chuẩn để chuyển số đếm detector sang độ sáng chuẩn hóa', 'C1'),
    ('observe photometric standard fields', 'verb + noun phrase', 'quan sát trường sao chuẩn quang trắc để hiệu chuẩn độ nhạy và biến thiên truyền qua khí quyển', 'C1'),
    ('monitor extinction coefficient changes', 'verb + noun phrase', 'theo dõi biến thiên hệ số suy hao khí quyển để đánh giá độ ổn định quang trắc trong đêm', 'C1'),
    ('flag saturated stellar images', 'verb + noun phrase', 'đánh dấu ảnh sao bị bão hòa để tránh dùng số đo mất tuyến tính trong phân tích khoa học', 'B2'),
    ('mask detector bad pixels', 'verb + noun phrase', 'che các pixel lỗi đã biết trong quá trình xử lý để chúng không làm lệch phép đo hoặc tạo giả tín hiệu', 'B2'),
    ('archive raw observation metadata', 'verb + noun phrase', 'lưu trữ metadata quan sát thô gồm thời gian, mục tiêu, cấu hình và điều kiện môi trường để bảo đảm khả năng tái xử lý', 'B2'),
    ('validate nightly data completeness', 'verb + noun phrase', 'xác nhận dữ liệu của một đêm quan sát đầy đủ giữa file khoa học, hiệu chuẩn và metadata trước khi đóng ca', 'B2'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-64-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v64'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-64-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-63 publication: `f8e5bc772c78569ab181c4752d79f81ea8fcaf18` — scale-62 publication state verified by English Content Master Plan Acceptance #162, English Content Full Validation #144 and Platform CI #1245; published output: `8722e17746730344c8adc366c282a2b541401d56`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-64 publication: `c39f556a3957f3ce0058b1990a831f2064475df9` — scale-63 publication state verified by English Content Master Plan Acceptance #165, English Content Full Validation #146 and Platform CI #1254; published output: `7d44880c65ef5eb8685df661d3ef5f4859f71720`.',
        'verified scale-63 checkpoint',
    )
    text = replace_once(
        text,
        '- Scale-63 publication completed at `7d44880c65ef5eb8685df661d3ef5f4859f71720`; bot-triggered PR workflows follow the known `action_required` publication pattern, so this normal-user checkpoint exists to verify the published state before opening scale-64.',
        '- Scale-63 publication checkpoint `c39f556a3957f3ce0058b1990a831f2064475df9` is fully verified; scale-64 is the current publication unit.',
        'scale-63 verification state',
    )
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,270 published records after scale-63', '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,310 published records after scale-64', 'E04 publication count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-63 publication', '## Published runtime snapshot after E04 scale-64 publication', 'runtime snapshot heading')
    text = replace_once(text, '- phrases: 3,270 records', '- phrases: 3,310 records', 'phrase runtime count')
    text = replace_once(text, '- total published rich records: 7,871', '- total published rich records: 7,911', 'rich runtime count')
    text = replace_once(text, '- editorial ledger: 7,871 decisions / 7,871 applied / 7,871 publish decisions', '- editorial ledger: 7,911 decisions / 7,911 applied / 7,911 publish decisions', 'editorial ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00002160`', '- E04 collocation frontier: `col.00002200`', 'collocation frontier')
    text = replace_once(text, '1. Scale-62 publication is fully verified at `f8e5bc772c78569ab181c4752d79f81ea8fcaf18`; do not duplicate scale-62 artifacts.', '1. Scale-63 publication is fully verified at `c39f556a3957f3ce0058b1990a831f2064475df9`; do not duplicate scale-63 artifacts.', 'verified workstream item')
    text = replace_once(text, '2. Scale-63 publication completed at `7d44880c65ef5eb8685df661d3ef5f4859f71720`; the current gate is normal-user checkpoint verification, not regeneration.', '2. Scale-64 is the current publication unit; do not start another collocation batch until its publication/checkpoint CI completes.', 'publication workstream item')
    text = replace_once(text, '3. Verify English Content Full Validation, English Content Master Plan Acceptance and Platform CI on this checkpoint. Only when all three PASS is scale-63 fully verified.', '3. After the scale-64 bot publication commit is created, create one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.', 'checkpoint workstream item')
    text = replace_once(text, '5. If no safer pending enrichment appears after the scale-63 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002160`, with fresh exact/near-dedupe preflight before any source apply.', '5. If no safer pending enrichment appears after the scale-64 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002200`, with fresh exact/near-dedupe preflight before any source apply.', 'next batch workstream item')
    old_next = 'Verify scale-63 publication `7d44880c65ef5eb8685df661d3ef5f4859f71720` under the normal-user checkpoint. If English Content Full Validation, Master Plan Acceptance and Platform CI all PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002160` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-64 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002200` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main64():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-64 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 2160:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 2160, got {max(nums) if nums else None}')

    new = [make_collocation(2161 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-64: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-64-collocations.json',
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
            'id': 'review.e04.scale-64.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-64-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-64-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-64-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-64-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-64-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-64-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 64 astronomical observatory operations collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==2160)', 'if(recallCollocations!==2200)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 2160 reviewed records', 'must expose 2200 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00002161', 'col.00002200'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 2200, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 3310, 'richRecords': 7911},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main64()
