"""Synthetic, offline checks for fixed-rate hybrid flipbooks and both KTX2 codecs."""
from __future__ import annotations

import importlib.util
import json
import shutil
import struct
from pathlib import Path

import numpy as np
import pytest
from PIL import Image

from vfxflip import grade, ktx2, media, motion, pipeline, timing, upgrade
from vfxflip.__main__ import main

HAS_CV2 = importlib.util.find_spec("cv2") is not None
HAS_KTX2 = bool(shutil.which("node") and (pipeline.TOOL_DIR / "ktx2/node_modules/ktx2-encoder").is_dir())
cv2_required = pytest.mark.skipif(not HAS_CV2, reason="cần OpenCV cục bộ")
ktx2_required = pytest.mark.skipif(not HAS_KTX2, reason="cần node và ktx2-encoder cục bộ")


@pytest.mark.parametrize("limit,count,end,capped", [(64, 61, 121, False), (30, 30, 60, True)])
def test_fixed_rate(limit, count, end, capped):
    plan = {"start": 0, "end": 121, "capped": False, "faded": True, "startMode": "rise"}
    result = timing.fixed_rate(plan, 2, limit)
    assert result["frames"] == count
    assert result["indices"][-1] == (120 if limit == 64 else 58)
    assert result["end"] == end and result["capped"] is capped
    assert result["faded"] is (not capped)
    assert result["step"] == 2.0 and result["startMode"] == "rise"
    assert plan["end"] == 121  # input is not mutated


def test_fixed_rate_preserves_existing_cap():
    result = timing.fixed_rate({"start": 4, "end": 24, "capped": True, "faded": False}, 2, 64)
    assert result["capped"] is True and result["faded"] is False


def test_vector_quantisation():
    strength = 0.08
    original = np.array([0, strength, -strength, 0.021, -0.027], np.float32)
    encoded = motion.encode(original, strength)
    assert encoded[:3].tolist() == [128, 255, 1]
    assert np.max(np.abs(motion.decode(encoded, strength) - original)) <= strength / 127


def test_sqrt_luma_alpha():
    assert motion.luma8(np.array([[[64, 16, 32], [255, 0, 0]]], np.uint8)).tolist() == [[128, 255]]
    assert motion.luma8(np.array([[[255, 1, 2, 0], [255, 0, 0, 64]]], np.uint8)).tolist() == [[0, 128]]


def diagonal(t: float) -> np.ndarray:
    yy, xx = np.mgrid[:72, :128].astype(np.float32)
    g = np.exp(-((xx - (42 + 3 * t)) ** 2 + (yy - (28 + 2 * t)) ** 2) / (2 * 5 ** 2))
    return np.round(g[..., None] * np.array([180, 210, 255])).astype(np.uint8)


@cv2_required
def test_diagonal_flow_and_midpoint():
    cells = np.stack([diagonal(i) for i in range(3)])
    result = motion.flow(cells, False)
    mask = motion.luma8(cells[0]) > 100
    actual = np.median(result["uv"][0][mask], axis=0)
    assert actual == pytest.approx([3 / 128, -2 / 72], rel=0.25)
    assert result["checks"]["warpRatio"] < 0.5
    d = motion.decode(result["encoded"][0], result["strength"]) * [128, -72]
    a, b, truth = cells[0] / 255, cells[1] / 255, diagonal(0.5) / 255
    warped = motion.warp_blend(a, b, d, 0.5)
    assert np.abs(warped - truth).mean() < 0.7 * np.abs((a + b) / 2 - truth).mean()
    assert np.all(result["encoded"][-1] == 128)
    assert motion.warp_blend(a, b, d, 0) == pytest.approx(a)
    assert motion.warp_blend(a, b, d, 1) == pytest.approx(b)


@cv2_required
def test_loop_and_vector_atlas_padding(tmp_path):
    cells = np.stack([diagonal(i) for i in range(3)])
    result = motion.flow(cells, True)
    assert np.abs(result["uv"][-1]).max() > 0
    path = tmp_path / "mv.png"
    motion.write_atlas(result["encoded"], 2, 2, path)
    with Image.open(path) as image:
        data = np.asarray(image)
        assert image.size == (256, 144)
    assert np.all(data[72:, 128:] == 128)
    assert np.array_equal(data[..., 0], data[..., 1])
    assert np.array_equal(data[..., 0], data[..., 2])
    assert motion.cells_from_atlas(path, 2, 2, 128, 72, 3).shape == (3, 72, 128, 4)


