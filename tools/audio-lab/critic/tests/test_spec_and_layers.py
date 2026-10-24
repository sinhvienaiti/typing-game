import numpy as np
import pytest

from critic import artifacts, audio as A, features, groups, learned, psycho
from critic import spec as S
from critic.tests import synth


@pytest.mark.parametrize("sid,group", [
    ("key.ok", "key_ok"), ("key-wrong", "key_bad"), ("ui.click", "ui"), ("word-hit", "reward"),
    ("gun.xung", "shot_gun"), ("arrow-fire", "shot_launch"), ("hit.t1", "hit_small"), ("hit.t4", "hit_heavy"),
    ("fire.impact.a", "hit_fire"), ("blast", "explosion"), ("kill.swarm", "death_swarm"),
    ("enemy.quadruped.death", "death_big"), ("dragon.roar", "creature"), ("alarm.surge", "alarm"),
    ("amb.forest", "ambience"), ("wave.horn", "stinger"), ("music.calm", "music"), ("something", None),
])
def test_group_from_id(sid, group):
    assert groups.infer_group(sid) == group


def test_duration_forms_and_overrides(tmp_path):
    assert S.from_mapping({"duration_ms": [80, 350]}).duration_ms == (80.0, 350.0)
    assert S.from_mapping({"lengthMs": 120}).duration_ms == (120.0, 120.0)
    assert S.from_mapping({"duration": {"min_ms": 10, "max_ms": 20}}).duration_ms == (10.0, 20.0)
    assert S.from_mapping({"duration_s": 1.5}).duration_ms == (1500.0, 1500.0)
    sp = S.from_mapping({"id": "gun.xung", "critic": {"attack_max_ms": 5}})
    assert sp.group == "shot_gun" and sp.dirty and sp.attack_max_ms == 5
    p = tmp_path / "c.yaml"
    p.write_text("- id: gun.xung\n  refs: [r/a.wav]\n- id: gun.tia\n", encoding="utf-8")
    cards = S.load_cards(p)
    assert S.match("gun.xung-3", cards).id == "gun.xung"
    assert S.match("gun.tia_v2", cards).id == "gun.tia"
    assert S.match("other", cards) is None
    assert cards[0].refs[0].endswith("r/a.wav")
    assert S.stem_id("gun.xung-3") == "gun.xung" and S.stem_id("hit.t1_v02") == "hit.t1"


def test_trapezoid_desirability():
    t = groups.at_least("crest_db", 12, 6)
    assert t.desirability(14) == 1 and t.desirability(6) == 0 and t.desirability(9) == pytest.approx(0.5)
    t = groups.between("duration_ms", 50, 150)
    assert t.desirability(100) == 1 and t.desirability(170) == pytest.approx(0.333, abs=0.01)


def test_refs_replace_targets_with_p10_p90():
    a = A.from_array(synth.punchy(), 48000)
    sp = S.from_mapping({"group": "hit_heavy"})
    m, _ = features.analyze(a, sp)
    st = features.ref_stats([dict(m, crest_db=c) for c in (30, 31, 32, 33, 34)])
    rows = {r["feature"]: r for r in features.l2_score(m, sp, st)["targets"]}
    assert rows["crest_db"]["source"] == "refs" and rows["crest_db"]["d"] < 1


def test_l1b_flags_pre_echo_and_noise_floor():
    rng = np.random.default_rng(0)
    x = synth.punchy().copy()
    pre = 0.02 * rng.standard_normal(int(48000 * 0.03))      # smeared energy before the hit
    y = np.concatenate([np.zeros(2400), pre * np.linspace(0, 1, len(pre)), x])
    a = A.from_array(y, 48000)
    sp = S.from_mapping({"group": "hit_heavy"})
    m, ctx = features.analyze(a, sp)
    ids = {f["id"] for f in artifacts.detect(a, m, ctx, sp)["flags"]}
    assert "pre_echo" in ids
    hiss = synth.punchy() + 0.003 * rng.standard_normal(len(x))   # -50 dBFS floor
    a = A.from_array(hiss, 48000)
    m, ctx = features.analyze(a, sp)
    l1b = artifacts.detect(a, m, ctx, sp)
    assert "noise_floor" in {f["id"] for f in l1b["flags"]}
    a = A.from_array(synth.punchy(), 48000)
    m, ctx = features.analyze(a, sp)
    assert artifacts.detect(a, m, ctx, sp)["flags"] == []


def test_l1b_stereo_mismatch():
    x = synth.punchy()
    st = np.stack([x, -x * 0.9], axis=1)
    a = A.from_array(st, 48000)
    sp = S.from_mapping({"group": "ambience"})
    m, ctx = features.analyze(a, sp)
    assert "stereo_mismatch" in {f["id"] for f in artifacts.detect(a, m, ctx, sp)["flags"]}


