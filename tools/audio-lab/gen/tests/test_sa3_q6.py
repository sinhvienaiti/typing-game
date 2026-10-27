"""gen/sa3.py, DECISIONS Q6: the 'bụp, thụp' words are refused in every game, and every committed card passes.

Needs only PyYAML (no numpy, soundfile or model), so it also runs on a machine without the Audio Lab venv.
"""
from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from gen import sa3

SPECS = Path(__file__).resolve().parents[2] / "specs"
GAMES = ("dragon-hold", "typing-defense", "typing-survival")


def card(game: str, *variants: str) -> dict:
    return {"id": "fire.test", "game": game, "duration": {"target_ms": 600, "min_ms": 480, "max_ms": 720},
            "prompt": {"text": "x", "variants": list(variants)}, "_path": "fire.test.yaml"}


def test_q6_words_are_refused_in_every_game():
    banned = ("a deep fireball whoomph launch", "a soft puff of smoke", "flame puffs", "a small pop", "popping embers",
              "like a balloon bursting", "a spring boing", "two wooden bonks", "a toy cannon", "toy-like and friendly",
              "a cartoon blast", "retro arcade hit", "8-bit explosion", "8 bit laser", "chiptune jingle",
              "tiếng bụp", "THỤP xuống")
    for game in GAMES:
        for text in banned:
            with pytest.raises(sa3.Sa3Error, match="Q6"):
                sa3.check_prompts({"id": "x", "game": game}, {"A": text})


def test_the_packs_puff_words_and_their_spellings_are_refused_too():
    """04-audio*.md ban poof; the Q6 pass removed plop, fwoomp, thoomp by hand; whoomp is whoomph without the h."""
    banned = ("a soft poof of smoke", "poofs of dust", "a wet plop", "plopping into water", "a big fwoomp",
              "a low thoomp", "a deep whoomp", "WHOOMPH of flame", "a round woomph", "fwhoomp of fire")
    for game in GAMES:
        for text in banned:
            with pytest.raises(sa3.Sa3Error, match="Q6"):
                sa3.check_prompts({"id": "x", "game": game}, {"A": text})


def test_q6_words_are_whole_words_and_a_layered_low_hit_passes():
    for game in GAMES:
        sa3.check_prompts({"id": "x", "game": game}, {
            "D": "a shot with real oomph, a whoosh and a boom, a ploughed field, a poodle barking",
            "A": "a population of crickets, a popular folk tune, puffin calls on a cliff",
            "B": "a hard crack, a heavy clang with a thick steel body and a deep layer underneath, a long ring",
            "C": "one low knock of an axe handle on bamboo, hollow woody thud with tiny splinter crackles"})


def test_a_job_with_a_banned_prompt_is_refused_and_names_the_decision():
    ok = card("dragon-hold", "E: a large beast hisses, fire catches under pressure and roars, a dense whoosh away")
    assert [it["name"] for it in sa3.build_job(ok, seeds=[1])["items"]] == ["fire.test__E__s1"]
    bad = card("dragon-hold", "A: dragon spit with a round whoomph launch", "E: fire catches and roars away")
    with pytest.raises(sa3.Sa3Error, match="Q6"):
        sa3.build_job(bad, seeds=[1])
    assert [it["name"] for it in sa3.build_job(bad, variants=["E"], seeds=[1])["items"]] == ["fire.test__E__s1"]


def test_q2_terms_still_hold_for_loi_goi_only():
    with pytest.raises(sa3.Sa3Error, match="Q2"):
        sa3.check_prompts({"id": "x", "game": "typing-defense"}, {"A": "a temple block tap"})
    sa3.check_prompts({"id": "x", "game": "typing-survival"}, {"A": "a temple block tap"})


def test_every_committed_card_passes_the_q6_check():
    paths = sorted(p for g in GAMES for p in (SPECS / g).glob("*.yaml"))
    assert len(paths) >= 140
    refused = []
    for p in paths:
        c = yaml.safe_load(p.read_text(encoding="utf-8"))
        prompts = {}
        try:
            prompts = sa3.prompts_from_card(c)
        except sa3.Sa3Error:
            continue                       # a card without a prompt (hit.sub, hit.tail, music stems)
        keep = {k: v for k, v in prompts.items() if k not in sa3.FORBIDDEN_KEYS.get((c["game"], c["id"]), ())}
        try:
            sa3.check_prompts(c, keep)
        except sa3.Sa3Error as e:
            refused.append(str(e))
    assert refused == []
