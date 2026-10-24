"""Resolve a recipe layer source to audio (48 kHz) plus its provenance."""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import soundfile as sf

from build import dsp, ledger, policy, synth


@dataclass
class Loaded:
    audio: np.ndarray                 # (n, ch) float64 at 48 kHz
    kind: str                         # library | file | synth | gen | sampler
    layer_meta: dict                  # goes into the SOURCES.json layer record
    rows: list[dict] = field(default_factory=list)          # licences.jsonl rows to add
    copies: dict[str, Path] = field(default_factory=dict)   # row key -> licence text on disk
    sha256: str | None = None
    raw_qa: dict | None = None        # §4.3.1 clip test on the stored source file(s); None for synth


_AUDIO_CACHE: dict[tuple[str, float], np.ndarray] = {}
_SCAN_CACHE: dict[tuple, dict] = {}
RAW_QA_CHECK = "clip trong file gốc (mục 4.3.1): 3 mẫu ≥ 0,999 FS hoặc 4 mẫu đỉnh phẳng"


def clip_scan_file(path: Path, window_s: list | tuple | None = None) -> dict:
    """§4.3.1 clip test on a source exactly as stored (before resampling, gain or mixing), cached.

    Resampling and normalising hide a flat top below 0.999 FS (the Stable Audio 3 PCM 16-bit case),
    so the test runs here, per layer, not on the mix."""
    path = Path(path)
    key = (str(path), path.stat().st_mtime, tuple(window_s) if window_s else None)
    if key not in _SCAN_CACHE:
        from critic.hygiene import clip_scan, source_clip_ok

        info = sf.info(str(path))
        data, file_sr = sf.read(str(path), always_2d=True, dtype="float64")
        if window_s:
            a, b = window_s
            data = data[int(a * file_sr): int(b * file_sr)]
        scan = clip_scan(data, info.subtype)
        _SCAN_CACHE[key] = {"file": path.name, "subtype": info.subtype, "fullRuns": scan["full_runs"],
                            "flatRuns": scan["flat_runs"], "ok": source_clip_ok(scan)}
    return dict(_SCAN_CACHE[key])


def raw_qa(items: list[dict]) -> dict:
    return {"check": RAW_QA_CHECK, "verdict": "PASS" if all(i["ok"] for i in items) else "BLOCK", "files": items}


def read_audio(path: Path, sr: int = dsp.SR) -> np.ndarray:
    key = (str(path), path.stat().st_mtime)
    if key not in _AUDIO_CACHE:
        data, file_sr = sf.read(str(path), always_2d=True, dtype="float64")
        _AUDIO_CACHE[key] = dsp.resample(data, file_sr, sr)
    return _AUDIO_CACHE[key]


def _ledger_row(ref, ledger_rows: dict[str, dict]) -> dict:
    if isinstance(ref, dict):
        return ref
    if ref not in ledger_rows:
        raise LookupError(f"ledger key {ref!r} not found in licences.jsonl")
    return ledger_rows[ref]


def _gen_record(g: dict, path: Path, sha: str, meta: dict) -> tuple[list[dict], dict[str, Path]]:
    """Licence rows of a model output from its candidate record (gen/sa3.py), checked by sha256.

    The record must describe this very file (wav16 or float copy) and name the same model; its rows
    (model, Stability registration, Gemma terms) and dated copies travel with the layer (§10.6)."""
    if not g.get("record"):
        return [], {}
    rp = Path(str(g["record"])).expanduser()
    rec = json.loads(rp.read_text(encoding="utf-8"))
    files = rec.get("files") or {}
    if sha not in {f.get("sha256") for f in files.values() if isinstance(f, dict)}:
        raise ValueError(f"{path.name}: sha256 không khớp hồ sơ {rp.name} (file đã đổi?)")
    mdl = rec.get("model") or {}
    rec_model = mdl.get("id") or (f"{mdl['repo']}@{mdl['revision']}" if mdl.get("repo") and mdl.get("revision") else None)
    if rec_model and rec_model != g["model"]:
        raise ValueError(f"{path.name}: lớp ghi mô hình {g['model']}, hồ sơ ghi {rec_model}")
    for k, rk in (("prompt", "prompt"), ("seed", "seed"), ("cfg", "cfg")):
        if k not in meta and rec.get(rk) is not None:
            meta[k] = rec[rk]
    meta["record"] = rp.name
    lic = rec.get("licence") if isinstance(rec.get("licence"), dict) else {}
    rows = [dict(r) for r in lic.get("rows") or [] if isinstance(r, dict)]
    copies = {k: Path(v) for k, v in (lic.get("copies") or {}).items()}
    if not rows and str(mdl.get("repo", "")).startswith("stabilityai/stable-audio-3"):
        from gen import sa3      # records of the batch 0b trial predate the rows: same model, same licence
        r2, c2 = sa3.licence_rows(sa3.load_install(), mdl.get("dit") or "sm-sfx")
        rows, copies = r2, {k: Path(v) for k, v in c2.items()}
    return rows, copies


