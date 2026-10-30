// node --test tests/pack.test.mjs
// feel:pack (TYPING_FEEL_SERVICE.md §6.5, §8.1): a tiny public/v1 made by the
// importer from the synthetic staging of fixture.mjs (fake bytes, no media),
// packed into a temp folder, then broken one rule at a time.
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { existsSync, mkdirSync, readdirSync, readFileSync, rmSync, unlinkSync, writeFileSync } from "node:fs";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import { crc32, inflateRawSync } from "node:zlib";
import { importStaging } from "../tools/import-staging.mjs";
import { DEFAULT_OUT_DIR, main, pack, PackError, parseArgs } from "../tools/pack.mjs";
import { makeStaging, ROWS } from "./fixture.mjs";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const T1 = Date.UTC(2026, 9, 31, 9, 0, 0);

/** Staging → importer → public/v1 in a temp folder, plus an empty out folder. */
async function fixture(t) {
  const fx = makeStaging();
  t.after(fx.cleanup);
  await importStaging({ stagingDir: fx.staging, publicDir: fx.out, now: T1 });
  const outDir = path.join(fx.base, "pack");
  const v1 = path.join(fx.out, "v1");
  const catalogueFile = path.join(v1, "keys/keys-manifest.json");
  const catalogue = () => JSON.parse(readFileSync(catalogueFile, "utf8"));
  const setFolder = (id) => path.join(v1, "keys", path.dirname(catalogue().profiles.find((row) => row.id === id).manifest));
  const writeCatalogue = (value) => writeFileSync(catalogueFile, `${JSON.stringify(value, null, 2)}\n`);
  return { ...fx, outDir, v1, catalogue, setFolder, writeCatalogue };
}

/** The entries of a plain zip (what feel:mirror reads): name -> bytes, checked against CRC-32. */
function unzip(zip) {
  let end = zip.length - 22;
  while (end >= 0 && zip.readUInt32LE(end) !== 0x06054b50) end -= 1;
  assert.ok(end >= 0, "end of central directory");
  const count = zip.readUInt16LE(end + 10);
  let at = zip.readUInt32LE(end + 16);
  const files = new Map();
  for (let index = 0; index < count; index += 1) {
    assert.equal(zip.readUInt32LE(at), 0x02014b50);
    const flags = zip.readUInt16LE(at + 8);
    const method = zip.readUInt16LE(at + 10);
    const crc = zip.readUInt32LE(at + 16);
    const compressed = zip.readUInt32LE(at + 20);
    const size = zip.readUInt32LE(at + 24);
    const nameLength = zip.readUInt16LE(at + 28);
    const skip = nameLength + zip.readUInt16LE(at + 30) + zip.readUInt16LE(at + 32);
    const mode = zip.readUInt32LE(at + 38) >>> 16;
    const offset = zip.readUInt32LE(at + 42);
    const name = zip.subarray(at + 46, at + 46 + nameLength).toString("utf8");
    assert.equal(flags & 0x801, 0x800, `${name}: UTF-8 name, not encrypted`);
    assert.equal(mode, 0o100644, `${name}: a plain 0644 file`);
    const start = offset + 30 + zip.readUInt16LE(offset + 26) + zip.readUInt16LE(offset + 28);
    const raw = zip.subarray(start, start + compressed);
    const data = method === 8 ? inflateRawSync(raw) : raw;
    assert.equal(method, name.endsWith(".ogg") ? 0 : 8, `${name}: OGG stored, JSON deflated`);
    assert.equal(data.length, size);
    assert.equal(crc32(data), crc, `${name}: CRC-32`);
    files.set(name, Buffer.from(data));
    at += 46 + skip;
  }
  return files;
}

/** Every file under `dir` (relative path -> bytes). */
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

async function refusal(fx) {
  await assert.rejects(pack({ publicDir: fx.out, outDir: fx.outDir }), PackError);
  assert.equal(existsSync(fx.outDir), false, "nothing written on a refusal");
  try {
    await pack({ publicDir: fx.out, outDir: fx.outDir });
  } catch (error) {
    return error.problems.join("\n");
  }
  return "";
}

