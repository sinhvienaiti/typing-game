#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-68.py'), run_name='e04_scale69_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-69-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-69.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-69'
REVIEWED_AT = '2026-10-07T16:30:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-69'
EXPECTED = {'collocations': 2360, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('align telescope mount axes', 'verb + noun phrase', 'căn chỉnh các trục của giá đỡ kính thiên văn để chuyển động theo hệ tọa độ quan sát chính xác và giảm sai số bám mục tiêu', 'C1'),
    ('collimate telescope optics precisely', 'verb + noun phrase', 'chuẩn trực hệ quang kính thiên văn chính xác để các phần tử quang học cùng trục và duy trì chất lượng ảnh trên toàn trường', 'C1'),
    ('calibrate guiding camera response', 'verb + noun phrase', 'hiệu chuẩn đáp ứng của camera dẫn đường để cải thiện độ ổn định khi bám sao trong các lần phơi sáng dài', 'C1'),
    ('focus primary imaging camera', 'verb + noun phrase', 'lấy nét camera chụp chính để đạt kích thước ảnh sao nhỏ và độ sắc nét phù hợp trước chuỗi quan sát', 'B2'),
    ('schedule astronomical observation windows', 'verb + noun phrase', 'lập lịch các khoảng quan sát thiên văn dựa trên độ cao mục tiêu, ánh trăng, thời tiết và yêu cầu của chương trình khoa học', 'C1'),
    ('track celestial targets continuously', 'verb + noun phrase', 'bám các mục tiêu thiên thể liên tục để giữ chúng ổn định trên cảm biến trong suốt phiên quan sát', 'B2'),
    ('monitor observatory dome humidity', 'verb + noun phrase', 'theo dõi độ ẩm trong mái vòm đài quan sát để giảm nguy cơ ngưng tụ trên thiết bị quang học và điện tử', 'B2'),
    ('open dome shutters safely', 'verb + noun phrase', 'mở cửa mái vòm an toàn sau khi xác nhận điều kiện thời tiết và cơ cấu chuyển động đáp ứng yêu cầu vận hành', 'B2'),
    ('close dome before rainfall', 'verb + noun phrase', 'đóng mái vòm trước khi mưa đến để bảo vệ kính thiên văn, cảm biến và thiết bị phụ trợ khỏi nước', 'B2'),
    ('verify weather safety thresholds', 'verb + noun phrase', 'xác nhận các ngưỡng an toàn về gió, độ ẩm, mây và lượng mưa trước khi cho phép quan sát tiếp tục', 'C1'),
    ('park telescope in safe position', 'verb + noun phrase', 'đưa kính thiên văn về vị trí đỗ an toàn để giảm tải cơ khí và tránh va chạm khi kết thúc hoặc gián đoạn vận hành', 'B2'),
    ('slew telescope toward target', 'verb + noun phrase', 'xoay nhanh kính thiên văn tới vùng mục tiêu đã chọn trước khi thực hiện căn chỉnh tinh và bắt đầu quan sát', 'B2'),
    ('synchronize observatory system clocks', 'verb + noun phrase', 'đồng bộ đồng hồ các hệ thống đài quan sát để dấu thời gian của ảnh, telemetry và nhật ký thống nhất với nhau', 'C1'),
    ('capture detector bias frames', 'verb + noun phrase', 'chụp các khung bias của cảm biến để đo mức tín hiệu điện tử nền phục vụ hiệu chỉnh dữ liệu ảnh khoa học', 'C1'),
    ('record dark calibration frames', 'verb + noun phrase', 'ghi các khung tối với điều kiện phơi sáng phù hợp để mô hình hóa dòng tối và nhiễu nhiệt của cảm biến', 'C1'),
    ('acquire flat field images', 'verb + noun phrase', 'thu các ảnh flat field để hiệu chỉnh chênh lệch độ nhạy pixel và hiện tượng tối góc trong hệ thống tạo ảnh', 'C1'),
    ('correct detector bias signal', 'verb + noun phrase', 'hiệu chỉnh tín hiệu bias của cảm biến khỏi dữ liệu quan sát để loại thành phần điện tử không thuộc nguồn thiên văn', 'C1'),
    ('cool imaging sensor gradually', 'verb + noun phrase', 'làm mát cảm biến chụp ảnh từ từ đến nhiệt độ vận hành để giảm nhiễu nhiệt mà tránh ứng suất hoặc ngưng tụ không mong muốn', 'B2'),
    ('monitor detector temperature stability', 'verb + noun phrase', 'theo dõi độ ổn định nhiệt độ cảm biến để các khung hiệu chuẩn và dữ liệu khoa học có điều kiện nhiệt tương thích', 'C1'),
    ('select appropriate photometric filters', 'verb + noun phrase', 'chọn bộ lọc quang trắc phù hợp với dải bước sóng và mục tiêu đo của chương trình quan sát', 'C1'),
    ('rotate filter wheel positions', 'verb + noun phrase', 'chuyển bánh xe bộ lọc tới đúng vị trí để thay đổi dải quang phổ quan sát theo trình tự đã lập', 'B2'),
    ('guide long exposure sequences', 'verb + noun phrase', 'dẫn đường cho chuỗi phơi sáng dài bằng sao tham chiếu để hạn chế kéo vệt do sai số bám của giá đỡ', 'C1'),
    ('dither telescope pointing between exposures', 'verb + noun phrase', 'dịch nhẹ hướng kính thiên văn giữa các lần phơi sáng để giảm ảnh hưởng của pixel lỗi và mẫu nhiễu cố định khi ghép ảnh', 'C1'),
    ('reduce raw astronomical images', 'verb + noun phrase', 'xử lý sơ cấp ảnh thiên văn thô bằng các bước hiệu chuẩn và làm sạch cần thiết trước phân tích khoa học', 'C1'),
    ('subtract sky background signal', 'verb + noun phrase', 'trừ tín hiệu nền bầu trời khỏi ảnh để tách tốt hơn thông lượng của nguồn thiên văn cần đo', 'C1'),
    ('solve astrometric image positions', 'verb + noun phrase', 'giải nghiệm trắc vị trí ảnh để ánh xạ pixel sang tọa độ bầu trời và xác định chính xác trường quan sát', 'C1'),
    ('calibrate photometric zero points', 'verb + noun phrase', 'hiệu chuẩn điểm không quang trắc từ sao chuẩn để chuyển tín hiệu thiết bị thành độ sáng có thể so sánh', 'C1'),
    ('flag saturated detector pixels', 'verb + noun phrase', 'đánh dấu các pixel cảm biến bị bão hòa để chúng không làm sai lệch phép đo độ sáng hoặc hình dạng nguồn', 'B2'),
    ('mask cosmic ray artifacts', 'verb + noun phrase', 'che các vệt và điểm do tia vũ trụ tạo ra để tránh nhầm chúng với tín hiệu thiên văn thật trong xử lý ảnh', 'C1'),
    ('combine calibrated exposure frames', 'verb + noun phrase', 'ghép các khung phơi sáng đã hiệu chuẩn để tăng tỷ lệ tín hiệu trên nhiễu và loại các sai lệch ngẫu nhiên', 'C1'),
    ('archive raw observation data', 'verb + noun phrase', 'lưu trữ dữ liệu quan sát thô cùng cấu trúc thư mục và metadata phù hợp để có thể tái xử lý về sau', 'B2'),
    ('annotate nightly observation logs', 'verb + noun phrase', 'chú thích nhật ký quan sát mỗi đêm với điều kiện trời, cấu hình thiết bị, sự cố và các quyết định vận hành quan trọng', 'B2'),
    ('verify target sky coordinates', 'verb + noun phrase', 'xác nhận tọa độ bầu trời của mục tiêu trước khi quan sát để tránh trỏ nhầm trường hoặc dùng hệ quy chiếu không phù hợp', 'B2'),
    ('update moving target ephemerides', 'verb + noun phrase', 'cập nhật lịch thiên thể cho các mục tiêu chuyển động để tọa độ dự báo phản ánh đúng thời điểm quan sát', 'C1'),
    ('compensate atmospheric refraction effects', 'verb + noun phrase', 'bù ảnh hưởng khúc xạ khí quyển khi cần để cải thiện độ chính xác vị trí ở các góc cao thấp khác nhau', 'C1'),
    ('measure atmospheric seeing conditions', 'verb + noun phrase', 'đo điều kiện seeing của khí quyển để đánh giá độ nhòe ảnh và lựa chọn mục tiêu hoặc cấu hình quan sát phù hợp', 'C1'),
    ('monitor nighttime sky transparency', 'verb + noun phrase', 'theo dõi độ trong suốt của bầu trời ban đêm để phát hiện mây mỏng hoặc suy giảm truyền sáng ảnh hưởng đến phép đo quang trắc', 'C1'),
    ('inspect dome drive mechanisms', 'verb + noun phrase', 'kiểm tra cơ cấu truyền động mái vòm để phát hiện hao mòn, sai lệch hoặc vật cản trước khi vận hành tự động', 'B2'),
    ('test emergency dome closure', 'verb + noun phrase', 'kiểm thử chức năng đóng mái vòm khẩn cấp để xác nhận hệ thống có thể bảo vệ thiết bị khi thời tiết xấu hoặc mất điều khiển', 'C1'),
    ('document instrument configuration changes', 'verb + noun phrase', 'ghi lại các thay đổi cấu hình thiết bị để dữ liệu quan sát có đầy đủ bối cảnh và có thể tái lập quy trình thu nhận', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-69-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v69'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-69-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-68 checkpoint verification: `200511cb4fbd6d6248534d0b30445a76cce03a1d` — scale-67 publication state verified by English Content Master Plan Acceptance #178, English Content Full Validation #152 and Platform CI #1287; published output: `ec3fd17cc756bd31dad93361e6f2b04b94e0e066`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-69 publication: `a937857a17e8319f5bc734b9bda7c2a92fc02fa2` — scale-68 publication state verified by English Content Master Plan Acceptance #182, English Content Full Validation #158 and Platform CI #1295; published output: `0b117abe1ccdede8b79cc4eaa2bb8c632613a547`.',
        'verified scale-68 checkpoint',
    )
    text = replace_once(
        text,
        '- Scale-68 publication is complete at `0b117abe1ccdede8b79cc4eaa2bb8c632613a547`; its bot-triggered PR workflows reached the known `action_required` state before job execution, so one normal-user checkpoint must verify the published state.',
        '- Scale-68 publication checkpoint `a937857a17e8319f5bc734b9bda7c2a92fc02fa2` is fully verified; scale-69 is the current publication unit.',
        'scale-68 verification state',
    )
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,470 published records after scale-68', '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,510 published records after scale-69', 'E04 publication count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-68 publication', '## Published runtime snapshot after E04 scale-69 publication', 'runtime snapshot heading')
    text = replace_once(text, '- phrases: 3,470 records', '- phrases: 3,510 records', 'phrase runtime count')
    text = replace_once(text, '- total published rich records: 8,071', '- total published rich records: 8,111', 'rich runtime count')
    text = replace_once(text, '- editorial ledger: 8,071 decisions / 8,071 applied / 8,071 publish decisions', '- editorial ledger: 8,111 decisions / 8,111 applied / 8,111 publish decisions', 'editorial ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00002360`', '- E04 collocation frontier: `col.00002400`', 'collocation frontier')
    text = replace_once(text, '1. Scale-67 publication is fully verified at `200511cb4fbd6d6248534d0b30445a76cce03a1d`; do not duplicate scale-67 artifacts.', '1. Scale-68 publication is fully verified at `a937857a17e8319f5bc734b9bda7c2a92fc02fa2`; do not duplicate scale-68 artifacts.', 'verified workstream item')
    text = replace_once(text, '2. Scale-68 publication is complete at `0b117abe1ccdede8b79cc4eaa2bb8c632613a547`; do not regenerate or duplicate scale-68 artifacts.', '2. Scale-69 is the current publication unit; do not start another collocation batch until its publication/checkpoint CI completes.', 'publication workstream item')
    text = replace_once(text, '3. Verify the normal-user scale-68 checkpoint with English Content Full Validation, Master Plan Acceptance and Platform CI; scale-68 becomes fully verified only when all three PASS.', '3. After the scale-69 bot publication commit is created, create one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.', 'checkpoint workstream item')
    text = replace_once(text, '5. If no safer pending enrichment appears after the scale-68 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002360`, expected IDs `col.00002361`–`col.00002400`, with fresh exact/near-dedupe preflight before any source apply.', '5. If no safer pending enrichment appears after the scale-69 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002400`, expected IDs `col.00002401`–`col.00002440`, with fresh exact/near-dedupe preflight before any source apply.', 'next batch workstream item')
    old_next = 'Create/verify exactly one normal-user checkpoint for scale-68 publication `0b117abe1ccdede8b79cc4eaa2bb8c632613a547`. After English Content Full Validation, Master Plan Acceptance and Platform CI all PASS on that checkpoint, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002360` (expected next range `col.00002361`–`col.00002400`, unless a safer under-target E04 family takes priority). Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-69 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002400` (expected next range `col.00002401`–`col.00002440`, unless a safer under-target E04 family takes priority). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main69():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-69 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 2360:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 2360, got {max(nums) if nums else None}')

    new = [make_collocation(2361 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-69: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-69-collocations.json',
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
            'id': 'review.e04.scale-69.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-69-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-69-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-69-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-69-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-69-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-69-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 69 astronomical observatory operations collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==2360)', 'if(recallCollocations!==2400)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 2360 reviewed records', 'must expose 2400 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00002361', 'col.00002400'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 2400, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 3510, 'richRecords': 8111},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main69()
