"""L1 hygiene gate (§4.3.1). The only layer that blocks in batch 1.

Each check records where the plan measures it ("raw" = the file as generated, "fixed" = after
the fix chain of §5.1 step 4, "both"), its exact threshold and the fix the plan names.

Stage semantics (CLI --stage):
  final (default)  the file is meant to ship: every failed check blocks (verdict BLOCK).
  raw              generator output before the fix chain: clipping still blocks (it cannot be
                   repaired); every other failed check becomes a fix to apply (verdict NEEDS_FIX),
                   after which the fixed file must pass `--stage final`.
"""
from __future__ import annotations

import numpy as np

from .audio import fnum
from .spec import Spec
from .thresholds import L1

UNFIXABLE = {"clip_full_scale", "clip_flat_top", "source_clip", "silent"}


def runs(mask: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    d = np.diff(np.concatenate([[0], mask.astype(np.int8), [0]]))
    s = np.where(d == 1)[0]
    return s, np.where(d == -1)[0] - s


LOSSY_OR_FLOAT = {"FLOAT", "DOUBLE", "VORBIS", "OPUS", "MPEG_LAYER_I", "MPEG_LAYER_II", "MPEG_LAYER_III"}
EIGHT_BIT = {"PCM_U8", "PCM_S8"}


def clip_scan(data: np.ndarray, subtype: str | None = None) -> dict:
    """Runs of >= 3 samples at >= 0.999 FS, and flat tops: >= 4 equal magnitudes above -20 dBFS.

    Deliberate deviations from §4.3.1 (ours, documented in thresholds.L1):
      - float and lossy files (Vorbis, Opus, MP3): a decoder overshoots past 1.0 without any clipping,
        so a full-scale run counts only when it is truly flat (equal values); the true-peak check
        still catches the overshoot, and a gain change fixes it;
      - 8-bit PCM: equal neighbours are quantisation, not clipping: no flat-top test, and the
        full-scale level is the largest 8-bit value; reported as `low_bit_depth` (an L1b flag);
      - ideal square/pulse plateaus (entered and left by a jump larger than the plateau itself,
        i.e. across zero) are drawn that way, not cut: counted as `plateau_runs`, not as clipping;
      - a flat run counts only within 1 dB of the channel's peak: a clip ceiling is the peak (also
        after normalising), while rounded crests of low notes sit anywhere."""
    sub = (subtype or "").upper()
    lossy = sub in LOSSY_OR_FLOAT
    eight = sub in EIGHT_BIT
    level = min(L1["clip_level"], 127 / 128 - 1e-6) if eight else L1["clip_level"]
    full_runs = full_samples = 0
    flat_runs = plateau_runs = 0
    full_idx: list[int] = []
    flat_idx: list[int] = []
    lvl = 10 ** (L1["flat_min_dbfs"] / 20)
    for ch in range(data.shape[1]):
        x = data[:, ch]
        a = np.abs(x)
        s, n = runs(a >= level)
        keep = n >= L1["clip_run"]
        if lossy:            # only truly flat runs: every sample of the run equal to the first
            keep &= np.array([bool(np.all(a[st: st + ln] == a[st])) for st, ln in zip(s, n)], dtype=bool) \
                if len(s) else keep
        full_runs += int(keep.sum())
        full_samples += int(n[keep].sum())
        full_idx += [int(i) for i in s[keep][:200]]
        if eight:
            continue
        peak_ch = float(a.max()) if len(a) else 0.0
        eq = (a[1:] == a[:-1]) & (a[1:] > lvl)
        s, n = runs(eq)
        for st, ln in zip(s, n):
            if ln + 1 < L1["flat_run"]:
                continue
            # Guard: a smooth low-frequency crest at 16 bit rounds to equal values, with
            # entry and exit steps under a few LSB; a clipped top is entered by a steep edge.
            entry = abs(x[st] - x[st - 1]) if st > 0 else 1.0
            ex = st + ln
            exit_ = abs(x[ex + 1] - x[ex]) if ex + 1 < len(x) else 1.0
            if max(entry, exit_) < L1["flat_guard_step"]:
                continue
            # A clip ceiling is the channel's own peak: clipping writes no sample past it, and gain or
            # normalising after the cut moves the ceiling and the peak together (the 16-bit Stable
            # Audio 3 case). A rounded crest of a low note (VSCO horn D2 at 16 bit) also gives equal
            # samples with edge steps of a few LSB, but far under the peak (ours, after batch 0).
            if a[st] < peak_ch * L1["flat_near_peak"]:
                continue
            # A drawn square/pulse jumps onto and off its plateau by more than the plateau height.
            if min(entry, exit_) >= a[st] * L1["plateau_jump_rel"]:
                plateau_runs += 1
                continue
            flat_runs += 1
            if len(flat_idx) < 200:
                flat_idx.append(int(st))
    return {"full_runs": full_runs, "full_samples": full_samples, "flat_runs": flat_runs,
            "plateau_runs": plateau_runs, "full_idx": full_idx, "flat_idx": flat_idx,
            "low_bit_depth": eight, "lossy_or_float": lossy}


def source_clip_ok(scan: dict) -> bool:
    """A layer source passes the raw clip gate (§4.3.1, clipping cannot be repaired)."""
    return scan["full_runs"] == 0 and scan["flat_runs"] == 0


def _c(cid, label_vi, on, value, unit, limit, ok, fix, msg_vi=""):
    return {"id": cid, "label_vi": label_vi, "measured_on": on, "value": value, "unit": unit,
            "limit": limit, "ok": ok, "fix": fix, "msg_vi": msg_vi}


def gate(data: np.ndarray, sr: int, m: dict, spec: Spec, stage: str = "final", subtype: str | None = None,
         source_qa: dict | None = None) -> tuple[dict, dict]:
    """source_qa: raw L1 of the layers this file was built from (critic.policy.source_qa, read from
    the build's SOURCES.json): a clipped layer blocks even when the mix and the chain hid it."""
    checks: list[dict] = []
    clip = clip_scan(data, subtype)
    checks.append(_c("clip_full_scale", "Clip (3 mẫu liền ≥ 0,999 FS)", "raw", clip["full_runs"], "đoạn", 0,
                     clip["full_runs"] == 0, "reject",
                     f"{clip['full_runs']} đoạn, {clip['full_samples']} mẫu chạm trần" if clip["full_runs"] else ""))
    checks.append(_c("clip_flat_top", "Đỉnh phẳng (4 mẫu cùng độ lớn, trên −20 dBFS)", "raw", clip["flat_runs"],
                     "đoạn", 0, clip["flat_runs"] == 0, "reject",
                     f"{clip['flat_runs']} đoạn đỉnh phẳng: đã bị cắt khi ghi file" if clip["flat_runs"] else ""))
    if source_qa and source_qa.get("checked"):
        bad = source_qa.get("failed") or []
        checks.append(_c("source_clip", "Clip trong nguồn của từng lớp (trước khi trộn)", "raw",
                         {"checked": source_qa["checked"], "failed": bad, "excepted": source_qa.get("excepted") or []},
                         "", 0, not bad, "reject",
                         ("lớp bị cắt đỉnh trong file nguồn: " + ", ".join(bad)) if bad else ""))
    if m.get("silent"):
        checks.append(_c("silent", "File im lặng", "raw", m["peak_dbfs"], "dBFS", L1["silent_dbfs"], False,
                         "reject", "không có mẫu nào trên −60 dBFS"))
    else:
        if spec.attack_max_ms is not None:
            v = m["attack_ms"]
            checks.append(_c("attack", "Thời gian lên 10–90 %", "both", v, "ms", spec.attack_max_ms,
                             v <= spec.attack_max_ms, "rewindow_or_reject",
                             f"lên {_n(v)} ms > {_n(spec.attack_max_ms)} ms" if v > spec.attack_max_ms else ""))
        if spec.head_max_ms is not None:      # None: not checked (loops, music: §4.3.1 specs lane)
            v = m["head_silence_ms"]
            checks.append(_c("head_silence", "Im lặng ở đầu", "fixed", v, "ms", spec.head_max_ms,
                             v <= spec.head_max_ms, "trim_head",
                             f"{_n(v)} ms trước tiếng đầu tiên" if v > spec.head_max_ms else ""))
        if not spec.loop:
            ok = bool(m["end_decayed"] or m["end_faded"])
            checks.append(_c("tail", "Đuôi tắt hẳn hoặc có làm mờ", "fixed", m["end_level_db_rel"], "dB",
                             L1["tail_floor_db"], ok, "fade_tail",
                             "" if ok else f"file dừng ở {_n(m['end_level_db_rel'])} dB so với đỉnh, không làm mờ: "
                                           "tiếng tách ở cuối"))
    dc = m["dc_offset"]
    checks.append(_c("dc_offset", "Lệch DC", "fixed", dc, "FS", L1["dc_max"], dc < L1["dc_max"], "hpf",
                     f"lệch DC {dc:.4f} FS".replace(".", ",") if dc >= L1["dc_max"] else ""))
    tp = m["true_peak_dbtp"]
    checks.append(_c("true_peak", "Đỉnh thật", "fixed", tp, "dBTP", L1["true_peak_max_dbtp"],
                     tp is not None and tp <= L1["true_peak_max_dbtp"], "limit",
                     f"đỉnh thật {_n(tp, 2)} dBTP > −1" if tp is not None and tp > L1["true_peak_max_dbtp"] else ""))
    if spec.duration_ms:
        lo, hi = spec.duration_ms
        d = m["duration_ms"]
        dev = 0.0 if lo <= d <= hi else (lo - d) / lo if d < lo else (d - hi) / hi
        ok = dev <= spec.duration_tol + 1e-9
        checks.append(_c("duration", "Độ dài so với spec", "fixed", d, "ms",
                         [fnum(lo * (1 - spec.duration_tol), 3), fnum(hi * (1 + spec.duration_tol), 3)], ok, "trim_or_regen",
                         "" if ok else f"dài {_n(d)} ms, spec {_n(lo)}–{_n(hi)} ms (lệch {_n(dev * 100)} %)"))
    if spec.loop:
        s = m.get("seam") or {}
        if s.get("applies"):
            ok_j = s["jump_excess_dbfs"] is None or s["jump_excess_dbfs"] < L1["loop_jump_max_dbfs"]
            # music loops change at the bar line by design (downbeat after a decayed tail): only the
            # sample jump gates them; RMS and centroid continuity are for ambience/beds (ours)
            music = spec.group == "music"
            ok_r = music or s["rms_diff_db"] < L1["loop_rms_max_db"]
            ok_c = music or s["centroid_diff_rel"] < L1["loop_centroid_max_rel"]
            bad = [x for x, ok in (
                (f"bước nhảy {_n(s['jump_excess_dbfs'])} dBFS", ok_j),
                (f"RMS lệch {_n(s['rms_diff_db'], 2)} dB", ok_r),
                (f"trọng tâm phổ lệch {_n(s['centroid_diff_rel'] * 100)} %", ok_c)) if not ok]
            checks.append(_c("loop_seam", "Mối nối vòng lặp", "fixed",
                             {"jump_excess_dbfs": s["jump_excess_dbfs"], "rms_diff_db": s["rms_diff_db"],
                              "centroid_diff_rel": s["centroid_diff_rel"]}, "",
                             {"jump_excess_dbfs": L1["loop_jump_max_dbfs"], "rms_diff_db": L1["loop_rms_max_db"],
                              "centroid_diff_rel": L1["loop_centroid_max_rel"]},
                             ok_j and ok_r and ok_c, "crossfade_or_inpaint", "; ".join(bad)))
        if spec.bpm and spec.bars:
            want = spec.bars * spec.beats_per_bar * 60.0 / spec.bpm * 1000
            err = abs(m["duration_ms"] - want)
            checks.append(_c("music_length", "Đúng số ô nhịp", "fixed", fnum(err, 2), "ms", L1["music_bar_tol_ms"],
                             err <= L1["music_bar_tol_ms"], "regen",
                             f"dài {_n(m['duration_ms'])} ms, cần {_n(want)} ms" if err > L1["music_bar_tol_ms"] else ""))
    checks.append(_c("sample_rate", "Tần số lấy mẫu", "fixed", sr, "Hz", L1["sample_rate"],
                     sr == L1["sample_rate"], "resample", "" if sr == L1["sample_rate"] else f"{sr} Hz, cần 48000 Hz"))
    ch = data.shape[1]
    ok_ch = ch == 1 or (spec.stereo_ok and ch == 2)
    checks.append(_c("channels", "Số kênh", "fixed", ch, "kênh", "1" if not spec.stereo_ok else "1–2", ok_ch,
                     "mono", "" if ok_ch else f"{ch} kênh, nhóm này cần mono"))
    if ch == 2 and m.get("stereo_correlation") is not None:
        r = m["stereo_correlation"]
        checks.append(_c("stereo_corr", "Tương quan hai kênh", "raw", r, "", L1["stereo_corr_min"],
                         r > L1["stereo_corr_min"], "mid", "" if r > L1["stereo_corr_min"] else f"tương quan {_n(r)} ≤ 0"))

    for c in checks:
        c["blocking"] = (not c["ok"]) and (stage == "final" or c["id"] in UNFIXABLE)
    failed = [c for c in checks if not c["ok"]]
    blocking = [c["id"] for c in failed if c["blocking"]]
    fixes = [c["fix"] for c in failed if not c["blocking"]]
    verdict = "BLOCK" if blocking else ("NEEDS_FIX" if failed else "PASS")
    res = {"stage": stage, "pass": not failed, "verdict": verdict, "blocking": blocking,
           "fixes": fixes, "failed": [c["id"] for c in failed], "checks": checks}
    return res, {"clip_idx": clip["full_idx"], "flat_idx": clip["flat_idx"], "clip_scan": {
        k: clip[k] for k in ("full_runs", "flat_runs", "plateau_runs", "low_bit_depth", "lossy_or_float")}}


def _n(v, nd: int = 1) -> str:
    if v is None:
        return "?"
    if isinstance(v, (int, np.integer)):
        return str(int(v)).replace("-", "−")
    return f"{float(v):.{nd}f}".replace(".", ",").replace("-", "−")
