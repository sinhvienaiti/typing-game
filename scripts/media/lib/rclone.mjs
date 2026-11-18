// The only way the media scripts run rclone: an argument array (no shell), an
// allowlist of subcommands, fixed timeouts, and output with tokens redacted.
// sync, bisync, move, moveto, delete, purge, rmdirs and cleanup can never run.
// The single exception for removal is `dedupe --dedupe-mode skip`, which only
// removes byte-identical duplicates (rclone 1.75 has no "identical" mode name).
import { spawn } from 'node:child_process';

const ALLOWED = new Set(['version', 'listremotes', 'config', 'about', 'mkdir', 'lsjson', 'lsf', 'size', 'copy', 'copyto', 'check', 'dedupe']);
const CONFIG_ALLOWED = new Set(['file', 'dump', 'create', 'reconnect', 'update']);
const FORBIDDEN_FLAGS = [/^--delete/, /^--remove-source-files/, /^--max-delete/, /^--track-renames/, /^--by-hash/, /^--interactive$/, /^-i$/];

export const NETWORK_FLAGS = ['--contimeout', '10s', '--timeout', '60s', '--retries', '3', '--low-level-retries', '5', '--tpslimit', '8'];
export const TRANSFER_FLAGS = ['--transfers', '4', '--checkers', '8', '--stats', '5s', '--stats-one-line', '--stats-log-level', 'NOTICE'];

export class RcloneError extends Error {
  constructor(message, result) {
    super(message);
    this.result = result;
  }
}

export function assertAllowed(args) {
  const [command, sub] = args;
  if (!ALLOWED.has(command)) throw new Error(`rclone ${command ?? ''} không nằm trong danh sách được phép`);
  if (command === 'config' && !CONFIG_ALLOWED.has(sub)) throw new Error(`rclone config ${sub ?? ''} không được phép`);
  for (const arg of args) {
    if (FORBIDDEN_FLAGS.some((pattern) => pattern.test(arg))) throw new Error(`cờ rclone không được phép: ${arg}`);
  }
  if (command === 'dedupe') {
    const modes = [];
    args.forEach((arg, index) => {
      if (arg === '--dedupe-mode') modes.push(args[index + 1]);
      else if (arg.startsWith('--dedupe-mode=')) modes.push(arg.slice('--dedupe-mode='.length));
    });
    const positional = args.slice(1).filter((arg, index, list) => !arg.startsWith('-') && list[index - 1] !== '--dedupe-mode');
    if (modes.length !== 1 || modes[0] !== 'skip' || positional.length !== 1) {
      throw new Error('rclone dedupe chỉ được chạy với --dedupe-mode skip trên một thư mục (chỉ xoá bản trùng giống hệt)');
    }
  }
  return true;
}

