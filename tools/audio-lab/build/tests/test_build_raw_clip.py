"""Raw L1 clip gate per layer source (§4.3.1): a clipped source never slips through mix + chain."""
import json

import numpy as np
import pytest
import soundfile as sf

from build import ledger, licence_check, release, render
from build.tests.helpers import make_library, recipe

SR = 48000


def _clipped_hit(n: int = int(0.14 * SR)) -> np.ndarray:
    """A hit hard-clipped at 0.6 and written as 16-bit PCM: after normalising, its flat tops sit
    below 0.999 FS, the Stable Audio 3 case of §4.3.1."""
    rng = np.random.default_rng(5)
    t = np.arange(n) / SR
    x = (np.sin(2 * np.pi * 90 * t) + 0.6 * rng.normal(0, 1, n) * np.exp(-t * 80)) * np.exp(-t * 18) * 1.8
    x[:48] *= np.linspace(0, 1, 48)
    return np.round(np.clip(x, -0.6, 0.6) * 32767) / 32767


def _libs(tmp_path):
    libs = tmp_path / "libs"
    make_library(libs)
    sf.write(str(libs / "testlib" / "pack1" / "Audio" / "hit_000.wav"), _clipped_hit(), SR, subtype="PCM_16")
    return libs


def _recipe(allow: str | None = None) -> dict:
    r = recipe(count=2)
    r["layers"][0]["vary"].pop("swap")            # every variant uses the clipped hit_000
    if allow:
        r["layers"][0]["allowClip"] = allow
    return r


def test_clipped_source_stops_the_render(tmp_path):
    libs = _libs(tmp_path)
    with pytest.raises(render.RawClipError, match="hit_000.wav"):
        render.render(_recipe(), out=tmp_path / "r", run="r", libraries=libs, date="2026-10-23")
    assert not (tmp_path / "r").exists()           # nothing written before the gate


def test_clean_sources_record_a_passing_raw_qa(tmp_path):
    libs = tmp_path / "libs"
    make_library(libs)
    res = render.render(recipe(count=2), out=tmp_path / "ok", run="ok", libraries=libs, date="2026-10-23")
    rec = next(iter(ledger.records(res.sources).values()))
    attack = next(ly for ly in rec["layers"] if ly["id"] == "attack")
    assert attack["rawQa"]["verdict"] == "PASS" and attack["rawQa"]["files"][0]["file"].startswith("hit_00")
    assert all("rawQa" not in ly for ly in rec["layers"] if ly["kind"] == "synth")
    assert ledger.schema_errors("sources", {"$version": ledger.SOURCES_VERSION, **ledger.records(res.sources)}) == []


def test_allow_clip_is_recorded_and_accepted_downstream(tmp_path):
    from critic import pipeline

    libs = _libs(tmp_path)
    res = render.render(_recipe("lớp méo có chủ ý cho thử nghiệm"), out=tmp_path / "x", run="x",
                        libraries=libs, date="2026-10-23")
    rec = next(iter(ledger.records(res.sources).values()))
    qa = rec["layers"][0]["rawQa"]
    assert qa["verdict"] == "BLOCK" and qa["exception"].startswith("lớp méo")
    out = tmp_path / "crit"
    pipeline.run([str(res.out / "masters")], out_dir=out, sources=[str(res.out / "SOURCES.json")],
                 opts=pipeline.Options(layers=("L1",), group="hit_heavy", quiet=True))
    r = json.loads((out / "hit.test-v1.json").read_text("utf-8"))
    chk = next(c for c in r["L1"]["checks"] if c["id"] == "source_clip")
    assert chk["ok"] and chk["value"]["excepted"] == ["attack"]


def test_final_critic_and_licence_check_catch_a_clipped_layer(tmp_path):
    """The mix and the chain hide the flat tops; the layer's rawQa still blocks (finding: L1 bypass)."""
    from critic import pipeline

    libs = _libs(tmp_path)
    res = render.render(_recipe(), out=tmp_path / "s", run="s", libraries=libs, date="2026-10-23", strict=False)
    out = tmp_path / "crit"
    pipeline.run([str(res.out / "masters")], out_dir=out, sources=[str(res.out / "SOURCES.json")],
                 opts=pipeline.Options(layers=("L1",), group="hit_heavy", quiet=True))
    r = json.loads((out / "hit.test-v1.json").read_text("utf-8"))
    assert r["verdict"] == "BLOCK" and "source_clip" in r["L1"]["blocking"]
    assert not any(c["id"] in ("clip_full_scale", "clip_flat_top") and not c["ok"] for c in r["L1"]["checks"])
    art, pub = tmp_path / "art", tmp_path / "pub"
    release.release(res.out, None, art, pub, date="2026-10-23")
    assert "raw-clip" in {p.code for p in licence_check.check(art, pub)}
