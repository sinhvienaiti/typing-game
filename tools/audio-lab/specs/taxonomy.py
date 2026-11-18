"""Plan tables as data (docs/games/AUDIO_PIPELINE.md). Other lanes import this.

Section numbers refer to AUDIO_PIPELINE.md. Game documents win over these numbers;
the readers in specs/readers apply game rules on top (see build.py).
"""
from __future__ import annotations

PLAN_DOC = "docs/games/AUDIO_PIPELINE.md"

# ── §4.6 eight shared families (plus music, rated by test J, not by the family model) ──
FAMILIES: dict[str, str] = {
    "phim-ui": "Phím và UI ngắn",
    "thuong": "Thưởng có cao độ",
    "ban": "Bắn, phóng",
    "trung": "Trúng, va chạm",
    "no": "Nổ, bẫy",
    "chet": "Chết quái",
    "sinh-vat": "Sinh vật",
    "nen": "Nền, báo nguy, stinger",
    "nhac": "Nhạc (ngoài 8 họ của §4.6; kiểm bằng bài J)",
}

# ── §4.3.1 onset classes: rise 10–90 % and lead silence (ms) ──
ONSET_CLASSES: dict[str, dict] = {
    "key": {"label": "Phím", "rise_max_ms": 3, "lead_silence_max_ms": 2},
    "ui": {"label": "UI", "rise_max_ms": 3, "lead_silence_max_ms": 2},
    "impact": {"label": "Trúng, bắn, nổ", "rise_max_ms": 10, "lead_silence_max_ms": 5},
    # §4.3.1 times the rise only for keys/UI, hits/shots/blasts and creatures; everything else
    # (rewards, alarms, stingers, monster deaths, other) keeps the head-silence limit only.
    "other": {"label": "Còn lại (thưởng, báo nguy, stinger, chết quái, khác): không kiểm thời gian lên",
              "rise_max_ms": None, "lead_silence_max_ms": 5},
    "creature": {"label": "Sinh vật", "rise_max_ms": 30, "lead_silence_max_ms": 15},
    "none": {"label": "Tiếng vút, dâng, nền: không kiểm thời gian lên", "rise_max_ms": None, "lead_silence_max_ms": 5},
    "loop": {"label": "Vòng lặp: không kiểm đầu tiếng, kiểm mối nối", "rise_max_ms": None, "lead_silence_max_ms": None},
}
ONSET_BASIS = "AUDIO_PIPELINE §4.3.1 (thời gian lên, im lặng ở đầu)"

