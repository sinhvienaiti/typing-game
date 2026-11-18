"""Phiếu 218: cổng, khoảng cách, điểm, tên, CLI và bàn giao thật qua kit."""
import itertools
import json
from pathlib import Path

import numpy as np
import pytest
import soundfile as sf

from keys import firefly_v2 as v2, firefly as ff, firefly_build as old, pipeline
from keys.tests.test_firefly_build import kit_actual


def feature(**updates):
    f=dict(clean=True,clip_samples=0,window_ms=100,main_ms=4,attack_ms=8,next_press_ms=150,
           tail={'t60_ms':120},space_like=False)
    f.update(updates)
    return f


@pytest.mark.parametrize('changes',[
    {'clean':False},{'clip_samples':1},{'window_ms':241},{'main_ms':41},
    {'attack_ms':41},{'next_press_ms':101},{'tail':{'t60_ms':161}},
])
def test_raw_gate_never_relaxes_clipping_overlap_or_long_tail(changes):
    assert v2.eligible(feature())
    assert not v2.eligible(feature(**changes))


def test_guard_preserves_unowned_output_and_source_symlink(tmp_path):
    src=tmp_path/'src';src.mkdir()
    linked=tmp_path/'linked';linked.symlink_to(src,target_is_directory=True)
    with pytest.raises(ValueError,match='chồng'):
        v2.guard(src,linked,tmp_path/'work',tmp_path/'evidence')
    out=tmp_path/'out';out.mkdir();(out/'keep.txt').write_text('keep')
    with pytest.raises(ValueError,match='không thuộc'):
        v2.guard(src,out,tmp_path/'work',tmp_path/'evidence')
    assert (out/'keep.txt').read_text()=='keep'


def test_distance_is_fixed_physical_scaling_not_refitted_to_get_eighty():
    x=np.zeros(9); y=x.copy();y[1:7]=1
    assert v2.distance(x,y)==pytest.approx(np.sqrt(6/9))
    assert v2.distance(x,x)==0
    assert v2.MIN_DISTANCE==.5


def test_uniqueness_rejects_shifted_inverted_waveform():
    rng=np.random.default_rng(218)
    y=rng.normal(size=4000)*np.exp(-np.arange(4000)/300)
    pool=[{'uid':str(i),'audio':a} for i,a in enumerate([y,np.r_[np.zeros(48),-y],rng.normal(size=4000)])]
    chosen=v2.unique(pool,3)
    assert [c['uid'] for c in chosen]==['0','2']


def test_score_components_have_real_effect_and_are_bounded():
    c={'v':np.zeros(9),'audio':np.zeros(4000),'features':feature(attack_ms=3,tail={'t60_ms':60}),
       'source_floor_at_target_dbfs':-80}
    good,parts=v2.score_set([c],[c],.4)
    poor,_=v2.score_set([dict(c,features=feature(attack_ms=12,tail={'t60_ms':160}),
                               source_floor_at_target_dbfs=-60)],[c],.94)
    assert good==pytest.approx(10) and poor<good
    assert set(parts)=={'cleanliness','consistency','repetition','background','tail'}
    assert all(0<=x<=1 for x in parts.values())


def test_names_retain_best_old_ids_and_family_score_order():
    groups=[]
    for i,(fid,label) in enumerate(v2.FAMILIES):
        for score in [6.2,8.1]:
            groups.append(dict(center=np.full(9,i*10.),score=score,centroid=100+i))
    anchors={fid:np.full(7,i*10.) for i,(fid,_) in enumerate(v2.FAMILIES)}
    result=v2.assign_names(groups,anchors)
    assert len({g['name'] for g in result})==14
    for i,(fid,_) in enumerate(v2.FAMILIES):
        assert result[i*2]['id']==fid and result[i*2]['score']==8.1


def test_cli_keeps_189_and_routes_v2(tmp_path,monkeypatch):
    calls=[]
    monkeypatch.setattr(v2,'build',lambda *args:calls.append(args))
    assert pipeline.main(['firefly','build-v2','--src',str(tmp_path/'src'),'--prepare-only'])==0
    assert calls[0][0]==tmp_path/'src' and calls[0][-1] is True


def test_staged_v2_catalogue_and_decoded_runtime():
    out=v2.STAGING
    if not (out/'keys-manifest.json').exists():
        pytest.skip('Chưa dựng media phiếu 218')
    root=json.loads((out/'keys-manifest.json').read_text())
    assert root['profiles']
    centers=[];maxcorr=0
    assert len({p['id'] for p in root['profiles']})==len(root['profiles'])
    assert len({p['name'] for p in root['profiles']})==len(root['profiles'])
    families=[f for _,f in v2.FAMILIES]
    ordering=[]
    for order,p in enumerate(root['profiles']):
        assert p['order']==order and p['score']>=6
        ordering.append((families.index(p['family']),-p['score']))
        man=json.loads((out/p['manifest']).read_text())
        assert (man['family'],man['score'])==(p['family'],p['score'])
        actual=kit_actual(man,'/keys/'+p['id'])
        assert 70<=len(actual['key'])<=100 and 6<=len(actual['space'])<=10
        assert len(actual['key'])+len(actual['space'])==len(man['files'])
        assert 1<=len({(f['source']['directory'],f['source']['original_file']) for f in man['files']})<=8
        centers.append(man['measurements']['timbre_center'])
        waves=[];levels=[]; kc=[];sc=[];kd=[];sd=[]
        for f in man['files']:
            path=out/p['id']/f['file'];assert path.suffix=='.ogg'
            assert old.sha(path)==f['sha256']
            y,sr=sf.read(path);assert sr==48000 and y.ndim==1
            met=old.audio_metrics(y,f['gate']['muted_intervals_samples'])
            assert met['duration_ms']<=(180 if f['set']=='key' else 260)
            assert met['true_peak_dbtp']<=-1 and met['background_dbfs']<=-60
            assert abs(met['lufs_m_max']-v2.TARGET)<=.75
            assert f['processing']['fade_in_ms']<=1
            assert f['source']['sha256'] and f['source']['cut_end_s']>f['source']['cut_start_s']
            levels.append(met['lufs_m_max']);waves.append(y)
            (kc if f['set']=='key' else sc).append(met['centroid_hz'])
            (kd if f['set']=='key' else sd).append(met['duration_ms'])
        assert max(levels)-min(levels)<=1.5
        assert max(sc)<np.median(kc)*.95 and min(sd)>np.median(kd)*1.05
        corr=max(old.corr_max(a,b) for a,b in itertools.combinations(waves,2))
        maxcorr=max(maxcorr,corr);assert corr<=.95
        y,sr=sf.read(out/p['preview']);assert abs(len(y)/sr-1)<=.01
        assert old.audio_metrics(y)['true_peak_dbtp']<=-1
    assert ordering==sorted(ordering)
    assert all(v2.distance(a,b)>=v2.MIN_DISTANCE-1e-6 for a,b in itertools.combinations(centers,2))
    assert all(any(p['id']==fid for p in root['profiles']) for fid,_ in v2.FAMILIES)
    assert not list(out.rglob('*.wav'))
