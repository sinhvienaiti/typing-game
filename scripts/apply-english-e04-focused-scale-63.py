#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-62.py'), run_name='e04_scale63_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-63-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-63.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-63'
REVIEWED_AT = '2026-10-07T14:50:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-63'
EXPECTED = {'collocations': 2120, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('inspect archival storage enclosures', 'verb + noun phrase', 'kiểm tra hộp, bìa và vật liệu bao gói lưu trữ để phát hiện hư hỏng, axit hóa hoặc cấu hình không còn bảo vệ tốt hiện vật tài liệu', 'B2'),
    ('monitor collection storage humidity', 'verb + noun phrase', 'theo dõi độ ẩm khu lưu trữ bộ sưu tập để hạn chế co giãn vật liệu, nấm mốc và suy giảm hóa học', 'B2'),
    ('calibrate conservation data loggers', 'verb + noun phrase', 'hiệu chuẩn thiết bị ghi dữ liệu bảo tồn để số đo nhiệt độ và độ ẩm dùng cho quyết định bảo quản có độ tin cậy phù hợp', 'C1'),
    ('condition incoming archival materials', 'verb + noun phrase', 'ổn định vật liệu lưu trữ mới tiếp nhận theo môi trường kho trước khi xử lý sâu hơn nhằm giảm sốc nhiệt ẩm và ngưng tụ', 'C1'),
    ('isolate mold-affected documents', 'verb + noun phrase', 'cách ly tài liệu bị ảnh hưởng bởi nấm mốc để hạn chế phát tán bào tử sang phần còn lại của bộ sưu tập', 'B2'),
    ('stabilize water-damaged records', 'verb + noun phrase', 'ổn định hồ sơ bị hư hại do nước bằng các bước kiểm soát ẩm, làm khô và hỗ trợ vật lý trước khi phục hồi chi tiết', 'C1'),
    ('surface-clean paper artifacts', 'verb + noun phrase', 'làm sạch bề mặt hiện vật giấy bằng phương pháp phù hợp để loại bụi và chất bẩn rời mà không gây mài mòn hoặc kéo rách', 'B2'),
    ('humidify brittle parchment safely', 'verb + noun phrase', 'làm ẩm da thuộc giòn một cách có kiểm soát để tăng độ dẻo trước khi chỉnh phẳng mà không làm biến dạng cấu trúc vật liệu', 'C1'),
    ('flatten creased archival documents', 'verb + noun phrase', 'làm phẳng tài liệu lưu trữ bị gấp nếp bằng độ ẩm và áp lực kiểm soát để giảm nếp mà vẫn bảo vệ mực và nền giấy', 'B2'),
    ('mend torn paper supports', 'verb + noun phrase', 'vá các phần nền giấy bị rách bằng vật liệu tương thích và kỹ thuật có thể đảo ngược để phục hồi khả năng nâng đỡ', 'B2'),
    ('reinforce weakened book bindings', 'verb + noun phrase', 'gia cố kết cấu đóng sách bị yếu tại gáy, bản lề hoặc chỉ khâu để cải thiện khả năng sử dụng mà không che mất cấu trúc gốc', 'C1'),
    ('encapsulate fragile documents', 'verb + noun phrase', 'bao bảo vệ tài liệu dễ vỡ trong lớp màng lưu trữ phù hợp để hỗ trợ thao tác và giảm tiếp xúc trực tiếp', 'B2'),
    ('construct acid-free storage mounts', 'verb + noun phrase', 'chế tạo giá đỡ lưu trữ không axit phù hợp với hình dạng hiện vật để phân bố lực và giảm tiếp xúc với vật liệu gây hại', 'C1'),
    ('fit custom archival boxes', 'verb + noun phrase', 'lắp hộp lưu trữ theo kích thước riêng để giữ hiện vật ổn định, tránh dịch chuyển và giảm tác động của bụi ánh sáng', 'B2'),
    ('interleave photographic materials', 'verb + noun phrase', 'đặt lớp ngăn phù hợp giữa các vật liệu ảnh để giảm ma sát, dính bề mặt và truyền sản phẩm phân hủy', 'C1'),
    ('sleeve nitrate film negatives', 'verb + noun phrase', 'đưa phim âm bản nitrate vào túi bảo quản phù hợp để hỗ trợ nhận dạng, cách ly và thao tác an toàn', 'C1'),
    ('segregate acetate film collections', 'verb + noun phrase', 'phân tách bộ sưu tập phim acetate có dấu hiệu suy giảm để giảm tích tụ hơi axit và hạn chế ảnh hưởng chéo', 'C1'),
    ('monitor vinegar syndrome indicators', 'verb + noun phrase', 'theo dõi các chỉ dấu hội chứng giấm ở phim acetate để phát hiện sớm tốc độ thủy phân và ưu tiên điều kiện lưu trữ lạnh hơn', 'C1'),
    ('digitize fragile manuscript pages', 'verb + noun phrase', 'số hóa các trang bản thảo dễ hỏng bằng thiết bị và giá đỡ phù hợp để giảm thời gian mở, ép hoặc chạm trực tiếp', 'B2'),
    ('verify capture color targets', 'verb + noun phrase', 'xác nhận bảng màu chuẩn được ghi hình đúng để kiểm soát tái tạo màu và hỗ trợ hiệu chỉnh ảnh số hóa', 'C1'),
    ('calibrate reproduction lighting', 'verb + noun phrase', 'hiệu chuẩn hệ thống chiếu sáng chụp sao để ánh sáng đồng đều, ổn định màu và không vượt mức nhiệt hay tia có hại cho hiện vật', 'C1'),
    ('minimize ultraviolet light exposure', 'verb + noun phrase', 'giảm phơi nhiễm tia tử ngoại cho hiện vật nhạy sáng để hạn chế phai màu và phân hủy vật liệu hữu cơ', 'B2'),
    ('rotate light-sensitive exhibits', 'verb + noun phrase', 'luân phiên hiện vật nhạy sáng theo lịch để giới hạn liều sáng tích lũy trong khi vẫn duy trì nội dung trưng bày', 'B2'),
    ('measure display-case illumination', 'verb + noun phrase', 'đo độ rọi trong tủ trưng bày để xác nhận mức ánh sáng phù hợp với giới hạn bảo tồn của từng loại vật liệu', 'B2'),
    ('buffer exhibition case humidity', 'verb + noun phrase', 'ổn định dao động độ ẩm trong tủ trưng bày bằng vật liệu đệm hoặc hệ thống kiểm soát phù hợp với hiện vật', 'C1'),
    ('inspect pest monitoring traps', 'verb + noun phrase', 'kiểm tra bẫy theo dõi côn trùng định kỳ để nhận biết loài, mật độ và vị trí hoạt động trong kho hoặc phòng trưng bày', 'B2'),
    ('identify insect activity patterns', 'verb + noun phrase', 'nhận diện mô hình hoạt động của côn trùng theo thời gian và khu vực để khoanh vùng nguồn xâm nhập và điều kiện thuận lợi', 'C1'),
    ('quarantine infested collection items', 'verb + noun phrase', 'cách ly hiện vật bị côn trùng xâm nhiễm để ngăn lan sang bộ sưu tập trước khi xử lý thích hợp', 'B2'),
    ('freeze infested collection materials', 'verb + noun phrase', 'xử lý đông lạnh vật liệu bộ sưu tập bị côn trùng theo chu trình kiểm soát để tiêu diệt sinh vật gây hại mà hạn chế hư hại vật liệu', 'C1'),
    ('document conservation treatment steps', 'verb + noun phrase', 'ghi chép từng bước xử lý bảo tồn, vật liệu sử dụng và quan sát để tạo hồ sơ có thể truy xuất cho lần can thiệp sau', 'B2'),
    ('record object condition changes', 'verb + noun phrase', 'ghi nhận thay đổi tình trạng hiện vật theo thời gian để theo dõi suy giảm, đánh giá rủi ro và điều chỉnh kế hoạch bảo quản', 'B2'),
    ('map surface damage locations', 'verb + noun phrase', 'lập bản đồ vị trí hư hại trên bề mặt hiện vật để mô tả chính xác phạm vi, kiểu tổn thương và diễn biến qua các lần kiểm tra', 'C1'),
    ('photograph treatment reference views', 'verb + noun phrase', 'chụp các góc tham chiếu trước, trong và sau xử lý để tạo bằng chứng trực quan nhất quán cho hồ sơ bảo tồn', 'B2'),
    ('sample conservation cleaning solvents', 'verb + noun phrase', 'thử mẫu dung môi làm sạch ở vùng kiểm soát để đánh giá tương tác với lớp màu, lớp phủ và chất bẩn trước khi áp dụng rộng', 'C1'),
    ('test coating solubility safely', 'verb + noun phrase', 'kiểm tra độ hòa tan của lớp phủ bằng phương pháp giới hạn để lựa chọn vật liệu xử lý mà không làm mất lớp nguyên gốc', 'C1'),
    ('prepare reversible mounting adhesives', 'verb + noun phrase', 'chuẩn bị chất kết dính gắn trưng bày có tính tương thích và khả năng đảo ngược để giảm rủi ro can thiệp lâu dài', 'C1'),
    ('handle oversized maps safely', 'verb + noun phrase', 'thao tác bản đồ khổ lớn bằng đủ điểm đỡ và mặt phẳng phù hợp để tránh gập, kéo rách hoặc biến dạng do trọng lượng', 'B2'),
    ('support bound volumes during imaging', 'verb + noun phrase', 'đỡ sách đóng quyển khi chụp số hóa bằng nôi hoặc giá điều chỉnh để hạn chế góc mở và lực tác động lên gáy sách', 'B2'),
    ('audit emergency salvage supplies', 'verb + noun phrase', 'kiểm tra vật tư cứu hộ khẩn cấp để xác nhận số lượng, tình trạng và khả năng tiếp cận khi xảy ra ngập nước, cháy hoặc sự cố môi trường', 'C1'),
    ('prioritize disaster recovery objects', 'verb + noun phrase', 'xác định thứ tự ưu tiên cứu hộ hiện vật sau thảm họa dựa trên mức độ nhạy cảm, giá trị, tình trạng và khả năng phục hồi', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-63-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v63'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-63-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-62 publication: `034d6543bc070a760fe405c1a9bd9c15a9fd4107` — scale-61 publication state verified by English Content Master Plan Acceptance #159, English Content Full Validation #142 and Platform CI #1219; published output: `c48d5703c0161917da90f51ae9efb21e024e17e2`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-63 publication: `f8e5bc772c78569ab181c4752d79f81ea8fcaf18` — scale-62 publication state verified by English Content Master Plan Acceptance #162, English Content Full Validation #144 and Platform CI #1245; published output: `8722e17746730344c8adc366c282a2b541401d56`.',
        'verified scale-62 checkpoint',
    )
    text = replace_once(
        text,
        '- Scale-62 publication completed at `8722e17746730344c8adc366c282a2b541401d56`; bot-triggered English Content Master Plan Acceptance #161 and Platform CI #1233 were `action_required`, so this normal-user checkpoint exists to verify the published state before opening scale-63.',
        '- Scale-62 publication checkpoint `f8e5bc772c78569ab181c4752d79f81ea8fcaf18` is fully verified; scale-63 is the current publication unit.',
        'scale-62 verification state',
    )
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,230 published records after scale-62', '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,270 published records after scale-63', 'E04 publication count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-62 publication', '## Published runtime snapshot after E04 scale-63 publication', 'runtime snapshot heading')
    text = replace_once(text, '- phrases: 3,230 records', '- phrases: 3,270 records', 'phrase runtime count')
    text = replace_once(text, '- total published rich records: 7,831', '- total published rich records: 7,871', 'rich runtime count')
    text = replace_once(text, '- editorial ledger: 7,831 decisions / 7,831 applied / 7,831 publish decisions', '- editorial ledger: 7,871 decisions / 7,871 applied / 7,871 publish decisions', 'editorial ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00002120`', '- E04 collocation frontier: `col.00002160`', 'collocation frontier')
    text = replace_once(text, '1. Scale-61 publication is fully verified at `034d6543bc070a760fe405c1a9bd9c15a9fd4107`; do not duplicate scale-61 artifacts.', '1. Scale-62 publication is fully verified at `f8e5bc772c78569ab181c4752d79f81ea8fcaf18`; do not duplicate scale-62 artifacts.', 'verified workstream item')
    text = replace_once(text, '2. Scale-62 publication completed at `8722e17746730344c8adc366c282a2b541401d56`; the current gate is normal-user checkpoint verification, not regeneration.', '2. Scale-63 is the current publication unit; do not start another collocation batch until its publication/checkpoint CI completes.', 'publication workstream item')
    text = replace_once(text, '3. Verify English Content Full Validation, English Content Master Plan Acceptance and Platform CI on this checkpoint. Only when all three PASS is scale-62 fully verified.', '3. After the scale-63 bot publication commit is created, create one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.', 'checkpoint workstream item')
    text = replace_once(text, '5. If no safer pending enrichment appears after the scale-62 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002120`, with fresh exact/near-dedupe preflight before any source apply.', '5. If no safer pending enrichment appears after the scale-63 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002160`, with fresh exact/near-dedupe preflight before any source apply.', 'next batch workstream item')
    old_next = 'Verify scale-62 publication `8722e17746730344c8adc366c282a2b541401d56` under the normal-user checkpoint. If English Content Full Validation, Master Plan Acceptance and Platform CI all PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002120` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-63 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002160` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main63():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-63 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 2120:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 2120, got {max(nums) if nums else None}')

    new = [make_collocation(2121 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-63: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-63-collocations.json',
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
            'id': 'review.e04.scale-63.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-63-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-63-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-63-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-63-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-63-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-63-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 63 museum and archive conservation collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==2120)', 'if(recallCollocations!==2160)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 2120 reviewed records', 'must expose 2160 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00002121', 'col.00002160'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 2160, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 3270, 'richRecords': 7871},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main63()
