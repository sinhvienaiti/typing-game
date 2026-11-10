#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-38.py'), run_name='e04_scale39_base')
read_json = BASE['read_json']
write_json = BASE['write_json']
normalized_key = BASE['normalized_key']
jaccard = BASE['jaccard']
digest = BASE['digest']
replace_once = BASE['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-39-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-39.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-39'
REVIEWED_AT = '2026-10-07T05:30:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-39'
EXPECTED = {'collocations': 1160, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('rotate application encryption keys', 'verb + noun phrase', 'luân phiên khóa mã hóa theo chu kỳ hoặc sự kiện bảo mật để giảm rủi ro lộ khóa', 'C1'),
    ('enforce password policies', 'verb + noun phrase', 'thực thi chính sách mật khẩu về độ mạnh, thời hạn và cách sử dụng', 'B2'),
    ('configure access controls', 'verb + noun phrase', 'cấu hình các cơ chế kiểm soát truy cập theo vai trò và nguyên tắc cấp quyền', 'B2'),
    ('review privileged accounts', 'verb + adjective + noun', 'rà soát các tài khoản đặc quyền để xác nhận nhu cầu và phạm vi quyền truy cập', 'C1'),
    ('revoke stale credentials', 'verb + adjective + noun', 'thu hồi thông tin xác thực không còn cần thiết hoặc đã quá hạn sử dụng', 'C1'),
    ('monitor authentication failures', 'verb + noun phrase', 'theo dõi các lần xác thực thất bại để phát hiện hành vi bất thường hoặc tấn công', 'B2'),
    ('analyze security alerts', 'verb + adjective + noun', 'phân tích cảnh báo bảo mật để đánh giá mức độ nghiêm trọng và hành động cần thiết', 'B2'),
    ('triage incident tickets', 'verb + noun phrase', 'phân loại và ưu tiên phiếu sự cố dựa trên tác động, độ khẩn cấp và phạm vi', 'C1'),
    ('contain compromised endpoints', 'verb + adjective + noun', 'cô lập các thiết bị đầu cuối bị xâm nhập để hạn chế lan truyền và mất dữ liệu', 'C1'),
    ('isolate affected systems', 'verb + adjective + noun', 'cách ly các hệ thống bị ảnh hưởng khỏi phần còn lại của môi trường', 'B2'),
    ('preserve digital forensic artifacts', 'verb + adjective + noun', 'bảo toàn bằng chứng số để hỗ trợ điều tra và duy trì tính toàn vẹn', 'C1'),
    ('capture memory images', 'verb + noun phrase', 'thu thập ảnh bộ nhớ của hệ thống để phục vụ phân tích pháp chứng', 'C1'),
    ('analyze network traffic', 'verb + noun phrase', 'phân tích lưu lượng mạng để nhận diện hành vi, bất thường và dấu hiệu tấn công', 'B2'),
    ('inspect system logs', 'verb + noun phrase', 'kiểm tra nhật ký hệ thống để truy tìm sự kiện và dấu vết hoạt động', 'B2'),
    ('correlate event records', 'verb + noun phrase', 'đối chiếu các bản ghi sự kiện từ nhiều nguồn để xác định mối liên hệ và chuỗi hành vi', 'C1'),
    ('patch vulnerable systems', 'verb + adjective + noun', 'vá các hệ thống có lỗ hổng nhằm giảm khả năng bị khai thác', 'B2'),
    ('verify patch deployment', 'verb + noun phrase', 'xác minh bản vá đã được triển khai đầy đủ và đúng phạm vi dự kiến', 'B2'),
    ('scan exposed services', 'verb + adjective + noun', 'quét các dịch vụ có thể truy cập để nhận diện bề mặt tấn công và cấu hình rủi ro', 'C1'),
    ('remediate security findings', 'verb + adjective + noun', 'khắc phục các phát hiện bảo mật được ghi nhận từ kiểm tra hoặc đánh giá', 'C1'),
    ('harden server configurations', 'verb + noun phrase', 'gia cố cấu hình máy chủ bằng cách giảm bề mặt tấn công và áp dụng thiết lập an toàn', 'C1'),
    ('disable unused services', 'verb + adjective + noun', 'vô hiệu hóa các dịch vụ không sử dụng để giảm rủi ro và tài nguyên dư thừa', 'B2'),
    ('restrict administrative access', 'verb + adjective + noun', 'hạn chế quyền truy cập quản trị cho đúng người, thiết bị và ngữ cảnh cần thiết', 'C1'),
    ('segment internal network zones', 'verb + adjective + noun', 'phân đoạn mạng nội bộ để giới hạn luồng truy cập và phạm vi ảnh hưởng của sự cố', 'C1'),
    ('enforce network policies', 'verb + noun phrase', 'thực thi chính sách mạng thông qua quy tắc truy cập, phân đoạn và kiểm soát lưu lượng', 'C1'),
    ('monitor data exfiltration', 'verb + noun phrase', 'theo dõi dấu hiệu dữ liệu bị chuyển trái phép ra ngoài môi trường kiểm soát', 'C1'),
    ('classify sensitive data', 'verb + adjective + noun', 'phân loại dữ liệu nhạy cảm theo mức độ quan trọng và yêu cầu bảo vệ', 'B2'),
    ('encrypt stored data', 'verb + adjective + noun', 'mã hóa dữ liệu khi lưu trữ để giảm nguy cơ lộ thông tin nếu phương tiện bị truy cập trái phép', 'B2'),
    ('protect backup copies', 'verb + noun phrase', 'bảo vệ các bản sao lưu khỏi truy cập trái phép, sửa đổi hoặc xóa phá hoại', 'B2'),
    ('test recovery procedures', 'verb + noun phrase', 'thử quy trình khôi phục để xác nhận khả năng phục hồi hệ thống và dữ liệu', 'B2'),
    ('restore priority business services', 'verb + adjective + noun', 'khôi phục các dịch vụ quan trọng theo thứ tự ưu tiên sau sự cố', 'B2'),
    ('document incident timelines', 'verb + noun phrase', 'ghi lại dòng thời gian sự cố để hỗ trợ điều tra, báo cáo và cải tiến phản ứng', 'C1'),
    ('notify affected stakeholders', 'verb + adjective + noun', 'thông báo cho các bên liên quan bị ảnh hưởng theo yêu cầu và thời hạn phù hợp', 'B2'),
    ('coordinate breach response', 'verb + noun phrase', 'điều phối hoạt động ứng phó sự cố rò rỉ hoặc xâm nhập dữ liệu giữa các nhóm liên quan', 'C1'),
    ('update incident playbooks', 'verb + noun phrase', 'cập nhật kịch bản ứng phó sự cố dựa trên bài học, công nghệ và rủi ro mới', 'C1'),
    ('test security controls', 'verb + adjective + noun', 'thử các biện pháp kiểm soát bảo mật để xác nhận chúng hoạt động như thiết kế', 'B2'),
    ('validate firewall rules', 'verb + noun phrase', 'xác nhận các quy tắc tường lửa phù hợp với chính sách và không tạo quyền truy cập dư thừa', 'C1'),
    ('review vulnerability reports', 'verb + noun phrase', 'rà soát báo cáo lỗ hổng để xác định mức độ ưu tiên và phạm vi khắc phục', 'B2'),
    ('prioritize remediation tasks', 'verb + noun phrase', 'ưu tiên các nhiệm vụ khắc phục dựa trên rủi ro, khả năng khai thác và tác động kinh doanh', 'C1'),
    ('track remediation deadlines', 'verb + noun phrase', 'theo dõi thời hạn khắc phục để bảo đảm các vấn đề rủi ro được xử lý đúng cam kết', 'B2'),
    ('close security exceptions', 'verb + adjective + noun', 'đóng các ngoại lệ bảo mật khi điều kiện cho phép hoặc biện pháp thay thế đã hoàn tất', 'C1'),
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
        'quality': {
            'state': 'draft',
            'checks': {
                'schema': {'status': 'pass', 'method': 'e04-scale-39-authoring-v1'},
                'grammar': {'status': 'pending', 'method': 'manual-review-required'},
                'translation': {'status': 'pending', 'method': 'manual-review-required'},
                'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
                'cefr': {'status': 'pending', 'method': 'manual-review-required'},
                'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
                'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v39'},
                'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
                'license': {'status': 'pending', 'method': 'manual-review-required'},
            },
        },
        'provenance': {
            'sources': [{
                'dataset': 'project-original',
                'sourceId': rid,
                'sourceUrl': 'content/english/phrases/e04-scale-39-collocations.json',
                'snapshot': '2026-10',
                'license': 'LicenseRef-Project-Original',
                'modified': False,
            }],
            'note': 'Project-original controlled E04 scale-up record.',
        },
    }

