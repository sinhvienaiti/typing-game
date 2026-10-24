"""Owner agreement (§4.6): how the critic's ranking matched the owner's blind Listening Board ratings,
before and after a calibration file (critic/calibration.py).

Inputs (read-only): ~/AudioLab/review/<game>/ratings.jsonl (append-only; the last line of an item wins),
the session file each rating names, and the critic JSON of every shown candidate. The whole critic
output folder of a candidate is re-scored, because z-scores and ranks depend on the rank group:
L2 is recomputed from the stored metrics with the calibrated targets, then score.combine runs with the
calibrated weights. L3 (audiobox) and L4 (CLAP/AST) values are stored model outputs and never change.

Measures, per rated item and summed:
- pairs: every pair of shown candidates the owner starred differently; the machine agrees when it
  orders them the same way (a machine tie counts one half);
- top: the machine's best shown candidate is the owner's pick (a k-way machine tie counts 1/k);
- pick rank: the machine's rank of the owner's pick in its whole rank group.

With a calibration it also splits the change into weights only and L2 targets only, and removes one
rule at a time (ablation), so every rule shows what it bought. All numbers are in-sample: the same
ratings chose the rules (§4.6 step 7 forbids any claim below 30 rated probes per family).
"""
from __future__ import annotations

import copy
import itertools
import json
import math
import statistics
from dataclasses import dataclass, field
from pathlib import Path

from . import calibration as C
from . import features, score
from .groups import FAMILIES
from .spec import from_json

BATCHES = ("0a", "0b")
SCORERS = ("combined", "L2", "L3", "L4")
SCORER_VI = {"combined": "Điểm tổng", "L2": "L2 đặc trưng", "L3": "L3 audiobox", "L4": "L4 CLAP/AST"}
ROLE_VI = {"top": "đứng đầu", "distinct": "khác nhất", "probe": "bản dò", "other": "khác (bản thêm)"}

# Features compared between the higher- and the lower-rated candidate of every pair (§4.6 task 1).
FEATURES = (
    ("attack_ms", "đầu tiếng: thời gian lên 10–90 %"),
    ("hf_attack_ms", "đầu tiếng: lớp tách ≥ 2 kHz lên"),
    ("crest_db", "crest (độ nảy)"),
    ("punch_db", "punch 20 ms đầu"),
    ("share_200_800", "thân 200–800 Hz"),
    ("mud_share", "dải đục 200–500 Hz"),
    ("share_below_150", "trầm dưới 150 Hz"),
    ("centroid_hz", "độ sáng: trọng tâm phổ"),
    ("share_above_3k", "độ sáng: phần trên 3 kHz"),
    ("flatness", "độ phẳng phổ (giống nhiễu)"),
    ("tail_ms", "đuôi"),
    ("stereo_correlation", "stereo: tương quan hai kênh (chỉ nền lặp)"),
    ("lufs_m_range_db", "kết cấu vòng: độ to dao động (chỉ nền lặp)"),
    ("loop_events", "kết cấu vòng: số dấu vòng lặp (chỉ nền lặp)"),
)
# Only meaningful for loops: on a one-shot the loudness range is just its decay, and stereo is rare.
LOOP_ONLY = {"stereo_correlation", "lufs_m_range_db", "loop_events"}


def resolve(p: str, home: Path) -> Path:
    return home / p[len("audiolab:"):] if p.startswith("audiolab:") else Path(p).expanduser()


@dataclass
class Cand:
    sha: str
    role: str
    stars: int | None
    pick: bool
    critic: Path
    stem: str = ""


@dataclass
class Item:
    game: str
    id: str
    batch: str
    session: str
    family: str
    group: str
    probe: bool
    note: str
    device: str | None
    contexts: list
    cands: list[Cand] = field(default_factory=list)

    @property
    def key(self) -> str:
        return f"{self.batch}:{self.id}"


