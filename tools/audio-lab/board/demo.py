"""Demo session with generated tones (no third-party audio), for tests and a first look.

Writes WAV files (+ a few demo cards and critic-like JSON) under <audio_dir> and the
session file under <review_root>/_demo/sessions/demo.json.
"""
from __future__ import annotations

import json
from pathlib import Path

SR = 48000
GAME = "_demo"


def _tones() -> dict[str, "object"]:
    import numpy as np
    from scipy import signal

    rng = np.random.default_rng(7)
    t = lambda dur: np.arange(int(dur * SR)) / SR  # noqa: E731

    def norm(x, peak_db):
        return x / (np.max(np.abs(x)) + 1e-12) * 10 ** (peak_db / 20)

    def fade(x, ms=3):
        n = int(SR * ms / 1000)
        x = x.copy()
        x[-n:] *= np.linspace(1, 0, n)
        return x

    def click(bright: bool):
        tt = t(0.035)
        noise = rng.standard_normal(len(tt)) * np.exp(-tt / 0.003)
        sos = signal.butter(4, 4000 if bright else 1500, "highpass" if bright else "lowpass", fs=SR, output="sos")
        body = np.sin(2 * np.pi * 180 * tt) * np.exp(-tt / 0.012) * 0.5
        return fade(signal.sosfilt(sos, noise) + body)

    def bell(f0, partials, tau):
        tt = t(1.0)
        x = sum(a * np.sin(2 * np.pi * f0 * r * tt) * np.exp(-tt / (tau / r ** 0.5)) for r, a in partials)
        return fade(x * np.minimum(1, tt / 0.002), 20)

    def hit(pitch, seed):
        r = np.random.default_rng(seed)
        tt = t(0.25)
        tr = signal.sosfilt(signal.butter(2, [2000, 6000], "bandpass", fs=SR, output="sos"),
                            r.standard_normal(len(tt))) * np.exp(-tt / 0.008)
        f = 140 * pitch * np.exp(-tt / 0.08) + 50
        body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / 0.07)
        return fade(tr * 0.8 + body, 10)

    def thin_hit(pitch, seed):
        x = hit(pitch, seed)
        return signal.sosfilt(signal.butter(2, 900, "highpass", fs=SR, output="sos"), x)

    def coin(f0, cut=False):
        tt = t(0.3)
        x = (np.sin(2 * np.pi * f0 * tt) + 0.4 * np.sin(2 * np.pi * f0 * 2.01 * tt)) * np.exp(-tt / 0.08)
        if cut:
            x = x[: int(0.06 * SR)]       # hard cut: the bad variant
            return x
        return fade(x, 10)

    def hum(detune=0.0):
        tt = t(2.0)
        x = sum(np.sin(2 * np.pi * (f + detune) * tt) / k for k, f in enumerate((55, 110, 165, 220), 1))
        return x

    a = click(True)
    return {
        "phim-sang.wav": norm(a, -14),
        "phim-duc.wav": norm(click(False), -14),
        "phim-sang-to.wav": norm(a, -4),          # same click, 10 dB louder: matching must cancel it
        "chuong-dong.wav": norm(bell(880, [(1, 1), (2.76, 0.4), (5.4, 0.2)], 0.45), -3),
        "chuong-gay.wav": norm(bell(660, [(1, 1), (3.0, 0.6), (5.0, 0.4), (7.0, 0.3)], 0.25), -3),
        **{f"trung-day-{i + 1}.wav": norm(hit(p, 10 + i), -2) for i, p in enumerate((1.0, 1.06, 0.95))},
        **{f"trung-mong-{i + 1}.wav": norm(thin_hit(p, 20 + i), -2) for i, p in enumerate((1.0, 1.06, 0.95))},
        **{f"xu-{i + 1}.wav": norm(coin(f, cut=(i == 2)), -3) for i, f in enumerate((1568, 1661, 1760, 1480))},
        "nen-ong.wav": norm(hum(), -6),
    }


