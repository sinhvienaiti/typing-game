"""Fixed vocabulary of the Listening Board (AUDIO_PIPELINE.md §5.3, §5.4, §7).

One source of truth: the server validates against it and serves it to the page.
"""
from __future__ import annotations

BOARD_VERSION = "1.0.0"
SESSION_SCHEMA = "audiolab.board.session/1"
RATING_SCHEMA = 1          # bump on any incompatible change of a ratings.jsonl line
DEFAULT_ANCHORS = 4        # §7 / §4.6 step 6: re-insert 4-6 earlier pairs per session ("anchors": 0 turns it off)

# §7 fixed tags, in display order, with their keyboard key (KeyboardEvent.code).
# Letters avoid A/B (candidate labels), V (pick), X (drop), I (image), Q/W (reserved).
TAGS: list[tuple[str, str]] = [
    ("hay", "KeyH"),
    ("hợp game", "KeyG"),
    ("chói", "KeyC"),
    ("đục", "KeyD"),
    ("rè/lỗi", "KeyR"),
    ("yếu/mỏng", "KeyY"),
    ("quá dài", "KeyK"),
    ("quá to", "KeyT"),
    ("quá nhỏ", "KeyN"),
    ("chậm", "KeyM"),
    ("sai chất liệu", "KeyS"),
    ("lạc thể loại", "KeyL"),
    ("nhàm khi lặp", "KeyP"),
    ("rẻ tiền", "KeyE"),
    ("khó nghe tiếng đọc", "KeyO"),
]
TAG_NAMES = [t for t, _ in TAGS]

# Listening contexts (§7). "mix" (Trong trận) arrives with board v2, after phase 3.
CONTEXTS = [
    {"key": "alone", "label": "Một mình", "enabled": True},
    {"key": "loop", "label": "Lặp 20 lần", "enabled": True},
    {"key": "small", "label": "Loa nhỏ", "enabled": True, "hint": "Lọc cao 200 Hz"},
    {"key": "mix", "label": "Trong trận", "enabled": False, "hint": "Có từ giai đoạn 3 (Bảng Nghe v2)"},
]
CONTEXT_KEYS = [c["key"] for c in CONTEXTS]
ENABLED_CONTEXTS = [c["key"] for c in CONTEXTS if c["enabled"]]

MODES = {
    "hero": "Chọn âm gốc",
    "variants": "Lượt biến thể",
    "pair": "So cặp",
    "style": "Bảng phong cách",
}

DEVICES = {"headphones": "Tai nghe", "speakers": "Loa"}

# Small-speaker simulation (§2, §6.1 F).
SMALL_SPEAKER_HPF_HZ = 200.0

# "Lặp 20 lần": gameplay rate and per-group randomisation (§5.3).
# interval_ms: mean gap between plays; jitter: +- fraction of the interval;
# cents / db: +- uniform pitch (playbackRate, like the kit) and level; offset_ms: 0..n start
# delay; gap_ms: minimum gap between two plays; avoid: do not repeat the last n variants.
LOOP_COUNT = 20
SPARSE_INTERVAL_MS = 1000  # ours: items played a second or more apart ...
SPARSE_LOOP_COUNT = 8      # ... repeat 8 times, not 20 (a 1.5 s reward x 20 = 30 s per candidate)
KIT_LOOP = {"interval_ms": 400, "jitter": 0.2, "cents": 85, "db": 0.0, "offset_ms": 0,
            "gap_ms": 30, "avoid": 2}       # SceneAudio: playbackRate x U(0.95, 1.05), gap 30 ms
