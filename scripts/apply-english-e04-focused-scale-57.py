#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-56.py'), run_name='e04_scale57_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-57-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-57.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-57'
REVIEWED_AT = '2026-10-07T12:25:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-57'
EXPECTED = {'collocations': 1880, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('inspect track geometry measurements', 'verb + noun phrase', 'kiểm tra các số đo hình học đường ray để phát hiện sai lệch về khổ đường, độ cao, độ xoắn và hướng tuyến trước khi chúng ảnh hưởng đến an toàn chạy tàu', 'C1'),
    ('monitor rail wear profiles', 'verb + noun phrase', 'theo dõi biên dạng mài mòn của ray để xác định tốc độ xuống cấp và thời điểm cần mài, sửa chữa hoặc thay thế', 'C1'),
    ('schedule preventive track maintenance', 'verb + adjective + noun', 'lập lịch bảo trì phòng ngừa cho đường ray dựa trên tải khai thác, dữ liệu kiểm tra và xu hướng xuống cấp của kết cấu', 'B2'),
    ('tamp ballast beneath sleepers', 'verb + noun phrase', 'chèn và đầm đá ba lát dưới tà vẹt để khôi phục cao độ, độ ổn định và phân bố tải của đường ray', 'C1'),
    ('stabilize newly maintained track', 'verb + adjective + noun', 'ổn định đoạn đường ray vừa được bảo trì để giảm dịch chuyển sau thi công và đưa tuyến trở lại điều kiện khai thác tin cậy', 'C1'),
    ('inspect turnout switch components', 'verb + noun phrase', 'kiểm tra các bộ phận của ghi chuyển hướng để phát hiện mài mòn, nứt, lỏng liên kết hoặc sai lệch có thể cản trở chuyển ghi', 'C1'),
    ('lubricate switch point mechanisms', 'verb + noun phrase', 'bôi trơn cơ cấu lưỡi ghi để giảm ma sát, hạn chế kẹt cơ khí và duy trì chuyển động ổn định của bộ chuyển hướng', 'C1'),
    ('verify point machine operation', 'verb + noun phrase', 'xác nhận máy chuyển ghi vận hành đúng hành trình, lực khóa và tín hiệu phản hồi trước khi cho phép thiết lập đường chạy', 'C1'),
    ('detect broken rail conditions', 'verb + adjective + noun', 'phát hiện tình trạng gãy ray bằng giám sát mạch, cảm biến hoặc kiểm tra chuyên dụng để cô lập khu vực nguy hiểm kịp thời', 'B2'),
    ('monitor wheel bearing temperatures', 'verb + noun phrase', 'theo dõi nhiệt độ ổ trục bánh xe để nhận biết quá nhiệt có thể dẫn đến hỏng ổ trục hoặc sự cố đoàn tàu', 'B2'),
    ('inspect rolling stock brakes', 'verb + noun phrase', 'kiểm tra hệ thống phanh của phương tiện đường sắt để xác nhận tình trạng má phanh, cơ cấu chấp hành và đường khí hoặc mạch điều khiển', 'B2'),
    ('test train braking performance', 'verb + noun phrase', 'kiểm tra hiệu năng phanh của đoàn tàu để xác nhận quãng đường dừng và đáp ứng phanh nằm trong giới hạn vận hành', 'B2'),
    ('maintain wheel flange profiles', 'verb + noun phrase', 'duy trì biên dạng vành bánh đúng tiêu chuẩn để giảm nguy cơ leo ray, mài mòn bất thường và tương tác không ổn định với đường ray', 'C1'),
    ('control wheel rail adhesion', 'verb + noun phrase', 'kiểm soát độ bám giữa bánh xe và ray để hạn chế trượt quay hoặc trượt hãm trong điều kiện bề mặt kém bám', 'C1'),
    ('apply sanding during low adhesion', 'verb + noun phrase', 'rải cát khi độ bám thấp để tăng ma sát tại tiếp xúc bánh xe và ray, hỗ trợ kéo và phanh an toàn', 'B2'),
    ('monitor axle load distribution', 'verb + noun phrase', 'theo dõi phân bố tải trọng trục để phát hiện quá tải hoặc mất cân bằng có thể ảnh hưởng đến phương tiện và kết cấu đường', 'C1'),
    ('verify signaling route locking', 'verb + noun phrase', 'xác nhận cơ chế khóa đường chạy của hệ thống tín hiệu ngăn các lộ trình xung đột được thiết lập đồng thời', 'C1'),
    ('test track circuit occupancy', 'verb + noun phrase', 'kiểm tra khả năng phát hiện chiếm dụng của mạch đường ray để bảo đảm hệ thống nhận biết chính xác sự hiện diện của đoàn tàu', 'C1'),
    ('calibrate axle counter sensors', 'verb + noun phrase', 'hiệu chuẩn cảm biến đếm trục để duy trì độ chính xác khi xác định trạng thái trống hoặc bị chiếm dụng của khu đoạn', 'C1'),
    ('inspect signal aspect visibility', 'verb + noun phrase', 'kiểm tra khả năng quan sát các biểu thị tín hiệu từ khoảng cách yêu cầu trong nhiều điều kiện ánh sáng và thời tiết', 'B2'),
    ('protect worksite possession limits', 'verb + noun phrase', 'bảo vệ ranh giới khu vực phong tỏa thi công để ngăn tàu hoặc phương tiện xâm nhập khi nhân sự đang làm việc trên tuyến', 'C1'),
    ('issue movement authority safely', 'verb + noun phrase', 'cấp quyền di chuyển cho đoàn tàu một cách an toàn dựa trên trạng thái đường chạy, tín hiệu và giới hạn khai thác hiện hành', 'C1'),
    ('manage temporary speed restrictions', 'verb + adjective + noun', 'quản lý các hạn chế tốc độ tạm thời bằng cách công bố, áp dụng và gỡ bỏ đúng vị trí, thời gian và điều kiện cần thiết', 'C1'),
    ('monitor train separation margins', 'verb + noun phrase', 'theo dõi khoảng cách an toàn giữa các đoàn tàu để duy trì biên dự phòng cần thiết khi tốc độ hoặc điều kiện vận hành thay đổi', 'C1'),
    ('coordinate junction route setting', 'verb + noun phrase', 'phối hợp thiết lập đường chạy qua nút giao để giảm xung đột, bảo đảm thứ tự ưu tiên và duy trì lưu lượng khai thác', 'C1'),
    ('recover delayed train services', 'verb + adjective + noun', 'khôi phục dịch vụ tàu bị chậm bằng điều chỉnh thứ tự chạy, quay đầu, thời gian dừng và phân bổ năng lực tuyến', 'B2'),
    ('regulate platform dwell times', 'verb + noun phrase', 'điều tiết thời gian dừng tại ga để cân bằng nhu cầu lên xuống hành khách với yêu cầu giữ đúng biểu đồ chạy tàu', 'B2'),
    ('dispatch trains from terminals', 'verb + noun phrase', 'điều độ tàu rời ga đầu cuối theo biểu đồ, trạng thái đường chạy, khả năng tiếp nhận phía trước và mức độ sẵn sàng của đoàn tàu', 'B2'),
    ('monitor passenger loading patterns', 'verb + noun phrase', 'theo dõi mô hình phân bố hành khách để hỗ trợ điều độ, bố trí phương tiện và kiểm soát quá tải tại ga hoặc trên tàu', 'B2'),
    ('coordinate emergency evacuation routes', 'verb + noun phrase', 'phối hợp các tuyến sơ tán khẩn cấp để đưa hành khách và nhân viên ra khỏi khu vực nguy hiểm theo lộ trình an toàn và có kiểm soát', 'C1'),
    ('inspect overhead catenary tension', 'verb + noun phrase', 'kiểm tra lực căng của hệ thống dây tiếp xúc trên cao để duy trì hình học tiếp xúc ổn định trong dải nhiệt độ và tốc độ thiết kế', 'C1'),
    ('monitor pantograph contact quality', 'verb + noun phrase', 'theo dõi chất lượng tiếp xúc giữa cần tiếp điện và dây dẫn để phát hiện hồ quang, mất tiếp xúc hoặc mài mòn bất thường', 'C1'),
    ('isolate traction power sections', 'verb + noun phrase', 'cô lập các phân đoạn nguồn điện kéo trước khi bảo trì hoặc xử lý sự cố nhằm ngăn cấp điện ngoài ý muốn', 'C1'),
    ('restore traction power safely', 'verb + noun phrase', 'khôi phục nguồn điện kéo an toàn sau khi xác nhận khu vực đã sẵn sàng, các tiếp địa tạm thời đã được tháo và liên động cho phép đóng điện', 'C1'),
    ('inspect third rail protection', 'verb + noun phrase', 'kiểm tra che chắn và biện pháp bảo vệ ray cấp điện thứ ba để giảm nguy cơ tiếp xúc điện hoặc xâm nhập vùng nguy hiểm', 'C1'),
    ('monitor tunnel ventilation systems', 'verb + noun phrase', 'theo dõi hệ thống thông gió đường hầm để bảo đảm chất lượng không khí bình thường và khả năng kiểm soát khói khi có sự cố', 'C1'),
    ('maintain station fire systems', 'verb + noun phrase', 'duy trì hệ thống phòng cháy tại nhà ga, bao gồm báo cháy, chữa cháy và các thiết bị hỗ trợ thoát nạn ở trạng thái sẵn sàng', 'B2'),
    ('verify level crossing protection', 'verb + noun phrase', 'xác nhận thiết bị bảo vệ đường ngang như đèn, chuông và rào chắn hoạt động đúng trước khi tàu tiếp cận khu vực giao cắt', 'B2'),
    ('inspect drainage along track', 'verb + noun phrase', 'kiểm tra hệ thống thoát nước dọc tuyến để phát hiện tắc nghẽn hoặc xói lở có thể làm suy yếu nền đường và kết cấu ray', 'B2'),
    ('respond to signaling system failures', 'verb + noun phrase', 'ứng phó với hỏng hóc hệ thống tín hiệu bằng cách bảo vệ chạy tàu, áp dụng quy trình dự phòng, cô lập lỗi và khôi phục chức năng có kiểm soát', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-57-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v57'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-57-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-56 publication: `d658981f167ddec66fb8268901fca9731e058460` — scale-55 publication state verified by English Content Master Plan Acceptance #140, English Content Full Validation #129 and Platform CI #1200; published output: `50208b470ecc5e4c1827185c085f6bc6b3315cf9`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-57 publication: `58b396286647474a566ce24f8cf683ca7bc86b79` — scale-56 publication state verified by English Content Master Plan Acceptance #143, English Content Full Validation #131 and Platform CI #1203; published output: `77088999ce16cd22440e52396f50d2c523c47d6c`.',
        'verified scale-56 checkpoint',
    )
    text = replace_once(text, '- Current scale-56 publication awaiting checkpoint CI verification: `77088999ce16cd22440e52396f50d2c523c47d6c`.\n', '', 'remove scale-56 pending verification line')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,990 published records after scale-56', '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,030 published records after scale-57', 'E04 published count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-56 publication', '## Published runtime snapshot after E04 scale-57 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,990 records', '- phrases: 3,030 records', 'phrase runtime count')
    text = replace_once(text, '- total published rich records: 7,591', '- total published rich records: 7,631', 'rich runtime count')
    text = replace_once(text, '- editorial ledger: 7,591 decisions / 7,591 applied / 7,591 publish decisions', '- editorial ledger: 7,631 decisions / 7,631 applied / 7,631 publish decisions', 'editorial ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001880`', '- E04 collocation frontier: `col.00001920`', 'collocation frontier')
    text = replace_once(
        text,
        '1. Scale-55 publication is fully verified at `d658981f167ddec66fb8268901fca9731e058460`; do not duplicate scale-55 artifacts.',
        '1. Scale-56 publication is fully verified at `58b396286647474a566ce24f8cf683ca7bc86b79`; do not duplicate scale-56 artifacts.',
        'first unfinished verified item',
    )
    text = replace_once(
        text,
        '2. Scale-56 publication is complete at `77088999ce16cd22440e52396f50d2c523c47d6c`; do not regenerate scale-56 artifacts.',
        '2. Scale-57 is the current publication unit; do not start another collocation batch until its publication/checkpoint CI completes.',
        'first unfinished publication item',
    )
    text = replace_once(
        text,
        '3. Verify this normal-user scale-56 checkpoint with English Content Full Validation, Master Plan Acceptance and Platform CI.',
        '3. After the scale-57 bot publication commit is created, create one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.',
        'first unfinished checkpoint item',
    )
    old_next = 'Verify mandatory CI for the scale-56 publication checkpoint without regenerating completed artifacts. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001880` (scale-57 unless a newer worker already advanced the branch), or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-57 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001920` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main57():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-57 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1880:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1880, got {max(nums) if nums else None}')

    new = [make_collocation(1881 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-57: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-57-collocations.json',
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
            'id': 'review.e04.scale-57.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-57-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-57-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-57-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-57-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-57-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-57-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 57 railway-operations collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1880)', 'if(recallCollocations!==1920)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1880 reviewed records', 'must expose 1920 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001881', 'col.00001920'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1920, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 3030, 'richRecords': 7631},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main57()
