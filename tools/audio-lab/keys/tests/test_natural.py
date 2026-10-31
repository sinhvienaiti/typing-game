"""Typing Feel Format natural-v1 (TYPING_FEEL_SERVICE.md §3.8, §3.9, §8.1): onsets.py, natural.py, `keys natural`.

Synthetic takes cover counts, lengths, reruns and every upload-rule message. The owner's real takes, when this machine
has them (tmp/keys-firefly), must give back the published raindrop-tile and hail-stone samples. Read-only on the
sources and on typing-feel/public: the published sets are copied into tmp_path first.
"""
import json
import os
import re
import shutil
import subprocess
from pathlib import Path

import numpy as np
import pytest
import soundfile as sf

from common import env
from keys import natural, onsets, pipeline

SR = 48000
REPO = env.REPO
TAKES = REPO / "tmp" / "keys-firefly"
PUBLIC_KEYS = REPO / "typing-feel" / "public" / "v1" / "keys"
CONTRACT = REPO / "typing-feel" / "contract" / "typing-feel.v1.json"
# Decoded PCM of a rerun against the published OGG: same recipe, same libsndfile/libvorbis, so the samples come out
# identical (max difference 0.0 on all 58 files, 31/10). 2**-20 (about -120 dBFS) only lets a decoder round floats
# differently; any change to a cut, a gain or the encoder shows up.
PCM_TOL = 2.0 ** -20
GAPS_MS = (380, 470, 520, 610, 430, 900, 400, 560)


# ---------------------------------------------------------------- synthetic takes
def tap(rng, level_db, sr=SR, tau=0.018, ms=300):
    t = np.arange(int(ms / 1000 * sr)) / sr
    body = rng.standard_normal(len(t)) * 0.6 + np.sin(2 * np.pi * rng.uniform(1800, 3200) * t)
    y = body * np.exp(-t / tau)
    ramp = max(1, int(0.0003 * sr))
    y[:ramp] *= np.linspace(0, 1, ramp)
    return y / np.abs(y).max() * 10 ** (level_db / 20)


def make_take(path, taps=16, seconds=None, sr=SR, channels=2, subtype="PCM_16", gaps_ms=GAPS_MS, noise_db=-80.0,
              droplets=True, loud_tap=None, tau=0.018, lead_in_tap=None, seed=5):
    """Taps at known times (first at 0.3 s); two quiet droplets inside the 900 ms gaps; returns the tap times (s)."""
    rng = np.random.default_rng(seed)
    times, t = [], 0.3
    for i in range(taps):
        times.append(t)
        t += gaps_ms[i % len(gaps_ms)] / 1000
    seconds = seconds or times[-1] + 0.7
    n = int(seconds * sr)
    mono = rng.standard_normal(n) * 10 ** (noise_db / 20)
    for i, at in enumerate(times):
        level = 0.0 if i == loud_tap else -3.0 - 9.0 * rng.random()
        y = tap(rng, level, sr, tau)
        a = int(at * sr)
        if i == lead_in_tap:                 # a soft tick 24 dB under the strike, the strike 40 ms later
            tick = tap(rng, level - 24, sr, tau=0.03)
            mono[a:a + len(tick)] += tick[:n - a]
            a += int(0.040 * sr)
        mono[a:a + len(y)] += y[:max(0, n - a)]
        if droplets and gaps_ms[i % len(gaps_ms)] >= 900 and i + 1 < taps:
            d = tap(rng, -45.0, sr, tau=0.004, ms=40)
            b = int((at + 0.6) * sr)
            mono[b:b + len(d)] += d
    if loud_tap is not None:
        mono = np.clip(mono, -1, 1)
    if channels == 1:
        data = mono[:, None]
    else:
        side = rng.standard_normal((n, channels)) * 10 ** ((noise_db - 6) / 20)
        data = np.stack([mono * (1.0 - 0.08 * c) for c in range(channels)], axis=1) + side
        if loud_tap is not None:
            data = np.clip(data, -1, 1)
    sf.write(str(path), data, sr, subtype=subtype, format="WAV")
    return times


def kit_files(out):
    return sorted(p.name for p in Path(out).glob("*.ogg"))


def decoded(path):
    return sf.read(str(path), dtype="float64", always_2d=True)[0]


@pytest.fixture(scope="module")
def take16(tmp_path_factory):
    d = tmp_path_factory.mktemp("take16")
    times = make_take(d / "synthetic.wav")
    return d / "synthetic.wav", times


