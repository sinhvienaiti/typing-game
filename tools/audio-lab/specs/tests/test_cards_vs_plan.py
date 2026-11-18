"""The committed cards follow §4.3.1 exactly: no rise limit where the plan does not time the rise,
and the critic reads the same limits as the card (review finding: 10 ms on rewards, alarms...)."""
from pathlib import Path

import pytest

from critic import groups as G
from critic import spec as S
from specs import store, taxonomy as tx

ROOT = Path(__file__).resolve().parents[1]
CARDS = store.card_files(ROOT)
TIMED = {"hit-small", "hit-heavy", "shot", "blast"}          # §4.3.1 "Trúng, bắn, nổ: ≤ 10 ms"


def test_there_are_cards():
    assert len(CARDS) >= 140


@pytest.mark.parametrize("path", CARDS, ids=lambda p: f"{p.parent.name}/{p.stem}")
def test_card_rise_limit_matches_the_plan(path):
    card = store.load_file(path)
    on, crit, cat = card["onset"], card["critic"], card.get("category")
    assert crit.get("attack_max_ms") == tx.ONSET_CLASSES[on["class"]]["rise_max_ms"] == on["rise_max_ms"]
    if on["class"] == "impact":
        assert cat in TIMED or (cat == "fx-other" and card.get("family") in tx.IMPACT_FAMILIES), cat
    if cat in ("word-reward", "warning", "stinger", "death-swarm", "death-big", "ambience", "music"):
        assert crit.get("attack_max_ms") is None
    if card["playback"]["mode"] == "loop":
        assert crit.get("head_max_ms") is None                # loops: no head check, seam instead
    sp = S.from_mapping(card, str(path))
    assert sp.attack_max_ms == crit.get("attack_max_ms") and sp.head_max_ms == crit.get("head_max_ms")
    # a critic group the plan does not time never gets a limit from the card's class
    if G.get(crit["group"]).attack_max_ms is None and cat != "fx-other":
        assert sp.attack_max_ms is None or on["class"] == "creature"
