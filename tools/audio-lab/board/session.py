"""Session files: validation, blind labels, loudness gains and the blind public view.

A session file (JSON, schema "audiolab.board.session/1") lists items; each item has an
id and 1-9 candidates. Candidate roles (top, distinct, probe...) and file paths never
leave the server; the page only sees labels A, B, C... shuffled per item by the seed.
"""
from __future__ import annotations

import hashlib
import json
import os
import random
import re
from dataclasses import dataclass, field
from pathlib import Path

from . import config, loudness

LETTERS = "ABCDEFGHI"
MAX_CANDIDATES = len(LETTERS)
SLUG = re.compile(r"^[A-Za-z0-9_][A-Za-z0-9._-]{0,63}$")
UNSAFE = re.compile(r"[^A-Za-z0-9._-]+")
AUDIO_EXT = {".wav", ".wave", ".ogg", ".oga", ".opus", ".flac", ".mp3", ".m4a"}


class SessionError(ValueError):
    """Invalid session file (message in Vietnamese, with the JSON location)."""


def audiolab_home() -> Path:
    return Path(os.environ.get("AUDIOLAB_HOME") or Path.home() / "AudioLab").expanduser()


def resolve_path(raw: str, base: Path) -> Path:
    """Session paths: absolute, ~/..., audiolab:<path under ~/AudioLab>, or relative to the file."""
    if raw.startswith("audiolab:"):
        return (audiolab_home() / raw[len("audiolab:"):]).resolve()
    p = Path(raw).expanduser()
    return (p if p.is_absolute() else base / p).resolve()


def display_path(p: Path) -> str:
    """Path for ratings.jsonl without the user's home directory in it."""
    p = p.resolve()
    for root, prefix in ((audiolab_home().resolve(), "audiolab:"), (Path.home().resolve(), "~/")):
        try:
            return prefix + str(p.relative_to(root))
        except ValueError:
            continue
    return str(p)


_sha_cache: dict[tuple[str, int, int], str] = {}


def file_sha(p: Path) -> str:
    st = p.stat()
    key = (str(p), st.st_size, st.st_mtime_ns)
    if key not in _sha_cache:
        _sha_cache[key] = loudness.sha256_file(p)
    return _sha_cache[key]


@dataclass
class Candidate:
    index: int                      # order in the session file (top, distinct, probe...)
    role: str
    files: list[Path]
    shas: list[str]
    cards: list[Path | None]
    critics: list[Path | None]
    key: str = ""                   # sha256 of the file (or of the joined file hashes)
    label: str = ""
    gains: list[float] = field(default_factory=list)
    measures: list[dict] = field(default_factory=list)


@dataclass
class Item:
    key: str
    index: int
    id: str
    desc: str
    family: str
    group: str
    mode: str
    contexts: list[str]
    probe: bool
    anchor: bool
    anchor_of: dict | None
    loop: dict
    candidates: list[Candidate]      # session order
    loudness_source: str = ""
    loudness_short_db: float = 0.0   # > 0: the quietest file could not be brought up to the others
    loudness_spread_100ms_db: float | None = None   # 100 ms loudness spread left after matching
    quiet_db: float = 0.0            # how far under the session target the item plays (true-peak cap)
    source_id: str | None = None     # real id behind a neutral calibration id (never sent to the page)

    def by_label(self, label: str) -> Candidate | None:
        return next((c for c in self.candidates if c.label == label), None)

    @property
    def displayed(self) -> list[Candidate]:
        return sorted(self.candidates, key=lambda c: c.label)


@dataclass
class Session:
    sid: str
    path: Path
    game: str
    batch: str
    title: str
    seed: int
    max_minutes: float
    max_items: int
    anchors_wanted: int
    target_lufs: float
    items: list[Item]
    raw: dict
    reveal: str = "item"             # "item": card after each id; "end": cards only when all are rated

    def item(self, key: str) -> Item | None:
        return next((i for i in self.items if i.key == key), None)


def _err(where: str, msg: str) -> SessionError:
    return SessionError(f"{where}: {msg}")


