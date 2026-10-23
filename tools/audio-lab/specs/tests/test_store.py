import copy

from specs import store


def _card():
    return {
        "schema": 1, "id": "x.y", "game": "dragon-hold", "status": "draft", "manual_fields": [],
        "duration": {"target_ms": 100, "min_ms": 80, "max_ms": 120},
        "prompt": {"text": "gen", "variants": []},
        "references": [], "notes": "",
        "playback": {"mode": "one-shot", "caps": {}},
    }


def test_merge_without_existing_is_generated():
    gen = _card()
    out, kept = store.merge(gen, None)
    assert out is gen and kept == []


def test_merge_keeps_hand_owned_fields():
    gen = _card()
    old = copy.deepcopy(gen)
    old["status"] = "approved"
    old["notes"] = "đã nghe, giữ"
    old["references"] = [{"path": "~/AudioLab/libraries/kenney/a.ogg", "licence": "CC0-1.0"}]
    old["prompt"]["variants"] = ["a", "b"]
    old["prompt"]["text"] = "old text"          # not hand-owned: regenerated
    out, kept = store.merge(gen, old)
    assert out["status"] == "approved" and out["notes"] == "đã nghe, giữ"
    assert out["references"][0]["licence"] == "CC0-1.0"
    assert out["prompt"]["variants"] == ["a", "b"]
    assert out["prompt"]["text"] == "gen"
    assert {"status", "notes", "references", "prompt.variants"} <= set(kept)


def test_merge_keeps_manual_sections_and_fields():
    gen = _card()
    old = copy.deepcopy(gen)
    old["duration"] = {"target_ms": 150, "min_ms": 140, "max_ms": 160, "manual": True}
    old["playback"]["mode"] = "loop"
    old["manual_fields"] = ["playback.mode"]
    gen["duration"]["target_ms"] = 99
    out, kept = store.merge(gen, old)
    assert out["duration"] == {"target_ms": 150, "min_ms": 140, "max_ms": 160, "manual": True}
    assert out["playback"]["mode"] == "loop"
    assert "duration" in kept and "playback.mode" in kept


def test_merge_whole_card_manual_and_unknown_keys():
    gen = _card()
    old = copy.deepcopy(gen)
    old["manual"] = True
    old["duration"]["target_ms"] = 1
    out, kept = store.merge(gen, old)
    assert out is old and kept == ["*"]

    old2 = copy.deepcopy(gen)
    old2["extra_note"] = "giữ"
    out2, kept2 = store.merge(gen, old2)
    assert out2["extra_note"] == "giữ" and "extra_note" in kept2


def test_dump_roundtrip_and_layout():
    card = _card()
    card["playback"]["caps"] = {"per_s": 4}
    card["duration"]["range"] = [120, 800]
    card["notes"] = "dòng 1\ndòng 2"
    text = store.dumps(card)
    assert text.startswith("# Thẻ spec âm thanh")
    assert "range: [120, 800]" in text
    assert "notes: |" in text
    assert store.loads(text) == card


def test_write_if_changed(tmp_path):
    p = tmp_path / "g" / "a.yaml"
    assert store.write_if_changed(p, "x") == "created"
    assert store.write_if_changed(p, "x") == "unchanged"
    assert store.write_if_changed(p, "y") == "updated"
