"""batch0 never silently replaces a listening session the owner may be rating (review finding)."""
import json

import pytest

from common import batch0


def test_session_files_are_not_overwritten_without_force(tmp_path, monkeypatch):
    monkeypatch.setattr(batch0.env, "REVIEW", tmp_path)
    items = [{"id": "calib-1", "source_id": "kenney_x", "candidates": ["a.wav"]}]
    p = batch0._write_session("_calib", "0a-calib", "t", items)
    doc = json.loads(p.read_text("utf-8"))
    assert doc["reveal"] == "end" and doc["items"][0]["id"] == "calib-1"
    with pytest.raises(batch0.SessionExists, match="--force"):
        batch0._write_session("_calib", "0a-calib", "t2", items)
    assert json.loads(p.read_text("utf-8"))["title"] == "t"
    batch0._write_session("_calib", "0a-calib", "t2", items, force=True)
    assert json.loads(p.read_text("utf-8"))["title"] == "t2"


def test_wave_horn_is_a_recipe_not_a_raw_render():
    assert "dragon-hold/wave.horn" in batch0.RECIPES and "wave.horn-sampler" not in batch0.SAMPLER
    assert (batch0.LAB / "build" / "recipes" / "dragon-hold" / "wave.horn.json").is_file()
