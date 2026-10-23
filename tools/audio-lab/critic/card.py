"""L6 PNG card: one image per file, readable at a glance (§4.1 L6, §4.5).

Header: verdict, rank, key numbers and flags. Panels: waveform (clip and flat-top marks, onset,
head silence), head and tail (or loop seam) zooms, mel spectrogram to Nyquist with the 8 kHz line
(learned models hear only below it), average spectrum, loudness envelope (1 ms RMS, LUFS-M,
100 ms blocks, -60 dB line) and the L2 target bars.
"""
from __future__ import annotations

import textwrap

import numpy as np

from . import audio as A
from .audio import pdb

COL = {"BLOCK": "#c62828", "NEEDS_FIX": "#ef6c00", "PASS": "#2e7d32", "UNGATED": "#546e7a"}
WORD = {"BLOCK": "CHẶN", "NEEDS_FIX": "CẦN SỬA", "PASS": "ĐẠT", "UNGATED": "CHƯA KIỂM L1"}


def vn(v, nd=1, unit="") -> str:
    if v is None:
        return "–"
    if isinstance(v, (int, np.integer)) and not isinstance(v, bool):
        s = str(int(v))
    else:
        s = f"{float(v):.{nd}f}"
    s = s.replace("-", "−").replace(".", ",")
    return f"{s} {unit}".strip()


def _fraction(feature: str) -> bool:
    return "share" in feature and not feature.endswith("_db")


def _key_lines(r: dict) -> list[str]:
    m = r.get("metrics") or {}
    ps = (r.get("L2") or {}).get("psycho") or {}
    pitched = bool((r.get("spec") or {}).get("pitched"))
    # pitched sounds: the 200-500 Hz share includes the fundamental, so it is not "mud"
    mud = f"200–500 Hz (gồm nốt gốc) {vn((m.get('mud_share') or 0) * 100, 0, '%')}" if pitched else \
        f"ù 200–500 Hz {vn((m.get('mud_share') or 0) * 100, 0, '%')}"
    lines = [
        f"Đỉnh {vn(m.get('peak_dbfs'), 1, 'dBFS')}  ·  đỉnh thật {vn(m.get('true_peak_dbtp'), 1, 'dBTP')}  ·  "
        f"LUFS-M max {vn(m.get('lufs_m_max'), 1)}  ·  LUFS 100 ms max {vn(m.get('lufs_100ms_max'), 1)}  ·  "
        f"DC {vn(m.get('dc_offset'), 4)}",
        f"Im lặng đầu {vn(m.get('head_silence_ms'), 1, 'ms')}  ·  lên 10–90 % {vn(m.get('attack_ms'), 1, 'ms')}  ·  "
        f"lớp tách lên {vn(m.get('hf_attack_ms'), 1, 'ms')}  ·  "
        f"crest {vn(m.get('crest_db'), 1, 'dB')}  ·  punch {vn(m.get('punch_db'), 1, 'dB')}  ·  "
        f"đuôi → −60 dB {vn(m.get('tail_ms'), 0, 'ms')}  ·  cuối file {vn(m.get('end_level_db_rel'), 0, 'dB')}",
        f"Trọng tâm {vn(m.get('centroid_hz'), 0, 'Hz')}  ·  rolloff 85 % {vn(m.get('rolloff85_hz'), 0, 'Hz')}  ·  "
        f"{mud}  ·  dưới 150 Hz {vn((m.get('share_below_150') or 0) * 100, 0, '%')}  ·  "
        f"mất loa nhỏ {vn(m.get('speaker_loss_db'), 1, 'dB')}  ·  độ chói {vn(ps.get('sharpness_acum'), 2, 'acum')}  ·  "
        f"độ gắt {vn(ps.get('roughness_asper'), 3, 'asper')}",
    ]
    s = m.get("seam")
    if s and s.get("applies"):
        lines.append(f"Mối nối: bước nhảy {vn(s.get('jump_excess_dbfs'), 1, 'dBFS')}  ·  RMS lệch {vn(s.get('rms_diff_db'), 2, 'dB')}"
                     f"  ·  trọng tâm lệch {vn((s.get('centroid_diff_rel') or 0) * 100, 1, '%')}")
    return lines


