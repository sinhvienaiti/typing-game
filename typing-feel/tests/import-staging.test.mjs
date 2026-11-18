// node --test tests/import-staging.test.mjs
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import { existsSync, readdirSync, readFileSync, rmSync, statSync, writeFileSync } from "node:fs";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import { canonicalJson, ImportError, importStaging, LEGACY_LABEL, loadContract, main, parseArgs, pathProblem, seedFingerprint, setManifestText } from "../tools/import-staging.mjs";
import { fakeBytes, LICENCE, makeStaging, ROWS } from "./fixture.mjs";

const SCRIPT = fileURLToPath(new URL("../tools/import-staging.mjs", import.meta.url));
const contract = loadContract();
const T1 = Date.UTC(2026, 9, 31, 9, 0, 0);
const T2 = Date.UTC(2026, 10, 2, 12, 30, 0);
const sha = (bytes) => createHash("sha256").update(bytes).digest("hex");

function fixture(t, options) {
  const fx = makeStaging(options);
  t.after(fx.cleanup);
  return fx;
}
const read = (file) => JSON.parse(readFileSync(file, "utf8"));
const catalogueOf = (out) => read(path.join(out, "v1/keys/keys-manifest.json"));

/** Every file under `dir` (relative path -> bytes), for byte-identical comparisons. */
function snapshot(dir) {
  const files = new Map();
  const walk = (rel) => {
    for (const entry of readdirSync(path.join(dir, rel), { withFileTypes: true })) {
      const child = rel ? `${rel}/${entry.name}` : entry.name;
      if (entry.isDirectory()) walk(child);
      else files.set(child, readFileSync(path.join(dir, child)));
    }
  };
  walk("");
  return files;
}

/** The kit resolver's refusal rules (shared/game-kit/feedback/typing-fx/audio.ts loadKeyboardCatalog). */
function kitRefuses(relative) {
  return !relative || relative.startsWith("/") || relative.includes(":") || relative.includes("\\") ||
    relative.split("/").some((part) => part === ".." || part === ".") || /[?#%]/.test(relative);
}

test("layout: catalogue-3, one sets/<id>/<fp12>/ per set, set-1 manifests and health", async (t) => {
  const fx = fixture(t);
  const result = await importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 });
  assert.equal(result.profiles, 4);
  assert.equal(result.created.length, 4);
  const catalogue = catalogueOf(fx.out);
  assert.deepEqual(Object.keys(catalogue), ["schema", "contract", "revision", "publishedAt", "default", "effects", "families", "profiles"]);
  assert.equal(catalogue.schema, "typing-feel/catalogue-3");
  assert.equal(catalogue.contract, 1);
  assert.equal(catalogue.revision, "r1");
  assert.equal(catalogue.publishedAt, "2026-10-31T09:00:00Z");
  assert.equal(catalogue.default, "bright-clack");
  assert.deepEqual(catalogue.effects, { style: "stamp", intensity: "normal", size: "large", volume: 1 });
  for (const profile of catalogue.profiles) {
    for (const field of contract.catalogue.profile.required) assert.ok(Object.hasOwn(profile, field), `${profile.id}.${field}`);
    for (const field of Object.keys(profile)) assert.ok([...contract.catalogue.profile.required, ...contract.catalogue.profile.optional].includes(field), `unknown field ${field}`);
    assert.equal(profile.status, "published");
    const match = /^sets\/([a-z0-9-]+)\/([0-9a-f]{12})\/keys-manifest\.json$/.exec(profile.manifest);
    assert.ok(match, profile.manifest);
    assert.equal(match[1], profile.id);
    assert.equal(profile.preview, `sets/${profile.id}/${match[2]}/preview.ogg`);
    const folder = path.join(fx.out, "v1/keys", path.dirname(profile.manifest));
    const row = ROWS.find((item) => item.id === profile.id);
    const expected = [
      ...Array.from({ length: row.keys }, (_, i) => `key-${String(i + 1).padStart(2, "0")}.ogg`),
      ...Array.from({ length: row.spaces }, (_, i) => `space-${String(i + 1).padStart(2, "0")}.ogg`),
      "preview.ogg", "keys-manifest.json",
    ].sort();
    assert.deepEqual(readdirSync(folder).sort(), expected, "only the listed audio and the set manifest; no .bak.json");
    assert.equal(profile.keys, row.keys);
    assert.equal(profile.spaces, row.spaces);
    const set = read(path.join(folder, "keys-manifest.json"));
    // The documented seed rule, computed independently of the importer: the
    // set manifest without its name, plus every audio file sorted by name.
    const audio = expected.filter((name) => name.endsWith(".ogg")).map((file) => {
      const bytes = readFileSync(path.join(folder, file));
      return { bytes: bytes.length, file, sha256: sha(bytes) };
    });
    const { name: _name, ...content } = set;
    assert.equal(match[2], sha(canonicalJson({ ...content, audio })).slice(0, 12));
    assert.deepEqual(Object.keys(set), contract.set.required);
    assert.equal(set.schema, "typing-feel/set-1");
    assert.equal(set.id, profile.id);
    assert.equal(set.name, row.name);
    assert.equal(set.licence, LICENCE);
    assert.equal(set.preview, "preview.ogg");
    assert.deepEqual(set.files.map((entry) => entry.file), expected.filter((name) => /^(key|space)-/.test(name)));
    for (const entry of set.files) {
      assert.deepEqual(Object.keys(entry), ["file", "set", "durationMs"]);
      assert.ok(Number.isInteger(entry.durationMs) && entry.durationMs > 0);
    }
  }
  const health = read(path.join(fx.out, "v1/health.json"));
  assert.deepEqual(Object.keys(health), contract.health.required);
  assert.equal(health.contract, 1);
  assert.equal(health.revision, "r1");
  assert.equal(health.builtAt, "2026-10-31T09:00:00Z");
  assert.equal(health.build, `data-${sha(readFileSync(path.join(fx.out, "v1/keys/keys-manifest.json"))).slice(0, 12)}`);
});

