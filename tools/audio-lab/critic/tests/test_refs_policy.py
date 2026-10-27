import json

import numpy as np

from critic import artifacts, audio as A, features, pipeline, policy
from critic import spec as S
from critic.tests import synth


def test_smeared_attack_flag_tracks_the_crack_rise():
    sp = S.from_mapping({"group": "hit_heavy"})

    def l1b(x):
        a = A.from_array(x, 48000)
        m, ctx = features.analyze(a, sp)
        return artifacts.detect(a, m, ctx, sp)

    assert "smeared_attack" in {f["id"] for f in l1b(synth.smeared(15.0))["flags"]}
    assert "smeared_attack" not in {f["id"] for f in l1b(synth.smeared(2.0))["flags"]}
    assert l1b(synth.punchy())["metrics"]["hf_attack_ms"] <= 1.0
    # no HF layer at all (low-passed boom): nothing to time
    assert l1b(synth.muddy())["metrics"]["hf_attack_ms"] is None


def test_smear_threshold_follows_refs():
    sp = S.from_mapping({"group": "hit_heavy"})
    a = A.from_array(synth.smeared(15.0), 48000)
    m, ctx = features.analyze(a, sp)
    lax = artifacts.ref_stats([{"hf_attack_ms": v} for v in (12.0, 14.0, 16.0, 18.0)])
    out = artifacts.detect(a, m, ctx, sp, lax)
    assert out["thresholds_source"] == "refs" and "smeared_attack" not in {f["id"] for f in out["flags"]}


def test_card_fields_from_the_specs_lane(tmp_path):
    p = tmp_path / "gun.xung.yaml"
    p.write_text(
        "id: gun.xung\ngame: typing-survival\n"
        "duration: {target_ms: 120, tolerance_pct: 20, min_ms: 96, max_ms: 144}\n"
        "references: [{path: refs/a.wav}]\n"
        "critic: {group: shot_gun, dirty: true, ast: {expected: ['Gunshot, gunfire'], forbid: [Speech]},"
        " head_max_ms: null, rate_hz: 5, refs: []}\n", encoding="utf-8")
    sp = S.load_cards(p)[0]
    assert sp.duration_ms == (120.0, 120.0) and sp.duration_tol == 0.2
    assert sp.ast_forbid == ["Speech"] and sp.ast_expected == ["Gunshot, gunfire"]
    assert sp.head_max_ms is None and sp.rate_hz == 5.0          # explicit null = not checked
    assert sp.refs == [str((tmp_path / "refs" / "a.wav").resolve())]


def test_ref_sets_are_per_card(tmp_path):
    d = tmp_path / "in"
    synth.write(d / "a.hit-1.wav", synth.punchy())
    synth.write(d / "b.hit-1.wav", synth.punchy(seed=4))
    refs = tmp_path / "refs"
    for i in range(5):
        synth.write(refs / f"r{i}.wav", synth.punchy(seed=10 + i))
    cards = tmp_path / "cards.yaml"
    cards.write_text(f"- id: a.hit\n  group: hit_heavy\n  refs: [{refs}]\n- id: b.hit\n  group: hit_heavy\n",
                     encoding="utf-8")
    out = tmp_path / "out"
    batch = pipeline.run([str(d)], spec_path=str(cards), out_dir=out,
                         opts=pipeline.Options(layers=("L1", "L1b", "L2"), quiet=True))
    ra = json.loads((out / "a.hit-1.json").read_text(encoding="utf-8"))
    rb = json.loads((out / "b.hit-1.json").read_text(encoding="utf-8"))
    assert ra["refs"] == {"set": "card:a.hit", "n": 5} and rb["refs"] == {"set": None, "n": 0}
    assert ra["L2"]["refs_used"] > 0 and rb["L2"]["refs_used"] == 0
    assert ra["score"]["stage"] == "ref5" and rb["score"]["stage"] == "batch1"
    assert batch["refs"]["card:a.hit"]["n"] == 5


