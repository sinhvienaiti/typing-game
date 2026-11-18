#!/usr/bin/env node
// Read-only protocol requests: no conversation, model request, or config mutation.
// Codex may still write its normal startup logs/cache outside this repository.
import { spawn } from 'node:child_process';
import { statSync } from 'node:fs';
import { createInterface } from 'node:readline';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(fileURLToPath(new URL('..', import.meta.url)));
const args = process.argv.slice(2);
if (args.includes('--help')) {
  console.log('Usage: node scripts/inspect-codex-skills.mjs [cwd ...] [--plugin NAME --marketplace-path FILE]\nRead Codex app-server skills/list; print names, enabled state and paths only.\nFor plugin/read, FILE is the local .agents/plugins/marketplace.json manifest.');
  process.exit(0);
}
const cwds = [];
let pluginName;
let marketplacePath;
for (let index = 0; index < args.length; index += 1) {
  const arg = args[index];
  if ((arg === '--plugin' || arg === '--marketplace-path') && args[index + 1] && !args[index + 1].startsWith('-')) {
    const value = args[++index];
    if (arg === '--plugin') pluginName = value;
    else marketplacePath = resolve(value);
  } else if (arg.startsWith('-')) {
    console.error('Unknown or incomplete option; use --help.');
    process.exit(1);
  } else cwds.push(resolve(arg));
}
if (Boolean(pluginName) !== Boolean(marketplacePath)) {
  console.error('Use --plugin NAME and --marketplace-path FILE together to inspect a local plugin.');
  process.exit(1);
}
if (marketplacePath) {
  try {
    if (!statSync(marketplacePath).isFile()) throw new Error();
  } catch {
    console.error('--marketplace-path must point to an existing marketplace.json file.');
    process.exit(1);
  }
}
if (!cwds.length) cwds.push(root);
const server = spawn('codex', ['app-server', '--stdio'], { cwd: root, stdio: ['pipe', 'pipe', 'pipe'] });
const pending = new Map();
let nextId = 0;
let stoppedError;
let killTimer;
// Drain diagnostics without printing potentially sensitive configuration values.
server.stderr.resume();
const lines = createInterface({ input: server.stdout });
function rejectPending(error) {
  stoppedError = error;
  for (const { reject } of pending.values()) reject(error);
  pending.clear();
}
server.on('error', error => rejectPending(new Error(`Cannot start codex: ${error.code ?? 'spawn error'}`)));
server.stdin.on('error', () => rejectPending(new Error('Codex app-server input closed.')));
server.on('exit', code => {
  clearTimeout(killTimer);
  rejectPending(new Error(`Codex app-server exited (${code}).`));
});
lines.on('line', line => {
  let message;
  try { message = JSON.parse(line); } catch { return; }
  const request = pending.get(message.id);
  if (!request) return;
  pending.delete(message.id);
  if (message.error) request.reject(new Error(`Codex ${request.method} failed (${message.error.code}); check CLI compatibility.`));
  else request.resolve(message.result);
});
function request(method, params) {
  return new Promise((resolvePromise, reject) => {
    if (stoppedError) { reject(stoppedError); return; }
    const id = ++nextId;
    pending.set(id, { resolve: resolvePromise, reject, method });
    server.stdin.write(`${JSON.stringify({ id, method, params })}\n`);
  });
}
const timeout = setTimeout(() => {
  rejectPending(new Error('Codex discovery timed out after 25 seconds.'));
  server.kill();
}, 25_000);
try {
  await request('initialize', {
    clientInfo: { name: 'typing-game-skill-inspector', version: '1.0.0' },
    ...(pluginName ? { capabilities: { experimentalApi: true } } : {}),
  });
  server.stdin.write(`${JSON.stringify({ method: 'initialized' })}\n`);
  const result = await request('skills/list', { cwds, forceReload: true });
  if (!Array.isArray(result?.data)) throw new Error('Unexpected skills/list response.');
  const data = result.data.map(entry => ({
    cwd: entry.cwd,
    // A parser error can embed file content; expose paths without raw diagnostics.
    errors: entry.errors.map(error => ({ path: error.path })),
    skills: entry.skills.map(({ name, scope, enabled, path, pluginId }) => ({ name, scope, enabled, path, ...(pluginId ? { pluginId } : {}) }))
      .sort((a, b) => a.name.localeCompare(b.name)),
  }));
  let plugin;
  if (pluginName) {
    const detail = (await request('plugin/read', { pluginName, marketplacePath }))?.plugin;
    if (!detail?.summary || !Array.isArray(detail.skills)) throw new Error('Unexpected plugin/read response.');
    const { name, id, installed, enabled, availability, disabledReason, localVersion, version } = detail.summary;
    plugin = {
      name, id, installed, enabled, availability, disabledReason, localVersion, version,
      marketplaceName: detail.marketplaceName,
      skills: detail.skills.map(({ name, enabled, path }) => ({ name, enabled, path })).sort((a, b) => a.name.localeCompare(b.name)),
    };
  }
  console.log(JSON.stringify({ data, ...(plugin ? { plugin } : {}) }, null, 2));
  if (data.some(entry => entry.errors.length)) process.exitCode = 1;
} catch (error) {
  console.error(error.message);
  process.exitCode = 1;
} finally {
  clearTimeout(timeout);
  lines.close();
  server.stdin.end();
  server.kill();
  // Bound teardown even if a future app-server ignores SIGTERM.
  killTimer = setTimeout(() => server.kill('SIGKILL'), 2_000);
  killTimer.unref();
}
