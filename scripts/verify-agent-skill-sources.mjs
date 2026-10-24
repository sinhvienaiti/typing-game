#!/usr/bin/env node
// Read-only verification of recorded external skill folders, not whole plugins.
import { createHash } from 'node:crypto';
import { lstatSync, readdirSync, readFileSync } from 'node:fs';
import { homedir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

function main() {
  let manifest = fileURLToPath(new URL('../.agents/skill-sources.json', import.meta.url));
  const args = process.argv.slice(2);
  if (args.length === 1 && args[0] === '--help') {
    console.log('Usage: node scripts/verify-agent-skill-sources.mjs [--manifest FILE]\nRead installed external skill folders; compare file counts and hashes without changing the baseline.');
    return;
  }
  if (args.length) {
    if (args.length !== 2 || args[0] !== '--manifest' || args[1].startsWith('-')) throw new Error('Use --help for supported arguments.');
    manifest = path.resolve(args[1]);
  }
  const data = JSON.parse(readFileSync(manifest, 'utf8'));
  if (data.schemaVersion !== 1 || data.hashAlgorithm?.id !== 'sha256-recursive-node-collation-v1') throw new Error('Unsupported provenance schema or hash algorithm.');
  if (data.hashAlgorithm.recordEncoding !== 'UTF-8' || !Array.isArray(data.sources) || !data.sources.length) throw new Error('Invalid provenance metadata.');
  const expectedOptions = { usage: 'sort', sensitivity: 'variant', ignorePunctuation: false, numeric: false, caseFirst: 'false' };
  const options = data.hashAlgorithm.collatorOptions;
  if (data.hashAlgorithm.locale !== 'en-US' || !options || typeof options !== 'object'
      || Object.keys(options).length !== Object.keys(expectedOptions).length
      || Object.entries(expectedOptions).some(([key, value]) => options[key] !== value)) {
    throw new Error('Algorithm v1 requires the explicit en-US collator and all recorded options.');
  }
  const collator = new Intl.Collator(data.hashAlgorithm.locale, data.hashAlgorithm.collatorOptions);
  const resolved = collator.resolvedOptions();
  if (resolved.locale !== 'en-US' || resolved.collation !== 'default'
      || Object.entries(expectedOptions).some(([key, value]) => resolved[key] !== value)) {
    throw new Error('Runtime cannot reproduce the requested collation without fallback.');
  }
  const sha = bytes => createHash('sha256').update(bytes).digest('hex');
  const validName = value => typeof value === 'string' && /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(value);
  const digest = directory => {
    if (!lstatSync(directory).isDirectory() || lstatSync(directory).isSymbolicLink()) throw new Error('Skill root must be a regular directory.');
    const records = [];
    const walk = (current, prefix = '') => {
      const entries = readdirSync(current, { withFileTypes: true })
        .filter(entry => !['.DS_Store', '__pycache__'].includes(entry.name))
        .sort((a, b) => collator.compare(a.name, b.name));
      for (let index = 1; index < entries.length; index += 1) {
        if (collator.compare(entries[index - 1].name, entries[index].name) === 0) throw new Error('Ambiguous filename collation; inspect before revising the algorithm.');
      }
      for (const entry of entries) {
        const relative = prefix ? `${prefix}/${entry.name}` : entry.name;
        const filename = path.join(current, entry.name);
        if (/[\0\r\n\\]/.test(entry.name)) throw new Error('Unsupported filename in skill tree.');
        if (entry.isDirectory()) walk(filename, relative);
        else if (entry.isFile()) records.push(`${relative}\0${sha(readFileSync(filename))}\n`);
        else throw new Error('Symlinks and special filesystem entries are unsupported.');
      }
    };
    walk(directory);
    return { fileCount: records.length, hash: sha(records.join('')) };
  };
  let checked = 0;
  let failures = 0;
  for (const source of data.sources) {
    if (!['user', 'plugin'].includes(source.scope) || typeof source.location !== 'string'
        || !(source.location.startsWith('~/') || path.isAbsolute(source.location))
        || !Array.isArray(source.skills) || !source.skills.length) throw new Error('Invalid source location, scope or skills.');
    const base = source.location.startsWith('~/') ? path.join(homedir(), source.location.slice(2)) : source.location;
    for (const skill of source.skills) {
      if (!validName(skill.name) || !Number.isInteger(skill.fileCount) || skill.fileCount < 1
          || !/^[a-f0-9]{64}$/.test(skill.treeSha256)) throw new Error('Invalid recorded skill name, count or hash.');
      checked += 1;
      try {
        const actual = digest(path.join(base, ...(source.scope === 'plugin' ? ['skills'] : []), skill.name));
        if (actual.fileCount !== skill.fileCount || actual.hash !== skill.treeSha256) throw new Error('File count or SHA-256 differs from the recorded baseline.');
        console.log(`PASS ${source.scope}/${skill.name} (${actual.fileCount} files)`);
      } catch (error) {
        failures += 1;
        console.error(`FAIL ${source.scope}/${skill.name}: ${error.code ?? error.message}`);
      }
    }
  }
  console.log(`${failures ? 'FAIL' : 'PASS'} ${checked} external skill trees; ${failures} failures; baseline unchanged`);
  if (failures) process.exitCode = 1;
}

try { main(); }
catch (error) { console.error(`FAIL ${error.code ?? error.message}`); process.exitCode = 1; }
