"""Download the CC0 libraries of plan §3.4 into ~/AudioLab/libraries (idempotent, resumable).

  run.sh gen.fetch_libraries                      # Kenney (all audio packs), VCSL, VSCO-2-CE
  run.sh gen.fetch_libraries --only kenney --kenney-packs impact-sounds,ui-audio
  run.sh gen.fetch_libraries --only vcsl --extra "Chordophones/Composite Chordophones/Concert Harp"
  run.sh gen.fetch_libraries --offline            # no network: re-check files, rewrite checksums and ledger

Kenney: each pack page must state CC0 (link to the CC0 deed); the zip's License.txt must say CC0.
VCSL / VSCO-2-CE: shallow, blob-less, sparse git checkout of a pinned commit (only the listed
instrument folders), plus the .sfz mapping files of the pinned SFZ branch commit (text only).
Every pack or instrument folder gets a line in libraries/SOURCES.jsonl; every library keeps
LICENSE-<download date>.txt and CHECKSUMS.sha256. No account, no token, user git config ignored.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
import zipfile
import zlib
from pathlib import Path
from urllib.parse import quote

from common import env
from gen import libraries as L

UA = "audio-lab-fetch/1.0 (local tool; no tracking)"
CC0_HREF = re.compile(r"^https?://creativecommons\.org/publicdomain/zero/1\.0/?$")


def log(msg: str) -> None:
    print(msg, flush=True)


# ---------- HTTP ----------

def http_get(url: str, timeout: float = 60.0, tries: int = 3) -> bytes:
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            last = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"GET {url} failed: {last}")


def download(url: str, dest: Path, tries: int = 4) -> Path:
    """Download to dest via dest.part; resumes a partial file with a Range request."""
    dest = Path(dest)
    part = dest.with_name(dest.name + ".part")
    for i in range(tries):
        have = part.stat().st_size if part.exists() else 0
        headers = {"User-Agent": UA}
        if have:
            headers["Range"] = f"bytes={have}-"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=120) as r:
                mode = "ab" if have and r.status == 206 else "wb"
                with open(part, mode) as f:
                    shutil.copyfileobj(r, f, 1 << 20)
            os.replace(part, dest)
            return dest
        except urllib.error.HTTPError as e:
            if e.code == 416 and part.exists():      # already complete
                os.replace(part, dest)
                return dest
            err = e
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            err = e
        log(f"  thử lại ({i + 1}/{tries}): {err}")
        time.sleep(2 * (i + 1))
    raise RuntimeError(f"download failed: {url}")


# ---------- Kenney ----------

def parse_kenney_page(page: str) -> dict:
    """Pull title, licence link/text, zip URL, file count and versions from a pack page."""
    def first(pat, flags=re.S):
        m = re.search(pat, page, flags)
        return html.unescape(m.group(1)).strip() if m else None

    lic = re.search(r"License</td>\s*<td[^>]*>\s*<a href='([^']+)'[^>]*>([^<]+)</a>", page)
    updates = re.findall(r"<td title='(\d\d)/(\d\d)/(\d{4})'><span class='type[^']*'>([^<]+)</span>"
                         r"<span class='description[^']*'>([^<]*)</span>", page)
    released = [u for u in updates if u[4].lower().startswith("released")]
    files = first(r"Files</td>\s*<td>(\d+)")
    return {
        "title": first(r"<h1 class='mobile-text-center[^']*'[^>]*>([^<]+)</h1>"),
        "licence_href": lic.group(1) if lic else None,
        "licence_text": html.unescape(lic.group(2)).strip() if lic else None,
        "zip_url": first(r"href='(https://kenney\.nl/media/pages/assets/[^']+?\.zip)'"),
        "files_on_page": int(files) if files else None,
        "version": updates[0][3].strip() if updates else None,
        "updated": f"{updates[0][2]}-{updates[0][1]}-{updates[0][0]}" if updates else None,
        "year": int(released[-1][2]) if released else (int(updates[-1][2]) if updates else None),
    }


def page_is_cc0(info: dict) -> bool:
    return bool(info.get("licence_href") and CC0_HREF.match(info["licence_href"])
                and "CC0" in (info.get("licence_text") or ""))


def _crc32(path: Path) -> int:
    crc = 0
    with open(path, "rb") as f:
        while chunk := f.read(1 << 20):
            crc = zlib.crc32(chunk, crc)
    return crc & 0xFFFFFFFF


def safe_extract(zpath: Path, dest: Path) -> tuple[list[Path], int]:
    """Extract regular files only; refuse absolute paths, '..', symlinks.

    Members already on disk with the same size and CRC are left alone (resumable, idempotent).
    Returns (all member paths, number written).
    """
    out, written = [], 0
    dest = Path(dest).resolve()
    with zipfile.ZipFile(zpath) as z:
        bad = z.testzip()
        if bad:
            raise RuntimeError(f"corrupt member in {zpath.name}: {bad}")
        for info in z.infolist():
            name = info.filename
            if info.is_dir() or name.startswith("__MACOSX/") or Path(name).name == ".DS_Store":
                continue
            mode = (info.external_attr >> 16) & 0o170000
            if mode == 0o120000:
                raise RuntimeError(f"symlink in zip refused: {name}")
            target = (dest / name).resolve()
            if name.startswith("/") or ".." in Path(name).parts or dest not in target.parents:
                raise RuntimeError(f"unsafe path in zip refused: {name}")
            out.append(target)
            if target.is_file() and target.stat().st_size == info.file_size and _crc32(target) == info.CRC:
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            if not os.access(target.parent, os.W_OK):
                target.parent.chmod(0o755)
            if target.exists() and not os.access(target, os.W_OK):
                target.chmod(0o644)
            with z.open(info) as src, open(target, "wb") as dst:
                shutil.copyfileobj(src, dst)
            written += 1
    return out, written


def kenney_licence_copy(base: Path, slug: str, info: dict, zip_sha: str, zip_name: str) -> Path:
    """LICENSE-<date>.txt: page statement + the zip's License.txt. Kept if one exists for this zip."""
    for p in sorted(base.glob("LICENSE-*.txt")):
        text = p.read_text(errors="replace")
        if zip_sha in text:
            if "Page licence statement:" not in text and info.get("licence_href"):   # older copy (PoC)
                p.write_text(text.rstrip("\n") + "\n----- added by gen.fetch_libraries -----\n"
                             f"Page licence statement: {info.get('licence_text')} -> {info.get('licence_href')} "
                             f"(checked {L.today()})\n")
            return p
    lic_txt = base / "License.txt"
    body = lic_txt.read_text(errors="replace") if lic_txt.exists() else "(License.txt missing from zip)"
    out = base / f"LICENSE-{L.today()}.txt"
    out.write_text(
        f"Kenney {info.get('title') or slug} {info.get('version') or ''} — licence copy, downloaded {L.today()}.\n"
        f"Source page: https://kenney.nl/assets/{slug}\n"
        f"Page licence statement: {info.get('licence_text')} -> {info.get('licence_href')} (checked {L.today()})\n"
        f"Zip: {zip_name}  sha256={zip_sha}\n"
        f"Licence: CC0 1.0 ({L.CC0_URL}). Attribution not required.\n"
        f"----- License.txt from the zip -----\n{body}")
    return out


