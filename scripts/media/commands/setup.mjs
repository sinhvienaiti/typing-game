// pnpm media:setup: one browser sign-in, then pin the remote to its own Drive
// folder. Run it in your own terminal, never through an AI agent: the browser
// login and the client secret must not end up in a chat transcript.
import { appendFileSync, chmodSync, existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { configFilePath, rcloneOk, remoteConfig, runRclone } from '../lib/rclone.mjs';
import { driveAbout, ensureRclone, tempDir } from '../lib/remote.mjs';
import { fmtBytes, MediaError, readHidden } from '../lib/ui.mjs';

export const DRIVE_README = `typing-game-media: kho media của dự án typing-game.

Không sửa tay. Dùng pnpm media:push / media:pull từ thư mục typing-game.
Không chia sẻ thư mục private/.

- repo/: ảnh, mô hình 3D, media chạy game. Đường dẫn giống hệt trong repo.
- private/: nhạc và âm thanh chỉ dùng riêng (có bản quyền). Không chia sẻ.
- _replaced/<thời điểm>/: bản cũ bị thay khi đẩy. Không tự xoá; dọn tay khi cần.
- _locks/<thời điểm>/: bản sao danh sách md5 sau mỗi lần đẩy.

Hướng dẫn: docs/MEDIA_STORAGE.md trong repo typing-game.
`;

/** The [remote] section for an own OAuth client, written by this script so the secret never goes on a command line. */
export function remoteSection(remote, clientId, clientSecret) {
  for (const value of [remote, clientId, clientSecret]) {
    if (!value || /[\r\n\[\]]/.test(value)) throw new MediaError('client id / secret không hợp lệ');
  }
  return `\n[${remote}]\ntype = drive\nscope = drive\nclient_id = ${clientId}\nclient_secret = ${clientSecret}\n`;
}

/** Arguments for the built-in client: rclone's own OAuth app, one browser sign-in. */
export function createArgs(remote) {
  return ['config', 'create', remote, 'drive', 'scope=drive', '--no-output'];
}

async function listRemotes(ctx) {
  const result = await rcloneOk(ctx, ['listremotes'], { network: false });
  return result.stdout.split('\n').map((line) => line.trim().replace(/:$/, '')).filter(Boolean);
}

function assertNotEncrypted(file) {
  if (existsSync(file) && readFileSync(file, 'utf8').startsWith('# Encrypted rclone configuration File')) {
    throw new MediaError('rclone.conf đang được mã hoá: các lệnh media chạy không hỏi mật khẩu nên sẽ treo. Bỏ mã hoá (rclone config encryption remove) hoặc dùng một file cấu hình riêng (RCLONE_CONFIG).');
  }
}

async function folderId(ctx, remote, name) {
  const result = await rcloneOk(ctx, ['lsjson', `${remote}:`, '--dirs-only', '--max-depth', '1']);
  const matches = JSON.parse(result.stdout || '[]').filter((item) => item.IsDir && item.Name === name);
  if (matches.length > 1) {
    throw new MediaError(`Drive có ${matches.length} thư mục tên ${name} ở My Drive. Đổi tên hoặc gộp tay cho còn một, rồi chạy lại.`);
  }
  return matches[0]?.ID ?? null;
}

export async function setup(ctx, options) {
  const { remote, driveFolder } = ctx.config;
  const version = await ensureRclone(ctx);
  ctx.out.write(`rclone ${version.join('.')}\n`);
  const confFile = await configFilePath(ctx);
  assertNotEncrypted(confFile);
  const remotes = await listRemotes(ctx);

  if (!remotes.includes(remote)) {
    if (options['client-id']) {
      const secret = ctx.env.TGMEDIA_CLIENT_SECRET || await readHidden(ctx, 'Client secret (không hiện khi gõ): ');
      if (!secret) throw new MediaError('Cần client secret: gõ khi được hỏi, hoặc đặt biến môi trường TGMEDIA_CLIENT_SECRET.');
      mkdirSync(path.dirname(confFile), { recursive: true, mode: 0o700 });
      if (existsSync(confFile)) {
        const current = readFileSync(confFile, 'utf8');
        if (current && !current.endsWith('\n')) appendFileSync(confFile, '\n');
      }
      appendFileSync(confFile, remoteSection(remote, options['client-id'], secret), { mode: 0o600 });
      chmodSync(confFile, 0o600);
      ctx.out.write('Đã lưu client vào rclone.conf. Trình duyệt sẽ mở: đăng nhập Google (tài khoản @gmail.com cá nhân) và bấm Allow.\n');
      const result = await runRclone(ctx, ['config', 'update', remote, 'scope=drive', '--no-output'], { capture: false, interactive: true, network: false });
      if (result.code !== 0) throw new MediaError(`Đăng nhập chưa xong (rclone mã ${result.code}). Chạy: pnpm media:setup --reconnect`);
    } else {
      ctx.out.write('Trình duyệt sẽ mở: đăng nhập Google (tài khoản @gmail.com cá nhân, không dùng tài khoản công ty) và bấm Allow.\n'
        + 'Nếu trình duyệt không mở (WSL): chép link http://127.0.0.1:53682/... rclone in ra sang Chrome trên Windows.\n');
      const result = await runRclone(ctx, createArgs(remote), { capture: false, interactive: true, network: false });
      if (result.code !== 0) throw new MediaError(`Kết nối chưa xong (rclone mã ${result.code}). Chạy lại pnpm media:setup.`);
    }
  } else if (options['client-id']) {
    throw new MediaError(`Remote "${remote}" đã có. Muốn đổi sang client riêng: rclone config delete ${remote} (tự chạy), rồi pnpm media:setup --client-id <id>.`);
  } else if (options.reconnect) {
    ctx.out.write('Đăng nhập lại Google trong trình duyệt…\n');
    const result = await runRclone(ctx, ['config', 'reconnect', `${remote}:`], { capture: false, interactive: true, network: false });
    if (result.code !== 0) throw new MediaError(`Đăng nhập lại chưa xong (rclone mã ${result.code}).`);
  }

  let config = await remoteConfig(ctx, remote);
  if (!config) throw new MediaError(`Chưa tạo được remote "${remote}".`);
  if (config.type !== 'drive') throw new MediaError(`Remote "${remote}" có kiểu ${config.type}, không phải Google Drive. Đặt tên khác cho remote đó rồi chạy lại.`);
  if (!config.root_folder_id) {
    let id = await folderId(ctx, remote, driveFolder);
    if (!id) {
      await rcloneOk(ctx, ['mkdir', `${remote}:${driveFolder}`]);
      id = await folderId(ctx, remote, driveFolder);
    }
    if (!id) throw new MediaError(`Không tìm thấy thư mục ${driveFolder} vừa tạo trên Drive. Chạy lại pnpm media:setup.`);
    await rcloneOk(ctx, ['config', 'update', remote, `root_folder_id=${id}`, 'config_refresh_token=false', '--no-output'], { network: false });
    config = await remoteConfig(ctx, remote);
    if (config?.root_folder_id !== id) throw new MediaError('Không lưu được root_folder_id vào rclone.conf.');
    ctx.out.write(`Đã khoá rclone vào thư mục My Drive/${driveFolder}: từ giờ rclone chỉ thấy thư mục này.\n`);
  } else {
    ctx.out.write(`Remote "${remote}" đã khoá vào một thư mục riêng (root_folder_id).\n`);
  }

  const dir = tempDir('media-readme-');
  try {
    const readme = path.join(dir, 'README.txt');
    writeFileSync(readme, DRIVE_README);
    await rcloneOk(ctx, ['copyto', readme, `${remote}:README.txt`]);
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }

  const about = await driveAbout(ctx, { remote });
  if (about?.free !== undefined) {
    ctx.out.write(`Drive còn trống ${fmtBytes(about.free)}${about.total ? ` / ${fmtBytes(about.total)}` : ''}.\n`);
    if (about.free < 6e9) ctx.out.write('! Lần đẩy đầu cần khoảng 3,7 GB cộng 2 GB dự phòng. Drive đầy thì Gmail ngừng nhận thư.\n');
  }
  ctx.out.write('\n✓ Xong. Tiếp theo:\n  pnpm media:status\n  pnpm media:push --dry-run\n  pnpm media:push\n');
  return 0;
}
