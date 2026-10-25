"""Batch 1c: the Q6 regeneration of Q6_REWRITE_2026-10-24.md §7 (action sounds shaped by their action).

  run.sh common.batch1c all [--game G] [--run b1c] [--force]
  run.sh common.batch1c generate|process|recipes|critic|link|report [--game G] [--run b1c] [--force]

The owner's rule (DECISIONS Q6, 24/10/2026): an action sound has the shape of its action, a build-up, a
forceful release, a body and a tail that echoes in the map's space; no puff, pop, balloon, toy, retro,
"bụp", "thụp". Only the Q6 keys of the cards are generated (new letters, so no candidate shares a name with
batch 0b or 1), at new seeds; gen.sa3 refuses every Q6-forbidden word before the model runs.

generate  Stable Audio 3 from the spec cards, one job at a time, in the order of §7: the Rồng Giữ Ải fire family
          (fire.cast, fire.impact.a/b/c, impact.multi, trap.pine-bomb.trigger, enemy.quadruped.howl at 2 s and
          3 s), then Lời Gọi (arrow-fire, wordshot-fire, ink-puff, blast, call-chop H with G), then Tuyến Cuối
          (kill.swarm, kill.elite, hurt.breach, gun.xung I/J/K, hit.t1, hit.t2, hit.t4). Each row carries the
          `pick_seconds` length of §7 (tests check it against gen.sa3.pick_seconds of the card).
process   gen/process.py on every raw take: true onset, natural window capped at the card's max, exponential tail,
          card channels, loudness as the card says (peak -1 dBTP); a creature keeps its whole call; the ids in
          BUILD_UP keep the build-up their action has (Q6), which the impact rules refused as a flam or a next hit.
recipes   the recipes §7 names, rebuilt for the Q6 lengths under build/recipes/<game>/<rid>.b1c.json (the batch 1
          files stay as rendered: session S2/S5/S4 of batch 1 is still open), rendered with build.render into
          ~/AudioLab/work/<game>/<sid>/<run>-recipe-<rid>: fire.impact.a/b/c and trap.pine-bomb.trigger (bodies
          from the new takes, peak-aligned), wordshot-fire.mix and blast.mix (layers ranked by the fast critic),
          kill.elite, hurt.breach, hurt.breach.b2, hit.t4 (bodies from the new takes).
critic    per game one critic run over every final (processed takes, recipe masters, the owner-rated references;
          calibration owner-v1; the card's critic.loop_eval decides the looped L3-L5 input), a raw-stage run for the
          ids whose whole takes are blocked only by the rise or length rule (creatures, whooshes, slow flares), and
          an L1 run on every raw float file.
link      critic AI steps into SOURCES.json, a batch-local release tree of the recipes, licence-check on it.
report    ~/AudioLab/work/_batch1c/<run>/REPORT.md and summary.json: per id the counts, the machine's top takes, the
          rank of every owner-rated reference, and the Q6 shape numbers (tail, punch, body share) against the L2
          rule proposed in DECISIONS Q6 (informational: not in the machine's score).

Heavy models run one at a time (common/batch1_dh.wait_heavy_free); nothing is written under games/**.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

from common import env
from common.batch1_dh import (_distinct, _docs, _flags, _fmt, _pct, _rank, _sid, _upper, _verified, body_window,
                              gen_src, wait_heavy_free)

LAB = env.LAB
SEED = 20261025
RUN = "b1c"
GAMES = ("dragon-hold", "typing-defense", "typing-survival")
DH, TD, TS = GAMES

# game -> id -> SA3 jobs: Q6 keys of the card, seeds, length (Q6_REWRITE §7, "Độ dài tạo"); "tag" names the length.
# Seeds 3001-3006 are new for every key here; call-chop G already has 2001-2006 (0b) and 3001-3006 (batch 1),
# so its row uses 3101-3106 (same prompt + seed = the same take again).
JOBS: dict[str, dict[str, list[dict]]] = {
    DH: {
        "fire.cast": [{"variants": ["E", "F", "G", "H"], "seeds": "3001-3006", "seconds": 2.0}],
        "fire.impact.a": [{"variants": ["E", "F", "G", "H"], "seeds": "3001-3006", "seconds": 1.0}],
        "fire.impact.b": [{"variants": ["F", "G", "H", "I"], "seeds": "3001-3006", "seconds": 1.0}],
        "fire.impact.c": [{"variants": ["C", "D", "E", "F"], "seeds": "3001-3006", "seconds": 2.0}],
        "impact.multi": [{"variants": ["A", "B", "C", "D"], "seeds": "3001-3006", "seconds": 2.0}],
        "trap.pine-bomb.trigger": [{"variants": ["C", "D", "E", "F"], "seeds": "3001-3006", "seconds": 2.0}],
        # 2 s is the card's length; 3 s as in batch 1, for the whole call with its echo (B is kept, not regenerated)
        "enemy.quadruped.howl": [{"variants": ["E", "F", "G"], "seeds": "3001-3006", "seconds": 2.0, "tag": True},
                                 {"variants": ["E", "F", "G"], "seeds": "3001-3006", "seconds": 3.0, "tag": True,
                                  "extra_length": True}],
    },
    TD: {
        "arrow-fire": [{"variants": ["E", "F", "G", "H"], "seeds": "3001-3006", "seconds": 1.0}],
        "wordshot-fire": [{"variants": ["E", "F", "G", "H"], "seeds": "3001-3006", "seconds": 1.0}],
        "ink-puff": [{"variants": ["E", "F", "G", "H"], "seeds": "3001-3006", "seconds": 1.0}],
        "blast": [{"variants": ["E", "F", "G", "H"], "seeds": "3001-3006", "seconds": 2.0}],
        "call-chop": [{"variants": ["G", "H"], "seeds": "3101-3106", "seconds": 1.0}],
    },
    TS: {
        "kill.swarm": [{"variants": ["E", "F"], "seeds": "3001-3006", "seconds": 1.0}],
        "kill.elite": [{"variants": ["E", "F", "G", "H"], "seeds": "3001-3006", "seconds": 1.0}],
        "hurt.breach": [{"variants": ["D", "E", "F"], "seeds": "3001-3006", "seconds": 2.0}],
        "gun.xung": [{"variants": ["I", "J", "K"], "seeds": "3001-3006", "seconds": 1.0}],
        "hit.t1": [{"variants": ["F", "G", "H", "I"], "seeds": "3001-3006", "seconds": 1.0}],
        "hit.t2": [{"variants": ["E", "F", "G", "H"], "seeds": "3001-3006", "seconds": 1.0}],
        "hit.t4": [{"variants": ["E", "F", "G"], "seeds": "3001-3006", "seconds": 2.0}],
    },
}

# takes the owner rated (DECISIONS Q1, Q5), put in the critic run next to the new ones: where the machine ranks them
REFS: dict[str, dict[str, Path]] = {
    DH: {"trap.pine-bomb.trigger 0a v3 (3/5)":
         env.WORK / DH / "trap.pine-bomb.trigger" / "batch0-2026-10-23-r2" / "masters" / "trap.pine-bomb.trigger-v3.wav",
         "enemy.quadruped.howl B s1004 (3/5)":
         env.WORK / DH / "enemy.quadruped.howl" / "b1" / "processed" / "enemy.quadruped.howl__B__s1004.wav"},
    TD: {"call-chop A s1006 (3/5)": env.WORK / TD / "call-chop" / "b1" / "processed" / "call-chop__A__s1006.wav",
         "call-chop E s2003 (3/5)": env.WORK / TD / "call-chop" / "b1" / "processed" / "call-chop__E__s2003.wav"},
    TS: {"gun.xung 0a v2 (4/5)": env.WORK / TS / "gun.xung" / "batch0-2026-10-23-r2" / "masters" / "gun.xung-v2.wav",
         "hit.t1 0b C s1006 (3/5)": env.WORK / TS / "hit.t1" / "sa3-r2" / "processed" / "hit.t1__C__s1006.wav",
         "hit.t2 0a v2 (3/5)": env.WORK / TS / "hit.t2" / "batch0-2026-10-23-r2" / "masters" / "hit.t2-v2.wav"},
}
# batch 1 renders that Q6 §7 keeps in use ("kill.swarm.vang.b1.json dùng tiếp"): ranked with the new takes
KEEP_B1 = {TS: [env.WORK / TS / "kill.swarm" / "b1-recipe-kill.swarm.vang" / "masters"]}


def _say(msg: str) -> None:
    print(f"[batch1c] {msg}", flush=True)


def base_dir(run: str, game: str | None = None) -> Path:
    p = env.WORK / "_batch1c" / run / (game or "")
    p.mkdir(parents=True, exist_ok=True)
    return p


def id_dir(game: str, sid: str, run: str) -> Path:
    return env.WORK / game / sid / run


def card_path(game: str, sid: str) -> Path:
    return LAB / "specs" / game / f"{sid}.yaml"


def recipe_path(game: str, rid: str) -> Path:
    return LAB / "build" / "recipes" / game / f"{rid}.b1c.json"


def sid_of(game: str, rid: str) -> str:
    """Recipe id -> card id (longest card id that is the recipe id or its prefix)."""
    for sid in sorted(JOBS[game], key=len, reverse=True):
        if rid == sid or rid.startswith(sid + "."):
            return sid
    raise KeyError(rid)


def recipe_run(game: str, rid: str, run: str) -> Path:
    return env.WORK / game / sid_of(game, rid) / f"{run}-recipe-{rid}"


def prompt_of(name: str) -> str:
    parts = Path(name).name.split("__")
    return parts[1][:1] if len(parts) >= 3 else ""


def _games(game: str | None) -> tuple[str, ...]:
    return (game,) if game else GAMES


# ---------------------------------------------------------------- step 1: generate

def build_jobs(game: str) -> list[tuple[str, dict, dict]]:
    """(id, row, sa3 job) in the order of §7; raises Sa3Error on a missing key or a forbidden word."""
    from gen import sa3

    out = []
    for sid, rows in JOBS[game].items():
        card = sa3.read_card(card_path(game, sid))
        for j in rows:
            job = sa3.build_job(card, variants=j["variants"], seeds=sa3.parse_seeds(j["seeds"]),
                                seconds=j.get("seconds"), tag_seconds=bool(j.get("tag")))
            out.append((sid, j, job))
    return out


def step_generate(run: str, game: str | None = None, force: bool = False) -> None:
    from gen import sa3

    plans = [(g, *row) for g in _games(game) for row in build_jobs(g)]     # check every job before the first runs
    _say(f"generate: {len(plans)} job, {sum(len(j['items']) for *_, j in plans)} bản")
    for g, sid, row, job in plans:
        wait_heavy_free(f"sa3 {sid}")
        t0 = time.time()
        res = sa3.run_job(job, id_dir(g, sid, run))
        _say(f"sa3 {g}/{sid} {','.join(row['variants'])} {job['_meta']['seconds']:g} s: {res['todo']} mới, "
             f"{res['skipped']} đã có, {time.time() - t0:.0f} s"
             + (f", RAM mô hình {res['mlx_peak_gb']} GB" if res.get("mlx_peak_gb") else ""))


# ---------------------------------------------------------------- step 2: process

# ids whose action is a build-up then a release, or several bursts (gen/process.py --build-up). The first process run
# (25/10) refused them by the one-shot impact rules: fire.cast 16/24 (15 "gõ hai lần": a huff 11-22 dB under the flame
# at 12-140 ms, the flame peak at 240-813 ms, prompts F, G, H), impact.multi 19/24 (the next fireball ended the window
# at 143-330 ms, or the first flare read as a flam), the pine bomb 8/24 (the fuse or crack at 0-43 ms, the boom at
# ~200 ms), hurt.breach 8/18 (a first part 6-21 dB under the boom, the boom at 107-412 ms). Plain impacts keep the
# strict rules: on fire.impact.* or a hit a second hit still reads as two hits.
BUILD_UP = {DH: {"fire.cast", "impact.multi", "trap.pine-bomb.trigger"}, TS: {"hurt.breach"}}

def step_process(run: str, game: str | None = None, force: bool = False) -> None:
    from gen import process, sa3

    for g in _games(game):
        for sid in JOBS[g]:
            raw = id_dir(g, sid, run) / "raw"
            if not raw.is_dir():
                _say(f"process {g}/{sid}: chưa có bản thô")
                continue
            card = sa3.read_card(card_path(g, sid))
            res = process.process_many(process.collect_records([str(raw)]), card, id_dir(g, sid, run) / "processed",
                                       force=force, build_up=sid in BUILD_UP.get(g, set()))
            _say(f"process {g}/{sid}: {res['kept']} giữ, {len(res['rejected'])} loại, {res['skipped']} đã có")
            for r in res["rejected"]:
                _say(f"  loại {r['candidate']}: {r['reason']}")


# ---------------------------------------------------------------- step 3: recipe sources

def _round_robin(rows: list[dict], key) -> list[dict]:
    """One row per prompt letter in turn (each letter's rows in their given order): variant n spreads the prompts."""
    by: dict[str, list[dict]] = {}
    for r in rows:
        by.setdefault(key(r), []).append(r)
    out, k = [], 0
    while any(by.values()):
        for p in sorted(by):
            if k < len(by[p]):
                out.append(by[p][k])
        k += 1
        if all(k >= len(v) for v in by.values()):
            break
    return out


# pool -> (game, id, window s, latest loudest 5 ms): bodies cut from 4 ms before the loudest 5 ms (one onset, no cut
# into a sound before, no clip), as the batch 1 fire bodies. The windows hold the card's length minus a short margin,
# so the recipe keeps the take's own crackle, debris and echo (the Q6 body and tail) instead of a 330 ms slice.
PEAK_POOLS = {
    "fire-a": (DH, "fire.impact.a", 0.56, 0.7),
    "fire-b": (DH, "fire.impact.b", 0.60, 0.7),
    "fire-c": (DH, "fire.impact.c", 0.95, 0.9),
    "pine": (DH, "trap.pine-bomb.trigger", 1.00, 1.2),     # the fuse hiss comes first: the boom may peak late
    "t4": (TS, "hit.t4", 0.85, 0.9),
    # kill.elite takes sound from their first sample (21/24 processed takes have an unverified onset, never listened):
    # the recipe body starts at the blast instead
    "elite": (TS, "kill.elite", 0.56, 0.6),
}
# pool -> (game, id): processed windows (process.py's true onset and natural length), no second onset
PROC_POOLS = {"breach": (TS, "hurt.breach")}
# id -> fast-critic-ranked layers (L1, L1b, L2; no model): a whoosh, a paper and dust burst
LAYER_POOLS = {"wordshot": (TD, "wordshot-fire"), "blast": (TD, "blast")}
LAYER_NO_FLAGS = {"wordshot": {"double_onset", "lr_imbalance"}, "blast": {"lr_imbalance"}}


def peak_bodies(game: str, sid: str, run: str, length_s: float, max_peak_s: float) -> dict:
    rows, rej = [], []
    for f in sorted((id_dir(game, sid, run) / "raw").glob("*.f32.wav")):
        r = body_window(f, length_s)
        r["record"] = str(f.with_name(f.name.replace(".f32.wav", ".json")))
        r["name"] = f.name.replace(".f32.wav", "")
        r["ok"] = bool(not r["double_onset"] and not r["clip"] and r["pre_db"] <= -3.0 and r["peak_s"] <= max_peak_s)
        (rows if r["ok"] else rej).append(r)
    rows.sort(key=lambda r: -r["peak_db"])
    return {"length_s": length_s, "n": len(rows) + len(rej), "ok": len(rows),
            "bodies": _round_robin(rows, lambda r: prompt_of(r["name"])),
            "rejected": [{k: r[k] for k in ("name", "double_onset", "clip", "pre_db", "peak_s")} for r in rej]}


def proc_bodies(game: str, sid: str, run: str) -> dict:
    from common import batch1_ts

    if game != batch1_ts.GAME:
        raise ValueError(game)
    rows = batch1_ts._proc_sources(sid, run)
    ok = sorted([r for r in rows if not r["double_onset"]], key=lambda r: -(r.get("len_ms") or 0))
    return {"n": len(rows), "ok": len(ok), "bodies": _round_robin(ok, lambda r: prompt_of(r["name"])),
            "rejected": [r["name"] for r in rows if r["double_onset"]]}


def _critic_run(inputs: list[Path], srcs: list[Path], out: Path, spec: Path, stage: str = "final",
                layers: str = "all", cards: bool = True) -> int:
    """The critic in its own process, so every other batch script sees a heavy model running and waits."""
    argv = ["run", *map(str, inputs), "--spec", str(spec), "--stage", stage, "--layers", layers, "--out", str(out),
            "--seed", str(SEED), "--quiet"]
    if cards:
        argv.append("--blind-cards")
    for s_ in srcs:
        if Path(s_).is_file():
            argv += ["--sources", str(s_)]
    return subprocess.run([sys.executable, "-I", str(LAB / "common" / "launch.py"), "critic", *argv]).returncode


def critic_out(run: str, game: str, name: str) -> Path:
    return base_dir(run, game) / f"critic-{name}"


def layer_pool(game: str, sid: str, key: str, run: str, force: bool) -> list[dict]:
    proc = id_dir(game, sid, run) / "processed"
    out = critic_out(run, game, f"layers-{sid}")
    if not (out / "_batch.json").is_file() or force:
        _critic_run([proc], [proc / "SOURCES.json"], out, card_path(game, sid), layers="L1,L1b,L2", cards=False)
    rows = []
    for d in _docs(out).values():
        pj = json.loads(Path(d["file"]["path"]).with_suffix(".proc.json").read_text("utf-8"))
        if pj.get("onset_verified", True) is False or LAYER_NO_FLAGS[key] & _flags(d):
            continue
        # a layer is not the whole sound: length, rise (the front layer carries it) and DC (the recipe's high-pass)
        # do not apply; a clip or anything else still refuses it
        if d["verdict"] != "PASS" and set(d["L1"]["blocking"]) - {"duration", "attack", "dc_offset"}:
            continue
        rows.append({"name": d["file"]["stem"], "l2": (d.get("L2") or {}).get("score") or 0.0,
                     "file": pj["source_f32"], "record": pj["raw_record"], "window": pj["window_raw_s"],
                     "len_ms": pj["window"]["len_ms"]})
    rows.sort(key=lambda r: -r["l2"])
    return _round_robin(rows, lambda r: prompt_of(r["name"]))


def step_sources(run: str, game: str | None = None, force: bool = False) -> dict:
    out = base_dir(run) / "sources.json"
    pools = json.loads(out.read_text("utf-8")) if out.is_file() and not force else {}
    for key, (g, sid, length, max_pk) in PEAK_POOLS.items():
        if g in _games(game) and (key not in pools or force):
            pools[key] = peak_bodies(g, sid, run, length, max_pk)
            _say(f"thân {key} ({sid}): {pools[key]['ok']}/{pools[key]['n']} dùng được (một đầu tiếng, không cắt vào âm "
                 f"trước, không clip, đỉnh trước {max_pk:g} s)")
    for key, (g, sid) in PROC_POOLS.items():
        if g in _games(game) and (key not in pools or force):
            pools[key] = proc_bodies(g, sid, run)
            _say(f"thân {key} ({sid}): {pools[key]['ok']}/{pools[key]['n']} (đầu tiếng đã xác minh, không hai đầu tiếng)")
    for key, (g, sid) in LAYER_POOLS.items():
        if g in _games(game) and (key not in pools or force):
            rows = layer_pool(g, sid, key, run, force)
            pools[key] = {"n": len(rows), "ok": len(rows), "bodies": rows}
            _say(f"lớp {key} ({sid}): {len(rows)} bản; đầu: {', '.join(r['name'] for r in rows[:4])}")
    out.write_text(json.dumps(pools, indent=1, ensure_ascii=False, default=float), "utf-8")
    return pools


# ---------------------------------------------------------------- step 4: recipes

def _cycle(layer: dict, sources: list[dict]) -> dict:
    layer["source"] = sources[0]
    if len(sources) > 1:
        layer.setdefault("vary", {}).update({"swapMode": "cycle", "swap": sources[1:]})
    return layer


def _lib(path: str) -> dict:
    return {"library": path if "/" in path else f"kenney/impact-sounds/Audio/{path}.ogg"}


def _smp(instrument: str, notes: str) -> dict:
    return {"sampler": {"instrument": instrument, "notes": notes}}


def _click(lid: str, off: float, gain: float, dur: float, hp: float, lp: float, jitter: tuple[float, float]) -> dict:
    return {"id": lid, "role": "sweetener", "source": {"synth": "click", "params": {"durMs": dur, "hpHz": hp, "lpHz": lp}},
            "offsetMs": off, "gainDb": gain, "vary": {"offsetMs": list(jitter)}}


def _recipe(game: str, rid: str, group: str, family: str, desc: str, layers: list[dict], chain: dict, count: int,
            seed: int, export: str, pitch=(0, 0), gain=(0, 0)) -> dict:
    return {"$schema": "../../schemas/recipe.schema.json", "schema": "audiolab.recipe/1", "game": game, "id": rid,
            "group": group, "family": family, "description": desc, "channels": 1, "layers": layers, "chain": chain,
            "variants": {"count": count, "seed": seed, "includeBase": True, "pitchCents": list(pitch), "gainDb": list(gain)},
            "export": {"path": export, "ogg": True, "oggQuality": 0.6}}


def _chain(max_ms: float, knee_ms: float, *, lowpass: float | None = None, dc: float = 35.0, sat: bool = False,
           peak_2k5: float | None = None, release_ms: float = 60.0) -> dict:
    filters = []
    if lowpass:
        filters.append({"type": "lowpass", "hz": lowpass, "order": 2})
    if peak_2k5 is not None:
        filters.append({"type": "peak", "hz": 2500, "gainDb": peak_2k5, "q": 0.7})
    c: dict = {"dcHpfHz": dc}
    if filters:
        c["filters"] = filters
    if sat:
        c["saturation"] = {"driveDb": 2, "mix": 0.2}
    c.update({"headTrim": {"thresholdDb": -50, "preRollMs": 0.5}, "maxLengthMs": max_ms,
              "tail": {"floorDb": -60, "shape": "exp", "kneeMs": knee_ms},
              "normalise": {"mode": "lufs-m-max", "target": -20},
              "limiter": {"ceilingDbtp": -1.0, "releaseMs": release_ms, "maxGrDb": 6}})
    return c


Q6_NOTE = ("Lô 1c (Q6, DECISIONS): âm theo hình dạng hành động, đủ phát có lực, thân, đuôi vang trong không gian bản đồ; "
           "lớp trầm chỉ nằm dưới, có thân và đuôi đè lên. ")


def dh_recipes(pools: dict) -> dict[str, dict]:
    out = {}
    A, B, C, P = (pools[k]["bodies"] for k in ("fire-a", "fire-b", "fire-c", "pine"))
    embers = [_click("ember1", 90, -24, 3, 3200, 9000, (-20, 25)), _click("ember2", 190, -27, 2, 3800, 10000, (-25, 30))]
    fronts_a = ["impactGeneric_light_002", "impactWood_heavy_003", "impactGeneric_light_000", "impactWood_heavy_004",
                "impactGeneric_light_004", "impactWood_heavy_001", "impactGeneric_light_002", "impactWood_heavy_000"]
    n = min(8, len(A))
    if n:
        out["fire.impact.a"] = _recipe(
            DH, "fire.impact.a", "hit-heavy", "trung",
            Q6_NOTE + "fire.impact.a 600 ms (480–720): lửa bùng có thân, than lách tách, mảnh văng, vang rừng thấp, ngắn. "
            "Đầu tiếng Kenney như công thức 0b anh chấm 3/5 (generic light, gỗ nặng), nhưng lọc cao 300 Hz và nhỏ hơn 4 dB: "
            "chỉ là tiếng chạm giòn, không thành cú 'thụp'. Thân là bản Stable Audio 3 prompt E–H của lô 1c, cửa sổ 560 ms "
            "từ 4 ms trước đỉnh 5 ms (một đầu tiếng), nên giữ được lửa bùng, lách tách, mảnh văng và vang rừng của chính bản "
            "đó (thân lô 1 họ B 'thân tròn' đã bỏ). Sub 90 ms nhỏ hơn 11 dB chỉ làm lớp dưới. Đuôi hàm mũ từ 380 ms. "
            "Biến thể n dùng đầu tiếng n và thân n (thân xen theo prompt).",
            [_cycle({"id": "front", "role": "attack", "gainDb": -4, "filters": [{"type": "highpass", "hz": 300}],
                     "trim": {"endMs": 80}, "fadeOutMs": 50}, [_lib(f) for f in fronts_a[:n]]),
             _cycle({"id": "body", "role": "body", "gainDb": -1, "fadeInMs": 3, "fadeOutMs": 180,
                     "filters": [{"type": "highpass", "hz": 90, "order": 4}]}, [gen_src(b) for b in A[:n]]),
             {"id": "sub", "role": "sub", "source": {"synth": "sub_thump", "params": {
                 "startHz": 80, "endHz": 45, "glideMs": 50, "durMs": 90, "decayMs": 70}}, "gainDb": -11},
             *json.loads(json.dumps(embers))],
            _chain(720, 380, lowpass=10000, sat=True), n, 3410, "sfx/dragon/fire-impact-a", pitch=(-20, 20), gain=(-0.5, 0.5))
    nb = min(8, len(B))
    if nb:
        out["fire.impact.b"] = _recipe(
            DH, "fire.impact.b", "hit-heavy", "trung",
            Q6_NOTE + "fire.impact.b 640 ms (512–768): như .a nhưng tối hơn, than nổ khô, dăm gỗ văng. Đầu tiếng generic "
            "light của hai bản 0b được 3/5 (lọc cao 300 Hz, −5 dB). Thân Stable Audio 3 prompt F–I, cửa sổ 600 ms, hạ một "
            "bán cung; lọc thấp 6,5 kHz cho màu tối; bốn tiếng than hồng tới 420 ms; sub 85 ms −12 dB chỉ ở dưới. Đuôi hàm "
            "mũ từ 400 ms. Biến thể n dùng thân n.",
            [_cycle({"id": "front", "role": "attack", "gainDb": -5, "filters": [{"type": "highpass", "hz": 300}],
                     "trim": {"endMs": 80}, "fadeOutMs": 50},
                    [_lib("impactGeneric_light_002"), _lib("impactGeneric_light_000")] * (nb // 2) + [_lib("impactGeneric_light_002")] * (nb % 2)),
             _cycle({"id": "body", "role": "body", "gainDb": 0, "fadeInMs": 3, "fadeOutMs": 200, "pitchSemitones": -1,
                     "filters": [{"type": "highpass", "hz": 90, "order": 4}]}, [gen_src(b) for b in B[:nb]]),
             {"id": "sub", "role": "sub", "source": {"synth": "sub_thump", "params": {
                 "startHz": 75, "endHz": 42, "glideMs": 50, "durMs": 85, "decayMs": 65}}, "gainDb": -12},
             *json.loads(json.dumps(embers)),
             _click("ember3", 300, -28, 2, 3000, 8000, (-30, 30)), _click("ember4", 420, -30, 3, 2600, 7000, (-30, 20))],
            _chain(768, 400, lowpass=6500, sat=True), nb, 3411, "sfx/dragon/fire-impact-b", pitch=(-20, 20), gain=(-0.5, 0.5))
    nc = min(8, len(C))
    if nc:
        fronts_c = ["impactWood_heavy_003", "impactGeneric_light_002", "impactWood_heavy_004", "impactGeneric_light_000",
                    "impactSoft_heavy_001", "impactWood_heavy_001", "impactGeneric_light_004", "impactWood_heavy_000"]
        out["fire.impact.c"] = _recipe(
            DH, "fire.impact.c", "blast", "trung",
            Q6_NOTE + "fire.impact.c 1000 ms (800–1200), đòn to (T3 trở lên, Hoàn hảo, Chớp): lửa bùng lớn có trọng lượng, "
            "gầm cháy tiếp, than và mảnh văng xa, vang thung lũng dài. Thân là bản Stable Audio 3 prompt C–F của chính id "
            "này, cửa sổ 950 ms từ 4 ms trước đỉnh (lô 1 ghép thân .a với lớp bùng lửa lọc thấp 1,8 kHz, dài 620 ms). Đầu "
            "tiếng Kenney gỗ nặng, generic light (lọc cao 200 Hz, −2 dB). Lớp nổ đục chỉ ở dưới: sub 140 ms −9 dB (≤ 150 ms). "
            "Than hồng rải tới 700 ms cho phần cháy tiếp. Đuôi hàm mũ từ 650 ms tới 1,2 s. Biến thể n dùng đầu tiếng n, thân n.",
            [_cycle({"id": "front", "role": "attack", "gainDb": -2, "filters": [{"type": "highpass", "hz": 200}],
                     "trim": {"endMs": 100}, "fadeOutMs": 60}, [_lib(f) for f in fronts_c[:nc]]),
             _cycle({"id": "body", "role": "body", "gainDb": 0, "fadeInMs": 3, "fadeOutMs": 320,
                     "filters": [{"type": "highpass", "hz": 70, "order": 4}]}, [gen_src(b) for b in C[:nc]]),
             {"id": "sub", "role": "sub", "source": {"synth": "sub_thump", "params": {
                 "startHz": 80, "endHz": 40, "glideMs": 70, "durMs": 140, "decayMs": 110}}, "gainDb": -9},
             *json.loads(json.dumps(embers)),
             _click("ember3", 300, -27, 2, 3000, 8000, (-30, 30)), _click("ember4", 450, -29, 3, 2800, 7500, (-30, 30)),
             _click("ember5", 580, -31, 2, 3000, 8000, (-40, 40)), _click("ember6", 700, -33, 2, 2600, 7000, (-40, 40))],
            _chain(1200, 650, lowpass=10000, sat=True, release_ms=80), nc, 3412, "sfx/dragon/fire-impact-c",
            pitch=(-20, 20), gain=(-0.5, 0.5))
    npb = min(6, len(P))
    if npb:
        seeds = [("seed1", "impactWood_light_000", 140, -15, 900, 30), ("seed2", "impactWood_light_002", 270, -17, 900, 40),
                 ("seed3", "impactWood_light_003", 410, -19, 900, 50), ("seed4", "impactWood_light_004", 560, -22, 1200, 60)]
        out["trap.pine-bomb.trigger"] = _recipe(
            DH, "trap.pine-bomb.trigger", "blast", "no",
            Q6_NOTE + "Bom Hạt Thông 1100 ms (880–1320): giữ khung công thức 0a v3 anh chấm 3/5 (nứt ván Kenney impactPlank "
            "medium 002, tiếng tách nhiễu 2–8 kHz 30 ms, bốn hạt gỗ văng lệch giờ), thay thân nổ Kenney sci-fi bằng thân và "
            "đuôi Q6: bản Stable Audio 3 prompt C–F, cửa sổ 1 s từ 4 ms trước đỉnh tiếng nổ (nổ trầm có thân, hạt và dăm văng, "
            "vang rừng thông). Sub 240 ms nhỏ hơn 12 dB chỉ ở dưới. Đuôi hàm mũ từ 750 ms. Tiếng ngòi xì có ở bản nguyên khối "
            "(cũng trong lần chấm), công thức bắt đầu ở tiếng nổ vì bẫy nổ ngay khi quái chạm. Biến thể n dùng thân n.",
            [{"id": "crack", "role": "attack", "source": _lib("impactPlank_medium_002"), "gainDb": 2,
              "filters": [{"type": "highpass", "hz": 600}], "trim": {"endMs": 320}, "fadeOutMs": 120,
              "vary": {"pitchCents": [-100, 60]}},
             {"id": "snap", "role": "attack", "source": {"synth": "noise_burst", "params": {
                 "color": "white", "durMs": 30, "attackMs": 0.2, "decayMs": 25, "hpHz": 2000, "lpHz": 8000}},
              "gainDb": -6},
             _cycle({"id": "body", "role": "body", "gainDb": -2, "fadeInMs": 2, "fadeOutMs": 350,
                     "filters": [{"type": "highpass", "hz": 40, "order": 2}]}, [gen_src(b) for b in P[:npb]]),
             {"id": "sub", "role": "sub", "source": {"synth": "sub_thump", "params": {
                 "startHz": 62, "endHz": 35, "glideMs": 120, "durMs": 240, "decayMs": 220}}, "gainDb": -12},
             *[{"id": i, "role": "debris", "source": _lib(f), "offsetMs": o, "gainDb": g,
                "filters": [{"type": "highpass", "hz": hp}], "vary": {"offsetMs": [-j, j], "pitchCents": [-150, 150]}}
               for i, f, o, g, hp, j in seeds]],
            _chain(1320, 750, dc=30, peak_2k5=-3, release_ms=80), npb, 3413, "sfx/trap/pine-bomb-trigger",
            pitch=(-100, 100))
    return out


def td_recipes(pools: dict) -> dict[str, dict]:
    out = {}
    W = pools["wordshot"]["bodies"][:4]
    if W:
        papers = [_lib("kenney/rpg-audio/Audio/bookFlip3.ogg"), _lib("kenney/rpg-audio/Audio/bookFlip2.ogg")] * 2
        out["wordshot-fire.mix"] = _recipe(
            TD, "wordshot-fire.mix", "shot", "ban",
            Q6_NOTE + "Phát Chữ 350 ms (280–420): vung tay tre, chữ giấy phóng vút đi, giấy phần phật bay xa, vang làng ngắn. "
            "Tiếng vút là bản Stable Audio 3 prompt E–H của lô 1c (mỗi prompt một bản, xếp bằng L1, L1b, L2; cửa sổ đầu "
            "tiếng thật, dài tự nhiên tới 420 ms nên giữ được đuôi làng), cộng tiếng lật giấy Kenney RPG bookFlip3/2 (cắt từ "
            "25 ms, lọc cao 1,5 kHz, −10 dB, vào sau 8 ms) cho chữ giấy. Lọc cao 120 Hz (§4.3.3 'khạc, phóng'). Phát sau mỗi "
            "từ (1,5 s một lần): đuôi hàm mũ từ 220 ms, thấp. Lô 1 dùng tiếng vút A–D (đã bỏ) và cắt ở 210 ms. "
            "Biến thể n dùng tiếng vút n.",
            [_cycle({"id": "whoosh", "role": "body", "fadeOutMs": 60}, [gen_src(b) for b in W]),
             _cycle({"id": "paper", "role": "sweetener", "gainDb": -10, "offsetMs": 8, "trim": {"startMs": 25, "endMs": 190},
                     "fadeOutMs": 60, "filters": [{"type": "highpass", "hz": 1500}]}, papers[:len(W)])],
            _chain(420, 220, dc=120), len(W), 3301, "sfx/battle/wordshot-fire")
    P = pools["blast"]["bodies"][:4]
    if P:
        n = len(P)
        drums = [_smp("frame-drum", "0:hdruml-hit:0.8:120"), {"sampler": {"instrument": "timpani", "notes": "0:timpani2-hit:1.0:110"}},
                 _smp("frame-drum", "0:hdruml-hit:0.8:110"), {"sampler": {"instrument": "timpani", "notes": "0:timpani2-hit:1.0:100"}}]
        fronts = [_lib(f"impactPlank_medium_00{k}") for k in (4, 2, 0, 4)]
        out["blast.mix"] = _recipe(
            TD, "blast.mix", "blast", "no",
            Q6_NOTE + "Tháp Pháo 800 ms (640–960): trống lớn nện có thân, giấy và bụi bung tung, mảnh giấy rơi lả tả, vang "
            "làng; không lớp nổ lách tách, không chất taiko. Nứt ván Kenney impactPlank (lọc cao 900 Hz, 60 ms) cho tiếng "
            "phát; trống khung VCSL đánh mở hoặc timpani VSCO-2-CE làm thân (−3 dB, lọc cao 70 Hz, giữ 500 ms: lô 1 cắt ở "
            "320 ms); lớp giấy, bụi và vang làng là bản Stable Audio 3 prompt E–H (xếp bằng L1, L1b, L2), lọc cao 300 Hz để "
            "tiếng trống của chính bản đó không thành đầu tiếng thứ hai, vào sau 12 ms, mờ vào 25 ms, −5 dB, dài tự nhiên "
            "tới 960 ms. Đuôi hàm mũ từ 520 ms. Biến thể n dùng nứt n, trống n, lớp giấy n.",
            [_cycle({"id": "crack", "role": "attack", "gainDb": -2, "trim": {"endMs": 60}, "fadeOutMs": 30,
                     "filters": [{"type": "highpass", "hz": 900}]}, fronts[:n]),
             _cycle({"id": "drum", "role": "body", "gainDb": -3, "trim": {"endMs": 500}, "fadeOutMs": 300,
                     "filters": [{"type": "highpass", "hz": 70, "order": 2}]}, drums[:n]),
             _cycle({"id": "paper", "role": "texture", "gainDb": -5, "offsetMs": 12, "fadeInMs": 25, "fadeOutMs": 300,
                     "filters": [{"type": "highpass", "hz": 300}]}, [gen_src(b) for b in P])],
            _chain(960, 520, dc=40, release_ms=80), n, 3401, "sfx/battle/blast")
    return out


def ts_recipes(pools: dict) -> dict[str, dict]:
    out = {}
    E = pools["elite"]["bodies"][:6]
    if E:
        arcs = [{"id": f"arc{i}", "role": "sweetener", "offsetMs": off, "gainDb": g, "source": {"synth": "noise_burst", "params": {
            "color": "white", "durMs": 18, "attackMs": 0.3, "decayMs": 14, "hpHz": 2000, "lpHz": 8000}},
            "vary": {"offsetMs": [-15, 15]}} for i, (off, g) in enumerate(((30, -16), (85, -18), (140, -20), (210, -22), (300, -25)))]
        out["kill.elite"] = _recipe(
            TS, "kill.elite", "death-big", "chet",
            Q6_NOTE + "Lính tinh nhuệ nổ 500 ms (400–600): thép xé toạc, nổ trầm có thân, phóng điện lách tách, mảnh rơi, "
            "vang hành lang thép. Thân là bản Stable Audio 3 prompt E–H của lô 1c, cửa sổ 560 ms từ 4 ms trước đỉnh 5 ms (một "
            "đầu tiếng, xen theo prompt): bản thô kêu ngay từ mẫu đầu nên 21/24 bản xử lý có đầu tiếng chưa xác minh, không "
            "nghe được nguyên khối. Lọc cao 45 Hz; năm tiếng tách điện tổng hợp 2–8 kHz thưa dần tới 300 ms. Đuôi hàm mũ từ 420 ms. Lô 1 dùng thân A–D (đã bỏ). Biến thể n dùng thân n.",
            [_cycle({"id": "body", "role": "body", "filters": [{"type": "highpass", "hz": 45, "order": 2}]},
                    [gen_src(b) for b in E]), *arcs],
            _chain(600, 420), len(E), 3530, "sfx/kills/kill-elite", pitch=(-30, 30))
    BR = pools["breach"]["bodies"][:6]
    if BR:
        siren = [{"id": "siren1", "role": "sweetener", "offsetMs": 30, "gainDb": -9, "source": {"synth": "tone", "params": {
            "wave": "square", "freqHz": 440, "durMs": 90, "attackMs": 4, "decayMs": 400}},
            "filters": [{"type": "lowpass", "hz": 1600, "order": 4}], "fadeOutMs": 15},
            {"id": "siren2", "role": "sweetener", "offsetMs": 140, "gainDb": -9, "source": {"synth": "tone", "params": {
                "wave": "square", "freqHz": 330, "durMs": 90, "attackMs": 4, "decayMs": 400}},
             "filters": [{"type": "lowpass", "hz": 1600, "order": 4}], "fadeOutMs": 15}]
        out["hurt.breach"] = _recipe(
            TS, "hurt.breach", "alarm", "nen",
            Q6_NOTE + "Tuyến bị phá 800 ms (640–960): nổ trầm có thân, thép rên, còi hai nốt ngắn, vang dội dọc hành lang "
            "thép. Thân là bản Stable Audio 3 prompt D–F của lô 1c (tạo 2 s, cửa sổ process.py dài tự nhiên tới 960 ms), lọc "
            "cao 40 Hz; còi giữ như lô 1 (440/330 Hz vuông, lọc thấp 1,6 kHz, 90 ms mỗi nốt ở 30 và 140 ms). Đuôi hàm mũ từ "
            "650 ms (lô 1: 720 ms tối đa, thân A–C đã bỏ). Biến thể n dùng thân n.",
            [_cycle({"id": "body", "role": "body", "filters": [{"type": "highpass", "hz": 40, "order": 2}]},
                    [gen_src(b) for b in BR]), *json.loads(json.dumps(siren))],
            _chain(960, 650, release_ms=80), len(BR), 3533, "sfx/alerts/hurt-breach")
        heads = [_lib(f"impactPlate_heavy_00{k}") for k in (0, 2, 4)] * 2
        b2_layers = [_cycle({"id": "hit", "role": "attack", "gainDb": -3, "filters": [{"type": "lowpass", "hz": 2500, "order": 2}],
                             "trim": {"endMs": 120}, "fadeOutMs": 60}, heads[:len(BR)]),
                     {"id": "boom", "role": "sub", "gainDb": -10, "source": {"synth": "sub_thump", "params": {
                         "startHz": 70, "endHz": 38, "glideMs": 120, "durMs": 300, "decayMs": 280, "driveDb": 6}}},
                     _cycle({"id": "body", "role": "body", "offsetMs": 10,
                             "filters": [{"type": "highpass", "hz": 40, "order": 2}, {"type": "lowpass", "hz": 1200, "order": 4}]},
                            [gen_src(b) for b in BR])]
        for s in json.loads(json.dumps(siren)):
            s["filters"] = [{"type": "lowpass", "hz": 1000, "order": 8}]
            b2_layers.append(s)
        out["hurt.breach.b2"] = _recipe(
            TS, "hurt.breach.b2", "alarm", "nen",
            Q6_NOTE + "Bản 2 của hurt.breach (như hurt.breach.b2 của lô 1, dựng lại cho 800 ms): cú đập thép Kenney Impact "
            "Plate heavy (lọc thấp 2,5 kHz) và lớp nổ trầm tổng hợp 70→38 Hz 300 ms −10 dB ở 0 ms làm tiếng phát; thân Stable "
            "Audio 3 prompt D–F lọc 40 Hz–1,2 kHz (thép rên và vang hành lang dưới dải giọng); còi lọc thấp 1 kHz. Biến thể n "
            "dùng cú đập n và thân n.",
            b2_layers, _chain(960, 650, release_ms=80), len(BR), 3536, "sfx/alerts/hurt-breach")
    T4 = pools["t4"]["bodies"][:6]
    if T4:
        fronts = [_lib(f"impactMetal_heavy_00{k}") for k in (0, 2, 3, 4)] * 2
        out["hit.t4"] = _recipe(
            TS, "hit.t4", "hit-heavy", "trung",
            Q6_NOTE + "Đòn lớn 900 ms (720–1080): nện nặng vào dầm thép, nứt giòn, thân thép dày có trọng lượng, lớp trầm bên "
            "dưới, dầm ngân dài lăn dọc hành lang thép. Mã game phát một tiếng mỗi bậc (không ghép lớp), nên mọi lớp nằm sẵn "
            "trong file. Đầu tiếng Kenney Impact Metal heavy (lọc cao 600 Hz, 60 ms, −4 dB); thân là bản Stable Audio 3 prompt "
            "E–G của lô 1c, cửa sổ 850 ms từ 4 ms trước đỉnh (giữ tiếng dầm ngân của chính bản đó; lô 1 lấy 300 ms rồi ghép "
            "đuôi Anvil); sub 90 ms −10 dB chỉ ở dưới. Đuôi hàm mũ từ 700 ms. Biến thể n dùng đầu tiếng n và thân n.",
            [_cycle({"id": "front", "role": "attack", "gainDb": -4, "filters": [{"type": "highpass", "hz": 600}],
                     "trim": {"endMs": 60}, "fadeOutMs": 40}, fronts[:len(T4)]),
             _cycle({"id": "body", "role": "body", "gainDb": 0, "fadeInMs": 2, "fadeOutMs": 300,
                     "filters": [{"type": "highpass", "hz": 90, "order": 2}]}, [gen_src(b) for b in T4]),
             {"id": "sub", "role": "sub", "source": {"synth": "sub_thump", "params": {
                 "startHz": 85, "endHz": 45, "glideMs": 45, "durMs": 90, "decayMs": 80, "driveDb": 3}}, "gainDb": -10}],
            _chain(1080, 700, dc=30, release_ms=80), len(T4), 3524, "sfx/hits/hit-t4")
    return out


RECIPES = {DH: dh_recipes, TD: td_recipes, TS: ts_recipes}
RECIPE_IDS = {DH: ("fire.impact.a", "fire.impact.b", "fire.impact.c", "trap.pine-bomb.trigger"),
              TD: ("wordshot-fire.mix", "blast.mix"),
              TS: ("kill.elite", "hurt.breach", "hurt.breach.b2", "hit.t4")}


def step_recipes(run: str, game: str | None = None, force: bool = False) -> None:
    from build import render

    pools = step_sources(run, game)
    for g in _games(game):
        recipes = RECIPES[g](pools)
        for rid in RECIPE_IDS[g]:
            if rid not in recipes:
                _say(f"recipe {g}/{rid}: không có nguồn nào dùng được, bỏ qua")
                continue
            p = recipe_path(g, rid)
            p.write_text(json.dumps(recipes[rid], ensure_ascii=False, indent=1) + "\n", "utf-8")
            out = recipe_run(g, rid, run)
            if out.is_dir() and (out / "render.json").is_file() and not force:
                _say(f"recipe {g}/{rid}: đã có {out}")
                continue
            res = render.render(p, out=out, spec=card_path(g, sid_of(g, rid)))
            _say(f"recipe {g}/{rid}: {res.report['count']} biến thể, mức id {res.report['idLevel']} LUFS-M; "
                 + ("; ".join(res.report["warnings"]) or "không cảnh báo"))


# ---------------------------------------------------------------- step 5: critic

def finals(run: str, game: str) -> tuple[list[Path], list[Path]]:
    dirs, srcs = [], []
    for sid in JOBS[game]:
        p = id_dir(game, sid, run) / "processed"
        if p.is_dir():
            dirs.append(p)
            srcs.append(p / "SOURCES.json")
    for rid in RECIPE_IDS[game]:
        r = recipe_run(game, rid, run)
        if (r / "masters").is_dir():
            dirs.append(r / "masters")
            srcs.append(r / "SOURCES.json")
    for f in REFS.get(game, {}).values():
        if f.is_file():
            dirs.append(f)
            srcs.append(f.parent.parent / "SOURCES.json" if f.parent.name == "masters" else f.parent / "SOURCES.json")
    for m in KEEP_B1.get(game, []):
        if m.is_dir():
            dirs.append(m)
            srcs.append(m.parent / "SOURCES.json")
    return dirs, srcs


INFO_BLOCKS = {"attack", "duration"}      # rules a whole take may break by design (a swell, a creature call, a flare)


def info_ids(run: str, game: str) -> list[str]:
    """Ids whose whole takes are blocked only by the rise or length rule, with fewer than 2 eligible finals."""
    docs = _docs(critic_out(run, game, "final"))
    out = []
    for sid in JOBS[game]:
        mine = [d for d in docs.values() if _sid(d) == sid and _kind(d) == "sa3"]
        ok = [d for d in mine if d["verdict"] == "PASS" and _verified(d) and not _flags(d) & NO_PICK_FLAGS]
        blocked = [d for d in mine if d["verdict"] == "BLOCK" and set(d["L1"]["blocking"]) <= INFO_BLOCKS and _verified(d)]
        if len(ok) < 2 and blocked:
            out.append(sid)
    return out


def step_critic(run: str, game: str | None = None, force: bool = False) -> None:
    for g in _games(game):
        out = critic_out(run, g, "final")
        if (out / "_batch.json").is_file() and not force:
            _say(f"critic {g}: đã có {out}")
        else:
            dirs, srcs = finals(run, g)
            wait_heavy_free(f"critic {g}")
            t0 = time.time()
            _say(f"critic {g} final ({len(dirs)} mục): mã {_critic_run(dirs, srcs, out, LAB / 'specs' / g)}, "
                 f"{time.time() - t0:.0f} s")
        for sid in info_ids(run, g):
            info = critic_out(run, g, f"info-{sid}")
            if (info / "_batch.json").is_file() and not force:
                continue
            proc = id_dir(g, sid, run) / "processed"
            refs = [f for label, f in REFS.get(g, {}).items() if label.split(" ")[0] == sid and f.is_file()]
            wait_heavy_free(f"critic info {sid}")
            rc = _critic_run([proc, *refs], [proc / "SOURCES.json", *(f.parent / "SOURCES.json" for f in refs)], info,
                             card_path(g, sid), stage="raw")
            _say(f"critic {g}/{sid} giai đoạn raw (bản nguyên khối chỉ bị luật lên hoặc luật độ dài chặn): mã {rc}")
        raw = critic_out(run, g, "raw")
        if not (raw / "_batch.json").is_file() or force:
            raws = [id_dir(g, sid, run) / "raw" for sid in JOBS[g] if (id_dir(g, sid, run) / "raw").is_dir()]
            rc = _critic_run(raws, [], raw, LAB / "specs" / g, stage="raw", layers="L1,L1b", cards=False)
            _say(f"critic {g} raw L1 (clip đọc bản float): mã {rc}")


# ---------------------------------------------------------------- step 6: ledger + release check

def staging_dirs(run: str, game: str) -> tuple[Path, Path]:
    """Batch-local release tree. Not ~/AudioLab/review/staging: nothing here is owner-approved yet."""
    root = base_dir(run, game) / "staging" / game
    return root / "art-src" / "audio", root / "public" / "assets" / game / "audio"


def step_link(run: str, game: str | None = None, force: bool = False) -> int:
    from build import critic_link, licence_check, release

    worst = 0
    for g in _games(game):
        outs = [p for p in sorted(base_dir(run, g).glob("critic-*")) if p.name in ("critic-final",)
                or p.name.startswith("critic-info-")]
        for sid in JOBS[g]:
            p = id_dir(g, sid, run) / "processed"
            if (p / "SOURCES.json").is_file():
                res = critic_link.apply(p / "SOURCES.json", outs, p / "licences.rows.jsonl")
                _say(f"mark-ai {g}/{sid}: {res['steps']} bước, {res['files']} hồ sơ")
        art, pub = staging_dirs(run, g)
        n = 0
        for rid in RECIPE_IDS[g]:
            r = recipe_run(g, rid, run)
            if not (r / "SOURCES.json").is_file():
                continue
            res = critic_link.apply(r / "SOURCES.json", outs, r / "licences.rows.jsonl")
            rel = release.release(r, None, art, pub)
            n += 1
            _say(f"mark-ai {g}/{rid} (công thức): {res['steps']} bước; cây thử: {len(rel['files'])} file, "
                 f"{rel['rowsAdded']} dòng sổ, {len(rel['licenceCopies'])} bản giấy phép")
        if n:
            rc = licence_check.main(["--art-src", str(art), "--public", str(pub)])
            _say(f"licence-check (cây thử, công thức lô 1c) {g}: mã {rc}")
            worst = max(worst, rc)
    return worst


# ---------------------------------------------------------------- step 7: report

NO_PICK_FLAGS = {"double_onset", "lr_imbalance"}           # batch 0b review 2: never offered for listening


def _kind(d: dict) -> str:
    """sa3 (a take of this batch) | recipe (this batch) | ref (owner-rated) | b1 (a batch 1 render kept in use)."""
    path = d["file"]["path"]
    if any(str(f) == path for refs in REFS.values() for f in refs.values()):
        return "ref"
    if "/b1-recipe-" in path:
        return "b1"
    if "-recipe-" in path:
        return "recipe"
    return "sa3"


def _ref_label(d: dict) -> str | None:
    path = d["file"]["path"]
    for refs in REFS.values():
        for label, f in refs.items():
            if str(f) == path:
                return label
    return None


# DECISIONS Q6 "đề xuất luật L2" (not in code, thresholds not measured yet): measured here on the batch 1c finals,
# informational only. (good, bad) of tail_ms per id or group; the lone-low rule only on cards from 400 ms (punch_db
# reads 100-300 ms after the onset, which is the decay of a shorter sound).
Q6_TAIL = {"fire.cast": (300, 120), "hit.t1": (60, 25), "hit.t2": (120, 50)}
Q6_TAIL_GROUP = {"hit_fire": (250, 100), "explosion": (500, 200)}
Q6_TAIL_DH_HEAVY = (200, 80)
LONE_LOW_FAMILIES = {"trung", "no", "ban", "chet"}


def q6_checks(d: dict) -> dict[str, str]:
    """Rule id -> 'đạt' | 'giữa' | 'trượt' for the Q6 rules that apply to this file."""
    sp, m = d.get("spec") or {}, d.get("metrics") or {}
    sid, game, grp, fam = sp.get("id") or "", sp.get("game") or "", sp.get("group") or "", sp.get("family") or ""
    out: dict[str, str] = {}

    def hi(v, good, bad):
        if v is None:
            return None
        return "đạt" if v >= good else ("trượt" if v <= bad else "giữa")

    tail = Q6_TAIL.get(sid) or Q6_TAIL_GROUP.get(grp) or (Q6_TAIL_DH_HEAVY if game == DH and grp == "hit_heavy" else None)
    if tail:
        r = hi(m.get("tail_ms"), *tail)
        if r:
            out["tail"] = r
    lone = sid != "gun.xung" and ((game in (DH, TD) and fam in LONE_LOW_FAMILIES)
                                  or (game == TS and re.match(r"^(kill|hurt|foe)\.", sid)))
    if lone and (sp.get("duration_target_ms") or 0) >= 400:
        p = m.get("punch_db")
        if p is not None:
            out["punch"] = "đạt" if 6 <= p <= 20 else ("trượt" if p < 0 or p > 32 else "giữa")
        r = hi(m.get("share_150_800"), 0.12, 0.03)
        if r:
            out["body"] = r
    # the flag of the proposal, with the lone-low rule's scope: never gun.xung (5 shots a second, each one short)
    if sid != "gun.xung" and ((m.get("share_below_150") or 0) >= 0.6 and (m.get("tail_ms") or 1e9) < 150
                              and (m.get("punch_db") or 0) >= 25):
        out["lone_low_hit"] = "trượt"
    return out


def _row(d: dict, final: dict | None = None) -> dict:
    """One report row; `final` = the final-stage doc of a file ranked in a raw-stage info run (verdict from final)."""
    m, s_ = d["metrics"], d.get("score") or {}
    f = final or d
    return {"stem": d["file"]["stem"], "file": d["file"]["path"], "sha8": d["file"].get("sha256", "")[:8],
            "kind": _kind(d), "ref": _ref_label(d), "verdict": f["verdict"], "blocking": f["L1"]["blocking"],
            "rank_stage": "raw" if final is not None else "final",
            "rank": s_.get("rank"), "n_ranked": s_.get("n_ranked"), "combined": s_.get("combined"),
            "L2": (d.get("L2") or {}).get("score"), "flags": sorted(_flags(d)), "verified": _verified(d),
            "q6": q6_checks(d),
            "metrics": {k: m.get(k) for k in ("duration_ms", "attack_ms", "tail_ms", "punch_db", "share_below_150",
                                               "share_150_800", "share_1k_4k", "sub_len_ms", "sustain_1k4k_ms",
                                               "lufs_m_max", "speaker_loss_db") if m.get(k) is not None}}


def loop_eval(game: str, sid: str) -> dict:
    """The card's critic.loop_eval (critic/spec.py reads it: L3-L5 hear a 3-4 s loop at rate_hz) and rate."""
    import yaml
    crit = (yaml.safe_load(card_path(game, sid).read_text("utf-8")) or {}).get("critic") or {}
    return {"enabled": bool((crit.get("loop_eval") or {}).get("enabled")), "rate_hz": crit.get("rate_hz")}


def summarise(run: str, game: str) -> dict:
    docs = _docs(critic_out(run, game, "final"))
    out: dict = {}
    for sid in JOBS[game]:
        mine = sorted([d for d in docs.values() if _sid(d) == sid], key=_rank)
        ok = [d for d in mine if d["verdict"] == "PASS" and _verified(d) and not _flags(d) & NO_PICK_FLAGS
              and _kind(d) in ("sa3", "recipe")]
        e: dict = {"n": len(mine), "n_new": sum(1 for d in mine if _kind(d) in ("sa3", "recipe")),
                   "pass": sum(1 for d in mine if d["verdict"] == "PASS" and _kind(d) in ("sa3", "recipe")),
                   "eligible": len(ok), "blocking": {}, "picks": [], "refs": [], "q6": {}}
        for d in mine:
            if _kind(d) in ("sa3", "recipe"):
                for b in d["L1"]["blocking"]:
                    e["blocking"][b] = e["blocking"].get(b, 0) + 1
        picks: list[tuple[dict, str]] = []
        if ok:
            picks.append((ok[0], "top"))
            other = [d for d in ok if _kind(d) != _kind(ok[0])]
            if other:
                picks.append((other[0], "best-recipe" if _kind(other[0]) == "recipe" else "best-take"))
            used = {d["file"]["path"] for d, _ in picks}
            dis = _distinct(ok[0], [d for d in _upper(ok) if d["file"]["path"] not in used])
            if dis is not None:
                picks.append((dis, "distinct"))
        info = {d["file"]["path"]: d for d in _docs(critic_out(run, game, f"info-{sid}")).values()}
        final_of = {d["file"]["path"]: d for d in mine}
        if info:
            blocked = [d for d in mine if _kind(d) == "sa3" and d["verdict"] == "BLOCK"
                       and set(d["L1"]["blocking"]) <= INFO_BLOCKS and _verified(d)]
            ranked = sorted([info[d["file"]["path"]] for d in blocked if d["file"]["path"] in info], key=_rank)
            e["rule_blocked_whole"] = len(blocked)
            for d in ranked[:2]:
                picks.append((d, "bị luật chặn"))
        e["picks"] = [dict(_row(d, final_of.get(d["file"]["path"]) if r == "bị luật chặn" else None), role=r)
                      for d, r in picks]
        e["refs"] = [_row(info[d["file"]["path"]], d) if d["verdict"] != "PASS" and d["file"]["path"] in info
                     else _row(d) for d in mine if _kind(d) in ("ref", "b1")]
        for d in ok:
            for rule, v in q6_checks(d).items():
                e["q6"].setdefault(rule, {"đạt": 0, "giữa": 0, "trượt": 0})[v] += 1
        e["loop_eval"] = loop_eval(game, sid)
        out[sid] = e
    return out


Q6_RULE_VI = {"tail": "đuôi", "punch": "cú đấm/thân", "body": "thân 150–800 Hz", "lone_low_hit": "cú trầm đứng riêng"}


def _q6_cell(q: dict) -> str:
    return "; ".join(f"{Q6_RULE_VI[k]} {v}" for k, v in q.items()) or "–"


def step_report(run: str, game: str | None = None, force: bool = False) -> Path:
    L = ["# Lô 1c (Q6): sinh lại họ âm hành động", "",
         "Tự sinh bởi `common/batch1c.py report`. Thẻ ảnh của bộ chấm: `<game>/critic-final/<tên>.png` (bản cho Bảng Nghe: "
         "`.blind.png`). Số đo trên máy Mac mini M4 (Apple M4).", "",
         "Không tính là bản nghe được: đầu tiếng chưa xác minh, cờ `double_onset` hay `lr_imbalance`. Cột Q6 so số đo với "
         "luật L2 đề xuất ở DECISIONS Q6 (chưa vào điểm máy, ngưỡng chưa hiệu chỉnh bằng tai anh). Hạng có '(raw)': xếp trong lần "
         "chấm giai đoạn raw của các bản nguyên khối chỉ bị luật lên hoặc luật độ dài chặn (cột L1 vẫn là kết quả giai "
         "đoạn cuối).", ""]
    summary: dict = {"run": run, "games": {}}
    for g in _games(game):
        b = critic_out(run, g, "final") / "_batch.json"
        if not b.is_file():
            L += [f"## {g}", "", "Chưa chấm.", ""]
            continue
        bd = json.loads(b.read_text("utf-8"))
        c = bd.get("counts") or {}
        s = summarise(run, g)
        summary["games"][g] = {"counts": c, "n_files": bd.get("n_files"), "elapsed_s": bd.get("elapsed_s"), "ids": s}
        L += [f"## {g}", "", f"Lần chấm cuối: {bd.get('n_files')} file, {c.get('PASS', 0)} ĐẠT, {c.get('BLOCK', 0)} CHẶN, "
              f"{c.get('NEEDS_FIX', 0)} CẦN SỬA; {_fmt(bd.get('elapsed_s'), 0)} s.", "",
              "| Id | Bản mới | Qua L1 | Nghe được | Bị chặn vì | Lặp L3–L5 | Q6 (bản nghe được) |", "|---|---|---|---|---|---|---|"]
        for sid, e in s.items():
            q = "; ".join(f"{Q6_RULE_VI[k]} {v['đạt']}/{v['giữa']}/{v['trượt']}" for k, v in e["q6"].items()) or "–"
            blk = ", ".join(f"{k} {v}" for k, v in sorted(e["blocking"].items(), key=lambda kv: -kv[1])) or "–"
            le = e["loop_eval"]
            lp = f"bật, {_fmt(float(le['rate_hz']), 2)} Hz" if le["enabled"] and le["rate_hz"] else ("bật" if le["enabled"] else "tắt")
            L.append(f"| `{sid}` | {e['n_new']} | {e['pass']} | {e['eligible']} | {blk} | {lp} | {q} |")
        L += ["", "Q6: số bản đạt/giữa/trượt trong các bản nghe được. Lặp L3–L5: `critic.loop_eval` của thẻ (bộ chấm còn tự "
              "lặp mọi file dưới 300 ms).", ""]
        for sid, e in s.items():
            L += [f"### `{sid}`", "", "| Vai trò | Bản | Loại | L1 | Hạng | Điểm | L2 | Dài ms | Lên ms | Đuôi ms | Đấm dB | "
                  "<150 Hz | 150–800 Hz | Q6 | Cờ |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
            for r in e["picks"] + [dict(r, role=r["ref"] or "lô 1 dùng tiếp") for r in e["refs"]]:
                m = r["metrics"]
                L.append(f"| {r['role']} | `{r['stem']}` | {r['kind']} | {r['verdict']} {','.join(r['blocking'])} | "
                         f"{r['rank'] or '–'}/{r['n_ranked'] or '–'}{' (raw)' if r['rank_stage'] == 'raw' else ''} | {_fmt(r['combined'], 2)} | {_fmt(r['L2'], 2)} | "
                         f"{_fmt(m.get('duration_ms'), 0)} | {_fmt(m.get('attack_ms'))} | {_fmt(m.get('tail_ms'), 0)} | "
                         f"{_fmt(m.get('punch_db'))} | {_pct(m.get('share_below_150'))} | {_pct(m.get('share_150_800'))} | "
                         f"{_q6_cell(r['q6'])} | {', '.join(r['flags']) or '–'} |")
            L.append("")
    path = base_dir(run) / "REPORT.md"
    path.write_text("\n".join(L) + "\n", "utf-8")
    (base_dir(run) / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1, default=str), "utf-8")
    _say(f"báo cáo {path}")
    return path


# ---------------------------------------------------------------- CLI

STEPS = {"generate": step_generate, "process": step_process, "sources": step_sources, "recipes": step_recipes,
         "critic": step_critic, "link": step_link, "report": step_report}
ALL = ("generate", "process", "recipes", "critic", "link", "report")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="batch1c", description="Lô 1c: sinh lại âm hành động theo Q6 (Q6_REWRITE §7).")
    ap.add_argument("step", choices=[*STEPS, "all"])
    ap.add_argument("--game", choices=GAMES)
    ap.add_argument("--run", default=RUN)
    ap.add_argument("--force", action="store_true", help="làm lại bước đã có")
    a = ap.parse_args(argv)
    env.apply()
    for name in (ALL if a.step == "all" else (a.step,)):
        rc = STEPS[name](a.run, a.game, a.force)
        if isinstance(rc, int) and rc:
            return rc
    return 0


if __name__ == "__main__":
    sys.exit(main())