test("packs public/v1 as typing-feel-v1-<revision>.zip: every file under v1/, byte for byte", async (t) => {
  const fx = await fixture(t);
  const result = await pack({ publicDir: fx.out, outDir: fx.outDir });
  assert.equal(result.file, path.join(fx.outDir, "typing-feel-v1-r1.zip"));
  assert.equal(result.revision, "r1");
  assert.equal(result.sets, ROWS.length);
  const source = snapshot(fx.v1);
  const audio = [...source.keys()].filter((name) => name.endsWith(".ogg"));
  assert.equal(result.audio, audio.length);
  assert.equal(result.files, source.size);
  const zip = readFileSync(result.file);
  assert.equal(result.zipBytes, zip.length);
  const files = unzip(zip);
  assert.deepEqual([...files.keys()], [...source.keys()].map((name) => `v1/${name}`).sort());
  for (const [name, bytes] of source) assert.ok(files.get(`v1/${name}`).equals(bytes), name);
  assert.ok(files.has("v1/health.json"));
  assert.ok(files.has("v1/keys/keys-manifest.json"));
  // No temp file left beside it.
  assert.deepEqual(readdirSync(fx.outDir), ["typing-feel-v1-r1.zip"]);
});

test("the zip is deterministic: packing again writes the same bytes", async (t) => {
  const fx = await fixture(t);
  const first = await pack({ publicDir: fx.out, outDir: fx.outDir });
  const bytes = readFileSync(first.file);
  const second = await pack({ publicDir: fx.out, outDir: fx.outDir });
  assert.equal(second.sha256, first.sha256);
  assert.ok(readFileSync(second.file).equals(bytes));
});

test("the system unzip accepts the pack when it is installed", async (t) => {
  const fx = await fixture(t);
  const result = await pack({ publicDir: fx.out, outDir: fx.outDir });
  const probe = spawnSync("unzip", ["-tq", result.file], { encoding: "utf8" });
  if (probe.error) {
    t.skip("unzip is not installed");
    return;
  }
  assert.equal(probe.status, 0, probe.stdout + probe.stderr);
});

test("leaves out dot files and *.tmp an importer left, keeps the rest", async (t) => {
  const fx = await fixture(t);
  const folder = fx.setFolder("deep");
  mkdirSync(path.join(path.dirname(folder), ".incoming-0123456789ab-1"), { recursive: true });
  writeFileSync(path.join(path.dirname(folder), ".incoming-0123456789ab-1/key-01.ogg"), "half");
  writeFileSync(path.join(fx.v1, "keys/keys-manifest.json.42.tmp"), "{");
  writeFileSync(path.join(fx.v1, ".DS_Store"), "x");
  const result = await pack({ publicDir: fx.out, outDir: fx.outDir });
  const names = [...unzip(readFileSync(result.file)).keys()];
  assert.equal(names.some((name) => name.includes(".incoming-") || name.endsWith(".tmp") || name.endsWith(".DS_Store")), false);
  assert.equal(result.skipped.length, 3);
});

test("refuses a catalogue that lists no set", async (t) => {
  const fx = await fixture(t);
  fx.writeCatalogue({ ...fx.catalogue(), profiles: [] });
  assert.match(await refusal(fx), /lists no set/);
});

test("refuses a catalogue row that does not resolve or misses the kit's fields", async (t) => {
  const fx = await fixture(t);
  const catalogue = fx.catalogue();
  const [first, second, third] = catalogue.profiles.map((row) => row.id);
  catalogue.profiles[0].manifest = "../outside/keys-manifest.json";
  catalogue.profiles[1].preview = "sets/x/preview.ogg?v=2";
  catalogue.profiles[2].order = "3";
  catalogue.profiles[3].id = "off";
  fx.writeCatalogue(catalogue);
  const problems = await refusal(fx);
  assert.match(problems, new RegExp(`profiles\\[0\\] \\(${first}\\): manifest does not resolve \\(".." segment\\)`));
  assert.match(problems, new RegExp(`profiles\\[1\\] \\(${second}\\): preview does not resolve \\(contains "\\?"\\)`));
  assert.match(problems, new RegExp(`profiles\\[2\\] \\(${third}\\): order is not a number`));
  assert.match(problems, /profiles\[3\] \(off\): id is not a valid set id/);
});

