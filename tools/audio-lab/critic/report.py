"""Outputs: <stem>.json per file (schema audiolab.critic.file/1), _batch.json, summary.md (Vietnamese)."""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

from .card import WORD, vn
from .groups import FAMILIES, GROUPS
from .thresholds import SCHEMA_BATCH, WEIGHTS


def default_out() -> Path:
    from common import env
    return env.WORK / "_critic" / dt.datetime.now().strftime("%Y%m%d-%H%M%S")


def check_out(out: Path) -> None:
    from common import env
    o = out.resolve()
    if env.GAMES.resolve() in o.parents or o == env.GAMES.resolve():
        raise SystemExit("không ghi vào games/** (chỉ đọc). Chọn thư mục trong ~/AudioLab/work")
    if env.REPO.resolve() in o.parents:
        print(f"audio-lab critic: cảnh báo: {o} nằm trong repo; JSON ở đó có thể bị đưa vào Git")


def unique_stem(stem: str, used: set[str]) -> str:
    s, k = stem, 2
    while s in used:
        s, k = f"{stem}__{k}", k + 1
    used.add(s)
    return s


def _jsonable(o):
    import numpy as np
    if isinstance(o, dict):
        return {str(k): _jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_jsonable(v) for v in o]
    if isinstance(o, (np.floating,)):
        v = float(o)
        return v if np.isfinite(v) else None
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    if isinstance(o, float) and o != o:
        return None
    if isinstance(o, float) and o in (float("inf"), float("-inf")):
        return None
    return o


