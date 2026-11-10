#!/usr/bin/env python3
from __future__ import annotations
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
base = runpy.run_path(str(ROOT / 'scripts/english-e04-scale-71-common.py'), run_name='e04_scale71_progress')
replace_once = base['replace_once']
path = base['PROGRESS_PATH']
text = path.read_text(encoding='utf-8')
replacements = [
('- Latest fully CI-verified scale-up checkpoint before scale-70 publication: `960ae1e512f91e9d852c6a63a5c1470958586534` — scale-69 publication state verified by English Content Master Plan Acceptance #185, English Content Full Validation #160 and Platform CI #1325; published output: `ee6723e664d7aed5d7dad8d3f1ffd7652e00a431`.', '- Latest fully CI-verified scale-up checkpoint before scale-71 publication: `f23b0b4936137b4ae66e195b63d2caeefbbae7d6` — scale-70 publication state verified by English Content Master Plan Acceptance #188, English Content Full Validation #163 and Platform CI #1328; published output: `39cc4ceac5f59cb996d0f9e28dc14c2f49d859f6`.', 'verified scale-70 checkpoint'),
('- Scale-70 publication commit: `39cc4ceac5f59cb996d0f9e28dc14c2f49d859f6`; bot-triggered English Content Master Plan Acceptance #187 and Platform CI #1327 ended `action_required` before jobs ran, so one normal-user checkpoint and its three mandatory CI gates are the current verification step.', '- Scale-70 publication checkpoint `f23b0b4936137b4ae66e195b63d2caeefbbae7d6` is fully verified; scale-71 is the current publication unit.', 'scale-70 verification state'),
('- E04 phrase/pattern architecture + current reviewed publication: complete — 3,550 published records after scale-70', '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,590 published records after scale-71', 'E04 publication count'),
('## Published runtime snapshot after E04 scale-70 publication', '## Published runtime snapshot after E04 scale-71 publication', 'runtime heading'),
('- phrases: 3,550 records', '- phrases: 3,590 records', 'phrase count'),
('- total published rich records: 8,151', '- total published rich records: 8,191', 'rich count'),
('- editorial ledger: 8,151 decisions / 8,151 applied / 8,151 publish decisions', '- editorial ledger: 8,191 decisions / 8,191 applied / 8,191 publish decisions', 'ledger count'),
('- E04 collocation frontier: `col.00002440`', '- E04 collocation frontier: `col.00002480`', 'frontier'),
('1. Scale-69 publication is fully verified at `960ae1e512f91e9d852c6a63a5c1470958586534`; do not duplicate scale-69 artifacts.', '1. Scale-70 publication is fully verified at `f23b0b4936137b4ae66e195b63d2caeefbbae7d6`; do not duplicate scale-70 artifacts.', 'verified workstream'),
('2. Scale-70 publication is complete at `39cc4ceac5f59cb996d0f9e28dc14c2f49d859f6`; do not regenerate or duplicate scale-70 artifacts.', '2. Scale-71 is the current publication unit; do not start another collocation batch until its publication/checkpoint CI completes.', 'current workstream'),
('3. Create exactly one normal-user checkpoint for scale-70 and verify English Content Full Validation, Master Plan Acceptance and Platform CI on that checkpoint SHA.', '3. After the scale-71 bot publication commit is created, create one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.', 'checkpoint workstream'),
('5. If no safer pending enrichment appears after the scale-70 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002440`, expected IDs `col.00002441`–`col.00002480`, with fresh exact/near-dedupe preflight before any source apply.', '5. If no safer pending enrichment appears after the scale-71 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002480`, expected IDs `col.00002481`–`col.00002520`, with fresh exact/near-dedupe preflight before any source apply.', 'next batch'),
('Create the single normal-user checkpoint for scale-70 publication `39cc4ceac5f59cb996d0f9e28dc14c2f49d859f6` and verify English Content Full Validation, Master Plan Acceptance and Platform CI. If all three PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002440` (expected next range `col.00002441`–`col.00002480`, unless a safer under-target E04 family takes priority). Recalculate counts and run exact/near dedupe before every write.', 'Scale-71 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002480` (expected next range `col.00002481`–`col.00002520`, unless a safer under-target E04 family takes priority). Recalculate counts and run exact/near dedupe before every write.', 'next task'),
]
for old, new, label in replacements:
    text = replace_once(text, old, new, label)
path.write_text(text, encoding='utf-8')
