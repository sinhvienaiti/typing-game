"""CC0 library sources: pinned specs, the ledger (libraries/SOURCES.jsonl) and licence lines.

Plan: docs/games/AUDIO_PIPELINE.md §3.4 (what to fetch), §10.2 (allowed licences),
§10.6 (licences.jsonl fields), §11 (layout under ~/AudioLab/libraries).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.parse import quote

from common import env

ROOT = env.LIBRARIES
LEDGER_NAME = "SOURCES.jsonl"
INDEX_NAME = "index.json"
SHA_CACHE_NAME = ".sha256-cache.json"

CC0_URL = "https://creativecommons.org/publicdomain/zero/1.0/"
AUDIO_EXTS = (".wav", ".wave", ".flac", ".ogg", ".oga", ".mp3", ".aif", ".aiff")

# Licence flags shared by every CC0 source (§10.6 field names).
CC0_FLAGS = {
    "licence": "CC0-1.0",
    "licence_version": "1.0",
    "licence_url": CC0_URL,
    "commercial_ok": True,
    "attribution_required": False,
    "attribution_text": None,
    "ai_input_allowed": True,
    "raw_redistribution_allowed": True,
    "genai_preference": None,
}

KENNEY_CATEGORY = "https://kenney.nl/assets/category:Audio"
KENNEY_AUTHOR = "Kenney (www.kenney.nl)"
# The 10 audio packs listed on the category page (checked 2026-10-23); the fetcher re-reads the page.
KENNEY_PACKS = (
    "impact-sounds", "sci-fi-sounds", "interface-sounds", "ui-audio", "rpg-audio",
    "digital-audio", "casino-audio", "music-jingles", "voiceover-pack", "voiceover-pack-fighter",
)


@dataclass(frozen=True)
class GitLibrary:
    key: str                      # folder under libraries/ and "library" field in the ledger
    title: str
    repo: str                     # https clone URL
    web: str                      # https://github.com/<owner>/<repo>
    commit: str                   # pinned sample commit (master)
    sfz_branch: str
    sfz_commit: str               # pinned SFZ mapping commit (text only)
    author: str
    paths: tuple[str, ...]        # sparse checkout (cone) paths fetched by default
    deny: tuple[str, ...]         # never fetched, even when asked (plan §8.2)
    attribution_requested: str | None = None   # courtesy request, not a CC0 condition
    notes: str = ""


VCSL = GitLibrary(
    key="vcsl",
    title="Versilian Community Sample Library (VCSL)",
    repo="https://github.com/sgossner/VCSL.git",
    web="https://github.com/sgossner/VCSL",
    commit="c1ea7bcc3c7309650ab0da9d15c9cd1fbc4a4c7e",     # master, 2026-01-14
    sfz_branch="sfz",
    sfz_commit="dfcf4a4918771eee884b96ad4493de82ef84daf6",  # sfz, 2020-12-23
    author="Versilian Studios LLC (Sam Gossner) and contributors",
    paths=(
        "Chordophones/Zithers/Dan Tranh",
        "Chordophones/Composite Chordophones/Folk Harp",
        "Idiophones/Struck Idiophones/Gong 1",
        "Idiophones/Struck Idiophones/Gong 2",
        "Idiophones/Struck Idiophones/Slit Drum",
        "Idiophones/Struck Idiophones/Woodblock",
        "Idiophones/Struck Idiophones/Anvil",
        "Idiophones/Struck Idiophones/Brake Drum",      # §3.4, §8.3 hit.tail, §9 #14 and #28
        "Idiophones/Struck Idiophones/Hand Chimes",
        "Idiophones/Struck Idiophones/Tubular Bells 1",
        "Idiophones/Struck Idiophones/Tubular Bells 2",
        "Membranophones/Struck Membranophones/Frame Drum",
    ),
    deny=("Idiophones/Struck Idiophones/Hand Bells, Nepalese",),
    notes="README: CC0, 'no royalties, no credit, no special terms'. SFZ mappings from the sfz branch.",
)

VSCO2CE = GitLibrary(
    key="vsco2ce",
    title="VS Chamber Orchestra: Community Edition (VSCO-2-CE)",
    repo="https://github.com/sgossner/VSCO-2-CE.git",
    web="https://github.com/sgossner/VSCO-2-CE",
    commit="440300901dfe9275fd84e0b7763af1f8443ae62e",     # master, 2020-08-05
    sfz_branch="SFZ",
    sfz_commit="6dd651d55dde97fd4028699be9d4481f26917891",  # SFZ, 2019-01-17
    author="Versilian Studios (Sam Gossner) and Ivy Audio (Simon Dalzell); cutting by Elan Hickler/Soundemote",
    paths=(
        "Strings/Cello Section",
        "Strings/Harp",
        "Woodwinds/Flute",
        "Brass/F Horn",
        "Brass/Tenor Trombone",
        "Percussion",
    ),
    deny=("Miscellania Raw/Misc 2/NepaleseBells",),
    attribution_requested=(
        "Samples: VS Chamber Orchestra: Community Edition by Versilian Studios/Sam Gossner "
        "and Ivy Audio/Simon Dalzell (https://vis.versilstudios.net/vsco-community.html)"
    ),
    notes=("LICENSE file is CC0 1.0. Readme.txt adds two requests that are not CC0 conditions: "
           "do not sell the samples directly; please credit Versilian Studios/Sam Gossner and/or "
           "Ivy Audio/Simon Dalzell and link the VSCO CE page. Project rule: never ship raw library files."),
)

GIT_LIBRARIES = {lib.key: lib for lib in (VCSL, VSCO2CE)}


def today() -> str:
    return date.today().isoformat()


def rel(path: Path, root: Path = ROOT) -> str:
    return Path(path).resolve().relative_to(Path(root).resolve()).as_posix()


# ---------- checksums ----------

def sha256_file(path: Path, bufsize: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(bufsize):
            h.update(chunk)
    return h.hexdigest()


class ShaCache:
    """sha256 per file, reused while (size, mtime_ns) is unchanged."""

    def __init__(self, root: Path = ROOT):
        self.root = Path(root)
        self.path = self.root / SHA_CACHE_NAME
        try:
            self.data = json.loads(self.path.read_text())
        except (OSError, ValueError):
            self.data = {}
        self.dirty = False

    def get(self, path: Path) -> str:
        path = Path(path)
        st = path.stat()
        key = rel(path, self.root)
        hit = self.data.get(key)
        if hit and hit[0] == st.st_size and hit[1] == st.st_mtime_ns:
            return hit[2]
        digest = sha256_file(path)
        self.data[key] = [st.st_size, st.st_mtime_ns, digest]
        self.dirty = True
        return digest

    def save(self) -> None:
        if self.dirty:
            self.root.mkdir(parents=True, exist_ok=True)
            tmp = self.path.with_suffix(".tmp")
            tmp.write_text(json.dumps(self.data, sort_keys=True))
            os.replace(tmp, self.path)
            self.dirty = False


def write_checksums(base: Path, files: list[Path], cache: ShaCache, header: str = "") -> Path:
    """Write base/CHECKSUMS.sha256 (sha256sum format, paths relative to base)."""
    lines = [f"# {header}"] if header else []
    for f in sorted(files, key=lambda p: rel(p, base)):
        lines.append(f"{cache.get(f)}  {rel(f, base)}")
    out = Path(base) / "CHECKSUMS.sha256"
    out.write_text("\n".join(lines) + "\n")
    return out


def audio_files(base: Path) -> list[Path]:
    base = Path(base)
    if not base.exists():
        return []
    return sorted(p for p in base.rglob("*")
                  if p.is_file() and p.suffix.lower() in AUDIO_EXTS and ".git" not in p.parts)


# ---------- ledger (libraries/SOURCES.jsonl, one JSON record per pack or instrument folder) ----------

def ledger_path(root: Path = ROOT) -> Path:
    return Path(root) / LEDGER_NAME


def read_ledger(root: Path = ROOT) -> list[dict]:
    p = ledger_path(root)
    if not p.exists():
        return []
    return [json.loads(line) for line in p.read_text().splitlines() if line.strip()]


def upsert_ledger(records: list[dict], root: Path = ROOT) -> None:
    """Replace records with the same (library, path), keep the rest, write atomically."""
    current = read_ledger(root)
    keys = {(r["library"], r["path"]) for r in records}
    kept = [r for r in current if (r.get("library"), r.get("path")) not in keys]
    merged = kept + list(records)
    merged.sort(key=lambda r: (r.get("library", ""), r.get("path", "")))
    p = ledger_path(root)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".tmp")
    tmp.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in merged))
    os.replace(tmp, p)


def record_for(path: Path, root: Path = ROOT, ledger: list[dict] | None = None) -> dict | None:
    """Ledger record whose `path` is the longest prefix of the file's path."""
    relp = rel(path, root)
    best = None
    for r in ledger if ledger is not None else read_ledger(root):
        rp = r.get("path", "").rstrip("/")
        if rp and (relp == rp or relp.startswith(rp + "/")):
            if best is None or len(rp) > len(best["path"]):
                best = r
    return best


