"""Unit checks of the colour curves, timing helpers and layout helpers (no video)."""
import numpy as np

from vfxflip import atlas, grade, layout, metrics, pipeline, timing


def test_crush_black_zero_below_threshold_and_keeps_hue():
    rgb = np.array([[[0.02, 0.01, 0.0], [0.6, 0.3, 0.1], [1.0, 1.0, 1.0], [0.028, 0.02, 0.01]]], np.float32)
    out = grade.crush_black(rgb, t0=0.03, k=0.05)
    assert np.all(out[0, 0] == 0) and np.all(out[0, 3] == 0)   # noise -> exactly 0
    assert np.allclose(out[0, 2], 1.0)                           # white stays white
    r = out[0, 1] / out[0, 1, 0]
    assert np.allclose(r, rgb[0, 1] / rgb[0, 1, 0], atol=1e-5)   # hue kept: one factor per pixel
    xs = np.linspace(0, 1, 2001, dtype=np.float32)
    ys = grade.crush_black(np.stack([xs, xs * 0.5, xs * 0.2], -1)[None], 0.03, 0.05)[0, :, 0]
    assert np.all(np.diff(ys) >= -1e-6) and np.max(np.abs(np.diff(ys))) < 0.01  # monotonic, no jump


def test_grey_cut_drops_charcoal_smoke_but_keeps_deep_red():
    img = np.zeros((32, 64, 3), np.float32)
    img[:, :32] = (0.15, 0.15, 0.16)   # charcoal smoke on black
    img[:, 32:] = (0.15, 0.03, 0.01)   # deep red flame edge, same brightness
    out = grade.crush_black(img, 0.02, grey_cut=0.22)
    assert out[16, 8].max() < 0.01
    assert out[16, 56, 0] > 0.08


def test_shoulder_lowers_white_core_without_shifting_hue():
    yy, xx = np.mgrid[0:64, 0:64]
    d = np.hypot(xx - 32, yy - 32) / 30.0
    i = np.clip(1.3 - d, 0, 1)
    rgb = np.stack([np.minimum(1, i * 1.2), np.minimum(1, i * 1.0), np.minimum(1, i * 0.9)], -1).astype(np.float32)
    before = grade.white_core_ratio(rgb)[0]
    after = grade.white_core_ratio(grade.shoulder(rgb, 0.86))[0]
    assert after < before
    xs = np.linspace(0, 1, 1001, dtype=np.float32)
    ys = grade.shoulder(np.stack([xs, xs, xs], -1)[None], 0.82, knee_at=0.55)[0, :, 0]
    assert np.all(np.diff(ys) >= -1e-6) and abs(ys[-1] - 0.82) < 1e-4


def test_warm_core_shrinks_white_and_keeps_peak():
    yy, xx = np.mgrid[0:96, 0:96]
    d = np.hypot(xx - 48, yy - 48) / 40.0
    i = np.clip(1.5 - d, 0, 1)
    rgb = np.stack([np.minimum(1, i * 1.3), np.minimum(1, i * 1.05), np.minimum(1, i * 0.95)], -1).astype(np.float32)
    assert grade.white_core_ratio(rgb)[0] > 0.4
    out = grade.warm_core(rgb, 0.28)
    assert grade.white_core_ratio(out)[0] <= 0.30
    assert np.allclose(out.max(-1), rgb.max(-1), atol=1e-6)     # brightest channel untouched
    assert (out[48, 48] > 0.85).all()                           # a white centre remains


def test_luma_matte_reproduces_the_source_over_white_and_keeps_shading():
    h, w = 48, 48
    a = np.clip(1.2 - np.hypot(*np.mgrid[-24:24, -24:24]) / 16.0, 0, 0.95).astype(np.float32)
    lc = float(grade.SMOKE_DENSE @ grade.LUMA)
    white = 0.96
    shade = 1.0 + 0.8 * (np.sin(np.arange(w) / 3.0)[None, :] > 0)   # lit and shadowed billows
    lum = np.clip(white * (1 - a) + lc * shade * a, 0, 1)
    rgb = np.repeat(lum[..., None], 3, -1)
    out = grade.luma_matte(rgb, np.full((h, w), white, np.float32))
    over_white = white * (1 - out[..., 3]) + grade.luma(out) * out[..., 3]
    assert np.abs(over_white - lum).max() < 0.03                 # exact over its own white plate
    assert out[..., 3].max() == 1.0 and out[..., 3][0, 0] == 0.0
    dense = out[..., 3] >= 1.0
    assert np.ptp(grade.luma(out)[dense]) > 0.05                 # dense smoke keeps light and shade
    assert out[..., :3].max() < 0.65                             # charcoal everywhere: no white fringe


def test_cool_dim_turns_dim_yellow_orange():
    dim_yellow = np.array([[[0.5, 0.4, 0.15]]], np.float32)
    out = grade.cool_dim(dim_yellow, 0.8)
    h = metrics.hsv(out[0, 0])[0]
    assert h < 38 and not metrics.mustard_mask(out)[0, 0]
    bright = np.array([[[1.0, 0.8, 0.3]]], np.float32)
    assert np.allclose(grade.cool_dim(bright, 0.8), bright, atol=1e-3)


