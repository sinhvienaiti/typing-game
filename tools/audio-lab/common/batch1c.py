"""Batch 1c: the Q6 regeneration of Q6_REWRITE_2026-10-24.md §7 (action sounds shaped by their action).

  run.sh common.batch1c all [--game G] [--run b1c] [--force]
  run.sh common.batch1c generate|process|recipes|critic|link|report|context|session [--game G] [--run b1c] [--force]

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
context   the listening list of each id (select, at most 4: the machine's top, the other kind, rule-blocked whole
          takes with a label, the owner-rated takes blind, probes, a prompt not offered yet, the most different)
          rendered in its scene with the game-like mixer (context/): dh-cast-chain (fire.cast at the Q6 750 ms, the
          impacts, impact.multi on words 2 and 5), dh-pack, dh-trap, td-wordhit-chain, td-night, ts-xung-3s (the
          gun.xung I/K sets next to batch 1's direction 2 and the game today), ts-xung-3s-kills, ts-breach; every
          other slot fixed. ~/AudioLab/work/_batch1c/<run>/<game>/context.
session   the board sessions, ~/AudioLab/review/<game>/sessions/1c-dh-1|1c-dh-2|1c-td|1c-ts-1|1c-ts-2.json (batch "1c",
          at most 10 items and 20 minutes each with the anchor pairs, cards at the end); an existing session file is
          never overwritten without --force, and one the owner has opened never.

Heavy models run one at a time (common/batch1_dh.wait_heavy_free); nothing is written under games/**.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
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
    # review of batch 1c: the processed window kept the take's build-up, so with D s3002 the boom came at 390 ms,
    # after the recipe's siren and steel hit ("hit, build-up, hit again"); the body now starts at the boom too
    "breach": (TS, "hurt.breach", 0.90, 1.0),
}
# id -> fast-critic-ranked layers (L1, L1b, L2; no model): a whoosh, a paper and dust burst
LAYER_POOLS = {"wordshot": (TD, "wordshot-fire"), "blast": (TD, "blast")}
LAYER_NO_FLAGS = {"wordshot": {"double_onset", "lr_imbalance"}, "blast": {"lr_imbalance"}}

# Level match of the bodies (review of batch 1c). The raw takes come from the model at levels 20 dB or more apart
# (fire.impact.b: -19.6 to -45.9 LUFS-M after the 90 Hz high-pass), and a body layer at one gain made the quiet
# variants a Kenney front and embers with no body (fire.impact.b-v3, the machine's top, 54 % of its samples under
# -90 dBFS). Each body is measured as the layer plays it (its window through the layer's filters) after its first
# BODY_SKIP_MS, LUFS-M max: the body is what follows the strike (the front layer carries the strike). A first pass
# measured the whole window, and the transient-only takes (fire.impact.a F: a click 23-26 dB over what follows it)
# came out level with real bodies, so fire.impact.a v2 and v6 kept 50-60 ms within 30 dB of their peak. Each take is
# brought to the median level of its pool by its source gainDb (up or down: the layer gains of the recipe were set
# for a typical take; matching to the loudest raised the paper of blast.mix by up to 5 dB and made v1 rise too slowly
# for the 10 ms rule); one more than BODY_SPREAD_DB under the loudest is left out (a near-silent take raised 26 dB is
# mostly the model's floor, a click raised 20 dB is still a click).
BODY_SPREAD_DB = 10.0
BODY_SKIP_MS = 40.0
BODY_FILTERS = {
    "fire-a": [{"type": "highpass", "hz": 90, "order": 4}],
    "fire-b": [{"type": "highpass", "hz": 90, "order": 4}],
    "fire-c": [{"type": "highpass", "hz": 70, "order": 4}],
    "pine": [{"type": "highpass", "hz": 40, "order": 2}],
    "t4": [{"type": "highpass", "hz": 90, "order": 2}],
    "elite": [{"type": "highpass", "hz": 45, "order": 2}],
    "breach": [{"type": "highpass", "hz": 40, "order": 2}],
    "wordshot": [{"type": "highpass", "hz": 120, "order": 2}],      # no layer filter: the chain's 120 Hz high-pass
    "blast": [{"type": "highpass", "hz": 300}],
}


def _filters(key: str) -> list[dict]:
    return json.loads(json.dumps(BODY_FILTERS[key]))


def body_level(file: str, window: list[float], filters: list[dict]) -> float:
    """LUFS-M max of a body window as its layer plays it (mono, through the layer's filters), after its first
    BODY_SKIP_MS (the strike)."""
    from build import dsp, measure
    from build.sources import read_audio

    x = read_audio(Path(file), dsp.SR)
    y = x[dsp.ms_to_n(window[0] * 1000):dsp.ms_to_n(window[1] * 1000)].mean(axis=1, keepdims=True)
    y = dsp.apply_filters(y, filters)
    return float(measure.lufs_m_max(y[dsp.ms_to_n(BODY_SKIP_MS):], dsp.SR))


def level_match(rows: list[dict], filters: list[dict], level=body_level) -> tuple[list[dict], list[dict]]:
    """(kept, too quiet): each row gets level_lufs and gain_db (to the median of the kept rows); a row more than
    BODY_SPREAD_DB under the loudest is too quiet."""
    import statistics

    for r in rows:
        r["level_lufs"] = round(level(r["file"], r["window"], filters), 1)
    if not rows:
        return [], []
    top = max(r["level_lufs"] for r in rows)
    kept = [r for r in rows if top - r["level_lufs"] <= BODY_SPREAD_DB]
    quiet = [r for r in rows if top - r["level_lufs"] > BODY_SPREAD_DB]
    ref = statistics.median(r["level_lufs"] for r in kept)
    for r in rows:
        r["gain_db"] = round(ref - r["level_lufs"], 1)
    return kept, quiet


def _gen(b: dict) -> dict:
    """A body take as a recipe source, with its level match (source gainDb) when it has one."""
    src = gen_src(b)
    if b.get("gain_db"):
        src["gen"]["gainDb"] = float(b["gain_db"])
    return src


def peak_bodies(game: str, sid: str, run: str, length_s: float, max_peak_s: float, key: str) -> dict:
    rows, rej = [], []
    for f in sorted((id_dir(game, sid, run) / "raw").glob("*.f32.wav")):
        r = body_window(f, length_s)
        r["record"] = str(f.with_name(f.name.replace(".f32.wav", ".json")))
        r["name"] = f.name.replace(".f32.wav", "")
        r["ok"] = bool(not r["double_onset"] and not r["clip"] and r["pre_db"] <= -3.0 and r["peak_s"] <= max_peak_s)
        (rows if r["ok"] else rej).append(r)
    rows, quiet = level_match(rows, _filters(key))
    rows.sort(key=lambda r: -r["level_lufs"])
    return {"length_s": length_s, "n": len(rows) + len(rej) + len(quiet), "ok": len(rows),
            "bodies": _round_robin(rows, lambda r: prompt_of(r["name"])),
            "rejected": [{k: r[k] for k in ("name", "double_onset", "clip", "pre_db", "peak_s")} for r in rej],
            "quiet": [{k: r[k] for k in ("name", "level_lufs", "gain_db")} for r in quiet]}


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


def fresh(out: Path) -> Path:
    """An empty folder for a critic run that replaces an earlier one. The critic writes one JSON per input and never
    removes the others, so a take that a re-run of process refused would keep its old verdict there (review fix of
    1c). The earlier run moves to <name>.prev (the one before it is dropped): kept to compare, never read by a step."""
    import shutil

    if out.is_dir():
        prev = out.with_name(out.name + ".prev")
        if prev.exists():
            shutil.rmtree(prev)
        out.rename(prev)
    return out


def layer_pool(game: str, sid: str, key: str, run: str, force: bool) -> list[dict]:
    proc = id_dir(game, sid, run) / "processed"
    out = critic_out(run, game, f"layers-{sid}")
    if not (out / "_batch.json").is_file() or force:
        _critic_run([proc], [proc / "SOURCES.json"], fresh(out), card_path(game, sid), layers="L1,L1b,L2", cards=False)
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
    rows, quiet = level_match(rows, _filters(key))
    rows.sort(key=lambda r: -r["l2"])
    return _round_robin(rows, lambda r: prompt_of(r["name"])), quiet


def step_sources(run: str, game: str | None = None, force: bool = False) -> dict:
    out = base_dir(run) / "sources.json"
    pools = json.loads(out.read_text("utf-8")) if out.is_file() and not force else {}
    for key, (g, sid, length, max_pk) in PEAK_POOLS.items():
        if g in _games(game) and (key not in pools or force):
            pools[key] = peak_bodies(g, sid, run, length, max_pk, key)
            _say(f"thân {key} ({sid}): {pools[key]['ok']}/{pools[key]['n']} dùng được (một đầu tiếng, không cắt vào âm "
                 f"trước, không clip, đỉnh trước {max_pk:g} s, không nhỏ hơn thân to nhất quá {BODY_SPREAD_DB:g} dB); "
                 f"nhỏ quá: {len(pools[key]['quiet'])}; cân mức {min([0.0] + [b['gain_db'] for b in pools[key]['bodies']]):+g} "
                 f"tới {max([0.0] + [b['gain_db'] for b in pools[key]['bodies']]):+g} dB")
    for key, (g, sid) in LAYER_POOLS.items():
        if g in _games(game) and (key not in pools or force):
            rows, quiet = layer_pool(g, sid, key, run, force)
            pools[key] = {"n": len(rows) + len(quiet), "ok": len(rows), "bodies": rows,
                          "quiet": [{k: r[k] for k in ("name", "level_lufs", "gain_db")} for r in quiet]}
            _say(f"lớp {key} ({sid}): {len(rows)} bản, nhỏ quá {len(quiet)}; đầu: {', '.join(r['name'] for r in rows[:4])}")
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
           "lớp trầm chỉ nằm dưới, có thân và đuôi đè lên. Mỗi bản Stable Audio 3 của lớp thân được cân mức (gainDb của "
           "nguồn) theo LUFS-M max của cửa sổ qua bộ lọc của lớp, lên bằng bản to nhất của bể; bản nhỏ hơn quá 10 dB bị "
           "loại (sửa sau phản biện: bản thô lệch nhau tới 26 dB). ")


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
                     "filters": _filters("fire-a")}, [_gen(b) for b in A[:n]]),
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
                     "filters": _filters("fire-b")}, [_gen(b) for b in B[:nb]]),
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
                     "filters": _filters("fire-c")}, [_gen(b) for b in C[:nc]]),
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
                     "filters": _filters("pine")}, [_gen(b) for b in P[:npb]]),
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
            [_cycle({"id": "whoosh", "role": "body", "fadeOutMs": 60}, [_gen(b) for b in W]),
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
                     "filters": _filters("blast")}, [_gen(b) for b in P])],
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
            [_cycle({"id": "body", "role": "body", "filters": _filters("elite")},
                    [_gen(b) for b in E]), *arcs],
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
            "thép. Thân là bản Stable Audio 3 prompt D–F của lô 1c (tạo 2 s), cửa sổ 900 ms từ 4 ms trước đỉnh tiếng nổ, lọc "
            "cao 40 Hz, nên còi vào ngay trên tiếng nổ (lượt đầu lấy cửa sổ process.py có phần tụ lực: ở thân D s3002 tiếng "
            "nổ tới ở 390 ms, sau còi); còi giữ như lô 1 (440/330 Hz vuông, lọc thấp 1,6 kHz, 90 ms mỗi nốt ở 30 và 140 ms). "
            "Đuôi hàm mũ từ 650 ms (lô 1: 720 ms tối đa, thân A–C đã bỏ). Biến thể n dùng thân n.",
            [_cycle({"id": "body", "role": "body", "filters": _filters("breach")},
                    [_gen(b) for b in BR]), *json.loads(json.dumps(siren))],
            _chain(960, 650, release_ms=80), len(BR), 3533, "sfx/alerts/hurt-breach")
        heads = [_lib(f"impactPlate_heavy_00{k}") for k in (0, 2, 4)] * 2
        b2_layers = [_cycle({"id": "hit", "role": "attack", "gainDb": -3, "filters": [{"type": "lowpass", "hz": 2500, "order": 2}],
                             "trim": {"endMs": 120}, "fadeOutMs": 60}, heads[:len(BR)]),
                     {"id": "boom", "role": "sub", "gainDb": -10, "source": {"synth": "sub_thump", "params": {
                         "startHz": 70, "endHz": 38, "glideMs": 120, "durMs": 300, "decayMs": 280, "driveDb": 6}}},
                     _cycle({"id": "body", "role": "body", "offsetMs": 10,
                             "filters": [{"type": "highpass", "hz": 40, "order": 2}, {"type": "lowpass", "hz": 1200, "order": 4}]},
                            [_gen(b) for b in BR])]
        for s in json.loads(json.dumps(siren)):
            s["filters"] = [{"type": "lowpass", "hz": 1000, "order": 8}]
            b2_layers.append(s)
        out["hurt.breach.b2"] = _recipe(
            TS, "hurt.breach.b2", "alarm", "nen",
            Q6_NOTE + "Bản 2 của hurt.breach (như hurt.breach.b2 của lô 1, dựng lại cho 800 ms): cú đập thép Kenney Impact "
            "Plate heavy (lọc thấp 2,5 kHz) và lớp nổ trầm tổng hợp 70→38 Hz 300 ms −10 dB ở 0 ms làm tiếng phát; thân Stable "
            "Audio 3 prompt D–F từ đỉnh tiếng nổ (như hurt.breach), lọc 40 Hz–1,2 kHz (thép rên và vang hành lang dưới dải "
            "giọng); còi lọc thấp 1 kHz. Đường xuất riêng sfx/alerts/hurt-breach-b2 (lượt đầu trùng đường với hurt.breach, "
            "nên bộ ogg sau ghi đè bộ trước). Biến thể n dùng cú đập n và thân n.",
            b2_layers, _chain(960, 650, release_ms=80), len(BR), 3536, "sfx/alerts/hurt-breach-b2")
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
                     "filters": _filters("t4")}, [_gen(b) for b in T4]),
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
            out = recipe_run(g, rid, run)
            # the committed recipe file always matches its render: written only when it is rendered (review of 1c)
            if out.is_dir() and (out / "render.json").is_file() and not force:
                done = out / "recipe.json"
                if done.is_file() and json.loads(done.read_text("utf-8")) != recipes[rid]:
                    _say(f"recipe {g}/{rid}: CẢNH BÁO nguồn đã đổi so với bản dựng ở {out}; {p.name} giữ như bản dựng, "
                         "thêm --force để dựng lại")
                else:
                    _say(f"recipe {g}/{rid}: đã có {out}")
                continue
            p.write_text(json.dumps(recipes[rid], ensure_ascii=False, indent=1) + "\n", "utf-8")
            # build.render writes over the masters it makes and leaves the others: a re-render with fewer variants
            # (fire.impact.b 8 -> 6 after the level match) would leave v7, v8 of the old one for the critic to rank
            res = render.render(p, out=fresh(out), spec=card_path(g, sid_of(g, rid)))
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
# ranked at raw stage too although the id has eligible finals: the session offers one of their rule-blocked whole
# takes with a label (Q6_REWRITE §11.3 #2): the pine bomb (a boom that swells, often after a fuse or a crack, §11.3 #1)
# and the bow (21/24 whole takes slower than 10 ms)
INFO_EXTRA = {DH: ("trap.pine-bomb.trigger",), TD: ("arrow-fire",)}


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


def info_inputs(run: str, game: str, sid: str) -> tuple[list[Path], list[Path]]:
    """Inputs of the raw-stage run of one id: its processed takes, its recipe masters, its owner-rated references and
    the batch 1 render kept in use for it."""
    dirs, srcs = finals(run, game)
    out_d, out_s = [], []
    for d, s_ in zip(dirs, srcs):
        if d.is_file():
            label = next((lb for lb, f in REFS.get(game, {}).items() if f == d), "")
            mine = label.split(" ")[0] == sid
        elif d.name == "processed":
            mine = d.parent.parent.name == sid
        else:                        # <id>/<run>-recipe-<rid>/masters, <id>/b1-recipe-<rid>/masters
            mine = d.parent.parent.name == sid
        if mine:
            out_d.append(d)
            out_s.append(s_)
    return out_d, out_s


def step_critic(run: str, game: str | None = None, force: bool = False) -> None:
    for g in _games(game):
        out = critic_out(run, g, "final")
        if (out / "_batch.json").is_file() and not force:
            _say(f"critic {g}: đã có {out}")
        else:
            dirs, srcs = finals(run, g)
            wait_heavy_free(f"critic {g}")
            t0 = time.time()
            _say(f"critic {g} final ({len(dirs)} mục): mã {_critic_run(dirs, srcs, fresh(out), LAB / 'specs' / g)}, "
                 f"{time.time() - t0:.0f} s")
        wanted = list(dict.fromkeys([*info_ids(run, g), *INFO_EXTRA.get(g, ())]))
        # a raw-stage run of an id that no longer needs one (its takes pass now) would still feed select(): set aside
        for old in base_dir(run, g).glob("critic-info-*"):
            if old.is_dir() and not old.name.endswith(".prev") and old.name[len("critic-info-"):] not in wanted:
                fresh(old)
                _say(f"critic {g}: {old.name} không còn cần (bản nguyên khối đã qua), chuyển sang .prev")
        for sid in wanted:
            info = critic_out(run, g, f"info-{sid}")
            if (info / "_batch.json").is_file() and not force:
                continue
            # every file a listening item of this id can hold (takes, recipes, owner-rated takes, the batch 1 render kept
            # in use) is ranked in this one run: `critic agreement` compares the combined z-scores of one rank group,
            # so an item never mixes this run with critic-final (review of batch 1c)
            dirs, srcs = info_inputs(run, g, sid)
            wait_heavy_free(f"critic info {sid}")
            rc = _critic_run(dirs, srcs, fresh(info), card_path(g, sid), stage="raw")
            _say(f"critic {g}/{sid} giai đoạn raw (bản nguyên khối chỉ bị luật lên hoặc luật độ dài chặn): mã {rc}")
        raw = critic_out(run, g, "raw")
        if not (raw / "_batch.json").is_file() or force:
            raws = [id_dir(g, sid, run) / "raw" for sid in JOBS[g] if (id_dir(g, sid, run) / "raw").is_dir()]
            rc = _critic_run(raws, [], fresh(raw), LAB / "specs" / g, stage="raw", layers="L1,L1b", cards=False)
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
        # the trial tree is rebuilt from the current renders every time: a release left from an earlier render (the
        # first hurt.breach.b2 on sfx/alerts/hurt-breach) would trip the export-path guard or hide a stale file
        fresh(base_dir(run, g) / "staging")
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
        # a window the card's max cut: tail_ms of the file is the cap's decay (the window's end minus its peak), so the
        # rule reads the take's own tail on its raw window (review of 1c)
        r = hi(m.get("tail_ms_natural", m.get("tail_ms")), *tail)
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


_NAT: dict[str, dict] = {}


def natural_tail(d: dict) -> dict:
    """The take's own tail when the card's max cut its window (proc.json): tail_ms (peak to the last frame over the
    critic's floor, as critic.features) on the raw float from the window start to the next event or the file end, and
    the level where the window was cut. Empty for a window that ends on the take's own decay, or not a whole take."""
    key = d["file"]["path"]
    if key not in _NAT:
        _NAT[key] = _natural_tail(d)
    return _NAT[key]


def _natural_tail(d: dict) -> dict:
    if _kind(d) != "sa3":
        return {}
    pj = _proc(d)
    if not pj or not (pj.get("window") or {}).get("capped"):
        return {}
    import soundfile as sf
    from critic import features as F
    w = pj["window"]
    x, sr = sf.read(pj["source_f32"], always_2d=True, dtype="float64")
    a = int(w["window_s"][0] * sr)
    end = x.shape[0] if w["end_kind"] in ("decayed", "file-end") else int((w["onset_s"] + w["natural_ms"] / 1000) * sr)
    mono = x[a:max(a + 1, end)].mean(axis=1)
    env_ = F.envelope(mono, sr)
    return {"tail_ms_natural": F.dynamics(mono, sr, env_)["tail_ms"],
            "cut_db": (pj.get("tail") or {}).get("natural_end_db")}


def _row(d: dict, final: dict | None = None) -> dict:
    """One report row; `final` = the final-stage doc of a file ranked in a raw-stage info run (verdict from final)."""
    m, s_ = dict(d["metrics"], **natural_tail(d)), d.get("score") or {}
    f = final or d
    return {"stem": d["file"]["stem"], "file": d["file"]["path"], "sha8": d["file"].get("sha256", "")[:8],
            "kind": _kind(d), "ref": _ref_label(d), "verdict": f["verdict"], "blocking": f["L1"]["blocking"],
            "rank_stage": "raw" if final is not None else "final",
            "rank": s_.get("rank"), "n_ranked": s_.get("n_ranked"), "combined": s_.get("combined"),
            "L2": (d.get("L2") or {}).get("score"), "flags": sorted(_flags(d)), "verified": _verified(d),
            "q6": q6_checks(dict(d, metrics=m)),
            "metrics": {k: m.get(k) for k in ("duration_ms", "attack_ms", "tail_ms", "tail_ms_natural", "cut_db",
                                               "punch_db", "share_below_150",
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
        e["cut_loud"] = sum(1 for d in ok if (natural_tail(d).get("cut_db") or -999) > CUT_DB)
        for d in ok:
            for rule, v in q6_checks(dict(d, metrics=dict(d["metrics"], **natural_tail(d)))).items():
                e["q6"].setdefault(rule, {"đạt": 0, "giữa": 0, "trượt": 0})[v] += 1
        e["loop_eval"] = loop_eval(game, sid)
        out[sid] = e
    return out


Q6_RULE_VI = {"tail": "đuôi", "punch": "cú đấm/thân", "body": "thân 150–800 Hz", "lone_low_hit": "cú trầm đứng riêng"}


def context_rows(run: str, game: str) -> list[str]:
    """The in-scene numbers of every listening pick (step context), when the renders exist."""
    p = base_dir(run, game) / "context" / "context.json"
    if not p.is_file():
        return []
    renders = json.loads(p.read_text("utf-8")).get("renders") or {}
    L = [f"### Bản dựng trong bối cảnh ({game})", "",
         "Giọng: dải 1–4 kHz của giọng đọc so với phần còn lại, 300 ms đầu mỗi từ, từ kém nhất (bài C, đạt từ 10 dB). "
         "1–4 kHz tụt: năng lượng 1–4 kHz của file tụt bao nhiêu sau 100 ms (luật âm xong từ, đạt từ 15 dB). Loa nhỏ: "
         "mức mất qua lọc cao 200 Hz. Hổng, trũng: số đo 'Liên thanh' của stem súng (BATCH1_BRIEF §3.5; hổng < 10 %, "
         "trũng < 12 dB). Đỉnh: bản trộn trước mức hạ chung của file dựng (−4, −11, −6 dB theo game), nên file nghe không clip.", "",
         "| Id | Vai trò | Bản | Kịch bản | Giọng min dB | 1–4 kHz tụt dB | Loa nhỏ dB | Hổng % | Trũng dB | Đỉnh dBTP |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for sid, rr in renders.items():
        for name, r in rr.items():
            m = r.get("metrics") or {}
            b = m.get("burst") or {}
            bd = m.get("focus_band_decay") or {}
            drop = bd.get("drop_db_at_100ms")
            drop = min(drop) if isinstance(drop, list) and drop else (None if isinstance(drop, list) else drop)
            L.append(f"| `{sid}` | {r.get('role')} | `{name}` | {r.get('scenario')} | {_fmt((m.get('voice') or {}).get('min_db'))} | "
                     f"{_fmt(drop)} | {_fmt(m.get('focus_small_speaker_loss_db'))} | "
                     f"{_fmt(b.get('gap_time_pct'))} | {_fmt(b.get('dip_median_db'))} | "
                     f"{_fmt((m.get('mix') or {}).get('true_peak_dbtp'))} |")
    return L + [""]


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
              "| Id | Bản mới | Qua L1 | Nghe được | Bị chặn vì | Lặp L3–L5 | Q6 (bản nghe được) | Cắt khi còn trên −30 dB |",
              "|---|---|---|---|---|---|---|---|"]
        for sid, e in s.items():
            q = "; ".join(f"{Q6_RULE_VI[k]} {v['đạt']}/{v['giữa']}/{v['trượt']}" for k, v in e["q6"].items()) or "–"
            blk = ", ".join(f"{k} {v}" for k, v in sorted(e["blocking"].items(), key=lambda kv: -kv[1])) or "–"
            le = e["loop_eval"]
            lp = f"bật, {_fmt(float(le['rate_hz']), 2)} Hz" if le["enabled"] and le["rate_hz"] else ("bật" if le["enabled"] else "tắt")
            L.append(f"| `{sid}` | {e['n_new']} | {e['pass']} | {e['eligible']} | {blk} | {lp} | {q} | {e['cut_loud']} |")
        L += ["", "Q6: số bản đạt/giữa/trượt trong các bản nghe được; luật đuôi đọc đuôi gốc của bản bị cắt theo độ dài tối "
              "đa của thẻ (đuôi của file là đường tắt dần của bước xử lý). Lặp L3–L5: `critic.loop_eval` của thẻ (bộ chấm "
              "còn tự lặp mọi file dưới 300 ms). Cột cuối: bản nghe được bị cắt ở độ dài tối đa khi âm gốc còn trên −30 dB.", ""]
        for sid, e in s.items():
            L += [f"### `{sid}`", "", "| Vai trò | Bản | Loại | L1 | Hạng | Điểm | L2 | Dài ms | Lên ms | Đuôi ms (gốc; cắt ở dB) | "
                  "Đấm dB | <150 Hz | 150–800 Hz | Q6 | Cờ |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
            for r in e["picks"] + [dict(r, role=r["ref"] or "lô 1 dùng tiếp") for r in e["refs"]]:
                m = r["metrics"]
                L.append(f"| {r['role']} | `{r['stem']}` | {r['kind']} | {r['verdict']} {','.join(r['blocking'])} | "
                         f"{r['rank'] or '–'}/{r['n_ranked'] or '–'}{' (raw)' if r['rank_stage'] == 'raw' else ''} | {_fmt(r['combined'], 2)} | {_fmt(r['L2'], 2)} | "
                         f"{_fmt(m.get('duration_ms'), 0)} | {_fmt(m.get('attack_ms'))} | {_fmt(m.get('tail_ms'), 0)}"
                         + (f" (gốc {_fmt(m.get('tail_ms_natural'), 0)}; {_fmt(m.get('cut_db'))})" if m.get("tail_ms_natural") is not None else "")
                         + f" | {_fmt(m.get('punch_db'))} | {_pct(m.get('share_below_150'))} | {_pct(m.get('share_150_800'))} | "
                         f"{_q6_cell(r['q6'])} | {', '.join(r['flags']) or '–'} |")
            L.append("")
        L += context_rows(run, g)
    path = base_dir(run) / "REPORT.md"
    path.write_text("\n".join(L) + "\n", "utf-8")
    (base_dir(run) / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1, default=str), "utf-8")
    _say(f"báo cáo {path}")
    return path


# ---------------------------------------------------------------- step 8: listening lists (plan §4.6 step 2)

# per item, references included: the board lays out 4 cards a row, and at 1280x720 a fifth card pushes the tag row
# below the fold (measured 147 px on gun.xung); batch 1 offered 2-4
MAX_CANDIDATES = 4
# probes (a take from the lower half of the machine's ranking) at 6/19 ids, about 30 % (§4.6 step 2), on ids where the
# references and rule-blocked takes leave room. Not fire.cast (review of 1c): its four Q6 prompts E-H come first.
PROBE_IDS = {DH: ("fire.impact.a", "fire.impact.c"), TD: ("ink-puff", "blast"), TS: ("hit.t4", "hurt.breach")}
RULE_NOTE = {     # shown to the owner (board note, at most 80 characters)
    "fire.impact.b": "Bị luật chặn: lửa bùng lên chậm (> 10 ms); chấm như mọi bản",
    "fire.impact.c": "Bị luật chặn: lửa bùng lên chậm (> 10 ms); chấm như mọi bản",
    "impact.multi": "Bị luật chặn: lửa bùng lên chậm (> 10 ms); chấm như mọi bản",
    "trap.pine-bomb.trigger": "Bị luật chặn: tiếng nổ lên chậm (> 10 ms); chấm như mọi bản",
    "enemy.quadruped.howl": "Bị luật chặn: tiếng tru lớn dần chậm (> 30 ms); chấm như mọi bản",
    "arrow-fire": "Bị luật chặn: tiếng vút lên chậm (> 10 ms); chấm như mọi bản",
    "wordshot-fire": "Bị luật chặn: tiếng vút lên chậm (> 10 ms); chấm như mọi bản",
}
CURRENT_NOTE = "Cách game đang phát: chỉ viên chẵn, không nền, không đuôi"
# a take of a BUILD_UP id the card's max cut while it still sounded over CUT_DB (review of 1c, Q6): its tail is the cap's
# exponential decay, not the take's own echo. The label lets the owner tell a card too short from a take with no tail.
CUT_NOTE = "đuôi rút vừa thẻ"
CUT_DB = -30.0
# gun.xung (Q6 §7 "đặt cạnh các hướng lô 1 trong Liên thanh 3 s"): batch 1 direction 2 (its set in session 1-ts-s1,
# bed 16 dB under the shot: the better burst numbers of batch 1 and the fixed gun of every Tuyến Cuối render here;
# direction 3 is the same set with a louder bed, direction 1 stays in 1-ts-s1: four cards fit 1280x720), the batch 1c
# whole takes per prompt as a set (A the prompt's eligible takes, B the same takes 5 dB lower, as batch 1's set B),
# and 0a v2 as the game plays today
B1_TS = env.WORK / "_batch1" / TS / "b1"
GUN_B1 = ("direction-2",)
GUN_PROMPTS = ("I", "J", "K")
GUN_B_DB = -5.0              # batch1_ts.GUN_B_DB: set B 4-6 dB under set A (BATCH1_BRIEF §3.2)
GUN_SET_MAX = 4


def _load(out: Path) -> dict[str, dict]:
    """Critic docs of one run by stem, each knowing its run folder (critic JSON and card live there)."""
    docs = _docs(out)
    for d in docs.values():
        d["_out"] = str(out)
    return docs


def _eligible(d: dict) -> bool:
    return d["verdict"] == "PASS" and _verified(d) and not _flags(d) & NO_PICK_FLAGS and _kind(d) in ("sa3", "recipe")


def _prompt_of(d: dict) -> str:
    return prompt_of(d["file"]["stem"])


def _rule_note(sid: str, final: dict) -> str | None:
    note = RULE_NOTE.get(sid)
    if note and "duration" in final["L1"]["blocking"]:
        note += "; dài hơn thẻ"
    return note


def _proc(d: dict) -> dict | None:
    p = Path(d["file"]["path"]).with_suffix(".proc.json")
    return json.loads(p.read_text("utf-8")) if p.is_file() else None


def cut_while_loud(game: str, sid: str, d: dict) -> bool:
    """A whole take of a BUILD_UP id whose window the card's max cut while the take sounded over CUT_DB."""
    if sid not in BUILD_UP.get(game, set()) or _kind(d) != "sa3":
        return False
    pj = _proc(d) or {}
    nat = (pj.get("tail") or {}).get("natural_end_db")
    return bool((pj.get("window") or {}).get("capped")) and nat is not None and nat > CUT_DB


def join_notes(*parts: str | None) -> str | None:
    """Owner-visible notes joined with '; ', each kept only while the note fits the board (80 characters)."""
    from board.session import MAX_NOTE
    out = ""
    for p in parts:
        if p and len(out + ("; " if out else "") + p) <= MAX_NOTE:
            out += ("; " if out else "") + p
    return out or None


def _spread(ranked: list[dict], want: int) -> list[dict]:
    """The best `want` of a ranking, one per prompt first (the prompts are the directions of the card)."""
    out: list[dict] = []
    seen: set[str] = set()
    for d in ranked:
        if len(out) < want and _prompt_of(d) not in seen:
            out.append(d)
            seen.add(_prompt_of(d))
    for d in ranked:
        if len(out) < want and d not in out:
            out.append(d)
    return out


def _probe(game: str, sid: str, order: list[dict], used: set[str]) -> dict | None:
    pool = [d for d in order[max(1, len(order) // 2):] if d["file"]["path"] not in used]
    if not pool:
        return None
    rng = random.Random(int(hashlib.sha256(f"batch-1c:{game}:{sid}".encode()).hexdigest()[:8], 16))
    return rng.choice(sorted(pool, key=lambda d: d["file"]["stem"]))


def _ref_role(label: str) -> str:
    tag = label.split(" ")[1]
    return f"ref-{tag}" if tag in ("0a", "0b") else "ref"


def select(run: str, game: str) -> dict[str, dict]:
    """Per id the listening list, at most MAX_CANDIDATES, filled in this order of priority: the machine's top and the
    best of the other kind (recipe or whole take); rule-blocked whole takes with a label (one, or up to three of
    different prompts when nothing is eligible); the takes the owner rated and the batch 1 render kept in use, blind
    (consistency pairs); a probe at PROBE_IDS; the best take of every prompt not offered yet (the prompts are the Q6
    directions of the card); then the most different take of the machine's upper half, of a prompt not offered first.
    An item holding a take ranked only at raw stage takes every critic doc from that raw-stage run (info_inputs ranked
    all of them there), so `critic agreement` compares one rank group per item."""
    final = _load(critic_out(run, game, "final"))
    sel: dict[str, dict] = {}
    for sid in JOBS[game]:
        if game == TS and sid == "gun.xung":
            sel[sid] = gun_select(run, final)
            continue
        mine = sorted([d for d in final.values() if _sid(d) == sid], key=_rank)
        ok = [d for d in mine if _eligible(d)]
        info = _load(critic_out(run, game, f"info-{sid}"))
        e: dict = {"n_new": sum(1 for d in mine if _kind(d) in ("sa3", "recipe")), "eligible": len(ok)}
        core: list[tuple[dict, str, str | None]] = []
        rule: list[tuple[dict, str, str | None]] = []
        refs: list[tuple[dict, str, str | None]] = []
        if ok:
            core.append((ok[0], "top", None))
            other = [d for d in ok if _kind(d) != _kind(ok[0])]
            if other:
                core.append((other[0], "best-recipe" if _kind(other[0]) == "recipe" else "best-take", None))
        if info:
            blocked = [d for d in mine if _kind(d) == "sa3" and d["verdict"] == "BLOCK" and _verified(d)
                       and set(d["L1"]["blocking"]) <= INFO_BLOCKS and not _flags(d) & NO_PICK_FLAGS]
            ranked = sorted([info[d["file"]["stem"]] for d in blocked if d["file"]["stem"] in info
                             and not _flags(info[d["file"]["stem"]]) & NO_PICK_FLAGS], key=_rank)
            e["rule_blocked_whole"] = len(blocked)
            rule = [(d, "rule-blocked", _rule_note(sid, final[d["file"]["stem"]])) for d in _spread(ranked, 1 if ok else 3)]
            if not ok:
                # a recipe blocked by the same rule (wordshot-fire.mix): the best raw-stage rank (best L2 without one)
                recs = sorted([d for d in mine if _kind(d) == "recipe" and d["verdict"] == "BLOCK"
                               and set(d["L1"]["blocking"]) <= INFO_BLOCKS and not _flags(d) & NO_PICK_FLAGS],
                              key=lambda d: (_rank(info[d["file"]["stem"]]) if d["file"]["stem"] in info else 1e9,
                                             -((d.get("L2") or {}).get("score") or 0.0)))
                if recs:
                    rule.append((recs[0], "rule-blocked-recipe", _rule_note(sid, recs[0])))
        for label, f in REFS.get(game, {}).items():
            if label.split(" ")[0] != sid:
                continue
            d = next((x for x in mine if x["file"]["path"] == str(f)), None)
            if d is None:
                continue
            fin = d
            if d["verdict"] != "PASS":
                d = next((x for x in info.values() if x["file"]["path"] == d["file"]["path"]), d)
            # blind, unless every new take of the id carries the rule label too (the howl): then it carries it
            note = _rule_note(sid, fin) if (not ok and fin["verdict"] == "BLOCK"
                                            and set(fin["L1"]["blocking"]) <= INFO_BLOCKS) else None
            refs.append((d, _ref_role(label), note))
        kept = [d for d in mine if _kind(d) == "b1" and d["verdict"] == "PASS" and not _flags(d) & NO_PICK_FLAGS]
        if kept:
            refs.append((kept[0], "b1-kept", None))
        ordered = core + rule + refs
        used = {d["file"]["path"] for d, _, _ in ordered}
        if sid in PROBE_IDS.get(game, ()) and ok:
            pr = _probe(game, sid, ok, used)
            if pr is not None:
                ordered.append((pr, "probe", None))
                used.add(pr["file"]["path"])
        if ok:
            heard = {_prompt_of(d) for d, _, _ in ordered if _kind(d) == "sa3"}
            for d in ok:                      # every Q6 direction not offered yet: its best take
                if _kind(d) == "sa3" and _prompt_of(d) not in heard and d["file"]["path"] not in used:
                    ordered.append((d, "other-prompt", None))
                    used.add(d["file"]["path"])
                    heard.add(_prompt_of(d))
            pool = [d for d in _upper(ok) if d["file"]["path"] not in used]
            dis = _distinct(ok[0], [d for d in pool if _prompt_of(d) not in heard]) or _distinct(ok[0], pool)
            if dis is not None:
                ordered.append((dis, "distinct", None))
        e["left_out"] = [r for _, r, _ in ordered[MAX_CANDIDATES:]]
        ordered = ordered[:MAX_CANDIDATES]
        if any(d.get("_out") == str(critic_out(run, game, f"info-{sid}")) for d, _, _ in ordered):
            # by path: a stem can repeat across folders (the recipe's -v3 and the 0a -v3 of the pine bomb: "-v3__2")
            by_path = {x["file"]["path"]: x for x in info.values()}
            swapped = [(by_path.get(d["file"]["path"], d), r, n) for d, r, n in ordered]
            e["mixed_runs"] = [d["file"]["stem"] for d, _, _ in swapped if d["_out"] != str(critic_out(run, game, f"info-{sid}"))]
            ordered = swapped
        e["picks"] = [{"docs": [d], "role": r, "note": join_notes(n, CUT_NOTE if cut_while_loud(game, sid, d) else None)}
                      for d, r, n in ordered]
        sel[sid] = e
    return sel


def _b1_doc(path: Path) -> dict | None:
    """The batch 1 critic doc of a batch 1 gun file (its JSON and card for the board)."""
    out = B1_TS / "critic-final"
    p = out / f"{path.stem}.json"
    if not p.is_file():
        return None
    d = json.loads(p.read_text("utf-8"))
    if d["file"]["path"] != str(path):
        return None
    d["_out"] = str(out)
    return d


def gun_select(run: str, final: dict[str, dict]) -> dict:
    mine = sorted([d for d in final.values() if _sid(d) == "gun.xung"], key=_rank)
    ok = [d for d in mine if _eligible(d)]
    e: dict = {"n_new": sum(1 for d in mine if _kind(d) == "sa3"), "eligible": len(ok), "picks": [], "prompts": {}}
    for name in GUN_B1:
        j = B1_TS / "context" / "gun.xung" / f"{name}.json"
        if not j.is_file():
            continue
        doc = json.loads(j.read_text("utf-8"))
        st = {k: [Path(p) for p in v] for k, v in doc["slots"]["gun.xung"].items() if isinstance(v, list)}
        a, b = st.get("A", []), st.get("B", [])
        files = [x for pair in zip(a, b) for x in pair] + a[len(b):] + b[len(a):]
        docs = [_b1_doc(p) for p in files]
        e["picks"].append({"files": files, "docs": docs if all(docs) else [], "set": st, "role": f"b1-{name}",
                           "bed_db": float(doc.get("bed_db_under_shot") or 16.0), "note": None})
    for p in GUN_PROMPTS:
        takes = [d for d in ok if _prompt_of(d) == p][:GUN_SET_MAX]
        allp = [d for d in mine if _prompt_of(d) == p]
        e["prompts"][p] = {"takes": len(allp), "eligible": len(takes),
                           "unverified": sum(1 for d in allp if not _verified(d)),
                           "flagged": sum(1 for d in allp if _flags(d) & NO_PICK_FLAGS),
                           "blocked": sum(1 for d in allp if d["verdict"] != "PASS")}
        if takes:
            fs = [Path(d["file"]["path"]) for d in takes]
            e["picks"].append({"files": fs, "docs": takes, "set": {"A": fs, "B": fs, "B_db": GUN_B_DB},
                               "role": f"1c-{p}", "bed_db": 16.0, "note": None})
    ref = [d for d in mine if _kind(d) == "ref"]
    if ref:
        e["picks"].append({"files": [Path(ref[0]["file"]["path"])], "docs": ref[:1], "role": "ref-0a-current",
                           "config": "current", "note": CURRENT_NOTE})
    while len(e["picks"]) > MAX_CANDIDATES:      # the 1c set with the fewest eligible takes gives way
        sets = [p for p in e["picks"] if p["role"].startswith("1c-")]
        drop = min(sets, key=lambda p: len(p["files"]))
        e["picks"].remove(drop)
        e.setdefault("left_out", []).append(drop["role"])
    return e


# ---------------------------------------------------------------- step 9: in-game context renders

SCENARIO = {DH: {"fire.cast": "dh-cast-chain", "fire.impact.a": "dh-cast-chain", "fire.impact.b": "dh-cast-chain",
                 "fire.impact.c": "dh-cast-chain", "impact.multi": "dh-cast-chain",
                 "trap.pine-bomb.trigger": "dh-trap", "enemy.quadruped.howl": "dh-pack"},
            TD: {"arrow-fire": "td-wordhit-chain", "wordshot-fire": "td-wordhit-chain", "ink-puff": "td-wordhit-chain",
                 "blast": "td-wordhit-chain", "call-chop": "td-night"},
            TS: {"kill.swarm": "ts-xung-3s-kills", "kill.elite": "ts-xung-3s-kills", "hurt.breach": "ts-breach",
                 "gun.xung": "ts-xung-3s", "hit.t1": "ts-xung-3s", "hit.t2": "ts-xung-3s", "hit.t4": "ts-xung-3s"}}
CTX_KEY = {DH: "scene", TD: "scene", TS: "burst"}       # Tuyến Cuối: "Liên thanh 3 s"; ts-breach is a scene


def ctx_key(game: str, sid: str) -> str:
    return "scene" if sid == "hurt.breach" else CTX_KEY[game]


def ctx_dir(run: str, game: str) -> Path:
    return base_dir(run, game) / "context"


def _b1_fixed(game: str) -> dict:
    """The fixed slots of the batch 1 renders of this game (beds, the word-hit scale, the gun set, ...)."""
    p = env.WORK / "_batch1" / game / "b1" / "context" / "context.json"
    if not p.is_file():
        return {}
    out: dict = {}
    for k, v in (json.loads(p.read_text("utf-8")).get("fixed") or {}).items():
        if isinstance(v, dict):
            out[k] = {n: ([Path(x) for x in f] if isinstance(f, list) else Path(f)) for n, f in v.items()}
        elif isinstance(v, list):
            out[k] = [Path(x) for x in v]
        else:
            out[k] = Path(v)
    return out


def fixed_slots(game: str, sel: dict) -> dict:
    """Every slot a render does not test: this batch's first pick for the 1c ids (Q6 replaces the batch 1 takes),
    batch 1's fixed take for the rest (the forest bed the owner rated 4/5, the word-hit scale, batch 1's gun set with
    the better burst numbers, the mechanical bed and tail)."""
    out = _b1_fixed(game)
    for sid in JOBS[game]:
        if game == TS and sid == "gun.xung":
            continue
        picks = sel.get(sid, {}).get("picks") or []
        if picks:
            f = Path(picks[0]["docs"][0]["file"]["path"])
            out[sid] = [f] if game == TS else f
    return out


def _pick_name(game: str, sid: str, p: dict) -> str:
    return p["role"] if (game == TS and sid == "gun.xung") else p["docs"][0]["file"]["stem"]


def _jsonable(v):
    if isinstance(v, dict):
        return {k: _jsonable(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [_jsonable(x) for x in v]
    return str(v) if isinstance(v, Path) else v


def pick_slots(game: str, sid: str, p: dict, fixed: dict) -> tuple[dict, str, float]:
    """(slots, playback configuration, bed dB) of one pick's render: the fixed slots with the pick in its own."""
    slots = dict(fixed)
    config, bed = p.get("config", "proposed"), float(p.get("bed_db") or 16.0)
    if game == TS and sid == "gun.xung":
        slots[sid] = p["set"] if p.get("set") else [Path(f) for f in p["files"]]
    else:
        f = Path(p["docs"][0]["file"]["path"])
        slots[sid] = [f] if game == TS else f
    return slots, config, bed


def render_pick(game: str, sid: str, slots: dict, config: str, bed: float, out: Path) -> dict:
    if game == DH:
        from context import scenes
        return scenes.render(SCENARIO[game][sid], slots, out, focus=sid)
    if game == TD:
        from context import td_scenes
        return td_scenes.render(SCENARIO[game][sid], slots, out, focus=sid)
    from context import ts_scenes
    return ts_scenes.render(SCENARIO[game][sid], slots, out, focus=sid, config=config, bed_db=bed)


def _file_id(v):
    """A slot's file by path and content: a re-processed take keeps its path (review fix of 1c: the knee moved, so the
    processed files changed under the same names, and a path-only signature reused the old renders)."""
    if isinstance(v, dict):
        return {k: _file_id(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [_file_id(x) for x in v]
    if isinstance(v, Path):
        from build import ledger
        return f"{v}#{ledger.sha256_file(v)[:16]}" if v.is_file() else str(v)
    return v


def _slots_sig(slots: dict, config: str, bed: float) -> str:
    return hashlib.sha256(json.dumps([_file_id(slots), config, bed], sort_keys=True).encode()).hexdigest()[:16]


def step_context(run: str, game: str | None = None, force: bool = False) -> dict:
    """Each pick in its scene (context/), every other slot fixed: the renders of one id differ only by that pick.
    A render on disk is reused only when it was made from the same slots (a new top changes every fixed slot)."""
    done_all: dict = {}
    for g in _games(game):
        sel = select(run, g)
        fixed = fixed_slots(g, sel)
        cj = ctx_dir(run, g) / "context.json"
        prev = (json.loads(cj.read_text("utf-8")).get("renders") or {}) if cj.is_file() else {}
        done: dict = {"fixed": _jsonable(fixed), "renders": {}}
        for sid in JOBS[g]:
            for p in sel[sid]["picks"]:
                name = _pick_name(g, sid, p)
                out = ctx_dir(run, g) / sid / f"{name}.wav"
                slots, config, bed = pick_slots(g, sid, p, fixed)
                sig = _slots_sig(slots, config, bed)
                same = ((prev.get(sid) or {}).get(name) or {}).get("slots_sig") == sig
                if same and out.is_file() and out.with_suffix(".json").is_file() and not force:
                    doc = json.loads(out.with_suffix(".json").read_text("utf-8"))
                else:
                    doc = render_pick(g, sid, slots, config, bed, out)
                m = doc["metrics"]
                done["renders"].setdefault(sid, {})[name] = {"file": str(out), "role": p["role"],
                                                             "scenario": SCENARIO[g][sid], "config": config,
                                                             "slots_sig": sig, "metrics": m}
                b = m.get("burst") or {}
                _say(f"context {g}/{sid} {name}: {SCENARIO[g][sid]}, giọng 1–4 kHz min "
                     f"{(m.get('voice') or {}).get('min_db')} dB, đỉnh {(m.get('mix') or {}).get('true_peak_dbtp')} dBTP"
                     + (f", hổng {b.get('gap_time_pct')} %, trũng {b.get('dip_median_db')} dB" if b else ""))
        ctx_dir(run, g).mkdir(parents=True, exist_ok=True)
        (ctx_dir(run, g) / "context.json").write_text(json.dumps(done, ensure_ascii=False, indent=1, default=float), "utf-8")
        done_all[g] = done
    return done_all


# ---------------------------------------------------------------- step 10: board sessions

# game -> sessions (name, title, ids in listening order). Plan §7 (AUDIO_PIPELINE.md:557): at most 10 ids and 20 minutes
# a session. About 40 s a card (the in-scene render, alone, the stars and tags; batch 1: 26 cards and 3 anchor pairs in
# 20-25 minutes), so the 7 ids of Rồng Giữ Ải and Tuyến Cuối (26 cards each) are two sessions (review of 1c); Lời Gọi
# (5 ids, 20 cards, 4 pairs) stays one. Tuyến Cuối starts with the gun: every other item plays over the burst.
SESSIONS = {DH: (("1c-dh-1", "Lô 1c · Rồng Giữ Ải 1/2 · khạc lửa, cầu lửa trúng (Q6)",
                  ("fire.cast", "fire.impact.a", "fire.impact.b", "fire.impact.c")),
                 ("1c-dh-2", "Lô 1c · Rồng Giữ Ải 2/2 · trúng nhiều quái, bom, tiếng tru (Q6)",
                  ("impact.multi", "trap.pine-bomb.trigger", "enemy.quadruped.howl"))),
            TD: (("1c-td", "Lô 1c · Lời Gọi · tên, Phát Chữ, mực, pháo, lời gọi (Q6)",
                  ("arrow-fire", "wordshot-fire", "ink-puff", "blast", "call-chop")),),
            TS: (("1c-ts-1", "Lô 1c · Tuyến Cuối 1/2 · súng, ba bậc trúng (Q6)",
                  ("gun.xung", "hit.t1", "hit.t2", "hit.t4")),
                 ("1c-ts-2", "Lô 1c · Tuyến Cuối 2/2 · hạ quái, báo nguy (Q6)",
                  ("kill.swarm", "kill.elite", "hurt.breach")))}
SEC_PER_CARD = 40.0
DESC = {
    "fire.cast": "Hỏa Long khạc cầu lửa khi gõ xong từ (600–900 ms). Nghe đủ bốn phần: khè họng tụ lực, lửa bắt và "
                 "gầm có lực, cầu lửa lao ra xa có thân, đuôi vang thung lũng thấp. 'Trong trận thô': giọng đọc phải rõ "
                 "ngay sau tiếng khạc",
    "fire.impact.a": "Cầu lửa trúng, âm gốc của họ (480–720 ms): lửa bùng có thân, than lách tách, mảnh văng, vang rừng "
                     "ngắn. Không được nghe như 'một cục rơi xuống'. 'Lặp' phát mỗi 1,5 s như sau mỗi từ",
    "fire.impact.b": "Biến thể tối hơn của cầu lửa trúng (512–768 ms): lửa bùng trầm, than nổ khô, dăm gỗ văng. Cùng họ "
                     "với .a nhưng phân biệt được. Bản có nhãn 'bị luật chặn' là chủ ý; chấm như mọi bản",
    "fire.impact.c": "Đòn to: bậc T3 trở lên, Hoàn hảo, Chớp (800–1200 ms). Lửa bùng lớn có trọng lượng, cháy tiếp, than "
                     "và mảnh văng xa, vang thung lũng dài. Dài và nặng hơn .a rõ, không có tiếng nổ thứ hai",
    "impact.multi": "Một từ trúng từ 3 quái trở lên (560–840 ms), phát chồng lên tiếng trúng thường: lửa bùng nặng nhiều "
                    "chỗ, than tản rộng, vang rừng. Mọi bản đều có nhãn 'bị luật chặn'; chấm như mọi bản. 'Trong trận "
                    "thô': từ thứ 2 và thứ 5",
    "trap.pine-bomb.trigger": "Bom Hạt Thông nổ (880–1320 ms): nổ trầm có thân, hạt và dăm văng, vang rừng thông. Lớp "
                              "trầm chỉ được nằm dưới, không thành một cú 'thụp'. Thử thêm 'Loa nhỏ'",
    "enemy.quadruped.howl": "Sói Mục tru gọi bầy: hít vào, tiếng tru dâng lên rồi hạ, vang rừng mục xa; phát cách nhau "
                            "1,5 s. Mọi bản có nhãn 'bị luật chặn' (luật đầu tiếng sinh vật); chấm như mọi bản. Cuối "
                            "tiếng tru có tiếng rít cao không?",
    "arrow-fire": "Tháp Cung bắn, tới 4 lần mỗi giây (160–240 ms): cung tre kẽo kẹt, dây bật, mũi tên vút đi xa, vang "
                  "làng ngắn. Nhẹ, nằm dưới mọi thứ. Trong trận có gắt, có che giọng đọc không?",
    "wordshot-fire": "Phát Chữ bay ra sau mỗi từ (280–420 ms): vung tay tre, chữ giấy phóng vút đi, giấy phần phật bay "
                     "xa, vang làng ngắn. Mọi bản có nhãn 'bị luật chặn' (tiếng vút lên chậm). 'Lặp' phát mỗi 1,5 s "
                     "như trong game: đuôi có đủ thấp để nghe 20 từ không mệt?",
    "ink-puff": "Mực Câm tan, tới 8 lần mỗi giây (160–240 ms): túi giấy thấm mực rách, mực bắn tóe nhỏ, giấy lả tả, vang "
                "ngắn. Mềm, không máu. Dày như trong trận có thành tiếng rè không?",
    "blast": "Tháp Pháo nổ (640–960 ms): trống lớn nện có thân, giấy và bụi bung tung, mảnh giấy rơi lả tả, vang làng. "
             "Không nổ lách tách, không chất taiko. Thử thêm 'Loa nhỏ'",
    "call-chop": "Lời gọi Chặt sáng lên: gõ gỗ trầm, chắc vào thân tre (200–300 ms). Nghe ra mõ chùa thì gắn 'sai chất "
                 "liệu'. 'Trong trận thô': cảnh đêm, gọi Chặt hai lần giữa lúc gõ",
    "gun.xung": "Súng Xung, pháo tự động bắn 10 viên mỗi giây. Mỗi bản là một bộ phát (bộ nặng và bộ nhẹ xen nhau), có "
                "nền cơ khí và đuôi khi ngừng; có bản là hướng của lô 1, có bản là Stable Audio 3 nguyên khối của lô 1c. "
                "'Liên thanh 3 s': một loạt liền, có lực, hay rời từng phát (nhãn 'ngắt quãng')?",
    "hit.t1": "Đạn Xung trúng vỏ thép, tới 10 lần mỗi giây (112–168 ms): keng giòn, thân thép gọn, đuôi hành lang thép "
              "ngắn. Sáng, gọn, không che tiếng súng và tiếng đọc từ",
    "hit.t2": "Chí mạng (208–312 ms): nặng hơn hit.t1, keng có thân, lớp trầm chỉ ở dưới, đuôi hành lang ngắn. Nghe kỹ có "
              "'gõ đúp' không",
    "hit.t4": "Đòn lớn (720–1080 ms): nện nặng vào dầm thép, nứt giòn, thân thép dày, dầm ngân dài lăn dọc hành lang. To "
              "và dài hơn hit.t2 rõ",
    "kill.swarm": "Bầy quái kim loại vỡ, hàng trăm lần mỗi trận (200–300 ms), hướng 'vỡ có vang': bản Stable Audio 3 mới "
                  "và công thức của lô 1. Có chói, có mỏng, lặp có mệt không?",
    "kill.elite": "Lính tinh nhuệ nổ (400–600 ms): thép xé toạc, nổ trầm có thân, phóng điện lách tách, mảnh rơi, vang "
                  "hành lang thép. Đuôi có bị cụt đột ngột không?",
    "hurt.breach": "Báo nguy, tuyến bị phá (640–960 ms): nổ trầm có thân, thép rên, còi hai nốt ngắn, vang dội dọc hành "
                   "lang thép. Khác hẳn tiếng trúng, đủ rõ để báo nguy giữa trận",
}
CONTEXTS = {
    "fire.cast": ["scene", "loop", "alone", "small"], "fire.impact.a": ["scene", "loop", "alone", "small"],
    "fire.impact.b": ["scene", "loop", "alone", "small"], "fire.impact.c": ["scene", "loop", "alone", "small"],
    "impact.multi": ["scene", "alone", "loop", "small"], "trap.pine-bomb.trigger": ["scene", "alone", "small"],
    "enemy.quadruped.howl": ["scene", "alone", "loop"],
    "arrow-fire": ["scene", "loop", "alone", "small"], "wordshot-fire": ["scene", "loop", "alone", "small"],
    "ink-puff": ["scene", "loop", "alone", "small"], "blast": ["scene", "alone", "small", "loop"],
    "call-chop": ["alone", "scene", "loop"],
    "gun.xung": ["burst", "alone", "loop", "small"], "hit.t1": ["burst", "loop", "alone", "small"],
    "hit.t2": ["burst", "alone", "loop", "small"], "hit.t4": ["burst", "alone", "small"],
    "kill.swarm": ["burst", "loop", "alone", "small"], "kill.elite": ["burst", "alone", "small"],
    "hurt.breach": ["scene", "alone", "small"],
}
# "Lặp": the fire family follows a word (one every 1.5 s at 40 WPM), so it repeats at that pace (Q6 rule 4: a low tail
# that 20 words in a row do not tire); the Tuyến Cuối rates are batch1_ts.LOOP (the scene's real pace)
LOOP = {"fire.cast": {"interval_ms": 1500, "count": 8}, "fire.impact.a": {"interval_ms": 1500, "count": 8},
        "fire.impact.b": {"interval_ms": 1500, "count": 8}, "fire.impact.c": {"interval_ms": 1500, "count": 8},
        "impact.multi": {"interval_ms": 1500, "count": 8}, "enemy.quadruped.howl": {"interval_ms": 1500, "count": 4},
        "wordshot-fire": {"interval_ms": 1500, "count": 8},
        "gun.xung": {"interval_ms": 100, "count": 30, "cents": 40, "db": 1}, "hit.t1": {"interval_ms": 100, "count": 20},
        "kill.swarm": {"interval_ms": 150, "count": 20}, "hit.t2": {"interval_ms": 400, "count": 8}}
RATE_FIX = {"call-chop": 3.0, "blast": 1 / 1.2}     # batch1_td._loop: alerts 3 a second; two cannon towers


MAX_ITEMS = 10               # plan §7: at most 10 ids and 20 minutes a session, anchors included
MAX_MINUTES = 20
ANCHORS = 4                  # §4.6 step 6 (batch 1: 4); fewer when the ids leave less room
ANCHORS_SPLIT = 2            # a game split in two sessions: 2 pairs each (4 in all, batch 1c first pass: 3)


class SessionExists(RuntimeError):
    pass


def anchors_for(n_ids: int, split: bool = False) -> int:
    return max(0, min(ANCHORS_SPLIT if split else ANCHORS, MAX_ITEMS - n_ids))


def session_path(game: str, name: str | None = None) -> Path:
    return env.REVIEW / game / "sessions" / f"{name or SESSIONS[game][0][0]}.json"


def est_minutes(n_cards: int, anchors: int) -> float:
    """Listening time of a session: SEC_PER_CARD a card, an anchor pair 2 cards."""
    return round((n_cards + 2 * anchors) * SEC_PER_CARD / 60.0, 1)


def _loop(game: str, sid: str, picks: list[dict]) -> dict | None:
    import yaml
    if sid in LOOP:
        return dict(LOOP[sid])
    card = yaml.safe_load(card_path(game, sid).read_text("utf-8")) or {}
    rate = RATE_FIX.get(sid) or (card.get("critic") or {}).get("rate_hz")
    gap = (card.get("playback") or {}).get("min_gap_ms") or 0
    longest = max(((d.get("metrics") or {}).get("duration_ms") or 0) for p in picks for d in p.get("docs") or [])
    if game == TS:
        return {"interval_ms": int(max(1000.0, longest + 300)), "count": 6}
    if not rate and not gap:
        return None
    iv = int(max(1000.0 / rate if rate else 0, gap, longest + 50))
    return {"interval_ms": iv, **({"count": 8} if iv >= 500 else {})}


def _cand(p: dict, ctx: Path | None, key: str) -> dict:
    from board import session as S
    docs = p.get("docs") or []
    files = [Path(f) for f in p.get("files") or [d["file"]["path"] for d in docs]]

    def card(d: dict) -> str | None:
        c = d.get("card_blind") or d.get("card")
        return S.display_path(Path(d["_out"]) / c) if c and (Path(d["_out"]) / c).is_file() else None

    if len(files) == 1:
        c: dict = {"file": S.display_path(files[0]), "role": p["role"]}
        if docs:
            c["critic"] = S.display_path(Path(docs[0]["_out"]) / f"{docs[0]['file']['stem']}.json")
            if card(docs[0]):
                c["card"] = card(docs[0])
    else:
        c = {"files": [S.display_path(f) for f in files], "role": p["role"]}
        if docs and len(docs) == len(files):
            c["critics"] = [S.display_path(Path(d["_out"]) / f"{d['file']['stem']}.json") for d in docs]
            c["cards"] = [card(d) for d in docs]
    if p.get("note"):
        c["note"] = p["note"]
    if ctx is not None and ctx.is_file():
        c["ctx"] = {key: S.display_path(ctx)}
    return c


def build_session(run: str, game: str, sel: dict, part: tuple[str, str, tuple[str, ...]] | None = None) -> dict:
    name, title, ids = part or SESSIONS[game][0]
    split = len(SESSIONS[game]) > 1
    items = []
    for sid in ids:
        picks = sel[sid]["picks"]
        if not picks:
            _say(f"phiên {name}: {sid} không có bản nào để nghe")
            continue
        key = ctx_key(game, sid)
        cands = [_cand(p, ctx_dir(run, game) / sid / f"{_pick_name(game, sid, p)}.wav", key) for p in picks]
        sp = next((d.get("spec") for p in picks for d in p.get("docs") or [] if d.get("spec")), None) or {}
        item = {"id": sid, "family": sp.get("family") or "", "group": sp.get("group") or "", "desc": DESC[sid],
                "probe": any(p["role"] == "probe" for p in picks), "contexts": CONTEXTS[sid], "candidates": cands}
        lp = _loop(game, sid, picks)
        if lp:
            item["loop"] = lp
        items.append(item)
    return {"schema": "audiolab.board.session/1", "session": name, "game": game, "batch": "1c", "title": title,
            "seed": int(hashlib.sha256(f"{game}:{name}".encode()).hexdigest()[:8], 16), "max_minutes": MAX_MINUTES,
            "anchors": anchors_for(len(items), split), "reveal": "end", "items": items}


def superseded(games: tuple[str, ...]) -> list[Path]:
    """Session files of batch 1c that SESSIONS no longer writes (1c-dh and 1c-ts before the split in two, review of
    1c): the board would still serve them. One the owner has opened is never moved (SessionExists)."""
    out = []
    for g in games:
        names = {part[0] for part in SESSIONS[g]}
        for path in sorted((env.REVIEW / g / "sessions").glob("1c-*.json")):
            try:
                raw = json.loads(path.read_text("utf-8"))
            except (OSError, ValueError):
                continue
            name = raw.get("session") or path.stem
            if str(raw.get("batch")) != "1c" or name in names:
                continue
            if (env.REVIEW / g / "state" / f"{name}.json").exists():
                raise SessionExists(f"{path}: phiên cũ anh đã mở; không cất đi")
            out.append(path)
    return out


def step_session(run: str, game: str | None = None, force: bool = False) -> list[Path]:
    """The sessions of each game (~/AudioLab/review/<game>/sessions/1c-*.json). An existing file needs --force, and a
    session the owner has opened (its state file exists) is never overwritten, --force or not."""
    from board import session as S
    games = _games(game)
    targets = [(g, part) for g in games for part in SESSIONS[g]]
    opened = [str(env.REVIEW / g / "state" / f"{part[0]}.json") for g, part in targets
              if (env.REVIEW / g / "state" / f"{part[0]}.json").exists()]
    if opened:
        raise SessionExists(f"{', '.join(opened)}: anh đã mở phiên này; không ghi đè (điểm và chỗ đang nghe nằm ở đó)")
    there = [session_path(g, part[0]) for g, part in targets if session_path(g, part[0]).exists()]
    if there and not force:
        raise SessionExists(f"{', '.join(map(str, there))} đã có; thêm --force để ghi đè (điểm đã chấm vẫn giữ trong "
                            "ratings.jsonl)")
    old = superseded(games)
    if old and not force:
        raise SessionExists(f"{', '.join(map(str, old))}: phiên 1c cũ, không còn trong SESSIONS; thêm --force để cất đi")
    for path in old:                    # never opened (checked in superseded): moved out of the board's sight
        dest = path.parent / "_superseded" / path.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        path.replace(dest)
        _say(f"phiên cũ {path.name} cất vào {dest.parent} (Bảng Nghe chỉ đọc sessions/*.json)")
    paths = []
    for g in games:
        sel = select(run, g)
        for part in SESSIONS[g]:
            doc = build_session(run, g, sel, part)
            path = session_path(g, part[0])
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", "utf-8")
            s = S.load(path)                # validate now: paths, ctx files, contexts, notes
            missing = [i.id for i in s.items if ctx_key(g, i.id) not in i.rendered]
            paths.append(path)
            n_cards = sum(len(i["candidates"]) for i in doc["items"])
            mins = est_minutes(n_cards, doc["anchors"])
            _say(f"phiên {path}: {len(doc['items'])} id, {n_cards} bản (+{doc['anchors']} cặp mốc khi mở), khoảng "
                 f"{mins:g} phút" + (f" (QUÁ {MAX_MINUTES} phút)" if mins > MAX_MINUTES else "")
                 + (f"; thiếu bản dựng trong bối cảnh: {', '.join(missing)}" if missing else ""))
    return paths


# ---------------------------------------------------------------- CLI

STEPS = {"generate": step_generate, "process": step_process, "sources": step_sources, "recipes": step_recipes,
         "critic": step_critic, "link": step_link, "report": step_report, "context": step_context,
         "session": step_session}
ALL = ("generate", "process", "recipes", "critic", "link", "report", "context", "session")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="batch1c", description="Lô 1c: sinh lại âm hành động theo Q6 (Q6_REWRITE §7).")
    ap.add_argument("step", choices=[*STEPS, "all"])
    ap.add_argument("--game", choices=GAMES)
    ap.add_argument("--run", default=RUN)
    ap.add_argument("--force", action="store_true", help="làm lại bước đã có; ghi đè file phiên")
    a = ap.parse_args(argv)
    env.apply()
    for name in (ALL if a.step == "all" else (a.step,)):
        try:
            rc = STEPS[name](a.run, a.game, a.force)
        except SessionExists as exc:
            print(f"batch1c: {exc}", file=sys.stderr)
            return 1
        if isinstance(rc, int) and rc:
            return rc
    return 0


if __name__ == "__main__":
    sys.exit(main())
