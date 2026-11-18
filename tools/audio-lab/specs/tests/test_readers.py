"""Readers on a small synthetic game: every kind of catalog/list disagreement is reported."""
from pathlib import Path

from specs.build import build_card
from specs.readers import dragon_hold, typing_survival

CATALOG = """
const def = (bus, priority, lengthMs, file, opts = {}) => ({
  gapMs: opts.gapMs ?? 30,
  vary: opts.vary ?? (bus !== "typing" && bus !== "ui" && bus !== "learning" && bus !== "stingers"),
});
export const SOUNDS = {
  "type.key": def("typing", 2, 60, "sfx/typing/key", { gapMs: 0 }),
  "fire.impact.a": def("dragon", 4, 340, "sfx/dragon/fire-impact-a", { gapMs: 30 }),
  "amb.forest": def("ambience", 5, 6000, "ambience/forest-wind", { loop: true, gainDb: -10 }),
  "only.code": def("ui", 2, 70, "sfx/ui/x"),
};
"""
MIX = """
const LEVELS = {
  music: { gain: 0.5, pronunciationDb: -4 },
  typing: { gain: 0.8, pronunciationDb: -2 },
  dragon: { gain: 0.75, pronunciationDb: -3 },
  ambience: { gain: 0.6, pronunciationDb: -4 },
  ui: { gain: 0.85, pronunciationDb: -3 },
};
"""
MUSIC = """// M0a synthesises Rừng and Đợt
export const MUSIC_LAYERS = ["forest"] as const;
export const SONG = { bpm: 84, beatsPerBar: 4, bars: 8 };
"""
LIST = """# Rồng Giữ Ải
## 1. Tình trạng
- OGG Vorbis, 48 kHz. Tiếng lẻ mono. Nhạc và nền stereo.
- Độ to: giọng −16 LUFS, nhạc −18 LUFS, nền −26 LUFS. Tiếng lẻ chuẩn hóa đỉnh −1 dBTP.
- Đòn trúng nên có 3–6 biến thể. Mã tự đổi cao độ 0,96–1,04, ±1,5 dB, lệch 0–12 ms.
- Đầu file không có khoảng lặng. Tiếng gõ phải bắt đầu ngay (< 20 ms).

## 2. Bus và nhường tiếng

| Bus | Chứa gì | Mức | Khi phát âm từ | Khi thoại | Khi báo đòn tướng, boss |
|---|---|---|---|---|---|
| `music` | Nhạc | 0,50 | −4 dB | −6 dB | −3 dB |
| `typing` | Phím | 0,80 | −2 dB | — | — |
| `dragon` | Rồng | 0,75 | −3 dB | — | −4 dB |
| `ambience` | Gió | 0,45 | −4 dB | −6 dB | −14 dB |
| `ui` | Nút | 0,85 | −3 dB | — | — |

## 4. Nhạc

| Lớp | Khi nào | Mức | Prompt cho file sau |
|---|---|---|---|
| `forest` | Mọi lúc | 0,9 | `Seamless 8-bar loop, 96 BPM, D Dorian, calm` |

## 5. Danh sách âm

### 5.1 Gõ phím (bus `typing`, P2)

| Id | Khi phát | Dài | Cách | Cảm giác | Prompt |
|---|---|---|---|---|---|
| `type.key` | Mỗi phím | 60 | 0 | Gõ gỗ | `Single short wooden knock, under 60 ms` |

### 5.2 Hỏa Long (bus `dragon`)

| Id | Khi phát | Dài | Cách | Bus/P | Cảm giác | Prompt |
|---|---|---|---|---|---|---|
| `fire.impact.a` | Trúng | 300 | 40 | stingers/P3 | Phụt | `Fireball impact, 900 ms` |

### 5.11 Nền (bus `ambience`, P5)

| Id | Khi phát | Dài | Cách | Cảm giác | Prompt |
|---|---|---|---|---|---|
| `amb.forest` | Luôn | lặp 6 s | — | Gió | `Seamless loop, wind, 6 s` |
| `only.list` | Mỗi lúc | 700 | 2500 | Chim | `Bird, 700 ms` |
"""

EMPTY_PLAN = {"batch1": {}, "style_board": {}, "sa3_trial": []}


def _game(tmp_path: Path) -> Path:
    root = tmp_path / "dragon-hold"
    for rel, text in {dragon_hold.FILES["catalog"]: CATALOG, dragon_hold.FILES["mix"]: MIX,
                      dragon_hold.FILES["music"]: MUSIC, dragon_hold.FILES["list"]: LIST}.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text, encoding="utf-8")
    return root


def test_dragon_reader_reports_each_disagreement(tmp_path):
    gd = dragon_hold.read(_game(tmp_path))
    kinds = {(i.id, i.kind) for i in gd.issues}
    assert not [i for i in gd.issues if i.kind == "reader-stale"], gd.issues
    for k in ("length", "gap", "bus", "priority", "prompt-length"):
        assert ("fire.impact.a", k) in kinds, k
    assert ("only.code", "only-code") in kinds
    assert ("only.list", "only-list") in kinds
    assert ("music.forest", "tempo") in kinds
    assert (None, "bus-level") in kinds          # ambience 0.6 in code vs 0,45 in the list
    assert ("type.key", "length") not in kinds and ("amb.forest", "loop") not in kinds
    assert gd.context["bus_gain"]["ambience"] == 0.6


