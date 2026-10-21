#!/usr/bin/env node
// No runtime dependencies: project skills intentionally use string-only YAML frontmatter.
import { existsSync, lstatSync, readdirSync, readFileSync, realpathSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

export function repositoryRoot(explicitRoot) {
  return explicitRoot
    ? path.resolve(explicitRoot)
    : execFileSync('git', ['rev-parse', '--show-toplevel'], { encoding: 'utf8' }).trim();
}

// Reject unsupported YAML instead of silently accepting an invalid document. Supporting
// scalar keys is sufficient for this repo; nested metadata needs a real YAML parser.
export function readFrontmatter(text) {
  const lines = text.replace(/^\uFEFF/, '').replace(/\r\n/g, '\n').split('\n');
  if (lines[0] !== '---') throw new Error('SKILL.md must begin with YAML frontmatter');
  const end = lines.indexOf('---', 1);
  if (end < 0) throw new Error('frontmatter has no closing ---');
  const result = Object.create(null);
  for (let index = 1; index < end; index += 1) {
    const line = lines[index];
    if (!line.trim() || /^\s*#/.test(line)) continue;
    const match = /^([a-z][a-z0-9_-]*):(?: +(.*))?$/.exec(line);
    if (!match) throw new Error(`unsupported YAML at line ${index + 1}; use top-level string fields`);
    const [, key, raw = ''] = match;
    if (key in result) throw new Error(`duplicate frontmatter key: ${key}`);
    let value;
    if (/^[>|][-+]?\s*(?:#.*)?$/.test(raw)) {
      const block = [];
      while (index + 1 < end && (/^ +\S/.test(lines[index + 1]) || !lines[index + 1].trim())) {
        block.push(lines[++index]);
      }
      const nonempty = block.filter((part) => part.trim());
      const indent = nonempty.length ? Math.min(...nonempty.map((part) => /^ */.exec(part)[0].length)) : 0;
      if (!indent) throw new Error(`empty or unindented block string: ${key}`);
      value = block.map((part) => part.slice(indent)).join(raw[0] === '>' ? ' ' : '\n').trim();
    } else if (raw.startsWith('"')) {
      // JSON strings form a portable, unambiguous subset of YAML double-quoted strings.
      try { value = JSON.parse(raw); } catch { throw new Error(`invalid quoted string: ${key}`); }
    } else if (raw.startsWith("'")) {
      if (!/^'(?:[^']|'')*'$/.test(raw)) throw new Error(`invalid quoted string: ${key}`);
      value = raw.slice(1, -1).replace(/''/g, "'");
    } else {
      value = raw.replace(/\s+#.*$/, '').trim();
      if (!value || /^[!&*\[\]{}|>@`"'%]/.test(value) || /^[?:-](?:\s|$)/.test(value) || /:(?:\s|$)/.test(value)
          || /^(?:null|true|false|yes|no|on|off|~|[-+]?\d.*)$/i.test(value)) {
        throw new Error(`ambiguous or unsupported YAML value for ${key}; quote the string`);
      }
    }
    if (typeof value !== 'string') throw new Error(`${key} must be a string`);
    result[key] = value;
  }
  return { fields: result, body: lines.slice(end + 1).join('\n') };
}

function inside(root, filename) {
  const relative = path.relative(root, filename);
  return relative !== '..' && !relative.startsWith(`..${path.sep}`) && !path.isAbsolute(relative);
}

export function validateSkills(root) {
  const errors = [];
  const warnings = [];
  const skillsRoot = path.join(root, '.agents', 'skills');
  const names = new Set();
  let count = 0;
  const fail = (filename, message) => errors.push(`${path.relative(root, filename)}: ${message}`);
  const checkTarget = (document, raw, fromRoot = false) => {
    if (/^(?:[a-z][a-z0-9+.-]*:|#|\/\/)/i.test(raw)) return;
    let target;
    try { target = decodeURIComponent(raw.replace(/^<|>$/g, '').split(/[?#]/)[0]); }
    catch { fail(document, `invalid link encoding: ${raw}`); return; }
    if (!target) return;
    const filename = path.resolve(fromRoot ? root : path.dirname(document), target);
    if (!inside(root, filename)) fail(document, `reference escapes the repository: ${raw}`);
    else if (!existsSync(filename)) fail(document, `missing reference: ${raw}`);
    else if (!inside(realpathSync(root), realpathSync(filename))) fail(document, `reference resolves outside the repository: ${raw}`);
  };
  const checkMarkdown = (filename) => {
    const markdown = readFileSync(filename, 'utf8');
    if (/\b(?:TODO|TBD|FIXME)\b|\[(?:INSERT|REPLACE|DESCRIPTION HERE)[^\]]*\]/i.test(markdown)) {
      fail(filename, 'unfinished scaffold placeholder');
    }
    // Inline links/images and Markdown reference definitions. Anchors and web URLs
    // need no filesystem lookup; local links are relative to their Markdown file.
    for (const match of markdown.matchAll(/!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:\s+["'][^\n]*["'])?\s*\)/g)) {
      checkTarget(filename, match[1]);
    }
    for (const match of markdown.matchAll(/^ {0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)/gm)) {
      checkTarget(filename, match[1]);
    }
    // Also check bare source references in code spans. Root-named paths resolve
    // from Git root; ./, ../ and references/ paths resolve from the document.
    for (const match of markdown.matchAll(/`([^`\n\s]+)`/g)) {
      const target = match[1].replace(/:\d+(?::\d+)?$/, '');
      if (/[*?<>]/.test(target)) continue;
      const fromRoot = /^(?:games|docs|shared|admin|scripts|portal|\.github|\.agents|\.claude)\//.test(target);
      if (fromRoot || /^(?:\.\.?\/|references\/)/.test(target)) checkTarget(filename, target, fromRoot);
    }
  };
  const walk = (directory) => {
    for (const entry of readdirSync(directory, { withFileTypes: true })) {
      const filename = path.join(directory, entry.name);
      if (entry.isSymbolicLink()) fail(filename, 'skill resources must be regular files/directories, not symlinks');
      else if (entry.isDirectory()) walk(filename);
      else if (entry.isFile() && entry.name.endsWith('.md')) checkMarkdown(filename);
      else if (!entry.isFile()) fail(filename, 'unsupported filesystem entry');
    }
  };
  if (!existsSync(skillsRoot)) return { count, errors: ['.agents/skills is missing'], warnings };
  if (!lstatSync(skillsRoot).isDirectory() || lstatSync(skillsRoot).isSymbolicLink()) {
    return { count, errors: ['.agents/skills must be a regular directory'], warnings };
  }
  for (const entry of readdirSync(skillsRoot, { withFileTypes: true }).sort((a, b) => a.name.localeCompare(b.name))) {
    if (entry.name.startsWith('.')) continue;
    const directory = path.join(skillsRoot, entry.name);
    if (!entry.isDirectory() || entry.isSymbolicLink()) { fail(directory, 'expected a skill directory'); continue; }
    count += 1;
    const skill = path.join(directory, 'SKILL.md');
    if (!existsSync(skill)) { fail(skill, 'missing skill entrypoint'); continue; }
    try {
      if (!lstatSync(skill).isFile()) throw new Error('entrypoint must be a regular file');
      const { fields, body } = readFrontmatter(readFileSync(skill, 'utf8'));
      if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(fields.name ?? '') || fields.name.length > 64) {
        fail(skill, 'name must use lowercase letters/digits/hyphens and at most 64 characters');
      }
      if (fields.name !== entry.name) fail(skill, 'name must match the skill folder');
      if (names.has(fields.name)) fail(skill, `duplicate name: ${fields.name}`);
      names.add(fields.name);
      if (!fields.description || fields.description.length < 35 || fields.description.length > 1024) {
        fail(skill, 'description must meaningfully describe purpose and trigger (35-1024 characters)');
      } else if (!/\b(?:when|use|for)\b/i.test(fields.description)) {
        warnings.push(`${path.relative(root, skill)}: review whether description states when this skill applies`);
      }
      if (!body.trim()) fail(skill, 'skill instructions are empty');
    } catch (error) { fail(skill, error.message); }
    walk(directory);
  }
  if (!count) errors.push('.agents/skills contains no skills');
  return { count, errors, warnings };
}

if (import.meta.url === pathToFileURL(process.argv[1] ?? '').href) {
  try {
    let explicitRoot;
    for (let index = 2; index < process.argv.length; index += 1) {
      const arg = process.argv[index];
      if (arg === '--help') {
        console.log('Usage: node scripts/validate-agent-skills.mjs [--root PATH]\nChecks scalar YAML frontmatter, names, placeholders and local Markdown/source references.');
        process.exit(0);
      }
      if (arg !== '--root' || !process.argv[index + 1]) throw new Error(`unknown or incomplete option: ${arg}`);
      explicitRoot = process.argv[++index];
    }
    const result = validateSkills(repositoryRoot(explicitRoot));
    result.warnings.forEach((warning) => console.warn(`WARN ${warning}`));
    result.errors.forEach((error) => console.error(`FAIL ${error}`));
    console.log(`${result.errors.length ? 'FAIL' : 'PASS'} ${result.count} project skills; ${result.errors.length} errors, ${result.warnings.length} warnings`);
    if (result.errors.length) process.exitCode = 1;
  } catch (error) { console.error(`FAIL ${error.message}`); process.exitCode = 1; }
}
