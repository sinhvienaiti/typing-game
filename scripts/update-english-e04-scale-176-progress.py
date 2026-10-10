#!/usr/bin/env python3
from pathlib import Path
import runpy
ROOT=Path(__file__).resolve().parents[1]
s=runpy.run_path(str(ROOT/'scripts/english-e04-scale-176-common.py'),run_name='e04_scale176_progress')
replace_once=s['replace_once']; path=s['PROGRESS_PATH']; text=path.read_text(encoding='utf-8')
repls=[
('- Latest bot publication commit: `80ec239390c0db63b48bf397f148f1c64d932b1e` — `feat(content): publish E04 phrase scale 175`.','- Latest fully CI-verified scale-up checkpoint before scale-176 publication: `abcfdc87b863a2ffd9d508e2a93669fe53738f70` — scale-175 publication state verified by English Content Master Plan Acceptance #668, English Content Full Validation #538 and Platform CI #1878; published output: `80ec239390c0db63b48bf397f148f1c64d932b1e`.','verified scale-175 checkpoint'),
('- Scale-175 publication has completed all apply-workflow gates; this normal-user checkpoint must be verified by English Content Full Validation, English Content Master Plan Acceptance and Platform CI before the next E04 batch is opened.','- Scale-175 publication checkpoint `abcfdc87b863a2ffd9d508e2a93669fe53738f70` is fully verified; scale-176 is the current publication unit.','scale-176 publication state'),
('- E04 phrase/pattern architecture + current reviewed publication: complete — 7,750 published records after scale-175','- E04 phrase/pattern architecture + current reviewed publication: complete — 7,790 published records after scale-176','E04 publication count'),
('## Published runtime snapshot after E04 scale-175 publication','## Published runtime snapshot after E04 scale-176 publication','runtime heading'),
('- phrases: 7,750 records','- phrases: 7,790 records','phrase count'),
('- total published rich records: 12,351','- total published rich records: 12,391','rich count'),
('- editorial ledger: 12,351 decisions / 12,351 applied / 12,351 publish decisions','- editorial ledger: 12,391 decisions / 12,391 applied / 12,391 publish decisions','ledger count'),
('- E04 phrasal-verb frontier: `pv.00000710`','- E04 phrasal-verb frontier: `pv.00000720`','pv frontier'),
('- E04 chunk frontier: `chunk.00000780`','- E04 chunk frontier: `chunk.00000795`','chunk frontier'),
('- E04 idiom frontier: `idiom.00000750`','- E04 idiom frontier: `idiom.00000765`','idiom frontier'),
('   - phrasal verbs: 1,000+; current frontier is 710, leaving a minimum deficit of 290;','   - phrasal verbs: 1,000+; current frontier is 720, leaving a minimum deficit of 280;','phrasal deficit'),
('1. Scale-175 bot publication is complete at `80ec239390c0db63b48bf397f148f1c64d932b1e`; do not duplicate scale-175 artifacts.','1. Scale-175 publication checkpoint `abcfdc87b863a2ffd9d508e2a93669fe53738f70` is fully verified; do not duplicate scale-175 artifacts.','verified workstream'),
('2. Verify this single normal-user checkpoint with English Content Full Validation, Master Plan Acceptance and Platform CI.','2. Scale-176 is the current publication unit; do not start another E04 batch until its publication/checkpoint CI completes.','current workstream'),
('3. After all three mandatory CI workflows PASS, recalculate deficits from the resulting HEAD and open the next bounded E04 unit (Scale-176) for under-target phrasal verbs, idioms and chunks unless safer reviewed enrichment has become available.','3. After the scale-176 bot publication commit is created, create exactly one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.','checkpoint workstream'),
('5. Reuse the established scale-up workflow and keep the batch bounded; preserve exact/near-dedupe, provenance, review, deterministic publication and runtime gates.','5. Scale-176 continues the under-target phrase families with 10 reviewed phrasal verbs, 15 chunks and 15 idioms. After its checkpoint, recalculate deficits from HEAD and continue another bounded phrasal-verb/idiom/chunk batch unless safer reviewed enrichment becomes available.','next family'),
('Verify this Scale-175 normal-user checkpoint against English Content Full Validation, English Content Master Plan Acceptance and Platform CI. Once all three PASS, continue immediately with Scale-176: recalculate live deficits from HEAD, use the next safe IDs after `pv.00000710`, `chunk.00000780` and `idiom.00000750`, generate one bounded reviewed batch, run exact/near dedupe before publication, and drive the full apply/publish/CI pipeline to completion.','Scale-176 is the current publication unit. After its bot publication commit is created, verify remote HEAD and create exactly one normal-user checkpoint. If all mandatory CI PASS, continue the under-target phrase families from frontiers `pv.00000720`, `chunk.00000795` and `idiom.00000765` with another bounded reviewed batch. Recalculate counts and run exact/near dedupe before every write.','next task')]
for old,new,label in repls: text=replace_once(text,old,new,label)
path.write_text(text,encoding='utf-8')