@pytest.fixture(scope="module")
def formatted_with_arrays(take16, tmp_path_factory):
    out = tmp_path_factory.mktemp("fmt") / "a"
    arrays = {}
    rep = natural.format_take(take16[0], out, "synthetic-set", "Synthetic Set", "Test", arrays=arrays)
    return out, rep, arrays


@pytest.fixture(scope="module")
def formatted(formatted_with_arrays):
    return formatted_with_arrays[:2]


# ---------------------------------------------------------------- onsets and counts
def test_onsets_find_every_tap_and_droplet(take16):
    path, times = take16
    rows = onsets.analyse(path)["hits"]
    taps = [h for h in rows if h["peakDb"] > -25]
    assert len(taps) == len(times) == 16
    assert len(rows) == 18                                   # 16 taps + 2 droplets 40 dB down
    for h, at in zip(taps, times):
        assert abs(h["onsetMs"] - at * 1000) < 2.0           # stepped back to the first sample above floor + 6 dB


def test_format_counts_lengths_manifest_and_files(formatted):
    out, rep = formatted
    assert rep["status"] == "formatted" and rep["acceptAllowed"] and rep["gates"]["pass"], rep["warnings"]
    assert rep["taps"]["found"] == 18 and rep["taps"]["usable"] == 16 and rep["taps"]["main"] == 16
    assert rep["counts"] == {"key": 16, "space": 8}
    assert kit_files(out) == sorted([f"key-{n:02d}.ogg" for n in range(1, 17)] + [f"space-{n:02d}.ogg" for n in range(1, 9)]
                                    + ["preview.ogg"])
    assert sorted(p.name for p in (out / "ab").iterdir()) == ["natural.mp3", "raw-cut.mp3"]
    man = json.loads((out / "keys-manifest.json").read_text())
    contract = json.loads(CONTRACT.read_text())["set"]
    assert man["schema"] == contract["schema"] == "typing-feel/set-1"
    assert list(man) == contract["required"]                  # nothing else: set-1 has no optional fields
    assert man["recipe"] == "natural-v1" and man["id"] == "synthetic-set" and man["preview"] == "preview.ogg"
    assert [f["file"] for f in man["files"]] == [f"key-{n:02d}.ogg" for n in range(1, 17)] + [f"space-{n:02d}.ogg" for n in range(1, 9)]
    pattern = re.compile(contract["file"]["filePattern"])
    for f in man["files"]:
        assert pattern.match(f["file"]) and f["set"] == f["file"].split("-")[0]
        data = decoded(out / f["file"])
        assert f["durationMs"] == round(len(data) / SR * 1000)
        assert f["durationMs"] <= (450 if f["set"] == "key" else round(450 * 2 ** (3 / 12)))
        assert data.shape[1] == 2 and sf.info(str(out / f["file"])).samplerate == SR
    lengths = {f["durationMs"] for f in man["files"] if f["set"] == "key"}
    assert 450 in lengths and min(lengths) < 450                # capped at 450, shorter when the next tap is closer
    pk = max(np.abs(decoded(out / f["file"])).max() for f in man["files"])
    assert -3.5 < 20 * np.log10(pk) < -1.0                      # the set is normalised to -2 dBFS before Vorbis
    assert rep["set"] == {"id": "synthetic-set", "name": "Synthetic Set", "family": "Test",
                          "licence": natural.DEFAULT_LICENCE}
    assert (out / "report.json").is_file() and json.loads((out / "report.json").read_text())["status"] == "formatted"


def test_spaces_are_the_longest_rooms_lowered_three_semitones(formatted):
    out, rep = formatted
    rows = rep["taps"]["rows"]
    main = [h for h in rows if h["peakDb"] > -25]
    want = sorted(range(len(main)), key=lambda i: -main[i]["gapToNextMs"])[:8]
    spaces = [r for r in rep["files"] if r["set"] == "space"]
    assert [r["tap"] for r in spaces] == [main[i]["n"] for i in want]
    for r in spaces:
        n = round(min(r["gapToNextMs"] - 2, 450) / 1000 * SR)
        assert r["durationMs"] == round(round(n / 2 ** (-3 / 12)) / SR * 1000)


def test_preview_is_one_second_and_fades_its_last_10_ms(formatted):
    out, rep = formatted
    p = decoded(out / "preview.ogg")
    assert len(p) == SR
    peak = np.abs(p).max()
    assert 20 * np.log10(np.sqrt(np.mean(p[-48:] ** 2)) / peak) < -40      # the last ms, after the Vorbis decoder
    assert rep["preview"]["gates"]["tail"] and rep["preview"]["fadeOutMs"] == 10.0
    pre = natural.fade_tail(np.ones((SR, 2)))
    assert pre[-1].max() == 0.0 and pre[-481].min() == 1.0 and np.all(np.diff(pre[-480:, 0]) <= 0)


