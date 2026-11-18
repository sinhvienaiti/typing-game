// Kiểm mã kit thật với staging v2 bằng filesystem; không dùng server hoặc mạng.
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
const staging = path.resolve(repo, process.argv[2] ?? "tmp/keys-firefly/staging-v2/keys-firefly");
const requests = [];
const catalogue = await loadKeyboardCatalog("/local-keys/", { fallback: [], extra: [{ value: "relay", label: "Relay" }], fetchJson: async (url) => {
  requests.push(url);
  return JSON.parse(await readFile(path.join(staging, url.slice("/local-keys/".length)), "utf8"));
} });
assert.equal(catalogue.state, "ready");
assert.deepEqual(requests, ["/local-keys/keys-manifest.json"]);
assert.deepEqual(catalogue.options.slice(0, 2).map((p) => p.value), ["off", "relay"]);
const raw = JSON.parse(await readFile(path.join(staging, "keys-manifest.json"), "utf8"));
const ordered = [...raw.profiles].sort((a, b) => a.order - b.order);
assert.deepEqual(catalogue.options.slice(2).map((p) => p.value), ordered.map((p) => p.id));
const packs = [];
let checkedSamples = 0;
for (const [i, choice] of catalogue.options.slice(2).entries()) {
  assert.equal(choice.family, ordered[i].family);
  assert.equal(choice.score, ordered[i].score);
  const manifest = JSON.parse(await readFile(path.join(staging, choice.manifest.slice("/local-keys/".length)), "utf8"));
  const files = keyboardFiles(manifest, choice.manifest.slice(0, choice.manifest.lastIndexOf("/") + 1));
  for (const url of [...files.key, ...files.space, choice.preview]) assert.ok((await stat(path.join(staging, url.slice("/local-keys/".length)))).size > 0);
  checkedSamples += files.key.length + files.space.length;
  packs.push({ id: choice.value, family: choice.family, score: choice.score, keys: files.key.length, spaces: files.space.length, total: files.key.length + files.space.length });
}
console.log(JSON.stringify({ state: catalogue.state, source: staging, audioTsSha256: createHash("sha256").update(audioSource).digest("hex"), catalogueRequestsOnly: requests, cataloguePacks: packs.length, families: [...new Set(packs.map((p) => p.family))], ownerMoreThan80Met: packs.length > 80, keyRange: [Math.min(...packs.map((p) => p.keys)), Math.max(...packs.map((p) => p.keys))], totalRange: [Math.min(...packs.map((p) => p.total)), Math.max(...packs.map((p) => p.total))], packs, checkedSampleFiles: checkedSamples, checkedPreviews: packs.length, networkRequests: 0 }, null, 2));
