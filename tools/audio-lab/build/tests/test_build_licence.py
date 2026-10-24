import json

import pytest

from build import ledger, licence_check, release, render
from build.tests.helpers import make_library, recipe


def _released_tree(tmp_path, strict=True, **lib_flags):
    libs = make_library(tmp_path / "libs", **lib_flags)
    res = render.render(recipe(count=3), out=tmp_path / "run", run="run", libraries=libs, date="2026-10-23",
                        strict=strict)
    art, pub = tmp_path / "art-src" / "audio", tmp_path / "public" / "audio"
    release.release(res.out, [1, 3], art, pub, date="2026-10-23")
    return art, pub


def _codes(art, pub):
    return sorted({p.code for p in licence_check.check(art, pub) if p.severity == "error"})


def _edit_rows(art, fn):
    path = art / "licences.jsonl"
    rows = [fn(r) for r in ledger.read_rows(path)]
    path.write_text("".join(json.dumps(r) + "\n" for r in rows))


def test_clean_release_passes(tmp_path):
    art, pub = _released_tree(tmp_path)
    assert _codes(art, pub) == []
    assert sorted(p.name for p in (pub / "sfx" / "hits").iterdir()) == ["hit-test-1.ogg", "hit-test-2.ogg"]
    man = json.loads((pub / "manifest.json").read_text())
    assert man["version"] == 2 and man["sounds"]["hit.test"]["files"] == ["sfx/hits/hit-test-1.ogg", "sfx/hits/hit-test-2.ogg"]
    assert (art / "licences" / "testlib-pack1-LICENSE-2026-10-23.txt").is_file()
    assert (art / "recipes" / "hit.test.json").is_file()
    assert licence_check.main(["--art-src", str(art), "--public", str(pub)]) == 0


def test_catches_planted_nc_source(tmp_path):
    art, pub = _released_tree(tmp_path)
    _edit_rows(art, lambda r: {**r, "licence": "CC-BY-NC-4.0"} if r["kind"] == "source" else r)
    codes = _codes(art, pub)
    assert "disallowed-licence" in codes
    assert licence_check.main(["--art-src", str(art), "--public", str(pub)]) == 1


def test_render_refuses_nc_library(tmp_path):
    libs = make_library(tmp_path / "libs", licence="CC-BY-NC-4.0", commercial_ok=False)
    with pytest.raises(render.LicenceError):
        render.render(recipe(count=1), out=tmp_path / "run", run="run", libraries=libs)
    assert not (tmp_path / "run").exists()


def test_catches_nc_library_rendered_without_gate(tmp_path):
    art, pub = _released_tree(tmp_path, strict=False, licence="CC-BY-NC-4.0", commercial_ok=False)
    assert {"disallowed-licence", "not-commercial"} <= set(_codes(art, pub))


def test_catches_missing_record_and_hash_mismatch(tmp_path):
    art, pub = _released_tree(tmp_path)
    (pub / "sfx" / "hits" / "stray.ogg").write_bytes(b"OggS-not-really")
    f = pub / "sfx" / "hits" / "hit-test-1.ogg"
    f.write_bytes(f.read_bytes()[:-10])
    codes = _codes(art, pub)
    assert "missing-record" in codes and "hash-mismatch" in codes


