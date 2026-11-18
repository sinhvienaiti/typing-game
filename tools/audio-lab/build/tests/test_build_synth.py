import numpy as np
import pytest

from build import synth


@pytest.mark.parametrize("name", sorted(synth.GENERATORS))
def test_generator_is_seeded_and_normalised(name):
    a = synth.generate(name, {}, 5)
    b = synth.generate(name, {}, 5)
    assert np.array_equal(a, b)
    assert np.all(np.isfinite(a)) and abs(np.max(np.abs(a)) - 1.0) < 1e-9


def test_noise_changes_with_seed():
    assert not np.array_equal(synth.generate("noise_burst", {}, 1), synth.generate("noise_burst", {}, 2))


def test_tone_glide_and_length():
    x = synth.generate("tone", {"wave": "square", "freqHz": 400, "endHz": 100, "glideMs": 100, "durMs": 250}, 0)
    assert len(x) == 12000
    spec_early = np.abs(np.fft.rfft(x[:2400]))
    spec_late = np.abs(np.fft.rfft(x[-4800:] * np.hanning(4800)))
    f_early = np.argmax(spec_early) * 48000 / 2400
    f_late = np.argmax(spec_late) * 48000 / 4800
    assert f_early > 250 and 80 < f_late < 130


def test_unknown_generator():
    with pytest.raises(ValueError):
        synth.generate("nope", {}, 0)
