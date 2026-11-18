#!/usr/bin/env node
// Canonical .agents/skills -> Claude copies. Never deletes files or resolves conflicts.
import { constants, copyFileSync, existsSync, lstatSync, mkdirSync, readFileSync, readdirSync, renameSync, writeFileSync, chmodSync } from 'node:fs';
import { createHash, randomUUID } from 'node:crypto';
import path from 'node:path';
import { repositoryRoot, validateSkills } from './validate-agent-skills.mjs';

function main() {
  let explicitRoot;
  let dryRun = false;
  let check = false;
  for (let index = 2; index < process.argv.length; index += 1) {
    const arg = process.argv[index];
    if (arg === '--root' && process.argv[index + 1]) explicitRoot = process.argv[++index];
    else if (arg === '--dry-run') dryRun = true;
    else if (arg === '--check') { check = true; dryRun = true; }
    else if (arg === '--help') {
      console.log('Usage: bash scripts/sync-agent-skills.sh [--dry-run|--check] [--root PATH]\nCopies .agents/skills into .claude/skills after a complete checksum conflict check.\n--dry-run prints the plan without writing; --check also exits 1 when sync is needed.\nNo force/prune/deletion: reconcile removals or manual divergence explicitly first.');
      return;
    } else throw new Error(`unknown or incomplete option: ${arg}`);
  }
  const root = repositoryRoot(explicitRoot);
  const sourceRoot = path.join(root, '.agents', 'skills');
  const targetRoot = path.join(root, '.claude', 'skills');
  const manifestPath = path.join(root, '.claude', '.agent-skills-sync.json');
  const conflicts = [];
  const operations = [];
  const sourceSnapshots = new Map();
  const targetSnapshots = new Map();
  const nextSkills = Object.create(null);
  const safeName = (value) => /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(value);
  const safeFile = (value) => value && !value.includes('\\') && !path.posix.isAbsolute(value)
    && value.split('/').every((part) => part && part !== '.' && part !== '..');
  const hash = (filename) => createHash('sha256').update(readFileSync(filename)).digest('hex');
  const same = (left, right) => JSON.stringify(left) === JSON.stringify(right);
  const stat = (filename) => {
    try { return lstatSync(filename); }
    catch (error) { if (error.code === 'ENOENT') return null; throw error; }
  };
  const regularDirectory = (filename) => {
    const entry = stat(filename);
    if (entry && (!entry.isDirectory() || entry.isSymbolicLink())) {
      throw new Error(`${path.relative(root, filename)} must be a regular directory`);
    }
  };
  // Reject symlink ancestors before any reads/copies can escape the intended roots.
  for (const directory of [path.join(root, '.agents'), sourceRoot, path.join(root, '.claude'), targetRoot]) regularDirectory(directory);
  const validation = validateSkills(root);
  if (validation.errors.length) throw new Error(`canonical skills failed validation:\n${validation.errors.join('\n')}`);
  let previous = { version: 1, source: '.agents/skills', skills: {} };
  if (stat(manifestPath)) {
    if (!stat(manifestPath).isFile() || stat(manifestPath).isSymbolicLink()) throw new Error('sync manifest must be a regular file');
    previous = JSON.parse(readFileSync(manifestPath, 'utf8'));
    if (previous.version !== 1 || previous.source !== '.agents/skills' || !previous.skills || typeof previous.skills !== 'object' || Array.isArray(previous.skills)) {
      throw new Error('unsupported or invalid sync manifest; inspect it before continuing');
    }
    for (const [name, files] of Object.entries(previous.skills)) {
      if (!safeName(name) || !files || typeof files !== 'object' || Array.isArray(files)) throw new Error('invalid skill in sync manifest');
      for (const [file, digest] of Object.entries(files)) {
        if (!safeFile(file) || !/^[a-f0-9]{64}$/.test(digest)) throw new Error('invalid file/checksum in sync manifest');
      }
    }
  }
  const manifestSnapshot = existsSync(manifestPath) ? hash(manifestPath) : null;
  const snapshot = (directory) => {
    if (!stat(directory)) return null;
    regularDirectory(directory);
    const files = Object.create(null);
    const directories = [];
    const walk = (current, prefix = '') => {
      for (const entry of readdirSync(current, { withFileTypes: true }).sort((a, b) => a.name.localeCompare(b.name))) {
        const relative = prefix ? `${prefix}/${entry.name}` : entry.name;
        const filename = path.join(current, entry.name);
        if (entry.isSymbolicLink()) throw new Error(`symlink is unsupported: ${path.relative(root, filename)}`);
        if (!safeFile(relative)) throw new Error(`nonportable skill resource path: ${relative}`);
        if (entry.isDirectory()) { directories.push(relative); walk(filename, relative); }
        else if (entry.isFile()) files[relative] = hash(filename);
        else throw new Error(`unsupported filesystem entry: ${path.relative(root, filename)}`);
      }
    };
    walk(directory);
    return { files, directories };
  };
  const names = readdirSync(sourceRoot, { withFileTypes: true }).filter((entry) => !entry.name.startsWith('.')).map((entry) => entry.name).sort();
  for (const name of Object.keys(previous.skills)) {
    if (!names.includes(name)) conflicts.push(`${name}: canonical skill was removed; no deletion is performed`);
  }
  for (const name of names) {
    const sourceTree = snapshot(path.join(sourceRoot, name));
    const targetTree = snapshot(path.join(targetRoot, name));
    const source = sourceTree.files;
    const target = targetTree?.files;
    const baseline = Object.hasOwn(previous.skills, name) ? previous.skills[name] : {};
    sourceSnapshots.set(name, sourceTree);
    targetSnapshots.set(name, targetTree);
    nextSkills[name] = source;
    for (const file of [...new Set([...Object.keys(source), ...Object.keys(target ?? {}), ...Object.keys(baseline)])].sort()) {
      const current = source[file];
      const copy = target?.[file];
      const before = Object.hasOwn(baseline, file) ? baseline[file] : undefined;
      const label = `${name}/${file}`;
      if (current && targetTree?.directories.includes(file)) conflicts.push(`${label}: Claude directory conflicts with a canonical file; preserved`);
      else if (before && !current) conflicts.push(`${label}: canonical file was removed; no deletion is performed`);
      else if (before && !copy) conflicts.push(`${label}: Claude copy was removed; preserve/reconcile that change first`);
      else if (!current && copy) conflicts.push(`${label}: extra Claude file would diverge from canonical source; preserved`);
      else if (copy === current) continue;
      else if (copy && copy !== before) conflicts.push(`${label}: existing Claude content differs; preserved`);
      else operations.push({ name, file, action: copy ? 'UPDATE' : 'ADD' });
    }
  }
  if (conflicts.length) throw new Error(`sync conflict; nothing written:\n${conflicts.map((item) => `  ${item}`).join('\n')}`);
  const nextManifest = { version: 1, source: '.agents/skills', skills: nextSkills };
  const manifestChanged = !same(previous, nextManifest) || !existsSync(manifestPath);
  operations.forEach(({ name, file, action }) => console.log(`${action} .claude/skills/${name}/${file}`));
  if (manifestChanged) console.log('UPDATE .claude/.agent-skills-sync.json');
  if (dryRun) {
    console.log(`${check ? 'CHECK' : 'DRY RUN'} ${operations.length} file changes; ${manifestChanged ? 'manifest update needed' : 'manifest current'}; nothing written`);
    if (check && (operations.length || manifestChanged)) process.exitCode = 1;
    return;
  }
  // Recheck all inputs after preflight, before the first mutation. Per-file baselines
  // also allow a partially interrupted sync to resume when every copied file is safe.
  for (const name of names) {
    if (!same(snapshot(path.join(sourceRoot, name)), sourceSnapshots.get(name))
        || !same(snapshot(path.join(targetRoot, name)), targetSnapshots.get(name))) {
      throw new Error('skills changed during preflight; rerun after edits finish (nothing written)');
    }
  }
  if ((existsSync(manifestPath) ? hash(manifestPath) : null) !== manifestSnapshot) throw new Error('manifest changed during preflight; rerun (nothing written)');
  for (const { name, file, action } of operations) {
    const source = path.join(sourceRoot, name, file);
    const target = path.join(targetRoot, name, file);
    mkdirSync(path.dirname(target), { recursive: true });
    if (action === 'ADD') copyFileSync(source, target, constants.COPYFILE_EXCL);
    else {
      if (hash(target) !== targetSnapshots.get(name).files[file]) throw new Error(`Claude file changed during sync; stopped: ${name}/${file}`);
      const staging = `${target}.agent-sync-${randomUUID()}`;
      copyFileSync(source, staging, constants.COPYFILE_EXCL);
      renameSync(staging, target);
    }
    chmodSync(target, lstatSync(source).mode & 0o777);
  }
  if (manifestChanged) {
    mkdirSync(path.dirname(manifestPath), { recursive: true });
    const staging = `${manifestPath}.${randomUUID()}.tmp`;
    writeFileSync(staging, `${JSON.stringify(nextManifest, null, 2)}\n`, { flag: 'wx' });
    renameSync(staging, manifestPath);
  }
  console.log(`PASS synced ${names.length} project skills; ${operations.length} file changes; unrelated Claude skills preserved`);
}

try { main(); } catch (error) { console.error(`FAIL ${error.message}`); process.exitCode = 1; }
