"""Listening Board HTTP server (standard library only; binds 127.0.0.1).

GET  /                                   page
GET  /static/<file>                      app.js, app.css
GET  /api/config | /api/health | /api/sessions
GET  /api/session/<sid>                  blind view + saved ratings (by label) + resume point
GET  /api/audio/<sid>/<item>/<label>/<n> audio as WAV (OGG is decoded); the URL never names the file
GET  /api/ctx/<sid>/<item>/<label>/<key>  the candidate's pre-rendered context (scene, burst) as WAV
GET  /api/reveal/<sid>/<item>            card + measurements, 403 until the item is rated
                                         (session "reveal": "end": until every item is rated)
GET  /api/card/<sid>/<item>/<label>      critic PNG, same rule
POST /api/rate                           append one line to ratings.jsonl
POST /api/state                          timer, device, position
"""
from __future__ import annotations

import errno
import hashlib
import json
import math
import random
import socket
import sys
import threading
from datetime import datetime
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

from . import config, loudness, session
from .store import Store

STATIC = Path(__file__).resolve().parent / "static"
STATIC_FILES = {"index.html": "text/html; charset=utf-8", "app.js": "text/javascript; charset=utf-8",
                "app.css": "text/css; charset=utf-8"}
IMAGE_TYPES = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}
CSP = ("default-src 'self'; img-src 'self' data: blob:; media-src 'self' blob:; connect-src 'self'; "
       "script-src 'self'; style-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'")
MAX_BODY = 64 * 1024
MAX_NOTE = 500

# Measurements shown after rating (whitelist: never scores, ranks, roles or learned-critic outputs).
# Keys: critic (audiolab.critic.file/1 "metrics") first, then the PoC analyze.py names, then the board's own.
REVEAL_KEYS = [
    # (keys, label, unit, scale, hint)
    (("duration_ms",), "Dài", "ms", 1, "Độ dài file"),
    (("lufs_momentary_max", "lufs_m_max"), "Độ to", "LUFS", 1, "LUFS-M max (cửa sổ 400 ms)"),
    (("true_peak_dbtp", "true_peak_db"), "Đỉnh", "dBTP", 1, "Đỉnh thật"),
    (("attack_ms", "attack_ms_10_90"), "Lên", "ms", 1, "Thời gian lên của đầu tiếng"),
    (("head_silence_ms",), "Im đầu", "ms", 1, "Im lặng ở đầu"),
    (("crest_db", "crest_factor_db"), "Crest", "dB", 1, "Hệ số đỉnh"),
    (("punch_db", "punch_db_early20_vs_100_300"), "Độ nảy", "dB", 1, "Đầu tiếng so với thân"),
    (("centroid_hz", "spectral_centroid_hz"), "Trọng tâm", "Hz", 1, "Trọng tâm phổ"),
    (("mud_share", "mud_200_500_share"), "Dải đục", "%", 100, "Phần năng lượng ở 200–500 Hz (không hiện với âm có cao độ: gồm nốt gốc)"),
    (("tail_ms", "tail_ms_to_minus60_rel"), "Đuôi", "ms", 1, "Độ dài đuôi"),
    (("speaker_loss_db", "laptop_speaker_loss_db"), "Mất loa nhỏ", "dB", 1, "Độ to mất đi khi lọc cao 200 Hz"),
]
MAX_FLAGS = 8


def critic_numbers(doc: dict) -> dict:
    """Numeric measurements from the top level and the usual nested blocks."""
    out = {}
    for scope in (doc, doc.get("raw"), doc.get("measures"), doc.get("fixed"), doc.get("metrics")):
        if isinstance(scope, dict):
            out.update({k: v for k, v in scope.items()
                        if isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)})
    return out


def critic_flags(doc: dict) -> list[str]:
    """L1 hygiene failures in Vietnamese ('chặn' = blocking). Nothing else: L1b, L4 and L5 flags are
    machine judgements, and showing them between ids would teach the owner's ear (§7, review)."""
    out = []
    l1 = doc.get("L1") if isinstance(doc.get("L1"), dict) else {}
    for ch in l1.get("checks") or []:
        if isinstance(ch, dict) and ch.get("ok") is False:
            out.append(f"L1 {'chặn' if ch.get('blocking') else 'sửa'}: {ch.get('label_vi') or ch.get('id')}")
    return out