def test_rerun_gives_the_same_pcm_not_necessarily_the_same_ogg_bytes(take16, formatted, tmp_path):
    out, rep = formatted
    rep2 = natural.format_take(take16[0], tmp_path / "b", "synthetic-set", "Synthetic Set", "Test")
    for name in kit_files(out):
        a, b = decoded(out / name), decoded(tmp_path / "b" / name)
        assert a.shape == b.shape and np.array_equal(a, b), name
    assert (out / "keys-manifest.json").read_bytes() == (tmp_path / "b" / "keys-manifest.json").read_bytes()
    assert [r["pcmSha256"] for r in rep["files"]] == [r["pcmSha256"] for r in rep2["files"]]
    assert rep["preview"]["pcmSha256"] == rep2["preview"]["pcmSha256"]


def test_report_numbers(formatted):
    out, rep = formatted
    for r in rep["files"]:
        for k in ("durationMs", "peakDbfs", "truePeakDbtp", "lufsMMax", "riseMs", "headMs", "mainStrikeMs",
                  "energyAfter120msPct", "pcmSha256", "gates"):
            assert r[k] is not None, (r["file"], k)
        assert r["truePeakDbtp"] <= -1.0 and not r["leadIn"]
    assert rep["loudness"]["min"] <= rep["loudness"]["max"] and rep["loudness"]["truePeakMaxDbtp"] <= -1.0
    assert rep["lengthsMs"]["key"][1] == 450
    assert rep["leadIns"] == [] and rep["upload"]["ok"]
    assert rep["ab"]["natural"]["lufsI"] is not None and rep["ab"]["rawCut"]["lufsI"] is not None
    tool = rep["tool"]
    assert tool["generator"].startswith("typing-feel natural-v1 (tools/audio-lab keys natural @")
    # Provenance pins the code even when HEAD does not hold it: '+dirty' and the modules' sha256.
    here = Path(natural.__file__).resolve().parent
    assert tool["files"] == {n: natural.sha256_file(here / n) for n in ("natural.py", "onsets.py")}
    if tool["gitSha"]:
        assert tool["generator"].endswith(f"@{tool['gitSha']}{'+dirty' if tool['dirty'] else ''})")
    else:
        assert tool["generator"].endswith("@unknown)") and tool["dirty"] is None
    assert rep["params"]["maxTapMs"] == 450 and rep["params"]["evenOut"] == {"amount": 0.6, "limitDb": 9.0, "headMs": 20.0}


# ---------------------------------------------------------------- the recipe pinned without the owner's takes
# tmp/keys-firefly is never in Git, so on a fresh clone only these tests guard natural-v1. They read the float arrays
# handed to the encoders (no codec bytes), so they hold on any machine with the same numpy.
GOLDEN = Path(__file__).with_name("natural_golden.json")
DB_TOL = 0.005
LONG_TAKES = ("preview.ogg", "natural.mp3", "raw-cut.mp3")


def level_db(a):
    return round(float(20 * np.log10(max(float(np.sqrt(np.mean(a ** 2))) if len(a) else 0.0, 1e-12))), 4)


def fingerprint(a, blocks=False):
    """Length, peak and level of the whole file, its first 20 ms and its last 25 ms (the fades); long takes add the
    level of every 250 ms block, which pins the 70 WPM rhythm and which tap plays where."""
    fp = {"frames": len(a), "peakDb": round(float(20 * np.log10(max(float(np.abs(a).max()), 1e-12))), 4),
          "rmsDb": level_db(a), "headDb": level_db(a[:round(0.020 * SR)]), "tailDb": level_db(a[-round(0.025 * SR):])}
    if blocks:
        step = round(0.25 * SR)
        fp["blocksDb"] = [level_db(a[i:i + step]) for i in range(0, len(a), step)]
    return fp


def test_recipe_parameters_are_the_owners_pick():
    p = natural.PARAMS
    assert p["fadeInMs"] == pytest.approx(0.6) and p["fadeOutMs"] == pytest.approx(25.0)
    assert {k: v for k, v in p.items() if k not in ("fadeInMs", "fadeOutMs")} == {
        "maxTapMs": 450.0, "eq": None,
        "mainTap": {"peakWithinDb": 25.0, "decay40BeforeNext": True},
        "evenOut": {"amount": 0.6, "limitDb": 9.0, "headMs": 20.0},
        "spaces": {"count": 8, "pick": "longest gapToNextMs", "semitones": -3.0, "gainDb": 1.5},
        "setPeakDbfs": -2.0, "maxKeys": 80, "sampleRate": 48000,
        "codec": "OGG Vorbis (libsndfile default quality)",
        "preview": {"seconds": 1.0, "fadeOutMs": 10.0},
        "abTakes": {"seconds": 16.0, "wpm": 70, "seeds": [7, 11]},
    }


