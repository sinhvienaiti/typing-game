"""Real learned layers (audiobox, CLAP x2, AST) from the offline cache. Opt-in: AUDIOLAB_TEST_MODELS=1."""
import json
import os

import pytest

from critic import learned, pipeline
from critic.tests import synth

pytestmark = pytest.mark.models


def test_learned_layers_rank_and_flag_only(tmp_path):
    assert os.environ.get("HF_HUB_OFFLINE") == "1"
    assert not os.environ.get("HF_TOKEN")
    d = tmp_path / "in"
    synth.write(d / "imp_punchy.wav", synth.punchy())
    synth.write(d / "imp_weak.wav", synth.weak_click())
    synth.write(d / "imp_muddy.wav", synth.muddy())
    synth.write(d / "imp_clipped.wav", synth.clipped(), subtype="PCM_16")
    (tmp_path / "cards.yaml").write_text(synth.CARDS, encoding="utf-8")
    out = tmp_path / "out"
    batch = pipeline.run([str(d)], spec_path=str(tmp_path / "cards.yaml"), out_dir=out,
                         opts=pipeline.Options(layers=("L1", "L1b", "L2", "L3", "L4", "L5"), quiet=True))
    res = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in out.glob("imp_*.json")}
    assert res["imp_clipped"]["verdict"] == "BLOCK"
    assert res["imp_clipped"]["L3"]["available"] is False          # blocked files never reach a model
    for n in ("imp_punchy", "imp_weak", "imp_muddy"):
        r = res[n]
        assert r["verdict"] == "PASS"                               # learned layers never block
        assert r["L3"]["available"] and 1 <= r["L3"]["scores"]["PQ"] <= 10
        assert len(r["L4"]["clap"]["top3"]) == 3 and len(r["L4"]["ast"]["top5"]) == 5
        assert r["L5"]["available"] is False                        # no approved refs yet
    assert res["imp_weak"]["L3"]["input"] == "repetition"           # < 300 ms -> 3-4 s repetition
    steps = {(x["step"], x["model"]) for x in res["imp_punchy"]["ai_steps"]}
    assert ("critic:audiobox", learned.pinned_id(learned.AES_REPO)) in steps
    assert ("critic:ast", learned.pinned_id(learned.AST_MODEL)) in steps
    assert {m for st, m in steps if st == "critic:clap"} == {learned.pinned_id(m) for m in learned.CLAP_MODELS}
    assert res["imp_clipped"]["ai_steps"] == []
    assert res["imp_punchy"]["score"]["rank"] == 1
    assert res["imp_punchy"]["score"]["weights_used"]["L3"] > 0
    log = batch["models"]["log"]
    assert log["aes"]["device"] in ("mps", "cpu", "cpu (fallback)")


def test_clap_is_repeatable_on_files_longer_than_ten_seconds(tmp_path):
    """The extractor's rand_trunc crop made a 15 s file score differently run to run (review finding)."""
    import numpy as np
    sr = 48000
    t = np.arange(15 * sr) / sr
    x = 0.2 * np.sin(2 * np.pi * 220 * t) * (1 + 0.5 * np.sin(2 * np.pi * 0.3 * t))
    x += 0.05 * np.random.default_rng(3).standard_normal(len(t))
    synth.write(tmp_path / "in" / "amb.long.wav", synth.fade_out(x, 100))
    got = []
    for k in range(2):
        out = tmp_path / f"out{k}"
        pipeline.run([str(tmp_path / "in")], out_dir=out,
                     opts=pipeline.Options(layers=("L1", "L4", "L5"), group="ambience", stage="raw", quiet=True))
        r = json.loads((out / "amb.long.json").read_text(encoding="utf-8"))
        got.append((r["L4"]["clap"]["top3"], r["L4"]["clap"]["pam_clean"], r["L4"]["clap"]["contrast"]))
    assert got[0] == got[1]