@ktx2_required
@pytest.mark.parametrize("codec,compression", [("uastc", 2), ("etc1s", 1)])
@pytest.mark.parametrize("transfer,code", [("srgb", 2), ("linear", 1)])
def test_ktx2_headers(tmp_path, codec, compression, transfer, code):
    yy, xx = np.mgrid[:32, :64]
    data = np.stack([xx * 4, yy * 8, (xx + yy) * 2, 128 + yy * 3], -1).astype(np.uint8)
    png, dest = tmp_path / "source.png", tmp_path / "encoded.ktx2"
    Image.fromarray(data).save(png)
    info = ktx2.encode(png, dest, codec, transfer)
    raw = dest.read_bytes()
    assert raw[:12] == bytes.fromhex("AB 4B 54 58 20 32 30 BB 0D 0A 1A 0A")
    assert struct.unpack_from("<II", raw, 20) == (64, 32)
    assert info["levels"] >= 2 and info["transfer"] == code
    assert info["supercompression"] == compression
    assert info["bytes"] == len(raw) and info["encodeMs"] > 0
    assert not list(tmp_path.glob(".*.tmp")) and not list(tmp_path.glob(".*.rgba"))


@pytest.mark.parametrize("look", ["neutral", "cool"])
def test_look_preserves_or_cools_blue_tail(lab, look):
    yy, xx = np.mgrid[:72, :128]
    g = np.exp(-((xx - 64) ** 2 + (yy - 36) ** 2) / 100)
    frames = np.repeat((g[..., None] * [0.18, 0.38, 0.8])[None], 48, axis=0)
    clip = lab.add_clip("blue", frames)
    params = dict(pipeline.DEFAULTS, known=True, cell=[128, 72], frames=24, fps=12,
                  look=look, flash=False, start=0, end=48, whiteFix="off", greyCut=0)
    work = lab.home / look
    pipeline.process(clip, work, lab.game, "blue", "v1", params)
    cells = motion.cells_from_atlas(work / "blue__v1.atlas.png", 4, 8, 128, 72, 24)
    ratios = [f[..., 2].sum() / max(f[..., 0].sum(), 1) for f in (cells[0], cells[-3])]
    delta = abs(ratios[1] / ratios[0] - 1)
    assert delta < 0.05 if look == "neutral" else delta > 0.05
    rgba = np.array([[[0.2, 0.4, 0.8, 0.6]]], np.float32)
    faded = grade.neutral_fade(rgba, 0.5)
    assert faded[..., :3] == pytest.approx(rgba[..., :3])
    assert faded[..., 3] == pytest.approx(rgba[..., 3] * 0.5)


@pytest.fixture
def upgrade_source(lab):
    yy, xx = np.mgrid[:108, :192]
    frames = np.stack([np.exp(-((xx - (70 + 0.6 * i)) ** 2 + (yy - 52) ** 2) / 150)[..., None]
                       * [0.18, 0.4, 0.8] for i in range(48)])
    source = lab.add_clip("blue", frames)
    lab.write_table({"blue": {"flash": False, "start": 0, "end": 48, "whiteFix": "off", "greyCut": 0}})
    folder = lab.home / "like" / "water"
    folder.mkdir(parents=True)
    entry = {"job": "blue", "source": str(source.relative_to(lab.home)), "role": "beast", "roles": ["beast"],
             "take": 1, "mode": "fire", "alpha": False, "code": "C1", "name": "Synthetic blue", "design": "test",
             "elements": "Water", "use": "Test", "layer": "rim", "modesAllowed": ["additive"], "tint": False,
             "alphaKind": "none", "premultiplied": False, "dir": {"vec": [1, 0]},
             "head": {"uv": [0.5, 0.5], "cellUv": [0.1, 0.1]}, "loop": False, "sourceFps": 24,
             "trim": {"start": 4, "end": 44, "step": 2, "startMode": "rise"},
             "timing": {"peak": 2, "holdEnd": 10},
             "video": {"peakTime": 0.167, "pivot": [0.5, 0.6], "file": "old.mp4"}}
    manifest = folder / "manifest.json"
    manifest.write_text(json.dumps({"flipbooks": {"blue-id": entry}}))
    return lab, manifest, entry


