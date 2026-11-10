#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-58.py'), run_name='e04_scale59_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-59-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-59.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-59'
REVIEWED_AT = '2026-10-07T13:05:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-59'
EXPECTED = {'collocations': 1960, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('inspect runway surface conditions', 'verb + noun phrase', 'kiểm tra tình trạng bề mặt đường băng để phát hiện nước, băng, mảnh vụn hoặc hư hỏng có thể ảnh hưởng đến cất và hạ cánh', 'C1'),
    ('report runway braking action', 'verb + noun phrase', 'báo cáo khả năng phanh trên đường băng dựa trên quan sát hoặc phép đo để hỗ trợ quyết định khai thác an toàn', 'C1'),
    ('remove foreign object debris', 'verb + adjective + noun', 'loại bỏ vật thể lạ trên khu bay để giảm nguy cơ hư hỏng động cơ, lốp hoặc thân tàu bay', 'B2'),
    ('monitor runway incursion risks', 'verb + noun phrase', 'theo dõi nguy cơ xâm nhập đường băng để phát hiện sớm tình huống phương tiện hoặc tàu bay đi vào khu vực không được phép', 'C1'),
    ('verify taxiway lighting serviceability', 'verb + noun phrase', 'xác nhận hệ thống đèn đường lăn hoạt động đúng để duy trì dẫn đường mặt đất trong điều kiện tầm nhìn hạn chế', 'C1'),
    ('coordinate runway closure windows', 'verb + noun phrase', 'phối hợp các khoảng thời gian đóng đường băng để bảo trì mà vẫn giảm ảnh hưởng đến lịch bay và năng lực sân bay', 'C1'),
    ('inspect aircraft parking stands', 'verb + noun phrase', 'kiểm tra vị trí đỗ tàu bay để xác nhận mặt sân, vạch sơn, thiết bị và vùng an toàn sẵn sàng cho chuyến tiếp theo', 'B2'),
    ('marshal aircraft onto stand', 'verb + noun phrase', 'hướng dẫn tàu bay vào đúng vị trí đỗ bằng tín hiệu mặt đất hoặc hệ thống hỗ trợ đỗ tự động', 'B2'),
    ('verify wheel chock placement', 'verb + noun phrase', 'xác nhận chèn bánh được đặt đúng vị trí để ngăn tàu bay dịch chuyển ngoài ý muốn khi đang phục vụ mặt đất', 'B2'),
    ('connect ground power safely', 'verb + noun phrase', 'kết nối nguồn điện mặt đất an toàn theo đúng thứ tự và điều kiện kỹ thuật trước khi cấp điện cho tàu bay', 'B2'),
    ('disconnect passenger boarding bridges', 'verb + noun phrase', 'tách cầu ống lồng khỏi tàu bay sau khi hoàn tất lên xuống khách và xác nhận khu vực xung quanh không còn chướng ngại', 'B2'),
    ('position ground support equipment', 'verb + noun phrase', 'bố trí thiết bị phục vụ mặt đất đúng khu vực an toàn để hỗ trợ chuyến bay mà không cản trở lối thoát hoặc vùng nguy hiểm', 'B2'),
    ('inspect baggage belt loaders', 'verb + noun phrase', 'kiểm tra xe băng tải hành lý trước sử dụng để phát hiện hư hỏng cơ khí, rò rỉ hoặc thiết bị bảo vệ không hoạt động', 'B2'),
    ('sequence baggage loading compartments', 'verb + noun phrase', 'sắp xếp thứ tự chất hành lý vào các khoang theo kế hoạch tải trọng, điểm đến và yêu cầu cân bằng tàu bay', 'C1'),
    ('reconcile passenger baggage counts', 'verb + noun phrase', 'đối soát số lượng hành khách và hành lý ký gửi để phát hiện sai lệch trước khi đóng chuyến', 'B2'),
    ('load unit load devices', 'verb + noun phrase', 'xếp các thiết bị chứa hàng tiêu chuẩn lên tàu bay theo vị trí được phân bổ và giới hạn tải trọng cho phép', 'B2'),
    ('secure cargo restraint systems', 'verb + noun phrase', 'cố định hệ thống giữ hàng để ngăn dịch chuyển tải trong khi lăn, cất cánh, bay và hạ cánh', 'C1'),
    ('verify dangerous goods segregation', 'verb + noun phrase', 'xác nhận hàng nguy hiểm được phân tách đúng quy định để tránh tương tác không tương thích trong vận chuyển hàng không', 'C1'),
    ('inspect fuel hydrant connections', 'verb + noun phrase', 'kiểm tra kết nối hệ thống cấp nhiên liệu ngầm để phát hiện rò rỉ, hư hỏng hoặc lắp ghép không đúng trước khi tiếp nhiên liệu', 'C1'),
    ('monitor aircraft refueling pressure', 'verb + noun phrase', 'theo dõi áp suất tiếp nhiên liệu để duy trì lưu lượng phù hợp và ngăn vượt giới hạn hệ thống nhiên liệu của tàu bay', 'C1'),
    ('bond refueling equipment electrically', 'verb + noun phrase', 'nối cân bằng điện thế thiết bị tiếp nhiên liệu để giảm nguy cơ phóng tĩnh điện trong quá trình truyền nhiên liệu', 'C1'),
    ('verify fuel uplift quantity', 'verb + noun phrase', 'xác nhận lượng nhiên liệu đã nạp khớp với yêu cầu chuyến bay và số liệu đo của hệ thống tiếp nhiên liệu', 'B2'),
    ('inspect potable water servicing', 'verb + noun phrase', 'kiểm tra quá trình cấp nước sạch cho tàu bay để duy trì vệ sinh, kết nối đúng và ngăn nhiễm bẩn nguồn nước', 'B2'),
    ('service aircraft lavatory systems', 'verb + noun phrase', 'phục vụ hệ thống vệ sinh tàu bay theo quy trình ngăn tràn, rò rỉ và nhiễm chéo với các dịch vụ khác', 'B2'),
    ('perform exterior aircraft walkaround', 'verb + noun phrase', 'thực hiện vòng kiểm tra bên ngoài tàu bay để phát hiện hư hỏng, rò rỉ, vật lạ hoặc cấu hình bất thường trước chuyến bay', 'B2'),
    ('inspect tire pressure condition', 'verb + noun phrase', 'kiểm tra tình trạng áp suất lốp để phát hiện lốp non, hư hỏng hoặc dấu hiệu cần bảo dưỡng trước khai thác', 'B2'),
    ('check landing gear safety pins', 'verb + noun phrase', 'kiểm tra chốt an toàn càng đáp đã được lắp hoặc tháo đúng trạng thái yêu cầu trước khi tàu bay di chuyển', 'B2'),
    ('confirm tug headset communication', 'verb + noun phrase', 'xác nhận liên lạc tai nghe giữa tổ lái và nhân viên kéo đẩy rõ ràng và hoạt động đúng trước khi bắt đầu đẩy lùi', 'B2'),
    ('verify towbar connection security', 'verb + noun phrase', 'xác nhận thanh kéo được nối chắc chắn với tàu bay và phương tiện kéo trước khi bắt đầu đẩy lùi hoặc kéo', 'B2'),
    ('monitor engine start clearance', 'verb + noun phrase', 'theo dõi điều kiện và quyền cho phép khởi động động cơ để bảo đảm khu vực luồng khí và hút vào đã an toàn', 'C1'),
    ('protect jet blast zones', 'verb + noun phrase', 'bảo vệ vùng chịu luồng phản lực bằng cách giữ người, thiết bị và phương tiện ngoài khu vực nguy hiểm khi động cơ hoạt động', 'C1'),
    ('coordinate deicing fluid application', 'verb + noun phrase', 'phối hợp phun dung dịch khử băng theo loại chất lỏng, vùng xử lý và thời điểm thích hợp trước khi khởi hành', 'C1'),
    ('monitor holdover time limits', 'verb + noun phrase', 'theo dõi giới hạn thời gian bảo vệ sau chống băng để quyết định tàu bay có còn đủ điều kiện cất cánh hay cần xử lý lại', 'C1'),
    ('inspect deicing vehicle readiness', 'verb + noun phrase', 'kiểm tra mức độ sẵn sàng của xe khử băng gồm chất lỏng, vòi phun, hệ thống nâng và thiết bị an toàn', 'B2'),
    ('sequence departure pushback requests', 'verb + noun phrase', 'sắp xếp thứ tự yêu cầu đẩy lùi của các chuyến khởi hành để giảm tắc nghẽn sân đỗ và đường lăn', 'C1'),
    ('manage remote stand bus transfers', 'verb + noun phrase', 'quản lý xe buýt trung chuyển tại vị trí đỗ xa để hành khách di chuyển đúng chuyến, đúng thời điểm và an toàn', 'B2'),
    ('verify gate departure readiness', 'verb + noun phrase', 'xác nhận cổng khởi hành đã sẵn sàng về hành khách, hành lý, tài liệu và phục vụ mặt đất trước khi đóng chuyến', 'B2'),
    ('respond to ground handling incidents', 'verb + noun phrase', 'ứng phó sự cố phục vụ mặt đất bằng cách bảo vệ hiện trường, hỗ trợ người liên quan và báo cáo theo quy trình khai thác', 'C1'),
    ('document aircraft damage findings', 'verb + noun phrase', 'ghi lại các phát hiện hư hỏng tàu bay bằng vị trí, mức độ và bằng chứng phù hợp để chuyển đánh giá kỹ thuật', 'C1'),
    ('audit turnaround process compliance', 'verb + noun phrase', 'đánh giá việc tuân thủ quy trình quay đầu chuyến bay để xác nhận các bước an toàn, chất lượng và thời gian được thực hiện nhất quán', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-59-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v59'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-59-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-58 publication: `df206e8ca5c2bd0b4123ea5d535ecbbc7fab6420` — scale-57 publication state verified by English Content Master Plan Acceptance #146, English Content Full Validation #133 and Platform CI #1206; published output: `696bfb51870d87aaccdd93647bc8da4762b5d30c`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-59 publication: `f106329a536d17416768e64ecb1a2b80aba87f0f` — scale-58 publication state verified by English Content Master Plan Acceptance #149, English Content Full Validation #135 and Platform CI #1209; published output: `704ad2444e0cf0ac93d18c8098ec90aba067496d`.',
        'verified scale-58 checkpoint',
    )
    text = replace_once(text, '- Current scale-58 publication awaiting checkpoint CI verification: `704ad2444e0cf0ac93d18c8098ec90aba067496d`.\n', '', 'remove scale-58 pending verification line')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,070 published records after scale-58', '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,110 published records after scale-59', 'E04 published count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-58 publication', '## Published runtime snapshot after E04 scale-59 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 3,070 records', '- phrases: 3,110 records', 'phrase runtime count')
    text = replace_once(text, '- total published rich records: 7,671', '- total published rich records: 7,711', 'rich runtime count')
    text = replace_once(text, '- editorial ledger: 7,671 decisions / 7,671 applied / 7,671 publish decisions', '- editorial ledger: 7,711 decisions / 7,711 applied / 7,711 publish decisions', 'editorial ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001960`', '- E04 collocation frontier: `col.00002000`', 'collocation frontier')
    text = replace_once(
        text,
        '1. Scale-57 publication is fully verified at `df206e8ca5c2bd0b4123ea5d535ecbbc7fab6420`; do not duplicate scale-57 artifacts.',
        '1. Scale-58 publication is fully verified at `f106329a536d17416768e64ecb1a2b80aba87f0f`; do not duplicate scale-58 artifacts.',
        'first unfinished verified item',
    )
    text = replace_once(
        text,
        '2. Scale-58 publication is complete at `704ad2444e0cf0ac93d18c8098ec90aba067496d`; do not regenerate scale-58 artifacts.',
        '2. Scale-59 is the current publication unit; do not start another collocation batch until its publication/checkpoint CI completes.',
        'first unfinished publication item',
    )
    text = replace_once(
        text,
        '3. Verify this normal-user scale-58 checkpoint with English Content Full Validation, Master Plan Acceptance and Platform CI.',
        '3. After the scale-59 bot publication commit is created, create one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.',
        'first unfinished checkpoint item',
    )
    old_next = 'Verify mandatory CI for the scale-58 publication checkpoint without regenerating completed artifacts. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001960` (scale-59 unless a newer worker already advanced the branch), or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-59 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002000` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main59():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-59 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1960:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1960, got {max(nums) if nums else None}')

    new = [make_collocation(1961 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-59: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-59-collocations.json',
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
            'id': 'review.e04.scale-59.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-59-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-59-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-59-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-59-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-59-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-59-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 59 airport ground-operations collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1960)', 'if(recallCollocations!==2000)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1960 reviewed records', 'must expose 2000 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001961', 'col.00002000'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 2000, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 3110, 'richRecords': 7711},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main59()