def _int(v) -> int:
    """Non-negative int from client input; anything else counts as 0."""
    try:
        return max(0, int(v)) if not isinstance(v, bool) else 0
    except (TypeError, ValueError, OverflowError):
        return 0


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


class ApiError(Exception):
    def __init__(self, status: int, msg: str):
        super().__init__(msg)
        self.status = status


def _anchor_candidates(line: dict) -> list[dict] | None:
    """Best and worst candidate of an earlier rating, if their files are still the same."""
    stars = line.get("stars") or {}
    shown = [h for h in line.get("shown") or [] if isinstance(stars.get(h), int)]
    if len(shown) < 2:
        return None
    best = line.get("pick") if line.get("pick") in shown else max(shown, key=lambda h: stars[h])
    worst = min((h for h in shown if h != best), key=lambda h: stars[h])
    out = []
    for h in (best, worst):
        names = (line.get("files") or {}).get(h)
        names = [names] if isinstance(names, str) else names
        if not names:
            return None
        paths = [session.resolve_path(n, Path("/")) for n in names]
        if not all(p.is_file() for p in paths):
            return None
        shas = [session.file_sha(p) for p in paths]
        key = shas[0] if len(shas) == 1 else hashlib.sha256("".join(shas).encode()).hexdigest()
        if key != h:
            return None
        out.append({"files": [str(p) for p in paths], "role": (line.get("roles") or {}).get(h) or "other"})
    return out


def pick_anchors(lines: list[dict], sid: str, n: int, seed: int) -> list[dict]:
    """§4.6 step 6: re-insert pairs rated in earlier sessions of the same game."""
    latest: dict[tuple, dict] = {}
    for line in lines:
        if line.get("session") == sid or line.get("anchor") or line.get("mode") not in ("hero", "pair"):
            continue
        latest[(line.get("session"), line.get("item"))] = line
    pool = [latest[k] for k in sorted(latest, key=str)]
    random.Random(f"{seed}:anchors").shuffle(pool)
    out: list[dict] = []
    for line in pool:
        cands = _anchor_candidates(line)
        if not cands:
            continue
        ctx = line.get("context")
        # Opaque key: the page must not be able to tell an anchor from a new item.
        tag = hashlib.sha256(f"{sid}:{line.get('session')}:{line.get('item')}".encode()).hexdigest()[:6]
        # Same mode and description as the original item, so nothing on the page marks it as an anchor.
        out.append({"key": f"{tag}-{line.get('id') or 'x'}", "id": line.get("id") or "?", "family": line.get("family") or "",
                    "group": line.get("group") or "", "mode": line.get("mode") or "hero", "anchor": True,
                    "desc": line.get("desc") or "",
                    "anchor_of": {"session": line.get("session"), "item": line.get("item"), "rev": line.get("rev", 1)},
                    "contexts": [ctx] if ctx in config.ENABLED_CONTEXTS and ctx not in config.RENDERED_CONTEXTS else None,
                    "candidates": cands})
        if len(out) >= n:
            break
    return out


