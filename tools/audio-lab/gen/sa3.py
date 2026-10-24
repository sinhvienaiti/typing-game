"""Stable Audio 3 wrapper: spec card -> job -> candidates with records and licence rows (§5.1 step 2).

  run.sh sa3 plan  --spec specs/<game>/<id>.yaml [--variant E ...] [--seeds 1001-1006] [--seconds 2]
  run.sh sa3 run   --spec specs/<game>/<id>.yaml --run sa3-r2 [...]      # generate, then records
  run.sh sa3 records --raw ~/AudioLab/work/<game>/<id>/<run>/raw --spec ...   # records from batch reports

The model runs through ~/AudioLab/models/sa3-meta/tools/batch_run.sh (sa3_batch.py: models stay
loaded, bit-identical to the ./sa3 CLI). Every job writes "raw_float": the 16-bit writer of the CLI
hard-clips |x| > 1, so L1 reads the unclipped float copy (<name>.f32.wav). Only the durations in
ALLOWED_SECONDS are accepted: 0.5 s and 1.5 s give full-scale noise in this build (batch 0b trial).
cfg defaults to 1.0 (plan §5.1): a negative prompt is then written down, never applied.

Per candidate: <name>.wav, <name>.f32.wav and <name>.json (audiolab.sa3.candidate/1: prompt, seed,
steps, cfg, duration, model + revision, weights and file sha256, raw stats, licence rows).
Licence rows (model, Stability registration, Gemma terms) go to <run>/licences.rows.jsonl through
build.ledger.append_rows; build.sources reads them back from the record of a `gen` layer.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import yaml

from common import env

ALLOWED_SECONDS = (1.0, 2.0, 3.0, 10.0)
RECORD_SCHEMA = "audiolab.sa3.candidate/1"
META = env.MODELS / "sa3-meta"
INSTALL_RECORD = META / "install-record.json"
BATCH_RUN = META / "tools" / "batch_run.sh"
LICENCES = env.HOME / "licences"
STABILITY = "LicenseRef-Stability-Community-2024"
STABILITY_URL = "https://stability.ai/community-license-agreement"
GEMMA = "LicenseRef-Gemma-Terms-of-Use"
GEMMA_URL = "https://ai.google.dev/gemma/terms"
DIT_WEIGHTS = {"sm-sfx": "dit_sm-sfx_f16.npz", "sm-music": "dit_sm-music_f16.npz"}
SHARED_WEIGHTS = ("same_s_decoder_f32.npz", "t5gemma_f16.npz")
_KEYED = re.compile(r"^([A-Z][0-9]?)\s*:\s*(.+)$", re.S)
# DECISIONS Q2 (TK 22.1: no temple wood block in Lời Gọi): words that give the hollow, high, pitched "tốc", for every
# id of the game, and the call-chop prompts B, D (B s1002 rated 2/5, the lowest of the id, batch 0b)
FORBIDDEN_TERMS: dict[str, tuple[str, ...]] = {
    "typing-defense": (r"\btok\b", r"\btốc\b", r"hollow\s+tube", r"temple\s+block", r"wooden\s+fish", r"\bmõ\b"),
}
FORBIDDEN_KEYS: dict[tuple[str, str], tuple[str, ...]] = {("typing-defense", "call-chop"): ("B", "D")}


class Sa3Error(ValueError):
    pass


def check_prompts(card: dict, prompts: dict[str, str]) -> None:
    """Refuse a prompt the decisions log forbids for this game or id (DECISIONS Q2)."""
    game, sid = card.get("game") or "", card.get("id") or ""
    keys = [k for k in prompts if k in FORBIDDEN_KEYS.get((game, sid), ())]
    if keys:
        raise Sa3Error(f"{sid}: prompt {', '.join(keys)} bị cấm (DECISIONS Q2, TK 22.1: tiếng gõ rỗng, cao giống mõ)")
    for k, text in prompts.items():
        for pat in FORBIDDEN_TERMS.get(game, ()):
            if re.search(pat, text, re.I):
                raise Sa3Error(f"{sid}: prompt {k} có cụm bị cấm /{pat}/ (DECISIONS Q2, TK 22.1): {text[:80]}")


# ---------------------------------------------------------------- install + model identity

def load_install(path: Path = INSTALL_RECORD) -> dict:
    if not Path(path).is_file():
        raise Sa3Error(f"chưa có {path}: Stable Audio 3 chưa cài (mục 10.1)")
    return json.loads(Path(path).read_text("utf-8"))


def model_id(install: dict) -> str:
    """'<repo>@<revision>' as licence_check looks it up (model:<repo>@<revision>)."""
    return f"{install['hf']['repo']}@{install['hf']['revision']}"


def weights_sha(install: dict, dit: str) -> dict[str, str]:
    by_name = {Path(w["file"]).name: w["sha256"] for w in install["weights"]}
    names = (DIT_WEIGHTS[dit], *SHARED_WEIGHTS)
    return {n: by_name[n] for n in names if n in by_name}


# ---------------------------------------------------------------- spec card -> job

def read_card(path: Path | str) -> dict:
    card = yaml.safe_load(Path(path).read_text("utf-8")) or {}
    if not card.get("id") or not card.get("game"):
        raise Sa3Error(f"{path}: thẻ spec thiếu id hoặc game")
    card["_path"] = str(Path(path).resolve())
    return card


def prompts_from_card(card: dict) -> dict[str, str]:
    """Prompt variants of the card (`prompt.variants`, "E: text" keeps its letter), else `prompt.text`."""
    p = card.get("prompt") or {}
    out: dict[str, str] = {}
    for i, v in enumerate(p.get("variants") or []):
        m = _KEYED.match(str(v).strip())
        key, text = (m.group(1), m.group(2).strip()) if m else ("ABCDEFGH"[i], str(v).strip())
        if key in out:
            raise Sa3Error(f"{card['id']}: khóa prompt {key} bị trùng")
        out[key] = text
    if not out and p.get("text"):
        out["A"] = str(p["text"]).strip()
    if not out:
        raise Sa3Error(f"{card['id']}: thẻ spec không có prompt")
    return out


def pick_seconds(card: dict, override: float | None = None) -> float:
    """Smallest allowed length that holds the card's longest version with margin (loops: 10 s)."""
    if override is not None:
        s = float(override)
        if s not in ALLOWED_SECONDS:
            raise Sa3Error(f"độ dài {s:g} s không được phép; chỉ {', '.join(f'{a:g}' for a in ALLOWED_SECONDS)} s "
                           "(0,5 s và 1,5 s cho ra nhiễu toàn thang trong bản cài này)")
        return s
    d = card.get("duration") or {}
    need = float(d.get("max_ms") or d.get("target_ms") or 1000.0) / 1000.0
    need = max(need * 1.2, need + 0.2)
    for s in ALLOWED_SECONDS:
        if s >= need:
            return s
    raise Sa3Error(f"{card['id']}: cần {need:.1f} s, dài hơn mức tạo tối đa {ALLOWED_SECONDS[-1]:g} s")


