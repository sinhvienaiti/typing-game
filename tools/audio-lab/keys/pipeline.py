"""Keyboard sound profiles for the typing games (keypress-sound lane, owner request 29/10/2026).

Five profiles (keys/specs/<profile>.yaml), each 10 single keystrokes and 3 spacebar strokes, made in
Audio Lab from Stable Audio 3 Small-SFX (no downloaded packs, no synth stand-ins):

  run.sh keys generate [--profiles creamy,thock] [--seeds 101-104] [--prompts A,B,C,D] [--run r1]
  run.sh keys slice    [--run r1]          # every take -> single strokes (onset, window, tail, mono, 48 kHz)
  run.sh keys critic   [--run r1]          # L1, L1b, L2, L3, L4 on every stroke (critic run --spec)
  run.sh keys pick     [--run r1]          # gate, rank, choose a consistent set per profile (+ alternative sets)
  run.sh keys master   [--run r1]          # one loudness target for all, masters + OGG runtime, re-check
  run.sh keys render   [--run r1]          # typing phrases at 60 and 100 WPM, 20x repeat
  run.sh keys session  [--run r1]          # Listening Board session keys-1
  run.sh keys stage    [--run r1]          # ~/AudioLab/review/staging/keys/<profile>/ + keys-manifest.json
  run.sh keys all      [--run r1]
  run.sh keys firefly survey [--folders 0,3] [--limit N]   # khảo sát chỉ đọc nguồn Firefly
  run.sh keys firefly build [--out DIR]                  # bộ 10+3 và preview 1 giây (phiếu 189)

Data: ~/AudioLab/work/_keys/<profile>/<run>/ (raw/, strokes/, critic/, masters/, runtime/), never in Git.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

import yaml

from common import env

LAB = env.LAB
SPECS = LAB / "keys" / "specs"
WORK = env.WORK / "_keys"
REVIEW = env.REVIEW / "keys"
STAGING = env.STAGING / "keys"
PROFILES = ("creamy", "thock", "clicky", "dome", "spring")
PARTS = ("key", "space")
PASSAGE_KEYS = ("A", "B", "E")     # 10 s typing passages, sliced into strokes
SINGLE_KEYS = ("C", "D", "F")      # 1 s single-stroke takes
SR = 48000


# ---------------------------------------------------------------- cards

def load_profile(pid: str) -> dict[str, dict]:
    """{'key': card, 'space': card} of one profile."""
    path = SPECS / f"{pid}.yaml"
    cards = yaml.safe_load(path.read_text("utf-8"))
    out = {}
    for c in cards:
        c["_path"] = str(path)
        out[c["profile"]["part"]] = c
    return out


def profiles_arg(text: str | None) -> list[str]:
    if not text or text == "all":
        return list(PROFILES)
    out = [p.strip() for p in text.split(",") if p.strip()]
    bad = [p for p in out if p not in PROFILES]
    if bad:
        raise SystemExit(f"keys: hồ sơ lạ {bad}; có {PROFILES}")
    return out


def run_dir(pid: str, run: str) -> Path:
    p = WORK / pid / run
    p.mkdir(parents=True, exist_ok=True)
    return p


def check_prompt(text: str) -> None:
    """DECISIONS Q2 (Lời Gọi: no hollow 'tok') and Q6 (no puffs, toys, retro): these files ship in all
    three games, so a keyboard prompt follows the union of their bans."""
    from gen import sa3
    for pat in (*sa3.Q2_TERMS, *sa3.Q6_TERMS):
        if re.search(pat, text, re.I):
            raise SystemExit(f"keys: prompt có cụm bị cấm /{pat}/ (DECISIONS Q2, Q6): {text[:80]}")


def wait_heavy_free(what: str) -> None:
    """One heavy model at a time on this machine (other lanes run Stable Audio 3 and the critic too)."""
    from common.batch1_dh import wait_heavy_free as _wait
    _wait(what)


# ---------------------------------------------------------------- generate (Stable Audio 3)

def cmd_generate(a) -> int:
    from gen import sa3

    seeds = sa3.parse_seeds(a.seeds)
    want = [k.strip() for k in (a.prompts or "A,B,C,D").split(",") if k.strip()]
    for pid in profiles_arg(a.profiles):
        for part, card in load_profile(pid).items():
            prompts = sa3.prompts_from_card(card)
            keys = [k for k in want if k in prompts]
            if not keys:
                continue
            items, meta_variants = [], {}
            for k in keys:
                check_prompt(prompts[k])
                secs = 10.0 if k in PASSAGE_KEYS else float(a.single_seconds)
                job = sa3.build_job(card, variants=[k], seeds=seeds, seconds=secs, tag_seconds=False,
                                    prompts=prompts)
                items += job["items"]
                meta_variants[k] = prompts[k]
            job["items"] = items
            job["_meta"]["variants"] = meta_variants
            job["_meta"]["seconds"] = sorted({it["seconds"] for it in items})
            rd = run_dir(pid, a.run)
            print(f"[{pid}/{part}] {len(items)} ứng viên -> {rd}/raw", flush=True)
            wait_heavy_free(f"sa3 keys {pid}/{part}")
            res = sa3.run_job(job, rd)
            print(json.dumps({k: v for k, v in res.items() if k != "records"} | {"records": len(res["records"])},
                             ensure_ascii=False), flush=True)
    return 0


# ---------------------------------------------------------------- slice (takes -> strokes)

PROVISIONAL_LUFS = -24.0     # candidates only: one level so the critic and the board compare like with like


def _level(y, target: float = PROVISIONAL_LUFS, ceiling: float = -1.5):
    """Pure gain to `target` LUFS-M max, never over `ceiling` dBTP (no limiter on candidates)."""
    from build import dsp, measure
    lm = measure.lufs_m_max(y, SR)
    tp = measure.true_peak_db(y, SR)
    g = min(target - lm, ceiling - tp)
    return y * dsp.db_to_gain(g), round(g, 2)


def cmd_slice(a) -> int:
    import numpy as np
    import soundfile as sf
    from build import ledger, measure, render, sources
    from gen import sa3
    from gen.process import TOOL, _model_id
    from keys import family, strokes

    for pid in profiles_arg(a.profiles):
        rd = run_dir(pid, a.run)
        out = rd / "strokes"
        if out.exists() and a.force:
            shutil.rmtree(out)
        out.mkdir(parents=True, exist_ok=True)
        date, tools = ledger.today(), render.tool_versions()
        data, index, skipped, rows = {}, [], [], None
        recs = sorted(p for p in (rd / "raw").glob("*.json") if not p.name.startswith("_"))
        for rp in recs:
            rec = sa3.read_record(rp)
            part = rec["id"].split(".")[0]
            f32 = Path(rec["files"]["f32"]["path"])
            x, sr_in = sf.read(str(f32), always_2d=True, dtype="float64")
            m, prep = strokes.prepare(x, sr_in)
            found, skip = strokes.find_strokes(m, rec["candidate"], part)
            skipped += skip
            for st in found:
                y, info = strokes.render(m, st, part)
                if y is None:
                    skipped.append({"take": rec["candidate"], "onset_ms": round(st.onset / SR * 1000, 1), "why": info["why"]})
                    continue
                # source window in the take (seconds), for the clip scan of the float copy
                w0 = max(0.0, st.onset / SR - 0.001)
                w1 = min(x.shape[0] / sr_in, w0 + info["duration_ms"] / 1000 + info.get("tightened_ms", 0) / 1000)
                y, gain = _level(y)
                stem = f"{rec['candidate']}-k{st.index:02d}"
                wav = out / f"{stem}.wav"
                sf.write(str(wav), y.astype(np.float32), SR, subtype="PCM_24")
                feat = family.features(y, SR, None if st.gap_ms is None else st.gap_ms - info.get("tightened_ms", 0))
                sha = ledger.sha256_file(wav)
                mid = _model_id(rec)
                raw_qa = sources.raw_qa([sources.clip_scan_file(f32, [w0, w1])])
                layer = {"id": "sa3", "role": "whole", "kind": "gen", "tool": TOOL, "model": mid,
                         "licence": sa3.STABILITY, "licenceAccepted": "licences/stability-registration.txt",
                         "source": f32.name, "sourceSha256": rec["files"]["f32"]["sha256"], "prompt": rec.get("prompt"),
                         "seed": int(rec["seed"]), "cfg": float(rec.get("cfg", 1.0)), "aiSteps": ["generate"],
                         "record": rp.name, "window": [round(w0, 4), round(w1, 4)], "rawQa": raw_qa}
                chain = (f"f32 raw, {prep['mono']} mono, hpf30 zero-phase, soxr VHQ -> 48 kHz, stroke window from 1 ms "
                         f"before the onset ({st.kind}"
                         + (f", gap {st.gap_ms:.0f} ms" if st.gap_ms else "")
                         + (f", gap shortened {info['tightened_ms']:g} ms in silence" if info.get("tightened_ms") else "")
                         + f"), 1 ms fade-in, exp cap tail to -60 dB, gain {gain:+.2f} dB (provisional {PROVISIONAL_LUFS:g} "
                         "LUFS-M max), PCM 24-bit")
                data[wav.name] = {"id": rec["id"], "game": "keys", "variant": len(index) + 1, "sha256": sha, "date": date,
                                  "run": a.run, "master": wav.name, "masterSha256": sha,
                                  "durationMs": round(len(y) / SR * 1000, 2), "sampleRate": SR, "channels": 1,
                                  "layers": [layer], "chain": chain, "tools": tools, "models": [mid], "aiSteps": [],
                                  "aiInputAllowed": True, "rawQa": f"{stem}.proc.json", "review": None}
                proc = {"stem": stem, "id": rec["id"], "part": part, "profile": pid, "take": rec["candidate"],
                        "prompt_key": rec.get("variant"), "seed": rec["seed"], "seconds": rec["seconds"],
                        "source_kind": "passage" if rec.get("variant") in PASSAGE_KEYS else "single",
                        "stroke": strokes.to_dict(st), "render": info, "prep": prep, "gain_db": gain,
                        "raw_qa": raw_qa, "summary": measure.summary(y, SR), "features": feat, "path": str(wav),
                        "sha256": sha, "chain": chain}
                (out / f"{stem}.proc.json").write_text(json.dumps(proc, indent=1, ensure_ascii=False, default=float), "utf-8")
                index.append({k: proc[k] for k in ("stem", "id", "part", "take", "prompt_key", "seed", "source_kind")}
                             | {"kind": st.kind, "gap_ms": proc["stroke"]["gap_ms"], "dur_ms": info["duration_ms"],
                                "tightened_ms": info.get("tightened_ms", 0), "clip": raw_qa.get("verdict")})
            if rows is None:
                rows = (rec.get("licence") or {}).get("rows")
        ledger.write_sources(out / "SOURCES.json", data)
        if rows:
            ledger.append_rows(out / "licences.rows.jsonl", rows)
        (out / "_strokes.json").write_text(json.dumps({"strokes": index, "skipped": skipped}, indent=1, ensure_ascii=False), "utf-8")
        by = {}
        for s in index:
            k = (s["part"], s["source_kind"])
            by[k] = by.get(k, 0) + 1
        print(f"[{pid}] {len(index)} cú gõ ({', '.join(f'{p}/{k}: {n}' for (p, k), n in sorted(by.items()))}), "
              f"bỏ {len(skipped)}", flush=True)
    return 0


# ---------------------------------------------------------------- critic (L1, L1b, L2, L3, L4, L6)

def cmd_critic(a) -> int:
    import subprocess

    for pid in profiles_arg(a.profiles):
        rd = run_dir(pid, a.run)
        out = rd / "critic"
        if out.is_dir():
            prev = out.with_name("critic.prev")
            if prev.exists():
                shutil.rmtree(prev)
            out.rename(prev)
        argv = ["run", str(rd / "strokes"), "--spec", str(SPECS / f"{pid}.yaml"), "--stage", "final",
                "--layers", a.layers, "--out", str(out), "--seed", "2910", "--blind-cards", "--quiet",
                "--sources", str(rd / "strokes" / "SOURCES.json")]
        wait_heavy_free(f"critic keys {pid}")
        print(f"[{pid}] critic -> {out}", flush=True)
        rc = subprocess.run([sys.executable, "-I", str(LAB / "common" / "launch.py"), "critic", *argv]).returncode
        if rc:
            print(f"[{pid}] critic dừng với mã {rc}", flush=True)
            return rc
    return 0


# ---------------------------------------------------------------- pick (gate, rank, families, listening list)

N_PART = {"key": 10, "space": 3}
TP_CEILING = -1.0
PROBE_PROFILES_FRAC = 0.3          # §4.6 step 2: a probe for ~30 % of the ids
MAX_T_MAIN_MS = 15.0               # the hit lands within 15 ms of the file start (finger touch, then bottom-out)
MASTER_TARGET = -27.0              # LUFS-M max for every file of every profile (see cmd_master)
MAX_LIMIT_DB = 0.0                 # pick: every stroke reaches the target by gain alone (transients untouched); the master limiter is only a safety
MAX_HIT_RISE_MS = 6.0              # the bottom-out's > 2 kHz rise; slower is model smear (fit prefers <= 2.5 ms)


def _runs(a) -> list[str]:
    return [r.strip() for r in (a.runs or a.run).split(",") if r.strip()]


def pool_for(pid: str, runs: list[str]) -> list[dict]:
    import soundfile as sf
    from keys import family, pick
    cards = load_profile(pid)
    pool = []
    for r in runs:
        rd = WORK / pid / r
        if not (rd / "strokes" / "_strokes.json").is_file():
            continue
        for row in pick.load_pool(rd, cards):
            y, sr = sf.read(row["path"])
            rel = row["proc"]["stroke"].get("gap_ms")
            row["feat"] = family.features(y, sr, None if rel is None else rel - row["proc"]["render"].get("tightened_ms", 0))
            row["fit"], row["fit_parts"] = family.fit_score(row["feat"], cards[row["part"]].get("fit") or {})
            if row["feat"]["t_main_ms"] > MAX_T_MAIN_MS:
                row["gate"], row["why"] = "BLOCK", row["why"] + [f"tiếng chính đến muộn ({row['feat']['t_main_ms']:.0f} ms)"]
            if row["feat"]["hit_rise_ms"] > MAX_HIT_RISE_MS:
                row["gate"], row["why"] = "BLOCK", row["why"] + [f"đáy phím nhòe (lên {row['feat']['hit_rise_ms']:.1f} ms trên 2 kHz)"]
            from build import measure
            row["reach"] = round(measure.lufs_m_max(y, sr) + (TP_CEILING - 0.4 - measure.true_peak_db(y, sr)), 2)
            if row["reach"] < MASTER_TARGET - MAX_LIMIT_DB:
                row["gate"], row["why"] = "BLOCK", row["why"] + [
                    f"đỉnh quá nhọn: tới {MASTER_TARGET:g} LUFS-M cần nén hơn {MAX_LIMIT_DB:g} dB (chỉ tới {row['reach']:.1f})"]
            row["run"] = r
            pool.append(row)
    # z and Q again over the pooled runs
    for part in PARTS:
        ok = [r for r in pool if r["part"] == part and r["gate"] == "PASS"]
        zp, za, zc = pick._z([r.get("pq") for r in ok]), pick._z([r.get("ast") for r in ok]), pick._z([r.get("critic_score") for r in ok])
        for r, x, y_, c in zip(ok, zp, za, zc):
            r["z"] = {"pq": round(x, 3), "ast": round(y_, 3), "critic": round(c, 3), "fit": round(2 * r["fit"] - 1, 3)}
            r["Q"] = round(pick.W["fit"] * r["z"]["fit"] + pick.W["pq"] * x + pick.W["ast"] * y_ + pick.W["critic"] * c
                           - r.get("l1b_penalty", 0), 4)
    return pool


def cmd_pick(a) -> int:
    from keys import family, pick
    ref = family.kenney_reference(WORK / "_kenney-family.json", env.LIBRARIES)
    runs = _runs(a)
    probe_ids = set(sorted(PROFILES, key=lambda p: hashlib.sha256(f"keys-probe:{p}".encode()).hexdigest())
                    [:max(1, round(PROBE_PROFILES_FRAC * len(PROFILES)))])
    summary = {}
    for pid in profiles_arg(a.profiles):
        pool = pool_for(pid, runs)
        by = {r["stem"]: r for r in pool}
        out = {"profile": pid, "runs": runs, "kenney": {k: v for k, v in ref.items() if k != "families"},
               "weights": pick.W, "parts": {}}
        for part in PARTS:
            sets = pick.candidate_sets(pool, part, N_PART[part], ref)
            ll = pick.listening_list(sets, pool, probe=(pid in probe_ids and part == "key"), seed=2910)
            out["parts"][part] = {"n_pool": sum(1 for r in pool if r["part"] == part),
                                  "n_pass": sum(1 for r in pool if r["part"] == part and r["gate"] == "PASS"),
                                  "n_sets": len(sets), "listen": ll}
        # a spacebar set for each key set: the closest good space set to the key set's medoid
        sp = pick.candidate_sets(pool, "space", N_PART["space"], ref)
        for ks in out["parts"]["key"]["listen"]:
            if not sp:
                break
            km = by[ks["medoid"]]["feat"]
            best = max(sp[:12], key=lambda s: s["score"] - 0.08 * family.mel_dist(by[s["medoid"]]["feat"], km))
            ks["space"] = {"members": best["members"], "medoid": best["medoid"], "score": best["score"], "report": best["report"]}
        out["gate"] = {r["stem"]: {"gate": r["gate"], "why": r["why"], "Q": r.get("Q"), "fit": r["fit"], "z": r.get("z"),
                                   "pq": r.get("pq"), "ast": r.get("ast"), "ast_top5": r.get("ast_top5"),
                                   "clap_top3": r.get("clap_top3"), "critic_score": r.get("critic_score"),
                                   "flags": r.get("flags"), "l1b": r.get("l1b"), "metrics": r.get("metrics"), "run": r["run"],
                                   "path": r["path"], "critic_json": r.get("critic_json"), "kind": r["kind"],
                                   "take": r["take"], "feat": {k: v for k, v in r["feat"].items() if k not in ("mel_db", "env")},
                                   "fit_parts": r["fit_parts"]} for r in pool}
        dest = WORK / pid / "pick.json"
        dest.write_text(json.dumps(out, indent=1, ensure_ascii=False, default=float), "utf-8")
        line = []
        for part in PARTS:
            p = out["parts"][part]
            top = p["listen"][0] if p["listen"] else None
            line.append(f"{part}: {p['n_pass']}/{p['n_pool']} qua cổng, {p['n_sets']} bộ"
                        + (f", đầu {top['score']:+.2f} (Q {top['report']['mean_Q']:+.2f}, fit {top['report']['mean_fit']:.2f}, "
                           f"mel {top['report']['mel_dist_mean']:.2f})" if top else ", KHÔNG CÓ BỘ"))
        print(f"[{pid}] " + "; ".join(line), flush=True)
        summary[pid] = out["parts"]
    return 0


# ---------------------------------------------------------------- master (one loudness target, WAV + OGG)

OGG_QUALITY = 0.6
LUFS_CAP = -20.0                    # the plan's common level for short sounds (§4.3.3); keystrokes cannot reach it


def _choices(text: str | None) -> dict[str, str]:
    out = {}
    for kv in (text or "").split(","):
        if "=" in kv:
            k, v = kv.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def listened_sets(pid: str) -> list[dict]:
    """The listening list of a profile: [{role, key: [stems], space: [stems]}]."""
    pk = json.loads((WORK / pid / "pick.json").read_text("utf-8"))
    out = []
    for s in pk["parts"]["key"]["listen"]:
        out.append({"role": s["role"], "key": s["members"], "space": (s.get("space") or {}).get("members") or [],
                    "key_report": s["report"], "space_report": (s.get("space") or {}).get("report"),
                    "score": s["score"]})
    return out, pk


def cmd_master(a) -> int:
    import io
    import numpy as np
    import soundfile as sf
    from build import ledger, measure, render as brender
    from keys import family

    choice = _choices(a.choice)
    plan = {}
    for pid in profiles_arg(a.profiles):
        sets, pk = listened_sets(pid)
        if not sets:
            print(f"[{pid}] chưa có bộ nào (chạy pick)", flush=True)
            continue
        plan[pid] = (sets, pk)
    # 1. one target for everything. Keystrokes are all transient (crest 20-28 dB): by gain alone at -1 dBTP the
    #    median stroke reaches -25..-27 LUFS-M max, never the plan's -20 (§4.3.3). So -27, and a stroke that needs
    #    it gets at most 2 dB of true-peak limiting on its first transient (pick gates the ones that need more).
    target = float(a.target) if a.target else MASTER_TARGET
    print(f"đích chung: {target:g} LUFS-M max, đỉnh thật <= {TP_CEILING:g} dBTP, nén tối đa {MAX_LIMIT_DB:g} dB", flush=True)
    reach = [(target, "", "", "")]
    date, tools = ledger.today(), brender.tool_versions()
    report = {"target_lufs_m_max": target, "true_peak_ceiling_dbtp": TP_CEILING, "ogg_quality": OGG_QUALITY,
              "limiter_max_db": MAX_LIMIT_DB, "profiles": {}}
    for pid, (sets, pk) in plan.items():
        chosen_role = choice.get(pid, "top")
        prof = {"chosen": chosen_role, "sets": {}}
        for s in sets:
            sdir = WORK / pid / "sets" / s["role"]
            if sdir.exists():
                shutil.rmtree(sdir)
            files = []
            for part in PARTS:
                stems = sorted(s[part], key=lambda st: -(pk["gate"][st]["Q"] or 0))
                for i, stem in enumerate(stems, 1):
                    g = pk["gate"][stem]
                    y, _ = sf.read(g["path"])
                    # gain to the target; a stroke whose first transient would pass -1 dBTP gets the chain's
                    # true-peak limiter (5 ms look-ahead, 30 ms release), iterated to the target (build.chain)
                    from build import chain as bchain
                    crep: dict = {}
                    y = bchain._normalise_and_limit(y[:, None], SR, {"mode": "lufs-m-max", "target": target},
                                                    {"ceilingDbtp": TP_CEILING, "maxGrDb": 3.0,
                                                     "releaseMs": 30.0}, crep)[:, 0]
                    gain, gr = crep.get("preGainDb", 0.0), crep.get("limiterGrDb", 0.0)
                    name = f"{part}-{i:02d}"
                    wav = sdir / "masters" / f"{name}.wav"
                    wav.parent.mkdir(parents=True, exist_ok=True)
                    sf.write(str(wav), y.astype(np.float32), SR, subtype="PCM_24")
                    y24, _ = sf.read(str(wav))
                    ogg = brender.encode_ogg(y24, SR, OGG_QUALITY)
                    dec, _ = sf.read(io.BytesIO(ogg), always_2d=True, dtype="float64")
                    (sdir / "runtime").mkdir(parents=True, exist_ok=True)
                    (sdir / "runtime" / f"{name}.ogg").write_bytes(ogg)
                    summ = measure.summary(y24, SR)
                    files.append({"name": name, "part": part, "stem": stem, "run": g["run"], "take": g["take"],
                                  "gain_db": round(gain, 2), "limiter_gr_db": gr, "master": f"masters/{name}.wav",
                                  "master_sha256": ledger.sha256_file(wav), "runtime": f"runtime/{name}.ogg",
                                  "runtime_sha256": ledger.sha256_bytes(ogg), "runtime_bytes": len(ogg),
                                  "duration_ms": summ["durationMs"], "lufs_m_max": summ["lufsMMax"],
                                  "true_peak_dbtp": summ["truePeakDbtp"], "head_ms": summ["headMs"],
                                  "ogg_true_peak_dbtp": round(measure.true_peak_db(dec, SR), 2),
                                  "ogg_head_ms": round(measure.head_ms(dec, SR), 2),
                                  "ogg_lufs_m_max": round(measure.lufs_m_max(dec, SR), 2),
                                  "lufs_100ms_max": round(float(np.max(measure.sliding_lufs(y24, SR, 0.1, 0.005))), 2),
                                  "Q": g["Q"], "fit": g["fit"], "pq": g["pq"], "ast": g["ast"],
                                  "critic_score": g["critic_score"], "critic_json": g["critic_json"], "kind": g["kind"]})
            bad = [f["name"] for f in files if f["ogg_true_peak_dbtp"] > TP_CEILING or f["true_peak_dbtp"] > TP_CEILING]
            prof["sets"][s["role"]] = {"dir": str(sdir), "files": files, "over_ceiling": bad,
                                       "key_report": s["key_report"], "space_report": s["space_report"]}
            print(f"[{pid}/{s['role']}] {len(files)} file, LUFS-M {min(f['lufs_m_max'] for f in files):.2f}.."
                  f"{max(f['lufs_m_max'] for f in files):.2f}, TP max {max(f['true_peak_dbtp'] for f in files):.2f} "
                  f"(OGG {max(f['ogg_true_peak_dbtp'] for f in files):.2f}), dài {min(f['duration_ms'] for f in files):.0f}.."
                  f"{max(f['duration_ms'] for f in files):.0f} ms" + (f", VƯỢT TRẦN: {bad}" if bad else ""), flush=True)
        report["profiles"][pid] = prof
    (WORK / "master.json").write_text(json.dumps(report, indent=1, ensure_ascii=False), "utf-8")
    return 0


# ---------------------------------------------------------------- recheck (critic on the masters, no model)

def cmd_recheck(a) -> int:
    import subprocess
    rep = json.loads((WORK / "master.json").read_text("utf-8"))
    bad = 0
    for pid, prof in rep["profiles"].items():
        if a.profiles and pid not in profiles_arg(a.profiles):
            continue
        for role, st in prof["sets"].items():
            sdir = Path(st["dir"])
            out = sdir / "critic"
            if out.exists():
                shutil.rmtree(out)
            # names key-01.., space-01..: one card per part (the key card's id is key.<pid>)
            tmp = sdir / "_named"
            if tmp.exists():
                shutil.rmtree(tmp)
            tmp.mkdir()
            for f in st["files"]:
                (tmp / f"{f['part']}.{pid}-{f['name'].split('-')[1]}.wav").symlink_to(sdir / f["master"])
            argv = ["run", str(tmp), "--spec", str(SPECS / f"{pid}.yaml"), "--stage", "final", "--layers",
                    "L1,L1b,L2,L6", "--out", str(out), "--blind-cards", "--quiet"]
            subprocess.run([sys.executable, "-I", str(LAB / "common" / "launch.py"), "critic", *argv], check=True)
            shutil.rmtree(tmp)
            for f in st["files"]:
                cj = out / f"{f['part']}.{pid}-{f['name'].split('-')[1]}.json"
                d = json.loads(cj.read_text("utf-8"))
                f["recheck"] = {"verdict": d["verdict"], "failed": d["L1"].get("failed"), "json": str(cj),
                                "card": d.get("card_blind") or d.get("card"),
                                "attack_ms": d["metrics"].get("attack_ms"), "head_silence_ms": d["metrics"].get("head_silence_ms"),
                                "l1b": [x["id"] for x in d.get("flags") or [] if x.get("layer") == "L1b"]}
                if d["verdict"] != "PASS":
                    bad += 1
            v = [f["recheck"]["verdict"] for f in st["files"]]
            print(f"[{pid}/{role}] kiểm lại L1: {v.count('PASS')}/{len(v)} ĐẠT", flush=True)
    (WORK / "master.json").write_text(json.dumps(rep, indent=1, ensure_ascii=False), "utf-8")
    return 1 if bad else 0


# ---------------------------------------------------------------- render (typing phrases)

WPMS = (60, 100)


def cmd_render(a) -> int:
    import numpy as np
    import soundfile as sf
    from build import measure
    from keys import phrases

    rep = json.loads((WORK / "master.json").read_text("utf-8"))
    mixes = []
    for pid, prof in rep["profiles"].items():
        for role, st in prof["sets"].items():
            sdir = Path(st["dir"])
            sets = {"key": [], "space": []}
            for f in sorted(st["files"], key=lambda f: f["name"]):
                y, _ = sf.read(str(sdir / f["master"]))
                sets[f["part"]].append(y)
            for wpm in WPMS:
                y, info = phrases.render(sets, wpm, seed=2910 + wpm)
                mixes.append((pid, role, wpm, sdir, y, info))
    # one gain for every render: the loudest reaches -1 dBTP, the others keep their place under it
    tp = max(measure.true_peak_db(y, SR) for *_, y, _ in mixes)
    g = 10 ** ((-1.0 - tp) / 20)
    for pid, role, wpm, sdir, y, info in mixes:
        out = sdir / f"phrase-{wpm}wpm.wav"
        sf.write(str(out), (y * g).astype(np.float32), SR, subtype="PCM_24")
        info["common_gain_db"] = round(20 * np.log10(g), 2)
        info["lufs_i"] = round(measure.lufs_i(y * g, SR), 2)
        info["lufs_s_max"] = round(measure.lufs_s_max(y * g, SR), 2)
        (sdir / f"phrase-{wpm}wpm.json").write_text(json.dumps(info, indent=1), "utf-8")
        rep["profiles"][pid]["sets"][role].setdefault("phrases", {})[str(wpm)] = {
            "file": str(out), "lufs_i": info["lufs_i"], "lufs_s_max": info["lufs_s_max"]}
        print(f"[{pid}/{role}] {wpm} WPM: {len(y) / SR:.1f} s, LUFS-I {info['lufs_i']:.1f}", flush=True)
    rep["phrase_common_gain_db"] = round(20 * np.log10(g), 2)
    (WORK / "master.json").write_text(json.dumps(rep, indent=1, ensure_ascii=False), "utf-8")
    return 0


# ---------------------------------------------------------------- session (Listening Board)

SESSION = "keys-1"
BATCH = "keys-29-10"
DESC = {
    "creamy": "Creamy: switch linear đã bôi trơn, keycap PBT, đáy phím êm và sâu (creamy), không có tiếng click",
    "thock": "Thock: switch tactile nặng trong vỏ nhôm, tiếng 'thock' trầm, có cộng hưởng, gọn",
    "clicky": "Clicky: switch click-jacket (kiểu box jade), tiếng click sáng, gọn, không gắt",
    "dome": "Soft Dome: cảm giác cao su điện dung (kiểu Topre), 'thock' tròn mềm, đuôi ngắn",
    "spring": "Classic Spring: bàn phím lò xo gãy cổ điển, tiếng 'ping' của lò xo và tiếng clack chắc, ngắn",
}


def cmd_session(a) -> int:
    rep = json.loads((WORK / "master.json").read_text("utf-8"))
    items = []
    for pid in PROFILES:
        prof = rep["profiles"].get(pid)
        if not prof:
            continue
        cands = []
        for role, st in prof["sets"].items():
            sdir = Path(st["dir"])
            files = sorted(st["files"], key=lambda f: (f["part"] != "key", f["name"]))
            cands.append({"files": [str(sdir / f["master"]) for f in files], "role": role,
                          "critics": [(f.get("recheck") or {}).get("json") for f in files],
                          "cards": [(f.get("recheck") or {}).get("card") for f in files],
                          "ctx": {"scene": st["phrases"]["60"]["file"], "burst": st["phrases"]["100"]["file"]}})
        items.append({"id": f"keys.{pid}", "family": "phim-ui", "group": "phim-dung", "mode": "hero",
                      "desc": DESC[pid] + ". Mỗi bản là một bộ 10 phím + 3 phím cách.",
                      "contexts": ["scene", "burst", "loop", "alone", "small"],
                      "ctx_labels": {"scene": "Gõ 60 WPM", "burst": "Gõ 100 WPM"},
                      "loop": {"interval_ms": 200, "jitter": 0.35, "cents": 50, "db": 0.7, "gap_ms": 30, "avoid": 2,
                               "count": 20},
                      "probe": any(c["role"] == "probe" for c in cands), "candidates": cands})
    # the five keyboards side by side (top sets, 60 WPM phrase): which to keep, which sound alike
    side = []
    for pid in PROFILES:
        prof = rep["profiles"].get(pid)
        if prof and "top" in prof["sets"]:
            side.append({"file": prof["sets"]["top"]["phrases"]["60"]["file"], "role": f"profile:{pid}"})
    if len(side) >= 2:
        items.append({"id": "keys.compare", "family": "phim-ui", "mode": "style",
                      "desc": "Năm bàn phím cạnh nhau (bộ máy xếp đầu, câu gõ 60 WPM). Chấm sao cho từng bàn phím; "
                              "ghi chú nếu hai bản nghe giống nhau.",
                      "contexts": ["alone", "small"], "candidates": side})
    sess = {"schema": "audiolab.board.session/1", "session": SESSION, "game": "keys", "batch": BATCH,
            "title": "Tiếng phím · 5 bàn phím (29/10)", "seed": 2910, "max_minutes": 20, "anchors": 0,
            "reveal": "item", "target_lufs": -23, "items": items}
    dest = REVIEW / "sessions" / f"{SESSION}.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    state = REVIEW / "state" / f"{SESSION}.json"
    if dest.exists() and not a.force:
        print(f"đã có {dest}; thêm --force để ghi lại", flush=True)
        return 2
    if state.exists() and a.force:
        print(f"CẢNH BÁO: anh đã mở phiên này ({state}); không ghi đè", flush=True)
        return 2
    dest.write_text(json.dumps(sess, indent=1, ensure_ascii=False), "utf-8")
    from board import session as bsession
    s = bsession.load(dest)
    print(f"phiên {dest}: {len(s.items)} mục, {sum(len(i.candidates) for i in s.items)} bản", flush=True)
    return 0

# ---------------------------------------------------------------- stage (layout the kit reads) + manifests

NAMES = {"creamy": "Creamy", "thock": "Thock", "clicky": "Clicky", "dome": "Soft Dome", "spring": "Classic Spring"}
MANIFEST_SCHEMA = "audiolab.keys.manifest/1"


KIT_FILE = re.compile(r"(?:^|/)(key|space)-(\d{2})\.(?:ogg|opus|webm|m4a|mp3|wav|flac)$", re.I)


def kit_files(manifest, depth: int = 0, found: dict | None = None) -> dict[str, list[str]]:
    """Python twin of keyboardFiles() in shared/game-kit/feedback/typing-fx/audio.ts: every string of the
    manifest that ends in key-NN.<ext> / space-NN.<ext> (no scheme, no leading /, no ..), first one per number."""
    top = found is None
    found = found if found is not None else {"key": {}, "space": {}}
    if depth > 6 or manifest is None:
        pass
    elif isinstance(manifest, str):
        v = manifest.strip()
        m = KIT_FILE.search(v)
        if m and not re.match(r"^[a-z]+:|^/", v, re.I) and ".." not in v:
            found[m.group(1).lower()].setdefault(int(m.group(2)), v)
    elif isinstance(manifest, list):
        for x in manifest:
            kit_files(x, depth + 1, found)
    elif isinstance(manifest, dict):
        for x in manifest.values():
            kit_files(x, depth + 1, found)
    if not top:
        return found
    return {k: [v[n] for n in sorted(v)] for k, v in found.items()}


def _licence_rows(pid: str, runs: set[str]) -> list[dict]:
    from build import ledger
    rows = {}
    for r in sorted(runs):
        for row in ledger.read_rows(WORK / pid / r / "strokes" / "licences.rows.jsonl"):
            rows[row["key"]] = row
    return list(rows.values())


def owner_picks() -> tuple[dict[str, str], set[str]]:
    """The owner's choice per profile from ~/AudioLab/review/keys/ratings.jsonl (last line per item wins; the
    line carries the role of every candidate it showed)."""
    rpath = REVIEW / "ratings.jsonl"
    if not rpath.is_file():
        return {}, set()
    last = {}
    for line in rpath.read_text("utf-8").splitlines():
        if line.strip():
            row = json.loads(line)
            if row.get("session") == SESSION and str(row.get("id", "")).startswith("keys."):
                last[row["id"][5:]] = row
    picks, rejected = {}, set()
    for pid, row in last.items():
        if pid not in PROFILES:
            continue
        if row.get("none"):
            rejected.add(pid)
        elif row.get("pick") in (row.get("roles") or {}):
            picks[pid] = row["roles"][row["pick"]]
    return picks, rejected


def cmd_stage(a) -> int:
    from build import ledger

    rep = json.loads((WORK / "master.json").read_text("utf-8"))
    choice = _choices(a.choice)
    status = "candidate: the owner has not listened yet (Listening Board session keys-1)"
    if a.from_ratings:
        owner, rejected = owner_picks()
        choice = {**owner, **choice}
        if owner or rejected:
            status = (f"owner picks from session keys-1: {', '.join(f'{k}={v}' for k, v in sorted(owner.items())) or 'none'}"
                      + (f"; rejected (no set passed): {', '.join(sorted(rejected))}" if rejected else ""))
        for pid in rejected:
            print(f"[{pid}] anh chọn 'Không bản nào đạt': không đưa vào staging", flush=True)
    date = ledger.today()
    STAGING.mkdir(parents=True, exist_ok=True)
    art = STAGING / "_art-src"
    index = {"schema": "audiolab.keys.index/1", "generated": date, "status": status,
             "layout": "<profile>/keys-manifest.json + <profile>/key-NN.ogg, space-NN.ogg (shared/game-kit/feedback/typing-fx "
                       "loadKeyboard(base, id)); masters and SOURCES under _art-src/<profile>/",
             "loudness": {"metric": "LUFS-M max (400 ms window, clip padded to 0.4 s)", "target": rep["target_lufs_m_max"],
                          "truePeakCeilingDbtp": TP_CEILING, "scope": "every file of every profile"},
             "session": str(REVIEW / "sessions" / f"{SESSION}.json"), "profiles": []}
    lic_copies = set()
    for pid in PROFILES:
        prof = rep["profiles"].get(pid)
        if not prof or (a.from_ratings and pid in rejected):
            continue
        role = choice.get(pid) or prof.get("chosen") or "top"
        st = prof["sets"][role]
        sdir = Path(st["dir"])
        dest = STAGING / pid
        if dest.exists():
            shutil.rmtree(dest)
        dest.mkdir(parents=True)
        adir = art / pid
        if adir.exists():
            shutil.rmtree(adir)
        (adir / "masters").mkdir(parents=True)
        runs = {f["run"] for f in st["files"]}
        srcs = {}
        for r in runs:
            srcs.update({k: v for k, v in ledger.read_sources(WORK / pid / r / "strokes" / "SOURCES.json").items()
                         if k != "$version"})
        rows = _licence_rows(pid, runs)
        files, sources = [], {}
        for f in sorted(st["files"], key=lambda f: (f["part"] != "key", f["name"])):
            ogg = f"{f['name']}.ogg"
            shutil.copy2(sdir / f["runtime"], dest / ogg)
            shutil.copy2(sdir / f["master"], adir / "masters" / f"{f['name']}.wav")
            src = srcs[f"{f['stem']}.wav"]
            layer = dict(src["layers"][0])
            proc = json.loads((WORK / pid / f["run"] / "strokes" / f"{f['stem']}.proc.json").read_text("utf-8"))
            chain = (proc["chain"].rsplit(", gain", 1)[0]
                     + f", gain to {rep['target_lufs_m_max']:g} LUFS-M max ({f['gain_db'] + proc['gain_db']:+.2f} dB from the take), "
                     f"PCM 24-bit master, OGG Vorbis q{OGG_QUALITY:g}")
            sources[ogg] = {"id": f"{f['part']}.{pid}", "game": "keys", "variant": int(f["name"].split("-")[1]),
                            "sha256": ledger.sha256_file(dest / ogg), "date": date, "run": f["run"],
                            "master": f"masters/{f['name']}.wav", "masterSha256": f["master_sha256"],
                            "durationMs": f["duration_ms"], "sampleRate": SR, "channels": 1, "layers": [layer],
                            "chain": chain, "tools": src["tools"], "models": src["models"], "aiSteps": src.get("aiSteps", []),
                            "aiInputAllowed": True, "rawQa": f"{f['stem']}.proc.json", "review": None}
            files.append({"file": ogg, "set": f["part"], "durationMs": f["duration_ms"],
                          "lufsMMax": f["ogg_lufs_m_max"], "truePeakDbtp": f["ogg_true_peak_dbtp"],
                          "headMs": f["ogg_head_ms"], "bytes": f["runtime_bytes"], "sha256": sources[ogg]["sha256"],
                          "master": {"sha256": f["master_sha256"], "lufsMMax": f["lufs_m_max"], "truePeakDbtp": f["true_peak_dbtp"],
                                     "lufs100msMax": f["lufs_100ms_max"]},
                          "source": {"model": layer.get("model"), "prompt": layer.get("prompt"), "seed": layer.get("seed"),
                                     "take": f["take"], "takeWindowS": layer.get("window"), "stroke": f["kind"],
                                     "licence": layer.get("licence")},
                          "critic": {"verdict": (f.get("recheck") or {}).get("verdict"), "Q": f["Q"], "fit": f["fit"],
                                     "audioboxPQ": f["pq"], "astTyping": f["ast"], "criticScore": f["critic_score"]}})
        ledger.write_sources(adir / "SOURCES.json", sources)
        ledger.append_rows(adir / "licences.jsonl", rows)
        for r in rows:
            if r.get("licenceCopy"):
                lic_copies.add(r["licenceCopy"])
        lm = [x["lufsMMax"] for x in files]
        man = {"schema": MANIFEST_SCHEMA, "id": pid, "name": NAMES[pid], "files": files,
               "set": role, "status": status, "generated": date,
               "target": DESC[pid].split(": ", 1)[1],
               "format": {"runtime": f"OGG Vorbis 48 kHz mono, quality {OGG_QUALITY:g}",
                          "master": "WAV 48 kHz 24-bit mono (_art-src/" + pid + "/masters/<name>.wav)"},
               "counts": {"key": sum(1 for x in files if x["set"] == "key"), "space": sum(1 for x in files if x["set"] == "space")},
               "loudness": {"metric": index["loudness"]["metric"], "target": rep["target_lufs_m_max"],
                            "min": min(lm), "max": max(lm), "spreadDb": round(max(lm) - min(lm), 2),
                            "truePeakMaxDbtp": max(x["truePeakDbtp"] for x in files)},
               "lengthMs": {"key": [min(x["durationMs"] for x in files if x["set"] == "key"), max(x["durationMs"] for x in files if x["set"] == "key")],
                            "space": [min(x["durationMs"] for x in files if x["set"] == "space"), max(x["durationMs"] for x in files if x["set"] == "space")]},
               "playback": {"pitch": 0.03, "level": 0.08, "note": "kit defaults (TypingSoundProfile.pitch, .level); the phrases "
                                                                   "on the board were rendered with them"},
               "family": {"key": st["key_report"], "space": st["space_report"]},
               "licence": {"summary": "Generated with Stable Audio 3 Small-SFX on this machine (Stability AI Community License, "
                                      "owner registered as an individual 23/10/2026); the owner owns the output. No downloaded "
                                      "sound packs, no synthesis.", "rows": rows,
                           "sourcesFile": f"_art-src/{pid}/SOURCES.json", "ledgerFile": f"_art-src/{pid}/licences.jsonl"}}
        seen = kit_files(man)
        want = {p_: [x["file"] for x in files if x["set"] == p_] for p_ in PARTS}
        if seen != want:
            raise SystemExit(f"[{pid}] keys-manifest.json: bộ đọc của kit thấy {seen}, cần {want}")
        (dest / "keys-manifest.json").write_text(json.dumps(man, indent=1, ensure_ascii=False), "utf-8")
        index["profiles"].append({"id": pid, "name": NAMES[pid], "folder": f"{pid}/", "manifest": f"{pid}/keys-manifest.json",
                                  "set": role, "keys": man["counts"]["key"], "spaces": man["counts"]["space"],
                                  "lufsMMax": [man["loudness"]["min"], man["loudness"]["max"]],
                                  "lengthMs": man["lengthMs"]})
        print(f"[{pid}] staging {dest} ({len(files)} file, bộ {role}, LUFS-M {min(lm):.2f}..{max(lm):.2f})", flush=True)
    (art / "licences").mkdir(parents=True, exist_ok=True)
    for rel in sorted(lic_copies):
        src = env.HOME / rel
        if src.is_file():
            shutil.copy2(src, art / "licences" / Path(rel).name)
    (STAGING / "keys-manifest.json").write_text(json.dumps(index, indent=1, ensure_ascii=False), "utf-8")
    print(f"chỉ mục {STAGING / 'keys-manifest.json'}", flush=True)
    return 0

# ---------------------------------------------------------------- CLI

def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if argv[:1] == ["firefly"]:                  # its own sub-commands and --help
        from keys import firefly
        env.apply()
        return firefly.main(argv[1:])
    ap = argparse.ArgumentParser(prog="keys", description="Năm bộ tiếng phím (Audio Lab).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("generate", help="Stable Audio 3: đoạn gõ 10 s và cú gõ đơn 1 s")
    g.add_argument("--profiles")
    g.add_argument("--prompts", help="khóa prompt, mặc định A,B,C,D")
    g.add_argument("--seeds", default="101-103")
    g.add_argument("--single-seconds", default="1")
    g.add_argument("--run", default="r1")
    s = sub.add_parser("slice", help="tách từng cú gõ")
    s.add_argument("--profiles")
    s.add_argument("--run", default="r1")
    s.add_argument("--force", action="store_true")
    c = sub.add_parser("critic", help="tai AI: L1, L1b, L2, L3, L4, thẻ ảnh mù")
    c.add_argument("--profiles")
    c.add_argument("--run", default="r1")
    c.add_argument("--layers", default="all")
    k = sub.add_parser("pick", help="cổng, xếp hạng, chọn bộ biến thể nhất quán và danh sách nghe")
    k.add_argument("--profiles")
    k.add_argument("--run", default="r1")
    k.add_argument("--runs", help="gộp nhiều lần chạy, vd. r1,r2")
    mm = sub.add_parser("master", help="một đích độ to chung, master WAV và OGG cho mọi bộ trong danh sách nghe")
    mm.add_argument("--profiles")
    mm.add_argument("--choice", help="bộ được chọn theo hồ sơ, vd. creamy=distinct (mặc định top)")
    mm.add_argument("--target", help="ép đích LUFS-M max")
    rc_ = sub.add_parser("recheck", help="kiểm lại L1, L1b, L2 và thẻ ảnh mù trên master")
    rc_.add_argument("--profiles")
    sub.add_parser("render", help="câu gõ 60 và 100 WPM cho mọi bộ")
    se = sub.add_parser("session", help="phiên Bảng Nghe keys-1")
    se.add_argument("--force", action="store_true")
    sg = sub.add_parser("stage", help="~/AudioLab/review/staging/keys/<profile>/ + keys-manifest.json")
    sg.add_argument("--choice", help="bộ cho từng hồ sơ, vd. creamy=distinct (mặc định: bộ đã chọn ở master)")
    sg.add_argument("--from-ratings", action="store_true", help="lấy bộ anh chọn trên Bảng Nghe (phiên keys-1)")
    ff = sub.add_parser("firefly", help="bản Adobe Firefly của chủ dự án: survey (chỉ đọc), build (phiếu 189)",
                        add_help=False)
    ff.add_argument("rest", nargs=argparse.REMAINDER)
    a = ap.parse_args(argv)
    env.apply()
    return {"generate": cmd_generate, "slice": cmd_slice, "critic": cmd_critic, "pick": cmd_pick,
            "master": cmd_master, "recheck": cmd_recheck, "render": cmd_render, "session": cmd_session,
            "stage": cmd_stage}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
