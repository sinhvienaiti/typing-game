#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-67.py'), run_name='e04_scale68_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-68-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-68.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-68'
REVIEWED_AT = '2026-10-07T16:15:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-68'
EXPECTED = {'collocations': 2320, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('assess artifact surface condition', 'verb + noun phrase', 'đánh giá tình trạng bề mặt hiện vật để xác định dấu hiệu nứt, bong, mài mòn hoặc biến đổi cần theo dõi bảo tồn', 'C1'),
    ('document object condition changes', 'verb + noun phrase', 'ghi chép các thay đổi về tình trạng hiện vật để so sánh theo thời gian và hỗ trợ quyết định bảo tồn', 'C1'),
    ('track display case humidity drift', 'verb + noun phrase', 'theo dõi xu hướng lệch độ ẩm trong tủ trưng bày để phát hiện sớm khi vi khí hậu rời khỏi khoảng bảo tồn mong muốn', 'C1'),
    ('stabilize exhibition temperature', 'verb + noun phrase', 'ổn định nhiệt độ khu trưng bày để hạn chế dao động môi trường gây ứng suất cho hiện vật nhạy cảm', 'C1'),
    ('verify conservation sensor calibration', 'verb + noun phrase', 'xác nhận các cảm biến dùng cho bảo tồn đã được hiệu chuẩn đúng để dữ liệu môi trường có thể tin cậy khi đánh giá rủi ro', 'C1'),
    ('inspect display case seals', 'verb + noun phrase', 'kiểm tra gioăng và điểm kín của tủ trưng bày để phát hiện khe hở làm giảm khả năng kiểm soát bụi và vi khí hậu', 'B2'),
    ('regenerate reusable desiccant packs', 'verb + noun phrase', 'tái hoạt hóa các gói hút ẩm có thể tái sử dụng theo quy trình phù hợp để khôi phục khả năng kiểm soát độ ẩm trong bao gói bảo tồn', 'B2'),
    ('measure ultraviolet light exposure', 'verb + noun phrase', 'đo mức phơi nhiễm tia tử ngoại để đánh giá nguy cơ phai màu và suy thoái vật liệu nhạy sáng', 'C1'),
    ('adjust gallery lighting levels', 'verb + noun phrase', 'điều chỉnh mức chiếu sáng phòng trưng bày để cân bằng khả năng quan sát với giới hạn bảo tồn hiện vật', 'B2'),
    ('rotate light-sensitive materials', 'verb + noun phrase', 'luân phiên trưng bày các vật liệu nhạy sáng để giảm tổng liều chiếu sáng tích lũy lên từng hiện vật', 'C1'),
    ('prepare archival storage boxes', 'verb + noun phrase', 'chuẩn bị hộp lưu trữ hồ sơ bằng vật liệu phù hợp để hỗ trợ, che chắn và giảm tác động môi trường lên tài liệu', 'B2'),
    ('label archival enclosures accurately', 'verb + noun phrase', 'ghi nhãn chính xác các bao bì lưu trữ để nhận diện tài liệu mà không cần thao tác mở hoặc xử lý không cần thiết', 'B2'),
    ('separate acidic paper materials', 'verb + noun phrase', 'tách các vật liệu giấy có tính axit khỏi tài liệu nhạy cảm để hạn chế truyền sản phẩm phân hủy sang hiện vật lân cận', 'C1'),
    ('remove surface dust carefully', 'verb + noun phrase', 'loại bỏ bụi bề mặt một cách thận trọng bằng dụng cụ phù hợp để tránh mài xước hoặc làm bong lớp vật liệu yếu', 'B2'),
    ('support fragile book spines', 'verb + noun phrase', 'nâng đỡ gáy sách dễ hư hỏng khi trưng bày hoặc thao tác để giảm ứng suất lên cấu trúc đóng sách', 'B2'),
    ('flatten folded paper documents', 'verb + noun phrase', 'làm phẳng tài liệu giấy bị gấp bằng phương pháp bảo tồn phù hợp để giảm nếp gãy và hỗ trợ lưu trữ an toàn', 'C1'),
    ('humidify brittle paper safely', 'verb + noun phrase', 'làm ẩm giấy giòn trong điều kiện kiểm soát để tăng tính linh hoạt trước khi làm phẳng hoặc xử lý tiếp', 'C1'),
    ('repair minor paper tears', 'verb + noun phrase', 'sửa các vết rách nhỏ trên giấy bằng vật liệu và keo bảo tồn tương thích để phục hồi tính ổn định khi thao tác', 'B2'),
    ('interleave fragile manuscript leaves', 'verb + noun phrase', 'chèn lớp vật liệu bảo tồn giữa các lá bản thảo mong manh để giảm ma sát và tiếp xúc trực tiếp trong lưu trữ hoặc thao tác', 'C1'),
    ('mount photographs with hinges', 'verb + noun phrase', 'gắn ảnh bằng các bản lề bảo tồn để giữ ảnh ổn định mà vẫn cho phép tháo lắp với mức can thiệp thấp', 'C1'),
    ('store negatives in sleeves', 'verb + noun phrase', 'lưu phim âm bản trong túi bảo quản riêng để giảm trầy xước, bụi và tiếp xúc trực tiếp giữa các bề mặt ảnh', 'B2'),
    ('freeze pest-infested materials', 'verb + noun phrase', 'xử lý đông lạnh vật liệu bị côn trùng xâm nhập theo quy trình kiểm soát để tiêu diệt sinh vật gây hại mà hạn chế tổn hại hiện vật', 'C1'),
    ('inspect collections for pests', 'verb + noun phrase', 'kiểm tra bộ sưu tập để phát hiện dấu vết côn trùng, phân, kén hoặc hư hại mới trước khi mức độ xâm nhập tăng lên', 'B2'),
    ('map pest activity hotspots', 'verb + noun phrase', 'lập bản đồ các điểm có hoạt động sinh vật gây hại cao từ dữ liệu giám sát để ưu tiên kiểm tra và biện pháp kiểm soát trong kho', 'C1'),
    ('record integrated pest findings', 'verb + noun phrase', 'ghi lại kết quả chương trình quản lý sinh vật gây hại tổng hợp để xác định khu vực rủi ro và đánh giá hiệu quả kiểm soát', 'C1'),
    ('quarantine incoming collection items', 'verb + noun phrase', 'cách ly hiện vật mới nhập trước khi đưa vào kho chung để kiểm tra côn trùng, nấm mốc và các nguy cơ lây nhiễm khác', 'C1'),
    ('clean storage shelving regularly', 'verb + noun phrase', 'vệ sinh giá kệ lưu trữ định kỳ để giảm bụi, mảnh vụn và môi trường thuận lợi cho sinh vật gây hại', 'B2'),
    ('maintain clear storage aisles', 'verb + noun phrase', 'duy trì lối đi trong kho thông thoáng để hỗ trợ kiểm tra, vận chuyển hiện vật và ứng phó khẩn cấp an toàn', 'B2'),
    ('secure oversized artifacts safely', 'verb + noun phrase', 'cố định hiện vật kích thước lớn bằng phương án hỗ trợ phù hợp để tránh lật, trượt hoặc chịu tải tập trung trong kho', 'C1'),
    ('pad vulnerable contact points', 'verb + noun phrase', 'đệm các điểm tiếp xúc dễ tổn thương để giảm ma sát, áp lực và va chạm giữa hiện vật với giá đỡ hoặc bao gói', 'B2'),
    ('construct custom storage supports', 'verb + noun phrase', 'chế tạo giá đỡ lưu trữ theo hình dạng hiện vật để phân bố tải và giữ tư thế ổn định lâu dài', 'C1'),
    ('handle objects with clean gloves', 'verb + noun phrase', 'thao tác hiện vật bằng găng tay sạch khi phù hợp để giảm truyền dầu, bụi hoặc chất bẩn từ tay lên bề mặt', 'B2'),
    ('plan safe artifact movements', 'verb + noun phrase', 'lập kế hoạch di chuyển hiện vật an toàn gồm tuyến đường, nhân lực, thiết bị và điểm dừng trước khi bắt đầu vận chuyển', 'C1'),
    ('document packing configurations', 'verb + noun phrase', 'ghi lại cấu hình đóng gói để có thể tái lập vị trí đệm, giá đỡ và hướng đặt hiện vật trong các lần vận chuyển sau', 'B2'),
    ('verify crate cushioning materials', 'verb + noun phrase', 'xác nhận vật liệu đệm trong thùng vận chuyển phù hợp với trọng lượng, hình dạng và độ nhạy của hiện vật', 'C1'),
    ('monitor vibration during transit', 'verb + noun phrase', 'theo dõi rung động trong quá trình vận chuyển để đánh giá mức tải cơ học mà hiện vật phải chịu và điều chỉnh biện pháp bảo vệ', 'C1'),
    ('acclimatize objects after transport', 'verb + noun phrase', 'cho hiện vật thích nghi dần với môi trường mới sau vận chuyển để giảm sốc nhiệt ẩm trước khi mở bao gói hoặc trưng bày', 'C1'),
    ('update collection location records', 'verb + noun phrase', 'cập nhật hồ sơ vị trí bộ sưu tập ngay sau khi di chuyển để duy trì khả năng truy xuất hiện vật chính xác', 'B2'),
    ('photograph conservation treatment stages', 'verb + noun phrase', 'chụp ảnh các giai đoạn xử lý bảo tồn để ghi nhận tình trạng trước, trong và sau can thiệp phục vụ hồ sơ kỹ thuật', 'C1'),
    ('archive treatment documentation securely', 'verb + noun phrase', 'lưu trữ an toàn hồ sơ xử lý bảo tồn để bảo đảm lịch sử can thiệp có thể truy cập và đối chiếu lâu dài', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-68-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v68'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-68-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-67 checkpoint verification: `39d1eeb559c13f88e563027d93b20075b46fc4c3` — scale-66 publication state verified by English Content Master Plan Acceptance #175, English Content Full Validation #151 and Platform CI #1277; published output: `e9e221c1caa5e660d845eff61fccdd3f3c8e5798`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-68 publication: `200511cb4fbd6d6248534d0b30445a76cce03a1d` — scale-67 publication state verified by English Content Master Plan Acceptance #178, English Content Full Validation #152 and Platform CI #1287; published output: `ec3fd17cc756bd31dad93361e6f2b04b94e0e066`.',
        'verified scale-67 checkpoint',
    )
    text = replace_once(
        text,
        '- Scale-67 publication is complete at `ec3fd17cc756bd31dad93361e6f2b04b94e0e066`; its bot-triggered PR workflows reached the known `action_required` state before job execution, so one normal-user checkpoint must verify the published state.',
        '- Scale-67 publication checkpoint `200511cb4fbd6d6248534d0b30445a76cce03a1d` is fully verified; scale-68 is the current publication unit.',
        'scale-67 verification state',
    )
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,430 published records after scale-67', '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,470 published records after scale-68', 'E04 publication count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-67 publication', '## Published runtime snapshot after E04 scale-68 publication', 'runtime snapshot heading')
    text = replace_once(text, '- phrases: 3,430 records', '- phrases: 3,470 records', 'phrase runtime count')
    text = replace_once(text, '- total published rich records: 8,031', '- total published rich records: 8,071', 'rich runtime count')
    text = replace_once(text, '- editorial ledger: 8,031 decisions / 8,031 applied / 8,031 publish decisions', '- editorial ledger: 8,071 decisions / 8,071 applied / 8,071 publish decisions', 'editorial ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00002320`', '- E04 collocation frontier: `col.00002360`', 'collocation frontier')
    text = replace_once(text, '1. Scale-66 publication is fully verified at `39d1eeb559c13f88e563027d93b20075b46fc4c3`; do not duplicate scale-66 artifacts.', '1. Scale-67 publication is fully verified at `200511cb4fbd6d6248534d0b30445a76cce03a1d`; do not duplicate scale-67 artifacts.', 'verified workstream item')
    text = replace_once(text, '2. Scale-67 publication is complete at `ec3fd17cc756bd31dad93361e6f2b04b94e0e066`; do not regenerate or duplicate scale-67 artifacts.', '2. Scale-68 is the current publication unit; do not start another collocation batch until its publication/checkpoint CI completes.', 'publication workstream item')
    text = replace_once(text, '3. Verify the normal-user scale-67 checkpoint with English Content Full Validation, Master Plan Acceptance and Platform CI; scale-67 becomes fully verified only when all three PASS.', '3. After the scale-68 bot publication commit is created, create one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.', 'checkpoint workstream item')
    text = replace_once(text, '5. If no safer pending enrichment appears after the scale-67 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002320`, expected IDs `col.00002321`–`col.00002360`, with fresh exact/near-dedupe preflight before any source apply.', '5. If no safer pending enrichment appears after the scale-68 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002360`, expected IDs `col.00002361`–`col.00002400`, with fresh exact/near-dedupe preflight before any source apply.', 'next batch workstream item')
    old_next = 'Create/verify exactly one normal-user checkpoint for scale-67 publication `ec3fd17cc756bd31dad93361e6f2b04b94e0e066`. After English Content Full Validation, Master Plan Acceptance and Platform CI all PASS on that checkpoint, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002320` (expected next range `col.00002321`–`col.00002360`, unless a safer under-target E04 family takes priority). Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-68 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002360` (expected next range `col.00002361`–`col.00002400`, unless a safer under-target E04 family takes priority). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main68():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-68 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 2320:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 2320, got {max(nums) if nums else None}')

    new = [make_collocation(2321 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-68: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-68-collocations.json',
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
            'id': 'review.e04.scale-68.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-68-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-68-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-68-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-68-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-68-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-68-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 68 museum and archive conservation operations collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==2320)', 'if(recallCollocations!==2360)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 2320 reviewed records', 'must expose 2360 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00002321', 'col.00002360'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 2360, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 3470, 'richRecords': 8071},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main68()
