import hashlib, json, subprocess
from pathlib import Path
OUT = Path('docs/codex-queue/228')
QUERY = Path('shared/learning/query.mjs')
BRIDGE = Path('portal/src/learning/bridge.ts')
ART = Path('portal/src/game-card.ts')
projection = '''    ...(record.recentSamples === undefined ? {} : {
      recentSamples: record.recentSamples.map((sample) => ({
        occurredAt: sample.occurredAt,
        gameId: sample.gameId,
        activityType: sample.activityType,
        result: sample.result,
        hintUsed: sample.hintUsed,
      })),
    }),
'''
decode = '''      let decoded = path;
      for (;;) {
        // Reject encoded separators at every encoding depth.
        if (/%(?:2f|5c)/i.test(decoded)) return null;
        const next = decodeURIComponent(decoded);
        if (next === decoded) break;
        decoded = next;
      }
      if (
        !decoded.startsWith(prefix) ||
        ["..", "\\\\", "//", "?", "#"].some((part) => decoded.includes(part))
      ) return null;
'''
normalized = '''      const normalized = new URL(decoded, app);
      if (
        image.origin !== app.origin || !image.pathname.startsWith(prefix) ||
        normalized.origin !== app.origin || !normalized.pathname.startsWith(prefix)
      ) return null;'''
def once(source, old, new):
    assert source.count(old) == 1, repr(old)
    return source.replace(old, new, 1)
def errors(source):
    assert source.count('makeLearningError(requestId, "query-failed")') == 2
    source = source.replace('''    } catch {
      this.#post(
        target,''', '''    } catch (error) {
      this.#post(
        target,''')
    return source.replace('makeLearningError(requestId, "query-failed")', 'makeLearningError(requestId, "query-failed", errorText(error))')
def art(source):
    source = once(source, decode, '')
    return once(source, normalized, '      if (image.origin !== app.origin || !image.pathname.startsWith(prefix)) return null;')
cases = [
    ('f2', QUERY, lambda s: once(s, projection, ''), ['portal/tests/learning-lookup.test.mjs','shared/learning/lookup.test.mjs']),
    ('f3', BRIDGE, errors, ['portal/tests/learning-lookup.test.mjs','shared/learning/lookup.test.mjs']),
    ('f4', BRIDGE, lambda s: s.replace('lookupParsedLearningRecords', 'lookupLearningRecords'), ['portal/tests/learning-lookup.test.mjs','shared/learning/lookup.test.mjs']),
    ('f5', ART, art, ['portal/tests/game-card.test.mjs']),
]
results = []
for name, path, mutate, tests in cases:
    original = path.read_bytes()
    mutant = mutate(original.decode())
    assert mutant != original.decode()
    try:
        path.write_text(mutant)
        subprocess.run(['python3', str(OUT/'run.py'), name+'-mutation', 'node', '--test', '--test-name-pattern='+name.upper(), *tests], check=True)
        run = json.loads((OUT/(name+'-mutation.json')).read_text())
        assert run['exit'] == 1 and run['fail'] > 0, run
    finally:
        path.write_bytes(original)
    assert path.read_bytes() == original
    results.append({'finding':name.upper(), 'file':str(path), 'tests':run['tests'], 'pass':run['pass'], 'fail':run['fail'], 'exit':run['exit'], 'restoredSha256':hashlib.sha256(original).hexdigest()})
(OUT/'mutation.json').write_text(json.dumps(results, indent=2)+'\n')
print(json.dumps(results, indent=2))
