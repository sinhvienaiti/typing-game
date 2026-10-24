"""Audio Lab build: layering engine, final chain, licence log.

  run.sh build render RECIPE.json [--run NAME] [--seed N] [--count N] [--spec CARD.yaml] [--out DIR]
  run.sh build validate RECIPE.json ...
  run.sh build release --run RUN_DIR [--variants 1,3,4] [--art-src DIR --public DIR]
  run.sh build licence-check [--game G] [--staging] [--art-src DIR --public DIR] [--json]
  run.sh build mark-ai --sources SOURCES.json --step critic:audiobox [--model REPO@REV] [--file KEY ...]
  run.sh build mark-ai --run RUN_DIR --from-critic CRITIC_OUT [...]   # every ai_step the critic reported
  run.sh build ledger add-model|add-acceptance|add-file|add-tool ...
  run.sh build synth NAME [--params JSON] [--seed N] --out FILE.wav
  run.sh build schema recipe|sources|licences
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from build import ledger, licence_check, policy


def _art_src(a) -> Path:
    from common import env

    if getattr(a, "art_src", None):
        return Path(a.art_src)
    if not getattr(a, "game", None):
        sys.exit("cần --art-src hoặc --game")
    return env.art_src_staging(a.game)


def cmd_render(a) -> int:
    from build import render

    rows = ledger.rows_by_key(ledger.read_rows(Path(a.ledger))) if a.ledger else None
    try:
        res = render.render(Path(a.recipe), out=a.out, run=a.run, libraries=a.libraries, seed=a.seed, count=a.count,
                            spec=a.spec, ledger_rows=rows, ogg=False if a.no_ogg else None)
    except (render.LicenceError, LookupError, FileNotFoundError) as e:
        print(f"Không dựng: {e}", file=sys.stderr)
        return 1
    if a.json:
        print(json.dumps(res.report, ensure_ascii=False, indent=2))
        return 0
    r = res.report
    print(f"Đã dựng {r['id']} ({r['game']}), {r['count']} biến thể, seed {r['seed']}, giới hạn: {r['limits']}")
    print(f"  Thư mục: {res.out}")
    for v in r["variants"]:
        f, c = v["final"], v["chain"]
        print(f"  v{v['variant']}: {f['durationMs']:.0f} ms, LUFS-M max {f['lufsMMax']}, đỉnh thật {f['truePeakDbtp']} dBTP, "
              f"đầu {f['headMs']} ms, ép {c.get('limiterGrDb', 0)} dB, thiếu {c.get('shortfallDb', 0)} dB"
              + ("" if v["aiInputAllowed"] else ", CẤM đưa vào AI"))
    for w in r["warnings"]:
        print(f"  chú ý: {w}")
    return 0


def cmd_validate(a) -> int:
    from build import recipe

    bad = 0
    for p in a.recipes:
        try:
            recipe.load(p)
            print(f"ĐẠT  {p}")
        except (recipe.RecipeError, json.JSONDecodeError) as e:
            bad += 1
            print(f"LỖI  {e}")
    return 1 if bad else 0


def cmd_release(a) -> int:
    from build import release

    run_dir = Path(a.run)
    report = json.loads((run_dir / "render.json").read_text(encoding="utf-8"))
    game = report["game"]
    a.game = a.game or game
    art = _art_src(a)
    pub = Path(a.public) if a.public else release.staging_public(game)
    variants = [int(x) for x in a.variants.split(",")] if a.variants else None
    out = release.release(run_dir, variants, art, pub)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


def cmd_mark_ai(a) -> int:
    sources = Path(a.sources) if a.sources else (Path(a.run) / "SOURCES.json" if a.run else None)
    if sources is None or not sources.is_file():
        sys.exit("cần --sources SOURCES.json hoặc --run RUN_DIR (có SOURCES.json)")
    if a.from_critic:
        from build import critic_link

        rows = Path(a.ledger) if a.ledger else sources.parent / ("licences.rows.jsonl" if a.run else "licences.jsonl")
        res = critic_link.apply(sources, [Path(d) for d in a.from_critic], rows)
        print(f"Đã ghi {res['steps']} bước AI cho {res['files']} hồ sơ; mô hình: {', '.join(res['models']) or '—'}; "
              f"dòng mô hình vào {rows.name}: {len(res['modelRows'])}; file chấm không khớp hồ sơ: {res['unmatched']}")
        return 0
    if not a.step:
        sys.exit("cần --step (hoặc --from-critic)")
    n = ledger.mark_ai_step(sources, a.step, a.file or None, a.model)
    print(f"Đã ghi bước AI '{a.step}' cho {n} hồ sơ")
    return 0


def _hf_weights_sha(repo: str, revision: str) -> str | None:
    from common import env

    snap = env.HF_HOME / "hub" / f"models--{repo.replace('/', '--')}" / "snapshots" / revision
    for name in ("model.safetensors", "pytorch_model.bin"):
        p = snap / name
        if p.is_symlink():
            blob = Path(p.readlink()).name
            if len(blob) == 64:
                return blob
    return None


def cmd_ledger(a) -> int:
    art = _art_src(a)
    if a.action == "add-model":
        if not a.repo:
            sys.exit("add-model cần --repo")
        if not a.revision:
            resolved = ledger.resolve_model(a.repo)
            if "@" not in resolved:
                sys.exit("không thấy revision trong HF cache; truyền --revision")
            a.revision = resolved.split("@", 1)[1]
        sha = a.sha256 or _hf_weights_sha(a.repo, a.revision)
        if not sha:
            sys.exit("không tìm được sha256 trọng số trong HF cache; truyền --sha256")
        row = ledger.model_row(a.repo, a.revision, a.licence, a.licence_url, sha, a.role, a.date)
    elif a.action == "add-tool":
        if not (a.name and a.version and (a.sha256 or a.path)):
            sys.exit("add-tool cần --name, --version và --sha256 hoặc --path (file để băm, vd. LICENSE gốc)")
        sha = a.sha256 or ledger.sha256_file(Path(a.path))
        row = ledger.tool_row(a.name, a.version, a.licence, a.licence_url, sha, a.date)
    elif a.action == "add-acceptance":
        row = ledger.acceptance_row(a.licence, a.version, a.who, a.file, art, a.licence_url, a.date)
    else:  # add-file
        path = Path(a.path)
        row = {"schema": ledger.LICENCE_SCHEMA_ID, "kind": "source", "origin": a.origin,
               "key": f"sha256:{ledger.sha256_file(path)}", "sha256": ledger.sha256_file(path), "file": path.name,
               "licence": policy.canonical(a.licence), "licenceUrl": a.licence_url, "licenceCopy": a.licence_copy,
               "date": a.date or ledger.today(), "commercial_ok": not a.not_commercial,
               "attribution_required": bool(a.attribution), "ai_input_allowed": not a.no_ai,
               "raw_redistribution_allowed": bool(a.raw_ok)}
        for k, v in (("attribution_text", a.attribution), ("author", a.author), ("url", a.url),
                     ("release_file", a.release_file), ("genai_preference", a.genai_preference)):
            if v:
                row[k] = v
    added = ledger.append_rows(art / "licences.jsonl", [row])
    ledger_path = art / "licences.jsonl"
    print(f"Đã thêm {row['key']} vào {ledger_path}" if added else f"{row['key']} đã có trong {ledger_path}")
    if row.get("attribution_required"):
        ledger.write_credits(art)
    return 0


def cmd_synth(a) -> int:
    import soundfile as sf

    from build import synth

    x = synth.generate(a.name, json.loads(a.params or "{}"), a.seed)
    out = Path(a.out).expanduser()
    out.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(out), x * 0.5, synth.SR, subtype="PCM_24")
    print(f"{a.out}: {len(x) / synth.SR * 1000:.0f} ms")
    return 0


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "licence-check":
        return licence_check.main(argv[1:])
    ap = argparse.ArgumentParser(prog="build", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("render", help="dựng công thức thành master WAV và OGG")
    p.add_argument("recipe")
    p.add_argument("--run")
    p.add_argument("--out", type=Path)
    p.add_argument("--seed", type=int)
    p.add_argument("--count", type=int)
    p.add_argument("--spec", type=Path)
    p.add_argument("--libraries", type=Path)
    p.add_argument("--ledger", help="licences.jsonl để tra khóa của nguồn file")
    p.add_argument("--no-ogg", action="store_true")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_render)

    p = sub.add_parser("validate", help="kiểm công thức theo schema")
    p.add_argument("recipes", nargs="+")
    p.set_defaults(fn=cmd_validate)

    p = sub.add_parser("release", help="đưa biến thể đã chọn vào art-src/public (mặc định: staging)")
    p.add_argument("--run", required=True)
    p.add_argument("--variants")
    p.add_argument("--game")
    p.add_argument("--art-src")
    p.add_argument("--public")
    p.set_defaults(fn=cmd_release)

    p = sub.add_parser("mark-ai", help="ghi một bước AI (vd. critic:audiobox) vào SOURCES.json")
    p.add_argument("--sources")
    p.add_argument("--run", help="thư mục một lần dựng (dùng SOURCES.json và licences.rows.jsonl trong đó)")
    p.add_argument("--step")
    p.add_argument("--model")
    p.add_argument("--file", action="append")
    p.add_argument("--from-critic", action="append", help="thư mục kết quả của run.sh critic (lặp lại được)")
    p.add_argument("--ledger", help="file licences jsonl nhận dòng mô hình (mặc định cạnh SOURCES.json)")
    p.set_defaults(fn=cmd_mark_ai)

    p = sub.add_parser("ledger", help="thêm dòng vào licences.jsonl")
    p.add_argument("action", choices=["add-model", "add-acceptance", "add-file", "add-tool"])
    p.add_argument("--game")
    p.add_argument("--art-src")
    p.add_argument("--licence", required=True)
    p.add_argument("--licence-url", required=True)
    p.add_argument("--date")
    p.add_argument("--repo")
    p.add_argument("--revision")
    p.add_argument("--role", default="critic", choices=["generate", "critic", "listener"])
    p.add_argument("--sha256")
    p.add_argument("--version")
    p.add_argument("--name", help="add-tool: tên công cụ")
    p.add_argument("--who")
    p.add_argument("--file", help="add-acceptance: đường dẫn trong art-src/audio")
    p.add_argument("--path", help="add-file: file nguồn; add-tool: file để băm")
    p.add_argument("--origin", default="owner-recording",
                   choices=["library", "freesound", "owner-recording", "other-recording", "generated", "purchased"])
    p.add_argument("--licence-copy", default="licences/owner-recordings.txt")
    p.add_argument("--attribution")
    p.add_argument("--author")
    p.add_argument("--url")
    p.add_argument("--release-file")
    p.add_argument("--genai-preference")
    p.add_argument("--no-ai", action="store_true")
    p.add_argument("--not-commercial", action="store_true")
    p.add_argument("--raw-ok", action="store_true")
    p.set_defaults(fn=cmd_ledger)

    p = sub.add_parser("synth", help="nghe thử một bộ tạo âm")
    p.add_argument("name")
    p.add_argument("--params")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--out", required=True)
    p.set_defaults(fn=cmd_synth)

    p = sub.add_parser("schema", help="in đường dẫn schema")
    p.add_argument("name", choices=["recipe", "sources", "licences"])
    p.set_defaults(fn=lambda a: print(ledger.SCHEMAS / f"{a.name}.schema.json") or 0)

    a = ap.parse_args(argv)
    return int(a.fn(a) or 0)


if __name__ == "__main__":
    sys.exit(main())
