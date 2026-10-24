import copy

from critic import score


def test_punchy_ranks_above_weak_and_muddy_in_its_family(synth_run):
    res = synth_run["res"]
    p, w, m = res["imp_punchy"], res["imp_weak"], res["imp_muddy"]
    assert p["score"]["rank_group"] == w["score"]["rank_group"] == m["score"]["rank_group"] == "id:imp"
    assert p["score"]["rank"] == 1
    assert p["score"]["rank"] < w["score"]["rank"]
    assert p["score"]["rank"] < m["score"]["rank"]
    assert p["L2"]["score"] > w["L2"]["score"] and p["L2"]["score"] > m["L2"]["score"]
    # a smeared crack (model artefact) also ranks below the clean layered hit
    assert p["score"]["rank"] < res["imp_smeared"]["score"]["rank"]


def test_blocked_files_are_not_ranked(synth_run):
    for n, r in synth_run["res"].items():
        if r["verdict"] == "BLOCK":
            assert r["score"]["rank"] is None and r["score"]["combined"] is None


def test_l2_notes_speak_sound_design(synth_run):
    weak = " ".join(synth_run["res"]["imp_weak"]["notes_vi"])
    muddy = " ".join(synth_run["res"]["imp_muddy"]["notes_vi"])
    assert "sub" in weak or "thân" in weak
    assert "ù" in muddy or "tách" in muddy or "sub" in muddy


def test_listening_list_has_top_and_distinct(synth_run):
    e = synth_run["batch"]["listen"]["id:imp"]
    assert e["top"] == "imp_punchy"                     # result stems: unique per run (two dirs, same name)
    assert e["distinct"] in {"imp_weak", "imp_muddy"}


def _fake(n, l2, l3, dirty=False):
    return {"file": {"name": f"f{n}.wav", "stem": f"f{n}"}, "verdict": "PASS", "flags": [],
            "spec": {"id": "x", "path": "card.yaml", "group": "hit_heavy", "dirty": dirty, "group_source": "spec"},
            "metrics": {"centroid_hz": 1000 + n, "duration_ms": 200},
            "L2": {"score": l2}, "L3": {"available": True, "scores": {"PQ": l3, "CE": l3}}, "L4": None, "L5": None}


def test_weights_and_disagreement_rule():
    rs = [_fake(i, l2=0.1 * i, l3=8 - i) for i in range(6)]      # L2 and L3 in opposite order
    score.combine(rs, n_refs=0)
    for r in rs:
        assert r["score"]["weights_used"] == {"L2": 0.667, "L3": 0.333, "L4": 0.0, "L5": 0.0}
    # ranks differ by 5 at both ends -> ask the owner
    assert rs[0]["ask_owner"]["value"] and rs[5]["ask_owner"]["value"]
    assert not rs[2]["ask_owner"]["value"]


def test_dirty_family_drops_audiobox():
    rs = [_fake(i, l2=0.1 * i, l3=8 - i, dirty=True) for i in range(6)]
    score.combine(rs, n_refs=0)
    assert rs[0]["score"]["stage"] == "batch1-dirty"
    assert rs[0]["score"]["weights_used"]["L3"] == 0.0
    assert [r["score"]["rank"] for r in rs] == [6, 5, 4, 3, 2, 1]
    assert not any(r["ask_owner"]["value"] for r in rs)


def test_ref5_stage_turns_on_l5():
    assert score.stage_for(False, 5) == "ref5"
    assert score.stage_for(True, 7) == "ref5-dirty"
    assert score.stage_for(True, 10) == "ref5"


def test_flags_ask_the_owner_and_force_the_card():
    rs = [_fake(i, l2=0.5, l3=5) for i in range(3)]
    rs[1]["flags"] = [{"layer": "L1b", "id": "pre_echo", "msg_vi": "có tiếng vọng"}]
    score.combine(rs, n_refs=0)
    assert rs[1]["ask_owner"]["value"] and rs[1]["read_card"]


def test_probe_is_deterministic_per_seed():
    rs = [_fake(i, l2=0.1 * i, l3=5) for i in range(8)]
    a = score.combine(copy.deepcopy(rs), n_refs=0, seed=3)["listen"]
    b = score.combine(copy.deepcopy(rs), n_refs=0, seed=3)["listen"]
    assert a == b
    probes = {score.combine(copy.deepcopy(rs), n_refs=0, seed=s)["listen"]["id:x"]["probe"] is not None
              for s in range(40)}
    assert probes == {True, False}      # about 30 % of ids get one


def _l4(fid):
    return {"layer": "L4", "id": fid, "msg_vi": fid}


def test_uncalibrated_ast_flags_never_ask_the_owner():
    rs = [_fake(i, l2=0.5, l3=5) for i in range(4)]
    rs[0]["flags"] = [_l4("ast_expected_missing")]
    rs[1]["flags"] = [_l4("ast_low_conf")]
    score.combine(rs, n_refs=0)
    assert not any(r["ask_owner"]["value"] for r in rs)
    assert rs[0]["flags"][0]["ask"] is False


def test_l4_flag_asks_only_when_it_separates_candidates():
    rs = [_fake(i, l2=0.5, l3=5) for i in range(4)]
    for r in rs:                                   # every candidate: a property of the id, not a candidate
        r["flags"] = [_l4("clap_expected_missing")]
    rs[2]["flags"].append(_l4("clap_material"))   # only one: it separates
    score.combine(rs, n_refs=0)
    assert [r["ask_owner"]["value"] for r in rs] == [False, False, True, False]
    st = score.ask_stats(rs)
    assert st["ask_owner"] == 1 and st["flags"]["L4:clap_expected_missing"] == {"files": 4, "ask": 0}


def test_probe_comes_from_the_lower_half_only():
    for seed in range(60):
        rs = [_fake(i, l2=0.1 * i, l3=5) for i in range(8)]
        rs[7]["flags"] = [{"layer": "L1b", "id": "pre_echo", "msg_vi": "x"}]   # rank 1, flagged
        e = score.combine(rs, n_refs=0, seed=seed)["listen"]["id:x"]
        if e["probe"]:
            r = next(r for r in rs if r["file"]["stem"] == e["probe"])
            assert r["score"]["rank"] > 4 and r["file"]["stem"] != e["distinct"]
