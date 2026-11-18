import numpy as np

from build import dsp, measure

SR = 48000


def _peak_hz(x):
    x = dsp.as2d(x)[:, 0]
    spec = np.abs(np.fft.rfft(x * np.hanning(x.size)))
    return np.argmax(spec) * SR / x.size


def test_pitch_modes():
    t = np.arange(SR // 2) / SR
    x = np.sin(2 * np.pi * 440 * t)
    up = dsp.pitch_varispeed(x, 12)
    assert abs(up.shape[0] - x.size / 2) <= 2 and abs(_peak_hz(up) - 880) < 6
    kept = dsp.pitch_preserve(x, 12)
    assert kept.shape[0] == x.size and abs(_peak_hz(kept[2400:-2400]) - 880) < 20


def test_mono_fold_rule():
    t = np.arange(4800) / SR
    s = np.sin(2 * np.pi * 300 * t)
    mid, how = dsp.to_channels(np.stack([s, 0.9 * s], 1), 1)
    assert how == "mid" and mid.shape[1] == 1
    anti, how = dsp.to_channels(np.stack([s, -s * 0.95], 1), 1)   # phase-cancelling: take the stronger channel
    assert how == "channel-0"


def test_filters_shape_spectrum():
    noise = np.random.default_rng(0).standard_normal(SR)
    def band_db(x, lo, hi):
        spec = np.abs(np.fft.rfft(dsp.as2d(x)[:, 0])) ** 2
        f = np.fft.rfftfreq(SR, 1 / SR)
        return 10 * np.log10(spec[(f >= lo) & (f < hi)].mean())
    hp = dsp.apply_filters(noise, [{"type": "highpass", "hz": 1000, "order": 4}])
    assert band_db(hp, 100, 300) < band_db(hp, 3000, 6000) - 30
    cut = dsp.apply_filters(noise, [{"type": "peak", "hz": 300, "gainDb": -12, "q": 1}])
    assert band_db(cut, 280, 320) < band_db(noise, 280, 320) - 9
    shelf = dsp.apply_filters(noise, [{"type": "highshelf", "hz": 4000, "gainDb": 6}])
    assert band_db(shelf, 10000, 14000) - band_db(noise, 10000, 14000) > 5


def test_place_and_fade():
    mix = dsp.place(np.zeros((0, 1)), np.ones(100), 50)
    assert mix.shape[0] == 150 and mix[:50].sum() == 0
    f = dsp.fade(np.ones(480), in_ms=5, out_ms=5)
    assert f[0, 0] == 0 and f[-1, 0] == 0 and f[240, 0] == 1


def test_true_peak_sees_intersample_overs():
    n = np.arange(4800)
    x = np.sin(np.pi / 2 * n + np.pi / 4)    # samples at ±0.707, true peak 1.0
    assert measure.sample_peak_db(x) < -2.9 and measure.true_peak_db(x) > -0.5
