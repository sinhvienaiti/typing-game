import { readFileSync } from 'node:fs';

const DEFAULT_FILE = new URL('../../../library/taxonomy.json', import.meta.url);
let cached;

const wordKey = word => typeof word === 'string'
  ? word.normalize('NFC').toLowerCase().trim().replace(/[\s_-]+/gu, ' ')
  : '';

function freeze(value) {
  if (value && typeof value === 'object') {
    Object.values(value).forEach(freeze);
    Object.freeze(value);
  }
  return value;
}

/** Đọc JSON tại chỗ, không ghi cache ra đĩa. fs có thể được bọc trong test. */
export function load({ file = DEFAULT_FILE, fs = { readFileSync } } = {}) {
  const data = JSON.parse(fs.readFileSync(file, 'utf8'));
  if (data.schemaVersion !== 1) throw new Error('Phiên bản taxonomy không được hỗ trợ');
  const seen = new Set();
  for (const group of data.synonyms) {
    for (const word of group) {
      const key = wordKey(word);
      if (!key || seen.has(key)) throw new Error(`Từ đồng nghĩa bị trùng: ${word}`);
      seen.add(key);
    }
  }
  return freeze(data);
}

const taxonomy = () => cached ??= load();

// folderMap dùng đường tương đối dưới art-src; ảnh và GLB dùng chung luật gương.
// Đường âm thanh public/ và src/ giữ nguyên vì nằm ngoài art-src.
function relativePath(input) {
  if (typeof input !== 'string') return null;
  const path = input.replaceAll('\\', '/').replace(/\/+$/u, '');
  if (path.startsWith('/') || /^[a-z]:/iu.test(path)) return null;
  if (path.split('/').some(part => !part || part === '.' || part === '..')) return null;
  return path.replace(/^art-src\//u, '').replace(/^3d\//u, '');
}

function folderParts(folder) {
  if (typeof folder !== 'string') return null;
  const colon = folder.indexOf(':');
  const game = colon < 0 ? null : folder.slice(0, colon);
  const path = relativePath(colon < 0 ? folder : folder.slice(colon + 1));
  return path ? { game, path } : null;
}

const beneath = (path, parent) => path === parent || path.startsWith(parent + '/');

function inScope(folder, scope) {
  const actual = folderParts(folder);
  const wanted = folderParts(scope);
  if (!actual || !wanted) return false;
  if (wanted.game) return actual.game === wanted.game && beneath(actual.path, wanted.path);
  // Scope không có game áp ở một thành phần thư mục, không khớp chuỗi con.
  return actual.path.split('/').some((_, i, parts) => beneath(parts.slice(i).join('/'), wanted.path));
}

/** Trả từ Anh chuẩn hoặc null. Giữ dấu để phân biệt gõ (click) và gỗ (wood). */
export function resolve(word, { folder } = {}) {
  const key = wordKey(word);
  if (!key) return null;
  const data = taxonomy();
  const scoped = Object.hasOwn(data.viTokens, key) ? data.viTokens[key] : null;
  if (scoped) return scoped.folders.some(scope => inScope(folder, scope)) ? scoped.word : null;
  for (const group of data.synonyms) {
    if (group.some(alias => wordKey(alias) === key)) return group[0];
  }
  return data.tags.find(tag => wordKey(tag) === key) ?? null;
}

/** Quan hệ đối xứng, trực tiếp; không gộp hai nhóm đồng nghĩa. */
export function related(a, b) {
  const left = resolve(a);
  const right = resolve(b);
  if (!left || !right) return false;
  return taxonomy().related.some(([x, y]) =>
    (left === x && right === y) || (left === y && right === x));
}

/** Trả kind hoặc null; nhận art-src/…, art-src/3d/…, 3d/… hay đường gương ngắn. */
export function kindFor(game, relPath) {
  const maps = taxonomy().folderMap;
  if (!Object.hasOwn(maps, game)) return null;
  const path = relativePath(relPath);
  if (!path) return null;
  const folders = maps[game];
  const folder = Object.keys(folders).filter(key => beneath(path, key))
    .sort((a, b) => b.length - a.length)[0];
  if (!folder) return null;
  const rule = folders[folder];
  if (rule.perItem && path !== folder) {
    const name = path.slice(path.lastIndexOf('/') + 1).split('.')[0];
    const stem = rule.hyphenVariants ? name.replace(/-v\d+$/u, '') : name;
    if (Object.hasOwn(rule.items ?? {}, stem)) return rule.items[stem].kind;
    const local = stem.replace(/^g\d{2}-/u, '');
    const prefix = Object.keys(rule.itemPrefixes ?? {}).filter(key =>
      local === key || local.startsWith(key + '-')).sort((a, b) => b.length - a.length)[0];
    if (prefix) return rule.itemPrefixes[prefix].kind;
  }
  return rule.kind;
}

/** Ngoài bốn game đã khai báo thì không đoán phong cách. td/ có override trong folderMap. */
export function styleFor(game) {
  const styles = taxonomy().gameStyles;
  return Object.hasOwn(styles, game) ? styles[game] : null;
}
