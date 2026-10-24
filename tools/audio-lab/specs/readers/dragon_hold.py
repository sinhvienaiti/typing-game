"""Rồng Giữ Ải: src/audio/catalog.ts (canonical ids, bus, priority, length) + docs/audio/M0_SOUND_LIST.md."""
from __future__ import annotations

import re
from pathlib import Path

from .. import parse
from ..model import DISAGREE, Entry, GameData, Issue
from . import common

GAME = "dragon-hold"
LABEL = "Rồng Giữ Ải"
FILES = {
    "catalog": "src/audio/catalog.ts",
    "mix": "src/audio/mix.ts",
    "music": "src/audio/music-plan.ts",
    "list": "docs/audio/M0_SOUND_LIST.md",
}

DEF_RE = re.compile(
    r'^\s*"(?P<id>[\w.-]+)":\s*def\(\s*"(?P<bus>\w+)",\s*(?P<p>\d),\s*(?P<len>[\d_]+),\s*"(?P<file>[^"]+)"'
    r"(?:,\s*\{(?P<opts>[^}]*)\})?\s*\)", re.M)
OPT_RE = re.compile(r'(\w+):\s*("[^"]*"|-?[\d_.]+|true|false)')
LEVEL_RE = re.compile(r"(\w+):\s*\{\s*gain:\s*([\d.]+),\s*pronunciationDb:\s*(-?[\d.]+)\s*\}")
NO_VARY = ("typing", "ui", "learning", "stingers")

# Rule sentences the reader turns into data (verified on every run).
LIST_NEEDLES = [
    "Tiếng lẻ chuẩn hóa đỉnh −1 dBTP",
    "nhạc −18 LUFS, nền −26 LUFS",
    "Tiếng lẻ mono. Nhạc và nền stereo",
    "Đòn trúng nên có 3–6 biến thể",
    "Mã tự đổi cao độ 0,96–1,04, ±1,5 dB, lệch 0–12 ms",
    "Tiếng gõ phải bắt đầu ngay (< 20 ms)",
]
CODE_NEEDLES = [
    "gapMs: opts.gapMs ?? 30",
    'bus !== "typing" && bus !== "ui" && bus !== "learning" && bus !== "stingers"',
    "M0a synthesises Rừng and Đợt",
]

CONTEXT = {
    "style_root": "painterly fantasy forest, warm, organic, outdoor",
    "sweetener": "than hồng lách tách và đàn hạc",
    "prompt_suffix": None,
    "loudness": {
        "short": {"metric": "peak-dbtp", "target": -1, "basis": "M0_SOUND_LIST §1: Tiếng lẻ chuẩn hóa đỉnh −1 dBTP"},
        "ambience": {"metric": "lufs-i", "target": -26, "basis": "M0_SOUND_LIST §1: nền −26 LUFS"},
        "music": {"metric": "lufs-i", "target": -18, "basis": "M0_SOUND_LIST §1: nhạc −18 LUFS"},
    },
    "onset_cap_ms": {"key": 20},
    "onset_basis": "M0_SOUND_LIST §1: Đầu file không có khoảng lặng. Tiếng gõ phải bắt đầu ngay (< 20 ms)",
    "variants": [{"categories": ["hit-small", "hit-heavy"], "min": 3, "max": 6, "basis": "M0_SOUND_LIST §1: Đòn trúng nên có 3–6 biến thể"}],
    "stereo": {"categories": ["music", "ambience"], "buses": ["music", "ambience"], "ids": [],
               "basis": "M0_SOUND_LIST §1: Tiếng lẻ mono. Nhạc và nền stereo"},
    "freq_roles": {
        "sub": "Thân gầm rồng, Bom Hạt Thông",
        "body": "Thân lửa, thân quái",
        "voice": "Chỉ đầu tiếng rất ngắn",
        "presence": "Lách tách than hồng, tiếng tách phím gỗ",
        "pitched": "Chuông nhỏ và đàn hạc theo ngũ cung",
    },
    "constraints": [],
    "per_id_gain": {"default_db": None, "basis": "src/audio/catalog.ts gainDb (mặc định 0 dB), mức trước bus"},
}

