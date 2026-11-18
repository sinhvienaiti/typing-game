import path from 'node:path';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { createHash } from 'node:crypto';

const exec = promisify(execFile);
const cmp = (a, b) => a < b ? -1 : a > b ? 1 : 0;
const stemOf = p => p.replace(/^art-src\/(?:3d\/)?|^3d\//u, '').replace(/\.[^/.]+$/u, '');
const media = /\.(?:png|jpe?g|webp|avif|gif|svg|tga|glb)$/iu;
export const catalogFile = p => media.test(p) || /\.prompt\.txt$/iu.test(p)
  || /(?:^|\/)README[^/]*\.md$/iu.test(p)
  || /\/(?:\.reports|\.campaign3d-model-cache)\/[^/]+\.json$/iu.test(p)
  || /\/vs-(?:buildings|characters)-(?:run|\d+[a-z]?(?:-continuation)?)\.json$/u.test(p);

/** Lock md5sum: đường dẫn có thể có dấu cách, không diễn giải escape hay URL. */
export function parseMd5(text, prefix, allowed) {
  const rows = new Map();
  for (const line of (text ?? '').split(/\r?\n/u)) {
    const match = line.match(/^([a-f0-9]{32}) [ *](.+)$/iu);
    if (!match) continue;
    const p = prefix + match[2];
    if (allowed(p)) rows.set(p, match[1].toLowerCase());
  }
  return rows;
}

/** Chỉ git ls-files; mỗi submodule được hỏi riêng, không mở các game ngoài danh sách. */
export async function gitMetadata(repoRoot, games, allowed, warnings) {
  const result = new Set();
  for (const game of [null, ...games]) {
    const prefix = game ? `games/${game}/` : '';
    const paths = game ? ['media.md5', 'art-src/3d/SOURCES.json', 'scripts/models/presets',
      `public/assets/${game}/models`] : ['scripts/models/presets'];
    try {
      const { stdout } = await exec('git', ['-C', path.join(repoRoot, prefix), 'ls-files', '-z', '--', ...paths],
        { encoding: 'utf8', maxBuffer: 8 * 1024 * 1024, env: { ...process.env, GIT_OPTIONAL_LOCKS: '0' } });
      for (const p of stdout.split('\0').filter(Boolean)) if (allowed(prefix + p)) result.add(prefix + p);
    } catch (error) {
      if (error.code === 'ENOENT' || /not a git repository|cannot change to/u.test(error.stderr ?? '')) {
        warnings.push(`${prefix || '.'}: không có danh sách Git cho --locks-only`);
      } else throw error;
    }
  }
  return result;
}

/** readText/readJson/walk do scan cung cấp, kiểm allowlist và symlink trước mỗi lần đọc. */
export async function loadGameJoins({ game, found, locksOnly, tracked, readText, readJson, walk, allowed }) {
  const prefix = `games/${game}/`;
  const canRead = p => allowed(p) && (!locksOnly || tracked.has(p));
  const sourcePath = `${prefix}art-src/3d/SOURCES.json`;
  const source = canRead(sourcePath) ? await readJson(sourcePath) : {};
  const cleanSources = rows => Object.fromEntries(Object.entries(rows ?? {}).filter(([p, row]) =>
    allowed(`${prefix}art-src/3d/${p}`) && (!row.image || allowed(prefix + (row.image.startsWith('art-src/') ? row.image : 'art-src/' + row.image)))));
  source.files = cleanSources(source.files);
  source.notMadeYet = cleanSources(source.notMadeYet);
  const lockPath = prefix + 'media.md5';
  const lock = parseMd5(canRead(lockPath) ? await readText(lockPath) : '', prefix, allowed);
  const virtual = new Map([...lock].filter(([p]) => catalogFile(p)).map(([p, md5]) => [p, { md5 }]));
  for (const [p, row] of Object.entries(source.files)) {
    const file = `${prefix}art-src/3d/${p}`;
    virtual.set(file, { ...virtual.get(file), md5: row.md5 ?? virtual.get(file)?.md5, bytes: row.bytes });
  }
  for (const row of [...Object.values(source.files), ...Object.values(source.notMadeYet)]) {
    if (row.image) {
      const file = prefix + (row.image.startsWith('art-src/') ? row.image : 'art-src/' + row.image);
      if (!virtual.has(file)) virtual.set(file, {});
    }
  }
  const metadata = new Set();
  if (locksOnly) for (const p of tracked) metadata.add(p);
  else {
    for (const dir of ['scripts/models/presets', `${prefix}scripts/models/presets`]) await walk(dir, metadata);
    for (const p of found) if (p.endsWith('/manifest.json')) metadata.add(p);
  }
  const preset = { models: {} };
  const presetFiles = new Map();
  for (const p of [...metadata].sort(cmp)) {
    if (!canRead(p) || !/^(?:scripts\/models\/presets|games\/[^/]+\/scripts\/models\/presets)\/[^/]+\.json$/u.test(p)) continue;
    if (p.startsWith('games/') && !p.startsWith(prefix)) continue;
    const data = await readJson(p);
    // Preset gốc dùng tên game (campaign3d-models là preset cũ của Space).
    if (!p.startsWith(prefix) && data.game !== game && !path.basename(p).startsWith(game)
      && !(game === 'space-typing' && path.basename(p) === 'campaign3d-models.json')) continue;
    for (const [key, row] of Object.entries(data.models ?? {})) {
      if (!row.source || !allowed(`${prefix}art-src/3d/${row.source}`) || !allowed(`${prefix}art-src/models/${key}.glb`)) continue;
      preset.models[key] = row;
      presetFiles.set(key, p);
    }
  }
  const targets = new Map();
  for (const [p, row] of Object.entries(source.files)) {
    for (const key of row.usedBy ?? []) {
      if (typeof key !== 'string' || !/^[\w-]+\/[\w/-]+$/u.test(key)) continue;
      if (!targets.has(key)) targets.set(key, new Set());
      targets.get(key).add(stemOf(p));
    }
  }
  for (const [key, row] of Object.entries(preset.models)) targets.set(key, new Set([stemOf(row.source)]));
  const target = key => targets.get(key)?.size === 1 ? [...targets.get(key)][0] : key;
  const links = {};
  const runtime = new Map();
  const manifests = [];
  for (const p of [...metadata].sort(cmp)) {
    if (!canRead(p) || !p.startsWith(`${prefix}public/assets/${game}/models/`) || !p.endsWith('/manifest.json')) continue;
    const data = await readJson(p);
    manifests.push(p);
    for (const [key, row] of Object.entries(data.models ?? {})) {
      if (!allowed(`${prefix}art-src/${key}`)) continue;
      for (const [tier, value] of Object.entries(row.tiers ?? {})) {
        if (!['high', 'medium'].includes(tier) || typeof value.url !== 'string') continue;
        const url = value.url.split(/[?#]/u)[0];
        if (!url.startsWith(`/assets/${game}/models/`)) continue;
        const file = prefix + 'public' + url;
        if (!allowed(file)) continue;
        virtual.set(file, { ...virtual.get(file), bytes: value.bytes });
        runtime.set(file, { stem: target(key), game, manifest: p, manifestKey: key, shipped: true, tier,
          importedFrom: row.importedFrom });
        links[url.slice(1).replace(/^assets\//u, 'public/assets/').replace(/\.(?:high|medium)\.glb$/u, '')] = target(key);
      }
    }
  }
  return { game, source, preset, presetFiles, lock, virtual, runtime, links, manifests, target };
}

const hiddenRoles = new Set(['rejected', 'prompt', 'report', 'review', 'draft', 'derivative', 'multiview', 'glb-spare', 'unknown']);
const nonCanonicalRoles = new Set(['rejected', 'review', 'draft', 'unknown']);
const rawPath = p => p.startsWith('games/space-typing/art-src/models/raw/');
const rank = file => file.path.includes('/art-src/3d/') ? 0 : file.path.includes('/art-src/models/') ? 2
  : file.path.includes('/art-src/') ? 1 : file.path.includes('/public/') ? 3 : file.path.includes('/src/assets/') ? 4 : 5;
const unique = rows => [...new Map(rows.map(row => [JSON.stringify(row), row])).values()];
const runtimeAuthority = row => row.card.usedBy.some(usage => usage.shipped);
const compareMaster = (a, b) => Number(hiddenRoles.has(a.file.role)) - Number(hiddenRoles.has(b.file.role)) || rank(a.file) - rank(b.file)
  || Number(runtimeAuthority(b)) - Number(runtimeAuthority(a)) || cmp(a.file.path, b.file.path);

function canonical(card, overrides = {}) {
  const byRole = new Map();
  for (const file of card.files) {
    file.canonical = false;
    if (nonCanonicalRoles.has(file.role) || /\.rejected-[^/]+/u.test(file.path)) continue;
    if (!byRole.has(file.role)) byRole.set(file.role, []);
    byRole.get(file.role).push(file);
  }
  card.canonical = {};
  for (const [role, files] of byRole) {
    files.sort((a, b) => rank(a) - rank(b) || cmp(a.path, b.path));
    const concept = card.canonical.concept;
    const prompt = role === 'prompt' && concept ? files.find(file => file.path === concept.replace(/\.[^/.]+$/u, '.prompt.txt') || file.path === concept + '.prompt.txt') : null;
    const selected = files.find(file => file.path === overrides[role]) ?? prompt ?? files[0];
    selected.canonical = true;
    card.canonical[role] = selected.path;
  }
  card.hiddenFiles = {};
  for (const file of card.files) {
    file.hidden = hiddenRoles.has(file.role);
    if (file.hidden) card.hiddenFiles[file.role] = (card.hiddenFiles[file.role] ?? 0) + 1;
  }
  card.hero = card.canonical.concept ?? card.canonical['tripo-source'] ?? card.canonical.icon ?? null;
  if (card.canonical.prompt) card.provenance.prompt = card.canonical.prompt;
}

/** Nối sổ trước, gom bản sao theo byte, suy trạng thái rồi mới áp tuyển chọn. */
export async function joinCards({ cards, games, privateLock, readText, readBinary, walk, allowed, locksOnly, warnings, handoffRoots = [] }) {
  const byGame = new Map(games.map(row => [row.game, row]));
  for (const card of cards) {
    const data = byGame.get(card.origin);
    card.usedBy = [];
    card.copies = [];
    card.provenance = {};
    for (const file of card.files) {
      const driveMd5 = data.lock.get(file.path);
      file.onDrive = privateLock.has(file.path) ? 'private' : driveMd5 ? driveMd5 === file.md5 ? 'yes' : 'changed' : 'no';
      const runtime = data.runtime.get(file.path);
      if (runtime) {
        const { stem, tier, importedFrom, ...usage } = runtime;
        card.usedBy.push(usage);
      }
    }
    const stem = card.uid.slice(card.origin.length + 1);
    const row = data.source.files[stem + '.glb'];
    const requested = data.source.notMadeYet[stem + '.glb'];
    if (row) {
      if (row.downloadedAs) card.provenance.downloadedAs = row.downloadedAs;
      if (row.image) card.provenance.image = row.image;
      for (const key of row.usedBy ?? []) card.usedBy.push({ game: card.origin, ref: `games/${card.origin}/art-src/3d/SOURCES.json`, manifestKey: key, shipped: false });
    }
    if (requested) {
      card.provenance.notMadeYet = requested;
      card.requested = !card.files.some(file => file.role === 'glb-original' && file.md5);
    }
    for (const [key, preset] of Object.entries(data.preset.models)) if (stemOf(preset.source) === stem) {
      card.usedBy.push({ game: card.origin, ref: data.presetFiles.get(key), manifestKey: key, shipped: false });
    }
    card.usedBy = unique(card.usedBy);
  }

  // Một try/version đã được chọn thành tên chính không còn là bản nháp.
  for (const card of cards) {
    const normal = card.files.filter(file => !hiddenRoles.has(file.role));
    card.files = card.files.filter(file => {
      if (!/\.(?:try|v)\d+(?=\.)/u.test(file.path) || !file.md5) return true;
      const master = normal.find(other => other.md5 === file.md5 && path.posix.dirname(other.path) === path.posix.dirname(file.path));
      if (!master) return true;
      card.copies.push({ ...file, location: 'same-folder', copyOf: card.uid, master: master.path, canonical: false });
      return false;
    });
  }
  const hashes = new Map();
  for (const card of cards) for (const file of card.files) {
    if (!file.md5 || rawPath(file.path)) continue;
    if (!hashes.has(file.md5)) hashes.set(file.md5, []);
    hashes.get(file.md5).push({ card, file });
  }
  for (const matches of hashes.values()) matches.sort(compareMaster);
  for (const card of cards) card.files = card.files.filter(file => {
    if (rawPath(file.path)) {
      const master = hashes.get(file.md5)?.[0];
      if (master) master.card.copies.push({ ...file, location: 'models-raw', copyOf: master.card.uid, master: master.file.path, canonical: false });
      else warnings.push(`${file.path}: models-raw chưa tìm thấy bản gốc; không chọn làm file chính`);
      return false;
    }
    const master = hashes.get(file.md5)?.find(row => row.card !== card);
    if (master && compareMaster(master, { card, file }) < 0) {
      file.copyOf = master.card.uid;
      master.card.copies.push({ ...file, location: 'game', master: master.file.path, canonical: false });
    }
    return true;
  });
  cards = cards.filter(card => card.files.length || card.requested);

  if (!locksOnly) {
    for (const root of handoffRoots) {
      const handoff = new Set();
      await walk(root, handoff);
      for (const p of [...handoff].sort(cmp).filter(p => media.test(p))) {
        try {
          const data = await readBinary(p);
          if (!data) continue;
          const md5 = createHash('md5').update(data).digest('hex');
          const matches = hashes.get(md5);
          const file = { path: p, md5, bytes: data.length, local: true, onDrive: privateLock.has(p) ? 'private' : 'no', canonical: false };
          if (matches?.length) {
            const master = matches[0];
            master.card.copies.push({ ...file, location: 'handoff', copyOf: master.card.uid, master: master.file.path });
            if (/tripo-upload/u.test(p) && !p.endsWith('.glb') && !master.card.files.some(f => f.role === 'glb-original')) master.card.tripoRequested = true;
          } else {
            const stem = p.slice(root.length + 1).replace(/\.[^/.]+$/u, '');
            const card = { uid: 'handoff:' + stem, short: 'handoff:' + path.posix.basename(stem), origin: 'handoff',
              type: p.endsWith('.glb') ? 'model3d' : 'image', status: 'draft', pipeline: p.endsWith('.glb') ? 'glb-original' : 'concept-only',
              files: [{ ...file, role: 'draft' }], usedBy: [], copies: [], provenance: {} };
            cards.push(card);
            hashes.set(md5, [{ card, file: card.files[0] }]);
          }
        } catch (error) {
          if (error.code !== 'ENOENT') throw error;
          warnings.push(`${p}: ENOENT — file handoff đã biến mất`);
        }
      }
    }
  }

  for (const card of cards) {
    const roles = new Set(card.files.map(f => f.role));
    card.rejectedMd5 = [...new Set(card.files.filter(f => f.role === 'rejected').map(f => f.md5).filter(Boolean))].sort(cmp);
    card.pipeline ??= roles.has('runtime-high') || roles.has('runtime-medium') ? 'runtime'
      : roles.has('glb-processed') ? 'processed' : roles.has('glb-original') ? 'glb-original'
        : card.tripoRequested || card.requested || roles.has('tripo-source') ? 'tripo-requested' : 'concept-only';
    card.status ??= card.usedBy.some(usage => usage.shipped) ? 'shipped'
      : card.requested ? 'requested' : [...roles].every(role => hiddenRoles.has(role))
        ? roles.has('rejected') ? 'rejected' : roles.has('review') ? 'review' : 'draft' : 'unscored';
    if (card.files.some(file => file.onDrive === 'private')) { card.private = true; card.status = 'private'; }
    card.copies.sort((a, b) => cmp(a.path, b.path));
    card.files.sort((a, b) => cmp(a.path, b.path));
    canonical(card);
  }

  const curated = new Set();
  await walk('library/curated', curated);
  const byUid = new Map(cards.map(card => [card.uid, card]));
  const byMd5 = new Map();
  for (const card of cards) for (const file of [...card.files, ...card.copies]) {
    if (!file.md5) continue;
    if (!byMd5.has(file.md5)) byMd5.set(file.md5, new Set());
    byMd5.get(file.md5).add(card);
  }
  for (const p of [...curated].filter(p => p.endsWith('.jsonl')).sort(cmp)) {
    let number = 0;
    for (const line of (await readText(p) ?? '').split(/\r?\n/u)) {
      number++;
      if (!line.trim()) continue;
      let row;
      try { row = JSON.parse(line); } catch { warnings.push(`${p}:${number}: dòng tuyển chọn không phải JSON`); continue; }
      if (!row || typeof row.uid !== 'string' || (row.md5s !== undefined && !Array.isArray(row.md5s))) {
        warnings.push(`${p}:${number}: dòng tuyển chọn cần uid và md5s hợp lệ`); continue;
      }
      // Không đưa trường tùy ý từ vùng cấm vào sản phẩm.
      const strings = JSON.stringify(row);
      if (!allowed(`library/curated/${row.uid?.replace(':', '/') ?? ''}`)
        || /(?:immortality-cultivation|tu-tien|TU_TIEN_|monkeytype)/iu.test(strings)) continue;
      let card = byUid.get(row.uid);
      if (!card) {
        const candidates = new Set((row.md5s ?? []).flatMap(md5 => [...(byMd5.get(md5) ?? [])]));
        if (candidates.size === 1) card = [...candidates][0];
        else if (candidates.size > 1) warnings.push(`${p}:${number}: md5 tuyển chọn khớp nhiều thẻ; cần uid hiện tại`);
      }
      if (!card) { warnings.push(`${p}:${number}: dòng tuyển chọn không còn thẻ`); continue; }
      const uid = card.uid;
      const rejectedMd5 = card.rejectedMd5;
      const former = [...new Set([...(card.formerUids ?? []), ...(row.formerUids ?? []), ...(row.uid !== uid ? [row.uid] : [])])].sort(cmp);
      const overrides = { ...card.canonical, ...row.canonical };
      const { files, copies, hiddenFiles, rejectedMd5: rejectedOverride, ...fields } = row;
      Object.assign(card, fields, { uid, rejectedMd5 });
      if (former.length) card.formerUids = former;
      canonical(card, overrides);
      // Quyền riêng tư và danh sách md5 loại là ràng buộc, không phải nhãn tuyển chọn.
      if (card.files.some(file => privateLock.has(file.path))) { card.private = true; card.status = 'private'; }
    }
  }
  return cards;
}