# ── §4.3.3 L2 groups. mix = level in the mix (tests A/B), not the per-file target ──
CATEGORIES: dict[str, dict] = {
    "key-ok": {
        "label": "Phím đúng", "duration_ms": [15, 60], "variants": [6, 10],
        "mix": {"metric": "lufs-m-max", "range": [-28, -24]},
        "spectrum": "Đề xuất mới (§6.2): tiếng tách chủ yếu trên 4 kHz, thân dưới 800 Hz, dải 1–4 kHz thấp hơn dải 4–8 kHz ít nhất 6 dB. Tài liệu game thắng cho đến khi sửa",
        "rand": "key-ok", "onset": "key", "family": "phim-ui", "dense": True,
        "bands": ["presence", "body"], "voice_band": "onset-only",
    },
    "key-bad": {
        "label": "Phím sai", "duration_ms": [60, 150], "variants": [2, 3],
        "mix": {"metric": "lufs-m-max", "range": None, "text": "Nhỏ hơn phím đúng ít nhất 3 dB"},
        "spectrum": "Năng lượng ở 150–600 Hz. Phần trên 3 kHz thấp hơn ít nhất 20 dB",
        "rand": "key-bad", "onset": "key", "family": "phim-ui", "dense": True,
        "bands": ["body"], "voice_band": "avoid",
    },
    "ui": {
        "label": "UI", "duration_ms": [10, 250], "variants": [1, 3],
        "mix": {"metric": "lufs-m-max", "range": [-30, -22], "text": "Không to hơn phím"},
        "spectrum": "1–5 kHz, mềm",
        "rand": "rare-fixed", "onset": "ui", "family": "phim-ui", "dense": False,
        "bands": ["voice", "presence"], "voice_band": "soft-short",
    },
    "word-reward": {
        "label": "Thưởng xong từ", "duration_ms": [150, 900], "variants": [1, 3],
        "mix": {"metric": "lufs-m-max", "range": [-22, -16], "text": "Từ −22 (bậc C) đến −16 (bậc S)"},
        "spectrum": "Nốt đúng thang, lệch không quá 10 cent. Năng lượng 1–4 kHz giảm ít nhất 15 dB trong 100 ms sau đầu tiếng (§6.2)",
        "rand": "word-reward", "onset": "other", "family": "thuong", "dense": True,
        "bands": ["pitched"], "voice_band": "decay-15db-100ms",
    },
    "shot": {
        "label": "Bắn, khạc", "duration_ms": [80, 350], "variants": [4, 6],
        "mix": {"metric": "lufs-m-max", "range": [-24, -18]},
        "spectrum": "Súng: từ 25 % năng lượng dưới 150 Hz, crest từ 12 dB. Khạc hoặc phóng: dưới 120 Hz thấp hơn ít nhất 12 dB",
        "rand": "shot", "onset": "impact", "family": "ban", "dense": True,
        "bands": ["body"], "voice_band": "onset-only",
    },
    "hit-small": {
        "label": "Trúng nhỏ", "duration_ms": [50, 150], "variants": [6, 8],
        "mix": {"metric": "lufs-m-max", "range": [-22, -20]},
        "spectrum": "Đầu tiếng 2–6 kHz, thân 200–800 Hz, crest từ 12 dB",
        "rand": "hit-small", "onset": "impact", "family": "trung", "dense": True,
        "bands": ["presence", "body"], "voice_band": "onset-only",
    },
    "hit-heavy": {
        "label": "Trúng vừa, nặng", "duration_ms": [120, 600], "variants": [3, 6],
        "mix": {"metric": "lufs-m-max", "range": [-19, -17], "heavy_range": [-16, -14], "text": "Vừa: −19 đến −17. Nặng: −16 đến −14"},
        "spectrum": "Tiếng nặng có sub 40–90 Hz, dài không quá 150 ms",
        "rand": "hit-heavy", "onset": "impact", "family": "trung", "dense": True,
        "bands": ["body", "sub"], "voice_band": "onset-only",
    },
    "blast": {
        "label": "Nổ", "duration_ms": [600, 2000], "variants": [3, 5],
        "mix": {"metric": "lufs-s-max", "range": [-15, -12]},
        "spectrum": "Tiếng nứt 2–8 kHz trong 30 ms đầu. Sub dài không quá 300 ms",
        "rand": "blast", "onset": "impact", "family": "no", "dense": False,
        "bands": ["sub", "presence"], "voice_band": "onset-only",
    },
    "death-swarm": {
        "label": "Chết bầy", "duration_ms": [80, 200], "variants": [8, 10],
        "mix": {"metric": "lufs-m-max", "range": [-24, -21]},
        "spectrum": "Dải giữa và cao, nhẹ",
        "rand": "death-swarm", "onset": "other", "family": "chet", "dense": True,
        "bands": ["presence"], "voice_band": "onset-only",
    },
    "death-big": {
        "label": "Chết lớn", "duration_ms": [400, 900], "variants": [3, 4],
        "mix": {"metric": "lufs-m-max", "range": [-20, -15]},
        "spectrum": "Tiếng thịch 60–150 Hz",
        "rand": "default", "onset": "other", "family": "chet", "dense": False,
        "bands": ["sub", "body"], "voice_band": "onset-only",
    },
    "creature": {
        "label": "Tiếng sinh vật", "duration_ms": [200, 1600], "variants": [3, 4],
        "mix": {"metric": "lufs-m-max", "range": [-20, -15]},
        "spectrum": "AST nên gắn Roar, Growling hoặc Animal, không gắn Speech (cờ)",
        "rand": "default", "onset": "creature", "family": "sinh-vat", "dense": False,
        "bands": ["body"], "voice_band": "free",
    },
    "warning": {
        "label": "Báo nguy", "duration_ms": [250, 2000], "variants": [1, 1],
        "mix": {"metric": "lufs-m-max", "range": [-17, -14]},
        "spectrum": "Không có âm kéo dài ở 1–4 kHz",
        "rand": "rare-fixed", "onset": "other", "family": "nen", "dense": False,
        "bands": ["voice"], "voice_band": "short-warning",
    },
    "ambience": {
        "label": "Nền lặp", "duration_ms": None, "variants": [1, 1],
        "mix": {"metric": "lufs-i", "range": None, "text": "LUFS-I theo tài liệu game (nền −26)"},
        "spectrum": "Phần lớn năng lượng dưới 300 Hz và ở 4–10 kHz",
        "rand": "none", "onset": "loop", "family": "nen", "dense": False,
        "bands": ["sub", "presence"], "voice_band": "avoid",
    },
    "music": {
        "label": "Nhạc", "duration_ms": None, "variants": [1, 1],
        "mix": {"metric": "lufs-i", "range": None, "text": "LUFS-I theo game (−18; Tuyến Cuối −16)"},
        "spectrum": "Đúng số ô nhịp, cùng giọng và điệu giữa các stem (bài J)",
        "rand": "none", "onset": "loop", "family": "nhac", "dense": False,
        "bands": [], "voice_band": "ducked",
    },
    "stinger": {
        "label": "Stinger", "duration_ms": [1000, 3600], "variants": [1, 1],
        "mix": {"metric": "lufs-s-max", "range": [-16, -12]},
        "spectrum": "Cùng giọng với nhạc",
        "rand": "rare-fixed", "onset": "other", "family": "nen", "dense": False,
        "bands": ["pitched"], "voice_band": "free",
    },
    "fx-other": {
        "label": "Khác (không có nhóm trong bảng §4.3.3)", "duration_ms": None, "variants": [1, 3],
        "mix": {"metric": "lufs-m-max", "range": None, "text": "Chưa có mức trong §4.3.3; lấy theo họ âm khi có âm đã duyệt"},
        "spectrum": None,
        "rand": "default", "onset": "other", "family": None, "dense": False,
        "bands": None, "voice_band": "free",
    },
}
CATEGORY_BASIS = "AUDIO_PIPELINE §4.3.3"

