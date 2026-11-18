"""Validate spec cards: JSON Schema (schema/card.schema.json) + checks the schema cannot express."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from jsonschema import Draft202012Validator

from . import store

SCHEMA_PATH = Path(__file__).resolve().parent / "schema" / "card.schema.json"
ERROR, WARN = "lỗi", "cảnh báo"


@dataclass
class Problem:
    path: Path
    level: str
    message: str

    def __str__(self) -> str:
        return f"{self.level}: {self.path.parent.name}/{self.path.name}: {self.message}"


def schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


_VALIDATOR: Draft202012Validator | None = None


def validator() -> Draft202012Validator:
    global _VALIDATOR
    if _VALIDATOR is None:
        s = schema()
        Draft202012Validator.check_schema(s)
        _VALIDATOR = Draft202012Validator(s)
    return _VALIDATOR


def _where(err) -> str:
    return ".".join(str(p) for p in err.absolute_path) or "(gốc)"


def check_card(card: dict, path: Path) -> list[Problem]:
    out: list[Problem] = []
    for err in sorted(validator().iter_errors(card), key=lambda e: list(e.absolute_path)):
        out.append(Problem(path, ERROR, f"{_where(err)}: {err.message}"))
    if not isinstance(card, dict):
        return out
    sid, game = card.get("id"), card.get("game")
    if sid is not None and path.name != f"{sid}.yaml":
        out.append(Problem(path, ERROR, f"tên file phải là {sid}.yaml"))
    if game is not None and path.parent.name != game:
        out.append(Problem(path, ERROR, f"thẻ của game {game} nằm trong thư mục {path.parent.name}"))
    for p in card.get("manual_fields") or []:
        if isinstance(p, str) and not store.has_path(card, p):
            out.append(Problem(path, ERROR, f"manual_fields trỏ tới {p}, trường này không có trong thẻ"))

    d = card.get("duration") or {}
    t, lo, hi = d.get("target_ms"), d.get("min_ms"), d.get("max_ms")
    if isinstance(t, (int, float)):
        if isinstance(lo, (int, float)) and lo > t:
            out.append(Problem(path, ERROR, f"duration.min_ms {lo} lớn hơn target_ms {t}"))
        if isinstance(hi, (int, float)) and hi < t:
            out.append(Problem(path, ERROR, f"duration.max_ms {hi} nhỏ hơn target_ms {t}"))
    elif card.get("status") not in ("proposed", "retired"):
        out.append(Problem(path, WARN, "chưa có duration.target_ms: ghi độ dài vào tài liệu game hoặc sửa tay (manual_fields)"))

    v = card.get("variants") or {}
    if all(isinstance(v.get(k), int) for k in ("min", "max", "target")):
        if not v["min"] <= v["target"] <= v["max"]:
            out.append(Problem(path, ERROR, f"variants: cần min ≤ target ≤ max (đang {v['min']}, {v['target']}, {v['max']})"))
        r = card.get("randomisation") or {}
        if r.get("group") == "rare-fixed" and v["min"] > 1 and not card.get("pitches"):
            out.append(Problem(path, WARN, "âm cố định (rare-fixed) mà cần nhiều hơn 1 biến thể"))

    pb = card.get("playback") or {}
    if pb.get("mode") == "loop" and (card.get("onset") or {}).get("class") not in ("loop", None):
        out.append(Problem(path, WARN, "vòng lặp nên có onset.class = loop"))
    if card.get("category") == "music" and not (d.get("music") or {}).get("bars"):
        out.append(Problem(path, ERROR, "nhạc cần duration.music.bpm và bars"))

    sp = card.get("source_plan") or {}
    if "model-later" in (sp.get("now") or []):
        out.append(Problem(path, ERROR, "source_plan.now không được có model-later: mô hình chưa cài (bước 0)"))
    if card.get("source_class") == "voice" and "model-later" in [k for r in sp.get("ranked") or [] for k in r.get("kinds", [])]:
        out.append(Problem(path, ERROR, "giọng người không dùng AI (§3.2)"))
    if "chu-du-an-ghi-am" in (card.get("blocked_by") or []) and card.get("source_class") == "voice" and "giay-dong-y" not in card.get("blocked_by", []):
        out.append(Problem(path, WARN, "giọng người cần nhắc giấy đồng ý (§10.4)"))

    for ref in card.get("references") or []:
        if isinstance(ref, dict) and str(ref.get("path", "")).startswith(("games/", "/Users")) and "/AudioLab/" not in str(ref.get("path")):
            out.append(Problem(path, WARN, f"âm tham chiếu {ref.get('path')} nên nằm dưới ~/AudioLab, không trong repo"))
    if card.get("status") == "proposed" and "sua-tai-lieu-game" not in (card.get("blocked_by") or []) and card.get("origin", {}).get("sound_list", {}).get("present") is False:
        out.append(Problem(path, WARN, "id đề xuất chưa có trong tài liệu game nhưng không ghi sua-tai-lieu-game"))
    return out


def check_files(paths: list[Path]) -> tuple[list[Problem], int]:
    problems: list[Problem] = []
    seen: dict[tuple[str, str], Path] = {}
    for p in paths:
        try:
            card = store.load_file(p)
        except Exception as exc:  # malformed YAML
            problems.append(Problem(p, ERROR, f"không đọc được YAML: {exc}"))
            continue
        problems += check_card(card, p)
        key = (str(card.get("game")), str(card.get("id")))
        if key in seen:
            problems.append(Problem(p, ERROR, f"trùng id với {seen[key]}"))
        seen[key] = p
    return problems, len(paths)
