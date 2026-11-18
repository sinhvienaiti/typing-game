// Hàm thuần: bên gọi đọc taxonomy, SOURCES và preset rồi truyền dữ liệu qua ctx.
const IMAGE = /^(?:png|jpe?g|webp|avif|gif|svg|tga)$/iu;
const AUDIO = /^(?:wav|ogg|opus|mp3|m4a|flac|aiff?|aac)$/iu;
const DERIVATIVES = new Set(['alpha', 'flat', 'padded', 'seamless', 'trim', 'crop', 'coal', 'fix']);
const compare = (a, b) => a < b ? -1 : a > b ? 1 : 0;
const beneath = (path, folder) => path === folder || path.startsWith(folder + '/');
const leaf = path => path.slice(path.lastIndexOf('/') + 1);
const withoutExtension = path => path.replace(/\.[^./]+$/u, '');

function relative(input) {
  if (typeof input !== 'string' || !input || /[\0\r\n]/u.test(input)) {
    throw new TypeError('Cần đường dẫn tương đối không rỗng');
  }
  const path = input.replaceAll('\\', '/');
  if (path.startsWith('/') || /^[a-z]:/iu.test(path)
    || path.split('/').some(part => !part || part === '.' || part === '..')) {
    throw new TypeError('Đường dẫn phải tương đối, không chứa . hoặc ..');
  }
  return path.replace(/^art-src\//u, '');
}

const originalStem = path => withoutExtension(relative(path).replace(/^3d\//u, ''));

function contextLinks(ctx) {
  const images = new Map();
  const models = new Map();
  const stems = new Set(ctx.stems ?? []);
  for (const [path, row] of Object.entries(ctx.sources?.files ?? {})) {
    const stem = originalStem(path);
    stems.add(stem);
    if (row.image) images.set(withoutExtension(relative(row.image)), stem);
    for (const key of row.usedBy ?? []) {
      // Một số dòng usedBy là chú thích công cụ, không phải khóa manifest.
      if (/^[\w-]+\/[\w/-]+$/u.test(key)) {
        if (!models.has(key)) models.set(key, new Set());
        models.get(key).add(stem);
      }
    }
  }
  for (const [key, row] of Object.entries(ctx.preset?.models ?? {})) {
    if (!row.source) continue;
    const stem = originalStem(row.source);
    // Preset là nguồn có thẩm quyền, thắng usedBy cũ trong SOURCES.
    models.set(key, new Set([stem]));
    stems.add(stem);
  }
  return { images, models, stems };
}

function hasHyphenVariants(path, ctx) {
  if (typeof ctx.hyphenVariants === 'boolean') return ctx.hyphenVariants;
  if (Array.isArray(ctx.hyphenVariants)) {
    return ctx.hyphenVariants.some(folder => beneath(path, relative(folder).replace(/\/\*\*$/u, '')));
  }
  const folders = ctx.taxonomy?.folderMap?.[ctx.game] ?? {};
  const folder = Object.keys(folders).filter(key => beneath(path, key)).sort((a, b) => b.length - a.length)[0];
  return folders[folder]?.hyphenVariants === true;
}

function alphabeticVariant(number) {
  let n = Number(number);
  if (!Number.isSafeInteger(n) || n < 1) return null;
  let label = '';
  while (n > 0) {
    n--;
    label = String.fromCharCode(97 + n % 26) + label;
    n = Math.floor(n / 26);
  }
  return label;
}

function linkedStem(path, modelKey, byId, links, ctx) {
  const explicit = ctx.links;
  if (explicit && Object.hasOwn(explicit, path)) return explicit[path];
  if (modelKey) {
    const targets = links.models.get(modelKey);
    if (targets?.size === 1) return [...targets][0];
  }
  if (links.images.has(path)) return links.images.get(path);
  if (byId) {
    const matches = [...links.stems].filter(stem => leaf(stem) === leaf(path));
    if (matches.length === 1) return matches[0];
  }
  return path;
}

function parse(relPath, ctx, links) {
  const path = relative(relPath);
  const parts = path.split('/');
  let name = parts.pop();
  const folder = parts.join('/');
  const review = parts.some(part => part === '_review' || part.startsWith('review-vs') || part === '_from-downloads');
  const reportFolder = parts.some(part => part === '.reports' || part === '.campaign3d-model-cache');
  const spareFolder = parts.includes('tripo-spares');
  const normalizedIcon = beneath(folder, 'icons/normalized');
  const icon = beneath(folder, 'ui/icons') || normalizedIcon;
  const prompt = /\.prompt\.txt$/iu.test(name);
  if (prompt) name = name.replace(/\.prompt\.txt$/iu, '');
  let extension = prompt ? '' : name.match(/\.([^.]+)$/u)?.[1]?.toLowerCase() ?? '';
  if (!prompt) name = withoutExtension(name);
  else {
    const mediaExtension = name.match(/\.([^.]+)$/u)?.[1] ?? '';
    if (IMAGE.test(mediaExtension) || AUDIO.test(mediaExtension) || mediaExtension === 'glb') {
      extension = mediaExtension.toLowerCase();
      name = withoutExtension(name);
    }
  }

  let ticket = null;
  let rejected = false;
  let draft = false;
  let derivative = false;
  let tripo = false;
  let spare = false;
  let variant = null;
  let size = null;
  let view = null;
  let tier = null;
  name = name.replace(/\.rejected-([^.]+)/gu, (_, value) => {
    rejected = true;
    ticket ??= value;
    return '';
  });
  if (spareFolder) {
    name = name.replace(/\.r2-rejected(?=\.|$)/gu, () => { rejected = true; spare = true; return ''; });
    name = name.replace(/-old(?:\..*)?$/u, () => { spare = true; return ''; });
    name = name.replace(/\.raw-download-[^.]+/gu, () => { spare = true; return ''; });
  }
  // Tách từng token để các tổ hợp .tripo.rejected-012.v1.alpha vẫn cùng stem.
  const tokens = name.split('.');
  name = tokens.shift();
  for (const token of tokens) {
    if (/^(?:v|try)\d+$/u.test(token)) draft = true;
    else if (DERIVATIVES.has(token)) derivative = true;
    else if (token === 'tripo') tripo = true;
    else if (normalizedIcon && /^(?:64|256)$/u.test(token)) size = Number(token);
    else if (token === 'high' || token === 'medium') tier = token;
    else if (spareFolder && /^(?:alt|r2)$/u.test(token)) spare = true;
    else if (reportFolder && token === 'rig') { /* báo cáo rig dùng cùng khóa model */ }
    else name += '.' + token; // Không đoán hậu tố chưa biết.
  }
  const multiview = name.match(/_(front|back|left)$/u);
  if (multiview) {
    view = multiview[1];
    name = name.slice(0, -multiview[0].length);
  }
  const hyphen = name.match(/-v(\d+)$/u);
  const logicalFolder = folder.replace(/^3d\//u, '');
  if (hyphen && hasHyphenVariants(`${logicalFolder}/${name}`, ctx)) {
    const label = alphabeticVariant(hyphen[1]);
    if (label) { variant = label; name = name.slice(0, -hyphen[0].length); }
  }
  if (AUDIO.test(extension)) {
    const audioVariant = name.match(/(?:_(\d+)|_(rr\d+)|-(\d+)|(\d+))$/u);
    if (audioVariant) {
      variant = audioVariant.slice(1).find(value => value !== undefined);
      name = name.slice(0, -audioVariant[0].length);
    }
  }

  let stem = folder ? `${folder}/${name}` : name;
  let modelKey = null;
  if (reportFolder) {
    modelKey = name.replaceAll('__', '/');
    stem = 'models/' + modelKey;
  } else if (stem.startsWith('3d/')) stem = stem.slice(3);
  else if (stem.startsWith('models/')) modelKey = stem.slice(7);
  else if (stem.startsWith('public/') && extension === 'glb') {
    const keys = [...links.models.keys()].filter(key =>
      stem.endsWith('/' + key) || stem.endsWith('/' + key + '/' + leaf(key)));
    if (keys.length === 1) modelKey = keys[0];
  }
  stem = linkedStem(stem, modelKey, icon || spareFolder, links, ctx);

  let role = 'unknown';
  const media = IMAGE.test(extension) || AUDIO.test(extension) || extension === 'glb';
  // Nhật ký sinh ảnh cũ của Lời Gọi: chỉ nhận mẫu run/phiếu, không nhận mọi JSON.
  const generationReport = !folder && extension === 'json'
    && /^vs-(?:buildings|characters)-(?:run|\d+[a-z]?(?:-continuation)?)$/u.test(name);
  if (review) role = 'review';
  else if (prompt) role = 'prompt';
  else if (rejected) role = 'rejected';
  else if (generationReport || (reportFolder && extension === 'json')
    || (/^README/iu.test(name) && extension === 'md')) role = 'report';
  else if (media && draft) role = 'draft';
  else if (extension === 'glb') {
    if (spareFolder && spare) role = 'glb-spare';
    else if (path.startsWith('models/')) role = 'glb-processed';
    else if (path.startsWith('public/') && tier) role = 'runtime-' + tier;
    else if (path.startsWith('3d/')) role = 'glb-original';
  } else if (IMAGE.test(extension)) {
    if (view) role = 'multiview';
    else if (tripo) role = 'tripo-source';
    else if (derivative) role = 'derivative';
    else if (normalizedIcon && size) role = 'icon-' + size;
    else if (icon && !normalizedIcon && !name.includes('.')) role = 'icon';
    else if (!name.includes('.')) role = 'concept';
  } else if (AUDIO.test(extension)) role = 'variant';
  return { stem, role, variant, ticket, size, view, tier };
}

/**
 * ctx: { game, taxonomy, hyphenVariants?: boolean | string[],
 *   sources?: SOURCES.json, preset?: {models}, stems?: string[], links?: { [stem]: stem } }.
 * paths tương đối dưới art-src (có thể kèm art-src/) hoặc từ gốc game cho public/.
 * Giá trị không có là null; variant ảnh -v1/-v2 là a/b, âm giữ 001/rr1/1.
 * links ghi đè tường minh; stems dùng nối icon/spare theo id duy nhất, không đoán khi trùng id.
 * Sidecar giữ role prompt và metadata của tên; review thắng mọi vai trò bên trong.
 */
export function parsePath(relPath, ctx = {}) {
  return parse(relPath, ctx, contextLinks(ctx));
}

/** Trả [{stem, files: [{path, role, variant, ticket, size, view, tier}]}], sắp ổn định. */
export function groupFiles(paths, ctx = {}) {
  const input = [...new Set(paths)].sort(compare);
  const links = contextLinks(ctx);
  // Đợt đầu tìm các stem nguồn, để icon hoạt động cả khi chưa có SOURCES.
  for (const path of input) {
    const parsed = parse(path, ctx, links);
    const logical = relative(path);
    if (!/^(?:icons\/normalized|ui\/icons|tripo-spares|models|public)\//u.test(logical)
      && ['concept', 'tripo-source', 'multiview', 'derivative', 'draft', 'glb-original'].includes(parsed.role)) {
      links.stems.add(parsed.stem);
    }
  }
  const cards = new Map();
  for (const path of input) {
    const { stem, ...file } = parse(path, ctx, links);
    if (!cards.has(stem)) cards.set(stem, { stem, files: [] });
    cards.get(stem).files.push({ path, ...file });
  }
  return [...cards.values()].sort((a, b) => compare(a.stem, b.stem));
}
