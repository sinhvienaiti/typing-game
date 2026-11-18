"""Batch 1, Rồng Giữ Ải (dragon-hold): steps P2 and P3 of BATCH1_BRIEF.md (§4.2, §4.4, §6, §7).

  run.sh common.batch1_dh all [--run b1] [--force]
  run.sh common.batch1_dh generate|process|bodies|recipes|critic|link|context|session|report [--run b1]

generate  Stable Audio 3 from the spec cards (prompt.variants), one job at a time, model resident per job:
          fire.cast A-D, fire.impact.a B (24 more bodies), fire.impact.b C/E, fire.impact.c A/B (flare layer),
          enemy.quadruped.howl B at 2 s and 3 s (whole calls), trap.pine-bomb.trigger A/B, general.g01.horn A/B
          (3 s texture), amb.forest E/F (10 s), amb.river, enemy.swarm.march, enemy.quadruped.march (10 s).
process   gen/process.py on every raw take (true onsets, exponential tail, card channels; creatures whole;
          loops: comb notch, L/R balance, crossfade, seam check).
bodies    the fire bodies for the recipes: true onset of each raw take, window from 4 ms before the 5 ms level
          peak of the body, kept only with one high-band onset (no second hit) -> bodies.json.
recipes   build/recipes/dragon-hold/<id>.b1.json (fire.impact.a/b/c, wave.horn, general.g01.horn,
          trap.pine-bomb.trigger), body lists filled from bodies.json, rendered with build.render.
critic    one full critic run over every final (one model load, calibration owner-v1), a raw-stage run on the
          whole howls (the creature rise rule blocks them at final), an L1 run on every raw file.
link      critic AI steps into SOURCES.json, a batch-local release tree, licence-check on it.
context   context/: the in-game renders (dh-cast-chain for fire.cast and fire.impact.*, dh-beds for beds and
          horns) per listened candidate, with metrics; they become the board context "Trong trận thô".
session   board sessions "1-dh-s2" (battle) and "1-dh-s3" (beds, horns) in ~/AudioLab/review/dragon-hold/sessions
          (never overwritten without --force), cards revealed at the end, 4 anchors.
report    ~/AudioLab/work/_batch1/dragon-hold/<run>/REPORT.md and summary.json.

Heavy models run one at a time: the generate step and the critic step each wait while another Stable Audio 3
or critic process runs on the machine. Nothing is written under games/**.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

from common import env

LAB = env.LAB
GAME = "dragon-hold"
SEED = 20261024

# id -> SA3 jobs (variants of the card, seeds, optional length; "tag" puts the length in the name)
JOBS: dict[str, list[dict]] = {
    "fire.cast": [{"variants": ["A", "B", "C", "D"], "seeds": "2001-2006"}],
    "fire.impact.a": [{"variants": ["B"], "seeds": "2001-2024"}],
    "fire.impact.b": [{"variants": ["C", "E"], "seeds": "2001-2006"}],
    "fire.impact.c": [{"variants": ["A", "B"], "seeds": "2001-2006"}],
    "enemy.quadruped.howl": [{"variants": ["B"], "seeds": "2001-2006", "seconds": 2.0, "tag": True},
                             {"variants": ["B"], "seeds": "2001-2006", "seconds": 3.0, "tag": True}],
    "trap.pine-bomb.trigger": [{"variants": ["A", "B"], "seeds": "2001-2006"}],
    "general.g01.horn": [{"variants": ["A", "B"], "seeds": "2001-2006", "seconds": 3.0}],
    "amb.forest": [{"variants": ["E", "F"], "seeds": "3001-3003"}],
    "amb.river": [{"variants": ["A", "B", "C", "D"], "seeds": "2001-2006"}],
    "enemy.swarm.march": [{"variants": ["A", "B", "C", "D"], "seeds": "2001-2006"}],
    "enemy.quadruped.march": [{"variants": ["A", "B", "C", "D"], "seeds": "2001-2006"}],
}
P2 = ["fire.cast", "fire.impact.a", "fire.impact.b", "fire.impact.c", "enemy.quadruped.howl", "trap.pine-bomb.trigger"]
P3 = ["amb.forest", "amb.river", "enemy.swarm.march", "enemy.quadruped.march", "wave.horn", "general.g01.horn"]
IDS = P2 + P3
LOOPS = {"amb.forest", "amb.river", "enemy.swarm.march", "enemy.quadruped.march"}
# earlier raw takes processed again with this batch's chain (only takes named after the same id)
OLD_RAW = {
    "fire.impact.a": ["sa3-trial"],          # B family: the recipe's bodies, and raw takes as candidates
    "enemy.quadruped.howl": ["sa3-trial"],   # B s1001-1006 (the owner's 3/5 call is B s1004)
    "amb.forest": ["sa3-r2"],                # E s2006 (4/5 in 0b) re-normalised with this chain
}
OLD_RAW_FILTER = {"fire.impact.a": ("__B__",), "enemy.quadruped.howl": ("__B__",), "amb.forest": ("__E__", "__F__")}


def _say(msg: str) -> None:
    print(f"[batch1-dh] {msg}", flush=True)


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


def recipe_path(sid: str) -> Path:
    return LAB / "build" / "recipes" / GAME / f"{sid}.b1.json"


def recipe_run(sid: str, run: str) -> Path:
    return env.WORK / GAME / sid / f"{run}-recipe"


# ---------------------------------------------------------------- one heavy model at a time

HEAVY = ("sa3_batch.py", "launch.py critic run", "launch.py critic agreement")


def heavy_running() -> list[str]:
    """Other processes holding a heavy model (Stable Audio 3 or the critic), never this one."""
    try:
        out = subprocess.run(["ps", "-axo", "pid=,command="], capture_output=True, text=True, timeout=10).stdout
    except (OSError, subprocess.SubprocessError):
        return []
    me = {os.getpid(), os.getppid()}
    hits = []
    for line in out.splitlines():
        pid, _, cmd = line.strip().partition(" ")
        if not pid.isdigit() or int(pid) in me or "grep" in cmd:
            continue
        exe = Path(cmd.split(" ", 1)[0]).name
        if not exe.startswith("python"):          # shells that only mention a command are not models
            continue
        if any(h in cmd for h in HEAVY) or ("launch.py common.batch" in cmd and cmd.rstrip().split(" ")[-1] in ("critic", "all")):
            hits.append(f"{pid} {cmd[:120]}")
    return hits


def wait_heavy_free(what: str, max_wait_s: float = 3600.0) -> None:
    t0 = time.time()
    while True:
        hits = heavy_running()
        if not hits:
            return
        if time.time() - t0 > max_wait_s:
            raise RuntimeError(f"{what}: một mô hình nặng khác vẫn chạy sau {max_wait_s:.0f} s: {hits[0]}")
        _say(f"{what}: chờ tiến trình nặng khác xong ({hits[0]})")
        time.sleep(20)


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
        res = process.process_many(records(sid, run), card, id_dir(sid, run) / "processed",
                                   notch=sid in LOOPS, force=force)
        _say(f"process {sid}: {res['kept']} giữ, {len(res['rejected'])} loại, {res['skipped']} đã có")
        for r in res["rejected"]:
            _say(f"  loại {r['candidate']}: {r['reason']}")


# ---------------------------------------------------------------- step 3: fire bodies for the recipes

# pool -> (raw dirs of the takes, name filter, window length s)
BODY_POOLS = {
    "a": (["fire.impact.a/sa3-trial/raw", "fire.impact.a/{run}/raw"], "__B__", 0.33),     # 'rounded low thump ...'
    "b": (["fire.impact.a/sa3-trial/raw", "fire.impact.b/{run}/raw"], ("__C__", "__E__"), 0.37),   # warm deep burst
}
BODY_LEAD_S = 0.004          # 0b recipe: the body window opens 4 ms before its 5 ms level peak


def body_window(f32: Path, length_s: float) -> dict:
    """Window of a body take from 4 ms before its loudest 5 ms, with the checks that keep one onset."""
    import soundfile as sf
    from critic import features as F
    from critic.thresholds import L1B

    x, sr = sf.read(str(f32), always_2d=True, dtype="float64")
    m = x.mean(axis=1)
    hop, win = int(0.001 * sr), int(0.005 * sr)
    c = np.concatenate([[0.0], np.cumsum(m ** 2)])
    starts = np.arange(0, max(1, m.size - win), hop)
    e = 10 * np.log10((c[starts + win] - c[starts]) / win + 1e-12)
    k = int(np.argmax(e))
    t_pk = starts[k] / sr
    a = max(0.0, t_pk - BODY_LEAD_S)
    b = min(m.size / sr, a + length_s)
    seg = m[int(a * sr):int(b * sr)]
    # what sounds just before the window (a cut into a sound would click or smear the front layer)
    pre = m[max(0, int((a - 0.02) * sr)):int(a * sr)]
    pre_db = 10 * np.log10(np.mean(pre ** 2) + 1e-12) - float(e[k]) if pre.size else -120.0
    ro = F.hf_reonset(seg, sr)
    dbl = (ro["hf_reonset_db"] is not None and ro["hf_reonset_db"] >= L1B["double_onset_db"]
           and (ro["hf_reonset_rise_db"] or 0) >= L1B["double_onset_rise_db"]
           and (ro["hf_reonset_dip_db"] or 0) <= L1B["double_onset_dip_db"])
    from build import sources
    w = [round(a, 4), round(b, 4)]
    clip = not sources.clip_scan_file(f32, w)["ok"]       # the render's own clip gate (float copies: equal samples)
    # pre_db: the 20 ms before the window, re the body peak. The 0b bodies (3/5) opened about 9 dB under it,
    # on the swell of the model's soft pre-hit; the front layer covers that, so only a louder sound is refused.
    return {"file": str(f32), "window": w, "peak_s": round(t_pk, 4), "peak_db": round(float(e[k]), 1),
            "pre_db": round(pre_db, 1), "double_onset": bool(dbl), "clip": clip, **ro,
            "ok": bool(not dbl and not clip and pre_db <= -3.0 and t_pk <= 0.7)}


def step_bodies(run: str, force: bool = False) -> dict:
    out = base_dir(run) / "bodies.json"
    if out.is_file() and not force:
        _say(f"bodies: đã có {out}")
        return json.loads(out.read_text("utf-8"))
    pools: dict = {}
    for key, (dirs, filt, length) in BODY_POOLS.items():
        filt = (filt,) if isinstance(filt, str) else filt
        rows = []
        for d in dirs:
            for f in sorted((env.WORK / GAME / d.format(run=run)).glob("*.f32.wav")):
                if any(t in f.name for t in filt):
                    r = body_window(f, length)
                    r["record"] = str(f.with_name(f.name.replace(".f32.wav", ".json")))
                    rows.append(r)
        ok = sorted([r for r in rows if r["ok"]], key=lambda r: -r["peak_db"])
        pools[key] = {"length_s": length, "n": len(rows), "ok": len(ok), "bodies": ok,
                      "rejected": [{k: r[k] for k in ("file", "double_onset", "clip", "pre_db", "peak_s")} for r in rows if not r["ok"]]}
        _say(f"bodies {key}: {len(ok)}/{len(rows)} thân dùng được (một đầu tiếng, không cắt vào âm trước, không clip)")
    # flare layer of fire.impact.c: the processed takes (true onset, natural window)
    flares = []
    for p in sorted((id_dir("fire.impact.c", run) / "processed").glob("*.proc.json")):
        d = json.loads(p.read_text("utf-8"))
        if d.get("onset_verified", True) is False:
            continue
        flares.append({"file": d["source_f32"], "record": d["raw_record"], "window": d["window_raw_s"],
                       "len_ms": d["window"]["len_ms"]})
    pools["flare"] = {"n": len(flares), "bodies": flares}
    # wooden texture of general.g01.horn: the processed A takes
    tex = []
    for p in sorted((id_dir("general.g01.horn", run) / "processed").glob("*.proc.json")):
        d = json.loads(p.read_text("utf-8"))
        tex.append({"file": d["source_f32"], "record": d["raw_record"], "window": d["window_raw_s"],
                    "len_ms": d["window"]["len_ms"]})
    pools["texture"] = {"n": len(tex), "bodies": tex}
    out.write_text(json.dumps(pools, indent=1, ensure_ascii=False, default=float), "utf-8")
    return pools


# ---------------------------------------------------------------- step 4: recipes

def gen_src(b: dict) -> dict:
    from gen import sa3
    rec = sa3.read_record(b["record"])
    return {"gen": {"tool": "stable-audio-3 (sa3_batch.py)", "model": rec["model"]["id"] if "id" in rec.get("model", {})
                    else f"{rec['model']['repo']}@{rec['model']['revision']}",
                    "licence": "LicenseRef-Stability-Community-2024", "file": b["file"], "record": b["record"],
                    "window": [float(v) for v in b["window"]]}}


def lib(name: str) -> dict:
    return {"library": f"kenney/impact-sounds/Audio/{name}.ogg"}


def _cycle(layer: dict, sources: list[dict]) -> dict:
    layer["source"] = sources[0]
    if len(sources) > 1:
        layer.setdefault("vary", {}).update({"swapMode": "cycle", "swap": sources[1:]})
    return layer


EMBERS = [{"id": "ember1", "role": "sweetener", "source": {"synth": "click", "params": {"durMs": 3, "hpHz": 3200, "lpHz": 9000}},
           "offsetMs": 90, "gainDb": -24, "vary": {"offsetMs": [-20, 25]}},
          {"id": "ember2", "role": "sweetener", "source": {"synth": "click", "params": {"durMs": 2, "hpHz": 3800, "lpHz": 10000}},
           "offsetMs": 190, "gainDb": -27, "vary": {"offsetMs": [-25, 30]}}]


def _recipe(sid: str, group: str, family: str, desc: str, layers: list[dict], chain: dict, count: int, seed: int,
            export: str, pitch=(-20, 20), gain=(-0.5, 0.5)) -> dict:
    return {"$schema": "../../schemas/recipe.schema.json", "schema": "audiolab.recipe/1", "game": GAME, "id": sid,
            "group": group, "family": family, "description": desc, "channels": 1, "layers": layers, "chain": chain,
            "variants": {"count": count, "seed": seed, "includeBase": True, "pitchCents": list(pitch), "gainDb": list(gain)},
            "export": {"path": export, "ogg": True, "oggQuality": 0.6}}


def recipes_from(pools: dict) -> dict[str, dict]:
    A = pools["a"]["bodies"][:12]
    B = pools["b"]["bodies"][:6]
    FL = pools["flare"]["bodies"]
    TX = pools["texture"]["bodies"][:3]
    out = {}
    # the two fronts of the 0b takes rated 3/5 (generic light 002, 000) first, then the brighter ones the brief asks
    # for; 12 takes because the critic refuses a front and a body whose high bands land 12-40 ms apart (double_onset)
    fronts_a = ["impactGeneric_light_002", "impactWood_heavy_003", "impactGeneric_light_000", "impactSoft_heavy_001",
                "impactWood_heavy_004", "impactSoft_heavy_003", "impactGeneric_light_004", "impactWood_heavy_001",
                "impactGeneric_light_002", "impactSoft_heavy_000", "impactGeneric_light_000", "impactWood_heavy_000"]
    n = min(12, len(A))
    out["fire.impact.a"] = _recipe(
        "fire.impact.a", "hit-heavy", "trung",
        "Lô 1 (BATCH1_BRIEF #2): mẫu của họ cầu lửa, từ công thức 0b (anh chấm 3/5 cả v4 và v2). Đầu tiếng Kenney "
        "(generic light như hai bản 3/5, thêm gỗ nặng và 'soft heavy' để thử hướng sáng hơn), thân lửa Stable Audio 3 "
        "họ B (24 thân mới + 6 cũ; chỉ giữ thân một đầu tiếng, cửa sổ từ 4 ms trước đỉnh 5 ms, 330 ms), lọc cao 130 Hz "
        "bậc 4, sub rút còn 90 ms và nhỏ đi 3 dB (anh chấm bản ít sub cao hơn: 0a v3 55 % dưới 150 Hz thắng bản 84 %), "
        "hai tiếng than hồng. Biến thể n dùng đầu tiếng n và thân n.",
        [_cycle({"id": "front", "role": "attack", "gainDb": -2, "filters": [{"type": "highpass", "hz": 140}],
                 "trim": {"endMs": 90}, "fadeOutMs": 50}, [lib(f) for f in fronts_a[:n]]),
         _cycle({"id": "body", "role": "body", "gainDb": -2, "fadeInMs": 3, "fadeOutMs": 120,
                 "filters": [{"type": "highpass", "hz": 130, "order": 4}]}, [gen_src(b) for b in A[:n]]),
         {"id": "sub", "role": "sub", "source": {"synth": "sub_thump", "params": {"startHz": 80, "endHz": 45, "glideMs": 50,
                                                                                    "durMs": 90, "decayMs": 70}}, "gainDb": -8},
         *json.loads(json.dumps(EMBERS))],
        {"dcHpfHz": 35, "filters": [{"type": "lowpass", "hz": 9000, "order": 2}], "saturation": {"driveDb": 2, "mix": 0.25},
         "headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": 400,
         "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 150}, "normalise": {"mode": "lufs-m-max", "target": -20},
         "limiter": {"ceilingDbtp": -1.0, "releaseMs": 60, "maxGrDb": 6}},
        n, 2410, "sfx/dragon/fire-impact-a")
    nb = min(6, len(B))
    out["fire.impact.b"] = _recipe(
        "fire.impact.b", "hit-heavy", "trung",
        "Lô 1 (BATCH1_BRIEF #3): cùng họ với fire.impact.a, tối hơn, có lách tách. Giữ đầu tiếng generic light của hai bản "
        "0b được 3/5, thân đổi sang Stable Audio 3 prompt C ('warm deep flame burst, crackling embers') và E (tối hơn), "
        "hạ thân 1 bán cung, lọc thấp 6,5 kHz, bốn tiếng than hồng, sub 85 ms. Biến thể n dùng thân n.",
        [_cycle({"id": "front", "role": "attack", "gainDb": -3, "filters": [{"type": "highpass", "hz": 140}],
                 "trim": {"endMs": 80}, "fadeOutMs": 50},
                [lib("impactGeneric_light_002"), lib("impactGeneric_light_000")] * 3),
         _cycle({"id": "body", "role": "body", "gainDb": -1, "fadeInMs": 3, "fadeOutMs": 140, "pitchSemitones": -1,
                 "filters": [{"type": "highpass", "hz": 120, "order": 4}]}, [gen_src(b) for b in B[:nb]]),
         {"id": "sub", "role": "sub", "source": {"synth": "sub_thump", "params": {"startHz": 75, "endHz": 42, "glideMs": 50,
                                                                                    "durMs": 85, "decayMs": 65}}, "gainDb": -9},
         *json.loads(json.dumps(EMBERS)),
         {"id": "ember3", "role": "sweetener", "source": {"synth": "click", "params": {"durMs": 2, "hpHz": 3000, "lpHz": 8000}},
          "offsetMs": 260, "gainDb": -28, "vary": {"offsetMs": [-30, 30]}},
         {"id": "ember4", "role": "sweetener", "source": {"synth": "click", "params": {"durMs": 3, "hpHz": 2600, "lpHz": 7000}},
          "offsetMs": 330, "gainDb": -30, "vary": {"offsetMs": [-30, 20]}}],
        {"dcHpfHz": 35, "filters": [{"type": "lowpass", "hz": 6500, "order": 2}], "saturation": {"driveDb": 2, "mix": 0.25},
         "headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": 450,
         "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 170}, "normalise": {"mode": "lufs-m-max", "target": -20},
         "limiter": {"ceilingDbtp": -1.0, "releaseMs": 60, "maxGrDb": 6}},
        nb, 2411, "sfx/dragon/fire-impact-b")
    nc = min(10, len(FL), len(A))
    out["fire.impact.c"] = _recipe(
        "fire.impact.c", "blast", "trung",
        "Lô 1 (BATCH1_BRIEF #4): đòn to = công thức của fire.impact.a cộng tiếng bùng lửa Stable Audio 3 ('big fire burst, "
        "roaring flames', cửa sổ tự nhiên tới 624 ms; lọc thấp 1,8 kHz vì tiếng lách tách của chính nó tạo đầu tiếng thứ hai "
        "20–40 ms sau, nên bốn tiếng than hồng thay phần lách tách), sub 140 ms (≤ 150 ms). Biến thể n dùng đầu tiếng, thân, bùng lửa n.",
        [_cycle({"id": "front", "role": "attack", "gainDb": -1, "filters": [{"type": "highpass", "hz": 120}],
                 "trim": {"endMs": 100}, "fadeOutMs": 60},
                [lib(f) for f in ["impactWood_heavy_003", "impactGeneric_light_002", "impactWood_heavy_004",
                                  "impactGeneric_light_000", "impactSoft_heavy_001", "impactWood_heavy_001",
                                  "impactGeneric_light_004", "impactWood_heavy_000", "impactSoft_heavy_003",
                                  "impactGeneric_light_002"][:nc]]),
         _cycle({"id": "body", "role": "body", "gainDb": -3, "fadeInMs": 3, "fadeOutMs": 120,
                 "filters": [{"type": "highpass", "hz": 130, "order": 4}]}, [gen_src(b) for b in A[:nc]]),
         # the flare's own crackle peaked 20-40 ms after the front (9/10 takes flagged double_onset in the first
         # render): it keeps its roar under 1.8 kHz and comes in over 15 ms; the embers carry the crackle
         _cycle({"id": "flare", "role": "tail", "gainDb": -2, "offsetMs": 8, "fadeInMs": 15, "fadeOutMs": 160,
                 "filters": [{"type": "highpass", "hz": 150, "order": 2}, {"type": "lowpass", "hz": 1800, "order": 4}]},
                [gen_src(b) for b in FL[:nc]]),
         # embers inside the shortest flare (the first render put one at 420 +- 40 ms: 4/10 takes ended on a lone
         # click 40-90 dB over the silence before it, which the critic does not flag)
         {"id": "ember3", "role": "sweetener", "source": {"synth": "click", "params": {"durMs": 2, "hpHz": 3000, "lpHz": 8000}},
          "offsetMs": 230, "gainDb": -27, "vary": {"offsetMs": [-30, 30]}},
         {"id": "ember4", "role": "sweetener", "source": {"synth": "click", "params": {"durMs": 3, "hpHz": 2800, "lpHz": 7500}},
          "offsetMs": 300, "gainDb": -29, "vary": {"offsetMs": [-30, 30]}},
         {"id": "sub", "role": "sub", "source": {"synth": "sub_thump", "params": {"startHz": 80, "endHz": 40, "glideMs": 70,
                                                                                    "durMs": 140, "decayMs": 110}}, "gainDb": -6},
         *json.loads(json.dumps(EMBERS))],
        {"dcHpfHz": 35, "filters": [{"type": "lowpass", "hz": 10000, "order": 2}], "saturation": {"driveDb": 2, "mix": 0.25},
         "headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": 620,
         "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 260}, "normalise": {"mode": "lufs-m-max", "target": -20},
         "limiter": {"ceilingDbtp": -1.0, "releaseMs": 80, "maxGrDb": 6}},
        nc, 2412, "sfx/dragon/fire-impact-c")
    horn = [{"start": 0, "note": "D3", "dur": 2.0, "vel": 100, "instrument": "f-horn.sus", "choke": True},
            {"start": 0.04, "note": "A3", "dur": 1.96, "vel": 92, "instrument": "f-horn.sus", "choke": True},
            {"start": 0, "key": "hdruml-hit", "dur": 0.6, "vel": 115, "instrument": "frame-drum"}]
    two = [{"start": 0, "note": "D3", "dur": 0.34, "vel": 96, "instrument": "f-horn.sus", "choke": True},
           {"start": 0.03, "note": "A3", "dur": 0.31, "vel": 88, "instrument": "f-horn.sus", "choke": True},
           {"start": 0.52, "note": "D3", "dur": 1.5, "vel": 104, "instrument": "f-horn.sus", "choke": True},
           {"start": 0.55, "note": "A3", "dur": 1.47, "vel": 96, "instrument": "f-horn.sus", "choke": True},
           {"start": 0, "key": "hdruml-hit", "dur": 0.6, "vel": 112, "instrument": "frame-drum"}]
    dbl = [{"start": 0.16, "note": "D3", "dur": 1.9, "vel": 100, "instrument": "f-horn.sus", "choke": True},
           {"start": 0.2, "note": "A3", "dur": 1.86, "vel": 92, "instrument": "f-horn.sus", "choke": True},
           {"start": 0, "key": "hdruml-hit", "dur": 0.4, "vel": 104, "instrument": "frame-drum"},
           {"start": 0.16, "key": "hdruml-hit", "dur": 0.6, "vel": 118, "instrument": "frame-drum"}]
    out["wave.horn"] = {
        "$schema": "../../schemas/recipe.schema.json", "schema": "audiolab.recipe/1", "game": GAME, "id": "wave.horn",
        "group": "rare-fixed", "family": "nen",
        "description": "Lô 1 (BATCH1_BRIEF #5): anh chọn hai kèn co Rê–La (0a v1, 3/5), chê trombone. Ba ứng viên cùng hướng "
                       "kèn co, khác hình câu: 1) một hơi dài 2 s; 2) hai hơi (ngắn 0,34 s, dài 1,5 s); 3) một hơi có trống "
                       "đôi (nhịp lấy đà 160 ms). Vang rừng không nướng vào file: game gửi bus stingers 0,16 vào vang rừng "
                       "0,9 s (mixer.ts), bản dựng bối cảnh có vang đó.",
        "channels": 1,
        "layers": [{"id": "phrase", "role": "body", "source": {"sampler": {"notes": horn}}, "fadeOutMs": 300,
                    "vary": {"swapMode": "cycle", "swap": [{"sampler": {"notes": two}}, {"sampler": {"notes": dbl}}]}}],
        "chain": {"dcHpfHz": 35, "headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": 2600,
                  "tail": {"floorDb": -60, "fadeMs": 300}, "normalise": {"mode": "lufs-m-max", "target": -20},
                  "limiter": {"ceilingDbtp": -1.0, "releaseMs": 80, "maxGrDb": 6}},
        "variants": {"count": 3, "seed": 2413, "includeBase": True},
        "export": {"path": "sfx/stinger/wave-horn", "ogg": True, "oggQuality": 0.6}}
    soft = [{"start": 0, "note": "D2", "dur": 1.2, "vel": 40, "instrument": "f-horn.sus", "choke": True},
            {"start": 0.05, "note": "A2", "dur": 1.15, "vel": 36, "instrument": "f-horn.sus", "choke": True}]
    full = [{"start": 0, "note": "D2", "dur": 1.75, "vel": 112, "instrument": "f-horn.sus", "choke": True},
            {"start": 0.04, "note": "A2", "dur": 1.71, "vel": 104, "instrument": "f-horn.sus", "choke": True}]
    nt = max(1, len(TX))
    # the Stable Audio 3 horn takes stop their highs at once about 0.8 s in (a model artefact seen on the cards):
    # the texture only colours the swell and fades out before it
    tx_layer = ([_cycle({"id": "texture", "role": "sweetener", "gainDb": -9, "fadeInMs": 300, "fadeOutMs": 350,
                         "trim": {"endMs": 650},
                         "filters": [{"type": "highpass", "hz": 70}, {"type": "lowpass", "hz": 2000, "order": 4}]},
                        [gen_src(b) for b in TX])] if TX else [])
    out["general.g01.horn"] = {
        "$schema": "../../schemas/recipe.schema.json", "schema": "audiolab.recipe/1", "game": GAME, "id": "general.g01.horn",
        "group": "rare-fixed", "family": "nen",
        "description": "Lô 1 (BATCH1_BRIEF #6): tù và của tướng G01, trầm hơn wave.horn, mở dần, 'gỗ, rêu', đáng sợ. Kèn co "
                       "quãng thấp Rê2–La2 (không trombone: anh chấm trombone 1–2/5), chỉ quãng năm Rê–La (không Si, Si giáng; "
                       "câu hỏi 16 #8 còn mở): lớp nhẹ (velocity thấp) chuyển dần sang lớp to (vào từ 0,3 s, mở trong 0,7 s) "
                       "để có tiếng mở dần; kết cấu gỗ Stable Audio 3 ('low wooden war horn, mossy') nhỏ bên dưới; một tiếng "
                       "trống khung. Kết cấu chỉ tô phần mở dần (cắt ở 650 ms, lọc thấp 2 kHz): các bản Stable Audio 3 của tù và tắt "
                       "dải cao đột ngột quanh 0,8 s. Biến thể n dùng kết cấu n.",
        "channels": 1,
        "layers": [{"id": "soft", "role": "body", "source": {"sampler": {"notes": soft}}, "trim": {"endMs": 1100}, "fadeOutMs": 650},
                   {"id": "full", "role": "body", "source": {"sampler": {"notes": full}}, "offsetMs": 300, "fadeInMs": 700,
                    "fadeOutMs": 350},
                   *tx_layer,
                   {"id": "drum", "role": "attack", "source": {"sampler": {"instrument": "frame-drum", "notes": "0:hdruml-hit:0.6:96"}},
                    "gainDb": -6}],
        "chain": {"dcHpfHz": 35, "headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": 2500,
                  "tail": {"floorDb": -60, "fadeMs": 400}, "normalise": {"mode": "lufs-m-max", "target": -20},
                  "limiter": {"ceilingDbtp": -1.0, "releaseMs": 80, "maxGrDb": 6}},
        "variants": {"count": nt, "seed": 2414, "includeBase": True},
        "export": {"path": "sfx/general/g01-horn", "ogg": True, "oggQuality": 0.6}}
    return out


RECIPE_IDS = ("fire.impact.a", "fire.impact.b", "fire.impact.c", "wave.horn", "general.g01.horn")


def step_recipes(run: str, force: bool = False) -> None:
    from build import render

    pools = step_bodies(run)
    for sid, data in recipes_from(pools).items():
        p = recipe_path(sid)
        p.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", "utf-8")
        out = recipe_run(sid, run)
        if out.is_dir() and (out / "render.json").is_file() and not force:
            _say(f"recipe {sid}: đã có {out}")
            continue
        res = render.render(p, out=out, spec=card_path(sid))
        _say(f"recipe {sid}: {res.report['count']} biến thể, mức id {res.report['idLevel']} LUFS-M; "
             + ("; ".join(res.report["warnings"]) or "không cảnh báo"))


# ---------------------------------------------------------------- step 4b: amb.forest blend (BATCH1_BRIEF #7)

BLEND_H_DB = -7.0      # "E cộng 20 % lớp trầm kiểu H": H at 20 % of E's power (-7 dB), then -26 LUFS-I again


def step_blend(run: str, force: bool = False) -> Path | None:
    """E s2006 (4/5) plus the low H s2004 bed (3/5) under it: to hear on headphones whether a pure bright bed tires."""
    import soundfile as sf
    from build import chain, ledger

    e_name, h_name = "amb.forest__E__s2006.wav", "amb.forest__H__s2004.wav"
    e_dir, h_dir = id_dir("amb.forest", run) / "processed", env.WORK / GAME / "amb.forest" / "sa3-r2" / "processed"
    out_dir = id_dir("amb.forest", run) / "blend"
    name = "amb.forest__E2006+H2004.wav"
    if (out_dir / name).is_file() and not force:
        _say(f"blend: đã có {out_dir / name}")
        return out_dir / name
    e, sr = sf.read(str(e_dir / e_name), always_2d=True, dtype="float64")
    h, sr2 = sf.read(str(h_dir / h_name), always_2d=True, dtype="float64")
    if sr != sr2 or e.shape != h.shape:
        raise RuntimeError(f"blend: hai vòng khác dạng {e.shape} {h.shape}")
    from critic import features as F
    from gen import process
    # Two seamless loops sum to a seamless loop, but the L1 seam test compares the 50 ms on each side of the
    # joint: the first sum failed it. H is turned round its own loop (25 ms steps) until the sum passes.
    tried, shift = [], 0
    for k in range(0, h.shape[0], int(0.025 * sr)):
        y = e + np.roll(h, k, axis=0) * 10 ** (BLEND_H_DB / 20)
        y, rep = chain.run(y, sr, {"normalise": {"mode": "lufs-i", "target": -26},
                                   "limiter": {"ceilingDbtp": -1.0, "maxGrDb": 3.0}}, loop=True)
        seam = F.seam(y, sr)
        tried.append(k)
        if process.seam_ok(seam):
            shift = k
            break
    else:
        raise RuntimeError("blend: không có vị trí nào của H cho mối nối đạt")
    out_dir.mkdir(parents=True, exist_ok=True)
    sf.write(str(out_dir / name), y.astype(np.float32), sr, subtype="PCM_24")
    se, sh = ledger.read_sources(e_dir / "SOURCES.json")[e_name], ledger.read_sources(h_dir / "SOURCES.json")[h_name]
    le = dict(se["layers"][0], id="bright", role="whole", gainDb=0.0)
    lh = dict(sh["layers"][0], id="low", role="body", gainDb=BLEND_H_DB)
    sha = ledger.sha256_file(out_dir / name)
    rec = {**se, "variant": 1, "renderVariant": 1, "sha256": sha, "masterSha256": sha, "master": name, "run": run,
           "date": ledger.today(), "layers": [le, lh],
           "chain": f"{e_name} + {h_name} at {BLEND_H_DB:g} dB turned {shift / sr * 1000:.0f} ms round its loop (both "
                    "seamless 6 s loops; seam checked), " + rep["summary"] + ", PCM 24-bit",
           "rawQa": "blend of two processed loops; layers[].rawQa hold the float clip tests"}
    data = {}
    data[name] = rec
    ledger.write_sources(out_dir / "SOURCES.json", data)
    rows = [json.loads(l) for l in (e_dir / "licences.rows.jsonl").read_text("utf-8").splitlines() if l.strip()]
    ledger.append_rows(out_dir / "licences.rows.jsonl", rows)
    _say(f"blend: {out_dir / name} ({rep['summary']})")
    return out_dir / name


# ---------------------------------------------------------------- step 5: critic

# already rated takes put next to the new ones (the owner hears them again blind: a consistency check)
TRAP_0A_V3 = env.WORK / GAME / "trap.pine-bomb.trigger" / "batch0-2026-10-23-r2"


def critic_out(run: str, name: str) -> Path:
    return base_dir(run) / f"critic-{name}"


def finals(run: str) -> tuple[list[Path], list[Path]]:
    """(folders or files with this batch's finals, their SOURCES.json)."""
    dirs, srcs = [], []
    for sid in JOBS:
        p = id_dir(sid, run) / "processed"
        if p.is_dir():
            dirs.append(p)
            srcs.append(p / "SOURCES.json")
    for sid in RECIPE_IDS:
        r = recipe_run(sid, run)
        dirs.append(r / "masters")
        srcs.append(r / "SOURCES.json")
    dirs.append(TRAP_0A_V3 / "masters" / "trap.pine-bomb.trigger-v3.wav")
    srcs.append(TRAP_0A_V3 / "SOURCES.json")
    return dirs, srcs


def step_critic(run: str, force: bool = False) -> None:
    from critic.__main__ import main as critic

    out = critic_out(run, "final")
    if (out / "_batch.json").is_file() and not force:
        _say(f"critic: đã có {out}")
        return
    dirs, srcs = finals(run)
    wait_heavy_free("critic")
    argv = ["run", *map(str, dirs), "--spec", str(LAB / "specs" / GAME), "--stage", "final", "--layers", "all",
            "--out", str(out), "--seed", str(SEED), "--blind-cards", "--quiet"]
    for s_ in srcs:
        argv += ["--sources", str(s_)]
    t0 = time.time()
    _say(f"critic final ({len(dirs)} mục): mã {critic(argv)}, {time.time() - t0:.0f} s")
    howl = id_dir("enemy.quadruped.howl", run) / "processed"
    argv = ["run", str(howl), "--spec", str(card_path("enemy.quadruped.howl")), "--stage", "raw", "--layers", "all",
            "--out", str(critic_out(run, "howl-info")), "--seed", str(SEED), "--sources", str(howl / "SOURCES.json"),
            "--blind-cards", "--quiet"]
    _say(f"critic howl (giai đoạn raw: L3–L5 cho tiếng gọi trọn mà luật lên 30 ms chặn): mã {critic(argv)}")
    blend = id_dir("amb.forest", run) / "blend"
    if blend.is_dir():
        # a deliberate candidate of the brief (#7), not ranked against the takes: its own run
        argv = ["run", str(blend), "--spec", str(card_path("amb.forest")), "--stage", "final", "--layers", "all",
                "--out", str(critic_out(run, "extra")), "--seed", str(SEED), "--sources", str(blend / "SOURCES.json"),
                "--blind-cards", "--quiet"]
        _say(f"critic blend amb.forest: mã {critic(argv)}")
    raws = [str(d) for sid in JOBS for d in raw_dirs(sid, run) if d.parent.name == run]
    argv = ["run", *raws, "--spec", str(LAB / "specs" / GAME), "--stage", "raw", "--layers", "L1,L1b",
            "--out", str(critic_out(run, "raw")), "--quiet"]
    _say(f"critic raw L1 (clip đọc bản float): mã {critic(argv)}")


# ---------------------------------------------------------------- step 5b: ledger + release check

def staging_dirs(run: str) -> tuple[Path, Path]:
    """Batch-local release tree. Not ~/AudioLab/review/staging: nothing here is owner-approved yet."""
    root = base_dir(run) / "staging" / GAME
    return root / "art-src" / "audio", root / "public" / "assets" / GAME / "audio"


def step_link(run: str, force: bool = False) -> int:
    from build import critic_link, licence_check, release

    outs = [critic_out(run, n) for n in ("final", "howl-info", "extra") if critic_out(run, n).is_dir()]
    folders = [id_dir(sid, run) / "processed" for sid in JOBS] + [id_dir("amb.forest", run) / "blend"]
    for p in folders:
        if (p / "SOURCES.json").is_file():
            res = critic_link.apply(p / "SOURCES.json", outs, p / "licences.rows.jsonl")
            _say(f"mark-ai {p.parent.parent.name}/{p.name}: {res['steps']} bước, {res['files']} hồ sơ")
    art, pub = staging_dirs(run)
    for sid in RECIPE_IDS:
        r = recipe_run(sid, run)
        res = critic_link.apply(r / "SOURCES.json", outs, r / "licences.rows.jsonl")
        rel = release.release(r, None, art, pub)
        _say(f"mark-ai {sid} (công thức): {res['steps']} bước; cây thử: {len(rel['files'])} file, {rel['rowsAdded']} dòng sổ, "
             f"{len(rel['licenceCopies'])} bản giấy phép")
    rc = licence_check.main(["--art-src", str(art), "--public", str(pub)])
    _say(f"licence-check (cây thử, chỉ công thức) {GAME}: mã {rc}")
    return rc


# ---------------------------------------------------------------- step 6: listening lists (plan §4.6 step 2)

NO_PICK_FLAGS = {"double_onset", "lr_imbalance"}           # batch 0b review 2: never offered
BED_NO_PICK = {"loop_signature", "decoder_comb", "stereo_mismatch"}
PROBE_IDS = ("fire.cast", "fire.impact.a", "amb.river", "enemy.quadruped.march")    # 4/12 ids, about 30 %
CAST_DIRECTIONS = {"tron": ("A", "C"), "hoi-tho": ("B", "D")}    # fire.cast: round puff / breathy spit (§9 step 2)
REF_0B = {
    "fire.impact.a": env.WORK / GAME / "fire.impact.a" / "sa3-r2-recipe" / "masters" / "fire.impact.a-v4.wav",   # 77e0dd55, 3/5
    "amb.forest": env.WORK / GAME / "amb.forest" / "sa3-r2" / "processed" / "amb.forest__E__s2006.wav",           # 10c80671, 4/5
    "wave.horn": env.WORK / GAME / "wave.horn" / "batch0-2026-10-23-r2" / "masters" / "wave.horn-v1.wav",         # d6e963bf, 3/5
}


def _docs(out: Path) -> dict[str, dict]:
    docs = {}
    if not out.is_dir():
        return docs
    for p in sorted(out.glob("*.json")):
        if p.name.startswith("_"):
            continue
        d = json.loads(p.read_text("utf-8"))
        docs[d["file"]["stem"]] = d
    return docs


def _sid(d: dict) -> str:
    return (d.get("spec") or {}).get("id") or ""


def _rank(d: dict) -> float:
    return (d.get("score") or {}).get("rank") or 1e9


def _flags(d: dict) -> set[str]:
    return {f["id"] for f in d.get("flags") or []}


def _proc(d: dict) -> dict:
    p = Path(d["file"]["path"]).with_suffix(".proc.json")
    try:
        return json.loads(p.read_text("utf-8"))
    except (OSError, ValueError):
        return {}


def _verified(d: dict) -> bool:
    return _proc(d).get("onset_verified", True) is not False


def _kind(d: dict) -> str:
    """recipe | sa3 | ref (a take rated in an earlier batch)."""
    path = d["file"]["path"]
    if "/batch0-" in path or "/sa3-r2" in path:
        return "ref"
    return "recipe" if "-recipe/" in path else "sa3"


def _prompt(d: dict) -> str:
    parts = d["file"]["stem"].split("__")
    return parts[1][:1] if len(parts) >= 3 else ""


def _distinct(top: dict, pool: list[dict]) -> dict | None:
    from critic import score
    if not pool:
        return None
    V = np.stack([score._vec(d) for d in [top, *pool]])
    sd = V.std(axis=0)
    sd[sd == 0] = 1.0
    return pool[int(np.argmax(np.linalg.norm((V[1:] - V[0]) / sd, axis=1)))]


def _upper(order: list[dict]) -> list[dict]:
    return order[1:max(2, (len(order) + 1) // 2)]


def _probe(sid: str, order: list[dict], used: set[str]) -> dict | None:
    pool = [d for d in order[max(1, len(order) // 2):] if d["file"]["stem"] not in used]
    if not pool:
        return None
    rng = random.Random(int(hashlib.sha256(f"batch-1-dh:{sid}".encode()).hexdigest()[:8], 16))
    return rng.choice(sorted(pool, key=lambda d: d["file"]["stem"]))


def select(run: str) -> dict[str, dict]:
    """Per id: the listening list (top, most different in the machine's upper half, probes at ~30 % of ids)."""
    docs = _docs(critic_out(run, "final"))
    info = _docs(critic_out(run, "howl-info"))
    extra = _docs(critic_out(run, "extra"))
    sel: dict[str, dict] = {}
    for sid in IDS:
        mine = [d for d in docs.values() if _sid(d) == sid]
        ok = sorted([d for d in mine if d["verdict"] == "PASS"], key=_rank)
        e: dict = {"n": len(mine), "pass": len(ok), "picks": []}
        e["pass_unverified_onset"] = sum(1 for d in ok if not _verified(d))
        e["pass_no_pick_flags"] = sum(1 for d in ok if _flags(d) & NO_PICK_FLAGS)
        ok = [d for d in ok if _verified(d) and not _flags(d) & NO_PICK_FLAGS]
        if sid in LOOPS:
            stereo = [d for d in ok if "near_mono" not in _flags(d)]
            clean = [d for d in stereo if not _flags(d) & BED_NO_PICK]
            e.update({"stereo_pass": len(stereo), "clean_pass": len(clean)})
            ok = clean or stereo or ok
        e["eligible"] = len(ok)
        picks: list[tuple[dict, str, str | None]] = []
        if sid == "enemy.quadruped.howl":
            # whole calls: the creature rise rule (<= 30 ms) blocks them at final (Q3: 150 ms after §4.3.1 changes)
            blocked = [d for d in mine if d["verdict"] == "BLOCK" and set(d["L1"]["blocking"]) <= {"attack", "duration"}
                       and _verified(d)]
            fb = {d["file"]["stem"]: d["L1"]["blocking"] for d in blocked}
            ranked = sorted([info[s_] for s_ in fb if s_ in info], key=_rank)
            swell = [d for d in ranked if fb[d["file"]["stem"]] == ["attack"]
                     and ((d.get("metrics") or {}).get("attack_ms") or 1e9) <= 150]
            pool = swell if len(swell) >= 2 else ranked
            heard = [d for d in pool if "ast_expected_missing" not in _flags(d) and "ast_forbidden" not in _flags(d)]
            pool = heard if len(heard) >= 2 else pool
            e.update({"blocked_whole": len(blocked), "swell_le_150ms": len(swell), "heard_as_howl": len(heard)})

            def note(d):
                return "Bị luật chặn: tiếng tru lớn dần chậm (> 30 ms)" + ("; dài hơn thẻ" if "duration" in fb[d["file"]["stem"]] else "")
            if ok:
                picks.append((ok[0], "top", None))
            if pool:
                picks.append((pool[0], "rule-blocked-top", note(pool[0])))
                two = _distinct(pool[0], _upper(pool))
                if two is not None:
                    picks.append((two, "rule-blocked-distinct", note(two)))
                pr = _probe(sid, pool, {d["file"]["stem"] for d, _, _ in picks})
                if pr is not None and len(picks) < 3:
                    picks.append((pr, "rule-blocked-probe", note(pr)))
            ref = [info.get(d["file"]["stem"]) for d in blocked if d["file"]["stem"].endswith("__B__s1004")]
            if ref and ref[0] is not None and ref[0]["file"]["stem"] not in {d["file"]["stem"] for d, _, _ in picks}:
                picks.append((ref[0], "rule-blocked-ref-0b", note(ref[0])))
            e["picks"] = picks
            sel[sid] = e
            continue
        if not ok:
            sel[sid] = e
            continue
        top = ok[0]
        picks.append((top, "top", None))
        if sid == "fire.cast":
            # two directions side by side (§9 step 2): the best take of the other prompt family
            mine_dir = next(k for k, v in CAST_DIRECTIONS.items() if _prompt(top) in v)
            other = [d for d in ok if _prompt(d) not in CAST_DIRECTIONS[mine_dir]]
            if other:
                picks.append((other[0], "direction-2", None))
        elif sid == "trap.pine-bomb.trigger":
            new = [d for d in ok if _kind(d) == "sa3"]
            ref = [d for d in mine if _kind(d) == "ref"]
            picks = [(new[0], "top", None)] if new else []
            if len(new) > 1:
                dis = _distinct(new[0], _upper(new))
                if dis is not None:
                    picks.append((dis, "distinct", None))
            if ref:
                picks.append((ref[0], "ref-0a", None))
        elif sid == "general.g01.horn":
            # the machine's top, then the best of the other source (sampler recipe vs. Stable Audio 3 whole take)
            rec = [d for d in ok if _kind(d) == "recipe"]
            raw = [d for d in ok if _kind(d) == "sa3"]
            other = rec if _kind(top) == "sa3" else raw
            if other:
                picks.append((other[0], "recipe-best" if other is rec else "sa3-best", None))
                dis = _distinct(other[0], other[1:])
                if dis is not None:
                    picks.append((dis, "recipe-distinct" if other is rec else "sa3-distinct", None))
        elif sid == "amb.forest":
            # brief #7: the 4/5 bed again (E s2006, same file), two new E/F seeds, E with 20 % of the low H bed
            new = [d for d in ok if "__s300" in d["file"]["stem"]]
            ref = [d for d in mine if d["file"]["stem"].endswith("E__s2006")]
            picks = [(new[0], "top", None)] if new else [(top, "top", None)]
            seen = {picks[0][0]["file"]["stem"]} | {d["file"]["stem"] for d in ref}
            dis = _distinct(picks[0][0], [d for d in new if d["file"]["stem"] not in seen]
                            or [d for d in ok if d["file"]["stem"] not in seen])
            if dis is not None:
                picks.append((dis, "distinct", None))
            if ref:
                picks.append((ref[0], "ref-0b", None))
            bl = [d for d in extra.values() if _sid(d) == sid and d["verdict"] == "PASS"]
            if bl:
                picks.append((bl[0], "blend-h20", None))
        elif sid == "wave.horn":
            picks = [(d, r, None) for d, r in zip(ok, ("top", "distinct", "other"))]
        else:
            dis = _distinct(top, _upper(ok))
            if dis is not None:
                picks.append((dis, "distinct", None))
        if sid in ("enemy.swarm.march", "enemy.quadruped.march"):
            # the 10 s takes are passing herds, not steady crowds: the machine's top swings 24-26 dB inside its
            # 4 s loop. One more take by rule: the evenest loop (lowest LUFS-M range) not listed yet.
            used = {d["file"]["stem"] for d, _, _ in picks}
            even = sorted([d for d in ok if d["file"]["stem"] not in used],
                          key=lambda d: (d.get("metrics") or {}).get("lufs_m_range_db") or 99)
            if even:
                picks.append((even[0], "steady", None))
        if sid in PROBE_IDS:
            pr = _probe(sid, ok, {d["file"]["stem"] for d, _, _ in picks})
            if pr is not None:
                picks.append((pr, "probe", None))
        e["picks"] = picks
        sel[sid] = e
    return sel


# ---------------------------------------------------------------- step 7: in-game context renders

SCENARIO = {"fire.cast": "dh-cast-chain", "fire.impact.a": "dh-cast-chain", "fire.impact.b": "dh-cast-chain",
            "fire.impact.c": "dh-cast-chain", "enemy.quadruped.howl": "dh-pack", "trap.pine-bomb.trigger": "dh-trap",
            "amb.forest": "dh-beds", "amb.river": "dh-beds", "enemy.swarm.march": "dh-beds",
            "enemy.quadruped.march": "dh-beds", "wave.horn": "dh-beds", "general.g01.horn": "dh-beds"}


def fixed_slots(sel: dict) -> dict[str, Path]:
    """Every slot a render does not test: the take the owner rated highest when there is one, else this batch's top."""
    out = {}
    for sid in IDS:
        picks = sel.get(sid, {}).get("picks") or []
        if picks:
            out[sid] = Path(picks[0][0]["file"]["path"])
    for sid, p in REF_0B.items():
        if p.is_file():
            out[sid] = p
    return out


def ctx_dir(run: str) -> Path:
    return base_dir(run) / "context"


def step_context(run: str, force: bool = False) -> dict:
    from context import scenes

    sel = select(run)
    fixed = fixed_slots(sel)
    done: dict = {"fixed": {k: str(v) for k, v in fixed.items()}, "renders": {}}
    for sid in IDS:
        for d, role, _ in sel[sid]["picks"]:
            stem = d["file"]["stem"]
            out = ctx_dir(run) / sid / f"{stem}.wav"
            if out.is_file() and out.with_suffix(".json").is_file() and not force:
                doc = json.loads(out.with_suffix(".json").read_text("utf-8"))
            else:
                slots = dict(fixed)
                slots[sid] = Path(d["file"]["path"])
                doc = scenes.render(SCENARIO[sid], slots, out, focus=sid)
            done["renders"].setdefault(sid, {})[stem] = {"file": str(out), "role": role, "metrics": doc["metrics"]}
            _say(f"context {sid} {stem}: {SCENARIO[sid]}, giọng 1–4 kHz min {(doc['metrics'].get('voice') or {}).get('min_db')} dB")
    (ctx_dir(run) / "context.json").write_text(json.dumps(done, ensure_ascii=False, indent=1, default=float), "utf-8")
    return done


# ---------------------------------------------------------------- step 8: board sessions

DESC = {
    "fire.cast": "Hỏa Long khạc cầu lửa khi gõ xong từ (272–408 ms). Hai hướng đặt cạnh nhau: phụt lửa tròn, và khạc có "
                 "hơi thở. Nghe 'Trong trận thô' trước: giọng đọc từ phải rõ ngay sau tiếng khạc",
    "fire.impact.a": "Cầu lửa trúng, âm gốc của cả họ: phụt lửa trầm, thân tròn, lách tách nhỏ. 'Trong trận thô': cầu lửa "
                     "rơi 0,6 s sau mỗi từ, xen với biến thể tối (.b) và đòn to (.c)",
    "fire.impact.b": "Biến thể tối hơn của cầu lửa trúng, có lách tách khô. Phải nghe cùng họ với .a nhưng phân biệt được",
    "fire.impact.c": "Đòn to (bậc T3 trở lên, Hoàn hảo, Chớp): bùng lửa lớn, trầm, cháy tiếp, dài hơn .a rõ ràng, không có "
                     "tiếng nổ thứ hai",
    "enemy.quadruped.howl": "Thú bốn chân tru gọi bầy, trọn một tiếng tru (0,9–1,3 s), phát cách nhau 1,5 s. Bản có nhãn ghi "
                            "sẵn bị luật đầu tiếng sinh vật chặn; anh chấm như mọi bản. Nghe kỹ cuối tiếng tru: có tiếng rít cao không",
    "trap.pine-bomb.trigger": "Bom Hạt Thông nổ trầm, hạt văng (bẫy duy nhất nổ). Thử thêm 'Loa nhỏ'",
    "amb.forest": "Gió qua rừng thông, vòng 6 s. Nghe ít nhất 3 vòng ở 'Lặp' bằng tai nghe: có mệt tai không, có nhận ra chỗ "
                  "nối không? Thấy nhàm thì gắn 'nhàm khi lặp'",
    "amb.river": "Suối, vòng 5 s, chạy cùng nền rừng (trong game nhỏ hơn nền rừng khoảng 8 dB). Có tiếng gì có cao độ lặp lại không?",
    "enemy.swarm.march": "Bầy quái lạo xạo trên lá, vòng 4 s, mono, to theo số quái còn sống",
    "enemy.quadruped.march": "Vó thú chạy, vòng 4 s, mono. Nhịp phi có đều qua chỗ nối không, có tiếng vó đôi ở chỗ nối không?",
    "wave.horn": "Tù và báo đợt. Ba bản cùng hai kèn co Rê–La, khác hình câu: một hơi dài; hai hơi ngắn rồi dài; một hơi có "
                 "trống đôi lấy đà",
    "general.g01.horn": "Tù và của tướng G01: trầm hơn tù và báo đợt, mở dần, 'gỗ, rêu', đáng sợ. Một bản là âm Stable Audio 3 "
                        "nguyên khối để so",
}
CONTEXTS = {"fire.cast": ["scene", "loop", "alone", "small"], "fire.impact.a": ["scene", "loop", "alone", "small"],
            "fire.impact.b": ["scene", "loop", "alone", "small"], "fire.impact.c": ["scene", "loop", "alone", "small"],
            "enemy.quadruped.howl": ["scene", "alone", "loop"], "trap.pine-bomb.trigger": ["alone", "scene", "small"],
            "amb.forest": ["loop", "scene", "alone"], "amb.river": ["loop", "scene", "alone"],
            "enemy.swarm.march": ["loop", "scene", "alone"], "enemy.quadruped.march": ["loop", "scene", "alone"],
            "wave.horn": ["alone", "scene", "small"], "general.g01.horn": ["alone", "scene", "small"]}
SESSIONS = [("1-dh-s2", "Lô 1 · Rồng Giữ Ải · trận đánh (S2)", P2),
            ("1-dh-s3", "Lô 1 · Rồng Giữ Ải · nền và tù và (S3)", P3)]


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


def _out_of(d: dict, run: str) -> Path:
    stem = d["file"]["stem"]
    for name in ("final", "extra", "howl-info"):
        o = critic_out(run, name)
        if (o / f"{stem}.json").is_file() and json.loads((o / f"{stem}.json").read_text("utf-8"))["file"]["path"] == d["file"]["path"]:
            return o
    return critic_out(run, "final")


def step_session(run: str, force: bool = False) -> list[Path]:
    import yaml

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
                out = critic_out(run, "howl-info") if role.startswith("rule-blocked") else _out_of(d, run)
                cands.append(_cand(d, role, out, note, ctx))
            sp = picks[0][0].get("spec") or {}
            item = {"id": sid, "family": sp.get("family") or "", "group": sp.get("group") or "", "desc": DESC[sid],
                    "probe": any(r == "probe" for _, r, _ in picks), "contexts": CONTEXTS[sid], "candidates": cands}
            card = yaml.safe_load(card_path(sid).read_text("utf-8")) or {}
            rate = (card.get("critic") or {}).get("rate_hz")
            if sid in LOOPS:
                item["loop"] = {"seamless": True, "count": 3}
            elif rate:
                gap = (card.get("playback") or {}).get("min_gap_ms") or 0
                longest = max((d["metrics"].get("duration_ms") or 0) for d, _, _ in picks)
                iv = int(max(1000.0 / rate, gap, longest + 50))
                item["loop"] = {"interval_ms": iv, **({"count": 8} if iv >= 1000 else {})}
            elif sid == "enemy.quadruped.howl":
                item["loop"] = {"interval_ms": 1500, "count": 4}
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

def _fmt(v, nd=1):
    if v is None:
        return "–"
    if isinstance(v, float):
        return f"{v:.{nd}f}".replace(".", ",").replace("-", "−")
    return str(v)


def _pct(v):
    return "–" if v is None else f"{v * 100:.0f} %"


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
            "flags": sorted(_flags(d)),
            "metrics": {k: m.get(k) for k in ("duration_ms", "attack_ms", "crest_db", "share_below_150", "share_200_800",
                                               "share_1k_4k", "share_above_3k", "centroid_hz", "sub_len_ms", "tail_ms",
                                               "lufs_m_max", "lufs_m_range_db", "speaker_loss_db", "phone_loss_db", "stereo_correlation",
                                               "side_mid_db") if m.get(k) is not None}}


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
    summary = {"run": run, "counts": c, "n_files": b.get("n_files"), "ids": {}, "fixed_slots": ctx.get("fixed")}
    L = ["# Lô 1 · Rồng Giữ Ải (P2, P3)", "",
         "Tự sinh bởi `common/batch1_dh.py report`. Thẻ ảnh của bộ chấm: `critic-final/<tên>.png` (bản cho Bảng Nghe: "
         "`.blind.png`); bản dựng trong bối cảnh: `context/<id>/<tên>.wav|.png|.json`.", "",
         f"Lần chấm cuối: {b.get('n_files')} file, {c.get('PASS', 0)} ĐẠT, {c.get('BLOCK', 0)} CHẶN, "
         f"{c.get('NEEDS_FIX', 0)} CẦN SỬA; hiệu chỉnh `{(b.get('calibration') or {}).get('id') or (b.get('calibration') or {}).get('version') or 'owner-v1'}`.", "",
         "Không đưa vào phiên: bản có đầu tiếng chưa xác minh, cờ `double_onset` (hai đầu tiếng) hay `lr_imbalance`; nền có "
         "`loop_signature`, `decoder_comb`, `stereo_mismatch` hay `near_mono` (nếu còn bản khác).", ""]
    merged = sorted(p.name for p in critic_out(run, "final").glob("_merged-*.txt"))
    if merged:
        L += ["Chấm lại riêng sau khi sửa công thức (xếp hạng theo id nên các id khác không đổi): "
              + ", ".join(m[len("_merged-"):-4] for m in merged) + ".", ""]
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
        summary["ids"][sid] = {**{k: v for k, v in e.items() if k != "picks"}, "picks": rows,
                               "note": (obs.get(sid) or {}).get("_id")}
        L += [f"## `{sid}`", "", f"{e['n']} bản cuối, {e['pass']} qua L1, {e.get('eligible', 0)} được chọn vào danh sách nghe "
              f"(sau các luật không chọn).", ""]
        if (obs.get(sid) or {}).get("_id"):
            L += [obs[sid]["_id"], ""]
        L += ["| Vai trò | Bản | Mã | Loại | L1 | Hạng | Điểm | L2 | PQ | AST | Lên ms | Dài ms | <150 Hz | 200–800 Hz | Cờ | Bối cảnh |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r_ in rows:
            m = r_["metrics"]
            cm = r_.get("context") or {}
            vc = (cm.get("voice") or {}).get("min_db")
            ctxs = (f"giọng 1–4 kHz min {_fmt(vc)} dB, tệ nhất {_fmt((cm.get('voice_worst') or {}).get('min_db'))} dB; "
                    f"loa nhỏ {_fmt(cm.get('focus_small_speaker_loss_db'))} dB") if cm else "–"
            L.append(f"| {r_['role']} | `{r_['stem']}` | {r_['sha8']} | {r_['kind']} | {r_['verdict']} {','.join(r_['blocking'])} | "
                     f"{r_['rank'] or '–'}/{r_['n_ranked'] or '–'} | {_fmt(r_['combined'], 2)} | {_fmt(r_['L2'], 2)} | {_fmt(r_['PQ'], 2)} | "
                     f"{', '.join(f'{a} {s2}' for a, s2 in r_['ast']) or '–'} | {_fmt(m.get('attack_ms'))} | {_fmt(m.get('duration_ms'), 0)} | "
                     f"{_pct(m.get('share_below_150'))} | {_pct(m.get('share_200_800'))} | {', '.join(r_['flags']) or '–'} | {ctxs} |")
        notes = [f"- `{r_['stem']}`: {r_['observation']}" for r_ in rows if r_.get("observation")]
        if notes:
            L += ["", "Thẻ ảnh và bản dựng (Claude đọc):", *notes]
        L.append("")
    path = base_dir(run) / "REPORT.md"
    path.write_text("\n".join(L) + "\n", "utf-8")
    (base_dir(run) / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1, default=str), "utf-8")
    _say(f"báo cáo {path}")
    return path


# ---------------------------------------------------------------- CLI

STEPS = {"generate": step_generate, "process": step_process, "bodies": step_bodies, "recipes": step_recipes, "blend": step_blend,
         "critic": step_critic, "link": step_link, "context": step_context,
         "session": step_session, "report": step_report}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="batch1_dh", description="Lô 1 · Rồng Giữ Ải (P2, P3 của BATCH1_BRIEF.md).")
    ap.add_argument("step", choices=[*STEPS, "all"])
    ap.add_argument("--run", default="b1")
    ap.add_argument("--force", action="store_true", help="làm lại bước đã có; ghi đè file phiên")
    a = ap.parse_args(argv)
    env.apply()
    for name in (list(STEPS) if a.step == "all" else [a.step]):
        try:
            rc = STEPS[name](a.run, a.force)
        except SessionExists as exc:
            print(f"batch1_dh: {exc}", file=sys.stderr)
            return 1
        if isinstance(rc, int) and rc:
            return rc
    return 0


if __name__ == "__main__":
    sys.exit(main())
