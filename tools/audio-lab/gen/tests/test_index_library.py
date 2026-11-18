"""index.json on a synthetic libraries folder (Kenney-like, VCSL-like with an SFZ map)."""
import json
from pathlib import Path

import numpy as np
import pytest
import soundfile as sf

from gen import index_library as I
from gen import libraries as L
from sampler.instrument import from_index

SR = 48000


def sine(midi, dur=1.0, sr=SR, cents=0.0):
    t = np.arange(int(dur * sr)) / sr
    f = 440.0 * 2 ** ((midi - 69 + cents / 100) / 12)
    return (0.4 * np.sin(2 * np.pi * f * t) * np.exp(-1.5 * t)).astype(np.float32)


@pytest.fixture()
def libroot(tmp_path):
    root = tmp_path / "libraries"
    k = root / "kenney/impact-sounds/Audio"
    k.mkdir(parents=True)
    sf.write(k / "impactMetal_heavy_000.ogg", sine(70, 0.3), SR, format="OGG", subtype="VORBIS")
    sf.write(k / "footstep_grass_003.ogg", sine(50, 0.2), SR, format="OGG", subtype="VORBIS")
    dt = root / "vcsl/Chordophones/Zithers/Dan Tranh"
    (dt / "Normal").mkdir(parents=True)
    (dt / "FX").mkdir(parents=True)
    # VCSL names are an octave low: "B1" sounds B2 (MIDI 47); C#2 sounds C#3 (49), 30 cents sharp
    sf.write(dt / "Normal/B1_f_1.wav", sine(47), SR, subtype="PCM_24")
    sf.write(dt / "Normal/B1_mf_1.wav", sine(47), SR, subtype="PCM_24")
    sf.write(dt / "Normal/C#2_f_1.wav", sine(49, cents=30), SR, subtype="PCM_24")
    sf.write(dt / "FX/FX_01.wav", sine(60, 0.4), SR)
    sfz = root / "vcsl-sfz/Chordophones/Zithers/Dan Tranh - Normal.sfz"
    sfz.parent.mkdir(parents=True)
    sfz.write_text("<group>\nampeg_release=0.3\n<region>\nlovel=0\nhivel=80\nsample=Dan Tranh/Normal/B1_mf_1.wav\n"
                   "pitch_keycenter=47\n<region>\nlovel=81\nhivel=127\nsample=Dan Tranh/Normal/B1_f_1.wav\n"
                   "pitch_keycenter=47\n")
    base = {**L.CC0_FLAGS, "downloaded": "2026-10-23", "licence_copy": "x/LICENSE-2026-10-23.txt"}
    L.upsert_ledger([
        {**base, "library": "kenney", "pack": "Impact Sounds", "path": "kenney/impact-sounds", "url": "u", "sha256": "z"},
        {**base, "library": "vcsl", "pack": "Dan Tranh", "path": "vcsl/Chordophones/Zithers/Dan Tranh",
         "commit": "c0ffee", "web": "https://example.invalid/vcsl", "sha256": "d"},
        {**base, "library": "vcsl", "pack": "SFZ mappings (text)", "path": "vcsl-sfz", "sha256": "s"},
    ], root)
    return root


def by_file(index):
    return {Path(e["file"]).name: e for e in index["files"]}


def test_index_fields(libroot):
    ix = I.build_index(libroot, verify_pitch=True, log=lambda *_: None)
    f = by_file(ix)
    assert set(f) == {"impactMetal_heavy_000.ogg", "footstep_grass_003.ogg", "B1_f_1.wav", "B1_mf_1.wav",
                      "C#2_f_1.wav", "FX_01.wav"}
    k = f["impactMetal_heavy_000.ogg"]
    assert (k["family"], k["weight"], k["variant"], k["rr"], k["kind"]) == ("impact/metal", "heavy", 0, 1, "sfx")
    assert k["sample_rate"] == SR and k["channels"] == 1 and k["licence"] == "CC0-1.0"
    assert abs(k["duration"] - 0.3) < 0.01 and len(k["sha256"]) == 64
    assert f["footstep_grass_003.ogg"]["family"] == "footstep/grass"
    b = f["B1_f_1.wav"]
    assert (b["instrument_id"], b["kind"], b["midi"], b["midi_source"], b["note_spn"]) == \
        ("vcsl/dan-tranh.normal", "pitched", 47, "sfz", "B2")
    assert (b["dyn"], b["rr"], b["sfz"]["lovel"], b["sfz"]["hivel"]) == ("f", 1, 81, 127)
    c = f["C#2_f_1.wav"]                       # not in the SFZ: octave offset learned from the folder
    assert (c["midi"], c["midi_source"]) == (49, "name+folder-sfz-offset")
    assert abs(c["f0"]["cents"] - 30) < 1 and c["f0"]["octave_off"] == 0 and c["f0"]["stable"]
    assert abs(b["f0"]["cents"]) < 1 and b["f0"]["method"] == I.F0_METHOD
    fx = f["FX_01.wav"]
    assert (fx["instrument_id"], fx["kind"], fx["midi"]) == ("vcsl/dan-tranh.fx", "unpitched", None)
    inst = ix["instruments"]["vcsl/dan-tranh.normal"]
    assert inst["range"] == ["B2", "C#3"] and inst["playable"] == ["G#2", "E3"] and inst["mode"] == "oneshot"


