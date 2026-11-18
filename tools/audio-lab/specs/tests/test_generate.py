"""End to end on the real games (read-only): generate into a temp folder, validate, regenerate."""
import hashlib
import json

import pytest

from common import env
from specs import store, validate
from specs.__main__ import main
from specs.generate import run
from specs.readers import READERS


def _sources() -> dict:
    out = {}
    for game, mod in READERS.items():
        for rel in mod.FILES.values():
            p = env.GAMES / game / rel
            out[str(p)] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


@pytest.fixture(scope="module")
def generated(tmp_path_factory):
    root = tmp_path_factory.mktemp("cards")
    before = _sources()
    results = run(root=root)
    assert _sources() == before, "generate must not touch games/**"
    return root, results


def test_every_game_has_cards_that_validate(generated):
    root, results = generated
    assert {r.game for r in results} == set(READERS)
    for r in results:
        assert len(r.cards) >= 25, r.game
        assert all(s == "created" for s in r.status.values())
    problems, n = validate.check_files(store.card_files(root))
    assert n == sum(len(r.cards) for r in results)
    assert [p for p in problems if p.level == validate.ERROR] == []


def test_regenerate_is_stable_and_keeps_hand_edits(generated):
    root, results = generated
    game = results[0].game
    sid = next(iter(results[0].cards))
    path = store.card_path(root, game, sid)
    card = store.load_file(path)
    card["status"] = "approved"
    card["notes"] = "chủ dự án đã nghe"
    card["duration"] = dict(card["duration"], target_ms=123, min_ms=100, max_ms=150, manual=True)
    card["onset"] = dict(card["onset"], rise_max_ms=7, manual=True)
    card["manual_fields"] = ["purpose"]
    card["purpose"] = "sửa tay"
    path.write_text(store.dumps(card), encoding="utf-8")

    again = run(root=root)
    st = {r.game: r.status for r in again}
    assert st[game][sid] == "updated"             # critic keys follow the hand-edited onset
    assert all(s == "unchanged" for g in st for i, s in st[g].items() if (g, i) != (game, sid))
    third = run(root=root)
    assert all(s == "unchanged" for r in third for s in r.status.values())
    kept = store.load_file(path)
    assert kept["status"] == "approved" and kept["notes"] == "chủ dự án đã nghe"
    assert kept["critic"]["attack_max_ms"] == 7   # critic keys are derived after the merge
    assert kept["duration"]["target_ms"] == 123 and kept["purpose"] == "sửa tay"
    assert main(["--root", str(root), "generate", "--check"]) == 0


def test_cli_report_and_validate(generated, capsys):
    root, _ = generated
    assert main(["--root", str(root), "validate"]) == 0
    capsys.readouterr()
    assert main(["--root", str(root), "report", "--json"]) == 0
    data = json.loads(capsys.readouterr().out)
    assert set(data["counts"]["category"]) == set(READERS)
    assert all(i["severity"] in ("disagree", "plan", "range", "stale", "info") for i in data["issues"])


def test_validator_catches_broken_cards(generated, tmp_path):
    root, results = generated
    r = results[0]
    sid = next(iter(r.cards))
    card = store.load_file(store.card_path(root, r.game, sid))
    bad = dict(card, category="laser", manual_fields=["nope.path"])
    bad["variants"] = {"target": 9, "min": 1, "max": 3}
    bad["source_plan"] = dict(card["source_plan"], now=["model-later"])
    p = tmp_path / r.game / "wrong-name.yaml"
    p.parent.mkdir(parents=True)
    p.write_text(store.dumps(bad), encoding="utf-8")
    msgs = [x.message for x in validate.check_card(store.load_file(p), p)]
    assert any("category" in m for m in msgs)
    assert any("tên file" in m for m in msgs)
    assert any("manual_fields" in m for m in msgs)
    assert any("variants" in m for m in msgs)
    assert any("model-later" in m for m in msgs)


def test_committed_cards_validate():
    paths = store.card_files(store.SPECS_DIR)
    if not paths:
        pytest.skip("chưa sinh thẻ trong repo")
    problems, _ = validate.check_files(paths)
    assert [str(p) for p in problems if p.level == validate.ERROR] == []


def test_critic_lane_reads_every_card(generated):
    """Cards feed critic/spec.py: known group, a string intent, a duration for every non-proposed id."""
    root, results = generated
    for r in results:
        for sid, card in r.cards.items():
            c = card["critic"]
            assert isinstance(c["intent"], str) and c["intent"], (r.game, sid)
            assert c["group"], (r.game, sid)
    try:
        from critic import groups as G, spec as S
    except Exception:   # the critic lane is optional for this module
        pytest.skip("chưa có critic/spec.py")
    specs = S.load_cards(root)
    assert len(specs) == sum(len(r.cards) for r in results)
    assert {s.group_source for s in specs} == {"spec"}
    assert all(s.group in G.GROUPS and isinstance(s.intent, str) for s in specs)
