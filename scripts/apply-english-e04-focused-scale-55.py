#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-54.py'), run_name='e04_scale55_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-55-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-55.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-55'
REVIEWED_AT = '2026-10-07T11:20:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-55'
EXPECTED = {'collocations': 1800, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('monitor wafer fabrication yields', 'verb + noun phrase', 'theo dõi tỷ lệ sản phẩm đạt yêu cầu trong quá trình chế tạo wafer để phát hiện sớm suy giảm hiệu suất công nghệ', 'C1'),
    ('calibrate lithography exposure systems', 'verb + noun phrase', 'hiệu chuẩn hệ thống phơi quang khắc để duy trì liều chiếu, tiêu cự và độ chính xác mẫu theo yêu cầu', 'C1'),
    ('align photomask pattern layers', 'verb + noun phrase', 'căn chỉnh các lớp mẫu photomask để các cấu trúc trên nhiều lớp wafer chồng khớp trong giới hạn sai số cho phép', 'C1'),
    ('coat wafers with photoresist', 'verb + noun phrase', 'phủ lớp cản quang lên wafer với độ dày và độ đồng đều phù hợp trước bước phơi quang', 'B2'),
    ('develop exposed resist patterns', 'verb + adjective + noun', 'hiện ảnh các mẫu cản quang đã phơi để tạo cấu trúc dùng cho bước khắc hoặc xử lý tiếp theo', 'C1'),
    ('etch nanoscale circuit features', 'verb + adjective + noun', 'khắc các đặc trưng mạch kích thước nano theo hình dạng và chiều sâu yêu cầu của quy trình', 'C1'),
    ('deposit thin dielectric films', 'verb + adjective + noun', 'lắng đọng các màng điện môi mỏng với thành phần, độ dày và độ đồng đều được kiểm soát', 'C1'),
    ('implant dopant ions precisely', 'verb + noun phrase', 'cấy ion pha tạp một cách chính xác để tạo nồng độ và độ sâu vùng bán dẫn theo thiết kế', 'C1'),
    ('anneal implanted semiconductor wafers', 'verb + adjective + noun', 'ủ nhiệt các wafer bán dẫn sau cấy ion để kích hoạt pha tạp và phục hồi tổn thương mạng tinh thể', 'C1'),
    ('measure critical dimension uniformity', 'verb + noun phrase', 'đo độ đồng đều của kích thước tới hạn trên wafer để đánh giá khả năng kiểm soát công nghệ', 'C1'),
    ('inspect wafer surface defects', 'verb + noun phrase', 'kiểm tra khuyết tật bề mặt wafer như hạt bụi, vết xước hoặc bất thường hình thái có thể ảnh hưởng đến năng suất', 'B2'),
    ('classify particle contamination events', 'verb + noun phrase', 'phân loại các sự kiện nhiễm hạt theo nguồn, mức độ và tác động để hỗ trợ điều tra nguyên nhân', 'C1'),
    ('control cleanroom humidity levels', 'verb + noun phrase', 'kiểm soát độ ẩm phòng sạch để hạn chế tĩnh điện, ngưng tụ và biến động nhạy cảm của quy trình', 'B2'),
    ('maintain ultrapure water systems', 'verb + adjective + noun', 'bảo trì hệ thống nước siêu tinh khiết dùng cho làm sạch wafer và các công đoạn sản xuất nhạy cảm', 'C1'),
    ('verify process chamber pressure', 'verb + noun phrase', 'xác nhận áp suất buồng xử lý nằm trong dải quy định trước và trong khi chạy quy trình', 'B2'),
    ('clean plasma etch chambers', 'verb + noun phrase', 'làm sạch buồng khắc plasma để loại bỏ cặn bám và giảm nguy cơ nhiễm chéo giữa các lô wafer', 'C1'),
    ('replace worn vacuum seals', 'verb + adjective + noun', 'thay các gioăng chân không đã mòn để ngăn rò rỉ và duy trì điều kiện áp suất ổn định', 'B2'),
    ('qualify new process recipes', 'verb + adjective + noun', 'thẩm định công thức quy trình mới bằng dữ liệu thử nghiệm trước khi cho phép sử dụng trong sản xuất', 'C1'),
    ('lock approved recipe parameters', 'verb + adjective + noun', 'khóa các tham số công thức đã được phê duyệt để ngăn thay đổi ngoài kiểm soát trong môi trường sản xuất', 'C1'),
    ('track wafer lot genealogy', 'verb + noun phrase', 'theo dõi lịch sử và quan hệ của từng lô wafer qua thiết bị, công đoạn, vật tư và lần xử lý', 'C1'),
    ('schedule bottleneck fabrication tools', 'verb + adjective + noun', 'lập lịch các thiết bị chế tạo đang là nút thắt để tối đa thông lượng và giảm thời gian chờ của lô', 'C1'),
    ('balance wafer starts across lines', 'verb + noun phrase', 'cân bằng số wafer bắt đầu sản xuất giữa các dây chuyền để phù hợp năng lực và nhu cầu đầu ra', 'C1'),
    ('prioritize hot lot processing', 'verb + noun phrase', 'ưu tiên xử lý các lô khẩn cấp theo quy tắc vận hành mà không gây mất kiểm soát dòng sản xuất chung', 'C1'),
    ('recover stalled production lots', 'verb + adjective + noun', 'khôi phục các lô sản xuất bị đình trệ bằng cách xử lý nguyên nhân, tái lập tuyến công nghệ và xác nhận điều kiện tiếp tục', 'C1'),
    ('monitor equipment utilization rates', 'verb + noun phrase', 'theo dõi tỷ lệ sử dụng thiết bị để nhận diện công suất nhàn rỗi, nút thắt và cơ hội cải thiện lịch sản xuất', 'B2'),
    ('reduce unplanned tool downtime', 'verb + adjective + noun', 'giảm thời gian dừng thiết bị ngoài kế hoạch bằng bảo trì, giám sát tình trạng và phản ứng sự cố hiệu quả hơn', 'C1'),
    ('perform preventive chamber maintenance', 'verb + adjective + noun', 'thực hiện bảo trì phòng ngừa cho buồng xử lý theo chu kỳ để giữ độ sạch và độ ổn định của thiết bị', 'B2'),
    ('analyze statistical process control charts', 'verb + adjective + noun', 'phân tích biểu đồ kiểm soát quá trình thống kê để nhận diện xu hướng, dịch chuyển và biến động bất thường', 'C1'),
    ('investigate out-of-control signals', 'verb + adjective + noun', 'điều tra các tín hiệu vượt kiểm soát để xác định nguyên nhân đặc biệt trước khi tiếp tục sản xuất', 'C1'),
    ('contain suspect wafer lots', 'verb + adjective + noun', 'cách ly các lô wafer nghi ngờ để ngăn chuyển tiếp tới công đoạn sau trước khi có quyết định chất lượng', 'C1'),
    ('release dispositioned production lots', 'verb + adjective + noun', 'giải phóng các lô sản xuất sau khi quyết định xử lý chất lượng xác nhận rằng chúng có thể tiếp tục theo tuyến đã định', 'C1'),
    ('measure electrical test yields', 'verb + adjective + noun', 'đo tỷ lệ đạt trong kiểm thử điện để đánh giá hiệu suất của wafer, die hoặc lô sản phẩm', 'B2'),
    ('probe completed wafer dies', 'verb + adjective + noun', 'dùng đầu dò kiểm tra điện các die trên wafer đã hoàn tất trước bước cắt và đóng gói', 'C1'),
    ('map defective die locations', 'verb + adjective + noun', 'lập bản đồ vị trí các die lỗi trên wafer để phục vụ phân loại, phân tích và điều khiển bước xử lý sau', 'C1'),
    ('dice finished semiconductor wafers', 'verb + adjective + noun', 'cắt các wafer bán dẫn đã hoàn thiện thành từng die riêng biệt theo đường cắt và dung sai quy định', 'C1'),
    ('attach dies to packages', 'verb + noun phrase', 'gắn die bán dẫn vào đế hoặc vỏ đóng gói bằng vật liệu và quy trình liên kết phù hợp', 'B2'),
    ('bond fine interconnect wires', 'verb + adjective + noun', 'liên kết các dây dẫn mảnh giữa die và chân gói để tạo kết nối điện tin cậy', 'C1'),
    ('encapsulate packaged semiconductor devices', 'verb + adjective + noun', 'bao kín linh kiện bán dẫn đóng gói bằng vật liệu bảo vệ chống ẩm, cơ học và tác động môi trường', 'C1'),
    ('run burn-in reliability tests', 'verb + noun phrase', 'thực hiện thử nghiệm burn-in để sàng lọc lỗi sớm bằng cách vận hành thiết bị dưới điều kiện ứng suất xác định', 'C1'),
    ('screen devices for parametric failures', 'verb + noun phrase', 'sàng lọc linh kiện để phát hiện các sai lệch tham số điện vượt giới hạn kỹ thuật cho phép', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-55-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v55'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-55-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-54 publication: `d3ceb1ce31075499283af412f2e338430f440fe3` — scale-53 publication state verified by English Content Master Plan Acceptance #134, English Content Full Validation #125 and Platform CI #1194; published output: `c6fdf79d94c4540bc2e3dffcd16b998a24e4509a`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-55 publication: `f0e25bc17c5dbb946467d2da61c49d4458bdcb37` — scale-54 publication state verified by English Content Master Plan Acceptance #137, English Content Full Validation #127 and Platform CI #1197; published output: `d9f363c56c17727c54049bf32309dbc59e409342`.',
        'verified scale-54 checkpoint',
    )
    text = replace_once(text, '- Current scale-54 publication awaiting checkpoint CI verification: `d9f363c56c17727c54049bf32309dbc59e409342`.\n', '', 'remove scale-54 pending verification line')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,910 published records after scale-54', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,950 published records after scale-55', 'E04 published count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-54 publication', '## Published runtime snapshot after E04 scale-55 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,910 records', '- phrases: 2,950 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 7,511', '- total published rich records: 7,551', 'rich count')
    text = replace_once(text, '- editorial ledger: 7,511 decisions / 7,511 applied / 7,511 publish decisions', '- editorial ledger: 7,551 decisions / 7,551 applied / 7,551 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001800`', '- E04 collocation frontier: `col.00001840`', 'collocation frontier')
    old_workstream = '''1. Scale-53 publication is fully verified at `d3ceb1ce31075499283af412f2e338430f440fe3`; do not duplicate scale-53 artifacts.
2. Scale-54 publication is complete at `d9f363c56c17727c54049bf32309dbc59e409342`; do not regenerate scale-54 artifacts.
3. Verify this normal-user scale-54 checkpoint with English Content Full Validation, Master Plan Acceptance and Platform CI.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-54 publication is fully verified at `f0e25bc17c5dbb946467d2da61c49d4458bdcb37`; do not duplicate scale-54 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-55 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_next = 'Verify mandatory CI for the scale-54 publication checkpoint without regenerating completed artifacts. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001800` (scale-55 unless a newer worker already advanced the branch), or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-55 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001840` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main55():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-55 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1800:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1800, got {max(nums) if nums else None}')

    new = [make_collocation(1801 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-55: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-55-collocations.json',
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
            'id': 'review.e04.scale-55.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-55-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-55-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-55-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-55-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-55-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-55-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 55 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1800)', 'if(recallCollocations!==1840)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1800 reviewed records', 'must expose 1840 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001801', 'col.00001840'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1840, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2950, 'richRecords': 7551},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main55()
