"""Helpers shared by the game readers."""
from __future__ import annotations

import re

from .. import parse
from ..model import DISAGREE, PLAN, STALE, Entry, Issue

KEY_RE = re.compile(r"\b([A-G](?:#|b)?\s+(?:minor|major|Dorian|Mixolydian|Phrygian|pentatonic))\b")


def need(text: str, needles: list[str], game: str, file: str) -> list[Issue]:
    """A reader relies on these rule sentences; flag the reader when one vanished."""
    return [Issue(game, None, "reader-stale", f"Không thấy câu \"{n}\" trong {file}: kiểm lại bộ đọc", STALE)
            for n in needles if n not in text]


def compare_prompt_length(e: Entry, target_ms: float | None, game: str) -> Issue | None:
    """Prompt length vs the code/list length (20 % tolerance, §4.3.1)."""
    prompt = e.listing.get("prompt") or ""
    d = parse.parse_duration(prompt)
    if d is None or target_ms is None:
        return None
    if d["kind"] == "max":
        if target_ms > d["ms"] * 1.2:
            return Issue(game, e.id, "prompt-length", f"Prompt ghi dưới {d['ms']:g} ms, mã dài {target_ms:g} ms",
                         DISAGREE, target_ms, d["ms"])
        return None
    if d["kind"] == "range":
        if not (d["min_ms"] * 0.8 <= target_ms <= d["max_ms"] * 1.2):
            return Issue(game, e.id, "prompt-length", f"Prompt ghi {d['min_ms']:g}–{d['max_ms']:g} ms, mã dài {target_ms:g} ms",
                         DISAGREE, target_ms, [d["min_ms"], d["max_ms"]])
        return None
    if abs(d["ms"] - target_ms) > 0.2 * target_ms:
        return Issue(game, e.id, "prompt-length", f"Prompt ghi {d['ms']:g} ms, mã dài {target_ms:g} ms (lệch quá 20 %)",
                     DISAGREE, target_ms, d["ms"])
    return None


def music_key_issues(entries: list[Entry], game: str) -> list[Issue]:
    """Stems that play together must share a key and mode (§6.1 test J)."""
    keys = {}
    for e in entries:
        m = KEY_RE.search(e.listing.get("prompt") or "")
        if e.id.startswith("music") and m:
            keys[e.id] = m.group(1)
    if len(set(keys.values())) <= 1:
        return []
    common = max(set(keys.values()), key=list(keys.values()).count)
    return [Issue(game, sid, "music-key", f"Prompt ghi \"{k}\", các stem khác ghi \"{common}\" (bài J, §16)", PLAN, None, k)
            for sid, k in keys.items() if k != common]


def bus_level_issues(levels: dict[str, dict], entries: list[Entry], game: str, list_file: str, code_file: str) -> list[Issue]:
    out: list[Issue] = []
    for bus, both in sorted(levels.items()):
        code, doc = both.get("code"), both.get("doc")
        if code is None or doc is None:
            where = list_file if doc is None else code_file
            out.append(Issue(game, None, "bus-missing", f"Bus `{bus}` không có trong {where}", DISAGREE, code, doc))
            continue
        ids = [e.id for e in entries if (e.code.get("bus") or e.listing.get("bus")) == bus]
        for key, label in (("gain", "mức"), ("duck", "mức hạ khi đọc từ")):
            a, b = code.get(key), doc.get(key)
            if a is None or b is None:
                continue
            if abs(float(a) - float(b)) > 0.005:
                out.append(Issue(game, None, "bus-level",
                                 f"Bus `{bus}`: {label} trong mã là {a:g}, trong {list_file} là {b:g} ({len(ids)} id dùng bus này)",
                                 DISAGREE, a, b))
    return out


def presence_issues(entries: list[Entry], game: str, code_file: str, list_file: str) -> list[Issue]:
    out: list[Issue] = []
    for e in entries:
        if e.proposed:
            continue
        if e.in_code and not e.in_list:
            out.append(Issue(game, e.id, "only-code", f"Có trong {code_file}, không có trong {list_file}", DISAGREE, True, False))
        elif e.in_list and not e.in_code:
            planned = "chưa có" in (e.listing.get("current") or "").lower()
            detail = f"Có trong {list_file}, mã chưa phát" + (" (danh sách ghi \"Chưa có\")" if planned else "")
            out.append(Issue(game, e.id, "only-list", detail, DISAGREE, False, True))
    return out
