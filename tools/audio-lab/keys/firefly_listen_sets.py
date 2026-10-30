"""Render one listening clip per installed Firefly keyboard set, for the owner to compare by ear.

Reads the installed sets (keys-manifest.json catalogue + OGG files), writes MP3 clips and index.json to
tmp/keys-firefly/listen-sets/. Every clip uses the same rhythm and loudness so only the sound differs.
Usage: bash tools/audio-lab/run.sh tools/audio-lab/keys/firefly_listen_sets.py [staging dir]
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[3]
SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / 'AudioLab/review/staging/keys-firefly'
OUT = REPO / 'tmp/keys-firefly/listen-sets'
SR = 48000
SECONDS = 9.0


def decode(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(path), '-f', 'f64le', '-ac', '1', '-ar', str(SR), 'pipe:1'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype='<f8')


def mp3(y, path):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f64le', '-ar', str(SR), '-ac', '1', '-i', 'pipe:0',
                    '-c:a', 'libmp3lame', '-b:a', '192k', str(path)], input=y.astype('<f8').tobytes(), check=True)


def pick(pool, recent, rng):
    """Like the kit: never repeat one of the last 8 variants when the pool allows it."""
    fresh = [i for i in range(len(pool)) if i not in recent[-8:]] or list(range(len(pool)))
    i = int(rng.choice(fresh))
    recent.append(i)
    return pool[i]


def render(keys, spaces, seed=11):
    """Words of 4–6 letters with a space between them; 70 WPM, then 100 WPM in the second half."""
    rng = np.random.default_rng(seed)
    out = np.zeros(round(SECONDS * SR))
    t, word_left, rk, rs = 0.1, int(rng.integers(4, 7)), [], []
    while True:
        part = 'space' if word_left == 0 else 'key'
        y = pick(spaces if part == 'space' else keys, rs if part == 'space' else rk, rng)
        if t + len(y) / SR > SECONDS - 0.05:
            break
        a = round(t * SR)
        out[a:a + len(y)] += float(rng.uniform(.92, 1.08)) * y
        word_left = int(rng.integers(4, 7)) if part == 'space' else word_left - 1
        wpm = 70 if t < SECONDS / 2 else 100
        t += (60 / (wpm * 5)) * float(rng.uniform(.9, 1.1))
    return out


def norm(y, rms=0.05):
    loud = np.abs(y) > 1e-5
    r = float(np.sqrt(np.mean(y[loud] ** 2))) if loud.any() else 1.0
    y = y * (rms / r)
    peak = float(np.max(np.abs(y)))
    return y * (0.89 / peak) if peak > 0.89 else y


def main():
    catalogue = json.loads((SRC / 'keys-manifest.json').read_text())
    profiles = sorted(catalogue['profiles'] if isinstance(catalogue, dict) else catalogue, key=lambda p: p['order'])
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for n, p in enumerate(profiles, 1):
        folder = SRC / p['id']
        keys = [decode(f) for f in sorted(folder.glob('key-*.ogg'))]
        spaces = [decode(f) for f in sorted(folder.glob('space-*.ogg'))]
        name = f"{n:02d}-{p['name']}-{p['score']:.1f}".replace(' ', '-') + '.mp3'  # names already start with the family
        mp3(norm(render(keys, spaces)), OUT / name)
        rows.append({'file': name, 'id': p['id'], 'name': p['name'], 'family': p['family'],
                     'score': round(p['score'], 2), 'keys': len(keys), 'spaces': len(spaces)})
        print(name, len(keys), len(spaces))
    (OUT / 'index.json').write_text(json.dumps({'source': str(SRC), 'seconds': SECONDS, 'sets': rows}, indent=1, ensure_ascii=False))


if __name__ == '__main__':
    main()
