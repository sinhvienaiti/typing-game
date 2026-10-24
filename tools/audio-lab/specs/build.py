"""Turn reader entries into spec cards (plain dicts, key order = YAML order)."""
from __future__ import annotations

import math
import re
from pathlib import Path

from . import parse
from . import taxonomy as tx
from .model import PLAN, RANGE, Entry, GameData, Issue
from .readers.plan import variant_range

SCHEMA_VERSION = 1


def _db(gain: float | None) -> float | None:
    if gain is None or gain <= 0:
        return None
    return round(20 * math.log10(gain), 2)


def _dedupe(items: list) -> list:
    out = []
    for x in items:
        if x not in out:
            out.append(x)
    return out


def _num(x: float | None) -> float | int | None:
    if x is None:
        return None
    x = round(float(x), 3)
    return int(x) if x == int(x) else x


def _caps(e: Entry) -> dict:
    caps = dict(parse.parse_caps(e.listing.get("when", "")))
    m = re.search(r"(\d+)\s*viên/s, tiếng phát cho một nửa", e.listing.get("when", ""))
    if m:
        caps["per_s"] = int(m.group(1)) / 2
    for k, v in (e.code.get("caps") or {}).items():
        if k == "alerts_per_s":
            caps["shared_per_s"] = v
        else:
            caps.setdefault(k, v)
    return {k: _num(v) for k, v in sorted(caps.items())}


def _duration(gd: GameData, e: Entry, category: str | None, loop: bool) -> tuple[dict, list[Issue]]:
    cat = tx.CATEGORIES.get(category or "", {})
    issues: list[Issue] = []
    prompt = e.listing.get("prompt") or ""
    d = {"target_ms": None, "tolerance_pct": 20, "tolerance_ms": None, "min_ms": None, "max_ms": None,
         "basis": None, "category_range_ms": cat.get("duration_ms"), "music": None}
    if category == "music":
        mu = gd.context.get("music", {})
        bars = parse.parse_bars(prompt) or {}
        bpm = e.code.get("bpm") or bars.get("bpm") or mu.get("bpm")
        n = e.code.get("bars") or bars.get("bars") or mu.get("bars")
        if bpm and n:
            target = parse.bars_ms(bpm, n, mu.get("beats_per_bar", 4))
            d.update(target_ms=_num(target), tolerance_pct=None, tolerance_ms=1, min_ms=_num(target - 1), max_ms=_num(target + 1),
                     basis="Đúng số ô nhịp, lệch không quá 1 ms (§4.3.1); BPM và số ô nhịp theo mã và prompt",
                     music={"bpm": _num(bpm), "bars": int(n), "beats_per_bar": mu.get("beats_per_bar", 4), "key": mu.get("key")})
        return d, issues
    target, basis, lo, hi = None, None, None, None
    if e.code.get("length_ms"):
        target, basis = e.code["length_ms"], f"{gd.files['catalog']} lengthMs (nguồn chuẩn của độ dài)"
    else:
        pd = parse.parse_duration(prompt)
        if pd:
            target = pd["ms"]
            basis = f"Prompt trong {gd.files['list']}"
            if pd["kind"] == "max":
                basis += f" (trần: dưới {pd['ms']:g} ms)"
                hi = pd["ms"]
            elif pd["kind"] == "range":
                lo, hi = pd["min_ms"], pd["max_ms"]
    if target is not None:
        explicit = lo is not None or hi is not None    # "under X ms" or "2–5 s" in the prompt
        if not explicit:
            lo, hi = target * 0.8, target * 1.2
        d.update(target_ms=_num(target), min_ms=_num(lo), max_ms=_num(hi), basis=basis, tolerance_pct=None if explicit else 20)
        rng = cat.get("duration_ms")
        if rng and not loop and not (rng[0] <= target <= rng[1]):
            issues.append(Issue(gd.game, e.id, "category-range",
                                f"Dài {target:g} ms, ngoài khoảng {rng[0]}–{rng[1]} ms của nhóm \"{cat['label']}\" (§4.3.3, chỉ để xếp hạng)",
                                RANGE, target, rng))
    return d, issues


