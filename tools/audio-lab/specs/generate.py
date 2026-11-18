"""Read the games (read-only), build cards, merge hand edits, write YAML."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from common import env

from . import store
from .build import build_card, derive_critic
from .model import GameData, Issue
from .readers import GAMES, READERS
from .readers.plan import read_plan

PLAN_PATH = env.REPO / "docs" / "games" / "AUDIO_PIPELINE.md"


@dataclass
class GameResult:
    game: str
    data: GameData
    cards: dict[str, dict] = field(default_factory=dict)      # merged cards by id
    texts: dict[str, str] = field(default_factory=dict)       # YAML by id
    status: dict[str, str] = field(default_factory=dict)      # id -> created|updated|unchanged
    kept: dict[str, list[str]] = field(default_factory=dict)  # id -> hand-kept paths
    orphans: list[Path] = field(default_factory=list)
    pruned: list[Path] = field(default_factory=list)
    issues: list[Issue] = field(default_factory=list)


def _is_hand_edited(card: dict) -> bool:
    return bool(card.get("manual") is True or card.get("manual_fields") or store.manual_sections(card)
                or card.get("references") or card.get("notes") or (card.get("prompt") or {}).get("variants")
                or card.get("status") not in ("draft", "proposed"))


def run(root: Path = store.SPECS_DIR, games_root: Path = env.GAMES, plan_path: Path = PLAN_PATH,
        games: list[str] | None = None, write: bool = True, prune: bool = False) -> list[GameResult]:
    plan = read_plan(plan_path)
    results: list[GameResult] = []
    for game in games or list(GAMES):
        reader = READERS[game]
        gd = reader.read(games_root / game)
        res = GameResult(game, gd, issues=list(gd.issues))
        for e in gd.entries:
            card, issues = build_card(gd, e, plan, reader)
            res.issues += issues
            path = store.card_path(root, game, e.id)
            existing = store.load_file(path) if path.exists() else None
            merged, kept = store.merge(card, existing)
            if kept != ["*"]:
                derive_critic(merged)
            res.cards[e.id] = merged
            res.kept[e.id] = kept
            text = store.dumps(merged)
            res.texts[e.id] = text
            if write:
                res.status[e.id] = store.write_if_changed(path, text)
            else:
                res.status[e.id] = "unchanged" if path.exists() and path.read_text(encoding="utf-8") == text else ("updated" if path.exists() else "created")
        gdir = root / game
        if gdir.is_dir():
            for p in sorted(gdir.glob("*.yaml")):
                if p.stem in res.cards:
                    continue
                try:
                    hand = _is_hand_edited(store.load_file(p))
                except Exception:
                    hand = True
                if prune and write and not hand:
                    p.unlink()
                    res.pruned.append(p)
                else:
                    res.orphans.append(p)
        results.append(res)
    return results
