"""Phiếu 189: cổng nguồn, chọn họ, nền, codec, nhịp preview và luật kit thật."""
import itertools
import json
import subprocess
from pathlib import Path

import numpy as np
import pytest
import soundfile as sf

from keys import firefly as ff, firefly_build as fb, pipeline


def folder(name, bands=0, centroid=600, count=50, length=100):
    return {'folder': name, 'files': count,
            'key_like': {'bands_db': {k: bands for k,*_ in ff.BANDS},
                         'centroid_hz': centroid, 'len40_ms': length, 't60_ms': 120}}


def test_grouping_merges_only_near_duplicates_and_compatible_small_folder():
    a, b, c = folder('a'), folder('b', .6, 630), folder('c', 3, 950)
    small = folder('small', .7, 650, count=8)
    groups, report = fb.group_folders([a,b,c,small])
    assert [[p['folder'] for p in g] for g in groups] == [['a','b','small'],['c']]
    assert [d['action'] for d in report['decisions']] == ['merge-near-duplicate','merge-small']
    assert len(report['pairs']) == 6


def test_grouping_does_not_chain_merges_and_omits_incompatible_small_folder():
    groups, report = fb.group_folders([folder('a'), folder('b', .7), folder('c', 1.4),
                                     folder('small', 15, 2000, count=8)])
    assert [[p['folder'] for p in g] for g in groups] == [['a','b'],['c']]
    assert report['decisions'][-1]['action'] == 'omit-small'


def test_mono_loss_selects_better_snr_channel():
    rng = np.random.default_rng(189)
    x = rng.standard_normal((4800,))*.1
    quiet = rng.standard_normal((480,2))*np.array([1e-5,1e-3])
    mono, info = fb.fold_mono(np.c_[x,-.9*x],quiet)
    assert info['fold_loss_db'] > 20 and info['method'] == 'left'
    np.testing.assert_array_equal(mono,x)
    mono, info = fb.fold_mono(np.c_[x,.98*x],quiet)
    assert info['method']=='mid' and info['fold_loss_db'] < 1
    np.testing.assert_allclose(mono,.99*x)


def test_background_gate_mutes_hold_without_touching_press_and_release():
    rng = np.random.default_rng(10)
    y = rng.standard_normal(9600)*1e-6
    y[100:800] += rng.standard_normal(700)*.1
    y[5000:5700] += rng.standard_normal(700)*.02
    clean, info = fb.quiet_gate(y,1e-6)
    np.testing.assert_allclose(clean[200:700],y[200:700])
    np.testing.assert_allclose(clean[5100:5600],y[5100:5600])
    assert np.max(abs(clean[2000:4000])) < 1e-12
    assert info['muted_intervals_samples']


def test_correlation_detects_shifted_and_inverted_twins():
    rng = np.random.default_rng(20)
    x = rng.standard_normal(4800)*np.exp(-np.arange(4800)/800)
    assert fb.corr_max(x,np.r_[np.zeros(96),-x]) > .99
    assert fb.corr_max(x,rng.standard_normal(6000)) < .1


def sets():
    rng = np.random.default_rng(1)
    return {part: [rng.standard_normal(4800)*np.exp(-np.arange(4800)/400)*.03 for _ in range(n)]
            for part,n in [('key',10),('space',3)]}


def test_preview_one_second_six_keys_one_space_cycle_timing_and_level():
    y, report = fb.phrase(sets())
    assert len(y)==48000
    ev = report['events']
    assert [e['set'] for e in ev] == ['key']*6+['space']
    assert [e['variant'] for e in ev[:6]]==list(range(1,7))
    assert all(.12*.97 <= b['time_s']-a['time_s'] <= .12*1.03+1e-6 for a,b in zip(ev,ev[1:]))
    assert all(.92<=e['gain']<=1.08 for e in ev)
    assert all(e['end_s']<=.995 for e in ev)
    assert np.max(abs(y[-2400:]))==0
    long, report = fb.phrase(sets(),10)
    assert len(long)==480000
    assert [e['variant'] for e in report['events'] if e['set']=='key'][:12] == list(range(1,11))+[1,2]


def test_output_guard_rejects_source_and_symlink(tmp_path):
    src=tmp_path/'source'; src.mkdir()
    out=tmp_path/'source-link'; out.symlink_to(src,target_is_directory=True)
    with pytest.raises(ValueError,match='chồng'):
        fb.safe_paths(src,out,tmp_path/'work',tmp_path/'evidence')
    with pytest.raises(ValueError,match='chồng'):
        fb.safe_paths(src,tmp_path,tmp_path/'work',tmp_path/'evidence')
    out=tmp_path/'existing';out.mkdir();(out/'unrelated.txt').write_text('preserve')
    with pytest.raises(ValueError,match='không thuộc'):
        fb.safe_paths(src,out,tmp_path/'work',tmp_path/'evidence')


