"""Owner calibration (§4.6): the versioned file, how the critic reads it, and the agreement report."""
from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from critic import agreement as AG
from critic import calibration as C
from critic import features, groups as G, pipeline, score
from critic import spec as S
from critic.tests import synth

PLAN = {"L2": 0.6, "L3": 0.3, "L4": 0.1, "L5": 0.0}


def _doc(**kw) -> dict:
    d = {"schema": C.SCHEMA, "version": "t1", "weights": {"rules": []}, "l2": {"rules": []}}
    d.update(kw)
    return d


def _spec(sid, group, game=None, **raw) -> S.Spec:
    return S.from_mapping({"id": sid, "group": group, "game": game, **raw})


# ------------------------------------------------------------------ the shipped file
def test_shipped_file_is_valid_and_is_the_default(monkeypatch):
    files = C.available()
    assert files and files[-1].name == "owner-v1.json"
    monkeypatch.delenv(C.ENV, raising=False)
    cal = C.load()
    assert cal is not None and cal.version == "1" and cal.date == "2026-10-24"
    assert C.load("1").path == cal.path and C.load("owner-v1").path == cal.path
    monkeypatch.setenv(C.ENV, "none")
    assert C.load() is None
    assert C.load("off") is None
    with pytest.raises(C.CalibrationError):
        C.load("99")


def test_shipped_rules_name_real_groups_families_and_features(tmp_path):
    cal = C.load("1")
    a = synth.write(tmp_path / "x.wav", synth.punchy())
    from critic import audio as A
    metrics, _ = features.analyze(A.load_checked(a), _spec("x", "hit_heavy"))
    for r in cal.weight_rules + cal.l2_rules:
        assert r.get("why_vi") and r.get("evidence"), r["id"]
        fam = (r.get("match") or {}).get("family")
        for f in (fam if isinstance(fam, list) else [fam] if fam else []):
            assert f in G.FAMILIES
    for r in cal.l2_rules:
        for d in r.get("set") or []:
            assert d["feature"] in metrics, d["feature"]
            assert d.get("low_vi") or d.get("high_vi")


def test_shipped_weights_lower_audiobox_only_where_it_disagreed():
    cal = C.load("1")
    for fam in ("trung", "ban", "phim-ui", "thuong"):
        w, rules = cal.weights(dict(PLAN), family=fam)
        assert w["L3"] == pytest.approx(0.099) and w["L2"] == pytest.approx(0.801) and w["L4"] == 0.1
        assert sum(w.values()) == pytest.approx(1.0) and rules == ["w-l3-audiobox"]
    for fam in ("nen", "no", "sinh-vat"):
        assert cal.weights(dict(PLAN), family=fam) == (PLAN, [])
    dirty = {"L2": 0.9, "L3": 0.0, "L4": 0.1, "L5": 0.0}
    assert cal.weights(dict(dirty), family="ban")[0] == pytest.approx(dirty)


# ------------------------------------------------------------------ validation
@pytest.mark.parametrize("bad", [
    {"L1": {"attack_max_ms": 150}},                                            # L1 is never calibrated
    {"hygiene": {}},
    {"weights": {"rules": [{"id": "a", "scale": {"L3": 1.5}}]}},                # only lower a weight
    {"weights": {"rules": [{"id": "a", "scale": {"L1": 0.5}}]}},                # L1 is not a ranking layer
    {"weights": {"rules": [{"id": "a", "scale": {"L3": 0.5}, "to": "L4"}]}},    # L4 cap 0.1 (§4.4)
    {"weights": {"rules": [{"id": "a", "match": {"group": "nope"}, "scale": {"L3": 0.5}}]}},
    {"weights": {"rules": [{"id": "a", "match": {"colour": "x"}, "scale": {"L3": 0.5}}]}},
    {"weights": {"rules": [{"id": "a", "scale": {"L3": 0.5}}, {"id": "a", "scale": {"L3": 0.5}}]}},
    {"l2": {"rules": [{"id": "t", "set": [{"feature": "crest_db", "good": [20, None], "bad": [25, None]}]}]}},
    {"l2": {"rules": [{"id": "t", "set": [{"feature": "crest_db"}]}]}},
    {"l2": {"rules": [{"id": "t", "weight": {"crest_db": -1}}]}},
    {"surprise": 1},
    {"version": ""},
])
def test_invalid_files_are_refused(bad):
    with pytest.raises(C.CalibrationError):
        C.from_dict(_doc(**bad))


