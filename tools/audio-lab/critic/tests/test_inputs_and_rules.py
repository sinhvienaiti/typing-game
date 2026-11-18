"""Degenerate inputs never stop a run, and the L1/L1b rules fixed after the batch-0 review."""
import json

import jsonschema
import numpy as np
import pytest
import soundfile as sf

from critic import artifacts, audio as A, features, hygiene, learned, pipeline
from critic import spec as S
from critic.schema import FILE_SCHEMA
from critic.tests import synth

SR = 48000


def _hit(n=int(0.12 * SR), seed=1):
    rng = np.random.default_rng(seed)
    t = np.arange(n) / SR
    x = (np.sin(2 * np.pi * 180 * t) * 0.5 + rng.normal(0, 0.2, n) * np.exp(-t * 60)) * np.exp(-t * 30)
    x[-240:] *= np.linspace(1, 0, 240)
    return x * 0.7


# ---------------------------------------------------------------- degenerate inputs (finding: one file kills the run)

def _broken_dir(tmp_path):
    d = tmp_path / "in"
    d.mkdir()
    x = _hit()
    sf.write(d / "hit.t1-mono.wav", x, SR, subtype="PCM_24")
    sf.write(d / "hit.t1-stereo.wav", np.stack([x, 0.9 * x], 1), SR, subtype="PCM_24")
    y = x.copy()
    y[100] = np.nan
    sf.write(d / "hit.t1-nan.wav", y.astype(np.float32), SR, subtype="FLOAT")
    y[100] = np.inf
    sf.write(d / "hit.t1-inf.wav", y.astype(np.float32), SR, subtype="FLOAT")
    sf.write(d / "hit.t1-empty.wav", np.zeros((0,)), SR, subtype="PCM_16")
    (d / "hit.t1-zerobyte.wav").write_bytes(b"")
    (d / "hit.t1-text.wav").write_text("this is not audio\n" * 50)
    sf.write(d / "hit.t1-6ch.wav", np.stack([x] * 6, 1), SR, subtype="PCM_16")
    return d


@pytest.mark.parametrize("layers", [("L1", "L1b", "L2", "L6"), ("L2",)])
def test_broken_files_are_blocked_not_fatal(tmp_path, layers):
    d = _broken_dir(tmp_path)
    out = tmp_path / "out"
    batch = pipeline.run([str(d)], out_dir=out, opts=pipeline.Options(layers=layers, group="hit_small", quiet=True))
    assert batch["n_files"] == 8
    res = {p.stem: json.loads(p.read_text("utf-8")) for p in out.glob("*.json") if not p.name.startswith("_")}
    want = {"hit.t1-nan": "not_finite", "hit.t1-inf": "not_finite", "hit.t1-empty": "empty",
            "hit.t1-zerobyte": "empty", "hit.t1-text": "unreadable"}
    for stem, code in want.items():
        r = res[stem]
        assert r["verdict"] == "BLOCK" and r["L1"]["blocking"] == [code] and r["error"]["code"] == code
        assert r["card"] is None and r["notes_vi"] and r["score"]["rank"] is None
        jsonschema.validate(r, FILE_SCHEMA)
    # the good files are scored as usual; six channels is a hygiene failure, not a crash
    assert res["hit.t1-mono"]["verdict"] != "BLOCK" or "L1" not in layers
    if "L1" in layers:
        assert "channels" in res["hit.t1-6ch"]["L1"]["failed"]
        assert res["hit.t1-6ch"]["metrics"]["lufs_m_max"] is not None
    assert "Bị chặn ở L1" in (out / "summary.md").read_text("utf-8")


def test_load_checked_reasons(tmp_path):
    d = _broken_dir(tmp_path)
    with pytest.raises(A.LoadError) as e:
        A.load_checked(d / "hit.t1-nan.wav")
    assert e.value.code == "not_finite" and "NaN" in e.value.msg_vi
    assert A.load_checked(d / "hit.t1-6ch.wav").channels == 6


# ---------------------------------------------------------------- clip scan per format (finding: false "unfixable clip")