def test_synthetic_golden_fingerprint_pins_the_recipe(formatted_with_arrays):
    """Every key, space, the preview and both A/B takes of the seed-5 take, before any encoder, against
    natural_golden.json (written from the code that reproduced raindrop-tile and hail-stone sample for sample, 31/10).
    Rewrite it only for an owner-approved recipe change: NATURAL_GOLDEN_WRITE=1 run.sh test <this file>."""
    _out, _rep, arrays = formatted_with_arrays
    got = {name: fingerprint(a, blocks=name in LONG_TAKES) for name, a in sorted(arrays.items())}
    if os.environ.get("NATURAL_GOLDEN_WRITE") == "1":
        GOLDEN.write_text(json.dumps(got, indent=1) + "\n")
        pytest.skip(f"wrote {GOLDEN.name}")
    want = json.loads(GOLDEN.read_text())
    assert sorted(got) == sorted(want)
    for name, w in want.items():
        g = got[name]
        assert g["frames"] == w["frames"], name
        for k in ("peakDb", "rmsDb", "headDb", "tailDb"):
            assert abs(g[k] - w[k]) <= DB_TOL, (name, k, g[k], w[k])
        if "blocksDb" in w:
            assert len(g["blocksDb"]) == len(w["blocksDb"]), name
            worst = max(abs(a - b) for a, b in zip(g["blocksDb"], w["blocksDb"]))
            assert worst <= DB_TOL, (name, "blocksDb", worst)
    # The set gain: the loudest sample of all keys and spaces lands on -2.00 dBFS.
    peak = max(float(np.abs(a).max()) for n, a in arrays.items() if n.startswith(("key-", "space-")))
    assert abs(20 * np.log10(peak) + 2.0) < 1e-6


def test_preview_pre_encode_is_the_render_with_a_10_ms_raised_cosine_tail(take16, formatted_with_arrays):
    _out, _rep, arrays = formatted_with_arrays
    chk = natural.check_upload(take16[0])
    b = natural.build(chk["analysis"]["stereo"], chk["analysis"]["hits"])
    unfaded = natural.master(natural.render(b["keys"], b["spaces"], seconds=1.0))
    pre = arrays["preview.ogg"]
    n = round(0.010 * SR)
    assert pre.shape == (SR, 2) and n == 480
    assert np.array_equal(pre[:-n], np.clip(unfaded[:-n], -1, 1))
    window = 0.5 + 0.5 * np.cos(np.linspace(0, np.pi, n))
    assert np.allclose(pre[-n:], np.clip(unfaded[-n:] * window[:, None], -1, 1), rtol=0, atol=1e-15)
    assert np.all(pre[-1] == 0.0)


def test_mono_and_44k1_takes_format(tmp_path):
    make_take(tmp_path / "mono.wav", channels=1)
    rep = natural.format_take(tmp_path / "mono.wav", tmp_path / "m")
    assert rep["status"] == "formatted" and rep["counts"] == {"key": 16, "space": 8}
    assert rep["set"]["id"] == "mono" and rep["set"]["name"] == "Mono"
    make_take(tmp_path / "cd.wav", sr=44100)
    rep = natural.format_take(tmp_path / "cd.wav", tmp_path / "c")
    assert rep["status"] == "formatted" and rep["counts"] == {"key": 16, "space": 8}
    assert sf.info(str(tmp_path / "c" / "key-01.ogg")).samplerate == SR


def test_lead_in_is_reported_never_trimmed(tmp_path):
    make_take(tmp_path / "lead.wav", lead_in_tap=3)
    rep = natural.format_take(tmp_path / "lead.wav", tmp_path / "o")
    tap4 = next(r for r in rep["files"] if r["file"] == "key-04.ogg")["tap"]
    from_tap4 = [r["file"] for r in rep["files"] if r["tap"] == tap4]       # key-04, and a space when its room is long
    assert [li["file"] for li in rep["leadIns"]] == from_tap4 and from_tap4[0] == "key-04.ogg"
    li = rep["leadIns"][0]
    assert 35 <= li["mainStrikeMs"] <= 50 and li["tickDb"] < -13
    row = next(r for r in rep["files"] if r["file"] == "key-04.ogg")
    assert row["durationMs"] == min(450, round(round((row["gapToNextMs"] - 2) / 1000 * SR) / SR * 1000))
    assert any(w.startswith("key-04.ogg: soft tick, then the main strike") for w in rep["warnings"])
    assert rep["acceptAllowed"]