def fetch_kenney(root: Path, packs: list[str], offline: bool, cache: L.ShaCache) -> list[dict]:
    ledger = {r["path"]: r for r in L.read_ledger(root)}
    records = []
    for slug in packs:
        base = root / "kenney" / slug
        base.mkdir(parents=True, exist_ok=True)
        prev = ledger.get(f"kenney/{slug}", {})
        log(f"[kenney] {slug}")
        if offline:
            info = {k: prev.get(k) for k in ("version", "year", "updated", "files_on_page")}
            info["title"] = prev.get("pack")
            info.update(zip_url=prev.get("url"), licence_href=(prev.get("verified") or {}).get("page_href"),
                        licence_text=(prev.get("verified") or {}).get("page_text"))
            if not prev:
                log("  bỏ qua: chưa có trong sổ và đang offline")
                continue
        else:
            try:
                info = parse_kenney_page(http_get(f"https://kenney.nl/assets/{slug}").decode("utf-8", "replace"))
            except RuntimeError as e:
                log(f"  BỎ QUA: không đọc được trang ({e})")
                continue
            if not page_is_cc0(info):
                log(f"  BỎ QUA: trang không ghi CC0 ({info.get('licence_text')!r} {info.get('licence_href')!r})")
                continue
            if not info.get("zip_url"):
                log("  BỎ QUA: không thấy link zip trên trang")
                continue
        zip_name = Path(info["zip_url"]).name if info.get("zip_url") else f"kenney_{slug}.zip"
        zpath = base / zip_name
        same_url = prev.get("url") == info.get("zip_url")
        if zpath.exists() and same_url and prev.get("sha256") == cache.get(zpath):
            log("  zip đã có, mã băm khớp sổ")
        elif offline:
            if not zpath.exists():
                log("  thiếu zip và đang offline")
                continue
        else:
            log(f"  tải {info['zip_url']}")
            if zpath.exists():
                zpath.unlink()
            try:
                download(info["zip_url"], zpath)
            except RuntimeError as e:
                log(f"  LỖI tải: {e} (chạy lại lệnh để tải tiếp)")
                continue
        zip_sha = cache.get(zpath)
        _, written = safe_extract(zpath, base)
        log(f"  giải nén: {written} file mới hoặc đã đổi" if written else "  file đã giải nén đủ, khớp CRC")
        lic_txt = base / "License.txt"
        zip_cc0 = lic_txt.exists() and "CC0" in lic_txt.read_text(errors="replace")
        if not zip_cc0:
            log("  BỎ QUA: License.txt trong zip không ghi CC0")
            continue
        copy = kenney_licence_copy(base, slug, info, zip_sha, zip_name)
        files = L.audio_files(base)
        L.write_checksums(base, files + [lic_txt], cache, header=f"zip {zip_name} sha256={zip_sha}")
        downloaded = prev.get("downloaded") if (same_url and prev.get("sha256") == zip_sha) else L.today()
        records.append({
            "library": "kenney", "pack": info.get("title") or slug, "slug": slug,
            "version": info.get("version"), "year": info.get("year"), "updated": info.get("updated"),
            "path": f"kenney/{slug}", "file": zip_name, "sha256": zip_sha, "url": info.get("zip_url"),
            "page": f"https://kenney.nl/assets/{slug}", "author": L.KENNEY_AUTHOR,
            **L.CC0_FLAGS,
            "licence_copy": L.rel(copy, root), "licence_copy_sha256": L.sha256_file(copy),
            "verified": {"page_href": info.get("licence_href"), "page_text": info.get("licence_text"),
                         "zip_license_txt_cc0": zip_cc0, "checked": prev.get("verified", {}).get("checked")
                         if offline else L.today()},
            "downloaded": downloaded or L.today(),
            "files": len(files), "files_on_page": info.get("files_on_page"),
            "attribution_requested": "Kenney (www.kenney.nl) — optional, see License.txt",
        })
        log(f"  {len(files)} file âm, CC0 đã kiểm")
    return records