const SECRET_PATTERNS = [
  [/("(?:access_token|refresh_token|id_token|client_secret|token)"\s*:\s*")((?:[^"\\]|\\.)*)(")/g, '$1***$3'],
  [/(\\"(?:access_token|refresh_token|id_token)\\"\s*:\s*\\")((?:[^"\\]|\\[^"])*)(\\")/g, '$1***$3'],
  [/^(\s*(?:token|client_secret|refresh_token|access_token)\s*=\s*).*$/gim, '$1***'],
  [/((?:client_secret|token|refresh_token|access_token)=)[^\s&"']+/gi, '$1***'],
  [/\bya29\.[\w.-]+/g, 'ya29.***'],
  [/\b1\/\/[\w-]{10,}/g, '1//***'],
  [/\bGOCSPX-[\w-]+/g, 'GOCSPX-***'],
  [/(Bearer\s+)[\w.~+/=-]+/gi, '$1***'],
];

export function redact(text) {
  let output = String(text);
  for (const [pattern, replacement] of SECRET_PATTERNS) output = output.replace(pattern, replacement);
  return output;
}

function forwardRedacted(stream, write) {
  let buffer = '';
  let timer = null;
  const flush = () => {
    if (buffer) write(redact(buffer));
    buffer = '';
  };
  stream.setEncoding('utf8');
  stream.on('data', (chunk) => {
    buffer += chunk;
    const end = Math.max(buffer.lastIndexOf('\n'), buffer.lastIndexOf('\r'));
    if (end !== -1) {
      write(redact(buffer.slice(0, end + 1)));
      buffer = buffer.slice(end + 1);
    }
    clearTimeout(timer);
    // Interactive questions end without a newline: show them after a short pause.
    if (buffer) timer = setTimeout(flush, 150);
  });
  stream.on('end', () => { clearTimeout(timer); flush(); });
}

/**
 * Runs rclone. capture: collect stdout/stderr (returned, never printed);
 * otherwise both are streamed to the terminal, redacted. interactive: stdin
 * is the terminal (setup only); otherwise stdin is /dev/null and rclone
 * never waits for a config password.
 */
export function runRclone(ctx, args, { capture = true, interactive = false, network = true } = {}) {
  assertAllowed(args);
  const fullArgs = [...args];
  if (network) fullArgs.push(...NETWORK_FLAGS);
  if ((args[0] === 'copy' || args[0] === 'copyto') && !args.includes('--transfers')) fullArgs.push('--transfers', '4');
  if (!interactive) fullArgs.push('--ask-password=false');
  const binary = ctx.env.RCLONE_BIN || 'rclone';
  return new Promise((resolve, reject) => {
    let child;
    try {
      child = spawn(binary, fullArgs, {
        cwd: ctx.root,
        env: ctx.env,
        stdio: [interactive ? 'inherit' : 'ignore', 'pipe', 'pipe'],
      });
    } catch (error) {
      reject(error);
      return;
    }
    let stdout = '';
    let stderr = '';
    if (capture) {
      child.stdout.setEncoding('utf8');
      child.stderr.setEncoding('utf8');
      child.stdout.on('data', (chunk) => { stdout += chunk; });
      child.stderr.on('data', (chunk) => { stderr += chunk; });
    } else {
      forwardRedacted(child.stdout, (text) => ctx.out.write(text));
      forwardRedacted(child.stderr, (text) => ctx.err.write(text));
    }
    child.on('error', (error) => {
      if (error.code === 'ENOENT') reject(new RcloneError('rclone chưa được cài', { code: 127 }));
      else reject(error);
    });
    child.on('close', (code) => resolve({ code, stdout, stderr }));
  });
}

/** Runs rclone and throws a redacted error when it fails. */
export async function rcloneOk(ctx, args, options = {}) {
  const result = await runRclone(ctx, args, options);
  if (result.code !== 0) {
    const detail = redact(`${result.stderr || ''}`.trim().split('\n').slice(-6).join('\n'));
    throw new RcloneError(`rclone ${args[0]} lỗi (mã ${result.code})${detail ? `:\n${detail}` : ''}`, result);
  }
  return result;
}

export async function rcloneVersion(ctx) {
  try {
    const result = await runRclone(ctx, ['version'], { network: false });
    const match = /v(\d+)\.(\d+)\.(\d+)/.exec(result.stdout);
    return match ? match.slice(1, 4).map(Number) : null;
  } catch (error) {
    if (error instanceof RcloneError) return null;
    throw error;
  }
}

export function versionAtLeast(version, minimum) {
  const wanted = minimum.split('.').map(Number);
  for (let index = 0; index < 3; index += 1) {
    if ((version[index] ?? 0) !== (wanted[index] ?? 0)) return (version[index] ?? 0) > (wanted[index] ?? 0);
  }
  return true;
}

export function installHint(platform = process.platform) {
  if (platform === 'darwin') return 'Cài rclone: brew install rclone';
  return 'Cài rclone trong WSL Ubuntu: sudo -v ; curl https://rclone.org/install.sh | sudo bash (không dùng apt: bản quá cũ)';
}

/** Parsed `rclone config dump` for one remote. Never printed: it holds the token. */
export async function remoteConfig(ctx, remote) {
  const result = await rcloneOk(ctx, ['config', 'dump'], { network: false });
  let data;
  try { data = JSON.parse(result.stdout); }
  catch { throw new Error('không đọc được cấu hình rclone (rclone config dump)'); }
  return data?.[remote] ?? null;
}

export async function configFilePath(ctx) {
  const result = await rcloneOk(ctx, ['config', 'file'], { network: false });
  const lines = result.stdout.trim().split('\n').map((line) => line.trim()).filter(Boolean);
  return lines.at(-1);
}

/** Parses the `--combined -` report of rclone check. */
export function parseCombined(text) {
  const report = { match: [], missingOnRemote: [], differ: [], error: [], extraOnRemote: [] };
  for (const line of text.split('\n')) {
    if (line.length < 3 || line[1] !== ' ') continue;
    const file = line.slice(2);
    if (line[0] === '=') report.match.push(file);
    else if (line[0] === '+') report.missingOnRemote.push(file);
    else if (line[0] === '*') report.differ.push(file);
    else if (line[0] === '!') report.error.push(file);
    else if (line[0] === '-') report.extraOnRemote.push(file);
  }
  return report;
}