def test_cli_routes_build_with_explicit_paths(tmp_path,monkeypatch):
    calls=[]
    monkeypatch.setattr(fb,'build',lambda *args: calls.append(args))
    assert pipeline.main(['firefly','build','--src',str(tmp_path/'src'),'--out',str(tmp_path/'out')])==0
    assert calls[0][0]==tmp_path/'src' and calls[0][2]==tmp_path/'out'


def kit_actual(manifest,base):
    """Chạy nguyên hàm keyboardFiles hiện hành bằng Node stripTypeScriptTypes, không build game."""
    source = (ff.REPO/'shared/game-kit/feedback/typing-fx/audio.ts').read_text()
    constant = source[source.index('const FILE = '):source.index('const FILE = ')+source[source.index('const FILE = '):].index('\n')]
    begin = source.index('export function keyboardFiles(')
    end = source.index('\nexport type KeyboardLoad',begin)
    fn = source[begin:end]
    script = '''import {stripTypeScriptTypes} from 'node:module';
let input='';for await(const chunk of process.stdin) input+=chunk;
const d=JSON.parse(input);
const code=stripTypeScriptTypes(d.source,{mode:'strip'}).replace('export function','function');
const f=new Function(code+';return keyboardFiles');
process.stdout.write(JSON.stringify(f()(d.manifest,d.base)));
'''
    run = subprocess.run(['node','--input-type=module','-e',script],
                         input=json.dumps({'source':constant+'\n'+fn,'manifest':manifest,'base':base}),
                         text=True,capture_output=True,check=True)
    return json.loads(run.stdout)


def test_manifest_walker_matches_actual_kit_rejections_depth_and_first_variant():
    man={'files':['key-02.ogg','key-01.ogg','key-01.wav','space-01.ogg',
                  '/key-03.ogg','https://example/key-04.wav','../key-05.wav'],
         'preview':'preview.ogg','deep':{'a':{'b':{'c':{'d':{'e':{'f':'key-08.ogg'}}}}}}}
    want={k:['/audio/'+p for p in v] for k,v in pipeline.kit_files(man).items()}
    assert kit_actual(man,'/audio')==want
    assert want=={'key':['/audio/key-01.ogg','/audio/key-02.ogg'],'space':['/audio/space-01.ogg']}


def test_codec_roundtrip_and_metrics(tmp_path):
    y=sets()['key'][0];y=np.r_[y,np.zeros(480)]
    master,runtime=fb.encode(y,tmp_path/'key-01.wav',tmp_path/'key-01.ogg')
    info=sf.info(tmp_path/'key-01.wav')
    assert (info.channels,info.samplerate,info.subtype)==(1,48000,'PCM_24')
    assert len(master)==len(runtime)==len(y)
    assert abs(fb.audio_metrics(master)['lufs_m_max']-fb.audio_metrics(runtime)['lufs_m_max']) < .5


def test_staged_manifests_and_audio_acceptance():
    out = ff.REPO/'tmp/keys-firefly/staging/keys-firefly'
    if not (out/'keys-manifest.json').exists():
        pytest.skip('Chưa dựng bộ nguồn chủ dự án trên máy này')
    root=json.loads((out/'keys-manifest.json').read_text())
    assert root['status']=='owner-approved-source'
    assert len(root['profiles'])>=1
    centers=[]; all_audio=[]
    for order,p in enumerate(root['profiles']):
        assert p['order']==order
        assert 1 <= len(p['name'].split()) <= 2
        manifest=json.loads((out/p['manifest']).read_text())
        actual=kit_actual(manifest,'/keys/'+p['id'])
        assert len(actual['key'])==10 and len(actual['space'])==3
        assert all(path.endswith('.ogg') for group in actual.values() for path in group)
        centers.append(manifest['family']['key_centroid_median_hz'])
        assert len({f['source']['directory'] for f in manifest['files'] if f['set']=='key'}) == 1
        lms=[];audio=[]
        for f in manifest['files']:
            for ext in ('wav','ogg'):
                path=out/p['id']/(Path(f['file']).stem+'.'+ext)
                assert fb.sha(path)==f['sha256'][ext]
                y,sr=sf.read(path);m=fb.audio_metrics(y, f['gate']['muted_intervals_samples'])
                assert sr==48000 and y.ndim==1
                assert m['duration_ms'] <= (180 if f['set']=='key' else 260)
                assert m['true_peak_dbtp']<=-1 and m['background_dbfs']<=-70
                assert abs(m['lufs_m_max']-manifest['loudness']['target'])<=.5
                assert f['processing']['fade_in_ms'] <= 1
                if ext=='ogg':
                    audio.append(y);lms.append(m['lufs_m_max'])
        assert max(lms)-min(lms)<=1
        assert max(fb.corr_max(a,b) for a,b in itertools.combinations(audio,2))<=.95
        all_audio+=audio
        y,sr=sf.read(out/p['preview'])
        assert abs(len(y)/sr-1)<=.01 and fb.audio_metrics(y)['background_dbfs']<=-70
        assert max(e['end_s'] for e in manifest['preview_schedule']['events'])<=.995
    assert centers==sorted(centers)
    assert max(fb.corr_max(a,b) for a,b in itertools.combinations(all_audio,2)) <= .95