def kenney_packs_from_category() -> list[str]:
    page = http_get(L.KENNEY_CATEGORY).decode("utf-8", "replace")
    slugs = re.findall(r"href='https://kenney\.nl/assets/([a-z0-9-]+)'", page)
    slugs += re.findall(r'href="https://kenney\.nl/assets/([a-z0-9-]+)"', page)
    found = [s for s in slugs if not s.startswith(("category", "tag", "series"))]
    return list(dict.fromkeys([*found, *L.KENNEY_PACKS]))


# ---------- git (VCSL, VSCO-2-CE) ----------

GIT_ENV = {
    "GIT_TERMINAL_PROMPT": "0", "GIT_LFS_SKIP_SMUDGE": "1", "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_CONFIG_GLOBAL": os.devnull, "GIT_ASKPASS": "true", "SSH_ASKPASS": "true",
}
GIT_SAFE = ["-c", "core.hooksPath=/dev/null", "-c", "credential.helper=", "-c", "core.symlinks=false",
            "-c", "core.fsmonitor=false", "-c", "submodule.recurse=false", "-c", "fetch.recurseSubmodules=false",
            "-c", "advice.detachedHead=false", "-c", "core.precomposeunicode=true", "-c", "core.quotepath=false"]


def git(repo: Path, *args: str, allow_file: bool = False, check: bool = True) -> str:
    proto = ["-c", "protocol.allow=never", "-c", "protocol.https.allow=always"]
    if allow_file:   # tests use a local repo
        proto += ["-c", "protocol.file.allow=always"]
    e = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    e.update(GIT_ENV)
    r = subprocess.run(["git", *GIT_SAFE, *proto, "-C", str(repo), *args],
                       capture_output=True, text=True, env=e)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout.strip()