def test_pitch_and_wobble_for_pitched_groups():
    t = np.arange(int(48000 * 0.8)) / 48000
    f = 440 * 2 ** (35 / 1200 * np.sin(2 * np.pi * 6 * t))          # ±35 cent vibrato
    x = 0.5 * np.sin(2 * np.pi * np.cumsum(f) / 48000) * np.exp(-t / 0.5)
    a = A.from_array(synth.fade_out(x, 10), 48000)
    sp = S.from_mapping({"group": "reward"})
    m, ctx = features.analyze(a, sp)
    assert abs(m["f0_hz"] - 440) < 6 and m["pitch_off_cents"] < 15
    assert "pitch_wobble" in {f["id"] for f in artifacts.detect(a, m, ctx, sp)["flags"]}


def test_mosqito_runs_or_reports_unavailable():
    out = psycho.measure(synth.punchy(), 48000, 0.0, -14.0)
    if psycho.AVAILABLE:
        assert out["sharpness_acum"] > 0 and out["roughness_asper"] is not None
    else:
        assert out["available"] is False and out["reason"]


def test_repetition_for_short_sounds():
    s = np.ones(4800, dtype=np.float32)
    x = learned.repetition([s], 48000, 6.0)
    assert 3.0 <= len(x) / 48000 <= 4.0
    on = np.flatnonzero(np.diff((x > 0).astype(int)) == 1)
    assert len(on) + 1 >= 10
    item = learned.Item("k", A.from_array(synth.weak_click(), 48000), S.from_mapping({"group": "key_ok"}))
    assert item.short and 3.0 <= len(item.mono(16000)) / 16000 <= 4.0


def test_card_loop_eval_turns_the_repetition_on_for_longer_files():
    """critic.loop_eval.enabled (specs card) repeats a 350 ms shot at its rhythm; without it the file is scored alone."""
    sr = 48000
    shot = np.zeros(int(0.35 * sr), dtype=np.float32)
    shot[:2400] = 0.5
    a = A.from_array(shot, sr)
    card = {"id": "gun.xung", "critic": {"rate_hz": 5, "loop_eval": {"enabled": True, "interval_ms": 200}}}
    on = learned.Item("on", a, S.from_mapping(card))
    assert on.spec.loop_eval and on.short and on.input_kind == "repetition"
    assert 3.0 <= len(on.mono(16000)) / 16000 <= 4.0
    off = learned.Item("off", a, S.from_mapping({"id": "gun.xung", "critic": {"loop_eval": {"enabled": False}}}))
    assert not off.spec.loop_eval and not off.short and off.input_kind == "file"
    tiny = learned.Item("tiny", A.from_array(synth.weak_click(), sr), S.from_mapping({"group": "key_ok", "loop_eval": {"enabled": False}}))
    assert tiny.short                                    # under 300 ms the plan's repetition always holds
    assert S.from_json(on.spec.to_json()).loop_eval is True


def test_no_ai_sources_never_reach_models():
    assert learned.no_ai("/Users/x/AudioLab/libraries/_no-ai/sonniss/a.wav")
    assert not learned.no_ai("/Users/x/AudioLab/libraries/kenney/a.ogg")


def test_l5_and_kad_on_toy_embeddings():
    rng = np.random.default_rng(1)
    refs = {f"r{i}": v / np.linalg.norm(v) for i, v in enumerate(rng.normal(0, 0.05, (8, 16)) + np.eye(16)[0])}
    near = refs["r0"] * 0.99 + 0.01 * np.eye(16)[1]
    far = np.eye(16)[5]
    res, batch = learned.run_l5({"near": near / np.linalg.norm(near), "far": far}, refs)
    assert res["near"]["flags"] == [] and res["far"]["flags"][0]["id"] == "ref_far"
    x = rng.normal(0, 1, (30, 8))
    assert learned.kad(x, rng.normal(0, 1, (30, 8))) < learned.kad(x, rng.normal(3, 1, (30, 8)))


def test_pitch_wobble_judges_the_longest_held_note():
    """A sampler phrase changes note; only the held note's wobble counts (§4.3.2)."""
    import numpy as np

    from critic.artifacts import wobble

    t = np.linspace(0, 1.2, 120)
    steady = np.where(t < 0.4, 523.25, np.where(t < 0.8, 587.33, 783.99)) * 2 ** (3 * np.sin(2 * np.pi * 5 * t) / 1200)
    assert wobble((t, steady)) < 10
    vib = 523.25 * 2 ** (35 * np.sin(2 * np.pi * 5 * t) / 1200)
    assert wobble((t, vib)) > 20