def test_wrong_schema_is_refused(tmp_path):
    p = tmp_path / "owner-v7.json"
    p.write_text(json.dumps({"schema": "other/1", "version": "7"}), encoding="utf-8")
    with pytest.raises(C.CalibrationError):
        C.load(str(p))
    p.write_text("{not json", encoding="utf-8")
    with pytest.raises(C.CalibrationError):
        C.load(str(p))


def test_newest_version_wins_and_env_chooses(tmp_path, monkeypatch):
    for v in (2, 10):
        (tmp_path / f"owner-v{v}.json").write_text(json.dumps(_doc(version=str(v))), encoding="utf-8")
    monkeypatch.delenv(C.ENV, raising=False)
    assert C.load(directory=tmp_path).version == "10"          # numeric, not alphabetical
    monkeypatch.setenv(C.ENV, "2")
    assert C.load(directory=tmp_path).version == "2"
    monkeypatch.delenv(C.ENV)
    empty = tmp_path / "empty"
    empty.mkdir()
    assert C.load(directory=empty) is None                      # no file: the plan's weights and targets


# ------------------------------------------------------------------ rules
def test_weight_rules_keep_the_sum_and_last_match_wins():
    cal = C.from_dict(_doc(weights={"rules": [
        {"id": "a", "match": {"group": "hit_small"}, "scale": {"L3": 0.5}},
        {"id": "b", "match": {"id": "^hit\\.t1$"}, "scale": {"L3": 0.0}, "to": "L5"},
    ]}))
    w, applied = cal.weights(dict(PLAN), group="hit_small", sid="hit.t1")
    assert applied == ["a", "b"] and w["L3"] == 0.0 and w["L5"] == pytest.approx(0.3) and w["L2"] == 0.6
    w, applied = cal.weights(dict(PLAN), group="hit_small", sid="hit.t2")
    assert applied == ["a"] and w["L3"] == pytest.approx(0.15) and w["L2"] == pytest.approx(0.75)
    assert cal.weights(dict(PLAN), group="ui", sid="ui-move") == (PLAN, [])


def test_l2_rules_set_reweight_and_drop():
    cal = C.from_dict(_doc(l2={"rules": [
        {"id": "s", "match": {"group": "hit_small"}, "set": [
            {"feature": "crest_db", "good": [20, None], "bad": [12, None], "weight": 1.5},
            {"feature": "centroid_hz", "good": [2000, None], "bad": [500, None]}]},
        {"id": "w", "match": {"group": "hit_small"}, "weight": {"mud_share": 0.25}},
        {"id": "d", "match": {"game": "typing-survival"}, "drop": ["punch_db"]},
    ]}))
    base = list(G.get("hit_small").targets)
    out, changed = cal.targets(base, group="hit_small", game="typing-survival", sid="hit.t1")
    by = {t.feature: t for t in out}
    assert by["crest_db"].good == (20, G.INF) and by["crest_db"].weight == 1.5
    assert by["centroid_hz"].bad == (500, G.INF)                    # a new target is appended
    assert by["mud_share"].weight == 0.25 and "punch_db" not in by
    assert changed == {"crest_db": "s", "centroid_hz": "s", "mud_share": "w", "punch_db": "d"}
    out2, changed2 = cal.targets(base, group="hit_small", game="dragon-hold", sid="enemy.biped.hit")
    assert "punch_db" in {t.feature for t in out2} and "punch_db" not in changed2


