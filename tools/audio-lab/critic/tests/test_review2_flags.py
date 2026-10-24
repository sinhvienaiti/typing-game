"""Batch 0b review 2 additions: two onsets in one shot (double_onset), channel balance of stereo
files (lr_imbalance), a near-mono bed read by its side level (near_mono)."""
from __future__ import annotations

import json

import numpy as np
import soundfile as sf
import yaml

from critic import pipeline

SR = 48000


def _card(tmp, sid, group, **over):
    c = {"id": sid, "game": "typing-survival", "critic": {"group": group, **over}}
    p = tmp / f"{sid}.yaml"
    p.write_text(yaml.safe_dump(c), "utf-8")
    return p


def _run(tmp, files: dict[str, np.ndarray], card) -> dict[str, dict]:
    ind = tmp / "in"
    ind.mkdir(exist_ok=True)
    for name, x in files.items():
        sf.write(str(ind / f"{name}.wav"), x, SR, subtype="PCM_24")
    out = tmp / "out"
    pipeline.run([str(ind)], spec_path=str(card), out_dir=out,
                 opts=pipeline.Options(layers=("L1", "L1b", "L2"), quiet=True))
    return {n: json.loads((out / f"{n}.json").read_text()) for n in files}


def _shot(second_at_ms: float | None, second_gain: float, seed: int = 3) -> np.ndarray:
    """A crack (noise burst, 4 ms decay) over a low body; optionally a second crack later."""
    from scipy import signal
    rng = np.random.default_rng(seed)
    n = int(0.12 * SR)
    t = np.arange(n) / SR
    crack = signal.sosfilt(signal.butter(4, 2500, "high", fs=SR, output="sos"), rng.standard_normal(n))
    x = 0.5 * crack * np.exp(-t / 0.004)
    x += 0.5 * np.sin(2 * np.pi * 90 * t) * np.exp(-t / 0.03)
    if second_at_ms is not None:
        k = int(second_at_ms / 1000 * SR)
        x[k:] += second_gain * 0.5 * crack[:n - k] * np.exp(-t[:n - k] / 0.004)
    x *= np.minimum(1.0, (n - np.arange(n)) / (0.01 * SR))       # fade the end
    return (0.8 * x / np.abs(x).max())[:, None]


def test_a_second_crack_25_ms_later_is_a_double_onset(tmp_path):
    card = _card(tmp_path, "gun.test", "shot_gun", duration_ms={"target_ms": 120, "tolerance_pct": 20})
    res = _run(tmp_path, {"gun.test__A__s1": _shot(25.0, 0.8), "gun.test__B__s1": _shot(None, 0.0)}, card)
    a, b = res["gun.test__A__s1"], res["gun.test__B__s1"]
    fa = {f["id"]: f for f in a["flags"]}
    assert "double_onset" in fa and 20 <= fa["double_onset"]["value"]["after_ms"] <= 30
    assert "double_onset" not in {f["id"] for f in b["flags"]}
    assert b["metrics"]["hf_reonset_db"] is not None and b["metrics"]["hf_reonset_db"] < -6


def _bed(seed: int, side_gain: float, right_gain: float = 1.0) -> np.ndarray:
    from scipy import signal
    from build import dsp
    rng = np.random.default_rng(seed)
    n = int(6.5 * SR)
    mid = signal.sosfilt(signal.butter(1, 3000, "low", fs=SR, output="sos"), rng.standard_normal(n)) * 0.1
    side = signal.sosfilt(signal.butter(1, 3000, "low", fs=SR, output="sos"), rng.standard_normal(n)) * 0.1 * side_gain
    x = np.stack([mid + side, (mid - side) * right_gain], axis=1)
    return dsp.loop_crossfade(x, 500, SR)


def test_stereo_beds_balance_and_side_level(tmp_path):
    card = _card(tmp_path, "amb.test", "ambience", loop=True, stereo=True, head_max_ms=None, attack_max_ms=None,
                 duration_ms={"target_ms": 6000, "tolerance_pct": 20})
    res = _run(tmp_path, {"amb.test__A__s1": _bed(1, 0.6),             # wide, balanced
                          "amb.test__B__s1": _bed(2, 0.25),            # side about -12 dB under the mid
                          "amb.test__C__s1": _bed(3, 0.6, 2.0)}, card)  # right channel 6 dB louder
    ids = {k: {f["id"] for f in v["flags"]} for k, v in res.items()}
    assert not ids["amb.test__A__s1"] & {"near_mono", "lr_imbalance"}
    b = res["amb.test__B__s1"]["metrics"]
    assert "near_mono" in ids["amb.test__B__s1"] and b["stereo_correlation"] < 0.98 and b["side_mid_db"] <= -10
    c = res["amb.test__C__s1"]
    assert "lr_imbalance" in ids["amb.test__C__s1"] and c["metrics"]["lr_balance_db"] < -5
    msg = next(f["msg_vi"] for f in c["flags"] if f["id"] == "lr_imbalance")
    assert "nghiêng sang phải" in msg


def test_a_beating_clank_is_one_onset():
    """hit.t1 recipe (review 2): its highs beat with dips of ~4.6 dB every 12 ms; that is one hit,
    so the double-onset rule wants the band to fall >= 6 dB before it comes back."""
    from critic import features as F
    n = int(0.1 * SR)
    t = np.arange(n) / SR
    x = (np.sin(2 * np.pi * 3000 * t) + 0.3 * np.sin(2 * np.pi * 3080 * t)) * np.exp(-t / 0.08)
    x += 0.5 * np.sin(2 * np.pi * 400 * t) * np.exp(-t / 0.03)
    r = F.hf_reonset(0.5 * x, SR)
    assert r["hf_reonset_db"] >= -6.0 and r["hf_reonset_rise_db"] >= 4.0     # it does come back ...
    assert r["hf_reonset_dip_db"] > -6.0                                      # ... but never fell far
