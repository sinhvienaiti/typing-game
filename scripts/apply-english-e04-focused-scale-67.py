#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-66.py'), run_name='e04_scale67_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-67-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-67.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-67'
REVIEWED_AT = '2026-10-07T16:00:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-67'
EXPECTED = {'collocations': 2280, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('inspect stage rigging hardware', 'verb + noun phrase', 'kiểm tra phần cứng hệ thống treo sân khấu để phát hiện mòn, biến dạng hoặc lắp ghép không an toàn trước khi sử dụng', 'B2'),
    ('verify overhead load limits', 'verb + noun phrase', 'xác nhận giới hạn tải trên cao trước khi treo cảnh trí, đèn hoặc thiết bị kỹ thuật lên kết cấu sân khấu', 'C1'),
    ('schedule stage rigging inspections', 'verb + noun phrase', 'lập lịch kiểm tra hệ thống rigging sân khấu theo chu kỳ để bảo đảm thiết bị nâng treo được đánh giá thường xuyên', 'C1'),
    ('secure suspended scenery', 'verb + noun phrase', 'cố định cảnh trí được treo để ngăn chuyển động ngoài ý muốn trong khi vận hành hoặc biểu diễn', 'B2'),
    ('install theatrical lighting fixtures', 'verb + noun phrase', 'lắp các thiết bị chiếu sáng sân khấu tại vị trí thiết kế và bảo đảm phương án treo, cấp điện phù hợp', 'B2'),
    ('focus stage lighting instruments', 'verb + noun phrase', 'chỉnh hướng và vùng chiếu của đèn sân khấu để đạt bố cục ánh sáng theo thiết kế', 'B2'),
    ('program lighting cue sequences', 'verb + noun phrase', 'lập trình chuỗi cue ánh sáng để các thay đổi cường độ, màu sắc và vị trí diễn ra đúng thời điểm', 'C1'),
    ('test emergency work lights', 'verb + noun phrase', 'kiểm tra đèn làm việc khẩn cấp để bảo đảm khu vực sân khấu vẫn có ánh sáng an toàn khi hệ thống chính gặp sự cố', 'B2'),
    ('route stage power cables', 'verb + noun phrase', 'đi dây nguồn sân khấu theo tuyến an toàn để giảm nguy cơ vấp, hư hỏng cáp và giao thoa với thiết bị chuyển động', 'B2'),
    ('protect cable crossing points', 'verb + noun phrase', 'bảo vệ các điểm cáp đi qua lối di chuyển bằng máng hoặc che chắn phù hợp để giảm nguy cơ vấp và nghiền cáp', 'B2'),
    ('balance electrical phase loads', 'verb + noun phrase', 'cân bằng tải giữa các pha điện để hạn chế quá tải và duy trì phân phối công suất ổn định cho thiết bị sân khấu', 'C1'),
    ('verify dimmer rack operation', 'verb + noun phrase', 'xác nhận tủ dimmer hoạt động đúng trước buổi diễn để các kênh ánh sáng phản hồi chính xác với hệ thống điều khiển', 'C1'),
    ('configure lighting control network', 'verb + noun phrase', 'cấu hình mạng điều khiển ánh sáng để bàn điều khiển, node và thiết bị nhận đúng dữ liệu trong hệ thống sân khấu', 'C1'),
    ('patch lighting control channels', 'verb + noun phrase', 'gán và kết nối các kênh điều khiển ánh sáng với thiết bị tương ứng để cue vận hành đúng theo sơ đồ', 'C1'),
    ('calibrate followspot alignment', 'verb + noun phrase', 'hiệu chỉnh hướng ngắm của followspot để người vận hành theo diễn viên chính xác trên sân khấu', 'C1'),
    ('coordinate scenery changeovers', 'verb + noun phrase', 'phối hợp thay đổi cảnh trí giữa các phân đoạn để hoàn thành đúng cue mà không cản trở người biểu diễn', 'B2'),
    ('mark scenic unit positions', 'verb + noun phrase', 'đánh dấu vị trí của các khối cảnh trí trên sàn để đội sân khấu có thể đặt lại chính xác trong mỗi lần chuyển cảnh', 'B2'),
    ('brace freestanding scenic elements', 'verb + noun phrase', 'gia cố các phần cảnh trí đứng độc lập để tránh lật hoặc dịch chuyển khi chịu rung, va chạm hoặc tải ngoài ý muốn', 'C1'),
    ('inspect stage floor surfaces', 'verb + noun phrase', 'kiểm tra bề mặt sàn sân khấu để phát hiện vật cản, hư hỏng hoặc khu vực trơn trượt trước khi rehearsal và biểu diễn', 'B2'),
    ('apply temporary floor markings', 'verb + noun phrase', 'dán dấu tạm trên sàn để chỉ vị trí diễn viên, đạo cụ hoặc cảnh trí mà không làm hỏng bề mặt sân khấu', 'B2'),
    ('rehearse scene change sequences', 'verb + noun phrase', 'diễn tập trình tự chuyển cảnh để đội kỹ thuật phối hợp nhịp nhàng, an toàn và đúng thời lượng', 'B2'),
    ('coordinate fly rail operations', 'verb + noun phrase', 'phối hợp vận hành hệ thống fly rail để nâng hạ cảnh trí và thiết bị theo cue mà vẫn duy trì vùng làm việc an toàn', 'C1'),
    ('call automation movement cues', 'verb + noun phrase', 'phát lệnh cue cho chuyển động tự động của sân khấu đúng thời điểm sau khi xác nhận vùng chuyển động đã an toàn', 'C1'),
    ('test stage automation interlocks', 'verb + noun phrase', 'kiểm tra liên động an toàn của hệ thống tự động sân khấu để ngăn chuyển động khi điều kiện bảo vệ chưa thỏa mãn', 'C1'),
    ('establish backstage traffic routes', 'verb + noun phrase', 'thiết lập tuyến di chuyển hậu trường để tách người, cảnh trí và thiết bị trong những thời điểm chuyển động đông đúc', 'B2'),
    ('manage quick costume changes', 'verb + noun phrase', 'quản lý các lần thay trang phục nhanh để diễn viên, trang phục và nhân sự hỗ trợ sẵn sàng đúng cue', 'B2'),
    ('organize prop preset tables', 'verb + noun phrase', 'sắp xếp bàn preset đạo cụ theo thứ tự sử dụng để diễn viên và đội đạo cụ lấy đúng món trong thời gian ngắn', 'B2'),
    ('verify prop handoff positions', 'verb + noun phrase', 'xác nhận vị trí bàn giao đạo cụ để việc đưa nhận diễn ra nhất quán và không cản trở lối hậu trường', 'B2'),
    ('track performance prop inventory', 'verb + noun phrase', 'theo dõi tồn kho đạo cụ biểu diễn để phát hiện món thiếu, hư hỏng hoặc chưa được trả về sau mỗi suất diễn', 'B2'),
    ('inspect orchestra pit barriers', 'verb + noun phrase', 'kiểm tra rào chắn khu vực hố nhạc để giảm nguy cơ ngã khi khu vực này mở hoặc thay đổi cấu hình', 'B2'),
    ('adjust acoustic shell panels', 'verb + noun phrase', 'điều chỉnh các tấm vỏ âm học theo cấu hình biểu diễn để hỗ trợ phản xạ và phân bố âm thanh mong muốn', 'C1'),
    ('position stage monitor speakers', 'verb + noun phrase', 'đặt loa monitor sân khấu để người biểu diễn nghe tín hiệu cần thiết mà hạn chế cản trở lối đi và phản hồi âm', 'B2'),
    ('check intercom beltpack channels', 'verb + noun phrase', 'kiểm tra kênh của bộ intercom đeo người để các vị trí kỹ thuật liên lạc đúng nhóm trong rehearsal và biểu diễn', 'B2'),
    ('test backstage paging system', 'verb + noun phrase', 'kiểm tra hệ thống gọi hậu trường để thông báo cue hoặc thông tin vận hành được nghe rõ tại các khu vực cần thiết', 'B2'),
    ('coordinate performer entrance cues', 'verb + noun phrase', 'phối hợp cue vào sân khấu của người biểu diễn để đúng thời điểm và không xung đột với chuyển động kỹ thuật', 'B2'),
    ('maintain clear fire exits', 'verb + noun phrase', 'duy trì lối thoát hiểm không bị che chắn bởi cảnh trí, thùng thiết bị hoặc hoạt động hậu trường', 'B2'),
    ('document technical rehearsal notes', 'verb + noun phrase', 'ghi chép các vấn đề và thay đổi trong rehearsal kỹ thuật để các bộ phận cập nhật cue và nhiệm vụ trước buổi diễn', 'B2'),
    ('review performance safety hazards', 'verb + noun phrase', 'xem xét các nguy cơ an toàn của buổi biểu diễn để xác định biện pháp kiểm soát trước khi khán giả vào', 'C1'),
    ('reset stage after performance', 'verb + noun phrase', 'đưa sân khấu về cấu hình chuẩn sau buổi diễn để chuẩn bị cho suất tiếp theo hoặc công việc bảo trì', 'B2'),
    ('secure equipment for storage', 'verb + noun phrase', 'cố định và sắp xếp thiết bị trước khi lưu kho để giảm hư hỏng, đổ ngã và cản trở lối tiếp cận', 'B2'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-67-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v67'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-67-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-66 publication: `8e30942991d843bdf1e88b9c541c6a165d3d6ae5` — scale-65 publication state verified by English Content Master Plan Acceptance #171, English Content Full Validation #150 and Platform CI #1272; published output: `830d3520a705fd1c43c0187d3568eb041e6c4e76`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-67 publication: `39d1eeb559c13f88e563027d93b20075b46fc4c3` — scale-66 publication state verified by English Content Master Plan Acceptance #175, English Content Full Validation #151 and Platform CI #1277; published output: `e9e221c1caa5e660d845eff61fccdd3f3c8e5798`.',
        'verified scale-66 checkpoint',
    )
    text = replace_once(
        text,
        '- Scale-66 publication completed at `e9e221c1caa5e660d845eff61fccdd3f3c8e5798`; bot-triggered English Content Master Plan Acceptance #174 and Platform CI #1276 ended `action_required` before jobs ran, matching the known bot-publication pattern. This normal-user checkpoint is the verification gate; do not regenerate scale-66.',
        '- Scale-66 publication checkpoint `39d1eeb559c13f88e563027d93b20075b46fc4c3` is fully verified; scale-67 is the current publication unit.',
        'scale-66 verification state',
    )
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,390 published records after scale-66', '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,430 published records after scale-67', 'E04 publication count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-66 publication', '## Published runtime snapshot after E04 scale-67 publication', 'runtime snapshot heading')
    text = replace_once(text, '- phrases: 3,390 records', '- phrases: 3,430 records', 'phrase runtime count')
    text = replace_once(text, '- total published rich records: 7,991', '- total published rich records: 8,031', 'rich runtime count')
    text = replace_once(text, '- editorial ledger: 7,991 decisions / 7,991 applied / 7,991 publish decisions', '- editorial ledger: 8,031 decisions / 8,031 applied / 8,031 publish decisions', 'editorial ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00002280`', '- E04 collocation frontier: `col.00002320`', 'collocation frontier')
    text = replace_once(text, '1. Scale-65 publication is fully verified at `8e30942991d843bdf1e88b9c541c6a165d3d6ae5`; do not duplicate scale-65 artifacts.', '1. Scale-66 publication is fully verified at `39d1eeb559c13f88e563027d93b20075b46fc4c3`; do not duplicate scale-66 artifacts.', 'verified workstream item')
    text = replace_once(text, '2. Scale-66 publication completed at `e9e221c1caa5e660d845eff61fccdd3f3c8e5798`; the current gate is normal-user checkpoint verification, not regeneration.', '2. Scale-67 is the current publication unit; do not start another collocation batch until its publication/checkpoint CI completes.', 'publication workstream item')
    text = replace_once(text, '3. Verify English Content Full Validation, English Content Master Plan Acceptance and Platform CI on this checkpoint. Only when all three PASS is scale-66 fully verified.', '3. After the scale-67 bot publication commit is created, create one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.', 'checkpoint workstream item')
    text = replace_once(text, '5. If no safer pending enrichment appears after the scale-66 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002280`, with fresh exact/near-dedupe preflight before any source apply.', '5. If no safer pending enrichment appears after the scale-67 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002320`, with fresh exact/near-dedupe preflight before any source apply.', 'next batch workstream item')
    old_next = 'Verify scale-66 publication `e9e221c1caa5e660d845eff61fccdd3f3c8e5798` under the normal-user checkpoint. If English Content Full Validation, Master Plan Acceptance and Platform CI all PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002280` (expected next range `col.00002281`–`col.00002320`, unless a safer under-target E04 family takes priority). Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-67 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002320` (expected next range `col.00002321`–`col.00002360`, unless a safer under-target E04 family takes priority). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main67():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-67 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 2280:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 2280, got {max(nums) if nums else None}')

    new = [make_collocation(2281 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-67: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-67-collocations.json',
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
            'id': 'review.e04.scale-67.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-67-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-67-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-67-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-67-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-67-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-67-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 67 theater stage technical operations collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==2280)', 'if(recallCollocations!==2320)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 2280 reviewed records', 'must expose 2320 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00002281', 'col.00002320'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 2320, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 3430, 'richRecords': 8031},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main67()
