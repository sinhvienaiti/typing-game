#!/usr/bin/env python3
from __future__ import annotations

import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_PATH = ROOT / 'scripts/apply-english-e04-focused-scale-49-impl.py'
base = runpy.run_path(str(BASE_PATH), run_name='e04_scale49_fixed_impl')

# Preflight on the first scale-49 prep correctly found that the original
# candidate "process customer returns" already existed as col.00001037.
# Keep the ID slot stable and replace only that candidate; do not weaken dedupe.
base['COLLOCATIONS'][37] = (
    'assess returned merchandise',
    'verb + adjective + noun',
    'đánh giá tình trạng hàng hóa được trả lại để quyết định hoàn kho, sửa chữa, giảm cấp hoặc loại bỏ',
    'B2',
)

# Re-export the implementation contract so the existing preflight can inspect
# the corrected candidate set without duplicating scale-49 logic.
read_json = base['read_json']
write_json = base['write_json']
normalized_key = base['normalized_key']
jaccard = base['jaccard']
digest = base['digest']
replace_once = base['replace_once']
MANIFEST_PATH = base['MANIFEST_PATH']
COL_PATH = base['COL_PATH']
DECISION_PATH = base['DECISION_PATH']
PROGRESS_PATH = base['PROGRESS_PATH']
BATCH_ID = base['BATCH_ID']
REVIEWED_AT = base['REVIEWED_AT']
REVIEWED_BY = base['REVIEWED_BY']
EXPECTED = base['EXPECTED']
NEAR_DUP_THRESHOLD = base['NEAR_DUP_THRESHOLD']
COLLOCATIONS = base['COLLOCATIONS']
make_collocation = base['make_collocation']
update_progress = base['update_progress']
main49 = base['main49']

if __name__ == '__main__':
    main49()