# ── §5.3 randomisation groups ──
RANDOMISATION: dict[str, dict] = {
    "key-ok": {"label": "Phím đúng", "pitch_cents": 50, "gain_db": 1, "rules": ["Tránh lặp 2 bản gần nhất"]},
    "key-bad": {"label": "Phím sai", "pitch_cents": 30, "gain_db": None, "rules": ["Nghỉ 150 ms giữa hai lần, để gõ loạn không ra tiếng dồn"]},
    "word-reward": {"label": "Thưởng theo từng từ", "pitch_cents": 30, "gain_db": 1,
                    "rules": ["±20–30 cent, hoặc leo một bậc thang âm", "Phát sau mỗi từ nên cần chút khác biệt"]},
    "rare-fixed": {"label": "Thưởng hiếm, UI, báo nguy, stinger", "pitch_cents": 0, "gain_db": 0,
                   "rules": ["Không đổi ngẫu nhiên: âm hiếm được nhận ra nhờ luôn giống nhau", "Chuỗi thưởng leo nốt theo thang, tối đa 8–12 bậc"]},
    "shot": {"label": "Bắn", "pitch_cents": 100, "gain_db": 2, "rules": ["Tối đa 4 tiếng cho mỗi loại vũ khí", "Hai lần phát cách nhau ít nhất 30 ms"]},
    "hit-small": {"label": "Trúng nhỏ", "pitch_cents": 150, "gain_db": 2, "rules": ["Gom trong 38–45 ms (kit đang dùng 38 ms)"]},
    "hit-heavy": {"label": "Trúng nặng", "pitch_cents": 80, "gain_db": 1, "rules": ["Hạ tiếng trúng nhỏ 3–6 dB trong 150 ms"]},
    "blast": {"label": "Nổ", "pitch_cents": 150, "gain_db": None, "rules": ["Tối đa 4 lần mỗi 120 ms", "Mỗi lần sau nhỏ hơn 3 dB"]},
    "death-swarm": {"label": "Chết bầy", "pitch_cents": 300, "gain_db": 3,
                    "rules": ["Tối đa 4 tiếng", "Khi hơn 6 con chết trong 100 ms, thêm một lớp \"chết hàng loạt\""]},
    "default": {"label": "Chưa có nhóm trong §5.3", "pitch_cents": None, "gain_db": None,
                "rules": ["§5.3 chưa có nhóm này: giữ cách đổi ngẫu nhiên hiện tại của mã"]},
    "none": {"label": "Vòng lặp, nhạc", "pitch_cents": 0, "gain_db": 0, "rules": ["Không đổi ngẫu nhiên"]},
}
RANDOMISATION_BASIS = "AUDIO_PIPELINE §5.3 (mã cần cho mỗi nhóm giá trị riêng, §6.3)"

