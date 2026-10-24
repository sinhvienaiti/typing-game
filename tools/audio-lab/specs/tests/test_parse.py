from specs import parse


def test_vn_number():
    assert parse.vn_number("0,50") == 0.5
    assert parse.vn_number("−4 dB") == -4.0
    assert parse.vn_number("10_000") == 10000.0
    assert parse.vn_number("không hạ") is None


def test_md_tables_keep_heading_path():
    text = "# A\n## 5. List\n### 5.1 Keys (bus `typing`, P2)\n\n| Id | Dài |\n|---|---|\n| `type.key` | 60 |\n| `type.miss` | 60 |\n"
    (t,) = parse.md_tables(text)
    assert t.heading.startswith("5.1 Keys")
    assert t.heading_path == ["A", "5. List", "5.1 Keys (bus `typing`, P2)"]
    assert [r["Id"] for r in t.rows] == ["`type.key`", "`type.miss`"]
    assert t.row_lines == [7, 8]


def test_parse_duration_kinds():
    assert parse.parse_duration("dry, very fast attack, under 60 ms, no reverb") == {"ms": 60.0, "kind": "max"}
    assert parse.parse_duration("Two tiny clinks, 0.06 s apart, 0.3 s total.") == {"ms": 300.0, "kind": "total"}
    assert parse.parse_duration("bamboo creaking softly, seamless loop 60 s, stereo.")["ms"] == 60000.0
    assert parse.parse_duration("Seamless loop, wind through a misty pine forest, soft gusts, no birds, 6 s")["ms"] == 6000.0
    d = parse.parse_duration("Five short stingers 2–5 s in the same key")
    assert d["kind"] == "range" and d["min_ms"] == 2000 and d["max_ms"] == 5000
    assert parse.parse_duration("dry, tight, very short (40 ms), industrial") == {"ms": 40.0, "kind": "exact"}
    assert parse.parse_duration("Exhausted dragon long falling groan, 1.6 s")["ms"] == 1600.0
    assert parse.parse_duration("no length here") is None


def test_bars_pitches_variants_caps():
    assert parse.parse_bars("84 BPM, 16 bars, seamless loop") == {"bpm": 84.0, "bars": 16}
    assert parse.parse_bars("Seamless 8-bar loop, 84 BPM") == {"bpm": 84.0, "bars": 8}
    assert parse.bars_ms(96, 8) == 20000.0
    assert parse.parse_pitches("one file per pitch C5, D5, F5, G5, A5, C6") == ["C5", "D5", "F5", "G5", "A5", "C6"]
    assert parse.parse_variant_count("1.5 s. Make 4 variants (two men, two women).") == 4
    assert parse.parse_caps("Tháp Cung bắn (tối đa 4 lần mỗi giây)") == {"per_s": 4}
    assert parse.parse_caps("Vụ nổ, tối đa 2 mỗi khung") == {"per_frame": 2}
    assert parse.parse_caps("Quái lọt vào Lũy (cách nhau ít nhất 0,8 s)") == {"min_gap_ms": 800.0}
    assert parse.parse_caps("tối đa một tiếng mỗi 420 ms") == {"min_gap_ms": 420.0}


def test_ts_helpers():
    text = 'export const SOUND_IDS = [\n  "key.ok",\n  "key.bad",\n] as const;\nconst BPM = 96;\n'
    assert parse.ts_string_array(text, "SOUND_IDS") == ["key.ok", "key.bad"]
    assert parse.ts_number_const(text, "BPM") == 96.0
