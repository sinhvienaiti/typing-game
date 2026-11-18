import * as fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { randomUUID } from 'node:crypto';
import { spawn } from 'node:child_process';
import { REPO_ROOT, loadCatalog, parseArgs, safeInfo, visibleFiles, main } from './find.mjs';
import { resolveCard } from './show.mjs';

export function runProcess(command, args) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, args, { stdio: ['ignore', 'ignore', 'pipe'], shell: false });
    let detail = '';
    child.stderr.on('data', chunk => { detail = (detail + chunk).slice(-4000); });
    child.on('error', error => reject(new Error(`Không chạy được ${command}: ${error.message}`)));
    child.on('close', (code, signal) => code === 0 ? resolve() : reject(new Error(`${command} thoát ${code ?? signal}: ${detail.trim()}`)));
  });
}

export async function runPlay(argv = [], { repoRoot = REPO_ROOT, io = fs, stdout = process.stdout,
  stderr = process.stderr, exec = runProcess, home = os.homedir() } = {}) {
  const { options, positional } = parseArgs(argv, ['variant'], ['help']);
  if (options.help) { stdout.write('Cách dùng: pnpm lib:play <uid|mã ngắn> [--variant N] (N bắt đầu từ 1)\n'); return 0; }
  if (positional.length !== 1) throw new Error('Cần đúng một mã thẻ âm thanh');
  const variant = Number(options.variant ?? 1);
  if (!Number.isInteger(variant) || variant < 1) throw new Error('--variant phải là số nguyên từ 1');
  const card = resolveCard(await loadCatalog({ repoRoot, io }), positional[0]);
  if (!['audio', 'music'].includes(card.type)) throw new Error(`Thẻ không phải âm thanh: ${card.uid}`);
  const files = visibleFiles(card).filter(f => /\.(?:ogg|opus|wav|mp3|m4a|aac|flac|aif|aiff)$/iu.test(f.path));
  files.sort((a, b) => String(a.variant ?? a.path).localeCompare(String(b.variant ?? b.path), 'en', { numeric: true }));
  const file = files[variant - 1];
  if (!file) throw new Error(`Không có biến thể ${variant}; thẻ có ${files.length} biến thể`);
  if (file.local === false) throw new Error(`File chưa có trên máy: ${file.path}`);
  let source;
  if (file.path.startsWith('~/AudioLab/')) {
    await safeInfo(home, file.path.slice(2), io);
    source = path.join(home, file.path.slice(2));
  } else {
    await safeInfo(repoRoot, file.path, io);
    source = path.join(repoRoot, file.path);
  }
  if (!(await io.stat(source)).isFile()) throw new Error(`Không phải file âm thanh: ${file.path}`);
  stdout.write(`Phát ${card.uid} · biến thể ${variant}: ${file.path}\n`);
  try { await exec('afplay', [source]); return 0; }
  catch (error) { stderr.write(`afplay chưa phát được; giải mã WAV bằng ffmpeg. ${error.message}\n`); }

  // Không xóa/đổi tên file nguồn; tên ngẫu nhiên tránh đè cache của phiên khác.
  const rel = 'library/.cache/play';
  await safeInfo(repoRoot, rel, io);
  const cache = path.join(repoRoot, rel);
  await io.mkdir(cache, { recursive: true });
  const wav = path.join(cache, `${randomUUID()}.wav`);
  await exec('ffmpeg', ['-nostdin', '-hide_banner', '-loglevel', 'error', '-i', source, '-vn', '-c:a', 'pcm_s16le', '-n', wav]);
  await exec('afplay', [wav]);
  return 0;
}
main(import.meta.url, runPlay);