def licence_line(path: Path, root: Path = ROOT, ledger: list[dict] | None = None,
                 sha256: str | None = None) -> dict:
    """One §10.6 licences.jsonl line for a library file (copy it into art-src/audio/licences.jsonl).

    `licence_copy` is the suggested name under art-src/audio/licences/; `licence_copy_source`
    is the dated copy under ~/AudioLab/libraries that must be copied there with it.
    """
    path = Path(path)
    r = record_for(path, root, ledger)
    if r is None:
        raise LookupError(f"no ledger record covers {path}; run gen.fetch_libraries first")
    relp = rel(path, root)
    inner = relp[len(r["path"]):].lstrip("/")
    if r.get("commit"):
        lib_rel = relp[len(r["library"]) + 1:] if relp.startswith(r["library"] + "/") else inner
        url = f"{r['web']}/blob/{r['commit']}/{quote(lib_rel)}"
        original = lib_rel
    else:
        url = f"{r.get('url')}#{quote(inner)}"
        original = inner
    copy_src = r.get("licence_copy")
    slug = re.sub(r"[^a-z0-9]+", "-", f"{r['library']}-{r.get('pack', '')}".lower()).strip("-")
    return {
        "sha256": sha256 or sha256_file(path),
        "library": r["library"],
        "pack": r.get("pack"),
        "year": r.get("year"),
        "file": original,
        "url": url,
        "author": r.get("author"),
        "licence": r.get("licence"),
        "licence_version": r.get("licence_version"),
        "downloaded": r.get("downloaded"),
        "licence_copy": f"licences/{slug}-LICENSE-{r.get('downloaded')}.txt",
        "licence_copy_source": str(Path(root) / copy_src) if copy_src else None,
        "commit": r.get("commit"),
        "commercial_ok": r.get("commercial_ok"),
        "attribution_required": r.get("attribution_required"),
        "attribution_text": r.get("attribution_text"),
        "attribution_requested": r.get("attribution_requested"),
        "ai_input_allowed": r.get("ai_input_allowed"),
        "raw_redistribution_allowed": r.get("raw_redistribution_allowed"),
        "genai_preference": r.get("genai_preference"),
        "release_file": None,
    }


def latest_licence_copy(base: Path) -> Path | None:
    copies = sorted(Path(base).glob("LICENSE-*.txt"))
    return copies[-1] if copies else None