def sparse_checkout(repo_dir: Path, url: str, commit: str, patterns: list[str], cone: bool = True,
                    allow_file: bool = False) -> str:
    """Shallow, blob-less, sparse checkout of one pinned commit. Safe to re-run after an interruption."""
    repo_dir.mkdir(parents=True, exist_ok=True)
    g = lambda *a, check=True: git(repo_dir, *a, allow_file=allow_file, check=check)  # noqa: E731
    if not (repo_dir / ".git").exists():
        g("init", "-q")
    if g("remote", check=False) != "origin":
        g("remote", "add", "origin", url)
    else:
        g("remote", "set-url", "origin", url)
    g("config", "extensions.partialClone", "origin")
    g("config", "remote.origin.promisor", "true")
    g("config", "remote.origin.partialclonefilter", "blob:none")
    mode = "--cone" if cone else "--no-cone"
    g("sparse-checkout", "set", mode, *patterns)
    head = g("rev-parse", "-q", "--verify", "HEAD^{commit}", check=False)
    if head != commit:
        have = g("cat-file", "-t", commit, check=False)
        if have != "commit":
            g("fetch", "-q", "--depth", "1", "--filter=blob:none", "origin", commit)
        g("checkout", "-q", "-f", "--detach", commit)
    if g("status", "--porcelain", "--untracked-files=no"):
        g("checkout", "-q", "-f", "--detach", commit)      # resume: fetch missing blobs
    g("sparse-checkout", "reapply")
    if g("status", "--porcelain", "--untracked-files=no"):
        raise RuntimeError(f"{repo_dir}: working tree differs from {commit} after checkout")
    return g("rev-parse", "HEAD")


def git_licence_copy(base: Path, lib: L.GitLibrary, commit: str) -> Path:
    for p in sorted(base.glob("LICENSE-*.txt")):
        if commit in p.read_text(errors="replace"):
            return p
    parts = [f"{lib.title} — licence copy, downloaded {L.today()}.",
             f"Repository: {lib.web}  commit {commit}",
             f"SFZ mappings: branch {lib.sfz_branch}  commit {lib.sfz_commit}",
             f"Licence: CC0 1.0 ({L.CC0_URL}) per the repository LICENSE file below.",
             f"Notes: {lib.notes}"]
    for name in ("README.md", "Readme.txt"):
        f = base / name
        if f.exists():
            parts.append(f"----- {name} at {commit} -----\n{f.read_text(errors='replace').strip()}")
    lic = base / "LICENSE"
    parts.append(f"----- LICENSE at {commit} -----\n"
                 + (lic.read_text(errors="replace") if lic.exists() else "(LICENSE missing!)"))
    out = base / f"LICENSE-{L.today()}.txt"
    out.write_text("\n".join(parts) + "\n")
    return out


