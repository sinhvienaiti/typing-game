// node --test tests/contract.test.mjs
// The contract is the one place games, the importer and the Admin agree on.
// Its effect enums and id rule must equal the kit's (TYPING_FEEL_SERVICE.md
// §3.4); the kit comparison skips in a split repo without ../shared/game-kit.
import assert from "node:assert/strict";
import { existsSync, readFileSync } from "node:fs";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import { loadContract } from "../tools/import-staging.mjs";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const KIT = path.resolve(ROOT, "../shared/game-kit/feedback/typing-fx");
const contract = loadContract();

test("contract: schemas, URLs and the version rule", () => {
  assert.equal(contract.contract, 1);
  assert.equal(contract.catalogue.schema, "typing-feel/catalogue-3");
  assert.equal(contract.set.schema, "typing-feel/set-1");
  assert.equal(contract.urls.catalogue.path, "/v1/keys/keys-manifest.json");
  assert.equal(contract.urls.catalogue.cacheControl, "no-cache");
  assert.equal(contract.urls.setManifest.path, "/v1/keys/sets/<id>/<fp12>/keys-manifest.json");
  assert.equal(contract.urls.setManifest.cacheControl, "public, max-age=31536000, immutable");
  assert.equal(contract.urls.setAudio.contentType, "audio/ogg");
  assert.equal(contract.urls.health.path, "/v1/health.json");
  assert.deepEqual(contract.urls.everyResponse, { "Access-Control-Allow-Origin": "*", "Cross-Origin-Resource-Policy": "cross-origin", "X-Content-Type-Options": "nosniff" });
  assert.equal(contract.versioning.readersIgnoreUnknownFields, true);
});

test("contract: fields, labels, recipes and the fingerprint rule are self-consistent", () => {
  const profile = contract.catalogue.profile;
  for (const field of profile.kitRequired) assert.ok(profile.required.includes(field), field);
  for (const field of [...profile.required, ...profile.optional]) assert.ok(Object.hasOwn(profile.fields, field) || ["id", "name"].includes(field), `documented: ${field}`);
  assert.ok(profile.optional.includes("labels"), "legacy-218 labels are an optional, additive field");
  assert.ok(Object.hasOwn(contract.labels, "legacy-218"));
  assert.deepEqual(Object.keys(contract.recipes).sort(), ["firefly-218", "natural-v1"]);
  assert.deepEqual(contract.statuses, ["published", "provisional"]);
  assert.deepEqual(contract.set.file.required, ["file", "set", "durationMs"]);
  assert.equal(new RegExp(contract.fingerprint.pattern).test("0123456789ab"), true);
  assert.equal(new RegExp(contract.fingerprint.pattern).test("0123456789abc"), false);
  assert.match(contract.fingerprint.seed.rule, /sha256/);
  assert.match(contract.fingerprint.admin.keepSeedPaths, /G6/);
  const id = new RegExp(contract.id.pattern);
  for (const good of ["bright-clack", "a", "x".repeat(32)]) assert.ok(id.test(good), good);
  for (const bad of ["", "-a", "Bright", "x".repeat(33), "a_b"]) assert.ok(!id.test(bad), bad);
});

test("contract: effect defaults sit inside the effect enums", () => {
  const { styles, intensities, sizes, volume, defaults } = contract.effects;
  assert.ok(styles.includes(defaults.style));
  assert.ok(intensities.includes(defaults.intensity));
  assert.ok(sizes.includes(defaults.size));
  assert.ok(defaults.volume >= volume.min && defaults.volume <= volume.max);
  assert.deepEqual(defaults, { style: "stamp", intensity: "normal", size: "large", volume: 1 });
});

/** `export const NAME = ["a", "b"] as const;` -> ["a", "b"]. */
function constList(text, name) {
  const match = new RegExp(`export const ${name}\\s*=\\s*\\[([^\\]]*)\\]\\s*as const`).exec(text);
  assert.ok(match, `${name} not found in the kit`);
  return [...match[1].matchAll(/"([^"]*)"/g)].map((item) => item[1]);
}

test("contract vs kit: TYPING_FX_STYLES / INTENSITIES / SIZES, defaults, id rule, resolver and set minimum", (t) => {
  if (!existsSync(path.join(KIT, "settings.ts")) || !existsSync(path.join(KIT, "audio.ts"))) {
    t.skip(`../shared/game-kit is absent (split repo?): ${KIT} not found, contract-vs-kit check skipped`);
    return;
  }
  const settings = readFileSync(path.join(KIT, "settings.ts"), "utf8");
  const audio = readFileSync(path.join(KIT, "audio.ts"), "utf8");
  assert.deepEqual(contract.effects.styles, constList(settings, "TYPING_FX_STYLES"));
  assert.deepEqual(contract.effects.intensities, constList(settings, "TYPING_FX_INTENSITIES"));
  assert.deepEqual(contract.effects.sizes, constList(settings, "TYPING_FX_SIZES"));
  const kitDefaults = /DEFAULT_TYPING_FX[^=]*=\s*Object\.freeze\(\{([^}]*)\}\)/.exec(settings);
  assert.ok(kitDefaults, "DEFAULT_TYPING_FX not found");
  for (const field of ["style", "intensity", "size"]) {
    assert.match(kitDefaults[1], new RegExp(`${field}:\\s*"${contract.effects.defaults[field]}"`), `kit default ${field}`);
  }
  // The catalogue loader's id test is the contract's id pattern, literally (inline or as a named constant).
  assert.ok(audio.includes(`/${contract.id.pattern}/`), `kit audio.ts has no /${contract.id.pattern}/`);
  assert.match(audio, /\.test\(row\.id\)/, "kit loadKeyboardCatalog tests row.id");
  // The kit drops a row whose id is its silent choice, so the contract reserves it.
  assert.ok(audio.includes('new Set(["off"])'), "kit loadKeyboardCatalog seeds its seen ids with off");
  assert.deepEqual(contract.id.reserved, ["off"]);
  const start = audio.indexOf("const resolve = (relative: string): string => {");
  assert.ok(start >= 0, "kit resolve() not found");
  const body = audio.slice(start, audio.indexOf("return root + relative;", start));
  assert.ok(body.includes("relative.startsWith(\"/\")"), "kit refuses a leading /");
  assert.ok(body.includes("!relative"), "kit refuses an empty path");
  const charClass = /\/\[([^\]]+)\]\/\.test\(relative\)/.exec(body)?.[1] ?? "";
  for (const character of contract.paths.forbiddenCharacters) {
    const escaped = JSON.stringify(character).slice(1, -1);
    assert.ok(body.includes(`relative.includes("${escaped}")`) || charClass.includes(character), `kit refuses ${JSON.stringify(character)}`);
  }
  for (const segment of contract.paths.forbiddenSegments) assert.ok(body.includes(`part === "${segment}"`), `kit refuses the ${segment} segment`);
  const want = (set) => Number(new RegExp(`${set}:\\s*\\{\\s*min:\\s*\\d+,\\s*want:\\s*(\\d+)`).exec(audio)?.[1]);
  assert.deepEqual(contract.set.minimum, { key: want("key"), space: want("space") });
});
