from pathlib import Path

import pytest

from build import ledger, policy, recipe
from build.tests.helpers import recipe as make_recipe

EXAMPLES = Path(__file__).resolve().parent.parent / "examples"


@pytest.mark.parametrize("path", sorted(EXAMPLES.glob("*.json")), ids=lambda p: p.name)
def test_examples_validate(path):
    recipe.load(path)


def test_bad_recipe_is_rejected():
    r = make_recipe()
    r["layers"][0]["source"] = {"library": "x.wav", "synth": "click"}    # two sources
    with pytest.raises(recipe.RecipeError):
        recipe.validate(r)
    r = make_recipe()
    r["layers"][1]["id"] = r["layers"][0]["id"]
    with pytest.raises(recipe.RecipeError):
        recipe.validate(r)


def test_hash_ignores_prose_only():
    r = make_recipe()
    h = recipe.recipe_hash(r)
    assert recipe.recipe_hash({**r, "description": "khác"}) == h
    assert recipe.recipe_hash({**r, "variants": {**r["variants"], "seed": 1}}) != h


def test_ranges_clamped_to_group_and_spec(tmp_path):
    r = make_recipe()
    r["group"] = "ui"
    plans, warns, src = recipe.plan_variants(r)
    assert src == "group:rare-fixed" and all(p.pitch_cents == 0 and p.gain_db == 0 for p in plans)
    assert any("vượt giới hạn" in w for w in warns)
    card = tmp_path / "card.yaml"
    card.write_text("variation:\n  pitchCents: 10\n  gainDb: 0.5\n")
    plans, _, src = recipe.plan_variants(make_recipe(count=8), recipe.read_spec_limits(card))
    assert src == "spec" and all(abs(p.pitch_cents) <= 10 and abs(p.gain_db) <= 0.5 for p in plans)


def test_policy_classification():
    assert policy.classify("CC0-1.0") == "allowed"
    assert policy.classify("CC0") == "allowed"
    assert policy.classify("LicenseRef-AudioLab-code") == "allowed"
    for bad in ("CC-BY-NC-4.0", "CC-BY-NC-SA-3.0", "LicenseRef-Freesound-Sampling+", "CC-BY-ND-4.0",
                "LicenseRef-qwen-research", "LicenseRef-ElevenLabs-free"):
        assert policy.classify(bad) == "denied", bad
    assert policy.classify("LicenseRef-Whatever") == "unknown"
    assert policy.model_denied("facebook/audiogen-medium") and not policy.model_denied("laion/clap-htsat-unfused")


def test_licence_row_schema_requires_date_url_hash():
    row = {"schema": "audiolab.licence/1", "kind": "model", "key": "model:x@y", "repo": "x", "revision": "y",
           "role": "critic", "commercial_ok": True, "licence": "Apache-2.0"}
    errs = ledger.schema_errors("licences", row)
    assert any("date" in e for e in errs) and any("licenceUrl" in e for e in errs) and any("sha256" in e for e in errs)


def test_spec_card_randomisation_block(tmp_path):
    """Spec cards from the specs lane: randomisation {group, pitch_cents, gain_db}, variants.target."""
    card = tmp_path / "hit.test.yaml"
    card.write_text("id: hit.test\nvariants: {target: 5, min: 4, max: 6}\n"
                    "randomisation: {group: key-bad, pitch_cents: 30, gain_db: null, rules: []}\n")
    r = make_recipe()
    del r["variants"]["count"]
    spec = recipe.read_spec(card)
    plans, warns, src = recipe.plan_variants(r, spec)
    assert src == "spec:key-bad" and len(plans) == 5
    assert all(abs(p.pitch_cents) <= 30 and p.gain_db == 0 for p in plans)     # null gain = no gain change
    assert all(abs(lp.pitch_cents) <= 30 and lp.gain_db == 0 for p in plans for lp in p.layers.values())
    card.write_text("id: other.id\nrandomisation: {group: default, pitch_cents: null, gain_db: null, rules: []}\n")
    plans, warns, src = recipe.plan_variants(make_recipe(), recipe.read_spec(card))
    assert src == "spec:default" and any("other.id" in w for w in warns)
    assert any(abs(p.pitch_cents) > 0 for p in plans[1:])                    # unlimited: recipe ranges kept