# ── §6.4 frequency bands ──
BANDS: dict[str, dict] = {
    "sub": {"label": "Dưới 120 Hz", "range_hz": [20, 120]},
    "body": {"label": "120–800 Hz", "range_hz": [120, 800]},
    "voice": {"label": "1–4 kHz (giọng đọc từ)", "range_hz": [1000, 4000]},
    "presence": {"label": "4–8 kHz", "range_hz": [4000, 8000]},
    "pitched": {"label": "Có cao độ", "range_hz": None},
}
VOICE_BAND_RULES: dict[str, str] = {
    "onset-only": "Chỉ đầu tiếng rất ngắn ở 1–4 kHz; không ngân ở dải giọng đọc (§6.4)",
    "decay-15db-100ms": "Năng lượng 1–4 kHz giảm ít nhất 15 dB trong 100 ms sau đầu tiếng; phần ngân dưới 1 kHz hoặc trên 4 kHz (§6.2)",
    "avoid": "Tránh dải 1–4 kHz",
    "soft-short": "Mềm và ngắn; không to hơn phím",
    "short-warning": "Báo nguy ngắn; không có âm kéo dài ở 1–4 kHz",
    "ducked": "Nhạc nhường giọng đọc theo mức của tài liệu game; không đổi mức ở đây (§6.2 bước 5)",
    "free": "Không phát dày; vẫn tránh ngân dài ở 1–4 kHz khi đang đọc từ",
}
BANDS_BY_SOURCE: dict[str, list[str]] = {
    "electric": ["presence"], "fire": ["body"], "creature": ["body"], "pitched-reward": ["pitched"],
    "foley-other": ["body"], "impact": ["body", "presence"], "ui": ["presence"], "warning-stinger": ["pitched"],
    "ambience": ["sub", "presence"], "voice": ["voice"], "key": ["presence"], "shot": ["body"],
    "blast": ["sub", "presence"], "music": [], "folk-instrument": ["pitched"], "folk-flute": ["pitched"],
}
FREQ_BASIS = "AUDIO_PIPELINE §6.4"

# ── §3.2 source classes: ranked options. Kinds are the five plan source kinds ──
KINDS: dict[str, str] = {
    "synth": "Tổng hợp bằng mã (numpy, pedalboard, WebAudio của game)",
    "cc0-layer": "Ghép lớp từ thư viện CC0 (Kenney, VCSL, VSCO-2-CE, Freesound CC0)",
    "sample-player": "Bộ phát mẫu Python: MIDI (mido) + mẫu nhạc cụ CC0 (VCSL, VSCO-2-CE)",
    "model-later": "Mô hình tạo âm (Stable Audio 3, ACE-Step…): chưa cài, chờ bước 0 của chủ dự án",
    "owner-recording": "Chủ dự án tự ghi (người khác ghi thì cần giấy đồng ý, §10.4)",
}