def test_vorbis_overshoot_is_not_clipping_but_true_peak_still_fails(tmp_path):
    t = np.arange(int(0.3 * SR)) / SR
    x = 1.25 * np.sin(2 * np.pi * 440 * t) * np.exp(-t * 8)     # float: over full scale, not flat
    scan = hygiene.clip_scan(x[:, None], "VORBIS")
    assert scan["full_runs"] == 0 and scan["lossy_or_float"]
    flat = np.clip(x, -1.0, 1.0)                                 # a real flat clip in a float file
    assert hygiene.clip_scan(flat[:, None], "FLOAT")["full_runs"] > 0
    assert hygiene.clip_scan(x[:, None], "PCM_16")["full_runs"] > 0   # integer PCM: as the plan says


def test_eight_bit_pcm_gets_a_bit_depth_flag_not_a_clip(tmp_path):
    p = tmp_path / "hit.t1-u8.wav"
    sf.write(p, _hit(), SR, subtype="PCM_U8")
    a = A.load(p)
    sp = S.from_mapping({"id": "hit.t1", "group": "hit_small"})
    m, ctx = features.analyze(a, sp)
    g, _ = hygiene.gate(a.data, a.sr, m, sp, "raw", subtype=a.subtype)
    assert "clip_flat_top" not in g["failed"] and "clip_full_scale" not in g["failed"]
    fl = artifacts.detect(a, m, ctx, sp)["flags"]
    assert "low_bit_depth" in {f["id"] for f in fl}


def test_square_plateaus_are_drawn_not_clipped():
    t = np.arange(int(0.05 * SR)) / SR
    sq = 0.4 * np.sign(np.sin(2 * np.pi * 1000 * t))
    sq = np.round(sq * 32767) / 32767
    scan = hygiene.clip_scan(sq[:, None], "PCM_16")
    assert scan["flat_runs"] == 0 and scan["plateau_runs"] >= 1
    # a clipped sine still counts (entered by its own slope, not a jump across zero)
    s = np.round(np.clip(np.sin(2 * np.pi * 90 * t), -0.6, 0.6) * 32767) / 32767
    assert hygiene.clip_scan(s[:, None], "PCM_16")["flat_runs"] > 0


# ---------------------------------------------------------------- DC (finding: mean of a short decaying wave)

def test_dc_is_measured_not_the_mean_of_a_decaying_wave():
    t = np.arange(int(0.12 * SR)) / SR
    hit = 0.35 * np.sin(2 * np.pi * 180 * t) * np.exp(-t / 0.03)
    assert abs(hit.mean()) > 0.001                     # plain mean: would fail the 0.1 % FS gate
    assert A.dc_estimate(hit[:, None], SR) < 0.0002     # no DC at all
    assert abs(A.dc_estimate((hit + 0.002)[:, None], SR) - 0.002) < 0.0003
    sp = S.from_mapping({"id": "hit.t1", "group": "hit_small"})
    m, _ = features.analyze(A.from_array(hit, SR), sp)
    assert m["dc_offset"] < 0.001 < m["mean_abs"]


# ---------------------------------------------------------------- head silence null (finding: null still checked 5 ms)

def test_explicit_null_head_limit_is_not_checked(tmp_path):
    card = S.from_mapping({"id": "music.calm", "critic": {"group": "music", "head_max_ms": None, "loop": True,
                                                           "stereo": True}})
    assert card.head_max_ms is None and S.from_mapping({"id": "x", "group": "music"}).head_max_ms is None
    n = int(round(8 * 4 * 60 / 84 * SR))
    x = np.zeros(n)
    beat = int(60 / 84 * SR)
    for k in range(1, 32):                              # stem enters on beat 2
        s = k * beat
        m = min(int(0.3 * SR), n - s)
        tt = np.arange(m) / SR
        x[s:s + m] += 0.2 * np.sin(2 * np.pi * 220 * tt) * np.exp(-tt * 8)
    a = A.from_array(np.stack([x, x], 1), SR)
    m, _ = features.analyze(a, card)
    g, _ = hygiene.gate(a.data, a.sr, m, card, "final")
    assert m["head_silence_ms"] > 700 and "head_silence" not in g["failed"]
    assert "head_silence" not in {c["id"] for c in g["checks"]}


# ---------------------------------------------------------------- smeared attack (finding: late embers read as a slow crack)