test("durations: 218 rows round metrics.duration_ms, owner picks keep durationMs", async (t) => {
  const fx = fixture(t);
  await importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 });
  const catalogue = catalogueOf(fx.out);
  const setOf = (id) => read(path.join(fx.out, "v1/keys", catalogue.profiles.find((p) => p.id === id).manifest));
  assert.deepEqual(setOf("deep").files[0], { file: "key-01.ogg", set: "key", durationMs: 101 });
  assert.deepEqual(setOf("raindrop-tile").files.at(-1), { file: "space-08.ogg", set: "space", durationMs: 408 });
});

test("byte-exact: every copied file has its staging sha256, and the counts match", async (t) => {
  const fx = fixture(t);
  const result = await importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 });
  let count = 0;
  for (const profile of catalogueOf(fx.out).profiles) {
    const folder = path.join(fx.out, "v1/keys", path.dirname(profile.manifest));
    for (const name of readdirSync(folder).filter((file) => file.endsWith(".ogg"))) {
      assert.equal(sha(readFileSync(path.join(folder, name))), sha(readFileSync(path.join(fx.staging, profile.id, name))), `${profile.id}/${name}`);
      assert.deepEqual(readFileSync(path.join(folder, name)), fakeBytes(profile.id, name));
      count += 1;
    }
  }
  const staged = ROWS.reduce((sum, row) => sum + row.keys + row.spaces + 1, 0);
  assert.equal(count, staged);
  assert.equal(result.audioFiles, staged);
});

test("idempotent: a rerun on the same staging writes byte-identical JSON and no new folder", async (t) => {
  const fx = fixture(t);
  await importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 });
  const before = snapshot(fx.out);
  const mtime = statSync(path.join(fx.out, "v1/keys/keys-manifest.json")).mtimeMs;
  const again = await importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T2 });
  assert.equal(again.created.length, 0);
  assert.equal(again.reused.length, 4);
  assert.equal(again.catalogueWritten, false);
  assert.equal(again.healthWritten, false);
  assert.equal(again.publishedAt, "2026-10-31T09:00:00Z", "publishedAt stays on a no-op rerun");
  const after = snapshot(fx.out);
  assert.deepEqual([...after.keys()].sort(), [...before.keys()].sort());
  for (const [file, bytes] of before) assert.deepEqual(after.get(file), bytes, file);
  assert.equal(statSync(path.join(fx.out, "v1/keys/keys-manifest.json")).mtimeMs, mtime, "unchanged files are not rewritten");
  assert.equal(read(path.join(fx.out, "v1/health.json")).builtAt, "2026-10-31T09:00:00Z");
});