def parse_seeds(text: str) -> list[int]:
    out: list[int] = []
    for part in str(text).split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = (int(x) for x in part.split("-", 1))
            out += list(range(a, b + 1))
        else:
            out.append(int(part))
    if not out:
        raise Sa3Error("không có seed nào")
    return out


def candidate_name(sound_id: str, variant: str, seed: int, seconds: float | None = None,
                   tag_seconds: bool = False) -> str:
    sec = f"{seconds:g}s" if tag_seconds and seconds is not None else ""
    return f"{sound_id}__{variant}{sec}__s{seed}"


def build_job(card: dict, *, variants: list[str] | None = None, seeds: list[int], seconds: float | None = None,
              steps: int = 8, cfg: float = 1.0, negative: str | None = None, dit: str = "sm-sfx",
              tag_seconds: bool = False, prompts: dict[str, str] | None = None) -> dict:
    """A job for sa3_batch.py (plus an `_meta` block this wrapper keeps; the driver ignores it)."""
    allp = prompts or prompts_from_card(card)
    keys = variants or list(allp)
    missing = [k for k in keys if k not in allp]
    if missing:
        raise Sa3Error(f"{card['id']}: không có prompt {', '.join(missing)}; có {', '.join(allp)}")
    check_prompts(card, {k: allp[k] for k in keys})
    if dit not in DIT_WEIGHTS:
        raise Sa3Error(f"dit {dit!r} không có; chọn {', '.join(DIT_WEIGHTS)}")
    if not 1 <= int(steps) <= 100:
        raise Sa3Error("steps phải trong 1–100")
    secs = pick_seconds(card, seconds)
    items = [{"prompt": allp[k], "seed": int(s), "seconds": secs,
              "name": candidate_name(card["id"], k, int(s), secs, tag_seconds)} for k in keys for s in seeds]
    names = [it["name"] for it in items]
    if len(set(names)) != len(names):
        raise Sa3Error("tên ứng viên bị trùng (trùng seed?)")
    apply_neg = negative if (negative and float(cfg) != 1.0) else None
    return {"dit": dit, "steps": int(steps), "cfg": float(cfg), "negative_prompt": apply_neg, "raw_float": True,
            "items": items,
            "_meta": {"id": card["id"], "game": card["game"], "spec_card": card.get("_path"),
                      "variants": {k: allp[k] for k in keys}, "seconds": secs,
                      "negative_written_not_applied": negative if negative and apply_neg is None else None}}


