import './lib/ts-hook.mjs';
import { readFileSync, statSync } from 'node:fs';
import path from 'node:path';
import { loadGameplays, loadKits } from './lib/spec-context.mjs';

const { validateSpec, specHash } = await import('../../shared/game-kit/map/spec.ts');

function main(args) {
  if (args[0] === 'build' || args[0] === 'check') {
    console.error(`${args[0]} not implemented in map-spec/0 (ticket 032)`);
    process.exitCode = 2;
    return;
  }
  if (args.length !== 2 || args[0] !== 'validate') {
    console.error('Usage: node tools/map-factory/cli.mjs validate <spec-directory>');
    process.exitCode = 2;
    return;
  }
  const file = path.join(args[1], 'map.spec.json');
  let text;
  try {
    if (!statSync(args[1]).isDirectory() || !statSync(file).isFile()) throw new Error('expected a spec directory with map.spec.json');
    text = readFileSync(file, 'utf8');
  } catch (error) {
    console.error(`${file}: ${error.message}`);
    process.exitCode = 2;
    return;
  }
  let spec;
  try {
    spec = JSON.parse(text);
  } catch {
    process.stdout.write('error spec-json ""\n');
    process.exitCode = 1;
    return;
  }
  const { gameplays, problems: gameplayProblems } = loadGameplays();
  const { kits, problems: kitProblems } = loadKits();
  const problems = [...gameplayProblems, ...kitProblems];
  if (problems.length) {
    for (const problem of problems) console.error(problem);
    process.exitCode = 2;
    return;
  }
  const errors = validateSpec(spec, { gameplays, kits });
  if (errors.length) {
    for (const { code, path } of errors) process.stdout.write(`error ${code} ${JSON.stringify(path)}\n`);
    process.exitCode = 1;
    return;
  }
  process.stdout.write(`ok ${specHash(spec)}\n`);
  process.exitCode = 0;
}

main(process.argv.slice(2));
