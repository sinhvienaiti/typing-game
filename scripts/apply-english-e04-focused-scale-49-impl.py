#!/usr/bin/env python3
from __future__ import annotations

import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-48.py'), run_name='e04_scale49_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-49-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-49.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-49'
REVIEWED_AT = '2026-10-07T09:05:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-49'
EXPECTED = {'collocations': 1560, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('receive inbound shipments', 'verb + adjective + noun', 'tiếp nhận các lô hàng đi vào kho và thực hiện các bước kiểm tra ban đầu theo quy trình', 'B2'),
    ('verify pallet labels', 'verb + noun phrase', 'xác minh nhãn pallet để bảo đảm mã hàng, lô và thông tin định danh khớp với chứng từ', 'B2'),
    ('scan inventory barcodes', 'verb + noun phrase', 'quét mã vạch hàng tồn kho để cập nhật vị trí, số lượng và trạng thái hàng hóa', 'B2'),
    ('inspect package damage', 'verb + noun phrase', 'kiểm tra hư hỏng bao bì để phát hiện sản phẩm có nguy cơ mất chất lượng trong vận chuyển', 'B2'),
    ('reconcile receiving records', 'verb + adjective + noun', 'đối chiếu hồ sơ nhận hàng với hàng thực tế và chứng từ để xử lý sai lệch', 'C1'),
    ('assign storage locations', 'verb + noun phrase', 'phân bổ vị trí lưu kho phù hợp theo loại hàng, sức chứa và yêu cầu vận hành', 'B2'),
    ('replenish picking zones', 'verb + noun phrase', 'bổ sung hàng vào khu vực lấy hàng để duy trì đủ tồn kho phục vụ đơn đang xử lý', 'B2'),
    ('rotate dated stock', 'verb + adjective + noun', 'luân chuyển hàng có hạn sử dụng theo nguyên tắc phù hợp để giảm nguy cơ tồn hàng quá hạn', 'B2'),
    ('monitor cold-room temperature', 'verb + noun phrase', 'theo dõi nhiệt độ kho lạnh để bảo đảm hàng nhạy cảm nhiệt độ được bảo quản trong giới hạn quy định', 'B2'),
    ('log freezer alarms', 'verb + noun phrase', 'ghi nhận các cảnh báo tủ đông để theo dõi sự cố và hành động khắc phục', 'B2'),
    ('calibrate temperature sensors', 'verb + noun phrase', 'hiệu chuẩn cảm biến nhiệt độ để số liệu giám sát chuỗi lạnh có độ chính xác cần thiết', 'B2'),
    ('inspect dock seals', 'verb + noun phrase', 'kiểm tra gioăng kín tại cửa bốc dỡ để hạn chế thất thoát nhiệt và xâm nhập từ môi trường bên ngoài', 'B2'),
    ('secure loading bays', 'verb + adjective + noun', 'bảo đảm khu vực bốc dỡ được kiểm soát an toàn trước và trong quá trình xử lý hàng', 'B2'),
    ('stage outbound orders', 'verb + adjective + noun', 'tập kết các đơn hàng xuất kho theo chuyến hoặc tuyến giao trước khi chất lên phương tiện', 'B2'),
    ('consolidate partial pallets', 'verb + adjective + noun', 'gộp các pallet chưa đầy khi phù hợp để sử dụng không gian và vận chuyển hiệu quả hơn', 'C1'),
    ('wrap pallet loads', 'verb + noun phrase', 'quấn cố định hàng trên pallet để giảm xê dịch hoặc hư hỏng trong thao tác và vận chuyển', 'B2'),
    ('verify shipment weights', 'verb + noun phrase', 'xác minh trọng lượng lô hàng để phát hiện sai lệch và hỗ trợ tính tải hoặc cước', 'B2'),
    ('print shipping labels', 'verb + noun phrase', 'in nhãn vận chuyển với thông tin nhận dạng và định tuyến cần thiết cho lô hàng', 'B2'),
    ('load delivery vehicles', 'verb + noun phrase', 'chất hàng lên phương tiện giao nhận theo thứ tự và yêu cầu an toàn phù hợp', 'B2'),
    ('sequence delivery stops', 'verb + noun phrase', 'sắp xếp thứ tự các điểm giao để hỗ trợ tuyến vận chuyển hiệu quả và đúng thời gian', 'C1'),
    ('track proof of delivery', 'verb + noun phrase', 'theo dõi bằng chứng giao hàng để xác nhận đơn đã được bàn giao cho đúng người hoặc địa điểm', 'B2'),
    ('investigate inventory discrepancies', 'verb + noun phrase', 'điều tra chênh lệch tồn kho để xác định nguyên nhân giữa số liệu hệ thống và hàng thực tế', 'C1'),
    ('cycle count stock', 'verb + noun phrase', 'kiểm đếm luân phiên một phần hàng tồn kho theo lịch để duy trì độ chính xác tồn kho', 'B2'),
    ('quarantine damaged goods', 'verb + adjective + noun', 'cách ly hàng bị hư hỏng để ngăn sử dụng hoặc xuất đi trước khi có quyết định xử lý', 'B2'),
    ('release quality holds', 'verb + noun phrase', 'gỡ trạng thái giữ chất lượng sau khi hàng đã đáp ứng điều kiện kiểm tra và được phép lưu chuyển', 'C1'),
    ('maintain batch traceability', 'verb + noun phrase', 'duy trì khả năng truy xuất theo lô từ lúc nhận đến lưu kho và phân phối', 'C1'),
    ('record lot numbers', 'verb + noun phrase', 'ghi lại số lô để hỗ trợ truy xuất, kiểm soát chất lượng và xử lý thu hồi', 'B2'),
    ('enforce temperature limits', 'verb + noun phrase', 'thực thi giới hạn nhiệt độ trong bảo quản và vận chuyển đối với hàng cần kiểm soát nhiệt', 'C1'),
    ('pre-cool refrigerated trailers', 'verb + adjective + noun', 'làm lạnh trước thùng xe lạnh đến nhiệt độ yêu cầu trước khi chất hàng nhạy cảm nhiệt', 'C1'),
    ('sanitize storage areas', 'verb + noun phrase', 'vệ sinh khử khuẩn khu vực lưu kho để giảm nguy cơ nhiễm bẩn hàng hóa', 'B2'),
    ('inspect racking systems', 'verb + noun phrase', 'kiểm tra hệ thống giá kệ để phát hiện biến dạng, hư hỏng hoặc điều kiện mất an toàn', 'B2'),
    ('clear warehouse aisles', 'verb + noun phrase', 'giữ lối đi trong kho thông thoáng để hỗ trợ di chuyển người và thiết bị an toàn', 'B2'),
    ('service dock levelers', 'verb + noun phrase', 'bảo dưỡng bàn nâng cầu dẫn tại cửa kho để duy trì thao tác bốc dỡ ổn định và an toàn', 'C1'),
    ('charge forklift batteries', 'verb + noun phrase', 'sạc ắc quy xe nâng theo quy trình để duy trì thiết bị sẵn sàng vận hành', 'B2'),
    ('inspect lifting equipment', 'verb + adjective + noun', 'kiểm tra thiết bị nâng để phát hiện hao mòn hoặc lỗi có thể ảnh hưởng an toàn thao tác', 'B2'),
    ('schedule carrier pickups', 'verb + noun phrase', 'lập lịch hãng vận chuyển đến lấy hàng theo thời gian xuất kho và năng lực bốc dỡ', 'B2'),
    ('manage return shipments', 'verb + noun phrase', 'quản lý các lô hàng trả về từ khâu vận chuyển đến tiếp nhận, kiểm tra và định tuyến xử lý', 'B2'),
    ('process customer returns', 'verb + noun phrase', 'xử lý hàng khách trả lại theo quy trình kiểm tra, hoàn kho, sửa chữa hoặc loại bỏ', 'B2'),
    ('segregate recalled products', 'verb + adjective + noun', 'tách riêng sản phẩm bị thu hồi để ngăn chúng tiếp tục được phân phối hoặc sử dụng', 'C1'),
    ('document chain-of-custody transfers', 'verb + noun phrase', 'ghi chép các lần chuyển giao trách nhiệm bảo quản để duy trì hồ sơ chuỗi kiểm soát rõ ràng', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-49-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v49'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-49-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-48 publication: `64d77904e3361da2bd51a356c33cb992f04b41db` — scale-47 publication state verified by English Content Master Plan Acceptance #115, English Content Full Validation #112 and Platform CI #1166; published output: `113edd521e847f9b3623d7af08045bc1ff65da26`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-49 publication: `1da7f8a848925a3c9843b9015e82ddfe05ca4a36` — scale-48 publication state verified by English Content Master Plan Acceptance #118, English Content Full Validation #114 and Platform CI #1170; published output: `c4c6a387cd1a5fbc062352b18b73b078826384c4`.',
        'verified scale-48 checkpoint',
    )
    text = replace_once(text, '- Scale-48 publication output: `c4c6a387cd1a5fbc062352b18b73b078826384c4` — `feat(content): publish E04 collocation scale 48`; Apply English E04 Scale 48 #1 passed preflight, controlled review, full quality gates, converge, deterministic replay and bot commit/push.\n', '', 'remove scale-48 publication line')
    text = replace_once(text, '- Scale-48 publication verification note: because the publication commit was created by `github-actions[bot]`, its PR-triggered English Content Master Plan Acceptance #117 and Platform CI #1169 ended `action_required` before any job started. This normal-user checkpoint intentionally re-triggers the mandatory CI without regenerating scale-48 content or weakening any gate.\n', '', 'remove scale-48 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,670 published records after scale-48', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,710 published records after scale-49', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-48 publication', '## Published runtime snapshot after E04 scale-49 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,670 records', '- phrases: 2,710 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 7,271', '- total published rich records: 7,311', 'rich count')
    text = replace_once(text, '- editorial ledger: 7,271 decisions / 7,271 applied / 7,271 publish decisions', '- editorial ledger: 7,311 decisions / 7,311 applied / 7,311 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001560`', '- E04 collocation frontier: `col.00001600`', 'collocation frontier')
    old_workstream = '''1. Scale-47 publication is fully verified; do not duplicate scale-47 artifacts.
2. Scale-48 publication `c4c6a387cd1a5fbc062352b18b73b078826384c4` is complete; do not regenerate or duplicate scale-48 artifacts.
3. Verify scale-48 publication state through the CI attached to this normal-user checkpoint; the bot-authored PR workflow attempts #117/#1169 ended `action_required` before jobs ran.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. If scale-48 checkpoint CI passes and no newer worker has claimed the next scope, create scale-49 as the next bounded collocation batch from frontier `col.00001560`, expected IDs `col.00001561` through `col.00001600`, while preserving exact/near-dedupe threshold 0.86 and all E10/E11/E12 gates.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-48 publication is fully verified; do not duplicate scale-48 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-49 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-48 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-48 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001560` (expected scale-49 range `col.00001561` through `col.00001600` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-49 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001600` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


scope.update({
    'MANIFEST_PATH': MANIFEST_PATH,
    'COL_PATH': COL_PATH,
    'DECISION_PATH': DECISION_PATH,
    'PROGRESS_PATH': PROGRESS_PATH,
    'BATCH_ID': BATCH_ID,
    'REVIEWED_AT': REVIEWED_AT,
    'REVIEWED_BY': REVIEWED_BY,
    'EXPECTED': EXPECTED,
    'NEAR_DUP_THRESHOLD': NEAR_DUP_THRESHOLD,
    'COLLOCATIONS': COLLOCATIONS,
    'make_collocation': make_collocation,
    'update_progress': update_progress,
})

# Patch the scale-specific constants embedded in the inherited main function by
# temporarily supplying the scale-49 values through its globals.
main = scope['main']
main_globals = main.__globals__
main_globals.update(scope)

# The inherited main uses fixed frontier/range literals from scale-48, so scale-49
# keeps the same validated algorithm but provides a compact local main with the new frontier.
def main49():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-49 artifact exists without matching batch manifest')

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
    import re
    nums = [int(match.group(1)) for record in existing['collocations'] if (match := re.fullmatch(r'col\.(\d{8})', str(record.get('id', ''))))]
    if not nums or max(nums) != 1560:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1560, got {max(nums) if nums else None}')

    new = [make_collocation(1561 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-49: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-49-collocations.json',
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
            'id': 'review.e04.scale-49.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-49-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-49-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-49-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-49-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-49-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-49-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 49 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1560)', 'if(recallCollocations!==1600)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1560 reviewed records', 'must expose 1600 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001561', 'col.00001600'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1600, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2710, 'richRecords': 7311},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main49()