def check_paths(lib: L.GitLibrary, paths: list[str]) -> list[str]:
    out = []
    for p in paths:
        p = p.strip().strip("/")
        if not p:
            continue
        if any(p == d or p.startswith(d + "/") or d.startswith(p + "/") for d in lib.deny):
            raise SystemExit(f"{lib.key}: '{p}' bị cấm theo kế hoạch §8.2 (không dùng chuông Nepal)")
        out.append(p)
    return list(dict.fromkeys(out))


def folder_digest(base: Path, files: list[Path], cache: L.ShaCache) -> str:
    """Content hash of a folder: sha256 of its sorted '<sha256>  <relative path>' lines."""
    lines = sorted(f"{cache.get(f)}  {L.rel(f, base)}" for f in files)
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def fetch_git_library(root: Path, lib: L.GitLibrary, extra: list[str], offline: bool, cache: L.ShaCache,
                      allow_file: bool = False) -> list[dict]:
    base = root / lib.key
    sfz_dir = root / f"{lib.key}-sfz"
    paths = check_paths(lib, [*lib.paths, *extra])
    prev = {r["path"]: r for r in L.read_ledger(root)}
    log(f"[{lib.key}] {len(paths)} thư mục, commit {lib.commit[:10]}")
    if offline:
        if not (base / ".git").exists():
            log("  chưa có và đang offline")
            return []
        commit = git(base, "rev-parse", "HEAD")
        sfz_commit = git(sfz_dir, "rev-parse", "HEAD") if (sfz_dir / ".git").exists() else None
    else:
        commit = sparse_checkout(base, lib.repo, lib.commit, paths, cone=True, allow_file=allow_file)
        sfz_commit = sparse_checkout(sfz_dir, lib.repo, lib.sfz_commit,
                                     ["*.sfz", "/LICENSE", "/README*", "/Readme*"], cone=False,
                                     allow_file=allow_file)
    for p in paths:   # deny list also guards against a stale checkout
        if not (base / p).exists():
            raise RuntimeError(f"{lib.key}: missing folder after checkout: {p}")
    copy = git_licence_copy(base, lib, commit)
    year = int(git(base, "show", "-s", "--format=%cs", "HEAD")[:4])
    lic_text = (base / "LICENSE").read_text(errors="replace") if (base / "LICENSE").exists() else ""
    if "CC0" not in lic_text:
        raise RuntimeError(f"{lib.key}: LICENSE at {commit} is not CC0; stop")
    all_files = []
    records = []
    for p in paths:
        files = L.audio_files(base / p)
        all_files += files
        key = f"{lib.key}/{p}"
        old = prev.get(key, {})
        url = f"{lib.web}/tree/{commit}/{quote(p)}"
        records.append({
            "library": lib.key, "pack": Path(p).name, "path": key, "folder": p,
            "repo": lib.repo, "web": lib.web, "commit": commit, "version": commit[:12],
            "url": url, "page": url,
            "sha256": folder_digest(base, files, cache), "sha256_of": "sorted '<sha256>  <path>' lines of the folder",
            "author": lib.author, "year": year, **L.CC0_FLAGS,
            "attribution_requested": lib.attribution_requested,
            "licence_copy": L.rel(copy, root), "licence_copy_sha256": L.sha256_file(copy),
            "verified": {"repo_license_cc0": True, "checked": old.get("verified", {}).get("checked")
                         if offline else L.today()},
            "downloaded": old.get("downloaded") if old.get("commit") == commit else L.today(),
            "files": len(files), "bytes": sum(f.stat().st_size for f in files),
            "notes": lib.notes,
        })
    sfz_files = sorted(sfz_dir.rglob("*.sfz")) if sfz_dir.exists() else []
    if sfz_files:
        key = f"{lib.key}-sfz"
        old = prev.get(key, {})
        records.append({
            "library": lib.key, "pack": "SFZ mappings (text)", "path": key, "folder": "*.sfz",
            "repo": lib.repo, "web": lib.web, "commit": sfz_commit, "branch": lib.sfz_branch,
            "version": sfz_commit[:12], "url": f"{lib.web}/tree/{sfz_commit}", "page": f"{lib.web}/tree/{sfz_commit}",
            "sha256": folder_digest(sfz_dir, sfz_files, cache), "sha256_of": "sorted '<sha256>  <path>' lines",
            "author": lib.author, "year": int(git(sfz_dir, "show", "-s", "--format=%cs", "HEAD")[:4]),
            **L.CC0_FLAGS,
            "licence_copy": L.rel(copy, root), "licence_copy_sha256": L.sha256_file(copy),
            "verified": {"repo_license_cc0": True, "checked": old.get("verified", {}).get("checked")
                         if offline else L.today()},
            "downloaded": old.get("downloaded") if old.get("commit") == sfz_commit else L.today(),
            "files": len(sfz_files), "notes": "Key/velocity maps only; used to confirm note names.",
        })
        L.write_checksums(sfz_dir, sfz_files, cache, header=f"{lib.repo} {lib.sfz_branch} {sfz_commit}")
    L.write_checksums(base, all_files, cache, header=f"{lib.repo} {commit}")
    size = sum(f.stat().st_size for f in all_files) / 1e6
    log(f"  {len(all_files)} file âm ({size:.0f} MB), {len(sfz_files)} file sfz; giấy phép: {copy.name}")
    return records


