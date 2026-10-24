"""Batch 0b, round 2: the six Stable Audio 3 trial ids reworked after the trial review.

  run.sh batch0b all [--run sa3-r2] [--force]
  run.sh batch0b generate|process|recipes|critic|link|session|report [--run sa3-r2]

generate  new candidates only where the review asked for other prompts (gen/sa3.py, from the cards):
          amb.forest E-H (no "birds" word, needles, stereo), call-chop E-G (prompt-A family: deep
          solid knock), enemy.quadruped.howl A and D at 2 s and 3 s (whole calls).
process   every raw candidate (144 of the trial + the new ones) through gen/process.py: true onsets
          for every window, creatures whole, exponential tail cap, card channels, comb notch for
          amb.forest, loop crossfade with a seam check.
recipes   layered recipes (build/recipes/<game>/<id>.sa3-r2.json): fire.impact.a (Kenney front + SA3
          body + sub <= 150 ms), gun.xung (Kenney breech + SA3 body from the boom, one shot + synth
          sub), hit.t1 (Kenney onset + SA3 clank + SA3 200-800 Hz body).
critic    one full critic run over every round-2 final (one model load); a raw-stage run on the howl
          finals for their learned layers (the creature rise rule blocks whole calls at final); an
          L1 run on every raw file (clip checks read the float copies).
link      critic AI steps into the SOURCES.json of the processed folders and recipe runs, a batch-local
          release tree of the recipe runs, licence-check on it.
session   Listening Board sessions "0b" in ~/AudioLab/review/<game>/sessions/ (never overwritten
          without --force), cards revealed at the end of a session. Never offered (review 2): an
          unverified file-start onset (proc.json onset_verified false), a double_onset or lr_imbalance
          flag; beds must be wide stereo (no near_mono or stereo_mismatch) with no loop signature.
report    ~/AudioLab/work/_batch0b/<run>/REPORT.md and summary.json.
Nothing is written under games/**; the official ~/AudioLab/review/staging stays empty (nothing here
is owner-approved).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
from pathlib import Path

import numpy as np

from common import env

LAB = env.LAB
IDS = [("typing-survival", "hit.t1"), ("typing-defense", "call-chop"), ("typing-survival", "gun.xung"),
       ("dragon-hold", "amb.forest"), ("dragon-hold", "enemy.quadruped.howl"), ("dragon-hold", "fire.impact.a")]
GAME = dict((sid, g) for g, sid in IDS)
NEW_JOBS = {
    "call-chop": [{"variants": ["E", "F", "G"], "seeds": "2001-2006"}],
    "amb.forest": [{"variants": ["E", "F", "G", "H"], "seeds": "2001-2006"}],
    "enemy.quadruped.howl": [{"variants": ["A", "D"], "seeds": "2001-2006", "seconds": 2.0, "tag": True},
                             {"variants": ["A", "D"], "seeds": "2001-2006", "seconds": 3.0, "tag": True}],
}
RECIPES = ("hit.t1", "gun.xung", "fire.impact.a")
NOTCH = {"amb.forest"}
A_FAMILY = ("A", "E", "F", "G")          # call-chop: deep solid knock (spec); B is the hollow "tốc"
PROBE_IDS = ("hit.t1", "amb.forest")      # §4.6 step 2: a machine-low probe at about 30 % of ids
RECIPE_DISTINCT = ("hit.t1",)             # review 2: distinct from the recipe variants, not a thin raw take
SEED = 20261023


def _say(msg: str) -> None:
    print(f"[batch0b] {msg}", flush=True)


def base_dir(run: str) -> Path:
    p = env.WORK / "_batch0b" / run
    p.mkdir(parents=True, exist_ok=True)
    return p


def id_dir(sid: str, run: str) -> Path:
    return env.WORK / GAME[sid] / sid / run


def card_path(sid: str) -> Path:
    return LAB / "specs" / GAME[sid] / f"{sid}.yaml"


def raw_dirs(sid: str, run: str) -> list[Path]:
    out = [env.WORK / GAME[sid] / sid / "sa3-trial" / "raw", id_dir(sid, run) / "raw"]
    return [p for p in out if p.is_dir()]


def recipe_run(sid: str, run: str) -> Path:
    return env.WORK / GAME[sid] / sid / f"{run}-recipe"


# ---------------------------------------------------------------- steps 1-3

def step_generate(run: str, force: bool = False) -> None:
    from gen import sa3

    for sid, jobs in NEW_JOBS.items():
        card = sa3.read_card(card_path(sid))
        for j in jobs:
            job = sa3.build_job(card, variants=j["variants"], seeds=sa3.parse_seeds(j["seeds"]),
                                seconds=j.get("seconds"), tag_seconds=bool(j.get("tag")))
            res = sa3.run_job(job, id_dir(sid, run))
            _say(f"sa3 {sid} {','.join(j['variants'])} {job['_meta']['seconds']:g} s: {res['todo']} mới, "
                 f"{res['skipped']} đã có" + (f", {res['loop_s']} s" if res.get("loop_s") else ""))


def step_process(run: str, force: bool = False) -> None:
    from gen import process, sa3

    for sid in GAME:
        card = sa3.read_card(card_path(sid))
        recs = process.collect_records([str(d) for d in raw_dirs(sid, run)])
        res = process.process_many(recs, card, id_dir(sid, run) / "processed", notch=sid in NOTCH, force=force)
        _say(f"process {sid}: {res['kept']} giữ, {len(res['rejected'])} loại, {res['skipped']} đã có")
        for r in res["rejected"]:
            _say(f"  loại {r['candidate']}: {r['reason']}")


def step_recipes(run: str, force: bool = False) -> None:
    from build import render

    for sid in RECIPES:
        g = GAME[sid]
        out = recipe_run(sid, run)
        if out.is_dir() and (out / "render.json").is_file() and not force:
            _say(f"recipe {sid}: đã có {out}")
            continue
        res = render.render(LAB / "build" / "recipes" / g / f"{sid}.sa3-r2.json", out=out, spec=card_path(sid))
        _say(f"recipe {sid}: {res.report['count']} biến thể, mức id {res.report['idLevel']} LUFS-M; "
             + ("; ".join(res.report["warnings"]) or "không cảnh báo"))


# ---------------------------------------------------------------- step 4: critic

def critic_out(run: str, name: str) -> Path:
    return base_dir(run) / f"critic-{name}"


def finals(run: str) -> tuple[list[Path], list[Path]]:
    """(folders with round-2 finals, their SOURCES.json)."""
    dirs, srcs = [], []
    for sid in GAME:
        p = id_dir(sid, run) / "processed"
        dirs.append(p)
        srcs.append(p / "SOURCES.json")
        if sid in RECIPES:
            r = recipe_run(sid, run)
            dirs.append(r / "masters")
            srcs.append(r / "SOURCES.json")
    return dirs, srcs


def step_critic(run: str, force: bool = False) -> None:
    from critic.__main__ import main as critic

    dirs, srcs = finals(run)
    argv = ["run", *map(str, dirs), "--spec", str(LAB / "specs"), "--stage", "final", "--layers", "all",
            "--out", str(critic_out(run, "final")), "--seed", str(SEED), "--blind-cards", "--quiet"]
    for s in srcs:
        argv += ["--sources", str(s)]
    _say(f"critic final ({len(dirs)} thư mục): mã {critic(argv)}")
    howl = id_dir("enemy.quadruped.howl", run) / "processed"
    argv = ["run", str(howl), "--spec", str(card_path("enemy.quadruped.howl")), "--stage", "raw", "--layers", "all",
            "--out", str(critic_out(run, "howl-info")), "--seed", str(SEED), "--sources", str(howl / "SOURCES.json"),
            "--blind-cards", "--quiet"]
    _say(f"critic howl (giai đoạn raw, chỉ để có L3–L4 cho tiếng tru nguyên vẹn): mã {critic(argv)}")
    raws = [str(d) for sid in GAME for d in raw_dirs(sid, run)]
    argv = ["run", *raws, "--spec", str(LAB / "specs"), "--stage", "raw", "--layers", "L1,L1b",
            "--out", str(critic_out(run, "raw")), "--quiet"]
    _say(f"critic raw L1 (clip đọc bản float): mã {critic(argv)}")


# ---------------------------------------------------------------- step 5: ledger + release check

def staging_dirs(run: str, game: str) -> tuple[Path, Path]:
    """Batch-local release tree. Not ~/AudioLab/review/staging: nothing here is owner-approved yet."""
    root = base_dir(run) / "staging" / game
    return root / "art-src" / "audio", root / "public" / "assets" / game / "audio"


def step_link(run: str, force: bool = False) -> int:
    from build import critic_link, licence_check, release

    out = critic_out(run, "final")
    for sid in GAME:
        p = id_dir(sid, run) / "processed"
        res = critic_link.apply(p / "SOURCES.json", [out, critic_out(run, "howl-info")], p / "licences.rows.jsonl")
        _say(f"mark-ai {sid} (processed): {res['steps']} bước, {res['files']} hồ sơ")
    games = set()
    for sid in RECIPES:
        r = recipe_run(sid, run)
        res = critic_link.apply(r / "SOURCES.json", [out], r / "licences.rows.jsonl")
        art, pub = staging_dirs(run, GAME[sid])
        rel = release.release(r, None, art, pub)
        games.add(GAME[sid])
        _say(f"mark-ai {sid} (recipe): {res['steps']} bước; release -> {art.parent.parent}: {len(rel['files'])} file, "
             f"{rel['rowsAdded']} dòng sổ, {len(rel['licenceCopies'])} bản giấy phép")
    worst = 0
    for g in sorted(games):
        art, pub = staging_dirs(run, g)
        rc = licence_check.main(["--art-src", str(art), "--public", str(pub)])
        _say(f"licence-check (cây thử) {g}: mã {rc}")
        worst = max(worst, rc)
    return worst


# ---------------------------------------------------------------- step 6: sessions

def _docs(out: Path) -> dict[str, dict]:
    docs = {}
    for p in sorted(out.glob("*.json")):
        if p.name.startswith("_"):
            continue
        d = json.loads(p.read_text("utf-8"))
        docs[d["file"]["stem"]] = d
    return docs


def _sid_of(d: dict) -> str:
    return (d.get("spec") or {}).get("id") or ""


def _variant(stem: str) -> str:
    parts = stem.split("__")
    return parts[1] if len(parts) >= 3 else "recipe"


def _cand(out: Path, d: dict, role: str, note: str | None = None) -> dict:
    from board import session

    c = {"file": session.display_path(Path(d["file"]["path"])), "role": role,
         "critic": session.display_path(out / f"{d['file']['stem']}.json")}
    card = d.get("card_blind") or d.get("card")
    if card and (out / card).is_file():
        c["card"] = session.display_path(out / card)
    if note:
        c["note"] = note
    return c


def _rank(d: dict) -> float:
    return (d.get("score") or {}).get("rank") or 1e9


def _flags(d: dict) -> set[str]:
    return {f["id"] for f in d.get("flags") or []}


def _proc(d: dict) -> dict:
    """gen/process.py report beside a processed file ({} for recipe masters)."""
    p = Path(d["file"]["path"]).with_suffix(".proc.json")
    try:
        return json.loads(p.read_text("utf-8"))
    except (OSError, ValueError):
        return {}


def _verified(d: dict) -> bool:
    """Review 2: a file start without evidence is no true onset; never offered for listening."""
    return _proc(d).get("onset_verified", True) is not False


# never offered for listening (review 2): two onsets in one shot; a bed leaning to one side
NO_PICK_FLAGS = {"double_onset", "lr_imbalance"}


def _distinct(top: dict, pool: list[dict]) -> dict | None:
    from critic import score
    if not pool:
        return None
    V = np.stack([score._vec(d) for d in [top, *pool]])
    sd = V.std(axis=0)
    sd[sd == 0] = 1.0
    return pool[int(np.argmax(np.linalg.norm((V[1:] - V[0]) / sd, axis=1)))]


def _upper(order: list[dict]) -> list[dict]:
    """The machine's upper half after the top: where the 'most different' pick comes from (the
    lower half is the probe's; batch 0b r2: the most different bed overall was the 48th of 48)."""
    return order[1:max(2, (len(order) + 1) // 2)]


def _probe(sid: str, order: list[dict], used: set[str]) -> dict | None:
    half = order[max(1, len(order) // 2):]
    pool = [d for d in half if d["file"]["stem"] not in used]
    if not pool:
        return None
    rng = random.Random(int(hashlib.sha256(f"batch-0b-r2:{sid}".encode()).hexdigest()[:8], 16))
    return rng.choice(sorted(pool, key=lambda d: d["file"]["stem"]))


def _item(sid: str, desc: str, cands: list[dict], docs_any: dict, **extra) -> dict:
    sp = docs_any.get("spec") or {}
    item = {"id": sid, "family": sp.get("family") or "", "group": sp.get("group") or "", "desc": desc,
            "probe": any(c["role"] == "probe" for c in cands), "candidates": cands}
    if sp.get("rate_hz") and not sp.get("loop"):
        item["loop"] = {"interval_ms": round(1000.0 / sp["rate_hz"])}
    if sp.get("loop"):
        item["loop"] = {"seamless": True}
    item.update(extra)
    return item


def select(run: str) -> dict[str, dict]:
    """Per id: the listening list of round 2, with the reasons (also written to summary.json)."""
    out = critic_out(run, "final")
    docs = _docs(out)
    info = _docs(critic_out(run, "howl-info")) if critic_out(run, "howl-info").is_dir() else {}
    sel: dict[str, dict] = {}
    for sid in GAME:
        mine = [d for d in docs.values() if _sid_of(d) == sid]
        ok = sorted([d for d in mine if d["verdict"] == "PASS"], key=_rank)
        entry: dict = {"n": len(mine), "pass": len(ok), "picks": []}
        unverified = [d for d in ok if not _verified(d)]
        flagged = [d for d in ok if _flags(d) & NO_PICK_FLAGS]
        entry.update({"pass_unverified_onset": len(unverified), "pass_no_pick_flags": len(flagged)})
        ok = [d for d in ok if _verified(d) and not _flags(d) & NO_PICK_FLAGS]
        probe_pool = None
        if sid == "gun.xung":            # review: SA3 only as a body layer -> the recipe variants
            ok = [d for d in ok if _variant(d["file"]["stem"]) == "recipe"]
        if sid == "amb.forest":          # the card wants stereo: near-mono loops are not offered
            stereo = [d for d in ok if "near_mono" not in _flags(d)]
            entry["stereo_pass"] = len(stereo)
            # review: knocks, chirps, tones and bands that come and go give the loop away; comb lines are a
            # defect; review 2: a bed under 0.3 correlation loses its highs folded to mono (G s2005)
            clean = [d for d in stereo if not _flags(d) & {"loop_signature", "decoder_comb", "stereo_mismatch"}]
            entry["stereo_clean_pass"] = len(clean)
            # review 2: the probe is machine-low but still a wide, clean stereo bed (not a near-mono one)
            probe_pool = clean or stereo or ok
            ok = clean or stereo or ok
        if sid == "call-chop":           # prefer the spec's deep solid knock (A family); one B as contrast
            fam_a = [d for d in ok if _variant(d["file"]["stem"])[:1] in A_FAMILY]
            fam_b = [d for d in ok if _variant(d["file"]["stem"])[:1] == "B"]
            top = fam_a[0] if fam_a else None
            dis = _distinct(top, _upper(fam_a)) if top else None
            picks = [(top, "top", None), (dis, "distinct", None),
                     (fam_b[0] if fam_b else None, "contrast-mo-risk",
                      "Đối chứng có chủ ý: tiếng 'tốc' rỗng, cao (giống mõ?)")]
            entry["picks"] = [(d, r, n) for d, r, n in picks if d is not None]
            sel[sid] = entry
            continue
        if sid == "enemy.quadruped.howl":
            # whole calls: the creature rise rule (<= 30 ms) blocks them at final; the owner judges
            # (rule change needs owner approval). Rank them by the raw-stage run's learned layers.
            blocked = [d for d in mine if d["verdict"] == "BLOCK" and set(d["L1"]["blocking"]) <= {"attack", "duration"}
                       and _verified(d)]
            ib = {s: info[s] for s in (d["file"]["stem"] for d in blocked) if s in info}
            final_block = {d["file"]["stem"]: d["L1"]["blocking"] for d in blocked}
            # prefer calls only the swell rule blocks (within the card's length); longer ones if too few
            ranked = sorted(ib.values(), key=_rank)
            swell_only = [d for d in ranked if final_block[d["file"]["stem"]] == ["attack"]]
            pool = swell_only if len(swell_only) >= 2 else ranked
            # the rule question needs howls: keep takes AST hears as the card's label (not a roar)
            heard = [d for d in pool if "ast_expected_missing" not in {f["id"] for f in d.get("flags") or []}]
            pool = heard if len(heard) >= 2 else pool

            def note(d):
                return "Bị luật chặn: tiếng tru lớn dần chậm (> 30 ms)" + (
                    "; dài hơn thẻ" if "duration" in final_block[d["file"]["stem"]] else "")
            picks = []
            if ok:
                picks.append((ok[0], "top", None))
            if pool:
                picks.append((pool[0], "rule-blocked-top", note(pool[0])))
                # the second: most different within the machine's upper half (never a low take)
                two = _distinct(pool[0], _upper(pool))
                if two is not None:
                    picks.append((two, "rule-blocked-distinct", note(two)))
            entry.update({"blocked_whole": len(blocked), "swell_only": len(swell_only), "heard_as_howl": len(heard),
                          "picks": picks})
            sel[sid] = entry
            continue
        if not ok:
            sel[sid] = entry
            continue
        top = ok[0]
        upper = _upper(ok)
        if sid in RECIPE_DISTINCT and _variant(top["file"]["stem"]) == "recipe":
            # review 2: the distinct take is another recipe variant (the raw takes lack the 200-800 Hz body)
            upper = [d for d in ok[1:] if _variant(d["file"]["stem"]) == "recipe"] or upper
        dis = _distinct(top, upper)
        picks = [(top, "top", None)] + ([(dis, "distinct", None)] if dis else [])
        if sid in PROBE_IDS:
            pr = _probe(sid, probe_pool or ok, {d["file"]["stem"] for d, _, _ in picks})
            if pr is not None:
                picks.append((pr, "probe", None))
        entry["picks"] = picks
        sel[sid] = entry
    return sel


DESC = {
    "hit.t1": "Đạn Xung trúng vỏ thép (bậc T1), 64–96 ms, lặp 5 lần mỗi giây",
    "gun.xung": "Pháo tự động Xung rời nòng, một phát, phát 5 lần mỗi giây",
    "call-chop": "Lời gọi Chặt: gõ gỗ trầm, chắc vào thân tre, 200–300 ms",
    "amb.forest": "Gió qua rừng thông, vòng lặp 6 s (nghe ít nhất 3 vòng để tìm chỗ nối)",
    "enemy.quadruped.howl": "Thú bốn chân tru gọi bầy, trọn một tiếng tru",
    "fire.impact.a": "Cầu lửa trúng: phụt lửa trầm, thân tròn, lách tách nhỏ",
}
SESSIONS = [("typing-survival", "0b-ts", "Lô 0b · Tuyến Cuối · Stable Audio 3, vòng 2", ["hit.t1", "gun.xung"]),
            ("typing-defense", "0b-td", "Lô 0b · Lời Gọi · Stable Audio 3, vòng 2", ["call-chop"]),
            ("dragon-hold", "0b-dh", "Lô 0b · Rồng Giữ Ải · Stable Audio 3, vòng 2",
             ["amb.forest", "enemy.quadruped.howl", "fire.impact.a"])]


class SessionExists(RuntimeError):
    pass


def step_session(run: str, force: bool = False) -> list[Path]:
    out = critic_out(run, "final")
    info_out = critic_out(run, "howl-info")
    sel = select(run)
    paths = []
    for game, sid_name, title, ids in SESSIONS:
        items = []
        for sid in ids:
            picks = sel[sid]["picks"]
            if not picks:
                _say(f"phiên {sid_name}: {sid} không có bản nào để nghe")
                continue
            cands = [_cand(info_out if r.startswith("rule-blocked") else out, d, r, n) for d, r, n in picks]
            desc = DESC[sid]
            if sid == "call-chop":
                desc += ". Một bản có nhãn ghi sẵn là đối chứng giống mõ: nếu nghe ra mõ chùa, gắn 'sai chất liệu'"
            if sid == "enemy.quadruped.howl":
                desc += ". Bản có nhãn ghi sẵn bị luật đầu tiếng sinh vật chặn; anh chấm như mọi bản"
            item = _item(sid, desc, cands, picks[0][0])
            if "interval_ms" in item.get("loop", {}):
                # never closer than the card's min gap, never overlapping the longest take
                import yaml
                gap = ((yaml.safe_load(card_path(sid).read_text("utf-8")) or {}).get("playback") or {}).get("min_gap_ms") or 0
                longest = max((d["metrics"].get("duration_ms") or 0) for d, _, _ in picks)
                item["loop"]["interval_ms"] = int(max(item["loop"]["interval_ms"], gap, longest + 50))
                if item["loop"]["interval_ms"] >= 1000:
                    item["loop"]["count"] = 8
            items.append(item)
        folder = env.REVIEW / game / "sessions"
        path = folder / f"{sid_name}.json"
        if path.exists() and not force:
            raise SessionExists(f"{path} đã có; thêm --force để ghi đè (điểm đã chấm vẫn giữ trong ratings.jsonl)")
        folder.mkdir(parents=True, exist_ok=True)
        doc = {"schema": "audiolab.board.session/1", "session": sid_name, "game": game, "batch": "0b", "title": title,
               "seed": int(hashlib.sha256(f"{game}:{sid_name}".encode()).hexdigest()[:8], 16), "max_minutes": 20,
               "anchors": 0, "reveal": "end", "items": items}
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", "utf-8")
        paths.append(path)
        _say(f"phiên {path}: {len(items)} id, {sum(len(i['candidates']) for i in items)} bản")
    return paths


# ---------------------------------------------------------------- step 7: report

def _fmt(v, nd=1):
    if v is None:
        return "–"
    if isinstance(v, float):
        return f"{v:.{nd}f}".replace(".", ",").replace("-", "−")
    return str(v)


def _note(r: dict) -> str:
    """Report column: what the owner should know beyond the flags (review 2)."""
    m, out = r["metrics"], []
    if m.get("stereo_correlation") is not None:
        out.append(f"tương quan L/R {_fmt(m['stereo_correlation'], 2)}, trái − phải {_fmt(m.get('lr_balance_db'), 1)} dB, "
                   f"bên/giữa {_fmt(m.get('side_mid_db'), 1)} dB")
    if m.get("share_below_150") is not None and r.get("loop"):
        out.append(f"dưới 150 Hz {_fmt(m['share_below_150'] * 100, 0)} %, 4–10 kHz "
                   f"{_fmt((r['loop'].get('ltas_share_4k_10k') or 0) * 100, 1)} %")
    if r.get("onset"):
        o = r["onset"]
        out.append(f"đầu tiếng {o.get('onset_kind')}" + ("" if o.get("onset_verified", True) else " chưa xác minh"))
    if (m.get("hf_reonset_db") is not None and (m.get("hf_reonset_dip_db") or 0) <= -6.0
            and (m.get("hf_reonset_rise_db") or 0) >= 4.0 and m["hf_reonset_db"] >= -12.0):     # a real rebound
        out.append(f"dải >2 kHz tụt {_fmt(m.get('hf_reonset_dip_db'), 1)} dB rồi lên lại {_fmt(m['hf_reonset_db'], 1)} dB "
                   f"sau {_fmt(m.get('hf_reonset_ms'), 0)} ms")
    return "; ".join(out) or "–"


def _row(d: dict, role: str) -> dict:
    m, s = d["metrics"], d.get("score") or {}
    l3 = ((d.get("L3") or {}).get("scores")) or {}
    ast = (((d.get("L4") or {}).get("ast") or {}).get("top5") or [])[:2]
    return {"stem": d["file"]["stem"], "role": role, "verdict": d["verdict"], "blocking": d["L1"]["blocking"],
            "rank": s.get("rank"), "n_ranked": s.get("n_ranked"), "combined": s.get("combined"),
            "L2": (d.get("L2") or {}).get("score"), "PQ": l3.get("PQ"), "CE": l3.get("CE"),
            "ast": [(a[0], round(float(a[1]), 2)) if isinstance(a, (list, tuple)) else (a.get("label"), round(a.get("score"), 2))
                    for a in ast],
            "flags": [f["id"] for f in d.get("flags") or []],
            "metrics": {k: m.get(k) for k in ("duration_ms", "attack_ms", "crest_db", "share_200_800", "share_below_150",
                                               "share_1k_4k", "sub_len_ms", "tail_ms", "lufs_m_max", "stereo_correlation",
                                               "lr_balance_db", "lr_balance_bands_db", "side_mid_db", "hf_reonset_ms",
                                               "hf_reonset_db", "hf_reonset_rise_db", "hf_reonset_dip_db")
                        if m.get(k) is not None},
            "onset": {k: (_proc(d).get("window") or {}).get(k) for k in ("onset_kind", "onset_verified", "head_db", "hf_peak_ms")}
            if (_proc(d).get("window") or {}).get("onset_kind") else None,
            "loop": {k: (m.get("loop_spectrum") or {}).get(k) for k in ("ltas_share_above_8k", "ltas_share_4k_10k",
                                                                         "comb_median_prom_db")} if m.get("loop_spectrum") else None,
            "loop_signature": {k: (m.get("loop_signature") or {}).get(k) for k in ("knocks", "chirps", "bands")} if m.get("loop_signature") else None}


def _onset_counts(sid: str, run: str) -> dict:
    """Onset kinds of the processed (kept) Stable Audio 3 files of one id, from their proc.json."""
    out = {"kept": 0, "quiet": 0, "file_start": 0, "file_start_verified": 0, "file_start_unverified": 0, "loop": 0}
    for p in sorted((id_dir(sid, run) / "processed").glob("*.proc.json")):
        d = json.loads(p.read_text("utf-8"))
        out["kept"] += 1
        w = d.get("window") or {}
        kind = w.get("onset_kind")
        b = d.get("lr_balance") or {}
        if b.get("applied"):
            bl = out.setdefault("balanced", {"applied": 0, "max_before_db": 0.0, "max_after_db": 0.0})
            bl["applied"] += 1
            bl["max_before_db"] = max(bl["max_before_db"], abs(b["before"]["broadband_db"]))
            bl["max_after_db"] = max(bl["max_after_db"], abs(b["after"]["broadband_db"]))
        if kind is None:
            out["loop"] += 1
        elif kind == "file-start":
            out["file_start"] += 1
            out["file_start_verified" if w.get("onset_verified") else "file_start_unverified"] += 1
        else:
            out["quiet"] += 1
    return out


def step_report(run: str, force: bool = False) -> Path:
    sel = select(run)
    out = critic_out(run, "final")
    b = json.loads((out / "_batch.json").read_text("utf-8"))
    c = b.get("counts") or {}
    info_out = critic_out(run, "howl-info")
    n_info = (json.loads((info_out / "_batch.json").read_text("utf-8")).get("n_files")
              if (info_out / "_batch.json").is_file() else 0)
    summary = {"run": run, "critic": str(out), "counts": c, "n_files": b.get("n_files"), "howl_info_files": n_info,
               "ids": {}}
    lines = ["# Lô 0b vòng 2: Stable Audio 3, 6 id", "",
             "Tự sinh bởi `common/batch0b.py report`. Thẻ ảnh: `critic-final/<tên>.png` (bản cho Bảng Nghe: `.blind.png`).", "",
             f"Lần chấm cuối (`critic-final/_batch.json`): {b.get('n_files')} file, {c.get('PASS', 0)} ĐẠT, "
             f"{c.get('BLOCK', 0)} CHẶN, {c.get('NEEDS_FIX', 0)} CẦN SỬA. Lần chấm phụ `critic-howl-info` (giai đoạn raw, "
             f"chỉ để có điểm học máy cho tiếng tru nguyên vẹn) chấm lại {n_info} file tiếng tru đã có trong lần cuối, "
             "không phải file mới.", "",
             "Không đưa vào phiên nghe (vòng soát 2): bản có đầu tiếng chưa xác minh (âm kêu ngay từ mẫu đầu, "
             "xem `onset_verified` trong `<tên>.proc.json`), bản có cờ `double_onset` (hai đầu tiếng) hay "
             "`lr_imbalance` (lệch kênh).", ""]
    for sid in GAME:
        e = sel[sid]
        docs = [d for d in _docs(out).values() if _sid_of(d) == sid]
        blocks: dict[str, int] = {}
        for d in docs:
            for k in d["L1"]["blocking"]:
                blocks[k] = blocks.get(k, 0) + 1
        starts = _onset_counts(sid, run)
        rows = [_row(d, r) for d, r, _ in e["picks"]]
        summary["ids"][sid] = {"n": e["n"], "pass": e["pass"], "blocking": blocks, "picks": rows, "onsets": starts,
                               **{k: v for k, v in e.items() if k not in ("picks", "n", "pass")}}
        lines += [f"## `{sid}`", "", f"{e['n']} bản cuối, {e['pass']} qua cổng L1. Chặn: "
                  + (", ".join(f"{k} {v}" for k, v in sorted(blocks.items())) or "không") + ".", ""]
        if starts["kept"] and starts["loop"] == starts["kept"]:
            bal = starts.get("balanced") or {}
            lines += [f"Cân hai kênh (vòng soát 2): {bal.get('applied', 0)}/{starts['kept']} bản stereo được cân theo từng "
                      f"1/3 octave; lệch lớn nhất trước khi cân {_fmt(bal.get('max_before_db'), 1)} dB, sau khi cân "
                      f"{_fmt(bal.get('max_after_db'), 1)} dB.", ""]
        elif starts["kept"]:
            lines += [f"Đầu tiếng của {starts['kept']} bản Stable Audio 3 đã xử lý: {starts['quiet']} có khoảng lặng trước "
                      f"đầu tiếng, {starts['file_start']} bắt đầu từ đầu file ({starts['file_start_verified']} có bằng chứng, "
                      f"{starts['file_start_unverified']} chưa xác minh). Bản qua L1 nhưng không chọn: "
                      f"{e.get('pass_unverified_onset', 0)} vì đầu tiếng chưa xác minh, {e.get('pass_no_pick_flags', 0)} vì "
                      "cờ hai đầu tiếng hoặc lệch kênh.", ""]
        lines += ["| Vai trò | Bản | L1 | Hạng | Điểm | L2 | PQ | AST | Lên ms | 200–800 Hz | Cờ | Ghi chú |",
                  "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in rows:
            m = r["metrics"]
            lines.append(f"| {r['role']} | `{r['stem']}` | {r['verdict']} {','.join(r['blocking'])} | {r['rank'] or '–'}/{r['n_ranked'] or '–'} | "
                         f"{_fmt(r['combined'], 2)} | {_fmt(r['L2'], 2)} | {_fmt(r['PQ'], 2)} | "
                         f"{', '.join(f'{a} {s}' for a, s in r['ast']) or '–'} | {_fmt(m.get('attack_ms'))} | "
                         f"{_fmt((m.get('share_200_800') or 0) * 100, 0)} % | {', '.join(r['flags']) or '–'} | {_note(r)} |")
        lines.append("")
    path = base_dir(run) / "REPORT.md"
    path.write_text("\n".join(lines) + "\n", "utf-8")
    (base_dir(run) / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1, default=str), "utf-8")
    _say(f"báo cáo {path}")
    return path


STEPS = {"generate": step_generate, "process": step_process, "recipes": step_recipes, "critic": step_critic,
         "link": step_link, "session": step_session, "report": step_report}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="batch0b", description="Lô 0b vòng 2 (Stable Audio 3, 6 id).")
    ap.add_argument("step", choices=[*STEPS, "all"])
    ap.add_argument("--run", default="sa3-r2")
    ap.add_argument("--force", action="store_true", help="làm lại bước đã có; ghi đè file phiên")
    a = ap.parse_args(argv)
    env.apply()
    steps = list(STEPS) if a.step == "all" else [a.step]
    for name in steps:
        try:
            rc = STEPS[name](a.run, a.force)
        except SessionExists as exc:
            print(f"batch0b: {exc}", file=sys.stderr)
            return 1
        if name == "link" and rc:
            print("batch0b: kiểm giấy phép trượt; dừng trước khi lập phiên", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