test("refuses a duplicate id and a row whose manifest or preview is missing", async (t) => {
  const fx = await fixture(t);
  const catalogue = fx.catalogue();
  catalogue.profiles[2].id = catalogue.profiles[0].id;
  catalogue.profiles[1].manifest = `sets/${catalogue.profiles[1].id}/000000000000/keys-manifest.json`;
  fx.writeCatalogue(catalogue);
  unlinkSync(path.join(fx.setFolder("raindrop-tile"), "preview.ogg"));
  const problems = await refusal(fx);
  assert.match(problems, /duplicate id/);
  assert.match(problems, /manifest keys\/sets\/[a-z-]+\/000000000000\/keys-manifest\.json is missing/);
  assert.match(problems, /\(raindrop-tile\): preview keys\/sets\/raindrop-tile\/[0-9a-f]{12}\/preview\.ogg is missing/);
});

test("refuses a sample a set manifest names but the folder lacks", async (t) => {
  const fx = await fixture(t);
  unlinkSync(path.join(fx.setFolder("deep"), "key-02.ogg"));
  assert.match(await refusal(fx), /files\[1\]: keys\/sets\/deep\/[0-9a-f]{12}\/key-02\.ogg is missing/);
});

test("refuses an empty OGG, a file that is no OGG stream, and a JSON that does not parse", async (t) => {
  const fx = await fixture(t);
  writeFileSync(path.join(fx.setFolder("deep"), "key-03.ogg"), "");
  writeFileSync(path.join(fx.setFolder("deep"), "key-04.ogg"), "<!doctype html>");
  writeFileSync(path.join(fx.setFolder("deep-amber"), "keys-manifest.json"), "{ not json");
  const problems = await refusal(fx);
  assert.match(problems, /key-03\.ogg: empty OGG/);
  assert.match(problems, /key-04\.ogg: not an OGG stream/);
  assert.match(problems, /deep-amber\/[0-9a-f]{12}\/keys-manifest\.json: not JSON/);
});

test("refuses typing-game.local anywhere: in a JSON, inside audio bytes, in a path", async (t) => {
  const fx = await fixture(t);
  fx.writeCatalogue({ ...fx.catalogue(), note: "https://feel.typing-game.local/v1/" });
  writeFileSync(path.join(fx.setFolder("deep"), "key-05.ogg"), Buffer.concat([Buffer.from("OggS"), Buffer.from(" comment=https://feel.typing-game.local ")]));
  mkdirSync(path.join(fx.v1, "keys/typing-game.local"), { recursive: true });
  writeFileSync(path.join(fx.v1, "keys/typing-game.local/x.json"), "{}");
  const problems = await refusal(fx);
  assert.match(problems, /^keys\/keys-manifest\.json: contains "typing-game\.local"/m);
  assert.match(problems, /key-05\.ogg: contains "typing-game\.local"/);
  assert.match(problems, /keys\/typing-game\.local\/x\.json: contains "typing-game\.local"/);
});

