"""Cross-module wiring: sampler phrases as recipe layers, critic ai_steps into the ledger, swapMode."""
import json

import numpy as np
import pytest
import soundfile as sf

from build import critic_link, ledger, licence_check, recipe as rcp, release, render
from build.tests.helpers import SR, make_library, recipe


def _pitched_pack(libs, licence="CC0-1.0", **flags):
    """A tiny pitched sample folder (Tone_<note>_v1_rr1.wav) inside a library pack."""
    make_library(libs, licence=licence, files=1, **flags)
    folder = libs / "testlib" / "pack1" / "Tones"
    folder.mkdir(parents=True, exist_ok=True)
    t = np.arange(int(SR * 0.6)) / SR
    for name, hz in (("C4", 261.63), ("E4", 329.63), ("G4", 392.0)):
        x = 0.5 * np.sin(2 * np.pi * hz * t) * np.exp(-t / 0.2)
        sf.write(str(folder / f"Tone_{name}_v1_rr1.wav"), x, SR, subtype="PCM_24")
    return libs


def _sampler_recipe(**src):
    data = recipe(count=2, library=False)
    data["id"] = "tone.test"
    data["layers"] = [{"id": "pluck", "role": "body", "fadeOutMs": 50,
                       "source": {"sampler": {"instrumentDir": "testlib/pack1/Tones", "pitched": True,
                                              "notes": "0:D4:0.3:100", **src}},
                       "vary": {"swapMode": "cycle", "swap": [{"sampler": {
                           "instrumentDir": "testlib/pack1/Tones", "pitched": True, "notes": "0:A4:0.3:100"}}]}}]
    data["chain"] = {"maxLengthMs": 500}
    return data


def test_sampler_layer_records_every_sample(tmp_path):
    libs = _pitched_pack(tmp_path / "libs")
    res = render.render(_sampler_recipe(), out=tmp_path / "run", run="run", libraries=libs, date="2026-10-23")
    recs = ledger.records(ledger.read_sources(tmp_path / "run" / "SOURCES.json"))
    layers = [r["layers"][0] for r in sorted(recs.values(), key=lambda r: r["variant"])]
    assert [layer["kind"] for layer in layers] == ["sampler", "sampler"]
    # D4 comes from C4 or E4, A4 from G4: each variant names the sample it used (cycle = deliberate combo).
    assert layers[0]["sources"][0]["source"].endswith(("Tone_C4_v1_rr1.wav", "Tone_E4_v1_rr1.wav"))
    assert layers[1]["sources"][0]["source"].endswith("Tone_G4_v1_rr1.wav")
    assert layers[1]["settings"]["swap"] == 1 and layers[0]["notes"][0]["midi"] == 62
    assert not ledger.schema_errors("sources", ledger.read_sources(tmp_path / "run" / "SOURCES.json"))
    keys = {r["key"] for r in res.rows}
    assert all(s["ledgerKey"] in keys for layer in layers for s in layer["sources"])
    art, pub = tmp_path / "art", tmp_path / "pub"
    release.release(res.out, None, art, pub, date="2026-10-23")
    assert [p for p in licence_check.check(art, pub) if p.severity == "error"] == []


def test_sampler_layer_refuses_nc_pack_and_licence_check_sees_samples(tmp_path):
    libs = _pitched_pack(tmp_path / "libs", licence="CC-BY-NC-4.0", commercial_ok=False)
    with pytest.raises(render.LicenceError):
        render.render(_sampler_recipe(), out=tmp_path / "run", run="run", libraries=libs)
    res = render.render(_sampler_recipe(), out=tmp_path / "run2", run="run2", libraries=libs, strict=False)
    art, pub = tmp_path / "art", tmp_path / "pub"
    release.release(res.out, None, art, pub, date="2026-10-23")
    codes = {p.code for p in licence_check.check(art, pub) if p.severity == "error"}
    assert {"disallowed-licence", "not-commercial"} <= codes


def test_sampler_prior_render_with_report(tmp_path):
    from sampler.engine import Sampler, parse_note_spec
    from sampler.instrument import from_folder

    libs = _pitched_pack(tmp_path / "libs")
    s = Sampler()
    s.add(from_folder(libs / "testlib" / "pack1" / "Tones", pitched=True), "t")
    r = s.render(parse_note_spec("0:C4:0.3 0.2:G4:0.3"))
    wav = r.write(tmp_path / "phrase.wav")
    wav.with_suffix(".json").write_text(json.dumps(r.report))
    data = _sampler_recipe()
    data["layers"][0]["source"] = {"sampler": {"render": str(wav)}}
    data["layers"][0].pop("vary")
    res = render.render(data, out=tmp_path / "run", run="run", libraries=libs, date="2026-10-23", count=1)
    layer = next(iter(res.sources.values()))["layers"][0]
    assert len(layer["sources"]) == 2 and layer["render"].startswith("phrase.wav sha256:")


