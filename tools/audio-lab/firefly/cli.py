"""Explicit-path Firefly CLI; no call to env.apply() and no implicit workspace."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import sys
from pathlib import Path

from build import ledger, policy

from .pipeline import GAMES, catalogue, component, ingest_id, under, write_json


def status(game, inbox, out, entries):
    rows, skipped = [], []
    folder = inbox / game
    unknown = sorted(p.name for p in folder.iterdir() if p.is_dir() and p.name not in entries) if folder.is_dir() else []
    for sid, info in entries.items():
        base = under(out, out / game / sid)
        runs = list(base.glob('*/firefly.json'))
        latest = max(runs, key=lambda p: (p.stat().st_mtime_ns, p.parent.name)) if runs else None
        doc = json.loads(latest.read_text(encoding='utf-8')) if latest else {}
        source = folder / sid
        files = list(source.iterdir()) if source.is_dir() else []
        rows.append({'id': sid, 'inboxFiles': sum(p.is_file() for p in files),
                     'inboxWav': sum(p.is_file() and p.suffix.lower() == '.wav' for p in files),
                     'latestRun': latest.parent.name if latest else None,
                     'found': doc.get('found', 0), 'passed': doc.get('passed', 0), 'selected': doc.get('selected', 0),
                     'variants': len(doc.get('variants', [])), 'expectedVariants': info['card']['variants'],
                     'finalGate': doc.get('finalGate', 'chưa có'), 'belowMin': doc.get('belowMin'),
                     'reasons': doc.get('errors', []) + doc.get('notes', []) + [f['reason'] for f in doc.get('files', []) if f.get('reason')],
                     'listen': (out / 'listen' / game / f'{sid}-20s.mp3').is_file()})
        skipped.extend({'id': sid, **f} for f in doc.get('files', []) if f.get('skipped'))
        for p in files:
            if not p.is_file() or p.suffix.lower() != '.wav':
                if not any(r['id'] == sid and r['file'] == p.name for r in skipped):
                    skipped.append({'id': sid, 'file': p.name, 'reason': 'không phải WAV'})
    for sid in unknown:
        skipped.extend({'id': sid, 'file': p.name, 'reason': 'id không có trong danh sách hoặc thẻ spec'}
                       for p in sorted((folder / sid).iterdir()))
    return {'schema': 'audiolab.firefly.status/1', 'game': game, 'ids': rows,
            'unknownIds': unknown, 'skippedFiles': skipped}


def parser():
    ap = argparse.ArgumentParser(prog='firefly', description='Nhận WAV Firefly của chủ dự án; inbox chỉ đọc.')
    subs = ap.add_subparsers(dest='command', required=True)
    for cmd in ('ingest', 'listen', 'status'):
        p = subs.add_parser(cmd)
        p.add_argument('--game', choices=GAMES, required=True)
        p.add_argument('--out', type=Path, required=True)
        if cmd != 'status':
            p.add_argument('--id')
        if cmd in ('ingest', 'status'):
            p.add_argument('--inbox', type=Path, required=True)
            p.add_argument('--list', type=Path)
        if cmd == 'ingest':
            p.add_argument('--run', default=dt.datetime.now().strftime('%Y%m%d-%H%M%S-%f'))
            p.add_argument('--split', choices=('auto', 'onset', 'whole'), default='auto')
            p.add_argument('--threshold-db', type=float, default=-35)
            p.add_argument('--min-gap-ms', type=float, default=150)
            p.add_argument('--pre-ms', type=float, default=5)
            p.add_argument('--tail-floor-db', type=float, default=-60)
            p.add_argument('--model', default='Adobe Firefly Audio Model')
            p.add_argument('--date')
        elif cmd == 'listen':
            p.add_argument('--slot', action='append', default=[])
        else:
            p.add_argument('--json', type=Path)
    return ap


def main(argv=None):
    ap = parser()
    args = ap.parse_args(argv)
    try:
        out = args.out.expanduser().resolve()
        if out.exists() and any(p.is_symlink() for p in out.rglob('*')):
            raise ValueError('--out chứa symlink; từ chối để bảo vệ inbox và giới hạn ghi')
        inbox = args.inbox.expanduser().resolve() if hasattr(args, 'inbox') else None
        if inbox:
            if inbox == out or inbox in out.parents or out in inbox.parents:
                raise ValueError('--inbox và --out phải tách rời, không chứa nhau')
            if not inbox.is_dir():
                raise ValueError('--inbox chưa có hoặc không phải thư mục')
        if getattr(args, 'id', None):
            component(args.id)
        if args.command == 'ingest':
            component(args.run)
            if args.run in ('takes', 'listen'):
                raise ValueError('--run trùng thư mục dành riêng')
            if not all(math.isfinite(v) for v in (args.threshold_db, args.min_gap_ms, args.pre_ms, args.tail_floor_db)):
                raise ValueError('Tham số tách cần số hữu hạn')
            if args.threshold_db >= 0 or args.tail_floor_db >= 0 or args.min_gap_ms <= 0 or args.pre_ms < 0:
                raise ValueError('Ngưỡng dB phải âm; gap > 0; pre >= 0')
            if args.date:
                dt.date.fromisoformat(args.date)
            if not policy.adobe_model_allowed(args.model):
                raise ValueError('--model chỉ cho phép Adobe Firefly Audio Model và phiên bản')
        entries = catalogue(args.game, getattr(args, 'list', None))
        if getattr(args, 'id', None):
            if args.id not in entries:
                raise ValueError(f'{args.id}: không có trong danh sách hoặc thẻ spec')
            entries = {args.id: entries[args.id]}
        if args.command == 'status':
            report = status(args.game, inbox, out, entries)
            print('ID | inbox | lần chạy | take/qua/chọn | biến thể/đích | final | MP3')
            for r in report['ids']:
                print(f"{r['id']} | {r['inboxFiles']} | {r['latestRun'] or '—'} | {r['found']}/{r['passed']}/{r['selected']} | "
                      f"{r['variants']}/{r['expectedVariants']['target']} | {r['finalGate']} | {r['listen']}")
                if r['reasons']:
                    print('  ' + '; '.join(r['reasons']))
            print('Id lạ: ' + ', '.join(report['unknownIds']))
            for f in report['skippedFiles']:
                print(f"Bỏ qua {f['id']}/{f['file']}: {f['reason']}")
            if args.json:
                write_json(under(out, args.json.expanduser()), report)
            return 0
        if args.command == 'ingest':
            # Process ids present in the inbox; status also shows every absent id.
            folder = inbox / args.game
            ids = [args.id] if args.id else [p.name for p in sorted(folder.iterdir()) if p.is_dir()] if folder.is_dir() else []
            before = {str(p.relative_to(inbox)): {'sha256': ledger.sha256_file(p), 'mtimeNs': p.stat().st_mtime_ns}
                      for p in sorted(inbox.rglob('*')) if p.is_file()}
            results, skipped = [], []
            for sid in ids:
                if sid not in entries:
                    skipped.append({'id': sid, 'reason': 'id không có trong danh sách hoặc thẻ spec'})
                    print(f'Bỏ qua {sid}: {skipped[-1]["reason"]}')
                    continue
                result = ingest_id(args.game, sid, entries[sid], inbox, out, args)
                results.append(result)
                print(f"{sid}: {result['found']} take, {result['passed']} qua, {result['selected']} chọn; "
                      f"final={result['finalGate']}" + ('; dưới min' if result['belowMin'] else ''))
            after = {str(p.relative_to(inbox)): {'sha256': ledger.sha256_file(p), 'mtimeNs': p.stat().st_mtime_ns}
                     for p in sorted(inbox.rglob('*')) if p.is_file()}
            unchanged = before == after
            write_json(under(out, out / args.game / 'ingest.json'),
                       {'run': args.run, 'ids': [r['id'] for r in results], 'skipped': skipped,
                        'inboxBefore': before, 'inboxAfter': after, 'inboxUnchanged': unchanged})
            return 0 if unchanged and all(r['ok'] for r in results) else 1
        from .listening import listen_id
        slots = {}
        for s in args.slot:
            sid, sep, filename = s.partition('=')
            if not sep or not filename:
                raise ValueError('--slot cần sid=FILE')
            slots[component(sid)] = Path(filename).expanduser().resolve()
            if not slots[sid].is_file():
                raise ValueError(f'Không có slot: {filename}')
        ids = [args.id] if args.id else [sid for sid in entries if (out / args.game / sid / 'takes.json').is_file()]
        errors = 0
        for sid in ids:
            try:
                doc = listen_id(args.game, sid, entries[sid], out, slots)
                print(f"{sid}: {doc['mode']}, {doc['duration_s']:.3f} s")
            except (OSError, ValueError, RuntimeError, KeyError) as e:
                print(f'{sid}: {e}', file=sys.stderr)
                errors += 1
        return 1 if errors else 0
    except (OSError, ValueError, KeyError, TypeError) as e:
        print(f'firefly: {e}', file=sys.stderr)
        return 2