SOURCE_CLASSES: dict[str, dict] = {
    "key": {
        "label": "Phím đúng/sai",
        "ranked": [
            (["synth"], "Tổng hợp bằng mã (theo luật dự án), chỉnh bằng bản dựng không chạy game và tai AI"),
            (["cc0-layer"], "Một mẫu thu thật Kenney CC0, mã đổi cao độ"),
            (["owner-recording"], "Một mẫu tự ghi, mã đổi cao độ"),
        ],
        "now": ["synth"], "later": [],
        "note": "Mô hình khuếch tán yếu với tiếng dưới 50 ms",
    },
    "ui": {
        "label": "UI",
        "ranked": [
            (["cc0-layer"], "Kenney Interface/UI Audio (CC0), có xử lý"),
            (["owner-recording"], "Tự ghi tiếng tre, giấy, gỗ"),
            (["model-later"], "Stable Audio 3, rồi cắt ngắn"),
        ],
        "now": ["cc0-layer"], "later": [],
        "note": "Không to hơn tiếng phím",
    },
    "pitched-reward": {
        "label": "Thưởng có cao độ",
        "ranked": [
            (["sample-player"], "Mẫu nhạc cụ thật VCSL, phát từng nốt bằng bộ phát mẫu Python; dời cao độ tối đa 3 bán cung; hoặc một nốt tốt, mã đổi cao độ trong khoảng đó"),
            (["synth"], "Mô hình vật lý Faust (chuông, sáo)"),
        ],
        "now": ["sample-player"], "later": [],
        "note": "Không viết prompt cho từng nốt. Nốt lệch dưới 10 cent",
    },
    "impact": {
        "label": "Va chạm, trúng",
        "ranked": [
            (["cc0-layer", "model-later"], "Ghép lớp: lớp đầu từ Kenney Impact (CC0), thân và đuôi từ Stable Audio 3"),
            (["model-later"], "Stable Audio 3 nguyên khối, tạo lại thân hoặc đuôi bằng inpaint"),
            (["synth"], "Tổng hợp"),
        ],
        "now": ["cc0-layer", "synth"], "later": ["model-later"],
        "note": "Khi chưa có Stable Audio 3: lớp đầu Kenney Impact + thân tổng hợp (§10.1)",
    },
    "shot": {
        "label": "Súng, khạc, bắn",
        "ranked": [
            (["model-later", "cc0-layer", "synth"], "Stable Audio 3, cộng lớp cơ khí Kenney, cộng sub tổng hợp"),
            (["synth"], "Tổng hợp thuần (ElevenLabs gói trả phí là việc của chủ dự án)"),
        ],
        "now": ["cc0-layer", "synth"], "later": ["model-later"],
        "note": None,
    },
    "electric": {
        "label": "Điện, hồ quang",
        "ranked": [
            (["synth"], "Tổng hợp bằng numpy và pedalboard"),
            (["model-later"], "Stable Audio 3"),
            (["cc0-layer"], "99Sounds Electromagnetic (chủ dự án tải); Surge XT nếu chủ dự án cài"),
        ],
        "now": ["synth"], "later": [],
        "note": "Giới hạn năng lượng 2–5 kHz khi đông quái",
    },
    "blast": {
        "label": "Nổ, bẫy",
        "ranked": [
            (["model-later"], "Stable Audio 3 Small-SFX"),
            (["cc0-layer"], "Ghép từ Kenney"),
            (["synth"], "Tổng hợp (ElevenLabs gói trả phí là việc của chủ dự án)"),
        ],
        "now": ["cc0-layer", "synth"], "later": ["model-later"],
        "note": None,
    },
    "fire": {
        "label": "Lửa, luồng lửa",
        "ranked": [
            (["model-later"], "Stable Audio 3"),
            (["cc0-layer"], "Bản ghi lửa CC0 trên Freesound (chủ dự án tải)"),
            (["synth"], "Tổng hợp (ElevenLabs gói trả phí là việc của chủ dự án)"),
        ],
        "now": ["cc0-layer", "synth"], "later": ["model-later"],
        "needs_now": ["chu-du-an-tai-freesound"],
        "note": "Luồng lửa tách 3 phần: đầu, vòng lặp, cuối",
    },
    "creature": {
        "label": "Tiếng sinh vật",
        "ranked": [
            (["cc0-layer"], "Ghép tiếng thú thật CC0, hạ 5–12 bán cung rồi xếp lớp"),
            (["model-later"], "Stable Audio 3 (tốt cho kết cấu; tiếng kêu chưa kiểm chứng)"),
            (["owner-recording"], "Chủ dự án tự gầm vào điện thoại, Claude hạ giọng"),
        ],
        "now": ["cc0-layer"], "later": ["model-later"],
        "needs_now": ["chu-du-an-tai-freesound"],
        "note": "Cấm nhãn Speech",
    },
    "ambience": {
        "label": "Nền lặp",
        "ranked": [
            (["model-later"], "Stable Audio 3, rồi sửa mối nối"),
            (["cc0-layer"], "Bản ghi hiện trường CC0"),
            (["synth"], "Tổng hợp bằng mã (như hiện nay)"),
        ],
        "now": ["cc0-layer", "synth"], "later": ["model-later"],
        "note": "Độ dài theo tài liệu game",
    },
    "warning-stinger": {
        "label": "Báo nguy, stinger",
        "ranked": [
            (["sample-player"], "Mẫu nhạc cụ (kèn co VSCO, cồng và trống khung VCSL) cộng MIDI"),
            (["model-later"], "Stable Audio 3 (tù và, còi)"),
        ],
        "now": ["sample-player"], "later": [],
        "note": "Báo nguy chỉ có một phiên bản cố định, để người chơi học được",
    },
    "music": {
        "label": "Nhạc nhiều lớp",
        "ranked": [
            (["sample-player"], "MIDI do Claude viết, phát bằng mẫu CC0 qua bộ phát mẫu Python; đúng BPM, đúng giọng, stem khớp ô nhịp"),
            (["model-later"], "ACE-Step 1.5 để phác ý tưởng và làm stinger"),
            (["model-later"], "Stable Audio 3 Small-Music cho pad; Magenta RealTime 2 cho nền thích ứng"),
        ],
        "now": ["sample-player"], "later": [],
        "note": "Mô hình tạo nhạc không tự sinh các stem tách rời trên cùng một lưới nhịp",
    },
    "folk-instrument": {
        "label": "Nhạc cụ dân gian Việt (có mẫu VCSL)",
        "ranked": [
            (["owner-recording"], "Chủ dự án tự ghi hoặc nhờ người ghi, có giấy đồng ý"),
            (["sample-player"], "VCSL: Dan Tranh, Slit Drum, Woodblock, Frame Drum (tạm thay trống cơm)"),
            (["model-later"], "LoRA Stable Audio 3 học trên bản ghi của chủ dự án"),
            (["synth"], "Tổng hợp (Faust)"),
        ],
        "now": ["sample-player"], "later": ["owner-recording"],
        "note": "Chuông và cồng VCSL phải được chủ dự án duyệt (§8.2)",
    },
    "folk-flute": {
        "label": "Sáo trúc (không có mẫu CC0 đã kiểm chứng)",
        "ranked": [
            (["owner-recording"], "Chủ dự án tự ghi sáo trúc, có giấy đồng ý nếu người khác thổi"),
            (["synth"], "Faust fluteModel hoặc tổng hợp như hiện nay"),
            (["model-later"], "LoRA Stable Audio 3 học trên bản ghi của chủ dự án"),
        ],
        "now": ["synth"], "later": ["owner-recording"],
        "note": "Chưa tìm được thư viện miễn phí đã kiểm chứng cho sáo trúc (§3.2)",
    },
    "voice": {
        "label": "Giọng người",
        "ranked": [(["owner-recording"], "Chủ dự án và người nhà ghi, có giấy đồng ý")],
        "now": ["owner-recording"], "later": [],
        "needs_now": ["chu-du-an-ghi-am", "giay-dong-y"],
        "note": "Không dùng AI. Stable Audio 3 không có giọng người",
    },
    "foley-other": {
        "label": "Tiếng động khác (không có dòng riêng trong §3.2)",
        "ranked": [
            (["cc0-layer"], "Ghép lớp CC0 (Kenney)"),
            (["model-later"], "Stable Audio 3"),
            (["owner-recording"], "Tự ghi foley"),
            (["synth"], "Tổng hợp"),
        ],
        "now": ["cc0-layer", "synth"], "later": ["model-later"],
        "note": "Theo thứ tự chung của §3.1 A",
    },
}
SOURCE_BASIS = "AUDIO_PIPELINE §3.2 (nguồn theo loại âm), §10.1 (khi chưa có Stable Audio 3)"