# ---------------------------------------------------------------- licence rows

def _sha(path: Path) -> str:
    from build import ledger
    return ledger.sha256_file(path)


def licence_rows(install: dict, dit: str = "sm-sfx", date: str | None = None,
                 licences: Path = LICENCES) -> tuple[list[dict], dict[str, str]]:
    """(rows, copies): model row (generate) + acceptance rows for the Stability registration and the
    Gemma terms (T5Gemma text encoder), as audiolab.licence/1 rows; copies = row key -> dated text."""
    from build import ledger

    date = date or ledger.today()
    reg = licences / "stability-registration.txt"
    lic_text = sorted(licences.glob("stability-community-license-*.txt"))
    gemma_text = sorted(licences.glob("gemma-terms-of-use-*.txt"))
    if not reg.is_file() or not lic_text:
        raise Sa3Error(f"thiếu bản đăng ký Stability hoặc bản giấy phép trong {licences} (mục 10.1)")
    w = weights_sha(install, dit)
    repo, rev = install["hf"]["repo"], install["hf"]["revision"]
    model = ledger.model_row(repo, rev, STABILITY, STABILITY_URL, w[DIT_WEIGHTS[dit]], "generate", date,
                             licenceCopy=f"licences/{lic_text[-1].name}", weights=w,
                             code=f"{install['repo']['url']}@{install['repo']['commit']}")
    acc = {"schema": ledger.LICENCE_SCHEMA_ID, "kind": "acceptance", "key": f"acceptance:{STABILITY}@2024-07-05",
           "licence": STABILITY, "licenceVersion": "2024-07-05", "licenceUrl": STABILITY_URL,
           "who": "chủ dự án (cá nhân)", "file": "licences/stability-registration.txt",
           "licenceCopy": "licences/stability-registration.txt", "sha256": _sha(reg), "date": date}
    rows, copies = [model, acc], {model["key"]: str(lic_text[-1]), acc["key"]: str(reg)}
    if gemma_text:
        g = {"schema": ledger.LICENCE_SCHEMA_ID, "kind": "acceptance", "key": f"acceptance:{GEMMA}@{gemma_text[-1].stem}",
             "licence": GEMMA, "licenceUrl": GEMMA_URL, "who": "chủ dự án (cá nhân)",
             "file": f"licences/{gemma_text[-1].name}", "licenceCopy": f"licences/{gemma_text[-1].name}",
             "sha256": _sha(gemma_text[-1]), "date": date}
        rows.append(g)
        copies[g["key"]] = str(gemma_text[-1])
    for r in rows:
        errs = ledger.schema_errors("licences", r)
        if errs:
            raise Sa3Error(f"dòng sổ {r['key']} sai schema: {errs}")
    return rows, copies