# ---------- CLI ----------

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="gen.fetch_libraries", description=__doc__.split("\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", default="kenney,vcsl,vsco2ce", help="kenney,vcsl,vsco2ce (mặc định: cả ba)")
    ap.add_argument("--kenney-packs", default="all", help="'all' (đọc trang danh mục) hoặc danh sách slug")
    ap.add_argument("--extra", action="append", default=[], metavar="LIB:PATH",
                    help="thêm thư mục, ví dụ 'vcsl:Membranophones/Struck Membranophones/Timpani 1'")
    ap.add_argument("--offline", action="store_true", help="không dùng mạng; chỉ kiểm file đã có và ghi lại sổ")
    ap.add_argument("--root", default=str(L.ROOT), help=argparse.SUPPRESS)
    a = ap.parse_args(argv)
    env.apply()
    root = Path(a.root)
    root.mkdir(parents=True, exist_ok=True)
    cache = L.ShaCache(root)
    only = {s.strip() for s in a.only.split(",") if s.strip()}
    unknown = only - {"kenney", *L.GIT_LIBRARIES}
    if unknown:
        ap.error(f"không biết thư viện: {', '.join(sorted(unknown))}")
    extras: dict[str, list[str]] = {}
    for item in a.extra:
        lib, _, path = item.partition(":")
        if lib not in L.GIT_LIBRARIES or not path:
            ap.error(f"--extra cần dạng vcsl:<đường dẫn> hoặc vsco2ce:<đường dẫn>, nhận '{item}'")
        extras.setdefault(lib, []).append(path)
    records: list[dict] = []
    try:
        if "kenney" in only:
            if a.kenney_packs == "all":
                packs = list(L.KENNEY_PACKS) if a.offline else kenney_packs_from_category()
            else:
                packs = [p.strip() for p in a.kenney_packs.split(",") if p.strip()]
            records += fetch_kenney(root, packs, a.offline, cache)
        for key, lib in L.GIT_LIBRARIES.items():
            if key in only:
                records += fetch_git_library(root, lib, extras.get(key, []), a.offline, cache)
    finally:
        cache.save()
        if records:
            L.upsert_ledger(records, root)
    log(f"Sổ nguồn: {L.ledger_path(root)} ({len(records)} dòng cập nhật)")
    log("Bước tiếp: run.sh gen.index_library")
    return 0


if __name__ == "__main__":
    sys.exit(main())
