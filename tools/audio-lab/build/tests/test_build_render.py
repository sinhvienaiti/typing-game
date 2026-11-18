import json

import numpy as np
import soundfile as sf

from build import ledger, render
from build.tests.helpers import make_library, recipe


def _render(tmp_path, name, **kw):
    libs = tmp_path / "libs"
    if not (libs / "SOURCES.jsonl").exists():
        make_library(libs)
    return render.render(recipe(**kw.pop("rkw", {})), out=tmp_path / name, run=name, libraries=libs,
                         date="2026-10-23", **kw)


def _hashes(res):
    out = {}
    for p in sorted(res.out.rglob("*")):
        if p.suffix in (".wav", ".ogg"):
            out[p.relative_to(res.out).as_posix()] = ledger.sha256_file(p)
    return out


def test_render_is_deterministic_for_a_seed(tmp_path):
    a = _render(tmp_path, "a")
    b = _render(tmp_path, "b")
    ha, hb = _hashes(a), _hashes(b)
    assert len(ha) == 8 and ha == hb               # 4 masters + 4 OGG, byte-identical
    ra, rb = ledger.records(a.sources), ledger.records(b.sources)
    assert {k: v["sha256"] for k, v in ra.items()} == {k: v["sha256"] for k, v in rb.items()}
    assert [v["plan"] for v in a.report["variants"]] == [v["plan"] for v in b.report["variants"]]
    c = _render(tmp_path, "c", seed=812)
    assert _hashes(c) != ha                          # another seed, other variants


def test_variants_differ_and_respect_group_limits(tmp_path):
    res = _render(tmp_path, "v", rkw={"count": 6})
    plans = [v["plan"] for v in res.report["variants"]]
    assert plans[0]["base"] and plans[0]["pitchCents"] == 0 and plans[0]["layers"]["attack"]["swap"] == 0
    assert len({ledger.sha256_file(res.out / v["master"]) for v in res.report["variants"]}) == 6
    for p in plans:                                  # hit-heavy: ±80 cents, ±1 dB (§5.3)
        assert abs(p["pitchCents"]) <= 80 and abs(p["gainDb"]) <= 1
        assert abs(p["layers"]["attack"]["pitchCents"]) <= 50
    assert {p["layers"]["attack"]["swap"] for p in plans[1:]} - {0, 1, 2} == set()


def test_outputs_are_48k_and_logged(tmp_path):
    res = _render(tmp_path, "o")
    for v in res.report["variants"]:
        for rel in (v["master"], "runtime/" + v["runtime"]):
            info = sf.info(str(res.out / rel))
            assert info.samplerate == 48000 and info.channels == 1
        assert v["final"]["truePeakDbtp"] <= -1.0 and v["final"]["headMs"] <= 2.0
    assert sf.info(str(res.out / res.report["variants"][0]["master"])).subtype == "PCM_24"
    assert sf.info(str(res.out / "runtime" / res.report["variants"][0]["runtime"])).subtype == "VORBIS"
    # SOURCES.json and licence rows validate against their schemas.
    assert ledger.schema_errors("sources", ledger.read_sources(res.out / "SOURCES.json")) == []
    rows = ledger.read_rows(res.out / "licences.rows.jsonl")
    assert {r["kind"] for r in rows} == {"source", "library"}
    assert all(ledger.schema_errors("licences", r) == [] for r in rows)
    rec = next(iter(ledger.records(res.sources).values()))
    kinds = {layer["kind"] for layer in rec["layers"]}
    assert kinds == {"library", "synth"} and rec["aiInputAllowed"] is True
    frag = json.loads((res.out / "manifest.fragment.json").read_text())
    assert frag["version"] == 2 and frag["sounds"]["hit.test"]["files"][0] == "sfx/hits/hit-test-1.ogg"


