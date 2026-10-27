"""A Stable Audio 3 layer carries its licence rows from the candidate record (gen/sa3.py) through
render and release, so licence_check sees the model row and the Stability registration."""
from __future__ import annotations

import json

import numpy as np
import pytest
import soundfile as sf

from build import ledger, licence_check, release, render
from build.tests.helpers import make_library
from gen import sa3

MODEL = "stabilityai/stable-audio-3-optimized@" + "f" * 40


def _install():
    return {"hf": {"repo": "stabilityai/stable-audio-3-optimized", "revision": "f" * 40},
            "repo": {"url": "https://github.com/Stability-AI/stable-audio-3", "commit": "e" * 40},
            "venv": {"key_versions": {"mlx": "0.32.4"}},
            "weights": [{"file": "MLX/dit_sm-sfx_f16.npz", "sha256": "1" * 64},
                        {"file": "MLX/same_s_decoder_f32.npz", "sha256": "2" * 64},
                        {"file": "MLX/t5gemma_f16.npz", "sha256": "3" * 64}]}


def _candidate(tmp, peak=1.2):
    lic = tmp / "licences"
    lic.mkdir()
    (lic / "stability-registration.txt").write_text("registration (test)\n")
    (lic / "stability-community-license-2026-10-23.txt").write_text("licence (test)\n")
    (lic / "gemma-terms-of-use-2026-10-23.txt").write_text("gemma (test)\n")
    raw = tmp / "raw"
    raw.mkdir()
    t = np.arange(44100) / 44100
    x = peak * np.sin(2 * np.pi * 400 * t) * np.exp(-t / 0.05)
    f32 = raw / "hit.test__A__s1.f32.wav"
    sf.write(str(f32), np.stack([x, x], axis=1), 44100, subtype="FLOAT")
    rows, copies = sa3.licence_rows(_install(), licences=lic, date="2026-10-23")
    rec = {"schema": sa3.RECORD_SCHEMA, "id": "hit.test", "candidate": f32.name[:-8], "prompt": "a clank", "seed": 1,
           "cfg": 1.0, "model": {"id": MODEL}, "files": {"f32": {"path": str(f32), "sha256": ledger.sha256_file(f32)}},
           "licence": {"rows": rows, "copies": copies}}
    rp = raw / "hit.test__A__s1.json"
    rp.write_text(json.dumps(rec), "utf-8")
    return f32, rp


def _recipe(f32, rp, window=(0.0, 0.2)):
    return {"schema": "audiolab.recipe/1", "game": "typing-survival", "id": "hit.test", "group": "hit-small", "channels": 1,
            "layers": [{"id": "tick", "role": "attack", "source": {"library": "testlib/pack1/Audio/hit_000.wav"},
                        "trim": {"endMs": 30}, "fadeOutMs": 20},
                       {"id": "body", "role": "body", "source": {"gen": {
                           "tool": "stable-audio-3 (sa3_batch.py)", "model": MODEL,
                           "licence": "LicenseRef-Stability-Community-2024", "file": str(f32), "record": str(rp),
                           "window": list(window)}}}],
            "chain": {"maxLengthMs": 150}, "variants": {"count": 1, "seed": 1}, "export": {"path": "sfx/hits/hit-test"}}


def test_gen_record_rows_reach_the_release_and_pass_licence_check(tmp_path):
    f32, rp = _candidate(tmp_path)
    libs = make_library(tmp_path / "libs")
    res = render.render(_recipe(f32, rp), out=tmp_path / "run", run="run", libraries=libs, date="2026-10-23")
    keys = {r["key"] for r in ledger.read_rows(res.out / "licences.rows.jsonl")}
    assert f"model:{MODEL}" in keys and "acceptance:LicenseRef-Stability-Community-2024@2024-07-05" in keys
    body = next(ly for ly in next(iter(res.sources.values()))["layers"] if ly["id"] == "body")
    assert body["record"] == rp.name and body["prompt"] == "a clank" and body["seed"] == 1
    assert body["rawQa"]["verdict"] == "PASS"            # float copy over 1.0 is not a clip
    art, pub = tmp_path / "art-src" / "audio", tmp_path / "public" / "audio"
    release.release(res.out, None, art, pub, date="2026-10-23")
    assert (art / "licences" / "stability-registration.txt").is_file()
    errors = [p for p in licence_check.check(art, pub) if p.severity == "error"]
    assert errors == []
    # without the registration file in the tree, the Stability layer is refused
    (art / "licences" / "stability-registration.txt").unlink()
    assert "stability-unregistered" in {p.code for p in licence_check.check(art, pub)}


def test_gen_record_must_describe_the_file(tmp_path):
    f32, rp = _candidate(tmp_path)
    rec = json.loads(rp.read_text())
    rec["files"]["f32"]["sha256"] = "0" * 64
    rp.write_text(json.dumps(rec))
    libs = make_library(tmp_path / "libs")
    with pytest.raises(ValueError, match="sha256"):
        render.render(_recipe(f32, rp), out=tmp_path / "run", run="run", libraries=libs)


def test_gen_gain_db_levels_one_take_among_the_swaps(tmp_path):
    """Batch 1c review: the takes a body layer swaps between come raw from the model, 20 dB or more apart; the
    source's gainDb levels one of them before the layer's chain, and the run records it."""
    from build import sources

    f32, rp = _candidate(tmp_path, peak=0.5)
    src = _recipe(f32, rp)["layers"][1]["source"]
    plain = sources.load(src, libraries=tmp_path, synth_seed=1)
    up = sources.load({"gen": dict(src["gen"], gainDb=6.0)}, libraries=tmp_path, synth_seed=1)
    assert np.allclose(up.audio, plain.audio * 10 ** (6 / 20)) and up.layer_meta["gainDb"] == 6.0
    from build import recipe
    data = _recipe(f32, rp)
    data["layers"][1]["source"]["gen"]["gainDb"] = 6.0
    recipe.validate(data, "hit.test")
