"""Audio I/O and DSP helpers. libsndfile only (WAV, FLAC, OGG Vorbis, MP3): no ffmpeg."""
from __future__ import annotations

import hashlib
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy import signal

EPS = 1e-12
AUDIO_EXTS = {".wav", ".wave", ".flac", ".ogg", ".oga", ".mp3", ".aif", ".aiff"}


def db(x):
    return 20.0 * np.log10(np.maximum(np.abs(x), EPS))


def pdb(p):
    return 10.0 * np.log10(np.maximum(p, EPS))


def fnum(v, nd=2):
    """Round for JSON; None for nan/inf."""
    if v is None:
        return None
    v = float(v)
    return round(v, nd) if np.isfinite(v) else None


@dataclass
class Audio:
    path: Path
    data: np.ndarray        # (frames, channels) float64, values exactly as stored (raw)
    sr: int
    fmt: str
    subtype: str
    sha256: str
    nbytes: int

    @property
    def channels(self) -> int:
        return int(self.data.shape[1])

    @property
    def frames(self) -> int:
        return int(self.data.shape[0])

    @property
    def duration(self) -> float:
        return self.frames / self.sr

    @property
    def mono(self) -> np.ndarray:
        return self.data.mean(axis=1)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


class LoadError(Exception):
    """A file the critic cannot score. `code` becomes the blocking L1 check id."""

    LABELS = {"unreadable": "Không đọc được file", "empty": "File rỗng",
              "not_finite": "Có mẫu không hữu hạn (NaN, Inf)"}

    def __init__(self, code: str, msg_vi: str, audio: "Audio | None" = None):
        super().__init__(msg_vi)
        self.code, self.msg_vi, self.audio = code, msg_vi, audio

    @property
    def label_vi(self) -> str:
        return self.LABELS.get(self.code, self.code)


def load(path: str | Path) -> Audio:
    p = Path(path)
    info = sf.info(str(p))
    data, sr = sf.read(str(p), always_2d=True, dtype="float64")
    return Audio(p, data, int(sr), info.format, info.subtype, sha256(p), p.stat().st_size)


def load_checked(path: str | Path) -> Audio:
    """load() plus the checks every later stage relies on; raises LoadError with a Vietnamese reason."""
    p = Path(path)
    try:
        size = p.stat().st_size
    except OSError as e:
        raise LoadError("unreadable", f"không mở được file: {e.strerror or e}") from e
    if size == 0:
        raise LoadError("empty", "file 0 byte")
    try:
        a = load(p)
    except Exception as e:  # noqa: BLE001 - libsndfile raises several types (LibsndfileError, RuntimeError...)
        raise LoadError("unreadable", f"libsndfile không đọc được ({type(e).__name__}: {str(e)[:160]})") from e
    if a.frames == 0 or a.channels == 0:
        raise LoadError("empty", "file không có mẫu nào (0 khung)", a)
    bad = int(np.size(a.data) - np.count_nonzero(np.isfinite(a.data)))
    if bad:
        raise LoadError("not_finite", f"{bad} mẫu là NaN hoặc Inf", a)
    return a


def from_array(x: np.ndarray, sr: int, name: str = "array") -> Audio:
    x = np.asarray(x, dtype=np.float64)
    if x.ndim == 1:
        x = x[:, None]
    return Audio(Path(name), x, int(sr), "ARRAY", "FLOAT", "", 0)


def collect(paths: list[str]) -> list[Path]:
    out: list[Path] = []
    for p in map(Path, paths):
        if p.is_dir():
            out += sorted(f for f in p.rglob("*") if f.suffix.lower() in AUDIO_EXTS and not f.name.startswith("."))
        elif p.is_file():
            out.append(p)
        else:
            raise FileNotFoundError(f"không thấy {p}")
    seen, uniq = set(), []
    for f in out:
        r = f.resolve()
        if r not in seen:
            seen.add(r)
            uniq.append(f)
    return uniq


# ---------------------------------------------------------------- filters
@lru_cache(maxsize=256)
def _sos(sr: int, lo: float | None, hi: float | None, order: int = 4):
    nyq = sr / 2
    if lo and hi and hi < nyq * 0.999:
        return signal.butter(order, [lo, hi], btype="band", fs=sr, output="sos")
    if lo:
        return signal.butter(order, min(lo, nyq * 0.99), btype="high", fs=sr, output="sos")
    return signal.butter(order, min(hi, nyq * 0.99), btype="low", fs=sr, output="sos")


def band(x: np.ndarray, sr: int, lo: float | None, hi: float | None, zero_phase: bool = True) -> np.ndarray:
    """Butterworth band/high/low pass. `lo`/`hi` None = open side."""
    if lo and lo >= sr / 2:
        return np.zeros_like(x)
    sos = _sos(sr, lo, hi)
    if zero_phase:
        # Silence on both sides instead of odd reflection: no start-up transient at an abrupt start.
        n = int(0.25 * sr)
        widths = [(n, n)] + [(0, 0)] * (x.ndim - 1)
        y = signal.sosfiltfilt(sos, np.pad(x, widths), axis=0, padtype=None)
        return y[n: n + x.shape[0]]
    return signal.sosfilt(sos, x, axis=0)


# ---------------------------------------------------------------- envelopes
def frame_rms(x: np.ndarray, sr: int, frame_ms: float = 1.0, hop_ms: float = 0.5):
    fl = max(1, int(round(sr * frame_ms / 1000)))
    hop = max(1, int(round(sr * hop_ms / 1000)))
    if len(x) < fl:
        x = np.pad(x, (0, fl - len(x)))
    n = 1 + (len(x) - fl) // hop
    c = np.concatenate([[0.0], np.cumsum(x.astype(np.float64) ** 2)])
    starts = np.arange(n) * hop
    rms = np.sqrt(np.maximum((c[starts + fl] - c[starts]) / fl, 0.0))
    t = (starts + fl / 2) / sr
    return t, rms