def test_ogg_serial_fix_keeps_a_valid_stream(tmp_path):
    x = np.sin(2 * np.pi * 440 * np.arange(24000) / 48000) * 0.5
    render.write_ogg(tmp_path / "a.ogg", x)
    render.write_ogg(tmp_path / "b.ogg", x)
    assert (tmp_path / "a.ogg").read_bytes() == (tmp_path / "b.ogg").read_bytes()
    y, sr = sf.read(str(tmp_path / "a.ogg"))      # libogg rejects pages with a bad CRC
    assert sr == 48000 and len(y) == len(x)


def test_stereo_loop_with_file_and_gen_layers(tmp_path):
    """Loop path (LUFS-I, crossfade), stereo, own-file layer with a ledger row and a model-output layer."""
    rng = np.random.default_rng(3)
    t = np.arange(3 * 48000) / 48000
    bed = np.stack([0.2 * np.sin(2 * np.pi * 110 * t), 0.2 * np.sin(2 * np.pi * 112 * t)], 1)
    sf.write(str(tmp_path / "bed.wav"), bed, 48000, subtype="FLOAT")
    sf.write(str(tmp_path / "gen.wav"), 0.1 * rng.standard_normal((44100 * 3, 2)), 44100, subtype="PCM_16")
    row = {"licence": "LicenseRef-owner-recording", "licenceUrl": "licences/owner-recordings.txt",
           "licenceCopy": "licences/owner-recordings.txt", "date": "2026-10-23", "origin": "owner-recording",
           "commercial_ok": True, "attribution_required": False, "ai_input_allowed": True,
           "raw_redistribution_allowed": False}
    r = {"schema": "audiolab.recipe/1", "game": "typing-defense", "id": "amb.test", "group": "none",
         "channels": 2, "loop": True,
         "layers": [
             {"id": "bed", "source": {"file": str(tmp_path / "bed.wav"), "ledger": row}},
             {"id": "air", "source": {"gen": {"tool": "ace-step", "model": "ACE-Step/Ace-Step1.5@abc",
                                              "licence": "MIT", "file": str(tmp_path / "gen.wav"),
                                              "prompt": "dusk air", "seed": 4, "window": [0.5, 2.5]}},
              "gainDb": -12, "pitchSemitones": -2, "pitchMode": "preserve"}],
         "chain": {"loopCrossfadeMs": 100}, "variants": {"count": 2, "seed": 5},
         "export": {"path": "music/amb-test"}}
    res = render.render(r, out=tmp_path / "run", run="run", libraries=tmp_path, date="2026-10-23")
    for v in res.report["variants"]:
        assert v["final"]["channels"] == 2 and v["final"]["truePeakDbtp"] <= -1.0
        assert abs(v["final"]["lufsI"] + 26.0) <= 0.5               # loops default to LUFS-I -26
        assert abs(v["final"]["durationMs"] - 2900) < 5                # 3 s bed minus the 100 ms crossfade
    rec = ledger.records(res.sources)["music/amb-test-1.ogg"]
    gen = next(layer for layer in rec["layers"] if layer["id"] == "air")
    assert gen["kind"] == "gen" and gen["aiSteps"] == ["generate"] and rec["models"] == ["ACE-Step/Ace-Step1.5@abc"]
    assert {row["kind"] for row in res.rows} == {"source"}
    assert res.report["limits"] == "group:none"
    assert [w for w in res.report["warnings"] if "không đổi ngẫu nhiên" not in w] == []


def test_ogg_never_overshoots_the_ceiling():
    rng = np.random.default_rng(9)
    x = np.clip(rng.standard_normal(24000) * 0.6, -1, 1) * 10 ** (-1.0 / 20)     # dense, peak right at -1 dBFS
    y, data, gain, tp = render.ogg_safe(x, -1.0)
    assert tp <= -1.0 and gain <= 0
    import io
    decoded, _ = sf.read(io.BytesIO(data), always_2d=True)
    from build import measure
    assert measure.true_peak_db(decoded) <= -1.0
