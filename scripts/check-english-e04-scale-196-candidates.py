#!/usr/bin/env python3
from __future__ import annotations
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
s = runpy.run_path(str(ROOT / 'scripts/english-e04-scale-196-common.py'), run_name='e04_scale196_gap_probe')
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
    "acknowledge the corn",
    "cut the cackle",
    "go for a Burton",
    "have a cob on",
    "put the acid on someone",
    "go crook",
    "ride Shanks's mare",
    "make a Horlicks of something",
    "not worth a tinker's cuss",
    "like billy-o",
    "all my eye and Betty Martin",
    "as queer as Dick's hatband",
    "kick over the traces",
    "carry coals to Newcastle",
    "cock a snook",
    "the whole boiling",
    "go to pot",
    "not by a long chalk",
    "like the clappers",
    "over-egg the pudding",
    "give it some welly",
    "take French leave",
    "jam tomorrow",
    "put paid to something",
    "throw a sickie",
    "spit the dummy",
    "chuck a wobbly",
    "flat out like a lizard drinking",
    "carry on like a pork chop",
    "a sandwich short of a picnic",
    "lose one's rag",
    "be up the pole",
    "play gooseberry",
    "talk the hind leg off a donkey",
    "like a bear with a sore head",
    "cheap at half the price",
    "spend a penny",
    "not cricket",
    "have a butcher's",
    "brass monkeys",
    "get out over one's skis",
    "put one's cards on the table",
    "keep one's powder dry",
    "make heavy weather of something",
    "go round the houses",
    "have kittens",
    "put the tin lid on it",
    "come the raw prawn",
    "give someone the drum",
    "a few roos loose in the top paddock",
    "couldn't raffle a chook in a pub",
    "do a Melba",
    "as flash as a rat with a gold tooth",
    "dry as a dead dingo's donger",
    "mad as a gumtree full of galahs",
    "full as a goog",
    "have tickets on oneself",
    "shoot through like a Bondi tram",
    "stone the crows",
    "tell someone to go and jump in the lake",
    "have a blue",
    "give someone a serve",
    "go off like a frog in a sock",
    "couldn't run a chook raffle",
    "put a sock in it",
    "on the wallaby track",
    "up sticks",
    "make ducks and drakes of something",
    "go to the country",
    "put up the shutters",
    "make bones about something",
    "cut no ice",
    "keep one's hair on",
    "put one's foot in it",
    "go nap on something",
    "take a powder",
    "give someone the raspberry",
    "have a dekko",
    "take a shufti",
    "go down the Swanee",
]

probe_results = []
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
    probe_results.append({'text': text, 'clean': not exact and not near, 'exactIds': exact, 'near': near})

print('SCALE196_GAP_PROBE=' + json.dumps({
    'existingE04Texts': len(existing),
    'threshold': threshold,
    'clean': [row['text'] for row in probe_results if row['clean']],
    'conflicts': [row for row in probe_results if not row['clean']],
}, ensure_ascii=False))

source = (ROOT / 'scripts/check-english-e04-scale-195-candidates.py').read_text(encoding='utf-8').replace('scale-195', 'scale-196').replace('scale195', 'scale196')
exec(compile(source, str(Path(__file__)), 'exec'), {'__name__': '__main__', '__file__': __file__})
