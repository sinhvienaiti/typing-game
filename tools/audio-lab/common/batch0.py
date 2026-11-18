"""Batch 0: one end-to-end run of the Audio Lab (phase 0-1 and the CC0 part of phase 2).

  run.sh batch0 all [--run NAME]          every step below, in order
  run.sh batch0 sampler|render|critic|link|session|report [--run NAME]

Inputs (45 sounds, 96 files): the 16 PoC originals (+ their 24 degraded copies as calibration
candidates), 14 Kenney CC0 files, 5 sampler renders and 10 layered recipes for real spec ids
(37 variants; wave.horn is a recipe with sampler layers, so it goes through the final chain).
Outputs: ~/AudioLab/work/_batch0/<run>/ (sampler renders, critic results, a release tree under
staging/<game>/ for licence_check), ~/AudioLab/work/<game>/<id>/<run>/ (recipe renders) and the
batch 0a Listening Board sessions in ~/AudioLab/review/<game>/sessions/. The official
~/AudioLab/review/staging/ is left alone: nothing here is owner-approved yet.
Nothing is written under games/**. Existing session files are never replaced without --force
(the owner may be rating them).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

from common import env

LAB = env.LAB
POC = env.FIXTURES / "poc40"
GAMES = ("dragon-hold", "typing-defense", "typing-survival")

# 14 Kenney CC0 files across impact, interface, sci-fi and RPG (none of the PoC eight).
KENNEY = [
    ("impact-sounds/Audio/impactPlate_light_001.ogg", "hit_small"),
    ("impact-sounds/Audio/impactWood_light_002.ogg", "hit_small"),
    ("impact-sounds/Audio/impactSoft_heavy_001.ogg", "hit_heavy"),
    ("impact-sounds/Audio/impactMining_003.ogg", "hit_small"),
    ("interface-sounds/Audio/click_001.ogg", "ui"),
    ("interface-sounds/Audio/select_003.ogg", "ui"),
    ("interface-sounds/Audio/error_004.ogg", "key_bad"),
    ("interface-sounds/Audio/pluck_001.ogg", "ui"),
    ("sci-fi-sounds/Audio/laserSmall_002.ogg", "shot_launch"),
    ("sci-fi-sounds/Audio/lowFrequency_explosion_000.ogg", "explosion"),
    ("sci-fi-sounds/Audio/thrusterFire_002.ogg", "whoosh"),
    ("rpg-audio/Audio/chop.ogg", "hit_heavy"),
    ("rpg-audio/Audio/handleCoins.ogg", "generic"),
    ("rpg-audio/Audio/metalClick.ogg", "ui"),
]

# Six sampler renders (CC0 VCSL / VSCO-2-CE). bpm 84 = Rồng Giữ Ải (D Dorian, §8.1).
SAMPLER = {
    "sampler-dan-tranh-scale": {
        "card": {"group": "stinger", "stereo": True, "pitched": True,
                 "intent": "a Vietnamese dan tranh zither, plucked notes"},
        "instrument": "dan-tranh.normal",
        "notes": [{"start": 0.3 * i, "note": n, "dur": 0.6 if i < 5 else 1.4, "vel": v, "choke": True}
                  for i, (n, v) in enumerate([("C4", 100), ("D4", 95), ("F4", 100), ("G4", 95), ("A4", 100), ("C5", 110)])]},
    "sampler-gong-leak": {
        "card": {"group": "alarm", "stereo": True, "intent": "a village gong strike, warning"},
        "instrument": "gong-1",   # choke: fade over the release after 1.3 s, like a damped village gong
        "notes": [{"start": 0, "key": "gong", "dur": 1.3, "vel": 96, "choke": True}]},
    "sampler-frame-drum": {
        "card": {"group": "generic", "stereo": True, "intent": "a frame drum, hand hits"},
        "instrument": "frame-drum", "bpm": 84,
        "notes": "0:hdruml-hit:0.5:110 1:hdrums-hit:0.5:80 1.5:hdrums-hit:0.5:70 2:hdruml-hit:0.5:105 3:hdrums-hitmuted:0.5:90"},
    "sampler-cello-dorian": {
        "card": {"group": "music", "loop": True, "stereo": True, "bpm": 84, "bars": 2, "pitched": True},
        "instrument": "cello-section.pizzt", "bpm": 84, "bars": 2,
        "notes": "0:D3:0.5:105 0.5:A3:0.5:85 1:D4:0.5:95 1.5:A3:0.5:80 2:C4:0.5:95 2.5:A3:0.5:80 3:B3:0.5:90 3.5:A3:0.5:80 "
                 "4:D3:0.5:105 4.5:A3:0.5:85 5:F3:0.5:95 5.5:G3:0.5:85 6:A3:0.5:95 6.5:C4:0.5:85 7:B3:0.5:90 7.5:A3:0.5:80"},
    "sampler-flute-dorian": {
        "card": {"group": "music", "loop": True, "stereo": True, "bpm": 84, "bars": 2, "pitched": True},
        "instrument": "flute.susvib", "bpm": 84, "bars": 2,
        "notes": "0:D5:1:85 1:E5:0.5:80 1.5:F5:0.5:85 2:A5:1.5:95 3.5:G5:0.5:80 4:F5:1:85 5:E5:1:80 6:D5:1.8:85"},
}

# Recipes for real spec ids (tools/audio-lab/build/recipes).
RECIPES = [
    "dragon-hold/fire.impact.a", "dragon-hold/trap.pine-bomb.trigger", "dragon-hold/wave.horn",
    "typing-survival/gun.xung", "typing-survival/hit.t1", "typing-survival/hit.t2",
    "typing-defense/ui-move", "typing-defense/ui-pick", "typing-defense/word-hit", "typing-defense/leak",
]


def base_dir(run: str) -> Path:
    p = env.WORK / "_batch0" / run
    p.mkdir(parents=True, exist_ok=True)
    return p


def _say(msg: str) -> None:
    print(f"[batch0] {msg}", flush=True)


# ---------------------------------------------------------------- step 1: sampler renders + cards

def step_sampler(run: str) -> list[Path]:
    from sampler.engine import Sampler, notes_from_json, parse_note_spec
    from sampler.instrument import from_index, load_index

    out_dir = base_dir(run) / "sampler"
    out_dir.mkdir(exist_ok=True)
    index = load_index(env.LIBRARIES / "index.json")
    written = []
    for name, cfg in SAMPLER.items():
        s = Sampler(seed=7)
        bpm = cfg.get("bpm")
        notes = parse_note_spec(cfg["notes"], bpm) if isinstance(cfg["notes"], str) else notes_from_json(cfg["notes"], bpm)
        for n in notes:
            n.instrument = n.instrument or cfg["instrument"]
        for inst in dict.fromkeys(n.instrument for n in notes):
            s.add(from_index(inst, index), inst)
        length = cfg["bars"] * 4 * 60.0 / bpm if cfg.get("bars") else None
        r = s.render(notes, length=length, tail="wrap" if length else "keep")
        path = r.write(out_dir / f"{name}.wav")
        rep = dict(r.report, notes_spec=cfg["notes"], bpm=bpm, bars=cfg.get("bars"))
        path.with_suffix(".json").write_text(json.dumps(rep, ensure_ascii=False, indent=1), "utf-8")
        _say(f"sampler {name}: {rep['duration']:.2f} s, {len(rep['notes'])} nốt, đỉnh {rep['peak_dbfs']} dBFS")
        written.append(path)
    write_cards(run)
    return written


def write_cards(run: str) -> Path:
    """Critic cards for the raw inputs: PoC cards + Kenney + sampler renders."""
    import yaml

    cards = yaml.safe_load((POC / "critic-cards.yaml").read_text("utf-8"))
    for rel, group in KENNEY:
        cards.append({"id": Path(rel).stem, "group": group})
    for name, cfg in SAMPLER.items():
        cards.append({"id": name, **cfg["card"]})
    path = base_dir(run) / "cards.yaml"
    path.write_text("# Critic cards for batch 0 raw inputs (generated by common/batch0.py)\n"
                    + yaml.safe_dump(cards, allow_unicode=True, sort_keys=False), "utf-8")
    return path


def raw_inputs(run: str) -> list[Path]:
    files = sorted((POC / "synthetic").glob("*.wav")) + sorted((POC / "cc0_kenney").glob("*.ogg"))
    files += sorted((POC / "degraded").glob("*.wav"))
    files += [env.LIBRARIES / "kenney" / rel for rel in (r for r, _ in KENNEY)]
    files += sorted((base_dir(run) / "sampler").glob("*.wav"))
    missing = [str(f) for f in files if not f.is_file()]
    if missing:
        raise FileNotFoundError("thiếu file đầu vào: " + ", ".join(missing))
    return files


# ---------------------------------------------------------------- step 2: recipe renders

def recipe_runs(run: str) -> list[tuple[str, str, Path, Path]]:
    """(game, id, recipe file, run dir)."""
    out = []
    for key in RECIPES:
        game, sid = key.split("/", 1)
        out.append((game, sid, LAB / "build" / "recipes" / f"{key}.json", env.WORK / game / sid / run))
    return out


def step_render(run: str) -> None:
    from build import render

    for game, sid, recipe, out in recipe_runs(run):
        spec = LAB / "specs" / game / f"{sid}.yaml"
        res = render.render(recipe, out=out, spec=spec if spec.is_file() else None)
        warn = "; ".join(res.report["warnings"]) or "—"
        _say(f"render {game}/{sid}: {res.report['count']} biến thể, mức id {res.report['idLevel']} LUFS-M, cảnh báo: {warn}")


# ---------------------------------------------------------------- step 3: critic (all layers)

def critic_out(run: str, name: str) -> Path:
    return base_dir(run) / f"critic-{name}"


def step_critic(run: str) -> None:
    from critic.__main__ import main as critic

    base = base_dir(run)
    rc = critic(["run", *map(str, raw_inputs(run)), "--spec", str(base / "cards.yaml"), "--stage", "raw",
                 "--layers", "all", "--out", str(critic_out(run, "raw")), "--seed", "20261023", "--blind-cards", "--quiet"])
    _say(f"critic raw: mã {rc}")
    for game in GAMES:
        runs = [r for r in recipe_runs(run) if r[0] == game]
        argv = ["run", *[str(r[3] / "masters") for r in runs], "--spec", str(LAB / "specs" / game),
                "--game", game, "--stage", "final", "--layers", "all", "--out", str(critic_out(run, game)),
                "--seed", "20261023", "--blind-cards", "--quiet"]
        for r in runs:
            argv += ["--sources", str(r[3] / "SOURCES.json")]
        rc = critic(argv)
        _say(f"critic {game}: mã {rc}")


# ---------------------------------------------------------------- step 4: ledger + staging

def staging_dirs(run: str, game: str) -> tuple[Path, Path]:
    """Batch-local release tree. Not ~/AudioLab/review/staging: nothing here is owner-approved yet."""
    root = base_dir(run) / "staging" / game
    return root / "art-src" / "audio", root / "public" / "assets" / game / "audio"


def step_link(run: str) -> int:
    from build import critic_link, licence_check, release

    for game, sid, _recipe, out in recipe_runs(run):
        res = critic_link.apply(out / "SOURCES.json", [critic_out(run, game)], out / "licences.rows.jsonl")
        _say(f"mark-ai {game}/{sid}: {res['steps']} bước, {res['files']} hồ sơ, mô hình {', '.join(res['models'])}")
        art, pub = staging_dirs(run, game)
        rel = release.release(out, None, art, pub)
        _say(f"release {game}/{sid} -> {art.parent.parent}: {len(rel['files'])} file, {rel['rowsAdded']} dòng sổ")
    worst = 0
    for game in GAMES:
        art, pub = staging_dirs(run, game)
        rc = licence_check.main(["--art-src", str(art), "--public", str(pub)])
        _say(f"licence-check {game}: mã {rc}")
        worst = max(worst, rc)
    return worst


# ---------------------------------------------------------------- step 5: batch 0a sessions

def _doc(out: Path, name: str) -> dict:
    return json.loads((out / f"{name}.json").read_text("utf-8"))


def _cand(out: Path, name: str, role: str) -> dict:
    from board import session

    doc = _doc(out, name)
    c = {"file": session.display_path(Path(doc["file"]["path"])), "role": role,
         "critic": session.display_path(out / f"{name}.json")}
    card = doc.get("card_blind") or doc.get("card")    # blind card for the board (§7)
    if card and (out / card).is_file():
        c["card"] = session.display_path(out / card)
    return c


def _listen_item(out: Path, gk: str, desc: str, all_cands: bool = False, item_id: str | None = None, **extra) -> dict:
    """One board item from a critic rank group.

    Default: the critic's listening list (§4.6 step 2: top, distinct, and a probe for ~30 % of ids).
    all_cands: every candidate that passed L1 (direction questions), roles from the list or "other"."""
    batch = json.loads((out / "_batch.json").read_text("utf-8"))
    entry = batch["listen"][gk]
    roles = {entry[r]: r for r in ("top", "distinct", "probe") if entry.get(r)}   # result stems
    if all_cands:
        docs = [json.loads(p.read_text("utf-8")) for p in sorted(out.glob("*.json")) if not p.name.startswith("_")]
        docs = [d for d in docs if (d.get("score") or {}).get("rank_group") == gk and d["verdict"] != "BLOCK"]
        stems = [d["file"]["stem"] for d in sorted(docs, key=lambda d: d["score"]["rank"] or 99)]
    else:
        stems = list(roles)
    cands = [_cand(out, s, roles.get(s, "other")) for s in stems]
    spec = _doc(out, stems[0])["spec"]
    item = {"id": item_id or spec.get("id") or gk.removeprefix("id:"), "family": spec.get("family") or "",
            "group": spec.get("group") or "", "desc": desc, "probe": "probe" in roles.values(), "candidates": cands}
    if spec.get("rate_hz") and not spec.get("loop"):
        item["loop"] = {"interval_ms": round(1000.0 / spec["rate_hz"])}
    item.update(extra)
    return item


class SessionExists(RuntimeError):
    pass


def _write_session(game: str, sid: str, title: str, items: list[dict], force: bool = False) -> Path:
    """Batch 0a sessions reveal cards only at the end (`reveal: end`): it is the first data of the
    owner's ear, and machine numbers shown between ids would steer the later ones (§4.6, §7)."""
    import hashlib

    folder = env.REVIEW / game / "sessions"
    path = folder / f"{sid}.json"
    if path.exists() and not force:
        raise SessionExists(f"{path} đã có; thêm --force để ghi đè (điểm đã chấm vẫn giữ trong ratings.jsonl)")
    folder.mkdir(parents=True, exist_ok=True)
    doc = {"schema": "audiolab.board.session/1", "session": sid, "game": game, "batch": "0a", "title": title,
           "seed": int(hashlib.sha256(f"{game}:{sid}".encode()).hexdigest()[:8], 16), "max_minutes": 20,
           "anchors": 0, "reveal": "end", "items": items}
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", "utf-8")
    return path


