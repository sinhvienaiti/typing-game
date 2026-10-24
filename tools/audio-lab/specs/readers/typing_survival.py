"""Tuyến Cuối: src/audio/theme-audio.ts (SOUND_IDS, BUSES, voice() calls) + docs/audio/THEME_SOUND_LIST.md."""
from __future__ import annotations

import fnmatch
import math
import re
from pathlib import Path

from .. import parse
from ..model import DISAGREE, PLAN, Entry, GameData, Issue
from . import common

GAME = "typing-survival"
LABEL = "Tuyến Cuối"
FILES = {
    "catalog": "src/audio/theme-audio.ts",
    "music": "src/audio/music.ts",
    "list": "docs/audio/THEME_SOUND_LIST.md",
}

BUS_RE = re.compile(r"(\w+):\s*\{\s*gain:\s*([\d.]+),\s*duck:\s*([\d.]+)\s*\}")
VOICE_RE = re.compile(r'this\.voice\(\s*"(\w+)"\s*,(.*?)\);', re.S)
PROMPT_RE = re.compile(r"^-\s*`([\w.]+)`\s*[—-]\s*\*Prompt:\*\s*\"(.+)\"\s*$", re.M)
ID_TOKEN = re.compile(r"^[a-z]+(?:\.[a-z0-9]+)+$")
FILE_EXT = re.compile(r"\.(ts|js|mjs|md|json|ogg|wav|css|html)$")

LIST_NEEDLES = [
    "đỉnh −1 dBFS",
    "dưới 5 ms",
    "cần 4–6 biến thể",
    "96 BPM, La thứ",
    "−16 LUFS",
    "mono (trừ nhạc và `end.*`)",
]

CONTEXT = {
    "style_root": "industrial, steel, close, punchy",
    "sweetener": "tia điện và thép ngân",
    "prompt_suffix": None,
    "loudness": {
        "short": {"metric": "peak-dbtp", "target": -1, "basis": "THEME_SOUND_LIST §2: đỉnh −1 dBFS"},
        "music": {"metric": "lufs-i", "target": -16, "basis": "THEME_SOUND_LIST §2: −16 LUFS"},
    },
    "onset_cap_ms": {"all": 5},
    "onset_basis": "THEME_SOUND_LIST §2: cắt im lặng đầu file, tiếng phải bắt đầu ngay, dưới 5 ms",
    "variants": [],   # filled from the list sentence in read()
    "stereo": {"categories": ["music"], "buses": [], "ids": ["end.win", "end.lose"],
               "basis": "THEME_SOUND_LIST §2: mono (trừ nhạc và end.*)"},
    "freq_roles": {
        "sub": "Sub súng, sub dùng chung hit.sub",
        "body": "Thân súng, thân tiếng trúng",
        "voice": "Chỉ đầu tiếng rất ngắn; báo nguy ngắn",
        "presence": "Tách phím, lách tách điện, đầu tiếng hit.t1",
        "pitched": "kill.chime theo ngũ cung La thứ",
    },
    "per_id_gain": {"default_db": 0.0, "basis": "Mã không có mức riêng cho từng id: voice() nối thẳng vào bus, mức nằm trong mã tổng hợp. File phát ở 0 dB vào bus"},
    "constraints": ["Âm industrial: thép, súng nặng, điện, kim loại vỡ; khác tiếng laser và nhạc điện tử vũ trụ của Space Typing (THEME_SOUND_LIST)"],
}

HIT_LAYERS = ("Mỗi bậc có file đầu tiếng + thân riêng; hit.sub và hit.tail dùng chung, mã ghép theo cờ bass và tail của tiers.ts; "
              "giữ trong mã độ to theo số viên và độ dài theo bậc (§6.3 #3). Cần nâng kit SceneAudio trước (§6.3 #1)")