def _onset(gd: GameData, rule: dict, category: str | None, loop: bool, family: str | None = None) -> dict:
    cat = tx.CATEGORIES.get(category or "", {})
    cls = rule.get("onset") or ("loop" if loop else cat.get("onset", "other"))
    if cls == "other" and category == "fx-other" and family in tx.IMPACT_FAMILIES:
        cls = "impact"           # a miscellaneous hit, shot or blast is still timed (§4.3.1)
    oc = tx.ONSET_CLASSES[cls]
    rise, lead = oc["rise_max_ms"], oc["lead_silence_max_ms"]
    basis = [tx.ONSET_BASIS]
    caps = gd.context.get("onset_cap_ms", {})
    cap = caps.get("all", caps.get(cls))
    if cap is not None and lead is not None:
        basis.append(gd.context["onset_basis"])
        lead = min(lead, cap)
    return {"class": cls, "rise_max_ms": rise, "lead_silence_max_ms": lead, "basis": "; ".join(basis)}


def _variants(gd: GameData, e: Entry, rule: dict, category: str | None, plan: dict) -> tuple[dict, list[Issue]]:
    issues: list[Issue] = []
    cat = tx.CATEGORIES.get(category or "", {})
    lo, hi = (cat.get("variants") or [1, 1])
    basis = f"{tx.CATEGORY_BASIS} ({cat.get('label', 'chưa phân loại')})"
    if rule.get("variants"):
        lo, hi, basis = rule["variants"]["min"], rule["variants"]["max"], rule["variants"]["basis"]
    game_rule = None
    for g in gd.context.get("variants", []):
        if e.id in g.get("ids", []) or category in g.get("categories", []):
            game_rule = g
    if game_rule:
        lo, hi, basis = game_rule["min"], game_rule["max"], game_rule["basis"]
    stated = parse.parse_variant_count(e.listing.get("prompt") or "")
    if stated:
        lo = hi = stated
        basis = f"Prompt trong {gd.files['list']}: {stated} biến thể"
        game_rule = {"min": stated, "max": stated}
    target = lo
    b1 = plan["batch1"].get((gd.game, e.id))
    if b1:
        vr = variant_range(b1["variants"])
        if vr:
            want = vr[1]
            if game_rule and not (game_rule["min"] <= want <= game_rule["max"]):
                issues.append(Issue(gd.game, e.id, "plan-variants",
                                    f"§9 #{b1['n']} ghi {b1['variants']} biến thể, tài liệu game ghi {game_rule['min']}–{game_rule['max']}: tài liệu game thắng",
                                    PLAN, [game_rule["min"], game_rule["max"]], b1["variants"]))
                target = max(game_rule["min"], min(want, game_rule["max"]))
            else:
                target = want
                lo, hi = min(lo, vr[0]), max(hi, vr[1])
                basis += f"; §9 #{b1['n']}: {b1['variants']}"
    return {"target": target, "min": lo, "max": hi, "basis": basis}, issues


def _bands(gd: GameData, rule: dict, category: str | None, source: str | None) -> dict:
    cat = tx.CATEGORIES.get(category or "", {})
    bands = rule.get("bands") or cat.get("bands") or tx.BANDS_BY_SOURCE.get(source or "", [])
    bands = _dedupe(list(bands) + list(rule.get("add_bands", [])))
    roles = gd.context.get("freq_roles", {})
    vb = rule.get("voice_band") or cat.get("voice_band", "free")
    return {
        "bands": [{"band": b, "range_hz": tx.BANDS[b]["range_hz"], "role": roles.get(b)} for b in bands],
        "voice_band": vb,
        "voice_band_text": tx.VOICE_BAND_RULES[vb],
        "spectrum": cat.get("spectrum"),
        "basis": tx.FREQ_BASIS + ", " + tx.CATEGORY_BASIS,
    }


