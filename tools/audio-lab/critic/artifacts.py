"""L1b model-artefact detectors (§4.3.2). Flag only in batch 1; measured on the raw file, before mono.

Thresholds are starting points (unverified); with >= 3 refs of the same group, hiss and swirl
compare against the refs' P90 instead (the plan's "vs refs of the same family").
"""
from __future__ import annotations

import numpy as np

from .audio import EPS, fnum, pdb
from . import audio as A
from .spec import Spec
from .thresholds import L1B


def _stft(mono: np.ndarray, sr: int, n_fft: int = 1024, hop: int = 256):
    from scipy import signal
    if len(mono) < n_fft:
        mono = np.pad(mono, (0, n_fft - len(mono)))
    f, t, Z = signal.stft(mono, fs=sr, nperseg=n_fft, noverlap=n_fft - hop, boundary=None, padded=True)
    return f, t, np.abs(Z) ** 2


def pre_echo(env: dict, percussive: bool) -> float | None:
    if not percussive:
        return None
    t, rms = env["t"], env["rms"]
    on = t[env["i10"]]
    w0, w1 = on - (L1B["pre_echo_window_ms"] + L1B["pre_echo_guard_ms"]) / 1000, on - L1B["pre_echo_guard_ms"] / 1000
    sel = (t >= max(0.0, w0)) & (t < w1)
    if sel.sum() < 6:   # less than ~3 ms of history before the onset
        return None
    peak = float(np.max(rms ** 2)) + EPS
    return fnum(pdb(np.mean(rms[sel] ** 2)) - pdb(peak), 1)


def hiss_and_swirl(mono: np.ndarray, sr: int, onset_s: float) -> dict:
    out = {"hiss_flatness_body": None, "hiss_flatness_tail": None, "hiss_share_rise_db": None,
           "hiss_tail_dbfs": None, "swirl_flux_db": None}
    lo, hi = L1B["hiss_band"]
    if sr < 2 * hi * 0.98:
        return out
    f, t, P = _stft(mono, sr)
    E = P.sum(axis=0) + EPS
    emax = E.max()
    ipk = int(np.argmax(E))
    hb = (f >= lo) & (f < hi)
    Ph = P[hb] + EPS
    flat = np.exp(np.mean(np.log(Ph), axis=0)) / np.mean(Ph, axis=0)
    share = pdb(Ph.sum(axis=0) / E)
    after = np.arange(len(E)) >= ipk
    body = after & (E >= emax * 10 ** (-20 / 10))
    tail = after & (E < emax * 10 ** (-20 / 10)) & (E >= emax * 10 ** (-70 / 10))
    if body.sum() >= 2 and tail.sum() >= 3:
        out["hiss_flatness_body"] = fnum(flat[body].mean(), 3)
        out["hiss_flatness_tail"] = fnum(flat[tail].mean(), 3)
        out["hiss_share_rise_db"] = fnum(share[tail].mean() - share[body].mean(), 1)
        ti = t[tail]
        out["hiss_tail_dbfs"] = fnum(A.rms_db(A.band(mono, sr, lo, hi), sr, float(ti[0]), float(ti[-1])), 1)
    sl, sh = L1B["swirl_band"]
    sb = (f >= sl) & (f < sh)
    sus = (t >= onset_s + 0.05) & (E >= emax * 10 ** (-40 / 10))
    if sus.sum() >= 4:
        L = 10 * np.log10(P[sb][:, sus] + EPS)
        out["swirl_flux_db"] = fnum(np.mean(np.abs(np.diff(L, axis=1))), 2)
    return out


def noise_floor(mono: np.ndarray, sr: int) -> dict:
    """Stationary level at the end of the tail (10 ms frames, the last 80 ms before a 20 ms fade)."""
    t, r = A.frame_rms(mono, sr, 10.0, 10.0)
    lv = pdb(r ** 2)
    ipk = int(np.argmax(lv))
    below = np.where((np.arange(len(lv)) > ipk) & (lv < lv[ipk] - 30))[0]
    if not len(below):
        return {"noise_floor_dbfs": None, "noise_floor_note": "đuôi chưa xuống −30 dB"}
    reg = np.arange(below[0], max(below[0], len(lv) - 2))     # skip the last 20 ms (fade)
    reg = reg[r[reg] > 0][-8:]
    if len(reg) < 5:
        return {"noise_floor_dbfs": None, "noise_floor_note": "đuôi im lặng tuyệt đối hoặc quá ngắn"}
    slope = float(np.polyfit(t[reg], lv[reg], 1)[0])
    if np.ptp(lv[reg]) > 2.0 or slope < -15:
        return {"noise_floor_dbfs": None, "noise_floor_note": "đuôi còn đang tắt dần", "tail_slope_db_s": fnum(slope, 1)}
    return {"noise_floor_dbfs": fnum(np.median(lv[reg]), 1), "tail_slope_db_s": fnum(slope, 1)}


