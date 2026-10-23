"""Lời Gọi: docs/audio/THEME_SOUND_LIST.md + code evidence in src/view/audio-min.ts and music.ts.

The game has no id table in code: each sound is a branch of TypingAudio. EVIDENCE maps an id to
the code that plays it, so the generator can tell which listed ids the game really plays.
"""
from __future__ import annotations

import re
from pathlib import Path

from .. import parse
from ..model import DISAGREE, Entry, GameData, Issue
from . import common

GAME = "typing-defense"
LABEL = "Lời Gọi"
FILES = {
    "catalog": "src/view/audio-min.ts",
    "music": "src/view/music.ts",
    "list": "docs/audio/THEME_SOUND_LIST.md",
}

# id -> (file role, regex proving the code plays it, bus in code, caps: {name: regex with one number group})
EVIDENCE: dict[str, tuple[str, str, str, dict[str, str]]] = {
    "call-power": ("catalog", r"kind === 0\)[^\n]*trong\(o,", "typing", {"alerts_per_s": r"ALERTS_PER_S = (\d+)"}),
    "call-build": ("catalog", r"kind === 1\)[^\n]*go\(o,", "typing", {"alerts_per_s": r"ALERTS_PER_S = (\d+)"}),
    "call-harvest": ("catalog", r"kind === 2\)[^\n]*chuong\(o,", "typing", {"alerts_per_s": r"ALERTS_PER_S = (\d+)"}),
    "call-chop": ("catalog", r"kind === 3\)\s*\{\s*go\(o,", "typing", {"alerts_per_s": r"ALERTS_PER_S = (\d+)"}),
    "call-mine": ("catalog", r"kind === 4\)[^\n]*chuong\(o,", "typing", {"alerts_per_s": r"ALERTS_PER_S = (\d+)"}),
    "call-quiz": ("catalog", r"else \[0, 0\.13\]\.forEach\(\(at, k\) => sao\(o,", "typing", {"alerts_per_s": r"ALERTS_PER_S = (\d+)"}),
    "key-right": ("catalog", r"go\(typing, t, 880", "typing", {}),
    "key-wrong": ("catalog", r"KEY\.wrong[^\n]*go\(typing,", "typing", {}),
    "word-hit": ("catalog", r"tranh\(typing,", "typing", {}),
    "word-hit-bell": ("catalog", r"chuong\(typing,", "typing", {}),
    "chain-callout": ("catalog", r"event\.callout\)[^\n]*sao\(typing,", "typing", {}),
    "wordshot-fire": ("catalog", r"PROJECTILE\.wordShot\)\s*\{\s*giay\(world,", "world", {}),
    "arrow-fire": ("catalog", r"PROJECTILE\.arrow && this\.room\(this\.last\.arrow, now, \d+\)\) giay\(world,", "world",
                   {"per_s": r"this\.room\(this\.last\.arrow, now, (\d+)\)"}),
    "blast": ("catalog", r"FX\.burst && blasts\+\+ < \d+\)\s*\{\s*trong\(world,", "world", {"per_frame": r"FX\.burst && blasts\+\+ < (\d+)"}),
    "ink-puff": ("catalog", r"FX\.death && puffs\+\+ < \d+ && this\.room\(this\.last\.puff, now, \d+\)\) giay\(world,", "world",
                 {"per_s": r"this\.room\(this\.last\.puff, now, (\d+)\)", "per_frame": r"puffs\+\+ < (\d+)"}),
    "coin": ("catalog", r"FX\.coin && this\.room\(this\.last\.coin, now, \d+\)\) chuong\(world,", "world",
             {"per_s": r"this\.room\(this\.last\.coin, now, (\d+)\)"}),
    "leak": ("catalog", r"FX\.leak && now - this\.last\.leak > \d+\)", "world", {"min_gap_ms": r"now - this\.last\.leak > (\d+)"}),
    "night-fall": ("catalog", r'event\.phase === "night"\)\s*\{[^}]*trong\(world,', "world", {}),
    "dawn": ("catalog", r'event\.phase === "dawn"\)[^\n]*sao\(world,', "world", {}),
    "defeat": ("catalog", r'event\.t === "defeat"\)\s*\{\s*chuong\(world,', "world", {}),
    "ui-move": ("catalog", r'sound === "move"\) go\(o,', "ui", {}),
    "ui-pick": ("catalog", r'sound === "pick"\)', "ui", {}),
    "ui-off": ("catalog", r'sound === "off"\) go\(o,', "ui", {}),
    "ui-lamp": ("catalog", r'UiSound = [^;]*"lamp"', "ui", {}),
    "amb-villager-call": ("catalog", r"pan\.connect\(this\.out\.world\.to\);\s*goi\(", "world", {}),
    "music-calm": ("music", r"tranh\(calm,", "music", {}),
    "music-tension": ("music", r"trong\(tense,", "music", {}),
}
BUS_NEEDLES = [r"private alert\([^)]*\)[^{]*\{\s*const o = this\.out\.typing", r"ui\(sound: UiSound\): void \{\s*if \(this\.ctx === null\) return;\s*const o = this\.out\.ui"]

