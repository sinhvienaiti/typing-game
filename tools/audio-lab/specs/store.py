"""Card files: YAML in/out, stable layout, and the merge that keeps hand edits.

Hand edits survive `generate` when:
  - the whole card has `manual: true` (left untouched);
  - a mapping inside the card has `manual: true` (that mapping is kept whole);
  - a dotted path is listed in `manual_fields` (e.g. `duration.target_ms`, `constraints`);
  - the field is hand-owned: status, references, prompt.variants, notes, manual_fields.
Keys a person added that the generator does not know are kept too (the validator flags them).
"""
from __future__ import annotations

import copy
from pathlib import Path

import yaml

SPECS_DIR = Path(__file__).resolve().parent
HAND_OWNED = ("status", "references", "prompt.variants", "notes", "manual_fields")
HEADER = (
    "# Thẻ spec âm thanh (AUDIO_PIPELINE §5.1 bước 1). Sinh bởi `pnpm audio:specs generate`; kiểm bằng `pnpm audio:specs validate`.\n"
    "# Sửa tay: thêm `manual: true` vào mục đã sửa, hoặc ghi đường dẫn (vd. duration.target_ms) vào manual_fields.\n"
    "# status, references, prompt.variants, notes luôn được giữ khi sinh lại. Comment YAML thì không: ghi chú để ở notes.\n"
)


class _Dumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):  # indent lists under their key
        return super().increase_indent(flow, False)


def _str(dumper, data: str):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


def _list(dumper, data: list):
    flat = all(isinstance(x, (int, float, bool)) or x is None or (isinstance(x, str) and len(x) <= 40) for x in data)
    flow = flat and len(data) <= 8 and sum(len(str(x)) + 2 for x in data) <= 90
    return dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=flow)


_Dumper.add_representer(str, _str)
_Dumper.add_representer(list, _list)


def dumps(card: dict) -> str:
    body = yaml.dump(card, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=4096, default_flow_style=False)
    return HEADER + body


def loads(text: str) -> dict:
    data = yaml.safe_load(text)
    if not isinstance(data, dict):
        raise ValueError("thẻ phải là một mapping YAML")
    return data


def card_path(root: Path, game: str, sound_id: str) -> Path:
    return root / game / f"{sound_id}.yaml"


def load_file(path: Path) -> dict:
    return loads(path.read_text(encoding="utf-8"))


def card_files(root: Path, game: str | None = None) -> list[Path]:
    games = [game] if game else sorted(p.name for p in root.iterdir() if p.is_dir() and not p.name.startswith(("_", ".")) and any(p.glob("*.yaml")))
    out: list[Path] = []
    for g in games:
        d = root / g
        if d.is_dir():
            out += sorted(d.glob("*.yaml"))
    return out


# ── dotted paths ──

def _get(d: dict, path: str):
    cur = d
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            raise KeyError(path)
        cur = cur[part]
    return cur


def has_path(d: dict, path: str) -> bool:
    try:
        _get(d, path)
        return True
    except KeyError:
        return False


def _set(d: dict, path: str, value) -> None:
    parts = path.split(".")
    cur = d
    for part in parts[:-1]:
        if not isinstance(cur.get(part), dict):
            cur[part] = {}
        cur = cur[part]
    cur[parts[-1]] = value


def manual_sections(d: dict, prefix: str = "") -> list[str]:
    """Dotted paths of nested mappings marked `manual: true` (the card root excluded)."""
    out: list[str] = []
    for k, v in d.items():
        if isinstance(v, dict):
            p = f"{prefix}{k}"
            if v.get("manual") is True:
                out.append(p)
            else:
                out += manual_sections(v, p + ".")
    return out


def merge(generated: dict, existing: dict | None) -> tuple[dict, list[str]]:
    """Generated card with the hand edits of `existing` laid back on top. Returns (card, kept paths)."""
    if existing is None:
        return generated, []
    if existing.get("manual") is True:
        return existing, ["*"]
    out = copy.deepcopy(generated)
    kept: list[str] = []
    paths = list(HAND_OWNED) + [p for p in (existing.get("manual_fields") or []) if isinstance(p, str)]
    for path in paths:
        if has_path(existing, path):
            value = _get(existing, path)
            if not has_path(out, path) or _get(out, path) != value:
                kept.append(path)
            _set(out, path, copy.deepcopy(value))
    for path in manual_sections(existing):
        _set(out, path, copy.deepcopy(_get(existing, path)))
        kept.append(path)
    for k, v in existing.items():
        if k not in out:
            out[k] = copy.deepcopy(v)
            kept.append(k)
    return out, _dedupe(kept)


def _dedupe(items: list[str]) -> list[str]:
    seen: list[str] = []
    for x in items:
        if x not in seen:
            seen.append(x)
    return seen


def write_if_changed(path: Path, text: str) -> str:
    """'created' | 'updated' | 'unchanged'."""
    if path.exists():
        if path.read_text(encoding="utf-8") == text:
            return "unchanged"
        path.write_text(text, encoding="utf-8")
        return "updated"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return "created"
