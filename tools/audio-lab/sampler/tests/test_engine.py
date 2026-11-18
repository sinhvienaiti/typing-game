"""Sample player on synthetic sample folders (no library, no network)."""
import json

import numpy as np
import pytest
import soundfile as sf

from sampler import __main__ as cli
from sampler.engine import MAX_SHIFT_CAP, Note, OutOfRange, Sampler, parse_note_spec
from sampler.instrument import from_folder
from sampler.midi import read_midi, write_midi
from sampler.naming import note_to_midi
from sampler.phrases import test_phrase as make_phrase

SR_IN = 44100


def tone(midi, amp=0.5, dur=1.0, sr=SR_IN, pre=0.02, decay=3.0, rr_marker=0.0):
    t = np.arange(int(dur * sr)) / sr
    f = 440.0 * 2 ** ((midi - 69) / 12)
    y = amp * np.sin(2 * np.pi * f * t + rr_marker) * np.exp(-decay * t)
    return np.concatenate([np.zeros(int(pre * sr)), y]).astype(np.float32)


def make_pitched(folder, roots=("C4", "E4", "G#4"), layers=(("v1", 0.15), ("v2", 0.6)), rrs=2):
    folder.mkdir(parents=True, exist_ok=True)
    for name in roots:
        m = note_to_midi(name)
        for lay, amp in layers:
            for rr in range(1, rrs + 1):
                sf.write(folder / f"Test_sus_{name}_{lay}_rr{rr}.wav", tone(m, amp, rr_marker=0.3 * rr), SR_IN)
    return folder


def f0_of(y, sr=48000, lo=0.05, hi=0.45):
    seg = y[int(lo * sr):int(hi * sr)]
    spec = np.abs(np.fft.rfft(seg * np.hanning(len(seg)), n=1 << 20))
    k = int(np.argmax(spec))
    a, b, c = spec[k - 1], spec[k], spec[k + 1]
    k = k + 0.5 * (a - c) / (a - 2 * b + c)                 # parabolic peak
    return k * sr / (1 << 20)


def cents(hz, midi):
    return 1200 * np.log2(hz / (440.0 * 2 ** ((midi - 69) / 12)))


@pytest.fixture()
def pitched(tmp_path):
    return from_folder(make_pitched(tmp_path / "test-sus"), inst_id="test/sus")


def test_folder_instrument_layout(pitched):
    assert pitched.pitched and pitched.roots() == [60, 64, 68]
    assert pitched.mode == "sustain"                         # 'sus' in the folder name
    play = pitched.playable(3.0)
    assert play[0] == 57 and play[-1] == 71 and all(m in play for m in range(57, 72))
    lay = sorted({(z.lovel, z.hivel) for z in pitched.zones if z.root == 60})
    assert lay == [(1, 64), (65, 127)]


def test_pitch_shift_lands_on_the_note(pitched):
    s = Sampler()
    s.add(pitched)
    for name in ("C4", "D4", "D#4", "F4", "A4", "A3"):
        m = note_to_midi(name)
        r = s.render([Note(0.0, m, 100, 0.8)])
        assert r.sr == 48000
        assert abs(cents(f0_of(r.audio[:, 0]), m)) < 5, name
        row = r.report["notes"][0]
        assert abs(row["shift_st"]) <= 3.0 + 1e-9


def test_shift_cap_is_enforced(pitched):
    s = Sampler()
    s.add(pitched)
    with pytest.raises(OutOfRange):
        s.render([Note(0.0, note_to_midi("C3"), 100, 0.5)])   # 9 semitones below C4
    r = s.render([Note(0.0, note_to_midi("C3"), 100, 0.5), Note(0.1, 60, 100, 0.5)], on_out_of_range="skip")
    assert len(r.report["skipped"]) == 1 and len(r.report["notes"]) == 1
    with pytest.raises(ValueError):
        Sampler(max_shift=MAX_SHIFT_CAP + 0.5)
    s.render([Note(0.0, 57, 100, 0.5)])                       # A3 = C4 - 3 st: exactly at the cap
    with pytest.raises(OutOfRange):                           # detune counts against the cap
        s.render([Note(0.0, 57, 100, 0.5, cents=-50)])


def test_velocity_layers_and_round_robin(pitched):
    s = Sampler(veltrack=0.0)
    s.add(pitched)
    r = s.render([Note(0.0, 60, 30, 0.2), Note(0.5, 60, 120, 0.2)])
    soft, loud = r.report["notes"]
    assert "_v1_" in soft["sample"] and "_v2_" in loud["sample"]
    r = s.render([Note(i * 0.3, 60, 100, 0.2) for i in range(4)])
    assert [n["rr"] for n in r.report["notes"]] == [1, 2, 1, 2]
    s = Sampler(rr_mode="random", seed=3)
    s.add(pitched)
    rrs = [n["rr"] for n in s.render([Note(i * 0.3, 60, 100, 0.2) for i in range(6)]).report["notes"]]
    assert all(a != b for a, b in zip(rrs, rrs[1:]))          # never the same sample twice in a row


