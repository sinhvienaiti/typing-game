"""Spec cards (YAML) per sound id, generated from game catalogs and docs.

Other lanes read cards through this API (no game files touched):

    from specs import load_card, load_cards, taxonomy
    card = load_card("typing-survival", "gun.xung")
    cards = load_cards("dragon-hold")          # {id: card}
    taxonomy.CATEGORIES[card["category"]]      # §4.3.3 ranges for L2
"""
from __future__ import annotations

from pathlib import Path

from . import taxonomy
from .store import SPECS_DIR, card_files, card_path, load_file

__all__ = ["SPECS_DIR", "load_card", "load_cards", "taxonomy"]


def load_card(game: str, sound_id: str, root: Path = SPECS_DIR) -> dict:
    return load_file(card_path(root, game, sound_id))


def load_cards(game: str | None = None, root: Path = SPECS_DIR) -> dict:
    """{id: card} for one game, or {(game, id): card} for all games."""
    out: dict = {}
    for p in card_files(root, game):
        c = load_file(p)
        out[c["id"] if game else (c["game"], c["id"])] = c
    return out