# ── blockers ──
BLOCKERS: dict[str, str] = {
    "buoc-0": "Chờ chủ dự án xong bước 0 (Stable Audio 3, §10.1, §15.1)",
    "chu-du-an-tai-freesound": "Cần chủ dự án tìm và tải âm CC0 trên Freesound bằng tay (§3.4)",
    "chu-du-an-ghi-am": "Cần chủ dự án tự ghi (§15.1 tùy chọn)",
    "giay-dong-y": "Bản ghi của người khác cần giấy đồng ý (§10.4)",
    "chu-du-an-duyet": "Chờ chủ dự án duyệt (nguồn chuông, cồng, quãng tám, văn hóa, điệu)",
    "sua-tai-lieu-game": "Id do kế hoạch đề xuất: cần thêm vào tài liệu game trước (chủ dự án duyệt)",
    "chua-co-trong-ma": "Tài liệu game có id nhưng mã chưa phát âm này",
}

# ── §10.2 licence policy per kind ──
LICENCE_BY_KIND: dict[str, dict] = {
    "synth": {"allowed": ["project-code"], "conditional": [],
              "note": "Mã của dự án. pedalboard (GPL-3.0) chỉ import trên máy, không chép vào repo (§10.9)"},
    "cc0-layer": {"allowed": ["CC0-1.0"], "conditional": [
        {"licence": "CC0-1.0 (Freesound, người tải lên từ chối AI)", "condition": "Chỉ ghép tay, không vào bước AI nào, không vào LoRA (§10.2)"}],
        "note": "Kenney, VCSL, VSCO-2-CE, Freesound CC0. Lưu LICENSE-<ngày>.txt kèm thư viện"},
    "sample-player": {"allowed": ["CC0-1.0", "project-code"], "conditional": [],
                      "note": "Mẫu VCSL, VSCO-2-CE (CC0); MIDI do Claude viết; mido là MIT (chưa kiểm lại)"},
    "model-later": {"allowed": [], "conditional": [
        {"licence": "Stability-Community-2024", "condition": "Bước 0: đăng ký Community License, chấp nhận AUP và điều khoản Gemma; có licences/stability-registration.txt (§10.1)"},
        {"licence": "MIT (ACE-Step 1.5)", "condition": "Ghim phiên bản; kiểm giai điệu trước khi bán"},
        {"licence": "Apache-2.0 (MOSS-SoundEffect)", "condition": "Chỉ khi bước 0 trả lời không"}],
        "note": "Chưa cài: chờ bước 0 của chủ dự án"},
    "owner-recording": {"allowed": ["owner-original"], "conditional": [
        {"licence": "release-CC0-or-transfer", "condition": "Bản ghi của người khác: cần giấy đồng ý (§10.4)"}],
        "note": None},
}
FORBIDDEN: list[str] = [
    "non-commercial-weights",       # AudioGen, MusicGen, MAGNeT, MMAudio, ... (§3.5)
    "freesound-cc-by-nc",
    "freesound-sampling-plus",
    "bbc-sound-effects",
    "pixabay",
    "sound-from-other-games",
    "sonniss-lot-1-2-and-any-ai-step",
    "elevenlabs-or-suno-free-tier-release",
]
LICENCE_RECORD = "art-src/audio/SOURCES.json và licences.jsonl (§10.5, §10.6); pnpm audio:licence-check chặn khi thiếu"