test("never overwrite: a set folder with other bytes is an error, and nothing changes", async (t) => {
  const fx = fixture(t);
  await importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 });
  const profile = catalogueOf(fx.out).profiles.find((p) => p.id === "deep");
  const folder = path.join(fx.out, "v1/keys", path.dirname(profile.manifest));
  writeFileSync(path.join(folder, "key-03.ogg"), "tampered");
  writeFileSync(path.join(folder, "extra.ogg"), "stray");
  const before = snapshot(fx.out);
  await assert.rejects(importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T2 }), (error) => {
    assert.ok(error instanceof ImportError);
    assert.match(error.message, /never overwritten/);
    assert.match(error.message, new RegExp(`${profile.manifest.replace("/keys-manifest.json", "")}/`));
    assert.match(error.message, /key-03\.ogg differs/);
    assert.match(error.message, /extra\.ogg is not part of this set/);
    return true;
  });
  const after = snapshot(fx.out);
  for (const [file, bytes] of before) assert.deepEqual(after.get(file), bytes, file);
  assert.equal(after.size, before.size);
});

test("never overwrite: an edited set manifest or a missing file is an error too", async (t) => {
  const fx = fixture(t);
  await importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 });
  const profile = catalogueOf(fx.out).profiles.find((p) => p.id === "raindrop-tile");
  const folder = path.join(fx.out, "v1/keys", path.dirname(profile.manifest));
  writeFileSync(path.join(folder, "keys-manifest.json"), "{}\n");
  await assert.rejects(importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T2 }), /keys-manifest\.json differs/);
  rmSync(path.join(folder, "key-01.ogg"));
  await assert.rejects(importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T2 }), /key-01\.ogg is missing/);
});

test("revisions: changed staging needs a new revision; old set folders stay; no step back", async (t) => {
  const fx = fixture(t);
  await importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 });
  const first = catalogueOf(fx.out).profiles.find((p) => p.id === "deep").manifest;
  writeFileSync(path.join(fx.staging, "deep/key-01.ogg"), "OggS re-made deep key 1");
  await assert.rejects(importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T2 }), /already holds revision r1 with other content.*--revision r2/s);
  const result = await importStaging({ stagingDir: fx.staging, publicDir: fx.out, revision: "r2", now: T2 });
  assert.equal(result.created.length, 1);
  const catalogue = catalogueOf(fx.out);
  assert.equal(catalogue.revision, "r2");
  assert.equal(catalogue.publishedAt, "2026-11-02T12:30:00Z");
  const second = catalogue.profiles.find((p) => p.id === "deep").manifest;
  assert.notEqual(second, first, "new bytes, new fp12");
  assert.ok(existsSync(path.join(fx.out, "v1/keys", first)), "the r1 folder is kept for rollback");
  assert.equal(read(path.join(fx.out, "v1/health.json")).revision, "r2");
  await assert.rejects(importStaging({ stagingDir: fx.staging, publicDir: fx.out, revision: "r1", now: T2 }), /holds revision "r2".*--revision r3/s);
  writeFileSync(path.join(fx.out, "v1/keys/keys-manifest.json"), JSON.stringify({ ...catalogue, revision: "admin-7" }));
  await assert.rejects(importStaging({ stagingDir: fx.staging, publicDir: fx.out, revision: "r3", now: T2 }), /did not write/);
});

