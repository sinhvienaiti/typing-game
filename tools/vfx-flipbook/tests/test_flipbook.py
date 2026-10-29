"""End-to-end runs on synthetic clips: one-shot trim, loop seam, luma matte, centring, direction."""
import json

import numpy as np
from PIL import Image

from vfxflip import pipeline


def _run(lab, cid):
    reports = pipeline.ingest(lab.game, cid, "v1", home=lab.home, table_dir=lab.table_dir)
    out = lab.home / "out" / lab.game / cid
    meta = json.loads((out / f"{cid}__v1.json").read_text())
    atlas = np.asarray(Image.open(out / meta["image"])).astype(np.float32) / 255
    for ext in ("atlas.png", "json", "sheet.jpg", "preview.mp4", "metrics.json"):
        assert (out / f"{cid}__v1.{ext}").is_file(), ext
    return reports[0], meta, atlas


def _cells(meta, atlas):
    cw, ch = meta["cell"]
    return np.stack([atlas[(i // meta["cols"]) * ch:(i // meta["cols"] + 1) * ch,
                           (i % meta["cols"]) * cw:(i % meta["cols"] + 1) * cw] for i in range(meta["frames"])])


def test_oneshot_drops_black_starts_on_flash_and_ends_after_fade(lab):
    blob, fire, add_clip, write_table = lab.blob, lab.fire, lab.add_clip, lab.write_table
    h, w, n = 216, 384, 84
    frames = np.zeros((n, h, w, 3), np.float32)
    for t in range(6, 12):                               # a small seed before the burst
        frames[t] = fire(0.6 * blob(h, w, 192, 108, 4))
    frames[12] = fire(blob(h, w, 192, 108, 40))          # one-frame flash
    for t in range(13, 56):                              # then the fireball grows and cools away
        k = (t - 13) / 43
        frames[t] = fire(0.75 * (1 - k) ** 1.5 * blob(h, w, 192, 108, 30 + 40 * k))
    add_clip("burst", frames)
    write_table({"burst": {"cell": [128, 128], "greyCut": 0.0, "maxSec": 3.0}})
    rep, meta, atlas = _run(lab, "burst")
    trim = meta["trim"]
    assert trim["droppedBlack"] == 6
    assert trim["startMode"] == "flash" and 11 <= trim["start"] <= 13
    assert rep["plan"]["faded"] and trim["end"] <= 60 and trim["tailFade"] == 0
    assert 24 <= meta["frames"] <= 32
    assert rep["checks"]["firstFramePeak"]["value"] >= 0.95
    assert not rep["flags"], rep["flags"]


def test_loop_window_skips_build_up_and_joins_cleanly(lab):
    blob, fire, add_clip, write_table = lab.blob, lab.fire, lab.add_clip, lab.write_table
    h = w = 192
    n = 110
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    th = np.arctan2(yy - 96, xx - 96)
    d = np.hypot(xx - 96, yy - 96)
    frames = np.zeros((n, h, w, 3), np.float32)
    for t in range(n):
        r = 48 + 6 * np.sin(3 * th + 0.7 * t) + 4 * np.sin(5 * th - 1.13 * t) + 3 * np.sin(2 * th + 0.31 * t)
        ramp = min(1.0, t / 24)                          # a build-up the loop must avoid
        frames[t] = fire(ramp * np.clip((r - d) / 14, 0, 1))
    add_clip("orb", frames)
    write_table({"orb": {"loop": True, "cell": [128, 128], "greyCut": 0.0}})
    rep, meta, atlas = _run(lab, "orb")
    assert meta["loop"] and meta["frames"] == 32
    assert meta["trim"]["start"] >= 22
    assert rep["checks"]["loopSeam"]["ratio"] <= 1.0
    assert rep["checks"]["loopEnergyCV"] < 0.05
    assert not rep["flags"], rep["flags"]


def test_luma_matte_smoke_on_white(lab):
    blob, fire, add_clip, write_table = lab.blob, lab.fire, lab.add_clip, lab.write_table
    h = w = 256
    n = 72
    frames = np.ones((n, h, w, 3), np.float32) * 0.96
    lc = 0.13
    for t in range(8, n):
        a = 0.9 * blob(h, w, 128, 150 - t * 0.4, 25 + t * 0.5, soft=0.8) * min(1.0, (t - 7) / 6)
        lum = 0.96 * (1 - a) + lc * a
        frames[t] = lum[..., None]
    add_clip("smoke", frames)
    write_table({"smoke": {"blend": "normal", "background": "white", "flash": False, "greyCut": 0.0,
                           "cell": [128, 128], "maxSec": 4.0}})
    rep, meta, atlas = _run(lab, "smoke")
    assert meta["channels"] == "rgba" and atlas.shape[-1] == 4
    cells = _cells(meta, atlas)
    alpha = cells[..., 3]
    assert alpha[len(cells) // 2].max() >= 0.95             # dense smoke stays dense
    assert alpha[:, :3, :3].max() < 0.02                    # background is clear
    assert cells[..., :3].max() < 0.65                      # charcoal RGB everywhere: no white fringe
    assert not rep["flags"], rep["flags"]


def test_centring_on_the_mass_with_a_margin(lab):
    blob, fire, add_clip, write_table = lab.blob, lab.fire, lab.add_clip, lab.write_table
    h, w, n = 360, 640, 60
    frames = np.zeros((n, h, w, 3), np.float32)
    for t in range(4, 44):
        k = (t - 4) / 40
        frames[t] = fire((1 - k) * blob(h, w, 470, 140, 30 + 30 * k))
    add_clip("offset", frames)
    write_table({"offset": {"cell": [128, 128], "greyCut": 0.0}})
    rep, meta, atlas = _run(lab, "offset")
    px, py = meta["pivot"]
    assert abs(px - 0.5) < 0.06 and abs(py - 0.5) < 0.06
    cells = _cells(meta, atlas)
    acc = cells[..., :3].max(-1).sum(0)
    yy, xx = np.mgrid[0:128, 0:128]
    cx, cy = (acc * xx).sum() / acc.sum() / 128, (acc * yy).sum() / acc.sum() / 128
    assert abs(cx - 0.5) < 0.05 and abs(cy - 0.5) < 0.05
    assert max(rep["checks"]["cellEdge"]["max"].values()) < 0.04


def test_directional_clip_is_turned_level_and_pivots_on_the_flash(lab):
    blob, fire, add_clip, write_table = lab.blob, lab.fire, lab.add_clip, lab.write_table
    h, w, n = 360, 640, 60
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    ang = np.radians(-30)                                  # rises to the right, like muzzle-flash v4/v5
    ux, uy = np.cos(ang), np.sin(ang)
    ox, oy = 160, 280
    along = (xx - ox) * ux + (yy - oy) * uy
    across = np.abs(-(xx - ox) * uy + (yy - oy) * ux)
    frames = np.zeros((n, h, w, 3), np.float32)
    for t in range(3, n):
        length = min(330, 40 + 12 * t)
        jet = np.clip((14 - across) / 6, 0, 1) * np.clip(1 - along / length, 0, 1) * (along > 0)
        frames[t] = fire(np.maximum(0.8 * jet, blob(h, w, ox, oy, 22)))
    add_clip("jet", frames)
    write_table({"jet": {"cell": [256, 128], "layout": "left-pivot", "axis": "horizontal",
                         "coreSide": "left", "greyCut": 0.0, "maxSec": 1.5}})
    rep, meta, atlas = _run(lab, "jet")
    assert abs(abs(meta["source"]["rotate"]) - 30) < 4
    assert abs(rep["checks"]["axis"]["degrees"]) < 8
    assert meta["pivot"][0] < 0.3                           # the flash sits at the left end
    assert not meta["source"]["flipX"]


def test_wrong_way_projectile_is_mirrored(lab):
    blob, fire, add_clip, write_table = lab.blob, lab.fire, lab.add_clip, lab.write_table
    h = w = 256
    n = 80
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    frames = np.zeros((n, h, w, 3), np.float32)
    for t in range(n):                                     # head on the left, tail trailing right
        tail = np.clip(1 - (xx - 90) / 120, 0, 1) * (xx > 90) * np.clip((18 - np.abs(yy - 128)) / 8, 0, 1)
        flick = 0.85 + 0.1 * np.sin(0.9 * t + xx / 9.0)
        frames[t] = fire(np.maximum(blob(h, w, 90, 128, 26), 0.6 * tail * flick))
    add_clip("head", frames)
    write_table({"head": {"loop": True, "cell": [128, 128], "axis": "horizontal", "coreSide": "right",
                          "greyCut": 0.0}})
    rep, meta, atlas = _run(lab, "head")
    assert meta["source"]["flipX"] is True
    assert meta["pivot"][0] > 0.5                            # the hot head now leads on the right