# ── §7 Listening Board contexts ──
BOARD_CONTEXTS = {"mot-minh": "Một mình", "lap-20": "Lặp 20 lần", "loa-nho": "Loa nhỏ", "trong-tran": "Trong trận"}
# Typical replay interval for dense sounds (ms); proposal from bots at 40 WPM (§6.1). Docs override per id.
TYPICAL_INTERVAL_MS: dict[str, int] = {
    "key-ok": 300, "key-bad": 600, "word-reward": 1500, "shot": 250, "hit-small": 200,
    "hit-heavy": 600, "death-swarm": 150,
}

# ── §4.4 AST labels worth checking (real-world sounds only); flag only ──
AST_HINTS: list[tuple[str, str]] = [
    (r"\b(wood|wooden|bamboo|clapper)\b", "Wood"),
    (r"\bbell\b|\bchime\b", "Bell"),
    (r"\bgong\b", "Gong"),
    (r"\bdrum\b|trống", "Drum"),
    (r"\bflute\b|sáo", "Flute"),
    (r"\bzither\b|đàn tranh", "Zither"),
    (r"\bharp\b", "Harp"),
    (r"\bexplosion\b|\bboom\b", "Explosion"),
    (r"\bautocannon\b|\bgun\b|\bshot from\b", "Gunshot, gunfire"),
    (r"\bfire\b|\bflame", "Fire"),
    (r"\bcoins?\b", "Coin (dropping)"),
    (r"\bwind\b", "Wind"),
    (r"\bstream\b", "Stream"),
    (r"\bsongbird\b|\bbird\b", "Bird"),
    (r"\bhowl\b", "Howl"),
    (r"\broar\b", "Roar"),
    (r"\bgrowl", "Growling"),
    (r"\bfootsteps?\b", "Walk, footsteps"),
    (r"\bsiren\b|\bklaxon\b", "Siren"),
    (r"\bglass\b", "Glass"),
    (r"\bhorn\b", "French horn"),
]