test("rename: a new name alone keeps the set folder and URL; the catalogue carries it", async (t) => {
  const fx = fixture(t);
  await importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 });
  const first = catalogueOf(fx.out).profiles.find((p) => p.id === "deep");
  const setFile = path.join(fx.out, "v1/keys", first.manifest);
  const setBytes = readFileSync(setFile);
  const stagingCatalogue = path.join(fx.staging, "keys-manifest.json");
  const source = read(stagingCatalogue);
  source.profiles.find((p) => p.id === "deep").name = "Deep Velvet Two";
  writeFileSync(stagingCatalogue, JSON.stringify(source));
  await assert.rejects(importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T2 }), /already holds revision r1 with other content.*--revision r2/s);
  const result = await importStaging({ stagingDir: fx.staging, publicDir: fx.out, revision: "r2", now: T2 });
  assert.equal(result.created.length, 0, "no new folder for a rename");
  assert.equal(result.reused.length, 4);
  assert.deepEqual(result.warnings, [`set deep: ${path.dirname(first.manifest)}/ keeps its set manifest name "Deep Velvet"; the catalogue carries "Deep Velvet Two".`]);
  const profile = catalogueOf(fx.out).profiles.find((p) => p.id === "deep");
  assert.equal(profile.manifest, first.manifest, "same folder, same URL");
  assert.equal(profile.name, "Deep Velvet Two");
  assert.deepEqual(readFileSync(setFile), setBytes, "the immutable set manifest is never rewritten");
  const again = await importStaging({ stagingDir: fx.staging, publicDir: fx.out, revision: "r2", now: T2 + 60_000 });
  assert.equal(again.catalogueWritten, false, "rerun of r2 is a no-op");
  // A fresh public folder gets the same fp12: the name is not part of it.
  const fresh = path.join(fx.base, "fresh");
  await importStaging({ stagingDir: fx.staging, publicDir: fresh, now: T2 });
  assert.equal(catalogueOf(fresh).profiles.find((p) => p.id === "deep").manifest, first.manifest);
  assert.equal(read(path.join(fresh, "v1/keys", first.manifest)).name, "Deep Velvet Two");
});

for (const [label, edit] of [
  ["a re-measured duration", (m) => { m.files[0].metrics.duration_ms += 7; }],
  ["a new licence", (m) => { m.licence = `${m.licence} (re-licensed)`; }],
]) {
  test(`content: ${label} with the same audio gets a new folder under a new revision`, async (t) => {
    const fx = fixture(t);
    await importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 });
    const first = catalogueOf(fx.out).profiles.find((p) => p.id === "deep").manifest;
    const stagingSet = path.join(fx.staging, "deep/keys-manifest.json");
    const manifest = read(stagingSet);
    edit(manifest);
    writeFileSync(stagingSet, JSON.stringify(manifest));
    await assert.rejects(importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T2 }), /already holds revision r1 with other content/);
    const result = await importStaging({ stagingDir: fx.staging, publicDir: fx.out, revision: "r2", now: T2 });
    assert.equal(result.created.length, 1);
    const second = catalogueOf(fx.out).profiles.find((p) => p.id === "deep").manifest;
    assert.notEqual(second, first, "other set manifest content, other fp12");
    assert.ok(existsSync(path.join(fx.out, "v1/keys", first)), "the r1 folder is kept for rollback");
  });
}

test(".bak.json catalogues and builder notes are skipped", async (t) => {
  const fx = fixture(t);
  await importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 });
  const catalogue = catalogueOf(fx.out);
  assert.ok(!catalogue.profiles.some((p) => p.id === "ghost"));
  assert.ok(existsSync(path.join(fx.staging, "keys-manifest.33-sets.bak.json")));
  for (const file of snapshot(fx.out).keys()) assert.doesNotMatch(file, /bak\.json$|firefly-builder/);
});

test("order and families: grouped by first appearance, contiguous from 0", async (t) => {
  const fx = fixture(t);
  await importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 });
  const catalogue = catalogueOf(fx.out);
  assert.deepEqual(catalogue.families, [{ id: "deep", name: "Deep", order: 0 }, { id: "bright-clack", name: "Bright Clack", order: 1 }]);
  assert.deepEqual(catalogue.profiles.map((p) => [p.order, p.id, p.family, p.familyId]), [
    [0, "deep", "Deep", "deep"],
    [1, "deep-amber", "Deep", "deep"],
    [2, "bright-clack", "Bright Clack", "bright-clack"],
    [3, "raindrop-tile", "Bright Clack", "bright-clack"],
  ]);
});

