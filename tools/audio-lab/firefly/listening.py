"""Twenty-second previews; context voices are read strictly from existing cache."""
from __future__ import annotations

import json
from contextlib import contextmanager
from pathlib import Path

import numpy as np
import soundfile as sf

from build import dsp, measure
from keys.firefly_build import mp3
from .pipeline import under, write_json

SR = 48000


@contextmanager
def cached_voices(*, probe=False):
    from context import voices
    previous = voices.load
    def read(voice, word):
        path = voices.path_for(voice, word)
        if not path.is_file():
            if probe:
                return np.zeros(1)
            raise FileNotFoundError(f'Thiếu giọng cache: {path.name}')
        x, sr = sf.read(path, always_2d=True)
        return dsp.resample(x, sr, SR).mean(axis=1)
    # Existing context builders call load(), which normally records on a cache miss.
    # Scope this read-only adapter tightly and always restore it, including on errors.
    voices.load = read
    try:
        yield
    finally:
        voices.load = previous


def context_audio(game, sid, focus_file, slots):
    from context import scenes, td_scenes, ts_scenes
    mod = {'dragon-hold': scenes, 'typing-survival': ts_scenes, 'typing-defense': td_scenes}[game]
    chosen = dict(slots)
    chosen[sid] = focus_file
    # Probe actual scenario events, not a second hard-coded list of slot names.
    scenario = None
    with cached_voices(probe=True):
        for candidate in mod.SCENARIOS:
            sc, _ = mod.build(candidate, chosen)
            if any(e.slot == sid for e in sc.events):
                scenario = candidate
                break
    if scenario is None:
        return None
    with cached_voices():
        sc, seconds = mod.build(scenario, chosen)
        if game == 'dragon-hold':
            from context import mixer
            result = mixer.render(sc.events, sc.voices, seconds, mixer.DRAGON_HOLD, duck_from='request')
        else:
            # td's key ticks are built in. They must be silent unless explicitly supplied.
            if game == 'typing-defense' and 'key' not in chosen:
                sc.events[:] = [e for e in sc.events if e.slot != 'key']
                sc.marks[:] = [m for m in sc.marks if m['id'] != 'key']
            elif game == 'typing-defense':
                for event in sc.events:
                    if event.slot == 'key':
                        event.audio = mod.load_mono(chosen['key'], mod.level_of('key'))
            result = mod.render_mix(sc, seconds)
        gain = getattr(mod, 'SCENE_GAIN_BY', {}).get(scenario, mod.SCENE_GAIN_DB)
        x = result['mix'] * 10**(gain/20)
        return x, scenario, sc.marks, seconds


def mix_level(card):
    target = card['loudness']['mix_target']
    levels = target.get('range')
    # Cards for ambience encode -26 in prose and have a null range; use proposal
    # or file level as their explicit numeric authority rather than parsing prose as a number.
    numeric = card['loudness'].get('proposal') or card['loudness']['file']
    return (target.get('metric') or numeric['metric'],
            float(sum(levels)/len(levels)) if levels else float(numeric['target']))


def sequence_audio(files, card):
    out = np.zeros((20*SR, 2))
    timeline, t, i = [], 0., 0
    metric, target = mix_level(card)
    while t < 19.95:
        path = files[i % len(files)]
        x, sr = sf.read(path, always_2d=True)
        x = dsp.resample(x, sr, SR)
        x, _ = dsp.to_channels(x, 2)
        now = measure.loudness(x, SR, metric)
        if np.isfinite(now):
            x *= 10**((target-now)/20)
        a = round(t*SR)
        n = min(len(x), len(out)-a)
        out[a:a+n] += x[:n]
        timeline.append({'t': t, 'variant': i % len(files)+1, 'file': str(path), 'end': (a+n)/SR,
                         'mixMetric': metric, 'mixTarget': target})
        t += max(float(card['playback'].get('min_gap_ms') or 0)/1000, len(x)/SR + .4)
        i += 1
    return out, timeline


def listen_id(game, sid, info, out, slots):
    base = under(out, out / game / sid)
    report = json.loads((base / 'takes.json').read_text(encoding='utf-8'))
    run = under(out, base / report['run'])
    files = [under(out, run / v['master']) for v in report['variants']]
    if not files:
        raise ValueError(f'{sid}: chưa có master để nghe')
    mode, scenario, reason = 'sequence', None, None
    try:
        result = context_audio(game, sid, files[0], slots)
    except FileNotFoundError as e:
        result, reason = None, str(e)
    if result is not None:
        chunk, scenario, marks, seconds = result
        x = np.zeros((20*SR, 2))
        timeline = []
        pos = 0
        while pos < len(x):
            n = min(len(chunk), len(x)-pos)
            x[pos:pos+n] = chunk[:n]
            timeline.extend([{**m, 't': m['t']+pos/SR} for m in marks if m['t'] < n/SR])
            pos += len(chunk)
        mode = 'context'
    else:
        x, timeline = sequence_audio(files, info['card'])
    x[-2400:] *= np.linspace(1, 0, 2400)[:, None]
    mono = x.mean(axis=1)
    tp = measure.true_peak_db(mono, SR)
    if tp > -1:
        mono *= 10**((-1.05-tp)/20)
    path = under(out, out / 'listen' / game / f'{sid}-20s.mp3')
    path.parent.mkdir(parents=True, exist_ok=True)
    mp3(mono, path)
    decoded, sr = sf.read(path, always_2d=True)
    doc = {'schema': 'audiolab.firefly.listen/1', 'game': game, 'id': sid, 'mode': mode,
           'scenario': scenario, 'focus': sid, 'fallbackReason': reason or ('Không có chỗ trong kịch bản' if mode == 'sequence' else None),
           'timeline': timeline, 'duration_s': len(decoded)/sr, 'bitrate_kbps': 192, 'fadeOutMs': 50,
           'lufs_i': measure.loudness(decoded, sr, 'lufs-i'), 'lufs_m_max': measure.lufs_m_max(decoded, sr),
           'true_peak_dbtp': measure.true_peak_db(decoded, sr),
           'voicePolicy': 'Chỉ đọc cache có sẵn; không ghi giọng mới.',
           'contextApproximation': 'Bộ nén dò đỉnh với bắt/nhả, bù mức Chromium; không có nhìn trước 6 ms.'}
    write_json(under(out, path.with_suffix('.json')), doc)
    return doc
