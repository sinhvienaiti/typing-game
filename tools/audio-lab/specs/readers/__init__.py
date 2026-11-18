"""One reader per game. Each module has read(game_root) -> GameData and current_randomisation(entry)."""
from __future__ import annotations

from . import dragon_hold, typing_defense, typing_survival

READERS = {
    dragon_hold.GAME: dragon_hold,
    typing_defense.GAME: typing_defense,
    typing_survival.GAME: typing_survival,
}
GAMES = tuple(READERS)
