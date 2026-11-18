"""PNG of a context render: level of the game mix, the focus stem and the spoken words; 1-4 kHz; limiter."""
from __future__ import annotations

from pathlib import Path

import numpy as np

SR = 48000


def _env_db(x: np.ndarray, win_s: float = 0.01) -> tuple[np.ndarray, np.ndarray]:
    m = x.mean(axis=1) if x.ndim == 2 else x
    hop = int(win_s * SR)
    n = m.shape[0] // hop
    e = np.sqrt(np.mean(m[: n * hop].reshape(n, hop) ** 2, axis=1) + 1e-12)
    return np.arange(n) * win_s, 20 * np.log10(e)


def draw(path: Path, res: dict, b, doc: dict) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    from critic import audio as A

    fig, ax = plt.subplots(3, 1, figsize=(15, 9), sharex=True, gridspec_kw={"height_ratios": [3, 2, 1]})
    t, g = _env_db(res["game"])
    ax[0].plot(t, g, color="0.55", lw=0.8, label="game mix (không giọng)")
    focus = doc.get("focus")
    if focus:
        from .scenes import _focus_stem
        st = _focus_stem(b, focus, doc["duration_s"])
        tf, f = _env_db(st)
        ax[0].plot(tf, f, color="tab:orange", lw=0.9, label=f"ứng viên: {focus}")
    tv, v = _env_db(res["voice"])
    ax[0].plot(tv, v, color="tab:blue", lw=0.9, label="giọng đọc")
    vc = (doc.get("metrics") or {}).get("voice") or {}
    for w, snr in zip(doc.get("words") or [], vc.get("per_word_db") or []):
        ax[0].axvspan(w["t_start"], w["t_start"] + 0.3, color="tab:green" if snr >= 10 else "tab:red", alpha=0.15)
        ax[0].text(w["t_start"], -8, f"{w['word']}\n{snr:+.0f} dB", fontsize=7, va="top")
    for mk in doc.get("timeline") or []:
        ax[0].axvline(mk["t"], color="0.8", lw=0.5)
        ax[0].text(mk["t"], -66, mk["id"].replace("fire.", "").replace("enemy.", ""), fontsize=6, rotation=90, va="bottom")
    ax[0].set_ylim(-70, 0)
    ax[0].set_ylabel("dBFS (RMS 10 ms)")
    ax[0].legend(loc="upper right", fontsize=8)
    gm = res["game"].mean(axis=1)
    vm = res["voice"].mean(axis=1)
    _, gb = _env_db(A.band(gm, SR, 1000, 4000))
    tb, vb = _env_db(A.band(vm, SR, 1000, 4000))
    ax[1].plot(tb[: gb.size], gb, color="0.45", lw=0.8, label="game mix 1–4 kHz")
    ax[1].plot(tb, vb, color="tab:blue", lw=0.8, label="giọng 1–4 kHz")
    ax[1].set_ylim(-80, -5)
    ax[1].set_ylabel("dB")
    ax[1].legend(loc="upper right", fontsize=8)
    tg = np.arange(res["gr_db"].size) / SR
    ax[2].plot(tg, res["gr_db"], color="tab:red", lw=0.8, label="bộ giới hạn master (dB ép)")
    for bus, c in (res.get("duck") or {}).items():
        if np.any(c < 0.999):
            ax[2].plot(tg, 20 * np.log10(np.maximum(c, 1e-4)), lw=0.7, label=f"hạ tiếng {bus}")
    ax[2].set_ylim(-8, 0.5)
    ax[2].set_xlabel("s")
    ax[2].legend(loc="lower right", fontsize=7, ncol=3)
    m = doc.get("metrics") or {}
    title = (f"{doc['scenario']} · {Path(doc['slots'].get(focus, '')).stem if focus else ''} · "
             f"giọng 1–4 kHz min {vc.get('min_db')} dB · tệ nhất (quét) {(m.get('voice_worst') or {}).get('min_db')} dB · "
             f"đỉnh {m['mix']['true_peak_dbtp']} dBTP · ép >3 dB {m['limiter']['time_over_3db_pct']} % · "
             f"loa nhỏ (ứng viên) {m.get('focus_small_speaker_loss_db')} dB")
    fig.suptitle(title, fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=80)
    plt.close(fig)
    return path
