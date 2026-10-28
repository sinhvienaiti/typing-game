import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { mkdirSync, realpathSync, rmSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

export const REPO_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
export const CACHE_DIR = path.join(REPO_ROOT, 'tools/map-factory/.cache');
export const FIXTURE_DIR = path.join(REPO_ROOT, 'tools/map-factory/test/fixtures/gameplay');

export function gamesDir() {
  if (process.env.MAP_FACTORY_GAMES_DIR) return process.env.MAP_FACTORY_GAMES_DIR;
  const common = execFileSync('git', ['-C', REPO_ROOT, 'rev-parse', '--path-format=absolute', '--git-common-dir'], { encoding: 'utf8' }).trim();
  return path.join(path.dirname(common), 'games');
}

export function gameRepo(id) {
  const repo = path.join(gamesDir(), id);
  const root = execFileSync('git', ['-C', repo, 'rev-parse', '--show-toplevel'], { encoding: 'utf8' }).trim();
  if (root !== realpathSync(repo)) {
    throw new Error(`${repo} is not a separate game repository (resolved Git root: ${root})`);
  }
  return repo;
}

export function resolveCommit(repo, rev) {
  const sha = execFileSync('git', ['-C', repo, 'rev-parse', '--verify', '--end-of-options', `${rev}^{commit}`], { encoding: 'utf8' }).trim();
  if (!/^[0-9a-f]{40}$/.test(sha)) throw new Error(`Invalid commit: ${sha}`);
  return sha;
}

export function extractTree(game, repo, sha) {
  if (!/^[a-z0-9-]+$/.test(game) || !/^[0-9a-f]{40}$/.test(sha)) {
    throw new Error('Invalid extraction game or commit');
  }
  const dir = path.resolve(CACHE_DIR, game, sha);
  const relative = path.relative(CACHE_DIR, dir);
  if (!relative || relative.startsWith('..') || path.isAbsolute(relative)) {
    throw new Error(`Extraction path is outside CACHE_DIR: ${dir}`);
  }
  rmSync(dir, { recursive: true, force: true });
  mkdirSync(dir, { recursive: true });
  const archive = execFileSync('git', ['-C', repo, 'archive', '--format=tar', sha, '--', 'package.json', 'src/content', 'src/sim'], { maxBuffer: 64 * 1024 * 1024 });
  execFileSync('tar', ['-x', '-C', dir], { input: archive });
  return dir;
}

export function canonicalJson(value) {
  if (typeof value === 'number') {
    if (!Number.isSafeInteger(value)) throw new TypeError(`Expected a safe integer: ${value}`);
    return String(value);
  }
  if (value === null || ['string', 'boolean'].includes(typeof value)) return JSON.stringify(value);
  if (Array.isArray(value)) return `[${Array.from(value, canonicalJson).join(',')}]`;
  if (typeof value === 'object') {
    return `{${Object.keys(value).sort().map(key => `${JSON.stringify(key)}:${canonicalJson(value[key])}`).join(',')}}`;
  }
  throw new TypeError(`Unsupported JSON value: ${typeof value}`);
}

export function gameplayHash(extract) {
  const { commit, hash, ...gameplay } = extract;
  return createHash('sha256').update(canonicalJson(gameplay), 'utf8').digest('hex');
}

export function fixtureText(extract) {
  return `{\n${Object.keys(extract).sort().map(key => `${JSON.stringify(key)}:${canonicalJson(extract[key])}`).join(',\n')}\n}\n`;
}

export function exactCm(m, what) {
  const c = Math.round(m * 100);
  if (!Number.isFinite(m) || Math.abs(m * 100 - c) > 1e-6) {
    throw new Error(`${what} is not an exact number of centimeters: ${m}`);
  }
  return c + 0;
}

export function gitStatus(repo) {
  return execFileSync('git', ['--no-optional-locks', '-C', repo, 'status', '--porcelain=v1'], { encoding: 'utf8' });
}

async function main(args) {
  const [game, ...rest] = args;
  const validGames = ['typing-defense', 'dragon-hold'];
  const write = rest.includes('--write');
  const revisions = rest.filter(arg => arg !== '--write');
  if ((!validGames.includes(game) && game !== 'all') || revisions.length > 1
      || rest.filter(arg => arg === '--write').length > 1
      || revisions.some(arg => arg.startsWith('--')) || (game === 'all' && revisions.length)) {
    console.error('Usage: node tools/map-factory/adapters/extract.mjs <typing-defense|dragon-hold|all> [rev] [--write]');
    process.exitCode = 2;
    return;
  }
  const selected = game === 'all' ? validGames : [game];
  for (const id of selected) {
    const adapter = await import(`./${id}.mjs`);
    const rev = revisions[0] ?? adapter.PIN;
    if (write && rev !== adapter.PIN) {
      console.error('--write requires the pinned commit');
      process.exitCode = 2;
      return;
    }
    const { extract } = await adapter.extract(rev);
    if (write) {
      mkdirSync(FIXTURE_DIR, { recursive: true });
      const file = path.join(FIXTURE_DIR, `${id}.${extract.map}.json`);
      writeFileSync(file, fixtureText(extract));
      console.log(`${file} ${extract.hash}`);
    } else {
      process.stdout.write(fixtureText(extract));
    }
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  // Finish module evaluation before adapters import these shared functions.
  main(process.argv.slice(2)).catch(error => {
    console.error(error);
    process.exitCode = 1;
  });
}
