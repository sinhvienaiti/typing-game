"""Existing-atlas CLI: decoded orientation, repeatability and isolated atomic writes."""
from __future__ import annotations

import copy
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

import numpy as np
import pytest
from PIL import Image

from vfxflip import atlas_ktx2, ktx2, pipeline
from vfxflip.__main__ import main

HAS_KTX2 = bool(shutil.which("node") and (pipeline.TOOL_DIR / "ktx2/node_modules/ktx2-encoder").is_dir())


@pytest.fixture
def existing(tmp_path, monkeypatch):
    monkeypatch.setenv("VFXLAB_HOME", str(tmp_path / "home"))
    folder = tmp_path / "atlas có dấu"
    folder.mkdir()
    pixels = np.zeros((32, 64, 4), np.uint8)
    pixels[:16] = [255, 0, 0, 255]
    pixels[16:] = [0, 0, 255, 128]
    entries = {}
    for cid in ("selected", "other"):
        Image.fromarray(pixels).save(folder / f"{cid}.atlas.png")
        (folder / f"{cid}.json").write_text('{"atlas": "không đổi"}', encoding="utf-8")
        entries[cid] = {"file": f"{cid}.atlas.png", "width": 64, "height": 32,
                        "md5": "giữ nguyên", "custom": [None, {"n": 1.25}], "role": "impact"}
    data = {"version": 1, "note": "Giữ đầy đủ dấu tiếng Việt", "flipbooks": entries}
    (folder / "manifest.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    return folder, data, pixels


def _snapshot(folder):
    return {p.name: (p.read_bytes(), p.stat().st_mtime_ns) for p in folder.iterdir() if p.is_file()}


def _fake_encode(png, output, *args):
    output.write_bytes(b"KTX2-test:" + png.read_bytes())
    return {"bytes": output.stat().st_size}


@pytest.mark.skipif(not HAS_KTX2, reason="cần node và bộ mã hoá KTX2 cục bộ")
def test_cli_decoded_yflip_mips_manifest_and_identical_reruns(existing, tmp_path, monkeypatch):
    folder, original, pixels = existing
    before = _snapshot(folder)
    assert main(["ktx2", str(folder), "--only", " selected, "]) == 0
    dest = folder / "selected.uastc.ktx2"
    data = json.loads((folder / "manifest.json").read_text())
    group = data["flipbooks"]["selected"].pop("ktx2")
    assert data == original
    assert group["yFlip"] is True and group["mipmaps"] is True and group["transfer"] == "srgb"
    item = group["uastc"]
    assert item["file"] == dest.name
    assert item["bytes"] == dest.stat().st_size
    assert item["md5"] == hashlib.md5(dest.read_bytes()).hexdigest()
    assert item["sourceMd5"] == hashlib.md5((folder / "selected.atlas.png").read_bytes()).hexdigest()
    rgba = tmp_path / "decoded.rgba"
    result = subprocess.run(["node", str(pipeline.TOOL_DIR / "ktx2/inspect.mjs"), str(dest),
                             "--rgba", str(rgba)], capture_output=True, text=True, check=True)
    info = json.loads(result.stdout.strip().splitlines()[-1])
    assert (info["width"], info["height"], info["levels"]) == (64, 32, 7)
    assert info["uastc"] and info["transfer"] == 2 and info["supercompression"] == 2
    decoded = np.frombuffer(rgba.read_bytes(), np.uint8).reshape(pixels.shape)
    assert np.abs(decoded.astype(int) - pixels[::-1].astype(int)).max() <= 3
    assert all(_snapshot(folder)[name] == value for name, value in before.items() if name != "manifest.json")
    assert not (folder / "other.uastc.ktx2").exists()

    first = _snapshot(folder)
    # Force re-encodes the same source to the same bytes (not merely a cache hit).
    assert main(["ktx2", str(folder), "--only", "selected", "--force"]) == 0
    assert {k: v[0] for k, v in _snapshot(folder).items()} == {k: v[0] for k, v in first.items()}

    def unexpected(*args, **kwargs):
        pytest.fail("md5 khớp phải bỏ qua bộ mã hoá")

    monkeypatch.setattr(ktx2, "encode", unexpected)
    stable = _snapshot(folder)
    assert main(["ktx2", str(folder), "--only", "selected"]) == 0
    assert _snapshot(folder) == stable


def test_source_change_and_corrupt_output_invalidate_cache(existing, monkeypatch):
    folder, _, _ = existing
    monkeypatch.setattr(ktx2, "encode", _fake_encode)
    assert atlas_ktx2.run(folder) == {"encoded": 2, "skipped": 0}
    assert atlas_ktx2.run(folder) == {"encoded": 0, "skipped": 2}
    png = folder / "selected.atlas.png"
    Image.new("RGBA", (64, 32), "green").save(png)
    assert atlas_ktx2.run(folder) == {"encoded": 1, "skipped": 1}
    dest = folder / "selected.uastc.ktx2"
    raw = dest.read_bytes()
    dest.write_bytes(bytes([raw[0] ^ 1]) + raw[1:])  # same size, different md5
    assert atlas_ktx2.run(folder) == {"encoded": 1, "skipped": 1}
    dest.unlink()
    assert atlas_ktx2.run(folder) == {"encoded": 1, "skipped": 1}


@pytest.mark.parametrize("only", ["absent", "selected,absent", " , "])
def test_unknown_only_does_not_write(existing, only):
    folder, _, _ = existing
    before = _snapshot(folder)
    assert main(["ktx2", str(folder), "--only", only]) == 3
    assert _snapshot(folder) == before


@pytest.mark.parametrize("field,value", [("file", "../outside.png"), ("file", "atlas.webp"), ("id", "../escape")])
def test_unsafe_paths_rejected_before_encoding(existing, field, value):
    folder, data, _ = existing
    if field == "id":
        data["flipbooks"][value] = data["flipbooks"].pop("other")
    else:
        data["flipbooks"]["other"][field] = value
    (folder / "manifest.json").write_text(json.dumps(data))
    before = _snapshot(folder)
    assert main(["ktx2", str(folder)]) == 3
    assert _snapshot(folder) == before


def test_failure_leaves_original_files_and_manifest(existing, monkeypatch):
    folder, _, _ = existing
    before = _snapshot(folder)

    def fail(png, output, *args):
        output.write_bytes(b"partial")
        raise ktx2.Ktx2Error("lỗi mã hoá")

    monkeypatch.setattr(ktx2, "encode", fail)
    assert main(["ktx2", str(folder)]) == 3
    assert _snapshot(folder) == before


def test_preserves_other_codec_and_concurrent_unrelated_edit(existing, monkeypatch):
    folder, data, _ = existing
    legacy = {"file": "legacy.etc1s.ktx2", "bytes": 12, "md5": "a" * 32}
    data["flipbooks"]["selected"]["ktx2"] = {"etc1s": legacy, "custom": "giữ"}
    manifest = folder / "manifest.json"
    manifest.write_text(json.dumps(data))

    def encode(png, output, *args):
        current = json.loads(manifest.read_text())
        current["note"] = "Một tác nhân khác vừa cập nhật"
        manifest.write_text(json.dumps(current))
        return _fake_encode(png, output)

    monkeypatch.setattr(ktx2, "encode", encode)
    assert main(["ktx2", str(folder), "--only", "selected"]) == 0
    updated = json.loads(manifest.read_text())
    group = updated["flipbooks"]["selected"].pop("ktx2")
    assert group["etc1s"] == legacy and group["custom"] == "giữ"
    expected = copy.deepcopy(data)
    expected["flipbooks"]["selected"].pop("ktx2")
    expected["note"] = "Một tác nhân khác vừa cập nhật"
    assert updated == expected


@pytest.mark.parametrize("change", ["png", "entry"])
def test_source_or_selected_entry_change_during_encode_stops_publish(existing, monkeypatch, change):
    folder, data, _ = existing
    manifest = folder / "manifest.json"

    def encode(png, output, *args):
        if change == "png":
            Image.new("RGBA", (64, 32), "green").save(png)
        else:
            data["flipbooks"]["selected"]["file"] = "other.atlas.png"
            manifest.write_text(json.dumps(data))
        return _fake_encode(png, output)

    monkeypatch.setattr(ktx2, "encode", encode)
    assert main(["ktx2", str(folder), "--only", "selected"]) == 3
    assert not list(folder.glob("*.ktx2"))
    assert "ktx2" not in json.loads(manifest.read_text())["flipbooks"]["selected"]


def test_atomic_manifest_failure_keeps_manifest_and_removes_temporary(existing, monkeypatch):
    folder, _, _ = existing
    manifest = folder / "manifest.json"
    before = manifest.read_bytes()
    monkeypatch.setattr(ktx2, "encode", _fake_encode)
    replace = atlas_ktx2.os.replace

    def fail_manifest(source, target):
        if target == manifest:
            raise OSError("không ghi được manifest")
        return replace(source, target)

    monkeypatch.setattr(atlas_ktx2.os, "replace", fail_manifest)
    assert main(["ktx2", str(folder), "--only", "selected"]) == 3
    assert manifest.read_bytes() == before
    assert not list(folder.glob(".*.tmp"))