# Classification, first match wins (§3.2 source class, §4.3.3 category, §4.6 family).
RULES: list[tuple[str, dict]] = [
    (r"type\.key", {"category": "key-ok", "source": "key", "add_bands": ["pitched"],
                    "constraints": ["Tiếng gỗ mềm, kèm chuông nhỏ theo ngũ cung Fa trưởng (§8.1)", "Chuông lên 1 bán cung mỗi chữ, tối đa 12 (mã đổi cao độ)"]}),
    (r"type\.miss", {"category": "key-bad", "source": "key"}),
    (r"type\.(back|switch)", {"category": "ui", "source": "key"}),
    (r"type\.word", {"category": "word-reward", "source": "pitched-reward"}),
    (r"fire\.cast", {"category": "word-reward", "source": "shot", "add_bands": ["body", "sub"],
                     "constraints": ["Theo luật âm xong từ (§6.2)", "Lớp gầm thú thêm sau (Freesound CC0 do chủ dự án tải, hoặc tự gầm) (§9)"]}),
    (r"fire\.impact\.a", {"category": "hit-heavy", "weight": "medium", "source": "impact", "dirty": True}),
    (r"fire\.impact\.b", {"category": "hit-heavy", "weight": "medium", "source": "impact", "dirty": True,
                          "layer_plan": {"builds_on": "fire.impact.a", "summary": "Từ fire.impact.a: đổi lớp thân, dịch ±cent, giữ đầu tiếng (§9 #3)"}}),
    (r"fire\.impact\.c", {"category": "hit-heavy", "weight": "heavy", "source": "impact", "dirty": True,
                          "layer_plan": {"builds_on": "fire.impact.a", "summary": "fire.impact.a cộng thêm tiếng bùng lửa (§5.2, §9 #4)"}}),
    (r"impact\.multi", {"category": "hit-heavy", "weight": "heavy", "source": "impact", "dirty": True}),
    (r"dragon\.(hurt|roar|down)", {"category": "creature", "source": "creature", "add_bands": ["sub"],
                                   "variants": {"min": 1, "max": 2, "basis": "§4.3.3: Rồng chính 1–2 biến thể"},
                                   "constraints": ["Hai Rồng có hai tính cách riêng: ghép tiếng thú khác nhau rồi hạ giọng (§8.1)"]}),
    (r"dragon\.(low|heartbeat)", {"category": "warning", "source": "warning-stinger"}),
    (r"dragon\.breath", {"category": "fx-other", "source": "fire", "family": "ban", "onset": "none", "dirty": True,
                         "parts": [{"name": "dau", "note": "Phần đầu (hít vào, bùng)"}, {"name": "vong-lap", "note": "Vòng lặp luồng lửa"},
                                   {"name": "cuoi", "note": "Phần cuối (tắt)"}],
                         "constraints": ["Lửa thật như đuốc, khí đốt, giẻ cháy vung trên sào; thân gầm 60–250 Hz (§8.1)", "Tách 3 phần: đầu, vòng lặp, cuối (§3.2)"]}),
    (r"dragon\.skyfire\.cast", {"category": "fx-other", "source": "fire", "family": "ban", "onset": "none"}),
    (r"dragon\.skyfire\.impact", {"category": "blast", "source": "blast", "dirty": True}),
    (r"dragon\.inferno", {"category": "blast", "source": "fire", "dirty": True}),
    (r"dragon\.rage", {"category": "fx-other", "source": "fire", "family": "sinh-vat", "onset": "none"}),
    (r"dragon\.(skill-ready|level)", {"category": "fx-other", "source": "pitched-reward", "family": "thuong", "rand": "rare-fixed"}),
    (r"dragon\.potion", {"category": "fx-other", "source": "foley-other", "family": "thuong"}),
    (r"enemy\.\w+\.spawn", {"category": "creature", "source": "creature"}),
    (r"enemy\.biped\.windup", {"category": "fx-other", "source": "foley-other", "family": "sinh-vat"}),
    (r"enemy\.(quadruped|flyer)\.windup", {"category": "fx-other", "source": "creature", "family": "sinh-vat", "onset": "creature"}),
    (r"enemy\.biped\.attack", {"category": "fx-other", "source": "foley-other", "family": "trung", "onset": "none"}),
    (r"enemy\.biped\.shoot", {"category": "shot", "source": "shot"}),
    (r"enemy\.quadruped\.attack", {"category": "hit-small", "source": "creature"}),
    (r"enemy\.quadruped\.charge", {"category": "hit-heavy", "weight": "heavy", "source": "impact"}),
    (r"enemy\.quadruped\.howl", {"category": "creature", "source": "creature"}),
    (r"enemy\.flyer\.attack", {"category": "fx-other", "source": "creature", "family": "trung", "onset": "none"}),
    (r"enemy\.swarm\.attack", {"category": "hit-small", "source": "impact"}),
    (r"enemy\.\w+\.hit", {"category": "hit-small", "source": "impact"}),
    (r"enemy\.swarm\.death", {"category": "death-swarm", "source": "impact", "dirty": True}),
    (r"enemy\.\w+\.death", {"category": "death-big", "source": "impact"}),
    (r"enemy\.\w+\.march", {"category": "ambience", "source": "ambience",
                            "constraints": ["Một vòng lặp cho cả lớp quái, to theo số quái sống; mã đặt trái phải (M0_SOUND_LIST §3)"]}),
    (r"kill\.chime", {"category": "word-reward", "source": "pitched-reward", "rand": "rare-fixed"}),
    (r"warn\.telegraph", {"category": "warning", "source": "warning-stinger", "onset": "none"}),
    (r"warn\.\w+", {"category": "warning", "source": "warning-stinger"}),
    (r"general\.g01\.horn", {"category": "stinger", "source": "warning-stinger", "related": ["wave.horn"],
                             "constraints": ["Như wave.horn, trầm hơn; kiểm điệu với stem general (§9 #6)"]}),
    (r"general\.g01\.attack", {"category": "hit-heavy", "weight": "heavy", "source": "impact"}),
    (r"general\.g01\.skill", {"category": "creature", "source": "creature"}),
    (r"general\.g01\.aura", {"category": "fx-other", "source": "warning-stinger", "family": "nen"}),
    (r"general\.g01\.death", {"category": "death-big", "source": "creature"}),
    (r"general\.aura\.break", {"category": "fx-other", "source": "impact", "family": "trung"}),
    (r"trap\.pine-bomb\.trigger", {"category": "blast", "source": "blast", "dirty": True,
                                   "constraints": ["Bom Hạt Thông là bẫy duy nhất nổ (§8.1)"]}),
    (r"trap\.spikes\.trigger", {"category": "hit-heavy", "weight": "medium", "source": "impact", "family": "no",
                                "constraints": ["Tiếng gỗ đâm lên. Không nổ (§8.1)"]}),
    (r"trap\.net\.trigger", {"category": "fx-other", "source": "foley-other", "family": "no",
                             "constraints": ["Dây quấn, không có tiếng nổ (§8.1)"]}),
    (r"trap\.[\w-]+\.arm", {"category": "fx-other", "source": "foley-other", "family": "no"}),
    (r"house\.herb\.pulse", {"category": "fx-other", "source": "pitched-reward", "family": "thuong", "onset": "none"}),
    (r"(unit\.warden|house\.herb)\.(place|down)", {"category": "fx-other", "source": "foley-other", "family": "trung"}),
    (r"unit\.hit", {"category": "hit-small", "source": "impact"}),
    (r"ui\.confirm", {"category": "ui", "source": "pitched-reward"}),
    (r"ui\.\w+", {"category": "ui", "source": "ui"}),
    (r"wave\.horn", {"category": "stinger", "source": "warning-stinger"}),
    (r"wave\.clear", {"category": "stinger", "source": "warning-stinger"}),
    (r"stinger\.(victory|defeat)", {"category": "stinger", "source": "warning-stinger"}),
    (r"learn\.(new|right)", {"category": "word-reward", "source": "pitched-reward", "rand": "rare-fixed"}),
    (r"learn\.wrong", {"category": "fx-other", "source": "pitched-reward", "family": "thuong", "rand": "rare-fixed",
                       "voice_band": "avoid"}),
    (r"amb\.bird", {"category": "fx-other", "source": "ambience", "family": "nen", "onset": "none"}),
    (r"amb\.\w+", {"category": "ambience", "source": "ambience"}),
    (r"music\.general", {"category": "music", "source": "music", "blocked_by": ["chu-du-an-duyet"],
                         "constraints": ["Stem general ghi \"D minor\" trên các stem Rê Dorian: đổi sang Rê Dorian, hoặc tránh nốt Si giáng khi ở hợp âm G. Chủ dự án chọn (§16 #8)"]}),
    (r"music\.\w+", {"category": "music", "source": "music"}),
]

