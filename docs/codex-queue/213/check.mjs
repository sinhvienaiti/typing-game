import { readFileSync, writeFileSync, readdirSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { validateList, calculateTakes, calculateTotals } from '../212/check.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '../../..');
const read = p => readFileSync(resolve(root, p), 'utf8');
const json = p => JSON.parse(read(p));
const git = (...args) => execFileSync('git', ['-C', resolve(root, 'games/dragon-hold'), ...args], { encoding: 'utf8' });
function parseCatalog(text) {
 const out = new Map();
 for (const m of text.matchAll(/"([^"\n]+)": def\("([^"\n]+)", (\d), ([\d_]+),([^\n]*)/g)) out.set(m[1], { bus: m[2], lengthMs: Number(m[4].replaceAll('_', '')), loop: m[5].includes('loop: true') });
 if (out.size !== 83) throw new Error(`Catalog changed: ${out.size}; review parser and scope`);
 return out;
}
const mainText = read('games/dragon-hold/src/audio/catalog.ts');
const branchText = git('show', 'dh-vfx:src/audio/catalog.ts');
const catalogs = [parseCatalog(mainText), parseCatalog(branchText)];
if (!branchText.includes('export function foeSfx') || !branchText.includes('export const FOE_SFX_IDS') || !branchText.includes('return { spawn: prefix + "spawn", move: prefix + "move", attack: sounds.attack, hit: sounds.hit, death: sounds.death }')) throw new Error('foeSfx implementation changed; review expansion');
const slots = branchText.match(/FOE_SFX_SLOTS = \[([^\]]+)\]/)?.[1].match(/"([^"]+)"/g).map(s => JSON.parse(s));
if (JSON.stringify(slots) !== JSON.stringify(['spawn', 'move', 'attack', 'hit', 'death'])) throw new Error('FOE_SFX_SLOTS changed');
const foeIds = [];
for (const [file, prefix] of [['enemies', 'enemy'], ['generals', 'general']]) {
 const source = git('show', `dh-vfx:src/content/data/${file}.ts`);
 for (const m of source.matchAll(/^  "([^"\n]+)": \{/gm)) {
  const foe = m[1];
  const block = source.slice(m.index, source.indexOf('\n  },', m.index));
  if (file === 'enemies' && !block.includes(`sounds("${foe}"`)) throw new Error(`${foe}: sound helper changed`);
  if (file === 'generals') for (const slot of ['attack', 'hit', 'death']) if (!block.includes(`${slot}: "general.${foe}.${slot}"`)) throw new Error(`${foe}: custom sound id changed`);
  foeIds.push(...slots.map(slot => `${prefix}.${foe}.${slot}`));
 }
}
const union = new Set([...catalogs.flatMap(c => [...c.keys()]), ...foeIds]);
const fired = json('docs/codex-queue/213/fired-ids.json');
const evidence = json('docs/codex-queue/213/source-evidence.json');
const list = json('docs/games/audio/firefly/dragon-hold.json');
const schema = json('docs/games/audio/firefly/schema.json');
const md = read('docs/games/audio/firefly/dragon-hold.md');
const q6 = /\b(?:puff|pop|balloon|thump|thud|whoomph|poof|plop|whoomp|woomp|fwoomp|fwhoomp|thoomp|boing|bonk|toy|cartoon|retro|8-bit|chiptune)\b/i;
const negative = /\b(?:no|not|without|never|neither|nor|avoid|exclude|excluding|except|cannot|can't|don't|doesn't|isn't|aren't|won't)\b/i;
const partner = /\b(?:veo|kling|seedance|runway|ray|elevenlabs|suno|stable audio|ace-step|gemini)\b/i;
function field(text, pattern, id) {
 const match = text.match(pattern);
 if (!match) throw new Error(`${id}: missing spec field ${pattern}`);
 return match[1];
}
export function audit(value, markdown) {
 const r = { schemaErrors: validateList(value, schema), missing: [], unknown: [], duplicates: [], promptErrors: [], nonAscii: [], markdownErrors: [], sourceErrors: [], specErrors: [], calculationErrors: [], clipErrors: [] };
 if (r.schemaErrors.length) return r;
 const all = [...value.rows, ...value.excluded, ...value.retired];
 const counts = new Map();
 for (const x of all) counts.set(x.id, (counts.get(x.id) ?? 0) + 1);
 for (const [id, n] of counts) if (n > 1) r.duplicates.push(`${id}: ${n}`);
 for (const x of fired.ids) if (!counts.has(x.id)) r.missing.push(x.id);
 for (const x of fired.manifestOnly) if (!value.rows.some(z => z.id === x.id)) r.missing.push(x.id);
 for (const c of catalogs) for (const id of c.keys()) if (!counts.has(id)) r.missing.push(id);
 for (const row of value.rows) if (!union.has(row.id)) r.unknown.push(row.id);
 const allowedExclusions = new Set([...union, ...evidence.unregistered, 'music.forest', 'music.wave', 'music.surge', 'music.general']);
 for (const row of [...value.excluded, ...value.retired]) if (!allowedExclusions.has(row.id)) r.unknown.push(row.id);
 const groups = json('docs/codex-queue/213/groups.json');
 const fire = Object.values(groups)[0];
 const clipConfig = json('tools/vfx-flipbook/dragon-hold.json').clips;
 const snapshot = json('docs/codex-queue/213/source-snapshot.json');
 const sourceCalls = new Set([...snapshot['dh-vfx:src/view/fx.ts'].matchAll(/flip\.pick\("([^"]+)"([^\n]*)/g), ...snapshot['dh-vfx:src/view/skyfire.ts'].matchAll(/flip\.pick\("([^"]+)"([^\n]*)/g)].flatMap(m => [...(m[0].matchAll(/"([^"\n]+)"/g))].map(x => x[1])));
 sourceCalls.add('flame-trail');
 for (const row of value.rows) {
  for (const key of ['prompt', 'playerName']) if (row[key] && /[^\x00-\x7f]/.test(row[key])) r.nonAscii.push(`${row.id}.${key}`);
  for (const [kind, rx] of [['Q6', q6], ['negative', negative], ['partner', partner]]) if (rx.test(row.prompt)) r.promptErrors.push(`${row.id}: ${kind}: ${row.prompt.match(rx)[0]}`);
  const own = evidence.own[row.id]; const base = own?.fallback ?? row.id;
  const def = catalogs[own ? 1 : 0].get(base);
  if (!def) { r.sourceErrors.push(`${row.id}: source def missing`); continue; }
  if (row.bus !== def.bus || row.loop !== def.loop || row.loop !== (row.shape === 'loop')) r.sourceErrors.push(`${row.id}: bus/loop/shape`);
  if (!row.basis.some(b => b.includes(`lengthMs=${def.lengthMs};`))) r.sourceErrors.push(`${row.id}: catalog lengthMs basis`);
  if (row.branchOnly !== (own ? 'dh-vfx' : null)) r.sourceErrors.push(`${row.id}: branchOnly`);
  if (row.inbox !== `~/AudioLab/inbox/firefly/dragon-hold/${row.id}/`) r.sourceErrors.push(`${row.id}: inbox`);
  const path = `tools/audio-lab/specs/dragon-hold/${base}.yaml`;
  const spec = read(path);
  const min = Number(field(spec, /^  min_ms: (\d+)$/m, base));
  const max = Number(field(spec, /^  max_ms: (\d+)$/m, base));
  const variants = Number(field(spec, /^variants:\s*\n  target: (\d+)$/m, base));
  const mode = field(spec, /^  mode: ([^\n]+)$/m, base);
  const channels = field(spec, /^  channels: ([^\n]+)$/m, base);
  if (row.targetMs.min !== min || row.targetMs.max !== max || row.variants !== variants || row.targetMs.min > row.targetMs.max) r.specErrors.push(`${row.id}: targetMs/variants`);
  if (!row.basis.some(b => b.includes(`playback.channels=${channels}`) && b.includes(`playback.mode=${mode}`))) r.specErrors.push(`${row.id}: channels/mode basis`);
  if (row.specCard !== (own ? null : path)) r.specErrors.push(`${row.id}: specCard`);
  const calculated = calculateTakes(row, value.assumptions);
  if (row.takes !== calculated.takes || row.hitsPerTake !== calculated.hitsPerTake) r.calculationErrors.push(`${row.id}: takes`);
  if (!Array.isArray(row.clips) || !Object.hasOwn(row, 'clipsWhy')) { r.clipErrors.push(`${row.id}: clips missing`); continue; }
  if (!row.clips.length && !row.clipsWhy) r.clipErrors.push(`${row.id}: empty clips reason`);
  if (row.clips.length && row.clipsWhy !== null) r.clipErrors.push(`${row.id}: clipsWhy should be null`);
  if (fire.includes(row.id) && !row.voiceHint) r.clipErrors.push(`${row.id}: voiceHint`);
  for (const c of row.clips) {
   if (!sourceCalls.has(c.clip)) r.clipErrors.push(`${row.id}: clip not called: ${c.clip}`);
   if (clipConfig[c.clip] ? c.phase !== clipConfig[c.clip].phase : !(c.clip === 'smoke-column' && c.phase === 'F' && c.syncNote.includes('chưa khai báo'))) r.clipErrors.push(`${row.id}: clip phase: ${c.clip}`);
  }
 }
 if (JSON.stringify(value.totals) !== JSON.stringify(calculateTotals(value.rows))) r.calculationErrors.push('totals');
 for (const branch of ['main', 'dh-vfx']) {
  const commit = git('rev-parse', '--short', branch).trim();
  if (value.sourceCommits?.[branch] !== commit || fired.sourceCommits[branch] !== commit) r.sourceErrors.push(`${branch}: commit changed (${commit}); review and regenerate`);
 }
 if (git('branch', '--show-current').trim() !== 'main') r.sourceErrors.push('Game branch is not main');
 // Pin all git-object evidence, including the seven files named in the task.
 for (const [key, old] of Object.entries(snapshot)) {
  const current = git('show', key);
  if (old !== current) r.sourceErrors.push(`${key}: source differs from snapshot`);
 }
 const liveMainCatalog = git('show', 'main:src/audio/catalog.ts');
 if (mainText !== liveMainCatalog) r.sourceErrors.push('main checkout catalog differs from committed source');
 for (const entry of fired.ids) {
  if (!union.has(entry.id)) r.sourceErrors.push(`${entry.id}: fired id unknown`);
  if (!entry.sources.length) r.sourceErrors.push(`${entry.id}: callsite missing`);
  for (const ref of entry.sources) {
   const match = ref.match(/^(main|dh-vfx):games\/dragon-hold\/(.+):(\d+)$/);
   const source = match && snapshot[`${match[1]}:${match[2]}`];
   if (!source || !source.split('\n')[Number(match[3]) - 1]) r.sourceErrors.push(`${entry.id}: bad ref ${ref}`);
  }
 }
 if (foeIds.length !== fired.foeSfxTotal) r.sourceErrors.push('FOE_SFX_IDS count changed');
 if (markdown !== undefined) {
  const blocks = new Map();
  for (const m of markdown.matchAll(/^### `([^`]+)`\n([\s\S]*?)(?=^### |^## |$(?![\s\S]))/gm)) {
   if (blocks.has(m[1])) r.markdownErrors.push(`${m[1]}: duplicate block`);
   blocks.set(m[1], m[2].match(/```text\n([\s\S]*?)\n```/)?.[1]);
  }
  for (const row of value.rows) if (blocks.get(row.id) !== row.prompt) r.markdownErrors.push(`${row.id}: exact prompt differs`);
  for (const id of blocks.keys()) if (!value.rows.some(x => x.id === id)) r.markdownErrors.push(`${id}: extra block`);
  const table = [...markdown.matchAll(/^\| `([^`]+)` \|/gm)].map(m => m[1]);
  for (const id of counts.keys()) if (table.filter(x => x === id).length !== 1) r.markdownErrors.push(`${id}: table set/count`);
  for (const id of table) if (!counts.has(id)) r.markdownErrors.push(`${id}: extra table id`);
  if (!markdown.includes(`**${value.rows.length} hàng · ${value.totals.takes} lượt dự kiến**`)) r.markdownErrors.push('totals');
 }
 return r;
}
const result = audit(list, md);
let selftest;
if (process.argv.includes('--selftest')) {
 const tests = [
  ['bỏ một hàng phát', x => x.rows.splice(x.rows.findIndex(r => fired.ids.some(f => f.id === r.id)), 1), r => r.missing.length > 0],
  ['thêm id lạ', x => x.rows.push({ ...x.rows[0], id: 'unknown.injected' }), r => r.unknown.includes('unknown.injected')],
  ['thêm chữ có dấu vào prompt', x => { x.rows[0].prompt += ' lửa'; }, r => r.nonAscii.some(x => x.endsWith('.prompt'))],
 ];
 selftest = tests.map(([name, mutate, caught]) => { const x = structuredClone(list); mutate(x); return { name, caught: caught(audit(x)) }; });
}
const counts = Object.fromEntries(Object.entries(result).map(([k, v]) => [k, v.length]));
const ok = Object.values(counts).every(n => n === 0) && (!selftest || selftest.every(x => x.caught));
const summary = { ok, catalogMain: catalogs[0].size, catalogBranch: catalogs[1].size, foeSfxIds: foeIds.length, fired: fired.ids.length, manifestOnly: fired.manifestOnly.length, rows: list.rows.length, branchOnly: list.rows.filter(r => r.branchOnly).length, excluded: list.excluded.length, counts, totals: list.totals, sourceCommits: list.sourceCommits, ...(selftest ? { selftest, selftestPassed: selftest.filter(t => t.caught).length } : {}), details: result };
const lines = [`${ok ? 'PASS' : 'FAIL'} · Phiếu 213`, `catalog main=${catalogs[0].size}; dh-vfx=${catalogs[1].size}; FOE_SFX_IDS=${foeIds.length}`, `fired=${fired.ids.length}; manifestOnly=${fired.manifestOnly.length}; rows=${list.rows.length}; dh-vfx-only=${summary.branchOnly}; excluded=${list.excluded.length}`, `missing=${counts.missing}; unknown=${counts.unknown}; duplicates=${counts.duplicates}; schemaErrors=${counts.schemaErrors}`, ...Object.entries(counts).filter(([k]) => !['missing', 'unknown', 'duplicates', 'schemaErrors'].includes(k)).map(([k, n]) => `${k}=${n}`), `takes=${list.totals.takes}; P0=${list.totals.byPriority.P0}; P1=${list.totals.byPriority.P1}; P2=${list.totals.byPriority.P2}`, `main=${list.sourceCommits.main}; dh-vfx=${list.sourceCommits['dh-vfx']}`, ...(selftest ? selftest.map(t => `${t.caught ? 'CAUGHT' : 'MISSED'} ${t.name}`).concat(`selftest=${selftest.filter(t => t.caught).length}/3`) : []), ...(!ok ? [JSON.stringify(result, null, 2)] : [])].join('\n') + '\n';
const suffix = selftest ? '-selftest' : '';
writeFileSync(resolve(here, `check${suffix}.json`), JSON.stringify(summary, null, 2) + '\n');
writeFileSync(resolve(here, `check${suffix}.txt`), lines);
process.stdout.write(lines);
process.exitCode = ok ? 0 : 1;