def test_full_scale_tap_warns_and_is_kept(tmp_path):
    times = make_take(tmp_path / "hot.wav", loud_tap=5)
    res = natural.check_upload(tmp_path / "hot.wav")
    assert res["ok"] and res["errors"] == []
    assert res["warnings"] == [f"Tap at {times[5]:.1f} s reaches full scale; check it in the A/B."]
    assert res["source"]["tapsClipped"] == 0
    rep = natural.format_take(tmp_path / "hot.wav", tmp_path / "o")
    assert rep["counts"]["key"] == 16 and rep["loudness"]["truePeakMaxDbtp"] <= -1.0
    assert rep["acceptAllowed"] and rep["gates"]["pass"]           # near full scale is not clipping


def clipped_take(path, tap=5, boost=30.0):
    """One tap pushed +30 dB into the rails and cut at full scale, as a recorder clips (flat tops), 16-bit."""
    times = make_take(path.with_name("base-" + path.name), subtype="FLOAT")
    x, sr = sf.read(str(path.with_name("base-" + path.name)), always_2d=True)
    a = int(times[tap] * sr)
    x[a:a + int(0.3 * sr)] *= boost
    sf.write(str(path), np.clip(x, -1.0, 1.0), sr, subtype="PCM_16")
    return times


def test_clipped_tap_warns_that_accept_will_stay_locked(tmp_path):
    times = clipped_take(tmp_path / "clip.wav")
    res = natural.check_upload(tmp_path / "clip.wav")
    assert res["ok"] and res["errors"] == []                       # a warning, as decision 7 keeps peaks: never refused
    (msg,) = res["warnings"]
    assert msg == (f"Tap at {times[5]:.1f} s is clipped (flat tops); Format keeps it as recorded, so key-06 and space-04 "
                   "fail the clip gate and Accept stays locked. Record the take again a little quieter.")
    assert res["source"]["tapsClipped"] == 1
    assert [r["id"] for r in res["rules"] if r["id"].startswith(("clipped", "fullScale"))] == ["clipped.5"]
    rep = natural.format_take(tmp_path / "clip.wav", tmp_path / "o")
    # The check said exactly what Format then does.
    assert not rep["acceptAllowed"]
    assert [f for f in rep["gates"]["failed"] if not f.startswith("preview")] == ["key-06.ogg:clip", "space-04.ogg:clip"]
    assert msg in rep["warnings"]


def test_noisy_take_warns_and_formats_an_empty_locked_set(tmp_path):
    make_take(tmp_path / "noisy.wav", noise_db=-40, droplets=False)
    res = natural.check_upload(tmp_path / "noisy.wav")
    assert res["ok"] and res["source"]["tapsUsable"] == 16
    fade, noise = res["warnings"]
    assert re.fullmatch(r"Background noise sits at -\d+(\.\d)? dBFS; aim for below -50 dBFS \(a dry, close take\)\.", noise)
    # 40 dB of decay never happens above a -40 dBFS floor: no tap counts for the recipe.
    assert fade == ("Only 0 taps fade out by 40 dB before the next one; Format needs at least 10 for a set "
                    "(record the taps further apart, or in a quieter room).")
    rep = natural.format_take(tmp_path / "noisy.wav", tmp_path / "o")
    assert rep["status"] == "formatted" and rep["counts"] == {"key": 0, "space": 0} and not rep["acceptAllowed"]
    assert "Only 0 keys; a set needs at least 10, so Accept stays locked." in rep["warnings"]


@pytest.mark.parametrize("subtype", ["PCM_16", "PCM_24", "FLOAT"])
def test_accepted_sample_formats(tmp_path, subtype):
    make_take(tmp_path / "t.wav", subtype=subtype)
    res = natural.check_upload(tmp_path / "t.wav")
    assert res["ok"], res["errors"]
    assert res["source"]["tapsUsable"] == 16 and res["source"]["tapsFound"] == 18


# ---------------------------------------------------------------- refusals (§3.8, one clear English line each)
def refused(path):
    res = natural.check_upload(path)
    assert not res["ok"]
    return res["errors"]


