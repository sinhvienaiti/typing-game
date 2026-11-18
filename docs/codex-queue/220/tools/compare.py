"""So mọi trường summary theo khóa ải/bot/chế độ/director, không bỏ số lẻ."""
import json, hashlib, pathlib, sys
root = pathlib.Path(__file__).resolve().parents[4]
report = root / 'docs/codex-queue/220'
tmp = root / 'games/.wt-ts-codex/tmp/codex-220/runs'

def compare(a, b, stage='c1-s1'):
    left, right = json.loads(a.read_text()), json.loads(b.read_text())
    key = lambda c: (c['stage'], c['bot'], c['mode'], c['director'])
    left = {key(c): c['summary'] for c in left if c['stage'] == stage}
    right = {key(c): c['summary'] for c in right if c['stage'] == stage}
    diffs = []
    for k in sorted(left.keys() | right.keys()):
        l, r = left.get(k, {}), right.get(k, {})
        for field in sorted(l.keys() | r.keys()):
            if field not in l or field not in r or l.get(field) != r.get(field):
                diffs.append({'cell': k, 'field': field, 'expected': l.get(field), 'actual': r.get(field)})
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    return {'expected': str(a.relative_to(root)), 'actual': str(b.relative_to(root)), 'expectedCells': len(left), 'actualCells': len(right), 'changedCells': len({tuple(x['cell']) for x in diffs}), 'diffs': diffs, 'scope': stage + ' · mọi trường summary', 'projectedSummaryMatch': left == right, 'expectedSha256': sha(a), 'actualSha256': sha(b)}

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'repro':
        rows = [compare(root / f'docs/codex-queue/209/runs/v6-s{first}.json', tmp / f'v6-s{first}.json') for first in [1, 101]]
    else:
        best = sys.argv[2]
        rows = [compare((root / f'docs/codex-queue/209/runs/{v}-s{first}.json') if v in ['v0', 'v6'] else tmp / f'{v}-s{first}.json', tmp / f'x-{v}-s{first}.json') for v in ['v0', 'v6', best] for first in [1, 101]]
    out = report / ('evidence/v6-repro.json' if mode == 'repro' else 'evidence/four-stage-repro.json')
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps([{'cells': r['actualCells'], 'changed': r['changedCells'], 'fields': len(r['diffs']), 'wholeFileShaMatch': r['expectedSha256'] == r['actualSha256'], 'projectedSummaryMatch':r['projectedSummaryMatch']} for r in rows]))
    sys.exit(1 if any(r['diffs'] or r['actualCells'] != 36 for r in rows) else 0)
