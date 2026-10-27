"""Sound groups (§4.3.3 rows), families (§4.6 step 4) and L2 ranking targets.

A Target is a trapezoid: desirability 1 inside `good`, 0 outside `bad`, linear between.
`None` on one side means open-ended. Numbers are starting points (§4.3.3), replaced by
P10-P90 of approved refs once a group has >= 5 of them.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

INF = float("inf")

# §4.6 step 4: eight shared families (+ music), slug -> Vietnamese name.
FAMILIES = {
    "phim-ui": "Phím và UI ngắn",
    "thuong": "Thưởng có cao độ",
    "ban": "Bắn, phóng",
    "trung": "Trúng, va chạm",
    "no": "Nổ, bẫy",
    "chet": "Chết quái",
    "sinh-vat": "Sinh vật",
    "nen": "Nền, báo nguy, stinger",
    "nhac": "Nhạc",
    "khac": "Khác",
}


@dataclass(frozen=True)
class Target:
    feature: str
    good: tuple[float, float]
    bad: tuple[float, float]
    weight: float = 1.0
    low_vi: str = ""      # note when the value is too low
    high_vi: str = ""     # note when the value is too high

    def desirability(self, v: float | None) -> float | None:
        if v is None or v != v:
            return None
        glo, ghi = self.good
        blo, bhi = self.bad
        if glo <= v <= ghi:
            return 1.0
        if v < glo:
            return 0.0 if v <= blo or glo == -INF else float((v - blo) / (glo - blo))
        return 0.0 if v >= bhi or ghi == INF else float((bhi - v) / (bhi - ghi))


def at_least(feature, good, bad, w=1.0, low_vi="", high_vi=""):
    return Target(feature, (good, INF), (bad, INF), w, low_vi, high_vi)


def at_most(feature, good, bad, w=1.0, low_vi="", high_vi=""):
    return Target(feature, (-INF, good), (-INF, bad), w, low_vi, high_vi)


def between(feature, lo, hi, tol=0.2, w=1.0, low_vi="", high_vi=""):
    return Target(feature, (lo, hi), (lo * (1 - tol), hi * (1 + tol)), w, low_vi, high_vi)


@dataclass(frozen=True)
class Group:
    key: str
    name_vi: str
    family: str
    dur_ms: tuple[float, float] | None
    attack_max_ms: float | None          # §4.3.1 L1 attack; None = not checked
    head_max_ms: float | None            # §4.3.1 L1 head silence; None = not checked (loops)
    percussive: bool = True              # pre-echo, punch, transient features make sense
    loop: bool = False
    stereo_ok: bool = False              # §4.3.1: mono except music, ambience, end stinger
    dirty: bool = False                  # §4.4 "bẩn có chủ ý"
    pitched: bool = False
    meter: str = "M"                     # loudness reference: M (momentary), S (short-term), I
    rate_hz: float = 3.0                 # game rhythm for the 3-4 s repetition (§4.4)
    targets: tuple[Target, ...] = field(default_factory=tuple)


# Notes in sound-design language (§4.5), Vietnamese.
CREST = at_least("crest_db", 12, 6, 1.0, "ít độ nảy (crest thấp, bị nén)")
PUNCH = at_least("punch_db", 6, 0, 1.0, "thiếu lực ở 20 ms đầu")
BODY = at_least("tail_ms", 40, 10, 1.0, "không có thân, tắt quá nhanh")
MUD = at_most("mud_share", 0.25, 0.45, 1.0, high_vi="thừa ù ở 200–500 Hz")
CRACK = at_least("transient_hf_share_db", -15, -30, 1.0, "thiếu lớp tách trên 2 kHz ở đầu tiếng")
SPEAKER = at_most("speaker_loss_db", 6, 12, 0.5, high_vi="mất nhiều trên loa nhỏ (lọc 200 Hz)")
WEIGHT = at_least("share_below_300", 0.25, 0.08, 1.0, "thiếu thân trầm dưới 300 Hz (mỏng)")   # ours, for heavy sounds


def _attack(limit, w=1.0):
    # graded below the L1 limit: a snappier onset ranks higher within the group
    return at_most("attack_ms", limit / 4, limit, w, high_vi="đầu tiếng chậm")


def _snap(good, bad, w=1.0):
    # rise of the >= 2 kHz crack layer (features.hf_attack); smeared model onsets rise slowly
    return at_most("hf_attack_ms", good, bad, w, high_vi="lớp tách đầu tiếng lên chậm (nhòe)")


def _dur(lo, hi, w=1.0):
    return between("duration_ms", lo, hi, 0.2, w, "ngắn hơn khoảng của nhóm", "dài hơn khoảng của nhóm")


def _g(key, name_vi, family, dur, attack, head, targets=(), **kw):
    t = ((_dur(*dur),) if dur else ()) + ((_attack(attack),) if attack else ()) + tuple(targets)
    return Group(key, name_vi, family, dur, attack, head, targets=t, **kw)


GROUPS: dict[str, Group] = {g.key: g for g in (
    _g("key_ok", "Phím đúng", "phim-ui", (15, 60), 3, 2, (
        at_most("key_1k4k_vs_4k8k_db", -6, 0, 1.5, high_vi="dải 1–4 kHz chưa thấp hơn dải 4–8 kHz 6 dB"),
        _snap(1.0, 3.0), SPEAKER), rate_hz=6.0),
    _g("key_bad", "Phím sai", "phim-ui", (60, 150), 3, 2, (
        at_least("share_150_600", 0.35, 0.10, 1.5, "ít năng lượng ở 150–600 Hz"),
        at_most("above3k_vs_150_600_db", -20, -8, 1.5, high_vi="phần trên 3 kHz chưa thấp hơn 20 dB"),
        SPEAKER), rate_hz=3.0),
    _g("ui", "UI", "phim-ui", (10, 250), 3, 2, (
        at_least("share_1k_5k", 0.35, 0.10, 1.5, "ít năng lượng ở 1–5 kHz"), SPEAKER), rate_hz=2.0),
    _g("reward", "Thưởng xong từ", "thuong", (150, 900), None, 5, (
        at_least("voice_drop_db", 15, 5, 1.5, "dải 1–4 kHz chưa giảm 15 dB trong 100 ms (che tiếng đọc)"),
        at_most("pitch_off_cents", 10, 30, 1.0, high_vi="nốt lệch thang quá 10 cent")),
        percussive=False, pitched=True, rate_hz=1.5),
    _g("shot_gun", "Bắn (súng)", "ban", (80, 350), 10, 5, (
        at_least("share_below_150", 0.25, 0.08, 1.5, "thiếu thân trầm dưới 150 Hz"), CREST, PUNCH, MUD,
        _snap(2.0, 8.0)), dirty=True, rate_hz=5.0),
    _g("shot_launch", "Khạc, phóng", "ban", (80, 350), 10, 5, (
        at_most("share_below_120", 0.063, 0.25, 1.5, high_vi="dưới 120 Hz chưa thấp hơn 12 dB"), MUD,
        # ours: a floor for the body, so a thin copy (nothing under 1 kHz) cannot pass every target
        at_least("share_150_800", 0.12, 0.03, 1.0, "thiếu thân 150–800 Hz (mỏng)")),
        rate_hz=4.0),
    _g("hit_small", "Trúng nhỏ", "trung", (50, 150), 10, 5, (
        at_least("onset_2k6k_share", 0.25, 0.05, 1.5, "thiếu lớp tách 2–6 kHz ở đầu tiếng"),
        at_least("share_200_800", 0.25, 0.08, 1.5, "thiếu thân 200–800 Hz"),
        CREST, PUNCH, BODY, MUD, _snap(2.0, 8.0)), rate_hz=5.0),
    _g("hit_heavy", "Trúng vừa, nặng", "trung", (120, 600), 10, 5, (
        at_least("share_sub_40_90", 0.08, 0.01, 1.5, "thiếu sub 40–90 Hz"),
        at_most("sub_len_ms", 150, 300, 1.0, high_vi="sub kéo dài quá 150 ms"),
        WEIGHT, CREST, PUNCH, BODY, MUD, CRACK, _snap(2.0, 8.0)), rate_hz=2.0),
    # ours: a fire impact is a low "whoomph" with a round body (Rồng Giữ Ải fire.impact.*: "phụt lửa
    # trầm, thân tròn"); no 2 kHz crack is wanted and late ember crackle is tail, so no CRACK/_snap.
    _g("hit_fire", "Trúng lửa trầm", "trung", (120, 600), 10, 5, (
        at_least("share_sub_40_90", 0.08, 0.01, 1.5, "thiếu sub 40–90 Hz"),
        at_most("sub_len_ms", 150, 300, 1.0, high_vi="sub kéo dài quá 150 ms"),
        WEIGHT, PUNCH, BODY, at_least("crest_db", 9, 4, 0.5, "ít độ nảy (crest thấp, bị nén)"),
        at_most("mud_share", 0.35, 0.55, 0.5, high_vi="thừa ù ở 200–500 Hz")),
        dirty=True, rate_hz=2.0),
    _g("explosion", "Nổ", "no", (600, 2000), 10, 5, (
        at_least("crack_2k8k_share_30ms", 0.20, 0.05, 1.5, "thiếu tiếng nứt 2–8 kHz trong 30 ms đầu"),
        at_most("sub_len_ms", 300, 600, 1.0, high_vi="sub kéo dài quá 300 ms"), WEIGHT, PUNCH, MUD),
        dirty=True, meter="S", rate_hz=1.0),
    _g("death_swarm", "Chết bầy", "chet", (80, 200), None, 5, (
        at_least("share_above_500", 0.6, 0.3, 1.5, "thiếu dải giữa và cao"),
        at_most("share_below_150", 0.15, 0.35, 1.0, high_vi="quá nặng ở dải trầm"), MUD),
        dirty=True, rate_hz=8.0),
    _g("death_big", "Chết lớn", "chet", (400, 900), None, 5, (
        at_least("share_60_150", 0.15, 0.03, 1.5, "thiếu tiếng thịch 60–150 Hz"), WEIGHT, MUD), rate_hz=1.0),
    _g("creature", "Tiếng sinh vật", "sinh-vat", (200, 1600), 30, 15, (), percussive=False, rate_hz=1.0),
    _g("alarm", "Báo nguy", "nen", (250, 2000), None, 5, (
        at_most("sustain_1k4k_ms", 100, 400, 1.5, high_vi="ngân dài ở 1–4 kHz (che tiếng đọc)"), SPEAKER),
        percussive=False, rate_hz=0.5),
    _g("ambience", "Nền lặp", "nen", None, None, None, (
        at_least("share_low300_hi4k10k", 0.7, 0.4, 1.5, "nhiều năng lượng ở 300 Hz–4 kHz"),
        at_most("lufs_m_range_db", 4, 8, 1.0, high_vi="độ to dao động trong vòng lặp")),
        percussive=False, loop=True, stereo_ok=True, meter="I", rate_hz=0.0),
    _g("music", "Nhạc", "nhac", None, None, None, (), percussive=False, loop=True, stereo_ok=True,
       meter="I", rate_hz=0.0),
    _g("stinger", "Stinger", "nen", (1000, 3600), None, 5, (), percussive=False, stereo_ok=True,
       meter="S", rate_hz=0.0),
    _g("whoosh", "Tiếng vút, luồng lửa", "ban", (200, 4000), None, 5, (MUD,), percussive=False,
       dirty=True, rate_hz=1.0),
    # §4.3.1 times the rise only for keys/UI, hits/shots/blasts and creatures: none here
    _g("generic", "Chung", "khac", None, None, 5, (MUD,), rate_hz=3.0),
)}

# Fallback id -> group when a spec card does not name a group (order matters).
ID_PATTERNS: list[tuple[str, str]] = [
    (r"^(key\.ok|type\.key|key-right)\b", "key_ok"),
    (r"^(key\.bad|type\.miss|key-wrong)\b", "key_bad"),
    (r"^ui[.-]", "ui"),
    (r"^(word\.load|word\.perfect|type\.word|word-hit|fire\.cast|kill\.chime|learn\.)", "reward"),
    (r"^(arrow-fire|wordshot-fire)", "shot_launch"),
    (r"^gun\.", "shot_gun"),
    (r"^(hit\.t1|enemy\..+\.hit)", "hit_small"),
    (r"^fire\.impact", "hit_fire"),
    (r"^hit\.", "hit_heavy"),
    (r"^(blast|trap\..+\.trigger|.+\.skyfire\.impact)", "explosion"),
    (r"^(kill\.swarm|enemy\.swarm\.death|ink-puff)", "death_swarm"),
    (r"^(kill\.elite|enemy\..+\.death)", "death_big"),
    (r"(\.spawn$|^dragon\.(hurt|roar))", "creature"),
    (r"^(warn\.|alarm\.|leak)", "alarm"),
    (r"^(amb[.-]|.+\.march$)", "ambience"),
    (r"^(end\.|stinger\.|wave\.horn)", "stinger"),
    (r"^(music\.|forest$|wave$)", "music"),
    (r"^dragon\.breath", "whoosh"),
]


def infer_group(sound_id: str | None) -> str | None:
    if not sound_id:
        return None
    sid = sound_id.lower()
    for pat, key in ID_PATTERNS:
        if re.search(pat, sid):
            return key
    return None


def get(key: str) -> Group:
    if key not in GROUPS:
        raise KeyError(f"nhóm '{key}' không có; chọn một trong: {', '.join(GROUPS)}")
    return GROUPS[key]