class Board:
    """Sessions, ratings and loudness cache behind the HTTP handler."""

    def __init__(self, review_root: Path, sessions: list[Path] | None = None, game: str | None = None,
                 batch: str | None = None, cache_path: Path | None = None):
        self.review_root = Path(review_root)
        self.store = Store(self.review_root)
        self.cache = loudness.MeasureCache(cache_path)
        self.explicit = [Path(p).expanduser().resolve() for p in sessions or []]
        self.game, self.batch = game, batch
        self.paths: dict[str, Path] = {}
        self.errors: dict[str, str] = {}
        self._loaded: dict[str, tuple[tuple, session.Session]] = {}
        self._lock = threading.RLock()
        self.port = 0

    # ---------------------------------------------------------------- sessions
    def discover(self) -> dict[str, Path]:
        if self.explicit:
            paths = self.explicit
        else:
            pattern = f"{self.game or '*'}/sessions/*.json"
            paths = sorted(self.review_root.glob(pattern))
        found: dict[str, Path] = {}
        errors: dict[str, str] = {}
        for p in paths:
            try:
                raw = session.read_raw(p)
            except session.SessionError as exc:
                errors[str(p)] = str(exc)
                continue
            if self.batch and str(raw.get("batch") or "") != self.batch:
                continue
            sid = raw.get("session") or p.stem
            if sid in found:
                errors[str(p)] = f"session id {sid!r} trùng với {found[sid]}"
                continue
            found[sid] = p
        with self._lock:
            self.paths, self.errors = found, errors
        return found

    def get(self, sid: str) -> session.Session:
        with self._lock:
            path = self.paths.get(sid) or self.discover().get(sid)
            if path is None:
                raise ApiError(404, f"không có phiên {sid!r}")
            st = path.stat()
            sig = (st.st_mtime_ns, st.st_size)
            hit = self._loaded.get(sid)
            if hit and hit[0] == sig:
                return hit[1]
            try:
                raw = session.read_raw(path)
                s = session.build(raw, path, self.cache, self._anchors(raw, path))
            except session.SessionError as exc:
                raise ApiError(422, str(exc)) from exc
            self._loaded[sid] = (sig, s)
            return s

    def _anchors(self, raw: dict, path: Path) -> list[tuple[int, dict]]:
        """Anchor items frozen in the session state (chosen by ensure_anchors)."""
        state = self.store.load_state(raw["game"], raw.get("session") or path.stem)
        return [(a["pos"], a["item"]) for a in state.get("anchors") or []]

    def ensure_anchors(self, sid: str) -> None:
        """§4.6 step 6: when the owner first opens a session, pick its anchors and freeze them.

        Picked at open time (not at server start), so ratings made earlier in the same server
        run count. A session that already has ratings but no anchors keeps none: inserting
        items mid-way would move the resume point."""
        with self._lock:
            path = self.paths.get(sid) or self.discover().get(sid)
            if path is None:
                return
            try:
                raw = session.read_raw(path)
                want = int(raw.get("anchors", config.DEFAULT_ANCHORS) or 0)
            except (session.SessionError, TypeError, ValueError):
                return                  # get() reports the bad file (HTTP 422)
            game = raw["game"]
            state = self.store.load_state(game, sid)
            if want <= 0 or "anchors" in state:
                return
            if self.store.latest(game, sid):
                state["anchors"] = []
                self.store.save_state(game, sid, state)
                return
            seed = raw.get("seed") if isinstance(raw.get("seed"), int) else 0
            picked = pick_anchors(self.store.lines(game), sid, want, seed)
            if not picked:
                return                  # nothing rated before: try again on the next open
            rng = random.Random(f"{seed}:anchor-pos")
            n = len(raw["items"])
            state["anchors"] = [{"pos": rng.randint(1, max(1, n)), "item": it} for it in picked]
            self.store.save_state(game, sid, state)
            self._loaded.pop(sid, None)

    def sessions(self) -> dict:
        out = []
        for sid, path in sorted(self.discover().items()):
            try:
                raw = session.read_raw(path)
            except session.SessionError:
                continue
            rated = len(self.store.latest(raw["game"], sid))
            anchors = len(self.store.load_state(raw["game"], sid).get("anchors") or [])   # known after first open
            out.append({"session": sid, "game": raw["game"], "batch": str(raw.get("batch") or ""),
                        "title": str(raw.get("title") or f"{raw['game']} · {raw.get('batch') or sid}"),
                        "items": len(raw["items"]) + anchors, "rated": rated})
        return {"sessions": out, "errors": list(self.errors.values())}

    # ---------------------------------------------------------------- views
    @staticmethod
    def labels_of(item: session.Item, line: dict) -> dict:
        lab = {c.key: c.label for c in item.candidates}
        tags = {lab[h]: v for h, v in (line.get("tags") or {}).items() if h in lab}
        return {"stars": {lab[h]: v for h, v in (line.get("stars") or {}).items() if h in lab},
                "pick": lab.get(line.get("pick")), "pickAuto": bool(line.get("pick_auto")),
                "none": bool(line.get("none")), "tags": tags, "note": line.get("note") or "",
                "dropped": [lab[h] for h in line.get("dropped") or [] if h in lab],
                "rev": line.get("rev", 1), "context": line.get("context")}

    def session_view(self, sid: str) -> dict:
        self.ensure_anchors(sid)
        s = self.get(sid)
        latest = self.store.latest(s.game, s.sid)
        state = self.store.load_state(s.game, s.sid)
        items = []
        for it in s.items:
            v = session.item_view(it)
            line = latest.get(it.key)
            v["rating"] = self.labels_of(it, line) if line else None
            items.append(v)
        resume = next((i for i, it in enumerate(s.items) if it.key not in latest), len(s.items))
        return {"session": s.sid, "game": s.game, "batch": s.batch, "title": s.title,
                "maxMinutes": s.max_minutes, "maxItems": s.max_items, "items": items,
                "resumeIndex": resume, "rated": sum(1 for it in s.items if it.key in latest), "revealAt": s.reveal,
                "state": {"elapsedMs": int(state.get("elapsed_ms") or 0), "device": state.get("device"),
                          "started": state.get("started")},
                "ratingsFile": session.display_path(self.store.ratings_path(s.game))}

    def _item(self, sid: str, key: str) -> tuple[session.Session, session.Item]:
        s = self.get(sid)
        it = s.item(key)
        if it is None:
            raise ApiError(404, f"không có id {key!r} trong phiên {sid!r}")
        return s, it

    def _rated(self, s: session.Session, it: session.Item) -> bool:
        return it.key in self.store.latest(s.game, s.sid)

    def _revealed(self, s: session.Session, it: session.Item) -> bool:
        """Cards and numbers open after the id is rated, or ("reveal": "end") after every id is."""
        latest = self.store.latest(s.game, s.sid)
        if s.reveal == "end":
            return all(x.key in latest for x in s.items)
        return it.key in latest

    _wav: dict[str, bytes] = {}

    def audio_bytes(self, path: Path) -> bytes:
        """Every candidate goes out as WAV: an OGG original next to WAV copies would show which one is the
        original through the Content-Type (§7: nothing may reveal the source)."""
        if path.suffix.lower() in (".wav", ".wave"):
            return path.read_bytes()
        key = session.file_sha(path)
        if key not in self._wav:
            import io

            import soundfile as sf
            data, sr = sf.read(str(path), always_2d=True, dtype="float32")
            buf = io.BytesIO()
            sf.write(buf, data, sr, format="WAV", subtype="FLOAT")
            self._wav[key] = buf.getvalue()
        return self._wav[key]

    def audio(self, sid: str, key: str, label: str, n: int) -> Path:
        _, it = self._item(sid, key)
        c = it.by_label(label)
        if c is None or not 0 <= n < len(c.files):
            raise ApiError(404, "không có bản này")
        return c.files[n]

    def ctx_audio(self, sid: str, key: str, label: str, ctx: str) -> Path:
        _, it = self._item(sid, key)
        c = it.by_label(label)
        if c is None or ctx not in it.rendered or ctx not in c.ctx:
            raise ApiError(404, "không có bản dựng cho bối cảnh này")
        return c.ctx[ctx]

    def card(self, sid: str, key: str, label: str, n: int = 0) -> Path:
        s, it = self._item(sid, key)
        if not self._revealed(s, it):
            raise ApiError(403, "chấm xong cả phiên mới xem được thẻ" if s.reveal == "end" else "chấm xong mới xem được thẻ")
        c = it.by_label(label)
        if c is None or not 0 <= n < len(c.cards) or c.cards[n] is None:
            raise ApiError(404, "không có thẻ ảnh")
        if c.cards[n].suffix.lower() not in IMAGE_TYPES:
            raise ApiError(404, "thẻ không phải ảnh")
        return c.cards[n]

    def reveal(self, sid: str, key: str) -> dict:
        s, it = self._item(sid, key)
        if not self._revealed(s, it):
            raise ApiError(403, "chấm xong cả phiên mới xem được thẻ và số đo" if s.reveal == "end"
                           else "chấm xong mới xem được thẻ và số đo")
        out = []
        for c in it.displayed:
            board_m = c.measures[0] if c.measures else {}
            doc = session.critic_doc(c.critics[0] if c.critics else None)
            crit = critic_numbers(doc) if doc else {}
            flags = critic_flags(doc) if doc else []
            pitched = bool(((doc or {}).get("spec") or {}).get("pitched"))
            rows = []
            for keys, label, unit, scale, hint in REVEAL_KEYS:
                if pitched and label == "Dải đục":
                    continue
                v = next((src[k] for src in (crit, board_m) for k in keys
                          if isinstance(src.get(k), (int, float)) and not isinstance(src.get(k), bool)
                          and math.isfinite(src[k])), None)
                if v is None:
                    continue
                v = float(v) * scale
                rows.append({"label": label, "value": round(v, 3 if abs(v) < 1 else 1), "unit": unit, "hint": hint})
            gain = c.gains[0] if c.gains else 0.0
            rows.append({"label": "Chỉnh", "value": gain, "unit": "dB", "signed": True,
                         "hint": "Mức Bảng Nghe đã chỉnh để các bản nghe cùng độ to"})
            out.append({"label": c.label, "cards": [n for n, p in enumerate(c.cards) if p is not None],
                        "measures": rows, "flags": flags[:MAX_FLAGS], "files": len(c.files)})
        return {"item": it.key, "loudness": it.loudness_source, "candidates": out}

    # ---------------------------------------------------------------- writes
    def rate(self, body: dict) -> dict:
        s, it = self._item(str(body.get("session")), str(body.get("item")))
        labels = {c.label: c for c in it.candidates}

        def check_labels(obj, what):
            bad = [k for k in obj if k not in labels]
            if bad:
                raise ApiError(400, f"{what}: nhãn lạ {bad}")

        stars = body.get("stars") or {}
        tags = body.get("tags") or {}
        dropped = body.get("dropped") or []
        if not isinstance(stars, dict) or not isinstance(tags, dict) or not isinstance(dropped, list):
            raise ApiError(400, "stars/tags/dropped sai kiểu")
        check_labels(stars, "stars")
        check_labels(tags, "tags")
        check_labels(dropped, "dropped")
        for k, v in stars.items():
            if not isinstance(v, int) or isinstance(v, bool) or not 1 <= v <= 5:
                raise ApiError(400, f"sao của {k} phải là số nguyên 1–5")
        for k, v in tags.items():
            if not isinstance(v, list) or any(t not in config.TAG_NAMES for t in v):
                raise ApiError(400, f"nhãn của {k} phải nằm trong danh sách cố định")
        pick = body.get("pick")
        none = bool(body.get("none"))
        if pick is not None and pick not in labels:
            raise ApiError(400, "pick phải là một nhãn")
        if it.mode != "variants":
            missing = [lb for lb in sorted(labels) if lb not in stars]
            if missing:
                raise ApiError(400, "còn thiếu sao cho " + ", ".join(missing))
            if len(labels) > 1 and (pick is None) == (not none):
                raise ApiError(400, "chọn một bản tốt nhất, hoặc bấm 'Không bản nào đạt'")
        if none:
            pick = None
        context = body.get("context") or it.contexts[0]
        heard = [c for c in body.get("contexts_heard") or [] if c in config.ENABLED_CONTEXTS]
        if context not in config.ENABLED_CONTEXTS:
            raise ApiError(400, f"bối cảnh {context!r} chưa dùng được")
        device = body.get("device")
        if device not in config.DEVICES:
            raise ApiError(400, "thiếu thiết bị nghe (tai nghe hay loa)")
        note = str(body.get("note") or "").strip()
        if len(note) > MAX_NOTE:
            raise ApiError(400, f"ghi chú dài quá {MAX_NOTE} ký tự")
        listens = body.get("listens") or {}
        prev = self.store.latest(s.game, s.sid).get(it.key)
        rev = int(prev.get("rev", 1)) + 1 if prev else 1
        key = {lb: c.key for lb, c in labels.items()}
        line = {
            "schema": config.RATING_SCHEMA, "kind": "rating", "ts": now_iso(),
            "game": s.game, "id": it.id, "item": it.key, "family": it.family, "group": it.group, "desc": it.desc,
            "batch": s.batch, "session": s.sid, "mode": it.mode,
            "context": context, "contexts_heard": sorted(set(heard) | {context}, key=config.CONTEXT_KEYS.index),
            "device": device,
            "shown": [c.key for c in it.candidates], "order": [c.label for c in it.candidates],
            "roles": {c.key: c.role for c in it.candidates},
            "stars": {key[lb]: v for lb, v in sorted(stars.items())},
            "pick": key.get(pick) if pick else None, "pick_auto": bool(body.get("pick_auto")) and pick is not None,
            "none": none,
            "tags": {key[lb]: sorted(set(v), key=config.TAG_NAMES.index) for lb, v in sorted(tags.items()) if v},
            "note": note,
            "anchor": it.anchor, "probe": it.probe,
            "listens": {key[lb]: int(v) for lb, v in listens.items()
                        if lb in key and isinstance(v, int) and not isinstance(v, bool) and v >= 0},
            "item_ms": _int(body.get("item_ms")), "session_ms": _int(body.get("session_ms")),
            "rev": rev, "revealed_before": prev is not None,
            "files": {c.key: [session.display_path(f) for f in c.files] for c in it.candidates},
            "gain_db": {c.key: c.gains for c in it.candidates},
            "loudness": it.loudness_source, "loudness_short_db": it.loudness_short_db,
            "loudness_spread_100ms_db": it.loudness_spread_100ms_db, "quiet_db": it.quiet_db,
            "reveal_at": s.reveal, "seed": s.seed, "board": config.BOARD_VERSION,
        }
        if it.source_id:
            line["source_id"] = it.source_id
        if it.mode == "variants":
            line["dropped"] = [key[lb] for lb in sorted(set(dropped))]
        if it.anchor_of:
            line["anchor_of"] = it.anchor_of
        if any(c.ctx for c in it.candidates):
            line["ctx_files"] = {c.key: {k: session.display_path(p) for k, p in c.ctx.items()} for c in it.candidates}
        self.store.append(s.game, line)
        self.save_state({"session": s.sid, "elapsedMs": _int(body.get("session_ms")), "device": device})
        return {"ok": True, "rev": rev, "revealAt": s.reveal,
                "reveal": self.reveal(s.sid, it.key) if self._revealed(s, it) else None}

    def save_state(self, body: dict) -> dict:
        s = self.get(str(body.get("session")))
        state = self.store.load_state(s.game, s.sid)
        state.setdefault("started", now_iso())
        el = body.get("elapsedMs")
        if isinstance(el, (int, float)) and el >= 0:
            state["elapsed_ms"] = max(int(state.get("elapsed_ms") or 0), int(el))
        if body.get("device") in config.DEVICES:
            state["device"] = body["device"]
        if isinstance(body.get("index"), int):
            state["index"] = body["index"]
        state["updated"] = now_iso()
        self.store.save_state(s.game, s.sid, state)
        return {"ok": True}