def read_raw(path: Path) -> dict:
    try:
        raw = json.loads(Path(path).read_text("utf-8"))
    except (OSError, ValueError) as exc:
        raise SessionError(f"{path}: không đọc được JSON ({exc})") from exc
    if not isinstance(raw, dict):
        raise SessionError(f"{path}: gốc phải là một object")
    schema = raw.get("schema", config.SESSION_SCHEMA)
    if schema != config.SESSION_SCHEMA:
        raise SessionError(f"{path}: schema {schema!r}, cần {config.SESSION_SCHEMA!r}")
    game = raw.get("game")
    if not isinstance(game, str) or not SLUG.match(game):
        raise SessionError(f"{path}: thiếu 'game' hoặc sai dạng (chữ, số, '-', '_')")
    sid = raw.get("session") or Path(path).stem
    if not isinstance(sid, str) or not SLUG.match(sid):
        raise SessionError(f"{path}: 'session' sai dạng: {sid!r}")
    items = raw.get("items")
    if not isinstance(items, list) or not items:
        raise SessionError(f"{path}: 'items' phải là danh sách không rỗng")
    return raw


def _list(v, n: int) -> list:
    if v is None:
        return [None] * n
    if isinstance(v, list):
        return (v + [None] * n)[:n]
    return [v] + [None] * (n - 1)


def _sibling(f: Path, suffixes: tuple[str, ...], dirs: list[Path] = ()) -> Path | None:
    """<stem><suffix> next to the file first, then in each critic_dir."""
    for folder in [f.parent, *dirs]:
        for s in suffixes:
            p = folder / (f.stem + s)
            if p.is_file():
                return p
    return None


def critic_doc(path: Path | None) -> dict | None:
    """One critic JSON (critic module audiolab.critic.file/1 or the PoC), or None."""
    if not path or not path.is_file():
        return None
    try:
        doc = json.loads(path.read_text("utf-8"))
    except (OSError, ValueError):
        return None
    doc = doc[0] if isinstance(doc, list) and len(doc) == 1 else doc
    return doc if isinstance(doc, dict) else None


def critic_sha(doc: dict) -> str | None:
    sha = doc.get("sha256")
    if not sha and isinstance(doc.get("file"), dict):
        sha = doc["file"].get("sha256")
    return sha if isinstance(sha, str) and len(sha) == 64 else None


def _critic_for(f: Path, sha: str, explicit: Path | None, dirs: list[Path]) -> tuple[Path | None, Path | None, bool]:
    """(critic JSON, card named by it, stale) for one file.

    A JSON about another version of the file (sha256 differs) is stale: it is dropped and
    no card is looked up for it, so old measurements never sit next to new audio."""
    path = explicit if explicit and explicit.is_file() else _sibling(f, (".critic.json", ".json"), dirs)
    doc = critic_doc(path)
    if doc is None:
        return None, None, False
    if critic_sha(doc) not in (None, sha):
        return None, None, True
    card = doc.get("card_blind") or doc.get("card")    # blind card first: no name, verdict or score
    card_path = (path.parent / card).resolve() if isinstance(card, str) and card else None
    return path, (card_path if card_path and card_path.is_file() else None), False


def _dirs(v, base: Path) -> list[Path]:
    v = [v] if isinstance(v, str) else v if isinstance(v, list) else []
    return [resolve_path(d, base) for d in v if isinstance(d, str) and d]


def _candidate(raw, where: str, base: Path, index: int, critic_dirs: list[Path] = ()) -> Candidate:
    if isinstance(raw, str):
        raw = {"file": raw}
    if not isinstance(raw, dict):
        raise _err(where, "ứng viên phải là đường dẫn hoặc object")
    names = raw.get("files") if raw.get("files") is not None else [raw.get("file")]
    if not isinstance(names, list) or not names or not all(isinstance(n, str) and n for n in names):
        raise _err(where, "cần 'file' hoặc 'files' (danh sách đường dẫn)")
    files = []
    for n in names:
        p = resolve_path(n, base)
        if not p.is_file():
            raise _err(where, f"không thấy file {n}")
        if p.suffix.lower() not in AUDIO_EXT:
            raise _err(where, f"đuôi file không hỗ trợ: {p.suffix}")
        files.append(p)
    cards = [resolve_path(c, base) if isinstance(c, str) else None
             for c in _list(raw.get("cards", raw.get("card")), len(files))]
    critics = [resolve_path(c, base) if isinstance(c, str) else None
               for c in _list(raw.get("critics", raw.get("critic")), len(files))]
    shas = [file_sha(f) for f in files]
    found = [_critic_for(f, s, c, critic_dirs) for f, s, c in zip(files, shas, critics)]
    critics = [c for c, _, _ in found]
    # Card: explicit > named by the critic JSON > <stem>.png next to the file or in a critic_dir.
    cards = [c if c and c.is_file() else
             (None if stale else named or _sibling(f, (".png", ".card.png"), critic_dirs))
             for c, (_, named, stale), f in zip(cards, found, files)]
    key = shas[0] if len(shas) == 1 else hashlib.sha256("".join(shas).encode()).hexdigest()
    role = raw.get("role")
    return Candidate(index=index, role=role if isinstance(role, str) and role else "", files=files,
                     shas=shas, cards=cards, critics=critics, key=key)


