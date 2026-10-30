#!/usr/bin/env python3
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]
s = runpy.run_path(str(ROOT / 'scripts/english-e04-scale-135-common.py'), run_name='e04_scale135_progress')
replace_once = s['replace_once']
path = s['PROGRESS_PATH']
text = path.read_text(encoding='utf-8')

repls = [
    (
        '- Latest fully CI-verified scale-up checkpoint before scale-134 publication: `75fab60100845a2568e73f3617e700a0b8288bd9` — scale-133 publication state verified by English Content Master Plan Acceptance #411, English Content Full Validation #322 and Platform CI #1621; published output: `8c1f7a0ec4bf07c96952f64bbd9266c2cb2643ea`.',
        '- Latest fully CI-verified scale-up checkpoint before scale-135 publication: `10e1bf9c128164d93b48d88d7b63bd28d16e2c25` — scale-134 publication state verified by English Content Master Plan Acceptance #414, English Content Full Validation #325 and Platform CI #1624; published output: `34ce9e491c465aa4d1b16bb2770f4c12325e535c`.',
        'verified scale-134 checkpoint',
    ),
    (
        '- Scale-133 publication checkpoint `75fab60100845a2568e73f3617e700a0b8288bd9` is fully verified; scale-134 is the current publication unit.',
        '- Scale-134 publication checkpoint `10e1bf9c128164d93b48d88d7b63bd28d16e2c25` is fully verified; scale-135 is the current publication unit.',
        'scale-134 verification state',
    ),
    (
        '- E04 phrase/pattern architecture + current reviewed publication: complete — 6,110 published records after scale-134',
        '- E04 phrase/pattern architecture + current reviewed publication: complete — 6,150 published records after scale-135',
        'E04 publication count',
    ),
    ('## Published runtime snapshot after E04 scale-134 publication', '## Published runtime snapshot after E04 scale-135 publication', 'runtime heading'),
    ('- phrases: 6,110 records', '- phrases: 6,150 records', 'phrase count'),
    ('- total published rich records: 10,711', '- total published rich records: 10,751', 'rich count'),
    ('- editorial ledger: 10,711 decisions / 10,711 applied / 10,711 publish decisions', '- editorial ledger: 10,751 decisions / 10,751 applied / 10,751 publish decisions', 'ledger count'),
    (
        '- E04 collocation frontier: `col.00005000`',
        '- E04 collocation frontier: `col.00005000`\n- E04 phrasal-verb frontier: `pv.00000310`\n- E04 chunk frontier: `chunk.00000180`\n- E04 idiom frontier: `idiom.00000150`',
        'phrase frontiers',
    ),
    (
        '1. Scale-133 publication is fully verified at `75fab60100845a2568e73f3617e700a0b8288bd9`; do not duplicate scale-133 artifacts.',
        '1. Scale-134 publication is fully verified at `10e1bf9c128164d93b48d88d7b63bd28d16e2c25`; do not duplicate scale-134 artifacts.',
        'verified workstream',
    ),
    (
        '2. Scale-134 is the current publication unit; do not start another E04 batch until its publication/checkpoint CI completes.',
        '2. Scale-135 is the current publication unit; do not start another E04 batch until its publication/checkpoint CI completes.',
        'current workstream',
    ),
    (
        '3. After the scale-134 bot publication commit is created, create exactly one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.',
        '3. After the scale-135 bot publication commit is created, create exactly one normal-user checkpoint and verify English Content Full Validation, Master Plan Acceptance and Platform CI.',
        'checkpoint workstream',
    ),
    (
        '5. After the scale-134 checkpoint, the collocation minimum target of 5,000 is satisfied. Recalculate family deficits from HEAD and continue with the safest under-target E04 family, prioritizing phrasal verbs and idioms/chunks over another collocation batch unless reviewed evidence justifies otherwise.',
        '5. Scale-135 resumes the under-target phrase families with 10 reviewed phrasal verbs, 15 chunks and 15 idioms. After its checkpoint, recalculate deficits from HEAD and continue another bounded phrasal-verb/idiom/chunk batch unless safer reviewed enrichment becomes available.',
        'next family',
    ),
    (
        'Scale-134 is the current publication unit. After its bot publication commit is created, verify remote HEAD and create exactly one normal-user checkpoint. If all mandatory CI PASS, recalculate E04 family deficits from HEAD: the collocation minimum is then 5,000, so continue with the safest under-target phrasal-verb or idiom/chunk batch rather than automatically extending collocations. Run exact/near dedupe before every write.',
        'Scale-135 is the current publication unit. After its bot publication commit is created, verify remote HEAD and create exactly one normal-user checkpoint. If all mandatory CI PASS, continue the under-target phrase families from frontiers `pv.00000310`, `chunk.00000180` and `idiom.00000150` with another bounded reviewed batch. Recalculate counts and run exact/near dedupe before every write.',
        'next task',
    ),
]
for old, new, label in repls:
    text = replace_once(text, old, new, label)
path.write_text(text, encoding='utf-8')