def render(r: dict, ctx: dict, png: str, blind: bool = False) -> None:
    """blind: card for the Listening Board, shown after the owner rated (§7): measurements and L1
    hygiene failures only. No file name, verdict, rank, score, "ask the owner", L2 target bars or
    L1b/L4/L5 flags: machine judgements shown between ids would teach the owner's ear."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    import librosa
    import librosa.display

    a: A.Audio = ctx["audio"]
    data, sr, mono = a.data, a.sr, a.mono
    m = r.get("metrics") or {}
    dur = a.duration
    ms = dur <= 2.0
    k = 1000.0 if ms else 1.0
    xl = "ms" if ms else "s"
    t = np.arange(len(mono)) / sr * k
    verdict = r["verdict"]
    onset = (m.get("onset_ms") or 0) / 1000
    attack_end = onset + (m.get("attack_ms") or 0) / 1000
    head = (m.get("head_silence_ms") or 0) / 1000

    plt.rcParams.update({"font.size": 10})
    sp = r["spec"]
    s = r.get("score") or {}
    l1 = r.get("L1") or {}
    keys = _key_lines(r)
    flags = [] if blind else [f"{f['layer']} {f['msg_vi']}" for f in r.get("flags", [])]
    fails = [c["msg_vi"] for c in l1.get("checks", []) if not c["ok"] and c.get("msg_vi")]
    txt = "; ".join(fails + flags) or ("Không có lỗi vệ sinh L1." if blind else "Không có cờ.")
    wrapped = textwrap.wrap(txt, 190)[:2]
    fig_h = 10.0
    H = fig_h * 72.0
    fig = plt.figure(figsize=(15, fig_h), dpi=100)

    def ty(pts):          # header laid out in points from the top
        return 1.0 - pts / H

    # header
    name = "Bản đang nghe" if blind else r['file']['name']
    length = vn(dur * 1000, 0, 'ms') if ms else vn(dur, 2, 's')
    if blind:   # no group key or file format: an OGG original next to WAV copies would show its source
        title = f"{name}   ·   {sp.get('group_name_vi')}   ·   {length}   ·   {a.channels} kênh"
    else:
        title = (f"{name}   ·   {sp.get('group_name_vi')} ({sp['group']}, họ {sp['family']})   ·   "
                 f"{length}   ·   {sr} Hz × {a.channels} kênh   ·   {r['file']['subtype']}")
    fig.text(0.01, ty(6), title, fontsize=14, weight="bold", va="top")
    why = ", ".join(l1.get("failed") or [])
    badge = WORD.get(verdict, verdict) + (f": {why}" if why else "")
    if not blind:
        fig.text(0.01, ty(32), badge, fontsize=13, weight="bold", va="top", color="white",
                 bbox={"facecolor": COL.get(verdict, "#555"), "edgecolor": "none", "pad": 3})
    l3 = ((r.get("L3") or {}).get("scores")) or {}
    rank = (f"Hạng {s['rank']}/{s['n_ranked']} trong {s.get('rank_group')}  ·  điểm tổng {vn(s.get('combined'), 2)}"
            if s.get("rank") else "Không xếp hạng (bị chặn)")
    rank += f"  ·  L2 {vn((r.get('L2') or {}).get('score'), 2)}"
    if l3:
        rank += f"  ·  AES PQ {vn(l3.get('PQ'), 2)} CE {vn(l3.get('CE'), 2)}"
    if r.get("ask_owner", {}).get("value"):
        rank += "  ·  HỎI CHỦ DỰ ÁN"
    if blind:   # numbers and L1 failures stay; nothing that ranks or judges
        rank = "Số đo và lỗi vệ sinh L1 (không có điểm hay cờ của máy)"
    fig.text(0.01, ty(58), rank, fontsize=12, va="top")
    y = 80.0
    for line in keys:
        fig.text(0.01, ty(y), line, fontsize=10.5, va="top", family="DejaVu Sans Mono")
        y += 15.5
    for line in wrapped:
        fig.text(0.01, ty(y), line, fontsize=10.5, va="top", color="#b71c1c" if (fails or flags) else "#2e7d32")
        y += 15.0
    gs = GridSpec(3, 8, figure=fig, top=ty(y + 26), bottom=0.05, left=0.05, right=0.98,
                  height_ratios=[1.0, 1.25, 1.0], hspace=0.45, wspace=0.9)

    # waveform
    ax = fig.add_subplot(gs[0, :6])
    for ch in range(data.shape[1]):
        ax.plot(t, data[:, ch], lw=0.6, alpha=0.85)
    ax.axhline(1, color="r", lw=0.5, ls="--")
    ax.axhline(-1, color="r", lw=0.5, ls="--")
    ci = ctx.get("clip_idx") or []
    if ci:
        ax.plot(np.array(ci) / sr * k, np.sign(mono[ci]) * 1.02, "r|", ms=12, mew=1.5, label=f"clip ({len(ci)}+)")
    fi = ctx.get("flat_idx") or []
    if fi:
        ax.plot(np.array(fi) / sr * k, np.sign(mono[fi]) * 1.06, "mv", ms=5, label=f"đỉnh phẳng ({len(fi)}+)")
    if head > 0.0005:
        ax.axvspan(0, head * k, color="#9e9e9e", alpha=0.35, label=f"im lặng đầu {vn(head * 1000, 1)} ms")
    ax.axvline(onset * k, color="g", lw=1, ls="--", label="đầu tiếng (10 %)")
    ax.set_xlim(0, max(t[-1], 1e-6))
    ax.set_ylim(-1.12, 1.12)
    ax.set_title("Dạng sóng (đường đỏ: 0 dBFS)", loc="left", fontsize=10)
    ax.set_xlabel(xl)
    ax.legend(loc="upper right", fontsize=8)

    # zooms
    ax = fig.add_subplot(gs[0, 6])
    a0 = int(max(0.0, onset - 0.010) * sr)
    a1 = min(len(mono), int((onset + 0.040) * sr))
    ax.plot((np.arange(a0, a1) / sr - onset) * 1000, mono[a0:a1], lw=0.8)
    ax.axvline(0, color="g", lw=0.8, ls="--")
    if attack_end - onset <= 0.040:
        ax.axvline((attack_end - onset) * 1000, color="orange", lw=0.8, ls="--")
    ax.set_xlim(-10, 40)
    ax.set_title(f"Đầu tiếng (lên {vn(m.get('attack_ms'), 1)} ms)", fontsize=9, loc="left")
    ax.set_xlabel("ms")
    ax = fig.add_subplot(gs[0, 7])
    seam = m.get("seam")
    if seam and seam.get("applies"):
        w = int(0.02 * sr)
        z = np.concatenate([mono[-w:], mono[:w]])
        ax.plot((np.arange(len(z)) - w) / sr * 1000, z, lw=0.8)
        ax.axvline(0, color="r", lw=1)
        ax.set_title("Mối nối (cuối → đầu)", fontsize=9, loc="left")
    else:
        w = min(len(mono), int(0.03 * sr))
        ax.plot((np.arange(w) - w) / sr * 1000, mono[-w:], lw=0.8)
        ax.axvline(0, color="r", lw=1)
        ax.set_title(f"Cuối file ({vn(m.get('end_level_db_rel'), 0)} dB)", fontsize=9, loc="left")
    ax.set_xlabel("ms")

    # mel spectrogram
    ax = fig.add_subplot(gs[1, :6])
    # short sounds need time resolution: a short window, zero-padded to 2048 so no mel row is empty
    win = 2048 if dur > 1.0 else 1024 if dur > 0.3 else 512
    n_fft = 2048
    hop = max(win // 8, len(mono) // 2400)
    import warnings
    with warnings.catch_warnings():      # small n_fft leaves a few low mel rows empty (drawn black)
        warnings.simplefilter("ignore", UserWarning)
        M = librosa.feature.melspectrogram(y=mono.astype(np.float32), sr=sr, n_fft=n_fft, hop_length=hop,
                                           win_length=win, n_mels=128, fmax=sr / 2)
    img = librosa.display.specshow(librosa.power_to_db(M, ref=np.max, top_db=80), sr=sr, hop_length=hop,
                                   x_axis="ms" if ms else "s", y_axis="mel", fmax=sr / 2, ax=ax, cmap="magma")
    ax.axhline(8000, color="w", ls=":", lw=1)
    ax.axvline(onset, color="#00e676", lw=1, ls="--")
    from matplotlib.ticker import FuncFormatter
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x * k:g}".replace(".", ",")))
    ax.set_title("Mel spectrogram tới Nyquist (sáng = to, dải 80 dB). Chấm trắng: 8 kHz, mô hình học máy "
                 "không nghe trên mức này", loc="left", fontsize=10)
    ax.set_xlabel(xl)

    # average spectrum
    ax = fig.add_subplot(gs[1, 6:])
    if "spectrum" in ctx:
        f, avg = ctx["spectrum"]
        sel = f >= 20
        ax.semilogx(f[sel], pdb(avg[sel] / (avg[sel].max() + 1e-20)), lw=0.9)
        for lo, hi, c in ((40, 90, "#bbdefb"), (200, 500, "#ffe0b2"), (1000, 4000, "#e1bee7"), (4000, 8000, "#c8e6c9")):
            ax.axvspan(lo, hi, color=c, alpha=0.6, lw=0)
        ax.set_xlim(20, sr / 2)
        ax.set_ylim(-80, 3)
    ax.set_title("Phổ trung bình (xanh: sub, cam: ù, tím: giọng 1–4k)", fontsize=9, loc="left")
    ax.set_xlabel("Hz")

    # loudness envelope (full width on the blind card: it has no L2 panel)
    ax = fig.add_subplot(gs[2, :] if blind else gs[2, :6])
    env = ctx.get("env")
    if env is not None:
        ax.plot(env["t"] * k, env["env_db"], lw=0.7, color="#1565c0", label="RMS 1 ms (dBFS)")
        ax.axhline(env["env_db"].max() - 60, color="grey", lw=0.8, ls=":", label="đỉnh − 60 dB")
    if "loudness" in ctx:
        tm, lm, tb, lb = ctx["loudness"]
        ax.plot(tm * k, lm, lw=1.3, color="k", label=f"LUFS-M 400 ms (max {vn(m.get('lufs_m_max'), 1)})")
        ax.plot(tb * k, lb, lw=0.9, color="#8e24aa", ls="--",
                label=f"LUFS cửa sổ 100 ms (max {vn(m.get('lufs_100ms_max'), 1)})")
    ax.axvline(onset * k, color="g", lw=1, ls="--")
    ax.axvline(attack_end * k, color="orange", lw=1, ls="--", label=f"đạt 90 % ({vn(m.get('attack_ms'), 1)} ms)")
    ax.set_xlim(0, dur * k)
    ax.set_ylim(-100, 3)
    ax.set_ylabel("dB")
    ax.set_xlabel(xl)
    ax.set_title("Đường độ to", loc="left", fontsize=10)
    ax.legend(loc="upper right", fontsize=8, ncol=3)

    if blind:
        fig.savefig(png, dpi=100, bbox_inches="tight")
        plt.close(fig)
        return
    # L2 targets
    ax = fig.add_subplot(gs[2, 6:])
    rows = [x for x in ((r.get("L2") or {}).get("targets") or []) if x.get("d") is not None]
    if rows:
        ds = [x["d"] for x in rows]
        ax.barh(range(len(rows)), [max(d, 0.02) for d in ds], height=0.8,
                color=[("#a5d6a7" if d >= 0.8 else "#ffe082" if d >= 0.5 else "#ef9a9a") for d in ds])
        for i, x in enumerate(rows):
            v = x["value"]
            val = vn(v * 100, 0, "%") if _fraction(x["feature"]) and v is not None else vn(v, 1)
            ax.text(0.02, i, f"{x['feature']} = {val}", va="center", fontsize=8)
        ax.set_yticks([])
        ax.set_ylim(len(rows) - 0.5, -0.5)
        ax.set_xlim(0, 1)
    ax.set_title(f"Mục tiêu L2 của nhóm (1 = đạt)", fontsize=9, loc="left")

    fig.savefig(png, dpi=100, bbox_inches="tight")
    plt.close(fig)
