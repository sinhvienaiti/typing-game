"""Rebuild the ticket-218 candidate sets that scored below 6 and render 10 of them to listen to (coordinator, 30/10).

Read-only on the source WAVs and on the 218 deliverables; writes only to tmp/keys-firefly/listen-rejected/.
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

REPO = Path('/Users/toandx/htdocs/typing-game')
sys.path.insert(0, str(REPO / 'tools/audio-lab'))
from keys import firefly_v2 as v2  # noqa: E402

OUT = REPO / 'tmp/keys-firefly/listen-rejected'
OUT.mkdir(parents=True, exist_ok=True)
SR = v2.SR

captured = []
real_score = v2.score_set


def spy(keys, spaces, maxcorr):
    score, comps = real_score(keys, spaces, maxcorr)
    captured.append({'keys': keys, 'spaces': spaces, 'score': score, 'components': comps, 'maxcorr': maxcorr})
    return score, comps


v2.score_set = spy
data = json.loads((v2.ff.OUT / 'features.json').read_text())
candidates, _ = v2.prepare(data, v2.WORK)
accepted, stats = v2.propose(candidates)
print('stats', stats)

low = [c for c in captured if c['score'] < 6]
high = [c for c in captured if c['score'] >= 6]
for c in low + high:
    c['center'] = np.median([k['v'] for k in c['keys']], axis=0)
    c['folders'] = sorted({k['take']['folder'] for k in c['keys']})
low.sort(key=lambda c: -c['score'])

# Ten rejected sets spread over the score range, each clearly different from the others picked.
picked = []
targets = np.linspace(low[0]['score'], low[-1]['score'], 10)
for t in targets:
    pool = sorted(low, key=lambda c: abs(c['score'] - t))
    for c in pool:
        if c in picked:
            continue
        if all(v2.distance(c['center'], p['center']) >= 0.5 for p in picked):
            picked.append(c)
            break
picked.sort(key=lambda c: -c['score'])


def render(sets, seconds=10.0, seed=7):
    rng = np.random.default_rng(seed)
    out = np.zeros(round(seconds * SR))
    t, i, ki, si = 0.05, 0, 0, 0
    keys = list(sets['keys'])
    rng.shuffle(keys)
    while True:
        part = 'space' if i % 6 == 5 else 'key'
        y = (sets['spaces'][si % len(sets['spaces'])] if part == 'space' else keys[ki % len(keys)])['audio']
        if t + len(y) / SR > seconds - 0.05:
            break
        a = round(t * SR)
        out[a:a + len(y)] += float(rng.uniform(.92, 1.08)) * y
        if part == 'space':
            si += 1
        else:
            ki += 1
        i += 1
        wpm = 70 if (t % 5.0) < 2.5 else 100
        t += (60 / (wpm * 5)) * float(rng.uniform(.95, 1.05))
    return out


def norm(y, rms=0.05):
    r = float(np.sqrt(np.mean(y[np.abs(y) > 1e-5] ** 2))) if np.any(np.abs(y) > 1e-5) else 1.0
    y = y * (rms / r)
    peak = float(np.max(np.abs(y)))
    return y * (0.89 / peak) if peak > 0.89 else y


def mp3(y, path):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f64le', '-ar', str(SR), '-ac', '1', '-i', 'pipe:0',
                    '-c:a', 'libmp3lame', '-b:a', '192k', str(path)], input=y.astype('<f8').tobytes(), check=True)


rows = []
best = max(high, key=lambda c: c['score'])
mp3(norm(render(best)), OUT / f'00-tham-chieu-dat-{best["score"]:.2f}.mp3')
rows.append({'file': f'00-tham-chieu-dat-{best["score"]:.2f}.mp3', 'score': best['score'], 'components': best['components'],
             'folders': best['folders'], 'keys': len(best['keys']), 'spaces': len(best['spaces'])})
for n, c in enumerate(picked, 1):
    name = f'{n:02d}-loai-{c["score"]:.2f}.mp3'
    mp3(norm(render(c)), OUT / name)
    rows.append({'file': name, 'score': c['score'], 'components': c['components'], 'maxcorr': c['maxcorr'],
                 'folders': c['folders'], 'keys': len(c['keys']), 'spaces': len(c['spaces'])})
(OUT / 'scores.json').write_text(json.dumps({'stats': stats, 'captured_below_6': len(low), 'captured_at_or_above_6': len(high),
                                             'sets': rows}, indent=1, ensure_ascii=False, default=float))
for r in rows:
    comp = ', '.join(f'{k} {v:.2f}' for k, v in r['components'].items())
    print(r['file'], '|', comp, '|', ','.join(f.replace('Adobe_2026-10-29', 'F') for f in r['folders']))