test("legacy-218: 218 rows are labelled; owner picks keep ownerPick, null score and their note", async (t) => {
  const fx = fixture(t);
  const result = await importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 });
  assert.equal(result.legacy, 3);
  assert.ok(Object.hasOwn(contract.labels, LEGACY_LABEL));
  const catalogue = catalogueOf(fx.out);
  for (const profile of catalogue.profiles) {
    const row = ROWS.find((item) => item.id === profile.id);
    const set = read(path.join(fx.out, "v1/keys", profile.manifest));
    assert.equal(profile.score, row.score);
    if (row.ownerPick) {
      assert.equal(profile.ownerPick, true);
      assert.equal(profile.note, row.note);
      assert.equal(profile.labels, undefined);
      assert.equal(set.recipe, "natural-v1");
    } else {
      assert.equal(profile.ownerPick, false);
      assert.deepEqual(profile.labels, ["legacy-218"]);
      assert.equal(profile.note, undefined);
      assert.equal(set.recipe, "firefly-218");
    }
    assert.ok(Object.hasOwn(contract.recipes, set.recipe));
  }
});

test("path rules: the exporter refuses what the kit resolver refuses, and more", () => {
  for (const good of ["sets/deep/0123456789ab/keys-manifest.json", "sets/a-b/abcdef012345/key-01.ogg", "deep/preview.ogg"]) {
    assert.equal(pathProblem(good, contract), null, good);
    assert.equal(kitRefuses(good), false, good);
  }
  for (const bad of ["", "/abs/x.ogg", "../x.ogg", "a/../b.ogg", "a/./b.ogg", ".", "a:b.ogg", "https://x/y.ogg", "a\\b.ogg", "a?b.ogg", "a#b.ogg", "a%2e.ogg"]) {
    assert.notEqual(pathProblem(bad, contract), null, bad);
    assert.equal(kitRefuses(bad), true, `kit also refuses ${bad}`);
  }
  // Stricter than the kit: no empty segment, no upper case, no leading dot.
  for (const strict of ["a//b.ogg", "Deep/key-01.ogg", ".hidden/key-01.ogg", "a/b/"]) assert.notEqual(pathProblem(strict, contract), null, strict);
});

test("path rules: every catalogue path the import writes passes the kit resolver", async (t) => {
  const fx = fixture(t);
  await importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 });
  for (const profile of catalogueOf(fx.out).profiles) {
    for (const relative of [profile.manifest, profile.preview]) {
      assert.equal(kitRefuses(relative), false, relative);
      assert.equal(pathProblem(relative, contract), null, relative);
    }
  }
});

for (const [label, edit, pattern] of [
  ["a bad id", (c) => { c.profiles[0].id = "Deep_Velvet"; }, /does not match/],
  ["the reserved id off", (c) => { c.profiles[0].id = "off"; }, /"off" is reserved/],
  ["a duplicate id", (c) => { c.profiles[1].id = c.profiles[0].id; }, /listed twice/],
  ["a manifest path that leaves staging", (c) => { c.profiles[0].manifest = "../outside/keys-manifest.json"; }, /refused \("\.\." segment\)/],
  ["an absolute manifest path", (c) => { c.profiles[0].manifest = "/etc/keys-manifest.json"; }, /leading \//],
  ["a preview in another folder", (c) => { c.profiles[0].preview = "deep-amber/preview.ogg"; }, /share one set folder/],
  ["a traversing file name in a set", (c, m) => { m.deep.files[0].file = "../key-01.ogg"; }, /refused/],
  ["a file whose set does not match", (c, m) => { m.deep.files[0].set = "space"; }, /does not match key-01\.ogg/],
  ["a set below the key minimum", (c, m) => { m["deep-amber"].files = m["deep-amber"].files.slice(2); }, /at least 10 keys/],
  ["a set manifest naming another id", (c, m) => { m.deep.id = "deep-amber"; }, /names id/],
  ["a row that is neither an owner pick nor scored", (c) => { c.profiles[0].score = null; }, /recipe is unknown/],
  ["a wrong staging schema", (c) => { c.schema = "typing-keys-firefly/catalogue-1"; }, /expected typing-keys-firefly\/catalogue-2/],
]) {
  test(`refuses ${label}, before writing anything`, async (t) => {
    const fx = fixture(t, { edit });
    await assert.rejects(importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 }), (error) => {
      assert.ok(error instanceof ImportError, error.stack);
      assert.match(error.message, pattern);
      return true;
    });
    assert.equal(existsSync(fx.out), false, "nothing written");
  });
}