class Handler(BaseHTTPRequestHandler):
    board: Board            # set on the subclass made by make_server
    verbose = False
    server_version = "AudioLabBoard/" + config.BOARD_VERSION
    sys_version = ""

    def log_message(self, fmt, *args):  # quiet unless --verbose
        if self.verbose:
            sys.stderr.write("board: " + fmt % args + "\n")

    def _host_ok(self) -> bool:
        host = (self.headers.get("Host") or "").lower()
        port = self.server.server_address[1]
        return host in (f"127.0.0.1:{port}", f"localhost:{port}")

    def _send(self, status: int, body: bytes, ctype: str, extra: dict | None = None) -> None:
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Cache-Control", "no-store")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _json(self, obj, status: int = 200) -> None:
        self._send(status, json.dumps(obj, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

    def _file(self, path: Path, ctype: str, extra: dict | None = None) -> None:
        try:
            data = path.read_bytes()
        except OSError:
            raise ApiError(404, "không đọc được file")
        self._send(200, data, ctype, extra)

    def _parts(self) -> list[str]:
        return [unquote(p) for p in urlsplit(self.path).path.split("/") if p]

    def _guard(self, fn) -> None:
        try:
            if not self._host_ok():
                raise ApiError(403, "chỉ mở qua 127.0.0.1")
            fn()
        except ApiError as exc:
            self._json({"error": str(exc)}, exc.status)
        except (BrokenPipeError, ConnectionResetError):
            pass
        except Exception as exc:  # pragma: no cover - last resort, keep the server up
            sys.stderr.write(f"board: lỗi {type(exc).__name__}: {exc}\n")
            self._json({"error": f"lỗi máy chủ: {type(exc).__name__}"}, 500)

    def do_GET(self):  # noqa: N802
        self._guard(self._get)

    def do_HEAD(self):  # noqa: N802
        self._guard(self._get)

    def do_POST(self):  # noqa: N802
        self._guard(self._post)

    def _get(self) -> None:
        b = self.board
        p = self._parts()
        if not p or p == ["index.html"]:
            return self._file(STATIC / "index.html", STATIC_FILES["index.html"], {"Content-Security-Policy": CSP})
        if p[0] == "static" and len(p) == 2 and p[1] in STATIC_FILES:
            return self._file(STATIC / p[1], STATIC_FILES[p[1]])
        if p[0] != "api" or len(p) < 2:
            raise ApiError(404, "không có trang này")
        route, args = p[1], p[2:]
        if route == "health":
            return self._json({"ok": True, "version": config.BOARD_VERSION, "port": self.server.server_address[1]})
        if route == "config":
            return self._json(config.client_config())
        if route == "sessions":
            return self._json(b.sessions())
        if route == "session" and len(args) == 1:
            return self._json(b.session_view(args[0]))
        if route == "audio" and len(args) == 4 and args[3].isdigit():
            f = b.audio(args[0], args[1], args[2], int(args[3]))
            try:
                data = b.audio_bytes(f)
            except Exception as exc:  # noqa: BLE001 - unreadable file: say so, keep serving
                raise ApiError(404, f"không đọc được âm ({type(exc).__name__})")
            return self._send(200, data, "audio/wav")
        if route == "ctx" and len(args) == 4:
            f = b.ctx_audio(args[0], args[1], args[2], args[3])
            try:
                data = b.audio_bytes(f)
            except Exception as exc:  # noqa: BLE001 - unreadable file: say so, keep serving
                raise ApiError(404, f"không đọc được âm ({type(exc).__name__})")
            return self._send(200, data, "audio/wav")
        if route == "reveal" and len(args) == 2:
            return self._json(b.reveal(args[0], args[1]))
        if route == "card" and len(args) in (3, 4):
            n = int(args[3]) if len(args) == 4 and args[3].isdigit() else 0
            f = b.card(args[0], args[1], args[2], n)
            return self._file(f, IMAGE_TYPES[f.suffix.lower()])
        raise ApiError(404, "không có API này")

    def _post(self) -> None:
        ctype = (self.headers.get("Content-Type") or "").split(";")[0].strip().lower()
        if ctype != "application/json":
            raise ApiError(415, "cần Content-Type: application/json")
        origin = self.headers.get("Origin")
        port = self.server.server_address[1]
        if origin and origin not in (f"http://127.0.0.1:{port}", f"http://localhost:{port}"):
            raise ApiError(403, "nguồn gọi không hợp lệ")
        length = int(self.headers.get("Content-Length") or 0)
        if not 0 < length <= MAX_BODY:
            raise ApiError(413, "thân yêu cầu rỗng hoặc quá lớn")
        try:
            body = json.loads(self.rfile.read(length).decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            raise ApiError(400, "JSON không hợp lệ")
        if not isinstance(body, dict):
            raise ApiError(400, "JSON phải là object")
        route = self._parts()[1:] if self._parts()[:1] == ["api"] else []
        if route == ["rate"]:
            return self._json(self.board.rate(body))
        if route == ["state"]:
            return self._json(self.board.save_state(body))
        raise ApiError(404, "không có API này")



class _Server(ThreadingHTTPServer):
    daemon_threads = True
    used_fallback = False


def port_busy(host: str, port: int) -> bool:
    """True when something already accepts connections on host:port (wildcard listeners too)."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.3)
        return s.connect_ex((host, port)) == 0


def make_server(board: Board, host: str = "127.0.0.1", port: int | None = None,
                fallback: int | None = None, verbose: bool = False) -> ThreadingHTTPServer:
    """Bind host:port; when port is busy and a fallback is given, bind the fallback instead."""
    handler = type("BoardHandler", (Handler,), {"board": board, "verbose": verbose})
    chosen, used_fallback = port or 0, False
    if chosen and fallback and port_busy(host, chosen):
        chosen, used_fallback = fallback, True
    try:
        httpd = _Server((host, chosen), handler)
    except OSError as exc:
        if exc.errno != errno.EADDRINUSE or fallback is None or used_fallback:
            raise
        httpd, used_fallback = _Server((host, fallback), handler), True
    httpd.used_fallback = used_fallback
    board.port = httpd.server_address[1]
    return httpd