def _loudness(gd: GameData, e: Entry, rule: dict, category: str | None, bus: str | None) -> dict:
    cat = tx.CATEGORIES.get(category or "", {})
    lo = gd.context["loudness"]
    if category == "music":
        file, proposal = lo.get("music"), None
    elif category == "ambience":
        file, proposal = lo.get("ambience") or lo.get("short"), None
    else:
        file = lo["short"]
        proposal = {"metric": "lufs-m-max", "target": -20, "pad_s": 0.4, "true_peak_max_dbtp": -1,
                    "basis": "AUDIO_PIPELINE §4.3.3, §5.1 bước 4: đề xuất chuẩn hóa mọi âm ngắn về một mức chung; tài liệu game đang ghi chuẩn hóa đỉnh"}
    gain = gd.context.get("bus_gain", {}).get(bus) if bus else None
    gain_db = e.code.get("gain_db")
    pg = gd.context.get("per_id_gain") or {}
    gain_basis = pg.get("basis") if e.in_code else None
    if gain_db is None and e.in_code and pg.get("default_db") is not None and category != "music":
        gain_db = pg["default_db"]
    mix = cat.get("mix") or {}
    rng = mix.get("heavy_range") if rule.get("weight") == "heavy" and mix.get("heavy_range") else mix.get("range")
    bus_db = _db(gain)
    return {
        "file": dict(file) if file else None,
        "proposal": proposal,
        "bus": bus,
        "bus_gain": gain,
        "bus_gain_db": bus_db,
        "gain_db": _num(gain_db),
        "gain_basis": gain_basis if gain_db is not None else None,
        # Level of the normalised file after its own gain and the bus (before master): gain_db + bus_gain_db.
        "relative_db": _num(gain_db + bus_db) if gain_db is not None and bus_db is not None else None,
        "pronunciation_duck_db": gd.context.get("duck_db", {}).get(bus) if bus else None,
        "mix_target": {"metric": mix.get("metric"), "range": rng, "text": mix.get("text"),
                       "weight": rule.get("weight"), "basis": tx.CATEGORY_BASIS + " (mức trong bản trộn, bài A và B)"} if mix else None,
    }


def _pitches(gd: GameData, e: Entry, rule: dict) -> dict | None:
    prompt = e.listing.get("prompt") or ""
    notes = parse.parse_pitches(prompt)
    out: dict | None = None
    if notes:
        m = re.search(r"(\d+)\s+pitches", prompt)
        sc = re.search(r"\b([A-G](?:#|b)?\d?\s+(?:major\s+|minor\s+)?pentatonic(?:\s+upward)?)", prompt)
        out = {"notes": notes, "count": int(m.group(1)) if m else len(notes), "scale": sc.group(1) if sc else None,
               "basis": f"Prompt trong {gd.files['list']}", "proposal": None}
    if rule.get("pitches"):
        p = rule["pitches"]
        out = {"notes": p.get("notes", []), "count": p.get("count", len(p.get("notes", [])) or None), "scale": p.get("scale"),
               "basis": p["basis"], "proposal": None}
    if rule.get("pitch_proposal") and out is not None:
        out["proposal"] = dict(rule["pitch_proposal"])
    return out


