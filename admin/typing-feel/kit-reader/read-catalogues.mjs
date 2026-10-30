// Loads each exported Typing Feel folder with the games' own reader
// (shared/game-kit/feedback/typing-fx/audio.ts loadKeyboardCatalog and
// keyboardFiles), exactly as a game does, and prints what it understood.
//   node --experimental-transform-types --import ./register.mjs read-catalogues.mjs <kitAudioTs> <publicDir>...
import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { pathToFileURL } from "node:url";

const [kitFile, ...publicDirs] = process.argv.slice(2);
const kit = await import(pathToFileURL(kitFile).href);
const BASE = "https://feel.test/v1/keys/";
const results = [];
for (const publicDir of publicDirs) {
  const keys = join(publicDir, "v1", "keys");
  const fetchJson = async (url) => {
    if (!url.startsWith(BASE)) throw new Error(`Unexpected URL ${url}`);
    return JSON.parse(await readFile(join(keys, ...url.slice(BASE.length).split("/")), "utf8"));
  };
  const catalogue = await kit.loadKeyboardCatalog(BASE, { fetchJson });
  const sets = [];
  for (const option of catalogue.options) {
    if (!option.manifest) continue;
    const manifest = await fetchJson(option.manifest);
    const folder = option.manifest.slice(0, option.manifest.lastIndexOf("/") + 1);
    const files = kit.keyboardFiles(manifest, folder);
    sets.push({ id: option.value, label: option.label, family: option.family ?? null, keys: files.key.length, spaces: files.space.length, preview: option.preview, firstKey: files.key[0] ?? null });
  }
  results.push({ publicDir, state: catalogue.state, revision: catalogue.revision ?? null, defaultId: catalogue.defaultId ?? null, effects: catalogue.effects ?? null, options: catalogue.options.map((option) => option.value), sets });
}
process.stdout.write(`${JSON.stringify(results)}\n`);