def step_session(run: str, force: bool = False) -> list[Path]:
    """Batch 0a (§12 phase 1): style-direction probes per game + the critic's disagreements.

    13 items in 4 sessions (§7: at most 10 ids per session), about 20 minutes in all. No anchor
    pairs yet: there are no earlier ratings to anchor on (§4.6 step 6). Every session reveals the
    cards at its end; calibration ids are neutral (calib-1...), the real name stays in source_id."""
    raw = critic_out(run, "raw")
    dh, td, ts = (critic_out(run, g) for g in GAMES)
    w = lambda *a: _write_session(*a, force=force)  # noqa: E731
    paths = [
        w("dragon-hold", "0a-dh", "Lô 0a · Rồng Giữ Ải · hướng âm", [
            _listen_item(dh, "id:fire.impact.a", "Cầu lửa trúng: phụt lửa trầm, thân tròn"),
            _listen_item(dh, "id:trap.pine-bomb.trigger", "Bom Hạt Thông nổ: nổ trầm, hạt văng"),
            _listen_item(dh, "id:wave.horn", "Tù và báo đợt: kèn và một tiếng trống khung. Các bản khác nhau ở "
                                             "loại kèn (kèn co, trombone, cả hai)", all_cands=True),
        ]),
        w("typing-survival", "0a-ts", "Lô 0a · Tuyến Cuối · hướng âm", [
            _listen_item(ts, "id:gun.xung", "Súng Xung: pháo tự động nặng, phát 5 lần mỗi giây"),
            _listen_item(ts, "id:hit.t1", "Đạn trúng bậc T1: tiếng keng ngắn trên vỏ thép"),
            _listen_item(ts, "id:hit.t2", "Chí mạng T2: keng nặng hơn, có cú thụi trầm"),
        ]),
        w("typing-defense", "0a-td", "Lô 0a · Lời Gọi · hướng âm và nguồn nhạc cụ", [
            _listen_item(td, "id:word-hit", "Gõ xong một từ: một nốt đàn tranh. Các bản khác nhau ở quãng tám và lối ngân",
                         all_cands=True, loop={"interval_ms": 1500}),
            _listen_item(td, "id:ui-pick", "Chọn một mục: phách gỗ rồi chuông đồng nhỏ. Các bản khác nhau ở nốt chuông",
                         all_cands=True),
            _listen_item(td, "id:ui-move", "Chuyển mục: chạm rất nhẹ lên thanh tre mỏng. Các bản khác nhau ở loại gỗ",
                         all_cands=True),
            _listen_item(td, "id:leak", "Quái lọt vào Lũy: cảnh báo, không còi. Cồng hội làng hay kẻng sắt?",
                         all_cands=True),
        ]),
        w("_calib", "0a-calib", "Lô 0a · Hiệu chỉnh: chỗ các lớp tai AI không đồng ý", [
            _listen_item(raw, "id:syn_punchy_impact", "Tiếng trúng nặng: bản nào chắc và sạch nhất?", all_cands=True,
                         item_id="calib-1", source_id="syn_punchy_impact"),
            _listen_item(raw, "id:kenney_impactBell_heavy_000", "Tiếng chuông kim loại bị gõ: bản nào hay nhất?",
                         all_cands=True, item_id="calib-2", source_id="kenney_impactBell_heavy_000"),
            _listen_item(raw, "id:kenney_laserLarge_000", "Tiếng súng laser: bản nào hay nhất?", all_cands=True,
                         item_id="calib-3", source_id="kenney_laserLarge_000"),
        ]),
    ]
    # The plan's full calibration set (§4.6 0a: 8 clean sounds x 3 degraded copies + 8 Kenney), with
    # this run's critic cards. Optional extra: its own batch label, so `--batch 0a` stays ~15 minutes.
    from board.calib import write_sessions as calib_sessions

    paths += calib_sessions(POC, env.REVIEW, env.WORK, critic_dir=raw, batch="0a-them", force=force)
    for p in paths:
        _say(f"phiên {p}")
    return paths