LIST_NEEDLES = [
    "Tiếng ngắn đỉnh −1 dBTP; nhạc −18 LUFS; âm nền −26 LUFS",
    "mono cho tiếng ngắn, stereo cho nhạc và âm nền",
    "phải bắt đầu dưới 20 ms và dài dưới 60 ms",
    "Không tôn giáo",
]

CONTEXT = {
    "style_root": "bamboo, wood, bronze, paper, Vietnamese village, dry, outdoor",
    "sweetener": "tre, chuông đồng và đàn tranh",
    "prompt_suffix": None,   # read from the list
    "loudness": {
        "short": {"metric": "peak-dbtp", "target": -1, "basis": "THEME_SOUND_LIST §1: Tiếng ngắn đỉnh −1 dBTP (TK 24.9)"},
        "ambience": {"metric": "lufs-i", "target": -26, "basis": "THEME_SOUND_LIST §1: âm nền −26 LUFS"},
        "music": {"metric": "lufs-i", "target": -18, "basis": "THEME_SOUND_LIST §1: nhạc −18 LUFS"},
    },
    "onset_cap_ms": {"key": 20},
    "onset_basis": "THEME_SOUND_LIST §1: tiếng phím phải bắt đầu dưới 20 ms và dài dưới 60 ms (TK 24.6)",
    "variants": [],
    "stereo": {"categories": ["music", "ambience"], "buses": [], "ids": [],
               "basis": "THEME_SOUND_LIST §1: mono cho tiếng ngắn, stereo cho nhạc và âm nền"},
    "freq_roles": {
        "sub": "Trống, blast",
        "body": "Thân gỗ, thân tre",
        "voice": "Chỉ đầu tiếng rất ngắn",
        "presence": "Tách tre, giấy, ink-puff",
        "pitched": "word-hit đàn tranh theo thang Hò–Xự–Xang–Xê–Cống",
    },
    "per_id_gain": {"default_db": 0.0, "basis": "Mã không có mức riêng cho từng id: nhánh TypingAudio nối thẳng vào bus, mức nằm trong mã tổng hợp. File phát ở 0 dB vào bus"},
    "constraints": [
        "Chất liệu: tre, gỗ, chuông đồng, cồng, giấy, trống cơm, sáo trúc, đàn tranh. Không laser, không tiếng máy, không synth điện tử",
        "Thang ngũ cung Hò, Xự, Xang, Xê, Cống (gần C D F G A); nốt của chữ và nhạc cùng một thang (TK 24.8)",
        "Không tôn giáo (TK 22.1): không chuông chùa, không mõ chùa, không tụng; cồng là cồng hội làng; phách tre thay mõ",
        "Tránh âm Trung Quốc hay Nhật Bản dán nhãn Việt: nhị dẫn giai điệu, shakuhachi, taiko (§8.2)",
    ],
}

BELLS = "Nguồn chuông: không dùng VCSL Hand Bells Nepalese; ứng viên Hand Chimes, Tubular Bells hoặc chuông đồng tự ghi. Chủ dự án duyệt trước lô 1c (§8.2)"
GONG = "Cồng là cồng hội làng, chỉ cho lúc trang trọng hoặc báo nguy; VCSL Gong 1/2 chưa rõ loại. Chủ dự án duyệt (§8.2)"
SAO = "Sáo trúc Việt Nam không có màng rung, không để tiếng \"rè màng\" (§8.2)"
LOCKED_KEY = {"ranked": [(["synth"], "Giữ tổng hợp bằng mã, không làm bằng AI (TK 24.6); chỉnh tham số bằng bản dựng không chạy game")],
              "now": ["synth"], "later": []}

