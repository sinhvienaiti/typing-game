import difflib, hashlib, json
from pathlib import Path
OUT=Path('docs/codex-queue/228')
before=json.loads((OUT/'hashes-before.json').read_text())
changed={f:Path(f).read_text() for f,h in before.items() if hashlib.sha256(Path(f).read_bytes()).hexdigest()!=h}
old=dict(changed)
f='shared/learning/query.mjs'; s=old[f]
a=s.index('    ...(record.recentSamples === undefined ? {} : {'); b=s.index('    entityType,',a); s=s[:a]+s[b:]
a=s.index('  return lookupParsedLearningRecords(profileInput, parseLearningLookup(lookupInput), now);');b=s.index('  const collection = collectionFor(profile, lookup.entityType);',a)
s=s[:a]+'  const profile = viewLearningProfile(profileInput);\n  const lookup = parseLearningLookup(lookupInput);\n'+s[b:]
s=s.replace('''      recentSamples: [],
      ...queryItem(record, lookup.entityType, now),''','''      ...queryItem(record, lookup.entityType, now),
      recentSamples: record.recentSamples ?? [],'''); old[f]=s
f='shared/learning/query.d.mts';s=old[f];a=s.index('/** Accepts the result of parseLearningLookup. */');b=s.index('\nexport type LearningStatus',a);old[f]=s[:a]+s[b:]
f='shared/learning/message-contract.mjs';old[f]=old[f].replace('''      ...(message === undefined ? {} : {
        message: typeof message === "string"
          ? message.slice(0, 300)
          : "Learning request failed",
      }),''','''      message:
        typeof message === "string"
          ? message.slice(0, 300)
          : "Learning request failed",''')
f='shared/learning/message-contract.d.mts';old[f]=old[f].replace('  message?: string,','  message: string,').replace('error: { code: string; message?: string };','error: { code: string; message: string };')
f='portal/src/learning/bridge.ts';s=old[f].replace('lookupParsedLearningRecords','lookupLearningRecords').replace('''    } catch {
      this.#post(
        target,''','''    } catch (error) {
      this.#post(
        target,''')
s=s.replace('''        makeLearningError(requestId, "query-failed"),''','''        makeLearningError(
          requestId,
          "query-failed",
          errorText(error),
        ),''',1)
s=s.replace('makeLearningError(requestId, "query-failed")','makeLearningError(requestId, "query-failed", errorText(error))');old[f]=s
f='portal/src/game-card.ts';s=old[f];a=s.index('      let decoded = path;');b=s.index('      const app = new URL(game.appUrl);',a);s=s[:a]+s[b:]
a=s.index('      const normalized = new URL(decoded, app);');b=s.index('      return image.href;',a)
s=s[:a]+'''      // Check again after URL normalization, including encoded dot segments.
      if (image.origin !== app.origin || !image.pathname.startsWith(prefix)) return null;
'''+s[b:];old[f]=s
f='portal/tests/game-card.test.mjs';old[f]=old[f].split('\nfor (const suffix of [\n  "%2e%2e/a.png",')[0]
f='portal/tests/learning-lookup.test.mjs';old[f]=old[f].split('\nfor (const [entityType, collection] of [["vocabulary", "vocabulary"],')[0].replace('import { parseLearningProfileBackup } from "../../shared/learning/profile-backup.mjs";\n','')
f='shared/learning/lookup.test.mjs';s=old[f];a=s.rfind('\nfor (const [entityType, collection]',0,s.index('test(`F2'));old[f]=s[:a]
for f,s in old.items():
 assert hashlib.sha256(s.encode()).hexdigest()==before[f], f
(OUT/'task.diff').write_text(''.join(''.join(difflib.unified_diff(old[f].splitlines(True),changed[f].splitlines(True),fromfile='a/'+f,tofile='b/'+f,n=0)) for f in sorted(changed)))
(OUT/'product-files.txt').write_text('\n'.join(sorted(changed))+'\n')
print('Validated initial SHA-256 for',len(old),'files; task.diff contains only ticket 228 changes.')