def _item(raw, where: str, base: Path, index: int, sess: dict, seen: set[str]) -> Item:
    if not isinstance(raw, dict):
        raise _err(where, "item phải là object")
    sound_id = raw.get("id")
    if not isinstance(sound_id, str) or not sound_id.strip():
        raise _err(where, "thiếu 'id'")
    mode = raw.get("mode") or sess.get("mode") or "hero"
    if mode not in config.MODES:
        raise _err(where, f"mode {mode!r} không có; dùng {', '.join(config.MODES)}")
    key = raw.get("key") or f"{index + 1:02d}-{sound_id.strip()}"
    key = UNSAFE.sub("_", str(key))[:80]
    if key in seen:
        raise _err(where, f"key {key!r} bị trùng")
    seen.add(key)
    cands_raw = raw.get("candidates")
    if not isinstance(cands_raw, list) or not 1 <= len(cands_raw) <= MAX_CANDIDATES:
        raise _err(where, f"'candidates' cần 1–{MAX_CANDIDATES} ứng viên")
    dirs = _dirs(raw.get("critic_dir"), base) + sess.get("critic_dirs", [])
    cands = [_candidate(c, f"{where}.candidates[{j}]", base, j, dirs) for j, c in enumerate(cands_raw)]
    if len({c.key for c in cands}) != len(cands):
        raise _err(where, "có hai ứng viên trùng file")
    probe = bool(raw.get("probe")) or any(c.role == "probe" for c in cands)
    for c in cands:   # default roles follow the §4.6 listening list: top, distinct, probe
        if not c.role:
            if mode == "variants":
                c.role = "variant"
            else:
                c.role = ("top", "distinct")[c.index] if c.index < 2 else ("probe" if probe and c.index == len(cands) - 1 else "other")
    item = {"family": raw.get("family") or "", "group": raw.get("group") or "", "mode": mode,
            "loop": raw.get("loop") or {}}
    contexts = raw.get("contexts") or raw.get("context") or config.default_contexts(item)
    if isinstance(contexts, str):
        contexts = [contexts]
    bad = [c for c in contexts if c not in config.CONTEXT_KEYS]
    if bad:
        raise _err(where, f"bối cảnh lạ: {bad}; dùng {config.CONTEXT_KEYS}")
    usable = [c for c in contexts if c in config.ENABLED_CONTEXTS]
    if "mix" in contexts and "loop" not in usable:
        usable.append("loop")      # §7: before phase 3 "Trong trận" is replaced by "Lặp 20 lần"
    if not isinstance(item["loop"], dict):
        raise _err(where, "'loop' phải là object")
    loop = config.loop_params(item)
    # Beds loop back to back (seam check); everything else (alarms, stingers too) repeats at its rate.
    if item["loop"].get("seamless", loop["preset"] == "nen"):
        loop["seamless"] = True
    # Blind labels: fixed by (seed, item key), different for every item.
    order = list(range(len(cands)))
    random.Random(f"{sess['seed']}:{key}").shuffle(order)
    for pos, ci in enumerate(order):
        cands[ci].label = LETTERS[pos]
    src_id = raw.get("source_id")
    return Item(key=key, index=index, id=sound_id.strip(), desc=str(raw.get("desc") or ""),
                family=item["family"], group=item["group"], mode=mode, contexts=usable or ["alone"],
                probe=probe, anchor=bool(raw.get("anchor")), anchor_of=raw.get("anchor_of"),
                loop=loop, candidates=cands, source_id=src_id if isinstance(src_id, str) and src_id else None)