MUSIC_NAMES = {"forest": "Rừng", "wave": "Đợt", "surge": "Dồn", "general": "mô-típ tướng"}


def _opts(raw: str | None) -> dict:
    out: dict = {}
    for k, v in OPT_RE.findall(raw or ""):
        if v in ("true", "false"):
            out[k] = v == "true"
        elif v.startswith('"'):
            out[k] = v.strip('"')
        else:
            out[k] = float(v.replace("_", ""))
    return out


def read_catalog(text: str) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for m in DEF_RE.finditer(text):
        opts = _opts(m.group("opts"))
        bus = m.group("bus")
        out[m.group("id")] = {
            "bus": bus,
            "priority": int(m.group("p")),
            "length_ms": float(m.group("len").replace("_", "")),
            "file": m.group("file"),
            "gap_ms": opts.get("gapMs", 30.0),
            "gain_db": opts.get("gainDb", 0.0),
            "vary": opts.get("vary", bus not in NO_VARY),
            "loop": bool(opts.get("loop", False)),
            "group": opts.get("group"),
        }
    return out


def _cell_ms(cell: str) -> tuple[float | None, bool]:
    loop = "lặp" in cell
    n = parse.vn_number(cell)
    if n is None:
        return None, loop
    return (n * 1000.0 if re.search(r"\bs\b", cell) else n), loop