def latest_ratings(review: Path, batches=BATCHES) -> list[dict]:
    """Last line per (game, session, item) of every ratings.jsonl (the file is append-only)."""
    rows: dict[tuple, dict] = {}
    for f in sorted(review.glob("*/ratings.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if not isinstance(d, dict) or d.get("kind") != "rating":
                continue
            if batches and d.get("batch") not in batches:
                continue
            rows[(d.get("game"), d.get("session"), d.get("item") or d.get("id"))] = d
    return sorted(rows.values(), key=lambda d: (str(d.get("batch")), str(d.get("ts"))))


def load_items(review: Path, home: Path, batches=BATCHES) -> list[Item]:
    items = []
    sessions: dict[Path, dict] = {}
    for d in latest_ratings(review, batches):
        sp = review / d["game"] / "sessions" / f"{d['session']}.json"
        if sp not in sessions:
            sessions[sp] = json.loads(sp.read_text(encoding="utf-8")) if sp.is_file() else {"items": []}
        sitem = next((i for i in sessions[sp]["items"] if i.get("id") == d["id"]), None)
        if sitem is None:
            continue
        by_file = {c["file"]: c for c in sitem.get("candidates") or [] if c.get("critic")}
        it = Item(d["game"], d["id"], d["batch"], d["session"], d.get("family") or sitem.get("family") or "khac",
                  d.get("group") or sitem.get("group") or "generic", bool(d.get("probe")), d.get("note") or "",
                  d.get("device"), list(d.get("contexts_heard") or []))
        for sha in d.get("shown") or []:
            f = (d.get("files") or {}).get(sha) or []
            c = by_file.get(f[0]) if f else None
            if c is None:
                continue
            it.cands.append(Cand(sha, (d.get("roles") or {}).get(sha) or c.get("role") or "?",
                                 (d.get("stars") or {}).get(sha), d.get("pick") == sha, resolve(c["critic"], home)))
        if len(it.cands) >= 2:
            items.append(it)
    return items


def _load_dir(d: Path) -> list[dict]:
    out = []
    for f in sorted(d.glob("*.json")):
        if f.name.startswith("_"):
            continue
        try:
            r = json.loads(f.read_text(encoding="utf-8"))
        except ValueError:
            continue
        if isinstance(r, dict) and str(r.get("schema", "")).startswith("audiolab.critic.file/"):
            r["_json"] = str(f)
            out.append(r)
    return out


def rescore(results: list[dict], cal) -> dict[str, dict]:
    """Copies of one critic output folder, L2 and combined score recomputed with `cal` (None = plan)."""
    rs = copy.deepcopy(results)
    for r in rs:
        l2 = r.get("L2")
        if not l2 or l2.get("score") is None or (r.get("refs") or {}).get("n"):
            continue          # no L2, or approved refs we cannot rebuild here: keep the stored L2
        new = features.l2_score(r["metrics"], from_json(r["spec"]), None, cal)
        r["L2"] = {**l2, **new}
    score.combine(rs, calibration=cal)
    return {r["_json"]: r for r in rs}


def value(r: dict, scorer: str) -> float | None:
    if r is None or r.get("verdict") == "BLOCK":
        return None
    if scorer == "combined":
        return (r.get("score") or {}).get("combined")
    return score._layer_value(r, scorer)


def feature(r: dict, f: str):
    if f in LOOP_ONLY and not (r.get("spec") or {}).get("loop"):
        return None
    m = r.get("metrics") or {}
    if f == "loop_events":
        sig = m.get("loop_signature") or {}
        return None if not sig.get("applies") else sum(int(sig.get(k) or 0) for k in ("knocks", "chirps", "bands"))
    v = m.get(f)
    return float(v) if isinstance(v, (int, float)) and math.isfinite(v) else None


def item_stats(it: Item, res: dict[str, dict], scorer: str) -> dict:
    vals = {c.sha: value(res.get(str(c.critic)), scorer) for c in it.cands}
    rated = [c for c in it.cands if c.stars is not None and vals[c.sha] is not None]
    agree, n = 0.0, 0
    for a, b in itertools.combinations(rated, 2):
        if a.stars == b.stars:
            continue
        n += 1
        dv = vals[a.sha] - vals[b.sha]
        agree += 0.5 if dv == 0 else float((dv > 0) == (a.stars > b.stars))
    top = None
    if rated:
        best = max(vals[c.sha] for c in rated)
        tied = [c for c in rated if vals[c.sha] == best]
        top = sum(c.pick for c in tied) / len(tied)
    pick = next((c for c in it.cands if c.pick), None)
    pr = res.get(str(pick.critic)) if pick else None
    return {"pairs_agree": agree, "pairs": n, "top_pick": top,
            "pick_rank": ((pr or {}).get("score") or {}).get("rank") if scorer == "combined" else None,
            "n_ranked": ((pr or {}).get("score") or {}).get("n_ranked") if scorer == "combined" else None,
            "values": {c.role: vals[c.sha] for c in it.cands}}


class _Scorer:
    """Loads every critic folder once; scores the rated items under any calibration."""

    def __init__(self, items: list[Item]):
        self.items = items
        self.dirs = sorted({c.critic.parent for it in items for c in it.cands})
        self.loaded = {d: _load_dir(d) for d in self.dirs}

    def results(self, cal) -> dict[str, dict]:
        res: dict[str, dict] = {}
        for d in self.dirs:
            res.update(rescore(self.loaded[d], cal))
        return res

    def stats(self, res: dict[str, dict]) -> dict:
        return {it.key: {s: item_stats(it, res, s) for s in SCORERS} for it in self.items}


def partial(cal, weights: bool = True, l2: bool = True, drop: str | None = None):
    """A copy of `cal` with only its weight rules, only its L2 rules, or without the rule `drop`."""
    keep = (lambda r: r["id"] != drop)
    return C.Calibration(version=f"{cal.version}{'' if weights and l2 else '-w' if weights else '-l2'}"
                                 f"{'-' + drop if drop else ''}",
                         path=cal.path, date=cal.date,
                         weight_rules=[r for r in cal.weight_rules if keep(r)] if weights else [],
                         l2_rules=[r for r in cal.l2_rules if keep(r)] if l2 else [], doc=cal.doc)


def run(items: list[Item], cal, contributions: bool = True) -> dict:
    """{"before"|"after": {item key: {scorer: stats}}, "results": {"before"|"after": {json: result}},
    "contrib": {"weights"|"l2": stats}, "ablation": {rule id: stats}, "stored_check": {...}}."""
    sc = _Scorer(items)
    out = {"results": {}, "before": {}, "after": {}, "contrib": {}, "ablation": {}}
    for tag, c in (("before", None), ("after", cal)):
        if tag == "after" and cal is None:
            continue
        out["results"][tag] = sc.results(c)
        out[tag] = sc.stats(out["results"][tag])
    if cal is not None and contributions:
        out["contrib"] = {"weights": sc.stats(sc.results(partial(cal, l2=False))),
                          "l2": sc.stats(sc.results(partial(cal, weights=False)))}
        for r in cal.weight_rules + cal.l2_rules:
            out["ablation"][r["id"]] = sc.stats(sc.results(partial(cal, drop=r["id"])))
    # stored scores (as the session was built) vs recomputed without calibration: same code -> same ranks
    stored = {r["_json"]: r for d in sc.dirs for r in sc.loaded[d]}
    same = sum(1 for it in items for c in it.cands
               if (stored.get(str(c.critic)) or {}).get("score", {}).get("rank")
               == (out["results"]["before"].get(str(c.critic)) or {}).get("score", {}).get("rank"))
    out["stored_check"] = {"same_rank": same, "n": sum(len(it.cands) for it in items)}
    return out


def _sum(stats: dict, keys, scorer: str) -> dict:
    a = sum(stats[k][scorer]["pairs_agree"] for k in keys)
    n = sum(stats[k][scorer]["pairs"] for k in keys)
    tops = [stats[k][scorer]["top_pick"] for k in keys if stats[k][scorer]["top_pick"] is not None]
    return {"agree": a, "n": n, "top": sum(tops), "n_top": len(tops)}


def role_of(c: Cand) -> str:
    return "top" if c.role.endswith("top") else "distinct" if c.role.endswith("distinct") else \
        "probe" if c.role == "probe" else "other"


def roles(items: list[Item]) -> dict:
    pick: dict[str, int] = {}
    stars: dict[str, list] = {}
    for it in items:
        for c in it.cands:
            r = role_of(c)
            if c.stars is not None:
                stars.setdefault(r, []).append(c.stars)
            if c.pick:
                pick[r] = pick.get(r, 0) + 1
    probes = [it for it in items if any(c.role == "probe" for c in it.cands)]
    probe_won = sum(1 for it in probes if any(c.role == "probe" and c.pick for c in it.cands))
    return {"pick": pick, "stars": {k: statistics.mean(v) for k, v in stars.items()}, "n": len(items),
            "probe_items": len(probes), "probe_picked": probe_won}


def roles_by_family(items: list[Item]) -> dict[str, dict]:
    """Per family: which role the owner picked (top / distinct / probe / other)."""
    out: dict[str, dict] = {}
    for it in items:
        e = out.setdefault(it.family, {"n": 0, "pick": {}, "probe_items": 0, "probe_picked": 0})
        e["n"] += 1
        p = next((c for c in it.cands if c.pick), None)
        if p is not None:
            r = role_of(p)
            e["pick"][r] = e["pick"].get(r, 0) + 1
        if any(c.role == "probe" for c in it.cands):
            e["probe_items"] += 1
            e["probe_picked"] += int(p is not None and p.role == "probe")
    return out


def separation(items: list[Item], results: dict[str, dict]) -> dict:
    """Per family and overall: in how many differently-starred pairs the better one has the larger value."""
    out: dict[str, dict[str, list]] = {}
    for it in items:
        rs = [(c, results.get(str(c.critic))) for c in it.cands if c.stars is not None]
        for (a, ra), (b, rb) in itertools.combinations(rs, 2):
            if a.stars == b.stars or ra is None or rb is None:
                continue
            hi, lo = (ra, rb) if a.stars > b.stars else (rb, ra)
            for f, _ in FEATURES:
                x, y = feature(hi, f), feature(lo, f)
                if x is None or y is None or x == y:
                    continue
                for fam in ("*", it.family):
                    e = out.setdefault(fam, {}).setdefault(f, [0, 0])
                    e[0] += x > y
                    e[1] += 1
    return out


# ------------------------------------------------------------------ report (Vietnamese)
def _num(x: float) -> str:
    return (f"{x:.2f}".rstrip("0").rstrip(".") if x != int(x) else str(int(x))).replace(".", ",")


def _pct(a: float, n: int) -> str:
    if not n:
        return "–"
    return f"{_num(a)}/{n} ({100 * a / n:.0f} %)"


def _rule_vi(r: dict) -> str:
    return r.get("why_vi") or r.get("id")


def report_md(items: list[Item], data: dict, cal) -> str:
    keys = [it.key for it in items]
    have_after = cal is not None and bool(data.get("after"))
    fams = sorted({it.family for it in items})
    rl = roles(items)
    L = ["# So tai chủ dự án với tai AI (mục 4.6)", ""]
    L.append(f"- Dữ liệu: {len(items)} id đã chấm mù ở lô {', '.join(sorted({it.batch for it in items}))}, "
             f"{sum(len(it.cands) for it in items)} bản; thiết bị nghe: "
             f"{', '.join(sorted({it.device or '?' for it in items}))}.")
    L.append("- Hiệu chỉnh so sánh: " + (f"`{Path(cal.path).name if cal.path else cal.version}` (bản {cal.version})"
                                         if have_after else "không"))
    sc = data["stored_check"]
    L.append(f"- Kiểm: tính lại không hiệu chỉnh cho đúng hạng đã lưu ở {sc['same_rank']}/{sc['n']} bản được nghe.")
    L.append(f"- Bản dò: có ở {rl['probe_items']} id; chủ dự án chọn bản dò ở {rl['probe_picked']}/{rl['probe_items']} id.")
    L += ["", "## Bản được chọn theo vai trò", "", "| Vai trò | Số lần được chọn | Sao trung bình |", "|---|---|---|"]
    for r in ("top", "distinct", "probe", "other"):
        if r in rl["stars"]:
            L.append(f"| {ROLE_VI[r]} | {rl['pick'].get(r, 0)}/{rl['n']} | {rl['stars'][r]:.2f} |".replace(".", ","))
    rf = roles_by_family(items)
    L += ["", "Theo họ âm (bản chủ dự án chọn là bản nào của máy):", "",
          "| Họ | Id | Đứng đầu | Khác nhất | Bản dò | Khác | Chọn bản dò / id có bản dò |",
          "|---|---|---|---|---|---|---|"]
    for fam in fams:
        e = rf[fam]
        L.append(f"| {FAMILIES.get(fam, fam)} | {e['n']} | " + " | ".join(str(e["pick"].get(r, 0)) for r in
                 ("top", "distinct", "probe", "other")) + f" | {e['probe_picked']}/{e['probe_items']} |")
    L += ["", "## Mức khớp theo lớp", "",
          "Cặp: mọi cặp bản chủ dự án cho số sao khác nhau; máy khớp khi xếp cặp đó cùng chiều (hòa tính nửa). "
          "Đầu: bản máy xếp cao nhất trong các bản được nghe chính là bản chủ dự án chọn. Đoán ngẫu nhiên: "
          "khoảng 50 % số cặp.", ""]
    hdr = "| Lớp | Cặp khớp, trước | Đầu khớp, trước |" + (" Cặp khớp, sau | Đầu khớp, sau |" if have_after else "")
    L += [hdr, "|---|---|---|" + ("---|---|" if have_after else "")]
    for s in SCORERS:
        b = _sum(data["before"], keys, s)
        row = f"| {SCORER_VI[s]} | {_pct(b['agree'], b['n'])} | {_pct(b['top'], b['n_top'])} |"
        if have_after:
            a = _sum(data["after"], keys, s)
            row += f" {_pct(a['agree'], a['n'])} | {_pct(a['top'], a['n_top'])} |"
        L.append(row)
    L += ["", "## Mức khớp theo họ âm (cặp khớp)", "",
          "| Họ | Id | " + " | ".join(f"{SCORER_VI[s]}, trước" for s in SCORERS)
          + (" | Điểm tổng, sau | L2, sau" if have_after else "") + " |",
          "|---|---|" + "---|" * (len(SCORERS) + (2 if have_after else 0))]
    for fam in fams:
        ks = [it.key for it in items if it.family == fam]
        row = f"| {FAMILIES.get(fam, fam)} | {len(ks)} | " + " | ".join(
            _pct(_sum(data["before"], ks, s)["agree"], _sum(data["before"], ks, s)["n"]) for s in SCORERS)
        if have_after:
            row += " | " + " | ".join(_pct(_sum(data["after"], ks, s)["agree"], _sum(data["after"], ks, s)["n"])
                                      for s in ("combined", "L2"))
        L.append(row + " |")
    if have_after and data.get("contrib"):
        L += ["", "## Mỗi phần của bản hiệu chỉnh mua được gì (điểm tổng)", "",
              "| Cấu hình | Cặp khớp | Đầu khớp |", "|---|---|---|"]
        b = _sum(data["before"], keys, "combined")
        L.append(f"| Kế hoạch (không hiệu chỉnh) | {_pct(b['agree'], b['n'])} | {_pct(b['top'], b['n_top'])} |")
        for tag, vi in (("weights", "Chỉ trọng số lớp"), ("l2", "Chỉ mục tiêu L2")):
            s = _sum(data["contrib"][tag], keys, "combined")
            L.append(f"| {vi} | {_pct(s['agree'], s['n'])} | {_pct(s['top'], s['n_top'])} |")
        a = _sum(data["after"], keys, "combined")
        L.append(f"| Cả hai (bản {cal.version}) | {_pct(a['agree'], a['n'])} | {_pct(a['top'], a['n_top'])} |")
        L += ["", "Bỏ từng luật (điểm tổng, cặp khớp và đầu khớp khi thiếu luật đó; các id đổi kết quả):", "",
              "| Luật | Thiếu luật này | Id bị ảnh hưởng | Vì sao có luật |", "|---|---|---|---|"]
        for r in cal.weight_rules + cal.l2_rules:
            st = data["ablation"].get(r["id"])
            if st is None:
                continue
            s = _sum(st, keys, "combined")
            hit = [k for k in keys if (st[k]["combined"]["pairs_agree"], st[k]["combined"]["top_pick"])
                   != (data["after"][k]["combined"]["pairs_agree"], data["after"][k]["combined"]["top_pick"])]
            L.append(f"| `{r['id']}` | {_pct(s['agree'], s['n'])}; đầu {_pct(s['top'], s['n_top'])} | "
                     f"{', '.join(f'`{k}`' for k in hit) or 'không đổi cặp nào'} | {_rule_vi(r)} |")
    L += ["", "## Từng id", "", "| Lô | Id | Họ | Sao theo vai trò | Cặp khớp, trước"
          + (" | sau" if have_after else "") + " | Hạng máy của bản được chọn, trước"
          + (" | sau" if have_after else "") + " |",
          "|---|---|---|---|---|---|" + ("---|---|" if have_after else "")]
    for it in items:
        st = ", ".join(f"{c.role} {c.stars}{'*' if c.pick else ''}" for c in it.cands)
        b = data["before"][it.key]["combined"]
        a = data["after"][it.key]["combined"] if have_after else None
        row = f"| {it.batch} | `{it.id}` | {it.family} | {st} | {_num(b['pairs_agree'])}/{b['pairs']} |"
        if a:
            row += f" {_num(a['pairs_agree'])}/{a['pairs']} |"
        row += f" {b['pick_rank']}/{b['n_ranked']} |"
        if a:
            row += f" {a['pick_rank']}/{a['n_ranked']} |"
        L.append(row)
    sep = separation(items, data["results"]["before"])
    fam_cols = sorted(k for k in sep if k != "*")
    L += ["", "## Đặc trưng tách bản được chấm cao", "",
          "Trong mỗi cặp sao khác nhau: bản được chấm cao có giá trị lớn hơn ở bao nhiêu cặp. "
          "Gần 100 % hoặc gần 0 % là hướng nhất quán; quanh 50 % là không tách.", "",
          "| Đặc trưng | Mọi họ | " + " | ".join(FAMILIES.get(f, f) for f in fam_cols) + " |",
          "|---|---|" + "---|" * len(fam_cols)]
    for f, vi in FEATURES:
        cells = []
        for fam in ["*"] + fam_cols:
            e = sep.get(fam, {}).get(f)
            cells.append(_pct(e[0], e[1]) if e else "–")
        L.append(f"| {vi} | " + " | ".join(cells) + " |")
    probes = rl["probe_items"]
    L += ["", f"Ghi chú: số cặp nhỏ ({len(items)} id, {_sum(data['before'], keys, 'combined')['n']} cặp, "
          f"{probes} id có bản dò). Số “sau” đo trên chính dữ liệu đã dùng để chọn luật, nên lạc quan; "
          "mục 4.6 bước 7 không cho tuyên bố gì khi một họ có dưới 30 bản dò đã chấm. Phép thử thật là điểm "
          "của lô sau, chấm với bản hiệu chỉnh này đã bật.", ""]
    return "\n".join(L)


def summary(items: list[Item], data: dict, cal) -> dict:
    keys = [it.key for it in items]
    fams = sorted({it.family for it in items})
    out = {"items": len(items), "roles": roles(items), "roles_by_family": roles_by_family(items),
           "stored_check": data["stored_check"], "calibration": cal.to_json() if cal else None,
           "by_scorer": {}, "by_family": {}, "per_item": {}, "contrib": {}, "ablation": {}}
    for tag in ("before", "after"):
        if not data.get(tag):
            continue
        out["by_scorer"][tag] = {s: _sum(data[tag], keys, s) for s in SCORERS}
        out["by_family"][tag] = {fam: {s: _sum(data[tag], [it.key for it in items if it.family == fam], s)
                                       for s in SCORERS} for fam in fams}
    for tag, st in (data.get("contrib") or {}).items():
        out["contrib"][tag] = {s: _sum(st, keys, s) for s in SCORERS}
    for rid, st in (data.get("ablation") or {}).items():
        out["ablation"][rid] = {s: _sum(st, keys, s) for s in SCORERS}
    for it in items:
        out["per_item"][it.key] = {tag: {s: dict(data[tag][it.key][s]) for s in SCORERS}
                                   for tag in ("before", "after") if data.get(tag)}
    out["separation"] = separation(items, data["results"]["before"])
    return out


def main(a) -> int:
    from common import env
    review = Path(a.review).expanduser() if a.review else env.REVIEW
    items = load_items(review, env.HOME, tuple(a.batch) if a.batch else BATCHES)
    if not items:
        print("audio-lab critic: chưa có điểm chấm nào khớp phiên và kết quả bộ chấm")
        return 1
    targets = [Path(p).expanduser() for p in (a.md, a.json) if p]
    if any(env.GAMES.resolve() in p.resolve().parents for p in targets):
        print("audio-lab critic: không ghi vào games/**")
        return 2
    cal = C.load(a.calibration)
    data = run(items, cal)
    md = report_md(items, data, cal)
    print(md)
    for path, text in ((a.md, md), (a.json, None)):
        if not path:
            continue
        p = Path(path).expanduser()
        p.parent.mkdir(parents=True, exist_ok=True)
        if text is None:
            p.write_text(json.dumps(summary(items, data, cal), ensure_ascii=False, indent=1), encoding="utf-8")
        else:
            p.write_text(text, encoding="utf-8")
    return 0