def test_even_indices():
    idx, step = timing.even_indices(10, 70, 200)
    assert step == 2 and len(idx) == 30 and idx[0] == 10 and idx[-1] == 68
    idx, step = timing.even_indices(0, 72, 200, may_trim=True)
    assert step == 2 and len(idx) == 32
    idx, step = timing.even_indices(0, 20, 200)
    assert len(idx) == 24 and step == 1                    # short cuts are padded to 24 frames


def test_crossfade_endpoints_are_real_frames():
    f = np.arange(12, dtype=np.float32)[:, None] * np.ones((1, 4), np.float32)
    out = timing.crossfade_loop(f, 8, 4)
    assert len(out) == 8
    assert np.allclose(out[0], f[8]) and np.allclose(out[3], f[3]) and np.allclose(out[7], f[7])


def test_flash_peak_needs_a_dip():
    grow = np.linspace(0, 1, 60)
    assert timing.find_flash_peak(grow, 0) is None
    flash = np.concatenate([np.linspace(0, 1, 10), np.linspace(1, 0.5, 20), np.linspace(0.5, 0.9, 30)])
    assert timing.find_flash_peak(flash, 0) in (8, 9, 10)


def test_strip_tile_wraps_seamlessly():
    rng = np.random.default_rng(1)
    x = np.cumsum(rng.normal(size=(1, 8, 300, 3)), axis=2).astype(np.float32)
    x = (x - x.min()) / (x.max() - x.min())
    out = pipeline._strip_tile(x, 256)
    assert out.shape[2] == 256
    raw = metrics.tile_seam(x[:, :, :256])          # cutting without the blend: a hard wrap
    assert metrics.tile_seam(out) < 0.2 * raw and metrics.tile_seam(out) < 1.25
    assert np.allclose(out[:, :, 0], x[:, :, 256]) and np.allclose(out[:, :, 255], x[:, :, 255])


def test_atlas_grid_is_power_of_two():
    for n, cw, ch in ((32, 256, 256), (24, 256, 256), (16, 1024, 256), (32, 256, 128), (32, 512, 512)):
        c, r = atlas.grid(n, cw, ch)
        assert c * r >= n
        for v in (c * cw, r * ch):
            assert v & (v - 1) == 0
    assert atlas.grid(32, 256, 256) == (8, 4)
    assert atlas.grid(32, 256, 128) == (4, 8)


def test_principal_axis_sign():
    img = np.zeros((100, 200), np.float32)
    for i in range(120):                       # streak rising to the right (y down)
        img[80 - i // 2, 40 + i] = 1.0
    ang, elong = layout.principal_axis(img)
    assert -30 < ang < -22 and elong > 3


def test_coverage_matte_widens_and_holds_over_neighbour_frames():
    """Fire on black -> coverage: opaque from opaque_at luma, 0 on black, widened 2-3 px, max over +-1 frame."""
    from vfxflip import grade
    h = w = 64
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    frames = np.zeros((3, h, w, 3), np.float32)
    frames[1][np.hypot(xx - 32, yy - 32) <= 10] = (0.8, 0.4, 0.1)   # a disc in the middle frame only
    cov = np.stack([grade.coverage_matte(f, opaque_at=0.25) for f in frames])
    assert cov[1, 32, 32] == 1.0 and cov[1, 2, 2] == 0.0 and cov[0].max() == 0.0
    wide = grade.widen_coverage(cov, 2.5, 1)
    row = wide[1, 32]
    grown = int((row > 0.5).sum()) - int((cov[1, 32] > 0.5).sum())
    assert 4 <= grown <= 6, grown                                    # about 2.5 px on each side
    assert wide[0, 32, 32] == 1.0 and wide[2, 32, 32] == 1.0         # held over the neighbouring frames


def test_decontaminate_takes_the_backdrop_out_of_soft_edges():
    h = w = 64
    d = np.hypot(*np.mgrid[-32:32, -32:32]).astype(np.float32)
    a = np.clip((20 - d) / 8.0, 0, 1).astype(np.float32)
    fg = np.array([0.95, 0.5, 0.1], np.float32)
    bg = np.array([0.3, 0.12, 0.0], np.float32)
    rgb = (a[..., None] * fg + (1 - a[..., None]) * bg).astype(np.float32)
    out = grade.matte_video_rgba(rgb, a, t0=0.02)
    soft = (out[..., 3] > 0.1) & (out[..., 3] < 0.9)
    assert np.abs(out[..., :3][soft] - fg).max() < 0.03            # straight colour = the effect's, not the mix
    assert np.abs(out[0, 0, :3] - fg).max() < 0.03                 # clear area carries the edge colour, not black
    assert out[0, 0, 3] == 0.0 and out[32, 32, 3] == 1.0
    over = out[..., :3] * out[..., 3:4] + (1 - out[..., 3:4]) * bg
    assert np.abs(over - rgb).max() < 0.04                         # over its own backdrop it is the source again


def test_oneshot_gap_end_stops_before_a_repeat():
    e = np.zeros(80)
    e[5:25] = np.linspace(1, 10, 20)
    e[25:30] = [8, 6, 4, 2, 1]
    e[50:70] = 5.0                                                  # the burst plays again later
    old = timing.plan_oneshot(e, e, 24.0, flash=False, max_sec=3.0, start_frac=0.05)
    assert old["end"] > 50
    new = timing.plan_oneshot(e, e, 24.0, flash=False, max_sec=3.0, start_frac=0.05, gap_end=6)
    assert new["faded"] and new["end"] == 30 and max(new["indices"]) < 30
