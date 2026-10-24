#!/usr/bin/env python3
from pathlib import Path
import runpy

ROOT=Path(__file__).resolve().parents[1]
s=runpy.run_path(str(ROOT/'scripts/english-e04-scale-136-common.py'), run_name='e04_scale136_progress')
replace_once=s['replace_once']; path=s['PROGRESS_PATH']; text=path.read_text(encoding='utf-8')
repls=[
('- Latest fully CI-verified scale-up checkpoint before scale-135 publication: `10e1bf9c128164d93b48d88d7b63bd28d16e2c25` — scale-134 publication state verified by English Content Master Plan Acceptance #414, English Content Full Validation #325 and Platform CI #1624; published output: `34ce9e491c465aa4d1b16bb2770f4c12325e535c`.','- Latest fully CI-verified scale-up checkpoint before scale-136 publication: `3424d5b3cf875e44f25b48bffcb095e70d475491` — scale-135 publication state verified by English Content Master Plan Acceptance #418, English Content Full Validation #328 and Platform CI #1628; published output: `75a82b1b9c5a4b87585aec005aa80469143858b5`.','verified scale-135 checkpoint'),
('- Scale-134 publication checkpoint `10e1bf9c128164d93b48d88d7b63bd28d16e2c25` is fully verified; scale-135 is the current publication unit.','- Scale-135 publication checkpoint `3424d5b3cf875e44f25b48bffcb095e70d475491` is fully verified; scale-136 is the current publication unit.','scale-135 verification state'),
('- E04 phrase/pattern architecture + current reviewed publication: complete — 6,150 published records after scale-135','- E04 phrase/pattern architecture + current reviewed publication: complete — 6,190 published records after scale-136','E04 publication count'),
('## Published runtime snapshot after E04 scale-135 publication','## Published runtime snapshot after E04 scale-136 publication','runtime heading'),
('- phrases: 6,150 records','- phrases: 6,190 records','phrase count'),
('- total published rich records: 10,751','- total published rich records: 10,791','rich count'),
('- editorial ledger: 10,751 decisions / 10,751 applied / 10,751 publish decisions','- editorial ledger: 10,791 decisions / 10,791 applied / 10,791 publish decisions','ledger count'),
('- E04 phrasal-verb frontier: `pv.00000310`','- E04 phrasal-verb frontier: `pv.00000320`','pv frontier'),
('- E04 chunk frontier: `chunk.00000180`','- E04 chunk frontier: `chunk.00000195`','chunk frontier'),
('- E04 idiom frontier: `idiom.00000150`','- E04 idiom frontier: `idiom.00000165`','idiom frontier'),
('1. Scale-134 publication is fully verified at `10e1bf9c128164d93b48d88d7b63bd28d16e2c25`; do not duplicate scale-134 artifacts.','1. Scale-135 publication is fully verified at `3424d5b3cf875e44f25b48bffcb095e70d475491`; do not duplicate scale-135 artifacts.','verified workstream'),
('2. Scale-135 is the current publication unit; do not start another E04 batch until its publication/checkpoint CI completes.','2. Scale-136 is the current publication unit; do not start another E04 batch until its publication/checkpoint CI completes.','current workstream'),
('3. After the scale-135 bot publication commit is created, create exactly one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.','3. After the scale-136 bot publication commit is created, create exactly one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.','checkpoint workstream'),
('5. Scale-135 resumes the under-target phrase families with 10 reviewed phrasal verbs, 15 chunks and 15 idioms. After its checkpoint, recalculate deficits from HEAD and continue another bounded phrasal-verb/idiom/chunk batch unless safer reviewed enrichment becomes available.','5. Scale-136 continues the under-target phrase families with 10 reviewed phrasal verbs, 15 chunks and 15 idioms. After its checkpoint, recalculate deficits from HEAD and continue another bounded phrasal-verb/idiom/chunk batch unless safer reviewed enrichment becomes available.','next family'),
('Scale-135 is the current publication unit. After its bot publication commit is created, verify remote HEAD and create exactly one normal-user checkpoint. If all mandatory CI PASS, continue the under-target phrase families from frontiers `pv.00000310`, `chunk.00000180` and `idiom.00000150` with another bounded reviewed batch. Recalculate counts and run exact/near dedupe before every write.','Scale-136 is the current publication unit. After its bot publication commit is created, verify remote HEAD and create exactly one normal-user checkpoint. If all mandatory CI PASS, continue the under-target phrase families from frontiers `pv.00000320`, `chunk.00000195` and `idiom.00000165` with another bounded reviewed batch. Recalculate counts and run exact/near dedupe before every write.','next task')]
for old,new,label in repls: text=replace_once(text,old,new,label)
path.write_text(text,encoding='utf-8')
