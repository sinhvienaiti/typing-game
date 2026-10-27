// Argument parsing for scripts/media/media.mjs. Fails closed: unknown flags,
// missing values and extra positionals are errors, so a typo can never turn
// `--dry-run` into a real push. pnpm 11 passes a literal `--` through
// (`pnpm media:push -- --dry-run` -> ['push', '--', '--dry-run']); one `--`
// right after the command is dropped, anywhere else it is an error.

export const SET_NAMES = ['originals', 'runtime', 'private'];

const HELP = { help: 'boolean' };

export const COMMANDS = {
  setup: { ...HELP, 'client-id': 'string', reconnect: 'boolean' },
  status: { ...HELP, only: 'sets', 'find-unknown': 'boolean' },
  push: { ...HELP, 'dry-run': 'boolean', only: 'sets', yes: 'boolean', forget: 'list', readd: 'list', 'new-only': 'boolean' },
  pull: { ...HELP, only: 'sets', to: 'string', 'update-stale': 'boolean' },
  check: { ...HELP, only: 'sets', remote: 'boolean', 'fix-duplicates': 'boolean' },
};

export class UsageError extends Error {}

function parseSets(value) {
  const names = value.split(',').map((name) => name.trim()).filter(Boolean);
  if (!names.length) throw new UsageError('--only cần tên nhóm: originals, runtime hoặc private');
  for (const name of names) {
    if (!SET_NAMES.includes(name)) throw new UsageError(`--only: nhóm không có: ${name} (chỉ có ${SET_NAMES.join(', ')})`);
  }
  return [...new Set(names)];
}

export function parseArgs(argv) {
  const args = [...argv];
  const command = args.shift();
  if (command === undefined || command === 'help' || command === '--help' || command === '-h') {
    return { command: 'help', options: {} };
  }
  const spec = COMMANDS[command];
  if (!spec) throw new UsageError(`Lệnh không có: ${command}. Dùng: ${Object.keys(COMMANDS).join(', ')}`);
  if (args[0] === '--') args.shift();

  const options = {};
  for (let index = 0; index < args.length; index += 1) {
    const arg = args[index];
    if (arg === '-h') { options.help = true; continue; }
    if (!arg.startsWith('--') || arg === '--') {
      throw new UsageError(`Tham số thừa: ${arg}`);
    }
    const eq = arg.indexOf('=');
    const name = eq === -1 ? arg.slice(2) : arg.slice(2, eq);
    const type = Object.hasOwn(spec, name) ? spec[name] : undefined;
    if (!type) throw new UsageError(`Cờ không có cho lệnh ${command}: --${name}`);
    if (type === 'boolean') {
      if (eq !== -1) throw new UsageError(`--${name} không nhận giá trị`);
      options[name] = true;
      continue;
    }
    let value;
    if (eq !== -1) value = arg.slice(eq + 1);
    else {
      value = args[index + 1];
      if (value === undefined || value.startsWith('--')) throw new UsageError(`--${name} cần một giá trị`);
      index += 1;
    }
    if (value === '') throw new UsageError(`--${name} cần một giá trị`);
    if (type === 'string') {
      if (Object.hasOwn(options, name)) throw new UsageError(`--${name} chỉ được dùng một lần`);
      options[name] = value;
    } else if (type === 'list') {
      (options[name] ??= []).push(value);
    } else if (type === 'sets') {
      options[name] = [...new Set([...(options[name] ?? []), ...parseSets(value)])];
    }
  }
  return { command, options };
}

export const USAGE = `Kho media trên Google Drive (chạy trong thư mục typing-game)

  pnpm media:setup [--client-id <id>] [--reconnect]
      Kết nối Google Drive (một lần mỗi máy). Tự chạy trong terminal của bạn, không qua AI.
  pnpm media:status [--only <nhóm>] [--find-unknown]
      Không cần mạng: mỗi nhóm có bao nhiêu file Thiếu / Mới / Khác.
  pnpm media:push [--dry-run] [--only <nhóm>] [--yes] [--new-only] [--forget <đường dẫn>] [--readd <đường dẫn>]
      Đẩy file mới và file đã đổi lên Drive, so md5, rồi cập nhật danh sách md5.
      --yes chỉ bỏ câu hỏi thay file gốc. File thiếu và đổi tên luôn cần trả lời y
      (hoặc --forget <đường dẫn cũ>). --readd thêm lại file đã bị bỏ khỏi danh sách.
  pnpm media:pull [--only <nhóm>] [--to <thư mục>] [--update-stale]
      Tải file còn thiếu về đúng chỗ, rồi so md5. Không ghi đè hay xoá file nào của bạn.
  pnpm media:check [--only <nhóm>] [--remote] [--fix-duplicates]
      Kiểm tra file trên máy (và trên Drive với --remote) khớp danh sách md5.

Nhóm: originals (art-src), runtime (media chạy game chưa vào Git), private (nhạc, âm thanh riêng).
originals và runtime tính riêng cho từng game trong media/media.config.json (games[]); game chưa có thư mục thì bỏ qua.
Viết cờ không có "--" đứng trước: pnpm media:push --dry-run
Hướng dẫn: docs/MEDIA_STORAGE.md`;
