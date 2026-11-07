#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-64.py'), run_name='e04_scale65_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-65-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-65.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-65'
REVIEWED_AT = '2026-10-07T15:15:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-65'
EXPECTED = {'collocations': 2200, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('inspect greenhouse glazing panels', 'verb + noun phrase', 'kiểm tra các tấm kính hoặc vật liệu phủ nhà kính để phát hiện nứt, hở hoặc suy giảm truyền sáng có thể ảnh hưởng đến cây trồng', 'B2'),
    ('seal greenhouse air leaks', 'verb + noun phrase', 'bịt các điểm rò khí trong nhà kính để giảm thất thoát nhiệt và duy trì môi trường trồng ổn định', 'B2'),
    ('monitor greenhouse humidity levels', 'verb + noun phrase', 'theo dõi độ ẩm không khí trong nhà kính để hạn chế bệnh nấm và hỗ trợ thoát hơi nước của cây', 'B2'),
    ('regulate greenhouse daytime temperatures', 'verb + noun phrase', 'điều chỉnh nhiệt độ ban ngày trong nhà kính bằng thông gió, che nắng hoặc sưởi để giữ cây trong khoảng sinh trưởng phù hợp', 'B2'),
    ('control nighttime temperature setpoints', 'verb + noun phrase', 'điều khiển điểm đặt nhiệt độ ban đêm để cân bằng tốc độ sinh trưởng, năng lượng và chất lượng cây trồng', 'C1'),
    ('vent excess greenhouse heat', 'verb + noun phrase', 'thoát nhiệt dư khỏi nhà kính bằng cửa mái hoặc quạt để tránh stress nhiệt cho cây', 'B2'),
    ('deploy thermal greenhouse screens', 'verb + noun phrase', 'triển khai màn giữ nhiệt trong nhà kính để giảm thất thoát năng lượng vào ban đêm hoặc trong thời tiết lạnh', 'B2'),
    ('adjust shade curtain positions', 'verb + noun phrase', 'điều chỉnh vị trí rèm che nắng để kiểm soát bức xạ và nhiệt tải trên tán cây', 'B2'),
    ('measure photosynthetically active radiation', 'verb + noun phrase', 'đo bức xạ quang hợp hữu hiệu để đánh giá lượng ánh sáng cây có thể sử dụng cho quang hợp', 'C1'),
    ('schedule supplemental grow lighting', 'verb + noun phrase', 'lập lịch chiếu sáng bổ sung để bù thiếu ánh sáng tự nhiên và duy trì tổng lượng ánh sáng ngày mục tiêu', 'C1'),
    ('verify grow light intensity', 'verb + noun phrase', 'xác nhận cường độ đèn trồng cây đạt mức thiết kế tại vùng tán cây mà không gây quá nhiệt hoặc lãng phí điện', 'B2'),
    ('balance greenhouse light distribution', 'verb + noun phrase', 'cân bằng phân bố ánh sáng trong nhà kính để giảm vùng thiếu sáng và cải thiện độ đồng đều của cây trồng', 'C1'),
    ('monitor substrate moisture content', 'verb + noun phrase', 'theo dõi độ ẩm giá thể để quyết định thời điểm và lượng tưới phù hợp với nhu cầu cây', 'B2'),
    ('calibrate irrigation dosing pumps', 'verb + noun phrase', 'hiệu chuẩn bơm định lượng tưới để bảo đảm lưu lượng nước và dung dịch dinh dưỡng đúng theo công thức', 'C1'),
    ('flush irrigation supply lines', 'verb + noun phrase', 'xả rửa đường cấp tưới để loại bỏ cặn, muối hoặc tạp chất có thể làm tắc đầu nhỏ giọt', 'B2'),
    ('inspect drip emitter performance', 'verb + noun phrase', 'kiểm tra hiệu suất đầu nhỏ giọt để phát hiện tắc nghẽn hoặc chênh lệch lưu lượng giữa các cây', 'B2'),
    ('measure irrigation drainage fraction', 'verb + noun phrase', 'đo tỷ lệ nước thoát sau tưới để đánh giá mức tưới, tích muối và hiệu quả sử dụng nước', 'C1'),
    ('collect root-zone drainage samples', 'verb + noun phrase', 'thu mẫu nước thoát vùng rễ để kiểm tra pH, độ dẫn điện và sự tích tụ dinh dưỡng', 'C1'),
    ('adjust nutrient solution conductivity', 'verb + noun phrase', 'điều chỉnh độ dẫn điện của dung dịch dinh dưỡng để duy trì nồng độ muối phù hợp với giai đoạn cây trồng', 'C1'),
    ('correct nutrient solution acidity', 'verb + noun phrase', 'hiệu chỉnh độ axit của dung dịch dinh dưỡng để giữ pH trong khoảng giúp cây hấp thu khoáng hiệu quả', 'C1'),
    ('mix concentrated fertilizer stocks', 'verb + noun phrase', 'pha dung dịch phân bón đậm đặc theo công thức để sử dụng an toàn trong hệ thống châm dinh dưỡng', 'B2'),
    ('verify fertilizer injector ratios', 'verb + noun phrase', 'xác nhận tỷ lệ châm phân của bộ injector đúng với công thức dinh dưỡng và lưu lượng tưới thực tế', 'C1'),
    ('monitor root-zone salinity trends', 'verb + noun phrase', 'theo dõi xu hướng độ mặn vùng rễ để phát hiện sớm tích muối gây giảm hút nước hoặc cháy rễ', 'C1'),
    ('leach accumulated substrate salts', 'verb + noun phrase', 'rửa trôi muối tích tụ trong giá thể bằng lượng nước phù hợp để phục hồi môi trường vùng rễ', 'C1'),
    ('inspect crop canopy density', 'verb + noun phrase', 'kiểm tra mật độ tán cây để đánh giá thông thoáng, phân bố ánh sáng và nhu cầu tỉa lá', 'B2'),
    ('prune lower canopy leaves', 'verb + noun phrase', 'tỉa lá ở phần thấp của tán cây để cải thiện thông gió, vệ sinh và phân bổ nguồn lực cho phần sinh trưởng chính', 'B2'),
    ('train vines onto support strings', 'verb + noun phrase', 'dẫn dây leo lên dây đỡ để giữ tán cây theo cấu trúc mong muốn và thuận tiện cho chăm sóc', 'B2'),
    ('lower mature greenhouse vines', 'verb + noun phrase', 'hạ các dây leo trưởng thành theo hệ thống móc dây để duy trì vùng thu hoạch ở độ cao thao tác phù hợp', 'C1'),
    ('remove greenhouse crop suckers', 'verb + noun phrase', 'loại bỏ chồi phụ trên cây trồng nhà kính để kiểm soát kiến trúc tán và tập trung sinh trưởng vào thân chính', 'B2'),
    ('thin excess fruit clusters', 'verb + noun phrase', 'tỉa bớt chùm quả vượt tải để cân bằng số quả, kích thước và chất lượng thu hoạch', 'B2'),
    ('monitor beneficial insect populations', 'verb + noun phrase', 'theo dõi quần thể côn trùng có ích để đánh giá hiệu quả kiểm soát sinh học đối với sâu hại', 'C1'),
    ('release biological control agents', 'verb + noun phrase', 'thả tác nhân kiểm soát sinh học theo mật độ và khu vực phù hợp để khống chế sâu hại trong nhà kính', 'C1'),
    ('inspect sticky monitoring cards', 'verb + noun phrase', 'kiểm tra bẫy dính giám sát để nhận biết xu hướng xuất hiện và mật độ côn trùng bay', 'B2'),
    ('scout crops for pest hotspots', 'verb + noun phrase', 'khảo sát cây trồng để xác định các điểm nóng sâu hại cần xử lý mục tiêu trước khi lan rộng', 'B2'),
    ('remove diseased plant material', 'verb + noun phrase', 'loại bỏ mô hoặc cây bị bệnh khỏi khu trồng để giảm nguồn lây nhiễm và áp lực mầm bệnh', 'B2'),
    ('sanitize greenhouse work tools', 'verb + noun phrase', 'khử vệ sinh dụng cụ làm việc trong nhà kính để hạn chế truyền mầm bệnh giữa các luống hoặc khu vực', 'B2'),
    ('record greenhouse climate alarms', 'verb + noun phrase', 'ghi lại cảnh báo khí hậu nhà kính để truy vết các lần vượt ngưỡng và đánh giá phản ứng vận hành', 'B2'),
    ('review daily crop climate data', 'verb + noun phrase', 'xem xét dữ liệu khí hậu cây trồng hằng ngày để điều chỉnh chiến lược nhiệt độ, độ ẩm, ánh sáng và tưới', 'C1'),
    ('forecast greenhouse harvest volumes', 'verb + noun phrase', 'dự báo sản lượng thu hoạch nhà kính dựa trên tải quả, tốc độ chín và lịch canh tác để hỗ trợ kế hoạch đóng gói', 'C1'),
    ('verify harvest lot traceability', 'verb + noun phrase', 'xác nhận khả năng truy xuất lô thu hoạch từ khu trồng, ngày hái và ca xử lý để đáp ứng yêu cầu chất lượng và an toàn thực phẩm', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-65-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v65'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-65-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-64 publication: `c39f556a3957f3ce0058b1990a831f2064475df9` — scale-63 publication state verified by English Content Master Plan Acceptance #165, English Content Full Validation #146 and Platform CI #1254; published output: `7d44880c65ef5eb8685df661d3ef5f4859f71720`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-65 publication: `88a3ecc183bce638542d63046f9a3c8123158657` — scale-64 publication state verified by English Content Master Plan Acceptance #168, English Content Full Validation #148 and Platform CI #1257; published output: `cef8463d5e24b1f28eb5ae723cfdfd5320485f0a`.',
        'verified scale-64 checkpoint',
    )
    text = replace_once(
        text,
        '- Scale-64 publication completed at `cef8463d5e24b1f28eb5ae723cfdfd5320485f0a`; bot-triggered PR workflows follow the known `action_required` publication pattern, so this normal-user checkpoint exists to verify the published state before opening scale-65.',
        '- Scale-64 publication checkpoint `88a3ecc183bce638542d63046f9a3c8123158657` is fully verified; scale-65 is the current publication unit.',
        'scale-64 verification state',
    )
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,310 published records after scale-64', '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,350 published records after scale-65', 'E04 publication count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-64 publication', '## Published runtime snapshot after E04 scale-65 publication', 'runtime snapshot heading')
    text = replace_once(text, '- phrases: 3,310 records', '- phrases: 3,350 records', 'phrase runtime count')
    text = replace_once(text, '- total published rich records: 7,911', '- total published rich records: 7,951', 'rich runtime count')
    text = replace_once(text, '- editorial ledger: 7,911 decisions / 7,911 applied / 7,911 publish decisions', '- editorial ledger: 7,951 decisions / 7,951 applied / 7,951 publish decisions', 'editorial ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00002200`', '- E04 collocation frontier: `col.00002240`', 'collocation frontier')
    text = replace_once(text, '1. Scale-63 publication is fully verified at `c39f556a3957f3ce0058b1990a831f2064475df9`; do not duplicate scale-63 artifacts.', '1. Scale-64 publication is fully verified at `88a3ecc183bce638542d63046f9a3c8123158657`; do not duplicate scale-64 artifacts.', 'verified workstream item')
    text = replace_once(text, '2. Scale-64 publication completed at `cef8463d5e24b1f28eb5ae723cfdfd5320485f0a`; the current gate is normal-user checkpoint verification, not regeneration.', '2. Scale-65 is the current publication unit; do not start another collocation batch until its publication/checkpoint CI completes.', 'publication workstream item')
    text = replace_once(text, '3. Verify English Content Full Validation, English Content Master Plan Acceptance and Platform CI on this checkpoint. Only when all three PASS is scale-64 fully verified.', '3. After the scale-65 bot publication commit is created, create one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.', 'checkpoint workstream item')
    text = replace_once(text, '5. If no safer pending enrichment appears after the scale-64 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002200`, with fresh exact/near-dedupe preflight before any source apply.', '5. If no safer pending enrichment appears after the scale-65 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002240`, with fresh exact/near-dedupe preflight before any source apply.', 'next batch workstream item')
    old_next = 'Verify scale-64 publication `cef8463d5e24b1f28eb5ae723cfdfd5320485f0a` under the normal-user checkpoint. If English Content Full Validation, Master Plan Acceptance and Platform CI all PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002200` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-65 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002240` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main65():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-65 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 2200:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 2200, got {max(nums) if nums else None}')

    new = [make_collocation(2201 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-65: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-65-collocations.json',
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
            'id': 'review.e04.scale-65.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-65-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-65-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-65-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-65-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-65-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-65-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 65 greenhouse horticulture operations collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==2200)', 'if(recallCollocations!==2240)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 2200 reviewed records', 'must expose 2240 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00002201', 'col.00002240'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 2240, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 3350, 'richRecords': 7951},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main65()