def wobble(track) -> float | None:
    if track is None:
        return None
    times, f0 = np.asarray(track[0], dtype=float), np.asarray(track[1], dtype=float)
    if len(f0) < 8:
        return None
    cents = 1200 * np.log2(f0 / np.median(f0))
    # A phrase (sampler arpeggio, music stem) changes note: judge the longest held note only,
    # otherwise every interval reads as hundreds of cents of "wobble".
    cuts = np.where(np.abs(np.diff(cents)) > 80.0)[0] + 1
    if len(cuts):
        seg = max(np.split(np.arange(len(cents)), cuts), key=len)
        if len(seg) < 8:
            return None
        times, cents = times[seg], cents[seg] - np.median(cents[seg])
    trend = np.polyval(np.polyfit(times, cents, 1), times)
    d = cents - trend
    return fnum((np.percentile(d, 95) - np.percentile(d, 5)) / 2, 1)


def detect(a: A.Audio, m: dict, ctx: dict, spec: Spec, ref_stats: dict | None = None,
           ai_generated: bool | None = None) -> dict:
    """ai_generated: False when the file's provenance says no generative model made it (library,
    sampler or code sources: critic.policy.provenance). Pitch wobble is then measured but not
    flagged: a real dan tranh or a played vibrato drifts by nature (§4.3.2 targets model artefacts)."""
    metrics: dict = {}
    flags: list[dict] = []

    def flag(fid, value, thr, msg):
        flags.append({"layer": "L1b", "id": fid, "value": value, "threshold": thr, "msg_vi": msg})

    if m.get("silent"):
        return {"metrics": metrics, "flags": flags, "thresholds_source": "default"}
    mono, sr = a.mono, a.sr
    g = spec.group_obj
    # a slow attack is the attack gate's business; its ramp would read as pre-echo
    fast = (m.get("attack_ms") or 0) <= (spec.attack_max_ms or 10.0)
    metrics["pre_echo_db"] = pre_echo(ctx["env"], g.percussive and fast)
    smear_limit = None
    if g.percussive and spec.attack_max_ms is not None:
        metrics["hf_attack_ms"] = m.get("hf_attack_ms")
        metrics["hf_onset_lag_ms"] = m.get("hf_onset_lag_ms")
        smear_limit = min(L1B["smear_attack_max_ms"], spec.attack_max_ms)
    metrics.update(hiss_and_swirl(mono, sr, (m.get("onset_ms") or 0) / 1000))
    if not spec.loop:
        metrics.update(noise_floor(mono, sr))
    metrics["pitch_wobble_cents"] = wobble(ctx.get("f0")) if spec.pitched else None
    if a.channels == 2:
        metrics["stereo_correlation"] = m.get("stereo_correlation")
        metrics["mono_loss_db"] = m.get("mono_loss_db")

    rs = ref_stats or {}
    src = "default"
    v = metrics.get("hf_attack_ms")
    if v is not None and smear_limit is not None:
        rsm = rs.get("hf_attack_ms")
        lim, why = smear_limit, f"{_n(smear_limit)} ms"
        if rsm and rsm["n"] >= L1B["refs_min"] and rsm["p90"] > smear_limit:
            # refs only relax the limit (a family whose approved cracks rise slowly); never tighten it
            src = "refs"
            lim, why = rsm["p90"], f"P90 của âm tham chiếu {_n(rsm['p90'])} ms"
        if v > lim:
            flag("smeared_attack", v, fnum(lim, 2),
                 f"đầu tiếng nhòe: lớp tách trên 2 kHz lên mất {_n(v)} ms (ngưỡng {why})")
    v = metrics["pre_echo_db"]
    if v is not None and v > L1B["pre_echo_max_db"]:
        flag("pre_echo", v, L1B["pre_echo_max_db"], f"có tiếng vọng trước đầu tiếng ({_n(v)} dB so với đỉnh)")
    ft, rise = metrics.get("hiss_flatness_tail"), metrics.get("hiss_share_rise_db")
    fb = metrics.get("hiss_flatness_body")
    hl = metrics.get("hiss_tail_dbfs")
    if ft is not None and (hl is None or hl > L1B["hiss_abs_floor_dbfs"]):
        rf, rr = rs.get("hiss_flatness_tail"), rs.get("hiss_share_rise_db")
        if rf and rr and rf["n"] >= L1B["refs_min"]:
            src = "refs"
            if ft > rf["p90"] and rise > rr["p90"]:
                flag("hf_hiss", ft, rf["p90"], f"rít cao tần 8–16 kHz ở đuôi, cao hơn P90 của âm tham chiếu")
        elif (ft >= L1B["hiss_flatness_min"] and ft - (fb or 0) >= L1B["hiss_flatness_rise"]
              and rise >= L1B["hiss_share_rise_db"]):
            flag("hf_hiss", ft, L1B["hiss_flatness_min"],
                 f"rít cao tần 8–16 kHz tăng ở đuôi (độ phẳng {_n(ft, 2)}, dải cao tăng {_n(rise)} dB)")
    sw = metrics.get("swirl_flux_db")
    rsw = rs.get("swirl_flux_db")
    if sw is not None and rsw and rsw["n"] >= L1B["refs_min"]:
        src = "refs"
        if sw > rsw["p90"]:
            flag("phasey_swirl", sw, fnum(rsw["p90"], 2), f"xoáy pha, 'kim loại giả' ở 4–16 kHz (biến thiên {_n(sw, 2)} dB > P90 tham chiếu)")
    elif sw is not None:
        metrics["swirl_note"] = "chưa có âm tham chiếu cùng nhóm nên chưa gắn cờ xoáy pha"
    v = metrics.get("pitch_wobble_cents")
    if v is not None and v > L1B["wobble_max_cents"]:
        if ai_generated is False:
            metrics["pitch_wobble_note"] = "nguồn là mẫu thu thật hoặc mã, không do mô hình tạo: không gắn cờ"
        else:
            flag("pitch_wobble", v, L1B["wobble_max_cents"], f"cao độ rung {_n(v)} cent ở đuôi")
    if str(a.subtype).upper() in ("PCM_U8", "PCM_S8"):
        flag("low_bit_depth", a.subtype, "PCM 16-bit trở lên",
             "PCM 8-bit: độ sâu bit thấp (nhiễu lượng tử khoảng −48 dBFS); không kiểm được đỉnh phẳng")
    if a.channels == 2:
        r, loss = metrics.get("stereo_correlation"), metrics.get("mono_loss_db")
        if (r is not None and r < L1B["stereo_corr_min"]) or (loss is not None and loss > L1B["mono_loss_max_db"]):
            flag("stereo_mismatch", {"correlation": r, "mono_loss_db": loss},
                 {"correlation": L1B["stereo_corr_min"], "mono_loss_db": L1B["mono_loss_max_db"]},
                 f"hai kênh lệch nhau (tương quan {_n(r, 2)}, mất {_n(loss)} dB khi gộp mono)")
    v = metrics.get("noise_floor_dbfs")
    if v is not None and v > L1B["noise_floor_max_dbfs"]:
        flag("noise_floor", v, L1B["noise_floor_max_dbfs"], f"nền nhiễu ở đuôi {_n(v)} dBFS")
    return {"metrics": metrics, "flags": flags, "thresholds_source": src}


L1B_REF_FEATURES = ("hiss_flatness_tail", "hiss_share_rise_db", "swirl_flux_db", "hf_attack_ms")


def ref_stats(rows: list[dict]) -> dict:
    out = {}
    for k in L1B_REF_FEATURES:
        vals = [r[k] for r in rows if isinstance(r.get(k), (int, float))]
        if vals:
            out[k] = {"n": len(vals), "p90": float(np.percentile(vals, L1B["refs_pct"]))}
    return out


def _n(v, nd=1) -> str:
    return "?" if v is None else f"{float(v):.{nd}f}".replace(".", ",").replace("-", "−")