LOOP_PRESETS: dict[str, dict] = {
    "kit": KIT_LOOP,
    "phim-dung": {"interval_ms": 300, "jitter": 0.3, "cents": 50, "db": 1.0, "gap_ms": 30},
    "phim-sai": {"interval_ms": 600, "jitter": 0.3, "cents": 30, "db": 0.0, "gap_ms": 150},
    "ui": {"interval_ms": 900, "jitter": 0.2, "cents": 0, "db": 0.0},
    "thuong-tu": {"interval_ms": 1800, "jitter": 0.2, "cents": 25, "db": 1.0},
    "thuong-hiem": {"interval_ms": 2000, "jitter": 0.1, "cents": 0, "db": 0.0},
    "ban": {"interval_ms": 250, "jitter": 0.1, "cents": 100, "db": 2.0, "gap_ms": 30},
    "trung-nho": {"interval_ms": 250, "jitter": 0.4, "cents": 150, "db": 2.0},
    "trung-nang": {"interval_ms": 700, "jitter": 0.3, "cents": 80, "db": 1.0},
    "no": {"interval_ms": 1200, "jitter": 0.3, "cents": 150, "db": 0.0},
    "chet-bay": {"interval_ms": 150, "jitter": 0.5, "cents": 300, "db": 3.0},
    "chet-lon": {"interval_ms": 1500, "jitter": 0.3, "cents": 80, "db": 1.0},
    "sinh-vat": {"interval_ms": 1500, "jitter": 0.3, "cents": 70, "db": 1.5, "offset_ms": 12},
    "nen": {"interval_ms": 2500, "jitter": 0.0, "cents": 0, "db": 0.0},
}
# The 8 shared families of §4.6 -> default loop preset.
FAMILY_PRESET = {
    "phim-ui": "phim-dung",
    "thuong": "thuong-tu",
    "ban": "ban",
    "trung": "trung-nho",
    "no": "no",
    "chet": "chet-bay",
    "sinh-vat": "sinh-vat",
    "nen": "nen",
}
# Critic group keys (critic/groups.py) -> loop preset, so a session may use the critic's group directly.
CRITIC_GROUP_PRESET = {
    "key_ok": "phim-dung", "key_bad": "phim-sai", "ui": "ui", "reward": "thuong-tu",
    "shot_gun": "ban", "shot_launch": "ban", "hit_small": "trung-nho", "hit_heavy": "trung-nang", "hit_fire": "trung-nang",
    "explosion": "no", "death_swarm": "chet-bay", "death_big": "chet-lon", "creature": "sinh-vat",
    "alarm": "thuong-hiem", "stinger": "thuong-hiem", "ambience": "nen", "music": "nen",
}
# Default listening contexts per family (§7 "Bối cảnh mặc định theo họ âm", before phase 3).
DENSE_FAMILIES = {"phim-ui", "thuong", "ban", "trung", "chet"}


def loop_params(item: dict) -> dict:
    """Resolve loop settings: item.loop > preset (item.loop.preset | group | family) > kit."""
    over = dict(item.get("loop") or {})
    name = over.pop("preset", None) or item.get("group") or FAMILY_PRESET.get(item.get("family") or "")
    name = CRITIC_GROUP_PRESET.get(name, name)
    if name not in LOOP_PRESETS:
        name = FAMILY_PRESET.get(item.get("family") or "", name)
    base = dict(KIT_LOOP)
    if name in LOOP_PRESETS:
        base.update(LOOP_PRESETS[name])
    base.update({k: v for k, v in over.items() if k in KIT_LOOP or k == "count"})
    if "count" not in base:
        base["count"] = SPARSE_LOOP_COUNT if float(base.get("interval_ms") or 0) >= SPARSE_INTERVAL_MS else LOOP_COUNT
    base["preset"] = name if name in LOOP_PRESETS else "kit"
    return base


def default_contexts(item: dict) -> list[str]:
    fam = item.get("family") or ""
    return ["loop", "alone"] if fam in DENSE_FAMILIES or item.get("mode") == "variants" else ["alone", "loop"]


FAMILY_LABELS = {
    "phim-ui": "Phím, UI",
    "thuong": "Thưởng có cao độ",
    "ban": "Bắn, phóng",
    "trung": "Trúng, va chạm",
    "no": "Nổ, bẫy",
    "chet": "Chết quái",
    "sinh-vat": "Sinh vật",
    "nen": "Nền, báo nguy, stinger",
}


def client_config() -> dict:
    return {
        "version": BOARD_VERSION,
        "tags": [{"name": n, "code": c} for n, c in TAGS],
        "contexts": CONTEXTS,
        "modes": MODES,
        "devices": DEVICES,
        "families": FAMILY_LABELS,
        "smallSpeakerHz": SMALL_SPEAKER_HPF_HZ,
    }