def write(out: Path, results: list[dict], meta: dict) -> dict:
    files = []
    for r in results:
        js = out / f"{r['file']['stem']}.json"
        js.write_text(json.dumps(_jsonable(r), ensure_ascii=False, indent=1), encoding="utf-8")
        s = r.get("score") or {}
        files.append({
            "name": r["file"]["name"], "stem": r["file"]["stem"], "path": r["file"]["path"], "json": js.name,
            "png": r.get("card"), "png_blind": r.get("card_blind"), "verdict": r["verdict"],
            "group": r["spec"]["group"], "rank_group": s.get("rank_group"), "rank": s.get("rank"),
            "combined": s.get("combined"), "l2": (r.get("L2") or {}).get("score"),
            "ask_owner": r["ask_owner"]["value"], "read_card": r["read_card"],
            "flags": [f"{f['layer']}:{f['id']}" for f in r["flags"]],
            "blocking": (r.get("L1") or {}).get("blocking", []), "fixes": (r.get("L1") or {}).get("fixes", []),
            "sha256": r["file"]["sha256"], "ai_steps": [f"{x['step']}@{x['model']}" for x in r.get("ai_steps") or []],
        })
    counts = {k: sum(1 for f in files if f["verdict"] == k) for k in ("PASS", "NEEDS_FIX", "BLOCK", "UNGATED")}
    from .score import ask_stats
    batch = {"schema": SCHEMA_BATCH, **meta, "out_dir": str(out), "n_files": len(files), "counts": counts,
             "ask_stats": ask_stats(results), "files": files}
    (out / "_batch.json").write_text(json.dumps(_jsonable(batch), ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "summary.md").write_text(summary_md(results, batch), encoding="utf-8")
    return batch


def _pct(v):
    return "–" if v is None else vn(v * 100, 0, "%")


def _w(stage: str) -> str:
    w = WEIGHTS[stage]
    return " · ".join(f"{n} {vn(x, 2)}" for n, x in zip(("L2", "L3", "L4", "L5"), w))


def _ask_line(st: dict) -> str:
    """Rates that tell whether "ask the owner" still filters (§4.5): share asking, share per flag type."""
    n = st.get("n") or 0
    if not n:
        return "- Tỉ lệ hỏi chủ dự án: không có file nào qua L1."
    parts = [f"`{k}` {v['files']}/{n} file ({v['ask']} tính vào hỏi)" for k, v in (st.get("flags") or {}).items()]
    return (f"- Tỉ lệ hỏi chủ dự án: {st['ask_owner']}/{n} file qua L1 ({vn(100 * st['ask_owner'] / n, 0, '%')}). "
            "Cờ theo loại: " + ("; ".join(parts) if parts else "không có") + ". Cờ AST “thiếu nhãn mong đợi” và "
            "“khó nhận ra” không tính vào hỏi cho đến khi AST được hiệu chỉnh; cờ L4 chỉ tính khi nó tách được "
            "các bản trong cùng id.")


def summary_md(results: list[dict], batch: dict) -> str:
    c = batch["counts"]
    ask = sum(1 for r in results if r["ask_owner"]["value"])
    read = sum(1 for r in results if r["read_card"])
    models = batch.get("models") or {}
    log = models.get("log") or {}
    lines = [
        "# Tai AI: kết quả chấm", "",
        f"- Lúc chạy: {batch['created']}. Bộ chấm {batch['tool']['version']}, schema `{results[0]['schema']}`, "
        f"chạy trong {vn(batch['elapsed_s'], 1, 's')}.",
        f"- Cổng L1 ở giai đoạn `{batch['stage']}`: "
        + ("mọi lỗi vệ sinh đều chặn." if batch["stage"] == "final" else
           "chỉ clip chặn; lỗi khác thành việc sửa, sửa xong phải chạy lại với `--stage final`."),
        f"- Lớp đã yêu cầu: {', '.join(batch['layers'])}.",
        "- Hiệu chỉnh theo điểm chủ dự án (mục 4.6): "
        + (f"`{Path(batch['calibration']['path']).name}` (bản {batch['calibration']['version']}, "
           f"{batch['calibration'].get('date') or 'không ghi ngày'}); L1 không bị hiệu chỉnh."
           if batch.get("calibration") else "không dùng (trọng số mục 4.5 và mục tiêu mục 4.3.3 gốc)."),
    ]
    if log:
        parts = []
        for k, v in log.items():
            if isinstance(v, dict) and "load_s" in v:
                parts.append(f"{k} ({v.get('device')}, nạp {vn(v['load_s'], 1, 's')})")
        if parts:
            lines.append(f"- Mô hình đã nạp: {', '.join(parts)}.")
    lines += [
        "- Âm tham chiếu: " + (", ".join(f"`{k}` {v['n']} âm" for k, v in (batch.get("refs") or {}).items())
                               or "chưa có") + ".",
        f"- {batch['n_files']} file: {c['PASS']} đạt, {c['NEEDS_FIX']} cần sửa, {c['BLOCK']} bị chặn"
        + (f", {c['UNGATED']} chưa qua L1" if c["UNGATED"] else "") + f". {ask} file cần hỏi chủ dự án. "
        f"{read} thẻ ảnh Claude cần đọc.",
        _ask_line(batch.get("ask_stats") or {}), "",
        "Điểm tổng là tổng có trọng số của z-score trong cùng nhóm xếp hạng (mục 4.5). "
        "Điểm máy chỉ để xếp hạng; tai chủ dự án là cổng cuối.", "",
        "## Xếp hạng theo nhóm", "",
    ]
    groups: dict[str, list[dict]] = {}
    for r in results:
        groups.setdefault(r["score"]["rank_group"], []).append(r)
    for gk, rs in groups.items():
        sp = rs[0]["spec"]
        st = rs[0]["score"]["stage"]
        used = next((r["score"].get("weights_used") for r in rs if r["score"].get("weights_used")), None)
        wtxt = " · ".join(f"{k} {vn(v, 2)}" for k, v in used.items()) if used else _w(st)
        lines += [f"### `{gk}`: {GROUPS[sp['group']].name_vi}, họ {FAMILIES.get(sp['family'], sp['family'])}", "",
                  f"Giai đoạn trọng số `{st}`; trọng số đang dùng: {wtxt}.", "",
                  "| Hạng | File | Kết luận | Điểm tổng | L2 | AES PQ / CE | Cờ | Hỏi chủ dự án | Nhận xét |",
                  "|---|---|---|---|---|---|---|---|---|"]
        rs = sorted(rs, key=lambda r: (r["score"].get("rank") is None, r["score"].get("rank") or 0))
        for r in rs:
            s = r["score"]
            l3 = ((r.get("L3") or {}).get("scores")) or {}
            aes = f"{vn(l3.get('PQ'), 2)} / {vn(l3.get('CE'), 2)}" if l3 else "–"
            fl = ", ".join(f"{f['layer']} {f['id']}" + ("" if f.get("ask", True) else " (không hỏi)")
                           for f in r["flags"]) or "–"
            why = "; ".join(r["ask_owner"]["reasons"])[:160] if r["ask_owner"]["value"] else "không"
            note = "; ".join(r["notes_vi"])[:200] or "–"
            if r["verdict"] == "BLOCK":
                note = "bị chặn: " + ", ".join(r["L1"]["blocking"])
            lines.append(f"| {s.get('rank') or '–'} | `{r['file']['name']}` | {WORD.get(r['verdict'], r['verdict'])} | "
                         f"{vn(s.get('combined'), 2)} | {vn((r.get('L2') or {}).get('score'), 2)} | {aes} | {fl} | "
                         f"{why} | {note} |")
        lines.append("")
    blocked = [r for r in results if r["verdict"] == "BLOCK"]
    if blocked:
        lines += ["## Bị chặn ở L1", "", "| File | Nhóm | Kiểm trượt | Cách sửa theo kế hoạch |", "|---|---|---|---|"]
        for r in blocked:
            bad = [ch for ch in r["L1"]["checks"] if not ch["ok"]]
            lines.append(f"| `{r['file']['name']}` | {r['spec']['group']} | "
                         + "; ".join(f"{ch['label_vi']}: {ch['msg_vi'] or vn(ch['value'])}" for ch in bad)
                         + f" | {', '.join(sorted({ch['fix'] for ch in bad}))} |")
        lines.append("")
    fix = [r for r in results if r["verdict"] == "NEEDS_FIX"]
    if fix:
        lines += ["## Cần sửa trước khi chấm lại (`--stage final`)", "", "| File | Việc sửa |", "|---|---|"]
        for r in fix:
            lines.append(f"| `{r['file']['name']}` | {', '.join(r['L1']['fixes'])} |")
        lines.append("")
    listen = batch.get("listen") or {}
    if listen:
        lines += ["## Danh sách nghe đề xuất (mục 4.6 bước 2)", "",
                  "Chỉ cho Claude và Bảng Nghe. Bảng Nghe không được lộ vai trò của từng bản cho chủ dự án.", "",
                  "| Nhóm xếp hạng | Bản đứng đầu | Bản khác nhất | Bản dò |", "|---|---|---|---|"]
        for gk, e in listen.items():
            lines.append(f"| `{gk}` | {e['top'] or '–'} | {e['distinct'] or '–'} | {e['probe'] or '–'} |")
        lines.append("")
    no_ai = [r for r in results if not r["cloud_ok"]]
    if no_ai:
        lines += ["## Không đưa vào mô hình học máy (mục 10.2)", "", "| File | Lý do |", "|---|---|"]
        for r in no_ai:
            lines.append(f"| `{r['file']['name']}` | {r['ai_policy']['reason']} |")
        lines.append("")
    cards = [r["card"] for r in results if r["read_card"] and r.get("card")]
    if cards:
        lines += ["## Thẻ ảnh Claude cần đọc (top-6, bản dò, mọi ca bị cờ)", "", ", ".join(f"`{c}`" for c in cards), ""]
    lines += ["## Ghi chú", "",
              "- L1 dùng ngưỡng mục 4.3.1, đo trên file như đang lưu; các chỗ lệch có chủ ý (đỉnh phẳng gần đỉnh, file nén, "
              "DC thật, mối nối) ghi ở `tools/audio-lab/README.md`. Ngưỡng L1b và mục tiêu L2 là điểm xuất phát "
              "(mục 4.3.2, 4.3.3), chưa hiệu chỉnh bằng điểm của chủ dự án.",
              "- Bước nhảy ở mối nối tính phần vượt quá bước nhảy P95 bình thường trong file, để tiếng sáng không bị chặn nhầm.",
              "- Âm ngắn dưới 300 ms, và âm có thẻ bật `critic.loop_eval`, được L3–L5 chấm trên bản lặp 3–4 s "
              "theo nhịp của thẻ hoặc của nhóm (mục 4.4).",
              "- Không gửi thẻ ảnh của file có `cloud_ok: false` (nguồn `_no-ai`) cho AI chạy trên mây (mục 10.3).", ""]
    return "\n".join(lines)


def print_console(results: list[dict], out: Path) -> None:
    for r in sorted(results, key=lambda r: (r["score"]["rank_group"], r["score"].get("rank") or 999)):
        s = r["score"]
        rank = f"{s['rank']}/{s['n_ranked']}" if s.get("rank") else "–"
        fl = ",".join(f"{f['layer']}:{f['id']}" for f in r["flags"])
        why = ",".join((r.get("L1") or {}).get("failed") or [])
        print(f"{WORD.get(r['verdict'], r['verdict']):12s} {rank:>6s}  L2 {vn((r.get('L2') or {}).get('score'), 2):>5s}  "
              f"{r['file']['name']:40s} {why} {fl}")
    print(f"audio-lab critic: kết quả ở {out}")