def _card(x, path: Path, title: str) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 5), dpi=100)
    tt = np.arange(len(x)) / SR
    ax1.plot(tt, x, lw=0.7, color="#1f77b4")
    ax1.set_ylim(-1.05, 1.05)
    ax1.set_title("Dạng sóng", fontsize=9)
    ax2.specgram(x, NFFT=512, Fs=SR, noverlap=384, cmap="magma")
    ax2.set_ylim(0, 16000)
    ax2.set_title("Phổ theo thời gian", fontsize=9)
    fig.suptitle(title, fontsize=10)
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def write_demo(audio_dir: Path, review_root: Path) -> Path:
    import soundfile as sf

    from . import loudness

    audio_dir = Path(audio_dir)
    audio_dir.mkdir(parents=True, exist_ok=True)
    tones = _tones()
    for name, x in tones.items():
        sf.write(str(audio_dir / name), x, SR, subtype="PCM_16")
    # Cards and critic-like JSON for two items, so the reveal and the critic loudness path are exercised.
    for name in ("chuong-dong.wav", "chuong-gay.wav", "trung-day-1.wav", "trung-mong-1.wav"):
        p = audio_dir / name
        _card(tones[name], p.with_suffix(".png"), "Thẻ demo (vẽ bằng bảng, không phải bộ phê bình)")
    for name in ("chuong-dong.wav", "chuong-gay.wav"):
        p = audio_dir / name
        m = loudness.measure(p)
        doc = {"file": name, "sha256": loudness.sha256_file(p), "lufs_momentary_max": m["lufs_m_max"],
               "true_peak_dbtp": m["true_peak_db"], "duration_ms": m["duration_ms"],
               "qa_flags": [{"level": "INFO", "rule": "demo", "msg": "số đo demo"}]}
        p.with_suffix(".json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), "utf-8")

    A = lambda n: str(audio_dir / n)  # noqa: E731
    sess = {
        "schema": "audiolab.board.session/1",
        "session": "demo",
        "game": GAME,
        "batch": "demo",
        "title": "Phiên demo (âm tổng hợp)",
        "seed": 7,
        "max_minutes": 20,
        "anchors": 0,
        "items": [
            {"id": "demo.phim", "family": "phim-ui", "desc": "Tiếng phím đúng: ngắn, gọn, không che giọng đọc.",
             "probe": True,
             "candidates": [{"file": A("phim-sang.wav"), "role": "top"},
                            {"file": A("phim-duc.wav"), "role": "distinct"},
                            {"file": A("phim-sang-to.wav"), "role": "probe"}]},
            {"id": "demo.chuong", "family": "thuong", "desc": "Âm thưởng khi gõ xong từ.",
             "candidates": [A("chuong-dong.wav"), A("chuong-gay.wav")]},
            {"id": "demo.trung", "family": "trung", "group": "trung-nho", "desc": "Trúng nhỏ, mỗi bản có 3 biến thể.",
             "candidates": [{"files": [A(f"trung-day-{i}.wav") for i in (1, 2, 3)], "role": "top"},
                            {"files": [A(f"trung-mong-{i}.wav") for i in (1, 2, 3)], "role": "distinct"}]},
            {"id": "demo.xu", "family": "thuong", "mode": "variants", "desc": "Lượt biến thể: bỏ bản nghe lạc.",
             "loop": {"interval_ms": 350, "jitter": 0.2},
             "candidates": [A(f"xu-{i}.wav") for i in (1, 2, 3, 4)]},
            {"id": "demo.nen", "family": "nen", "desc": "Nền lặp 2 s: nghe mối nối.",
             "candidates": [A("nen-ong.wav")]},
        ],
    }
    out = Path(review_root) / GAME / "sessions" / "demo.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(sess, ensure_ascii=False, indent=1), "utf-8")
    return out