# ---------------------------------------------------------------- run + records

def writer_clip_runs(x: np.ndarray) -> dict:
    """Runs of >= 3 samples at >= 0.999 FS in the 16-bit file (the CLI writer's hard clip)."""
    from critic.hygiene import runs
    full = samples = 0
    for ch in range(x.shape[1]):
        s, n = runs(np.abs(x[:, ch]) >= 0.999)
        keep = n >= 3
        full += int(keep.sum())
        samples += int(n[keep].sum())
    return {"runs_ge3_at_0999": full, "samples": samples}


def raw_stats(wav16: Path, f32: Path) -> dict:
    import soundfile as sf
    x16, sr = sf.read(str(wav16), always_2d=True)
    xf, _ = sf.read(str(f32), always_2d=True)
    corr = None
    if xf.shape[1] == 2 and np.std(xf[:, 0]) > 0 and np.std(xf[:, 1]) > 0:
        corr = round(float(np.corrcoef(xf[:, 0], xf[:, 1])[0, 1]), 4)
    return {"sr": int(sr), "channels": int(x16.shape[1]), "frames": int(x16.shape[0]),
            "peak_abs_float": round(float(np.abs(xf).max()), 4), "writer_clip_16bit": writer_clip_runs(x16),
            "stereo_corr": corr, "dual_mono": bool(xf.shape[1] == 2 and np.array_equal(xf[:, 0], xf[:, 1]))}


def write_records(report: dict, job: dict, raw_dir: Path, install: dict, *, run: str,
                  report_path: Path, rows: list[dict], copies: dict[str, str]) -> list[Path]:
    """One <name>.json per generated item (never overwrites an existing record)."""
    meta = job.get("_meta") or {}
    inv = {v: k for k, v in (meta.get("variants") or {}).items()}
    dit = report.get("dit") or job["dit"]
    out = []
    for it in report["items"]:
        wav = raw_dir / Path(it["path"]).name
        f32 = wav.with_name(wav.stem + ".f32.wav")
        rec_path = wav.with_suffix(".json")
        if rec_path.exists() or not wav.is_file():
            continue
        if not f32.is_file():
            raise Sa3Error(f"{wav.name}: thiếu bản float {f32.name} (job phải có raw_float)")
        rec = {
            "schema": RECORD_SCHEMA, "id": meta.get("id"), "game": meta.get("game"), "run": run,
            "candidate": wav.stem, "variant": inv.get(it["prompt"]), "prompt": it["prompt"],
            "negative_prompt": report.get("negative_prompt"),
            "negative_prompt_written_not_applied": meta.get("negative_written_not_applied"),
            "seed": int(it["seed"]), "steps": int(report["steps"]), "cfg": float(report["cfg"]),
            "seconds": float(it["seconds"]),
            "model": {"id": model_id(install), "repo": install["hf"]["repo"], "revision": install["hf"]["revision"],
                      "dit": dit, "decoder": report.get("decoder"), "dtype": "fp16",
                      "weights_sha256": weights_sha(install, dit),
                      "code": f"{install['repo']['url']}@{install['repo']['commit']}",
                      "mlx": install["venv"]["key_versions"].get("mlx"),
                      "tool": "sa3_batch.py (resident models, bit-identical to ./sa3)", "licence": STABILITY},
            "timing_s": {"sample": it.get("sample_s"), "decode": it.get("decode_s"), "total": it.get("total_s")},
            "batch_report": str(report_path), "spec_card": meta.get("spec_card"),
            "created": dt.datetime.fromtimestamp(wav.stat().st_mtime).astimezone().isoformat(timespec="seconds"),
            "files": {"wav16": {"path": str(wav), "sha256": _sha(wav),
                                "note": "CLI-identical 16-bit PCM; hard-clipped at |x| > 1 by the writer"},
                      "f32": {"path": str(f32), "sha256": _sha(f32), "note": "same samples, unclipped float32"}},
            "raw_stats": raw_stats(wav, f32),
            "licence": {"rows": rows, "copies": copies, "ledger": str(raw_dir.parent / "licences.rows.jsonl")},
        }
        rec_path.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", "utf-8")
        out.append(rec_path)
    return out


