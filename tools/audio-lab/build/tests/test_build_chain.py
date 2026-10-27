import numpy as np
import pytest

from build import chain, measure, recipe
from build.tests.helpers import impact

SR = 48000


def _params(**over):
    p = recipe.chain_params({"layers": []})
    p.update(over)
    return p


def test_chain_removes_head_silence():
    x = np.concatenate([np.zeros(int(0.25 * SR)), 1e-6 * np.random.default_rng(1).standard_normal(SR // 20), impact(3)])
    assert measure.head_ms(x, SR) > 250
    y, rep = chain.run(x, SR, _params())
    assert measure.head_ms(y, SR) <= 2.0             # keys/UI limit (§4.3.1)
    assert rep["headCutMs"] >= 290


@pytest.mark.parametrize("seed", range(6))
def test_chain_never_clips(seed):
    rng = np.random.default_rng(seed)
    # Hot, clipped-looking input: +12 dB over full scale, square-ish bursts, DC.
    x = 4.0 * np.tanh(3 * rng.standard_normal(int(SR * rng.uniform(0.05, 1.5)))) + 0.01
    for mode, target in (("lufs-m-max", -20.0), ("lufs-m-max", -6.0), ("lufs-s-max", -14.0), ("peak", -1.0)):
        y, rep = chain.run(x, SR, _params(normalise={"mode": mode, "target": target}))
        assert measure.true_peak_db(y, SR) <= -1.0 + 1e-6
        assert np.max(np.abs(y)) < 0.999
        assert rep["safetyGainDb"] <= 0


def test_chain_removes_dc_and_fades_tail():
    x = impact(5, ms=200) * 0.5 + 0.01
    y, _ = chain.run(x, SR, _params())
    from critic.audio import dc_estimate
    assert dc_estimate(y, SR) < 0.001               # < 0.1 % FS (true DC, §4.3.1)
    assert abs(y[-1, 0]) < 1e-4


def test_chain_hits_common_level():
    t = np.arange(int(0.6 * SR)) / SR
    x = 0.05 * np.sin(2 * np.pi * 220 * t) * np.exp(-t / 0.3)      # low crest: no limiting needed
    y, rep = chain.run(x, SR, _params())
    assert abs(measure.lufs_m_max(y, SR) + 20.0) <= 0.2
    assert rep["shortfallDb"] == 0 and rep["limiterGrDb"] == 0


def test_chain_reports_shortfall_instead_of_squashing():
    x = impact(7, ms=60)                                              # 60 ms click cannot reach -20 LUFS-M
    y, rep = chain.run(x, SR, _params())
    assert rep["limiterGrDb"] <= 6.0 + 0.05
    assert rep["shortfallDb"] > 0.5
    assert abs(measure.lufs_m_max(y, SR) - (rep["target"] - rep["shortfallDb"])) <= 0.3


def test_loop_keeps_head_and_crossfades():
    t = np.arange(int(2.0 * SR)) / SR
    x = 0.3 * np.sin(2 * np.pi * 110 * t) + 0.05 * np.random.default_rng(2).standard_normal(t.size)
    p = recipe.chain_params({"layers": [], "loop": True, "chain": {"loopCrossfadeMs": 50}})
    y, rep = chain.run(x, SR, p, loop=True)
    assert "headCutMs" not in rep and "tailCutMs" not in rep
    assert y.shape[0] == x.size - int(0.05 * SR)
    jump = abs(y[-1, 0] - y[0, 0])
    assert jump < 0.05


def test_exp_tail_caps_a_ringing_sound_without_a_flat_cut():
    """Batch 0b review: a ring cut by maxLengthMs decays exponentially to the floor, no cut-then-fade."""
    t = np.arange(int(0.3 * SR)) / SR
    x = np.sin(2 * np.pi * 2500 * t) * np.exp(-t / 0.08)            # rings for 200+ ms
    norm = {"normalise": {"mode": "none"}}
    old, _ = chain.run(x, SR, _params(maxLengthMs=96, tail={"floorDb": -60, "fadeMs": 25}, headTrim=None, **norm))
    new, rep = chain.run(x, SR, _params(maxLengthMs=96, tail={"floorDb": -60, "shape": "exp", "kneeMs": 30},
                                        headTrim=None, **norm))
    assert new.shape[0] == old.shape[0] == int(0.096 * SR)
    assert rep["tailShape"]["shape"] == "exp" and rep["tailShape"]["capped"] and rep["tailShape"]["knee_ms"] == 30.0

    def level(y, a_ms, b_ms):
        seg = y[int(a_ms * SR / 1000):int(b_ms * SR / 1000), 0]
        return 10 * np.log10(np.mean(seg ** 2) + 1e-20)
    ref = level(new, 0, 10)
    steps = [level(new, a, a + 10) - ref for a in range(30, 90, 10)]
    assert all(b < a for a, b in zip(steps, steps[1:]))               # keeps falling, no flat stretch
    d = np.diff(steps)
    assert d.max() - d.min() < 3.0                                     # about straight in dB: exponential
    assert level(new, 86, 96) - ref < -45                              # reaches the floor at the cap
    assert level(old, 60, 70) - level(old, 30, 40) > -8                # the old way stays flat, then fades
    assert np.allclose(new[: int(0.03 * SR), 0], old[: int(0.03 * SR), 0])
