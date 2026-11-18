"""May a file reach a learned model (L3-L5) or a cloud reader of its card? (§10.2, §10.3, §10.7)

Read-only. Sources of truth, in order:
  1. path markers: libraries/_no-ai/..., anything Sonniss;
  2. the library ledger ~/AudioLab/libraries/SOURCES.jsonl (pack rows with ai_input_allowed=false);
  3. ledgers given with --sources: art-src/audio/SOURCES.json (records with sha256/masterSha256 and
     aiInputAllowed) or licences.jsonl-style rows (sha256 + ai_input_allowed).
The critic never writes a ledger; it reports `ai_steps` so the caller can run build.ledger.mark_ai_step.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

NO_AI_MARKERS = ("/_no-ai/", "/sonniss")
_AI_TOOL = re.compile(r"stable-audio|ace-step|moss|elevenlabs|magenta|lora|audio-to-audio", re.I)   # build.policy.AI_TOOLS


def path_forbidden(path) -> bool:
    p = str(path).replace("\\", "/").lower()
    return any(mk in p for mk in NO_AI_MARKERS)


@dataclass
class Policy:
    lib_root: Path | None = None
    lib_denied: list[str] = field(default_factory=list)          # pack paths under lib_root
    sha_denied: dict[str, str] = field(default_factory=dict)     # sha256 -> where it was found
    name_denied: dict[str, str] = field(default_factory=dict)    # record key basename -> where
    loaded: list[str] = field(default_factory=list)
    records: dict[str, dict] = field(default_factory=dict)       # sha256 / masterSha256 -> SOURCES.json record

    def provenance(self, path, sha256: str | None = None) -> dict:
        """What made this file, when a ledger says so: {"kind", "ai_generated"} or {}.

        A build record (SOURCES.json) is AI-generated when a layer is a model output (kind gen, or a
        generative tool); a file inside the CC0 libraries, or a sampler render with its report
        (x.json with "sources" next to x.wav), is a recording."""
        rec = self.records.get(sha256 or "")
        if rec is not None:
            layers = [ly for ly in rec.get("layers") or [] if isinstance(ly, dict)]
            gen = any(ly.get("kind") == "gen" or ly.get("model") or _AI_TOOL.search(str(ly.get("tool") or ""))
                      for ly in layers)
            return {"kind": "build", "ai_generated": bool(gen) or bool(rec.get("models") and not layers)}
        pr = Path(path).resolve()
        if self.lib_root is not None:
            root = self.lib_root.resolve()
            if root in pr.parents:
                return {"kind": "library", "ai_generated": False}
        rep = pr.with_suffix(".json")
        if rep.is_file():
            try:
                doc = json.loads(rep.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                doc = None
            if isinstance(doc, dict) and isinstance(doc.get("sources"), list) and "notes" in doc:
                return {"kind": "sampler", "ai_generated": False}
        return {}

    def source_qa(self, sha256: str | None) -> dict | None:
        """Raw L1 of the layers a build record was mixed from (build.render writes layer `rawQa`).

        {"checked": n, "failed": [layer ids], "excepted": [layer ids], "unchecked": [layer ids]},
        or None when no build record matches the file."""
        rec = self.records.get(sha256 or "")
        if rec is None:
            return None
        out = {"checked": 0, "failed": [], "excepted": [], "unchecked": []}
        for ly in rec.get("layers") or []:
            if not isinstance(ly, dict):
                continue
            lid = str(ly.get("id") or ly.get("role") or "?")
            qa = ly.get("rawQa")
            if not isinstance(qa, dict):
                if ly.get("kind") not in ("synth",):
                    out["unchecked"].append(lid)
                continue
            out["checked"] += 1
            if qa.get("verdict") == "BLOCK":
                (out["excepted"] if qa.get("exception") else out["failed"]).append(lid)
        return out

    def check(self, path, sha256: str | None = None) -> tuple[bool, str | None]:
        """(allowed, reason in Vietnamese)."""
        if path_forbidden(path):
            return False, "đường dẫn thuộc nguồn cấm AI (_no-ai hoặc Sonniss)"
        p = Path(path).resolve()
        if self.lib_root is not None:
            for rel in self.lib_denied:
                root = (self.lib_root / rel).resolve()
                if root == p or root in p.parents:
                    return False, f"gói thư viện {rel} có ai_input_allowed=false"
        if sha256 and sha256 in self.sha_denied:
            return False, f"sổ nguồn {self.sha_denied[sha256]} ghi aiInputAllowed=false"
        if p.name in self.name_denied:
            return False, f"sổ nguồn {self.name_denied[p.name]} ghi aiInputAllowed=false"
        return True, None


def _denied(rec: dict) -> bool:
    for k in ("aiInputAllowed", "ai_input_allowed"):
        if rec.get(k) is False:
            return True
    return False


def _add_record(pol: Policy, key: str | None, rec: dict, where: str) -> None:
    if not isinstance(rec, dict) or not _denied(rec):
        return
    for k in ("sha256", "masterSha256", "sourceSha256"):
        v = rec.get(k)
        if isinstance(v, str) and len(v) == 64:
            pol.sha_denied[v] = where
    for name in (key, rec.get("master"), rec.get("file")):
        if isinstance(name, str) and name:
            pol.name_denied[Path(name).name] = where


def load(sources: list[str] | None = None, libraries: Path | None = None) -> Policy:
    pol = Policy()
    if libraries is None:
        try:
            from common import env
            libraries = env.LIBRARIES
        except Exception:
            libraries = None
    if libraries is not None:
        led = Path(libraries) / "SOURCES.jsonl"
        pol.lib_root = Path(libraries)
        if led.is_file():
            for line in led.read_text(encoding="utf-8").splitlines():
                try:
                    row = json.loads(line)
                except ValueError:
                    continue
                if isinstance(row, dict) and _denied(row) and row.get("path"):
                    pol.lib_denied.append(str(row["path"]))
            pol.loaded.append(str(led))
    for s in sources or []:
        p = Path(s).expanduser()
        if not p.is_file():
            raise FileNotFoundError(f"không thấy sổ nguồn {p}")
        text = p.read_text(encoding="utf-8")
        if p.suffix == ".jsonl":
            for line in text.splitlines():
                try:
                    row = json.loads(line)
                except ValueError:
                    continue
                _add_record(pol, row.get("key") if isinstance(row, dict) else None, row, p.name)
        else:
            data = json.loads(text)
            items = data.items() if isinstance(data, dict) else enumerate(data)
            for k, rec in items:
                if isinstance(k, str) and k.startswith("$"):
                    continue
                _add_record(pol, k if isinstance(k, str) else None, rec, p.name)
                if isinstance(rec, dict):
                    for hk in ("sha256", "masterSha256"):
                        if isinstance(rec.get(hk), str) and len(rec[hk]) == 64:
                            pol.records[rec[hk]] = rec
        pol.loaded.append(str(p))
    return pol