def _runner(job_path: Path, out_dir: Path) -> int:
    """batch_run.sh JOB OUTDIR (sets HF offline, no token; one resident-model process)."""
    if not BATCH_RUN.is_file():
        raise Sa3Error(f"không thấy {BATCH_RUN}")
    environ = {k: v for k, v in os.environ.items() if k not in env.TOKEN_VARS}
    environ.update({"HF_HUB_OFFLINE": "1", "HF_HUB_DISABLE_IMPLICIT_TOKEN": "1"})
    proc = subprocess.run(["bash", str(BATCH_RUN), str(job_path), str(out_dir)], env=environ,
                          capture_output=True, text=True)
    sys.stdout.write(proc.stdout)
    if proc.returncode:
        sys.stderr.write(proc.stderr)
    return proc.returncode


def run_job(job: dict, run_dir: Path, *, install: dict | None = None, runner=_runner, date: str | None = None,
            licences: Path = LICENCES) -> dict:
    """Generate the job into <run_dir>/raw, write records and licence rows. Skips existing candidates."""
    from build import ledger

    install = install or load_install()
    raw = Path(run_dir) / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    todo = [it for it in job["items"] if not ((raw / f"{it['name']}.wav").is_file() and (raw / f"{it['name']}.json").is_file())]
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    rows, copies = licence_rows(install, job["dit"], date, licences)
    ledger.append_rows(Path(run_dir) / "licences.rows.jsonl", rows)
    result = {"todo": len(todo), "skipped": len(job["items"]) - len(todo), "records": [], "report": None}
    if not todo:
        return result
    driver_job = {k: v for k, v in job.items() if k != "_meta"} | {"items": todo, "raw_float": True}
    job_path = raw / f"_job-{stamp}.json"
    job_path.write_text(json.dumps({**driver_job, "_meta": job.get("_meta")}, indent=1, ensure_ascii=False), "utf-8")
    tmp = raw / f"_batch-{stamp}"
    tmp.mkdir()
    rc = runner(job_path, tmp)
    if rc:
        raise Sa3Error(f"sa3_batch dừng với mã {rc}; xem {tmp}/time.txt và run.log")
    rep = json.loads((tmp / "report.json").read_text("utf-8"))
    for it in rep["items"]:
        name = Path(it["path"]).name
        for f in (name, name[:-4] + ".f32.wav"):
            if (tmp / f).is_file():
                shutil.move(str(tmp / f), str(raw / f))
        it["path"] = str(raw / name)
    rep_path = raw / f"_batch-report-{stamp}.json"
    rep_path.write_text(json.dumps(rep, indent=1, ensure_ascii=False), "utf-8")
    for f, dst in (("run.log", f"_run-{stamp}.log"), ("time.txt", f"_time-{stamp}.txt")):
        if (tmp / f).is_file():
            shutil.move(str(tmp / f), str(raw / dst))
    shutil.rmtree(tmp, ignore_errors=True)
    result["report"] = str(rep_path)
    result["records"] = [str(p) for p in write_records(rep, job, raw, install, run=Path(run_dir).name,
                                                       report_path=rep_path, rows=rows, copies=copies)]
    result["loop_s"] = rep.get("loop_s")
    result["warm_mean_s"] = rep.get("warm_mean_s")
    result["mlx_peak_gb"] = rep.get("mlx_peak_gb_total")
    return result