def test_calibrated_attack_target_is_not_overridden_by_the_card():
    cal = C.load("1")
    sp = _spec("enemy.quadruped.howl", "creature", "dragon-hold", attack_max_ms=30)
    rows = {t.feature: (t, src) for t, src in features.targets_for(sp, None, cal)}
    t, src = rows["attack_ms"]
    assert src == "calibration:t-creature-whole-call" and t.good[1] == 150
    rows = {t.feature: (t, src) for t, src in features.targets_for(sp, None, None)}
    assert rows["attack_ms"][0].bad[1] == 30


# ------------------------------------------------------------------ owner cases, stored metrics (regression)
FOREST = {   # amb.forest 0b: E s2006 4/5 (bright), H s2004 3/5 (dark, the machine's old top)
    "E": {"share_above_3k": 0.538, "share_low300_hi4k10k": 0.482, "lufs_m_range_db": 6.54},
    "H": {"share_above_3k": 0.019, "share_low300_hi4k10k": 0.670, "lufs_m_range_db": 1.30},
}
HIT_T1 = {   # hit.t1 0b: raw Stable Audio 3 3/5; layered recipe v4 2/5 (L2 measures the rest as equal)
    "raw": {"duration_ms": 96, "attack_ms": 1.5, "onset_2k6k_share": 0.35, "share_200_800": 0.055, "crest_db": 17.86,
            "punch_db": 30, "tail_ms": 88, "mud_share": 0.015, "hf_attack_ms": 0.5},
    "v4": {"duration_ms": 96, "attack_ms": 1.5, "onset_2k6k_share": 0.26, "share_200_800": 0.567, "crest_db": 13.87,
           "punch_db": 30, "tail_ms": 84, "mud_share": 0.133, "hf_attack_ms": 1.25},
}
CHOP = {     # call-chop 0b: deep knock A 3/5, hollow mõ-like B 2/5
    "A": {"share_below_300": 0.792, "mud_share": 0.14},
    "B": {"share_below_300": 0.025, "mud_share": 0.072},
}


def _l2(m, sp, cal):
    return features.l2_score(m, sp, None, cal)["score"]


def test_owner_forest_pick_wins_only_after_calibration():
    cal = C.load("1")
    sp = _spec("amb.forest", "ambience", "dragon-hold")
    assert _l2(FOREST["E"], sp, None) < _l2(FOREST["H"], sp, None)
    assert _l2(FOREST["E"], sp, cal) > _l2(FOREST["H"], sp, cal)
    river = _spec("amb.river", "ambience", "dragon-hold")        # only forest beds are brightened
    assert _l2(FOREST["E"], river, cal) == _l2(FOREST["E"], river, None)


def test_owner_hit_t1_pick_wins_only_after_calibration_and_only_in_survival():
    cal = C.load("1")
    sp = _spec("hit.t1", "hit_small", "typing-survival")
    assert _l2(HIT_T1["raw"], sp, None) < _l2(HIT_T1["v4"], sp, None)
    assert _l2(HIT_T1["raw"], sp, cal) > _l2(HIT_T1["v4"], sp, cal)
    other = _spec("enemy.biped.hit", "hit_small", "dragon-hold")
    assert _l2(HIT_T1["raw"], other, cal) == _l2(HIT_T1["raw"], other, None)


def test_owner_call_chop_knock_beats_the_mo_like_contrast():
    cal = C.load("1")
    sp = _spec("call-chop", "generic", "typing-defense")
    assert _l2(CHOP["A"], sp, None) == _l2(CHOP["B"], sp, None)
    assert _l2(CHOP["A"], sp, cal) > _l2(CHOP["B"], sp, cal)


def test_l2_rows_say_which_rule_changed_them():
    cal = C.load("1")
    r = features.l2_score(FOREST["E"], _spec("amb.forest", "ambience", "dragon-hold"), None, cal)
    src = {row["feature"]: row["source"] for row in r["targets"]}
    assert src["share_above_3k"] == "calibration:t-amb-forest-bright" and r["calibration"] == "1"
    assert features.l2_score(FOREST["E"], _spec("amb.forest", "ambience"), None, None)["calibration"] is None


