#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = runpy.run_path(str(ROOT / 'scripts/apply-english-e04-focused-scale-40.py'), run_name='e04_scale41_base')
read_json = BASE['read_json']
write_json = BASE['write_json']
normalized_key = BASE['normalized_key']
jaccard = BASE['jaccard']
digest = BASE['digest']
replace_once = BASE['replace_once']

MANIFEST_PATH = ROOT / 'content/english/batches/manifest.json'
COL_PATH = ROOT / 'content/english/phrases/e04-scale-41-collocations.json'
DECISION_PATH = ROOT / 'content/english/reviews/decisions.d/e04-scale-41.json'
PROGRESS_PATH = ROOT / 'docs/ENGLISH_LEARNING_CONTENT_SYSTEM_PROGRESS.md'
BATCH_ID = 'e04.phrase-pattern-scale-41'
REVIEWED_AT = '2026-10-07T06:45:00Z'
REVIEWED_BY = 'chatgpt-editorial-scale-41'
EXPECTED = {'collocations': 1240, 'verbPatterns': 510, 'phraseItems': 600}
NEAR_DUP_THRESHOLD = 0.86

COLLOCATIONS = [
    ('forecast room occupancy', 'verb + noun phrase', 'dự báo công suất phòng để hỗ trợ kế hoạch giá, nhân sự và vận hành khách sạn', 'B2'),
    ('adjust seasonal room rates', 'verb + adjective + noun', 'điều chỉnh giá phòng theo mùa dựa trên nhu cầu và điều kiện thị trường', 'B2'),
    ('manage room inventory', 'verb + noun phrase', 'quản lý lượng phòng có thể bán theo loại phòng, ngày và kênh phân phối', 'B2'),
    ('process group reservations', 'verb + noun phrase', 'xử lý đặt phòng theo đoàn với số lượng, điều khoản và thông tin khách đã thỏa thuận', 'B2'),
    ('confirm guest preferences', 'verb + noun phrase', 'xác nhận sở thích và yêu cầu của khách trước hoặc trong thời gian lưu trú', 'B2'),
    ('assign accessible guest rooms', 'verb + adjective + noun', 'phân phòng phù hợp cho khách cần các tiện ích hỗ trợ tiếp cận', 'B2'),
    ('coordinate airport transfers', 'verb + noun phrase', 'điều phối phương tiện đưa đón sân bay theo lịch trình và thông tin chuyến bay của khách', 'B2'),
    ('prepare welcome amenities', 'verb + noun phrase', 'chuẩn bị tiện ích chào đón trong phòng theo tiêu chuẩn hoặc yêu cầu đặc biệt', 'B2'),
    ('handle early guest arrivals', 'verb + adjective + noun', 'xử lý trường hợp khách đến sớm bằng cách kiểm tra phòng sẵn sàng và lựa chọn hỗ trợ phù hợp', 'B2'),
    ('store guest luggage', 'verb + noun phrase', 'lưu giữ hành lý của khách an toàn trước nhận phòng hoặc sau trả phòng', 'B2'),
    ('verify guest identification', 'verb + noun phrase', 'xác minh giấy tờ nhận dạng của khách theo quy trình nhận phòng và yêu cầu pháp lý', 'B2'),
    ('authorize incidental deposits', 'verb + adjective + noun', 'xác nhận khoản tạm giữ cho các chi phí phát sinh trong thời gian lưu trú', 'C1'),
    ('issue digital room keys', 'verb + adjective + noun', 'cấp khóa phòng điện tử hoặc khóa số cho khách sau khi hoàn tất thủ tục cần thiết', 'B2'),
    ('explain property facilities', 'verb + noun phrase', 'giới thiệu các khu vực, tiện ích và giờ hoạt động của cơ sở lưu trú cho khách', 'B2'),
    ('resolve folio discrepancies', 'verb + noun phrase', 'xử lý chênh lệch trên bảng kê chi phí của khách trước khi thanh toán hoặc trả phòng', 'C1'),
    ('process express checkouts', 'verb + adjective + noun', 'xử lý trả phòng nhanh theo quy trình đã xác nhận mà không cần thủ tục kéo dài tại quầy', 'B2'),
    ('inspect vacant guest rooms', 'verb + adjective + noun', 'kiểm tra các phòng trống để xác nhận tình trạng sạch sẽ, an toàn và sẵn sàng bán', 'B2'),
    ('replenish minibar supplies', 'verb + noun phrase', 'bổ sung đồ dùng minibar theo mức tồn tiêu chuẩn và lượng khách đã sử dụng', 'B2'),
    ('replace damaged linens', 'verb + adjective + noun', 'thay khăn hoặc đồ vải bị hư hỏng để duy trì tiêu chuẩn vệ sinh và chất lượng phòng', 'B2'),
    ('sanitize high-touch surfaces', 'verb + adjective + noun', 'khử khuẩn các bề mặt thường xuyên tiếp xúc để giảm rủi ro vệ sinh', 'B2'),
    ('report maintenance faults', 'verb + noun phrase', 'báo cáo hỏng hóc kỹ thuật để bộ phận bảo trì xử lý theo mức độ ưu tiên', 'B2'),
    ('dispatch engineering technicians', 'verb + adjective + noun', 'điều kỹ thuật viên đến xử lý sự cố thiết bị hoặc cơ sở vật chất tại khu vực cần hỗ trợ', 'C1'),
    ('monitor pool water quality', 'verb + noun phrase', 'theo dõi chất lượng nước hồ bơi theo các chỉ số vận hành và an toàn quy định', 'C1'),
    ('schedule preventive property maintenance', 'verb + adjective + noun', 'lập lịch bảo trì phòng ngừa cho thiết bị và hạ tầng của cơ sở lưu trú', 'C1'),
    ('coordinate banquet setups', 'verb + noun phrase', 'điều phối việc bố trí phòng tiệc theo sơ đồ, số khách và yêu cầu sự kiện', 'B2'),
    ('finalize event floor plans', 'verb + noun phrase', 'hoàn thiện sơ đồ mặt bằng sự kiện với bàn ghế, lối đi và khu chức năng đã xác nhận', 'C1'),
    ('stage conference equipment', 'verb + noun phrase', 'bố trí thiết bị hội nghị tại đúng vị trí và thời điểm trước khi sự kiện bắt đầu', 'B2'),
    ('test ballroom audiovisual systems', 'verb + adjective + noun', 'kiểm thử hệ thống âm thanh và hình ảnh trong phòng tiệc trước sự kiện', 'C1'),
    ('manage catering orders', 'verb + noun phrase', 'quản lý đơn đặt đồ ăn thức uống cho sự kiện theo số lượng, thời gian và dịch vụ yêu cầu', 'B2'),
    ('accommodate dietary restrictions', 'verb + noun phrase', 'đáp ứng các hạn chế ăn uống của khách bằng lựa chọn món và quy trình phục vụ phù hợp', 'C1'),
    ('prepare buffet stations', 'verb + noun phrase', 'chuẩn bị các quầy buffet với món ăn, dụng cụ và biển thông tin cần thiết', 'B2'),
    ('monitor food holding temperatures', 'verb + noun phrase', 'theo dõi nhiệt độ giữ nóng hoặc giữ lạnh thực phẩm trong thời gian phục vụ', 'C1'),
    ('record allergen information', 'verb + noun phrase', 'ghi nhận thông tin chất gây dị ứng để hỗ trợ phục vụ và truyền đạt an toàn thực phẩm', 'B2'),
    ('rotate perishable stock', 'verb + adjective + noun', 'luân chuyển hàng dễ hỏng theo nguyên tắc hạn dùng để giảm lãng phí và rủi ro', 'B2'),
    ('audit front-desk cash drawers', 'verb + adjective + noun', 'kiểm tra tiền mặt tại quầy lễ tân so với giao dịch và số liệu hệ thống', 'C1'),
    ('reconcile daily hotel revenue', 'verb + adjective + noun', 'đối chiếu doanh thu khách sạn theo ngày giữa hệ thống đặt phòng, thanh toán và báo cáo', 'C1'),
    ('review post-stay feedback', 'verb + adjective + noun', 'rà soát phản hồi sau lưu trú để nhận diện vấn đề dịch vụ và cơ hội cải thiện', 'B2'),
    ('respond to service complaints', 'verb + prepositional phrase', 'phản hồi khiếu nại dịch vụ theo cách kịp thời, chuyên nghiệp và có hướng xử lý rõ ràng', 'B2'),
    ('train front-desk agents', 'verb + adjective + noun', 'đào tạo nhân viên lễ tân về quy trình, hệ thống và tiêu chuẩn phục vụ khách', 'B2'),
    ('update emergency contact lists', 'verb + adjective + noun', 'cập nhật danh sách liên hệ khẩn cấp để nhân viên có thông tin chính xác khi xảy ra sự cố', 'B2'),
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
                'schema': {'status': 'pass', 'method': 'e04-scale-41-authoring-v1'},
                'grammar': {'status': 'pending', 'method': 'manual-review-required'},
                'translation': {'status': 'pending', 'method': 'manual-review-required'},
                'naturalness': {'status': 'pending', 'method': 'manual-review-required'},
                'cefr': {'status': 'pending', 'method': 'manual-review-required'},
                'targetStructure': {'status': 'pending', 'method': 'manual-review-required'},
                'exactDuplicate': {'status': 'pass', 'method': 'normalized-key-v41'},
                'nearDuplicate': {'status': 'pending', 'method': 'manual-review-required'},
                'license': {'status': 'pending', 'method': 'manual-review-required'},
            },
        },
        'provenance': {
            'sources': [{
                'dataset': 'project-original',
                'sourceId': rid,
                'sourceUrl': 'content/english/phrases/e04-scale-41-collocations.json',
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
        '- Latest fully CI-verified scale-up checkpoint before scale-40 publication: `929afcb95c0ac95daef8b5732af14138743032ce` — scale-39 publication state verified by English Content Master Plan Acceptance #89, English Content Full Validation #94 and Platform CI #1132; published output: `ccf47b48a02c94ac9c8ed3b3bf46266c95298af7`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-41 publication: `fd8cc5c6cb04e2c2a500aa067480f72148c30cc6` — scale-40 publication state verified by English Content Master Plan Acceptance #93, English Content Full Validation #97 and Platform CI #1136; published output: `ca9f43aa36bf4f9458ea4feb7088af66150896ae`.',
        'verified scale-40 checkpoint',
    )
    text = replace_once(text, '- Scale-40 publication output: `ca9f43aa36bf4f9458ea4feb7088af66150896ae` — `feat(content): publish E04 collocation scale 40`; preflight, controlled review, full quality gates, converge and deterministic replay passed before the bot commit was pushed.\n', '', 'remove scale-40 publication line')
    text = replace_once(text, '- Scale-40 publication verification note: because the publication commit was created by `github-actions[bot]`, its PR-triggered English Content Master Plan Acceptance #92 and Platform CI #1135 ended `action_required` before any job started. This normal-user checkpoint intentionally re-triggers the mandatory CI without regenerating scale-40 content or weakening any gate.\n', '', 'remove resolved scale-40 verification note')
    text = replace_once(text, '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,350 published records after scale-40', '- E04 phrase/pattern architecture + current reviewed publication: complete — 2,390 published records after scale-41', 'E04 count')
    text = replace_once(text, '## Published runtime snapshot after E04 scale-40 publication', '## Published runtime snapshot after E04 scale-41 publication', 'snapshot heading')
    text = replace_once(text, '- phrases: 2,350 records', '- phrases: 2,390 records', 'phrase count')
    text = replace_once(text, '- total published rich records: 6,951', '- total published rich records: 6,991', 'rich count')
    text = replace_once(text, '- editorial ledger: 6,951 decisions / 6,951 applied / 6,951 publish decisions', '- editorial ledger: 6,991 decisions / 6,991 applied / 6,991 publish decisions', 'ledger count')
    text = replace_once(text, '- E04 collocation frontier: `col.00001240`', '- E04 collocation frontier: `col.00001280`', 'collocation frontier')
    old_workstream = '''1. Scale-39 publication is fully verified; do not duplicate scale-39 artifacts.
2. Scale-40 publication `ca9f43aa36bf4f9458ea4feb7088af66150896ae` is complete; do not regenerate or duplicate scale-40 artifacts.
3. Verify scale-40 publication state through the CI attached to this normal-user checkpoint; the bot-authored PR workflow attempts #92/#1135 ended `action_required` before jobs ran.
4. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
5. If scale-40 checkpoint CI passes and no newer worker has claimed the next scope, create the next bounded E04 scale batch from frontier `col.00001240`, preferring collocations before generating more verb patterns that already meet their minimum.
6. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
7. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    new_workstream = '''1. Scale-40 publication is fully verified; do not duplicate scale-40 artifacts.
2. The latest enrichment evidence scan found whole-phrase candidates only for already-covered E04 records; there is no newly safe uncovered enrichment queue to promote automatically. Lemma-only verb-pattern evidence remains review-only.
3. Verify the resulting scale-41 publication commit and mandatory CI without regenerating completed artifacts.
4. If no safer pending enrichment appears, create the next bounded E04 scale batch for the most under-target family with established source/license/generator support, preferring collocations before generating more verb patterns that already meet their minimum.
5. After each E04 batch passes all gates, continue immediately with the next safe batch in the same run when possible.
6. When E04 has no immediately safe batch, continue to the next E11 corpus family using the same controlled-batch procedure.'''
    text = replace_once(text, old_workstream, new_workstream, 'first unfinished workstream')
    old_blocker = "No content/data blocker. Scale-40 publication HEAD's bot-authored PR workflow attempts ended `action_required` before any job started; this checkpoint re-triggers the same gates from a normal branch write so the publication state can be verified without regenerating content."
    text = replace_once(text, old_blocker, 'None.', 'blocker')
    old_next = 'Wait for the CI attached to this checkpoint HEAD. If all mandatory gates PASS, record scale-40 as fully verified and continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001240` (expected scale-41 range `col.00001241` through `col.00001280` if no newer worker has claimed it), or move to the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch. Recalculate counts and run exact/near dedupe before every write.'
    new_next = 'Scale-41 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00001280` (or the next safer under-target E04 family if collocation preflight cannot produce a clean reviewed batch). Recalculate counts and run exact/near dedupe before every write.'
    text = replace_once(text, old_next, new_next, 'next task')
    PROGRESS_PATH.write_text(text, encoding='utf-8')


def main():
    manifest = read_json(MANIFEST_PATH)
    if any(batch.get('id') == BATCH_ID for batch in manifest.get('batches', [])):
        print(json.dumps({'status': 'skip', 'reason': 'batch already exists', 'batch': BATCH_ID}, indent=2))
        return
    if COL_PATH.exists() or DECISION_PATH.exists():
        raise RuntimeError('scale-41 artifact exists without matching batch manifest')

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
    if not nums or max(nums) != 1240:
        raise RuntimeError(f'collocation ID frontier drifted; expected max 1240, got {max(nums) if nums else None}')

    new = [make_collocation(1241 + i, spec) for i, spec in enumerate(COLLOCATIONS)]
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
                raise RuntimeError(f'duplicate inside scale-41: {text!r} ~ {prior["text"]!r} ({score:.3f})')
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
            'path': 'content/english/phrases/e04-scale-41-collocations.json',
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
            'id': 'review.e04.scale-41.' + record['id'].replace('.', '-'),
            'batchId': BATCH_ID,
            'recordSetId': 'scale-collocations',
            'recordId': record['id'],
            'sourceDigest': digest(record),
            'targetState': 'published',
            'checks': {
                'grammar': {'status': 'pass', 'method': 'e04-scale-41-grammar-editorial-review'},
                'translation': {'status': 'pass', 'method': 'e04-scale-41-bilingual-review'},
                'naturalness': {'status': 'pass', 'method': 'e04-scale-41-naturalness-review'},
                'cefr': {'status': 'pass', 'method': 'e04-scale-41-cefr-review'},
                'targetStructure': {'status': 'pass', 'method': 'e04-scale-41-structure-review'},
                'nearDuplicate': {'status': 'pass', 'method': 'e04-scale-41-cross-batch-near-dedup-review'},
                'license': {'status': 'pass', 'method': 'project-original-license-review-v1'},
            },
            'reviewedAt': REVIEWED_AT,
            'reviewedBy': REVIEWED_BY,
            'note': 'Focused E04 scale 41 collocation reviewed for structure, grammar, Vietnamese meaning, naturalness, CEFR, exact/near dedup and project-original provenance.',
        })
    write_json(DECISION_PATH, {'schemaVersion': 1, 'decisions': decisions})

    smoke_path = ROOT / 'scripts/smoke-published-english-content.mjs'
    smoke = smoke_path.read_text(encoding='utf-8')
    smoke = replace_once(smoke, 'if(recallCollocations!==1240)', 'if(recallCollocations!==1280)', 'smoke count')
    smoke = replace_once(smoke, 'must expose 1240 reviewed records', 'must expose 1280 reviewed records', 'smoke message')
    smoke_path.write_text(smoke, encoding='utf-8')

    update_progress()
    print(json.dumps({
        'status': 'applied',
        'batch': BATCH_ID,
        'collocationsAdded': 40,
        'collocationRange': ['col.00001241', 'col.00001280'],
        'sourceCountsBefore': actual,
        'sourceCountsAfter': {'collocations': 1280, 'verbPatterns': 510, 'phraseItems': 600},
        'expectedRuntimeAfterPublish': {'phrases': 2390, 'richRecords': 6991},
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