def test_dragon_reader_flags_missing_rule_text(tmp_path):
    root = _game(tmp_path)
    p = root / dragon_hold.FILES["list"]
    p.write_text(LIST.replace("Đòn trúng nên có 3–6 biến thể", "Đòn trúng có biến thể"), encoding="utf-8")
    gd = dragon_hold.read(root)
    assert any(i.kind == "reader-stale" for i in gd.issues)


def test_build_card_applies_game_rules(tmp_path):
    gd = dragon_hold.read(_game(tmp_path))
    e = gd.entry("fire.impact.a")
    card, _ = build_card(gd, e, EMPTY_PLAN, dragon_hold)
    assert card["category"] == "hit-heavy" and card["family"] == "trung"
    assert card["duration"]["target_ms"] == 340 and card["duration"]["min_ms"] == 272
    assert (card["variants"]["min"], card["variants"]["max"]) == (3, 6)      # game doc wins over §4.3.3
    assert card["loudness"]["file"]["metric"] == "peak-dbtp"
    assert card["loudness"]["proposal"]["target"] == -20
    assert card["source_plan"]["now"] == ["cc0-layer", "synth"] and "model-later" in card["source_plan"]["later"]
    assert card["critic"]["group"] == "hit_fire" and card["critic"]["attack_max_ms"] == 10   # fire impact template
    key, _ = build_card(gd, gd.entry("type.key"), EMPTY_PLAN, dragon_hold)
    assert key["onset"]["lead_silence_max_ms"] == 2 and key["critic"]["loop_eval"]["enabled"] is True
    assert key["critic"]["group"] == "key_ok" and key["critic"]["rate_hz"] == 3.333
    amb, _ = build_card(gd, gd.entry("amb.forest"), EMPTY_PLAN, dragon_hold)
    assert amb["playback"]["mode"] == "loop" and amb["playback"]["channels"] == "stereo"
    assert amb["playback"]["min_gap_ms"] is None and amb["loudness"]["file"]["target"] == -26
    odd, issues = build_card(gd, gd.entry("only.list"), EMPTY_PLAN, dragon_hold)
    assert odd["category"] is None and any(i.kind == "unclassified" for i in issues)


def test_build_card_takes_the_game_rhythm_from_the_rule(tmp_path):
    """A reader rule's `repeat` (the game's own rhythm) beats the plan's typical interval for the board and critic."""
    gd = dragon_hold.read(_game(tmp_path))
    gd.rules = [(r"fire\.impact\.a", {"category": "shot", "source": "shot", "repeat": (800, "nhịp của game")})] + gd.rules
    card, _ = build_card(gd, gd.entry("fire.impact.a"), EMPTY_PLAN, dragon_hold)
    assert card["board"]["repeat_interval_ms"] == 800 and card["board"]["repeat_basis"] == "nhịp của game"
    assert card["critic"]["rate_hz"] == 1.25


def test_survival_bus_lookup_from_voice_calls():
    text = '''
export const SOUND_IDS = ["key.ok", "word.load", "word.perfect", "ui.move", "ui.back", "music.calm"] as const;
const v = this.voice("keys", 0, "key.ok");
const w = this.voice("alerts", pan, perfect ? "word.perfect" : "word.load");
const u = this.voice("ui", 0, ("ui." + kind) as SoundId);
this.music.start(this.ctx, this.inserts.get("music")!, this.buffer);
'''
    ids = ["key.ok", "word.load", "word.perfect", "ui.move", "ui.back", "music.calm"]
    assert typing_survival.code_buses(text, ids) == {
        "key.ok": "keys", "word.perfect": "alerts", "word.load": "alerts", "ui.move": "ui", "ui.back": "ui", "music.calm": "music"}


def test_survival_opens_the_s1_spread_and_reads_gun_bus():
    code = '''
export const SOUND_IDS = ["key.ok", "hit.t1", ...GUN_SOUND_IDS] as const;
const GUN_BUS: Readonly<Record<GunSoundId, { bus: Bus; gap: number }>> = {
  "gun.tan.fire": { bus: "guns", gap: 60 },
  "star.get": { bus: "ui", gap: 0 },
};
'''
    guns = 'export const GUN_SOUND_IDS = [\n  "gun.tan.fire",\n  "star.get",\n] as const;'
    assert typing_survival.sound_ids(code, guns) == (["key.ok", "hit.t1", "gun.tan.fire", "star.get"], ["gun.tan.fire", "star.get"])
    assert typing_survival.sound_ids('export const SOUND_IDS = ["key.ok"] as const;', guns) == (["key.ok"], [])
    assert typing_survival.gun_buses(code) == {"gun.tan.fire": {"bus": "guns", "gap_ms": 60.0}, "star.get": {"bus": "ui", "gap_ms": 0.0}}


def test_survival_s1_ids_on_the_real_game_are_in_code_classified_and_on_a_bus():
    """The 14 S1 ids of gun-audio.ts: in SOUND_IDS (spread), a GUN_BUS bus, a RULES row, no reader issue."""
    from common import env
    gd = typing_survival.read(env.GAMES / typing_survival.GAME)
    s1 = [e for e in gd.entries if e.code.get("code_file") == typing_survival.FILES["guns"]]
    assert len(s1) >= 14
    for e in s1:
        assert e.in_code and e.in_list and e.code["bus"] and e.listing.get("prompt"), e.id
        assert (gd.rule_for(e.id) or {}).get("category"), e.id
    assert [i for i in gd.issues if i.id in {e.id for e in s1}] == []
