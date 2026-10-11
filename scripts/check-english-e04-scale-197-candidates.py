#!/usr/bin/env python3
from __future__ import annotations
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
s = runpy.run_path(str(ROOT / 'scripts/english-e04-scale-197-common.py'), run_name='e04_scale197_gap_probe')
manifest = s['read_json'](s['MANIFEST_PATH'])
nk = s['normalized_key']
jac = s['jaccard']
threshold = s['NEAR_DUP_THRESHOLD']
existing = []
for batch in manifest.get('batches', []):
    if batch.get('phase') != 'E04' or batch.get('category') != 'phrases':
        continue
    for rs in batch.get('recordSets', []):
        for record in s['read_json'](ROOT / rs['path']).get('records', []):
            value = record.get('text') or record.get('pattern') or ''
            if value:
                existing.append((record.get('id'), value))

probe = [
    'bed in', 'bed down', 'black out', 'blank out', 'block in', 'bog down', 'box in',
    'branch off from', 'break out into', 'brush past', 'bulk up', 'bump along', 'bump up against',
    'chug along', 'clamber down', 'claw back', 'cotton to', 'crank out', 'creep up on',
    'crowd in on', 'drum up', 'duck out of', 'ease off on', 'edge out', 'eke out', 'ferret out',
    'flag down', 'flare up', 'fling off', 'flounce out', 'fork out', 'fritter away', 'fuss over',
    'gear down', 'gear up for', 'gussy up', 'hack away at', 'hammer away at', 'hive off',
    'hunker down to', 'jockey for', 'key in on', 'lay into', 'leach away', 'limber up', 'lope along',
    'lumber along', 'mark down', 'narrow down', 'pan out', 'pare back', 'pare down', 'pick apart',
    'pile into', 'pitch in', 'pore over', 'rattle off', 'reel off', 'rope in', 'saw away at',
    'scrounge around for', 'shunt off', 'siphon off', 'skive off', 'slough off', 'sniff around',
    'snuff out', 'spool off', 'spool out', 'squirrel away', 'stitch up', 'taper off', 'tee off on',
    'think through', 'trickle down', 'trundle off', 'tune out', 'warm through', 'whack up',
    'winkle out of', 'wolf down', 'chunter on', 'faff about', 'faff around', 'fiddle about with',
    'fiddle around with', 'mooch about', 'mooch around', 'pootle about', 'pootle around',
    'potter about', 'potter around', 'slog away at', 'soldier on with', 'square up to',
    'stand in for', 'tag along with', 'veer away from', 'weigh in on', 'wind down from',
    'wise up to', 'zero in on', 'zoom in on', 'buckle down to', 'knuckle down to', 'lash out at',
    'live down', 'live up to', 'muck in', 'muck about', 'nose around for', 'nose out', 'own up to',
    'patch through', 'peg away at', 'phase in', 'phase out', 'pick over', 'play along with',
    'press ahead with', 'press on with', 'root about for', 'rough out', 'round on', 'scare up',
    'screen out', 'shack up with', 'ship out', 'shop around for', 'sift through', 'sit in for',
    'sleep in', 'slip up on', 'sound out', 'splash out on', 'square away', 'stand down from',
    'stave off', 'step down from', 'stick up for', 'straighten out', 'strike out at', 'talk around',
    'thrash out', 'tip off', 'trip up', 'tuck into', 'walk back', 'wean off', 'weed out',
    'whittle away at', 'work around', 'yield up', 'chew over', 'clam up', 'clamp down on',
    'crop up', 'doss down', 'drift apart', 'filter out', 'fish around for', 'flesh out',
    'flick through', 'foul up', 'gloss over', 'grind away at', 'grow apart', 'hinge on',
    'home in on', 'iron out', 'jack up', 'kick against', 'knock about', 'leaf through',
    'lock onto', 'map out', 'mull over', 'muscle in on', 'paper over', 'parcel out',
    'peel away from', 'peter out', 'plough on', 'plow on', 'prune back', 'rake in',
    'ratchet up', 'root out', 'rough in', 'scrape by on', 'shell out for', 'shore up',
    'size up', 'skim over', 'slog through', 'snap out of', 'sort through', 'spin off from',
    'squeeze out', 'stamp out', 'stir up', 'string along', 'tail off', 'tease out',
    'thin out', 'track down', 'veer off', 'ward off', 'wash out', 'water down', 'whip through'
]

rows = []
for text in probe:
    key = nk(text)
    exact = []
    near = []
    for rid, old_text in existing:
        old_key = nk(old_text)
        if old_key == key:
            exact.append(rid)
            continue
        score = jac(text, old_text)
        if score >= threshold:
            near.append({'id': rid, 'text': old_text, 'score': round(score, 3)})
    rows.append({'text': text, 'clean': not exact and not near, 'exactIds': exact, 'near': near})

print('SCALE197_PHRASAL_GAP_PROBE=' + json.dumps({
    'existingE04Texts': len(existing),
    'threshold': threshold,
    'clean': [row['text'] for row in rows if row['clean']],
    'conflicts': [row for row in rows if not row['clean']],
}, ensure_ascii=False))

source = (ROOT / 'scripts/check-english-e04-scale-196-candidates.py').read_text(encoding='utf-8').replace('scale-196', 'scale-197').replace('scale196', 'scale197')
exec(compile(source, str(Path(__file__)), 'exec'), {'__name__': '__main__', '__file__': __file__})
