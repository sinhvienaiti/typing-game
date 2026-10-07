#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-65.py'), run_name='e04_scale66_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-66-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-66.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-66'
REVIEWED_AT = '2026-10-07T15:35:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-66'
EXPECTED = {'collocations': 2240, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('inspect collection storage conditions', 'verb + noun phrase', 'kiểm tra điều kiện kho lưu trữ bộ sưu tập để phát hiện các yếu tố môi trường hoặc vận hành có thể gây hại cho hiện vật', 'B2'),
    ('monitor gallery temperature stability', 'verb + noun phrase', 'theo dõi độ ổn định nhiệt độ trong phòng trưng bày để hạn chế co giãn và suy thoái vật liệu', 'B2'),
    ('monitor gallery relative humidity', 'verb + noun phrase', 'theo dõi độ ẩm tương đối trong phòng trưng bày để bảo vệ vật liệu nhạy cảm với dao động ẩm', 'B2'),
    ('calibrate environmental data loggers', 'verb + noun phrase', 'hiệu chuẩn thiết bị ghi dữ liệu môi trường để bảo đảm số liệu nhiệt độ và độ ẩm có độ tin cậy phù hợp', 'C1'),
    ('review microclimate sensor readings', 'verb + noun phrase', 'xem xét số đo cảm biến vi khí hậu để nhận biết xu hướng bất thường bên trong tủ trưng bày hoặc vùng lưu trữ', 'C1'),
    ('adjust display case humidity', 'verb + noun phrase', 'điều chỉnh độ ẩm bên trong tủ trưng bày để phù hợp với yêu cầu bảo quản của hiện vật', 'B2'),
    ('replace saturated silica gel', 'verb + adjective + noun', 'thay silica gel đã bão hòa để khôi phục khả năng đệm ẩm trong tủ hoặc hộp bảo quản', 'B2'),
    ('condition silica gel packs', 'verb + noun phrase', 'điều hòa các gói silica gel đến mức ẩm mục tiêu trước khi sử dụng cho kiểm soát vi khí hậu', 'C1'),
    ('inspect artifact surface changes', 'verb + noun phrase', 'kiểm tra thay đổi trên bề mặt hiện vật như nứt, bong, đổi màu hoặc ăn mòn để phát hiện suy thoái sớm', 'B2'),
    ('document conservation condition findings', 'verb + noun phrase', 'ghi chép các phát hiện về tình trạng bảo quản bằng mô tả và bằng chứng nhất quán để theo dõi thay đổi theo thời gian', 'C1'),
    ('photograph treatment progress stages', 'verb + noun phrase', 'chụp ảnh các giai đoạn xử lý bảo tồn để tạo hồ sơ trực quan trước, trong và sau can thiệp', 'B2'),
    ('prepare object condition reports', 'verb + noun phrase', 'lập báo cáo tình trạng hiện vật trước trưng bày, vận chuyển hoặc xử lý để ghi nhận rủi ro và hư hỏng hiện có', 'B2'),
    ('handle artifacts with supports', 'verb + noun phrase', 'thao tác hiện vật với giá đỡ phù hợp để phân bố tải và tránh gây ứng suất lên phần yếu', 'B2'),
    ('move oversized collection objects', 'verb + noun phrase', 'di chuyển hiện vật bộ sưu tập kích thước lớn bằng kế hoạch nâng đỡ và lộ trình bảo đảm an toàn cho người và hiện vật', 'B2'),
    ('pad object transport crates', 'verb + noun phrase', 'lót đệm thùng vận chuyển hiện vật để giảm rung, va chạm và điểm chịu lực trong quá trình di chuyển', 'B2'),
    ('secure objects inside crates', 'verb + noun phrase', 'cố định hiện vật bên trong thùng vận chuyển để ngăn dịch chuyển mà không tạo áp lực gây hư hỏng', 'B2'),
    ('acclimatize objects before unpacking', 'verb + noun phrase', 'cho hiện vật thích nghi với môi trường mới trước khi mở kiện để giảm nguy cơ ngưng tụ và sốc nhiệt ẩm', 'C1'),
    ('quarantine incoming collection materials', 'verb + noun phrase', 'cách ly vật liệu bộ sưu tập mới tiếp nhận để kiểm tra sâu hại hoặc nguy cơ lây nhiễm trước khi nhập kho chính', 'C1'),
    ('inspect objects for pest activity', 'verb + noun phrase', 'kiểm tra hiện vật để tìm dấu hiệu hoạt động của côn trùng hoặc sinh vật gây hại như phân, lỗ thoát hoặc xác côn trùng', 'B2'),
    ('deploy insect monitoring traps', 'verb + noun phrase', 'bố trí bẫy giám sát côn trùng tại các vị trí phù hợp để theo dõi hoạt động sâu hại trong bảo tàng', 'B2'),
    ('identify museum pest specimens', 'verb + noun phrase', 'nhận dạng mẫu sinh vật gây hại trong bảo tàng để lựa chọn biện pháp kiểm soát phù hợp với loài và mức rủi ro', 'C1'),
    ('isolate infested collection objects', 'verb + noun phrase', 'cách ly hiện vật bị nhiễm sâu hại để ngăn lây lan sang các vật liệu bộ sưu tập khác', 'B2'),
    ('freeze pest-affected materials', 'verb + noun phrase', 'xử lý đông lạnh vật liệu bị sâu hại theo chu trình phù hợp để tiêu diệt côn trùng mà hạn chế rủi ro cho hiện vật', 'C1'),
    ('clean archival storage shelving', 'verb + noun phrase', 'làm sạch giá kệ lưu trữ lưu trữ học để loại bụi và nguồn thức ăn cho sâu hại mà không làm nhiễm bẩn hiện vật', 'B2'),
    ('vacuum collection storage areas', 'verb + noun phrase', 'hút bụi khu vực kho bộ sưu tập bằng phương pháp phù hợp để giảm bụi, mảnh vụn và nguy cơ sâu hại', 'B2'),
    ('filter particulate air pollution', 'verb + noun phrase', 'lọc ô nhiễm hạt trong không khí để giảm bụi và hạt có thể bám hoặc phản ứng với bề mặt hiện vật', 'C1'),
    ('limit ultraviolet light exposure', 'verb + noun phrase', 'giới hạn tiếp xúc tia cực tím để giảm phai màu và suy thoái quang hóa ở vật liệu nhạy sáng', 'B2'),
    ('measure gallery illuminance levels', 'verb + noun phrase', 'đo mức độ rọi trong phòng trưng bày để xác nhận ánh sáng nằm trong giới hạn phù hợp với hiện vật', 'B2'),
    ('rotate light-sensitive exhibits', 'verb + noun phrase', 'luân phiên hiện vật nhạy sáng để kiểm soát tổng liều chiếu sáng và giảm tích lũy hư hại', 'C1'),
    ('fit ultraviolet filtering films', 'verb + noun phrase', 'lắp phim lọc tia cực tím lên nguồn sáng hoặc bề mặt kính thích hợp để giảm bức xạ gây hại', 'B2'),
    ('prepare reversible conservation adhesives', 'verb + noun phrase', 'chuẩn bị chất kết dính bảo tồn có khả năng đảo ngược để hỗ trợ can thiệp có thể tháo bỏ trong tương lai', 'C1'),
    ('test cleaning solvent compatibility', 'verb + noun phrase', 'kiểm tra độ tương thích của dung môi làm sạch trên vùng thử nhỏ để tránh hòa tan màu, lớp phủ hoặc vật liệu gốc', 'C1'),
    ('consolidate fragile painted surfaces', 'verb + noun phrase', 'gia cố bề mặt sơn mong manh bằng vật liệu và kỹ thuật phù hợp để giảm nguy cơ mất lớp màu', 'C1'),
    ('stabilize flaking paint layers', 'verb + noun phrase', 'ổn định các lớp sơn đang bong để ngăn mảnh màu tiếp tục tách khỏi nền trước khi xử lý sâu hơn', 'C1'),
    ('support weakened textile fibers', 'verb + noun phrase', 'nâng đỡ sợi dệt suy yếu bằng vật liệu hỗ trợ tương thích để giảm ứng suất cơ học khi trưng bày hoặc lưu trữ', 'C1'),
    ('humidify distorted paper safely', 'verb + noun phrase', 'làm ẩm giấy bị biến dạng một cách có kiểm soát để tăng tính mềm dẻo trước khi làm phẳng mà không gây ố hoặc chảy mực', 'C1'),
    ('flatten creased archival documents', 'verb + noun phrase', 'làm phẳng tài liệu lưu trữ bị gấp nếp bằng kỹ thuật phù hợp để cải thiện khả năng sử dụng mà không làm yếu giấy', 'C1'),
    ('house photographs in enclosures', 'verb + noun phrase', 'đặt ảnh trong bao bì bảo quản đạt yêu cầu để giảm tiếp xúc với bụi, chất ô nhiễm và thao tác trực tiếp', 'B2'),
    ('label archival boxes safely', 'verb + noun phrase', 'ghi nhãn hộp lưu trữ bằng phương pháp an toàn để duy trì nhận dạng mà không đưa vật liệu có hại vào gần hiện vật', 'B2'),
    ('record object location changes', 'verb + noun phrase', 'ghi nhận thay đổi vị trí hiện vật trong hệ thống quản lý bộ sưu tập để duy trì khả năng truy vết và kiểm kê chính xác', 'B2'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-66-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v66'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-66-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-65 publication: `88a3ecc183bce638542d63046f9a3c8123158657` — scale-64 publication state verified by English Content Master Plan Acceptance #168, English Content Full Validation #148 and Platform CI #1257; published output: `cef8463d5e24b1f28eb5ae723cfdfd5320485f0a`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-66 publication: `8e30942991d843bdf1e88b9c541c6a165d3d6ae5` — scale-65 publication state verified by English Content Master Plan Acceptance #171, English Content Full Validation #150 and Platform CI #1272; published output: `830d3520a705fd1c43c0187d3568eb041e6c4e76`.',
        'verified scale-65 checkpoint',
    )
    text = replace_once(
        text,
        '- Scale-65 publication completed at `830d3520a705fd1c43c0187d3568eb041e6c4e76`; bot-triggered PR workflows follow the known `action_required` publication pattern, so this normal-user checkpoint exists to verify the published state before opening scale-66.',
        '- Scale-65 publication checkpoint `8e30942991d843bdf1e88b9c541c6a165d3d6ae5` is fully verified; scale-66 is the current publication unit.',
        'scale-65 verification state',
    )
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,350 published records after scale-65', '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,390 published records after scale-66', 'E04 publication count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-65 publication', '## Published runtime snapshot after E04 scale-66 publication', 'runtime snapshot heading')
    text = replace_once(text, '- phrases: 3,350 records', '- phrases: 3,390 records', 'phrase runtime count')
    text = replace_once(text, '- total published rich records: 7,951', '- total published rich records: 7,991', 'rich runtime count')
    text = replace_once(text, '- editorial ledger: 7,951 decisions / 7,951 applied / 7,951 publish decisions', '- editorial ledger: 7,991 decisions / 7,991 applied / 7,991 publish decisions', 'editorial ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00002240`', '- E04 collocation frontier: `col.00002280`', 'collocation frontier')
    text = replace_once(text, '1. Scale-64 publication is fully verified at `88a3ecc183bce638542d63046f9a3c8123158657`; do not duplicate scale-64 artifacts.', '1. Scale-65 publication is fully verified at `8e30942991d843bdf1e88b9c541c6a165d3d6ae5`; do not duplicate scale-65 artifacts.', 'verified workstream item')
    text = replace_once(text, '2. Scale-65 publication completed at `830d3520a705fd1c43c0187d3568eb041e6c4e76`; the current gate is normal-user checkpoint verification, not regeneration.', '2. Scale-66 is the current publication unit; do not start another collocation batch until its publication/checkpoint CI completes.', 'publication workstream item')
    text = replace_once(text, '3. Verify English Content Full Validation, English Content Master Plan Acceptance and Platform CI on this checkpoint. Only when all three PASS is scale-65 fully verified.', '3. After the scale-66 bot publication commit is created, create one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.', 'checkpoint workstream item')
    text = replace_once(text, '5. If no safer pending enrichment appears after the scale-65 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002240`, with fresh exact/near-dedupe preflight before any source apply.', '5. If no safer pending enrichment appears after the scale-66 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002280`, with fresh exact/near-dedupe preflight before any source apply.', 'next batch workstream item')
    old_next = 'Verify scale-65 publication `830d3520a705fd1c43c0187d3568eb041e6c4e76` under the normal-user checkpoint. If English Content Full Validation, Master Plan Acceptance and Platform CI all PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002240` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-66 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002280` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main66():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-66 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 2240:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 2240, got {max(nums) if nums else None}')

    new = [make_collocation(2241 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-66: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-66-collocations.json',
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
            'id': 'review.e04.scale-66.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-66-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-66-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-66-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-66-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-66-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-66-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 66 museum collection conservation collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==2240)', 'if(recallCollocations!==2280)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 2240 reviewed records', 'must expose 2280 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00002241', 'col.00002280'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 2280, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 3390, 'richRecords': 7991},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main66()
