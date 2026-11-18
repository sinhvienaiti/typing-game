"""Library fetcher pieces that run without network: page parsing, zip safety, git, ledger."""
import json
import os
import subprocess
import zipfile

import pytest

from gen import fetch_libraries as F
from gen import libraries as L

PAGE = """<h1 class='mobile-text-center mobile-contain' style='margin-top:0'>Impact Sounds</h1>
<tr><td class='title text-muted'>Files</td>
<td>130×</td></tr>
<tr><td class='title text-muted'>License</td>
<td class='bold'><a href='https://creativecommons.org/publicdomain/zero/1.0/' target='_blank'>Creative Commons CC0</a></td></tr>
<td title='22/07/2024'><span class='type no-select'>1.1</span><span class='description'>Small fixes</span>
<td title='19/12/2019'><span class='type grey'>1.0</span><span class='description text-muted'>Released in 2019</span>
<a id='donate-text' href='https://kenney.nl/media/pages/assets/impact-sounds/87b4dd-1677/kenney_impact-sounds.zip'>x</a>
"""


def test_kenney_page_parse_and_cc0_check():
    info = F.parse_kenney_page(PAGE)
    assert info["title"] == "Impact Sounds" and info["files_on_page"] == 130
    assert (info["version"], info["updated"], info["year"]) == ("1.1", "2024-07-22", 2019)
    assert info["zip_url"].endswith("/kenney_impact-sounds.zip")
    assert F.page_is_cc0(info)
    other = F.parse_kenney_page(PAGE.replace("publicdomain/zero/1.0/", "licenses/by/4.0/").replace("CC0", "BY"))
    assert not F.page_is_cc0(other)


def test_safe_extract_is_idempotent_and_refuses_traversal(tmp_path):
    good = tmp_path / "good.zip"
    with zipfile.ZipFile(good, "w") as z:
        z.writestr("License.txt", "License: (Creative Commons Zero, CC0)")
        z.writestr("Audio/a.ogg", b"OggS0000")
    dest = tmp_path / "pack"
    files, written = F.safe_extract(good, dest)
    assert written == 2 and (dest / "Audio/a.ogg").read_bytes() == b"OggS0000"
    assert F.safe_extract(good, dest)[1] == 0                      # second run touches nothing
    (dest / "Audio/a.ogg").write_bytes(b"broken")
    assert F.safe_extract(good, dest)[1] == 1                      # resume repairs a changed file
    bad = tmp_path / "bad.zip"
    with zipfile.ZipFile(bad, "w") as z:
        z.writestr("../evil.txt", "x")
    with pytest.raises(RuntimeError):
        F.safe_extract(bad, tmp_path / "out")
    assert not (tmp_path / "evil.txt").exists()


def test_default_selection_follows_the_plan():
    names = {p.split("/")[-1] for p in L.VCSL.paths}
    for want in ("Dan Tranh", "Gong 1", "Gong 2", "Slit Drum", "Woodblock", "Anvil", "Hand Chimes",
                 "Tubular Bells 1", "Tubular Bells 2", "Frame Drum", "Folk Harp"):
        assert want in names
    assert not any("Nepalese" in p for p in L.VCSL.paths + L.VSCO2CE.paths)
    vsco = {p.split("/")[-1] for p in L.VSCO2CE.paths}
    assert {"Cello Section", "Harp", "Flute", "F Horn", "Tenor Trombone", "Percussion"} <= vsco
    with pytest.raises(SystemExit):
        F.check_paths(L.VCSL, ["Idiophones/Struck Idiophones/Hand Bells, Nepalese"])
    with pytest.raises(SystemExit):                                # a parent folder would pull it in
        F.check_paths(L.VCSL, ["Idiophones/Struck Idiophones"])
    assert F.check_paths(L.VCSL, ["a/b/", "a/b"]) == ["a/b"]


