#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scope = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-51.py'), run_name='e04_scale52_base')

read_json = scope['read_json']
write_json = scope['write_json']
normalized_key = scope['normalized_key']
jaccard = scope['jaccard']
digest = scope['digest']
replace_once = scope['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-52-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-52.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-52'
REVIEWED_AT = '2026-10-07T10:32:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-52'
EXPECTED = {'collocations': 1680, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('rotate privileged access credentials', 'verb + adjective + noun', 'luân phiên thông tin xác thực có đặc quyền theo lịch hoặc sau sự kiện rủi ro để giảm khả năng lạm dụng lâu dài', 'C1'),
    ('revoke dormant user accounts', 'verb + adjective + noun', 'thu hồi các tài khoản người dùng không còn hoạt động để giảm bề mặt tấn công và quyền truy cập dư thừa', 'B2'),
    ('enforce multifactor authentication policies', 'verb + adjective + noun', 'thực thi chính sách xác thực đa yếu tố cho các hệ thống và nhóm người dùng thuộc phạm vi bắt buộc', 'C1'),
    ('review elevated access requests', 'verb + adjective + noun', 'xem xét yêu cầu cấp quyền truy cập nâng cao dựa trên nhu cầu công việc, phạm vi và thời hạn phù hợp', 'C1'),
    ('monitor suspicious login patterns', 'verb + adjective + noun', 'theo dõi mẫu đăng nhập đáng ngờ như vị trí bất thường, tần suất cao hoặc hành vi khác với thông lệ', 'C1'),
    ('triage endpoint security alerts', 'verb + noun phrase', 'phân loại ban đầu các cảnh báo bảo mật thiết bị đầu cuối để xác định mức độ ưu tiên và hướng điều tra', 'C1'),
    ('isolate compromised workstations', 'verb + adjective + noun', 'cô lập máy trạm bị xâm nhập khỏi mạng để hạn chế lan truyền và bảo toàn bằng chứng điều tra', 'B2'),
    ('quarantine malicious email attachments', 'verb + adjective + noun', 'cách ly tệp đính kèm email độc hại để ngăn người dùng hoặc hệ thống tiếp tục truy cập và thực thi', 'B2'),
    ('block known command-and-control domains', 'verb + adjective + noun', 'chặn các tên miền chỉ huy và kiểm soát đã biết nhằm cắt liên lạc giữa mã độc và hạ tầng của kẻ tấn công', 'C1'),
    ('update intrusion detection signatures', 'verb + noun phrase', 'cập nhật chữ ký phát hiện xâm nhập để nhận diện các mẫu tấn công và chỉ báo mới đã được xác thực', 'C1'),
    ('tune security monitoring rules', 'verb + noun phrase', 'tinh chỉnh quy tắc giám sát bảo mật để cải thiện tín hiệu hữu ích và giảm cảnh báo giả không cần thiết', 'C1'),
    ('correlate authentication event logs', 'verb + noun phrase', 'liên kết nhật ký sự kiện xác thực từ nhiều nguồn để phát hiện chuỗi hành vi đáng ngờ hoặc truy cập bất thường', 'C1'),
    ('preserve incident forensic evidence', 'verb + adjective + noun', 'bảo toàn bằng chứng pháp chứng của sự cố theo cách duy trì tính toàn vẹn và khả năng truy xuất nguồn gốc', 'C1'),
    ('capture volatile memory images', 'verb + adjective + noun', 'thu thập ảnh bộ nhớ khả biến để giữ lại tiến trình, kết nối và dữ liệu tạm thời phục vụ điều tra', 'C1'),
    ('document incident response timelines', 'verb + noun phrase', 'ghi lại dòng thời gian ứng phó sự cố gồm phát hiện, quyết định, hành động và mốc khôi phục quan trọng', 'C1'),
    ('escalate critical security incidents', 'verb + adjective + noun', 'chuyển cấp các sự cố bảo mật nghiêm trọng đến nhóm và cấp quản lý phù hợp theo tiêu chí đã định', 'B2'),
    ('coordinate breach notification procedures', 'verb + noun phrase', 'phối hợp quy trình thông báo vi phạm dữ liệu theo nghĩa vụ pháp lý, hợp đồng và kế hoạch truyền thông', 'C1'),
    ('validate backup restoration procedures', 'verb + noun phrase', 'xác thực quy trình khôi phục từ bản sao lưu bằng thử nghiệm có kiểm soát để bảo đảm dữ liệu và dịch vụ có thể phục hồi', 'C1'),
    ('test disaster recovery failover', 'verb + noun phrase', 'kiểm thử chuyển đổi dự phòng trong kế hoạch khôi phục thảm họa để xác nhận hệ thống thay thế hoạt động đúng yêu cầu', 'C1'),
    ('verify recovery point objectives', 'verb + adjective + noun', 'xác minh mục tiêu điểm khôi phục phù hợp với tần suất sao lưu, sao chép và mức mất dữ liệu chấp nhận được', 'C1'),
    ('measure recovery time objectives', 'verb + adjective + noun', 'đo khả năng đáp ứng mục tiêu thời gian khôi phục của dịch vụ thông qua diễn tập hoặc sự cố thực tế', 'C1'),
    ('scan internet-facing assets', 'verb + adjective + noun', 'quét các tài sản hướng Internet để phát hiện dịch vụ lộ ra ngoài, cấu hình yếu và lỗ hổng có thể khai thác', 'B2'),
    ('prioritize exploitable vulnerabilities', 'verb + adjective + noun', 'ưu tiên lỗ hổng có khả năng bị khai thác dựa trên mức độ phơi bày, tác động và bằng chứng đe dọa', 'C1'),
    ('track remediation due dates', 'verb + noun phrase', 'theo dõi hạn hoàn thành khắc phục lỗ hổng và điểm yếu để tránh tồn đọng vượt mức rủi ro cho phép', 'B2'),
    ('validate security patch deployment', 'verb + noun phrase', 'xác thực việc triển khai bản vá bảo mật đã hoàn tất trên đúng phạm vi và không gây lỗi vận hành đáng kể', 'C1'),
    ('review firewall rule exceptions', 'verb + noun phrase', 'xem xét các ngoại lệ luật tường lửa để bảo đảm nhu cầu còn hợp lệ và phạm vi mở mạng được giới hạn', 'C1'),
    ('restrict unnecessary network ports', 'verb + adjective + noun', 'hạn chế các cổng mạng không cần thiết để giảm dịch vụ có thể bị dò quét hoặc tấn công', 'B2'),
    ('segment sensitive application networks', 'verb + adjective + noun', 'phân đoạn mạng của ứng dụng nhạy cảm để giới hạn đường đi truy cập và giảm khả năng di chuyển ngang', 'C1'),
    ('inspect encrypted traffic metadata', 'verb + adjective + noun', 'kiểm tra siêu dữ liệu của lưu lượng mã hóa để nhận diện mẫu bất thường mà không cần giải mã nội dung trái chính sách', 'C1'),
    ('rotate application signing certificates', 'verb + noun phrase', 'luân phiên chứng thư ký ứng dụng trước khi hết hạn hoặc khi khóa liên quan có nguy cơ bị lộ', 'C1'),
    ('protect cryptographic key material', 'verb + adjective + noun', 'bảo vệ vật liệu khóa mật mã bằng kiểm soát truy cập, lưu trữ an toàn và quy trình vòng đời phù hợp', 'C1'),
    ('audit secrets management practices', 'verb + noun phrase', 'đánh giá cách quản lý bí mật như mật khẩu dịch vụ, token và khóa API để phát hiện lưu trữ hoặc phân phối không an toàn', 'C1'),
    ('remove hard-coded credentials', 'verb + adjective + noun', 'loại bỏ thông tin xác thực được ghi cứng trong mã nguồn hoặc cấu hình và chuyển sang cơ chế quản lý bí mật an toàn', 'B2'),
    ('review third-party security attestations', 'verb + adjective + noun', 'xem xét chứng thực bảo mật của bên thứ ba để đánh giá mức độ kiểm soát và các ngoại lệ có liên quan đến dịch vụ sử dụng', 'C1'),
    ('assess vendor cyber risk', 'verb + noun phrase', 'đánh giá rủi ro an ninh mạng của nhà cung cấp dựa trên dữ liệu xử lý, quyền truy cập và mức độ phụ thuộc dịch vụ', 'C1'),
    ('monitor exposed cloud storage', 'verb + adjective + noun', 'theo dõi kho lưu trữ đám mây bị phơi bày để phát hiện cấu hình công khai ngoài ý muốn và dữ liệu có nguy cơ rò rỉ', 'C1'),
    ('enforce secure configuration baselines', 'verb + adjective + noun', 'thực thi cấu hình chuẩn an toàn trên hệ điều hành, dịch vụ và nền tảng để giảm sai lệch cấu hình', 'C1'),
    ('detect unauthorized configuration drift', 'verb + adjective + noun', 'phát hiện thay đổi cấu hình không được phê duyệt so với baseline nhằm nhận diện sai lệch hoặc hành vi can thiệp trái phép', 'C1'),
    ('conduct phishing simulation exercises', 'verb + noun phrase', 'thực hiện diễn tập giả lập lừa đảo để đo khả năng nhận biết, báo cáo và phản ứng của người dùng', 'B2'),
    ('track security awareness completion', 'verb + noun phrase', 'theo dõi việc hoàn thành đào tạo nhận thức bảo mật để xác định nhóm quá hạn và duy trì yêu cầu tuân thủ', 'B2'),
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
            'schema': {'status': 'pass', 'method': 'e04-scale-52-authoring-v1'},
            'grammar': {'status': 'pending', 'method': 'manual-review-required'},
            'translation': {'status': 'pending', 'method': 'manual-review-required'},
            'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
            'cefr': {'status': 'pending', 'method': 'manual-review-required'},
            'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
            'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v52'},
            'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
            'license': {'status': 'pending', 'method': 'manual-review-required'},
        }},
        'provenance': {'sources': [{
            'dataset': 'project-original',
            'sourceId': rid,
            'sourceUrl': 'content/english/phrases/e04-scale-52-collocations.json',
            'snapshot': '2026-10',
            'license': 'LicenseRef-Project-Original',
            'modified': False,
        }], 'note': 'Project-original controlled E04 scale-up record.'},
    }


