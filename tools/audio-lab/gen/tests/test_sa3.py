"""gen/sa3.py: jobs from spec cards, allowed lengths, records and licence rows (no model run)."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest
import soundfile as sf

from build import ledger
from gen import sa3

SR = 44100


def card(tmp: Path, **over) -> dict:
    c = {"id": "hit.test", "game": "typing-survival", "duration": {"target_ms": 80, "min_ms": 64, "max_ms": 96},
         "prompt": {"text": "a short steel clank", "variants": ["A: steel clank one", "B: steel clank two"]}}
    c.update(over)
    c["_path"] = str(tmp / "hit.test.yaml")
    return c


def install() -> dict:
    return {"hf": {"repo": "stabilityai/stable-audio-3-optimized", "revision": "f" * 40},
            "repo": {"url": "https://github.com/Stability-AI/stable-audio-3", "commit": "e" * 40},
            "venv": {"key_versions": {"mlx": "0.32.4"}},
            "weights": [{"file": "MLX/dit_sm-sfx_f16.npz", "sha256": "1" * 64},
                        {"file": "MLX/same_s_decoder_f32.npz", "sha256": "2" * 64},
                        {"file": "MLX/t5gemma_f16.npz", "sha256": "3" * 64}]}


def licences(tmp: Path) -> Path:
    d = tmp / "licences"
    d.mkdir()
    (d / "stability-registration.txt").write_text("registration (test)\n")
    (d / "stability-community-license-2026-10-23.txt").write_text("licence (test)\n")
    (d / "gemma-terms-of-use-2026-10-23.txt").write_text("gemma terms (test)\n")
    return d


def test_seconds_are_picked_from_the_allowed_set_only(tmp_path):
    assert sa3.pick_seconds(card(tmp_path)) == 1.0
    assert sa3.pick_seconds(card(tmp_path, duration={"max_ms": 1320})) == 2.0
    assert sa3.pick_seconds(card(tmp_path, duration={"max_ms": 7200})) == 10.0
    assert sa3.pick_seconds(card(tmp_path), 3) == 3.0
    for bad in (0.5, 1.5, 6.0):        # 0.5 s and 1.5 s give full-scale noise in this build
        with pytest.raises(sa3.Sa3Error):
            sa3.pick_seconds(card(tmp_path), bad)


def test_prompts_from_card_keep_their_letters(tmp_path):
    c = card(tmp_path, prompt={"text": "x", "variants": ["E: wind in pines", "plain prompt"]})
    assert sa3.prompts_from_card(c) == {"E": "wind in pines", "B": "plain prompt"}
    assert sa3.prompts_from_card(card(tmp_path, prompt={"text": "only text", "variants": []})) == {"A": "only text"}
    with pytest.raises(sa3.Sa3Error):
        sa3.prompts_from_card(card(tmp_path, prompt={"text": None, "variants": ["A: x", "A: y"]}))


def test_job_has_float_copies_and_keeps_the_negative_prompt_written_only(tmp_path):
    job = sa3.build_job(card(tmp_path), seeds=[7, 8], negative="music, voice")
    assert job["raw_float"] is True and job["cfg"] == 1.0 and job["negative_prompt"] is None
    assert job["_meta"]["negative_written_not_applied"] == "music, voice"
    assert [it["name"] for it in job["items"]] == ["hit.test__A__s7", "hit.test__A__s8", "hit.test__B__s7", "hit.test__B__s8"]
    tagged = sa3.build_job(card(tmp_path), variants=["B"], seeds=[1], seconds=3, tag_seconds=True)
    assert tagged["items"][0]["name"] == "hit.test__B3s__s1" and tagged["items"][0]["seconds"] == 3.0
    cfg3 = sa3.build_job(card(tmp_path), seeds=[1], cfg=3.0, negative="music")
    assert cfg3["negative_prompt"] == "music"
    with pytest.raises(sa3.Sa3Error):
        sa3.build_job(card(tmp_path), variants=["Z"], seeds=[1])


def test_forbidden_prompts_of_loi_goi_are_refused(tmp_path):
    """DECISIONS Q2: call-chop B, D and the 'tốc' words are refused for typing-defense; other games are free."""
    chop = card(tmp_path, id="call-chop", game="typing-defense",
                prompt={"variants": ["A: one low knock of an axe handle on bamboo", "B: a hollow knock",
                                     "D: hollow bamboo tube, low resonant tok", "E: deep solid knock on bamboo"]})
    assert [it["name"] for it in sa3.build_job(chop, variants=["A", "E"], seeds=[1])["items"]] == \
        ["call-chop__A__s1", "call-chop__E__s1"]
    for keys in (["B"], ["D"], None):          # None: every prompt of the card, B and D among them
        with pytest.raises(sa3.Sa3Error):
            sa3.build_job(chop, variants=keys, seeds=[1])
    other = card(tmp_path, id="ui-move", game="typing-defense", prompt={"variants": ["A: a temple block tap"]})
    with pytest.raises(sa3.Sa3Error):
        sa3.build_job(other, seeds=[1])
    for text in ("small wooden fish knock", "a mõ hit", "one TOK on wood", "tiếng tốc"):
        with pytest.raises(sa3.Sa3Error):
            sa3.check_prompts({"id": "x", "game": "typing-defense"}, {"A": text})
    sa3.check_prompts({"id": "x", "game": "typing-defense"}, {"A": "a stoked fire, token, hollow woody thud"})
    sa3.check_prompts({"id": "x", "game": "dragon-hold"}, {"A": "a temple block tap"})


def test_licence_rows_are_valid_and_name_the_model_revision(tmp_path):
    rows, copies = sa3.licence_rows(install(), licences=licences(tmp_path), date="2026-10-23")
    keys = {r["key"] for r in rows}
    assert f"model:stabilityai/stable-audio-3-optimized@{'f' * 40}" in keys
    assert "acceptance:LicenseRef-Stability-Community-2024@2024-07-05" in keys
    for r in rows:
        assert not ledger.schema_errors("licences", r)
        assert Path(copies[r["key"]]).is_file()
    model = next(r for r in rows if r["kind"] == "model")
    assert model["role"] == "generate" and model["commercial_ok"] is True and model["sha256"] == "1" * 64


def fake_runner(job_path: Path, out: Path) -> int:
    """Stands in for batch_run.sh: writes 16-bit + float copies and the driver's report."""
    job = json.loads(job_path.read_text())
    items = []
    for k, it in enumerate(job["items"]):
        n = int(it["seconds"] * SR)
        t = np.arange(n) / SR
        x = 1.3 * np.sin(2 * np.pi * 300 * t) * np.exp(-t / 0.05)       # over full scale: the writer clips
        st = np.stack([x, x], axis=1)
        sf.write(str(out / f"{it['name']}.wav"), np.clip(st, -1, 1), SR, subtype="PCM_16")
        sf.write(str(out / f"{it['name']}.f32.wav"), st, SR, subtype="FLOAT")
        items.append({"name": it["name"], "prompt": it["prompt"], "seed": it["seed"], "seconds": it["seconds"],
                      "sample_s": 0.5, "decode_s": 0.05, "total_s": 0.6, "peak_abs": 1.3, "path": str(out / f"{it['name']}.wav")})
    (out / "report.json").write_text(json.dumps({"dit": job["dit"], "decoder": "same-s", "steps": job["steps"],
                                                 "cfg": job["cfg"], "negative_prompt": job["negative_prompt"],
                                                 "items": items, "loop_s": 1.2, "warm_mean_s": 0.6}))
    (out / "run.log").write_text("ok\n")
    return 0