def test_refuses_a_file_that_is_not_wav(tmp_path):
    (tmp_path / "x.wav").write_bytes(b"this is not audio at all" * 40)
    assert refused(tmp_path / "x.wav") == [
        "This file is not a WAV file. Export the take as WAV (PCM 16-bit, 24-bit or 32-bit float)."]
    sf.write(str(tmp_path / "f.wav"), np.zeros((SR * 5, 2)), SR, format="FLAC")
    (msg,) = refused(tmp_path / "f.wav")
    assert msg.startswith("This file is not a WAV file (it is FLAC") and msg.endswith(
        "Export the take as WAV (PCM 16-bit, 24-bit or 32-bit float).")


def test_refuses_8_bit_and_64_bit_float(tmp_path):
    make_take(tmp_path / "u8.wav", subtype="PCM_U8", noise_db=-40)
    assert "The WAV holds 8-bit PCM samples; use PCM 16-bit, 24-bit or 32-bit float." in refused(tmp_path / "u8.wav")
    make_take(tmp_path / "f64.wav", subtype="DOUBLE")
    assert refused(tmp_path / "f64.wav") == ["The WAV holds 64-bit float samples; use PCM 16-bit, 24-bit or 32-bit float."]


def test_refuses_a_sample_rate_other_than_44k1_or_48k(tmp_path):
    make_take(tmp_path / "low.wav", sr=22050)
    assert "Sample rate 22.05 kHz; use 44.1 or 48 kHz." in refused(tmp_path / "low.wav")
    make_take(tmp_path / "hi.wav", sr=96000)
    assert refused(tmp_path / "hi.wav") == ["Sample rate 96 kHz; use 44.1 or 48 kHz."]


def test_refuses_more_than_two_channels(tmp_path):
    make_take(tmp_path / "three.wav", channels=3)
    assert refused(tmp_path / "three.wav") == ["The file has 3 channels; use mono or stereo."]


def test_refuses_takes_shorter_than_4_s_or_longer_than_30_s(tmp_path):
    make_take(tmp_path / "short.wav", taps=4, seconds=2.0, gaps_ms=(400,))
    errs = refused(tmp_path / "short.wav")
    assert errs[0] == "The take is 2 s long; it must be 4 to 30 s."
    make_take(tmp_path / "long.wav", seconds=31.0)
    assert refused(tmp_path / "long.wav") == ["The take is 31 s long; it must be 4 to 30 s."]
    # Just outside a limit, the number is rounded toward the side that breaks the rule: never "4 s" or "30 s".
    make_take(tmp_path / "under.wav", taps=12, seconds=3.96, gaps_ms=(300,))
    assert refused(tmp_path / "under.wav")[0] == "The take is 3.96 s long; it must be 4 to 30 s."
    make_take(tmp_path / "over.wav", seconds=30.04)
    assert refused(tmp_path / "over.wav") == ["The take is 30.04 s long; it must be 4 to 30 s."]
    make_take(tmp_path / "edge.wav", taps=12, seconds=4.0, gaps_ms=(300,))
    assert natural.check_upload(tmp_path / "edge.wav")["ok"]
    assert (natural.fmt_past(3.99998, up=False), natural.fmt_past(30.00002, up=True)) == ("3.99", "30.01")


def test_refuses_more_than_50_mb_without_reading_it(tmp_path):
    p = tmp_path / "big.wav"
    make_take(p, taps=2, seconds=1.0)
    with open(p, "r+b") as f:
        f.truncate(50 * 1024 * 1024 + 150 * 1024)          # sparse: no 50 MB written to disk
    res = natural.check_upload(p)
    assert res["errors"] == ["The file is 50.15 MB; the limit is 50 MB."]
    assert [r["id"] for r in res["rules"]] == ["size"]
    with open(p, "r+b") as f:
        f.truncate(50 * 1024 * 1024 + 1)
    assert natural.check_upload(p)["errors"] == ["The file is 50.01 MB; the limit is 50 MB."]


def test_refuses_too_few_usable_taps(tmp_path):
    make_take(tmp_path / "few.wav", taps=7, seconds=6.0)
    res = natural.check_upload(tmp_path / "few.wav")
    assert res["errors"] == ["Found 7 usable taps; need at least 12, each at least 150 ms before the next."]
    assert res["warnings"] == ["Only 7 taps fade out by 40 dB before the next one; Format needs at least 10 for a set "
                               "(record the taps further apart, or in a quieter room)."]


def test_refuses_taps_closer_than_150_ms(tmp_path):
    make_take(tmp_path / "fast.wav", taps=20, gaps_ms=(120,), tau=0.004, seconds=5.0)
    res = natural.check_upload(tmp_path / "fast.wav")
    assert res["source"]["tapsFound"] == 20
    assert res["errors"] == ["Found 1 usable tap; need at least 12, each at least 150 ms before the next."]