# ------------------------------------------------------------------ combine and the pipeline
def _fake(n, l2, l3, family="trung"):
    return {"file": {"name": f"f{n}.wav", "stem": f"f{n}"}, "verdict": "PASS", "flags": [],
            "spec": {"id": "x", "path": "card.yaml", "group": "hit_small", "family": family, "dirty": False,
                     "group_source": "spec"},
            "metrics": {"centroid_hz": 1000 + n, "duration_ms": 90},
            "L2": {"score": l2}, "L3": {"available": True, "scores": {"PQ": l3, "CE": l3}}, "L4": None, "L5": None}


def test_combine_uses_the_calibrated_weights_and_records_them():
    rs = [_fake(i, l2=0.1 * i, l3=8 - i) for i in range(4)]
    score.combine(rs, n_refs=0, calibration=C.load("1"))
    s = rs[0]["score"]
    assert s["weights_plan"] == PLAN and s["calibration"] == "1" and s["calibration_rules"] == ["w-l3-audiobox"]
    assert s["weights_used"]["L3"] == pytest.approx(0.099 / 0.9, abs=1e-3)       # L4/L5 did not run
    assert [r["score"]["rank"] for r in rs] == [4, 3, 2, 1]                        # L2 now leads
    plain = [_fake(i, l2=0.1 * i, l3=8 - i) for i in range(4)]
    score.combine(plain, n_refs=0)
    assert plain[0]["score"]["calibration"] is None and plain[0]["score"]["calibration_rules"] == []


def test_pipeline_reads_a_calibration_file(tmp_path):
    d = tmp_path / "in"
    synth.write(d / "imp_a.wav", synth.punchy())
    synth.write(d / "imp_b.wav", synth.muddy())
    cards = tmp_path / "cards.yaml"
    cards.write_text("- id: imp\n  game: typing-survival\n  group: hit_heavy\n", encoding="utf-8")
    calf = tmp_path / "owner-v3.json"
    calf.write_text(json.dumps(_doc(version="3", l2={"rules": [
        {"id": "t-x", "match": {"group": "hit_heavy"}, "set": [
            {"feature": "centroid_hz", "good": [100, None], "bad": [50, None], "high_vi": "x"}]}]})),
        encoding="utf-8")
    out = tmp_path / "out"
    batch = pipeline.run([str(d)], spec_path=str(cards), out_dir=out,
                         opts=pipeline.Options(layers=("L1", "L1b", "L2"), quiet=True, calibration=str(calf)))
    r = json.loads((out / "imp_a.json").read_text(encoding="utf-8"))
    import jsonschema
    from critic.schema import FILE_SCHEMA
    jsonschema.validate(r, FILE_SCHEMA)
    assert batch["calibration"]["version"] == "3" and r["L2"]["calibration"] == "3"
    assert any(t["source"] == "calibration:t-x" for t in r["L2"]["targets"])
    assert "owner-v3.json" in (out / "summary.md").read_text(encoding="utf-8")
    out2 = tmp_path / "out2"
    batch = pipeline.run([str(d)], spec_path=str(cards), out_dir=out2,
                         opts=pipeline.Options(layers=("L1", "L1b", "L2"), quiet=True, calibration="none"))
    assert batch["calibration"] is None
    r = json.loads((out2 / "imp_a.json").read_text(encoding="utf-8"))
    assert not any(t["source"].startswith("calibration") for t in r["L2"]["targets"])


# ------------------------------------------------------------------ agreement
def _item(stars: dict, pick: str, roles: dict | None = None) -> AG.Item:
    it = AG.Item("g", "x", "0a", "s", "trung", "hit_small", False, "", None, [])
    for k, s in stars.items():
        it.cands.append(AG.Cand(k, (roles or {}).get(k, "top"), s, k == pick, Path(f"/r/{k}.json")))
    return it