def build(raw: dict, path: Path, cache: loudness.MeasureCache | None,
          extra: list[tuple[int, dict]] | None = None) -> Session:
    """Validate a raw session (plus inserted anchor items) and compute loudness gains."""
    base = Path(path).resolve().parent
    sid = raw.get("session") or Path(path).stem
    seed = raw.get("seed")
    if not isinstance(seed, int):
        seed = int(hashlib.sha256(f"{raw['game']}:{sid}".encode()).hexdigest()[:8], 16)
    sess = {"seed": seed, "mode": raw.get("mode"), "critic_dirs": _dirs(raw.get("critic_dir"), base)}
    # Default keys come from the position in the file, so inserted anchors never shift them.
    raw_items = []
    for i, it in enumerate(raw["items"]):
        if isinstance(it, dict) and not it.get("key") and isinstance(it.get("id"), str):
            it = {**it, "key": f"{i + 1:02d}-{UNSAFE.sub('_', it['id'].strip())}"}
        raw_items.append(it)
    for pos, it in sorted(extra or [], key=lambda x: x[0]):
        raw_items.insert(min(pos, len(raw_items)), it)
    seen: set[str] = set()
    items = [_item(it, f"items[{i}]", base, i, sess, seen) for i, it in enumerate(raw_items)]
    target = float(raw.get("target_lufs", loudness.TARGET_LUFS))
    for it in items:
        files = []
        for c in it.candidates:
            c.measures = [cache.get(s, f) if cache else loudness.measure(f) for s, f in zip(c.shas, c.files)]
            for m, s, cj in zip(c.measures, c.shas, c.critics):
                files.append({"measure": m, "critic": loudness.critic_value(cj, s)})
        bal = loudness.balance(files, target=target)
        gains = bal["gains"]
        it.loudness_source, it.loudness_short_db = bal["source"], bal["short_db"]
        it.loudness_spread_100ms_db = bal["spread_100ms_db"]
        if bal["played_lufs_m"] is not None:
            it.quiet_db = round(max(0.0, target - bal["played_lufs_m"]), 1)
        k = 0
        for c in it.candidates:
            c.gains = gains[k:k + len(c.files)]
            k += len(c.files)
    if cache:
        cache.save()
    reveal = raw.get("reveal", "item")
    if reveal not in ("item", "end"):
        raise SessionError(f"{path}: 'reveal' phải là 'item' hoặc 'end'")
    return Session(sid=sid, path=Path(path).resolve(), game=raw["game"], batch=str(raw.get("batch") or ""),
                   title=str(raw.get("title") or f"{raw['game']} · {raw.get('batch') or sid}"),
                   seed=seed, max_minutes=float(raw.get("max_minutes", 20)),
                   max_items=int(raw.get("max_items", 10)), anchors_wanted=int(raw.get("anchors", config.DEFAULT_ANCHORS) or 0),
                   target_lufs=target, items=items, raw=raw, reveal=reveal)


def load(path: Path, cache: loudness.MeasureCache | None = None) -> Session:
    return build(read_raw(path), path, cache)


def item_view(item: Item) -> dict:
    """What the page may see: no file names, roles, probe or anchor flags, scores."""
    desc = item.desc
    if item.quiet_db > loudness.QUIET_NOTE_DB:      # §7: the owner keeps the volume fixed; say why it is quiet
        note = (f"Bảng phát id này nhỏ hơn mức chung khoảng {item.quiet_db:.0f} dB để không vượt đỉnh; "
                "đừng chỉnh âm lượng máy, và đừng tính là âm quá nhỏ.")
        desc = f"{desc} ({note})" if desc else note
    return {
        "key": item.key,
        "index": item.index,
        "id": item.id,
        "desc": desc,
        "family": item.family,
        "mode": item.mode,
        "modeLabel": config.MODES[item.mode],
        "contexts": item.contexts,
        "loop": {k: item.loop[k] for k in ("interval_ms", "jitter", "cents", "db", "offset_ms", "gap_ms",
                                           "avoid", "count", "seamless") if k in item.loop},
        "candidates": [
            {"label": c.label,
             "files": [{"n": n, "gainDb": g, "durationMs": m.get("duration_ms")}
                       for n, (g, m) in enumerate(zip(c.gains, c.measures))]}
            for c in item.displayed
        ],
    }
