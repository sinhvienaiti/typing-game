"""Ratings (append-only JSONL) and per-session state (timer, device, anchors).

~/AudioLab/review/<game>/ratings.jsonl        one line per rating; never rewritten
~/AudioLab/review/<game>/state/<session>.json  resume state (atomic replace)
A re-rated item gets a new line with rev + 1; the last line of a (session, item) wins.
"""
from __future__ import annotations

import json
import os
import threading
from pathlib import Path


class Store:
    def __init__(self, review_root: Path):
        self.root = Path(review_root)
        self._lock = threading.Lock()
        self._cache: dict[Path, tuple[tuple[int, int], list[dict], int]] = {}

    def ratings_path(self, game: str) -> Path:
        return self.root / game / "ratings.jsonl"

    def state_path(self, game: str, sid: str) -> Path:
        return self.root / game / "state" / f"{sid}.json"

    def append(self, game: str, line: dict) -> None:
        path = self.ratings_path(game)
        text = json.dumps(line, ensure_ascii=False, separators=(",", ":")) + "\n"
        with self._lock:
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "a", encoding="utf-8") as f:
                f.write(text)
                f.flush()
                os.fsync(f.fileno())

    def lines(self, game: str) -> list[dict]:
        """All valid lines of a game's ratings file (bad lines are skipped and counted)."""
        path = self.ratings_path(game)
        try:
            st = path.stat()
        except FileNotFoundError:
            return []
        sig = (st.st_size, st.st_mtime_ns)
        with self._lock:
            hit = self._cache.get(path)
            if hit and hit[0] == sig:
                return hit[1]
            out, bad = [], 0
            with open(path, encoding="utf-8") as f:
                for raw in f:
                    raw = raw.strip()
                    if not raw:
                        continue
                    try:
                        obj = json.loads(raw)
                    except ValueError:
                        bad += 1
                        continue
                    if isinstance(obj, dict) and obj.get("kind") == "rating":
                        out.append(obj)
            self._cache[path] = (sig, out, bad)
            return out

    def bad_lines(self, game: str) -> int:
        self.lines(game)
        hit = self._cache.get(self.ratings_path(game))
        return hit[2] if hit else 0

    def latest(self, game: str, sid: str) -> dict[str, dict]:
        """item key -> last rating line of this session."""
        out: dict[str, dict] = {}
        for line in self.lines(game):
            if line.get("session") == sid and isinstance(line.get("item"), str):
                out[line["item"]] = line
        return out

    def load_state(self, game: str, sid: str) -> dict:
        try:
            data = json.loads(self.state_path(game, sid).read_text("utf-8"))
            return data if isinstance(data, dict) else {}
        except (OSError, ValueError):
            return {}

    def save_state(self, game: str, sid: str, state: dict) -> None:
        path = self.state_path(game, sid)
        with self._lock:
            path.parent.mkdir(parents=True, exist_ok=True)
            tmp = path.with_suffix(".tmp")
            tmp.write_text(json.dumps(state, ensure_ascii=False, indent=1), "utf-8")
            os.replace(tmp, path)
