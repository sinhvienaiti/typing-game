// Kiểm mã kit thật với staging 189 bằng filesystem; không mở server hay tải mạng.
import assert from "node:assert/strict";
import { readFile, stat } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import { createHash } from "node:crypto";
import path from "node:path";
import ts from "../../../shared/game-kit/node_modules/typescript/lib/typescript.js";

const repo = fileURLToPath(new URL("../../../", import.meta.url));
const compile = (source) => ts.transpileModule(source, { compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.ESNext } }).outputText;
const dataUrl = (source) => "data:text/javascript;base64," + Buffer.from(source).toString("base64");
const audioSource = await readFile(path.join(repo, "shared/game-kit/feedback/typing-fx/audio.ts"), "utf8");
const intensity = compile(await readFile(path.join(repo, "shared/game-kit/feedback/typing-fx/intensity.ts"), "utf8"));
const compiled = compile(audioSource).replace('from "./intensity"', `from "${dataUrl(intensity)}"`);
const { loadKeyboardCatalog, keyboardFiles } = await import(dataUrl(compiled));
const staging = path.resolve(repo, process.argv[2] ?? "tmp/keys-firefly/staging/keys-firefly");
const requests = [];
const catalogue = await loadKeyboardCatalog("/local-keys/", { fallback: [], fetchJson: async (url) => {
  requests.push(url);
  return JSON.parse(await readFile(path.join(staging, url.slice("/local-keys/".length)), "utf8"));
} });
assert.equal(catalogue.state, "ready");
assert.deepEqual(requests, ["/local-keys/keys-manifest.json"]);
assert.deepEqual(catalogue.options.map((p) => p.value), ["off", "deep", "warm", "rounded", "solid", "crisp", "clear", "bright-clack"]);
const packs = [];
for (const choice of catalogue.options.slice(1)) {
  const manifest = JSON.parse(await readFile(path.join(staging, choice.manifest.slice("/local-keys/".length)), "utf8"));
  const files = keyboardFiles(manifest, choice.manifest.slice(0, choice.manifest.lastIndexOf("/") + 1));
  assert.equal(files.key.length, 10);
  assert.equal(files.space.length, 3);
  for (const url of [...files.key, ...files.space, choice.preview]) assert.ok((await stat(path.join(staging, url.slice("/local-keys/".length)))).size > 0);
  packs.push({ id: choice.value, keys: files.key.length, spaces: files.space.length, preview: choice.preview });
}
console.log(JSON.stringify({ state: catalogue.state, source: staging, audioTsSha256: createHash("sha256").update(audioSource).digest("hex"), catalogueRequestsOnly: requests, options: catalogue.options.map((p) => ({ id: p.value, name: p.label })), packs, checkedSampleFiles: 91, checkedPreviews: 7, networkRequests: 0 }, null, 2));