def _local_repo(tmp_path):
    repo = tmp_path / "origin"
    (repo / "Idio/Wood").mkdir(parents=True)
    (repo / "Idio/Other").mkdir(parents=True)
    (repo / "Idio/Wood/wood_click_f_rr1.wav").write_bytes(b"RIFF-wood")
    (repo / "Idio/Other/big.wav").write_bytes(b"RIFF-other")
    (repo / "LICENSE").write_text("CC0 1.0 Universal")
    env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}
    run = lambda *a: subprocess.run(["git", "-C", str(repo), *a], check=True, capture_output=True,  # noqa: E731
                                    text=True, env=env).stdout.strip()
    run("init", "-q")
    run("add", "-A")
    run("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "init")
    run("config", "uploadpack.allowfilter", "true")
    run("config", "uploadpack.allowanysha1inwant", "true")
    return repo, run("rev-parse", "HEAD")


def test_sparse_checkout_pinned_resumable(tmp_path):
    repo, sha = _local_repo(tmp_path)
    dest = tmp_path / "lib"
    url = f"file://{repo}"
    assert F.sparse_checkout(dest, url, sha, ["Idio/Wood"], allow_file=True) == sha
    assert (dest / "Idio/Wood/wood_click_f_rr1.wav").exists() and (dest / "LICENSE").exists()
    assert not (dest / "Idio/Other").exists()
    (dest / "Idio/Wood/wood_click_f_rr1.wav").unlink()            # interrupted / damaged checkout
    assert F.sparse_checkout(dest, url, sha, ["Idio/Wood"], allow_file=True) == sha
    assert (dest / "Idio/Wood/wood_click_f_rr1.wav").read_bytes() == b"RIFF-wood"
    with pytest.raises(RuntimeError):                              # file:// is refused unless allowed
        F.sparse_checkout(tmp_path / "lib2", url, sha, ["Idio/Wood"])


def test_fetch_git_library_writes_ledger_licence_and_checksums(tmp_path):
    repo, sha = _local_repo(tmp_path)
    lib = L.GitLibrary(key="vcsl", title="Test", repo=f"file://{repo}", web="https://example.invalid/vcsl",
                       commit=sha, sfz_branch="sfz", sfz_commit=sha, author="A", paths=("Idio/Wood",),
                       deny=("Idio/Bells",))
    root = tmp_path / "libraries"
    cache = L.ShaCache(root)
    recs = F.fetch_git_library(root, lib, [], offline=False, cache=cache, allow_file=True)
    cache.save()
    L.upsert_ledger(recs, root)
    L.upsert_ledger(recs, root)                                     # idempotent
    rows = L.read_ledger(root)
    assert [r["path"] for r in rows] == ["vcsl/Idio/Wood"]
    row = rows[0]
    assert row["commit"] == sha and row["licence"] == "CC0-1.0" and row["files"] == 1
    assert row["ai_input_allowed"] and row["commercial_ok"] and not row["attribution_required"]
    assert (root / row["licence_copy"]).read_text().count(sha) >= 1
    assert (root / "vcsl/CHECKSUMS.sha256").exists()
    line = L.licence_line(root / "vcsl/Idio/Wood/wood_click_f_rr1.wav", root)
    for k in ("sha256", "library", "pack", "file", "url", "author", "licence", "licence_version", "downloaded",
              "licence_copy", "commercial_ok", "attribution_required", "attribution_text", "ai_input_allowed",
              "raw_redistribution_allowed", "genai_preference", "release_file"):
        assert k in line, k
    assert line["url"] == f"https://example.invalid/vcsl/blob/{sha}/Idio/Wood/wood_click_f_rr1.wav"
    assert json.loads(json.dumps(line)) == line


def test_record_for_prefers_longest_prefix(tmp_path):
    L.upsert_ledger([{"library": "x", "path": "x/a", "pack": "A"}, {"library": "x", "path": "x/a/b", "pack": "B"}],
                    tmp_path)
    assert L.record_for(tmp_path / "x/a/b/c.wav", tmp_path)["pack"] == "B"
    assert L.record_for(tmp_path / "x/a/c.wav", tmp_path)["pack"] == "A"
    assert L.record_for(tmp_path / "x/ab/c.wav", tmp_path) is None


def test_licence_lines_from_a_sampler_report(tmp_path, capsys):
    from gen import licence_lines
    root = tmp_path / "libraries"
    (root / "vcsl/Idio/Wood").mkdir(parents=True)
    (root / "vcsl/Idio/Wood/a.wav").write_bytes(b"RIFF")
    L.upsert_ledger([{**L.CC0_FLAGS, "library": "vcsl", "pack": "Wood", "path": "vcsl/Idio/Wood", "commit": "abc",
                      "web": "https://example.invalid/vcsl", "downloaded": "2026-10-23",
                      "licence_copy": "vcsl/LICENSE-2026-10-23.txt"}], root)
    rep = tmp_path / "r.json"
    rep.write_text(json.dumps({"sources": [{"file": "vcsl/Idio/Wood/a.wav"}, {"file": "/elsewhere/own.wav"}]}))
    assert licence_lines.main([str(rep), "vcsl/Idio/Wood/a.wav", "--root", str(root)]) == 2   # one unknown file
    out = [json.loads(x) for x in capsys.readouterr().out.splitlines()]
    assert len(out) == 1 and out[0]["licence"] == "CC0-1.0" and out[0]["file"] == "Idio/Wood/a.wav"
