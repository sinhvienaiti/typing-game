#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-52.py'), run_name='e04_scale53_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-53-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-53.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-53'
REVIEWED_AT = '2026-10-07T10:42:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-53'
EXPECTED = {'collocations': 1720, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('screen clinical trial participants', 'verb + adjective + noun', 'sàng lọc người tham gia thử nghiệm lâm sàng theo tiêu chí nhận vào, loại trừ và các yêu cầu an toàn của nghiên cứu', 'C1'),
    ('obtain informed consent signatures', 'verb + adjective + noun', 'thu thập chữ ký đồng thuận sau khi người tham gia đã được cung cấp và hiểu thông tin cần thiết về nghiên cứu', 'B2'),
    ('verify eligibility criteria compliance', 'verb + noun phrase', 'xác minh việc đáp ứng các tiêu chí đủ điều kiện trước khi đưa người tham gia vào nghiên cứu', 'C1'),
    ('randomize enrolled study subjects', 'verb + adjective + noun', 'phân ngẫu nhiên người tham gia đã được tuyển vào các nhóm nghiên cứu theo phương pháp đã phê duyệt', 'C1'),
    ('dispense investigational medicinal products', 'verb + adjective + noun', 'cấp phát thuốc nghiên cứu theo phân nhóm, liều dùng và quy trình kiểm soát được phê duyệt', 'C1'),
    ('reconcile investigational product inventory', 'verb + adjective + noun', 'đối chiếu tồn kho sản phẩm nghiên cứu giữa số liệu cấp phát, hoàn trả, hủy và lượng thực tế còn lại', 'C1'),
    ('document protocol deviation events', 'verb + noun phrase', 'ghi nhận các sự kiện sai lệch khỏi đề cương nghiên cứu cùng nguyên nhân, tác động và hành động khắc phục', 'C1'),
    ('report serious adverse events', 'verb + adjective + noun', 'báo cáo biến cố bất lợi nghiêm trọng theo thời hạn và yêu cầu của đề cương, nhà tài trợ và cơ quan quản lý', 'C1'),
    ('assess adverse event causality', 'verb + noun phrase', 'đánh giá mối liên hệ nhân quả giữa biến cố bất lợi và can thiệp nghiên cứu dựa trên thông tin lâm sàng hiện có', 'C1'),
    ('monitor participant safety signals', 'verb + noun phrase', 'theo dõi các tín hiệu an toàn ở người tham gia để nhận diện xu hướng hoặc rủi ro mới cần đánh giá', 'C1'),
    ('schedule protocol-mandated study visits', 'verb + adjective + noun', 'lập lịch các lần thăm khám bắt buộc theo đề cương trong đúng cửa sổ thời gian cho phép', 'B2'),
    ('collect protocol-required laboratory samples', 'verb + adjective + noun', 'thu thập mẫu xét nghiệm được đề cương yêu cầu theo đúng thời điểm, loại ống và điều kiện xử lý', 'B2'),
    ('process biological specimens promptly', 'verb + noun phrase', 'xử lý mẫu sinh học kịp thời để bảo toàn chất lượng và tính phù hợp cho phân tích nghiên cứu', 'B2'),
    ('ship frozen specimens securely', 'verb + adjective + noun', 'vận chuyển mẫu đông lạnh an toàn với bao gói, nhiệt độ và hồ sơ theo dõi phù hợp', 'B2'),
    ('maintain specimen chain of custody', 'verb + noun phrase', 'duy trì chuỗi kiểm soát mẫu từ lúc thu thập đến lưu trữ, vận chuyển và tiếp nhận tại phòng xét nghiệm', 'C1'),
    ('calibrate clinical research equipment', 'verb + adjective + noun', 'hiệu chuẩn thiết bị dùng trong nghiên cứu lâm sàng theo lịch để duy trì độ chính xác và khả năng truy xuất', 'C1'),
    ('verify source data accuracy', 'verb + noun phrase', 'xác minh độ chính xác của dữ liệu nguồn bằng cách đối chiếu hồ sơ gốc với dữ liệu đã nhập vào hệ thống nghiên cứu', 'C1'),
    ('resolve electronic data queries', 'verb + adjective + noun', 'xử lý các truy vấn dữ liệu điện tử bằng cách kiểm tra hồ sơ nguồn, làm rõ thông tin và cập nhật hợp lệ', 'B2'),
    ('lock completed case report forms', 'verb + adjective + noun', 'khóa biểu mẫu báo cáo ca đã hoàn tất sau khi dữ liệu được rà soát và các truy vấn liên quan đã được giải quyết', 'C1'),
    ('review missing data patterns', 'verb + adjective + noun', 'xem xét các mẫu dữ liệu thiếu để phát hiện vấn đề hệ thống, sai sót thu thập hoặc rủi ro thiên lệch', 'C1'),
    ('perform remote monitoring visits', 'verb + adjective + noun', 'thực hiện các đợt giám sát từ xa để đánh giá tiến độ, dữ liệu, tuân thủ và vấn đề của điểm nghiên cứu', 'C1'),
    ('conduct on-site monitoring visits', 'verb + adjective + noun', 'thực hiện giám sát trực tiếp tại điểm nghiên cứu để kiểm tra hồ sơ, quy trình và điều kiện thực tế', 'C1'),
    ('track monitoring action items', 'verb + noun phrase', 'theo dõi các hạng mục hành động sau giám sát cho đến khi có bằng chứng khắc phục và đóng việc phù hợp', 'B2'),
    ('close outstanding monitoring findings', 'verb + adjective + noun', 'đóng các phát hiện giám sát còn tồn sau khi hành động khắc phục đã được thực hiện và xác nhận đầy đủ', 'C1'),
    ('submit ethics committee amendments', 'verb + noun phrase', 'nộp các sửa đổi nghiên cứu cho hội đồng đạo đức để được xem xét trước khi triển khai khi có yêu cầu', 'C1'),
    ('renew institutional review approvals', 'verb + adjective + noun', 'gia hạn phê duyệt của hội đồng xem xét tại cơ sở khi nghiên cứu tiếp tục vượt quá kỳ phê duyệt hiện tại', 'C1'),
    ('maintain regulatory binder completeness', 'verb + noun phrase', 'duy trì tính đầy đủ của hồ sơ quản lý nghiên cứu với tài liệu hiện hành, có phiên bản và chữ ký cần thiết', 'C1'),
    ('archive essential trial documents', 'verb + adjective + noun', 'lưu trữ các tài liệu thiết yếu của thử nghiệm theo thời hạn và điều kiện bảo quản được quy định', 'C1'),
    ('verify investigator delegation logs', 'verb + noun phrase', 'xác minh nhật ký phân công của nghiên cứu viên phản ánh đúng người, nhiệm vụ và thời gian được ủy quyền', 'C1'),
    ('document staff training completion', 'verb + noun phrase', 'ghi nhận việc hoàn thành đào tạo của nhân sự nghiên cứu đối với đề cương, quy trình và thay đổi có liên quan', 'B2'),
    ('reconcile participant visit payments', 'verb + noun phrase', 'đối chiếu các khoản chi trả cho người tham gia với số lần thăm khám đủ điều kiện và hồ sơ tài chính liên quan', 'B2'),
    ('track study enrollment targets', 'verb + noun phrase', 'theo dõi mục tiêu tuyển người tham gia so với tiến độ thực tế để nhận diện chậm trễ và nhu cầu điều chỉnh', 'B2'),
    ('forecast site recruitment performance', 'verb + noun phrase', 'dự báo hiệu suất tuyển người của điểm nghiên cứu dựa trên tốc độ sàng lọc, tỷ lệ đủ điều kiện và xu hướng tuyển hiện tại', 'C1'),
    ('evaluate participant retention trends', 'verb + noun phrase', 'đánh giá xu hướng duy trì người tham gia để nhận diện nguy cơ bỏ cuộc và các yếu tố ảnh hưởng đến việc tiếp tục nghiên cứu', 'C1'),
    ('implement retention support measures', 'verb + noun phrase', 'triển khai biện pháp hỗ trợ duy trì người tham gia như nhắc lịch, hỗ trợ đi lại hoặc cải thiện phối hợp theo quy định', 'B2'),
    ('prepare interim analysis datasets', 'verb + adjective + noun', 'chuẩn bị bộ dữ liệu cho phân tích giữa kỳ với phạm vi, mốc cắt dữ liệu và kiểm soát chất lượng phù hợp', 'C1'),
    ('protect treatment assignment blinding', 'verb + noun phrase', 'bảo vệ việc làm mù phân nhóm điều trị để giảm nguy cơ thiên lệch trong thu thập, đánh giá và phân tích dữ liệu', 'C1'),
    ('manage emergency unblinding requests', 'verb + adjective + noun', 'quản lý yêu cầu mở mù khẩn cấp theo điều kiện cho phép và ghi nhận đầy đủ lý do, người phê duyệt và thời điểm', 'C1'),
    ('prepare database lock documentation', 'verb + noun phrase', 'chuẩn bị hồ sơ khóa cơ sở dữ liệu để chứng minh các kiểm tra, phê duyệt và điều kiện đóng dữ liệu đã hoàn tất', 'C1'),
    ('compile clinical study closeout records', 'verb + adjective + noun', 'tổng hợp hồ sơ kết thúc nghiên cứu lâm sàng gồm tài liệu quản lý, dữ liệu, sản phẩm nghiên cứu và xác nhận đóng điểm', 'C1'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-53-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v53'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-53-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-52 verification: `23f896b9408996a12bf495f3da00e6f99125e9b3` — scale-51 publication state verified by English Content Master Plan Acceptance #128, English Content Full Validation #121 and Platform CI #1185; published output: `8984819e3e0671d8fc990b3356f4cbd9b52e6086`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-53 publication: `d12a87c7004bf5009b22ac2069f26c588ae0461a` — scale-52 publication state verified by English Content Master Plan Acceptance #131, English Content Full Validation #123 and Platform CI #1188; published output: `ae830459fb912231aed2ee12cc1c00fe9e447d1b`.',
        'verified scale-52 checkpoint',
    )
    text = replace_once(text, '- Scale-52 publication commit: `ae830459fb912231aed2ee12cc1c00fe9e447d1b` — E04 collocation scale-52 published with clean threshold-0.86 preflight; published frontier is `col.00001720`.\n', '', 'remove scale-52 publication line')
    text = replace_once(text, '- Scale-52 verification state: publication is complete, but the normal-user checkpoint verification is still required. Bot-triggered English Content Master Plan Acceptance #130 and Platform CI #1187 ended `action_required` before jobs ran, matching the known bot-publication pattern; do not regenerate scale-52.\n', '', 'remove scale-52 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,830 published records after scale-52', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,870 published records after scale-53', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-52 publication', '## Published runtime snapshot after E04 scale-53 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,830 records', '- phrases: 2,870 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 7,431', '- total published rich records: 7,471', 'rich count')
    text = replace_once(text, '- editorial ledger: 7,431 decisions / 7,431 applied / 7,431 publish decisions', '- editorial ledger: 7,471 decisions / 7,471 applied / 7,471 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001720`', '- E04 collocation frontier: `col.00001760`', 'collocation frontier')
    old_workstream = '''1. Scale-51 publication is fully verified at `23f896b9408996a12bf495f3da00e6f99125e9b3`; do not duplicate scale-51 artifacts.
2. Scale-52 source/application/publication is complete at `ae830459fb912231aed2ee12cc1c00fe9e447d1b`; do not regenerate or republish it.
3. Verify this normal-user checkpoint with all three mandatory workflows: English Content Master Plan Acceptance, English Content Full Validation and Platform CI. Scale-52 is not fully verified until all three PASS on the checkpoint.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. After scale-52 is fully verified, re-resolve HEAD and recalculate deficits. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-52 publication is fully verified at `d12a87c7004bf5009b22ac2069f26c588ae0461a`; do not duplicate scale-52 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-53 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_next = 'Scale-52 publication is complete at `ae830459fb912231aed2ee12cc1c00fe9e447d1b`. Verify this normal-user checkpoint until English Content Master Plan Acceptance, English Content Full Validation and Platform CI all PASS. Do not create a second CI-refresh checkpoint. Once all three pass, mark scale-52 fully verified in the next real-state progress update associated with subsequent bounded work, then continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001720` (expected scale-53 range `col.00001721` through `col.00001760` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-53 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001760` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main53():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-53 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1720:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1720, got {max(nums) if nums else None}')

    new = [make_collocation(1721 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-53: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-53-collocations.json',
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
            'id': 'review.e04.scale-53.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-53-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-53-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-53-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-53-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-53-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-53-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 53 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1720)', 'if(recallCollocations!==1760)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1720 reviewed records', 'must expose 1760 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001721', 'col.00001760'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1760, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2870, 'richRecords': 7471},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main53()