def test_ai_policy_paths_ledgers_and_skip(tmp_path):
    assert policy.path_forbidden("/x/libraries/_no-ai/a.wav") and policy.path_forbidden("/x/Sonniss/GDC/a.wav")
    lib = tmp_path / "libraries"
    (lib / "freesound" / "optout").mkdir(parents=True)
    (lib / "SOURCES.jsonl").write_text(
        json.dumps({"path": "freesound/optout", "ai_input_allowed": False}) + "\n"
        + json.dumps({"path": "kenney/impact-sounds", "ai_input_allowed": True}) + "\n", encoding="utf-8")
    banned = synth.write(lib / "freesound" / "optout" / "x.wav", synth.punchy())
    ok = synth.write(tmp_path / "in" / "y.wav", synth.punchy(seed=3))
    named = synth.write(tmp_path / "in" / "gun.xung-3.wav", synth.punchy(seed=7))
    sha = A.sha256(ok)
    src = tmp_path / "SOURCES.json"
    src.write_text(json.dumps({"$version": 1, "gun.xung-3.wav": {"aiInputAllowed": False, "sha256": "0" * 64},
                               "other.ogg": {"aiInputAllowed": True, "sha256": sha}}), encoding="utf-8")
    pol = policy.load([str(src)], libraries=lib)
    assert pol.check(banned)[0] is False and "freesound/optout" in pol.check(banned)[1]
    assert pol.check(ok, sha) == (True, None)
    assert pol.check(named, A.sha256(named))[0] is False
    jl = tmp_path / "licences.jsonl"
    jl.write_text(json.dumps({"key": "src1", "sha256": sha, "ai_input_allowed": False}) + "\n", encoding="utf-8")
    assert policy.load([str(jl)], libraries=lib).check(ok, sha)[0] is False


def test_forbidden_files_never_reach_learned_layers(tmp_path, monkeypatch):
    from critic import learned
    d = tmp_path / "_no-ai" / "in"
    synth.write(d / "x.wav", synth.punchy())
    called = []
    monkeypatch.setattr(learned, "run_l3", lambda items: called.append(items) or {})
    monkeypatch.setattr(learned, "run_l4", lambda items, m: called.append(items) or ({}, {}))
    out = tmp_path / "out"
    pipeline.run([str(d)], out_dir=out, opts=pipeline.Options(layers=("L1", "L2", "L3", "L4"), quiet=True))
    r = json.loads((out / "x.json").read_text(encoding="utf-8"))
    assert called == [] and r["cloud_ok"] is False and r["ai_steps"] == []
    assert r["L3"]["available"] is False and "_no-ai" in r["L3"]["reason"]
    assert "Không đưa vào mô hình" in (out / "summary.md").read_text(encoding="utf-8")


def test_ai_steps_are_reported_for_the_ledger(tmp_path, monkeypatch):
    from critic import learned
    d = tmp_path / "in"
    synth.write(d / "x.wav", synth.punchy())
    monkeypatch.setattr(learned, "run_l3", lambda items: {it.key: {"available": True, "scores": {"PQ": 6.0, "CE": 3.0}}
                                                           for it in items})
    out = tmp_path / "out"
    pipeline.run([str(d)], out_dir=out, opts=pipeline.Options(layers=("L1", "L2", "L3"), quiet=True))
    r = json.loads((out / "x.json").read_text(encoding="utf-8"))
    pinned = f"{learned.AES_REPO}@{learned.revision(learned.AES_REPO)}"      # the revision it loaded (§10.8)
    assert r["ai_steps"] == [{"step": "critic:audiobox", "model": pinned}]
    b = json.loads((out / "_batch.json").read_text(encoding="utf-8"))
    assert b["files"][0]["ai_steps"] == [f"critic:audiobox@{pinned}"] and len(b["files"][0]["sha256"]) == 64


def test_mp3_free_formats_load(tmp_path):
    x = synth.punchy()
    for ext, sub in ((".flac", "PCM_24"), (".ogg", "VORBIS")):
        p = synth.write(tmp_path / f"x{ext}", x, subtype=sub)
        a = A.load(p)
        assert a.sr == 48000 and abs(a.duration - 0.45) < 0.01 and np.max(np.abs(a.data)) > 0.5
