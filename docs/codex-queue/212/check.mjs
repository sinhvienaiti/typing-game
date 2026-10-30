import { readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '../../..');
const read = p => readFileSync(resolve(root, p), 'utf8');

/** Validator for the exact 2020-12 vocabulary used by schema.json; fails closed on unknown keywords. */
export function validateList(value, schema) {
  const errors = [];
  const known = new Set(['$schema', 'title', 'type', 'enum', 'properties', 'required', 'additionalProperties', 'items', 'minimum', 'exclusiveMinimum', 'maximum', 'minLength', 'pattern']);
  function check(v, s, path) {
    for (const k of Object.keys(s)) if (!known.has(k)) errors.push(`${path}: unsupported schema keyword ${k}`);
    const types = Array.isArray(s.type) ? s.type : s.type ? [s.type] : [];
    const matches = t => t === 'null' ? v === null : t === 'array' ? Array.isArray(v) : t === 'object' ? v !== null && typeof v === 'object' && !Array.isArray(v) : t === 'integer' ? Number.isInteger(v) : t === 'number' ? typeof v === 'number' && Number.isFinite(v) : typeof v === t;
    if (types.length && !types.some(matches)) { errors.push(`${path}: type ${types.join('|')}`); return; }
    if (s.enum && !s.enum.some(x => Object.is(x, v))) errors.push(`${path}: enum`);
    if (typeof v === 'string') {
      if (s.minLength !== undefined && [...v].length < s.minLength) errors.push(`${path}: minLength`);
      if (s.pattern && !new RegExp(s.pattern, 'u').test(v)) errors.push(`${path}: pattern`);
    }
    if (typeof v === 'number') {
      if (s.minimum !== undefined && v < s.minimum) errors.push(`${path}: minimum`);
      if (s.exclusiveMinimum !== undefined && v <= s.exclusiveMinimum) errors.push(`${path}: exclusiveMinimum`);
      if (s.maximum !== undefined && v > s.maximum) errors.push(`${path}: maximum`);
    }
    if (Array.isArray(v) && s.items) v.forEach((x, i) => check(x, s.items, `${path}[${i}]`));
    if (v !== null && typeof v === 'object' && !Array.isArray(v)) {
      for (const k of s.required ?? []) if (!Object.hasOwn(v, k)) errors.push(`${path}.${k}: required`);
      for (const [k, x] of Object.entries(v)) {
        if (s.properties?.[k]) check(x, s.properties[k], `${path}.${k}`);
        else if (s.additionalProperties === false) errors.push(`${path}.${k}: additionalProperties`);
        else if (typeof s.additionalProperties === 'object') check(x, s.additionalProperties, `${path}.${k}`);
      }
    }
  }
  check(value, schema, '$');
  return errors;
}

/** All production constants come from assumptions. Fraction means expected usable yield, not a guarantee. */
export function calculateTakes(row, assumptions) {
  const hitsPerTake = row.shape === 'hits'
    ? Math.min(assumptions.maxHitsPerTake, Math.floor(assumptions.fileSeconds * 1000 / (row.targetMs.max + assumptions.silenceMs))) : 1;
  if (hitsPerTake < 1 || assumptions.usableFraction <= 0) throw new Error(`${row.id}: impossible take assumptions`);
  const takes = Math.ceil(row.variants / (hitsPerTake * assumptions.usableFraction)) + (row.priority === 'P0' ? assumptions.p0ReserveTakes : 0);
  return { hitsPerTake, takes };
}
export function calculateTotals(rows) {
  return { rows: rows.length, takes: rows.reduce((s, r) => s + r.takes, 0), byPriority: Object.fromEntries(['P0', 'P1', 'P2'].map(p => [p, rows.filter(r => r.priority === p).reduce((s, r) => s + r.takes, 0)])) };
}