def rms_db(x: np.ndarray, sr: int, t0: float, t1: float) -> float:
    a, b = int(max(0.0, t0) * sr), int(max(0.0, t1) * sr)
    seg = x[a:b]
    return float(pdb(np.mean(seg ** 2))) if len(seg) else float("-inf")


# ---------------------------------------------------------------- loudness (BS.1770 via pyloudnorm filters)
def k_weighted(data: np.ndarray, sr: int) -> np.ndarray:
    import pyloudnorm as pyln
    meter = pyln.Meter(sr)
    z = data.copy()
    for _, stage in meter._filters.items():   # same K-weighting as integrated_loudness
        for ch in range(z.shape[1]):
            z[:, ch] = stage.apply_filter(z[:, ch])
    return z


def sliding_loudness(data: np.ndarray, sr: int, win_s: float, hop_s: float, z: np.ndarray | None = None):
    """Momentary (0.4 s) / short-term (3 s) / 100 ms loudness curve in LUFS.

    The clip is padded with silence on both sides, so a short sound is measured as if padded to
    the window length (§4.3.3: LUFS-M max after padding to 0.4 s)."""
    z = k_weighted(data, sr) if z is None else z
    # BS.1770 weights for L, R, C, Ls, Rs; channels past the fifth count 1.0 (the standard is silent)
    g = np.array([1.0, 1.0, 1.0, 1.41, 1.41] + [1.0] * max(0, z.shape[1] - 5))[: z.shape[1]]
    win = max(1, int(win_s * sr))
    hop = max(1, int(hop_s * sr))
    pad = np.zeros((win, z.shape[1]))
    zp = np.vstack([pad, z, pad])
    c = np.vstack([np.zeros((1, z.shape[1])), np.cumsum(zp ** 2, axis=0)])
    starts = np.arange(0, zp.shape[0] - win, hop)
    ms = (c[starts + win] - c[starts]) / win
    lufs = -0.691 + 10 * np.log10(np.maximum((ms * g).sum(axis=1), EPS))
    return starts / sr, lufs                 # time = window end in clip time


def integrated(data: np.ndarray, sr: int, block_s: float = 0.4) -> float | None:
    import pyloudnorm as pyln
    n_min = int(block_s * sr) + 1
    x = data if data.shape[0] >= n_min else np.vstack([data, np.zeros((n_min - data.shape[0], data.shape[1]))])
    try:
        v = float(pyln.Meter(sr, block_size=block_s).integrated_loudness(x))
    except Exception:
        return None
    return v if np.isfinite(v) else None


def dc_estimate(data: np.ndarray, sr: int) -> float:
    """True DC offset (§4.3.1 "Lệch DC"), largest over channels, in FS.

    Not the plain mean: a short decaying wave (a 120 ms hit at 180 Hz) has a non-zero mean with no DC
    at all. Here: Hann-weighted means over 40 ms frames (sound above ~50 Hz falls in the window's
    side lobes), then the median over the quiet frames (30 dB under the loudest: head, gaps, tail),
    or over every frame when the sound never gets quiet. A tone whose phase turns from frame to
    frame averages out; only an offset common to the frames remains (ours, §5.5: measure DC, do
    not game the mean)."""
    x2 = data if data.ndim == 2 else data[:, None]
    n = x2.shape[0]
    if n == 0:
        return 0.0
    fl = int(min(0.04 * sr, max(16, n // 3)))
    if n < 2 * fl:
        return float(np.max(np.abs(x2.mean(axis=0))))
    hop = max(1, fl // 4)
    w = np.hanning(fl + 2)[1:-1]
    w /= w.sum()
    box = np.full(fl, 1.0 / fl)
    out = 0.0
    for ch in range(x2.shape[1]):
        x = x2[:, ch]
        means = signal.fftconvolve(x, w, mode="valid")[::hop]
        rms = np.sqrt(np.maximum(signal.fftconvolve(x * x, box, mode="valid")[::hop], 0.0))
        quiet = rms <= rms.max() * 10 ** (-30 / 20)
        sel = means[quiet] if quiet.sum() >= 2 else means
        out = max(out, abs(float(np.median(sel))))
    return out


def true_peak_dbtp(data: np.ndarray) -> float:
    """4x oversampled peak (BS.1770-4 annex 2 style estimate)."""
    up = signal.resample_poly(data, 4, 1, axis=0)
    return float(db(np.max(np.abs(up)))) if up.size else float("-inf")


def resample(x: np.ndarray, sr: int, target: int) -> np.ndarray:
    if sr == target:
        return x
    try:
        import soxr
        return soxr.resample(x, sr, target, quality="HQ")
    except Exception:
        from math import gcd
        g = gcd(sr, target)
        return signal.resample_poly(x, target // g, sr // g, axis=0)


def power_spectrum(x: np.ndarray, sr: int, n_fft: int = 4096):
    """Energy distribution over frequency (sum of |STFT|^2 over all frames)."""
    n_fft = int(min(n_fft, 2 ** int(np.floor(np.log2(max(256, len(x)))))))
    if len(x) < n_fft:
        x = np.pad(x, (0, n_fft - len(x)))
    f, _, Z = signal.stft(x, fs=sr, nperseg=n_fft, noverlap=n_fft * 3 // 4, boundary=None, padded=True)
    return f, (np.abs(Z) ** 2).sum(axis=1)