def test_catches_missing_ledger_row(tmp_path):
    art, pub = _released_tree(tmp_path)
    rows = [r for r in ledger.read_rows(art / "licences.jsonl") if r["kind"] != "source"]
    (art / "licences.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
    assert "missing-record" in _codes(art, pub)


def test_catches_unknown_licence_and_missing_copy(tmp_path):
    art, pub = _released_tree(tmp_path)
    _edit_rows(art, lambda r: {**r, "licence": "LicenseRef-Mystery"} if r["kind"] == "source" else r)
    (art / "licences" / "testlib-pack1-LICENSE-2026-10-23.txt").unlink()
    codes = _codes(art, pub)
    assert "unknown-licence" in codes and "missing-licence-copy" in codes


def test_catches_ai_steps_on_no_ai_and_sonniss(tmp_path):
    art, pub = _released_tree(tmp_path, ai_input_allowed=False)
    assert _codes(art, pub) == []                         # rendered only: no AI step yet
    ledger.mark_ai_step(art / "SOURCES.json", "critic:audiobox", model="facebook/audiobox-aesthetics@9b1d")
    assert "ai-forbidden" in _codes(art, pub)
    _edit_rows(art, lambda r: {**r, "library": "sonniss", "licence": "LicenseRef-Sonniss-GDC-2.0", "ai_input_allowed": True})
    codes = _codes(art, pub)
    assert "sonniss-ai" in codes
    assert "missing-record" in codes                      # the critic model has no ledger row


def test_catches_nc_model_and_unregistered_stability(tmp_path):
    art, pub = _released_tree(tmp_path)
    src = ledger.read_sources(art / "SOURCES.json")
    key = next(iter(ledger.records(src)))
    src[key]["layers"].append({"id": "gen", "kind": "gen", "tool": "stable-audio-3",
                               "model": "stabilityai/stable-audio-3-optimized@abc",
                               "licence": "LicenseRef-Stability-Community-2024", "aiSteps": ["generate"]})
    src[key]["models"] = ["facebook/musicgen-small@main"]
    ledger.write_sources(art / "SOURCES.json", src)
    ledger.append_rows(art / "licences.jsonl", [ledger.model_row(
        "stabilityai/stable-audio-3-optimized", "abc", "LicenseRef-Stability-Community-2024",
        "https://stability.ai/community-license-agreement", "1" * 64, "generate", "2026-10-23")])
    codes = _codes(art, pub)
    assert "nc-model" in codes and "stability-unregistered" in codes
    (art / "licences" / "stability-registration.txt").write_text("registered 2026-10-23\n")
    ledger.append_rows(art / "licences.jsonl", [ledger.acceptance_row(
        "LicenseRef-Stability-Community-2024", "2024-07-05", "owner", "licences/stability-registration.txt", art,
        "https://stability.ai/community-license-agreement", "2026-10-23")])
    assert "stability-unregistered" not in _codes(art, pub)


def test_cc_by_needs_credits(tmp_path):
    art, pub = _released_tree(tmp_path, licence="CC-BY-4.0", attribution_required=True,
                              attribution_text="Hit pack by Test (CC-BY 4.0)")
    assert _codes(art, pub) == []                         # release wrote CREDITS.md
    (art / "CREDITS.md").write_text("# Ghi công\n")
    assert "missing-credit" in _codes(art, pub)


def test_default_scan_skips_games_without_pipeline(capsys):
    assert licence_check.main(["--json"]) in (0, 1)
    out = json.loads(capsys.readouterr().out)
    assert {g["game"] for g in out["games"]} == {"dragon-hold", "typing-defense", "typing-survival", "space-typing"}


def test_rerelease_replaces_previous_set(tmp_path):
    art, pub = _released_tree(tmp_path)
    release.release(tmp_path / "run", [2], art, pub, date="2026-10-23")
    assert sorted(p.name for p in (pub / "sfx" / "hits").iterdir()) == ["hit-test-1.ogg"]
    recs = ledger.records(ledger.read_sources(art / "SOURCES.json"))
    assert list(recs) == ["sfx/hits/hit-test-1.ogg"] and recs["sfx/hits/hit-test-1.ogg"]["renderVariant"] == 2
    assert _codes(art, pub) == []


def test_build_cli_dispatches_licence_check(tmp_path):
    from build.__main__ import main

    art, pub = _released_tree(tmp_path)
    assert main(["licence-check", "--art-src", str(art), "--public", str(pub)]) == 0
    _edit_rows(art, lambda r: {**r, "licence": "CC-BY-NC-4.0"} if r["kind"] == "source" else r)
    assert main(["licence-check", "--art-src", str(art), "--public", str(pub)]) == 1


def test_no_ai_folder_and_init_audio_from_sonniss(tmp_path):
    """A library under _no-ai/ is ai_input_allowed=false; audio-to-audio from a Sonniss hero is caught."""
    libs = make_library(tmp_path / "libs", path="_no-ai/sonniss/pack1", library="sonniss",
                        licence="LicenseRef-Sonniss-GDC-2.0",
                        licence_copy="_no-ai/sonniss/pack1/LICENSE-2026-10-23.txt")
    pack = libs / "_no-ai" / "sonniss" / "pack1"
    pack.parent.mkdir(parents=True)
    (libs / "testlib" / "pack1").rename(pack)
    r = recipe(count=1)
    r["layers"][0]["source"] = {"library": "_no-ai/sonniss/pack1/Audio/hit_000.wav"}
    r["layers"][0]["vary"] = {}
    res = render.render(r, out=tmp_path / "run", run="run", libraries=libs, date="2026-10-23")
    assert all(v["aiInputAllowed"] is False for v in res.report["variants"])
    art, pub = tmp_path / "art-src" / "audio", tmp_path / "public" / "audio"
    release.release(res.out, None, art, pub, date="2026-10-23")
    assert _codes(art, pub) == []
    # A model layer that used the Sonniss-layered master as init audio.
    src = ledger.read_sources(art / "SOURCES.json")
    key, rec = next(iter(ledger.records(src).items()))
    rec["layers"].append({"id": "a2a", "kind": "gen", "tool": "ace-step", "model": "ACE-Step/Ace-Step1.5@abc",
                          "licence": "MIT", "initAudio": f"hero.wav sha256:{rec['masterSha256']}",
                          "aiSteps": ["generate", "init-audio"]})
    ledger.write_sources(art / "SOURCES.json", src)
    ledger.append_rows(art / "licences.jsonl", [ledger.model_row(
        "ACE-Step/Ace-Step1.5", "abc", "MIT", "https://opensource.org/license/mit", "2" * 64, "generate", "2026-10-23")])
    assert "sonniss-ai" in _codes(art, pub)


def test_mark_ai_step_with_repo_only_model(tmp_path):
    """Critic reports repo names (critic.learned.AI_STEPS); the check matches a ledger row for that repo."""
    art, pub = _released_tree(tmp_path)
    ledger.mark_ai_step(art / "SOURCES.json", "critic:audiobox", model="example/critic-not-in-cache")
    assert "missing-record" in _codes(art, pub)
    ledger.append_rows(art / "licences.jsonl", [ledger.model_row(
        "example/critic-not-in-cache", "abc", "CC-BY-4.0", "https://example.invalid", "3" * 64, "critic", "2026-10-23")])
    probs = licence_check.check(art, pub)
    assert [p.code for p in probs if p.severity == "error"] == []
    assert any(p.code == "model-revision" for p in probs)


def test_unadopted_game_is_skipped_not_passed_and_its_audio_is_scanned(tmp_path, monkeypatch, capsys):
    """Review finding: licence-check printed ĐẠT while checking nothing (§10.7 rule 1)."""
    import hashlib

    from build import licence_check as lc

    root = tmp_path / "games" / "space-typing"
    d = root / "public" / "assets" / "audio"
    d.mkdir(parents=True)
    (d / "old.ogg").write_bytes(b"old cc0 file")
    (d / "new.ogg").write_bytes(b"new file without a record")
    legacy = {"public/assets/audio/old.ogg": hashlib.sha256(b"old cc0 file").hexdigest()}
    n, probs = lc.scan_unadopted(root, "space-typing", legacy)
    assert n == 1 and [(p.code, p.where) for p in probs] == [("missing-record", "public/assets/audio/new.ogg")]
    (d / "new.ogg").unlink()
    (d / "old.ogg").write_bytes(b"changed")
    assert [p.code for p in lc.scan_unadopted(root, "space-typing", legacy)[1]] == ["legacy-changed"]
    (d / "old.ogg").write_bytes(b"old cc0 file")
    monkeypatch.setattr(lc, "targets", lambda games, staging: [
        ("space-typing", root / "art-src" / "audio", d, root),
        ("dragon-hold", tmp_path / "dh" / "art-src" / "audio", tmp_path / "dh" / "pub", tmp_path / "dh")])
    monkeypatch.setattr(lc, "load_legacy", lambda: {"space-typing": legacy})
    assert lc.main([]) == 0
    out = capsys.readouterr().out
    assert "Kiểm giấy phép: BỎ QUA" in out and "ĐẠT" not in out and "1 file cũ được miễn" in out
    (d / "stray.wav").write_bytes(b"x")
    assert lc.main([]) == 1 and "TRƯỢT" in capsys.readouterr().out


def test_legacy_list_covers_the_space_typing_files_in_git():
    from build import licence_check as lc

    leg = lc.load_legacy()
    assert len(leg.get("space-typing", {})) >= 100
    assert all(len(v) == 64 for v in leg["space-typing"].values())