def test_release_tail_and_oneshot(tmp_path):
    folder = make_pitched(tmp_path / "plain", roots=("C4",), layers=(("v1", 0.5),), rrs=1)
    sus = from_folder(folder, mode="sustain", release=0.1)
    one = from_folder(folder, mode="oneshot")
    for inst, ringing in ((sus, False), (one, True)):
        s = Sampler()
        s.add(inst)
        y = s.render([Note(0.0, 60, 127, 0.2)]).audio[:, 0]
        after = np.abs(y[int(0.32 * 48000):int(0.6 * 48000)]).max() if len(y) > int(0.6 * 48000) else 0.0
        assert (after > 0.05) == ringing
    s = Sampler()
    s.add(sus)
    y = s.render([Note(0.0, 60, 127, 0.2)]).audio[:, 0]
    assert len(y) <= int(0.31 * 48000)                        # voice ends at note-off + release


def test_loop_wrap_and_cut(pitched):
    s = Sampler()
    s.add(pitched)
    notes = [Note(0.9, 60, 120, 0.05)]
    wrap = s.render(notes, length=1.0, tail="wrap").audio
    cut = s.render(notes, length=1.0, tail="cut").audio
    keep = s.render(notes).audio
    assert len(wrap) == len(cut) == 48000 and len(keep) > 48000
    assert np.abs(wrap[:2400]).max() > 0.01                  # tail folded back to the start
    assert np.abs(cut[:2400]).max() == 0.0


def test_unpitched_key_map(tmp_path):
    d = tmp_path / "drum"
    d.mkdir()
    for art in ("Hit", "Hand"):
        for v in (1, 2):
            for rr in (1, 2):
                sf.write(d / f"Drum_{art}_v{v}_rr{rr}_Sum.wav", tone(45, 0.2 * v, dur=0.3), SR_IN)
    inst = from_folder(d)
    assert not inst.pitched
    assert inst.keymap == {"drum-hand": 36, "drum-hit": 37}
    s = Sampler()
    s.add(inst)
    r = s.render([Note(0.0, None, 100, 0.2, key="drum-hit"), Note(0.3, 36, 20, 0.2)])
    a, b = r.report["notes"]
    assert a["key"] == "drum-hit" and "_v2_" in a["sample"]
    assert b["key"] == "drum-hand" and "_v1_" in b["sample"]
    with pytest.raises(OutOfRange):
        s.render([Note(0.0, None, 100, 0.2, key="nope")])


def test_wav_output_and_report(pitched, tmp_path):
    s = Sampler()
    s.add(pitched)
    r = s.render(parse_note_spec("0:C4:0.5:100 0.5:E4:0.5:80"))
    out = r.write(tmp_path / "x.wav")
    info = sf.info(str(out))
    assert (info.samplerate, info.channels, info.subtype) == (48000, 2, "PCM_24")
    assert len(r.report["sources"]) == 2 and r.report["peak_dbfs"] <= -1.0 + 1e-6


def test_parse_note_spec_beats_and_keys():
    a, b = parse_note_spec("0:C5:1:90 2:hdrum-hit:0.5", bpm=120)
    assert (a.start, a.midi, a.duration, a.velocity) == (0.0, 72, 0.5, 90)
    assert (b.start, b.midi, b.key) == (1.0, None, "hdrum-hit")


def test_midi_roundtrip_and_sustain_pedal(tmp_path, pitched):
    import mido
    path = write_midi(tmp_path / "t.mid", [(0, 60, 1, 100), (1, 64, 0.5, 80), (2, 67, 1, 90)], bpm=120)
    notes, meta = read_midi(path)
    assert meta["bpm"] == 120 and len(notes) == 3
    assert [(round(n.start, 3), n.midi, round(n.duration, 3)) for n in notes] == \
        [(0.0, 60, 0.5), (0.5, 64, 0.25), (1.0, 67, 0.5)]
    mid = mido.MidiFile(str(path))                          # pedal held over the first note
    tr = mid.tracks[0]
    tr.insert(2, mido.Message("control_change", control=64, value=127, time=0))
    tr.insert(len(tr) - 1, mido.Message("control_change", control=64, value=0, time=0))
    mid.save(str(tmp_path / "ped.mid"))
    notes, _ = read_midi(tmp_path / "ped.mid")
    assert round(notes[0].duration, 3) == 1.5                # released with the pedal, at the end


def test_cli_render_midi_and_phrase(tmp_path, pitched):
    folder = make_pitched(tmp_path / "cli-sus")
    mid = write_midi(tmp_path / "m.mid", [(0, 60, 1, 100), (1, 62, 1, 100), (2, 64, 2, 100)], bpm=96)
    out = tmp_path / "out" / "m.wav"
    assert cli.main(["render", "--instrument-dir", str(folder), "--midi", str(mid), "--bars", "1",
                     "--tail", "wrap", "-o", str(out)]) == 0
    rep = json.loads(out.with_suffix(".json").read_text())
    assert rep["duration"] == pytest.approx(4 * 60 / 96, abs=1e-3) and len(rep["notes"]) == 3
    assert cli.main(["phrase", "--instrument-dir", str(folder), "--out-dir", str(tmp_path / "ph")]) == 0
    assert any((tmp_path / "ph").glob("*.wav"))
    with pytest.raises(SystemExit):
        cli.main(["--max-shift", "4", "list"])


def test_phrase_covers_layers_rr_and_stays_in_range(pitched):
    notes, length = make_phrase(pitched, 3.0)
    play = set(pitched.playable(3.0))
    assert all(n.midi in play for n in notes) and length > 2
    s = Sampler()
    s.add(pitched)
    rows = s.render(notes).report["notes"]
    assert {tuple(r["layer"]) for r in rows} == {(1, 64), (65, 127)}
    assert {r["rr"] for r in rows} == {1, 2}