RULES: list[tuple[str, dict]] = [
    (r"key\.ok", {"category": "key-ok", "source": "key", "constraints": ["Rơ-le thép khô (§8.3)"]}),
    (r"key\.bad", {"category": "key-bad", "source": "key"}),
    (r"word\.load", {"category": "word-reward", "source": "impact",
                     "constraints": ["Theo luật âm xong từ (§6.2): đang ở bus alerts (chỉ hạ −2 dB), kế hoạch đề xuất chuyển sang bus được hạ sâu hơn"]}),
    (r"word\.perfect", {"category": "word-reward", "source": "impact", "add_bands": ["presence"],
                        "layer_plan": {"builds_on": "word.load", "summary": "word.load cộng tiếng nạp điện tổng hợp (§9 #18)"},
                        "constraints": ["Theo luật âm xong từ (§6.2)"]}),
    (r"gun\.xung\.loop", {"category": "ambience", "source": "foley-other", "family": "ban", "dirty": True,
                          "layer_plan": {"builds_on": "gun.xung", "shares": [], "summary": "Nền cơ khí chạy suốt loạt bắn, dưới các phát đơn (BATCH1_BRIEF §3.2)"},
                          "constraints": ["Không có đầu tiếng nổi lên: mọi đầu tiếng thấp hơn đỉnh phát đơn ít nhất 12 dB (BATCH1_BRIEF §3.2)",
                                          "Không có chu kỳ rõ ở 5–15 Hz: tự tương quan đường bao ở độ trễ 60–220 ms dưới 0,3"]}),
    (r"gun\.xung\.tail", {"category": "fx-other", "source": "impact", "family": "ban", "onset": "none", "dirty": True,
                          "layer_plan": {"builds_on": None, "shares": ["hit.tail"], "summary": "Khi ngừng bắn: vang thép sảnh rộng và máy dừng; chung chất liệu với hit.tail (BATCH1_BRIEF §3.2)"}}),
    (r"gun\.xung", {"category": "shot", "source": "shot", "dirty": True, "add_bands": ["sub"],
                    "constraints": ["Ghép bốn lớp: thịch sub 40–90 Hz ≤120 ms, cơ khí ngắn, năng lượng, đuôi dùng chung hit.tail (§8.3)",
                                    "Phát 5 lần mỗi giây nên phải ngắn (§3.2)"]}),
    (r"gun\.tia\.(start|end)", {"category": "fx-other", "source": "electric", "family": "ban", "onset": "none", "dirty": True}),
    (r"gun\.tia\.pulse", {"category": "hit-small", "source": "electric", "dirty": True}),
    (r"hit\.t1", {"category": "hit-small", "source": "impact", "layer_plan": {"builds_on": None, "shares": ["hit.sub", "hit.tail"], "summary": HIT_LAYERS}}),
    (r"hit\.t2", {"category": "hit-heavy", "weight": "medium", "source": "impact", "layer_plan": {"builds_on": None, "shares": ["hit.sub", "hit.tail"], "summary": HIT_LAYERS}}),
    (r"hit\.t4", {"category": "hit-heavy", "weight": "heavy", "source": "impact", "layer_plan": {"builds_on": None, "shares": ["hit.sub", "hit.tail"], "summary": HIT_LAYERS}}),
    (r"hit\.sub", {"category": "fx-other", "source": "impact", "family": "trung", "bands": ["sub"],
                   "source_override": {"ranked": [(["synth"], "Tổng hợp, dùng chung cho mọi bậc (§9 #13)")], "now": ["synth"], "later": []},
                   "layer_plan": {"builds_on": None, "shares": [], "summary": "Lớp sub dùng chung, mã thêm từ bậc T2 (§6.3 #3)"}}),
    (r"hit\.tail", {"category": "fx-other", "source": "impact", "family": "trung", "onset": "none",
                    "source_override": {"ranked": [(["sample-player"], "VCSL Anvil, Brake Drum cộng vang phòng rộng, dùng chung (§9 #14)")],
                                        "now": ["sample-player"], "later": []},
                    "layer_plan": {"builds_on": None, "shares": [], "summary": "Đuôi kim loại dùng chung, mã thêm từ bậc T4 và cho súng (§6.3 #3, §8.3)"}}),
    (r"kill\.swarm", {"category": "death-swarm", "source": "impact", "dirty": True,
                      "constraints": ["Nốt kill.chime tách riêng để mã chỉnh cao độ (§9 #15)"]}),
    (r"kill\.elite", {"category": "death-big", "source": "impact", "dirty": True}),
    (r"kill\.chime", {"category": "word-reward", "source": "pitched-reward", "rand": "rare-fixed",
                      "source_override": {"ranked": [(["sample-player"], "Thanh thép: VCSL Anvil, Brake Drum hoặc thanh kim loại, phát từng nốt"),
                                                     (["synth"], "Tổng hợp thanh thép như hiện nay")],
                                          "now": ["sample-player", "synth"], "later": []},
                      "pitches": {"notes": [], "scale": "Ngũ cung La thứ, từ C5 trở lên, tối đa 12 bậc",
                                  "basis": "THEME_SOUND_LIST §5 (chuỗi hạ), AUDIO_PIPELINE §6.4"}}),
    (r"foe\.shot", {"category": "shot", "source": "shot"}),
    (r"foe\.shot\.down", {"category": "hit-small", "source": "impact"}),
    (r"hurt\.breach", {"category": "warning", "source": "warning-stinger",
                       "source_override": {"ranked": [(["model-later", "synth"], "Stable Audio 3 cộng còi tổng hợp (§9 #20)"), (["synth"], "Tổng hợp như hiện nay")],
                                           "now": ["synth"], "later": ["model-later"]}}),
    (r"hurt\.hull", {"category": "hit-heavy", "weight": "heavy", "source": "impact"}),
    (r"hurt\.drain", {"category": "fx-other", "source": "electric", "family": "trung", "dirty": True}),
    (r"support\.repair", {"category": "fx-other", "source": "foley-other", "family": "nen"}),
    (r"alarm\.surge", {"category": "warning", "source": "warning-stinger", "onset": "none",
                       "source_override": {"ranked": [(["synth"], "Còi tổng hợp bằng numpy và pedalboard"), (["model-later"], "Stable Audio 3 (còi)")],
                                           "now": ["synth"], "later": []}}),
    (r"end\.(win|lose)", {"category": "stinger", "source": "warning-stinger",
                          "source_override": {"ranked": [(["sample-player", "synth"], "MIDI và bộ phát mẫu (VCSL Anvil, Brake Drum) cộng synth tổng hợp bằng mã"),
                                                         (["model-later"], "Stable Audio 3")],
                                              "now": ["sample-player", "synth"], "later": []}}),
    (r"ui\.\w+", {"category": "ui", "source": "ui"}),
    (r"music\.surge", {"category": "music", "source": "music",
                       "constraints": ["Lớp chiến là những cú bùng ngắn, nghịch phách; không có pad kéo dài ở 300 Hz–3 kHz (§8.3, §8.5)"]}),
    (r"music\.\w+", {"category": "music", "source": "music"}),
]

