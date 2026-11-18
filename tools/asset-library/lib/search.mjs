// Lõi thuần, không I/O. Node và trang nhúng truyền cùng catalog + taxonomy JSON:
// const index = createSearch(catalog, { taxonomy });
// index.search('chòi', { type: '3d', limit: 6 }) -> [{ card, score }].
// Không đổi thẻ đầu vào; tạo lại index sau khi catalog/taxonomy thay đổi.

// Giữ đúng STOP của tools/tripo-match/match.mjs; không import module có I/O đó.
export const STOP = Object.freeze(['3d', 'model', 'glb', 'png', 'alpha', 'flat', 'front', 'back', 'left',
  'stylized', 'fantasy', 'cartoon', 'with', 'the', 'of', 'a', 'an', 'cua', 'va', 'o']);
const stop = new Set(STOP);
export const WEIGHTS = Object.freeze({ name: 5, aliases: 4, subkind: 3, kind: 3, tags: 2, text: 1 });
const hiddenStatuses = new Set(['draft', 'rejected', 'review']);
const hiddenRoles = new Set(['draft', 'rejected', 'review', 'glb-spare', 'unknown']);
const array = value => value == null ? [] : Array.isArray(value) ? value : [value];
const cmp = (a, b) => a < b ? -1 : a > b ? 1 : 0;
const words = text => String(text ?? '').replace(/([\p{Ll}\d])(\p{Lu})/gu, '$1 $2')
  .replace(/(\p{Lu})(\p{Lu}\p{Ll})/gu, '$1 $2').toLowerCase().normalize('NFC').match(/[\p{L}\p{M}\d]+/gu) ?? [];
export const unaccent = text => String(text ?? '').toLowerCase().normalize('NFD').replace(/\p{M}/gu, '').replace(/đ/gu, 'd');
export const normalize = text => words(text).map(unaccent).join(' ');
export const tokenize = text => [...new Set(words(text).map(unaccent).filter(w => !stop.has(w) && !/^\d+$/u.test(w)))];

function inScope(folder, scope) {
  const colon = scope.indexOf(':');
  const game = colon < 0 ? '' : scope.slice(0, colon);
  const wanted = (colon < 0 ? scope : scope.slice(colon + 1)).replace(/\/+$/u, '');
  const split = folder.indexOf(':');
  if (game && game !== folder.slice(0, split)) return false;
  const parts = folder.slice(split + 1).split('/');
  return parts.some((_, i) => (i === 0 || !game) &&
    (parts.slice(i).join('/') === wanted || parts.slice(i).join('/').startsWith(wanted + '/')));
}

function vocabulary(taxonomy) {
  const aliases = new Map();
  // Khớp có dấu trước: gõ = click, gỗ = wood; chữ go không dấu theo nhóm wood.
  for (const group of taxonomy.synonyms ?? []) {
    const canonical = normalize(group[0]);
    for (const value of group) aliases.set(words(value).join(' '), canonical);
  }
  const fallback = new Map();
  for (const [alias, canonical] of aliases) if (!fallback.has(unaccent(alias))) fallback.set(unaccent(alias), canonical);
  const scopes = Object.entries(taxonomy.viTokens ?? {});
  const maxPhrase = Math.max(1, ...[...aliases.keys()].map(a => a.split(' ').length));
  function tokens(text, scope) {
    const input = words(text), result = new Set();
    for (let i = 0; i < input.length;) {
      let consumed = false;
      for (let n = Math.min(maxPhrase, input.length - i); n > 0; n--) {
        const raw = input.slice(i, i + n).join(' '), plain = unaccent(raw);
        const scoped = scopes.find(([key]) => key === raw);
        let canonical;
        if (scoped) canonical = scope.has(scoped[0]) ? normalize(scoped[1].word) : plain;
        else canonical = aliases.get(raw) ?? fallback.get(plain);
        if (canonical !== undefined) {
          result.add(canonical); i += n; consumed = true; break;
        }
      }
      if (!consumed) { const w = unaccent(input[i++]); if (!stop.has(w) && !/^\d+$/u.test(w)) result.add(w); }
    }
    return result;
  }
  const related = new Map();
  for (const [a, b] of taxonomy.related ?? []) {
    const left = [...tokens(a, new Set())][0], right = [...tokens(b, new Set())][0];
    if (!left || !right || left === right) continue;
    if (!related.has(left)) related.set(left, new Set());
    if (!related.has(right)) related.set(right, new Set());
    related.get(left).add(right); related.get(right).add(left);
  }
  return { tokens, related, scopes };
}