/** Parse literal const arrays and their spreads from current source, never importing executable game code. */
export function readSoundIds() {
  const text = ['theme-audio', 'type-audio', 'gun-audio'].map(n => read(`games/typing-survival/src/audio/${n}.ts`)).join('\n');
  const expand = (name, chain = []) => {
    if (chain.includes(name)) throw new Error(`cyclic array: ${name}`);
    const body = text.match(new RegExp(`export const ${name}\\s*=\\s*\\[([\\s\\S]*?)\\] as const`))?.[1];
    if (body === undefined) throw new Error(`missing source array: ${name}`);
    return [...body.matchAll(/"([^"\n]+)"|\.\.\.([A-Z_]+)/g)].flatMap(m => m[1] ? [m[1]] : expand(m[2], [...chain, name]));
  };
  return expand('SOUND_IDS');
}
const q6 = /\b(?:pop|puff|balloon|thud|thump|toy|cartoon|retro|8-bit|chiptune)\b/i;
const oldEra = /\b(?:ship|spaceship|hull|industrial|corridor|turret)\b/i;
const negative = /\b(?:no|not|without|never|neither|nor|avoid|exclude|excluding|except|cannot|can't|don't|doesn't|isn't|aren't|won't)\b/i;
const viet = /(?<![\p{L}\p{N}_])(?:Đầu Đàn|Xung|Tia|Tán|Pháo|Lính|Bầy|Trâu|Khiên|Vỏ)(?![\p{L}\p{N}_])/u;
function scanText(value, path = '$', found = []) {
  if (typeof value === 'string' && viet.test(value)) found.push(`${path}: ${value}`);
  else if (Array.isArray(value)) value.forEach((v, i) => scanText(v, `${path}[${i}]`, found));
  else if (value && typeof value === 'object') for (const [k, v] of Object.entries(value)) if (k !== 'id') scanText(v, `${path}.${k}`, found);
  return found;
}
function mdBlocks(md) {
  const blocks = new Map();
  for (const m of md.matchAll(/^## `([^`]+)`\n([\s\S]*?)(?=^## |$(?![\s\S]))/gm)) {
    const prompt = m[2].match(/```text\n([\s\S]*?)\n```/);
    if (blocks.has(m[1])) throw new Error(`duplicate Markdown block: ${m[1]}`);
    if (prompt) blocks.set(m[1], prompt[1]);
  }
  return blocks;
}
export function audit(list, schema, soundIds, specIds, md) {
  const result = { schemaErrors: validateList(list, schema), missing: [], duplicates: [], unknown: [], promptErrors: [], vietnameseNames: scanText(list), markdownErrors: [], calculationErrors: [], specErrors: [] };
  // Schema failures may make all subsequent checks meaningless; preserve diagnostics instead of crashing.
  if (result.schemaErrors.length) return result;
  const all = [...list.rows, ...list.excluded, ...list.retired];
  const counts = new Map();
  all.forEach(x => counts.set(x.id, (counts.get(x.id) ?? 0) + 1));
  for (const [id, n] of counts) if (n > 1) result.duplicates.push(`${id}: ${n}`);
  const union = new Set([...soundIds, ...specIds]);
  for (const id of union) {
    const allowed = soundIds.includes(id) ? all : [...list.rows, ...list.retired];
    if (!allowed.some(r => r.id === id)) result.missing.push(id);
  }
  for (const id of counts.keys()) if (!union.has(id)) result.unknown.push(id);
  for (const r of list.rows) {
    if (/[^\x00-\x7f]/.test(r.prompt)) result.promptErrors.push(`${r.id}: non-ASCII`);
    for (const [kind, regex] of [['Q6', q6], ['old era', oldEra], ['negative', negative]]) if (regex.test(r.prompt)) result.promptErrors.push(`${r.id}: ${kind}: ${r.prompt.match(regex)[0]}`);
    if (r.targetMs.min > r.targetMs.max) result.schemaErrors.push(`${r.id}: min > max`);
    if (r.loop !== (r.shape === 'loop')) result.schemaErrors.push(`${r.id}: loop/shape disagree`);
    if (r.inbox !== `~/AudioLab/inbox/firefly/${list.game}/${r.id}/`) result.schemaErrors.push(`${r.id}: inbox`);
    if (r.specCard !== null && !specIds.includes(r.id)) result.specErrors.push(`${r.id}: missing spec`);
    try {
      const calc = calculateTakes(r, list.assumptions);
      for (const k of ['hitsPerTake', 'takes']) if (r[k] !== calc[k]) result.calculationErrors.push(`${r.id}: ${k} ${r[k]} != ${calc[k]}`);
    } catch (e) { result.calculationErrors.push(e.message); }
  }
  const calculated = calculateTotals(list.rows);
  if (JSON.stringify(calculated) !== JSON.stringify(list.totals)) result.calculationErrors.push('totals disagree');
  if (md !== undefined) {
    try {
      const blocks = mdBlocks(md);
      for (const r of list.rows) if (blocks.get(r.id) !== r.prompt) result.markdownErrors.push(`${r.id}: prompt/block differs`);
      for (const id of blocks.keys()) if (!list.rows.some(r => r.id === id)) result.markdownErrors.push(`${id}: extra block`);
      const table = [...md.matchAll(/^\| `([^`]+)` \|/gm)].map(m => m[1]);
      for (const id of union) if (table.filter(x => x === id).length !== 1) result.markdownErrors.push(`${id}: table occurrence count`);
      for (const id of table) if (!counts.has(id)) result.markdownErrors.push(`${id}: extra table id`);
      const summary = [...md.matchAll(/^\| `([^`]+)` \| ([^|]+) \| (P[012]) \| (\d+) \|$/gm)];
      for (const r of list.rows) {
        const entry = summary.find(m => m[1] === r.id);
        if (!entry || entry[2].trim() !== (r.playerName ?? '—') || entry[3] !== r.priority || Number(entry[4]) !== r.takes) result.markdownErrors.push(`${r.id}: summary differs`);
      }
      if (!md.includes(`**${list.rows.length} hàng · ${list.totals.takes} lượt dự kiến**`)) result.markdownErrors.push('Markdown totals differ');
    } catch (e) { result.markdownErrors.push(e.message); }
  }
  return result;
}
function main() {
  const list = JSON.parse(read('docs/games/audio/firefly/typing-survival.json'));
  const schema = JSON.parse(read('docs/games/audio/firefly/schema.json'));
  const soundIds = readSoundIds();
  const specIds = readdirSync(resolve(root, 'tools/audio-lab/specs/typing-survival')).filter(f => f.endsWith('.yaml')).map(f => f.slice(0, -5));
  const md = read('docs/games/audio/firefly/typing-survival.md');
  const result = audit(list, schema, soundIds, specIds, md);
  // Source-card equality, including deliberately null duration fallback.
  for (const r of list.rows) if (r.specCard) {
    const text = read(r.specCard);
    for (const k of ['min', 'max']) {
      const val = text.match(new RegExp(`^  ${k}_ms: (\\d+|null)$`, 'm'))?.[1];
      if (val && val !== 'null' && Number(val) !== r.targetMs[k]) result.specErrors.push(`${r.id}: ${k} differs from spec`);
    }
    const val = text.match(/^variants:\s*\n\s+target: (\d+)/m)?.[1];
    if (val && Number(val) !== r.variants) result.specErrors.push(`${r.id}: variants differ from spec`);
  }
  let selftest;
  if (process.argv.includes('--selftest')) {
    const tests = [
      ['missing row', x => x.rows.splice(0, 1), r => r.missing.length > 0],
      ['forbidden pop', x => { x.rows[0].prompt += ' pop'; }, r => r.promptErrors.some(e => e.includes('Q6'))],
      ['unknown id', x => { x.rows.push({ ...x.rows[0], id: 'unknown.injected' }); }, r => r.unknown.includes('unknown.injected')],
    ];
    selftest = tests.map(([name, mutate, caught]) => { const x = structuredClone(list); mutate(x); return { name, caught: caught(audit(x, schema, soundIds, specIds)) }; });
  }
  const longest = [...list.rows].sort((a,b) => b.prompt.length - a.prompt.length)[0];
  const counts = Object.fromEntries(Object.entries(result).map(([k,v]) => [k, v.length]));
  const summary = { soundIds: soundIds.length, specIds: specIds.length, specOnly: specIds.filter(x => !soundIds.includes(x)), codeOnly: soundIds.filter(x => !specIds.includes(x)), rows: list.rows.length, excluded: list.excluded.length, excludedByReason: Object.fromEntries([...new Set(list.excluded.map(x => x.reason))].map(reason => [reason, list.excluded.filter(x => x.reason === reason).length])), retired: list.retired.length, counts, totals: list.totals, longestPrompt: { id: longest.id, characters: longest.prompt.length }, ...(selftest ? { selftest, selftestPassed: selftest.filter(x => x.caught).length } : {}), details: result };
  const ok = Object.values(counts).every(n => n === 0) && (!selftest || selftest.every(x => x.caught));
  const output = JSON.stringify({ ok, ...summary }, null, 2) + '\n';
  // Only the direct CLI writes the ticket's requested outputs. Imports have no side effects.
  const suffix = selftest ? '-selftest' : '';
  writeFileSync(resolve(here, `check${suffix}.json`), output);
  const lines = [`${ok ? 'PASS' : 'FAIL'} · Phiếu 212`, `SOUND_IDS=${soundIds.length}; spec=${specIds.length}; rows=${list.rows.length}; excluded=${list.excluded.length}; retired=${list.retired.length}`, ...Object.entries(counts).map(([k,v]) => `${k}=${v}`), `takes=${list.totals.takes}; P0=${list.totals.byPriority.P0}; P1=${list.totals.byPriority.P1}; P2=${list.totals.byPriority.P2}`, `longestPrompt=${longest.id}: ${longest.prompt.length} ASCII characters`, ...(selftest ? selftest.map(t => `${t.caught ? 'CAUGHT' : 'MISSED'} ${t.name}`) : []), ...(selftest ? [`selftest=${selftest.filter(x => x.caught).length}/3`] : []), ...(!ok ? [output] : [])].join('\n') + '\n';
  writeFileSync(resolve(here, `check${suffix}.txt`), lines);
  process.stdout.write(lines);
  process.exitCode = ok ? 0 : 1;
}
if (process.argv[1] && pathToFileURL(resolve(process.argv[1])).href === import.meta.url) main();
