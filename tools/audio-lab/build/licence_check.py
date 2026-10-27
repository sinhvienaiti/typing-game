"""Licence check (AUDIO_PIPELINE.md §10.7): blocks a build on any licence or provenance gap.

Usage:
  run.sh licence-check                          # every game (games/**)
  run.sh licence-check --game dragon-hold       # one game in the repo
  run.sh licence-check --staging [--game G]     # ~/AudioLab/review/staging/<game> trees
  run.sh licence-check --art-src DIR [--public DIR] [--json]
  run.sh licence-check --freeze-legacy space-typing   # rewrite build/legacy-audio.json from the game's git HEAD

A game without SOURCES.json/licences.jsonl is not "passed": its released audio is still scanned, and
every file must be on the explicit legacy list (build/legacy-audio.json, §16 #9: the Space Typing
CC0 files already in Git) with the same sha256, or it is an error (§10.7 rule 1). When no game was
checked at all, the result line says BỎ QUA, never ĐẠT.

Exit 0: no error. Exit 1: at least one error. Exit 2: bad arguments.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

from build import ledger, policy

HEX64 = re.compile(r"\b[0-9a-f]{64}\b")
AUDIO_EXT = {".ogg", ".wav", ".flac", ".opus", ".mp3", ".m4a", ".aac", ".webm"}
LEGACY_FILE = Path(__file__).resolve().parent / "legacy-audio.json"
# Released audio folders per game, relative to games/<game> (§11; Space Typing keeps its own layout).
RELEASE_DIRS = {"space-typing": ["public/assets/audio", "src/assets/audio"]}


def release_dirs(game: str) -> list[str]:
    return RELEASE_DIRS.get(game, [f"public/assets/{game}/audio"])


def load_legacy(path: Path = LEGACY_FILE) -> dict[str, dict[str, str]]:
    """{game: {path under games/<game>: sha256}} of grandfathered files (§16 #9)."""
    if not path.is_file():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {g: dict(v.get("files") or {}) for g, v in data.items() if not g.startswith("$") and isinstance(v, dict)}


def scan_unadopted(game_root: Path, game: str, legacy: dict[str, str]) -> tuple[int, list[Problem]]:
    """A game without a ledger: every released audio file must be a listed legacy file, unchanged."""
    probs: list[Problem] = []
    n_legacy = 0
    for rel_dir in release_dirs(game):
        d = game_root / rel_dir
        if not d.is_dir():
            continue
        for f in sorted(d.rglob("*")):
            if not f.is_file() or f.suffix.lower() not in AUDIO_EXT:
                continue
            rel = f.relative_to(game_root).as_posix()
            want = legacy.get(rel)
            if want is None:
                probs.append(Problem("missing-record", rel, "file phát hành không có SOURCES.json và không nằm trong "
                                     "danh sách file cũ được miễn (mục 10.7, 16 #9)"))
            elif ledger.sha256_file(f) != want:
                probs.append(Problem("legacy-changed", rel, "file cũ được miễn đã đổi nội dung: file mới cần hồ sơ "
                                     "trong SOURCES.json (mục 10.5)"))
            else:
                n_legacy += 1
    return n_legacy, probs


def freeze_legacy(game: str, out: Path = LEGACY_FILE) -> int:
    """Write the legacy list from the game's committed audio (git HEAD blobs, not the working tree)."""
    import hashlib
    import subprocess
    from common import env

    root = env.game_dir(game)
    files = subprocess.run(["git", "-C", str(root), "ls-files", "-z", "--", *release_dirs(game)],
                           capture_output=True, check=True).stdout.decode().split("\0")
    head = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True,
                          check=True).stdout.strip()
    got = {}
    for rel in sorted(f for f in files if f and Path(f).suffix.lower() in AUDIO_EXT):
        blob = subprocess.run(["git", "-C", str(root), "show", f"HEAD:{rel}"], capture_output=True, check=True).stdout
        got[rel] = hashlib.sha256(blob).hexdigest()
    data = json.loads(out.read_text(encoding="utf-8")) if out.is_file() else {}
    data["$basis"] = ("AUDIO_PIPELINE.md §16 #9: các file âm CC0 đã có trong Git của Space Typing được giữ nguyên; "
                      "file mới phải có hồ sơ SOURCES.json (§10.5). Sinh bằng licence-check --freeze-legacy.")
    data[game] = {"commit": head, "count": len(got), "files": got}
    out.write_text(json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return len(got)


@dataclass
class Problem:
    code: str
    where: str
    message: str
    severity: str = "error"


class Checker:
    def __init__(self, art_src: Path, public: Path | None = None, require_files: bool = True,
                 legacy: dict[str, str] | None = None):
        self.art = Path(art_src)
        self.public = Path(public) if public else None
        self.require_files = require_files
        self.legacy = legacy or {}
        self.problems: list[Problem] = []
        self._rows: dict[str, dict] = {}

    def err(self, code: str, where: str, msg: str) -> None:
        self.problems.append(Problem(code, where, msg))

    def warn(self, code: str, where: str, msg: str) -> None:
        self.problems.append(Problem(code, where, msg, "warning"))

    # ------------------------------------------------------------ inputs
    def _load(self) -> tuple[dict, dict[str, dict]]:
        src_path = self.art / "SOURCES.json"
        try:
            data = ledger.read_sources(src_path)
        except json.JSONDecodeError as e:
            self.err("schema", "SOURCES.json", f"JSON hỏng: {e}")
            data = {}
        for e in ledger.schema_errors("sources", {"$version": ledger.SOURCES_VERSION, **ledger.records(data)}):
            self.err("schema", "SOURCES.json", e)
        rows = ledger.read_rows(self.art / "licences.jsonl")
        for i, r in enumerate(rows, 1):
            if "_invalid" in r:
                self.err("schema", "licences.jsonl", r["_invalid"])
                continue
            for e in ledger.schema_errors("licences", r):
                self.err("missing-record", f"licences.jsonl dòng {i} ({r.get('key', '?')})", e)
        return ledger.records(data), ledger.rows_by_key(rows)

    # ------------------------------------------------------------ checks
    def _check_files(self, recs: dict[str, dict]) -> None:
        if self.public is None or not self.public.is_dir():
            return
        by_name = {Path(k).name: k for k in recs}
        legacy_shas = set(self.legacy.values())
        for f in sorted(self.public.rglob("*")):
            if not f.is_file() or f.suffix.lower() not in AUDIO_EXT:
                continue
            rel = f.relative_to(self.public).as_posix()
            key = rel if rel in recs else by_name.get(f.name)
            if key is None and legacy_shas and ledger.sha256_file(f) in legacy_shas:
                continue                     # grandfathered file (§16 #9), unchanged
            if key is None:
                self.err("missing-record", rel, "file phát hành không có hồ sơ trong SOURCES.json")
                continue
            sha = ledger.sha256_file(f)
            if recs[key].get("sha256") != sha:
                self.err("hash-mismatch", rel, f"sha256 của file ({sha[:12]}…) khác hồ sơ ({str(recs[key].get('sha256'))[:12]}…)")
        for key in recs:
            if not (self.public / key).is_file() and not any(self.public.rglob(Path(key).name)):
                self.warn("orphan-record", key, "có hồ sơ nhưng không thấy file trên máy (có thể đang ở Drive)")

    def _licence_ok(self, where: str, licence: str | None) -> str:
        state = policy.classify(licence)
        if state == "missing":
            self.err("missing-record", where, "thiếu mã giấy phép")
        elif state == "denied":
            self.err("disallowed-licence", where, f"giấy phép bị cấm: {licence}")
        elif state == "unknown":
            self.err("unknown-licence", where, f"giấy phép lạ (không có trong chính sách 10.2): {licence}")
        return state

    def _model_ok(self, where: str, model: str, rows: dict[str, dict]) -> None:
        if policy.model_denied(model):
            self.err("nc-model", where, f"trọng số phi thương mại bị cấm (mục 3.5): {model}")
        row = rows.get(f"model:{model}")
        if row is None and "@" not in model:   # repo without revision: any ledger row for that repo
            same = [r for r in rows.values() if r.get("kind") == "model" and r.get("repo") == model]
            row = same[-1] if same else None
            if row is not None:
                self.warn("model-revision", where, f"mô hình {model} không ghi revision; dùng dòng {row['key']}")
        if row is None:
            self.err("missing-record", where, f"mô hình {model} chưa có dòng trong licences.jsonl")
            return
        if row.get("commercial_ok") is False or policy.classify(row.get("licence")) == "denied":
            self.err("nc-model", where, f"mô hình {model} có giấy phép không thương mại: {row.get('licence')}")
        elif policy.classify(row.get("licence")) == "unknown":
            self.err("unknown-licence", where, f"mô hình {model}: giấy phép lạ {row.get('licence')}")

    def _stability_ok(self, where: str, rows: dict[str, dict]) -> None:
        acc = [r for r in rows.values() if r.get("kind") == "acceptance"
               and policy.canonical(r.get("licence")) == "LicenseRef-Stability-Community-2024"]
        if not acc:
            self.err("stability-unregistered", where, "lớp Stable Audio 3 nhưng chưa có dòng đăng ký Stability (mục 10.1)")
            return
        for r in acc:
            if not (self.art / r.get("file", "")).is_file():
                self.err("stability-unregistered", where, f"thiếu file xác nhận đăng ký {r.get('file')}")

    def _credits_ok(self, where: str, row: dict) -> None:
        credits = self.art / "CREDITS.md"
        text = credits.read_text(encoding="utf-8") if credits.is_file() else ""
        if row["key"] not in text and (not row.get("attribution_text") or row["attribution_text"] not in text):
            self.err("missing-credit", where, f"nguồn CC-BY {row.get('file', row['key'])} chưa có trong CREDITS.md")

    def _check_row(self, where: str, row: dict, steps: list[str]) -> None:
        lic = row.get("licence")
        self._licence_ok(where, lic)
        if row.get("commercial_ok") is False:
            self.err("not-commercial", where, f"nguồn {row['key']} có commercial_ok=false")
        if steps and policy.is_sonniss(row):
            self.err("sonniss-ai", where, f"nguồn Sonniss đã qua bước AI: {', '.join(steps)}")
        elif steps and row.get("ai_input_allowed") is False:
            self.err("ai-forbidden", where, f"nguồn cấm đưa vào AI (ai_input_allowed=false) đã qua: {', '.join(steps)}")
        cond = policy.ALLOWED.get(policy.canonical(lic) or "", {}).get("cond")
        if cond == "credits" or row.get("attribution_required"):
            self._credits_ok(where, row)
        if cond == "release" or row.get("origin") == "other-recording":
            rel = row.get("release_file")
            if not rel or not (self.art / rel).is_file():
                self.err("missing-release", where, "bản ghi của người khác chưa có giấy đồng ý (mục 10.4)")
        if cond == "subscription" and not row.get("subscription"):
            self.err("missing-record", where, "âm ElevenLabs cần ghi kỳ đăng ký gói trả phí (subscription)")
        lib_key = row.get("libraryKey")
        if lib_key and lib_key not in self._rows:
            self.err("missing-record", where, f"thiếu dòng thư viện {lib_key} trong licences.jsonl")
        copy = row.get("licenceCopy")
        if row.get("kind") in ("source", "library") and copy and not (self.art / copy).is_file():
            self.err("missing-licence-copy", where, f"thiếu bản lưu giấy phép {copy}")

    def _check_init_audio(self, where: str, ref: str, recs: dict[str, dict], rows: dict[str, dict]) -> None:
        """audio-to-audio: every source under the init file went through an AI step (§10.2: no Sonniss)."""
        hashes = HEX64.findall(ref)
        if not hashes:
            self.err("missing-record", where, f"initAudio không ghi sha256 của file gốc: {ref!r}")
            return
        for h in hashes:
            if f"sha256:{h}" in rows:
                self._check_row(where + " › initAudio", rows[f"sha256:{h}"], ["init-audio"])
                continue
            hero = [r for r in recs.values() if h in (r.get("sha256"), r.get("masterSha256"))]
            if not hero:
                self.err("missing-record", where, f"initAudio sha256 {h[:12]}… không có trong sổ hay hồ sơ")
            for rec in hero:
                for layer in rec.get("layers") or []:
                    for ref in [layer, *(layer.get("sources") or [])]:
                        row = rows.get(ref.get("ledgerKey") or "") or rows.get(f"sha256:{ref.get('sourceSha256', '')}")
                        if row is not None:
                            self._check_row(f"{where} › initAudio › {layer.get('id', '?')}", row, ["init-audio"])

    def _check_records(self, recs: dict[str, dict], rows: dict[str, dict]) -> None:
        for key, rec in recs.items():
            file_steps = list(rec.get("aiSteps") or [])
            for m in rec.get("models") or []:
                self._model_ok(key, m, rows)
            for layer in rec.get("layers") or []:
                where = f"{key} › {layer.get('id', '?')}"
                steps = file_steps + list(layer.get("aiSteps") or [])
                qa = layer.get("rawQa")
                if isinstance(qa, dict) and qa.get("verdict") == "BLOCK" and not qa.get("exception"):
                    self.err("raw-clip", where, "nguồn của lớp bị cắt đỉnh trong file gốc (mục 4.3.1), "
                                                "không có lý do allowClip")
                tool = layer.get("tool", "")
                lic = policy.canonical(layer.get("licence"))
                if layer.get("kind") == "synth" or tool == policy.SYNTH_TOOL:
                    self._licence_ok(where, lic)
                    continue
                if layer.get("model") or policy.AI_TOOLS.search(tool or ""):
                    self._licence_ok(where, lic)
                    if layer.get("model"):
                        self._model_ok(where, layer["model"], rows)
                    if "stability" in (lic or "").lower() or "stable-audio" in tool.lower():
                        self._stability_ok(where, rows)
                    if layer.get("initAudio"):
                        self._check_init_audio(where, str(layer["initAudio"]), recs, rows)
                    if layer.get("kind") == "gen" and not layer.get("ledgerKey"):
                        continue
                subs = layer.get("sources")
                if isinstance(subs, list) and subs:   # sampler phrase: one ledger row per sample
                    for sub in subs:
                        sw = f"{where} › {sub.get('source', '?')}"
                        row = rows.get(sub.get("ledgerKey") or "") or rows.get(f"sha256:{sub.get('sourceSha256', '')}")
                        if row is None:
                            self.err("missing-record", sw, "mẫu của lớp chưa có dòng trong licences.jsonl")
                            continue
                        self._check_row(sw, row, steps)
                    continue
                row = rows.get(layer.get("ledgerKey") or "") or rows.get(f"sha256:{layer.get('sourceSha256', '')}")
                if row is None:
                    self.err("missing-record", where, "nguồn của lớp chưa có dòng trong licences.jsonl")
                    self._licence_ok(where, lic)
                    continue
                if lic and policy.canonical(row.get("licence")) != lic:
                    self.err("missing-record", where, f"giấy phép lớp ({lic}) khác sổ nguồn ({row.get('licence')})")
                self._check_row(where, row, steps)
        for k, row in rows.items():  # rows not referenced by a record still must be clean
            if row.get("kind") in ("library", "model"):
                where = f"licences.jsonl › {k}"
                if row.get("kind") == "model":
                    if policy.model_denied(row.get("repo", "")) or row.get("commercial_ok") is False:
                        self.err("nc-model", where, f"sổ có trọng số phi thương mại: {row.get('repo')}")
                elif self._licence_ok(where, row.get("licence")) == "allowed" and row.get("commercial_ok") is False:
                    self.err("not-commercial", where, "thư viện commercial_ok=false")

    def run(self) -> list[Problem]:
        recs, rows = self._load()
        self._rows = rows
        if self.require_files:
            self._check_files(recs)
        self._check_records(recs, rows)
        return self.problems


# ---------------------------------------------------------------- targets

def _adopted(art: Path, public: Path | None) -> bool:
    if (art / "SOURCES.json").is_file() or (art / "licences.jsonl").is_file():
        return True
    man = public / "manifest.json" if public else None
    if man and man.is_file():
        try:
            return json.loads(man.read_text(encoding="utf-8")).get("version") == 2
        except (json.JSONDecodeError, AttributeError):
            return False
    return False


def targets(games: list[str] | None, staging: bool) -> list[tuple[str, Path, Path, Path]]:
    """(game, art-src/audio, released audio folder, game root)."""
    from common import env

    out = []
    for g in games or env.GAME_SLUGS:
        root = env.STAGING / g if staging else env.game_dir(g)
        out.append((g, root / "art-src" / "audio", root / release_dirs(g)[0], root))
    return out


def check(art_src: Path, public: Path | None = None, require_files: bool = True,
          legacy: dict[str, str] | None = None) -> list[Problem]:
    return Checker(art_src, public, require_files, legacy).run()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="licence-check", description="Kiểm giấy phép và nguồn gốc âm (mục 10.7).")
    ap.add_argument("--game", action="append", help="game slug (lặp được)")
    ap.add_argument("--staging", action="store_true", help="kiểm ~/AudioLab/review/staging/<game>")
    ap.add_argument("--art-src", type=Path, help="thư mục art-src/audio")
    ap.add_argument("--public", type=Path, help="thư mục public/assets/<game>/audio")
    ap.add_argument("--no-files", action="store_true", help="không quét file phát hành")
    ap.add_argument("--json", action="store_true", help="in JSON")
    ap.add_argument("--freeze-legacy", metavar="GAME", help="ghi lại danh sách file cũ được miễn từ git HEAD của game")
    a = ap.parse_args(argv)

    if a.freeze_legacy:
        n = freeze_legacy(a.freeze_legacy)
        print(f"licence-check: {n} file cũ của {a.freeze_legacy} ghi vào {LEGACY_FILE}")
        return 0
    legacy_all = load_legacy()
    if a.art_src:
        if not a.art_src.is_dir():
            print(f"licence-check: không có thư mục {a.art_src}", file=sys.stderr)
            return 2
        jobs = [("(tùy chọn)", a.art_src, a.public, None)]
        explicit = True
    else:
        jobs = targets(a.game, a.staging)
        explicit = bool(a.game)
    report, errors, checked, legacy_n = [], 0, 0, 0
    for game, art, pub, root in jobs:
        legacy = legacy_all.get(game, {})
        if not explicit and not _adopted(art, pub):
            n_leg, probs = scan_unadopted(root, game, legacy) if root is not None and not a.no_files else (0, [])
            legacy_n += n_leg
            errors += sum(p.severity == "error" for p in probs)
            report.append({"game": game, "skipped": "chưa dùng đường ống âm (không có SOURCES.json/licences.jsonl)",
                           "legacy": n_leg, "problems": [asdict(p) for p in probs]})
            continue
        checked += 1
        probs = check(art, pub, require_files=not a.no_files, legacy=legacy)
        errors += sum(p.severity == "error" for p in probs)
        report.append({"game": game, "artSrc": str(art), "public": str(pub) if pub else None,
                       "problems": [asdict(p) for p in probs]})
    state = "TRƯỢT" if errors else ("ĐẠT" if checked else "BỎ QUA")
    if a.json:
        print(json.dumps({"ok": errors == 0, "state": state, "checked": checked, "errors": errors,
                          "legacy": legacy_n, "games": report}, ensure_ascii=False, indent=2))
    else:
        for item in report:
            probs = item["problems"]
            if "skipped" in item:
                extra = f"; {item['legacy']} file cũ được miễn (mục 16 #9)" if item.get("legacy") else ""
                print(f"[{item['game']}] bỏ qua: {item['skipped']}{extra}"
                      + (f"; {len(probs)} file không hồ sơ" if probs else ""))
            else:
                n_err = sum(p["severity"] == "error" for p in probs)
                print(f"[{item['game']}] {item['artSrc']}: {n_err} lỗi, {len(probs) - n_err} cảnh báo")
            for p in probs:
                tag = "LỖI" if p["severity"] == "error" else "chú ý"
                print(f"  {tag} {p['code']}: {p['where']}: {p['message']}")
        if state == "BỎ QUA":
            print("Kiểm giấy phép: BỎ QUA (chưa game nào có SOURCES.json để kiểm"
                  + (f"; {legacy_n} file cũ được miễn theo mục 16 #9" if legacy_n else "") + ")")
        else:
            print("Kiểm giấy phép: " + ("ĐẠT" if not errors else f"TRƯỢT ({errors} lỗi)")
                  + f" ({checked} game có hồ sơ)")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