# Critic lane group keys (critic/groups.py). The critic falls back to its own id rules when a key is unknown.
CRITIC_GROUPS: dict[str, str] = {
    "key-ok": "key_ok", "key-bad": "key_bad", "ui": "ui", "word-reward": "reward", "hit-small": "hit_small",
    "hit-heavy": "hit_heavy", "blast": "explosion", "death-swarm": "death_swarm", "death-big": "death_big",
    "creature": "creature", "warning": "alarm", "ambience": "ambience", "music": "music", "stinger": "stinger",
}


# Ids whose critic template differs from their category's (critic/groups.py), with the reason.
CRITIC_GROUP_BY_ID: list[tuple[str, str, str]] = [
    (r"^fire\.impact\.", "hit_fire", "Rồng Giữ Ải: phụt lửa trầm, thân tròn; không cần lớp tách 2 kHz, lửa lách tách là đuôi"),
]
# §4.3.1: families whose "fx-other" sounds are still hits, shots or blasts (rise ≤ 10 ms).
IMPACT_FAMILIES = ("trung", "ban", "no")


def critic_group(category: str | None, source: str | None, dirty: bool, onset: str | None,
                 sound_id: str | None = None) -> str:
    import re
    for pat, group, _why in CRITIC_GROUP_BY_ID:
        if sound_id and re.search(pat, sound_id):
            return group
    if category == "shot":
        return "shot_gun" if dirty else "shot_launch"
    if category in CRITIC_GROUPS:
        return CRITIC_GROUPS[category]
    if source in ("fire", "electric") and onset == "none":
        return "whoosh"
    return "generic"


# Plan §4.4: short sounds are scored on a 3–4 s loop of about 10 plays.
SHORT_LOOP_EVAL_MS = 300


def family_of(category: str) -> str | None:
    return CATEGORIES[category]["family"]