def _source_plan(gd: GameData, e: Entry, rule: dict, source: str | None, plan: dict) -> dict:
    sc = tx.SOURCE_CLASSES.get(source or "", {"ranked": [], "now": [], "later": [], "note": None})
    ov = rule.get("source_override") or {}
    ranked = ov.get("ranked", sc["ranked"])
    now = list(ov.get("now", sc["now"]))
    later = list(ov.get("later", sc["later"]))
    later_needs = (["buoc-0"] if "model-later" in later else []) + (["chu-du-an-ghi-am"] if "owner-recording" in later else [])
    b1 = plan["batch1"].get((gd.game, e.id))
    return {
        "now": now,
        "later": later,
        "ranked": [{"rank": i + 1, "kinds": list(kinds), "detail": detail} for i, (kinds, detail) in enumerate(ranked)],
        "needs_now": list(sc.get("needs_now", [])) if "source_override" not in rule else [],
        "needs_later": later_needs,
        "note": ov.get("note") if ov else sc.get("note"),
        "batch1": {"n": b1["n"], "why": b1["why"], "source": b1["source"], "variants": b1["variants"]} if b1 else None,
        "style_board": e.id in plan["style_board"].get(gd.game, []),
        "sa3_trial": e.id in plan["sa3_trial"],
        "basis": tx.SOURCE_BASIS,
    }


def _licence(source_plan: dict) -> dict:
    kinds = _dedupe([k for r in source_plan["ranked"] for k in r["kinds"]] + source_plan["now"] + source_plan["later"])
    allowed, conditional, notes = [], [], []
    for k in kinds:
        pol = tx.LICENCE_BY_KIND[k]
        allowed += pol["allowed"]
        conditional += [c for c in pol["conditional"] if c not in conditional]
        if pol["note"]:
            notes.append(pol["note"])
    return {
        "allowed": _dedupe(allowed),
        "conditional": conditional,
        "forbidden": list(tx.FORBIDDEN),
        "attribution_required": False,
        "notes": _dedupe(notes),
        "record": tx.LICENCE_RECORD,
        "basis": "AUDIO_PIPELINE §10.2",
    }


def _board(e: Entry, category: str | None, caps: dict, gap_ms: float | None, rule: dict) -> dict:
    cat = tx.CATEGORIES.get(category or "", {})
    dense = bool(rule.get("dense", cat.get("dense", False)) or (caps.get("per_s") or 0) >= 3)
    contexts = ["trong-tran", "lap-20"] if dense else ["mot-minh", "trong-tran"]
    before = _dedupe(["lap-20" if c == "trong-tran" else c for c in contexts])
    interval, basis = None, None
    if caps.get("per_s"):
        interval, basis = 1000 / caps["per_s"], "Trần phát mỗi giây của tài liệu hoặc mã"
    elif dense and category in tx.TYPICAL_INTERVAL_MS:
        interval, basis = tx.TYPICAL_INTERVAL_MS[category], "Đề xuất theo bot 40 WPM (§6.1); chỉnh khi có nhịp thật của game"
    if interval is not None and gap_ms:
        interval = max(interval, gap_ms)
    return {"contexts": contexts, "contexts_before_phase3": before, "dense": dense,
            "repeat_interval_ms": _num(interval), "repeat_basis": basis, "loudness_match": "lufs-m",
            "basis": "AUDIO_PIPELINE §7"}


def _critic(e: Entry, rule: dict, category: str | None, source: str | None, duration: dict, loop: bool, board: dict) -> dict:
    dirty = rule.get("dirty")
    if dirty is None:
        dirty = source in ("electric", "fire", "blast")
    prompt = (e.listing.get("prompt") or "").lower()
    expect = _dedupe([label for rx, label in tx.AST_HINTS if re.search(rx, prompt)])
    forbid = ["Speech"] if category == "creature" or source == "creature" else []
    target = duration.get("target_ms")
    short = bool(target is not None and target < tx.SHORT_LOOP_EVAL_MS and not loop)
    weights = {"l2": 0.9, "l3": 0.0, "l4": 0.1, "l5": 0.0} if dirty else {"l2": 0.6, "l3": 0.3, "l4": 0.1, "l5": 0.0}
    return {
        "group": None,   # set by derive_critic()
        "dirty": bool(dirty),
        "weights_batch1": weights,
        "loop_eval": {"enabled": short, "length_s": [3, 4] if short else None, "plays": 10 if short else None,
                      "interval_ms": board["repeat_interval_ms"] if short else None},
        "ast": {"expected": expect, "forbid": forbid},
        "basis": "AUDIO_PIPELINE §4.4, §4.5 (L4 chỉ gắn cờ, trọng số tối đa 0,1)",
    }