def read_list(text: str) -> tuple[dict[str, dict], dict[str, dict]]:
    """(sounds by id, bus levels by bus) from M0_SOUND_LIST.md."""
    sounds: dict[str, dict] = {}
    levels: dict[str, dict] = {}
    for t in parse.md_tables(text):
        top = t.heading_path[1] if len(t.heading_path) > 1 else t.heading
        if t.header[0] == "Bus" and top.startswith("2."):
            for row in t.rows:
                bus = (parse.backticks(row["Bus"]) or [""])[0]
                duck = row.get("Khi phát âm từ", "")
                levels[bus] = {"gain": parse.vn_number(row.get("Mức", "")),
                               "duck": 0.0 if "không hạ" in duck else parse.vn_number(duck)}
        elif t.header[0] == "Lớp" and top.startswith("4."):
            for row, line in zip(t.rows, t.row_lines):
                layer = (parse.backticks(row["Lớp"]) or [""])[0]
                prompt = (parse.backticks(row.get("Prompt cho file sau", "")) or [row.get("Prompt cho file sau", "")])[0]
                sounds["music." + layer] = {
                    "section": t.heading, "bus": "music", "priority": None, "when": row.get("Khi nào", ""),
                    "feel": f"Lớp {MUSIC_NAMES.get(layer, layer)}; mức {row.get('Mức', '')}",
                    "prompt": prompt, "length_cell": "", "gap_cell": "", "line": line, "layer": layer,
                }
        elif t.header[0] == "Id" and top.startswith("5."):
            sec_bus = re.search(r"bus `(\w+)`", t.heading)
            sec_p = re.search(r"\bP(\d)\b", t.heading)
            for row, line in zip(t.rows, t.row_lines):
                ids = parse.backticks(row["Id"])
                if not ids:
                    continue
                bus = sec_bus.group(1) if sec_bus else None
                prio = int(sec_p.group(1)) if sec_p else None
                if row.get("Bus/P"):
                    bp = re.match(r"(\w+)/P(\d)", row["Bus/P"].strip())
                    if bp:
                        bus, prio = bp.group(1), int(bp.group(2))
                if row.get("P"):
                    pm = re.search(r"P(\d)", row["P"])
                    prio = int(pm.group(1)) if pm else prio
                prompt_cell = row.get("Prompt", "")
                sounds[ids[0]] = {
                    "section": t.heading, "bus": bus, "priority": prio, "when": row.get("Khi phát", ""),
                    "feel": row.get("Cảm giác", ""), "prompt": (parse.backticks(prompt_cell) or [prompt_cell])[0],
                    "length_cell": row.get("Dài", ""), "gap_cell": row.get("Cách", ""), "line": line,
                }
    return sounds, levels


