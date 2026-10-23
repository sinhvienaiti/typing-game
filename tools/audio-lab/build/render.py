"""Render a recipe: layers -> mix -> final chain -> 48 kHz WAV masters + OGG Vorbis runtime files.

Output (one run): <out>/
  masters/<id>-v<n>.wav            48 kHz PCM 24-bit
  runtime/<stem>-<n>.ogg           48 kHz OGG Vorbis (byte-deterministic)
  render.json                      plan, per-variant QA (raw mix and final), chain report
  SOURCES.json                     §10.5 records for each runtime file (keys = runtime paths)
  licences.rows.jsonl              §10.6 rows this run needs
  manifest.fragment.json           §11 manifest v2 entry for the id
  recipe.json                      the exact recipe rendered
"""
from __future__ import annotations

import datetime as dt
import io
import json
import struct
from dataclasses import dataclass
from importlib import metadata
from pathlib import Path

import numpy as np
import soundfile as sf

from build import chain, dsp, ledger, measure, policy, recipe as rcp, sources

ENGINE = "audiolab-build/1"
SR = dsp.SR


# ---------------------------------------------------------------- file writers

def write_wav(path: Path, x: np.ndarray, sr: int = SR) -> None:
    """PCM 24-bit (no PEAK chunk, so the bytes are deterministic)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(path), dsp.as2d(x), sr, subtype="PCM_24", format="WAV")


# Ogg page CRC: poly 0x04C11DB7, init 0, not reflected.
_CRC_TABLE = []
for _i in range(256):
    _c = _i << 24
    for _ in range(8):
        _c = ((_c << 1) ^ 0x04C11DB7) & 0xFFFFFFFF if _c & 0x80000000 else (_c << 1) & 0xFFFFFFFF
    _CRC_TABLE.append(_c)


def _crc_fast(data: bytes) -> int:
    crc = 0
    for byte in data:
        crc = ((crc << 8) & 0xFFFFFFFF) ^ _CRC_TABLE[((crc >> 24) ^ byte) & 0xFF]
    return crc


def fix_ogg_serial(data: bytes, serial: int) -> bytes:
    """libsndfile picks a random Ogg stream serial; set a fixed one and redo page CRCs."""
    out = bytearray(data)
    pos = 0
    while pos + 27 <= len(out):
        if out[pos:pos + 4] != b"OggS":
            raise ValueError(f"not an Ogg page at byte {pos}")
        nseg = out[pos + 26]
        size = 27 + nseg + sum(out[pos + 27:pos + 27 + nseg])
        out[pos + 14:pos + 18] = struct.pack("<I", serial)
        out[pos + 22:pos + 26] = b"\0\0\0\0"
        out[pos + 22:pos + 26] = struct.pack("<I", _crc_fast(bytes(out[pos:pos + size])))
        pos += size
    return bytes(out)


def encode_ogg(x: np.ndarray, sr: int = SR, quality: float = 0.6) -> bytes:
    """OGG Vorbis bytes; the stream serial comes from the PCM hash, so equal input gives equal bytes."""
    buf = io.BytesIO()
    sf.write(buf, dsp.as2d(x).astype(np.float32), sr, format="OGG", subtype="VORBIS",
             compression_level=float(np.clip(1.0 - quality, 0.0, 1.0)))
    pcm_hash = ledger.sha256_bytes(np.ascontiguousarray(dsp.as2d(x), dtype="<f4").tobytes())
    return fix_ogg_serial(buf.getvalue(), int(pcm_hash[:8], 16))


def write_ogg(path: Path, x: np.ndarray, sr: int = SR, quality: float = 0.6) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(encode_ogg(x, sr, quality))


def ogg_safe(x: np.ndarray, ceiling_db: float, sr: int = SR, quality: float = 0.6) -> tuple[np.ndarray, bytes, float, float]:
    """Encode; if Vorbis overshoot pushes the decoded true peak over the ceiling, lower the mix and retry.

    Returns (audio used for master and OGG, OGG bytes, gain applied dB, decoded true peak dBTP)."""
    applied = 0.0
    for _ in range(4):
        data = encode_ogg(x, sr, quality)
        decoded, _ = sf.read(io.BytesIO(data), always_2d=True, dtype="float64")
        tp = measure.true_peak_db(decoded, sr)
        if tp <= ceiling_db:
            break
        step = ceiling_db - tp - 0.05
        x = x * dsp.db_to_gain(step)
        applied += step
    else:  # keep the OGG bytes in step with the last gain change
        data = encode_ogg(x, sr, quality)
        decoded, _ = sf.read(io.BytesIO(data), always_2d=True, dtype="float64")
        tp = measure.true_peak_db(decoded, sr)
    return x, data, round(applied, 3), round(tp, 2)


def tool_versions() -> dict[str, str]:
    out = {"audiolab-build": ENGINE.split("/")[1], "libsndfile": sf.__libsndfile_version__}
    for pkg in ("numpy", "scipy", "soxr", "soundfile", "pedalboard", "pyloudnorm"):
        try:
            out[pkg] = metadata.version(pkg)
        except metadata.PackageNotFoundError:
            pass
    return out


# ---------------------------------------------------------------- render

class LicenceError(RuntimeError):
    pass


class RawClipError(RuntimeError):
    """A layer source is clipped as stored (§4.3.1: clipping cannot be repaired)."""


def _raw_clip_gate(layer: dict, loaded: sources.Loaded, strict: bool) -> dict | None:
    """Per-source L1 clip gate, before mixing. A clipped source stops the render unless the recipe
    names a reason in `allowClip` (recorded as rawQa.exception, which the final critic accepts)."""
    qa = loaded.raw_qa
    if qa is None or qa["verdict"] == "PASS":
        return qa
    qa = dict(qa)
    if layer.get("allowClip"):
        qa["exception"] = str(layer["allowClip"])
        return qa
    if strict:
        bad = ", ".join(f"{f['file']} ({f['fullRuns']} đoạn chạm trần, {f['flatRuns']} đoạn đỉnh phẳng)"
                        for f in qa["files"] if not f["ok"])
        raise RawClipError(f"lớp '{layer['id']}': nguồn bị cắt đỉnh trong file gốc: {bad}. Đổi nguồn, "
                           "hoặc ghi lý do vào allowClip của lớp (mục 4.3.1: clip không sửa được)")
    return qa


def _refuse_bad_source(layer_id: str, loaded: sources.Loaded) -> None:
    """Render-time gate: never mix a disallowed source or a non-commercial model (§3.5, §10.2)."""
    for row in loaded.rows:
        why = policy.source_problem(row)
        if why:
            raise LicenceError(f"lớp '{layer_id}': nguồn {row.get('path') or row.get('file') or row['key']} bị chặn: {why}")
    model = loaded.layer_meta.get("model")
    if model and policy.model_denied(model):
        raise LicenceError(f"lớp '{layer_id}': mô hình phi thương mại bị cấm: {model}")
    lic = loaded.layer_meta.get("licence")
    if loaded.kind == "gen" and policy.classify(lic) != "allowed":
        raise LicenceError(f"lớp '{layer_id}': giấy phép đầu ra mô hình {lic!r} không được phép")


@dataclass
class RunResult:
    out: Path
    report: dict
    sources: dict
    rows: list[dict]


def _layer_audio(layer: dict, lp: rcp.LayerPlan, loaded: sources.Loaded, channels: int) -> tuple[np.ndarray, dict]:
    x, fold = dsp.to_channels(loaded.audio, channels)
    tr = layer.get("trim") or {}
    if tr:
        x = dsp.trim(x, tr.get("startMs", 0.0), tr.get("endMs"))
    if layer.get("reverse"):
        x = x[::-1].copy()
    semis = float(layer.get("pitchSemitones", 0.0)) + lp.pitch_cents / 100.0
    if semis:
        x = (dsp.pitch_preserve if layer.get("pitchMode") == "preserve" else dsp.pitch_varispeed)(x, semis)
    x = dsp.apply_filters(x, layer.get("filters"))
    x = dsp.fade(x, layer.get("fadeInMs", 0.0), layer.get("fadeOutMs", 0.0))
    gain = float(layer.get("gainDb", 0.0)) + lp.gain_db
    x = x * dsp.db_to_gain(gain)
    settings = {
        "offsetMs": round(float(layer.get("offsetMs", 0.0)) + lp.offset_ms, 3), "gainDb": round(gain, 3),
        "pitchSemitones": round(semis, 4), "pitchMode": layer.get("pitchMode", "varispeed"), "fold": fold,
    }
    for k in ("trim", "fadeInMs", "fadeOutMs", "reverse", "filters"):
        if layer.get(k):
            settings[k] = layer[k]
    if lp.swap_index:
        settings["swap"] = lp.swap_index
    return x, settings


def _chain_all(mixes: list, params: dict, level: float, loop: bool) -> list[tuple[np.ndarray, dict]]:
    out = []
    for plan, mix, *_ in mixes:
        p = json.loads(json.dumps(params))
        if (p.get("normalise") or {}).get("mode", "none") != "none":
            p["normalise"]["target"] = level + plan.gain_db
        final, rep = chain.run(mix, SR, p, loop=loop)
        rep["params"] = p
        out.append((final, rep))
    return out


def render(recipe_in: dict | str | Path, *, out: Path | None = None, run: str | None = None,
           libraries: Path | None = None, seed: int | None = None, count: int | None = None,
           spec: Path | None = None, ledger_rows: dict[str, dict] | None = None, ogg: bool | None = None,
           date: str | None = None, strict: bool = True) -> RunResult:
    """Render every variant. strict=False only lets tests plant bad sources for licence_check."""
    from common import env  # paths of ~/AudioLab

    data = rcp.load(recipe_in) if not isinstance(recipe_in, dict) else recipe_in
    if isinstance(recipe_in, dict):
        rcp.validate(data)
    libraries = Path(libraries) if libraries else env.LIBRARIES
    date = date or ledger.today()
    rhash = rcp.recipe_hash(data)
    run = run or f"{dt.datetime.now():%Y%m%d-%H%M%S}-{rhash[:8]}"

    channels = int(data.get("channels", 1))
    loop = bool(data.get("loop", False))
    params = rcp.chain_params(data)
    spec_info = rcp.read_spec(spec)
    plans, warnings, limit_src = rcp.plan_variants(data, spec_info, seed, count)
    stem = rcp.export_stem(data)
    exp = data.get("export") or {}
    want_ogg = exp.get("ogg", True) if ogg is None else ogg
    quality = float(exp.get("oggQuality", 0.6))
    layers_by_id = {layer["id"]: layer for layer in data["layers"]}
    tools = tool_versions()

    all_rows: dict[str, dict] = {}
    copies: dict[str, str] = {}
    mixes = []
    for plan in plans:
        mix = np.zeros((0, channels))
        layer_recs, ai_ok, models = [], True, []
        for lid, lp in plan.layers.items():
            layer = layers_by_id[lid]
            if layer.get("mute"):
                continue
            loaded = sources.load(lp.source, libraries=libraries, synth_seed=lp.synth_seed, ledger_rows=ledger_rows)
            if strict:
                _refuse_bad_source(lid, loaded)
            layer_qa = _raw_clip_gate(layer, loaded, strict)
            x, settings = _layer_audio(layer, lp, loaded, channels)
            mix = dsp.place(mix, x, dsp.ms_to_n(settings["offsetMs"]))
            for row in loaded.rows:
                all_rows.setdefault(row["key"], row)
                if row.get("kind") == "source" and row.get("ai_input_allowed") is False:
                    ai_ok = False
            for key, path in loaded.copies.items():
                copies[key] = str(path)
            if loaded.layer_meta.get("model"):
                models.append(loaded.layer_meta["model"])
            rec_layer = {"id": lid, "role": layer.get("role", lid), **loaded.layer_meta, "settings": settings}
            if layer_qa is not None:
                rec_layer["rawQa"] = layer_qa
            layer_recs.append(rec_layer)
        if plan.pitch_cents:
            mix = dsp.pitch_varispeed(mix, plan.pitch_cents / 100.0)
        mixes.append((plan, mix, layer_recs, ai_ok, models, measure.summary(mix, SR)))

    # Sources passed the gate: only now create the run folder.
    out = Path(out) if out else env.work_dir(data["game"], data["id"], run)
    out.mkdir(parents=True, exist_ok=True)

    # Chain pass. If short sounds cannot reach the common level without squashing past maxGrDb,
    # lower the id's level so every variant lands at the same loudness (variant gain offsets kept).
    base_target = float((params.get("normalise") or {}).get("target", -20.0))
    level = base_target
    finals = _chain_all(mixes, params, level, loop)
    short = [rep["achieved"] - plan.gain_db for (plan, *_), (_, rep) in zip(mixes, finals)
             if rep.get("shortfallDb", 0) > 0.1]
    if short:
        level = round(min(short), 2)
        finals = _chain_all(mixes, params, level, loop)
        warnings.append(f"âm quá ngắn hoặc quá nhọn để đạt mức chung {base_target:g}: cả id dùng mức {level:g} "
                        f"(thiếu {base_target - level:.1f} dB; bù bằng gainDb trong catalog nếu cần)")

    variants, recs = [], {}
    for (plan, mix, layer_recs, ai_ok, models, raw_qa), (final, chain_rep) in zip(mixes, finals):
        ogg_bytes = None
        if want_ogg:
            ceiling = float((chain_rep["params"].get("limiter") or {}).get("ceilingDbtp", -1.0))
            final, ogg_bytes, ogg_gain, ogg_tp = ogg_safe(final, ceiling, SR, quality)
            chain_rep["oggTruePeakDbtp"] = ogg_tp
            if ogg_gain:
                chain_rep["oggSafetyGainDb"] = ogg_gain
        final_qa = measure.summary(final, SR)
        n = plan.n
        master_rel = f"masters/{data['id']}-v{n}.wav"
        write_wav(out / master_rel, final)
        runtime_rel = f"{stem}-{n}.ogg"
        rec = {
            "id": data["id"], "game": data["game"], "variant": n, "renderVariant": n, "date": date,
            "recipe": f"recipes/{data['id']}.json", "recipeHash": rhash, "seed": plan.seed, "run": out.name,
            "master": master_rel, "masterSha256": ledger.sha256_file(out / master_rel),
            "durationMs": final_qa["durationMs"], "sampleRate": SR, "channels": channels,
            "layers": layer_recs, "chain": chain_rep["summary"] + f", soxr{SR // 1000}k, {'mono' if channels == 1 else 'stereo'}",
            "chainParams": chain_rep["params"], "tools": tools, "models": sorted(set(models)), "aiSteps": [],
            "aiInputAllowed": ai_ok, "rawQa": f"render.json#variants/{n - 1}/raw", "review": None,
        }
        if want_ogg:
            (out / "runtime" / runtime_rel).parent.mkdir(parents=True, exist_ok=True)
            (out / "runtime" / runtime_rel).write_bytes(ogg_bytes)
            rec["sha256"] = ledger.sha256_file(out / "runtime" / runtime_rel)
            recs[runtime_rel] = rec
        else:
            rec["sha256"] = rec["masterSha256"]
            recs[master_rel] = rec
        variants.append({"variant": n, "plan": plan.to_json(), "master": master_rel,
                         "runtime": runtime_rel if want_ogg else None, "raw": raw_qa, "final": final_qa,
                         "layersRawQa": {ly["id"]: ly["rawQa"] for ly in layer_recs if ly.get("rawQa")},
                         "chain": chain_rep, "aiInputAllowed": ai_ok})

    rows = list(all_rows.values())
    report = {
        "engine": ENGINE, "game": data["game"], "id": data["id"], "run": out.name, "date": date,
        "recipeHash": rhash, "seed": plans[0].seed if plans else None, "count": len(plans),
        "limits": limit_src, "spec": spec_info["path"] if spec_info else None, "warnings": warnings, "chainParams": params, "idLevel": level, "loop": loop,
        "channels": channels,
        "exportStem": stem, "licenceCopies": copies, "tools": tools, "variants": variants,
    }
    (out / "recipe.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "render.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    ledger.write_sources(out / "SOURCES.json", recs)
    rows_path = out / "licences.rows.jsonl"
    rows_path.unlink(missing_ok=True)
    ledger.append_rows(rows_path, rows)
    frag = {"version": 2, "sounds": {data["id"]: {
        "files": [v["runtime"] for v in variants] if want_ogg else [v["master"] for v in variants],
        "durationMs": [round(v["final"]["durationMs"]) for v in variants], "loop": loop}}}
    (out / "manifest.fragment.json").write_text(json.dumps(frag, indent=2) + "\n", encoding="utf-8")
    return RunResult(out, report, recs, rows)