test("refuses a missing audio file and a missing default set", async (t) => {
  const fx = fixture(t);
  rmSync(path.join(fx.staging, "deep/key-02.ogg"));
  await assert.rejects(importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 }), /deep\/key-02\.ogg: file not found/);
  assert.equal(existsSync(fx.out), false);
  writeFileSync(path.join(fx.staging, "deep/key-02.ogg"), "back");
  await assert.rejects(importStaging({ stagingDir: fx.staging, publicDir: fx.out, defaultSet: "missing", now: T1 }), /Default set "missing"/);
  await assert.rejects(importStaging({ stagingDir: fx.staging, publicDir: fx.out, defaultSet: "off", now: T1 }), /default set: id "off" is reserved/);
  assert.equal(existsSync(fx.out), false);
});

test("unlisted audio in a set folder is reported, never copied", async (t) => {
  const fx = fixture(t);
  writeFileSync(path.join(fx.staging, "deep/key-99.ogg"), "unlisted");
  const result = await importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 });
  assert.deepEqual(result.warnings, ["set deep: deep/key-99.ogg is not listed in deep/keys-manifest.json; not copied."]);
  for (const file of snapshot(fx.out).keys()) assert.doesNotMatch(file, /key-99/);
});

test("set manifest text is the set-1 object, one file per line", () => {
  const manifest = { schema: "typing-feel/set-1", id: "x", name: "X \"quoted\"", licence: LICENCE, recipe: "natural-v1", files: [{ file: "key-01.ogg", set: "key", durationMs: 450 }], preview: "preview.ogg" };
  const text = setManifestText(manifest);
  assert.deepEqual(JSON.parse(text), manifest);
  assert.match(text, /\n {4}\{"file":"key-01\.ogg","set":"key","durationMs":450\}\n/);
  const audio = [{ file: "b", bytes: 1, sha256: "2" }, { file: "a", bytes: 3, sha256: "4" }];
  assert.equal(seedFingerprint(manifest, audio), seedFingerprint(manifest, [...audio].reverse()), "audio order-free");
  assert.equal(seedFingerprint(manifest, audio), seedFingerprint({ ...manifest, name: "Renamed" }, audio), "the name is left out");
  assert.notEqual(seedFingerprint(manifest, audio), seedFingerprint({ ...manifest, files: [{ ...manifest.files[0], durationMs: 451 }] }, audio), "durations count");
  assert.notEqual(seedFingerprint(manifest, audio), seedFingerprint({ ...manifest, recipe: "firefly-218" }, audio), "the recipe counts");
  assert.notEqual(seedFingerprint(manifest, audio), seedFingerprint(manifest, [{ ...audio[0], sha256: "3" }, audio[1]]), "audio bytes count");
});

test("CLI: usage errors exit 2, refusals exit 1, success prints a summary", async (t) => {
  const fx = fixture(t);
  const run = (...args) => spawnSync(process.execPath, [SCRIPT, ...args], { encoding: "utf8" });
  for (const args of [[], ["a", "b"], ["--out"], ["--bogus", "x"]]) {
    const result = run(...args);
    assert.equal(result.status, 2, `${args.join(" ")}: ${result.stderr}`);
    assert.match(result.stderr, /Usage: pnpm feel:import/);
  }
  const missing = run(path.join(fx.base, "nowhere"), "--out", fx.out);
  assert.equal(missing.status, 1, missing.stderr);
  assert.match(missing.stderr, /refused: staging keys-manifest\.json: not found.*\nNothing was changed\./s);
  const ok = run("--", fx.staging, "--out", fx.out);
  assert.equal(ok.status, 0, ok.stderr);
  assert.match(ok.stdout, /Typing Feel r1: 4 sets in 2 families, 65 audio files .* 3 labelled legacy-218\./);
  assert.match(ok.stdout, /set folders: 4 new, 0 unchanged/);
  const again = run(fx.staging, "--out", fx.out);
  assert.match(again.stdout, /set folders: 0 new, 4 unchanged/);
  assert.match(again.stdout, /keys-manifest\.json: unchanged/);
  assert.deepEqual(parseArgs(["--", "dir", "--revision", "r2"]), { revision: "r2", stagingDir: "dir" });
  let printed = "";
  assert.equal(await main(["--help"], { out: { write: (text) => { printed += text; } }, err: { write() {} } }), 0);
  assert.match(printed, /Usage/);
});
