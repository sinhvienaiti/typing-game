"""Batch 1, Lời Gọi (typing-defense): step P5 of BATCH1_BRIEF.md (§4.3, §4.4, §6, §7).

  run.sh common.batch1_td all [--run b1] [--force]
  run.sh common.batch1_td generate|process|recipes|critic|link|context|session|report [--run b1]

generate  Stable Audio 3 from the spec cards (prompt.variants), one job at a time, model resident per job:
          wordshot-fire A-D, arrow-fire A-D, ink-puff A-D, blast A-D (A, B paper layers for the recipe, C, D whole
          takes), call-chop A, E, F, G at new seeds (B, D are forbidden: DECISIONS Q2; gen/sa3.py refuses them).
process   gen/process.py on every raw take (true onsets, exponential tail, mono); call-chop also re-processes its
          batch 0b takes of the allowed prompts (A s1001-1006, E-G s2001-2006).
recipes   build/recipes/typing-defense/<rid>.b1.json, rendered with build.render: word-hit (three directions of the
          7-note scale A3 C4 D4 F4 G4 A4 C5), word-hit-bell (Hand Chimes C7, A6; Tubular Bells C5), wordshot-fire
          (Stable Audio 3 whoosh + Kenney bookFlip), blast (frame drum or timpani + Stable Audio 3 paper burst),
          coin (Kenney handleCoins + Hand Chimes: ring above 4 kHz, or short in 1-4 kHz), leak (Anvil kẻng: 0a
          pattern, tighter pattern, with a frame drum), ui-move (VCSL Slit Drum), ui-pick (clapper + Hand Chimes A5).
critic    one full critic run over every final and the rated 0a/0b references (one model load, calibration owner-v1),
          an L1 run on every raw file.
link      critic AI steps into SOURCES.json, a batch-local release tree of the recipes, licence-check on it, and a
          count of the licence rows behind every listened file.
context   context/td_scenes.py: td-wordhit-chain (the S5 ids), td-night (leak, call-chop), td-menu (ui-move, ui-pick),
          one render per listened candidate, with metrics; they become the board context "Trong trận thô".
session   board sessions "1-td-s5" and "1-td-s6" in ~/AudioLab/review/typing-defense/sessions (never overwritten
          without --force), cards revealed at the end, 4 anchors.
report    ~/AudioLab/work/_batch1/typing-defense/<run>/REPORT.md and summary.json.

Heavy models run one at a time: the generate step and the critic step each wait while another Stable Audio 3 or
critic process runs on the machine. Nothing is written under games/**.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
import time
from pathlib import Path

import numpy as np

from common import env
from common.batch1_dh import (_distinct, _docs, _flags, _fmt, _pct, _rank, _sid, _upper, _verified, gen_src,
                              wait_heavy_free)

LAB = env.LAB
GAME = "typing-defense"
SEED = 20261024

# id -> SA3 jobs (variants of the card, seeds); every length is the card's (1 s)
JOBS: dict[str, list[dict]] = {
    "wordshot-fire": [{"variants": ["A", "B", "C", "D"], "seeds": "2001-2006"}],
    "arrow-fire": [{"variants": ["A", "B", "C", "D"], "seeds": "2001-2006"}],
    "ink-puff": [{"variants": ["A", "B", "C", "D"], "seeds": "2001-2006"}],
    "blast": [{"variants": ["A", "B", "C", "D"], "seeds": "2001-2006"}],
    "call-chop": [{"variants": ["A", "E", "F", "G"], "seeds": "3001-3006"}],
}
SCALE = ("A3", "C4", "D4", "F4", "G4", "A4", "C5")      # word-hit one octave down (BATCH1_BRIEF #21, 16 #4)
S5 = ["word-hit", "word-hit-bell", "wordshot-fire", "arrow-fire", "ink-puff", "blast", "coin"]
S6 = ["leak", "call-chop", "ui-move", "ui-pick"]
IDS = S5 + S6
# earlier raw takes processed again with this batch's chain (only the prompts batch 1 keeps: DECISIONS Q2)
OLD_RAW = {"call-chop": ["sa3-trial", "sa3-r2"]}
OLD_RAW_FILTER = {"call-chop": ("__A__", "__E__", "__F__", "__G__")}


def _say(msg: str) -> None:
    print(f"[batch1-td] {msg}", flush=True)


def base_dir(run: str) -> Path:
    p = env.WORK / "_batch1" / GAME / run
    p.mkdir(parents=True, exist_ok=True)
    return p


def id_dir(sid: str, run: str) -> Path:
    return env.WORK / GAME / sid / run


def card_path(sid: str) -> Path:
    return LAB / "specs" / GAME / f"{sid}.yaml"


def raw_dirs(sid: str, run: str) -> list[Path]:
    out = [env.WORK / GAME / sid / r / "raw" for r in OLD_RAW.get(sid, [])] + [id_dir(sid, run) / "raw"]
    return [p for p in out if p.is_dir()]


# ---------------------------------------------------------------- step 1: generate

def step_generate(run: str, force: bool = False) -> None:
    from gen import sa3

    for sid, jobs in JOBS.items():
        card = sa3.read_card(card_path(sid))
        for j in jobs:
            job = sa3.build_job(card, variants=j["variants"], seeds=sa3.parse_seeds(j["seeds"]),
                                seconds=j.get("seconds"), tag_seconds=bool(j.get("tag")))
            wait_heavy_free(f"sa3 {sid}")
            t0 = time.time()
            res = sa3.run_job(job, id_dir(sid, run))
            _say(f"sa3 {sid} {','.join(j['variants'])} {job['_meta']['seconds']:g} s: {res['todo']} mới, "
                 f"{res['skipped']} đã có, {time.time() - t0:.0f} s"
                 + (f", RAM mô hình {res['mlx_peak_gb']} GB" if res.get("mlx_peak_gb") else ""))


# ---------------------------------------------------------------- step 2: process

def records(sid: str, run: str) -> list[Path]:
    from gen import process

    out = []
    for d in raw_dirs(sid, run):
        keep = OLD_RAW_FILTER.get(sid) if d.parent.name != run else None
        out += [r for r in process.collect_records([str(d)]) if not keep or any(k in r.name for k in keep)]
    return out


def step_process(run: str, force: bool = False) -> None:
    from gen import process, sa3

    for sid in JOBS:
        card = sa3.read_card(card_path(sid))
        res = process.process_many(records(sid, run), card, id_dir(sid, run) / "processed", force=force)
        _say(f"process {sid}: {res['kept']} giữ, {len(res['rejected'])} loại, {res['skipped']} đã có")
        for r in res["rejected"]:
            _say(f"  loại {r['candidate']}: {r['reason']}")


# ---------------------------------------------------------------- step 3: Stable Audio 3 layers for the recipes

# id -> prompts whose processed takes feed a recipe layer
LAYER_POOLS = {"wordshot-fire": ("A", "B", "C", "D"), "blast": ("A", "B")}
# a paper burst flutters (several small onsets by nature); a whoosh with two onsets would sound like two shots
LAYER_NO_FLAGS = {"wordshot-fire": {"double_onset", "lr_imbalance"}, "blast": {"lr_imbalance"}}


def critic_out(run: str, name: str) -> Path:
    return base_dir(run) / f"critic-{name}"


def step_layers(run: str, force: bool = False) -> dict:
    """Rank the processed takes that feed recipe layers with the fast layers (L1, L1b, L2; no model)."""
    from critic.__main__ import main as critic

    out_json = base_dir(run) / "layers.json"
    if out_json.is_file() and not force:
        return json.loads(out_json.read_text("utf-8"))
    pools = {}
    for sid, prompts in LAYER_POOLS.items():
        proc = id_dir(sid, run) / "processed"
        out = critic_out(run, f"layers-{sid}")
        if not (out / "_batch.json").is_file() or force:
            critic(["run", str(proc), "--spec", str(card_path(sid)), "--stage", "final", "--layers", "L1,L1b,L2",
                    "--out", str(out), "--seed", str(SEED), "--sources", str(proc / "SOURCES.json"), "--quiet"])
        docs = _docs(out)
        rows = []
        for d in docs.values():
            stem = d["file"]["stem"]
            parts = stem.split("__")
            if len(parts) < 3 or parts[1][:1] not in prompts:
                continue
            pj = json.loads(Path(d["file"]["path"]).with_suffix(".proc.json").read_text("utf-8"))
            if pj.get("onset_verified", True) is False or LAYER_NO_FLAGS[sid] & _flags(d):
                continue
            # a layer is not the whole sound: the card's length, rise (a whoosh swells; the paper or drum layer
            # carries the front) and DC (the recipe's high-pass) do not apply; clips and the rest still refuse it
            if d["verdict"] != "PASS" and set(d["L1"]["blocking"]) - {"duration", "attack", "dc_offset"}:
                continue
            rows.append({"stem": stem, "prompt": parts[1][:1], "l2": (d.get("L2") or {}).get("score") or 0.0,
                         "file": pj["source_f32"], "record": pj["raw_record"], "window": pj["window_raw_s"],
                         "len_ms": pj["window"]["len_ms"]})
        rows.sort(key=lambda r: -r["l2"])
        # one per prompt first (A, B, C, D), then the rest by L2
        firsts, seen = [], set()
        for r in rows:
            if r["prompt"] not in seen:
                firsts.append(r)
                seen.add(r["prompt"])
        pools[sid] = firsts + [r for r in rows if r not in firsts]
        _say(f"layers {sid}: {len(rows)} bản dùng được làm lớp; đầu: {', '.join(r['stem'] for r in pools[sid][:4])}")
    out_json.write_text(json.dumps(pools, indent=1, ensure_ascii=False), "utf-8")
    return pools


# ---------------------------------------------------------------- step 4: recipes

def recipe_path(rid: str) -> Path:
    return LAB / "build" / "recipes" / GAME / f"{rid}.b1.json"


def recipe_run(rid: str, run: str) -> Path:
    sid = rid.split(".")[0]
    return env.WORK / GAME / sid / f"{run}-recipe-{rid}"


def _cycle(layer: dict, sources: list[dict]) -> dict:
    layer["source"] = sources[0]
    if len(sources) > 1:
        layer.setdefault("vary", {}).update({"swapMode": "cycle", "swap": sources[1:]})
    return layer


def _smp(instrument: str, notes) -> dict:
    return {"sampler": {"instrument": instrument, "notes": notes}}


def _lib(path: str) -> dict:
    return {"library": path}


def _recipe(rid: str, group: str, family: str, desc: str, layers: list[dict], chain: dict, count: int, seed: int,
            export: str, pitch=(0, 0), gain=(0, 0)) -> dict:
    return {"$schema": "../../schemas/recipe.schema.json", "schema": "audiolab.recipe/1", "game": GAME, "id": rid,
            "group": group, "family": family, "description": desc, "channels": 1, "layers": layers, "chain": chain,
            "variants": {"count": count, "seed": seed, "includeBase": True, "pitchCents": list(pitch), "gainDb": list(gain)},
            "export": {"path": export, "ogg": True, "oggQuality": 0.6}}


LIMIT = {"ceilingDbtp": -1.0, "releaseMs": 60, "maxGrDb": 6}
NORM = {"mode": "lufs-m-max", "target": -20}


# The strong VCSL layer (velocity >= 100) of the A3 note (G#3 shifted up a semitone) is sharp: the critic's pYIN read
# 223.7 Hz (+29 cents) on the first render, against <= 10 cents in the brief (#21); the sampler's tuning table has no
# correction for that layer. The other notes read within one pYIN bin (10 cents).
CENTS_FIX = {100: {"A3": -25.0}}


def _scale(vel: int, dur: float = 0.8) -> list[dict]:
    fix = CENTS_FIX.get(vel, {})
    return [_smp("dan-tranh.normal", [{"start": 0, "note": n, "dur": dur, "vel": vel, "cents": fix[n]}]) if n in fix
            else _smp("dan-tranh.normal", f"0:{n}:{dur}:{vel}") for n in SCALE]


def recipes_from(pools: dict) -> dict[str, dict]:
    out: dict[str, dict] = {}
    # ---- word-hit: three directions of the 7-note scale (variant n = note n of A3 C4 D4 F4 G4 A4 C5)
    wh_chain = {"dcHpfHz": 40, "filters": [{"type": "peak", "hz": 2500, "gainDb": -3, "q": 0.7}],
                "headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": 900,
                "tail": {"floorDb": -60, "fadeMs": 200}, "normalise": NORM, "limiter": LIMIT}
    out["word-hit.d1"] = _recipe(
        "word-hit.d1", "word-reward", "thuong",
        "Lô 1 (BATCH1_BRIEF #21), hướng 1 = công thức 0a mà anh chấm 3/5 ở C4 (e79e84d1): tiếng gảy đàn tranh VCSL "
        "Normal đủ dải giữ 120 ms, phần ngân cùng nốt lọc thấp 1 kHz bậc 4 nhỏ hơn 4 dB, khoét nhẹ 2,5 kHz (mục 6.2). "
        "Cả thang hạ một quãng tám: A3 (từ ẩu), C4, D4, F4, G4, A4, C5. Không lối rung (0a: 2/5). Biến thể n là nốt n.",
        [_cycle({"id": "pluck", "role": "attack", "trim": {"endMs": 120}, "fadeOutMs": 90}, _scale(100)),
         _cycle({"id": "ring", "role": "tail", "gainDb": -4, "fadeOutMs": 250,
                 "filters": [{"type": "lowpass", "hz": 1000, "order": 4}]}, _scale(100))],
        wh_chain, 7, 2101, "sfx/reward/word-hit")
    out["word-hit.d2"] = _recipe(
        "word-hit.d2", "word-reward", "thuong",
        "Lô 1, hướng 2 'gảy mềm, ấm': lớp cường độ nhẹ của VCSL (velocity 75, tiếng gảy tròn hơn, ít tiếng móng), "
        "tiếng gảy giữ 140 ms, phần ngân dưới 1 kHz to hơn hướng 1 (−2 dB) và dài hơn. Cùng thang A3–C5.",
        [_cycle({"id": "pluck", "role": "attack", "trim": {"endMs": 140}, "fadeOutMs": 100}, _scale(75)),
         _cycle({"id": "ring", "role": "tail", "gainDb": -2, "fadeOutMs": 300,
                 "filters": [{"type": "lowpass", "hz": 1000, "order": 4}]}, _scale(75))],
        {**wh_chain, "filters": [{"type": "peak", "hz": 2500, "gainDb": -2, "q": 0.7}]}, 7, 2102, "sfx/reward/word-hit")
    out["word-hit.d3"] = _recipe(
        "word-hit.d3", "word-reward", "thuong",
        "Lô 1, hướng 3 'sáng, ánh dây thép': hướng 1 cộng một lớp ngân trên 4,5 kHz (lọc cao bậc 4, −8 dB), phần mục 6.2 "
        "cho phép ngân (dưới 1 kHz hoặc trên 4 kHz), để giữ ánh kim của dây đàn mà không ngân ở dải giọng đọc.",
        [_cycle({"id": "pluck", "role": "attack", "trim": {"endMs": 120}, "fadeOutMs": 90}, _scale(100)),
         _cycle({"id": "ring", "role": "tail", "gainDb": -4, "fadeOutMs": 250,
                 "filters": [{"type": "lowpass", "hz": 1000, "order": 4}]}, _scale(100)),
         _cycle({"id": "air", "role": "sweetener", "gainDb": -8, "fadeOutMs": 300,
                 "filters": [{"type": "highpass", "hz": 4500, "order": 4}]}, _scale(100))],
        wh_chain, 7, 2103, "sfx/reward/word-hit")
    # ---- word-hit-bell: Hand Chimes C7, A6; Tubular Bells C5 (VSCO-2-CE), split like word-hit (§6.2)
    bells = [_smp("hand-chimes", "0:C7:0.6:90"), _smp("hand-chimes", "0:A6:0.6:90"),
             _lib("vsco2ce/Percussion/TB_hit_C5_v4_rr1.wav")]
    out["word-hit-bell"] = _recipe(
        "word-hit-bell", "rare-fixed", "thuong",
        "Lô 1 (BATCH1_BRIEF #22): chuông thêm khi Hoàn hảo, Chớp; 0,5 s; cố định. Ba ứng viên: 1) VCSL Hand Chimes C7 "
        "(2.093 Hz, đúng nốt mã đang dùng), 2) Hand Chimes A6, 3) VSCO-2-CE Tubular Bells C5 (chưa nghe; không đo được cao "
        "độ tin cậy). Nốt nào cũng gần dải giọng nên tách lớp như word-hit: tiếng 'ting' đủ dải chỉ giữ 100 ms, phần ngân "
        "dài chỉ còn trên 4 kHz (lọc cao bậc 4) và dưới 1 kHz (lọc thấp bậc 4; với chuông nhỏ gần như không còn gì). "
        "Không Hand Bells Nepalese.",
        [_cycle({"id": "ting", "role": "attack", "trim": {"endMs": 100}, "fadeOutMs": 60}, bells),
         _cycle({"id": "ring-high", "role": "tail", "gainDb": -6, "fadeOutMs": 250,
                 "filters": [{"type": "highpass", "hz": 4000, "order": 4}]}, bells),
         _cycle({"id": "ring-low", "role": "tail", "gainDb": -6, "fadeOutMs": 250,
                 "filters": [{"type": "lowpass", "hz": 1000, "order": 4}]}, bells)],
        {"dcHpfHz": 60, "headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": 560,
         "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 300}, "normalise": NORM, "limiter": LIMIT},
        3, 2201, "sfx/reward/word-hit-bell")
    # ---- wordshot-fire: Stable Audio 3 whoosh + Kenney RPG bookFlip (paper)
    W = pools.get("wordshot-fire", [])[:4]
    if W:
        papers = [_lib("kenney/rpg-audio/Audio/bookFlip3.ogg"), _lib("kenney/rpg-audio/Audio/bookFlip2.ogg")] * 2
        out["wordshot-fire.mix"] = _recipe(
            "wordshot-fire.mix", "shot", "ban",
            "Lô 1 (BATCH1_BRIEF #23): Phát Chữ bay ra. Tiếng vút Stable Audio 3 (bốn bản đứng đầu L2, mỗi prompt một bản; "
            "cửa sổ đầu tiếng thật của chuỗi xử lý) cộng tiếng lật giấy Kenney RPG bookFlip3/bookFlip2 (cắt từ 25 ms, "
            "lọc cao 1,5 kHz, −9 dB, vào sau 8 ms), lọc cao 120 Hz (mục 4.3.3 'khạc, phóng': dưới 120 Hz thấp hơn ít "
            "nhất 12 dB). Biến thể n dùng tiếng vút n.",
            [_cycle({"id": "whoosh", "role": "body", "fadeOutMs": 40}, [gen_src(b) for b in W]),
             _cycle({"id": "paper", "role": "sweetener", "gainDb": -9, "offsetMs": 8, "trim": {"startMs": 25, "endMs": 190},
                     "fadeOutMs": 60, "filters": [{"type": "highpass", "hz": 1500}]}, papers[:len(W)])],
            {"dcHpfHz": 120, "headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": 210,
             "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 90}, "normalise": NORM, "limiter": LIMIT},
            len(W), 2301, "sfx/battle/wordshot-fire")
    # ---- blast: a dry plank crack + frame drum or timpani + Stable Audio 3 paper burst
    P = pools.get("blast", [])[:4]
    if len(P) == 4:             # vòng 3: the muted drum left A s2004's own flutter as a second onset at 31 ms (+2.4 dB)
        P = [P[0], P[1], P[3]]
    if P:
        drums = [_smp("frame-drum", "0:hdruml-hit:0.6:118"), {"sampler": {"instrument": "timpani", "notes": "0:timpani2-hit:0.8:105"}},
                 _smp("frame-drum", "0:hdruml-hitmuted:0.5:120")]
        fronts = [_lib(f"kenney/impact-sounds/Audio/impactPlank_medium_00{k}.ogg") for k in (4, 2, 0)]
        n = len(P)
        out["blast.mix"] = _recipe(
            "blast.mix", "blast", "no",
            "Lô 1 (BATCH1_BRIEF #26): Tháp Pháo, cụm Phát Chữ. Vòng 2 sau thẻ ảnh: vòng 1 (nứt tổng hợp 3 ms, rồi lớp giấy "
            "lên chậm) bị chặn ở thời gian lên 14 ms và có hai đầu tiếng 23–25 ms, 72 % dưới 150 Hz, sub dài 315 ms. Nay tiếng "
            "nứt là ván gỗ Kenney impactPlank (lọc cao 900 Hz, 60 ms), to nhất ở đầu; trống khung VCSL (đánh mở, rồi đánh chặn) "
            "hoặc timpani VSCO-2-CE nhỏ hơn 4 dB, lọc cao 70 Hz, cắt ở 320 ms; lớp giấy, bụi Stable Audio 3 (prompt A, B) vào "
            "sau 12 ms, mờ vào 25 ms, −7 dB, lọc cao 400 Hz. Không lách tách, không chất taiko. Biến thể n dùng nứt n, trống n, giấy n.",
            [_cycle({"id": "crack", "role": "attack", "trim": {"endMs": 60}, "fadeOutMs": 30,
                     "filters": [{"type": "highpass", "hz": 900}]}, fronts[:n]),
             _cycle({"id": "drum", "role": "body", "gainDb": -4, "trim": {"endMs": 320}, "fadeOutMs": 180,
                     "filters": [{"type": "highpass", "hz": 70, "order": 2}]}, drums[:n]),
             _cycle({"id": "paper", "role": "texture", "gainDb": -7, "offsetMs": 12, "fadeInMs": 25, "fadeOutMs": 120,
                     "filters": [{"type": "highpass", "hz": 400}]}, [gen_src(b) for b in P])],
            {"dcHpfHz": 40, "headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": 460,
             "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 200}, "normalise": NORM,
             "limiter": {"ceilingDbtp": -1.0, "releaseMs": 80, "maxGrDb": 6}},
            n, 2401, "sfx/battle/blast")
    # ---- coin: one Kenney coin clink + Hand Chimes; two directions (BATCH1_BRIEF #27 acceptance)
    chimes = [_smp("hand-chimes", f"0:{n}:0.5:85") for n in ("C7", "A6", "G6", "D7")]
    coin_chain = {"dcHpfHz": 40, "filters": [{"type": "highpass", "hz": 150}], "headTrim": {"thresholdDb": -50, "preRollMs": 0.5},
                  "maxLengthMs": 340, "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 180}, "normalise": NORM, "limiter": LIMIT}
    # vòng 1: the whole handful (handleCoins2: clinks 18-40 ms apart -> double_onset; handleCoins cut at 50 ms put the
    # loud clink at 110 ms -> attack 100 ms) and a C7/A6 line left at -65 dB to the last sample by a 4th-order 4 kHz HPF
    out["coin.ring"] = _recipe(
        "coin.ring", "default", "thuong",
        "Lô 1 (BATCH1_BRIEF #27), hướng 'ngân trên 4 kHz': một tiếng xu chạm của Kenney RPG handleCoins (cắt đúng một tiếng "
        "chạm 150–238 ms, lọc cao 400 Hz), cộng chuông VCSL Hand Chimes nốt ngũ cung cao (C7, A6, G6, D7): tiếng 'ting' đủ "
        "dải 60 ms, phần ngân chỉ còn trên 5 kHz (lọc cao bậc 8). Vòng 2 sau thẻ ảnh: vòng 1 dùng cả nắm xu (hai đầu tiếng, "
        "tiếng to tới muộn 100 ms) và lọc bậc 4 để lại vạch nốt chuông −65 dB tới hết file. Biến thể n dùng nốt n.",
        [{"id": "coin", "role": "attack", "gainDb": -2, "trim": {"startMs": 150, "endMs": 238}, "fadeOutMs": 50,
          "filters": [{"type": "highpass", "hz": 400}], "source": _lib("kenney/rpg-audio/Audio/handleCoins.ogg")},
         _cycle({"id": "ting", "role": "sweetener", "gainDb": -6, "offsetMs": 8, "trim": {"endMs": 60}, "fadeOutMs": 40}, chimes),
         _cycle({"id": "ring", "role": "tail", "gainDb": -4, "offsetMs": 8, "fadeOutMs": 220,
                 "filters": [{"type": "highpass", "hz": 5000, "order": 8}]}, chimes)],
        coin_chain, 4, 2501, "sfx/battle/coin")
    out["coin.short"] = _recipe(
        "coin.short", "default", "thuong",
        "Lô 1 (BATCH1_BRIEF #27), hướng 'tắt nhanh ở 1–4 kHz': một tiếng xu chạm khác (Kenney RPG handleCoins2, cắt "
        "110–165 ms), chuông Hand Chimes đủ dải giữ 262 ms và mờ dần từ 32 ms, nên nghe ra nốt rồi tắt, không đọng dưới giọng "
        "đọc. Vòng 2, 3: vòng 1 ngắn hơn 240 ms của thẻ và dùng cả nắm xu; vòng 2 dài 238 ms. Biến thể n dùng nốt n.",
        [{"id": "coin", "role": "attack", "gainDb": -2, "trim": {"startMs": 110, "endMs": 165}, "fadeOutMs": 30,
          "filters": [{"type": "highpass", "hz": 400}], "source": _lib("kenney/rpg-audio/Audio/handleCoins2.ogg")},
         _cycle({"id": "chime", "role": "sweetener", "gainDb": -6, "offsetMs": 8, "trim": {"endMs": 262},
                 "fadeOutMs": 230}, chimes)],
        coin_chain, 4, 2502, "sfx/battle/coin")
    # ---- leak: the 0a kẻng (4/5), finished: pattern, tail, level; one candidate with a small drum under it
    leak_chain = {"dcHpfHz": 35, "filters": [{"type": "peak", "hz": 2500, "gainDb": -4, "q": 0.8}],
                  "headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": 1250,
                  "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 900}, "normalise": NORM,
                  "limiter": {"ceilingDbtp": -1.0, "releaseMs": 80, "maxGrDb": 6}}
    sub = {"id": "sub", "role": "sub", "source": {"synth": "sub_thump", "params": {"startHz": 70, "endHz": 45, "glideMs": 80,
                                                                                    "durMs": 260, "decayMs": 240}}, "gainDb": -12}
    out["leak"] = _recipe(
        "leak", "rare-fixed", "nen",
        "Lô 1 (BATCH1_BRIEF #28): kẻng sắt VCSL Anvil ba nhát (0a v2, anh chấm 4/5, 0d842a87). Chỉ hoàn thiện: 1) đúng "
        "nhịp 0a (0, 0,28, 0,56 s) nhưng đuôi tắt dần tự nhiên theo hàm mũ tới 1,25 s thay cho làm mờ 250 ms; 2) nhịp dồn "
        "hơn (0, 0,24, 0,48 s), nhát cuối ngân dài hơn. Sub nhẹ dưới nhát đầu, khoét 2,5 kHz như 0a.",
        [_cycle({"id": "strike", "role": "body", "fadeOutMs": 200},
                [_smp("anvil", "0:anvil-hit2:0.4:105 0.28:anvil-hit2:0.4:90 0.56:anvil-hit2:0.65:80"),
                 _smp("anvil", "0:anvil-hit2:0.4:105 0.24:anvil-hit2:0.4:92 0.48:anvil-hit2:0.75:84")]),
         json.loads(json.dumps(sub))],
        leak_chain, 2, 2801, "sfx/alerts/leak")
    out["leak.drum"] = _recipe(
        "leak.drum", "rare-fixed", "nen",
        "Lô 1 (BATCH1_BRIEF #28): ứng viên thêm 'kẻng cộng trống hội nhỏ'. Kẻng như bản 1 (nhịp 0a), cộng trống khung VCSL "
        "đánh mở dưới nhát đầu và nhát cuối (−7 dB, lọc thấp 1,5 kHz để trống không lấn dải giọng).",
        [{"id": "strike", "role": "body", "fadeOutMs": 200,
          "source": _smp("anvil", "0:anvil-hit2:0.4:105 0.28:anvil-hit2:0.4:90 0.56:anvil-hit2:0.65:80")},
         {"id": "drum", "role": "body", "gainDb": -7, "fadeOutMs": 200, "filters": [{"type": "lowpass", "hz": 1500, "order": 2}],
          "source": _smp("frame-drum", "0:hdruml-hit:0.6:100 0.56:hdruml-hit:0.6:88")},
         json.loads(json.dumps(sub))],
        leak_chain, 1, 2802, "sfx/alerts/leak")
    # ---- ui-move: the final from VCSL Slit Drum (0a v3 3/5, ea8b0706)
    out["ui-move"] = _recipe(
        "ui-move", "rare-fixed", "phim-ui",
        "Lô 1 (BATCH1_BRIEF 4.4): bản cuối từ trống khe VCSL Slit Drum (anh chọn 0a v3, ea8b0706). Máy chấm sai id này "
        "(0/3 cặp; anh chọn bản ít năng lượng 1–5 kHz nhất), nên ba bản trải đều thay vì theo điểm máy: 1) khe cao, lớp "
        "nhẹ, lớp 'giấy' nhỏ hơn 0a 6 dB; 2) khe thấp, lớp nhẹ; 3) khe cao, lớp vừa (velocity 90). Lên ≤ 3 ms, 40 ms.",
        [_cycle({"id": "tap", "role": "attack", "filters": [{"type": "highpass", "hz": 500}], "trim": {"endMs": 60},
                 "fadeOutMs": 25},
                [_smp("slit-drum", "0:logdrumhi-medm:0.05:60"), _smp("slit-drum", "0:logdrumlo-medm:0.05:60"),
                 _smp("slit-drum", "0:logdrumhi-medm:0.05:90")]),
         {"id": "paper", "role": "sweetener", "gainDb": -20,
          "source": {"synth": "noise_burst", "params": {"color": "white", "durMs": 12, "attackMs": 0.3, "decayMs": 9,
                                                        "hpHz": 3000, "lpHz": 8000}}}],
        {"dcHpfHz": 60, "filters": [{"type": "peak", "hz": 2200, "gainDb": -3, "q": 0.9}],
         "headTrim": {"thresholdDb": -50, "preRollMs": 0.2}, "maxLengthMs": 46, "tail": {"floorDb": -60, "fadeMs": 6},
         "normalise": NORM, "limiter": {"ceilingDbtp": -1.0, "releaseMs": 20, "maxGrDb": 6}},
        3, 2601, "sfx/ui/ui-move")
    # ---- ui-pick: clapper + Hand Chimes A5 (0a v3 3/5, 2b7be772): the bell louder or softer
    out["ui-pick"] = _recipe(
        "ui-pick", "rare-fixed", "phim-ui",
        "Lô 1 (BATCH1_BRIEF 4.4): bản cuối phách gỗ VCSL Woodblock wood-click2 rồi chuông Hand Chimes A5 (anh chọn 0a v3, "
        "2b7be772). Hai bản quanh bản 0a: 1) chuông to hơn (velocity 110, khoảng +3 dB); 2) chuông nhỏ hơn (velocity 64, "
        "khoảng −4 dB). Phách giữ đúng 0a (cắt 6 ms đầu, lọc cao 600 Hz, +6 dB).",
        [{"id": "clapper", "role": "attack", "source": _smp("woodblock", "0:wood-click2:0.1:60"),
          "filters": [{"type": "highpass", "hz": 600}], "trim": {"startMs": 6, "endMs": 70}, "fadeOutMs": 35,
          "fadeInMs": 0.3, "gainDb": 6},
         _cycle({"id": "bell", "role": "sweetener", "offsetMs": 40, "gainDb": -14, "fadeOutMs": 200},
                [_smp("hand-chimes", "0:A5:0.6:110"), _smp("hand-chimes", "0:A5:0.6:64")])],
        {"dcHpfHz": 60, "filters": [{"type": "peak", "hz": 2500, "gainDb": -2, "q": 0.8}],
         "headTrim": {"thresholdDb": -50, "preRollMs": 0.3}, "maxLengthMs": 650, "tail": {"floorDb": -60, "fadeMs": 120},
         "normalise": NORM, "limiter": LIMIT},
        2, 2602, "sfx/ui/ui-pick")
    return out


def step_recipes(run: str, force: bool = False) -> None:
    from build import render

    pools = step_layers(run)
    for rid, data in recipes_from(pools).items():
        p = recipe_path(rid)
        p.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", "utf-8")
        out = recipe_run(rid, run)
        if out.is_dir() and (out / "render.json").is_file() and not force:
            _say(f"recipe {rid}: đã có {out}")
            continue
        res = render.render(p, out=out, spec=card_path(rid.split(".")[0]))
        _say(f"recipe {rid}: {res.report['count']} biến thể, mức id {res.report['idLevel']} LUFS-M; "
             + ("; ".join(res.report["warnings"]) or "không cảnh báo"))


RECIPE_IDS = ("word-hit.d1", "word-hit.d2", "word-hit.d3", "word-hit-bell", "wordshot-fire.mix", "blast.mix",
              "coin.ring", "coin.short", "leak", "leak.drum", "ui-move", "ui-pick")


# ---------------------------------------------------------------- step 5: critic

# takes the owner rated in batch 0a, put next to the new ones (heard again blind: a consistency check). The 0a word-hit
# C4 (e79e84d1) and the 0b call-chop takes (1bbffcc4, 3e5ee6dc) are reproduced bit for bit by this batch's recipe and
# chain, so they are already in the run.
REF_0A = {
    "leak": env.WORK / GAME / "leak" / "batch0-2026-10-23-r2" / "masters" / "leak-v2.wav",            # 0d842a87, 4/5
    "ui-move": env.WORK / GAME / "ui-move" / "batch0-2026-10-23-r2" / "masters" / "ui-move-v3.wav",   # ea8b0706, 3/5
    "ui-pick": env.WORK / GAME / "ui-pick" / "batch0-2026-10-23-r2" / "masters" / "ui-pick-v3.wav",   # 2b7be772, 3/5
}
REF_SHA8 = {"e79e84d1": "word-hit 0a C4, 3/5", "1bbffcc4": "call-chop 0b A s1006, 3/5", "3e5ee6dc": "call-chop 0b E s2003, 3/5",
            "0d842a87": "leak 0a v2, 4/5", "ea8b0706": "ui-move 0a v3, 3/5", "2b7be772": "ui-pick 0a v3, 3/5"}
WHOOSH = "wordshot-fire"       # whooshes swell (attack 20-60 ms): ranked again at raw stage, offered as rule-blocked


def finals(run: str) -> tuple[list[Path], list[Path]]:
    dirs, srcs = [], []
    for sid in JOBS:
        p = id_dir(sid, run) / "processed"
        if p.is_dir():
            dirs.append(p)
            srcs.append(p / "SOURCES.json")
    for rid in RECIPE_IDS:
        r = recipe_run(rid, run)
        dirs.append(r / "masters")
        srcs.append(r / "SOURCES.json")
    for p in REF_0A.values():
        dirs.append(p)
        srcs.append(p.parent.parent / "SOURCES.json")
    return dirs, srcs


def step_critic(run: str, force: bool = False) -> None:
    from critic.__main__ import main as critic

    out = critic_out(run, "final")
    if (out / "_batch.json").is_file() and not force:
        _say(f"critic: đã có {out}")
    else:
        dirs, srcs = finals(run)
        wait_heavy_free("critic")
        argv = ["run", *map(str, dirs), "--spec", str(LAB / "specs" / GAME), "--stage", "final", "--layers", "all",
                "--out", str(out), "--seed", str(SEED), "--blind-cards", "--quiet"]
        for s_ in srcs:
            argv += ["--sources", str(s_)]
        t0 = time.time()
        _say(f"critic final ({len(dirs)} mục): mã {critic(argv)}, {time.time() - t0:.0f} s")
    info = critic_out(run, "whoosh-info")
    if not (info / "_batch.json").is_file() or force:
        proc = id_dir(WHOOSH, run) / "processed"
        wait_heavy_free("critic whoosh")
        argv = ["run", str(proc), "--spec", str(card_path(WHOOSH)), "--stage", "raw", "--layers", "all",
                "--out", str(info), "--seed", str(SEED), "--sources", str(proc / "SOURCES.json"), "--blind-cards", "--quiet"]
        _say(f"critic tiếng vút (giai đoạn raw: L3–L5 cho bản mà luật lên 10 ms của thẻ chặn): mã {critic(argv)}")
    raw = critic_out(run, "raw")
    if not (raw / "_batch.json").is_file() or force:
        raws = [str(d) for sid in JOBS for d in raw_dirs(sid, run) if d.parent.name == run]
        argv = ["run", *raws, "--spec", str(LAB / "specs" / GAME), "--stage", "raw", "--layers", "L1,L1b",
                "--out", str(raw), "--quiet"]
        _say(f"critic raw L1 (clip đọc bản float): mã {critic(argv)}")


# ---------------------------------------------------------------- step 5b: ledger + release check

def staging_dirs(run: str) -> tuple[Path, Path]:
    """Batch-local release tree. Not ~/AudioLab/review/staging: nothing here is owner-approved yet."""
    root = base_dir(run) / "staging" / GAME
    return root / "art-src" / "audio", root / "public" / "assets" / GAME / "audio"


def licence_rows_of(path: Path) -> dict:
    """The record and licence rows behind one listened file (any run folder with SOURCES.json)."""
    from build import ledger
    folder = path.parent.parent if path.parent.name == "masters" else path.parent
    recs = ledger.records(ledger.read_sources(folder / "SOURCES.json"))
    sha = ledger.sha256_file(path)
    rec = next((r for r in recs.values() if r.get("sha256") == sha or r.get("masterSha256") == sha), None)
    rows_path = folder / "licences.rows.jsonl"
    rows = [json.loads(x) for x in rows_path.read_text("utf-8").splitlines() if x.strip()] if rows_path.is_file() else []
    kinds: dict[str, int] = {}
    for r in rows:
        kinds[r.get("kind") or r.get("type") or "?"] = kinds.get(r.get("kind") or r.get("type") or "?", 0) + 1
    layers = (rec or {}).get("layers") or []
    return {"record": rec is not None, "layers": len(layers),
            "licences": sorted({(lay.get("licence") or (lay.get("source") or {}).get("licence") or "?") for lay in layers}),
            "ai_steps": len((rec or {}).get("aiSteps") or []), "rows": len(rows), "row_kinds": kinds}


def step_link(run: str, force: bool = False) -> int:
    from build import critic_link, licence_check, release

    outs = [critic_out(run, n) for n in ("final", "whoosh-info") if critic_out(run, n).is_dir()]
    for sid in JOBS:
        p = id_dir(sid, run) / "processed"
        if (p / "SOURCES.json").is_file():
            res = critic_link.apply(p / "SOURCES.json", outs, p / "licences.rows.jsonl")
            _say(f"mark-ai {sid}/processed: {res['steps']} bước, {res['files']} hồ sơ")
    art, pub = staging_dirs(run)
    for rid in RECIPE_IDS:
        r = recipe_run(rid, run)
        res = critic_link.apply(r / "SOURCES.json", outs, r / "licences.rows.jsonl")
        rel = release.release(r, None, art, pub)
        _say(f"mark-ai {rid} (công thức): {res['steps']} bước; cây thử: {len(rel['files'])} file, {rel['rowsAdded']} dòng sổ, "
             f"{len(rel['licenceCopies'])} bản giấy phép")
    rc = licence_check.main(["--art-src", str(art), "--public", str(pub)])
    _say(f"licence-check (cây thử, các công thức) {GAME}: mã {rc}")
    return rc


# ---------------------------------------------------------------- step 6: listening lists (plan §4.6 step 2)

NO_PICK_FLAGS = {"double_onset", "lr_imbalance"}           # batch 0b review 2: never offered
PROBE_IDS = ("wordshot-fire", "ink-puff", "call-chop")     # 3/11 ids, about 30 %
DIRECTIONS = {"arrow-fire": {"dây ngân": ("A", "C"), "bật dây trầm": ("B", "D")},
              "ink-puff": {"giấy ướt bục": ("A", "B"), "phụt khói": ("C", "D")}}
SMALL_SPEAKER_IDS = {"wordshot-fire", "arrow-fire", "ink-puff", "blast", "coin", "leak", "call-chop"}
RULE_NOTE = {WHOOSH: "Bị luật chặn: tiếng vút lên chậm (> 10 ms); thẻ chờ đổi sang loại 'tiếng vút'"}


def _kind(d: dict) -> str:
    """recipe | sa3 | ref (a file rated in an earlier batch, by its hash)."""
    if d["file"].get("sha256", "")[:8] in REF_SHA8:
        return "ref"
    return "recipe" if "-recipe-" in d["file"]["path"] else "sa3"


def _rid(d: dict) -> str:
    """Recipe id of a master (word-hit.d1-v2 -> word-hit.d1), or the prompt letter of a take (A)."""
    stem = d["file"]["stem"]
    if "__" in stem:
        return stem.split("__")[1][:1]
    return stem.rsplit("-v", 1)[0]


def _variant(d: dict) -> int:
    try:
        return int(d["file"]["stem"].rsplit("-v", 1)[1].split("__")[0])
    except (IndexError, ValueError):
        return 0


def _probe(sid: str, order: list[dict], used: set[str]) -> dict | None:
    pool = [d for d in order[max(1, len(order) // 2):] if d["file"]["stem"] not in used]
    if not pool:
        return None
    rng = random.Random(int(hashlib.sha256(f"batch-1-td:{sid}".encode()).hexdigest()[:8], 16))
    return rng.choice(sorted(pool, key=lambda d: d["file"]["stem"]))


def _combined(d: dict) -> float | None:
    return (d.get("score") or {}).get("combined")


def select(run: str) -> dict[str, dict]:
    """Per id: the listening list (top, most different, the other direction or source, probes at ~30 % of ids)."""
    docs = _docs(critic_out(run, "final"))
    info = _docs(critic_out(run, "whoosh-info"))
    sel: dict[str, dict] = {}
    for sid in IDS:
        mine = [d for d in docs.values() if _sid(d) == sid]
        if sid == "blast":            # prompts A, B are paper layers of the recipe, not candidates
            mine = [d for d in mine if not (_kind(d) == "sa3" and _rid(d) in ("A", "B"))]
        ok = sorted([d for d in mine if d["verdict"] == "PASS"], key=_rank)
        e: dict = {"n": len(mine), "pass": len(ok), "picks": []}
        e["pass_unverified_onset"] = sum(1 for d in ok if not _verified(d))
        e["pass_no_pick_flags"] = sum(1 for d in ok if _flags(d) & NO_PICK_FLAGS)
        ok = [d for d in ok if _verified(d) and not _flags(d) & NO_PICK_FLAGS]
        if sid in SMALL_SPEAKER_IDS:        # BATCH1_BRIEF §2: battle sounds lose <= 6 dB through a 200 Hz high-pass
            loud = [d for d in ok if ((d.get("metrics") or {}).get("speaker_loss_db") or 0) <= 6.0]
            e["small_speaker_over_6db"] = len(ok) - len(loud)
            ok = loud or ok
        e["eligible"] = len(ok)
        picks: list[tuple[dict, str, str | None]] = []
        used = lambda: {d["file"]["stem"] for d, _, _ in picks}        # noqa: E731
        if sid == "word-hit":
            sets: dict[str, dict] = {}
            for d in mine:
                sets.setdefault(_rid(d), {})[_variant(d)] = d
            rows = []
            for rid, notes in sets.items():
                sc = [_combined(d) for d in notes.values() if d["verdict"] == "PASS" and _combined(d) is not None]
                rows.append({"rid": rid, "pass": sum(1 for d in notes.values() if d["verdict"] == "PASS"), "n": len(notes),
                             "median": float(np.median(sc)) if sc else -1e9,
                             "pitch_off_max": max(((d.get("metrics") or {}).get("pitch_off_cents") or 0) for d in notes.values()),
                             "files": {SCALE[v - 1]: d["file"]["path"] for v, d in sorted(notes.items()) if 1 <= v <= 7}})
            rows.sort(key=lambda r: (-r["pass"], -r["median"]))
            e["directions"] = rows
            e["sets"] = {r["rid"]: r["files"] for r in rows}
            c4 = {r["rid"]: sets[r["rid"]].get(2) for r in rows if sets[r["rid"]].get(2) is not None}
            if rows and rows[0]["rid"] in c4:
                top = c4[rows[0]["rid"]]
                picks.append((top, "top", None))
                rest = [c4[r["rid"]] for r in rows[1:] if r["rid"] in c4]
                dis = _distinct(top, rest)
                if dis is not None:
                    picks.append((dis, "distinct", None))
                picks += [(d, "other", None) for d in rest if d is not dis]
            # direction 1 renders the 0a recipe again: its C4 is the rated take itself (a consistency pair)
            picks = [(d, "ref-0a" if _kind(d) == "ref" else r, n) for d, r, n in picks]
            e["picks"] = picks
            sel[sid] = e
            continue
        if sid in ("leak", "ui-move", "ui-pick"):
            # finals around a rated take: the take again (blind), then every new candidate (ui-move: the machine
            # disagreed with the owner on 3/3 pairs, so the list is not cut by its ranking)
            ref = [d for d in mine if _kind(d) == "ref"]
            new = [d for d in ok if _kind(d) != "ref"]
            if new:
                picks.append((new[0], "top", None))
                dis = _distinct(new[0], new[1:])
                if dis is not None:
                    picks.append((dis, "distinct", None))
                picks += [(d, "other", None) for d in new[1:] if d is not dis]
            if ref:
                picks.append((ref[0], "ref-0a", None))
            e["picks"] = picks[:4]
            sel[sid] = e
            continue
        if not ok and sid != WHOOSH:
            sel[sid] = e
            continue
        top = ok[0] if ok else None
        if top is not None:
            picks.append((top, "top", None))
        if sid in DIRECTIONS:
            mine_dir = next((k for k, v in DIRECTIONS[sid].items() if _rid(top) in v), None)
            other = [d for d in ok if mine_dir is None or _rid(d) not in DIRECTIONS[sid][mine_dir]]
            if other:
                picks.append((other[0], "direction-2", None))
            if sid not in PROBE_IDS:
                dis = _distinct(top, [d for d in _upper(ok) if d["file"]["stem"] not in used()])
                if dis is not None:
                    picks.append((dis, "distinct", None))
        elif sid == "blast":
            other = [d for d in ok if _kind(d) != _kind(top)]
            if other:
                picks.append((other[0], "recipe-best" if _kind(other[0]) == "recipe" else "sa3-best", None))
            dis = _distinct(top, [d for d in _upper(ok) if d["file"]["stem"] not in used()])
            if dis is not None:
                picks.append((dis, "distinct", None))
        elif sid == "coin":
            # the variants of one direction differ only by the chime's note (the cards showed coin.ring v2 and v3 as
            # the same sound a tone apart): the other direction is the most different take
            other = [d for d in ok if _rid(d) != _rid(top)]
            if other:
                picks.append((other[0], "direction-2", None))
        elif sid == "word-hit-bell":
            picks += [(d, r, None) for d, r in zip(ok[1:], ("distinct", "other"))]
        elif sid == WHOOSH:
            if top is not None:
                other = [d for d in ok if _kind(d) != _kind(top)]
                if other:
                    picks.append((other[0], "recipe-best" if _kind(other[0]) == "recipe" else "sa3-best", None))
            blocked = [d for d in mine if d["verdict"] == "BLOCK" and set(d["L1"]["blocking"]) <= {"attack", "dc_offset"}
                       and _verified(d) and not _flags(d) & NO_PICK_FLAGS]
            ranked = sorted([info[d["file"]["stem"]] for d in blocked if d["file"]["stem"] in info], key=_rank)
            covered = {_rid(d) for d, _, _ in picks if _kind(d) == "sa3"}
            ranked = [d for d in ranked if _rid(d) not in covered] or ranked
            e.update({"rule_blocked": len(blocked)})
            if ranked:
                picks.append((ranked[0], "rule-blocked-top", RULE_NOTE[WHOOSH]))
        else:
            dis = _distinct(top, [d for d in _upper(ok) if d["file"]["stem"] not in used()])
            if dis is not None:
                picks.append((dis, "distinct", None))
        if sid in PROBE_IDS:
            pr = _probe(sid, ok, used())
            if pr is not None:
                picks.append((pr, "probe", None))
        if sid == "call-chop" and top is not None and _kind(top) == "ref":
            new = [d for d in ok if "__s300" in d["file"]["stem"] and d["file"]["stem"] not in used()]
            if new:
                picks.insert(1, (new[0], "top-new-seed", None))
        if sid == "call-chop":
            refs = [d for d in mine if d["file"].get("sha256", "")[:8] == "1bbffcc4"]
            if refs and refs[0]["file"]["stem"] not in used():
                picks.append((refs[0], "ref-0b", None))
        e["picks"] = picks[:4]
        sel[sid] = e
    return sel


# ---------------------------------------------------------------- step 7: in-game context renders

SCENARIO = {**{sid: "td-wordhit-chain" for sid in S5}, "leak": "td-night", "call-chop": "td-night",
            "ui-move": "td-menu", "ui-pick": "td-menu"}


def fixed_slots(sel: dict) -> dict:
    """Every slot a render does not test: this batch's top (word-hit: the top direction's scale); the rated 0a
    takes for leak and the UI (their finals are what this batch tests)."""
    out: dict = {}
    for sid in IDS:
        picks = sel.get(sid, {}).get("picks") or []
        if sid == "word-hit":
            sets = sel[sid].get("sets") or {}
            if picks:
                out[sid] = {n: Path(p) for n, p in sets[_rid(picks[0][0])].items()}
            continue
        if picks:
            out[sid] = Path(picks[0][0]["file"]["path"])
    for sid, p in REF_0A.items():
        if p.is_file():
            out[sid] = p
    return out


def ctx_dir(run: str) -> Path:
    return base_dir(run) / "context"


def _slot_for(sid: str, d: dict, sel: dict):
    if sid == "word-hit":
        return {n: Path(p) for n, p in sel[sid]["sets"][_rid(d)].items()}
    return Path(d["file"]["path"])


def step_context(run: str, force: bool = False) -> dict:
    from context import td_scenes

    sel = select(run)
    fixed = fixed_slots(sel)
    done: dict = {"fixed": {k: ({n: str(p) for n, p in v.items()} if isinstance(v, dict) else str(v)) for k, v in fixed.items()},
                  "renders": {}, "current": {}}
    for sid in IDS:
        for d, role, _ in sel[sid]["picks"]:
            stem = d["file"]["stem"]
            out = ctx_dir(run) / sid / f"{stem}.wav"
            if out.is_file() and out.with_suffix(".json").is_file() and not force:
                doc = json.loads(out.with_suffix(".json").read_text("utf-8"))
            else:
                slots = dict(fixed)
                slots[sid] = _slot_for(sid, d, sel)
                doc = td_scenes.render(SCENARIO[sid], slots, out, focus=sid)
            done["renders"].setdefault(sid, {})[stem] = {"file": str(out), "role": role, "metrics": doc["metrics"]}
            vc = (doc["metrics"].get("voice") or {}).get("min_db")
            _say(f"context {sid} {stem}: {SCENARIO[sid]}, giọng 1–4 kHz min {vc} dB, "
                 f"đỉnh {doc['metrics']['mix']['true_peak_dbtp']} dBTP")
    # the game's current playback (frame starts, 1 s windows) once, with the fixed slots: what the wiring step fixes
    for scen in ("td-wordhit-chain", "td-night"):
        out = ctx_dir(run) / "_current" / f"{scen}.wav"
        if out.is_file() and not force:
            doc = json.loads(out.with_suffix(".json").read_text("utf-8"))
        else:
            doc = td_scenes.render(scen, fixed, out, focus="arrow-fire", config="current")
        done["current"][scen] = {"file": str(out), "metrics": doc["metrics"]}
    (ctx_dir(run) / "context.json").write_text(json.dumps(done, ensure_ascii=False, indent=1, default=float), "utf-8")
    return done


# ---------------------------------------------------------------- step 8: board sessions

DESC = {
    "word-hit": "Nốt đàn tranh sau mỗi từ, cả thang hạ một quãng tám (A3 khi gõ ẩu, rồi C4 D4 F4 G4 A4 C5 theo bậc "
                "Chuỗi). Ba bản là ba hướng của cùng bộ 7 nốt; 'Một mình' và 'Lặp' chỉ phát nốt C4, 'Trong trận thô' "
                "phát cả thang theo thứ tự, có giọng đọc, Phát Chữ, tháp cung. Có ra đàn tranh Việt không, hay nghe "
                "như đàn Trung Quốc? Giọng đọc có rõ ngay sau nốt không?",
    "word-hit-bell": "Chuông thêm khi gõ Hoàn hảo hoặc Chớp (0,5 s, luôn giống nhau). Ba bản: hai nốt chuông tay nhỏ và "
                     "một chuông ống (Tubular Bells). Có hợp làng tre không, có gợi chuông chùa, chuông nhà thờ không? "
                     "'Trong trận thô': chuông ở từ thứ 4 và từ cuối",
    "wordshot-fire": "Phát Chữ bay ra khi gõ xong từ: vút nhanh, có tiếng giấy, tre (144–216 ms). Bản có nhãn ghi sẵn bị "
                     "luật đầu tiếng chặn vì tiếng vút lên chậm; anh chấm như mọi bản. Nghe 'Trong trận thô' trước",
    "arrow-fire": "Tháp Cung bắn, tới 4 lần mỗi giây, nhẹ, nằm dưới mọi thứ (64–96 ms). Hai hướng: dây cung ngân, và bật "
                  "dây trầm có tiếng vút nhỏ. Trong trận: ba tháp bắn đều, có thành từng cụm rồi im không? Có gắt không?",
    "ink-puff": "Quái Mực Câm tan, tới 8 lần mỗi giây: mềm, không máu (120–180 ms). Hai hướng: túi giấy ướt bục, và phụt "
                "khói giấy. Dày như trong trận mà có thành tiếng rè không?",
    "blast": "Tháp Pháo nổ, cụm Phát Chữ: tiếng trống đầm và giấy, bụi tung (320–480 ms). Không nổ lách tách, không trống "
             "taiko. Một bản là âm Stable Audio 3 nguyên khối để so. Thử thêm 'Loa nhỏ'",
    "coin": "Đồng xu rơi sau khi hạ quái, tới 3 lần mỗi giây (240–360 ms). Hai hướng: chuông ngân rất cao, và chuông tắt "
            "nhanh. Có nhàm khi nghe dày không, có che giọng đọc không?",
    "leak": "Quái lọt vào Lũy: kẻng sắt ba nhát (anh đã chấm 4/5 ở lô 0a). Bản cuối: một bản giữ nhịp cũ với đuôi tắt tự "
            "nhiên, một bản nhịp dồn hơn, một bản có trống nhỏ bên dưới; một bản là bản 0a. Bản cuối không được kém 4/5",
    "call-chop": "Lời gọi Chặt sáng lên: gõ gỗ trầm, chắc vào thân tre (200–300 ms). Không được giống mõ chùa: nghe ra mõ "
                 "thì gắn 'sai chất liệu'. 'Trong trận thô': cảnh đêm, gọi Chặt hai lần giữa lúc gõ",
    "ui-move": "Chuyển mục trên màn đầu: chạm rất nhẹ lên trống khe (40 ms), không to hơn phím. Ba bản mới và bản 0a anh đã "
               "chọn. 'Trong trận thô': lướt menu năm bước rồi chọn",
    "ui-pick": "Chọn một mục: phách gỗ rồi chuông tay A5 (anh đã chọn hướng này ở lô 0a). Khác nhau ở độ to của chuông",
}
CONTEXTS = {"word-hit": ["scene", "loop", "alone", "small"], "word-hit-bell": ["scene", "alone", "loop"],
            "wordshot-fire": ["scene", "loop", "alone", "small"], "arrow-fire": ["scene", "loop", "alone", "small"],
            "ink-puff": ["scene", "loop", "alone", "small"], "blast": ["scene", "alone", "small", "loop"],
            "coin": ["scene", "loop", "alone", "small"], "leak": ["alone", "scene", "small"],
            "call-chop": ["alone", "scene", "loop"], "ui-move": ["alone", "scene", "loop"], "ui-pick": ["alone", "scene"]}
SESSIONS = [("1-td-s5", "Lô 1 · Lời Gọi · chuỗi từ và trận (S5)", S5),
            ("1-td-s6", "Lô 1 · Lời Gọi · báo nguy, lời gọi, UI (S6)", S6)]


class SessionExists(RuntimeError):
    pass


def _cand(d: dict, role: str, out: Path, note: str | None, ctx: Path | None) -> dict:
    from board import session
    c = {"file": session.display_path(Path(d["file"]["path"])), "role": role,
         "critic": session.display_path(out / f"{d['file']['stem']}.json")}
    card = d.get("card_blind") or d.get("card")
    if card and (out / card).is_file():
        c["card"] = session.display_path(out / card)
    if note:
        c["note"] = note
    if ctx is not None and ctx.is_file():
        c["ctx"] = {"scene": session.display_path(ctx)}
    return c


def _loop(sid: str, picks: list) -> dict | None:
    import yaml
    card = yaml.safe_load(card_path(sid).read_text("utf-8")) or {}
    rate = (card.get("critic") or {}).get("rate_hz")
    gap = (card.get("playback") or {}).get("min_gap_ms") or 0
    longest = max((d["metrics"].get("duration_ms") or 0) for d, _, _ in picks)
    if sid == "call-chop":
        rate = 3.0                                    # alerts at most 3 a second (audio-min.ts ALERTS_PER_S)
    if sid in ("ui-move",):
        rate = 4.0                                    # a quick menu walk
    if sid == "blast":
        rate = 1 / 1.2                                # two cannon towers, 2.2-2.6 s each (content/slice-1a.ts)
    if not rate and not gap:
        return None
    iv = int(max(1000.0 / rate if rate else 0, gap, longest + 50))
    return {"interval_ms": iv, **({"count": 8} if iv >= 1000 else {})}


def step_session(run: str, force: bool = False) -> list[Path]:
    sel = select(run)
    paths = []
    for name, title, ids in SESSIONS:
        items = []
        for sid in ids:
            picks = sel[sid]["picks"]
            if not picks:
                _say(f"phiên {name}: {sid} không có bản nào để nghe")
                continue
            cands = []
            for d, role, note in picks:
                ctx = ctx_dir(run) / sid / f"{d['file']['stem']}.wav"
                out = critic_out(run, "whoosh-info") if role.startswith("rule-blocked") else critic_out(run, "final")
                cands.append(_cand(d, role, out, note, ctx))
            sp = picks[0][0].get("spec") or {}
            item = {"id": sid, "family": sp.get("family") or "", "group": sp.get("group") or "", "desc": DESC[sid],
                    "probe": any(r == "probe" for _, r, _ in picks), "contexts": CONTEXTS[sid], "candidates": cands}
            lp = _loop(sid, picks)
            if lp:
                item["loop"] = lp
            items.append(item)
        folder = env.REVIEW / GAME / "sessions"
        path = folder / f"{name}.json"
        if path.exists() and not force:
            raise SessionExists(f"{path} đã có; thêm --force để ghi đè (điểm đã chấm vẫn giữ trong ratings.jsonl)")
        folder.mkdir(parents=True, exist_ok=True)
        doc = {"schema": "audiolab.board.session/1", "session": name, "game": GAME, "batch": "1", "title": title,
               "seed": int(hashlib.sha256(f"{GAME}:{name}".encode()).hexdigest()[:8], 16), "max_minutes": 20,
               "anchors": 4, "reveal": "end", "items": items}
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", "utf-8")
        from board import session as S
        S.load(path)                    # validate now (paths, ctx files, contexts)
        paths.append(path)
        _say(f"phiên {path}: {len(items)} id, {sum(len(i['candidates']) for i in items)} bản (+4 cặp mốc khi mở)")
    return paths


# ---------------------------------------------------------------- step 9: report

def row(d: dict, role: str) -> dict:
    m, s_ = d["metrics"], d.get("score") or {}
    l3 = ((d.get("L3") or {}).get("scores")) or {}
    ast = (((d.get("L4") or {}).get("ast") or {}).get("top5") or [])[:2]
    return {"stem": d["file"]["stem"], "file": d["file"]["path"], "sha8": d["file"].get("sha256", "")[:8], "role": role,
            "kind": _kind(d), "verdict": d["verdict"], "blocking": d["L1"]["blocking"],
            "rank": s_.get("rank"), "n_ranked": s_.get("n_ranked"), "combined": s_.get("combined"),
            "L2": (d.get("L2") or {}).get("score"), "PQ": l3.get("PQ"), "CE": l3.get("CE"),
            "ast": [(a[0], round(float(a[1]), 2)) if isinstance(a, (list, tuple)) else (a.get("label"), round(a.get("score"), 2))
                    for a in ast],
            "flags": sorted(_flags(d)), "licence": licence_rows_of(Path(d["file"]["path"])),
            "metrics": {k: m.get(k) for k in ("duration_ms", "attack_ms", "crest_db", "share_below_150", "share_200_800",
                                               "share_1k_4k", "share_above_3k", "centroid_hz", "tail_ms", "lufs_m_max",
                                               "speaker_loss_db", "pitch_off_cents", "f0_hz") if m.get(k) is not None}}


def step_report(run: str, force: bool = False) -> Path:
    sel = select(run)
    ctx = {}
    cj = ctx_dir(run) / "context.json"
    if cj.is_file():
        ctx = json.loads(cj.read_text("utf-8"))
    obs = {}
    oj = base_dir(run) / "observations.json"
    if oj.is_file():
        obs = json.loads(oj.read_text("utf-8"))
    b = json.loads((critic_out(run, "final") / "_batch.json").read_text("utf-8"))
    c = b.get("counts") or {}
    summary = {"run": run, "counts": c, "n_files": b.get("n_files"), "ids": {}, "fixed_slots": ctx.get("fixed"),
               "current_playback": {k: (v.get("metrics") or {}).get("caps") for k, v in (ctx.get("current") or {}).items()}}
    L = ["# Lô 1 · Lời Gọi (P5)", "",
         "Tự sinh bởi `common/batch1_td.py report`. Thẻ ảnh của bộ chấm: `critic-final/<tên>.png` (bản cho Bảng Nghe: "
         "`.blind.png`); bản dựng trong bối cảnh: `context/<id>/<tên>.wav|.png|.json`; cách phát hiện tại của game: "
         "`context/_current/`.", "",
         f"Lần chấm cuối: {b.get('n_files')} file, {c.get('PASS', 0)} ĐẠT, {c.get('BLOCK', 0)} CHẶN, "
         f"{c.get('NEEDS_FIX', 0)} CẦN SỬA; hiệu chỉnh `{(b.get('calibration') or {}).get('id') or 'owner-v1'}`.", "",
         "Không đưa vào phiên: bản có đầu tiếng chưa xác minh, cờ `double_onset` (hai đầu tiếng) hay `lr_imbalance`. "
         "Lớp giấy A, B của `blast` là lớp của công thức, không phải ứng viên.", ""]
    if obs.get("_findings"):
        L += ["## Phát hiện trong bối cảnh và trên thẻ ảnh", ""] + [f"- {x}" for x in obs["_findings"]] + [""]
    summary["findings"] = obs.get("_findings") or []
    for sid in IDS:
        e = sel[sid]
        rows = [row(d, r) for d, r, _ in e["picks"]]
        rend = (ctx.get("renders") or {}).get(sid) or {}
        for r_ in rows:
            r_["context"] = (rend.get(r_["stem"]) or {}).get("metrics")
            r_["observation"] = (obs.get(sid) or {}).get(r_["stem"])
        summary["ids"][sid] = {**{k: v for k, v in e.items() if k not in ("picks", "sets")}, "picks": rows,
                               "sets": e.get("sets"), "note": (obs.get(sid) or {}).get("_id")}
        L += [f"## `{sid}`", "", f"{e['n']} bản cuối, {e['pass']} qua L1, {e.get('eligible', 0)} được chọn vào danh sách nghe "
              f"(sau các luật không chọn)." + (f" {e['rule_blocked']} bản bị luật lên 10 ms chặn." if e.get("rule_blocked") else ""), ""]
        if e.get("directions"):
            L += ["| Hướng | Qua L1 | Điểm tổng trung vị | Lệch cao độ lớn nhất (cent) |", "|---|---|---|---|"]
            L += [f"| `{r['rid']}` | {r['pass']}/{r['n']} | {_fmt(r['median'], 2)} | {_fmt(r['pitch_off_max'])} |" for r in e["directions"]]
            L.append("")
        if (obs.get(sid) or {}).get("_id"):
            L += [obs[sid]["_id"], ""]
        L += ["| Vai trò | Bản | Mã | Loại | L1 | Hạng | Điểm | L2 | PQ | AST | Lên ms | Dài ms | <150 Hz | 1–4 kHz | Cờ | Bối cảnh | Giấy phép |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r_ in rows:
            m = r_["metrics"]
            cm = r_.get("context") or {}
            vc = (cm.get("voice") or {}).get("min_db")
            bd = (cm.get("focus_band_decay") or {}).get("min_db")
            ctxs = (f"giọng min {_fmt(vc)} dB, tệ nhất {_fmt((cm.get('voice_worst') or {}).get('min_db'))} dB; loa nhỏ "
                    f"{_fmt(cm.get('focus_small_speaker_loss_db'))} dB" + (f"; 1–4 kHz tụt {_fmt(bd)} dB/100 ms" if bd is not None else "")) if cm else "–"
            L.append(f"| {r_['role']} | `{r_['stem']}` | {r_['sha8']} | {r_['kind']} | {r_['verdict']} {','.join(r_['blocking'])} | "
                     f"{r_['rank'] or '–'}/{r_['n_ranked'] or '–'} | {_fmt(r_['combined'], 2)} | {_fmt(r_['L2'], 2)} | {_fmt(r_['PQ'], 2)} | "
                     f"{', '.join(f'{a} {s2}' for a, s2 in r_['ast']) or '–'} | {_fmt(m.get('attack_ms'))} | {_fmt(m.get('duration_ms'), 0)} | "
                     f"{_pct(m.get('share_below_150'))} | {_pct(m.get('share_1k_4k'))} | {', '.join(r_['flags']) or '–'} | {ctxs} | "
                     f"{', '.join(r_['licence']['licences'])}; {r_['licence']['layers']} lớp, {r_['licence']['rows']} dòng sổ, "
                     f"{r_['licence']['ai_steps']} bước AI |")
        notes = [f"- `{r_['stem']}`: {r_['observation']}" for r_ in rows if r_.get("observation")]
        if notes:
            L += ["", "Thẻ ảnh và bản dựng (Claude đọc):", *notes]
        L.append("")
    cur = summary["current_playback"]
    if cur:
        L += ["## Cách phát hiện tại của game và cách phát đề xuất (BATCH1_BRIEF L1, L2)", "",
              "| Kịch bản | Id | Cấu hình | Mô phỏng xin | Phát | Bỏ | Im lâu nhất (s) | Nhiều nhất trong 250 ms |", "|---|---|---|---|---|---|---|---|"]
        for scen, caps in cur.items():
            for cfg in ("current", "proposed"):
                for sid, s_ in ((caps or {}).get(cfg) or {}).items():
                    L.append(f"| {scen} | `{sid}` | {cfg} | {s_['asked']} | {s_['played']} | {s_['dropped']} | "
                             f"{_fmt(s_.get('longest_silence_s'), 2)} | {s_.get('max_in_250ms', '–')} |")
        L.append("")
    path = base_dir(run) / "REPORT.md"
    path.write_text("\n".join(L) + "\n", "utf-8")
    (base_dir(run) / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1, default=str), "utf-8")
    _say(f"báo cáo {path}")
    return path


STEPS = {"generate": step_generate, "process": step_process, "layers": step_layers, "recipes": step_recipes,
         "critic": step_critic, "link": step_link, "context": step_context, "session": step_session,
         "report": step_report}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="batch1_td", description="Lô 1 · Lời Gọi (P5 của BATCH1_BRIEF.md).")
    ap.add_argument("step", choices=[*STEPS, "all"])
    ap.add_argument("--run", default="b1")
    ap.add_argument("--force", action="store_true", help="làm lại bước đã có; ghi đè file phiên")
    a = ap.parse_args(argv)
    env.apply()
    for name in (list(STEPS) if a.step == "all" else [a.step]):
        try:
            rc = STEPS[name](a.run, a.force)
        except SessionExists as exc:
            print(f"batch1_td: {exc}", file=sys.stderr)
            return 1
        if isinstance(rc, int) and rc:
            return rc
    return 0


if __name__ == "__main__":
    sys.exit(main())