def derive_critic(card: dict) -> dict:
    """Mirror card fields into the keys critic/spec.py reads (it lifts `critic:` to the top level).

    Run after the merge so hand edits (onset, duration, board...) flow through; skipped when
    `critic` itself is marked manual.
    """
    c = card.get("critic")
    if not isinstance(c, dict) or c.get("manual") is True:
        return card
    pb, on, du = card.get("playback") or {}, card.get("onset") or {}, card.get("duration") or {}
    mu = du.get("music") or {}
    interval = (card.get("board") or {}).get("repeat_interval_ms")
    bands = [b.get("band") for b in (card.get("frequency_role") or {}).get("bands") or []]
    derived = {
        "group": tx.critic_group(card.get("category"), card.get("source_class"), bool(c.get("dirty")), on.get("class"),
                                 card.get("id")),
        "loop": pb.get("mode") == "loop",
        "stereo": pb.get("channels") == "stereo",
        "pitched": bool(card.get("pitches")) or "pitched" in bands,
        "attack_max_ms": on.get("rise_max_ms"),
        "head_max_ms": on.get("lead_silence_max_ms"),
        "rate_hz": _num(1000.0 / interval) if interval else None,
        "bpm": mu.get("bpm"),
        "bars": mu.get("bars"),
        "beats_per_bar": mu.get("beats_per_bar"),
        # Always a string: critic falls back to the top-level `prompt` mapping when intent is empty.
        "intent": (card.get("prompt") or {}).get("text") or card.get("when") or card.get("purpose") or card.get("id"),
        "refs": [str(Path(r["path"]).expanduser()) for r in card.get("references") or [] if isinstance(r, dict) and r.get("path")],
    }
    out = {}
    for k in ("group", "dirty", "weights_batch1", "loop_eval", "ast"):
        if k in c:
            out[k] = derived["group"] if k == "group" else c[k]
    for k, v in derived.items():
        if k != "group":
            out[k] = v
    for k, v in c.items():
        out.setdefault(k, v)
    out["basis"] = out.pop("basis", None) or "AUDIO_PIPELINE §4.4, §4.5"
    card["critic"] = out
    return card


