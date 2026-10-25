"""Batch 1c (Q6_REWRITE §7): the job table generates only the Q6 keys, at the §7 lengths, with names no earlier batch
used, and the rebuilt recipes are valid for the Q6 lengths of their cards."""
import json

import pytest

from common import batch0b, batch1_dh, batch1_td, batch1_ts, batch1c
from gen import sa3

# Q6_REWRITE_2026-10-24.md §7: id -> (keys to generate, pick_seconds), in the order of the table
Q6_TABLE = {
    "dragon-hold": [("fire.cast", "EFGH", 2.0), ("fire.impact.a", "EFGH", 1.0), ("fire.impact.b", "FGHI", 1.0),
                    ("fire.impact.c", "CDEF", 2.0), ("impact.multi", "ABCD", 2.0),
                    ("trap.pine-bomb.trigger", "CDEF", 2.0), ("enemy.quadruped.howl", "EFG", 2.0)],
    "typing-defense": [("arrow-fire", "EFGH", 1.0), ("wordshot-fire", "EFGH", 1.0), ("ink-puff", "EFGH", 1.0),
                       ("blast", "EFGH", 2.0), ("call-chop", "GH", 1.0)],
    "typing-survival": [("kill.swarm", "EF", 1.0), ("kill.elite", "EFGH", 1.0), ("hurt.breach", "DEF", 2.0),
                        ("gun.xung", "IJK", 1.0), ("hit.t1", "FGHI", 1.0), ("hit.t2", "EFGH", 1.0),
                        ("hit.t4", "EFG", 2.0)],
}


def test_games_and_ids_follow_the_q6_order():
    assert tuple(batch1c.JOBS) == ("dragon-hold", "typing-defense", "typing-survival")
    for game, rows in Q6_TABLE.items():
        assert list(batch1c.JOBS[game]) == [sid for sid, _, _ in rows]


@pytest.mark.parametrize("game", list(Q6_TABLE))
def test_rows_hold_the_q6_keys_and_the_section_7_lengths(game):
    for sid, keys, secs in Q6_TABLE[game]:
        card = sa3.read_card(batch1c.card_path(game, sid))
        rows = batch1c.JOBS[game][sid]
        main = [r for r in rows if not r.get("extra_length")]
        assert len(main) == 1, sid
        assert "".join(main[0]["variants"]) == keys, sid
        assert main[0]["seconds"] == secs == sa3.pick_seconds(card), sid
        for r in rows:
            assert set(r["variants"]) <= set(sa3.prompts_from_card(card)), sid
        assert all(r["variants"] == main[0]["variants"] for r in rows), sid
    howl = batch1c.JOBS["dragon-hold"]["enemy.quadruped.howl"]
    if game == "dragon-hold":
        assert sorted(r["seconds"] for r in howl) == [2.0, 3.0] and all(r.get("tag") for r in howl)


@pytest.mark.parametrize("game", list(Q6_TABLE))
def test_every_job_builds_and_passes_the_q6_word_check(game):
    jobs = batch1c.build_jobs(game)          # gen.sa3.check_prompts raises on a forbidden word or key
    names = [it["name"] for _, _, job in jobs for it in job["items"]]
    assert len(names) == len(set(names))
    for _, _, job in jobs:
        for text in job["_meta"]["variants"].values():
            for pat in sa3.Q6_TERMS:
                assert not __import__("re").search(pat, text, __import__("re").I), text


def _triples(table: dict) -> set[tuple[str, str, int]]:
    out = set()
    for sid, rows in table.items():
        for r in rows:
            for k in r["variants"]:
                for s in sa3.parse_seeds(r["seeds"]):
                    out.add((sid, k, s))
    return out


def test_no_take_repeats_an_earlier_batch():
    old = (_triples(batch1_dh.JOBS) | _triples(batch1_td.JOBS) | _triples(batch1_ts.JOBS)
           | _triples(batch0b.NEW_JOBS))
    new = set().union(*(_triples(t) for t in batch1c.JOBS.values()))
    assert not new & old
    assert min(s for _, _, s in new) >= 3001          # the 0b trial used 1001-1006, batch 0b/1 2001-2006
    assert {s for sid, k, s in new if sid == "call-chop"} == set(range(3101, 3107))