# Ids the plan adds that the game list does not have yet (game docs win: proposal only).
PLAN_PROPOSED = {
    "hit.sub": "AUDIO_PIPELINE §6.3 #3, §9 #13, §16 #6: lớp sub dùng chung của bậc trúng",
    "hit.tail": "AUDIO_PIPELINE §6.3 #3, §9 #14, §16 #6: đuôi kim loại dùng chung",
    "gun.xung.loop": "BATCH1_BRIEF §3.2: nền cơ khí liên thanh chạy suốt loạt bắn Xung",
    "gun.xung.tail": "BATCH1_BRIEF §3.2: đuôi khi súng Xung ngừng bắn",
}
PROPOSED_BUS = {"gun.xung.loop": "guns", "gun.xung.tail": "guns"}     # default: impacts


def _bus_globs(text: str) -> tuple[dict[str, dict], dict[str, list[str]]]:
    levels: dict[str, dict] = {}
    globs: dict[str, list[str]] = {}
    for t in parse.md_tables(text):
        if t.header[:2] == ["Bus", "Mức"]:
            for row in t.rows:
                bus = (parse.backticks(row["Bus"]) or [""])[0]
                duck = row.get("Khi đọc từ", "")
                levels[bus] = {"gain": parse.vn_number(row["Mức"]), "duck": parse.vn_number(duck)}
                globs[bus] = parse.backticks(row.get("Âm trên bus", ""))
    return levels, globs


