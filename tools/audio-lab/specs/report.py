"""Counts per game and category, and every place the catalog (code) and the sound list disagree."""
from __future__ import annotations

import datetime as dt
from collections import Counter

from . import taxonomy as tx
from .generate import GameResult
from .model import DISAGREE, INFO, PLAN, RANGE, STALE

SEVERITY_TITLES = [
    (DISAGREE, "Lệch giữa mã (catalog) và danh sách âm"),
    (PLAN, "Kế hoạch đề xuất khác tài liệu game (tài liệu game thắng)"),
    (STALE, "Bộ đọc cần kiểm lại"),
    (RANGE, "Ngoài khoảng xuất phát của §4.3.3 (chỉ để xếp hạng, không chặn)"),
    (INFO, "Ghi chú"),
]
GAME_ORDER = ["dragon-hold", "typing-defense", "typing-survival"]


def counts(results: list[GameResult]) -> dict:
    by_cat: dict[str, Counter] = {}
    by_fam: dict[str, Counter] = {}
    by_now: dict[str, Counter] = {}
    by_status: dict[str, Counter] = {}
    for r in results:
        cards = r.cards.values()
        by_cat[r.game] = Counter(str(c.get("category")) for c in cards)
        by_fam[r.game] = Counter(str(c.get("family")) for c in cards)
        by_now[r.game] = Counter("+".join((c.get("source_plan") or {}).get("now") or ["?"]) for c in cards)
        by_status[r.game] = Counter(str(c.get("status")) for c in cards)
    return {"category": by_cat, "family": by_fam, "source_now": by_now, "status": by_status}


def _table(title: str, rows: list[str], per_game: dict[str, Counter], games: list[str], label=lambda k: k) -> list[str]:
    out = [f"| {title} | " + " | ".join(games) + " | Tổng |", "|---|" + "---:|" * (len(games) + 1)]
    for k in rows:
        vals = [per_game[g].get(k, 0) for g in games]
        if sum(vals):
            out.append(f"| {label(k)} | " + " | ".join(str(v) for v in vals) + f" | {sum(vals)} |")
    tot = [sum(per_game[g].values()) for g in games]
    out.append("| **Tổng** | " + " | ".join(f"**{v}**" for v in tot) + f" | **{sum(tot)}** |")
    return out


def markdown(results: list[GameResult]) -> str:
    games = [r.game for r in sorted(results, key=lambda r: GAME_ORDER.index(r.game) if r.game in GAME_ORDER else 99)]
    c = counts(results)
    lines = [f"# Thẻ spec âm: số liệu và chỗ lệch ({dt.date.today().isoformat()})", ""]
    cat_rows = list(tx.CATEGORIES) + sorted({k for g in games for k in c["category"][g] if k not in tx.CATEGORIES})
    lines += ["## Số thẻ theo nhóm (§4.3.3)", ""]
    lines += _table("Nhóm", cat_rows, c["category"], games, lambda k: f"`{k}` {tx.CATEGORIES.get(k, {}).get('label', '(chưa phân loại)')}")
    lines += ["", "## Số thẻ theo họ (§4.6)", ""]
    lines += _table("Họ", list(tx.FAMILIES) + ["None"], c["family"], games, lambda k: f"`{k}` {tx.FAMILIES.get(k, '(chưa có họ)')}")
    now_rows = sorted({k for g in games for k in c["source_now"][g]})
    lines += ["", "## Nguồn làm ngay (khi chưa có mô hình)", ""]
    lines += _table("Nguồn", now_rows, c["source_now"], games, lambda k: f"`{k}`")
    lines += ["", "## Trạng thái", ""]
    lines += _table("Trạng thái", sorted({k for g in games for k in c["status"][g]}), c["status"], games, lambda k: f"`{k}`")

    for sev, title in SEVERITY_TITLES:
        block: list[str] = []
        for r in results:
            items = [i for i in r.issues if i.severity == sev]
            if not items:
                continue
            block += [f"### {r.data.label} (`{r.game}`): {len(items)}", ""]
            for i in sorted(items, key=lambda i: (i.kind, i.id or "")):
                who = f"`{i.id}`" if i.id else "(chung)"
                block.append(f"- {who} [{i.kind}] {i.detail}")
            block.append("")
        if block:
            ids = sorted({(i.game, i.id) for r in results for i in r.issues if i.severity == sev and i.id})
            lines += ["", f"## {title}", "", f"Số id có tên (cả ba game): {len(ids)}.", ""] + block
    orphans = [p for r in results for p in r.orphans]
    if orphans:
        lines += ["", "## Thẻ không còn id tương ứng (giữ lại, xem có cần xóa)", ""] + [f"- `{p.parent.name}/{p.name}`" for p in orphans]
    return "\n".join(lines).rstrip() + "\n"


def as_json(results: list[GameResult]) -> dict:
    c = counts(results)
    return {
        "date": dt.date.today().isoformat(),
        "counts": {k: {g: dict(v) for g, v in per.items()} for k, per in c.items()},
        "issues": [i.as_dict() for r in results for i in r.issues],
        "orphans": [str(p) for r in results for p in r.orphans],
    }