RULES: list[tuple[str, dict]] = [
    (r"call-power", {"category": "fx-other", "source": "folk-instrument", "family": "phim-ui",
                     "constraints": ["Trống cơm có hai mặt, thường lên dây cách nhau khoảng một quãng năm (§8.2)"]}),
    (r"call-(build|chop|mine)", {"category": "fx-other", "source": "impact", "family": "phim-ui"}),
    (r"call-harvest", {"category": "fx-other", "source": "pitched-reward", "family": "thuong", "blocked_by": ["chu-du-an-duyet"], "constraints": [BELLS]}),
    (r"call-quiz", {"category": "fx-other", "source": "folk-flute", "family": "thuong", "constraints": [SAO]}),
    (r"key-right", {"category": "key-ok", "source": "key", "source_override": LOCKED_KEY}),
    (r"key-wrong", {"category": "key-bad", "source": "key", "source_override": LOCKED_KEY}),
    (r"word-hit", {"category": "word-reward", "source": "folk-instrument", "blocked_by": ["chu-du-an-duyet"],
                   "variants": {"min": 7, "max": 7, "basis": "6 nốt và 1 bản vuốt lên: mỗi nốt một file (THEME_SOUND_LIST §2, §9 #21)"},
                   "source_override": {"ranked": [(["sample-player"], "VCSL Dan Tranh (Normal và Gliss) qua bộ phát mẫu Python, dời tối đa 3 bán cung (§9 #21)"),
                                                  (["owner-recording"], "Tự ghi đàn tranh"), (["synth"], "Tổng hợp như hiện nay")],
                                       "now": ["sample-player"], "later": []},
                   "pitch_proposal": {"notes": ["C4", "D4", "F4", "G4", "A4", "C5"],
                                      "basis": "AUDIO_PIPELINE §8.2, §16 #4: hạ một quãng tám thành C4–C5 vì mẫu VCSL chỉ có B1–B4 (chờ chủ dự án duyệt)"},
                   "constraints": ["Đàn tranh có luyến láy bằng tay trái (§8.2)", "Bản vuốt lên lấy từ thư mục Gliss của VCSL (§8.2)"]}),
    (r"word-hit-bell", {"category": "word-reward", "source": "pitched-reward", "rand": "rare-fixed", "blocked_by": ["chu-du-an-duyet"], "constraints": [BELLS]}),
    (r"chain-callout", {"category": "word-reward", "source": "folk-flute", "rand": "rare-fixed", "constraints": [SAO]}),
    (r"wordshot-fire", {"category": "shot", "source": "shot"}),
    (r"arrow-fire", {"category": "shot", "source": "shot", "constraints": ["Hoặc tự ghi tiếng dây cung tre (§9 #24)"]}),
    (r"blast", {"category": "blast", "source": "blast", "dirty": False,
                "constraints": ["Trống và giấy, không nổ lách tách (§3.2)", "VCSL Frame Drum hoặc Timpani cộng giấy bung (§9 #26)"]}),
    (r"ink-puff", {"category": "death-swarm", "source": "foley-other", "dirty": False, "constraints": ["Mềm, không máu (THEME_SOUND_LIST)"]}),
    (r"coin", {"category": "fx-other", "source": "ui", "family": "thuong", "add_bands": ["pitched"], "blocked_by": ["chu-du-an-duyet"],
               "constraints": ["Kenney RPG cộng VCSL Hand Chimes (§9 #27)", BELLS]}),
    (r"leak", {"category": "warning", "source": "warning-stinger", "blocked_by": ["chu-du-an-duyet"],
               "constraints": [GONG, "Báo động dùng kẻng sắt hoặc trống hội, không dùng mõ; VCSL Anvil hoặc Brake Drum cho tiếng kẻng (§8.2)"]}),
    (r"night-fall", {"category": "stinger", "source": "warning-stinger", "blocked_by": ["chu-du-an-duyet"], "constraints": [GONG]}),
    (r"dawn", {"category": "stinger", "source": "folk-flute", "constraints": [SAO, "Thắng, sáng: điệu Bắc (gợi ý, chờ chủ dự án duyệt) (§8.2)"]}),
    (r"defeat", {"category": "stinger", "source": "warning-stinger", "blocked_by": ["chu-du-an-duyet"],
                 "constraints": [GONG, SAO, "Thua: điệu Nam hoặc Oán (gợi ý, chờ duyệt); tránh âm hưởng kèn đám ma (§8.2)"]}),
    (r"ui-[\w]+", {"category": "ui", "source": "ui"}),
    (r"amb-villager-call", {"category": "fx-other", "source": "voice", "family": "nen", "onset": "none",
                            "constraints": ["Không dùng AI (§3.2)", "Chỉ tiếng \"Ơ… ơi!\", không lời khác"]}),
    (r"amb-[\w-]+", {"category": "ambience", "source": "ambience"}),
    (r"music-stingers", {"category": "stinger", "source": "music", "blocked_by": ["chu-du-an-duyet"],
                         "parts": [{"name": "dau-dem", "note": "Đầu đêm"}, {"name": "het-dem", "note": "Hết đêm"},
                                   {"name": "nha-moi", "note": "Mở nhà mới"}, {"name": "chuoi-20", "note": "Mốc Chuỗi 20"},
                                   {"name": "chuoi-40", "note": "Mốc Chuỗi 40"}],
                         "constraints": ["Chủ dự án ký duyệt từng stem nhạc và từng âm có cồng (§8.2)"]}),
    (r"music-[\w]+", {"category": "music", "source": "music", "blocked_by": ["chu-du-an-duyet"],
                      "constraints": ["Chủ dự án ký duyệt từng stem nhạc và từng âm có cồng (§8.2)"]}),
]


