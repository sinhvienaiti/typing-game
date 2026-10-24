"""Batch 1, Tuyến Cuối (typing-survival): steps P1 and P4 of BATCH1_BRIEF.md (§3, §4.1, §6, §7).

  run.sh common.batch1_ts all [--run b1] [--force]
  run.sh common.batch1_ts generate|process|bodies|recipes|critic|loops|kills|t2|load|breach|stage2|link|context|session|report

generate  Stable Audio 3 from the spec cards (prompt.variants), one job at a time, model resident per job:
          gun.xung E-H (bodies, 1 s), gun.xung.loop A-C (10 s), gun.xung.tail A-B (3 s), hit.t1 C/E, hit.t2 A-D,
          hit.t4 A-D, kill.swarm A-D, kill.elite A-D, word.load A-D, gun.tia.pulse A-B (texture), hurt.breach A-C.
process   gen/process.py on every raw take (true onsets, exponential tail, mono; loops: crossfade, seam check).
bodies    body windows for the recipes (one high-band onset, no cut into a sound before): gun bodies (4 checked
          0b bodies + new E-H), hit.t4 300 ms, hit.t2, kill.elite, hurt.breach, word.load, tia textures.
recipes   build/recipes/typing-survival/<id>.b1*.json: the gun family in three directions (BATCH1_BRIEF §3.4: A and B
          sets, loop, tail), hit.sub, hit.tail, hit.t2 and hit.t4 heard pre-mixed with their shared layers,
          kill.elite, word.load (Kenney), gun.tia.pulse, hurt.breach; rendered with build.render.
critic    one full critic run over every final (one model load, calibration owner-v1) and an L1 run on every raw file.
loops     the bed and ceasefire candidates in one critic run: model beds, library bed, two split beds (hum under 600 Hz
          plus a quiet clatter at 3-8 kHz, or at 5.5-9 kHz without the pitched chirps), tails.
kills     kill.swarm direction 'shatter with a short ring': Kenney Impact head on the C/D model bodies (their own onset is
          not verified), scored in one critic run with every kill.swarm take.
t2        hit.t2.kb2: the Kenney head on peak-aligned model bodies (the process.py windows of hit.t2.kb left a second
          clank 32-62 ms after the head), scored in one run with hit.t2.raw, hit.t2.kb and 0a v2.
load      word.load.kn2: the Kenney click and latch trimmed to their own hits (word.load.kn kept their lead-in, its main
          hit ~95 ms late), scored in one run with every word.load take and word.load.kn.
breach    hurt.breach.b2: a steel hit and a sub boom at 0 ms, groan and siren under 1.2 kHz, scored with hurt.breach.
stage2    what needs the machine's top first: hit.sub (top hit.t2 with sub v1/v2), hit.tail (top hit.t4 head with
          tail v1-v3), word.perfect (top word.load + whine + sparks); rendered and scored in their own critic run.
link      critic AI steps into SOURCES.json, a batch-local release tree, licence-check on it.
context   context/ts_scenes.py: "Liên thanh 3 s" (ts-xung-3s, current vs proposed playback), kills, Tia, breach.
session   board sessions "1-ts-s1" (guns and hits) and "1-ts-s4" (kills, words, Tia, breach) in
          ~/AudioLab/review/typing-survival/sessions (never overwritten without --force), cards revealed at the end.
report    ~/AudioLab/work/_batch1/typing-survival/<run>/REPORT.md and summary.json.

Heavy models run one at a time: the generate and critic steps wait while another Stable Audio 3 or critic
process runs on the machine. Nothing is written under games/**.
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
from common.batch1_dh import gen_src, heavy_running, wait_heavy_free  # noqa: F401  (shared helpers)

LAB = env.LAB
GAME = "typing-survival"
SEED = 20261024

# id -> SA3 jobs (variants of the card, seeds, length)
JOBS: dict[str, list[dict]] = {
    "gun.xung": [{"variants": ["E", "F", "G", "H"], "seeds": "2001-2006", "seconds": 1.0}],
    "gun.xung.loop": [{"variants": ["A", "B", "C"], "seeds": "3001-3004", "seconds": 10.0}],
    "gun.xung.tail": [{"variants": ["A", "B"], "seeds": "2001-2006", "seconds": 3.0}],
    "hit.t1": [{"variants": ["C", "E"], "seeds": "2001-2006", "seconds": 1.0}],
    "hit.t2": [{"variants": ["A", "B", "C", "D"], "seeds": "2001-2006", "seconds": 1.0}],
    "hit.t4": [{"variants": ["A", "B", "C", "D"], "seeds": "2001-2006", "seconds": 1.0}],
    "kill.swarm": [{"variants": ["A", "B", "C", "D"], "seeds": "2001-2006", "seconds": 1.0}],
    "kill.elite": [{"variants": ["A", "B", "C", "D"], "seeds": "2001-2006", "seconds": 1.0}],
    "word.load": [{"variants": ["A", "B", "C", "D"], "seeds": "2001-2006", "seconds": 1.0}],
    "gun.tia.pulse": [{"variants": ["A", "B"], "seeds": "2001-2006", "seconds": 1.0}],
    "hurt.breach": [{"variants": ["A", "B", "C"], "seeds": "2001-2006", "seconds": 1.0}],
}
P1 = ["gun.xung", "gun.xung.loop", "gun.xung.tail", "hit.t1", "hit.t2", "hit.sub", "hit.t4", "hit.tail"]
P4 = ["kill.swarm", "kill.elite", "word.load", "word.perfect", "gun.tia.pulse", "hurt.breach"]
IDS = P1 + P4
LOOPS = {"gun.xung.loop"}
TWO_PART = {"word.load"}       # BATCH1_BRIEF #17: the 40-70 ms "ka-chunk" is the design (expected_onsets: 2)
# earlier raw takes processed again with this batch's chain (only takes named after the same id)
OLD_RAW = {"hit.t1": ["sa3-trial"]}
OLD_RAW_FILTER = {"hit.t1": ("__A__", "__C__", "__D__")}      # C is the root (C s1006 3/5); A, D as the brief says


def _say(msg: str) -> None:
    print(f"[batch1-ts] {msg}", flush=True)


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


def _stale_two_part(sid: str, run: str) -> bool:
    """Processed before the two-part option existed (no `two_part` key in the proc reports)."""
    procs = list((id_dir(sid, run) / "processed").glob("*.proc.json"))
    return bool(procs) and any("two_part" not in json.loads(p.read_text("utf-8")) for p in procs)


def step_process(run: str, force: bool = False) -> None:
    from gen import process, sa3

    for sid in JOBS:
        card = sa3.read_card(card_path(sid))
        res = process.process_many(records(sid, run), card, id_dir(sid, run) / "processed",
                                   notch=sid in LOOPS, force=force or (sid in TWO_PART and _stale_two_part(sid, run)),
                                   two_part=sid in TWO_PART)
        _say(f"process {sid}: {res['kept']} giữ, {len(res['rejected'])} loại, {res['skipped']} đã có")
        for r in res["rejected"]:
            _say(f"  loại {r['candidate']}: {r['reason']}")


# ---------------------------------------------------------------- step 3: bodies for the recipes

# the four gun bodies checked in batch 0b (no second onset with any breech; recipe gun.xung.sa3-r2, 3/5)
GUN_0B_BODIES = [("A", 1005, 0.0364), ("D", 1002, 0.0299), ("C", 1002, 0.0434), ("D", 1005, 0.0299)]
GUN_BODY_S = 0.20            # head 0-120 ms with its early decay; the shared synthetic tail layer carries the rest
T4_BODY_S = 0.30             # BATCH1_BRIEF #14: hit.t4 head + body window 300 ms


def _proc_sources(sid: str, run: str, verified_only: bool = True) -> list[dict]:
    """Processed takes as recipe sources: their raw float file and the window process.py chose."""
    from critic import features as F
    from critic.thresholds import L1B
    import soundfile as sf

    out = []
    for p in sorted((id_dir(sid, run) / "processed").glob("*.proc.json")):
        d = json.loads(p.read_text("utf-8"))
        if verified_only and d.get("onset_verified") is False:
            continue
        wav = p.with_name(p.name.replace(".proc.json", ".wav"))
        x, sr = sf.read(str(wav), dtype="float64", always_2d=True)
        ro = F.hf_reonset(x.mean(axis=1), sr)
        dbl = (ro["hf_reonset_db"] is not None and ro["hf_reonset_db"] >= L1B["double_onset_db"]
               and (ro["hf_reonset_rise_db"] or 0) >= L1B["double_onset_rise_db"]
               and (ro["hf_reonset_dip_db"] or 0) <= L1B["double_onset_dip_db"])
        out.append({"file": d["source_f32"], "record": d["raw_record"], "window": d["window_raw_s"], "name": d["candidate"],
                    "len_ms": (d.get("window") or {}).get("len_ms"), "double_onset": bool(dbl),
                    "peak": float(np.max(np.abs(x)))})
    return out


def step_bodies(run: str, force: bool = False) -> dict:
    from common.batch1_dh import body_window

    out = base_dir(run) / "bodies.json"
    if out.is_file() and not force:
        _say(f"bodies: đã có {out}")
        return json.loads(out.read_text("utf-8"))
    pools: dict = {}
    # gun bodies: the four 0b bodies (same start, longer window) first, then the new E-H takes
    old = []
    trial = env.WORK / GAME / "gun.xung" / "sa3-trial" / "raw"
    for v, s, a in GUN_0B_BODIES:
        f = trial / f"gun.xung__{v}__s{s}.f32.wav"
        old.append({"file": str(f), "record": str(f.with_name(f.name.replace(".f32.wav", ".json"))),
                    "window": [a, round(a + GUN_BODY_S, 4)], "name": f"gun.xung__{v}__s{s}", "old_0b": True})
    new, rej = [], []
    for f in sorted((id_dir("gun.xung", run) / "raw").glob("*.f32.wav")):
        r = body_window(f, GUN_BODY_S)
        r["record"] = str(f.with_name(f.name.replace(".f32.wav", ".json")))
        r["name"] = f.name.replace(".f32.wav", "")
        (new if r["ok"] else rej).append(r)
    new.sort(key=lambda r: -r["peak_db"])
    pools["gun"] = {"length_s": GUN_BODY_S, "old": old, "new": new,
                    "rejected": [{k: r[k] for k in ("name", "double_onset", "clip", "pre_db", "peak_s")} for r in rej]}
    _say(f"bodies gun: 4 thân 0b + {len(new)}/{len(new) + len(rej)} thân mới dùng được")
    t4, rej = [], []
    for f in sorted((id_dir("hit.t4", run) / "raw").glob("*.f32.wav")):
        r = body_window(f, T4_BODY_S)
        r["record"] = str(f.with_name(f.name.replace(".f32.wav", ".json")))
        r["name"] = f.name.replace(".f32.wav", "")
        (t4 if r["ok"] else rej).append(r)
    t4.sort(key=lambda r: -r["peak_db"])
    pools["t4"] = {"length_s": T4_BODY_S, "bodies": t4, "rejected": [r["name"] for r in rej]}
    _say(f"bodies hit.t4: {len(t4)}/{len(t4) + len(rej)}")
    for key, sid in (("t2", "hit.t2"), ("elite", "kill.elite"), ("breach", "hurt.breach"), ("tia", "gun.tia.pulse"),
                     ("load", "word.load"), ("tail", "gun.xung.tail")):
        # textures and tails carry no onset of their own (the synthetic arc, the card's onset class "none")
        rows = _proc_sources(sid, run, verified_only=sid not in ("gun.tia.pulse", "gun.xung.tail"))
        ok = [r for r in rows if not r["double_onset"] or sid in ("word.load", "gun.tia.pulse")]
        pools[key] = {"bodies": ok, "rejected": [r["name"] for r in rows if r not in ok]}
        _say(f"bodies {sid}: {len(ok)}/{len(rows)} (đầu tiếng đã xác minh, không hai đầu tiếng)")
    out.write_text(json.dumps(pools, indent=1, ensure_ascii=False, default=float), "utf-8")
    return pools


# ---------------------------------------------------------------- step 4: recipes

def lib(path: str) -> dict:
    return {"library": path if "/" in path else f"kenney/impact-sounds/Audio/{path}.ogg"}


def _cycle(layer: dict, sources: list[dict]) -> dict:
    layer["source"] = sources[0]
    if len(sources) > 1:
        layer.setdefault("vary", {}).update({"swapMode": "cycle", "swap": sources[1:]})
    return layer


def _recipe(rid: str, group: str, family: str, desc: str, layers: list[dict], chain: dict, count: int, seed: int,
            export: str, pitch=(0, 0), gain=(0, 0), loop: bool = False) -> dict:
    d = {"$schema": "../../schemas/recipe.schema.json", "schema": "audiolab.recipe/1", "game": GAME, "id": rid,
         "group": group, "family": family, "description": desc, "channels": 1, "layers": layers, "chain": chain,
         "variants": {"count": count, "seed": seed, "includeBase": True, "pitchCents": list(pitch), "gainDb": list(gain)},
         "export": {"path": export, "ogg": True, "oggQuality": 0.6}}
    if loop:
        d["loop"] = True
    return d


def _j(x):
    return json.loads(json.dumps(x))


BREECH = [lib(f"impactMetal_light_00{k}") for k in range(5)]
BREECH_LAYER = {"id": "breech", "role": "mech", "offsetMs": 12, "gainDb": -9,
                "filters": [{"type": "highpass", "hz": 1200}, {"type": "peak", "hz": 2500, "gainDb": -4, "q": 1.0}],
                "trim": {"endMs": 35}, "fadeOutMs": 25, "vary": {"offsetMs": [-3, 4]}}
CRACK = {"id": "crack", "role": "attack", "source": {"synth": "noise_burst", "params": {
    "color": "white", "durMs": 30, "attackMs": 0.2, "decayMs": 30, "hpHz": 1800, "lpHz": 9000}}, "gainDb": 8,
    "vary": {"gainDb": [-1.0, 1.0]}}
# the shared tail: pink noise 160-650 Hz, t60 900 ms -> the shot is -20 dB at about 175 ms and -40 dB before 330 ms
# (BATCH1_BRIEF §3.2: -20 dB at 140-180 ms, -40 dB before 350 ms; at 100 ms the previous round is about -12 dB)
TAIL = {"id": "tail", "role": "tail", "source": {"synth": "noise_burst", "params": {
    "color": "pink", "durMs": 380, "attackMs": 3, "decayMs": 900, "hpHz": 160, "lpHz": 650, "order": 4}}, "gainDb": -1}
SUB = {"id": "sub", "role": "sub", "source": {"synth": "sub_thump", "params": {
    "startHz": 95, "endHz": 45, "glideMs": 45, "durMs": 115, "decayMs": 100, "click": 0.2, "driveDb": 8}}, "gainDb": -4}
GUN_CHAIN = {"dcHpfHz": 35, "saturation": {"driveDb": 5, "mix": 0.35}, "headTrim": {"thresholdDb": -50, "preRollMs": 0.3},
             "maxLengthMs": 380, "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 300},
             "normalise": {"mode": "lufs-m-max", "target": -20}, "limiter": {"ceilingDbtp": -1.0, "releaseMs": 40, "maxGrDb": 6}}
GUN_B_DB = -5.0              # set B is 4-6 dB under set A (BATCH1_BRIEF §3.2)


def gun_recipes(pools: dict) -> dict[str, dict]:
    out = {}
    syn_body = {"id": "body", "role": "body", "source": {"synth": "noise_burst", "params": {
        "color": "pink", "durMs": 140, "attackMs": 0.5, "decayMs": 150, "hpHz": 150, "lpHz": 520, "order": 4}}, "gainDb": 0}
    for key in ("a", "b"):
        heavy = key == "a"
        body = _j(syn_body)
        if not heavy:
            body["gainDb"] = -3
            body["source"]["params"]["hpHz"] = 200
        layers = [_j(CRACK), _cycle(_j(BREECH_LAYER), BREECH[:4] if heavy else BREECH[1:] + BREECH[:1]), body, _j(TAIL)]
        if heavy:
            layers.append(_j(SUB))
        chain = _j(GUN_CHAIN)
        if not heavy:
            chain["normalise"]["target"] = -20 + GUN_B_DB
        out[f"gun.xung.d1{key}"] = _recipe(
            f"gun.xung.d1{key}", "shot", "ban",
            "Lô 1 (BATCH1_BRIEF §3.4, hướng 1 '0a nâng cấp'): công thức 0a (anh chấm 4/5) giữ nổ giòn nhiễu trắng và khóa "
            "nòng Kenney Impact Metal light; thân nhiễu hồng 150–520 Hz dày hơn khoảng 6 dB; lớp đuôi 160–650 Hz tắt "
            "dần (t60 900 ms: −20 dB ở khoảng 175 ms, −40 dB trước 330 ms) để phát trước còn khoảng −12 dB khi phát sau tới; "
            + ("sub 95→45 Hz bão hòa 8 dB để có họa âm nghe được trên loa nhỏ. Bộ A (nặng)."
               if heavy else "không sub, thân mỏng hơn, nhỏ hơn bộ A 5 dB. Bộ B (nhẹ), phát xen với A.")
            + " Biến thể n dùng khóa nòng thứ n.", layers, chain, 4, 2501 if heavy else 2502,
            f"sfx/guns/gun-xung-{key}", pitch=(-20, 20), gain=(-0.5, 0.5))
    old, new = pools["gun"]["old"], pools["gun"]["new"]
    bodies = [old[0], new[0], old[1], new[1], new[2], old[2], new[3], old[3]] if len(new) >= 4 else old + new
    for key, part in (("a", bodies[:4]), ("b", bodies[4:8])):
        heavy = key == "a"
        body = _cycle({"id": "body", "role": "body", "offsetMs": 0.5, "gainDb": 1 if heavy else -2, "fadeInMs": 1.5,
                       "fadeOutMs": 90, "filters": [{"type": "highpass", "hz": 90 if heavy else 150, "order": 2},
                                                   {"type": "lowpass", "hz": 1800, "order": 4}]},
                      [gen_src(b) for b in part])
        layers = [_j(CRACK), _cycle(_j(BREECH_LAYER), BREECH[:4] if heavy else BREECH[1:] + BREECH[:1]), body, _j(TAIL)]
        if heavy:
            layers.append(_j(SUB))
        chain = _j(GUN_CHAIN)
        if not heavy:
            chain["normalise"]["target"] = -20 + GUN_B_DB
        out[f"gun.xung.d2{key}"] = _recipe(
            f"gun.xung.d2{key}", "shot", "ban",
            "Lô 1 (BATCH1_BRIEF §3.4, hướng 2 'thân Stable Audio 3'): công thức 0b (3/5) với thân Stable Audio 3 lọc 90 Hz–1,8 kHz "
            "(4 thân 0b đã kiểm không có đầu tiếng thứ hai: A s1005, D s1002, C s1002, D s1005; 4 thân mới từ prompt E–H, "
            "chỉ giữ thân một đầu tiếng), cửa sổ 200 ms từ 4 ms trước đỉnh; khóa nòng đổi sang Impact Metal light như 0a, cộng "
            "nổ giòn và lớp đuôi chung như hướng 1. " + ("Bộ A: có sub." if heavy else "Bộ B: không sub, nhỏ hơn A 5 dB.")
            + " Biến thể n dùng thân n và khóa nòng n.", layers, chain, 4, 2503 if heavy else 2504,
            f"sfx/guns/gun-xung-{key}", pitch=(-20, 20), gain=(-0.5, 0.5))
    # the bed: library loops (no model), cut to 3.0 s, crossfaded into a 2.5 s loop
    def loop_recipe(rid, desc, layers, seed):
        return _recipe(rid, "ambience", "ban", desc, layers,
                       {"dcHpfHz": 35, "loopCrossfadeMs": 500, "normalise": {"mode": "lufs-i", "target": -26},
                        "limiter": {"ceilingDbtp": -1.0, "maxGrDb": 3}}, 2, seed, "sfx/guns/gun-xung-loop", loop=True)
    out["gun.xung.loop.lib"] = loop_recipe(
        "gun.xung.loop.lib",
        "Lô 1 (BATCH1_BRIEF §3.2): nền cơ khí liên thanh từ thư viện CC0, không mô hình. Động cơ Kenney Sci-fi engineCircular "
        "(lọc thấp 500 Hz) là phần chính 80–500 Hz; lách cách băng đạn VSCO-2-CE Ratchet1-Fast (lọc cao 3 kHz) rất nhỏ; đoạn "
        "3,0 s nối thành vòng 2,5 s. Biến thể 2 đổi sang spaceEngineLow (đoạn giữa) và Snare2-roll.",
        [_cycle({"id": "engine", "role": "body", "trim": {"startMs": 1000, "endMs": 4000},
                 "filters": [{"type": "highpass", "hz": 60}, {"type": "lowpass", "hz": 500, "order": 4}]},
                [lib("kenney/sci-fi-sounds/Audio/engineCircular_001.ogg"), lib("kenney/sci-fi-sounds/Audio/spaceEngineLow_002.ogg")]),
         _cycle({"id": "rattle", "role": "sweetener", "gainDb": -22, "trim": {"startMs": 2000, "endMs": 5000},
                 "filters": [{"type": "highpass", "hz": 3000, "order": 4}, {"type": "lowpass", "hz": 8000}]},
                [lib("vsco2ce/Percussion/Ratchet1-Fast_v1_rr1_Sum.wav"), lib("vsco2ce/Percussion/Snare2-rollNS_v3_rr1_Sum.wav")])],
        2510)
    # ceasefire tail from the library: brake drum / anvil rung low, a synthetic hall, a servo winding down
    out["gun.xung.tail.smp"] = _recipe(
        "gun.xung.tail.smp", "generic", "ban",
        "Lô 1 (BATCH1_BRIEF §3.2): khi ngừng bắn. Vang thép: VCSL Brake Drum (biến thể 2: Anvil) lọc thấp 1,5 kHz; vang sảnh "
        "tổng hợp (nhiễu hồng 150–1200 Hz, t60 650 ms); servo hạ (răng cưa 260→70 Hz lọc thấp 700 Hz). Phần 1–4 kHz tắt sớm.",
        [_cycle({"id": "steel", "role": "body", "gainDb": -4, "filters": [{"type": "lowpass", "hz": 1500, "order": 4}],
                 "trim": {"endMs": 650}, "fadeOutMs": 250},
                [lib("vcsl/Idiophones/Struck Idiophones/Brake Drum/BrakeDrum1_Hammer_v2_rr1_Mid.wav"),
                 lib("vcsl/Idiophones/Struck Idiophones/Anvil/Anvil_Hit2_v2_rr1_Mid.wav")]),
         {"id": "hall", "role": "tail", "gainDb": -6, "source": {"synth": "noise_burst", "params": {
             "color": "pink", "durMs": 650, "attackMs": 15, "decayMs": 650, "hpHz": 150, "lpHz": 1200, "order": 2}}},
         {"id": "servo", "role": "sweetener", "gainDb": -14, "offsetMs": 40, "source": {"synth": "tone", "params": {
             "wave": "saw", "freqHz": 260, "endHz": 70, "glideMs": 420, "durMs": 480, "attackMs": 20, "decayMs": 600}},
          "filters": [{"type": "lowpass", "hz": 700, "order": 2}]}],
        {"dcHpfHz": 35, "headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": 650,
         "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 380}, "normalise": {"mode": "lufs-m-max", "target": -20},
         "limiter": {"ceilingDbtp": -1.0, "releaseMs": 80, "maxGrDb": 6}}, 2, 2511, "sfx/guns/gun-xung-tail")
    return out


# hit.sub (BATCH1_BRIEF #13): 85->45 Hz, 90 ms, 3 dB of drive; a second, rounder take to compare
SUB_V = [{"synth": "sub_thump", "params": {"startHz": 85, "endHz": 45, "glideMs": 45, "durMs": 90, "decayMs": 80, "driveDb": 3}},
         {"synth": "sub_thump", "params": {"startHz": 72, "endHz": 42, "glideMs": 60, "durMs": 110, "decayMs": 100, "driveDb": 6}}]
SUB_IN_T2_DB = -9.0          # the shared sub under the T2 head: 35-55 % of the pre-mix under 150 Hz (brief #13)
SUB_IN_T4_DB = -8.0
# hit.tail (brief #14): VCSL Anvil / Brake Drum, a short full-band 'ting' then only the part under 1.2 kHz, plus a hall
ANVIL = "vcsl/Idiophones/Struck Idiophones/Anvil/Anvil_Hit1_v2_rr1_Mid.wav"
BRAKE = "vcsl/Idiophones/Struck Idiophones/Brake Drum/BrakeDrum1_Hammer_v3_rr1_Mid.wav"


def tail_layers(k: int) -> list[dict]:
    """Tail v1 (anvil), v2 (brake drum), v3 (both, darker): ring under 1.2 kHz, the 1-4 kHz part only 100 ms."""
    src = [lib(ANVIL), lib(BRAKE), lib(ANVIL)][k]
    ring = {"id": "ring", "role": "tail", "source": src, "gainDb": -3, "trim": {"endMs": 900}, "fadeOutMs": 400,
            "filters": [{"type": "lowpass", "hz": 1200 if k < 2 else 900, "order": 4}]}
    ting = {"id": "ting", "role": "attack", "source": src, "gainDb": -10, "trim": {"endMs": 100}, "fadeOutMs": 70,
            "filters": [{"type": "highpass", "hz": 1200}]}
    hall = {"id": "hall", "role": "tail", "gainDb": -9, "offsetMs": 10, "source": {"synth": "noise_burst", "params": {
        "color": "pink", "durMs": 850, "attackMs": 20, "decayMs": 800, "hpHz": 120, "lpHz": 900 if k < 2 else 700, "order": 2}}}
    out = [ring, ting, hall]
    if k == 2:
        out.append({"id": "ring2", "role": "tail", "source": lib(BRAKE), "gainDb": -6, "trim": {"endMs": 800}, "fadeOutMs": 350,
                    "filters": [{"type": "lowpass", "hz": 900, "order": 4}]})
    return out


def hit_recipes(pools: dict) -> dict[str, dict]:
    out = {}
    out["hit.sub"] = _recipe(
        "hit.sub", "generic", "trung",
        "Lô 1 (BATCH1_BRIEF #13): sub dùng chung của bậc trúng (mã thêm từ T2). Biến thể 1: 85→45 Hz, 90 ms, bão hòa 3 dB; "
        "biến thể 2: 72→42 Hz, 110 ms, bão hòa 6 dB (tròn hơn, nhiều họa âm hơn).",
        [_cycle({"id": "sub", "role": "sub"}, _j(SUB_V))],
        {"dcHpfHz": 25, "headTrim": {"thresholdDb": -50, "preRollMs": 0.3}, "maxLengthMs": 130,
         "tail": {"floorDb": -60, "fadeMs": 10}, "normalise": {"mode": "lufs-m-max", "target": -20},
         "limiter": {"ceilingDbtp": -1.0, "releaseMs": 40, "maxGrDb": 6}}, 2, 2520, "sfx/hits/hit-sub")
    out["hit.tail"] = _recipe(
        "hit.tail", "generic", "trung",
        "Lô 1 (BATCH1_BRIEF #14): đuôi kim loại dùng chung (mã thêm từ T4; chất liệu của gun.xung.tail). Biến thể 1: VCSL "
        "Anvil; 2: VCSL Brake Drum; 3: cả hai, tối hơn. Tiếng 'ting' đủ dải chỉ giữ 100 ms, phần ngân chỉ dưới 1,2 kHz, "
        "vang sảnh tổng hợp (nhiễu hồng t60 800 ms), để dải 1–4 kHz không ngân quá 300 ms trên −30 dB.",
        [], {"dcHpfHz": 35, "headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": 900,
             "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 550}, "normalise": {"mode": "lufs-m-max", "target": -20},
             "limiter": {"ceilingDbtp": -1.0, "releaseMs": 80, "maxGrDb": 6}}, 3, 2521, "sfx/hits/hit-tail")
    # cycle every tail layer by variant: layer i of variant n is tail_layers(n)[i]; v3 has one more layer
    tl = [tail_layers(k) for k in range(3)]
    layers = []
    for i in range(3):
        lay = _j(tl[0][i])
        lay["source"] = tl[0][i]["source"]
        lay["vary"] = {"swapMode": "cycle", "swap": [tl[1][i]["source"], tl[2][i]["source"]]}
        layers.append(lay)
    extra = _j(tl[2][3])
    extra["vary"] = {"swapMode": "cycle", "swap": [{"synth": "noise_burst", "params": {"durMs": 1, "decayMs": 1}},
                                                   tl[2][3]["source"]]}
    extra["source"] = {"synth": "noise_burst", "params": {"durMs": 1, "decayMs": 1}}
    extra["gainDb"] = -6
    layers.append(extra)
    out["hit.tail"]["layers"] = layers
    T2 = pools["t2"]["bodies"]
    T2 = sorted(T2, key=lambda r: r["name"])
    n2 = min(12, len(T2))
    sub_t2 = {"id": "sub", "role": "sub", "source": _j(SUB_V[0]), "gainDb": SUB_IN_T2_DB}
    chain_t2 = {"dcHpfHz": 30, "headTrim": {"thresholdDb": -50, "preRollMs": 0.3}, "maxLengthMs": 192,
                "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 120}, "normalise": {"mode": "lufs-m-max", "target": -20},
                "limiter": {"ceilingDbtp": -1.0, "releaseMs": 50, "maxGrDb": 6}}
    out["hit.t2.raw"] = _recipe(
        "hit.t2.raw", "hit-heavy", "trung",
        "Lô 1 (BATCH1_BRIEF #13), nghe ghép sẵn: đầu tiếng + thân là bản Stable Audio 3 thô có cửa sổ (prompt A–D, cửa sổ "
        "process.py, đầu tiếng đã xác minh, không hai đầu tiếng), lọc cao 120 Hz; cộng hit.sub v1 (85→45 Hz, 90 ms) nhỏ "
        "hơn 9 dB. Biến thể n dùng bản thô n.",
        [_cycle({"id": "body", "role": "body", "filters": [{"type": "highpass", "hz": 120, "order": 2}]},
                [gen_src(b) for b in T2[:n2]]), sub_t2], chain_t2, n2, 2522, "sfx/hits/hit-t2")
    fronts = [lib(f"impactMetal_heavy_00{k}") for k in (0, 2, 3, 4)]
    nk = min(6, n2)
    out["hit.t2.kb"] = _recipe(
        "hit.t2.kb", "hit-heavy", "trung",
        "Lô 1 (BATCH1_BRIEF #13), nghe ghép sẵn: đầu tiếng Kenney Impact Metal heavy (lọc cao 700 Hz, 45 ms) trên thân Stable "
        "Audio 3 lọc 120 Hz–2 kHz; cộng hit.sub v1 nhỏ hơn 9 dB. Biến thể n dùng đầu tiếng n và thân n.",
        [_cycle({"id": "front", "role": "attack", "gainDb": -3, "filters": [{"type": "highpass", "hz": 700}],
                 "trim": {"endMs": 45}, "fadeOutMs": 30}, (fronts * 2)[:nk]),
         _cycle({"id": "body", "role": "body", "gainDb": -1, "fadeInMs": 2,
                 "filters": [{"type": "highpass", "hz": 120, "order": 2}, {"type": "lowpass", "hz": 2000, "order": 4}]},
                [gen_src(b) for b in T2[n2 - nk:n2] or T2[:nk]]), _j(sub_t2)], _j(chain_t2), nk, 2523, "sfx/hits/hit-t2")
    T4 = pools["t4"]["bodies"]
    n4 = min(8, len(T4))
    out["hit.t4"] = _recipe(
        "hit.t4", "hit-heavy", "trung",
        "Lô 1 (BATCH1_BRIEF #14), nghe ghép sẵn đủ lớp như mã ghép từ T4: đầu tiếng Kenney Impact Metal heavy, thân Stable "
        "Audio 3 300 ms (prompt A–D, cửa sổ từ 4 ms trước đỉnh, một đầu tiếng), hit.sub v1 nhỏ hơn 8 dB, hit.tail v1 "
        "(Anvil dưới 1,2 kHz, 'ting' 100 ms, vang sảnh). Biến thể n dùng thân n.",
        [_cycle({"id": "front", "role": "attack", "gainDb": -4, "filters": [{"type": "highpass", "hz": 600}],
                 "trim": {"endMs": 60}, "fadeOutMs": 40}, (fronts * 2)[:n4]),
         _cycle({"id": "body", "role": "body", "gainDb": 0, "fadeInMs": 2, "fadeOutMs": 120,
                 "filters": [{"type": "highpass", "hz": 90, "order": 2}]}, [gen_src(b) for b in T4[:n4]]),
         {"id": "sub", "role": "sub", "source": _j(SUB_V[0]), "gainDb": SUB_IN_T4_DB},
         *[dict(_j(l), id=f"tail-{l['id']}", offsetMs=15) for l in tail_layers(0)]],
        {"dcHpfHz": 30, "headTrim": {"thresholdDb": -50, "preRollMs": 0.3}, "maxLengthMs": 950,
         "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 600}, "normalise": {"mode": "lufs-m-max", "target": -20},
         "limiter": {"ceilingDbtp": -1.0, "releaseMs": 80, "maxGrDb": 6}}, n4, 2524, "sfx/hits/hit-t4")
    return out


def p4_recipes(pools: dict) -> dict[str, dict]:
    out = {}
    E = pools["elite"]["bodies"]
    ne = min(6, len(E))
    E = sorted(E, key=lambda r: -(r.get("len_ms") or 0))[:ne]
    arcs = [{"id": f"arc{i}", "role": "sweetener", "offsetMs": off, "gainDb": g, "source": {"synth": "noise_burst", "params": {
        "color": "white", "durMs": 18, "attackMs": 0.3, "decayMs": 14, "hpHz": 2000, "lpHz": 8000}}, "vary": {"offsetMs": [-15, 15]}}
            for i, (off, g) in enumerate(((30, -16), (85, -18), (140, -20), (210, -22), (300, -25)))]
    out["kill.elite"] = _recipe(
        "kill.elite", "death-big", "chet",
        "Lô 1 (BATCH1_BRIEF #16): lính tinh nhuệ nổ. Thân Stable Audio 3 (prompt A–D, cửa sổ process.py 400–600 ms) cộng "
        "tia điện tổng hợp: năm tiếng tách nhiễu 2–8 kHz thưa dần (30–300 ms), nhỏ dần.",
        [_cycle({"id": "body", "role": "body", "filters": [{"type": "highpass", "hz": 45, "order": 2}]},
                [gen_src(b) for b in E]), *arcs],
        {"dcHpfHz": 35, "headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": 600,
         "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 400}, "normalise": {"mode": "lufs-m-max", "target": -20},
         "limiter": {"ceilingDbtp": -1.0, "releaseMs": 60, "maxGrDb": 6}}, ne, 2530, "sfx/kills/kill-elite", pitch=(-30, 30))
    LD = pools["load"]["bodies"]
    nl = min(4, len(LD))
    out["word.load.kn"] = _recipe(
        "word.load.kn", "reward", "thuong",
        "Lô 1 (BATCH1_BRIEF #17), hướng 2: 'ka' là Kenney RPG metalClick (lọc cao 1 kHz, 60 ms), 'chunk' là metalLatch 55 ms "
        "sau, dưới đó thân của một bản Stable Audio 3 lọc thấp 900 Hz cho sức nặng. Dải 1–4 kHz phải tắt 15 dB trong 100 ms.",
        [{"id": "ka", "role": "attack", "source": lib("kenney/rpg-audio/Audio/metalClick.ogg"), "gainDb": -6,
          "filters": [{"type": "highpass", "hz": 1000}], "trim": {"endMs": 60}, "fadeOutMs": 35},
         {"id": "chunk", "role": "mech", "source": lib("kenney/rpg-audio/Audio/metalLatch.ogg"), "offsetMs": 55, "gainDb": -3,
          "trim": {"endMs": 140}, "fadeOutMs": 70, "vary": {"offsetMs": [-8, 10]}},
         _cycle({"id": "body", "role": "body", "offsetMs": 50, "gainDb": -2, "fadeInMs": 2, "fadeOutMs": 80,
                 "filters": [{"type": "lowpass", "hz": 900, "order": 4}, {"type": "highpass", "hz": 60}]},
                [gen_src(b) for b in LD[:nl]])],
        {"dcHpfHz": 35, "headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": 300,
         "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 200}, "normalise": {"mode": "lufs-m-max", "target": -20},
         "limiter": {"ceilingDbtp": -1.0, "releaseMs": 50, "maxGrDb": 6}}, nl, 2531, "sfx/words/word-load", pitch=(-20, 20))
    TX = pools["tia"]["bodies"]
    nt = min(6, len(TX))
    out["gun.tia.pulse"] = _recipe(
        "gun.tia.pulse", "hit-small", "trung",
        "Lô 1 (BATCH1_BRIEF #19): tia điện chích. Tách điện tổng hợp (nhiễu trắng 2–8 kHz, 40 ms, hai tiếng tách), ù 100 Hz "
        "và 50 Hz rất ngắn, kết cấu Stable Audio 3 ('electric arc crackle') lọc cao 1,5 kHz bên dưới. Biến thể n dùng kết cấu n.",
        [{"id": "arc", "role": "attack", "gainDb": -4, "source": {"synth": "noise_burst", "params": {
            "color": "white", "durMs": 40, "attackMs": 0.3, "decayMs": 35, "hpHz": 2000, "lpHz": 8000}}},
         {"id": "tick", "role": "sweetener", "offsetMs": 14, "gainDb": -10, "source": {"synth": "click", "params": {
             "durMs": 3, "hpHz": 3000, "lpHz": 9000}}, "vary": {"offsetMs": [-6, 10]}},
         {"id": "hum", "role": "body", "gainDb": -10, "source": {"synth": "tone", "params": {
             "wave": "square", "freqHz": 100, "durMs": 50, "attackMs": 2, "decayMs": 60}},
          "filters": [{"type": "lowpass", "hz": 400, "order": 2}]},
         _cycle({"id": "texture", "role": "body", "gainDb": -6, "filters": [{"type": "highpass", "hz": 1500, "order": 2}],
                 "fadeOutMs": 20}, [gen_src(b) for b in TX[:nt]])],
        {"dcHpfHz": 35, "headTrim": {"thresholdDb": -50, "preRollMs": 0.3}, "maxLengthMs": 60,
         "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 35}, "normalise": {"mode": "lufs-m-max", "target": -20},
         "limiter": {"ceilingDbtp": -1.0, "releaseMs": 30, "maxGrDb": 6}}, nt, 2532, "sfx/guns/gun-tia-pulse", pitch=(-40, 40))
    BR = pools["breach"]["bodies"]
    nb = min(3, len(BR))
    BR = sorted(BR, key=lambda r: -(r.get("len_ms") or 0))[:nb]
    siren = [{"id": "siren1", "role": "sweetener", "offsetMs": 30, "gainDb": -9, "source": {"synth": "tone", "params": {
                "wave": "square", "freqHz": 440, "durMs": 90, "attackMs": 4, "decayMs": 400}},
              "filters": [{"type": "lowpass", "hz": 1600, "order": 4}], "fadeOutMs": 15},
             {"id": "siren2", "role": "sweetener", "offsetMs": 140, "gainDb": -9, "source": {"synth": "tone", "params": {
                 "wave": "square", "freqHz": 330, "durMs": 90, "attackMs": 4, "decayMs": 400}},
              "filters": [{"type": "lowpass", "hz": 1600, "order": 4}], "fadeOutMs": 15}]
    out["hurt.breach"] = _recipe(
        "hurt.breach", "alarm", "nen",
        "Lô 1 (BATCH1_BRIEF #20): tuyến bị phá. Thân Stable Audio 3 (nổ trầm, thép rên; cửa sổ process.py) cộng còi hai nốt "
        "tổng hợp 440/330 Hz (vuông, lọc thấp 1,6 kHz, mỗi nốt 90 ms, ở 30 ms và 140 ms): hai nhịp ngắn, không ngân ở 1–4 kHz.",
        [_cycle({"id": "body", "role": "body", "filters": [{"type": "highpass", "hz": 40, "order": 2}]},
                [gen_src(b) for b in BR]), *siren],
        {"dcHpfHz": 35, "headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": 720,
         "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 450}, "normalise": {"mode": "lufs-m-max", "target": -20},
         "limiter": {"ceilingDbtp": -1.0, "releaseMs": 80, "maxGrDb": 6}}, nb, 2533, "sfx/alerts/hurt-breach")
    return out


def recipe_path(rid: str) -> Path:
    return LAB / "build" / "recipes" / GAME / f"{rid}.b1.json"


def recipe_run(rid: str, run: str) -> Path:
    sid = rid if (LAB / "specs" / GAME / f"{rid}.yaml").is_file() else ".".join(rid.split(".")[:-1]) or rid
    if rid.startswith("gun.xung.d"):
        sid = "gun.xung"
    return env.WORK / GAME / sid / f"{run}-recipe-{rid}"


def card_for(rid: str) -> Path:
    for sid in sorted(IDS + ["gun.xung.loop", "gun.xung.tail"], key=len, reverse=True):
        if rid == sid or rid.startswith(sid + "."):
            return card_path(sid)
    raise KeyError(rid)


def render_recipes(recipes: dict[str, dict], run: str, force: bool) -> None:
    from build import render

    for rid, data in recipes.items():
        p = recipe_path(rid)
        p.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", "utf-8")
        out = recipe_run(rid, run)
        if out.is_dir() and (out / "render.json").is_file() and not force:
            _say(f"recipe {rid}: đã có {out}")
            continue
        res = render.render(p, out=out, spec=card_for(rid))
        _say(f"recipe {rid}: {res.report['count']} biến thể, mức id {res.report['idLevel']} LUFS-M; "
             + ("; ".join(res.report["warnings"]) or "không cảnh báo"))


STAGE1 = ("gun.xung.d1a", "gun.xung.d1b", "gun.xung.d2a", "gun.xung.d2b", "gun.xung.loop.lib", "gun.xung.tail.smp",
          "hit.sub", "hit.tail", "hit.t2.raw", "hit.t2.kb", "hit.t4", "kill.elite", "word.load.kn", "gun.tia.pulse", "hurt.breach")


def step_recipes(run: str, force: bool = False) -> None:
    pools = step_bodies(run)
    rec = {**gun_recipes(pools), **hit_recipes(pools), **p4_recipes(pools)}
    render_recipes({k: rec[k] for k in STAGE1}, run, force)


# ---------------------------------------------------------------- step 5: critic

REF_0A = {
    "gun.xung": env.WORK / GAME / "gun.xung" / "batch0-2026-10-23-r2" / "masters" / "gun.xung-v2.wav",   # 00d0eb0f, 4/5
    "hit.t2": env.WORK / GAME / "hit.t2" / "batch0-2026-10-23-r2" / "masters" / "hit.t2-v2.wav",         # e169bbdd, 3/5
}
REF_0B_HIT_T1 = env.WORK / GAME / "hit.t1" / "sa3-r2" / "processed" / "hit.t1__C__s1006.wav"           # 7120c956, 3/5
CANDIDATE_TAKES = ("gun.xung.loop", "gun.xung.tail", "hit.t1", "kill.swarm", "kill.elite", "word.load", "gun.tia.pulse")


def critic_out(run: str, name: str) -> Path:
    return base_dir(run) / f"critic-{name}"


def finals(run: str) -> tuple[list[Path], list[Path]]:
    dirs, srcs = [], []
    for sid in CANDIDATE_TAKES:
        p = id_dir(sid, run) / "processed"
        if p.is_dir():
            dirs.append(p)
            srcs.append(p / "SOURCES.json")
    for rid in STAGE1:
        r = recipe_run(rid, run)
        dirs.append(r / "masters")
        srcs.append(r / "SOURCES.json")
    for sid, f in REF_0A.items():
        dirs.append(f)
        srcs.append(f.parent.parent / "SOURCES.json")
    return dirs, srcs


def _critic_run(inputs: list[Path], srcs: list[Path], out: Path, spec: Path, stage: str = "final", layers: str = "all") -> int:
    """The critic in its own process (`launch.py critic run ...`), so every other batch script sees a heavy model
    running (common/batch1_dh.heavy_running) and waits."""
    import subprocess

    argv = ["run", *map(str, inputs), "--spec", str(spec), "--stage", stage, "--layers", layers, "--out", str(out),
            "--seed", str(SEED), "--quiet"]
    if layers != "L1,L1b":
        argv.append("--blind-cards")
    for s_ in srcs:
        if s_.is_file():
            argv += ["--sources", str(s_)]
    return subprocess.run([sys.executable, "-I", str(LAB / "common" / "launch.py"), "critic", *argv]).returncode


def step_critic(run: str, force: bool = False) -> None:
    out = critic_out(run, "final")
    if (out / "_batch.json").is_file() and not force:
        _say(f"critic: đã có {out}")
        return
    dirs, srcs = finals(run)
    wait_heavy_free("critic")
    t0 = time.time()
    _say(f"critic final ({len(dirs)} mục): mã {_critic_run(dirs, srcs, out, LAB / 'specs' / GAME)}, {time.time() - t0:.0f} s")
    raws = [d for sid in JOBS for d in raw_dirs(sid, run) if d.parent.name == run]
    _say(f"critic raw L1 (clip đọc bản float): mã {_critic_run(raws, [], critic_out(run, 'raw'), LAB / 'specs' / GAME, 'raw', 'L1,L1b')}")


# ---------------------------------------------------------------- listening-list helpers (plan §4.6 step 2)

NO_PICK_FLAGS = {"double_onset", "lr_imbalance"}
BED_NO_PICK = {"loop_signature", "decoder_comb", "stereo_mismatch"}
PROBE_IDS = ("hit.t1", "hit.t4", "kill.swarm", "gun.tia.pulse")      # 4/14 ids, about 30 %
ONSET_FREE = {"gun.xung.tail", "gun.xung.loop", "hit.tail"}            # onset class none/loop: nothing to verify


def _docs(out: Path) -> dict[str, dict]:
    docs = {}
    if not out.is_dir():
        return docs
    for p in sorted(out.glob("*.json")):
        if p.name.startswith("_"):
            continue
        d = json.loads(p.read_text("utf-8"))
        d["_out"] = str(out)
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
    return _sid(d) in ONSET_FREE or _proc(d).get("onset_verified", True) is not False


def _kind(d: dict) -> str:
    path = d["file"]["path"]
    if "/batch0-" in path or "/sa3-r2/" in path:
        return "ref"
    return "recipe" if "-recipe-" in path else "sa3"


def _rid(d: dict) -> str:
    """Recipe id of a master (gun.xung.d2a-v3 -> gun.xung.d2a); '' for model takes."""
    stem = d["file"]["stem"]
    return stem.rsplit("-v", 1)[0] if _kind(d) == "recipe" else ""


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
    rng = random.Random(int(hashlib.sha256(f"batch-1-ts:{sid}".encode()).hexdigest()[:8], 16))
    return rng.choice(sorted(pool, key=lambda d: d["file"]["stem"]))


# kept on disk and in the report only: hit.t2.kb (flam 32-62 ms after the head, see T2_KB2), word.load.kn (its main hit
# ~95 ms late, see load_kn2_recipe)
SUPERSEDED = {"hit.t2.kb", "word.load.kn"}


def eligible(docs: dict[str, dict], sid: str) -> tuple[list[dict], dict]:
    # the 0a/0b references are scored in the same run for comparison; they enter a session only as their own pick
    mine = [d for d in docs.values() if _sid(d) == sid and _kind(d) != "ref" and _rid(d) not in SUPERSEDED]
    ok = sorted([d for d in mine if d["verdict"] == "PASS"], key=_rank)
    info = {"n": len(mine), "pass": len(ok), "pass_unverified_onset": sum(1 for d in ok if not _verified(d))}
    allowed = NO_PICK_FLAGS - ({"double_onset"} if sid in TWO_PART else set())
    info["pass_no_pick_flags"] = sum(1 for d in ok if _flags(d) & allowed)
    ok = [d for d in ok if _verified(d) and not _flags(d) & allowed]
    if sid in LOOPS:
        clean = [d for d in ok if not _flags(d) & BED_NO_PICK]
        info["clean_pass"] = len(clean)
        ok = clean or ok
    info["eligible"] = len(ok)
    return ok, info


# ---------------------------------------------------------------- loops: the bed's own rules (BATCH1_BRIEF §3.2)

def loop_measures(path: Path) -> dict:
    """No clear period at 5-15 Hz (envelope autocorrelation at 60-220 ms under 0.3); 1-4 kHz at least 18 dB under
    100-500 Hz (the bed must leave the spoken word alone)."""
    import soundfile as sf
    from critic import audio as A

    x, sr = sf.read(str(path), always_2d=True, dtype="float64")
    m = x.mean(axis=1)
    m2 = np.concatenate([m, m])                     # the loop as it plays: once round
    hop, win = int(0.005 * sr), int(0.010 * sr)
    c = np.concatenate([[0.0], np.cumsum(m2 ** 2)])
    s = np.arange(0, m2.size - win, hop)
    e = np.sqrt((c[s + win] - c[s]) / win)
    e = e - e.mean()
    ac = np.correlate(e, e, "full")[e.size - 1:]
    ac = ac / (ac[0] or 1.0)
    lags = np.arange(ac.size) * 5
    sel = (lags >= 60) & (lags <= 220)
    k = int(np.argmax(ac[sel]))
    v = float(np.sum(A.band(m, sr, 100, 500) ** 2)) / (float(np.sum(A.band(m, sr, 1000, 4000) ** 2)) + 1e-14)
    out = {"period_ac": round(float(ac[sel][k]), 2), "period_lag_ms": int(lags[sel][k]),
           "low_over_voice_db": round(10 * np.log10(v), 1)}
    out["ok"] = out["period_ac"] < 0.3 and out["low_over_voice_db"] >= 18.0
    return out


def split_loop_recipe(run: str) -> dict | None:
    """The model beds keep their hum under 600 Hz and only a quiet 3-8 kHz clatter (the voice band stays free)."""
    rows = []
    for p in sorted((id_dir("gun.xung.loop", run) / "processed").glob("*.proc.json")):
        d = json.loads(p.read_text("utf-8"))
        if not (d.get("loop") or {}).get("seam_ok"):
            continue
        rows.append((loop_measures(p.with_name(p.name.replace(".proc.json", ".wav")))["period_ac"], d))
    rows = [d for a, d in sorted(rows, key=lambda r: r[0]) if a < 0.3][:4]
    if not rows:
        return None
    src = [gen_src({"file": d["source_f32"], "record": d["raw_record"], "window": d["window_raw_s"]}) for d in rows]
    return _recipe(
        "gun.xung.loop.split", "ambience", "ban",
        "Lô 1 (BATCH1_BRIEF §3.2): nền liên thanh từ bản Stable Audio 3 dài 10 s (4 bản ít chu kỳ nhất ở 5–15 Hz: "
        + ", ".join(d["candidate"] for d in rows) + "), cùng đoạn 3,0 s mà process.py đã chọn, tách hai lớp: ù và động cơ "
        "dưới 600 Hz, lách cách 3–8 kHz nhỏ hơn 16 dB; dải 1–4 kHz gần như trống để giọng đọc không bị che. Nối thành vòng 2,5 s.",
        [_cycle({"id": "hum", "role": "body", "filters": [{"type": "highpass", "hz": 55}, {"type": "lowpass", "hz": 600, "order": 4}]},
                [_j(s) for s in src]),
         _cycle({"id": "clatter", "role": "sweetener", "gainDb": -16,
                 "filters": [{"type": "highpass", "hz": 3000, "order": 4}, {"type": "lowpass", "hz": 8000, "order": 2}]},
                [_j(s) for s in src])],
        {"dcHpfHz": 35, "loopCrossfadeMs": 500, "normalise": {"mode": "lufs-i", "target": -26},
         "limiter": {"ceilingDbtp": -1.0, "maxGrDb": 3}}, len(rows), 2512, "sfx/guns/gun-xung-loop", loop=True)


def split2_loop_recipe(run: str) -> dict | None:
    """The split bed again with its clatter moved to 5.5-9 kHz: the 3-8 kHz clatter of the first split carried pitched
    chirps at 2-4 kHz (L1b loop_signature at 2.0, 2.9, 4.2 kHz) that come back every round of the loop."""
    rec = split_loop_recipe(run)
    if not rec:
        return None
    rec = _j(rec)
    rec["id"] = "gun.xung.loop.split2"
    rec["variants"]["seed"] = 2513
    for lay in rec["layers"]:
        if lay["id"] == "clatter":
            lay["gainDb"] = -18
            lay["filters"] = [{"type": "highpass", "hz": 5500, "order": 8}, {"type": "lowpass", "hz": 9000, "order": 2}]
    rec["description"] = rec["description"].replace("lách cách 3–8 kHz nhỏ hơn 16 dB", "lách cách dời lên 5,5–9 kHz, nhỏ "
                                                    "hơn 18 dB (bản tách đầu có tiếng chíp có cao độ 2–4 kHz lặp lại mỗi vòng)")
    return rec


# kill.swarm, direction "shatter with a short ring" (prompts C, D): the model takes start mid-sound (onset not verified),
# so the card's first source (source_plan rank 1: Kenney Impact head, Stable Audio 3 body and tail) is built from them
SWARM_RING = ("C__s2001", "D__s2002", "C__s2004", "D__s2005", "C__s2005", "D__s2006")
SWARM_HEADS = ("impactMetal_light_002", "impactPlate_light_001", "impactTin_medium_002", "impactMetal_light_004",
               "impactPlate_light_003", "impactTin_medium_004")
SWARM_BODY_S = 0.26


def swarm_recipe(run: str) -> dict | None:
    from common.batch1_dh import body_window

    raw = id_dir("kill.swarm", run) / "raw"
    bodies = []
    for tag in SWARM_RING:
        f = raw / f"kill.swarm__{tag}.f32.wav"
        if not f.is_file():
            continue
        r = body_window(f, SWARM_BODY_S)
        if r["ok"]:
            bodies.append({"file": str(f), "record": str(f.with_name(f.name.replace(".f32.wav", ".json"))),
                           "window": r["window"], "name": f.name.replace(".f32.wav", "")})
    if not bodies:
        return None
    n = len(bodies)
    return _recipe(
        "kill.swarm.vang", "death-swarm", "chet",
        "Lô 1 (BATCH1_BRIEF #15), hướng 'vỡ có vang': bản Stable Audio 3 prompt C, D (mảnh thép văng, vang ngắn trong sảnh "
        "thép) bắt đầu giữa tiếng nên đầu tiếng chưa xác minh; dựng theo nguồn hạng 1 của thẻ: đầu tiếng Kenney Impact "
        "(Metal light, Plate light, Tin medium; lọc cao 1,5 kHz, 40 ms) trên thân Stable Audio 3 cửa sổ 260 ms từ 4 ms trước "
        "đỉnh (" + ", ".join(b["name"].replace("kill.swarm__", "") for b in bodies) + "), lọc cao 150 Hz, khoét nhẹ 2,5 kHz. "
        "Biến thể n dùng đầu tiếng n và thân n.",
        [_cycle({"id": "head", "role": "attack", "gainDb": -6, "filters": [{"type": "highpass", "hz": 1500}],
                 "trim": {"endMs": 40}, "fadeOutMs": 25}, [lib(h) for h in SWARM_HEADS[:n]]),
         _cycle({"id": "body", "role": "body", "offsetMs": 0.5, "fadeInMs": 2,
                 "filters": [{"type": "highpass", "hz": 150, "order": 2}, {"type": "peak", "hz": 2500, "gainDb": -3, "q": 0.8}]},
                [gen_src(b) for b in bodies])],
        {"dcHpfHz": 35, "headTrim": {"thresholdDb": -50, "preRollMs": 0.3}, "maxLengthMs": 300,
         "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 200}, "normalise": {"mode": "lufs-m-max", "target": -20},
         "limiter": {"ceilingDbtp": -1.0, "releaseMs": 40, "maxGrDb": 6}}, n, 2534, "sfx/kills/kill-swarm")


# hit.t2.kb2: the Kenney head on peak-aligned bodies. The process.py windows of the D takes open 30-50 ms before the
# body's own clank, so hit.t2.kb v2-v6 carry a second hit 32-62 ms after the head, 0-4 dB louder above 1 kHz (a flam
# the critic's double-onset test does not catch: no dip between the two). Windows from 4 ms before the loudest 5 ms.
T2_KB2 = ("A__s2002", "B__s2005", "D__s2005", "A__s2003", "B__s2001", "D__s2004")


def t2_kb2_recipe(run: str) -> dict | None:
    from common.batch1_dh import body_window

    raw = id_dir("hit.t2", run) / "raw"
    bodies = []
    for tag in T2_KB2:
        f = raw / f"hit.t2__{tag}.f32.wav"
        r = body_window(f, 0.192) if f.is_file() else {"ok": False}
        if r["ok"]:
            bodies.append({"file": str(f), "record": str(f.with_name(f.name.replace(".f32.wav", ".json"))),
                           "window": r["window"], "name": f.name.replace(".f32.wav", "")})
    if not bodies:
        return None
    data = json.loads(recipe_path("hit.t2.kb").read_text("utf-8"))
    data = _j(data)
    data["id"] = "hit.t2.kb2"
    n = len(bodies)
    data["variants"]["count"] = n
    data["variants"]["seed"] = 2525
    for lay in data["layers"]:
        if lay["id"] == "front":
            pool = [lay["source"], *lay.get("vary", {}).get("swap", [])]
            _cycle(lay, (pool * 2)[:n])
        elif lay["id"] == "body":
            lay.pop("vary", None)
            _cycle(lay, [gen_src(b) for b in bodies])
    data["description"] = (
        "Lô 1 (BATCH1_BRIEF #13), nghe ghép sẵn: đầu tiếng Kenney Impact Metal heavy (lọc cao 700 Hz, 45 ms) trên thân "
        "Stable Audio 3 lọc 120 Hz–2 kHz, cửa sổ từ 4 ms trước đỉnh của thân (" + ", ".join(b["name"].replace("hit.t2__", "")
                                                                                     for b in bodies)
        + ") để đầu tiếng Kenney rơi đúng cú gõ của thân; cộng hit.sub v1 nhỏ hơn 9 dB. Bản kb trước dùng cửa sổ của "
        "process.py: thân họ D gõ 32–62 ms sau đầu tiếng (gõ đúp). Biến thể n dùng đầu tiếng n và thân n.")
    return data


def step_t2(run: str, force: bool = False) -> None:
    """hit.t2: the peak-aligned Kenney recipe, scored in one run with the raw recipe, the first Kenney recipe and 0a v2."""
    rec = t2_kb2_recipe(run)
    if rec:
        render_recipes({"hit.t2.kb2": rec}, run, force)
    out = critic_out(run, "t2")
    if (out / "_batch.json").is_file() and not force:
        _say(f"critic t2: đã có {out}")
        return
    rids = ("hit.t2.raw", "hit.t2.kb", "hit.t2.kb2")
    ins = [recipe_run(r, run) / "masters" for r in rids if (recipe_run(r, run) / "masters").is_dir()] + [REF_0A["hit.t2"]]
    srcs = [recipe_run(r, run) / "SOURCES.json" for r in rids] + [REF_0A["hit.t2"].parent.parent / "SOURCES.json"]
    wait_heavy_free("critic t2")
    _say(f"critic hit.t2 (thô, kb, kb2, 0a v2): mã {_critic_run(ins, srcs, out, LAB / 'specs' / GAME)}")


# word.load.kn2: the Kenney layers trimmed to their own hits. metalClick.ogg holds ~88 ms of lead-in noise and two
# clicks (100 ms, 272 ms), metalLatch.ogg ~40 ms of lead-in before its hit at 44 ms; word.load.kn trimmed only the end,
# so its 'ka' was the lead-in noise and its main hit (the latch) landed ~95 ms after the word.
def load_kn2_recipe(run: str) -> dict | None:
    p = recipe_path("word.load.kn")
    if not p.is_file():
        return None
    data = _j(json.loads(p.read_text("utf-8")))
    data["id"] = "word.load.kn2"
    data["variants"]["seed"] = 2535
    for lay in data["layers"]:
        if lay["id"] == "ka":                    # the first click at ~100 ms of the file, as loud as the latch
            lay["trim"] = {"startMs": 97, "endMs": 150}
            lay["fadeOutMs"] = 30
            lay["gainDb"] = 2
        elif lay["id"] == "chunk":               # the latch hit at ~44 ms of the file, 52 ms after the click; short
            lay["trim"] = {"startMs": 41, "endMs": 150}  # tail so 1-4 kHz falls by 100 ms (plan §6.2)
            lay["offsetMs"] = 52
            lay["fadeOutMs"] = 70
        elif lay["id"] == "body":
            lay["offsetMs"] = 50
    data["description"] = (
        "Lô 1 (BATCH1_BRIEF #17), hướng 2 sửa lại: 'ka' là tiếng tách đầu của Kenney RPG metalClick (cắt từ 97 ms của file, "
        "lọc cao 1 kHz), 'chunk' là cú chốt của metalLatch (cắt từ 41 ms của file) 52 ms sau, dưới đó thân Stable Audio 3 lọc "
        "thấp 900 Hz. Bản kn trước chỉ cắt đuôi nên 'ka' là đoạn nhiễu dẫn của file và cú chính tới muộn khoảng 95 ms.")
    return data


def step_load(run: str, force: bool = False) -> None:
    """word.load: the trimmed Kenney recipe, scored in one run with every model take and the first Kenney recipe."""
    rec = load_kn2_recipe(run)
    if rec:
        render_recipes({"word.load.kn2": rec}, run, force)
    out = critic_out(run, "load")
    if (out / "_batch.json").is_file() and not force:
        _say(f"critic load: đã có {out}")
        return
    rids = ("word.load.kn", "word.load.kn2")
    ins = [id_dir("word.load", run) / "processed"] + [recipe_run(r, run) / "masters" for r in rids
                                                       if (recipe_run(r, run) / "masters").is_dir()]
    srcs = [id_dir("word.load", run) / "processed" / "SOURCES.json"] + [recipe_run(r, run) / "SOURCES.json" for r in rids]
    wait_heavy_free("critic load")
    _say(f"critic word.load (bản thô, kn, kn2): mã {_critic_run(ins, srcs, out, LAB / 'specs' / GAME)}")


# hurt.breach.b2: the first recipe has no hit (the model's boom swells: 10-90 % rise 83-125 ms, punch under 1 dB) and
# 340 ms of 1-4 kHz sustain (L2 sustain_1k4k). b2 adds a steel hit and a sub boom at 0 ms and keeps the groan and the
# siren under 1.2 kHz.
def breach_b2_recipe(run: str) -> dict | None:
    p = recipe_path("hurt.breach")
    if not p.is_file():
        return None
    data = _j(json.loads(p.read_text("utf-8")))
    data["id"] = "hurt.breach.b2"
    data["variants"]["seed"] = 2536
    n = data["variants"]["count"]
    heads = [lib(f"impactPlate_heavy_00{k}") for k in (0, 2, 4)][:n]
    layers = [_cycle({"id": "hit", "role": "attack", "gainDb": -3, "filters": [{"type": "lowpass", "hz": 2500, "order": 2}],
                      "trim": {"endMs": 120}, "fadeOutMs": 60}, heads),
              {"id": "boom", "role": "sub", "gainDb": -9, "source": {"synth": "sub_thump", "params": {
                  "startHz": 70, "endHz": 38, "glideMs": 120, "durMs": 300, "decayMs": 280, "driveDb": 6}}}]
    for lay in data["layers"]:
        if lay["id"] == "body":
            lay["offsetMs"] = 10
            lay["filters"] = [{"type": "highpass", "hz": 40, "order": 2}, {"type": "lowpass", "hz": 1200, "order": 4}]
        elif lay["id"].startswith("siren"):
            lay["filters"] = [{"type": "lowpass", "hz": 1000, "order": 8}]
        layers.append(lay)
    data["layers"] = layers
    data["description"] = (
        "Lô 1 (BATCH1_BRIEF #20), bản 2: thêm cú đập thép Kenney Impact Plate heavy (lọc thấp 2,5 kHz) và tiếng nổ trầm "
        "tổng hợp (70→38 Hz, 300 ms) ở 0 ms; thân Stable Audio 3 (thép rên) lọc 40 Hz–1,2 kHz; còi hai nốt 440/330 Hz lọc "
        "thấp 1 kHz. Bản 1 không có cú đập (tiếng nổ của mô hình lớn dần 83–125 ms) và ngân 340 ms ở 1–4 kHz.")
    return data


def step_breach(run: str, force: bool = False) -> None:
    rec = breach_b2_recipe(run)
    if rec:
        render_recipes({"hurt.breach.b2": rec}, run, force)
    out = critic_out(run, "breach")
    if (out / "_batch.json").is_file() and not force:
        _say(f"critic breach: đã có {out}")
        return
    rids = ("hurt.breach", "hurt.breach.b2")
    ins = [recipe_run(r, run) / "masters" for r in rids if (recipe_run(r, run) / "masters").is_dir()]
    srcs = [recipe_run(r, run) / "SOURCES.json" for r in rids]
    wait_heavy_free("critic breach")
    _say(f"critic hurt.breach (b1, b2): mã {_critic_run(ins, srcs, out, LAB / 'specs' / GAME)}")


def step_kills(run: str, force: bool = False) -> None:
    """kill.swarm: the ring direction as a recipe, scored in one run with every model take so the ranks compare."""
    rec = swarm_recipe(run)
    if rec:
        render_recipes({"kill.swarm.vang": rec}, run, force)
    out = critic_out(run, "kills")
    if (out / "_batch.json").is_file() and not force:
        _say(f"critic kills: đã có {out}")
        return
    ins = [id_dir("kill.swarm", run) / "processed"] + ([recipe_run("kill.swarm.vang", run) / "masters"] if rec else [])
    srcs = [id_dir("kill.swarm", run) / "processed" / "SOURCES.json", recipe_run("kill.swarm.vang", run) / "SOURCES.json"]
    wait_heavy_free("critic kills")
    _say(f"critic kill.swarm (bản thô + vỡ có vang): mã {_critic_run(ins, srcs, out, LAB / 'specs' / GAME)}")


def step_loops(run: str, force: bool = False) -> None:
    """Every bed candidate scored in one run (model takes, library recipe, split recipes), so their ranks compare; the
    ceasefire tails with them (the first final run read the tail card's 550 ms target +-20 %, not its 400-700 ms range)."""
    rec = split_loop_recipe(run)
    if rec:
        render_recipes({"gun.xung.loop.split": rec, "gun.xung.loop.split2": split2_loop_recipe(run)}, run, force)
    out = critic_out(run, "loops")
    if (out / "_batch.json").is_file() and not force:
        _say(f"critic loops: đã có {out}")
        return
    rids = ("gun.xung.loop.lib", "gun.xung.loop.split", "gun.xung.loop.split2", "gun.xung.tail.smp")
    ins = [id_dir(s, run) / "processed" for s in ("gun.xung.loop", "gun.xung.tail")] + \
        [recipe_run(r, run) / "masters" for r in rids if (recipe_run(r, run) / "masters").is_dir()]
    srcs = [id_dir(s, run) / "processed" / "SOURCES.json" for s in ("gun.xung.loop", "gun.xung.tail")] + \
        [recipe_run(r, run) / "SOURCES.json" for r in rids]
    wait_heavy_free("critic loops")
    _say(f"critic nền + đuôi ngừng bắn: mã {_critic_run(ins, srcs, out, LAB / 'specs' / GAME)}")


# ---------------------------------------------------------------- step 6: stage 2 (needs the machine's top first)

def _layers_of(rid: str, n: int) -> list[dict]:
    """The layers of variant n of a stage-1 recipe with every cycled source fixed to that variant's (no vary)."""
    data = json.loads(recipe_path(rid).read_text("utf-8"))
    out = []
    for lay in data["layers"]:
        lay = _j(lay)
        v = lay.pop("vary", None) or {}
        if v.get("swapMode") == "cycle" and v.get("swap"):
            pool = [lay["source"], *v["swap"]]
            lay["source"] = pool[(n - 1) % len(pool)]
        out.append(lay)
    return out, data


def step_stage2(run: str, force: bool = False) -> None:
    docs = _docs(critic_out(run, "final"))
    t2docs = _docs(critic_out(run, "t2")) or docs
    t2, _ = eligible(t2docs, "hit.t2")
    t2 = [d for d in t2 if _kind(d) == "recipe"]
    t4, _ = eligible(docs, "hit.t4")
    wl, _ = eligible(_docs(critic_out(run, "load")) or docs, "word.load")
    rec = {}
    if t2:
        top = t2[0]
        n = int(top["file"]["stem"].rsplit("-v", 1)[1])
        lays, data = _layers_of(_rid(top), n)
        lays = [l for l in lays if l["id"] != "sub"]
        sub = {"id": "sub", "role": "sub", "source": _j(SUB_V[0]), "gainDb": SUB_IN_T2_DB,
               "vary": {"swapMode": "cycle", "swap": [_j(SUB_V[1])]}}
        rec["hit.sub.mix"] = _recipe(
            "hit.sub.mix", "generic", "trung",
            f"Lô 1 (BATCH1_BRIEF #13): hai bản thử của hit.sub dưới cùng một đầu tiếng + thân T2 (bản máy xếp đầu: "
            f"{top['file']['stem']}). Biến thể 1: sub v1 (85→45 Hz, 90 ms, bão hòa 3 dB); 2: sub v2 (72→42 Hz, 110 ms, 6 dB).",
            [*lays, sub], data["chain"], 2, 2540, "sfx/hits/hit-sub-mix")
    if t4:
        top = t4[0]
        n = int(top["file"]["stem"].rsplit("-v", 1)[1])
        lays, data = _layers_of(_rid(top), n)
        head = [l for l in lays if not l["id"].startswith("tail-")]
        tl = [tail_layers(k) for k in range(3)]
        tails = []
        for i in range(3):
            lay = dict(_j(tl[0][i]), id=f"tail-{tl[0][i]['id']}", offsetMs=15)
            lay["vary"] = {"swapMode": "cycle", "swap": [tl[1][i]["source"], tl[2][i]["source"]]}
            tails.append(lay)
        silent = {"synth": "noise_burst", "params": {"durMs": 1, "decayMs": 1}}
        tails.append(dict(_j(tl[2][3]), id="tail-ring2", offsetMs=15, source=silent,
                          vary={"swapMode": "cycle", "swap": [silent, tl[2][3]["source"]]}))
        rec["hit.tail.mix"] = _recipe(
            "hit.tail.mix", "generic", "trung",
            f"Lô 1 (BATCH1_BRIEF #14): ba bản thử của hit.tail dưới cùng một đầu tiếng + thân T4 và hit.sub v1 (bản máy xếp "
            f"đầu: {top['file']['stem']}). Biến thể 1: Anvil; 2: Brake Drum; 3: cả hai, tối hơn.",
            [*head, *tails], data["chain"], 3, 2541, "sfx/hits/hit-tail-mix")
    if wl:
        top = wl[0]
        if _kind(top) == "recipe":
            n = int(top["file"]["stem"].rsplit("-v", 1)[1])
            base, _ = _layers_of(_rid(top), n)
        else:
            p = _proc(top)
            base = [{"id": "load", "role": "body", "source": gen_src({"file": p["source_f32"], "record": p["raw_record"],
                                                                      "window": p["window_raw_s"]})}]
        whine = [{"synth": "tone", "params": {"wave": "saw", "freqHz": 280, "endHz": 880, "glideMs": 260, "durMs": 300,
                                              "attackMs": 30, "decayMs": 500}},
                 {"synth": "tone", "params": {"wave": "sine", "freqHz": 4600, "endHz": 7200, "glideMs": 260, "durMs": 300,
                                              "attackMs": 30, "decayMs": 500}}]
        sparks = [{"id": f"spark{i}", "role": "sweetener", "offsetMs": off, "gainDb": g, "source": {"synth": "click", "params": {
            "durMs": 2, "hpHz": 5200, "lpHz": 12000}}, "vary": {"offsetMs": [-20, 20]}}
                  for i, (off, g) in enumerate(((190, -20), (260, -23), (330, -25), (400, -28)))]
        rec["word.perfect"] = _recipe(
            "word.perfect", "reward", "thuong",
            f"Lô 1 (BATCH1_BRIEF #18): word.load (bản máy xếp đầu: {top['file']['stem']}) cộng tiếng nạp điện rít lên, đặt ngoài "
            "dải giọng: biến thể 1 dưới 1 kHz (răng cưa 280→880 Hz, lọc thấp 1 kHz), biến thể 2 trên 4 kHz (sine 4,6→7,2 kHz); "
            "bốn tia lửa trên 5 kHz.",
            [*base, {"id": "whine", "role": "sweetener", "offsetMs": 90, "gainDb": -12, "source": whine[0],
                     "filters": [{"type": "lowpass", "hz": 1000, "order": 4}],
                     "vary": {"swapMode": "cycle", "swap": [whine[1]]}}, *sparks],
            {"dcHpfHz": 35, "headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": 520,
             "tail": {"floorDb": -60, "shape": "exp", "kneeMs": 380}, "normalise": {"mode": "lufs-m-max", "target": -20},
             "limiter": {"ceilingDbtp": -1.0, "releaseMs": 60, "maxGrDb": 6}}, 2, 2542, "sfx/words/word-perfect")
    render_recipes(rec, run, force)
    out = critic_out(run, "stage2")
    if (out / "_batch.json").is_file() and not force:
        _say(f"critic stage2: đã có {out}")
        return
    ins = [recipe_run(r, run) / "masters" for r in rec]
    wait_heavy_free("critic stage2")
    _say(f"critic stage2 ({', '.join(rec)}): mã {_critic_run(ins, [recipe_run(r, run) / 'SOURCES.json' for r in rec], out, LAB / 'specs' / GAME)}")


# ---------------------------------------------------------------- step 7: listening lists

DIRECTIONS = {"d1": ("gun.xung.d1a", "gun.xung.d1b", 16.0), "d2": ("gun.xung.d2a", "gun.xung.d2b", 16.0),
              "d3": ("gun.xung.d2a", "gun.xung.d2b", 11.0)}
KILL_DIRS = {"kho": ("A", "B"), "vang": ("C", "D")}      # kill.swarm: dry shatter / shatter with a short ring
LOAD_DIRS = {"sa3": "sa3", "kenney": "recipe"}          # word.load: model take / Kenney latch on a model body


def _kill_dir(d: dict) -> str:
    """kill.swarm direction: 'vang' (prompts C, D; the ring recipe built on them) or 'kho' (prompts A, B)."""
    if _rid(d) == "kill.swarm.vang":
        return "vang"
    return next((k for k, v in KILL_DIRS.items() if _prompt(d) in v), "kho")


def _pick(docs: list[dict], role: str, note: str | None = None) -> dict:
    return {"docs": docs, "role": role, "note": note}


def _set_docs(docs: dict[str, dict], rid: str) -> list[dict]:
    """A gun set: the variants of one recipe that pass L1 with no flag that keeps a take out of a session."""
    mine = sorted([d for d in docs.values() if _rid(d) == rid], key=lambda d: d["file"]["stem"])
    return [d for d in mine if d["verdict"] == "PASS" and not _flags(d) & NO_PICK_FLAGS]


def select(run: str) -> dict[str, dict]:
    docs = _docs(critic_out(run, "final"))
    s2 = _docs(critic_out(run, "stage2"))
    loops_docs = _docs(critic_out(run, "loops"))
    kills_docs = _docs(critic_out(run, "kills"))
    t2_docs = _docs(critic_out(run, "t2"))
    load_docs = _docs(critic_out(run, "load"))
    breach_docs = _docs(critic_out(run, "breach"))
    sel: dict[str, dict] = {}
    # gun.xung: three directions, each a whole set (A and B alternate), and 0a v2 as the game plays it today
    sets = {rid: _set_docs(docs, rid) for rid in ("gun.xung.d1a", "gun.xung.d1b", "gun.xung.d2a", "gun.xung.d2b")}
    allg = [d for d in docs.values() if _sid(d) == "gun.xung"]
    g = {"n": len(allg), "pass": sum(1 for d in allg if d["verdict"] == "PASS"), "picks": [],
         "sets": {k: [d["file"]["stem"] for d in v] for k, v in sets.items()}}
    for key, (ra, rb, bed) in DIRECTIONS.items():
        a, b = sets[ra], sets[rb]
        files = [x for pair in zip(a, b) for x in pair] + a[len(b):] + b[len(a):]
        if key == "d3":
            files = [x for pair in zip(b, a) for x in pair] + b[len(a):] + a[len(b):]
        note = "Cùng phát đơn với một bản khác; chỉ khác mức nền trong 'Liên thanh 3 s'" if key in ("d2", "d3") else None
        g["picks"].append({"docs": files, "role": f"direction-{key[1]}", "note": note, "set": {"A": a, "B": b}, "bed_db": bed})
    ref = [d for d in allg if d["file"]["path"] == str(REF_0A["gun.xung"])]
    if ref:
        g["picks"].append(_pick(ref, "ref-0a-current", "Cách game đang phát: chỉ viên chẵn, không nền, không đuôi"))
    sel["gun.xung"] = g
    for sid in IDS:
        if sid == "gun.xung":
            continue
        pool = s2 if sid in ("hit.sub", "hit.tail", "word.perfect") else docs
        if sid in ("gun.xung.loop", "gun.xung.tail") and loops_docs:
            pool = loops_docs     # one run with the split beds and the tail card's corrected length (see step_loops)
        if sid == "kill.swarm" and kills_docs:
            pool = kills_docs     # one run with the ring recipe (see step_kills)
        if sid == "hit.t2" and t2_docs:
            pool = t2_docs        # one run with the peak-aligned Kenney recipe (see step_t2)
        if sid == "word.load" and load_docs:
            pool = load_docs      # one run with the trimmed Kenney recipe (see step_load)
        if sid == "hurt.breach" and breach_docs:
            pool = breach_docs    # one run with the recipe that has a hit (see step_breach)
        if sid in ("hit.sub", "hit.tail"):
            ok, info = eligible({k: v for k, v in pool.items() if ".mix-" in k}, sid)
        else:
            ok, info = eligible(pool, sid)
        if sid == "gun.xung.loop":
            lm = {d["file"]["stem"]: loop_measures(Path(d["file"]["path"])) for d in ok}
            info["loop_rules"] = lm
            good = [d for d in ok if lm[d["file"]["stem"]]["ok"]]
            info["loop_rules_pass"] = len(good)
            ok = good or ok
        e = {**info, "picks": []}
        if not ok:
            sel[sid] = e
            continue
        top = ok[0]
        picks = [_pick([top], "top")]
        used = {top["file"]["stem"]}
        if sid in ("hit.sub", "hit.tail", "word.perfect", "hurt.breach"):
            picks = [_pick([d], ("top", "distinct", "other")[i]) for i, d in enumerate(ok[:3])]
        elif sid == "gun.xung.loop":
            # the best bed that keeps the brief's own rules (no 5-15 Hz period, voice band 18 dB down), even when the
            # L1b loop-signature detector flags it: shown with its flag, as the rule-blocked howl was in batch 0b
            allp = sorted([d for d in pool.values() if _sid(d) == sid and d["verdict"] == "PASS" and _kind(d) != "ref"
                           and not _flags(d) & (BED_NO_PICK - {"loop_signature"})], key=_rank)
            rule = [d for d in allp if d["file"]["stem"] not in used and loop_measures(Path(d["file"]["path"]))["ok"]]
            if rule:
                d = rule[0]
                lm = loop_measures(Path(d["file"]["path"]))
                info["loop_rules"][d["file"]["stem"]] = lm
                note = None
                if "loop_signature" in _flags(d):
                    note = "Máy gắn cờ 'dấu vòng lặp' (tiếng có cao độ rất nhỏ). Anh có nghe ra không?"
                picks.append(_pick([d], "rule-pass", note))
                used.add(d["file"]["stem"])
            other = [d for d in ok if _kind(d) == "recipe" and d["file"]["stem"] not in used]
            if other:
                picks.append(_pick([other[0]], "other-source"))
        elif sid == "kill.swarm":
            mine = _kill_dir(top)
            other = [d for d in ok if _kill_dir(d) != mine]
            if other:
                picks.append(_pick([other[0]], "direction-2"))
            dis = _distinct(top, [d for d in _upper(ok) if d["file"]["stem"] not in {p["docs"][0]["file"]["stem"] for p in picks}])
            if dis is not None:
                picks.append(_pick([dis], "distinct"))
        elif sid in ("word.load", "kill.elite", "gun.xung.loop", "gun.xung.tail", "hit.t2"):
            # the best of the other source (model take vs recipe), then the most different of the upper half
            other = [d for d in ok if (_kind(d) == "recipe") != (_kind(top) == "recipe") and _kind(d) != "ref"]
            if sid == "hit.t2":
                other = [d for d in ok if _rid(d) and _rid(d) != _rid(top)]
            if other:
                picks.append(_pick([other[0]], "direction-2" if sid == "word.load" else "other-source"))
            seen = {p["docs"][0]["file"]["stem"] for p in picks}
            dis = _distinct(top, [d for d in _upper(ok) if d["file"]["stem"] not in seen])
            if dis is not None:
                picks.append(_pick([dis], "distinct"))
            if sid == "hit.t2":
                ref = [d for d in pool.values() if d["file"]["path"] == str(REF_0A["hit.t2"])]
                if ref:
                    picks.append(_pick(ref, "ref-0a"))
        else:
            dis = _distinct(top, _upper(ok))
            if dis is not None:
                picks.append(_pick([dis], "distinct"))
        if sid == "hit.t1":
            ref = [d for d in ok if d["file"]["stem"] == "hit.t1__C__s1006"]
            if ref and ref[0]["file"]["stem"] not in {p["docs"][0]["file"]["stem"] for p in picks}:
                picks.append(_pick(ref, "ref-0b", None))
        if sid in PROBE_IDS:
            pr = _probe(sid, ok, {p["docs"][0]["file"]["stem"] for p in picks})
            if pr is not None:
                picks.append(_pick([pr], "probe"))
        e["picks"] = picks
        sel[sid] = e
    return sel


# ---------------------------------------------------------------- step 8: in-game context renders

SCENARIO = {"gun.xung": "ts-xung-3s", "gun.xung.loop": "ts-xung-3s", "gun.xung.tail": "ts-xung-3s", "hit.t1": "ts-xung-3s",
            "hit.t2": "ts-xung-3s", "hit.sub": "ts-xung-3s", "hit.t4": "ts-xung-3s", "hit.tail": "ts-xung-3s",
            "kill.swarm": "ts-xung-3s-kills", "kill.elite": "ts-xung-3s-kills", "word.load": "ts-xung-3s-kills",
            "word.perfect": "ts-xung-3s-kills", "gun.tia.pulse": "ts-tia-3s", "hurt.breach": "ts-breach"}
CTX_KEY = {sid: ("scene" if sid == "hurt.breach" else "burst") for sid in SCENARIO}
SLOT = {"hit.sub": "hit.t2", "hit.tail": "hit.t4"}      # the pre-mixes play where the game plays the tier


def ctx_dir(run: str) -> Path:
    return base_dir(run) / "context"


def fixed_slots(sel: dict) -> tuple[dict, str]:
    """Every slot a render does not test: this batch's top (the gun: the direction with the better burst numbers)."""
    out: dict = {}
    for sid in IDS:
        if sid in ("gun.xung", "hit.sub", "hit.tail"):
            continue
        picks = sel.get(sid, {}).get("picks") or []
        if picks:
            out[SLOT.get(sid, sid)] = [Path(picks[0]["docs"][0]["file"]["path"])]
    best, key = None, "d2"
    for p in sel["gun.xung"]["picks"]:
        if p.get("set") and p["role"] in ("direction-1", "direction-2"):
            st = {"A": [Path(d["file"]["path"]) for d in p["set"]["A"]], "B": [Path(d["file"]["path"]) for d in p["set"]["B"]]}
            from context import ts_scenes
            sc_, dur = ts_scenes.build("ts-xung-3s", {**out, "gun.xung": st}, "proposed")
            b = ts_scenes.burst_numbers(ts_scenes.render_mix(sc_, dur), sc_)
            passes = sum(1 for k, v in b.items() if k.endswith("_pass") and v)
            cand = (passes, -(b.get("dip_median_db") or 99))
            if best is None or cand > best[0]:
                best = (cand, st, p["role"])
    if best:
        out["gun.xung"] = best[1]
        key = best[2]
    return out, key


def step_context(run: str, force: bool = False) -> dict:
    from context import ts_scenes

    sel = select(run)
    fixed, gun_dir = fixed_slots(sel)
    done: dict = {"fixed": {k: ({kk: [str(x) for x in vv] for kk, vv in v.items()} if isinstance(v, dict) else [str(x) for x in v])
                            for k, v in fixed.items()}, "fixed_gun_direction": gun_dir, "renders": {}}
    for sid in IDS:
        for p in sel[sid]["picks"]:
            d0 = p["docs"][0]
            name = p["role"] if sid == "gun.xung" else d0["file"]["stem"]
            out = ctx_dir(run) / sid / f"{name}.wav"
            config, bed = "proposed", 16.0
            slots = dict(fixed)
            if sid == "gun.xung":
                if p.get("set"):
                    slots["gun.xung"] = {"A": [Path(d["file"]["path"]) for d in p["set"]["A"]],
                                         "B": [Path(d["file"]["path"]) for d in p["set"]["B"]]}
                    bed = p["bed_db"]
                else:
                    slots["gun.xung"] = [Path(d0["file"]["path"])]
                    config = "current"
            else:
                slots[SLOT.get(sid, sid)] = [Path(d0["file"]["path"])]
                if sid == "gun.xung.loop":
                    bed = 11.0            # loud enough to tell the beds apart; the gun item asks 16 vs 11 dB
            if out.is_file() and out.with_suffix(".json").is_file() and not force:
                doc = json.loads(out.with_suffix(".json").read_text("utf-8"))
            else:
                doc = ts_scenes.render(SCENARIO[sid], slots, out, focus=SLOT.get(sid, sid), config=config, bed_db=bed)
            p["ctx"] = out
            done["renders"].setdefault(sid, {})[name] = {"file": str(out), "role": p["role"], "config": config,
                                                         "bed_db": bed, "metrics": doc["metrics"]}
            b = doc["metrics"].get("burst") or {}
            _say(f"context {sid} {name}: {SCENARIO[sid]} {config}, hổng {b.get('gap_time_pct')} %, trũng "
                 f"{b.get('dip_median_db')} dB, giọng min {(doc['metrics'].get('voice') or {}).get('min_db')} dB")
    (ctx_dir(run) / "context.json").write_text(json.dumps(done, ensure_ascii=False, indent=1, default=float), "utf-8")
    return done


# ---------------------------------------------------------------- step 9: board sessions

DESC = {
    "gun.xung": "Súng Xung, pháo tự động bắn 10 viên mỗi giây. Mỗi bản là một bộ phát đơn (bộ nặng và bộ nhẹ xen nhau). Nghe "
                "'Liên thanh 3 s' trước: có nghe thành một loạt liền, có lực không, hay rời từng phát (nhãn 'ngắt quãng')? "
                "Một bản là cách game đang phát hôm nay. Nghe bằng tai nghe, rồi một lượt bằng loa",
    "gun.xung.loop": "Nền cơ khí chạy suốt loạt bắn (băng đạn, động cơ tháp pháo), nằm dưới tiếng súng. Không được có nhịp riêng "
                     "hay tiếng nổi lên. 'Lặp' phát liền 3 vòng để nghe chỗ nối; 'Liên thanh 3 s' đặt nền to hơn đề xuất "
                     "(thấp hơn phát súng 11 dB) để nghe rõ nền",
    "gun.xung.tail": "Khi súng ngừng bắn: vang thép của sảnh rộng, máy dừng. Không được nghe như bị cắt",
    "hit.t1": "Đạn Xung trúng vỏ thép, tới 10 lần mỗi giây. Phải sáng, gọn, không che tiếng súng và tiếng đọc từ; "
              "lặp nhiều có nhàm không",
    "hit.t2": "Chí mạng (T2): keng nặng hơn hit.t1, có cú thụi trầm (nghe đã ghép sẵn lớp sub dùng chung). Nghe kỹ có "
              "'gõ đúp' (hai cú gõ sát nhau) không",
    "hit.sub": "Lớp sub dùng chung của bậc trúng: hai bản sub dưới cùng một tiếng chí mạng. Nghe bằng tai nghe và thử 'Loa nhỏ'",
    "hit.t4": "Đòn lớn (T4): thép dầm, trầm, ngân (đã ghép sẵn đủ lớp: đầu, thân, sub, đuôi). Phải to và dài hơn hit.t2 rõ ràng",
    "hit.tail": "Đuôi kim loại dùng chung của đòn lớn: ba bản đuôi dưới cùng một cú T4 (đe, trống phanh, cả hai)",
    "kill.swarm": "Bầy quái kim loại vỡ, hàng trăm lần mỗi trận. Hai hướng: vỡ khô, và vỡ có vang ngắn",
    "kill.elite": "Lính tinh nhuệ nổ: thép xé, nổ trầm, tia điện",
    "word.load": "Gõ xong một từ: nạp băng đạn 'cạch-chắc' (hai nhịp cách nhau khoảng 50 ms là cố ý). Giọng đọc từ phải rõ "
                 "ngay sau. Hai hướng: chốt Kenney hai nhịp trên thân Stable Audio 3, và bản Stable Audio 3 nguyên khối",
    "word.perfect": "Từ gõ chuẩn: nạp đạn cộng tiếng nạp điện rít lên và tia lửa. Tiếng rít đặt dưới 1 kHz hoặc trên 4 kHz",
    "gun.tia.pulse": "Tia điện chích, mỗi nhịp 0,1 s khi Tia trúng quái. 'Liên thanh 3 s': Tia chạy 2,5 s",
    "hurt.breach": "Báo nguy: tuyến bị phá. Cú đập thép, nổ trầm, thép rên, còi hai nốt ngắn. Phải khác hẳn tiếng trúng, và "
                   "đủ rõ để báo nguy giữa trận",
}
CONTEXTS = {"gun.xung": ["burst", "alone", "loop", "small"], "gun.xung.loop": ["loop", "burst", "alone"],
            "gun.xung.tail": ["burst", "alone", "small"], "hit.t1": ["burst", "loop", "alone", "small"],
            "hit.t2": ["burst", "alone", "loop", "small"], "hit.sub": ["alone", "small", "burst"],
            "hit.t4": ["burst", "alone", "small"], "hit.tail": ["alone", "burst", "small"],
            "kill.swarm": ["burst", "loop", "alone", "small"], "kill.elite": ["burst", "alone", "small"],
            "word.load": ["burst", "alone", "loop"], "word.perfect": ["burst", "alone"],
            "gun.tia.pulse": ["burst", "loop", "alone"], "hurt.breach": ["scene", "alone", "small"]}
LOOP = {"gun.xung": {"interval_ms": 100, "count": 30, "cents": 40, "db": 1}, "hit.t1": {"interval_ms": 100, "count": 20},
        "gun.tia.pulse": {"interval_ms": 100, "count": 20}, "kill.swarm": {"interval_ms": 150, "count": 20},
        "hit.t2": {"interval_ms": 400, "count": 8}, "word.load": {"interval_ms": 1400, "count": 6}}
SESSIONS = [("1-ts-s1", "Lô 1 · Tuyến Cuối · súng và trúng (S1)", P1),
            ("1-ts-s4", "Lô 1 · Tuyến Cuối · hạ quái, nạp đạn, Tia, báo nguy (S4)", P4)]


class SessionExists(RuntimeError):
    pass


def _cand(p: dict) -> dict:
    from board import session
    docs = p["docs"]
    def card(d):
        c = d.get("card_blind") or d.get("card")
        return session.display_path(Path(d["_out"]) / c) if c and (Path(d["_out"]) / c).is_file() else None
    if len(docs) == 1:
        d = docs[0]
        c = {"file": session.display_path(Path(d["file"]["path"])), "role": p["role"],
             "critic": session.display_path(Path(d["_out"]) / f"{d['file']['stem']}.json")}
        if card(d):
            c["card"] = card(d)
    else:
        c = {"files": [session.display_path(Path(d["file"]["path"])) for d in docs], "role": p["role"],
             "critics": [session.display_path(Path(d["_out"]) / f"{d['file']['stem']}.json") for d in docs],
             "cards": [card(d) for d in docs]}
    if p.get("note"):
        c["note"] = p["note"]
    return c


def step_session(run: str, force: bool = False) -> list[Path]:
    sel = select(run)
    ctxj = json.loads((ctx_dir(run) / "context.json").read_text("utf-8")) if (ctx_dir(run) / "context.json").is_file() else {}
    paths = []
    for name, title, ids in SESSIONS:
        items = []
        for sid in ids:
            picks = sel[sid]["picks"]
            if not picks:
                _say(f"phiên {name}: {sid} không có bản nào để nghe")
                continue
            cands = []
            for p in picks:
                c = _cand(p)
                key = p["role"] if sid == "gun.xung" else p["docs"][0]["file"]["stem"]
                r = ((ctxj.get("renders") or {}).get(sid) or {}).get(key)
                if r and Path(r["file"]).is_file():
                    from board import session as S
                    c["ctx"] = {CTX_KEY[sid]: S.display_path(Path(r["file"]))}
                cands.append(c)
            sp = picks[0]["docs"][0].get("spec") or {}
            item = {"id": sid, "family": sp.get("family") or "", "group": sp.get("group") or "", "desc": DESC[sid],
                    "probe": any(p["role"] == "probe" for p in picks), "contexts": CONTEXTS[sid], "candidates": cands}
            if sid in LOOPS:
                item["loop"] = {"seamless": True, "count": 3}
            elif sid in LOOP:
                item["loop"] = LOOP[sid]
            else:
                longest = max((d["metrics"].get("duration_ms") or 0) for p in picks for d in p["docs"])
                iv = int(max(1000.0, longest + 300))
                item["loop"] = {"interval_ms": iv, "count": 6}
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
        S.load(path)
        paths.append(path)
        _say(f"phiên {path}: {len(items)} id, {sum(len(i['candidates']) for i in items)} bản (+4 cặp mốc khi mở)")
    return paths


# ---------------------------------------------------------------- step 5b: ledger + release check

def staging_dirs(run: str) -> tuple[Path, Path]:
    root = base_dir(run) / "staging" / GAME
    return root / "art-src" / "audio", root / "public" / "assets" / GAME / "audio"


def step_link(run: str, force: bool = False) -> int:
    from build import critic_link, licence_check, release

    outs = [critic_out(run, n) for n in ("final", "loops", "kills", "t2", "load", "breach", "stage2")
            if critic_out(run, n).is_dir()]
    for sid in CANDIDATE_TAKES:
        p = id_dir(sid, run) / "processed"
        if (p / "SOURCES.json").is_file():
            res = critic_link.apply(p / "SOURCES.json", outs, p / "licences.rows.jsonl")
            _say(f"mark-ai {sid}/processed: {res['steps']} bước, {res['files']} hồ sơ")
    art, pub = staging_dirs(run)
    rids = list(STAGE1) + [r for r in ("gun.xung.loop.split", "gun.xung.loop.split2", "kill.swarm.vang", "hit.t2.kb2",
                                       "word.load.kn2", "hurt.breach.b2", "hit.sub.mix",
                                       "hit.tail.mix", "word.perfect")
                           if (recipe_run(r, run) / "SOURCES.json").is_file()]
    for rid in rids:
        r = recipe_run(rid, run)
        res = critic_link.apply(r / "SOURCES.json", outs, r / "licences.rows.jsonl")
        rel = release.release(r, None, art, pub)
        _say(f"mark-ai {rid}: {res['steps']} bước; cây thử: {len(rel['files'])} file, {rel['rowsAdded']} dòng sổ, "
             f"{len(rel['licenceCopies'])} bản giấy phép")
    rc = licence_check.main(["--art-src", str(art), "--public", str(pub)])
    _say(f"licence-check (cây thử, chỉ công thức) {GAME}: mã {rc}")
    return rc


# ---------------------------------------------------------------- step 10: report

def _fmt(v, nd=1):
    if v is None:
        return "–"
    if isinstance(v, float):
        return f"{v:.{nd}f}".replace(".", ",").replace("-", "−")
    return str(v)


def _pct(v):
    return "–" if v is None else f"{v * 100:.0f} %"


def row(d: dict) -> dict:
    m, s_ = d["metrics"], d.get("score") or {}
    l3 = ((d.get("L3") or {}).get("scores")) or {}
    ast = (((d.get("L4") or {}).get("ast") or {}).get("top5") or [])[:2]
    return {"stem": d["file"]["stem"], "file": d["file"]["path"], "sha8": d["file"].get("sha256", "")[:8],
            "kind": _kind(d), "verdict": d["verdict"], "blocking": d["L1"]["blocking"],
            "rank": s_.get("rank"), "n_ranked": s_.get("n_ranked"), "combined": s_.get("combined"),
            "L2": (d.get("L2") or {}).get("score"), "PQ": l3.get("PQ"),
            "ast": [(a[0], round(float(a[1]), 2)) if isinstance(a, (list, tuple)) else (a.get("label"), round(a.get("score"), 2))
                    for a in ast],
            "flags": sorted(_flags(d)),
            "metrics": {k: m.get(k) for k in ("duration_ms", "attack_ms", "crest_db", "share_below_150", "share_200_800",
                                               "share_1k_4k", "share_above_3k", "centroid_hz", "tail_ms", "voice_drop_db",
                                               "lufs_m_range_db", "speaker_loss_db") if m.get(k) is not None}}


BURST_KEYS = (("gap_time_pct", "hổng %"), ("dip_median_db", "trũng tv"), ("dip_max_db", "trũng max"), ("onset_sd_ms", "nhịp sd ms"),
              ("small_speaker_loss_db", "loa nhỏ"), ("pump_median_db", "bơm"), ("stop_max_drop_10ms_db", "ngừng: tụt 10 ms"))


def step_report(run: str, force: bool = False) -> Path:
    sel = select(run)
    cj = ctx_dir(run) / "context.json"
    ctx = json.loads(cj.read_text("utf-8")) if cj.is_file() else {}
    oj = base_dir(run) / "observations.json"
    obs = json.loads(oj.read_text("utf-8")) if oj.is_file() else {}
    b = json.loads((critic_out(run, "final") / "_batch.json").read_text("utf-8"))
    c = b.get("counts") or {}
    summary = {"run": run, "counts": c, "n_files": b.get("n_files"), "ids": {}, "fixed_slots": ctx.get("fixed"),
               "fixed_gun_direction": ctx.get("fixed_gun_direction")}
    L = ["# Lô 1 · Tuyến Cuối (P1, P4)", "",
         "Tự sinh bởi `common/batch1_ts.py report`. Thẻ ảnh của bộ chấm: `critic-<lần chấm>/<tên>.png` (bản cho Bảng Nghe: "
         "`.blind.png`); lần chấm chung `critic-final`, lần chấm riêng để thứ hạng so được trong một id: `critic-loops` (nền, "
         "đuôi ngừng bắn), `critic-kills` (kill.swarm), `critic-t2` (hit.t2), `critic-load` (word.load), `critic-breach` "
         "(hurt.breach), `critic-stage2` (hit.sub, hit.tail, word.perfect); bản dựng trong bối cảnh: "
         "`context/<id>/<tên>.wav|.png|.json`.", "",
         f"Lần chấm cuối: {b.get('n_files')} file, {c.get('PASS', 0)} ĐẠT, {c.get('BLOCK', 0)} CHẶN, {c.get('NEEDS_FIX', 0)} CẦN SỬA; "
         "hiệu chỉnh owner-v1.", "",
         "Không đưa vào phiên: bản có đầu tiếng chưa xác minh (trừ đuôi và nền, không có đầu tiếng), cờ `double_onset` (trừ "
         "`word.load`, hai nhịp là cố ý) hay `lr_imbalance`; nền có `loop_signature`, `decoder_comb`, `stereo_mismatch` (trừ một "
         "nền đạt luật nền của lô 1, vào phiên với nhãn ghi rõ cờ). Công thức đã có bản sửa (`hit.t2.kb`, `word.load.kn`) chỉ còn "
         "trong báo cáo.", "",
         f"Các chỗ cố định trong bản dựng bối cảnh: bản máy xếp đầu của mỗi id; súng là hướng `{ctx.get('fixed_gun_direction')}` "
         "(hướng có nhiều số đo 'Liên thanh' đạt hơn).", ""]
    if obs.get("_findings"):
        L += ["## Phát hiện", ""] + [f"- {x}" for x in obs["_findings"]] + [""]
    summary["findings"] = obs.get("_findings") or []
    for sid in IDS:
        e = sel[sid]
        rend = (ctx.get("renders") or {}).get(sid) or {}
        L += [f"## `{sid}`", ""]
        if sid == "gun.xung":
            L += [f"{e['n']} phát đơn, {e['pass']} qua L1. Bộ: " + "; ".join(f"{k} {len(v)} bản" for k, v in e["sets"].items()), ""]
        else:
            L += [f"{e.get('n', 0)} bản cuối, {e.get('pass', 0)} qua L1, {e.get('eligible', 0)} được chọn vào danh sách nghe.", ""]
        if (obs.get(sid) or {}).get("_id"):
            L += [obs[sid]["_id"], ""]
        L += ["| Vai trò | Bản | Mã | Loại | L1 | Hạng | Điểm | L2 | PQ | AST | Lên ms | Dài ms | <150 Hz | 1–4 kHz | Cờ |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        rows_out = []
        for p in e["picks"]:
            for d in p["docs"]:
                r_ = row(d)
                r_["role"] = p["role"]
                rows_out.append(r_)
                m = r_["metrics"]
                L.append(f"| {p['role']} | `{r_['stem']}` | {r_['sha8']} | {r_['kind']} | {r_['verdict']} {','.join(r_['blocking'])} | "
                         f"{r_['rank'] or '–'}/{r_['n_ranked'] or '–'} | {_fmt(r_['combined'], 2)} | {_fmt(r_['L2'], 2)} | {_fmt(r_['PQ'], 2)} | "
                         f"{', '.join(f'{a} {s2}' for a, s2 in r_['ast']) or '–'} | {_fmt(m.get('attack_ms'))} | {_fmt(m.get('duration_ms'), 0)} | "
                         f"{_pct(m.get('share_below_150'))} | {_pct(m.get('share_1k_4k'))} | {', '.join(r_['flags']) or '–'} |")
        L += ["", "Bối cảnh (" + ("'Trong trận thô'" if CTX_KEY[sid] == "scene" else "'Liên thanh 3 s'") + f", `{SCENARIO[sid]}`):", "",
              "| Bản | Cấu hình | " + " | ".join(lbl for _, lbl in BURST_KEYS) + " | Giọng min dB | Đỉnh game dBTP |",
              "|---|---|" + "---|" * (len(BURST_KEYS) + 2)]
        for name, r in rend.items():
            bm = r["metrics"].get("burst") or {}
            L.append(f"| `{name}` | {r['config']}{' nền −' + _fmt(r['bed_db'], 0) if sid in ('gun.xung', 'gun.xung.loop') else ''} | "
                     + " | ".join(_fmt(bm.get(k)) for k, _ in BURST_KEYS)
                     + f" | {_fmt((r['metrics'].get('voice') or {}).get('min_db'))} | {_fmt(r['metrics'].get('game_peak_dbtp'))} |")
        notes = [(k, v) for k, v in (obs.get(sid) or {}).items() if k != "_id"]
        if notes:
            L += ["", "Thẻ ảnh và bản dựng (Claude đọc):", *[f"- `{k}`: {v}" for k, v in notes]]
        L.append("")
        summary["ids"][sid] = {**{k: v for k, v in e.items() if k not in ("picks", "sets")}, "picks": rows_out,
                               "context": {k: v["metrics"] for k, v in rend.items()}, "notes": obs.get(sid)}
    path = base_dir(run) / "REPORT.md"
    path.write_text("\n".join(L) + "\n", "utf-8")
    (base_dir(run) / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1, default=str), "utf-8")
    _say(f"báo cáo {path}")
    return path


# ---------------------------------------------------------------- CLI

STEPS: dict = {"generate": step_generate, "process": step_process, "bodies": step_bodies, "recipes": step_recipes,
                "critic": step_critic, "loops": step_loops, "kills": step_kills, "t2": step_t2, "load": step_load,
                "breach": step_breach,
                "stage2": step_stage2,
                "link": step_link, "context": step_context, "session": step_session,
                "report": step_report}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="batch1_ts", description="Lô 1 · Tuyến Cuối (P1, P4 của BATCH1_BRIEF.md).")
    ap.add_argument("step", choices=[*STEPS, "all"])
    ap.add_argument("--run", default="b1")
    ap.add_argument("--force", action="store_true", help="làm lại bước đã có; ghi đè file phiên")
    a = ap.parse_args(argv)
    env.apply()
    for name in (list(STEPS) if a.step == "all" else [a.step]):
        try:
            rc = STEPS[name](a.run, a.force)
        except SessionExists as exc:
            print(f"batch1_ts: {exc}", file=sys.stderr)
            return 1
        if isinstance(rc, int) and rc:
            return rc
    return 0


if __name__ == "__main__":
    sys.exit(main())