const activeFiles = card => array(card.files).filter(f => !hiddenRoles.has(f.role) && !hiddenStatuses.has(f.status));
const runtimeFile = f => /^runtime(?:-|$)/u.test(f.role ?? '');
const hasRuntime = card => card.pipeline === 'runtime' || activeFiles(card).some(runtimeFile);
const isModel = card => ['3d', 'model3d'].includes(card.type);

function has(card, feature) {
  const files = activeFiles(card);
  switch (feature) {
    case 'glb': return isModel(card) || files.some(f => /\.glb$/iu.test(f.path ?? ''));
    case 'runtime': return hasRuntime(card);
    case 'clips': return array(card.model?.clips).length > 0 || files.some(f => array(f.glb?.clips).length > 0);
    case 'rig': return card.model?.skinned === true || files.some(f => f.glb?.skinned === true);
    case 'prompt': return Boolean(card.provenance?.prompt) || files.some(f => f.role === 'prompt');
    case 'icon': return files.some(f => /^icon(?:-|$)/u.test(f.role ?? ''));
    default: throw new Error(`Khả năng không hỗ trợ: ${feature}`);
  }
}

// Ưu tiên số đo runtime (high, rồi medium), sau đó GLB gốc như cột CLI §5.2.
function triangles(card) {
  const t = card.model?.triangles;
  if (typeof t === 'number') return t;
  const runtime = hasRuntime(card);
  const candidates = runtime ? [t?.high, t?.medium, t?.original] : [t?.original, t?.high, t?.medium];
  const value = candidates.find(v => typeof v === 'number' && Number.isFinite(v));
  if (value !== undefined) return value;
  const tierRank = f => f.role === 'runtime-high' ? 0 : runtimeFile(f) ? 1 : f.role === 'glb-original' ? 2 : 3;
  const files = activeFiles(card).slice().sort((a, b) => tierRank(a) - tierRank(b));
  return files.map(f => f.glb?.triangles).find(v => typeof v === 'number' && Number.isFinite(v));
}

function qualityScore(card) {
  const q = card.quality ?? {};
  const value = card.type === 'audio' || card.type === 'music' ? q.score : isModel(card) ? q.score3d : q.score2d;
  return typeof value === 'number' && Number.isFinite(value) ? value : undefined;
}

const filterKeys = new Set(['type', 'kind', 'sub', 'tag', 'biome', 'style', 'game', 'used-by', 'status',
  'pipeline', 'min-score', 'max-tris', 'has', 'drive', 'all', 'requested', 'json', 'limit']);
const keyAliases = { subkind: 'sub', usedBy: 'used-by', minScore: 'min-score', maxTris: 'max-tris' };
function prepareFilters(input) {
  const f = {};
  for (const [raw, value] of Object.entries(input)) {
    const key = keyAliases[raw] ?? raw.replace(/^--/u, '');
    if (!filterKeys.has(key)) throw new Error(`Bộ lọc không hỗ trợ: ${raw}`);
    f[key] = value;
  }
  for (const key of ['min-score', 'max-tris', 'limit']) if (f[key] !== undefined) {
    const raw = f[key]; f[key] = Number(raw);
    if (raw === null || raw === '' || typeof raw === 'boolean' || !Number.isFinite(f[key]) || f[key] < 0 || (key === 'limit' && !Number.isInteger(f[key]))) {
      throw new Error(`Bộ lọc ${key} phải là số không âm${key === 'limit' ? ' nguyên' : ''}`);
    }
  }
  for (const key of ['all', 'requested']) if (f[key] !== undefined && typeof f[key] !== 'boolean') throw new Error(`${key} phải là boolean`);
  for (const feature of array(f.has)) if (!['glb', 'runtime', 'clips', 'rig', 'prompt', 'icon'].includes(feature)) throw new Error(`Khả năng không hỗ trợ: ${feature}`);
  return f;
}

