import * as fs from 'node:fs/promises';
import { REPO_ROOT, loadCatalog, parseArgs, visibleFiles, cardName, qualityLabel, driveLabel, number, table, main } from './find.mjs';

export function resolveCard(catalog, uid) {
  const exact = catalog.cards.find(card => card.uid === uid);
  if (exact) return exact;
  const colon = uid.indexOf(':');
  const matches = colon < 0 ? [] : catalog.cards.filter(card => card.uid.split(':')[0] === uid.slice(0, colon) &&
    card.uid.split(':').at(-1).split('/').at(-1) === uid.slice(colon + 1));
  if (matches.length === 1) return matches[0];
  if (matches.length > 1) throw new Error(`Mã ngắn không duy nhất: ${uid}\n${matches.map(c => c.uid).join('\n')}`);
  throw new Error(`Không tìm thấy thẻ: ${uid}`);
}

// Chỉ in lệnh, không chạy copy. Quote từng đối số để dùng được cả mã có dấu cách.
const quote = value => /^[A-Za-z0-9_./:-]+$/u.test(value) ? value : `'${value.replace(/'/gu, "'\"'\"'")}'`;
export const copyCommand = card => `pnpm lib:copy ${quote(card.uid)} --to <game>`;

export async function runShow(argv = [], { repoRoot = REPO_ROOT, io = fs, stdout = process.stdout } = {}) {
  const { options, positional } = parseArgs(argv, [], ['all', 'json', 'help']);
  if (options.help) { stdout.write('Cách dùng: pnpm lib:show <uid|mã ngắn> [--all] [--json]\n'); return 0; }
  if (positional.length !== 1) throw new Error('Cần đúng một mã thẻ: pnpm lib:show <uid|mã ngắn>');
  const card = resolveCard(await loadCatalog({ repoRoot, io }), positional[0]);
  const files = visibleFiles(card, options.all);
  const view = { ...card, files };
  if (options.json) stdout.write(JSON.stringify(view, null, 2) + '\n');
  else {
    stdout.write(`${cardName(card)} · ${card.uid}\n${qualityLabel(card)}\n`);
    // Giữ mọi trường metadata của thẻ, kể cả các trường được bổ sung bởi phiếu sau.
    const { files: ignored, ...metadata } = card;
    stdout.write(JSON.stringify(metadata, null, 2) + '\n\n');
    stdout.write(table(['vai trò', 'chính', 'trên máy', 'byte', 'Drive', 'đường dẫn'], files.slice().sort((a, b) =>
      a.role.localeCompare(b.role) || a.path.localeCompare(b.path)).map(f => [
      f.role, f.canonical ? 'có' : '—', f.local === false ? 'chưa' : f.local === true ? 'có' : '—', number(f.bytes), driveLabel(f.onDrive), f.path,
    ])) + '\n');
    const hidden = card.files.length - files.length;
    if (hidden) stdout.write(`Ẩn ${hidden} file chi tiết; dùng --all để xem.\n`);
    stdout.write(`\nLệnh chép (thay <game> bằng game đích):\n${copyCommand(card)}\n`);
    if (card.licence?.private || card.licence?.notForRelease || card.status === 'private') {
      stdout.write('Thẻ riêng tư hoặc không được phát hành; lib:copy sẽ từ chối.\n');
    }
  }
  return 0;
}
main(import.meta.url, runShow);
