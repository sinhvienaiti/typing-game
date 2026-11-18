"""Sinh fixture, chạy ba lệnh và ghi số đo phiếu 217; không cần WAV của chủ dự án."""
import argparse
import json
import os
import sys
from pathlib import Path

repo = Path(__file__).resolve().parents[3]
root = repo / 'tmp/firefly-ingest'
sys.pycache_prefix = str(root / 'demo-cache/pycache')
sys.path.insert(0, str(repo / 'tools/audio-lab'))
os.environ.update(AUDIOLAB_HOME=str(root / 'demo-home'), MPLCONFIGDIR=str(root / 'demo-cache/matplotlib'),
                  NUMBA_CACHE_DIR=str(root / 'demo-cache/numba'), XDG_CACHE_HOME=str(root / 'demo-cache'))
from common import env
env.CACHE = root / 'demo-cache'
env.apply()
import numpy as np
import soundfile as sf
from build import ledger, measure
from firefly import main
from firefly.pipeline import write_json
from firefly.tests.test_firefly import hits
from context import voices

ap = argparse.ArgumentParser()
ap.add_argument('--voice-cache', type=Path, help='Chỉ đọc cache giọng có sẵn; không tạo giọng.')
a = ap.parse_args()
if a.voice_cache:
    voices.DIR = a.voice_cache.resolve()
inbox, out = root / 'inbox', root / 'demo-out'
hits(inbox / 'dragon-hold/fire.impact.a/demo.wav')
forest = inbox / 'dragon-hold/amb.forest/demo.wav'
forest.parent.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(217)
unit = rng.normal(0, .04, (48000, 2))
sf.write(forest, np.tile(unit, (6, 1)), 48000, subtype='PCM_16')

def snapshot():
    return {str(p.relative_to(inbox)): {'sha256': ledger.sha256_file(p), 'mtimeNs': p.stat().st_mtime_ns}
            for p in inbox.rglob('*.wav')}

def hashes():
    return {str(p.relative_to(out)): ledger.sha256_file(p) for p in out.rglob('*')
            if p.suffix in ('.wav', '.ogg') and ('masters' in p.parts or 'runtime' in p.parts)}

before = snapshot()
cmd = ['ingest', '--game', 'dragon-hold', '--inbox', str(inbox), '--out', str(out), '--run', 'demo-217']
codes = {'ingest': main(cmd)}
first = hashes()
codes['ingestAgain'] = main(cmd)
second = hashes()
codes['listen'] = main(['listen', '--game', 'dragon-hold', '--out', str(out)])
codes['status'] = main(['status', '--game', 'dragon-hold', '--inbox', str(inbox), '--out', str(out),
                        '--json', str(out / 'status.json')])
ids = []
for sid in ('fire.impact.a', 'amb.forest'):
    doc = json.loads((out / 'dragon-hold' / sid / 'takes.json').read_text())
    preview = json.loads((out / 'listen/dragon-hold' / f'{sid}-20s.json').read_text())
    run = out / 'dragon-hold' / sid / 'demo-217'
    variants = []
    for v in doc['variants']:
        wav, sr = sf.read(run / v['master'], always_2d=True)
        ogg, osr = sf.read(run / 'runtime' / v['runtime'], always_2d=True)
        variants.append({'variant': v['variant'], 'durationMs': len(wav)/sr*1000,
                         'lufsMMax': measure.lufs_m_max(wav, sr), 'lufsI': measure.lufs_i(wav, sr),
                         'truePeakDbtp': measure.true_peak_db(wav, sr),
                         'oggLufsMMax': measure.lufs_m_max(ogg, osr),
                         'oggTruePeakDbtp': measure.true_peak_db(ogg, osr), 'gate': v['gate']['verdict']})
    ids.append({'id': sid, 'found': doc['found'], 'passed': doc['passed'], 'selected': doc['selected'],
                'variantsExpected': doc['expectedVariants'], 'variants': variants, 'finalGate': doc['finalGate'],
                'idLevel': doc['idLevel'], 'split': doc['split'],
                'listen': {'mode': preview['mode'], 'scenario': preview['scenario'], 'duration_s': preview['duration_s'],
                           'true_peak_dbtp': preview['true_peak_dbtp'], 'lufs_m_max': preview['lufs_m_max']}})
result = {'codes': codes, 'ids': ids, 'repeat': {'same': sum(second.get(k) == v for k,v in first.items()),
          'total': len(first), 'equal': first == second, 'before': first, 'after': second},
          'inbox': {'unchanged': before == snapshot(), 'before': before, 'after': snapshot()},
          'out': str(out), 'voiceCache': str(voices.DIR),
          'note': 'Fixture kỹ thuật; không phải âm để phát hành, chưa đánh giá nghe. Không ghi hoặc sửa cache giọng.'}
write_json(repo / 'docs/codex-queue/217/demo.json', result)
assert all(code == 0 for code in codes.values()), codes
assert first == second and before == snapshot()