def _fake_pool(tmp_path, name: str, n: int, length: float) -> list[dict]:
    rows = []
    for i in range(n):
        rec = tmp_path / f"{name}__{'EFGH'[i % 4]}__s{3001 + i}.json"
        rec.write_text(json.dumps({"schema": sa3.RECORD_SCHEMA, "model": {"id": "repo@rev"}}), "utf-8")
        rows.append({"file": str(rec.with_suffix(".f32.wav")), "record": str(rec), "window": [0.01, 0.01 + length],
                     "name": rec.stem})
    return rows


def test_recipes_are_valid_and_fit_the_q6_lengths(tmp_path):
    from build import recipe

    pools = {key: {"bodies": _fake_pool(tmp_path, key, 8, 0.5)} for key in
             ("fire-a", "fire-b", "fire-c", "pine", "t4", "elite", "breach", "wordshot", "blast")}
    built = {g: batch1c.RECIPES[g](pools) for g in batch1c.GAMES}
    for g, recs in built.items():
        assert set(recs) == set(batch1c.RECIPE_IDS[g])
        for rid, data in recs.items():
            recipe.validate(data, rid)
            card = sa3.read_card(batch1c.card_path(g, batch1c.sid_of(g, rid)))
            d = card["duration"]
            cap = data["chain"]["maxLengthMs"]
            assert d["min_ms"] < cap <= d["max_ms"], (rid, cap, d)
            assert data["chain"]["tail"]["shape"] == "exp" and data["chain"]["tail"]["kneeMs"] < cap
            assert 1 <= data["variants"]["count"] <= 8
            # Q6 rule 3: a sub is only a layer under a body; never the loudest layer of the recipe
            subs = [lay for lay in data["layers"] if lay.get("role") == "sub"]
            assert all(lay.get("gainDb", 0) <= -9 for lay in subs), rid
            assert any(lay.get("role") in ("body", "texture") for lay in data["layers"]), rid
    assert batch1c.recipe_path("dragon-hold", "fire.impact.a").name == "fire.impact.a.b1c.json"


def test_round_robin_spreads_the_prompts():
    rows = [{"p": p, "i": i} for p, i in [("E", 0), ("E", 1), ("E", 2), ("F", 0), ("G", 0), ("G", 1)]]
    out = batch1c._round_robin(rows, lambda r: r["p"])
    assert [r["p"] for r in out] == ["E", "F", "G", "E", "G", "E"]


def test_q6_checks_follow_the_decisions_proposal():
    def doc(sid, game, group, family, target, **m):
        return {"spec": {"id": sid, "game": game, "group": group, "family": family, "duration_target_ms": target},
                "metrics": m}
    # a lone low hit: 120 ms of 80 Hz, no body, no tail
    lone = batch1c.q6_checks(doc("fire.impact.a", "dragon-hold", "hit_fire", "trung", 600, tail_ms=60, punch_db=35,
                                 share_150_800=0.01, share_below_150=0.9))
    assert lone == {"tail": "trượt", "punch": "trượt", "body": "trượt", "lone_low_hit": "trượt"}
    shaped = batch1c.q6_checks(doc("fire.impact.a", "dragon-hold", "hit_fire", "trung", 600, tail_ms=380, punch_db=12,
                                   share_150_800=0.3, share_below_150=0.3))
    assert shaped == {"tail": "đạt", "punch": "đạt", "body": "đạt"}
    # short sounds: no lone-low rule (punch_db reads their decay); gun.xung never
    assert "punch" not in batch1c.q6_checks(doc("kill.swarm", "typing-survival", "death_swarm", "chet", 250, punch_db=30))
    assert batch1c.q6_checks(doc("gun.xung", "typing-survival", "shot_gun", "ban", 0, punch_db=40, tail_ms=96,
                                 share_below_150=0.83)) == {}
    assert batch1c.q6_checks(doc("hit.t2", "typing-survival", "hit_heavy", "trung", 260, punch_db=40, tail_ms=132,
                                 share_below_150=0.72)) == {"tail": "đạt", "lone_low_hit": "trượt"}
    assert batch1c.q6_checks(doc("hit.t1", "typing-survival", "hit_small", "trung", 140, tail_ms=40)) == {"tail": "giữa"}
