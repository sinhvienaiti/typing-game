import numpy as np
import pytest

from critic import audio as A, features, hygiene, pipeline
from critic import spec as S
from critic.tests import synth
from critic.thresholds import L1


def test_l1_blocks_exactly_the_broken_ones(synth_run):
    res = synth_run["res"]
    blocked = {n for n, r in res.items() if r["verdict"] == "BLOCK"}
    assert blocked == set(synth.BROKEN)
    for n in synth.CLEAN:
        assert res[n]["verdict"] == "PASS", (n, res[n]["L1"]["failed"])


@pytest.mark.parametrize("name,check", sorted(synth.BROKEN.items()))
def test_l1_names_the_defect(synth_run, name, check):
    r = synth_run["res"][name]
    assert check in r["L1"]["blocking"], r["L1"]["failed"]


def test_weak_and_muddy_are_quality_not_hygiene(synth_run):
    # taste problems must only lower the rank, never block
    for n in ("imp_weak", "imp_muddy"):
        assert synth_run["res"][n]["L1"]["pass"] is True


def test_l1b_flags_but_never_blocks(synth_run):
    for n, fid in synth.FLAGGED_ONLY.items():
        r = synth_run["res"][n]
        assert r["verdict"] == "PASS"
        assert fid in {f["id"] for f in r["flags"]}
        assert r["ask_owner"]["value"] and r["read_card"]
    assert not synth_run["res"]["imp_punchy"]["flags"]


def test_clip_is_measured_on_the_raw_samples(synth_run):
    r = synth_run["res"]["imp_clipped"]
    c = {x["id"]: x for x in r["L1"]["checks"]}
    assert not c["clip_full_scale"]["ok"] and c["clip_full_scale"]["measured_on"] == "raw"
    assert c["clip_full_scale"]["fix"] == "reject"


def _gate(x, sr=48000, group="hit_heavy", stage="final", **card):
    a = A.from_array(x, sr)
    sp = S.from_mapping({"group": group, **card})
    m, _ = features.analyze(a, sp)
    return hygiene.gate(a.data, sr, m, sp, stage)[0]


def test_raw_stage_turns_fixable_failures_into_fixes():
    g = _gate(synth.head_silence(), stage="raw")
    assert g["verdict"] == "NEEDS_FIX" and "trim_head" in g["fixes"] and not g["blocking"]
    g = _gate(synth.with_dc(), stage="raw")
    assert g["verdict"] == "NEEDS_FIX" and "hpf" in g["fixes"]
    g = _gate(synth.clipped(), stage="raw")
    assert g["verdict"] == "BLOCK" and "clip_full_scale" in g["blocking"]


def test_flat_top_after_normalisation_still_blocks():
    # PCM16 clipped then turned down: under 0.999 FS, caught by the flat-top rule
    x = np.round(synth.clipped() * 32767) / 32767 * 0.7
    scan = hygiene.clip_scan(x[:, None])
    assert scan["full_runs"] == 0 and scan["flat_runs"] > 0
    assert "clip_flat_top" in _gate(x)["blocking"]


def test_smooth_low_crest_at_16_bit_is_not_a_flat_top():
    x = np.round(synth.smooth_lf_crest_16bit() * 32767) / 32767
    a = np.abs(x)
    eq = (a[1:] == a[:-1]) & (a[1:] > 0.1)
    s, n = hygiene.runs(eq)
    assert (n >= 3).any(), "fixture must contain >= 4 equal samples at a crest"
    assert hygiene.clip_scan(x[:, None])["flat_runs"] == 0


def test_true_peak_limit_is_minus_one_dbtp():
    x = synth.norm_peak(synth.punchy(), -0.5)
    g = _gate(x)
    assert "true_peak" in g["blocking"]
    assert _gate(synth.norm_peak(synth.punchy(), -1.5))["verdict"] == "PASS"


def test_tail_passes_with_a_5ms_fade_and_fails_without():
    x = synth.punchy()[: int(48000 * 0.12)]
    assert "tail" in _gate(x)["failed"]
    assert "tail" not in _gate(synth.fade_out(x, 6))["failed"]


def test_head_silence_limits_follow_the_group():
    x = np.concatenate([np.zeros(int(48000 * 0.004)), synth.punchy()])   # 4 ms
    assert "head_silence" not in _gate(x, group="hit_heavy")["failed"]   # <= 5 ms
    assert "head_silence" in _gate(x, group="ui", duration_ms=[10, 600])["failed"]   # <= 2 ms


def test_duration_vs_spec_card_tolerance():
    x = synth.punchy(0.45)
    assert "duration" not in _gate(x, duration_ms=400)["failed"]          # +12.5 %
    assert "duration" in _gate(x, duration_ms=300)["failed"]              # +50 %
    # specs-lane mapping: target ± tolerance_pct, never a second 20 % on top of min/max
    card = {"target_ms": 375, "tolerance_pct": 20, "min_ms": 300, "max_ms": 450}
    assert "duration" not in _gate(x, duration=card)["failed"]            # 450 ms = +20 %
    card = {"target_ms": 360, "tolerance_pct": 20, "min_ms": 288, "max_ms": 432}
    assert "duration" in _gate(x, duration=card)["failed"]                # +25 %
    card = {"target_ms": 449, "tolerance_ms": 1, "tolerance_pct": None}   # music-style exact length
    assert "duration" not in _gate(x, duration=card)["failed"]
    card = {"target_ms": 447, "tolerance_ms": 1, "tolerance_pct": None}
    assert "duration" in _gate(x, duration=card)["failed"]


def test_loop_seam_thresholds():
    seamless = features.seam(synth.loop(True)[:, None], 48000)
    broken = features.seam(synth.loop(False)[:, None], 48000)
    assert seamless["jump_excess_dbfs"] < L1["loop_jump_max_dbfs"]
    assert seamless["rms_diff_db"] < L1["loop_rms_max_db"]
    assert broken["rms_diff_db"] > L1["loop_rms_max_db"] or broken["jump_excess_dbfs"] > L1["loop_jump_max_dbfs"]


def test_music_loop_length_and_seam():
    card = {"bpm": 96, "bars": 8}
    ok = _gate(synth.music_loop(), group="music", **card)
    assert ok["verdict"] == "PASS", ok["failed"]                  # downbeat after a decayed tail is fine
    c = {x["id"]: x for x in ok["checks"]}
    assert c["music_length"]["value"] <= 1.0 and c["loop_seam"]["ok"]
    assert "music_length" in _gate(synth.music_loop(extra_ms=10), group="music", **card)["blocking"]
    assert "loop_seam" in _gate(synth.music_loop(click=True), group="music", **card)["blocking"]
    # the same bar-line change in an ambience bed is a seam fault (RMS jump)
    assert "loop_seam" in _gate(synth.music_loop(), group="ambience")["failed"]


def test_stereo_allowed_only_where_the_plan_says():
    st = np.stack([synth.loop(True), synth.loop(True)], axis=1)
    assert "channels" not in _gate(st, group="ambience")["failed"]
    st = np.stack([synth.punchy(), synth.punchy()], axis=1)
    assert "channels" in _gate(st, group="hit_heavy")["failed"]


def test_silent_file_blocks():
    g = _gate(np.zeros(4800))
    assert g["verdict"] == "BLOCK" and "silent" in g["blocking"]
