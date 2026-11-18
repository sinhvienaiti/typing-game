"""Read the batch-1 table, style-board and Stable Audio 3 trial ids from AUDIO_PIPELINE.md §9."""
from __future__ import annotations

import re
from pathlib import Path

from .. import parse

GAME_NAMES = {"Rồng Giữ Ải": "dragon-hold", "Lời Gọi": "typing-defense", "Tuyến Cuối": "typing-survival"}


def _variants(cell: str, count: int) -> list[str]:
    parts = [p.strip() for p in cell.split("+")]
    if len(parts) == count:
        return parts
    return [cell.strip()] * count


def read_plan(path: Path) -> dict:
    """{"batch1": {(game, id): {...}}, "style_board": {game: [ids]}, "sa3_trial": [ids], "text": str}."""
    text = parse.read_text(path)
    batch1: dict[tuple[str, str], dict] = {}
    for table in parse.md_tables(text):
        if not table.heading.startswith("9.") or "Id" not in table.header:
            continue
        for row, line in zip(table.rows, table.row_lines):
            game = GAME_NAMES.get(row.get("Game", "").strip())
            if not game:
                continue
            ids = parse.backticks(row["Id"])
            variants = _variants(row.get("Biến thể", ""), len(ids))
            for sound_id, var in zip(ids, variants):
                batch1[(game, sound_id)] = {
                    "n": int(row["#"]) if row.get("#", "").strip().isdigit() else None,
                    "why": row.get("Vì sao làm trước", "").strip(),
                    "source": row.get("Nguồn", "").strip(),
                    "variants": var,
                    "line": line,
                }
    style_board: dict[str, list[str]] = {}
    for name, game in GAME_NAMES.items():
        m = re.search(r"^\s*-\s*" + re.escape(name) + r":\s*(`.+)$", text, re.M)
        if m:
            style_board[game] = parse.backticks(m.group(1))
    m = re.search(r"Bản thử Stable Audio 3, 6 id\*\*[^:]*:\s*(.+)$", text, re.M)
    trial = parse.backticks(m.group(1)) if m else []
    return {"batch1": batch1, "style_board": style_board, "sa3_trial": trial, "text": text}


def variant_range(text: str) -> tuple[int, int] | None:
    """'4' -> (4, 4); '1–2' -> (1, 2); '7 file' -> (7, 7)."""
    nums = [int(n) for n in re.findall(r"\d+", text or "")]
    if not nums:
        return None
    return (min(nums), max(nums))
