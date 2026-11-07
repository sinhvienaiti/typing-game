#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-59.py'), run_name='e04_scale60_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-60-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-60.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-60'
REVIEWED_AT = '2026-10-07T13:40:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-60'
EXPECTED = {'collocations': 2000, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('coordinate berth line handling', 'verb + noun phrase', 'phối hợp thao tác dây buộc tại cầu cảng để tàu cập hoặc rời bến an toàn, đúng trình tự và không gây tải bất thường lên thiết bị neo', 'C1'),
    ('confirm vessel draft clearance', 'verb + noun phrase', 'xác nhận mớn nước của tàu phù hợp với độ sâu luồng và cầu bến trước khi cho phép di chuyển trong khu vực cảng', 'C1'),
    ('monitor under-keel clearance', 'verb + noun phrase', 'theo dõi khoảng hở dưới đáy tàu để duy trì biên an toàn khi thủy triều, tải trọng hoặc độ sâu luồng thay đổi', 'C1'),
    ('schedule tidal berth windows', 'verb + noun phrase', 'lập lịch khung giờ cập bến theo thủy triều để tàu có đủ độ sâu và giảm rủi ro chậm trễ khai thác', 'C1'),
    ('coordinate pilot boarding arrangements', 'verb + noun phrase', 'phối hợp việc đón trả hoa tiêu gồm vị trí, thời điểm và phương tiện tiếp cận để bảo đảm chuyển người an toàn', 'C1'),
    ('verify harbor tug availability', 'verb + noun phrase', 'xác nhận tàu kéo cảng sẵn sàng đúng số lượng và công suất cần thiết cho kế hoạch điều động tàu', 'B2'),
    ('secure mooring lines properly', 'verb + noun phrase', 'cố định dây buộc tàu đúng cách để duy trì vị trí tàu ổn định trước gió, dòng chảy và thay đổi mực nước', 'B2'),
    ('inspect bollard load condition', 'verb + noun phrase', 'kiểm tra tình trạng chịu tải của bích neo để phát hiện hư hỏng hoặc dấu hiệu quá tải trước khi sử dụng', 'C1'),
    ('inspect gangway safety nets', 'verb + noun phrase', 'kiểm tra lưới an toàn cầu thang lên xuống tàu để giảm nguy cơ ngã xuống nước hoặc khu vực giữa tàu và bờ', 'B2'),
    ('confirm berth departure readiness', 'verb + noun phrase', 'xác nhận tàu và cầu bến đã sẵn sàng rời bến sau khi hoàn tất hàng hóa, chứng từ, dây buộc và điều động hỗ trợ', 'B2'),
    ('assign container crane sequences', 'verb + noun phrase', 'phân bổ trình tự làm việc của cẩu container để cân bằng năng suất, hạn chế giao cắt và bám sát kế hoạch xếp dỡ', 'C1'),
    ('monitor quay crane productivity', 'verb + noun phrase', 'theo dõi năng suất cẩu bờ theo số lượt nâng và thời gian chu kỳ để phát hiện sớm điểm nghẽn khai thác', 'C1'),
    ('sequence container discharge moves', 'verb + noun phrase', 'sắp xếp thứ tự dỡ container từ tàu để duy trì ổn định tàu và cấp hàng hợp lý cho khu bãi', 'C1'),
    ('verify stowage plan revisions', 'verb + noun phrase', 'xác nhận các thay đổi kế hoạch xếp hàng đã được cập nhật nhất quán trước khi tiếp tục xếp hoặc dỡ container', 'C1'),
    ('reconcile container load lists', 'verb + noun phrase', 'đối soát danh sách container xếp tàu với kế hoạch thực tế để phát hiện thiếu, thừa hoặc sai vị trí', 'B2'),
    ('verify container seal integrity', 'verb + noun phrase', 'xác nhận niêm phong container còn nguyên vẹn và số niêm phong khớp hồ sơ trước khi giao nhận hoặc kiểm tra', 'B2'),
    ('inspect twistlock engagement', 'verb + noun phrase', 'kiểm tra khóa xoắn đã gài đúng vào góc container để bảo đảm container được cố định trong vận chuyển và xếp chồng', 'B2'),
    ('inspect container corner castings', 'verb + noun phrase', 'kiểm tra các góc đúc của container để phát hiện nứt, biến dạng hoặc hư hỏng ảnh hưởng đến nâng hạ và khóa giữ', 'B2'),
    ('secure refrigerated container power', 'verb + noun phrase', 'bảo đảm nguồn điện cho container lạnh được kết nối chắc chắn để duy trì nhiệt độ hàng hóa trong thời gian lưu bãi', 'B2'),
    ('monitor reefer temperature alarms', 'verb + noun phrase', 'theo dõi cảnh báo nhiệt độ container lạnh để xử lý sớm mất điện, sai nhiệt độ hoặc sự cố thiết bị làm lạnh', 'B2'),
    ('position straddle carriers safely', 'verb + noun phrase', 'định vị xe nâng khung an toàn khi tiếp cận container để tránh va chạm với người, thiết bị và hàng hóa xung quanh', 'B2'),
    ('route terminal tractor movements', 'verb + noun phrase', 'điều hướng di chuyển của đầu kéo trong cảng theo tuyến được phân công để giảm giao cắt và ùn tắc nội bộ', 'B2'),
    ('inspect rubber-tired gantry cranes', 'verb + noun phrase', 'kiểm tra cẩu giàn bánh lốp trước vận hành để phát hiện bất thường ở bánh xe, cơ cấu nâng, phanh và thiết bị an toàn', 'C1'),
    ('coordinate yard crane dispatch', 'verb + noun phrase', 'phối hợp điều động cẩu bãi theo nhu cầu nâng hạ thực tế để giảm thời gian chờ và di chuyển không cần thiết', 'C1'),
    ('optimize container yard stacking', 'verb + noun phrase', 'tối ưu cách xếp container trong bãi theo chuyến tàu, thời gian lấy hàng và đặc tính container để giảm đảo chuyển', 'C1'),
    ('segregate hazardous cargo units', 'verb + noun phrase', 'phân tách các đơn vị hàng nguy hiểm theo nhóm tương thích và yêu cầu khoảng cách để giảm rủi ro sự cố hóa chất', 'C1'),
    ('verify dangerous goods declarations', 'verb + noun phrase', 'xác nhận khai báo hàng nguy hiểm đầy đủ và khớp với nhãn, chứng từ cùng thông tin vận chuyển trước khi chấp nhận hàng', 'C1'),
    ('inspect spill response equipment', 'verb + noun phrase', 'kiểm tra thiết bị ứng phó tràn đổ để bảo đảm vật tư thấm hút, rào chắn và dụng cụ bảo hộ sẵn sàng sử dụng', 'B2'),
    ('maintain terminal fire lane access', 'verb + noun phrase', 'duy trì lối tiếp cận dành cho chữa cháy trong bến cảng luôn thông thoáng để phương tiện khẩn cấp có thể triển khai nhanh', 'B2'),
    ('monitor terminal gate congestion', 'verb + noun phrase', 'theo dõi ùn tắc tại cổng cảng để điều chỉnh luồng xe, lịch hẹn và làn xử lý trước khi hàng chờ kéo dài', 'C1'),
    ('validate truck appointment slots', 'verb + noun phrase', 'kiểm tra tính hợp lệ của khung giờ hẹn xe tải để bảo đảm phương tiện đến đúng thời điểm và đúng nghiệp vụ giao nhận', 'B2'),
    ('verify driver credential records', 'verb + noun phrase', 'xác nhận hồ sơ nhận dạng và quyền ra vào của tài xế trước khi cho phép phương tiện đi vào khu vực hạn chế', 'B2'),
    ('weigh outbound container loads', 'verb + noun phrase', 'cân container xuất cổng để xác nhận khối lượng khai báo và hỗ trợ yêu cầu an toàn, vận tải cùng chứng từ', 'B2'),
    ('reconcile gate transaction records', 'verb + noun phrase', 'đối soát giao dịch cổng với container, phương tiện và lệnh giao nhận để phát hiện sai lệch dữ liệu trước khi khóa ca', 'C1'),
    ('calibrate weighbridge measurement systems', 'verb + noun phrase', 'hiệu chuẩn hệ thống cân xe để duy trì độ chính xác đo khối lượng và đáp ứng yêu cầu kiểm soát khai thác', 'C1'),
    ('coordinate customs hold releases', 'verb + noun phrase', 'phối hợp giải phóng lệnh giữ của hải quan sau khi có phê duyệt để container chỉ được di chuyển khi trạng thái pháp lý hợp lệ', 'C1'),
    ('inspect customs examination areas', 'verb + noun phrase', 'kiểm tra khu vực khám hàng hải quan để bảo đảm an ninh, chiếu sáng, thiết bị và vùng thao tác sẵn sàng', 'B2'),
    ('document container damage findings', 'verb + noun phrase', 'ghi lại phát hiện hư hỏng container bằng vị trí, mức độ và bằng chứng phù hợp để hỗ trợ quyết định giao nhận hoặc sửa chữa', 'C1'),
    ('respond to berth safety incidents', 'verb + noun phrase', 'ứng phó sự cố an toàn tại cầu bến bằng cách cô lập khu vực, hỗ trợ người liên quan và kích hoạt quy trình báo cáo phù hợp', 'C1'),
    ('review port call performance', 'verb + noun phrase', 'đánh giá hiệu quả một lượt tàu ghé cảng theo thời gian chờ, năng suất xếp dỡ, thời gian quay vòng và các nguyên nhân chậm trễ', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-60-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v60'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-60-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-59 publication: `f106329a536d17416768e64ecb1a2b80aba87f0f` — scale-58 publication state verified by English Content Master Plan Acceptance #149, English Content Full Validation #135 and Platform CI #1209; published output: `704ad2444e0cf0ac93d18c8098ec90aba067496d`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-60 publication: `3022771803cd449b254abfc4ccc60180656819c1` — scale-59 publication state verified by English Content Master Plan Acceptance #153, English Content Full Validation #138 and Platform CI #1213; published output: `4a07d83aa704ccd64a4a994495aac4b560474441`.',
        'verified scale-59 checkpoint',
    )
    text = replace_once(text, '- Scale-59 publication completed at `4a07d83aa704ccd64a4a994495aac4b560474441`; this checkpoint update exists to verify the publication under a normal-user HEAD before opening scale-60.\n', '', 'remove scale-59 checkpoint-pending line')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,110 published records after scale-59', '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,150 published records after scale-60', 'E04 published count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-59 publication', '## Published runtime snapshot after E04 scale-60 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 3,110 records', '- phrases: 3,150 records', 'phrase runtime count')
    text = replace_once(text, '- total published rich records: 7,711', '- total published rich records: 7,751', 'rich runtime count')
    text = replace_once(text, '- editorial ledger: 7,711 decisions / 7,711 applied / 7,711 publish decisions', '- editorial ledger: 7,751 decisions / 7,751 applied / 7,751 publish decisions', 'editorial ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00002000`', '- E04 collocation frontier: `col.00002040`', 'collocation frontier')
    text = replace_once(
        text,
        '1. Scale-58 publication is fully verified at `f106329a536d17416768e64ecb1a2b80aba87f0f`; do not duplicate scale-58 artifacts.',
        '1. Scale-59 publication is fully verified at `3022771803cd449b254abfc4ccc60180656819c1`; do not duplicate scale-59 artifacts.',
        'first unfinished verified item',
    )
    text = replace_once(
        text,
        '2. Scale-59 publication completed at `4a07d83aa704ccd64a4a994495aac4b560474441`; the earlier exact duplicate at `col.00001988` was replaced without weakening the `0.86` preflight threshold.',
        '2. Scale-60 is the current publication unit; do not start another collocation batch until its publication/checkpoint CI completes.',
        'first unfinished publication item',
    )
    text = replace_once(
        text,
        '3. Verify English Content Full Validation, Master Plan Acceptance and Platform CI on this normal-user checkpoint before attaching any scale-60 preparation commit.',
        '3. After the scale-60 bot publication commit is created, create one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.',
        'first unfinished checkpoint item',
    )
    old_next = 'Verify all three mandatory CI workflows for the scale-59 normal-user checkpoint. If PASS, continue immediately with a genuinely new bounded collocation batch from frontier `col.00002000` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-60 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002040` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main60():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-60 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 2000:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 2000, got {max(nums) if nums else None}')

    new = [make_collocation(2001 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-60: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-60-collocations.json',
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
            'id': 'review.e04.scale-60.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-60-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-60-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-60-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-60-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-60-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-60-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 60 maritime container-terminal operations collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==2000)', 'if(recallCollocations!==2040)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 2000 reviewed records', 'must expose 2040 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00002001', 'col.00002040'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 2040, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 3150, 'richRecords': 7751},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main60()