SAMPLER_TOOL = "audiolab-sampler"
_SAMPLER_CACHE: dict[str, tuple[np.ndarray, dict]] = {}


def _sampler_render(cfg: dict, libraries: Path, sr: int) -> tuple[np.ndarray, dict]:
    """Render a sampler phrase in-process (sampler/engine.py), cached per config."""
    key = json.dumps({"cfg": cfg, "lib": str(libraries), "sr": sr}, sort_keys=True)
    if key in _SAMPLER_CACHE:
        return _SAMPLER_CACHE[key]
    from sampler.engine import Sampler, notes_from_json, parse_note_spec
    from sampler.instrument import from_folder, from_index, load_index

    s = Sampler(sr=sr, max_shift=float(cfg.get("maxShift", 3.0)), rr_mode=cfg.get("rr", "cycle"),
                seed=int(cfg.get("seed", 0)), veltrack=float(cfg.get("veltrack", 0.5)))
    tuning = cfg.get("tuning", "auto")
    index = None
    names = cfg.get("instrument") or []
    names = [names] if isinstance(names, str) else list(names)
    if cfg.get("instrumentDir"):              # a sample folder inside the libraries tree
        folder = libraries / cfg["instrumentDir"]
        s.add(from_folder(folder, pitched=cfg.get("pitched"), octave_offset=int(cfg.get("octaveOffset", 0))),
              cfg.get("instrumentName") or "dir")
    bpm = cfg.get("bpm")
    if "notes" in cfg and isinstance(cfg["notes"], str):
        notes = parse_note_spec(cfg["notes"], bpm)
    else:
        notes = notes_from_json(list(cfg.get("notes") or []), bpm)
    first = names[0] if names else None
    for n in notes:
        n.instrument = n.instrument or first
    for name in dict.fromkeys([*names, *(n.instrument for n in notes if n.instrument)]):
        if name not in s.instruments:
            index = index or load_index(libraries / "index.json")
            s.add(from_index(name, index, root=libraries, tuning=tuning), name)
    length = cfg.get("lengthS")
    r = s.render(notes, length=length, tail=cfg.get("tail", "keep" if not length else "cut"), normalize="guard")
    out = (r.audio.astype(np.float64), r.report)
    _SAMPLER_CACHE[key] = out
    return out


def _load_sampler(cfg: dict, libraries: Path, sr: int) -> Loaded:
    """A sampler phrase as one layer: notes rendered from CC0 multisamples (§3.2, §8.2).

    Either renders in-process ({instrument, notes, ...}) or reads a prior render ({render: x.wav}
    with the sampler's x.json report next to it). Every sample the phrase used gets its own
    source + library row, so licence_check sees each one (§10.6)."""
    if cfg.get("render"):
        path = Path(cfg["render"]).expanduser()
        rep_path = path.with_suffix(".json")
        if not rep_path.is_file():
            raise FileNotFoundError(f"sampler render {path} has no report {rep_path.name}")
        report = json.loads(rep_path.read_text(encoding="utf-8"))
        audio = read_audio(path, sr)
        render_sha = ledger.sha256_file(path)
    else:
        audio, report = _sampler_render(cfg, libraries, sr)
        render_sha = None
    rows, copies, subs, lics = [], {}, [], set()
    lib_root = libraries.resolve()
    for src in report.get("sources") or []:
        rel = str(src.get("file") or "")
        p = Path(rel)
        if p.is_absolute():
            try:
                rel = p.resolve().relative_to(lib_root).as_posix()
            except ValueError as e:
                raise LookupError(f"sampler sample {rel} is outside {libraries}; give it a ledger row") from e
        src_row, lib_row, copy = ledger.library_rows(libraries, rel)
        if src.get("sha256") and src["sha256"] != src_row["sha256"]:
            raise ValueError(f"sampler sample {rel}: sha256 differs from the index (library changed?)")
        rows += [src_row, lib_row]
        copies[src_row["key"]] = copy
        copies[lib_row["key"]] = copy
        lics.add(src_row["licence"])
        subs.append({"source": rel, "sourceSha256": src_row["sha256"], "ledgerKey": src_row["key"],
                     "licence": src_row["licence"]})
    if not subs:
        raise LookupError("sampler layer used no library sample")
    notes = [{k: n.get(k) for k in ("instrument", "start", "midi", "note", "key", "velocity", "shift_st", "tune_cents")}
             for n in report.get("notes") or []]
    meta = {"kind": "sampler", "tool": SAMPLER_TOOL, "licence": lics.pop() if len(lics) == 1 else "mixed",
            "instruments": sorted((report.get("instruments") or {}).keys()), "notes": notes, "sources": subs}
    if render_sha:
        meta["render"] = f"{Path(cfg['render']).name} sha256:{render_sha}"
    if report.get("skipped"):
        meta["skipped"] = report["skipped"]
    # every sample as stored in the library (the phrase itself is our code's mix)
    qa = raw_qa([clip_scan_file(libraries / sub["source"]) for sub in subs])
    return Loaded(audio, "sampler", meta, rows, copies, render_sha, qa)


