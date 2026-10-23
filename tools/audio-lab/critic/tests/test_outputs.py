import json

import jsonschema
import numpy as np

from critic import pipeline
from critic.__main__ import main
from critic.schema import FILE_SCHEMA
from critic.tests import synth
from critic.thresholds import SCHEMA_BATCH, SCHEMA_FILE


def test_every_file_json_matches_the_schema(synth_run):
    for name, r in synth_run["res"].items():
        assert r["schema"] == SCHEMA_FILE
        jsonschema.validate(r, FILE_SCHEMA)


def test_batch_and_summary(synth_run):
    out = synth_run["out"]
    b = json.loads((out / "_batch.json").read_text(encoding="utf-8"))
    assert b["schema"] == SCHEMA_BATCH
    assert b["counts"]["BLOCK"] == len(synth.BROKEN) and b["counts"]["PASS"] == len(synth.CLEAN)
    md = (out / "summary.md").read_text(encoding="utf-8")
    assert md.startswith("# Tai AI: kết quả chấm")
    assert "## Bị chặn ở L1" in md and "imp_clipped.wav" in md
    assert "Danh sách nghe đề xuất" in md


def test_card_png_is_drawn(tmp_path):
    d = tmp_path / "in"
    synth.write(d / "imp_punchy.wav", synth.punchy())
    synth.write(d / "loop_broken.wav", synth.loop(False))
    (tmp_path / "cards.yaml").write_text(synth.CARDS, encoding="utf-8")
    out = tmp_path / "out"
    pipeline.run([str(d)], spec_path=str(tmp_path / "cards.yaml"), out_dir=out,
                 opts=pipeline.Options(layers=("L1", "L2", "L6"), quiet=True))
    import matplotlib.image as mpimg
    for stem in ("imp_punchy", "loop_broken"):
        png = out / f"{stem}.png"
        assert png.is_file() and png.stat().st_size > 50_000
        h, w = mpimg.imread(str(png)).shape[:2]
        assert w >= 1200 and h >= 800
        assert json.loads((out / f"{stem}.json").read_text(encoding="utf-8"))["card"] == png.name


def test_cli_run_groups_schema(tmp_path, capsys):
    d = tmp_path / "in"
    synth.write(d / "hit.t1-1.wav", synth.punchy(0.12))
    synth.write(d / "hit.t1-2.wav", synth.weak_click())
    out = tmp_path / "out"
    assert main(["run", str(d), "--layers", "L1,L2", "--out", str(out), "--quiet"]) == 0
    r = json.loads((out / "hit.t1-1.json").read_text(encoding="utf-8"))
    assert r["spec"]["group"] == "hit_small" and r["spec"]["group_source"] == "id"
    assert r["score"]["rank_group"] == "id:hit.t1"
    assert main(["run", str(d), "--layers", "L1,L2", "--out", str(out), "--quiet", "--group", "nope"]) == 2
    assert main(["groups"]) == 0
    assert "hit_heavy" in capsys.readouterr().out
    assert main(["schema"]) == 0
    assert json.loads(capsys.readouterr().out)["$id"] == SCHEMA_FILE


def test_fail_on_block_exit_code(tmp_path):
    d = tmp_path / "in"
    synth.write(d / "x.wav", synth.clipped(), subtype="PCM_16")
    assert main(["run", str(d), "--layers", "L1", "--out", str(tmp_path / "o"), "--quiet", "--fail-on-block"]) == 1


def test_output_refuses_games_folder(tmp_path):
    from common import env
    import pytest
    d = tmp_path / "in"
    synth.write(d / "x.wav", synth.punchy())
    with pytest.raises(SystemExit):
        pipeline.run([str(d)], out_dir=env.GAMES / "dragon-hold" / "_critic_should_not_exist",
                     opts=pipeline.Options(layers=("L1",), quiet=True))
    assert not (env.GAMES / "dragon-hold" / "_critic_should_not_exist").exists()


def test_pairs_port(tmp_path, capsys):
    d = tmp_path / "in"
    x = synth.punchy()
    synth.write(d / "p.wav", x)
    synth.write(d / "p__clipped.wav", np.clip(x * 8, -1, 1), subtype="PCM_16")
    synth.write(d / "p__thin.wav", synth.norm_peak(synth._band(x, 1500, None), -17))
    out = tmp_path / "out"
    pipeline.run([str(d)], out_dir=out, opts=pipeline.Options(layers=("L1", "L2"), group="hit_heavy", quiet=True))
    assert main(["pairs", str(out)]) == 0
    md = capsys.readouterr().out
    assert "| L1 rồi L2 (bộ chấm) | 1/1 | 0/0 | 1/1 | **2/2** |" in md


def test_blind_card_for_the_board(tmp_path):
    """--blind-cards writes <stem>.blind.png and records it; the board prefers it (§7: no score shown)."""
    import json

    from critic.pipeline import Options, run
    from critic.tests.synth import punchy, write

    f = write(tmp_path / "hit.wav", punchy())
    out = tmp_path / "out"
    run([str(f)], out_dir=str(out), opts=Options(layers=("L1", "L2", "L6"), blind_cards=True, quiet=True))
    doc = json.loads((out / "hit.json").read_text())
    assert doc["card"] == "hit.png" and doc["card_blind"] == "hit.blind.png"
    assert (out / "hit.blind.png").stat().st_size > 10000