def test_swap_mode_cycle_is_deterministic():
    data = recipe(count=4)
    data["layers"][0]["vary"]["swapMode"] = "cycle"
    plans, _, _ = rcp.plan_variants(data)
    assert [p.layers["attack"].swap_index for p in plans] == [0, 1, 2, 0]


def test_critic_ai_steps_reach_the_ledger(tmp_path, monkeypatch):
    libs = make_library(tmp_path / "libs")
    res = render.render(recipe(count=2), out=tmp_path / "run", run="run", libraries=libs, date="2026-10-23")
    master = res.out / "masters" / "hit.test-v2.wav"
    crit = tmp_path / "critic"
    crit.mkdir()
    doc = {"schema": "audiolab.critic.file/1", "file": {"path": str(master), "sha256": ledger.sha256_file(master)},
           "ai_steps": [{"step": "critic:audiobox", "model": "facebook/audiobox-aesthetics"},
                        {"step": "critic:clap", "model": "laion/clap-htsat-unfused"}]}
    (crit / "hit.test-v2.json").write_text(json.dumps(doc))
    (crit / "other.json").write_text(json.dumps({**doc, "file": {"sha256": "f" * 64}}))
    monkeypatch.setattr(ledger, "resolve_model", lambda m: m if "@" in m else f"{m}@rev1")
    monkeypatch.setattr(critic_link, "hf_weights_sha", lambda repo, rev: "4" * 64)
    out = critic_link.apply(res.out / "SOURCES.json", [crit], res.out / "licences.rows.jsonl")
    assert out["files"] == 1 and out["unmatched"] == 1 and out["steps"] == 2
    recs = ledger.records(ledger.read_sources(res.out / "SOURCES.json"))
    v2 = next(r for r in recs.values() if r["variant"] == 2)
    v1 = next(r for r in recs.values() if r["variant"] == 1)
    assert v2["aiSteps"] == ["critic:audiobox", "critic:clap"] and not v1["aiSteps"]
    assert "facebook/audiobox-aesthetics@rev1" in v2["models"]
    art, pub = tmp_path / "art", tmp_path / "pub"
    release.release(res.out, None, art, pub, date="2026-10-23")
    assert [p for p in licence_check.check(art, pub) if p.severity == "error"] == []
    # A no-AI source that the critic heard anyway is caught.
    rows = [{**r, "ai_input_allowed": False} if r["kind"] == "source" else r for r in ledger.read_rows(art / "licences.jsonl")]
    (art / "licences.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
    assert "ai-forbidden" in {p.code for p in licence_check.check(art, pub)}


def test_short_sub_sound_passes_dc_without_mean_zeroing():
    """A 110 ms sub thump keeps a plain mean above 0.1 % FS after the 35 Hz high-pass, with no DC at
    all: the critic measures true DC (critic.audio.dc_estimate), so the chain needs no Hann
    correction that only games the mean (§4.3.1, §5.5)."""
    from build import chain, synth
    from critic.audio import dc_estimate

    x = synth.generate("sub_thump", {"startHz": 95, "endHz": 45, "glideMs": 45, "durMs": 110, "decayMs": 100,
                                     "click": 0.25, "driveDb": 4}, 1, SR)[:, None]
    params = {"dcHpfHz": 35, "saturation": {"driveDb": 6, "mix": 0.45}, "tail": {"floorDb": -60, "fadeMs": 10},
              "normalise": {"mode": "lufs-m-max", "target": -20}, "limiter": {"ceilingDbtp": -1.0, "maxGrDb": 6}}
    y, rep = chain.run(x, SR, params)
    assert abs(float(y.mean())) > 0.001            # the plain mean of a short decaying wave
    assert dc_estimate(y, SR) < 0.001              # but no DC offset
    assert "dc0" not in rep["summary"]
    # A real offset is still seen, and the chain's high-pass removes it.
    assert dc_estimate(y + 0.003, SR) > 0.002
    y2, _ = chain.run(x + 0.01, SR, params)
    assert dc_estimate(y2, SR) < 0.001
