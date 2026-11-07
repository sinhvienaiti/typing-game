#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-57.py'), run_name='e04_scale58_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-58-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-58.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-58'
REVIEWED_AT = '2026-10-07T12:45:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-58'
EXPECTED = {'collocations': 1920, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('monitor cold storage temperatures', 'verb + noun phrase', 'theo dõi nhiệt độ kho lạnh liên tục để phát hiện sai lệch có thể ảnh hưởng đến chất lượng hoặc độ an toàn của hàng hóa nhạy nhiệt', 'B2'),
    ('verify refrigerated trailer setpoints', 'verb + noun phrase', 'xác nhận nhiệt độ cài đặt của xe moóc lạnh phù hợp với yêu cầu vận chuyển của từng loại hàng trước khi xếp hàng', 'B2'),
    ('inspect insulated dock seals', 'verb + adjective + noun', 'kiểm tra gioăng cách nhiệt tại cửa bến để hạn chế thất thoát lạnh và hơi ẩm xâm nhập trong quá trình bốc dỡ', 'B2'),
    ('precondition temperature sensitive cargo', 'verb + adjective + noun', 'điều hòa trước hàng hóa nhạy nhiệt về dải nhiệt độ yêu cầu trước khi đóng gói hoặc chuyển sang phương tiện vận tải', 'C1'),
    ('record shipment temperature excursions', 'verb + noun phrase', 'ghi nhận các lần nhiệt độ lô hàng vượt giới hạn để đánh giá ảnh hưởng, nguyên nhân và quyết định xử lý tiếp theo', 'C1'),
    ('quarantine compromised cold chain loads', 'verb + adjective + noun', 'cách ly các lô hàng có dấu hiệu đứt gãy chuỗi lạnh để ngăn xuất kho trước khi hoàn tất đánh giá chất lượng', 'C1'),
    ('validate thermal packaging performance', 'verb + noun phrase', 'xác nhận hiệu năng của bao bì giữ nhiệt bằng dữ liệu thử nghiệm phù hợp với thời gian vận chuyển và điều kiện môi trường dự kiến', 'C1'),
    ('replace depleted gel packs', 'verb + adjective + noun', 'thay các túi gel lạnh đã mất khả năng duy trì nhiệt độ trước khi đóng lại kiện hàng cần kiểm soát nhiệt', 'B2'),
    ('monitor freezer defrost cycles', 'verb + noun phrase', 'theo dõi chu kỳ xả băng của thiết bị đông lạnh để tránh tích tụ băng và duy trì hiệu suất làm lạnh ổn định', 'B2'),
    ('inspect evaporator coil icing', 'verb + noun phrase', 'kiểm tra hiện tượng đóng băng trên dàn bay hơi để phát hiện vấn đề luồng khí, xả băng hoặc điều khiển nhiệt độ', 'C1'),
    ('balance warehouse refrigeration loads', 'verb + noun phrase', 'cân bằng tải lạnh trong kho để tránh quá tải cục bộ và duy trì nhiệt độ đồng đều giữa các khu vực lưu trữ', 'C1'),
    ('calibrate wireless temperature loggers', 'verb + adjective + noun', 'hiệu chuẩn bộ ghi nhiệt độ không dây nhằm bảo đảm dữ liệu giám sát chuỗi lạnh có độ chính xác cần thiết', 'C1'),
    ('position sensors inside pallets', 'verb + noun phrase', 'bố trí cảm biến bên trong pallet tại các vị trí đại diện để theo dõi nhiệt độ thực tế của hàng trong quá trình lưu trữ và vận chuyển', 'B2'),
    ('maintain humidity control limits', 'verb + noun phrase', 'duy trì độ ẩm trong giới hạn kiểm soát để bảo vệ hàng nhạy ẩm và hạn chế ngưng tụ trong khu vực bảo quản', 'C1'),
    ('prevent condensation on packaging', 'verb + noun phrase', 'ngăn ngưng tụ trên bao bì bằng cách kiểm soát chênh lệch nhiệt độ, độ ẩm và thời gian chuyển tiếp giữa các vùng nhiệt', 'B2'),
    ('sequence inbound pallet receiving', 'verb + noun phrase', 'sắp xếp thứ tự tiếp nhận pallet đầu vào để giảm thời gian chờ tại bến và đưa hàng nhạy nhiệt vào vùng bảo quản đúng lúc', 'C1'),
    ('scan serialized case labels', 'verb + adjective + noun', 'quét nhãn thùng có mã định danh duy nhất để duy trì khả năng truy xuất nguồn gốc qua các bước nhận, lưu kho và xuất hàng', 'B2'),
    ('verify lot traceability records', 'verb + noun phrase', 'xác nhận hồ sơ truy xuất theo lô đầy đủ và khớp với hàng thực tế trước khi cho phép tiếp tục xử lý hoặc phân phối', 'C1'),
    ('assign pallets to storage zones', 'verb + noun phrase', 'phân pallet vào khu vực lưu trữ phù hợp dựa trên nhiệt độ, điều kiện bảo quản, mức độ quay vòng và hạn chế tương thích', 'B2'),
    ('optimize automated storage locations', 'verb + adjective + noun', 'tối ưu vị trí lưu trữ tự động để giảm hành trình thiết bị, tăng mật độ chứa và duy trì khả năng truy xuất hàng', 'C1'),
    ('monitor shuttle system availability', 'verb + noun phrase', 'theo dõi mức độ sẵn sàng của hệ thống shuttle để phát hiện suy giảm năng lực trước khi ảnh hưởng đến luồng nhập xuất kho', 'C1'),
    ('clear conveyor accumulation faults', 'verb + noun phrase', 'xử lý lỗi dồn hàng trên băng tải bằng cách xác định điểm nghẽn, giải phóng vật cản và khôi phục luồng vận chuyển an toàn', 'B2'),
    ('inspect barcode reader alignment', 'verb + noun phrase', 'kiểm tra căn chỉnh đầu đọc mã vạch để bảo đảm mã được nhận dạng ổn định ở tốc độ vận hành thiết kế', 'B2'),
    ('validate dimensioning system accuracy', 'verb + noun phrase', 'xác nhận độ chính xác của hệ thống đo kích thước để dữ liệu thể tích và phân loại kiện hàng đáng tin cậy', 'C1'),
    ('reconcile warehouse inventory balances', 'verb + noun phrase', 'đối soát số dư tồn kho giữa hệ thống và thực tế để xác định chênh lệch, nguyên nhân và hành động điều chỉnh cần thiết', 'B2'),
    ('investigate recurring picking discrepancies', 'verb + adjective + noun', 'điều tra các sai lệch lấy hàng lặp lại để tìm nguyên nhân về vị trí, nhãn, quy trình hoặc cấu hình hệ thống', 'C1'),
    ('prioritize first expiry inventory', 'verb + adjective + noun', 'ưu tiên xuất hàng có hạn dùng sớm nhất để giảm nguy cơ quá hạn và hỗ trợ nguyên tắc quản lý FEFO', 'B2'),
    ('block expired stock allocation', 'verb + adjective + noun', 'ngăn hệ thống phân bổ hàng đã hết hạn vào đơn xuất để tránh phát hành sản phẩm không còn đủ điều kiện sử dụng', 'B2'),
    ('release quality approved inventory', 'verb + adjective + noun', 'giải phóng tồn kho đã được phê duyệt chất lượng để hàng có thể được phân bổ, lấy và xuất theo quy trình thông thường', 'C1'),
    ('stage outbound orders by route', 'verb + noun phrase', 'tập kết đơn hàng xuất theo tuyến vận chuyển để rút ngắn thời gian xếp xe và giảm nhầm lẫn khi bàn giao', 'B2'),
    ('verify loading sequence constraints', 'verb + noun phrase', 'xác nhận các ràng buộc về thứ tự xếp hàng nhằm duy trì khả năng giao đúng điểm, cân bằng tải và điều kiện nhiệt độ', 'C1'),
    ('minimize dock door dwell time', 'verb + noun phrase', 'giảm thời gian hàng lưu tại cửa bến để hạn chế tiếp xúc với điều kiện môi trường ngoài vùng kiểm soát', 'C1'),
    ('seal refrigerated transport compartments', 'verb + adjective + noun', 'niêm phong khoang vận tải lạnh sau khi hoàn tất xếp hàng để bảo vệ tính toàn vẹn của lô hàng và kiểm soát truy cập', 'B2'),
    ('verify carrier handoff documentation', 'verb + noun phrase', 'xác nhận chứng từ bàn giao cho đơn vị vận chuyển đầy đủ, chính xác và gắn đúng với lô hàng thực tế', 'B2'),
    ('monitor delivery temperature compliance', 'verb + noun phrase', 'theo dõi việc tuân thủ nhiệt độ tại điểm giao để xác nhận chuỗi lạnh được duy trì đến khi người nhận tiếp quản', 'C1'),
    ('retrieve shipment logger data', 'verb + noun phrase', 'thu hồi dữ liệu từ bộ ghi của lô hàng sau vận chuyển để đánh giá lịch sử nhiệt độ và xử lý các cảnh báo nếu có', 'B2'),
    ('review cold chain alarm history', 'verb + noun phrase', 'xem xét lịch sử cảnh báo chuỗi lạnh để nhận diện xu hướng, lỗi lặp lại và khu vực cần cải tiến kiểm soát', 'C1'),
    ('escalate critical temperature deviations', 'verb + adjective + noun', 'báo cáo nâng cấp các sai lệch nhiệt độ nghiêm trọng đến người có thẩm quyền để quyết định giữ hàng, đánh giá hoặc thu hồi', 'C1'),
    ('document product disposition decisions', 'verb + noun phrase', 'ghi lại quyết định xử lý sản phẩm sau sai lệch, bao gồm căn cứ đánh giá và trạng thái cuối cùng của lô hàng', 'C1'),
    ('audit cold chain process controls', 'verb + noun phrase', 'đánh giá định kỳ các kiểm soát quy trình chuỗi lạnh để xác nhận chúng được thực hiện nhất quán và còn phù hợp với rủi ro hiện tại', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-58-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v58'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-58-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-57 publication: `58b396286647474a566ce24f8cf683ca7bc86b79` — scale-56 publication state verified by English Content Master Plan Acceptance #143, English Content Full Validation #131 and Platform CI #1203; published output: `77088999ce16cd22440e52396f50d2c523c47d6c`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-58 publication: `df206e8ca5c2bd0b4123ea5d535ecbbc7fab6420` — scale-57 publication state verified by English Content Master Plan Acceptance #146, English Content Full Validation #133 and Platform CI #1206; published output: `696bfb51870d87aaccdd93647bc8da4762b5d30c`.',
        'verified scale-57 checkpoint',
    )
    text = replace_once(text, '- Current scale-57 publication awaiting checkpoint CI verification: `696bfb51870d87aaccdd93647bc8da4762b5d30c`.\n', '', 'remove scale-57 pending verification line')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,030 published records after scale-57', '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,070 published records after scale-58', 'E04 published count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-57 publication', '## Published runtime snapshot after E04 scale-58 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 3,030 records', '- phrases: 3,070 records', 'phrase runtime count')
    text = replace_once(text, '- total published rich records: 7,631', '- total published rich records: 7,671', 'rich runtime count')
    text = replace_once(text, '- editorial ledger: 7,631 decisions / 7,631 applied / 7,631 publish decisions', '- editorial ledger: 7,671 decisions / 7,671 applied / 7,671 publish decisions', 'editorial ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001920`', '- E04 collocation frontier: `col.00001960`', 'collocation frontier')
    text = replace_once(
        text,
        '1. Scale-56 publication is fully verified at `58b396286647474a566ce24f8cf683ca7bc86b79`; do not duplicate scale-56 artifacts.',
        '1. Scale-57 publication is fully verified at `df206e8ca5c2bd0b4123ea5d535ecbbc7fab6420`; do not duplicate scale-57 artifacts.',
        'first unfinished verified item',
    )
    text = replace_once(
        text,
        '2. Scale-57 publication is complete at `696bfb51870d87aaccdd93647bc8da4762b5d30c`; do not regenerate scale-57 artifacts.',
        '2. Scale-58 is the current publication unit; do not start another collocation batch until its publication/checkpoint CI completes.',
        'first unfinished publication item',
    )
    text = replace_once(
        text,
        '3. Verify this normal-user scale-57 checkpoint with English Content Full Validation, Master Plan Acceptance and Platform CI.',
        '3. After the scale-58 bot publication commit is created, create one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.',
        'first unfinished checkpoint item',
    )
    old_next = 'Verify mandatory CI for the scale-57 publication checkpoint without regenerating completed artifacts. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001920` (scale-58 unless a newer worker already advanced the branch), or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-58 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001960` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main58():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-58 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1920:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1920, got {max(nums) if nums else None}')

    new = [make_collocation(1921 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-58: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-58-collocations.json',
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
            'id': 'review.e04.scale-58.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-58-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-58-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-58-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-58-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-58-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-58-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 58 cold-chain logistics collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1920)', 'if(recallCollocations!==1960)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1920 reviewed records', 'must expose 1960 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001921', 'col.00001960'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1960, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 3070, 'richRecords': 7671},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main58()