def read_list(text: str) -> dict[str, dict]:
    sounds: dict[str, dict] = {}
    for t in parse.md_tables(text):
        if t.header[0] != "Id":
            continue
        sec_bus = re.search(r"bus `(\w+)`", t.heading)
        for row, line in zip(t.rows, t.row_lines):
            ids = parse.backticks(row["Id"])
            if not ids:
                continue
            sounds[ids[0]] = {"section": t.heading, "bus": sec_bus.group(1) if sec_bus else None,
                              "when": row.get("Khi nào", ""), "feel": row.get("Không khí", ""),
                              "current": row.get("Hiện tại (mã)", ""), "prompt": row.get("Prompt cho file thật", ""), "line": line}
    return sounds


def read(game_root: Path) -> GameData:
    texts = {k: parse.read_text(game_root / v) for k, v in FILES.items()}
    lst = texts["list"]
    issues = common.need(lst, LIST_NEEDLES, GAME, FILES["list"])
    for rx in BUS_NEEDLES:
        if not re.search(rx, texts["catalog"]):
            issues.append(Issue(GAME, None, "reader-stale", f"Không thấy mẫu bus `{rx}` trong {FILES['catalog']}: kiểm lại EVIDENCE", "stale"))

    listed = read_list(lst)
    code: dict[str, dict] = {}
    for sid, (role, rx, bus, caps) in EVIDENCE.items():
        if re.search(rx, texts[role]):
            found = {}
            for name, crx in caps.items():
                m = re.search(crx, texts[role])
                if m:
                    found[name] = float(m.group(1))
            code[sid] = {"bus": bus, "caps": found, "code_file": FILES[role]}
    bpm_m = re.search(r"EIGHTH = 60 / (\d+) / 2", texts["music"])
    bpm = float(bpm_m.group(1)) if bpm_m else None
    for sid in ("music-calm", "music-tension"):
        if sid in code:
            code[sid].update({"loop": True, "bpm": bpm})

    ctx = dict(CONTEXT)
    m = re.search(r'đuôi chung: \*"(.+?)"\*', lst)
    ctx["prompt_suffix"] = m.group(1) if m else None
    if m and "no music" in m.group(1):
        issues.append(Issue(GAME, None, "prompt-suffix",
                            "Đuôi prompt chung có \"no music, no speech\" nhưng §1 bảo ghép cho mọi prompt: bộ sinh chỉ ghép cho tiếng lẻ, "
                            "không ghép cho nhạc, nền lặp và giọng người (amb-villager-call); nên sửa câu ở §1", DISAGREE))
    if not m:
        issues.append(Issue(GAME, None, "reader-stale", "Không thấy đuôi prompt chung ở §1", "stale"))
    ctx["music"] = {"bpm": bpm, "bars": 16, "beats_per_bar": 4, "key": "ngũ cung Hò–Xự–Xang–Xê–Cống"}
    ctx["bus_gain"] = {}
    wm = re.search(r"this\.out\.world = \{ ctx, to: new GainNode\(ctx, \{ gain: ([\d.]+) \}\) \}", texts["catalog"])
    if wm and re.search(r"this\.out\.ui = \{ ctx, to: this\.sfx \}", texts["catalog"]) and re.search(r"typing\.connect\(this\.sfx\)", texts["catalog"]):
        ctx["bus_gain"] = {"typing": 1.0, "world": float(wm.group(1)), "ui": 1.0, "music": 1.0}
    else:
        issues.append(Issue(GAME, None, "reader-stale", "Không đọc được mức bus trong audio-min.ts", "stale"))
    ctx["duck_db"] = {"music": -9.0}

    entries: list[Entry] = []
    for sid in list(listed) + [s for s in code if s not in listed]:
        e = Entry(sid, GAME, in_code=sid in code, in_list=sid in listed, code=dict(code.get(sid, {})), listing=dict(listed.get(sid, {})))
        entries.append(e)
        li, c = e.listing, e.code
        if not (e.in_code and e.in_list):
            continue
        if li.get("bus") and c.get("bus") and li["bus"] != c["bus"]:
            issues.append(Issue(GAME, sid, "bus", f"Bus: mã `{c['bus']}`, danh sách `{li['bus']}`", DISAGREE, c["bus"], li["bus"]))
        if not li.get("bus"):
            issues.append(Issue(GAME, sid, "bus", f"Danh sách không ghi bus (mục \"{li.get('section')}\"); mã phát qua `{c['bus']}`", DISAGREE, c["bus"], None))
        doc_caps = parse.parse_caps(li.get("when", ""))
        for name, val in doc_caps.items():
            have = c.get("caps", {}).get(name)
            if have is not None and abs(have - val) > 0.5:
                issues.append(Issue(GAME, sid, "cap", f"Trần {name}: mã {have:g}, danh sách {val:g}", DISAGREE, have, val))
            elif have is None and name != "per_frame":
                issues.append(Issue(GAME, sid, "cap", f"Danh sách ghi trần {name} = {val:g}, không thấy trong mã", DISAGREE, None, val))
        if sid.startswith("music-") and bpm:
            bars = parse.parse_bars(li.get("prompt", "")) or {}
            if bars.get("bpm") and bars["bpm"] != bpm:
                issues.append(Issue(GAME, sid, "tempo", f"Prompt ghi {bars['bpm']:g} BPM, mã {bpm:g} BPM", DISAGREE, bpm, bars["bpm"]))
    issues += common.presence_issues(entries, GAME, FILES["catalog"] + " / " + FILES["music"], FILES["list"])
    issues.append(Issue(GAME, None, "no-catalog",
                        "Mã không có bảng id âm (như SOUND_IDS của Tuyến Cuối): bộ sinh dò từng nhánh của TypingAudio bằng EVIDENCE; "
                        "đề xuất thêm một danh sách id vào mã khi làm bộ tải file (§6.3 #6)", "info"))
    for e in entries:
        e.code.setdefault("bus", e.listing.get("bus"))
    return GameData(GAME, LABEL, FILES, entries, issues, {}, ctx, RULES)


def current_randomisation(e: Entry) -> str:
    if e.id == "key-right":
        return "Cao lên một bán cung mỗi chữ, tối đa 12 (mã tổng hợp); không ngẫu nhiên"
    if e.id == "word-hit":
        return "Nốt theo bậc Chuỗi trên ngũ cung; Chớp có vuốt lên; Ẩu thấp một bậc (mã tổng hợp)"
    if e.id.startswith("music-"):
        return "Mã chọn ngẫu nhiên hình đàn tranh mỗi ô nhịp; file nhạc thì không đổi ngẫu nhiên"
    return "Tổng hợp trong mã; game chưa có bộ tải file (§6.3 #6)"