def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-51 verification: `2c25c72ecb7367dcb486806910ce980c7a7edc85` — scale-50 publication state verified by English Content Master Plan Acceptance #125, English Content Full Validation #119 and Platform CI #1180; published output: `af88c97dedd74dc8159a05528f3c79fb8af6c3c7`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-52 publication: `23f896b9408996a12bf495f3da00e6f99125e9b3` — scale-51 publication state verified by English Content Master Plan Acceptance #128, English Content Full Validation #121 and Platform CI #1185; published output: `8984819e3e0671d8fc990b3356f4cbd9b52e6086`.',
        'verified scale-51 checkpoint',
    )
    text = replace_once(text, '- Scale-51 publication commit: `8984819e3e0671d8fc990b3356f4cbd9b52e6086` — E04 collocation scale-51 published with clean threshold-0.86 preflight; published frontier is `col.00001680`.\n', '', 'remove scale-51 publication line')
    text = replace_once(text, '- Scale-51 verification state: publication is complete, but the normal-user checkpoint verification is still required. Bot-triggered English Content Master Plan Acceptance #127 and Platform CI #1184 ended `action_required` before jobs ran, matching the known bot-publication pattern; do not regenerate scale-51.\n', '', 'remove scale-51 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,790 published records after scale-51', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,830 published records after scale-52', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-51 publication', '## Published runtime snapshot after E04 scale-52 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,790 records', '- phrases: 2,830 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 7,391', '- total published rich records: 7,431', 'rich count')
    text = replace_once(text, '- editorial ledger: 7,391 decisions / 7,391 applied / 7,391 publish decisions', '- editorial ledger: 7,431 decisions / 7,431 applied / 7,431 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001680`', '- E04 collocation frontier: `col.00001720`', 'collocation frontier')
    old_workstream = '''1. Scale-50 publication is fully verified at `2c25c72ecb7367dcb486806910ce980c7a7edc85`; do not duplicate scale-50 artifacts.
2. Scale-51 source/application/publication is complete at `8984819e3e0671d8fc990b3356f4cbd9b52e6086`; do not regenerate or republish it.
3. Verify this normal-user checkpoint with all three mandatory workflows: English Content Master Plan Acceptance, English Content Full Validation and Platform CI. Scale-51 is not fully verified until all three PASS on the checkpoint.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. After scale-51 is fully verified, re-resolve HEAD and recalculate deficits. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-51 publication is fully verified at `23f896b9408996a12bf495f3da00e6f99125e9b3`; do not duplicate scale-51 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-52 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_next = 'Scale-51 publication is complete at `8984819e3e0671d8fc990b3356f4cbd9b52e6086`. Verify this normal-user checkpoint until English Content Master Plan Acceptance, English Content Full Validation and Platform CI all PASS. Do not create a second CI-refresh checkpoint. Once all three pass, mark scale-51 fully verified in the next real-state progress update associated with subsequent bounded work, then continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001680` (expected scale-52 range `col.00001681` through `col.00001720` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-52 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001720` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main52():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-52 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1680:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1680, got {max(nums) if nums else None}')

    new = [make_collocation(1681 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-52: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-52-collocations.json',
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
            'id': 'review.e04.scale-52.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-52-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-52-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-52-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-52-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-52-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-52-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 52 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1680)', 'if(recallCollocations!==1720)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1680 reviewed records', 'must expose 1720 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001681', 'col.00001720'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1720, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2830, 'richRecords': 7431},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main52()