def test_late_high_events_are_tail_not_a_smeared_crack():
    t = np.arange(int(0.3 * SR)) / SR
    thump = 0.8 * np.sin(2 * np.pi * np.cumsum(80 - 30 * np.minimum(t / 0.07, 1)) / SR) * np.exp(-t / 0.05)
    thump[: int(0.0015 * SR)] *= np.linspace(0, 1, int(0.0015 * SR))
    rng = np.random.default_rng(4)
    embers = np.zeros_like(t)
    for at in (0.085, 0.18, 0.22):                      # crackle after the attack
        i = int(at * SR)
        embers[i: i + 96] += synth._band(rng.standard_normal(96), 3000, 9000) * np.hanning(96) * 2.0
    x = synth.fix_chain(thump + embers)
    sp = S.from_mapping({"id": "fire.impact.a"})
    assert sp.group == "hit_fire"
    m, ctx = features.analyze(A.from_array(x, SR), sp)
    flags = {f["id"] for f in artifacts.detect(A.from_array(x, SR), m, ctx, sp)["flags"]}
    assert "smeared_attack" not in flags
    l2 = features.l2_score(m, sp)
    assert "transient_hf_share_db" not in {r["feature"] for r in l2["targets"]}    # no crack wanted


def test_shot_launch_floor_catches_a_thin_copy():
    sp = S.from_mapping({"id": "arrow-fire"})
    thin = {"share_150_800": 0.0, "share_below_120": 0.0, "mud_share": 0.0, "duration_ms": 200, "attack_ms": 2}
    full = dict(thin, share_150_800=0.4)
    assert features.l2_score(thin, sp)["score"] < features.l2_score(full, sp)["score"]


# ---------------------------------------------------------------- pitch wobble on recorded sources

def test_wobble_is_not_flagged_on_recorded_or_coded_sources():
    t = np.arange(int(1.0 * SR)) / SR
    f = 523.25 * 2 ** (40 * np.sin(2 * np.pi * 5 * t) / 1200)        # a played vibrato, 40 cents
    x = synth.fix_chain(0.5 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.5))
    sp = S.from_mapping({"id": "word-hit", "group": "reward"})
    a = A.from_array(x, SR)
    m, ctx = features.analyze(a, sp)
    unknown = artifacts.detect(a, m, ctx, sp)
    recorded = artifacts.detect(a, m, ctx, sp, ai_generated=False)
    assert "pitch_wobble" in {f["id"] for f in unknown["flags"]}
    assert "pitch_wobble" not in {f["id"] for f in recorded["flags"]}
    assert recorded["metrics"]["pitch_wobble_cents"] == unknown["metrics"]["pitch_wobble_cents"]


def test_provenance_from_a_build_record_and_a_sampler_report(tmp_path):
    from critic import policy
    src = tmp_path / "SOURCES.json"
    src.write_text(json.dumps({"$version": "audiolab.sources/1", "a.ogg": {
        "sha256": "a" * 64, "masterSha256": "b" * 64,
        "layers": [{"id": "x", "kind": "sampler", "rawQa": {"verdict": "PASS"}},
                   {"id": "y", "kind": "synth"}]}}), "utf-8")
    pol = policy.load([str(src)], libraries=tmp_path / "libs")
    assert pol.provenance(tmp_path / "m.wav", "b" * 64) == {"kind": "build", "ai_generated": False}
    assert pol.source_qa("b" * 64) == {"checked": 1, "failed": [], "excepted": [], "unchecked": []}
    (tmp_path / "s.json").write_text(json.dumps({"sources": [], "notes": []}), "utf-8")
    assert pol.provenance(tmp_path / "s.wav", "c" * 64)["kind"] == "sampler"
    assert pol.provenance(tmp_path / "z.wav", "d" * 64) == {}


# ---------------------------------------------------------------- CLAP windows (finding: rand_trunc made scores random)

def test_long_inputs_use_fixed_windows():
    x = np.arange(15 * 48000, dtype=np.float32)
    w1 = learned.windows(x, 480000, 6)
    w2 = learned.windows(x, 480000, 6)
    assert [len(w) for w in w1] == [480000, 480000] and all((a == b).all() for a, b in zip(w1, w2))
    assert w1[0][0] == 0 and w1[-1][-1] == x[-1]
    assert len(learned.windows(x[:1000], 480000, 6)) == 1