def _res(values: dict) -> dict:
    return {f"/r/{k}.json": {"verdict": "PASS", "score": {"combined": v, "rank": None}} for k, v in values.items()}


def test_pairs_ties_and_top_pick():
    it = _item({"a": 3, "b": 2, "c": 2}, "a")
    st = AG.item_stats(it, _res({"a": 0.9, "b": 0.1, "c": 0.5}), "combined")
    assert (st["pairs_agree"], st["pairs"], st["top_pick"]) == (2.0, 2, 1.0)    # b-c same stars: no pair
    st = AG.item_stats(it, _res({"a": 0.1, "b": 0.1, "c": 0.9}), "combined")
    assert (st["pairs_agree"], st["top_pick"]) == (0.5, 0.0)                     # a-b machine tie = half
    st = AG.item_stats(it, _res({"a": 0.5, "b": 0.5, "c": 0.1}), "combined")
    assert st["top_pick"] == 0.5                                                 # 2-way tie at the top


def test_pairs_across_two_critic_runs_are_not_compared():
    """Batch 1c review: a take ranked only at raw stage (critic-info-<id>) next to final-stage takes (critic-final):
    their combined z-scores come from two rank groups, so those pairs are counted apart and the item has no top pick."""
    it = AG.Item("g", "x", "1c", "s", "trung", "hit_fire", False, "", None, [])
    for k, s, d in (("a", 4, "final"), ("b", 2, "final"), ("c", 3, "info")):
        it.cands.append(AG.Cand(k, "top", s, k == "a", Path(f"/{d}/{k}.json")))
    res = {f"/{d}/{k}.json": {"verdict": "PASS", "score": {"combined": v, "rank": None}}
           for k, v, d in (("a", 0.9, "final"), ("b", 0.1, "final"), ("c", 2.0, "info"))}
    st = AG.item_stats(it, res, "combined")
    assert (st["pairs_agree"], st["pairs"], st["cross_run_pairs"], st["top_pick"]) == (1.0, 1, 2, None)


def test_roles_by_family_and_loop_only_features():
    it = _item({"a": 2, "p": 3}, "p", roles={"a": "top", "p": "probe"})
    rf = AG.roles_by_family([it])
    assert rf["trung"] == {"n": 1, "pick": {"probe": 1}, "probe_items": 1, "probe_picked": 1}
    one_shot = {"spec": {"loop": False}, "metrics": {"lufs_m_range_db": 9.0, "crest_db": 12.0}}
    assert AG.feature(one_shot, "lufs_m_range_db") is None and AG.feature(one_shot, "crest_db") == 12.0
    assert AG.feature({"spec": {"loop": True}, "metrics": {"lufs_m_range_db": 9.0}}, "lufs_m_range_db") == 9.0


def test_partial_calibrations_split_weights_targets_and_rules():
    cal = C.load("1")
    w = AG.partial(cal, l2=False)
    t = AG.partial(cal, weights=False)
    assert w.weight_rules == cal.weight_rules and w.l2_rules == []
    assert t.weight_rules == [] and t.l2_rules == cal.l2_rules
    d = AG.partial(cal, drop="t-hit-boom")
    assert [r["id"] for r in d.l2_rules] == [r["id"] for r in cal.l2_rules if r["id"] != "t-hit-boom"]


def test_rescore_without_calibration_reproduces_the_stored_ranks(synth_run):
    stored = AG._load_dir(synth_run["out"])
    again = AG.rescore(stored, None)
    for r in stored:
        assert again[r["_json"]]["score"].get("rank") == r["score"].get("rank")
        if (r.get("L2") or {}).get("score") is not None:
            assert again[r["_json"]]["L2"]["score"] == pytest.approx(r["L2"]["score"])
    # and the input is not mutated
    assert copy.deepcopy(stored) == stored