def test_index_incremental_reuses_f0_and_feeds_the_sampler(libroot, tmp_path):
    ix = I.build_index(libroot, verify_pitch=True, log=lambda *_: None)
    out = libroot / "index.json"
    I.write_index(ix, out)
    again = I.build_index(libroot, verify_pitch=False, previous=json.loads(out.read_text()), log=lambda *_: None)
    assert by_file(again)["C#2_f_1.wav"]["f0"] == by_file(ix)["C#2_f_1.wav"]["f0"]
    inst = from_index("dan-tranh.normal", again)
    z = {Path(z.path).name: z for z in inst.zones}
    assert abs(z["C#2_f_1.wav"].tune_cents + 30) < 3           # auto tuning pulls it back to pitch
    assert (z["B1_mf_1.wav"].lovel, z["B1_mf_1.wav"].hivel) == (0, 80)
    assert any("tuned 1" in n for n in inst.notes)
    b1 = by_file(again)["B1_f_1.wav"]
    b1["sfz"]["tune"] = -11                                    # library map detunes an in-tune sample
    z2 = {Path(z.path).name: z for z in from_index("dan-tranh.normal", again).zones}
    assert z2["B1_f_1.wav"].tune_cents == 0.0
    assert {Path(z.path).name: z.tune_cents for z in from_index("dan-tranh.normal", again, tuning="sfz").zones}[
        "B1_f_1.wav"] == -11.0
    c2 = by_file(again)["C#2_f_1.wav"]
    c2["f0"]["drift_cents"] = 45.0                              # a pluck that glides too much
    glide = from_index("dan-tranh.normal", again)
    assert all(z.tune_cents == 0 for z in glide.zones) and any("gliding" in n for n in glide.notes)
    c2["f0"]["drift_cents"] = None                              # no clear spectral peak
    assert all(z.tune_cents == 0 for z in from_index("dan-tranh.normal", again).zones)


def test_main_writes_index_and_summary(libroot, capsys):
    assert I.main(["--root", str(libroot)]) == 0
    assert (libroot / "index.json").exists()
    assert "vcsl/dan-tranh.normal" in capsys.readouterr().out
    assert I.main(["--root", str(libroot), "--summary"]) == 0


@pytest.mark.skipif(not (L.ROOT / L.INDEX_NAME).exists(), reason="real library index not built")
def test_real_library_word_hit_range():
    """Plan §8.2: word-hit C5–C6 on VCSL Dan Tranh stays within the 3-semitone cap."""
    from sampler.engine import Note, Sampler
    from sampler.instrument import load_index
    s = Sampler()
    s.add(from_index("dan-tranh.normal", load_index()))
    notes = [Note(i * 0.2, m, 100, 0.4) for i, m in enumerate((72, 74, 77, 79, 81, 84))]
    rows = s.render(notes).report["notes"]
    assert len(rows) == 6 and max(abs(r["shift_st"]) for r in rows) <= 1.5


def test_f0_fft_peak_on_bars_and_glides(tmp_path):
    """Inharmonic bar (partials 1, 2.76, 5.4): the fundamental is read to ~1 cent.
    A pitch glide is flagged unstable, so the sampler leaves it alone."""
    t = np.arange(int(1.2 * SR)) / SR
    f = 440.0 * 2 ** (24 / 1200)                                   # A4 + 24 cents
    bar = sum(a * np.sin(2 * np.pi * f * k * t) for k, a in ((1, 0.4), (2.76, 0.3), (5.4, 0.2)))
    sf.write(tmp_path / "bar.wav", (bar * np.exp(-2 * t)).astype(np.float32), SR)
    r = I.estimate_f0(tmp_path / "bar.wav", 69)
    assert abs(r["cents"] - 24) < 1 and r["stable"]
    glide = 440.0 * 2 ** (np.linspace(40, -20, len(t)) / 1200)        # falls 60 cents over 1.2 s
    y = 0.4 * np.sin(2 * np.pi * np.cumsum(glide) / SR) * np.exp(-1.0 * t)
    sf.write(tmp_path / "glide.wav", y.astype(np.float32), SR)
    g = I.estimate_f0(tmp_path / "glide.wav", 69)
    assert g["octave_off"] == 0 and not g["stable"] and g["drift_cents"] > 10


@pytest.mark.skipif(not (L.ROOT / L.INDEX_NAME).exists(), reason="real library index not built")
def test_real_library_rewards_are_in_tune():
    """Plan §3.2: pitched rewards within 10 cents. Dan Tranh and Folk Harp, C5–C6, every layer."""
    from sampler.engine import Note, Sampler
    from sampler.instrument import load_index
    ix = load_index()
    for name in ("dan-tranh.normal", "folk-harp"):
        inst = from_index(name, ix)
        for vel in (40, 90, 120):
            s = Sampler()
            s.add(inst)
            for m in range(72, 85):
                y = s.render([Note(0.0, m, vel, 1.0)]).audio.mean(axis=1)
                ref = 440.0 * 2 ** ((m - 69) / 12)
                hz = I.spectral_peak(y[int(0.06 * 48000):int(0.66 * 48000)], 48000, ref, 2 ** (1.5 / 12))
                assert hz and abs(1200 * np.log2(hz / ref)) < 10, (name, m, vel)
