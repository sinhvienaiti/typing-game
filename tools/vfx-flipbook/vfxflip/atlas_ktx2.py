"""Compress existing PNG atlases; only the manifest's ktx2 fields are changed."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import re
import shutil
import tempfile
from pathlib import Path

from . import ktx2, pipeline


def _md5(path: Path) -> str:
    with path.open("rb") as handle:
        return hashlib.file_digest(handle, "md5").hexdigest()


def _read(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("flipbooks"), dict):
        raise ktx2.Ktx2Error("manifest phải có bảng flipbooks")
    return data


def _write(path: Path, data: dict) -> None:
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         prefix=".manifest.", suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            json.dump(data, handle, ensure_ascii=False, indent=1)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        temporary.chmod(path.stat().st_mode & 0o777)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def _current(group: dict, output: Path, source_md5: str) -> bool:
    item = group.get("uastc")
    return (group.get("yFlip") is True and group.get("mipmaps") is True
            and group.get("transfer") == "srgb" and isinstance(item, dict)
            and item.get("sourceMd5") == source_md5 and item.get("level") == 2
            and item.get("file") == output.name and output.is_file()
            and item.get("bytes") == output.stat().st_size and item.get("md5") == _md5(output))


def run(folder: Path, *, only: set[str] | None = None, force: bool = False) -> dict:
    """Publish each atlas atomically, then checkpoint its manifest entry for resumability."""
    manifest = folder.resolve() / "manifest.json"
    try:
        data = _read(manifest)
        entries = data["flipbooks"]
        if only is not None and (not only or only - entries.keys()):
            raise ktx2.Ktx2Error(f"--only có id không tồn tại hoặc rỗng: {sorted(only - entries.keys())}")
        plans = []
        # Validate every selected path before creating any output.
        for cid, entry in entries.items():
            if only is not None and cid not in only:
                continue
            if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", cid, re.I) or not isinstance(entry, dict):
                raise ktx2.Ktx2Error(f"mục không hợp lệ: {cid}")
            filename = entry.get("file")
            if not isinstance(filename, str) or not re.fullmatch(r"[a-z0-9][a-z0-9._-]*\.png", filename, re.I):
                raise ktx2.Ktx2Error(f"{cid}: file phải là tên atlas PNG cạnh manifest")
            png, output = manifest.parent / filename, manifest.parent / f"{cid}.uastc.ktx2"
            if png.is_symlink() or output.is_symlink() or not png.is_file():
                raise ktx2.Ktx2Error(f"{cid}: thiếu PNG hoặc đường dẫn là symlink")
            plans.append((cid, copy.deepcopy(entry), png, output))

        encoded = skipped = 0
        for cid, original, png, output in plans:
            source_md5 = _md5(png)
            group = original.get("ktx2", {})
            group = copy.deepcopy(group) if isinstance(group, dict) else {}
            if not force and _current(group, output, source_md5):
                skipped += 1
                print(f"skip {cid}: md5 khớp", flush=True)
                continue
            print(f"KTX2 {output.name} (UASTC, sRGB, mipmap, lật Y)…", flush=True)
            cache = pipeline.lab_home() / "cache" / "ktx2"
            cache.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory(dir=cache) as work:
                staged = Path(work) / output.name
                info = ktx2.encode(png, staged, "uastc", "srgb")
                if _md5(png) != source_md5:
                    raise ktx2.Ktx2Error(f"{cid}: PNG đã đổi trong lúc nén; chưa xuất bản")
                # Re-read so unrelated edits made during a long encode are preserved.
                latest = _read(manifest)
                if latest["flipbooks"].get(cid) != original:
                    raise ktx2.Ktx2Error(f"{cid}: mục manifest đã đổi trong lúc nén; chưa xuất bản")
                group.update(yFlip=True, mipmaps=True, transfer="srgb")
                group["uastc"] = {"file": output.name, "md5": _md5(staged), "bytes": info["bytes"],
                                  "sourceMd5": source_md5, "level": 2}
                # Copy to a sibling before replace: VFXLAB_HOME can be on another filesystem.
                temporary = None
                try:
                    with tempfile.NamedTemporaryFile(dir=output.parent, prefix=f".{output.name}.",
                                                     suffix=".tmp", delete=False) as handle:
                        temporary = Path(handle.name)
                        with staged.open("rb") as source:
                            shutil.copyfileobj(source, handle)
                        handle.flush()
                        os.fsync(handle.fileno())
                    os.replace(temporary, output)
                finally:
                    if temporary is not None:
                        temporary.unlink(missing_ok=True)
                latest["flipbooks"][cid]["ktx2"] = group
                _write(manifest, latest)
            encoded += 1
        result = {"encoded": encoded, "skipped": skipped}
        print(f"ktx2: {encoded} đã nén, {skipped} bỏ qua", flush=True)
        return result
    except (OSError, ValueError, TypeError) as exc:
        raise ktx2.Ktx2Error(f"không nén được manifest {manifest}: {exc}") from exc