def load(source: dict, *, libraries: Path, synth_seed: int, ledger_rows: dict[str, dict] | None = None,
         sr: int = dsp.SR) -> Loaded:
    ledger_rows = ledger_rows or {}
    if "synth" in source:
        name, params = source["synth"], source.get("params") or {}
        audio = synth.generate(name, params, synth_seed, sr)[:, None]
        meta = {"kind": "synth", "tool": policy.SYNTH_TOOL, "generator": name, "params": params,
                "seed": int(synth_seed), "licence": policy.SYNTH_LICENCE}
        return Loaded(audio, "synth", meta)

    if "library" in source:
        rel = source["library"]
        path = libraries / rel
        if not path.is_file():
            raise FileNotFoundError(f"library file missing: {path}")
        src_row, lib_row, copy = ledger.library_rows(libraries, rel)
        meta = {"kind": "library", "source": rel, "sourceSha256": src_row["sha256"], "ledgerKey": src_row["key"],
                "licence": src_row["licence"]}
        return Loaded(read_audio(path, sr), "library", meta, [src_row, lib_row],
                      {src_row["key"]: copy, lib_row["key"]: copy}, src_row["sha256"], raw_qa([clip_scan_file(path)]))

    if "gen" in source:
        g = source["gen"]
        path = Path(g["file"]).expanduser()
        audio = read_audio(path, sr)
        if g.get("window"):
            a, b = g["window"]
            audio = audio[dsp.ms_to_n(a * 1000, sr): dsp.ms_to_n(b * 1000, sr)]
        sha = ledger.sha256_file(path)
        meta = {"kind": "gen", "tool": g["tool"], "model": g["model"], "licence": policy.canonical(g["licence"]),
                "source": path.name, "sourceSha256": sha, "aiSteps": ["generate"]}
        for k in ("prompt", "negativePrompt", "cfg", "seed", "window", "initAudio", "initNoise"):
            if k in g:
                meta[k] = g[k]
        rows, copies = _gen_record(g, path, sha, meta)
        if "stability" in meta["licence"].lower():
            meta["licenceAccepted"] = "licences/stability-registration.txt"
        if g.get("initAudio"):
            meta["aiSteps"].append("init-audio")
            init = Path(str(g["initAudio"])).expanduser()
            if init.is_file():
                meta["initAudio"] = f"{init.name} sha256:{ledger.sha256_file(init)}"
        return Loaded(audio, "gen", meta, rows, copies, sha, raw_qa=raw_qa([clip_scan_file(path, g.get("window"))]))

    if "sampler" in source:
        return _load_sampler(source["sampler"], libraries, sr)

    # Own / owner-downloaded file with an explicit ledger row (or key).
    path = Path(source["file"]).expanduser()
    row = dict(_ledger_row(source["ledger"], ledger_rows))
    sha = ledger.sha256_file(path)
    if row.get("sha256") and row["sha256"] != sha:
        raise ValueError(f"{path}: sha256 {sha} does not match ledger row {row.get('key')}")
    row.setdefault("schema", ledger.LICENCE_SCHEMA_ID)
    row.setdefault("kind", "source")
    row.setdefault("key", f"sha256:{sha}")
    row.setdefault("sha256", sha)
    row.setdefault("file", path.name)
    meta = {"kind": "file", "source": path.name, "sourceSha256": sha, "ledgerKey": row["key"],
            "licence": policy.canonical(row.get("licence"))}
    copies = {}
    if source.get("licenceText"):
        copies[row["key"]] = Path(source["licenceText"]).expanduser()
    return Loaded(read_audio(path, sr), "file", meta, [row], copies, sha, raw_qa([clip_scan_file(path)]))
