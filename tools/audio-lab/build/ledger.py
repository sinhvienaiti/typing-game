"""Licence log writers/readers: licences.jsonl rows (§10.6) and SOURCES.json records (§10.5)."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import shutil
from functools import lru_cache
from pathlib import Path

import jsonschema

from build import policy

SCHEMAS = Path(__file__).resolve().parent / "schemas"
LICENCE_SCHEMA_ID = "audiolab.licence/1"
SOURCES_VERSION = "audiolab.sources/1"


@lru_cache(maxsize=None)
def schema(name: str) -> dict:
    return json.loads((SCHEMAS / f"{name}.schema.json").read_text(encoding="utf-8"))


def validator(name: str) -> jsonschema.Draft202012Validator:
    return jsonschema.Draft202012Validator(schema(name))


def schema_errors(name: str, obj) -> list[str]:
    errs = sorted(validator(name).iter_errors(obj), key=lambda e: list(e.absolute_path))
    return [f"{'/'.join(map(str, e.absolute_path)) or '(gốc)'}: {e.message}" for e in errs]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def today() -> str:
    return dt.date.today().isoformat()


def _write_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


# ---------------------------------------------------------------- licences.jsonl

def read_rows(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    rows = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as e:
                rows.append({"_invalid": f"dòng {n}: {e}"})
    return rows


def rows_by_key(rows: list[dict]) -> dict[str, dict]:
    return {r["key"]: r for r in rows if isinstance(r, dict) and "key" in r}


def append_rows(path: Path, new_rows: list[dict]) -> int:
    """Append rows whose key is not in the ledger yet (append-only). Returns rows added."""
    for r in new_rows:
        errs = schema_errors("licences", r)
        if errs:
            raise ValueError(f"licence row {r.get('key')!r} invalid: {errs}")
    have = rows_by_key(read_rows(path))
    add = []
    for r in new_rows:
        if r["key"] in have:
            continue
        have[r["key"]] = r
        add.append(r)
    if add:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "a", encoding="utf-8") as f:
            for r in add:
                f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")
    return len(add)


@lru_cache(maxsize=8)
def _library_packs(ledger: str, mtime: float) -> tuple[dict, ...]:
    return tuple(r for r in read_rows(Path(ledger)) if "path" in r)


def library_pack(libraries: Path, rel: str) -> dict | None:
    """The pack row of ~/AudioLab/libraries/SOURCES.jsonl that holds `rel` (longest path prefix)."""
    ledger_path = libraries / "SOURCES.jsonl"
    if not ledger_path.is_file():
        return None
    best = None
    for row in _library_packs(str(ledger_path), ledger_path.stat().st_mtime):
        prefix = row["path"].rstrip("/") + "/"
        if rel.startswith(prefix) and (best is None or len(prefix) > len(best["path"]) + 1):
            best = row
    return best


def _copy_name(pack: dict) -> str:
    """kenney/impact-sounds/LICENSE-<date>.txt -> kenney-impact-sounds-LICENSE-<date>.txt (shared copies stay one file)."""
    return pack["licence_copy"].replace(" ", "-").replace("/", "-")


def library_rows(libraries: Path, rel: str) -> tuple[dict, dict, Path]:
    """(source row, library row, licence copy on disk) for one library file."""
    pack = library_pack(libraries, rel)
    if pack is None:
        raise LookupError(f"no library pack in {libraries / 'SOURCES.jsonl'} covers {rel!r}")
    lic = policy.canonical(pack["licence"])
    url = pack.get("licence_url") or policy.licence_url(lic) or pack.get("page") or pack["url"]
    copy_rel = f"licences/{_copy_name(pack)}"
    common = {
        "schema": LICENCE_SCHEMA_ID,
        "licence": lic,
        "licenceUrl": url,
        "licenceCopy": copy_rel,
        "date": pack["downloaded"],
        "commercial_ok": bool(pack["commercial_ok"]),
        "attribution_required": bool(pack["attribution_required"]),
        "ai_input_allowed": bool(pack["ai_input_allowed"]) and not rel.startswith(policy.NO_AI_PREFIX)
        and not policy.is_sonniss(pack),
        "raw_redistribution_allowed": bool(pack.get("raw_redistribution_allowed", False)),
    }
    if pack.get("attribution_text"):
        common["attribution_text"] = pack["attribution_text"]
    if pack.get("licence_version"):
        common["licenceVersion"] = str(pack["licence_version"])
    if pack.get("genai_preference"):
        common["genai_preference"] = pack["genai_preference"]
    lib_key = f"library:{pack['path']}@{pack.get('version', '?')}"
    lib_row = {**common, "kind": "library", "key": lib_key, "library": pack["library"], "pack": pack["pack"],
               "version": str(pack.get("version", "")), "url": pack["url"], "sha256": pack["sha256"]}
    if pack.get("page"):
        lib_row["page"] = pack["page"]
    path = libraries / rel
    file_sha = sha256_file(path)
    src_row = {**common, "kind": "source", "key": f"sha256:{file_sha}", "sha256": file_sha, "origin": "library",
               "library": pack["library"], "pack": pack["pack"], "packVersion": str(pack.get("version", "")),
               "file": Path(rel).name, "path": rel, "url": pack.get("page") or pack["url"],
               "author": pack.get("author", ""), "libraryKey": lib_key}
    if pack.get("year"):
        src_row["year"] = int(pack["year"])
    return src_row, lib_row, libraries / pack["licence_copy"]


def model_row(repo: str, revision: str, licence: str, licence_url: str, sha256: str, role: str,
              date: str | None = None, commercial_ok: bool | None = None, **extra) -> dict:
    lic = policy.canonical(licence)
    ok = policy.classify(lic) == "allowed" and not policy.model_denied(repo) if commercial_ok is None else commercial_ok
    row = {"schema": LICENCE_SCHEMA_ID, "kind": "model", "key": f"model:{repo}@{revision}", "repo": repo,
           "revision": revision, "licence": lic, "licenceUrl": licence_url, "sha256": sha256, "role": role,
           "date": date or today(), "commercial_ok": bool(ok), **extra}
    return row


def tool_row(name: str, version: str, licence: str, licence_url: str, sha256: str, date: str | None = None,
             **extra) -> dict:
    """A local tool (GPL tools stay local, §10.9; L7 listener licence file hash, §10.2)."""
    return {"schema": LICENCE_SCHEMA_ID, "kind": "tool", "key": f"tool:{name}@{version}", "name": name,
            "version": version, "licence": licence, "licenceUrl": licence_url, "sha256": sha256,
            "date": date or today(), **extra}


def acceptance_row(licence: str, version: str, who: str, file_rel: str, art_src: Path, licence_url: str,
                   date: str | None = None) -> dict:
    """A licence acceptance (Stability registration, Gemma terms...). `file_rel` lives in art-src/audio."""
    path = art_src / file_rel
    return {"schema": LICENCE_SCHEMA_ID, "kind": "acceptance", "key": f"acceptance:{policy.canonical(licence)}@{version}",
            "licence": policy.canonical(licence), "licenceVersion": version, "licenceUrl": licence_url,
            "who": who, "file": file_rel, "sha256": sha256_file(path), "date": date or today()}


def copy_licence_texts(rows: list[dict], copies: dict[str, Path], art_src: Path) -> list[str]:
    """Copy dated licence texts next to the ledger (art-src/audio/licences/...)."""
    done = []
    for r in rows:
        rel = r.get("licenceCopy")
        src = copies.get(r["key"])
        if not rel or src is None or not src.is_file():
            continue
        dst = art_src / rel
        if not dst.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dst)
            done.append(rel)
    return done


# ---------------------------------------------------------------- SOURCES.json

def read_sources(path: Path) -> dict:
    if not path.is_file():
        return {"$version": SOURCES_VERSION}
    return json.loads(path.read_text(encoding="utf-8"))


def write_sources(path: Path, data: dict) -> None:
    data = {"$version": SOURCES_VERSION, **{k: v for k, v in data.items() if k != "$version"}}
    errs = schema_errors("sources", data)
    if errs:
        raise ValueError(f"SOURCES.json invalid: {errs[:5]}")
    ordered = {"$version": SOURCES_VERSION, **dict(sorted((k, v) for k, v in data.items() if k != "$version"))}
    _write_atomic(path, json.dumps(ordered, ensure_ascii=False, indent=2) + "\n")


def records(data: dict) -> dict[str, dict]:
    return {k: v for k, v in data.items() if not k.startswith("$")}


def resolve_model(model: str) -> str:
    """'org/name' -> 'org/name@<revision>' from the pinned table (common/fetch_models.MODELS, §10.8).

    Never from the cache's refs/main: a later download could move it. Unknown repos stay unchanged
    (licence_check then warns that the revision is missing). Callers should pass 'repo@rev' as the
    critic logged it (critic.learned.ai_steps)."""
    if "@" in model:
        return model
    try:
        from common.fetch_models import MODELS
        rev = (MODELS.get(model) or ("",))[0]
    except Exception:  # noqa: BLE001 - outside the lab layout
        rev = ""
    return f"{model}@{rev}" if rev else model


def mark_ai_step(sources_path: Path, step: str, files: list[str] | None = None, model: str | None = None) -> int:
    """Record that an AI step (e.g. critic:audiobox) touched files; licence_check enforces ai_input_allowed.

    Call this from any tool that feeds a rendered file to a model (critic.learned.AI_STEPS gives
    step + repo@revision as the critic loaded it). Returns records changed.
    """
    model = resolve_model(model) if model else None
    data = read_sources(sources_path)
    changed = 0
    for key, rec in records(data).items():
        if files and key not in files and Path(key).name not in files:
            continue
        steps = rec.setdefault("aiSteps", [])
        if step not in steps:
            steps.append(step)
            changed += 1
        if model:
            models = rec.setdefault("models", [])
            if model not in models:
                models.append(model)
    write_sources(sources_path, data)
    return changed


def ai_input_allowed(sources_path: Path) -> dict[str, bool]:
    """Per file: may it go to an ML critic or any other AI step?"""
    return {k: bool(v.get("aiInputAllowed", True)) for k, v in records(read_sources(sources_path)).items()}


# ---------------------------------------------------------------- CREDITS.md

CREDITS_HEADER = "# Ghi công âm thanh\n\nTự sinh bởi `tools/audio-lab/build` từ `licences.jsonl` (nguồn cần ghi công, mục 10.2).\n\n"


def write_credits(art_src: Path) -> Path | None:
    rows = [r for r in read_rows(art_src / "licences.jsonl")
            if r.get("kind") == "source" and r.get("attribution_required")]
    path = art_src / "CREDITS.md"
    if not rows and not path.exists():
        return None
    lines = []
    for r in sorted(rows, key=lambda r: r["key"]):
        text = r.get("attribution_text") or f"\"{r.get('file', '?')}\" — {r.get('author', '?')}"
        lines.append(f"- {text} ({r['licence']}, {r.get('url') or r['licenceUrl']}) <!-- {r['key']} -->")
    _write_atomic(path, CREDITS_HEADER + "\n".join(lines) + ("\n" if lines else ""))
    return path
