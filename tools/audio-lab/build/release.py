"""Promote chosen variants of a run into an art-src/public tree (staging by default).

Writes, for one id: public/<stem>-<k>.ogg, art-src/masters/<id>/<id>-v<k>.wav, SOURCES.json records,
licences.jsonl rows + dated licence copies, recipes/<id>.json, review/qa/<id>.build.json,
manifest.json (v2) and CREDITS.md. Replaces the id's previous release in that tree.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

from build import ledger


def staging_public(game: str) -> Path:
    from common import env

    p = env.STAGING / game / "public" / "assets" / game / "audio"
    p.mkdir(parents=True, exist_ok=True)
    return p


def _update_manifest(path: Path, sound_id: str, files: list[str], durations: list[int], loop: bool) -> None:
    man = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
    sounds = {}
    for k, v in (man.get("sounds") or {}).items():   # v1 -> v2: id -> [paths] becomes {"files": [...]}
        sounds[k] = {"files": list(v)} if isinstance(v, list) else v
    sounds[sound_id] = {"files": files, "durationMs": durations, "loop": loop}
    out = {"version": 2, "sounds": dict(sorted(sounds.items()))}
    if man.get("music"):
        out["music"] = man["music"]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def release(run_dir: Path, variants: list[int] | None, art_src: Path, public: Path, date: str | None = None) -> dict:
    run_dir, art_src, public = Path(run_dir), Path(art_src), Path(public)
    report = json.loads((run_dir / "render.json").read_text(encoding="utf-8"))
    run_recs = ledger.records(ledger.read_sources(run_dir / "SOURCES.json"))
    by_variant = {r["renderVariant"]: (k, r) for k, r in run_recs.items()}
    chosen = variants or sorted(by_variant)
    missing = [v for v in chosen if v not in by_variant]
    if missing:
        raise ValueError(f"run {run_dir.name} has no variant(s) {missing}")
    sid, stem = report["id"], report["exportStem"]
    date = date or ledger.today()

    # Drop the id's previous release in this tree.
    src_path = art_src / "SOURCES.json"
    data = ledger.read_sources(src_path)
    # Two recipes with one export path would overwrite each other's runtime files (batch 1c review: hurt.breach and
    # hurt.breach.b2 both on sfx/alerts/hurt-breach, 24 masters for 18 ogg files): refused before anything is written.
    for key, rec in ledger.records(data).items():
        if rec.get("id") != sid and key.rsplit("-", 1)[0] == stem:
            raise ValueError(f"đường xuất {stem} đã thuộc công thức '{rec.get('id')}' ({key}); "
                             f"công thức '{sid}' cần export.path riêng")
    for key, rec in list(ledger.records(data).items()):
        if rec.get("id") == sid:
            (public / key).unlink(missing_ok=True)
            if rec.get("master"):
                (art_src / rec["master"]).unlink(missing_ok=True)
            del data[key]

    files, durations, qa = [], [], []
    variants_qa = {v["variant"]: v for v in report["variants"]}
    for k, rv in enumerate(chosen, 1):
        old_key, rec = by_variant[rv]
        new_key = f"{stem}-{k}.ogg" if old_key.endswith(".ogg") else f"{stem}-{k}.wav"
        src_file = run_dir / ("runtime" if old_key.endswith(".ogg") else "") / old_key
        (public / new_key).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src_file, public / new_key)
        master_rel = f"masters/{sid}/{sid}-v{k}.wav"
        (art_src / master_rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(run_dir / rec["master"], art_src / master_rel)
        new = {**rec, "variant": k, "renderVariant": rv, "master": master_rel, "date": date,
               "rawQa": f"review/qa/{sid}.build.json#variants/{k - 1}/raw"}
        data[new_key] = new
        files.append(new_key)
        durations.append(round(rec["durationMs"]))
        v = variants_qa[rv]
        qa.append({"variant": k, "renderVariant": rv, "raw": v["raw"], "final": v["final"], "chain": v["chain"]})
    ledger.write_sources(src_path, data)

    rows = ledger.read_rows(run_dir / "licences.rows.jsonl")
    added = ledger.append_rows(art_src / "licences.jsonl", rows)
    copies = {k: Path(p) for k, p in (report.get("licenceCopies") or {}).items()}
    copied = ledger.copy_licence_texts(rows, copies, art_src)
    recipe_dst = art_src / "recipes" / f"{sid}.json"
    recipe_dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(run_dir / "recipe.json", recipe_dst)
    qa_dst = art_src / "review" / "qa" / f"{sid}.build.json"
    qa_dst.parent.mkdir(parents=True, exist_ok=True)
    qa_dst.write_text(json.dumps({"id": sid, "run": report["run"], "recipeHash": report["recipeHash"],
                                  "variants": qa}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    _update_manifest(public / "manifest.json", sid, files, durations, bool(report.get("loop")))
    credits = ledger.write_credits(art_src)
    return {"id": sid, "files": files, "rowsAdded": added, "licenceCopies": copied,
            "artSrc": str(art_src), "public": str(public), "credits": str(credits) if credits else None}