test("refuses typing-game.local in any case, and spelt with JSON escapes", async (t) => {
  const fx = await fixture(t);
  const folder = fx.setFolder("deep");
  const manifest = JSON.parse(readFileSync(path.join(folder, "keys-manifest.json"), "utf8"));
  writeFileSync(path.join(folder, "keys-manifest.json"), JSON.stringify({ ...manifest, note: "https://feel.TYPING-GAME.LOCAL" }));
  writeFileSync(path.join(fx.v1, "keys/keys-manifest.json"), JSON.stringify(fx.catalogue()).replace(/^\{/, '{"note":"https://feel.\\u0074yping-game.local",'));
  const problems = await refusal(fx);
  assert.match(problems, /deep\/[0-9a-f]{12}\/keys-manifest\.json: contains "typing-game\.local"/);
  assert.match(problems, /^keys\/keys-manifest\.json: contains "typing-game\.local"/m);
  // One line per file, even when both its bytes and its parsed JSON match.
  assert.equal(problems.split("\n").filter((line) => /^keys\/sets\/deep\/.*: contains/.test(line)).length, 1);
});

test("refuses a row whose manifest is not its set manifest, or whose preview is not an OGG", async (t) => {
  const fx = await fixture(t);
  const catalogue = fx.catalogue();
  const [first, second, third] = catalogue.profiles;
  first.manifest = first.preview;
  second.manifest = third.manifest;
  third.preview = third.manifest;
  fx.writeCatalogue(catalogue);
  const problems = await refusal(fx);
  assert.match(problems, new RegExp(`\\(${first.id}\\): manifest keys/sets/${first.id}/[0-9a-f]{12}/preview\\.ogg is not a set manifest`));
  assert.match(problems, new RegExp(`\\(${second.id}\\): manifest keys/sets/${third.id}/[0-9a-f]{12}/keys-manifest\\.json is the set "${third.id}"`));
  assert.match(problems, new RegExp(`\\(${third.id}\\): preview keys/sets/${third.id}/[0-9a-f]{12}/keys-manifest\\.json is not an OGG`));
});

test("refuses other file types, a missing health.json and one of another revision", async (t) => {
  const fx = await fixture(t);
  writeFileSync(path.join(fx.setFolder("deep"), "take.wav"), "RIFF");
  writeFileSync(path.join(fx.v1, "health.json"), JSON.stringify({ contract: 1, revision: "r2", build: "x", builtAt: "y" }));
  let problems = await refusal(fx);
  assert.match(problems, /take\.wav: not a \.json or \.ogg file/);
  assert.match(problems, /health\.json: revision "r2" is not the catalogue's "r1"/);
  unlinkSync(path.join(fx.v1, "health.json"));
  problems = await refusal(fx);
  assert.match(problems, /health\.json: missing/);
});

test("refuses a missing v1 folder", async (t) => {
  const fx = await fixture(t);
  rmSync(fx.v1, { recursive: true });
  assert.match(await refusal(fx), /no v1 folder/);
});

test("CLI: refusals exit 1 and list the problems, success exits 0, bad usage exits 2", async (t) => {
  const fx = await fixture(t);
  const io = () => {
    const chunks = { out: "", err: "" };
    return { chunks, out: { write: (text) => (chunks.out += text) }, err: { write: (text) => (chunks.err += text) } };
  };
  let run = io();
  assert.equal(await main(["--public", fx.out, "--out", fx.outDir], run), 0);
  assert.match(run.chunks.out, /Typing Feel r1: 4 sets, \d+ files \(\d+ OGG, \d+ bytes\) -> .*typing-feel-v1-r1\.zip/);
  assert.match(run.chunks.out, /sha256 [0-9a-f]{64}/);
  fx.writeCatalogue({ ...fx.catalogue(), profiles: [] });
  rmSync(fx.outDir, { recursive: true });
  run = io();
  assert.equal(await main(["--public", fx.out, "--out", fx.outDir], run), 1);
  assert.match(run.chunks.err, /feel:pack refused \(1 problem\):\n {2}- keys\/keys-manifest\.json: lists no set\nNothing was written\./);
  assert.equal(existsSync(fx.outDir), false);
  run = io();
  assert.equal(await main(["--bogus"], run), 2);
  assert.equal(await main(["--out"], run), 2);
  assert.deepEqual(parseArgs(["--", "--out", "x"]), { outDir: "x" });
  // As a process: the exit code reaches the shell.
  const child = spawnSync(process.execPath, [path.join(ROOT, "tools/pack.mjs"), "--public", fx.out, "--out", fx.outDir], { encoding: "utf8" });
  assert.equal(child.status, 1, child.stdout + child.stderr);
});

test("the default output is the parent repo's tmp/typing-feel-pack, which Git ignores", (t) => {
  assert.equal(DEFAULT_OUT_DIR, path.resolve(ROOT, "..", "tmp", "typing-feel-pack"));
  const probe = spawnSync("git", ["-C", path.dirname(ROOT), "check-ignore", "-q", path.join(DEFAULT_OUT_DIR, "typing-feel-v1-r1.zip")]);
  if (probe.error || probe.status === 128) {
    t.skip("not in a Git work tree");
    return;
  }
  assert.equal(probe.status, 0, "tmp/typing-feel-pack/*.zip is ignored");
});