function matches(card, f) {
  if (card.status === 'requested') { if (!f.requested) return false; }
  else if (!f.all && (hiddenStatuses.has(card.status) || card.hidden === true ||
    array(card.files).some(file => /(?:^|\/)AudioLab\/work\//u.test(file.path ?? '')))) return false;
  for (const [key, value] of [['type', isModel(card) ? '3d' : card.type], ['kind', card.kind], ['sub', card.subkind],
    ['style', card.style], ['game', card.origin], ['status', card.status], ['pipeline', card.pipeline]]) {
    if (f[key] !== undefined && !array(f[key]).map(v => v === 'model3d' ? '3d' : v).includes(value)) return false;
  }
  for (const [key, values] of [['tag', array(card.tags)], ['biome', array(card.biome)]]) {
    if (f[key] !== undefined && !array(f[key]).every(v => values.includes(v))) return false;
  }
  if (f['used-by'] !== undefined && !array(f['used-by']).every(game => array(card.usedBy).some(u => u.game === game))) return false;
  if (f['min-score'] !== undefined && !(qualityScore(card) >= f['min-score'])) return false;
  if (f['max-tris'] !== undefined && !(triangles(card) <= f['max-tris'])) return false;
  if (f.has !== undefined && !array(f.has).every(feature => has(card, feature))) return false;
  if (f.drive !== undefined && !activeFiles(card).some(file => array(f.drive).includes(file.onDrive))) return false;
  return true;
}

/** Index trong RAM; kết quả là thẻ gốc kèm điểm, thứ tự hòa điểm ổn định. */
export function createSearch(catalog, { taxonomy } = {}) {
  if (!taxonomy || typeof taxonomy !== 'object') throw new TypeError('Cần truyền taxonomy JSON vào createSearch');
  const cards = Array.isArray(catalog) ? catalog : catalog?.cards;
  if (!Array.isArray(cards)) throw new TypeError('Catalog phải là mảng thẻ hoặc { cards: [] }');
  const vocab = vocabulary(taxonomy);
  const rows = cards.map(card => {
    const folder = String(card.uid ?? '').slice(0, String(card.uid ?? '').lastIndexOf('/'));
    const scope = new Set(vocab.scopes.filter(([, rule]) => rule.folders.some(s => inScope(folder, s))).map(([key]) => key));
    const fields = {
      name: card.name || String(card.uid ?? '').split('/').at(-1).split(':').at(-1),
      aliases: [card.aliases, card.nameVi, card.meaning].flat().filter(Boolean).join(' '),
      subkind: card.subkind, kind: card.kind, tags: array(card.tags).join(' '),
      text: [card.uid, card.path, ...activeFiles(card).map(f => f.path),
        card.provenance?.tripoFile, card.provenance?.description, card.description].filter(Boolean).join(' '),
    };
    const kinds = taxonomy.kinds?.[isModel(card) || card.type === 'image' ? 'visual' : 'audio'];
    const classification = Number(Boolean(kinds?.[card.kind])) + Number(Boolean(kinds?.[card.kind]?.subkinds?.[card.subkind]));
    return { card, scope, scopeKey: [...scope].join('|'), classification,
      fields: Object.entries(fields).map(([key, value]) => [WEIGHTS[key], vocab.tokens(value, scope)]),
      bonus: (['shipped', 'pass'].includes(card.status) ? 1 : card.status === 'provisional' ? -0.5 : 0) + (hasRuntime(card) ? 0.5 : 0) };
  });
  return Object.freeze({
    search(query = '', filters = {}) {
      const f = prepareFilters(filters), queries = new Map(), result = [];
      for (const row of rows) {
        if (!matches(row.card, f)) continue;
        if (!queries.has(row.scopeKey)) queries.set(row.scopeKey, vocab.tokens(query, row.scope));
        const tokens = queries.get(row.scopeKey);
        let score = 0;
        // Mỗi trường góp tối đa trọng số của nó: nhiều alias/từ lặp không tự
        // nhân điểm. Trường chỉ khớp từ liên quan góp đúng nửa trọng số.
        for (const [weight, field] of row.fields) {
          let relevance = 0;
          for (const token of tokens) {
            if (field.has(token)) { relevance = 1; break; }
            if ([...(vocab.related.get(token) ?? [])].some(other => field.has(other))) relevance = 0.5;
          }
          score += weight * relevance;
        }
        if (tokens.size && score === 0) continue;
        result.push({ card: row.card, score: score + row.bonus, classification: row.classification });
      }
      // Hòa điểm ưu tiên loại/loại con hợp taxonomy, sau đó uid.
      result.sort((a, b) => b.score - a.score || b.classification - a.classification || cmp(a.card.uid, b.card.uid));
      return (f.limit === undefined ? result : result.slice(0, f.limit)).map(({ card, score }) => ({ card, score }));
    },
  });
}

/** Tiện ích cho một lượt tìm; dùng createSearch khi tìm lặp trên trang. */
export function search(catalog, query = '', filters = {}, options = {}) {
  return createSearch(catalog, options).search(query, filters);
}