@cv2_required
@ktx2_required
def test_upgrade_end_to_end(upgrade_source, tmp_path):
    lab, manifest, like = upgrade_source
    original_text = manifest.read_text()
    out = tmp_path / "hybrid"
    out.mkdir()
    other = {"file": "unrelated.png", "nested": {"keep": [1, "nguyên vẹn"]}}
    (out / "manifest.json").write_text(json.dumps({"version": 1, "custom": "giữ", "flipbooks": {"other": other}}))
    entry = upgrade.run(f"{manifest}:blue-id", out, [128, 72], 12, home=lab.home, table_dir=lab.table_dir,
                        repo_root=lab.home, game=lab.game, videos="crf23")
    for name in ("blue-id.atlas.png", "blue-id.json", "blue-id.mv.png", "blue-id.uastc.ktx2", "blue-id.etc1s.ktx2",
                 "blue-id.mv.uastc.ktx2", "blue-id.mv.etc1s.ktx2", "blue-id.crf23.mp4"):
        assert (out / name).is_file()
    result = json.loads((out / "manifest.json").read_text())
    assert result["flipbooks"]["other"] == other and result["custom"] == "giữ"
    assert result["flipbooks"]["blue-id"] == entry
    assert manifest.read_text() == original_text
    assert "video" not in entry
    assert entry["fps"] == 12 and entry["frames"] == 24 and not entry["loop"]
    assert entry["trim"]["step"] == 2
    assert entry["cols"] * entry["cell"][0] == entry["width"]
    assert entry["rows"] * entry["cell"][1] == entry["height"]
    assert entry["compareWith"] == {"folder": "water", "id": "blue-id"}
    assert entry["upgrade"]["look"] == "neutral"
    assert entry["sourceRect"]["frame"] == [192, 108]
    x, y, w, h = entry["sourceRect"]["crop"]
    assert entry["head"]["cellUv"] == [round((96 - x) / w, 4), round((54 - y) / h, 4)]
    assert entry["head"]["uv"] == like["head"]["uv"]
    for key in upgrade.COPY_FIELDS:
        if key != "head":
            assert entry[key] == like[key]
    assert entry["md5"] == upgrade.md5(out / entry["file"])
    assert entry["bytes"] == (out / entry["file"]).stat().st_size
    mv = entry["motion"]
    assert mv["layout"] == "x-rgb-y-a" and mv["zero"] == 128 and mv["scale"] == 127
    assert mv["strength"] >= 1e-4 and mv["checks"]["warpRatio"] >= 0
    assert mv["md5"] == upgrade.md5(out / mv["file"])
    with Image.open(out / mv["file"]) as image:
        assert image.size == (entry["width"], entry["height"])
    for group, transfer in ((entry["ktx2"], "srgb"), (mv["ktx2"], "linear")):
        assert group["yFlip"] is True and group["mipmaps"] is True and group["transfer"] == transfer
        for codec in ("uastc", "etc1s"):
            item = group[codec]
            assert item["md5"] == upgrade.md5(out / item["file"])
            assert item["bytes"] == (out / item["file"]).stat().st_size and item["encodeS"] > 0
    meta = json.loads((out / entry["json"]).read_text())
    assert meta["source"]["crop"] == entry["sourceRect"]["crop"] and meta["upgrade"] == entry["upgrade"]
    assert meta["image"] == entry["file"] and meta["id"] == "blue-id"
    en = json.loads((lab.home / "out" / lab.game / "upgrade" / "blue-id" / "blue__v1.metrics.json").read_text())["energy"]
    sm = [np.mean(en[max(0, i - 1):i + 2]) for i in range(len(en))]
    peak = int(np.argmax(sm))
    assert entry["timing"]["peak"] == peak
    assert entry["timing"]["holdEnd"] == max(i for i, v in enumerate(sm) if v >= 0.6 * sm[peak])
    video = entry["videoVariants"]["crf23"]
    assert video["frames"] == 40 and video["fps"] == 24 and video["crf"] == 23
    assert (video["w"], video["h"]) == (192, 108) and video["ssim"] > 0.8
    assert video["peakTime"] == like["video"]["peakTime"] and video["pivot"] == like["video"]["pivot"]
    assert video["start"] == 0.0 and video["bytes"] == (out / video["file"]).stat().st_size


def test_reject_six_fps_without_mv(tmp_path, capsys):
    result = main(["upgrade", "--like", "missing.json:id", "--out", str(tmp_path / "out"),
                   "--cell", "128x72", "--fps", "6", "--no-mv"])
    assert result == 3 and "vector" in capsys.readouterr().err
    assert not (tmp_path / "out").exists()


def test_reject_large_atlas_without_output(upgrade_source, tmp_path):
    lab, manifest, _ = upgrade_source
    out = tmp_path / "hybrid"
    with pytest.raises(media.MediaError, match="max-atlas 256"):
        upgrade.run(f"{manifest}:blue-id", out, [128, 72], 12, max_atlas=256,
                    home=lab.home, table_dir=lab.table_dir, repo_root=lab.home, game=lab.game)
    assert not out.exists()


@pytest.mark.parametrize("overrides,match", [({"look": "wrong"}, "look"), ({"fps": 10}, "chia hết"),
                                            ({"fps": 48}, "chia hết")])
def test_pipeline_parameter_errors(upgrade_source, tmp_path, overrides, match):
    lab, _, entry = upgrade_source
    params = dict(pipeline.DEFAULTS, known=True, **overrides)
    with pytest.raises(media.MediaError, match=match):
        pipeline.process(lab.home / entry["source"], tmp_path / "bad", lab.game, "blue", "v1", params)
    assert not (tmp_path / "bad").exists()
