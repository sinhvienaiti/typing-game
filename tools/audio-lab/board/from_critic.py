"""Board sessions from a critic run's listening list (§4.6 step 2, §5.1 step 7).

Reads <out>/_batch.json ("listen": top, distinct, probe per rank group) and the per-file
JSON next to it (file path, spec, card). Writes ~/AudioLab/review/<game>/sessions/<sid>.json,
split into parts of at most `max_items` ids (§7: 10 ids per session).
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from . import config, session

ROLES = ("top", "distinct", "probe")


class FromCriticError(ValueError):
    pass


def _read(path: Path) -> dict:
    try:
        doc = json.loads(path.read_text("utf-8"))
    except (OSError, ValueError) as exc:
        raise FromCriticError(f"không đọc được {path}: {exc}") from exc
    if not isinstance(doc, dict):
        raise FromCriticError(f"{path}: không phải object")
    return doc


def items_from_run(out: Path, ids: set[str] | None = None) -> tuple[list[dict], list[str]]:
    """(session items, skipped ids with the reason) for one critic output folder."""
    out = Path(out).expanduser().resolve()
    batch = _read(out / "_batch.json")
    rows = [f for f in batch.get("files") or [] if isinstance(f, dict)]
    # Listening entries are result stems (unique per run). Older runs wrote file names; a name that
    # two files share (r1/masters and r2/masters) cannot be resolved and is refused.
    by_stem = {(f.get("stem") or Path(str(f.get("json") or "")).stem): f for f in rows if f.get("stem") or f.get("json")}
    by_name: dict[str, list[dict]] = {}
    for f in rows:
        by_name.setdefault(f.get("name"), []).append(f)
    items, skipped = [], []
    for gk, entry in sorted((batch.get("listen") or {}).items()):
        if not isinstance(entry, dict):
            continue
        cands, spec = [], {}
        for role in ROLES:
            name = entry.get(role)
            if not name:
                continue
            row = by_stem.get(name)
            if row is None:
                same = by_name.get(name) or []
                if len(same) > 1:
                    raise FromCriticError(f"{out}: tên {name} trùng ở {len(same)} file; chạy lại bộ chấm (bản mới ghi stem)")
                row = same[0] if same else None
            if not row or not row.get("json"):
                raise FromCriticError(f"{out}: _batch.json không có JSON cho {name}")
            jpath = out / row["json"]
            doc = _read(jpath)
            fpath = Path((doc.get("file") or {}).get("path") or "")
            if not fpath.is_file():
                raise FromCriticError(f"{jpath}: không thấy file âm {fpath}")
            c = {"file": session.display_path(fpath), "role": role, "critic": session.display_path(jpath)}
            card = doc.get("card_blind") or doc.get("card")    # blind card: no name, verdict or score
            if card and (out / card).is_file():
                c["card"] = session.display_path(out / card)
            cands.append(c)
            spec = spec or (doc.get("spec") or {})
        sound_id = str(spec.get("id") or gk.removeprefix("id:"))
        if ids and sound_id not in ids:
            continue
        if not cands:
            skipped.append(f"{sound_id}: không bản nào qua cổng L1")
            continue
        fam = spec.get("family") if spec.get("family") in config.FAMILY_LABELS else ""
        item = {"id": sound_id, "family": fam, "group": spec.get("group") or "",
                "desc": spec.get("desc_vi") or spec.get("group_name_vi") or "",
                "probe": bool(entry.get("probe")), "candidates": cands}
        rate = spec.get("rate_hz")
        if isinstance(rate, (int, float)) and rate > 0 and not spec.get("loop"):
            item["loop"] = {"interval_ms": round(1000.0 / rate)}     # gameplay rate from the spec
        items.append(item)
    return items, skipped


def write_sessions(outs: list[Path], review_root: Path, game: str, batch: str, sid: str,
                   title: str | None = None, seed: int | None = None, ids: set[str] | None = None,
                   max_items: int = 10, force: bool = False,
                   anchors: int | None = None) -> tuple[list[Path], list[str]]:
    if not session.SLUG.match(game) or not session.SLUG.match(sid):
        raise FromCriticError("game và session chỉ gồm chữ, số, '.', '-', '_'")
    items, skipped = [], []
    for out in outs:
        it, sk = items_from_run(Path(out), ids)
        items += it
        skipped += sk
    if not items:
        raise FromCriticError("không có id nào để nghe")
    parts = [items[i:i + max_items] for i in range(0, len(items), max_items)]
    folder = Path(review_root) / game / "sessions"
    written = []
    for k, part in enumerate(parts, 1):
        name = sid if len(parts) == 1 else f"{sid}-{k}"
        path = folder / f"{name}.json"
        if path.exists() and not force:
            raise FromCriticError(f"{path} đã có; thêm --force để ghi đè (điểm cũ vẫn giữ trong ratings.jsonl)")
        s = seed if isinstance(seed, int) else int(hashlib.sha256(f"{game}:{name}".encode()).hexdigest()[:8], 16)
        label = title or f"{game} · lô {batch} · {name}"
        doc = {"schema": config.SESSION_SCHEMA, "session": name, "game": game, "batch": batch,
               "title": label if len(parts) == 1 or title is None else f"{label} ({k}/{len(parts)})",
               "seed": s, "max_minutes": 20, "items": part}
        if anchors is not None:
            doc["anchors"] = max(0, int(anchors))
        folder.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=1), "utf-8")
        written.append(path)
    return written, skipped
