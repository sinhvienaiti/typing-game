import fs from 'node:fs';
import {im, D, json} from './lib.mjs';

const records = JSON.parse(fs.readFileSync(`${D}/processed.json`));
const jobs = JSON.parse(fs.readFileSync(`${D}/jobs.json`));
const deliveredFiles = [];

for (const r of records) {
  const job = jobs.find(j => j.id === r.id);
  const promptText = job.prompt;

  const targetDir = job.targetDir;
  const selectedDir = job.selectedDir;
  fs.mkdirSync(selectedDir, {recursive: true});

  // Try file:
  const tryFile = r.version === 'new' 
    ? `${targetDir}/${r.baseName}.try${r.attempt}.png`
    : `${targetDir}/${r.baseName}.${r.version}-try${r.attempt}.png`;
  const tryPrompt = tryFile.replace(/\.png$/, '.prompt.txt');

  const src1024 = r.outputs.find(o => o.size[0] === 1024).file;
  fs.writeFileSync(tryFile, fs.readFileSync(src1024));
  fs.writeFileSync(tryPrompt, promptText + '\n');
  deliveredFiles.push(tryFile);

  // Selected files:
  for (const o of r.outputs) {
    const s = o.size[0];
    const selFile = `${selectedDir}/${r.name}${s === 1024 ? '' : '.' + s}.png`;
    const selPrompt = selFile.replace(/\.png$/, '.prompt.txt');
    fs.writeFileSync(selFile, fs.readFileSync(o.file));
    fs.writeFileSync(selPrompt, promptText + '\n');
    deliveredFiles.push(selFile);
  }
}

json(`${D}/delivered.json`, deliveredFiles);
console.log(`Updated delivery of ${deliveredFiles.length} files.`);