def read(game_root: Path) -> GameData:
    texts = {k: parse.read_text(game_root / v) for k, v in FILES.items()}
    issues = common.need(texts["list"], LIST_NEEDLES, GAME, FILES["list"])
    issues += common.need(texts["catalog"] + texts["music"], CODE_NEEDLES, GAME, FILES["catalog"])

    catalog = read_catalog(texts["catalog"])
    listed, doc_levels = read_list(texts["list"])
    code_levels = {m.group(1): {"gain": float(m.group(2)), "duck": float(m.group(3))} for m in LEVEL_RE.finditer(texts["mix"])}

    song_bpm = parse.ts_number_const(texts["music"], "bpm")
    song_bars = parse.ts_number_const(texts["music"], "bars")
    layers = parse.ts_string_array(texts["music"], "MUSIC_LAYERS")
    synth_layers = {"forest", "wave"} if "M0a synthesises Rừng and Đợt" in texts["music"] else set()
    for layer in layers:
        catalog["music." + layer] = {"bus": "music", "priority": None, "length_ms": None, "file": f"music/forest/{layer}",
                                     "gap_ms": None, "gain_db": None, "vary": False, "loop": True, "group": None,
                                     "bpm": song_bpm, "bars": int(song_bars) if song_bars else None,
                                     "synth": layer in synth_layers, "layer": layer, "code_file": FILES["music"]}

    entries: list[Entry] = []
    for sid in list(catalog) + [s for s in listed if s not in catalog]:
        e = Entry(sid, GAME, in_code=sid in catalog, in_list=sid in listed,
                  code=dict(catalog.get(sid, {})), listing=dict(listed.get(sid, {})))
        entries.append(e)
        if not (e.in_code and e.in_list):
            continue
        c, li = e.code, e.listing
        if sid.startswith("music."):
            bars = parse.parse_bars(li.get("prompt", ""))
            if bars and bars.get("bpm") and c.get("bpm") and bars["bpm"] != c["bpm"]:
                issues.append(Issue(GAME, sid, "tempo", f"Prompt ghi {bars['bpm']:g} BPM, music-plan.ts {c['bpm']:g} BPM", DISAGREE, c["bpm"], bars["bpm"]))
            if bars and bars.get("bars") and c.get("bars") and bars["bars"] != c["bars"]:
                issues.append(Issue(GAME, sid, "bars", f"Prompt ghi {bars['bars']} ô nhịp, music-plan.ts {c['bars']}", DISAGREE, c["bars"], bars["bars"]))
            continue
        length, loop = _cell_ms(li.get("length_cell", ""))
        if length is not None and abs(length - c["length_ms"]) > 0.5:
            issues.append(Issue(GAME, sid, "length", f"Dài: catalog {c['length_ms']:g} ms, danh sách {length:g} ms", DISAGREE, c["length_ms"], length))
        if loop != c["loop"]:
            issues.append(Issue(GAME, sid, "loop", f"Lặp: catalog {c['loop']}, danh sách {loop}", DISAGREE, c["loop"], loop))
        gap = parse.vn_number(li.get("gap_cell", "")) if li.get("gap_cell", "").strip() not in ("", "—", "-") else None
        if gap is not None and not c["loop"] and abs(gap - c["gap_ms"]) > 0.5:
            issues.append(Issue(GAME, sid, "gap", f"Cách: catalog {c['gap_ms']:g} ms, danh sách {gap:g} ms", DISAGREE, c["gap_ms"], gap))
        if li.get("bus") and li["bus"] != c["bus"]:
            issues.append(Issue(GAME, sid, "bus", f"Bus: catalog `{c['bus']}`, danh sách `{li['bus']}`", DISAGREE, c["bus"], li["bus"]))
        if li.get("priority") is not None and li["priority"] != c["priority"]:
            issues.append(Issue(GAME, sid, "priority", f"Ưu tiên: catalog P{c['priority']}, danh sách P{li['priority']}", DISAGREE, c["priority"], li["priority"]))
        hit = common.compare_prompt_length(e, c["length_ms"], GAME)
        if hit:
            issues.append(hit)
    issues += common.presence_issues(entries, GAME, FILES["catalog"], FILES["list"])
    issues += common.music_key_issues(entries, GAME)

    levels = {b: {"code": code_levels.get(b), "doc": doc_levels.get(b)} for b in sorted(set(code_levels) | set(doc_levels))}
    for e in entries:
        e.code.setdefault("bus", e.listing.get("bus"))
    issues += common.bus_level_issues(levels, entries, GAME, FILES["list"], FILES["mix"])

    ctx = dict(CONTEXT)
    ctx["bus_gain"] = {b: v["gain"] for b, v in code_levels.items()}
    ctx["duck_db"] = {b: v["duck"] for b, v in code_levels.items()}
    ctx["music"] = {"bpm": song_bpm, "bars": int(song_bars) if song_bars else None, "beats_per_bar": 4, "key": "Rê Dorian"}
    return GameData(GAME, LABEL, FILES, entries, issues, levels, ctx, RULES)


def current_randomisation(e: Entry) -> str:
    if e.code.get("loop"):
        return "Vòng lặp, không đổi ngẫu nhiên"
    if e.code.get("vary"):
        return "±4 % cao độ (khoảng ±68 cent), ±1,5 dB, lệch 0–12 ms (catalog vary)"
    return "Không đổi ngẫu nhiên (catalog vary: false)"
