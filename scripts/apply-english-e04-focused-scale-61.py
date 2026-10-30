#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-60.py'), run_name='e04_scale61_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-61-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-61.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-61'
REVIEWED_AT = '2026-10-07T14:00:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-61'
EXPECTED = {'collocations': 2040, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('sample raw water turbidity', 'verb + noun phrase', 'lấy mẫu độ đục của nước thô tại điểm đại diện để theo dõi biến động nguồn nước và điều chỉnh quá trình xử lý', 'B2'),
    ('monitor intake screen differential', 'verb + noun phrase', 'theo dõi chênh lệch qua lưới chắn nước vào để phát hiện tắc nghẽn do rác, rong hoặc vật thể trôi nổi', 'C1'),
    ('adjust coagulant dosing rate', 'verb + noun phrase', 'điều chỉnh lưu lượng hóa chất keo tụ theo chất lượng nước đầu vào và mục tiêu tạo bông để duy trì hiệu quả xử lý', 'C1'),
    ('calibrate chlorine residual analyzer', 'verb + noun phrase', 'hiệu chuẩn thiết bị phân tích clo dư để bảo đảm số đo dùng cho điều khiển khử trùng chính xác và truy xuất được', 'C1'),
    ('verify flocculation basin mixing', 'verb + noun phrase', 'xác nhận mức khuấy trong bể tạo bông phù hợp để các hạt va chạm và kết tụ mà không phá vỡ bông đã hình thành', 'C1'),
    ('inspect sedimentation scraper mechanism', 'verb + noun phrase', 'kiểm tra cơ cấu gạt bùn của bể lắng để phát hiện kẹt, mòn hoặc chuyển động bất thường trước khi ảnh hưởng đến thu gom bùn', 'C1'),
    ('backwash rapid sand filters', 'verb + noun phrase', 'rửa ngược bộ lọc cát nhanh theo chu kỳ hoặc theo tổn thất áp lực để phục hồi khả năng lọc và loại bỏ cặn tích tụ', 'B2'),
    ('measure filter head loss', 'verb + noun phrase', 'đo tổn thất cột áp qua bộ lọc để đánh giá mức bám cặn và xác định thời điểm cần rửa ngược', 'B2'),
    ('monitor filter breakthrough turbidity', 'verb + noun phrase', 'theo dõi độ đục tăng bất thường sau lọc để phát hiện hiện tượng xuyên lọc trước khi chất lượng nước vượt giới hạn', 'C1'),
    ('control membrane transmembrane pressure', 'verb + noun phrase', 'kiểm soát áp suất xuyên màng trong giới hạn vận hành để duy trì lưu lượng và giảm nguy cơ đóng cặn hoặc hư hỏng màng', 'C1'),
    ('perform membrane integrity testing', 'verb + noun phrase', 'thực hiện kiểm tra tính toàn vẹn của màng để phát hiện rò rỉ, đứt sợi hoặc suy giảm khả năng loại bỏ tạp chất', 'C1'),
    ('chemically clean ultrafiltration modules', 'verb + noun phrase', 'làm sạch hóa học mô-đun siêu lọc theo quy trình kiểm soát nồng độ và thời gian tiếp xúc để phục hồi thông lượng màng', 'C1'),
    ('monitor reverse osmosis recovery', 'verb + noun phrase', 'theo dõi tỷ lệ thu hồi của hệ thống thẩm thấu ngược để cân bằng sản lượng nước, chất lượng và nguy cơ đóng cặn', 'C1'),
    ('adjust antiscalant dosing system', 'verb + noun phrase', 'điều chỉnh hệ thống châm chất chống cáu cặn theo lưu lượng và hóa học nước cấp để bảo vệ màng thẩm thấu ngược', 'C1'),
    ('inspect high-pressure feed pumps', 'verb + noun phrase', 'kiểm tra bơm cấp áp lực cao về rung, rò rỉ, nhiệt độ và tiếng ồn để phát hiện sớm hư hỏng cơ khí', 'B2'),
    ('verify ultraviolet reactor intensity', 'verb + noun phrase', 'xác nhận cường độ tia cực tím của thiết bị phản ứng đủ cho mục tiêu khử trùng trong điều kiện lưu lượng hiện tại', 'C1'),
    ('clean ultraviolet quartz sleeves', 'verb + noun phrase', 'làm sạch ống thạch anh bảo vệ đèn cực tím để loại bỏ cặn bám làm suy giảm truyền tia và hiệu quả khử trùng', 'B2'),
    ('monitor ozone contactor residual', 'verb + noun phrase', 'theo dõi ozone dư trong bể tiếp xúc để xác nhận liều xử lý phù hợp đồng thời hạn chế ozone thoát ra ngoài hệ thống', 'C1'),
    ('inspect ozone destructor unit', 'verb + noun phrase', 'kiểm tra thiết bị phá hủy ozone khí thải để bảo đảm ozone còn dư được xử lý trước khi xả ra khu vực làm việc', 'C1'),
    ('calibrate dissolved oxygen probes', 'verb + noun phrase', 'hiệu chuẩn đầu dò oxy hòa tan để các quyết định điều khiển sục khí dựa trên số liệu chính xác và ổn định', 'B2'),
    ('monitor aeration basin oxygen', 'verb + noun phrase', 'theo dõi oxy hòa tan trong bể sục khí để duy trì điều kiện thích hợp cho vi sinh xử lý chất hữu cơ và nitơ', 'B2'),
    ('adjust return sludge flow', 'verb + noun phrase', 'điều chỉnh lưu lượng bùn tuần hoàn về bể sinh học để kiểm soát nồng độ sinh khối và độ sâu lớp bùn ở bể lắng', 'C1'),
    ('measure sludge blanket depth', 'verb + noun phrase', 'đo độ sâu lớp bùn trong bể lắng để phát hiện tích tụ quá mức và điều chỉnh tuần hoàn hoặc xả bùn', 'B2'),
    ('control waste sludge rate', 'verb + noun phrase', 'kiểm soát tốc độ xả bùn dư để duy trì tuổi bùn mục tiêu và ổn định hiệu suất của quá trình sinh học', 'C1'),
    ('inspect clarifier scum removal', 'verb + noun phrase', 'kiểm tra hệ thống thu váng của bể lắng để bảo đảm dầu mỡ, bọt và vật nổi được loại bỏ đều đặn', 'B2'),
    ('dewater sludge with centrifuges', 'verb + noun phrase', 'tách nước bùn bằng máy ly tâm để giảm thể tích bùn trước vận chuyển, xử lý hoặc tiêu hủy tiếp theo', 'B2'),
    ('condition sludge with polymer', 'verb + noun phrase', 'điều hòa bùn bằng polymer với liều phù hợp để tăng khả năng tách nước và giảm tiêu hao hóa chất', 'C1'),
    ('monitor digester gas pressure', 'verb + noun phrase', 'theo dõi áp suất khí trong bể tiêu hóa để duy trì vận hành an toàn và phát hiện tắc nghẽn hoặc tích áp bất thường', 'C1'),
    ('test biogas methane concentration', 'verb + noun phrase', 'kiểm tra nồng độ methane trong khí sinh học để đánh giá chất lượng khí, hiệu quả tiêu hóa và điều kiện sử dụng năng lượng', 'C1'),
    ('inspect anaerobic digester mixing', 'verb + noun phrase', 'kiểm tra hệ thống khuấy của bể tiêu hóa kỵ khí để duy trì phân bố nhiệt, chất nền và vi sinh đồng đều', 'C1'),
    ('maintain odor control scrubbers', 'verb + noun phrase', 'bảo trì hệ thống tháp rửa kiểm soát mùi để duy trì lưu lượng khí, hóa chất và hiệu quả loại bỏ hợp chất gây mùi', 'B2'),
    ('monitor lift station wet wells', 'verb + noun phrase', 'theo dõi mực nước và trạng thái hố thu của trạm bơm nâng để ngăn tràn và bảo đảm bơm khởi động đúng ngưỡng', 'B2'),
    ('test emergency generator transfer', 'verb + noun phrase', 'kiểm tra chuyển nguồn sang máy phát dự phòng để xác nhận thiết bị thiết yếu tiếp tục hoạt động khi nguồn điện chính bị mất', 'B2'),
    ('inspect distribution reservoir levels', 'verb + noun phrase', 'kiểm tra mực nước bể chứa phân phối để duy trì dự trữ, áp lực mạng và khả năng đáp ứng nhu cầu cao điểm', 'B2'),
    ('flush dead-end water mains', 'verb + noun phrase', 'xả rửa các tuyến ống cụt để loại bỏ cặn lắng, nước lưu lâu và cải thiện chất lượng nước tại vùng ít lưu thông', 'B2'),
    ('verify pressure zone setpoints', 'verb + noun phrase', 'xác nhận các giá trị đặt của vùng áp lực phù hợp để cung cấp nước ổn định mà không gây áp suất quá cao hoặc quá thấp', 'C1'),
    ('locate distribution leak losses', 'verb + noun phrase', 'xác định vị trí thất thoát do rò rỉ trên mạng phân phối bằng dữ liệu lưu lượng, áp lực hoặc thiết bị dò chuyên dụng', 'C1'),
    ('disinfect repaired water mains', 'verb + noun phrase', 'khử trùng tuyến ống nước vừa sửa chữa trước khi đưa trở lại vận hành để giảm nguy cơ nhiễm bẩn vi sinh', 'B2'),
    ('collect regulatory compliance samples', 'verb + noun phrase', 'thu thập mẫu tuân thủ theo vị trí, tần suất và phương pháp quy định để chứng minh chất lượng nước đáp ứng yêu cầu pháp lý', 'C1'),
    ('review treatment process trends', 'verb + noun phrase', 'xem xét xu hướng dữ liệu quá trình xử lý để nhận biết suy giảm hiệu suất, biến động nguồn nước và nhu cầu tối ưu vận hành', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-61-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v61'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-61-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-60 publication: `3022771803cd449b254abfc4ccc60180656819c1` — scale-59 publication state verified by English Content Master Plan Acceptance #153, English Content Full Validation #138 and Platform CI #1213; published output: `4a07d83aa704ccd64a4a994495aac4b560474441`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-61 publication: `700c9a76f181023cd5ae1f0449b6bf29030f7f82` — scale-60 publication state verified by English Content Master Plan Acceptance #156, English Content Full Validation #140 and Platform CI #1216; published output: `e6c4500a5443310b3d7cfc5fd7f4eb3ebad89dc9`.',
        'verified scale-60 checkpoint',
    )
    text = replace_once(text, '- Scale-60 publication completed at `e6c4500a5443310b3d7cfc5fd7f4eb3ebad89dc9`; this checkpoint update exists to verify the publication under a normal-user HEAD before opening scale-61.\n', '', 'remove scale-60 checkpoint-pending line')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,150 published records after scale-60', '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,190 published records after scale-61', 'E04 published count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-60 publication', '## Published runtime snapshot after E04 scale-61 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 3,150 records', '- phrases: 3,190 records', 'phrase runtime count')
    text = replace_once(text, '- total published rich records: 7,751', '- total published rich records: 7,791', 'rich runtime count')
    text = replace_once(text, '- editorial ledger: 7,751 decisions / 7,751 applied / 7,751 publish decisions', '- editorial ledger: 7,791 decisions / 7,791 applied / 7,791 publish decisions', 'editorial ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00002040`', '- E04 collocation frontier: `col.00002080`', 'collocation frontier')
    text = replace_once(text, '1. Scale-59 publication is fully verified at `3022771803cd449b254abfc4ccc60180656819c1`; do not duplicate scale-59 artifacts.', '1. Scale-60 publication is fully verified at `700c9a76f181023cd5ae1f0449b6bf29030f7f82`; do not duplicate scale-60 artifacts.', 'verified workstream item')
    text = replace_once(text, '2. Scale-60 publication completed at `e6c4500a5443310b3d7cfc5fd7f4eb3ebad89dc9`; do not regenerate scale-60 artifacts.', '2. Scale-61 is the current publication unit; do not start another collocation batch until its publication/checkpoint CI completes.', 'publication workstream item')
    text = replace_once(text, '3. Verify English Content Full Validation, Master Plan Acceptance and Platform CI on this normal-user checkpoint before attaching any scale-61 preparation commit.', '3. After the scale-61 bot publication commit is created, create one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.', 'checkpoint workstream item')
    text = replace_once(text, '5. If all checkpoint gates PASS and no safer pending enrichment appears, create the next bounded E04 collocation scale batch from frontier `col.00002040`, with fresh exact/near-dedupe preflight before any source apply.', '5. If no safer pending enrichment appears after the scale-61 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002080`, with fresh exact/near-dedupe preflight before any source apply.', 'next batch workstream item')
    old_next = 'Verify all three mandatory CI workflows for the scale-60 normal-user checkpoint. If PASS, continue immediately with a genuinely new bounded collocation batch from frontier `col.00002040` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-61 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002080` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main61():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-61 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 2040:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 2040, got {max(nums) if nums else None}')

    new = [make_collocation(2041 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-61: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-61-collocations.json',
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
            'id': 'review.e04.scale-61.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-61-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-61-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-61-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-61-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-61-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-61-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 61 water-treatment and utility operations collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==2040)', 'if(recallCollocations!==2080)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 2040 reviewed records', 'must expose 2080 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00002041', 'col.00002080'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 2080, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 3190, 'richRecords': 7791},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main61()