def test_run_job_writes_records_rows_and_skips_existing(tmp_path):
    lic = licences(tmp_path)
    job = sa3.build_job(card(tmp_path), seeds=[1], negative="music")
    run_dir = tmp_path / "work" / "hit.test" / "r2"
    res = sa3.run_job(job, run_dir, install=install(), runner=fake_runner, date="2026-10-23", licences=lic)
    assert res["todo"] == 2 and len(res["records"]) == 2
    rec = sa3.read_record(res["records"][0])
    assert rec["schema"] == sa3.RECORD_SCHEMA and rec["variant"] == "A" and rec["seed"] == 1 and rec["cfg"] == 1.0
    assert rec["model"]["id"] == f"stabilityai/stable-audio-3-optimized@{'f' * 40}"
    assert rec["files"]["f32"]["sha256"] == ledger.sha256_file(Path(rec["files"]["f32"]["path"]))
    assert rec["raw_stats"]["writer_clip_16bit"]["runs_ge3_at_0999"] >= 1 and rec["raw_stats"]["peak_abs_float"] > 1.0
    assert rec["raw_stats"]["dual_mono"] is True
    assert rec["negative_prompt_written_not_applied"] == "music"
    rows = ledger.read_rows(run_dir / "licences.rows.jsonl")
    assert {r["kind"] for r in rows} == {"model", "acceptance"}
    again = sa3.run_job(job, run_dir, install=install(), runner=fake_runner, date="2026-10-23", licences=lic)
    assert again["todo"] == 0 and again["skipped"] == 2
    assert len(ledger.read_rows(run_dir / "licences.rows.jsonl")) == len(rows)      # append-only, no duplicates