def build_card(gd: GameData, e: Entry, plan: dict, reader) -> tuple[dict, list[Issue]]:
    rule = gd.rule_for(e.id) or {}
    category = rule.get("category")
    source = rule.get("source")
    cat = tx.CATEGORIES.get(category or "", {})
    family = rule.get("family") or cat.get("family")
    loop = bool(e.code.get("loop")) or category in ("ambience", "music")
    bus = e.code.get("bus") or e.listing.get("bus")
    issues: list[Issue] = []
    if not rule:
        issues.append(Issue(gd.game, e.id, "unclassified", "Không có luật phân loại cho id này: thêm vào RULES của bộ đọc hoặc sửa tay (manual: true)", RANGE))

    caps = _caps(e)
    stereo = gd.context.get("stereo", {})
    is_stereo = e.id in stereo.get("ids", []) or (category in stereo.get("categories", []) and (not stereo.get("buses") or bus in stereo.get("buses", [])))
    gap = None if loop else e.code.get("gap_ms")
    if gap is None and caps.get("min_gap_ms"):
        gap = caps["min_gap_ms"]
    playback = {
        "mode": "loop" if loop else "one-shot",
        "channels": "stereo" if is_stereo else "mono",
        "channels_basis": stereo.get("basis"),
        "bus": bus,
        "priority": e.code.get("priority", e.listing.get("priority")),
        "min_gap_ms": _num(gap),
        "limit_group": e.code.get("group"),
        "caps": caps,
        "format": "OGG Vorbis 48 kHz trong game; gốc WAV 48 kHz (§4.3.1, §11)",
    }
    duration, di = _duration(gd, e, category, loop)
    variants, vi = _variants(gd, e, rule, category, plan)
    issues += di + vi
    # The shared suffix ("no music, no speech", Lời Gọi §1) only fits one-shot effects.
    sfx_suffix = not loop and category not in ("music", "stinger") and source != "voice"
    rand_group = rule.get("rand") or cat.get("rand", "default")
    rg = tx.RANDOMISATION[rand_group]
    source_plan = _source_plan(gd, e, rule, source, plan)
    board = _board(e, category, caps, gap, rule)

    blocked = list(rule.get("blocked_by", [])) + list(source_plan["needs_now"])
    if e.proposed:
        blocked.append("sua-tai-lieu-game")
    if e.in_list and not e.in_code and not e.proposed:
        blocked.append("chua-co-trong-ma")
    layer_plan = None
    if rule.get("layer_plan") or rule.get("related"):
        lp = rule.get("layer_plan") or {}
        layer_plan = {"builds_on": lp.get("builds_on"), "shares": list(lp.get("shares", [])),
                      "summary": lp.get("summary"), "related": list(rule.get("related", []))}
    plan_refs = []
    if source_plan["batch1"]:
        plan_refs.append(f"AUDIO_PIPELINE §9 #{source_plan['batch1']['n']} (lô 1)")
    if source_plan["style_board"]:
        plan_refs.append("AUDIO_PIPELINE §9 (âm chữ ký của bảng phong cách)")
    if source_plan["sa3_trial"]:
        plan_refs.append("AUDIO_PIPELINE §9 (bản thử Stable Audio 3, 6 id)")
    if e.proposed:
        plan_refs.append(e.proposed)

    card = {
        "schema": SCHEMA_VERSION,
        "id": e.id,
        "game": gd.game,
        "status": "proposed" if e.proposed else "draft",
        "manual_fields": [],
        "when": e.listing.get("when") or (e.proposed or ""),
        "purpose": e.listing.get("feel") or "",
        "category": category,
        "family": family,
        "source_class": source,
        "playback": playback,
        "duration": duration,
        "onset": _onset(gd, rule, category, loop, family),
        "variants": variants,
        "randomisation": {"group": rand_group, "pitch_cents": rg["pitch_cents"], "gain_db": rg["gain_db"],
                          "rules": list(rg["rules"]), "current_code": reader.current_randomisation(e), "basis": tx.RANDOMISATION_BASIS},
        "frequency_role": _bands(gd, rule, category, source),
        "loudness": _loudness(gd, e, rule, category, bus),
        "prompt": {"text": e.listing.get("prompt") or None,
                   "suffix": gd.context.get("prompt_suffix") if sfx_suffix else None,
                   "style_root": gd.context.get("style_root"), "sweetener": gd.context.get("sweetener"),
                   "variants": [], "basis": f"{gd.files['list']}; gốc prompt theo AUDIO_PIPELINE §5.2 (chốt sau bảng phong cách)"},
        "pitches": _pitches(gd, e, rule),
        "parts": [dict(p) for p in rule["parts"]] if rule.get("parts") else None,
        "layer_plan": layer_plan,
        "references": [],
        "source_plan": source_plan,
        "licence": _licence(source_plan),
        "constraints": _dedupe(list(rule.get("constraints", [])) + list(gd.context.get("constraints", []))),
        "board": board,
        "critic": _critic(e, rule, category, source, duration, loop, board),
        "blocked_by": _dedupe(blocked),
        "origin": {
            "code": {"file": e.code.get("code_file", gd.files["catalog"]), "present": e.in_code,
                     "asset_stem": e.code.get("file") if gd.game == "dragon-hold" else None,
                     "synth_in_code": e.code.get("synth", e.in_code)},
            "sound_list": {"file": gd.files["list"], "present": e.in_list, "section": e.listing.get("section")},
            "plan": plan_refs,
        },
        "notes": "",
    }
    return derive_critic(card), issues
