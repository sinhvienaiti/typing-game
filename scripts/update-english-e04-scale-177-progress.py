#!/usr/bin/env python3
from pathlib import Path
import runpy
ROOT=Path(__file__).resolve().parents[1]
s=runpy.run_path(str(ROOT/'scripts/english-e04-scale-177-common.py'),run_name='e04_scale177_progress')
replace_once=s['replace_once']; path=s['PROGRESS_PATH']; text=path.read_text(encoding='utf-8')
repls=[
('- Latest bot publication commit: `0af400dcc97be0de6d99bb08ec84c92980ef1ba9` — `feat(content): publish E04 phrase scale 176`.','- Latest fully CI-verified scale-up checkpoint before scale-177 publication: `8fa3de0a218df42405c2cd6f393d6a8b147edd54` — scale-176 publication state verified by English Content Full Validation #545, English Content Master Plan Acceptance #676 and Platform CI #1886; published output: `0af400dcc97be0de6d99bb08ec84c92980ef1ba9`.','verified scale-176 checkpoint'),
('- Scale-176 publication checkpoint `8fa3de0a218df42405c2cd6f393d6a8b147edd54` is fully verified by English Content Full Validation #545, English Content Master Plan Acceptance #676 and Platform CI #1886.','- Scale-176 publication checkpoint `8fa3de0a218df42405c2cd6f393d6a8b147edd54` is fully verified; scale-177 is the active publication unit.','scale-177 publication state'),
('- Scale-177 is the current first-unfinished E04 publication unit.','- Scale-177 source/apply publication is active; after bot publication create exactly one normal-user checkpoint before opening scale-178.','first unfinished state'),
('- E04 phrase/pattern architecture + current reviewed publication: complete — 7,790 published records after scale-176','- E04 phrase/pattern architecture + current reviewed publication: complete — 7,830 published records after scale-177','E04 publication count'),
('## Published runtime snapshot after E04 scale-176 publication','## Published runtime snapshot after E04 scale-177 publication','runtime heading'),
('- phrases: 7,790 records','- phrases: 7,830 records','phrase count'),
('- total published rich records: 12,391','- total published rich records: 12,431','rich count'),
('- editorial ledger: 12,391 decisions / 12,391 applied / 12,391 publish decisions','- editorial ledger: 12,431 decisions / 12,431 applied / 12,431 publish decisions','ledger count'),
('- E04 phrasal-verb frontier: `pv.00000720`','- E04 phrasal-verb frontier: `pv.00000730`','pv frontier'),
('- E04 chunk frontier: `chunk.00000795`','- E04 chunk frontier: `chunk.00000810`','chunk frontier'),
('- E04 idiom frontier: `idiom.00000765`','- E04 idiom frontier: `idiom.00000780`','idiom frontier'),
('   - phrasal verbs: 1,000+; current frontier is 720, leaving a minimum deficit of 280;','   - phrasal verbs: 1,000+; current frontier is 730, leaving a minimum deficit of 270;','phrasal deficit'),
('2. Scale-177 is the current publication unit; do not start another E04 batch until its publication/checkpoint CI completes.','2. Scale-177 is the active publication unit; do not start scale-178 until its bot publication, one normal-user checkpoint and all three mandatory CI gates complete.','current workstream'),
('3. Scale-177 uses the next bounded 40-record phrase batch: 10 phrasal verbs + 15 chunks + 15 idioms, with frontier lease `pv.00000720` / `chunk.00000795` / `idiom.00000765` and near-dedupe threshold `0.86` unchanged.','3. Scale-177 adds the bounded 40-record phrase batch: 10 phrasal verbs + 15 chunks + 15 idioms, advancing the expected publication frontiers to `pv.00000730` / `chunk.00000810` / `idiom.00000780`; near-dedupe threshold remains `0.86`.','scale-177 frontiers'),
('Run Scale-177 preflight against the full current E04 corpus. Resolve only exact/near-duplicate offenders without changing the `0.86` threshold or clean candidates. Then drive apply → review/license → generate/publish → full quality gates → deterministic verification → bot publication → one normal-user checkpoint → English Content Full Validation + Master Plan Acceptance + Platform CI. If all PASS, continue from the resulting live frontiers into the next bounded E04 unit.','Finish the active Scale-177 apply/publish pipeline through deterministic verification and bot publication. Then create exactly one normal-user tree-identical checkpoint and verify English Content Full Validation + Master Plan Acceptance + Platform CI on that checkpoint. If all three PASS, open Scale-178 from the resulting live frontiers without changing the `0.86` threshold.','next task')]
for old,new,label in repls: text=replace_once(text,old,new,label)
path.write_text(text,encoding='utf-8')