def test_refused_take_writes_only_the_report(tmp_path):
    make_take(tmp_path / "few.wav", taps=7, seconds=6.0)
    rep = natural.format_take(tmp_path / "few.wav", tmp_path / "o")
    assert rep["status"] == "refused" and rep["upload"]["errors"]
    assert sorted(p.name for p in (tmp_path / "o").iterdir()) == ["report.json"]
    assert json.loads((tmp_path / "o" / "report.json").read_text())["upload"]["errors"] == rep["upload"]["errors"]


# ---------------------------------------------------------------- CLI (`run.sh keys natural`)
def test_cli_check_json_and_exit_codes(take16, tmp_path, capsys):
    assert pipeline.main(["natural", str(take16[0]), "--check", "--json"]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["ok"] and out["source"]["tapsUsable"] == 16 and "analysis" not in out
    make_take(tmp_path / "few.wav", taps=7, seconds=6.0)
    assert pipeline.main(["natural", str(tmp_path / "few.wav"), "--check"]) == 1
    assert "refused: Found 7 usable taps" in capsys.readouterr().out
    assert pipeline.main(["natural", "--src", str(tmp_path / "few.wav"), "--out", str(tmp_path / "o")]) == 1
    assert pipeline.main(["natural", str(take16[0]), "--out", str(tmp_path / "o")]) == 2          # not empty
    assert "is not empty" in capsys.readouterr().err
    assert pipeline.main(["natural", str(take16[0]), "--out", str(tmp_path / "p"), "--id", "Bad Id"]) == 2
    assert pipeline.main(["natural", str(take16[0]), "--out", str(tmp_path / "q"), "--id", "off"]) == 2
    assert pipeline.main(["natural", str(take16[0])]) == 2                                          # no --out
    assert not (tmp_path / "p").exists() and not (tmp_path / "q").exists()


def test_cli_through_run_sh(take16, tmp_path):
    """What the Admin job runs: bash tools/audio-lab/run.sh keys natural --src … --out … (array args, no shell)."""
    run = env.LAB / "run.sh"
    p = subprocess.run(["bash", str(run), "keys", "natural", "--src", str(take16[0]), "--out", str(tmp_path / "o"),
                        "--id", "cli-set", "--name", "CLI Set", "--family", "Test"],
                       capture_output=True, text=True, timeout=180, env=os.environ.copy())
    assert p.returncode == 0, p.stderr
    assert p.stdout.startswith("cli-set: 16 keys, 8 spaces, 0 lead-ins, gates pass, accept allowed")
    assert json.loads((tmp_path / "o" / "keys-manifest.json").read_text())["name"] == "CLI Set"


# ---------------------------------------------------------------- the owner's real takes (when on this machine)
REAL = [  # source, analyse.py output of 30/10, published set, §3.8 table (found, usable, peak dBFS, floor dB)
    ("raindrop/src/raindrop.wav", "raindrop/hits.json", "raindrop-tile", (22, 17, -1.76, -90.3)),
    ("hail/src/hail-v1.wav", "hail/hits-v1.json", None, (52, 22, -0.03, -66.2)),
    ("hail/src/hail-v4.wav", "hail/hits-v4.json", "hail-stone", (37, 17, -0.07, -73.1)),
]


def need(path):
    if not path.is_file():
        pytest.skip(f"{path} is not on this machine")
    return path


@pytest.mark.parametrize("src,hits,_set,_table", REAL, ids=["raindrop", "hail-v1", "hail-v4"])
def test_onsets_module_matches_analyse_py(src, hits, _set, _table):
    assert onsets.analyse(need(TAKES / src)) == json.loads(need(TAKES / hits).read_text())


@pytest.mark.parametrize("src,_hits,_set,table", REAL, ids=["raindrop", "hail-v1", "hail-v4"])
def test_real_takes_pass_the_fast_check(src, _hits, _set, table):
    res = natural.check_upload(need(TAKES / src))
    found, usable, peak, floor = table
    s = res["source"]
    assert res["ok"] and res["errors"] == []
    assert (s["tapsFound"], s["tapsUsable"], s["peakDbfs"], s["noiseFloorDbfs"]) == (found, usable, peak, floor)
    hot = [w for w in res["warnings"] if "reaches full scale" in w]
    assert len(hot) == (0 if src.startswith("raindrop") else 1)       # one tap above 0.99 in each hail take
    assert res["warnings"] == hot


def published_copy(set_id, dest):
    """Copy one published set out of typing-feel/public (read-only there) and return the copy."""
    catalogue = json.loads(need(PUBLIC_KEYS / "keys-manifest.json").read_text())
    row = next((p for p in catalogue["profiles"] if p["id"] == set_id), None)
    if row is None:
        pytest.skip(f"{set_id} is not in the published catalogue")
    folder = (PUBLIC_KEYS / row["manifest"]).parent
    shutil.copytree(folder, dest)
    return dest


@pytest.mark.parametrize("src,_hits,set_id,_table", [r for r in REAL if r[2]], ids=["raindrop-tile", "hail-stone"])
def test_real_take_reproduces_the_published_set(src, _hits, set_id, _table, tmp_path):
    take = need(TAKES / src)
    ref = published_copy(set_id, tmp_path / "published")
    ref_man = json.loads((ref / "keys-manifest.json").read_text())
    rep = natural.format_take(take, tmp_path / "out", set_id, ref_man["name"])
    out = tmp_path / "out"
    assert rep["status"] == "formatted" and rep["gates"]["pass"] and rep["acceptAllowed"]
    # The set-1 text is the import-staging layout, byte for byte.
    assert (out / "keys-manifest.json").read_text() == (ref / "keys-manifest.json").read_text()
    for f in ref_man["files"]:
        a, b = decoded(ref / f["file"]), decoded(out / f["file"])
        assert a.shape == b.shape, f["file"]
        assert np.abs(a - b).max() <= PCM_TOL, f["file"]
    # preview.ogg: the same typing up to the owner's 31/10 fade (and the Vorbis blocks around it), then faded.
    a, b = decoded(ref / "preview.ogg"), decoded(out / "preview.ogg")
    assert a.shape == b.shape == (SR, 2)
    keep = SR - 4096
    assert np.abs(a[:keep] - b[:keep]).max() <= PCM_TOL
    assert np.sqrt(np.mean(b[-48:] ** 2)) < np.sqrt(np.mean(a[-48:] ** 2))
    if set_id == "hail-stone":     # the owner kept these on 31/10: keys 04 06 12 16 20 23 25 and 4 spaces, 35-205 ms
        lead = [li["file"] for li in rep["leadIns"]]
        assert lead == [f"key-{n:02d}.ogg" for n in (4, 6, 12, 16, 20, 23, 25)] + \
            [f"space-{n:02d}.ogg" for n in (3, 5, 6, 7)]
        assert 35 <= min(li["mainStrikeMs"] for li in rep["leadIns"]) and max(li["mainStrikeMs"] for li in rep["leadIns"]) <= 210
    else:
        assert rep["leadIns"] == []
    assert_ab_takes_are_what_the_owner_heard(src, out)


# The A/B takes the owner listened to on 30/10 (tmp/keys-firefly/*/out): natural (build2 version A, hail.py) and the
# raw cut (build.py, raindrop only). The Listen step compares a new set against these two recipes.
OWNER_AB = {
    "raindrop/src/raindrop.wav": ("raindrop/out/raindrop-70wpm-v2-A-natural.mp3", "raindrop/out/raindrop-70wpm-raw-cut.mp3"),
    "hail/src/hail-v1.wav": ("hail/out/hail-70wpm-v1.mp3", None),
    "hail/src/hail-v4.wav": ("hail/out/hail-70wpm-v4.mp3", None),
}


def decode_mp3(path):
    raw = subprocess.run([onsets.ffmpeg(), "-v", "error", "-nostdin", "-i", str(path), "-f", "f64le", "-ac", "2", "-ar",
                          str(SR), "pipe:1"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype="<f8").reshape(-1, 2)


def assert_ab_takes_are_what_the_owner_heard(src, out):
    checked = 0
    for ours, ref in zip(("natural.mp3", "raw-cut.mp3"), OWNER_AB[src]):
        if ref is None or not (TAKES / ref).is_file():
            continue
        a, b = decode_mp3(out / "ab" / ours), decode_mp3(TAKES / ref)
        assert a.shape == b.shape, ours
        assert np.abs(a - b).max() <= PCM_TOL, ours
        checked += 1
    return checked


def test_hail_v1_ab_take_is_what_the_owner_heard(tmp_path):
    take = need(TAKES / "hail/src/hail-v1.wav")
    need(TAKES / OWNER_AB["hail/src/hail-v1.wav"][0])
    rep = natural.format_take(take, tmp_path / "out", "hail-v1", "Hail V1")
    assert rep["status"] == "formatted"
    assert assert_ab_takes_are_what_the_owner_heard("hail/src/hail-v1.wav", tmp_path / "out") == 1