# ---------------------------------------------------------------- step 6: combined report

def _fmt(v, nd=2):
    return "–" if v is None else (f"{v:.{nd}f}".replace(".", ",") if isinstance(v, float) else str(v))


def step_report(run: str) -> Path:
    """REPORT.md: one table per critic run (verdict, ranks L2/L3, flags, CLAP/AST top label) plus the
    listening lists and the L2-vs-L3 disagreements. Numbers only; the reading of the cards is Claude's."""
    import collections

    base = base_dir(run)
    lines = [f"# Lô 0: báo cáo bộ phê bình ({run})", "",
             "Tự sinh bởi `common/batch0.py report`. Bảng chi tiết của từng lần chấm: `critic-*/summary.md`; "
             "thẻ ảnh: `critic-*/<tên>.png` (bản cho Bảng Nghe: `<tên>.blind.png`).", ""]
    for name in ("raw", *GAMES):
        out = critic_out(run, name)
        if not (out / "_batch.json").is_file():
            continue
        b = json.loads((out / "_batch.json").read_text("utf-8"))
        c = b["counts"]
        st = b.get("ask_stats") or {}
        n_el = st.get("n") or 0
        rates = "; ".join(f"`{k}` {v['files']}/{n_el} ({v['ask']} tính vào hỏi)" for k, v in (st.get("flags") or {}).items())
        lines += [f"## `critic-{name}` (giai đoạn `{b['stage']}`)", "",
                  f"{b['n_files']} file: {c['PASS']} đạt, {c['NEEDS_FIX']} cần sửa, {c['BLOCK']} bị chặn; "
                  f"chạy {_fmt(float(b['elapsed_s']), 1)} s.", "",
                  f"Hỏi chủ dự án: {st.get('ask_owner', 0)}/{n_el} file qua L1"
                  + (f" ({round(100 * st.get('ask_owner', 0) / n_el)} %)" if n_el else "") + ". Cờ theo loại: "
                  + (rates or "không có") + ".", "",
                  "| File | Kết luận | Hạng (L2/L3) | AES PQ | Kiểm L1 trượt | Cờ | CLAP #1 | AST #1 |",
                  "|---|---|---|---|---|---|---|---|"]
        groups = collections.defaultdict(list)
        for f in sorted(out.glob("*.json")):
            if f.name.startswith("_"):
                continue
            d = json.loads(f.read_text("utf-8"))
            s = d.get("score") or {}
            groups[s.get("rank_group")].append(d)
            l3 = (d.get("L3") or {}).get("scores") or {}
            l4 = d.get("L4") or {}
            clap = ((l4.get("clap") or {}).get("top3") or [[None]])[0][0]
            ast = ((l4.get("ast") or {}).get("top5") or [[None]])[0][0]
            fails = ", ".join(x["id"] for x in d["L1"]["checks"] if not x["ok"]) or "–"
            flags = ", ".join(x["id"] + ("" if x.get("ask", True) else "°") for x in d["flags"]) or "–"
            rank = f"{_fmt(s.get('rank'))} ({_fmt(s.get('rank_l2'))}/{_fmt(s.get('rank_l3'))})"
            lines.append(f"| `{d['file']['name']}` | {d['verdict']} | {rank} | {_fmt(l3.get('PQ'))} | {fails} | "
                         f"{flags} | {clap or '–'} | {ast or '–'} |")
        lines += ["", "° = cờ không tính vào “hỏi chủ dự án” (AST chưa hiệu chỉnh, hoặc cờ L4 mọi bản cùng id đều có).", "",
                  "Danh sách nghe (mục 4.6 bước 2) và chỗ L2, L3 chọn khác bản đứng đầu:", ""]
        for gk, entry in sorted(b["listen"].items()):
            el = [d for d in groups.get(gk, []) if d["verdict"] != "BLOCK"]
            if not el:
                continue
            t2 = min(el, key=lambda d: d["score"]["rank_l2"] or 99)["file"]["stem"]
            t3 = min(el, key=lambda d: d["score"]["rank_l3"] or 99)["file"]["stem"]
            note = f"; **L2 chọn {t2}, L3 chọn {t3}**" if len(el) > 1 and t2 != t3 else ""
            lines.append(f"- `{gk}`: đầu `{entry.get('top')}`, khác nhất `{entry.get('distinct') or '–'}`, "
                         f"dò `{entry.get('probe') or '–'}`{note}")
        lines.append("")
    path = base / "REPORT.md"
    path.write_text("\n".join(lines) + "\n", "utf-8")
    _say(f"báo cáo {path}")
    return path


# ---------------------------------------------------------------- CLI

STEPS = {"sampler": step_sampler, "render": step_render, "critic": step_critic, "link": step_link,
         "session": step_session, "report": step_report}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="batch0", description="Chạy trọn lô 0 của Audio Lab (giai đoạn 0–1).")
    ap.add_argument("step", choices=[*STEPS, "all"])
    ap.add_argument("--run", default=f"batch0-{dt.date.today().isoformat()}")
    ap.add_argument("--force", action="store_true", help="ghi đè file phiên đã có (điểm đã chấm vẫn giữ)")
    a = ap.parse_args(argv)
    env.apply()
    for name in (STEPS if a.step == "all" else [a.step]):
        _say(f"bước {name} ({a.run})")
        try:
            rc = STEPS[name](a.run, force=a.force) if name == "session" else STEPS[name](a.run)
        except SessionExists as e:
            _say(f"dừng: {e}")
            return 3
        if name == "link" and rc:          # licence check failed: stop before making sessions
            return rc
    return 0


if __name__ == "__main__":
    sys.exit(main())