def read_list(text: str) -> dict[str, dict]:
    sounds: dict[str, dict] = {}
    for t in parse.md_tables(text):
        if t.header[0] != "Id":
            continue
        for row, line in zip(t.rows, t.row_lines):
            ids = parse.backticks(row["Id"])
            if ids:
                sounds[ids[0]] = {"section": t.heading, "when": row.get("Khi nào", ""), "feel": row.get("Cảm giác", ""),
                                  "current": row.get("Mã hiện tại", "") or row.get("Mã hiện tại (bản giữ chỗ)", ""),
                                  "line": line, "prompt": None}
    for m in PROMPT_RE.finditer(text):
        sid = m.group(1)
        sounds.setdefault(sid, {"section": None, "when": "", "feel": "", "current": "", "line": None})
        sounds[sid]["prompt"] = m.group(2)
        sounds[sid]["prompt_line"] = text[: m.start()].count("\n") + 1
    return sounds


def code_buses(text: str, ids: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for m in VOICE_RE.finditer(text):
        bus, rest = m.group(1), m.group(2)
        named = [s for s in re.findall(r'"([\w.]+)"', rest) if s in ids]
        if '"ui." +' in rest:
            named += [s for s in ids if s.startswith("ui.")]
        for sid in named:
            out[sid] = bus
    if re.search(r'this\.music\.start\(this\.ctx, this\.inserts\.get\("music"\)', text):
        for sid in ids:
            if sid.startswith("music."):
                out[sid] = "music"
    return out


def read(game_root: Path) -> GameData:
    texts = {k: parse.read_text(game_root / v) for k, v in FILES.items()}
    lst, code = texts["list"], texts["catalog"]
    issues = common.need(lst, LIST_NEEDLES, GAME, FILES["list"])

    ids = parse.ts_string_array(code, "SOUND_IDS")
    buses = code_buses(code, ids)
    code_levels = {m.group(1): {"gain": float(m.group(2)), "duck": float(m.group(3))} for m in BUS_RE.finditer(code)}
    doc_levels, globs = _bus_globs(lst)
    listed = read_list(lst)
    bpm = parse.ts_number_const(texts["music"], "BPM")

    ctx = dict(CONTEXT)
    m = re.search(r"Tiếng lặp nhiều \(([^)]*)\) cần (\d+)–(\d+) biến thể", lst)
    if m:
        ctx["variants"] = [{"ids": parse.backticks(m.group(1)), "min": int(m.group(2)), "max": int(m.group(3)),
                            "basis": f"THEME_SOUND_LIST §2: tiếng lặp nhiều cần {m.group(2)}–{m.group(3)} biến thể"}]
    bars = parse.parse_bars(lst[lst.find("## 2."):lst.find("## 3.")]) or {}
    ctx["music"] = {"bpm": bpm, "bars": bars.get("bars") or 8, "beats_per_bar": 4, "key": "La thứ"}
    ctx["bus_gain"] = {b: v["gain"] for b, v in code_levels.items()}
    ctx["duck_db"] = {b: round(20 * math.log10(v["duck"]), 2) for b, v in code_levels.items()}

    order = ids + [s for s in listed if s not in ids]
    entries: list[Entry] = []
    for sid in order:
        e = Entry(sid, GAME, in_code=sid in ids, in_list=sid in listed and listed[sid].get("section") is not None,
                  code={"bus": buses.get(sid)} if sid in ids else {}, listing=dict(listed.get(sid, {})))
        if sid.startswith("music.") and sid in ids:
            e.code.update({"loop": True, "bpm": bpm, "bars": ctx["music"]["bars"]})
        doc_bus = next((b for b, gl in globs.items() if any(fnmatch.fnmatchcase(sid, g) for g in gl)), None)
        e.listing["bus"] = doc_bus
        entries.append(e)
        if e.in_code and e.in_list:
            if doc_bus and buses.get(sid) and doc_bus != buses[sid]:
                issues.append(Issue(GAME, sid, "bus", f"Bus: mã `{buses[sid]}`, danh sách `{doc_bus}`", DISAGREE, buses[sid], doc_bus))
            if not doc_bus:
                issues.append(Issue(GAME, sid, "bus", "Bảng bus của danh sách không ghi id này", DISAGREE, buses.get(sid), None))
            if not e.listing.get("prompt"):
                issues.append(Issue(GAME, sid, "prompt-missing", "Danh sách có dòng bảng nhưng không có prompt", DISAGREE, None, None))
        if e.in_code and not buses.get(sid):
            issues.append(Issue(GAME, sid, "bus", "Không tìm thấy lời gọi voice() phát id này trong mã", DISAGREE, None, doc_bus))

    # Prose-only ids: named in the list text but neither a table row nor in SOUND_IDS (e.g. kill.chime).
    globbed = {g for gl in globs.values() for g in gl}
    for tok in sorted(set(parse.backticks(lst))):
        if ID_TOKEN.match(tok) and not FILE_EXT.search(tok) and tok not in order and tok not in globbed:
            line = parse.line_of(lst, f"`{tok}`")
            prose = lst.splitlines()[line - 1].strip() if line else ""
            entries.append(Entry(tok, GAME, proposed="THEME_SOUND_LIST: nhắc trong văn bản, chưa có trong bảng và mã",
                                 listing={"section": None, "when": prose, "feel": "", "prompt": None, "bus": "kills" if tok.startswith("kill.") else None}))
            issues.append(Issue(GAME, tok, "prose-only", f"Chỉ nhắc trong văn bản danh sách (dòng {line}); chưa có dòng bảng, prompt hay id trong mã",
                                DISAGREE, False, "prose"))
    for sid, basis in PLAN_PROPOSED.items():
        if all(e.id != sid for e in entries):
            entries.append(Entry(sid, GAME, proposed=basis, listing={"section": None, "when": "", "feel": "", "prompt": None,
                                                                         "bus": PROPOSED_BUS.get(sid, "impacts")}))
            issues.append(Issue(GAME, sid, "plan-only", f"Kế hoạch đề xuất id mới ({basis}); cần thêm vào THEME_SOUND_LIST.md trước", PLAN))

    issues += common.presence_issues(entries, GAME, FILES["catalog"], FILES["list"])
    levels: dict[str, dict] = {}
    for b in sorted(set(code_levels) | set(doc_levels)):
        c, d = code_levels.get(b), doc_levels.get(b)
        levels[b] = {"code": {"gain": c["gain"], "duck": c["duck"]} if c else None,
                     "doc": {"gain": d["gain"], "duck": d["duck"]} if d else None}
    issues += common.bus_level_issues(levels, entries, GAME, FILES["list"], FILES["catalog"])
    for e in entries:
        e.code.setdefault("bus", e.listing.get("bus"))
    return GameData(GAME, LABEL, FILES, entries, issues, levels, ctx, RULES)


def current_randomisation(e: Entry) -> str:
    if e.id == "key.ok":
        return "5 cao độ xoay vòng theo chữ, thêm ±3 % ngẫu nhiên (mã tổng hợp)"
    if e.id.startswith("music."):
        return "Vòng lặp, không đổi ngẫu nhiên"
    return "Tổng hợp trong mã; khi có file, SceneAudio của kit đổi ±5 % tốc độ phát cho mọi âm (§5.3)"
