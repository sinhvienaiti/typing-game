#!/usr/bin/env python3
from __future__ import annotations
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
base = runpy.run_path(str(ROOT / 'scripts/english-e04-scale-70-common.py'), run_name='e04_scale70_progress')
replace_once = base['replace_once']
path = base['PROGRESS_PATH']
text = path.read_text(encoding='utf-8')
replacements = [
('- Latest fully CI-verified scale-up checkpoint before scale-69 publication: `a937857a17e8319f5bc734b9bda7c2a92fc02fa2` — scale-68 publication state verified by English Content Master Plan Acceptance #182, English Content Full Validation #158 and Platform CI #1295; published output: `0b117abe1ccdede8b79cc4eaa2bb8c632613a547`.', '- Latest fully CI-verified scale-up checkpoint before scale-70 publication: `960ae1e512f91e9d852c6a63a5c1470958586534` — scale-69 publication state verified by English Content Master Plan Acceptance #185, English Content Full Validation #160 and Platform CI #1325; published output: `ee6723e664d7aed5d7dad8d3f1ffd7652e00a431`.', 'verified scale-69 checkpoint'),
('- Scale-69 publication commit: `ee6723e664d7aed5d7dad8d3f1ffd7652e00a431`; bot-triggered English Content Master Plan Acceptance #184 and Platform CI #1310 ended `action_required` before jobs ran, so one normal-user checkpoint and its three mandatory CI gates are the current verification step.', '- Scale-69 publication checkpoint `960ae1e512f91e9d852c6a63a5c1470958586534` is fully verified; scale-70 is the current publication unit.', 'scale-69 verification state'),
('- E04 phrase/pattern architecture + current reviewed publication: complete — 3,510 published records after scale-69', '- E04 phrase/pattern architecture + current reviewed publication: complete — 3,550 published records after scale-70', 'E04 publication count'),
('## Published runtime snapshot after E04 scale-69 publication', '## Published runtime snapshot after E04 scale-70 publication', 'runtime heading'),
('- phrases: 3,510 records', '- phrases: 3,550 records', 'phrase count'),
('- total published rich records: 8,111', '- total published rich records: 8,151', 'rich count'),
('- editorial ledger: 8,111 decisions / 8,111 applied / 8,111 publish decisions', '- editorial ledger: 8,151 decisions / 8,151 applied / 8,151 publish decisions', 'ledger count'),
('- E04 collocation frontier: `col.00002400`', '- E04 collocation frontier: `col.00002440`', 'frontier'),
('1. Scale-68 publication is fully verified at `a937857a17e8319f5bc734b9bda7c2a92fc02fa2`; do not duplicate scale-68 artifacts.', '1. Scale-69 publication is fully verified at `960ae1e512f91e9d852c6a63a5c1470958586534`; do not duplicate scale-69 artifacts.', 'verified workstream'),
('2. Scale-69 publication is complete at `ee6723e664d7aed5d7dad8d3f1ffd7652e00a431`; do not regenerate or duplicate its artifacts.', '2. Scale-70 is the current publication unit; do not start another collocation batch until its publication/checkpoint CI completes.', 'current workstream'),
('3. Create exactly one normal-user checkpoint for scale-69 and verify English Content Full Validation, Master Plan Acceptance and Platform CI on that checkpoint SHA.', '3. After the scale-70 bot publication commit is created, create one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.', 'checkpoint workstream'),
('5. If no safer pending enrichment appears after the scale-69 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002400`, expected IDs `col.00002401`–`col.00002440`, with fresh exact/near-dedupe preflight before any source apply.', '5. If no safer pending enrichment appears after the scale-70 checkpoint, continue with a bounded E04 collocation batch from frontier `col.00002440`, expected IDs `col.00002441`–`col.00002480`, with fresh exact/near-dedupe preflight before any source apply.', 'next batch'),
('Create the single normal-user checkpoint for scale-69 publication `ee6723e664d7aed5d7dad8d3f1ffd7652e00a431` and verify English Content Full Validation, Master Plan Acceptance and Platform CI. If all three PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002400` (expected next range `col.00002401`–`col.00002440`, unless a safer under-target E04 family takes priority). Recalculate counts and run exact/near dedupe before every write.', 'Scale-70 is the current publication unit. After its bot publication commit is created, verify remote HEAD and all mandatory CI. If PASS, continue immediately with the next genuinely new bounded collocation batch from frontier `col.00002440` (expected next range `col.00002441`–`col.00002480`, unless a safer under-target E04 family takes priority). Recalculate counts and run exact/near dedupe before every write.', 'next task'),
]
for old, new, label in replacements:
    text = replace_once(text, old, new, label)
path.write_text(text, encoding='utf-8')
