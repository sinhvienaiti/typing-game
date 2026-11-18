"""Lô 0a sessions (§4.6 step 1) from the 40-sound PoC fixtures in ~/AudioLab/work/_fixtures/poc40.

lo0a-1: 8 ids, each = one good sound + its clipped, muddy and thin copies (24 pairs).
lo0a-2: the 8 Kenney CC0 sounds alone (absolute stars and tags).
Cards and measurements: a critic output folder (--critic-dir, e.g. `run.sh critic ... --out DIR`
over the 40 fixtures) when given, else the newest PoC re-run (poc/rerun.sh) when present.
"""
from __future__ import annotations

import json
from pathlib import Path

GAME = "_calib"
# good source stem -> (Vietnamese description, family)
GOOD = {
    "kenney_explosionCrunch_000": ("Tiếng nổ giòn", "no"),
    "kenney_impactBell_heavy_000": ("Gõ chuông đồng", "trung"),
    "kenney_impactMetal_heavy_000": ("Va kim loại nặng", "trung"),
    "kenney_impactPunch_heavy_000": ("Cú đấm nặng", "trung"),
    "kenney_impactWood_heavy_000": ("Gõ gỗ hoặc tre nặng", "trung"),
    "kenney_laserLarge_000": ("Súng laser", "ban"),
    "syn_punchy_impact": ("Tiếng trúng có lực", "trung"),
    "syn_scifi_zap": ("Tiếng zap sci-fi", "ban"),
}
KENNEY_ONLY = {
    "kenney_impactGeneric_light_000": ("Va nhẹ", "phim-ui"),
    "kenney_spaceEngineLow_000": ("Động cơ trầm, vòng lặp", "nen"),
}


def _latest_poc_out(work: Path) -> Path | None:
    runs = sorted(p for p in (work / "_poc").glob("*/out") if (p / "analyze").is_dir())
    return runs[-1] if runs else None


def _with_qa(path: Path, qa_dir: Path | None) -> dict:
    c = {"file": str(path)}
    if qa_dir:   # the blind card (critic --blind-cards) first: no file name, verdict or score
        for key, ext in (("card", ".blind.png"), ("card", ".png"), ("critic", ".json")):
            q = qa_dir / (path.stem + ext)
            if key not in c and q.is_file():
                c[key] = str(q)
    return c


def write_sessions(fixtures: Path, review_root: Path, work: Path, seed: int = 20261023,
                   critic_dir: Path | None = None, batch: str = "0a", force: bool = False) -> list[Path]:
    """Two calibration sessions; cards open only at the end (`reveal: end`), and an existing
    session file is never replaced without force (the owner may be rating it)."""
    fixtures = Path(fixtures)
    if not (fixtures / "degraded").is_dir():
        raise FileNotFoundError(f"không thấy bộ âm thử ở {fixtures}")
    if critic_dir is not None:
        critic_dir = Path(critic_dir).expanduser().resolve()
        if not critic_dir.is_dir():
            raise FileNotFoundError(f"không thấy thư mục kết quả bộ phê bình {critic_dir}")
        qa_good = qa_bad = critic_dir
    else:
        poc = _latest_poc_out(Path(work))
        qa_good = poc / "analyze" if poc else None
        qa_bad = poc / "analyze_degraded" if poc and (poc / "analyze_degraded").is_dir() else None
    items1 = []
    for n, (stem, (desc, fam)) in enumerate(GOOD.items(), 1):
        folder = "cc0_kenney" if stem.startswith("kenney_") else "synthetic"
        ext = ".ogg" if folder == "cc0_kenney" else ".wav"
        good = fixtures / folder / (stem + ext)
        cands = [{**_with_qa(good, qa_good), "role": "good"}]
        for kind in ("clipped", "muddy", "thin"):
            bad = fixtures / "degraded" / f"{stem}__{kind}.wav"
            cands.append({**_with_qa(bad, qa_bad), "role": f"degraded:{kind}"})
        items1.append({"id": f"0a.{n:02d}", "key": f"0a-{n:02d}", "desc": desc, "family": fam,
                       "contexts": ["alone", "loop"], "candidates": cands})
    items2 = []
    singles = {**{k: v for k, v in GOOD.items() if k.startswith("kenney_")}, **KENNEY_ONLY}
    for n, (stem, (desc, fam)) in enumerate(sorted(singles.items()), 1):
        f = fixtures / "cc0_kenney" / (stem + ".ogg")
        items2.append({"id": f"0a.k{n}", "key": f"0a-k{n}", "desc": desc, "family": fam,
                       "contexts": ["alone", "small"], "candidates": [{**_with_qa(f, qa_good), "role": "reference"}]})
    out = []
    for sid, title, items in (("lo0a-1", "Lô 0a · phần 1: bản tốt và bản làm hỏng", items1),
                              ("lo0a-2", "Lô 0a · phần 2: 8 âm Kenney CC0", items2)):
        sess = {"schema": "audiolab.board.session/1", "session": sid, "game": GAME, "batch": batch,
                "title": title, "seed": seed, "max_minutes": 15, "anchors": 0, "reveal": "end", "items": items}
        p = Path(review_root) / GAME / "sessions" / f"{sid}.json"
        if p.exists() and not force:
            raise FileExistsError(f"{p} đã có; thêm --force để ghi đè (điểm đã chấm vẫn giữ trong ratings.jsonl)")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(sess, ensure_ascii=False, indent=1), "utf-8")
        out.append(p)
    return out