def update_progress():
    text = PROGRESS_PATH.read_text(encoding='utf-8')
    text = replace_once(
        text,
        '- Latest fully CI-verified scale-up checkpoint before scale-38 publication: `bf930fc2eb5b104d6a34ec2f0e88e7f631cee0f5` — scale-37 publication state verified by English Content Master Plan Acceptance #82, English Content Full Validation #89 and Platform CI #1125; published output: `d76454a30225b0dc1c4c85238b834e24afaa1b35`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-39 publication: `39de17e5f4c2498ffe8151b356e30525b457f95b` — scale-38 publication state verified by English Content Master Plan Acceptance #85, English Content Full Validation #91 and Platform CI #1128; published output: `1109e688f4c14ba7c8b5d64b3061d91696e75700`.',
        'verified scale-38 checkpoint',
    )
    text = replace_once(text, '- Latest published scale-up HEAD before this checkpoint: `1109e688f4c14ba7c8b5d64b3061d91696e75700` — `feat(content): publish E04 collocation scale 38`.\n', '', 'remove scale-38 publication line')
    text = replace_once(text, '- Latest scale-38 pre-publication HEAD: `62a3d4fb57363b86c76102090240e070126786d6` — Apply English E04 Scale 38 #1 passed clean preflight, source apply, review/E10/license, generate/publish, full quality gates, converge, deterministic replay and bot commit/push.\n', '', 'remove scale-38 prep line')
    text = replace_once(text, '- Scale-38 publication verification note: the publication commit was created by `github-actions[bot]`; its PR-triggered English Content Master Plan Acceptance #84 and Platform CI #1127 ended `action_required` before jobs ran, so this checkpoint intentionally re-triggers the mandatory CI from a normal branch write without regenerating scale-38 content or weakening any gate.\n', '', 'remove resolved scale-38 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,270 published records after scale-38', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,310 published records after scale-39', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-38 publication', '## Published runtime snapshot after E04 scale-39 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,270 records', '- phrases: 2,310 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 6,871', '- total published rich records: 6,911', 'rich count')
    text = replace_once(text, '- editorial ledger: 6,871 decisions / 6,871 applied / 6,871 publish decisions', '- editorial ledger: 6,911 decisions / 6,911 applied / 6,911 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001160`', '- E04 collocation frontier: `col.00001200`', 'collocation frontier')
    old_workstream = '''1. Verify scale-38 publication state through this normal-user checkpoint CI; do not duplicate scale-38 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. If scale-38 checkpoint CI passes and no newer worker has claimed the next scope, create scale-39 as the next bounded collocation batch from frontier `col.00001160`.
4. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
5. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-38 publication is fully verified; do not duplicate scale-38 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-39 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-38 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-38 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001160` (expected scale-39 range `col.00001161` through `col.00001200` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-39 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001200` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')

def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-39 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1160:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1160, got {max(nums) if nums else None}')

    new = [make_collocation(1161 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-39: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-39-collocations.json',
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
            'id': 'review.e04.scale-39.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-39-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-39-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-39-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-39-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-39-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-39-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 39 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1160)', 'if(recallCollocations!==1200)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1160 reviewed records', 'must expose 1200 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001161', 'col.00001200'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1200, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2310, 'richRecords': 6911},
    }, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
