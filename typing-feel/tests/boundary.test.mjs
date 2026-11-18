// node --test tests/boundary.test.mjs
// typing-feel/ stands alone (TYPING_FEEL_SERVICE.md §6.1): its code imports only
// Node built-ins and files inside this folder, so moving it to its own repo
// later is just moving the folder.
import assert from "node:assert/strict";
import { existsSync, readdirSync, readFileSync } from "node:fs";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const CODE = /\.(?:m?js|cjs|m?ts|cts|tsx?)$/;
const FOLDERS = ["tools", "src", "tests"];

/** Every module specifier in `text`: static and dynamic import, export … from, require. */
export function specifiers(text) {
  const found = [];
  const patterns = [
    /\bimport\s+(?:[\w*{}\s,$]+?\s+from\s+)?["']([^"']+)["']/g,
    /\bexport\s+(?:\*|\{[^}]*\}|\*\s+as\s+\w+)\s*from\s*["']([^"']+)["']/g,
    /\bimport\s*\(\s*["'`]([^"'`]+)["'`]\s*\)/g,
    /\brequire\s*\(\s*["'`]([^"'`]+)["'`]\s*\)/g,
  ];
  for (const pattern of patterns) for (const match of text.matchAll(pattern)) found.push(match[1]);
  return found;
}

/** Why `specifier` imported from `file` leaves typing-feel/, or null. */
export function outside(file, specifier) {
  if (specifier.startsWith("node:")) return null;
  if (!specifier.startsWith("./") && !specifier.startsWith("../")) return "not a node: built-in or a relative path";
  const target = path.resolve(path.dirname(file), specifier);
  const rel = path.relative(ROOT, target);
  return rel === "" || rel.startsWith("..") || path.isAbsolute(rel) ? "resolves outside typing-feel/" : null;
}

function codeFiles() {
  const files = [];
  const walk = (dir) => {
    for (const entry of readdirSync(dir, { withFileTypes: true })) {
      if (entry.name === "node_modules") continue;
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) walk(full);
      else if (CODE.test(entry.name)) files.push(full);
    }
  };
  for (const folder of FOLDERS) if (existsSync(path.join(ROOT, folder))) walk(path.join(ROOT, folder));
  return files;
}

test("the scanner sees every import form (so the boundary check is not empty)", () => {
  // Keywords are spliced in so this file's own text holds no such import.
  const [IMPORT, EXPORT, REQUIRE] = ["import", "export", "require"];
  const sample = [
    `${IMPORT} a from "../../shared/game-kit/x.ts";`,
    `${IMPORT} { b, c } from './ok.mjs';`,
    `${IMPORT} "side-effect";`,
    `${EXPORT} * from "../../admin/store.mjs";`,
    `const d = await ${IMPORT}('three');`,
    `const e = ${REQUIRE}("fs");`,
  ].join("\n");
  assert.deepEqual(specifiers(sample), ["../../shared/game-kit/x.ts", "./ok.mjs", "side-effect", "../../admin/store.mjs", "three", "fs"]);
  const here = path.join(ROOT, "tools/x.mjs");
  assert.equal(outside(here, "node:fs"), null);
  assert.equal(outside(here, "../contract/a.json"), null);
  assert.match(outside(here, "../../shared/game-kit/x.ts"), /outside/);
  assert.match(outside(here, "three"), /built-in/);
  assert.match(outside(here, "fs"), /built-in/);
});

test("tools/, src/ and tests/ import nothing outside typing-feel/", () => {
  const files = codeFiles();
  assert.ok(files.some((file) => file.endsWith(path.join("tools", "import-staging.mjs"))), "the importer is scanned");
  const offenders = [];
  for (const file of files) {
    for (const specifier of specifiers(readFileSync(file, "utf8"))) {
      const problem = outside(file, specifier);
      if (problem) offenders.push(`${path.relative(ROOT, file)}: ${specifier} (${problem})`);
    }
  }
  assert.deepEqual(offenders, []);
});

test("package.json has no dependencies (Node built-ins only)", () => {
  const pkg = JSON.parse(readFileSync(path.join(ROOT, "package.json"), "utf8"));
  assert.equal(pkg.private, true);
  assert.equal(pkg.type, "module");
  for (const field of ["dependencies", "devDependencies", "peerDependencies", "optionalDependencies"]) assert.equal(pkg[field], undefined, field);
});