def read_record(path: Path | str) -> dict:
    """Candidate record of this wrapper or of the batch 0b trial (both carry files.f32/wav16)."""
    rec = json.loads(Path(path).read_text("utf-8"))
    if not str(rec.get("schema", "")).startswith(("audiolab.sa3.candidate/", "audiolab.sa3-trial.candidate/")):
        raise Sa3Error(f"{path}: không phải hồ sơ ứng viên Stable Audio 3")
    return rec


# ---------------------------------------------------------------- CLI

def _job_from_args(a) -> tuple[dict, dict]:
    card = read_card(a.spec)
    prompts = prompts_from_card(card)
    for kv in a.prompt or []:
        k, _, text = kv.partition("=")
        if not text or not re.fullmatch(r"[A-Z][0-9]?", k):
            raise Sa3Error(f"--prompt cần dạng KHÓA=văn bản (vd. E=wind in pines), có {kv!r}")
        prompts[k] = text.strip()
    job = build_job(card, variants=a.variant, seeds=parse_seeds(a.seeds), seconds=a.seconds, steps=a.steps,
                    cfg=a.cfg, negative=a.negative, dit=a.dit, tag_seconds=a.tag_seconds, prompts=prompts)
    return card, job


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="sa3", description="Stable Audio 3: tạo ứng viên từ thẻ spec (mục 5.1).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("plan", "run"):
        p = sub.add_parser(name, help="in job" if name == "plan" else "tạo ứng viên, ghi hồ sơ và sổ")
        p.add_argument("--spec", required=True, help="specs/<game>/<id>.yaml")
        p.add_argument("--variant", action="append", help="khóa prompt (A, B, E...); mặc định mọi prompt của thẻ")
        p.add_argument("--prompt", action="append", help="thêm prompt KHÓA=văn bản (không ghi vào thẻ)")
        p.add_argument("--seeds", default="1001-1006")
        p.add_argument("--seconds", type=float, help=f"độ dài tạo, chỉ {ALLOWED_SECONDS}")
        p.add_argument("--steps", type=int, default=8)
        p.add_argument("--cfg", type=float, default=1.0)
        p.add_argument("--negative", help="negative prompt (chỉ có tác dụng khi cfg khác 1)")
        p.add_argument("--dit", default="sm-sfx")
        p.add_argument("--tag-seconds", action="store_true", help="ghi độ dài vào tên (E2s__s1001)")
        if name == "run":
            p.add_argument("--run", required=True, help="tên lần chạy: ~/AudioLab/work/<game>/<id>/<run>")
    r = sub.add_parser("records", help="ghi lại hồ sơ từ báo cáo lô (không tạo âm)")
    r.add_argument("--run-dir", required=True)
    r.add_argument("--spec", required=True)
    a = ap.parse_args(argv)
    env.apply()
    try:
        if a.cmd == "plan":
            _, job = _job_from_args(a)
            print(json.dumps(job, indent=1, ensure_ascii=False))
            return 0
        if a.cmd == "run":
            card, job = _job_from_args(a)
            res = run_job(job, env.work_dir(card["game"], card["id"], a.run))
            print(json.dumps({k: v for k, v in res.items() if k != "records"} | {"records": len(res["records"])},
                             ensure_ascii=False))
            return 0
        card = read_card(a.spec)
        install = load_install()
        run_dir = Path(a.run_dir).expanduser()
        rows, copies = licence_rows(install)
        n = 0
        for rp in sorted((run_dir / "raw").glob("_batch-report-*.json")):
            rep = json.loads(rp.read_text("utf-8"))
            meta = {"id": card["id"], "game": card["game"], "spec_card": card["_path"],
                    "variants": prompts_from_card(card)}
            n += len(write_records(rep, {"dit": rep["dit"], "_meta": meta}, run_dir / "raw", install,
                                   run=run_dir.name, report_path=rp, rows=rows, copies=copies))
        print(f"{n} hồ sơ mới")
        return 0
    except Sa3Error as exc:
        print(f"sa3: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
